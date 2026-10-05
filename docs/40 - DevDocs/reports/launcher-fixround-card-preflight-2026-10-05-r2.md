## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5fb0ddf5 main` | no output, exit 0 | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/launcher-fixround-1005` | `fatal: Needed a single revision` (exit 128: branch is new) | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/launcher-fixround-1005` | `No such file or directory` | OK |
| 1d | `grep -n -E "^(RULINGS\|BASE\|BRANCH\|WORKTREE\|TIP\|CHECK REPORT\|HOUSE B):"` on the card | `3:BRANCH: ops/launcher-fixround-1005` · `4:WORKTREE: launcher-fixround-1005` · `5:BASE: 5fb0ddf5` · `6:TIP:` · `8:CHECK REPORT:` · `10:HOUSE B:` · `12:RULINGS: 2026-10-05 R412` (TIP, CHECK REPORT, HOUSE B empty) | OK |
| 1e | `grep -c -F "SHIPPED, not rebuilt"` on the card | `6` (L1–L6 each marked; line 16 says "they are NOT rebuilt") | OK |
| 2a | `grep -n "^\| R412 " …/cto-2026-10-05.md` | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` | OK |
| 2b | `git log -1 --format=%h -S"\| R412 \|" -- …/cto-2026-10-05.md` | `b3583b28` (committed) | OK |
| 3a | `git diff --stat 5fb0ddf5 main -- ops/desk/desk-launch.sh ops/desk/deploy-card.sh "docs/40 - DevDocs/prompts/CARD.md" tests/ops/test_desk_launch_prechecks.py` | empty: main = BASE for all four files, so the reads below are BASE | OK |
| 3b | `git show 5fb0ddf5:ops/desk/desk-launch.sh`, line 714 | `carry=$(printf '%s\n' "$srow" \| awk -F'\|' '{print $7}')` (field 7; the new `frep=` field 8 goes after it) | OK |
| 3c | same, lines 733-736 | `{ [ -n "$(git -C "$REPO" log -1 --format=%H -- "$crep")" ] && git … diff --quiet -- "$crep" && git … diff --cached --quiet -- "$crep"; } \|\| refuse "deploy $sbranch: the check report is not committed or differs from its commit — commit $crep"` (the committed-and-unmodified test the card copies) | OK |
| 3d | same, lines 746-748 | 746 `ltip=$(printf '%s\n' "$clast" \| sed -n 's/.* tip: \([0-9a-f]*\).*/\1/p')` · 747 `[ -n "$ltip" ] && { [ "$ltip" = "$ctip" ] \|\| [ "$ltip" = "$shead" ]; } \` · 748 `\|\| refuse "deploy $sbranch: the check's tip '$ltip' is neither the code tip $ctip nor the branch head $shead — the check is not clean: $clast"`; 749-757 are P3 (`bhead`, `merge-base --is-ancestor "$ctip" "$shead"`, `diff --stat … ':(exclude)docs'`), unchanged by the row | OK |
| 3e | `grep -n -E "ships=\"\|check report \| its stop\|^\|---\|---" ops/desk/deploy-card.sh` | `141:    ships="$ships\| $n \| \`$branch\` \| \`$ctip\` \| \`$head\` \| \`$creport\` \| \`held unfixed: 0\` and \`ready: YES\` \|$nl"` · `207:\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` · `208:\|---\|---\|---\|---\|---\|---\|` (6 cells each; card names 141, 207, 208) | OK |
| 3f | `grep -n -E "^\| # \| branch\|^\|---\|---\|^## SHIPS"` on `prompts/CARD.md` | `44:\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` · `45:\|---\|---\|---\|---\|---\|---\|` (the other `\|---\|` hits are 12, 37, 90: other tables). The card's fence names lines 44-45 and nothing else in that file (card lines 28, 33, 34, 52: no "line 44" alone left) | OK |
| 3g | test file at BASE | `tests/ops/test_desk_launch_prechecks.py` exists: `73:class Desk:` · `141: def built_line` · `145: def write_build_report` · `185: def ship` · `430:def break_other_tip(desk):` · `432: … is neither the code tip {desk.tip} nor the branch head {desk.head} …`. The card's helper names all exist | OK |
| 4a | red test on BASE, by reading 746-748 | a row whose check tip is an ancestor of the code tip: `$ltip` ≠ `$ctip`, ≠ `$shead` → line 748 refuses `neither the code tip`. The test is red on BASE | OK |
| 4b | negative controls (a) empty `fix report` cell, (b) report last line lacks `tip: <code tip>`, (c) report uncommitted | on BASE the check tip is neither value → line 748 refuses `neither the code tip` (green for the stated reason; BASE has no `frep`, so the cell is ignored). On the fixed script the new proof (non-empty, last line, committed) fails → still refused | OK |
| 4c | negative control (d) check tip not an ancestor of the code tip | on BASE the check tip is neither value → same refusal. On the fixed script `merge-base --is-ancestor "$ltip" "$ctip"` fails → refused | OK |
| 4d | the "no `fix report` column" test | a row of today's shape: `$7` = literals, `$8` empty; `ltip` = `ctip` or `shead` passes at 747 on BASE and after; the new proof runs only when `ltip` is neither | OK |
| 4e | does the 7th cell break other SHIPS parsers? `grep -rn -F "its stop line must carry" ops tests` | `desk-launch.sh:698,730`; `deploy-card.sh:207`; `test_desk_launch_recut.py:102`, `test_deploy_step0.py:165`, `test_hub_lines.py:192`, `test_desk_launch_prechecks.py:173`. The tests write their own fixture headers; none reads the script's or `CARD.md`'s. The launcher reads `$3`–`$7` and a 7th cell is `$8`, so rows of six cells and rows of seven both parse | OK |
| 5a | the rows change only the files they name | F1 files: `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py`, `ops/desk/deploy-card.sh`, `docs/40 - DevDocs/prompts/CARD.md` (44-45). `## NOT IN THIS JOB` names the same lines (714 and the new `frep=`, 746-748, 141, 207-208, 44-45) and fences every hub file | OK |
| 5b | no new command or argument (his R411, R412) | the fix uses `git merge-base --is-ancestor` (already at line 753), `ship_cell`, `grep`/`tail`; the `fix report` is a header value (card line 33: "the column is a header value, not a new argument or command"). R411 (cto-2026-10-05.md:107): "a new command stops the draft" — none added | OK |
| 6a | `git -C /Users/cobalt/cobalt diff --stat -- <card>` | empty | OK |
| 6b | `git -C /Users/cobalt/cobalt log -1 --format=%h -- <card>` | `e8fa0219` | OK |
| 6c | `grep -c -F "«FILL" <card>` | `0` | OK |

## ISSUES
None. Round 1's two FAILs:
- Round 1 issue 1 (no way to find the build REPORT from a deploy launch): fixed by the amends. The report is now the SHIPS row's `fix report` cell (`frep`, field 8), checked at line 714 plus the new test; no other file needs to be read.
- Round 1 issue 2 (`RULINGS` held R412 only, while the draft report said `R376, R412`): the card still holds `2026-10-05 R412` only. Not a FAIL now: R376's row (`cto-2026-10-05.md:49`) ends `APPLIED: LAWS L75 07:33`, not `APPROVED`, so binding it in `RULINGS` would make the L1 gate refuse the launch. The card cites R376 as its cause in prose only. The stale `R376, R412` line is in the draft report, a record, and is left.

PREFLIGHT DONE · card: launcher-fixround-21 · checks: 24 · fails: 0 · ready: YES
