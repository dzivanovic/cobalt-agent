# Typed classifiers for Cobalt — research input for a tribunal (2026-09-21)

Ordered `cto-2026-09-21.md` R31; widened 15:00 ET to the whole project. INPUT to a four-house tribunal (L67). It proposes no design, builds nothing, recommends no purchase.

**How to read the quotes.** Every quoted figure carries its URL. The quotes were extracted through a fetch tool that passes the page through a small model, so they are "verbatim as returned"; a house relying on a number re-opens the URL first. NOT FOUND = looked for on the pages read, absent. NOT KNOWN = nobody has published it. Nothing here was run: no sign-up, no key, no call.

---

## §0 One-page answer

**What it is.** The site sells a hosted model called Jev, from a San Francisco start-up, launched publicly on 2026-09-16 — five days before this document. You send it a block of content ("state") plus a set of typed questions — pick one of these options, rate on these levels, yes or no — and it returns the answer with a probability for every option and a confidence figure, not text. "Type-safe" there means the answer's shape is fixed by the question, so code can branch on it without parsing prose.

**Three best uses for Cobalt** (all event-driven, all in shadow first):
1. Triage of incoming text — headlines, X posts, filing sections: catalyst kind, relevance, urgency, with "unsure" as a first-class result.
2. The gaps Cobalt already marks as unknown — the desk-graded card dots that are N/A today (`src/cobalt/cards/scoring.py:20-24`) and the "unknown catalyst" that makes a definition not evaluable (`src/cobalt/radar/evaluate.py:25-27`).
3. Cheap routing — a DM or voice sentence to the right handler; a task to the right model tier — in front of the expensive models.

**Three hardest limits.**
1. Hosted only, closed weights, not the chat-completions shape: it cannot run locally (L23) and is not a drop-in behind the routing layer (L5); and it is a new vendor and a new meter (L27).
2. Its own documentation says it is unreliable with numbers, dates, counting and nearness — so it cannot look at Cobalt's computed features as numbers — and it returns no reasons, because it does not generate text.
3. No independent accuracy or calibration evidence exists yet; every benchmark is the vendor's own, and determinism controls are NOT FOUND in its API.

**What a tribunal would have to decide.** Whether Cobalt adopts the PATTERN (typed question in, typed answer with probabilities and an abstain out, stored and replayable) independently of the PRODUCT; which of the classification sites in §5 get one, all in shadow; and whether the product is worth a bake-off against the models Cobalt already routes to, given it needs a spend and data-exposure ruling first.

---

## §1 What it is

**Short answer.** A closed, hosted decision model with its own API — not a schema-validation library, not a code-generation agent, and not a small classifier you train. The vendor calls the class "System One models"; the first and only model is Jev.

- **Maker.** "TypeSafe AI, Inc., located at 255 California St, Suite 1300, San Francisco, CA 94117" (https://typesafe.ai/legal/terms). CEO Diogo Almeida, a former OpenAI researcher (https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711). Two further co-founders, a 2024 founding date and a lead investor appear only in a search-result summary of a press release that was not fetched — treat as unverified.
- **Funding.** "$40 million in funding" (The Register, same URL).
- **What "type-safe" means there.** "Typed outputs that software can act on" (https://typesafe.ai/). The docs: "You get typed values and probability distributions that your code can branch on, sort by, and route with." (https://docs.typesafe.ai/).
- **The model.** "We're building with a new architecture, a new sampler, and a new training algorithm: Reinforcement Learning for Calibrated Decisions (RLCD)." (https://typesafe.ai/). Parameter count, base model and training data: NOT FOUND.
- **Hosted vs self-hosted, open vs closed.** Hosted API only. Independent write-up: "There are no published weights and no on-prem option today." (https://www.truefoundry.com/blog/typesafe-ai-jev).
- **Availability — sources disagree.** The vendor's quickstart says "Get your API key from the dashboard" (https://docs.typesafe.ai/introduction/quickstart.md). The independent write-up says it is "currently behind an early-access waitlist" (TrueFoundry URL above). Not tested — no sign-up was allowed in this run.
- **Maturity.** Announced 2026-09-16 (The Register). One model version, `jev-1.13.0`. Python and JavaScript SDKs with changelogs (not read). Production users, uptime history, SLA: NOT FOUND. Terms page "Last updated Sep 19, 2026"; privacy policy "Last updated Nov 19, 2025".
- **Independent scepticism.** "Still unknown: performance on public benchmarks, behaviour on tasks that aren't cleanly decision-shaped, accuracy on domain-specific work in someone else's hands" (TrueFoundry). The Register calls the vendor's "hallucination-free" claim not "a fair comparison as its output is not natural language".

---

## §2 How it is used

**Short answer.** One HTTPS POST carries the content and a named map of questions; one JSON response carries a typed answer per question, with probabilities. There are exactly three question types.

| Item | Fact | Source |
|---|---|---|
| Endpoint | `POST https://api.typesafe.ai/v1/systemone`, header `Authorization: Bearer <API_KEY>` | https://docs.typesafe.ai/api.md |
| Request | `state` (string, object or array) · `model` · `questions` (map of id → question) | same |
| Question types | `choice` (one option from a described set) · `score` (ordered described levels, 2–10) · `noul` (yes/no as a 0–1 probability) | same; https://docs.typesafe.ai/llms.txt |
| How labels are declared | Choice: a map of option → description. Score: a list of level descriptions. Noul: optional descriptions of true and false. Descriptions are plain language or JSON. | api.md |
| Answer | Choice: `choice`, `probabilities`, `confidence`. Score: `score`, `legend`, `probabilities`, `confidence`. Noul: `noul`. Plus `model` (the versioned id that answered) and `usage`. | api.md |
| Confidence | "confidence is a statistic computed from the probability distribution" — concentration of the distribution, 0 to 1. It is NOT a separate accuracy estimate. | https://docs.typesafe.ai/confidence.md |
| Abstention | No refusal type. Abstaining is the caller's code: low confidence → "Model is genuinely unsure. Don't guess." Thresholds: "Start with conservative thresholds, test with your own data, and adjust." | confidence.md |
| Batch | Many questions per call: "Every question is evaluated in parallel and in isolation against the same state in one go." Many states per call: NOT FOUND. | https://docs.typesafe.ai/ |
| Limits | "64k tokens per request; 32k tokens for `state` plus the longest question". Up to 255 options per Choice (third-party: TrueFoundry). | https://docs.typesafe.ai/models.md |
| Latency (vendor claims) | "70ms-500ms, 40x-200x faster than traditional LLMs" (as reported by The Register). Home-page demo: "Completed in 0.114s". Independent measurement: NONE FOUND. | URLs above |
| Price | "$0.042 / MTok for input and $0 for output" (The Register, quoting the vendor); models page: "Output tokens are free." | URLs above |
| Rate limits | "250,000 tokens per second / 1,200 requests per minute." — and they "can change without notice". | models.md |
| Errors | 401, 422 (validation), 429 (rate limit), 529 (overloaded); retry "with exponential backoff". | api.md |
| Version pinning | `jev-latest` and `jev-preview` are aliases; "If you have tuned confidence thresholds against a specific version, pin that version's ID instead of the alias." Deprecation policy: NOT FOUND. | models.md |
| Determinism | Seed, temperature or any repeatability setting: NOT FOUND in the API reference. Whether the same input returns the same probabilities: NOT KNOWN. | api.md |
| Training on your data | "will not train or fine tune any artificial intelligence or machine learning models on your prompts or other Input" | https://typesafe.ai/legal/privacy-policy |
| Retention | "as long as reasonably necessary to provide you with the Services, or otherwise in support of our business" — no fixed period. | same |
| Location, sharing | "The Services are hosted in the United States"; data goes to "vendors and service providers that help us provide the Services". | same |
| API-specific terms, DPA, zero-retention option | NOT FOUND. The site terms say: "Do not submit any information or other materials that you consider confidential or proprietary through the Site." Whether "the Site" includes the API is NOT KNOWN. | https://typesafe.ai/legal/terms |

The vendor's own Python quickstart, trimmed (reference only, L15 — nothing was installed or run):

```python
from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
client = TypeSafeClient()                      # key from env TYPESAFE_API_KEY
response = client.system_one(
    state=ticket,
    questions={
        "department": Choice(instructions="Which team should handle this",
                             criteria={"billing": "Payment or subscription issues",
                                       "technical": "Bugs or integration problems"}),
        "is_urgent": Noul(instructions="The message conveys urgency or time-sensitivity"),
    },
)
print(response.answers["department"].choice)   # "technical"
print(response.answers["is_urgent"].noul)      # 1.0
```

---

## §3 Worked examples

**Short answer.** Examples A, B and E are written in the product's documented request shape; C and D use the generic typed pattern with Pydantic on a routed model, because the product cannot do what they need. All were CONSTRUCTED for this document and none was run; tickers and labels are placeholders.

**A — headline → catalyst kind, materiality, freshness (product shape).** Three questions in one call; the abstain is code.

```json
{"model": "jev-1.13.0",
 "state": {"headline": "XYZ prices $50M registered direct offering", "source_kind": "wire"},
 "questions": {
  "kind": {"type": "choice", "instructions": "What kind of event is this for the stock",
    "criteria": {"offering": "Company sells or registers new shares",
                 "earnings": "Results or guidance", "clinical": "Trial or regulator news",
                 "other": "A real event of another kind", "noise": "No new information"}},
  "materiality": {"type": "score", "instructions": "How much this changes the stock's day",
    "criteria": ["Irrelevant", "Minor", "Notable", "Day-defining"]},
  "is_new": {"type": "noul", "instructions": "This reports something not previously public"}}}
```
Code then applies: `if answers.kind.confidence < floor: label = UNSURE` — `floor` is a settings value, never a literal.

**B — free-text trade note → mistake tags (product shape).** Choice is single-select, so a multi-tag taxonomy becomes one Noul per tag in one call (the vendor's "fan-out" pattern: "Send many questions in a single call, including speculative ones, and let your code decide what's relevant."). Each tag comes back as a probability; code proposes tags above a floor and he confirms. The tag list is user data (L32) and is sent with every call — see §6.

**C — computed features → context label, with reasons (generic pattern, NOT the product).** The product is the wrong tool twice here: its docs say it "cannot reliably judge whether two values are near each other" and "reads dates as text, not as ordered quantities" (https://docs.typesafe.ai/model-jaggedness/jev-1.13.md), and it returns no reasons. So deterministic code first turns every number into a word bucket, and a routed model with a schema picks the label:

```python
class ContextInput(BaseModel):          # built by a deterministic collector; numbers already bucketed
    rvol_bucket: Literal["low", "normal", "high", "extreme"]
    gap_bucket: Literal["none", "small", "large"]
    trend_htf: Literal["up", "down", "flat"]

class ContextLabel(BaseModel):
    label: Literal["context_a", "context_b", "context_c", "unsure"]
    reasons: list[Reason]               # each Reason names an input key; validator rejects unknown keys
    # no numeric field at all: the model never emits a number that reaches a score
```
A reason that cites a key not in `ContextInput` fails validation → loud FAILED (L1), never a default label.

**D — DM or voice sentence → handler (generic pattern, local model).** `Literal["skill", "instant_answer", "headless_session", "unknown"]` plus the skill id from an enum generated from the registry. `unknown` asks him to rephrase; it never guesses a skill.

**E — his scoring example, in the product's own "composite scoring" pattern.** The vendor's advice: "Break a complex judgment into atomic scores, combine with weights you control in code." (https://docs.typesafe.ai/patterns/composite-scoring.md). The model rates narrow dimensions; the weights and the arithmetic stay in code. That matches Cobalt's rule — but see §5: under L52 each model-rated dimension is a MODELLED number, and the vendor itself warns "score levels are weak in numerical calibration".

---

## §4 Invoking it from Cobalt

**Short answer.** The pattern fits Cobalt's seam exactly; the product fits it only partly. It is not chat-completions-shaped, so today's routing class cannot call it, and it has no local mode, so it cannot sit in a local-first fallback chain without a Cobalt-side adapter.

What exists today: the routing class is in the old tree and uses the LiteLLM SDK's `completion` call (`src/cobalt_agent/llm.py:12`), with a `response_format` pass-through (`llm.py:83`, `:146-147`); TRIAGE keeps it and adds "retries, timeouts, fallback chain … usage/cost capture" (`docs/20 - Assessment/TRIAGE.md:117`). The new core has NO LLM call site yet (grep of `src/cobalt` for the routing library on 2026-09-21: zero matches). So the first typed classifier would also be the new core's first routed call — the seam gets designed once, here.

Three ways the product could be reached, in order of lawfulness:
1. **Through the LiteLLM PROXY as a pass-through endpoint.** "Route requests from your LiteLLM proxy to any external API." with "centralized authentication, spend tracking, budgeting" (https://docs.litellm.ai/docs/proxy/pass_through). This keeps one door and one cost ledger (L5, L27). It does NOT give fallback or model swap: the request is the vendor's shape, so no other model can answer it. Whether Cobalt runs the proxy (L22 names proxy-mode for the local lane) or only the SDK in the engine path: NOT KNOWN from the files read.
2. **A Cobalt adapter behind the routing layer** that takes ONE neutral typed question and renders it either as the vendor's request or as a schema-constrained chat call to a routed or local model. This is the only shape that gives L25 a fallback chain. It is new code and a design decision.
3. **The vendor SDK called directly.** An out-of-band bypass under L5 and third-party code under L15. Needs a ruling; not recommended as a default reading of the laws.

The seam, in Python-shaped pseudocode (a sketch of the shape, not a design):

```python
def classify(question_id: str, payload: BaseModel) -> Classified:
    q = registry.load(question_id)                 # L10: schema-validated config, in git, has a dry-run
    request = q.render(payload)                    # deterministic; payload already validated (L1)
    raw = router.call(lane=q.lane, request=request)   # ONE door (L5); lane has a fallback chain (L25)
    answer = q.answer_model.model_validate(raw.body)  # invalid -> raises -> loud FAILED, never a default
    if answer.confidence < q.floor(settings):      # floor is a ruled setting, not a literal (L53)
        answer = answer.as_unsure()                # abstain is a typed value, shown as "unsure"
    store.write(ClassificationRecord(              # L57: replayable
        question_id=question_id, question_sha=q.sha256, input=payload, request=request,
        model_id=raw.model_id,                     # the versioned id the response reports, never an alias
        raw_response=raw.body, answer=answer, lane=raw.lane, degraded=raw.degraded, at=clock.now()))
    return Classified(answer=answer, role="shadow")  # L7: shadow until agreement stats + his approval
```
"Replay" for a model call means re-reading the stored response, not re-asking the model: a vendor model can change under an alias, and determinism is NOT KNOWN (§2).

---

## §5 Cobalt's classification problems, mapped — the whole project

**Short answer.** Most of Cobalt's choices are already deterministic and must stay so; a typed classifier earns a place where the INPUT is language or where Cobalt today says "unknown" and waits for him. It never produces a number that reaches a score, never ranks, never sizes, never approves.

**His scoring example, head-on.** In a complex scoring algorithm a classifier belongs in three places: (1) choosing a discrete label or regime from features that code already computed and bucketed; (2) triaging text into a category that code then maps to a grade through a ruled table; (3) proposing a rule or a weight change for him to approve (REQ "the system continuously PROPOSES improvements", `COBALT-REQUIREMENTS.md:117-119`). It does NOT belong in: the score's numbers, the curves, conviction, proximity, the proposed key, sizing, or the ranking. `scoring.py:1-2` names the card score "the ONE ranking authority that reaches a radar card" (L52-b), and CLAUDE.md rules "all numeric computation is deterministic code". The model has a slot already built for it: a dot carries `tier: Literal["deterministic", "judgment"]` and `role: Literal["shadow", "live", "human"]` (`scoring.py:97-98`), and shadow grades "do not count" in conviction (`scoring.py:27-28`). A classifier's output enters as a judgment-tier SHADOW dot and stays there until an L7 run promotes it.

**"LLM structures."** Two uses that are not about trading at all. (a) Typed outputs as the CONTRACT between agents: the orchestrator sends a typed question, a specialist returns a Pydantic-validated answer, an invalid answer is a failed job (L18), never prose the next agent must interpret. (b) A classifier as a cheap ROUTER in front of expensive models: it labels the TASK CLASS; the class → model mapping stays in routing config "assigned by measured evidence" (L26), so the model picks a label, never a model.

Latency column: "event" = seconds are fine, invoked on an event (L2); "sub-second" per `COBALT-REQUIREMENTS.md:218-219` ("sub-second … would be ideal; seconds is acceptable").

| # | Area (where cited) | The choice set, by kind | Who decides today | Typed classifier helps? | Latency needed | It must never |
|---|---|---|---|---|---|---|
| 1 | Scans → stocks in play, pool admission | admit / reject; rank order | deterministic (filters, his rank rule — L53) | NO | per scan | admit, reject or rank a name |
| 2 | Setup formation (`radar/evaluate.py:13-16`, `:140`) | formed / not formed / avoided / not evaluable / input stale | deterministic three-valued predicate AST, zero tokens | NO | per scan | supply a truth value for a predicate (L2: no model in the loop) |
| 3 | The unknown catalyst inside formation (`evaluate.py:25-27`) | catalyst present: yes / no / unsure, plus kind | nobody — today it is `not_evaluable` | ONLY IN SHADOW, computed on a news EVENT and stored; the scan reads the stored label | event | be called from the scan tick; turn "unsure" into yes |
| 4 | Card dots — computed factors (`scoring.py:12-19`) | grade 1–10 from a curve | deterministic curves, shadow role | NO | per scan | replace a curve |
| 5 | Card dots — desk factors: catalyst, market alignment, sector alignment (`scoring.py:20-24`) | a small ordered grade or with / flat / against | N/A today (`DESK_NA`, `DEFAULT_UNRULED`) | ONLY IN SHADOW — the clearest fit in the project | event | enter conviction before L7; emit the grade number itself (it picks a label; a ruled table maps label → grade) |
| 6 | Card dots — human factors, the tape dot (L11) | his grade | him | NO, by law | — | compute the human-only variable |
| 7 | Card score, proximity, proposed key, sizing (`scoring.py:1-47`) | numbers | deterministic | NO, never | per scan | touch them (L52, CLAUDE.md) |
| 8 | ASET grade (`aset/models.py:29-38`; REQ `:106-111`) | five-step grade enum | him, by tap; engine sizes from it | NO for the grade; a shadow "suggested grade" is an L7 + L52 tribunal matter | sub-second | grade or size; show a suggestion without its n (L8) |
| 9 | News / X / squawk triage (REQ `:85-88`) | relevant to a watched name / market-wide / noise / duplicate; urgency level | not built | YES — highest-volume language task | event, seconds | feed the grading chain from a ToS-risky source (L9); run as a poll loop |
| 10 | Catalyst kind + grade for a headline (ladder: desk supplies it in S3, `scoring.py:21`) | kind (offering, earnings, regulatory, …); materiality level; fresh yes / no | him | YES, in shadow beside his label | event | invent a kind outside the enum; grade without n (L8) |
| 11 | "Why is this ticker moving?" resolver (REQ `:189-201`) | which of the candidate causes the deterministic resolver found | not built; spec = deterministic lookup, local model composes | YES for picking among candidates with probabilities; NO for writing the paragraph | seconds | name a cause that is not in the resolver's candidate list |
| 12 | Earnings triple-beat matrix (REQ `:165-169`) | beat / inline / miss ×3 → composed class | not built | NO — it is arithmetic on fetched numbers, then a lookup table | event | compare numbers (the vendor: "Jev is not a calculator.") |
| 13 | Guidance direction from prose (REQ `:170-172`) | raised / maintained / cut / none / unsure | not built; spec = local model + Pydantic + verbatim quote | PARTLY — a label yes; but "No quote, no number" needs generated text, which the product cannot give | event | emit a figure without its source quote |
| 14 | Research extraction: filing-section tagging, dilution flags (REQ `:149-154`, `:160-163`) | section kind; instrument present yes / no / unsure | not built; spec = local model, structured JSON | YES — but the local model with a schema is the ruled lane | batch, minutes | replace the three-failures-escalate rule with a silent retry |
| 15 | Market-context checkpoints (ladder F5, `SPRINT-LADDER-v0_1.md:632`) | regime label from computed numbers | numbers deterministic; narrative single-house | ONLY IN SHADOW, from bucketed features (§3 C) | scheduled | see raw numbers and "judge" them; change a risk setting |
| 16 | Exits, legs, fills, expiry (ladder F11, `:590`) | state transitions | deterministic state machine + his taps | NO | sub-second | infer a fill or a leg |
| 17 | 19b trigger / strike alert (ladder F9, `:615`) | triggered / not | deterministic price-cross detector | NO — latency and L2 | ≤ seconds, hard | sit anywhere on this path |
| 18 | DRC: unfilled card taken / passed / discarded; adherence boxes (ladder F14, `:592`) | three-way choice; yes / no | him — Cobalt asks | NO — these are his attestations | — | pre-tick an attestation |
| 19 | Journaling: trade note → mistake / tag taxonomy | multi-label from his tag list | him | YES as PROPOSED tags he confirms (§3 B) | after close | write a tag as his; count a proposed tag in a statistic |
| 20 | Coaching and cadence reviews (REQ `:91-95`) | per trade: followed plan / deviated / unsure, by rule | not built | ONLY IN SHADOW, from deterministic facts first; language only for his free text | after close | "hold him accountable" on a model label without n (L8) |
| 21 | Strategy decay / size-down flag (REQ `:114-116`) | decaying yes / no | not built | NO — statistics with n; any change is HITL | weekly | flag from a judgment |
| 22 | Readiness scorecard from wearable data (REQ `:112-113`) | four-step grade | not built | NO — numbers through a ruled table | daily | touch the daily stop |
| 23 | Voice / DM intent → tier and skill (REQ `:206-209`; `TRIAGE.md:141` keyword routing = REDESIGN) | skill / instant answer / headless session / unknown | old tree: keyword routing | YES — textbook fit; but the spec says "small local router model" and fully local for voice, so: the pattern on the local model, not the hosted product | sub-second | route a trading-logic action past HITL; guess on "unknown" |
| 24 | Chief of staff: which specialist, ask vs act (L6, L38; ladder F20, `:633`) | agent id from the registry enum; ask / act | not built | YES — typed contract between agents | seconds | spawn (L36), approve (L37), or invent an agent not in the registry (L16) |
| 25 | Model routing: task class → tier (L26; REQ `:223-236`) | task-class enum | config + his rulings | YES for labelling the task class only | sub-second | choose the model; override the evidence table |
| 26 | HITL approvals, law classification at the fold, restart derivation (L37, L42, fold job) | approve / deny; law / decision | him, or deterministic rules | NO, by law | — | be anywhere near them |
| 27 | Ops: day-open log triage (L49 local seat "reads and judges") | green / amber / red per check, with the cited log line | local seat, prose prompt | YES — a schema tightens what exists; local lane | minutes | turn a missing log into green (L1) |

Counted: 27 areas; a typed classifier helps in 14 (rows 9, 10, 11, 14, 19, 23, 24, 25, 27 plainly; rows 3, 5, 15, 20 only in shadow; row 13 partly) and is excluded in 13 (rows 1, 2, 4, 6, 7, 8, 12, 16, 17, 18, 21, 22, 26).

---

## §6 Boundaries

**Short answer.** The pattern passes Cobalt's laws if it is built as §4 sketches. The product, as published today, fails local-first outright and leaves four laws unanswerable from public facts.

**Law by law.**
- **L1 fail-loud.** The product never refuses: a Choice always returns one of the options, with probabilities. "Unsure" exists only if Cobalt's code makes it a typed value and every consumer renders it. HTTP 422 / 429 / 529 are loud; a confident wrong label is not — "what's been eliminated is the malformed answer, not the mistaken judgment" (TrueFoundry).
- **L2 no model in a watch loop.** Claimed latency (70–500 ms, unverified) would allow per-tick calls; the law does not. The model runs on an EVENT (a new headline, a fill, a DM); the scan reads the stored label. A local model with bounded latency is the only case the prompt's card allows per tick, and nothing in §5 needs it.
- **L5 / L22 / L24 routing.** Not chat-completions-shaped. Reachable through the LiteLLM proxy's pass-through (one door, one ledger) but without swap or fallback; hot-swappable only behind a Cobalt adapter (§4). It is rung 3 of L24 — a metered fast-wire API, "sync-only, rare, bounded, cost-footered" — and L5 itself is under routing-tribunal review.
- **L7 shadow.** Every "yes" in §5 starts as shadow beside his hand label, with agreement statistics, then his approval. For labels that reach a dot this is not optional.
- **L8 sample size.** Agreement under n = 30 per LABEL reads "insufficient data". Rare classes will sit there for weeks; a tribunal should expect that, not work around it.
- **L10 config-as-code.** Questions, option descriptions and level descriptions ARE the classifier. They need a Pydantic schema, git, a hash stored with every answer, and a dry-run against yesterday's stored inputs. A wording edit is a new classifier and restarts its shadow count.
- **L15 external code.** The SDK is third-party code; the REST shape can be called without it. The vendor also ships an installable "skill" for coding agents — not installed, see the run report.
- **L23 / L25 local-first, fallback.** The product cannot run locally and has no degraded mode of its own. The host's local model can do the same JOB through schema-constrained output (§7), which makes local the first candidate by law and the product a candidate only where a bake-off shows local is not sufficient (L26).
- **L27 budget.** A new vendor and a new meter need his ruling, whatever the size. Price facts: "$0.042 / MTok for input and $0 for output". Free tier or minimum spend: NOT FOUND.
- **L32 / L17 what leaves the machine.** Every call sends the state AND the full question text: option names, level descriptions, tag lists. For §5 rows 9–14 the state is public text and the options are common trader vocabulary. For rows 5, 19 and 20 the questions would carry his taxonomy and his notes — user data. Exposing that to a vendor is his choice (L17, opt-out default); secrets never. Retention is open-ended and an API data agreement was NOT FOUND (§2).
- **L37.** No classifier output is ever an approval, a waiver or a gate result.
- **L52.** A label that reaches a dot is "modelled", must be marked so, and must degrade the score accordingly; the card score stays the one ranking authority; and the classifier must be auditable by another house — which for a closed hosted model means auditing the stored record, not the model.
- **L57 explainability.** Achievable only as record-replay: store question hash, input, raw response and the versioned model id the response reports. Re-asking later is not a replay: pinning exists ("pin that version's ID"), a deprecation policy was NOT FOUND, determinism is NOT KNOWN.

**Technical limits.**
- **Accuracy evidence.** Vendor benchmarks only, "self-graded on a format the company invented" (TrueFoundry). Nothing on financial text. Cobalt would have to measure on its own labelled history.
- **Calibration.** It is the product's central claim and "the one no outside party has tested yet" (TrueFoundry). The vendor's own limits page: "score levels are weak in numerical calibration".
- **Numbers, dates, counting.** "Jev is not a calculator. We strongly recommend implementing any mathematical logic in code."; it "does not count reliably"; it "reads dates as text, not as ordered quantities" (jaggedness page). Every numeric feature must be bucketed into words by code first.
- **No reasons.** It is "not trained to generate text". His phrase "classification reasoning" is met only by decomposition — several narrow questions whose answers ARE the reasons — or by a text model with a schema (§7).
- **Distractors and injection.** "unrelated detail acts as a distractor"; it is vulnerable to "adversarial content" and an "injected instruction" (same page). Headlines and posts are untrusted input; the state must be trimmed by code and never carry instructions.
- **Literal reading.** It struggles with "double negatives or complex indirection" — option descriptions need testing like code.
- **Drift.** An alias can move to a new version; thresholds tuned on one version do not carry. Pin, and re-run shadow on a version change.
- **Label-set changes.** Adding or rewording an option changes every probability. Version the question; never compare agreement statistics across versions.
- **Cold start.** No training is needed to start, but no TRUST exists without labelled history: he has to hand-label in shadow anyway (L7, L8). There is no fine-tuning offer on the pages read.
- **Cost at Cobalt's volumes — all call counts ASSUMED, for arithmetic only.** Text triage: 2,000 items a day × 600 input tokens = 1.2 M tokens → 1.2 × $0.042 = $0.05 a day ≈ $1.11 over 22 sessions. A deliberately absurd case the laws forbid anyway (100 names × 400 minutes × 1,000 tokens = 40 M tokens) = $1.68 a day ≈ $37 a month. The one measured size available: the vendor's single-question example reports 296 input tokens. Price is not the constraint; the ruling, the data exposure and the evidence are.
- **Lock-in.** The three question types are easy to re-express as a JSON schema for any model, so the PATTERN is portable. What does not transfer: the probabilities, and every threshold tuned on them.
- **Outage.** Hosted in the United States, no SLA found, rate limits that "can change without notice", a five-day-old public service. A dead lane must show red (L9) and the label must read "unavailable", never the last good answer.

---

## §7 What else can be done

**Short answer.** The same job — a typed answer from a closed label set, validated, with an abstain — can be done today on the models Cobalt already routes to, including the local one. The product's distinct offer is speed, price and probabilities per option; whether those are worth a new vendor is an evidence question.

1. **Schema-constrained output on the routed models (cloud or local).** LiteLLM accepts a Pydantic model as `response_format` and lists OpenAI, xAI, Gemini, Anthropic and Ollama among supported providers, with `litellm.enable_json_schema_validation = True` for models without native support (https://docs.litellm.ai/docs/completion/json_mode). The host's LM Studio enforces a JSON schema on its OpenAI-compatible endpoint; for MLX models it does so "using Outlines" (https://lmstudio.ai/docs/developer/openai-compat/structured-output). That is the local model already behind the local route — no new vendor, no data leaves, inside L5 as written, and it can return reasons. Costs: seconds, not milliseconds (the local model's thinking is always on); no calibrated probability per option — a self-reported confidence field is not one; and the shape is guaranteed, the judgment is not. **Beats the product** wherever seconds are fine, reasons are wanted, or the content is his — most of §5.
2. **A small local classifier trained on his own labels.** SetFit is "An efficient and prompt-free framework for few-shot fine-tuning of Sentence Transformers"; with "only 8 labeled examples per class" it was "competitive with fine-tuning RoBERTa Large on the full training set of 3k examples" on one sentiment dataset (https://huggingface.co/docs/setfit/index — a vendor-side benchmark too, and not finance). The same family includes embeddings plus a classical model. It runs in milliseconds on the host, is fully deterministic once trained, has a pinned artifact that replays exactly (L57), and gives real probabilities that can be checked for calibration against his labels. Costs: it needs labelled history per label (L8 applies to training as well as to trust), retraining when labels change, and it is an embedder — TRIAGE gates embedders behind an unwritten ADR (`TRIAGE.md:43`). **Beats the product** for high-volume, stable label sets once a few hundred of his labels exist — news relevance, intent routing.
3. **Rules first, a model only on the residue.** Deterministic rules (source, ticker match, filing form type, keyword tables) settle most items; only what the rules cannot place goes to a model, and its answer is marked modelled. This is the shape the "why is it moving" spec already has (`COBALT-REQUIREMENTS.md:190-201`). **Beats everything** on auditability and cost, and shrinks the volume that any model — local, routed or this product — has to be trusted on.

These stack rather than compete: rules → local typed model → (only if a bake-off shows a gap) a faster or better-calibrated lane.

---

## §8 Questions for the tribunal

Each is answerable ADOPT / ADOPT WITH (conditions) / REJECT. None asks him to rule before a design exists.

1. Adopt the typed-classification PATTERN (§4: validated input → one routed call → validated typed answer with a first-class "unsure" → stored record → shadow) as the new core's standard for every judgment call, independent of any vendor?
2. Adopt the rule that a model on a scoring path emits a LABEL only, and a ruled table in code maps label → grade — so no model-emitted number ever reaches a dot (L52, §5 head-on)?
3. Adopt §5 rows 5 and 10 (desk-graded dots, catalyst kind) as the first shadow site, since the slot (`tier: judgment`, `role: shadow`) already exists?
4. Adopt record-replay (stored question hash, input, raw response, versioned model id) as what L57 means for any model-produced label?
5. Adopt "event-computed, scan-read": a label is computed on an event and stored; the scan only reads it (L2) — including for the unknown-catalyst gap (row 3)?
6. Adopt a neutral question schema (choice / ordered score / yes-no) that renders to any lane, so the local model, a routed cloud model and a hosted decision model are interchangeable behind one adapter (L5, L25)?
7. Adopt the local model with schema-constrained output as the FIRST lane for every site in §5 (L23), with other lanes admitted only by a bake-off on his labelled history (L26)?
8. Admit the hosted product to such a bake-off at all — given it needs a spend ruling (L27), a data-exposure choice (L17, L32) and has no independent evidence yet — or defer until independent calibration results and API data terms exist?
9. Adopt numeric bucketing as a hard rule: no model sees a raw computed number; code turns it into a ruled word bucket first (§3 C, §6)?
10. Adopt per-label sample gates: agreement statistics per LABEL, "insufficient data" under n = 30, and a question-text change resets the count (L8, L10)?

---

## §9 Sources

All fetched 2026-09-21. 18 fetches, 1 search.

| # | URL | What it gave |
|---|---|---|
| 1 | https://typesafe.ai/ | Product claim, RLCD sentence, price and demo figures, site map |
| 2 | https://docs.typesafe.ai/ | "typed values and probability distributions"; parallel questions |
| 3 | https://docs.typesafe.ai/llms.txt | Full docs index: primitives, patterns, cookbooks, SDKs, agent skill, limits page |
| 4 | https://docs.typesafe.ai/api.md | Endpoint, auth, request and response schema, error codes; no determinism parameter |
| 5 | https://docs.typesafe.ai/confidence.md | Confidence = concentration of the distribution; abstain is the caller's job |
| 6 | https://docs.typesafe.ai/patterns/composite-scoring.md | Atomic scores, weights in code |
| 7 | https://docs.typesafe.ai/model-jaggedness/jev-1.13.md | Known limits: numbers, dates, counting, distractors, injection, no text; reviewed 2026-09-17 |
| 8 | https://typesafe.ai/legal/terms | Legal entity, address, "do not submit … confidential", updated 2026-09-19 |
| 9 | https://docs.typesafe.ai/models.md | Model ids, aliases, pinning advice, 64k limit, price, rate limits |
| 10 | https://typesafe.ai/legal/privacy-policy | No training on input; open-ended retention; US hosting; updated 2025-11-19 |
| 11 | https://docs.typesafe.ai/introduction/quickstart.md | Python SDK call shape; key from dashboard; an agent-plugin install line (not followed) |
| 12 | https://www.theregister.com/ai-and-ml/2026/09/16/typesafe-ai-debuts-model-for-machines-that-plays-doom/5296711 | Launch date, CEO, $40M, latency and price claims, journalist's caveat |
| 13 | https://www.truefoundry.com/blog/typesafe-ai-jev | Closed, hosted, waitlist; "still unknown" list; 255-option limit; self-graded benchmarks |
| 14 | https://flaviocopes.com/jev/ | HTTP 403 — nothing obtained |
| 15 | https://docs.litellm.ai/docs/proxy/pass_through | Proxy can front any external API with auth and spend tracking |
| 16 | https://docs.litellm.ai/docs/completion/json_mode | Pydantic model as `response_format`; provider list; client-side validation flag |
| 17 | https://lmstudio.ai/docs/developer/openai-compat/structured-output | JSON-schema enforcement; Outlines for MLX; small-model caveat |
| 18 | https://huggingface.co/docs/setfit/index | Few-shot, prompt-free classifier; 8-examples claim |

Search run (generic terms only): the vendor's name with "System One models Jev founders funding". It surfaced sources 12–14 and a press release (not fetched) from which the co-founder names, founding year and lead investor in §1 are UNVERIFIED.

NOT FOUND on the pages read: parameter count or base model · any independent benchmark or calibration study · determinism settings · deprecation policy · SLA or uptime · API-specific data terms, DPA or zero-retention option · free tier or minimum spend · multi-state batch endpoint · fine-tuning · any finance-domain evaluation. NOT READ (budget): the cookbooks (one is titled as turning "natural-language trading requests into calls to ordinary typed functions" — outside Cobalt's boundary: Cobalt never executes trades), the SDK changelogs, the vendor blog and manifesto, the intent-routing and confidence-routing pattern pages.

Local files cited: `src/cobalt/cards/scoring.py` · `src/cobalt/radar/evaluate.py` · `src/cobalt/taxonomy/catalyst.py` (read, not cited — it is a vault batch-apply tool, not a classifier) · `src/cobalt/aset/models.py` · `src/cobalt_agent/llm.py` · `docs/00 - Project/SPRINT-LADDER-v0_1.md` · `docs/00 - Project/COBALT-REQUIREMENTS.md` · `docs/20 - Assessment/TRIAGE.md`.
