# Card 548 `result-file-1014` — preflight round 3 (2026-10-14, read-only)

Read at `main` HEAD `ae34ebf3`. The card is committed there. No test was run.

Round 2's two FAILs: RF2 (5) is repaired for the `- (b) THE LOCK` line, but card 547 now rewrites the same test body and deletes what RF2 reads (ISSUE 1, new FAIL). RF4/RF5 (4) is repaired (one NOTE, ISSUE 2).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <548 card>`; `git log --oneline -4 -- <548 card>` | diff empty; commits `ae34ebf3`, `00921627`, `32687899` | OK |
| 2 | `grep -c "«FILL" <548 card>` | `0` | OK |
| 3 | header vs `CARD.md` (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS | all present; empty are the desk's (BASE, TIP) or the check's (CHECK REPORT, HOUSE B); no other placeholder | OK |
| 4 | RF2 (5), round-2 FAIL: `grep -n` of each EXEMPT prefix on `BUILD-HUB.md` at HEAD | `:12` `claude --bg `, `:17` `L1 a missing input`, `:65` the pytest line, `:80` `(a0)`, `:81` `THE GATE, ONE CALL`, `:82` `(a) OFFLINE`, `:83` `- (b) THE LOCK` (now in EXEMPT), `:105` `§0 Headline`, `:109` the DB:none line, `:111` `<tip>` = the last code commit | OK |
| 5 | RF4, round-2 FAIL: `deploy-card.sh:483-507` at HEAD | `:483` `last`, `:486-488` `frep`, `hn=""`, `[ -z "$frep" ] \|\| hn=$(held_n "$last")`, `:490-491` literals, `:493-494` tip, `:501` cut, `:504-507` `BUILT ·`, `:524` SHIPS cell: all as written; RF4 now reads `held_n` whenever a `.result` exists (NOTE 2) | OK (ISSUE 2) |
| 6 | RF5 (4), round-2 FAIL: the table | now holds the row "stop line `held unfixed: 1`, clean `.result`, NO fix report: all three refuse"; `deploy-step0.sh:702` and `desk-launch.sh:1479` read at HEAD: both take `held_n` on the stop line | OK |
| 7 | RF3 anchors: `deploy-step0.sh:657`, `:677-733`, `:679`, `:686-694`, `:702`, `:706`, `:721`, `:741-749` | all as written | OK |
| 8 | RF5 anchors: `desk-launch.sh:1446-1449`, `:1450-1459`, `:1469-1473`, `:1479`, `:1450-1489` | all as written (`:1479` `hn=$(held_n "$clast")`) | OK |
| 9 | RF1 helper idiom: `gate.sh:67-68` | `refuse()` is `printf 'REFUSED: %s\n' "$*" >&2`; the `>` test removes `>&2` first | OK |
| 10 | hub lines: `BUILD-HUB.md:109`, `CHECK-HUB.md:125` start as the card says; one `claude --bg ` line each (`:12`, `CHECK-HUB.md:10`) | as written | OK |
| 11 | red test names its failing reason on BASE, every row | RF1 exit 127; RF2 count 0 / `1 failed`; RF3 `lacks 'held unfixed: 0'` / P2 passes / `does not end 'BUILT ·'`; RF4 `lacks 'held unfixed: 0'` / written; RF5 `its stop line lacks …` / launches; RF6 RUN | OK |
| 12 | no test pins a whole file, a whole fixed-file line equal to a commit, or a BASE literal | RF1, RF3-RF5 pin by content. RF2 (5) keeps `BASE = "5e5fab02"` and `base_lines()` (an ordered subsequence by content, brain R1472). Card 547 H1 deletes both and its test (18) forbids them | FAIL (ISSUE 1) |
| 13 | RF2 (4): the `test_hub_lines.py` diff-stat | named a builder command with its output quoted, not an assertion | OK |
| 14 | stop line stays the finish signal (L71); the file is additional | `desk-watch.sh:40-44`, `desk-done.sh:24-31` named in `## NOT IN THIS JOB`; no `.result` on `FAILED` or `SHADOW BUILT` | OK |
| 15 | the file carries only keys the stop line carries | 15 build keys and 22 check keys, one per stop-line field; `env` = `.env` named as the explicit exception | OK |
| 16 | each row's files hold its RESTARTS class home (K10) | `ops/desk/` operator script, `docs/40 - DevDocs/prompts/` DOCS, `tests/` no resident; RF6 expects none | OK |
| 17 | overlap: `grep -o file:line` of 521, 523, 537, 546, 547, 549, 550 | 546: `deploy-card.sh:38-39`, `desk-launch.sh:502-522, 541, 1727`, `BUILD-HUB.md:80, 105`; 537: `deploy-card.sh:29-31, 534-543`, `desk-launch.sh:994`; 547: `BUILD-HUB.md:12, 83`, `CHECK-HUB.md:10`, `desk-launch.sh:1003, 1082-1089, 2119-2121`, AND `tests/ops/test_build_hub_no_clutter.py` (`:15`, `:27-30`, `:51-54`, `:57-60`); 521: `desk-launch.sh:135-138, 2174-2189`, `BUILD-HUB.md:80-82`; 523: `BUILD-HUB.md:105, 111, new :112` and the same test file; 549, 550: none. No overlap with `deploy-step0.sh:677-733`, `deploy-card.sh:483-507`, `desk-launch.sh:1450-1489`, `BUILD-HUB.md:109`, `CHECK-HUB.md:125`. The test file is shared with 523 and 547 | OK (ISSUE 1) |
| 18 | RF2 vs 523 H3 (3) and 547 H1: which lands first | see ISSUE 1 | FAIL |
| 19 | X1: readers of a BUILT / CHECK DONE line outside the three gates | `card-fill.sh:66-78`, `preflight.sh:246-270`, `desk-launch.sh:1689-1698` named in `## NOT IN THIS JOB`; other readers (`preflight.sh:169-176`, `desk-launch.sh:157`, `:1671`) not named (NOTE 3) | OK (NOTE 3) |
| 20 | what blocks the card's own deploy | ISSUE 4 | OK |

## ISSUES

1. FAIL RF2 (5): card 547 H1 rewrites the body of the same test (`test_no_other_line_changes_from_base`), deletes `BASE`, `base_lines()` and the `git show` read, and its test (18) asserts the file holds none of them (547 line 40, line 46); RF2 (5) rewrites the same body on `base_lines()` and keeps `BASE`, and its negative control (a BASE line deleted from a copy) needs it. Whichever deploys second breaks the first's test: 548 after 547 has no `base_lines()` to read; 547 after 548 removes what 548's negative control uses. The card names only 523 as the order. Fix: say which lands first and what the second does. Simplest: 548 RF2 (5) drops the BASE read and takes 547's by-content shape (exempt prefixes, no `BASE`, no `git show`; the negative control runs on a copy of the hub's own lines), so the two edits of the body agree; or order 547 first and say RF2 (5) then edits the by-content body 547 left.
2. NOTE RF4: with `hn` read from `held_n "$last"` whenever a `.result` exists, a held stop line with NO fix report gives `hn` of 1 or more, `deploy-card.sh:489` skips the literal refusals and `:512` (the `held_rule` call) sits inside the `frep` block, so the card would be written as a held row with no fix report. Say that `hn` of 1 or more with an empty `frep` refuses (as `:490` does today). RF5 (4)'s last row catches it red; the card should say so.
3. NOTE X1: readers not named in `## NOT IN THIS JOB`: `preflight.sh:169-176`, `desk-launch.sh:157`, `:1671` (`house B: needed`). They stay on the stop line.
4. NOTE deploy blockers: (a) `deploy-smoke-string-1014` (537) deploys first (one deploy at a time). (b) 523's recut must land first (`hub-text-1013` was rolled back): RF2 keeps its two exemptions `FIX-ROUND REPORT (brain R1309):` and `§0 Headline`. (c) The order against 547 (ISSUE 1). (d) 546's `deploy-card.sh:38-39` edit shifts lines before `:483`: RF3-RF5 re-read by content (E3). (e) The deploy waits for this card's own check; BASE, TIP, CHECK REPORT and HOUSE B are the desk's.
5. NOTE: `tests/ops/test_build_hub_no_clutter.py::test_the_launch_line_is_byte_identical_to_base` (`:51-54`) equals BASE's `claude --bg ` line; cards 537 and 547 change that line, not this one. Not 548's.

PREFLIGHT DONE · card: result-file-1014 · checks: 20 · fails: 1 · ready: NO
