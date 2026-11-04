# JS Regex Scan - Short Report

- Generated: 2026-11-04 12:23:49 UTC
- Inputs: URLs <code>data/urls.txt</code> | Auth <code>data/user-A.txt</code> (2 headers, 45 cookies)
- Routes: 254 tested, 162 duplicate, 0 errors
- Files: 144 with matches | File matches: 1059 | Unique texts: 539 | R1: 278 | R2: 781 | Unscanned: 0
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP

## Routes With Unique Scan Results

| # | Route | HTTP | Files | Matches | New files | New matches | Note |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | <code>https://console.byteplus.com/datafinder/app/218463/access-analysis-mp</code> | 200 | 21 | 378 | 21 | 378 | - |
| 2 | <code>https://console.byteplus.com/datafinder/app/218463/access-analysis-mp/:report_id?/:result_id</code> | 200 | 33 | 451 | 12 | 73 | - |
| 3 | <code>https://console.byteplus.com/datafinder/app/218463/access-analysis-web</code> | 200 | 32 | 443 | 1 | 8 | - |
| 4 | <code>https://console.byteplus.com/datafinder/app/218463/access-analysis-web/:report_id?/:result_id</code> | 200 | 35 | 454 | 3 | 11 | - |
| 5 | <code>https://console.byteplus.com/datafinder/app/218463/ai_landing_page</code> | 200 | 34 | 453 | 0 | 0 | - |
| 19 | <code>https://console.byteplus.com/datafinder/app/218463/channel-analysis</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 29 | <code>https://console.byteplus.com/datafinder/app/218463/dashboard-editor</code> | 200 | 34 | 452 | 1 | 8 | - |
| 30 | <code>https://console.byteplus.com/datafinder/app/218463/dashboard-editor/:dashboard_id</code> | 200 | 38 | 451 | 5 | 7 | - |
| 31 | <code>https://console.byteplus.com/datafinder/app/218463/dashboard/:dashboard_id</code> | 200 | 36 | 455 | 1 | 1 | final URL: https://console.byteplus.com/datafinder/app/218463/dashboard/0 |
| 34 | <code>https://console.byteplus.com/datafinder/app/218463/data-manage/analysis-items</code> | 200 | 36 | 462 | 1 | 8 | - |
| 52 | <code>https://console.byteplus.com/datafinder/app/218463/data-manage/public-params</code> | 200 | 36 | 462 | 1 | 8 | - |
| 55 | <code>https://console.byteplus.com/datafinder/app/218463/data-manage/virtual-event</code> | 200 | 36 | 462 | 1 | 8 | - |
| 73 | <code>https://console.byteplus.com/datafinder/app/218463/datagator/media-authorization</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 77 | <code>https://console.byteplus.com/datafinder/app/218463/datagator/sync-task/edit</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 80 | <code>https://console.byteplus.com/datafinder/app/218463/detective/:tenantId?/:taskId?/:user_id?/:stage</code> | 200 | 35 | 456 | 1 | 3 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 81 | <code>https://console.byteplus.com/datafinder/app/218463/diagnostic/:tenantId?/:taskId?/:stage</code> | 200 | 35 | 454 | 1 | 1 | - |
| 84 | <code>https://console.byteplus.com/datafinder/app/218463/douyin-analysis</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 91 | <code>https://console.byteplus.com/datafinder/app/218463/editor</code> | 200 | 34 | 452 | 1 | 8 | - |
| 92 | <code>https://console.byteplus.com/datafinder/app/218463/embed-analysis-result</code> | 200 | 41 | 462 | 5 | 20 | - |
| 93 | <code>https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail</code> | 200 | 35 | 454 | 2 | 9 | - |
| 94 | <code>https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail/detail</code> | 200 | 40 | 469 | 6 | 23 | final URL: https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail/detail?query_id=&amp;query_type=user_unique_id&amp;appId=&amp;activeEventId=&amp;curDevice=pc&amp;curDevice=mobile&amp;curDevice=mp&amp;isShowFiltered=true&amp;eventParamsType=list&amp;timestamp=1791244800000&amp;timestamp=1793792996280&amp;resolvedQueryId=&amp;resolvedQueryType=&amp;selectedTemplateId=&amp;eventCategory=event&amp;flowType=event&amp;eventOperation=in&amp;subjectId=&amp;eventFilterList=%5B%5D&amp;snapshot_id=&amp;sort=desc&amp;searchQuestion= |
| 95 | <code>https://console.byteplus.com/datafinder/app/218463/embed-dashboard</code> | 200 | 42 | 463 | 1 | 1 | - |
| 96 | <code>https://console.byteplus.com/datafinder/app/218463/embed-dashboard-editor</code> | 200 | 33 | 444 | 1 | 8 | - |
| 97 | <code>https://console.byteplus.com/datafinder/app/218463/embed-dashboard-editor/:dashboard_id</code> | 200 | 41 | 461 | 0 | 0 | - |
| 98 | <code>https://console.byteplus.com/datafinder/app/218463/embed-des-registration-management</code> | 200 | 33 | 444 | 2 | 9 | - |
| 99 | <code>https://console.byteplus.com/datafinder/app/218463/embed-event-analysis/:report_id?/:result_id</code> | 200 | 43 | 467 | 5 | 13 | - |
| 100 | <code>https://console.byteplus.com/datafinder/app/218463/embed-funnel-analysis/:report_id?/:result_id</code> | 200 | 44 | 471 | 1 | 4 | - |
| 101 | <code>https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard</code> | 200 | 36 | 442 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard/7000732696393548289 |
| 102 | <code>https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard/:dashboard_id</code> | 200 | 43 | 464 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard/0 |
| 103 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission</code> | 200 | 33 | 444 | 1 | 8 | - |
| 104 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission/department</code> | 200 | 33 | 444 | 1 | 8 | - |
| 105 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission/roles</code> | 200 | 33 | 444 | 1 | 8 | - |
| 106 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission/roles/detail</code> | 200 | 33 | 444 | 1 | 8 | - |
| 108 | <code>https://console.byteplus.com/datafinder/app/218463/embed-report/no-access</code> | 200 | 32 | 443 | 1 | 8 | - |
| 110 | <code>https://console.byteplus.com/datafinder/app/218463/embed-session-replay-list</code> | 200 | 35 | 455 | 2 | 13 | final URL: https://console.byteplus.com/datafinder/app/218463/embed-session-replay-list?filter_id=377994 |
| 111 | <code>https://console.byteplus.com/datafinder/app/218463/embed-session-replay-player/:recording_id</code> | 200 | 41 | 465 | 0 | 0 | - |
| 112 | <code>https://console.byteplus.com/datafinder/app/218463/embed-user-cohort/edit-cohort/:type/:id</code> | 200 | 35 | 451 | 3 | 11 | final URL: https://console.byteplus.com/datafinder/app/218463/user-cohort |
| 113 | <code>https://console.byteplus.com/datafinder/app/218463/embed-virtual-event-edit</code> | 200 | 38 | 451 | 2 | 10 | - |
| 118 | <code>https://console.byteplus.com/datafinder/app/218463/funnel-analysis</code> | 200 | 36 | 462 | 1 | 8 | - |
| 121 | <code>https://console.byteplus.com/datafinder/app/218463/industry-analysis</code> | 200 | 36 | 457 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 125 | <code>https://console.byteplus.com/datafinder/app/218463/items-analysis/:report_id?/:result_id</code> | 200 | 36 | 462 | 1 | 8 | - |
| 126 | <code>https://console.byteplus.com/datafinder/app/218463/journey-diagnostics/:tenantId?/:taskId</code> | 200 | 35 | 454 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/journey-diagnostics |
| 129 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 132 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/dashboard/:spaceId?/:taskId?/:subTaskId?/:leafTaskId</code> | 200 | 32 | 439 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/dashboard/:spaceId?%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId= |
| 133 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/journeys/:spaceId?/:taskId?/:subTaskId?/:leafTaskId</code> | 200 | 34 | 443 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/journeys/:spaceId?%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId= |
| 134 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/trace/:spaceId?/:taskId?/:subTaskId?/:leafTaskId</code> | 200 | 36 | 450 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/trace/:spaceId?%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId= |
| 135 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/:pageType?/:spaceId?/:taskId?/:subTaskId?/:leafTaskId</code> | 200 | 35 | 493 | 1 | 44 | - |
| 136 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/cozeloop/:spaceId/:module/:subModule/result/:result</code> | 200 | 36 | 454 | 1 | 2 | - |
| 137 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/cozeloop/:spaceId?/:module?/:subModule?/:leafModule</code> | 200 | 39 | 471 | 2 | 16 | - |
| 138 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/share/session/:token</code> | 200 | 34 | 446 | 0 | 0 | - |
| 139 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/share/trace/:token</code> | 200 | 36 | 452 | 2 | 6 | - |
| 141 | <code>https://console.byteplus.com/datafinder/app/218463/ltv-analysis/:report_id?/:result_id</code> | 200 | 22 | 379 | 1 | 1 | - |
| 142 | <code>https://console.byteplus.com/datafinder/app/218463/manage</code> | 200 | 33 | 444 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 145 | <code>https://console.byteplus.com/datafinder/app/218463/manage/audit-log</code> | 200 | 13 | 300 | 0 | 0 | - |
| 147 | <code>https://console.byteplus.com/datafinder/app/218463/manage/common-settings</code> | 200 | 36 | 462 | 1 | 8 | - |
| 148 | <code>https://console.byteplus.com/datafinder/app/218463/manage/dashboard-manage</code> | 200 | 38 | 458 | 0 | 0 | - |
| 151 | <code>https://console.byteplus.com/datafinder/app/218463/manage/monitor/:monitorId</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 154 | <code>https://console.byteplus.com/datafinder/app/218463/manage/session-replay-settings</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 157 | <code>https://console.byteplus.com/datafinder/app/218463/metric-system</code> | 200 | 36 | 462 | 1 | 8 | - |
| 159 | <code>https://console.byteplus.com/datafinder/app/218463/metric-system/edit/:edit_id</code> | 200 | 36 | 462 | 1 | 8 | - |
| 161 | <code>https://console.byteplus.com/datafinder/app/218463/op/app</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/app/218463/overview |
| 163 | <code>https://console.byteplus.com/datafinder/app/218463/overview</code> | 200 | 36 | 462 | 1 | 8 | - |
| 182 | <code>https://console.byteplus.com/datafinder/app/218463/render/analysis/result</code> | 200 | 41 | 462 | 2 | 4 | - |
| 193 | <code>https://console.byteplus.com/datafinder/app/218463/scenarios/editor</code> | 200 | 34 | 447 | 0 | 0 | final URL: https://console.byteplus.com/datafinder/app/218463/scenarios |
| 197 | <code>https://console.byteplus.com/datafinder/app/218463/session-replay/agent</code> | 200 | 34 | 452 | 0 | 0 | - |
| 201 | <code>https://console.byteplus.com/datafinder/app/218463/session-replay/recording/:recording_id</code> | 200 | 36 | 455 | 1 | 1 | - |
| 202 | <code>https://console.byteplus.com/datafinder/app/218463/session-replay/recording/report/:report_id</code> | 200 | 37 | 463 | 0 | 0 | - |
| 222 | <code>https://console.byteplus.com/datafinder/app/218463/user-cohort</code> | 200 | 37 | 464 | 1 | 8 | - |
| 224 | <code>https://console.byteplus.com/datafinder/app/218463/user-cohort/history/:id</code> | 200 | 36 | 456 | 0 | 0 | - |
| 229 | <code>https://console.byteplus.com/datafinder/ai-sparring</code> | 200 | 32 | 443 | 1 | 8 | - |
| 230 | <code>https://console.byteplus.com/datafinder/ai-sparring-management</code> | 200 | 32 | 443 | 1 | 8 | - |
| 231 | <code>https://console.byteplus.com/datafinder/ai_landing_page</code> | 200 | 22 | 386 | 1 | 8 | - |
| 232 | <code>https://console.byteplus.com/datafinder/bridge</code> | 200 | 34 | 453 | 1 | 8 | - |
| 233 | <code>https://console.byteplus.com/datafinder/lark-verify</code> | 200 | 22 | 386 | 1 | 8 | - |
| 234 | <code>https://console.byteplus.com/datafinder/llm-workbench/operations-agent/:pageType?/:spaceId?/:taskId?/:subTaskId?/:leafTaskId</code> | 200 | 54 | 538 | 11 | 23 | final URL: https://console.byteplus.com/datafinder/project/null/llm-workbench/operations-agent/landing?%2F%3AspaceId%3F%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId= |
| 235 | <code>https://console.byteplus.com/datafinder/llm-workbench/operations-agent/admin-open</code> | 200 | 34 | 453 | 1 | 8 | - |
| 236 | <code>https://console.byteplus.com/datafinder/llm-workbench/operations-agent/share/session/:token</code> | 200 | 39 | 464 | 2 | 10 | - |
| 237 | <code>https://console.byteplus.com/datafinder/llm-workbench/operations-agent/share/trace/:token</code> | 200 | 37 | 455 | 1 | 3 | - |
| 238 | <code>https://console.byteplus.com/datafinder/no-access</code> | 200 | 34 | 453 | 1 | 8 | - |
| 239 | <code>https://console.byteplus.com/datafinder/not-found</code> | 200 | 34 | 453 | 1 | 8 | - |
| 240 | <code>https://console.byteplus.com/datafinder/org</code> | 200 | 36 | 455 | 1 | 1 | final URL: https://console.byteplus.com/datafinder/org/84/products |
| 241 | <code>https://console.byteplus.com/datafinder/org/:ordId/embed-function-overview</code> | 200 | 42 | 463 | 0 | 0 | - |
| 242 | <code>https://console.byteplus.com/datafinder/org/:orgId/collocation</code> | 200 | 35 | 461 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/no-access?region=cn-beijing |
| 243 | <code>https://console.byteplus.com/datafinder/org/:orgId/project/new</code> | 200 | 35 | 461 | 1 | 8 | - |
| 244 | <code>https://console.byteplus.com/datafinder/org/:orgId/welcome</code> | 200 | 36 | 462 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/org/welcome |
| 245 | <code>https://console.byteplus.com/datafinder/org/:orgId?/collocation</code> | 200 | 35 | 461 | 1 | 8 | - |
| 247 | <code>https://console.byteplus.com/datafinder/org/:orgId?/overview</code> | 200 | 35 | 461 | 1 | 8 | - |
| 248 | <code>https://console.byteplus.com/datafinder/org/:orgId?/products</code> | 200 | 35 | 461 | 1 | 8 | - |
| 249 | <code>https://console.byteplus.com/datafinder/org/:orgId?/project</code> | 200 | 35 | 461 | 1 | 8 | - |
| 250 | <code>https://console.byteplus.com/datafinder/org/:orgId?/upgrade</code> | 200 | 35 | 461 | 1 | 8 | - |
| 252 | <code>https://console.byteplus.com/datafinder/overdue</code> | 200 | 35 | 454 | 2 | 9 | - |
| 253 | <code>https://console.byteplus.com/datafinder/products/:orgId</code> | 200 | 37 | 463 | 1 | 8 | final URL: https://console.byteplus.com/datafinder/org/84/products |

## Unique Matched Files

Each file lists its matches once. `R1`/`R2` are the regex labels; `xN` is the occurrence count when greater than one. `first` is the first-seen route number and `routes` is the compressed loaded-on route list; both map to the table above.

<details><summary><b>1.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/echarts.min-4.7.0.js</code> - <b>233</b> matches (R1 0 / R2 233) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R2: <code>L.get("avoidLabelOverlap")</code>
- R2: <code>L.get("minShowLabelAngle")</code>
- R2: <code>T.get("smooth")</code>
- R2: <code>_.get("show")</code>
- R2: <code>a.get("description")</code> (x2)
- R2: <code>a.get("formatter")</code>
- R2: <code>a.get("icon")</code>
- R2: <code>a.get("inside")</code> (x2)
- R2: <code>a.get("realtime")</code>
- R2: <code>a.get("show")</code> (x2)
- R2: <code>a.get("throttle")</code>
- R2: <code>c.get("axisLine.lineStyle.color")</code>
- R2: <code>c.get("barBorderRadius")</code>
- R2: <code>e.get("alignWithLabel")</code>
- R2: <code>e.get("animation")</code> (x3)
- R2: <code>e.get("axisExpandCenter")</code>
- R2: <code>e.get("axisExpandCount")</code>
- R2: <code>e.get("axisExpandDebounce")</code>
- R2: <code>e.get("axisExpandWidth")</code>
- R2: <code>e.get("axisLabel.inside")</code>
- R2: <code>e.get("axisLabel.show")</code>
- R2: <code>e.get("axisLine.lineStyle.color")</code> (x3)
- R2: <code>e.get("axisTick.inside")</code>
- R2: <code>e.get("backgroundColor")</code>
- R2: <code>e.get("borderColor")</code>
- R2: <code>e.get("borderRadius")</code>
- R2: <code>e.get("borderWidth")</code>
- R2: <code>e.get("cursor")</code>
- R2: <code>e.get("draggable")</code>
- R2: <code>e.get("focusNodeAdjacency")</code>
- R2: <code>e.get("hoverAnimation")</code>
- R2: <code>e.get("itemGap")</code>
- R2: <code>e.get("itemStyle.color")</code> (x2)
- R2: <code>e.get("label.show")</code>
- R2: <code>e.get("maxInterval")</code>
- R2: <code>e.get("minInterval")</code>
- R2: <code>e.get("orient")</code>
- R2: <code>e.get("parallelIndex")</code>
- R2: <code>e.get("rotate")</code>
- R2: <code>e.get("show")</code> (x4)
- R2: <code>e.get("showDetail")</code>
- R2: <code>e.get("symbolOffset")</code>
- R2: <code>e.get("symbolRotate")</code>
- R2: <code>e.get("triggerEvent")</code>
- R2: <code>e.hostModel.get("percentPrecision")</code>
- R2: <code>f.get("axisPointer.axis")</code>
- R2: <code>f.get("itemGap")</code>
- R2: <code>f.get("itemSize")</code>
- R2: <code>f.get("rotate")</code>
- R2: <code>f.get("show")</code>
- R2: <code>g.get("dataBackgroundColor")</code>
- R2: <code>g.get("show")</code>
- R2: <code>h.get("axisLabel.show")</code>
- R2: <code>h.get("axisLine.lineStyle.color")</code>
- R2: <code>h.get("itemSize")</code>
- R2: <code>h.get("show")</code>
- R2: <code>h.get("showTitle")</code>
- R2: <code>i.get("axisExpandTriggerOn")</code>
- R2: <code>i.get("axisExpandable")</code>
- R2: <code>i.get("backgroundColor")</code>
- R2: <code>i.get("borderRadius")</code>
- R2: <code>i.get("connectedBackgroundColor")</code>
- R2: <code>i.get("emphasis.label.position")</code>
- R2: <code>i.get("excludeComponents")</code>
- R2: <code>i.get("focusNodeAdjacency")</code> (x2)
- R2: <code>i.get("friction")</code>
- R2: <code>i.get("gravity")</code>
- R2: <code>i.get("hoverAnimation")</code>
- R2: <code>i.get("label.formatter")</code>
- R2: <code>i.get("label.precision")</code>
- R2: <code>i.get("markLine")</code> (x2)
- R2: <code>i.get("markPoint")</code> (x2)
- R2: <code>i.get("pixelRatio")</code>
- R2: <code>i.get("seriesDataIndices")</code>
- R2: <code>i.get("show")</code>
- R2: <code>i.get("showContent")</code>
- R2: <code>i.get("silent")</code>
- R2: <code>i.get("stack")</code> (x2)
- R2: <code>i.get("symbolRepeatDirection")</code>
- R2: <code>i.get("symbolRotate")</code>
- R2: <code>i.get("textStyle.color")</code>
- R2: <code>i.get("tooltip")</code>
- R2: <code>i.get("value")</code>
- R2: <code>i.get("z")</code>
- R2: <code>i.get("zoomLock")</code>
- R2: <code>l.get("borderColor")</code>
- R2: <code>l.get("dataBackgroundColor")</code>
- R2: <code>l.get("ellipsis")</code>
- R2: <code>l.get("fillerColor")</code>
- R2: <code>l.get("handleIcon")</code>
- R2: <code>l.get("handleSize")</code>
- R2: <code>l.get("r")</code>
- R2: <code>l.get("r0")</code>
- R2: <code>m.get("formatter")</code>
- R2: <code>m.get("show")</code>
- R2: <code>n.get("boundaryGap")</code>
- R2: <code>n.get("buttonColor")</code>
- R2: <code>n.get("buttonTextColor")</code>
- R2: <code>n.get("edgeForkPosition")</code>
- R2: <code>n.get("edgeShape")</code>
- R2: <code>n.get("expandAndCollapse")</code>
- R2: <code>n.get("hoverAnimation")</code>
- R2: <code>n.get("inverse")</code>
- R2: <code>n.get("itemStyle.color")</code>
- R2: <code>n.get("lineStyle.curveness")</code> (x2)
- R2: <code>n.get("lineStyle.show")</code>
- R2: <code>n.get("max")</code>
- R2: <code>n.get("min")</code>
- R2: <code>n.get("option.bar")</code>
- R2: <code>n.get("option.line")</code>
- R2: <code>n.get("option.stack")</code>
- R2: <code>n.get("pointer.show")</code>
- R2: <code>n.get("polyline")</code>
- R2: <code>n.get("readOnly")</code>
- R2: <code>n.get("roam")</code>
- R2: <code>n.get("show")</code> (x3)
- R2: <code>n.get("symbolOffset")</code>
- R2: <code>n.get("symbolRotate")</code>
- R2: <code>n.get("symbolSize")</code>
- R2: <code>n.get("title")</code>
- R2: <code>n.get("triggerOn")</code>
- R2: <code>o.get("circular.rotateLabel")</code>
- R2: <code>o.get("emptyItemWidth")</code>
- R2: <code>o.get("formatterParams")</code>
- R2: <code>o.get("icon")</code>
- R2: <code>o.get("ignoreForceLayout")</code>
- R2: <code>o.get("lineStyle.curveness")</code>
- R2: <code>o.get("rippleEffect.period")</code>
- R2: <code>o.get("roam")</code> (x2)
- R2: <code>o.get("selectedMode")</code>
- R2: <code>o.get("show")</code> (x4)
- R2: <code>o.get("silent")</code>
- R2: <code>p.get("show")</code>
- R2: <code>r.get("animation")</code>
- R2: <code>r.get("borderColor")</code>
- R2: <code>r.get("borderRadius")</code>
- R2: <code>r.get("borderWidth")</code>
- R2: <code>r.get("hoverOffset")</code>
- R2: <code>r.get("itemGap")</code>
- R2: <code>r.get("orient")</code>
- R2: <code>r.get("selectedOffset")</code>
- R2: <code>r.get("shadowBlur")</code>
- R2: <code>r.get("shadowColor")</code>
- R2: <code>r.get("shadowOffsetX")</code>
- R2: <code>r.get("shadowOffsetY")</code>
- R2: <code>r.get("show")</code>
- R2: <code>s.get("label.formatter")</code>
- R2: <code>s.get("label.precision")</code>
- R2: <code>s.get("show")</code>
- R2: <code>s.get("textAlign")</code>
- R2: <code>s.get("textBackgroundColor")</code>
- R2: <code>s.get("textBorderRadius")</code>
- R2: <code>s.get("textFill")</code>
- R2: <code>s.get("textPadding")</code>
- R2: <code>s.get("textPosition")</code>
- R2: <code>s.get("verticalAlign")</code>
- R2: <code>t.ecModel.get("useUTC")</code>
- R2: <code>t.get("axisExpandRate")</code>
- R2: <code>t.get("axisLabel.inside")</code>
- R2: <code>t.get("axisLine.lineStyle.color")</code> (x2)
- R2: <code>t.get("axisLine.show")</code>
- R2: <code>t.get("axisTick.inside")</code>
- R2: <code>t.get("backgroundColor")</code> (x3)
- R2: <code>t.get("barMaxWidth")</code> (x3)
- R2: <code>t.get("barMinWidth")</code> (x2)
- R2: <code>t.get("barWidth")</code> (x2)
- R2: <code>t.get("borderRadius")</code>
- R2: <code>t.get("boundaryGap")</code> (x2)
- R2: <code>t.get("calendarIndex")</code>
- R2: <code>t.get("center")</code> (x3)
- R2: <code>t.get("confine")</code>
- R2: <code>t.get("connectNulls")</code> (x2)
- R2: <code>t.get("containLabel")</code>
- R2: <code>t.get("coordinateSystem")</code>
- R2: <code>t.get("delay")</code>
- R2: <code>t.get("dim")</code>
- R2: <code>t.get("edgeSymbol")</code>
- R2: <code>t.get("edgeSymbolSize")</code>
- R2: <code>t.get("endAngle")</code>
- R2: <code>t.get("enterable")</code>
- R2: <code>t.get("extraCssText")</code>
- R2: <code>t.get("geoCoord")</code>
- R2: <code>t.get("gradientColor")</code>
- R2: <code>t.get("inverse")</code>
- R2: <code>t.get("itemGap")</code> (x3)
- R2: <code>t.get("label.align")</code>
- R2: <code>t.get("label.baseline")</code>
- R2: <code>t.get("label.verticalAlign")</code>
- R2: <code>t.get("layoutIterations")</code>
- R2: <code>t.get("legendHoverLink")</code>
- R2: <code>t.get("max")</code> (x3)
- R2: <code>t.get("maxSize")</code>
- R2: <code>t.get("min")</code> (x3)
- R2: <code>t.get("minSize")</code>
- R2: <code>t.get("nameMap")</code> (x2)
- R2: <code>t.get("nodeAlign")</code>
- R2: <code>t.get("orient")</code> (x3)
- R2: <code>t.get("parallelId")</code>
- R2: <code>t.get("parallelIndex")</code> (x4)
- R2: <code>t.get("period")</code>
- R2: <code>t.get("polarId")</code>
- R2: <code>t.get("polarIndex")</code>
- R2: <code>t.get("radarIndex")</code> (x2)
- R2: <code>t.get("radius")</code>
- R2: <code>t.get("realtime")</code>
- R2: <code>t.get("scaleLimit")</code> (x2)
- R2: <code>t.get("show")</code> (x4)
- R2: <code>t.get("showLegendSymbol")</code> (x2)
- R2: <code>t.get("silent")</code> (x3)
- R2: <code>t.get("singleAxisId")</code>
- R2: <code>t.get("singleAxisIndex")</code>
- R2: <code>t.get("smooth")</code>
- R2: <code>t.get("smoothMonotone")</code> (x2)
- R2: <code>t.get("stack")</code> (x2)
- R2: <code>t.get("startAngle")</code> (x3)
- R2: <code>t.get("step")</code>
- R2: <code>t.get("subtarget")</code>
- R2: <code>t.get("symbol")</code> (x2)
- R2: <code>t.get("symbolMargin")</code>
- R2: <code>t.get("symbolSize")</code>
- R2: <code>t.get("target")</code>
- R2: <code>t.get("text")</code>
- R2: <code>t.get("textBaseline")</code>
- R2: <code>t.get("textVerticalAlign")</code>
- R2: <code>t.get("title.0.text")</code>
- R2: <code>t.get("triggerEvent")</code>
- R2: <code>t.get("visualDimension")</code>
- R2: <code>t.get("z")</code> (x3)
- R2: <code>t.get("zlevel")</code>
- R2: <code>t.get("zoom")</code> (x3)
- R2: <code>u.get("renderMode")</code>
- R2: <code>v.get("show")</code>
- R2: <code>w.get("animation")</code>

</details>

<details><summary><b>2.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/instant-finder-ef959ef1.js</code> - <b>59</b> matches (R1 1 / R2 58) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)
- R2: <code>a.get("formatter")</code>
- R2: <code>a.get("rotate")</code> (x2)
- R2: <code>c.get("boundaryGap")</code>
- R2: <code>c.get("formatter")</code>
- R2: <code>c.get("show")</code>
- R2: <code>d.get("alignTicks")</code>
- R2: <code>d.get("formatterParams")</code>
- R2: <code>d.get("interval")</code>
- R2: <code>e.get("animation")</code>
- R2: <code>e.get("backgroundColor")</code>
- R2: <code>e.get("blurScope")</code>
- R2: <code>e.get("borderColor")</code>
- R2: <code>e.get("borderWidth")</code>
- R2: <code>e.get("disabled")</code>
- R2: <code>e.get("enterable")</code> (x2)
- R2: <code>e.get("focus")</code>
- R2: <code>e.get("instant_finder")</code> (x2)
- R2: <code>e.get("maxInterval")</code>
- R2: <code>e.get("minInterval")</code>
- R2: <code>e.get("scale")</code>
- R2: <code>e.get("seriesDataIndices")</code>
- R2: <code>e.get("show")</code>
- R2: <code>e.get("smooth")</code>
- R2: <code>e.get("step")</code>
- R2: <code>e.get("transitionDuration")</code>
- R2: <code>e.get("triggerLineEvent")</code>
- R2: <code>i.get("barMaxWidth")</code>
- R2: <code>i.get("barMinWidth")</code>
- R2: <code>i.get("barWidth")</code>
- R2: <code>i.get("z")</code>
- R2: <code>n.ecModel.get("useUTC")</code>
- R2: <code>n.get("coordinateSystem")</code>
- R2: <code>n.get("debug")</code> (x2)
- R2: <code>n.get("lineHeight")</code>
- R2: <code>n.get("parallelIndex")</code>
- R2: <code>n.get("renderMode")</code>
- R2: <code>n.get("stack")</code> (x2)
- R2: <code>n.get("symbolKeepAspect")</code>
- R2: <code>n.get("verticalAlign")</code>
- R2: <code>o.get("icon")</code>
- R2: <code>o.get("throttle")</code>
- R2: <code>o.get("triggerOn")</code>
- R2: <code>o.get("useUTC")</code>
- R2: <code>p.get("delay")</code>
- R2: <code>p.get("easing")</code>
- R2: <code>r.get("renderMode")</code>
- R2: <code>r.get("useUTC")</code>
- R2: <code>s.get("textShadowColor")</code>
- R2: <code>s.get("textStyle")</code>
- R2: <code>s.get("verticalAlign")</code>
- R2: <code>t.get("containLabel")</code>
- R2: <code>t.get("cursor")</code>
- R2: <code>t.get("extraCssText")</code>
- R2: <code>t.get("rotate")</code>
- R2: <code>t.get("silent")</code>
- R2: <code>t.get("triggerEvent")</code> (x2)
- R2: <code>v.get("textStyle")</code>
- R2: <code>z.get("smooth")</code>

</details>

<details><summary><b>3.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_ai_checker_entry_tsx~src_uba-pages_ai_checker_components_TrajectoryAnalysis_tra~c6b547-ef959ef1.js</code> - <b>44</b> matches (R1 27 / R2 17) - first 135 - routes: 135, 234</summary>

- R1: <code>.query.keyword</code>
- R1: <code>.query.kind</code>
- R1: <code>.query.length</code>
- R1: <code>.query.maintainer</code>
- R1: <code>.query.page</code>
- R1: <code>.query.page_size</code>
- R1: <code>.query.params</code> (x2)
- R1: <code>.query.period</code>
- R1: <code>.query.slice</code>
- R1: <code>.query.status</code>
- R1: <code>.query.trim</code> (x2)
- R1: <code>location.href=A</code> (x2)
- R1: <code>location.href=C</code>
- R1: <code>location.href=G</code>
- R1: <code>location.href=I</code>
- R1: <code>location.href=M</code>
- R1: <code>location.href=V</code>
- R1: <code>location.href=Z</code>
- R1: <code>location.href=a</code> (x2)
- R1: <code>location.href=c</code>
- R1: <code>location.href=r</code>
- R1: <code>location.href=v</code>
- R1: <code>location.href=y</code> (x3)
- R1: <code>new URL(window.location.href</code> (x14)
- R1: <code>new URLSearchParams(location.search</code>
- R1: <code>new URLSearchParams(window.location.search</code> (x30)
- R1: <code>window.location.assign(</code>
- R2: <code>A.get("offline_instance_id")</code>
- R2: <code>A.get("task_version")</code>
- R2: <code>L.get("agentIds")</code>
- R2: <code>L.get("endDate")</code>
- R2: <code>L.get("startDate")</code>
- R2: <code>L.get("weekendOption")</code>
- R2: <code>M.get("filters")</code>
- R2: <code>M.get("issue_id")</code>
- R2: <code>M.get("view_id")</code>
- R2: <code>P.get("action")</code>
- R2: <code>ee.get("projectId")</code>
- R2: <code>ie.get("projectId")</code>
- R2: <code>input.get("messages")</code>
- R2: <code>m.get("role")</code> (x2)
- R2: <code>output.get("final")</code>
- R2: <code>output.get("text")</code>
- R2: <code>span.get("output")</code>

</details>

<details><summary><b>4.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytecloud_common-lib_6_13_0_node_modules_bytecloud_common-lib_es_jw~1f7822-ef959ef1.js</code> - <b>24</b> matches (R1 10 / R2 14) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.assign(</code>
- R1: <code>location.href=V</code> (x3)
- R1: <code>location.href=`</code> (x2)
- R1: <code>location.href=c</code>
- R1: <code>location.href=g</code>
- R1: <code>location.href=h</code>
- R1: <code>location.href=y</code>
- R1: <code>location=n</code>
- R1: <code>new URL(location.href</code> (x3)
- R1: <code>window.location.replace(</code> (x3)
- R2: <code>D.configManager.get("reportErrorCallback")</code>
- R2: <code>D.configManager.get("user")</code> (x6)
- R2: <code>I.configManager.get("reportErrorCallback")</code>
- R2: <code>ee.configManager.get("user")</code> (x6)
- R2: <code>h.get("csrfToken")</code>
- R2: <code>r.collect.configManager.get("user")</code> (x2)
- R2: <code>r.configManager.get("browser")</code>
- R2: <code>r.configManager.get("user_unique_id")</code> (x3)
- R2: <code>r.configManager.get("user_unique_id_type")</code>
- R2: <code>r.configManager.get("web_id")</code> (x3)
- R2: <code>v.collect.configManager.get("custom")</code>
- R2: <code>v.configManager.get("user_unique_id")</code> (x3)
- R2: <code>v.configManager.get("user_unique_id_type")</code>
- R2: <code>v.configManager.get("web_id")</code> (x3)

</details>

<details><summary><b>5.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_byted_btm-web-sdk_0_2_17_node_modules_byted_btm-web-sdk_dist_src_bt~dc3136-ef959ef1.js</code> - <b>22</b> matches (R1 3 / R2 19) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location.href=M</code>
- R1: <code>location=f</code>
- R1: <code>window.location.replace(</code>
- R2: <code>E.styles.get("heatmap_popper_arrow")</code>
- R2: <code>E.styles.get("heatmap_tooltip")</code>
- R2: <code>E.styles.get("heatmap_tooltip_container")</code>
- R2: <code>o.styles.get("heatmap_block_name")</code>
- R2: <code>o.styles.get("heatmap_inner_block")</code>
- R2: <code>o.styles.get("heatmap_inner_container")</code>
- R2: <code>o.styles.get("heatmap_inner_data")</code>
- R2: <code>o.styles.get("heatmap_inner_name")</code>
- R2: <code>y.styles.get("heatmap_button")</code>
- R2: <code>y.styles.get("heatmap_button_img")</code>
- R2: <code>y.styles.get("heatmap_button_text")</code> (x2)
- R2: <code>y.styles.get("heatmap_canvas")</code>
- R2: <code>y.styles.get("heatmap_color_bar")</code>
- R2: <code>y.styles.get("heatmap_divider")</code>
- R2: <code>y.styles.get("heatmap_divider_bottom")</code>
- R2: <code>y.styles.get("heatmap_handle_area")</code>
- R2: <code>y.styles.get("heatmap_handle_dot")</code>
- R2: <code>y.styles.get("heatmap_rect")</code>
- R2: <code>y.styles.get("heatmap_toolbar_container")</code>

</details>

<details><summary><b>6.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/indoc-sdk-ef959ef1.js</code> - <b>16</b> matches (R1 4 / R2 12) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location.href=h</code>
- R1: <code>location=!</code>
- R1: <code>location=e</code> (x6)
- R1: <code>location=n</code>
- R2: <code>Mn.get("_TEA_VE_APIHOST")</code>
- R2: <code>Mn.get("_TEA_VE_OPEN")</code>
- R2: <code>Mn.get("_VISUAL_EDITOR_U")</code>
- R2: <code>Mn.get("_VISUAL_EDITOR_V")</code>
- R2: <code>Mn.get("lang")</code>
- R2: <code>e.collect.configManager.get("custom")</code>
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>i.configManager.get("reportErrorCallback")</code>
- R2: <code>i.configManager.get("user")</code> (x6)
- R2: <code>n.get("defaultKeyword")</code>

</details>

<details><summary><b>7.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~data_font_truetype_charset_utf-8_base64_AAEAAAASAQAABAAgRkZUTYh7ieMAAB6kAAAAHEdERUYAJwAkAAAd~7223cb-ef959ef1.js</code> - <b>13</b> matches (R1 7 / R2 6) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=A</code>
- R1: <code>location.href=L</code>
- R1: <code>location.href=O</code>
- R1: <code>location.href=Q</code>
- R1: <code>new URLSearchParams(location.search</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code> (x4)
- R1: <code>window.location.replace(</code>
- R2: <code>e.default.get("/v1/micro_fe")</code>
- R2: <code>g.get("crh")</code>
- R2: <code>u.searchParams.get("event_name")</code>
- R2: <code>u.searchParams.get("options")</code>
- R2: <code>u.searchParams.get("with_dashboard_operation")</code>
- R2: <code>u.searchParams.get("with_events")</code>

</details>

<details><summary><b>8.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code> - <b>11</b> matches (R1 4 / R2 7) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=i</code>
- R1: <code>location.href=p</code>
- R1: <code>new URL(window.location.href</code> (x2)
- R1: <code>new URLSearchParams(location.search</code> (x2)
- R2: <code>o.get("end_time")</code>
- R2: <code>o.get("start_time")</code>
- R2: <code>o.get("tb_duration_order")</code>
- R2: <code>o.get("tb_page")</code>
- R2: <code>o.get("tb_page_size")</code>
- R2: <code>o.get("tb_start_time_order")</code>
- R2: <code>o.get("user_id_type")</code>

</details>

<details><summary><b>9.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@teareplay/oncall-ef959ef1.js</code> - <b>10</b> matches (R1 3 / R2 7) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=h</code>
- R1: <code>location=C</code> (x2)
- R1: <code>new URL(location.href</code> (x3)
- R2: <code>er.configManager.get("browser")</code>
- R2: <code>er.configManager.get("user_unique_id")</code> (x3)
- R2: <code>er.configManager.get("user_unique_id_type")</code>
- R2: <code>er.configManager.get("web_id")</code> (x3)
- R2: <code>nr.configManager.get("reportErrorCallback")</code>
- R2: <code>nr.configManager.get("user")</code> (x7)
- R2: <code>rr.get("Content-Type")</code>

</details>

<details><summary><b>10.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytecloud_common-lib_7_52_0_axios_1_13_2_byted-tea-sdk_5_3_10_node_~d45cb8-ef959ef1.js</code> - <b>9</b> matches (R1 3 / R2 6) - first 137 - routes: 137</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x3)
- R1: <code>new URL(window.location.href</code>
- R2: <code>r.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)
- R2: <code>t.configManager.get("browser")</code>
- R2: <code>t.configManager.get("user_unique_id")</code> (x3)
- R2: <code>t.configManager.get("user_unique_id_type")</code>
- R2: <code>t.configManager.get("web_id")</code> (x3)

</details>

<details><summary><b>11.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code> - <b>9</b> matches (R1 3 / R2 6) - first 92 - routes: 92-95, 97, 99-100, 102, 111, 182, 241</summary>

- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(location.search</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>o.get("context")</code>
- R2: <code>o.get("dashboardId")</code>
- R2: <code>o.get("dashboard_id")</code>
- R2: <code>o.get("history_id")</code>
- R2: <code>o.get("reportId")</code>
- R2: <code>o.get("report_id")</code>

</details>

<details><summary><b>12.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793791839869</code> - <b>8</b> matches (R1 2 / R2 6) - first 2 - routes: 2</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>13.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793791857034</code> - <b>8</b> matches (R1 2 / R2 6) - first 3 - routes: 3</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>14.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792052792</code> - <b>8</b> matches (R1 2 / R2 6) - first 19 - routes: 19</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>15.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792175030</code> - <b>8</b> matches (R1 2 / R2 6) - first 29 - routes: 29</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>16.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792238990</code> - <b>8</b> matches (R1 2 / R2 6) - first 34 - routes: 34</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>17.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792457878</code> - <b>8</b> matches (R1 2 / R2 6) - first 52 - routes: 52</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>18.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792494768</code> - <b>8</b> matches (R1 2 / R2 6) - first 55 - routes: 55</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>19.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792720470</code> - <b>8</b> matches (R1 2 / R2 6) - first 73 - routes: 73</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>20.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792780623</code> - <b>8</b> matches (R1 2 / R2 6) - first 77 - routes: 77</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>21.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792869663</code> - <b>8</b> matches (R1 2 / R2 6) - first 84 - routes: 84</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>22.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792956857</code> - <b>8</b> matches (R1 2 / R2 6) - first 91 - routes: 91</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>23.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792982249</code> - <b>8</b> matches (R1 2 / R2 6) - first 93 - routes: 93</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>24.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793792995388</code> - <b>8</b> matches (R1 2 / R2 6) - first 94 - routes: 94</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>25.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793022872</code> - <b>8</b> matches (R1 2 / R2 6) - first 96 - routes: 96</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>26.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793047801</code> - <b>8</b> matches (R1 2 / R2 6) - first 98 - routes: 98</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>27.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793108997</code> - <b>8</b> matches (R1 2 / R2 6) - first 103 - routes: 103</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>28.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793121551</code> - <b>8</b> matches (R1 2 / R2 6) - first 104 - routes: 104</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>29.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793133301</code> - <b>8</b> matches (R1 2 / R2 6) - first 105 - routes: 105</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>30.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793145537</code> - <b>8</b> matches (R1 2 / R2 6) - first 106 - routes: 106</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>31.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793170418</code> - <b>8</b> matches (R1 2 / R2 6) - first 108 - routes: 108</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>32.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793195604</code> - <b>8</b> matches (R1 2 / R2 6) - first 110 - routes: 110</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>33.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793221074</code> - <b>8</b> matches (R1 2 / R2 6) - first 112 - routes: 112</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>34.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793234020</code> - <b>8</b> matches (R1 2 / R2 6) - first 113 - routes: 113</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>35.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793297078</code> - <b>8</b> matches (R1 2 / R2 6) - first 118 - routes: 118</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>36.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793381909</code> - <b>8</b> matches (R1 2 / R2 6) - first 125 - routes: 125</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>37.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793432045</code> - <b>8</b> matches (R1 2 / R2 6) - first 129 - routes: 129</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>38.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793657073</code> - <b>8</b> matches (R1 2 / R2 6) - first 147 - routes: 147</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>39.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793708599</code> - <b>8</b> matches (R1 2 / R2 6) - first 151 - routes: 151</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>40.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793747162</code> - <b>8</b> matches (R1 2 / R2 6) - first 154 - routes: 154</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>41.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793783958</code> - <b>8</b> matches (R1 2 / R2 6) - first 157 - routes: 157</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>42.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793808562</code> - <b>8</b> matches (R1 2 / R2 6) - first 159 - routes: 159</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>43.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793833127</code> - <b>8</b> matches (R1 2 / R2 6) - first 161 - routes: 161</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>44.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793793857438</code> - <b>8</b> matches (R1 2 / R2 6) - first 163 - routes: 163</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>45.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794600618</code> - <b>8</b> matches (R1 2 / R2 6) - first 222 - routes: 222</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>46.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794687558</code> - <b>8</b> matches (R1 2 / R2 6) - first 229 - routes: 229</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>47.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794702137</code> - <b>8</b> matches (R1 2 / R2 6) - first 230 - routes: 230</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>48.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794712582</code> - <b>8</b> matches (R1 2 / R2 6) - first 231 - routes: 231</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>49.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794725855</code> - <b>8</b> matches (R1 2 / R2 6) - first 232 - routes: 232</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>50.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794737019</code> - <b>8</b> matches (R1 2 / R2 6) - first 233 - routes: 233</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>51.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794763533</code> - <b>8</b> matches (R1 2 / R2 6) - first 235 - routes: 235</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>52.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794799520</code> - <b>8</b> matches (R1 2 / R2 6) - first 238 - routes: 238</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>53.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794812252</code> - <b>8</b> matches (R1 2 / R2 6) - first 239 - routes: 239</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>54.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794850916</code> - <b>8</b> matches (R1 2 / R2 6) - first 242 - routes: 242</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>55.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794861075</code> - <b>8</b> matches (R1 2 / R2 6) - first 243 - routes: 243</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>56.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794874340</code> - <b>8</b> matches (R1 2 / R2 6) - first 244 - routes: 244</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>57.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794887142</code> - <b>8</b> matches (R1 2 / R2 6) - first 245 - routes: 245</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>58.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794912458</code> - <b>8</b> matches (R1 2 / R2 6) - first 247 - routes: 247</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>59.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794949363</code> - <b>8</b> matches (R1 2 / R2 6) - first 248 - routes: 248</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>60.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794960984</code> - <b>8</b> matches (R1 2 / R2 6) - first 249 - routes: 249</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>61.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794973819</code> - <b>8</b> matches (R1 2 / R2 6) - first 250 - routes: 250</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>62.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793794998783</code> - <b>8</b> matches (R1 2 / R2 6) - first 252 - routes: 252</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>63.</b> <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js?globalName=IndocStudioFinder&amp;t=1793795011366</code> - <b>8</b> matches (R1 2 / R2 6) - first 253 - routes: 253</summary>

- R1: <code>location.href=f</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>nt.collect.configManager.get("custom")</code>
- R2: <code>nt.configManager.get("user_unique_id")</code> (x3)
- R2: <code>nt.configManager.get("user_unique_id_type")</code>
- R2: <code>nt.configManager.get("web_id")</code> (x3)
- R2: <code>rt.configManager.get("reportErrorCallback")</code>
- R2: <code>rt.configManager.get("user")</code> (x6)

</details>

<details><summary><b>64.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-ui_TeaNextOncall_index_tsx-ef959ef1.js</code> - <b>8</b> matches (R1 2 / R2 6) - first 2 - routes: 2, 4-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91, 118, 121, 125-126, 129, 147-148, 151, 154, 157, 159, 161, 163, 193, 197, 201-202, 222, 224, 240, 242-245, 247-250, 253</summary>

- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>n.get("context")</code>
- R2: <code>n.get("dashboardId")</code>
- R2: <code>n.get("dashboard_id")</code>
- R2: <code>n.get("history_id")</code>
- R2: <code>n.get("reportId")</code>
- R2: <code>n.get("report_id")</code>

</details>

<details><summary><b>65.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/suite-navigation-ef959ef1.js</code> - <b>8</b> matches (R1 1 / R2 7) - first 4 - routes: 4-5, 19, 31, 34, 52, 55, 73, 77, 80-81, 84, 118, 121, 125-126, 129, 135-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 197, 201-202, 222, 224, 232, 234-240, 242-245, 247-250, 252-253</summary>

- R1: <code>location.href=N</code>
- R2: <code>e.get("/v1/config")</code>
- R2: <code>e.get("/v1/index")</code>
- R2: <code>e.get("/v1/menu")</code>
- R2: <code>e.get("/v1/resources")</code>
- R2: <code>e.get("/v1/user")</code>
- R2: <code>e.get("/v1/user/orgs")</code>
- R2: <code>e.get("/v2/navigation_menu")</code>

</details>

<details><summary><b>66.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_path-to-regexp_6_3_0_node_modules_path-to-regexp_dist_es2015_index_~aabd00-ef959ef1.js</code> - <b>7</b> matches (R1 1 / R2 6) - first 137 - routes: 137</summary>

- R1: <code>location=u</code>
- R2: <code>R.configManager.get("user")</code> (x6)
- R2: <code>_.configManager.get("reportErrorCallback")</code>
- R2: <code>a.collect.configManager.get("custom")</code>
- R2: <code>a.configManager.get("user_unique_id")</code> (x3)
- R2: <code>a.configManager.get("user_unique_id_type")</code>
- R2: <code>a.configManager.get("web_id")</code> (x3)

</details>

<details><summary><b>67.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_react-pdf_7_7_3__types_react_16_14_60_react-dom_16_14_0_react_16_14~5cf4f4-ef959ef1.js</code> - <b>7</b> matches (R1 0 / R2 7) - first 236 - routes: 236</summary>

- R2: <code>J._l10nPromise.get("editor_alt_text_button_label")</code>
- R2: <code>J._l10nPromise.get("editor_alt_text_decorative_tooltip")</code>
- R2: <code>J._l10nPromise.get("editor_alt_text_edit_button_label")</code>
- R2: <code>T.AnnotationEditor._l10nPromise.get("editor_free_text2_aria_label")</code>
- R2: <code>T.AnnotationEditor._l10nPromise.get("free_text2_default_content")</code>
- R2: <code>n.AnnotationEditor._l10nPromise.get("editor_ink2_aria_label")</code>
- R2: <code>n.AnnotationEditor._l10nPromise.get("editor_ink_canvas_aria_label")</code>

</details>

<details><summary><b>68.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - <b>6</b> matches (R1 4 / R2 2) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=p</code>
- R1: <code>new URLSearchParams(location.search</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>i.Z.get("__spti")</code>
- R2: <code>rb.Z.get("csrfToken")</code>

</details>

<details><summary><b>69.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code> - <b>6</b> matches (R1 0 / R2 6) - first 94 - routes: 94</summary>

- R2: <code>E.get("hour")</code>
- R2: <code>E.get("minute")</code>
- R2: <code>E.get("second")</code>
- R2: <code>d.get("hour")</code>
- R2: <code>d.get("minute")</code>
- R2: <code>d.get("second")</code>

</details>

<details><summary><b>70.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_monaco-editor-ef959ef1.js</code> - <b>5</b> matches (R1 3 / R2 2) - first 110 - routes: 110, 112</summary>

- R1: <code>.query.modelInfo</code> (x5)
- R1: <code>.query.word</code>
- R1: <code>location.href=_</code>
- R2: <code>W.get("text")</code>
- R2: <code>m.get("3")</code>

</details>

<details><summary><b>71.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai-analysis-space_components_CurrentAnalysisFavoriteButton_index_tsx~src_uba-p~943b6d-ef959ef1.js</code> - <b>5</b> matches (R1 3 / R2 2) - first 99 - routes: 99-100, 234</summary>

- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(location.search</code>
- R1: <code>window.location.replace(</code>
- R2: <code>E.get("jobId")</code>
- R2: <code>E.get("reportId")</code>

</details>

<details><summary><b>72.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code> - <b>5</b> matches (R1 5 / R2 0) - first 139 - routes: 139, 234, 236-237</summary>

- R1: <code>.query.dimensions</code> (x9)
- R1: <code>.query.filters</code>
- R1: <code>.query.measures</code> (x6)
- R1: <code>.query.periods</code> (x3)
- R1: <code>.query.visualization</code> (x2)

</details>

<details><summary><b>73.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_GeneralAnalysis_tsx-ef959ef1.js</code> - <b>5</b> matches (R1 4 / R2 1) - first 234 - routes: 234</summary>

- R1: <code>.query.dimensions</code>
- R1: <code>.query.filters</code>
- R1: <code>.query.measures</code>
- R1: <code>.query.periods</code> (x2)
- R2: <code>d.get(`${g.subject}:${g.name}`)</code>

</details>

<details><summary><b>74.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_ad-feelgood-ef959ef1.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=e</code>
- R1: <code>location=i</code>
- R1: <code>window.location.replace(</code>

</details>

<details><summary><b>75.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_bytereplay_others-ef959ef1.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 94 - routes: 94, 110-111, 132-137, 234</summary>

- R1: <code>location=$</code> (x2)
- R1: <code>location=U</code>
- R1: <code>location=q</code> (x2)
- R2: <code>se.get("Content-Type")</code>

</details>

<details><summary><b>76.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_file-saver_2_0_5_node_modules_file-saver_dist_FileSaver_min_js-ef959ef1.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 100 - routes: 100</summary>

- R1: <code>location.href=c</code>
- R1: <code>location.href=v</code>
- R1: <code>location=c</code>
- R1: <code>location=v</code>

</details>

<details><summary><b>77.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_react-grid-layout_1_3_4_react-dom_16_14_0_react_16_14_0_node_module~8cdb78-ef959ef1.js</code> - <b>4</b> matches (R1 0 / R2 4) - first 92 - routes: 92, 95, 97, 102, 111, 134, 182, 202, 234, 241</summary>

- R2: <code>N.get("action")</code>
- R2: <code>N.get("controlled")</code>
- R2: <code>N.get("lifecycle")</code>
- R2: <code>N.get("status")</code>

</details>

<details><summary><b>78.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_ConversionAnalysisEntry_index_tsx-ef959ef1.js</code> - <b>4</b> matches (R1 1 / R2 3) - first 234 - routes: 234</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>P.get("reportId")</code>
- R2: <code>P.get("resultId")</code>
- R2: <code>q.get("event_name")</code>

</details>

<details><summary><b>79.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_board_avatar-group_svg~src_uba-ui_Hove~acf15e-ef959ef1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location.href=(</code> (x5)
- R1: <code>location.href=`</code> (x2)
- R1: <code>new URLSearchParams(location.search</code> (x2)

</details>

<details><summary><b>80.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_ai_checker_components_DashboardRuntimeProvider_index_tsx~src_uba-pages_ai_check~638f87-ef959ef1.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 236 - routes: 236</summary>

- R1: <code>location.href=(</code>
- R2: <code>y.get("hideHeader")</code>
- R2: <code>y.get("hide_era_menu")</code>

</details>

<details><summary><b>81.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_ai_checker_components_DashboardRuntimeProvider_index_tsx~src_uba-pages_ai_check~c2882a-ef959ef1.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 237 - routes: 237</summary>

- R1: <code>location.href=(</code>
- R2: <code>L.get("hideHeader")</code>
- R2: <code>L.get("hide_era_menu")</code>

</details>

<details><summary><b>82.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/fc-tools-ef959ef1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=J</code>
- R1: <code>location.href=j</code>
- R1: <code>location.href=w</code>

</details>

<details><summary><b>83.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_mermaid-ef959ef1.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 80 - routes: 80</summary>

- R2: <code>ze.get("fill")</code>
- R2: <code>ze.get("stroke")</code>
- R2: <code>ze.get("stroke-dasharray")</code>

</details>

<details><summary><b>84.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bdeefe_suite-design_0_0_87_react_16_14_0_node_modules_bdeefe_suite-~b4e7e6-ef959ef1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 30 - routes: 30, 92, 95, 97, 101-102, 111, 121, 133-134, 193, 202, 234, 241</summary>

- R1: <code>location=0</code>
- R1: <code>location=t</code>
- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>85.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytereplay_snapshot_0_17_19_node_modules_bytereplay_snapshot_dist_e~b2e5c3-ef959ef1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 94 - routes: 94, 110-111, 134, 136-137, 202</summary>

- R1: <code>location=b</code>
- R1: <code>location=l</code>
- R1: <code>location=s</code>

</details>

<details><summary><b>86.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_lark_open-widgets_1_1_7-beta_2__arco-design_web-react_2_63_0__lark_~2f61f1-ef959ef1.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location=$</code>
- R2: <code>o.cfg.get("reportErrorCallback")</code>
- R2: <code>s.cfg.get("evtParams")</code>

</details>

<details><summary><b>87.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_GeneralAnalysisBarChart_tsx~src_uba-page~e77cfd-ef959ef1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 234 - routes: 234</summary>

- R1: <code>.query.dimensions</code> (x2)
- R1: <code>.query.periods</code> (x4)
- R1: <code>.query.visualization</code> (x4)

</details>

<details><summary><b>88.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_detective_contexts_WorkspaceManageProvider_tsx-ef959ef1.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>r.get("isLibraIframe")</code>
- R2: <code>r.get("showUserDetail")</code>

</details>

<details><summary><b>89.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_event_structure_eventAnalysisContext_ts-ef959ef1.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 99 - routes: 99-100</summary>

- R1: <code>new URLSearchParams(location.search</code> (x2)
- R2: <code>E.get("dateTime")</code>
- R2: <code>Y.get("dateTime")</code>

</details>

<details><summary><b>90.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_MicroscopeUserListModal_index_tsx~src_uba-pages_event_utils_microscope_agentDrill~d4edce-ef959ef1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 92 - routes: 92, 95, 97, 99-100, 102, 111, 182, 241</summary>

- R1: <code>location.href=L</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>91.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/locale-en_US-ef959ef1.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R2: <code>input.get("messages")</code>
- R2: <code>m.get("role")</code> (x2)

</details>

<details><summary><b>92.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIbehaviorlogoFinderColor_svg~src_components_finder-icon_index_tsx~src_layouts_~8147a9-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 112 - routes: 112</summary>

- R1: <code>location.href=(</code>
- R2: <code>q.get("oa_space_id")</code>

</details>

<details><summary><b>93.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-ui_Menu_Header_index_tsx-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 4 - routes: 4-5, 19, 31, 34, 52, 55, 73, 77, 80-81, 84, 118, 121, 125-126, 129, 135-139, 147-148, 151, 154, 157, 159, 161, 163, 201-202, 222, 224, 232, 234-240, 242-245, 247-250, 252-253</summary>

- R1: <code>location.href=(</code>
- R1: <code>location.href=m</code>

</details>

<details><summary><b>94.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/module2-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.replace(</code> (x2)
- R1: <code>location=s</code>

</details>

<details><summary><b>95.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_ant-design_create-react-context_0_2_6_prop-types_15_8_1_react_16_4_~c7c932-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=T</code> (x2)
- R1: <code>location.href=d</code>

</details>

<details><summary><b>96.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytecloud_cloud-api-config_0_22_0_node_modules_bytecloud_cloud-api-~966aac-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 136 - routes: 136-137</summary>

- R1: <code>location.href=`</code>
- R1: <code>location.href=t</code>

</details>

<details><summary><b>97.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_byted-ei_kani-js-sdk_2_0_13_node_modules_byted-ei_kani-js-sdk_lib_i~748ee1-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.replace(</code>
- R1: <code>location=c</code>

</details>

<details><summary><b>98.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_css-loader_6_8_1_webpack_4_47_0_node_modules_css-loader_dist_cjs_js~94ee70-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location=w</code>
- R2: <code>Ce.get("onEffect")</code> (x2)

</details>

<details><summary><b>99.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_volcengine-service_web-sdk_2_1_1_node_modules_volcengine-service_we~737f9a-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location.assign(</code>
- R2: <code>O.default.get("csrfToken")</code>

</details>

<details><summary><b>100.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~87a468-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 113 - routes: 113</summary>

- R1: <code>location.href=(</code>
- R2: <code>le.get("oa_space_id")</code>

</details>

<details><summary><b>101.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_uba-pages_cost-governance_assets_ai-loading-color_svg~src_pages_embed~c11d28-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 182 - routes: 182</summary>

- R1: <code>new URLSearchParams(location.search</code> (x3)
- R2: <code>D.get("isCustomFilter")</code>

</details>

<details><summary><b>102.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~src_uba-ui_HoverEl~75953a-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 99 - routes: 99-100</summary>

- R1: <code>location.href=(</code>
- R2: <code>lt.get("oa_space_id")</code>

</details>

<details><summary><b>103.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_uba-pages_dashboard_widgets_Report_component~974a2b-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 182 - routes: 182, 234, 241</summary>

- R1: <code>location.href=(</code>
- R2: <code>lt.get("oa_space_id")</code>

</details>

<details><summary><b>104.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_pages_dashboard_dashboard_approval_index_tsx~src_uba-pages_dashboard_components_ApplyPer~6cfb9f-ef959ef1.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 92 - routes: 92, 95, 99-100, 102, 113, 148, 182</summary>

- R2: <code>t.get("hideHeader")</code>
- R2: <code>t.get("hide_era_menu")</code>

</details>

<details><summary><b>105.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_FilterMetric_FilterMetricModal_index_tsx-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>.query.queryHash</code>
- R1: <code>.query.state</code> (x3)

</details>

<details><summary><b>106.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_AICheckerLayout_index_tsx~src_uba-pages_ai_checker_compo~5ab8d6-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 234 - routes: 234</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x9)
- R2: <code>i.default.get(`/v1/app?app_id=${D}`)</code>

</details>

<details><summary><b>107.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_AnalysisCopilot_AnalysisCopilotAction_tsx~src_uba-pages_~2a1423-ef959ef1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 234 - routes: 234</summary>

- R1: <code>.query.slice</code>
- R1: <code>.query.trim</code>

</details>

<details><summary><b>108.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_Filter_components_FilterCard_styles_less~src_uba-block_InlineCohort_entries_Inlin~f1568a-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 99 - routes: 99-100</summary>

- R1: <code>new URLSearchParams(location.search</code>
- R2: <code>E.get("jobId")</code>

</details>

<details><summary><b>109.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_analysis_creators_createAnalysisReport_ts~src_uba-utils_analysis_creators_crea~93d478-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 92 - routes: 92, 95, 97, 99-100, 102, 182, 222, 224, 241</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x3)
- R2: <code>z.get("source")</code>

</details>

<details><summary><b>110.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_utils_i18n_index_ts-ef959ef1.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R2: <code>E.get("dorToken")</code>
- R2: <code>E.get("eraUserUniqueId")</code>

</details>

<details><summary><b>111.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~~~~~~~src_uba-pages_ai_checker_components_SessionDetail_SessionDetail_tsx-ef959ef1.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 234 - routes: 234, 236</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>q.get("content-type")</code>

</details>

<details><summary><b>112.</b> <code>https://livechat.im.byteplusbiz.com/sockjs.min.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 141 - routes: 141</summary>

- R1: <code>location=r</code>

</details>

<details><summary><b>113.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/main-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R2: <code>j.get("/v1/init")</code>

</details>

<details><summary><b>114.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIbehaviorlogoFinderColor_svg~src_layouts_empty_css~src_uba-ui_NoData_index_tsx~ac5daf-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=(</code>

</details>

<details><summary><b>115.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_40x_overdue_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 252 - routes: 252</summary>

- R1: <code>location.href="</code>

</details>

<details><summary><b>116.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_dashboard__layout_tsx~src_uba-utils_factory_createContextWithSelector_tsx~src_uba-u~d42463-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 31 - routes: 31, 101-102</summary>

- R2: <code>N.get("oa_space_id")</code>

</details>

<details><summary><b>117.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_products_overview_index_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 240 - routes: 240, 253</summary>

- R1: <code>location.href=(</code>

</details>

<details><summary><b>118.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_des_entries_DesPageCore_tsx~src_hooks_useSelector_ts~src_uba-utils_ai_getAIAgen~96164b-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 98 - routes: 98</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>119.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_session-replay_components_SessionReplayDetailHeader_SessionReplayPlayerSaveToDa~8c754f-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 201 - routes: 201</summary>

- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>120.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@arco-design/web-react-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R2: <code>o.get("month")</code>

</details>

<details><summary><b>121.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/module-others-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 145, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location.href=d</code>

</details>

<details><summary><b>122.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_teareplay_others-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 94 - routes: 94, 111</summary>

- R1: <code>location=q</code>

</details>

<details><summary><b>123.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_ies_intl-incontext-plugin_1_0_7_node_modules_ies_intl-incontext-plu~61ddbe-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>location=E</code>

</details>

<details><summary><b>124.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_rehype-raw_7_0_0_node_modules_rehype-raw_index_js~node_modules_pnpm~bb5e8d-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location=!</code>

</details>

<details><summary><b>125.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_tiptap_extension-table_3_13_0__tiptap_core_3_8_0__tiptap_pm_3_8_0_n~b8070f-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 30 - routes: 30, 92, 95, 97, 101-102, 111, 126, 133-134, 234, 241</summary>

- R2: <code>f.get("defaultProtocol")</code> (x2)

</details>

<details><summary><b>126.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIstarColor_svg~src_uba-pages_smart-studio_components_SmartStudioTask_SmartStu~f17c20-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 2 - routes: 2-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-230, 232, 234-245, 247-250, 252-253</summary>

- R1: <code>location.href=T</code>

</details>

<details><summary><b>127.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_components_with-menu-authorized_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 4 - routes: 4, 19, 29-31, 34, 52, 55, 73, 77, 84, 91, 93-94, 96-97, 101-106, 118, 121, 125, 129, 142, 147-148, 151, 154, 157, 159, 161, 163, 193, 197, 222, 224, 240, 244, 253</summary>

- R1: <code>location.href=(</code>

</details>

<details><summary><b>128.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_layouts_stopPageLoadCollectorProvider_tsx~src_uba-pages_session-replay_structures_sessio~639eee-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 94 - routes: 94</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>129.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_DashboardChart_ButtonGroup_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 99 - routes: 99-100, 113, 201</summary>

- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>130.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_DashboardChart_EventDashboardModal_tsx~src_uba-pages_event_utils_meta_helper_c~5747e1-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 30 - routes: 30, 92, 95, 97, 99-100, 102, 111, 113, 182, 241</summary>

- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>131.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_assets_ai-technolog-spark_svg~src_uba-pages_ai_checker_components_I~4371bc-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 234 - routes: 234</summary>

- R1: <code>.query.queryHash</code>

</details>

<details><summary><b>132.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_AiAssist_AiAssistComposer_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 234 - routes: 234</summary>

- R1: <code>.query.toLocaleLowerCase</code>

</details>

<details><summary><b>133.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_SessionDetail_SpanArea_tsx~src_uba-pages_ai_checker_comp~d0372a-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 139 - routes: 139, 234, 236-237</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x3)

</details>

<details><summary><b>134.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_TrajectoryAnalysis_index_ts-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 234 - routes: 234</summary>

- R2: <code>wn.get("reportId")</code>

</details>

<details><summary><b>135.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_stores_useSpaceOverviewStore_ts-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 30 - routes: 30, 92, 95, 97, 99-100, 102, 113, 137-139, 148, 182, 236-237</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>136.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorDowngrade_BehaviorDetailBehavi~4b5be2-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 93 - routes: 93-94</summary>

- R1: <code>location.href=(</code>

</details>

<details><summary><b>137.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_dashboard_components_SelectDashboard_index_tsx~src_pages_datamanager_dashCente~585f5f-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 30 - routes: 30, 92, 95, 97, 99-102, 111, 113, 148, 182, 241</summary>

- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>138.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_dashboard_home_render_tsx~src_uba-pages_event_utils_microscope_AgentDrillDownT~77e5c2-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 234 - routes: 234, 241</summary>

- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>139.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_tag_components_CohortCreate_index_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 234 - routes: 234</summary>

- R1: <code>new URLSearchParams(location.search</code> (x2)

</details>

<details><summary><b>140.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_tag_entries_cohort_index_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 112 - routes: 112, 234</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>141.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_AsyncBoundary_index_tsx~src_services_dashboard_ts~src_uba-block_InlineCohort_util~53ce98-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 81 - routes: 81</summary>

- R2: <code>C.get("oa_space_id")</code>

</details>

<details><summary><b>142.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_UbaChart_index_tsx-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>143.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_pref_loading_react_tsx~src_services_dashboard_ts~src_uba-block_InlineCohort_ut~bc719c-ef959ef1.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 1 - routes: 1-5, 19, 29-31, 34, 52, 55, 73, 77, 80-81, 84, 91-106, 108, 110-113, 118, 121, 125-126, 129, 132-139, 141-142, 147-148, 151, 154, 157, 159, 161, 163, 182, 193, 197, 201-202, 222, 224, 229-245, 247-250, 252-253</summary>

- R2: <code>m.get("oa_space_id")</code>

</details>

<details><summary><b>144.</b> <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~~src_uba-pages_dashboard_widgets_Report_component_AnalysisReports_index_tsx~src_uba-pages_da~c7b14e-ef959ef1.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 95 - routes: 95, 241</summary>

- R1: <code>location.href=z</code>

</details>

## Duplicate Routes

162 routes skipped as duplicate results. Full mapping is in `data/scan.log`.

<details><summary>Duplicate mapping</summary>

- Route 4: 7-18, 20-28, 32-33, 35-51, 53-54, 56-72, 74-76, 78-79, 82-83, 85-90, 115-117, 119-120, 124, 127-128, 130-131, 140, 143-144, 146, 149-150, 152-153, 155-156, 158, 160, 162, 164-181, 184-189, 191-192, 194-196, 198-200, 203-211, 214, 216-221, 223, 225-228, 251
- Route 5: 6, 114, 212-213, 246
- Route 31: 215
- Route 92: 107, 183
- Route 99: 109
- Route 121: 122-123, 190
- Route 145: 254

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
