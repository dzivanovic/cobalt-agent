# Card 550 `card-template-1014` — preflight (read-only)

Read on `main` HEAD `7d221f51` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`). The card's anchors were drafted on `0ffb6949`; `git -C /Users/cobalt/cobalt diff 0ffb6949 HEAD --stat -- CARD.md deploy-card.sh tests/ops restarts.py` printed nothing, so the anchors hold on HEAD. No test was run (no `uv run` in this seat): the REDs stay UNPROVEN until the builder quotes them.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C … log --oneline -n 3 -- <550 card>` | `7d221f51 docs(desk): K5 card-template card 550 drafted, preflight prompt 552`: committed | OK |
| 2 | `git -C … diff HEAD --stat -- <550 card>` | empty: unchanged against HEAD | OK |
| 3 | header keys read from the card (`grep -c -E "^(JOB\|LADDER\|CLASS\|INSTALL\|BRANCH\|WORKTREE\|BASE\|TIP\|REPORT\|CHECK REPORT\|HOUSE B\|DB\|RESTARTS\|RULINGS):"`) | 14: every build/check field of CARD.md (`JOB LADDER BRANCH WORKTREE BASE TIP REPORT CHECK REPORT HOUSE B DB RULINGS`) plus `CLASS`, `INSTALL`, `RESTARTS`; `TIP` and `BASE` empty (the desk's) | OK |
| 4 | `grep -n -E "«FILL\|FILL:" <card>` | hits at `:22` and `:59` only, prose quoting the `«FILL` token; no placeholder in a header field | OK |
| 5 | `CARD.md` anchors `:33 :54 :55 :56 :58 :62 :66 :71 :73 :75 :138`, 150 lines (Read) | each is the line the card names | OK |
| 6 | `grep -c -F "DEPLOY PROOF" CARD.md` | `0` as the card says | OK |
| 7 | `grep -n -i -e "by number" -e "never by a quoted" -e "git show" CARD.md` | no hit as the card says | OK |
| 8 | `ops/desk/deploy-card.sh:29-31`, `:534-543` (Read); `grep -n` of `DEPLOY PROOF` and `FILL: markers/smoke` | `:29-31` comment, `:535` awk on `## DEPLOY PROOF`, `:537-538` and `:542-543` the `«FILL` lines: as quoted | OK |
| 9 | test anchors (Read): `test_prodwrite_hub.py:16-18, :145-150, :187-191`; `test_deploy_card.py:383-386, :426-434`; `test_deploy_step_c.py:332-334`; `test_desk_launch_prechecks.py:826-832` | each matches the card's quote and line | OK |
| 10 | `src/cobalt/jobs/restarts.py:225-228`, `:245-246` | `docs/` → `DOCS`; `tests/` → "test/documentation; no resident": RESTARTS `none` holds | OK |
| 11 | C1 red: `grep -c "DEPLOY PROOF" CARD.md` is 0, so the count of lines starting `` `## DEPLOY PROOF` (build, check; REQUIRED `` is 0 | `assert 0 == 1` is the named reason | OK |
| 12 | C2 red (1): no line equals `## HOW A CARD CITES AND PINS` on BASE | count 0, named reason | OK |
| 13 | C2 control (2) is GREEN on BASE: the four lines it pins exist (`:138` holds `` `MIGRATIONS`, `SET`, `TICKERS`. Body: ``; `:46` `\| # \| branch \| code tip \|`; `## A PRODWRITE CARD, IN SHORT`; `` `## LAUNCHD` (deploy) ``) | all four present, once each | OK |
| 14 | `## DEPLOY PROOF` marker counts: after the edit `grep -c -F "## DEPLOY PROOF" CARD.md` | C1 line and the C2 `- DEPLOY PROOF:` line (it holds `` `## DEPLOY PROOF` ``) = `2`; the C2 heading line does not hold it. `HOW A CARD CITES AND PINS` = `1` | OK |
| 15 | test holds no whole file, no whole fixed-file line equal to a commit, no BASE hash | C1, C2(1): none. C2(2) pins four lines of `CARD.md` that the card does not change | FAIL (see ISSUES 1) |
| 16 | test holds no `git show` (X3 and the WHY line) | row C2(1) requires the test to assert the text `` `git show <BASE>:<file>` `` and `the `BASE` literal` | FAIL (see ISSUES 2) |
| 17 | wording of the new text traces only to R1471 and R1472 (`cto-2026-10-14.md` rows R1471 `:8`, R1472 `:7`; `cto-2026-10-14-words.md:8-9`) | R1471: "(6) card template (rulings by R number, no HEAD hash, anchors by file:line, DEPLOY PROOF required)". R1472: "pins only the lines its own card changes, no test holds a whole fixed-file line equal to a commit". Clauses with no source: see ISSUES 3 | FAIL |
| 18 | RESTARTS class home per row (K10): C1, C2 → `docs/…/CARD.md` (`DOCS`) and `tests/ops/…` (no resident); R3 → none | no restart for any row | OK |
| 19 | overlap with 521, 523, 537, 549 (`grep -n "CARD\.md"` over each file) | 521: `:33` forbids a `CARD.md` edit; its test 3d asserts `CARD.md` holds no `--deploy-gate`, and the new text holds none. 523: names no `CARD.md` line. 537: reads the `## SMOKE READS` paragraph, edits none. 549: no `CARD.md` hit | OK |
| 20 | overlap with 546, 547, 548 | 546: no `CARD.md` hit; 548: reads `## SHIPS` only (`:47`), edits none; 547 not in `prompts/2026-10-14/` (no db-copy card): nothing to compare | OK (NOTE 6) |
| 21 | what blocks this card's own deploy | 537 deploys first (one deploy at a time; `cto-2026-10-14.md:16`); 537's build `91b68031` is live. Also open: the 523 fix-round recut and deploy (`:17`) | OK (NOTE 5) |

## ISSUES
1. FAIL (check 15): C2 control `test_c2_the_lines_other_tests_pin_stand` pins four lines of `CARD.md` that this card does not change (`:138` TICKERS line, the SHIPS header, the PRODWRITE heading and section words, the LAUNCHD line). Brain R1472 and the card's own WHY say a test pins only the lines its own card changes; those four lines are already pinned by their own tests, and X4 already asks whether those tests stay GREEN. Fix: drop the control, or reduce it to the new lines only.
2. FAIL (check 16): the card's WHY and X3 say the test holds no `git show` and no `BASE` literal, but row C2(1) makes the test assert the text `` `git show <BASE>:<file>` `` and `the `BASE` literal`; ORDER allows `<BASE>` text only, and its `grep -e "git show"` expects no hit. Either narrow the rule to "no `git show` call, no 8-hex BASE" in WHY, X3 and ORDER, or drop those two needles from C2(1).
3. FAIL (check 17), clauses with no ruling behind them: (a) ANCHORS: "recorded in `## RECORDS` with its command and time", "at drafting `BASE` is empty, `git show HEAD:<file>` stands in", "the builder re-reads it on the `BASE` the desk writes (BUILD-HUB E3)"; R1471 says only "anchors by file:line". (b) RULINGS: "the card names the row, not its words" and "never by a quoted text that can drift"; R1471 says "rulings by R number". (c) TESTS bullet attributes "no `BASE` literal" to "his R1471"; R1471 has no test rule, and R1472 says "no BASE hash" and "only 523's own lines". (d) C1's "a docs-only or tests-only card names its files too". Cut these or have the desk rule them (the drafter's ASK DESK 1 holds the same point).
4. NOTE: C1 quotes "DEPLOY PROOF required" and "rulings by R number, no HEAD hash, anchors by file:line" as his words; they sit in the desk's row at `cto-2026-10-14.md:16` and `:27`, not in `cto-2026-10-14-words.md` (`:8-9` holds only the relay). Write them as the row's text, not as his.
5. NOTE: the card's own `## DEPLOY PROOF` has two lines without both `· before ` and `· after ` (the `RULE:` line and the `ONE SMOKE READ` line). `deploy-card.sh:541` takes every such line as a smoke read, so the `RULE:` line lands in the deploy card's `## SMOKE READS` as prose. Move it to `## RECORDS`.
6. NOTE: 547 (db-copy) is not written; its overlap cannot be compared. 537 rows S1(2)/S2(2) still read a `BASE` literal; this card does not touch them (drafter ASK DESK 3; 537 deploys first).

PREFLIGHT DONE · card: card-template-1014 · checks: 21 · fails: 3 · ready: NO
