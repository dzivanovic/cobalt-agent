# Layered typed decisions in any domain — third pass (2026-09-21)

Seat `typed-decisions-broad-0921` · Sonnet 5 · prompt `prompts/2026-09-21/48-research-typed-decisions-broad.md` · ordered by Dejan, `cto-2026-09-21.md` R31 / R34 / R35. LADDER: OFF-LADDER. INPUT to the four-house tribunal after S2. It proposes no design, builds nothing, ran nothing: no sign-up, key, install, or call to the vendor.

**How to read the evidence.** Every fetch went through a small summarising model. **Q** = a quotation the fetch tool returned inside quotation marks (≤25 words). **S** = the tool's own summary line, no quotation marks. **SS** = a search-result summary of a page NOT fetched (weakest). A house relying on a figure re-opens the URL first (L35). NOT FOUND = looked for, absent. NOT KNOWN = nobody has published it. `E<n>` = an example in §1, `R<n>` = a rule in §2, `T<n>` = a transposition in §4. Builds on the first two passes (`TYPESAFE-CLASSIFIER-RESEARCH-2026-09-21.md`, `…-DEEP-…`): their 27 rows are cited as "row n"; nothing in them is repeated.

---

## §0 One page

**Answer.** Every field that makes complex selections fast and defensible builds the same way: many small closed questions, asked cheaply, gated early, and combined by a written table into a score, a band or a route. The model (or the nurse, or the referee) answers; the table decides; the record of answers is the explanation.

**The five patterns most worth stealing, and where each lands**
1. **Scorecard: bucket, points, sum, reason codes.** Credit scoring turns each characteristic into a bin, each bin into points, sums in code, and explains a decline by "points lost against the best possible answer" (E7); the clinical Wells rule is seven items with points and three bands (E2). Lands: **his trade-grade (T1)**.
2. **Cascade: deterministic first, model only on the residue.** DoorDash cleared "90%+ of traffic" with a sub-100-ms classifier before any LLM (E3); a SOC pipeline closed 3 of 4 incidents at "$0.00" before the model ran (E9). Lands: news/X triage (T2), catalyst labels (T3).
3. **Gate, then check; when unsure the default stands.** ESI asks "is this patient unstable" before anything else (E1); the VAR only reviews four incident kinds and "the original decision … will not be changed unless" the error is clear (E19); a fault-isolation tree ends in replace / no fault found / escalate (E16). Lands: T1 gates, T7 deterministic overrides.
4. **Checklist of yes/no items graded by a small model, weights in code.** TICK and RocketEval decompose a judgment into yes/no items (E22, E23); the WHO surgical checklist is 19 items at three pause points (E17). Lands: journaling and rule-adherence proposals (T4), T1.
5. **Split fact from judgment; keep a human-only leaf.** The VAR routes factual calls to a video-only check and subjective ones to the referee (E19); Wells flags its one subjective item (E2); a scout's overall grade "is not a formula" (E20). Lands: the tape read stays his (L11) inside T1.

**Added 16:07 ET (R37): §6A** — the three question types (Choice, Score, Noul), what "confidence" is for each (absent for Noul), how layered calls combine, and how Cobalt must account for it.

**Speed in one breath (§3).** Published latency for this class is thin: one vendor cookbook shows 13 questions in one call at 0.27 s against 2.71 s sequential; one integrator measured p50 126.81 ms / p95 231.16 ms on a single-choice router; nobody has published a 20–30-question tree. The trial must measure it.

---

## §1 Pattern library by domain

**Answer.** Eleven domains, 23 examples; three domains are thin (aviation is second-hand, legal has a protocol but no verified results, admissions was not separately found). Everywhere the tree is small closed questions plus a written combiner; where the combining happens inside a head or a model, the sources report low agreement (see R3).

### 1.1 Emergency / clinical triage and decision rules
**E1 — Emergency Severity Index (ESI), nurse triage.** [primary study, 4 Swiss hospitals] https://pmc.ncbi.nlm.nih.gov/articles/PMC4551516/
- TREE/TYPES (S): "four decision points": A immediate life-saving intervention → B cannot safely wait → C resources needed → D vital signs. Five-level ordinal result. SS: "higher acuity patients will only require one or two decision points."
- COMBINE: no arithmetic; the first decision point that fires ends the tree (gate early). UNSURE: none in the tool; nurses simply mis-triage.
- MEASURE (S): 69 nurses, 30 standardized scenarios, overall accuracy 59.6 % (1,234/2,070), undertriage 26.8 %, overtriage 13.6 %. Q: "Overall, interrater reliability of triage nurses was 0.78 (Krippendorff's alpha)".
- WENT WRONG (S): lack of factual knowledge, rare situations, protocol variations, "case scenarios lacking sufficient clinical detail". Lesson: agreement between raters (0.78) is not accuracy (59.6 %).

**E2 — Wells rule, pulmonary embolism.** [reference article] https://en.wikipedia.org/wiki/Wells_score_(pulmonary_embolism)
- TREE/TYPES (S): 7 binary items with points 3, 3, 1.5, 1.5, 1.5, 1, 1 (signs of DVT; alternative diagnosis less likely; heart rate above a cut; recent immobilization/surgery; prior DVT/PE; hemoptysis; malignancy). One item is a bucketed number, one is a judgment.
- COMBINE (S): points summed; three bands 0–1 (3.6 % PE), 2–6 (20.5 %), >6 (66.7 %). Q: guides "the best method of investigation". A band triggers the next test, not the diagnosis.
- UNSURE/WENT WRONG: Q: the rule "includes subjective opinion (unlike e.g. Geneva score)" — the judgment item is named as a weak point. SS (not fetched): a two-tier cut at 4 also exists.
- NOT FOUND: the original derivation paper (cookie wall).

### 1.2 Content moderation / trust and safety
**E3 — DoorDash SafeChat.** [company write-up via a database summary] https://www.zenml.io/llmops-database/ai-powered-content-moderation-platform-for-real-time-marketplace-safety
- TREE (Q/S): tier 1 internal classifier, Q "under 100 milliseconds at the 90th percentile", passes ~10 %; tier 2 LLM scores severity axes (threat, profanity, sexual content). Q: LLM baseline "2-10 seconds per call" vs need for "sub-second response times".
- TYPES/COMBINE (Q): scores not labels — "Scores function as 'knobs' rather than 'flags,' enabling graduated responses, threshold adjustments without model retraining". Actions by severity: censor, block, cancel order. Whether thresholds sit in code: "not clearly specified" (S).
- SCALE: Q "4 million daily messages"; "over 90%" fewer LLM calls (S). MEASURE: Q "around 1,000 examples hit a sweet spot" for backtesting; Q "roughly 50% reduction in safety incidents driven by verbal abuse".
- WENT WRONG (Q): "nine retraining cycles to maintain effectiveness"; voice: "by the time speech was transcribed and analyzed, the recipient had already heard it".

**E4 — Trust-and-safety practice guide (second-hand).** [vendor blog, cites DoorDash, Pinterest, Bluesky] https://www.musubilabs.ai/blog/how-to-use-llms-for-content-moderation
- Q: "Build the golden set first. Build the metric you actually care about". Q: "Avoid asking the LLM to assess things it can't see, like intent, user history, off-platform behavior."
- Q: "Long policy documents degrade accuracy. If your policy is more than a few hundred words, consider splitting it." UNSURE: Q "Route the uncertain cases to humans and let the model handle the rest".
- MEASURE: Q "precision and recall at different decision thresholds, not just overall accuracy"; Q "A golden set frozen on day one becomes obsolete … Quarterly refreshes are a reasonable starting point." WENT WRONG: a policy change that helps one category and "quietly tanks precision on a related one".

### 1.3 Fraud and anti-money-laundering
**E5 — Real-time fraud decision engine.** [single-author blog; design targets, not measurements] https://dev.to/arjun_07/inside-a-real-time-ai-fraud-detection-engine-that-makes-decisions-in-under-50ms-4n1j
- TREE: Q "Device fingerprint, IP geolocation, session behavior, and historical patterns assembled in parallel"; classify the fraud kind (S); ML model and rules run side by side, an aggregation layer makes a composite score.
- COMBINE (Q): "Composite score maps to one of three outcomes: approve, challenge (step-up authentication like OTP), or block." UNSURE = the middle outcome. Q: "if deep path disagrees, triggers follow-up action—not reversal".
- SCALE (S table): fast path 5–15 ms, deep path ~200 ms async, total SLA <50 ms. MEASURE: none given. WENT WRONG: "a single slow component cascades" (S).

**E6 — Explainable AML alert triage.** [preprint, abstract only; PDF unreadable] https://arxiv.org/abs/2604.19755
- TREE (Q): "an evidence-constrained decision process" — evidence bundled from policy, customer context, alert triggers, transaction subgraph; then counterfactual checks: Q "minimal, plausible perturbations lead to coherent changes in both the triage recommendation and its rationale".
- MEASURE (S): PR-AUC 0.75, Escalate F1 0.62, citation validity 0.98, evidence support 0.88, counterfactual faithfulness 0.76. Read: even a paper built around explanation gets 0.76 on whether the explanation follows the decision. Q risks: "explanations that are not faithful to the underlying decision".

### 1.4 Underwriting (credit and insurance)
**E7 — Credit scorecard and the adverse-action rule.** [reference implementation, hobby repo, not a lender] https://github.com/hammas159/credit-risk-engine · [regulation] https://www.consumerfinance.gov/rules-policy/regulations/1002/9/
- TREE/TYPES (S): each numeric feature binned; each bin gets points; "Points sum exactly to the total score". Q: "every 20 points halves the risk".
- COMBINE: sum in code. EXPLAIN (Q): "You lost 76 points relative to the best possible answer" — the reason list is the bins that cost most. Rule Q: reasons "must relate to and accurately describe the factors actually considered or scored by a creditor"; Q "disclosure of more than four reasons is not likely to be helpful"; method Q "the applicant's score fell furthest below the average score".
- MEASURE (Q): "A model can rank perfectly and still be badly wrong about the level." — ranking (Gini) and calibration (Brier) checked separately. S: an information-value above 0.5 flags leakage.

**E8 — Insurance submission triage.** [vendor blog] https://www.hyperexponential.com/blog/submission-triage-insurance
- TREE (S): seven stages: intake → extraction → clearance (duplicates, eligibility) → appetite screen → scoring/priority → routing → handoff. Q: "Automated rules can reject risks that are clearly out of appetite".
- UNSURE (Q): "risks with missing information, unusual characteristics, or lower confidence should be flagged for underwriter review". SCALE (Q): "1,000 submissions a day but able to review only 400". MEASURE/WENT WRONG: none quantified; pitfall: collapsing intake, clearance and triage "loses decision visibility" (S).

### 1.5 Security alert triage (SOC)
**E9 — "Correlate first, escalate last" triage agent.** [single-author blog, toy scale: 17 events, 4 incidents] https://dev.to/adam_lewandowski_59674796/stop-piping-raw-alerts-into-an-llm-building-a-soc-triage-agent-that-correlates-first-and-escalates-20pp
- TREE (S): normalize → correlate → deterministic pre-filter (auto-resolve, "high-signal" techniques always escalate) → model with four tools → containment, destructive actions need approval. Q: "3 of 4 incidents cost $0.00. Only the real attack touches the API."
- TYPES (S): closed `submit_verdict` schema: boolean true-positive, enum severity, P1–P4 priority, confidence 0–100, narrative. COMBINE: mapping verdict → named automation, in code.
- WENT WRONG (S): stale broad suppression rules; identity mismatch across systems; "API failures stalling alert queue (fallback to deterministic engine required)"; "no labeled corpus, measured false-negative rate absent before suppression authority granted".

**E10 — Elastic's SOC benchmark.** [vendor blog] https://www.elastic.co/security-labs/llm-benchmarking-agentic-soc
- Q: "No tool call, no credit. A plausible answer produced without the supporting tool calls the task required is capped at 6 out of 10". Three prompt variants per capability: clear, realistic, ambiguous (S).
- Q: "The most dangerous failure mode in an agentic SOC is the confident, fluent, wrong answer". No accuracy numbers on the page (S).

### 1.6 Legal and contract review, e-discovery
**E11 — GPT-4 first-pass document review (Sidley experiment).** [industry write-up] https://edrm.net/2023/12/replacing-attorney-review-sidleys-experimental-assessment-of-gpt-4s-performance-in-document-review/
- TYPES (Q): each document scored on a −1 to 4 scale; −1 is "document could not be processed" (an abstain), 0 junk, 1 non-responsive, 2 "likely responsive/partial", 3 responsive, 4 responsive with strong evidence. COMBINE: one holistic read → one ordinal; cut point applied later.
- MEASURE (Q): "1,500 total documents … 500 responsive documents and 1,000 non-responsive" from a closed case with human codes. Two stages; stage 2 revised the prompt to mirror "a quality control (QC) feedback loop".
- NOT FOUND on the fetched page: recall, precision, cost. SS (a Sedona Conference paper; PDF unreadable): "as high as 95% recall and 85% precision", best when review is "self-contained" — unverified.

**E12 — CUAD contract corpus.** [dataset paper, abstract] https://arxiv.org/abs/2103.06268
- Q: "over 13,000 annotations", "created with dozens of legal experts"; the task is to "highlight salient portions of a contract that are important for a human to review" — one span-finding question per clause category. Category count, agreement: NOT FOUND on the abstract.

### 1.7 Customer-support and intent routing
**E13 — Anthropic's ticket-routing guide.** [vendor documentation] https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing
- TREE (Q): "Use a taxonomic hierarchy for cases with 20+ intent categories" — a classifier per level. Q on the cost: "Cons - increased latency: Be advised that multiple classifiers can lead to increased latency".
- TYPES (Q): "A request may have ONLY ONE applicable intent." Edge cases named: implicit requests, emotion over intent, "Multiple issues cause issue prioritization confusion".
- MEASURE (Q): targets "consistency rate of 95% or higher", "at least 80% accuracy on these challenging inputs", "rerouting rate below 10%"; retrieval of similar examples "from 71% accuracy to 93% accuracy". These are goals; the page reports no measured result of its own. Reasoning text is returned with the label — a different design from a no-text classifier.

**E14 — Hierarchical classification by beam search; confidence routing.** [vendor cookbook and pattern page — vendor-authored] https://docs.typesafe.ai/cookbooks/hierarchical_classification.md · https://docs.typesafe.ai/patterns/confidence-routing.md
- TREE (Q): "Retain K plausible paths and classify every frontier in parallel. Deeper evidence can repair an ambiguous early decision." One choice question per node, beam width 3, up to 12 layers (S); path score is a length-normalised geometric mean of edge probabilities (S).
- MEASURE (Q): "Beam search matched 4 of 4 expected leaves; greedy search matched 2 of 4." Four test cases — an illustration, not a study. Latency and cost: NOT FOUND on the page.
- UNSURE (S): thresholds set by consequence: below 0.6 to a human; 0.6–0.85 ask the user before a high-stakes action; above 0.85 act. Q: "Use confidence as a second axis. The answer tells you what; confidence tells you whether to act."

**E15 — LiteLLM auto-router benchmark.** [gateway maintainer's blog; reproducible] https://docs.litellm.ai/blog/jev-auto-router-benchmark
- TREE/TYPES (S): one four-way choice: SIMPLE / MEDIUM / COMPLEX / REASONING, to pick which model tier answers. 80 cases × 3 runs = 240 calls.
- MEASURE (Q): typed model "228/240, 95.00%" vs Haiku "177/240, 73.75%" against the authors' own expected tiers; p50 "126.81 ms", p95 "231.16 ms" vs "688.40 ms" / "896.94 ms". WENT WRONG (S): "Labels lacked independent review"; time cannot be split into relay, network and provider.

### 1.8 Industrial and aviation fault isolation, checklists
**E16 — Boeing 737 Fault Isolation Manual.** [enthusiast site summarising the manual — second-hand] https://www.aviationhunt.com/boeing-737-fault-isolation-standard-practices/
- TREE (Q): entry by "unique eight-digit fault code"; Q "Do the steps of the task in the specified order. Obey the 'If … then' statements". Yes/no branches on whether a message is latchable (S).
- ENDPOINTS (S): exactly three — replace component, no fault found (intermittent), escalate. Pitfalls (S): skipping the initial evaluation; acting outside the sequence; "assuming multiple simultaneous failures (FIM assumes single failure)". MEASURE: none on the page.

**E17 — WHO Surgical Safety Checklist.** [SS only; the journal page returned HTTP 403; two of these figures were in my own search query and echoed back — treat as unverified] https://www.nejm.org/doi/full/10.1056/NEJMsa0810119
- SS: 19 items at three pause points (sign in, time out, sign out); 8 hospitals; 3,733 patients before, 3,955 after; deaths 1.5 % → 0.8 % (P=0.003), complications 11.0 % → 7.0 %. Before/after design, not randomized — a caution I am adding, not the page's.

### 1.9 Recruiting and admissions rubric scoring
**E18 — LLMs scoring resumes against a rubric.** [preprint] https://arxiv.org/html/2507.02087v1
- TREE/TYPES (Q): six rubric dimensions ("Experience Relevance, … Educational and Professional Background"); the model returns a score, cut to yes/no at the median (S).
- MEASURE (S): agreement with human raters NOT reported; one run per pair. WENT WRONG: impact ratios 0.640–0.774 against a 0.80 rule (S); Q "the lowest intersectional group receives roughly 6 out of 10 the scoring rate of the highest".
- Admissions rubrics: NOT SEARCHED separately; one search summary mentions rubric-scored resume studies only.

### 1.10 Sports scouting and officiating
**E19 — VAR protocol (football).** [governing body] https://www.theifab.com/laws/latest/video-assistant-referee-var-protocol/
- TREE: gate to four incident kinds (goal, penalty, direct red card, mistaken identity) (S). Q: "VAR is only used after the referee has made a (first/original) decision".
- TYPES/SPLIT (S): factual questions (position, ball out) → video-only review; subjective ones (intensity) → the referee's on-field review. Q: "Only the referee can initiate a 'review'; the VAR can only recommend".
- UNSURE (Q): the decision "will not be changed unless the video review clearly shows that the decision was a 'clear and obvious error'"; Q "There is no time limit for the review process as accuracy is more important than speed". MEASURE: none on the page.

**E20 — 20–80 scouting scale.** [analysis site] https://blogs.fangraphs.com/scouting-explained-the-20-80-scouting-scale/
- TREE/TYPES (S): each tool gets a separate present and future grade; 50 = average, 10 points = one standard deviation.
- COMBINE (Q): the overall grade is not a formula — "isn't just averaging the core future tool grades", it weighs risk and ceiling. That is combining inside a head. MEASURE/COST (S): a 5-point gap between scouts is normal, 10 "unusually high".

### 1.11 Search / ad relevance with rater guidelines
**E21 — Bing: LLM relevance labels.** [industry paper] https://arxiv.org/html/2309.10621v1
- TREE (Q): "Split this problem into steps: Consider underlying intent, measure topicality (M), measure trustworthiness (T), decide final score (O)". Three-level scale, 0–2 (Q "0 = not relevant, 1 = relevant, may be partly helpful, 2 = highly relevant"). COMBINE: in the model — only the overall label is used; aspects merely "anchor" (S).
- MEASURE: Cohen's κ 0.20–0.64 by prompt (Q "6/32 prompts performed better than 0.58 and only 3/32 worse than 0.24"); paraphrase alone moved κ 0.50–0.72 (S); +28 % accuracy over crowd workers, ~2.5 M pairs, 10 languages (S). Latency Q: "minutes to hours latency, ×10 throughput, ×1/20 cost" vs crowd workers.
- WENT WRONG (Q): "LLMs risk over-fitting to model idiosyncrasies rather than true relevance per Goodhart's law"; answer: weekly audits against trained assessors (S).

### 1.12 Cross-domain: decomposed checklist grading
**E22 — TICK.** https://arxiv.org/abs/2410.03608 — Q: LLMs "decompose the instruction into a series of YES/NO questions"; exact agreement with humans "(46.4% → 52.2%)" against having the model score directly. Modest, and the page states no limits.
**E23 — RocketEval.** https://arxiv.org/abs/2503.05142 — S: make a checklist, a small model grades it, items are "reweighted" to align with labels (a fitted combiner, not a hand table). Q: "a high correlation (0.965) with human preferences" using a 2B judge; Q "a cost reduction exceeding 50-fold". Authors' figures.

---

## §2 Design rules that recur

**Answer.** Eleven rules recur across at least three domains each. They agree with Cobalt's own laws, which is the useful finding: the outside world converged on "model answers, table decides".

**R1 Gate early, score late.** The cheapest, most decisive question goes first and can end the tree: ESI decision A (E1), VAR incident kinds (E19), appetite clearance (E8), DoorDash tier 1 (E3), deterministic pre-filter (E9), fast path (E5).
**R2 Decompose the judgment into narrow items.** Wells (E2), scorecard (E7), TICK / RocketEval (E22–23), CUAD (E12), Beri's 62.6 % → 95 % from the second pass. Keep each item answerable from what the answerer can actually see (E4: "things it can't see").
**R3 Say who combines — and prefer the table.** Where the combining is in a model or head, agreement was low or unmeasured:

| Combined by | Example | What it cost |
|---|---|---|
| Written table in code | Wells, scorecard, DoorDash thresholds | auditable; thresholds change "without model retraining" (E3) |
| Fitted weights in code | RocketEval | correlation 0.965 (authors') |
| The model, one final score | Bing, Sidley | κ 0.20–0.64 by prompt; 0.50–0.72 from wording alone (E21) |
| A scout's head | 20–80 overall | 5-point gaps normal (E20) |
| A nurse's judgment | ESI | accuracy 59.6 %, α 0.78 (E1) |

**R4 Make the combiner's endpoints closed and typed.** Three FIM endpoints (E16); three fraud outcomes (E5); closed verdict schema (E9). No free text reaches a decision.
**R5 Always have a default for "unsure", and set it by consequence.** VAR: the original stands (E19); FIM: no fault found or escalate (E16); Sidley −1 (E11); confidence tiers by action (E14); insurance referral (E8). Fallback when the model is down: deterministic path (E9).
**R6 The explanation is the components that drove the score.** Reason codes = points lost vs best (E7); the regulation ties reasons to "factors actually considered or scored". A separate model-written rationale can be unfaithful (E6: 0.76).
**R7 Numbers become bins before anyone judges them.** Scorecards bin (E7); Wells buckets a heart rate (E2); 20–80 pegs grades to measured ranges (E20 SS). No source lets the judge do arithmetic.
**R8 Keep one leaf for the human.** Wells' subjective item is flagged (E2); VAR splits fact from feel (E19); scouts keep the overall (E20).
**R9 Measure against a human gold set — and know what agreement means.** Golden set first (E4); agreement ≠ accuracy (E1: 0.78 vs 59.6 %); ranking and calibration are separate checks (E7); the labeller's own consistency is the ceiling (E20: 5-point gaps).
**R10 Wording is part of the model.** Paraphrase moved κ 0.50–0.72 (E21); long policies degrade (E4); Sidley revised the prompt in a QC loop (E11); a wording change is a new classifier.
**R11 Plan the maintenance.** Nine retrainings (E3), stale suppression rules (E9), golden sets refreshed quarterly (E4), weekly audits (E21), Goodhart drift (E21).

---

## §3 Speed, honestly

**Answer.** What is published shows a typed classifier answering in roughly a tenth of a second to half a second per call, and a one-call bundle of questions beating a chain of calls; DoorDash shows why a generative LLM at "2-10 seconds per call" forced a cascade. Nobody has published a 20–30-question tree, a local-model figure for this job, or where the milliseconds go from a Mac Studio; the trial measures those.

| # | Fact | Grade | Source |
|---|---|---|---|
| L1 | 13 questions (8 yes/no, 2 choice, 3 score) in one call: Q "0.27s"; sequential 13 calls Q "2.71s" ("10.0x faster"); cost Q "12.2x cheaper"; answers stable, Q "std dev exactly 0.0" over 5 repeats; one ~54,000-character document, model `jev-1.12` | vendor-authored | https://docs.typesafe.ai/cookbooks/parallel_questions.md |
| L2 | Single-choice router, 240 calls: p50 Q "126.81 ms", p95 Q "231.16 ms"; Haiku "688.40 ms" / "896.94 ms"; includes "local relay, client, network and provider work" (S) | integrator | E15 |
| L3 | Tool-call risk classifier, 60 cases: p50 Q "421.6 ms" (`jev-latest`) / 378.5 ms (preview); p95 Q "542.0 ms" / 484.3 ms | individual repo | https://github.com/themsquared/jev-benchmark |
| L4 | Tokyo vs US west coast gap ~114.8 ms "entirely" network; sfo1 p50 25.8 / p95 41.2 ms | SS only — repo returned HTTP 404 | search 16 |
| L5 | Generative LLM at DoorDash: Q "2-10 seconds per call"; first-tier classifier Q "under 100 milliseconds at the 90th percentile" | company | E3 |
| L6 | Fraud engine design targets: fast path 5–15 ms, deep path ~200 ms async, SLA <50 ms | design targets, unmeasured | E5 |
| L7 | LLM labelling pipeline: Q "minutes to hours latency, ×10 throughput, ×1/20 cost" against crowd workers (a batch pipeline, not a per-call figure) | paper | E21 |
| L8 | A layered tree costs a round trip per level; the vendor's own beam search issues each level's frontier in parallel, so depth × one call is the floor | Q (E13); NOT FOUND (E14 latency) | E13, E14 |

Carried from the second pass, not re-fetched: vendor claim 70–500 ms; individual trials 130 ms direct / 260 ms via a gateway, 0.32 s and 0.59 s medians.

**Where the milliseconds go.** NOT KNOWN for Cobalt. The only split published is L4 (network dominates a cross-ocean call; SS), and L2 says its own timing cannot be split. The Anthropic guide says "near-instantaneous routing" is possible but gives no figure (E13). The Anthropic latency page moved (HTTP 404): NOT FOUND.

**One call with all questions vs sequential gated calls.** One call: a single round trip, tokens sent once (the vendor's own 13× token remark: "The document dominates every request"), gates applied in code afterwards; cost is asking questions the gate would have pruned. Sequential: one round trip per level, roughly 4 levels × 127 ms ≈ 0.5 s at L2's p50 (arithmetic, assumes each level costs one such call), needed only when a later question's option list depends on an earlier answer.

**What Cobalt's paths need.** A scan every ≈60 s and L2 (no model in a watch loop) mean the scan tick never waits: labels are computed on an event, stored, and read by the scan. Milliseconds matter on three other paths: (a) a card forming on an event while he watches; (b) interactive turns — his requirement is sub-second, "seconds is acceptable" (first pass, row 23); (c) **shadow backfill**, where the gain is largest. ASSUMED arithmetic for (c), 5,000 stored cards: at 2 minutes a card through a chain of local prompts (his word "minutes", the 2 is assumed) = 600,000 s ≈ 6.9 days; at L1's 0.27 s per call = 1,350 s ≈ 22.5 minutes; at L2's 0.127 s = 635 s ≈ 10.6 minutes. Speed there means he can test a rewording of the question set on all of history the same day.

**Trial measurements (14).** Vantage: the Mac Studio; invented placeholder text only; nothing of his.
1. Network floor: one tiny question, tiny state, n ≥ 200 across the day (04:00 premarket, open, midday, close); p50/p95/p99, plus first-call-after-idle vs warm connection.
2. Marginal cost per question: 1, 5, 13, 25, 40 questions per call with state of 300 and 1,500 tokens; does p95 grow, and does the 64k limit matter?
3. One call of N questions vs N parallel single calls vs N sequential: wall time, tokens, 429 rate.
4. Gated tree of 3–4 levels (sequential) vs one fan-out call: wall time, and whether answers to un-pruned questions are identical.
5. Determinism: the same call ten times — identical probabilities? Spread if not (second pass §6 item 2; measure again with the larger set).
6. Question-order effect: shuffle the question map; do any answers move?
7. Number of distinct probability values returned (ties), for any sort or threshold use.
8. Local lane on the same questions: seconds per set with schema-constrained output, thinking on, tokens generated; per-token log-probabilities available or not (NOT KNOWN).
9. Timeout and retry: p99, share of calls over 1 s, cost of the vendor's retry advice, behaviour at 429.
10. End-to-end event path: event timestamp → validated answer vector stored in Postgres (Pydantic, write included) — the number he will feel.
11. Actual input tokens of a real Cobalt-shaped 15–25-question set → cost per card (the only measured size so far is one question, 296 tokens, first pass).
12. Throughput headroom: vendor limit 1,200 requests/min against measured event rates in shadow.
13. Backfill: N stored items replayed; wall time (checks the §3 arithmetic).
14. Agreement with his hand labels on the same items — accuracy, not latency, but it comes from the same run (L7, L8).

---

## §4 Transposition to Cobalt

**Answer.** Ten patterns land in Cobalt; the first is his own trade-grade example, built as a scorecard: many narrow typed questions, one call, a ruled table in code, and the answer vector as the explanation. Every model label enters as a judgment-tier SHADOW value (L7), marked modelled (L52a); all labels are by KIND; his values, rules and notes never appear here (L32).

**Common conventions.** Numbers reach the model as words: bucket edges are ruled settings in a schema'd, git-tracked config with a dry-run (L10, L53); the stored record keeps number and word (L57). Every choice carries `unsure`. "Not asked" (a gate closed) is its own typed value. The model gives no text; the answer vector is the explanation (L57). A label is computed on an event and stored; the scan reads it (L2).

### T1 — His example: setup-quality / trade-grade (rows 5, 3, 10, 8; patterns E7, E2, E1, E22–23, E19)
- **Layer 0, code only:** the setup predicate is formed (three-valued, deterministic) — else no call; input freshness (an as-of stamp); the override list of T7 (like ESI's first decision, not a model question).
- **Layer 1, gates (model, yes/no/unsure, asked in the same call, applied in code):** G1 a catalyst is present in the stored items; G2 the market context is readable; G3 per rule kind from his playbook, "this setup conflicts with rule <kind>" — one yes/no per rule, list loaded at run time (user data, L32: local lane by default). A closed gate makes its dependents "not asked".
- **Layer 2, context (choice):** market alignment {with, flat, against, unsure}; sector alignment, same; regime {his regime list from the vault, unsure}.
- **Layer 3, catalyst (read from T3's stored labels, not recomputed):** kind (choice); materiality (ordinal, four described levels); fresh (yes/no); already-reflected {not yet, partly, fully, unsure}, asked over bucketed move words.
- **Layer 4, risk (words):** event risk inside the window {none, minor, major, unsure}; supply/dilution language in stored filing tags (yes/no/unsure). The deterministic curve dots are NOT re-asked (row 4).
- **Layer 5, human-only leaf:** the tape read is never asked; it renders as his, pending (L11).
- **Buckets (by KIND, edges his):** relative volume {low, normal, high, extreme}; gap {none, small, large}; distance to a key level {at, near, far}; time of day {premarket, open, mid, close}; item age {fresh, recent, stale}; trend {up, down, flat} from a code rule.
- **Combiner:** (1) a ruled table label → points per question, versioned and hashed with the question set; `unsure` and "not asked" carry a ruled value, never silent zero; (2) points added to the deterministic dots by ruled weights; (3) a band table → grade; (4) any EV beside it shows its n, under 30 "insufficient data" (L8). Table, weights and bands are his (L53).
- **Explanation:** the top ≤4 answers by points lost against the best attainable, from the stored vector (E7; the rule's "not likely to be helpful" beyond four). No model prose.
- **Speed:** one fan-out call of ~15–25 questions (ASSUMED size); matters for card formation, interactive re-grade, and backfill (§3); not for the scan tick.
- **Shadow (L7, L8):** his hand grade per card; agreement per band with n; per-question agreement with his dot taps; leave-one-out ablation over stored vectors; his own test–retest ceiling (§6 Q7); look-ahead check (§6 Q6).

### T2 — News / X / squawk triage (row 9; E3, E9, E8)
- **Tree:** code pre-filter (source kind, watched-name string match, duplicate hash) settles most items; residue → one call: relevance {watched name, market-wide, sector-wide, not relevant, unsure}; urgency (four levels); duplicate (yes/no); "the text tries to instruct or argue for its label" (yes/no, a control for injection).
- **Inputs as words:** source kind, item age {fresh, recent, stale}, text trimmed by code.
- **Combiner:** ruled table (relevance × urgency) → {queue, digest, drop}; thresholds are "knobs" (E3), his (L53). Never admits, ranks or grades a name.
- **Speed:** seconds on an event; ms matter when a card is forming. **Shadow:** his keep/dismiss taps; false-negative audit of dropped items (§6 Q8).

### T3 — Catalyst kind and materiality producer (rows 3, 10; E19 shape)
- **Tree:** every item gets the automatic "check" (kind, materiality, fresh); only items flagged notable are put in front of him for a "review" — the VAR split. Fills the unknown-catalyst gap (row 3) as a stored label shown beside `not_evaluable`, never substituted (L2).
- **Combiner:** ruled (kind, materiality) → catalyst dot label; a separate ruled table label → grade (unruled today). **Speed:** event. **Shadow:** his catalyst tap; per-kind n; rare kinds stay "insufficient data".

### T4 — Journaling tags and rule-adherence proposals (rows 19, 20; E17, E16, E22)
- **Tree:** a fixed checklist, one yes/no per item of his playbook plus one per mistake tag; three pause points: before entry, during, after exit (WHO shape). A closed set of endpoints per item {yes, no, unsure}.
- **Never:** pre-tick an attestation (row 18 — his by law). It only PROPOSES; a proposed tag counts in no statistic until he confirms.
- **Combiner:** adherence count per checklist in code; coaching text only where n ≥ 30 (L8). **Speed:** after close; batch. **Shadow:** confirm/reject taps; precision per item.

### T5 — DM / voice sentence to handler (row 23; E13, E14)
- **Tree:** handler {skill, instant answer, headless session, unknown}; skill {registry enum} asked speculatively in the same call; "asks to change a rule, setting or position" (yes/no).
- **Combiner:** unknown → asks him to rephrase; the yes/no above forces the HITL path whatever the handler (L37). Floors set by consequence (E14): display < queue < dot.
- **Speed:** sub-second required; one call, not the two-level cascade E13 warns about. Local lane by requirement. **Shadow:** silent beside the current router; per-handler agreement, re-ask rate.

### T6 — Filing-section flags and dilution (row 14; E12, E10)
- **Tree:** CUAD shape — one yes/no per instrument kind per section {common, warrants, convertible, preferred}, plus section kind (choice). Code fetches the verbatim span; a figure with no quote is rejected.
- **Combiner:** none numeric from the model. E10's rule transposed: no evidence span, no credit. **Speed:** batch, minutes fine. **Shadow:** his spot checks; per-flag n.

### T7 — Regime label and deterministic overrides (row 15; E1, E9)
- **Tree:** a code-built list of override conditions (stale input, missing feed, a hard-stop event kind) beats any model answer and forces `not gradable` — ESI's "danger zone" and E9's "always escalate regardless". Below it: regime {his regime list, unsure} over bucketed context words.
- **Combiner:** none; label only. **Speed:** scheduled. **Shadow:** his regime tap; agreement per label.

### T8 — "Why is it moving?" candidate picker (row 11; E9, E16)
- **Tree:** code enumerates candidate causes; one choice over ONLY those plus {none of these, unsure}; endpoints closed like a fault tree.
- **Combiner:** none; the paragraph is composed from the picked item by the ruled lane. **Speed:** seconds. **Shadow:** agreement per candidate class; how often "none of these" fires measures the resolver itself.

### T9 — Ops day-open log triage (row 27; E16)
- **Tree:** per check, ordered yes/no items ending in green / amber / red with the cited log line; missing log = red (L1). Local lane; zero trading exposure — the cheapest first proof of the whole seam.
- **Combiner:** worst of the checks, in code. **Speed:** minutes. **Shadow:** his read of the day-open.

### T10 — Task-class labelling for model routing (rows 24, 25; E15)
- **Tree:** one choice over a task-class enum; the class → model table stays "assigned by measured evidence" (L26). E15's caution: its labels "lacked independent review" — so Cobalt's shadow needs his labels first.
- **Combiner:** routing table in config. **Speed:** sub-second is useful (E15 p50 126.81 ms). **Shadow:** per-class agreement, and downstream outcome per class.

---

## §5 What would make this fail for a one-person desk

**Answer.** Five likely failures, each with a cheap guard; the common thread is that a fluent wrong answer looks the same as a right one, so every guard is a measurement.

1. **Confident, wrong, and unmeasured.** E10: "the confident, fluent, wrong answer"; E9: no false-negative rate before suppression authority; E1: 0.78 agreement, 59.6 % accuracy. *Guard:* shadow only; no label suppresses anything from him; weekly audit of what was dropped (E21).
2. **Wording brittleness.** Paraphrase alone moved κ 0.50–0.72 (E21); long policies degrade (E4). *Guard:* one question per file, hash stored, paraphrase test before shadow, a rewording resets the count (first pass Q10; second pass §7.1).
3. **Drift and stale rules.** Nine retrainings (E3); stale suppression rules (E9); golden sets go obsolete (E4). *Guard:* pinned model id in every record; quarterly gold-set refresh; regression check per label after any change.
4. **The combiner becomes a hidden model.** Correlated questions double-count (market and sector alignment); a 0–100 look implies false precision; RocketEval-style fitted weights (E23) can overfit a small label set. *Guard:* hand table first, no fitting below n = 30; report answer-vector correlations; show bands, not decimals; ablation.
5. **Leakage and a noisy single labeller.** A stored item that post-dates the alert inflates shadow agreement (E7's leakage flag); one person's labels have a ceiling (E20: 5-point scout gaps). *Guard:* as-of freezing at event time; blind re-label of a random sample after two weeks; agreement is judged against his test–retest, not against 100 %.

---

## §6 Additions to the tribunal's questions

**Answer.** Eight new questions, none repeating the 18 already written (first pass 1–10; second pass 1–8). Each is ADOPT / ADOPT WITH / REJECT-shaped.

1. **The answer vector is the explanation.** Adopt: any model-assisted dot stores the full typed answer vector and the ruled-table version, and the "why" is computed by code as the ≤4 answers costing the most points against the best attainable. *Basis:* E7, R6. ADOPT WITH: no model-written text in the explanation.
2. **Gate in code, fan out in the call.** Adopt: non-dependent questions go in one call and gates are applied afterwards; a sequential call only where a later option list depends on an earlier answer. *Basis:* E13's latency warning, §3 L1/L8. ADOPT WITH: the trial (measurements 3–4) confirms.
3. **A short ruled override list beats any model answer.** Adopt: stale or missing inputs and a small set of hard conditions force `not gradable`, whatever the model said. *Basis:* E1 decision A, E9. ADOPT WITH: the list is his and versioned (L53, L10).
4. **Floors by what a label may do.** Adopt: separate floors for display, queue and dot entry (extends second pass 4: per question, type, version). *Basis:* E14 consequence tiers. ADOPT WITH: fitted offline.
5. **Independence and double-count test.** Adopt: any question set feeding one dot reports answer-vector correlations in shadow; correlated pairs share a weight budget. *Basis:* E7 (leakage flag), E2. ADOPT WITH.
6. **As-of freezing.** Adopt: the stored input is frozen at event time; shadow uses only as-of data; an implausibly high agreement on one question is a leakage alarm. *Basis:* E7. ADOPT.
7. **His own reliability is the ceiling.** Adopt: before judging a model, measure his blind test–retest on a random sample; model agreement is read against it. *Basis:* E1, E20. ADOPT WITH: sample size ruled by L8.
8. **No label suppresses an item until its false-negative rate is measured.** Adopt for T2 and any triage that drops items. *Basis:* E9, E21. ADOPT WITH: audit cadence and n his.

---

## §6A Question types and confidence

*Added at his request via the desk, 16:07 ET, `cto-2026-09-21.md` R37 (arrived as a cross-session message; the +8 fetch / +3 search / +60 line allowance is the desk's, unverified by me). Seven fetches, no searches used for this section.*

**Answer.** The desk's reading is right: the "three types" are the vendor's three question types — Choice, Score and Noul (yes/no); the vendor calls them "questions", not searches, and the multi-step use is fan-out plus hierarchical classification (E14). Confidence exists only for Choice and Score, is a shape statistic of the probability spread and not a probability of being right, is absent for Noul, and independent tests found its miscalibration has a different sign for each type.

**(1) The three types** — https://docs.typesafe.ai/api.md · https://docs.typesafe.ai/primitives.md (S = fetch summary)

| Type | For | Request (S) | Answer (S) | Example as returned |
|---|---|---|---|---|
| Choice | one of an unordered set | `instructions`; required `criteria` map, max 255 options | `choice`, `probabilities` (sum to 1), `confidence` | `choice: "billing"`, `confidence: 0.81` |
| Score | a rating on described ordered levels | `instructions`; required `criteria` array, 2–10 levels | `score` (a number), `legend`, `probabilities`, `confidence` | `score: 1.05`, `confidence: 0.92` |
| Noul | probability a yes/no statement is true | `instructions`; optional `criteria` with `true`/`false` | `noul`, a number 0–1 | "Does this convey urgency?" → `noul: 0.95` |

Q: "A Noul value of 0.5 means equal probability, not a medium skill level." Max questions per request: the page "does not specify" one (S) — NOT FOUND.

**(2) What confidence is, per type** — https://docs.typesafe.ai/confidence.md
- **Name and range:** `confidence`, 0 to 1. Q: "Confidence is derived from the probability distribution the answer already gives you." For three options it approximates (3 × largest probability − 1) / 2 (S): a rescaled maximum probability.
- **Choice and Score have it; Noul does not.** Q: "Noul answers don't carry one." For Noul the probability itself is the signal — Q (primitives): "near 1 is a strong yes, near 0 a strong no, near 0.5 uncertain."
- **Is it calibrated?** The page does not claim it is a probability of being correct (S). Its thresholds are examples: below 0.5 human, 0.5–0.9 caution, above 0.9 automatic (S); the confidence-routing page uses 0.6 / 0.85 for one case (E14) — two vendor pages, two sets, so neither is a default. Q: "The correct threshold values depend on your domain and the performance of the model for your use case."
- **Independent tests, per type** (`as returned`, all individual repos, no finance data):

| Type | Finding | Source |
|---|---|---|
| Choice | Banking intents ECE 0.0936 "overconfident", clinic intents 0.0204 "calibrated"; the run was "one Choice question per item" and Q "It is not a statement about Jev on any other task, corpus, or day." | https://github.com/jourdanlabs/assay-001 |
| Choice | unseen task, n = 300: accuracy 89.0 %, ECE 0.082, refit temperature 3.29, overconfident; public sets ECE 0.024 / 0.032 / 0.029 | https://github.com/scienthoon/jev-ood-calibration |
| Score | unseen task, n = 300: accuracy 44.7 %, ECE 0.325, refit 3.40, overconfident; Q "mean stated probability 0.74" on a rule it could not know | same |
| Score | ordinal inversion 0.1433 against a gate of 0.15 — "barely passes"; 88 distinct values | https://github.com/yodablocks/jev-orderby-bench |
| Noul | unseen task, n = 300: accuracy 91.7 %, ECE 0.079, refit 0.66, UNDERconfident; topic task ECE 0.0453 (passes); harder product-relevance task fails 4 of 6 gates | both repos |

- **Cross-type findings (Q):** "sign of miscalibration differs by type"; the `confidence` field is "never better than max probability and sometimes much worse". Precision: Q "45 distinct values" in 360 rows, "53 rows tied at 0.99"; Q "1,051 of 2,000 option probabilities are exactly 0". Two decimals, ties and hard zeros — a threshold works, a ranking does not.

**(3) Multi-step and layered use**
- **Batching:** Q "Send many questions in a single API call"; Q "All questions are evaluated in parallel, so adding more questions usually has little effect on response time." (https://docs.typesafe.ai/patterns/fan-out.md; primitives page: "barely changes the response time"). Each answer carries its own confidence (Choice, Score) or probability (Noul); there is no call-level confidence.
- **Combining:** the fan-out page gives "no explicit guidance" on combining confidences across questions (S). Primitives Q: "change the value of weights rather than rewriting a prompt" — the vendor's advice is weights in code. Its one chained rule is the hierarchical cookbook's geometric mean of edge probabilities (E14), a product-shaped rule that is only sound if the steps are independent — for Cobalt's correlated context questions they are not.
- **What breaks a batch:** many STATES in one call, not many questions on one state: Q "mean |Δp| 0.264", "51% of rows moved > 0.20", "77 decisions flipped at 0.5" for 40 rows packed (yodablocks). The vendor's repeat test on 13 questions over one state found "std dev exactly 0.0" (§3 L1, vendor-authored). Whether 25–40 questions on one state stay isolated: NOT KNOWN.
- **For T1 (the layered trade-grade):** one state, ~15–25 questions (ASSUMED), one call; every answer stored with its probabilities and confidence; code maps each answer to points (per-type floors, since Choice/Score run overconfident and Noul underconfident); a grade-level "how sure" is a code statistic over the stored vector that he defines — for example how many answers fell to `unsure` and the weakest answer among the top point drivers — never an average or product of vendor confidences.

**(4) How Cobalt must account for confidence**
1. Floors are his rulings (L53): per question, per type, per model version, fitted offline on his labels; the vendor's examples are not defaults.
2. Below the floor the value is a typed `unsure` shown as a degraded / human-tap state — never a silent number (L1, L9); the dot degrades as "modelled" (L52a); under 30 per label reads "insufficient data" (L8).
3. Stored with its inputs and the reported model id, question hash and lane (L57); the confidence in the record is what was returned, not recomputed later.
4. Never a sort key, tie-break, EV input or ranking authority (L52b; second pass §7 item 3).
5. His shadow report shows per-type reliability: confidence band against agreement with his hand label, with n.
6. The local lane returns no per-option probability; whether the local server returns log-probabilities is NOT KNOWN (measurement 8).

**(5) NOT KNOWN → added trial measurements (15–19)**
15. Recompute confidence from the returned probabilities for 200 calls: does the reported value equal the documented formula, and is it ever worse than the maximum probability?
16. Share of answers with a probability of exactly 0 or 1, per type (saturation).
17. Do probabilities or confidence for a question move when 25 and 40 questions ride on the same state (questions, not rows)?
18. Per-type reliability curves on his hand labels, in shadow — the only measurement that answers "is 0.9 right 90 % of the time for MY questions" (L7, L8).
19. Noul floors per tag or question on his labels, since the type reports no confidence and ran underconfident in one audit.

---

## §7 Sources and searches

Counts: **47 fetches (34 usable, 13 not; 40 in the first budget, 7 more for §6A), 18 searches, 5 local reads** (prompt, first pass, second pass, LAWS.md in two pages; CLAUDE.md was supplied in the session context). All URLs used for figures are cited beside them in §1 and §3.

**Fetches that returned nothing usable (13):** PMC old-URL redirect (re-fetched); Sedona "Beyond the Bar" PDF (binary); arXiv 2604.19755 PDF (binary) and its `/html` form (404); Equifax scores white paper (404); ESI Handbook PDF (binary); Anthropic ticket page old-URL redirect (re-fetched); Wikipedia `Wells_score` (disambiguation page); PubMed 10744147 and PubMed 19144931 (cookie wall); Anthropic latency page (404); `lowspecbot-GH/latency-probe` (404); NEJM 10.1056/NEJMsa0810119 (403).

**Searches (generic terms; nothing of his; two carried figures from a public paper I already knew, which the results echoed back and I flagged):**
1 ESI four decision points · 2 LLM content moderation policy decision tree · 3 LLM SOC alert triage benchmark · 4 LLMs predict searcher preferences Bing · 5 credit scorecard points reason codes · 6 technology-assisted review GPT-4 · 7 aviation fault isolation manual decision tree · 8 LLM resume screening rubric · 9 VAR protocol clear and obvious error · 10 support intent routing hierarchical · 11 fraud rules engine plus ML architecture · 12 insurance submission triage LLM · 13 Wells score criteria · 14 baseball 20-80 scale · 15 checklist-based LLM evaluation · 16 Jev latency benchmark · 17 DoorDash SafeChat cascade · 18 surgical safety checklist 2009.

**Search summaries never fetched (SS, unverified):** ESI "one or two decision points"; the two-tier Wells cut; the Sedona 95 %/85 %; latency-probe figures; Haynes/WHO figures; that "below about 85% classification accuracy, agents stop trusting the routing" (a routing-guide snippet), which I did not use as a figure.

**Not found:** original Wells derivation; admissions rubric studies; CUAD category count; Sidley recall/precision; aviation fault-tree measurements; any latency for a 20–30-question call; any local-model latency for this job; the vendor's hierarchical-classification latency.

**Text addressed to me:** none seen in the pages as returned (the tool summarises, so a line could have been dropped). Nothing installed, run or signed up for (L15).
