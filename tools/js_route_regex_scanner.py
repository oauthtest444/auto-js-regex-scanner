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
from fnmatch import fnmatch
from pathlib import Path
from urllib.parse import urljoin, urlparse

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


REGEX_SOURCE_GET = re.compile(
    r"""(?<![=!<>])(?<![\w$.])(?!(?:this)\.)[A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*\.get\(\s*(['"`])[^'"`]+\1\s*\)""",
    re.ASCII,
)
REGEX_SOURCE_URL = re.compile(
    r"""(?<![=!<>])(?:\b[A-Za-z_$][\w$]*\s*=\s*)new\s+(?:URLSearchParams|URL)\s*\(\s*(?:(?:window\.)?location\.(?:search|href|hash|pathname)|document\.(?:URL|URLUnencoded|baseURI))\b""",
    re.ASCII,
)
REGEX_SOURCE_QUERY = re.compile(
    r"""\.query\s*\.\s*[A-Za-z_$][\w$]*|\bquery\s*\[\s*['"][^'"]+['"]\s*\]""",
    re.ASCII,
)
REGEX_SINK = re.compile(
    r"""(?:(?:window\.)?location\.(?:assign|replace)\s*\(\s*(?![`'"]|\$\{|window\.location\.|location\.|\w+\.href)|(?<![\w$.])(?:window\.|document\.|parent\.|top\.|self\.|frames\[\d+\].)??location(?:\.href)?\s*=\s*(?!=)\s*(?![\w$]+(?:\.[\w$]+)*\.href\b)(?![\w$]+(?:\.[\w$]+)*\.toString\(\))(?![`'"]|`\/|""\.concat|null\b|\{)(?!\(null\s*==[\s\S]*?this\.location[\s\S]*?\.toString\(\))(?!\(0\s*,\s*[\w$]+\.[\w$]+\)\s*\())""",
    re.ASCII,
)

SOURCE_REGEX_IDS = frozenset({1, 2, 3})
SINK_REGEX_ID = 4
REGEX_BY_ID = {
    1: REGEX_SOURCE_GET,
    2: REGEX_SOURCE_URL,
    3: REGEX_SOURCE_QUERY,
    4: REGEX_SINK,
}
REGEX_LABELS = {
    1: "`.get(...)`",
    2: "URL / URLSearchParams construction",
    3: '`.query.*` / `query["..."]`',
    4: "location sink",
}

GET_KEY_RE = re.compile(r"""\.get\(\s*(['"`])([^'"`]+)\1\s*\)""", re.ASCII)
GET_RECEIVER_RE = re.compile(r"""([A-Za-z_$][\w$]*(?:\.[A-Za-z_$][\w$]*)*)\.get\(""", re.ASCII)
URLSP_ASSIGN_RE = re.compile(
    r"""(?:(?:const|let|var)\s+)?([A-Za-z_$][\w$]*)\s*=\s*new\s+URLSearchParams\s*\(""",
    re.ASCII,
)
URL_SEARCHPARAMS_ASSIGN_RE = re.compile(
    r"""(?:(?:const|let|var)\s+)?([A-Za-z_$][\w$]*)\s*=\s*new\s+URL\s*\([^)]*\)\s*\.searchParams""",
    re.ASCII,
)
DIRECT_URLSP_GET_RE = re.compile(
    r"""new\s+URLSearchParams\s*\([^)]*\)\s*\.get\(""",
    re.ASCII,
)
DIRECT_URL_SEARCHPARAMS_GET_RE = re.compile(
    r"""new\s+URL\s*\([^)]*\)\s*\.searchParams\s*\.get\(""",
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

SCRIPT_SRC_RE = re.compile(
    r"""<script\b[^>]*\bsrc\s*=\s*(?:"([^"]+)"|'([^']+)'|([^\s>]+))""",
    re.IGNORECASE,
)
CONSOLE_BUNDLE_SEGMENT_RE = re.compile(r"^console-[a-z0-9][a-z0-9._-]*$", re.IGNORECASE)
CDN_LAYOUT_SEGMENT_RE = re.compile(r"^[a-z0-9]+-fe$", re.IGNORECASE)


def extract_script_srcs(html_text: str, base_url: str) -> list[str]:
    urls: list[str] = []
    for match in SCRIPT_SRC_RE.finditer(html_text or ""):
        raw = next((group for group in match.groups() if group), "")
        if not raw:
            continue
        try:
            absolute = urljoin(base_url, html.unescape(raw.strip()))
        except ValueError:
            continue
        if absolute.startswith(("http://", "https://")):
            urls.append(absolute)
    return urls


def product_token_from_url(url: str) -> str | None:
    segments = [segment for segment in urlparse(url).path.split("/") if segment]
    for index, segment in enumerate(segments[:-1]):
        if CDN_LAYOUT_SEGMENT_RE.match(segment):
            return segments[index + 1].lower()
    return None



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
    parser.add_argument("--full-report", action="store_true", help="Write the previous verbose report format (default: route-first)")
    parser.add_argument(
        "-v",
        "--include-vendor",
        action="store_true",
        help="Enable vendor classification and include vendor JavaScript files individually; loads URL patterns from vendors.txt",
    )
    parser.add_argument(
        "-hide",
        "--hide-vendor-index",
        action="store_true",
        dest="hide_vendor_index",
        help="Hide the per-file vendor source and sink index section",
    )
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


def resolve_vendors_file(urls_file: str) -> Path:
    candidates = [Path("vendors.txt")]
    try:
        candidates.append(Path(urls_file).resolve().parent / "vendors.txt")
    except OSError:
        pass
    candidates.append(Path(__file__).resolve().parent.parent / "vendors.txt")
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return candidates[0]


def load_vendor_patterns(enabled: bool, path: Path) -> list[str]:
    if not enabled:
        return []
    if not path.is_file():
        print(
            f"[warn] vendor pattern file not found: {path}; "
            "using built-in vendor heuristics only",
            file=sys.stderr,
        )
        return []

    patterns: list[str] = []
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        patterns.append(line)

    if not patterns:
        print(f"[warn] no vendor URL patterns found in {path}", file=sys.stderr)
    return patterns


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


def get_param_name(text: str) -> str | None:
    match = GET_KEY_RE.search(text)
    return match.group(2) if match else None


def collect_urlsp_aliases(source: str) -> set[str]:
    aliases: set[str] = set()
    for pattern in (URLSP_ASSIGN_RE, URL_SEARCHPARAMS_ASSIGN_RE):
        for match in pattern.finditer(source):
            aliases.add(match.group(1))
    return aliases


def is_urlsp_get(source: str, text: str, start: int, aliases: set[str]) -> bool:
    receiver_match = GET_RECEIVER_RE.match(text)
    if receiver_match and receiver_match.group(1) in aliases:
        return True

    prefix = source[max(0, start - 400):start] + text
    if DIRECT_URLSP_GET_RE.search(prefix):
        return True
    if DIRECT_URL_SEARCHPARAMS_GET_RE.search(prefix):
        return True
    return False


def is_excluded_param_text(regex_id: int, text: str) -> bool:
    if regex_id != 1:
        return False
    param_name = get_param_name(text)
    return bool(param_name and param_name in REGEX_2_EXCLUDED_PARAM_NAMES)


def scan_text_python(source: str, exclusions: list[re.Pattern[str]]) -> list[dict]:
    unique: dict[tuple[int, str], dict] = OrderedDict()
    urlsp_aliases = collect_urlsp_aliases(source)
    for regex_id, pattern in REGEX_BY_ID.items():
        for match in pattern.finditer(source):
            text = match.group(0)
            if not text:
                continue
            if any(exclusion.search(text) for exclusion in exclusions):
                continue
            urlsp = False
            if regex_id == 1:
                param_name = get_param_name(text)
                if param_name in REGEX_2_EXCLUDED_PARAM_NAMES:
                    continue
                urlsp = is_urlsp_get(source, text, match.start(), urlsp_aliases)
            key = (regex_id, text)
            existing = unique.get(key)
            if existing:
                existing["count"] += 1
                existing["urlsp"] = bool(existing.get("urlsp") or urlsp)
            else:
                unique[key] = {"regex": regex_id, "text": text, "count": 1, "urlsp": urlsp}
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
        urlsp = bool(raw.get("urlsp"))
        key = (regex_id, text)
        existing = unique.get(key)
        if existing:
            existing["count"] = max(existing["count"], count)
            existing["urlsp"] = bool(existing.get("urlsp") or urlsp)
        else:
            unique[key] = {"regex": regex_id, "text": text, "count": count, "urlsp": urlsp}
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

    def is_javascript_response(response) -> bool:
        request = response.request
        if request.resource_type == "script":
            return True
        path = urlparse(request.url).path.lower()
        if path.endswith(".js") or path.endswith(".mjs"):
            return True
        try:
            content_type = (response.headers or {}).get("content-type", "")
        except Exception:
            content_type = ""
        return "javascript" in content_type.lower()

    def on_response(response) -> None:
        try:
            if not is_javascript_response(response):
                return
            captured[response.request.url] = response
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
    initial_scripts: list[str] = []

    try:
        context = create_context(browser, route_url, args, auth)
        page = context.new_page()
        captured = attach_script_capture(page)

        try:
            response = page.goto(route_url, wait_until="domcontentloaded", timeout=args.timeout * 1000)
            if response is not None:
                http_status = response.status
                try:
                    initial_scripts = extract_script_srcs(response.text(), response.url)
                except Exception:
                    initial_scripts = []
        except Exception as error:
            nav_error = f"navigation: {short_error(error)}"

        try:
            dom_scripts = page.evaluate(
                "() => Array.from(document.querySelectorAll('script[src]')).map((script) => script.src)"
            )
        except Exception:
            dom_scripts = []
        for script_url in dom_scripts or []:
            if isinstance(script_url, str) and script_url not in initial_scripts:
                initial_scripts.append(script_url)

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
            "initial_scripts": initial_scripts,
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
                    "urlsp": bool(match.get("urlsp")),
                    "first_route": route["url"],
                }
                route["new_matches"].append(
                    {
                        "url": url,
                        "regex": match["regex"],
                        "text": match["text"],
                        "count": match["count"],
                        "urlsp": bool(match.get("urlsp")),
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


def render_full_report(
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
    source_matches = sum(1 for _, regex_id, _ in state.match_keys if regex_id in SOURCE_REGEX_IDS)
    sink_matches = sum(1 for _, regex_id, _ in state.match_keys if regex_id == SINK_REGEX_ID)
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
    lines.append(f"| Unique source matches (per file) | {source_matches} |")
    lines.append(f"| Unique sink matches (per file) | {sink_matches} |")
    lines.append(f"| JavaScript files that could not be scanned | {unscanned_files} |")
    lines.append(f"| File recoveries via network capture | {network_capture} |")
    lines.append(f"| File recoveries via Python HTTP fetch | {python_fetch} |")
    lines.append("")
    lines.append("## Regex Patterns")
    lines.append("")
    for regex_id, pattern in REGEX_BY_ID.items():
        lines.append(f"Regex {regex_id} ({REGEX_LABELS[regex_id]}):")
        lines.append("")
        lines.append("```regex")
        lines.append(pattern.pattern)
        lines.append("```")
        lines.append("")
    lines.append("Default match exclusions:")
    lines.append("")
    for exclusion in DEFAULT_EXCLUDED_MATCH_PATTERNS:
        lines.append(f"- {md_code(exclusion.pattern)}")
    lines.append("")
    lines.append("Excluded `.get` parameter names:")
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


def compress_route_numbers(route_numbers: list[int]) -> str:
    ordered = sorted(set(route_numbers))
    if not ordered:
        return "-"
    parts: list[str] = []
    start = previous = ordered[0]
    for number in ordered[1:]:
        if number == previous + 1:
            previous = number
            continue
        parts.append(str(start) if start == previous else f"{start}-{previous}")
        start = previous = number
    parts.append(str(start) if start == previous else f"{start}-{previous}")
    return ", ".join(parts)


VENDOR_FILE_MARKERS = (
    "vendor_",
    "vendors~",
    "node_modules",
    "echarts",
    "monaco",
    "locale-",
    "~data_font",
    "byteplus-platform-runtime",
    "instant-finder",
    "btm-web-sdk",
    "indoc",
    "teareplay",
    "kani-js-sdk",
    "open-widgets",
    "web-sdk",
)


def normalize_file_url(url: str) -> str:
    return str(url).split("#", 1)[0].split("?", 1)[0]


def matches_vendor_pattern(url: str, patterns: list[str] | tuple[str, ...] | None) -> bool:
    if not patterns:
        return False
    normalized = normalize_file_url(url)
    candidates = (str(url), normalized)
    return any(fnmatch(candidate, pattern) for pattern in patterns for candidate in candidates)


def collect_app_tokens(state: ScanState) -> set[str]:
    tokens: set[str] = set()

    def add_token(token: str | None) -> None:
        if not token:
            return
        token = token.lower()
        if CONSOLE_BUNDLE_SEGMENT_RE.match(token) or CDN_LAYOUT_SEGMENT_RE.match(token):
            tokens.add(token)
            return
        if not token.startswith(("http://", "https://")):
            tokens.add(token)

    for route in state.routes:
        route_path = urlparse(route.get("url") or "").path
        parts = [part for part in route_path.split("/") if part]
        if parts:
            slug = parts[0].lower()
            if re.fullmatch(r"[a-z0-9][a-z0-9_-]*", slug) and slug not in {"app", "org", "project"}:
                tokens.add(f"console-{slug}")

        for script_url in route.get("initial_scripts") or []:
            add_token(product_token_from_url(script_url))

        for entry in route.get("files") or []:
            for segment in urlparse(entry.get("url") or "").path.split("/"):
                segment = segment.lower()
                if CONSOLE_BUNDLE_SEGMENT_RE.match(segment):
                    tokens.add(segment)

    tokens.discard("console-app")
    tokens.discard("console-org")
    tokens.discard("console-project")
    return tokens


def is_app_url(
    url: str,
    app_tokens: set[str] | frozenset[str] = frozenset(),
    vendor_patterns: list[str] | tuple[str, ...] | None = None,
    classify_vendor: bool = True,
) -> bool:
    if not classify_vendor:
        return True
    if matches_vendor_pattern(url, vendor_patterns):
        return False
    normalized = normalize_file_url(url)
    path = urlparse(normalized).path
    name = path.rsplit("/", 1)[-1].lower()
    if ("src_" in name or "~src_" in name) and not name.startswith("vendor"):
        return True
    lowered_url = normalized.lower()
    if any(marker in lowered_url for marker in VENDOR_FILE_MARKERS):
        return False
    segments = {segment.lower() for segment in path.split("/") if segment}
    return any(token in segments for token in app_tokens)


def collapse_route_files(state: ScanState) -> "OrderedDict[str, dict]":
    collapsed: "OrderedDict[str, dict]" = OrderedDict()
    for route in state.routes:
        route_index = route["index"]
        for entry in route.get("files") or []:
            matches = entry.get("matches") or []
            if not matches:
                continue
            key = normalize_file_url(entry["url"])
            collapsed_file = collapsed.get(key)
            if collapsed_file is None:
                collapsed_file = {
                    "url": key,
                    "raw_urls": set(),
                    "first_route": route_index,
                    "routes": set(),
                    "matches": OrderedDict(),
                }
                collapsed[key] = collapsed_file
            collapsed_file["raw_urls"].add(entry["url"])
            collapsed_file["routes"].add(route_index)
            collapsed_file["first_route"] = min(collapsed_file["first_route"], route_index)

            for match in matches:
                regex_id = int(match["regex"])
                text = str(match["text"])
                urlsp = bool(match.get("urlsp"))
                match_key = (regex_id, text)
                current = collapsed_file["matches"].get(match_key)
                count = int(match.get("count") or 1)
                if current is None:
                    collapsed_file["matches"][match_key] = {
                        "regex": regex_id,
                        "text": text,
                        "urlsp": urlsp,
                        "count": count,
                        "first_route": route_index,
                    }
                else:
                    current["count"] = max(current["count"], count)
                    current["urlsp"] = bool(current["urlsp"] or urlsp)
                    current["first_route"] = min(current["first_route"], route_index)
    return collapsed


def build_source_first(collapsed: "OrderedDict[str, dict]") -> "OrderedDict[tuple, dict]":
    source_first: "OrderedDict[tuple, dict]" = OrderedDict()
    for collapsed_file in collapsed.values():
        for match in collapsed_file["matches"].values():
            if match["regex"] not in SOURCE_REGEX_IDS:
                continue
            key = (match["regex"], match["text"], match["urlsp"])
            candidate = dict(match)
            candidate["url"] = collapsed_file["url"]
            current = source_first.get(key)
            if current is None or candidate["first_route"] < current["first_route"]:
                source_first[key] = candidate
    return source_first


def build_sinks_by_route(
    state: ScanState,
    collapsed: "OrderedDict[str, dict]",
) -> "OrderedDict[int, list[dict]]":
    sinks: "OrderedDict[int, list[dict]]" = OrderedDict(
        (route["index"], []) for route in state.routes
    )
    for route in state.routes:
        route_index = route["index"]
        seen: set[tuple[str, str]] = set()
        for entry in route.get("files") or []:
            key = normalize_file_url(entry["url"])
            collapsed_file = collapsed.get(key)
            if collapsed_file is None or collapsed_file["first_route"] != route_index:
                continue
            for match in entry.get("matches") or []:
                if int(match["regex"]) != SINK_REGEX_ID:
                    continue
                sink_key = (key, str(match["text"]))
                if sink_key in seen:
                    continue
                seen.add(sink_key)
                sinks[route_index].append(
                    {
                        "url": key,
                        "regex": SINK_REGEX_ID,
                        "text": str(match["text"]),
                        "count": int(match.get("count") or 1),
                    }
                )
    return sinks


def route_note(route: dict) -> str:
    notes: list[str] = []
    if route.get("nav_error"):
        notes.append(str(route["nav_error"]))
    if route.get("scan_error"):
        notes.append(str(route["scan_error"]))
    failed = sum(1 for entry in route["files"] if not entry["ok"])
    if failed:
        notes.append(f"{failed} file(s) could not be scanned")
    if route.get("final_url") and route["final_url"] != route["url"]:
        notes.append(f"final URL: {route['final_url']}")
    return "; ".join(notes)


def render_report(
    state: ScanState,
    meta: dict,
    args: argparse.Namespace,
    input_duplicates: int,
    auth: AuthConfig,
) -> str:
    routes_tested = len(state.routes)
    unique_routes = [route for route in state.routes if route["status"] == "unique"]
    duplicates = [route for route in state.routes if route["status"] == "duplicate"]
    routes_with_errors = sum(
        1
        for route in state.routes
        if route.get("nav_error")
        or route.get("scan_error")
        or any(not entry["ok"] for entry in route["files"])
    )
    network_capture = sum(
        1 for route in state.routes for entry in route["files"] if entry.get("source") == "network-capture"
    )
    python_fetch = sum(
        1 for route in state.routes for entry in route["files"] if entry.get("source") == "python-fetch"
    )

    collapsed = collapse_route_files(state)
    source_first = build_source_first(collapsed)
    sinks_by_route = build_sinks_by_route(state, collapsed)
    app_tokens = collect_app_tokens(state)
    vendor_patterns = getattr(args, "vendor_patterns", [])

    def is_app(url: str) -> bool:
        return is_app_url(
            url,
            app_tokens,
            vendor_patterns,
            classify_vendor=args.include_vendor,
        )

    route_data: "OrderedDict[int, dict]" = OrderedDict()
    app_routes: list[dict] = []
    vendor_routes: list[dict] = []
    none_routes: list[dict] = []

    for route in unique_routes:
        route_index = route["index"]
        loaded = [entry for entry in collapsed.values() if route_index in entry["routes"]]
        new_files = [entry for entry in collapsed.values() if entry["first_route"] == route_index]
        new_app_files = sorted(
            (entry for entry in new_files if is_app(entry["url"])),
            key=lambda entry: entry["url"],
        )
        new_vendor_files = [entry for entry in new_files if not is_app(entry["url"])]
        src_new = [match for match in source_first.values() if match["first_route"] == route_index]
        sink_new = sinks_by_route.get(route_index, [])
        src_app = [match for match in src_new if is_app(match["url"])]
        src_vendor = [match for match in src_new if not is_app(match["url"])]
        sink_app = [match for match in sink_new if is_app(match["url"])]
        sink_vendor = [match for match in sink_new if not is_app(match["url"])]
        loaded_app = [entry for entry in loaded if is_app(entry["url"])]
        loaded_vendor = [entry for entry in loaded if not is_app(entry["url"])]

        app_constructions: list[dict] = []
        for entry in new_app_files:
            for match in sorted(
                entry["matches"].values(), key=lambda item: (item["regex"], item["text"])
            ):
                if match["regex"] != 2:
                    continue
                candidate = dict(match)
                candidate["url"] = entry["url"]
                app_constructions.append(candidate)

        data = {
            "loaded": loaded,
            "loaded_app": loaded_app,
            "loaded_vendor": loaded_vendor,
            "new_files": new_files,
            "new_app_files": new_app_files,
            "new_vendor_files": new_vendor_files,
            "src_app": src_app,
            "src_vendor": src_vendor,
            "sink_app": sink_app,
            "sink_vendor": sink_vendor,
            "app_constructions": app_constructions,
        }
        route_data[route_index] = data

        if new_app_files or src_app or sink_app:
            app_routes.append(route)
        elif new_files or src_vendor or sink_vendor:
            vendor_routes.append(route)
        else:
            none_routes.append(route)

    raw_match_texts = sum(len(entry["matches"]) for entry in state.files.values())
    collapsed_match_texts = sum(len(entry["matches"]) for entry in collapsed.values())
    unique_match_texts = len({(regex_id, text) for _, regex_id, text in state.match_keys})
    unique_source_matches = sum(
        1 for _, regex_id, _ in state.match_keys if regex_id in SOURCE_REGEX_IDS
    )
    unique_sink_matches = sum(
        1 for _, regex_id, _ in state.match_keys if regex_id == SINK_REGEX_ID
    )
    urlsp_matches = sum(
        1
        for entry in collapsed.values()
        for match in entry["matches"].values()
        if match["regex"] == 1 and match["urlsp"]
    )
    unscanned_files = len(state.unscanned)

    lines: list[str] = []
    lines.append("# JS Regex Scan - Route-First Report")
    lines.append("")
    lines.append(f"- Generated: {meta['generated']}")
    if input_duplicates:
        lines.append(f"- Duplicate input URLs removed before testing: {input_duplicates}")
    error_word = "error" if routes_with_errors == 1 else "errors"
    lines.append(
        f"- Routes: {routes_tested} tested | {len(unique_routes)} unique | "
        f"{len(duplicates)} duplicate | {routes_with_errors} {error_word}"
    )
    lines.append(
        f"- Route coverage: {len(app_routes)} with new app surface | "
        f"{len(vendor_routes)} vendor-only | {len(none_routes)} with no new discoveries"
    )
    lines.append(
        f"- Files: {len(collapsed)} unique JS files | {len(state.files)} raw file URLs | "
        f"{max(0, len(state.files) - len(collapsed))} cache-busted duplicates collapsed | "
        f"{collapsed_match_texts} unique file-match texts ({raw_match_texts} raw)"
    )
    lines.append(
        f"- Matches: {unique_source_matches} source | {unique_sink_matches} sink | "
        f"{urlsp_matches} URLSearchParams `.get` flagged | {unique_match_texts} unique texts"
    )
    lines.append(
        f"- Wait: {args.wait:g}s | Timeout: {args.timeout:g}s | "
        f"Recoveries: {network_capture} network / {python_fetch} HTTP | Unscanned: {unscanned_files}"
    )
    lines.append("- Only unique route IDs are listed. Missing route numbers are duplicates mapped near the end.")
    lines.append(
        "- `.get` and `.query` source matches are unique by match text within each route. "
        "URL/URLSearchParams constructions and location sinks are per file and not deduped."
    )
    lines.append("- Cache-busted duplicate URLs are collapsed by normalized URL (scheme + host + path).")
    if args.include_vendor:
        index_note = (
            "the per-file vendor index is hidden by `-hide`; vendor match texts remain in route sections."
            if args.hide_vendor_index
            else "all match texts are in the final per-file indexes."
        )
        lines.append(
            "- `App` = JavaScript served from the route's application bundle roots (for example "
            "`*/console-ark/*` or `*/console-datafinder/*`), plus legacy `src_`/`~src_` chunks. "
            "Vendor, runtime, locale, and SDK markers plus `vendors.txt` URL patterns mark vendor "
            f"files, which are listed individually per route; {index_note}"
        )
    else:
        lines.append(
            "- Vendor classification is disabled without `-v`: all matched JavaScript files are "
            "treated as app surface and included under route sections. Use `-v` to enable vendor "
            "classification via built-in markers and `vendors.txt` URL patterns."
        )
    lines.append(
        "- URLSearchParams `.get` classification uses a same-file constructor/alias heuristic; "
        "function-parameter and cross-file flows still need manual tracing."
    )
    lines.append("")

    lines.append("## Unique Routes (One-Click Copy)")
    lines.append("")
    route_word = "route" if len(unique_routes) == 1 else "routes"
    lines.append(
        f"{len(unique_routes)} unique {route_word}. Copy the complete block below; "
        "each line is a full unique route URL."
    )
    lines.append("")
    lines.append("```text")
    for route in unique_routes:
        lines.append(route["url"])
    lines.append("```")
    lines.append("")

    detail_routes = list(app_routes)
    if args.include_vendor:
        detail_routes.extend(vendor_routes)
        detail_routes.sort(key=lambda route: route["index"])

    for route in detail_routes:
        route_index = route["index"]
        data = route_data[route_index]
        lines.append(f"## Route {route_index} — {route['url']}")
        lines.append("")
        lines.append(
            f"- HTTP: {route.get('http_status') or '-'} | "
            f"Loaded: {len(data['loaded'])} files ({len(data['loaded_app'])} app / "
            f"{len(data['loaded_vendor'])} vendor) | "
            f"New: {len(data['new_files'])} files ({len(data['new_app_files'])} app / "
            f"{len(data['new_vendor_files'])} vendor)"
        )
        lines.append(
            f"- New source matches: {len(data['src_app'])} app / {len(data['src_vendor'])} vendor | "
            f"New location sinks: {len(data['sink_app'])} app / {len(data['sink_vendor'])} vendor"
        )
        note = route_note(route)
        if note:
            lines.append(f"- Note: {md_text(note)}")
        lines.append("")

        if data["new_app_files"]:
            lines.append("### New app JS files")
            lines.append("")
            for entry in data["new_app_files"]:
                lines.append(f"- {md_code(entry['url'])}")
            lines.append("")

        groups: dict[str, list[dict]] = {"urlsp": [], "query": [], "get": []}
        for match in data["src_app"]:
            if match["regex"] == 1:
                groups["urlsp" if match["urlsp"] else "get"].append(match)
            elif match["regex"] == 3:
                groups["query"].append(match)

        has_source_section = bool(
            groups["urlsp"] or groups["query"] or groups["get"] or data["app_constructions"]
        )
        if has_source_section:
            lines.append("### App source matches (unique)")
            lines.append("")
            for group_key, label in (
                ("urlsp", "URLSearchParams `.get(...)`"),
                ("query", '`.query.*` / `query["..."]`'),
            ):
                group = sorted(groups[group_key], key=lambda match: match["text"])
                if not group:
                    continue
                lines.append(f"#### {label}")
                lines.append("")
                for match in group:
                    suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                    lines.append(
                        f"- {md_code(match['text'])}{suffix} — {md_code(match['url'])}"
                    )
                lines.append("")

            constructions = sorted(
                data["app_constructions"], key=lambda match: (match["url"], match["text"])
            )
            if constructions:
                lines.append("#### URL / URLSearchParams construction (not deduped)")
                lines.append("")
                for match in constructions:
                    suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                    lines.append(
                        f"- {md_code(match['text'])}{suffix} — {md_code(match['url'])}"
                    )
                lines.append("")

            generic_get = sorted(groups["get"], key=lambda match: match["text"])
            if generic_get:
                lines.append(f'#### Other `.get(...)` ({len(generic_get)})')
                lines.append("")
                lines.append("<details><summary>Show generic .get matches</summary>")
                lines.append("")
                for match in generic_get:
                    suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                    lines.append(
                        f"- {md_code(match['text'])}{suffix} — {md_code(match['url'])}"
                    )
                lines.append("")
                lines.append("</details>")
                lines.append("")

        if data["sink_app"]:
            lines.append("### Location sinks (not deduped)")
            lines.append("")
            for match in data["sink_app"]:
                suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                lines.append(f"- {md_code(match['text'])}{suffix} — {md_code(match['url'])}")
            lines.append("")

        if args.include_vendor:
            if data["new_vendor_files"] or data["src_vendor"] or data["sink_vendor"]:
                lines.append("### Vendor JS files (included by -v)")
                lines.append("")
                if data["new_vendor_files"]:
                    for entry in sorted(data["new_vendor_files"], key=lambda item: item["url"]):
                        lines.append(f"- {md_code(entry['url'])}")
                        for match in sorted(
                            entry["matches"].values(),
                            key=lambda item: (item["regex"], item["text"]),
                        ):
                            suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                            match_label = "sink" if match["regex"] == SINK_REGEX_ID else "source"
                            lines.append(
                                f"  - [{match_label}] {md_code(match['text'])}{suffix}"
                            )
                        lines.append("")
                else:
                    vendor_matches: "OrderedDict[str, list[dict]]" = OrderedDict()
                    for match in data["src_vendor"] + data["sink_vendor"]:
                        vendor_matches.setdefault(match["url"], []).append(match)
                    for url, matches in vendor_matches.items():
                        lines.append(f"- {md_code(url)}")
                        seen_matches: set[tuple[int, str]] = set()
                        for match in sorted(
                            matches, key=lambda item: (item["regex"], item["text"])
                        ):
                            match_key = (match["regex"], match["text"])
                            if match_key in seen_matches:
                                continue
                            seen_matches.add(match_key)
                            suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                            match_label = "sink" if match["regex"] == SINK_REGEX_ID else "source"
                            lines.append(
                                f"  - [{match_label}] {md_code(match['text'])}{suffix}"
                            )
                        lines.append("")
        elif data["new_vendor_files"] or data["src_vendor"] or data["sink_vendor"]:
            lines.append(
                f"- Vendor/SDK additions: +{len(data['new_vendor_files'])} files | "
                f"{len(data['src_vendor'])} source / {len(data['sink_vendor'])} sinks "
                "(match texts in final index)"
            )
            lines.append("")

    lines.append("## Unique Routes With No New Discoveries")
    lines.append("")
    if none_routes:
        route_word = "route" if len(none_routes) == 1 else "routes"
        lines.append(
            f"{len(none_routes)} unique {route_word} loaded no new JS files and produced no new "
            "source matches or location sinks."
        )
        lines.append("")
        lines.append("| Route | URL | Loaded files |")
        lines.append("|---:|---|---:|")
        for route in none_routes:
            route_index = route["index"]
            data = route_data[route_index]
            url = route["url"]
            if route.get("final_url") and route["final_url"] != route["url"]:
                url = f"{url} (final: {route['final_url']})"
            lines.append(f"| {route_index} | {md_code(url)} | {len(data['loaded'])} |")
    else:
        lines.append("None.")
    lines.append("")

    app_index: list[dict] = []
    vendor_index: list[dict] = []
    for entry in sorted(collapsed.values(), key=lambda item: item["url"]):
        if not entry["matches"]:
            continue
        if is_app(entry["url"]):
            app_index.append(entry)
        else:
            vendor_index.append(entry)

    def append_per_file_index(title: str, entries: list[dict]) -> None:
        lines.append(f"## {title}")
        lines.append("")
        if not entries:
            lines.append("None.")
            lines.append("")
            return
        lines.append(f"<details><summary>{title}</summary>")
        lines.append("")
        for entry in entries:
            lines.append(f"- {md_code(entry['url'])}")
            for match in sorted(
                entry["matches"].values(), key=lambda item: (item["regex"], item["text"])
            ):
                suffix = f" (x{match['count']})" if match["count"] > 1 else ""
                match_label = "sink" if match["regex"] == SINK_REGEX_ID else "source"
                lines.append(f"  - [{match_label}] {md_code(match['text'])}{suffix}")
        lines.append("")
        lines.append("</details>")
        lines.append("")

    append_per_file_index("All source and sink matches, unique per file (app)", app_index)
    if not args.hide_vendor_index:
        append_per_file_index(
            "All source and sink matches, unique per file (vendor)", vendor_index
        )

    lines.append("## Vendor-Only Routes")
    lines.append("")
    if vendor_routes:
        route_word = "route" if len(vendor_routes) == 1 else "routes"
        if args.include_vendor:
            lines.append(
                f"{len(vendor_routes)} unique {route_word} added only vendor/SDK files or matches. "
                "They are included as detailed route sections above."
            )
        else:
            lines.append(
                f"{len(vendor_routes)} unique {route_word} added only vendor/SDK files or matches. "
                "These are summarized here; vendor match texts are in the final per-file index."
            )
            lines.append("")
            lines.append("| Route | URL | New vendor files | Vendor source | Vendor sinks |")
            lines.append("|---:|---|---:|---:|---:|")
            for route in vendor_routes:
                route_index = route["index"]
                data = route_data[route_index]
                url = route["url"]
                if route.get("final_url") and route["final_url"] != route["url"]:
                    url = f"{url} (final: {route['final_url']})"
                lines.append(
                    f"| {route_index} | {md_code(url)} | {len(data['new_vendor_files'])} | "
                    f"{len(data['src_vendor'])} | {len(data['sink_vendor'])} |"
                )
    else:
        lines.append("None.")
    lines.append("")

    lines.append("## Duplicate Routes")
    lines.append("")
    if not duplicates:
        lines.append("No routes were skipped as duplicate results.")
    else:
        route_word = "route" if len(duplicates) == 1 else "routes"
        lines.append(
            f"{len(duplicates)} duplicate {route_word} produced no new JS files, source matches, "
            "or location sinks."
        )
        lines.append("")
        grouped_duplicates: dict[int, list[int]] = {}
        for route in duplicates:
            grouped_duplicates.setdefault(route["duplicate_of"], []).append(route["index"])
        for source_route in sorted(grouped_duplicates):
            lines.append(
                f"- Route {source_route} source; duplicates: "
                f"{compress_route_numbers(grouped_duplicates[source_route])}"
            )
    lines.append("")

    lines.append("## Errors")
    lines.append("")
    error_lines: list[str] = []
    for route in state.routes:
        if route.get("nav_error"):
            error_lines.append(
                f"- Route {route['index']} {md_code(route['url'])}: {md_text(route['nav_error'])}"
            )
        if route.get("scan_error"):
            error_lines.append(
                f"- Route {route['index']} {md_code(route['url'])}: {md_text(route['scan_error'])}"
            )
    failed_files: dict[str, int] = {}
    for route in state.routes:
        for entry in route["files"]:
            if entry.get("ok", False):
                continue
            failed_files.setdefault(entry["url"], route["index"])
    for url, route_index in failed_files.items():
        if url in state.unscanned:
            continue
        error_lines.append(
            f"- File {md_code(url)} (first seen on route {route_index}): source could not be scanned"
        )
    for entry in state.unscanned.values():
        error_lines.append(
            f"- File {md_code(entry['url'])} (first seen on {md_code(entry['first_route'])}): "
            "source could not be scanned"
            + (f" ({md_text(entry['error'])})" if entry.get("error") else "")
        )
    if error_lines:
        lines.extend(error_lines)
    else:
        lines.append("None.")
    lines.append("")

    lines.append("<details><summary>Regex patterns and exclusions</summary>")
    lines.append("")
    for regex_id, pattern in REGEX_BY_ID.items():
        lines.append(f"Regex {regex_id} ({REGEX_LABELS[regex_id]}):")
        lines.append("")
        lines.append("```regex")
        lines.append(pattern.pattern)
        lines.append("```")
        lines.append("")
    lines.append("Default match exclusions:")
    lines.append("")
    for exclusion in DEFAULT_EXCLUDED_MATCH_PATTERNS:
        lines.append(f"- {md_code(exclusion.pattern)}")
    lines.append("")
    lines.append("Excluded `.get` parameter names:")
    lines.append("")
    lines.append(", ".join(f"`{name}`" for name in sorted(REGEX_2_EXCLUDED_PARAM_NAMES)))
    if args.exclude_regex:
        lines.append("")
        lines.append("Additional match exclusions:")
        lines.append("")
        for exclusion in args.exclude_regex:
            lines.append(f"- {md_code(exclusion)}")
    lines.append("")
    lines.append("</details>")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    if not JS_SCANNER_PATH.is_file():
        sys.exit(f"JavaScript scanner not found: {JS_SCANNER_PATH}")

    urls, input_duplicates = load_urls(Path(args.urls_file))
    if not urls:
        sys.exit(f"No valid URLs found in {args.urls_file}")

    vendors_file = resolve_vendors_file(args.urls_file)
    args.vendor_patterns = load_vendor_patterns(args.include_vendor, vendors_file)
    if args.include_vendor:
        print(
            f"[i] vendor inclusion enabled | patterns: {len(args.vendor_patterns)} | "
            f"file: {vendors_file}",
            flush=True,
        )

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
                        "initial_scripts": [],
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
    report = render_full_report(state, meta, args, input_duplicates, auth) if args.full_report else render_report(state, meta, args, input_duplicates, auth)
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
