## §0 Headline
- Re-preflight: 6 checks, 0 fails; the label is `aset` in all three places.
- Grok read NOT RUN: the desk's `bare-guard.py` refused every `grok` call from this seat (G7, `route: the desk launches`). The inputs are staged; the read is still owed.
- ESCALATE: 1.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff --numstat` | `DEPLOY-HUB.md` 2/2, `STANDING-LIST.md` 1/0. Other modified files (`.claude/settings.json`, reports) are outside the two and were dirty before the drafters. | OK |
| 2 | read 4.2 (line 137), STEP-5 (3) (line 162), row (line 149); `grep -c -F "same call again, then STEP-5" DEPLOY-HUB.md` | The same five steps in all three. Both stop rules present. grep → `0`. | OK |
| 3 | `grep -n -F -e "--kill"` on both files; `orphan-clean.sh` lines 75-83 | `--kill aset` at DEPLOY-HUB 137, 162 and STANDING-LIST 149. The script's label table has the one entry `aset`. Dry-run last lines match script lines 174 and 252. No `sleep`, `pgrep` or radar call in the new text. | OK |
| 4 | `grep -c -F -e` on the three allow strings in DEPLOY-HUB | `sh …/ops/desk/*`, `date*`, `launchctl print gui/501/*` are on the launch line (line 11). | OK |
| 5 | `git diff --numstat` for DEPLOY-HUB | `2 2`: only 4.2 and STEP-5 (3) differ from HEAD. | OK |
| 6 | read the row; `grep -n -i -e DRAFT -e "awaiting his yes" STANDING-LIST.md` | Hits at lines 8, 172, 173 only ("first draft", other rows). None in row 149. The row names who, where, the precondition and the exclusions. | OK |

## GROK READ
Not run. `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(…/scratch/tribunal-bars-0920/**)" -p "…"` was refused by the PreToolUse hook: `bare-guard.py: route: the desk launches` (`ops/desk/bare-guard.py:75`, rule G7). `grok --version` was refused the same way. `bare-guard.py:756` exempts only a prompt file named `<n>-<name>-tribunal[-r<n>].md`; this prompt (`275-kill-row-repreflight-grok-read.md`) does not match. I did not retry in another spelling.

Staged and ready, `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/kill-row/`: `orphan-clean.sh` 12334 B, `STANDING-LIST.md` 40686 B, `DEPLOY-HUB.md` 58628 B (each `wc -c` equal to its original), `DIFF.md` (the two hunks and the row; the 4.2 line is shortened with `...` where its unchanged tail follows).

## FILE-CHECKED
No Grok claims to check.

## ISSUES
- ESCALATE 1: the Grok read of the DEPLOY-HUB change needs a seat the guard lets launch `grok`: a prompt named like a `-tribunal.md` hub under `prompts/20*/`, or the desk running the one call itself with the staged folder above. Nothing else is blocked.
- L32: the staged files carry no personal content.
- Nothing was edited in either hub or standing-list file; no commit was made.

FAILED: Grok read not run — bare-guard G7 refused `grok` for this prompt's seat · checks: 6 · fails: 0
