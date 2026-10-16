# Card 648 `check-scratch-1016` (CHECK, K5) — preflight round 2, 2026-10-16 (`date` not run: not on the allow list's need)

Read only. Card `prompts/2026-10-16/648-check-scratch-check-card.md`, amended by commit `2d0cce8a` after round 1 (`1a093e2d`). BASE `b84cca9a`, TIP `85eade55`, both resolve with `git rev-parse --short=8`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `grep -n -E "^(JOB\|LADDER\|CLASS\|INSTALL\|BRANCH\|WORKTREE\|BASE\|TIP\|REPORT\|CHECK REPORT\|HOUSE A\|HOUSE B\|BAND\|DB\|RESTARTS\|RULINGS):"` on the card | all 16 header lines present (`:1-16`), same as round 1 | OK |
| 2 | Read `## ROWS` | CS-1 and R2 RUN rows, CS-1 carries the RED and the control; unchanged but R2's cell | OK |
| 3 | Read row SC1 | unchanged | OK |
| 4 | `grep -n -E "«FIL[L]\|«INSTAL[L]\|TBD\|TODO\|XXX"` on the card | no output | OK |
| 5 | `grep -n -i "opus"` on the card | `:20` `… house B only if the hub seats it (next flow change 1); the Opus seat is the check (the brain's condition 1); no re-check af…`. `:57` (X7) carries the same sentence (diff below). FAIL 5 closed, part 1 | OK |
| 5a | house B wording vs header | `:12` `HOUSE B: as needed`; `:20` and X7 `house B only if the hub seats it`. The "Both outside houses run" sentence is gone from both places; the header and the text agree | OK |
| 5b | R2 red-first cell | `RUN — asserts nothing, so no RED and no control: only CS-1 carries a RED and a control; quote the output` | OK |
| 5c | launch line | `:20` `Before the launch, confirm the check on `band-routing-1015` has ended and that no other Grok hub runs (L15).` present | OK |
| 6 | `grep -n -F "deploy-gate" ops/desk/gate.sh` | `:2`, `:29`, `:136` (parsed), `:147`; `gate.sh check-scratch-1016 offline --deploy-gate` is valid | OK |
| 7 | `grep -n "^\| R1532 " reports/cto-2026-10-15.md` | `:102` `R1532 … HIS RULING · APPROVED: routing B …` | OK |
| 8 | `git grep -n -F "def test_cs1_" ops/check-scratch-1016 -- tests/ops/test_stage_set.py` | `:359 :419 :423 :427 :431 :435 :439`, seven | OK |
| 9 | `git grep -n -F "assert done.returncode == 0"` (same ref and file) | `:102 :213 :244 :364`; `:364` is the line CS-1 names | OK |
| 10 | `git grep -n -F "clearable" … ops/desk/stage-set.sh` | `:90` comment, `:92` definition, `:130` the one call | OK |
| 11 | `git grep -n -F "rm -r" … ops/desk/stage-set.sh` | `:151 rm -rf "$dest"`, `:158 rm -rf -- "$dest"` | OK |
| 12 | tip line numbers the card cites (`:8`, `:50-54`, `:92-124`, `:126-137`, `:157`) | unchanged from round 1: the amend touched the card only, `git diff --name-only --no-renames b84cca9a 85eade55` is `ops/desk/stage-set.sh`, `tests/ops/test_stage_set.py`; `git diff --stat 85eade55 0605334f -- . ":(exclude)docs"` prints nothing | OK |
| 13 | `git log --oneline b84cca9a..85eade55` | `85eade55`, `3f0fd60e` (two commits) | OK |
| 14 | `git diff HEAD --stat -- <card>` | prints nothing; the card is committed (`2d0cce8a`) and its diff against HEAD is empty (as found) | OK |
| 15 | `git diff 1a093e2d HEAD -U0 -- <card>` | three hunks only: `:20` (WHY: the "Both outside houses run" sentence replaced by "House A (Grok) runs inside this check, house B only if the hub seats it …; the Opus seat is the check …" and the added "Before the launch, confirm …" sentence), `:30` (R2 red-first cell), `:57` (X7). Nothing else changed | OK |
| 16 | `ls -ld …/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/check-scratch-1016-check` | `No such file or directory`: nothing to clear. (`SCRATCH="$WT/agy-trial/scratch"`, `stage-set.sh:40`) | OK |

16 checks as in round 1 are rows 1-4, 6-14, 16 plus 15 (the diff), with 5 split in 5, 5a-5c.

## ISSUES
- NOTE 1: what blocks `desk-launch.sh check "<card>"`: nothing in the card (committed, diff against HEAD empty, no `«FILL`, scratch folder absent). One thing not mine to close: `band-routing-1015-check` still exists in the scratch root (mtime Oct 16 11:56); the card's launch line tells the desk to confirm that check has ended and that no other Grok hub runs (L15), and I did not check running processes.
- NOTE 2: `CARD.md` on `main` has no `BAND` row (round 1 NOTE 4); `BAND: MID` stays harmless until band-routing deploys.
- NOTE 3: no test was run, no mutation tried; every RED and green in the rows stays the builder's, UNPROVEN until the check quotes it (L70).
- NOTE 4: the first header line of this report says `date` not run; the time is not recorded.

PREFLIGHT DONE · card: check-scratch-1016-check · checks: 19 · fails: 0 · ready: YES
