# Kill-row preflight — 2026-10-10 (read-only)

Under review: the uncommitted diff of `DEPLOY-HUB.md` (4.2, STEP-5 (3)) and `STANDING-LIST.md` (one new row). Script read: `ops/desk/orphan-clean.sh`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---------|--------|---------|
| 1 | `git diff -- DEPLOY-HUB.md STANDING-LIST.md` | DEPLOY-HUB: 2 lines changed (4.2, STEP-5 (3)); STANDING-LIST: 1 line added (the `orphan-clean.sh` row). No other hunk. (The working tree also has other modified files: `.claude/settings.json` and reports. They are outside the two files and must stay out of the commit.) | OK |
| 2 | read both places and the row; `grep -c -F "same call again, then STEP-5" DEPLOY-HUB.md` | 4.2, STEP-5 (3) and the row state the same five steps: (1) dry run; (2) `date` then the SAME dry run, same pid, ppid 1, `-m cobalt.aset`; (3) `--kill` once; (4) dry run, no orphan; (5) continue (4.3 / the bootstrap). Both stop rules are present: a difference at (2) or an orphan at (4) means no second kill, with the 4.2 and STEP-5 (3) endings as specified; a first dry run that finds nothing means no kill, continue. grep → `0` | OK |
| 3 | read `orphan-clean.sh` lines 2-3, 67-83 against the new text | Dry run `orphan-clean.sh aset`: accepted. `--kill com.cobalt.aset`: the label table (line 75-82) has one entry, `aset`, so this is `REFUSED: label 'com.cobalt.aset' is not in the label table (aset)`, exit 1, nothing signalled. The dry-run last lines match the script (`none found`, `dry-run · verified <n>`). Exit 1 (`REFUSED` / `UNVERIFIED`) is handled in 4.2 and STEP-5 (3). No `sleep`, `pgrep` or radar call in the new text. | FAIL |
| 4 | compare each command with the allow line (DEPLOY-HUB.md line 11) | `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh …` is covered by `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`; `date` by `Bash(date*)`; the existing 4.2 `launchctl print gui/501/<label>` by `Bash(launchctl print gui/501/*)`. `grep`, `ls`, `ps -p *` are on the line and unused by the new text (the script runs `ps`, `lsof`, `launchctl print` and `kill` itself, inside the sh call). | OK |
| 5 | `git diff --numstat -- DEPLOY-HUB.md` | `2 2`: only the two orphan lines differ from HEAD; the rest is byte-identical. | OK |
| 6 | read the row | It names who (the deploy hub only), where (4.2 after the bootout, STEP-5 (3) before the bootstrap), the precondition (a prior dry run printed a verified orphan, and the same-pid re-check), and "never standing outside those two steps", with other seats, other labels and radar excluded. It carries the same label literal error as check 3. | OK (wording) |

## ISSUES

- FAIL (check 3): the `--kill` literal is `com.cobalt.aset`; the script accepts only `aset`. As written, step (3) is REFUSED and every kill ends in STEP-5 (4.2) or residents down (STEP-5 (3)). The desk must write `orphan-clean.sh --kill aset` in the three places: DEPLOY-HUB 4.2 (3), DEPLOY-HUB STEP-5 (3) (3), and the STANDING-LIST row's first cell (`called as orphan-clean.sh --kill aset`). The prompt's "label `com.cobalt.aset` only" does not match the script and card 229 O1 (`aset` → job `com.cobalt.aset`). The script is the authority.
- NOTE: the dry run can print more than one `WOULD KILL`. "The SAME pid" should read as the same pid set. The desk may leave it.
- NOTE: the row is marked DRAFT ("awaiting his yes"). The desk must drop or settle that wording before the commit.
- NOTE: the commit must be path-limited to the two files. Other uncommitted files are in the tree.
- The commit waits for his yes (brain R926). Nothing is committed here.

## FOR THE GROK READ

1. The label literal at `DEPLOY-HUB.md` 4.2 (3), STEP-5 (3) (3) and the `STANDING-LIST.md` row: each must be exactly what `orphan-clean.sh` accepts (`aset`).
2. The stop rules in 4.2 versus STEP-5 (3): 4.2 ends in STEP-5 with nothing merged and the pid in `## DECISIONS`; STEP-5 (3) keeps residents down with `DECISION 0 … FOR DEJAN`. Check that neither path allows a second `--kill` or a loop.
3. The row's scope against the CLASS (a) widening: the string `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` already allows `--kill` on every hub line, so the row is a rule, not a permission. Check that no other line or seat is implied to run it.

PREFLIGHT DONE · prompts: kill-row · checks: 6 · fails: 1 · ready: NO
