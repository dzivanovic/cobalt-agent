# F23 gate run preflight, 2026-10-26 08:12 ET

Read-only. Main tip `a5183949` (`git rev-parse --short=8 main`).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | read 1046, 1050 line 1 | MODEL · SEAT · SESSION present, one launch line each, same shape as precedent 970 (`permission-mode auto` in the launch line; no METER tag in 970, 1045, 1046 or 1050) | OK |
| 1b | read 1051 header vs `CARD.md` deploy column | JOB LADDER BRANCH WORKTREE BASE TIP REPORT RULINGS TAG MIGRATIONS SET TICKERS all present, plus WAITS as in 929; no `«FILL`, no placeholder token (`grep` empty). 1050 is a seat prompt, not a card: CLASS/LADDER/RULINGS as in 1046 | OK |
| 2a | read 1046 `## REPORT` | five `GATE RESULT` lines E1 E2 E4 E5 E6 at column 0 | OK |
| 2b | E1/E2 text | `NOT RUN — offline leg … passed; … render seat 1050, … [HIS HAND]`; desk writes `OK` after 1050 plus his opens (R2465) | OK |
| 2c | E4 text | `OK — settled offline` needs 3 parity tests, `date +%Z` EDT/EST, link `America/New_York`. Now: `/etc/localtime -> /var/db/timezone/zoneinfo/America/New_York` | OK |
| 2d | E5 text, `grep -n "uv sync" reports/deploy-f23-playbook.md` | lines 185, 197 carry `uv sync`; `DEPLOYED … 7398d4a7` at line 4 and 260; 1046 and 1051 E5 lines are identical | OK |
| 2e | E6 text | `RULED post-load watch`, weekday `cobalt jobs check` after load | OK |
| 3a | 1046 strings vs its allow line | all four `uv run pytest …` strings, `date`, `date +%Z`, `ls`, `grep`, `git -C … rev-parse` on the allow line; no `launchctl`, no `cobalt jobs`, no `git apply`/`cherry-pick`/`git mv`/`rm`/`revert` (grep hits are prohibitions only) | OK |
| 3b | 1050 strings vs its allow line | take and release lock, `db migrate --proof-only`, render (both), `mv` of `.f23-render/data/2026-10-25`, pytest `--basetemp`, `ls`, `grep`, `tail`, `date` all on the line. Lock via `ops/desk/take-devdb-lock.sh f23-playbook-1013 90` and `release-devdb-lock.sh` (both exist, `ops/desk/`); the release removes `.env` and the lock dir | OK |
| 3c | `mv` in 1050 step 3a | source and target both under `/Users/cobalt/cobalt-wt/.f23-render/data/`, a scratch output folder, not a tracked file. Confirmed: not the BUILD-HUB.md:14 ban | OK |
| 3d | `ls -d` of worktree and scratch | `/Users/cobalt/cobalt-wt/f23-playbook-1013` exists; `.f23-render` absent (step 0 passes); `ls -la /Users/cobalt/cobalt-wt/*/.env` has no stale file now | OK |
| 4 | spot-check of 20 cites on main | tests `test_playbook_offline.py` 273, 291, 373, 392, 412 ✓; `test_jobs.py` 88, 107, 658, 797 ✓; `test_playbook_registry.py:16` ✓; `watchdog.py:336` (due ≤ registered rule) ✓, `:441`, `:451-456` (`unregistered`) ✓; plist `:6`, `:20` (vault key), `:44` (RunAtLoad), `:46-49` (logs) ✓; `cli.py:573` `playbook_cli.add_parser(sub)` ✓; `playbook.yaml:12-13` 8 / 120 ✓; `gate-lists.md:56` `## LEVEL 0013` ✓; `bootstrap-owed.json:3` playbook gate E1 E2 E4 E5 E6 ✓ (file is gitignored, on disk, not on main); `779:21` `## LAUNCHD` ✓; `F23-FINAL` `:151` heading, E1 `:157`, E2 `:158`, E4 `:159`, E5 `:160`, E6 `:161` ✓; `DEPLOY-HUB.md:3` ✓, `:146` ✓; `deploy-step-c.sh:176`, `:185` ✓. One miss: see ISSUES (X3 `:336`) | OK |
| 5a | 1051 TAG | `deploy-2026-10-27-playbook-bootstrap`, a date; `git rev-parse --verify` finds no such tag; 929 shape; the desk re-dates it | OK |
| 5b | `--bootstrap-only` admits it | `## LAUNCHD` mode `add` (`:176`); build card `prompts/2026-10-13/503-f23-card.md:P6` matches the `-card.md:<row>` shape and exists; owed file lists the label; `ops/com.cobalt.playbook.plist` Label on main; every owed item E1 E2 E4 E5 E6 needs a non-empty column-0 line (`:185`): E5, E6 present, E1 E2 E4 the desk adds, so a refusal until then (CHECK ASKS X2) | OK |
| 5c | 1051 `jobs register` | not a string on the card; barred at `DEPLOY-HUB.md:3` | OK |
| 5d | 1051 smoke reads vs `deploy-smoke.sh:341-359` | both rows end `· prints 1`. The script reads only `exit 0, listed`, `` exit 0, `<v>` ``, `exit 0, a count of 1 or more`, `exit 0, one integer`, or a bare `` `<v>` ``; any other text is `RED … not one this script reads`. Both reads would go RED on a correct tree | FAIL |
| 5e | 1051 MARKERS row | `grep -c -F "com.cobalt.playbook" …/bootstrap-owed.json` · before `1` · after `0`; today it counts 1 (line 3 only) | OK |
| 5f | the single `unregistered` beat | in RECORDS (THE UNREGISTERED BEAT) and CHECK ASKS X3 ("EXPECTED, NOT A RED SMOKE") | OK |
| 6a | 1050 class and scratch | `CLASS: K2`; scratch `/Users/cobalt/cobalt-wt/.f23-render/data` (render `--out`) | OK |
| 6b | 1050 lock | step 1 takes, step 4 releases always, records `ls …/f23-playbook-1013/.env` "No such file"; SECOND PASS repeats lock, proof, render, release | OK |
| 6c | 1050 SECOND PASS | a rerun of step 2's render the desk launches on `CONTINUE` after his open | OK |
| 7a | R2465 F23 line, 1051 `## RECORDS` | present, equal to the drafter's `REVISION (brain R2465)` line (`draft-f23-gate-run-2026-10-26.md:35`) | OK |
| 7b | R2463 | the row (`cto-2026-10-26.md:18`) is F4 only; it has no F23 content, so nothing to carry | OK |
| 7c | R2467 line | verbatim in 1046 `## RECORDS` and 1050 `## RECORDS` (matches the drafter's line `:46`) | OK |
| 8 | `ls prompts/2026-10-26/` | `1050-f23-render-seat.md` and `1050-f4-gate-run-preflight.md` both present | NOTE |

## ISSUES
- 1051 FAIL: `## SMOKE READS` (both rows) ends `· prints 1`, which `deploy-smoke.sh` does not read, so both reads go RED. Use `exit 0, a count of 1 or more` or ``exit 0, `1` `` (as 1048 and 929 do). This blocks the deploy; the gate run and the render seat are not blocked.
- 1051 NOTE: CHECK ASKS X3 cites `watchdog.py:336` for the text `never run yet (registered, not yet due)`; that text is at `:530`, and `:336` is the rule (a never-run job whose due moment precedes registration is not missed). The cite and the claim agree in substance; correct the line number.
- 1051 NOTE: the R2465 RECORDS line is the drafter's wording, not byte-equal to the R2465 row in `cto-2026-10-26.md:17` (the row reads "launched only on X15 FAIL … by a K2 seat, his open legs"). Same facts. Say so if the check wants the row verbatim.
- 1046, 1050 NOTE: no METER tag, as in precedent 970 and 1045. No fail.
- 1050 NOTE: the file numbered 1050 also exists as `1050-f4-gate-run-preflight.md`; the desk renumbers the render seat at launch, and its launch line names its own path (drafter `REVISION (brain R2467)`). The desk must also change the path in 1046 line 1 `CARD:` and the 1050 references in 1051 and the 1046 report text.
- 1051 NOTE: `data/deploy/bootstrap-owed.json` is gitignored and absent from main, present on disk (3 items check out); the `--bootstrap-only` read uses the disk file.
- BLOCKS THE LAUNCH: 1051 only (smoke wording). 1046 and 1050 may launch now.

PREFLIGHT DONE · cards: 1046 1050 1051 · checks: 27 · fails: 1 · ready: NO
