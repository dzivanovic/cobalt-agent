# ROUTING PROPOSAL — 2026-09-22 (input to the routing tribunal, L67)

Proposer: Opus 5.5 (`claude-opus-5-5`), seat `routing-propose-0922`, prompt `prompts/2026-09-22/47-propose-routing.md`, written 18:37 EDT. Authority: `cto-2026-09-22.md` R81 ("A": the tribunal runs this week, its own lane, L72). This is a PROPOSAL. The four houses rule on it and derive the final (L67). Anything unresolved goes to Dejan as OPEN. A law file is never voted (L39).

**Conflict of interest, stated once (L26):** the proposer is an Anthropic model. Several items below ask for trials that could move seats away from Anthropic's top tier. Each house should weigh this proposal's Anthropic rows with that in mind.

## §0 The one idea

Two subjects share the word "routing," and the frozen clauses mix them:

- **ENGINE routing** covers the model calls Cobalt's own code makes (L5, L22, L24 rung 3, L25's fallback chain). **Measured:** `src/cobalt/` makes **zero** model calls today. `grep` finds no completion, messages or chat endpoint anywhere in the tree. The only hit is the heartbeat's port probe of `mainframe` (`heartbeat/probes.py:252`). The only engine calls that exist are in the old tree (`src/cobalt_agent/llm.py`, `memory/postgres.py:31` `litellm.embedding`), and they die with it (TRIAGE rows 43, 125).
- **SEAT routing** covers which house and model sits each agent-session seat that builds, checks or designs Cobalt (L26, L27's routing sentence, L29, L47, L49, L67). All real routing today is seat routing. Dejan's per-seat rulings (09-15 A, 09-21 R46, 09-22 R32/R36/R73/R76) make those assignments, not a config file.

Proposal: the law says which subject each clause governs. Seat assignments live in ONE **seat table**: task class → house → model id → meter → evidence → date → re-test trigger. Model ids stay out of the law sentences (L31). Law sets the rules for how the table is filled and re-tested.

## §1 The frozen clauses, one by one

### 1. L5 Routing law — REWRITTEN

**Says:** every LLM call goes through the routing layer; out-of-band calls (embeddings, extractor) are routing bypasses.

**Practice diverges:** new-core makes no model calls, so L5 binds nothing in `src/cobalt/`. Seats are CLI sessions on consumer plans (L27.6), not calls through a routing layer. A worker that cites L5 against a seat launch is misreading it. The two old-tree bypasses it was written for are REDESIGN/KILL in TRIAGE (rows 43, 54, 66, 124–125).

**Evidence:** the grep above (18:3x, this seat). The call inventory in TRIAGE:43/:125.

**Proposed text:**
> L5 Engine routing (ruled 08-22; amended <date>). Every model call Cobalt's CODE makes (inference, embedding, extraction, any future call) goes through ONE model-access module. A direct call to a model endpoint from any other module is a defect, killed on sight (L3). Agent sessions that build, check or design Cobalt are not engine calls; their house and model come from the seat table (L26), under L29.

### 2. L24 Three-rung economics, routing sentence — REWRITTEN

**Says:** (1) local = free, first · (2) subscription-agent federation = free (async dead-drop; sync CLI bridges) · (3) metered fast-wire APIs = sync-only, rare, bounded, cost-footered. Pay-per-token = narrowest rung.

**Practice diverges (measured, `reports/seat-usage.md`, 09-16 → 09-22):**
- **Rung 1 (local):** 684–1,067 output tokens a day. That is the day-open verdict and nothing else. Local is not "first" for any seat except that one.
- **Rung 2 (subscriptions):** carries all the work. On 09-22 alone: Opus 5 1.27 M, Sonnet 5 2.43 M, Fable 1.05 M, Opus 5.5 1.01 M, Grok 0.62 M output tokens.
- **Rung 2 is not "free":** it is prepaid and weekly-capped. The meter binds (09-16 Codex at 2 %; 09-22 Codex out until Sat 09-26 06:47, R13; "Fable at 76% for the week", R36).
- **Rung 3 (paid API):** zero engine calls exist. The rung is unused, not narrow.
- "(Grok Bot etc.)" names a vendor in law text (L31).

**Proposed text:**
> L24 Three-rung economics (ruled 08-29/31; amended <date>). The rungs are a COST order, not an assignment: (1) local = zero marginal cost · (2) subscription seats = prepaid and bounded by weekly meters, each meter a monitored resource (L25) · (3) metered APIs = paid per token, engine calls only, sync-only, bounded, cost-footered, the narrowest rung. A task goes to the cheapest rung whose seat the seat table records as passing that task class (L26). Cost never assigns a seat by itself.

### 3. L26 House-agnostic routing — REWRITTEN

**Says:** measured evidence assigns task classes (bake-offs, slice reviews, cost-ledger token-per-outcome). Assignments are recorded in routing config with rationale. Claude recommends against Claude when measurements say so. Assignments are re-tested as local models improve.

**Practice diverges:**
- (a) **No routing config exists.** `configs/cobalt/` has no routing or seat file. `configs/rules.yaml:26` `cortex_routing` is the old tree's intent router, not model routing.
- (b) **Assignments are his rulings, and some carry measurements:**
  - Measured: Gemini as bounded reviewer (09-15 "A", trial Attempt D: 250 s, 0 denials, 1 new verified finding). Grok CAPABLE as checker (audit-house trial 09-16, planted defect found).
  - Meter- or preference-driven: 09-21 R46 checker seats by kind of work; 09-22 R32/R36/R76 Opus 5.5 trial; 09-15 CODEX METER RULING "no Sol builds this week".
- (c) **The bake-off never ran:** the local bake-off has been queued since 09-10 (LEDGER:1143, R12), still "no date".
- (d) **Most tiers were never tested as builders:** Terra has 15,605 output tokens in 14 days (09-10, 09-13), Haiku ≤ 9 k a day. LEDGER:1325: "TERRA AND SONNET … HAVE NEVER BEEN TESTED AS BUILDERS."
- (e) **Law is baked into a config string:** the seat-usage role hints in `configs/cobalt/seat_usage.yaml` read "L29 floor" and "L29 ceiling for this tier" (visible in every `seat-usage.md` day).

**Proposed text:**
> L26 House-agnostic routing (ruled 08-29/31; amended <date>). Right intelligence for the right task, across houses. Every seat assignment is ONE row of the seat table: task class, house, model id, meter, evidence, date, re-test trigger. Evidence is one of two kinds, named on the row: MEASURED (a trial report, a bake-off, a check record, a cost-ledger figure, each with its n) or RULED (his ruling, cited by date and R-number). A ruled row stands (Dejan rules). It is marked ruled, never passed off as measured. The assignment key is the SPEC CLASS (§4). A seat's model is re-tested on the triggers in §5. The house that would lose a seat by a measurement says so (the Claude-against-Claude clause, house-neutral). Model ids live in the table, never in law text (L31).

### 4. L27 routing sentence — OPEN FOR DEJAN (D2)

**Says:** "Codex is the OVERFLOW valve, never the main line — local first, Claude where it is the floor or best fit, Codex when a Claude meter binds; all of the Codex weekly allowance used each week, most of it on Astra."

**Practice diverges:**
- One house is not "overflow." L67 (09-18) made its top model a standing design-tribunal seat, and 09-21 R46 made its implementation model the standing code checker.
- The allowance does not go unused. It ran out mid-week twice (09-16 at 2 %; 09-22 out until 09-26).
- Three vendor names appear in law text (L31).
- The sentence sets a house's economic role, which is Dejan's call, so the proposer does not pick.

**Evidence:** `areas/cobalt-houses.md` 09-15/09-16 meter lines; `cto-2026-09-22.md` R13; L67 [amended 2026-09-21].

**Option A text (house-neutral):**
> Each house's weekly allowance is planned in the seat table: none is left idle by design, none is spent past its ceiling, and a bound meter moves the seat to the fallback its row names (L47). Never money.

### 5. L29 Model rule — REWRITTEN, with one OPEN FOR DEJAN (D1)

**Says (15 clauses, audit §1b):**
- **Write-path floor:** a write path (vault/DB write, migration, delete, recovery, forensics) runs on the house's top implementation model; Opus 5 is the floor and Fable is at his call.
- **Any house, any seat:** allowed once the floor is met and a permission gate is scratch-proven.
- **Lower tiers:** Sonnet/Haiku (and equivalents) do non-write mechanical work only.
- **Auto mode:** granted per session; never on a write path.
- **Plans:** consumer plans; API keys for the engine.
- **No house privileged.**
- **OpenAI roles:** Sol is the floor and Astra the reviewer; plan review is two parties, ≤3 rounds.
- **Sol profile:** workspace-write, network on, cannot commit.
- **Sessions:** cleared every turn, one wake-up.
- **Architect seat:** any house by his ruling.

**Practice diverges:**
1. **Sonnet 5 already runs production deploys.** Where the deploy has no write path, practice applies L29 by reading. `prompts/2026-09-21/11-panel-order-deploy.md` line 1: "WHY NOT OPUS: … no migration, no settings write, no DB write, no vault write … its rollback is a `git revert` of code, not a data recovery. No L29 floor applies." Four such deploys ended DEPLOY DONE, rollback not used (`deploy-2026-09-21`, `-21b`, `-21h`, `-22` STACKED, 2 branches). The rubric is already in use without a name.
2. **The named model is stale.** "Opus 5 floor": Opus tasks run on Opus 5.5 since 09-22 13:20 (R32), and Fable-type seats are asked per seat (R76). A model id in law text goes stale on every release (L31).
3. **"Two parties, ≤3 rounds" is superseded** by L67 [amended 09-18 R20] (four houses, ≤3 rounds each) but still sits in L29.
4. **The floor was read wider than written.** The 09-07 local verdict read it as "never a write path (floor is cloud top-tier)" (LEDGER:906-907), which is not in the text. LEDGER:1325 records that Astra "cites [it] to declare houses INELIGIBLE without assessing anything."
5. **No launch shape is proven to satisfy "never auto mode on a write path".** It is not proven unattended *and* dialog-free (L63 state note; `acceptEdits` asks on unlisted Bash). The deny-unlisted scratch test is still owed.
6. **The write path does not tell dev from production** (audit C5). A `cobalt_dev` migration and a `--allow-prod` one bind alike.

**Why the floor exists (audit C11 §2a):** the 09-03/04 daily-note overwrite (LEDGER:615-632). It protects **his notes and the production DB**, not code quality.

**Proposed text:**
> L29 Write-path seat rule (ruled 09-03/04; amended 09-07, 09-10, 09-12, 09-13, <date>). A WRITE PATH is a vault or DB write, migration, delete, recovery or forensics. A session on one runs only when (1) its model is the house's top implementation model, OR the seat table (L26) records that model PASSED for that task class by a measured trial (§5) — [D1] · (2) the house's permission gate is proven in a scratch test to stop file AND command writes outside the session's workspace · (3) its launch line states its permission mode, never auto mode (L62). A session with NO write path (a production deploy that fast-forwards code and restarts residents with no migration, settings, DB or vault write included) takes its model from the seat table by task class. Any house may hold any seat on these terms; no house is privileged. The architect seat is assigned to any house by his ruling, another house reviewing. Code sessions are cleared every turn: durable state lives in the plan file and the report, and one scheduled small-context wake-up is permitted.

**L29 clause trace (nothing dropped; audit §5 checks .6 by name):**

| clause | goes to |
|---|---|
| .1 write-path floor | new L29 (1) + D1 |
| .2 Fable at his call | seat table (ruled rows; R76 is the current form) |
| .3 any house once floor + gate | new L29 (2), "any house" sentence |
| .4 Sonnet/Haiku non-write only | seat table: an untested tier has no PASSED write row. The ban becomes a default, not law |
| .5 auto mode per session, never blanket | already L55.1, removed as a duplicate |
| **.6 never auto mode on a write path** | **new L29 (3), kept verbatim in substance** |
| .7 consumer plans / API keys | already L27 [09-10], removed as a duplicate |
| .8 no house privileged | new L29 |
| 09-10 OpenAI roles | seat table rows (model ids out of law) |
| 09-10 plan review two parties ≤3 | superseded by L67 R20, moved to LAWS-HISTORY |
| 09-10 writer profile (`-s workspace-write`, network on, never `danger-full-access`, cannot commit) | L33 as its writer launcher profile |
| 09-10 cleared every turn + one wake-up | new L29 last sentence |
| 09-12 architect any house | new L29 |
| 09-13 O12 restore note | stays as provenance |
| status note (LEDGER:906-907, :1325) | retired: this rewrite answers it |

### 6. L49 Local-seat doctrine, the "routing tribunal may touch" marker — REWRITTEN (marker off, text kept)

**Says:** the local seat reads and judges and never composes; no long output; a cost estimate up front; its only write path is a Cobalt command.

**Practice matches it exactly (§3).** The local seat runs one job, the day-open. Dejan launches it by hand in the Qwen1 pane. It runs `cobalt day-open` and writes a one-line `SEAT VERDICT` through `cobalt day-open verdict`. That is 684–1,067 output tokens a day from 09-16 to 09-22, GREEN every day (`day-open-2026-09-2{0,1,2}.md:163-175`).

**Where it collides:** with L23 ("LOCAL = first candidate for every task"), not with practice (audit C11). §1.7 below fixes L23 instead.

**Evidence for the doctrine:** 09-11 ~7 k report tokens took 20+ min of a 50-min run (LEDGER:1185); 09-13 an API death on leaked think tags (LEDGER:1325). Against it: the `/no_think` fix measured a tool turn at 21.3 s → 5.8 s (LEDGER:1120 era, 09-09 Phase A2). That fix predates both failures, so it does not refute them.

**Proposed:** keep the text and remove the marker. The local seat's WIDER use goes through §5 trials, not a law edit. Local-as-hub is D3.

### 7. The cluster (L21, L22, L23, L25) — frozen with the above; smallest edits only

| law | proposal | why (evidence) |
|---|---|---|
| L21 | unchanged | a principle, no divergence found |
| L22 | wording only: "Max subscription and Anthropic API" → "a house's subscription and its API are separate meters" | L31 (vendor names). Substance is ENGINE routing and stands |
| L23 | amend: "LOCAL = first candidate for every task" → "LOCAL is the first candidate ASSESSED for every task class: it is assigned where the seat table records it passing, and every other class records why not." Drop the status note and replace it with the seat table's local rows | resolves audit C11 (A vs B/C): "first assessed" survives L49 and L29; "first assigned" survives neither. The continuity rationale (08-28 outage) is kept whole |
| L25 | (a) "fix local, or move that task class to cloud explicitly in **ADR-0008's bake-off table**" → "…in **the seat table**". (b) "Claude → next-best house" → "the seat's house → the next row the seat table names" | (a) **ADR-0008 has no bake-off table**: `grep -i bake-off "docs/10 - Decisions/"` returns nothing, so the law points at nothing (ESCALATE 1). (b) L31 |

## §2 The seat map as it runs today (22 Sep, 18:3x)

Sources: `cto-2026-09-22.md` §5 (16:2x) and R13/R32/R36/R73/R76, 09-21 R46, `areas/cobalt-houses.md`, `seat-usage.md` 09-22, deploy prompts 09-21.

| # | house | seat | model id | meter | evidence kind |
|---|---|---|---|---|---|
| 1 | Anthropic | CTO desk | `claude-opus-5-5` | subscription weekly; refreshed full 09-22 (R74) | RULED R36/R76 (trial, "until his evaluation") |
| 2 | Anthropic | hubs (tribunal, check, build-lane) | `claude-sonnet-5` | same | RULED/practice; 09-13 six correct STOPs (LEDGER:1325) |
| 3 | Anthropic | production deploy hub, no write path | `claude-sonnet-5` | same | MEASURED: 4 × DEPLOY DONE 09-21/22, 0 rollbacks |
| 4 | Anthropic | production deploy hub WITH migration/settings write | `claude-opus-5-5` (was Opus 5) | same | RULED L29 floor (`02-deploy-stack-3.md`) |
| 5 | Anthropic | builder / fix builder | `claude-opus-5-5` | same | RULED R32; builds on the L75 record |
| 6 | Anthropic | prompt drafter | `claude-opus-5-5` | same | RULED R32/R36 |
| 7 | Anthropic | design-tribunal seat, derive seat | per seat: `claude-opus-5-5` or `claude-fable-5-1` (asked, R76); DRC `41`/`42` Fable (R73) | same; "Fable at 76% for the week" (R36, 13:45) | RULED |
| 8 | Anthropic | code checker | `claude-opus-5-5` (`claude -p`) | same | RULED R46 + R32 |
| 9 | OpenAI | design-tribunal seat | `gpt-6-astra` | Codex weekly; OUT until 09-26 06:47 (R13) | RULED L67/R46 |
| 10 | OpenAI | code checker | `gpt-5.6-sol` | same allowance as row 9 | RULED R46 |
| 11 | OpenAI | builder | `gpt-5.6-sol` | same | RULED 09-10; no build seat held since 09-15 (meter rulings) |
| 12 | OpenAI | triage / builder candidate | `gpt-5.6-terra` | same | NONE: 15,605 output tokens ever |
| 13 | xAI | design-tribunal seat, code checker, blind code seat | `grok-4.7-build` | subscription; `grok` rule strings dated to 09-23 23:59 (R30) | MEASURED: audit-house trial 09-16 CAPABLE |
| 14 | Google | design-tribunal seat, code checker | Gemini 3.1 Pro under `agy` | subscription, two weekly buckets | MEASURED: trial Attempt D 09-15; RULED "A" |
| 15 | local | day-open verdict | `mainframe` (Qwen3.8-27B 8-bit) | zero marginal | MEASURED: GREEN daily; ~0.7–1.1 k tokens/day |

Not seated: Haiku (a few small hub-side runs, ≤ 9 k output a day), the Cobalt engine (no model calls). **Measurement gaps:** agy usage is not in `ccusage`; the Codex meter is known only by probe; the cost of `claude-opus-5-5` and `claude-fable-5-1` is UNPRICED in the pinned table.

## §3 The local seat's real role (L49)

- **Today:** one read-and-judge job, the day-open verdict, launched by his hand, written only through a Cobalt command. The doctrine holds; nothing contradicts it.
- **Not today, and not tested since 09-13:** hub, builder, report author. The plan of record (LEDGER:1325) is the local seat as Cobalt's hub. The bar is higher than the morning check: holding a dispatch's rules across a long session and STOPPING on a proof mismatch. Evidence: two harness failures (09-11 stuck process, 09-13 think-tag death), zero hub trials.
- **Next lawful widening (for the tribunal, T10):** a read-and-judge CHECK role. Example: a class-S diff against its spec, output capped at a verdict table. Run as a §5 trial beside a cloud checker, never replacing one until PASSED.

## §4 The assignment key: spec class (LEDGER:1325's axis, his words)

- **Class S (specified):** "the spec is defensible against a real-world artifact and testable." There is nothing to infer, and a wrong guess fails visibly. The lowest tier that PASSED this class in the seat table may take it.
- **Class H (horizon):** "a new horizon with undefined outcomes." It needs a model that will notice the spec ITSELF is wrong, so it takes the top seat. This matches 09-21 R46: "For the designs and creations we need the higher level models."
- **W overlay:** a write path adds L29's three conditions to either class.

**Honest caution (LEDGER:1325, carried in):** asking a model to judge another model's competence is the judgement models are worst at. The rubric binds only once it is **validated retrospectively** against known outcomes (T6). This proposal did NOT produce that validation. Data points it found:

| build / run | class (proposed reading) | seat | outcome |
|---|---|---|---|
| S2-P1 radar pool, 09-10 | H disguised as S: spec written against an imagined note (L45 origin) | Sol | 1213 / 1 failed, NOT READY; 7 extraction defects found 09-12 |
| 4 production deploys, 09-21/22 | S, no write path | Sonnet 5 | 4 × DONE, 0 rollbacks |
| 09-13 dispatches | S (hub) | Sonnet 5 | 6 correct STOPs (LEDGER:1325) |
| chunk 1a / chunk 2 fix rounds, 09-20 | S | Opus 5 | FIX 13 / FIX 6, built in 12 / 17 min (L75) |
| day-open, 09-16→09-22 | S, read-and-judge | local | GREEN daily |

The first row supports the axis: the failure came from class mis-reading, not from model tier.

## §5 How a seat assignment is re-tested

- **Triggers (any one):**
  - (a) a house ships a new model id (09-22 Opus 5 → 5.5 is the live case, and today it is being assigned by trial ruling, not by measurement);
  - (b) a meter change makes a cheaper row attractive;
  - (c) a seat's class-S builds draw more HOLD findings at check than the table's baseline;
  - (d) Dejan asks.
- **Procedure: a SHADOW BUILD (the L7 pattern applied to seats).**
  - The candidate model builds the same checked, class-S prompt in its own worktree, beside or after the incumbent, on the same base tip.
  - Both go through the same L67 check (three checkers) and the same offline + with-DB gate.
  - No shadow build ever merges.
- **PASS bar:**
  - gate green on both suites;
  - HOLD findings ≤ the incumbent's on the same prompt;
  - no false completion or failure claim (L35, L70);
  - wall-clock and meter recorded.
- **Recording:** the seat-table row names the trial report and its n. An n = 1 pass is a spot check, stated as such. A class-level PASS needs the n the tribunal sets (T8).
- **Law steps:** a trial is its own lane (L72) and never holds a build. Promoting a row off a trial is his approval, one message (L7 shape).

## §6 What the tribunal must rule (12)

| # | question | this proposal's position |
|---|---|---|
| T1 | Split ENGINE routing (L5, L22, L24 rung 3, L25) from SEAT routing (L26, L29, L49)? | yes (§0) |
| T2 | L5 text | §1.1 |
| T3 | L24 text: cost order ≠ assignment | §1.2 |
| T4 | The seat table's FORM and home. A committed `configs/cobalt/seats.yaml` with a Pydantic schema and dry-run (L10), or a `50 - Roles/` doc that replaces the stale `MODELS.md` (still lists `claude-fable-5`; R32's ops item) | YAML under `configs/cobalt/` (outside the old glob), rendered to `MODELS.md` |
| T5 | The class S / H key + W overlay (§4) | adopt |
| T6 | Retrospective validation: every build 09-10 → 09-22 tabled (class, seat, check HOLDs, gate, outcome). The rubric binds only if it predicts the known outcomes | required before T5 binds; owner = a hub job |
| T7 | L29 text + trace (§1.5) | adopt; check .6 by name |
| T8 | Re-test procedure + PASS bar + the n for a class-level PASS (§5) | shadow build; n per the tribunal |
| T9 | L23 "first assessed", L25 pointer + vendor names, L22 wording (§1.7) | adopt |
| T10 | L49 marker off; the local seat's next trial role (§3) | read-and-judge checker trial |
| T11 | FIRST TRIALS, from his three open questions (LEDGER:1325): can Terra build what Sol builds? Is Sonnet a builder as well as a hub? Is Haiku enough for the hub seat? | schedule one class-S shadow build each for Sonnet 5 and Terra; one Haiku hub trial on a read-only tribunal hub |
| T12 | Measurement gaps: agy usage capture, a Codex meter readout, seat-usage role hints regenerated from the seat table (they cite "L29 floor/ceiling" today) | ops items, owners named |

## §7 What only Dejan rules

**D1 — the production write-path floor.**
- **A:** a PRODUCTION write path (live vault, production DB, `--allow-prod` migration, `trader_settings` write, recovery/forensics on production) always runs on the house's top implementation model. Only DEV write paths (`cobalt_dev`, dev vault, worktree) can be earned down by trial.
- **B:** the same trial rule everywhere.
- **Recommend A.** The floor exists because his notes were overwritten (09-03/04). Production writes are rare (one Opus deploy row in the seat map), so A costs little meter. Every trial runs on dev anyway, so B's evidence could never come from production.

**D2 — L27's routing sentence.**
- **A:** replace it with the house-neutral allowance sentence (§1.4), with each house's role living in the seat table.
- **B:** keep the sentence as written.
- **Recommend A.** Practice already contradicts "overflow" (standing tribunal and checker seats). The allowance is exhausted, not under-used. The sentence names three vendors in law text (L31).

**D3 — the local seat as Cobalt's hub (plan of record, LEDGER:1325).**
- **A:** keep it as plan of record, gated on a measured hub trial (T10/T11 shape) that the seat table records. No hub use before a PASS.
- **B:** retire it as plan of record, and the local seat stays read-and-judge.
- **Recommend A.** Nothing measured says a 27B cannot hold a hub, and nothing says it can. The trial is cheap on a zero-marginal meter, and L49 already caps the cost of a bad run.

## §8 Sources read

LAWS.md (full, applied 17:4x) · LAWS-HISTORY H-L27, H-L29a–e · `laws-audit-2026-09-20.md` C5, C11, §2b, §4b · `LAWS-CONSOLIDATION-COMPARE-2026-09-22.md` · LEDGER:21-30, :873-880, :900-912, :1115-1125, :1138-1152, :1160-1168, :1180-1190, :1236-1256, :1308-1335 · ADR-0008 (D6; no bake-off table) · `MODELS.md` · `areas/cobalt-houses.md` · `cto-2026-09-22.md` R13/R32/R36/R73/R74/R76/R81 + §5 · `cto-2026-09-21.md` R46 via L67 · `seat-usage.md` 09-09 → 09-22 · deploy prompts/reports 09-21/22 · `src/cobalt/` grep.
