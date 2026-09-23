# JEV hands-on trial — plan (2026-09-23)

Drafted by the Opus 5.5 seat `jev-trial-draft-0923` (prompt `prompts/2026-09-23/27-draft-jev-trial.md`). LADDER: OFF-LADDER — `cto-2026-09-21.md` R31 / R34 / R35 / R37, `cto-2026-09-23.md` R34 + R38. L72: a parallel lane; it holds nothing. INPUT to the typed-classifier design tribunal (09-21 R34: after S2 closes, never dropped). It decides nothing about adoption.

**His words that set this plan.** 09-21 R35: "this is blazing fast this can do a significant multi question hard selective prompt with several layers of deep selections and then derive the actual scoring in milliseconds. The difference is minutes or milliseconds." 09-23 R34: "when we need to review JEV, openrouter has access and it is financed there. We can do test using cobalt's openrouter api key". 09-23 R38: "JEV is https://typesafe.ai/ type safe llm clasifier". → The trial's FIRST question is SPEED of a layered multi-question typed call, measured from this host, through OpenRouter, on Cobalt's funded `OPENROUTER_API_KEY`.

**Per-case override, cited once (L73, recorded by the desk in `cto-2026-09-23.md` R34 / R38, not folded):** a metered API key used for a trial sets aside L22 / L29's "API keys are for Cobalt's engine", L27's narrowest-rung rule and L5's one-door rule for THIS trial only. The routing cluster stays frozen (L5, L22, L27 — routing tribunal). Nothing in this plan rewrites them.

---

## §0 One screen

- **What runs:** a new-core collector (`src/cobalt/classify/`, build `28`) that discovers the Jev model on OpenRouter's own model list, sends typed question sets, and stores every call's inputs, answer, confidence, latency, cost and returned model id to a local results file under `~/cobalt-wt/jev-trial/scratch/` (not the vault, not the DB, not git).
- **Question sets:** 4 — S1 (news triage), S2 (catalyst kind / materiality / freshness), S3 (alignment labels from word buckets), T9 (ops day-open triage). Plus the LAYERED set **L20**: S1 + S2 + S3 fused into one 20-question call on one state — the shape of his R35 example, and the call the success bar is built on.
- **Measured per call:** end-to-end latency ms · HTTP ms · each answer · per-option probabilities and `confidence` where the response carries them · input / output tokens and cost from the response's `usage` · the model id AS RETURNED · the door (`openrouter`).
- **Comparison:** the local model on the same typed questions (build after `28`, no meter); an Opus 5.5 seat as a blind reference grader (subscription seat).
- **Spend cap proposed: $3.00** for the whole trial, enforced by the code before and during every run (§5). His to approve.
- **Calls:** ≤1,100 metered calls in total, ≈$0.07 at the vendor's published price; OpenRouter's price for this model is NOT KNOWN until discovery (§5).
- **Does NOT decide:** adoption, any site, any threshold, any floor, which lane, which door. The tribunal does (09-21 R34).

## §1 What is NOT KNOWN before the first call (the build discovers; nobody guesses)

| # | Unknown | Settled by | If it goes the wrong way |
|---|---|---|---|
| U1 | Whether OpenRouter lists a Jev / typesafe model at all. Neither research pass names OpenRouter; they found a Cloudflare gateway page (fetched) and Vercel / LiteLLM hooks (second-hand) (`…-DEEP-2026-09-21.md` §2 row 22). | Build `28` STEP-DISCOVER: OpenRouter's public model list, matched by `(?i)(typesafe|jev)` on `id` and `name`. | Zero matches → `FAILED` loud; this door is closed. The trial falls back to R35's path (his own sign-up and key — his hands). Two or more → `FAILED` with the list; he picks the id. |
| U2 | The request shape OpenRouter accepts for it (vendor-native `questions` object, or chat + `response_format` JSON schema). | The discovered model entry's `supported_parameters` and `description`, as returned. | Neither documented → `FAILED` with the entry quoted; the desk decides. The build never invents a parameter. |
| U3 | Whether per-option probabilities and `confidence` come back through this door. They ARE the product's distinctive output (09-21 R37). | The one probe call in build `28` — its raw response becomes the fixture (L45). | Absent → every confidence measurement (M7, M8, B6) reads `NOT AVAILABLE THROUGH OPENROUTER`; latency and labels are still measured. The tribunal is told the door hides the probabilities. |
| U4 | The model id OpenRouter returns (a versioned id such as `jev-1.13.0`, or only a slug). A gateway can hide the version ("No model version tracking via Gateway", deep research §3.1 row 1). | The probe response's `model` field (and `provider` if present). | Unversioned → B4 fails; recorded, not hidden. |
| U5 | OpenRouter's price for this model and whether its `usage` carries a cost. | The discovered entry's `pricing` fields; the probe response's `usage`. | No cost in `usage` → cost = tokens × entry pricing, marked `computed`. |
| U6 | Gateway latency. Research: ≈130 ms direct vs ≈260 ms through a gateway (one individual's figures, deep §3.1 row 9). | M1. | Recorded as the door's cost; the direct-vendor figure stays NOT KNOWN unless he runs R35's path. |

## §2 The question sets

Conventions (from the research, unchanged): every Choice carries `unsure`; no raw number reaches the model — states carry WORDS only (deep §5, broad §4 R7); labels by KIND only, no ticker, no value of his (L32); every question set carries a sha256 of its full text, and a wording change is a new set (L10); the trial is CLI-invoked, never a watch loop (L2). Question texts live in `configs/cobalt/classify/trial.yaml` (Pydantic schema, git, `--dry-run`, L10).

| Set | Research source | Questions (types) | Inputs | Provenance | Reference label |
|---|---|---|---|---|---|
| **S1** news / X triage | deep §5 S1; broad T2 | `relevance` Choice {watched name, market-wide, sector-wide, not relevant, unsure} · `urgency` Score {background, routine, notable, act-now} · `duplicate` Noul · `argues_for_label` Noul (injection control, broad T2) | 40 headline-shaped items + 10 injection-control items | CONSTRUCTED — Cobalt stores no news: `src/cobalt/aset/radar_panel.py:1041` renders "no news source wired to radar cards (S3)". L45 binds where the real artifact exists; here none does, and 09-21 R35 ruled invented text only. Placeholder names (`XYZ`), never a real ticker. | Opus 5.5 seat, blind |
| **S2** catalyst kind, materiality, freshness | deep §5 S2; broad T3 | `kind` Choice {offering, results / guidance, trial or regulator news, deal, contract, management change, other real event, no new information, unsure} · `materiality` Score {irrelevant, minor, notable, day-defining} · `is_new` Noul | the same 40 items | CONSTRUCTED (as S1). The common event kinds, never his catalyst list (that is user data, L32; it is S2's shadow run's input, not the trial's). | Opus 5.5 seat, blind |
| **S3** market / sector alignment as a label | deep §5 S3; broad T7 | `market_alignment` Choice {with, flat, against, unsure} · `sector_alignment` Choice (same) · `regime_clear` Noul | 40 word-bucket states (`trend: up/down/flat`, `strength: low/normal/high`, `day_phase: premarket/open/mid/close`) | CONSTRUCTED word combinations. No bucket EDGE is used or invented: the state is words, so no number is turned into a word by the trial (edges are his, L53). A shuffled-key twin of 20 states tests order sensitivity (deep §5 S3). | Opus 5.5 seat, blind |
| **T9** ops day-open triage | broad T9; first pass row 27 ("the cheapest first proof of the whole seam") | per report: `overall` Choice {green, amber, red, unsure} · `db_ok` / `services_ok` / `jobs_ok` / `logs_ok` Noul | the committed `docs/40 - DevDocs/reports/day-open-*.md` files (14 on 2026-09-23) | REAL — Cobalt's own stored artifacts, read at run time, passed through `cobalt.redact.redact()`; a body that redaction would change is REFUSED, never sent (§6). Outside S1–S8: added because it is the one set with real stored inputs; his to strike (report ESCALATE). | the verdict each report already states, where it states one; the Opus seat otherwise |
| **L20** the layered call | broad T1 (his trade-grade example), deep §5 | all of S1 (4) + S2 (3) + S3 (3) + 10 more narrow gates written as broad T1 layers 1–4 by KIND (catalyst present, context readable, event risk in window, supply language present, …) = 20 questions, ONE state, ONE call | 40 states composed from S1 × S3 items | CONSTRUCTED | — (a speed and stability workload, not an accuracy set) |

**Excluded, with the reason:** S4 (reads S2's stored labels — no read side exists in a trial) · S5 (inputs are his DM / voice sentences — user data; the voice v3 design is in its own tribunal) · S6 (his notes and tag list — user data, L17 / L32: leaving the machine is his choice, not the plan's) · S7 (Cobalt stores no filings; fetching them is a second network path) · S8 (the resolver is not built).

## §3 Measurements (numbered after broad research §3 and §6A; only what this door can answer)

| M | What | Design | Calls |
|---|---|---|---|
| M1 | network floor + gateway | one Noul, one-line state; 50 calls in each of four windows (04:00–05:00, 09:30–10:00, 12:00–12:30, 15:30–16:00 ET); first-call-after-idle flagged | 200 |
| M2 | marginal cost per question | 1, 5, 13, 20, 40 questions × state of ≈300 and ≈1,500 tokens × 10 reps | 100 |
| M3 | one call of N vs N parallel vs N sequential | N = 13 (the vendor's cookbook size), 10 reps each shape | 270 |
| M4 | gated 4-level tree vs one fan-out | L20's questions split into 4 dependent levels vs one call, 20 reps | 100 |
| M5 | determinism | 10 L20 states × 10 identical repeats | 100 |
| M6 | question-order effect | 20 L20 states, question map as written and reversed | 40 |
| M7 | ties / saturation (broad §6A (5) 15–16) | computed from every response that carries probabilities: distinct values, share exactly 0 or 1, reported `confidence` vs the documented formula | 0 (derived) |
| M8 | the sets | S1 50 · S2 40 · S3 40 + 20 shuffled · T9 14 · L20 40 | 204 |
| M9 | local lane, same questions | S1, S2, S3, L20 on the local model, schema-constrained, sequential; seconds per set; whether log-probabilities are returned | 0 metered |
| M10 | reference grader | Opus 5.5 seat labels S1, S2, S3 items blind (never sees a Jev answer); agreement per label with n | 0 metered |
| | | **metered total** | **1,014 (ceiling 1,100)** |

## §4 Pre-registered success bar — FIXED HERE, BEFORE ANY CALL

Changing a bar after the first call voids the trial's verdict for that bar; the results report prints this table verbatim beside the results.

| Bar | Test | Pass |
|---|---|---|
| **B1 speed** (his R35 goal) | L20, one call, end-to-end from this host through OpenRouter, M8's 40 calls | p50 ≤ 500 ms AND p95 ≤ 1,000 ms |
| **B2 fan-out** | M3: one call of 13 vs 13 sequential, median wall time | one call ≤ ¼ of sequential |
| **B3 typed validity** | every metered call | 100 % validate into the Pydantic result; ONE invalid response = FAIL (L1) |
| **B4 model id** | every response | a versioned model id is returned (not only an alias or slug) |
| **B5 stability** | M5 | with probabilities: max per-option spread ≤ 0.05 AND 0 answer flips; without: ≤ 1 flip in 100 |
| **B6 confidence through the door** | the probe + M8 | per-option probabilities for Choice / Score and a `confidence` field are present — a FACT reported YES / NO, not graded |
| **B7 order** | M6 | ≤ 2 of 20 states change any answer |
| **B8 injection** | S1's 10 control items | ≤ 1 of 10 answers moved by the embedded instruction vs its clean twin |
| **B9 minutes vs milliseconds** | M9 vs M8, L20 | local median ÷ Jev median ≥ 10 |
| **B10 agreement (informational)** | M10, S1 `relevance`, S2 `kind`, S3 `market_alignment` | ≥ 80 %, each with its n; n < 30 on a label reads "insufficient data" (L8). Constructed items: this bar says nothing about accuracy on his text. |
| **B11 spend** | ledger | total ≤ the approved cap; any overrun = FAILED |

**Verdict line** (one of, printed by the results report): `SPEED CLAIM HOLDS THROUGH OPENROUTER` iff B1, B2, B3, B4 and B11 all pass · otherwise `SPEED CLAIM DOES NOT HOLD THROUGH OPENROUTER — <failed bars>`. B5–B10 are reported beside it, never folded into it.

## §5 Spend cap — PROPOSED $3.00 (his to approve)

- **Arithmetic (ASSUMED sizes):** 1,014 calls × ≈1,500 input tokens ≈ 1.5 M tokens. At the vendor's published $0.042 / MTok input, output free (deep §1 rows 1–2) ≈ **$0.07**. OpenRouter's price for this model is NOT KNOWN (U5); $3.00 covers a ≈40× markup and matches his "a couple of dollars" (09-21 R35).
- **Enforced in code, not by promise** (the L53 total-demand shape): one spend ledger `scratch/classify-spend.jsonl` records every metered call's cost (returned, or computed from tokens × the discovered entry's pricing, marked `computed`). Before ANY `--run`: projected cost of the run + everything already in the ledger > cap → REFUSED, zero calls. During a run: the running total reaching the cap stops the run loud. A call whose returned cost exceeds 10× its projection stops the run loud (the pricing assumption is wrong). The cap sits in `configs/cobalt/classify/trial.yaml` as `spend_cap_usd` with `source: ruling` naming his row.
- **Optional, his hands:** a credit limit on the OpenRouter key itself (outside Cobalt). Not assumed.

## §6 Secrets and data leaving the machine

- `OPENROUTER_API_KEY` is read by the Python process at call time through the new core's one vault reader, `cobalt.redact.secrets.read_secret` (the same Fernet file `VaultManager` holds; `src/cobalt/redact/secrets.py:237`). It exists only in the `Authorization` header of one request. Never printed, logged, stored, in `.env`, in a command line, in an exception, a fixture or a report (L4, L41).
- `COBALT_MASTER_KEY` reaches the process only through a secret-free wrapper `ops/run_classify_trial.sh` that sources `~/.cobalt_key` — the precedent of `ops/run_backup.sh` and `ops/start_aset.sh`. No session receives either key (L41).
- Model discovery reads OpenRouter's PUBLIC model list with no credential at all.
- Every outbound body passes `cobalt.redact.redact()` and the F19 literal guard; a body that redaction would change is REFUSED, never sent redacted. Every stored response passes the same guard before it is written.
- What leaves: constructed text (S1–S3, L20) and Cobalt's day-open reports (T9) — to OpenRouter and to the vendor behind it (US-hosted; no training on input; retention and the DPA text unread — deep §1 rows 9, 16). Nothing of his trading data, notes, lists or settings (L32).

## §7 What is stored (L57) and where

Per call, one JSON line in `~/cobalt-wt/jev-trial/scratch/classify-results-<set>-<utc stamp>.jsonl`: question-set id + sha256 · item id + provenance (`constructed` / `real:<path>`) · the rendered request (guarded) · the raw response (guarded) · each typed answer · probabilities / confidence as returned (never recomputed) · `latency_ms`, `http_ms` · usage + cost (`returned` / `computed`) · model id and provider AS RETURNED · door `openrouter` · UTC time. Not the vault, not the DB, not git (the prompt's rule; `scratch/` is excluded by `.git/info/exclude`). The results report (a later prompt) quotes counts and percentiles computed by code from these files.

## §8 Sequence (each step its own law step)

1. **Build `28`** (Opus 5.5, dev lane, offline code + tests) — STEP-DISCOVER (keyless) and ONE probe call through the wrapper (≈$0.0001); the probe's guarded response becomes the fixture (L45); every other command is `--dry-run`.
2. **Check `29`** (L67: Opus 5.5 · Grok · Gemini; Sol on METER) — secrets handling is every checker's first answer. A HOLD → classify (L75) → fix round.
3. **Local-lane collector** (a second class behind the same interface, L9; its own small build + check) — M9.
4. **Trial run** (a hub prompt, drafted after `29` reads clean): M1–M8 within the cap; M10 by an Opus seat on the stored items.
5. **Results report** → the typed-classifier tribunal's input pack (09-21 R34), beside the three research documents.

## §9 What this trial does NOT decide

- Adoption of the product, the pattern, or any site in the research's map — the four-house tribunal decides (09-21 R34; L67).
- Any confidence floor, threshold, bucket edge, grade table or weight — his values (L53), fitted on HIS labels in a shadow run (L7, L8), never on constructed items.
- Door: OpenRouter vs the vendor direct vs a local lane — the routing tribunal and the design tribunal (L5, L26 frozen).
- Nothing reaches a card, a dot, the DB, the vault or production. No shadow run starts from this trial (L7).
- Accuracy on trading text: constructed items cannot answer it (deep §6 "NOT settled by a trial" 1).
