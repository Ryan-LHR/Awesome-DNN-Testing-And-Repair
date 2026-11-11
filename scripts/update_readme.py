"""Validate paper data and update English and Simplified Chinese READMEs using Python's standard library.

Usage:
    python3 scripts/update_readme.py
    python3 scripts/update_readme.py --check
"""

import argparse
import json
import re
import sys
from datetime import date, timedelta
from ipaddress import ip_address
from pathlib import Path
from urllib.parse import quote, urlsplit


CATEGORIES = {
    "Coverage Metrics": 4,
    "Test Generation": 4,
    "Test Selection and Prioritization": 4,
    "Model Repair": 4,
    "DNN Verification": 4,
    "Other": 4,
    "Surveys": 3,
    "Empirical Studies": 3,
}
TARGET_MODEL_TYPES = {
    "Non-LLM DNN": "Non-LLM DNNs",
    "LLM": "LLMs",
    "QNN": "QNNs",
}
ZH_HANS_LABELS = {
    "Research Papers": "研究论文",
    "Coverage Metrics": "覆盖度量",
    "Test Generation": "测试生成",
    "Test Selection and Prioritization": "测试选择与排序",
    "Model Repair": "模型修复",
    "DNN Verification": "DNN 验证",
    "Other": "其他",
    "Surveys": "综述",
    "Empirical Studies": "实证研究",
    "Non-LLM DNNs": "非 LLM 深度神经网络",
    "LLMs": "大语言模型（LLM）",
    "QNNs": "量子神经网络（QNN）",
    "Year": "年份",
    "Date": "日期",
    "Paper": "论文",
    "Name": "简称",
    "Title": "标题",
    "Links": "链接",
    "Venue": "来源",
    " (preprint)": "（预印本）",
}
PUBLICATION_TYPES = ("conference", "journal", "preprint")
BADGES = {
    "Paper": "assets/badges/paper.svg",
    "arXiv": "assets/badges/arxiv.svg",
    "Code": "assets/badges/code.svg",
    "Website": "assets/badges/website.svg",
}
OVERVIEW_BEGIN_MARKER = "<!-- BEGIN GENERATED OVERVIEW -->"
OVERVIEW_END_MARKER = "<!-- END GENERATED OVERVIEW -->"
RECENT_BEGIN_MARKER = "<!-- BEGIN GENERATED RECENT PAPERS -->"
RECENT_END_MARKER = "<!-- END GENERATED RECENT PAPERS -->"
RECOMMENDED_BEGIN_MARKER = "<!-- BEGIN GENERATED RECOMMENDED PAPERS -->"
RECOMMENDED_END_MARKER = "<!-- END GENERATED RECOMMENDED PAPERS -->"
RECOMMENDED_PAPER_IDS = ("dufp-2026",)
RECOMMENDED_SUMMARIES = {
    "dufp-2026": {
        "en": "Prioritizes DNN test inputs by combining decision ambiguity with distributional atypicality.",
        "zh-Hans": "结合决策歧义与分布非典型性，对 DNN 测试输入进行优先级排序。",
    },
}
BEGIN_MARKER = "<!-- BEGIN GENERATED PAPERS -->"
END_MARKER = "<!-- END GENERATED PAPERS -->"
RESOURCE_FIELDS = ("paper_url", "arxiv_url", "code_url", "website_url")
SCAN_STATES = {
    "directory_status": ("complete_as_of_cutoff",),
    "screening_stage": ("title_only",),
    "title_screen_status": ("complete",),
    "decision": ("candidate", "boundary", "not_selected_at_title_screen", "out_of_scope"),
}


def url_error(value):
    if not isinstance(value, str) or not value:
        return "must be a non-empty HTTP(S) URL."
    if re.search(r"[\s\x00-\x1f\x7f\\]", value):
        return "must not contain whitespace, control characters or backslashes."
    if re.search(r"%(?![0-9A-Fa-f]{2})", value):
        return "contains an invalid percent escape."
    try:
        parts = urlsplit(value)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            return "must be an absolute HTTP(S) URL with a host."
        if parts.username is not None or parts.password is not None:
            return "must not contain embedded credentials."
        if parts.port is not None and not 1 <= parts.port <= 65535:
            return "has an invalid port."
        host = parts.hostname.encode("idna").decode("ascii")
        try:
            ip_address(host)
        except ValueError:
            labels = host.rstrip(".").split(".")
            if len(host) > 253 or len(labels) < 2 or any(
                not re.fullmatch(r"[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?", label)
                for label in labels
            ):
                return "has an invalid domain name."
    except (ValueError, UnicodeError):
        return "has an invalid host or port."
    return None


def date_error(value):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value):
        return "must use YYYY-MM-DD format."
    try:
        date.fromisoformat(value)
    except ValueError:
        return "must be a valid calendar date."
    return None


def validate_papers(papers):
    if not isinstance(papers, list):
        return ["papers.json must contain an array of paper objects."]

    errors = []
    seen_ids = set()
    seen_dois = set()
    for index, paper in enumerate(papers, 1):
        if not isinstance(paper, dict):
            errors.append(f"Paper #{index} must be an object.")
            continue
        paper_id = paper.get("id")
        label = f"Paper #{index} ({paper_id})"
        for field in ("id", "title", "venue", "paper_url", "abstract"):
            value = paper.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{label}: {field} must be a non-empty string.")

        if paper.get("language") not in ("en", "zh"):
            errors.append(f"{label}: language must be en or zh.")

        authors = paper.get("authors")
        if authors is not None and (
            not isinstance(authors, list)
            or any(not isinstance(author, str) or not author.strip() for author in authors)
        ):
            errors.append(f"{label}: authors must be null or an array of non-empty strings.")

        if paper.get("ccf_rank") not in (None, "A", "B", "C"):
            errors.append(f"{label}: ccf_rank must be null, A, B or C.")

        if isinstance(paper_id, str):
            if paper_id in seen_ids:
                errors.append(f"{label}: duplicate id.")
            seen_ids.add(paper_id)

        for field in ("alias", "doi", "arxiv_url", "code_url", "website_url"):
            value = paper.get(field)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                errors.append(f"{label}: {field} must be null or a non-empty string.")
        for field in RESOURCE_FIELDS:
            value = paper.get(field)
            if isinstance(value, str) and value:
                error = url_error(value)
                if error:
                    errors.append(f"{label}: {field} {error}")
        doi = paper.get("doi")
        if isinstance(doi, str) and doi.strip():
            doi = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", doi.strip(), flags=re.I)
            doi = doi.casefold()
            if doi in seen_dois:
                errors.append(f"{label}: duplicate DOI {doi}.")
            seen_dois.add(doi)

        categories = paper.get("categories")
        if not isinstance(categories, list) or not categories:
            errors.append(f"{label}: categories must be a non-empty array.")
        elif any(not isinstance(category, str) or category not in CATEGORIES for category in categories):
            errors.append(f"{label}: categories contains an unknown category.")
        elif len(categories) != len(set(categories)):
            errors.append(f"{label}: categories contains duplicates.")

        target_model_types = paper.get("target_model_types")
        if not isinstance(target_model_types, list) or not target_model_types:
            errors.append(f"{label}: target_model_types must be a non-empty array.")
        elif any(not isinstance(model_type, str) or model_type not in TARGET_MODEL_TYPES for model_type in target_model_types):
            errors.append(f"{label}: target_model_types contains an unknown model type.")
        elif len(target_model_types) != len(set(target_model_types)):
            errors.append(f"{label}: target_model_types contains duplicates.")

        publication_type = paper.get("publication_type")
        if publication_type not in PUBLICATION_TYPES:
            errors.append(f"{label}: publication_type must be conference, journal or preprint.")
        dates = paper.get("dates")
        if not isinstance(dates, dict):
            errors.append(f"{label}: dates must be an object.")
        else:
            required_year = "first_public_year" if publication_type == "preprint" else "publication_year"
            for field in ("publication_year", "online_year", "first_public_year"):
                year = dates.get(field)
                if year is None and (field != required_year or publication_type not in PUBLICATION_TYPES):
                    continue
                if type(year) is not int or not 1000 <= year <= 9999:
                    errors.append(f"{label}: dates.{field} must be a four-digit integer.")
            for field in ("publication_date", "first_public_date", "checked_on"):
                value = dates.get(field)
                if value is None:
                    continue
                error = date_error(value)
                if error:
                    errors.append(f"{label}: dates.{field} {error}")
    return errors


def validate_scan_log(log):
    if not isinstance(log, dict) or not isinstance(log.get("scope"), dict) or not isinstance(log.get("scans"), list):
        return ["scan-log.json: must contain a scope object and a scans array."]
    errors = []
    scope = log["scope"]
    revision = scope.get("revision")
    if type(revision) is not int or revision < 1:
        errors.append("scan-log.json: scope.revision must be a positive integer.")
    for field in ("start_year", "end_year"):
        value = scope.get(field)
        if type(value) is not int or not 1000 <= value <= 9999:
            errors.append(f"scan-log.json: scope.{field} must be a four-digit integer.")
    start, end = scope.get("start_year"), scope.get("end_year")
    if type(start) is int and type(end) is int and start > end:
        errors.append("scan-log.json: scope.start_year must not exceed scope.end_year.")
    for field, allowed in (("venues", None), ("categories", CATEGORIES), ("target_model_types", TARGET_MODEL_TYPES)):
        values = scope.get(field)
        if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f"scan-log.json: scope.{field} must be a non-empty array of non-empty strings.")
        elif len(values) != len(set(values)) or (allowed is not None and any(v not in allowed for v in values)):
            errors.append(f"scan-log.json: scope.{field} contains duplicate or unknown values.")
    scan_ids = set()
    batches = set()
    for index, scan in enumerate(log["scans"], 1):
        label = f"Scan #{index} ({scan.get('id') if isinstance(scan, dict) else '?'})"
        if not isinstance(scan, dict):
            errors.append(f"{label}: must be an object.")
            continue
        for field in ("id", "venue", "track"):
            if not isinstance(scan.get(field), str) or not scan[field].strip():
                errors.append(f"{label}: {field} must be a non-empty string.")
        scan_id = scan.get("id")
        if isinstance(scan_id, str):
            if scan_id in scan_ids:
                errors.append(f"{label}: duplicate scan id.")
            scan_ids.add(scan_id)
        year = scan.get("year")
        if type(year) is not int or not 1000 <= year <= 9999:
            errors.append(f"{label}: year must be a four-digit integer.")
        scope_revision = scan.get("scope_revision")
        if type(scope_revision) is not int or scope_revision < 1 or (type(revision) is int and scope_revision > revision):
            errors.append(f"{label}: scope_revision must reference an existing scope revision.")
        if scope_revision == revision:
            if isinstance(scope.get("venues"), list) and scan.get("venue") not in scope["venues"]:
                errors.append(f"{label}: venue is outside the current scope.")
            if all(type(v) is int for v in (year, start, end)) and not start <= year <= end:
                errors.append(f"{label}: year is outside the current scope.")
        for field in ("checked_on", "coverage_through"):
            error = date_error(scan.get(field))
            if error:
                errors.append(f"{label}: {field} {error}")
        if not date_error(scan.get("checked_on")) and not date_error(scan.get("coverage_through")):
            if scan["coverage_through"] > scan["checked_on"]:
                errors.append(f"{label}: coverage_through must not be later than checked_on.")
        for field in ("directory_status", "screening_stage", "title_screen_status"):
            if scan.get(field) not in SCAN_STATES[field]:
                errors.append(f"{label}: unknown {field}; update the reviewed workflow vocabulary first.")
        batch = tuple(scan.get(k) for k in ("venue", "year", "track", "coverage_through", "scope_revision"))
        if all(isinstance(v, (str, int)) for v in batch):
            if batch in batches:
                errors.append(f"{label}: duplicate scan scope and cutoff.")
            batches.add(batch)
        sources = scan.get("sources")
        if not isinstance(sources, list) or not sources:
            errors.append(f"{label}: sources must be a non-empty array.")
        else:
            source_urls = set()
            for number, source in enumerate(sources, 1):
                prefix = f"{label}: source #{number}"
                if not isinstance(source, dict):
                    errors.append(f"{prefix} must be an object.")
                    continue
                url = source.get("url")
                error = url_error(url)
                if error:
                    errors.append(f"{prefix} url {error}")
                elif url in source_urls:
                    errors.append(f"{prefix} duplicate source URL.")
                else:
                    source_urls.add(url)
                if not isinstance(source.get("kind"), str) or not source["kind"].strip():
                    errors.append(f"{prefix} kind must be a non-empty string.")
                for field in ("entry_count", "sections_checked"):
                    value = source.get(field)
                    if value is not None and (type(value) is not int or value < 0):
                        errors.append(f"{prefix} {field} must be a non-negative integer.")
        entries = scan.get("entries")
        if not isinstance(entries, list):
            errors.append(f"{label}: entries must be an array.")
            continue
        seen = {"source_id": set(), "doi": set()}
        for number, entry in enumerate(entries, 1):
            prefix = f"{label}: entry #{number}"
            if not isinstance(entry, dict):
                errors.append(f"{prefix} must be an object.")
                continue
            for field in ("source_id", "title", "reason"):
                if not isinstance(entry.get(field), str) or not entry[field].strip():
                    errors.append(f"{prefix} {field} must be a non-empty string.")
            if entry.get("decision") not in SCAN_STATES["decision"]:
                errors.append(f"{prefix} unknown decision; update the reviewed workflow vocabulary first.")
            for field in seen:
                value = entry.get(field)
                if value is None and field == "doi":
                    continue
                if not isinstance(value, str) or not value.strip():
                    if field == "doi":
                        errors.append(f"{prefix} doi must be null or a non-empty string.")
                    continue
                key = value.strip().casefold()
                if field == "doi":
                    key = re.sub(r"^(https?://(dx\.)?doi\.org/|doi:\s*)", "", key)
                if key in seen[field]:
                    errors.append(f"{prefix} duplicate {field} within this scan.")
                seen[field].add(key)
    return errors


def paper_year(paper):
    field = "first_public_year" if paper["publication_type"] == "preprint" else "publication_year"
    return paper["dates"][field]


def escape_cell(value):
    value = " ".join(value.split())
    for character in "\\[]|*":
        value = value.replace(character, "\\" + character)
    return value


def paper_link(label, url):
    url = quote(url, safe=":/?#[]@!$&'*+,;=%~")
    return f"[![{escape_cell(label)}]({BADGES[label]})]({url})"


def render_resources(paper):
    paper_host = urlsplit(paper["paper_url"]).hostname
    label = "arXiv" if paper_host == "arxiv.org" or paper_host.endswith(".arxiv.org") else "Paper"
    resource_links = {paper["paper_url"]: label}
    for field, label in (("arxiv_url", "arXiv"), ("code_url", "Code"), ("website_url", "Website")):
        if paper.get(field):
            resource_links.setdefault(paper[field], label)
    return "<br>".join(paper_link(label, url) for url, label in resource_links.items())


def render_venue(paper, language="en"):
    labels = ZH_HANS_LABELS if language == "zh-Hans" else {}
    venue = escape_cell(paper["venue"])
    if paper["publication_type"] == "conference":
        venue += f"<br>{paper_year(paper)}"
    elif paper["publication_type"] == "preprint":
        venue += labels.get(" (preprint)", " (preprint)")
    return venue


def render_recent_papers(papers, end, language="en"):
    labels = ZH_HANS_LABELS if language == "zh-Hans" else {}
    previous_month = end.replace(day=1) - timedelta(days=1)
    start = previous_month.replace(day=min(end.day, previous_month.day))
    matches = []
    for paper in papers:
        field = "first_public_date" if paper["publication_type"] == "preprint" else "publication_date"
        value = paper["dates"].get(field)
        if value:
            published = date.fromisoformat(value)
            if start <= published <= end:
                matches.append((published, paper))
    matches.sort(key=lambda item: (-item[0].toordinal(), item[1]["title"].casefold()))
    lines = [f"*{start.isoformat()} — {end.isoformat()}*", ""]
    if not matches:
        lines.append(
            "当前收录中暂无日期已确认且位于此时间范围内的论文。"
            if language == "zh-Hans"
            else "No papers in the collection have a confirmed publication or first preprint date within this window."
        )
        return "\n".join(lines)
    lines.extend([
        "| " + " | ".join(labels.get(column, column) for column in ("Date", "Paper", "Venue", "Links")) + " |",
        "| :---: | --- | :---: | --- |",
    ])
    for published, paper in matches:
        title = escape_cell(paper["title"])
        if paper.get("alias"):
            title = f"**{escape_cell(paper['alias'])}** — {title}"
        lines.append(f"| {published.isoformat()} | {title} | {render_venue(paper, language)} | {render_resources(paper)} |")
    return "\n".join(lines)


def render_recommended_papers(papers, language="en"):
    matches = [paper for paper_id in RECOMMENDED_PAPER_IDS for paper in papers if paper["id"] == paper_id]
    lines = []
    for paper in matches:
        heading = escape_cell(paper.get("alias") or paper["title"])
        venue = render_venue(paper, language).replace("<br>", " ")
        lines.extend([f"**{heading}** · {venue}", "", f"> {escape_cell(paper['title'])}"])
        authors = paper.get("authors")
        if authors:
            author = escape_cell(authors[0]) + (" et al." if len(authors) > 1 else "")
            lines.extend([">", f"> {author}"])
        summary = RECOMMENDED_SUMMARIES.get(paper["id"], {}).get(language)
        if summary:
            lines.extend([">", f"> {summary}"])
        resources = render_resources(paper).replace("<br>", " ")
        lines.extend([">", f"> {resources}", ""])
    return "\n".join(lines).rstrip()


def render_overview(papers, language="en"):
    labels = ZH_HANS_LABELS if language == "zh-Hans" else {}
    research_count = sum(
        any(CATEGORIES[category] == 4 for category in paper["categories"])
        for paper in papers
    )
    research_label = labels.get("Research Papers", "Research Papers")
    lines = [f"- **[{research_label}](#research-papers)** ({research_count})"]
    for category, level in CATEGORIES.items():
        count = sum(category in paper["categories"] for paper in papers)
        link = f"[{labels.get(category, category)}](#{category.lower().replace(' ', '-')})"
        label = f"  - {link}" if level == 4 else f"- **{link}**"
        lines.append(f"{label} ({count})")
    return "\n".join(lines)


def render_tables(papers, language="en"):
    labels = ZH_HANS_LABELS if language == "zh-Hans" else {}
    lines = []
    if language == "zh-Hans":
        lines.extend(['<a name="research-papers"></a>', ""])
    lines.extend([f"### {labels.get('Research Papers', 'Research Papers')}", ""])
    for category, level in CATEGORIES.items():
        if language == "zh-Hans":
            lines.extend([f'<a name="{category.lower().replace(" ", "-")}"></a>', ""])
        lines.extend([f"{'#' * level} {labels.get(category, category)}", ""])
        for target_model_type, heading in TARGET_MODEL_TYPES.items():
            matches = sorted(
                (paper for paper in papers if category in paper["categories"] and target_model_type in paper["target_model_types"]),
                key=lambda paper: (-paper_year(paper), paper["title"].casefold()),
            )
            if not matches:
                continue
            lines.extend([
                f"{'#' * (level + 1)} {labels.get(heading, heading)}", "",
                "| " + " | ".join(labels.get(column, column) for column in ("Year", "Name", "Title", "Links", "Venue")) + " |",
                "| :---: | --- | --- | --- | :---: |",
            ])
            for paper in matches:
                year = paper_year(paper)
                alias = f"**{escape_cell(paper['alias'])}**" if paper.get("alias") else "—"
                alias = re.sub(r" \((conf-version|journal-version)\)\*\*$", r"**<br>(\1)", alias)
                resources = render_resources(paper)
                venue = render_venue(paper, language)
                title = escape_cell(paper["title"])
                lines.append(f"| {year} | {alias} | {title} | {resources} | {venue} |")
            lines.append("")
    return "\n".join(lines).rstrip()


def replace_tables(readme, tables, begin_marker=BEGIN_MARKER, end_marker=END_MARKER):
    if readme.count(begin_marker) != 1 or readme.count(end_marker) != 1:
        raise ValueError(f"README must contain exactly one {begin_marker} and {end_marker} marker.")
    start = readme.index(begin_marker) + len(begin_marker)
    end = readme.index(end_marker)
    if end < start:
        raise ValueError("README generated-table markers are in the wrong order.")
    newline = "\r\n" if "\r\n" in readme else "\n"
    tables = tables.replace("\n", newline)
    return readme[:start] + newline * 2 + tables + newline * 2 + readme[end:]


def replace_badge_counts(readme, papers):
    counts = {
        "Papers": len(papers),
        "With%20code": sum(bool(paper.get("code_url")) for paper in papers),
    }
    for label, count in counts.items():
        readme = re.sub(
            rf"(https://img\.shields\.io/badge/{label}-)\d+(-)",
            rf"\g<1>{count}\2",
            readme,
        )
    return readme


def main():
    parser = argparse.ArgumentParser(description="Validate papers.json and update English and Simplified Chinese README overviews, recent and recommended papers, paper tables, and badge counts.")
    parser.add_argument("--check", action="store_true", help="Check data and README without writing files.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    papers = json.loads((root / "data/papers.json").read_text(encoding="utf-8"))
    scan_log = json.loads((root / "data/scan-log.json").read_text(encoding="utf-8"))
    errors = validate_papers(papers) + validate_scan_log(scan_log)
    if errors:
        print("Validation failed:\n" + "\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    for badge in BADGES.values():
        if not (root / badge).is_file():
            raise FileNotFoundError(f"Missing badge asset: {badge}")

    updates = []
    today = date.today()
    for filename, language in (("README.md", "en"), ("README.zh-Hans.md", "zh-Hans")):
        visible_papers = papers
        if language == "en":
            visible_papers = [paper for paper in papers if paper["language"] == "en"]
        path = root / filename
        readme = path.read_bytes().decode("utf-8")
        updated = replace_tables(readme, render_overview(visible_papers, language), OVERVIEW_BEGIN_MARKER, OVERVIEW_END_MARKER)
        updated = replace_tables(updated, render_recent_papers(visible_papers, today, language), RECENT_BEGIN_MARKER, RECENT_END_MARKER)
        updated = replace_tables(updated, render_recommended_papers(visible_papers, language), RECOMMENDED_BEGIN_MARKER, RECOMMENDED_END_MARKER)
        updated = replace_tables(updated, render_tables(visible_papers, language))
        updated = replace_badge_counts(updated, papers)
        if updated != readme:
            updates.append((path, updated))
    if not updates:
        print(f"Validated {len(papers)} papers and scan-log.json; README.md and README.zh-Hans.md are up to date.")
        return 0
    filenames = ", ".join(path.name for path, _ in updates)
    if args.check:
        print(f"Out of date: {filenames}. Run python3 scripts/update_readme.py.", file=sys.stderr)
        return 1
    for path, updated in updates:
        path.write_bytes(updated.encode("utf-8"))
    print(f"Validated {len(papers)} papers; updated {filenames}.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
