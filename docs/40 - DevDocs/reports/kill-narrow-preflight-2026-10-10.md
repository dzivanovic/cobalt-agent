# kill-narrow-preflight — card 284 (2026-10-10)

Read-only. Card `prompts/2026-10-10/284-kill-hub-card.md` at HEAD `a12e69ad`, last commit touching it `36c94606`.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <card>` | empty (card also not in `git status` M list) | OK |
| 2 | `git diff da7d2dd8 HEAD -- <card>` | hunks start at line 16 (rows) and the TEXT blocks; lines 1-11 (JOB, LADDER, BRANCH, WORKTREE, BASE `6fe8d690`, TIP `91c48f36`, REPORT, CHECK REPORT, HOUSE B `as needed`, DB, RULINGS `R855`) not in any hunk | OK |
| 3 | brain point 1, `--kill` ONCE at 4.2 after the loop: card `:32` "AFTER the loop, ONCE, if `com.cobalt.aset` is in `<restart set>` … (3) `sh …/orphan-clean.sh --kill aset` once" | present | OK |
| 4 | point 2, exit 1 or `FAILED: <pid> survived KILL` → STEP-5, no second kill: `:32` "or exit 1 (`REFUSED:` / `UNVERIFIED:` / `FAILED: <pid> survived KILL`) → no second kill, STEP-5 (nothing merged)" | present | OK |
| 5 | point 3, pids under `## RECORDS` and a `DECISION 0` named line: `:32` "its pids into `## RECORDS`" and "`DECISION 0: aset orphan <pids or the line> — FOR DEJAN`" | present | OK |
| 6 | point 4, STEP-5 (3) dry run ONLY, no `--kill`: `:44` "(dry run ONLY, no kill)"; K2 NEW holds no `--kill` | present | OK |
| 7 | point 5, STANDING-LIST row names 4.2 only: `:50` "ONLY in the deploy hub, at 4.2 once after the per-resident bootout loop" … "never standing outside 4.2 (STEP-5 runs the dry run only)" | present | OK |
| 8 | `grep -n -F -e "--kill" <card>` over the TEXT blocks (`:26-50`) | K1 OLD `:26` none; K1 NEW `:32` once (4.2 step 3); K2 OLD `:38` none; K2 NEW `:44` none; K3 `:50` two (the row's command string and its step (3), both 4.2). Other hits `:15 :19-21 :29 :71 :72 :79 :80 :82` are WHY, rows, heading, CHECK ASKS, RECORDS prose | OK |
| 9 | label: `grep -n -E "orphan-clean.sh\|aset" ops/desk/orphan-clean.sh`; `:2-3` usage `<label>` / `--kill <label>`, `:76-82` `aset)` is the only label, `:82` "not in the label table (aset)" | the TEXT uses `aset` everywhere; `--kill com.cobalt.aset` 0 hits in the card's TEXT | OK |
| 10 | orphan-clean anchors: `:174` `none found`, `:250` `WOULD KILL`, `:252` `dry-run · verified`, `:296-297` `FAILED … survived KILL` + `exit 1`, `:59-60` REFUSED exit 1 | all as named | OK |
| 11 | DEPLOY-HUB anchors `git show 6fe8d690:` (read from the saved output): `:137` starts `4.2 for each`, `:162` `- (3) THE RESTORE`, `:163` (4), `:164` (5) "STEP-5 is never entered twice", `:175` STEP-7 (3); K1 OLD and K2 OLD match those lines by eye | OK | OK |
| 12 | STANDING-LIST at `6fe8d690`: `:148` `Bash(launchctl print gui/501/*)`, `:149` `cobalt.sh status` | as the card says | OK |
| 13 | line counts: DEPLOY-HUB at BASE 181, STANDING-LIST at BASE 220; card pins 181 / 221 / 220 | 181 and 220 proven; 221 = 220 + the one inserted line. The card pins line counts only, no byte counts | OK |
| 14 | `grep -n -E "«FIL[L]\|OpenAI\|Sol \(" <card>` | exit 1, no hit (no placeholder; no OpenAI seat; `:82` names house A Grok, R920 / R955) | OK |
| 15 | new commands: TEXT uses `orphan-clean.sh` (CLASS (a), `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`) and `date`; no `sleep`, `pgrep`, radar call (`:58` NOT IN THIS JOB repeats R411 / R412) | none new | OK |
| 16 | D1-D6 in `kill-narrow-rows-2026-10-10.md` `## DECISIONS`: D1 and D2 and D3 gone by the narrowing; D4, D5, D6 fixed by new TEXT K1; each states which. The check report made no fixes (`## FIXES` none), so each defect maps to a row, none left unmapped; O4 stays out of scope | OK | OK |
| 17 | `grep -c` of the card's row greps against the TEXT: `ORPHAN-CLEAN, aset only` in K1 NEW once; `survived KILL` once (K1 NEW); `(dry run ONLY, no kill)` once (K2 NEW); `the kill sequence:` once (K1 NEW only); `not held DOWN` 0; `orphan-clean.sh --kill aset` once in K1 NEW (none in K2 NEW), once in K3 | agree with the rows (read, not run on the hub files) | OK |

## ISSUES
- NOTE (stale, `:80`): RECORDS says "orphan-clean.sh --kill aset" is at `DEPLOY-HUB.md:137`, `:162` and that the staged copies under `…/scratch/tribunal-bars-0920/kill-row/` differ from main by exactly K1, K2, K3. Those copies are the round-1 text; K2 NEW now holds no `--kill`. K1's row says `:137` only. A builder must take the TEXT blocks, not the staged copies.
- NOTE (stale, `:71-74`): CHECK ASKS X2 ("STEP-5 (3) keeps residents down") and X5 ("not held DOWN" hold-down, `aset: <UP|DOWN>`) describe the dropped round-1 K2. X1 and X3 still fit; X4 (`2 2` / `1 0` numstat) still fits. The desk should trim X2 and X5 before the check, or the check will chase a hold-down that no longer exists.
- NOTE (K1): sequence step (1) "clean … go on" and step (5) "go on (the agent step below, then 4.3)" — a clean step (1) goes on to the agent step by the same reading; no defect, the check can confirm.
- NOTE (seats): the earlier check ran Sol in seat A and Grok in seat B (`kill-hub-row-check-2026-10-10.md` RECORDS); the card's `:82` says house A Grok. R920 / R955 say Grok is house A; the launcher decides the order.
- NOTE: `git status` shows other untracked/modified docs, none touching the card, DEPLOY-HUB or STANDING-LIST. `tests/ops/test_hub_lines.py` and the hub-file `grep -c` markers were not run (read-only seat).

PREFLIGHT DONE · card: kill-hub-row-1010 · checks: 17 · fails: 0 · ready: YES
