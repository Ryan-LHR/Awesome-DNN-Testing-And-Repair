# Paper data guide

[English](#english) · [简体中文](#简体中文)

## English

[papers.json](papers.json) is a JSON array with one record per publication. Edit it to add or correct papers; the README overviews, paper tables, and counts are generated from this file. Keep conference and journal versions as separate records, with distinct IDs and aliases marked `(conf-version)` or `(journal-version)` when applicable.

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
| `target_model_types` | A nonempty array containing `Non-LLM DNN`, `LLM`, and/or `QNN`, describing the models studied. |
| `abstract` | Original abstract, preserving its wording; remove PDF line breaks and layout artifacts only. |
| `publication_type` | `conference`, `journal`, or `preprint`. |
| `dates` | An object containing `publication_year` for conferences/journals or `first_public_year` for preprints. Years are integers. |

### Categories, dates, and optional fields

Use these category values exactly: `Coverage Metrics`, `Test Generation`, `Test Selection and Prioritization`, `Model Repair`, `DNN Verification`, `Other`, `Surveys`, `Empirical Studies`. `Research Papers` is a display group, not a stored category. Store a paper once even when it has several categories or model types; the generator displays it in each applicable section.

`Coverage Metrics` includes metric evaluation. Seed selection within fuzzing alone does not qualify as `Test Selection and Prioritization`.

`dates.publication_year` is the formal publication year; `online_year` is the online publication year; `first_public_year` and `first_public_date` record the first public release; `checked_on` records when the metadata was checked. Date strings use `YYYY-MM-DD`. Leave unavailable optional dates as `null` or omit them.

| Optional field | How to fill it |
| --- | --- |
| `alias`, `venue_name`, `authors` | Paper/method name, full venue name, and an array of author names in publication order. |
| `doi`, `arxiv_url` | Bare DOI and full arXiv URL; no separate arXiv ID is needed. |
| `code_url`, `website_url` | Code/replication package and paper project website. Prefer the authors' GitHub repository when both GitHub and another package are available; replication packages such as Zenodo are also accepted as Code. |
| `ccf_rank` | Verified venue rank: `A`, `B`, or `C`; use `null` when unverified or unavailable. |
| `evidence`, `notes` | Optional source records with `url`, `label`, and `supports`, and a text note for relevant clarification. |

Omit unavailable optional fields or use `null` for unknown scalar metadata. Check for an existing record by title and DOI before adding one. English README tables include `en` papers; the Simplified Chinese README includes all papers. Top-level Papers and With code badges count the whole collection in both versions.

After editing, run these commands from the repository root and review the generated changes:

```sh
python3 scripts/update_readme.py
python3 scripts/update_readme.py --check
```

## 简体中文

[papers.json](papers.json) 是一个 JSON 数组，每条记录对应一次发表。新增或纠正论文时修改该文件，README 的目录、论文表格和计数由脚本生成。会议版与期刊扩展版分别保留，使用不同的 `id`，适用时在 `alias` 后标注 `(conf-version)` 或 `(journal-version)`。

当前脚本要求填写：`id`、`title`、`language`、`venue`、`paper_url`、`categories`、`target_model_types`、`abstract`、`publication_type` 和 `dates`。具体规则如下：

- `id` 唯一且保持稳定，例如 `deepxplore-2017`；`title` 保留原文完整标题；`abstract` 保留原文摘要，只清理 PDF 断行和排版问题。
- `language` 表示论文原文语言，取 `en` 或 `zh`，不根据标题文字或 README 语言推断。
- `venue` 只写会议／期刊简称，例如 `SOSP`、`TOSEM`，不拼接年份；`paper_url` 填 DOI 链接、出版页面或预印本链接。
- `categories` 至少包含一个上方列出的英文分类值，可多选；`Research Papers` 只是展示分组，不写入数组。`target_model_types` 至少包含一个 `Non-LLM DNN`、`LLM` 或 `QNN`。同篇论文即使属于多个分类或模型对象，也只存一条记录。
- 覆盖度量可以包含指标评估；模糊测试中的种子选择本身不归入测试选择与排序。
- `publication_type` 取 `conference`、`journal` 或 `preprint`。`dates` 将时间字段放在同一个对象内：会议／期刊必填正式发表年 `publication_year`，预印本必填首次公开年 `first_public_year`，年份使用整数。
- `dates.online_year` 表示在线发表年，`first_public_date` 表示首次公开日期，`checked_on` 表示元数据核查日期。日期字符串使用 `YYYY-MM-DD`；未知的可选时间字段可填 `null` 或省略。

其余字段均为可选：`alias` 是论文／方法简称，`venue_name` 是来源全称，`authors` 按原文顺序保存作者姓名数组；`doi` 保存 DOI 本身，`arxiv_url` 保存完整链接，不另存 arXiv ID。`code_url` 可指向作者代码或正式复现包，同时有 GitHub 和其他复现包时优先 GitHub；`website_url` 指论文项目网站。`ccf_rank` 保存已核实的来源评级 `A`、`B` 或 `C`，未核实或无对应评级时填 `null`。`evidence` 可记录包含 `url`、`label`、`supports` 的来源对象，`notes` 用于必要的文字补充。

可选字段缺失时可省略，未知的可选标量元数据可填 `null`。新增前按标题和 DOI 查重。英文 README 只展示 `en` 论文，简体中文版展示全部论文；两版顶部 Papers 和 With code 徽章都统计全库。

修改后在仓库根目录运行上面的两条命令，再审核生成的差异。[下方 DeepXplore 示例](#deepxplore-example) 同时属于覆盖度量和测试生成，展示了多分类的填写方式。

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
