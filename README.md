# Automated JS Route Regex Scanner

Runs `tools/js_route_regex_scanner.py` with Playwright Chromium on GitHub Actions.

This repository is based on the automation pattern from
`oauthtest444/test-menual-jss-redirrect-testter`: drop inputs into `data/`, let the
workflow scan, and commit the results back to `data/`.

## How to use

1. Add one route per line to `data/urls.txt`.
2. Add authentication headers/cookies to `data/user-A.txt`.
3. Commit and push your input changes, then click **Run workflow** on the
   **JS Regex Route Scan** workflow in the Actions tab.

The workflow runs:

```bash
python3 tools/js_route_regex_scanner.py \
  -l data/urls.txt \
  -h data/user-A.txt \
  -o data/report.md \
  --wait 10 \
  --timeout 20
```

`-h` means the auth-header file, not help. Use `--help` for the full CLI help.
`--timeout` is in seconds.

## Inputs

- `data/urls.txt` — target routes, one per line. Blank lines and lines starting
  with `#` are ignored. Bare domains are treated as `https://...`.
- `data/user-A.txt` — optional. Either a Burp Repeater-style raw request or plain
  header lines. Example raw request:

```http
GET / HTTP/1.1
Host: console.byteplus.com
Cookie: session=...
X-Csrf-Token: ...
```

If this file is empty, the scan runs without authentication.

## Outputs

- `data/report.md` — short Markdown report containing unique routes, unique
  matched JavaScript files, and unique regex matches. Each file is shown once in
  a collapsible section; expand it to see every match. Files with no matches are
  not listed.
- `data/scan.log` — full console output from the scan.
- `data/processed-urls.txt` — the last URL batch that was scanned.

The scanner writes the short report by default. Use `--full-report` if you need
the previous verbose layout.

After a successful scan, `data/urls.txt` is cleared to a placeholder so the next
manual run does not re-scan the same batch. The original batch is kept in
`data/processed-urls.txt`. If the scan fails, `data/urls.txt` is left unchanged
so the batch can be retried.

## Regex 2 exclusions

Regex 2 skips common property names that are not URL parameters:

`left`, `right`, `top`, `bottom`, `width`, `height`, `x`, `y`, `type`, `name`,
`length`, `size`, `index`, `id`, `class`, `className`, `style`, `color`,
`position`, `offset`, `margin`, `padding`, `display`, `direction`, `align`,
`trigger`, `series`, `data`.

Header/cache/storage `.get()` calls are also excluded by default.

## Manual console scripts

- `tools/js_route_scan_console.js` — two-regex scanner with popup.
- `tools/js_route_scan_console_regex2.js` — the one-regex console script using
  the same regex 2 exclusion set.

## Security warning

This repository is public. `data/user-A.txt` is committed and visible to
everyone. Use temporary/test credentials only, and remove or rotate them when
you are done.
