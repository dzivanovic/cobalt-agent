# P2 deploy card preflight — 2026-10-05

Card `61-deploy-p2-card.md` (`p2-deploy-61`): every fact checked, 8 of 8 OK, no issues.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `rev-parse --verify f15/p2-replay-1004^{commit}` | `6269f05e120c3f33a35951b2bdc7199e4a068fd9` = card TIP `6269f05e` (head) | OK |
| 1 | `log --oneline 437c7299..f15/p2-replay-1004 -- tests src configs ops`; `merge-base --is-ancestor 437c7299 f15/p2-replay-1004` | both empty, exit 0 | OK |
| 1 | `tail -n 5` of the check report | last line: `CHECK DONE · job: f15-p2 · pass: 1 · tip: 437c7299 · … held unfixed: 0 · … ready: YES …` = the SHIPS cell's spelling; `log -1 --format=%h` → `4e8795dc`, `diff --stat` empty | OK |
| 2 | `merge-base --is-ancestor c96b5118 main`; same for `07a4b8fe` | exit 0, exit 0 | OK |
| 2 | `diff --stat main...f15/p2-replay-1004` | 10 files, 1822 insertions, 4 deletions: `cobalt/cards/cli.md`, `cobalt/cards/predictions.md`, `reports/f15-p2-build-2026-10-04.md`, `ops/desk/gate-lists.md`, `src/cobalt/cards/cli.py`, `src/cobalt/cards/predictions.py`, `tests/cobalt/test_f15_p2_replay.py`, `tests/cobalt/test_f15_p2_replay_db.py`, `tests/experiments/f15_p2/conftest.py`, `tests/experiments/f15_p2/test_x7_x10_x11_db.py`. The card lists the same ten, each with its RESTARTS class (aset+radar, radar, operator script, test, test, test, test, DOCS ×3). No D5 or K3 file. | OK |
| 3 | `rev-parse --verify deploy/deploy-p2-1005`; `rev-parse --verify refs/tags/deploy-2026-10-05-p2` | `fatal: Needed a single revision`, twice (both new) | OK |
| 3 | `ls /Users/cobalt/cobalt-wt/deploy-p2-1005`; `ls …/reports/deploy-deploy-p2-1005.md` | `No such file or directory`, twice (both new) | OK |
| 4 | `grep -n "^| R326 "` in `reports/cto-2026-10-03.md` | line 332: `HIS RULING: A on all three …` · `HIS RULING · APPROVED`; `log -1 -S"| R326 |"` → `b1337431`; file clean | OK |
| 4 | `grep -n "^| R412 "` in `reports/cto-2026-10-05.md` | line 109: `HIS RULING: drop pre-merge (d2) …` · `APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a)`; `log -1 -S"| R412 |"` → `b3583b28`; file clean | OK |
| 5 | marker counts on main (`def corpus(`, `def replay(`, `def cmd_replay`) | `0`, `0`, `0` = card `before` | OK |
| 5 | `ls` of the two test paths on main | `No such file or directory`, twice = card `before` | OK |
| 5 | `git show 437c7299:<path>` | `predictions.py`: `def corpus(` 1, `def replay(` 1; `cli.py`: `def cmd_replay` 1; `test_f15_p2_replay.py` and `conftest.py` exist = card `after`. No marker on a D5 file (`drc/reconcile.py` dropped). | OK |
| 6 | `CARD.md` line 44 and `ops/desk/deploy-card.sh` line 207 | both: `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|`, the card's SHIPS header is the same seven columns | OK |
| 7 | `grep -c -F "«FILL"` on the card | `0`; header keys and `## SHIPS` / `## MARKERS` / `## SMOKE READS` / `## RECORDS` match `64-deploy-d5-card.md` and `51-deploy-k3-card.md` | OK |
| 8 | `git diff --stat --` and `git log -1 --format=%h --` on the card and both drafter reports | diff empty for all; card `4c58a879`, first draft `d664b926`, re-point `4c58a879` | OK |

## ISSUES

None.

PREFLIGHT DONE · card: p2-deploy-61 · checks: 8 · fails: 0 · ready: YES
