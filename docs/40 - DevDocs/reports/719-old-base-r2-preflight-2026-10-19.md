## CHECKS

Edit state: the amend is COMMITTED in `ebcca344` (parent `ee414e79`). `git diff HEAD -- <card>` prints nothing, as it should. The proof is `git diff ee414e79 ebcca344 -- <card>`.

| # | command | output | OK/FAIL |
|---|---|---|---|
| a1 | row `W` vs. W1 (`:34`): W1 says its `--deselect` goes at the end of PASS 1 and its id at the end of PASS 2 | row: PASS 1 gains ` --deselect tests/cobalt/test_strike_detector_db.py`, PASS 2 gains ` tests/cobalt/test_strike_detector_db.py`. Equal to W1's text and to the file W1 will write (`grep -c -F` → 2 is W1's own proof) | OK |
| a2 | `git -C /Users/cobalt/cobalt show e4586978:ops/desk/gate-lists.md` | BASE PASS 1 ends `--deselect tests/cobalt/test_radar_price_floor_db.py`; PASS 2 ends `tests/cobalt/test_radar_price_floor_db.py`. Neither names `test_strike_detector_db.py`, so both additions are new and sit at the end. The file's own rule (`:5-7`, read in the output) says the same | OK |
| a3 | same output, section headers in file order | OFFLINE, PROOF ONLY, PASS 1, FORWARD, PASS 2, STRAY ROWS, LIVE-NOTE, ROLLBACK, FINGERPRINT, ALLOWED SKIPS, LEVEL 0013. The row's ORDER list is the first nine, in the same order; the ALLOWED SKIPS section the row's last step names exists (one line). No `## OFFLINE OPS` | OK |
| b | `grep -n "" prompts/BUILD-HUB.md` lines 35-37 | `:36` is the intro of THE LOCK (the text binds a step that takes the lock by hand); `:37` is the take (atomic, waits, `.env` copied by name), the check (exactly one `.env`), the release, and `ls` proving the `.env` gone. The row's gloss "(take, `.env` copied by name, release, `.env` proven gone)" is what `:36-37` says. The cite names `prompts/BUILD-HUB.md`; the file is `docs/40 - DevDocs/prompts/BUILD-HUB.md` (the same short form the card uses elsewhere) | OK |
| c | WHY line, `git diff ee414e79 ebcca344` | now `Rows M1, T1, C1-C4, W1, D1, W in order` | OK |
| d | `git diff HEAD -- <card>`; `git diff ee414e79 ebcca344 -- <card>` | HEAD diff: empty (committed). Amend diff: 2 lines changed (`4 ++--`): the WHY line and the `W` row. The three edits (additions, order line, WHY) are inside those two lines. Header lines 1-11 (JOB, LADDER, BRANCH, WORKTREE, BASE `e4586978`, TIP, REPORT, CHECK REPORT, HOUSE B, RULINGS, SHADOW OF, PRECONDITION) not in the diff | OK |
| e | round 1 ISSUE 1 (row left the order, lock handling and skips check to the hub) | the row now gives the order, the by-hand lock and `.env` handling and the ALLOWED SKIPS check, and says no `gate.sh` call | OK |
| f | round 1 checks 1-7 | carried as passed (they cover 855, 718 and the 719 table's placement; 719's `W` is still the last table row, `:36`, after D1) | OK (carried) |

## ISSUES

None blocking. Two notes:
1. The BASE's STRAY ROWS line holds a placeholder (`<every constructed ticker your with-DB tests write, each quoted>`). The row says to run the BASE's lines verbatim; the gate seat has to fill it with the tickers the card's with-DB tests write (as at that date). Not a card defect.
2. The lock position (before PROOF ONLY, after FINGERPRINT) is the drafter's choice (amend report D2); the gate-lists give none. It matches the lock-held-across-the-passes rule of `BUILD-HUB.md:37`. Not blocking.

PREFLIGHT DONE · card: s4-p1-1018-gemini · checks: 8 · fails: 0 · ready: YES
