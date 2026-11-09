const repo = 'https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair';
const topics = ['Coverage Metrics', 'Test Generation', 'Test Selection and Prioritization', 'Model Repair', 'DNN Verification', 'Other'];
const facetKeys = ['year', 'venue', 'ccf'];
const state = { categories: new Set(), query: '', year: new Set(), venue: new Set(), ccf: new Set(), withCode: false, oldest: false, limit: 12 };
const escape = (value = '') => String(value).replace(/[&<>"']/g, character => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[character]));
const yearOf = paper => paper.dates.publication_year || paper.dates.first_public_year;
const symbols = {
  search: '<circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 4 4"/>',
  arrow: '<path d="M7 17 17 7M7 7h10v10"/>',
  chevron: '<path d="m6 9 6 6 6-6"/>',
  sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2m0 16v2M2 12h2m16 0h2M5 5l1.5 1.5m11 11L19 19M5 19l1.5-1.5m11-11L19 5"/>',
  moon: '<path d="M20 15A8.5 8.5 0 0 1 9 4a8.5 8.5 0 1 0 11 11Z"/>',
  filter: '<path d="M4 7h16M4 17h16M9 4v6m6 4v6"/>',
  website: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c5 5 5 13 0 18-5-5-5-13 0-18Z"/>',
};
const icon = name => `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${symbols[name]}</svg>`;
const resourceIcons = {"paper": "<svg aria-hidden=\"true\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 16 16\"><path d=\"M0 1.75A.75.75 0 0 1 .75 1h4.253c1.227 0 2.317.59 3 1.501A3.743 3.743 0 0 1 11.006 1h4.245a.75.75 0 0 1 .75.75v10.5a.75.75 0 0 1-.75.75h-4.507a2.25 2.25 0 0 0-1.591.659l-.622.621a.75.75 0 0 1-1.06 0l-.622-.621A2.25 2.25 0 0 0 5.258 13H.75a.75.75 0 0 1-.75-.75Zm7.251 10.324.004-5.073-.002-2.253A2.25 2.25 0 0 0 5.003 2.5H1.5v9h3.757a3.75 3.75 0 0 1 1.994.574ZM8.755 4.75l-.004 7.322a3.752 3.752 0 0 1 1.992-.572H14.5v-9h-3.495a2.25 2.25 0 0 0-2.25 2.25Z\"/></svg>", "code": "<svg aria-hidden=\"true\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\" width=\"16\" height=\"16\" viewBox=\"0 0 16 16\"><path d=\"M6.766 11.328c-2.063-.25-3.516-1.734-3.516-3.656 0-.781.281-1.625.75-2.188-.203-.515-.172-1.609.063-2.062.625-.078 1.468.25 1.968.703.594-.187 1.219-.281 1.985-.281.765 0 1.39.094 1.953.265.484-.437 1.344-.765 1.969-.687.218.422.25 1.515.046 2.047.5.593.766 1.39.766 2.203 0 1.922-1.453 3.375-3.547 3.64.531.344.89 1.094.89 1.954v1.625c0 .468.391.734.86.547C13.781 14.359 16 11.53 16 8.03 16 3.61 12.406 0 7.984 0 3.563 0 0 3.61 0 8.031a7.88 7.88 0 0 0 5.172 7.422c.422.156.828-.125.828-.547v-1.25c-.219.094-.5.156-.75.156-1.031 0-1.64-.562-2.078-1.609-.172-.422-.36-.672-.719-.719-.187-.015-.25-.093-.25-.187 0-.188.313-.328.625-.328.453 0 .844.281 1.25.86.313.452.64.655 1.031.655s.641-.14 1-.5c.266-.265.47-.5.657-.656\"/></svg>", "arxiv": "<span class=\"arxiv-mark\" aria-hidden=\"true\"></span>"};
const resourceIcon = name => `<span class="resource-icon">${resourceIcons[name] || icon(name)}</span>`;
let papers = [];

const displayCategory = name => name === 'Test Selection and Prioritization' ? 'Test Selection & Prioritization' : name;
const abstractText = text => text.replace(/\\textbackslashtimes/g, '×').replace(/\\textbackslash/g, '\\').replace(/\\[%_]/g, match => match[1]).replace(/\\[()]/g, '');

function categoryButton(name, label) {
  return `<button class="category" data-category="${escape(name)}" aria-pressed="false"><span>${escape(label)}</span><span class="number"></span></button>`;
}

function fields() {
  const years = [...new Set(papers.map(yearOf))].sort((a, b) => b - a).map(String);
  const venues = [...new Set(papers.map(paper => paper.venue))].sort();
  return [['year', 'Year', 'All years', years], ['venue', 'Venue', 'All venues', venues], ['ccf', 'CCF', 'All ranks', ['A', 'B', 'C', 'Unspecified']]].map(([key, label, all, choices]) => `
    <details class="filter-field" data-facet="${key}">
      <summary><span>${label}</span><span class="facet-summary" data-empty="${all}">${all}</span>${icon('chevron')}</summary>
      ${key === 'venue' ? `<label class="venue-lookup">${icon('search')}<input type="search" placeholder="Search venues" aria-label="Search venues" autocomplete="off"></label>` : ''}
      <fieldset class="facet-options"><legend class="visually-hidden">${label}</legend>${choices.map(choice => `<label class="facet-option"><input type="checkbox" data-filter="${key}" value="${escape(choice)}"><span>${escape(choice)}</span><span class="facet-count" aria-hidden="true"></span></label>`).join('')}</fieldset>
      ${key === 'venue' ? '<p class="venue-no-match" role="status" hidden>No matching venues</p>' : ''}
      <button class="clear-facet" data-clear-facet="${key}" disabled>Clear selection</button>
    </details>`).join('');
}

function facetValue(paper, key) {
  return key === 'year' ? String(yearOf(paper)) : key === 'ccf' ? paper.ccf_rank || 'Unspecified' : paper.venue;
}

function matchesFacet(paper, key) {
  return !state[key].size || state[key].has(facetValue(paper, key));
}

function updateFacetControls(candidates) {
  document.querySelectorAll('[data-facet]').forEach(facet => {
    const key = facet.dataset.facet;
    const selected = state[key];
    const counts = new Map();
    for (const paper of candidates) {
      if (!facetKeys.every(other => other === key || matchesFacet(paper, other))) continue;
      const value = facetValue(paper, key);
      counts.set(value, (counts.get(value) || 0) + 1);
    }
    facet.querySelectorAll('.facet-option').forEach(option => {
      const input = option.querySelector('input');
      input.checked = selected.has(input.value);
      option.querySelector('.facet-count').textContent = counts.get(input.value) || 0;
    });
    const summary = facet.querySelector('.facet-summary');
    summary.textContent = selected.size === 1 ? [...selected][0] : selected.size ? `${selected.size} selected` : summary.dataset.empty;
    facet.querySelector('.clear-facet').disabled = !selected.size;
  });
}

function setTheme(theme) {
  document.documentElement.dataset.theme = theme;
  const button = document.querySelector('.theme-switch');
  button.innerHTML = icon(theme === 'dark' ? 'sun' : 'moon');
  button.setAttribute('aria-label', `Switch to ${theme === 'dark' ? 'light' : 'dark'} mode`);
  document.querySelector('meta[name="theme-color"]').content = theme === 'dark' ? '#151613' : '#f6f6f3';
  try { localStorage.setItem('dnn-theme', theme); } catch {}
}

function readURL() {
  const params = new URLSearchParams(location.search);
  const categories = [...topics, 'Surveys', 'Empirical Studies'];
  state.query = params.get('q') || '';
  state.categories = new Set(params.getAll('category').filter(category => categories.includes(category)));
  for (const key of facetKeys) {
    const choices = new Set([...document.querySelectorAll(`[data-filter="${key}"]`)].map(input => input.value));
    state[key] = new Set(params.getAll(key).filter(value => choices.has(value)));
  }
  state.withCode = params.get('code') === '1';
  state.oldest = params.get('sort') === 'oldest';
  state.limit = 12;
  document.querySelector('#search').value = state.query;
  document.querySelector('#sort').value = state.oldest ? 'oldest' : 'newest';
}

function syncURL() {
  const url = new URL(location.href);
  url.search = '';
  if (state.query.trim()) url.searchParams.set('q', state.query.trim());
  state.categories.forEach(category => url.searchParams.append('category', category));
  for (const key of facetKeys) state[key].forEach(value => url.searchParams.append(key, value));
  if (state.withCode) url.searchParams.set('code', '1');
  if (state.oldest) url.searchParams.set('sort', 'oldest');
  history.replaceState(null, '', url);
}

async function init() {
  const response = await fetch('data/papers.json');
  if (!response.ok) throw new Error(`Paper data returned HTTP ${response.status}`);
  const data = await response.json();
  papers = [...new Map(data.map(paper => [paper.id, paper])).values()];
  const years = papers.map(yearOf);
  document.querySelector('#app').innerHTML = `
    <svg class="icon-filters" aria-hidden="true"><defs><filter id="arxiv-white-to-alpha" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 -3 -3 -3 9 0"/></filter></defs></svg>
    <div class="shell">
      <header class="masthead">
        <a class="wordmark" href="./" aria-label="Awesome DNN Testing and Repair"><strong>awesome<span>.</span></strong><small>DNN Testing & Repair</small></a>
        <div class="masthead-actions"><a class="github-link" href="${repo}" target="_blank" rel="noreferrer">GitHub ${icon('arrow')}</a><button class="theme-switch" aria-label="Switch to dark mode">${icon('moon')}</button></div>
      </header>
      <section class="introduction" aria-label="About this collection">
        <h1>DNN Testing<br><span>& Repair.</span></h1>
        <div class="introduction-copy"><p>Papers on testing, verification, and repair of deep neural networks.</p><div class="collection-meta"><span><b>${papers.length}</b> papers</span><i aria-hidden="true">·</i><button class="with-code" aria-pressed="false"><b>${papers.filter(paper => paper.code_url).length}</b> with code</button><i aria-hidden="true">·</i><span>${Math.min(...years)}–${Math.max(...years)}</span></div></div>
      </section>
      <div class="library">
        <aside class="sidebar" id="sidebar" aria-label="Browse and filter papers">
          <div class="sidebar-tools">
            <h2 class="sidebar-title">Browse papers</h2>
            <button class="desktop-filter-shortcut" aria-controls="paper-categories filter-panel">${icon('filter')}<span>Filters</span></button>
          </div>
          <nav id="paper-categories" aria-label="Paper categories">${categoryButton('all', 'All papers')}<button class="research-label" data-category="research" aria-pressed="false">${icon('chevron')}Research Papers</button><div class="research-topics">${topics.map(category => categoryButton(category, displayCategory(category))).join('')}</div><div class="separate-topics">${['Surveys', 'Empirical Studies'].map(category => categoryButton(category, category)).join('')}</div></nav>
          <div class="filter-panel" id="filter-panel"><h2>Filter by</h2>${fields()}</div>
          <div class="contribution"><a href="${repo}/issues/new?template=01-recommend-paper.yml" target="_blank" rel="noreferrer">Suggest a paper ${icon('arrow')}</a></div>
        </aside>
        <main id="main" tabindex="-1">
          <div class="search-row"><label class="search-box">${icon('search')}<input id="search" type="search" aria-label="Search papers" placeholder="Search papers, authors, or keywords" autocomplete="off"><kbd aria-hidden="true">/</kbd></label><button class="mobile-filters" aria-haspopup="dialog" aria-controls="filter-dialog">${icon('filter')}Filters</button></div>
          <div class="results-heading"><div><h2 id="result-title">All papers</h2><span class="result-count" id="result-count" role="status" aria-atomic="true"></span></div><select class="sort-select" id="sort" aria-label="Sort papers"><option value="newest">Newest first</option><option value="oldest">Oldest first</option></select></div>
          <div class="selected-filters" id="selected-filters" aria-label="Active filters"></div>
          <div id="papers"></div><button class="load-more" id="load-more">Show more papers ↓</button>
        </main>
      </div>
      <footer class="site-footer"><span>A community-curated collection.</span><a href="assets/credits.html">Asset credits</a></footer>
    </div>
    <dialog class="filter-dialog" id="filter-dialog" aria-labelledby="filter-dialog-title">
      <div class="filter-dialog-heading"><h2 id="filter-dialog-title">Browse & filter</h2><button id="close-filters" aria-label="Close filters">×</button></div>
      <div id="mobile-sidebar"></div><div class="filter-dialog-footer"><button id="apply-filters"></button></div>
    </dialog>`;

  setTheme(document.documentElement.dataset.theme === 'dark' ? 'dark' : 'light');
  document.querySelector('.theme-switch').onclick = () => setTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');
  const dialog = document.querySelector('#filter-dialog');
  const sidebar = document.querySelector('#sidebar');
  const filterShortcut = sidebar.querySelector('.desktop-filter-shortcut');
  const sidebarTitle = sidebar.querySelector('.sidebar-title');
  filterShortcut.onclick = () => {
    const showFilters = sidebar.dataset.view !== 'filters';
    sidebar.dataset.view = showFilters ? 'filters' : 'topics';
    filterShortcut.querySelector('span').textContent = showFilters ? 'Topics' : 'Filters';
    sidebarTitle.textContent = showFilters ? 'Filter papers' : 'Browse papers';
    sidebar.scrollTop = 0;
  };

  const venueField = sidebar.querySelector('[data-facet="venue"]');
  const venueOptions = venueField.querySelector('.facet-options');
  const venueSearch = venueField.querySelector('input[type="search"]');
  const venueNoMatch = venueField.querySelector('.venue-no-match');
  venueSearch.oninput = () => {
    const query = venueSearch.value.trim().toLowerCase();
    let matches = 0;
    for (const option of venueOptions.querySelectorAll('.facet-option')) {
      const matchesQuery = option.querySelector('input').value.toLowerCase().includes(query);
      option.classList.toggle('venue-excluded', !matchesQuery);
      if (matchesQuery) matches++;
    }
    venueOptions.scrollTop = 0;
    venueNoMatch.hidden = matches > 0;
  };

  document.querySelector('.mobile-filters').onclick = () => {
    document.querySelector('#mobile-sidebar').append(sidebar);
    document.body.classList.add('filters-open');
    dialog.showModal();
  };
  const closeFilters = () => dialog.close();
  document.querySelector('#close-filters').onclick = closeFilters;
  document.querySelector('#apply-filters').onclick = closeFilters;
  dialog.addEventListener('click', event => { if (event.target === dialog) closeFilters(); });
  dialog.addEventListener('close', () => {
    document.querySelector('.library').prepend(sidebar);
    document.body.classList.remove('filters-open');
    document.querySelector('.mobile-filters').focus({ preventScroll: true });
  });
  matchMedia('(min-width: 801px)').addEventListener('change', event => { if (event.matches && dialog.open) closeFilters(); });
  document.querySelector('#search').oninput = event => { state.query = event.target.value; state.limit = 12; render(); };
  document.querySelector('#sort').onchange = event => { state.oldest = event.target.value === 'oldest'; render(); };
  document.querySelector('.with-code').onclick = () => {
    state.withCode = !state.withCode;
    state.limit = 12;
    render();
  };
  document.querySelectorAll('[data-category]').forEach(button => button.onclick = () => {
    const value = button.dataset.category;
    if (value === 'all') state.categories.clear();
    else if (value === 'research') {
      const active = topics.every(topic => state.categories.has(topic));
      topics.forEach(topic => active ? state.categories.delete(topic) : state.categories.add(topic));
    } else if (state.categories.has(value)) state.categories.delete(value);
    else state.categories.add(value);
    state.limit = 12;
    render();
  });
  document.querySelectorAll('[data-filter]').forEach(input => input.onchange = () => {
    const selected = state[input.dataset.filter];
    if (input.checked) selected.add(input.value);
    else selected.delete(input.value);
    state.limit = 12;
    render();
  });
  document.querySelectorAll('[data-clear-facet]').forEach(button => button.onclick = () => {
    state[button.dataset.clearFacet].clear();
    state.limit = 12;
    render();
  });
  document.querySelector('#load-more').onclick = () => { state.limit += 12; render(); };
  document.addEventListener('keydown', event => {
    if (event.key === '/' && !event.metaKey && !event.ctrlKey && !event.altKey && !dialog.open && !document.activeElement.closest('input, textarea, select, [contenteditable="true"]')) {
      event.preventDefault();
      document.querySelector('#search').focus();
    }
  });
  window.addEventListener('popstate', () => { readURL(); render(false); });
  readURL();
  render(false);
}

function paperCard(paper, expanded) {
  const year = yearOf(paper);
  const conference = paper.publication_type === 'conference';
  const venue = conference ? `${paper.venue}' ${year}` : paper.venue;
  const alias = paper.alias && !paper.title.toLowerCase().startsWith(paper.alias.toLowerCase()) ? paper.alias : '';
  const abstract = escape(abstractText(paper.abstract));
  const links = [['Paper', paper.paper_url], ['arXiv', paper.arxiv_url], ['Code', paper.code_url], ['Website', paper.website_url]].filter(([, url]) => url);
  return `<article class="paper" data-paper-id="${escape(paper.id)}" aria-labelledby="title-${escape(paper.id)}">
    <div class="paper-topline"><div class="publication"><span class="venue">${escape(venue)}</span>${!conference ? `<i aria-hidden="true">·</i><span>${year}</span>` : ''}${paper.ccf_rank ? `<span class="rank">CCF ${paper.ccf_rank}</span>` : paper.publication_type === 'preprint' ? '<span class="rank">Preprint</span>' : ''}</div>${alias ? `<span class="alias">${escape(alias)}</span>` : ''}</div>
    <h3 id="title-${escape(paper.id)}">${escape(paper.title)}</h3><p class="authors">${escape(paper.authors.join(', '))}</p><p class="abstract-excerpt">${abstract}</p>
    <details class="abstract-details"${expanded ? ' open' : ''}><summary><span class="closed-label">Full abstract</span><span class="open-label">Close abstract</span>${icon('chevron')}</summary><p class="abstract-full">${abstract}</p></details>
    <div class="paper-footer"><div class="paper-tags">${paper.categories.map(category => `<span>${escape(category)}</span>`).join('')}</div><div class="paper-resources" aria-label="Resources for ${escape(paper.alias || paper.title)}">${links.map(([label, url]) => `<a class="resource-link resource-${label.toLowerCase()}" href="${escape(url)}" target="_blank" rel="noreferrer">${resourceIcon(label.toLowerCase())}<span>${label}</span></a>`).join('')}</div></div>
  </article>`;
}

function render(updateURL = true) {
  const expanded = new Set([...document.querySelectorAll('.paper:has(details[open])')].map(paper => paper.dataset.paperId));
  const terms = state.query.toLowerCase().trim().split(/\s+/).filter(Boolean);
  const candidates = papers.filter(paper => {
    if (state.withCode && !paper.code_url) return false;
    const searchable = [paper.title, paper.alias, ...paper.authors, abstractText(paper.abstract)].join(' ').toLowerCase();
    return terms.every(term => searchable.includes(term));
  });
  const matchesCategory = paper => !state.categories.size || paper.categories.some(category => state.categories.has(category));
  const categoryPapers = candidates.filter(paper => facetKeys.every(key => matchesFacet(paper, key)));
  const results = categoryPapers.filter(matchesCategory)
    .sort((a, b) => (state.oldest ? 1 : -1) * (yearOf(a) - yearOf(b)));
  const count = `${results.length} ${results.length === 1 ? 'paper' : 'papers'}`;
  document.querySelector('#result-count').textContent = count;
  document.querySelector('#apply-filters').textContent = `Show ${count}`;
  document.querySelector('#result-title').textContent = state.categories.size === 1 ? displayCategory([...state.categories][0]) : state.categories.size === topics.length && topics.every(topic => state.categories.has(topic)) ? 'Research Papers' : state.categories.size ? 'Selected papers' : 'All papers';
  document.querySelectorAll('[data-category]').forEach(button => {
    const category = button.dataset.category;
    const active = category === 'all' ? !state.categories.size : category === 'research' ? topics.every(topic => state.categories.has(topic)) : state.categories.has(category);
    button.classList.toggle('active', active);
    button.setAttribute('aria-pressed', active);
    const number = button.querySelector('.number');
    if (number) number.textContent = category === 'all' ? categoryPapers.length : categoryPapers.filter(paper => paper.categories.includes(category)).length;
  });
  document.querySelector('.with-code').setAttribute('aria-pressed', state.withCode);
  const selected = [...state.categories].map(category => ['category', category]);
  for (const key of facetKeys) state[key].forEach(value => selected.push([key, value]));
  if (state.withCode) selected.push(['code', 'With code']);
  document.querySelector('#selected-filters').innerHTML = selected.length ? `${selected.map(([key, value]) => `<button data-remove="${key}" data-value="${escape(value)}" aria-label="Remove ${key} filter: ${escape(value)}">${escape(value)}<span aria-hidden="true">×</span></button>`).join('')}<button data-remove="all">Clear filters</button>` : '';
  document.querySelectorAll('[data-remove]').forEach(button => button.onclick = () => {
    const key = button.dataset.remove;
    if (key === 'category') state.categories.delete(button.dataset.value);
    else if (key === 'code') state.withCode = false;
    else if (key === 'all') {
      state.categories.clear();
      facetKeys.forEach(facet => state[facet].clear());
      state.withCode = false;
    }
    else state[key].delete(button.dataset.value);
    state.limit = 12;
    render();
  });
  document.querySelector('#papers').innerHTML = results.length ? results.slice(0, state.limit).map(paper => paperCard(paper, expanded.has(paper.id))).join('') : '<div class="empty"><h3>No papers found</h3><p>Try a broader search or remove one of the filters.</p><button class="reset-search">Reset search and filters</button></div>';
  const reset = document.querySelector('.reset-search');
  if (reset) reset.onclick = () => { history.replaceState(null, '', location.pathname); readURL(); render(); document.querySelector('#search').focus(); };
  document.querySelector('#load-more').hidden = results.length <= state.limit;
  updateFacetControls(candidates.filter(matchesCategory));
  if (updateURL) syncURL();
}

init().catch(error => {
  console.error(error);
  document.querySelector('#app').innerHTML = `<div class="loading"><h1>Unable to load the paper collection</h1><p>Please try again, or <a href="${repo}">browse the collection on GitHub</a>.</p><button class="load-more" id="retry">Try again</button></div>`;
  document.querySelector('#retry').onclick = () => location.reload();
});
