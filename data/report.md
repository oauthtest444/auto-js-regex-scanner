# JS Regex Scan - Route-First Report

- Generated: 2026-11-05 17:39:24 UTC
- Routes: 3 tested | 3 unique | 0 duplicate | 0 errors
- Route coverage: 3 with new app surface | 0 vendor-only | 0 with no new discoveries
- Files: 17 unique JS files | 17 raw file URLs | 0 cache-busted duplicates collapsed | 85 unique file-match texts (85 raw)
- Matches: 67 source | 18 sink | 4 URLSearchParams `.get` flagged | 51 unique texts
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP | Unscanned: 0
- Only unique route IDs are listed. Missing route numbers are duplicates mapped near the end.
- `.get` and `.query` source matches are unique by match text within each route. URL/URLSearchParams constructions and location sinks are per file and not deduped.
- Cache-busted duplicate URLs are collapsed by normalized URL (scheme + host + path).
- `App` = JavaScript served from the route's application bundle roots (for example `*/console-ark/*` or `*/console-datafinder/*`), plus legacy `src_`/`~src_` chunks. Vendor, runtime, locale, and SDK markers plus `vendors.txt` URL patterns mark vendor files, which are listed individually per route; all match texts are in the final per-file indexes.
- URLSearchParams `.get` classification uses a same-file constructor/alias heuristic; function-parameter and cross-file flows still need manual tracing.

## Unique Routes (One-Click Copy)

3 unique routes. Copy the complete block below; each line is a full unique route URL.

```text
https://console.byteplus.com/ark
https://console.byteplus.com/ark/region:ap-southeast-1/model
https://console.byteplus.com/ark/region:ap-southeast-1/model/detail
```

## Route 1 — https://console.byteplus.com/ark

- HTTP: 200 | Loaded: 13 files (9 app / 4 vendor) | New: 13 files (9 app / 4 vendor)
- New source matches: 24 app / 18 vendor | New location sinks: 12 app / 4 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/2184.1fa6f9e2e4.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6652.6caf14fb81.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>e.get("userInfo")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>e.get("vault_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
- <code>i.get("t")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>t.get("userInfo")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/2184.1fa6f9e2e4.js</code>
- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
- <code>n=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>r=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>n=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>t=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>
- <code>t=new URL(location.pathname</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>

#### Other `.get(...)` (10)

<details><summary>Show generic .get matches</summary>

- <code>I.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>e.collect.configManager.get("user")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>g.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>i.A.get("csrfToken")</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>i.configManager.get("user")</code> (x13) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>n.configManager.get("user")</code> (x14) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>p.searchParams.get("paths")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>
- <code>r.configManager.get("reportErrorCallback")</code> (x4) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>r.get("*")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code>
- <code>sC.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>location.assign(</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>window.location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>window.location.replace(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>location.assign(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>
- <code>location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>
- <code>window.location.href=</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
- <code>window.location.assign(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
- <code>window.location.assign(</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6652.6caf14fb81.js</code>
- <code>window.location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>

### Vendor JS files (included by -v)

- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime-os/main.cea8b975.js</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>oH.get("_TEA_VE_APIHOST")</code>
  - [source] <code>oH.get("_VISUAL_EDITOR_U")</code>
  - [source] <code>oH.get("_VISUAL_EDITOR_V")</code>
  - [source] <code>oH.get("lang")</code>
  - [source] <code>r.configManager.get("user")</code> (x6)
  - [source] <code>t.get("AccountID")</code>
  - [source] <code>t.get("__spti")</code>
  - [source] <code>t.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x2)
  - [sink] <code>window.location.href=</code> (x4)
  - [sink] <code>window.location.replace(</code>

- <code>https://res.gcloudcache.com/bp-fe/finance/volcf-sdk-app/static/js/577.ff151c5d.js</code>
  - [source] <code>I.A.get("csrfToken")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>o.configManager.get("user")</code> (x6)

- <code>https://res.gcloudcache.com/volc-fe/account-onboarding-app/static/js/main.d4898c72.js</code>
  - [source] <code>et.A.get("csrfToken")</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>

- <code>https://res.gcloudcache.com/volc-fe/kyc-modal-app/static/js/async/671.ff467394.js</code>
  - [source] <code>H7e.get("user_locale")</code> (x2)
  - [source] <code>U7e.get("csrfToken")</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.href=</code>

## Route 2 — https://console.byteplus.com/ark/region:ap-southeast-1/model

- HTTP: 200 | Loaded: 14 files (10 app / 4 vendor) | New: 3 files (3 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 2 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>

### App source matches (unique)

#### `.query.*` / `query["..."]`

- <code>.query.trim</code> (x4) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
- <code>d=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
- <code>window.location.assign(</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>

## Route 3 — https://console.byteplus.com/ark/region:ap-southeast-1/model/detail

- HTTP: 200 | Loaded: 14 files (10 app / 4 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>
- <code>l=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>

## Unique Routes With No New Discoveries

None.

## All source and sink matches, unique per file (app)

<details><summary>All source and sink matches, unique per file (app)</summary>

- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
  - [sink] <code>window.location.assign(</code> (x2)
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code>
  - [source] <code>r.get("*")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/2184.1fa6f9e2e4.js</code>
  - [source] <code>a=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6652.6caf14fb81.js</code>
  - [sink] <code>window.location.assign(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
  - [source] <code>e.get("vault_id")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x12)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x4)
  - [source] <code>e.configManager.get("web_id")</code> (x12)
  - [source] <code>g.A.get("csrfToken")</code>
  - [source] <code>i.configManager.get("user")</code> (x13)
  - [source] <code>n.configManager.get("user")</code> (x14)
  - [source] <code>r.configManager.get("reportErrorCallback")</code> (x4)
  - [source] <code>n=new URL(window.location.href</code>
  - [source] <code>r=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>location.assign(</code> (x3)
  - [sink] <code>window.location.href=</code> (x2)
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
  - [source] <code>I.A.get("csrfToken")</code>
  - [source] <code>e.get("userInfo")</code> (x2)
  - [source] <code>i.A.get("csrfToken")</code> (x3)
  - [source] <code>i.get("t")</code>
  - [source] <code>sC.A.get("csrfToken")</code>
  - [source] <code>t.get("userInfo")</code> (x2)
  - [source] <code>e=new URL(window.location.href</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>n=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URLSearchParams(location.search</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.href=</code>
  - [sink] <code>window.location.replace(</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>
  - [source] <code>p.searchParams.get("paths")</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [source] <code>t=new URL(location.pathname</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.replace(</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [source] <code>l=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
  - [source] <code>a=new URL(window.location.href</code>
  - [source] <code>d=new URL(window.location.href</code>
  - [sink] <code>window.location.assign(</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("user")</code> (x7)
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
  - [source] <code>.query.trim</code> (x4)

</details>

## All source and sink matches, unique per file (vendor)

<details><summary>All source and sink matches, unique per file (vendor)</summary>

- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime-os/main.cea8b975.js</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>oH.get("_TEA_VE_APIHOST")</code>
  - [source] <code>oH.get("_VISUAL_EDITOR_U")</code>
  - [source] <code>oH.get("_VISUAL_EDITOR_V")</code>
  - [source] <code>oH.get("lang")</code>
  - [source] <code>r.configManager.get("user")</code> (x6)
  - [source] <code>t.get("AccountID")</code>
  - [source] <code>t.get("__spti")</code>
  - [source] <code>t.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x2)
  - [sink] <code>window.location.href=</code> (x4)
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/finance/volcf-sdk-app/static/js/577.ff151c5d.js</code>
  - [source] <code>I.A.get("csrfToken")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>o.configManager.get("user")</code> (x6)
- <code>https://res.gcloudcache.com/volc-fe/account-onboarding-app/static/js/main.d4898c72.js</code>
  - [source] <code>et.A.get("csrfToken")</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/kyc-modal-app/static/js/async/671.ff467394.js</code>
  - [source] <code>H7e.get("user_locale")</code> (x2)
  - [source] <code>U7e.get("csrfToken")</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.href=</code>

</details>

## Vendor-Only Routes

None.

## Duplicate Routes

No routes were skipped as duplicate results.

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
