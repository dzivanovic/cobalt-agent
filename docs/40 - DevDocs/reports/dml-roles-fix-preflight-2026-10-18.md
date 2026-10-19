# Card 448 `dml-roles-1013` — preflight of row FIX1 (read-only), 2026-10-18

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read `/Users/cobalt/cobalt-wt/dml-roles-1013/tests/cobalt/test_db_credentials.py:168` | `class TestTheLiveFactoryAuthenticatesAsCobaltApp:` (under `@requires_db`, `:167`) | OK |
| 2 | Read the same file `:202-211` | `:202` `def test_it_is_a_member_of_all_three_side_roles(self, real_connect)`; `:204-210` the `pg_auth_members` query, `ORDER BY 1`; `:211` `assert [r[0] for r in rows] == ["cobalt_backup", "cobalt_system", "cobalt_user"]`. Every `file:line` of FIX1 holds | OK |
| 3 | the row's assertion text | exact sorted full list `["cobalt_apply_system", "cobalt_apply_user", "cobalt_backup", "cobalt_system", "cobalt_user"]`, "the full list and never a subset check"; sorted order matches `ORDER BY 1` (`_` sorts after letters in the C-like order of the other names; `apply_*` < `backup` < `system` < `user`). X7 repeats "no subset form" | OK |
| 4 | the row's rename | `test_it_is_a_member_of_exactly_the_five_roles`, "its name and docstring say five roles" (the test has no docstring today, so the builder adds one) | OK |
| 5 | the row's scope | "that one test and nothing else: no other line of `test_db_credentials.py` changes"; files column "(the one test at `:202-211` only)" | OK |
| 6 | grep for a command string in FIX1, X7 and the FIX1 RECORDS lines | none: FIX1 adds no launch line, allow string or command; `## RECORDS` COMMANDS (R411, R412) stands as written (`uv run pytest`, `uv run cobalt jobs restarts`, the desk scripts) | OK |
| 7 | RESTARTS class home (K10) | `## RECORDS` last-but-three bullet: "FIX1 adds `tests/cobalt/test_db_credentials.py` → `test/documentation; no resident` (`:245-246`) … R2's expected `com.cobalt.radar` alone stands" | OK |
| 8 | `grep -c -E "^\| FIX1 \||^- X7 \|FIX1 reads"` of the card | `3` (row FIX1, X7 in `## CHECK ASKS`, FIX1 reads in `## RECORDS`) | OK |
| 9 | the continue step | row FIX1: "After the row the continue step is `W` again, then the check, then the deploy" | OK |
| 10 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- "…/448-dml-roles-card.md"`, `git log --oneline -3 -- <card>` | diff prints nothing; last commit `c8b4986d docs(desk): 448 FIX1 and gemini-grant cards, preflights, deploy 798 failed` | OK |
| 11 | `grep -l "test_db_credentials" -r prompts/2026-10-18` | only `801-draft-448-fix-round.md` and `802-448-fix-preflight.md` (the drafter's own prompt and this one). No other open card names the file | OK |
| 12 | FIX1's RED names a reason | the old three-role assertion is red against the five memberships (`At index 0 diff: 'cobalt_apply_system' != 'cobalt_backup'`, build report `:100`, `:127`); the new exact-five is green on this cluster and red on a sixth membership | OK |
| 13 | ASK DESK judged | see `## ISSUES` NOTE 1 and NOTE 2 | OK |

## ISSUES
- NOTE 1 (ASK DESK, the drafter's default): the exact-five assertion reads cluster-wide membership, so it is red on a cluster where 0025 never ran. The gate does NOT run after 0025's first forward on a fresh cluster: W's pass 1 runs at 0013 before the `--migration` forward (build report `:100`: run 1's pass 1 "was green only because it ran before any forward"). On THIS cluster the memberships already exist (run 1's forward made them; the rollback keeps them, D6), so pass 1 is green with FIX1. A rebuilt or new cluster would be red in pass 1 until some 0025 forward ran there. Default (exact five, as ruled) is right; no change to the card.
- NOTE 2 (what blocks the card's own deploy): (a) card 304 deploys first and the deploy is outside market hours (R1309, `## RECORDS`); (b) until FIX1 reaches `main`, every gate on this server that runs `main`'s old three-role pin meets the same pass-1 red, because the memberships are cluster-wide (build report `:115`; deploy 798 cos-outage failed for it, commit `578b2512`). 448's own gate runs FIX1 and is green on the five memberships.
- NOTE 3: the build report's suggested fix carried a `# DML roles (0025)` comment on the line; the row does not ask for it. Optional, no fail.
- NOTE 4: the row gives no command line for FIX1's RED; the builder quotes the pass-1 output of W. Same as card 503's FIX1 shape.

PREFLIGHT DONE · card: dml-roles-1013 · checks: 13 · fails: 0 · ready: YES
