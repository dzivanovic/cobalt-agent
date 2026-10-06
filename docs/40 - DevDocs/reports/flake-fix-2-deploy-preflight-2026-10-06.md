# flake-fix-2 deploy card — preflight (2026-10-06)

Card: `prompts/2026-10-06/31-deploy-flake-fix-2-card.md`. Read-only; every check run, output quoted.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git rev-parse --verify 1a52ad0d^{commit}` | `1a52ad0d7eb613845968c195f2d086331318384b` | OK |
| 2 | `git log --oneline -1 ops/flake-fix-2-1006` | `1a52ad0d fix(flake-fix-2): XL76 harness opens through open_migrated inside its try ...` | OK |
| 3 | `git merge-base --is-ancestor 1a52ad0d ops/flake-fix-2-1006` | exit 0, no output | OK |
| 4 | check report last line | `CHECK DONE · job: flake-fix-2 · pass: 1 · tip: 1a52ad0d ... held unfixed: 0 ... RESTARTS: none ... ready: YES` | OK |
| 5 | `git log -1 --format=%h -- <check report>` | `dd16e87d` (committed) | OK |
| 6 | `rev-parse --verify deploy/deploy-flake-fix-2-1006` (BRANCH) | `fatal: Needed a single revision` (absent) | OK |
| 7 | `rev-parse --verify deploy-2026-10-06-flake-fix-2` (TAG) | `fatal: Needed a single revision` (absent) | OK |
| 8 | `ls /Users/cobalt/cobalt-wt/deploy-flake-fix-2-1006` (WORKTREE) | `No such file or directory` | OK |
| 9 | `ls <reports>/deploy-deploy-flake-fix-2-1006.md` (REPORT) | `No such file or directory` | OK |
| 10 | `grep -n "^\| (R326\|R412\|R474) "` in cto-2026-10-03 / 10-05 | R326 (10-03:332) `HIS RULING · APPROVED`; R412 (10-05:109) `HIS RULING ... APPROVED`; R474 (10-05:140) `HIS RULING · APPROVED` | OK |
| 11 | `git diff --stat -- cto-2026-10-03.md cto-2026-10-05.md`; `git log -1 --format=%h -- both` | diff empty; `1f4a8598` (committed) | OK |
| 12 | `git diff --stat main...ops/flake-fix-2-1006` | 15 files, 442 insertions, 101 deletions; the 15 paths equal the card's SHIPS list (12 tests, 2 DevDocs, 1 build report) | OK |
| 13 | `git diff --stat main...ops/flake-fix-2-1006 -- src ops/desk tests/cobalt/conftest.py` | empty (RESTARTS: none holds; check says `RESTARTS: none`) | OK |
| 14 | BEFORE `ls tests/cobalt/migration_retry.py` on main | `No such file or directory` (exit 1) | OK |
| 15 | BEFORE `grep -c -F open_migrated` on the 10 files on main | all 10 `0` | OK |
| 16 | BEFORE `grep -c -F "migration retry" test_drc_store.py` | `8` | OK |
| 17 | BEFORE `def test_the_migration_step_retries_a_first_deadlock` on main | `0` (git grep, no match) | OK |
| 18 | BEFORE `grep -c -F flake-fix-2` cli.md / store.md | `0` / `0` | OK |
| 19 | AFTER `git grep -c -F open_migrated 1a52ad0d` | drc_store 3, radar_migrated_support 2, radar_score_migration 3, p4_migrations 4, voice_store 3, archiver_migrations 4, stale_score_db 2, tenancy 3, radar_handicap_store 2, xl76 harness 2 — each equals the card | OK |
| 20 | AFTER `def open_migrated(apply, paths)` in migration_retry.py | `1` | OK |
| 21 | AFTER `migration retry` in test_drc_store.py | `7` | OK |
| 22 | AFTER `def test_the_migration_step_retries_a_first_deadlock` | `1` | OK |
| 23 | AFTER `def test_first_deadlock_retries_once_on_a_fresh_connection` in test_migration_retry.py | `1` | OK |
| 24 | AFTER `def test_xl76_reports_false_when_the_migration_step_fails` | `1` | OK |
| 25 | AFTER `flake-fix-2` cli.md / store.md | `2` / `1` | OK |
| 26 | SMOKE READS (4): the counts of #20, #22, #19 (xl76 = 2), #24 | all exit 0, each ≥ 1 | OK |
| 27 | `grep -c -F "«FILL" <card>` | `0` | OK |
| 28 | card shape vs `prompts/CARD.md` and `desk-launch.sh` deploy case (line 919-959): header JOB/LADDER/BRANCH/WORKTREE/BASE/TIP/REPORT/RULINGS/TAG/MIGRATIONS/SET present; sections SHIPS, MARKERS, SMOKE READS present; BASE `main`; REPORT matches `deploy-*.md`; TAG plain; TIP 8-hex and a commit; `SET: none` is only required to be non-empty (`need ... SET`), not rejected; MIGRATIONS `none` accepted so no READ-BACK needed | OK |
| 29 | `git diff --stat -- <card>`; `git log -1 --format=%h -- <card>` | diff empty; `51816c25` (committed, clean) | OK |

## ISSUES

None. (Sibling cards `64-deploy-d5-card.md` and `09-deploy-next-flow-card.md` were not opened separately; shape was checked against `CARD.md` and `desk-launch.sh`.)

PREFLIGHT DONE · card: deploy-flake-fix-2-31 · checks: 29 · fails: 0 · ready: YES
