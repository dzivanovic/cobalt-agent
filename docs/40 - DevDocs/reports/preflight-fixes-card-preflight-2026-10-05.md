# preflight-fixes card 20 — preflight (read-only), 2026-10-05

Card: `prompts/2026-10-05/20-preflight-fixes-card.md`. The hubs, `preflight.sh` and the test file have no diff `b56622fa..HEAD` and no working-tree change, so what I read is BASE.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git merge-base --is-ancestor b56622fa main` | exit 0, no output | OK |
| 2 | `git rev-parse --verify ops/preflight-fixes-1005` | `fatal: Needed a single revision` (exit 128): branch is new | OK |
| 3 | `ls /Users/cobalt/cobalt-wt/preflight-fixes-1005` | `No such file or directory`: worktree is new | OK |
| 4 | card header read | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `DB: none` present; `RULINGS: 2026-10-05 R387, 2026-10-05 R412` | OK |
| 5 | `grep -n "^\| R387 " cto-2026-10-05.md` + `git log -1 --format=%h -S"\| R387 \|"` | `62:\| R387 \| 10-05 08:53 ET \| HIS RULING (L79, via brain): …`; commit `744a596a` | OK |
| 6 | `grep -n "^\| R412 "` + `git log -1 --format=%h -S"\| R412 \|"` | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) …`; commit `b3583b28` | OK |
| 7 | `preflight.sh` 143-157 at BASE | line 143 `else`, 144 `tip_full=…`, 149-156 the `git log --stat` docs-only rule, 157 `fi`: the check's head row, as the card says | OK |
| 8 | `preflight.sh` 203-205 at BASE | `case "$last" in` / `"BUILT · job: $job · tip: $tip"*"self-check: 3 of 3"*) ok=0 ;;` / `esac` | OK |
| 9 | `BUILD-HUB.md:97` | `A line you cannot back → fix it, or `self-check: <k> of 3` in the stop line with the gap under `## DECISIONS`.` The card's quote is byte for byte (it drops the final period) | OK |
| 10 | `CHECK-HUB.md:61` | `… A lower self-check count is recorded and goes to the house as a fact.` byte for byte | OK |
| 11 | `CHECK-HUB.md:120` | `- PREFLIGHT, added: `tail -n 3 "<CHECK REPORT>"` → the last non-blank line starts `CHECK DONE · job: <JOB> · pass: 1` and carries `house B: needed` … `<tip now>` = its `tip:`, and `git log --oneline -1` shows it (or a docs-only commit above it).` The card's quotes match byte for byte | OK |
| 12 | `CHECK-HUB.md:58` (and READ's "line 58 (`## PREFLIGHT`…)") | Line 58 is the `<CHECK REPORT>` section list. The `preflight.sh check "<card>"` call is at line 61, under the `## PREFLIGHT` heading at line 60. "Same call for both passes" is stated at line 8 (`desk-launch.sh check <card> PASS-2`, "the same line"). The hub text the card relies on exists; its line numbers 58 (twice) are wrong | FAIL |
| 13 | `tests/ops/test_preflight.py` | Line 213 is `test_a_check_whose_report_is_short_of_three_self_checks_fails`; lines 68-101 hold `write_card`, `built`, `GOOD_LAST`, `preflight`, `last_line`, `rules` | OK |
| 14 | F1 red, by reading 199-206 | A last line with `self-check: 2 of 3` does not match the `case` pattern at 204, so `ok=1`, `report` fails, exit 1, `FAILED PREFLIGHT: report`. The rewritten test's `assert done.returncode == 0` fails on BASE as stated | OK |
| 15 | F1 negative control | A last line with ` \| self-check: 3 of 3` cut out cannot match the pattern at 204, so it fails `report` on BASE. Green on BASE, as the card says | OK |
| 16 | F2 red, by reading 143-157 | The card `TIP` is the build tip. A `fix(x-job):` src commit above it gives `others=src/a.py`, so `ok` stays 1 and the last line is `FAILED PREFLIGHT: head` (`status` precedes `head` and is clean). The new test's `assert returncode == 0` fails on BASE as stated | OK |
| 17 | F2 negative controls | `house B: not needed` and "a further src commit above the pass-1 tip" both leave a src commit above the card `TIP` on BASE, so `FAILED PREFLIGHT: head`. Green on BASE for the stated reason; the card also has them run against the fixed script | OK |
| 18 | new commands in rows | Rows use `ops/desk/preflight.sh` and the gate's `uv run pytest -q tests/ops/test_preflight.py`. The build allow line has `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` and `Bash(uv run pytest *)` (BUILD-HUB.md:12). No new command | OK |
| 19 | `grep -c -F "«FILL"` on the card | `0` | OK |
| 20 | `git diff --stat -- <card>` and `git log -1 --format=%h -- <card>` | diff empty; log `e7cebe73`: committed on main and clean | OK |

## ISSUES
- Check 12: the card cites `CHECK-HUB.md:58` for the `preflight.sh check "<card>"` call used in both passes. That call is at `CHECK-HUB.md:61`, and the "same line for PASS-2" statement is at `:8`. The `## READ` entry "line 58 (`## PREFLIGHT`, the self-check sentence at 61)" should read lines 60-61. The row-F2 sentence and READ both need the citation fixed.

PREFLIGHT DONE · card: preflight-fixes-20 · checks: 20 · fails: 1 · ready: NO
