# Material — Xin Li

Facts only. No design opinions. Everything here is verified. Do not invent
anything; if a fact you want is not here, leave it out.

## Who

- Xin Li · 李鑫 — he/him not stated; use the name, avoid pronouns if unsure
- Ph.D. student, Nanyang Technological University (NTU), Singapore, 2025–2029 (expected)
- Advised by Prof. Chau Yuen (IEEE Fellow) — https://blogs.ntu.edu.sg/chau-yuen/
- Email xin019@e.ntu.edu.sg · site https://lixin.ai/
- GitHub https://github.com/LiXin97
- Google Scholar https://scholar.google.com/citations?user=Hxf8sNkAAAAJ
- LinkedIn https://www.linkedin.com/in/xin-li-1196331a0/
- CV (PDF, in repo) /data/Xin_Li_CV_2026.pdf
- Portrait (in repo) /data/avatar-280.webp — 280×280, the only photo that exists

## What the work is about, in his own words

Three threads, which he describes as one loop rather than three separate areas:

1. **Measure** — benchmarks and evaluation protocols built to be audited rather than
   trusted: per-problem provenance, verifier-checkable answers, and an explicit limit
   on what a score supports. Question: does a score mean what it appears to mean, and
   would we notice if it didn't?
2. **Train** — reinforcement learning, on-policy distillation and verifier-guided
   selection. Question: can we reward the reasoning we are able to check, rather than
   the answer we hope for?
3. **Compose** — protocols, memory and measurement for systems where several models
   interact. Question: when several models work together, does the interaction help,
   or quietly destroy answers that were already right?

The return leg: composition creates new failure modes, which have to be measured too.
The common ground: domains where an answer can be checked — formal verification,
mathematics, code, wireless systems.

## Publications

Marked `*` = equal contribution. "position" is his place in the author list.

### 2026

**Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation**
arXiv preprint, 2026 · position: first of 9
Xin Li, Hao Jiang, Xin Gao, Annan Wang, Yuchen Xie, Jinghao Guo, Xingwei Qu, Yichi Zhang, Chau Yuen
https://lixin.ai/DN-MOPD/ · https://arxiv.org/abs/2609.35347 · https://github.com/LiXin97/DN-MOPD
· data https://huggingface.co/datasets/XINLI1997/DN-MOPD-Data
· models https://huggingface.co/collections/XINLI1997/dn-mopd-6aba5f0df7bd8732d7205ed4
RESULT: label routing decides which teacher supervises a prompt but not how strongly that
teacher's feedback counts; normalizing the feedback scale per domain adds **1.2–3.1 points**
over label routing, across 2B, 4B and 9B students.

**WirelessMathBench-XL: An Auditable Benchmark for Wireless Mathematical Reasoning**
NeurIPS 2026, Evaluations and Datasets Track (poster) · position: first of 7
Xin Li, Mengbing Liu, Yiyang Zhu, Wenhe Zhang, Li Wei, Jiancheng An, Chau Yuen
https://lixin.ai/WirelessMathBench-XL/ · https://arxiv.org/abs/2509.23219
RESULT: **4,027** problems drawn from **836** arXiv papers across **20** wireless subfields.
Every problem ships 13-gram contamination-overlap evidence against public pretraining text.
Frontier models cluster at 86.5–91.3%.
CAUTION: during review the contamination claim was deliberately narrowed. It is "a rerunnable
audit producing per-problem evidence for one lexical channel", NOT "proof the benchmark is
clean". Do not overstate it.

**Measuring Collapse and Correction in Homogeneous-Panel LLM Debate** (project name: DebateLedger)
NeurIPS 2026, Evaluations and Datasets Track (poster) · position: joint first of 3
Xin Li*, Mengbing Liu*, Chau Yuen
https://lixin.ai/DebateLedger/
RESULT: across **6,925** logged MMLU-Pro debates, **253** collapses (a correct majority turned
wrong). A probe-gated freeze prevents **29** collapses but gives up **108** corrections — net
**−79** under equal weights. **58.9%** of collapses begin in the first debate round.

**Target-Local Verifier Choice in Best-of-K Reasoning Selection** (project name: TLVC)
Findings of EMNLP 2026 · position: first of 3
Xin Li, Hao Jiang, Weisi Lin
https://lixin.ai/TLVC/ · code https://github.com/LiXin97/TLVC
NOTE: no arXiv link exists. The project page currently shows a placeholder that 404s; ignore it.
RESULT: on a **34**-generator, **7**-verifier Best-of-K math panel, one strong process reward
model is the best fixed verifier overall — and still not the best verifier for every generator.
Label-free candidate statistics predict which verifier class wins.

**Stacked Intelligent Metasurface-Diffractive Deep Neural Networks for Onboard Terrain Classification from SAR Level-0 Raw Data**
IEEE Transactions on Signal Processing, 2026 · position: second of 4
Mengbing Liu, Xin Li, Jiancheng An, Chau Yuen
https://onboradsim.github.io/
RESULT: roughly **90%** accuracy classifying terrain directly from Level-0 raw SAR, with a
stacked metasurface performing the inference in-wave, before digitisation or downlink.
Extended from a workshop paper at ML4RS @ ICLR 2025.

**GraphReduce: Coverage-Preserving LLM Aggregation for E-commerce Review Insights**
EMNLP 2026, Industry Track · position: second of 4
Hao Jiang, Xin Li, Yichi Zhang, Weisi Lin
https://graphreduce.github.io/

**LiveCANNBench: Benchmark SWE AI Coding for Ascend CANN**
Findings of ACL 2026, pp. 22788–22803 · position: **eighth of 13**
Sijie Wang, Kai Zhao, Wee Peng Tay, Shuo Zhang, Chengwen Liu, Quanjiang Guo, Ren Junhao,
Xin Li, Heng Lian, Jingdi Lei, Rui She, Huacan Wang, Ronghao Chen
https://aclanthology.org/2026.findings-acl.1143/ · pdf https://aclanthology.org/2026.findings-acl.1143.pdf
RESULT: **400+** SWE-level task instances from real Ascend CANN repositories, multi-file,
multi-language and execution-aware, on a live benchmarking paradigm that mitigates leakage.

**Local Success Does Not Compose: Benchmarking Large Language Models for Compositional Formal Verification** (project name: DafnyComp)
ICLR 2026 · position: joint first of 5
Xu Xu*, Xin Li*, Xingwei Qu, Jie Fu, Binhang Yuan
https://dafnycomp.github.io/ · https://openreview.net/forum?id=y4kAMUBqLq · https://arxiv.org/abs/2509.23061
RESULT: a model can verify a function on its own and still fail once the specifications have to
compose. The benchmark measures the distance between those two results.

**Re:Form: Reducing Human Priors in Scalable Formal Software Verification with RL in LLMs: A Preliminary Study on Dafny**
TMLR 2026 · position: joint first (fifth of a long equal-contribution block)
Chuanhao Yan*, Fengdi Che*, Xuhan Huang*, Xu Xu*, Xin Li*, Yizhi Li*, Xingwei Qu*, …, Jie Fu
https://openreview.net/forum?id=cAQmIS4GOe · https://arxiv.org/abs/2507.16331 · https://github.com/Veri-Code/ReForm

**RobustMAD: Evaluating Real-World Robustness of Multimodal Small Language Models for Deployable Anomaly Detection Assistants**
TMLR 2026 · position: second of 7
Anushiya Arunan, Xin Li, Yan Qin, U-Xuan Tan, Nhu Khue Vuong, Xiaoli Li, Chau Yuen
https://robustmad.github.io/ · https://openreview.net/forum?id=skrA9UYNIZ · https://github.com/en-research/RobustMAD

### 2025

**LACP: LLM Agent Communication Protocol Requires Urgent Standardization**
AI4NextG workshop @ NeurIPS 2025 · position: first of 3
Xin Li, Mengbing Liu, Chau Yuen
https://lixin.ai/LACP/ · https://arxiv.org/abs/2510.13821

**WirelessMathBench: A Mathematical Modeling Benchmark for LLMs in Wireless Communications**
Findings of ACL 2025 · position: first of 6
Xin Li, Mengbing Liu, Li Wei, Jiancheng An, Mérouane Debbah, Chau Yuen
https://lixin.ai/WirelessMathBench/ · https://arxiv.org/abs/2505.14354
NOTE: the first benchmark for LLM mathematical reasoning in wireless communications, and the
work WirelessMathBench-XL extends.

**TransPathNet: A Novel Two-Stage Framework for Indoor Radio Map Prediction**
ICASSP 2025 · position: first of 5
Xin Li, Ran Liu, Saihua Xu, Sirajudeen Gulam Razul, Chau Yuen
https://lixin.ai/TransPathNet/ · https://github.com/LiXin97/TransPathNet · https://arxiv.org/abs/2501.16023
RESULT: placed **4th** in the Indoor Pathloss Prediction Challenge, at 9.73 dB RMSE.

**Onboard Terrain Classification via SIM-DNN** — ML4RS workshop @ ICLR 2025
https://onboradsim.github.io/ (later extended into the IEEE TSP 2026 paper above)

### 2020 — robot perception, before the Ph.D.

**Co-Planar Parametrization for Stereo-SLAM and Visual-Inertial Odometry**
IEEE Robotics and Automation Letters, 2020 · position: joint first of 5
Xin Li*, Yanyan Li*, Evin Pinar Örnek, Jinlong Lin, Federico Tombari
https://arxiv.org/abs/2009.12662 · https://github.com/LiXin97/Co-Planar-Parametrization-VIO

**Leveraging Planar Regularities for Point-Line Visual-Inertial Odometry**
IROS 2020 · position: joint first of 4
Xin Li*, Yijia He*, Jinlong Lin, Xiao Liu
https://arxiv.org/abs/2004.11969 · https://github.com/LiXin97/Co-Planar-Parametrization-VIO

### Named in his research description but with no venue yet
WritingPreferenceBench (https://WritingPreferenceBench.github.io/),
WirelessMathLM (https://lixin.ai/WirelessMathLM/),
ListOPD (https://lixin.ai/ListOPD/). Use or omit as you see fit.

## Experience

- **Research Assistant**, NTU Singapore — Apr 2024 – Jan 2025. Supervised by Chau Yuen.
  Built WirelessMathBench and TransPathNet.
- **SLAM Algorithm Engineer (Project Lead)**, Gausium Robotics, Singapore — Mar 2022 – Feb 2024.
  Led a team of five engineers building hierarchical multimodal localization (vision, LiDAR,
  Wi-Fi) for commercial cleaning robots: 95% localization accuracy across 100,000+ m² of complex
  environments; the system is deployed on a fleet of 1,000+ active robots.
- **Research Intern**, Microsoft Research Asia, Beijing — Sep 2020 – Mar 2021.
  Supervised by Dr. Yang Liu and Dr. Yizhong Zhang. Multi-sensor RGB-D + IMU fusion for
  large-scale indoor mapping; vectorized maps of 10,000+ m² at sub-meter accuracy.
- **Research Intern**, MEGVII, Beijing — Feb 2019 – Mar 2020. Supervised by Dr. Yijia He.
  Real-time monocular visual-inertial odometry; semi-dense 3D mesh reconstruction at 30+ FPS.

## Education

- Ph.D., Nanyang Technological University, Singapore — 2025–2029 (expected), adv. Chau Yuen
- M.E., Peking University, China — 2018–2021, adv. Prof. Jinlong Lin
- B.E., Northeastern University, China — 2014–2018

## Grants, awards, service

- Google Gemini Academic Program Award — US$10,000 — 2026
- Modal Academics Compute Grant — US$2,000 — 2025
- Cohere Labs Catalyst Grant — US$1,500 — 2025
- OpenAI Researcher Access Program — US$1,000 — 2025
  (all four are competitive compute/access grants he won himself, not advisor funding)
- Rohde & Schwarz Award, IEEE 6G Summit Singapore — 2025
- PREMIA Best Student Paper Award, finalist — 2025
- NTU Research Scholarship (full Ph.D. funding) — 2025
- Conference reviewer: NeurIPS, ICLR, ICML, AAAI, CVPR, ECCV, AISTATS, SIGGRAPH, IROS, ICRA
- Journal reviewer: IEEE RA-L, ACM TOG, IEEE TNNLS
- Workshop organizer: AIR4D @ IROS 2025 (https://4drobotics-iros2025.github.io/)
- Mentoring:
  - Chengqi Liang — M.Sc. dissertation, NTU, 2026; went on to a Ph.D. at CUHK-Shenzhen
  - Yukun Jin — B.Eng. final-year project, NTU, 2026 (Wuhan University undergraduate on NTU's 3.5+0.5+1 programme); went on to an M.Sc. at NTU
  - Haoyu Xu — M.Comp. dissertation, NUS, 2024; went on to a Ph.D. at Peking University

## Talks

- WirelessMathBench — ACL 2025, and NICE (NLP Academic Exchange Platform) Session 66,
  Oct 2025. Slides exist in the repo at /data/talk_slides/.

## Project pages that already exist and are live

https://lixin.ai/DebateLedger/ · /DN-MOPD/ · /ListOPD/ · /TLVC/ · /WirelessMathBench-XL/
· /WirelessMathLM/ · /WirelessMathBench/ · /LACP/ · /TransPathNet/
https://dafnycomp.github.io/ · https://robustmad.github.io/ · https://graphreduce.github.io/
· https://onboradsim.github.io/ · https://livecannbench.github.io/
· https://WritingPreferenceBench.github.io/

## Context for the site, not instructions for the design

He is a second-year-equivalent Ph.D. student who wants to be read as a researcher on LLM
evaluation, post-training and agents, and who is interested in research roles and internships
at frontier AI labs. His earlier record is robotics and wireless; he does not want it hidden,
but he does not want it to be the first impression either.
