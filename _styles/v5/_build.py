#!/usr/bin/env python3
"""Generates the site. Every fact comes from _styles/MATERIAL.md.

Run:  python3 _styles/v5/_build.py
Writes two copies from the same data:
  - _styles/v5/     the preview, with every layout and palette and the switcher
  - the repo root   the production site: Track layout, Paper palette, no switcher
Output is plain static HTML; the site itself has no build step.
"""
from pathlib import Path
from html import escape
import json

OUT = Path(__file__).parent
ROOT = OUT.parent.parent
SITE = "https://lixin.ai/"
PROD = False      # flipped at the bottom for the production pass

ME = "Xin Li"

# ---------------------------------------------------------------- papers
# thread: evaluate | train | orchestrate | wireless | robotics
P = [
  dict(id="debateledger", blurb="Distinguishes harmful collapse from useful correction in multi-agent debate.",
       thread="orchestrate", year=2026, lead=True,
       title="Measuring Collapse and Correction in Homogeneous-Panel LLM Debate", short="DebateLedger",
       authors="Xin Li*, Mengbing Liu*, Chau Yuen",
       venue="NeurIPS 2026", venue_long="NeurIPS 2026 · Evaluations and Datasets Track", pos="joint first of 3",
       links=[("Project", "https://lixin.ai/DebateLedger/")],
       fig=("−79", "net, under equal weights", True),
       claim="Debate can turn a wrong answer right, and it can also talk a correct majority into a wrong one. "
             "DebateLedger counts the two apart, and finds that stopping collapse also stops correction: "
             "across 6,925 logged MMLU-Pro debates, 253 collapses turned a correct majority wrong, and a probe-gated freeze "
             "prevents 29 of them but gives up 108 corrections — net −79 under equal weights. "
             "58.9% of collapses begin in the first debate round.",
       scope=None),
  dict(id="wmbxl", blurb="A wireless-math benchmark with per-problem provenance and reproducible text-overlap audits.",
       thread="evaluate", year=2026, lead=True,
       title="WirelessMathBench-XL: An Auditable Benchmark for Wireless Mathematical Reasoning", short="WirelessMathBench-XL",
       authors="Xin Li, Mengbing Liu, Yiyang Zhu, Wenhe Zhang, Li Wei, Jiancheng An, Chau Yuen",
       venue="NeurIPS 2026", venue_long="NeurIPS 2026 · Evaluations and Datasets Track", pos="first of 7",
       links=[("Project", "https://lixin.ai/WirelessMathBench-XL/"), ("arXiv", "https://arxiv.org/abs/2509.23219")],
       fig=("4,027", "problems", False),
       claim="A benchmark that ships its own audit: every problem carries 13-gram contamination-overlap evidence "
             "against public pretraining text. 4,027 problems drawn from 836 arXiv papers across 20 wireless subfields; "
             "frontier models cluster at 86.5–91.3%.",
       scope="A rerunnable audit producing per-problem evidence for one lexical channel — not a proof that the benchmark is clean."),
  dict(id="dnmopd", blurb="In multi-teacher distillation, normalizing each teacher's feedback scale per domain beats label routing alone.",
       thread="train", year=2026, lead=True,
       title="Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation", short="DN-MOPD",
       authors="Xin Li, Hao Jiang, Xin Gao, Annan Wang, Yuchen Xie, Jinghao Guo, Xingwei Qu, Yichi Zhang, Chau Yuen",
       venue="Preprint 2026", venue_long="arXiv preprint, 2026", pos="first of 9",
       links=[("Project", "https://lixin.ai/DN-MOPD/"), ("arXiv", "https://arxiv.org/abs/2609.35347"),
              ("Code", "https://github.com/LiXin97/DN-MOPD"),
              ("Data", "https://huggingface.co/datasets/XINLI1997/DN-MOPD-Data"),
              ("Models", "https://huggingface.co/collections/XINLI1997/dn-mopd-6aba5f0df7bd8732d7205ed4")],
       fig=("+1.2–3.1", "points over label routing", False),
       claim="Label routing decides which teacher supervises a prompt, but not how strongly that teacher's "
             "feedback counts. Normalizing the feedback scale per domain adds 1.2–3.1 points over label routing, across 2B, 4B and 9B students.",
       scope=None),
  dict(id="tlvc", blurb="No single verifier is best for every generator in best-of-K selection; label-free statistics predict which kind wins.",
       thread="orchestrate", year=2026, lead=True,
       title="Target-Local Verifier Choice in Best-of-K Reasoning Selection", short="TLVC",
       authors="Xin Li, Hao Jiang, Weisi Lin",
       venue="EMNLP 2026", venue_long="Findings of EMNLP 2026", pos="first of 3",
       links=[("Project", "https://lixin.ai/TLVC/"), ("Code", "https://github.com/LiXin97/TLVC")],
       fig=("34 × 7", "generators × verifiers", False),
       claim="On a 34-generator, 7-verifier Best-of-K math panel, one strong process reward model is the best fixed verifier overall — "
             "and still not the best verifier for every generator. Label-free candidate statistics predict which verifier class wins.",
       scope=None),
  dict(id="dafnycomp", blurb="Models that verify functions one at a time can still fail once the specifications have to compose.",
       thread="evaluate", year=2026, lead=True,
       title="Local Success Does Not Compose: Benchmarking Large Language Models for Compositional Formal Verification", short="DafnyComp",
       authors="Xu Xu*, Xin Li*, Xingwei Qu, Jie Fu, Binhang Yuan",
       venue="ICLR 2026", venue_long="ICLR 2026", pos="joint first of 5",
       links=[("Project", "https://dafnycomp.github.io/"), ("OpenReview", "https://openreview.net/forum?id=y4kAMUBqLq"),
              ("arXiv", "https://arxiv.org/abs/2509.23061")],
       fig=None,
       claim="A model can verify a function on its own and still fail once the specifications have to compose. "
             "The benchmark measures the distance between those two results.",
       scope=None),
  dict(id="reform", blurb="Reinforcement learning for formal software verification in Dafny, with fewer human priors.",
       thread="train", year=2026, lead=True,
       title="Re:Form: Reducing Human Priors in Scalable Formal Software Verification with RL in LLMs: A Preliminary Study on Dafny", short="Re:Form",
       authors="Chuanhao Yan*, Fengdi Che*, Xuhan Huang*, Xu Xu*, Xin Li*, Yizhi Li*, Xingwei Qu*, …, Jie Fu",
       venue="TMLR 2026", venue_long="TMLR 2026", pos="joint first",
       links=[("OpenReview", "https://openreview.net/forum?id=cAQmIS4GOe"), ("arXiv", "https://arxiv.org/abs/2507.16331"),
              ("Code", "https://github.com/Veri-Code/ReForm")],
       fig=None, claim=None, scope=None),
  dict(id="simd2nn", thread="wireless", year=2026, lead=False,
       title="Stacked Intelligent Metasurface-Diffractive Deep Neural Networks for Onboard Terrain Classification from SAR Level-0 Raw Data",
       short="SIM-D²NN",
       authors="Mengbing Liu, Xin Li, Jiancheng An, Chau Yuen",
       venue="IEEE TSP 2026", venue_long="IEEE Transactions on Signal Processing, 2026", pos="second of 4",
       links=[("Project", "https://onboradsim.github.io/")],
       fig=("~90%", "accuracy from raw SAR", False),
       claim="Classifies terrain directly from Level-0 raw SAR at roughly 90% accuracy, with a stacked metasurface performing the inference "
             "in-wave, before digitisation or downlink. Extended from a workshop paper at ML4RS @ ICLR 2025.",
       scope=None),
  dict(id="robustmad", thread="evaluate", year=2026, lead=False,
       title="RobustMAD: Evaluating Real-World Robustness of Multimodal Small Language Models for Deployable Anomaly Detection Assistants",
       short="RobustMAD",
       authors="Anushiya Arunan, Xin Li, Yan Qin, U-Xuan Tan, Nhu Khue Vuong, Xiaoli Li, Chau Yuen",
       venue="TMLR 2026", venue_long="TMLR 2026", pos="second of 7",
       links=[("Project", "https://robustmad.github.io/"), ("OpenReview", "https://openreview.net/forum?id=skrA9UYNIZ"),
              ("Code", "https://github.com/en-research/RobustMAD")],
       fig=None, claim=None, scope=None),
  dict(id="graphreduce", thread="train", year=2026, lead=False,
       title="GraphReduce: Coverage-Preserving LLM Aggregation for E-commerce Review Insights", short="GraphReduce",
       authors="Hao Jiang, Xin Li, Yichi Zhang, Weisi Lin",
       venue="EMNLP 2026", venue_long="EMNLP 2026 · Industry Track", pos="second of 4",
       links=[("Project", "https://graphreduce.github.io/")],
       fig=("59.3 → 93.1%", "extractor quality, with an anti-copy RL objective", False),
       claim="Turns thousands of review tuples into a ranked list of product insights while every tuple stays attached to "
             "the insight it supports: membership is computed outside the LLM, so coverage is 100% with no duplicates. "
             "An anti-copy reinforcement objective lifts the upstream extractor from 59.3% to 93.1% production quality.",
       scope=None),
  dict(id="livecann", thread="evaluate", year=2026, lead=False,
       title="LiveCANNBench: Benchmark SWE AI Coding for Ascend CANN", short="LiveCANNBench",
       authors="Sijie Wang, Kai Zhao, Wee Peng Tay, Shuo Zhang, Chengwen Liu, Quanjiang Guo, Ren Junhao, Xin Li, "
               "Heng Lian, Jingdi Lei, Rui She, Huacan Wang, Ronghao Chen",
       venue="ACL 2026", venue_long="Findings of ACL 2026", pos="eighth of 13",
       links=[("Anthology", "https://aclanthology.org/2026.findings-acl.1143/"),
              ("PDF", "https://aclanthology.org/2026.findings-acl.1143.pdf")],
       fig=("400+", "SWE-level tasks", False),
       claim="400+ SWE-level task instances built from real Ascend CANN repositories — multi-file, multi-language and execution-aware — "
             "on a live benchmarking paradigm that mitigates leakage.",
       scope=None),
  dict(id="lacp", thread="orchestrate", year=2025, lead=True,
       title="LACP: LLM Agent Communication Protocol Requires Urgent Standardization", short="LACP",
       authors="Xin Li, Mengbing Liu, Chau Yuen",
       venue="NeurIPS 2025 workshop", venue_long="AI4NextG workshop @ NeurIPS 2025", pos="first of 3",
       links=[("Project", "https://lixin.ai/LACP/"), ("arXiv", "https://arxiv.org/abs/2510.13821")],
       fig=None, claim=None, scope=None),
  dict(id="wmb", thread="evaluate", year=2025, lead=True,
       title="WirelessMathBench: A Mathematical Modeling Benchmark for LLMs in Wireless Communications", short="WirelessMathBench",
       authors="Xin Li, Mengbing Liu, Li Wei, Jiancheng An, Mérouane Debbah, Chau Yuen",
       venue="ACL 2025", venue_long="Findings of ACL 2025", pos="first of 6",
       links=[("Project", "https://lixin.ai/WirelessMathBench/"), ("arXiv", "https://arxiv.org/abs/2505.14354")],
       fig=None,
       claim="The first benchmark for LLM mathematical reasoning in wireless communications, and the work WirelessMathBench-XL extends.",
       scope=None),
  dict(id="transpath", thread="wireless", year=2025, lead=True,
       title="TransPathNet: A Novel Two-Stage Framework for Indoor Radio Map Prediction", short="TransPathNet",
       authors="Xin Li, Ran Liu, Saihua Xu, Sirajudeen Gulam Razul, Chau Yuen",
       venue="ICASSP 2025", venue_long="ICASSP 2025", pos="first of 5",
       links=[("Project", "https://lixin.ai/TransPathNet/"), ("Code", "https://github.com/LiXin97/TransPathNet"),
              ("arXiv", "https://arxiv.org/abs/2501.16023")],
       fig=("4th", "Indoor Pathloss Prediction Challenge", False),
       claim="Placed 4th in the Indoor Pathloss Prediction Challenge, at 9.73 dB RMSE.", scope=None),
  dict(id="coplanar", thread="robotics", year=2020, lead=True,
       title="Co-Planar Parametrization for Stereo-SLAM and Visual-Inertial Odometry", short="Co-Planar VIO",
       authors="Xin Li*, Yanyan Li*, Evin Pinar Örnek, Jinlong Lin, Federico Tombari",
       venue="IEEE RA-L 2020", venue_long="IEEE Robotics and Automation Letters, 2020", pos="joint first of 5",
       links=[("arXiv", "https://arxiv.org/abs/2009.12662"), ("Code", "https://github.com/LiXin97/Co-Planar-Parametrization-VIO")],
       fig=None, claim=None, scope=None),
  dict(id="planar", thread="robotics", year=2020, lead=True,
       title="Leveraging Planar Regularities for Point-Line Visual-Inertial Odometry", short="Planar VIO",
       authors="Xin Li*, Yijia He*, Jinlong Lin, Xiao Liu",
       venue="IROS 2020", venue_long="IROS 2020", pos="joint first of 4",
       links=[("arXiv", "https://arxiv.org/abs/2004.11969"), ("Code", "https://github.com/LiXin97/Co-Planar-Parametrization-VIO")],
       fig=None, claim=None, scope=None),
]
BY = {p["id"]: p for p in P}

THREADS = [
  dict(id="evaluate", n="01", verb="Evaluate",
       q="What can models do, where do they fail, and how reliably can we tell?",
       desc="Benchmarks, robustness tests and evaluation protocols built to be audited rather than trusted: per-problem provenance, "
            "verifier-checkable answers, and an explicit limit on what a score supports.",
       hero="wmbxl", hero_fig=("4,027", "problems, each carrying its own contamination evidence"),
       works=["wmbxl", "dafnycomp", "livecann", "robustmad", "wmb"],
       also=[("WritingPreferenceBench", "https://WritingPreferenceBench.github.io/", "Project page; no venue yet.")]),
  dict(id="train", n="02", verb="Train",
       q="How can models learn from verifiers, rewards, and other models?",
       desc="What the training signal should be — which reward, and how much each teacher's feedback should count.",
       hero="dnmopd", hero_fig=("+1.2–3.1", "points from normalizing each teacher's feedback scale"),
       works=["dnmopd", "reform", "graphreduce"],
       also=[("ListOPD", "https://lixin.ai/ListOPD/",
              "A computable extrapolation cliff in on-policy distillation of near-deterministic structured outputs. Project page; no venue yet."),
             ("WirelessMathLM", "https://lixin.ai/WirelessMathLM/",
              "The earlier arXiv version of WirelessMathBench-XL, which also trains models on the benchmark with reinforcement learning.")]),
  dict(id="orchestrate", n="03", verb="Orchestrate",
       q="How should models, tools, and verifiers work together to complete tasks reliably?",
       desc="The system around a model at inference time: harnesses and tools, verifier choice, and protocols for several agents "
            "working together — including when that system breaks answers that were already right.",
       hero="debateledger", hero_fig=("29 / 108", "collapses a freeze prevents / corrections it gives up"),
       works=["debateledger", "tlvc", "lacp"], also=[]),
]
TH = {t["id"]: t for t in THREADS}

RETURN = "Every new way of orchestrating models creates new failure modes, which need to be evaluated in turn."
DESC = ("Xin Li, Ph.D. student at NTU Singapore, working on LLM agents: evaluating, training and orchestrating them, "
        "and agents that improve themselves.")
LEDE = ("I work on LLM agents — evaluating what they can do, training them, and orchestrating them with tools, "
        "verifiers and each other to get real tasks done. Lately, on agents that improve themselves.")
GROUND = ["formal verification", "mathematics", "code"]
GROUND_K = "So far, mostly where an answer can be checked:"
GROUND_NOW = "Now, self-improvement beyond checkable answers."
SEEK = "I’m looking for <b>research internships in 2027</b>, on LLM agents, post-training, and self-improvement."

# Every news item, newest first. Home shows the first five; news.html shows them all.
NEWS = [
  ("Sep 2026", 'Our paper <a href="https://onboradsim.github.io/">SIM-D<sup>2</sup>NN</a> (on onboard terrain classification straight from raw SAR data, using a stacked metasurface as the classifier) was accepted to IEEE Transactions on Signal Processing.'),
  ("Sep 2026", 'Two of our papers were accepted to the NeurIPS 2026 Evaluations and Datasets Track: <a href="https://lixin.ai/WirelessMathBench-XL/">WirelessMathBench-XL</a>, a wireless-math benchmark shipped with a rerunnable contamination audit, and <a href="https://lixin.ai/DebateLedger/">DebateLedger</a>, a protocol separating harmful collapse from useful correction in multi-agent LLM debate.'),
  ("Aug 2026", 'Two of our papers were accepted to EMNLP 2026: <a href="https://lixin.ai/TLVC/">TLVC</a>, on picking the right verifier for best-of-K reasoning selection (Findings), and <a href="https://graphreduce.github.io/">GraphReduce</a>, on coverage-preserving LLM aggregation of e-commerce reviews (Industry Track).'),
  ("Jun 2026", 'Our paper <a href="https://robustmad.github.io/">RobustMAD</a> (a robustness benchmark for multimodal small language models in anomaly detection) was accepted to TMLR.'),
  ("May 2026", 'Our paper <a href="https://arxiv.org/pdf/2507.16331">Re:Form</a> (on cutting human priors from RL-trained formal software verification) was accepted to TMLR.'),
  ("Apr 2026", 'Our paper <a href="https://livecannbench.github.io/">LiveCANNBench</a> (a benchmark for AI coding on Ascend CANN) was accepted to Findings of ACL 2026.'),
  ("Jan 2026", 'Received a Google Gemini Academic Program Award (US$10,000).'),
  ("Jan 2026", 'Our paper <a href="https://dafnycomp.github.io/">DafnyComp</a> (on benchmarking LLMs for compositional formal verification) was accepted to ICLR 2026.'),
  ("Dec 2025", 'Received the Rohde &amp; Schwarz Award at the IEEE 6G Summit Singapore.'),
  ("Sep 2025", 'Our paper <a href="https://lixin.ai/LACP/">LACP</a> (a communication protocol for LLM agents) was accepted to <a href="https://ai4nextg.github.io/">AI4NextG @ NeurIPS 2025</a>.'),
  ("May 2025", 'Our paper <a href="https://lixin.ai/WirelessMathBench/">WirelessMathBench</a> (a benchmark for mathematical reasoning in wireless communications) was accepted to Findings of ACL 2025.'),
  ("May 2025", 'Our workshop on <a href="https://4drobotics-iros2025.github.io/">Advancements for Intelligent Robotics in 4D Scenes</a> at IROS 2025 was accepted.'),
  ("Mar 2025", 'Our paper <a href="https://onboradsim.github.io/">SIM-D<sup>2</sup>NN</a> (on onboard terrain classification for remote sensing) was accepted to the <a href="https://ml-for-rs.github.io/iclr2025/">ML4RS @ ICLR 2025</a>.'),
  ("Jan 2025", 'Our paper <a href="https://lixin.ai/TransPathNet/">TransPathNet</a> (on indoor pathloss prediction) was accepted to ICASSP 2025, ranked 4th in the Indoor Pathloss Challenge.'),
  ("Jan 2025", 'Started my Ph.D. at NTU, supported by the NTU Research Scholarship.'),
]

FONTS = ("https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400"
         "&family=IBM+Plex+Mono:wght@400;500;600&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500;600"
         "&family=Inter+Tight:wght@500;600;700;800;900&family=Inter:wght@400;500;600&display=swap")
CJK = "https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500&family=Noto+Sans+SC:wght@500&display=swap&text=%E6%9D%8E%E9%91%AB"

NAV = [("evaluate", "Evaluate", "evaluate.html"), ("train", "Train", "train.html"), ("orchestrate", "Orchestrate", "orchestrate.html"),
       None, ("pubs", "Publications", "publications.html"), ("news", "News", "news.html"), ("about", "About", "about.html")]


# ---------------------------------------------------------------- helpers
def e(s):
    return escape(s, quote=True)


def authors_html(a):
    out = []
    for name in a.split(", "):
        star = name.endswith("*")
        bare = name.rstrip("*")
        if bare == ME:
            out.append(f'<b class="me">{e(bare)}</b>{"<sup>*</sup>" if star else ""}')
        else:
            out.append(f'{e(bare)}{"<sup>*</sup>" if star else ""}')
    return ", ".join(out)


def links_html(links, cls="links"):
    return f'<p class="{cls}">' + "".join(
        f'<a href="{e(u)}">{e(t)}</a>' for t, u in links) + "</p>"


def subtitle(p):
    """The descriptive part of a title, without a leading project name."""
    t = p["title"]
    if t.startswith(p["short"] + ":"):
        t = t[len(p["short"]) + 1:].strip()
    return t.split(":")[0].strip()


def vshort(p):
    """Short venue that never drops Findings or Industry Track."""
    v = p["venue_long"]
    return (v.replace("IEEE Transactions on Signal Processing, 2026", "IEEE TSP 2026")
             .replace("EMNLP 2026 · Industry Track", "EMNLP 2026 Industry")
             .replace("NeurIPS 2026 · Evaluations and Datasets Track", "NeurIPS 2026")
             .replace("arXiv preprint, 2026", "Preprint 2026")
             .replace("AI4NextG workshop @ NeurIPS 2025", "AI4NextG @ NeurIPS 2025")
             .replace("IEEE Robotics and Automation Letters, 2020", "IEEE RA-L 2020"))


def venue_pill(p):
    return f'<span class="venue">{e(vshort(p))}</span>'


def abbrev(a, keep=3):
    """First `keep` names, an ellipsis, and the last name, once a list runs past five."""
    names = a.split(", ")
    if len(names) <= 5 or "…" in names:
        return a
    return ", ".join(names[:keep] + ["…", names[-1]])


def short_pos(pos):
    if pos.startswith("first"):
        return "first author"
    if pos.startswith("joint first"):
        return "joint first author"
    return pos


def page(slug, title, body, desc, home="index.html", extra_js="", canon=None):
    nav = []
    for item in NAV:
        if item is None:
            nav.append('<span class="nav__sep" aria-hidden="true"></span>')
            continue
        key, label, href = item
        cur = ' aria-current="page"' if key == slug else ""
        nav.append(f'<a href="{href}"{cur}>{label}</a>')
    nav.append('<a href="/data/Xin_Li_CV_2026.pdf">CV</a>')
    if PROD:
        return prod_page(slug, title, body, desc, nav, canon)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<script>(function(){{try{{var q=new URLSearchParams(location.search).get('theme');var t=q||localStorage.getItem('v5-theme')||'paper';if(q)localStorage.setItem('v5-theme',q);document.documentElement.dataset.theme=t;}}catch(_){{document.documentElement.dataset.theme='paper';}}document.documentElement.classList.add('js');}})();</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<link rel="stylesheet" href="{CJK}">
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/paper.css">
<link rel="stylesheet" href="css/night.css">
<link rel="stylesheet" href="css/swiss.css">
<link rel="stylesheet" href="css/present.css">
<link rel="icon" href="/images/icon-32.png?v=4">
</head>
<body class="page--{slug}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
  <a class="brand" href="{home}">Xin Li<span lang="zh-Hans">李鑫</span></a>
  <nav class="nav" aria-label="Site">{"".join(nav)}</nav>
</div></header>
<main id="main" tabindex="-1">
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <p>Xin Li · Nanyang Technological University, Singapore</p>
  <p><a href="mailto:xin019@e.ntu.edu.sg">xin019@e.ntu.edu.sg</a> · Updated October 2026</p>
</div></footer>
<script src="js/preview.js" defer></script>
{'<script src="js/filter.js" defer></script>' if slug == "pubs" else ""}{extra_js}
</body>
</html>
"""


# ---------------------------------------------------------------- production shell
PROD_FONTS = ("https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400"
              "&family=IBM+Plex+Mono:wght@400;500;600&display=swap")
PROD_CJK = "https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@500&display=swap&text=%E6%9D%8E%E9%91%AB"
PROD_HAND = "https://fonts.googleapis.com/css2?family=Caveat:wght@700&display=swap&text=Change%20the%20future"
# Home only: mount the 3D portrait unless the reader asked for less motion; without WebGL the photo stays.
PORTRAIT_JS = """<script type="module">if (!matchMedia('(prefers-reduced-motion: reduce)').matches)
  import('/assets/portrait3d.js').then((m) => m.mountPortrait(document.querySelector('.portrait3d'))).catch(() => {});</script>
"""
HOME_TITLE = "Xin Li @ NTU — LLM Agents"
SHARE_CARD = "https://lixin.ai/data/share-card.jpg?v=6"

# The old site was one page with section anchors; links to them (CVs, emails, other
# pages) land on the new home, so send each to where that section now lives.
OLD_ANCHORS = """
<script>(function(){var m={publications:'publications.html',news:'news.html',about:'about.html',
experience:'about.html#experience',education:'about.html#education',awards:'about.html#awards',
mentoring:'about.html#mentoring',service:'about.html#service',talks:'about.html#talks'};
var t=m[location.hash.slice(1)];if(t)location.replace(t);})();</script>"""


def json_ld():
    return """
<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "ProfilePage", "@id": "https://lixin.ai/#profile",
 "dateCreated": "2024-04-05T14:53:00+08:00", "dateModified": "2026-10-06T10:00:00+08:00", "url": "https://lixin.ai/",
 "mainEntity": {"@type": "Person", "@id": "https://lixin.ai/#person", "name": "Xin Li", "alternateName": "李鑫",
  "url": "https://lixin.ai/", "image": "https://lixin.ai/data/XinLI_profile.webp", "jobTitle": "PhD Student",
  "affiliation": {"@type": "Organization", "name": "Nanyang Technological University", "url": "https://www.ntu.edu.sg/"},
  "description": """ + json.dumps(DESC, ensure_ascii=False) + """,
  "email": "mailto:xin019@e.ntu.edu.sg",
  "sameAs": ["https://github.com/LiXin97", "https://lixin97.github.io/", "https://www.linkedin.com/in/xin-li-1196331a0/",
             "https://scholar.google.com/citations?user=Hxf8sNkAAAAJ"]}}
</script>
<script type="application/ld+json">
{"@context": "https://schema.org", "@type": "WebSite", "@id": "https://lixin.ai/#website", "url": "https://lixin.ai/",
 "name": "Xin Li @ NTU", "publisher": {"@type": "Person", "@id": "https://lixin.ai/#person"}}
</script>"""


def prod_page(slug, title, body, desc, nav, canon):
    path = canon if canon is not None else ("publications.html" if slug == "pubs" else f"{slug}.html")
    url = SITE + path
    js = '<script src="/assets/filter.js" defer></script>\n' if slug == "pubs" else ""
    hand = f'\n<link rel="stylesheet" href="{PROD_HAND}">' if path == "" else ""
    return f"""<!doctype html>
<!-- Generated by _styles/v5/_build.py from _styles/MATERIAL.md. Edit there, then rerun it. -->
<html lang="en" data-theme="paper">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
<meta name="author" content="Xin Li">
<meta name="theme-color" content="#F5F1E8" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#16140F" media="(prefers-color-scheme: dark)">
<meta property="og:title" content="{e(title)}">
<meta property="og:site_name" content="lixin.ai">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SHARE_CARD}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SHARE_CARD}">
<meta name="color-scheme" content="light dark">
<script>(function(){{var r=document.documentElement;r.classList.add('js');try{{var m=localStorage.getItem('theme');if(m==='light'||m==='dark')r.setAttribute('data-mode',m);}}catch(_){{}}}})();</script>{OLD_ANCHORS if path == "" else ""}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{PROD_FONTS}">
<link rel="stylesheet" href="{PROD_CJK}">{hand}
<link rel="stylesheet" href="/assets/site.css">
<link rel="icon" type="image/png" sizes="16x16" href="/images/icon-16.png?v=4">
<link rel="icon" type="image/png" sizes="32x32" href="/images/icon-32.png?v=4">
<link rel="apple-touch-icon" sizes="180x180" href="/images/icon-180.png?v=4">{json_ld() if path == "" else ""}
</head>
<body class="page--{slug}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head"><div class="wrap">
  <a class="brand" href="/">Xin Li<span lang="zh-Hans">李鑫</span></a>
  <nav class="nav" aria-label="Site">{"".join(nav)}</nav>
</div></header>
<main id="main" tabindex="-1">
{body}
</main>
<footer class="site-foot"><div class="wrap">
  <p>Xin Li · Nanyang Technological University, Singapore</p>
  <p><a href="mailto:xin019@e.ntu.edu.sg">xin019@e.ntu.edu.sg</a> · Updated October 2026</p>
  <p class="mode-switch" role="group" aria-label="Colour scheme"><span>Theme</span><button type="button" data-mode="system">Auto</button><button type="button" data-mode="light">Light</button><button type="button" data-mode="dark">Dark</button></p>
</div></footer>
<script src="/assets/mode.js" defer></script>
{PORTRAIT_JS if path == "" else ""}{js}</body>
</html>
"""


# ---------------------------------------------------------------- loop (shared)
def loop_html(heading_level="h2"):
    items = []
    for t in THREADS:
        fig_n, fig_l = t["hero_fig"]
        items.append(f"""
      <li class="loop__item">
        <span class="loop__n">{t['n']}</span>
        <a class="loop__verb" href="{t['id']}.html">{t['verb']}<span class="loop__go" aria-hidden="true">→</span></a>
        <p class="loop__q">{e(t['q'])}</p>
        <p class="loop__fig"><b>{e(fig_n)}</b><span>{e(fig_l)}</span></p>
      </li>""")
    ground = "".join(f"<span>{e(g)}</span>" for g in GROUND)
    return f"""
  <section class="loop wrap" aria-labelledby="loop-h">
    <{heading_level} id="loop-h" class="label"><span>The research, as one loop</span><span class="label__aside">three questions · one return</span></{heading_level}>
    <ol class="loop__list">{"".join(items)}
    </ol>
    <p class="loop__return"><span class="loop__return-mark" aria-hidden="true">↺</span><span><b>Back to 01.</b> {e(RETURN)}</span></p>
    <p class="loop__ground"><span class="loop__ground-k">{e(GROUND_K)}</span>{ground}<span class="loop__ground-now">{e(GROUND_NOW)}</span></p>
  </section>"""


# ---------------------------------------------------------------- loop drawings
import math


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def _arc(cx, cy, r, a1, a2):
    """Clockwise arc from a1 to a2 degrees (0 = east, 90 = south, as SVG draws)."""
    x1, y1 = _pt(cx, cy, r, a1)
    x2, y2 = _pt(cx, cy, r, a2)
    large = 1 if (a2 - a1) % 360 > 180 else 0
    return f"M {x1:.2f} {y1:.2f} A {r} {r} 0 {large} 1 {x2:.2f} {y2:.2f}"


RING = dict(size=440, c=220, r=160, nr=25, gap=14)
NODE_ANG = {"evaluate": -90, "train": 30, "orchestrate": 150}


def ring_svg():
    """The loop as a ring: 01 at the top, clockwise. The leg from 03 back to 01 is the return."""
    c, r, nr, g = RING["c"], RING["r"], RING["nr"], RING["gap"]
    legs = [("evaluate", "train", "fwd"), ("train", "orchestrate", "fwd"), ("orchestrate", "evaluate", "ret")]
    paths = []
    for a, b, kind in legs:
        a1 = NODE_ANG[a] + g
        a2 = NODE_ANG[b] - g
        if a2 <= a1:
            a2 += 360
        mk = "url(#ah-ret)" if kind == "ret" else "url(#ah)"
        paths.append(f'<path class="ring__leg ring__leg--{kind} ring__leg--{a}" d="{_arc(c, c, r, a1, a2)}" marker-end="{mk}"/>')
    nodes = []
    for t in THREADS:
        x, y = _pt(c, c, r, NODE_ANG[t["id"]])
        nodes.append(f'<g class="ring__node ring__node--{t["id"]}"><circle cx="{x:.2f}" cy="{y:.2f}" r="{nr}"/>'
                     f'<text x="{x:.2f}" y="{y:.2f}" dy=".35em">{t["n"]}</text></g>')
    label_path = _arc(c, c, r + 21, NODE_ANG["orchestrate"] + 18, NODE_ANG["evaluate"] + 360 - 18)
    orbit = f"M {c} {c - r} A {r} {r} 0 0 1 {c} {c + r} A {r} {r} 0 0 1 {c} {c - r}"
    return f"""<svg class="ring__svg" viewBox="0 0 {RING['size']} {RING['size']}" role="img"
      aria-label="The research loop: 01 Evaluate, then 02 Train, then 03 Orchestrate, and back to 01 Evaluate.">
      <defs>
        <marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="9" markerHeight="9" markerUnits="userSpaceOnUse" orient="auto"><path class="ring__ah" d="M0,1 L9,5 L0,9 z"/></marker>
        <marker id="ah-ret" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="11" markerHeight="11" markerUnits="userSpaceOnUse" orient="auto"><path class="ring__ah ring__ah--ret" d="M0,1 L9,5 L0,9 z"/></marker>
        <path id="ring-label-path" d="{label_path}"/>
      </defs>
      <circle class="ring__track" cx="{c}" cy="{c}" r="{r}"/>
      {''.join(paths)}
      <text class="ring__arclabel"><textPath href="#ring-label-path" startOffset="50%" text-anchor="middle">new failure modes</textPath></text>
      <circle class="ring__dot" r="5"><animateMotion dur="9s" repeatCount="indefinite" path="{orbit}"/></circle>
      {''.join(nodes)}
    </svg>"""


def ring_center():
    return f"""<div class="ring__center">
        <p class="ring__k">So far</p>
        <p class="ring__v">where an answer can be checked</p>
        <span class="ring__rule" aria-hidden="true"></span>
        <p class="ring__k ring__k--now">Now</p>
        <p class="ring__v ring__v--now">self-improvement beyond checkable answers</p>
      </div>"""


def thread_label(t, cls):
    n, lbl = t["hero_fig"]
    return f"""<div class="{cls} {cls}--{t['id']}">
        <p class="tl__n">{t['n']}</p>
        <a class="tl__verb" href="{t['id']}.html">{t['verb']}</a>
        <p class="tl__q">{e(t['q'])}</p>
        <p class="tl__fig"><b>{e(n)}</b> <span>{e(lbl)}</span></p>
      </div>"""


HERO_LINKS = [("Google Scholar", "https://scholar.google.com/citations?user=Hxf8sNkAAAAJ"), ("GitHub", "https://github.com/LiXin97"),
              ("CV", "/data/Xin_Li_CV_2026.pdf"), ("Email", "mailto:xin019@e.ntu.edu.sg")]


def hero_block(variant=""):
    return f"""
  <header class="hero wrap {variant}">
    <div class="hero__text">
      <p class="kicker">Ph.D. student · Nanyang Technological University · advised by <a href="https://blogs.ntu.edu.sg/chau-yuen/">Prof. Chau Yuen</a></p>
      <h1 class="name">Xin Li<span class="name__cjk" lang="zh-Hans">李鑫</span></h1>
      <p class="lede">{e(LEDE)}</p>
      <p class="hero__seek">{SEEK}</p>
      {links_html(HERO_LINKS, "links links--plain hero__links")}
    </div>
    {hero_photo()}
  </header>"""


def hero_photo():
    """Production: the 3D depth portrait (assets/portrait3d.js) drawn over the photo, which stays as the fallback."""
    img = '<img class="hero__photo" src="/data/avatar-560.webp" width="560" height="560" alt="Portrait of Xin Li" fetchpriority="high">'
    if not PROD:
        return img
    return f"""<div class="hero__photo portrait3d" data-assets="/assets/portrait/">
      {img.replace(' class="hero__photo"', '')}
      <p class="portrait3d__slogan" aria-hidden="true">Change the future</p>
    </div>"""


def tail_sections(also_list=True):
    """Also-in-2026, recent and coda. Track leaves the 2026 list out: its panels already name every paper."""
    also_ids = ["dafnycomp", "reform", "simd2nn", "robustmad", "graphreduce", "livecann"]
    also = "".join(f"""
        <li><a class="also__name" href="{e(BY[i]['links'][0][1])}">{e(BY[i]['short'])}</a><span class="also__t">{e(subtitle(BY[i]))}</span><span class="also__v">{e(vshort(BY[i]))}</span></li>"""
                   for i in also_ids)
    recent = news_items(NEWS[:5])
    also_sec = f"""
  <section class="also wrap" aria-labelledby="also-h">
    <h2 id="also-h" class="label"><span>Also in 2026</span><a class="label__aside" href="publications.html">All publications →</a></h2>
    <ul class="also__list">{also}
    </ul>
  </section>""" if also_list else ""
    return also_sec + f"""
  <section class="recent wrap" aria-labelledby="recent-h">
    <h2 id="recent-h" class="label"><span>Recent</span><a class="label__aside" href="news.html">All news →</a></h2>
    <ol class="recent__list">{recent}</ol>
  </section>
  <section class="coda wrap">
    <div>
      <h2 class="label"><span>Before the Ph.D.</span></h2>
      <p>Robot perception — visual-inertial odometry at MEGVII, RGB-D + IMU indoor mapping at Microsoft Research Asia,
        and multimodal localization at Gausium Robotics, where I led a five-engineer team and shipped to a fleet of
        <b>1,000+</b> commercial cleaning robots. <a href="about.html">More →</a></p>
    </div>
    <div>
      <h2 class="label"><span>Contact</span></h2>
      <p>Looking for research internships in 2027, and always glad to talk about research or collaboration.</p>
      <p class="links links--plain"><a href="mailto:xin019@e.ntu.edu.sg">xin019@e.ntu.edu.sg</a><a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ">Scholar</a><a href="https://github.com/LiXin97">GitHub</a><a href="https://www.linkedin.com/in/xin-li-1196331a0/">LinkedIn</a><a href="/data/Xin_Li_CV_2026.pdf">CV</a></p>
    </div>
  </section>"""


def evidence(p):
    """One result, small: the reading, then what it is from."""
    n, lbl, neg = p["fig"]
    return f"""<a class="ev" href="{e(p['links'][0][1])}">
          <span class="ev__fig{' is-neg' if neg else ''}">{e(n)}</span>
          <span class="ev__lbl">{e(lbl)}</span>
          <span class="ev__name">{e(p['short'])}</span>
          <span class="ev__v">{e(vshort(p))}</span>
        </a>"""


# ---------------------------------------------------------------- index
def card(p):
    t = TH.get(p["thread"])
    tag = f'{t["n"]} · {t["verb"]}' if t else ""
    n, lbl, neg = p["fig"]
    scope = f'<p class="scope"><b>Scope</b> {e(p["scope"])}</p>' if p["scope"] else ""
    return f"""
      <article class="card" id="r-{p['id']}">
        <p class="card__tag"><a href="{p['thread']}.html">{e(tag)}</a></p>
        <p class="card__fig{' is-neg' if neg else ''}"><b>{e(n)}</b><span>{e(lbl)}</span></p>
        <h3 class="card__title"><a href="{e(p['links'][0][1])}">{e(p['short'])}</a></h3>
        <p class="card__authors">{authors_html(abbrev(p['authors']))}</p>
        <p class="card__meta"><span>{e(p['venue_long'])}</span></p>
        <p class="card__claim">{e(p['claim'])}</p>
        {scope}
        {links_html(p['links'][1:], 'links links--quiet') if len(p['links']) > 1 else ''}
      </article>"""


def build_index():
    cards = "".join(card(BY[i]) for i in ["debateledger", "wmbxl", "dnmopd", "tlvc"])
    also_ids = ["dafnycomp", "reform", "simd2nn", "robustmad", "graphreduce", "livecann"]
    also = "".join(f"""
        <li><a class="also__name" href="{e(BY[i]['links'][0][1])}">{e(BY[i]['short'])}</a><span class="also__t">{e(subtitle(BY[i]))}</span><span class="also__v">{e(vshort(BY[i]))}</span></li>"""
                   for i in also_ids)
    recent = news_items(NEWS[:5])
    body = f"""
  <header class="hero wrap">
    <div class="hero__text">
      <p class="kicker">Ph.D. student · Nanyang Technological University · advised by <a href="https://blogs.ntu.edu.sg/chau-yuen/">Prof. Chau Yuen</a></p>
      <h1 class="name">Xin Li<span class="name__cjk" lang="zh-Hans">李鑫</span></h1>
      <p class="lede">{e(LEDE)}</p>
    </div>
    <img class="hero__photo" src="/data/avatar-560.webp" width="560" height="560" alt="Portrait of Xin Li" fetchpriority="high">
  </header>
{loop_html()}
  <section class="results wrap" aria-labelledby="res-h">
    <h2 id="res-h" class="label"><span>Selected results</span><span class="label__aside">2026</span></h2>
    <div class="cards">{cards}
    </div>
  </section>

  <section class="also wrap" aria-labelledby="also-h">
    <h2 id="also-h" class="label"><span>Also in 2026</span><a class="label__aside" href="publications.html">All publications →</a></h2>
    <ul class="also__list">{also}
    </ul>
  </section>

  <section class="recent wrap" aria-labelledby="recent-h">
    <h2 id="recent-h" class="label"><span>Recent</span><a class="label__aside" href="news.html">All news →</a></h2>
    <ol class="recent__list">{recent}</ol>
  </section>

  <section class="coda wrap">
    <div>
      <h2 class="label"><span>Before the Ph.D.</span></h2>
      <p>Robot perception — visual-inertial odometry at MEGVII, RGB-D + IMU indoor mapping at Microsoft Research Asia,
        and multimodal localization at Gausium Robotics, where I led a five-engineer team and shipped to a fleet of
        <b>1,000+</b> commercial cleaning robots. <a href="about.html">More →</a></p>
    </div>
    <div>
      <h2 class="label"><span>Contact</span></h2>
      <p>Looking for research internships in 2027, and always glad to talk about research or collaboration.</p>
      <p class="links links--plain"><a href="mailto:xin019@e.ntu.edu.sg">xin019@e.ntu.edu.sg</a><a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ">Scholar</a><a href="https://github.com/LiXin97">GitHub</a><a href="https://www.linkedin.com/in/xin-li-1196331a0/">LinkedIn</a><a href="/data/Xin_Li_CV_2026.pdf">CV</a></p>
    </div>
  </section>"""
    return page("home", "Xin Li — Evaluate, Train, Orchestrate",
                body, DESC)


# ---------------------------------------------------------------- thread pages
def work(p, open_fig=True):
    t = TH.get(p["thread"])
    claim = f'<p class="work__claim">{e(p["claim"])}</p>' if p["claim"] else ""
    scope = f'<p class="scope"><b>Scope</b> {e(p["scope"])}</p>' if p["scope"] else ""
    lead = " is-lead" if p["pos"].startswith(("first", "joint first")) else ""
    return f"""
      <article class="work" id="{p['id']}">
        <div class="work__side">
          <p class="work__venue">{venue_pill(p)}</p>
        </div>
        <div class="work__main">
          <h3 class="work__title"><a href="{e(p['links'][0][1])}">{e(p['title'])}</a></h3>
          <p class="work__authors">{authors_html(p['authors'])}</p>
          {claim}
          {scope}
          {links_html(p['links'])}
        </div>
      </article>"""


def build_thread(t):
    i = [x["id"] for x in THREADS].index(t["id"])
    prev_t, next_t = THREADS[i - 1], THREADS[(i + 1) % 3]
    prev_note = "the return leg arrives here" if t["id"] == "evaluate" else "previous"
    next_note = "back to 01 — the return leg" if t["id"] == "orchestrate" else "next"
    works = "".join(work(BY[w]) for w in t["works"])
    also = ""
    if t["also"]:
        also = '<section class="thread-also wrap"><h2 class="label"><span>Also on this thread</span></h2><ul>' + "".join(
            f'<li><a href="{e(u)}">{e(n)}</a> <span>{e(d)}</span></li>' for n, u, d in t["also"]) + "</ul></section>"
    steps = "".join(
        f'<a href="{x["id"]}.html"{" aria-current=\"step\"" if x["id"] == t["id"] else ""}><span>{x["n"]}</span>{x["verb"]}</a>'
        for x in THREADS)
    body = f"""
  <header class="thread-head wrap">
    <nav class="steps" aria-label="The loop">{steps}<span class="steps__ret" aria-hidden="true">↺</span></nav>
    <p class="thread-n">{t['n']} / 03</p>
    <h1 class="thread-verb">{t['verb']}</h1>
    <p class="thread-q">{e(t['q'])}</p>
    <p class="thread-desc">{e(t['desc'])}</p>
  </header>
  <section class="works-sec wrap" aria-labelledby="works-h">
    <h2 id="works-h" class="label"><span>Work on this thread</span><span class="label__aside">{len(t['works'])} papers</span></h2>
    <div class="works">{works}
    </div>
  </section>
  {also}
  <nav class="pager wrap" aria-label="Through the loop">
    <a class="pager__prev" href="{prev_t['id']}.html"><span>← {e(prev_note)}</span><b>{prev_t['n']} {prev_t['verb']}</b></a>
    <a class="pager__next" href="{next_t['id']}.html"><span>{e(next_note)} →</span><b>{next_t['n']} {next_t['verb']}</b></a>
  </nav>"""
    return page(t["id"], f"{t['verb']} — Xin Li", body, t["q"])


# ---------------------------------------------------------------- publications
LABEL = {"evaluate": "01 Evaluate", "train": "02 Train", "orchestrate": "03 Orchestrate",
         "wireless": "Wireless systems", "robotics": "Robot perception"}


def pub(p):
    lead = " is-lead" if p["pos"].startswith(("first", "joint first")) else ""
    return f"""
      <li class="pub" data-thread="{p['thread']}">
        <div class="pub__top"><h3 class="pub__title"><a href="{e(p['links'][0][1])}">{e(p['title'])}</a></h3>{venue_pill(p)}</div>
        <p class="pub__authors">{authors_html(p['authors'])}</p>
        <p class="pub__meta"><span class="pub__thread">{e(LABEL[p['thread']])}</span></p>
        {links_html(p['links'], 'links links--quiet')}
      </li>"""


ORDINAL = {w: i for i, w in enumerate(("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"), 1)}
MAIN_TRACK = ("NeurIPS", "ICLR", "ICML", "ACL", "EMNLP", "NAACL")


def pub_rank(p):
    """Order within a year: papers Xin leads (first or joint first) before co-authored ones; then main-track
    NeurIPS/ICLR/ICML/ACL/EMNLP/NAACL, other conferences, Findings and journals, workshops (preprints have their
    own group, see build_pubs); then
    sole first author before joint first, earlier author position first. Ties keep their order in P."""
    v, pos = p["venue_long"], p["pos"]
    if v.startswith("arXiv"):
        tier = 3
    elif "workshop" in v.lower():
        tier = 2
    elif v.startswith(MAIN_TRACK) and "Industry" not in v:
        tier = 0
    else:
        tier = 1
    joint = pos.startswith("joint")
    n = ORDINAL.get(pos.removeprefix("joint ").split()[0], 99)
    return (n != 1, tier, n, joint)


def is_preprint(p):
    return p["venue_long"].startswith("arXiv")


def build_pubs():
    """Preprints first, in their own group (newest work, kept apart from what has been reviewed); then each year.
    A preprint moves into its year by itself once its venue is filled in."""
    groups = []
    sections = [("Preprints", sorted((p for p in P if is_preprint(p)), key=lambda p: (-p["year"], pub_rank(p))))]
    sections += [(y, sorted((p for p in P if p["year"] == y and not is_preprint(p)), key=pub_rank)) for y in (2026, 2025, 2020)]
    for head, papers in sections:
        if papers:
            groups.append(f'<section class="year"><h2 class="year__h">{head}</h2><ol class="pubs">{"".join(pub(p) for p in papers)}</ol></section>')
    filters = "".join(f'<button type="button" data-f="{k}" aria-pressed="{"true" if k == "all" else "false"}">{v}</button>'
                      for k, v in [("all", "All"), ("evaluate", "Evaluate"), ("train", "Train"), ("orchestrate", "Orchestrate"),
                                   ("wireless", "Wireless"), ("robotics", "Robotics")])
    body = f"""
  <header class="plain-head wrap">
    <h1 class="plain-h1">Publications</h1>
    <p class="plain-sub"><sup>*</sup> equal contribution. Also on
      <a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ">Google Scholar</a>.</p>
    <div class="filter" role="group" aria-label="Filter by thread">{filters}</div>
  </header>
  <div class="wrap pubs-wrap">{"".join(groups)}
    <p class="pubs-note">Also: <i>Onboard Terrain Classification via SIM-DNN</i>, ML4RS workshop @ ICLR 2025 — extended into the IEEE TSP paper above.</p>
  </div>"""
    return page("pubs", "Publications — Xin Li", body, "Complete publication record of Xin Li.")


# ---------------------------------------------------------------- news
def news_items(items, month_only=False):
    return "".join(f'<li><time>{e(d.split()[0] if month_only else d)}</time><span>{t}</span></li>' for d, t in items)


def build_news():
    years = sorted({d.split()[1] for d, _ in NEWS}, reverse=True)
    groups = "".join(
        f'<section class="year"><h2 class="year__h">{y}</h2>'
        f'<ol class="recent__list news-list">{news_items([n for n in NEWS if n[0].endswith(y)], month_only=True)}</ol></section>'
        for y in years)
    body = f"""
  <header class="plain-head wrap">
    <h1 class="plain-h1">News</h1>
    <p class="plain-sub">Since starting the Ph.D. in January 2025. Papers in full are on the <a href="publications.html">publications</a> page.</p>
  </header>
  <div class="wrap pubs-wrap">{groups}
  </div>"""
    return page("news", "News — Xin Li", body, "News from Xin Li: paper acceptances, awards and other updates since 2025.")


# ---------------------------------------------------------------- about
def rows(items):
    return "".join(f'<div class="row"><p class="row__k">{k}</p><div class="row__v">{v}</div></div>' for k, v in items)


def build_about():
    exp = rows([
        ("Apr 2024 – Jan 2025", "<b>Research Assistant</b>, NTU Singapore. Supervised by Chau Yuen. Built WirelessMathBench and TransPathNet."),
        ("Mar 2022 – Feb 2024", "<b>SLAM Algorithm Engineer, Project Lead</b>, Gausium Robotics, Singapore. Led five engineers on hierarchical "
                                "multimodal localization — vision, LiDAR, Wi-Fi — for commercial cleaning robots: 95% localization accuracy "
                                "across 100,000+ m², deployed on a fleet of 1,000+ active robots."),
        ("Sep 2020 – Mar 2021", "<b>Research Intern</b>, Microsoft Research Asia, Beijing. With Dr. Yang Liu and Dr. Yizhong Zhang. "
                                "RGB-D + IMU fusion for large-scale indoor mapping; vectorized maps of 10,000+ m² at sub-meter accuracy."),
        ("Feb 2019 – Mar 2020", "<b>Research Intern</b>, MEGVII, Beijing. With Dr. Yijia He. Real-time monocular visual-inertial "
                                "odometry; semi-dense 3D mesh reconstruction at 30+ FPS."),
    ])
    edu = rows([
        ("2025 – 2029 (expected)", "<b>Ph.D.</b>, Nanyang Technological University, Singapore. Advised by Prof. Chau Yuen."),
        ("2018 – 2021", "<b>M.E.</b>, Peking University. Advised by Prof. Jinlong Lin."),
        ("2014 – 2018", "<b>B.E.</b>, Northeastern University, China."),
    ])
    grants = rows([
        ("2026", "<b>Google Gemini Academic Program Award</b> — US$10,000"),
        ("2025", "<b>Modal Academics Compute Grant</b> — US$2,000"),
        ("2025", "<b>Cohere Labs Catalyst Grant</b> — US$1,500"),
        ("2025", "<b>OpenAI Researcher Access Program</b> — US$1,000"),
        ("2025", "<b>Rohde &amp; Schwarz Award</b>, IEEE 6G Summit Singapore"),
        ("2025", "<b>PREMIA Best Student Paper Award</b>, finalist"),
        ("2025", "<b>NTU Research Scholarship</b>, full Ph.D. funding"),
    ])
    service = rows([
        ("Reviewer", "NeurIPS, ICLR, ICML, AAAI, CVPR, ECCV, AISTATS, SIGGRAPH, IROS, ICRA · IEEE RA-L, ACM TOG, IEEE TNNLS"),
        ("Organizer", '<a href="https://4drobotics-iros2025.github.io/">AIR4D</a> workshop @ IROS 2025'),
    ])
    talks = rows([
        ("Oct 2025", "<b>Teaching Large Language Models Mathematical Reasoning in Wireless Communications: From Benchmarking "
                     "to Efficient Training</b> — ISEE Youth Scholar Forum, School of Information and Electronic Engineering, "
                     "Zhejiang University"),
        ("Jul 2025", '<b>WirelessMathBench</b> — ACL 2025 (<a href="/data/talk_slides/ACL_WirelessMathBench_Slides.pdf">slides</a>)'),
        ("Jun 2025", '<b>WirelessMathBench: A Mathematical Modeling Benchmark for LLMs in Wireless Communications</b> — '
                     'NICE Session 66, Evaluation Paper Sharing @ ICML &amp; ACL 2025 '
                     '(<a href="/data/talk_slides/WirelessMath_Slides.pdf">slides</a>)'),
    ])
    mentoring = rows([
        ("2026", '<b>Chengqi Liang</b> — M.Sc. dissertation, Nanyang Technological University. '
                 'Went on to a Ph.D. at <a href="https://www.cuhk.edu.cn/">The Chinese University of Hong Kong, Shenzhen</a>.'),
        ("2026", '<b>Yukun Jin</b> — B.Eng. final-year project, Nanyang Technological University. An undergraduate at '
                 '<a href="https://www.whu.edu.cn/">Wuhan University</a> on NTU\'s 3.5+0.5+1 integrated programme; '
                 'went on to an M.Sc. at NTU.'),
        ("2024", '<b>Haoyu Xu</b> — M.Comp. dissertation, <a href="https://www.nus.edu.sg/">National University of Singapore</a>. '
                 'Went on to a Ph.D. at <a href="https://www.pku.edu.cn/">Peking University</a>.'),
    ])
    body = f"""
  <header class="plain-head wrap about-head">
    <img class="portrait" src="/data/avatar-280.webp" width="280" height="280" alt="Portrait of Xin Li">
    <div>
      <h1 class="plain-h1">About</h1>
      <p class="about-bio">I am a Ph.D. student at Nanyang Technological University (NTU), advised by
        <a href="https://blogs.ntu.edu.sg/chau-yuen/">Prof. Chau Yuen</a>. I work on LLM agents: benchmarks that evaluate what
        they can do, training that improves them, and orchestration that gets real tasks done with tools, verifiers
        and other agents — and, lately,
        agents that improve themselves. So far most of the work has been in domains where an answer can be checked:
        formal verification, mathematics, and code. The current work is on self-improvement beyond checkable answers.</p>
      <p class="about-bio">Before my Ph.D. I worked on robot perception — visual-inertial odometry at MEGVII, RGB-D + IMU
        indoor mapping at Microsoft Research Asia, and multimodal localization at Gausium Robotics, where I led a
        five-engineer team and shipped to a fleet of 1,000+ commercial cleaning robots.</p>
      <p class="links links--plain"><a href="mailto:xin019@e.ntu.edu.sg">xin019@e.ntu.edu.sg</a><a href="/data/Xin_Li_CV_2026.pdf">CV (PDF)</a><a href="https://scholar.google.com/citations?user=Hxf8sNkAAAAJ">Scholar</a><a href="https://github.com/LiXin97">GitHub</a><a href="https://www.linkedin.com/in/xin-li-1196331a0/">LinkedIn</a></p>
    </div>
  </header>
  <div class="wrap about-body">
    <section id="experience"><h2 class="label"><span>Experience</span></h2>{exp}</section>
    <section id="education"><h2 class="label"><span>Education</span></h2>{edu}</section>
    <section id="awards"><h2 class="label"><span>Grants &amp; awards</span></h2>{grants}</section>
    <section id="mentoring"><h2 class="label"><span>Mentoring</span></h2>{mentoring}</section>
    <section id="talks"><h2 class="label"><span>Talks</span></h2>{talks}</section>
    <section id="service"><h2 class="label"><span>Service</span></h2>{service}</section>
  </div>"""
    return page("about", "About — Xin Li", body, "About Xin Li: experience, education, grants, mentoring, talks and service.")

FEATURED = {"evaluate": ["wmbxl"], "train": ["dnmopd"], "orchestrate": ["debateledger", "tlvc"]}


def also_names(t):
    """The rest of a thread's work, by name, pointing at its page."""
    rest = [w for w in t["works"] if w not in FEATURED[t["id"]]]
    if not rest:
        return ""
    names = " · ".join(e(BY[w]["short"]) for w in rest)
    return f'<p class="also-names"><a href="{t["id"]}.html">Also: {names} →</a></p>'


def readings():
    out = []
    for i in ["debateledger", "wmbxl", "dnmopd", "tlvc"]:
        p = BY[i]; t = TH[p["thread"]]; n, lbl, neg = p["fig"]
        out.append(f"""
        <a class="reading" href="{e(p['links'][0][1])}">
          <span class="reading__tag">{t['n']} · {t['verb']}</span>
          <span class="reading__fig{' is-neg' if neg else ''}">{e(n)}</span>
          <span class="reading__lbl">{e(lbl)}</span>
          <span class="reading__name">{e(p['short'])}</span>
          <span class="reading__v">{e(vshort(p))}</span>
        </a>""")
    return "".join(out)


# ---------------------------------------------------------------- ring
def build_ring():
    T = TH
    ground = "".join(f"<span>{e(g)}</span>" for g in GROUND)
    body = hero_block() + f"""
  <section class="ring wrap" aria-labelledby="loop-h">
    <h2 id="loop-h" class="label"><span>The research, as one loop</span><span class="label__aside">clockwise from 01</span></h2>
    <div class="ring__stage">
      {thread_label(T['evaluate'], 'tl')}
      <div class="ring__orbit">
        <div class="ring__fig">{ring_svg()}{ring_center()}</div>
        {thread_label(T['train'], 'tl')}
        {thread_label(T['orchestrate'], 'tl')}
      </div>
    </div>
    <p class="ring__return"><span aria-hidden="true">↺</span> <b>03 → 01.</b> {e(RETURN)}</p>
  </section>
  <section class="readings wrap" aria-labelledby="rd-h">
    <h2 id="rd-h" class="label"><span>Selected results</span><span class="label__aside">2026</span></h2>
    <div class="readings__row">{readings()}
    </div>
  </section>""" + tail_sections()
    return page("ring", "Xin Li — the loop", body, DESC, home="ring.html")


# ---------------------------------------------------------------- track
def build_track():
    panels = []
    for k, t in enumerate(THREADS):
        names = "".join(
            f'<li class="panel__lead"><a href="{e(BY[w]["links"][0][1])}">{e(BY[w]["short"])}</a>'
            f'<p class="panel__blurb">{e(BY[w]["blurb"])}</p><p class="panel__venue">{e(vshort(BY[w]))}</p></li>'
            if BY[w].get("blurb") else
            f'<li class="panel__lead panel__lead--short"><a href="{e(BY[w]["links"][0][1])}" title="{e(BY[w]["title"])}">'
            f'{e(BY[w]["short"])}</a><p class="panel__venue">{e(vshort(BY[w]))}</p></li>'
            for w in t["works"])
        panels.append(f"""
      <article class="panel panel--{t['id']}">
        <p class="panel__n">{t['n']}</p>
        <h3 class="panel__verb"><a href="{t['id']}.html">{t['verb']}</a></h3>
        <p class="panel__q">{e(t['q'])}</p>
        <ul class="panel__works" aria-label="Papers on this thread">{names}</ul>
      </article>""")
        if k < 2:
            panels.append('<span class="track__link" aria-hidden="true"><i></i></span>')
    ground = "".join(f"<span>{e(g)}</span>" for g in GROUND)
    body = hero_block() + f"""
  <section class="track wrap" aria-labelledby="loop-h">
    <h2 id="loop-h" class="label"><span>The research, as one loop</span><span class="label__aside">clockwise from 01</span></h2>
    <div class="track__row">{"".join(panels)}
    </div>
    <div class="track__return"><span class="track__rail" aria-hidden="true"></span>
      <p><b>03 → 01.</b> {e(RETURN)}</p></div>
    <p class="track__ground"><span class="track__ground-k">{e(GROUND_K)}</span>{ground}<span class="track__now">{e(GROUND_NOW)}</span></p>
  </section>""" + tail_sections(also_list=False)
    return page("track", HOME_TITLE if PROD else "Xin Li — the loop", body, DESC, home="track.html", canon="")


# ---------------------------------------------------------------- scroll
def build_scroll():
    steps = []
    for t in THREADS:
        ev = "".join(evidence(BY[i]) for i in FEATURED[t["id"]])
        steps.append(f"""
      <section class="step" data-step="{t['id']}" aria-labelledby="st-{t['id']}">
        <p class="step__n">{t['n']} / 03</p>
        <h3 class="step__verb" id="st-{t['id']}"><a href="{t['id']}.html">{t['verb']}</a></h3>
        <p class="step__q">{e(t['q'])}</p>
        <p class="step__d">{e(t['desc'])}</p>
        <div class="step__ev">{ev}</div>
        {also_names(t)}
      </section>""")
    steps.append(f"""
      <section class="step step--return" data-step="return" aria-labelledby="st-return">
        <p class="step__n">03 → 01</p>
        <h3 class="step__verb" id="st-return">Back to Evaluate</h3>
        <p class="step__q">{e(RETURN)}</p>
      </section>
      <section class="step step--now" data-step="now" aria-labelledby="st-now">
        <p class="step__n">So far → now</p>
        <h3 class="step__verb" id="st-now">The loop, run by the agent</h3>
        <p class="step__q">{e(GROUND_K)} {e(", ".join(GROUND))}. {e(GROUND_NOW)}</p>
      </section>""")
    body = f"""
  <header class="hero hero--tall wrap">
    <div class="hero__text">
      <p class="kicker">Ph.D. student · Nanyang Technological University · advised by <a href="https://blogs.ntu.edu.sg/chau-yuen/">Prof. Chau Yuen</a></p>
      <h1 class="name">Xin Li<span class="name__cjk" lang="zh-Hans">李鑫</span></h1>
      <p class="lede">{e(LEDE)}</p>
      <p class="hero__cue" aria-hidden="true">The loop ↓</p>
    </div>
    <img class="hero__photo" src="/data/avatar-560.webp" width="560" height="560" alt="Portrait of Xin Li" fetchpriority="high">
  </header>
  <div class="scrolly wrap" data-step="all">
    <h2 class="sr-only">The research, as one loop</h2>
    <div class="scrolly__fig"><div class="ring__fig">{ring_svg()}{ring_center()}</div></div>
    <div class="scrolly__steps">{"".join(steps)}
    </div>
  </div>""" + tail_sections()
    return page("scroll", "Xin Li — the loop", body, DESC, home="scroll.html",
                extra_js='<script src="js/scrolly.js" defer></script>')


# ---------------------------------------------------------------- write
pages = {"index.html": build_index(), "publications.html": build_pubs(), "news.html": build_news(), "about.html": build_about(),
         "ring.html": build_ring(), "track.html": build_track(), "scroll.html": build_scroll()}
for t in THREADS:
    pages[f"{t['id']}.html"] = build_thread(t)
for name, html in pages.items():
    (OUT / name).write_text(html, encoding="utf-8")
    print(f"wrote {name}  {len(html):,} bytes")

# ---------------------------------------------------------------- production pass
PROD = True
prod = {"index.html": build_track(), "publications.html": build_pubs(), "news.html": build_news(), "about.html": build_about()}
for t in THREADS:
    prod[f"{t['id']}.html"] = build_thread(t)
(ROOT / "assets").mkdir(exist_ok=True)
(ROOT / "assets" / "site.css").write_text(
    "/* Generated by _styles/v5/_build.py: base.css + paper.css + present.css. Edit those, then rerun it. */\n"
    + "\n".join((OUT / "css" / f).read_text() for f in ("base.css", "paper.css", "present.css")), encoding="utf-8")
for f in ("filter.js", "mode.js"):
    (ROOT / "assets" / f).write_text((OUT / "js" / f).read_text(), encoding="utf-8")
for name, html in prod.items():
    (ROOT / name).write_text(html, encoding="utf-8")
    print(f"wrote /{name}  {len(html):,} bytes")

# Pages renamed since they went public; GitHub Pages has no server redirects, so each old URL is a stub.
MOVED = {"coordinate.html": ("orchestrate.html", "Orchestrate"), "measure.html": ("evaluate.html", "Evaluate")}
for old, (new, title) in MOVED.items():
    (ROOT / old).write_text(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} — Xin Li</title>
<link rel="canonical" href="{SITE}{new}">
<meta name="robots" content="noindex">
<meta http-equiv="refresh" content="0; url=/{new}">
<script>location.replace('/{new}' + location.hash);</script>
</head>
<body><p>This page is now <a href="/{new}">{title}</a>.</p></body>
</html>
""", encoding="utf-8")
    print(f"wrote /{old} -> /{new}")
