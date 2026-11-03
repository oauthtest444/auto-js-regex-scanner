(async () => {
  const regex =
    /(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])([^'"`]+)\1\s*\)/g;

  const excluded = new Set([
    "left", "right", "top", "bottom",
    "width", "height", "x", "y",
    "type", "name", "length", "size",
    "index", "id", "class", "className",
    "style", "color", "position",
    "offset", "margin", "padding",
    "display", "direction", "align",
    "trigger", "series", "data"
  ]);

  const urls = new Set([
    ...[...document.scripts]
      .map(s => s.src)
      .filter(Boolean),

    ...performance
      .getEntriesByType("resource")
      .filter(r => r.initiatorType === "script")
      .map(r => r.name)
  ]);

  const fileResults = new Map();

  console.log(`Scanning ${urls.size} JavaScript resources...`);

  await Promise.allSettled(
    [...urls].map(async url => {
      try {
        const response = await fetch(url);
        if (!response.ok) return;

        const source = await response.text();
        const matches = new Set();

        for (const match of source.matchAll(regex)) {
          if (excluded.has(match[2])) continue;
          matches.add(match[0]);
        }

        if (matches.size > 0) {
          fileResults.set(url, [...matches]);
        }
      } catch (_) {}
    })
  );

  const sortedResults = [...fileResults.entries()]
    .sort((a, b) => b[1].length - a[1].length);

  const totalMatches = sortedResults.reduce(
    (sum, item) => sum + item[1].length, 0
  );

  // Build complete report
  let output = "";

  for (const [url, matches] of sortedResults) {
    output += `FILE: ${url}\n`;
    output += `MATCH COUNT: ${matches.length}\n`;
    output += `${"-".repeat(80)}\n`;

    for (const match of matches) {
      output += `  ${match}\n`;
    }

    output += "\n";
  }

  output += `${"=".repeat(80)}\n`;
  output += `FILES WITH MATCHES: ${sortedResults.length}\n`;
  output += `TOTAL UNIQUE FILE MATCHES: ${totalMatches}\n`;

  console.log(output);

  // Remove previous popup
  document.getElementById("regex-scan-results")?.remove();

  // Create popup
  const panel = document.createElement("div");

  panel.id = "regex-scan-results";

  panel.style.cssText = `
    position:fixed;
    top:20px;
    left:20px;
    width:85%;
    height:75%;
    z-index:2147483647;
    background:#fff;
    color:#111;
    border:3px solid #16a34a;
    border-radius:8px;
    padding:15px;
    box-shadow:0 5px 30px #0005;
    font:13px Arial;
  `;

  const heading = document.createElement("div");

  heading.textContent =
    `Files: ${sortedResults.length} | Unique matches: ${totalMatches}`;

  heading.style.cssText =
    "font-weight:bold;margin-bottom:10px;font-size:14px";

  // Results area
  const outputBox = document.createElement("textarea");

  outputBox.readOnly = true;
  outputBox.value = output;

  outputBox.style.cssText = `
    width:100%;
    height:calc(100% - 105px);
    box-sizing:border-box;
    padding:10px;
    background:#f8fafc;
    color:#111;
    font:12px monospace;
    resize:none;
    border:1px solid #aaa;
  `;

  // Button container
  const controls = document.createElement("div");

  controls.style.cssText =
    "display:flex;gap:10px;margin-top:10px";

  // Copy button
  const copyButton = document.createElement("button");

  copyButton.textContent = "Copy Results";

  copyButton.style.cssText = `
    padding:9px 20px;
    background:#16a34a;
    color:white;
    border:0;
    border-radius:5px;
    cursor:pointer;
    font-weight:bold;
  `;

  copyButton.onclick = async () => {
    try {
      await navigator.clipboard.writeText(output);
      copyButton.textContent = "Copied!";
    } catch (_) {
      outputBox.focus();
      outputBox.select();

      const copied = document.execCommand("copy");

      copyButton.textContent = copied
        ? "Copied!"
        : "Press Ctrl+C";

    }

    setTimeout(() => {
      copyButton.textContent = "Copy Results";
    }, 2000);
  };

  // Close button
  const closeButton = document.createElement("button");

  closeButton.textContent = "Close";

  closeButton.style.cssText = `
    padding:9px 20px;
    background:#555;
    color:white;
    border:0;
    border-radius:5px;
    cursor:pointer;
  `;

  closeButton.onclick = () => panel.remove();

  controls.append(copyButton, closeButton);

  panel.append(heading, outputBox, controls);

  document.body.appendChild(panel);

  console.log("FILES WITH MATCHES:", sortedResults.length);
  console.log("TOTAL UNIQUE FILE MATCHES:", totalMatches);

})(); 
