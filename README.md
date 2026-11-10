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
python3 tools/js_route_regex_scanner.py -l data/urls.txt -h data/user-A.txt -o data/report.md --wait 10 --timeout 20
```

`-h` means the auth-header file, not help. Use `--help` for the full CLI help.
`--timeout` is in seconds.

### `--wait: command not found`

This error comes from the shell, not the scanner. It happens when a stray space
follows a `\` line-continuation, for example:

```bash
  -v venders.txt \<space>
  --wait 10
```

bash escapes the space, ends the command there, and then runs `--wait 10` as a
command. Run the scan on a single line (recommended), or make sure the backslash
is the last character on the line. Path arguments with accidental leading or
trailing whitespace are trimmed by the scanner and reported with a warning that
points to this cause.

## Inputs

- `data/urls.txt` — target routes, one per line. Blank lines and lines starting
  with `#` are ignored. Bare domains are treated as `https://...`. A
  `view-source:` prefix is stripped, so `view-source:https://host/path` is
  scanned as `https://host/path`.
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

- `data/report.md` — route-first Markdown report. An upper section provides a
  copy-friendly unique first-route list, followed by app route sections with
  new app JS files, app source matches, and location sinks. Vendor-only and
  no-new routes are summarized. Files with no matches are not listed.
- `data/scan.log` — full console output from the scan.
- `data/processed-urls.txt` — the last URL batch that was scanned.

The scanner writes the route-first report by default. Use `--full-report` if you
need the previous verbose layout.

After a successful scan, `data/urls.txt` is cleared to a placeholder so the next
manual run does not re-scan the same batch. The original batch is kept in
`data/processed-urls.txt`. If the scan fails, `data/urls.txt` is left unchanged
so the batch can be retried.

## Raw HTML scanning

Every visited tab has its raw HTML response body scanned with the same four
regexes, so matches inside inline scripts, inline handlers, and markup are
reported next to the JavaScript results. This is the `view-source:` payload of
each route.

- Documents are matched by response URL normalized to `scheme://host/path`
  (query and hash removed), the same collapsing used for JavaScript files.
- Identical HTML bodies are hashed with SHA-256 and scanned once; later copies
  reuse the cached matches and are reported as `identical to <url>`.
- Matches are deduped per document URL, and the route-level signature includes
  raw HTML matches, so a route that only adds HTML matches is not marked a
  duplicate.
- The report adds a `Raw HTML Documents With Matches (One-Click Copy)` block of
  `view-source:` URLs and a per-document index.
- Limits: `--max-html-bytes` (default 5000000) and `--no-html` to disable.

## Regex 1 `.get` exclusions

The `.get` source regex skips common property names that are not URL parameters:

`left`, `right`, `top`, `bottom`, `width`, `height`, `x`, `y`, `type`, `name`,
`length`, `size`, `index`, `id`, `class`, `className`, `style`, `color`,
`position`, `offset`, `margin`, `padding`, `display`, `direction`, `align`,
`trigger`, `series`, `data`.

Header/cache/storage `.get()` calls are also excluded by default.

## Manual console scripts

- `tools/js_route_scan_console.js` — four-regex scanner with popup: three
  source regexes and one location-sink regex.
- `tools/js_route_scan_console_regex2.js` — the older one-regex console script.

## Security warning

This repository is public. `data/user-A.txt` is committed and visible to
everyone. Use temporary/test credentials only, and remove or rotate them when
you are done.
