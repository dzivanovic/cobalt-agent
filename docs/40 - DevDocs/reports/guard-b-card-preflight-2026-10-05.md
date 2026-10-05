## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify 47ec01c5^{commit}` | `47ec01c5cc6ba97cda7caa8c516fe9dc25359b9b` | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/cobalt-guard-b-1004` | `47ec01c5cc6ba97cda7caa8c516fe9dc25359b9b` (= tip, the branch head) | OK |
| 1c | `tail -n 1` of `cobalt-guard-b-check-2026-10-04-r3.md` | `CHECK DONE · job: cobalt-guard-b · pass: 1 · tip: 47ec01c5 · … · held unfixed: 0 · … · RESTARTS: none · … · ready: YES · decisions: 1 · for Dejan: 0` | OK |
| 1d | `git log -1 --format=%h -- <check report>` | `e3202c78` (committed) | OK |
| 2a | `rev-parse --verify deploy/deploy-guard-b-1005` | `fatal: Needed a single revision` (absent) | OK |
| 2b | `ls /Users/cobalt/cobalt-wt/deploy-guard-b-1005` | `No such file or directory` | OK |
| 2c | `ls <reports>/deploy-deploy-guard-b-1005.md` | `No such file or directory` | OK |
| 2d | `rev-parse --verify deploy-2026-10-05-guard-b` | `fatal: Needed a single revision` (tag absent) | OK |
| 3a | `grep -n "^| R39[0-2] " reports/cto-2026-10-05.md` | lines 67 R390 `HIS RULING (L79, via brain…)`, 68 R391 `HIS RULING (desk chat)…`, 70 R392 `HIS RULING (desk chat)…` | OK |
| 3b | `git log -1 --format=%h -- reports/cto-2026-10-05.md` and `git diff --stat -- <same>` | `7e5f86e5`; diff empty (committed, clean) | OK |
| 4a | `grep -c -F "@include" /Users/cobalt/cobalt/ops/desk/bare-guard.py` (main) | `0` = card `before 0` | OK |
| 4b | `git show 47ec01c5:ops/desk/bare-guard.py`, saved, then `grep -c -F "@include"` on the saved output | `3` = card `after 3` | OK |
| 4c | smoke read `grep -c -F "@include" …/bare-guard.py` | same command as 4a/4b. On main today `0`, so it is red until the branch merges. After the merge it reads `3`, which meets "a count of 1 or more", exit 0. Expected for a pre-deploy card. | OK |
| 4d | `git diff --stat main...47ec01c5` | `reports/cobalt-guard-b-build-2026-10-04.md` (+352), `ops/desk/bare-guard.py` (+301), `tests/ops/test_bare_guard.py` (+299); 3 files, 932 insertions, 20 deletions | OK |
| 4e | RESTARTS class home (K10; check says `RESTARTS: none`) | `grep -F "bare-guard"` and `grep -F "ops/desk"` on `configs/cobalt/jobs.yaml` give no match. DEPLOY-HUB K10 is the STEP-4.7 smoke label and has no class rule. `CARD.md` has no K10 or RESTARTS text. The class is derived by `uv run cobalt jobs restarts`, which I may not run. The check's own table gave `RESTARTS: none`, and BUILD-HUB L42 makes an UNCLASSIFIED path a build failure, so the check ran with none unclassified. Not re-derived by me. | OK (not re-run) |
| 5 | `grep -c -F "«FILL" <card>` | `0` | OK |
| 6a | `git diff --stat -- <card>` | empty (clean) | OK |
| 6b | `git log -1 --format=%h -- <card>` | `7e5f86e5` (committed) | OK |

## ISSUES
- none (note on 4e: the RESTARTS class home was not re-derived. `uv run` is outside this seat's allowed commands.)

PREFLIGHT DONE · card: guard-b-15 · checks: 20 · fails: 0 · ready: YES
