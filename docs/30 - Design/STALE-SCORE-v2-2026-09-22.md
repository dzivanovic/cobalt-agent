# STALE SCORE — v2 (derived 2026-09-22)

Derived by seat `stale-score-tribunal-derive-0922` (Fable 5.1, `claude-fable-5-1`, the Fable seat's second job under row R51 of `reports/cto-2026-09-21.md`) from `prompts/2026-09-21/63-stale-score-tribunal-derive.md`. This is the proposal, whole, with each amended paragraph REPLACED in place and tagged `[F-nn]`; the fold table is `reports/stale-score-tribunal-derive-2026-09-22.md` `## Fold table`. Every `[F-nn]` text is a house's wording taken word for word, or the proposal's own text kept; nothing here was written by the derive except cross-references and the answers recorded in §8.

**Inputs.** Proposal: `docs/30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md` (all `file:line` on MAIN at `031196f`; the derive re-read three ranges on main at `3ceb469`, named where used). Round-1 rulings: hub `reports/stale-score-tribunal-2026-09-22.md` (stop line `STALE SCORE TRIBUNAL R1 DONE`, committed `5f8d6ea`); Grok `scratch/tribunal-bars-0920/stale-score-tribunal/r1/grok-ruling.md` (ruled in full, `TRIBUNAL R1: BUILD AFTER C1 lands, before the A-01 ruling`); Gemini `…/r1/gemini-ruling.md` (ruled in full, `TRIBUNAL R1: BUILD AFTER a separate version bump is added and tap_dot reason drop is fixed`); Fable `reports/stale-score-tribunal-fable-r1-2026-09-22.md` (row R51 `Fable seat: yes`; ruled in full, blind, `TRIBUNAL R1: BUILD AFTER the derive, on a tree that already carries setups/seven-0921`, committed `be4c79b`); **Astra: `METER` — did not rule** (`cto-2026-09-22.md` §4 R13 "A": this week's design tribunals run on Grok · Gemini · Fable without Astra; Codex meter returns Sat 2026-09-26 06:47 ET). Every item below was ruled by 3 of 4 seats; the Astra column is `ASTRA PENDING (R13)` throughout — Astra reads this v2 when its meter returns. No house returned `REJECT` or `DO NOT BUILD`; `## NEEDS ROUND 2` in the derive report is EMPTY, so the tribunal closes and this v2 is the FINAL's input.

Ladder: `S2-P2 · F10 Dots / ladder` (a defect in what is live). Origin: `reports/stale-marker-design-2026-09-21.md` ESCALATE 1; `reports/setups-tribunal-r2-2026-09-21.md` ESCALATE 3. PROVEN = read in the file. UNPROVEN = not checkable from reads (L70) → an experiment in §7.

## 1. Fact base

### 1a. Every writer of `last`, `proximity`, `card_score`, a dot, or the ladder order

| # | Claim | file:line | |
|---|---|---|---|
| W1 | **Staleness is known at evaluation.** `intraday_stale` = no closed i1 bar today, OR the last bar's close older than `2 × radar.scan_interval` (ttl 200 s at 100) | `radar/evaluate.py:529-534`; `anatomy/freshness.py:106-120`; `tunables.yaml:467-468` | PROVEN |
| W2 | It is used three ways: no formation (`input_stale` return), stale flag on `atrs_from_open` and `Extension.leg_count` | `evaluate.py:598-599`, `:439`, `:459` | PROVEN |
| W3 | It is NOT stored as its own field on `MemberEvaluation`. `evaluation="input_stale"` has two meanings: intraday-stale (`:599`) or daily bars missing (`:624`, `:629`) | `evaluate.py:340-364`, `:599`, `:624`, `:629` | PROVEN |
| W4 | `htf_level_proximity` is computed FROM `last_price` with NO stale flag, even when intraday-stale | `evaluate.py:463-477` | PROVEN |
| W5 | **Refresh writer (stage):** every open card whose def still loads is refreshed. There is no evaluation-state guard | `evaluate.py:1317-1349` | PROVEN |
| W6 | `refresh_card` takes `last = ev.last_price`, the last closed stored bar however old. If there is no bar today it falls back to `card.entry`, which gives **proximity = 1.000000, the maximum** | `evaluate.py:776-778`; `scoring.py:254-261` | PROVEN |
| W7 | `refresh_card` returns `last_price=ev.last_price` (stale price included) | `evaluate.py:803` | PROVEN |
| W8 | **Row writer (refresh):** `refresh_radar_card` writes `proximity`, `last_price = COALESCE(new, old)`, and (no newer tap) `conviction, card_score, score_suppressed, proposed_key`. It then upserts every dot | `cards/store.py:1016-1053` | PROVEN |
| W9 | Same writer, when a tap landed after the stage read: it writes `proximity`/`last_price` and leaves `card_score` as the tap route computed it, which uses the OLD proximity. This is a one-scan inconsistency that exists today whether the bars are stale or not | `store.py:1029-1037` | PROVEN |
| W10 | **Tap writer:** `tap_dot` recomputes conviction, `suppression(dots)` and `card_score` from the stored dots and the STORED proximity. It does not know about staleness. `prox is None → card_score None` is already handled | `store.py:1182-1231` (`:1217-1219`); `scoring.py:264-267` | PROVEN |
| W11 | **Create writer:** a card forms only on `evaluation == "formed"`, so it never forms on stale intraday bars | `evaluate.py:1361-1406`, `:598` | PROVEN |
| W12 | **Seam copy writer:** `copy_card_values` copies proximity/score to `system.radar_score`. Columns are nullable. `[F-12]` Gemini (a), verbatim: "Missed writers: `radar_score` seam table is written in `radar/store.py:423-425` (via `copy_card_values`), missed in W12 which only lists the caller." | `evaluate.py:1356-1358`, `:1431`; `radar/store.py:423-425`; `0006_radar_score.sql:103-106` | PROVEN |
| W13 | `aset_sizings.proximity` / `card_score` are nullable, with no CHECK on either column | `0007_radar_cards.sql:47-48`, `:66-82` | PROVEN |
| W14 | Dots: `compute_dots` marks a stale observation `input_stale` (no grade). `refresh_dots` moves the prior grade into `history` and carries taps | `scoring.py:172-176`, `:201-235` | PROVEN |
| W15 | Suppression holds only while a computed N/A dot is UNTAPPED | `scoring.py:247-251` | PROVEN |
| W16 | **Ladder order:** WATCH by `card_score desc nulls last`, then `pool_position`. Pinned cards (ARMED/TRIGGERED/FILLED) by `pool_position`, then score. ADR-0009 D4: `card_score` alone orders WATCH | `cards/radar.py:167-183`; `evaluate.py:134-138`; ADR-0009:28 | PROVEN |
| W17 | **Replay (L57):** `replay_receipt` re-runs `evaluate_member` on receipt bars + `as_of` + `scan_interval` and re-scores with the same `last` rule. Audit export refuses a run whose recompute ≠ published | `evaluate.py:1043-1089` (`:1079`); `audit_export.py:244-259` | PROVEN |
| W18 | The nightly `com.cobalt.replay` (`replay/cards.py`) replays counterfactual R of unfilled cards. It never recomputes `card_score` | `replay/cards.py:1-57`, grep | PROVEN |
| W19 | `[F-11]` The panel renders `None` proximity/score as `—` and prints `score_suppressed` on the card — the reason line is at `radar_panel.py:998` and the null score chip at `:1023`, not at the proposal's cited `:957` (anchor drift; hub `## Checked against the files`, HOLDS) | `aset/radar_panel.py:998`, `:1023`, `:1039` | PROVEN |
| W20 | The receipt carries nothing from `poll_failures`. The stamp's clock cannot be replayed from a receipt | grep `poll_failures` in `evaluate.py` = 0 | PROVEN |
| W21 | `[F-11]` Only `Rubberband.md` names a computed factor among the live notes (`atrs_from_open`, `rvol`, `Extension.leg_count`, `htf_level_proximity`, `trail_fit`) — Grok (a): "W21 (only Rubberband.md names a computed factor) is `UNVERIFIED` — that vault grep is not in `greps.txt`." | grep of `Vault/Think/1 - Trading` | UNVERIFIED (grep scope; the author's own caveat) |
| W22 | `[F-11]` Grok (a), verbatim: "Add W22: `audit_export.py:363` calls `score_card` with `last = ev.last_price if ev.last_price is not None else trigger`. That is a scorer, not a row writer, and it is not in W1–W21." (hub Checked + FC4, HOLDS; re-read by the derive on main `3ceb469`, `audit_export.py:363-364`) | `radar/audit_export.py:363` | PROVEN |

`[F-11]` Grok (a), verbatim, on the live path: "§1a's live path holds: no evaluation-state guard (`evaluate.py:1317-1348`; refresh at `:1345`; the only continue is a missing def at `:1330`), proximity from the old close or from `card.entry` (`:776`), row write (`store.py:1032-1044`), tap rescore from stored proximity (`:1217-1219`), WATCH order (`cards/radar.py:179-183`)."

### 1b. The sequence that produces a live score on a stale `last` today

1. S4 stores no new bar for ticker X, or X's newest bar is older than 200 s.
2. S5 `evaluate_member`: `intraday_stale = True`, `last_price` = the old close, and the function returns `input_stale` (W1, W2).
3. The stage refreshes X's open card anyway (W5). `refresh_card` computes proximity from the old close (W6).
4. The dots: the stale computed dots are `input_stale`, but any dot he has TAPPED is exempt (W15). A def with NO computed factor (every live note except Rubberband, W21 — UNVERIFIED) has nothing to suppress, so one tap is enough.
5. `card_score = conviction × proximity(old close) × 100` is written (W8) and orders WATCH (W16).
6. His next tap on any dot recomputes from the stored stale proximity (W10). A score suppressed by an untapped stale dot therefore comes back the moment he taps that dot. This is the r2 ESCALATE 3 mechanism.
7. If X has NO bar at all today: proximity = 1.0, the maximum (W6). Any conviction then scores at its ceiling. (Hub-verified correction to the author's report, not to this line: the card "tops WATCH" only when that integer is the cohort maximum — `round(conviction × 100)`; a conviction of 0.5 scores 50 and sits below a fresh 54. Grok WRONG FACTS #4, HOLDS.)
8. The replay reproduces all of it exactly (W17). L57 holds as reproducibility; the replayed number is still stale.

### 1c. Can it ARM, EXPIRE or REORDER on stale input? (this sets the size of the problem)

| Act | On stale input? | Why | |
|---|---|---|---|
| ARM | **No.** | `src/cobalt/radar/` has no `→ARMED` transition (grep). Arming is his button (`aset/web.py:640-655`), and the COBALT-actor hops at `store.py:496-505` run only inside his one-click fill. He may arm off a stale score, but that is his act | PROVEN (grep `ARMED`; hub Checked, HOLDS) |
| FORM | **No.** | W11 | PROVEN |
| EXPIRE: stop-before-arm | **No false expiry. Can be LATE.** | It reads real stored bars (`evaluate.py:1340-1344`, `cards/expire.py:287-299`). Stale means no new bar, so a touch is found late, never invented | PROVEN |
| EXPIRE: avoid | **No false expiry. Can be LATE.** | An intraday-stale evaluation returns before avoid is evaluated (`evaluate.py:598` vs `:626`) | PROVEN |
| EXPIRE: deadline | **Correct.** | Wall clock (`expire.py:305`) | PROVEN |
| REORDER | **Yes.** | WATCH order is `card_score` (W16). The stale score is live | PROVEN path |
| Health pills (FILLED) | **Computed on stale bars.** | `evaluate.py:780-797`. Not a score; out of scope (§5, Q5) | PROVEN |
| Shadow dot grade | **`htf_level_proximity` graded on a stale price** | W4; `engine_grade_at_tap` is recorded at tap (`store.py:1209`) and feeds `shadow_agreement_v` (`0007:255`), which is L7 data | PROVEN path · rows UNPROVEN (X25) |

All three houses that ruled confirm the sentence "Cobalt cannot arm, create or wrongly expire a card on stale bars; an expiry on stop or avoid can only come late" is TRUE; no breaking sequence was found (Grok (a), Gemini (a), Fable (a)).

**Size:** the score and the WATCH order are wrong while bars are stale. Arm, form and expire are not (expiry can only be late). Production occurrence is UNPROVEN (L70); X9 counts it. **Timing:** after C1 deploys, every new formation carries the untappable `assumed_formation` dot, so its score is null for life (`reports/setups-c1-draft-2026-09-21.md` E5; `cto-2026-09-21.md` R40). That makes the defect DORMANT for new cards from C1 until his first `A-01` ruling. Until then it is LIVE today, and for cards opened before C1. (Branch fact, hub-verified: C1 is commit `58aa823` on `setups/seven-0921`, worktree `~/cobalt-wt/setups-c1`; no ref `setups/c1-rubberband-0921` exists — see §6.)

## 2. Options

Common to all: formation, arm and expiry are untouched. The R36 STALE stamp renders beside the result and is not replaced. No number changes.

### (A) A card-level suppression recorded when bars are stale, lifted when they are fresh
- **A1: a stored string.** The refresh writes `card_score NULL` plus a reason. **Fails:** `tap_dot` recomputes `suppression(dots)` and the score from the stored (stale) proximity, and overwrites both (W10). This is the "stored string dies on the first tap" of Fable R2-2.1. REJECTED.
- **A2: C1's carrier, a synthetic untappable `bars_fresh` dot.** It is recomputed on every refresh from W1, is `input_stale` while stale, and is refused in `tap_dot`.
  - **Does C1's path fit?** Half of it. The *untappable* half fits: the tap path reads stored dots, so `suppression()` holds (C1's path 1).
  - The *carry-from-own-row* half does NOT fit. C1's dot is static and never lifts (`setups-c1-draft` five-path table, path 2: "re-appends from the card's OWN stored dot"). A freshness dot must be RE-DERIVED every scan, so paths 2, 3 and 5 need new code in a different shape.
  - It also puts a dot that is not a quality factor on EVERY card. That is visible, it shifts positions, it lands in `published_numbers` dot lists and it enters the tap-refusal surface. Meanwhile proximity is still computed from the stale price and shown as a number.
  - Files: `scoring.py`, `evaluate.py` (3 sites + replay), `store.py` `tap_dot`, `audit_export.py`.
  - **He sees:** an extra `bars n/a STALE` dot, score `—`, and a proximity number that is stale.
  - **Stored:** a dot row per card. **Replay:** recomputes the dot from the receipt.
  - **Cost:** M. Two recompute carriers exist for one fact (L3 concern). Not built (Grok (b), Gemini (b), Fable (b): C is the smaller mechanism).

### (B) Freeze the card whole while stale
- **Mechanism:** skip `refresh_card` / `refresh_radar_card` when `intraday_stale`. Expiry still runs. Files: `evaluate.py` (one guard) and replay (no card entry for that scan).
- **He sees:** the last FRESH score, proximity and `last`, shown as current. The only sign of age is the R36 stamp, which runs on the poller's clock (RTH only).
- **Stored:** nothing new. The row keeps its older values.
- **Fails L1:** an old number shown live is plausible-wrong. A tap during the freeze recomputes from the frozen proximity (W10) and publishes a score for a price that is minutes old. The WATCH order keeps ranking by it.
- **Cost:** XS. **Rejected as a design;** usable only as a stop-gap.

### (C) Proximity is UNKNOWN while stale. The score follows it, and every other value stays computed and marked — THE DESIGN (3 of 3 seats that ruled)
- **Mechanism.** One rule: **no fresh last → no proximity**.
  1. `[F-10]` Fable (e), verbatim: "`MemberEvaluation.intraday_stale: bool` — a required field, no default. It is computed immediately after `last_price` (`evaluate.py:502`: `True` when `last_bar is None`, else `intraday_staleness(observed_at=last_bar.ts + 1 min, as_of=member.as_of, scan_interval).stale`) and placed in `base`, so every return path carries it: the `not_evaluable` return at `:518-524` (today reached before `:529` computes the flag), the intraday return `:599` (True), the daily returns `:624`/`:629` (False — a fresh `last`), and `formed`. It is never keyed on `evaluation` (W3)." (UNCHECKED by a hub — read by the derive at `evaluate.py:502`, `:517-524`, `:529-534` on main `3ceb469`: borne out. Grok Q10 and Gemini (e) rule the same field, required with no default; the guard reads the field, never the label.)
  2. `score_card(..., last: Decimal | None)`: `last is None → proximity None`. `card_score(conv, None, …) → None` already holds (`scoring.py:265`). This is the ONLY pre-existing null branch: `score_card`'s `last`, `proximity()` and `CardScore.proximity` are non-Optional `Decimal` today (`scoring.py:254`, `:264`, `:312`, `:319-330`; hub Checked, HOLDS) — steps 2 and 6 are new code.
  3. `[F-13]` Grok (b), verbatim, replacing the proposal's step 3 and its "one existing branch" claim: "One helper, `score_last(ev) -> Decimal | None`, lives next to `score_card`. It returns None if and only if `ev.intraday_stale`. If `not ev.intraday_stale` and `ev.last_price is None`, it raises `EvaluateError`. Every `score_card` caller uses it and then passes that last through: `refresh_card` (`evaluate.py:776`), `replay_receipt` (`:1079`), the create call (`:1384`), and `audit_export.py:363`. The `card.entry` fallback and the `trigger` fallback are deleted. `score_card(last=None)` sets proximity None, sets `card_score` None via the existing `card_score` guard (`scoring.py:265`), and sets `score_suppressed` to the bars-stale sentence plus any `suppression(dots)` text. `tap_dot` keeps the stored sentence, per Q6. No new dot. No second carrier." (Derive read on main `3ceb469`: the create call at `evaluate.py:1384` passes `last=ev.last_price` for a formed evaluation, which has a closed bar; the helper returns that same value there — no number at formation changes.)
     `[F-14]` Grok (c), verbatim (the author's ESCALATE 1 is placed INSIDE this design by all three seats that ruled): "Delete the entry fallback at `evaluate.py:776` and `:1079`, and the trigger fallback at `audit_export.py:363`. Do not replace them with another price. `last_price` on the row stays `COALESCE` (Q4): a scan whose `ev.last_price` is None leaves the previous `last_price` in the column, including NULL if none was ever stored. It does not write `card.entry` into `last_price`." (Hub Checked, HOLDS: the 1.0 path; "tops WATCH" overstated. Fable (c)'s WATCH-impact claim is FC9 UNVERIFIABLE → X23.)
  4. `[F-16]` Grok (f), verbatim, replacing the proposal's step 4 sentence: "`published_numbers` writes JSON null for a null proximity, conviction, and `card_score`, never the string `"None"`. Publish and `replay_receipt` both go through `published_numbers` (`evaluate.py:1082` already does). The bars-stale sentence is a pure function of `ev`: no closed bar → `"bars stale — no closed bar"`; else `"bars stale — last close HH:MM:SS ET, older than 2 × radar.scan_interval"`, close time = `last_bar.ts + 1 minute` in `America/New_York`. Dot reasons, if any, are appended from `suppression(dots)`. No new column." Conviction, proposed key and dots are computed as today; he still sees what his taps say.
  5. `htf_level_proximity` gets `stale=intraday_stale` (W4). It is a function of `last`. (Q7/(g): forward, this stops new stale-graded engine values; a stale dot carries no `engine_grade`, so a later tap records `engine_grade_at_tap` NULL and adds no pair to `shadow_agreement_v` — X21 proves it. Rows recorded BEFORE this change are his, before any L7 promotion, never before this build — §8 Q7.)
  6. `CardUpdate.proximity` and `CardScore.proximity` become Optional. `published_numbers` writes `null` (step 4).
  7. `[F-06]` Grok Q6, verbatim, replacing the proposal's step 7: "Taps during staleness are accepted. `tap_dot` does not refuse a normal factor, and it does not recompute `card_score` from stored proximity when that proximity is NULL: `card_score` stays NULL. In that case `tap_dot` does not replace `score_suppressed` with `suppression(dots)`. It writes the stored `score_suppressed` back if that value is non-null, else the constant `PROXIMITY_UNKNOWN` (`"bars stale — no proximity"`) defined once in `scoring.py`. The bars-stale sentence with the close time is owned only by the refresh/replay helper. A tap cannot publish a number and cannot erase the sentence the helper stored. Conviction and the proposed key still update from the tap, as today." (Hub Checked: `tap_dot` writes `suppressed = suppression(dots)` at `store.py:1218`/`:1222` with no proximity-aware branch — HOLDS; FC3 HOLDS. Gemini's closing condition "tap_dot reason drop is fixed" is met by this step.)
  8. `store.refresh_radar_card` taps-moved branch: when `proximity IS NULL`, also null `card_score` and set the reason (closes W9 for this case). `[F-18]` Kept scoped to the null-proximity case: Grok (i) "Keep step 8 scoped to `update.proximity is None`. Do not widen C to the fresh race."; Gemini (i) "belongs outside this design as its own item"; Fable (i) offered a widening that closes the fresh case in the same lines and wrote "If the derive keeps step 8 alone, the fresh case stays a separate item and step 8 does not make it harder." The widening is OWNER ITEM 9 in the derive report, not built here.
- **Lifts by itself:** the first refresh with a fresh bar recomputes proximity, and the score returns with no tap (W8).
- **Files:** `radar/evaluate.py`, `cards/scoring.py`, `cards/store.py` (2 writers), `radar/audit_export.py` (`[F-13]` a code change, not signature only: the `:363` caller moves onto `score_last` and the `trigger` fallback is deleted; `[F-08]` the version gate below), `replay/formations.py` (the `SUPPORTED_EVALUATORS` set moves with the singleton, `[F-08]`), tests, DevDocs.
- **He sees:**
  - Score chip `—`.
  - `score suppressed: bars stale — last close 10:42:00 ET, older than 2 × radar.scan_interval` (W19; the sentence of step 4 `[F-16]`), or `bars stale — no closed bar` when no bar has closed.
  - Proximity `—`. His conviction and proposed key as before.
  - `last` = the real last print, with the R36 STALE stamp beside it when the poller agrees.
  - The WATCH card sinks below scored cards (nulls last) at the next reload or card action. The ladder is not re-sorted on the periodic refresh (`STALE-MARKER-PROPOSAL` F15). `[F-17]` 3 of 3: two messages on two clocks, and the sink is engineering (L1 + the ladder's existing null rule), not his; whether the ladder should re-render every scan is OWNER ITEM 7. The rendering lag is X29.
- **Stored (L57):** `proximity NULL`, `card_score NULL`, `score_suppressed` text, and `radar_score_id` → the seam row `evaluation=input_stale`. The receipt already holds the bars, `as_of` and `scan_interval` from which staleness is recomputed (W17, W20). No new column.
- **Replay:** `evaluate_member` recomputes `intraday_stale` from receipt values, and `replay_receipt` takes the same helper, so recompute = published. `[F-08]` Grok Q8, verbatim, replacing "Pre-change receipts … replay refuses other versions (C1 gate 5)": "When C branches, replace the singleton then on main. Set `EVALUATOR_VERSION`, `DESK_FORMULA_VERSION`, and `SUPPORTED_EVALUATORS` to the same new string. Do not leave the previous string in the set. Ride C1's string only if C and C1 ship in one deploy and no receipt is written at an intermediate version. Otherwise C bumps again on top of C1's string. `audit-export` reads the `evaluator_version` already written on the run/receipt (`evaluate.py:928`, `:1253`) and, if it is missing or not equal to `EVALUATOR_VERSION`, refuses with a version message before `replay_receipt`. No new column: the key is already in that payload; if a run proves it is not on the object audit loads, add it to that same JSON write." (Hub Checked + FC6, HOLDS: `audit_export.py` has NO receipt-version check today; the refusals at `replay/runner.py:219-224` / `replay/formations.py:145-149` gate the nightly module binding, not a receipt. Gemini Q8: "If C1 and this design deploy separately, sharing a version bump will break the replay gate". Fable Q8/(f): the same gate, 3 lines.)
- **C1's path:** `[F-13]` the proposal's paragraph "It uses the existing null-proximity branch, which all five of C1's paths already pass through" is WITHDRAWN as FALSE (hub Checked, HOLDS: only `card_score()` tolerates None today; refresh and replay substitute `card.entry`, audit substitutes `trigger`). What stands: C makes no new carrier and does not compete with the untappable `assumed_formation` dot; the one path for "an input of the score is unknown" is proximity NULL through `score_last` (step 3). **L3: one path.**
- **Cost:** S logic (~40-60 lines) + M tests; Grok (b): the helper and the two reason strings sit inside those lines, the tap change ~5 lines in `store.py`, the audit version gate ~10 lines in `audit_export.py`.

### (D) Variant of C: null `last` too
Write `last_price NULL` while stale. **Loses the real last print** that the R36 stamp marks, and `COALESCE` would need changing. Not taken (Q4, 3 of 3).

## 3. Recommendation: (C) — see `## L52 (a)–(d) re-answered for v2` at the end of this file.

## 4. Which clock

**The evaluator's clock:** last closed i1 bar older than `2 × radar.scan_interval`, measured from the bar CLOSE (`last_bar.ts + 1 minute`, `evaluate.py:532-534`), every session (W1). Why:
1. It is the clock that already decides whether this card may form on these bars (W2) and already marks its dots stale. One definition of "stale input" per card (L3).
2. It can be replayed from the receipt; the poller's `poll_failures` cannot (W20, L57).
3. The banner clock is per scan, not per ticker.

`[F-03]` Grok Q3, verbatim, replacing the proposal's band sentence (§8 Q3: "The score nulls at 200 s and the stamp shows at 180 s" — WRONG FACT, hub Checked HOLDS: the two clocks anchor to different bar edges, the band is ~80 s of open-age, not ~20 s): "The score and the R36 stamp stay two messages on two clocks. They may disagree. The score line does not say the stamp is present, and the stamp is not a score input. The score nulls only on the evaluator clock (`intraday_staleness`, `2 × radar.scan_interval`, age of the bar close, every session). The stamp stays the poller's `poll_failures` rendering (`radar.poll_bar_max_age_s`, RTH only). No factor, offset, or session gate is added to close the band. While the stamp is on and the score is still live, the score is right. While the score line is on and the stamp is off, the line is right."

The stamp keeps the poller's clock. It is a RENDERING and is not changed.

**L53:** No number is proposed, changed or added. The score obeys the existing `2 × radar.scan_interval` rule (Astra R1-12). `radar.scan_interval` and `radar.poll_bar_max_age_s` stay his. Whether the score should follow a different clock (RTH-only, or the poller's), and whether the two clocks should meet, is his — OWNER ITEMS 2 and 3; neither is a precondition to build.

## 5. Deliberately NOT changed

- The R36 stamp, `poll_failures` and `stamp_poll`. The design does not depend on the stamp, so the carried S4-over-S3 overwrite (`radar/store.py:269-273`) does not touch it. The stamp is on `main` (`490c231`, hub FC8 HOLDS); C does not read `poll_failures`.
- Formation, arm, the expiry order and causes, and the key tap.
- `ladder_order` / `TIE_POLICY` text, conviction, the proposed key, the curves and every threshold. (Q9, 3 of 3: the `pool_position` tie-break among null scores is live today and not a precondition.)
- C1's `assumed_formation` dot.
- Health pills on FILLED cards (Q5, 3 of 3: own item).
- Daily-stale `input_stale`, which does not touch `last` (Q10, 3 of 3: proximity stays computed from the fresh `last`; the guard reads `intraday_stale`, never the label).
- The W9 race when the bars are fresh (a separate item; `[F-18]` Grok (i) prices the general fix at about 15 lines in `refresh_radar_card`, S2 only, plus a cobalt_dev race test; Fable (i) at ~5 lines in the same branch through `card_score()` — OWNER ITEM 9).
- The panel, which already renders `—` and the reason (W19 at `:998`/`:1023`).
- His hand grades. Taps during staleness are ACCEPTED and kept (step 7).
- Past `htf_level_proximity` tap rows already in `shadow_agreement_v` (Q7/(g), 3 of 3: his, before any promotion — OWNER ITEM 4).

## 6. Chunks, seats, migration, restarts, evenings

`[F-19]` Grok (j), verbatim: "S1 then S2 on one branch. S1 is the pure helper, `intraday_stale`, `score_card(last=None)`, the reason strings, `htf_level_proximity` `stale=intraday_stale`, Optional proximity, `published_numbers` nulls, the version singleton, and the offline tests. S2 is `tap_dot` (Q6) and the taps-moved null (step 8), plus cobalt_dev tests. Seat for the branch is the house's L29 floor (Opus 5 if Claude builds it): S2 writes `"user".aset_sizings` and `"user".card_dot_taps`. No migration (W13; staged `0007:47-49` are nullable; no new column). C branches off main after C1 has landed, not stacked on the unmerged C1 branch, and the version rule is Q8. C does not wait for C2. C is merged before his first A-01 ruling. The R36 stamp build is not a predecessor: `main..s2/stale-marker-0921` is empty in `greps.txt`, and C does not read `poll_failures`."

| Chunk | Scope (per `[F-19]`, plus the folds that name a file) | Seat (L29) |
|---|---|---|
| S1 | Pure: `intraday_stale` required field `[F-10]`; `score_last` helper and the three deleted fallbacks `[F-13]` `[F-14]` (`evaluate.py:776`, `:1079`, `audit_export.py:363`); `score_card(last=None)`; the reason strings and `published_numbers` nulls `[F-16]`; `htf_level_proximity` `stale=intraday_stale`; Optional proximity; the version singleton and the `audit-export` version gate `[F-08]`; `replay/formations.py` set; offline tests (§7, "before S1") | house's L29 floor (Opus 5 if Claude builds it), same branch as S2 |
| S2 | Writers: `store.tap_dot` keeps the stored sentence `[F-06]`; `refresh_radar_card` taps-moved null (step 8); with-DB tests on `cobalt_dev` (§7, "before S2") | **Opus 5 floor** (user-table write path) |

- **Migration: no.** The columns are already nullable (W13; `0006:103-106`).
- **RESTARTS (GUESS until `cobalt jobs restarts <range>` — X17 replaces this list, L42):**
  - `com.cobalt.radar` (imports `radar.evaluate`). The restart must fall inside 20:00–21:00 (L43), with the residents down before the merge (L66).
  - `com.cobalt.aset` (`aset/web.py:47` imports `cobalt.cards` — UNVERIFIABLE FROM READS in the hub's table; X17).
  - The one-shot `com.cobalt.replay` reads the new version on its next run.
- **Sequencing — what the rulings decide (the deploy order itself is the desk's lane, L68):** C1 is commit `58aa823` on branch `setups/seven-0921` (worktree `~/cobalt-wt/setups-c1`); the name `setups/c1-rubberband-0921` used by the proposal's packet does not exist (hub Checked + FC7, HOLDS). C touches the same functions as C1 (`refresh_card`, `tap_dot`, `replay_receipt`, the dot sites). All three seats that ruled: C is built on a tree that carries C1 and is live before his first `A-01` ruling. Grok and Gemini: off `main` AFTER C1 lands, not stacked (Gemini: "not stacked unless explicitly coordinated"). Fable: on a tree that already carries `setups/seven-0921` — after it lands, or stacked under the L68 gate on the combined tree. The version rule is `[F-08]`: ride C1's string only in one deploy with no intermediate receipt, else a separate bump.
- **Must not wait for C2.** The defect is live today and returns at the first `A-01` ruling. C must be live no later than that ruling (3 of 3; Fable: "before `A-01`" orders the lane, it does not gate the build).
- **Evenings to live (GUESS, unchanged from the proposal except that the tribunal closed today):** tribunal round 1 done 2026-09-22, no round 2; then build (after C1 lands), ≥3 code checkers (L67 as amended 2026-09-21: Sol, Opus 5, Grok/Gemini) and one deploy. Earliest THU 09-24 if C1 lands WED 09-23.

## 7. First-gate experiments (L70; each runnable on `cobalt_dev`, RED on main first where marked)

`[F-20]` X1–X9 as Grok (k) leaves them (Gemini and Fable keep X1–X9; Fable's X4 replacement says the same as Grok's); X10–X22 are Grok's, verbatim; X23–X29 are Fable's X10–X16, verbatim, renumbered (the hub's `## Experiments named` table conflates Grok's X10/X11 with Fable's — they are different experiments). Each is placed before the chunk it gates.

**Before S1 (pure, offline):**
- **X1 (RED on main):** KEEP, but drive age off the passed `scan_interval`: close-age = ttl + 1, not a hardcoded 201. RED on main: all dots tapped, `card_score` non-null. After: proximity NULL, `card_score` NULL, reason names that close time.
- **X5 (RED on main), CHANGE into two.** X5a: `last_bar` None → proximity value 1 on main, NULL after. X5b: member whose bars are all from the prior session → record whether `last_bar` is None. If it is not, main's proximity is the old close (not 1) and C still nulls. This settles the word "today".
- **X6:** KEEP. `htf_level_proximity` is `input_stale` whenever `intraday_stale`, including when `last_price` is not None and `daily_ok` is true.
- **X7:** KEEP. Add one assertion: a promoted stale WATCH card is still promoted. Pinned order unchanged.
- **X8:** KEEP. Deadline still expires on the wall clock. A stored bar through the stop still expires `stop_before_arm`. A stale scan does not expire `avoid`.
- **X10:** on a fixture receipt, `rebuild_members(...).as_of` equals the receipt's `as_of`, not `datetime.now`. If it is wall-clock, replay is not L57-sound and the design changes before any bump ships. (Hub: UNVERIFIABLE FROM READS — the settling experiment for (d).)
- **X11:** `audit_export.py:363` path, member with `last_price` None, does not emit proximity 1 after the change.
- **X12:** `published_numbers` of a null score is JSON null on both sides, not the string `"None"`.
- **X14:** `evaluation == "input_stale"` from daily-missing (`:624`) with a close younger than the ttl leaves proximity non-null.
- **X15:** pure clock fixture, not a product change. Open-age 210 s, RTH → stamp predicate true, `intraday_stale` false. Same bar, session not RTH, close-age 540 s → `intraday_stale` true, stamp predicate false.
- **X18:** repo grep of the old version string and of every `score_card(` call. Any caller not on `score_last` fails the build.
- **X19:** who reads `DESK_FORMULA_VERSION`. If anything compares it to `EVALUATOR_VERSION`, it moves with the singleton.
- **X20:** `formations.py:145` — is `evaluator_version` the binding's stored string or the module constant? If it is the binding's, old nightly bindings are refused until regenerated. That refusal is accepted. Do not union the old string back into the set to silence it.
- **X22:** `radar_panel.py` around `:758` (`last=r.last_price`). If that function recomputes `proximity` from `last`, it is a missed scorer and must render the stored proximity instead. If it only displays `last`, no design change.
- **X26 (Fable X13):** pure: an open card refreshed through the slug-match path (`evaluate.py:1324-1328`) with an evaluation of `not_evaluable` — can `evaluability` differ while `formation_changes` is empty? Either result leaves (e)'s wording; a "yes" makes it load-bearing.
- **X27 (Fable X14):** pure: the stage's `score_suppressed` text and `replay_receipt`'s are byte-identical for a stale card (ET time format, dot-reason order) — X4's precondition.

**Before S2 (writers, `cobalt_dev`):**
- **X2:** KEEP. Step 3 expects the score NULL and the helper's sentence unchanged (Q6), not a new constant. (The proposal's sequence: form a card and tap all its dots; stop feeding bars and run the stage — NULL score, NULL proximity; tap another dot — score stays NULL, reason kept; add a fresh bar and run the stage — the score returns with no tap.)
- **X3:** KEEP. Taps-moved while the update proximity is NULL → the row's `card_score` is NULL.
- **X13:** tap while proximity is NULL leaves `score_suppressed` byte-identical and leaves `card_score` NULL.
- **X16:** no bar this scan, previous `last_price` 5.25 → column still 5.25 (`COALESCE`) and proximity NULL.
- **X21:** one tap on `htf_level_proximity` while `intraday_stale` inserts `engine_grade_at_tap` NULL and adds no row to `shadow_agreement_v`. A tap from before the change is still in the view.
- **X23 (Fable X10):** on `cobalt_dev`, a def whose `preferred_windows_ref` ends after the last scan of the day, a card formed on it, a scan on the next trade date before any bar → does the card survive to that scan and does it publish proximity `1.000000` on main (WATCH impact of ESCALATE 1)? A "never survives" result makes ESCALATE 1 a terminal-card artifact. (Hub FC9: UNVERIFIABLE FROM READS.)
- **X24 (Fable X11):** on `cobalt_dev` with an archived low-volume ticker's i1 bars: are minutes with no prints stored as bars? If not, Q2's premarket nulls are frequent by design and RTH-only becomes a real owner question.

**Before the audit / deploy gate:**
- **X4, CHANGE.** Same-version stale card: recompute = published, including JSON null. A pre-change receipt: the version message, and the test fails if the error is the mismatch path.
- **X17:** `cobalt jobs restarts <range>` on the diff. That table replaces the restart guess. A resident the command names that this ruling does not name is added, not ignored.

**Measurement only (not a design gate):**
- **X9:** KEEP as a measurement only, not a design gate. Run on cobalt_dev, then the hub read-only on production (L41). Zero rows does not remove the code path. A positive count confirms occurrence. It does not change C. (Count the radar cards whose `radar_score_id` seam row is `input_stale` while `card_score IS NOT NULL`.)
- **X25 (Fable X12):** `cobalt_dev`, then the hub read-only on production: count `card_dot_taps` rows for `htf_level_proximity` with `engine_grade_at_tap IS NOT NULL` whose `at` falls inside a run whose `radar_score` row for that card's member/def is `input_stale`. Zero → Q7's backlog is empty.
- **X28 (Fable X15):** `cobalt_dev`: count receipts whose `published.proximity = '1.000000'` on a card whose seam row is `input_stale` — how often the fallback published in the past.
- **X29 (Fable X16):** rendering: after a scan nulls a score, `/radar` fetched before and after a tap on another card — the strip's chip and slot change only after the tap; the badge appears within one `refreshPool`.

Dropped: none of X1–X9.

## 8. Questions for the tribunal — as ruled (3 of 4 seats each: Grok, Gemini, Fable; Astra `ASTRA PENDING (R13)`)

1. **Sink or hold?** `[F-01]` Ruled: SINK. 3-0 ADOPT. The ladder already sinks a null (`cards/radar.py:179-183`); holding the slot would be a second ranking input (L52 b) or a rank on a dead price (L1). Holding is OWNER ITEM 1, his, after the tribunal.
2. **Premarket under the every-session clock?** `[F-02]` Ruled: ACCEPT the evaluator's clock; no RTH-only rule is added. 3-0 ADOPT. An RTH-only score rule is OWNER ITEM 2 (L53). Whether thin names print gap-minutes is X24.
3. **The band?** `[F-03]` Ruled: reason text is enough; the two clocks are not made to meet; §4 carries Grok's wording. Grok ADOPT WITH, Gemini ADOPT, Fable ADOPT WITH (same fact: 80 s, not 20). Whether the clocks should meet is OWNER ITEM 3.
4. **Keep the stale `last` (C) or null it (D)?** `[F-04]` Ruled: C. 3-0 ADOPT. `COALESCE` keeps the prior print regardless; D would blank what the STALE stamp marks.
5. **FILLED health pills?** `[F-05]` Ruled: own item. 3-0 ADOPT. OWNER ITEM 6.
6. **A tap during staleness?** `[F-06]` Ruled: ACCEPT the tap, score stays NULL, the stored sentence is kept — step 7 is Grok's wording. Grok ADOPT WITH, Gemini ADOPT, Fable ADOPT.
7. **Stale-graded `htf_level_proximity` taps in the agreement stats?** `[F-07]` Ruled: forward, step 5 stops new ones (engineering); backward, the rows already stored are HIS, before any L7 promotion, never before this build. Grok ADOPT (leave them), Gemini ADOPT WITH (exclude, as an owner item), Fable ADOPT WITH (his call; X25 counts them). Not a build gate. OWNER ITEM 4.
8. **The version bump?** `[F-08]` Ruled: Grok's wording (§2 C "Replay"): ride C1's string only in one deploy with no intermediate receipt, else a separate bump; the audit-export version gate. Grok ADOPT WITH, Gemini ADOPT WITH (separate bump), Fable ADOPT WITH (same rule).
9. **Must the `pool_position` tie-break be ruled first?** `[F-09]` Ruled: NO. 3-0 ADOPT. The tie policy is live today; nulls join the existing bucket. OWNER ITEM 5, not a precondition.
10. **Daily-stale `input_stale`: leave proximity computed?** `[F-10]` Ruled: YES. Grok ADOPT WITH (required field, no default; the guard never reads the label), Gemini ADOPT, Fable ADOPT; step 1 carries the field definition.

## WRONG FACTS — hub-verified corrections applied in this v2

| Correction (hub `## Checked against the files`, all HOLDS) | Applied at |
|---|---|
| Only `card_score()` tolerates None today; `score_card`/`proximity()`/`CardScore.proximity` are non-Optional (`scoring.py:254`, `:264`, `:312`, `:319-330`) — the proposal's "all five paths already pass through" premise is FALSE | §2 C step 2, step 3 `[F-13]`, "C1's path" |
| `tap_dot` drops `score_suppressed` to `suppression(dots)` alone (`store.py:1217-1222`) | §2 C step 7 `[F-06]` |
| The band is ~80 s of open-age (stamp anchored at bar open, score at bar close), not ~20 s; the clock is "bar close", not "bar time" | §4 `[F-03]`, §8 Q3 |
| `radar_panel.py` reason line at `:998`, chip at `:1023`, RANK+WHY at `:1039` — not `:957` | W19 `[F-11]` |
| `audit_export.py:363` carries a third `last` fallback (`else trigger`); `audit_export.py` is a code change, not "signature only" | W22 `[F-11]`, §2 C step 3 `[F-13]`, Files |
| `audit_export.py` has NO receipt-version check today; the version refusals gate the nightly module binding | §2 C "Replay" `[F-08]`, X4 |
| `radar/store.py:423-425` is the SQL writer of the seam columns (W12 cited only the caller) | W12 `[F-12]` |
| No-bar proximity 1.0 does not necessarily "top WATCH" | §1b step 7 note |
| `setups/c1-rubberband-0921` does not exist; C1 = `58aa823` on `setups/seven-0921` | §1c, §6 `[F-19]` |
| W21 (only Rubberband names a computed factor) is grep-scope only, UNVERIFIED | W21 `[F-11]` |

## Dissents, verbatim

None. No house returned `REJECT` or `DO NOT BUILD` on any item (hub `## ESCALATE`: "No house said `DO NOT BUILD`. No `REJECT` was returned by either house"; Fable: `reject: 0`). The one house wording v2 does not follow that changes a mechanism is Fable (i) — an `ADOPT WITH`, not a dissent; its text and cost are carried as OWNER ITEM 9 in the derive report, with the seat's own sentence that step 8 alone is acceptable.

## L52 (a)–(d) re-answered for v2

| L52 | Answer for v2 |
|---|---|
| (a) | Every number is traceable. Proximity is computed only from a `last` that `score_last` returns — a closed bar fresh by the receipt-replayable rule `2 × radar.scan_interval` from the bar close (`[F-13]`, `[F-10]`). A stale or absent `last` degrades proximity and `card_score` to NULL with a reason sentence that is a pure function of the evaluation (`[F-16]`), never to a modelled value; the three price fallbacks that produced a modelled proximity (`card.entry` twice, `trigger` once) are deleted (`[F-14]`). No number, factor, offset or session gate is added (`[F-03]`, L53) |
| (b) | ONE authority, unchanged: `card_score` orders WATCH (ADR-0009 D4). The stale card holds NULL and falls to the existing tie policy; no hold, no stored slot, no second order (`[F-01]`, `[F-09]`). A tap cannot publish a number while proximity is NULL (`[F-06]`) |
| (c) | The seam is real artifacts: `MemberEvaluation.intraday_stale` (required, no default, set at `evaluate.py:502`, carried on every return path) · `score_last(ev)` beside `score_card` · `score_card(last=None)` · `CardScore.proximity` / `CardUpdate.proximity` Optional · `aset_sizings.proximity NULL` (nullable, W13) · `tap_dot`'s keep-the-stored-sentence branch · `refresh_radar_card`'s taps-moved NULL branch (step 8) · `published_numbers` JSON null · the version singleton (`EVALUATOR_VERSION`, `DESK_FORMULA_VERSION`, `SUPPORTED_EVALUATORS`) and the `audit-export` version gate (`[F-08]`) · receipt `as_of` + bars + `scan_interval` (W17) |
| (d) | Auditable by another house: `cobalt radar audit-export` replays the receipt through the same helper and refuses any mismatch (W17), and refuses a receipt of another evaluator version by name before the replay (`[F-08]`); the staleness is a pure function of receipt values (X10 proves `as_of` is the receipt's, X27 proves the sentence is byte-identical on both sides). The build is checked by at least three houses other than its author (L67 as amended 2026-09-21: Sol, Opus 5, Grok/Gemini); Astra reads this v2 when its meter returns (R13) |
