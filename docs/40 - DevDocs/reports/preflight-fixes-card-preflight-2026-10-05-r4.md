# preflight-fixes card 20 — preflight round 4 (read-only)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `grep -n -F "test_the_trees_brain_hub_line_is_printed_with_its_handover_filled"` on the card | line 21: F3 red-first cell names that test and `assert INSTALL in text` (line 285), fails on BASE `b56622fa` | OK |
| 1b | `git -C … show b56622fa:tests/ops/test_desk_launch_brain.py` | `def test_the_trees_brain_hub_line_is_printed_with_its_handover_filled(tmp_path):` exists at BASE, body holds `assert INSTALL in text  # the title token stands until his approval row` | OK |
| 1c | `grep -n -F "assert INSTALL in text"` on the test file; `git diff b56622fa HEAD --stat -- <test file>` | `285:    assert INSTALL in text  # …`; diff stat empty (file identical at BASE and HEAD, so line 285 holds at BASE) | OK |
| 1d | `git show b56622fa:"docs/40 - DevDocs/prompts/BRAIN-HUB.md"` | title: `# BRAIN-HUB — the standing brain seat (installed 2026-10-05 on his 2026-10-02 R54 …)`; no `«INSTALL`, so the assert fails at BASE | OK |
| 2a | `git log --oneline -- <card>` | 71fcbefe, 98d77082, f29e19fb, bb394622, e7cebe73 | OK |
| 2b | `git diff 98d77082 HEAD -- <card>` (98d77082 = the card commit round 3 judged) | one hunk, `@@ -18,7 +18,7 @@`: only the F3 row's red-first cell changed; F1 and F2 rows are context lines | OK |
| 3a | `git diff --stat -- <card>` | empty | OK |
| 3b | `git log -1 --format=%h -- <card>` | `71fcbefe` | OK |
| 3c | `grep -c -F "«FILL" <card>` | `0` | OK |
| 3d | new command or argument (R411, R412) | the F3 diff adds only a test name, an assert and a commit hash; no command, no argument | OK |

## ISSUES
none

PREFLIGHT DONE · card: preflight-fixes-20 · checks: 10 · fails: 0 · ready: YES
