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

Within each category, papers are listed by formal publication year, newest first. Preprint and online publication dates are recorded separately in the [paper data](data/papers.json).

Resource links are shown only when recorded in the paper data.

CCF venue categories in the paper data refer to the 2026 directory. A `null` value means no verified category is recorded.

### Research Papers

#### Coverage Metrics

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2025 | **QuanTest** | [QuanTest: Entanglement-Guided Testing of Quantum Neural Network Systems](https://doi.org/10.1145/3688840) | [arXiv](https://arxiv.org/abs/2402.12950) | TOSEM |
| 2023 | **IDC** | [Input Distribution Coverage: Measuring Feature Interaction Adequacy in Neural Network Testing](https://doi.org/10.1145/3576040) | — | TOSEM |
| 2022 | **testRNN** | [Coverage-Guided Testing for Recurrent Neural Networks](https://doi.org/10.1109/tr.2021.3080664) | — | TR |
| 2022 | — | [Is Neuron Coverage Needed to Make Person Detection More Robust?](https://doi.org/10.1109/cvprw56347.2022.00326) | — | CVPRW' 2022 |
| 2022 | **NPC** | [NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks](https://doi.org/10.1145/3490489) | [arXiv](https://arxiv.org/abs/2203.12915) · [Code](https://github.com/ltl7155/NPC) | TOSEM |
| 2022 | **RNN-Test** | [RNN-Test: Towards Adversarial Testing for Recurrent Neural Network Systems](https://doi.org/10.1109/tse.2021.3114353) | — | TSE |
| 2021 | — | [Are Coverage Criteria Meaningful Metrics for DNNs?](https://doi.org/10.1109/ijcnn52387.2021.9533987) | — | IJCNN' 2021 |
| 2021 | **DeepCon** | [DeepCon: Contribution Coverage Testing for Deep Learning Systems](https://doi.org/10.1109/saner50967.2021.00026) | — | SANER' 2021 |
| 2020 | — | [An Empirical Study on Correlation between Coverage and Robustness for Deep Neural Networks](https://doi.org/10.1109/iceccs51672.2020.00016) | [arXiv](https://arxiv.org/abs/1911.05904) | ICECCS' 2020 |
| 2020 | — | [Correlations between Deep Neural Network Model Coverage Criteria and Model Quality](https://doi.org/10.1145/3368089.3409671) | — | ESEC/FSE' 2020 |
| 2020 | — | [Is neuron coverage a meaningful measure for testing deep neural networks?](https://doi.org/10.1145/3368089.3409754) | — | ESEC/FSE' 2020 |
| 2019 | **DeepCT** | [DeepCT: Tomographic Combinatorial Testing for Deep Learning Systems](https://doi.org/10.1109/saner.2019.8668044) | — | SANER' 2019 |
| 2019 | **DeepPath** | [DeepPath: Path-Driven Testing Criteria for Deep Neural Networks](https://doi.org/10.1109/aitest.2019.00013) | — | AITest' 2019 |
| 2019 | **DeepStellar** | [DeepStellar: model-based quantitative analysis of stateful deep learning systems](https://doi.org/10.1145/3338906.3338954) | — | ESEC/FSE' 2019 |
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
| 2024 | **GIST** | [GIST: Generated Inputs Sets Transferability in Deep Learning](https://doi.org/10.1145/3672457) | [arXiv](https://arxiv.org/abs/2311.00801) | TOSEM |
| 2023 | **Test4Deep (journal-version)** | [A White-Box Testing for Deep Neural Networks Based on Neuron Coverage](https://doi.org/10.1109/tnnls.2022.3156620) | — | TNNLS |
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
| 2022 | **DeepState** | [DeepState: Selecting Test Suites to Enhance the Robustness of Recurrent Neural Networks](https://doi.org/10.1145/3510003.3510231) | — | ICSE' 2022 |
| 2021 | — | [Test Selection for Deep Learning Systems](https://doi.org/10.1145/3417330) | [arXiv](https://arxiv.org/abs/1904.13195) | TOSEM |

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
| 2022 | — | [Machine Learning Testing: Survey, Landscapes and Horizons](https://doi.org/10.1109/tse.2019.2962027) | [arXiv](https://arxiv.org/abs/1906.10742) | TSE |
| 2021 | — | [神经网络验证和测试技术研究综述](https://doi.org/10.3778/j.issn.1002-8331.2106-0342) | — | 计算机工程与应用 |
| 2020 | — | [深度神经网络测试研究综述](https://doi.org/10.13328/j.cnki.jos.005951) | — | 软件学报 |

### Empirical Studies

| Year | Name | Paper | Resources | Venue |
| --- | --- | --- | --- | --- |
| 2022 | — | [Is Neuron Coverage Needed to Make Person Detection More Robust?](https://doi.org/10.1109/cvprw56347.2022.00326) | — | CVPRW' 2022 |
| 2021 | — | [Are Coverage Criteria Meaningful Metrics for DNNs?](https://doi.org/10.1109/ijcnn52387.2021.9533987) | — | IJCNN' 2021 |
| 2021 | — | [Test Selection for Deep Learning Systems](https://doi.org/10.1145/3417330) | [arXiv](https://arxiv.org/abs/1904.13195) | TOSEM |
| 2020 | — | [An Empirical Study on Correlation between Coverage and Robustness for Deep Neural Networks](https://doi.org/10.1109/iceccs51672.2020.00016) | [arXiv](https://arxiv.org/abs/1911.05904) | ICECCS' 2020 |
| 2020 | — | [Correlations between Deep Neural Network Model Coverage Criteria and Model Quality](https://doi.org/10.1145/3368089.3409671) | — | ESEC/FSE' 2020 |
| 2020 | — | [Is neuron coverage a meaningful measure for testing deep neural networks?](https://doi.org/10.1145/3368089.3409754) | — | ESEC/FSE' 2020 |
| 2020 | — | [Towards Characterizing Adversarial Defects of Deep Learning Software from the Lens of Uncertainty](https://doi.org/10.1145/3377811.3380368) | [arXiv](https://arxiv.org/abs/2004.11573) | ICSE' 2020 |
| 2019 | — | [Structural Coverage Criteria for Neural Networks Could Be Misleading](https://doi.org/10.1109/icse-nier.2019.00031) | — | ICSE-NIER' 2019 |

## Star History

[![Star History Chart](https://api.star-history.com/chart?repos=Ryan-LHR/awesome-dnn-testing-and-repair&type=date&legend=top-left)](https://www.star-history.com/?repos=Ryan-LHR%2Fawesome-dnn-testing-and-repair&type=date&legend=top-left)
