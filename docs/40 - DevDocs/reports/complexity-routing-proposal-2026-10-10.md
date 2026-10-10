# Model-by-complexity rule · design proposal for the tribunal · 2026-10-10

Proposer: Opus 5.5 drafter `complexity-propose` (L67: one house proposes; Fable · Astra · Grok rule, Gemini optional).
Asked by: brain plan `reports/s5-weekend-and-parked-answer-2026-10-10.md` (NOT-MVP rows "Model-by-complexity tribunal", "JEV router ruling"); his R73 10-02 (`docs/00 - Project/PROJECT-LEDGER.md:2704`: wait at least a week, record per-job stats first); his R8 10-03 (`cto-2026-10-03.md:14`, `areas/cobalt-houses.md:27`: the router waits for this tribunal and the JEV picker).
Frozen: L5, L21–L27, L29. This proposal amends none. It proposes a rule to run in SHADOW and a trial; a law edit, if any, comes after the tribunal reads the shadow data.

## §0 Headline
- Per-job stats exist since 10-05: 27 next-flow checks and 26 builds carry a `tokens:` MEASURE in their stop line. n=27 < 30: every per-band number below is "insufficient data" under L8.
- Every build and every check in that sample ran on Opus 5.5 (L29 floor, BUILD-HUB:3, L67 check flow). The data has ZERO model variance: it measures cost per job, not model-versus-outcome. No routing claim can be derived from it.
- Card size does not predict check outcome in this sample: two 1–2-row cards drew 11 held findings each (`guard-g2`, `radar-ladder-refresh`).
- Proposal: compute a complexity score at launch from the card, LOG it beside the seat actually used (shadow, L7-style), and run ONE trial in the only lane the frozen laws leave open: non-write drafters, Sonnet vs Opus. Builds and checks stay Opus.
- Money effect: none in dollars (L27: Max plan, minimum tiers). The effect is on the weekly Claude meter only, and it is UNKNOWN until the trial runs.

## 1. The data actually found

### 1.1 Sources
- Stop lines of `reports/*-build-2026-10-*.md`, `*-check-2026-10-*.md`, `*-fixround-2026-10-*.md` (L71: each worker's stop line carries `tokens: <n>`).
- Desk rows with touches: `cto-2026-10-06.md:48` (flake-fix-2: 1 build + 1 check), `:160` (card 39 drc-d5-o1-b2: 1 build + 1 check + 1 fix round, 219,290 + 198,504 + 128,005).
- Recut/deploy failures with tokens: `cto-2026-10-07.md:48` (radar-direction-color attempt 2, 113,286), `cto-2026-10-08.md:29` (desk-ops-fixes attempt 2, 84,201), `cto-2026-10-10.md:55` (https-only attempt 2, 98,148).
- Before 10-05: no per-job tokens (`gain-measure-survey-2026-10-05.md:14`).
- Drafters, preflights, tribunal hubs: no systematic per-job MEASURE found in the reports read (only desk rows like `cto-2026-10-05.md:76,80`: guard-b drafter 52,252, preflight 53,874, P7 drafter 71,497). Count: UNKNOWN (L70).
- Seat usage: day totals only; Opus and Sonnet are **unpriced** in `seat-usage.md:29-37` (10-10). `weekly_pct_open`/`close` are blank.

### 1.2 Per-job rows, next flow (house A Sol + house B Grok at once), 10-06 → 10-10
All builds and checks: Opus 5.5. `rows` = card rows built. `DB` = takes `cobalt_dev` and restarts aset/radar. `held` = findings the check ran and held.

| job | rows | DB / migration | build tokens | check tokens | findings | held | ready |
|---|---:|---|---:|---:|---:|---:|---|
| flake-fix-2 | 1 | DB | 230,163 | 203,860 | 10 | 1 | YES |
| guard-g2 | 1 | — | 273,887 | 216,430 | 15 | 11 | YES |
| launcher-next-flow | 3 | — | 273,122 | 191,425 | 4 | 0 | YES |
| radar-ladder-refresh | 2 | DB | 172,093 | 181,164 | 12 | 11 | YES |
| drc-d5-o1-b2 | 4 | DB | 219,290 + fix 128,005 | 198,504 | 4 | 2 | NO → 1 fix round |
| desk-stop-guard | 6 | — | 197,604 | 174,440 | 9 | 5 | YES |
| radar-arm-disarm | 5 | DB | 232,402 | 165,017 | 6 | 0 | YES |
| radar-direction-color | 4 | DB | 165,689 | 148,149 | 3 | 1 | YES (deploy failed twice at gate c3, environmental) |
| worktree-salvage | 7 | — | 206,624 | 175,727 | 7 | 4 | YES |
| desk-ops-fixes | 3 (fix round) | — | 145,252 | 101,004 | 11 | 1 | YES (after 1 fix round, R669) |
| stt-model-fix | 3 | DB | 200,409 | 188,056 | 6 | 4 | YES |
| price-floor | 7 | DB, migration 0023 | 397,831 | 228,719 | 3 | 1 | YES |
| radar-display-fix | 6 | DB | 179,901 | 176,294 | 6 | 3 | YES |
| guard-g2-open-reads | 3 | — | 215,263 | 227,244 | 11 | 7 | YES |
| disarm-one-tap | 5 | DB | 194,339 | 172,187 | 7 | 0 | YES |
| arm-unsized | 4 | DB | 182,519 | 182,250 | 5 | 0 | YES |
| desk-pane-by-id | 4 | — | 108,051 | 141,671 | 4 | 1 | YES |
| guard-d1 | 6 | — | 159,100 | 215,804 | 15 | 9 | YES |
| guard-d2 | 6 | — | 174,620 | 184,393 | 8 | 7 | YES |
| radar-top50 | 4 (fix round) | DB | 93,357 | 153,816 | 9 | 1 | YES (a void re-check, R758) |
| stop-guard-g7 | 5 | — | 136,922 | 160,632 | 11 | 4 | YES |
| voice-clarify-fix | 5 | DB | 179,120 | 161,041 | 4 | 0 | YES |
| s4-p1 | 8 | DB | 415,769 | 259,254 | 11 | 4 | YES |
| s4-p2 | 9 | DB, migration 0024 | 423,747 | 238,152 | 9 | 4 | YES |
| archiver-429 | 3 | DB | 227,362 | 207,006 | 9 | 5 | YES |
| strike-fallback-env | 2 | DB | 165,478 | 138,173 | 2 | 1 | YES |
| https-only | — (build report not in main) | DB | UNKNOWN | 180,198 | 10 | 3 | YES (recut attempt 2 FAILED merge) |

### 1.3 Totals (n=27 checks, n=26 builds: insufficient data, L8)
- Build tokens: sum 5,478,629; median ≈181,000; range 93,357–423,747.
- Check tokens: sum 4,970,610; median 181,164; range 101,004–259,254.
- Held findings: 90 across 27 checks; 5 checks held 0; 1 check ready NO.
- The three most expensive builds (s4-p1, s4-p2, price-floor) are the three largest cards (7–9 rows; two migrations). Below 7 rows, row count tracks neither tokens nor held findings.

### 1.4 What the data cannot say
- Whether a cheaper model would have produced the same outcome: no job ran on two models.
- Deploy outcome per job: deploy attempts are in desk rows, not tallied here (three failed recuts found above). UNKNOWN as a per-job column.
- His touches per job (R107 10-03): two desk rows only. UNKNOWN for the rest.

## 2. What a complexity score could be derived from
Every input below is on the card or its BASE before launch; none reads an outcome (the routing tribunal's 09-22 finding (e): a key that reads outcomes into the class is not deterministic).

| input | source at launch | weight (proposed) |
|---|---|---:|
| W: write path (vault/DB write, migration, delete, recovery, forensics) | card `RESTARTS`, `migration`, L29 definition | gate, not a weight |
| R: card rows | card row count | 1 per row over 3 |
| M: migration | card names one | +3 |
| S: services restarted | card `RESTARTS` | +1 each |
| X: seams (files shared with another open card) | seam doc, LAWS:363 | +2 each |
| H: new horizon (no precedent card or design to copy) | the drafter's launch row (`cto-desk-contract.md` Seats, 09-27 line) | +4 |
| $: touches money, sizing or his vault notes | card; L67 MANDATORY HOUSE B trigger | +3 |

Score = R + M + S + X + H + $. Bands: LOW 0–2 · MID 3–6 · HIGH ≥7. Band cut points are modelled, not measured (L52(a) spirit): the trial sets them.

## 3. Seats it would choose between, and where the laws already decide

| seat kind | candidates | decided today by | can the score move it? |
|---|---|---|---|
| Build (write path) | Opus 5.5 / Fable 5.1; Sol (OpenAI floor) | L29 floor, BUILD-HUB:3 | Only UP: HIGH may propose Fable to him (contract Seats, 10-04 line). Never below Opus. |
| Build (no write path) | Sonnet / Opus | L29: "Sonnet non-write mechanical only" | Not in this proposal (Q3). |
| Check | fresh Opus + Sol + Grok (Gemini by seat order) | L67 BUILD CHECK FLOW | No. |
| Design proposal / tribunal seat | Fable (as Opus) · Astra · Grok · Gemini | L67 SEATS BY KIND | No. |
| Drafter, card drafter, preflight, tribunal hub (non-write) | Sonnet 5.5 / Opus 5.5 | contract Seats 09-25, 09-27 lines (precedent → Sonnet; judgment → Opus) | YES: the trial lane. |
| Mundane read/format work | mainframe (Qwen local, L23) / Sonnet | L23 local-first | Not in this proposal (X5 retro owns it). |
| Astra / Sol / Terra | OpenAI family top model per contract 09-28 line | L29 house roles, contract | No. |

The only lane where a complexity rule can choose a model without touching a frozen law is the non-write drafter/preflight/hub lane, and the up-escalation of a HIGH design or build to Fable on his word.

## 4. The rule (proposed)
1. At every launch the desk writes `complexity: <score> <band> (R<r> M<m> S<s> X<x> H<h> $<d>)` into the launch row. It changes no seat. (Shadow.)
2. Non-write drafters, preflights and hubs: LOW → Sonnet 5.5; MID or HIGH → Opus 5.5. This restates the 09-27 precedent rule with a number; it applies only after the trial in §5 passes.
3. HIGH builds and HIGH design proposals: the desk names Fable 5.1 to the brain; the brain asks him (contract Seats, 10-04 line). No automatic Fable.
4. Builds, checks, tribunal seats: unchanged (L29, L67).
5. The JEV picker, when it lands (R8), receives the same score as an input feature and runs in shadow beside this rule to 80% agreement; the higher-agreement router decides only after that.

## 5. How it is measured against outcomes

### 5.1 Shadow log (all jobs, from the first launch after the tribunal)
- Per job: score, band, seat used, tokens (stop line), fix rounds, held findings, ready, deploy attempts to DEPLOYED, his touches.
- Read at n≥30 per band (L8). Expect ~5 builds a day at the 10-06→10-10 rate (26 in 5 days); MID fills first, LOW and HIGH may take weeks.
- Test: does band predict held findings, fix rounds and tokens better than row count alone? If not, the score is retired, not tuned.

### 5.2 Trial (the non-write lane only)
- Class: card drafters and preflights scored LOW.
- Arms: Sonnet 5.5 vs Opus 5.5, alternating by launch order (no desk choice per job).
- Outcome: preflight ready on first run (drafter arm); a planted-mismatch STOP (preflight arm, per the 09-22 routing tribunal's T11 known-answer replay); downstream build fix rounds.
- PASS for Sonnet: n≥30 per arm, first-run ready rate within 5 points of Opus, zero missed planted mismatches.
- Result recorded in the seat table with rationale (L26); his ruling makes it a row.

## 6. Meter and money effect (L27)
- Dollars: zero change. Claude is the Max plan; Grok and Codex stay at minimum tiers; no top-up.
- Meter: builds and checks dominate (≈10.4 M tokens over 53 runs in §1.3), and the rule does not move them. The trial lane (drafters, preflights) is 50–70 k tokens a job where measured; a Sonnet shift there saves a small share of the weekly Claude meter. The size is UNKNOWN until drafter MEASURE rows exist.
- HIGH → Fable raises the Opus/Fable meter draw on the few jobs it touches; each one is his word.
- The shadow log costs one launch-row field; no new session.
- Prerequisite: drafters and preflights must carry `tokens:` in their stop line (L71 already requires it; the reports read do not show it).

## 7. Not in scope
- Any edit to L5, L21–L27, L29, L67.
- Moving any write-path build below Opus, or any check off the L67 flow.
- House choice (Astra/Grok/Gemini seat order) and the X5 routing retro (local lane).
- The JEV trial itself, its merge, and R34 "which house is JEV".
- Effort level within one model.
- Pricing the unpriced Opus/Sonnet rows in `seat-usage.md`.

## 8. Questions for the tribunal (each with a default)
- **Q1. Is a shadow log at launch worth a launch-row field before any routing changes?** Default: YES, shadow first (L7 pattern).
- **Q2. Are the inputs R, M, S, X, H, $ the right ones, and is H (new horizon) a fair launch-time input or a desk judgment in disguise?** Default: keep all six; H is set by the drafter's own launch row, already required by the 09-27 Seats line.
- **Q3. Should non-write BUILDS (docs-only, ops scripts without DB) enter the Sonnet trial?** Default: NO; L29 reads "mechanical work only", and these builds run the full gate (L68).
- **Q4. Band cut points 0–2 / 3–6 / ≥7.** Default: keep as modelled; reset at n≥30 per band from the shadow log.
- **Q5. Trial PASS bar: first-run ready within 5 points of Opus and zero missed planted mismatches.** Default: keep.
- **Q6. HIGH → Fable: name to him per job, or never?** Default: name per job via the brain, no automatic seat.
- **Q7. Does the JEV picker consume this score as a feature, or route blind and be compared against it?** Default: compare blind; the score is the baseline it must beat to 80% agreement (R8).
- **Q8. Retire the score if band does not beat row count at n≥30?** Default: YES, retire.
