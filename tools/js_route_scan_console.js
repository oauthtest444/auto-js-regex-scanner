(async () => {
  'use strict';

  const REGEXES = [
    {
      id: 1,
      pattern: /(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])[^'"`]+\1\s*\)/g
    },
    {
      id: 2,
      pattern: /(?<![=!<>])(?:\b[A-Za-z_$][\w$]*\s*=\s*)new\s+(?:URLSearchParams|URL)\s*\(\s*(?:(?:window\.)?location\.(?:search|href|hash|pathname)|document\.(?:URL|URLUnencoded|baseURI))\b/g
    },
    {
      id: 3,
      pattern: /\.query\s*\.\s*[A-Za-z_$][\w$]*|\bquery\s*\[\s*['"][^'"]+['"]\s*\]/g
    },
    {
      id: 4,
      pattern: /(?:(?:window\.)?location\.(?:assign|replace)\s*\(\s*(?![`'"]|\$\{|window\.location\.|location\.|\w+\.href)|(?<![\w$.])(?:window\.|document\.|parent\.|top\.|self\.|frames\[\d+\].)??location(?:\.href)?\s*=\s*(?!=)\s*(?![\w$]+(?:\.[\w$]+)*\.href\b)(?![\w$]+(?:\.[\w$]+)*\.toString\(\))(?![`'"]|`\/|""\.concat|null\b|\{)(?!\(null\s*==[\s\S]*?this\.location[\s\S]*?\.toString\(\))(?!\(0\s*,\s*[\w$]+\.[\w$]+\)\s*\())/g
    }
  ];

  const GET_KEY_PATTERN = /\.get\(\s*(['"`])([^'"`]+)\1\s*\)/;
  const GET_RECEIVER_PATTERN = /([A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*)\.get\(/;
  const URLSP_ASSIGN_PATTERN = /(?:(?:const|let|var)\s+)?([A-Za-z_$][\w$]*)\s*=\s*new\s+URLSearchParams\s*\(/g;
  const URL_SEARCHPARAMS_ASSIGN_PATTERN = /(?:(?:const|let|var)\s+)?([A-Za-z_$][\w$]*)\s*=\s*new\s+URL\s*\([^)]*\)\s*\.searchParams/g;
  const DIRECT_URLSP_GET_PATTERN = /new\s+URLSearchParams\s*\([^)]*\)\s*\.get\(/;
  const DIRECT_URL_SEARCHPARAMS_GET_PATTERN = /new\s+URL\s*\([^)]*\)\s*\.searchParams\s*\.get\(/;

  const REGEX_2_EXCLUDED_PARAM_NAMES = new Set([
    'left', 'right', 'top', 'bottom',
    'width', 'height', 'x', 'y',
    'type', 'name', 'length', 'size',
    'index', 'id', 'class', 'className',
    'style', 'color', 'position',
    'offset', 'margin', 'padding',
    'display', 'direction', 'align',
    'trigger', 'series', 'data'
  ]);

  const DEFAULT_EXCLUDED_MATCH_PATTERNS = [
    /\bheaders?\s*\.\s*get\s*\(/i,
    /\b(?:cache|storage|registry)\s*\.\s*get\s*\(/i
  ];

  const extraExcludes = Array.isArray(globalThis.__JS_ROUTE_SCAN_EXCLUDES__)
    ? globalThis.__JS_ROUTE_SCAN_EXCLUDES__.map((source) => {
        try {
          return new RegExp(source);
        } catch (error) {
          return null;
        }
      }).filter(Boolean)
    : [];

  const EXCLUDED_MATCH_PATTERNS = DEFAULT_EXCLUDED_MATCH_PATTERNS.concat(extraExcludes);
  const EXCLUDED_URL_PATTERN = /^(?:data|blob|chrome-extension|devtools|chrome|edge|about|view-source):/i;
  const FETCH_TIMEOUT_MS = 30000;
  const SCAN_DEADLINE_MS = 120000;
  const CONCURRENCY = 8;

  function isJavaScriptUrl(value) {
    const url = String(value || '').trim();
    if (!url) return false;
    if (EXCLUDED_URL_PATTERN.test(url)) return false;
    const path = url.split('?')[0].split('#')[0].toLowerCase();
    if (path.endsWith('.map')) return false;
    return true;
  }

  function collectScriptUrls() {
    const urls = new Set();

    document.querySelectorAll('script[src]').forEach((script) => {
      try {
        const url = new URL(script.src, location.href).href;
        if (isJavaScriptUrl(url)) urls.add(url);
      } catch (error) {
        return;
      }
    });

    for (const entry of performance.getEntriesByType('resource')) {
      if (entry.initiatorType !== 'script') continue;
      if (isJavaScriptUrl(entry.name)) urls.add(entry.name);
    }

    return Array.from(urls);
  }

  function collectUrlspAliases(source) {
    const aliases = new Set();
    for (const pattern of [URLSP_ASSIGN_PATTERN, URL_SEARCHPARAMS_ASSIGN_PATTERN]) {
      pattern.lastIndex = 0;
      let match;
      while ((match = pattern.exec(source)) !== null) {
        aliases.add(match[1]);
      }
    }
    return aliases;
  }

  function isUrlspGet(source, text, start, aliases) {
    const receiverMatch = GET_RECEIVER_PATTERN.exec(text);
    if (receiverMatch && aliases.has(receiverMatch[1])) return true;
    const prefix = source.slice(Math.max(0, start - 400), start) + text;
    return DIRECT_URLSP_GET_PATTERN.test(prefix)
      || DIRECT_URL_SEARCHPARAMS_GET_PATTERN.test(prefix);
  }

  function scanText(source) {
    const uniqueMatches = new Map();
    const urlspAliases = collectUrlspAliases(source);

    for (const regex of REGEXES) {
      regex.pattern.lastIndex = 0;
      let match;
      while ((match = regex.pattern.exec(source)) !== null) {
        const matchedText = match[0];
        if (!matchedText) {
          regex.pattern.lastIndex += 1;
          continue;
        }
        if (EXCLUDED_MATCH_PATTERNS.some((pattern) => pattern.test(matchedText))) continue;
        let urlsp = false;
        if (regex.id === 1) {
          const keyMatch = GET_KEY_PATTERN.exec(matchedText);
          if (keyMatch && REGEX_2_EXCLUDED_PARAM_NAMES.has(keyMatch[2])) continue;
          urlsp = isUrlspGet(source, matchedText, match.index, urlspAliases);
        }

        const key = `${regex.id}\u0000${matchedText}`;
        const existing = uniqueMatches.get(key);
        if (existing) {
          existing.count += 1;
          existing.urlsp = Boolean(existing.urlsp || urlsp);
        } else {
          uniqueMatches.set(key, {
            regex: regex.id,
            text: matchedText,
            count: 1,
            urlsp
          });
        }
      }
    }

    return Array.from(uniqueMatches.values());
  }

  async function fetchSource(url, deadline) {
    if (Date.now() >= deadline) throw new Error('scan deadline exceeded');

    const controller = new AbortController();
    const remaining = Math.max(1000, deadline - Date.now());
    const timer = setTimeout(() => controller.abort(), Math.min(FETCH_TIMEOUT_MS, remaining));

    try {
      const response = await fetch(url, {
        cache: 'force-cache',
        credentials: 'same-origin',
        signal: controller.signal
      });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return await response.text();
    } finally {
      clearTimeout(timer);
    }
  }

  async function mapLimit(items, limit, worker) {
    const results = new Array(items.length);
    let nextIndex = 0;

    async function run() {
      while (true) {
        const index = nextIndex;
        nextIndex += 1;
        if (index >= items.length) return;
        results[index] = await worker(items[index], index);
      }
    }

    const workers = Array.from({ length: Math.min(limit, items.length) }, run);
    await Promise.all(workers);
    return results;
  }

  function buildReportText(urls, files, summary) {
    const lines = [];
    const matchedFiles = files.filter((file) => file.matches.length > 0);

    for (const file of matchedFiles) {
      lines.push(`FILE: ${file.url}`);
      lines.push(`MATCH COUNT: ${file.matches.length}`);
      lines.push('-'.repeat(80));
      for (const match of file.matches) {
        lines.push(`  [Regex ${match.regex}] ${match.text}`);
      }
      lines.push('');
    }

    lines.push('='.repeat(80));
    lines.push(`FILES WITH MATCHES: ${summary.filesWithMatches}`);
    lines.push(`TOTAL UNIQUE FILE MATCHES: ${summary.totalUniqueFileMatches}`);
    return lines.join('\n');
  }

  async function copyText(text) {
    try {
      await navigator.clipboard.writeText(text);
      return true;
    } catch (error) {
      const textarea = document.createElement('textarea');
      textarea.value = text;
      textarea.style.position = 'fixed';
      textarea.style.opacity = '0';
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      let copied = false;
      try {
        copied = document.execCommand('copy');
      } catch (copyError) {
        copied = false;
      }
      textarea.remove();
      return copied;
    }
  }

  function showPopup(reportText, summary) {
    const existing = document.getElementById('js-route-scan-overlay');
    if (existing) existing.remove();

    const overlay = document.createElement('div');
    overlay.id = 'js-route-scan-overlay';
    overlay.style.cssText = 'position:fixed;inset:0;z-index:2147483647;background:rgba(0,0,0,.55);display:flex;align-items:center;justify-content:center;padding:24px;box-sizing:border-box;';

    const panel = document.createElement('div');
    panel.style.cssText = 'width:min(1100px,96vw);height:min(820px,92vh);background:#111827;color:#e5e7eb;border:1px solid #374151;border-radius:10px;display:flex;flex-direction:column;font-family:system-ui,-apple-system,Segoe UI,sans-serif;box-shadow:0 24px 70px rgba(0,0,0,.55);overflow:hidden;';

    const header = document.createElement('div');
    header.style.cssText = 'display:flex;align-items:center;justify-content:space-between;gap:12px;padding:14px 18px;border-bottom:1px solid #374151;background:#0f172a;';

    const title = document.createElement('div');
    title.textContent = 'JS Route Regex Scan';
    title.style.cssText = 'font-size:16px;font-weight:700;';

    const stats = document.createElement('div');
    stats.textContent = `Files with matches: ${summary.filesWithMatches} | Total unique file matches: ${summary.totalUniqueFileMatches}`;
    stats.style.cssText = 'font-size:12px;color:#93c5fd;';

    const titleWrap = document.createElement('div');
    titleWrap.appendChild(title);
    titleWrap.appendChild(stats);

    const closeButton = document.createElement('button');
    closeButton.type = 'button';
    closeButton.textContent = 'Close';
    closeButton.style.cssText = 'border:1px solid #4b5563;background:#1f2937;color:#e5e7eb;border-radius:6px;padding:8px 14px;cursor:pointer;font-size:13px;';
    closeButton.addEventListener('click', () => overlay.remove());

    header.appendChild(titleWrap);
    header.appendChild(closeButton);

    const pre = document.createElement('pre');
    pre.textContent = reportText;
    pre.style.cssText = 'flex:1;margin:0;padding:16px 18px;overflow:auto;white-space:pre-wrap;word-break:break-word;font:12px/1.5 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;';

    const actions = document.createElement('div');
    actions.style.cssText = 'display:flex;gap:10px;justify-content:flex-end;padding:12px 18px;border-top:1px solid #374151;background:#0f172a;';

    const copyButton = document.createElement('button');
    copyButton.type = 'button';
    copyButton.textContent = 'Copy results';
    copyButton.style.cssText = 'border:1px solid #2563eb;background:#1d4ed8;color:#fff;border-radius:6px;padding:8px 14px;cursor:pointer;font-size:13px;';
    copyButton.addEventListener('click', async () => {
      const copied = await copyText(reportText);
      copyButton.textContent = copied ? 'Copied' : 'Copy failed';
      setTimeout(() => {
        copyButton.textContent = 'Copy results';
      }, 1500);
    });

    const bottomCloseButton = document.createElement('button');
    bottomCloseButton.type = 'button';
    bottomCloseButton.textContent = 'Close';
    bottomCloseButton.style.cssText = closeButton.style.cssText;
    bottomCloseButton.addEventListener('click', () => overlay.remove());

    actions.appendChild(copyButton);
    actions.appendChild(bottomCloseButton);
    panel.appendChild(header);
    panel.appendChild(pre);
    panel.appendChild(actions);
    overlay.appendChild(panel);
    document.documentElement.appendChild(overlay);
  }

  globalThis.__JS_ROUTE_SCANNER_SCAN_TEXT__ = scanText;

  const startedAt = Date.now();
  const deadline = startedAt + SCAN_DEADLINE_MS;
  const urls = collectScriptUrls();

  console.log(`Scanning ${urls.length} JavaScript resources...`);

  const files = await mapLimit(urls, CONCURRENCY, async (url) => {
    try {
      const source = await fetchSource(url, deadline);
      return {
        url,
        ok: true,
        error: null,
        source: 'browser-fetch',
        matches: scanText(source)
      };
    } catch (error) {
      const message = error && error.name === 'AbortError'
        ? 'fetch timeout'
        : String((error && error.message) || error);
      return {
        url,
        ok: false,
        error: message,
        source: null,
        matches: []
      };
    }
  });

  const summary = {
    filesCollected: files.length,
    filesWithMatches: files.filter((file) => file.matches.length > 0).length,
    totalUniqueFileMatches: files.reduce((total, file) => total + file.matches.length, 0),
    fetchFailures: files.filter((file) => !file.ok).length,
    durationMs: Date.now() - startedAt
  };

  const reportText = buildReportText(urls, files, summary);
  console.log(reportText);
  showPopup(reportText, summary);

  const result = {
    pageUrl: location.href,
    title: document.title,
    files,
    summary
  };

  globalThis.__JS_ROUTE_SCANNER_LAST__ = result;
  return result;
})();
