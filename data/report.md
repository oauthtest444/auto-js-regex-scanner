# JavaScript Route Regex Scan Report

- Generated: 2026-11-03 19:11:22 UTC
- URL list: <code>data/urls.txt</code>
- Authentication: <code>data/user-A.txt</code> (2 headers, 45 cookies)
- Wait after navigation: 10s
- Navigation timeout: 20s
- Unique matches are counted per JavaScript file; the same match text in two files counts once per file.

## Summary

| Metric | Value |
| --- | ---: |
| Routes tested | 209 |
| Routes skipped as duplicate results | 140 |
| Routes with errors | 0 |
| Unique JavaScript files with matches | 107 |
| Unique regex matches (per file) | 900 |
| Unique match texts across files | 629 |
| Unique regex 1 matches (per file) | 178 |
| Unique regex 2 matches (per file) | 722 |
| JavaScript files that could not be scanned | 0 |
| File recoveries via network capture | 0 |
| File recoveries via Python HTTP fetch | 0 |

## Regex Patterns

Regex 1:

```regex
(new\s+(URLSearchParams|URL)\s*\(\s*((window\.)?location\.(search|href|hash|pathname)|document\.(URL|URLUnencoded|baseURI))|(\.query\s*\.\s*[A-Za-z_$][\w$]*|\bquery\s*\[\s*['"][^'"]+['"]\s*\])|((window\.)?location\.(assign|replace)\s*\(|\b(location|location\.href)\s*=\s*[^=]))
```

Regex 2:

```regex
(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])([^'"`]+)\1\s*\)
```

Default match exclusions:

- <code>\bheaders?\s*\.\s*get\s*\(</code>
- <code>\b(?:cache&#124;storage&#124;registry)\s*\.\s*get\s*\(</code>

Regex 2 excluded parameter names:

`align`, `bottom`, `class`, `className`, `color`, `data`, `direction`, `display`, `height`, `id`, `index`, `left`, `length`, `margin`, `name`, `offset`, `padding`, `position`, `right`, `series`, `size`, `style`, `top`, `trigger`, `type`, `width`, `x`, `y`

## Routes With Unique Scan Results

| # | Route | HTTP | Matched JS files | Unique file matches | New JS files | New matches | Notes |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code> | 200 | 14 | 60 | 14 | 60 | - |
| 2 | <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code> | 200 | 9 | 35 | 2 | 4 | - |
| 3 | <code>https://console.byteplus.com/datatester/ai-research</code> | 200 | 8 | 32 | 1 | 1 | final URL: https://console.byteplus.com/datatester/ai-research/home |
| 4 | <code>https://console.byteplus.com/datatester/redirect</code> | 200 | 18 | 66 | 4 | 6 | final URL: https://console.byteplus.com/datatester/app/566590/experiment/list |
| 11 | <code>https://console.byteplus.com/datatester/volc-sale</code> | 200 | 13 | 57 | 1 | 1 | - |
| 12 | <code>https://console.byteplus.com/datatester/permission-portal</code> | 200 | 14 | 60 | 0 | 0 | - |
| 13 | <code>https://console.byteplus.com/datatester/org/create</code> | 200 | 14 | 62 | 2 | 6 | - |
| 23 | <code>https://console.byteplus.com/datatester/app/566590/dashboard</code> | 200 | 17 | 78 | 3 | 18 | - |
| 26 | <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code> | 200 | 16 | 64 | 2 | 4 | - |
| 27 | <code>https://console.byteplus.com/datatester/app/566590/draft/:draftId/bav-event/detail</code> | 200 | 0 | 0 | 0 | 0 | final URL: about:blank |
| 32 | <code>https://console.byteplus.com/datatester/app/566590/event-group</code> | 200 | 15 | 63 | 1 | 3 | - |
| 36 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code> | 200 | 15 | 65 | 1 | 5 | - |
| 37 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code> | 200 | 16 | 68 | 2 | 8 | - |
| 39 | <code>https://console.byteplus.com/datatester/app/566590/volcSale/index</code> | 200 | 15 | 61 | 0 | 0 | final URL: https://console.byteplus.com/datatester/volc-sale |
| 40 | <code>https://console.byteplus.com/datatester/app/566590/volcSale/caliber</code> | 200 | 15 | 61 | 1 | 1 | - |
| 41 | <code>https://console.byteplus.com/datatester/app/566590/form-editor</code> | 200 | 34 | 278 | 15 | 209 | - |
| 42 | <code>https://console.byteplus.com/datatester/app/566590/behavior-detail</code> | 200 | 15 | 63 | 1 | 3 | - |
| 43 | <code>https://console.byteplus.com/datatester/app/566590/open-api</code> | 200 | 15 | 118 | 1 | 58 | - |
| 47 | <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code> | 200 | 15 | 64 | 1 | 4 | final URL: https://console.byteplus.com/datatester/app/566590/personalization/coding/list?tab=all |
| 48 | <code>https://console.byteplus.com/datatester/app/566590/personalization/:campaignId/:campaignTab</code> | 200 | 15 | 62 | 0 | 0 | final URL: https://console.byteplus.com/datatester/app/566590/personalization/:campaignId/exp_builder |
| 50 | <code>https://console.byteplus.com/datatester/app/566590/tour</code> | 200 | 15 | 63 | 1 | 3 | - |
| 51 | <code>https://console.byteplus.com/datatester/app/566590/guide</code> | 200 | 30 | 121 | 1 | 3 | - |
| 52 | <code>https://console.byteplus.com/datatester/app/566590/demo-h5</code> | 200 | 15 | 62 | 1 | 2 | - |
| 65 | <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code> | 200 | 20 | 72 | 4 | 9 | - |
| 66 | <code>https://console.byteplus.com/datatester/app/566590/experiment/create/:mode?/:experimentId?</code> | 200 | 17 | 64 | 0 | 0 | - |
| 67 | <code>https://console.byteplus.com/datatester/app/566590/experiment/detail/:mode/:experimentId</code> | 200 | 21 | 73 | 0 | 0 | - |
| 69 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/review/:reviewId/detail</code> | 200 | 30 | 119 | 1 | 1 | - |
| 70 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code> | 200 | 31 | 264 | 2 | 146 | - |
| 71 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/ad-report</code> | 200 | 30 | 119 | 1 | 1 | - |
| 72 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report</code> | 200 | 21 | 73 | 1 | 1 | - |
| 81 | <code>https://console.byteplus.com/datatester/app/566590/flight/experience-config</code> | 200 | 15 | 61 | 1 | 1 | - |
| 82 | <code>https://console.byteplus.com/datatester/app/566590/flight/layer/list</code> | 200 | 15 | 62 | 1 | 2 | - |
| 94 | <code>https://console.byteplus.com/datatester/app/566590/metric/board</code> | 200 | 15 | 66 | 1 | 6 | - |
| 100 | <code>https://console.byteplus.com/datatester/app/566590/feature/list/:tag?</code> | 200 | 15 | 63 | 1 | 3 | - |
| 101 | <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code> | 200 | 18 | 70 | 3 | 8 | - |
| 103 | <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/version/:featureAppId?</code> | 200 | 17 | 67 | 0 | 0 | - |
| 109 | <code>https://console.byteplus.com/datatester/app/566590/system/system-setting</code> | 200 | 15 | 61 | 1 | 1 | - |
| 110 | <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code> | 200 | 15 | 64 | 1 | 4 | - |
| 112 | <code>https://console.byteplus.com/datatester/app/566590/system/permission/list</code> | 200 | 16 | 64 | 0 | 0 | - |
| 118 | <code>https://console.byteplus.com/datatester/app/566590/system/origin-events</code> | 200 | 15 | 63 | 1 | 3 | - |
| 119 | <code>https://console.byteplus.com/datatester/app/566590/system/simulator-manage</code> | 200 | 15 | 63 | 1 | 3 | - |
| 120 | <code>https://console.byteplus.com/datatester/app/566590/system/event-params</code> | 200 | 15 | 63 | 1 | 3 | - |
| 121 | <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code> | 200 | 17 | 85 | 3 | 25 | - |
| 122 | <code>https://console.byteplus.com/datatester/app/566590/system/virtual-params</code> | 200 | 15 | 63 | 1 | 3 | - |
| 123 | <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/create/web</code> | 200 | 15 | 63 | 1 | 3 | - |
| 124 | <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code> | 200 | 16 | 293 | 2 | 233 | - |
| 125 | <code>https://console.byteplus.com/datatester/app/566590/system/bav-events</code> | 200 | 15 | 63 | 1 | 3 | - |
| 128 | <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/list</code> | 200 | 16 | 64 | 1 | 2 | - |
| 134 | <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-user-list</code> | 200 | 15 | 61 | 1 | 1 | - |
| 135 | <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-manage-list</code> | 200 | 15 | 61 | 1 | 1 | - |
| 136 | <code>https://console.byteplus.com/datatester/app/566590/system/scheduled-task-management</code> | 200 | 15 | 62 | 1 | 2 | - |
| 137 | <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code> | 200 | 16 | 65 | 2 | 5 | - |
| 138 | <code>https://console.byteplus.com/datatester/app/566590/system/templates/basic</code> | 200 | 30 | 119 | 1 | 1 | - |
| 139 | <code>https://console.byteplus.com/datatester/app/566590/system/templates/editor</code> | 200 | 28 | 116 | 1 | 2 | - |
| 140 | <code>https://console.byteplus.com/datatester/app/566590/system/templates/list</code> | 200 | 30 | 119 | 1 | 1 | - |
| 141 | <code>https://console.byteplus.com/datatester/app/566590/user-cohort/list</code> | 200 | 15 | 61 | 1 | 1 | - |
| 146 | <code>https://console.byteplus.com/datatester/app/566590/metric-group/list</code> | 200 | 15 | 62 | 1 | 2 | - |
| 148 | <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code> | 200 | 18 | 66 | 3 | 4 | - |
| 151 | <code>https://console.byteplus.com/datatester/app/566590/metric-group/detail/:id?</code> | 200 | 16 | 63 | 0 | 0 | - |
| 152 | <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code> | 200 | 15 | 67 | 1 | 7 | - |
| 175 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/user-hit</code> | 200 | 17 | 65 | 1 | 1 | - |
| 176 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/diagnosis</code> | 200 | 17 | 65 | 1 | 1 | - |
| 178 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/calculator</code> | 200 | 17 | 65 | 1 | 1 | - |
| 179 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/vm-simulation</code> | 200 | 18 | 69 | 1 | 1 | - |
| 182 | <code>https://console.byteplus.com/datatester/app/566590/open/integration/create</code> | 200 | 15 | 64 | 0 | 0 | - |
| 196 | <code>https://console.byteplus.com/datatester/app/566590/open/template/:id/:mode</code> | 200 | 31 | 121 | 1 | 1 | - |
| 203 | <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code> | 200 | 16 | 70 | 1 | 4 | - |
| 206 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/list</code> | 200 | 17 | 65 | 1 | 1 | - |
| 207 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/create</code> | 200 | 21 | 80 | 1 | 3 | - |

## New Discoveries by Route

### Route 1: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

New matched JavaScript files:

- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-sg/log-sdk/collect/5/plugin/visual.js</code>
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code>
- <code>https://lf16-unpkg-i18n.byted-static.com/obj/unpkg-va/xgplayer/2.9.6/browser/index.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/1.0.0.1528/preload.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/19362.6387ad3d.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6123.0837ab6d.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/7454.8b7b620f.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/arco_designs.7f78af21.async.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code>

New regex matches:

- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-sg/log-sdk/collect/5/plugin/visual.js</code> - [Regex 1] <code>new URL(window.location.href</code> (x1)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 1] <code>new URL(location.href</code> (x2)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 2] <code>e.configManager.get("user_unique_id")</code> (x3)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 2] <code>e.configManager.get("user_unique_id_type")</code> (x1)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 2] <code>e.configManager.get("web_id")</code> (x3)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 2] <code>n.configManager.get("reportErrorCallback")</code> (x1)
- <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - [Regex 2] <code>r.configManager.get("user")</code> (x7)
- <code>https://lf16-unpkg-i18n.byted-static.com/obj/unpkg-va/xgplayer/2.9.6/browser/index.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/1.0.0.1528/preload.js</code> - [Regex 1] <code>location.href=e</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/1.0.0.1528/preload.js</code> - [Regex 1] <code>location.href=i</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/19362.6387ad3d.js</code> - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code> - [Regex 2] <code>l.get(`/datatester/common-service/api/v3/apps/custom-config/${e}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code> - [Regex 2] <code>l.get(`/datatester/experiment/api/v3/process/${e}/detail`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code> - [Regex 2] <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/${t}/brief`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code> - [Regex 2] <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code> - [Regex 2] <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/history/${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code> - [Regex 1] <code>location.assign(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code> - [Regex 1] <code>location.href=i</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code> - [Regex 1] <code>location=a</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code> - [Regex 2] <code>tf.A.get("csrfToken")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>location.href="</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>location.href=`</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>location.href=a</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>location.href=t</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 1] <code>location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 2] <code>eI.get(`v1/volc/orgs/${e}/operation_deadline`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 2] <code>eP.get(`/org/${e}/operation_deadline`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - [Regex 2] <code>p.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${a}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6123.0837ab6d.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6123.0837ab6d.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6123.0837ab6d.js</code> - [Regex 1] <code>location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/7454.8b7b620f.js</code> - [Regex 2] <code>o.get(`${p}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/7454.8b7b620f.js</code> - [Regex 2] <code>o.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/7454.8b7b620f.js</code> - [Regex 2] <code>o.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>location.href=i</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>location.href=n</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>location.href=t</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>location.replace(</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 1] <code>window.location.replace(</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - [Regex 2] <code>i.get("onEffect")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/arco_designs.7f78af21.async.js</code> - [Regex 2] <code>t.get("month")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - [Regex 2] <code>d.get(`/v2/app/${e}/recipient/list?${o.stringify(a)}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - [Regex 2] <code>n.A.get("x-rgw-dor")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - [Regex 2] <code>n.get(`/v2/userinfo?org_id=${e}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - [Regex 2] <code>p.get("/v2/org_list")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - [Regex 1] <code>location.href=p</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - [Regex 2] <code>i.Z.get("__spti")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - [Regex 2] <code>rb.Z.get("csrfToken")</code> (x1)

### Route 2: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48496.5b2a454b.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58519.f0df961e.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48496.5b2a454b.js</code> - [Regex 1] <code>location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48496.5b2a454b.js</code> - [Regex 1] <code>location=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58519.f0df961e.js</code> - [Regex 2] <code>eG.get(`${eL}v3/apps/${e}/metadata/properties`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58519.f0df961e.js</code> - [Regex 2] <code>eG.get(`${eL}v3/apps/${e}/portal/role/${t}/property-desensitization`)</code> (x1)

### Route 3: <code>https://console.byteplus.com/datatester/ai-research</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4806.0109974e.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4806.0109974e.js</code> - [Regex 2] <code>C.get("/datatester/compass/api/v3/survey/user_info")</code> (x1)

### Route 4: <code>https://console.byteplus.com/datatester/redirect</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13384.373605de.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/22146.69329a00.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61407.d6e23ed9.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75360.0ea54511.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13384.373605de.js</code> - [Regex 1] <code>location.href=`</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/22146.69329a00.js</code> - [Regex 2] <code>c.get(`/datatester/api/v2/apps/${t}/features/cohorts_open_status?feature_id=${a}&amp;version=${r}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/22146.69329a00.js</code> - [Regex 2] <code>c.get(`/datatester/api/v2/apps/${t}/flights/cohorts_open_status?flight_id=${a}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/22146.69329a00.js</code> - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61407.d6e23ed9.js</code> - [Regex 1] <code>window.location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75360.0ea54511.js</code> - [Regex 2] <code>l.get(`/datatester/experiment/api/v3/app/${e}/traffic_info/${t}`)</code> (x1)

### Route 11: <code>https://console.byteplus.com/datatester/volc-sale</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6625.8405fd46.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6625.8405fd46.js</code> - [Regex 1] <code>location.href=`</code> (x5)

### Route 12: <code>https://console.byteplus.com/datatester/permission-portal</code>

New matched JavaScript files: none

New regex matches: none

### Route 13: <code>https://console.byteplus.com/datatester/org/create</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14518.9565419e.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/66107.93c9a306.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14518.9565419e.js</code> - [Regex 2] <code>u.get(`${c}/v3/app/${t.app_id}/call-source/${t.id}/access-status`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14518.9565419e.js</code> - [Regex 2] <code>u.get(`/datarangers/api/org/${t}/tester-subjects?project_id=${e}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14518.9565419e.js</code> - [Regex 2] <code>u.get(`/datatester/org_management/api/org/${t}/tester-subjects?project_id=${e}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/66107.93c9a306.js</code> - [Regex 2] <code>o.get(`${u}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/66107.93c9a306.js</code> - [Regex 2] <code>o.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/66107.93c9a306.js</code> - [Regex 2] <code>o.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)

### Route 23: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6127.02689e58.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95783.90718b0f.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6127.02689e58.js</code> - [Regex 2] <code>u.get(`/datatester/api/v2/apps/${l}/features/cohorts_open_status?feature_id=${t}&amp;version=${n}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6127.02689e58.js</code> - [Regex 2] <code>u.get(`/datatester/api/v2/apps/${l}/flights/cohorts_open_status?flight_id=${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95783.90718b0f.js</code> - [Regex 1] <code>location=0</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 1] <code>location=!</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 1] <code>location=e</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>e.collect.configManager.get("custom")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>e.configManager.get("user_unique_id")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>e.configManager.get("user_unique_id_type")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>e.configManager.get("web_id")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>fS.get("_TEA_VE_APIHOST")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>fS.get("_VISUAL_EDITOR_U")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>fS.get("_VISUAL_EDITOR_V")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>fS.get("lang")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>i.configManager.get("user")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>n.configManager.get("reportErrorCallback")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - [Regex 2] <code>n.get("defaultKeyword")</code> (x1)

### Route 26: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>

New matched JavaScript files:

- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/log-sdk/collect/visual-ab-inspector.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61859.05b038a9.js</code>

New regex matches:

- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/log-sdk/collect/visual-ab-inspector.js</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/log-sdk/collect/visual-ab-inspector.js</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61859.05b038a9.js</code> - [Regex 1] <code>location.href=l</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61859.05b038a9.js</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x2)

### Route 27: <code>https://console.byteplus.com/datatester/app/566590/draft/:draftId/bav-event/detail</code>

New matched JavaScript files: none

New regex matches: none

### Route 32: <code>https://console.byteplus.com/datatester/app/566590/event-group</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/69835.b7f0e2d2.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/69835.b7f0e2d2.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/69835.b7f0e2d2.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/69835.b7f0e2d2.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 36: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code> - [Regex 2] <code>na.get(`/projects/${a}/apps/ios/lookup?download_url=${encodeURIComponent(e)}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code> - [Regex 2] <code>na.get(`/projects/${l}/apps/sync-res?request_id=${r}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code> - [Regex 2] <code>s6.get(`${s8(i)}/industries?account_id=${r}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code> - [Regex 2] <code>s6.get(`${s8(i)}/universal-materials/check?material_ids=${e}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code> - [Regex 2] <code>vu.get(`/projects/${l}/channels/${e}/experiment-creation-task/${a}`)</code> (x1)

### Route 37: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code> - [Regex 1] <code>location.href=p</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code> - [Regex 1] <code>location=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code> - [Regex 1] <code>location=p</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code> - [Regex 1] <code>.query.modelInfo</code> (x7)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code> - [Regex 1] <code>.query.word</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code> - [Regex 2] <code>e.get("text")</code> (x1)

### Route 39: <code>https://console.byteplus.com/datatester/app/566590/volcSale/index</code>

New matched JavaScript files: none

New regex matches: none

### Route 40: <code>https://console.byteplus.com/datatester/app/566590/volcSale/caliber</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99606.9cf38234.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99606.9cf38234.js</code> - [Regex 2] <code>M.get(`/v2/app/${n}/management/event_usage/`)</code> (x1)

### Route 41: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/11053.6fd86b1e.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28073.a2217d3f.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40184.07ffaccf.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/41974.52459966.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42360.4dfa46fb.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48001.326bc790.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/57671.49fbaaac.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/65247.3231c58e.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/73667.5682fe30.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95936.3477233c.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/11053.6fd86b1e.js</code> - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 1] <code>location=!</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>a.attributes.get("scriptlevel")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>e.get("bevelled")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>e.get("largeop")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>e.get("linethickness")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>e.get("mathsize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>i.get("lspace")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>i.get("rspace")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("data-semantic-speech")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("lspace")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("mathsize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("rspace")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("scriptlevel")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("scriptminsize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.get("scriptsizemultiplier")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>n.node.attributes.get("bevelled")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>o.get("frame")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>o.get("mjx-keep-attrs")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>r.get("depth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>r.gullet.macros.get("\\df@tag")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.attributes.get("columnalign")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.attributes.get("columnspacing")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.get("background-color")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.get("font-family")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.gullet.macros.get("\\df@tag")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.macros.get("\\df@tag")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - [Regex 2] <code>t.node.attributes.get("selection")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28073.a2217d3f.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28073.a2217d3f.js</code> - [Regex 2] <code>n.get(`${i}/template-group`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28073.a2217d3f.js</code> - [Regex 2] <code>s.get("parent_manage_type")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>B.get("lineWidth")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>C.get("_order")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>C.get("_rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>Y.get("_order")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>Y.get("_rank")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>a.get("__source")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>a.get("__target")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>a.get("collapsed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>a.get("groupTitle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>a.get("lineWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>a.get("rank")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>c.get("_editStyleCache")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>c.get("anchors")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>c.get("cluster")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>c.get("len")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>c.get("visible")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>d.get("linkNode")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>d.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>d.get("visible")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.canvas.get("pixelRatio")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("__cacheMagnetStyles")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("_anchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("_children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("_order")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("anchorIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("branchCount")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("children")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("collapsed")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("crossOrigin")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("cursor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("dummy")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("len")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("lineDash")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("linkGroupOnCollapse")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("order")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("originGroupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("originSize")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("originSource")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("originTarget")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("rank")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("reversed")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("source")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.get("target")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.graph.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>e.relatedTarget.get("children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>g.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>g.get("visible")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>h.get("container")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>h.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("_editStyleCache")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("anchorIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("children")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("collapsed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("parent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("rank")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("sourceAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("target")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.get("targetAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>i.layer.get("__loadingCircle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>l.get("linkNode")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>l.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>l.get("reversed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("collapsed")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("container")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("cursor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("dummy")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("fontSize")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("gapYs")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("originGroupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("originSize")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("outerNode")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("rank")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("source")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("target")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>n.get("titleHeight")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("_children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("anchors")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("attr")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("cluster")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("depth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>o.get("target")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("anchorIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("anchors")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("minlen")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("parent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("path")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("points")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("rank")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>r.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>s.get("container")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>s.get("parent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>s.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>s.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>s.get("target")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>s.node.get("anchors")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.canvas.get("pixelRatio")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_animateShow")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_background")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_keyShape")</code> (x10)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_label")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_order")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_paste")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("_selections")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("animateHandler")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("children")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("clickInteraction")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("collapsed")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("controlPoints")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("destroyed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("dummy")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("encodeValue")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("endArrow")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("fillStyle")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("fixed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("groupNodes")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("ignoreGrid")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("mask")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("minlen")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("order")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("pixelRatio")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("rank")</code> (x9)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("root")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("source")</code> (x7)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("startArrow")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("target")</code> (x8)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("targets")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("toDraw")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("triggerId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>t.get("weight")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("_editStyleCache")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("children")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("collapsed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("source")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("sourceAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("styles")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("target")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>u.get("targetAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - [Regex 2] <code>v.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40184.07ffaccf.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40184.07ffaccf.js</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/41974.52459966.js</code> - [Regex 1] <code>.query.data</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/41974.52459966.js</code> - [Regex 1] <code>.query.isFetched</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/41974.52459966.js</code> - [Regex 1] <code>.query.isLoading</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42360.4dfa46fb.js</code> - [Regex 1] <code>location.href=`</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42360.4dfa46fb.js</code> - [Regex 2] <code>o.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${t}/metrics`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48001.326bc790.js</code> - [Regex 1] <code>location.href=r</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48001.326bc790.js</code> - [Regex 1] <code>new URL(window.location.href</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48001.326bc790.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code> - [Regex 1] <code>location.href=`</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code> - [Regex 2] <code>o.get("parent_manage_type")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code> - [Regex 2] <code>s.get("/datatester/compass/api/v3/knowledge/feishu/doc/authorize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/57671.49fbaaac.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/57671.49fbaaac.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code> - [Regex 2] <code>a.get(`/datatester/experiment/api/v3/app/-1/experiment?page_size=9999&amp;is_holdout=1&amp;holdout_batch_id=${e}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code> - [Regex 2] <code>a.get(`/datatester/experiment/api/v3/apps/${e}/holdout/holdout_batch/${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code> - [Regex 2] <code>n.get("father_experiment_id")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code> - [Regex 2] <code>o.get("parent_manage_type")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code> - [Regex 2] <code>o.get(`/datatester/metric/api/v3/${l}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code> - [Regex 2] <code>o.get(`/datatester/rule/api/v3/apps/${t}/rules?type=recycle,risk,release_suggestion`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/65247.3231c58e.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/73667.5682fe30.js</code> - [Regex 1] <code>.query.app</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95936.3477233c.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)

### Route 42: <code>https://console.byteplus.com/datatester/app/566590/behavior-detail</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77520.022eb086.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77520.022eb086.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77520.022eb086.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77520.022eb086.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 43: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>

New matched JavaScript files:

- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code>

New regex matches:

- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.assign(</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=R</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=`</code> (x3)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=c</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=i</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=l</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=r</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.href=t</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location.replace(</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location=!</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location=e</code> (x6)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>new URL(location.href</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>window.location.assign(</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 1] <code>window.location.replace(</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get("/v1/approvals")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get("/v1/current_env")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get("/v1/current_user")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get("/v1/products")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1${e}/catalogs`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1${e}/resources/${n}?with_package=1&amp;with_rule=1`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1${e}/resources/${n}?with_rule=1&amp;with_history=1&amp;with_package=1`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1${n}/resource_packages?with_resource=1&amp;with_app=1`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1${n}/resource_rules`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1/apps/${n}/app_packages`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1/apps/${n}/permissions`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1/apps/${n}`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1/docs/${n}`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1/permissions/authorizations/${n}`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Ei.get(`/v1/products/${n}/resource_packages?with_resource=1`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Fh.get("/api/v1/whoami")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Pve.get("/v1/user")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Pve.get(`/v1/users/${n}/orgs`)</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Vp.get("_TEA_VE_APIHOST")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Vp.get("_TEA_VE_OPEN")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Vp.get("_VISUAL_EDITOR_U")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Vp.get("_VISUAL_EDITOR_V")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>Vp.get("lang")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.collect.configManager.get("custom")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.configManager.get("user_unique_id")</code> (x3)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.configManager.get("user_unique_id_type")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.configManager.get("web_id")</code> (x3)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/config")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/console")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/index")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/products")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/resources")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/solution/industry")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/solution/productability")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/solution/scene_conf")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/user")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>e.get("/v1/user/orgs")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>h.get("dashboardId")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>n.get("month")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>p.get("text")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>r.configManager.get("reportErrorCallback")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - [Regex 2] <code>r.configManager.get("user")</code> (x6)

### Route 47: <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code> - [Regex 1] <code>.query.data</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code> - [Regex 1] <code>.query.isFetched</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code> - [Regex 1] <code>.query.isLoading</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code> - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 48: <code>https://console.byteplus.com/datatester/app/566590/personalization/:campaignId/:campaignTab</code>

New matched JavaScript files: none

New regex matches: none

### Route 50: <code>https://console.byteplus.com/datatester/app/566590/tour</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/30972.1e37cec5.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/30972.1e37cec5.js</code> - [Regex 2] <code>i.get(`${c}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/30972.1e37cec5.js</code> - [Regex 2] <code>i.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/30972.1e37cec5.js</code> - [Regex 2] <code>i.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)

### Route 51: <code>https://console.byteplus.com/datatester/app/566590/guide</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6153.d03c43cf.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6153.d03c43cf.js</code> - [Regex 2] <code>r.get(`${c}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6153.d03c43cf.js</code> - [Regex 2] <code>r.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6153.d03c43cf.js</code> - [Regex 2] <code>r.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> (x1)

### Route 52: <code>https://console.byteplus.com/datatester/app/566590/demo-h5</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/38167.19428004.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/38167.19428004.js</code> - [Regex 1] <code>location.href=q</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/38167.19428004.js</code> - [Regex 2] <code>i.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 65: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4427.4a710825.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/45173.ea9352cb.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5549.81b452d5.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4427.4a710825.js</code> - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/45173.ea9352cb.js</code> - [Regex 1] <code>location.href=x</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/45173.ea9352cb.js</code> - [Regex 1] <code>window.location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code> - [Regex 1] <code>.query.data</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code> - [Regex 1] <code>.query.isFetched</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code> - [Regex 1] <code>.query.isLoading</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code> - [Regex 1] <code>window.location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5549.81b452d5.js</code> - [Regex 2] <code>u.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${a}/metrics`)</code> (x1)

### Route 66: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/:mode?/:experimentId?</code>

New matched JavaScript files: none

New regex matches: none

### Route 67: <code>https://console.byteplus.com/datatester/app/566590/experiment/detail/:mode/:experimentId</code>

New matched JavaScript files: none

New regex matches: none

### Route 69: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/review/:reviewId/detail</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/17527.5b1fc02c.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/17527.5b1fc02c.js</code> - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 70: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 1] <code>location.href="</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 1] <code>location.href=o</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 1] <code>location.href=t</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>A.get("lineWidth")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>D.get("_order")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>D.get("_rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>Y.get("_order")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>Y.get("_rank")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>a.get("__source")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>a.get("__target")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>a.get("lineWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>a.get("parent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>c.get("container")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>d.get("linkNode")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>d.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>d.get("visible")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("__cacheMagnetStyles")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("_anchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("_order")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("anchorIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("children")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("collapsed")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("crossOrigin")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("cursor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("dummy")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("len")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("lineDash")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("order")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("originGroupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("originSource")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("originTarget")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("rank")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("reversed")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("source")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("target")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.get("temp")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>e.graph.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>g.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>h.get("anchors")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>h.get("linkNode")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>h.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>h.get("reversed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("anchorIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("anchors")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("minlen")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("path")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("points")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>i.get("rank")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>l.get("_editStyleCache")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>l.get("len")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>l.node.get("anchors")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("collapsed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("cursor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("disableAnchorEvent")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("disableNodeEvent")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("dummy")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("gapYs")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("originGroupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("outerNode")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("source")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("target")</code> (x6)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>n.get("titleHeight")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("__baseId")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("__count")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("anchors")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("depth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>o.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("_editStyleCache")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("_selections")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("anchorIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("collapsed")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("container")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("rank")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("sourceAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("target")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.get("targetAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>r.layer.get("__loadingCircle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>s.get("collapsed")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>s.get("container")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>s.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>s.get("source")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>s.get("target")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>s.get("titleSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_animateShow")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_background")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_keyShape")</code> (x10)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_label")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_order")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_paste")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("_selections")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("animateHandler")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("children")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("clickInteraction")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("collapsed")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("controlPoints")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("crossOrigin")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("destroyed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("dummy")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("encodeValue")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("endArrow")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("fillStyle")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("fixed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("groupId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("groupNodes")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("ignoreGrid")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("lineWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("mask")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("minlen")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("order")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("pixelRatio")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("rank")</code> (x9)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("root")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("setDefaultGroup")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("setDefaultNode")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("source")</code> (x7)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("startArrow")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("target")</code> (x7)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("targets")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("toDraw")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("triggerId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>t.get("weight")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("_editStyleCache")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("collapsed")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("source")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("sourceAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("styles")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("target")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>u.get("targetAnchor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - [Regex 2] <code>v.get("rank")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 1] <code>location.href="</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 1] <code>location.href=l</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 2] <code>a.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 2] <code>eP.get("/datatester/common-service/api/v3/apps/-1/app-info/filter-global-app/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 2] <code>eP.get(`${eB}app/${e}/experiment/${t}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 2] <code>eP.get(`${eU}launch-review/${e}/view/${l}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - [Regex 2] <code>eP.get(`${eU}launch-strategy/lark/groups/`)</code> (x1)

### Route 71: <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/ad-report</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75472.a3ebeed9.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75472.a3ebeed9.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 72: <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/3192.4c9ba2bb.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/3192.4c9ba2bb.js</code> - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 81: <code>https://console.byteplus.com/datatester/app/566590/flight/experience-config</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/53419.06fa74a6.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/53419.06fa74a6.js</code> - [Regex 1] <code>.query.is_open</code> (x1)

### Route 82: <code>https://console.byteplus.com/datatester/app/566590/flight/layer/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90193.0fc8bf16.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90193.0fc8bf16.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90193.0fc8bf16.js</code> - [Regex 2] <code>hA.get("/datatester/mutex/api/v3/layer_config")</code> (x1)

### Route 94: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - [Regex 1] <code>location=a</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - [Regex 2] <code>_.Ay.get("AttributeSelect.custom")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent1")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent2")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent3")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent4")</code> (x1)

### Route 100: <code>https://console.byteplus.com/datatester/app/566590/feature/list/:tag?</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74094.fbf11ba1.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74094.fbf11ba1.js</code> - [Regex 1] <code>.query.data</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74094.fbf11ba1.js</code> - [Regex 1] <code>.query.isFetched</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74094.fbf11ba1.js</code> - [Regex 1] <code>.query.isLoading</code> (x1)

### Route 101: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42269.a4a937aa.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/46458.0f3122db.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/67872.ebb0f9c5.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42269.a4a937aa.js</code> - [Regex 1] <code>.query.charCodeAt</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42269.a4a937aa.js</code> - [Regex 1] <code>.query.length</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42269.a4a937aa.js</code> - [Regex 1] <code>.query.spec</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/46458.0f3122db.js</code> - [Regex 1] <code>.query.data</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/46458.0f3122db.js</code> - [Regex 1] <code>.query.isFetched</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/46458.0f3122db.js</code> - [Regex 1] <code>.query.isLoading</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/67872.ebb0f9c5.js</code> - [Regex 1] <code>new URL(window.location.href</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/67872.ebb0f9c5.js</code> - [Regex 2] <code>r.get(`/datatester/feature-flag/api/v3/apps/${e}/permission-check/large-feature`)</code> (x1)

### Route 103: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/version/:featureAppId?</code>

New matched JavaScript files: none

New regex matches: none

### Route 109: <code>https://console.byteplus.com/datatester/app/566590/system/system-setting</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10837.794ed6ea.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10837.794ed6ea.js</code> - [Regex 2] <code>q.get(`/v2/management/confidence_level/${t}/`)</code> (x1)

### Route 110: <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code> - [Regex 1] <code>location.href=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code> - [Regex 1] <code>location.href=h</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code> - [Regex 1] <code>location=e</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code> - [Regex 1] <code>location=h</code> (x1)

### Route 112: <code>https://console.byteplus.com/datatester/app/566590/system/permission/list</code>

New matched JavaScript files: none

New regex matches: none

### Route 118: <code>https://console.byteplus.com/datatester/app/566590/system/origin-events</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77845.49b14a94.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77845.49b14a94.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77845.49b14a94.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77845.49b14a94.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 119: <code>https://console.byteplus.com/datatester/app/566590/system/simulator-manage</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14861.9dbbbb6d.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14861.9dbbbb6d.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14861.9dbbbb6d.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14861.9dbbbb6d.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 120: <code>https://console.byteplus.com/datatester/app/566590/system/event-params</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59334.99758278.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59334.99758278.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59334.99758278.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59334.99758278.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 121: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>

New matched JavaScript files:

- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/publicParams.1ab3a298.js#2</code>
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5179.82af1be3.js</code>

New regex matches:

- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/publicParams.1ab3a298.js#2</code> - [Regex 1] <code>location.href=r</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/publicParams.1ab3a298.js#2</code> - [Regex 1] <code>location.replace(</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href="</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=a</code> (x3)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=e</code> (x3)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=n</code> (x6)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=p</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=r</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=t</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location.href=u</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location=R</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location=e</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location=n</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>location=r</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 1] <code>window.location.replace(</code> (x5)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>a.get("onEffect")</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>e.configManager.get("user_unique_id")</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>e.configManager.get("web_id")</code> (x2)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>n.configManager.get("reportErrorCallback")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>n.configManager.get("user")</code> (x3)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>r.cfg.get("reportErrorCallback")</code> (x1)
- <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - [Regex 2] <code>t.cfg.get("evtParams")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5179.82af1be3.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5179.82af1be3.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5179.82af1be3.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 122: <code>https://console.byteplus.com/datatester/app/566590/system/virtual-params</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99979.c81dbd10.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99979.c81dbd10.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99979.c81dbd10.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99979.c81dbd10.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 123: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/create/web</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/85506.5d9746e8.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/85506.5d9746e8.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/85506.5d9746e8.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/85506.5d9746e8.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 124: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28445.1e26d244.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28445.1e26d244.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28445.1e26d244.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28445.1e26d244.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>E.get("smooth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>I.get("show")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>T.get("verticalAlign")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>_.get("formatter")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>_.get("show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("draggable")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("focusNodeAdjacency")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("ignoreForceLayout")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("itemStyle.color")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("label.margin")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("lineStyle.curveness")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("lineStyle.show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("show")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>a.get("symbolSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>c.get("show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>d.get("friction")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>d.get("gravity")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>d.get("parallelIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.ecModel.get("useUTC")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("animation")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("avoidLabelOverlap")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("axisExpandRate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("axisLabel.inside")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("axisLine.lineStyle.color")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("axisTick.inside")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("backgroundColor")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("barMaxWidth")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("barMinWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("barWidth")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("borderRadius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("boundaryGap")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("calendarIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("center")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("circular.rotateLabel")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("confine")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("connectNulls")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("containLabel")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("edgeForkPosition")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("edgeShape")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("edgeSymbol")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("edgeSymbolSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("endAngle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("enterable")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("expandAndCollapse")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("extraCssText")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("gradientColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("hoverAnimation")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("inverse")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("itemGap")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("itemSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("label.align")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("label.baseline")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("label.verticalAlign")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("layoutIterations")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("legendHoverLink")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("lineStyle.curveness")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("max")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("maxSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("min")</code> (x4)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("minShowLabelAngle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("minSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("nameMap")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("nodeAlign")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("orient")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("parallelIndex")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("radarIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("radius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("realtime")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("roam")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("scaleLimit")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("selectedMode")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("show")</code> (x9)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("showContent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("showLegendSymbol")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("showTitle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("silent")</code> (x5)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("smooth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("smoothMonotone")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("stack")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("startAngle")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("step")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("subtarget")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("symbol")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("symbolMargin")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("symbolOffset")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("symbolRotate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("symbolSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("target")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("text")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("textBaseline")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("textVerticalAlign")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("title.0.text")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("triggerEvent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("visualDimension")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("z")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("zlevel")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>e.get("zoom")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("borderColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("borderRadius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("borderWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("buttonColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("buttonTextColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("itemGap")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("itemSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("readOnly")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("shadowBlur")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("shadowColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("shadowOffsetX")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("shadowOffsetY")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>f.get("title")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>g.get("barBorderRadius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>g.get("r")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>g.get("r0")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>h.get("renderMode")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("axisLine.lineStyle.color")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("icon")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("inverse")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("lineStyle.curveness")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("option.bar")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("option.line")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("option.stack")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("polyline")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("show")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("triggerEvent")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>i.get("triggerOn")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>l.get("label.formatter")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>l.get("label.precision")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>l.get("rotate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>m.get("axisPointer.axis")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>m.get("show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("animation")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("axisExpandTriggerOn")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("axisExpandable")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("backgroundColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("borderRadius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("connectedBackgroundColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("coordinateSystem")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("dim")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("excludeComponents")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("hoverAnimation")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("itemStyle.color")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("label.formatter")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("label.precision")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("markLine")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("markPoint")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("pixelRatio")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("rotate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("seriesDataIndices")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("stack")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("symbolRepeatDirection")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("symbolRotate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("textStyle.color")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("value")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("z")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>n.get("zoomLock")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>o.get("boundaryGap")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>o.get("emptyItemWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>o.get("focusNodeAdjacency")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>o.get("formatterParams")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>o.get("rotate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>o.get("show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>p.get("ellipsis")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("borderColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("dataBackgroundColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("description")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("fillerColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("formatter")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("handleIcon")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("handleSize")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("realtime")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>r.get("show")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>s.get("inside")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>s.get("rippleEffect.period")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>s.get("tooltip")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("alignWithLabel")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisExpandCenter")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisExpandCount")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisExpandDebounce")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisExpandWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisLabel.inside")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisLabel.show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisLine.lineStyle.color")</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisLine.show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("axisTick.inside")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("backgroundColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("barMaxWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("barMinWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("borderColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("borderRadius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("borderWidth")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("cursor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("delay")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("geoCoord")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("hoverAnimation")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("itemGap")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("itemStyle.color")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("label.show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("maxInterval")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("minInterval")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("orient")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("parallelId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("parallelIndex")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("period")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("polarId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("polarIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("radarIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("scaleLimit")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("showDetail")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("showLegendSymbol")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("singleAxisId")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("singleAxisIndex")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("symbolOffset")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.get("symbolRotate")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>t.hostModel.get("percentPrecision")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("animation")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("hoverOffset")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("icon")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("selectedOffset")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("textAlign")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("textBackgroundColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("textBorderRadius")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("textFill")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("textPadding")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("textPosition")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>u.get("throttle")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>x.get("emphasis.label.position")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>x.get("show")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>y.get("dataBackgroundColor")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - [Regex 2] <code>y.get("show")</code> (x1)

### Route 125: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78118.efd8ad5a.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78118.efd8ad5a.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78118.efd8ad5a.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78118.efd8ad5a.js</code> - [Regex 2] <code>i.A.get("x-rgw-dor")</code> (x2)

### Route 128: <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43762.350c7dd2.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43762.350c7dd2.js</code> - [Regex 2] <code>tq.get("/datatester/experiment/api/v3/third-take-over/system-names")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43762.350c7dd2.js</code> - [Regex 2] <code>tq.get(`/datatester/common-service/api/v3/apps/${n}/workflow-templates/metrics-filter/${l}`)</code> (x1)

### Route 134: <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-user-list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/54562.8ee76a9d.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/54562.8ee76a9d.js</code> - [Regex 2] <code>u.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${s}`)</code> (x1)

### Route 135: <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-manage-list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/31062.6d254733.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/31062.6d254733.js</code> - [Regex 2] <code>u.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${s}`)</code> (x1)

### Route 136: <code>https://console.byteplus.com/datatester/app/566590/system/scheduled-task-management</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/88928.499aa73b.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/88928.499aa73b.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/88928.499aa73b.js</code> - [Regex 2] <code>j.get(`/datatester/api/v2/management/apps/${e}/cronjob/settings`)</code> (x1)

### Route 137: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40287.de3b0782.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40287.de3b0782.js</code> - [Regex 2] <code>u.get(`/v2/apps/${e}/pre_tab_task/${t}/retry`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code> - [Regex 1] <code>location.href=h</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code> - [Regex 1] <code>location.href=t</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code> - [Regex 1] <code>location=h</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code> - [Regex 1] <code>location=t</code> (x1)

### Route 138: <code>https://console.byteplus.com/datatester/app/566590/system/templates/basic</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50481.c0109988.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50481.c0109988.js</code> - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 139: <code>https://console.byteplus.com/datatester/app/566590/system/templates/editor</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64140.9e9ecfa7.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64140.9e9ecfa7.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64140.9e9ecfa7.js</code> - [Regex 2] <code>l.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${t}/metrics`)</code> (x1)

### Route 140: <code>https://console.byteplus.com/datatester/app/566590/system/templates/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13910.8de76419.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13910.8de76419.js</code> - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 141: <code>https://console.byteplus.com/datatester/app/566590/user-cohort/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59694.dc35e0c0.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59694.dc35e0c0.js</code> - [Regex 2] <code>_.get(`/datatester/api/v2/app/${t}/cohort/${a}/refresh`)</code> (x1)

### Route 146: <code>https://console.byteplus.com/datatester/app/566590/metric-group/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/34036.11e62fd1.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/34036.11e62fd1.js</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/34036.11e62fd1.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x2)

### Route 148: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50476.2b42d973.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58444.2ee6a332.js</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/brace.e9c426df.async.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50476.2b42d973.js</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58444.2ee6a332.js</code> - [Regex 1] <code>new URLSearchParams(window.location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/brace.e9c426df.async.js</code> - [Regex 1] <code>location.replace(</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/brace.e9c426df.async.js</code> - [Regex 2] <code>o.get("packaged")</code> (x1)

### Route 151: <code>https://console.byteplus.com/datatester/app/566590/metric-group/detail/:id?</code>

New matched JavaScript files: none

New regex matches: none

### Route 152: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 1] <code>.query.data</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 1] <code>.query.isFetched</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 1] <code>.query.isLoading</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 1] <code>new URLSearchParams(location.search</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 2] <code>ey.get(`${ex}${i}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 2] <code>l.get(`/datatester/metric/api/v3/${a}`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - [Regex 2] <code>l.get(`/datatester/rule/api/v3/apps/${t}/rules?type=recycle,risk,release_suggestion`)</code> (x1)

### Route 175: <code>https://console.byteplus.com/datatester/app/566590/toolbox/user-hit</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56722.95fe8edf.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56722.95fe8edf.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 176: <code>https://console.byteplus.com/datatester/app/566590/toolbox/diagnosis</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/23200.177e5a97.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/23200.177e5a97.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 178: <code>https://console.byteplus.com/datatester/app/566590/toolbox/calculator</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77901.a002a061.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77901.a002a061.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 179: <code>https://console.byteplus.com/datatester/app/566590/toolbox/vm-simulation</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61022.0272997e.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61022.0272997e.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 182: <code>https://console.byteplus.com/datatester/app/566590/open/integration/create</code>

New matched JavaScript files: none

New regex matches: none

### Route 196: <code>https://console.byteplus.com/datatester/app/566590/open/template/:id/:mode</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43704.27d5aba2.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43704.27d5aba2.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 203: <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code> - [Regex 1] <code>.query.abOpConfigId</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code> - [Regex 1] <code>.query.isShowConfigPane</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code> - [Regex 2] <code>T.get(`${k}/v1/apps/${e.appId}/optimization-plans/${e.planId}/subgoals`)</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code> - [Regex 2] <code>T.get(`${k}/v1/apps/${e.appId}/optimization-plans/${e.planId}`)</code> (x1)

### Route 206: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/list</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/52295.90ceff7b.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/52295.90ceff7b.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)

### Route 207: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/create</code>

New matched JavaScript files:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/87017.c29a62f1.js</code>

New regex matches:

- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/87017.c29a62f1.js</code> - [Regex 1] <code>new URL(window.location.href</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/87017.c29a62f1.js</code> - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> (x1)
- <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/87017.c29a62f1.js</code> - [Regex 2] <code>rZ.get(`/datatester/feature-flag/api/v4/apps/${t}/permission-check/user-tag`)</code> (x1)

## Unique JavaScript Files With Matches

### 1. <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-sg/log-sdk/collect/5/plugin/visual.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 1
  - [Regex 1] <code>new URL(window.location.href</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 2. <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 7
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>new URL(location.href</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id_type")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>e.configManager.get("web_id")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>n.configManager.get("reportErrorCallback")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>r.configManager.get("user")</code> - occurrences: 7 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 3. <code>https://lf16-unpkg-i18n.byted-static.com/obj/unpkg-va/xgplayer/2.9.6/browser/index.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 1
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 4. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/1.0.0.1528/preload.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 2
  - [Regex 1] <code>location.href=e</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=i</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 5. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/19362.6387ad3d.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 1
  - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 6. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 5
  - [Regex 2] <code>l.get(`/datatester/common-service/api/v3/apps/custom-config/${e}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>l.get(`/datatester/experiment/api/v3/process/${e}/detail`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/${t}/brief`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/history/${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 7. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 5
  - [Regex 1] <code>location.assign(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=i</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location=a</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>tf.A.get("csrfToken")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 8. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 11
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href="</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=`</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=a</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=t</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>eI.get(`v1/volc/orgs/${e}/operation_deadline`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>eP.get(`/org/${e}/operation_deadline`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>p.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${a}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 9. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6123.0837ab6d.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 10. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/7454.8b7b620f.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 3
  - [Regex 2] <code>o.get(`${p}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>o.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>o.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 11. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 8
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=i</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=n</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=t</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.replace(</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>window.location.replace(</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>i.get("onEffect")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 12. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/arco_designs.7f78af21.async.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 1
  - [Regex 2] <code>t.get("month")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 13. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 6
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>d.get(`/v2/app/${e}/recipient/list?${o.stringify(a)}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>n.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>n.get(`/v2/userinfo?org_id=${e}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>p.get("/v2/org_list")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 14. <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
- Loaded on routes: 1, 2, 3, 4, 11, 12, 13, 23, 26, 32, 36, 37, 39, 40, 41, 42, 43, 47, 48, 50, 51, 52, 65, 66, 67, 69, 70, 71, 72, 81, 82, 94, 100, 101, 103, 109, 110, 112, 118, 119, 120, 121, 122, 123, 124, 125, 128, 134, 135, 136, 137, 138, 139, 140, 141, 146, 148, 151, 152, 175, 176, 178, 179, 182, 196, 203, 206, 207
- Unique matches: 6
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>location.href=p</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>i.Z.get("__spti")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>
  - [Regex 2] <code>rb.Z.get("csrfToken")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tinder_plan_v2</code>

### 15. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48496.5b2a454b.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>
- Loaded on routes: 2, 12, 112
- Unique matches: 2
  - [Regex 1] <code>location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>
  - [Regex 1] <code>location=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>

### 16. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58519.f0df961e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>
- Loaded on routes: 2, 12, 112
- Unique matches: 2
  - [Regex 2] <code>eG.get(`${eL}v3/apps/${e}/metadata/properties`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>
  - [Regex 2] <code>eG.get(`${eL}v3/apps/${e}/portal/role/${t}/property-desensitization`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/invite-confirm/:appId</code>

### 17. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4806.0109974e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/ai-research</code>
- Loaded on routes: 3
- Unique matches: 1
  - [Regex 2] <code>C.get("/datatester/compass/api/v3/survey/user_info")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/ai-research</code>

### 18. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13384.373605de.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/redirect</code>
- Loaded on routes: 4, 41, 51, 65, 67, 69, 70, 71, 72, 138, 139, 140, 196
- Unique matches: 1
  - [Regex 1] <code>location.href=`</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/redirect</code>

### 19. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/22146.69329a00.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/redirect</code>
- Loaded on routes: 4
- Unique matches: 3
  - [Regex 2] <code>c.get(`/datatester/api/v2/apps/${t}/features/cohorts_open_status?feature_id=${a}&amp;version=${r}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/redirect</code>
  - [Regex 2] <code>c.get(`/datatester/api/v2/apps/${t}/flights/cohorts_open_status?flight_id=${a}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/redirect</code>
  - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/redirect</code>

### 20. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61407.d6e23ed9.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/redirect</code>
- Loaded on routes: 4, 41, 51, 67, 69, 70, 71, 72, 138, 139, 140, 196
- Unique matches: 1
  - [Regex 1] <code>window.location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/redirect</code>

### 21. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75360.0ea54511.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/redirect</code>
- Loaded on routes: 4, 41, 51, 67, 69, 70, 71, 72, 138, 139, 140, 196
- Unique matches: 1
  - [Regex 2] <code>l.get(`/datatester/experiment/api/v3/app/${e}/traffic_info/${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/redirect</code>

### 22. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6625.8405fd46.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/volc-sale</code>
- Loaded on routes: 11, 39
- Unique matches: 1
  - [Regex 1] <code>location.href=`</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/volc-sale</code>

### 23. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14518.9565419e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/org/create</code>
- Loaded on routes: 13
- Unique matches: 3
  - [Regex 2] <code>u.get(`${c}/v3/app/${t.app_id}/call-source/${t.id}/access-status`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/org/create</code>
  - [Regex 2] <code>u.get(`/datarangers/api/org/${t}/tester-subjects?project_id=${e}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/org/create</code>
  - [Regex 2] <code>u.get(`/datatester/org_management/api/org/${t}/tester-subjects?project_id=${e}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/org/create</code>

### 24. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/66107.93c9a306.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/org/create</code>
- Loaded on routes: 13
- Unique matches: 3
  - [Regex 2] <code>o.get(`${u}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/org/create</code>
  - [Regex 2] <code>o.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/org/create</code>
  - [Regex 2] <code>o.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/org/create</code>

### 25. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6127.02689e58.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
- Loaded on routes: 23, 41, 48, 51, 65, 67, 69, 70, 71, 72, 101, 103, 128, 138, 139, 140, 196, 207
- Unique matches: 2
  - [Regex 2] <code>u.get(`/datatester/api/v2/apps/${l}/features/cohorts_open_status?feature_id=${t}&amp;version=${n}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>u.get(`/datatester/api/v2/apps/${l}/flights/cohorts_open_status?flight_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>

### 26. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95783.90718b0f.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
- Loaded on routes: 23
- Unique matches: 1
  - [Regex 1] <code>location=0</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>

### 27. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
- Loaded on routes: 23
- Unique matches: 15
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 1] <code>location=!</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 1] <code>location=e</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>e.collect.configManager.get("custom")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id_type")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>e.configManager.get("web_id")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>fS.get("_TEA_VE_APIHOST")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>fS.get("_VISUAL_EDITOR_U")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>fS.get("_VISUAL_EDITOR_V")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>fS.get("lang")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>i.configManager.get("user")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>n.configManager.get("reportErrorCallback")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>
  - [Regex 2] <code>n.get("defaultKeyword")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/dashboard</code>

### 28. <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/log-sdk/collect/visual-ab-inspector.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>
- Loaded on routes: 26
- Unique matches: 2
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>

### 29. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61859.05b038a9.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>
- Loaded on routes: 26
- Unique matches: 2
  - [Regex 1] <code>location.href=l</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/:flightStatus/:flightId/visual-editor/version/:versionId</code>

### 30. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/69835.b7f0e2d2.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/event-group</code>
- Loaded on routes: 32
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/event-group</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/event-group</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/event-group</code>

### 31. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>
- Loaded on routes: 36
- Unique matches: 5
  - [Regex 2] <code>na.get(`/projects/${a}/apps/ios/lookup?download_url=${encodeURIComponent(e)}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>
  - [Regex 2] <code>na.get(`/projects/${l}/apps/sync-res?request_id=${r}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>
  - [Regex 2] <code>s6.get(`${s8(i)}/industries?account_id=${r}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>
  - [Regex 2] <code>s6.get(`${s8(i)}/universal-materials/check?material_ids=${e}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>
  - [Regex 2] <code>vu.get(`/projects/${l}/channels/${e}/experiment-creation-task/${a}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch</code>

### 32. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
- Loaded on routes: 37
- Unique matches: 4
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
  - [Regex 1] <code>location.href=p</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
  - [Regex 1] <code>location=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
  - [Regex 1] <code>location=p</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>

### 33. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
- Loaded on routes: 37, 41, 179, 182
- Unique matches: 4
  - [Regex 1] <code>.query.modelInfo</code> - occurrences: 7 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
  - [Regex 1] <code>.query.word</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>
  - [Regex 2] <code>e.get("text")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/scene/llm</code>

### 34. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99606.9cf38234.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/volcSale/caliber</code>
- Loaded on routes: 40
- Unique matches: 1
  - [Regex 2] <code>M.get(`/v2/app/${n}/management/event_usage/`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/volcSale/caliber</code>

### 35. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/11053.6fd86b1e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41
- Unique matches: 1
  - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 36. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 139, 140, 196
- Unique matches: 27
  - [Regex 1] <code>location=!</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.attributes.get("scriptlevel")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("bevelled")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("largeop")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("linethickness")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("mathsize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("lspace")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("rspace")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("data-semantic-speech")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("lspace")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("mathsize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("rspace")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("scriptlevel")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("scriptminsize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("scriptsizemultiplier")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.node.attributes.get("bevelled")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("frame")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("mjx-keep-attrs")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("depth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.gullet.macros.get("\\df@tag")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.attributes.get("columnalign")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.attributes.get("columnspacing")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("background-color")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("font-family")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.gullet.macros.get("\\df@tag")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.macros.get("\\df@tag")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.node.attributes.get("selection")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 37. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28073.a2217d3f.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 139, 140, 196
- Unique matches: 3
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get(`${i}/template-group`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("parent_manage_type")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 38. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41
- Unique matches: 151
  - [Regex 2] <code>B.get("lineWidth")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>C.get("_order")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>C.get("_rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>Y.get("_order")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>Y.get("_rank")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get("__source")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get("__target")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get("collapsed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get("groupTitle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get("lineWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get("rank")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>c.get("_editStyleCache")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>c.get("anchors")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>c.get("cluster")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>c.get("len")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>c.get("visible")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>d.get("linkNode")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>d.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>d.get("visible")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.canvas.get("pixelRatio")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("__cacheMagnetStyles")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("_anchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("_children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("_order")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("anchorIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("branchCount")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("children")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("collapsed")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("crossOrigin")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("cursor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("dummy")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("len")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("lineDash")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("linkGroupOnCollapse")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("order")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("originGroupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("originSize")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("originSource")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("originTarget")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("rank")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("reversed")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("source")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.get("target")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.graph.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>e.relatedTarget.get("children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>g.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>g.get("visible")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>h.get("container")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>h.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("_editStyleCache")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("anchorIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("children")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("collapsed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("parent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("rank")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("sourceAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("target")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.get("targetAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>i.layer.get("__loadingCircle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>l.get("linkNode")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>l.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>l.get("reversed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("collapsed")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("container")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("cursor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("dummy")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("fontSize")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("gapYs")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("originGroupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("originSize")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("outerNode")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("rank")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("source")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("target")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("titleHeight")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("_children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("anchors")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("attr")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("cluster")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("depth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("target")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("anchorIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("anchors")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("minlen")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("parent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("path")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("points")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("rank")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>r.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("container")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("parent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("target")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.node.get("anchors")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.canvas.get("pixelRatio")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_animateShow")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_background")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_keyShape")</code> - occurrences: 10 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_label")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_order")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_paste")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("_selections")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("animateHandler")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("children")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("clickInteraction")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("collapsed")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("controlPoints")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("destroyed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("dummy")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("encodeValue")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("endArrow")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("fillStyle")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("fixed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("groupNodes")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("ignoreGrid")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("mask")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("minlen")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("order")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("pixelRatio")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("rank")</code> - occurrences: 9 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("root")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("source")</code> - occurrences: 7 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("startArrow")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("target")</code> - occurrences: 8 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("targets")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("toDraw")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("triggerId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>t.get("weight")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("_editStyleCache")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("children")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("collapsed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("source")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("sourceAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("styles")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("target")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>u.get("targetAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>v.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 39. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40184.07ffaccf.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 196
- Unique matches: 2
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 40. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/41974.52459966.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 139, 140, 175, 176, 178, 179, 196, 206, 207
- Unique matches: 3
  - [Regex 1] <code>.query.data</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>.query.isFetched</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>.query.isLoading</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 41. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42360.4dfa46fb.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 140, 196
- Unique matches: 2
  - [Regex 1] <code>location.href=`</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${t}/metrics`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 42. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48001.326bc790.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 67, 69, 70, 71, 72, 138, 140, 196
- Unique matches: 3
  - [Regex 1] <code>location.href=r</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>new URL(window.location.href</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 43. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 139, 140, 196
- Unique matches: 4
  - [Regex 1] <code>location.href=`</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("parent_manage_type")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>s.get("/datatester/compass/api/v3/knowledge/feishu/doc/authorize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 44. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/57671.49fbaaac.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41
- Unique matches: 2
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 45. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 67, 69, 70, 71, 72, 138, 139, 140, 196
- Unique matches: 4
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get(`/datatester/experiment/api/v3/app/-1/experiment?page_size=9999&amp;is_holdout=1&amp;holdout_batch_id=${e}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>a.get(`/datatester/experiment/api/v3/apps/${e}/holdout/holdout_batch/${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>n.get("father_experiment_id")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 46. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 139, 140, 196
- Unique matches: 4
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get("parent_manage_type")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get(`/datatester/metric/api/v3/${l}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
  - [Regex 2] <code>o.get(`/datatester/rule/api/v3/apps/${t}/rules?type=recycle,risk,release_suggestion`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 47. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/65247.3231c58e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 139, 140, 196
- Unique matches: 1
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 48. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/73667.5682fe30.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 140, 175, 176, 178, 179, 196, 206, 207
- Unique matches: 1
  - [Regex 1] <code>.query.app</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 49. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95936.3477233c.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>
- Loaded on routes: 41, 51, 69, 70, 71, 138, 140, 196
- Unique matches: 1
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/form-editor</code>

### 50. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77520.022eb086.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/behavior-detail</code>
- Loaded on routes: 42
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/behavior-detail</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/behavior-detail</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/behavior-detail</code>

### 51. <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
- Loaded on routes: 43
- Unique matches: 58
  - [Regex 1] <code>location.assign(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=R</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=`</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=c</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=i</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=l</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=r</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.href=t</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location=!</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location=e</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>new URL(location.href</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>window.location.assign(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 1] <code>window.location.replace(</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get("/v1/approvals")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get("/v1/current_env")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get("/v1/current_user")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get("/v1/products")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1${e}/catalogs`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1${e}/resources/${n}?with_package=1&amp;with_rule=1`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1${e}/resources/${n}?with_rule=1&amp;with_history=1&amp;with_package=1`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1${n}/resource_packages?with_resource=1&amp;with_app=1`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1${n}/resource_rules`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1/apps/${n}/app_packages`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1/apps/${n}/permissions`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1/apps/${n}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1/docs/${n}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1/permissions/authorizations/${n}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Ei.get(`/v1/products/${n}/resource_packages?with_resource=1`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Fh.get("/api/v1/whoami")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Pve.get("/v1/user")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Pve.get(`/v1/users/${n}/orgs`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Vp.get("_TEA_VE_APIHOST")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Vp.get("_TEA_VE_OPEN")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Vp.get("_VISUAL_EDITOR_U")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Vp.get("_VISUAL_EDITOR_V")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>Vp.get("lang")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.collect.configManager.get("custom")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id_type")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.configManager.get("web_id")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/config")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/console")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/index")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/products")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/resources")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/solution/industry")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/solution/productability")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/solution/scene_conf")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/user")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>e.get("/v1/user/orgs")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>h.get("dashboardId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>n.get("month")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>p.get("text")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>r.configManager.get("reportErrorCallback")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>
  - [Regex 2] <code>r.configManager.get("user")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open-api</code>

### 52. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code>
- Loaded on routes: 47
- Unique matches: 4
  - [Regex 1] <code>.query.data</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code>
  - [Regex 1] <code>.query.isFetched</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code>
  - [Regex 1] <code>.query.isLoading</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code>
  - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/list</code>

### 53. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/30972.1e37cec5.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/tour</code>
- Loaded on routes: 50
- Unique matches: 3
  - [Regex 2] <code>i.get(`${c}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tour</code>
  - [Regex 2] <code>i.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tour</code>
  - [Regex 2] <code>i.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/tour</code>

### 54. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6153.d03c43cf.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/guide</code>
- Loaded on routes: 51
- Unique matches: 3
  - [Regex 2] <code>r.get(`${c}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/guide</code>
  - [Regex 2] <code>r.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/guide</code>
  - [Regex 2] <code>r.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/guide</code>

### 55. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/38167.19428004.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/demo-h5</code>
- Loaded on routes: 52
- Unique matches: 2
  - [Regex 1] <code>location.href=q</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/demo-h5</code>
  - [Regex 2] <code>i.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/demo-h5</code>

### 56. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4427.4a710825.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
- Loaded on routes: 65, 66, 67, 139
- Unique matches: 1
  - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>

### 57. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/45173.ea9352cb.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
- Loaded on routes: 65, 66, 139
- Unique matches: 2
  - [Regex 1] <code>location.href=x</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
  - [Regex 1] <code>window.location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>

### 58. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
- Loaded on routes: 65
- Unique matches: 5
  - [Regex 1] <code>.query.data</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
  - [Regex 1] <code>.query.isFetched</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
  - [Regex 1] <code>.query.isLoading</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
  - [Regex 1] <code>window.location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>

### 59. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5549.81b452d5.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>
- Loaded on routes: 65, 66
- Unique matches: 1
  - [Regex 2] <code>u.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${a}/metrics`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/create/mab/:experimentId?</code>

### 60. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/17527.5b1fc02c.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/review/:reviewId/detail</code>
- Loaded on routes: 69
- Unique matches: 1
  - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/review/:reviewId/detail</code>

### 61. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
- Loaded on routes: 70
- Unique matches: 137
  - [Regex 1] <code>location.href="</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 1] <code>location.href=o</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 1] <code>location.href=t</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>A.get("lineWidth")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>D.get("_order")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>D.get("_rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>Y.get("_order")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>Y.get("_rank")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>a.get("__source")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>a.get("__target")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>a.get("lineWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>a.get("parent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>c.get("container")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>d.get("linkNode")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>d.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>d.get("visible")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("__cacheMagnetStyles")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("_anchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("_order")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("anchorIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("children")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("collapsed")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("crossOrigin")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("cursor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("dummy")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("len")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("lineDash")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("order")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("originGroupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("originSource")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("originTarget")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("rank")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("reversed")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("source")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("target")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.get("temp")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>e.graph.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>g.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>h.get("anchors")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>h.get("linkNode")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>h.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>h.get("reversed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("anchorIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("anchors")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("minlen")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("path")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("points")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>i.get("rank")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>l.get("_editStyleCache")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>l.get("len")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>l.node.get("anchors")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("collapsed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("cursor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("disableAnchorEvent")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("disableNodeEvent")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("dummy")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("gapYs")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("originGroupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("outerNode")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("source")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("target")</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>n.get("titleHeight")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("__baseId")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("__count")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("anchors")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("depth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>o.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("_editStyleCache")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("_selections")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("anchorIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("collapsed")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("container")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("rank")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("sourceAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("target")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.get("targetAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>r.layer.get("__loadingCircle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>s.get("collapsed")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>s.get("container")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>s.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>s.get("source")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>s.get("target")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>s.get("titleSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_animateShow")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_background")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_keyShape")</code> - occurrences: 10 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_label")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_order")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_paste")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("_selections")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("animateHandler")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("children")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("clickInteraction")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("collapsed")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("controlPoints")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("crossOrigin")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("destroyed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("dummy")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("encodeValue")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("endArrow")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("fillStyle")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("fixed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("groupId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("groupNodes")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("ignoreGrid")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("lineWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("mask")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("minlen")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("order")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("pixelRatio")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("rank")</code> - occurrences: 9 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("root")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("setDefaultGroup")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("setDefaultNode")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("source")</code> - occurrences: 7 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("startArrow")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("target")</code> - occurrences: 7 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("targets")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("toDraw")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("triggerId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>t.get("weight")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("_editStyleCache")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("collapsed")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("source")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("sourceAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("styles")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("target")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>u.get("targetAnchor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>v.get("rank")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>

### 62. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
- Loaded on routes: 70
- Unique matches: 9
  - [Regex 1] <code>location.href="</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 1] <code>location.href=l</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>a.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>eP.get("/datatester/common-service/api/v3/apps/-1/app-info/filter-global-app/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>eP.get(`${eB}app/${e}/experiment/${t}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>eP.get(`${eU}launch-review/${e}/view/${l}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>
  - [Regex 2] <code>eP.get(`${eU}launch-strategy/lark/groups/`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/reviewinfo</code>

### 63. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75472.a3ebeed9.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/ad-report</code>
- Loaded on routes: 71
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/ad-report</code>

### 64. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/3192.4c9ba2bb.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report</code>
- Loaded on routes: 72
- Unique matches: 1
  - [Regex 2] <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report</code>

### 65. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/53419.06fa74a6.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/experience-config</code>
- Loaded on routes: 81
- Unique matches: 1
  - [Regex 1] <code>.query.is_open</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/experience-config</code>

### 66. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90193.0fc8bf16.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/layer/list</code>
- Loaded on routes: 82
- Unique matches: 2
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/layer/list</code>
  - [Regex 2] <code>hA.get("/datatester/mutex/api/v3/layer_config")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/layer/list</code>

### 67. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>
- Loaded on routes: 94, 203, 207
- Unique matches: 6
  - [Regex 1] <code>location=a</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>
  - [Regex 2] <code>_.Ay.get("AttributeSelect.custom")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>
  - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent1")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>
  - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent2")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>
  - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent3")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>
  - [Regex 2] <code>_.Ay.get("AttributeSelect.noContent4")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric/board</code>

### 68. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74094.fbf11ba1.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/list/:tag?</code>
- Loaded on routes: 100
- Unique matches: 3
  - [Regex 1] <code>.query.data</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/list/:tag?</code>
  - [Regex 1] <code>.query.isFetched</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/list/:tag?</code>
  - [Regex 1] <code>.query.isLoading</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/list/:tag?</code>

### 69. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42269.a4a937aa.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
- Loaded on routes: 101, 103, 207
- Unique matches: 3
  - [Regex 1] <code>.query.charCodeAt</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
  - [Regex 1] <code>.query.length</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
  - [Regex 1] <code>.query.spec</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>

### 70. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/46458.0f3122db.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
- Loaded on routes: 101
- Unique matches: 3
  - [Regex 1] <code>.query.data</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
  - [Regex 1] <code>.query.isFetched</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
  - [Regex 1] <code>.query.isLoading</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>

### 71. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/67872.ebb0f9c5.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
- Loaded on routes: 101, 103
- Unique matches: 2
  - [Regex 1] <code>new URL(window.location.href</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>
  - [Regex 2] <code>r.get(`/datatester/feature-flag/api/v3/apps/${e}/permission-check/large-feature`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/edit</code>

### 72. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10837.794ed6ea.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/system-setting</code>
- Loaded on routes: 109
- Unique matches: 1
  - [Regex 2] <code>q.get(`/v2/management/confidence_level/${t}/`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/system-setting</code>

### 73. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code>
- Loaded on routes: 110
- Unique matches: 4
  - [Regex 1] <code>location.href=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code>
  - [Regex 1] <code>location.href=h</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code>
  - [Regex 1] <code>location=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code>
  - [Regex 1] <code>location=h</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/data-overview</code>

### 74. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77845.49b14a94.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/origin-events</code>
- Loaded on routes: 118
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/origin-events</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/origin-events</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/origin-events</code>

### 75. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14861.9dbbbb6d.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/simulator-manage</code>
- Loaded on routes: 119
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/simulator-manage</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/simulator-manage</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/simulator-manage</code>

### 76. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59334.99758278.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/event-params</code>
- Loaded on routes: 120
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/event-params</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/event-params</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/event-params</code>

### 77. <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/publicParams.1ab3a298.js#2</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
- Loaded on routes: 121
- Unique matches: 2
  - [Regex 1] <code>location.href=r</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>

### 78. <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
- Loaded on routes: 121
- Unique matches: 20
  - [Regex 1] <code>location.href="</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=a</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=e</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=n</code> - occurrences: 6 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=p</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=r</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=t</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location.href=u</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location=R</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location=e</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location=n</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>location=r</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>window.location.replace(</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>a.get("onEffect")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>e.configManager.get("user_unique_id")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>e.configManager.get("web_id")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>n.configManager.get("reportErrorCallback")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>n.configManager.get("user")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>r.cfg.get("reportErrorCallback")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>t.cfg.get("evtParams")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>

### 79. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5179.82af1be3.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
- Loaded on routes: 121
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/public-params</code>

### 80. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99979.c81dbd10.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/virtual-params</code>
- Loaded on routes: 122
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/virtual-params</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/virtual-params</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/virtual-params</code>

### 81. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/85506.5d9746e8.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/create/web</code>
- Loaded on routes: 123
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/create/web</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/create/web</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/create/web</code>

### 82. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28445.1e26d244.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
- Loaded on routes: 124
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>

### 83. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
- Loaded on routes: 124
- Unique matches: 230
  - [Regex 2] <code>E.get("smooth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>I.get("show")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>T.get("verticalAlign")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>_.get("formatter")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>_.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("draggable")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("focusNodeAdjacency")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("ignoreForceLayout")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("itemStyle.color")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("label.margin")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("lineStyle.curveness")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("lineStyle.show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("show")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>a.get("symbolSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>c.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>d.get("friction")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>d.get("gravity")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>d.get("parallelIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.ecModel.get("useUTC")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("animation")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("avoidLabelOverlap")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("axisExpandRate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("axisLabel.inside")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("axisLine.lineStyle.color")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("axisTick.inside")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("backgroundColor")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("barMaxWidth")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("barMinWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("barWidth")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("borderRadius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("boundaryGap")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("calendarIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("center")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("circular.rotateLabel")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("confine")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("connectNulls")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("containLabel")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("edgeForkPosition")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("edgeShape")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("edgeSymbol")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("edgeSymbolSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("endAngle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("enterable")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("expandAndCollapse")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("extraCssText")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("gradientColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("hoverAnimation")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("inverse")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("itemGap")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("itemSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("label.align")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("label.baseline")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("label.verticalAlign")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("layoutIterations")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("legendHoverLink")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("lineStyle.curveness")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("max")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("maxSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("min")</code> - occurrences: 4 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("minShowLabelAngle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("minSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("nameMap")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("nodeAlign")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("orient")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("parallelIndex")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("radarIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("radius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("realtime")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("roam")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("scaleLimit")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("selectedMode")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("show")</code> - occurrences: 9 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("showContent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("showLegendSymbol")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("showTitle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("silent")</code> - occurrences: 5 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("smooth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("smoothMonotone")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("stack")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("startAngle")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("step")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("subtarget")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("symbol")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("symbolMargin")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("symbolOffset")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("symbolRotate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("symbolSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("target")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("text")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("textBaseline")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("textVerticalAlign")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("title.0.text")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("triggerEvent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("visualDimension")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("z")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("zlevel")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>e.get("zoom")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("borderColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("borderRadius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("borderWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("buttonColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("buttonTextColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("itemGap")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("itemSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("readOnly")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("shadowBlur")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("shadowColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("shadowOffsetX")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("shadowOffsetY")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>f.get("title")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>g.get("barBorderRadius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>g.get("r")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>g.get("r0")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>h.get("renderMode")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("axisLine.lineStyle.color")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("icon")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("inverse")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("lineStyle.curveness")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("option.bar")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("option.line")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("option.stack")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("polyline")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("show")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("triggerEvent")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>i.get("triggerOn")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>l.get("label.formatter")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>l.get("label.precision")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>l.get("rotate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>m.get("axisPointer.axis")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>m.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("animation")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("axisExpandTriggerOn")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("axisExpandable")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("backgroundColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("borderRadius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("connectedBackgroundColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("coordinateSystem")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("dim")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("excludeComponents")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("hoverAnimation")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("itemStyle.color")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("label.formatter")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("label.precision")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("markLine")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("markPoint")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("pixelRatio")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("rotate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("seriesDataIndices")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("stack")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("symbolRepeatDirection")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("symbolRotate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("textStyle.color")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("value")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("z")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>n.get("zoomLock")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>o.get("boundaryGap")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>o.get("emptyItemWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>o.get("focusNodeAdjacency")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>o.get("formatterParams")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>o.get("rotate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>o.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>p.get("ellipsis")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("borderColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("dataBackgroundColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("description")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("fillerColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("formatter")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("handleIcon")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("handleSize")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("realtime")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>r.get("show")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>s.get("inside")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>s.get("rippleEffect.period")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>s.get("tooltip")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("alignWithLabel")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisExpandCenter")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisExpandCount")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisExpandDebounce")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisExpandWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisLabel.inside")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisLabel.show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisLine.lineStyle.color")</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisLine.show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("axisTick.inside")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("backgroundColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("barMaxWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("barMinWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("borderColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("borderRadius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("borderWidth")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("cursor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("delay")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("geoCoord")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("hoverAnimation")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("itemGap")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("itemStyle.color")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("label.show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("maxInterval")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("minInterval")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("orient")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("parallelId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("parallelIndex")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("period")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("polarId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("polarIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("radarIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("scaleLimit")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("showDetail")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("showLegendSymbol")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("singleAxisId")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("singleAxisIndex")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("symbolOffset")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.get("symbolRotate")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>t.hostModel.get("percentPrecision")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("animation")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("hoverOffset")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("icon")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("selectedOffset")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("textAlign")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("textBackgroundColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("textBorderRadius")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("textFill")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("textPadding")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("textPosition")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>u.get("throttle")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>x.get("emphasis.label.position")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>x.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>y.get("dataBackgroundColor")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>
  - [Regex 2] <code>y.get("show")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events/detail/:pageId</code>

### 84. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78118.efd8ad5a.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events</code>
- Loaded on routes: 125
- Unique matches: 3
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events</code>
  - [Regex 2] <code>i.A.get("x-rgw-dor")</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/bav-events</code>

### 85. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43762.350c7dd2.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/list</code>
- Loaded on routes: 128
- Unique matches: 2
  - [Regex 2] <code>tq.get("/datatester/experiment/api/v3/third-take-over/system-names")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/list</code>
  - [Regex 2] <code>tq.get(`/datatester/common-service/api/v3/apps/${n}/workflow-templates/metrics-filter/${l}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/list</code>

### 86. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/54562.8ee76a9d.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-user-list</code>
- Loaded on routes: 134
- Unique matches: 1
  - [Regex 2] <code>u.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${s}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-user-list</code>

### 87. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/31062.6d254733.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-manage-list</code>
- Loaded on routes: 135
- Unique matches: 1
  - [Regex 2] <code>u.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${s}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/online-announce-manage-list</code>

### 88. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/88928.499aa73b.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/scheduled-task-management</code>
- Loaded on routes: 136
- Unique matches: 2
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 3 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/scheduled-task-management</code>
  - [Regex 2] <code>j.get(`/datatester/api/v2/management/apps/${e}/cronjob/settings`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/scheduled-task-management</code>

### 89. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40287.de3b0782.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>
- Loaded on routes: 137
- Unique matches: 1
  - [Regex 2] <code>u.get(`/v2/apps/${e}/pre_tab_task/${t}/retry`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>

### 90. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>
- Loaded on routes: 137
- Unique matches: 4
  - [Regex 1] <code>location.href=h</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>
  - [Regex 1] <code>location.href=t</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>
  - [Regex 1] <code>location=h</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>
  - [Regex 1] <code>location=t</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/pre-flow</code>

### 91. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50481.c0109988.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/basic</code>
- Loaded on routes: 138
- Unique matches: 1
  - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/basic</code>

### 92. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64140.9e9ecfa7.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/editor</code>
- Loaded on routes: 139
- Unique matches: 2
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/editor</code>
  - [Regex 2] <code>l.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${t}/metrics`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/editor</code>

### 93. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13910.8de76419.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/list</code>
- Loaded on routes: 140
- Unique matches: 1
  - [Regex 2] <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/system/templates/list</code>

### 94. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59694.dc35e0c0.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/user-cohort/list</code>
- Loaded on routes: 141
- Unique matches: 1
  - [Regex 2] <code>_.get(`/datatester/api/v2/app/${t}/cohort/${a}/refresh`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/user-cohort/list</code>

### 95. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/34036.11e62fd1.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/list</code>
- Loaded on routes: 146, 148
- Unique matches: 2
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/list</code>
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/list</code>

### 96. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50476.2b42d973.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>
- Loaded on routes: 148
- Unique matches: 1
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>

### 97. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58444.2ee6a332.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>
- Loaded on routes: 148, 151
- Unique matches: 1
  - [Regex 1] <code>new URLSearchParams(window.location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>

### 98. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/brace.e9c426df.async.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>
- Loaded on routes: 148, 151, 207
- Unique matches: 2
  - [Regex 1] <code>location.replace(</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>
  - [Regex 2] <code>o.get("packaged")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/list</code>

### 99. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
- Loaded on routes: 152
- Unique matches: 7
  - [Regex 1] <code>.query.data</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
  - [Regex 1] <code>.query.isFetched</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
  - [Regex 1] <code>.query.isLoading</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
  - [Regex 1] <code>new URLSearchParams(location.search</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
  - [Regex 2] <code>ey.get(`${ex}${i}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
  - [Regex 2] <code>l.get(`/datatester/metric/api/v3/${a}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>
  - [Regex 2] <code>l.get(`/datatester/rule/api/v3/apps/${t}/rules?type=recycle,risk,release_suggestion`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/list</code>

### 100. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56722.95fe8edf.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/user-hit</code>
- Loaded on routes: 175
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/user-hit</code>

### 101. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/23200.177e5a97.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/diagnosis</code>
- Loaded on routes: 176
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/diagnosis</code>

### 102. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77901.a002a061.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/calculator</code>
- Loaded on routes: 178
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/calculator</code>

### 103. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61022.0272997e.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/vm-simulation</code>
- Loaded on routes: 179
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/vm-simulation</code>

### 104. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43704.27d5aba2.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/open/template/:id/:mode</code>
- Loaded on routes: 196
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/open/template/:id/:mode</code>

### 105. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code>
- Loaded on routes: 203
- Unique matches: 4
  - [Regex 1] <code>.query.abOpConfigId</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code>
  - [Regex 1] <code>.query.isShowConfigPane</code> - occurrences: 2 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code>
  - [Regex 2] <code>T.get(`${k}/v1/apps/${e.appId}/optimization-plans/${e.planId}/subgoals`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code>
  - [Regex 2] <code>T.get(`${k}/v1/apps/${e.appId}/optimization-plans/${e.planId}`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/list</code>

### 106. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/52295.90ceff7b.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/list</code>
- Loaded on routes: 206
- Unique matches: 1
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/list</code>

### 107. <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/87017.c29a62f1.js</code>

- First seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/create</code>
- Loaded on routes: 207
- Unique matches: 3
  - [Regex 1] <code>new URL(window.location.href</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/create</code>
  - [Regex 2] <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/create</code>
  - [Regex 2] <code>rZ.get(`/datatester/feature-flag/api/v4/apps/${t}/permission-check/user-tag`)</code> - occurrences: 1 - first seen on: <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/create</code>

## Skipped Duplicate Routes

| # | Route | Duplicate of route | Matched JS files | Unique file matches |
| ---: | --- | ---: | ---: | ---: |
| 5 | <code>https://console.byteplus.com/datatester/</code> | 4 | 18 | 66 |
| 6 | <code>https://console.byteplus.com/datatester/404</code> | 4 | 18 | 66 |
| 7 | <code>https://console.byteplus.com/datatester/ai-research/home</code> | 3 | 8 | 32 |
| 8 | <code>https://console.byteplus.com/datatester/ai-research/audience/list</code> | 3 | 8 | 32 |
| 9 | <code>https://console.byteplus.com/datatester/ai-research/daily-job</code> | 3 | 8 | 32 |
| 10 | <code>https://console.byteplus.com/datatester/ai-research/*</code> | 3 | 8 | 32 |
| 14 | <code>https://console.byteplus.com/datatester/org/:orgId/*</code> | 4 | 18 | 66 |
| 15 | <code>https://console.byteplus.com/datatester/app/:appId</code> | 4 | 18 | 66 |
| 16 | <code>https://console.byteplus.com/datatester/org/:orgId/collocation</code> | 4 | 18 | 66 |
| 17 | <code>https://console.byteplus.com/datatester/org/:orgId/collocation-config</code> | 4 | 18 | 66 |
| 18 | <code>https://console.byteplus.com/datatester/org/:orgId/org-info</code> | 4 | 18 | 66 |
| 19 | <code>https://console.byteplus.com/datatester/org/:orgId/caliber</code> | 4 | 18 | 66 |
| 20 | <code>https://console.byteplus.com/datatester/org/:orgId/app</code> | 4 | 18 | 66 |
| 21 | <code>https://console.byteplus.com/datatester/org/:orgId/project</code> | 4 | 18 | 66 |
| 22 | <code>https://console.byteplus.com/datatester/org/:orgId/config-import</code> | 4 | 18 | 66 |
| 24 | <code>https://console.byteplus.com/datatester/app/566590/experiment</code> | 1 | 14 | 60 |
| 25 | <code>https://console.byteplus.com/datatester/app/566590/audience</code> | 1 | 14 | 60 |
| 28 | <code>https://console.byteplus.com/datatester/app/566590/flight</code> | 1 | 14 | 60 |
| 29 | <code>https://console.byteplus.com/datatester/app/566590/metric</code> | 1 | 14 | 60 |
| 30 | <code>https://console.byteplus.com/datatester/app/566590/feature</code> | 1 | 14 | 60 |
| 31 | <code>https://console.byteplus.com/datatester/app/566590/system</code> | 1 | 14 | 60 |
| 33 | <code>https://console.byteplus.com/datatester/app/566590/user-cohort</code> | 1 | 14 | 60 |
| 34 | <code>https://console.byteplus.com/datatester/app/566590/metric-group</code> | 1 | 14 | 60 |
| 35 | <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle</code> | 1 | 14 | 60 |
| 38 | <code>https://console.byteplus.com/datatester/app/566590/scene/push</code> | 1 | 14 | 60 |
| 44 | <code>https://console.byteplus.com/datatester/app/566590/toolbox</code> | 1 | 14 | 60 |
| 45 | <code>https://console.byteplus.com/datatester/app/566590/open</code> | 1 | 14 | 60 |
| 46 | <code>https://console.byteplus.com/datatester/app/566590/personalization/list</code> | 1 | 14 | 60 |
| 49 | <code>https://console.byteplus.com/datatester/app/566590/personalization/coding/:campaignId/:campaignTab</code> | 1 | 14 | 60 |
| 53 | <code>https://console.byteplus.com/datatester/org/:orgId/app/list</code> | 4 | 18 | 66 |
| 54 | <code>https://console.byteplus.com/datatester/org/:orgId/app/add</code> | 4 | 18 | 66 |
| 55 | <code>https://console.byteplus.com/datatester/org/:orgId/app/continue</code> | 4 | 18 | 66 |
| 56 | <code>https://console.byteplus.com/datatester/org/:orgId/app/:appId/detail</code> | 4 | 18 | 66 |
| 57 | <code>https://console.byteplus.com/datatester/org/:orgId/app/:appId/tea</code> | 4 | 18 | 66 |
| 58 | <code>https://console.byteplus.com/datatester/org/:orgId/project/list</code> | 4 | 18 | 66 |
| 59 | <code>https://console.byteplus.com/datatester/org/:orgId/project/add</code> | 4 | 18 | 66 |
| 60 | <code>https://console.byteplus.com/datatester/org/:orgId/project/:projectId/detail</code> | 4 | 18 | 66 |
| 61 | <code>https://console.byteplus.com/datatester/org/:orgId/project/:projectId/edit</code> | 4 | 18 | 66 |
| 62 | <code>https://console.byteplus.com/datatester/org/:orgId/project/app_cert</code> | 4 | 18 | 66 |
| 63 | <code>https://console.byteplus.com/datatester/app/566590/experiment/list</code> | 4 | 18 | 66 |
| 64 | <code>https://console.byteplus.com/datatester/app/566590/experiment/mab</code> | 1 | 14 | 60 |
| 68 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:experimentId/detail</code> | 67 | 21 | 73 |
| 73 | <code>https://console.byteplus.com/datatester/app/566590/experiment/mab/:experimentId/report</code> | 72 | 21 | 73 |
| 74 | <code>https://console.byteplus.com/datatester/app/566590/audience/param-filters/list</code> | 1 | 14 | 60 |
| 75 | <code>https://console.byteplus.com/datatester/app/566590/audience/param-filters/create</code> | 1 | 14 | 60 |
| 76 | <code>https://console.byteplus.com/datatester/app/566590/audience/param-filters/detail/:paramId</code> | 1 | 14 | 60 |
| 77 | <code>https://console.byteplus.com/datatester/app/566590/audience/param-filters/edit/:paramId</code> | 1 | 14 | 60 |
| 78 | <code>https://console.byteplus.com/datatester/app/566590/audience/*</code> | 1 | 14 | 60 |
| 79 | <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan</code> | 1 | 14 | 60 |
| 80 | <code>https://console.byteplus.com/datatester/app/566590/flight/experience-list</code> | 48 | 15 | 62 |
| 83 | <code>https://console.byteplus.com/datatester/app/566590/flight/:flightId/diagnosis</code> | 1 | 14 | 60 |
| 84 | <code>https://console.byteplus.com/datatester/app/566590/flight/:draftId?/create/:step?/:mode?</code> | 1 | 14 | 60 |
| 85 | <code>https://console.byteplus.com/datatester/app/566590/flight/:draftId?/create-ad/:step?</code> | 1 | 14 | 60 |
| 86 | <code>https://console.byteplus.com/datatester/app/566590/flight/:flightId/detail</code> | 67 | 21 | 73 |
| 87 | <code>https://console.byteplus.com/datatester/app/566590/flight/:flightId/edit</code> | 67 | 21 | 73 |
| 88 | <code>https://console.byteplus.com/datatester/app/566590/flight/:flightId/bav-event/detail</code> | 27 | 0 | 0 |
| 89 | <code>https://console.byteplus.com/datatester/app/566590/flight/:flightId/report</code> | 72 | 21 | 73 |
| 90 | <code>https://console.byteplus.com/datatester/app/566590/flight/approval</code> | 1 | 14 | 60 |
| 91 | <code>https://console.byteplus.com/datatester/app/566590/flight/list/draft</code> | 4 | 18 | 66 |
| 92 | <code>https://console.byteplus.com/datatester/app/566590/flight/mab/list/draft</code> | 4 | 18 | 66 |
| 93 | <code>https://console.byteplus.com/datatester/app/566590/flight/list/:tag?</code> | 4 | 18 | 66 |
| 95 | <code>https://console.byteplus.com/datatester/app/566590/metric/receiving-group/list</code> | 1 | 14 | 60 |
| 96 | <code>https://console.byteplus.com/datatester/app/566590/metric/alarm-task/list</code> | 1 | 14 | 60 |
| 97 | <code>https://console.byteplus.com/datatester/app/566590/metric/alarm-task/create/:type?</code> | 94 | 15 | 66 |
| 98 | <code>https://console.byteplus.com/datatester/app/566590/metric/alarm-task/:taskId/edit</code> | 94 | 15 | 66 |
| 99 | <code>https://console.byteplus.com/datatester/app/566590/metric/alarm-task/:taskId/detail</code> | 94 | 15 | 66 |
| 102 | <code>https://console.byteplus.com/datatester/app/566590/feature/from/:flightId/:versionId?</code> | 101 | 18 | 70 |
| 104 | <code>https://console.byteplus.com/datatester/app/566590/feature/create</code> | 103 | 17 | 67 |
| 105 | <code>https://console.byteplus.com/datatester/app/566590/feature/:featureId/report</code> | 1 | 14 | 60 |
| 106 | <code>https://console.byteplus.com/datatester/app/566590/system/history</code> | 101 | 18 | 70 |
| 107 | <code>https://console.byteplus.com/datatester/app/566590/system/filters</code> | 1 | 14 | 60 |
| 108 | <code>https://console.byteplus.com/datatester/app/566590/system/allow-list</code> | 1 | 14 | 60 |
| 111 | <code>https://console.byteplus.com/datatester/app/566590/system/media-account</code> | 1 | 14 | 60 |
| 113 | <code>https://console.byteplus.com/datatester/app/566590/system/permission/add-role</code> | 112 | 16 | 64 |
| 114 | <code>https://console.byteplus.com/datatester/app/566590/system/permission/create</code> | 112 | 16 | 64 |
| 115 | <code>https://console.byteplus.com/datatester/app/566590/system/caliber</code> | 40 | 15 | 61 |
| 116 | <code>https://console.byteplus.com/datatester/app/566590/system/virtual-event-management</code> | 1 | 14 | 60 |
| 117 | <code>https://console.byteplus.com/datatester/app/566590/system/async-task</code> | 1 | 14 | 60 |
| 126 | <code>https://console.byteplus.com/datatester/app/566590/system/data-management/bav-event/create/web</code> | 123 | 15 | 63 |
| 127 | <code>https://console.byteplus.com/datatester/app/566590/system/data-management/bav-event/detail/:pageId</code> | 124 | 16 | 293 |
| 129 | <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/create</code> | 128 | 16 | 64 |
| 130 | <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/:workflowId/create</code> | 128 | 16 | 64 |
| 131 | <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/:workflowId/edit</code> | 128 | 16 | 64 |
| 132 | <code>https://console.byteplus.com/datatester/app/566590/system/workflow-template/:workflowId/detail</code> | 128 | 16 | 64 |
| 133 | <code>https://console.byteplus.com/datatester/app/566590/system/task-approval/list</code> | 101 | 18 | 70 |
| 142 | <code>https://console.byteplus.com/datatester/app/566590/user-cohort/create</code> | 141 | 15 | 61 |
| 143 | <code>https://console.byteplus.com/datatester/app/566590/user-cohort/:cohortId/edit</code> | 141 | 15 | 61 |
| 144 | <code>https://console.byteplus.com/datatester/app/566590/user-cohort/:cohortId/detail</code> | 141 | 15 | 61 |
| 145 | <code>https://console.byteplus.com/datatester/app/566590/user-cohort/:cohortId/copy</code> | 141 | 15 | 61 |
| 147 | <code>https://console.byteplus.com/datatester/app/566590/metric-group/type/:type/:id?</code> | 1 | 14 | 60 |
| 149 | <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/create</code> | 148 | 18 | 66 |
| 150 | <code>https://console.byteplus.com/datatester/app/566590/metric-group/global-dimension/:mode/:dimensionId</code> | 148 | 18 | 66 |
| 153 | <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/detail/:id</code> | 152 | 15 | 67 |
| 154 | <code>https://console.byteplus.com/datatester/app/566590/metric-group-bundle/edit/:id?</code> | 152 | 15 | 67 |
| 155 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/plan/:type/v2/:mode</code> | 36 | 15 | 65 |
| 156 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/plan/:adId/:channel/:mode</code> | 36 | 15 | 65 |
| 157 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/manager/:channel?/:type?</code> | 36 | 15 | 65 |
| 158 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/experiment/create</code> | 36 | 15 | 65 |
| 159 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/experiment/:experimentId/edit</code> | 36 | 15 | 65 |
| 160 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/experiment/:experimentId/:type?</code> | 36 | 15 | 65 |
| 161 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/experiment</code> | 36 | 15 | 65 |
| 162 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/assets/material/upload</code> | 36 | 15 | 65 |
| 163 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/assets/:mode?</code> | 36 | 15 | 65 |
| 164 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/accounts</code> | 36 | 15 | 65 |
| 165 | <code>https://console.byteplus.com/datatester/app/566590/scene/adlaunch/scene/adlaunch</code> | 36 | 15 | 65 |
| 166 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/list</code> | 37 | 16 | 68 |
| 167 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/:evalId/edit</code> | 37 | 16 | 68 |
| 168 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/create</code> | 37 | 16 | 68 |
| 169 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/:reportId/report</code> | 37 | 16 | 68 |
| 170 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/dataset/list</code> | 37 | 16 | 68 |
| 171 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/dataset/create</code> | 37 | 16 | 68 |
| 172 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/dataset/:datasetId/edit</code> | 37 | 16 | 68 |
| 173 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/dataset/:datasetId/detail</code> | 37 | 16 | 68 |
| 174 | <code>https://console.byteplus.com/datatester/app/566590/scene/llm/metric/list</code> | 37 | 16 | 68 |
| 177 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule</code> | 1 | 14 | 60 |
| 180 | <code>https://console.byteplus.com/datatester/app/566590/open/custom-management</code> | 1 | 14 | 60 |
| 181 | <code>https://console.byteplus.com/datatester/app/566590/open/integration-list</code> | 1 | 14 | 60 |
| 183 | <code>https://console.byteplus.com/datatester/app/566590/open/integration/:jobId/edit</code> | 182 | 15 | 64 |
| 184 | <code>https://console.byteplus.com/datatester/app/566590/open/integration/:jobId/view</code> | 182 | 15 | 64 |
| 185 | <code>https://console.byteplus.com/datatester/app/566590/open/integration/:jobId/log</code> | 1 | 14 | 60 |
| 186 | <code>https://console.byteplus.com/datatester/app/566590/open/secret-key</code> | 1 | 14 | 60 |
| 187 | <code>https://console.byteplus.com/datatester/app/566590/open/open-component-doc/:id</code> | 182 | 15 | 64 |
| 188 | <code>https://console.byteplus.com/datatester/app/566590/open/datasource-list</code> | 1 | 14 | 60 |
| 189 | <code>https://console.byteplus.com/datatester/app/566590/open/datasource/:id?</code> | 1 | 14 | 60 |
| 190 | <code>https://console.byteplus.com/datatester/app/566590/open/dataset-list</code> | 1 | 14 | 60 |
| 191 | <code>https://console.byteplus.com/datatester/app/566590/open/dataset/:id?</code> | 182 | 15 | 64 |
| 192 | <code>https://console.byteplus.com/datatester/app/566590/open/virtual-dataset/:id?</code> | 182 | 15 | 64 |
| 193 | <code>https://console.byteplus.com/datatester/app/566590/open/template/list</code> | 1 | 14 | 60 |
| 194 | <code>https://console.byteplus.com/datatester/app/566590/open/template/create</code> | 1 | 14 | 60 |
| 195 | <code>https://console.byteplus.com/datatester/app/566590/open/template/bref/:id/:mode</code> | 1 | 14 | 60 |
| 197 | <code>https://console.byteplus.com/datatester/app/566590/experiment/mab/list</code> | 4 | 18 | 66 |
| 198 | <code>https://console.byteplus.com/datatester/app/566590/experiment/mab/:experimentId/detail</code> | 67 | 21 | 73 |
| 199 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report/advanced/heatmap/click</code> | 72 | 21 | 73 |
| 200 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report/advanced/heatmap/element</code> | 72 | 21 | 73 |
| 201 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report/advanced/heatmap/browser</code> | 72 | 21 | 73 |
| 202 | <code>https://console.byteplus.com/datatester/app/566590/experiment/:flightId/report/advanced/heatmap/attention</code> | 72 | 21 | 73 |
| 204 | <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/create</code> | 203 | 16 | 70 |
| 205 | <code>https://console.byteplus.com/datatester/app/566590/flight/optimization-plan/:planId/detail</code> | 203 | 16 | 70 |
| 208 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/detail/:ruleId</code> | 207 | 21 | 80 |
| 209 | <code>https://console.byteplus.com/datatester/app/566590/toolbox/check-rule/edit/:ruleId</code> | 207 | 21 | 80 |

## Errors and Unscanned Files

No navigation, scan, or file retrieval errors were recorded.
