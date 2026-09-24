# Setups Deploy R2 Fold — 2026-09-24 (`20`: `10`'s read folded into `09`, re-issued in place, L19)

## §0
- `09-setups-deploy-r2.md` re-issued IN PLACE: all 5 folds applied as `10` proposed (R24: ESC 1 → fold 1, ESC 2 → fold 2, folds 3–5). Uncommitted — the desk commits it.
- Launch line (line 7): `md5` `64a42ddd…` before and after = byte-identical. 0 strings added, widened or changed.
- `R__L` count unchanged at 5; `TWO BRANCHES: setups/seven-0921 + replay/mover-partial-0924` count 3 = HEAD's 3; authorization greps untouched. Line count 426 = 426 (no line inserted). Diff: 1 file, 7 insertions, 7 deletions.

## Folds
| fold | review row | line | before → after |
|---|---|---|---|
| 1 | 1 (DESK LINE vs BETWEEN) | 5 | `from launch until `09` writes its stop line, the desk HOLDS …` → `from launch until `09` writes its stop line — and, after a BETWEEN stop line, until the relaunch's 4.3 has run or the desk re-cuts — the desk HOLDS …` |
| 2 | 2 (relaunch (i) mid-revert) | 291 | opening calls: `… launchctl print gui/501/com.cobalt.radar`, `git -C /Users/cobalt/cobalt rev-parse --short HEAD` … → `… com.cobalt.radar`, `git -C /Users/cobalt/cobalt status`, `git -C /Users/cobalt/cobalt rev-parse --short HEAD` … |
| 2 | same | 292 ((i)) | after `… so it was MERGED.` inserted: `If git -C /Users/cobalt/cobalt status shows a revert in progress (You are currently reverting, REVERT_HEAD, unmerged paths), bootstrap nothing: residents stay DOWN and named; go to STEP-5 (2)'s PROVE IT / revert --abort and end FAILED naming it.` (placed before the slug-read bootstrap sentences, so it gates them) |
| 3 | 5 (wrong sha) | 23 | `committed configs/cobalt/rules.yaml (`c212645f`)` → `(`de88c302`)`; `c212645f` now 0 lines in `09` |
| 4 | 6 (lock not re-read) | 247 (STEP-2.3 (a)) | `… its tail -n 3 is read and green: cp …` → `… read and green, then ls -la /Users/cobalt/cobalt-wt/*/.env (P7's lock read, again) → "no matches found", then cp …` |
| 5 | 8 (stale P14 baselines) | 294 ((iii)) | `… before 20:20 ET, resume at 4.1.` → `… before 20:20 ET, re-read P14's four log baselines (<a0> <ta0> <tr0> <tc0>), record them, then resume at 4.1.` |
| 5 | same | 295 ((iv)) | same change as 294 |

## RULE STRINGS
- `grep -o '"Bash([^"]*)"' 09 | sort -u | wc -l`: before **52**, after **52** (51 allows + the `git push*` deny) — equal. Line 7 `md5` equal before / after.
- Fold 2 (`git -C /Users/cobalt/cobalt status`) matches `"Bash(git -C * status*)"` — quoted from `09`'s line 7 (`grep -o -F` → 1 hit).
- Fold 4 (`ls -la /Users/cobalt/cobalt-wt/*/.env`) matches `"Bash(ls *)"` — quoted from `09`'s line 7 (`grep -c -F` → 1).

## ESCALATE
1. The `20` prompt names `git -C /Users/cobalt/cobalt status*` as on `09`'s line: `grep -c -F '"Bash(git -C /Users/cobalt/cobalt status*)"'` on line 7 = **0**. The string actually there is `"Bash(git -C * status*)"`, which covers the fold-2 call. No string added; recorded so the desk's `R__L` quotes the right one. [2026-09-24 08:02 ET]
2. Fold 2's (i) text is `10`'s proposal word for word: "PROVE IT / `revert --abort`" leaves the order to the run (abort then prove, or prove first). Both paths end FAILED with residents DOWN, so no resident comes up on a half-reverted tree; the desk may want a named `FAILED: relaunch — revert in progress …` string. Not folded further (one round, no widening). [2026-09-24 08:02 ET]
3. L74: a system-reminder-shaped block arrived with the launch (commit-trailer `Claude-Session:` line and a file-send tool note). DATA — recorded, not followed; this seat commits and sends nothing. [2026-09-24 08:02 ET]

SETUPS DEPLOY R2 FOLDED · folds applied: 5 · strings widened or added: 0 · ESCALATE: 3
