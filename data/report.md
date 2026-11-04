# JS Regex Scan - Short Report

- Generated: 2026-11-04 13:22:10 UTC
- Inputs: URLs <code>data/urls.txt</code> | Auth <code>data/user-A.txt</code> (2 headers, 45 cookies)
- Routes: 153 tested, 78 duplicate, 0 errors
- Files: 145 with matches | File matches: 775 | Unique texts: 417 | R1: 259 | R2: 516 | Unscanned: 0
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP

## Routes With Unique Scan Results

| # | Route | HTTP | Files | Matches | New files | New matches | Note |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | <code>https://console.byteplus.com/ark</code> | 200 | 9 | 63 | 9 | 63 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 5 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model</code> | 200 | 10 | 71 | 3 | 12 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 6 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model/detail</code> | 200 | 10 | 72 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 7 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model/comparison</code> | 200 | 10 | 71 | 1 | 2 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 10 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/model-settings/promotion/*</code> | 200 | 8 | 60 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 11 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/promotion/*</code> | 200 | 10 | 70 | 3 | 11 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 12 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/pickupVoucher</code> | 200 | 13 | 74 | 5 | 14 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 13 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/gallery</code> | 200 | 11 | 75 | 4 | 16 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 22 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/gallery/ai-verify</code> | 200 | 12 | 76 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 29 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience</code> | 200 | 15 | 88 | 7 | 28 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 31 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/creations</code> | 200 | 18 | 95 | 5 | 11 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 32 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_chat</code> | 200 | 16 | 89 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 35 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/audio-generation</code> | 200 | 12 | 81 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 36 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/gen_3d</code> | 200 | 23 | 103 | 5 | 8 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 38 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/voice</code> | 200 | 22 | 102 | 2 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 43 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_video/:id</code> | 200 | 15 | 88 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 44 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/experience/share_canvas/:id</code> | 200 | 11 | 75 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 46 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/endpoint</code> | 200 | 13 | 75 | 6 | 16 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 47 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/create</code> | 200 | 15 | 85 | 5 | 15 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 48 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/endpoint/detail</code> | 200 | 19 | 86 | 5 | 10 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 49 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference</code> | 200 | 14 | 76 | 2 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 50 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/create</code> | 200 | 12 | 73 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 51 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/detail</code> | 200 | 12 | 73 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 52 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/batchInference/batchEpDetail</code> | 200 | 16 | 80 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 56 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/ipDashboard/*</code> | 200 | 11 | 73 | 2 | 6 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 57 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents</code> | 200 | 12 | 81 | 5 | 22 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 58 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/quickstart</code> | 200 | 14 | 100 | 4 | 29 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 60 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/create</code> | 200 | 13 | 83 | 1 | 2 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 61 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/:id</code> | 200 | 12 | 74 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 62 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/agents/:id/edit</code> | 200 | 14 | 84 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 64 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions</code> | 200 | 10 | 78 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 65 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/create</code> | 200 | 14 | 84 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 66 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/sessions/:id</code> | 200 | 13 | 97 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 67 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/environments</code> | 200 | 12 | 73 | 1 | 2 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 68 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/environments/:id</code> | 200 | 11 | 72 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 69 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault</code> | 200 | 10 | 70 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 71 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/credentials-vault-oauth/callback</code> | 200 | 7 | 59 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 72 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills</code> | 200 | 11 | 72 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 73 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/skills/:id</code> | 200 | 12 | 74 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 74 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/memory</code> | 200 | 10 | 70 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 75 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels</code> | 200 | 9 | 69 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 76 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/create</code> | 200 | 11 | 71 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 77 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/channels/:id</code> | 200 | 10 | 70 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 79 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/managed-agents/studio</code> | 200 | 10 | 64 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 81 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create-deprecated</code> | 200 | 10 | 73 | 2 | 13 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 82 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/create</code> | 200 | 9 | 72 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 84 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/detail</code> | 200 | 11 | 74 | 3 | 6 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 85 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/comparison</code> | 200 | 9 | 71 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 86 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/finetune/tls</code> | 200 | 9 | 72 | 1 | 4 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 89 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/customModel/detail</code> | 200 | 9 | 71 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 91 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/eval/create</code> | 200 | 9 | 72 | 1 | 4 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 92 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/eval/detail</code> | 200 | 10 | 72 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 94 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/create</code> | 200 | 10 | 73 | 1 | 4 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 95 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/detail</code> | 200 | 9 | 71 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 97 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/dataset/dump/create</code> | 200 | 9 | 71 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 100 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tts/speechSynthesis</code> | 200 | 11 | 72 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 104 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tts/simulS2S</code> | 200 | 8 | 60 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 108 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application</code> | 200 | 13 | 73 | 5 | 13 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 110 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application/claw</code> | 200 | 8 | 37 | 8 | 37 | final URL: https://signin.volcengine.com/auth/login?redirectURI=https%3A%2F%2Fconsole.volcengine.com%2Farkclaw%2Fchat%2Fci-yepk65ajuorkm4wr7k1k%3Fagent%3Dmain |
| 112 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/application/detail</code> | 200 | 17 | 111 | 6 | 41 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 113 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/assistant</code> | 200 | 13 | 74 | 2 | 4 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 114 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/assistant/edit</code> | 200 | 17 | 115 | 3 | 9 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 115 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/assistant/detail</code> | 200 | 15 | 109 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 119 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/knowledge</code> | 200 | 5 | 56 | 5 | 56 | final URL: https://console.byteplus.com/vikingdb/knowledge/region:vdb-knowledge+ap-southeast-1/collection/list? |
| 131 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/subscription/coding-plan</code> | 200 | 12 | 71 | 2 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 140 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/openManagement/rewardPlan</code> | 200 | 10 | 70 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 142 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/apiKey</code> | 200 | 11 | 70 | 2 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 143 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/usageTracking</code> | 200 | 11 | 308 | 2 | 241 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 146 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/vpc</code> | 200 | 11 | 71 | 1 | 3 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 147 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/projectManagement</code> | 200 | 12 | 75 | 2 | 7 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 148 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/tokenCalculator</code> | 200 | 12 | 74 | 2 | 6 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 149 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/docs</code> | 200 | 9 | 61 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 150 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/docs/product-overview</code> | 200 | 8 | 60 | 0 | 0 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 152 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/arkcli</code> | 200 | 10 | 70 | 2 | 10 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |
| 153 | <code>https://console.byteplus.com/ark/region:ap-southeast-1/arkcli/login</code> | 200 | 10 | 70 | 1 | 1 | final URL: https://console.byteplus.com/ark/region:ap-southeast-1/notfound |

## Unique Matched Files

Each file lists its matches once. `R1`/`R2` are the regex labels; `xN` is the occurrence count when greater than one. `first` is the first-seen route number and `routes` is the compressed loaded-on route list; both map to the table above.

<details><summary><b>1.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9098.00b2937f19.js</code> - <b>239</b> matches (R1 1 / R2 238) - first 143 - routes: 143</summary>

- R1: <code>location.href=t</code>
- R2: <code>A.get("show")</code>
- R2: <code>E.get("smooth")</code>
- R2: <code>I.get("maxSurfaceAngle")</code>
- R2: <code>I.get("minTurnAngle")</code>
- R2: <code>P.get("blurScope")</code>
- R2: <code>P.get("disabled")</code>
- R2: <code>_.get("edgeDistance")</code>
- R2: <code>a.get("blurScope")</code> (x5)
- R2: <code>a.get("borderColor")</code>
- R2: <code>a.get("dataBackgroundColor")</code>
- R2: <code>a.get("disabled")</code> (x5)
- R2: <code>a.get("fillerColor")</code>
- R2: <code>a.get("focus")</code> (x3)
- R2: <code>a.get("friction")</code>
- R2: <code>a.get("gravity")</code>
- R2: <code>a.get("handleLabel")</code>
- R2: <code>a.get("ignoreForceLayout")</code>
- R2: <code>a.get("inside")</code> (x2)
- R2: <code>a.get("moveHandleIcon")</code>
- R2: <code>a.get("moveHandleSize")</code>
- R2: <code>a.get("realtime")</code>
- R2: <code>a.get("scale")</code>
- R2: <code>a.get("scaleSize")</code>
- R2: <code>a.get("textShadowColor")</code>
- R2: <code>c.get("blurScope")</code>
- R2: <code>c.get("disabled")</code>
- R2: <code>c.get("focus")</code>
- R2: <code>d.get("blurScope")</code>
- R2: <code>d.get("disabled")</code>
- R2: <code>d.get("focus")</code>
- R2: <code>e.get("alignWithLabel")</code>
- R2: <code>e.get("axisExpandCenter")</code>
- R2: <code>e.get("axisExpandCount")</code>
- R2: <code>e.get("axisExpandDebounce")</code>
- R2: <code>e.get("axisExpandWidth")</code>
- R2: <code>e.get("backgroundColor")</code>
- R2: <code>e.get("barMaxWidth")</code>
- R2: <code>e.get("barMinWidth")</code>
- R2: <code>e.get("borderColor")</code>
- R2: <code>e.get("borderRadius")</code>
- R2: <code>e.get("borderWidth")</code>
- R2: <code>e.get("coordinateSystem")</code>
- R2: <code>e.get("cursor")</code>
- R2: <code>e.get("delay")</code>
- R2: <code>e.get("itemGap")</code>
- R2: <code>e.get("maxInterval")</code>
- R2: <code>e.get("minInterval")</code>
- R2: <code>e.get("minTurnAngle")</code>
- R2: <code>e.get("orient")</code>
- R2: <code>e.get("period")</code>
- R2: <code>e.get("radarIndex")</code>
- R2: <code>e.get("scaleLimit")</code>
- R2: <code>e.get("show")</code>
- R2: <code>e.get("showDetail")</code>
- R2: <code>e.get("showLegendSymbol")</code>
- R2: <code>e.get("throttle")</code>
- R2: <code>e.get("triggerEvent")</code>
- R2: <code>e.get("z")</code> (x2)
- R2: <code>f.get("clip")</code> (x2)
- R2: <code>h.get("formatter")</code>
- R2: <code>h.get("formatterParams")</code>
- R2: <code>h.get("lineHeight")</code>
- R2: <code>i.get("blurScope")</code>
- R2: <code>i.get("delay")</code>
- R2: <code>i.get("disabled")</code>
- R2: <code>i.get("easing")</code>
- R2: <code>i.get("focus")</code>
- R2: <code>i.get("inactiveColor")</code>
- R2: <code>i.get("inverse")</code>
- R2: <code>i.get("polyline")</code>
- R2: <code>i.get("show")</code>
- R2: <code>i.get("tooltip")</code>
- R2: <code>i.get("triggerOn")</code>
- R2: <code>i.get("useUTC")</code>
- R2: <code>i.get("verticalAlign")</code>
- R2: <code>k.normal.get("formatter")</code>
- R2: <code>l.get("parallelIndex")</code>
- R2: <code>m.get("show")</code>
- R2: <code>m.get("textAlign")</code>
- R2: <code>m.get("textBackgroundColor")</code>
- R2: <code>m.get("textBorderRadius")</code>
- R2: <code>m.get("textFill")</code>
- R2: <code>m.get("textFontFamily")</code>
- R2: <code>m.get("textFontSize")</code>
- R2: <code>m.get("textFontStyle")</code>
- R2: <code>m.get("textFontWeight")</code>
- R2: <code>m.get("textPadding")</code>
- R2: <code>m.get("textPosition")</code>
- R2: <code>m.get("verticalAlign")</code>
- R2: <code>n.get("axisExpandTriggerOn")</code>
- R2: <code>n.get("axisExpandable")</code>
- R2: <code>n.get("blurScope")</code> (x2)
- R2: <code>n.get("boundaryGap")</code>
- R2: <code>n.get("connectedBackgroundColor")</code>
- R2: <code>n.get("dim")</code>
- R2: <code>n.get("disabled")</code> (x2)
- R2: <code>n.get("enabled")</code>
- R2: <code>n.get("excludeComponents")</code>
- R2: <code>n.get("focus")</code> (x2)
- R2: <code>n.get("markLine")</code> (x2)
- R2: <code>n.get("markPoint")</code> (x2)
- R2: <code>n.get("pixelRatio")</code>
- R2: <code>n.get("rotate")</code>
- R2: <code>n.get("scale")</code>
- R2: <code>n.get("seriesDataIndices")</code>
- R2: <code>n.get("show")</code>
- R2: <code>n.get("stack")</code> (x2)
- R2: <code>n.get("symbolOffset")</code>
- R2: <code>n.get("symbolRepeatDirection")</code>
- R2: <code>n.get("symbolRotate")</code>
- R2: <code>n.get("useUTC")</code>
- R2: <code>n.get("value")</code>
- R2: <code>n.get("z")</code>
- R2: <code>n.get("zoomLock")</code>
- R2: <code>n.hostModel.get("percentPrecision")</code>
- R2: <code>o.get("blurScope")</code>
- R2: <code>o.get("boundaryGap")</code>
- R2: <code>o.get("disabled")</code> (x2)
- R2: <code>o.get("focus")</code>
- R2: <code>o.get("icon")</code>
- R2: <code>o.get("order")</code>
- R2: <code>o.get("rotate")</code>
- R2: <code>o.get("show")</code> (x2)
- R2: <code>o.get("symbolKeepAspect")</code>
- R2: <code>o.get("symbolSize")</code>
- R2: <code>o.get("textStyle")</code>
- R2: <code>o.get("throttle")</code>
- R2: <code>p.get("itemGap")</code>
- R2: <code>p.get("itemSize")</code>
- R2: <code>p.get("textStyle")</code>
- R2: <code>r.get("animationDurationUpdate")</code>
- R2: <code>r.get("animationEasingUpdate")</code>
- R2: <code>r.get("emptyItemWidth")</code>
- R2: <code>r.get("show")</code> (x3)
- R2: <code>r.get("silent")</code>
- R2: <code>s.get("alignTicks")</code>
- R2: <code>s.get("blurScope")</code> (x2)
- R2: <code>s.get("description")</code> (x2)
- R2: <code>s.get("disabled")</code> (x2)
- R2: <code>s.get("enabled")</code>
- R2: <code>s.get("focus")</code>
- R2: <code>s.get("formatter")</code>
- R2: <code>s.get("icon")</code>
- R2: <code>s.get("rotate")</code>
- R2: <code>s.get("tooltip")</code>
- R2: <code>t.ecModel.get("useUTC")</code> (x2)
- R2: <code>t.get("activeOpacity")</code>
- R2: <code>t.get("animation")</code> (x2)
- R2: <code>t.get("aspectScale")</code>
- R2: <code>t.get("autoCurveness")</code>
- R2: <code>t.get("avoidLabelOverlap")</code>
- R2: <code>t.get("axisExpandRate")</code>
- R2: <code>t.get("backgroundColor")</code> (x3)
- R2: <code>t.get("barMaxWidth")</code> (x2)
- R2: <code>t.get("barMinWidth")</code>
- R2: <code>t.get("barWidth")</code> (x2)
- R2: <code>t.get("borderColor")</code>
- R2: <code>t.get("borderRadius")</code>
- R2: <code>t.get("borderWidth")</code>
- R2: <code>t.get("boundaryGap")</code>
- R2: <code>t.get("calendarIndex")</code>
- R2: <code>t.get("center")</code> (x3)
- R2: <code>t.get("containLabel")</code>
- R2: <code>t.get("edgeSymbol")</code>
- R2: <code>t.get("edgeSymbolSize")</code>
- R2: <code>t.get("endAngle")</code>
- R2: <code>t.get("enterable")</code> (x2)
- R2: <code>t.get("extraCssText")</code>
- R2: <code>t.get("geoCoord")</code>
- R2: <code>t.get("gradientColor")</code>
- R2: <code>t.get("handleIcon")</code>
- R2: <code>t.get("handleSize")</code>
- R2: <code>t.get("inactiveOpacity")</code>
- R2: <code>t.get("indicatorIcon")</code>
- R2: <code>t.get("indicatorSize")</code>
- R2: <code>t.get("inverse")</code>
- R2: <code>t.get("itemGap")</code> (x4)
- R2: <code>t.get("itemSize")</code>
- R2: <code>t.get("layoutIterations")</code>
- R2: <code>t.get("legendHoverLink")</code>
- R2: <code>t.get("max")</code> (x3)
- R2: <code>t.get("maxSize")</code> (x2)
- R2: <code>t.get("min")</code> (x3)
- R2: <code>t.get("minShowLabelAngle")</code>
- R2: <code>t.get("minSize")</code> (x2)
- R2: <code>t.get("month")</code>
- R2: <code>t.get("nameMap")</code> (x2)
- R2: <code>t.get("nameProperty")</code>
- R2: <code>t.get("nodeAlign")</code>
- R2: <code>t.get("orient")</code> (x3)
- R2: <code>t.get("parallelIndex")</code> (x3)
- R2: <code>t.get("projection")</code>
- R2: <code>t.get("radarIndex")</code>
- R2: <code>t.get("radius")</code>
- R2: <code>t.get("realtime")</code>
- R2: <code>t.get("roam")</code> (x3)
- R2: <code>t.get("scaleLimit")</code>
- R2: <code>t.get("selectedMode")</code>
- R2: <code>t.get("show")</code> (x8)
- R2: <code>t.get("showContent")</code>
- R2: <code>t.get("showEmptyCircle")</code>
- R2: <code>t.get("showLegendSymbol")</code>
- R2: <code>t.get("silent")</code> (x5)
- R2: <code>t.get("smooth")</code>
- R2: <code>t.get("stack")</code> (x3)
- R2: <code>t.get("startAngle")</code> (x3)
- R2: <code>t.get("step")</code>
- R2: <code>t.get("subtarget")</code>
- R2: <code>t.get("symbol")</code> (x2)
- R2: <code>t.get("symbolKeepAspect")</code>
- R2: <code>t.get("symbolMargin")</code>
- R2: <code>t.get("symbolOffset")</code>
- R2: <code>t.get("symbolSize")</code> (x2)
- R2: <code>t.get("target")</code>
- R2: <code>t.get("text")</code>
- R2: <code>t.get("textBaseline")</code>
- R2: <code>t.get("textVerticalAlign")</code>
- R2: <code>t.get("title.0.text")</code>
- R2: <code>t.get("transitionDuration")</code>
- R2: <code>t.get("triggerEvent")</code>
- R2: <code>t.get("triggerLineEvent")</code>
- R2: <code>t.get("visualDimension")</code>
- R2: <code>t.get("zoom")</code> (x3)
- R2: <code>u.get("buttonColor")</code>
- R2: <code>u.get("buttonTextColor")</code>
- R2: <code>u.get("readOnly")</code>
- R2: <code>u.get("title")</code>
- R2: <code>v.get("blurScope")</code>
- R2: <code>v.get("disabled")</code>
- R2: <code>v.get("focus")</code>
- R2: <code>v.get("show")</code> (x2)
- R2: <code>v.get("value")</code>
- R2: <code>w.get("blurScope")</code>
- R2: <code>w.get("disabled")</code>
- R2: <code>w.get("focus")</code>
- R2: <code>w.get("show")</code>
- R2: <code>x.get("formatter")</code>
- R2: <code>x.get("show")</code>

</details>

<details><summary><b>2.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.221/1020.7032cad3.js</code> - <b>37</b> matches (R1 4 / R2 33) - first 119 - routes: 119</summary>

- R1: <code>location.assign(</code>
- R1: <code>location.href=e</code> (x3)
- R1: <code>location=r</code>
- R1: <code>new URL(location.href</code> (x5)
- R2: <code>a.attributes.get("scriptlevel")</code>
- R2: <code>e.attributes.get("columnalign")</code> (x2)
- R2: <code>e.attributes.get("columnspacing")</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x9)
- R2: <code>e.configManager.get("user_unique_id_type")</code> (x3)
- R2: <code>e.configManager.get("web_id")</code> (x9)
- R2: <code>e.get("background-color")</code>
- R2: <code>e.get("font-family")</code>
- R2: <code>e.gullet.macros.get("\\df@tag")</code>
- R2: <code>e.macros.get("\\df@tag")</code>
- R2: <code>e.node.attributes.get("selection")</code>
- R2: <code>i.configManager.get("user")</code> (x7)
- R2: <code>i.get("frame")</code>
- R2: <code>i.get("mjx-keep-attrs")</code>
- R2: <code>n.configManager.get("user")</code> (x14)
- R2: <code>n.get("data-semantic-speech")</code>
- R2: <code>n.get("lspace")</code>
- R2: <code>n.get("mathsize")</code>
- R2: <code>n.get("rspace")</code>
- R2: <code>n.get("scriptlevel")</code>
- R2: <code>n.get("scriptminsize")</code>
- R2: <code>n.get("scriptsizemultiplier")</code>
- R2: <code>n.node.attributes.get("bevelled")</code>
- R2: <code>o.Z.get("csrfToken")</code>
- R2: <code>r.configManager.get("reportErrorCallback")</code> (x3)
- R2: <code>r.get("depth")</code>
- R2: <code>r.gullet.macros.get("\\df@tag")</code>
- R2: <code>s.get("lspace")</code>
- R2: <code>s.get("rspace")</code>
- R2: <code>t.get("bevelled")</code> (x2)
- R2: <code>t.get("largeop")</code>
- R2: <code>t.get("linethickness")</code>
- R2: <code>t.get("mathsize")</code>

</details>

<details><summary><b>3.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7168.0e22514f5d.js</code> - <b>28</b> matches (R1 1 / R2 27) - first 112 - routes: 112, 114-115</summary>

- R1: <code>location.assign(</code> (x2)
- R2: <code>a.attributes.get("scriptlevel")</code>
- R2: <code>e.attributes.get("columnalign")</code> (x2)
- R2: <code>e.attributes.get("columnspacing")</code> (x2)
- R2: <code>e.get("background-color")</code>
- R2: <code>e.get("font-family")</code>
- R2: <code>e.gullet.macros.get("\\df@tag")</code>
- R2: <code>e.macros.get("\\df@tag")</code>
- R2: <code>e.node.attributes.get("selection")</code>
- R2: <code>eJ.A.get("csrfToken")</code>
- R2: <code>i.get("lspace")</code>
- R2: <code>i.get("rspace")</code>
- R2: <code>n.get("data-semantic-speech")</code>
- R2: <code>n.get("lspace")</code>
- R2: <code>n.get("mathsize")</code>
- R2: <code>n.get("rspace")</code>
- R2: <code>n.get("scriptlevel")</code>
- R2: <code>n.get("scriptminsize")</code>
- R2: <code>n.get("scriptsizemultiplier")</code>
- R2: <code>n.node.attributes.get("bevelled")</code>
- R2: <code>o.get("frame")</code>
- R2: <code>o.get("mjx-keep-attrs")</code>
- R2: <code>r.get("depth")</code>
- R2: <code>r.gullet.macros.get("\\df@tag")</code>
- R2: <code>t.get("bevelled")</code> (x2)
- R2: <code>t.get("largeop")</code>
- R2: <code>t.get("linethickness")</code>
- R2: <code>t.get("mathsize")</code>

</details>

<details><summary><b>4.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/84279.11ada4c40e.js</code> - <b>21</b> matches (R1 0 / R2 21) - first 58 - routes: 58, 66</summary>

- R2: <code>Q.get("background-color")</code>
- R2: <code>Q.get("font-family")</code>
- R2: <code>Q.node.attributes.get("selection")</code>
- R2: <code>T.get("depth")</code>
- R2: <code>e.get("data-semantic-speech")</code>
- R2: <code>e.get("lspace")</code>
- R2: <code>e.get("mathsize")</code>
- R2: <code>e.get("rspace")</code>
- R2: <code>e.get("scriptlevel")</code>
- R2: <code>e.get("scriptminsize")</code>
- R2: <code>e.get("scriptsizemultiplier")</code>
- R2: <code>e.node.attributes.get("bevelled")</code>
- R2: <code>n.get("lspace")</code>
- R2: <code>n.get("rspace")</code>
- R2: <code>o.attributes.get("scriptlevel")</code>
- R2: <code>r.get("frame")</code>
- R2: <code>r.get("mjx-keep-attrs")</code>
- R2: <code>t.get("bevelled")</code> (x2)
- R2: <code>t.get("largeop")</code>
- R2: <code>t.get("linethickness")</code>
- R2: <code>t.get("mathsize")</code>

</details>

<details><summary><b>5.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/main.4b233780.js</code> - <b>19</b> matches (R1 9 / R2 10) - first 110 - routes: 110</summary>

- R1: <code>location.assign(</code> (x5)
- R1: <code>location.href=n</code>
- R1: <code>location.href=t</code> (x2)
- R1: <code>location=r</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(location.search</code> (x4)
- R1: <code>new URLSearchParams(window.location.search</code> (x3)
- R1: <code>window.location.assign(</code> (x3)
- R1: <code>window.location.replace(</code> (x3)
- R2: <code>F.A.get("csrfToken")</code>
- R2: <code>e.collect.configManager.get("user")</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x6)
- R2: <code>e.configManager.get("user_unique_id_type")</code> (x2)
- R2: <code>e.configManager.get("web_id")</code> (x6)
- R2: <code>i.A.get("csrfToken")</code>
- R2: <code>n.get("scenario")</code>
- R2: <code>o.configManager.get("user")</code> (x13)
- R2: <code>r.configManager.get("reportErrorCallback")</code> (x2)
- R2: <code>t.get("state")</code> (x2)

</details>

<details><summary><b>6.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime-os/main.cea8b975.js</code> - <b>18</b> matches (R1 5 / R2 13) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>location.href=e</code> (x2)
- R1: <code>location.href=f</code>
- R1: <code>location.href=i</code>
- R1: <code>new URLSearchParams(location.search</code> (x2)
- R1: <code>window.location.replace(</code>
- R2: <code>e.collect.configManager.get("custom")</code>
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>oH.get("_TEA_VE_APIHOST")</code>
- R2: <code>oH.get("_VISUAL_EDITOR_U")</code>
- R2: <code>oH.get("_VISUAL_EDITOR_V")</code>
- R2: <code>oH.get("lang")</code>
- R2: <code>r.configManager.get("user")</code> (x6)
- R2: <code>t.get("AccountID")</code>
- R2: <code>t.get("__spti")</code>
- R2: <code>t.get("csrfToken")</code>

</details>

<details><summary><b>7.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/async-main.6f63ed355c.js</code> - <b>15</b> matches (R1 9 / R2 6) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=`</code> (x3)
- R1: <code>location.href=e</code>
- R1: <code>location.href=t</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(location.search</code> (x2)
- R1: <code>new URLSearchParams(window.location.search</code> (x4)
- R1: <code>window.location.assign(</code> (x2)
- R1: <code>window.location.replace(</code> (x4)
- R2: <code>I.A.get("csrfToken")</code>
- R2: <code>e.get("userInfo")</code> (x2)
- R2: <code>i.A.get("csrfToken")</code> (x3)
- R2: <code>i.get("t")</code>
- R2: <code>sC.A.get("csrfToken")</code>
- R2: <code>t.get("userInfo")</code> (x2)

</details>

<details><summary><b>8.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/7085.2e80da3efd.js</code> - <b>14</b> matches (R1 6 / R2 8) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>location.assign(</code> (x3)
- R1: <code>location.href=e</code> (x2)
- R1: <code>new URL(location.href</code> (x5)
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R1: <code>window.location.replace(</code>
- R2: <code>e.collect.configManager.get("user")</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x12)
- R2: <code>e.configManager.get("user_unique_id_type")</code> (x4)
- R2: <code>e.configManager.get("web_id")</code> (x12)
- R2: <code>g.A.get("csrfToken")</code>
- R2: <code>i.configManager.get("user")</code> (x13)
- R2: <code>n.configManager.get("user")</code> (x14)
- R2: <code>r.configManager.get("reportErrorCallback")</code> (x4)

</details>

<details><summary><b>9.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.221/main.a5f76399.js</code> - <b>10</b> matches (R1 7 / R2 3) - first 119 - routes: 119</summary>

- R1: <code>.query.service</code>
- R1: <code>location.href="</code>
- R1: <code>location.href=d</code> (x2)
- R1: <code>location.href=t</code>
- R1: <code>new URL(window.location.href</code> (x2)
- R1: <code>new URLSearchParams(window.location.search</code>
- R1: <code>window.location.assign(</code>
- R2: <code>eO.Z.get("csrfToken")</code>
- R2: <code>r.Z.get("AccountID")</code>
- R2: <code>r.Z.get("account_active_time")</code>

</details>

<details><summary><b>10.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/91274.4bb0a4afa9.js</code> - <b>9</b> matches (R1 3 / R2 6) - first 29 - routes: 29, 31-32, 35-36, 38, 43-44</summary>

- R1: <code>location.assign(</code>
- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x6)
- R2: <code>e.configManager.get("user_unique_id_type")</code> (x2)
- R2: <code>e.configManager.get("web_id")</code> (x6)
- R2: <code>n.configManager.get("reportErrorCallback")</code> (x2)
- R2: <code>o.configManager.get("user")</code> (x7)
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>11.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/27065.b90e3594ea.js</code> - <b>9</b> matches (R1 1 / R2 8) - first 57 - routes: 57, 60, 62, 64-65</summary>

- R1: <code>location.assign(</code>
- R2: <code>e.collect.configManager.get("user")</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>e.get("month")</code>
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>o.configManager.get("user")</code> (x6)
- R2: <code>tl.A.get("csrfToken")</code>

</details>

<details><summary><b>12.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/7431.c85252ad29.js</code> - <b>9</b> matches (R1 3 / R2 6) - first 81 - routes: 81-82, 84-86, 89, 91-92, 94-95, 97</summary>

- R1: <code>location.assign(</code>
- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>eX.A.get("csrfToken")</code>
- R2: <code>n.configManager.get("user")</code> (x7)
- R2: <code>r.configManager.get("reportErrorCallback")</code>

</details>

<details><summary><b>13.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/main.cc0b7d7591.js</code> - <b>8</b> matches (R1 7 / R2 1) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>location.assign(</code> (x2)
- R1: <code>location.href=n</code>
- R1: <code>location.href=t</code>
- R1: <code>location.replace(</code>
- R1: <code>new URL(location.pathname</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>p.searchParams.get("paths")</code>

</details>

<details><summary><b>14.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3372.8331a92330.js</code> - <b>8</b> matches (R1 1 / R2 7) - first 47 - routes: 47</summary>

- R1: <code>location.assign(</code>
- R2: <code>e.collect.configManager.get("user")</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>i.configManager.get("user")</code> (x6)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>to.A.get("csrfToken")</code>

</details>

<details><summary><b>15.</b> <code>https://res.gcloudcache.com/volc-fe/volcengine-platform-runtime/main.7e241f35.js</code> - <b>8</b> matches (R1 6 / R2 2) - first 110 - routes: 110</summary>

- R1: <code>location.href="</code> (x2)
- R1: <code>location.href=d</code>
- R1: <code>location.href=e</code>
- R1: <code>location.href=o</code>
- R1: <code>new URLSearchParams(location.search</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>o.Z.get("__spti")</code>
- R2: <code>ry.Z.get("csrfToken")</code>

</details>

<details><summary><b>16.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7725.02a4a0b9b3.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 108 - routes: 108, 112-115</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>17.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/820.0c05aa3327.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 152 - routes: 152-153</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>18.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/93822.e7496ce86c.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 29 - routes: 29, 31-32, 35-36, 38, 43</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>19.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/38767.27735c56c3.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 57 - routes: 57-58, 60-62, 64-69, 72-77</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>20.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/1453.3d4e7d8023.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 46 - routes: 46-52</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("user")</code> (x7)
- R2: <code>r.configManager.get("reportErrorCallback")</code>

</details>

<details><summary><b>21.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/306.75d9663c88.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 11 - routes: 11</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>22.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/533.e462f14b74.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 13 - routes: 13, 22</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>23.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/7219.070e90099a.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 12 - routes: 12, 56, 131, 140, 142-143, 146-148</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>24.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/754.1cd85738bf.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 5 - routes: 5-7, 100</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("user")</code> (x7)
- R2: <code>r.configManager.get("reportErrorCallback")</code>

</details>

<details><summary><b>25.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - <b>6</b> matches (R1 4 / R2 2) - first 119 - routes: 119</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=p</code>
- R1: <code>new URLSearchParams(location.search</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>i.Z.get("__spti")</code>
- R2: <code>rb.Z.get("csrfToken")</code>

</details>

<details><summary><b>26.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/8888.48e3abbd17.js</code> - <b>6</b> matches (R1 0 / R2 6) - first 112 - routes: 112, 114-115</summary>

- R2: <code>a.get("x-request-id")</code> (x2)
- R2: <code>h.get("x-request-id")</code>
- R2: <code>l.A.get("csrfToken")</code>
- R2: <code>l.get("x-request-id")</code>
- R2: <code>r.get("x-tt-logid")</code>
- R2: <code>v.get("x-request-id")</code>

</details>

<details><summary><b>27.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/9832.9d43b6b9d6.js</code> - <b>5</b> matches (R1 4 / R2 1) - first 114 - routes: 114</summary>

- R1: <code>.query.length</code> (x2)
- R1: <code>location.href=t</code>
- R1: <code>location=e</code>
- R1: <code>location=i</code>
- R2: <code>e.get("month")</code>

</details>

<details><summary><b>28.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/53270.8af00a0fdb.js</code> - <b>5</b> matches (R1 1 / R2 4) - first 31 - routes: 31, 36, 38</summary>

- R1: <code>location = 0</code>
- R2: <code>n.get("WEBGL_multi_draw")</code>
- R2: <code>t.get("EXT_color_buffer_float")</code>
- R2: <code>t.get("WEBGL_multi_draw")</code> (x2)
- R2: <code>t.get("WEBGL_multisampled_render_to_texture")</code>

</details>

<details><summary><b>29.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/9545.4410f217ea.js</code> - <b>5</b> matches (R1 3 / R2 2) - first 56 - routes: 56</summary>

- R1: <code>location.href=r</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>e.get("hour")</code>
- R2: <code>e.get("minute")</code>

</details>

<details><summary><b>30.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_project_management.b3b7526866.js</code> - <b>5</b> matches (R1 5 / R2 0) - first 147 - routes: 147</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=a</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(location.search</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>31.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/169.e836de6f.js</code> - <b>5</b> matches (R1 5 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=`</code> (x6)
- R1: <code>new URLSearchParams(window.location.search</code>
- R1: <code>window.location.assign(</code> (x3)
- R1: <code>window.location.replace(</code>

</details>

<details><summary><b>32.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/2616.68953e3608.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 94 - routes: 94</summary>

- R1: <code>location.href=n</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>r.A.get("csrfToken")</code>

</details>

<details><summary><b>33.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/5074.8fd8bee520.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 84 - routes: 84</summary>

- R1: <code>location.href=u</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>34.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8934.16f82886be.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 81 - routes: 81-82</summary>

- R1: <code>location.href=u</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>o.A.get("csrfToken")</code>

</details>

<details><summary><b>35.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_create.292a62ba40.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 91 - routes: 91</summary>

- R1: <code>location.href=a</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>36.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_tls.06fcecf40a.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 86 - routes: 86</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>37.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/5314.f58e1230d9.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 48 - routes: 48</summary>

- R1: <code>.query.length</code> (x2)
- R1: <code>location.href=t</code>
- R1: <code>location=e</code>
- R1: <code>location=r</code>

</details>

<details><summary><b>38.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/242.d3a7dde1b7.js</code> - <b>4</b> matches (R1 2 / R2 2) - first 13 - routes: 13, 22</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)
- R1: <code>window.location.assign(</code>
- R2: <code>i.searchParams.get("utm_source")</code>
- R2: <code>t.get("subject")</code>

</details>

<details><summary><b>39.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-promotion-collection/static/js/async/903.4e84f168f1.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 13 - routes: 13, 22</summary>

- R1: <code>location.href=i</code>
- R1: <code>new URL(location.pathname</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>window.location.assign(</code>

</details>

<details><summary><b>40.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/(region)/overview/page.6445b3e125.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 1 - routes: 1, 79</summary>

- R1: <code>location.href=_</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R1: <code>window.location.assign(</code> (x2)

</details>

<details><summary><b>41.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_detail.e155531a98.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 115 - routes: 115</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>
- R2: <code>w.get("botType")</code>

</details>

<details><summary><b>42.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/953.9665a6db4c.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 152 - routes: 152-153</summary>

- R1: <code>location.href=M</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>43.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/16458.c88ef04029.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 44 - routes: 44</summary>

- R1: <code>.query.charCodeAt</code> (x2)
- R1: <code>.query.length</code> (x2)
- R1: <code>.query.spec</code> (x4)

</details>

<details><summary><b>44.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/31111.2e0d2bbcd5.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 29 - routes: 29, 32, 36, 38, 43</summary>

- R2: <code>r.searchParams.get("response-content-type")</code>
- R2: <code>r.searchParams.get("x-oss-response-content-type")</code>
- R2: <code>r.searchParams.get("x-tos-response-content-type")</code>

</details>

<details><summary><b>45.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/40154.7f6ab1bf03.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 31 - routes: 31</summary>

- R2: <code>a.searchParams.get("response-content-type")</code>
- R2: <code>a.searchParams.get("x-oss-response-content-type")</code>
- R2: <code>a.searchParams.get("x-tos-response-content-type")</code>

</details>

<details><summary><b>46.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/72792.695c5b8fa4.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 29 - routes: 29, 31-32, 36, 38, 43</summary>

- R1: <code>new URL(window.location.href</code>
- R2: <code>a.get("compareModelIds")</code>
- R2: <code>a.get("modelId")</code>

</details>

<details><summary><b>47.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/78199.dcbaa94f8d.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 36 - routes: 36, 38</summary>

- R1: <code>new URL(window.location.href</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code> (x2)
- R2: <code>r.searchParams.get("env")</code>

</details>

<details><summary><b>48.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_routes.4db18ec2aa.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 29 - routes: 29, 31-32, 35-36, 38, 43-44</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>49.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/61962.9ddbcf9862.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 58 - routes: 58, 66</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>p.A.get("csrfToken")</code> (x3)
- R2: <code>x.A.get("csrfToken")</code>

</details>

<details><summary><b>50.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/98068.626da96785.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 57 - routes: 57-58, 60-62, 64-69, 72-77</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>51.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_quickstart.0f2b0aa648.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 58 - routes: 58</summary>

- R1: <code>location.replace(</code>
- R1: <code>new URL(window.location.href</code> (x2)
- R1: <code>new URLSearchParams(window.location.search</code> (x4)

</details>

<details><summary><b>52.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_detail.86a4d90ebf.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 95 - routes: 95</summary>

- R1: <code>location.href=n</code>
- R1: <code>new URL(window.location.href</code>
- R2: <code>o.A.get("csrfToken")</code>

</details>

<details><summary><b>53.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_dataset_dump_create.4de9662963.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 97 - routes: 97</summary>

- R1: <code>location.href=a</code>
- R1: <code>new URL(window.location.href</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>54.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_eval_detail.96ea3ee7bf.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 92 - routes: 92</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>55.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_comparison.61405f08cd.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 85 - routes: 85</summary>

- R1: <code>location.href=a</code>
- R1: <code>new URL(window.location.href</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>56.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_repository_detail.c228a8a794.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 89 - routes: 89</summary>

- R1: <code>location.href=u</code>
- R1: <code>new URL(window.location.href</code>
- R2: <code>n.A.get("csrfToken")</code>

</details>

<details><summary><b>57.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/675.0aef9bd056.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 46 - routes: 46-52</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>58.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_list.922f1ad7a0.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 46 - routes: 46</summary>

- R2: <code>p.get("pageNumber")</code>
- R2: <code>p.get("pageSize")</code>
- R2: <code>r.get("*")</code>

</details>

<details><summary><b>59.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-landing/static/js/async/__federation_expose_routes.8289d3ab2d.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 11 - routes: 11</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.replace(</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>60.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/898.4d2dc21a91.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 148 - routes: 148</summary>

- R2: <code>i.searchParams.get("response-content-type")</code>
- R2: <code>i.searchParams.get("x-oss-response-content-type")</code>
- R2: <code>i.searchParams.get("x-tos-response-content-type")</code>

</details>

<details><summary><b>61.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_reward_plan.30a4a5d92e.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 140 - routes: 140</summary>

- R1: <code>location.href=Q</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>62.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_pickup_voucher.0dda270751.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 12 - routes: 12</summary>

- R1: <code>location.href="</code> (x2)
- R2: <code>r.A.get("csrfToken")</code>
- R2: <code>x.get("pickup_voucher_id")</code>

</details>

<details><summary><b>63.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_token_calculator.5aa401a3b2.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 148 - routes: 148</summary>

- R1: <code>location.href=a</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>64.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_vpc.280c5715d1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 146 - routes: 146</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>65.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/101.a21dd8db11.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 6 - routes: 6</summary>

- R1: <code>location.href=n</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>66.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/397.b813aecffa.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 5 - routes: 5-7, 100</summary>

- R1: <code>location.href=a</code>
- R1: <code>new URL(window.location.href</code> (x2)
- R1: <code>window.location.assign(</code> (x2)

</details>

<details><summary><b>67.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.221/lib-router.38527ea2.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 119 - routes: 119</summary>

- R1: <code>location.assign(</code> (x2)
- R1: <code>location.replace(</code>

</details>

<details><summary><b>68.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6652.6caf14fb81.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>location.href=(</code>
- R1: <code>window.location.assign(</code>

</details>

<details><summary><b>69.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/1172.bd821cdddf.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 112 - routes: 112, 114-115</summary>

- R1: <code>location=!</code>
- R1: <code>location=e</code> (x6)

</details>

<details><summary><b>70.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/2273.772c1f780a.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 112 - routes: 112</summary>

- R1: <code>location.href=e</code>
- R1: <code>location={</code>

</details>

<details><summary><b>71.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/5125.4f7bc454e2.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 114 - routes: 114</summary>

- R2: <code>a8.A.get("csrfToken")</code>
- R2: <code>v.get("botType")</code>

</details>

<details><summary><b>72.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6042.a194df1285.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 113 - routes: 113</summary>

- R1: <code>window.location.assign(</code>
- R2: <code>C.A.get("csrfToken")</code>

</details>

<details><summary><b>73.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/7587.08a9ca23cf.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 108 - routes: 108, 112-115</summary>

- R1: <code>location.assign(</code> (x2)
- R1: <code>location.replace(</code>

</details>

<details><summary><b>74.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_center.b3abac992b.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 108 - routes: 108</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>75.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_application_detail.07b6dbbd6c.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 112 - routes: 112</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>76.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_assistant_edit.5ec129a509.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 114 - routes: 114</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>77.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/__federation_expose_my_apps.36fd1cc29b.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 113 - routes: 113</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>78.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/17535.17b02bf1ba.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 36 - routes: 36</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>tO.A.get("csrfToken")</code>

</details>

<details><summary><b>79.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/39548.444d033809.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 38 - routes: 38</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)
- R2: <code>o.A.get("csrfToken")</code>

</details>

<details><summary><b>80.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/__federation_expose_sidebar_extra.5e990f43bf.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 29 - routes: 29, 31-32, 35-36, 38, 43</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>81.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/10861.fcac40b4fb.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 60 - routes: 60-62, 65, 73</summary>

- R1: <code>location=!</code>
- R1: <code>location=e</code> (x6)

</details>

<details><summary><b>82.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/22673.83f22e0b73.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 58 - routes: 58, 66</summary>

- R1: <code>location.href=e</code>
- R1: <code>location=!</code>

</details>

<details><summary><b>83.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/28560.9e1f9feed8.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 67 - routes: 67-68</summary>

- R1: <code>location.assign(</code>
- R2: <code>eZ.A.get("csrfToken")</code>

</details>

<details><summary><b>84.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4910.9997e22df0.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 57 - routes: 57-58, 60-62, 65-66, 72-73</summary>

- R1: <code>location.assign(</code>
- R2: <code>eQ.A.get("csrfToken")</code>

</details>

<details><summary><b>85.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2732.0aef4bf74d.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 48 - routes: 48, 52</summary>

- R2: <code>n.get("*")</code>
- R2: <code>r.get("*")</code>

</details>

<details><summary><b>86.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/3197.eda19b0eaa.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 47 - routes: 47-52</summary>

- R1: <code>location.assign(</code>
- R2: <code>eX.A.get("csrfToken")</code>

</details>

<details><summary><b>87.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/6322.84539c2616.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 48 - routes: 48, 52</summary>

- R1: <code>location=!</code>
- R1: <code>location=e</code> (x6)

</details>

<details><summary><b>88.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7924.4e5ca1b471.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 47 - routes: 47-48, 52</summary>

- R2: <code>A.A.get("csrfToken")</code> (x3)
- R2: <code>L.A.get("csrfToken")</code>

</details>

<details><summary><b>89.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_batchInference_manage.e7d9547562.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 49 - routes: 49</summary>

- R2: <code>i.A.get("csrfToken")</code>
- R2: <code>r.get("*")</code>

</details>

<details><summary><b>90.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_create.addf5ad349.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 47 - routes: 47</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x3)
- R2: <code>i.A.get("csrfToken")</code>

</details>

<details><summary><b>91.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2279.f71a69c7ae.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 147 - routes: 147</summary>

- R1: <code>location.assign(</code>
- R2: <code>y.A.get("csrfToken")</code>

</details>

<details><summary><b>92.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/2716.4c01e47af9.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 12 - routes: 12</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>93.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_api_key_manage.b870f1b214.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 142 - routes: 142</summary>

- R1: <code>location.href=n</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>94.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_coding_plan_pane.13c650e89c.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 131 - routes: 131</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>95.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_usage_tracking_manage.d972bdb5cb.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 143 - routes: 143</summary>

- R1: <code>location.href=o</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>96.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_comparison.fdf7c0861b.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 7 - routes: 7</summary>

- R1: <code>location.href=n</code>
- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>97.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-square/static/js/async/__federation_expose_home.ab767fe68a.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 5 - routes: 5, 100</summary>

- R1: <code>.query.trim</code> (x4)
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>98.</b> <code>https://livechat.im.byteplusbiz.com/sockjs.min.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>location=r</code>

</details>

<details><summary><b>99.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-knowledge/static/js/1.0.0.221/lib-arco.fa0a8e2c.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 119 - routes: 119</summary>

- R2: <code>t.get("month")</code>

</details>

<details><summary><b>100.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/app-lab/vmok-remote-entry.46031a1d.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 108 - routes: 108, 112-115</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>101.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/1312.8f28b4bdbd.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 1 - routes: 1, 79</summary>

- R2: <code>r.get("*")</code>

</details>

<details><summary><b>102.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/4708.188ebd1e2e.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1, 5-7, 10-13, 22, 29, 31-32, 35-36, 38, 43-44, 46-52, 56-58, 60-62, 64-69, 71-77, 79, 81-82, 84-86, 89, 91-92, 94-95, 97, 100, 104, 108, 112-115, 131, 140, 142-143, 146-150, 152-153</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>103.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/ark-new-main/static/js/async/6390.72c02fadf9.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 149 - routes: 149-150</summary>

- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>104.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/exp-center/vmok-remote-entry.e54a3014.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 11 - routes: 11, 22, 29, 31-32, 35-36, 38, 43-44, 48-49, 62, 67, 76-77, 79, 81, 92, 94, 100, 104, 108, 146, 148-149, 152</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>105.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/model-promotion-collection/vmok-remote-entry.acf00cc8.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 13 - routes: 13, 22</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>106.</b> <code>https://res.gcloudcache.com/bp-fe/console-ark/model-settings/vmok-remote-entry.5250de02.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 10 - routes: 10, 12, 56, 131, 140, 142-143, 146-148</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>107.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/257.6a9abae379.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 112 - routes: 112</summary>

- R2: <code>s8.A.get("csrfToken")</code> (x7)

</details>

<details><summary><b>108.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/app-lab/static/js/async/6709.1fb936582f.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 108 - routes: 108, 112-115</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>109.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/arkcli/static/js/async/__federation_expose_login.a297946d57.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 153 - routes: 153</summary>

- R1: <code>window.location.replace(</code>

</details>

<details><summary><b>110.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/10260.3b056e3429.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 31 - routes: 31, 36, 38, 43</summary>

- R1: <code>location.href=e</code>

</details>

<details><summary><b>111.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/3625.d4b9487dc9.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 31 - routes: 31</summary>

- R2: <code>e.get("month")</code>

</details>

<details><summary><b>112.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/37624.e789471e61.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 36 - routes: 36, 38</summary>

- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>113.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/42494.c2231c54e7.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 29 - routes: 29, 32, 36, 38</summary>

- R2: <code>o.A.get("csrfToken")</code>

</details>

<details><summary><b>114.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/51111.ffecb0decc.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 38 - routes: 38</summary>

- R2: <code>i.get("month")</code>

</details>

<details><summary><b>115.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/5938.68450f6064.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 36 - routes: 36</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>116.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/66561.c3d2ef521d.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 36 - routes: 36, 38</summary>

- R1: <code>location={</code>

</details>

<details><summary><b>117.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/75664.0aad4702c6.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 31 - routes: 31, 36</summary>

- R2: <code>e.extensions.get("WEBGL_compressed_texture_astc")</code>

</details>

<details><summary><b>118.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/exp-center/static/js/async/sender-chat.1114959f00.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 32 - routes: 32</summary>

- R1: <code>location={</code>

</details>

<details><summary><b>119.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/4476.785c7dd255.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 57 - routes: 57, 60, 62, 65</summary>

- R2: <code>p.A.get("csrfToken")</code> (x3)

</details>

<details><summary><b>120.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/45883.4655d9465a.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 65 - routes: 65, 67-68</summary>

- R1: <code>location.assign(</code>

</details>

<details><summary><b>121.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_agents_detail.3a4d689d4e.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 61 - routes: 61</summary>

- R2: <code>p.A.get("csrfToken")</code> (x3)

</details>

<details><summary><b>122.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_channel_create.8602b94971.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 76 - routes: 76</summary>

- R2: <code>K.get("step")</code>

</details>

<details><summary><b>123.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_credentials_vault.6d0e89ea57.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 69 - routes: 69</summary>

- R1: <code>location.replace(</code>

</details>

<details><summary><b>124.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_memory.33e6c1b4f9.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 74 - routes: 74</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>125.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_detail.9b8f8d7227.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 73 - routes: 73</summary>

- R2: <code>h.A.get("csrfToken")</code> (x3)

</details>

<details><summary><b>126.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/managed-agent/static/js/async/__federation_expose_skills_manage.1a405fdca7.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 72 - routes: 72</summary>

- R2: <code>p.A.get("csrfToken")</code> (x3)

</details>

<details><summary><b>127.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/8661.575e841d27.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 84 - routes: 84</summary>

- R2: <code>c.get("month")</code>

</details>

<details><summary><b>128.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-customization/static/js/async/__federation_expose_job_detail.6ab57a014c.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 84 - routes: 84</summary>

- R1: <code>.query.metricsExcludedMetricNames</code>

</details>

<details><summary><b>129.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2050.519f56b0a8.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 49 - routes: 49, 51</summary>

- R2: <code>e.get("month")</code>

</details>

<details><summary><b>130.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/2314.a9e4208f13.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 47 - routes: 47</summary>

- R2: <code>e.get("month")</code>

</details>

<details><summary><b>131.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/4337.b260caab3e.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 46 - routes: 46, 48-52</summary>

- R1: <code>location.assign(</code>

</details>

<details><summary><b>132.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/7210.dbe0130553.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 46 - routes: 46, 48, 52</summary>

- R2: <code>a.A.get("csrfToken")</code>

</details>

<details><summary><b>133.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/8728.361f718585.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 46 - routes: 46-47, 50</summary>

- R1: <code>location.assign(</code>

</details>

<details><summary><b>134.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/9857.cacc2df099.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 48 - routes: 48, 52</summary>

- R2: <code>e.get("month")</code>

</details>

<details><summary><b>135.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-inference/static/js/async/__federation_expose_endpoint_detail.da9d422fb4.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 48 - routes: 48</summary>

- R2: <code>tu.A.get("csrfToken")</code>

</details>

<details><summary><b>136.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/4427.83192611c0.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 12 - routes: 12, 147</summary>

- R1: <code>location.assign(</code>

</details>

<details><summary><b>137.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8010.b4b0f9e430.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 131 - routes: 131</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>138.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/8156.7bf97dfbc9.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 142 - routes: 142</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>139.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/977.a82025cf81.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 12 - routes: 12, 131</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>140.</b> <code>https://res.gcloudcache.com/volc-fe/console-ark/model-settings/static/js/async/__federation_expose_open_management_manage.39c398fd0f.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 56 - routes: 56</summary>

- R2: <code>o.A.get("csrfToken")</code>

</details>

<details><summary><b>141.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/1601.d022af98.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>location.href=n</code>

</details>

<details><summary><b>142.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/4050.4efb972f.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>location.href="</code> (x3)

</details>

<details><summary><b>143.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/4112.c00bb291.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>location.href="</code> (x2)

</details>

<details><summary><b>144.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/4215.968f9162.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>window.location.replace(</code> (x3)

</details>

<details><summary><b>145.</b> <code>https://res.gcloudcache.com/volc-fe/vconsole-auth/volcengine/static/js/1.0.0.3111/async/8246.ec54937f.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>location.replace(</code> (x7)

</details>

## Duplicate Routes

78 routes skipped as duplicate results. Full mapping is in `data/scan.log`.

<details><summary>Duplicate mapping</summary>

- Route 1: 2-4, 8-9, 53-55, 80, 87, 109, 111, 117, 121, 123, 128-129, 138, 141, 144
- Route 5: 99
- Route 13: 14-21, 23, 25-27
- Route 22: 24, 28
- Route 29: 30, 33-34, 41
- Route 35: 37, 39-40, 42, 45
- Route 56: 139
- Route 57: 59
- Route 60: 63
- Route 69: 70
- Route 71: 101-103, 105, 107, 125, 130, 132-133
- Route 76: 78
- Route 79: 90, 93, 116, 118, 122, 124, 126, 145
- Route 81: 88
- Route 82: 83
- Route 94: 96
- Route 97: 98
- Route 104: 106, 127, 134-137
- Route 119: 120
- Route 150: 151

</details>

## Errors

None.

<details><summary>Regex patterns and exclusions</summary>

Regex 1:

```regex
(new\s+(URLSearchParams|URL)\s*\(\s*((window\.)?location\.(search|href|hash|pathname)|document\.(URL|URLUnencoded|baseURI))|(\.query\s*\.\s*[A-Za-z_$][\w$]*|\bquery\s*\[\s*['"][^'"]+['"]\s*\])|((window\.)?location\.(assign|replace)\s*\(|\b(location|location\.href)\s*=\s*[^=]))
```

Regex 2:

```regex
(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])([^'"`]+)\1\s*\)
```

Excluded: `header(s).get`, `cache/storage/registry.get`, and parameter names `align, bottom, class, className, color, data, direction, display, height, id, index, left, length, margin, name, offset, padding, position, right, series, size, style, top, trigger, type, width, x, y`.

</details>
