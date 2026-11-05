# JS Regex Scan - Route-First Report

- Generated: 2026-11-05 03:04:17 UTC
- Routes: 153 tested | 67 unique | 86 duplicate | 0 errors
- Route coverage: 0 with new app surface | 53 vendor-only | 14 with no new discoveries
- Files: 132 unique JS files | 132 raw file URLs | 0 cache-busted duplicates collapsed | 704 unique file-match texts (704 raw)
- Matches: 633 source | 71 sink | 8 URLSearchParams `.get` flagged | 414 unique texts
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP | Unscanned: 0
- Only unique route IDs are listed. Missing route numbers are duplicates mapped near the end.
- Source matches are unique by match text within each route. Location sinks are per file and not deduped.
- Cache-busted duplicate URLs are collapsed by normalized URL (scheme + host + path).
- `App` = application `src_`/`~src_` chunks. Vendor, runtime, locale, replay, and SDK bundles are collapsed; vendor match texts are in the final index.
- URLSearchParams `.get` classification uses a same-file constructor/alias heuristic; function-parameter and cross-file flows still need manual tracing.

## Unique First Routes

53 unique first routes that load new JS files with unique regex matches. `--` separates entries.

https://console.byteplus.com/ark
--
https://console.byteplus.com/ark/region:ap-southeast-1/model
--
https://console.byteplus.com/ark/region:ap-southeast-1/model/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/model/comparison
--
https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/promotion/*
--
https://console.byteplus.com/ark/region:ap-southeast-1/promotion/*
--
https://console.byteplus.com/ark/region:ap-southeast-1/pickupVoucher
--
https://console.byteplus.com/ark/region:ap-southeast-1/gallery
--
https://console.byteplus.com/ark/region:ap-southeast-1/experience
--
https://console.byteplus.com/ark/region:ap-southeast-1/experience/*
--
https://console.byteplus.com/ark/region:ap-southeast-1/experience/creations
--
https://console.byteplus.com/ark/region:ap-southeast-1/endpoint
--
https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/create
--
https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/batchInference
--
https://console.byteplus.com/ark/region:ap-southeast-1/ipDashboard/*
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/quickstart
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/:id
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/create
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/environments
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills/:id
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/memory
--
https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/create
--
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create-deprecated
--
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/comparison
--
https://console.byteplus.com/ark/region:ap-southeast-1/finetune/tls
--
https://console.byteplus.com/ark/region:ap-southeast-1/customModel/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/eval/create
--
https://console.byteplus.com/ark/region:ap-southeast-1/eval/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/create
--
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/dataset/dump/create
--
https://console.byteplus.com/ark/region:ap-southeast-1/application
--
https://console.byteplus.com/ark/region:ap-southeast-1/application/claw
--
https://console.byteplus.com/ark/region:ap-southeast-1/application/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/assistant
--
https://console.byteplus.com/ark/region:ap-southeast-1/assistant/edit
--
https://console.byteplus.com/ark/region:ap-southeast-1/assistant/detail
--
https://console.byteplus.com/ark/region:ap-southeast-1/knowledge
--
https://console.byteplus.com/ark/region:ap-southeast-1/subscription/coding-plan
--
https://console.byteplus.com/ark/region:ap-southeast-1/openManagement/rewardPlan
--
https://console.byteplus.com/ark/region:ap-southeast-1/apiKey
--
https://console.byteplus.com/ark/region:ap-southeast-1/usageTracking
--
https://console.byteplus.com/ark/region:ap-southeast-1/vpc
--
https://console.byteplus.com/ark/region:ap-southeast-1/projectManagement
--
https://console.byteplus.com/ark/region:ap-southeast-1/tokenCalculator
--
https://console.byteplus.com/ark/region:ap-southeast-1/docs
--
https://console.byteplus.com/ark/region:ap-southeast-1/arkcli
--
https://console.byteplus.com/ark/region:ap-southeast-1/arkcli/login

## Vendor-Only Routes

53 unique routes added only vendor/SDK files or matches. These are summarized here; vendor match texts are in the final index.

| Route | URL | New vendor files | Vendor source | Vendor sinks |
|---:|---|---:|---:|---:|
| 1 | <code>https://console.byteplus.com/ark (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 8 | 36 | 13 |
| 5 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 3 | 3 | 2 |
| 6 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 1 | 0 |
| 7 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model/comparison (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 10 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/promotion/* (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 11 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/promotion/* (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 0 | 2 |
| 12 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/pickupVoucher (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 4 | 2 |
| 13 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/gallery (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 4 | 3 | 3 |
| 29 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 1 | 3 |
| 30 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/* (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 3 | 6 | 0 |
| 31 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/creations (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 9 | 2 |
| 46 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/endpoint (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 6 | 4 | 3 |
| 47 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 4 | 2 |
| 48 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 4 | 3 | 1 |
| 49 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 0 | 0 |
| 56 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/ipDashboard/* (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound?openAssetsLibrary=false)</code> | 5 | 3 | 1 |
| 57 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 3 | 3 |
| 58 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/quickstart (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 4 | 23 | 2 |
| 61 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/:id (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 65 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 1 |
| 67 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/environments (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 1 | 1 |
| 69 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 1 |
| 72 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 73 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills/:id (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 1 | 0 |
| 74 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/memory (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 76 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 1 | 0 |
| 81 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create-deprecated (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 1 | 2 |
| 84 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 3 | 3 | 0 |
| 85 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/comparison (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 86 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/tls (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 89 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/customModel/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 91 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/eval/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 92 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/eval/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 94 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 95 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 97 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/dump/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 108 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 1 | 3 |
| 110 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application/claw (final: https://signin.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fconsole.volcengine.com%2Farkclaw%2Fchat%2Fci-yepk65ajuorkm4wr7k1k%3Fagent%3Dmain)</code> | 5 | 7 | 10 |
| 112 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 5 | 28 | 2 |
| 113 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/assistant (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 1 | 1 |
| 114 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/assistant/edit (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 3 | 2 | 1 |
| 115 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/assistant/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 1 | 0 |
| 119 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/knowledge (final: https://console.byteplus.com/vikingdb/knowledge/region:vdb-knowledge+ap-southeast-1/collection/list?)</code> | 5 | 12 | 7 |
| 131 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/subscription/coding-plan (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 0 | 0 |
| 140 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/openManagement/rewardPlan (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 2 | 0 |
| 142 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/apiKey (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 0 | 0 |
| 143 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/usageTracking (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 237 | 0 |
| 146 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/vpc (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 0 |
| 147 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/projectManagement (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 1 | 1 |
| 148 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tokenCalculator (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 3 | 0 |
| 149 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/docs (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 1 | 0 |
| 152 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/arkcli (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 2 | 1 | 1 |
| 153 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/arkcli/login (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 1 | 0 | 1 |

## Unique Routes With No New Discoveries

14 unique routes loaded no new JS files and produced no new source matches or location sinks.

| Route | URL | Loaded files |
|---:|---|---:|
| 43 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_video/:id (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 14 |
| 44 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_canvas/:id (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 9 |
| 50 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/create (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 11 |
| 51 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/detail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 11 |
| 52 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/batchEpDetail (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 14 |
| 53 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/inferenceFoundry (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 9 |
| 64 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 9 |
| 66 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/:id (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 13 |
| 71 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault-oauth/callback (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 6 |
| 75 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 8 |
| 99 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tts/soundReplicate (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 10 |
| 102 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tts/recordingRecognition (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 7 |
| 139 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/openManagement (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 10 |
| 150 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/docs/product-overview (final: https://console.byteplus.com/ark/region:ap-southeast-1/notfound)</code> | 7 |

## Duplicate Routes

86 duplicate routes produced no new JS files, source matches, or location sinks.

- Route 1 source; duplicates: 2-4, 8-9, 54-55, 79, 87, 90, 109, 116-118, 122-125, 135, 138, 144-145
- Route 13 source; duplicates: 14-28
- Route 29 source; duplicates: 32-33, 35-42, 45
- Route 30 source; duplicates: 34
- Route 53 source; duplicates: 80, 93, 111, 121, 141
- Route 57 source; duplicates: 59-60, 62-63
- Route 67 source; duplicates: 68
- Route 69 source; duplicates: 70
- Route 71 source; duplicates: 101, 103-107, 126-127, 129-130, 132-133, 137
- Route 75 source; duplicates: 77
- Route 76 source; duplicates: 78
- Route 81 source; duplicates: 82-83, 88
- Route 94 source; duplicates: 96
- Route 97 source; duplicates: 98
- Route 99 source; duplicates: 100
- Route 102 source; duplicates: 128, 134, 136
- Route 119 source; duplicates: 120
- Route 149 source; duplicates: 151

## Vendor/SDK Match Index

<details><summary>All vendor/SDK source and sink matches, unique per file</summary>

- <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.222/9418.e579034e.js</code>
  - [source] <code>a.attributes.get("scriptlevel")</code>
  - [source] <code>e.attributes.get("columnalign")</code> (x2)
  - [source] <code>e.attributes.get("columnspacing")</code> (x2)
  - [source] <code>e.configManager.get("user_unique_id")</code> (x9)
  - [source] <code>e.configManager.get("user_unique_id_type")</code> (x3)
  - [source] <code>e.configManager.get("web_id")</code> (x9)
  - [source] <code>e.get("background-color")</code>
  - [source] <code>e.get("font-family")</code>
  - [source] <code>e.gullet.macros.get("\\df@tag")</code>
  - [source] <code>e.macros.get("\\df@tag")</code>
  - [source] <code>e.node.attributes.get("selection")</code>
  - [source] <code>i.configManager.get("user")</code> (x7)
  - [source] <code>i.get("frame")</code>
  - [source] <code>i.get("mjx-keep-attrs")</code>
  - [source] <code>n.configManager.get("user")</code> (x14)
  - [source] <code>n.get("data-semantic-speech")</code>
  - [source] <code>n.get("lspace")</code>
  - [source] <code>n.get("mathsize")</code>
  - [source] <code>n.get("rspace")</code>
  - [source] <code>n.get("scriptlevel")</code>
  - [source] <code>n.get("scriptminsize")</code>
  - [source] <code>n.get("scriptsizemultiplier")</code>
  - [source] <code>n.node.attributes.get("bevelled")</code>
  - [source] <code>o.Z.get("csrfToken")</code>
  - [source] <code>r.configManager.get("reportErrorCallback")</code> (x3)
  - [source] <code>r.get("depth")</code>
  - [source] <code>r.gullet.macros.get("\\df@tag")</code>
  - [source] <code>s.get("lspace")</code>
  - [source] <code>s.get("rspace")</code>
  - [source] <code>t.get("bevelled")</code> (x2)
  - [source] <code>t.get("largeop")</code>
  - [source] <code>t.get("linethickness")</code>
  - [source] <code>t.get("mathsize")</code>
  - [source] <code>t=new URL(location.href</code>
  - [sink] <code>location.href=</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.222/lib-arco.fa0a8e2c.js</code>
  - [source] <code>t.get("month")</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.222/lib-router.38527ea2.js</code>
  - [sink] <code>location.assign(</code> (x2)
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.222/main.ead65e34.js</code>
  - [source] <code>eO.Z.get("csrfToken")</code>
  - [source] <code>r.Z.get("AccountID")</code>
  - [source] <code>r.Z.get("account_active_time")</code>
  - [source] <code>t=new URL(window.location.href</code>
  - [source] <code>.query.service</code>
  - [sink] <code>location.href=</code> (x2)
  - [sink] <code>window.location.assign(</code>
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
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code>
  - [source] <code>i.Z.get("__spti")</code>
  - [source] <code>rb.Z.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x3)
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-ark/app-lab/vmok-remote-entry.46031a1d.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code>
  - [sink] <code>window.location.assign(</code> (x2)
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code>
  - [source] <code>r.get("*")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6390.72c02fadf9.js</code>
  - [source] <code>p=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6652.6caf14fb81.js</code>
  - [sink] <code>window.location.assign(</code>
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
- <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/__federation_expose_login.a297946d57.js</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/10260.3b056e3429.js</code>
  - [sink] <code>location.href=</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code>
  - [source] <code>r.searchParams.get("response-content-type")</code>
  - [source] <code>r.searchParams.get("x-oss-response-content-type")</code>
  - [source] <code>r.searchParams.get("x-tos-response-content-type")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/3625.d4b9487dc9.js</code>
  - [source] <code>e.get("month")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code>
  - [source] <code>a.searchParams.get("response-content-type")</code>
  - [source] <code>a.searchParams.get("x-oss-response-content-type")</code>
  - [source] <code>a.searchParams.get("x-tos-response-content-type")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/42494.c2231c54e7.js</code>
  - [source] <code>o.A.get("csrfToken")</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code>
  - [source] <code>n.get("WEBGL_multi_draw")</code>
  - [source] <code>t.get("EXT_color_buffer_float")</code>
  - [source] <code>t.get("WEBGL_multi_draw")</code> (x2)
  - [source] <code>t.get("WEBGL_multisampled_render_to_texture")</code>
  - [sink] <code>location =</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code>
  - [source] <code>a.get("compareModelIds")</code>
  - [source] <code>a.get("modelId")</code>
  - [source] <code>e=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/75664.0aad4702c6.js</code>
  - [source] <code>e.extensions.get("WEBGL_compressed_texture_astc")</code>
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
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/169.e836de6f.js</code>
  - [source] <code>o=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.assign(</code> (x2)
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/4215.968f9162.js</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/8246.ec54937f.js</code>
  - [sink] <code>location.replace(</code> (x2)
- <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/main.4b233780.js</code>
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
- <code>https://res.gcloudcache.com/volc-fe/volcengine-platform-runtime/main.7e241f35.js</code>
  - [source] <code>o.Z.get("__spti")</code>
  - [source] <code>ry.Z.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x2)
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>t=new URLSearchParams(location.search</code>
  - [sink] <code>location.href=</code>
  - [sink] <code>window.location.href=</code> (x2)

</details>

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
