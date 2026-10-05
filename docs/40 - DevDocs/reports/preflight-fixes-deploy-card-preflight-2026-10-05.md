# preflight-fixes deploy card (39) — preflight, 2026-10-05

Read-only. Each command was run as typed (one per call); outputs quoted. Marker "after" counts were counted by hand from `git show 0af97be7:ops/desk/preflight.sh` (a pipe is not allowed on this seat): `card 20 F2` 2 lines (header `(card 20 F2)`, comment `# card 20 F2 (CHECK-HUB.md:120)`), `card 20 F1` 2 lines (header, `# card 20 F1 (BUILD-HUB.md:97…)`), `(recorded)` 2 lines (header, the `printf`).

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git rev-parse --verify 0af97be7^{commit}` | `0af97be7a51ea2892812032c0673276325a0dd2b` | OK |
| 1b | `git rev-parse --verify ops/preflight-fixes-1005` | `0af97be7a51ea2892812032c0673276325a0dd2b` (= tip) | OK |
| 1c | `tail -n 3` of check report | last line `CHECK DONE · job: preflight-fixes · pass: 1 · tip: 0af97be7 · … held unfixed: 0 · … ready: YES …` | OK |
| 1d | `git log -1 --format=%h -- <check report>` | `4f586d6e` | OK |
| 2a | `rev-parse --verify deploy/deploy-preflight-fixes-1005` | `fatal: Needed a single revision` | OK (new) |
| 2b | `rev-parse --verify deploy-2026-10-05-preflight-fixes` | `fatal: Needed a single revision` | OK (new) |
| 2c | `ls /Users/cobalt/cobalt-wt/deploy-preflight-fixes-1005` | `No such file or directory` | OK (new) |
| 2d | `ls <this report path>` before writing | `No such file or directory` | OK (new) |
| 3a | `grep -n -E "^\| R(376\|387\|390\|412) " reports/cto-2026-10-05.md` | R376 l.49, R387 l.62, R390 l.67, R412 l.109; each row begins `HIS RULING` | OK |
| 3b | `git log -1 --format=%h -- cto-2026-10-05.md` and `git diff --stat -- <it>` | `aedf6bac`; diff empty (clean, committed) | OK |
| 4a | `grep -c -F "card 20 F2" ops/desk/preflight.sh` (main) | `0` = before `0`; after on `0af97be7` = 2 | OK |
| 4b | `grep -c -F "card 20 F1" ops/desk/preflight.sh` (main) | `0` = before `0`; after = 2 | OK |
| 4c | `grep -c -F "(recorded)" ops/desk/preflight.sh` (main) | `0` = before `0`; after = 2 | OK |
| 4d | smoke reads (F2 `card 20 F2`, F1 `(recorded)`) | counts 2 and 2 on the tip: `1 or more` holds; grep exits 0 on a count ≥ 1 | OK |
| 4e | `git diff --stat main...0af97be7` | `preflight-fixes-build-2026-10-05.md` (docs/), `ops/desk/preflight.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_preflight.py`; 4 files, 291+/10−; SHIPS row names exactly these; no hub file | OK |
| 4f | RESTARTS home (K10): `grep -n -i RESTARTS <check report>` | l.7 `RESTARTS: none`; l.242–249 `jobs restarts b56622fa..HEAD` → `RESTARTS: none`; stop line `RESTARTS: none` | OK |
| 5a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 5b | shape vs `prompts/CARD.md` and `15-deploy-guard-b-card.md` | all deploy keys present (JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, RULINGS, TAG, MIGRATIONS, SET); `## SHIPS`, `## MARKERS`, `## SMOKE READS`, `## RECORDS` in order; no READ-BACK (MIGRATIONS none); same columns as the sibling; commands are `grep -c -F` on absolute paths | OK |
| 6a | `git diff --stat -- <card>` | empty | OK |
| 6b | `git log -1 --format=%h -- <card>` | `aedf6bac` | OK |

## ISSUES
None. Notes, not fails: (1) the card's RECORDS line for G (d2) says "per the sibling cards' RECORDS wording" and not a literal; per R412 (d2) is dropped from DEPLOY-HUB, so the hub reads it as the card says. (2) `cto-2026-10-05.md` showed a 2-line diff mid-run and was clean on re-read (the desk committed meanwhile); R376/R387/R390/R412 sit in the committed text.

PREFLIGHT DONE · card: preflight-fixes-deploy-39 · checks: 20 · fails: 0 · ready: YES
