# Card 641 `check-scratch-1016` — fix round FR-1 / FR-2, preflight round 3

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>`; `git log --oneline -4 -- <card>` | diff empty; last commit `1edaae19` (amend2); committed | OK |
| 2 | `git diff -U0 7c3633cd HEAD -- <card>` (round 2's card) | touches only two lines: the FR-1 row (CONTROLS text) and FIX ROUND ORDER. Nothing else | OK |
| 3 | FAIL closed, part 1: FIX ROUND ORDER (read) | says `2 failed`, names `test_fr1_a_build_card_read_copy_does_not_block_the_clear` and `test_fr1_control_this_jobs_own_check_folder_shape`, both `assert done.returncode == 0` on `more than one prior card copy`; `test_fr1_control_two_same_job_check_cards_are_refused` named GREEN | OK |
| 4 | part 2: FR-1 row CONTROLS (read) | (i) two-same-job: GREEN on the tip and after; (ii) own-check-folder: RED on the tip (clear half, `more than one prior card copy`), GREEN after, refuse half GREEN on both | OK |
| 5 | part 3: `grep -n -o -E ".{60}(1 failed\|2 failed).{60}"` on the card | `1 failed` stays only at: CS-1 RED `:29`, FR-1 `fr1_a` run alone `:31` (correct: 1 red when that test runs alone, on the tip), FR-2 mutation `:32`, old CS-1 `ORDER:` `:34`, FR-2 mutation in FIX ROUND ORDER `:36`. `2 failed` at `:36` once. No place says `1 failed` for the whole-file FR-1 run | OK |
| 6 | part 4: `grep -n -o -E ".{50}GREEN on the tip.{50}"` on the card | one hit, `:31`, control (i) only. No place calls (ii) GREEN on the tip | OK |
| 7 | `grep -c -E "FILL\|TODO\|TBD\|XXX\|«"` on the card | `0` | OK |
| 8 | `git diff --stat 85eade55 ops/check-scratch-1016 -- ops tests` | prints nothing: the branch's `ops/` and `tests/` equal the tip | OK |
| 9 | `git rev-parse --short=8 85eade55` | `85eade55` | OK |
| 10 | amend2 record (`draft-641-fixround-amend2-2026-10-16.md`) vs the diff of check 2 | it claims two places, card only, 0 decisions; the diff is those two places | OK |
| 11 | sample 1: `grep -n` on `stage-set.sh` (branch, equal to tip): `clearable() {`, `copied=""` | `:92`, `:108` | OK |
| 12 | sample 2: the `find … -name '*-card.md'` line, `no prior card copy`, `more than one prior` | `:109`, `:110`, `:111` (card says `:108-111`) | OK |
| 13 | sample 3: `--find-object` line; `field JOB` | `:113`; `:115` is `field JOB "$copied"` (`:95` is `name=$(field JOB)`) | OK |
| 14 | sample 4: `rm -rf` lines | `:151` (`fail`), `:158` (clear): two | OK |
| 15 | sample 5: header words "its one files/*-card.md a version of a card" | `:8` | OK |
| 16 | sample 6: `tests/ops/test_stage_set.py` (branch): `job` fixture, `:78` string, `prior_staging`, `CHECK REPORT:` insert, `snapshot`, `fr_card`, `test_cs1_a_`, `test_c12_`, `_copy_*`, `refused_untouched` | `:51-52`, `:78` (`"TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n\| row \| what \|\n"`), `:193`, `:202`, `:225`, `:344`, `:359`, `:330`, `:379`/`:384`, `:404`; no `HOUSE A` anywhere in the file | OK |
| 17 | sample 7: headers of 641, 638, 583 (`grep -n -E "^(CHECK REPORT\|HOUSE A\|JOB):"`) | 641 and 583: `CHECK REPORT:` `:10`, no `HOUSE A:`; 638: `CHECK REPORT:` `:10`, `HOUSE A: grok` `:11` | OK |
| 18 | sample 8: build report M5 line (`grep -n -F "Another-job"`, branch worktree) | `:150`, holds `Another-job: M5` | OK |
| 19 | FIXTURE LINE and fixture/`prior_staging` (reread, unchanged since r2's checks 3-8) | `:75-79` span, new string at `:78`; `prior_staging` inserts `CHECK REPORT:` before `TREE STATE:` so `HOUSE A: grok` stays in every card; no assertion changes | OK |
| 20 | CS-1 controls and FR-2 under the FR-1 rule (reread against `git show 85eade55:ops/desk/stage-set.sh`) | unchanged from r2 check 12: all still refuse, FR-2's test reaches `:115` alone via the fallback | OK |
| 21 | `git show 85eade55:ops/desk/stage-set.sh` whole | `clearable()` `:92-122`, gate `:124-131` as the card cites | OK |
| 22 | what blocks `desk-launch.sh build "<card>" "FIX ROUND row FR-1"` (not run) | nothing in the card: committed (diff vs HEAD empty), BASE `b84cca9a` set, TIP empty by design, no FILL marker. `main` also holds the desk's uncommitted `.claude/settings.json` (not mine, not read) | NOTE |

## ISSUES
- NOTE: the CS-1 row ("no existing test edited") and the old `ORDER:` paragraph (`1 failed`) stand as history; FR rows win (stated in `## CONTINUE FIX ROUND`). No change needed.
- NOTE: the FR-1 test cell's `1 failed` is for `fr1_a` run alone; it matches the whole-file `2 failed` (fr1_a plus the own-check-folder control).
- NOTE: I ran no test, no launcher and no mutation; every RED is read from the code and UNPROVEN until the builder quotes it (L70).

PREFLIGHT DONE · card: check-scratch-1016-fixround · checks: 22 · fails: 0 · ready: YES
