# Card 641 `check-scratch-1016` — preflight round 2

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | Read card 641: `test_cs1_control_no_prior_card_copy_is_refused` in CS-1 | present: "`dest/files/` holds no `*-card.md`; exit 1; stderr starts `REFUSED: the dest is not empty: <dest>`; `snapshot(dest)` equal before and after" | OK |
| 2 | same control named in `## ORDER` and `## CHECK ASKS` (X2) | ORDER: "the six controls named GREEN (the five above and `test_cs1_control_no_prior_card_copy_is_refused`)"; X2: "no card copy at all (`test_cs1_control_no_prior_card_copy_is_refused`)" | OK |
| 3 | CONTROLS text | "CONTROLS (six; all stage the SECOND card, `02-x-job-fr-card.md`, never the first …" | OK |
| 4 | `git -C /Users/cobalt/cobalt show main:ops/desk/stage-set.sh`, line 8 | line 8: `# fifo, .git or .env anywhere in it; its files/<card name> a version of the card committed on main,`; card now cites `:8` (was `:6-8`) | OK |
| 5 | `-card.md`-count sentence in `## NOT IN THIS JOB` | present: "The `-card.md` count is over the whole of `files/` … fails closed; accepted under option 1, named for the check." | OK |
| 6 | `git -C /Users/cobalt/cobalt log -p dc688b32..HEAD -- <card>` | one commit, `c84acdf6`, 4 insertions, 3 deletions: only the `:8` citation, the CONTROLS text and sixth control, the ORDER line, the count sentence, the X2 text | OK |
| 7 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <card>` and `git status --short -- <card> ops/desk/stage-set.sh` | nothing printed: committed, empty diff against HEAD | OK |
| 8 | `grep -n "«\|FILL\|TODO\|TBD\|XXX\|<fill" <card>` | line 7 `BASE: «FILL: …»` (the desk's), and line 58 (`## RECORDS`) holds the literal `«FILL»` in prose: "`BASE` is the desk's `«FILL»`" | FAIL |

## ISSUES
- FAIL (check 8): `desk-launch.sh build` refuses a card while `grep -n '«FILL' "$card"` matches (`desk-launch.sh:994-995`, "incomplete card: the «FILL tokens listed above still stand"). Line 58 of the card holds `«FILL»` in prose, so the launch stays refused after the desk fills line 7's BASE. Fix: drafter rewords line 58 without the `«` character (e.g. "`BASE` is left for the desk to fill").
- NOTE: what blocks `desk-launch.sh build "<card>"` today: (1) `BASE: «FILL…»` on line 7, which is the desk's to fill; (2) the `«FILL` text on line 58, which the desk cannot fix without editing the prose (the FAIL above). Nothing else was seen. I did not run the launcher, and I did not re-check the round-1 passes.

PREFLIGHT DONE · card: check-scratch-1016 · checks: 8 · fails: 1 · ready: NO
