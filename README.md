# Awesome DNN Testing and Repair

A collection of papers on deep neural network testing and repair.

## Overview

This collection focuses on testing and repairing deep neural network models, with publication details and links to papers, preprints, and code where available.

- [Research Papers](#research-papers)
  - [Coverage Metrics](#coverage-metrics)
  - [Test Generation](#test-generation)
  - [Test Selection and Prioritization](#test-selection-and-prioritization)
  - [Model Repair](#model-repair)
  - [Other](#other)
- [Surveys](#surveys)
- [Empirical Studies](#empirical-studies)

## Papers

Within each category, published papers are listed by formal publication year, newest first. Preprints use their first public year and are marked accordingly. Preprint and online publication dates are recorded separately in the [paper data](data/papers.json).

Resource links are shown only when recorded in the paper data.

CCF venue categories in the paper data refer to the 2026 directory. A `null` value means no verified category is recorded.

### Research Papers

#### Coverage Metrics

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2025 | **QuanTest** | [QuanTest: Entanglement-Guided Testing of Quantum Neural Network Systems](https://doi.org/10.1145/3688840) | [arXiv](https://arxiv.org/abs/2402.12950) | TOSEM |
| 2024 | — | [Can Coverage Criteria Guide Failure Discovery for Image Classifiers? An Empirical Study](https://doi.org/10.1145/3672446) | — | TOSEM |
| 2023 | **ATOM** | [ATOM: Automated Black-Box Testing of Multi-Label Image Classification Systems](https://doi.org/10.1109/ase56229.2023.00156) | — | ASE' 2023 |
| 2023 | **SA (journal-version)** | [Evaluating Surprise Adequacy for Deep Learning System Testing](https://doi.org/10.1145/3546947) | [Code](https://github.com/coinse/sadl) | TOSEM |
| 2023 | **IDC** | [Input Distribution Coverage: Measuring Feature Interaction Adequacy in Neural Network Testing](https://doi.org/10.1145/3576040) | — | TOSEM |
| 2022 | **testRNN** | [Coverage-Guided Testing for Recurrent Neural Networks](https://doi.org/10.1109/tr.2021.3080664) | — | TR |
| 2022 | — | [Is Neuron Coverage Needed to Make Person Detection More Robust?](https://doi.org/10.1109/cvprw56347.2022.00326) | — | CVPRW' 2022 |
| 2022 | **NPC** | [NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks](https://doi.org/10.1145/3490489) | [arXiv](https://arxiv.org/abs/2203.12915) · [Code](https://github.com/ltl7155/NPC) | TOSEM |
| 2022 | **RNN-Test** | [RNN-Test: Towards Adversarial Testing for Recurrent Neural Network Systems](https://doi.org/10.1109/tse.2021.3114353) | — | TSE |
| 2021 | — | [A Review and Refinement of Surprise Adequacy](https://doi.org/10.1109/deeptest52559.2021.00009) | — | DeepTest (workshop)' 2021 |
| 2021 | — | [Are Coverage Criteria Meaningful Metrics for DNNs?](https://doi.org/10.1109/ijcnn52387.2021.9533987) | — | IJCNN' 2021 |
| 2021 | **DeepCon** | [DeepCon: Contribution Coverage Testing for Deep Learning Systems](https://doi.org/10.1109/saner50967.2021.00026) | — | SANER' 2021 |
| 2020 | — | [An Empirical Study on Correlation between Coverage and Robustness for Deep Neural Networks](https://doi.org/10.1109/iceccs51672.2020.00016) | [arXiv](https://arxiv.org/abs/1911.05904) | ICECCS' 2020 |
| 2020 | — | [Correlations between Deep Neural Network Model Coverage Criteria and Model Quality](https://doi.org/10.1145/3368089.3409671) | — | ESEC/FSE' 2020 |
| 2020 | — | [Is neuron coverage a meaningful measure for testing deep neural networks?](https://doi.org/10.1145/3368089.3409754) | — | ESEC/FSE' 2020 |
| 2019 | **DeepCT** | [DeepCT: Tomographic Combinatorial Testing for Deep Learning Systems](https://doi.org/10.1109/saner.2019.8668044) | — | SANER' 2019 |
| 2019 | **DeepPath** | [DeepPath: Path-Driven Testing Criteria for Deep Neural Networks](https://doi.org/10.1109/aitest.2019.00013) | — | AITest' 2019 |
| 2019 | **DeepStellar** | [DeepStellar: model-based quantitative analysis of stateful deep learning systems](https://doi.org/10.1145/3338906.3338954) | — | ESEC/FSE' 2019 |
| 2019 | **SA (conf-version)** | [Guiding Deep Learning System Testing Using Surprise Adequacy](https://doi.org/10.1109/icse.2019.00108) | [arXiv](https://arxiv.org/abs/1808.08444) | ICSE' 2019 |
| 2019 | — | [Structural Coverage Criteria for Neural Networks Could Be Misleading](https://doi.org/10.1109/icse-nier.2019.00031) | — | ICSE-NIER' 2019 |
| 2019 | — | [Structural Test Coverage Criteria for Deep Neural Networks](https://doi.org/10.1145/3358233) | [arXiv](https://arxiv.org/abs/1803.04792) | TECS |
| 2019 | — | [Towards Improved Testing For Deep Learning](https://doi.org/10.1109/icse-nier.2019.00030) | [arXiv](https://arxiv.org/abs/1902.06320) | ICSE-NIER' 2019 |
| 2018 | **DeepGauge** | [DeepGauge: multi-granularity testing criteria for deep learning systems](https://doi.org/10.1145/3238147.3238202) | [arXiv](https://arxiv.org/abs/1803.07519) | ASE' 2018 |
| 2017 | **DeepXplore** | [DeepXplore: Automated Whitebox Testing of Deep Learning Systems](https://doi.org/10.1145/3132747.3132785) | [arXiv](https://arxiv.org/abs/1705.06640) · [Code](https://github.com/peikexin9/deepxplore) | SOSP' 2017 |

#### Test Generation

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2026 | **SUNTest** | [White-Box Test Input Generation for Enhancing Deep Neural Network Models through Suspicious Neuron Awareness](https://doi.org/10.1145/3736305) | — | TOSEM |
| 2025 | **Clover** | [Context-Aware Fuzzing for Robustness Enhancement of Deep Learning Models](https://doi.org/10.1145/3680464) | — | TOSEM |
| 2025 | **DiffGAN** | [DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis](https://doi.org/10.1109/tse.2025.3611329) | — | TSE |
| 2025 | **IATT** | [IATT: Interpretation Analysis-based Transferable Test Generation for Convolutional Neural Networks](https://doi.org/10.1145/3705301) | — | TOSEM |
| 2025 | **NSGen** | [Neuron Semantic-Guided Test Generation for Deep Neural Networks Fuzzing](https://doi.org/10.1145/3688835) | — | TOSEM |
| 2025 | **NLPLego** | [NLPLego: Assembling Test Generation for Natural Language Processing Applications](https://doi.org/10.1145/3691631) | — | TOSEM |
| 2025 | **QuanTest** | [QuanTest: Entanglement-Guided Testing of Quantum Neural Network Systems](https://doi.org/10.1145/3688840) | [arXiv](https://arxiv.org/abs/2402.12950) | TOSEM |
| 2025 | — | [Search-Based DNN Testing and Retraining With GAN-Enhanced Simulations](https://doi.org/10.1109/tse.2025.3540549) | — | TSE |
| 2025 | **TAEFuzz** | [TAEFuzz: Automatic Fuzzing for Image-based Deep Learning Systems via Transferable Adversarial Examples](https://doi.org/10.1145/3714463) | — | TOSEM |
| 2024 | **CIT4DNN** | [CIT4DNN: Generating Diverse and Rare Inputs for Neural Networks Using Latent Space Combinatorial Testing](https://doi.org/10.1145/3597503.3639106) | — | ICSE' 2024 |
| 2024 | **SINVAD** | [Deceiving Humans and Machines Alike: Search-based Test Input Generation for DNNs Using Variational Autoencoders](https://doi.org/10.1145/3635706) | — | TOSEM |
| 2024 | **DFuzzer** | [DFuzzer: Diversity-Driven Seed Queue Construction of Fuzzing for Deep Learning Models](https://doi.org/10.1109/tr.2023.3322406) | — | TR |
| 2024 | **FIPSER** | [FIPSER: Improving Fairness Testing of DNN by Seed Prioritization](https://doi.org/10.1145/3691620.3695486) | [Code](https://github.com/light-chimes/FIPSER) | ASE' 2024 |
| 2024 | **GIST** | [GIST: Generated Inputs Sets Transferability in Deep Learning](https://doi.org/10.1145/3672457) | [arXiv](https://arxiv.org/abs/2311.00801) | TOSEM |
| 2024 | — | [Seed Selection for Testing Deep Neural Networks](https://doi.org/10.1145/3607190) | — | TOSEM |
| 2023 | **Test4Deep (journal-version)** | [A White-Box Testing for Deep Neural Networks Based on Neuron Coverage](https://doi.org/10.1109/tnnls.2022.3156620) | — | TNNLS |
| 2023 | **ATOM** | [ATOM: Automated Black-Box Testing of Multi-Label Image Classification Systems](https://doi.org/10.1109/ase56229.2023.00156) | — | ASE' 2023 |
| 2023 | **CoCoFuzzing** | [CoCoFuzzing: Testing Neural Code Models With Coverage-Guided Fuzzing](https://doi.org/10.1109/tr.2022.3208239) | [arXiv](https://arxiv.org/abs/2106.09242) | TR |
| 2023 | **DistXplore** | [DistXplore: Distribution-Guided Testing for Evaluating and Enhancing Deep Learning Systems](https://doi.org/10.1145/3611643.3616266) | — | ESEC/FSE' 2023 |
| 2023 | **DeepSensor** | [Excitement surfeited turns to errors: Deep learning testing framework based on excitable neurons](https://doi.org/10.1016/j.ins.2023.118936) | [arXiv](https://arxiv.org/abs/2202.07464) | Information Sciences |
| 2023 | **QuoTe (journal-version)** | [QuoTe: Quality-oriented Testing for Deep Learning Systems](https://doi.org/10.1145/3582573) | — | TOSEM |
| 2022 | **CAGFuzz** | [CAGFuzz: Coverage-Guided Adversarial Generative Fuzzing Testing for Image-Based Deep Learning Systems](https://doi.org/10.1109/tse.2021.3124006) | — | TSE |
| 2022 | **testRNN** | [Coverage-Guided Testing for Recurrent Neural Networks](https://doi.org/10.1109/tr.2021.3080664) | — | TR |
| 2022 | **RNN-Test** | [RNN-Test: Towards Adversarial Testing for Recurrent Neural Network Systems](https://doi.org/10.1109/tse.2021.3114353) | — | TSE |
| 2021 | **DLFuzz (journal-version)** | [Coverage Guided Differential Adversarial Testing of Deep Learning Systems](https://doi.org/10.1109/tnse.2020.2997359) | — | TNSE |
| 2021 | **DeepCon** | [DeepCon: Contribution Coverage Testing for Deep Learning Systems](https://doi.org/10.1109/saner50967.2021.00026) | — | SANER' 2021 |
| 2021 | **RobOT (conf-version)** | [RobOT: Robustness-Oriented Testing for Deep Learning Systems](https://doi.org/10.1109/icse43902.2021.00038) | — | ICSE' 2021 |
| 2020 | **DeepJanus** | [Model-based exploration of the frontier of behaviours for deep learning system testing](https://doi.org/10.1145/3368089.3409730) | — | ESEC/FSE' 2020 |
| 2020 | — | [Towards Characterizing Adversarial Defects of Deep Learning Software from the Lens of Uncertainty](https://doi.org/10.1145/3377811.3380368) | [arXiv](https://arxiv.org/abs/2004.11573) | ICSE' 2020 |
| 2019 | **DeepCT** | [DeepCT: Tomographic Combinatorial Testing for Deep Learning Systems](https://doi.org/10.1109/saner.2019.8668044) | — | SANER' 2019 |
| 2019 | **DeepHunter** | [DeepHunter: A Coverage-Guided Fuzz Testing Framework for Deep Neural Networks](https://doi.org/10.1145/3293882.3330579) | [arXiv](https://arxiv.org/abs/1809.01266) | ISSTA' 2019 |
| 2019 | **DeepStellar** | [DeepStellar: model-based quantitative analysis of stateful deep learning systems](https://doi.org/10.1145/3338906.3338954) | — | ESEC/FSE' 2019 |
| 2019 | — | [Structural Test Coverage Criteria for Deep Neural Networks](https://doi.org/10.1145/3358233) | [arXiv](https://arxiv.org/abs/1803.04792) | TECS |
| 2019 | **Test4Deep (conf-version)** | [Test4Deep: an Effective White-Box Testing for Deep Neural Networks](https://doi.org/10.1109/cse/euc.2019.00013) | — | CSE/EUC' 2019 |
| 2018 | **DeepRoad** | [DeepRoad: GAN-Based Metamorphic Testing and Input Validation Framework for Autonomous Driving Systems](https://doi.org/10.1145/3238147.3238187) | — | ASE' 2018 |
| 2018 | **DeepTest** | [DeepTest: automated testing of deep-neural-network-driven autonomous cars](https://doi.org/10.1145/3180155.3180220) | [arXiv](https://arxiv.org/abs/1708.08559) | ICSE' 2018 |
| 2018 | **DLFuzz (conf-version)** | [DLFuzz: differential fuzzing testing of deep learning systems](https://doi.org/10.1145/3236024.3264835) | — | ESEC/FSE' 2018 |
| 2017 | **DeepXplore** | [DeepXplore: Automated Whitebox Testing of Deep Learning Systems](https://doi.org/10.1145/3132747.3132785) | [arXiv](https://arxiv.org/abs/1705.06640) · [Code](https://github.com/peikexin9/deepxplore) | SOSP' 2017 |

#### Test Selection and Prioritization

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2026 | **AcTracer** | [AcTracer: Active Testing of Large Language Model via Multi-Stage Sampling](https://doi.org/10.1145/3744340) | [arXiv](https://arxiv.org/abs/2408.03573) · [Code](https://github.com/YuhengHuang42/test_selection_llm) | TOSEM |
| 2026 | **MetaDTS** | [MetaDTS: Distribution difference-based adaptive test input selection for Deep Neural Networks](https://doi.org/10.1016/j.sysarc.2025.103682) | — | JSA |
| 2026 | **PriCod** | [PriCod: Prioritizing Test Inputs for Compressed Deep Neural Networks](https://doi.org/10.1145/3730435) | — | TOSEM |
| 2026 | **SETS** | [SETS: A Simple yet Effective DNN Test Selection Approach](https://doi.org/10.1145/3772084) | — | TOSEM |
| 2025 | — | [Assessing the Robustness of Test Selection Methods for Deep Neural Networks](https://doi.org/10.1145/3715693) | — | TOSEM |
| 2025 | **AudioTest** | [AudioTest: Prioritizing Audio Test Cases](https://doi.org/10.1145/3728907) | — | PACMSE |
| 2025 | **DeepVec** | [DeepVec: State-Vector Aware Test Case Selection for Enhancing Recurrent Neural Network](https://doi.org/10.1109/tse.2025.3565037) | [Code](https://github.com/ZhonghaoJiang/DeepVec) | TSE |
| 2025 | **EATS** | [Efficient adaptive test case selection for DNNs robustness enhancement](https://doi.org/10.1016/j.jss.2025.112451) | — | JSS |
| 2025 | **LBT** | [Learning-Based Testing for Deep Learning: Enhancing Model Robustness with Adversarial Input Prioritization](https://arxiv.org/abs/2509.23961) | [arXiv](https://arxiv.org/abs/2509.23961) | arXiv (preprint) |
| 2025 | **MetaSel** | [MetaSel: A Test Selection Approach for Fine-Tuned DNN Models](https://doi.org/10.1109/tse.2025.3612253) | [arXiv](https://arxiv.org/abs/2503.17534) | TSE |
| 2025 | **Prophet** | [Prioritizing Speech Test Cases](https://doi.org/10.1145/3707450) | — | TOSEM |
| 2024 | — | [Can Coverage Criteria Guide Failure Discovery for Image Classifiers? An Empirical Study](https://doi.org/10.1145/3672446) | — | TOSEM |
| 2024 | **DeepGD** | [DeepGD: A Multi-Objective Black-Box Test Selection Approach for Deep Neural Networks](https://doi.org/10.1145/3644388) | — | TOSEM |
| 2024 | **DATIS** | [Distance-Aware Test Input Selection for Deep Neural Networks](https://doi.org/10.1145/3650212.3652125) | [Code](https://github.com/DATIS-24/DATIS) | ISSTA' 2024 |
| 2024 | **FAST** | [FAST: Boosting Uncertainty-based Test Prioritization Methods for Neural Networks via Feature Selection](https://doi.org/10.1145/3691620.3695472) | — | ASE' 2024 |
| 2024 | **FATS** | [FATS: Feature Distribution Analysis-Based Test Selection for Deep Learning Enhancement](https://doi.org/10.1109/tbdata.2023.3334648) | — | TBD |
| 2024 | **GraphPrior** | [GraphPrior: Mutation-based Test Input Prioritization for Graph Neural Networks](https://doi.org/10.1145/3607191) | — | TOSEM |
| 2024 | **NSS** | [Neuron Sensitivity-Guided Test Case Selection](https://doi.org/10.1145/3672454) | — | TOSEM |
| 2024 | **VRank** | [Prioritizing test cases for deep learning-based video classifiers](https://doi.org/10.1007/s10664-024-10520-1) | — | EMSE |
| 2024 | **TDPR** | [Prioritizing Test Inputs for DNNs Using Training Dynamics](https://doi.org/10.1145/3691620.3695498) | [Code](https://github.com/TDPR-24/TDPR) | ASE' 2024 |
| 2024 | **PCPrior** | [Test Input Prioritization for 3D Point Clouds](https://doi.org/10.1145/3643676) | — | TOSEM |
| 2024 | **NodeRank** | [Test Input Prioritization for Graph Neural Networks](https://doi.org/10.1109/tse.2024.3385538) | [Code](https://github.com/yinghuali/NodeRank) | TSE |
| 2024 | **MLPrior** | [Test Input Prioritization for Machine Learning Classifiers](https://doi.org/10.1109/tse.2024.3350019) | — | TSE |
| 2024 | — | [Test Selection for Deep Neural Networks using Meta-Models with Uncertainty Metrics](https://doi.org/10.1145/3650212.3680312) | — | ISSTA' 2024 |
| 2024 | — | [Towards Exploring the Limitations of Test Selection Techniques on Graph Neural Networks: An Empirical Study](https://doi.org/10.1007/s10664-024-10515-y) | — | EMSE |
| 2023 | **CertPri** | [CertPri: Certifiable Prioritization for Deep Neural Networks via Movement Cost in Feature Space](https://doi.org/10.1109/ase56229.2023.00126) | [arXiv](https://arxiv.org/abs/2307.09375) | ASE' 2023 |
| 2023 | **SA (journal-version)** | [Evaluating Surprise Adequacy for Deep Learning System Testing](https://doi.org/10.1145/3546947) | [Code](https://github.com/coinse/sadl) | TOSEM |
| 2023 | **NNS** | [In Defense of Simple Techniques for Neural Network Test Case Selection](https://doi.org/10.1145/3597926.3598073) | — | ISSTA' 2023 |
| 2023 | **RTS** | [Robust Test Selection for Deep Neural Networks](https://doi.org/10.1109/tse.2023.3330982) | [Code](https://github.com/swf1996120/RTS) | TSE |
| 2022 | **ATS** | [Adaptive test selection for deep neural networks](https://doi.org/10.1145/3510003.3510232) | [Code](https://github.com/SATE-Lab/ATS) | ICSE' 2022 |
| 2022 | **DAT** | [An Empirical Study on Data Distribution-Aware Test Selection for Deep Learning Enhancement](https://doi.org/10.1145/3511598) | — | TOSEM |
| 2022 | **DeepState** | [DeepState: Selecting Test Suites to Enhance the Robustness of Recurrent Neural Networks](https://doi.org/10.1145/3510003.3510231) | — | ICSE' 2022 |
| 2022 | — | [Simple techniques work surprisingly well for neural network test prioritization and active learning (replicability study)](https://doi.org/10.1145/3533767.3534375) | — | ISSTA' 2022 |
| 2021 | **PRIMA** | [Prioritizing Test Inputs for Deep Neural Networks via Mutation Analysis](https://doi.org/10.1109/icse43902.2021.00046) | — | ICSE' 2021 |
| 2021 | — | [Test Selection for Deep Learning Systems](https://doi.org/10.1145/3417330) | [arXiv](https://arxiv.org/abs/1904.13195) | TOSEM |
| 2021 | **TestRank** | [TestRank: Bringing Order into Unlabeled Test Instances for Deep Learning Tasks](https://proceedings.neurips.cc/paper/2021/hash/ae78510109d46b0a6eef9820a4ca95d6-Abstract.html) | [Code](https://github.com/cure-lab/TestRank) | NeurIPS' 2021 |
| 2020 | **DeepGini** | [DeepGini: prioritizing massive tests to enhance the robustness of deep neural networks](https://doi.org/10.1145/3395363.3397357) | — | ISSTA' 2020 |
| 2020 | **MCP** | [Multiple-boundary clustering and prioritization to promote neural network retraining](https://doi.org/10.1145/3324884.3416621) | — | ASE' 2020 |
| 2019 | **SA (conf-version)** | [Guiding Deep Learning System Testing Using Surprise Adequacy](https://doi.org/10.1109/icse.2019.00108) | [arXiv](https://arxiv.org/abs/1808.08444) | ICSE' 2019 |
| 2019 | — | [Input Prioritization for Testing Neural Networks](https://doi.org/10.1109/aitest.2019.000-6) | — | AITest' 2019 |

#### Model Repair

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2021 | **AI-Lancet** | [AI-Lancet: Locating Error-inducing Neurons to Optimize Neural Networks](https://doi.org/10.1145/3460120.3484818) | — | CCS' 2021 |
| 2019 | **DeepCorrect** | [DeepCorrect: Correcting DNN Models Against Image Distortions](https://doi.org/10.1109/tip.2019.2924172) | [arXiv](https://arxiv.org/abs/1705.02406) | TIP |

#### Other

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2018 | **DeepMutation** | [DeepMutation: Mutation Testing of Deep Learning Systems](https://doi.org/10.1109/issre.2018.00021) | [arXiv](https://arxiv.org/abs/1805.05206) | ISSRE' 2018 |

### Surveys

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2024 | — | [Test Optimization in DNN Testing: A Survey](https://doi.org/10.1145/3643678) | — | TOSEM |
| 2022 | — | [Machine Learning Testing: Survey, Landscapes and Horizons](https://doi.org/10.1109/tse.2019.2962027) | [arXiv](https://arxiv.org/abs/1906.10742) | TSE |
| 2021 | — | [神经网络验证和测试技术研究综述](https://doi.org/10.3778/j.issn.1002-8331.2106-0342) | — | 计算机工程与应用 |
| 2020 | — | [深度神经网络测试研究综述](https://doi.org/10.13328/j.cnki.jos.005951) | — | 软件学报 |

### Empirical Studies

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2025 | — | [Assessing the Robustness of Test Selection Methods for Deep Neural Networks](https://doi.org/10.1145/3715693) | — | TOSEM |
| 2024 | — | [Can Coverage Criteria Guide Failure Discovery for Image Classifiers? An Empirical Study](https://doi.org/10.1145/3672446) | — | TOSEM |
| 2024 | — | [Seed Selection for Testing Deep Neural Networks](https://doi.org/10.1145/3607190) | — | TOSEM |
| 2024 | — | [Towards Exploring the Limitations of Test Selection Techniques on Graph Neural Networks: An Empirical Study](https://doi.org/10.1007/s10664-024-10515-y) | — | EMSE |
| 2022 | **DAT** | [An Empirical Study on Data Distribution-Aware Test Selection for Deep Learning Enhancement](https://doi.org/10.1145/3511598) | — | TOSEM |
| 2022 | — | [Is Neuron Coverage Needed to Make Person Detection More Robust?](https://doi.org/10.1109/cvprw56347.2022.00326) | — | CVPRW' 2022 |
| 2022 | — | [Simple techniques work surprisingly well for neural network test prioritization and active learning (replicability study)](https://doi.org/10.1145/3533767.3534375) | — | ISSTA' 2022 |
| 2021 | — | [A Review and Refinement of Surprise Adequacy](https://doi.org/10.1109/deeptest52559.2021.00009) | — | DeepTest (workshop)' 2021 |
| 2021 | — | [Are Coverage Criteria Meaningful Metrics for DNNs?](https://doi.org/10.1109/ijcnn52387.2021.9533987) | — | IJCNN' 2021 |
| 2021 | — | [Test Selection for Deep Learning Systems](https://doi.org/10.1145/3417330) | [arXiv](https://arxiv.org/abs/1904.13195) | TOSEM |
| 2020 | — | [An Empirical Study on Correlation between Coverage and Robustness for Deep Neural Networks](https://doi.org/10.1109/iceccs51672.2020.00016) | [arXiv](https://arxiv.org/abs/1911.05904) | ICECCS' 2020 |
| 2020 | — | [Correlations between Deep Neural Network Model Coverage Criteria and Model Quality](https://doi.org/10.1145/3368089.3409671) | — | ESEC/FSE' 2020 |
| 2020 | — | [Is neuron coverage a meaningful measure for testing deep neural networks?](https://doi.org/10.1145/3368089.3409754) | — | ESEC/FSE' 2020 |
| 2020 | — | [Towards Characterizing Adversarial Defects of Deep Learning Software from the Lens of Uncertainty](https://doi.org/10.1145/3377811.3380368) | [arXiv](https://arxiv.org/abs/2004.11573) | ICSE' 2020 |
| 2019 | — | [Structural Coverage Criteria for Neural Networks Could Be Misleading](https://doi.org/10.1109/icse-nier.2019.00031) | — | ICSE-NIER' 2019 |

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=Ryan-LHR/awesome-dnn-testing-and-repair&type=date&legend=top-left)](https://www.star-history.com/?repos=Ryan-LHR%2Fawesome-dnn-testing-and-repair&type=date&legend=top-left)
