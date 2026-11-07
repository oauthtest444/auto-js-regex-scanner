# JS Regex Scan - Route-First Report

- Generated: 2026-11-07 03:36:31 UTC
- Routes: 55 tested | 1 unique | 54 duplicate | 0 errors
- Route coverage: 1 with new app surface | 0 vendor-only | 0 with no new discoveries
- Files: 9 unique JS files | 9 raw file URLs | 0 cache-busted duplicates collapsed | 68 unique file-match texts (68 raw)
- Matches: 55 source | 13 sink | 7 URLSearchParams `.get` flagged | 49 unique texts
- Wait: 10s | Timeout: 20s | Recoveries: 55 network / 0 HTTP | Unscanned: 0
- Only unique route IDs are listed. Missing route numbers are duplicates mapped near the end.
- `.get` and `.query` source matches are unique by match text within each route. URL/URLSearchParams constructions and location sinks are per file and not deduped.
- Cache-busted duplicate URLs are collapsed by normalized URL (scheme + host + path).
- `App` = JavaScript served from the route's application bundle roots (for example `*/console-ark/*` or `*/console-datafinder/*`), plus legacy `src_`/`~src_` chunks. Vendor, runtime, locale, and SDK markers plus `vendors.txt` URL patterns mark vendor files, which are counted per route but not listed individually in route sections; all match texts are in the final per-file indexes.
- URLSearchParams `.get` classification uses a same-file constructor/alias heuristic; function-parameter and cross-file flows still need manual tracing.

## Unique Routes (One-Click Copy)

1 unique route. Copy the complete block below; each line is a full unique route URL.

```text
https://console.byteplus.com/ai
```

## Route 1 — https://console.byteplus.com/ai

- HTTP: 200 | Loaded: 9 files (4 app / 5 vendor) | New: 9 files (4 app / 5 vendor)
- New source matches: 16 app / 27 vendor | New location sinks: 7 app / 6 vendor
- Note: final URL: https://signin.byteplus.com/auth/login?redirectURI=https%3A%2F%2Fconsole.byteplus.com%2Fai

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/1669.231a13e5.js</code>
- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/3018.68d9667e.js</code>
- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/4845.0afff8dd.js</code>
- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>e.get("fs_origin")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>e.get("fs_request_id")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>e.get("theme")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>n.get("fs_origin")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>t.get("fs_origin")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>t.get("redirectURI")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>t.get("theme")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>

#### Other `.get(...)` (9)

<details><summary>Show generic .get matches</summary>

- <code>e.collect.configManager.get("user")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>e.configManager.get("user_unique_id")</code> (x6) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>e.configManager.get("user_unique_id_type")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>e.configManager.get("web_id")</code> (x6) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>i.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>n.searchParams.get("fs_audiences")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>n.searchParams.get("fs_origin")</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>o.configManager.get("user")</code> (x13) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>r.configManager.get("reportErrorCallback")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.assign(</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>location.assign(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>window.location.href=</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>window.location.replace(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/4845.0afff8dd.js</code>
- <code>location.replace(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/3018.68d9667e.js</code>
- <code>window.location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/1669.231a13e5.js</code>

## Unique Routes With No New Discoveries

None.

## All source and sink matches, unique per file (app)

<details><summary>All source and sink matches, unique per file (app)</summary>

- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/1669.231a13e5.js</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/3018.68d9667e.js</code>
  - [sink] <code>location.replace(</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/async/4845.0afff8dd.js</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/bp-fe/vconsole-auth/byteplus/static/js/1.0.0.2917/main.bbfb9c4e.js</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x6)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x2)
  - [source] <code>e.configManager.get("web_id")</code> (x6)
  - [source] <code>e.get("fs_origin")</code>
  - [source] <code>e.get("fs_request_id")</code>
  - [source] <code>e.get("theme")</code>
  - [source] <code>i.A.get("csrfToken")</code>
  - [source] <code>n.get("fs_origin")</code>
  - [source] <code>n.searchParams.get("fs_audiences")</code>
  - [source] <code>n.searchParams.get("fs_origin")</code>
  - [source] <code>o.configManager.get("user")</code> (x13)
  - [source] <code>r.configManager.get("reportErrorCallback")</code> (x2)
  - [source] <code>t.get("fs_origin")</code>
  - [source] <code>t.get("redirectURI")</code>
  - [source] <code>t.get("theme")</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>window.location.assign(</code> (x3)
  - [sink] <code>window.location.href=</code> (x2)
  - [sink] <code>window.location.replace(</code> (x2)

</details>

## All source and sink matches, unique per file (vendor)

<details><summary>All source and sink matches, unique per file (vendor)</summary>

- <code>https://accounts.google.com/gsi/client</code>
  - [source] <code>_.Tc.get("g_state")</code>
  - [source] <code>a.P.get("ll")</code>
  - [source] <code>a.h.get("onTokenRefresh")</code>
  - [sink] <code>location=</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/async.66010596.js</code>
  - [source] <code>c.Z.get("__tea_cache_tokens_3569")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>i.configManager.get("reportErrorCallback")</code>
  - [source] <code>n.configManager.get("user")</code> (x6)
  - [source] <code>t7.get("_TEA_VE_APIHOST")</code>
  - [source] <code>t7.get("_VISUAL_EDITOR_U")</code>
  - [source] <code>t7.get("_VISUAL_EDITOR_V")</code>
  - [source] <code>t7.get("lang")</code>
  - [sink] <code>window.location.href=</code> (x2)
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code>
  - [source] <code>i.Z.get("__spti")</code>
  - [source] <code>rb.Z.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x3)
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/volcengine-arch-platform/827.4ec81f7aa59a70bf.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>el.A.get("signin_i18next")</code> (x2)
  - [source] <code>el.A.get("user_locale")</code>
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>o.configManager.get("user")</code> (x7)
- <code>https://res.gcloudcache.com/bp-fe/volcengine-arch-platform/bp.4ec81f7aa59a70bf.js</code>
  - [source] <code>V.get("_TEA_VE_APIHOST")</code>
  - [source] <code>V.get("_VISUAL_EDITOR_U")</code>
  - [source] <code>V.get("_VISUAL_EDITOR_V")</code>
  - [source] <code>V.get("lang")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>i.A.get("__spti")</code>
  - [source] <code>i.A.get("__tea_cache_tokens_3569")</code>
  - [source] <code>i.configManager.get("user")</code> (x6)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.A.get("csrfToken")</code>
  - [source] <code>t=new URL(window.location.href</code>
  - [sink] <code>window.location.href=</code> (x2)
  - [sink] <code>window.location.replace(</code>

</details>

## Vendor-Only Routes

None.

## Duplicate Routes

54 duplicate routes produced no new JS files, source matches, or location sinks.

- Route 1 source; duplicates: 2-55

## Errors

None.

<details><summary>Regex patterns and exclusions</summary>

Regex 1 (`.get(...)`):

```regex
(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])[^'"`]+\1\s*\)
```

Regex 2 (URL / URLSearchParams construction):

```regex
(?<![=!<>])(?:\b[A-Za-z_$][\w$]*\s*=\s*)new\s+(?:URLSearchParams|URL)\s*\(\s*(?:(?:window\.)?location\.(?:search|href|hash|pathname)|document\.(?:URL|URLUnencoded|baseURI))\b
```

Regex 3 (`.query.*` / `query["..."]`):

```regex
\.query\s*\.\s*[A-Za-z_$][\w$]*|\bquery\s*\[\s*['"][^'"]+['"]\s*\]
```

Regex 4 (location sink):

```regex
(?:(?:window\.)?location\.(?:assign|replace)\s*\(\s*(?![`'"]|\$\{|window\.location\.|location\.|\w+\.href)|(?<![\w$.])(?:window\.|document\.|parent\.|top\.|self\.|frames\[\d+\].)??location(?:\.href)?\s*=\s*(?!=)\s*(?![\w$]+(?:\.[\w$]+)*\.href\b)(?![\w$]+(?:\.[\w$]+)*\.toString\(\))(?![`'"]|`\/|""\.concat|null\b|\{)(?!\(null\s*==[\s\S]*?this\.location[\s\S]*?\.toString\(\))(?!\(0\s*,\s*[\w$]+\.[\w$]+\)\s*\())
```

Default match exclusions:

- <code>\bheaders?\s*\.\s*get\s*\(</code>
- <code>\b(?:cache&#124;storage&#124;registry)\s*\.\s*get\s*\(</code>

Excluded `.get` parameter names:

`align`, `bottom`, `class`, `className`, `color`, `data`, `direction`, `display`, `height`, `id`, `index`, `left`, `length`, `margin`, `name`, `offset`, `padding`, `position`, `right`, `series`, `size`, `style`, `top`, `trigger`, `type`, `width`, `x`, `y`

</details>
