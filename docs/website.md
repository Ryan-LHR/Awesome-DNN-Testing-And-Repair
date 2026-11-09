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
- Categories, years, venues, and CCF ranks all support multiple selections. Year,
  Venue, and CCF use expandable checkbox lists. Selections within a group are
  combined with OR; the groups are combined with AND. For example, selecting 2024
  and 2025 plus ICSE and TOSEM matches papers from either year at either venue.
  An empty group matches all values. Each selected value can be removed
  individually, each checkbox group has a clear action, and Clear filters resets
  all groups. Papers are deduplicated by their data IDs.
- On desktop, use **Filters** at the top of the sidebar to show the filters and
  **Topics** to return to categories. **Search venues** narrows the Venue options
  while keeping current selections.
- Option counts reflect the search and other filter groups. The group's own
  selections are excluded so other choices in the same group remain comparable.
- The `with code` count in the collection header toggles a filter for papers
  with a code link. It combines with other filters and is shared as `code=1`.
- With a search or filter active and no topic selected, the results heading is
  **Filtered papers**.
- Research Papers includes all existing research categories, including DNN
  Verification. Surveys and Empirical Studies remain separate category choices.
- Years follow formal publication year, falling back to first public year for
  preprints. Conference labels use `ICSE' 2021`; journals use `TOSEM` with the year
  shown separately. Sorting is by year; ties retain data order.
- Titles are plain text. Paper, arXiv, Code, and Website links appear separately
  when present in the data. If Paper and arXiv point to the same URL, only
  arXiv is shown. Abstracts expand in place. Common escaped percent, underscore,
  and multiplication symbols are displayed as readable text without changing
  the source data.
- Search, filters, and sort are stored in the URL for sharing or reloading.
  Multiselect groups use repeated parameters, such as `year=2024&year=2025`;
  existing links with a single year, venue, or CCF rank remain supported.
  The default theme is light. A manually chosen theme is stored in this browser.
- On desktop, **Copy link** at the top right of a paper card copies its direct
  link. Opening it loads and scrolls to that paper, even past the first 12 results.
- Mobile filters open in a keyboard-accessible drawer. Escape, Close, or Show
  papers dismisses it. `/` focuses search.

## GitHub Pages

After reviewing changes locally, commit and push to `main`. Changes to `site/`,
`data/papers.json`, the build or shared validation script, or the Pages workflow
automatically build and deploy the site. Pull requests run a build check only;
they do not publish. Documentation-only and README-only changes do not deploy.

1. In the repository, open **Settings → Pages → Build and deployment**.
2. Set **Source** to **GitHub Actions**.
3. Push a website or paper-data change to `main`.
4. Open **Actions → Deploy paper browser** and wait for the build and deploy jobs
   to finish. The deployment job reports the published URL.

To republish manually, open **Actions → Deploy paper browser → Run workflow** and
choose `main`. This remains available alongside automatic publishing.

For this repository the default project URL is:

<https://ryan-lhr.github.io/Awesome-DNN-Testing-And-Repair/>

Future paper and website updates publish automatically after their push to `main`.
The workflow uses GitHub's Pages artifact and deployment actions; it does not
create a `gh-pages` branch or require a personal access token. GitHub environment
protection rules still apply.

See [GitHub's custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages)
and [publishing source settings](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Assets

The accepted resource controls use the thin-border capsule design, the open-book
icon for Paper, the colored arXiv mark, and the GitHub mark for Code. Source and
license credits are linked from the site footer and included in `site/assets/`.
