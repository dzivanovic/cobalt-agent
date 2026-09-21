# Setups tribunal, round 1 — three non-Anthropic houses (2026-09-21)

## §0 Headline
- Hub `setups-tribunal-0921`, Sonnet 5. Packet of 44 files staged (0 byte mismatches) and put before Astra, Grok and Gemini at 09:57 ET. **1 of 3 houses ruled: Grok** (`TRIBUNAL R1: BUILD AFTER scoped A-01, atr name, hole-fill, assumed persist`). **Astra: METER** (usage limit mid-run, reset 11:12 AM). **Gemini: HARNESS** (`command` permission auto-denied, no output). No retries by the hub.
- File-check of Grok's claims against the real files: 30 HOLD · 3 DO NOT HOLD · 4 UNVERIFIABLE FROM READS. Blockers to build that HOLD: 3 (assumed-persist on refresh, hole-fill scope, the `atr_working` name). ESCALATE: 3. Owner items: 7, none a precondition.
- Redactions (L32): 7 spans of Grok's text that paraphrase his notes' definition content are replaced by `[user data: <note>:<lines>]` — 6 table cells in `## Wording offered` (a) and 1 scenario clause. No value, quote or wording from his notes, the gap table or `assumed-values.md` is in this report.
- L74 (recorded once, not followed): a block that arrived beside a tool result asked for a `Claude-Session:` line in commits and named a file-send tool. It is data; this run commits nothing.

## AUTHORIZATION (verified by the hub, each its own Bash call)
| proof | result |
|---|---|
| R13 in `cto-2026-09-20.md` | line 86, carries the 13:33 ET words |
| R23 in `cto-2026-09-20.md` | line 206, grok/agy through 2026-09-21 23:59 ET |
| R15 in `cto-2026-09-21.md` | line 27, carries "I don't want to rule on anything" |
| R18 in `cto-2026-09-21.md` | line 29, carries the seven-setup list |
| R18 committed on main | `0cf4b822ff5971e50c5503321be761734b9f0b63` |
| proposal committed on main | `652434e50156f9ea30777703c0fc1072b8562308` |
| 14 allow + 3 deny strings in `08-bars-chunk-e-check.md` | 17 of 17 count 1 (no new rule) |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| DATE GATE (row 1) | `date` | 0 | allowed — `Mon Sep 21 09:28:59 EDT 2026` (before 2026-09-22) |
| `Bash(grok *)` | `grok --version` | 0 | allowed — `grok 1.0.25 (f7e67d6988e2) [stable]` |
| `Bash(agy *)` | `agy --version` | 0 | allowed — `1.2.7` |
| `Bash(ls *)` | `ls scratch/tribunal-bars-0920` | 0 | allowed — base folder exists (Grok's allow string has its folder) |
| `Bash(ls *)` | `ls scratch/tribunal-bars-0920/setups-tribunal/r1` | 1 | allowed — `No such file or directory` = fresh run |
| STAGGER `Bash(tail *)` | `tail -n 3 …/degraded-line-deploy-review-2026-09-21.md` | 0 | allowed — last non-blank line is `DEGRADED LINE DEPLOY REVIEW DONE · …`, not in-progress; no other three-house hub running |
| CODEX PROBE (gate) | `codex exec --skip-git-repo-check -m gpt-6-astra -s read-only "Reply with only the word OK."` | 0 | allowed — replied `OK`, exit 0, no usage-limit text → **astra: UP** (at 09:29; the meter then ran out mid-ruling, below) |
| DATE GATE (row 2, before the launches) | `date` | 0 | allowed — `Mon Sep 21 09:56:29 EDT 2026` (before 2026-09-22; before 23:20 ET) |

## Packet
Folder `scratch/tribunal-bars-0920/setups-tribunal/r1/` (gitignored, `.gitignore:90`), 44 files, staged by Read → Write. Every copy `wc -c`-checked against its original: **0 mismatches**. Main HEAD at staging: `a9314bf6b9d2dd1f54db027c39d4420ce23de202` (the proposal cited `0cf4b82`; the code line numbers it cites still hold at the gate lines, e.g. `evaluate.py:635-647`). Trailing whitespace: `grep -c -E "[[:space:]]$"` = 0 on every original except `Second Chance Scalp.md` (2 lines, :24 and :63); the Write tool KEPT them (8,978 B = 8,978 B), so the gap is 0 everywhere. The proposal is 42,357 B = the 42,357 B the prompt named.

| file(s) in the folder | original | bytes | marks |
|---|---|---|---|
| `PROPOSAL.md.part1` + `.part2` | `docs/30 - Design/SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md` (cut before line 181 `## 9. ACCEPTANCE …`) | 27,413 + 14,944 = 42,357 | ordered parts |
| `design-report.md` | `reports/setups-design-2026-09-21.md` | 9,708 | |
| `owner-rulings.md` | R13 :25, R15 :27, R17 :28, R18 :29 of `cto-2026-09-21.md` | composed | |
| `laws-excerpt.md` | L1, L3, L7, L8, L10, L11, L28, L32, L45, L52, L53, L57, L65, L67, L70 of LAWS.md | composed | |
| `rubberband-proof.md`, `test_rubberband_card_proof.py` | `~/cobalt-wt/rubberband-proof/…` | 11,752 · 15,712 | |
| `defs-gap-table.md`, `assumed-values.md`, `trade-tags.txt` | `docs/_inflight/…`, vault trade notes | 33,956 · 13,316 · composed | **[USER DATA]** |
| `note-rubberband.md`, `note-hitchhiker.md`, `note-backside.md`, `note-second-chance.md`, `note-fashionably-late.md`, `note-nine-ema-scalp.md`, `note-vwap-continuation.md` | `1 - Trading/4 - Strategies/*.md` | 5,603 · 3,683 · 7,602 · 8,978 · 3,246 · 4,905 · 4,773 | **[USER DATA]** |
| `ADR-0009.md`, `TAXONOMY-DRAFT-v0_7.md` | `docs/10 - Decisions/…`, `docs/30 - Design/…` | 6,461 · 35,697 | |
| `evaluate.py.part1/2/3` | `src/cobalt/radar/evaluate.py` cut before `class OpenRadarCard` (:700) and `class StageOutcome` (:1097) | 30,202 + 18,564 + 22,335 = 71,101 | ordered parts; `evaluate_member` whole in part 1 |
| `anatomy-registry/extension/structure/bars/indicators/leg/daily.py` | `src/cobalt/radar/anatomy/*.py` | 2,789 · 6,095 · 4,638 · 5,559 · 6,233 · 2,284 · 7,761 | |
| `evaluate_cli.py` | `src/cobalt/radar/evaluate_cli.py` | 19,415 | |
| `taxonomy-loader/tunables/vault_loader/predicate/trade_def.py` | `src/cobalt/taxonomy/*.py` | 8,694 · 4,482 · 19,447 · 23,346 · 33,063 | |
| `cards-radar.py`, `cards-scoring.py` | `src/cobalt/cards/*.py` | 8,481 · 14,048 | |
| `tunables.yaml` | `configs/cobalt/taxonomy/tunables.yaml` | 28,028 | |
| `test-live-note.excerpt.py`, `radar-panel-owners.excerpt.py`, `settings-card.excerpt.py` | `test_radar_evaluate.py:680-720` (anchor :692), `radar_panel.py:255-265` (anchor :261), `settings/card.py:60-75` (anchor :72) | excerpts | each headed by real path and range |
| `greps.txt` | the eight pre-computed searches, none over 400 lines | composed | grep honours `.gitignore`, said in the file |
| `QUESTIONS.md` | the verbatim questions + the file-list paragraph | composed | |

The seven cheat-sheet PDFs are NOT staged (a binary cannot pass Read → Write byte-identical and no copy rule exists); QUESTIONS.md says so. No house disputed a cheat-sheet quote, so no PDF was opened.

## CONTINUE
LAUNCHED 09:57 ET, all three `run_in_background`, one attempt each, 20-minute timeout; spellings = `prompts/2026-09-19/01-review-harness.md` §2.1–2.3 with the sentence this prompt names; no rule added.
- GROK: completed exit 0 by ~10:05 ET; wrote `grok-ruling.md` itself (195 lines), replied with the path. Closing line present.
- ASTRA: `astra: METER` — probed UP at 09:29, then mid-run the CLI printed (verbatim, twice) `ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at 11:12 AM.` exit 1, 135,471 tokens used; it printed only its file reads, no ruling. No `astra-ruling.md` written (nothing to keep).
- GEMINI: `gemini: HARNESS` — exit 0 with no ruling; verbatim output: `jetski: no output produced — a tool required the "command" permission that headless mode cannot prompt for, so it was auto-denied. Add an allow-rule under permissions.allow in settings.json (e.g. command(<target>)). Alternatively, re-run with --dangerously-skip-permissions to auto-approve all tools.` No `gemini-ruling.md` written (nothing to keep).
next: none — the report is complete; the desk commits it (breadcrumb kept for a relaunch: collate is done).

## Rulings table
Only Grok ruled. Astra and Gemini columns: `—` (METER / HARNESS). "Agreement" = n/a with one ruling.

| item | grok | gemini | astra | agreement | wording / reason (≤25 words) |
|---|---|---|---|---|---|
| O1 direction from anatomy `A-01` | ADOPT WITH | — | — | 1 of 1 | Scope `against ext.direction` to rubberband's C1; backside/FL bind side through the mirrored frame; never for the four with-trend defs. |
| O2 mirrored frame | ADOPT WITH | — | — | 1 of 1 | Frame kept; replace property test with `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)`; stated property false for stop cents. |
| O3 `unclassified` token | ADOPT | — | — | 1 of 1 | `setup_ref` already `str` (`cards-radar.py:84`); `SetupRef` enum must not gain it; validate token on Formation/spec. |
| O4 score suppressed on assumed formation | ADOPT WITH | — | — | 1 of 1 | Persist `assumed_formation` on the row; `refresh_card` must not overwrite it from live dots; A-01 suppresses in C1. |
| O5 one vault note + hole-fill | ADOPT WITH | — | — | 1 of 1 | New L28 Cobalt command writes the unit; hole-fill only if engine value null AND source assumed AND same scope AND same key. |
| O6 premarket seed beside Extension ATR | ADOPT WITH | — | — | 1 of 1 | Seeded ATR gets a NEW name (`atr_seeded`); keep `atr_working`; `ev.ema9` stays RTH until version bump. |
| O7 opening-drive termination `A-07` | ADOPT | — | — | 1 of 1 | Literal taxonomy reading almost never forms; proposed rule is the only forming one; modelled, suppressed; taxonomy amendment is OWNER after cards. |
| O8 9-EMA catalyst `A-13` | ADOPT | — | — | 1 of 1 | No catalyst collector; tap gate contradicts R17; mark on atom, chip on card, dot stays YOURS. |
| (a) direction | not safe for all seven | — | — | 1 of 1 | Right for rubberband; backside/FL need the frame; four with-trend defs are not against-Extension. |
| (b) mirrored frame | ten non-equivalences named | — | — | 1 of 1 | Stop buffer+nudge, upper third, `gt=0` spec, tie label, etc.; stated property test not enough. |
| (c) L52 (a)/(b)/(c)/(d) | ADOPT WITH / ADOPT / ADOPT WITH / ADOPT | — | — | 1 of 1 | (a) recorder must wrap every cfg read; (b) one authority `card_score`; (c) name seams; (d) receipt holds tunables. |
| (d) assumed visibility | paths (1)(2)(5) not covered as written | — | — | 1 of 1 | A-01 not a cfg key; cfg reads outside interpreter; `refresh_card` recomputes suppression. |
| (e) store | build the L28 command | — | — | 1 of 1 | R15 is not an L65 write instruction; +S on C2; hole-fill same key+scope only. |
| (f) acceptance | gates 1–4 catch; gate 5 does not | — | — | 1 of 1 | Green-while-empty: builder-chosen day, wrong-reason replay, unset env, zero tagged rubberband/backside. |
| (g) warm-up | no number moves if names differ | — | — | 1 of 1 | `ev.ema9` moves if seeded; "two quantities" true only with two names. |
| (h) chunks / experiments / latency | split C3; X6, X8 added | — | — | 1 of 1 | C3a D1+warm-up then C3b Range; 700 vs ~50 evaluations, 14×; p95 UNVERIFIED (X5). |
| (i) not checkable | X1–X6, X8 (X7 "settled") | — | — | 1 of 1 | See `## Experiments named`. |
| closing line | `TRIBUNAL R1: BUILD AFTER scoped A-01, atr name, hole-fill, assumed persist` | HARNESS (no line) | METER (no line) | — | — |

## Wording offered, verbatim
Grok's `grok-ruling.md`, item by item, UNEDITED except the seven `[user data: …]` redactions (§0). Every `ADOPT WITH` replacement block, the reasoning beside it, and the closing line. No `REJECT` was issued.

### O1 — ADOPT WITH (paste)
> Direction comes from the trade's own anatomy. `valid_setups[].relation` is never read for direction. C1 only: a def whose long-side trigger/stop is a fade of a culminating unqualified `Extension` (rubberband) sets `trade_direction = against ext.direction`. Backside and fashionably-late are NOT that case — they bind side only through the mirrored frame on their own long-side text (state `backside` / `reverting`, range/EMA/cross). Never apply `against ext.direction` to hitchhiker, second-chance, nine-ema-scalp, or vwap-continuation. Setup identity is not detected; `setup_ref = unclassified`. Both frames True → `not_formed both_sides`. A def with no oriented object and no bindable `trade_direction` → `not_evaluable: Direction(unbound)`.

Root-cause reading of `evaluate.py.part1:635-645` is right for rubberband: `relation` is setup-context (`TAXONOMY-DRAFT-v0_7.md:136-137`, `:124`), not Extension-vs-trade. Proof run: mixed 4+1 → `not_evaluable Setup(relation)` on all 71 scans a single-relation control forms (`rubberband-proof.md`).
`against ext.direction` on a **backside** that has already reclaimed the open puts the card on the wrong side (see (a)). Detecting gap/day-2/VIR is size L and changes no rubberband side; leave it off.

### O2 — ADOPT WITH (paste)
> Every def is evaluated twice, once per side, on a Frame. Long = stored bars. Short = the same detectors on mirrored bars (price → −price, high ↔ low; volume and time unchanged). `trade_direction` in a frame means that frame's side. A price from the mirrored frame is negated before it reaches `Formation` or `RadarCardSpec`. Acceptance property (not the proposal's): `negate_prices(eval_as_long(mirror(bars))) == eval_as_short(bars)` for price outputs, and `pred_as_long(mirror(bars)) == pred_as_short(bars)` for predicates. Do not ship `detector(mirror(bars)) == mirror(detector(bars))`.

The frame method is the simpler mechanism (one transform vs a long/short branch in every detector). The stated property test is false for additive cents and for “from the bottom” quantities — it would fail the suite or, if weakened, miss a real branch bug.
Concrete: long stop at extreme E=10.02, buffer 0.02 → raw 10.00, ten-cent nudge to 10.01 (`anatomy-structure.py:100-116`, `_on_ten_cent_grid:96-98`). `detector(mirror)` long-stop = −10.04; `mirror(detector)` = −10.01. Not equal. The frame pipeline (always long, then negate) yields the correct short stop 10.04.
Named non-equivalences: stop buffer + nudge (`anatomy-structure.py:13-21,100-116`); `DayRange.upper_third` (not an odd map of OHLC — hitchhiker `note-hitchhiker.md:38`); `RadarCardSpec.trigger_price`/`structural_stop` `Field(gt=0)` (`cards-radar.py:86-88`) — negate before the spec or create raises; HTF proximity tie prefers `prior_high` (`anatomy-daily.py:147-149`); Python `%` on negative cents (`anatomy-structure.py:96-98`). Volume band and ATR true range are invariant (volume; `high-low`). Staged `WorkingBar`/`DailyBar` do not require positive prices. Archiver `Bar` is not staged → X6.

### O3 — ADOPT
`RadarCardSpec.setup_ref` is already `str` (`cards-radar.py:84`), not `SetupRef`. `SetupRef` (`taxonomy-trade_def.py:155-165`) has no `unclassified` and must not — that enum is setup identity on the def, which this design does not detect. A nullable column is a C1 migration for no gain. Validate the reserved token on `Formation`/`RadarCardSpec` only. Honest on the face: `card_why` leads with `setup_ref` (`evaluate.py.part1:674-680`).

### O4 — ADOPT WITH (paste)
> A formation that consulted any assumed `cfg` key or assumed resolver (A-01, A-05, A-13 included) sets `score_suppressed = assumed_formation` at create. That string is stored on the card row and is not overwritten by `refresh_card` from live tunables or from `suppression(dots)` (`cards-scoring.py:247-251`; `evaluate.py.part2:60-81`). `card_score` remains the only ranking authority (ADR-0009 D4). Null scores sink by the existing WATCH tie policy (`evaluate.py.part1:134-138`). Proximity stays computed from live entry/stop (same path as `trail_fit` N/A). C1 has no `assumed_keys` column yet: rubberband still sets `score_suppressed = assumed_formation` because A-01 is assumed. The chip and view column land in C2.

Without persist-on-refresh: he rules A-02, next scan `refresh_card` calls `score_card` which only suppresses on N/A computed dots (`cards-scoring.py:247-268`), and a hitchhiker card that formed on assumed A-02 would show a score. L52(a)/L57 hole.
Suppressing the score is not a second ranking authority. Chip-only would leave an unmarked modelled number in `card_score` (L52(a) fail). Cost: early cards show no score. That matches R17.

### O5 — ADOPT WITH (paste)
> Store: one vault note `1 - Trading/4 - Strategies/Assumed Defaults.md`, marker unit `tunables:assumed`, rows `source: assumed` (`TunableSource.ASSUMED`). Cobalt writes that unit with a new L28 command (create-if-absent, deterministic, versioned `vault_writes`, dry-run `cobalt taxonomy tunables --assumed`, proven on the dev vault first). The desk does not write unruled numbers (L65). R15 is the what (defaults assumed and marked), not a L73 override of L65. `merge_tunables` hole-fill: a user row may fill an engine row only when engine `value is null` AND user `source == assumed` AND user `scope ==` engine `scope` AND keys equal. Any other collision stays loud (`taxonomy-loader.py:90-112`). Engine null → non-null in the same load as dropping the assumed row, or the merge fails loud. Owner edit of the unit: human wins (L28). Open cards keep the `assumed_keys` they formed with.

Hole-fill as written (null engine value only) widens: a `per_trade(hitchhiker)` row for `range.wick_ratio_max` would fill the global engine key for every def that reads it. Constrain scope.
L65: “Never a value he has not ruled.” Assumed rows are unruled by definition (`laws-excerpt.md` L65). R15 does not name a file, a sha, or a desk write. Cost of L28 path: +S on C2 (command + marker unit + parser proof). Desk-write is cheaper and unlawful.

### O6 — ADOPT WITH (paste)
> Frame series: `run` = RTH only, unchanged (Extension, Legs, Range, DayRange, RangeBreak, RTH VWAP, session open). `warm` = complete premarket 2m buckets through now, used only to seed EMA9, EMA21, and a **new** quantity `atr_seeded`. The Extension's RTH Wilder ATR stays the existing seam observation `atr_working` (`evaluate.py.part1:568`, `anatomy-extension.py:112`). Do not rename it `atr_run`. `ev.ema9` for card health (`evaluate.py.part1:560-564`; health consumer in greps) stays the RTH-run EMA until C3 bumps `EVALUATOR_VERSION` and gate 5 refuses old receipts. Two quantities, two names.

Proposal name `atr_working` for the seeded ATR collides with today's Extension ATR observation. Renaming the live name moves Rubberband `atrs_from_open` inputs on replay of old receipts (`evaluate.py.part1:438-445`). Seeding `ev.ema9` without a version bump silently moves FILLED-card health. RTH-only would leave EMA21(2m) with no value until 21×2 min after 09:30 = 10:12 ET (`anatomy-indicators.py:157-161`; E7). X1 before C3.

### O7 — ADOPT
Literal `TAXONOMY-DRAFT-v0_7.md:94` (“first pullback ≥1 opposing bar”) makes hitchhiker's precondition (`note-hitchhiker.md:35`) almost never True and its avoid (`:68`) almost always True: the first opposing bar already ended the drive as `pullback`. Concrete: 20-bar up drive, then an 8-bar sideways micro-Range from the extreme — literal path never forms a hitchhiker card. The proposed rule (micro-Range from the drive extreme within A-07 retrace ⇒ `terminated_by: consolidation`) is the only reading that can form. It is modelled, key A-07, score suppressed. Not his to rule before cards (R15/R17). Taxonomy amendment is `OWNER (after cards)`.

### O8 — ADOPT
No catalyst collector (gap table G12). Leaving `catalyst_ref` unknown → `not_formed` / path-B (`evaluate.py.part1:619-622`). A tap gate forms no card until he taps — contradicts R17. A-13 is a constant True on the evaluated set: every S5 member is already admitted (`evaluate.py.part1:320`; G8). Concrete residual: an unexplained-RVOL name with no news still forms a nine-ema-scalp card once D3/D1 land. Mark A-13 on the atom, chip on the card, `catalyst` dot stays YOURS (`evaluate.py.part1:683-692`). Weakened intent is visible, not silent.

### (a) DIRECTION
The category-error reading is **right for rubberband** (`note-rubberband.md:36-41` 4+1 mix; trigger/stop only make sense fading the culminating Extension; proof test A/B). It is **right that relation is not Extension-vs-trade** for all seven (`TAXONOMY-DRAFT-v0_7.md:136-137`).

It is **not** true that `trade_direction = against ext.direction` is safe for every one of the seven.

| slug | `valid_setups` | direction source | `against ext.direction` |
|---|---|---|---|
| rubberband | mixed 4+1 | fade culminating Extension | correct (C1) |
| backside | mixed 4+1 | [user data: note-backside.md:97-102] | **wrong side** if last > open |
| fashionably-late | mixed 4+1 | [user data: note-fashionably-late.md:39-44] | frame, not against-ext |
| hitchhiker | all `with_trend` | [user data: note-hitchhiker.md:28-38] | **wrong side** |
| second-chance | all `with_trend` | [user data: note-second-chance.md:101-108] | **wrong side** |
| nine-ema-scalp | all `with_trend` | [user data: note-nine-ema-scalp.md:37-46] | **wrong side** |
| vwap-continuation | all `with_trend` | [user data: note-vwap-continuation.md:34-41] | **wrong side** |

Concrete wrong-side, backside: open 10.00, low 9.50, last 10.40, [user data: note-backside.md:97-102]. `detect_extension` direction is `up` (`anatomy-extension.py:96-103`). Against = short. Correct trade = long. C4 must use the frame, not C1's one-liner.
`setup_ref = unclassified` is honest: nothing in `src/cobalt/radar` detects a setup (proof report; greps `relation` only at `evaluate.py:35,635,647`). The `setup_relation` tap stays YOURS (`evaluate_cli.py:35`).

### (b) THE MIRRORED FRAME
Non-equivalences (file:line), not a complete list of detectors:

1. `structural_stop` additive buffer + round-away + ten-cent nudge — `anatomy-structure.py:13-21,96-116`. Property test as written fails (O2 sequence).
2. `DayRange.upper_third` = low + ⅔(high−low) — hitchhiker `note-hitchhiker.md:38`. `detector(mirror)` computes the mirrored **lower** third, not the mirror of the upper third. Frame pipeline is OK; the stated property test is not.
3. `RadarCardSpec` `gt=0` on trigger/stop — `cards-radar.py:86-88`. Negative prices never reach a card if negate-back holds; they crash create if it does not (fail-loud, good).
4. Stop buffer `buffer <= 0` refused — `anatomy-structure.py:101-102`. Mirror must not negate the buffer.
5. HTF proximity exact-tie → `prior_high` — `anatomy-daily.py:147-149`. Value is even; the label is frame-local.
6. `htf_range_break` up/down from session vs prior H/L — `anatomy-daily.py:182-196`. Booleans flip with high↔low; `day_count == 1` avoid (rubberband) is directionless and preserved.
7. Extension path-A volume band — volume unchanged, `bar.direction` flips with close−open and so does run direction (`anatomy-extension.py:98-131`). Equivalence holds.
8. ATR / EMA seed — ATR is even (true range); EMA is odd (closes). Staged models do not `gt=0` prices (`anatomy-bars.py:44-47`).
9. Decimal prec 28 — `anatomy-indicators.py:26-27,40`. Sign-symmetric if the property is the frame pipeline.
10. Tick/round-number: the ten-cent grid **is** the round-number law. No other tick size in staged anatomy.

`detector(mirror(bars)) == mirror(detector(bars))` is **not** enough: it false-fails (1)(2) and does not mention (3). Use O2's replacement property. X4 on stored days, detector by detector, with that property. X6: whether archiver `Bar` accepts negative OHLC (not in this folder).

### (c) L52 (a)–(d)
**(a) ADOPT WITH** the O4 persist + C1 A-01 suppression + recorder that wraps every `resolve_cfg` / `_cfg_value` / `from_tunables` read, not only the interpreter `cfg` at `evaluate.py.part1:601-602`. `consulted` today records **atom names**, not cfg keys (`evaluate.py.part1:221-228`). Unmarked numbers that can reach a card: A-01 on C1 if suppression is deferred to C2; A-05/A-13 resolver outcomes if only `source: assumed` cfg rows are recorded; proximity from an assumed trigger/stop (traceable to receipt prices — chip marks the card); `ev.ema9` if seeded without a version bump (O6).

**(b) ADOPT.** One ranking authority: `card_score` (ADR-0009 D4; `cards-scoring.py:1-4,264-267`). Formation, side binding, and `assumed_formation` do not add a second. WATCH order is that same score, nulls last, then pool position (`cards-radar.py:23-29`). Tie policy unchanged.

**(c) ADOPT WITH** these seams named as artifacts in the chunk that adds them: `Formation.assumed_keys`, `score_suppressed=assumed_formation` persisted on the row (not only on `RadarScoreDetail`), `TunableSource.ASSUMED`, hole-fill predicate (O5), `atr_seeded`, Frame, `TRIGGERS`/`STOPS`/`RELATIONS` registries, `assumed_keys` view column + `FIELD_OWNERS` badge (panel import check `radar-panel-owners.excerpt.py:8-11`). Gate 5 is a real test: `replay_receipt` today does **not** refuse a version mismatch (`evaluate.py.part2:344-365` — always `evaluate_member` with current code).

**(d) ADOPT** if C2 puts assumed rows in the tunables snapshot the receipt already stores (`evaluate.py.part3:138-141`) and new modules join `FORMULA_FILES` (`evaluate.py.part1:144-152`). `cobalt radar audit-export` exists (greps). Another house can replay from that bundle. Mirrored-frame tests need no DB.

### (d) ASSUMED VISIBILITY
Paths that can miss `assumed_keys`:

1. C1 A-01 — convention, not a cfg key. If only `source: assumed` rows are recorded, rubberband scores unmarked.
2. `_cfg_value` / `ExtensionParams.from_tunables` / stop buffer — not the interpreter `cfg` (`evaluate.py.part1:419-422,653-657`; `anatomy-extension.py:54-63`).
3. A-13 / A-05 — resolver outcomes, not cfg keys. Proposal L52 table already marks them; the recorder must.
4. Hole-filled row consumed by a detector that never calls `cfg()` (Range touch A-03, bound-flat A-04, snapback A-08).
5. `refresh_card` — formation evidence never touched (`evaluate.py.part2:71-74`) but `score_suppressed` is recomputed from dots (`:78-81`). Open card can gain a score after a ruling (O4 scenario).
6. Code defaults (`ATR_PERIOD = 14`, `anatomy-indicators.py:39`) — ruled/taxonomy, not assumed. Leave them.

`assumed_formation` as specified does **not** cover (1)(2)(5) without the O4/O1 C1 wording. With it, yes.

### (e) THE STORE
Hole-fill cannot lawfully widen past “engine row, committed value null, same key, same scope, user source assumed.” Owner later edits the assumed unit: next load uses the new value; open cards keep formation inputs (L57). Engine null → value: merge must fail unless the assumed row is gone in that same load (else two sources for one key, L3/L1).
ESCALATE 7: R15 is **not** a L65 write instruction. Build the L28 Cobalt-owned unit (O5). Cost +S on C2 vs a desk paste. Do not treat R15 as a L73 override of L65 — R15 does not name the note or the values.

### (f) ACCEPTANCE
Walk the Rubberband miss through gates 1–5:

| gate | would it have caught it? |
|---|---|
| 1 real-shape `formed` on a 4+1 note | **Yes**, if the fixture is the mixed shape (today's suite used single-relation `anatomy_def` — proof “Why the S2-P2 suite… were green”). |
| 2 evaluable ⇒ forms | **Yes.** Registry already calls rubberband evaluable (`anatomy-registry.py:27-38`; gap table). Property test would have been red on main. |
| 3 live-note asserts `formed` | **Yes if run.** Today it only asserts rubberband is not stuck at `not_evaluable` (`test-live-note.excerpt.py:34-37`) and is skipped unless `COBALT_LIVE_VAULT_ROOT` is set (`:9-10`). |
| 4 `--expect-formed` RED on 0 | **Yes for 09-19** (`formations=0` accepted). Needs a known day. |
| 5 old receipt refused | **No** for the original miss (no formed rubberband receipt). Needed later. Today replay does not refuse (part2:344-365). |

Still green while forming nothing: fixture day chosen by the builder house (gate 1 “checker confirms by chart” is not a test); a replay day that forms for the wrong reason (with-trend geometry still `formed` — proof test B); a def the registry marks not evaluable (property test never runs — by design); live-note skipped because the env is unset; **zero tagged rubberband and zero tagged backside** in `trade-tags.txt` (hitchhiker / fashionably-late / nine-ema-scalp / vwap-continuation / second-chance tags exist; `nine-ema-reclaim` is a different slug). Gate 4 cannot key rubberband/backside off tagged trades until X2 finds pool days.

### (g) WARM-UP AND SESSIONS
No existing Rubberband number moves **if** Extension ATR stays RTH-run under the live name `atr_working` and `atrs_from_open` keeps using `ext.atr` (`evaluate.py.part1:437-445`). Dots/curves unchanged by this design. Receipt already holds premarket i1 (`evaluate.py.part1:498-500`) — L57 for a seeded value is OK.
`ev.ema9` **does** move if C3 seeds it and health keeps reading it — that is an existing FILLED-card number. O6 wording forbids the silent move.
“Two quantities, not two paths” is true only with two names. As written, `atr_working` is a second implementation of the **same name**. `wilder_atr` is one function (`anatomy-indicators.py:99-113`); calling it on `warm` vs `run` is two inputs, one path — good — **if** the outputs are stored under different names.

### (h) CHUNKS AND EXPERIMENTS
C1 is **S for logic** (direction + token + geometry guard + `assumed_formation` on A-01). It does **not** need C2 registries. Gates 1–5 and X2/X3 are most of the work; still one evening if X2 has any stored day. Geometry guard is worth having (fail-loud inverted stop) but did **not** catch the with-trend control (WRONG FACTS).
C3 at L is too big for one checked deploy evening (D1+warmup **and** Range(micro), the largest group in the gap table). **Split:** C3a D1+warmup (M, unlocks none alone) then C3b D2+D3 hitchhiker (L). Order C1 → C2 → C3a → C3b → {C4, C5, C6} → C7 stands; C7 still reuses C6 levels. C4/C5/C6 after C3b is honest: backside needs Range+EMA, nine-ema needs pullback roles, vwap needs dist+levels.
X1 before C3a/C5 — yes. X2 before C1 fixture — yes. X3 before C1 deploy — yes. X4 with C2 — yes, on the O2 property. X5 with C2 — yes. Missing: X6 (negative `Bar`), X7 (gate 5 — already settled from reads: no version check), X8 (`refresh_card` vs persisted `assumed_formation`).

Scan latency, arithmetic from staged files: `radar.scan_interval` **= 100 seconds** (`tunables.yaml:468-469`). Today `not_evaluable` returns before `working_bars` (`evaluate.py.part1:517-524`), so ~1 full path × 50 members. After C2: 7 defs × 2 frames × 50 = **700** full `evaluate_member` calls vs ~50 today ≈ **14×** full-path CPU. Whether 700 × p95(`evaluate_member`) > 100 s is **UNVERIFIED — X5: time 7 defs × 2 frames × 50 members on `cobalt_dev` against a 100 s budget**. If it exceeds, drop the second frame to on-demand (only evaluate short when long failed, or the reverse) rather than side-aware detectors.

### (i) NOT CHECKABLE FROM READS
- **X1:** share of pool names with ≥ period complete 2m premarket buckets by 09:30, last 10 stored sessions. Low ⇒ earliest windows stay empty; do not drop the seed, report the rate.
- **X2:** whether `cobalt_dev` holds i1 for tagged trade days in `trade-tags.txt` (2025 dates — coverage unknown). None ⇒ C1 fixture is a checker-confirmed pool day, not a tagged trade.
- **X3:** `cobalt radar evaluate --replay` last 10 stored sessions after C1: rubberband `formed` > 0 somewhere. Zero is allowed (proof ESCALATE 2) and is not a C1 defect.
- **X4:** O2 property, detector by detector, on stored days. A fail that is only the old property test is not a defect.
- **X5:** scan latency at 2× evaluation (above). Result that changes the design: p95 over 100 s → sequential frames or a smaller pool during C2, never silent miss.
- **X6:** construct mirrored i1 as archiver `Bar`. If `gt=0` (not staged), Frame must wrap `WorkingBar` only, never round-trip through `Bar`.
- **X8:** after C2, form a card on an assumed key, then change that row's `source` to `ruling`; assert the open card still has `score_suppressed=assumed_formation`.

X7 is no longer an experiment: `replay_receipt` recomputes with current `evaluate_member` and does not read `EVALUATOR_VERSION` (`evaluate.py.part2:344-365`). Gate 5 is a C1 build, not a measurement.

### Closing line
`TRIBUNAL R1: BUILD AFTER scoped A-01, atr name, hole-fill, assumed persist`

## Checked against the files
Real files opened by the hub: `/Users/cobalt/cobalt/src/…` (Read / grep), the notes under `/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies/`, `cards/store.py`, `replay/runner.py`, `replay/formations.py`, `radar/seam.py`, `archiver/models.py`. Line numbers below are the ORIGINAL files' (the packet's `part` numbers add to them: `part2:N` = `evaluate.py:699+N`; `part3:N` = `evaluate.py:1096+N`). Only Grok made claims (Astra and Gemini did not rule).

| # | claim · who | file:line | verdict | note (≤30 words) |
|---|---|---|---|---|
| 1 | Evaluator reads `valid_setups[].relation` as trade-vs-Extension; the field is setup context · grok | `evaluate.py:635-647`; `TAXONOMY-DRAFT-v0_7.md:124,136-137` | HOLDS | Gate reads the relation set at :635-646; taxonomy puts `relation` on the setup entry and direction separately. |
| 2 | Rubberband is a 4+1 mix; proof: mixed def `not_evaluable` on all 71 scans · grok | `note-rubberband.md:36-41`; `rubberband-proof.md` test A | HOLDS | Note lists five entries (four countertrend, one with-trend); the proof report states the 71 scans. |
| 3 | Backside: mixed 4+1, unqualified `Extension.state == backside` anchor · grok | `note-backside.md:90-94,98` | HOLDS | Five `valid_setups` entries mixed; anchor is unqualified. |
| 4 | Fashionably-late: mixed 4+1, `Extension.state IN {reverting, backside}` · grok | `note-fashionably-late.md:32-36,40` | HOLDS | As stated. |
| 5 | Hitchhiker, second-chance, nine-ema-scalp, vwap-continuation are all `with_trend` · grok | `note-hitchhiker.md:29-30`; `note-second-chance.md:102-103`; `note-nine-ema-scalp.md:38-39`; `note-vwap-continuation.md:35-36` | HOLDS | Every entry is `with_trend` in all four. |
| 6 | `against ext.direction` would put those four on the wrong side · grok | `PROPOSAL.md:33`; notes (grep `Extension`) | DOES NOT HOLD | The proposal binds it to defs "whose precondition anchor is an unqualified Extension"; the three have none, nine-ema only `Extension.instantiated on Leg(pre_test)` (qualified, `note-nine-ema-scalp.md:78`). |
| 7a | Extension direction = sign(last close − session open); C1 gate flips it · grok | `anatomy/extension.py:96-103`; `evaluate.py:636-637` | HOLDS | Direction is computed from close vs open; countertrend branch sets short on `up`. |
| 7b | So a backside card forms SHORT when last > open with a rising range · grok | — | UNVERIFIABLE FROM READS | No backside detector exists (`extension.py:70` produces `culminating\|none`); needs the C4 build. Run: evaluate a backside fixture with last > open once D4 exists. |
| 8a | Long stop E=10.02, buffer 0.02: raw 10.00 → nudged 10.01; long on mirrored extreme −10.02 → −10.04 · grok | `anatomy/structure.py:100-116`, `:96-98` | ARITHMETIC OK | 10.02−0.02=10.00; on-grid → toward-structure 10.01. −10.02−0.02=−10.04, off-grid, no nudge. Both calls use trade_direction `long`. |
| 8b | The stated property test is false for the stop · grok | `structure.py:100-116`; `PROPOSAL.md:55` | HOLDS | With `trade_direction` fixed to long in both frames (proposal :55) the two values differ (−10.04 vs −10.01). A long↔short-mapped comparison is not stated in the proposal. |
| 9 | Mirrored `upper_third` is the original lower third, not its mirror · grok | `note-hitchhiker.md:38`; `assumed-values.md` A-06 | HOLDS | low+⅔(high−low) after negate/swap = −(low+⅓·range). By reading, not run. |
| 10 | `RadarCardSpec` trigger/stop `gt=0`; long stop must sit below trigger · grok | `cards/radar.py:86-88,106-114` | HOLDS | Both fields `Field(gt=0)`; `_stop_side` validator refuses a wrong-side stop. |
| 11 | HTF proximity tie → `prior_high`; range-break up/down from session vs prior · grok | `anatomy/daily.py:147-149,182-196` | HOLDS | `to_high <= to_low` picks prior_high; up/down/outside-day as stated. |
| 12 | Stop buffer `<= 0` refused · grok | `anatomy/structure.py:101-102` | HOLDS | ValueError on non-positive buffer. |
| 13 | Staged `WorkingBar`/`DailyBar` carry no price positivity · grok | `anatomy/bars.py:44-47`; `daily.py:49-52`; `greps.txt` | HOLDS | OHLC are bare `Decimal`; only volume/minutes carry `ge`/`gt`. |
| 14 | Archiver `Bar` accepts negative OHLC (X6) · grok (as an unknown) | `archiver/models.py:41-45` | HOLDS (field level) | OHLC are bare `Decimal`, volume `ge=0`. A `model_validator` was not searched. |
| 15 | Python `%` on negative cents behaves symmetrically · grok | `structure.py:96-98` | UNVERIFIABLE FROM READS | Behaviour of `Decimal % 10` on negative values not run. Run: `_on_ten_cent_grid` on `Decimal('-10.00')` and `Decimal('-10.04')`. |
| 16 | `setup_ref` is `str`; `SetupRef` has no `unclassified`; `card_why` leads with it · grok | `cards/radar.py:84`; `taxonomy/trade_def.py:155-165`; `evaluate.py:674-680` | HOLDS | As stated. |
| 17 | `refresh_card` recomputes `score_suppressed` from dots and the store writes it back · grok | `evaluate.py:777-779,798-803`; `cards/scoring.py:247-251,319-336`; `cards/store.py:1039-1047` | HOLDS | `score_card` suppresses only on N/A computed dots; the UPDATE writes `update.score_suppressed` unless taps moved. Nothing preserves a create-time string. |
| 18 | Hole-fill as proposed can widen by scope: a per-trade row fills a global engine key for every def · grok | `PROPOSAL.md` §8; `taxonomy/loader.py:104-126`; `tunables.yaml:73-80` | HOLDS | Proposal states no scope condition; `merge_tunables` is key-only and `resolve_cfg` returns `row.value` by key. Engine `range.wick_ratio_max` is global, null. |
| 19 | R15 names no file, sha or desk write · grok | `owner-rulings.md` R15 (`cto-2026-09-21.md:27`) | HOLDS | Text names no note. Whether it is a per-case L73 override is a ruling, not checked. |
| 20 | Seeded ATR name `atr_working` collides with today's seam observation · grok | `evaluate.py:568`; `PROPOSAL.md` §5 | HOLDS | `_obs("atr_working", ext.atr.value …)` is the Extension's ATR. |
| 21 | Renaming that observation moves Rubberband `atrs_from_open` inputs · grok | `evaluate.py:438-445,568`; `radar/seam.py:106` | DOES NOT HOLD | `atrs_from_open` inputs are keyed `atr`, `atr_period`, `atr_bars_used`; the observation name only needs to match `IDENTIFIER`. |
| 22 | `ev.ema9` is the RTH-run EMA and feeds FILLED-card health; the proposal does not address it · grok | `evaluate.py:560-564,794`; `PROPOSAL.md` §5 | HOLDS | `ema(run, ma.fast)`; passed to `card_health`. §5 names only the Extension ATR and `atrs_from_open` as unmoved. |
| 23 | EMA21 on 2m has no value before 10:12 ET · grok | `anatomy/indicators.py:157-161` | ARITHMETIC OK + HOLDS | 21 bars × 2 min = 42 min after 09:30 = 10:12; warm-up raises `InsufficientBars` below `period`. |
| 24 | `replay_receipt` does not read the evaluator version · grok | `evaluate.py:1043-1089` | HOLDS | Only `evaluate_member` with current code; `evaluator_version` appears at :928, :1253 only. |
| 25 | "Replay does not refuse a version mismatch; gate 5 is a build, X7 settled" · grok | `replay/formations.py:81,145-148`; `replay/runner.py:219-224` | DOES NOT HOLD | The nightly formation replay refuses any evaluator version outside `{"s2p2.1"}`. (Hub-noted: a C1 bump of `EVALUATOR_VERSION` meets that check.) |
| 26 | `consulted` records atom names, not cfg keys; cfg reads exist outside the interpreter · grok | `evaluate.py:221-228,419-422,653-657`; `anatomy/extension.py:54-63` | HOLDS | `Cfg` branch does not record; `_cfg_value` and `ExtensionParams.from_tunables` read tunables directly. |
| 27 | Live-note test asserts only "not stuck at `not_evaluable`" and skips without the env var · grok | `test_radar_evaluate.py:686-688,714` (excerpt) | HOLDS | As stated. |
| 28 | Zero tagged rubberband / backside trades; `nine-ema-reclaim` is another slug · grok | `trade-tags.txt` | HOLDS | Neither slug appears; `nine-ema-reclaim` and `nine-ema-scalp` both do. |
| 29 | WRONG FACT 1: the geometry guard would not have refused the with-trend control · grok | `rubberband-proof.md` test B; `cards/radar.py:106-114` | HOLDS | With-trend def formed long and created cards on two scans; the same "long stop below trigger" check passed at create. |
| 30 | WRONG FACT 3: "every setup gives the same side" is used beyond rubberband · grok | `PROPOSAL.md` §1, Open 1; `note-backside.md:98` | HOLDS | §1 states it for rubberband/backside/fashionably-late; backside's anchor is unqualified. |
| 31a | Latency: 7 defs × 2 frames × 50 members = 700 vs ~50 today (≈14×); `scan_interval` 100 s · grok | `tunables.yaml:467-474` | ARITHMETIC OK | 7×2×50 = 700; 700/50 = 14. |
| 31b | Not-evaluable defs return before `working_bars` · grok | `evaluate.py:517-524,526` | HOLDS | Early return precedes the aggregation. |
| 31c | Whether 700 × p95 exceeds 100 s · grok | — | UNVERIFIABLE FROM READS | Run X5: time it on `cobalt_dev`. |
| 32a | Literal taxonomy: first opposing bar ends a leg as `pullback` · grok | `TAXONOMY-DRAFT-v0_7.md:94` | HOLDS | Text reads "terminated by the first pullback (≥1 opposing bar) or consolidation". |
| 32b | So hitchhiker's precondition is almost never True (A-07) · grok | — | UNVERIFIABLE FROM READS | Run: evaluate hitchhiker on stored drive-then-range days under both readings. |
| 33 | A-13 is constant True on the evaluated set (every member already admitted) · grok | `evaluate.py:320,1287-1288` | HOLDS | Members come from admitted pool; departed ones form no new card. |
| 34 | C1 does not need C2 · grok | `PROPOSAL.md` §10 | HOLDS | Chain is C1 → C2 → … as stated. |

Also hub-noted, claimed by no house: `vault_loader.py:271-280` refuses a tunables row whose scope is not `per_trade(<slug>)` of the note it sits in; the proposal's `Assumed Defaults.md` rows carry `scope` `global` or `per_trade(<slug>)` (§8).

Counts: HOLDS = 30 (rows 1,2,3,4,5,7a,8b,9,10,11,12,13,14,16,17,18,19,20,22,23,24,26,27,28,29,30,31b,32a,33,34) · DOES NOT HOLD = 3 (6, 21, 25) · UNVERIFIABLE FROM READS = 4 (7b, 15, 31c, 32b) · ARITHMETIC OK = 3 (8a, 23, 31a).

## Experiments named (L70)
| experiment | named by | gates (house's claim) | result that would change the design |
|---|---|---|---|
| X1 premarket-seed viability (share of names with ≥ period complete 2m premarket buckets by 09:30, last 10 sessions) | proposal, grok | C3a / C5 | Low rate ⇒ earliest windows stay empty; report the rate, keep the seed. |
| X2 does `cobalt_dev` hold i1 for tagged trade days | proposal, grok | C1 fixture choice | None held ⇒ C1 fixture is a checker-confirmed pool day. |
| X3 C1 `--replay` over the last 10 stored sessions | proposal, grok | C1 deploy | Zero rubberband formations is allowed (proof ESCALATE 2), not a C1 defect. |
| X4 mirror equivalence on stored days, detector by detector, on grok's replacement property | proposal, grok | C2 | A fail that is only the old property test is not a defect. |
| X5 scan latency at 7 defs × 2 frames × 50 members vs 100 s | proposal, grok | C2 | p95 over 100 s ⇒ sequential frames / smaller pool, never a silent miss. |
| X6 mirrored i1 as archiver `Bar` | grok | C2 Frame | Field-level: OHLC unconstrained (`archiver/models.py:41-44`); a model validator was not searched. |
| X7 replay version mismatch | grok (called settled) | C1 gate 5 | Hub check: `replay_receipt` reads no version, but `replay/formations.py:81,145` and `replay/runner.py:219-224` refuse versions outside `{"s2p2.1"}`. |
| X8 form a card on an assumed key, then change the row `source` to `ruling`; the open card must keep `assumed_formation` | grok | C2 | Card gains a score ⇒ suppression must be persisted (see row 17). |
| Not a house's: `Decimal % 10` on negative cents (row 15); backside/last>open outcome (7b); A-07 literal-reading effect (32b) | hub | — | See the rows. |

## OWNER ITEMS (after cards)
Grok's `OWNER (after cards):` list, verbatim (no redaction needed):
- Every A-01…A-23 value, including whether A-07 amends `TAXONOMY-DRAFT-v0_7.md:94` or stays assumed.
- Whether A-13 (in-play as “or setup”) is an acceptable catalyst proxy, or a tap later.
- Note-vs-sheet: fashionably-late stop anchors (`note-fashionably-late.md:47-51` vs sheet; design follows the note); vwap-continuation `rejected` as avoid (`note-vwap-continuation.md:81` vs sheet decreasing factor).
- Whether setup identity is later an engine `setup_relation` dot under L7 shadow.
- Whether to collapse to one ATR after a Rubberband shadow (do not move Extension ATR in this design).
- One ATR vs two; fixture/replay days from his tagged trades (report STATS list).
- L11 explicit `frontier` marks on the six defs that only have text/human factors (note edit, L65).

Grok: "None of these is a precondition to build." No house made an owner item a precondition; nothing conflicts with R15 / R17.

## WRONG FACTS claimed
| # | Grok's claim | hub file-check |
|---|---|---|
| 1 | `PROPOSAL.md` §2.3: the geometry guard "alone would have turned the with-trend Rubberband card of the proof's control into a refusal" — proof test B shows it formed long and created cards | HOLDS (row 29): the with-trend control formed and created cards on two scans; the guard's condition is already enforced at card creation (`cards/radar.py:106-114`). |
| 2 | §5 / Open 6: the seeded ATR is named `atr_working`, already the Extension's seam observation | HOLDS (row 20). |
| 3 | Open 1 / §1: "for these defs every setup gives the same side" is used to justify `against ext.direction` beyond rubberband | HOLDS as a reading of §1 (row 30); the four with-trend defs are outside the rule (row 6). |

## ESCALATE
1. **ASK DESK: astra did not rule round 1 (`astra: METER` — verbatim above, reset 11:12 AM) — relaunch it alone inside today's window before the derive?** [10:18 ET] Astra was REQUIRED by this prompt and probed UP at 09:29. Safe default taken: no retry by the hub.
2. **ASK DESK: gemini did not rule round 1 (`gemini: HARNESS` — the `command` permission auto-denied, verbatim above) — relaunch it alone inside today's window before the derive?** [10:18 ET] Safe default taken: no retry, no rule change by the hub.
3. **A number reaching a card unmarked that HOLDS (L52 (a)):** direction and trigger/stop rest on `A-01`, a convention that is neither a `cfg` key nor a resolver, while `PROPOSAL.md` §7's recorder covers "every `cfg(key)` and every assumed resolver" (row 30; grok (c)(a), (d)(1)). One house so far.
No `DO NOT BUILD`, no `REJECT`, no second ranking authority claimed, no owner item written as a precondition, no packet mismatch.

SETUPS TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER scoped A-01, atr name, hole-fill, assumed persist · gemini: HARNESS · astra: METER · houses that ruled: 1 of 3 · claims that HOLD: 30 · blockers to build: 3 · owner items: 7 · ESCALATE: 3
