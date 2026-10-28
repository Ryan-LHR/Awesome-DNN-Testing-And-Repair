# Awesome DNN Testing and Repair

A curated pilot collection on testing, diagnosing, and repairing deep neural networks.

[English](README.md) · [简体中文](README.zh-CN.md)

**Seed pilot: 14 papers.** Evidence checked as of 2026-10-28. This is not an exhaustive survey; classifications and original one-line notes await maintainer review.

DNN models and their behavior; library/compiler testing and AI-assisted testing of ordinary software are adjacent topics, not the core corpus. Repair, mutation testing, and test selection still need additional seeds.

First public means the earliest public record verified so far, rather than a guarantee that no earlier version exists. It is stored separately from the publication year.

[Browse / 检索页面](site/index.html) · [By first public year / 首发年](docs/by-year.md) · [By venue / 发表来源](docs/by-venue.md) · [Seed review / 种子核验](docs/SEED_REVIEW.md)

[Workflow / 工作流](docs/WORKFLOW.md) · [Search protocol / 检索规则](docs/SEARCH_PROTOCOL.md) · [Taxonomy / 分类规则](docs/TAXONOMY.md) · [Validation / 验证记录](docs/VALIDATION.md) · [Contribute / 贡献](CONTRIBUTING.md)

> Generated from `data/papers.json` and `data/catalog.json`. Edit the data, then run `python3 scripts/catalog.py build`.

## Topics / 研究主题

### Test generation / 测试生成 (8)

- **IATT: Interpretation Analysis-based Transferable Test Generation for Convolutional Neural Networks** · TOSEM 2025 · first public 2025
  - Uses interpretation-guided perturbations on surrogate models to generate transferable tests for black-box targets.
  - [Paper](https://doi.org/10.1145/3705301) · `iatt-2025`

- **A White-Box Testing for Deep Neural Networks Based on Neuron Coverage** · TNNLS 2023 · first public 2022
  - Tracks inactive neurons and optimizes test inputs to expose inconsistent DNN behavior.
  - [Paper](https://doi.org/10.1109/tnnls.2022.3156620) · `test4deep-journal-2023`

- **CAGFuzz: Coverage-Guided Adversarial Generative Fuzzing Testing for Image-Based Deep Learning Systems** · TSE 2022 · first public 2022
  - Combines adversarial generation and coverage feedback to test image-based deep learning systems.
  - [Paper](https://doi.org/10.1109/tse.2021.3124006) · `cagfuzz-2022`

- **CoCoFuzzing: Testing Neural Code Models With Coverage-Guided Fuzzing** · TR 2023 · first public 2021
  - Uses semantics-preserving code transformations and coverage feedback to test neural code models.
  - [Paper](https://doi.org/10.1109/tr.2022.3208239) · `cocofuzzing-2023`

- **Test4Deep: an Effective White-Box Testing for Deep Neural Networks** · CSE/EUC 2019 · first public 2019
  - Presents a white-box DNN testing approach under the Test4Deep name.
  - [Paper](https://doi.org/10.1109/cse/euc.2019.00013) · `test4deep-2019`

- **DeepHunter: A Coverage-Guided Fuzz Testing Framework for Deep Neural Networks** · ISSTA 2019 · first public 2018
  - Combines metamorphic mutations and coverage feedback to search for DNN failures.
  - [Paper](https://doi.org/10.1145/3293882.3330579) · `deephunter-2019`

- **DeepRoad: GAN-Based Metamorphic Testing and Input Validation Framework for Autonomous Driving Systems** · ASE 2018 · first public 2018
  - Uses GAN-based image transformations in metamorphic testing of driving models.
  - [Paper](https://doi.org/10.1145/3238147.3238187) · `deeproad-2018`

- **DeepXplore: Automated Whitebox Testing of Deep Learning Systems** · SOSP 2017 · first public 2017
  - Combines neuron coverage and differential behavior to generate failure-revealing inputs.
  - [Paper](https://doi.org/10.1145/3132747.3132785) · [Code](https://github.com/peikexin9/deepxplore) · `deepxplore-2017`

### Test adequacy and coverage / 测试充分性与覆盖准则 (2)

- **NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks** · TOSEM 2022 · first public 2022
  - Characterizes model decision paths and defines path-based test adequacy criteria.
  - [Paper](https://doi.org/10.1145/3490489) · [Code](https://github.com/ltl7155/NPC) · `npc-2022`

- **DeepCon: Contribution Coverage Testing for Deep Learning Systems** · SANER 2021 · first public 2021
  - Introduces contribution coverage as a criterion for assessing and guiding DNN tests.
  - [Paper](https://doi.org/10.1109/saner50967.2021.00026) · `deepcon-2021`

### Test selection and prioritization / 测试选择与优先级 (0)

Seed collection pending / 等待补充种子论文。

### Mutation testing / 变异测试 (0)

Seed collection pending / 等待补充种子论文。

### Fault localization and repair / 故障定位与模型修复 (1)

- **AI-Lancet: Locating Error-inducing Neurons to Optimize Neural Networks** · CCS 2021 · first public 2021
  - Locates error-inducing neurons to support targeted correction of neural network behavior.
  - [Paper](https://doi.org/10.1145/3460120.3484818) · `ai-lancet-2021`

### Empirical studies / 实证研究与评估 (2)

- **Correlations between Deep Neural Network Model Coverage Criteria and Model Quality** · ESEC/FSE 2020 · first public 2020
  - Studies correlations between coverage criteria, model quality, test generation, and retraining.
  - [Paper](https://doi.org/10.1145/3368089.3409671) · `coverage-quality-2020`

- **Towards Characterizing Adversarial Defects of Deep Learning Software from the Lens of Uncertainty** · ICSE 2020 · first public 2020
  - Studies uncertainty patterns of benign and adversarial inputs and generates underexplored cases.
  - [Paper](https://doi.org/10.1145/3377811.3380368) · `uncertainty-2020`

### Surveys / 综述 (1)

- **Machine Learning Testing: Survey, Landscapes and Horizons** · TSE 2022 · first public 2019
  - Maps ML testing properties, components, workflows, and application scenarios.
  - [Paper](https://doi.org/10.1109/tse.2019.2962027) · `ml-testing-survey-2022`

## Local use

```sh
python3 scripts/catalog.py validate
python3 scripts/catalog.py build
python3 scripts/catalog.py build --check
python3 -m unittest discover -s tests
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/site/` after starting the local server. The catalogue also works by opening `site/index.html` directly.

## Release status

Local workflow prototype. No hosted site or public repository has been published. Select a content/code license and review the seed records before public release. Linked papers and code retain their authors’ terms.
