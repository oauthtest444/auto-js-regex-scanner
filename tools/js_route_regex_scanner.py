#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from collections import OrderedDict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    sys.exit("Missing dependency: requests. Install it with: pip install requests")

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit(
        "Missing dependency: playwright. Install it with: "
        "pip install playwright && python -m playwright install chromium"
    )


REGEX_1 = re.compile(
    r"""(new\s+(URLSearchParams|URL)\s*\(\s*((window\.)?location\.(search|href|hash|pathname)|document\.(URL|URLUnencoded|baseURI))|(\.query\s*\.\s*[A-Za-z_$][\w$]*|\bquery\s*\[\s*['"][^'"]+['"]\s*\])|((window\.)?location\.(assign|replace)\s*\(|\b(location|location\.href)\s*=\s*[^=]))""",
    re.ASCII,
)
REGEX_2 = re.compile(
    r"""(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])([^'"`]+)\1\s*\)""",
    re.ASCII,
)

REGEX_2_EXCLUDED_PARAM_NAMES = frozenset(
    {
        "left",
        "right",
        "top",
        "bottom",
        "width",
        "height",
        "x",
        "y",
        "type",
        "name",
        "length",
        "size",
        "index",
        "id",
        "class",
        "className",
        "style",
        "color",
        "position",
        "offset",
        "margin",
        "padding",
        "display",
        "direction",
        "align",
        "trigger",
        "series",
        "data",
    }
)

DEFAULT_EXCLUDED_MATCH_PATTERNS = [
    re.compile(r"\bheaders?\s*\.\s*get\s*\(", re.IGNORECASE),
    re.compile(r"\b(?:cache|storage|registry)\s*\.\s*get\s*\(", re.IGNORECASE),
]

DROP_REQUEST_HEADERS = {
    "host",
    "content-length",
    "connection",
    "transfer-encoding",
    "upgrade",
    "proxy-connection",
    "te",
    "trailer",
    "cookie",
    "user-agent",
    "accept-encoding",
    "priority",
}

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
)

JS_SCANNER_PATH = Path(__file__).resolve().with_name("js_route_scan_console.js")


@dataclass
class AuthConfig:
    headers: dict = field(default_factory=dict)
    cookies: dict = field(default_factory=dict)
    user_agent: str | None = None
    source: str | None = None


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        add_help=False,
        description="Scan JavaScript loaded by multiple routes and report unique regex matches.",
        epilog=(
            "Examples:\n"
            "  python3 js_route_regex_scanner.py -l urls.txt -h auth.txt -o output.md\n"
            "  python3 js_route_regex_scanner.py --help"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-l", "--list", dest="urls_file", default="urls.txt", help="URL list file (default: urls.txt)")
    parser.add_argument(
        "-h",
        "--headers",
        dest="headers_file",
        default=None,
        help="Burp Repeater header file (default: auth.txt when present)",
    )
    parser.add_argument("-o", "--output", dest="output_file", default="output.md", help="Markdown output file (default: output.md)")
    parser.add_argument("--wait", type=float, default=10.0, help="Seconds to wait after each navigation (default: 10)")
    parser.add_argument("--timeout", type=float, default=60.0, help="Navigation timeout in seconds (default: 60)")
    parser.add_argument("--headed", action="store_true", help="Run Chromium with a visible window")
    parser.add_argument("--ignore-https-errors", action="store_true", help="Ignore TLS certificate errors")
    parser.add_argument("--exclude-regex", action="append", default=[], metavar="REGEX", help="Extra match text exclusion regex (repeatable)")
    parser.add_argument("--user-agent", default=None, help="Override the browser User-Agent")
    parser.add_argument("--max-js-bytes", type=int, default=30_000_000, help="Maximum JavaScript bytes to scan per fallback fetch")
    parser.add_argument("--help", action="help", help="Show this help message and exit")
    return parser.parse_args(argv)


def load_urls(path: Path) -> tuple[list[str], int]:
    if not path.is_file():
        sys.exit(f"URL list not found: {path}")

    urls: list[str] = []
    seen: set[str] = set()
    duplicates = 0

    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "://" not in line:
            line = "https://" + line.lstrip("/")
        parsed = urlparse(line)
        if parsed.scheme not in ("http", "https") or not parsed.netloc:
            print(f"[warn] skipping invalid URL: {line}", file=sys.stderr)
            continue
        if line in seen:
            duplicates += 1
            continue
        seen.add(line)
        urls.append(line)

    return urls, duplicates


def parse_cookie_header(value: str) -> dict[str, str]:
    cookies: dict[str, str] = OrderedDict()
    for part in str(value or "").split(";"):
        part = part.strip()
        if not part or "=" not in part:
            continue
        name, cookie_value = part.split("=", 1)
        name = name.strip()
        if name:
            cookies[name] = cookie_value.strip()
    return dict(cookies)


def parse_auth_file(path: Path) -> AuthConfig:
    text = path.read_text(encoding="utf-8", errors="replace")
    raw_headers: dict[str, str] = OrderedDict()
    current_name: str | None = None
    started = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip("\r")
        if not started:
            if not line.strip():
                continue
            started = True
            if re.match(r"^[A-Z]+ \S+ HTTP/\d", line.strip()):
                continue
        if not line.strip():
            break
        if line[0] in " \t" and current_name:
            raw_headers[current_name] = f"{raw_headers[current_name]} {line.strip()}".strip()
            continue
        if ":" not in line:
            continue
        name, value = line.split(":", 1)
        name = name.strip()
        value = value.strip()
        if not name or name.startswith(":"):
            continue
        if name.lower() == "cookie" and name in raw_headers:
            raw_headers[name] = f"{raw_headers[name]}; {value}"
        else:
            raw_headers[name] = value
        current_name = name

    user_agent = None
    headers: dict[str, str] = OrderedDict()
    for name, value in raw_headers.items():
        lower_name = name.lower()
        if lower_name == "user-agent":
            user_agent = value
            continue
        if lower_name in DROP_REQUEST_HEADERS or lower_name.startswith("sec-"):
            continue
        headers[name] = value

    cookies = parse_cookie_header(raw_headers.get("Cookie", ""))
    return AuthConfig(headers=dict(headers), cookies=cookies, user_agent=user_agent, source=str(path))


def load_auth_config(args: argparse.Namespace) -> AuthConfig:
    if args.headers_file:
        path = Path(args.headers_file)
        if not path.is_file():
            sys.exit(f"Header file not found: {path}")
    else:
        path = Path("auth.txt")
        if not path.is_file():
            return AuthConfig()

    auth = parse_auth_file(path)
    if not auth.headers and not auth.cookies and not auth.user_agent:
        print(f"[warn] no usable authentication headers found in {path}", file=sys.stderr)
    return auth


def compile_exclusions(patterns: list[str]) -> list[re.Pattern[str]]:
    compiled = list(DEFAULT_EXCLUDED_MATCH_PATTERNS)
    for pattern in patterns:
        try:
            compiled.append(re.compile(pattern))
        except re.error as error:
            sys.exit(f"Invalid --exclude-regex {pattern!r}: {error}")
    return compiled


def is_excluded_param_text(regex_id: int, text: str) -> bool:
    if regex_id != 2:
        return False
    match = REGEX_2.fullmatch(text)
    return bool(match and match.group(2) in REGEX_2_EXCLUDED_PARAM_NAMES)


def scan_text_python(source: str, exclusions: list[re.Pattern[str]]) -> list[dict]:
    unique: dict[tuple[int, str], dict] = OrderedDict()
    for regex_id, pattern in ((1, REGEX_1), (2, REGEX_2)):
        for match in pattern.finditer(source):
            text = match.group(0)
            if not text:
                continue
            if any(exclusion.search(text) for exclusion in exclusions):
                continue
            if regex_id == 2 and match.group(2) in REGEX_2_EXCLUDED_PARAM_NAMES:
                continue
            key = (regex_id, text)
            existing = unique.get(key)
            if existing:
                existing["count"] += 1
            else:
                unique[key] = {"regex": regex_id, "text": text, "count": 1}
    return list(unique.values())


def normalize_matches(raw_matches: list) -> list[dict]:
    unique: dict[tuple[int, str], dict] = OrderedDict()
    for raw in raw_matches or []:
        if not isinstance(raw, dict):
            continue
        try:
            regex_id = int(raw.get("regex"))
        except (TypeError, ValueError):
            continue
        text = str(raw.get("text") or "")
        if not text:
            continue
        if is_excluded_param_text(regex_id, text):
            continue
        try:
            count = int(raw.get("count") or 1)
        except (TypeError, ValueError):
            count = 1
        key = (regex_id, text)
        existing = unique.get(key)
        if existing:
            existing["count"] = max(existing["count"], count)
        else:
            unique[key] = {"regex": regex_id, "text": text, "count": count}
    return list(unique.values())


def normalize_files(raw_files: list) -> list[dict]:
    files: dict[str, dict] = OrderedDict()
    for raw in raw_files or []:
        if not isinstance(raw, dict):
            continue
        url = str(raw.get("url") or "").strip()
        if not url:
            continue
        entry = files.setdefault(
            url,
            {"url": url, "ok": False, "error": None, "source": None, "matches": []},
        )
        if raw.get("ok"):
            entry["ok"] = True
        if raw.get("error"):
            entry["error"] = str(raw["error"])
        if raw.get("source"):
            entry["source"] = str(raw["source"])
        entry["matches"] = normalize_matches(entry["matches"] + normalize_matches(raw.get("matches") or []))
    return list(files.values())


def decode_body(data: bytes, content_type: str | None) -> str:
    encoding = "utf-8"
    if content_type:
        match = re.search(r"charset=([^;]+)", content_type, re.IGNORECASE)
        if match:
            encoding = match.group(1).strip().strip("\"'")
    try:
        return data.decode(encoding, errors="replace")
    except LookupError:
        return data.decode("utf-8", errors="replace")


def unique_captured(captured: dict) -> dict:
    seen: set[int] = set()
    result: dict[str, object] = OrderedDict()
    for url, response in captured.items():
        identity = id(response)
        if identity in seen:
            continue
        seen.add(identity)
        result[url] = response
    return result


def read_captured_body(response, max_bytes: int) -> str:
    status = getattr(response, "status", None)
    if status is not None and status >= 400:
        raise RuntimeError(f"HTTP {status}")
    data = response.body()
    if not data:
        return ""
    if len(data) > max_bytes:
        raise RuntimeError(f"body exceeds {max_bytes} bytes")
    try:
        content_type = response.headers.get("content-type")
    except Exception:
        content_type = None
    return decode_body(data, content_type)


def build_fetch_headers(
    url: str,
    route_url: str,
    auth: AuthConfig,
    user_agent: str | None,
    context,
) -> dict[str, str]:
    headers: dict[str, str] = {
        "User-Agent": user_agent or auth.user_agent or DEFAULT_USER_AGENT,
        "Accept": "*/*",
    }
    host = urlparse(url).hostname
    target_host = urlparse(route_url).hostname

    if host and target_host and host == target_host:
        headers.update(auth.headers)
        if context is not None:
            try:
                cookies = context.cookies(url)
            except Exception:
                cookies = []
            if cookies:
                headers["Cookie"] = "; ".join(f"{cookie['name']}={cookie['value']}" for cookie in cookies)
        elif auth.cookies:
            headers["Cookie"] = "; ".join(f"{name}={value}" for name, value in auth.cookies.items())

    headers.setdefault("Referer", route_url)
    return headers


def fetch_js_with_requests(
    session: requests.Session,
    url: str,
    route_url: str,
    auth: AuthConfig,
    user_agent: str | None,
    context,
    max_bytes: int,
    ignore_https_errors: bool,
) -> str:
    headers = build_fetch_headers(url, route_url, auth, user_agent, context)
    with session.get(
        url,
        headers=headers,
        timeout=30,
        verify=not ignore_https_errors,
        stream=True,
        allow_redirects=False,
    ) as response:
        if 300 <= response.status_code < 400:
            location = response.headers.get("location", "")
            raise RuntimeError(f"HTTP {response.status_code} redirect to {location}")
        if response.status_code >= 400:
            raise RuntimeError(f"HTTP {response.status_code}")
        content_type = response.headers.get("content-type")
        chunks: list[bytes] = []
        total = 0
        for chunk in response.iter_content(65536):
            if not chunk:
                continue
            total += len(chunk)
            if total > max_bytes:
                raise RuntimeError(f"body exceeds {max_bytes} bytes")
            chunks.append(chunk)
    return decode_body(b"".join(chunks), content_type)


def attach_script_capture(page) -> dict:
    captured: dict[str, object] = OrderedDict()

    def on_response(response) -> None:
        try:
            request = response.request
            if request.resource_type != "script":
                return
            captured[request.url] = response
            captured.setdefault(response.url, response)
        except Exception:
            return

    page.on("response", on_response)
    return captured


def install_auth_route(context, host: str, headers: dict[str, str]) -> None:
    def handler(route) -> None:
        try:
            request_host = urlparse(route.request.url).hostname
            if request_host == host:
                merged = dict(route.request.headers)
                merged.update(headers)
                route.continue_(headers=merged)
            else:
                route.continue_()
        except Exception:
            try:
                route.continue_()
            except Exception:
                pass

    context.route("**/*", handler)


def create_context(browser, route_url: str, args: argparse.Namespace, auth: AuthConfig):
    options = {
        "service_workers": "block",
        "ignore_https_errors": args.ignore_https_errors,
        "viewport": {"width": 1440, "height": 900},
    }
    user_agent = args.user_agent or auth.user_agent
    if user_agent:
        options["user_agent"] = user_agent

    context = browser.new_context(**options)
    host = urlparse(route_url).hostname
    route_headers = dict(auth.headers)
    if host and auth.cookies:
        cookie_values = [
            {"name": name, "value": value, "domain": host, "path": "/"}
            for name, value in auth.cookies.items()
        ]
        try:
            context.add_cookies(cookie_values)
        except Exception as error:
            print(f"[warn] could not set cookies for {host}: {error}", file=sys.stderr)
            route_headers["Cookie"] = "; ".join(f"{name}={value}" for name, value in auth.cookies.items())
    if host and route_headers:
        install_auth_route(context, host, route_headers)
    return context


def captured_fallback_files(captured: dict, exclusions: list[re.Pattern[str]], max_bytes: int) -> list[dict]:
    files: list[dict] = []
    for url, response in unique_captured(captured).items():
        entry = {"url": url, "ok": False, "error": None, "source": None, "matches": []}
        try:
            source = read_captured_body(response, max_bytes)
            entry["matches"] = scan_text_python(source, exclusions)
            entry["ok"] = True
            entry["source"] = "network-capture"
        except Exception as error:
            entry["error"] = f"captured body: {error}"
        files.append(entry)
    return files


def enrich_failed_files(
    files: list[dict],
    captured: dict,
    route_url: str,
    auth: AuthConfig,
    session: requests.Session,
    context,
    user_agent: str | None,
    args: argparse.Namespace,
    exclusions: list[re.Pattern[str]],
) -> list[dict]:
    captured_by_url = unique_captured(captured)

    for entry in files:
        if entry["ok"]:
            continue
        url = entry["url"]
        errors: list[str] = []
        source_text: str | None = None
        source_name: str | None = None

        response = captured_by_url.get(url) or captured.get(url)
        if response is not None:
            try:
                source_text = read_captured_body(response, args.max_js_bytes)
                source_name = "network-capture"
            except Exception as error:
                errors.append(f"captured body: {error}")

        if source_text is None:
            try:
                source_text = fetch_js_with_requests(
                    session,
                    url,
                    route_url,
                    auth,
                    user_agent,
                    context,
                    args.max_js_bytes,
                    args.ignore_https_errors,
                )
                source_name = "python-fetch"
            except Exception as error:
                errors.append(f"requests fetch: {error}")

        if source_text is not None:
            entry["matches"] = scan_text_python(source_text, exclusions)
            entry["ok"] = True
            entry["source"] = source_name
            entry["error"] = None
        else:
            entry["error"] = "; ".join(errors) or entry.get("error") or "fetch failed"

    return files


def scan_route(
    browser,
    route_url: str,
    args: argparse.Namespace,
    auth: AuthConfig,
    session: requests.Session,
    js_source: str,
    exclusions: list[re.Pattern[str]],
) -> dict:
    started_at = time.time()
    context = None
    page = None
    nav_error = None
    scan_error = None
    http_status = None
    title = ""
    captured: dict = OrderedDict()
    files: list[dict] = []

    try:
        context = create_context(browser, route_url, args, auth)
        page = context.new_page()
        captured = attach_script_capture(page)

        try:
            response = page.goto(route_url, wait_until="domcontentloaded", timeout=args.timeout * 1000)
            if response is not None:
                http_status = response.status
        except Exception as error:
            nav_error = f"navigation: {short_error(error)}"

        page.wait_for_timeout(max(0.0, args.wait) * 1000)

        try:
            title = page.title()
        except Exception:
            title = ""

        if args.exclude_regex:
            try:
                page.evaluate(
                    "(patterns) => { globalThis.__JS_ROUTE_SCAN_EXCLUDES__ = patterns; }",
                    args.exclude_regex,
                )
            except Exception:
                pass

        scan_result = None
        try:
            scan_result = page.evaluate(js_source)
        except Exception as error:
            scan_error = f"scanner: {short_error(error)}"

        if not isinstance(scan_result, dict) or not isinstance(scan_result.get("files"), list):
            if scan_error is None:
                scan_error = "scanner returned no result"
            files = captured_fallback_files(captured, exclusions, args.max_js_bytes)
        else:
            files = normalize_files(scan_result.get("files") or [])

        user_agent = None
        try:
            user_agent = page.evaluate("navigator.userAgent")
        except Exception:
            user_agent = None

        files = enrich_failed_files(
            files,
            captured,
            route_url,
            auth,
            session,
            context,
            user_agent,
            args,
            exclusions,
        )

        return {
            "url": route_url,
            "final_url": page.url,
            "title": title,
            "http_status": http_status,
            "nav_error": nav_error,
            "scan_error": scan_error,
            "files": files,
            "js_summary": scan_result.get("summary") if isinstance(scan_result, dict) else None,
            "duration": round(time.time() - started_at, 2),
        }
    finally:
        if context is not None:
            try:
                context.close()
            except Exception:
                pass


class ScanState:
    def __init__(self) -> None:
        self.files: dict[str, dict] = OrderedDict()
        self.match_keys: set[tuple[str, int, str]] = set()
        self.signatures: dict[str, int] = {}
        self.routes: list[dict] = []
        self.unscanned: dict[str, dict] = OrderedDict()
        self.scanned_ok: set[str] = set()
        self.skipped = 0

    def add_route(self, route: dict) -> dict:
        route["index"] = len(self.routes) + 1
        files_by_url: dict[str, dict] = OrderedDict()
        for entry in route["files"]:
            files_by_url[entry["url"]] = entry

        for url, entry in files_by_url.items():
            if entry.get("ok") or entry.get("matches"):
                self.scanned_ok.add(url)
                self.unscanned.pop(url, None)
                continue
            if url in self.scanned_ok:
                continue
            unscanned = self.unscanned.get(url)
            if unscanned is None:
                self.unscanned[url] = {
                    "url": url,
                    "first_route": route["url"],
                    "routes": [route["index"]],
                    "error": entry.get("error"),
                }
            else:
                if route["index"] not in unscanned["routes"]:
                    unscanned["routes"].append(route["index"])
                if entry.get("error"):
                    unscanned["error"] = entry["error"]

        matched_by_url: dict[str, dict] = OrderedDict(
            (url, entry) for url, entry in files_by_url.items() if entry["matches"]
        )
        file_urls = sorted(matched_by_url)
        match_entries: list[list] = []
        for url in file_urls:
            for match in sorted(matched_by_url[url]["matches"], key=lambda item: (item["regex"], item["text"])):
                match_entries.append([url, match["regex"], match["text"]])

        signature = hashlib.sha256(
            json.dumps(
                {"files": file_urls, "matches": match_entries},
                ensure_ascii=False,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()

        route["signature"] = signature
        route["total_files"] = len(file_urls)
        route["total_matches"] = len(match_entries)
        route["new_files"] = []
        route["new_matches"] = []

        has_route_error = bool(route.get("nav_error") or route.get("scan_error"))
        if not has_route_error and signature in self.signatures:
            route["status"] = "duplicate"
            route["duplicate_of"] = self.signatures[signature]
            self.skipped += 1
            self.routes.append(route)
            return route

        if not has_route_error:
            self.signatures[signature] = route["index"]
        route["status"] = "unique"
        route["duplicate_of"] = None

        for url in file_urls:
            entry = matched_by_url[url]
            if url not in self.files:
                self.files[url] = {
                    "url": url,
                    "first_route": route["url"],
                    "routes": [],
                    "matches": OrderedDict(),
                }
                route["new_files"].append(url)

            global_file = self.files[url]
            if route["index"] not in global_file["routes"]:
                global_file["routes"].append(route["index"])

            for match in sorted(entry["matches"], key=lambda item: (item["regex"], item["text"])):
                key = (url, match["regex"], match["text"])
                if key in self.match_keys:
                    continue
                self.match_keys.add(key)
                global_file["matches"][key] = {
                    "regex": match["regex"],
                    "text": match["text"],
                    "count": match["count"],
                    "first_route": route["url"],
                }
                route["new_matches"].append(
                    {
                        "url": url,
                        "regex": match["regex"],
                        "text": match["text"],
                        "count": match["count"],
                    }
                )

        self.routes.append(route)
        return route


def short_error(error) -> str:
    text = str(error).strip()
    return text.splitlines()[0] if text else error.__class__.__name__


def md_code(value, limit: int = 500) -> str:
    text = " ".join(str(value).split())
    if len(text) > limit:
        text = text[:limit] + "..."
    return "<code>" + html.escape(text, quote=False).replace("|", "&#124;") + "</code>"


def md_text(value) -> str:
    return html.escape(" ".join(str(value).split()), quote=False).replace("|", "&#124;")


def render_report(
    state: ScanState,
    meta: dict,
    args: argparse.Namespace,
    input_duplicates: int,
    auth: AuthConfig,
) -> str:
    routes_tested = len(state.routes)
    unique_files = len(state.files)
    unique_matches = len(state.match_keys)
    unique_match_texts = len({(regex_id, text) for _, regex_id, text in state.match_keys})
    regex_1_matches = sum(1 for _, regex_id, _ in state.match_keys if regex_id == 1)
    regex_2_matches = sum(1 for _, regex_id, _ in state.match_keys if regex_id == 2)
    unscanned_files = len(state.unscanned)
    routes_with_errors = sum(
        1
        for route in state.routes
        if route.get("nav_error") or route.get("scan_error") or any(not entry["ok"] for entry in route["files"])
    )
    network_capture = sum(
        1 for route in state.routes for entry in route["files"] if entry.get("source") == "network-capture"
    )
    python_fetch = sum(
        1 for route in state.routes for entry in route["files"] if entry.get("source") == "python-fetch"
    )

    lines: list[str] = []
    lines.append("# JavaScript Route Regex Scan Report")
    lines.append("")
    lines.append(f"- Generated: {meta['generated']}")
    lines.append(f"- URL list: {md_code(meta['urls_file'])}")
    if auth.source:
        header_word = "header" if len(auth.headers) == 1 else "headers"
        cookie_word = "cookie" if len(auth.cookies) == 1 else "cookies"
        lines.append(
            f"- Authentication: {md_code(auth.source)} "
            f"({len(auth.headers)} {header_word}, {len(auth.cookies)} {cookie_word})"
        )
    else:
        lines.append("- Authentication: none")
    lines.append(f"- Wait after navigation: {args.wait:g}s")
    lines.append(f"- Navigation timeout: {args.timeout:g}s")
    if input_duplicates:
        lines.append(f"- Duplicate input URLs removed before testing: {input_duplicates}")
    lines.append("- Unique matches are counted per JavaScript file; the same match text in two files counts once per file.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("| --- | ---: |")
    lines.append(f"| Routes tested | {routes_tested} |")
    lines.append(f"| Routes skipped as duplicate results | {state.skipped} |")
    lines.append(f"| Routes with errors | {routes_with_errors} |")
    lines.append(f"| Unique JavaScript files with matches | {unique_files} |")
    lines.append(f"| Unique regex matches (per file) | {unique_matches} |")
    lines.append(f"| Unique match texts across files | {unique_match_texts} |")
    lines.append(f"| Unique regex 1 matches (per file) | {regex_1_matches} |")
    lines.append(f"| Unique regex 2 matches (per file) | {regex_2_matches} |")
    lines.append(f"| JavaScript files that could not be scanned | {unscanned_files} |")
    lines.append(f"| File recoveries via network capture | {network_capture} |")
    lines.append(f"| File recoveries via Python HTTP fetch | {python_fetch} |")
    lines.append("")
    lines.append("## Regex Patterns")
    lines.append("")
    lines.append("Regex 1:")
    lines.append("")
    lines.append("```regex")
    lines.append(REGEX_1.pattern)
    lines.append("```")
    lines.append("")
    lines.append("Regex 2:")
    lines.append("")
    lines.append("```regex")
    lines.append(REGEX_2.pattern)
    lines.append("```")
    lines.append("")
    lines.append("Default match exclusions:")
    lines.append("")
    for exclusion in DEFAULT_EXCLUDED_MATCH_PATTERNS:
        lines.append(f"- {md_code(exclusion.pattern)}")
    lines.append("")
    lines.append("Regex 2 excluded parameter names:")
    lines.append("")
    lines.append(", ".join(f"`{name}`" for name in sorted(REGEX_2_EXCLUDED_PARAM_NAMES)))
    if args.exclude_regex:
        lines.append("")
        lines.append("Additional match exclusions:")
        lines.append("")
        for exclusion in args.exclude_regex:
            lines.append(f"- {md_code(exclusion)}")
    lines.append("")
    lines.append("## Routes With Unique Scan Results")
    lines.append("")
    if not any(route["status"] == "unique" for route in state.routes):
        lines.append("No routes produced unique scan results.")
    else:
        lines.append("| # | Route | HTTP | Matched JS files | Unique file matches | New JS files | New matches | Notes |")
        lines.append("| ---: | --- | ---: | ---: | ---: | ---: | ---: | --- |")
        for route in state.routes:
            if route["status"] != "unique":
                continue
            notes = []
            if route.get("nav_error"):
                notes.append(route["nav_error"])
            if route.get("scan_error"):
                notes.append(route["scan_error"])
            failed = sum(1 for entry in route["files"] if not entry["ok"])
            if failed:
                notes.append(f"{failed} file(s) could not be scanned")
            if route.get("final_url") and route["final_url"] != route["url"]:
                notes.append(f"final URL: {route['final_url']}")
            lines.append(
                f"| {route['index']} | {md_code(route['url'])} | {route.get('http_status') or '-'} | "
                f"{route['total_files']} | {route['total_matches']} | {len(route['new_files'])} | "
                f"{len(route['new_matches'])} | {md_text('; '.join(notes)) if notes else '-'} |"
            )
    lines.append("")
    lines.append("## New Discoveries by Route")
    lines.append("")
    unique_routes = [route for route in state.routes if route["status"] == "unique"]
    if not unique_routes:
        lines.append("No new JavaScript files or regex matches were discovered.")
    for route in unique_routes:
        lines.append(f"### Route {route['index']}: {md_code(route['url'])}")
        lines.append("")
        if route["new_files"]:
            lines.append("New matched JavaScript files:")
            lines.append("")
            for url in route["new_files"]:
                lines.append(f"- {md_code(url)}")
            lines.append("")
        else:
            lines.append("New matched JavaScript files: none")
            lines.append("")
        if route["new_matches"]:
            lines.append("New regex matches:")
            lines.append("")
            for match in route["new_matches"]:
                lines.append(
                    f"- {md_code(match['url'])} - [Regex {match['regex']}] "
                    f"{md_code(match['text'])} (x{match['count']})"
                )
            lines.append("")
        else:
            lines.append("New regex matches: none")
            lines.append("")
    lines.append("## Unique JavaScript Files With Matches")
    lines.append("")
    if not state.files:
        lines.append("No JavaScript files with matches were discovered.")
    for index, entry in enumerate(state.files.values(), start=1):
        lines.append(f"### {index}. {md_code(entry['url'])}")
        lines.append("")
        lines.append(f"- First seen on: {md_code(entry['first_route'])}")
        lines.append(
            "- Loaded on routes: "
            + ", ".join(str(route_index) for route_index in entry["routes"])
        )
        lines.append(f"- Unique matches: {len(entry['matches'])}")
        for match in entry["matches"].values():
            lines.append(
                f"  - [Regex {match['regex']}] {md_code(match['text'])} - "
                f"occurrences: {match['count']} - first seen on: {md_code(match['first_route'])}"
            )
        lines.append("")
    lines.append("## Skipped Duplicate Routes")
    lines.append("")
    duplicates = [route for route in state.routes if route["status"] == "duplicate"]
    if not duplicates:
        lines.append("No routes were skipped as duplicate results.")
    else:
        lines.append("| # | Route | Duplicate of route | Matched JS files | Unique file matches |")
        lines.append("| ---: | --- | ---: | ---: | ---: |")
        for route in duplicates:
            lines.append(
                f"| {route['index']} | {md_code(route['url'])} | {route['duplicate_of']} | "
                f"{route['total_files']} | {route['total_matches']} |"
            )
    lines.append("")
    lines.append("## Errors and Unscanned Files")
    lines.append("")
    error_lines: list[str] = []
    for route in state.routes:
        if route.get("nav_error"):
            error_lines.append(f"- Route {route['index']} {md_code(route['url'])}: {md_text(route['nav_error'])}")
        if route.get("scan_error"):
            error_lines.append(f"- Route {route['index']} {md_code(route['url'])}: {md_text(route['scan_error'])}")
    if unscanned_files:
        for entry in state.unscanned.values():
            error_lines.append(
                f"- File {md_code(entry['url'])} (first seen on {md_code(entry['first_route'])}): "
                "source could not be scanned"
                + (f" ({md_text(entry['error'])})" if entry.get("error") else "")
            )
    if error_lines:
        lines.extend(error_lines)
    else:
        lines.append("No navigation, scan, or file retrieval errors were recorded.")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not JS_SCANNER_PATH.is_file():
        sys.exit(f"JavaScript scanner not found: {JS_SCANNER_PATH}")

    urls, input_duplicates = load_urls(Path(args.urls_file))
    if not urls:
        sys.exit(f"No valid URLs found in {args.urls_file}")

    auth = load_auth_config(args)
    exclusions = compile_exclusions(args.exclude_regex)
    js_source = JS_SCANNER_PATH.read_text(encoding="utf-8")
    output_path = Path(args.output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    state = ScanState()
    total = len(urls)

    with sync_playwright() as playwright:
        try:
            browser = playwright.chromium.launch(
                headless=not args.headed,
                args=[
                    "--no-sandbox",
                    "--disable-setuid-sandbox",
                    "--disable-dev-shm-usage",
                ],
            )
        except Exception as error:
            sys.exit(f"Could not launch Chromium: {error}")

        try:
            for index, url in enumerate(urls, start=1):
                print(f"[{index}/{total}] {url}", flush=True)
                try:
                    route = scan_route(browser, url, args, auth, session, js_source, exclusions)
                except Exception as error:
                    route = {
                        "url": url,
                        "final_url": url,
                        "title": "",
                        "http_status": None,
                        "nav_error": f"route scan failed: {short_error(error)}",
                        "scan_error": None,
                        "files": [],
                        "js_summary": None,
                        "duration": 0,
                    }
                state.add_route(route)

                if route["status"] == "duplicate":
                    print(
                        f"  duplicate of route {route['duplicate_of']} "
                        f"({route['total_files']} matched JS files, {route['total_matches']} matches); skipped",
                        flush=True,
                    )
                else:
                    print(
                        f"  {route['total_files']} matched JS files, {route['total_matches']} unique matches, "
                        f"{len(route['new_files'])} new files, {len(route['new_matches'])} new matches "
                        f"({route['duration']}s)",
                        flush=True,
                    )
        except KeyboardInterrupt:
            print("\nInterrupted; writing partial report.", file=sys.stderr)
        finally:
            try:
                browser.close()
            except Exception:
                pass

    meta = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
        "urls_file": args.urls_file,
    }
    report = render_report(state, meta, args, input_duplicates, auth)
    output_path.write_text(report, encoding="utf-8")

    print("")
    print(f"ROUTES TESTED: {len(state.routes)}")
    print(f"ROUTES SKIPPED (DUPLICATE RESULTS): {state.skipped}")
    print(f"UNIQUE JAVASCRIPT FILES WITH MATCHES: {len(state.files)}")
    print(f"UNIQUE REGEX MATCHES: {len(state.match_keys)}")
    print(f"UNIQUE MATCH TEXTS: {len({(regex_id, text) for _, regex_id, text in state.match_keys})}")
    print(f"REPORT: {output_path.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
