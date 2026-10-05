## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt merge-base --is-ancestor 5fb0ddf5 main` | no output, exit 0 | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse --verify ops/launcher-fixround-1005` | `fatal: Needed a single revision` (exit 128: branch is new) | OK |
| 1c | `ls /Users/cobalt/cobalt-wt/launcher-fixround-1005` | `No such file or directory` | OK |
| 1d | card header lines 6, 8, 10 | `TIP:`, `CHECK REPORT:`, `HOUSE B:` all empty | OK |
| 1e | card rows L1–L6 | each reads `· SHIPPED, not rebuilt`; line 16: "they are NOT rebuilt" | OK |
| 2a | `grep -n "^| R412 " …/cto-2026-10-05.md` | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|` | OK |
| 2b | `git log -1 --format=%h -S"\| R412 \|" -- …/cto-2026-10-05.md` | `b3583b28` | OK |
| 2c | card header `RULINGS:` vs draft report | card holds `2026-10-05 R412` only; draft report says `R376, R412` | FAIL (see ISSUES 2) |
| 3a | `git show 5fb0ddf5:ops/desk/desk-launch.sh`, lines 746-748 | 746 `ltip=$(printf '%s\n' "$clast" \| sed -n 's/.* tip: \([0-9a-f]*\).*/\1/p')` · 747 `[ -n "$ltip" ] && { [ "$ltip" = "$ctip" ] \|\| [ "$ltip" = "$shead" ]; } \` · 748 `\|\| refuse "deploy $sbranch: the check's tip '$ltip' is neither the code tip $ctip nor the branch head $shead — the check is not clean: $clast"` | OK |
| 3b | same, lines 749-757 | 749 comment `# P3: …`; 750-752 `bhead=… rev-parse --short=8`, refuse `the head moved: $bhead`; 753-754 `merge-base --is-ancestor "$ctip" "$shead"` refuse `the code tip … is not an ancestor`; 755-757 `moved=$(git … diff --stat "$ctip" "$shead" -- . ':(exclude)docs')`, refuse `the head adds more than docs` | OK |
| 3c | test file at BASE; `grep -n` on the file (`git diff --stat 5fb0ddf5 main` on it and the script is empty, so main = BASE) | `tests/ops/test_desk_launch_prechecks.py` exists; `430:def break_other_tip(desk):`, `432:… is neither the code tip {desk.tip} nor the branch head {desk.head} …`; `141 built_line`, `145 write_build_report`, `185 ship` | OK |
| 4a | red on BASE, read from 746-748 | check tip an earlier ancestor ≠ `$ctip`, ≠ `$shead` → line 748 refuses `neither the code tip` | OK |
| 4b | negative control (a): check tip not an ancestor (`OTHER_TIP`, or a main-only commit) | BASE: not equal to either → `neither` refusal. Fixed script: `merge-base --is-ancestor` fails → still refused | OK |
| 4c | negative controls (b) build REPORT last line lacks `tip: <code tip>`, (c) build REPORT uncommitted | BASE: the check tip is neither value → `neither` refusal for the stated reason. Fixed script: the new proof fails → refused | OK |
| 5a | row changes only 746-748 and its test file; adds no new command or argument | The row says so, but the new proof needs the build REPORT's path, and a deploy launch has none. Deploy card header `REPORT:` is the deploy report (`CARD.md` header table; `write_deploy` in the test fixture); `## SHIPS` columns (`CARD.md`) hold no build report; `DEPLOY-HUB.md` names no build-report field (`grep -n "build report\|BUILT ·\|REPORT"` hits only the deploy REPORT). The build report lives on the job card and in the job's worktree. Lines 746-748 alone cannot find it. | FAIL (see ISSUES 1) |
| 6a | `git diff --stat -- <card>` | empty | OK |
| 6b | `git log -1 --format=%h -- <card>` | `de5f99aa` | OK |
| 6c | `grep -c -F "«FILL" <card>` | `0` | OK |

## ISSUES
1. Check 5a: row F1 does not say where the deploy launch finds "the card's build REPORT". The deploy card's `REPORT` is the deploy report; the `## SHIPS` table has no build-report column; the hub names none. A fix confined to lines 746-748 with no new argument cannot read a file it cannot locate. The card must name the derivation (for instance a build-report path column in `## SHIPS`, or a fixed glob under the branch's `docs/40 - DevDocs/reports/` read with `git show <branch head>:<path>`) and widen the row's lines or files to match, or his R412 reading of "no new argument" must be settled first. The desk decides; no workaround is guessed here.
2. Check 2c: the card's `RULINGS:` line is `2026-10-05 R412`; the draft report says `R376, R412` were set. R376 (his small-fix ruling the row cites) is not in `RULINGS`, so the launch gate L1 does not prove it. Add it if the desk wants it bound, or correct the draft report.

PREFLIGHT DONE · card: launcher-fixround-21 · checks: 18 · fails: 2 · ready: NO
