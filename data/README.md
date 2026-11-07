# Paper data guide

[English](#english) · [简体中文](#简体中文)

## English

[papers.json](papers.json) is a JSON array with one record per publication. Edit it to add or correct papers; the README overviews, paper tables, and counts are generated from this file. Resource links appear in the READMEs only when recorded here. Keep conference and journal versions as separate records, with distinct IDs and aliases marked `(conf-version)` or `(journal-version)` when applicable.

[scan-log.json](scan-log.json) records the scan scope, sources, check dates, screening progress, and candidate or exclusion decisions. It supports incremental scans by identifying material already checked and reviews still pending. The log includes candidates awaiting review and excluded entries; README paper lists and counts use the accepted records in `papers.json`.

### Required fields

These fields are required by the current validation script. The [DeepXplore example](#deepxplore-example) below uses an existing record.

| Field | How to fill it |
| --- | --- |
| `id` | A unique, stable identifier, usually a lowercase name and year, such as `deepxplore-2017`. Preserve existing IDs. |
| `title` | Full original paper title. |
| `language` | Original paper language: `en` or `zh`. This is independent of the title's spelling or the README language. |
| `venue` | Short venue name, such as `SOSP` or `TOSEM`, without a year. The generator adds conference years. |
| `paper_url` | DOI URL or a link to the paper's publication page or preprint. |
| `categories` | A nonempty array of applicable categories from the list below. |
| `target_model_types` | A nonempty array containing `Non-LLM DNN`, `LLM`, and/or `QNN`, describing the models being tested, verified, repaired, or reviewed. |
| `abstract` | Original abstract, preserving its wording; remove PDF line breaks and layout artifacts only. |
| `publication_type` | `conference`, `journal`, or `preprint`. |
| `dates` | An object containing `publication_year` for conferences/journals or `first_public_year` for preprints. Years are integers. |

### Categories, dates, and optional fields

Use these category values exactly: `Coverage Metrics`, `Test Generation`, `Test Selection and Prioritization`, `Model Repair`, `DNN Verification`, `Other`, `Surveys`, `Empirical Studies`. `Research Papers` is a display group, not a stored category. Store a paper once even when it has several categories or model types; the generator displays it in each applicable section.

`Coverage Metrics` includes metric evaluation. Seed selection within fuzzing alone does not qualify as `Test Selection and Prioritization`.

`dates.publication_year` is the formal publication year; `online_year` is the online publication year; `first_public_year` and `first_public_date` record the first public release; `checked_on` records when the metadata was checked. Years must be four-digit integers; date strings must be valid calendar dates in `YYYY-MM-DD` format. Leave unavailable optional dates as `null` or omit them.

`dates.publication_date` is optional and records the first formal online publication date reported by the publisher for a conference or journal paper, including online-first publication. It is not the acceptance date or a later issue-assignment date, and may differ in year from `publication_year`. Do not infer it from a year alone.

Recent Papers uses `publication_date` for conference/journal papers and `first_public_date` for preprints; a revised preprint does not reset its date. Entries without the relevant exact date remain in the category tables but are excluded from Recent Papers. Each generation uses the previous month's same day through today, inclusive, clamping the start to that month's last day when needed. Matching entries appear once, newest first, without a count limit. The displayed range is a snapshot refreshed only when the generator runs.

| Optional field | How to fill it |
| --- | --- |
| `alias`, `venue_name`, `authors` | Paper/method name, full venue name, and an array of non-empty author names in publication order. `authors` may be omitted, `null`, or `[]`. |
| `doi`, `arxiv_url` | Bare DOI and full arXiv URL; no separate arXiv ID is needed. |
| `code_url`, `website_url` | Code/replication package and paper project website. Prefer the authors' GitHub repository when both GitHub and another package are available; replication packages such as Zenodo are also accepted as Code. |
| `ccf_rank` | Verified venue rank in the 2026 directory: `A`, `B`, or `C`; use `null` when unverified or unavailable. |
| `evidence`, `notes` | Optional source records with `url`, `label`, and `supports`, and a text note for relevant clarification. |

Omit unavailable optional fields or use `null` for unknown scalar metadata. Check for an existing record by title and DOI before adding one. English README tables include `en` papers; the Simplified Chinese README includes all papers. Top-level Papers and With code badges count the whole collection in both versions.

After editing, run these commands from the repository root and review the generated changes:

```sh
python3 scripts/update_readme.py
python3 scripts/update_readme.py --check
```

Both commands validate paper data and the scan log offline. Resource URLs must be absolute HTTP(S) URLs with a valid host, without whitespace, embedded credentials, or malformed percent escapes. Optional links remain optional.

Scan checks cover scope revisions, venue/year ranges, dates, source records, and the existing status vocabulary. Scan IDs and scope/cutoff combinations must be unique; source IDs and DOIs must be unique within each scan. The same paper may appear in later scan batches. Extend `SCAN_STATES` in the script when a new screening stage or decision has been reviewed; validation does not infer or change screening decisions.

For a separate network availability report:

```sh
python3 scripts/check_links.py --output work/link-check.json
```

This checks recorded Paper, arXiv, Code, and Website URLs once per distinct URL. It reports redirects, HTTP errors, and transport failures without changing data or READMEs. HTTP 401/403/429/451 responses indicate restricted access, not a confirmed dead link; even 404/410 responses need review. A successful response does not verify paper identity or full-text access. Reports belong in the ignored `work/` directory; no scheduled workflow is enabled.

## 简体中文

[papers.json](papers.json) 是一个 JSON 数组，每条记录对应一次发表。新增或纠正论文时修改该文件，README 的目录、论文表格和计数由脚本生成，资源链接仅在数据中已收录时显示。会议版与期刊扩展版分别保留，使用不同的 `id`，适用时在 `alias` 后标注 `(conf-version)` 或 `(journal-version)`。

[scan-log.json](scan-log.json) 保存扫描范围、来源、检查日期、筛选进度，以及候选或排除决定，供增量扫描时识别已检查内容和待完成的审核。台账包含待审核候选及排除条目；README 论文列表与计数以 `papers.json` 中已收录的记录为准。

当前脚本要求填写：`id`、`title`、`language`、`venue`、`paper_url`、`categories`、`target_model_types`、`abstract`、`publication_type` 和 `dates`。具体规则如下：

- `id` 唯一且保持稳定，例如 `deepxplore-2017`；`title` 保留原文完整标题；`abstract` 保留原文摘要，只清理 PDF 断行和排版问题。
- `language` 表示论文原文语言，取 `en` 或 `zh`，不根据标题文字或 README 语言推断。
- `venue` 只写会议／期刊简称，例如 `SOSP`、`TOSEM`，不拼接年份；`paper_url` 填 DOI 链接、出版页面或预印本链接。
- `categories` 至少包含一个上方列出的英文分类值，可多选；`Research Papers` 只是展示分组，不写入数组。`target_model_types` 至少包含一个 `Non-LLM DNN`、`LLM` 或 `QNN`，表示被测试、验证、修复或综述的模型。同篇论文即使属于多个分类或模型对象，也只存一条记录。
- 覆盖度量可以包含指标评估；模糊测试中的种子选择本身不归入测试选择与排序。
- `publication_type` 取 `conference`、`journal` 或 `preprint`。`dates` 将时间字段放在同一个对象内：会议／期刊必填正式发表年 `publication_year`，预印本必填首次公开年 `first_public_year`，年份使用整数。
- `dates.online_year` 表示在线发表年，`first_public_date` 表示首次公开日期，`checked_on` 表示元数据核查日期。年份必须为四位整数，日期字符串使用 `YYYY-MM-DD` 且必须是实际存在的日期；未知的可选时间字段可填 `null` 或省略。
- 可选的 `dates.publication_date` 保存出版方公布的会议／期刊论文首次正式在线发表日期，包含 online-first；不使用录用日期或后续编入卷期的日期，其年份可能与 `publication_year` 不同。不能仅凭年份推算，未知时省略或填 `null`。

近期论文栏目对会议／期刊使用 `publication_date`，对预印本使用 `first_public_date`，预印本修订不重置日期。缺少相应精确日期的论文仍保留在分类正文中，不进入近期栏目。每次生成使用上月同日至当天的闭区间；上月没有对应日期时取其最后一天。匹配论文按日期降序展示，每篇只出现一次，不限制条数。展示的时间范围是快照，仅在运行生成脚本时刷新。

其余字段均为可选：`alias` 是论文／方法简称，`venue_name` 是来源全称，`authors` 按原文顺序保存作者姓名数组，每个姓名必须是非空字符串，字段可省略、填 `null` 或空数组 `[]`；`doi` 保存 DOI 本身，`arxiv_url` 保存完整链接，不另存 arXiv ID。`code_url` 可指向作者代码或正式复现包，同时有 GitHub 和其他复现包时优先 GitHub；`website_url` 指论文项目网站。`ccf_rank` 依据 2026 年目录保存已核实的来源评级 `A`、`B` 或 `C`，未核实或无对应评级时填 `null`。`evidence` 可记录包含 `url`、`label`、`supports` 的来源对象，`notes` 用于必要的文字补充。

可选字段缺失时可省略，未知的可选标量元数据可填 `null`。新增前按标题和 DOI 查重。英文 README 只展示 `en` 论文，简体中文版展示全部论文；两版顶部 Papers 和 With code 徽章都统计全库。

修改后在仓库根目录运行上面的两条命令，再审核生成的差异。[下方 DeepXplore 示例](#deepxplore-example) 同时属于覆盖度量和测试生成，展示了多分类的填写方式。

这两条命令均离线校验论文数据和扫描台账。资源链接必须是带有效主机名的完整 HTTP(S) URL，不含空白、内嵌账号密码或错误的百分号转义；可选链接仍可省略或填 `null`。

台账校验覆盖范围版本、来源与年份范围、日期、来源记录及现有状态用语。扫描 ID 和范围／截止日期组合不能重复；同一批次内的来源 ID 和 DOI 不能重复，同篇论文可以出现在后续扫描批次。新增筛选阶段或决定经审核后，再扩展脚本中的 `SCAN_STATES`；校验不会推断或修改收录决定。

联网巡检单独使用上面的 `scripts/check_links.py` 命令，对已有 Paper、arXiv、Code 和 Website 链接去重访问，报告重定向、HTTP 错误及网络故障，不修改数据或 README。401/403/429/451 表示访问受限，不能据此判断链接失效；404/410 也需复核。响应成功不代表已核实论文身份或取得全文。报告保存在已忽略的 `work/` 目录，目前不启用定时工作流。

<a name="deepxplore-example"></a>

## DeepXplore example / 示例

Copied from the existing record; optional `evidence` and `notes` are omitted. / 取自现有记录，仅省略可选的 `evidence` 和 `notes`。

```json
{
  "id": "deepxplore-2017",
  "title": "DeepXplore: Automated Whitebox Testing of Deep Learning Systems",
  "language": "en",
  "venue": "SOSP",
  "venue_name": "Proceedings of the 26th Symposium on Operating Systems Principles",
  "paper_url": "https://doi.org/10.1145/3132747.3132785",
  "alias": "DeepXplore",
  "categories": [
    "Coverage Metrics",
    "Test Generation"
  ],
  "target_model_types": [
    "Non-LLM DNN"
  ],
  "authors": [
    "Kexin Pei",
    "Yinzhi Cao",
    "Junfeng Yang",
    "Suman Jana"
  ],
  "abstract": "Deep learning (DL) systems are increasingly deployed in safety- and security-critical domains including self-driving cars and malware detection, where the correctness and predictability of a system’s behavior for corner case inputs are of great importance. Existing DL testing depends heavily on manually labeled data and therefore often fails to expose erroneous behaviors for rare inputs. We design, implement, and evaluate DeepXplore, the first whitebox framework for systematically testing real-world DL systems. First, we introduce neuron coverage for systematically measuring the parts of a DL system exercised by test inputs. Next, we leverage multiple DL systems with similar functionality as cross-referencing oracles to avoid manual checking. Finally, we demonstrate how finding inputs for DL systems that both trigger many differential behaviors and achieve high neuron coverage can be represented as a joint optimization problem and solved efficiently using gradient-based search techniques. DeepXplore efficiently finds thousands of incorrect corner case behaviors (e.g., self-driving cars crashing into guard rails and malware masquerading as benign software) in state-of-the-art DL models with thousands of neurons trained on five popular datasets including ImageNet and Udacity self-driving challenge data. For all tested DL models, on average, DeepXplore generated one test input demonstrating incorrect behavior within one second while running only on a commodity laptop. We further show that the test inputs generated by DeepXplore can also be used to retrain the corresponding DL model to improve the model’s accuracy by up to 3%.",
  "publication_type": "conference",
  "ccf_rank": "A",
  "dates": {
    "publication_year": 2017,
    "online_year": 2017,
    "first_public_year": 2017,
    "first_public_date": "2017-05-18",
    "checked_on": "2026-10-28"
  },
  "doi": "10.1145/3132747.3132785",
  "arxiv_url": "https://arxiv.org/abs/1705.06640",
  "code_url": "https://github.com/peikexin9/deepxplore"
}
```
