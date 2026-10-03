# Set 2 deploy card — preflight (2026-10-03)

Card: `prompts/2026-10-03/23-deploy-set2-card.md`

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `rev-parse --short=8` row 1 `ops/adoption-scripts-b2-1003` | `9694a679` (card: `9694a679`) | OK |
| 1b | `rev-parse --short=8` row 2 `ops/rename-follow-up-1003` | `8c32a8d1` (card: `8c32a8d1`) | OK |
| 1c | `rev-parse --short=8` row 3 `ops/close-timer-1003` | `47a689a1` (card: `47a689a1`) | OK |
| 1d | `rev-parse --short=8` row 4 `ops/deploy-steps-1003` | `f04a1d56` (card: `f04a1d56`) | OK |
| 1e | tail of row 1 check report | `tip: b7eeb80c` · `held unfixed: 0` · `ready: YES` | OK |
| 1f | tail of row 2 check report | `tip: 393f3ad5` · `held unfixed: 0` · `ready: YES` | OK |
| 1g | tail of row 3 check report | `tip: 47a689a1` · `held unfixed: 0` · `ready: YES` | OK |
| 1h | tail of row 4 check report | `tip: f04a1d56` · `held unfixed: 0` · `ready: YES` | OK |
| 1i | `merge-base --is-ancestor b7eeb80c ops/adoption-scripts-b2-1003` | exit 0 | OK |
| 1j | `merge-base --is-ancestor 393f3ad5 ops/rename-follow-up-1003` | exit 0 | OK |
| 1k | `merge-base --is-ancestor 47a689a1 ops/close-timer-1003` | exit 0 | OK |
| 1l | `merge-base --is-ancestor f04a1d56 ops/deploy-steps-1003` | exit 0 | OK |
| 2a | `merge-base --is-ancestor 0a4a7743 ops/adoption-scripts-b2-1003` | exit 0 | OK |
| 2b | `merge-base --is-ancestor 6251baeb ops/adoption-scripts-b2-1003` | exit 0 | OK |
| 3a | `diff --stat main...ops/adoption-scripts-b2-1003 -- src/cobalt/db_migrations` | only `cli.py` (114 insertions, 1 deletion); no new migration file (card: `cli.py` is migrate-command code) | OK |
| 3b | same, `ops/rename-follow-up-1003` | empty | OK |
| 3c | same, `ops/close-timer-1003` | empty | OK |
| 3d | same, `ops/deploy-steps-1003` | empty | OK |
| 4a | main: `ls tests/ops/test_desk_launch_recut.py` | `No such file or directory` | OK |
| 4b | main: `grep -c -F "The old side of a rename/copy" src/cobalt/jobs/restarts.py` | `0` | OK |
| 4c | main: `ls ops/desk/close-timer.sh` | `No such file or directory` | OK |
| 4d | main: `ls ops/desk/deploy-step0.sh` | `No such file or directory` | OK |
| 4e | `ls-tree` row 1 head, `tests/ops/test_desk_launch_recut.py` | listed | OK |
| 4f | `git grep -c -F "The old side of a rename/copy" ops/rename-follow-up-1003 -- src/cobalt/jobs/restarts.py` | `:1` | OK |
| 4g | `ls-tree` row 3 head, `ops/desk/close-timer.sh` | listed | OK |
| 4h | `ls-tree` row 4 head, `ops/desk/deploy-step0.sh` | listed | OK |
| 5a | `ls-tree` row 1 head, `tests/ops/test_hub_lines.py` and `tests/cobalt/test_migrate_level.py` | both listed | OK |
| 5b | `git grep -c -F "def test_" ops/rename-follow-up-1003 -- tests/cobalt/test_jobs_restarts.py` | `19` (1 or more) | OK |
| 5c | `ls-tree` row 3 head, `ops/desk/com.cobalt.close-timer.plist` | listed | OK |
| 5d | `ls-tree` row 4 head, `ops/desk/deploy-outage.sh` and `ops/desk/deploy-smoke.sh` | both listed | OK |
| 5e | the four smoke commands: absolute paths, no `%` | read from the card | OK |
| 6a | `grep -c -x -F` of the adoption-scripts-b stop line against its report | `1` | OK |
| 6b | same, rename-follow-up | `1` | OK |
| 6c | same, close-timer | `1` | OK |
| 6d | same, deploy-steps | `1` | OK |
| 7a | `grep -n "^| R149 " cto-2026-10-02.md` | `156:` … `HIS RULING: Saturday 10-03 is not a trading day …` … `HIS RULING · APPROVED` | OK |
| 7b | `grep -n "^| R157 " cto-2026-10-02.md` | `164:` … `HIS RULING (B): the brain's full process list for 10-03 runs this week …` … `HIS RULING · APPROVED` | OK |

## ISSUES

None.

PREFLIGHT DONE · card: set2-1003 · checks: 38 · fails: 0 · ready: YES
