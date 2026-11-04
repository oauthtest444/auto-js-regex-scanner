# JS Regex Scan - Route-First Report

- Generated: 2026-11-04 18:33:53 UTC
- Routes: 258 tested | 79 unique | 179 duplicate | 0 errors
- Route coverage: 23 with new app surface | 4 vendor-only | 52 with no new discoveries
- Files: 71 unique JS files | 101 raw file URLs | 30 cache-busted duplicates collapsed | 535 unique file-match texts (745 raw)
- Matches: 685 source | 60 sink | 52 URLSearchParams `.get` flagged | 488 unique texts
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP | Unscanned: 0
- Only unique route IDs are listed. Missing route numbers are duplicates mapped near the end.
- Source matches are unique by match text within each route. Location sinks are per file and not deduped.
- Cache-busted duplicate URLs are collapsed by normalized URL (scheme + host + path).
- `App` = application `src_`/`~src_` chunks. Vendor, runtime, locale, replay, and SDK bundles are collapsed; vendor match texts are in the final index.
- URLSearchParams `.get` classification uses a same-file constructor/alias heuristic; function-parameter and cross-file flows still need manual tracing.

## Unique First Routes

27 unique first routes that load new JS files with unique regex matches. `--` separates entries.

https://console.byteplus.com/datafinder/app/218463/access-analysis-mp
--
https://console.byteplus.com/datafinder/app/218463/access-analysis-mp/:report_id?/:result_id
--
https://console.byteplus.com/datafinder/app/218463/behavior-detail
--
https://console.byteplus.com/datafinder/app/218463/behavior-detail/detail
--
https://console.byteplus.com/datafinder/app/218463/dashboard-editor/:dashboard_id
--
https://console.byteplus.com/datafinder/app/218463/dashboard/:dashboard_id
--
https://console.byteplus.com/datafinder/app/218463/data-manage/data-verification-details
--
https://console.byteplus.com/datafinder/app/218463/data-manage/event-params
--
https://console.byteplus.com/datafinder/app/218463/diagnostic/:tenantId?/:taskId?/:stage
--
https://console.byteplus.com/datafinder/app/218463/editor
--
https://console.byteplus.com/datafinder/app/218463/embed-analysis-result
--
https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail/detail
--
https://console.byteplus.com/datafinder/app/218463/embed-dashboard
--
https://console.byteplus.com/datafinder/app/218463/embed-dashboard-editor/:dashboard_id
--
https://console.byteplus.com/datafinder/app/218463/embed-des-registration-management
--
https://console.byteplus.com/datafinder/app/218463/embed-event-analysis/:report_id?/:result_id
--
https://console.byteplus.com/datafinder/app/218463/embed-session-replay-list
--
https://console.byteplus.com/datafinder/app/218463/embed-user-cohort/edit-cohort/:type/:id
--
https://console.byteplus.com/datafinder/app/218463/embed-virtual-event-edit
--
https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/journeys/:spaceId?/:taskId?/:subTaskId?/:leafTaskId
--
https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/cozeloop/:spaceId/:module/:subModule/result/:result
--
https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/share/session/:token
--
https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/share/trace/:token
--
https://console.byteplus.com/datafinder/app/218463/user-list
--
https://console.byteplus.com/datafinder/llm-workbench/operations-agent/share/session/:token
--
https://console.byteplus.com/datafinder/llm-workbench/operations-agent/share/trace/:token
--
https://console.byteplus.com/datafinder/org/:ordId/embed-function-overview

## Route 1 — https://console.byteplus.com/datafinder/app/218463/access-analysis-mp

- HTTP: 200 | Loaded: 29 files (8 app / 21 vendor) | New: 29 files (8 app / 21 vendor)
- New source matches: 20 app / 374 vendor | New location sinks: 3 app / 18 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_board_avatar-group_svg~src_uba-ui_Hove~acf15e-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIstarColor_svg~src_uba-pages_smart-studio_components_SmartStudioTask_SmartStu~f17c20-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_FilterMetric_FilterMetricModal_index_tsx-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_detective_contexts_WorkspaceManageProvider_tsx-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_UbaChart_index_tsx-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_pref_loading_react_tsx~src_services_dashboard_ts~src_uba-block_InlineCohort_ut~bc719c-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_utils_i18n_index_ts-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>E.get("dorToken")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_utils_i18n_index_ts-ef959ef1.js</code>
- <code>E.get("eraUserUniqueId")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_utils_i18n_index_ts-ef959ef1.js</code>
- <code>m.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_pref_loading_react_tsx~src_services_dashboard_ts~src_uba-block_InlineCohort_ut~bc719c-ef959ef1.js</code>
- <code>r.get("isLibraIframe")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_detective_contexts_WorkspaceManageProvider_tsx-ef959ef1.js</code>
- <code>r.get("showUserDetail")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_detective_contexts_WorkspaceManageProvider_tsx-ef959ef1.js</code>

#### `.query.*` / `query["..."]`

- <code>.query.queryHash</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_FilterMetric_FilterMetricModal_index_tsx-ef959ef1.js</code>
- <code>.query.state</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_FilterMetric_FilterMetricModal_index_tsx-ef959ef1.js</code>

#### URL / URLSearchParams construction

- <code>A=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>M=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>W=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_UbaChart_index_tsx-ef959ef1.js</code>
- <code>p=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>r=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_detective_contexts_WorkspaceManageProvider_tsx-ef959ef1.js</code>
- <code>s=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_board_avatar-group_svg~src_uba-ui_Hove~acf15e-ef959ef1.js</code>

#### Other `.get(...)` (7)

<details><summary>Show generic .get matches</summary>

- <code>o.get("end_time")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>o.get("start_time")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>o.get("tb_duration_order")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>o.get("tb_page")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>o.get("tb_page_size")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>o.get("tb_start_time_order")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>o.get("user_id_type")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>

</details>

### App location sinks (not deduped)

- <code>location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_AppNext_tsx~src_uba-utils_operators_takeData_ts-ef959ef1.js</code>
- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIstarColor_svg~src_uba-pages_smart-studio_components_SmartStudioTask_SmartStu~f17c20-ef959ef1.js</code>

- Vendor/SDK additions: +21 files | 374 source / 18 sinks (match texts in final index)

## Route 2 — https://console.byteplus.com/datafinder/app/218463/access-analysis-mp/:report_id?/:result_id

- HTTP: 200 | Loaded: 30 files (9 app / 21 vendor) | New: 2 files (1 app / 1 vendor)
- New source matches: 0 app / 7 vendor | New location sinks: 1 app / 1 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-ui_Menu_Header_index_tsx-ef959ef1.js</code>

### App location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-ui_Menu_Header_index_tsx-ef959ef1.js</code>

- Vendor/SDK additions: +1 files | 7 source / 1 sinks (match texts in final index)

## Route 11 — https://console.byteplus.com/datafinder/app/218463/behavior-detail

- HTTP: 200 | Loaded: 31 files (10 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 7 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction

- <code>f=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>

#### Other `.get(...)` (6)

<details><summary>Show generic .get matches</summary>

- <code>o.get("context")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>
- <code>o.get("dashboardId")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>
- <code>o.get("dashboard_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>
- <code>o.get("history_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>
- <code>o.get("reportId")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>
- <code>o.get("report_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailSearchBar_components_BehaviorDetailSea~ebd390-ef959ef1.js</code>

</details>

## Route 12 — https://console.byteplus.com/datafinder/app/218463/behavior-detail/detail

- HTTP: 200 | Loaded: 32 files (11 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 6 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/datafinder/app/218463/behavior-detail/detail?query_id=&amp;query_type=user_unique_id&amp;appId=&amp;activeEventId=&amp;curDevice=pc&amp;curDevice=mobile&amp;curDevice=mp&amp;isShowFiltered=true&amp;eventParamsType=list&amp;timestamp=1791244800000&amp;timestamp=1793813404772&amp;resolvedQueryId=&amp;resolvedQueryType=&amp;selectedTemplateId=&amp;eventCategory=event&amp;flowType=event&amp;eventOperation=in&amp;subjectId=&amp;eventFilterList=%5B%5D&amp;snapshot_id=&amp;sort=desc&amp;searchQuestion=

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>

### App source matches (unique)

#### Other `.get(...)` (6)

<details><summary>Show generic .get matches</summary>

- <code>E.get("hour")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>
- <code>E.get("minute")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>
- <code>E.get("second")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>
- <code>d.get("hour")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>
- <code>d.get("minute")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>
- <code>d.get("second")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_behaviorDetail_components_BehaviorDetailBehaviorFlow_index_tsx~src_uba-pages_b~22852f-ef959ef1.js</code>

</details>

## Route 30 — https://console.byteplus.com/datafinder/app/218463/dashboard-editor/:dashboard_id

- HTTP: 200 | Loaded: 33 files (11 app / 22 vendor) | New: 4 files (2 app / 2 vendor)
- New source matches: 4 app / 5 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_DashboardChart_EventDashboardModal_tsx~src_uba-pages_event_utils_meta_helper_c~5747e1-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_analysis_creators_createAnalysisReport_ts~src_uba-utils_analysis_creators_crea~93d478-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>z.get("source")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_analysis_creators_createAnalysisReport_ts~src_uba-utils_analysis_creators_crea~93d478-ef959ef1.js</code>

#### URL / URLSearchParams construction

- <code>B=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_analysis_creators_createAnalysisReport_ts~src_uba-utils_analysis_creators_crea~93d478-ef959ef1.js</code>
- <code>xt=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_DashboardChart_EventDashboardModal_tsx~src_uba-pages_event_utils_meta_helper_c~5747e1-ef959ef1.js</code>
- <code>z=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-utils_analysis_creators_createAnalysisReport_ts~src_uba-utils_analysis_creators_crea~93d478-ef959ef1.js</code>

- Vendor/SDK additions: +2 files | 5 source / 0 sinks (match texts in final index)

## Route 31 — https://console.byteplus.com/datafinder/app/218463/dashboard/:dashboard_id

- HTTP: 200 | Loaded: 31 files (10 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/datafinder/app/218463/dashboard/0

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_dashboard__layout_tsx~src_uba-utils_factory_createContextWithSelector_tsx~src_uba-u~d42463-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>N.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_dashboard__layout_tsx~src_uba-utils_factory_createContextWithSelector_tsx~src_uba-u~d42463-ef959ef1.js</code>

## Route 43 — https://console.byteplus.com/datafinder/app/218463/data-manage/data-verification-details

- HTTP: 200 | Loaded: 31 files (10 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~src_uba-ui_HoverEl~804835-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>se.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~src_uba-ui_HoverEl~804835-ef959ef1.js</code>

## Route 46 — https://console.byteplus.com/datafinder/app/218463/data-manage/event-params

- HTTP: 200 | Loaded: 31 files (10 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_external_rangers_event-params_index_tsx-ef959ef1.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction

- <code>f=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_external_rangers_event-params_index_tsx-ef959ef1.js</code>

## Route 81 — https://console.byteplus.com/datafinder/app/218463/diagnostic/:tenantId?/:taskId?/:stage

- HTTP: 200 | Loaded: 31 files (10 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_AsyncBoundary_index_tsx~src_services_dashboard_ts~src_uba-block_InlineCohort_util~53ce98-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>C.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_AsyncBoundary_index_tsx~src_services_dashboard_ts~src_uba-block_InlineCohort_util~53ce98-ef959ef1.js</code>

## Route 91 — https://console.byteplus.com/datafinder/app/218463/editor

- HTTP: 200 | Loaded: 31 files (9 app / 22 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_layouts_empty_css~src_pages_editor__layout_tsx~src_dsl_v3-types_types_ts~src_services_das~1e869a-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>A.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_layouts_empty_css~src_pages_editor__layout_tsx~src_dsl_v3-types_types_ts~src_services_das~1e869a-ef959ef1.js</code>

## Route 92 — https://console.byteplus.com/datafinder/app/218463/embed-analysis-result

- HTTP: 200 | Loaded: 35 files (14 app / 21 vendor) | New: 3 files (3 app / 0 vendor)
- New source matches: 5 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_uba-pages_dashboard_widgets_Report_component~974a2b-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_pages_dashboard_dashboard_approval_index_tsx~src_uba-pages_dashboard_components_ApplyPer~6cfb9f-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_MicroscopeUserListModal_index_tsx~src_uba-pages_event_utils_microscope_agentDrill~d4edce-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>lt.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_uba-pages_dashboard_widgets_Report_component~974a2b-ef959ef1.js</code>
- <code>t.get("hideHeader")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_pages_dashboard_dashboard_approval_index_tsx~src_uba-pages_dashboard_components_ApplyPer~6cfb9f-ef959ef1.js</code>
- <code>t.get("hide_era_menu")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_pages_dashboard_dashboard_approval_index_tsx~src_uba-pages_dashboard_components_ApplyPer~6cfb9f-ef959ef1.js</code>

#### URL / URLSearchParams construction

- <code>O=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_MicroscopeUserListModal_index_tsx~src_uba-pages_event_utils_microscope_agentDrill~d4edce-ef959ef1.js</code>
- <code>l=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_MicroscopeUserListModal_index_tsx~src_uba-pages_event_utils_microscope_agentDrill~d4edce-ef959ef1.js</code>

## Route 95 — https://console.byteplus.com/datafinder/app/218463/embed-dashboard

- HTTP: 200 | Loaded: 36 files (16 app / 20 vendor) | New: 2 files (2 app / 0 vendor)
- New source matches: 3 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_uba-pages_cost-governance_assets_ai-loading-color_svg~src_pages_embed~c11d28-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~~src_uba-pages_dashboard_widgets_Report_component_AnalysisReports_index_tsx~src_uba-pages_da~c7b14e-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>D.get("isCustomFilter")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_uba-pages_cost-governance_assets_ai-loading-color_svg~src_pages_embed~c11d28-ef959ef1.js</code>

#### URL / URLSearchParams construction

- <code>D=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_uba-pages_cost-governance_assets_ai-loading-color_svg~src_pages_embed~c11d28-ef959ef1.js</code>
- <code>l=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_uba-pages_cost-governance_assets_ai-loading-color_svg~src_pages_embed~c11d28-ef959ef1.js</code>

### App location sinks (not deduped)

- <code>window.location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~~src_uba-pages_dashboard_widgets_Report_component_AnalysisReports_index_tsx~src_uba-pages_da~c7b14e-ef959ef1.js</code>

## Route 98 — https://console.byteplus.com/datafinder/app/218463/embed-des-registration-management

- HTTP: 200 | Loaded: 29 files (9 app / 20 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_des_entries_DesPageCore_tsx~src_hooks_useSelector_ts~src_uba-utils_ai_getAIAgen~96164b-ef959ef1.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction

- <code>C=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_des_entries_DesPageCore_tsx~src_hooks_useSelector_ts~src_uba-utils_ai_getAIAgen~96164b-ef959ef1.js</code>

## Route 99 — https://console.byteplus.com/datafinder/app/218463/embed-event-analysis/:report_id?/:result_id

- HTTP: 200 | Loaded: 38 files (18 app / 20 vendor) | New: 6 files (5 app / 1 vendor)
- New source matches: 8 app / 0 vendor | New location sinks: 1 app / 2 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~src_uba-ui_HoverEl~75953a-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_DashboardChart_ButtonGroup_tsx-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai-analysis-space_components_CurrentAnalysisFavoriteButton_index_tsx~src_uba-p~943b6d-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_event_structure_eventAnalysisContext_ts-ef959ef1.js</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_Filter_components_FilterCard_styles_less~src_uba-block_InlineCohort_entries_Inlin~f1568a-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>E.get("dateTime")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_event_structure_eventAnalysisContext_ts-ef959ef1.js</code>
- <code>E.get("jobId")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_Filter_components_FilterCard_styles_less~src_uba-block_InlineCohort_entries_Inlin~f1568a-ef959ef1.js</code>
- <code>E.get("reportId")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai-analysis-space_components_CurrentAnalysisFavoriteButton_index_tsx~src_uba-p~943b6d-ef959ef1.js</code>
- <code>Y.get("dateTime")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_event_structure_eventAnalysisContext_ts-ef959ef1.js</code>

#### URL / URLSearchParams construction

- <code>A=new URL(window.location.href</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai-analysis-space_components_CurrentAnalysisFavoriteButton_index_tsx~src_uba-p~943b6d-ef959ef1.js</code>
- <code>E=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-ui_Filter_components_FilterCard_styles_less~src_uba-block_InlineCohort_entries_Inlin~f1568a-ef959ef1.js</code>
- <code>K=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-block_DashboardChart_ButtonGroup_tsx-ef959ef1.js</code>
- <code>Y=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_event_structure_eventAnalysisContext_ts-ef959ef1.js</code>

### App location sinks (not deduped)

- <code>window.location.replace(</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai-analysis-space_components_CurrentAnalysisFavoriteButton_index_tsx~src_uba-p~943b6d-ef959ef1.js</code>

- Vendor/SDK additions: +1 files | 0 source / 2 sinks (match texts in final index)

## Route 110 — https://console.byteplus.com/datafinder/app/218463/embed-session-replay-list

- HTTP: 200 | Loaded: 30 files (9 app / 21 vendor) | New: 2 files (1 app / 1 vendor)
- New source matches: 1 app / 9 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/datafinder/app/218463/embed-session-replay-list?filter_id=378079

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_uba-ui_AIPromptBanner_index_tsx~src_uba-ui_C~9b5ee5-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>w.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_uba-ui_AIPromptBanner_index_tsx~src_uba-ui_C~9b5ee5-ef959ef1.js</code>

- Vendor/SDK additions: +1 files | 9 source / 0 sinks (match texts in final index)

## Route 112 — https://console.byteplus.com/datafinder/app/218463/embed-user-cohort/edit-cohort/:type/:id

- HTTP: 200 | Loaded: 29 files (9 app / 20 vendor) | New: 2 files (1 app / 1 vendor)
- New source matches: 1 app / 4 vendor | New location sinks: 0 app / 0 vendor
- Note: final URL: https://console.byteplus.com/datafinder/app/218463/user-cohort

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIstarColor_svg~src_uba-ui_HoverElement_index_less~src_layouts_stopPageLoadColl~9fc246-ef959ef1.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction

- <code>M=new URLSearchParams(location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_assets_ai_AIstarColor_svg~src_uba-ui_HoverElement_index_less~src_layouts_stopPageLoadColl~9fc246-ef959ef1.js</code>

- Vendor/SDK additions: +1 files | 4 source / 0 sinks (match texts in final index)

## Route 113 — https://console.byteplus.com/datafinder/app/218463/embed-virtual-event-edit

- HTTP: 200 | Loaded: 31 files (12 app / 19 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~87a468-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>le.get("oa_space_id")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_assets_NEW_svg~src_assets_ai_AIbehaviorlogoFinderColor_svg~src_assets_ai_AIstarColor_svg~87a468-ef959ef1.js</code>

## Route 136 — https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/cozeloop/:spaceId/:module/:subModule/result/:result

- HTTP: 200 | Loaded: 32 files (10 app / 22 vendor) | New: 2 files (1 app / 1 vendor)
- New source matches: 5 app / 8 vendor | New location sinks: 0 app / 1 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code>

### App source matches (unique)

#### `.query.*` / `query["..."]`

- <code>.query.dimensions</code> (x9) — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code>
- <code>.query.filters</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code>
- <code>.query.measures</code> (x6) — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code>
- <code>.query.periods</code> (x3) — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code>
- <code>.query.visualization</code> (x2) — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_GeneralAnalysis_CustomDimension_customDimensionDomain_ts~abbec1-ef959ef1.js</code>

- Vendor/SDK additions: +1 files | 8 source / 1 sinks (match texts in final index)

## Route 139 — https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/share/trace/:token

- HTTP: 200 | Loaded: 31 files (11 app / 20 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_SessionDetail_SpanArea_tsx~src_uba-pages_ai_checker_comp~d0372a-ef959ef1.js</code>

### App source matches (unique)

#### URL / URLSearchParams construction

- <code>M=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_SessionDetail_SpanArea_tsx~src_uba-pages_ai_checker_comp~d0372a-ef959ef1.js</code>
- <code>s=new URLSearchParams(window.location.search</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_ai_checker_components_SessionDetail_SpanArea_tsx~src_uba-pages_ai_checker_comp~d0372a-ef959ef1.js</code>

## Route 225 — https://console.byteplus.com/datafinder/app/218463/user-list

- HTTP: 200 | Loaded: 31 files (10 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 1 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_single_user-list_UserList_tsx-ef959ef1.js</code>

### App location sinks (not deduped)

- <code>location.href=</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_pages_single_user-list_UserList_tsx-ef959ef1.js</code>

## Route 236 — https://console.byteplus.com/datafinder/llm-workbench/operations-agent/share/session/:token

- HTTP: 200 | Loaded: 33 files (12 app / 21 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 1 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~~~~~~~src_uba-pages_ai_checker_components_SessionDetail_SessionDetail_tsx-ef959ef1.js</code>

### App source matches (unique)

#### Other `.get(...)` (1)

<details><summary>Show generic .get matches</summary>

- <code>q.get("content-type")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~~~~~~~src_uba-pages_ai_checker_components_SessionDetail_SessionDetail_tsx-ef959ef1.js</code>

</details>

## Route 237 — https://console.byteplus.com/datafinder/llm-workbench/operations-agent/share/trace/:token

- HTTP: 200 | Loaded: 32 files (12 app / 20 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 2 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_ai_checker_components_DashboardRuntimeProvider_index_tsx~src_uba-pages_ai_check~c2882a-ef959ef1.js</code>

### App source matches (unique)

#### URLSearchParams `.get(...)`

- <code>L.get("hideHeader")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_ai_checker_components_DashboardRuntimeProvider_index_tsx~src_uba-pages_ai_check~c2882a-ef959ef1.js</code>
- <code>L.get("hide_era_menu")</code> — <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-pages_ai_checker_components_DashboardRuntimeProvider_index_tsx~src_uba-pages_ai_check~c2882a-ef959ef1.js</code>

## Route 241 — https://console.byteplus.com/datafinder/org/:ordId/embed-function-overview

- HTTP: 200 | Loaded: 37 files (15 app / 22 vendor) | New: 1 files (1 app / 0 vendor)
- New source matches: 0 app / 0 vendor | New location sinks: 0 app / 0 vendor

### New app JS files

- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_uba-pages_dashboard_home_render_tsx~src_uba-pages_event_utils_microscope_AgentDrillDownT~77e5c2-ef959ef1.js</code>

## Vendor-Only Routes

4 unique routes added only vendor/SDK files or matches. These are summarized here; vendor match texts are in the final index.

| Route | URL | New vendor files | Vendor source | Vendor sinks |
|---:|---|---:|---:|---:|
| 94 | <code>https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail/detail (final: https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail/detail?query_id=&amp;query_type=user_unique_id&amp;appId=&amp;activeEventId=&amp;curDevice=pc&amp;curDevice=mobile&amp;curDevice=mp&amp;isShowFiltered=true&amp;eventParamsType=list&amp;timestamp=1791244800000&amp;timestamp=1793814678913&amp;resolvedQueryId=&amp;resolvedQueryType=&amp;selectedTemplateId=&amp;eventCategory=event&amp;flowType=event&amp;eventOperation=in&amp;subjectId=&amp;eventFilterList=%5B%5D...</code> | 2 | 2 | 0 |
| 97 | <code>https://console.byteplus.com/datafinder/app/218463/embed-dashboard-editor/:dashboard_id</code> | 1 | 1 | 0 |
| 133 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/journeys/:spaceId?/:taskId?/:subTaskId?/:leafTaskId (final: https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/journeys/:spaceId?%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId=)</code> | 1 | 0 | 1 |
| 138 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/share/session/:token</code> | 1 | 7 | 0 |

## Unique Routes With No New Discoveries

52 unique routes loaded no new JS files and produced no new source matches or location sinks.

| Route | URL | Loaded files |
|---:|---|---:|
| 9 | <code>https://console.byteplus.com/datafinder/app/218463/attribution-analysis/:report_id?/:result_id</code> | 29 |
| 29 | <code>https://console.byteplus.com/datafinder/app/218463/dashboard-editor</code> | 28 |
| 35 | <code>https://console.byteplus.com/datafinder/app/218463/data-manage/analysis-subjects</code> | 30 |
| 37 | <code>https://console.byteplus.com/datafinder/app/218463/data-manage/bav-events/create/web</code> | 31 |
| 80 | <code>https://console.byteplus.com/datafinder/app/218463/detective/:tenantId?/:taskId?/:user_id?/:stage (final: https://console.byteplus.com/datafinder/app/218463/overview)</code> | 32 |
| 82 | <code>https://console.byteplus.com/datafinder/app/218463/distribute-analysis</code> | 13 |
| 93 | <code>https://console.byteplus.com/datafinder/app/218463/embed-behavior-detail</code> | 29 |
| 96 | <code>https://console.byteplus.com/datafinder/app/218463/embed-dashboard-editor</code> | 28 |
| 100 | <code>https://console.byteplus.com/datafinder/app/218463/embed-funnel-analysis/:report_id?/:result_id</code> | 37 |
| 101 | <code>https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard (final: https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard/7000732696393548289)</code> | 32 |
| 102 | <code>https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard/:dashboard_id (final: https://console.byteplus.com/datafinder/app/218463/embed-fusion-dashboard/0)</code> | 36 |
| 103 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission</code> | 28 |
| 104 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission/department</code> | 28 |
| 105 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission/roles</code> | 27 |
| 106 | <code>https://console.byteplus.com/datafinder/app/218463/embed-permission/roles/detail</code> | 28 |
| 107 | <code>https://console.byteplus.com/datafinder/app/218463/embed-report</code> | 34 |
| 108 | <code>https://console.byteplus.com/datafinder/app/218463/embed-report/no-access</code> | 28 |
| 109 | <code>https://console.byteplus.com/datafinder/app/218463/embed-retention-analysis/custom/:report_id?/:result_id</code> | 37 |
| 111 | <code>https://console.byteplus.com/datafinder/app/218463/embed-session-replay-player/:recording_id</code> | 33 |
| 121 | <code>https://console.byteplus.com/datafinder/app/218463/industry-analysis (final: https://console.byteplus.com/datafinder/app/218463/overview)</code> | 31 |
| 132 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/dashboard/:spaceId?/:taskId?/:subTaskId?/:leafTaskId (final: https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/dashboard/:spaceId/0?%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId=)</code> | 32 |
| 134 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/trace/:spaceId?/:taskId?/:subTaskId?/:leafTaskId (final: https://console.byteplus.com/datafinder/app/218463/llm-workbench/embed-operations-agent/trace/:spaceId?%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId=)</code> | 31 |
| 135 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/:pageType?/:spaceId?/:taskId?/:subTaskId?/:leafTaskId</code> | 32 |
| 137 | <code>https://console.byteplus.com/datafinder/app/218463/llm-workbench/operations-agent/cozeloop/:spaceId?/:module?/:subModule?/:leafModule</code> | 31 |
| 148 | <code>https://console.byteplus.com/datafinder/app/218463/manage/dashboard-manage</code> | 31 |
| 176 | <code>https://console.byteplus.com/datafinder/app/218463/push (final: https://console.byteplus.com/datafinder/app/218463/overview)</code> | 31 |
| 177 | <code>https://console.byteplus.com/datafinder/app/218463/qrcode-analysis</code> | 31 |
| 178 | <code>https://console.byteplus.com/datafinder/app/218463/qrcode-analysis/:report_id?/:result_id</code> | 31 |
| 179 | <code>https://console.byteplus.com/datafinder/app/218463/qrcode-manage</code> | 31 |
| 180 | <code>https://console.byteplus.com/datafinder/app/218463/qrcode-manage/edit-qrcode/:code_id</code> | 31 |
| 182 | <code>https://console.byteplus.com/datafinder/app/218463/render/analysis/result</code> | 35 |
| 183 | <code>https://console.byteplus.com/datafinder/app/218463/render/dashboard</code> | 33 |
| 193 | <code>https://console.byteplus.com/datafinder/app/218463/scenarios/editor (final: https://console.byteplus.com/datafinder/app/218463/scenarios)</code> | 29 |
| 212 | <code>https://console.byteplus.com/datafinder/app/218463/tag</code> | 32 |
| 229 | <code>https://console.byteplus.com/datafinder/ai-sparring</code> | 28 |
| 230 | <code>https://console.byteplus.com/datafinder/ai-sparring-management</code> | 28 |
| 231 | <code>https://console.byteplus.com/datafinder/ai_landing_page</code> | 19 |
| 232 | <code>https://console.byteplus.com/datafinder/bridge</code> | 30 |
| 233 | <code>https://console.byteplus.com/datafinder/lark-verify</code> | 19 |
| 234 | <code>https://console.byteplus.com/datafinder/llm-workbench/operations-agent/:pageType?/:spaceId?/:taskId?/:subTaskId?/:leafTaskId (final: https://console.byteplus.com/datafinder/project/null/llm-workbench/operations-agent/landing?%2F%3AspaceId%3F%2F%3AtaskId%3F%2F%3AsubTaskId%3F%2F%3AleafTaskId=)</code> | 34 |
| 235 | <code>https://console.byteplus.com/datafinder/llm-workbench/operations-agent/admin-open</code> | 30 |
| 238 | <code>https://console.byteplus.com/datafinder/no-access</code> | 30 |
| 239 | <code>https://console.byteplus.com/datafinder/not-found</code> | 30 |
| 240 | <code>https://console.byteplus.com/datafinder/org (final: https://console.byteplus.com/datafinder/org/84/products)</code> | 31 |
| 242 | <code>https://console.byteplus.com/datafinder/org/:orgId/collocation (final: https://console.byteplus.com/datafinder/no-access?region=cn-beijing)</code> | 31 |
| 250 | <code>https://console.byteplus.com/datafinder/org/:orgId?/upgrade</code> | 31 |
| 251 | <code>https://console.byteplus.com/datafinder/org/welcome</code> | 31 |
| 252 | <code>https://console.byteplus.com/datafinder/overdue</code> | 30 |
| 255 | <code>https://console.byteplus.com/datafinder/crash</code> | 30 |
| 256 | <code>https://console.byteplus.com/datafinder/crash/:appPlatform?/:id/:os</code> | 29 |
| 257 | <code>https://console.byteplus.com/datafinder/symbol/:os</code> | 30 |
| 258 | <code>https://console.byteplus.com/datafinder/sourcemap</code> | 30 |

## Duplicate Routes

179 duplicate routes produced no new JS files, source matches, or location sinks.

- Route 2 source; duplicates: 3-8, 10, 13-28, 32-34, 36, 38-42, 44-45, 47-79, 83-90, 114-120, 124, 126-131, 140-147, 149-161, 163-175, 181, 184-188, 191, 194-211, 213-224, 227-228, 243-249, 253-254
- Route 9 source; duplicates: 162
- Route 82 source; duplicates: 125, 189
- Route 121 source; duplicates: 122-123, 190, 192
- Route 225 source; duplicates: 226

## Vendor/SDK Match Index

<details><summary>All vendor/SDK source and sink matches, unique per file</summary>

- <code>https://lf-dp.byteintlstatic.com/obj/dp-open-internet-us/indoc/1.0.0.380/runtime/indoc-v2.js</code>
  - [source] <code>nt.collect.configManager.get("custom")</code>
  - [source] <code>nt.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>nt.configManager.get("user_unique_id_type")</code>
  - [source] <code>nt.configManager.get("web_id")</code> (x3)
  - [source] <code>rt.configManager.get("reportErrorCallback")</code>
  - [source] <code>rt.configManager.get("user")</code> (x6)
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code>
  - [source] <code>i.Z.get("__spti")</code>
  - [source] <code>rb.Z.get("csrfToken")</code>
  - [source] <code>e=new URLSearchParams(location.search</code> (x3)
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [sink] <code>window.location.href=</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/echarts.min-4.7.0.js</code>
  - [source] <code>L.get("avoidLabelOverlap")</code>
  - [source] <code>L.get("minShowLabelAngle")</code>
  - [source] <code>T.get("smooth")</code>
  - [source] <code>_.get("show")</code>
  - [source] <code>a.get("description")</code> (x2)
  - [source] <code>a.get("formatter")</code>
  - [source] <code>a.get("icon")</code>
  - [source] <code>a.get("inside")</code> (x2)
  - [source] <code>a.get("realtime")</code>
  - [source] <code>a.get("show")</code> (x2)
  - [source] <code>a.get("throttle")</code>
  - [source] <code>c.get("axisLine.lineStyle.color")</code>
  - [source] <code>c.get("barBorderRadius")</code>
  - [source] <code>e.get("alignWithLabel")</code>
  - [source] <code>e.get("animation")</code> (x3)
  - [source] <code>e.get("axisExpandCenter")</code>
  - [source] <code>e.get("axisExpandCount")</code>
  - [source] <code>e.get("axisExpandDebounce")</code>
  - [source] <code>e.get("axisExpandWidth")</code>
  - [source] <code>e.get("axisLabel.inside")</code>
  - [source] <code>e.get("axisLabel.show")</code>
  - [source] <code>e.get("axisLine.lineStyle.color")</code> (x3)
  - [source] <code>e.get("axisTick.inside")</code>
  - [source] <code>e.get("backgroundColor")</code>
  - [source] <code>e.get("borderColor")</code>
  - [source] <code>e.get("borderRadius")</code>
  - [source] <code>e.get("borderWidth")</code>
  - [source] <code>e.get("cursor")</code>
  - [source] <code>e.get("draggable")</code>
  - [source] <code>e.get("focusNodeAdjacency")</code>
  - [source] <code>e.get("hoverAnimation")</code>
  - [source] <code>e.get("itemGap")</code>
  - [source] <code>e.get("itemStyle.color")</code> (x2)
  - [source] <code>e.get("label.show")</code>
  - [source] <code>e.get("maxInterval")</code>
  - [source] <code>e.get("minInterval")</code>
  - [source] <code>e.get("orient")</code>
  - [source] <code>e.get("parallelIndex")</code>
  - [source] <code>e.get("rotate")</code>
  - [source] <code>e.get("show")</code> (x4)
  - [source] <code>e.get("showDetail")</code>
  - [source] <code>e.get("symbolOffset")</code>
  - [source] <code>e.get("symbolRotate")</code>
  - [source] <code>e.get("triggerEvent")</code>
  - [source] <code>e.hostModel.get("percentPrecision")</code>
  - [source] <code>f.get("axisPointer.axis")</code>
  - [source] <code>f.get("itemGap")</code>
  - [source] <code>f.get("itemSize")</code>
  - [source] <code>f.get("rotate")</code>
  - [source] <code>f.get("show")</code>
  - [source] <code>g.get("dataBackgroundColor")</code>
  - [source] <code>g.get("show")</code>
  - [source] <code>h.get("axisLabel.show")</code>
  - [source] <code>h.get("axisLine.lineStyle.color")</code>
  - [source] <code>h.get("itemSize")</code>
  - [source] <code>h.get("show")</code>
  - [source] <code>h.get("showTitle")</code>
  - [source] <code>i.get("axisExpandTriggerOn")</code>
  - [source] <code>i.get("axisExpandable")</code>
  - [source] <code>i.get("backgroundColor")</code>
  - [source] <code>i.get("borderRadius")</code>
  - [source] <code>i.get("connectedBackgroundColor")</code>
  - [source] <code>i.get("emphasis.label.position")</code>
  - [source] <code>i.get("excludeComponents")</code>
  - [source] <code>i.get("focusNodeAdjacency")</code> (x2)
  - [source] <code>i.get("friction")</code>
  - [source] <code>i.get("gravity")</code>
  - [source] <code>i.get("hoverAnimation")</code>
  - [source] <code>i.get("label.formatter")</code>
  - [source] <code>i.get("label.precision")</code>
  - [source] <code>i.get("markLine")</code> (x2)
  - [source] <code>i.get("markPoint")</code> (x2)
  - [source] <code>i.get("pixelRatio")</code>
  - [source] <code>i.get("seriesDataIndices")</code>
  - [source] <code>i.get("show")</code>
  - [source] <code>i.get("showContent")</code>
  - [source] <code>i.get("silent")</code>
  - [source] <code>i.get("stack")</code> (x2)
  - [source] <code>i.get("symbolRepeatDirection")</code>
  - [source] <code>i.get("symbolRotate")</code>
  - [source] <code>i.get("textStyle.color")</code>
  - [source] <code>i.get("tooltip")</code>
  - [source] <code>i.get("value")</code>
  - [source] <code>i.get("z")</code>
  - [source] <code>i.get("zoomLock")</code>
  - [source] <code>l.get("borderColor")</code>
  - [source] <code>l.get("dataBackgroundColor")</code>
  - [source] <code>l.get("ellipsis")</code>
  - [source] <code>l.get("fillerColor")</code>
  - [source] <code>l.get("handleIcon")</code>
  - [source] <code>l.get("handleSize")</code>
  - [source] <code>l.get("r")</code>
  - [source] <code>l.get("r0")</code>
  - [source] <code>m.get("formatter")</code>
  - [source] <code>m.get("show")</code>
  - [source] <code>n.get("boundaryGap")</code>
  - [source] <code>n.get("buttonColor")</code>
  - [source] <code>n.get("buttonTextColor")</code>
  - [source] <code>n.get("edgeForkPosition")</code>
  - [source] <code>n.get("edgeShape")</code>
  - [source] <code>n.get("expandAndCollapse")</code>
  - [source] <code>n.get("hoverAnimation")</code>
  - [source] <code>n.get("inverse")</code>
  - [source] <code>n.get("itemStyle.color")</code>
  - [source] <code>n.get("lineStyle.curveness")</code> (x2)
  - [source] <code>n.get("lineStyle.show")</code>
  - [source] <code>n.get("max")</code>
  - [source] <code>n.get("min")</code>
  - [source] <code>n.get("option.bar")</code>
  - [source] <code>n.get("option.line")</code>
  - [source] <code>n.get("option.stack")</code>
  - [source] <code>n.get("pointer.show")</code>
  - [source] <code>n.get("polyline")</code>
  - [source] <code>n.get("readOnly")</code>
  - [source] <code>n.get("roam")</code>
  - [source] <code>n.get("show")</code> (x3)
  - [source] <code>n.get("symbolOffset")</code>
  - [source] <code>n.get("symbolRotate")</code>
  - [source] <code>n.get("symbolSize")</code>
  - [source] <code>n.get("title")</code>
  - [source] <code>n.get("triggerOn")</code>
  - [source] <code>o.get("circular.rotateLabel")</code>
  - [source] <code>o.get("emptyItemWidth")</code>
  - [source] <code>o.get("formatterParams")</code>
  - [source] <code>o.get("icon")</code>
  - [source] <code>o.get("ignoreForceLayout")</code>
  - [source] <code>o.get("lineStyle.curveness")</code>
  - [source] <code>o.get("rippleEffect.period")</code>
  - [source] <code>o.get("roam")</code> (x2)
  - [source] <code>o.get("selectedMode")</code>
  - [source] <code>o.get("show")</code> (x4)
  - [source] <code>o.get("silent")</code>
  - [source] <code>p.get("show")</code>
  - [source] <code>r.get("animation")</code>
  - [source] <code>r.get("borderColor")</code>
  - [source] <code>r.get("borderRadius")</code>
  - [source] <code>r.get("borderWidth")</code>
  - [source] <code>r.get("hoverOffset")</code>
  - [source] <code>r.get("itemGap")</code>
  - [source] <code>r.get("orient")</code>
  - [source] <code>r.get("selectedOffset")</code>
  - [source] <code>r.get("shadowBlur")</code>
  - [source] <code>r.get("shadowColor")</code>
  - [source] <code>r.get("shadowOffsetX")</code>
  - [source] <code>r.get("shadowOffsetY")</code>
  - [source] <code>r.get("show")</code>
  - [source] <code>s.get("label.formatter")</code>
  - [source] <code>s.get("label.precision")</code>
  - [source] <code>s.get("show")</code>
  - [source] <code>s.get("textAlign")</code>
  - [source] <code>s.get("textBackgroundColor")</code>
  - [source] <code>s.get("textBorderRadius")</code>
  - [source] <code>s.get("textFill")</code>
  - [source] <code>s.get("textPadding")</code>
  - [source] <code>s.get("textPosition")</code>
  - [source] <code>s.get("verticalAlign")</code>
  - [source] <code>t.ecModel.get("useUTC")</code>
  - [source] <code>t.get("axisExpandRate")</code>
  - [source] <code>t.get("axisLabel.inside")</code>
  - [source] <code>t.get("axisLine.lineStyle.color")</code> (x2)
  - [source] <code>t.get("axisLine.show")</code>
  - [source] <code>t.get("axisTick.inside")</code>
  - [source] <code>t.get("backgroundColor")</code> (x3)
  - [source] <code>t.get("barMaxWidth")</code> (x3)
  - [source] <code>t.get("barMinWidth")</code> (x2)
  - [source] <code>t.get("barWidth")</code> (x2)
  - [source] <code>t.get("borderRadius")</code>
  - [source] <code>t.get("boundaryGap")</code> (x2)
  - [source] <code>t.get("calendarIndex")</code>
  - [source] <code>t.get("center")</code> (x3)
  - [source] <code>t.get("confine")</code>
  - [source] <code>t.get("connectNulls")</code> (x2)
  - [source] <code>t.get("containLabel")</code>
  - [source] <code>t.get("coordinateSystem")</code>
  - [source] <code>t.get("delay")</code>
  - [source] <code>t.get("dim")</code>
  - [source] <code>t.get("edgeSymbol")</code>
  - [source] <code>t.get("edgeSymbolSize")</code>
  - [source] <code>t.get("endAngle")</code>
  - [source] <code>t.get("enterable")</code>
  - [source] <code>t.get("extraCssText")</code>
  - [source] <code>t.get("geoCoord")</code>
  - [source] <code>t.get("gradientColor")</code>
  - [source] <code>t.get("inverse")</code>
  - [source] <code>t.get("itemGap")</code> (x3)
  - [source] <code>t.get("label.align")</code>
  - [source] <code>t.get("label.baseline")</code>
  - [source] <code>t.get("label.verticalAlign")</code>
  - [source] <code>t.get("layoutIterations")</code>
  - [source] <code>t.get("legendHoverLink")</code>
  - [source] <code>t.get("max")</code> (x3)
  - [source] <code>t.get("maxSize")</code>
  - [source] <code>t.get("min")</code> (x3)
  - [source] <code>t.get("minSize")</code>
  - [source] <code>t.get("nameMap")</code> (x2)
  - [source] <code>t.get("nodeAlign")</code>
  - [source] <code>t.get("orient")</code> (x3)
  - [source] <code>t.get("parallelId")</code>
  - [source] <code>t.get("parallelIndex")</code> (x4)
  - [source] <code>t.get("period")</code>
  - [source] <code>t.get("polarId")</code>
  - [source] <code>t.get("polarIndex")</code>
  - [source] <code>t.get("radarIndex")</code> (x2)
  - [source] <code>t.get("radius")</code>
  - [source] <code>t.get("realtime")</code>
  - [source] <code>t.get("scaleLimit")</code> (x2)
  - [source] <code>t.get("show")</code> (x4)
  - [source] <code>t.get("showLegendSymbol")</code> (x2)
  - [source] <code>t.get("silent")</code> (x3)
  - [source] <code>t.get("singleAxisId")</code>
  - [source] <code>t.get("singleAxisIndex")</code>
  - [source] <code>t.get("smooth")</code>
  - [source] <code>t.get("smoothMonotone")</code> (x2)
  - [source] <code>t.get("stack")</code> (x2)
  - [source] <code>t.get("startAngle")</code> (x3)
  - [source] <code>t.get("step")</code>
  - [source] <code>t.get("subtarget")</code>
  - [source] <code>t.get("symbol")</code> (x2)
  - [source] <code>t.get("symbolMargin")</code>
  - [source] <code>t.get("symbolSize")</code>
  - [source] <code>t.get("target")</code>
  - [source] <code>t.get("text")</code>
  - [source] <code>t.get("textBaseline")</code>
  - [source] <code>t.get("textVerticalAlign")</code>
  - [source] <code>t.get("title.0.text")</code>
  - [source] <code>t.get("triggerEvent")</code>
  - [source] <code>t.get("visualDimension")</code>
  - [source] <code>t.get("z")</code> (x3)
  - [source] <code>t.get("zlevel")</code>
  - [source] <code>t.get("zoom")</code> (x3)
  - [source] <code>u.get("renderMode")</code>
  - [source] <code>v.get("show")</code>
  - [source] <code>w.get("animation")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/locale-en_US-ef959ef1.js</code>
  - [source] <code>input.get("messages")</code>
  - [source] <code>m.get("role")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/main-ef959ef1.js</code>
  - [source] <code>j.get("/v1/init")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_layouts_stopPageLoadCollectorProvider_tsx~src_pages_embed-session-replay-list_index_tsx~s~6fac17-ef959ef1.js</code>
  - [source] <code>a.get("end_time")</code>
  - [source] <code>a.get("start_time")</code>
  - [source] <code>a.get("tb_duration_order")</code>
  - [source] <code>a.get("tb_page")</code>
  - [source] <code>a.get("tb_page_size")</code>
  - [source] <code>a.get("tb_start_time_order")</code>
  - [source] <code>a.get("user_id_type")</code>
  - [source] <code>u=new URL(window.location.href</code>
  - [source] <code>y=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/src_uba-ui_TeaNextOncall_index_tsx-ef959ef1.js</code>
  - [source] <code>n.get("context")</code>
  - [source] <code>n.get("dashboardId")</code>
  - [source] <code>n.get("dashboard_id")</code>
  - [source] <code>n.get("history_id")</code>
  - [source] <code>n.get("reportId")</code>
  - [source] <code>n.get("report_id")</code>
  - [source] <code>E=new URLSearchParams(window.location.search</code>
  - [source] <code>o=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@arco-design/web-react-ef959ef1.js</code>
  - [source] <code>o.get("month")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/fc-tools-ef959ef1.js</code>
  - [sink] <code>window.location.href=</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/indoc-sdk-ef959ef1.js</code>
  - [source] <code>Mn.get("_TEA_VE_APIHOST")</code>
  - [source] <code>Mn.get("_TEA_VE_OPEN")</code>
  - [source] <code>Mn.get("_VISUAL_EDITOR_U")</code>
  - [source] <code>Mn.get("_VISUAL_EDITOR_V")</code>
  - [source] <code>Mn.get("lang")</code>
  - [source] <code>e.collect.configManager.get("custom")</code>
  - [source] <code>e.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>e.configManager.get("user_unique_id_type")</code>
  - [source] <code>e.configManager.get("web_id")</code> (x3)
  - [source] <code>i.configManager.get("reportErrorCallback")</code>
  - [source] <code>i.configManager.get("user")</code> (x6)
  - [source] <code>n.get("defaultKeyword")</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/instant-finder-ef959ef1.js</code>
  - [source] <code>a.get("formatter")</code>
  - [source] <code>a.get("rotate")</code> (x2)
  - [source] <code>c.get("boundaryGap")</code>
  - [source] <code>c.get("formatter")</code>
  - [source] <code>c.get("show")</code>
  - [source] <code>d.get("alignTicks")</code>
  - [source] <code>d.get("formatterParams")</code>
  - [source] <code>d.get("interval")</code>
  - [source] <code>e.get("animation")</code>
  - [source] <code>e.get("backgroundColor")</code>
  - [source] <code>e.get("blurScope")</code>
  - [source] <code>e.get("borderColor")</code>
  - [source] <code>e.get("borderWidth")</code>
  - [source] <code>e.get("disabled")</code>
  - [source] <code>e.get("enterable")</code> (x2)
  - [source] <code>e.get("focus")</code>
  - [source] <code>e.get("instant_finder")</code> (x2)
  - [source] <code>e.get("maxInterval")</code>
  - [source] <code>e.get("minInterval")</code>
  - [source] <code>e.get("scale")</code>
  - [source] <code>e.get("seriesDataIndices")</code>
  - [source] <code>e.get("show")</code>
  - [source] <code>e.get("smooth")</code>
  - [source] <code>e.get("step")</code>
  - [source] <code>e.get("transitionDuration")</code>
  - [source] <code>e.get("triggerLineEvent")</code>
  - [source] <code>i.get("barMaxWidth")</code>
  - [source] <code>i.get("barMinWidth")</code>
  - [source] <code>i.get("barWidth")</code>
  - [source] <code>i.get("z")</code>
  - [source] <code>n.ecModel.get("useUTC")</code>
  - [source] <code>n.get("coordinateSystem")</code>
  - [source] <code>n.get("debug")</code> (x2)
  - [source] <code>n.get("lineHeight")</code>
  - [source] <code>n.get("parallelIndex")</code>
  - [source] <code>n.get("renderMode")</code>
  - [source] <code>n.get("stack")</code> (x2)
  - [source] <code>n.get("symbolKeepAspect")</code>
  - [source] <code>n.get("verticalAlign")</code>
  - [source] <code>o.get("icon")</code>
  - [source] <code>o.get("throttle")</code>
  - [source] <code>o.get("triggerOn")</code>
  - [source] <code>o.get("useUTC")</code>
  - [source] <code>p.get("delay")</code>
  - [source] <code>p.get("easing")</code>
  - [source] <code>r.get("renderMode")</code>
  - [source] <code>r.get("useUTC")</code>
  - [source] <code>s.get("textShadowColor")</code>
  - [source] <code>s.get("textStyle")</code>
  - [source] <code>s.get("verticalAlign")</code>
  - [source] <code>t.get("containLabel")</code>
  - [source] <code>t.get("cursor")</code>
  - [source] <code>t.get("extraCssText")</code>
  - [source] <code>t.get("rotate")</code>
  - [source] <code>t.get("silent")</code>
  - [source] <code>t.get("triggerEvent")</code> (x2)
  - [source] <code>v.get("textStyle")</code>
  - [source] <code>z.get("smooth")</code>
  - [source] <code>e=new URLSearchParams(window.location.search</code>
  - [source] <code>n=new URLSearchParams(window.location.search</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/module-others-ef959ef1.js</code>
  - [sink] <code>location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/module2-ef959ef1.js</code>
  - [sink] <code>location.replace(</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@dp/suite-navigation-ef959ef1.js</code>
  - [source] <code>e.get("/v1/config")</code>
  - [source] <code>e.get("/v1/index")</code>
  - [source] <code>e.get("/v1/menu")</code>
  - [source] <code>e.get("/v1/resources")</code>
  - [source] <code>e.get("/v1/user")</code>
  - [source] <code>e.get("/v1/user/orgs")</code>
  - [source] <code>e.get("/v2/navigation_menu")</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_@teareplay/oncall-ef959ef1.js</code>
  - [source] <code>er.configManager.get("browser")</code>
  - [source] <code>er.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>er.configManager.get("user_unique_id_type")</code>
  - [source] <code>er.configManager.get("web_id")</code> (x3)
  - [source] <code>nr.configManager.get("reportErrorCallback")</code>
  - [source] <code>nr.configManager.get("user")</code> (x7)
  - [source] <code>rr.get("Content-Type")</code>
  - [source] <code>rr=new URL(location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_ad-feelgood-ef959ef1.js</code>
  - [sink] <code>window.location.href=</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_bytereplay_others-ef959ef1.js</code>
  - [source] <code>se.get("Content-Type")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendor_monaco-editor-ef959ef1.js</code>
  - [source] <code>W.get("text")</code>
  - [source] <code>m.get("3")</code>
  - [source] <code>.query.modelInfo</code> (x5)
  - [source] <code>.query.word</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bdeefe_suite-design_0_0_87_react_16_14_0_node_modules_bdeefe_suite-~b4e7e6-ef959ef1.js</code>
  - [source] <code>b=new URL(window.location.href</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytecloud_cloud-api-config_0_22_0_node_modules_bytecloud_cloud-api-~966aac-ef959ef1.js</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytecloud_common-lib_6_13_0_node_modules_bytecloud_common-lib_es_jw~1f7822-ef959ef1.js</code>
  - [source] <code>D.configManager.get("reportErrorCallback")</code>
  - [source] <code>D.configManager.get("user")</code> (x6)
  - [source] <code>I.configManager.get("reportErrorCallback")</code>
  - [source] <code>ee.configManager.get("user")</code> (x6)
  - [source] <code>h.get("csrfToken")</code>
  - [source] <code>r.collect.configManager.get("user")</code> (x2)
  - [source] <code>r.configManager.get("browser")</code>
  - [source] <code>r.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>r.configManager.get("user_unique_id_type")</code>
  - [source] <code>r.configManager.get("web_id")</code> (x3)
  - [source] <code>v.collect.configManager.get("custom")</code>
  - [source] <code>v.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>v.configManager.get("user_unique_id_type")</code>
  - [source] <code>v.configManager.get("web_id")</code> (x3)
  - [source] <code>s=new URL(location.href</code>
  - [sink] <code>location.assign(</code>
  - [sink] <code>window.location.href=</code> (x7)
  - [sink] <code>window.location.replace(</code> (x3)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_bytecloud_common-lib_7_52_0_axios_1_13_2_byted-tea-sdk_5_3_10_node_~d45cb8-ef959ef1.js</code>
  - [source] <code>r.configManager.get("reportErrorCallback")</code>
  - [source] <code>r.configManager.get("user")</code> (x7)
  - [source] <code>t.configManager.get("browser")</code>
  - [source] <code>t.configManager.get("user_unique_id")</code> (x3)
  - [source] <code>t.configManager.get("user_unique_id_type")</code>
  - [source] <code>t.configManager.get("web_id")</code> (x3)
  - [source] <code>e=new URL(location.href</code>
  - [source] <code>g=new URL(window.location.href</code>
  - [sink] <code>window.location.href=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_byted-ei_kani-js-sdk_2_0_13_node_modules_byted-ei_kani-js-sdk_lib_i~748ee1-ef959ef1.js</code>
  - [sink] <code>location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_byted_btm-web-sdk_0_2_17_node_modules_byted_btm-web-sdk_dist_src_bt~dc3136-ef959ef1.js</code>
  - [source] <code>E.styles.get("heatmap_popper_arrow")</code>
  - [source] <code>E.styles.get("heatmap_tooltip")</code>
  - [source] <code>E.styles.get("heatmap_tooltip_container")</code>
  - [source] <code>o.styles.get("heatmap_block_name")</code>
  - [source] <code>o.styles.get("heatmap_inner_block")</code>
  - [source] <code>o.styles.get("heatmap_inner_container")</code>
  - [source] <code>o.styles.get("heatmap_inner_data")</code>
  - [source] <code>o.styles.get("heatmap_inner_name")</code>
  - [source] <code>y.styles.get("heatmap_button")</code>
  - [source] <code>y.styles.get("heatmap_button_img")</code>
  - [source] <code>y.styles.get("heatmap_button_text")</code> (x2)
  - [source] <code>y.styles.get("heatmap_canvas")</code>
  - [source] <code>y.styles.get("heatmap_color_bar")</code>
  - [source] <code>y.styles.get("heatmap_divider")</code>
  - [source] <code>y.styles.get("heatmap_divider_bottom")</code>
  - [source] <code>y.styles.get("heatmap_handle_area")</code>
  - [source] <code>y.styles.get("heatmap_handle_dot")</code>
  - [source] <code>y.styles.get("heatmap_rect")</code>
  - [source] <code>y.styles.get("heatmap_toolbar_container")</code>
  - [sink] <code>window.location.href=</code>
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_css-loader_6_8_1_webpack_4_47_0_node_modules_css-loader_dist_cjs_js~94ee70-ef959ef1.js</code>
  - [source] <code>Ce.get("onEffect")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_file-saver_2_0_5_node_modules_file-saver_dist_FileSaver_min_js-ef959ef1.js</code>
  - [sink] <code>location.href=</code>
  - [sink] <code>location=</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_lark_open-widgets_1_1_7-beta_2__arco-design_web-react_2_63_0__lark_~2f61f1-ef959ef1.js</code>
  - [source] <code>o.cfg.get("reportErrorCallback")</code>
  - [source] <code>s.cfg.get("evtParams")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_react-grid-layout_1_3_4_react-dom_16_14_0_react_16_14_0_node_module~8cdb78-ef959ef1.js</code>
  - [source] <code>N.get("action")</code>
  - [source] <code>N.get("controlled")</code>
  - [source] <code>N.get("lifecycle")</code>
  - [source] <code>N.get("status")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_react-pdf_7_7_3__types_react_16_14_60_react-dom_16_14_0_react_16_14~5cf4f4-ef959ef1.js</code>
  - [source] <code>J._l10nPromise.get("editor_alt_text_button_label")</code>
  - [source] <code>J._l10nPromise.get("editor_alt_text_decorative_tooltip")</code>
  - [source] <code>J._l10nPromise.get("editor_alt_text_edit_button_label")</code>
  - [source] <code>T.AnnotationEditor._l10nPromise.get("editor_free_text2_aria_label")</code>
  - [source] <code>T.AnnotationEditor._l10nPromise.get("free_text2_default_content")</code>
  - [source] <code>n.AnnotationEditor._l10nPromise.get("editor_ink2_aria_label")</code>
  - [source] <code>n.AnnotationEditor._l10nPromise.get("editor_ink_canvas_aria_label")</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_tiptap_extension-table_3_13_0__tiptap_core_3_8_0__tiptap_pm_3_8_0_n~b8070f-ef959ef1.js</code>
  - [source] <code>f.get("defaultProtocol")</code> (x2)
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/vendors~node_modules_pnpm_volcengine-service_web-sdk_2_1_1_node_modules_volcengine-service_we~737f9a-ef959ef1.js</code>
  - [source] <code>O.default.get("csrfToken")</code>
  - [sink] <code>location.assign(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~data_font_truetype_charset_utf-8_base64_AAEAAAASAQAABAAgRkZUTYh7ieMAAB6kAAAAHEdERUYAJwAkAAAd~7223cb-ef959ef1.js</code>
  - [source] <code>e.default.get("/v1/micro_fe")</code>
  - [source] <code>g.get("crh")</code>
  - [source] <code>u.searchParams.get("event_name")</code>
  - [source] <code>u.searchParams.get("options")</code>
  - [source] <code>u.searchParams.get("with_dashboard_operation")</code>
  - [source] <code>u.searchParams.get("with_events")</code>
  - [source] <code>L=new URLSearchParams(location.search</code> (x2)
  - [source] <code>P=new URLSearchParams(window.location.search</code>
  - [source] <code>R=new URLSearchParams(window.location.search</code>
  - [source] <code>g=new URLSearchParams(location.search</code>
  - [sink] <code>location.href=</code> (x4)
  - [sink] <code>window.location.replace(</code>
- <code>https://res.gcloudcache.com/bp-fe/console-datafinder/~src_layouts_stopPageLoadCollectorProvider_tsx~src_uba-pages_session-replay_structures_sessio~639eee-ef959ef1.js</code>
  - [source] <code>N=new URLSearchParams(window.location.search</code>

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
