# Typed classifiers for Cobalt — SECOND PASS, deeper research (2026-09-21)

Seat `typesafe-research-deep-0921` · Sonnet 5 · prompt `prompts/2026-09-21/47-research-typesafe-deep.md` · ordered by Dejan, `cto-2026-09-21.md` R34. LADDER: OFF-LADDER (R31 / R34). It EXTENDS `TYPESAFE-CLASSIFIER-RESEARCH-2026-09-21.md` (the first pass) and is read together with it as INPUT to the four-house tribunal design session after sprint S2 closes. It proposes no design, recommends no purchase, builds nothing, ran nothing: no sign-up, no key, no install, no call to the product.

**How to read the evidence.** Three kinds of text are in here, and each is marked. (1) `as returned by the fetch tool`: a page fetched today and passed through a small summarising model, so a quote is verbatim as returned, not proven verbatim. (2) `search summary`: a sentence written by the search tool about result pages that were NOT fetched — the weakest kind, never used as a figure without that label. (3) `second-hand`: a project or claim that appears only in someone's curated list. Every URL is in §8. NOT FOUND = looked for on the pages read, absent. NOT KNOWN = nobody has published it.

---

## §0 What the second pass adds

**Short answer.** The product turned out to have a large, noisy public ecosystem after only six days, and for the first time there is independent measurement of its probabilities — mixed, and mostly bad news for trusting them blindly. Five facts changed or sharpened the first pass.

1. **There are users, but almost none are professionals, and none is a named production customer.** In six days the community produced hundreds of demos, SDKs and clones (one curated list counts 297 entries, as returned by the fetch tool). §3 tables 24 real users: 3 independent audits, 10 users reporting their own trial, 11 second-hand mentions. Named customers on the vendor's own pages: none (home page, launch post, The Register — all checked). The finance list is 8 projects, all crypto bots, paper trading or hobby forecasting (§3.3).
2. **Independent calibration evidence now exists and it is mixed.** Reported by third parties, on their own code: probabilities well calibrated on one public intent benchmark (ECE 0.0204) and overconfident on another (0.0936); on a task the model cannot have seen, ECE 0.107, 4.4 times the noise floor, with Choice and Score overconfident and yes/no underconfident. Probabilities come back at two decimals, so ranking by them produces ties (53 of 360 rows tied at 0.99). Packing many rows into one call shifted answers by slot. The first pass said "no independent evidence"; that is no longer true.
3. **The data-terms picture is better than the first pass said, and still unfinished.** The vendor's legal page lists a Data Processing Agreement and a Master Customer Agreement and says Zero Data Retention is available to enterprise customers. The first pass reported "DPA NOT FOUND": it had not read that page. The DPA text itself was not read (a guessed URL returned 404). The privacy policy's retention sentence is about "personal data", not about the content sent in requests, and "the Site" in the terms includes subdomains.
4. **The company is verified.** Founded 2024; $40M seed led by DCVC; CEO Diogo Almeida, CTO Erik Gafni, COO Sasha Sheng (team page and a press-release copy, both fetched). Churn is fast: four SDK releases in seven days, two breaking; the vendor's own cookbook still cites `jev-1.12` while the docs list `jev-1.13.0`.
5. **The typed interface is already portable.** The vendor itself publishes an MIT-licensed adapter that runs the same typed question over OpenAI-compatible providers and native Anthropic. The product is also reachable through gateways (a Cloudflare model page confirmed by fetch; Vercel, LiteLLM hooks second-hand). That does not change the L5 / L15 verdict, but it shows the neutral-schema idea (first pass question 6) is what the vendor's own community is already doing.

---

## §1 Verification of the first pass's quotes

**Short answer.** Of 48 quotes and terms re-opened today, 46 came back the same and 2 differ; neither difference weakens a limit the first pass reported. One of them (the DPA) makes the vendor look better than the first pass said.

All quotes below are `as returned by the fetch tool`. A house that relies on a number re-opens the URL first (L35). Not re-opened, because the job is capped at 10 fetches: the quickstart page, the LiteLLM, LM Studio and SetFit pages (alternatives, not vendor figures) and the page that returned HTTP 403 in the first pass.

| # | First-pass claim (what was quoted) | URL | Status |
|---|---|---|---|
| 1 | Price "$0.042 / MTok" | docs.typesafe.ai/models.md | CONFIRMED — "Price (per Btok / per Mtok) \| $42 / $0.042" |
| 2 | "Output tokens are free." | same | CONFIRMED — "Charged per input token. Output tokens are free." |
| 3 | Rate limits "250,000 tokens per second / 1,200 requests per minute" | same | CONFIRMED |
| 4 | Limits "can change without notice" | same | CONFIRMED — "Rate limits are adjusting dynamically. We are serving a very large volume of demand, and the limits above can change without notice" |
| 5 | "64k tokens per request; 32k tokens for state plus the longest question" | same | CONFIRMED |
| 6 | Aliases `jev-latest`, `jev-preview`; "pin that version's ID" | same | CONFIRMED — both alias to `jev-1.13.0` today |
| 7 | Deprecation policy NOT FOUND | same | CONFIRMED absent; new sentence: "An alias moves when a new release ships, so the answers behind it can change without a change on your side." |
| 8 | No training on Input | typesafe.ai/legal/privacy-policy | CONFIRMED — "We will not train or fine tune any artificial intelligence or machine learning models on your prompts or other Input." |
| 9 | Retention "as long as reasonably necessary … or otherwise in support of our business" | same | **DIFFERS** — returned "We retain personal data about you for as long as reasonably necessary to provide you with the Services"; the tail "in support of our business" was not returned, and the subject is personal data, not request content |
| 10 | "hosted in the United States" | same | CONFIRMED |
| 11 | Sharing with "vendors and service providers" | same | CONFIRMED — "We may disclose personal data we receive to vendors and service providers that help us provide the Services." |
| 12 | Privacy policy dated Nov 19, 2025 | same | CONFIRMED |
| 13 | Entity and address | typesafe.ai/legal/terms | CONFIRMED — "TypeSafe AI, Inc., located at 255 California St, Suite 1300, San Francisco, CA 94117" |
| 14 | "Do not submit … confidential or proprietary through the Site." | same | CONFIRMED; new: "Site" is the "website at https://typesafe.ai, including subdomains of that website" — docs and API hosts are subdomains, so whether it covers the API stays open |
| 15 | Terms "Last updated Sep 19, 2026" | same | CONFIRMED |
| 16 | "API-specific terms, DPA, zero-retention option: NOT FOUND" | docs.typesafe.ai/legal.md (not read by the first pass) | **DIFFERS** — lists a Data Processing Agreement ("how we process customer data on your behalf, including data retention"), a Master Customer Agreement, the Privacy Policy, and Zero Data Retention "available for enterprise customers" (contact privacy@typesafe.ai). No SOC 2 document, no subprocessor list, no security page on it |
| 17 | "Jev is not a calculator. We strongly recommend implementing any mathematical logic in code." | …/model-jaggedness/jev-1.13.md | CONFIRMED |
| 18 | "does not count reliably" | same | CONFIRMED — "`jev-1.13` does not count reliably." |
| 19 | "reads dates as text, not as ordered quantities" | same | CONFIRMED |
| 20 | Cannot judge nearness | same | CONFIRMED — "Given RGB triples or hex values it cannot reliably judge whether two values are near each other." |
| 21 | Distractors | same | CONFIRMED — "Unrelated detail acts as a distractor, and a large state makes it harder to tell which part of the input produced a wrong answer." |
| 22 | Adversarial / injected instruction | same | CONFIRMED — "Content written to adversarially steer the model, whether that is an injected instruction, a deliberately misleading framing, or text that argues for its own classification, can move the answer." |
| 23 | "not trained to generate text" | same | CONFIRMED |
| 24 | "score levels are weak in numerical calibration" | same | CONFIRMED |
| 25 | Double negatives | same | CONFIRMED — "Instructions carrying double negatives or complex indirection are answered less reliably." |
| 26 | Confidence is "a statistic computed from the probability distribution" | docs.typesafe.ai/confidence.md | CONFIRMED; new: "We provide confidence as a convenient measure that fits most use-cases, but you are never locked into our definition." |
| 27 | "Model is genuinely unsure. Don't guess." | same | CONFIRMED (a code example routing below 0.5 to a human; the page also shows >0.9 for destructive actions) |
| 28 | "Start with conservative thresholds, test with your own data, and adjust" | same | CONFIRMED |
| 29 | `POST https://api.typesafe.ai/v1/systemone`, Bearer key | docs.typesafe.ai/api.md | CONFIRMED |
| 30 | Three question types; Score 2–10 levels | same | CONFIRMED |
| 31 | 255 options per Choice (first pass: third-party only) | same | CONFIRMED by the vendor — "maximum of 255 options per Choice" |
| 32 | Errors 401 / 422 / 429 / 529, backoff advice | same | CONFIRMED |
| 33 | RLCD term | typesafe.ai | CONFIRMED — "Reinforcement Learning for Calibrated Decisions (RLCD)"; the longer "new architecture, new sampler" sentence was not returned |
| 34 | "Typed outputs that software can act on" | same | CONFIRMED |
| 35 | Demo "Completed in 0.114s" | same | CONFIRMED (the page shows 8.566 s for the LLM side of the demo) |
| 36 | "$40 million in funding" | theregister.com …/5296711 | CONFIRMED |
| 37 | CEO a former OpenAI researcher | same | CONFIRMED — "Diogo Almeida, co-founder and CEO of TypeSafe AI, is a former OpenAI researcher" |
| 38 | "70ms-500ms, 40x-200x faster" | same | CONFIRMED — "supposedly ranges from 70ms-500ms" |
| 39 | Price sentence | same | CONFIRMED — "Jev charges $0.042 / MTok for input and $0 for output" |
| 40 | "hallucination-free … not a fair comparison" | same | CONFIRMED |
| 41 | "no published weights and no on-prem option today" | truefoundry.com/blog/typesafe-ai-jev | CONFIRMED (article dated 2026-09-18) |
| 42 | Early-access waitlist | same | CONFIRMED — "currently behind an early-access waitlist"; the vendor's home page agrees: "Try our first System One Model, Jev, in early access." |
| 43 | The "still unknown" list | same | CONFIRMED; the full list ends "and anything at all about production reliability at scale" |
| 44 | Benchmarks "self-graded on a format the company invented" | same | CONFIRMED |
| 45 | "what's been eliminated is the malformed answer, not the mistaken judgment" | same | CONFIRMED |
| 46 | Calibration "the one no outside party has tested yet" | same | CONFIRMED as a statement of 2026-09-18; §3.1 shows outside parties have tested it since |
| 47 | "Break a complex judgment into atomic scores, combine with weights you control in code." | …/patterns/composite-scoring.md | CONFIRMED |
| 48 | Limits page "reviewed 2026-09-17" | jaggedness page | CONFIRMED |

**Total: 48 quotes checked, 2 differ (rows 9 and 16).**

---

## §2 Everything it can do

**Short answer.** It does three things — pick one of many, rate on ordered levels, give a yes-or-no probability — on text only, many questions at once, hosted in the United States. Anything else people do with it (routing, guardrails, extraction, re-ranking, search, forecasting features) is those three primitives arranged in code.

| # | Capability | How it is invoked (reference only) | Limits and caveats | Source |
|---|---|---|---|---|
| 1 | Choice: one option from a described set | `type: "choice"`, `instructions`, `criteria: {option: description}` → `choice`, `probabilities`, `confidence` | ≤ 255 options | api.md |
| 2 | Score: ordered levels | `type: "score"`, `criteria: [level descriptions]` → `score`, `legend`, `probabilities`, `confidence` | 2–10 levels; "weak in numerical calibration" | api.md; jaggedness |
| 3 | Noul: yes/no probability | `type: "noul"`, optional `criteria: {true, false}` → `noul` (0–1) | no `confidence` field on the answer per the schema returned | api.md |
| 4 | Many questions per call, parallel and isolated | one request, a map of ids → questions, any mix of types | "Adding questions barely changes the response time"; a hard cap on questions per call NOT FOUND | primitives.md |
| 5 | State as text, JSON object or array | `state`: string / object / array | 64k tokens per request, 32k for state plus longest question; a Cloudflare model page shows "32,000 tokens" | models.md; Cloudflare page |
| 6 | Images, audio, video, documents as input | — | none: "Text only. String, JSON object, or array of text values. No image, audio, or video input." | models.md |
| 7 | Structured (JSON) instructions and criteria | instructions, options, levels and noul criteria "accept JSON structure" | wording is the classifier; "Wrong criteria descriptions are catastrophic" in one third-party study (§3.1, 16.7 % vs 25 % random floor) | llms.txt; third-party |
| 8 | Several states in one call ("batching rows") | not a documented feature; the vendor's parallel-questions cookbook batches QUESTIONS, not states | a community integration that packed 40 rows per call saw answers move by slot (0.049 to about 0.42) | cookbook; §3.1 |
| 9 | Async / sync clients | Python `AsyncTypeSafeClient` / `TypeSafeClient`; JS/TS client | streaming NOT FOUND | sdk/python/usage.md |
| 10 | Retries and timeouts | `RetryPolicy(max_retries=3, backoff_max=0.2, timeout=1.0)` | retry on 429 / 529 with backoff is the vendor's advice | usage.md; api.md |
| 11 | Typed response models | Python SDK ≥ 0.7.0 `system_one(..., response_model=…)` (Pydantic) | SDK swapped msgspec → pydantic in 0.7.0 (breaking) | changelog |
| 12 | Confidence | a statistic of the probability distribution: concentrated = high | not an accuracy estimate; "you are never locked into our definition" | confidence.md |
| 13 | Probability semantics | per-option `probabilities` | returned at two decimals (45 distinct values in 360 rows; ties at 0.99) per a third party; independent calibration is mixed (§3.1) | api.md; third-party |
| 14 | Abstention | none built in; the caller adds an "unsure" option to the label set or thresholds `confidence` | third party: with the option available Jev chose "unknown" for 95 % of 300 ambiguous items; without it 79 % picked the dataset's stereotype (second-hand) | confidence.md; awesome list |
| 15 | Determinism controls | none: no seed, temperature or repeat setting in the API reference or the Python usage page | the vendor's consistency cookbook reports per-question probability standard deviation 0.0102 over 15 repeats — small, not zero (the request's `uid` field also changed) | api.md; consistency cookbook |
| 16 | Fine-tuning, examples-in-prompt, custom models | — | NOT FOUND on any page read | all |
| 17 | Evaluation tooling | vendor: `evals.typesafe.ai` (four workflow evals: security incidents, agent-trace observability, invoice processing, customer service); console playground with share links; community `jevcal` fits a per-question threshold to a target accuracy (second-hand) | vendor reference labels are model-generated ("an average of the responses of GPT-6 Astra and Claude Fable 5.1") | evals page; launch post |
| 18 | Cookbooks (vendor) | 18 pages: parallel questions, re-ranking, line-by-line search, structure recovery, function calling (a trading-analytics example), skill suggestion, entity alignment, RAG passage classification, citation check, LLM guardrails, SDE cascade, date extraction, pre-parsed values, hierarchical classification, feature discovery, classification using confidence (SEC filings) | all vendor-authored; numbers are the vendor's | llms.txt |
| 19 | Official SDKs | Python (first release 0.5.7 on 2026-09-14, latest 0.7.1 on 2026-09-21) and JavaScript/TypeScript | two breaking releases in seven days | changelog |
| 20 | Community SDKs | Go, Rust, Java, PHP, Ruby, Elixir, Swift, Scala, .NET, Kotlin and others | second-hand; not vetted | awesome lists |
| 21 | Same interface over other LLMs | official MIT adapter `system-one-adapter-python`: drop-in for `system_one`, runs over OpenAI-compatible providers and native Anthropic; answer modes "probabilities" or "discrete" | 235 stars, 4 open issues on the fetch day; reference only (L15) | github.com/typesafe-ai/system-one-adapter-python |
| 22 | Gateways and routers | Cloudflare page: `env.AI.run('typesafe/jev', …)`, "Third-party" model; Vercel AI Gateway, LiteLLM pre-call hooks, a new-api plugin, a Bifrost feature request — second-hand | version tracking through a gateway is not guaranteed (a third party: "No model version tracking via Gateway") | Cloudflare page; awesome list; §3.1 |
| 23 | Deployment: hosted only | — | "no published weights and no on-prem option"; hosted in the United States; open-weight lookalikes exist but are not this model | TrueFoundry; privacy policy |
| 24 | Access | early access / waitlist ("Try our first System One Model, Jev, in early access.") | a third-party guide says accounts can sign in to the console but need to be let in before API keys work (search summary); not tested | home page |
| 25 | Rate limits | 250,000 tokens/s, 1,200 requests/min | "can change without notice" | models.md |
| 26 | Price | $0.042 per million input tokens; output free | free tier or minimum spend NOT FOUND | models.md |
| 27 | SLA and uptime | none published on the pages read | a third-party status tracker showed 99.854 % over 90 days and 5 minutes' downtime on 2026-09-17, and a press report of demand briefly leaving the API unable to serve users launch week (both search summaries) | search |
| 28 | Status page | link not on the home page navigation; NOT FOUND on vendor pages read | third-party trackers exist | home page |
| 29 | Compliance | DPA and MCA listed; ZDR for enterprise; no training on Input; SOC 2 NOT FOUND; GDPR not mentioned in the privacy policy | see §1 rows 9, 14, 16 | legal.md; privacy policy |
| 30 | Changelog and roadmap | SDK changelog only (four releases); model changelog NOT FOUND; the limits page says "Many of these will be fixed in later versions." | no dates promised | changelog; jaggedness |
| 31 | Agent skill / plugin for coding agents | vendor page "Drop-in skill for Claude Code, Codex, and other agent environments" | NOT installed (L15); irrelevant to Cobalt's runtime | llms.txt |

Reference snippets (nothing was run). A request, built from the schema in row 1–4, with placeholder kinds:

```json
{"model": "jev-1.13.0",
 "state": {"text": "<item text>"},
 "questions": {
  "kind":   {"type": "choice", "instructions": "<what to decide>", "criteria": {"a": "<desc>", "b": "<desc>", "unsure": "<desc>"}},
  "level":  {"type": "score",  "instructions": "<how much>", "criteria": ["<lv1>", "<lv2>", "<lv3>"]},
  "fresh":  {"type": "noul",   "instructions": "<yes/no statement>"}}}
```

The vendor's Python usage page (as returned): `async with AsyncTypeSafeClient() as client: result = await client.system_one(state, questions)`; `TypeSafeClient(retry=RetryPolicy(max_retries=3, backoff_max=0.2, timeout=1.0))`. The SDK reads `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL`, `TYPESAFE_DEFAULT_MODEL` (default `jev-latest`) and logs to the `typesafe_sdk` logger with secrets redacted in debug mode.

**Capabilities tabled: 31.**

**What the vendor's own finance-shaped cookbooks say** (vendor-authored, self-reported):
- *Classification using confidence.* 60 annual reports (Item 1 "Business" only), 75 industry groups. Forced to name a group every time: 39 of 60 right. At confidence ≥ 0.9, "right 90% of the time" (27 of 30); below it, 40 % at group level, 70 % if allowed to answer at the coarser division level; letting it answer coarsely when unsure gave 48 of 60 useful. Stated failures: a company that just sold one of two segments; a startup describing a business it plans to enter. Read as: confidence does sort easy from hard, and a 75-way choice is 65 % right on its own.
- *Function calling.* "plot rolling correlation between nvda and spy for the past month" becomes a typed function call with each argument a closed-set choice; overall confidence is "the least certain judgement in the call". No accuracy figure, no latency figure, no safety warning on the page.
- *SDE cascade.* A cheap model extracts, Jev checks each extracted field with a yes/no, and only flagged items escalate to an expensive model — "up-and-left of every single model" on cost and quality (100 prompts, one dataset; the cost chart is "a historical snapshot").

---

## §3 Who else uses it, with their examples

**Short answer.** After six days there are many trials and demos and no named production customer. The honest list is 24 users, of which only 3 are independent audits; the rest report their own small tests or appear second-hand. Nothing found is a professional trading desk, and nothing found triages trading news in production.

### 3.1 The table

Grades: `vendor-claimed` · `self-reported by the user` (the user's own account of their own trial) · `independent` (a third party measured it on public data with reproducible code) · `unverified mention` (second-hand: a curated list, a search summary, a survey gist). "Read" = the source page was fetched today. Volumes are the users' own.

| # | Who | What they classify | Question types | Volume · latency · accuracy they report | What went wrong (their words) | Grade · read? | Source |
|---|---|---|---|---|---|---|---|
| 1 | `scienthoon` (an individual; repo `jev-ood-calibration`) | 900 rule-generated support tickets, plus three public benchmarks | Choice, Score, Noul | ECE 0.024 / 0.032 / 0.029 on the public sets; **0.107 on the unseen task = 4.4 × the noise floor**; on the unknowable priority label "accuracy was 44.7%" at "0.74" average probability; Choice T = 3.29, Score T = 3.40 (overconfident), Noul T = 0.66 (underconfident); ≈ $0.06 | one task family; possible training contamination on public sets; no model-version tracking through the gateway | independent · read | github.com/scienthoon/jev-ood-calibration |
| 2 | `jourdanlabs` (repo `assay-001`) | Banking intents (Banking77) and CLINC150 | Choice | 8,576 responses; CLINC150 ECE 0.0204 (PASS); Banking77 ECE 0.0936 "systematically overconfident" (FAIL); "zero type errors" (PASS) | pre-registered; "It is not a statement about Jev on any other task, corpus, or day." | independent · read | github.com/jourdanlabs/assay-001 |
| 3 | `yodablocks` (repo `jev-orderby-bench`) | topic membership (20 Newsgroups, 360 rows) and product-query relevance (Amazon ESCI, 306 pairs) | Noul, Score, Choice | topic task passes all six pre-registered gates; ESCI fails four (Noul ECE 0.242 vs gate 0.10); "53 rows tie at 0.99", only 45 distinct values in 360 rows; a 40-row batch moved answers by slot, "0.049 … about 0.42"; batch size 1 restored baseline; rewording moves answers 0.164 on average | two-decimal output "caps the sort key at 101 distinct values" | independent · read | github.com/yodablocks/jev-orderby-bench |
| 4 | Good Start Labs (on Langfuse's blog) | 6,003 rubric checks | yes/no verdicts | Jev matched Claude Fable 5.1's verdict 91.5 % of the time; $160 per million graded answers vs $33,000 for Fable | "It cannot abstain"; "No rationale, when you actually need one"; "Context rot"; production use not stated | self-reported · read | langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals |
| 5 | Emil Lindfors (individual) | 24 Norwegian government consultation responses | 11 questions: 4 Choice, 6 Noul, 1 Score per the fetch tool's tally | stance 20 of 24 (83 %), respondent type 21 of 23 (91 %), ordered scale 19 of 24 (79 %); $0.22 per 1,000 documents; median 0.32 s | "Careful question wording degraded calibration, pushing probabilities toward 0.3–0.7"; a scraper blocked by a firewall; one PDF with no text layer | self-reported · read | lindfors.no/blog/a-first-look-at-typesafes-jev |
| 6 | Near Here (a UK local-events website) | event listings valid vs unsuitable | Noul / Choice | 50 cases: Jev 48 (96 %), Gemini Flash-Lite 43 (86 %), Mistral Small 42 (84 %); $0.043 per 1,000 decisions vs $2.496 and $0.370; median 0.59 s | Jev let 2 of 37 unsuitable listings through; "prompt configurations we selected for prospective production use; this report does not claim they have already been deployed" | self-reported · read | nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation |
| 7 | Classmethod Malaysia (a consultancy engineer) | conversation context into 4 difficulty tiers, to route LLM calls | Choice | 40 calls, all correct; median 0.643–0.674 s; ≈ $0.000025 per call | "Medium tier has lower confidence" (0.57–0.67); "not a comprehensive accuracy benchmark"; not integrated into the router it was for | self-reported · read | dev.classmethod.jp/en/articles/jev-for-llm-model-routing |
| 8 | Rajesh Beri (analyst blog) | phishing emails (2,000, synthetic bodies) | Noul, decomposed | one holistic question: Jev 62.6 % (Haiku 81.3 %); the same task split into five atomic questions combined by logistic regression: Jev 95.0 % (Haiku 93.2 %, p = 0.063); a 5,721-call pre-registered study cost $0.176 | "Wrong criteria descriptions are catastrophic: 16.7%, below the 25% random floor"; "State is data, and jev-1.13 does not treat it as hostile by default" | self-reported · read | beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval |
| 9 | `cristiancolon` (individual; repo `jev-hft`) | news items and Bitcoin order-book text, paper trading only | relevant + directional; higher / lower / flat over 2, 10, 60 s | Jev ≈ 130 ms direct, ≈ 260 ms through a gateway; news cost "cents daily", market data ≈ $3 a day | market-data part "Fails to beat simple order-book imbalance rules over nine-hour runs"; "Jev leans 'down' nearly all the time" (≈ 80 % of short-term answers); for news, "whether that makes money needs real data collected over time" | self-reported · read | github.com/cristiancolon/jev-hft |
| 10 | `buberlo` (individual; repo `jev-trader`) | market regime, direction, toxic flow, liquidity stress, quote environment, inventory pressure | six atomic judgments | state under 400 tokens; 300 ms block deadline; no results published (1 star, 1 commit) | "for research and educational purposes … never disable the risk engine" | self-reported · read | github.com/buberlo/jev-trader |
| 11 | LangChain engineers (two named authors) | model routing; a safety classifier for risky tool calls in an agent | Noul | no sample sizes or accuracy | "Jev isn't a drop-in replacement for an LLM. It doesn't generate text." | self-reported (a guide, not a deployment) · read | langchain.com/blog/building-a-harness-with-jev |
| 12 | Valyu AI (a DEV Community guide) | tutorial: papers screened on four dimensions | Choice, Score, Noul | "well under a cent" for twenty papers; 67.8 % on the vendor's benchmark | "treat these as launch-week artefacts, not production case studies" | self-reported · read | dev.to/valyuai/how-to-use-jev-… |
| 13 | A contributor to NVIDIA-NeMo `Switchyard` (PR #739) | request routing by classification | Choice | ≈ 250–320 ms measured against the real API (issue benchmark ≈ 281 ms) | PR open, not merged; design falls back to a default target on low confidence or error ("fail-open") | self-reported · read | github.com/NVIDIA-NeMo/Switchyard/pull/739 |
| 14 | Jarrod Watts (developer advocate at a blockchain foundation) | buy / sell on an on-chain order book, one decision per 300 ms block | Choice | decisions landing in ≈ 81 ms | sources disagree on paper vs real orders (the survey gist says paper with a dashboard; a search summary says real post-only orders) | unverified mention | x.com / repo `jarrodwatts/jev-trader` (not fetched) |
| 15 | `aowang-ai` (repo `jev-trade`) | long / short, open / close / hold on Hyperliquid, five wallets | Choice | "Real fills", per the survey gist | none stated | unverified mention | gist.github.com/drillan/… |
| 16 | QuantDinger (OpenByteInc) | a pre-trade gate in a crypto / stocks / forex platform | not stated | "11.7k stars" is the platform, not the Jev feature | none stated | unverified mention | gist.github.com/drillan/… |
| 17 | Ryan Vogel (individual) | 1,500 of his own emails: subject, reply requested, queue | not stated | none stated | none stated | unverified mention (search summary of a post the LangChain guide cites) | search |
| 18 | Kyle Jeong (Browserbase) and Browser Use's `jev-ultrafast` | browser-agent action choice | Choice | a flight search in 7.1 s (search summary) | none stated | unverified mention | search; awesome list |
| 19 | Notra (a marketing-analytics platform) | "production GEO platform routing classifiers" | not stated | none | none | unverified mention (a list's description of a company's repo) | awesome-jev |
| 20 | Vercel (`eve` default router, `ai-python`, `fx`, `json-render`, AI Gateway) | agent routing, permission review | not stated | none | none | unverified mention (list entries; Vercel's own pages not read) | awesome-jev |
| 21 | `simonmesmith` | Banking77 intents | Choice | 92.40 % vs a BERT baseline at 93.66 %; $0.44 for the test | none stated | unverified mention (survey gist) | gist |
| 22 | `kyotofin` | IRS tax forms, 261 types | Choice | "100% accuracy", $0.001 per page, "34× cheaper, 6× faster" than a prior LLM | none stated | unverified mention (survey gist; the author's own claim) | gist |
| 23 | Janus (community evaluation) | Banking77 and Web of Science, 500 items each | Choice | a Jev-to-DeepSeek cascade beat either alone on Banking77; on Web of Science it "matched Jev alone at 47% higher cost" | none stated | unverified mention (list entry) | awesome-jev |
| 24 | Sutro (`jev-align`) | rows of CSV / Parquet / JSONL | Choice, Noul | none | "Experimental" | unverified mention (list entry) | awesome-jev |

**Counts: 24 users — 3 independent, 10 self-reported, 11 unverified mentions, 0 vendor-claimed.** Other things the vendor claims (its own workflow evals, the launch post's 193.6× faster and 444.6× cheaper) are vendor-claimed measurements, not users. Not counted as users: open-weight lookalikes (Kev, NanoJev, Laya, jev-local and others — they copy the interface, not the model), commentary sites, and roughly 250 further demo repositories in the community lists.

### 3.2 One paragraph per read user

**The three audits (rows 1–3).** They are the most valuable finding of this pass because they are the only reproducible measurements, and they agree on a pattern: the probabilities are usable on tasks close to what a model has seen (intent labels, topic membership) and unreliable on a task with a hidden rule (Noul underconfident, Choice and Score overconfident by roughly a temperature of 3). None used finance data. Two warn about mechanics that matter to any sorted or batched use: two-decimal output ties, and position effects in packed batches.

**Good Start Labs, Lindfors, Near Here, Classmethod (rows 4–7).** Four small trials with a common shape: a fixed label set, a few dozen to a few thousand items, accuracy in the high 80s to 90s against a reference the author chose, cost and latency two to three orders of magnitude below a frontier model. Each names a limit the vendor also names: no abstain unless built, no rationale, sensitivity to wording. None is in production; Near Here says so plainly.

**Beri (row 8).** The best template for Cobalt's L7: a pre-registered shadow run of 5,721 calls for $0.176, and a result that one holistic question scored 62.6 % while five atomic questions combined in code scored 95 %. It also reports the worst wording failure found (16.7 %, below random).

**jev-hft (row 9).** The only pipeline found that reads news, filings and posts and asks Jev for relevance and direction, then checks the price 30 minutes later. Its honest verdict: comprehension looked right, money unproven, per-second market prediction no better than a plain rule, and a strong "down" bias. That bias is exactly the failure a shadow measurement against his hand labels is built to catch.

**buberlo (row 10) and LangChain (row 11).** Both show the same architecture Cobalt's laws already require — atomic typed judgments over a compact state, thresholds, sizing and vetoes in code, fallback when confidence drops or the service is unavailable — one for a trading bot (which Cobalt never is), one for an agent framework's tool-call gate.

**Valyu and the Switchyard contributor (rows 12–13).** A tutorial that says outright it is not a case study, and an open, unmerged pull request into a large company's routing repository, written by an individual contributor. Neither is an endorsement by that company.

### 3.3 Finance, trading and news-triage users

**Short answer.** There are eight finance-flavoured projects, all hobby, crypto or paper-trading, and none is a professional desk. The closest match to Cobalt — a pipeline reading headlines, filings and posts — exists once, is paper-only, and reports no edge.

| Project | Domain | Grade | Notes |
|---|---|---|---|
| `jev-hft` (row 9) | news, filings, X posts → relevance + direction; Bitcoin order book | self-reported, read | paper only; no edge shown; "down" bias |
| `jev-trader` (`buberlo`, row 10) | crypto market making, six atomic judgments | self-reported, read | no results published |
| `jev-trader` (`jarrodwatts`, row 14) | crypto, on-chain order book | unverified | paper vs real disputed between sources |
| `jev-trade` (`aowang-ai`, row 15) | crypto perpetuals, five wallets | unverified | "Real fills" per one gist |
| QuantDinger (row 16) | crypto / stocks / forex pre-trade gate | unverified | a platform, feature scale unknown |
| `jev_stock` (`sosopop`) | Hong Kong stock direction: up / flat / down | unverified | "HTML reports generated" |
| `jevocks` (`unicodeveloper`) | stock status terminal | unverified | list entry only |
| `Jev X Sentiment Analysis` (`brainstormity`) | crypto tweets to entry ranges | unverified | list entry only |

The survey gist's own conclusions (second-hand, as returned): "Every project gives Jev only typed judgments (Choice/Noul/Score) over compact state; thresholds, risk vetoes, and order placement stay in deterministic code"; two clusters, "low-latency crypto trading exploiting Jev's 70–500 ms latency" and "slower financial classification/forecasting"; "Dry-run/paper-by-default is the norm". Adjacent, non-trading: the vendor's own SEC-filing classification cookbook (§2), and two survey-gist banking-intent and tax-form classifiers (rows 21–22). A search summary also mentions a brand-headline triage run — 384 morning headlines against 15 brands in 24.9 seconds for $0.19 — source not fetched, not a trading use.

News triage in production: none found. Squawk, X-account monitoring for a trader, filing-section tagging by a fund or broker: none found.

### 3.4 Searches that found nothing (or nothing more)

- Customers or design partners named by the vendor: none — the home page (no customers or testimonials), the launch post (none), The Register (no named customers), the docs use-case page ("no named companies, customers, or example organizations").
- Job posts (Ashby board): five or six openings for the vendor's own staff; they name no customer.
- Podcasts, conference talks: nothing surfaced except social posts and one launch-day thread.
- The Hacker News launch thread: its page returned HTTP 429 to the fetch tool, so its comments were not read. Search summaries say it reached about 1,500–1,800 points and 456–480 comments and that the founder answered in it; three commenters were reported as saying they would use it in production. Not verified.
- The vendor's own status page: no link found.
- Package-registry download counts: not reached (one search surfaced a community Python client on PyPI, `jevclient`; counts not read).
- Professional finance users: the three finance-specific searches (trading agent; SEC filings and news sentiment; production use by a team) returned only the projects in §3.3.

---

## §4 The company and vendor risk

**Short answer.** A two-year-old, three-founder company with a $40M seed led by a known venture firm, hiring, five days into a public launch, shipping breaking changes weekly. For a one-person trading shop the risks are age, version churn, no on-prem path and no published exit, not the price.

**Facts from pages fetched today.**
- **Team page** (as returned): Diogo Almeida, CEO — "co-invented RLHF and InstructGPT, the methods that lead to ChatGPT and GPT4. Previously, he was at Google Brain." Sasha Sheng, COO — "ex-research engineer from Meta/FAIR". Erik Gafni, CTO — "repeat founder (Ravel, multi-modal AI for dna-sequencing), an early employee at two unicorns (Invitae and Freenome)". Backers: "top-tier investors" — none named on that page. Five-day in-person work rule at a San Francisco office. Motto "Build Prod, Not God".
- **Press-release copy on a finance portal** (as returned): "$40 million in seed funding led by DCVC"; "Founded in 2024"; the product "currently available in early access for select developers", waitlist on the site. A DCVC general partner is quoted; co-investors are not named there. The first pass's unverified items — co-founder names, founding year, lead investor — are now verified from these two pages. A second copy of the release returned HTTP 403.
- **Product age:** public launch 2026-09-15 / 16; the Python SDK's first public release is dated 2026-09-14 (changelog); the terms page updated 2026-09-19; the limits page reviewed 2026-09-17.
- **Churn:** SDK 0.5.7 (09-14) → 0.6.0 (09-15, breaking: `Score.criteria` becomes an ordered list) → 0.7.0 (09-18, breaking: serialiser change, new `response_model`) → 0.7.1 (09-21). The vendor's SDE cascade cookbook names `jev-1.12` and the models page names `jev-1.13.0` with no release date.
- **Capacity signals:** the limits page says rate limits "are adjusting dynamically" because of "a very large volume of demand"; a press report of launch-week overload and a 90-day availability figure of 99.854 % come from search summaries only.

**Risk signals for a one-person shop (statements of fact, no recommendation).**
- *Runway:* $40M seed, hiring for engineering, marketing and recruiting; runway itself is unpublished.
- *Lock-in:* the question definitions are plain JSON (choice / score / noul with descriptions). They can be exported by Cobalt's own store in a neutral form, and the vendor's own adapter shows the same set runs over other LLMs. What does not transfer: the probabilities and every threshold tuned on them; a third party found no version tracking through a gateway.
- *Export of your own question definitions:* the vendor keeps none unless the console saves them — NOT KNOWN; Cobalt would keep its own copy (L10) regardless.
- *Data:* DPA, MCA and ZDR-for-enterprise exist by name; their text was not read; whether ZDR is offered to a single-user account is NOT KNOWN.
- *Exit path:* no self-host; hosted in the United States; open-weight lookalikes exist but do not reproduce the model's behaviour.

---

## §5 Eight worked question sets for Cobalt, product against local model

**Short answer.** Each set below is a small closed list of typed questions over text or bucketed facts, a ruled table in code that turns the answers into something the card can use, and a shadow measurement against his own hand label. Labels are by KIND only — no ticker, number, threshold or note of his appears (L32); where his own list is needed, the set says "his list, loaded from the vault".

**Conventions for all eight.**
- *Product form:* the vendor's request shape (§2). *Local form:* a Pydantic model with `Literal` fields, given to the local model through the schema-constrained endpoint (LM Studio enforces a JSON schema; for MLX models it uses Outlines — first pass §7). It returns labels and `reasons`, no calibrated per-option probability. Whether the local runtime can return per-token log-probabilities that would give one is NOT KNOWN (§6).
- *Numbers:* deterministic code buckets every number into a word first (first-pass question 9); no model ever sees a raw computed value; no model emits a number that reaches a dot (L52).
- *Abstain:* every Choice carries an `unsure` option; below a floor set in settings (L53), the record is `unsure`. Nothing turns `unsure` into an answer.
- *Record:* question hash, input, request, raw response, model id as reported, lane, degraded flag, time (L57); shadow role only (L7).
- *Shadow measurement, common to all:* per-label agreement with his hand label, a confusion matrix, per-label n, "insufficient data" under 30 (L8), abstain rate, coverage at the floor, agreement between lanes, and a paraphrase-stability check (the same question reworded, answers must not move beyond a bound the tribunal sets — the third-party studies found 0.164 average movement on rewording and catastrophic failures on wrong descriptions). A question-text change is a new classifier and resets its count (L10).
- *Order of events:* a label is computed on an EVENT and stored; the scan reads the stored label (L2).

### S1 — News / X / squawk triage (map row 9)

Question set: `relevance` Choice {a watched name, market-wide, sector-wide, not relevant, unsure} · `urgency` Score {background, routine, notable, act-now} · `duplicate` Noul ("this restates something already in the last items"). Placeholders for wording only.
- *Deterministic inputs:* the item text trimmed by code (length cap, source kind, timestamp), the watched-name list resolved by string match first (rules before model, first-pass §7.3), the list of the last N item hashes for the duplicate test.
- *What code does:* a ruled table maps (`relevance`, `urgency`) to a surface — queue, digest line, or drop. It never grades, ranks or admits a name to a pool (map rows 1, 7).
- *Shadow:* his keep / dismiss taps on surfaced items are the hand label; measure per label agreement, and the drop rate against items he later opened. Injection control set: headlines carrying an instruction, run in shadow (the vendor states its model can be steered by "text that argues for its own classification").
- *Local form:* `class Triage(BaseModel): relevance: Literal[...]; urgency: Literal[...]; duplicate: bool; reasons: list[str]` with each reason quoting a span of the input; a validator rejects a span not present in the text.

### S2 — Catalyst kind, materiality and freshness for a headline (map row 10; feeds row 5 dot and row 3)

Question set: `kind` Choice over the common event kinds (offering, results / guidance, trial or regulator news, deal, contract, management change, other real event, no new information) — his own catalyst list replaces these from the vault · `materiality` Score, four described levels · `is_new` Noul.
- *Deterministic inputs:* the headline and lead sentence; source kind; time since first sighting (bucketed into words by code); whether the name is on the watched list.
- *What code does:* a ruled table (his, dated, in git) maps (`kind`, `materiality`) to the catalyst dot's label, and only a separate ruled table maps that label to a grade. The model picks neither table and emits no grade (map row 5: it enters as a judgment-tier shadow dot, `scoring.py:97-98`). Grade tables are DEFAULT_UNRULED today; nothing here revives one.
- *Shadow:* his catalyst-dot tap is the hand label. Report agreement on `kind`, and on the ordered `materiality` as a weighted difference, per label with n. The rare kinds will sit under 30 for weeks — expected, not worked around (L8).
- *Local form:* `Literal` for `kind`, an integer-free `Literal["irrelevant","minor","notable","day-defining"]` for materiality, `is_new: bool`, `reasons` as quoted spans.

### S3 — Market and sector alignment as a label, not a grade (map row 5)

Question set: `alignment` Choice {with, flat, against, unsure} asked twice with different bucketed contexts (market, sector) · `regime_clear` Noul.
- *Deterministic inputs:* only bucketed words produced by code from the context feeds already computed (trend up / down / flat, strength low / normal / high, day-phase word). No raw number reaches the model.
- *What code does:* the label goes to the dot as a shadow judgment; the label → grade map is the unruled default ESCALATE 4 of the S2 plan and stays his to rule. Until then the dot stays `DEFAULT_UNRULED` and this only records what the model would have said.
- *Shadow:* his tap on the two dots; agreement per label; a check that the answer does not change when bucket order in the input is shuffled (the vendor's limits page: it cannot judge nearness or order reliably).
- *Local form:* same three-label enum; `reasons` must name input keys and validation rejects unknown keys (first pass §3 C).

### S4 — The unknown catalyst inside setup formation (map row 3)

Question set: `catalyst_present` Noul + `catalyst_kind` Choice (as S2) + `unsure` handled in code.
- *Deterministic inputs:* the stored S2 label for the name's newest items in the look-back window (already computed at event time); item age in words.
- *What code does:* the formation predicate stays three-valued and deterministic. The model never runs in the scan; the scan reads the stored label. Today the answer is `not_evaluable`; a shadow label would be shown beside it, never substituted (map row 3; L2; `evaluate.py:25-27` per the first pass).
- *Shadow:* a paired count: how often the stored label would have flipped `not_evaluable` to formed / not formed, and whether he agreed on cards where he tapped. Nothing changes the evaluator until an L7 run and his approval.
- *Local form:* reuse S2's model; only the read-side changes.

### S5 — DM or voice sentence to handler (map row 23)

Question set: `handler` Choice {registered skill, instant answer, headless session, unknown} · `skill` Choice over an enum generated from the skill registry (L16), only asked when `handler` is a skill · `is_trading_logic` Noul ("this asks to change a rule, setting or position").
- *Deterministic inputs:* the transcribed sentence; the registry's skill ids and one-line descriptions.
- *What code does:* `unknown` asks him to rephrase; `is_trading_logic` above the floor forces the HITL path regardless of `handler` (CLAUDE.md, L7, L37); no label executes anything. A skill id not in the registry fails validation, loud.
- *Shadow:* he keeps using the current router; the classifier runs silently; measure per-handler agreement with what he actually got and how often he re-asked.
- *Local form:* first choice by the requirement itself ("small local router model", fully local for voice): `handler: Literal[...]; skill: Literal[<enum from registry>] | None; is_trading_logic: bool`. The hosted product is a bake-off candidate only if local latency is too slow for the sub-second aim (requirements 218–219 per the first pass).

### S6 — Journaling: mistake and tag proposals from a trade note (map row 19)

Question set: one `Noul` per tag in his taxonomy ("this note describes <tag>") — the vendor's fan-out pattern — plus `note_kind` Choice {plan, execution, emotion, other}.
- *Deterministic inputs:* the note text only. His tag list is loaded from the vault at run time and is user data (L32): with the product it leaves the machine on every call (L17 opt-out default — his choice); with the local model it does not.
- *What code does:* tags above a floor are PROPOSED for him to confirm; a proposed tag never counts in a statistic and is never written as his (map row 19; L28).
- *Shadow:* his confirm / reject taps; precision per tag with n; a per-tag calibration bin only when n allows. Per-tag Noul answers may be underconfident (one audit found Noul T = 0.66), so the floor is set per tag, not globally.
- *Local form:* `class Tags(BaseModel): tags: list[Literal[<his tag enum>]]; evidence: dict[tag, quoted span]` — the local lane is the default because of the data exposure.

### S7 — Filing-section flags and dilution instruments (map row 14)

Question set: `section_kind` Choice {risk factors, use of proceeds, dilution terms, results discussion, other} · `instrument_present` Choice {common, warrants, convertible, preferred, none, unsure} · `verbatim_needed` Noul.
- *Deterministic inputs:* the filing section text after a rule pass by form type and headings; the token count.
- *What code does:* nothing numeric comes from the model. A figure needs a verbatim quote from the section (CLAUDE.md), which the product cannot produce (it generates no text) — so the product can only TAG and code fetches the span; the extraction path stays the local model with schema and quote validation.
- *Shadow:* his spot checks on a sample; per-label agreement; batch minutes are fine (event lane).
- *Local form:* the ruled lane: `flags: list[Flag]` where each `Flag` has `kind`, `quote: str` and a validator that the quote is a substring of the section; three failures escalate a tier (CLAUDE.md 3-tries).

### S8 — "Why is this ticker moving?" candidate picker (map row 11)

Question set: `cause` Choice over ONLY the candidates the deterministic resolver found, plus {none of these, unsure} · `single_cause` Noul.
- *Deterministic inputs:* the resolver's ranked candidate list with their source items; item ages in words.
- *What code does:* the paragraph is composed by the local model from the picked candidate's source item; a cause outside the candidate list cannot be selected because the enum is built per call from the list (map row 11; L52 not touched).
- *Shadow:* his agreement per candidate class; how often `none of these` fires (an honest coverage number for the resolver itself).
- *Local form:* `cause: Literal[<per-call enum>, "none", "unsure"]`.

**Next in line, not written up:** ops day-open log triage (row 27: green / amber / red per check with the cited log line, local lane, zero trading exposure — the cheapest first proof of the whole seam), chief-of-staff agent routing (row 24) and task-class labelling for model routing (row 25).

**Question sets: 8.**

**Compared like for like.** Because both forms are generated from one neutral definition (kind, options, descriptions, floor), the same items and the same hand labels score the two lanes side by side; the tribunal reads a per-site table: agreement with his label per label with n, abstain rate, latency, cost, and whether reasons were available.

---

## §6 What is still not known

**Short answer.** Several things a tribunal must not assume are still unknown, and most could be settled in one short, cheap, approved hands-on trial. Nothing has been run; this list says what a trial would settle and what it never can.

**Not known, and settled by a 30-minute trial with his approval** (sign-up, one key, a few dollars at most; needs his L27 / L17 ruling first; the run would use invented placeholder text, never his data):
1. Whether an account is let in at once or waits on the waitlist, and what a key requires.
2. Whether the same request repeated ten times returns identical probabilities, and how much they move (the vendor's own cookbook shows a small non-zero spread).
3. Whether two-decimal probabilities are what the live API returns (a third party reports so).
4. Whether a batch of many questions changes answers to each (the vendor claims "in isolation"), and what happens at 30 or 60 questions.
5. Whether the reported model id in a response matches the requested alias, and what a pinned id does when that version is retired.
6. Latency from this host to the API, measured (the vendor's 70–500 ms; a third party reports ~430 ms from one region).
7. What a rejected or failed request looks like on the wire (422 body, 429 headers).
8. Whether a fixed set of injected instructions in a headline moves an answer, on invented text.

**Not known, and NOT settled by a trial:**
1. Accuracy and calibration on financial and trading text; only his labelled history can answer (§5 shadow).
2. Any professional production use; none found, and a trial does not create one.
3. The DPA's actual terms, subprocessors, retention length, and whether ZDR is offered to a single-user account (needs the documents or the vendor's answer). A guessed URL for the DPA returned 404.
4. Whether "the Site" in the terms includes the API.
5. SOC 2 status, an SLA, a deprecation policy, uptime over months; none published.
6. The company's runway and its behaviour when a model version is retired.
7. Whether the local runtime returns per-token log-probabilities (settled by a local, no-cost check with his approval, not a vendor trial).
8. How the local model's option-picking compares with the product's on Cobalt's own text — settled only by the shadow bake-off.
9. The Hacker News launch thread's actual content (rate-limited to the fetch tool; a browser read would settle it).
10. Whether the vendor holds question definitions server-side.

---

## §7 Additions to the tribunal's question list

**Short answer.** Eight new questions, none repeating the first pass's ten. Each is answerable ADOPT, ADOPT WITH (conditions) or REJECT, and each traces to a fact found in this pass.

1. **Wording as a tested artifact.** Adopt a rule that a question set passes a paraphrase-stability test and a wrong-description test on stored items before its shadow run starts, in addition to the hash and reset (first-pass 10). *Basis:* one audit measured 0.164 average movement on reworded questions; another measured a wrong description falling to 16.7 %, below the random floor. ADOPT WITH: the bound on movement is set by the tribunal.
2. **Decompose, and let code combine.** Adopt "several atomic questions combined by ruled code" over "one holistic question" wherever a label feeds a dot. *Basis:* one holistic question 62.6 % against five atomic ones 95.0 % in the same study; the vendor's own composite-scoring pattern. ADOPT WITH: the combining weights are ruled settings, and the atomic answers are stored (L57).
3. **A model probability is never a sort key, a tie-break or a threshold by itself.** *Basis:* two-decimal output ties (53 of 360 rows at 0.99) and Noul-versus-Choice miscalibration of opposite sign. ADOPT.
4. **Floors are per question, per type and per model version.** Adopt: no single global confidence floor; each question's floor is fitted on his labels and expires on a version change. *Basis:* one audit found Choice and Score overconfident and Noul underconfident on identical inputs. ADOPT WITH: fitting is offline, deterministic, and its output a ruled setting (L53).
5. **One item per call unless batch-invariance is proven.** *Basis:* a 40-row batch shifted answers by slot in a third-party study. ADOPT WITH: a batch-invariance test on his data before any packing.
6. **The door is part of the lane.** Adopt: the record stores which path answered (vendor direct, a gateway, the local model), thresholds are tuned only on a pinned id through one path, and a gateway path is admitted only if it reports the model id. *Basis:* "No model version tracking via Gateway" in one audit; the product is offered through gateways whose terms and data paths were not read. ADOPT WITH.
7. **Untrusted text is data, and a control set proves it.** Adopt: every text-triage question set ships with an injection control set (items that argue for their own label) and must show no movement beyond a bound before shadow. *Basis:* the vendor's limits page ("text that argues for its own classification, can move the answer") and its own RAG-passage cookbook. ADOPT WITH.
8. **Settle the unknowns first, or design around them.** Adopt: the tribunal receives §6's trial results (or an explicit "no trial") before ruling on admitting the product to any bake-off; if no trial is approved, the design must not depend on determinism, on a DPA term, or on a reported model id. ADOPT WITH: the trial's ruling belongs to him (L27, L17).

---

## §8 Sources

All fetched 2026-09-21 by this seat. **Fetches: 45 of 45 (three returned no content: HTTP 429, 403, 404). Searches: 15 of 20.** Local reads: 6 of 25 (prompt file, first-pass document, its report, `LAWS.md` in two parts, `src/cobalt/cards/scoring.py` lines 1–120).

**Fetches, in order (F = the job it served; 1 verify, 2 capabilities, 3 users, 4 company).**

| # | F | URL | What it gave |
|---|---|---|---|
| 1 | 1 | docs.typesafe.ai/models.md | price, rate limits, limits, aliases, text-only |
| 2 | 1 | typesafe.ai/legal/privacy-policy | no training, retention, hosting |
| 3 | 1 | typesafe.ai/legal/terms | entity, "Site" scope, date |
| 4 | 1 | docs.typesafe.ai/model-jaggedness/jev-1.13.md | known limits, reviewed 2026-09-17 |
| 5 | 1 | docs.typesafe.ai/confidence.md | confidence definition, thresholds |
| 6 | 1 | docs.typesafe.ai/api.md | schema, errors, 255 options |
| 7 | 1 | typesafe.ai/ | RLCD, price, demo, no customers, nav links |
| 8 | 1 | theregister.com/ai-and-ml/2026/09/16/…/5296711 | funding, CEO, latency, caveat |
| 9 | 1 | truefoundry.com/blog/typesafe-ai-jev | independent scepticism, 09-18 |
| 10 | 1 | docs.typesafe.ai/patterns/composite-scoring.md | pattern sentence |
| 11 | 2 | docs.typesafe.ai/llms.txt | full docs index, cookbook list |
| 12 | 2 | typesafe.ai/blog/introducing-system-one-models-and-jev | launch claims, links |
| 13 | 2 | docs.typesafe.ai/concepts/use-case-map.md | use cases by industry; no customers |
| 14 | 2 | docs.typesafe.ai/cookbooks/classification_using_confidence.md | SEC 10-K numbers |
| 15 | 2 | docs.typesafe.ai/cookbooks/function_calling.md | trading-analytics example |
| 16 | 2 | docs.typesafe.ai/cookbooks/consistency_noul_cookbook.md | repeat-call variability |
| 17 | 2 | evals.typesafe.ai/ | vendor workflow evals |
| 18 | 2 | docs.typesafe.ai/primitives.md | multi-question guidance |
| 19 | 2 | docs.typesafe.ai/sdk/python/usage.md | async, retries, env vars |
| 20 | 2 | github.com/typesafe-ai/system-one-adapter-python | official adapter over other LLMs |
| 21 | 2 | docs.typesafe.ai/sdk/python/changelog.md | releases and dates |
| 22 | 2 | docs.typesafe.ai/cookbooks/sde_cascade.md | cascade example |
| 23 | 3 | langfuse.com/blog/2026-09-18-using-typesafes-jev-for-evals | Good Start Labs, 6,003 checks |
| 24 | 3 | langchain.com/blog/building-a-harness-with-jev | routing and tool-call gate |
| 25 | 3 | news.ycombinator.com/item?id=49767192 | HTTP 429, nothing obtained |
| 26 | 3 | github.com/yibie/awesome-jev | community list (297 entries as returned) |
| 27 | 3 | dev.to/valyuai/how-to-use-jev-a-practical-guide-… | tutorial |
| 28 | 3 | github.com/AbdelStark/awesome-typesafe-jev | second list, independent-evaluation index |
| 29 | 3 | gist.github.com/drillan/6916b16e8ea31a8ec36c8f59d6483150 | finance and trading survey |
| 30 | 3 | github.com/cristiancolon/jev-hft | news + order-book pipeline |
| 31 | 3 | developers.cloudflare.com/ai/models/typesafe/jev/ | gateway listing |
| 32 | 3 | github.com/NVIDIA-NeMo/Switchyard/pull/739 | open routing PR |
| 33 | 3 | github.com/scienthoon/jev-ood-calibration | independent calibration |
| 34 | 3 | github.com/yodablocks/jev-orderby-bench | ties, batching, ESCI |
| 35 | 3 | dev.classmethod.jp/en/articles/jev-for-llm-model-routing/ | 40-call routing test |
| 36 | 3 | github.com/jourdanlabs/assay-001 | pre-registered verification |
| 37 | 3 | lindfors.no/blog/a-first-look-at-typesafes-jev | early-access trial |
| 38 | 4 | typesafe.ai/team | founders |
| 39 | 4 | morningstar.com/…/20260915525333/… | HTTP 403 |
| 40 | 4 | docs.typesafe.ai/legal.md | DPA, MCA, ZDR named |
| 41 | 4 | finance.yahoo.com/technology/ai/articles/typesafe-ai-emerges-stealth-40m-190000776.html | DCVC, founded 2024 |
| 42 | 4 | docs.typesafe.ai/legal/data-processing-agreement.md | HTTP 404 (guessed URL) |
| 43 | 3 | github.com/buberlo/jev-trader | six atomic judgments |
| 44 | 3 | beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval | 62.6 % vs 95 % |
| 45 | 3 | nearhere.events/blog/typesafe-jev-mistral-gemini-event-validation | 50-case validation |

Fetch split by job: verify 10 · capabilities 12 · users 18 (rows 23–37 and 43–45, incl. the 429) · company 5 (rows 38–42, incl. the 403, the 404 and the legal page); total 45. Users and company ran over their per-job caps of 15 and 4; the hard total held (see the run report's ESCALATE).

**Searches (generic terms plus the product's public name; a few queries carried public project or person names that the LangChain guide itself cites; nothing of his).**
1. `TypeSafe AI Jev System One model customers`
2. `Jev TypeSafe Hacker News discussion`
3. `"typesafe-sdk" Jev github`
4. `TypeSafe AI Jev review tried classification confidence`
5. `Diogo Almeida TypeSafe AI founders seed funding investors`
6. `Jev TypeSafe stock trading agent classification headlines`
7. `Jev TypeSafe SEC filings earnings news sentiment financial classification`
8. `Jev TypeSafe calibration audit independent overconfident results`
9. `TypeSafe Jev in production our team switched routing classifier`
10. `Jarrod Watts trading agent Jev`
11. `TypeSafe AI hiring jobs Ashby Jev customers design partners`
12. `TypeSafe Jev API outage rate limit 429 early access problems developers`
13. `TypeSafe AI enterprise SOC 2 data processing agreement zero data retention Jev`
14. `Jev TypeSafe launch thread comments engineers tried production accuracy skeptic`
15. `Jev TypeSafe email triage news triage Ryan Vogel Kyle Jeong browser agents production`

**Only in search summaries, never fetched (treat as unverified):** the launch-thread scores and commenter count; the launch-week overload report; the third-party availability figure; the "384 headlines" brand run; the Zurich-to-London search timing; Ryan Vogel's 1,500 emails; the claim that ZDR exists (later confirmed by fetch #40); the account-gating description. Other sources that appeared only as search hits and were not read: the vendor blog posts "bitterest lesson" and the manifesto, Tom's Hardware, Latent Space, DataCamp, MarkTechPost, Kingy AI, Colin McNamara, explainx.ai, several independent audits by name (`jev-calibration-audit`, `jev-cyrillic-audit`, `jev-sec-bench`, `JevBench`, `jev-measured`) — those exist per the awesome lists and were not opened.

Local files cited: `src/cobalt/cards/scoring.py` (lines 1–120: desk factors, `DESK_NA`, `DEFAULT_UNRULED`, `tier` and `role` fields) · the first-pass document and report · `LAWS.md` (L1, L2, L5, L7, L8, L10, L15, L17, L23, L25, L26, L27, L32, L37, L52, L53, L57, L74).
