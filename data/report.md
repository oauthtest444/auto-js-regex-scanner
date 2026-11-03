# JavaScript Route Regex Scan Report

- Generated: 2026-11-03 18:17:53 UTC
- URL list: <code>data/urls.txt</code>
- Authentication: none
- Wait after navigation: 10s
- Navigation timeout: 20s
- Unique matches are counted per JavaScript file; the same match text in two files counts once per file.

## Summary

| Metric | Value |
| --- | ---: |
| Routes tested | 1 |
| Routes skipped as duplicate results | 0 |
| Routes with errors | 0 |
| Unique JavaScript files with matches | 0 |
| Unique regex matches (per file) | 0 |
| Unique match texts across files | 0 |
| Unique regex 1 matches (per file) | 0 |
| Unique regex 2 matches (per file) | 0 |
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
| 1 | <code>https://example.com</code> | 200 | 0 | 0 | 0 | 0 | final URL: https://example.com/ |

## New Discoveries by Route

### Route 1: <code>https://example.com</code>

New matched JavaScript files: none

New regex matches: none

## Unique JavaScript Files With Matches

No JavaScript files with matches were discovered.
## Skipped Duplicate Routes

No routes were skipped as duplicate results.

## Errors and Unscanned Files

No navigation, scan, or file retrieval errors were recorded.
