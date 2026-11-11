const languageNames = new Map([
  ['en', 'English'],
  ['zh-Hans', '简体中文'],
  ['zh-Hant', '繁體中文'],
]);

// English source strings map to their Simplified and Traditional Chinese translations.
const chineseStrings = {
  'Awesome DNN Testing and Repair': ['Awesome DNN 测试与修复', 'Awesome DNN 測試與修復'],
  'DNN Testing & Repair': ['DNN 测试与修复', 'DNN 測試與修復'],
  'DNN Testing': ['DNN 测试', 'DNN 測試'],
  '& Repair.': ['与修复。', '與修復。'],
  'Papers on testing, verification, and repair of deep neural networks.': ['收录深度神经网络测试、验证与修复相关论文。', '收錄深度神經網路測試、驗證與修復相關論文。'],
  'Language': ['界面语言', '介面語言'],
  'Language: {language}': ['界面语言：{language}', '介面語言：{language}'],
  'Switch to dark mode': ['切换到深色模式', '切換至深色模式'],
  'Switch to light mode': ['切换到浅色模式', '切換至淺色模式'],
  '{count} paper': ['{count} 篇论文', '{count} 篇論文'],
  '{count} papers': ['{count} 篇论文', '{count} 篇論文'],
  '{count} with code': ['{count} 篇含代码', '{count} 篇含程式碼'],
  'About this collection': ['关于论文库', '關於論文庫'],
  'Browse and filter papers': ['浏览与筛选论文', '瀏覽與篩選論文'],
  'Browse papers': ['浏览论文', '瀏覽論文'],
  'Paper categories': ['论文分类', '論文分類'],
  'All papers': ['全部论文', '全部論文'],
  'Research Papers': ['研究论文', '研究論文'],
  'Coverage Metrics': ['覆盖度量', '覆蓋度量'],
  'Test Generation': ['测试生成', '測試生成'],
  'Test Selection & Prioritization': ['测试选择与排序', '測試選擇與排序'],
  'Test Selection and Prioritization': ['测试选择与排序', '測試選擇與排序'],
  'Model Repair': ['模型修复', '模型修復'],
  'DNN Verification': ['DNN 验证', 'DNN 驗證'],
  'Other': ['其他', '其他'],
  'Surveys': ['综述', '綜述'],
  'Empirical Studies': ['实证研究', '實證研究'],
  'Topics': ['分类', '分類'],
  'Filters': ['筛选', '篩選'],
  'Filter papers': ['筛选论文', '篩選論文'],
  'Filter by': ['筛选条件', '篩選條件'],
  'Year': ['年份', '年份'],
  'All years': ['全部年份', '全部年份'],
  'Venue': ['期刊与会议', '期刊與會議'],
  'All venues': ['全部期刊与会议', '全部期刊與會議'],
  'All ranks': ['全部等级', '全部等級'],
  'Unspecified': ['未标注', '未標註'],
  'Search venues': ['搜索期刊或会议', '搜尋期刊或會議'],
  'No matching venues': ['没有匹配的期刊或会议', '找不到符合的期刊或會議'],
  'Clear selection': ['清空此组', '清除這組選取'],
  '{count} selected': ['已选 {count} 项', '已選取 {count} 項'],
  'Browse & filter': ['浏览与筛选', '瀏覽與篩選'],
  'Close filters': ['关闭筛选', '關閉篩選'],
  'Show {count}': ['查看 {count}', '查看 {count}'],
  'Suggest a paper': ['推荐论文', '推薦論文'],
  'Search papers': ['搜索论文', '搜尋論文'],
  'Search papers, authors, or keywords': ['搜索论文、作者或关键词', '搜尋論文、作者或關鍵字'],
  'Sort papers': ['论文排序', '論文排序'],
  'Newest first': ['最新优先', '最新優先'],
  'Oldest first': ['最早优先', '最早優先'],
  'Active filters': ['已选筛选条件', '已選篩選條件'],
  'Remove filter: {value}': ['移除筛选条件：{value}', '移除篩選條件：{value}'],
  'Clear filters': ['清除筛选', '清除篩選'],
  'With code': ['含代码', '含程式碼'],
  'Filtered papers': ['筛选结果', '篩選結果'],
  'Selected papers': ['所选分类论文', '所選分類論文'],
  'Show more papers': ['加载更多论文', '載入更多論文'],
  'No papers found': ['未找到论文', '找不到論文'],
  'Try a broader search or remove one of the filters.': ['试试更宽泛的关键词，或移除部分筛选条件。', '試試較廣泛的關鍵字，或移除部分篩選條件。'],
  'Reset search and filters': ['重置搜索与筛选', '重設搜尋與篩選'],
  'Preprint': ['预印本', '預印本'],
  'Full abstract': ['展开摘要', '展開摘要'],
  'Close abstract': ['收起摘要', '收合摘要'],
  'Paper': ['论文', '論文'],
  'Code': ['代码', '程式碼'],
  'Website': ['项目网站', '專案網站'],
  'Resources for {paper}': ['{paper} 的相关资源', '{paper} 的相關資源'],
  'Copy link to {paper}': ['复制 {paper} 的链接', '複製 {paper} 的連結'],
  'Copy link': ['复制链接', '複製連結'],
  'Copy link to this paper': ['复制这篇论文的链接', '複製這篇論文的連結'],
  'Link copied': ['链接已复制', '已複製連結'],
  'Paper link copied.': ['已复制论文链接。', '已複製論文連結。'],
  'A community-curated collection.': ['由社区共同维护的论文库。', '由社群共同維護的論文庫。'],
  'Asset credits': ['素材来源', '素材來源'],
  'About & Cite': ['关于与引用', '關於與引用'],
  'Close About & Cite': ['关闭关于与引用', '關閉關於與引用'],
  '{project} is a curated collection of papers on testing, verification, and repair of deep neural networks.': ['{project} 收录深度神经网络测试、验证与修复相关论文。', '{project} 收錄深度神經網路測試、驗證與修復相關論文。'],
  'Cite this collection': ['引用本项目', '引用本專案'],
  'Copy BibTeX': ['复制 BibTeX', '複製 BibTeX'],
  'BibTeX selected. Use your keyboard to copy it.': ['已选中 BibTeX，请使用键盘快捷键复制。', '已選取 BibTeX，請使用鍵盤快速鍵複製。'],
  'Copied': ['已复制', '已複製'],
  'BibTeX copied.': ['已复制 BibTeX。', '已複製 BibTeX。'],
  'Contribute': ['参与贡献', '參與貢獻'],
  'Recommend a paper': ['推荐论文', '推薦論文'],
  'Suggest a paper to add to the collection.': ['推荐一篇值得收录的论文。', '推薦一篇值得收錄的論文。'],
  'Report an error': ['报告条目错误', '回報條目錯誤'],
  'Flag a broken link or an incorrect paper detail.': ['报告失效链接或不准确的论文信息。', '回報失效連結或不正確的論文資訊。'],
  'Skip to papers': ['跳到论文列表', '跳至論文列表'],
  'Loading the paper collection…': ['正在加载论文库…', '正在載入論文庫…'],
  'Unable to load the paper collection': ['无法加载论文库', '無法載入論文庫'],
  'Please try again, or {link}.': ['请重试，或{link}。', '請重試，或{link}。'],
  'browse the collection on GitHub': ['在 GitHub 上浏览论文库', '在 GitHub 上瀏覽論文庫'],
  'Try again': ['重试', '重試'],
};

function readLanguage() {
  const requested = new URLSearchParams(location.search).get('lang');
  if (languageNames.has(requested)) return requested;
  try {
    const saved = localStorage.getItem('dnn-language');
    if (languageNames.has(saved)) return saved;
  } catch {}
  return 'en';
}

const language = readLanguage();
const chineseIndex = language === 'zh-Hant' ? 1 : 0;

function t(source, values) {
  const translation = Object.hasOwn(chineseStrings, source) ? chineseStrings[source] : null;
  const text = language !== 'en' && translation ? translation[chineseIndex] : source;
  return values ? text.replace(/\{(\w+)\}/g, (_, key) => values[key]) : text;
}
