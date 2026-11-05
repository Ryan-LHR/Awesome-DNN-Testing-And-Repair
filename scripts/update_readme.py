"""Validate paper data and update the README overview and tables using Python's standard library.

Usage:
    python3 scripts/update_readme.py
    python3 scripts/update_readme.py --check
"""

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import quote


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
PUBLICATION_TYPES = ("conference", "journal", "preprint")
BADGES = {
    "Paper": "assets/badges/paper.svg",
    "arXiv": "assets/badges/arxiv.svg",
    "Code": "assets/badges/code.svg",
    "Website": "assets/badges/website.svg",
}
OVERVIEW_BEGIN_MARKER = "<!-- BEGIN GENERATED OVERVIEW -->"
OVERVIEW_END_MARKER = "<!-- END GENERATED OVERVIEW -->"
BEGIN_MARKER = "<!-- BEGIN GENERATED PAPERS -->"
END_MARKER = "<!-- END GENERATED PAPERS -->"


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

        if isinstance(paper_id, str):
            if paper_id in seen_ids:
                errors.append(f"{label}: duplicate id.")
            seen_ids.add(paper_id)

        for field in ("alias", "doi", "arxiv_url", "code_url", "website_url"):
            value = paper.get(field)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                errors.append(f"{label}: {field} must be null or a non-empty string.")
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
        elif publication_type in PUBLICATION_TYPES:
            field = "first_public_year" if publication_type == "preprint" else "publication_year"
            year = dates.get(field)
            if type(year) is not int or not 1000 <= year <= 9999:
                errors.append(f"{label}: dates.{field} must be a four-digit integer.")
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


def render_overview(papers):
    research_count = sum(
        any(CATEGORIES[category] == 4 for category in paper["categories"])
        for paper in papers
    )
    lines = [f"- **[Research Papers](#research-papers)** ({research_count})"]
    for category, level in CATEGORIES.items():
        count = sum(category in paper["categories"] for paper in papers)
        link = f"[{category}](#{category.lower().replace(' ', '-')})"
        label = f"  - {link}" if level == 4 else f"- **{link}**"
        lines.append(f"{label} ({count})")
    lines.extend(["", "A paper may appear in more than one category."])
    return "\n".join(lines)


def render_tables(papers):
    lines = ["### Research Papers", ""]
    for category, level in CATEGORIES.items():
        lines.extend([f"{'#' * level} {category}", ""])
        for target_model_type, heading in TARGET_MODEL_TYPES.items():
            matches = sorted(
                (paper for paper in papers if category in paper["categories"] and target_model_type in paper["target_model_types"]),
                key=lambda paper: (-paper_year(paper), paper["title"].casefold()),
            )
            if not matches:
                continue
            lines.extend([
                f"{'#' * (level + 1)} {heading}", "",
                "| Year | Name | Title | Resources | Venue |",
                "| --- | --- | --- | --- | --- |",
            ])
            for paper in matches:
                year = paper_year(paper)
                alias = f"**{escape_cell(paper['alias'])}**" if paper.get("alias") else "—"
                resource_links = {paper["paper_url"]: "Paper"}
                for field, label in (("arxiv_url", "arXiv"), ("code_url", "Code"), ("website_url", "Website")):
                    if paper.get(field):
                        resource_links.setdefault(paper[field], label)
                resources = " ".join(paper_link(label, url) for url, label in resource_links.items())
                venue = escape_cell(paper["venue"])
                if paper["publication_type"] == "conference":
                    venue += f"' {year}"
                elif paper["publication_type"] == "preprint":
                    venue += " (preprint)"
                title = escape_cell(paper["title"])
                lines.append(f"| {year} | {alias} | {title} | {resources} | {venue} |")
            lines.append("")
    return "\n".join(lines).rstrip()


def replace_tables(readme, tables, begin_marker=BEGIN_MARKER, end_marker=END_MARKER):
    if readme.count(begin_marker) != 1 or readme.count(end_marker) != 1:
        raise ValueError(f"README.md must contain exactly one {begin_marker} and {end_marker} marker.")
    start = readme.index(begin_marker) + len(begin_marker)
    end = readme.index(end_marker)
    if end < start:
        raise ValueError("README.md generated-table markers are in the wrong order.")
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
    parser = argparse.ArgumentParser(description="Validate papers.json and update README overview, paper tables, and badge counts.")
    parser.add_argument("--check", action="store_true", help="Check data and README without writing files.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    papers = json.loads((root / "data/papers.json").read_text(encoding="utf-8"))
    errors = validate_papers(papers)
    if errors:
        print("Validation failed:\n" + "\n".join(f"- {error}" for error in errors), file=sys.stderr)
        return 1

    for badge in BADGES.values():
        if not (root / badge).is_file():
            raise FileNotFoundError(f"Missing badge asset: {badge}")

    path = root / "README.md"
    readme = path.read_bytes().decode("utf-8")
    updated = replace_tables(readme, render_overview(papers), OVERVIEW_BEGIN_MARKER, OVERVIEW_END_MARKER)
    updated = replace_tables(updated, render_tables(papers))
    updated = replace_badge_counts(updated, papers)
    if updated == readme:
        print(f"Validated {len(papers)} papers; README.md is up to date.")
        return 0
    if args.check:
        print("README.md is out of date. Run python3 scripts/update_readme.py.", file=sys.stderr)
        return 1
    path.write_bytes(updated.encode("utf-8"))
    print(f"Validated {len(papers)} papers; updated README.md.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)
