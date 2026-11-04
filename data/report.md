# JS Regex Scan - Short Report

- Generated: 2026-11-04 11:08:18 UTC
- Inputs: URLs <code>data/urls.txt</code> | Auth <code>data/user-A.txt</code> (2 headers, 45 cookies)
- Routes: 43 tested, 42 duplicate, 0 errors
- Files: 4 with matches | File matches: 247 | Unique texts: 247 | R1: 16 | R2: 231 | Unscanned: 0
- Wait: 10s | Timeout: 20s | Recoveries: 0 network / 0 HTTP

## Routes With Unique Scan Results

| # | Route | HTTP | Files | Matches | New files | New matches | Note |
| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | <code>https://console.byteplus.com/datarangers/app/add</code> | 200 | 4 | 247 | 4 | 247 | - |

## Unique Matched Files

Each file lists its matches once. `R1`/`R2` are the regex labels; `xN` is the occurrence count when greater than one. `first` is the first-seen route number and `routes` is the compressed loaded-on route list; both map to the table above.

<details><summary><b>1.</b> <code>https://res.gcloudcache.com/bp-fe/dp/rangers/rangers/1.0.0.2052/static/echarts@4.3.1.external.js</code> - <b>225</b> matches (R1 0 / R2 225) - first 1 - routes: 1</summary>

- R2: <code>C.get("smooth")</code>
- R2: <code>S.get("show")</code>
- R2: <code>a.get("emphasis.label.position")</code>
- R2: <code>a.get("emptyItemWidth")</code>
- R2: <code>a.get("focusNodeAdjacency")</code>
- R2: <code>a.get("formatterParams")</code>
- R2: <code>a.get("inside")</code>
- R2: <code>a.get("rippleEffect.period")</code>
- R2: <code>a.get("rotate")</code>
- R2: <code>a.get("show")</code> (x4)
- R2: <code>d.get("ellipsis")</code>
- R2: <code>e.get("axisExpandCenter")</code>
- R2: <code>e.get("axisExpandCount")</code>
- R2: <code>e.get("axisExpandDebounce")</code>
- R2: <code>e.get("axisExpandWidth")</code>
- R2: <code>e.get("axisLabel.inside")</code>
- R2: <code>e.get("axisLabel.show")</code> (x2)
- R2: <code>e.get("axisLine.lineStyle.color")</code> (x3)
- R2: <code>e.get("axisLine.show")</code>
- R2: <code>e.get("axisTick.inside")</code>
- R2: <code>e.get("axisTick.show")</code>
- R2: <code>e.get("backgroundColor")</code>
- R2: <code>e.get("borderColor")</code>
- R2: <code>e.get("borderRadius")</code>
- R2: <code>e.get("borderWidth")</code>
- R2: <code>e.get("cursor")</code>
- R2: <code>e.get("delay")</code>
- R2: <code>e.get("geoCoord")</code>
- R2: <code>e.get("hoverAnimation")</code>
- R2: <code>e.get("itemGap")</code> (x2)
- R2: <code>e.get("itemStyle.color")</code>
- R2: <code>e.get("label.show")</code>
- R2: <code>e.get("maxInterval")</code>
- R2: <code>e.get("minInterval")</code>
- R2: <code>e.get("orient")</code> (x2)
- R2: <code>e.get("parallelId")</code>
- R2: <code>e.get("parallelIndex")</code> (x2)
- R2: <code>e.get("period")</code>
- R2: <code>e.get("polarId")</code>
- R2: <code>e.get("polarIndex")</code>
- R2: <code>e.get("radarIndex")</code>
- R2: <code>e.get("radius")</code>
- R2: <code>e.get("rotate")</code>
- R2: <code>e.get("scaleLimit")</code>
- R2: <code>e.get("selectedMode")</code>
- R2: <code>e.get("show")</code>
- R2: <code>e.get("showDetail")</code>
- R2: <code>e.get("showLegendSymbol")</code>
- R2: <code>e.get("singleAxisId")</code>
- R2: <code>e.get("singleAxisIndex")</code>
- R2: <code>e.get("symbolOffset")</code>
- R2: <code>e.get("symbolRotate")</code>
- R2: <code>e.get("triggerEvent")</code>
- R2: <code>e.hostModel.get("percentPrecision")</code>
- R2: <code>f.get("itemGap")</code>
- R2: <code>f.get("itemSize")</code>
- R2: <code>f.get("show")</code>
- R2: <code>g.get("dataBackgroundColor")</code>
- R2: <code>g.get("show")</code>
- R2: <code>h.get("barBorderRadius")</code>
- R2: <code>i.get("animation")</code>
- R2: <code>i.get("axisExpandTriggerOn")</code>
- R2: <code>i.get("axisExpandable")</code>
- R2: <code>i.get("backgroundColor")</code>
- R2: <code>i.get("borderRadius")</code>
- R2: <code>i.get("boundaryGap")</code>
- R2: <code>i.get("connectedBackgroundColor")</code>
- R2: <code>i.get("coordinateSystem")</code>
- R2: <code>i.get("description")</code> (x2)
- R2: <code>i.get("dim")</code>
- R2: <code>i.get("excludeComponents")</code>
- R2: <code>i.get("hoverAnimation")</code>
- R2: <code>i.get("itemStyle.color")</code>
- R2: <code>i.get("label.formatter")</code>
- R2: <code>i.get("label.precision")</code>
- R2: <code>i.get("markLine")</code> (x2)
- R2: <code>i.get("markPoint")</code> (x2)
- R2: <code>i.get("pixelRatio")</code>
- R2: <code>i.get("seriesDataIndices")</code>
- R2: <code>i.get("show")</code>
- R2: <code>i.get("stack")</code> (x2)
- R2: <code>i.get("symbolRepeatDirection")</code>
- R2: <code>i.get("symbolRotate")</code>
- R2: <code>i.get("textStyle.color")</code>
- R2: <code>i.get("value")</code>
- R2: <code>i.get("z")</code>
- R2: <code>i.get("zoomLock")</code>
- R2: <code>m.get("formatter")</code>
- R2: <code>m.get("show")</code>
- R2: <code>n.get("buttonColor")</code>
- R2: <code>n.get("buttonTextColor")</code>
- R2: <code>n.get("icon")</code>
- R2: <code>n.get("inverse")</code>
- R2: <code>n.get("lineStyle.curveness")</code>
- R2: <code>n.get("lineStyle.show")</code>
- R2: <code>n.get("option.bar")</code>
- R2: <code>n.get("option.line")</code>
- R2: <code>n.get("option.stack")</code>
- R2: <code>n.get("option.tiled")</code>
- R2: <code>n.get("polyline")</code>
- R2: <code>n.get("readOnly")</code>
- R2: <code>n.get("show")</code> (x2)
- R2: <code>n.get("title")</code>
- R2: <code>n.get("triggerOn")</code>
- R2: <code>o.get("borderColor")</code>
- R2: <code>o.get("boundaryGap")</code>
- R2: <code>o.get("dataBackgroundColor")</code>
- R2: <code>o.get("draggable")</code>
- R2: <code>o.get("fillerColor")</code>
- R2: <code>o.get("focusNodeAdjacency")</code>
- R2: <code>o.get("formatter")</code>
- R2: <code>o.get("gravity")</code>
- R2: <code>o.get("handleIcon")</code>
- R2: <code>o.get("handleSize")</code>
- R2: <code>o.get("icon")</code>
- R2: <code>o.get("itemStyle.color")</code>
- R2: <code>o.get("realtime")</code>
- R2: <code>o.get("show")</code>
- R2: <code>o.get("symbolSize")</code>
- R2: <code>o.get("throttle")</code>
- R2: <code>p.get("r")</code>
- R2: <code>p.get("r0")</code>
- R2: <code>p.get("show")</code> (x2)
- R2: <code>r.get("animation")</code>
- R2: <code>r.get("borderColor")</code>
- R2: <code>r.get("borderRadius")</code>
- R2: <code>r.get("borderWidth")</code>
- R2: <code>r.get("hoverOffset")</code>
- R2: <code>r.get("selectedOffset")</code>
- R2: <code>r.get("shadowBlur")</code>
- R2: <code>r.get("shadowColor")</code>
- R2: <code>r.get("shadowOffsetX")</code>
- R2: <code>r.get("shadowOffsetY")</code>
- R2: <code>r.get("tooltip")</code>
- R2: <code>s.get("label.formatter")</code>
- R2: <code>s.get("label.precision")</code>
- R2: <code>s.get("show")</code>
- R2: <code>s.get("verticalAlign")</code>
- R2: <code>t.ecModel.get("useUTC")</code>
- R2: <code>t.get("animation")</code> (x3)
- R2: <code>t.get("avoidLabelOverlap")</code>
- R2: <code>t.get("axisExpandRate")</code>
- R2: <code>t.get("axisLabel.inside")</code>
- R2: <code>t.get("axisLine.lineStyle.color")</code> (x2)
- R2: <code>t.get("axisTick.inside")</code>
- R2: <code>t.get("backgroundColor")</code> (x3)
- R2: <code>t.get("barMaxWidth")</code> (x3)
- R2: <code>t.get("barMinWidth")</code>
- R2: <code>t.get("barWidth")</code> (x2)
- R2: <code>t.get("borderRadius")</code>
- R2: <code>t.get("boundaryGap")</code>
- R2: <code>t.get("calendarIndex")</code>
- R2: <code>t.get("center")</code> (x3)
- R2: <code>t.get("circular.rotateLabel")</code>
- R2: <code>t.get("confine")</code>
- R2: <code>t.get("connectNulls")</code> (x2)
- R2: <code>t.get("containLabel")</code>
- R2: <code>t.get("edgeSymbol")</code>
- R2: <code>t.get("edgeSymbolSize")</code>
- R2: <code>t.get("endAngle")</code>
- R2: <code>t.get("enterable")</code>
- R2: <code>t.get("expandAndCollapse")</code>
- R2: <code>t.get("extraCssText")</code>
- R2: <code>t.get("gradientColor")</code>
- R2: <code>t.get("hoverAnimation")</code>
- R2: <code>t.get("inverse")</code>
- R2: <code>t.get("itemGap")</code> (x3)
- R2: <code>t.get("itemSize")</code>
- R2: <code>t.get("label.align")</code>
- R2: <code>t.get("label.baseline")</code>
- R2: <code>t.get("label.verticalAlign")</code>
- R2: <code>t.get("layoutIterations")</code>
- R2: <code>t.get("legendHoverLink")</code>
- R2: <code>t.get("lineStyle.curveness")</code>
- R2: <code>t.get("max")</code> (x4)
- R2: <code>t.get("maxSize")</code>
- R2: <code>t.get("min")</code> (x4)
- R2: <code>t.get("minShowLabelAngle")</code>
- R2: <code>t.get("minSize")</code>
- R2: <code>t.get("nameMap")</code> (x2)
- R2: <code>t.get("nodeAlign")</code>
- R2: <code>t.get("orient")</code> (x3)
- R2: <code>t.get("parallelIndex")</code> (x3)
- R2: <code>t.get("pointer.show")</code>
- R2: <code>t.get("radarIndex")</code>
- R2: <code>t.get("radius")</code>
- R2: <code>t.get("realtime")</code>
- R2: <code>t.get("roam")</code> (x3)
- R2: <code>t.get("scaleLimit")</code>
- R2: <code>t.get("show")</code> (x9)
- R2: <code>t.get("showContent")</code>
- R2: <code>t.get("showLegendSymbol")</code>
- R2: <code>t.get("showTitle")</code>
- R2: <code>t.get("silent")</code> (x5)
- R2: <code>t.get("smooth")</code>
- R2: <code>t.get("smoothMonotone")</code> (x2)
- R2: <code>t.get("stack")</code> (x2)
- R2: <code>t.get("startAngle")</code> (x3)
- R2: <code>t.get("step")</code>
- R2: <code>t.get("subtarget")</code>
- R2: <code>t.get("symbol")</code> (x2)
- R2: <code>t.get("symbolMargin")</code>
- R2: <code>t.get("symbolOffset")</code>
- R2: <code>t.get("symbolRotate")</code>
- R2: <code>t.get("symbolSize")</code>
- R2: <code>t.get("target")</code>
- R2: <code>t.get("text")</code>
- R2: <code>t.get("textBaseline")</code>
- R2: <code>t.get("textVerticalAlign")</code>
- R2: <code>t.get("title.0.text")</code>
- R2: <code>t.get("triggerEvent")</code>
- R2: <code>t.get("visualDimension")</code>
- R2: <code>t.get("z")</code> (x2)
- R2: <code>t.get("zlevel")</code>
- R2: <code>t.get("zoom")</code> (x3)
- R2: <code>u.get("axisPointer.axis")</code>
- R2: <code>u.get("renderMode")</code>
- R2: <code>u.get("show")</code>
- R2: <code>u.get("textAlign")</code>
- R2: <code>u.get("textBackgroundColor")</code>
- R2: <code>u.get("textBorderRadius")</code>
- R2: <code>u.get("textFill")</code>
- R2: <code>u.get("textPadding")</code>
- R2: <code>u.get("textPosition")</code>
- R2: <code>w.get("show")</code>

</details>

<details><summary><b>2.</b> <code>https://res.gcloudcache.com/bp-fe/dp/rangers/rangers/1.0.0.2052/static/umi.61a04b83.js</code> - <b>14</b> matches (R1 11 / R2 3) - first 1 - routes: 1</summary>

- R1: <code>.query.id</code> (x2)
- R1: <code>.query.redirectURI</code>
- R1: <code>.query.roleId</code>
- R1: <code>location.href=T</code>
- R1: <code>location.href=a</code>
- R1: <code>location.href=h</code> (x2)
- R1: <code>location.href=n</code> (x2)
- R1: <code>location.href=r</code> (x3)
- R1: <code>location.href=t</code>
- R1: <code>location=r</code>
- R1: <code>window.location.replace(</code> (x7)
- R2: <code>i.get("onEffect")</code> (x2)
- R2: <code>r.cfg.get("reportErrorCallback")</code>
- R2: <code>t.cfg.get("evtParams")</code>

</details>

<details><summary><b>3.</b> <code>https://res.gcloudcache.com/bp-fe/byteplus-platform-runtime/main.e9a0251e.js</code> - <b>6</b> matches (R1 4 / R2 2) - first 1 - routes: 1</summary>

- R1: <code>location.href=e</code>
- R1: <code>location.href=p</code>
- R1: <code>new URLSearchParams(location.search</code> (x3)
- R1: <code>new URLSearchParams(window.location.search</code>
- R2: <code>i.Z.get("__spti")</code>
- R2: <code>rb.Z.get("csrfToken")</code>

</details>

<details><summary><b>4.</b> <code>https://fast.trychameleon.com/messo/S8B4hoeMzCx6ZO4iqtJgUEzG5uR78SKPb4aT3Jk24p8pdN-1JJ65m-CbIaNU9ebFFFXFK6/messo.min.js</code> - <b>2</b> matches (R1 1 / R2 1) - first 1 - routes: 1</summary>

- R1: <code>location=w</code>
- R2: <code>p.get('uid')</code>

</details>

## Duplicate Routes

42 routes skipped as duplicate results. Full mapping is in `data/scan.log`.

<details><summary>Duplicate mapping</summary>

- Route 1: 2-43

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
