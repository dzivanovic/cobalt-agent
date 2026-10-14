# Card 548 `result-file-1014` — preflight round 5 (2026-10-14, read-only)

Read at `main` HEAD `dbe6ef76`. The card is committed there (last commit `dbe6ef76`). No test was run.

Round 4's one FAIL (RF2 (5) against card 547, the order) is repaired in text: the header and RF2 (5) name one order, 537, 523's recut, 547, then 548, and RF2 (5) edits the hunk 547 leaves. No FAIL stays.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <548 card>`; `git log --oneline -3 -- <548 card>` | diff empty; commits `dbe6ef76`, `6943792e`, `ae34ebf3` | OK |
| 2 | `grep -c "«FILL" <548 card>` | `0` | OK |
| 3 | header vs `CARD.md` (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS (+ CLASS, INSTALL, RESTARTS as card 547 carries them) | all present; empty fields are BASE, TIP (the desk's), CHECK REPORT, HOUSE B (the check's); no other placeholder | OK |
| 4 | `git diff --stat HEAD` over the 3 gates, `preflight.sh`, `card-fill.sh`, `desk-watch.sh`, `desk-done.sh`, `gate.sh`, 3 hubs, 7 test files, `restarts.py` | printed nothing: working files equal HEAD, so `Read` and `grep -n` of them are HEAD's | OK |
| 5 | RF2 (5) and the stated order against card 547 H1 (`547-db-copy-card.md`, now in `prompts/2026-10-14/`) | 547 H1 test (18) asserts only that `test_build_hub_no_clutter.py` holds a `startswith("- (b) THE LOCK")` filter, found by content, no `BASE`/`git show` assertion; 548 RF2 (5) keeps that literal as a tuple entry. Header says 537, 523 recut, 547, then 548, with BASE filled after 547's deploy; RF2 (5) names the body 547 leaves (filter on both sides plus equality on `base_lines()`) as the one it replaces. 547's own `## NOT IN THIS JOB` says the later deploy re-finds its lines by content. `grep` of the card: no "order does not matter" left | OK |
| 6 | RF3 anchors, `deploy-step0.sh` (`grep -n`) | `:69` `HERE=`, `:132` `rel()`, `:175` `held_n()`, `:649` `lits=`, `:657` clean pair prepended, `:699`/`:702` `held_n "$last"`, `:706` tip `grep -o`, `:721` `"BUILT ·"*"tip: $ctip"*`, `:727` fix-report why | OK |
| 7 | RF4 anchors, `deploy-card.sh` | `:480` `hash-object`, `:483` `last=`, `:486` `frep=`, `:487` `hn=""`, `:488` `[ -z "$frep" ] \|\| hn=$(held_n "$last")`, `:490-491` literals, `:501` `${frep#"$REPO"/}`, `:502` `flast`, `:505` `BUILT ·` tip, `:507`, `:524` SHIPS cell | OK |
| 8 | RF5 anchors, `desk-launch.sh` | `:264` `here=`, `:1136` `held_n()`, `:1450` `clast=`, `:1459` `ltip=`, `:1463` `fixed_ok`, `:1473` `BUILT ·` case, `:1479` `hn=$(held_n "$clast")`, `:1488` tip test | OK |
| 9 | `deploy-card.sh` has no `HERE` (RF4 uses `dirname "$0"`) | grep: `dirname` only at `:127` (`$out`); the idiom is `desk-launch.sh:264` `here=$(cd "$(dirname "$0")" && pwd)`; the card cites `:369` for the idiom, a line of that file I did not re-read, and the idiom itself is proved at `:264` | OK |
| 10 | RF4: `hn` read whenever a `.result` exists, a held stop line with empty `frep` refuses; RF5 (4) last row names it | stated in RF4 and in RF5 (4) | OK |
| 11 | `test_build_hub_no_clutter.py` at HEAD: `:15` `BASE`, `:27-30` `base_lines()`, `:51-54` launch-line test, `:57-60` `ls[:i] + ls[i + 2:] == base_lines()` | as the card names; RF2 (5) keeps `BASE`, `base_lines()` and the `git show` read | OK |
| 12 | each row's red test names its failing reason on BASE | RF1 exit 127; RF2 count 0 / `1 failed` / negative controls; RF3 `lacks 'held unfixed: 0'` / P2 passes / `does not end 'BUILT ·'`; RF4 `lacks 'held unfixed: 0'` / written; RF5 `its stop line lacks …` / launches; RF6 RUN | OK |
| 13 | no test pins a whole file, a whole fixed-file line equal to a commit, or a BASE literal | RF1, RF3-RF5 pin by content; RF2 (4) is a builder command, not an assertion; RF2 (5) keeps the existing `BASE` by design (brain R1472: an ordered-subsequence check by content with EXEMPT prefixes) | OK |
| 14 | stop line stays the finish signal (L71); the file is additional | `desk-watch.sh:40-44`, `desk-done.sh:24-31` in `## NOT IN THIS JOB`; no `.result` on `FAILED` or `SHADOW BUILT`; reports with no file are read as today | OK |
| 15 | the file carries only keys the stop line carries | 15 build keys, 22 check keys, one per stop-line field; `env` = `.env` named as the one exception, and RF1 (3) puts it in the helper's header | OK |
| 16 | each row's files hold its RESTARTS class home (K10) | `ops/desk/` operator script, `docs/40 - DevDocs/prompts/` DOCS, `tests/` no resident; RF6 expects none | OK |
| 17 | X1: readers outside the three gates | `card-fill.sh:66-78`, `preflight.sh:246-270`, `desk-launch.sh:1689-1698` (grep: `:1693`, `:1694`), `preflight.sh:169-176`, `desk-launch.sh:157` and `:1671` all in `## NOT IN THIS JOB` | OK |
| 18 | overlap with 521, 523, 537, 546, 549, 550 (`grep -o` of each card's `file:line`) | 546: `deploy-card.sh:38-39`, `desk-launch.sh:502-522, 541, 1727`, `BUILD-HUB.md:80, 105`, DEPLOY-HUB lines; 549: none; 550: `deploy-card.sh:29-31, 534-543`, `desk-launch.sh:994`; 537: `DEPLOY-HUB.md:11`, `desk-launch.sh:135-138, 2174-2189`, BUILD-HUB edits by content; 521: `BUILD-HUB.md:12, 65, 80-82`; 523: `BUILD-HUB.md:105, 111`, `DEPLOY-HUB.md:57-59`. None touches `deploy-step0.sh:677-733`, `deploy-card.sh:483-507`, `desk-launch.sh:1450-1489`, `BUILD-HUB.md:109`, `CHECK-HUB.md:125`. 546's `deploy-card.sh:38-39` and 550's `:29-31` shift later lines: the card says RF3-RF5 re-read by content | OK |
| 19 | overlap with 547 | 547 ranges: `BUILD-HUB.md:83`, `desk-launch.sh:1082-1089`, `gate.sh`, `gate-lists.md`; no line overlap with 548. Same test body `test_build_hub_no_clutter.py:57-60`: 547 deploys first, 548 replaces its body (check 5) | OK |
| 20 | 523 H3 (3) and RF2 both touch the BUILD-HUB no-clutter test: which first | 523's recut first (header: `hub-text-1013` was rolled back); RF2 (5) keeps any exemption 523 wrote (`FIX-ROUND REPORT (brain R1309):`, `§0 Headline`) and adds its own | OK |
| 21 | what blocks the card's own deploy | see ISSUE 1 | OK |

## ISSUES

1. NOTE deploy blockers, in order: (a) `deploy-smoke-string-1014` (537) deploys first (one deploy at a time); (b) 523's recut; (c) 547 (BASE of this card is filled after it, so RF2 (5) finds the body 547 left); (d) 546's `deploy-card.sh:38-39` edit (and 550's `:29-31`) shift RF3-RF5 lines, re-read by content (E3); (e) this card's own check (BASE, TIP, CHECK REPORT, HOUSE B are the desk's).
2. NOTE card 547 H1's own repair body (drop `- (b) THE LOCK` from both sides, then equality on `base_lines()`) has no exemption for the lines 537 and 523 change; if either deploys first, 547's builder meets a RED there. That is card 547's text, not this card's; RF2 (5) is not affected because it exempts those lines itself. The desk may want the same sentence in 547 (r4 ISSUE 1 asked for it; the amend-4 drafter did not touch 547).
3. NOTE RF2 "WRITTEN: with the file tool its launch line already allows": a new `.result` file is made with the Write tool, which the same `Edit(//Users/cobalt/cobalt-wt/**)` rule covers; if a seat's Write is refused, that is a launch-line fact, not a card edit. Unproved until the first build writes one.
4. NOTE the check's `.result` is read from the working file after a blob proof, the fix report's from `git show <head>`; RF3-RF5 say so and RF5 (4) tests that the three verdicts agree.

PREFLIGHT DONE · card: result-file-1014 · checks: 21 · fails: 0 · ready: YES
