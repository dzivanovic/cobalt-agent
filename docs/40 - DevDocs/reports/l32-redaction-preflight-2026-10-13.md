# Card 472 `l32-redaction-1013` preflight · 2026-10-13

§0: card committed (`81ee1c3e`), unchanged against HEAD `240ac340`; header, RULINGS, anchors and the no-quote rule hold. Two FAILs: the FOR THE CHECK line is absent, and `## RECORDS` names no RESTARTS class. Ready: NO until the desk adds both.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>` | empty | OK |
| 2 | `git log --oneline -3 -- <card>` | `81ee1c3e` (committed) | OK |
| 3 | `grep -c "«FILL" <card>` | 1, the BASE line only | OK |
| 4 | header `CLASS:` / `DB:` / `RULINGS:` | `K2` / `none` / `2026-10-12 R1138` | OK |
| 5 | `grep -n R1138 reports/cto-2026-10-12.md` | `:173` row `HIS RULING · APPROVED` | OK |
| 6 | L1 anchor: `grep -n -E "[0-9]+ non-empty"` on the proposal | `:19`, section `## 2.1`, last bullet; pattern count 1 | OK |
| 7 | L2 anchor: five-number pattern on the proposal | `:76`, section `## 5`; count 1 | OK |
| 8 | L3 anchor: `non-empty` pattern on the drafter report | `:50`, section `## RECORDS`; count 1 | OK |
| 9 | L4 anchor: five-number pattern on `338-f23-tribunal.md` | `:16`, section `## 1.`; count 1 | OK |
| 10 | `git diff HEAD --stat` on the three target files | empty (working tree equals HEAD, so the greps prove HEAD) | OK |
| 11 | tribunal `:60` and `:298` read | `:60` the three known spans; `:298` item 8 KNOWN SPANS | OK |
| 12 | `grep -c -E` count patterns and `strategy notes` on the card | 0; the card names spans by file, line and section only | OK |
| 13 | rows for the proposal spans, the drafter span and `338:16` | L1, L2 (proposal), L3 (drafter), L4 (338) | OK |
| 14 | each row's red | each is `RUN — asserts nothing` with a `grep -c` that prints 1 on BASE; stated | OK |
| 15 | V1 pattern `time_window [0-9]` on the three files | hits only `proposal:19` and `drafter:50`, both inside L1 and L3; 0 after | OK |
| 16 | `grep -n -E "allowedTools\|desk-launch"` on the card | none; no new command on any seat's line | OK |
| 17 | RESTARTS class in `## RECORDS` | `RESTARTS\|DOCS` matches once, in the `## ROWS` intro (`DOCS ONLY`); none in `## RECORDS` | FAIL |
| 18 | FOR THE CHECK line byte for byte (`grep -c -F`) | 0 in the card; no `FOR THE CHECK` line at all | FAIL |
| 19 | blockers of the card's own deploy | see ISSUES | NOTE |

## ISSUES
- FAIL 18: the card has no FOR THE CHECK line. Add, byte for byte: `FOR THE CHECK: seam and L32 2026-10-13 brain: first ready merges first; row 18 approved R1324 K2, card pending; FINAL untouched; card 472 names spans by file:line only (no quotes) and gains 338-f23-tribunal.md:16` (other cards carry it as a `FOR THE CHECK:` line in the notes).
- FAIL 17: `## RECORDS` does not name the RESTARTS class of the changed paths. All three are under `docs/`, so the class is `DOCS`; add it.
- NOTE: the card's rows and RECORDS say "HEAD `0e3590dc`"; HEAD is now `240ac340`. The anchors still hold (files unmodified), so the stale hash misleads only.
- NOTE: the card cites neither R1347 nor R1349 (the brain's directions) and not R1324. The R1324 row in `cto-2026-10-13.md` (`^| R1324 `) is about the survey rows, and I found no text there that says "row 18". The FOR THE CHECK line quotes R1324 as the desk wrote it; the desk should confirm which row carries the row-18 approval.
- NOTE: the card's LADDER cites R1343 (row exists, `^| R1343 `, "MVP drafters ahead"); it is not an approval of the card.
- NOTE, blockers of the card's own deploy: docs only, no migration, no restart. It must still wait for any live deploy (one at a time). Queue per `cto-2026-10-13.md`: 446 and 458 in check, then 304 row CR and its deploy, then 448 and 462. The desk decides whether 472 merges before or after them; the brain's rule is "first ready merges first".

PREFLIGHT DONE · card: l32-redaction-1013 · checks: 19 · fails: 2 · ready: NO
