<p align="center">
  <img src="assets/banner.svg" alt="Awesome DNN Testing and Repair — 测试、验证、修复" width="100%" />
</p>

<h1 align="center">Awesome DNN Testing and Repair</h1>

<p align="center">
<a href="#papers"><img alt="Papers" src="https://img.shields.io/badge/Papers-146-00629B?style=flat" /></a> <a href="data/papers.json"><img alt="With code" src="https://img.shields.io/badge/With%20code-90-B45309?style=flat" /></a> <a href="https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/Ryan-LHR/awesome-dnn-testing-and-repair?style=flat&amp;label=Stars&amp;color=E2BF46" /></a> <a href="https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/forks"><img alt="Forks" src="https://img.shields.io/github/forks/Ryan-LHR/awesome-dnn-testing-and-repair?style=flat&amp;label=Forks&amp;color=00629B" /></a> <a href="https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair"><img alt="Visitors" src="https://komarev.com/ghpvc/?username=Ryan-LHR-awesome-dnn-testing-and-repair&amp;label=Visitors&amp;color=1283c3&amp;style=flat" /></a> <a href="data/papers.json"><img alt="Data" src="https://img.shields.io/badge/Data-JSON-087CA7?style=flat" /></a> <a href="https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/Ryan-LHR/awesome-dnn-testing-and-repair?style=flat&amp;label=Last%20commit&amp;color=087CA7" /></a> <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-E2BF46?style=flat" /></a> <a href="https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/pulls"><img alt="PRs welcome" src="https://img.shields.io/badge/PRs-welcome-21865B?style=flat" /></a>
</p>

<p align="center">
<a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-d9d9d9?style=flat" /></a> <a href="README.zh-Hans.md" aria-current="page"><img alt="简体中文" src="https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-00629B?style=flat" /></a> <a href="README.zh-Hant.md"><img alt="繁體中文" src="https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-d9d9d9?style=flat" /></a>
</p>

深度神经网络测试、验证与修复相关论文合集。

<a name="overview"></a>

## 📋 概览

本项目关注深度神经网络模型的测试、验证与修复，整理相关论文的发表信息，并提供已收录的论文、预印本和代码链接。

<!-- BEGIN GENERATED OVERVIEW -->

- **[研究论文](#research-papers)** (141)
  - [覆盖度量](#coverage-metrics) (24)
  - [测试生成](#test-generation) (43)
  - [测试选择与排序](#test-selection-and-prioritization) (43)
  - [模型修复](#model-repair) (40)
  - [DNN 验证](#dnn-verification) (3)
  - [其他](#other) (1)
- **[综述](#surveys)** (5)
- **[实证研究](#empirical-studies)** (16)

同一篇论文可能归入多个类别。

<!-- END GENERATED OVERVIEW -->

<a name="papers"></a>

## 📄 论文列表

每个类别内按研究对象分组：非 LLM 深度神经网络、大语言模型（LLM）和量子神经网络（QNN）。研究对象指论文中被测试、验证、修复或综述的模型；涉及多种模型的论文会出现在各个适用分组中。

各分组内，已发表论文按正式发表年份降序排列；预印本采用首次公开年份，并作相应标注。预印本日期和在线发表日期分别记录在[论文数据](data/papers.json)中。

资源链接仅在论文数据中已收录时显示。

论文数据中的 CCF 评级依据 2026 年目录；`null` 表示尚未记录经核实的评级。

<!-- BEGIN GENERATED PAPERS -->

<a name="research-papers"></a>

### 研究论文

<a name="coverage-metrics"></a>

#### 覆盖度量

##### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2024 | — | Can Coverage Criteria Guide Failure Discovery for Image Classifiers? An Empirical Study | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3672446) | TOSEM |
| 2023 | **ATOM** | ATOM: Automated Black-Box Testing of Multi-Label Image Classification Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/ase56229.2023.00156) | ASE<br>2023 |
| 2023 | **SA**<br>(journal-version) | Evaluating Surprise Adequacy for Deep Learning System Testing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3546947)<br>[![Code](assets/badges/code.svg)](https://github.com/coinse/sadl) | TOSEM |
| 2023 | **IDC** | Input Distribution Coverage: Measuring Feature Interaction Adequacy in Neural Network Testing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3576040)<br>[![Code](assets/badges/code.svg)](https://github.com/less-lab-uva/InputDistributionCoverage) | TOSEM |
| 2022 | **testRNN** | Coverage-Guided Testing for Recurrent Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tr.2021.3080664)<br>[![Code](assets/badges/code.svg)](https://github.com/TrustAI/testRNN) | TR |
| 2022 | — | Is Neuron Coverage Needed to Make Person Detection More Robust? | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/cvprw56347.2022.00326) | CVPRW<br>2022 |
| 2022 | **NPC** | NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3490489)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2203.12915)<br>[![Code](assets/badges/code.svg)](https://github.com/ltl7155/NPC) | TOSEM |
| 2022 | **RNN-Test** | RNN-Test: Towards Adversarial Testing for Recurrent Neural Network Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2021.3114353) | TSE |
| 2021 | — | A Review and Refinement of Surprise Adequacy | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/deeptest52559.2021.00009)<br>[![Code](assets/badges/code.svg)](https://github.com/testingautomated-usi/surprise-adequacy) | DeepTest (workshop)<br>2021 |
| 2021 | — | Are Coverage Criteria Meaningful Metrics for DNNs? | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/ijcnn52387.2021.9533987) | IJCNN<br>2021 |
| 2021 | **DeepCon** | DeepCon: Contribution Coverage Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner50967.2021.00026) | SANER<br>2021 |
| 2020 | — | An Empirical Study on Correlation between Coverage and Robustness for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/iceccs51672.2020.00016)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1911.05904) | ICECCS<br>2020 |
| 2020 | — | Correlations between Deep Neural Network Model Coverage Criteria and Model Quality | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3368089.3409671)<br>[![Code](assets/badges/code.svg)](https://github.com/RU-System-Software-and-Security/CovTesting) | ESEC/FSE<br>2020 |
| 2020 | — | Is neuron coverage a meaningful measure for testing deep neural networks? | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3368089.3409754)<br>[![Code](assets/badges/code.svg)](https://doi.org/10.5281/zenodo.4021473) | ESEC/FSE<br>2020 |
| 2019 | **DeepCT** | DeepCT: Tomographic Combinatorial Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner.2019.8668044) | SANER<br>2019 |
| 2019 | **DeepPath** | DeepPath: Path-Driven Testing Criteria for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/aitest.2019.00013) | AITest<br>2019 |
| 2019 | **DeepStellar** | DeepStellar: model-based quantitative analysis of stateful deep learning systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3338906.3338954) | ESEC/FSE<br>2019 |
| 2019 | **SA**<br>(conf-version) | Guiding Deep Learning System Testing Using Surprise Adequacy | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse.2019.00108)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1808.08444) | ICSE<br>2019 |
| 2019 | — | Structural Coverage Criteria for Neural Networks Could Be Misleading | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse-nier.2019.00031) | ICSE-NIER<br>2019 |
| 2019 | — | Structural Test Coverage Criteria for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3358233)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1803.04792)<br>[![Code](assets/badges/code.svg)](https://github.com/TrustAI/DeepConcolic) | TECS |
| 2019 | — | Towards Improved Testing For Deep Learning | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse-nier.2019.00030)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1902.06320) | ICSE-NIER<br>2019 |
| 2018 | **DeepGauge** | DeepGauge: multi-granularity testing criteria for deep learning systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3238147.3238202)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1803.07519) | ASE<br>2018 |
| 2017 | **DeepXplore** | DeepXplore: Automated Whitebox Testing of Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3132747.3132785)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1705.06640)<br>[![Code](assets/badges/code.svg)](https://github.com/peikexin9/deepxplore) | SOSP<br>2017 |

##### 量子神经网络（QNN）

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2025 | **QuanTest** | QuanTest: Entanglement-Guided Testing of Quantum Neural Network Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3688840)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2402.12950)<br>[![Code](assets/badges/code.svg)](https://github.com/am0x00/QuanTest) | TOSEM |

<a name="test-generation"></a>

#### 测试生成

##### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2026 | **SUNTest** | White-Box Test Input Generation for Enhancing Deep Neural Network Models through Suspicious Neuron Awareness | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3736305)<br>[![Code](assets/badges/code.svg)](https://github.com/TestingAIGroup/SUNTest) | TOSEM |
| 2025 | **Clover** | Context-Aware Fuzzing for Robustness Enhancement of Deep Learning Models | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3680464)<br>[![Code](assets/badges/code.svg)](https://github.com/PapRep/Clover) | TOSEM |
| 2025 | **DiffGAN** | DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2025.3611329) | TSE |
| 2025 | **IATT** | IATT: Interpretation Analysis-based Transferable Test Generation for Convolutional Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3705301)<br>[![Code](assets/badges/code.svg)](https://github.com/samxrl/IATT) | TOSEM |
| 2025 | **NSGen** | Neuron Semantic-Guided Test Generation for Deep Neural Networks Fuzzing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3688835)<br>[![Code](assets/badges/code.svg)](https://github.com/unknownhl/NSGen) | TOSEM |
| 2025 | **NLPLego** | NLPLego: Assembling Test Generation for Natural Language Processing Applications | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3691631)<br>[![Code](assets/badges/code.svg)](https://github.com/SSCT-Lab/NLPLego) | TOSEM |
| 2025 | — | Search-Based DNN Testing and Retraining With GAN-Enhanced Simulations | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2025.3540549)<br>[![Code](assets/badges/code.svg)](https://doi.org/10.5281/zenodo.14535408) | TSE |
| 2025 | **TAEFuzz** | TAEFuzz: Automatic Fuzzing for Image-based Deep Learning Systems via Transferable Adversarial Examples | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3714463)<br>[![Code](assets/badges/code.svg)](https://anonymous.4open.science/r/TAEFuzz-4575) | TOSEM |
| 2024 | **CIT4DNN** | CIT4DNN: Generating Diverse and Rare Inputs for Neural Networks Using Latent Space Combinatorial Testing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3597503.3639106)<br>[![Code](assets/badges/code.svg)](https://github.com/less-lab-uva/CIT4DNN) | ICSE<br>2024 |
| 2024 | **SINVAD** | Deceiving Humans and Machines Alike: Search-based Test Input Generation for DNNs Using Variational Autoencoders | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3635706)<br>[![Code](assets/badges/code.svg)](https://github.com/coinse/SINVAD) | TOSEM |
| 2024 | **DFuzzer** | DFuzzer: Diversity-Driven Seed Queue Construction of Fuzzing for Deep Learning Models | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tr.2023.3322406) | TR |
| 2024 | **FIPSER** | FIPSER: Improving Fairness Testing of DNN by Seed Prioritization | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3691620.3695486)<br>[![Code](assets/badges/code.svg)](https://github.com/light-chimes/FIPSER) | ASE<br>2024 |
| 2024 | **GIST** | GIST: Generated Inputs Sets Transferability in Deep Learning | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3672457)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2311.00801)<br>[![Code](assets/badges/code.svg)](https://github.com/FlowSs/GIST) | TOSEM |
| 2024 | — | Seed Selection for Testing Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3607190) | TOSEM |
| 2023 | **Test4Deep**<br>(journal-version) | A White-Box Testing for Deep Neural Networks Based on Neuron Coverage | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tnnls.2022.3156620) | TNNLS |
| 2023 | **ATOM** | ATOM: Automated Black-Box Testing of Multi-Label Image Classification Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/ase56229.2023.00156) | ASE<br>2023 |
| 2023 | **CoCoFuzzing** | CoCoFuzzing: Testing Neural Code Models With Coverage-Guided Fuzzing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tr.2022.3208239)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2106.09242)<br>[![Code](assets/badges/code.svg)](https://doi.org/10.5281/zenodo.4000441) | TR |
| 2023 | **DistXplore** | DistXplore: Distribution-Guided Testing for Evaluating and Enhancing Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3611643.3616266)<br>[![Code](assets/badges/code.svg)](https://github.com/l1lk/DistXplore) | ESEC/FSE<br>2023 |
| 2023 | **DeepSensor** | Excitement surfeited turns to errors: Deep learning testing framework based on excitable neurons | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1016/j.ins.2023.118936)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2202.07464)<br>[![Code](assets/badges/code.svg)](https://github.com/Allen-piexl/DeepSensor/) | Information Sciences |
| 2023 | **DFLARE / DREPAIR** | Finding Deviated Behaviors of the Compressed DNN Models for Image Classifications | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3583564)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2112.02819)<br>[![Code](assets/badges/code.svg)](https://github.com/yqtianust/DFlare) | TOSEM |
| 2023 | **QuoTe**<br>(journal-version) | QuoTe: Quality-oriented Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3582573)<br>[![Code](assets/badges/code.svg)](https://github.com/Testing4AI/QuoTe) | TOSEM |
| 2022 | **CAGFuzz** | CAGFuzz: Coverage-Guided Adversarial Generative Fuzzing Testing for Image-Based Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2021.3124006) | TSE |
| 2022 | **testRNN** | Coverage-Guided Testing for Recurrent Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tr.2021.3080664)<br>[![Code](assets/badges/code.svg)](https://github.com/TrustAI/testRNN) | TR |
| 2022 | **RNN-Test** | RNN-Test: Towards Adversarial Testing for Recurrent Neural Network Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2021.3114353) | TSE |
| 2022 | **TSDTest** | TSDTest: A Efficient Coverage Guided Two-Stage Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/qrs-c57518.2022.00033) | QRS-C<br>2022 |
| 2021 | **DLFuzz**<br>(journal-version) | Coverage Guided Differential Adversarial Testing of Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tnse.2020.2997359)<br>[![Code](assets/badges/code.svg)](https://github.com/turned2670/DLFuzz) | TNSE |
| 2021 | **DeepCon** | DeepCon: Contribution Coverage Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner50967.2021.00026) | SANER<br>2021 |
| 2021 | **RobOT**<br>(conf-version) | RobOT: Robustness-Oriented Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse43902.2021.00038)<br>[![Code](assets/badges/code.svg)](https://github.com/SmallkeyChen/RobOT) | ICSE<br>2021 |
| 2020 | **Sensei / Sensei-SA** | Fuzz testing based data augmentation to improve robustness of deep neural networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3377811.3380415) | ICSE<br>2020 |
| 2020 | **DeepJanus** | Model-based exploration of the frontier of behaviours for deep learning system testing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3368089.3409730)<br>[![Code](assets/badges/code.svg)](https://github.com/testingautomated-usi/DeepJanus) | ESEC/FSE<br>2020 |
| 2020 | — | Towards Characterizing Adversarial Defects of Deep Learning Software from the Lens of Uncertainty | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3377811.3380368)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2004.11573) | ICSE<br>2020 |
| 2019 | **DeepCT** | DeepCT: Tomographic Combinatorial Testing for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner.2019.8668044) | SANER<br>2019 |
| 2019 | **DeepFault** | DeepFault: Fault Localization for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/978-3-030-16722-6_10)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1902.05974) | FASE<br>2019 |
| 2019 | **DeepHunter** | DeepHunter: A Coverage-Guided Fuzz Testing Framework for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3293882.3330579)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1809.01266) | ISSTA<br>2019 |
| 2019 | **DeepStellar** | DeepStellar: model-based quantitative analysis of stateful deep learning systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3338906.3338954) | ESEC/FSE<br>2019 |
| 2019 | — | Structural Test Coverage Criteria for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3358233)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1803.04792)<br>[![Code](assets/badges/code.svg)](https://github.com/TrustAI/DeepConcolic) | TECS |
| 2019 | **Test4Deep**<br>(conf-version) | Test4Deep: an Effective White-Box Testing for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/cse/euc.2019.00013) | CSE/EUC<br>2019 |
| 2018 | **DeepRoad** | DeepRoad: GAN-Based Metamorphic Testing and Input Validation Framework for Autonomous Driving Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3238147.3238187) | ASE<br>2018 |
| 2018 | **DeepTest** | DeepTest: automated testing of deep-neural-network-driven autonomous cars | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3180155.3180220)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1708.08559) | ICSE<br>2018 |
| 2018 | **DLFuzz**<br>(conf-version) | DLFuzz: differential fuzzing testing of deep learning systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3236024.3264835)<br>[![Code](assets/badges/code.svg)](https://github.com/turned2670/DLFuzz) | ESEC/FSE<br>2018 |
| 2017 | **DeepXplore** | DeepXplore: Automated Whitebox Testing of Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3132747.3132785)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1705.06640)<br>[![Code](assets/badges/code.svg)](https://github.com/peikexin9/deepxplore) | SOSP<br>2017 |

##### 大语言模型（LLM）

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2025 | **NLPLego** | NLPLego: Assembling Test Generation for Natural Language Processing Applications | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3691631)<br>[![Code](assets/badges/code.svg)](https://github.com/SSCT-Lab/NLPLego) | TOSEM |
| 2024 | **LLM-Fuzzer** | LLM-Fuzzer: Scaling Assessment of Large Language Model Jailbreaks | [![Paper](assets/badges/paper.svg)](https://www.usenix.org/conference/usenixsecurity24/presentation/yu-jiahao)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2309.10253)<br>[![Code](assets/badges/code.svg)](https://github.com/hubertyoo/GPTFuzz) | USENIX Security<br>2024 |

##### 量子神经网络（QNN）

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2025 | **QuanTest** | QuanTest: Entanglement-Guided Testing of Quantum Neural Network Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3688840)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2402.12950)<br>[![Code](assets/badges/code.svg)](https://github.com/am0x00/QuanTest) | TOSEM |

<a name="test-selection-and-prioritization"></a>

#### 测试选择与排序

##### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2026 | **MetaDTS** | MetaDTS: Distribution difference-based adaptive test input selection for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1016/j.sysarc.2025.103682) | JSA |
| 2026 | **PriCod** | PriCod: Prioritizing Test Inputs for Compressed Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3730435)<br>[![Code](assets/badges/code.svg)](https://github.com/yinghuali/PriCod) | TOSEM |
| 2026 | **SETS** | SETS: A Simple yet Effective DNN Test Selection Approach | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3772084)<br>[![Code](assets/badges/code.svg)](https://github.com/GIST-NJU/SETS) | TOSEM |
| 2026 | **DuFP** | When Ambiguity Meets Atypicality: Dual-Perspective Test Input Prioritization for DNNs | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3832783.3834351)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2609.34703)<br>[![Code](assets/badges/code.svg)](https://github.com/Ryan-LHR/DuFP) | ASE<br>2026 |
| 2025 | — | Assessing the Robustness of Test Selection Methods for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3715693)<br>[![Code](assets/badges/code.svg)](https://anonymous.4open.science/r/Robust-testing-test-selection-3F83/) | TOSEM |
| 2025 | **AudioTest** | AudioTest: Prioritizing Audio Test Cases | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3728907)<br>[![Code](assets/badges/code.svg)](https://zenodo.org/records/13961855) | PACMSE |
| 2025 | **DeepFeature** | DeepFeature: Guiding adversarial testing for deep neural network systems using robust features | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1016/j.jss.2024.112201)<br>[![Code](assets/badges/code.svg)](https://github.com/Deepfea/DeepFeature) | JSS |
| 2025 | **DeepVec** | DeepVec: State-Vector Aware Test Case Selection for Enhancing Recurrent Neural Network | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2025.3565037)<br>[![Code](assets/badges/code.svg)](https://github.com/ZhonghaoJiang/DeepVec) | TSE |
| 2025 | **EATS** | Efficient adaptive test case selection for DNNs robustness enhancement | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1016/j.jss.2025.112451) | JSS |
| 2025 | **LBT** | Learning-Based Testing for Deep Learning: Enhancing Model Robustness with Adversarial Input Prioritization | [![Paper](assets/badges/paper.svg)](https://arxiv.org/abs/2509.23961) | arXiv（预印本） |
| 2025 | **MetaSel** | MetaSel: A Test Selection Approach for Fine-Tuned DNN Models | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2025.3612253)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2503.17534) | TSE |
| 2025 | **Prophet** | Prioritizing Speech Test Cases | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3707450)<br>[![Code](assets/badges/code.svg)](https://github.com/yangzhou6666/ASRProphet) | TOSEM |
| 2024 | — | Can Coverage Criteria Guide Failure Discovery for Image Classifiers? An Empirical Study | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3672446) | TOSEM |
| 2024 | **DeepGD** | DeepGD: A Multi-Objective Black-Box Test Selection Approach for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3644388)<br>[![Code](assets/badges/code.svg)](https://github.com/ZOE-CA/DeepGD) | TOSEM |
| 2024 | **DeepSample** | DeepSample: DNN sampling-based testing for operational accuracy assessment | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3597503.3639584)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2403.19271) | ICSE<br>2024 |
| 2024 | **DATIS** | Distance-Aware Test Input Selection for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3650212.3652125)<br>[![Code](assets/badges/code.svg)](https://github.com/DATIS-24/DATIS) | ISSTA<br>2024 |
| 2024 | **FAST** | FAST: Boosting Uncertainty-based Test Prioritization Methods for Neural Networks via Feature Selection | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3691620.3695472)<br>[![Code](assets/badges/code.svg)](https://github.com/Testing4AI/FAST) | ASE<br>2024 |
| 2024 | **FATS** | FATS: Feature Distribution Analysis-Based Test Selection for Deep Learning Enhancement | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tbdata.2023.3334648)<br>[![Code](assets/badges/code.svg)](https://github.com/smile-ya/FATS) | TBD |
| 2024 | **GraphPrior** | GraphPrior: Mutation-based Test Input Prioritization for Graph Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3607191)<br>[![Code](assets/badges/code.svg)](https://github.com/yinghuali/GraphPrior) | TOSEM |
| 2024 | **NSS** | Neuron Sensitivity-Guided Test Case Selection | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3672454) | TOSEM |
| 2024 | **VRank** | Prioritizing test cases for deep learning-based video classifiers | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/s10664-024-10520-1)<br>[![Code](assets/badges/code.svg)](https://github.com/yinghuali/VRank) | EMSE |
| 2024 | **TDPR** | Prioritizing Test Inputs for DNNs Using Training Dynamics | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3691620.3695498)<br>[![Code](assets/badges/code.svg)](https://github.com/TDPR-24/TDPR) | ASE<br>2024 |
| 2024 | **PCPrior** | Test Input Prioritization for 3D Point Clouds | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3643676)<br>[![Code](assets/badges/code.svg)](https://github.com/yinghuali/PCPrior) | TOSEM |
| 2024 | **NodeRank** | Test Input Prioritization for Graph Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2024.3385538)<br>[![Code](assets/badges/code.svg)](https://github.com/yinghuali/NodeRank) | TSE |
| 2024 | **MLPrior** | Test Input Prioritization for Machine Learning Classifiers | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2024.3350019)<br>[![Code](assets/badges/code.svg)](https://github.com/yinghuali/MLPrior) | TSE |
| 2024 | — | Test Selection for Deep Neural Networks using Meta-Models with Uncertainty Metrics | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3650212.3680312)<br>[![Code](assets/badges/code.svg)](https://github.com/DNNTestingMeta/MetaModelTesting) | ISSTA<br>2024 |
| 2024 | — | Towards Exploring the Limitations of Test Selection Techniques on Graph Neural Networks: An Empirical Study | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/s10664-024-10515-y)<br>[![Code](assets/badges/code.svg)](https://github.com/BlueBerry-xueqi/graph_testing) | EMSE |
| 2023 | **CertPri** | CertPri: Certifiable Prioritization for Deep Neural Networks via Movement Cost in Feature Space | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/ase56229.2023.00126)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2307.09375)<br>[![Code](assets/badges/code.svg)](https://github.com/haibinzheng/CertPri) | ASE<br>2023 |
| 2023 | **SA**<br>(journal-version) | Evaluating Surprise Adequacy for Deep Learning System Testing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3546947)<br>[![Code](assets/badges/code.svg)](https://github.com/coinse/sadl) | TOSEM |
| 2023 | **NNS** | In Defense of Simple Techniques for Neural Network Test Case Selection | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3597926.3598073) | ISSTA<br>2023 |
| 2023 | **RTS** | Robust Test Selection for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2023.3330982)<br>[![Code](assets/badges/code.svg)](https://github.com/swf1996120/RTS) | TSE |
| 2022 | **ATS** | Adaptive test selection for deep neural networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3510003.3510232)<br>[![Code](assets/badges/code.svg)](https://github.com/SATE-Lab/ATS) | ICSE<br>2022 |
| 2022 | **DAT** | An Empirical Study on Data Distribution-Aware Test Selection for Deep Learning Enhancement | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3511598)<br>[![Code](assets/badges/code.svg)](https://github.com/code4papers/DAT) | TOSEM |
| 2022 | **DeepState** | DeepState: Selecting Test Suites to Enhance the Robustness of Recurrent Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3510003.3510231)<br>[![Code](assets/badges/code.svg)](https://github.com/SATE-Lab/DeepState) | ICSE<br>2022 |
| 2022 | — | Simple techniques work surprisingly well for neural network test prioritization and active learning (replicability study) | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3533767.3534375)<br>[![Code](assets/badges/code.svg)](https://github.com/testingautomated-usi/simple-tip) | ISSTA<br>2022 |
| 2021 | **PRIMA** | Prioritizing Test Inputs for Deep Neural Networks via Mutation Analysis | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse43902.2021.00046)<br>[![Code](assets/badges/code.svg)](https://github.com/sail-repos/PRIMA) | ICSE<br>2021 |
| 2021 | — | Test Selection for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3417330)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1904.13195)<br>[![Code](assets/badges/code.svg)](https://github.com/TestSelection/TestSelection) | TOSEM |
| 2021 | **TestRank** | TestRank: Bringing Order into Unlabeled Test Instances for Deep Learning Tasks | [![Paper](assets/badges/paper.svg)](https://proceedings.neurips.cc/paper/2021/hash/ae78510109d46b0a6eef9820a4ca95d6-Abstract.html)<br>[![Code](assets/badges/code.svg)](https://github.com/cure-lab/TestRank) | NeurIPS<br>2021 |
| 2020 | **DeepGini** | DeepGini: prioritizing massive tests to enhance the robustness of deep neural networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3395363.3397357)<br>[![Code](assets/badges/code.svg)](https://github.com/deepgini/deepgini) | ISSTA<br>2020 |
| 2020 | **MCP** | Multiple-boundary clustering and prioritization to promote neural network retraining | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3324884.3416621)<br>[![Code](assets/badges/code.svg)](https://github.com/actionabletest/MCP) | ASE<br>2020 |
| 2019 | **SA**<br>(conf-version) | Guiding Deep Learning System Testing Using Surprise Adequacy | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse.2019.00108)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1808.08444) | ICSE<br>2019 |
| 2019 | — | Input Prioritization for Testing Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/aitest.2019.000-6)<br>[![Code](assets/badges/code.svg)](http://www.github.com/bntejn/keras-prioritizer) | AITest<br>2019 |

##### 大语言模型（LLM）

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2026 | **AcTracer** | AcTracer: Active Testing of Large Language Model via Multi-Stage Sampling | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3744340)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2408.03573)<br>[![Code](assets/badges/code.svg)](https://github.com/YuhengHuang42/test_selection_llm) | TOSEM |

<a name="model-repair"></a>

#### 模型修复

##### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2026 | **SMiR** | SMiR: Minimizing Side Effects in Repairing Specific Misclassifications for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3771545)<br>[![Code](assets/badges/code.svg)](https://github.com/AnonymousSE4AI/SMiR) | TOSEM |
| 2025 | **AutoRIC** | AutoRIC: Automated Neural Network Repairing Based on Constrained Optimization | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3690634)<br>[![Code](assets/badges/code.svg)](https://github.com/Anonymous89000/AutoRIC) | TOSEM |
| 2025 | **DEFault** | Improved Detection and Diagnosis of Faults in Deep Neural Networks Using Hierarchical and Explainable Classification | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse55347.2025.00224)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2501.12560)<br>[![Code](assets/badges/code.svg)](https://github.com/SigmaJahan/DEFault-DNN-Debugging)<br>[![Website](assets/badges/website.svg)](https://default-ai.com/) | ICSE<br>2025 |
| 2025 | **FeaProtect** | Mitigating Regression Faults Induced by Feature Evolution in Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3712199)<br>[![Code](assets/badges/code.svg)](https://github.com/youhanmo/FeaProtect) | TOSEM |
| 2025 | **PatchPro** | Patch Synthesis for Property Repair of Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse55347.2025.00181)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2404.01642) | ICSE<br>2025 |
| 2025 | **Repairs and Breaks Prediction**<br>(journal-version) | Repairs and Breaks Prediction for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3702983)<br>[![Code](assets/badges/code.svg)](https://github.com/posl/DNN-repair-break-prediction) | TOSEM |
| 2024 | **Dare**<br>(journal-version) | A Post-training Framework for Improving the Performance of Deep Learning Models via Model Transformation | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3630011)<br>[![Code](assets/badges/code.svg)](https://doi.org/10.5281/zenodo.10009069) | TOSEM |
| 2024 | **CrossCert** | CrossCert: A Cross-Checking Detection Approach to Patch Robustness Certification for Deep Learning Models | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3660827)<br>[![Code](assets/badges/code.svg)](https://github.com/kio-cs/CrossCert) | PACMSE |
| 2024 | **Faire** | Faire: Repairing Fairness of Neural Networks via Neuron Condition Synthesis | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3617168) | TOSEM |
| 2024 | **INNER** | Interpretability Based Neural Network Repair | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3650212.3680330)<br>[![Code](assets/badges/code.svg)](https://github.com/implicitDeclaration/inner) | ISSTA<br>2024 |
| 2024 | **IDNN** | Isolation-Based Debugging for Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3650212.3652132)<br>[![Code](assets/badges/code.svg)](https://github.com/Testing4AI/IDNN) | ISSTA<br>2024 |
| 2024 | **MetaRepair** | MetaRepair: Learning to Repair Deep Neural Networks from Repairing Experiences | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3664647.3680638) | ACM MM<br>2024 |
| 2024 | **NeuFair** | NeuFair: Neural Network Fairness Repair with Dropout | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3650212.3680380)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2407.04268)<br>[![Code](assets/badges/code.svg)](https://github.com/vdasu/neufair) | ISSTA<br>2024 |
| 2024 | **RUNNER** | RUNNER: Responsible UNfair NEuron Repair for Enhancing Deep Neural Network Fairness | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3597503.3623334)<br>[![Code](assets/badges/code.svg)](https://github.com/Ace0001/RUNNER) | ICSE<br>2024 |
| 2024 | **VeRe** | VeRe: Verification Guided Synthesis for Repairing Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3597503.3623332)<br>[![Code](assets/badges/code.svg)](https://github.com/nninjn/VeRe) | ICSE<br>2024 |
| 2023 | **AdRep** | Adaptive Search-based Repair of Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3583131.3590477)<br>[![Code](assets/badges/code.svg)](https://github.com/jst-qaml/adaptiveRepair) | GECCO<br>2023 |
| 2023 | **AIREPAIR** | AIREPAIR: A Repair Platform for Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse-companion58688.2023.00033)<br>[![Code](assets/badges/code.svg)](https://github.com/theyoucheng/AIRepair) | ICSE-Companion<br>2023 |
| 2023 | **NeuRecoverLite** | An Experience Report on Regression-Free Repair of Deep Neural Network Model | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner56733.2023.00090) | SANER (Industry)<br>2023 |
| 2023 | **Repair and Side-effect Prediction**<br>(conf-version) | An Initial Analysis of Repair and Side-effect Prediction for Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/cain58948.2023.00017) | CAIN<br>2023 |
| 2023 | **Arachne** | Arachne: Search-Based Repair of Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3563210)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1912.12463)<br>[![Code](assets/badges/code.svg)](https://github.com/coinse/arachne) | TOSEM |
| 2023 | **APRNN** | Architecture-Preserving Provable Repair of Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3591238)<br>[![Code](assets/badges/code.svg)](https://github.com/95616ARG/APRNN) | PACMPL |
| 2023 | **ArchRepair** | ArchRepair: Block-Level Architecture-Oriented Repairing for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3585005) | TOSEM |
| 2023 | **DeepPatch** | DeepPatch: Maintaining Deep Learning Model Programs to Retain Standard Accuracy with Substantial Robustness Improvement | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3604609)<br>[![Code](assets/badges/code.svg)](https://github.com/Wsine/deeppatch) | TOSEM |
| 2023 | **DISTRREP** | Distributed Repair of Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icst57152.2023.00017) | ICST<br>2023 |
| 2023 | **DFLARE / DREPAIR** | Finding Deviated Behaviors of the Compressed DNN Models for Image Classifications | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3583564)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2112.02819)<br>[![Code](assets/badges/code.svg)](https://github.com/yqtianust/DFlare) | TOSEM |
| 2023 | **RiFT** | Improving Generalization of Adversarial Training via Robust Critical Fine-Tuning | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/iccv51070.2023.00408)<br>[![Code](assets/badges/code.svg)](https://github.com/Immortalise/RiFT) | ICCV<br>2023 |
| 2023 | — | Lightweight Approaches to DNN Regression Error Reduction: An Uncertainty Alignment Perspective | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse48619.2023.00106)<br>[![Code](assets/badges/code.svg)](https://github.com/Lizn-zn/Uncertainty-Alignment) | ICSE<br>2023 |
| 2022 | **CARE** | Causality-based neural network repair | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3510003.3510080) | ICSE<br>2022 |
| 2022 | — | Neural Network Repair with Reachability Analysis | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/978-3-031-15839-1_13)<br>[![Code](assets/badges/code.svg)](https://github.com/Shaddadi/veritex) | FORMATS<br>2022 |
| 2022 | **NeuRecover** | NeuRecover: Regression-Controlled Repair of Deep Neural Networks with Training History | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner53432.2022.00128) | SANER<br>2022 |
| 2022 | **I-repair** | Repairing misclassifications in neural networks using limited data | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3477314.3507059) | SAC<br>2022 |
| 2022 | **Dare**<br>(conf-version) | Toward Improving the Robustness of Deep Learning Models via Model Transformation | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3551349.3556920)<br>[![Code](assets/badges/code.svg)](https://doi.org/10.5281/zenodo.7018397) | ASE<br>2022 |
| 2021 | **AI-Lancet** | AI-Lancet: Locating Error-inducing Neurons to Optimize Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3460120.3484818) | CCS<br>2021 |
| 2021 | **AUTOTRAINER** | AUTOTRAINER: An Automatic DNN Training Problem Detection and Repair System | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse43902.2021.00043)<br>[![Code](assets/badges/code.svg)](https://github.com/shiningrain/AUTOTRAINER) | ICSE<br>2021 |
| 2021 | **PRDNN** | Provable repair of deep neural networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3453483.3454064)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2104.04413)<br>[![Code](assets/badges/code.svg)](https://github.com/95616ARG/PRDNN) | PLDI<br>2021 |
| 2020 | **FSGMix** | Few-Shot Guided Mix for DNN Repairing | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icsme46990.2020.00079) | ICSME-NIER<br>2020 |
| 2019 | **Apricot** | Apricot: A Weight-Adaptation Approach to Fixing Deep Learning Models | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/ase.2019.00043) | ASE<br>2019 |
| 2019 | **DeepCorrect** | DeepCorrect: Correcting DNN Models Against Image Distortions | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tip.2019.2924172)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1705.02406)<br>[![Code](assets/badges/code.svg)](https://github.com/tsborkar/DeepCorrect) | TIP |
| 2018 | **MODE** | MODE: automated neural network model debugging via state differential analysis and input selection | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3236024.3236082)<br>[![Code](assets/badges/code.svg)](https://github.com/dnnmode/buggymodels) | ESEC/FSE<br>2018 |

##### 大语言模型（LLM）

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2022 | **ROME** | Locating and Editing Factual Associations in GPT | [![Paper](assets/badges/paper.svg)](https://proceedings.neurips.cc/paper_files/paper/2022/hash/6f1d43d5a82a37e89b0665b33bf3a182-Abstract-Conference.html)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2202.05262)<br>[![Code](assets/badges/code.svg)](https://github.com/kmeng01/rome) | NeurIPS<br>2022 |

<a name="dnn-verification"></a>

#### DNN 验证

##### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2022 | **DeepPAC** | Towards Practical Robustness Analysis for DNNs based on PAC-Model Learning | [![Paper](assets/badges/paper.svg)](https://conf.researchr.org/details/icse-2022/icse-2022-papers/106/Towards-Practical-Robustness-Analysis-for-DNNs-based-on-PAC-Model-Learning)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2101.10102) | ICSE<br>2022 |
| 2019 | — | Robustness Verification of Classification Deep Neural Networks via Linear Programming | [![Paper](assets/badges/paper.svg)](https://openaccess.thecvf.com/content_CVPR_2019/html/Lin_Robustness_Verification_of_Classification_Deep_Neural_Networks_via_Linear_Programming_CVPR_2019_paper.html) | CVPR<br>2019 |
| 2017 | **Reluplex** | Reluplex: An Efficient SMT Solver for Verifying Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://link.springer.com/chapter/10.1007/978-3-319-63387-9_5)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1702.01135) | CAV<br>2017 |

<a name="other"></a>

#### 其他

##### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2018 | **DeepMutation** | DeepMutation: Mutation Testing of Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/issre.2018.00021)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1805.05206) | ISSRE<br>2018 |

<a name="surveys"></a>

### 综述

#### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2024 | — | Test Optimization in DNN Testing: A Survey | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3643678) | TOSEM |
| 2024 | — | 深度神经网络修复策略综述 | [![Paper](assets/badges/paper.svg)](https://www.jos.org.cn/1000-9825/7061.htm) | 软件学报 |
| 2022 | — | Machine Learning Testing: Survey, Landscapes and Horizons | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/tse.2019.2962027)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1906.10742) | TSE |
| 2021 | — | 神经网络验证和测试技术研究综述 | [![Paper](assets/badges/paper.svg)](https://doi.org/10.3778/j.issn.1002-8331.2106-0342) | 计算机工程与应用 |
| 2020 | — | 深度神经网络测试研究综述 | [![Paper](assets/badges/paper.svg)](https://doi.org/10.13328/j.cnki.jos.005951) | 软件学报 |

<a name="empirical-studies"></a>

### 实证研究

#### 非 LLM 深度神经网络

| 年份 | 简称 | 论文标题 | 资源<br>Resources | 会议／期刊 |
| --- | --- | --- | --- | --- |
| 2025 | — | Assessing the Robustness of Test Selection Methods for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3715693)<br>[![Code](assets/badges/code.svg)](https://anonymous.4open.science/r/Robust-testing-test-selection-3F83/) | TOSEM |
| 2024 | — | Can Coverage Criteria Guide Failure Discovery for Image Classifiers? An Empirical Study | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3672446) | TOSEM |
| 2024 | — | Seed Selection for Testing Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3607190) | TOSEM |
| 2024 | — | Towards Exploring the Limitations of Test Selection Techniques on Graph Neural Networks: An Empirical Study | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1007/s10664-024-10515-y)<br>[![Code](assets/badges/code.svg)](https://github.com/BlueBerry-xueqi/graph_testing) | EMSE |
| 2023 | **NeuRecoverLite** | An Experience Report on Regression-Free Repair of Deep Neural Network Model | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/saner56733.2023.00090) | SANER (Industry)<br>2023 |
| 2022 | **DAT** | An Empirical Study on Data Distribution-Aware Test Selection for Deep Learning Enhancement | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3511598)<br>[![Code](assets/badges/code.svg)](https://github.com/code4papers/DAT) | TOSEM |
| 2022 | — | Is Neuron Coverage Needed to Make Person Detection More Robust? | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/cvprw56347.2022.00326) | CVPRW<br>2022 |
| 2022 | — | Simple techniques work surprisingly well for neural network test prioritization and active learning (replicability study) | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3533767.3534375)<br>[![Code](assets/badges/code.svg)](https://github.com/testingautomated-usi/simple-tip) | ISSTA<br>2022 |
| 2021 | — | A Review and Refinement of Surprise Adequacy | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/deeptest52559.2021.00009)<br>[![Code](assets/badges/code.svg)](https://github.com/testingautomated-usi/surprise-adequacy) | DeepTest (workshop)<br>2021 |
| 2021 | — | Are Coverage Criteria Meaningful Metrics for DNNs? | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/ijcnn52387.2021.9533987) | IJCNN<br>2021 |
| 2021 | — | Test Selection for Deep Learning Systems | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3417330)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1904.13195)<br>[![Code](assets/badges/code.svg)](https://github.com/TestSelection/TestSelection) | TOSEM |
| 2020 | — | An Empirical Study on Correlation between Coverage and Robustness for Deep Neural Networks | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/iceccs51672.2020.00016)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/1911.05904) | ICECCS<br>2020 |
| 2020 | — | Correlations between Deep Neural Network Model Coverage Criteria and Model Quality | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3368089.3409671)<br>[![Code](assets/badges/code.svg)](https://github.com/RU-System-Software-and-Security/CovTesting) | ESEC/FSE<br>2020 |
| 2020 | — | Is neuron coverage a meaningful measure for testing deep neural networks? | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3368089.3409754)<br>[![Code](assets/badges/code.svg)](https://doi.org/10.5281/zenodo.4021473) | ESEC/FSE<br>2020 |
| 2020 | — | Towards Characterizing Adversarial Defects of Deep Learning Software from the Lens of Uncertainty | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1145/3377811.3380368)<br>[![arXiv](assets/badges/arxiv.svg)](https://arxiv.org/abs/2004.11573) | ICSE<br>2020 |
| 2019 | — | Structural Coverage Criteria for Neural Networks Could Be Misleading | [![Paper](assets/badges/paper.svg)](https://doi.org/10.1109/icse-nier.2019.00031) | ICSE-NIER<br>2019 |

<!-- END GENERATED PAPERS -->

<a name="star-history"></a>

## 🌟 Star 历史

<p align="center">
  <a href="https://www.star-history.com/?repos=Ryan-LHR%2Fawesome-dnn-testing-and-repair&amp;type=date&amp;legend=top-left">
    <img src="https://api.star-history.com/chart?repos=Ryan-LHR/awesome-dnn-testing-and-repair&amp;type=date&amp;legend=top-left" alt="Star 历史图" width="700" />
  </a>
</p>

<a name="license"></a>

## ⚖️ 许可证

本项目的原创内容与代码采用 [MIT 许可证](LICENSE)。第三方论文、摘要及其他材料保留各自原有的权利与许可。

<a name="tips"></a>

## 💡 阅读提示

- [英文版](README.md#papers)只展示英文论文；简体中文版同时展示中英文论文。
- 两版顶部的 **Papers** 和 **With code** 徽章都统计全库；分类计数按各版本实际展示的论文计算。

<a name="contributing"></a>

## 🙌 欢迎贡献

欢迎贡献！你可以[推荐论文](https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/issues/new?template=01-recommend-paper.yml)、[提交纠错](https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/issues/new?template=02-correct-entry.yml)，或提交 [Pull Request](https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/pulls)。推荐论文只需提供标题和论文链接，建议分类、其他链接和补充说明均为选填。直接修改数据时，请参考[数据填写说明与 DeepXplore 示例](data/README.md#简体中文)。

感谢每一位为本合集作出贡献的朋友！

<a href="https://github.com/Ryan-LHR/awesome-dnn-testing-and-repair/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ryan-LHR/awesome-dnn-testing-and-repair" alt="Awesome DNN Testing and Repair 的贡献者" />
</a>
