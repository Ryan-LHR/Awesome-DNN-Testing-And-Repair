# Paper browser

The browser uses the existing `data/papers.json` collection. Its HTML, CSS, JavaScript,
font, and icons are in `site/`. It has no package manager, framework, runtime API, or
external font dependency.

## Build and preview

From the repository root, with Python 3:

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Open <http://127.0.0.1:8000/>. Stop the server with Ctrl+C. Rebuild after editing
`site/` or `data/papers.json`. The build validates the paper data using the shared
validator in `scripts/update_readme.py` and creates the ignored `dist/` directory.
Do not edit generated files in `dist/`.

All site asset and data URLs are relative, so the same output works at a domain
root or a GitHub project subpath.

## Browsing behavior

- Search matches title, alias, authors, and the full abstract, ignoring case.
  Multiple search words must all match, in any of those fields.
- Multiple selected categories are combined with OR. Category, year, venue, and
  CCF filters are combined with AND. Papers are deduplicated by their data IDs.
- Research Papers includes all existing research categories, including DNN
  Verification. Surveys and Empirical Studies remain separate category choices.
- Years follow formal publication year, falling back to first public year for
  preprints. Conference labels use `ICSE' 2021`; journals use `TOSEM` with the year
  shown separately. Sorting is by year; ties retain data order.
- Titles are plain text. Paper, arXiv, Code, and Website links appear separately
  when present in the data. Abstracts expand in place. Common escaped percent,
  underscore, and multiplication symbols are displayed as readable text without
  changing the source data.
- Search, filters, and sort are stored in the URL for sharing or reloading.
  The default theme is light. A manually chosen theme is stored in this browser.
- Mobile filters open in a keyboard-accessible drawer. Escape, Close, or Show
  papers dismisses it. `/` focuses search.

## GitHub Pages

Review, commit, and push the source first. Publication is manual; pushing does not
deploy the site. Pull requests that touch website inputs run a build check.

1. In the repository, open **Settings → Pages → Build and deployment**.
2. Set **Source** to **GitHub Actions**.
3. Open **Actions → Deploy paper browser → Run workflow** and choose `main`.
4. Wait for the build and deploy jobs to finish. The deployment job reports the
   published URL.

For this repository the default project URL is:

<https://ryan-lhr.github.io/awesome-dnn-testing-and-repair/>

Run the workflow again after future paper or website updates. The workflow uses
GitHub's Pages artifact and deployment actions; it does not create a `gh-pages`
branch or require a personal access token. GitHub environment protection rules
still apply.

See [GitHub's custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [publishing source settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Assets

The accepted resource controls use the thin-border capsule design, the open-book
icon for Paper, the colored arXiv mark, and the GitHub mark for Code. Source and
license credits are linked from the site footer and included in `site/assets/`.
