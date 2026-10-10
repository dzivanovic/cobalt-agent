## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>` | empty (card committed, no diff) | OK |
| 2 | `git diff b8201983~1 b8201983 -- <card>` | one `+` line, row `S`, after H6; no other row, no `BASE`/`TIP`/`CHECK REPORT`/`HOUSE B`/`RULINGS` line changed | OK |
| 3 | row S text vs verbatim ROW TEXT in `291-draft-ops-hand-row-s.md` | task column = text through "stop with a DECISION."; proof column = text after "Proof:" through "at the new tip"; files column = after "Files:"; no word dropped (only the labels `Proof:`/`Files:` became column heads) | OK |
| 4 | row S files names `ops/desk/bare-guard.py` and its tests; card union keeps the path | row S files: `ops/desk/bare-guard.py`, its tests; H1 and H2 also list `ops/desk/bare-guard.py`, `tests/ops/test_bare_guard.py` (`tests/ops/test_bare_guard.py` exists) | OK |
| 5 | `git show main:ops/desk/bare-guard.py --stat` and `seat()` / G9 in the file | file exists on main; `def seat` at `:732`; G9 tribunal rule at `:125`, `:754` (R877) | OK |
| 6 | `git diff 1eb47b59 main --stat -- ops/desk/bare-guard.py` | 1 file, 8 insertions, 4 deletions (non-empty) | OK |
| 7 | `git rev-parse 6a18ff95 1eb47b59` | `6a18ff952447964f062645974cdc613d6ec6e3b7`, `1eb47b5928dfc5fb90fe0fa950da19c2c6681bc2` | OK |
| 8 | `grep -c "«FILL" <card>` | 0 | OK |
| 9 | new command introduced (R411, R412) | row S names only `git show`, `git diff`, the Edit tool and `deploy-card.sh` (`ops/desk/deploy-card.sh` exists); none new | OK |
| 10 | proof of row S | `deploy-card.sh` exit 0 is a RUN, asserts nothing (L70); fix-round shape not re-checked (CHECK-HUB, L75) | OK |

## ISSUES
- NOTE: row S writes the branch as `ops/hand-1010`; the real branch is `ops/ops-hand-1010` (card BRANCH line; `rev-parse` gives `6a18ff95`). Brain's verbatim text, kept as is; the tip sha is right.
- NOTE: card header `TIP: 2cb7a9ad` is stale against row S's tip `6a18ff95` (the branch tip today). The header is the desk's field and was not changed; the desk updates it at the next tip.
- NOTE: `OPS_HAND` and `G12` do not exist on main's `bare-guard.py` (they live on the branch), as row S expects; H1's older `file:line` refs (`:731-752` etc.) are from `d0a5fbb8` and are shifted on main now (`seat` is `:732`); row S cites none of them.

PREFLIGHT DONE · card: ops-hand-1010 · checks: 10 · fails: 0 · ready: YES
