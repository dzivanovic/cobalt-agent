# launcher-checks card 21, rows F2-F4: preflight r3 (2026-10-05)

Card: `prompts/2026-10-02/21-launcher-checks-card.md`. Read-only: no test run, no git write.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5fb0ddf5 main` | exit 0 (main is `caedb43f`); BASE is on main | OK |
| 2 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` | `7e7803d5`; the branch exists and sits on the check's tip, past header TIP `c1746720` (`rev-parse --short=8 c1746720` → `c1746720`) | OK |
| 3 | `ls -d /Users/cobalt/cobalt-wt/launcher-fixround-1005 "…/reports/launcher-checks-check-2026-10-05.md"` | both listed: the WORKTREE and the CHECK REPORT exist | OK |
| 4 | `grep -n -E "^\| R(412\|439) " …/cto-2026-10-05.md` | `109:\| R412 \| … HIS RULING: drop pre-merge (d2) … \| APPROVED (in cto-desk-contract.md …)`; `135:\| R439 \| 10-05 15:44 ET \| DESK RECORD: card 21 check ready NO (O1/O4…). Brain ruled (a): rows F2-F4 on card 21; card 26 deploys FIRST, card 21's builder merges main after … \| LAUNCHED` | OK |
| 5 | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R412 \|" -- "…/cto-2026-10-05.md"` | `b3583b280d50c829da1d8f5290c2c385b50ef68c`: R412 is committed | OK |
| 6 | `git show main:ops/desk/deploy-step0.sh` + `grep -n` (`diff --stat main` on the file → empty) | `337: lits=$(printf '%s\n' "$line" \| awk -F'\|' '{print $7}' …)`; `358: # P2: the check's stop line`; `378: t=$(… 'tip: …')`; `381: "$ctip"*) ;;`; `382: … why="its tip $t is not the row's code tip $ctip"`; `387: row "P2 check $n" …`. P2 block 358-387, tip test 377-384, refusal 382 | OK |
| 7 | `grep -n -E "P2 EVERY CHECK\|…" DEPLOY-HUB.md` (`diff --stat main` empty) | `58:- **P2 EVERY CHECK, COMMITTED** (L67). … its `tip:` equals the row's code tip; …` | OK |
| 8 | `grep -n -E "^\| # \| branch\|^\|---…\|^The code tip is" CARD.md` (`diff --stat main` empty) | `44:\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|`; `45:\|---\|---\|---\|---\|---\|---\|`; `47:The code tip is the `tip:` of the check's stop line (a fresh Opus pass may have moved it past the build's). The last column is `held unfixed: 0` and `ready: YES` …` | OK |
| 9 | F2 red-first: `git show ops/launcher-fixround-1005:tests/ops/test_deploy_step0.py` (read) | `@pytest.mark.xfail(strict=True, …)` above `test_o1_a_fix_round_row_the_launcher_accepts_passes_p2`; assertion `assert "is not the row's code tip" not in last_line(done), done.stdout`. By reading, main's script (check tip `checked` ≠ code tip `fixed`, line 382) ends `… its tip <checked> is not the row's code tip <fixed>`: red on BASE. The check's RUNS O1 quotes that run. Negative controls (a)-(c) are named with the expected `FAILED STEP-0: P2 check 1 — …`; the no-fix-report control is `test_a_check_report_whose_tip_is_not_the_row_s_code_tip_fails`, which exists | OK |
| 10 | F3 red-first: `grep -c -F "is an ancestor of the code tip" DEPLOY-HUB.md` (without the backticked `tip:`: a backtick refused in one bare command) | `0` | OK |
| 11 | F4 red-first: `grep -c -F "is an ancestor of the code tip" CARD.md` (same spelling) | `0`; the card's second grep `grep -n -F "The last column is"` hits only line 47 (check 8) | OK |
| 12 | F3 text names the merge: row F3 | "BEFORE writing this row the builder merges `main` into its branch, then re-reads line 58"; line 58 only | OK |
| 13 | Fence: card `## NOT IN THIS JOB` and the F2-F4 files columns | F2 `deploy-step0.sh` + `test_deploy_step0.py`; F3 `DEPLOY-HUB.md` (line 58 only); F4 `CARD.md` (lines 44-45 and 47); NOT IN THIS JOB lists the same, with F1's `desk-launch.sh`, its test, `deploy-card.sh` 141/207-208 and `CARD.md` 44-45. Note: `deploy-card.sh` is F1's, already built at `c1746720`, and is not in this prompt's list; not a F2-F4 file | OK |
| 14 | No row adds a command or argument | F1 says "the column is a header value, not a new argument or command"; F2-F4 touch P2 logic and two text lines only | OK |
| 15 | Rule text of F2-F4 against the brain's rule (prompt line 9) | The card (lines 29-31, F2, F3, F4) says "the literals and the `tip: <code tip>` are read from the fix report's `BUILT ·` stop line". The brain's rule: the literals (`held unfixed: 0`, `ready: YES`) are read from the CHECK report's last line; only `tip: <code tip>` comes from the fix report's `BUILT ·` line. A BUILT line holds no literals (the O1 test's fix report has none; amend 4 DECISION 1 says so), so a builder following the card text fails the xfail-turned-test | FAIL |
| 16 | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | (empty) | OK |
| 17 | `git -C /Users/cobalt/cobalt log -1 --format=%h -- <card>` | `caedb43f`: committed | OK |
| 18 | `grep -c -F "«FILL" <card>` | `0` | OK |

## ISSUES
- #15: F2, F3 and F4 read "the literals and `tip: <code tip>` … from the fix report's `BUILT ·` stop line"; the brain's rule reads the literals from the check report's last line and only `tip: <code tip>` from the fix report. Fix the wording in all three rows (and the matching header sentence line 29) before the builder resumes.

PREFLIGHT DONE · card: launcher-fixround-21 · checks: 18 · fails: 1 · ready: NO
