# worktree-salvage preflight r2 — 2026-10-07 (card 83, after amend)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C … diff f77f1bc3 HEAD -- <card>` | 3 hunks only: W1 `:19`, W4 `:22`, W7 `:25`, X2 `:45` (4 rows' edits: count, lock match, clean-tree commit, `clean -` note). No other line moved (header, W2, W3, W5, W6, NOT IN, RESTARTS, RECORDS untouched) | OK |
| 2 | `git log --oneline -4 -- <card>` ; `git diff --stat HEAD -- prompts/2026-10-07 cto-2026-10-07*.md draft` | `62545d31`, `f77f1bc3`; diff empty (card, draft, R613 rows committed; HEAD now `c4e52f4e`) | OK |
| 3 | `grep -c "FILL" <card>` | `1` (the BASE token only); BRANCH `ops/worktree-salvage-1007`, WORKTREE `worktree-salvage-1007`, TIP/CHECK REPORT/HOUSE B empty, `DB: none` (header lines 1-11 not in diff) | OK |
| 4 | `ls /Users/cobalt/cobalt-wt` | no `worktree-salvage-1007` (worktree new) | OK |
| 5 | `grep -n "R613" reports/cto-2026-10-07.md` | `:8` `HIS RULING … APPROVED — pending fold`; committed (#2) | OK |
| 6 | `git diff --stat f77f1bc3 HEAD -- ops/desk/job-clean.sh tests/ops/test_gate_clean.py src/cobalt/jobs/restarts.py` | empty: every `file:line` cite proven in round 1 still holds | OK |
| 7 | FAIL #13 fixed: `grep -n "def test_\|parametrize" tests/ops/test_gate_clean.py`, own count | `:251-315` holds `def test_` at `:251 :269 :274 :282 :291 :298 :310` = 7 functions; `@parametrize` `:290` over 6 values → 6 + 6 = 12 collected. Card W1 now says "7 test functions, 12 collected tests, the parametrized `:290` running 6 cases"; X2 says "the 12 old collected tests (7 functions)". Whole file 22 `def test_` (32 collected) | OK |
| 8 | NOTE W4 fixed: read card `:22` | `add -A` and `commit` run only when `status --porcelain` non-empty; DETACHED CLEAN unmerged → `switch -c` alone, `SALVAGED: <wip> 0 files <m> commits ahead`; DETACHED test says "the clean path … the wip tip is that commit" | OK |
| 9 | NOTE W1 fixed: read card `:19` | "the line matches `^locked( \|$)` (git prints `locked <reason>` …), not the bare line" | OK |
| 10 | NOTE W7 fixed: read card `:25` | "greps for `--force` and `-f ` forms only, so `clean -` is a loose substring: the builder keeps the card header and every script comment free of `clean -`" | OK |
| 11 | `grep -n -e "--force" -e "branch -D" -e " -f" -e "reset --hard" -e "clean -" <card>` | hits `:15 :24 :25 :48` only, all prose forbidding the forms; no script text with a force form | OK |
| 12 | RED/control status on BASE (W1-W7, `:24` one-arg usage refusal; W6 grep `0`) | unchanged by the amend (no row's test or assertion edited); round-1 #17-20 stand | OK |
| 13 | Rows W1-W7 vs R613; new commands vs R411/R412; RESTARTS homes | no row added or removed; the amend's W4 text names no new command (`switch -c`, `add -A`, `commit` already there); RESTARTS paragraph and RECORDS unchanged | OK |

## ISSUES
- NOTE: the amend report `## RECORDS` lists `:290` among the `def test_` lines; the `def` is `:291` (`:290` is the decorator). Counts are right; the card cites `:290` only as "the parametrized".
- NOTE: the draft report still says "eight existing tests" / "8 tests" (desk's kept default; not a fail).
- NOTE: main HEAD is `c4e52f4e`; BASE is still the desk's fill at launch.

PREFLIGHT DONE · card: worktree-salvage-83 · checks: 13 · fails: 0 · ready: YES
