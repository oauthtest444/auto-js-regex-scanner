# JS Regex Scan - Route-First Report

- Generated: 2026-11-05 19:22:18 UTC
- Routes: 153 tested | 78 unique | 75 duplicate | 0 errors
- Route coverage: 56 with new app surface | 2 vendor-only | 20 with no new discoveries
- Files: 169 unique JS files | 169 raw file URLs | 0 cache-busted duplicates collapsed | 903 unique file-match texts (903 raw)
- Matches: 806 source | 97 sink | 18 URLSearchParams `.get` flagged | 467 unique texts
- Wait: 10s | Timeout: 20s | Recoveries: 3 network / 0 HTTP | Unscanned: 0
- Only unique route IDs are listed. Missing route numbers are duplicates mapped near the end.
- `.get` and `.query` source matches are unique by match text within each route. URL/URLSearchParams constructions and location sinks are per file and not deduped.
- Cache-busted duplicate URLs are collapsed by normalized URL (scheme + host + path).
- `App` = JavaScript served from the route's application bundle roots (for example `*/console-ark/*` or `*/console-datafinder/*`), plus legacy `src_`/`~src_` chunks. Vendor, runtime, locale, and SDK markers plus `vendors.txt` URL patterns mark vendor files, which are counted per route but not listed individually in route sections; all match texts are in the final per-file indexes.
- URLSearchParams `.get` classification uses a same-file constructor/alias heuristic; function-parameter and cross-file flows still need manual tracing.

## Unique Routes (One-Click Copy)

78 unique routes. Copy the complete block below; each line is a full unique route URL.

```text
https://console.byteplus.com/ark
https://console.byteplus.com/ark/region:ap-southeast-1
https://console.byteplus.com/ark/region:ap-southeast-1/model
https://console.byteplus.com/ark/region:ap-southeast-1/model/detail
https://console.byteplus.com/ark/region:ap-southeast-1/model/comparison
https://console.byteplus.com/ark/region:ap-southeast-1/model/leaderboard
https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/ip-letter-download
https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/promotion/*
https://console.byteplus.com/ark/region:ap-southeast-1/promotion/*
https://console.byteplus.com/ark/region:ap-southeast-1/pickupVoucher
https://console.byteplus.com/ark/region:ap-southeast-1/gallery
https://console.byteplus.com/ark/region:ap-southeast-1/gallery/*
https://console.byteplus.com/ark/region:ap-southeast-1/experience
https://console.byteplus.com/ark/region:ap-southeast-1/experience/creations
https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_image
https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_video
https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_3d
https://console.byteplus.com/ark/region:ap-southeast-1/experience/voice
https://console.byteplus.com/ark/region:ap-southeast-1/experience/claw
https://console.byteplus.com/ark/region:ap-southeast-1/experience/ma/:presetKey
https://console.byteplus.com/ark/region:ap-southeast-1/experience/share/:id
https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_video/:id
https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_canvas/:id
https://console.byteplus.com/ark/region:ap-southeast-1/endpoint
https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/create
https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/detail
https://console.byteplus.com/ark/region:ap-southeast-1/batchInference
https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/create
https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/detail
https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/batchEpDetail
https://console.byteplus.com/ark/region:ap-southeast-1/ipDashboard/*
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/quickstart
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/create
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/:id
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/create
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/:id
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/environments
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault/:id
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault-oauth/callback
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills/:id
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/memory
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/create
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/:id
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create-deprecated
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/detail
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/comparison
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/tls
https://console.byteplus.com/ark/region:ap-southeast-1/customModel/detail
https://console.byteplus.com/ark/region:ap-southeast-1/eval/create
https://console.byteplus.com/ark/region:ap-southeast-1/eval/detail
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/create
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/detail
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/version/create
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/dump/create
https://console.byteplus.com/ark/region:ap-southeast-1/tts/speechRecognition
https://console.byteplus.com/ark/region:ap-southeast-1/application
https://console.byteplus.com/ark/region:ap-southeast-1/application/doubaoAPI
https://console.byteplus.com/ark/region:ap-southeast-1/application/claw
https://console.byteplus.com/ark/region:ap-southeast-1/application/detail
https://console.byteplus.com/ark/region:ap-southeast-1/assistant
https://console.byteplus.com/ark/region:ap-southeast-1/assistant/edit
https://console.byteplus.com/ark/region:ap-southeast-1/assistant/detail
https://console.byteplus.com/ark/region:ap-southeast-1/knowledge
https://console.byteplus.com/ark/region:ap-southeast-1/subscription/coding-plan
https://console.byteplus.com/ark/region:ap-southeast-1/openManagement
https://console.byteplus.com/ark/region:ap-southeast-1/openManagement/rewardPlan
https://console.byteplus.com/ark/region:ap-southeast-1/apiKey
https://console.byteplus.com/ark/region:ap-southeast-1/usageTracking
https://console.byteplus.com/ark/region:ap-southeast-1/vpc
https://console.byteplus.com/ark/region:ap-southeast-1/projectManagement
https://console.byteplus.com/ark/region:ap-southeast-1/tokenCalculator
https://console.byteplus.com/ark/region:ap-southeast-1/docs
https://console.byteplus.com/ark/region:ap-southeast-1/arkcli
```

## Route 1 — https://console.byteplus.com/ark

- HTTP: 200 | Loaded: 13 files (8 app / 5 vendor) | New: 13 files (8 app / 5 vendor)
- New source matches: 23 app / 21 vendor | New location sinks: 11 app / 6 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/overview

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/2184.1fa6f9e2e4.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6652.6caf14fb81.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>e.get("userInfo")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>i.get("t")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>
- <code>t.get("userInfo")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/2184.1fa6f9e2e4.js</code>
- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
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

## Route 2 — https://console.byteplus.com/ark/region:ap-southeast-1

- HTTP: 200 | Loaded: 14 files (9 app / 5 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/overview

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/exp-center/vmok-remote-entry.e54a3014.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/exp-center/vmok-remote-entry.e54a3014.js</code>

## Route 5 — https://console.byteplus.com/ark/region:ap-southeast-1/model

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 4 files (4 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 3 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/model?view=DEFAULT_VIEW&amp;groupType=ModelGroups

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>e.get("vault_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>

#### `.query.*` / `query["..."]`

- <code>.query.trim</code> (x4) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
- <code>d=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>

### Location sinks (not deduped)

- <code>window.location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6947.d9bbbceb34.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code>
- <code>window.location.assign(</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code>

## Route 6 — https://console.byteplus.com/ark/region:ap-southeast-1/model/detail

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>
- <code>l=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code>

## Route 7 — https://console.byteplus.com/ark/region:ap-southeast-1/model/comparison

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/model/comparison?selection=%5B%7B%22columnId%22%3A%22column-1%22%2C%22modelName%22%3A%22dola-seed-2-1-turbo%22%2C%22modelVersion%22%3A%22260628%22%7D%2C%7B%22columnId%22%3A%22column-2%22%2C%22modelName%22%3A%22deepseek-v4-1-flash-economy%22%2C%22modelVersion%22%3A%22261017%22%7D%2C%7B%22columnId%22%3A%22column-3%22%2C%22modelName%22%3A%22deepseek-v4-1-flash%22%2C%22modelVersion%22%3A%22261017%22%7D%5D

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_comparison.fdf7c0861b.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>n=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_comparison.fdf7c0861b.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_comparison.fdf7c0861b.js</code>

## Route 10 — https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/promotion/*

- HTTP: 200 | Loaded: 8 files (8 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/model-settings/vmok-remote-entry.5250de02.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/model-settings/vmok-remote-entry.5250de02.js</code>

## Route 11 — https://console.byteplus.com/ark/region:ap-southeast-1/promotion/*

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 2 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/overview

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/306.75d9663c88.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/__federation_expose_routes.8289d3ab2d.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/306.75d9663c88.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/__federation_expose_routes.8289d3ab2d.js</code>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/306.75d9663c88.js</code>
- <code>location.replace(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/__federation_expose_routes.8289d3ab2d.js</code>

## Route 12 — https://console.byteplus.com/ark/region:ap-southeast-1/pickupVoucher

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 5 files (5 app / 0 vendor)
- New source matches: 4 app / 0 vendor | New location sinks: 2 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2716.4c01e47af9.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/4427.83192611c0.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/7219.070e90099a.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/977.a82025cf81.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_pickup_voucher.0dda270751.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2716.4c01e47af9.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/7219.070e90099a.js</code>
- <code>a=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/977.a82025cf81.js</code>

#### Other `.get(...)` (2)

<details><summary>Show generic .get matches</summary>

- <code>r.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_pickup_voucher.0dda270751.js</code>
- <code>x.get("pickup_voucher_id")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_pickup_voucher.0dda270751.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/7219.070e90099a.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/4427.83192611c0.js</code>

## Route 13 — https://console.byteplus.com/ark/region:ap-southeast-1/gallery

- HTTP: 200 | Loaded: 12 files (12 app / 0 vendor) | New: 4 files (4 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 3 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/model-promotion-collection/vmok-remote-entry.acf00cc8.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/533.e462f14b74.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/903.4e84f168f1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>t.get("subject")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/model-promotion-collection/vmok-remote-entry.acf00cc8.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/533.e462f14b74.js</code>
- <code>i=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/903.4e84f168f1.js</code>
- <code>t=new URL(location.pathname</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/903.4e84f168f1.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>i.searchParams.get("utm_source")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/533.e462f14b74.js</code>
- <code>window.location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/903.4e84f168f1.js</code>
- <code>window.location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code>

## Route 29 — https://console.byteplus.com/ark/region:ap-southeast-1/experience

- HTTP: 200 | Loaded: 16 files (16 app / 0 vendor) | New: 8 files (8 app / 0 vendor)
- New source matches: 10 app / 0 vendor | New location sinks: 4 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/42494.c2231c54e7.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/91274.4bb0a4afa9.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/93822.e7496ce86c.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_routes.4db18ec2aa.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_sidebar_extra.5e990f43bf.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>a.get("compareModelIds")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code>
- <code>a.get("modelId")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/91274.4bb0a4afa9.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/93822.e7496ce86c.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_routes.4db18ec2aa.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_routes.4db18ec2aa.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_sidebar_extra.5e990f43bf.js</code>

#### Other `.get(...)` (8)

<details><summary>Show generic .get matches</summary>

- <code>n.get("WEBGL_multi_draw")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>
- <code>o.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/42494.c2231c54e7.js</code>
- <code>r.searchParams.get("response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code>
- <code>r.searchParams.get("x-oss-response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code>
- <code>r.searchParams.get("x-tos-response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code>
- <code>t.get("EXT_color_buffer_float")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>
- <code>t.get("WEBGL_multi_draw")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>
- <code>t.get("WEBGL_multisampled_render_to_texture")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/93822.e7496ce86c.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/91274.4bb0a4afa9.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/91274.4bb0a4afa9.js</code>
- <code>location =</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>

## Route 31 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/creations

- HTTP: 200 | Loaded: 18 files (18 app / 0 vendor) | New: 4 files (4 app / 0 vendor)
- New source matches: 5 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/10260.3b056e3429.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/3625.d4b9487dc9.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/75664.0aad4702c6.js</code>

### App source matches (unique)

#### Other `.get(...)` (5)

<details><summary>Show generic .get matches</summary>

- <code>a.searchParams.get("response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code>
- <code>a.searchParams.get("x-oss-response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code>
- <code>a.searchParams.get("x-tos-response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code>
- <code>e.extensions.get("WEBGL_compressed_texture_astc")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/75664.0aad4702c6.js</code>
- <code>e.get("month")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/3625.d4b9487dc9.js</code>

</details>

### Location sinks (not deduped)

- <code>location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/10260.3b056e3429.js</code>

## Route 34 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_video

- HTTP: 200 | Loaded: 18 files (18 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/37624.e789471e61.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/37624.e789471e61.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code>
- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code>
- <code>t=new URL(window.location.href</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>r.searchParams.get("env")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code>

</details>

## Route 36 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_3d

- HTTP: 200 | Loaded: 21 files (21 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/17535.17b02bf1ba.js</code>

### App source matches (unique)

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>tO.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/17535.17b02bf1ba.js</code>

</details>

## Route 38 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/voice

- HTTP: 200 | Loaded: 21 files (21 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/39548.444d033809.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/51111.ffecb0decc.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/39548.444d033809.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>i.get("month")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/51111.ffecb0decc.js</code>

</details>

## Route 39 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/claw

- HTTP: 200 | Loaded: 17 files (17 app / 0 vendor) | New: 5 files (5 app / 0 vendor)
- New source matches: 15 app / 0 vendor | New location sinks: 9 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/802.7e735117.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/888.bbea105d.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/976.e5ed7b4c.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/lib-router.635e7c1f.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>n.get("payment_status")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>n.get("s_v_web_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/lib-router.635e7c1f.js</code>

#### Other `.get(...)` (13)

<details><summary>Show generic .get matches</summary>

- <code>Cookies3.get("isIntranet")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>F9.Z.get(`${location.protocol}//${zo}/obj/finance/env.json`)</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>I.Z.get("monitor_huoshan_web_id")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>I.Z.get("monitor_utm")</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>I.Z.get("user_locale")</code> (x5) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>a.Z.get("user_locale")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>ns.Z.get(`${location.protocol}//${atob(t)}/obj/finance/env.json`)</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>o.Z.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>t.get("*")</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>t.get("arkclaw_x_starter")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/888.bbea105d.js</code>
- <code>t.get("month")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/802.7e735117.js</code>
- <code>u.Z.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>y.Z.get("csrfToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>

</details>

### Location sinks (not deduped)

- <code>location.assign(</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/lib-router.635e7c1f.js</code>
- <code>location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/lib-router.635e7c1f.js</code>
- <code>window.location.href=</code> (x7) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>location.href=</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>location.assign(</code> (x10) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>location=</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
- <code>location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/976.e5ed7b4c.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/976.e5ed7b4c.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/888.bbea105d.js</code>

## Route 42 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/share/:id

- HTTP: 200 | Loaded: 18 files (18 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 21 app / 0 vendor | New location sinks: 2 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/64502.495c754e7c.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>

### App source matches (unique)

#### Other `.get(...)` (21)

<details><summary>Show generic .get matches</summary>

- <code>Q.get("background-color")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>Q.get("font-family")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>Q.node.attributes.get("selection")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>T.get("depth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("data-semantic-speech")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("lspace")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("mathsize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("rspace")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("scriptlevel")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("scriptminsize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.get("scriptsizemultiplier")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>e.node.attributes.get("bevelled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>n.get("lspace")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>n.get("rspace")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>o.attributes.get("scriptlevel")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>r.get("frame")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>r.get("mjx-keep-attrs")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>t.get("bevelled")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>t.get("largeop")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>t.get("linethickness")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
- <code>t.get("mathsize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>

</details>

### Location sinks (not deduped)

- <code>location=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/64502.495c754e7c.js</code>
- <code>location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/64502.495c754e7c.js</code>

## Route 44 — https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_canvas/:id

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/16458.c88ef04029.js</code>

### App source matches (unique)

#### `.query.*` / `query["..."]`

- <code>.query.charCodeAt</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/16458.c88ef04029.js</code>
- <code>.query.length</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/16458.c88ef04029.js</code>
- <code>.query.spec</code> (x4) — <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/16458.c88ef04029.js</code>

## Route 46 — https://console.byteplus.com/ark/region:ap-southeast-1/endpoint

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 6 files (6 app / 0 vendor)
- New source matches: 4 app / 0 vendor | New location sinks: 3 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/1453.3d4e7d8023.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/4337.b260caab3e.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/675.0aef9bd056.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7210.dbe0130553.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/8728.361f718585.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_list.922f1ad7a0.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/1453.3d4e7d8023.js</code>
- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/675.0aef9bd056.js</code>
- <code>u=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/675.0aef9bd056.js</code>

#### Other `.get(...)` (3)

<details><summary>Show generic .get matches</summary>

- <code>a.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7210.dbe0130553.js</code>
- <code>p.get("pageNumber")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_list.922f1ad7a0.js</code>
- <code>p.get("pageSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_list.922f1ad7a0.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/1453.3d4e7d8023.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/4337.b260caab3e.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/8728.361f718585.js</code>

## Route 47 — https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/create

- HTTP: 200 | Loaded: 15 files (15 app / 0 vendor) | New: 5 files (5 app / 0 vendor)
- New source matches: 4 app / 0 vendor | New location sinks: 2 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2314.a9e4208f13.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3197.eda19b0eaa.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3372.8331a92330.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7924.4e5ca1b471.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_create.addf5ad349.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_create.addf5ad349.js</code>
- <code>n=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_create.addf5ad349.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_create.addf5ad349.js</code>

#### Other `.get(...)` (4)

<details><summary>Show generic .get matches</summary>

- <code>A.A.get("csrfToken")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7924.4e5ca1b471.js</code>
- <code>L.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7924.4e5ca1b471.js</code>
- <code>eX.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3197.eda19b0eaa.js</code>
- <code>to.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3372.8331a92330.js</code>

</details>

### Location sinks (not deduped)

- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3197.eda19b0eaa.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3372.8331a92330.js</code>

## Route 48 — https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/detail

- HTTP: 200 | Loaded: 17 files (17 app / 0 vendor) | New: 4 files (4 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 1 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/detail?Tab=Overview

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2732.0aef4bf74d.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/5314.f58e1230d9.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/9857.cacc2df099.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_detail.da9d422fb4.js</code>

### App source matches (unique)

#### Other `.get(...)` (2)

<details><summary>Show generic .get matches</summary>

- <code>n.get("*")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2732.0aef4bf74d.js</code>
- <code>tu.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_detail.da9d422fb4.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/5314.f58e1230d9.js</code>

## Route 49 — https://console.byteplus.com/ark/region:ap-southeast-1/batchInference

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2050.519f56b0a8.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_batchInference_manage.e7d9547562.js</code>

## Route 56 — https://console.byteplus.com/ark/region:ap-southeast-1/ipDashboard/*

- HTTP: 200 | Loaded: 14 files (14 app / 0 vendor) | New: 5 files (5 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 1 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/openManagement?advancedActiveKey=mediaAsset&amp;assetType=CopyrightManagement&amp;copyrightManagementSubTab=UsageRevenue&amp;openAssetsLibrary=false

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/1206.ce188f4c26.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/5227.c74122e561.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/6239.711d224b6f.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_manage.39c398fd0f.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/5227.c74122e561.js</code>
- <code>r=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code>

#### Other `.get(...)` (2)

<details><summary>Show generic .get matches</summary>

- <code>e.get("hour")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code>
- <code>e.get("minute")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code>

</details>

### Location sinks (not deduped)

- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/6239.711d224b6f.js</code>

## Route 57 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents

- HTTP: 200 | Loaded: 12 files (12 app / 0 vendor) | New: 5 files (5 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 3 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/27065.b90e3594ea.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/38767.27735c56c3.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4476.785c7dd255.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4910.9997e22df0.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/98068.626da96785.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/38767.27735c56c3.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/98068.626da96785.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/98068.626da96785.js</code>

#### Other `.get(...)` (3)

<details><summary>Show generic .get matches</summary>

- <code>eQ.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4910.9997e22df0.js</code>
- <code>p.A.get("csrfToken")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4476.785c7dd255.js</code>
- <code>tl.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/27065.b90e3594ea.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/38767.27735c56c3.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4910.9997e22df0.js</code>
- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/27065.b90e3594ea.js</code>

## Route 58 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/quickstart

- HTTP: 200 | Loaded: 15 files (15 app / 0 vendor) | New: 4 files (4 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 2 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/22673.83f22e0b73.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/61962.9ddbcf9862.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/84279.11ada4c40e.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/61962.9ddbcf9862.js</code>
- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>
- <code>n=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>
- <code>r=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>
- <code>t=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>x.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/61962.9ddbcf9862.js</code>

</details>

### Location sinks (not deduped)

- <code>location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/22673.83f22e0b73.js</code>
- <code>location.replace(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>

## Route 61 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/:id

- HTTP: 200 | Loaded: 12 files (12 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_agents_detail.3a4d689d4e.js</code>

## Route 65 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/create

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/45883.4655d9465a.js</code>

### Location sinks (not deduped)

- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/45883.4655d9465a.js</code>

## Route 67 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/environments

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/28560.9e1f9feed8.js</code>

### App source matches (unique)

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>eZ.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/28560.9e1f9feed8.js</code>

</details>

### Location sinks (not deduped)

- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/28560.9e1f9feed8.js</code>

## Route 69 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_credentials_vault.6d0e89ea57.js</code>

### Location sinks (not deduped)

- <code>location.replace(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_credentials_vault.6d0e89ea57.js</code>

## Route 72 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_manage.1a405fdca7.js</code>

## Route 73 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills/:id

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_detail.9b8f8d7227.js</code>

### App source matches (unique)

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>h.A.get("csrfToken")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_detail.9b8f8d7227.js</code>

</details>

## Route 74 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/memory

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_memory.33e6c1b4f9.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_memory.33e6c1b4f9.js</code>

## Route 76 — https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/create

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_channel_create.8602b94971.js</code>

### App source matches (unique)

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>K.get("step")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_channel_create.8602b94971.js</code>

</details>

## Route 81 — https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create-deprecated

- HTTP: 200 | Loaded: 9 files (9 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 2 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create-deprecated?Id=&amp;customModelId=

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/7431.c85252ad29.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8934.16f82886be.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/7431.c85252ad29.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8934.16f82886be.js</code>
- <code>u=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8934.16f82886be.js</code>

### Location sinks (not deduped)

- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/7431.c85252ad29.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/7431.c85252ad29.js</code>

## Route 84 — https://console.byteplus.com/ark/region:ap-southeast-1/finetune/detail

- HTTP: 200 | Loaded: 12 files (12 app / 0 vendor) | New: 3 files (3 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/finetune/detail?Id=&amp;metricsExcludedMetricNames[]&amp;pluginManage.tab=normal&amp;tab=overview

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/5074.8fd8bee520.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8661.575e841d27.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_detail.6ab57a014c.js</code>

### App source matches (unique)

#### `.query.*` / `query["..."]`

- <code>.query.metricsExcludedMetricNames</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_detail.6ab57a014c.js</code>

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/5074.8fd8bee520.js</code>
- <code>u=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/5074.8fd8bee520.js</code>

#### Other `.get(...)` (2)

<details><summary>Show generic .get matches</summary>

- <code>c.get("month")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8661.575e841d27.js</code>
- <code>n.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/5074.8fd8bee520.js</code>

</details>

## Route 85 — https://console.byteplus.com/ark/region:ap-southeast-1/finetune/comparison

- HTTP: 200 | Loaded: 9 files (9 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_comparison.61405f08cd.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_comparison.61405f08cd.js</code>

## Route 86 — https://console.byteplus.com/ark/region:ap-southeast-1/finetune/tls

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_tls.06fcecf40a.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_tls.06fcecf40a.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_tls.06fcecf40a.js</code>

## Route 89 — https://console.byteplus.com/ark/region:ap-southeast-1/customModel/detail

- HTTP: 200 | Loaded: 9 files (9 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/customModel/detail?Id=

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_repository_detail.c228a8a794.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>u=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_repository_detail.c228a8a794.js</code>

## Route 91 — https://console.byteplus.com/ark/region:ap-southeast-1/eval/create

- HTTP: 200 | Loaded: 9 files (9 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/eval/create?prefill=

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_create.292a62ba40.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_create.292a62ba40.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_create.292a62ba40.js</code>

## Route 92 — https://console.byteplus.com/ark/region:ap-southeast-1/eval/detail

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_detail.96ea3ee7bf.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_detail.96ea3ee7bf.js</code>

## Route 94 — https://console.byteplus.com/ark/region:ap-southeast-1/dataset/create

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/2616.68953e3608.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>n=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/2616.68953e3608.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/2616.68953e3608.js</code>

## Route 95 — https://console.byteplus.com/ark/region:ap-southeast-1/dataset/detail

- HTTP: 200 | Loaded: 9 files (9 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_detail.86a4d90ebf.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>n=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_detail.86a4d90ebf.js</code>

## Route 97 — https://console.byteplus.com/ark/region:ap-southeast-1/dataset/dump/create

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_dump_create.4de9662963.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_dump_create.4de9662963.js</code>

## Route 108 — https://console.byteplus.com/ark/region:ap-southeast-1/application

- HTTP: 200 | Loaded: 25 files (13 app / 12 vendor) | New: 17 files (5 app / 12 vendor)
- New source matches: 1 app / 25 vendor | New location sinks: 3 app / 1 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/app-lab/vmok-remote-entry.46031a1d.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6709.1fb936582f.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7587.08a9ca23cf.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7725.02a4a0b9b3.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_center.b3abac992b.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/app-lab/vmok-remote-entry.46031a1d.js</code>
- <code>i=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6709.1fb936582f.js</code>
- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7725.02a4a0b9b3.js</code>
- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_center.b3abac992b.js</code>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7725.02a4a0b9b3.js</code>
- <code>location.assign(</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7587.08a9ca23cf.js</code>
- <code>location.replace(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7587.08a9ca23cf.js</code>

## Route 110 — https://console.byteplus.com/ark/region:ap-southeast-1/application/claw

- HTTP: 200 | Loaded: 8 files (0 app / 8 vendor) | New: 8 files (0 app / 8 vendor)
- New source matches: 0 app / 15 vendor | New location sinks: 0 app / 14 vendor
- Note: final URL: https://signin.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fconsole.volcengine.com%2Farkclaw%2Fchat%2Fci-yepk65ajuorkm4wr7k1k%3Fagent%3Dmain

## Route 112 — https://console.byteplus.com/ark/region:ap-southeast-1/application/detail

- HTTP: 200 | Loaded: 29 files (17 app / 12 vendor) | New: 5 files (5 app / 0 vendor)
- New source matches: 10 app / 0 vendor | New location sinks: 2 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/2273.772c1f780a.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/257.6a9abae379.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_detail.07b6dbbd6c.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_detail.07b6dbbd6c.js</code>

#### Other `.get(...)` (10)

<details><summary>Show generic .get matches</summary>

- <code>a.get("x-request-id")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>
- <code>eJ.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
- <code>h.get("x-request-id")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>
- <code>i.get("lspace")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
- <code>i.get("rspace")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
- <code>l.get("x-request-id")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>
- <code>o.get("mjx-keep-attrs")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
- <code>r.get("x-tt-logid")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>
- <code>s8.A.get("csrfToken")</code> (x7) — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/257.6a9abae379.js</code>
- <code>v.get("x-request-id")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>

</details>

### Location sinks (not deduped)

- <code>location.assign(</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
- <code>location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/2273.772c1f780a.js</code>

## Route 113 — https://console.byteplus.com/ark/region:ap-southeast-1/assistant

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6042.a194df1285.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_my_apps.36fd1cc29b.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_my_apps.36fd1cc29b.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>C.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6042.a194df1285.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6042.a194df1285.js</code>

## Route 114 — https://console.byteplus.com/ark/region:ap-southeast-1/assistant/edit

- HTTP: 200 | Loaded: 17 files (17 app / 0 vendor) | New: 3 files (3 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 1 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/assistant/edit?tab=Edit

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/5125.4f7bc454e2.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/9832.9d43b6b9d6.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_edit.5ec129a509.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_edit.5ec129a509.js</code>

#### Other `.get(...)` (2)

<details><summary>Show generic .get matches</summary>

- <code>a8.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/5125.4f7bc454e2.js</code>
- <code>v.get("botType")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/5125.4f7bc454e2.js</code>

</details>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/9832.9d43b6b9d6.js</code>

## Route 115 — https://console.byteplus.com/ark/region:ap-southeast-1/assistant/detail

- HTTP: 200 | Loaded: 14 files (14 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_detail.e155531a98.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_detail.e155531a98.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>w.get("botType")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_detail.e155531a98.js</code>

</details>

## Route 119 — https://console.byteplus.com/ark/region:ap-southeast-1/knowledge

- HTTP: 200 | Loaded: 9 files (0 app / 9 vendor) | New: 9 files (0 app / 9 vendor)
- New source matches: 0 app / 22 vendor | New location sinks: 0 app / 13 vendor
- Note: final URL: https://signin.byteplus.com/auth/login?redirectURI=https%3A%2F%2Fconsole.byteplus.com%2Fvikingdb%2Fknowledge%2Fregion%3Avdb-knowledge%2Bap-southeast-1%2Fcollection%2Flist%3F

## Route 131 — https://console.byteplus.com/ark/region:ap-southeast-1/subscription/coding-plan

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8010.b4b0f9e430.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_coding_plan_pane.13c650e89c.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>e=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8010.b4b0f9e430.js</code>
- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_coding_plan_pane.13c650e89c.js</code>

## Route 140 — https://console.byteplus.com/ark/region:ap-southeast-1/openManagement/rewardPlan

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_reward_plan.30a4a5d92e.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>Q=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_reward_plan.30a4a5d92e.js</code>
- <code>g=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_reward_plan.30a4a5d92e.js</code>

## Route 142 — https://console.byteplus.com/ark/region:ap-southeast-1/apiKey

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/apiKey?apikey=%7B%7D

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8156.7bf97dfbc9.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_api_key_manage.b870f1b214.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8156.7bf97dfbc9.js</code>
- <code>n=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_api_key_manage.b870f1b214.js</code>

## Route 143 — https://console.byteplus.com/ark/region:ap-southeast-1/usageTracking

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 237 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_usage_tracking_manage.d972bdb5cb.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_usage_tracking_manage.d972bdb5cb.js</code>

#### Other `.get(...)` (237)

<details><summary>Show generic .get matches</summary>

- <code>A.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>E.get("smooth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>I.get("maxSurfaceAngle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>I.get("minTurnAngle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>P.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>P.get("disabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>_.get("edgeDistance")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("blurScope")</code> (x5) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("borderColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("dataBackgroundColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("disabled")</code> (x5) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("fillerColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("focus")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("friction")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("gravity")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("handleLabel")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("ignoreForceLayout")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("inside")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("moveHandleIcon")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("moveHandleSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("realtime")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("scale")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("scaleSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>a.get("textShadowColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>c.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>c.get("disabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>c.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>d.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>d.get("disabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>d.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("alignWithLabel")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("axisExpandCenter")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("axisExpandCount")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("axisExpandDebounce")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("axisExpandWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("backgroundColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("barMaxWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("barMinWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("borderColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("borderRadius")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("borderWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("coordinateSystem")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("cursor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("delay")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("itemGap")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("maxInterval")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("minInterval")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("minTurnAngle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("orient")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("period")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("radarIndex")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("scaleLimit")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("showDetail")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("showLegendSymbol")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("throttle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("triggerEvent")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>e.get("z")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>f.get("clip")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>h.get("formatter")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>h.get("formatterParams")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>h.get("lineHeight")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("delay")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("disabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("easing")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("inactiveColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("inverse")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("polyline")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("tooltip")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("triggerOn")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("useUTC")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>i.get("verticalAlign")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>k.normal.get("formatter")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>l.get("parallelIndex")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textAlign")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textBackgroundColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textBorderRadius")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textFill")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textFontFamily")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textFontSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textFontStyle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textFontWeight")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textPadding")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("textPosition")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>m.get("verticalAlign")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("axisExpandTriggerOn")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("axisExpandable")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("blurScope")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("boundaryGap")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("connectedBackgroundColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("dim")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("disabled")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("enabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("excludeComponents")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("focus")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("markLine")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("markPoint")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("pixelRatio")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("rotate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("scale")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("seriesDataIndices")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("stack")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("symbolOffset")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("symbolRepeatDirection")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("symbolRotate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("useUTC")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("value")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("z")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.get("zoomLock")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>n.hostModel.get("percentPrecision")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("boundaryGap")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("disabled")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("icon")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("order")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("rotate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("show")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("symbolKeepAspect")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("symbolSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("textStyle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>o.get("throttle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>p.get("itemGap")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>p.get("itemSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>p.get("textStyle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>r.get("animationDurationUpdate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>r.get("animationEasingUpdate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>r.get("emptyItemWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>r.get("show")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>r.get("silent")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("alignTicks")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("blurScope")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("description")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("disabled")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("enabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("formatter")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("icon")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("rotate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>s.get("tooltip")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.ecModel.get("useUTC")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("activeOpacity")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("animation")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("aspectScale")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("autoCurveness")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("avoidLabelOverlap")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("axisExpandRate")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("backgroundColor")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("barMaxWidth")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("barMinWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("barWidth")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("borderColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("borderRadius")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("borderWidth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("boundaryGap")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("calendarIndex")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("center")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("containLabel")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("edgeSymbol")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("edgeSymbolSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("endAngle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("enterable")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("extraCssText")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("geoCoord")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("gradientColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("handleIcon")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("handleSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("inactiveOpacity")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("indicatorIcon")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("indicatorSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("inverse")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("itemGap")</code> (x4) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("itemSize")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("layoutIterations")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("legendHoverLink")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("max")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("maxSize")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("min")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("minShowLabelAngle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("minSize")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("nameMap")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("nameProperty")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("nodeAlign")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("orient")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("parallelIndex")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("projection")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("radarIndex")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("radius")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("realtime")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("roam")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("scaleLimit")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("selectedMode")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("show")</code> (x8) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("showContent")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("showEmptyCircle")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("showLegendSymbol")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("silent")</code> (x5) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("smooth")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("stack")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("startAngle")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("step")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("subtarget")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("symbol")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("symbolKeepAspect")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("symbolMargin")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("symbolOffset")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("symbolSize")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("target")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("text")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("textBaseline")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("textVerticalAlign")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("title.0.text")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("transitionDuration")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("triggerEvent")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("triggerLineEvent")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("visualDimension")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>t.get("zoom")</code> (x3) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>u.get("buttonColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>u.get("buttonTextColor")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>u.get("readOnly")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>u.get("title")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>v.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>v.get("disabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>v.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>v.get("show")</code> (x2) — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>v.get("value")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>w.get("blurScope")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>w.get("disabled")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>w.get("focus")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>w.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>x.get("formatter")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
- <code>x.get("show")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>

</details>

## Route 146 — https://console.byteplus.com/ark/region:ap-southeast-1/vpc

- HTTP: 200 | Loaded: 10 files (10 app / 0 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_vpc.280c5715d1.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>o=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_vpc.280c5715d1.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_vpc.280c5715d1.js</code>

## Route 147 — https://console.byteplus.com/ark/region:ap-southeast-1/projectManagement

- HTTP: 200 | Loaded: 13 files (13 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 1 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/projectManagement?quota=%7B%22business%22%3A%22Endpoint%22%2C%22quota%22%3A%22ModelTPM%22%2C%22table%22%3A%7B%7D%7D&amp;tab=Quota

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2279.f71a69c7ae.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_project_management.b3b7526866.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_project_management.b3b7526866.js</code>
- <code>t=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_project_management.b3b7526866.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_project_management.b3b7526866.js</code>

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>y.A.get("csrfToken")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2279.f71a69c7ae.js</code>

</details>

### Location sinks (not deduped)

- <code>location.assign(</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2279.f71a69c7ae.js</code>

## Route 148 — https://console.byteplus.com/ark/region:ap-southeast-1/tokenCalculator

- HTTP: 200 | Loaded: 11 files (11 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/898.4d2dc21a91.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_token_calculator.5aa401a3b2.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>a=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_token_calculator.5aa401a3b2.js</code>
- <code>t=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_token_calculator.5aa401a3b2.js</code>

#### Other `.get(...)` (3)

<details><summary>Show generic .get matches</summary>

- <code>i.searchParams.get("response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/898.4d2dc21a91.js</code>
- <code>i.searchParams.get("x-oss-response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/898.4d2dc21a91.js</code>
- <code>i.searchParams.get("x-tos-response-content-type")</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/898.4d2dc21a91.js</code>

</details>

## Route 149 — https://console.byteplus.com/ark/region:ap-southeast-1/docs

- HTTP: 200 | Loaded: 11 files (7 app / 4 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/ark/region:ap-southeast-1/docs/product-overview

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6390.72c02fadf9.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>p=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6390.72c02fadf9.js</code>

## Route 152 — https://console.byteplus.com/ark/region:ap-southeast-1/arkcli

- HTTP: 200 | Loaded: 9 files (9 app / 0 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/820.0c05aa3327.js</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/953.9665a6db4c.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction (not deduped)

- <code>t=new URL(location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/820.0c05aa3327.js</code>
- <code>M=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/953.9665a6db4c.js</code>
- <code>i=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/953.9665a6db4c.js</code>

### Location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/820.0c05aa3327.js</code>

## Unique Routes With No New Discoveries

20 unique routes loaded no new JS files and produced no new source matches or location sinks.

| Route | URL | Loaded files |
|---:|---|---:|
| 8 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model/leaderboard (final: https://console.byteplus.com/ark/region:ap-southeast-1/overview)</code> | 9 |
| 9 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/ip-letter-download (final: https://console.byteplus.com/ark/region:ap-southeast-1/overview)</code> | 10 |
| 14 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/gallery/*</code> | 11 |
| 33 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_image</code> | 15 |
| 40 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/ma/:presetKey</code> | 12 |
| 43 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_video/:id</code> | 15 |
| 50 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/create</code> | 12 |
| 51 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/detail?Tab=overview)</code> | 13 |
| 52 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/batchEpDetail (final: https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/batchEpDetail?Tab=overview)</code> | 15 |
| 60 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/create</code> | 13 |
| 64 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions</code> | 11 |
| 66 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/:id</code> | 14 |
| 70 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault/:id (final: https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault?searchField=Name)</code> | 11 |
| 71 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault-oauth/callback</code> | 8 |
| 75 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels</code> | 10 |
| 77 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/:id</code> | 9 |
| 96 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/version/create</code> | 9 |
| 101 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tts/speechRecognition</code> | 7 |
| 109 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application/doubaoAPI (final: https://console.byteplus.com/ark/region:ap-southeast-1/overview)</code> | 21 |
| 139 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/openManagement (final: https://console.byteplus.com/ark/region:ap-southeast-1/openManagement?LLM=%7B%7D)</code> | 12 |

## All source and sink matches, unique per file (app)

<details><summary>All source and sink matches, unique per file (app)</summary>

- <code>https://res.gcloudcache.com/bp-fe/console-ark/app-lab/vmok-remote-entry.46031a1d.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
  - [sink] <code>window.location.assign(</code> (x2)
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code>
  - [source] <code>r.get("*")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/2184.1fa6f9e2e4.js</code>
  - [source] <code>a=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6390.72c02fadf9.js</code>
  - [source] <code>p=new URL(window.location.href</code>
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
- <code>https://res.gcloudcache.com/bp-fe/console-ark/exp-center/vmok-remote-entry.e54a3014.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/model-promotion-collection/vmok-remote-entry.acf00cc8.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/model-settings/vmok-remote-entry.5250de02.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/666.9828743d.js</code>
  - [source] <code>Cookies3.get("isIntranet")</code>
  - [source] <code>F9.Z.get(`${location.protocol}//${zo}/obj/finance/env.json`)</code>
  - [source] <code>I.Z.get("monitor_huoshan_web_id")</code> (x2)
  - [source] <code>I.Z.get("monitor_utm")</code> (x2)
  - [source] <code>I.Z.get("user_locale")</code> (x5)
  - [source] <code>a.Z.get("user_locale")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x14)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x4)
  - [source] <code>e.configManager.get("web_id")</code> (x14)
  - [source] <code>i.configManager.get("user")</code> (x19)
  - [source] <code>n.configManager.get("reportErrorCallback")</code> (x5)
  - [source] <code>n.configManager.get("user")</code> (x3)
  - [source] <code>n.get("payment_status")</code>
  - [source] <code>n.get("s_v_web_id")</code>
  - [source] <code>ns.Z.get(`${location.protocol}//${atob(t)}/obj/finance/env.json`)</code>
  - [source] <code>o.Z.get("csrfToken")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t.get("*")</code> (x3)
  - [source] <code>u.Z.get("csrfToken")</code>
  - [source] <code>y.Z.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [sink] <code>location.assign(</code> (x10)
  - [sink] <code>location.href=</code> (x3)
  - [sink] <code>location=</code> (x2)
  - [sink] <code>window.location.href=</code> (x7)
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/802.7e735117.js</code>
  - [source] <code>t.get("month")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/888.bbea105d.js</code>
  - [source] <code>t.get("arkclaw_x_starter")</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/976.e5ed7b4c.js</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x4)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x4)
  - [source] <code>n.configManager.get("reportErrorCallback")</code> (x2)
  - [source] <code>n.configManager.get("user")</code> (x7)
  - [sink] <code>location.href=</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ecs/volc-claw/static/js/1.0.0.853/async/lib-router.635e7c1f.js</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/2273.772c1f780a.js</code>
  - [sink] <code>location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/257.6a9abae379.js</code>
  - [source] <code>s8.A.get("csrfToken")</code> (x7)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/5125.4f7bc454e2.js</code>
  - [source] <code>a8.A.get("csrfToken")</code>
  - [source] <code>v.get("botType")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6042.a194df1285.js</code>
  - [source] <code>C.A.get("csrfToken")</code>
  - [sink] <code>window.location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6709.1fb936582f.js</code>
  - [source] <code>i=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code>
  - [source] <code>a.attributes.get("scriptlevel")</code>
  - [source] <code>e.attributes.get("columnalign")</code> (x2)
  - [source] <code>e.attributes.get("columnspacing")</code> (x2)
  - [source] <code>e.get("background-color")</code>
  - [source] <code>e.get("font-family")</code>
  - [source] <code>e.gullet.macros.get("\\df@tag")</code>
  - [source] <code>e.macros.get("\\df@tag")</code>
  - [source] <code>e.node.attributes.get("selection")</code>
  - [source] <code>eJ.A.get("csrfToken")</code>
  - [source] <code>i.get("lspace")</code>
  - [source] <code>i.get("rspace")</code>
  - [source] <code>n.get("data-semantic-speech")</code>
  - [source] <code>n.get("lspace")</code>
  - [source] <code>n.get("mathsize")</code>
  - [source] <code>n.get("rspace")</code>
  - [source] <code>n.get("scriptlevel")</code>
  - [source] <code>n.get("scriptminsize")</code>
  - [source] <code>n.get("scriptsizemultiplier")</code>
  - [source] <code>n.node.attributes.get("bevelled")</code>
  - [source] <code>o.get("frame")</code>
  - [source] <code>o.get("mjx-keep-attrs")</code>
  - [source] <code>r.get("depth")</code>
  - [source] <code>r.gullet.macros.get("\\df@tag")</code>
  - [source] <code>t.get("bevelled")</code> (x2)
  - [source] <code>t.get("largeop")</code>
  - [source] <code>t.get("linethickness")</code>
  - [source] <code>t.get("mathsize")</code>
  - [sink] <code>location.assign(</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7587.08a9ca23cf.js</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7725.02a4a0b9b3.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code>
  - [source] <code>a.get("x-request-id")</code> (x2)
  - [source] <code>h.get("x-request-id")</code>
  - [source] <code>l.A.get("csrfToken")</code>
  - [source] <code>l.get("x-request-id")</code>
  - [source] <code>r.get("x-tt-logid")</code>
  - [source] <code>v.get("x-request-id")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/9832.9d43b6b9d6.js</code>
  - [source] <code>e.get("month")</code>
  - [source] <code>.query.length</code> (x2)
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_center.b3abac992b.js</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_detail.07b6dbbd6c.js</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_detail.e155531a98.js</code>
  - [source] <code>w.get("botType")</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_edit.5ec129a509.js</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_my_apps.36fd1cc29b.js</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/820.0c05aa3327.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/953.9665a6db4c.js</code>
  - [source] <code>M=new URL(window.location.href</code>
  - [source] <code>i=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/10260.3b056e3429.js</code>
  - [sink] <code>location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/16458.c88ef04029.js</code>
  - [source] <code>.query.charCodeAt</code> (x2)
  - [source] <code>.query.length</code> (x2)
  - [source] <code>.query.spec</code> (x4)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/17535.17b02bf1ba.js</code>
  - [source] <code>tO.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code>
  - [source] <code>r.searchParams.get("response-content-type")</code>
  - [source] <code>r.searchParams.get("x-oss-response-content-type")</code>
  - [source] <code>r.searchParams.get("x-tos-response-content-type")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/3625.d4b9487dc9.js</code>
  - [source] <code>e.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/37624.e789471e61.js</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/39548.444d033809.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code>
  - [source] <code>a.searchParams.get("response-content-type")</code>
  - [source] <code>a.searchParams.get("x-oss-response-content-type")</code>
  - [source] <code>a.searchParams.get("x-tos-response-content-type")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/42494.c2231c54e7.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/51111.ffecb0decc.js</code>
  - [source] <code>i.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>
  - [source] <code>n.get("WEBGL_multi_draw")</code>
  - [source] <code>t.get("EXT_color_buffer_float")</code>
  - [source] <code>t.get("WEBGL_multi_draw")</code> (x2)
  - [source] <code>t.get("WEBGL_multisampled_render_to_texture")</code>
  - [sink] <code>location =</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/64502.495c754e7c.js</code>
  - [sink] <code>location.href=</code>
  - [sink] <code>location=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code>
  - [source] <code>a.get("compareModelIds")</code>
  - [source] <code>a.get("modelId")</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/75664.0aad4702c6.js</code>
  - [source] <code>e.extensions.get("WEBGL_compressed_texture_astc")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code>
  - [source] <code>r.searchParams.get("env")</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URL(window.location.href</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/84279.04499e58ab.js</code>
  - [source] <code>Q.get("background-color")</code>
  - [source] <code>Q.get("font-family")</code>
  - [source] <code>Q.node.attributes.get("selection")</code>
  - [source] <code>T.get("depth")</code>
  - [source] <code>e.get("data-semantic-speech")</code>
  - [source] <code>e.get("lspace")</code>
  - [source] <code>e.get("mathsize")</code>
  - [source] <code>e.get("rspace")</code>
  - [source] <code>e.get("scriptlevel")</code>
  - [source] <code>e.get("scriptminsize")</code>
  - [source] <code>e.get("scriptsizemultiplier")</code>
  - [source] <code>e.node.attributes.get("bevelled")</code>
  - [source] <code>n.get("lspace")</code>
  - [source] <code>n.get("rspace")</code>
  - [source] <code>o.attributes.get("scriptlevel")</code>
  - [source] <code>r.get("frame")</code>
  - [source] <code>r.get("mjx-keep-attrs")</code>
  - [source] <code>t.get("bevelled")</code> (x2)
  - [source] <code>t.get("largeop")</code>
  - [source] <code>t.get("linethickness")</code>
  - [source] <code>t.get("mathsize")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/91274.4bb0a4afa9.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x6)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x2)
  - [source] <code>e.configManager.get("web_id")</code> (x6)
  - [source] <code>n.configManager.get("reportErrorCallback")</code> (x2)
  - [source] <code>o.configManager.get("user")</code> (x7)
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>location.assign(</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/93822.e7496ce86c.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_routes.4db18ec2aa.js</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_sidebar_extra.5e990f43bf.js</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/22673.83f22e0b73.js</code>
  - [sink] <code>location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/27065.b90e3594ea.js</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>e.get("month")</code>
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>o.configManager.get("user")</code> (x6)
  - [source] <code>tl.A.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/28560.9e1f9feed8.js</code>
  - [source] <code>eZ.A.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/38767.27735c56c3.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4476.785c7dd255.js</code>
  - [source] <code>p.A.get("csrfToken")</code> (x3)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/45883.4655d9465a.js</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4910.9997e22df0.js</code>
  - [source] <code>eQ.A.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/61962.9ddbcf9862.js</code>
  - [source] <code>p.A.get("csrfToken")</code> (x3)
  - [source] <code>x.A.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/84279.11ada4c40e.js</code>
  - [source] <code>Q.get("background-color")</code>
  - [source] <code>Q.get("font-family")</code>
  - [source] <code>Q.node.attributes.get("selection")</code>
  - [source] <code>T.get("depth")</code>
  - [source] <code>e.get("data-semantic-speech")</code>
  - [source] <code>e.get("lspace")</code>
  - [source] <code>e.get("mathsize")</code>
  - [source] <code>e.get("rspace")</code>
  - [source] <code>e.get("scriptlevel")</code>
  - [source] <code>e.get("scriptminsize")</code>
  - [source] <code>e.get("scriptsizemultiplier")</code>
  - [source] <code>e.node.attributes.get("bevelled")</code>
  - [source] <code>n.get("lspace")</code>
  - [source] <code>n.get("rspace")</code>
  - [source] <code>o.attributes.get("scriptlevel")</code>
  - [source] <code>r.get("frame")</code>
  - [source] <code>r.get("mjx-keep-attrs")</code>
  - [source] <code>t.get("bevelled")</code> (x2)
  - [source] <code>t.get("largeop")</code>
  - [source] <code>t.get("linethickness")</code>
  - [source] <code>t.get("mathsize")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/98068.626da96785.js</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_agents_detail.3a4d689d4e.js</code>
  - [source] <code>p.A.get("csrfToken")</code> (x3)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_channel_create.8602b94971.js</code>
  - [source] <code>K.get("step")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_credentials_vault.6d0e89ea57.js</code>
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_memory.33e6c1b4f9.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>n=new URLSearchParams(window.location.search</code>
  - [source] <code>r=new URL(window.location.href</code>
  - [source] <code>t=new URL(window.location.href</code>
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_detail.9b8f8d7227.js</code>
  - [source] <code>h.A.get("csrfToken")</code> (x3)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_manage.1a405fdca7.js</code>
  - [source] <code>p.A.get("csrfToken")</code> (x3)
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/2616.68953e3608.js</code>
  - [source] <code>r.A.get("csrfToken")</code>
  - [source] <code>n=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/5074.8fd8bee520.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
  - [source] <code>u=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/7431.c85252ad29.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>eX.A.get("csrfToken")</code>
  - [source] <code>n.configManager.get("user")</code> (x7)
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>location.assign(</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8661.575e841d27.js</code>
  - [source] <code>c.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8934.16f82886be.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
  - [source] <code>u=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_detail.86a4d90ebf.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
  - [source] <code>n=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_dump_create.4de9662963.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>a=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_create.292a62ba40.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>a=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_detail.96ea3ee7bf.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>o=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_comparison.61405f08cd.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>a=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_detail.6ab57a014c.js</code>
  - [source] <code>.query.metricsExcludedMetricNames</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_tls.06fcecf40a.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>o=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_repository_detail.c228a8a794.js</code>
  - [source] <code>n.A.get("csrfToken")</code>
  - [source] <code>u=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/1453.3d4e7d8023.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("user")</code> (x7)
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2050.519f56b0a8.js</code>
  - [source] <code>e.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2314.a9e4208f13.js</code>
  - [source] <code>e.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2732.0aef4bf74d.js</code>
  - [source] <code>n.get("*")</code>
  - [source] <code>r.get("*")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3197.eda19b0eaa.js</code>
  - [source] <code>eX.A.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3372.8331a92330.js</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>i.configManager.get("user")</code> (x6)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>to.A.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/4337.b260caab3e.js</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/5314.f58e1230d9.js</code>
  - [source] <code>.query.length</code> (x2)
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/675.0aef9bd056.js</code>
  - [source] <code>o=new URL(window.location.href</code>
  - [source] <code>u=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7210.dbe0130553.js</code>
  - [source] <code>a.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7924.4e5ca1b471.js</code>
  - [source] <code>A.A.get("csrfToken")</code> (x3)
  - [source] <code>L.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/8728.361f718585.js</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/9857.cacc2df099.js</code>
  - [source] <code>e.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_batchInference_manage.e7d9547562.js</code>
  - [source] <code>i.A.get("csrfToken")</code>
  - [source] <code>r.get("*")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_create.addf5ad349.js</code>
  - [source] <code>i.A.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>n=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_detail.da9d422fb4.js</code>
  - [source] <code>tu.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_list.922f1ad7a0.js</code>
  - [source] <code>p.get("pageNumber")</code>
  - [source] <code>p.get("pageSize")</code>
  - [source] <code>r.get("*")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/306.75d9663c88.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/__federation_expose_routes.8289d3ab2d.js</code>
  - [source] <code>e=new URL(window.location.href</code>
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code>
  - [source] <code>i.searchParams.get("utm_source")</code>
  - [source] <code>t.get("subject")</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/533.e462f14b74.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/903.4e84f168f1.js</code>
  - [source] <code>i=new URL(window.location.href</code>
  - [source] <code>t=new URL(location.pathname</code>
  - [sink] <code>window.location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/1206.ce188f4c26.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>o.configManager.get("user")</code> (x7)
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2279.f71a69c7ae.js</code>
  - [source] <code>y.A.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2716.4c01e47af9.js</code>
  - [source] <code>o=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/4427.83192611c0.js</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/5227.c74122e561.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/6239.711d224b6f.js</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/7219.070e90099a.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8010.b4b0f9e430.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8156.7bf97dfbc9.js</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/898.4d2dc21a91.js</code>
  - [source] <code>i.searchParams.get("response-content-type")</code>
  - [source] <code>i.searchParams.get("x-oss-response-content-type")</code>
  - [source] <code>i.searchParams.get("x-tos-response-content-type")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code>
  - [source] <code>A.get("show")</code>
  - [source] <code>E.get("smooth")</code>
  - [source] <code>I.get("maxSurfaceAngle")</code>
  - [source] <code>I.get("minTurnAngle")</code>
  - [source] <code>P.get("blurScope")</code>
  - [source] <code>P.get("disabled")</code>
  - [source] <code>_.get("edgeDistance")</code>
  - [source] <code>a.get("blurScope")</code> (x5)
  - [source] <code>a.get("borderColor")</code>
  - [source] <code>a.get("dataBackgroundColor")</code>
  - [source] <code>a.get("disabled")</code> (x5)
  - [source] <code>a.get("fillerColor")</code>
  - [source] <code>a.get("focus")</code> (x3)
  - [source] <code>a.get("friction")</code>
  - [source] <code>a.get("gravity")</code>
  - [source] <code>a.get("handleLabel")</code>
  - [source] <code>a.get("ignoreForceLayout")</code>
  - [source] <code>a.get("inside")</code> (x2)
  - [source] <code>a.get("moveHandleIcon")</code>
  - [source] <code>a.get("moveHandleSize")</code>
  - [source] <code>a.get("realtime")</code>
  - [source] <code>a.get("scale")</code>
  - [source] <code>a.get("scaleSize")</code>
  - [source] <code>a.get("textShadowColor")</code>
  - [source] <code>c.get("blurScope")</code>
  - [source] <code>c.get("disabled")</code>
  - [source] <code>c.get("focus")</code>
  - [source] <code>d.get("blurScope")</code>
  - [source] <code>d.get("disabled")</code>
  - [source] <code>d.get("focus")</code>
  - [source] <code>e.get("alignWithLabel")</code>
  - [source] <code>e.get("axisExpandCenter")</code>
  - [source] <code>e.get("axisExpandCount")</code>
  - [source] <code>e.get("axisExpandDebounce")</code>
  - [source] <code>e.get("axisExpandWidth")</code>
  - [source] <code>e.get("backgroundColor")</code>
  - [source] <code>e.get("barMaxWidth")</code>
  - [source] <code>e.get("barMinWidth")</code>
  - [source] <code>e.get("borderColor")</code>
  - [source] <code>e.get("borderRadius")</code>
  - [source] <code>e.get("borderWidth")</code>
  - [source] <code>e.get("coordinateSystem")</code>
  - [source] <code>e.get("cursor")</code>
  - [source] <code>e.get("delay")</code>
  - [source] <code>e.get("itemGap")</code>
  - [source] <code>e.get("maxInterval")</code>
  - [source] <code>e.get("minInterval")</code>
  - [source] <code>e.get("minTurnAngle")</code>
  - [source] <code>e.get("orient")</code>
  - [source] <code>e.get("period")</code>
  - [source] <code>e.get("radarIndex")</code>
  - [source] <code>e.get("scaleLimit")</code>
  - [source] <code>e.get("show")</code>
  - [source] <code>e.get("showDetail")</code>
  - [source] <code>e.get("showLegendSymbol")</code>
  - [source] <code>e.get("throttle")</code>
  - [source] <code>e.get("triggerEvent")</code>
  - [source] <code>e.get("z")</code> (x2)
  - [source] <code>f.get("clip")</code> (x2)
  - [source] <code>h.get("formatter")</code>
  - [source] <code>h.get("formatterParams")</code>
  - [source] <code>h.get("lineHeight")</code>
  - [source] <code>i.get("blurScope")</code>
  - [source] <code>i.get("delay")</code>
  - [source] <code>i.get("disabled")</code>
  - [source] <code>i.get("easing")</code>
  - [source] <code>i.get("focus")</code>
  - [source] <code>i.get("inactiveColor")</code>
  - [source] <code>i.get("inverse")</code>
  - [source] <code>i.get("polyline")</code>
  - [source] <code>i.get("show")</code>
  - [source] <code>i.get("tooltip")</code>
  - [source] <code>i.get("triggerOn")</code>
  - [source] <code>i.get("useUTC")</code>
  - [source] <code>i.get("verticalAlign")</code>
  - [source] <code>k.normal.get("formatter")</code>
  - [source] <code>l.get("parallelIndex")</code>
  - [source] <code>m.get("show")</code>
  - [source] <code>m.get("textAlign")</code>
  - [source] <code>m.get("textBackgroundColor")</code>
  - [source] <code>m.get("textBorderRadius")</code>
  - [source] <code>m.get("textFill")</code>
  - [source] <code>m.get("textFontFamily")</code>
  - [source] <code>m.get("textFontSize")</code>
  - [source] <code>m.get("textFontStyle")</code>
  - [source] <code>m.get("textFontWeight")</code>
  - [source] <code>m.get("textPadding")</code>
  - [source] <code>m.get("textPosition")</code>
  - [source] <code>m.get("verticalAlign")</code>
  - [source] <code>n.get("axisExpandTriggerOn")</code>
  - [source] <code>n.get("axisExpandable")</code>
  - [source] <code>n.get("blurScope")</code> (x2)
  - [source] <code>n.get("boundaryGap")</code>
  - [source] <code>n.get("connectedBackgroundColor")</code>
  - [source] <code>n.get("dim")</code>
  - [source] <code>n.get("disabled")</code> (x2)
  - [source] <code>n.get("enabled")</code>
  - [source] <code>n.get("excludeComponents")</code>
  - [source] <code>n.get("focus")</code> (x2)
  - [source] <code>n.get("markLine")</code> (x2)
  - [source] <code>n.get("markPoint")</code> (x2)
  - [source] <code>n.get("pixelRatio")</code>
  - [source] <code>n.get("rotate")</code>
  - [source] <code>n.get("scale")</code>
  - [source] <code>n.get("seriesDataIndices")</code>
  - [source] <code>n.get("show")</code>
  - [source] <code>n.get("stack")</code> (x2)
  - [source] <code>n.get("symbolOffset")</code>
  - [source] <code>n.get("symbolRepeatDirection")</code>
  - [source] <code>n.get("symbolRotate")</code>
  - [source] <code>n.get("useUTC")</code>
  - [source] <code>n.get("value")</code>
  - [source] <code>n.get("z")</code>
  - [source] <code>n.get("zoomLock")</code>
  - [source] <code>n.hostModel.get("percentPrecision")</code>
  - [source] <code>o.get("blurScope")</code>
  - [source] <code>o.get("boundaryGap")</code>
  - [source] <code>o.get("disabled")</code> (x2)
  - [source] <code>o.get("focus")</code>
  - [source] <code>o.get("icon")</code>
  - [source] <code>o.get("order")</code>
  - [source] <code>o.get("rotate")</code>
  - [source] <code>o.get("show")</code> (x2)
  - [source] <code>o.get("symbolKeepAspect")</code>
  - [source] <code>o.get("symbolSize")</code>
  - [source] <code>o.get("textStyle")</code>
  - [source] <code>o.get("throttle")</code>
  - [source] <code>p.get("itemGap")</code>
  - [source] <code>p.get("itemSize")</code>
  - [source] <code>p.get("textStyle")</code>
  - [source] <code>r.get("animationDurationUpdate")</code>
  - [source] <code>r.get("animationEasingUpdate")</code>
  - [source] <code>r.get("emptyItemWidth")</code>
  - [source] <code>r.get("show")</code> (x3)
  - [source] <code>r.get("silent")</code>
  - [source] <code>s.get("alignTicks")</code>
  - [source] <code>s.get("blurScope")</code> (x2)
  - [source] <code>s.get("description")</code> (x2)
  - [source] <code>s.get("disabled")</code> (x2)
  - [source] <code>s.get("enabled")</code>
  - [source] <code>s.get("focus")</code>
  - [source] <code>s.get("formatter")</code>
  - [source] <code>s.get("icon")</code>
  - [source] <code>s.get("rotate")</code>
  - [source] <code>s.get("tooltip")</code>
  - [source] <code>t.ecModel.get("useUTC")</code> (x2)
  - [source] <code>t.get("activeOpacity")</code>
  - [source] <code>t.get("animation")</code> (x2)
  - [source] <code>t.get("aspectScale")</code>
  - [source] <code>t.get("autoCurveness")</code>
  - [source] <code>t.get("avoidLabelOverlap")</code>
  - [source] <code>t.get("axisExpandRate")</code>
  - [source] <code>t.get("backgroundColor")</code> (x3)
  - [source] <code>t.get("barMaxWidth")</code> (x2)
  - [source] <code>t.get("barMinWidth")</code>
  - [source] <code>t.get("barWidth")</code> (x2)
  - [source] <code>t.get("borderColor")</code>
  - [source] <code>t.get("borderRadius")</code>
  - [source] <code>t.get("borderWidth")</code>
  - [source] <code>t.get("boundaryGap")</code>
  - [source] <code>t.get("calendarIndex")</code>
  - [source] <code>t.get("center")</code> (x3)
  - [source] <code>t.get("containLabel")</code>
  - [source] <code>t.get("edgeSymbol")</code>
  - [source] <code>t.get("edgeSymbolSize")</code>
  - [source] <code>t.get("endAngle")</code>
  - [source] <code>t.get("enterable")</code> (x2)
  - [source] <code>t.get("extraCssText")</code>
  - [source] <code>t.get("geoCoord")</code>
  - [source] <code>t.get("gradientColor")</code>
  - [source] <code>t.get("handleIcon")</code>
  - [source] <code>t.get("handleSize")</code>
  - [source] <code>t.get("inactiveOpacity")</code>
  - [source] <code>t.get("indicatorIcon")</code>
  - [source] <code>t.get("indicatorSize")</code>
  - [source] <code>t.get("inverse")</code>
  - [source] <code>t.get("itemGap")</code> (x4)
  - [source] <code>t.get("itemSize")</code>
  - [source] <code>t.get("layoutIterations")</code>
  - [source] <code>t.get("legendHoverLink")</code>
  - [source] <code>t.get("max")</code> (x3)
  - [source] <code>t.get("maxSize")</code> (x2)
  - [source] <code>t.get("min")</code> (x3)
  - [source] <code>t.get("minShowLabelAngle")</code>
  - [source] <code>t.get("minSize")</code> (x2)
  - [source] <code>t.get("month")</code>
  - [source] <code>t.get("nameMap")</code> (x2)
  - [source] <code>t.get("nameProperty")</code>
  - [source] <code>t.get("nodeAlign")</code>
  - [source] <code>t.get("orient")</code> (x3)
  - [source] <code>t.get("parallelIndex")</code> (x3)
  - [source] <code>t.get("projection")</code>
  - [source] <code>t.get("radarIndex")</code>
  - [source] <code>t.get("radius")</code>
  - [source] <code>t.get("realtime")</code>
  - [source] <code>t.get("roam")</code> (x3)
  - [source] <code>t.get("scaleLimit")</code>
  - [source] <code>t.get("selectedMode")</code>
  - [source] <code>t.get("show")</code> (x8)
  - [source] <code>t.get("showContent")</code>
  - [source] <code>t.get("showEmptyCircle")</code>
  - [source] <code>t.get("showLegendSymbol")</code>
  - [source] <code>t.get("silent")</code> (x5)
  - [source] <code>t.get("smooth")</code>
  - [source] <code>t.get("stack")</code> (x3)
  - [source] <code>t.get("startAngle")</code> (x3)
  - [source] <code>t.get("step")</code>
  - [source] <code>t.get("subtarget")</code>
  - [source] <code>t.get("symbol")</code> (x2)
  - [source] <code>t.get("symbolKeepAspect")</code>
  - [source] <code>t.get("symbolMargin")</code>
  - [source] <code>t.get("symbolOffset")</code>
  - [source] <code>t.get("symbolSize")</code> (x2)
  - [source] <code>t.get("target")</code>
  - [source] <code>t.get("text")</code>
  - [source] <code>t.get("textBaseline")</code>
  - [source] <code>t.get("textVerticalAlign")</code>
  - [source] <code>t.get("title.0.text")</code>
  - [source] <code>t.get("transitionDuration")</code>
  - [source] <code>t.get("triggerEvent")</code>
  - [source] <code>t.get("triggerLineEvent")</code>
  - [source] <code>t.get("visualDimension")</code>
  - [source] <code>t.get("zoom")</code> (x3)
  - [source] <code>u.get("buttonColor")</code>
  - [source] <code>u.get("buttonTextColor")</code>
  - [source] <code>u.get("readOnly")</code>
  - [source] <code>u.get("title")</code>
  - [source] <code>v.get("blurScope")</code>
  - [source] <code>v.get("disabled")</code>
  - [source] <code>v.get("focus")</code>
  - [source] <code>v.get("show")</code> (x2)
  - [source] <code>v.get("value")</code>
  - [source] <code>w.get("blurScope")</code>
  - [source] <code>w.get("disabled")</code>
  - [source] <code>w.get("focus")</code>
  - [source] <code>w.get("show")</code>
  - [source] <code>x.get("formatter")</code>
  - [source] <code>x.get("show")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code>
  - [source] <code>e.get("hour")</code>
  - [source] <code>e.get("minute")</code>
  - [source] <code>r=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/977.a82025cf81.js</code>
  - [source] <code>a=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_api_key_manage.b870f1b214.js</code>
  - [source] <code>n=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_coding_plan_pane.13c650e89c.js</code>
  - [source] <code>o=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_manage.39c398fd0f.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_reward_plan.30a4a5d92e.js</code>
  - [source] <code>Q=new URL(window.location.href</code>
  - [source] <code>g=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_pickup_voucher.0dda270751.js</code>
  - [source] <code>r.A.get("csrfToken")</code>
  - [source] <code>x.get("pickup_voucher_id")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_project_management.b3b7526866.js</code>
  - [source] <code>a=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(location.search</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_token_calculator.5aa401a3b2.js</code>
  - [source] <code>a=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_usage_tracking_manage.d972bdb5cb.js</code>
  - [source] <code>o=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_vpc.280c5715d1.js</code>
  - [source] <code>o=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
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
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_comparison.fdf7c0861b.js</code>
  - [source] <code>n=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
  - [source] <code>.query.trim</code> (x4)

</details>

## All source and sink matches, unique per file (vendor)

<details><summary>All source and sink matches, unique per file (vendor)</summary>

- <code>https://accounts.google.com/gsi/client</code>
  - [source] <code>_.Tc.get("g_state")</code>
  - [source] <code>a.P.get("ll")</code>
  - [source] <code>a.h.get("onTokenRefresh")</code>
  - [sink] <code>location=</code>
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
- <code>https://res.gcloudcache.com/bp-fe/finance/volcf-sdk-app/static/js/577.ff151c5d.js</code>
  - [source] <code>I.A.get("csrfToken")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
  - [source] <code>o.configManager.get("user")</code> (x6)
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
- <code>https://res.gcloudcache.com/volc-fe/account-onboarding-app/static/js/async/249.e984d516.js</code>
  - [source] <code>Td.A.get(`${location.protocol}//${atob(t)}/obj/finance/env.json`)</code> (x2)
  - [source] <code>Vl.A.get("csrfToken")</code> (x2)
  - [source] <code>Vl.A.get("user_locale")</code> (x7)
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x15)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x5)
  - [source] <code>e.configManager.get("web_id")</code> (x15)
  - [source] <code>n.configManager.get("reportErrorCallback")</code> (x5)
  - [source] <code>o.configManager.get("user")</code> (x20)
  - [source] <code>r.configManager.get("user")</code> (x14)
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>location.assign(</code> (x5)
  - [sink] <code>window.location.href=</code> (x3)
- <code>https://res.gcloudcache.com/volc-fe/account-onboarding-app/static/js/main.d4898c72.js</code>
  - [source] <code>et.A.get("csrfToken")</code>
  - [source] <code>t=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/volc-fe/kyc-modal-app/static/js/async/671.ff467394.js</code>
  - [source] <code>H7e.get("user_locale")</code> (x2)
  - [source] <code>U7e.get("csrfToken")</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/navbar/static/js/main.732666406b.js</code>
  - [source] <code>o=new URLSearchParams(window.location.search</code>
  - [source] <code>r=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/navbar/static/js/vconsole.df85073f8e.js</code>
  - [source] <code>d.get("csrfToken")</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>l.get("/v2/config")</code>
  - [source] <code>o.configManager.get("user")</code> (x6)
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3120/async/169.e836de6f.js</code>
  - [source] <code>o=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.assign(</code> (x2)
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3120/async/4215.968f9162.js</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3120/async/8246.ec54937f.js</code>
  - [sink] <code>location.replace(</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3120/main.696c482e.js</code>
  - [source] <code>F.A.get("csrfToken")</code>
  - [source] <code>e.collect.configManager.get("user")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x6)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x2)
  - [source] <code>e.configManager.get("web_id")</code> (x6)
  - [source] <code>i.A.get("csrfToken")</code>
  - [source] <code>n.get("scenario")</code>
  - [source] <code>o.configManager.get("user")</code> (x13)
  - [source] <code>r.configManager.get("reportErrorCallback")</code> (x2)
  - [source] <code>t.get("state")</code> (x2)
  - [source] <code>e=new URLSearchParams(location.search</code>
  - [source] <code>n=new URLSearchParams(location.search</code> (x2)
  - [source] <code>r=new URLSearchParams(window.location.search</code> (x2)
  - [source] <code>t=new URL(window.location.href</code>
  - [source] <code>t=new URLSearchParams(location.search</code>
  - [sink] <code>location.assign(</code> (x3)
  - [sink] <code>window.location.assign(</code>
  - [sink] <code>window.location.href=</code> (x2)
  - [sink] <code>window.location.replace(</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/volcengine-platform-runtime/async.0b1bbb44.js</code>
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
- <code>https://res.gcloudcache.com/volc-fe/volcengine-platform-runtime/main.7e241f35.js</code>
  - [source] <code>o.Z.get("__spti")</code>
  - [source] <code>ry.Z.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x2)
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URLSearchParams(location.search</code>
  - [sink] <code>location.href=</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/1209.b1058b4f.js</code>
  - [source] <code>D.A.get("csrfToken")</code> (x3)
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/2700.85bfcf68.js</code>
  - [source] <code>_.A.get("csrfToken")</code>
  - [source] <code>l.A.get("csrfToken")</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/2907.9a0bad67.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>i.configManager.get("user")</code> (x7)
  - [source] <code>n.configManager.get("reportErrorCallback")</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/5010.2b0613a4.js</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>e.get("month")</code>
  - [source] <code>n.configManager.get("user")</code> (x7)
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
  - [source] <code>t=new URL(location.href</code>
  - [source] <code>.query.charCodeAt</code> (x2)
  - [source] <code>.query.length</code> (x2)
  - [source] <code>.query.spec</code> (x4)
  - [sink] <code>window.location.href=</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/589.d06e21ba.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/673.e7e6ad5b.js</code>
  - [source] <code>Y.A.get("csrfToken")</code> (x3)
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/7471.3d388194.js</code>
  - [source] <code>a.attributes.get("scriptlevel")</code>
  - [source] <code>e.attributes.get("columnalign")</code> (x2)
  - [source] <code>e.attributes.get("columnspacing")</code> (x2)
  - [source] <code>e.get("background-color")</code>
  - [source] <code>e.get("font-family")</code>
  - [source] <code>e.gullet.macros.get("\\df@tag")</code>
  - [source] <code>e.macros.get("\\df@tag")</code>
  - [source] <code>e.node.attributes.get("selection")</code>
  - [source] <code>i.get("mjx-keep-attrs")</code>
  - [source] <code>n.get("data-semantic-speech")</code>
  - [source] <code>n.get("lspace")</code> (x2)
  - [source] <code>n.get("mathsize")</code>
  - [source] <code>n.get("rspace")</code> (x2)
  - [source] <code>n.get("scriptlevel")</code>
  - [source] <code>n.get("scriptminsize")</code>
  - [source] <code>n.get("scriptsizemultiplier")</code>
  - [source] <code>n.node.attributes.get("bevelled")</code>
  - [source] <code>o.get("frame")</code>
  - [source] <code>r.get("depth")</code>
  - [source] <code>r.gullet.macros.get("\\df@tag")</code>
  - [source] <code>t.get("bevelled")</code> (x2)
  - [source] <code>t.get("largeop")</code>
  - [source] <code>t.get("linethickness")</code>
  - [source] <code>t.get("mathsize")</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/7834.77fa1ab9.js</code>
  - [source] <code>_.A.get("csrfToken")</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/__federation_expose_mcp.d92e838a.js</code>
  - [source] <code>te.A.get("csrfToken")</code> (x2)
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/__federation_expose_oldMcp.5353c608.js</code>
  - [source] <code>W.A.get("csrfToken")</code> (x2)
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/__federation_expose_rag.d03a95c5.js</code>
  - [source] <code>m.A.get("csrfToken")</code>
- <code>https://sf-model-ark.bytepluscdn.com/obj/ark-static-sg/ark-demo-house-byteplus/static/js/async/__federation_expose_vlm.100e89ea.js</code>
  - [source] <code>l.A.get("csrfToken")</code>

</details>

## Vendor-Only Routes

2 unique routes added only vendor/SDK files or matches. They are included as detailed route sections above.

## Duplicate Routes

75 duplicate routes produced no new JS files, source matches, or location sinks.

- Route 2 source; duplicates: 3-4
- Route 5 source; duplicates: 99-100
- Route 8 source; duplicates: 53-54, 79, 87, 90, 93, 117, 121, 124, 126-130, 132-134, 136-138, 141, 144-145
- Route 9 source; duplicates: 55, 80, 116, 118, 122-123, 125, 135
- Route 13 source; duplicates: 21, 23, 25, 27-28
- Route 14 source; duplicates: 15-20, 22, 24, 26
- Route 29 source; duplicates: 30, 32, 35, 41
- Route 36 source; duplicates: 37
- Route 40 source; duplicates: 45
- Route 57 source; duplicates: 59, 62-63
- Route 67 source; duplicates: 68
- Route 71 source; duplicates: 107
- Route 76 source; duplicates: 78
- Route 81 source; duplicates: 82-83, 88
- Route 97 source; duplicates: 98
- Route 101 source; duplicates: 102-106
- Route 109 source; duplicates: 111
- Route 119 source; duplicates: 120, 153
- Route 149 source; duplicates: 150-151

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
