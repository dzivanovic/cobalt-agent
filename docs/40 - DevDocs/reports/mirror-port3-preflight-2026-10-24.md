# mirror-port3 preflight — card 1041 — 2026-10-24

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read card; `git log --oneline -1 986feb8c`; `grep -n "^| R1863 " reports/cto-2026-10-18.md` | all CARD.md headers present (JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, BAND, RESTARTS, MIGRATIONS, RULINGS); only placeholder is the empty `TIP:`; JOB `radar-mirror-scope-port3`, BRANCH `ops/radar-mirror-scope-port3`, WORKTREE `radar-mirror-scope-port3`, BAND HIGH; BASE `986feb8c` resolves (main commit, ancestor of HEAD `8db139ef`); R1863 line 90 = `HIS RULING · APPROVED` | OK |
| 2 | `git diff --stat 11ed17b8 25994142` | 9 files: the 7 spec files (notes.md 32, notes.py 46, test_radar_evaluate 4, test_radar_mirror_scope 201, test_radar_notes 7, test_radar_replay 21, test_radar_runner 17) + build report + `.result`; card's E1(b) rows list the same 7 with the same counts, none extra; the 2 reports are named as excluded | OK |
| 3 | `git diff --stat 11ed17b8 HEAD --` the 7 paths | empty (main unchanged on all seven) | OK |
| 4 | builder commands in card vs `BUILD-HUB.md:14` | only `git show`, `git diff`, `uv run pytest`, `uv run cobalt jobs restarts`; `git apply`/`cherry-pick`/`git mv`/`rm`/`mv`/`revert` appear only as prohibitions in NOT IN THIS JOB | OK |
| 5 | markers vs spec/HEAD; `deploy-smoke.sh` :118, :122, :188-189 | `git grep -c -F "MIRROR_SOURCE_PREFIX = "`: 25994142 → 1, HEAD → 0 (before 0 / after 1 right); test def: 25994142 → 1, absent on HEAD (before 0 per hub precedent, DECISION 3); both marker forms (`grep -c -F`, `ls`) are mapped; no curl, no http, no `uv run` in section | OK |
| 6 | RESTARTS / MIGRATIONS lines | `com.cobalt.aset com.cobalt.cos com.cobalt.radar`; `none` | OK |
| 7 | `grep -F` the brain's line in prompt 1040:8; GATE and RECORDS | RECORDS line 73 is verbatim to 1040:8; HOLD named (RECORDS, NOT IN THIS JOB); GATE names Monday 2026-10-26 after 16:00 ET and a non-idle radar cycle clearing the stale stamp first | OK |
| 8 | `grep pytest` card 1032 vs card 1041 ORDER | same 7 test files, identical command | OK |

## ISSUES
- NOTE: BASE `986feb8c` is not HEAD (`8db139ef`, two desk-doc commits later); the card says the desk resets it at launch. Not a blocker.
- NOTE: marker 2 `before 0` while the test file is absent (grep prints `No such file`, exit 2); card DECISION 3 and deploy 1027 treat absent as a valid before. Not a blocker.
- NOTE: the empty `TIP:` is the desk's token, allowed.
- Blockers: none.

PREFLIGHT DONE · card: 1041 · checks: 8 · fails: 0 · ready: YES
