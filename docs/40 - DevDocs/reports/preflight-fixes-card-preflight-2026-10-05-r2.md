# preflight-fixes card 20 — preflight round 2 (read-only), 2026-10-05

Card: `prompts/2026-10-05/20-preflight-fixes-card.md` (last commit `bb394622`). `git diff --stat b56622fa HEAD` and `git status --short` over `ops/desk/preflight.sh`, `tests/ops/test_preflight.py`, `BUILD-HUB.md`, `CHECK-HUB.md` print nothing, so what I read is BASE.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git merge-base --is-ancestor b56622fa main` | exit 0, no output: BASE is on main | OK |
| 2 | `git rev-parse --verify ops/preflight-fixes-1005` | `fatal: Needed a single revision` (exit 128): branch is new | OK |
| 3 | `ls /Users/cobalt/cobalt-wt/preflight-fixes-1005` | `No such file or directory`: worktree is new | OK |
| 4 | card header read | `TIP:`, `CHECK REPORT:`, `HOUSE B:` empty; `DB: none` present; `RULINGS: 2026-10-05 R387, 2026-10-05 R412` | OK |
| 5 | `grep -n "^\| R387 \|^\| R412 " cto-2026-10-05.md` | `62:\| R387 \| 10-05 08:53 ET \| HIS RULING (L79, via brain): …`; `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) …` | OK |
| 6 | `git log -1 --format=%h -S"\| R412 \|" -- cto-2026-10-05.md` and the same for R387 | R412 `b3583b28`; R387 `744a596a`: both committed | OK |
| 7 | `preflight.sh` 143-157 at BASE | 143 `else`, 144 `tip_full=…`, 149 `git log --stat`, 152-153 docs-only rule, 157 `fi`: the check's head row | OK |
| 8 | `preflight.sh` 203-205 at BASE | `case "$last" in` / `"BUILT · job: $job · tip: $tip"*"self-check: 3 of 3"*) ok=0 ;;` / `esac` | OK |
| 9 | `BUILD-HUB.md:97` | `A line you cannot back → fix it, or `self-check: <k> of 3` in the stop line with the gap under `## DECISIONS`.` The card's quote is byte for byte (drops the final period) | OK |
| 10 | `CHECK-HUB.md:61` | `… A lower self-check count is recorded and goes to the house as a fact.` byte for byte | OK |
| 11 | `CHECK-HUB.md:120` | `… the last non-blank line starts `CHECK DONE · job: <JOB> · pass: 1` and carries `house B: needed` … `<tip now>` = its `tip:`, and `git log --oneline -1` shows it (or a docs-only commit above it).` Card quotes byte for byte | OK |
| 12 | `CHECK-HUB.md:8` and `:60-61` (the round-1 FAIL) | line 8: `THE SECOND PASS is a second launch, `desk-launch.sh check <card> PASS-2`, of the same line`; line 60 is `## PREFLIGHT`, line 61 holds `preflight.sh check "<card>"`. The card now cites `8,61,120` and READ `60-61`: matches | OK |
| 13 | `BUILD-HUB.md:93-97, 105-109` | 93 `## PRE-STOP SELF-CHECK`, 97 the `self-check: <k> of 3` sentence; 105 `## STOP LINE`, 106 the BUILT line | OK |
| 14 | `tests/ops/test_preflight.py` 68-101, 193-230 | `write_card` 68, `built` 76, `GOOD_LAST` 87, `preflight` 90, `last_line` 96, `rules` 100; line 213 is `test_a_check_whose_report_is_short_of_three_self_checks_fails` | OK |
| 15 | F1 red, by reading 199-206 | A last line with `self-check: 2 of 3` does not match the pattern at 204, so `ok=1`, `report` fails, exit 1, `FAILED PREFLIGHT: report`. The rewritten test's `assert done.returncode == 0` fails on BASE | OK |
| 16 | F1 negative control | `GOOD_LAST` with ` \| self-check: 3 of 3` cut out cannot match line 204's pattern: fails `report` on BASE, green on BASE | OK |
| 17 | F2 red, by reading 143-157 | Card `TIP` is the build tip; a `fix(x-job):` src commit above it gives `others=src/a.py` (152), so `ok` stays 1 (153) and the last line is `FAILED PREFLIGHT: head` (`status` precedes it and is clean). The new test's `assert returncode == 0` fails on BASE | OK |
| 18 | F2 negative controls | `house B: not needed`, and a further src commit above the pass-1 tip, both leave a src commit above the card `TIP` on BASE: `FAILED PREFLIGHT: head`. Green on BASE for that reason | OK |
| 19 | new commands in rows | Rows use `ops/desk/preflight.sh` and `uv run pytest -q tests/ops/test_preflight.py`. `BUILD-HUB.md:12` allow line has `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` and `Bash(uv run pytest *)`. No new command | OK |
| 20 | `grep -c -F "«FILL"` / `git diff --stat -- <card>` / `git log -1 --format=%h -- <card>` | `0` / empty / `bb394622`: committed on main and clean | OK |

## ISSUES
- None.

PREFLIGHT DONE · card: preflight-fixes-20 · checks: 20 · fails: 0 · ready: YES
