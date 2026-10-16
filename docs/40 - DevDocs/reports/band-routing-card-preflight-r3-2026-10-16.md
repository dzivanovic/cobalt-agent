# Card 583 band-routing-1015 — preflight round 3 (read-only), 2026-10-16

Seat band-routing-preflight-r3 (Sonnet 5.5). Prompt 630. Card `prompts/2026-10-15/583-band-routing-card.md`, last commit `da345e0b`. Reads and greps only, no test run. Only round 2's three fails and the amend's own edits are checked.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | B6 lead and reason: `grep -c -E` of the answer's `Same row, inside the same fence: G5's SHADOW branch also admits <REPORT>.result (…never a link)` in the card (backticks as `.`, the hook bars a backtick) | `1`. The "Same row as B5 (brain answer, Q2 + issue 6)" attribution is gone | OK |
| 2 | B6 red cell: `grep -c -E` of `RED: the gate seat's write of its .result is refused today, passes after; a write to any other path is still refused (control).` in the card | `1`, the answer's words, no "GREEN on BASE and after" added | OK |
| 3 | B6 reason: `grep -c -F` of `2026-10-14 item 3: every build writes one structured result file. A routed build without it is a build report the gate can't read. A guard rule serving K2 runs by card in K5 with no word of his.` in the card | `1` | OK |
| 4 | the answer's whole row (lead, RED, control, `bare-guard.py joins the card's files.`) as one pattern in `reports/band-routing-answer-2026-10-16.md` | `1`: the answer row exists as quoted. The card splits it across cells (lead and reason, RED, files); the last sentence sits in the files cell, as round 2 accepted. `grep -x` cannot hold: a card row is one table line | OK (NOTE 2) |
| 5 | `git diff b8d2fcfa da345e0b -- <card>`, the `## NOT IN THIS JOB` hunk | one bar changed: `not the check arm (:1692-1729)` → `not the check arm (:1692-1729) except B5's :1724-1730`. The other bullets of that section are context lines, unchanged. The bar admits B5's `:1724-1730`; `:1749-1752` is outside `:1692-1729` | OK |
| 6 | ORDER, Read of `:41` | names "B1, B2 (1)-(2), B3 (1)-(8), B4, B5 and B6" for the RED quote on `BASE`, and the edit order "B1, B2, B4, then B3, then B5 and B6 (each red re-run before its edit)" | OK |
| 7 | CHECK ASKS, Read of `:63-71` | X6 asks B5 (routed worktree with only the untracked `SHADOW-INSTRUCTIONS.md` passes `check` and `preflight.sh`; non-routed refused); X7 asks B6 (`.result` admitted, any other path refused). Neither writes the label "B5" or "B6": they name them by content | OK (NOTE 1) |
| 8 | WHY (`:18`) and SOURCE OF TRUTH PER ROW (`:20`) | WHY: "Six rows and one RUN row". SOURCE OF TRUTH: ends `…; B5 reports/band-routing-answer-2026-10-16.md Q2 (…); B6 the same answer, Q2 + issue 6 (…)`. The label B5/B6 is in the SOURCE paragraph, not in the WHY sentence itself | OK (NOTE 1) |
| 9 | the drafter edits touch nothing else: `git log --oneline eddf923b..HEAD -- <card>` and the `git diff b8d2fcfa da345e0b` read whole | one commit, `da345e0b`. Seven hunks only: WHY "Four"→"Six"; SOURCE OF TRUTH + B5/B6; B6 lead; ORDER; the one NOT IN THIS JOB bar; X6; X7. Rows B1-B5, R3, DEPLOY PROOF, RECORDS, header: unchanged | OK |
| 10 | no other bar changed: `git diff b8d2fcfa da345e0b` on `## NOT IN THIS JOB` | only the check-arm bar differs (check 5) | OK |
| 11 | committed: `git diff HEAD --stat -- <card>` | prints nothing; the card is tracked, `git log` lists it at `da345e0b` | OK |
| 12 | placeholder: `grep -n -E "«\|TBD\|TODO\|XXX\|<fill"` of the card | no output | OK |
| 13 | `grep -n -E "^(BASE\|TIP):"` of the card | `7:BASE:` and `8:TIP:`, both empty (the desk's fill at launch, by design) | OK |
| 14 | build launch blockers: `ls /Users/cobalt/cobalt-wt` | no `band-routing-1015` worktree; none of the stale `deploy-*` entries belongs to this job | OK |

## ISSUES

1. NOTE (checks 7, 8): X6 and X7 do not write "B5" or "B6", and WHY's own sentence lists no rows; the labels appear in ORDER and the SOURCE OF TRUTH paragraph. Round 2 asked for one ask each: both exist.
2. NOTE (check 4): `grep -x -F` per line is not possible, the row is a table line; the comparison was by cell fragments. B6's control lacks "GREEN on `BASE` and after" because the answer lacks it (drafter decision 1, the answer file wins).
3. NOTE: `0e848919` (`:35`, `:50`) and `fad8bf8e` (`:79`) stay as session ids in the card text; not HEAD hashes (round 2 note 5).
4. NOTE: what blocks the build launch: nothing in the card. The desk fills `BASE` and `TIP` at launch (main after card 580's deploy, landed). No worktree or branch exists. The build runs on Opus (583 is a HIGH card on its own `BAND`).

PREFLIGHT DONE · card: band-routing-1015 · checks: 14 · fails: 0 · ready: YES
