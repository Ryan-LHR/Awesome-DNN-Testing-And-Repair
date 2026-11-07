"""Validate the shared paper data and build the static paper browser."""

import json
import shutil
from pathlib import Path

from update_readme import validate_papers


def main():
    root = Path(__file__).resolve().parents[1]
    data = root / "data/papers.json"
    papers = json.loads(data.read_text(encoding="utf-8"))
    errors = validate_papers(papers)
    if errors:
        raise SystemExit("Invalid paper data:\n" + "\n".join(errors))

    output = root / "dist"
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(root / "site", output)
    (output / "data").mkdir()
    shutil.copy2(data, output / "data/papers.json")
    (output / ".nojekyll").touch()
    print(f"Built {len(papers)} papers into {output}")


if __name__ == "__main__":
    main()
