# Card 472 `l32-redaction-1013` preflight round 2 · 2026-10-13

§0: card committed (`a6c6335c`), no diff against HEAD `f922f8dd`. Round-1 FAIL 18 (FOR THE CHECK) and FAIL 17 (RESTARTS class) are now OK. One FAIL left: the card still names a stale HEAD (`83c9894e`; HEAD is `f922f8dd`). Anchors hold. Ready: NO until the hash is current.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <card>` | empty | OK |
| 2 | `git log --oneline -3 -- <card>` | `a6c6335c` (amend), `81ee1c3e` | OK |
| 3 | `grep -n "«FILL"` on the card | only the BASE line (:6) | OK |
| 4 | header `CLASS:` / `DB:` / `RULINGS:` | `K2` / `none` / `2026-10-12 R1138` | OK |
| 5 | `grep -n -E "^\| R1138 "` on `cto-2026-10-12.md` | `:173`, `HIS RULING · APPROVED` | OK |
| 6 | L1: pattern `[0-9]+ non-empty` on the proposal | `:19`, section `## 2.1` (:13-20), last bullet | OK |
| 7 | L2: five-number pattern on the proposal | `:76`, section `## 5` (:62-78) | OK |
| 8 | L3: `non-empty` pattern on the drafter report | `:50`, last RECORDS line | OK |
| 9 | L4: five-number pattern on `338-f23-tribunal.md` | `:16`, section `## 1.`, KNOWN SPANS paragraph; one hit | OK |
| 10 | `git diff HEAD --stat` on the three files, `restarts.py`, `f23-tribunal-2026-10-11.md` | empty (working tree = HEAD, so the greps prove HEAD) | OK |
| 11 | each row's red | L1-L4 each `RUN — asserts nothing` with a `grep -c -E` that prints 1 on BASE (checks 6-9 show one line each) | OK |
| 12 | V1: `time_window [0-9]` on the three files | hits `proposal:19` and `drafter:50` only, inside L1 and L3; V1 expects 4 changed lines in 3 files = L1-L4 | OK |
| 13 | rows for proposal :19, :76, drafter :50, `338:16` | L1, L2, L3, L4 | OK |
| 14 | no count or user text in the card: `grep -n -E "[0-9]+ non-empty\|time_window [0-9]\|[0-9]/[0-9]/[0-9]/[0-9]/[0-9]"` | only the L1 red command's pattern (:23, a pattern, not a count); spans named by file, line, section | OK |
| 15 | `grep -n -E "allowedTools\|desk-launch"` on the card | none; no new command on any seat's line | OK |
| 16 | RESTARTS class in `## RECORDS` | names `DOCS` for all three paths, cites `restarts.py:225-228`; `restarts.py` :225 `startswith("docs/")`, :228 `"DOCS", ()` | OK |
| 17 | FOR THE CHECK line, `grep -c -F` with the exact line | 1 | OK |
| 18 | brain rows by id in `cto-2026-10-13.md` | R1347, R1349, R1356, R1324 all exist and say what the card says (R1349: "row 18 approved R1324 (K2); card 472 names spans by file:line only, plus `338-f23-tribunal.md:16`"; R1324: "yes, yes, and remove") | OK |
| 19 | the card's `:20 :18 :11 :43` line numbers for those rows | today the rows sit at `:27 :26 :18 :50` (the live file grew while I read); ids hold | NOTE |
| 20 | card's HEAD hash against `git rev-parse HEAD` | card says `83c9894e` (`## ROWS` intro and `## RECORDS`); HEAD is `f922f8dd` | FAIL |
| 21 | round-1 FAILs now OK | FAIL 18 → check 17 OK; FAIL 17 → check 16 OK; stale hash → check 20, still FAIL | FAIL |
| 22 | blockers of the card's own deploy | see ISSUES | NOTE |

## ISSUES
- FAIL 20: the card's HEAD hash is `83c9894e`, not the current `f922f8dd` (it was current at the amend; the desk has committed since). The anchors still hold on the current HEAD (checks 6-10), so only the record is stale. Fix: refresh the hash (and the `:line` of R-rows if kept) at the fill that sets BASE, or drop the hash from the intro and name BASE only.
- NOTE 19: the `cto-2026-10-13.md` line numbers in `## RECORDS` drift because the brain's file is live; the row ids are the stable anchor.
- NOTE, blockers of the card's own deploy (docs only, no migration, no restart): one deploy at a time. First 304 (F4 refresh): fix report is on main (`a9fcd08e`), deploy card `491` is committed (`3aa481c0`) but its launch was refused for two FILL markers; drafter `draft-491-fill` (prompt 492, R1365, R1366) fills them, then the desk commits 491 and launches the deploy (`cto-2026-10-13.md` §5 OWED line). Then 458 (check ready YES, tip `824e478b`). 472's own deploy waits for both, unless the brain rules "first ready merges first" otherwise (R1349); the card also needs its BASE filled.

PREFLIGHT DONE · card: l32-redaction-1013 · checks: 22 · fails: 2 · ready: NO
