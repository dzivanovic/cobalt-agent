# preflight-fixes card 20 — preflight round 3 (row F3), 2026-10-05

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git log --oneline -- <card>` | `98d77082`, `f29e19fb`, `bb394622`, `e7cebe73` | OK |
| 1b | `git diff -U0 bb394622 HEAD -- <card>` (F1/F2 vs round 2) | only: RULINGS line `R387, R412` → `R412`; "Two rows" → "Three rows"; F3 row added; "these two rows" → "these three rows". F1 and F2 rows unchanged | OK |
| 1c | `git rev-parse b56622fa` / `merge-base --is-ancestor b56622fa main` | `b56622fa8f88335c347109048c424303579f3682` / exit 0 (no output); card header `BASE: b56622fa` | OK |
| 1d | header | `BRANCH: ops/preflight-fixes-1005`, `WORKTREE: preflight-fixes-1005`, `TIP:`, `CHECK REPORT:`, `HOUSE B:` all empty; `DB: none` | OK |
| 2a | `grep -n -E "^\| (R387\|R412) " cto-2026-10-05.md` | line 62 `\| R387 \| … HIS RULING (L79, via brain) …`; line 109 `\| R412 \| … HIS RULING: …` | OK |
| 2b | `git grep -c -E "^\| (R387\|R412\|R425) " HEAD -- cto-2026-10-05.md` | `3` (all three rows are in HEAD). The file's only uncommitted diff is one added wake-up row at line 140 (preflights 34-36), not an R row | OK |
| 2c | `grep -n "^\| R425 "` | line 133 `\| R425 \| 10-05 13:49 ET \| DESK RECORD: brain ruled (1) row F3 on card 20 for test_desk_launch_brain.py:285 (builder refused CONTINUE, BUILD-HUB rule b → card amend + relaunch); (2) card 26 rows … \| RECORD \|` | OK (a DESK RECORD that reports the brain's ruling; it carries no verbatim quote) |
| 3a | `grep -n "assert INSTALL" tests/ops/test_desk_launch_brain.py` (same file, no diff to BASE: `git diff --stat b56622fa main -- <test> <hub>` empty); `git show b56622fa:<test>` | `285:    assert INSTALL in text  # the title token stands until his approval row` | OK |
| 3b | `git show b56622fa:"docs/40 - DevDocs/prompts/BRAIN-HUB.md"` line 1 | `# BRAIN-HUB — the standing brain seat (installed 2026-10-05 on his 2026-10-02 R54 (FOR DEJAN 13 = A) at the R350 brain restart)` | OK |
| 3c | `git merge-base --is-ancestor 4a19b075 b56622fa`; `git log -1 --format="%h %s" 4a19b075` | exit 0 (no output); `4a19b075 docs(desk): R357 wake-up ecc18b72; R358 BRAIN-HUB installed on R54 for the brain restart` | OK |
| 3d | `grep -n "^\| R358 "` in `cto-2026-10-05.md` | line 31 `\| R358 \| 10-05 06:58 ET \| DESK RECORD (R350, 10-02 R54): … filled from R54 in BRAIN-HUB.md line 1.` | OK |
| 4a | read of the test at BASE: `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` (line 285) | `INSTALL = "«INSTALL"`; the BASE title (3b) holds no `«INSTALL`, so `assert INSTALL in text` fails there. The test is not run | OK (claim is true) |
| 4b | CARD.md `red first` rule: "the test … named, with the assertion it fails on" | F3's `red first` cell reads only "the line as it stands fails on main". It names no test and no assertion, and says `main` where the F1 and F2 rows say `BASE` | FAIL |
| 4c | negative control | the card names none for F3 and none is needed ("a negative control, if any") | OK |
| 5a | F3 `files` cell | `tests/ops/test_desk_launch_brain.py` only; `BRAIN-HUB.md` is not named in any row's files | OK |
| 5b | `## NOT IN THIS JOB` | five bullets, the same as before: `BUILD-HUB.md`/`CHECK-HUB.md`/fixed files; PASS-2 rows; other `preflight.sh` rules; a new argument or command; "A red outside these three rows". No bullet excludes the `test_desk_launch_brain.py` red | OK |
| 5c | row counts | WHY "Three rows"; table F1, F2, F3; NOT IN THIS JOB "these three rows" | OK |
| 6a | R411 / R412: any new command or argument | none in F3 (a one-line test edit); the card's own bullet bars a new argument; RECORDS says the build uses only the existing scripts and its allow line | OK |
| 6b | `grep -c -F "«FILL" <card>` | `0` | OK |
| 6c | `git diff --stat -- <card>` / `git log -1 --format=%h -- <card>` | empty / `98d77082` (committed, clean) | OK |

## ISSUES
- 4b: F3's `red first` cell names no test and no assertion (CARD.md asks for both) and says `main` rather than `BASE`. Fix: name `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled` and `assert INSTALL in text` (line 285), fails on BASE `b56622fa` because the hub title reads `installed 2026-10-05`, not `«INSTALL`. The red itself is real, so this is a one-cell amend.

Notes (not FAILs): `RULINGS` now lists only `R412` (R387 is in `LADDER`); R425, the brain's F3 ruling, is a desk record and is not in `RULINGS`. The desk may add it.

PREFLIGHT DONE · card: preflight-fixes-20 · checks: 19 · fails: 1 · ready: NO
