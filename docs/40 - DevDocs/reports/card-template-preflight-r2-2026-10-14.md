# Card 550 `card-template-1014` — preflight round 2 (read-only)

Read on `main` HEAD `f3b509ac` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`). The amend (`reports/draft-550-amend-2026-10-14.md`) was read on `f6cdc67f`; `git -C /Users/cobalt/cobalt diff HEAD --stat -- CARD.md deploy-card.sh restarts.py tests/ops` printed nothing, so the anchors hold on HEAD. No test was run (no `uv run` in this seat): every RED stays UNPROVEN until the builder quotes it.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 15 | test holds no whole file, no whole fixed-file line equal to a commit, no BASE hash (re-check) | control C2(2) is gone; C1 and C2(1) pin only the new lines, found by text. C1 and C2(1) name neighbour lines (`` `## CHECK ASKS` ``, `` `## RECORDS` ``, the `State of the desk` bullet, `## EXAMPLE 1`) only to prove the order: see NOTE 2 | OK |
| 16 | test holds no `git show` call, no 8-hex BASE (re-check) | WHY, X3 and ORDER now say "no `git show` call, no 8-hex `BASE`"; C2(1) needles are `his R1471`, `brain R1472`, `a whole fixed-file line equal to a commit`, `a BASE hash`: no `git show` text. `grep -n -E -e "git show" -e "[0-9a-f]{8}"` over the card hits only prose lines (the rule text, the HEAD hashes in `## RECORDS`) | OK |
| 17 | wording added to `CARD.md` traces only to R1471, R1472 (`cto-2026-10-14.md:8` R1471, `:7` R1472, `:16`, `:27`) | ANCHORS, TESTS, DEPLOY PROOF bullets: R1471 "anchors by file:line", "DEPLOY PROOF required"; R1472 "pins only the lines its own card changes, no test holds a whole fixed-file line equal to a commit", "no BASE hash". The ASK DESK 1 clause "no HEAD hash" is R1471's own. Clauses still beyond the two rulings: NOTE 1 | OK (NOTE 1) |
| 1 | `git -C … log --oneline -n 3 -- <550 card>` | `f3b509ac docs(desk): card 550 amended, preflight r2 prompt`, `7d221f51 …`: committed | OK |
| 2 | `git -C … diff HEAD --stat -- <550 card>` | empty | OK |
| 3 | header keys (`JOB LADDER CLASS INSTALL BRANCH WORKTREE BASE TIP REPORT CHECK REPORT HOUSE B DB RESTARTS RULINGS`) read from the card `:1-14` | every build/check field `CARD.md` requires (`JOB LADDER BRANCH WORKTREE BASE TIP REPORT CHECK REPORT HOUSE B DB RULINGS`) present, plus `CLASS`, `INSTALL`, `RESTARTS` as cards 537 and 547 carry them; `BASE:` and `TIP:` empty (the desk's); no other placeholder token | OK |
| 4 | `grep -n -E "«FILL"` over the card | no field holds one | OK |
| 5 | `CARD.md` anchors `:33 :54 :55 :56 :58 :62 :66 :71 :73 :75 :138` (Read) | each is the line the card names | OK |
| 6 | `wc -l CARD.md` against the card's READ line "whole (150 lines)" | `149`; the card says 150 | FAIL (ISSUES 1) |
| 7 | `grep -c -F "DEPLOY PROOF" CARD.md` | `0`, as C1 says | OK |
| 8 | `grep -n -i -e "by number" -e "git show" -e "drafter" CARD.md` | one hit, `:7` (the drafter line, no drafter-prompt shape); no `by number`, no `git show`, as the card says | OK |
| 9 | `ops/desk/deploy-card.sh` `grep -n -E "DEPLOY PROOF\|FILL: (markers\|smoke)\|· before\|· after"` | `:29-30` comment, `:535` awk on `## DEPLOY PROOF`, `:537-538` and `:542-543` the `«FILL` lines, `:540-541` the before/after split: as quoted | OK |
| 10 | test anchors `test_prodwrite_hub.py:16-18` (`REPO`, `HUBS`), `:146` (`HUBS / "CARD.md"` read as text) | match the card's shape claim | OK |
| 11 | C1 red: lines starting `` `## DEPLOY PROOF` (build, check; REQUIRED `` | `DEPLOY PROOF` occurs 0 times in `CARD.md`: count 0, `assert 0 == 1` | OK |
| 12 | C2 red: lines equal to `## HOW A CARD CITES AND PINS` | none in `CARD.md` (`grep -c -F "HOW A CARD CITES AND PINS"` → 0): count 0, named reason | OK |
| 13 | `## DEPLOY PROOF` counts on the card: after the edit `grep -c -F "## DEPLOY PROOF" CARD.md` | the C1 line and the C2 `- DEPLOY PROOF:` line (holds `` `## DEPLOY PROOF` ``) = `2`; the heading line and the `Owed by` line do not hold it; `HOW A CARD CITES AND PINS` = `1` | OK |
| 14 | order anchors are unique by start: `` `## CHECK ASKS` ``, `` `## RECORDS` `` (backticked, `:54`, `:56` only; the examples' headings are bare), `## EXAMPLE 1 — the E1 fix, at its BUILD launch` (`:75`), the `State of the desk` bullet (`:73`) | each starts one line | OK |
| 18 | RESTARTS class home per row (K10): `src/cobalt/jobs/restarts.py:225-228` (`docs/` → `DOCS`), `:246` ("test/documentation; no resident") | C1, C2 → `docs/…/CARD.md`, `tests/ops/…`; R3 → none: no restart | OK |
| 19 | overlap with 521, 523, 537, 549 (`grep -n -F "CARD.md"` over each file) | 521: `:33` forbids a `CARD.md` edit; its test 3d asserts `CARD.md` holds no `--deploy-gate`, and the new text holds none; `:74` reads `CARD.md:58-62`, not edited. 523: `CARD.md` named in prose of row H2 only (`## SHIPS`), edits `BUILD-HUB.md`. 537: reads the `## SMOKE READS` paragraph, edits none. 549: no hit | OK |
| 20 | overlap with 546, 547, 548 (all three now exist in `prompts/2026-10-14/`) | 546: no `CARD.md` hit. 547: no `CARD.md` hit. 548: reads `prompts/CARD.md` `## SHIPS` (`:47`), edits none; the new lines sit outside `## SHIPS` | OK |
| 21 | what blocks this card's own deploy (`cto-2026-10-14.md:16-17`) | one deploy at a time: 537 deploys first (build `91b68031` live at the desk row's last read); the 523 fix-round recut and deploy is also open (`:17`). The card's build itself waits on no card | OK (NOTE 4) |

## ISSUES
1. FAIL (check 6): `## READ` says `docs/40 - DevDocs/prompts/CARD.md` "whole (150 lines)"; `wc -l` and the Read tool give 149. Fix: write 149 (no other anchor moves).
2. NOTE: C1 and C2(1) find `` `## CHECK ASKS` ``, `` `## RECORDS` ``, the `State of the desk` bullet and `## EXAMPLE 1` by their starts, to prove the section order. Those lines are not changed by the card; they are read as position anchors, not pinned whole. The builder keeps it to a start-match, never a whole-line or commit comparison.
3. NOTE: clauses of the new `CARD.md` text with no ruling of R1471 or R1472 behind them: C1's "One marker line per file the set changes" and "at least one smoke read line: the command typed whole and what a green answer looks like" (from `CARD.md` `## SMOKE READS` and `deploy-card.sh:540-543`, not from a ruling); C2's `or R<n> of the named report` in the RULINGS bullet. The desk takes them with its other defaults or cuts them.
4. NOTE (carried from round 1, untouched by the amend): C1 quotes "DEPLOY PROOF required" and "rulings by R number, no HEAD hash, anchors by file:line" as his words; they sit in the desk's row (`cto-2026-10-14.md:16`, `:27`), not in `cto-2026-10-14-words.md` (`:8-12` holds only the relay and "I approve all changes"). And the card's `## DEPLOY PROOF` `RULE:` line carries neither `· before ` nor `· after `, so `deploy-card.sh:541` takes it as a smoke read line of the deploy card as prose; move it to `## RECORDS`.
5. NOTE: 537 rows S1(2)/S2(2) still read a `BASE` literal; this card does not touch them (537 deploys first).

PREFLIGHT DONE · card: card-template-1014 · checks: 21 · fails: 1 · ready: NO
