# Redesign brief — lixin.ai

You are building ONE complete redesign of Xin Li's academic homepage, as a single
standalone HTML file. Another agent is building a different direction from the same
brief; do not try to cover every direction yourself. Commit to yours.

## Where the content comes from

Read `/home/xin/Projects/LiXin97.github.io/index.html`. Every publication, author
list, venue, link, date, award and experience entry you need is in there, already
correct. **Use it verbatim.** Do not invent papers, numbers, venues, co-authors or
dates. Do not write placeholder text. If you want to say something the record does
not support, leave it out.

Portrait: `/data/avatar-280.webp` (280x280). It is the only photo. There are also
`/data/figs/debateledger.webp` and `/data/figs/dn-mopd.webp` (paper figures) —
**do not use them.** The decision has been made not to put paper figures on this page.

## Verified numbers you may use for one-line claims

Only these. Anything else, read it out of index.html or omit it.

- **DebateLedger** (Measuring Collapse and Correction in Homogeneous-Panel LLM Debate,
  NeurIPS 2026): 6,925 MMLU-Pro debates logged; 253 collapses; a probe-gated freeze
  prevents 29 collapses but gives up 108 corrections, net -79 under equal weights;
  58.9% of collapses begin in the first debate round.
- **WirelessMathBench-XL** (NeurIPS 2026): 4,027 problems drawn from 836 arXiv papers
  across 20 wireless subfields; ships per-problem 13-gram contamination-overlap
  evidence against public pretraining text; frontier models cluster at 86.5-91.3%.
- **DN-MOPD** (arXiv 2026): normalizing each teacher's feedback scale per domain adds
  1.2-3.1 points over label routing, across 2B, 4B and 9B students.
- **SIM-D2NN** (IEEE TSP 2026): ~90% accuracy classifying terrain directly from SAR
  Level-0 raw data, with the metasurface doing the inference in-wave.
- **TransPathNet** (ICASSP 2025): placed 4th in the Indoor Pathloss Prediction Challenge.
- **Gausium Robotics**: led a team of five engineers; 95% localization accuracy across
  100,000+ m2; deployed on a fleet of 1,000+ commercial cleaning robots.

Careful: WirelessMathBench-XL's contamination result was deliberately scoped during
review. It is "a rerunnable audit that produces per-problem evidence for one lexical
channel", NOT "proof the benchmark is clean". Do not overstate it.

## What the research says (3 surveys, 42 pages read)

Survey A — 21 frontier-lab and widely-admired researchers (Schulman, Shunyu Yao,
Jason Wei, Noam Brown, Leike, Perez, Olah, Weng, Nanda, Horace He, Elhage, Denny Zhou,
Karpathy, Liang, Hashimoto, Steinhardt, Tri Dao, Danqi Chen...):

- 19/21 are deliberately plain. Stylesheets: Elhage 322 bytes, Liang 416 bytes.
- **Scroll-spy nav: 0/21. Pinned left rail: 1/21. Dark mode: 3/21.**
- Any image beyond a portrait: 5/21. No image at all: 5/21.
- 8 of 13 lab researchers list NO publications on the homepage.
- 0 of 13 lab pages have a news feed, an awards block, a teaching section, or an
  education paragraph.
- What separates authoritative from generic: (a) the bio names artifacts, not roles
  -- Horace He literally heads that block "Why you might know me."; (b) papers are
  presented as claims, not citations; (c) ruthless subtraction; (d) a stated point of
  view -- a question and a bet, not a keyword list.
- Caveat the survey itself raises: a PhD student must NOT copy "no publications at
  all". That works when o1 and ChatGPT are on your CV. From a student it reads as an
  empty page. Keep the record visible.

Survey B — 21 peer PhD students in LLM eval / agents / post-training:

- Median page: single column, one portrait, 1-2 sections, a "Selected" tier,
  reverse-chronological, no thumbnails, no stated ask.
- Only 7/21 have a news section at all; 4/13 among current students.
- Paper thumbnails: 3/21, and all three cap the figured tier at 4-5 items.
- Strongest pages (zhangyuanhan-ai.github.io, kenqgu.com, jiayipan.com, xuhuiz.com):
  every featured item carries **a one-line result with a number**, e.g.
  "Gemini-3.1-Pro scores 56.3% vs. 84.4% for humans", "1.2M+ HuggingFace downloads".
  All three surveys independently called this the highest-leverage change.
- Career pivots are never hidden; they are compressed to one sentence and placed
  after the current research.
- Xin's current page runs NINE sections. Nobody in either survey runs nine.

Survey C — structure and screening:

- Anthropic states "We don't currently offer internships"; their early-career route
  is Fellows, AI-safety scoped. Meta intern postings name "first-authored
  publications" at NeurIPS/ICLR/ACL etc. Only 2/13 peer students state an ask, and
  one is expired ("summer ( 2025 )" on a page dated 2026) which reads as neglect.
- NN/g: "The first two paragraphs must state the most important information."
- A benchmark paper with only a Paper link reads as a paper; one with dataset,
  code and leaderboard links reads as infrastructure other people use.

## Hard constraints for the file you write

1. **One self-contained HTML file.** Inline `<style>`. Google Fonts via `<link>` is
   fine. No build step, no framework, no external JS libraries.
2. **No paper figures.** The portrait is the only photo you may use.
3. **Real content only**, taken from index.html. No lorem, no invented numbers.
4. **Responsive.** No horizontal overflow at 390px. Verify this.
5. **Accessible.** One `<h1>`; heading order with no skips; `alt` on the portrait;
   visible `:focus-visible`; colour contrast at least 4.5:1 for body text.
6. **Light theme is required and is the default.** Dark mode is optional; if you
   include it, it must be correct in both, with `color-scheme` declared.
7. Keep it under ~45 KB of HTML.
8. **Verify your own work before you finish.** A local server already serves the repo
   root at http://127.0.0.1:8000/ . Screenshot your page with:
   `google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars
    --window-size=1280,1800 --virtual-time-budget=9000 --screenshot=OUT.png URL`
   Then READ the png with the Read tool and fix what looks wrong. Iterate at least
   twice. Also screenshot at 420px wide to check the narrow layout. A page you never
   looked at will be rejected.

## The research roadmap

Xin's three threads are a loop, and he wants this shown. Content, agreed with him:

- **01 Measure** — "Does a score mean what it appears to mean, and would we notice if
  it didn't?" — WirelessMathBench-XL, DafnyComp, RobustMAD
- **02 Train** — "Can we reward the reasoning we are able to check, rather than the
  answer we hope for?" — Re:Form, DN-MOPD, TLVC
- **03 Compose** — "When several models work together, does the interaction help, or
  quietly destroy answers that were already right?" — DebateLedger, LACP
- the return leg: composition creates new failure modes, which have to be measured too
- the ground: formal verification, mathematics, code, wireless systems

Whether you render this as a diagram, as three columns of prose, as a numbered
paragraph, or leave it out entirely is YOUR call and depends on your direction. If you
draw it, draw it in HTML/CSS/SVG with real selectable text -- never an image. A working
reference implementation is at `_styles/roadmap.html` (dark panel, animated pulse);
you may borrow from it, simplify it, or ignore it.

## Things the evidence says to drop, unless your direction argues otherwise

- the pinned left rail and the scroll-spy nav (0/21 and 1/21)
- nine separate sections; Mentoring, Talks, Education and Service as standalone blocks
- a 15-item news list
- the line "I'm looking for research internships for 2027" as currently worded

## Deliverable

Write exactly one file at the path you are given. Then reply with: the path, the
design thesis in two sentences, what you deliberately cut, and anything you were
unsure about. Do not modify index.html or any other existing file.

---

## ADDENDUM (verified after the first four directions were built)

Two papers that index.html mentions only in the news list now have full records.
Any further work on these pages must use these, not guesses.

### TLVC — first author, belongs in a Selected tier
- Title: **Target-Local Verifier Choice in Best-of-K Reasoning Selection**
- Authors: **Xin Li**, Hao Jiang, Weisi Lin  (Xin Li is first author of three)
- Venue: Findings of EMNLP 2026
- Links: project https://lixin.ai/TLVC/ · code https://github.com/LiXin97/TLVC
  · PDF https://lixin.ai/TLVC/paper.pdf
- **No arXiv link.** The project page currently shows the placeholder
  `https://arxiv.org/abs/XXXX.XXXXX`, which 404s. Do not reproduce it anywhere.
- Usable claim, from the project page's own description: one strong process reward
  model is the best fixed verifier across a **34-generator, 7-verifier** Best-of-K
  math panel, but not the best verifier for every generator; label-free candidate
  statistics predict which verifier class wins, and budgeted policies beat the
  fixed choice.

### LiveCANNBench — middle author, belongs in the full record only
- Title: **LiveCANNBench: Benchmark SWE AI Coding for Ascend CANN**
- Authors: Sijie Wang, Kai Zhao, Wee Peng Tay, Shuo Zhang, Chengwen Liu,
  Quanjiang Guo, Ren Junhao, **Xin Li**, Heng Lian, Jingdi Lei, Rui She,
  Huacan Wang, Ronghao Chen  — Xin Li is **8th of 13**.
- Venue: Findings of ACL 2026, pages 22788-22803
- Links: https://aclanthology.org/2026.findings-acl.1143/
  · PDF https://aclanthology.org/2026.findings-acl.1143.pdf
  · DOI 10.18653/v1/2026.findings-acl.1143
- Content: 400+ SWE-level task instances built from real CANN repositories,
  multi-file / multi-language / execution-aware, on a live benchmarking paradigm
  that mitigates data leakage.
- Because Xin is a middle author of thirteen, this does NOT go in a selected tier.
  It belongs in the complete list, where the venue still counts.
