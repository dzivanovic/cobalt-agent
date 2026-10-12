BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Mon Oct 12 18:16:50 EDT 2026

## DIGEST FOR THE DESK
- SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW
- C1 Sonnet LOW (366) BELOW — opus-own 4 vs 1, extra 3; three are missing tests, one repeats the original's own defect. SELF: yes (apart)
- C2 Sonnet MID (369) CLOSE BELOW — opus-own 3 vs 2, extra 1; all weak-test findings, three distinct. SELF: yes (apart)
- C3 Sonnet HIGH (372) CLOSE BELOW — opus-own 3 vs 2, extra 1; first-run reds were its own, both cleared within 2 re-passes. SELF: yes (apart)
- C4 Terra LOW (367) CLOSE BELOW — opus-own 2 vs 1, extra 1; O1 repeats the original's defect, O2 = Grok G1. SELF: no
- C5 Terra MID (370) AT LEVEL — opus-own 2 vs 2, extra 0; the 4 house-held findings count for nothing (SHADOW-HUB :78). SELF: no
- C6 Terra HIGH (373) BELOW — opus-own 13 vs 2, extra 11; its own with-DB red stayed red after both re-passes. SELF: no
- Experiments: X1 (C1: are the original's tests just as weak, so the gap is the check seat's strictness?), X2 (same on C2–C4).
- Owner: none.
- WITHDRAWN: 1 · ESCALATE: 1 (check seats differ in strictness; only X1/X2 can settle it; the grades stand as written).

## Grades
Paths are relative to `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/` unless stated. Baseline (the original's Opus-own held count): LOW 1, MID 2, HIGH 2. I re-derived each one below.

**C1 Sonnet LOW (366) — BELOW** · STAKE: yes — Sonnet is my own vendor's model, and the baseline is my own model's work · SELF: yes (recorded apart, counts on no cell)
- Shadow opus-own held: 4 — `strike-fallback-env-1010-sonnet-check-2026-10-11.md:277` (`held: 4 (opus-own 4 · house 0)`), findings O1–O4 at :100–168.
- Original opus-own held: 1 — `strike-fallback-env-check-2026-10-10.md:223` (`held: 1`, house A Sol's A1 rejected :5), O1 at :101–119.
- Extra = 4 − 1 = 3 → two or more → BELOW.
- Distinct defects: O1 (override unpinned, :102), O2 (60 s boundary unpinned, :126) and O3 (second-streak reset unpinned, :139) are three separate missing tests. O4 (:156) is the SAME defect as the original's O1 (unprintable exception escapes `step()`, original :103). The original's build had the same defect, so O4 cancels against the baseline and the 3 extra are all missing tests.
- No first-run red is recorded for 366: the table row (`complexity-shadow-results-2026-10-11.md:18`) names none, while it does name one for 372 and 373. The check gate on the tip is green (:6). I did not read the build's stop line itself: UNVERIFIED — `tail -n 1` of the 366 build report.

**C2 Sonnet MID (369) — CLOSE BELOW** · STAKE: yes — Sonnet is my own vendor's model, and the baseline is my own model's work · SELF: yes (recorded apart)
- Shadow opus-own held: 3 — `radar-display-fix-1008-sonnet-check-2026-10-11.md:281` (`held: 3 (opus-own 3 · house 0)`), O1–O3 at :109–156.
- Original opus-own held: 2 — `radar-display-fix-check-2026-10-08.md:4` (held 3 = O1, O2 Opus + A3 Sol; table :143–148), :246 `held: 3`.
- Extra = 3 − 2 = 1 → CLOSE BELOW.
- Distinct defects: O1 (stale line can leave the `try`, :111), O2 (`since <time>` unpinned, :132) and O3 (unconditional TERMINAL restore, :146) are three distinct weak tests; O1 and O2 sit on one test but use different mutations. O4 is the original's O3 (rejected there too; original :126, shadow :160). It was REJECTED and is not counted.
- No first-run red is recorded for 369 in the table (:18). Build stop line not read: UNVERIFIED — `tail -n 1` of the 369 build report.

**C3 Sonnet HIGH (372) — CLOSE BELOW** · STAKE: yes — Sonnet is my own vendor's model, and the baseline is my own model's work · SELF: yes (recorded apart)
- Shadow opus-own held: 3 — `s4-p1-1009-sonnet-check-2026-10-11.md:299` (`held: 8 (opus-own 3 · house 5)`), O1–O3 at :116–185.
- Original opus-own held: 2 — `s4-p1-check-2026-10-09.md:4` ("4 held … 2 defects … each found by Opus and by Sol": O1, O3), :279 `held: 4`.
- Extra = 3 − 2 = 1 → CLOSE BELOW.
- Distinct defects: O1 (same-day overwrite, :118), O2 (`seen_at` = tick start, :139) and O3 (unbounded `join`, :166) are distinct. O2 is the SAME defect as the original's O3 (original :107). House H3 = O2 (:5) is a house finding and counts for nothing.
- Red at first run: the model's own. Two reds, each fixed by one re-pass (2 of 2 used): `/Users/cobalt/cobalt-wt/s4-p1-1009-sonnet/docs/40 - DevDocs/reports/s4-p1-1009-sonnet-build-2026-10-11.md:7`, :157 (offline, "the model's own red"), :181 (with-DB `:163`). It was GREEN after pass S2 2 (:204, `197 passed`). A red only makes BELOW when it is still red after 2 re-passes (SHADOW-HUB :37, :78), so BELOW does not apply.

**C4 Terra LOW (367) — CLOSE BELOW** · STAKE: yes — the baseline is my own model's work · SELF: no
- Shadow opus-own held: 2 — `strike-fallback-env-1010-terra-check-2026-10-11.md:193` (`held: 3 (opus-own 2 · house 1)`), O1 :64–82, O2 :84–88.
- Original opus-own held: 1 (as C1).
- Extra = 2 − 1 = 1 → CLOSE BELOW.
- Distinct defects: O1 (:66) is the SAME defect as the original's O1 (and as C1's O4). It cancels against the baseline. O2 (+30 s half asserts only the last record, :86) is the same finding as house G1 (:5 "O2 = G1"). G1 is a house finding and counts for nothing, so one extra remains.
- No red at first run (`suites at first run: green`, :30).

**C5 Terra MID (370) — AT LEVEL** · STAKE: yes — the baseline is my own model's work · SELF: no
- Shadow opus-own held: 2 — `radar-display-fix-1008-terra-check-2026-10-11.md:223` (`held: 6 (opus-own 2 · house 4)`), O1 :97–109, O2 :111–121.
- Original opus-own held: 2 (as C2).
- Extra = 2 − 2 = 0 → AT LEVEL.
- Distinct defects: O1 (`owned` single write unpinned, :99) and O2 (a JS comment satisfies 3 tests, :113) are distinct. House A1 and A2 share O2's root cause (:5) and A3 and A4 are separate, but all four are house findings and count for nothing (SHADOW-HUB :78).
- No first-run red is recorded for 370 in the table (:19). Build stop line not read: UNVERIFIED — `tail -n 1` of the 370 build report.

**C6 Terra HIGH (373) — BELOW** · STAKE: yes — the baseline is my own model's work · SELF: no
- Shadow opus-own held: 13 — `s4-p1-1009-terra-check-2026-10-11.md:355` (`held: 25 (opus-own 13 · house 12)`), runs O1–O13 :272–284, all HELD.
- Original opus-own held: 2 (as C3).
- Extra = 13 − 2 = 11 → BELOW.
- Distinct defects: the check folds the 25 into 11 (:324–335). Among the opus-own, O6 and O13 are one fold (M1 refusal / literal 50, :329) and O3 and O4 are one (C3 MISSED, :327). O12 is SCOPE (:335). Counting only distinct, non-SCOPE opus-own defects still gives ≥9 against 2. BELOW either way.
- Red at first run: the model's own, still red after both re-passes. The build's with-DB stayed 4959/1 (`/Users/cobalt/cobalt-wt/s4-p1-1009-terra/docs/40 - DevDocs/reports/s4-p1-1009-terra-build-2026-10-11.md:212`). Its gate seat rules out the harness (:178: lock taken at once, level 0013, `.env` present). The check reproduces the red under a taken lock at level 0013, F2 = F0 (check :275). So it is not INCOMPLETE (SHADOW-HUB :38), and it is BELOW on this ground alone (SHADOW-HUB :78).

**(a) THE FACT BASE** (table rows Sonnet and Terra, `complexity-shadow-results-2026-10-11.md:18–19`)
| cell | figure | verdict |
|---|---|---|
| 366 | tip `813036e8` · held 4/0 (opus-own 4) · open 0 · offline 4196/0 · with-DB 5093/0 | HOLDS — sonnet LOW check :277 |
| 369 | tip `c289f478` (gate on `c5795c7b`) · held 3/0 · open 5 · 4000/0 · 4884/0 | HOLDS — sonnet MID check :4, :5, :281 |
| 372 | tip `51fe6947` · held 8 (3/5) · open 11 · first run red · 4159/0 · 5048/0 · passes 4 | HOLDS — sonnet HIGH check :47, :299 |
| 367 | tip `d02370df` · held 3 (2/1) · open 4 · 4195/0 · 5092/0 · passes 4 | HOLDS — terra LOW check :30, :193 |
| 370 | tip `e544d94f` · held 6 (2/4) · open 6 · 4000/0 · 4884/0 | HOLDS — terra MID check :223 |
| 373 | tip `9e3a133b` (gate on `aad18813`) · held 25 (13/12) · open 0 · build 4071/0, 4959/1 · check 4071/15, 895/1 · first run red · passes 4 | HOLDS — terra HIGH check :6, :355; build report :212 |
Not settled from what I read: builder tokens and wall for all six. I read the build stop lines only for 372 (check :47), 367 (check :30) and 373 (build :212), and those three match the table. 366, 369 and 370 tokens/wall: UNVERIFIED — `tail -n 1` of each build report under `/Users/cobalt/cobalt-wt/<job>/`.

EXPERIMENTS: see `## Experiments (L70)`.
OWNER (after the sitting): none — see `## OWNER`.
WRONG FACTS: none — see `## WRONG FACTS`.

SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW

## Self-attack
One `grep -rl --exclude="results-sitting*"` per counted finding over `reports/`. I listed file names with `-l`, and the exclude keeps the blind. These finding ids are the checks' own:
| cell · finding | search | other files that hold it | verdict |
|---|---|---|---|
| C1 O1 | `override=True` | none besides the 366 check | distinct |
| C1 O2 | `exactly 60 s` | none | distinct |
| C1 O3 | `second streak` | none | distinct |
| C1 O4 / C4 O1 | `Unprintable` | original `strike-fallback-env-check-2026-10-10.md`, terra LOW check | SAME defect as the original's O1. It cancels against the baseline in both cells, as written above |
| C2 O1 | `stale_line_leaves_the_try` | none | distinct (the original's O1 is a different mutation: banner out of the guard, original :98) |
| C2 O2 | `since_time_is_dropped` | none | distinct |
| C2 O3 | `restore_is_unconditional` | none | distinct |
| C3 O1 | `second_run_on_the_same_et_date` | none | distinct |
| C3 O2 | `seen_at_is_the_polls_wall_clock` | original `s4-p1-check-2026-10-09.md` | SAME defect as the original's O3. It is counted in both, as written |
| C3 O3 | `blocked strike tick` | none | distinct |
| C4 O2 | `_messages(records)[-1]` (-F) | none besides the 367 check | distinct (= house G1 in the same file) |
| C5 O1 | `a_second_write_to_owned` | none | distinct |
| C5 O2 | `names_its_fetch_once_outside_a_comment` | none | distinct |
| C6 O1 | `unreadable_radar_plan` | none | distinct |
| C6 O2 | `TradeDefStore` | older build/draft reports (setups 09-21/22, drc 09-28, s2-p4 09-18) | those name the class, not this defect; distinct |
| C6 O3 | `bars_source` | none | distinct |
| C6 O4 | `test_watch_cross_persists_missed_with_reason` | none | distinct (one fold with O3, :327) |
| C6 O5 | `sleeps the floor` | none | distinct (related to the original's O1 C4-interval defect but a different fault: floor vs interval+tick) |
| C6 O6 | `five_names_at_three_seconds_names_the_minimum` | none | distinct |
| C6 O7 | `Charter re-rule` | none | distinct |
| C6 O8 | `first_poll_that_sees_a_bar` | none | distinct |
| C6 O9 | `default_clock_stops_polls_outside_the_windows` | none | distinct |
| C6 O10 | `acceptance_time_is_held_not_two_bars` | none | distinct |
| C6 O11 | `_touches_entry` | original check, preflight, build 10-09, sonnet HIGH check | those cite the replay function; only the terra check holds the second-copy defect |
| C6 O12 | `test_setups_registries.py` | original check, sonnet HIGH check, and many older reports | the SAME scope edit was REJECTED by the sonnet HIGH check (H7, :212, :270) but HELD by the terra check (:283). Without O12, extra = 10, still BELOW |
| C6 O13 | `radar_rpm + demand > 50` (-F) | none | distinct (one fold with O6, :329) |
The first 13 searches ran unquoted and zsh refused them with `no matches found` before grep started. They read nothing, and I re-ran them quoted.
WITHDRAWN: "No red at first run (the build's stop line counts only the check's tip; the check gate is green, :6)." (C1) — I read no 366 build stop line. The only sources for this are `complexity-shadow-results-2026-10-11.md:18` and the check's §0 (:6), and neither says how the stop line counts. Replaced by the UNVERIFIED line now under C1. The same bare "No red at first run" under C2 and C5 is narrowed the same way.

## Experiments (L70)
- X1: in a scratch worktree on the original LOW build tip `f47ad2f0` (card 365's original), run the 366 check's O1–O3 tests and their mutations (`override=True` at `__main__`, `>=`→`>` at the repeat line, delete the `_last_error = None` line). If the original's own tests also stay green under those mutations, the original has the same three gaps. Its check simply did not look, and C1's extra 3 would be the check seat's strictness, not the model. Re-graded on comparable strictness, C1 would move to AT LEVEL.
- X2: the same on the MID original `eb14f860` (C2's O3 unconditional-restore mutation, C5's O1 second-write mutation) and the HIGH original `444e32b5` (C3's O1 same-day overwrite test). Any of them failing on the original moves that cell's extra down by one: C2 → AT LEVEL, C3 → AT LEVEL. C6 does not change, because 11 − 3 is still ≥2.

## OWNER (after the sitting)
none — the six grades come from a counting rule the houses can apply. The routing word on the result is his already (R1014/L29), and nothing here touches his money, data, laws or trading judgement.

## WRONG FACTS
none — every Sonnet and Terra figure I checked in `complexity-shadow-results-2026-10-11.md:18–19` matches the check files (table in (a)). The baseline 1 / 2 / 2 (`complexity-shadow-results-2026-10-11.md:9`; `bakeoff-results-stage-answer-2026-10-11.md:35`) matches the originals (`strike-fallback-env-check-2026-10-10.md:223`; `radar-display-fix-check-2026-10-08.md:4`; `s4-p1-check-2026-10-09.md:4`).
The Grok rows are UNSCORED (`complexity-shadow-results-2026-10-11.md:17`; `bakeoff-results-stage-answer-2026-10-11.md:8, :19–20`). I opened the two Grok checks only to read their CHECK DONE lines (`radar-display-fix-1008-grok-check-2026-10-11.md:254`, `archiver-429-grok-check-2026-10-11.md:381`) and graded nothing there.

## READING
- `428-results-sitting-opus-seat.md` whole; `271-model-tribunal-opus-seat.md` (grep of AUTHORIZATION / PATTERN RULE / (ii) / RECOVERY, lines 18, 20, 22).
- Authorization: `grep -c -x -F "FABLE ROW: R__"` 428 → 0 · `grep -n R109 cto-2026-09-22.md` → :56 carries "Make all Opus 5.5 for now" and `claude-opus-5-5` · `git log -S"R109"` → `6f4da5e99a585d97b9d09528ebfd58cdc86644a4` · `cto-2026-10-12.md:7` R1270 `Fable seat: yes` · `git log -S"427-results-sitting-tribunal.md"` → `9a1083ada774b65ecf3d1d2be54a0e5567810249` · `cto-2026-10-11.md:74` R1069 "tribunal seats approved" · `tail -n 3` table → `TABLE DONE · rows: 11 · unknown: 21` · seven allow and three deny strings each counted 1 in 271 · my model id `claude-opus-5-5` = R109's.
- `LAWS.md` :1–93, :130–141, :204–239, :339–406.
- `complexity-shadow-results-2026-10-11.md` whole; `bakeoff-results-stage-answer-2026-10-11.md` whole; `SHADOW-HUB.md` :37–38, :72–103.
- `427-results-sitting-tribunal.md`: line grep of `01-QUESTIONS.md (verbatim)` / `SITTING:`; :30–32 (the question set). I did not open its §1 staging list.
- Heading greps on all nine check files. Ranges opened: sonnet LOW :3–8, :97–181 (CHECK DONE :277); terra LOW :3–96 (CHECK DONE :193); sonnet MID :3–8, :106–174 (:281); terra MID :3–7, :94–131 (:223); sonnet HIGH :3–7, :113–197 (:299) + grep `first run`/`re-pass`; terra HIGH :3–8, :36–266, :270–309, :323–336 (:355); original LOW :3–7, :98–130 (:223); original MID :3–7, :93–149 (:246); original HIGH :3–8, :71–146 (:279).
- Build reports (grep only): `s4-p1-1009-sonnet-build-2026-10-11.md` (`first run` / `pass S2` / `red`), `s4-p1-1009-terra-build-2026-10-11.md` (`first run` / `Pass S2` / `harness`).
- Grep of H7/A5/B4 in the HIGH original and sonnet HIGH checks; grep `score`/CHECK DONE in the two Grok checks; the self-attack greps above (13 that zsh refused and that never ran, then 27 that ran, one with `-F` re-run).
- I never opened `scratch/tribunal-bars-0920/results-sitting/`, `reports/results-sitting-2026-10-12.md`, any house file, his notes, `Rules.md` or any vault file outside LAWS.md.

## L74
This session's harness sent attribution reminders asking for a `Claude-Session:` line in commits and PR bodies, and naming a file-send tool. Recorded once here as data. I did not act on it: this seat makes no commit and sends no file.

## ESCALATE
1. CHECK-SEAT STRICTNESS (for the hub and desk, not him): the grading rule counts Opus-own held findings, but the check seats were not equally strict. The 366 check's mutation-driven missing-test findings (O1–O3) have no counterpart search in the LOW original's check. The same setups SCOPE edit was rejected in 372 (sonnet HIGH check :212) and held in 373 (terra HIGH check :283). Unproven as a defect (L70) until X1/X2 run. Safe default: the grades stand as written by the rule, and nothing routes by this sitting (L29).

## CONTINUE
next: none — done. MEASURE: this seat cannot read its own token meter (UNVERIFIED).

RESULTS SITTING OPUS DONE · SITTING: C1 BELOW · C2 CLOSE BELOW · C3 CLOSE BELOW · C4 CLOSE BELOW · C5 AT LEVEL · C6 BELOW · apart: C1 C2 C3 · withdrawn: 1 · ESCALATE: 1
