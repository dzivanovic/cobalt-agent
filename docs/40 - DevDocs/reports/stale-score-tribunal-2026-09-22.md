# Stale-score tribunal, round 1 — report named from PREFLIGHT row 1: date 2026-09-22

## §0 Headline
- Authorization verified against committed files — all checks passed. Grok and Gemini ruled inside their 20-minute windows; Astra held to METER per today's desk R13. Fable seat ruled separately, blind, and its claims were file-checked here.
- Ruled: `TRIBUNAL R1: BUILD AFTER <condition>` from both grok (C1 sequencing) and gemini (version bump + tap_dot fix) — neither REJECTs, neither says DO NOT BUILD.
- Real finding, triangulated 3 ways (my own reads, grok, Fable): the proposal's premise that "the null-proximity branch is already handled" by the tap/refresh/replay paths is FALSE today — `score_card`/`proximity()`/`CardScore.proximity` are all non-Optional; only `card_score()` tolerates None.
- Status: **STALE SCORE TRIBUNAL R1 DONE**. Fable R1 claims checked: 8 of 9 HOLD (1 UNVERIFIABLE FROM READS, 0 fail).
- ESCALATE count: 1 (packet staged at 174,017 B, over the 110 KB target after all three sanctioned cuts).

## AUTHORIZATION
| check | command | result |
|---|---|---|
| R13 row (push/approve, 09-20) | `grep -n "^| R13 " cto-2026-09-20.md` | found :86, "Push and approved everything...I'm expecting you to run for a while." |
| R23 row (grok/agy through 09-21) | `grep -n "^| R23 " cto-2026-09-20.md` | found :206, "yes" — extends through Monday 2026-09-21 23:59 ET |
| R36 row (STALE stamp) | `grep -n "^| R36 " cto-2026-09-21.md` | found :47, carries "a small STALE stamp on that ticker's row and on its card" — matches required text |
| R40 row (assumed_formation dot) | `grep -n "^| R40 " cto-2026-09-21.md` | found :51, carries "ONE EXTRA DOT THAT CANNOT BE TAPPED" — matches required text |
| Proposal committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md"` | `86df294cdde4037d6c49a7ac438521ba51fa9e6a` — non-empty, OK |
| Proposal stop line committed | `git log -1 -S"STALE SCORE PROPOSED" -- stale-score-design-2026-09-21.md` | same SHA `86df294...` — non-empty, OK |
| Launch row names this file | `grep -n "61-stale-score-tribunal.md" cto-2026-09-21.md cto-2026-09-22.md` | found in cto-2026-09-22.md:33, R27 desk launch row |
| Launch row committed | `git log -1 -S"61-stale-score-tribunal.md" -- cto-2026-09-21.md cto-2026-09-22.md` | `9e1c2bb48d483614c579300c377df696787d355b` — non-empty, OK |
| Extension text present (today = 09-22) | `grep -n -F "Bash(grok *) and Bash(agy *) through 2026-09-22"` | found cto-2026-09-21.md:50, R39 "All approved" |
| Extension text committed | `git log -1 -S"Bash(grok *) and Bash(agy *) through 2026-09-22" -- cto-2026-09-21.md cto-2026-09-22.md` | `77d4c5952ad405185f1d0110c887d3216129a438` — non-empty, OK |
| 14 allow + 3 deny strings each ≥1 in `08-bars-chunk-e-check.md` | `grep -c -F -e "<rule>"` × 17 | all ≥1; `Bash(grok *)`=2, `Bash(agy *)`=2 (lines 1 and 5, as expected); all others = 1 |
| Today's R13 "A" astra override | `grep -n "^| R13 " cto-2026-09-22.md` | found :47, "A" — `61` runs THIS WEEK on Grok · Gemini · Fable without Astra; astra-REQUIRED gate re-issued to "astra: METER — proceed on three" |

No FAILED condition triggered. Launch line's 14 allow / 3 deny strings are byte-identical to the approved `08-bars-chunk-e-check.md` line. No rule added.

## PREFLIGHT
| rule | command | exit | allowed/DENIED + reason |
|---|---|---|---|
| Date + extension + windows | `date` | 0 | `Tue Sep 22 12:46:45 EDT 2026` — date=2026-09-22, covered by R39 extension (proven above); time 12:46 ET is outside both blackout windows (19:25–20:45, 23:20+) — ALLOWED |
| grok present | `grok --version` | 0 | `grok 1.0.25 (f7e67d6988e2) [stable]` — ALLOWED |
| agy present | `agy --version` | 0 | `1.2.8` — ALLOWED |
| base folder exists | `ls scratch/tribunal-bars-0920` | 0 | populated (many prior-tribunal artifacts) — folder exists, ALLOWED, no mkdir run |
| r1 folder recovery check | `ls scratch/tribunal-bars-0920/stale-score-tribunal/r1` | 1 | "No such file or directory" — fresh run, not a relaunch |
| Stagger s1 (`38`) | `tail -n 3 float-handicap-tribunal-2026-09-21.md` | 0 | last non-blank line `FLOAT HANDICAP TRIBUNAL R1 DONE · ...` — matches done prefix, not running |
| Stagger s2 (`52`) | `tail -n 3 stale-marker-check-2026-09-22.md` | 0 | last non-blank line `STALE MARKER CHECK DONE · ...` — matches done prefix, not running |
| Stagger s3 (`54`) | `tail -n 3 stale-marker-deploy-review-2026-09-22.md` | 1 | "No such file" — checked desk row: `grep -n -F "54 has stopped or will not run" cto-2026-09-21.md cto-2026-09-22.md` → found cto-2026-09-22.md:33 (R27), same line also names `61-stale-score-tribunal.md` → "54: no report — not running (launch row)" |
| Stagger s4 (`57`) | `tail -n 3 setups-c1-check-2026-09-22.md` | 1 | "No such file" — checked desk row: `grep -n -F "57 has stopped or will not run" cto-2026-09-21.md cto-2026-09-22.md` → found cto-2026-09-22.md:33 (R27), same line also names `61-stale-score-tribunal.md` → "57: no report — not running (launch row)" |
| Astra launch shape (stdin experiment) | `grep -c -F "Experiment field: **reads started**" setups-tribunal-r2-2026-09-21.md` | 0 | `1` — recorded as working; would append ` < /dev/null` IF astra were launched |
| Astra meter | `grep -n "^| R13 " cto-2026-09-22.md` | 0 | found :47 (09:4x ET), "A" — the three queued design tribunals (`38`, `61`, `73`) run THIS WEEK on Grok·Gemini·Fable without Astra; astra-REQUIRED gate re-issued to "astra: METER — proceed on three"; Codex meter out until Sat 2026-09-26 06:47 ET. **No Codex probe run** — the desk's own ruling already answers PREFLIGHT's astra-shape question; running the probe would duplicate a settled fact, not test one. `astra: METER — reset Sat 2026-09-26 06:47 ET` |

Denial check: `grok`/`agy` not denied at preflight (version calls succeeded). Continuing with Grok + Gemini; Astra recorded METER, not launched, per today's R13 override (this is not a harness failure — it is the desk's own standing ruling for this exact file, read directly from the committed table).

## Packet
Staged in `scratch/tribunal-bars-0920/stale-score-tribunal/r1/` (worktree `agy-trial`). Whole-file copies (`PROPOSAL.md`, `scoring.py`) staged via `cp` and byte-verified with `diff` + `wc -c` against source — both IDENTICAL. Excerpt files built from Read ranges, each range headed `# <real path>:<first>-<last> (anchor "<text>" at :<n>)`. Trailing-whitespace check: `grep -c -E "[[:space:]]$"` on PROPOSAL.md and scoring.py = 0 each, matching their whole-file byte counts exactly.

**Anchor drift found and corrected (panel.excerpt.py, before it was cut — see below):** `def _field(` was spec'd at :877, actually at :915 (+38); `score suppressed:` was spec'd at :957, actually at :998 (+41); "the RANK + WHY fields line" was spec'd at :998, actually at :1039 (found by content search, not a fixed offset). All other anchors in evaluate.py, store.py, cards/radar.py, expire.py, audit_export.py, poller.py, freshness.py, tunables.yaml, LAWS.md, ADR-0009 matched their spec'd line exactly — no drift.

**Branch-state fact found while building `greps.txt`:** `setups/c1-rubberband-0921` does not exist as a git ref anywhere reachable from `/Users/cobalt/cobalt` (`fatal: ambiguous argument`, recorded verbatim). `git branch -a` + `git worktree list` show the actual C1 worktree is `/Users/cobalt/cobalt-wt/setups-c1` on branch `setups/seven-0921`. `c1-facts.md`'s own file:line citations are against MAIN at `23fb828`, not against this branch, so the citations are unaffected — but no house can read a C1-branch diff under the name the packet gives it. Noted in `greps.txt` and in `QUESTIONS.md`'s file list; not chased further (not this hub's lane to rename or re-derive the branch).

Per-file byte counts (`wc -c`, after cuts):
| file | bytes |
|---|---|
| PROPOSAL.md | 20,933 |
| design-digest.md | 7,218 |
| owner-rulings.md | 2,110 |
| c1-facts.md | 1,829 |
| laws-excerpt.md | 7,651 |
| ADR-0009-D4.excerpt.md | 671 |
| scoring.py | 14,048 |
| evaluate.excerpt.py | 19,061 |
| store.excerpt.py | 6,398 |
| cards-radar.excerpt.py | 2,984 |
| clocks.excerpt.py | 4,086 |
| expire-audit.excerpt.py | 2,766 |
| migrations.excerpt.sql | 4,339 |
| greps.txt | 65,092 |
| QUESTIONS.md | 14,831 |
| **total** | **174,017** |

**Over 110 KB.** Applied the cut order in full: (i) `panel.excerpt.py` cut ENTIRELY (was 1,873 B) — its two citations in `QUESTIONS.md` item (h) (`panel.excerpt.py :957`) are now unstaged; the reason text they'd illustrate is still in `PROPOSAL.md` §2 C step 4 and `design-digest.md`'s DIGEST, and `greps.txt` has no dedicated search that reproduces the `score_suppressed` render string — a real (small) gap, disclosed here rather than papered over; (ii) the `0006_radar_score.sql:95-109` range cut from `migrations.excerpt.sql` (~500 B) — `system.radar_score`'s nullable-column shape is still established by W12/W13 in the fact table; (iii) the `evaluate.py:487-505` range (`evaluate_member` head) cut from `evaluate.excerpt.py` (~640 B) — `greps.txt`'s `last_price` search still shows the exact same assignment line (`last_price = last_bar.close if last_bar else None`, :502). All three cuts are named in `QUESTIONS.md`'s file list, in this section, and none of them touch `PROPOSAL.md`, `QUESTIONS.md`, `greps.txt`, or the `refresh_card` / `replay_receipt` / `tap_dot` / `refresh_radar_card` / `score_card` ranges (all protected, none cut).

**Total after all three sanctioned cuts: 174,017 − 1,873 − ~500 − ~640 ≈ 171,000 B — still far over 110 KB.** No further cut is authorized by the cut order (it names exactly these three and no more); greps.txt (65,092 B, the single largest file) is explicitly protected. The overage is dominated by `greps.txt`'s full absolute-path output (17 grep commands + 3 git log commands, ~534 lines, run exactly as specified — `/Users/cobalt/cobalt/...` prefixes make each line long) and by `PROPOSAL.md` + `scoring.py` + `evaluate.excerpt.py`, none of which the cut order permits touching. This is recorded here and under `## ESCALATE`, not silently absorbed or fixed by an unauthorized fourth cut.

## CONTINUE
next: monitor Grok and Gemini to completion or 20-minute timeout (deadline 13:23:41 ET); astra held to METER per today's R13, not launched.

## Clock
| time | trigger | running houses (launch → deadline) | action |
|---|---|---|---|
| 13:03:41 ET | launch | grok launched 13:03:41 → deadline 13:23:41; gemini launched 13:03:41 → deadline 13:23:41 | both launched together, `run_in_background`, independent |
| 13:07:02 ET | completion notice (gemini) | grok still running, 3m21s elapsed of 20m; gemini DONE (exit 0, ~3m21s) | wrote `gemini-ruling.md` byte-for-byte from its printed answer, minus the harness's trailing `[exited with code 0]` line; closing line: `TRIBUNAL R1: BUILD AFTER a separate version bump is added and tap_dot reason drop is fixed` |
| 13:21:18 ET | completion notice (grok) | grok DONE (exit 0, ~17m37s, inside its 20m window) | grok wrote `grok-ruling.md` itself (its own allow string) — 40,001 B, 260 lines; closing line: `TRIBUNAL R1: BUILD AFTER C1 lands, before the A-01 ruling` |
| 13:23:08 ET | collate step, Fable check | both houses DONE; astra METER (not launched, per today's R13) | houses that ruled: 2 of 2 launched (2 of 3 seats total; L67 floor met). Proceeding to collate |

## Rulings table
| item | grok | gemini | astra | agreement | wording offered / reason |
|---|---|---|---|---|---|
| Q1 sink or hold | ADOPT sink | ADOPT sink | — | 2-0 ADOPT | ladder already sinks nulls; a hold is a second ranking input (L52 b) |
| Q2 premarket every-session clock | ADOPT | ADOPT | — | 2-0 ADOPT | RTH-only would be a new owner rule (L53); clock already gates formation |
| Q3 the band | ADOPT WITH (reword) | ADOPT (no reword) | — | 2-0 ADOPT, wording differs | grok: reason text enough, band is ~80s not 20s, two clocks measure different edges |
| Q4 keep stale `last` (C) vs null (D) | ADOPT C | ADOPT C | — | 2-0 ADOPT | COALESCE keeps prior print regardless; D would blank what the STALE stamp marks |
| Q5 FILLED health pills | ADOPT own item | ADOPT own item | — | 2-0 ADOPT | pills aren't a score/rank key; out of scope |
| Q6 tap during staleness | ADOPT WITH (keep stored reason) | ADOPT accept | — | 2-0 ADOPT | grok: tap_dot must not overwrite the stale reason with dots-only suppression |
| Q7 stale-graded taps in agreement stats | ADOPT leave, not a gate | ADOPT WITH exclude, owner item | — | 2-0 ADOPT | no stored staleness-at-tap fact exists; backlog cleanup is his, before promotion only |
| Q8 version bump | ADOPT WITH (detailed gate) | ADOPT WITH separate bump | — | 2-0 ADOPT WITH | both: sharing C1's string across separate deploys breaks the replay/runner gate |
| Q9 pool_position tie-break first? | ADOPT no | ADOPT no | — | 2-0 ADOPT | tie policy already live; nulls join the existing bucket |
| Q10 daily-stale, proximity computed | ADOPT WITH (required-field wording) | ADOPT | — | 2-0 ADOPT | daily-missing returns only reached after the intraday-stale return; `last` still fresh |
| (a) fact base | ADOPT WITH (adds W22, corrects panel cite, corrects arm/expire framing) | ADOPT WITH, no tag (adds radar/store.py:423-425 writer) | — | 2-0 substance agrees; gemini's tag missing | both: §1 holds with named additions; arm/form/expire sentence TRUE |
| (b) option C vs L3 | ADOPT WITH (new `score_last()` helper; proposal's "already handles" premise FALSE) | ADOPT (no tag; agrees paths differ, tap_dot drops reason) | — | 2-0 substance agrees | **verified FALSE today**: `score_card`/`proximity()`/`CardScore.proximity` all require non-Optional `Decimal` — only `card_score()` tolerates None |
| (c) no-bar → proximity 1.0 | ADOPT WITH (safe to delete; doesn't always top WATCH) | ADOPT (holds; safe to delete) | — | 2-0 ADOPT | grok corrects "tops WATCH" — only tops if its conviction is the cohort max |
| (d) the clock | ADOPT (sound in all 4 cases; no smuggled number) | ADOPT (sound; no smuggled number) | — | 2-0 ADOPT | replay soundness conditioned on `rebuild_members` using receipt `as_of` (UNVERIFIED, X10) |
| (e) two meanings of input_stale | ADOPT WITH (field placement wording) | ADOPT (no tag; field is exact) | — | 2-0 ADOPT | required field with no default is the fail-loud choice; a default False would hide the gap |
| (f) L57 replay | ADOPT WITH (version-gate wording; nightly replay never touches card_score) | ADOPT (no tag; version bump + consumers) | — | 2-0 ADOPT WITH, same finding | **verified**: `audit_export.py` has NO receipt-version check today — only writes the field |
| (g) L7 shadow stats | ADOPT (leave past rows, owner item) | ADOPT (exclude, owner item) | — | 2-0 ADOPT | no stored staleness-at-tap fact; forward stop is step 5, backward is his |
| (h) what he sees | ADOPT (two messages, sink is engineering) | ADOPT (two messages, sink) | — | 2-0 ADOPT | can contradict in the ~80s RTH band and outside RTH; sink follows existing null rule |
| (i) racing tap on fresh input | ADOPT keep scoped to stale case | ADOPT keep scoped to stale case (own text agrees with grok despite an earlier drafting slip in this table — see note below) | — | 2-0 ADOPT, same scope | both: leave the fresh-input race as its own item; step 8 stays scoped to the null-proximity case |
| (j) chunks/seats/order | ADOPT WITH (C1 branch is actually setups/seven-0921, not c1-rubberband) | ADOPT (S1/S2 split, Opus floor, off main after C1) | — | 2-0 substance agrees | **verified**: `setups/c1-rubberband-0921` does not exist; C1 = commit `58aa823` on `setups/seven-0921` |
| (k) not checkable from reads | ADOPT WITH (X1-X9 kept + X10-X22 added) | ADOPT (X1-X9 kept, no new X) | — | 2-0 keep X1-X9 | grok adds 13 new experiments; gemini adds none |
| closing line | `TRIBUNAL R1: BUILD AFTER C1 lands, before the A-01 ruling` | `TRIBUNAL R1: BUILD AFTER a separate version bump is added and tap_dot reason drop is fixed` | — | both BUILD AFTER, different conditions named | neither REJECTs nor says DO NOT BUILD |

## Wording offered, verbatim
**GROK, Q3:** "The score and the R36 stamp stay two messages on two clocks. They may disagree. The score line does not say the stamp is present, and the stamp is not a score input. The score nulls only on the evaluator clock (`intraday_staleness`, `2 × radar.scan_interval`, age of the bar close, every session). The stamp stays the poller's `poll_failures` rendering (`radar.poll_bar_max_age_s`, RTH only). No factor, offset, or session gate is added to close the band. While the stamp is on and the score is still live, the score is right. While the score line is on and the stamp is off, the line is right."

**GROK, Q6 (replacing proposal §2 C step 7):** "Taps during staleness are accepted. `tap_dot` does not refuse a normal factor, and it does not recompute `card_score` from stored proximity when that proximity is NULL: `card_score` stays NULL. In that case `tap_dot` does not replace `score_suppressed` with `suppression(dots)`. It writes the stored `score_suppressed` back if that value is non-null, else the constant `PROXIMITY_UNKNOWN` (`"bars stale — no proximity"`) defined once in `scoring.py`. The bars-stale sentence with the close time is owned only by the refresh/replay helper. A tap cannot publish a number and cannot erase the sentence the helper stored. Conviction and the proposed key still update from the tap, as today."

**GROK, Q8:** "When C branches, replace the singleton then on main. Set `EVALUATOR_VERSION`, `DESK_FORMULA_VERSION`, and `SUPPORTED_EVALUATORS` to the same new string. Do not leave the previous string in the set. Ride C1's string only if C and C1 ship in one deploy and no receipt is written at an intermediate version. Otherwise C bumps again on top of C1's string. `audit-export` reads the `evaluator_version` already written on the run/receipt (`evaluate.py:928`, `:1253`) and, if it is missing or not equal to `EVALUATOR_VERSION`, refuses with a version message before `replay_receipt`. No new column: the key is already in that payload; if a run proves it is not on the object audit loads, add it to that same JSON write."

**GROK, Q10:** "Proximity is nulled only when `MemberEvaluation.intraday_stale` is true. `intraday_stale` is a required bool with no default, set from the local already computed at `evaluate.py:527-534`, on every `result()` path. The guard does not read `evaluation`. Daily-missing `input_stale` (`evaluate.py:624`, `:629`) leaves proximity computed from the fresh `last`."

**GROK, (a) [correction to §1]:** "§1a's live path holds: no evaluation-state guard (`evaluate.py:1317-1348`; refresh at `:1345`; the only continue is a missing def at `:1330`), proximity from the old close or from `card.entry` (`:776`), row write (`store.py:1032-1044`), tap rescore from stored proximity (`:1217-1219`), WATCH order (`cards/radar.py:179-183`). Add W22: `audit_export.py:363` calls `score_card` with `last = ev.last_price if ev.last_price is not None else trigger`. That is a scorer, not a row writer, and it is not in W1–W21. W21 (only Rubberband.md names a computed factor) is `UNVERIFIED` — that vault grep is not in `greps.txt`. W19's behavior (null renders as `—`, the reason prints) holds at `radar_panel.py:998` and `:1023`, not at the cited `:957`."

**GROK, (b) [replacing the "one existing branch" claim and step 3]:** "One helper, `score_last(ev) -> Decimal | None`, lives next to `score_card`. It returns None if and only if `ev.intraday_stale`. If `not ev.intraday_stale` and `ev.last_price is None`, it raises `EvaluateError`. Every `score_card` caller uses it and then passes that last through: `refresh_card` (`evaluate.py:776`), `replay_receipt` (`:1079`), the create call (`:1384`), and `audit_export.py:363`. The `card.entry` fallback and the `trigger` fallback are deleted. `score_card(last=None)` sets proximity None, sets `card_score` None via the existing `card_score` guard (`scoring.py:265`), and sets `score_suppressed` to the bars-stale sentence plus any `suppression(dots)` text. `tap_dot` keeps the stored sentence, per Q6. No new dot. No second carrier."

**GROK, (c):** "Delete the entry fallback at `evaluate.py:776` and `:1079`, and the trigger fallback at `audit_export.py:363`. Do not replace them with another price. `last_price` on the row stays `COALESCE` (Q4): a scan whose `ev.last_price` is None leaves the previous `last_price` in the column, including NULL if none was ever stored. It does not write `card.entry` into `last_price`."

**GROK, (f) [plus Q8's version gate]:** "`published_numbers` writes JSON null for a null proximity, conviction, and `card_score`, never the string `"None"`. Publish and `replay_receipt` both go through `published_numbers` (`evaluate.py:1082` already does). The bars-stale sentence is a pure function of `ev`: no closed bar → `"bars stale — no closed bar"`; else `"bars stale — last close HH:MM:SS ET, older than 2 × radar.scan_interval"`, close time = `last_bar.ts + 1 minute` in `America/New_York`. Dot reasons, if any, are appended from `suppression(dots)`. No new column."

**GROK, (j):** "S1 then S2 on one branch. S1 is the pure helper, `intraday_stale`, `score_card(last=None)`, the reason strings, `htf_level_proximity` `stale=intraday_stale`, Optional proximity, `published_numbers` nulls, the version singleton, and the offline tests. S2 is `tap_dot` (Q6) and the taps-moved null (step 8), plus cobalt_dev tests. Seat for the branch is the house's L29 floor (Opus 5 if Claude builds it): S2 writes `"user".aset_sizings` and `"user".card_dot_taps`. No migration (W13; staged `0007:47-49` are nullable; no new column). C branches off main after C1 has landed, not stacked on the unmerged C1 branch, and the version rule is Q8. C does not wait for C2. C is merged before his first A-01 ruling. The R36 stamp build is not a predecessor: `main..s2/stale-marker-0921` is empty in `greps.txt`, and C does not read `poll_failures`."

**GEMINI, Q6 (replacing proposal §2 C step 7, brief form):** accept the tap; "the trader's hand grade is never stale... The score remains null because proximity is null."

**GEMINI, Q8:** `ADOPT WITH a separate version bump` — "C1 is an independent path. If C1 and this design deploy separately, sharing a version bump will break the replay gate in `audit_export.py`."

**GEMINI, (b) [no explicit tag]:** "`cards/store.py:1228` (`tap_dot`) drops the `score_suppressed` reason because it re-evaluates `suppression(dots)` locally without knowing proximity is null. `cards/store.py:1016-1037` (`refresh_radar_card` taps-moved branch) keeps the older `card_score` and `last_price`."

**GEMINI, (i) [no explicit tag]:** "This is a general race condition and belongs outside this design as its own item. C's step 8 correctly handles the stale case by nulling the score when proximity is null, and does not make the fresh case harder to fix later."

## Checked against the files
| claim | who | file:line | verdict | note |
|---|---|---|---|---|
| `score_card`/`proximity()` require non-Optional `Decimal`; `CardScore.proximity` is a required field; only `card_score()` tolerates `None` today | grok (b) WRONG FACTS #3, fable (b) | `scoring.py:254`, `:264`, `:312`, `:319-330` | **HOLDS** | verified directly: read whole function bodies myself; proposal's "already handles" premise for 4/5 paths is false |
| `tap_dot` drops `score_suppressed` down to `suppression(dots)` alone, losing the stale reason on a tap | gemini (b), grok Q6 | `store.py:1217-1222` (packet `store.excerpt.py`) | **HOLDS** | read myself during packet staging; `suppressed = suppression(dots)` has no proximity-aware branch |
| `radar/store.py:423-425` is the real SQL writer of `radar_score.proximity/conviction/card_score`, called from `evaluate.py:1431` | gemini WRONG FACT, grok (a) ("already W12"), fable (b) | `radar/store.py:419-430` | **HOLDS** (citation-completeness disagreement, not a factual conflict) | read the function myself; both houses agree on the underlying fact, disagree only on whether W12's caller-only citation "counts" |
| `ARMED` under `src/cobalt/radar/` matches only the `TIE_POLICY` string at `evaluate.py:135`; no `→ARMED` writer | grok WRONG FACT #1, fable (a) | `greps.txt` (1 match) + `evaluate.py:135` | **HOLDS** | I ran this grep myself during packet staging; matches both houses |
| `design-digest.md`'s own stop line ("can arm, expire or reorder on stale input: yes") contradicts its own §0 headline ("Arm, form and expire CANNOT act on stale input... expiry can only be LATE") | grok WRONG FACT #1 | `design-digest.md` (staged; source `stale-score-design-2026-09-21.md:4` vs `:107`) | **HOLDS** | read both lines myself in the source report before staging |
| `score suppressed:` line is at `radar_panel.py:998`, not the proposal's cited `:957`; RANK+WHY line at `:1039` not `:998` | grok WRONG FACT #2, fable (a) W19 note | `radar_panel.py:996-999`, `:1039` | **HOLDS** | this is the exact anchor drift I found and disclosed in `## Packet` before any house ran — independently rediscovered by both grok and Fable |
| No-bar proximity=1.0 does not necessarily "top WATCH" — only tops if conviction is the cohort max; `card_score = round(conviction × 1.0 × 100)` | grok WRONG FACT #4 | `scoring.py:264-267` | **HOLDS** | arithmetic re-derived myself from the real function: conv 0.5→50 sits below a fresh conv 0.6/prox 0.9→54 |
| Clock band between the stamp (bar-open anchored, 180s) and the score-null threshold (bar-close anchored, 200s) is ~80s of overlap, not the ~20s the proposal's phrasing suggests | grok WRONG FACT #5 (Q3), fable WRONG FACT #1 | `evaluate.py:532-534` (staged), `poller.py:121` (staged), `freshness.py:117-119` (staged) | **HOLDS** | I verified the two anchor points (`last_bar.ts + 1 min` vs `bar.ts`) myself while staging `clocks.excerpt.py` |
| `audit_export.py` (`export_run`) has NO receipt-version check today — it only ever WRITES `evaluator_version` into payloads (`:161`, `:188`); the version refusals at `replay/runner.py:219-224` / `replay/formations.py:145-149` gate the nightly module BINDING, not a receipt | fable WRONG FACT #2, consistent with grok's Q8/(f) reasoning | `audit_export.py:196-260`; `replay/runner.py`, `replay/formations.py` (both grep-confirmed) | **HOLDS** | I read `export_run`'s full hash-check body myself: no `evaluator_version` comparison anywhere in it |
| A third `last` fallback exists at `audit_export.py:363` (`else trigger`), which the proposal's §2 C "Files" list calls "signature only" | fable WRONG FACT #3 / W22 (grok also names this range in (a)) | `audit_export.py:358-364` | **HOLDS** | I read this function myself: `last=ev.last_price if ev.last_price is not None else trigger` is a genuine third fallback in the candidate-evaluation path |
| `setups/c1-rubberband-0921` does not exist as a git ref; C1 is commit `58aa823` on branch `setups/seven-0921` (worktree `/Users/cobalt/cobalt-wt/setups-c1`) | grok (j), fable (j) | `git log --oneline -1 58aa823`, `git merge-base --is-ancestor 58aa823 setups/seven-0921`, `git worktree list` | **HOLDS** | I independently found this same fact while building `greps.txt`, before reading either house's ruling; then re-confirmed with an ancestor check |
| R36 STALE-stamp commit `490c231` touches `radar_panel.py` and is on `main` | fable (j)/ESCALATE 4 | `git show --stat 490c231`, `git merge-base --is-ancestor 490c231 main` | **HOLDS** | verified directly; commit message and diffstat match fable's description exactly |
| `main..s2/stale-marker-0921` is empty (no commits ahead of main) | grok (j) | `greps.txt` git log command | **HOLDS** | I ran this exact command while building `greps.txt`; exit 0, empty output |
| The evaluator clock is sound on replay ONLY IF `rebuild_members` sets `member.as_of` from the receipt, not wall-clock now | grok (d) | `evaluate.py` (`rebuild_members` body not staged) | **UNVERIFIABLE FROM READS** | the function body is outside the packet's excerpt ranges; grok's own X10 names the settling experiment |
| `com.cobalt.aset` restart classification (whether it imports the affected module) | grok (j) | `aset/web.py:47` (not staged) | **UNVERIFIABLE FROM READS** | grok itself flags this as still a guess pending `cobalt jobs restarts <range>` (L42); not contested |
| Gemini's answers to (a) through (k) never use the required `ADOPT` / `ADOPT WITH` / `REJECT` tag — Q1–Q10 are correctly tagged, (a)–(k) are narrative only | — (format compliance, not a factual claim) | `gemini-ruling.md` | **HOLDS** (format gap) | read the file myself; substance is present and inferable, but the required tag is missing on 11 of 21 items |

## Fable round-1 claims, file-checked
Fable's report exists and ends `STALE SCORE TRIBUNAL FABLE R1 DONE` (`stale-score-tribunal-fable-r1-2026-09-22.md`). Checked every `file:line` claim behind an `ADOPT WITH`, `REJECT`, or `## WRONG FACTS` line:
| id | claim (Fable's line) | file:line | verdict | note |
|---|---|---|---|---|
| FC1 | Q1: `ladder_order` sorts WATCH by `_nulls_last(card_score)` first, a null lands `(1,0)`, after every scored card | `cards/radar.py:161-164`, `:179-183` | **HOLDS** | matches `cards-radar.excerpt.py`, staged and verified against source earlier |
| FC2 | Q3/WRONG FACT 1: stamp counts from bar OPEN (`poller.py:117-121`, `bar.ts`), score counts from bar CLOSE (`evaluate.py:533`, `last_bar.ts+1min`); band is 80s in one unit, not 20s | `poller.py:121`, `evaluate.py:532-534`, `freshness.py:117-119` | **HOLDS** | same finding I made independently and grok made independently — triangulated three ways |
| FC3 | Q6: `tap_dot` writes `score_suppressed = suppression(dots)` (dots-only) unless step 7 fixes it, so the stale reason is lost for one scan | `store.py:1218`, `:1222` | **HOLDS** | same file range I already read for the grok/gemini cross-check above |
| FC4 | (a) W22: a third `last` fallback at `audit_export.py:363`, `else trigger` — the proposal's "signature only" undersells it | `audit_export.py:358-364` | **HOLDS** | read myself, see `## Checked against the files` above |
| FC5 | (b): the only pre-existing null branch is `card_score()` (`scoring.py:264-267`); `score_card`/`proximity()`/`CardScore.proximity` all require non-Optional `Decimal` | `scoring.py:254`, `264`, `312`, `319-330` | **HOLDS** | same verification as grok's WRONG FACTS #3, above |
| FC6 | (f)/WRONG FACT 2: `audit_export.py` has no receipt-version check; the version refusals in `replay/runner.py:219-224` and `replay/formations.py:145-149` gate the module binding, not a receipt | `audit_export.py:196-260`; `replay/runner.py`; `replay/formations.py` | **HOLDS** | I read `export_run`'s body myself; confirmed no `evaluator_version` comparison anywhere in it |
| FC7 | (j): C1 is commit `58aa823` on `setups/seven-0921` (worktree `setups-c1`, tip `60ddac4`); no `setups/c1-rubberband-0921` ref exists | `git log`, `git merge-base --is-ancestor`, `git worktree list` | **HOLDS** | I verified this with my own git commands (see above), independently of both grok and Fable |
| FC8 | (j)/ESCALATE 4: R36 stamp commit `490c231` is on `main`; commit touches `radar_panel.py` | `git show --stat 490c231`; `git merge-base --is-ancestor 490c231 main` | **HOLDS** | verified myself, commit message and file list match exactly |
| FC9 | (c): the 1.0 path needs a card alive on a later trade date than its formation, gated by `expires_at` (defaults to the formation day's RTH close, `expire.py:254-261`) | `expire.py` (not staged beyond `radar_expiry` at `:272-312`; `:254-261` is outside the packet) | **UNVERIFIABLE FROM READS** (packet gap, not a contested fact) | the specific `expires_at`-default logic Fable cites sits outside what I staged; grok independently reached a compatible conclusion without needing that range |

Fable R1 claims checked: **8 HOLD** of 9 checked (FC1–FC8); 1 UNVERIFIABLE FROM READS (FC9). No Fable claim DOES NOT HOLD.

## Experiments named (L70)
| experiment | named by | gates which chunk | result that would change the design |
|---|---|---|---|
| X1 (RED on main) | proposal, grok, gemini(keep), fable(keep) | S1 | tapped-card score with a stale bar: main scores non-null, new code must give null + reason |
| X2 | proposal, grok, gemini(keep), fable(keep) | S1/S2 | form→stale→tap→fresh-bar sequence: score null then returns with no extra tap |
| X3 | proposal, grok, fable(widened by (i)) | S2 | racing tap during staleness leaves NULL score |
| X4 | proposal (CHANGED by grok and fable) | S1 (audit gate) | on main, a pre-change stale-scored receipt is refused by MISMATCH; WITH a version gate, refused by VERSION instead — the test target changes with the design choice |
| X5 (RED on main, split into X5a/X5b by grok) | proposal, grok, fable(keep) | S1 | no-bar-today gives proximity 1.0 on main, NULL after; grok's split isolates "no bar" from "prior-session bar" |
| X6 | proposal, grok, gemini(keep), fable(keep) | S1 | `htf_level_proximity` is `input_stale` whenever `intraday_stale` |
| X7 | proposal, grok, gemini(keep), fable(keep) | S1 | stale WATCH card sorts after scored cards; pinned order unchanged |
| X8 | proposal, grok, gemini(keep), fable(keep) | S1 | expiry (deadline/stop_before_arm) unaffected by staleness |
| X9 (hub-run, L41) | proposal, grok, gemini(keep), fable(keep) | none (measurement only) | production occurrence count — a positive count confirms occurrence but does not itself change the design (grok/fable both demote it from "evidence of defect" to a plain count) |
| X10 | grok, fable (independently, same substance) | (c)/(d) | whether a def's window lets a card survive to a later trade date with no bar — settles whether ESCALATE 1's WATCH impact is real or terminal-card-only |
| X11 | grok | Q2 | whether thin tickers actually print gap-minutes as missing bars |
| X12 | grok, fable (same substance) | Q7/(g) | count of `htf_level_proximity` taps recorded on stale `last`, feeding the L7 backlog decision |
| X13 | grok, fable (same substance) | (e) | whether `evaluability` can differ on the slug-match refresh path with an empty `formation_changes` |
| X14 | grok, fable | (f) | whether the stage's and replay's `score_suppressed` text are byte-identical for a stale card |
| X15 | grok, fable | (c) | count of past receipts published with `proximity='1.000000'` on an `input_stale` seam row |
| X16–X22 (grok only) | grok | S1/S2/audit | version-string consumer sweep, `published_numbers` JSON-null check, tap-reason byte-identity, daily-stale/fresh-last interaction, restart derivation, `score_card(` caller sweep, `DESK_FORMULA_VERSION` readers, `radar_panel.py:758` recompute check — full text in `grok-ruling.md` (k), not reproduced here |
| X16 (fable) | fable | (h) | rendering check: does the ladder strip's chip/slot change only after a tap or reload, not on the periodic pool refresh |

Proposal's own X1–X9 (§7) are the baseline; every house keeps them, with X4 and X5 revised as shown and new ones added on top (grok 13, fable 7, several shared).

## OWNER (after the tribunal)
- Whether a stale WATCH card holds its slot instead of sinking (Q1/(h)) — all sources agree sinking is the engineering default; holding would be his call.
- Whether the score clock should be RTH-only (Q2) — L53, his.
- Whether the poller's clock (bar-open, 180s) and the evaluator's clock (bar-close, 200s) should be made to meet (Q3/(d)) — values and any new rule are his.
- Whether past `htf_level_proximity` taps recorded on a stale price are excluded from `shadow_agreement_v` before any L7 promotion (Q7/(g)) — never before this build, only before a promotion.
- Whether `pool_position` as the tie-break among null-score WATCH cards needs its own ruling first (Q9) — all sources say no, not a precondition.
- FILLED health pills on stale bars (Q5) — its own item, out of scope here.
- Whether the ladder re-renders every scan rather than only on card action/reload (h) — today's existing rendering rule, not part of C.
- The R36 stamp's wording, size and colour (carried over from R36, still not ruled).

No house wrote an owner item as a precondition to build (checked against the `## ESCALATE` trigger for that).

## WRONG FACTS claimed
| claimed by | statement | file:line | verdict |
|---|---|---|---|
| grok #1 | `design-digest.md`'s stop line ("can arm, expire or reorder on stale input: yes") contradicts its own §0 headline and `PROPOSAL.md` §1c (arm/form: No) | `design-digest.md` (staged) | HOLDS |
| grok #2 / fable (a) | W19/fact-table cite `radar_panel.py:957` for the suppression line; real line is `:998` (drifted) | `radar_panel.py:996-999` | HOLDS |
| grok #3 / fable (b) | "all five paths already handle null proximity" is false — only `card_score()` tolerates None; `score_card`/`proximity()`/`CardScore.proximity` require non-Optional `Decimal` | `scoring.py:254,264,312,319-330` | HOLDS |
| grok #4 | "tops WATCH" overstates the no-bar/proximity-1.0 case — only tops if conviction is the cohort max | `scoring.py:264-267` | HOLDS |
| grok #5 / fable #1 | clock-band arithmetic: real overlap is ~80s because the two clocks anchor to different bar edges, not ~20s | `evaluate.py:532-534`, `poller.py:121` | HOLDS |
| gemini (unlabeled) | W12 "missed" the explicit SQL writer `radar/store.py:423-425` (grok/fable: already covered via the caller citation `evaluate.py:1431`) | `radar/store.py:419-430` | HOLDS as a fact; the two houses disagree only on whether citing the caller counts as citing the writer — recorded, not resolved by me (L37) |
| fable #2 | `audit_export.py` has no receipt-version gate; the version refusals in `replay/runner.py` / `replay/formations.py` gate the module binding, not a receipt | `audit_export.py:196-260` | HOLDS |
| fable #3 | proposal's "signature only" claim for `audit_export.py` undersells a real third `last` fallback at `:363` | `audit_export.py:358-364` | HOLDS |
| fable #4 (digest, not proposal) | "Only Rubberband.md names computed factors" is not contradicted — recorded as grep-scope only, matching the author's own caveat | (vault, not re-checked) | Fable itself declined to re-check; not adjudicated here either — recorded as the author's own disclosed limitation, not a defect |

## Independence
`grep -c -F -e "-ruling" grok-ruling.md` = 1 — the one match is grok quoting its own launch instruction ("No `-ruling.md` opened."), not a reference to another house's content; not a breach. `grep -c -F -e "-ruling" gemini-ruling.md` = 0. No astra ruling file (not launched, METER). No independence breach found.

## ESCALATE
- No house said `DO NOT BUILD`. No `REJECT` was returned by either house.
- Both houses' `BUILD AFTER` conditions rest on claims that **HOLD** (grok: C1-sequencing facts, verified; gemini: the tap_dot reason-drop, verified) — both count as real, file-verified blockers to build, not stylistic preferences.
- No unmarked number reaching a card was found: every proposed numeric change (proximity NULL, card_score NULL) is explicitly marked with a reason string per L1.
- Second ranking authority: none proposed; ADR-0009 D4 (`card_score` alone orders WATCH) is unchanged by every ruling — L52(b) holds.
- Fable-seat claims that DO NOT HOLD: **none** (8 of 9 checked HOLD; the 1 remaining is a packet-gap UNVERIFIABLE, not a failure).
- No house proposed a number for one of his keys (`radar.scan_interval`, `radar.poll_bar_max_age_s`); both named the keys and left the values his (L53).
- No owner item was written as a precondition to build (checked above).
- **Packet over 110 KB after the cut order**: total 174,017 B after the three sanctioned cuts (see `## Packet`) — still ~64 KB over target. Flagged here per the rule; no further unauthorized cut was made.
- Houses that did not rule: none among the two launched (grok and gemini both produced a `TRIBUNAL R1:` line). Astra was not launched (recorded `METER` per today's desk R13, not a harness failure).
- Independence breach: none (see `## Independence`).
- `ASK DESK`: none needed. Both launched houses ruled inside their 20-minute windows; the Fable seat had already finished; no relaunch or escalation decision was required of me.

## Close
`date`: Tue Sep 22 13:30:39 EDT 2026.

STALE SCORE TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER C1 lands, before the A-01 ruling · gemini: TRIBUNAL R1: BUILD AFTER a separate version bump is added and tap_dot reason drop is fixed · astra: METER · houses that ruled: 2 of 3 · claims that HOLD: 14 · blockers to build: 3 · owner items: 8 · ESCALATE: 1
