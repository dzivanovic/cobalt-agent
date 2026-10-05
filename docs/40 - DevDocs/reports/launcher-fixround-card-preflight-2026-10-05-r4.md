# launcher-checks card 21, rows F2-F4: preflight r4 (2026-10-05)

Card: `prompts/2026-10-02/21-launcher-checks-card.md`. Read-only: no test run, no git write.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | r3 #15 ("F2, F3, F4 read the literals from the fix report; the brain reads them from the CHECK report") vs card now: `grep -c -F "read from the CHECK report's last line" <card>` | `3` (lines 29 F2 incl. its RULE sentence, 30 F3, 31 F4); `grep -c -F "literals and" <card>` → `0` (old clause gone). Card text: "the literals `held unfixed: 0` and `ready: YES` are read from the CHECK report's last line, and `tip: <code tip>` is read from the fix report's `BUILT ·` stop line". Amend 5 report agrees. #15 is the only r3 FAIL | OK |
| 2 | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5fb0ddf5 main` | exit 0, no output: BASE is on main | OK |
| 3 | `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-fixround-1005` and `… c1746720` | `7e7803d5` (branch exists, on the check's tip) · `c1746720` (header TIP resolves) | OK |
| 4 | `ls -d /Users/cobalt/cobalt-wt/launcher-fixround-1005 "…/reports/launcher-checks-check-2026-10-05.md"` | both listed: WORKTREE and CHECK REPORT exist | OK |
| 5 | `grep -n -E "^\| R(412\|439) " …/cto-2026-10-05.md` | `109:\| R412 … HIS RULING: drop pre-merge (d2) … \| APPROVED (in cto-desk-contract.md …)` · `139:\| R439 \| 10-05 15:44 ET \| DESK RECORD: card 21 check ready NO (O1/O4 …). Brain ruled (a): rows F2-F4 on card 21; card 26 deploys FIRST, card 21's builder merges main after … \| LAUNCHED` | OK |
| 6 | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R412 \|" -- "…/cto-2026-10-05.md"` | `b3583b280d50c829da1d8f5290c2c385b50ef68c`: R412 committed | OK |
| 7 | `git -C /Users/cobalt/cobalt diff --stat main -- ops/desk/deploy-step0.sh DEPLOY-HUB.md CARD.md` | empty: working files equal `main`, so the greps below read main | OK |
| 8 | `grep -n -E "lits=\|# P2\|why=\|…" ops/desk/deploy-step0.sh` | `337: lits=$(printf '%s\n' "$line" \| awk -F'\|' '{print $7}' …)` · `358: # P2: the check's stop line` · `382: … *) case "$ctip" in "$t"*) ;; *) why="its tip $t is not the row's code tip $ctip" ;; esac ;;` · `387: row "P2 check $n" …`. Matches the card's 358-387, literals 337, refusal 382 | OK |
| 9 | `grep -n -E "P2 EVERY CHECK" DEPLOY-HUB.md` | `58:- **P2 EVERY CHECK, COMMITTED** (L67). … and its `tip:` equals the row's code tip; …` | OK |
| 10 | `grep -n -E "^The code tip is\|^\| # \| branch\|^\|---\|---" CARD.md` | `44:\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` · `45:\|---\|---\|---\|---\|---\|---\|` · `47:The code tip is the `tip:` of the check's stop line … The last column is `held unfixed: 0` and `ready: YES` …` | OK |
| 11 | F2 red-first: `grep -n -E "xfail\|def test_o1_a…\|assert \"is not the row's code tip\"\|def test_a_check_report_whose_tip" <WT>/tests/ops/test_deploy_step0.py` | `246/247: def test_a_check_report_whose_tip_is_not_the_row_s_code_tip_fails` · `546: @pytest.mark.xfail(strict=True, …` · `548: def test_o1_a_fix_round_row_the_launcher_accepts_passes_p2` · `569: assert "is not the row's code tip" not in last_line(done), done.stdout`. By reading, main's line 382 makes the fix-round row end `… its tip <checked> is not the row's code tip <fixed>` (check RUNS O1): red on BASE. Controls (a)-(c) named with `FAILED STEP-0: P2 check 1 — …`; the no-fix-report control is the test at 247 | OK |
| 12 | F3 red-first: `grep -c -F "is an ancestor of the code tip" DEPLOY-HUB.md` (no backtick: bare-command rule) | `0` at main | OK |
| 13 | F4 red-first: same grep on `CARD.md` | `0` at main; `The last column is` hits only line 47 (check 10) | OK |
| 14 | F3 names the merge | row F3: "BEFORE writing this row the builder merges `main` into its branch, then re-reads line 58 and edits it as it stands. Touch line 58 only" | OK |
| 15 | Fence: `## NOT IN THIS JOB` and the F2-F4 files columns | F2 `deploy-step0.sh` + `test_deploy_step0.py`; F3 `DEPLOY-HUB.md` (line 58 only); F4 `CARD.md` (lines 44-45 and 47). NOT IN THIS JOB lists F1's `desk-launch.sh`, its test, `CARD.md` 44-45, and the F2-F4 files, and nothing else. `deploy-card.sh` (lines 141, 207-208) is F1's, already built at `c1746720`, not in this prompt's list and not an F2-F4 file (same note as r3 #13). Row counts agree: F1 + F2-F4 = 4 rows, F1-F4 named alike in the Rows block, the check asks and the fence | OK |
| 16 | No row adds a command or argument | NOT IN THIS JOB: "the column is a header value, not a new argument or command"; F2-F4 touch P2 logic, one test file and two text lines | OK |
| 17 | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | empty: clean | OK |
| 18 | `git -C /Users/cobalt/cobalt log -1 --format=%h -- <card>` | `b2a903d5`: committed | OK |
| 19 | `grep -c -F "«FILL" <card>` | `0` | OK |

## ISSUES
None.

PREFLIGHT DONE · card: launcher-fixround-21 · checks: 19 · fails: 0 · ready: YES
