"""Check recorded resource URLs and save a report without changing paper data.

Usage:
    python3 scripts/check_links.py --output work/link-check.json
"""

import argparse
import json
import socket
import ssl
import sys
import threading
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen

from update_readme import RESOURCE_FIELDS, validate_papers


def request_url(url, method, timeout):
    request = Request(url, method=method, headers={"User-Agent": "Awesome-DNN-Testing-And-Repair-LinkCheck/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            return {"method": method, "http_status": response.status, "final_url": response.url}
    except HTTPError as error:
        result = {"method": method, "http_status": error.code, "final_url": error.url}
        error.close()
        return result
    except (URLError, OSError, ValueError) as error:
        reason = getattr(error, "reason", error)
        if isinstance(reason, ssl.SSLError):
            kind = "tls_error"
        elif isinstance(reason, (TimeoutError, socket.timeout)):
            kind = "timeout"
        elif isinstance(reason, socket.gaierror):
            kind = "dns_error"
        else:
            kind = "network_error"
        return {"method": method, "http_status": None, "final_url": None, "error_kind": kind, "error": str(error)}


def check_url(url, timeout):
    attempts = [request_url(url, "HEAD", timeout)]
    code = attempts[-1]["http_status"]
    if code is not None and code >= 400 and code != 429:
        attempts.append(request_url(url, "GET", timeout))
    result = attempts[-1]
    code = result["http_status"]
    if code is None:
        status = result["error_kind"]
    elif 200 <= code < 300:
        status = "redirected" if result["final_url"] != url else "reachable"
    elif code in (404, 410):
        status = "not_found"
    elif code in (401, 403, 429, 451):
        status = "access_limited"
    elif code >= 500:
        status = "server_error"
    else:
        status = "http_error"
    return {"url": url, "status": status, **result, "attempts": attempts}


def main():
    parser = argparse.ArgumentParser(description="Report HTTP availability of recorded paper, arXiv, Code, and Website URLs.")
    parser.add_argument("--output", type=Path, default=Path("work/link-check.json"), help="Report path; paper data and READMEs are never written.")
    parser.add_argument("--timeout", type=float, default=15, help="Timeout per request in seconds.")
    parser.add_argument("--workers", type=int, default=6, help="Maximum concurrent URLs; at most two per starting host.")
    args = parser.parse_args()
    if args.timeout <= 0 or args.workers < 1:
        parser.error("timeout and workers must be positive")
    root = Path(__file__).resolve().parent.parent
    output = args.output.resolve()
    if output in {(root / name).resolve() for name in ("data/papers.json", "data/scan-log.json", "README.md", "README.zh-Hans.md", "README.zh-Hant.md")}:
        parser.error("output must not overwrite repository data or README files")
    papers = json.loads((root / "data/papers.json").read_text(encoding="utf-8"))
    errors = validate_papers(papers)
    if errors:
        print("Validation failed:\n" + "\n".join(errors), file=sys.stderr)
        return 1
    urls = {}
    for paper in papers:
        for field in RESOURCE_FIELDS:
            if paper.get(field):
                urls.setdefault(paper[field], []).append({"id": paper["id"], "title": paper["title"], "field": field})
    hosts = {urlsplit(url).hostname: threading.Semaphore(2) for url in urls}

    def check(item):
        url, references = item
        with hosts[urlsplit(url).hostname]:
            result = check_url(url, args.timeout)
        return {**result, "references": references}

    started_at = datetime.now(timezone.utc).isoformat()
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        for result in pool.map(check, urls.items()):
            results.append(result)
            if len(results) % 25 == 0:
                print(f"Checked {len(results)}/{len(urls)} URLs.", flush=True)
    report = {
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "scope": list(RESOURCE_FIELDS),
        "paper_count": len(papers),
        "reference_count": sum(len(refs) for refs in urls.values()),
        "unique_url_count": len(urls),
        "summary": dict(Counter(result["status"] for result in results)),
        "notes": [
            "HTTP responses measure availability, not paper identity or full-text access.",
            "HTTP errors from HEAD except rate limits are checked once with GET; TLS verification stays enabled.",
            "404/410 results need review; restricted, rate-limited and transport failures do not prove a dead link.",
            "DOI redirects are expected. No recorded URLs are replaced or removed.",
        ],
        "results": results,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Checked {len(results)} unique URLs: {report['summary']}")
    print(f"Report: {output}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
