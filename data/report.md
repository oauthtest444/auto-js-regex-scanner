# JS Regex Scan - Short Report

- Generated: 2026-11-03 19:11:22 UTC
- Inputs: URLs <code>data/urls.txt</code> | Auth <code>data/user-A.txt</code> (2 headers, 45 cookies)
- Routes: 209 tested, 140 duplicate, 0 errors
- Files: 107 with matches | File matches: 900 | Unique texts: 629 | R1: 178 | R2: 722 | Unscanned: 0
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP

## Routes With Unique Scan Results

| # | Route | HTTP | Files | Matches | New files | New matches | Note |
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

## Unique Matched Files

Each file lists its matches once. `R1`/`R2` are the regex labels; `xN` is the occurrence count when greater than one. `first` is the first-seen route number and `routes` is the compressed loaded-on route list; both map to the table above.

<details><summary><b>1.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/echarts.ae112f35.async.js</code> - <b>230</b> matches (R1 0 / R2 230) - first 124 - routes: 124</summary>

- R2: <code>E.get("smooth")</code>
- R2: <code>I.get("show")</code> (x2)
- R2: <code>T.get("verticalAlign")</code>
- R2: <code>_.get("formatter")</code>
- R2: <code>_.get("show")</code>
- R2: <code>a.get("draggable")</code>
- R2: <code>a.get("focusNodeAdjacency")</code> (x2)
- R2: <code>a.get("ignoreForceLayout")</code>
- R2: <code>a.get("itemStyle.color")</code>
- R2: <code>a.get("label.margin")</code>
- R2: <code>a.get("lineStyle.curveness")</code>
- R2: <code>a.get("lineStyle.show")</code>
- R2: <code>a.get("show")</code> (x2)
- R2: <code>a.get("symbolSize")</code>
- R2: <code>c.get("show")</code>
- R2: <code>d.get("friction")</code>
- R2: <code>d.get("gravity")</code>
- R2: <code>d.get("parallelIndex")</code>
- R2: <code>e.ecModel.get("useUTC")</code>
- R2: <code>e.get("animation")</code> (x3)
- R2: <code>e.get("avoidLabelOverlap")</code>
- R2: <code>e.get("axisExpandRate")</code>
- R2: <code>e.get("axisLabel.inside")</code>
- R2: <code>e.get("axisLine.lineStyle.color")</code> (x3)
- R2: <code>e.get("axisTick.inside")</code>
- R2: <code>e.get("backgroundColor")</code> (x3)
- R2: <code>e.get("barMaxWidth")</code> (x2)
- R2: <code>e.get("barMinWidth")</code>
- R2: <code>e.get("barWidth")</code> (x2)
- R2: <code>e.get("borderRadius")</code>
- R2: <code>e.get("boundaryGap")</code>
- R2: <code>e.get("calendarIndex")</code>
- R2: <code>e.get("center")</code> (x3)
- R2: <code>e.get("circular.rotateLabel")</code>
- R2: <code>e.get("confine")</code>
- R2: <code>e.get("connectNulls")</code> (x2)
- R2: <code>e.get("containLabel")</code>
- R2: <code>e.get("edgeForkPosition")</code>
- R2: <code>e.get("edgeShape")</code>
- R2: <code>e.get("edgeSymbol")</code>
- R2: <code>e.get("edgeSymbolSize")</code>
- R2: <code>e.get("endAngle")</code>
- R2: <code>e.get("enterable")</code>
- R2: <code>e.get("expandAndCollapse")</code>
- R2: <code>e.get("extraCssText")</code>
- R2: <code>e.get("gradientColor")</code>
- R2: <code>e.get("hoverAnimation")</code>
- R2: <code>e.get("inverse")</code>
- R2: <code>e.get("itemGap")</code> (x3)
- R2: <code>e.get("itemSize")</code>
- R2: <code>e.get("label.align")</code>
- R2: <code>e.get("label.baseline")</code>
- R2: <code>e.get("label.verticalAlign")</code>
- R2: <code>e.get("layoutIterations")</code>
- R2: <code>e.get("legendHoverLink")</code>
- R2: <code>e.get("lineStyle.curveness")</code>
- R2: <code>e.get("max")</code> (x4)
- R2: <code>e.get("maxSize")</code>
- R2: <code>e.get("min")</code> (x4)
- R2: <code>e.get("minShowLabelAngle")</code>
- R2: <code>e.get("minSize")</code>
- R2: <code>e.get("nameMap")</code> (x2)
- R2: <code>e.get("nodeAlign")</code>
- R2: <code>e.get("orient")</code> (x2)
- R2: <code>e.get("parallelIndex")</code> (x2)
- R2: <code>e.get("radarIndex")</code>
- R2: <code>e.get("radius")</code>
- R2: <code>e.get("realtime")</code>
- R2: <code>e.get("roam")</code> (x3)
- R2: <code>e.get("scaleLimit")</code>
- R2: <code>e.get("selectedMode")</code>
- R2: <code>e.get("show")</code> (x9)
- R2: <code>e.get("showContent")</code>
- R2: <code>e.get("showLegendSymbol")</code>
- R2: <code>e.get("showTitle")</code>
- R2: <code>e.get("silent")</code> (x5)
- R2: <code>e.get("smooth")</code>
- R2: <code>e.get("smoothMonotone")</code> (x2)
- R2: <code>e.get("stack")</code> (x3)
- R2: <code>e.get("startAngle")</code> (x3)
- R2: <code>e.get("step")</code>
- R2: <code>e.get("subtarget")</code>
- R2: <code>e.get("symbol")</code> (x2)
- R2: <code>e.get("symbolMargin")</code>
- R2: <code>e.get("symbolOffset")</code>
- R2: <code>e.get("symbolRotate")</code>
- R2: <code>e.get("symbolSize")</code>
- R2: <code>e.get("target")</code>
- R2: <code>e.get("text")</code>
- R2: <code>e.get("textBaseline")</code>
- R2: <code>e.get("textVerticalAlign")</code>
- R2: <code>e.get("title.0.text")</code>
- R2: <code>e.get("triggerEvent")</code>
- R2: <code>e.get("visualDimension")</code>
- R2: <code>e.get("z")</code> (x3)
- R2: <code>e.get("zlevel")</code>
- R2: <code>e.get("zoom")</code> (x3)
- R2: <code>f.get("borderColor")</code>
- R2: <code>f.get("borderRadius")</code>
- R2: <code>f.get("borderWidth")</code>
- R2: <code>f.get("buttonColor")</code>
- R2: <code>f.get("buttonTextColor")</code>
- R2: <code>f.get("itemGap")</code>
- R2: <code>f.get("itemSize")</code>
- R2: <code>f.get("readOnly")</code>
- R2: <code>f.get("shadowBlur")</code>
- R2: <code>f.get("shadowColor")</code>
- R2: <code>f.get("shadowOffsetX")</code>
- R2: <code>f.get("shadowOffsetY")</code>
- R2: <code>f.get("show")</code>
- R2: <code>f.get("title")</code>
- R2: <code>g.get("barBorderRadius")</code>
- R2: <code>g.get("r")</code>
- R2: <code>g.get("r0")</code>
- R2: <code>h.get("renderMode")</code>
- R2: <code>i.get("axisLine.lineStyle.color")</code>
- R2: <code>i.get("icon")</code>
- R2: <code>i.get("inverse")</code>
- R2: <code>i.get("lineStyle.curveness")</code>
- R2: <code>i.get("option.bar")</code>
- R2: <code>i.get("option.line")</code>
- R2: <code>i.get("option.stack")</code>
- R2: <code>i.get("polyline")</code>
- R2: <code>i.get("show")</code> (x2)
- R2: <code>i.get("triggerEvent")</code>
- R2: <code>i.get("triggerOn")</code>
- R2: <code>l.get("label.formatter")</code>
- R2: <code>l.get("label.precision")</code>
- R2: <code>l.get("rotate")</code>
- R2: <code>m.get("axisPointer.axis")</code>
- R2: <code>m.get("show")</code>
- R2: <code>n.get("animation")</code>
- R2: <code>n.get("axisExpandTriggerOn")</code>
- R2: <code>n.get("axisExpandable")</code>
- R2: <code>n.get("backgroundColor")</code>
- R2: <code>n.get("borderRadius")</code>
- R2: <code>n.get("connectedBackgroundColor")</code>
- R2: <code>n.get("coordinateSystem")</code>
- R2: <code>n.get("dim")</code>
- R2: <code>n.get("excludeComponents")</code>
- R2: <code>n.get("hoverAnimation")</code>
- R2: <code>n.get("itemStyle.color")</code>
- R2: <code>n.get("label.formatter")</code>
- R2: <code>n.get("label.precision")</code>
- R2: <code>n.get("markLine")</code> (x2)
- R2: <code>n.get("markPoint")</code> (x2)
- R2: <code>n.get("pixelRatio")</code>
- R2: <code>n.get("rotate")</code>
- R2: <code>n.get("seriesDataIndices")</code>
- R2: <code>n.get("stack")</code> (x2)
- R2: <code>n.get("symbolRepeatDirection")</code>
- R2: <code>n.get("symbolRotate")</code>
- R2: <code>n.get("textStyle.color")</code>
- R2: <code>n.get("value")</code>
- R2: <code>n.get("z")</code>
- R2: <code>n.get("zoomLock")</code>
- R2: <code>o.get("boundaryGap")</code> (x2)
- R2: <code>o.get("emptyItemWidth")</code>
- R2: <code>o.get("focusNodeAdjacency")</code>
- R2: <code>o.get("formatterParams")</code>
- R2: <code>o.get("rotate")</code>
- R2: <code>o.get("show")</code>
- R2: <code>p.get("ellipsis")</code>
- R2: <code>r.get("borderColor")</code>
- R2: <code>r.get("dataBackgroundColor")</code>
- R2: <code>r.get("description")</code> (x2)
- R2: <code>r.get("fillerColor")</code>
- R2: <code>r.get("formatter")</code>
- R2: <code>r.get("handleIcon")</code>
- R2: <code>r.get("handleSize")</code>
- R2: <code>r.get("realtime")</code>
- R2: <code>r.get("show")</code> (x3)
- R2: <code>s.get("inside")</code> (x2)
- R2: <code>s.get("rippleEffect.period")</code>
- R2: <code>s.get("tooltip")</code>
- R2: <code>t.get("alignWithLabel")</code>
- R2: <code>t.get("axisExpandCenter")</code>
- R2: <code>t.get("axisExpandCount")</code>
- R2: <code>t.get("axisExpandDebounce")</code>
- R2: <code>t.get("axisExpandWidth")</code>
- R2: <code>t.get("axisLabel.inside")</code>
- R2: <code>t.get("axisLabel.show")</code>
- R2: <code>t.get("axisLine.lineStyle.color")</code> (x3)
- R2: <code>t.get("axisLine.show")</code>
- R2: <code>t.get("axisTick.inside")</code>
- R2: <code>t.get("backgroundColor")</code>
- R2: <code>t.get("barMaxWidth")</code>
- R2: <code>t.get("barMinWidth")</code>
- R2: <code>t.get("borderColor")</code>
- R2: <code>t.get("borderRadius")</code>
- R2: <code>t.get("borderWidth")</code>
- R2: <code>t.get("cursor")</code>
- R2: <code>t.get("delay")</code>
- R2: <code>t.get("geoCoord")</code>
- R2: <code>t.get("hoverAnimation")</code>
- R2: <code>t.get("itemGap")</code> (x2)
- R2: <code>t.get("itemStyle.color")</code>
- R2: <code>t.get("label.show")</code>
- R2: <code>t.get("maxInterval")</code>
- R2: <code>t.get("minInterval")</code>
- R2: <code>t.get("orient")</code> (x2)
- R2: <code>t.get("parallelId")</code>
- R2: <code>t.get("parallelIndex")</code> (x2)
- R2: <code>t.get("period")</code>
- R2: <code>t.get("polarId")</code>
- R2: <code>t.get("polarIndex")</code>
- R2: <code>t.get("radarIndex")</code>
- R2: <code>t.get("scaleLimit")</code>
- R2: <code>t.get("showDetail")</code>
- R2: <code>t.get("showLegendSymbol")</code>
- R2: <code>t.get("singleAxisId")</code>
- R2: <code>t.get("singleAxisIndex")</code>
- R2: <code>t.get("symbolOffset")</code>
- R2: <code>t.get("symbolRotate")</code>
- R2: <code>t.hostModel.get("percentPrecision")</code>
- R2: <code>u.get("animation")</code>
- R2: <code>u.get("hoverOffset")</code>
- R2: <code>u.get("icon")</code>
- R2: <code>u.get("selectedOffset")</code>
- R2: <code>u.get("textAlign")</code>
- R2: <code>u.get("textBackgroundColor")</code>
- R2: <code>u.get("textBorderRadius")</code>
- R2: <code>u.get("textFill")</code>
- R2: <code>u.get("textPadding")</code>
- R2: <code>u.get("textPosition")</code>
- R2: <code>u.get("throttle")</code>
- R2: <code>x.get("emphasis.label.position")</code>
- R2: <code>x.get("show")</code>
- R2: <code>y.get("dataBackgroundColor")</code>
- R2: <code>y.get("show")</code>

</details>

<details><summary><b>2.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/35680.39b89bfb.js</code> - <b>151</b> matches (R1 0 / R2 151) - first 41 - routes: 41</summary>

- R2: <code>B.get("lineWidth")</code> (x3)
- R2: <code>C.get("_order")</code> (x2)
- R2: <code>C.get("_rank")</code>
- R2: <code>Y.get("_order")</code> (x4)
- R2: <code>Y.get("_rank")</code> (x2)
- R2: <code>a.get("__source")</code> (x2)
- R2: <code>a.get("__target")</code> (x2)
- R2: <code>a.get("collapsed")</code>
- R2: <code>a.get("groupTitle")</code>
- R2: <code>a.get("lineWidth")</code>
- R2: <code>a.get("rank")</code> (x2)
- R2: <code>c.get("_editStyleCache")</code> (x2)
- R2: <code>c.get("anchors")</code>
- R2: <code>c.get("cluster")</code>
- R2: <code>c.get("len")</code>
- R2: <code>c.get("visible")</code>
- R2: <code>d.get("linkNode")</code> (x2)
- R2: <code>d.get("rank")</code>
- R2: <code>d.get("visible")</code>
- R2: <code>e.canvas.get("pixelRatio")</code>
- R2: <code>e.get("__cacheMagnetStyles")</code>
- R2: <code>e.get("_anchor")</code>
- R2: <code>e.get("_children")</code>
- R2: <code>e.get("_order")</code> (x4)
- R2: <code>e.get("anchorIndex")</code>
- R2: <code>e.get("branchCount")</code>
- R2: <code>e.get("children")</code> (x4)
- R2: <code>e.get("collapsed")</code> (x5)
- R2: <code>e.get("crossOrigin")</code>
- R2: <code>e.get("cursor")</code>
- R2: <code>e.get("dummy")</code> (x2)
- R2: <code>e.get("len")</code> (x2)
- R2: <code>e.get("lineDash")</code> (x4)
- R2: <code>e.get("linkGroupOnCollapse")</code> (x2)
- R2: <code>e.get("order")</code> (x2)
- R2: <code>e.get("originGroupId")</code>
- R2: <code>e.get("originSize")</code> (x2)
- R2: <code>e.get("originSource")</code>
- R2: <code>e.get("originTarget")</code>
- R2: <code>e.get("rank")</code> (x5)
- R2: <code>e.get("reversed")</code> (x2)
- R2: <code>e.get("source")</code> (x5)
- R2: <code>e.get("target")</code> (x5)
- R2: <code>e.graph.get("_selections")</code>
- R2: <code>e.relatedTarget.get("children")</code>
- R2: <code>g.get("rank")</code>
- R2: <code>g.get("visible")</code>
- R2: <code>h.get("container")</code> (x2)
- R2: <code>h.get("source")</code>
- R2: <code>i.get("_editStyleCache")</code>
- R2: <code>i.get("anchorIndex")</code>
- R2: <code>i.get("children")</code> (x2)
- R2: <code>i.get("collapsed")</code>
- R2: <code>i.get("groupId")</code>
- R2: <code>i.get("parent")</code>
- R2: <code>i.get("rank")</code> (x4)
- R2: <code>i.get("source")</code>
- R2: <code>i.get("sourceAnchor")</code>
- R2: <code>i.get("target")</code>
- R2: <code>i.get("targetAnchor")</code>
- R2: <code>i.layer.get("__loadingCircle")</code>
- R2: <code>l.get("linkNode")</code> (x2)
- R2: <code>l.get("rank")</code>
- R2: <code>l.get("reversed")</code>
- R2: <code>n.get("_selections")</code>
- R2: <code>n.get("collapsed")</code> (x2)
- R2: <code>n.get("container")</code>
- R2: <code>n.get("cursor")</code>
- R2: <code>n.get("dummy")</code> (x2)
- R2: <code>n.get("fontSize")</code> (x4)
- R2: <code>n.get("gapYs")</code>
- R2: <code>n.get("originGroupId")</code>
- R2: <code>n.get("originSize")</code> (x4)
- R2: <code>n.get("outerNode")</code>
- R2: <code>n.get("rank")</code> (x3)
- R2: <code>n.get("source")</code> (x6)
- R2: <code>n.get("target")</code> (x6)
- R2: <code>n.get("titleHeight")</code>
- R2: <code>o.get("_children")</code>
- R2: <code>o.get("_selections")</code>
- R2: <code>o.get("anchors")</code>
- R2: <code>o.get("attr")</code>
- R2: <code>o.get("children")</code>
- R2: <code>o.get("cluster")</code>
- R2: <code>o.get("depth")</code>
- R2: <code>o.get("rank")</code>
- R2: <code>o.get("source")</code>
- R2: <code>o.get("target")</code>
- R2: <code>r.get("_selections")</code>
- R2: <code>r.get("anchorIndex")</code>
- R2: <code>r.get("anchors")</code> (x3)
- R2: <code>r.get("children")</code>
- R2: <code>r.get("groupId")</code>
- R2: <code>r.get("minlen")</code> (x2)
- R2: <code>r.get("parent")</code>
- R2: <code>r.get("path")</code>
- R2: <code>r.get("points")</code>
- R2: <code>r.get("rank")</code> (x4)
- R2: <code>r.get("source")</code>
- R2: <code>s.get("container")</code>
- R2: <code>s.get("parent")</code>
- R2: <code>s.get("rank")</code>
- R2: <code>s.get("source")</code>
- R2: <code>s.get("target")</code> (x2)
- R2: <code>s.node.get("anchors")</code>
- R2: <code>t.canvas.get("pixelRatio")</code> (x2)
- R2: <code>t.get("_animateShow")</code> (x3)
- R2: <code>t.get("_background")</code> (x2)
- R2: <code>t.get("_children")</code>
- R2: <code>t.get("_keyShape")</code> (x10)
- R2: <code>t.get("_label")</code> (x3)
- R2: <code>t.get("_order")</code> (x2)
- R2: <code>t.get("_paste")</code> (x3)
- R2: <code>t.get("_selections")</code> (x5)
- R2: <code>t.get("animateHandler")</code>
- R2: <code>t.get("children")</code> (x2)
- R2: <code>t.get("clickInteraction")</code> (x2)
- R2: <code>t.get("collapsed")</code> (x3)
- R2: <code>t.get("controlPoints")</code>
- R2: <code>t.get("destroyed")</code>
- R2: <code>t.get("dummy")</code>
- R2: <code>t.get("encodeValue")</code> (x2)
- R2: <code>t.get("endArrow")</code>
- R2: <code>t.get("fillStyle")</code> (x3)
- R2: <code>t.get("fixed")</code>
- R2: <code>t.get("groupId")</code>
- R2: <code>t.get("groupNodes")</code>
- R2: <code>t.get("ignoreGrid")</code> (x2)
- R2: <code>t.get("mask")</code> (x2)
- R2: <code>t.get("minlen")</code>
- R2: <code>t.get("order")</code>
- R2: <code>t.get("pixelRatio")</code>
- R2: <code>t.get("rank")</code> (x9)
- R2: <code>t.get("root")</code> (x2)
- R2: <code>t.get("source")</code> (x7)
- R2: <code>t.get("startArrow")</code>
- R2: <code>t.get("target")</code> (x8)
- R2: <code>t.get("targets")</code> (x4)
- R2: <code>t.get("toDraw")</code>
- R2: <code>t.get("triggerId")</code>
- R2: <code>t.get("weight")</code>
- R2: <code>u.get("_editStyleCache")</code> (x2)
- R2: <code>u.get("children")</code>
- R2: <code>u.get("collapsed")</code>
- R2: <code>u.get("rank")</code>
- R2: <code>u.get("source")</code> (x3)
- R2: <code>u.get("sourceAnchor")</code>
- R2: <code>u.get("styles")</code>
- R2: <code>u.get("target")</code> (x4)
- R2: <code>u.get("targetAnchor")</code>
- R2: <code>v.get("rank")</code>

</details>

<details><summary><b>3.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5221.9e03eeea.js</code> - <b>137</b> matches (R1 3 / R2 134) - first 70 - routes: 70</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=o</code>
- R1: <code>location.href=t</code> (x2)
- R2: <code>A.get("lineWidth")</code> (x3)
- R2: <code>D.get("_order")</code> (x2)
- R2: <code>D.get("_rank")</code>
- R2: <code>Y.get("_order")</code> (x4)
- R2: <code>Y.get("_rank")</code> (x2)
- R2: <code>a.get("__source")</code> (x2)
- R2: <code>a.get("__target")</code> (x2)
- R2: <code>a.get("lineWidth")</code>
- R2: <code>a.get("parent")</code>
- R2: <code>c.get("container")</code>
- R2: <code>d.get("linkNode")</code> (x2)
- R2: <code>d.get("rank")</code>
- R2: <code>d.get("visible")</code>
- R2: <code>e.get("__cacheMagnetStyles")</code>
- R2: <code>e.get("_anchor")</code>
- R2: <code>e.get("_order")</code> (x4)
- R2: <code>e.get("anchorIndex")</code>
- R2: <code>e.get("children")</code> (x4)
- R2: <code>e.get("collapsed")</code> (x5)
- R2: <code>e.get("crossOrigin")</code>
- R2: <code>e.get("cursor")</code>
- R2: <code>e.get("dummy")</code> (x2)
- R2: <code>e.get("len")</code> (x2)
- R2: <code>e.get("lineDash")</code> (x4)
- R2: <code>e.get("order")</code> (x2)
- R2: <code>e.get("originGroupId")</code>
- R2: <code>e.get("originSource")</code>
- R2: <code>e.get("originTarget")</code>
- R2: <code>e.get("rank")</code> (x5)
- R2: <code>e.get("reversed")</code> (x2)
- R2: <code>e.get("source")</code> (x6)
- R2: <code>e.get("target")</code> (x6)
- R2: <code>e.get("temp")</code>
- R2: <code>e.graph.get("_selections")</code>
- R2: <code>g.get("rank")</code>
- R2: <code>h.get("anchors")</code>
- R2: <code>h.get("linkNode")</code> (x2)
- R2: <code>h.get("rank")</code>
- R2: <code>h.get("reversed")</code>
- R2: <code>i.get("_selections")</code>
- R2: <code>i.get("anchorIndex")</code>
- R2: <code>i.get("anchors")</code> (x3)
- R2: <code>i.get("groupId")</code>
- R2: <code>i.get("minlen")</code> (x2)
- R2: <code>i.get("path")</code>
- R2: <code>i.get("points")</code>
- R2: <code>i.get("rank")</code> (x2)
- R2: <code>l.get("_editStyleCache")</code> (x2)
- R2: <code>l.get("len")</code>
- R2: <code>l.node.get("anchors")</code>
- R2: <code>n.get("_selections")</code>
- R2: <code>n.get("collapsed")</code>
- R2: <code>n.get("cursor")</code>
- R2: <code>n.get("disableAnchorEvent")</code> (x2)
- R2: <code>n.get("disableNodeEvent")</code> (x2)
- R2: <code>n.get("dummy")</code> (x2)
- R2: <code>n.get("gapYs")</code>
- R2: <code>n.get("originGroupId")</code>
- R2: <code>n.get("outerNode")</code>
- R2: <code>n.get("rank")</code>
- R2: <code>n.get("source")</code> (x6)
- R2: <code>n.get("target")</code> (x6)
- R2: <code>n.get("titleHeight")</code>
- R2: <code>o.get("__baseId")</code> (x2)
- R2: <code>o.get("__count")</code>
- R2: <code>o.get("_selections")</code>
- R2: <code>o.get("anchors")</code>
- R2: <code>o.get("depth")</code>
- R2: <code>o.get("groupId")</code>
- R2: <code>o.get("rank")</code>
- R2: <code>r.get("_editStyleCache")</code>
- R2: <code>r.get("_selections")</code>
- R2: <code>r.get("anchorIndex")</code>
- R2: <code>r.get("collapsed")</code> (x2)
- R2: <code>r.get("container")</code> (x2)
- R2: <code>r.get("groupId")</code>
- R2: <code>r.get("rank")</code> (x4)
- R2: <code>r.get("source")</code>
- R2: <code>r.get("sourceAnchor")</code>
- R2: <code>r.get("target")</code>
- R2: <code>r.get("targetAnchor")</code>
- R2: <code>r.layer.get("__loadingCircle")</code>
- R2: <code>s.get("collapsed")</code> (x4)
- R2: <code>s.get("container")</code>
- R2: <code>s.get("rank")</code>
- R2: <code>s.get("source")</code>
- R2: <code>s.get("target")</code>
- R2: <code>s.get("titleSize")</code>
- R2: <code>t.get("_animateShow")</code> (x2)
- R2: <code>t.get("_background")</code> (x2)
- R2: <code>t.get("_keyShape")</code> (x10)
- R2: <code>t.get("_label")</code> (x3)
- R2: <code>t.get("_order")</code> (x2)
- R2: <code>t.get("_paste")</code> (x3)
- R2: <code>t.get("_selections")</code> (x5)
- R2: <code>t.get("animateHandler")</code>
- R2: <code>t.get("children")</code> (x3)
- R2: <code>t.get("clickInteraction")</code> (x2)
- R2: <code>t.get("collapsed")</code> (x5)
- R2: <code>t.get("controlPoints")</code>
- R2: <code>t.get("crossOrigin")</code>
- R2: <code>t.get("destroyed")</code>
- R2: <code>t.get("dummy")</code>
- R2: <code>t.get("encodeValue")</code> (x2)
- R2: <code>t.get("endArrow")</code>
- R2: <code>t.get("fillStyle")</code> (x3)
- R2: <code>t.get("fixed")</code>
- R2: <code>t.get("groupId")</code>
- R2: <code>t.get("groupNodes")</code>
- R2: <code>t.get("ignoreGrid")</code> (x3)
- R2: <code>t.get("lineWidth")</code>
- R2: <code>t.get("mask")</code>
- R2: <code>t.get("minlen")</code>
- R2: <code>t.get("order")</code>
- R2: <code>t.get("pixelRatio")</code>
- R2: <code>t.get("rank")</code> (x9)
- R2: <code>t.get("root")</code> (x2)
- R2: <code>t.get("setDefaultGroup")</code>
- R2: <code>t.get("setDefaultNode")</code>
- R2: <code>t.get("source")</code> (x7)
- R2: <code>t.get("startArrow")</code>
- R2: <code>t.get("target")</code> (x7)
- R2: <code>t.get("targets")</code> (x3)
- R2: <code>t.get("toDraw")</code>
- R2: <code>t.get("triggerId")</code>
- R2: <code>t.get("weight")</code>
- R2: <code>u.get("_editStyleCache")</code> (x2)
- R2: <code>u.get("collapsed")</code>
- R2: <code>u.get("source")</code> (x2)
- R2: <code>u.get("sourceAnchor")</code>
- R2: <code>u.get("styles")</code>
- R2: <code>u.get("target")</code> (x3)
- R2: <code>u.get("targetAnchor")</code>
- R2: <code>v.get("rank")</code>

</details>

<details><summary><b>4.</b> <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/data/dp/dataopen/mfe/1.0.0.67/index.js#2</code> - <b>58</b> matches (R1 16 / R2 42) - first 43 - routes: 43</summary>

- R1: <code>location.assign(</code>
- R1: <code>location.href=R</code>
- R1: <code>location.href=`</code> (x3)
- R1: <code>location.href=c</code> (x2)
- R1: <code>location.href=i</code>
- R1: <code>location.href=l</code>
- R1: <code>location.href=r</code>
- R1: <code>location.href=t</code>
- R1: <code>location.replace(</code>
- R1: <code>location=!</code>
- R1: <code>location=e</code> (x6)
- R1: <code>location=n</code>
- R1: <code>new URL(location.href</code>
- R1: <code>new URLSearchParams(location.search</code>
- R1: <code>window.location.assign(</code>
- R1: <code>window.location.replace(</code> (x2)
- R2: <code>Ei.get("/v1/approvals")</code>
- R2: <code>Ei.get("/v1/current_env")</code>
- R2: <code>Ei.get("/v1/current_user")</code>
- R2: <code>Ei.get("/v1/products")</code>
- R2: <code>Ei.get(`/v1${e}/catalogs`)</code>
- R2: <code>Ei.get(`/v1${e}/resources/${n}?with_package=1&amp;with_rule=1`)</code>
- R2: <code>Ei.get(`/v1${e}/resources/${n}?with_rule=1&amp;with_history=1&amp;with_package=1`)</code>
- R2: <code>Ei.get(`/v1${n}/resource_packages?with_resource=1&amp;with_app=1`)</code>
- R2: <code>Ei.get(`/v1${n}/resource_rules`)</code>
- R2: <code>Ei.get(`/v1/apps/${n}/app_packages`)</code>
- R2: <code>Ei.get(`/v1/apps/${n}/permissions`)</code>
- R2: <code>Ei.get(`/v1/apps/${n}`)</code>
- R2: <code>Ei.get(`/v1/docs/${n}`)</code>
- R2: <code>Ei.get(`/v1/permissions/authorizations/${n}`)</code>
- R2: <code>Ei.get(`/v1/products/${n}/resource_packages?with_resource=1`)</code>
- R2: <code>Fh.get("/api/v1/whoami")</code>
- R2: <code>Pve.get("/v1/user")</code>
- R2: <code>Pve.get(`/v1/users/${n}/orgs`)</code>
- R2: <code>Vp.get("_TEA_VE_APIHOST")</code>
- R2: <code>Vp.get("_TEA_VE_OPEN")</code>
- R2: <code>Vp.get("_VISUAL_EDITOR_U")</code>
- R2: <code>Vp.get("_VISUAL_EDITOR_V")</code>
- R2: <code>Vp.get("lang")</code>
- R2: <code>e.collect.configManager.get("custom")</code>
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>e.get("/v1/config")</code>
- R2: <code>e.get("/v1/console")</code>
- R2: <code>e.get("/v1/index")</code>
- R2: <code>e.get("/v1/products")</code>
- R2: <code>e.get("/v1/resources")</code>
- R2: <code>e.get("/v1/solution/industry")</code>
- R2: <code>e.get("/v1/solution/productability")</code>
- R2: <code>e.get("/v1/solution/scene_conf")</code>
- R2: <code>e.get("/v1/user")</code>
- R2: <code>e.get("/v1/user/orgs")</code>
- R2: <code>h.get("dashboardId")</code>
- R2: <code>n.get("month")</code>
- R2: <code>p.get("text")</code>
- R2: <code>r.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x6)

</details>

<details><summary><b>5.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13484.14cb09a0.js</code> - <b>27</b> matches (R1 1 / R2 26) - first 41 - routes: 41, 51, 69-71, 138-140, 196</summary>

- R1: <code>location=!</code>
- R2: <code>a.attributes.get("scriptlevel")</code>
- R2: <code>e.get("bevelled")</code> (x2)
- R2: <code>e.get("largeop")</code>
- R2: <code>e.get("linethickness")</code>
- R2: <code>e.get("mathsize")</code>
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
- R2: <code>t.attributes.get("columnalign")</code> (x2)
- R2: <code>t.attributes.get("columnspacing")</code> (x2)
- R2: <code>t.get("background-color")</code>
- R2: <code>t.get("font-family")</code>
- R2: <code>t.gullet.macros.get("\\df@tag")</code>
- R2: <code>t.macros.get("\\df@tag")</code>
- R2: <code>t.node.attributes.get("selection")</code>

</details>

<details><summary><b>6.</b> <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/vendors.7c90a73d.async.js#2</code> - <b>20</b> matches (R1 13 / R2 7) - first 121 - routes: 121</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=a</code> (x3)
- R1: <code>location.href=e</code> (x3)
- R1: <code>location.href=n</code> (x6)
- R1: <code>location.href=p</code> (x2)
- R1: <code>location.href=r</code> (x2)
- R1: <code>location.href=t</code>
- R1: <code>location.href=u</code> (x2)
- R1: <code>location=R</code>
- R1: <code>location=e</code>
- R1: <code>location=n</code>
- R1: <code>location=r</code>
- R1: <code>window.location.replace(</code> (x5)
- R2: <code>a.get("onEffect")</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x2)
- R2: <code>e.configManager.get("web_id")</code> (x2)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>n.configManager.get("user")</code> (x3)
- R2: <code>r.cfg.get("reportErrorCallback")</code>
- R2: <code>t.cfg.get("evtParams")</code>

</details>

<details><summary><b>7.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/indoc.ecc1b3c3.async.js</code> - <b>15</b> matches (R1 4 / R2 11) - first 23 - routes: 23</summary>

- R1: <code>location.href=e</code>
- R1: <code>location=!</code>
- R1: <code>location=e</code> (x6)
- R1: <code>location=n</code>
- R2: <code>e.collect.configManager.get("custom")</code>
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>fS.get("_TEA_VE_APIHOST")</code>
- R2: <code>fS.get("_VISUAL_EDITOR_U")</code>
- R2: <code>fS.get("_VISUAL_EDITOR_V")</code>
- R2: <code>fS.get("lang")</code>
- R2: <code>i.configManager.get("user")</code> (x6)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>n.get("defaultKeyword")</code>

</details>

<details><summary><b>8.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58873.975ffab2.js</code> - <b>11</b> matches (R1 7 / R2 4) - first 1 - routes: 1, 4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R1: <code>location.href="</code>
- R1: <code>location.href=`</code> (x6)
- R1: <code>location.href=a</code>
- R1: <code>location.href=t</code>
- R1: <code>location.replace(</code>
- R2: <code>eI.get(`v1/volc/orgs/${e}/operation_deadline`)</code>
- R2: <code>eP.get(`/org/${e}/operation_deadline`)</code>
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)
- R2: <code>p.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${a}`)</code>

</details>

<details><summary><b>9.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78301.2bffffc8.js</code> - <b>9</b> matches (R1 4 / R2 5) - first 70 - routes: 70</summary>

- R1: <code>location.href="</code>
- R1: <code>location.href=e</code>
- R1: <code>location.href=l</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>a.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>
- R2: <code>eP.get("/datatester/common-service/api/v3/apps/-1/app-info/filter-global-app/")</code>
- R2: <code>eP.get(`${eB}app/${e}/experiment/${t}`)</code>
- R2: <code>eP.get(`${eU}launch-review/${e}/view/${l}`)</code>
- R2: <code>eP.get(`${eU}launch-strategy/lark/groups/`)</code>

</details>

<details><summary><b>10.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75131.1f65ca18.js</code> - <b>8</b> matches (R1 7 / R2 1) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=i</code> (x2)
- R1: <code>location.href=n</code> (x4)
- R1: <code>location.href=t</code> (x4)
- R1: <code>location.replace(</code> (x3)
- R1: <code>location=n</code>
- R1: <code>window.location.replace(</code> (x5)
- R2: <code>i.get("onEffect")</code> (x2)

</details>

<details><summary><b>11.</b> <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-us/log-sdk/collect/5/collect.js</code> - <b>7</b> matches (R1 2 / R2 5) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URL(location.href</code> (x2)
- R2: <code>e.configManager.get("user_unique_id")</code> (x3)
- R2: <code>e.configManager.get("user_unique_id_type")</code>
- R2: <code>e.configManager.get("web_id")</code> (x3)
- R2: <code>n.configManager.get("reportErrorCallback")</code>
- R2: <code>r.configManager.get("user")</code> (x7)

</details>

<details><summary><b>12.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/15163.e3a9cd54.js</code> - <b>7</b> matches (R1 4 / R2 3) - first 152 - routes: 152</summary>

- R1: <code>.query.data</code>
- R1: <code>.query.isFetched</code>
- R1: <code>.query.isLoading</code>
- R1: <code>new URLSearchParams(location.search</code>
- R2: <code>ey.get(`${ex}${i}`)</code>
- R2: <code>l.get(`/datatester/metric/api/v3/${a}`)</code>
- R2: <code>l.get(`/datatester/rule/api/v3/apps/${t}/rules?type=recycle,risk,release_suggestion`)</code>

</details>

<details><summary><b>13.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74451.d9c4e483.js</code> - <b>6</b> matches (R1 1 / R2 5) - first 94 - routes: 94, 203, 207</summary>

- R1: <code>location=a</code>
- R2: <code>_.Ay.get("AttributeSelect.custom")</code>
- R2: <code>_.Ay.get("AttributeSelect.noContent1")</code>
- R2: <code>_.Ay.get("AttributeSelect.noContent2")</code>
- R2: <code>_.Ay.get("AttributeSelect.noContent3")</code>
- R2: <code>_.Ay.get("AttributeSelect.noContent4")</code>

</details>

<details><summary><b>14.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/main.590222ea.js</code> - <b>6</b> matches (R1 2 / R2 4) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.href=e</code>
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>d.get(`/v2/app/${e}/recipient/list?${o.stringify(a)}`)</code>
- R2: <code>n.A.get("x-rgw-dor")</code> (x2)
- R2: <code>n.get(`/v2/userinfo?org_id=${e}`)</code>
- R2: <code>p.get("/v2/org_list")</code>

</details>

<details><summary><b>15.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - <b>6</b> matches (R1 4 / R2 2) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=p</code>
- R1: <code>new URLSearchParams(location.search</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>i.Z.get("__spti")</code>
- R2: <code>rb.Z.get("csrfToken")</code>

</details>

<details><summary><b>16.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/36928.a3e2b85c.js</code> - <b>5</b> matches (R1 0 / R2 5) - first 36 - routes: 36</summary>

- R2: <code>na.get(`/projects/${a}/apps/ios/lookup?download_url=${encodeURIComponent(e)}`)</code>
- R2: <code>na.get(`/projects/${l}/apps/sync-res?request_id=${r}`)</code>
- R2: <code>s6.get(`${s8(i)}/industries?account_id=${r}`)</code>
- R2: <code>s6.get(`${s8(i)}/universal-materials/check?material_ids=${e}`)</code>
- R2: <code>vu.get(`/projects/${l}/channels/${e}/experiment-creation-task/${a}`)</code>

</details>

<details><summary><b>17.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/47024.049423bc.js</code> - <b>5</b> matches (R1 5 / R2 0) - first 65 - routes: 65</summary>

- R1: <code>.query.data</code>
- R1: <code>.query.isFetched</code>
- R1: <code>.query.isLoading</code>
- R1: <code>new URLSearchParams(window.location.search</code> (x4)
- R1: <code>window.location.replace(</code>

</details>

<details><summary><b>18.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5057.7330a5f2.js</code> - <b>5</b> matches (R1 0 / R2 5) - first 1 - routes: 1, 4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R2: <code>l.get(`/datatester/common-service/api/v3/apps/custom-config/${e}`)</code>
- R2: <code>l.get(`/datatester/experiment/api/v3/process/${e}/detail`)</code>
- R2: <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/${t}/brief`)</code>
- R2: <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/${t}`)</code>
- R2: <code>u.get(`/datatester/experiment/api/v3/app/${e}/review/history/${t}`)</code>

</details>

<details><summary><b>19.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/55916.fdbcf6e3.js</code> - <b>5</b> matches (R1 4 / R2 1) - first 1 - routes: 1, 4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.assign(</code>
- R1: <code>location.href=i</code>
- R1: <code>location=a</code>
- R1: <code>location=n</code>
- R2: <code>tf.A.get("csrfToken")</code>

</details>

<details><summary><b>20.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10059.beaffa2a.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 37 - routes: 37</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=p</code>
- R1: <code>location=e</code>
- R1: <code>location=p</code>

</details>

<details><summary><b>21.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56627.fe41ee2c.js</code> - <b>4</b> matches (R1 2 / R2 2) - first 41 - routes: 41, 51, 69-71, 138-140, 196</summary>

- R1: <code>location.href=`</code>
- R1: <code>new URLSearchParams(window.location.search</code> (x5)
- R2: <code>o.get("parent_manage_type")</code>
- R2: <code>s.get("/datatester/compass/api/v3/knowledge/feishu/doc/authorize")</code>

</details>

<details><summary><b>22.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59314.4e72325d.js</code> - <b>4</b> matches (R1 1 / R2 3) - first 41 - routes: 41, 51, 67, 69-72, 138-140, 196</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)
- R2: <code>a.get(`/datatester/experiment/api/v3/app/-1/experiment?page_size=9999&amp;is_holdout=1&amp;holdout_batch_id=${e}`)</code>
- R2: <code>a.get(`/datatester/experiment/api/v3/apps/${e}/holdout/holdout_batch/${t}`)</code>
- R2: <code>n.get("father_experiment_id")</code>

</details>

<details><summary><b>23.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64632.066f0760.js</code> - <b>4</b> matches (R1 1 / R2 3) - first 41 - routes: 41, 51, 69-71, 138-140, 196</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)
- R2: <code>o.get("parent_manage_type")</code>
- R2: <code>o.get(`/datatester/metric/api/v3/${l}`)</code>
- R2: <code>o.get(`/datatester/rule/api/v3/apps/${t}/rules?type=recycle,risk,release_suggestion`)</code>

</details>

<details><summary><b>24.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/68029.89f8b91b.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 110 - routes: 110</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=h</code>
- R1: <code>location=e</code>
- R1: <code>location=h</code>

</details>

<details><summary><b>25.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78728.d0dd6904.js</code> - <b>4</b> matches (R1 4 / R2 0) - first 137 - routes: 137</summary>

- R1: <code>location.href=h</code>
- R1: <code>location.href=t</code>
- R1: <code>location=h</code>
- R1: <code>location=t</code>

</details>

<details><summary><b>26.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90497.ec017806.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 47 - routes: 47</summary>

- R1: <code>.query.data</code>
- R1: <code>.query.isFetched</code>
- R1: <code>.query.isLoading</code>
- R2: <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>27.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/92238.569a7e16.js</code> - <b>4</b> matches (R1 2 / R2 2) - first 203 - routes: 203</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>T.get(`${k}/v1/apps/${e.appId}/optimization-plans/${e.planId}/subgoals`)</code>
- R2: <code>T.get(`${k}/v1/apps/${e.appId}/optimization-plans/${e.planId}`)</code>

</details>

<details><summary><b>28.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/monaco-editor.ee450aad.async.js</code> - <b>4</b> matches (R1 3 / R2 1) - first 37 - routes: 37, 41, 179, 182</summary>

- R1: <code>.query.modelInfo</code> (x7)
- R1: <code>.query.word</code> (x3)
- R1: <code>location.href=e</code>
- R2: <code>e.get("text")</code>

</details>

<details><summary><b>29.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14518.9565419e.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 13 - routes: 13</summary>

- R2: <code>u.get(`${c}/v3/app/${t.app_id}/call-source/${t.id}/access-status`)</code>
- R2: <code>u.get(`/datarangers/api/org/${t}/tester-subjects?project_id=${e}`)</code>
- R2: <code>u.get(`/datatester/org_management/api/org/${t}/tester-subjects?project_id=${e}`)</code>

</details>

<details><summary><b>30.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/14861.9dbbbb6d.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 119 - routes: 119</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>31.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/22146.69329a00.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 4 - routes: 4</summary>

- R2: <code>c.get(`/datatester/api/v2/apps/${t}/features/cohorts_open_status?feature_id=${a}&amp;version=${r}`)</code>
- R2: <code>c.get(`/datatester/api/v2/apps/${t}/flights/cohorts_open_status?flight_id=${a}`)</code>
- R2: <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>32.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28073.a2217d3f.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 41 - routes: 41, 51, 69-71, 138-140, 196</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>n.get(`${i}/template-group`)</code>
- R2: <code>s.get("parent_manage_type")</code>

</details>

<details><summary><b>33.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/28445.1e26d244.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 124 - routes: 124</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>34.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/30972.1e37cec5.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 50 - routes: 50</summary>

- R2: <code>i.get(`${c}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code>
- R2: <code>i.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code>
- R2: <code>i.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code>

</details>

<details><summary><b>35.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/41974.52459966.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 41 - routes: 41, 51, 69-71, 138-140, 175-176, 178-179, 196, 206-207</summary>

- R1: <code>.query.data</code>
- R1: <code>.query.isFetched</code>
- R1: <code>.query.isLoading</code>

</details>

<details><summary><b>36.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42269.a4a937aa.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 101 - routes: 101, 103, 207</summary>

- R1: <code>.query.charCodeAt</code> (x2)
- R1: <code>.query.length</code> (x2)
- R1: <code>.query.spec</code> (x4)

</details>

<details><summary><b>37.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/46458.0f3122db.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 101 - routes: 101</summary>

- R1: <code>.query.data</code>
- R1: <code>.query.isFetched</code>
- R1: <code>.query.isLoading</code>

</details>

<details><summary><b>38.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48001.326bc790.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 41 - routes: 41, 51, 67, 69-72, 138, 140, 196</summary>

- R1: <code>location.href=r</code>
- R1: <code>new URL(window.location.href</code>
- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>39.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5179.82af1be3.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 121 - routes: 121</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>40.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59334.99758278.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 120 - routes: 120</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>41.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6123.0837ab6d.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 1 - routes: 1, 4, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R1: <code>location.replace(</code>

</details>

<details><summary><b>42.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6153.d03c43cf.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 51 - routes: 51</summary>

- R2: <code>r.get(`${c}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code>
- R2: <code>r.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code>
- R2: <code>r.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code>

</details>

<details><summary><b>43.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/66107.93c9a306.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 13 - routes: 13</summary>

- R2: <code>o.get(`${u}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code>
- R2: <code>o.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code>
- R2: <code>o.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code>

</details>

<details><summary><b>44.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/69835.b7f0e2d2.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 32 - routes: 32</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>45.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/74094.fbf11ba1.js</code> - <b>3</b> matches (R1 3 / R2 0) - first 100 - routes: 100</summary>

- R1: <code>.query.data</code>
- R1: <code>.query.isFetched</code>
- R1: <code>.query.isLoading</code>

</details>

<details><summary><b>46.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/7454.8b7b620f.js</code> - <b>3</b> matches (R1 0 / R2 3) - first 1 - routes: 1, 4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R2: <code>o.get(`${p}/v3/app/${e.app_id}/call-source/${e.id}/access-status`)</code>
- R2: <code>o.get(`/datarangers/api/org/${e}/tester-subjects?project_id=${t}`)</code>
- R2: <code>o.get(`/datatester/org_management/api/org/${e}/tester-subjects?project_id=${t}`)</code>

</details>

<details><summary><b>47.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77520.022eb086.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 42 - routes: 42</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>48.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77845.49b14a94.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 118 - routes: 118</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>49.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/78118.efd8ad5a.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 125 - routes: 125</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>50.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/85506.5d9746e8.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 123 - routes: 123</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>51.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/87017.c29a62f1.js</code> - <b>3</b> matches (R1 1 / R2 2) - first 207 - routes: 207</summary>

- R1: <code>new URL(window.location.href</code>
- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>
- R2: <code>rZ.get(`/datatester/feature-flag/api/v4/apps/${t}/permission-check/user-tag`)</code>

</details>

<details><summary><b>52.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99979.c81dbd10.js</code> - <b>3</b> matches (R1 2 / R2 1) - first 122 - routes: 122</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)
- R2: <code>i.A.get("x-rgw-dor")</code> (x2)

</details>

<details><summary><b>53.</b> <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/dp/rangers/rangers/1.0.0.1732/static/publicParams.1ab3a298.js#2</code> - <b>2</b> matches (R1 2 / R2 0) - first 121 - routes: 121</summary>

- R1: <code>location.href=r</code>
- R1: <code>location.replace(</code>

</details>

<details><summary><b>54.</b> <code>https://lf16-data.bytepluscdn.com/obj/data-static-sg/log-sdk/collect/visual-ab-inspector.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 26 - routes: 26</summary>

- R1: <code>location=n</code>
- R1: <code>new URLSearchParams(location.search</code>

</details>

<details><summary><b>55.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/1.0.0.1528/preload.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.href=e</code> (x2)
- R1: <code>location.href=i</code>

</details>

<details><summary><b>56.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/34036.11e62fd1.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 146 - routes: 146, 148</summary>

- R1: <code>new URLSearchParams(location.search</code>
- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>57.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/38167.19428004.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 52 - routes: 52</summary>

- R1: <code>location.href=q</code> (x2)
- R2: <code>i.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>58.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40184.07ffaccf.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 41 - routes: 41, 196</summary>

- R1: <code>location.href=e</code>
- R1: <code>location=n</code>

</details>

<details><summary><b>59.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/42360.4dfa46fb.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 41 - routes: 41, 51, 69-71, 138, 140, 196</summary>

- R1: <code>location.href=`</code>
- R2: <code>o.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${t}/metrics`)</code>

</details>

<details><summary><b>60.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43762.350c7dd2.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 128 - routes: 128</summary>

- R2: <code>tq.get("/datatester/experiment/api/v3/third-take-over/system-names")</code>
- R2: <code>tq.get(`/datatester/common-service/api/v3/apps/${n}/workflow-templates/metrics-filter/${l}`)</code>

</details>

<details><summary><b>61.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/45173.ea9352cb.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 65 - routes: 65-66, 139</summary>

- R1: <code>location.href=x</code>
- R1: <code>window.location.replace(</code>

</details>

<details><summary><b>62.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/48496.5b2a454b.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 2 - routes: 2, 12, 112</summary>

- R1: <code>location.replace(</code>
- R1: <code>location=e</code>

</details>

<details><summary><b>63.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/57671.49fbaaac.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 41 - routes: 41</summary>

- R1: <code>.query.abOpConfigId</code> (x2)
- R1: <code>.query.isShowConfigPane</code> (x2)

</details>

<details><summary><b>64.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58519.f0df961e.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 2 - routes: 2, 12, 112</summary>

- R2: <code>eG.get(`${eL}v3/apps/${e}/metadata/properties`)</code>
- R2: <code>eG.get(`${eL}v3/apps/${e}/portal/role/${t}/property-desensitization`)</code>

</details>

<details><summary><b>65.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6127.02689e58.js</code> - <b>2</b> matches (R1 0 / R2 2) - first 23 - routes: 23, 41, 48, 51, 65, 67, 69-72, 101, 103, 128, 138-140, 196, 207</summary>

- R2: <code>u.get(`/datatester/api/v2/apps/${l}/features/cohorts_open_status?feature_id=${t}&amp;version=${n}`)</code>
- R2: <code>u.get(`/datatester/api/v2/apps/${l}/flights/cohorts_open_status?flight_id=${t}`)</code>

</details>

<details><summary><b>66.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61859.05b038a9.js</code> - <b>2</b> matches (R1 2 / R2 0) - first 26 - routes: 26</summary>

- R1: <code>location.href=l</code>
- R1: <code>new URLSearchParams(location.search</code> (x2)

</details>

<details><summary><b>67.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/64140.9e9ecfa7.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 139 - routes: 139</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>l.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${t}/metrics`)</code>

</details>

<details><summary><b>68.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/67872.ebb0f9c5.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 101 - routes: 101, 103</summary>

- R1: <code>new URL(window.location.href</code>
- R2: <code>r.get(`/datatester/feature-flag/api/v3/apps/${e}/permission-check/large-feature`)</code>

</details>

<details><summary><b>69.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/88928.499aa73b.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 136 - routes: 136</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x3)
- R2: <code>j.get(`/datatester/api/v2/management/apps/${e}/cronjob/settings`)</code>

</details>

<details><summary><b>70.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/90193.0fc8bf16.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 82 - routes: 82</summary>

- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>hA.get("/datatester/mutex/api/v3/layer_config")</code>

</details>

<details><summary><b>71.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/brace.e9c426df.async.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 148 - routes: 148, 151, 207</summary>

- R1: <code>location.replace(</code>
- R2: <code>o.get("packaged")</code>

</details>

<details><summary><b>72.</b> <code>https://lf-global-static.iapplogcdn.com/obj/applog-sdk-static-sg/log-sdk/collect/5/plugin/visual.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1, 4, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>new URL(window.location.href</code>

</details>

<details><summary><b>73.</b> <code>https://lf16-unpkg-i18n.byted-static.com/obj/unpkg-va/xgplayer/2.9.6/browser/index.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R1: <code>location.href=e</code>

</details>

<details><summary><b>74.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/10837.794ed6ea.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 109 - routes: 109</summary>

- R2: <code>q.get(`/v2/management/confidence_level/${t}/`)</code>

</details>

<details><summary><b>75.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/11053.6fd86b1e.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 41 - routes: 41</summary>

- R2: <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>76.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13384.373605de.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 4 - routes: 4, 41, 51, 65, 67, 69-72, 138-140, 196</summary>

- R1: <code>location.href=`</code> (x2)

</details>

<details><summary><b>77.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/13910.8de76419.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 140 - routes: 140</summary>

- R2: <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>78.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/17527.5b1fc02c.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 69 - routes: 69</summary>

- R2: <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>79.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/19362.6387ad3d.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 1 - routes: 1, 4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R2: <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>80.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/23200.177e5a97.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 176 - routes: 176</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>81.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/31062.6d254733.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 135 - routes: 135</summary>

- R2: <code>u.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${s}`)</code>

</details>

<details><summary><b>82.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/3192.4c9ba2bb.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 72 - routes: 72</summary>

- R2: <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>83.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/40287.de3b0782.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 137 - routes: 137</summary>

- R2: <code>u.get(`/v2/apps/${e}/pre_tab_task/${t}/retry`)</code>

</details>

<details><summary><b>84.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/43704.27d5aba2.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 196 - routes: 196</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>85.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4427.4a710825.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 65 - routes: 65-67, 139</summary>

- R2: <code>s.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>86.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/4806.0109974e.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 3 - routes: 3</summary>

- R2: <code>C.get("/datatester/compass/api/v3/survey/user_info")</code>

</details>

<details><summary><b>87.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50476.2b42d973.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 148 - routes: 148</summary>

- R1: <code>new URLSearchParams(location.search</code> (x2)

</details>

<details><summary><b>88.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/50481.c0109988.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 138 - routes: 138</summary>

- R2: <code>p.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>89.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/52295.90ceff7b.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 206 - routes: 206</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>90.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/53419.06fa74a6.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 81 - routes: 81</summary>

- R1: <code>.query.is_open</code>

</details>

<details><summary><b>91.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/54562.8ee76a9d.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 134 - routes: 134</summary>

- R2: <code>u.get(`/common-service/api/v3/apps/${t}/sanctum/announcement/task/${s}`)</code>

</details>

<details><summary><b>92.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/5549.81b452d5.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 65 - routes: 65-66</summary>

- R2: <code>u.get(`/datatester/objective/api/v1/apps/${e}/subgoals/${a}/metrics`)</code>

</details>

<details><summary><b>93.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/56722.95fe8edf.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 175 - routes: 175</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>94.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/58444.2ee6a332.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 148 - routes: 148, 151</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>95.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/59694.dc35e0c0.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 141 - routes: 141</summary>

- R2: <code>_.get(`/datatester/api/v2/app/${t}/cohort/${a}/refresh`)</code>

</details>

<details><summary><b>96.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61022.0272997e.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 179 - routes: 179</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>97.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/61407.d6e23ed9.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 4 - routes: 4, 41, 51, 67, 69-72, 138-140, 196</summary>

- R1: <code>window.location.replace(</code>

</details>

<details><summary><b>98.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/65247.3231c58e.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 41 - routes: 41, 51, 69-71, 138-140, 196</summary>

- R1: <code>new URLSearchParams(window.location.search</code> (x2)

</details>

<details><summary><b>99.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/6625.8405fd46.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 11 - routes: 11, 39</summary>

- R1: <code>location.href=`</code> (x5)

</details>

<details><summary><b>100.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/73667.5682fe30.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 41 - routes: 41, 51, 69-71, 138, 140, 175-176, 178-179, 196, 206-207</summary>

- R1: <code>.query.app</code>

</details>

<details><summary><b>101.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75360.0ea54511.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 4 - routes: 4, 41, 51, 67, 69-72, 138-140, 196</summary>

- R2: <code>l.get(`/datatester/experiment/api/v3/app/${e}/traffic_info/${t}`)</code>

</details>

<details><summary><b>102.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/75472.a3ebeed9.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 71 - routes: 71</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>103.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/77901.a002a061.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 178 - routes: 178</summary>

- R2: <code>n.get("/datatester/report/api/v3/baseline_flight/metric_group/meta/")</code>

</details>

<details><summary><b>104.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95783.90718b0f.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 23 - routes: 23</summary>

- R1: <code>location=0</code>

</details>

<details><summary><b>105.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/95936.3477233c.js</code> - <b>1</b> matches (R1 1 / R2 0) - first 41 - routes: 41, 51, 69-71, 138, 140, 196</summary>

- R1: <code>new URLSearchParams(window.location.search</code>

</details>

<details><summary><b>106.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/99606.9cf38234.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 40 - routes: 40</summary>

- R2: <code>M.get(`/v2/app/${n}/management/event_usage/`)</code>

</details>

<details><summary><b>107.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-dp/datatester/arco_designs.7f78af21.async.js</code> - <b>1</b> matches (R1 0 / R2 1) - first 1 - routes: 1-4, 11-13, 23, 26, 32, 36-37, 39-43, 47-48, 50-52, 65-67, 69-72, 81-82, 94, 100-101, 103, 109-110, 112, 118-125, 128, 134-141, 146, 148, 151-152, 175-176, 178-179, 182, 196, 203, 206-207</summary>

- R2: <code>t.get("month")</code>

</details>

## Duplicate Routes

140 routes skipped as duplicate results. Full mapping is in `data/scan.log`.

<details><summary>Duplicate mapping</summary>

- Route 1: 24-25, 28-31, 33-35, 38, 44-46, 49, 64, 74-79, 83-85, 90, 95-96, 105, 107-108, 111, 116-117, 147, 177, 180-181, 185-186, 188-190, 193-195
- Route 3: 7-10
- Route 4: 5-6, 14-22, 53-63, 91-93, 197
- Route 27: 88
- Route 36: 155-165
- Route 37: 166-174
- Route 40: 115
- Route 48: 80
- Route 67: 68, 86-87, 198
- Route 72: 73, 89, 199-202
- Route 94: 97-99
- Route 101: 102, 106, 133
- Route 103: 104
- Route 112: 113-114
- Route 123: 126
- Route 124: 127
- Route 128: 129-132
- Route 141: 142-145
- Route 148: 149-150
- Route 152: 153-154
- Route 182: 183-184, 187, 191-192
- Route 203: 204-205
- Route 207: 208-209

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
