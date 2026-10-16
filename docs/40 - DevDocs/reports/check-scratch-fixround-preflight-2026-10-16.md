# Card 641 `check-scratch-1016` — fix round FR-1 / FR-2 preflight

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>`; `git log --oneline -- <card>` | diff empty; last commit `13cd5919` (FR-1/FR-2 drafted); committed | OK |
| 2 | `git diff -U0 61dbb578 HEAD -- <card>` (round-2 preflight base) | 14 insertions, 2 deletions: `## CONTINUE FIX ROUND`, rows FR-1 and FR-2, FIX ROUND ORDER, NOT-IN-THIS-JOB bullet 2 (replaced), READ lines, X5 and X6, one RECORDS line. CS-1 and R2 untouched | OK |
| 3 | FR-1 against the direction (R1706/R1709): `HOUSE A:` beside `CHECK REPORT:`, JOB = `$name`, exactly one clears, zero or 2+ refuse, build-card READ copies ignored, `:115` fallback for one other-JOB check card, controls (i) and (ii) | all present in the FR-1 row | OK |
| 4 | FR-2 against the direction: test pins `:115` alone (sole other-JOB copy that passes `:113-114`), mutation `:115` removed alone → `1 failed`, M5 line corrected | present; the mutation is rerun after FR-1 | OK |
| 5 | FR-1 against FR-2 and the CS-1 rows: the fallback hands the lone other-JOB card to `:115`, so FR-2's test stays red for `:115` alone | consistent; "the FR row wins" is stated | OK |
| 6 | FR-1 against the existing tests: `grep -n "HOUSE A" tests/ops/test_stage_set.py` (branch worktree) | no output. The `job` fixture card (`:74-79`) and `prior_staging` (`:193-222`) never write `HOUSE A:`. Every existing test that clears (`test_c1_` `:240`, `test_c2_c9_` `:288`, `:303`, `:321`, and all seven `test_cs1_` incl. `test_cs1_a_` `:359`) stages a prior copy with no `HOUSE A:`. Under FR-1 that copy is not a check card: zero cards, so `no prior card copy`. The card says "no existing test edited" and "then the same command → `0 failed`" | FAIL |
| 7 | file:line on the tip (`85eade55`, the branch is `0605334f` = docs on top; `grep -n` on the branch worktree): `clearable() {` | `:92` | OK |
| 8 | same: `copied=` / `find … -name '*-card.md'` / `no prior card copy` / `more than one prior` | `:108` / `:109` / `:110` / `:111` | OK |
| 9 | same: `--find-object` / `field JOB "$copied"` / `prior=$(field` | `:113` (with `:114` the miss) / `:115` / `:116` | OK |
| 10 | same: header words "its one files/*-card.md a version of a card on main" | `:8` | OK |
| 11 | same: `rm -rf` | `:151` (`fail`), `:158` (clear); two lines, as the card says | OK |
| 12 | `grep -n "^def " tests/ops/test_stage_set.py` (branch): `_copy_of_another_job`, `_copy_no_prompts_card`, `refused_untouched`, seven `test_cs1_` | `:379`, `:384`, `:404`, `:359` + `:419-439` | OK |
| 13 | headers: `grep -n -E "^(CHECK REPORT\|HOUSE A\|JOB):"` on 633, 638, 583 | 633 and 638: `HOUSE A:` on line 11 beside `CHECK REPORT:` on line 10; 583: `CHECK REPORT:` line 10, no `HOUSE A:`. 641 header (read): `CHECK REPORT:` line 10, no `HOUSE A:` | OK |
| 14 | build report line `:150` (branch worktree) | holds `(1) Every added …` and the words "Another-job: M5" | OK |
| 15 | rows in ROWS / ORDER / CHECK ASKS and the launch note | FR-1, FR-2 in ROWS; FIX ROUND ORDER names both; X5, X6 in CHECK ASKS; launch note: "`build` at `FIX ROUND row FR-1`" (twice) | OK |
| 16 | `grep -n -F "«" / TODO / TBD / XXX` on the card | no output (BASE `b84cca9a` filled; TIP empty by design) | OK |
| 17 | `git rev-parse --short=8 85eade55`; `ops/check-scratch-1016` | `85eade55`; `0605334f` (the card says so) | OK |
| 18 | `ls`/read of FR-1 test shape: the first card committed with `HOUSE A: grok` before `prior_staging(change=False)` | workable: `prior_staging` commits the card file as it stands, and `fr_card` copies its text. It works only for that test | OK |

## ISSUES
- FAIL (check 6): FR-1 makes `HOUSE A:` a must for the prior copy, but the shared `job` fixture and `prior_staging` write no `HOUSE A:`. After the `clearable()` edit all existing clear tests (`test_c1_`, `test_c2_c9_` ×8, `test_c10_`–`test_c12_`, `test_cs1_a_` and the controls that need a clear) go red or pass for the wrong reason, which contradicts "no existing test edited" and "the same command → `0 failed`". `test_cs1_control_a_prior_copy_of_another_job_is_refused` and the no-prompts control still refuse, but at "no prior card copy" and never reach `:113-115`. Fix (drafter): either allow `prior_staging`/`job` to carry `HOUSE A: grok` (name that one edit of existing test code, and the ORDER's "1 failed" then changes), or move the `HOUSE A:` line into the fixture card by an appended helper that the FR tests use while the old tests are re-pointed. The brain's call: the discriminator or the test rule.
- NOTE: the FR-1 test (`prior_staging` then drop a READ copy) is written to be red on the tip with "more than one prior card copy"; true on the tip code (`:111`).
- NOTE: what blocks `desk-launch.sh build "<card>" "FIX ROUND row FR-1"`: the card (committed, no «FILL, BASE set) and the worktree look launchable. I did not run the launcher. The real blocker is the FAIL above: a builder who follows the card cannot reach `0 failed` without editing existing tests. The desk's `.claude/settings.json` is modified (not mine, not read).

PREFLIGHT DONE · card: check-scratch-1016-fixround · checks: 18 · fails: 1 · ready: NO
