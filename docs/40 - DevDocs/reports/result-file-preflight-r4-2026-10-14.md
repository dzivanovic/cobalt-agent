# Card 548 `result-file-1014` — preflight round 4 (2026-10-14, read-only)

Read at `main` HEAD `6943792e`. The card is committed there (last commit `6943792e`). No test was run.

Round 3's one FAIL (RF2 (5) against card 547 H1) is repaired in text: both cards now keep `BASE` and `base_lines()` and exempt by content. One FAIL stays: the card says the order against 547 does not matter, and it does (ISSUE 1).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <548 card>`; `git log --oneline -3 -- <548 card>` | diff empty; commits `6943792e`, `ae34ebf3`, `00921627` | OK |
| 2 | `grep -c "«FILL" <548 card>` | `0` | OK |
| 3 | header vs `CARD.md` (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS (+ CLASS, INSTALL, RESTARTS as card 547 carries them) | all present; empty fields are BASE, TIP (the desk's), CHECK REPORT, HOUSE B (the check's); no other placeholder | OK |
| 4 | `git diff --stat HEAD` over the 3 gates, 4 reader scripts, 3 hubs, `gate.sh`, 6 test files, `restarts.py` | printed nothing: working files equal HEAD, so `Read` and `grep -n` of them are HEAD's | OK |
| 5 | RF3 anchors, `deploy-step0.sh` | `:69` `HERE=`, `:132` `rel()`, `:649` `lits=`, `:657` clean pair, `:677-733` P2, `:679` `last=`, `:686-694` loop, `:702` `held_n`, `:706` tip `grep -o`, `:721` `"BUILT ·"*"tip: $ctip"*`, `:741-749` report proof | OK |
| 6 | RF4 anchors, `deploy-card.sh` | `:477-482` proof, `:483` `last`, `:486-488` `frep`, `hn=""`, `[ -z "$frep" ] \|\| hn=$(held_n "$last")`, `:490-491` literals, `:493-494` tip, `:501` `${frep#"$REPO"/}`, `:504-507` `BUILT ·`, `:524` SHIPS cell | OK |
| 7 | RF5 anchors, `desk-launch.sh` | `:264` `here=`, `:1446-1449` report proof, `:1450` `clast`, `:1451-1458` literals, `:1459` `ltip`, `:1463-1476` `fixed_ok` (`:1469`, `:1472-1473`), `:1479` `hn=$(held_n "$clast")`, `:1488-1489` tip test; `:369` `dirname "$0"` idiom | OK |
| 8 | RF4 `held_n` read on any `.result` + empty `frep` refuses (r3 NOTE 2) | stated in RF4; RF5 (4) last row names it red | OK |
| 9 | hub lines: `BUILD-HUB.md:109` starts `A "DB: none" build writes`, `CHECK-HUB.md:125` starts `A "DB: none" card`; one `claude --bg ` line each (`BUILD-HUB.md:12`, `CHECK-HUB.md:10`) | as written | OK |
| 10 | RF1 helper idiom `gate.sh` `refuse()` | `printf 'REFUSED: %s\n' "$*" >&2` (r3 check 9; `gate.sh` unchanged since) | OK |
| 11 | each row's red test names its failing reason on BASE | RF1 exit 127; RF2 count 0 / `1 failed`; RF3 `lacks 'held unfixed: 0'` / P2 passes / `does not end 'BUILT ·'`; RF4 `lacks 'held unfixed: 0'` / written; RF5 `its stop line lacks …` / launches; RF6 RUN | OK |
| 12 | no test pins a whole file, a whole fixed-file line equal to a commit, or a BASE literal | RF1, RF3-RF5 pin by content; RF2 (4) is a builder command, not an assertion; RF2 (5) keeps the existing `BASE = "5e5fab02"` and `base_lines()` by design (brain R1472: the check is an ordered subsequence by content with EXEMPT prefixes, and it needs `base_lines()` for its negative control) | OK |
| 13 | stop line stays the finish signal (L71); the file is additional | `desk-watch.sh:40-44`, `desk-done.sh:24-31` in `## NOT IN THIS JOB`; no `.result` on `FAILED` or `SHADOW BUILT`; no-file reports read byte for byte as today | OK |
| 14 | the file carries only keys the stop line carries | 15 build keys, 22 check keys, one per stop-line field; `env` = `.env` named as the one exception and RF1 (3) puts it in the helper's header | OK |
| 15 | each row's files hold its RESTARTS class home (K10) | `ops/desk/` operator script, `docs/40 - DevDocs/prompts/` DOCS, `tests/` no resident; RF6 expects none | OK |
| 16 | X1 readers outside the three gates | `card-fill.sh:66-78`, `preflight.sh:246-270`, `desk-launch.sh:1689-1698`, `preflight.sh:169-176`, `:157`, `:1671` all named in `## NOT IN THIS JOB` (r3 NOTE 3 repaired) | OK |
| 17 | overlap with 521, 523, 537, 546, 549, 550 (`grep -o file:line` of each card) | 546: `deploy-card.sh:38-39`, `desk-launch.sh:502-522, 541, 1727`, `BUILD-HUB.md:80, 105`; 521: `BUILD-HUB.md:12, 65, 80-82`; 537: `BUILD-HUB.md:12, 65, 80-82`, `deploy-card.sh:29-31`; 549, 550: none; none touches `deploy-step0.sh:677-733`, `deploy-card.sh:483-507`, `desk-launch.sh:1450-1489`, `BUILD-HUB.md:109`, `CHECK-HUB.md:125`. 546's `deploy-card.sh:38-39` shifts later lines: the card says RF3-RF5 re-read by content | OK |
| 18 | overlap with 547 (now in `prompts/2026-10-14/`) | 547 ranges: `BUILD-HUB.md:83`, `desk-launch.sh:1003, 1082-1089, 2119-2121`, `gate.sh`, `gate-lists.md`: no line overlap with 548. SAME TEST BODY: 547 H1 and 548 RF2 (5) both rewrite `test_build_hub_no_clutter.py:57-60` | FAIL (ISSUE 1) |
| 19 | 523 H3 (3) vs RF2 (5): which lands first | the card's header: 523's recut deploys first (`hub-text-1013` was rolled back); RF2 (5) keeps any exemption 523 wrote (`FIX-ROUND REPORT (brain R1309):`, `§0 Headline`) | OK |
| 20 | what blocks the card's own deploy | see ISSUE 2 | OK |

## ISSUES

1. FAIL RF2 (5) / header: the card says "against 547 the order does not matter" because both exempt by content. The bodies do not compose. 547 H1 prescribes `test_no_other_line_changes_from_base` as "drop every `- (b) THE LOCK` line from both sides, then assert the two lists equal `base_lines()`": that body has no exemption list, so if 548 deploys first, 547's equality turns RED on `BUILD-HUB.md:109` (548's own line, not exempted by 547's body) and on every line another card replaced. If 547 deploys first, 548's body replaces 547's (the `- (b) THE LOCK` exemption is kept in EXEMPT), but 547's test (18) looks for a `startswith("- (b) THE LOCK")` filter by content, and 548's tuple of prefixes may not hold that text. Both cards also edit the same hunk (`:57-60`): the second deploy meets a textual conflict unless its builder's BASE already holds the first. Fix: name one order and what the second does. Simplest: 547 deploys before 548, 548's BASE is filled after 547's deploy, and RF2 (5) says "the body 547 left (a `startswith("- (b) THE LOCK")` filter and an equality on `base_lines()`) becomes the EXEMPT-prefix subsequence, with `- (b) THE LOCK` kept as a literal `startswith("- (b) THE LOCK")` entry". The same sentence belongs in card 547 NOT IN THIS JOB (desk's card).
2. NOTE deploy blockers, in order: (a) `deploy-smoke-string-1014` (537) first (one deploy at a time); (b) 523's recut (RF2 keeps its two exemptions); (c) 547 before 548 (ISSUE 1); (d) 546's `deploy-card.sh:38-39` edit shifts RF3-RF5 lines (re-read by content, E3); (e) the card's own check (BASE, TIP, CHECK REPORT, HOUSE B are the desk's).
3. NOTE RF2 "WRITTEN: with the file tool its launch line already allows": the allow strings are `Edit(//Users/cobalt/cobalt-wt/**)` (and the reports path on CHECK-HUB); a new `.result` file is created by the Write tool, which the same Edit path rule covers. If a seat's Write is refused, that is a launch-line fact, not a card edit (no allow string changes here). Unproved until the first build writes one.
4. NOTE: the `.result` is read at the gates from HEAD (`git show`) for the fix report but from the working file plus a blob proof for the check; the card says so in RF3-RF5 and RF5 (4) tests the verdicts agree.

PREFLIGHT DONE · card: result-file-1014 · checks: 20 · fails: 1 · ready: NO
