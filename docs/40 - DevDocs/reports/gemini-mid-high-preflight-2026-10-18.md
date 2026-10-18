# Preflight: Gemini shadow cards 718 (MID `radar-display-fix-1018-gemini`) and 719 (HIGH `s4-p1-1018-gemini`), 2026-10-18

Read-only. Nothing launched, run or committed. Cards: `prompts/2026-10-18/718-shadow-radar-display-fix-1018-gemini-card.md`, `…/719-shadow-s4-p1-1018-gemini-card.md`. Precedents: `prompts/2026-10-11/369-…-sonnet-card.md`, `372-…-sonnet-card.md`.

## CHECKS

| # | card | command | output | OK/FAIL |
|---|---|---|---|---|
| 1 | 718, 719 | `git -C /Users/cobalt/cobalt log --oneline -n 3 -- <718> <719>` | One commit for both: `4f130ff1 docs(desk): R1840 Gemini shadow cards drafted, preflight prompts`. Committed. | OK |
| 2 | 718, 719 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- <718> <719>` | Empty. No change against HEAD. | OK |
| 3 | 718, 719 | Header read against `desk-launch.sh` (`grep -n shadow`, `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` at `:1030`, shadow arm `:1717-1751`, `field SHADOW OF`) | Both headers hold JOB, LADDER, BRANCH, WORKTREE, BASE, REPORT, RULINGS and `SHADOW OF:`, plus CHECK REPORT, HOUSE B and PRECONDITION. `TIP:` is empty: `need` does not list TIP for build or shadow, and the 10-11 cards got theirs only after the build. REPORT is under `/Users/cobalt/cobalt-wt/<WORKTREE>/docs/40 - DevDocs/reports/` (the `:1705` pattern). | OK |
| 4 | 718, 719 | JOB suffix (`:1740-1743`: `*-"$slug"`); the `gemini` row of `SHADOW-HUB.md` `## BUILDERS` (`:22`) | JOB `radar-display-fix-1018-gemini` and `s4-p1-1018-gemini` both end `-gemini`, the slug of the `gemini-4-argon-high` row. The job chars are `[a-z0-9-]`. | OK |
| 5 | 718, 719 | BRANCH, WORKTREE vs `:1723-1726` and `:1708-1714`; `ls /Users/cobalt/cobalt-wt`; `git branch --list "shadow/*1018*"` | BRANCH `shadow/radar-display-fix-1018-gemini-4-argon-high` and `shadow/s4-p1-1018-gemini-4-argon-high` start `shadow/`. Neither worktree dir exists in `cobalt-wt`. Neither branch exists. | OK |
| 6 | 718, 719 | Placeholder scan: `«FILL`, `«INSTALL`, `«SIGN`, `<…>` tokens | None in either card. The `<this card>` in `## ARM` is the desk's launch-line token. Only `TIP:` is blank (check 3). `SHADOW-HUB.md` is clean on `git diff HEAD --stat` and its `gemini` row holds no `«SIGN` (`:22` reads `HIS RULING · APPROVED`). | OK |
| 7 | 718 | `git diff --no-index <369 sonnet card> <718>` | Differences are the header (JOB, BRANCH, WORKTREE, TIP, REPORT, CHECK REPORT, RULINGS gains `2026-10-17 R1738`, PRECONDITION added), the added `## ARM` block, and one last `RECORDS` line. `## ROWS`, `WHY`, `## NOT IN THIS JOB`, `## READ`, `## CHECK ASKS` and the other `## RECORDS` lines have no hunk: byte for byte. | OK |
| 8 | 719 | `git diff --no-index <372 sonnet card> <719>` | Same shape: header, `## ARM`, one added `RECORDS` line. `## ROWS` (M1 to D1), the deploy gate, RESTARTS, `## DECISIONS`, `## NOT IN THIS JOB`, `## READ`, `## CHECK ASKS` have no hunk. | OK |
| 9 | 718 | `git -C /Users/cobalt/cobalt show --stat --format=%h%x20%cs%x20%s 50b0cd87 --no-patch`; BASE of 369 | `50b0cd87 2026-10-08 docs(desk): radar display-fix drafter 55902983 launched`. A commit. 369 reads `BASE: 50b0cd87`, same value. | OK |
| 10 | 719 | `git -C /Users/cobalt/cobalt show --stat --format=%h%x20%cs%x20%s e4586978 --no-patch`; BASE of 372 | `e4586978 2026-10-09 Merge branch 'main' into deploy/radar-top50-1009`. A commit. 372 reads `BASE: e4586978`, same value. | OK |
| 11 | 718, 719 | `grep -n -i argon SHADOW-HUB.md`; `## ARM` bullets; `desk-launch.sh` `:405` | Both name `gemini-4-argon-high` only, "Medium and low are not run". The hub holds the one row (`:22`, 1 row, signed). The launcher refuses any other Gemini id at `:405`. | OK |
| 12 | 718, 719 | `## ARM` bullet "Never merged, never deployed" | Present in both. BRANCH is under `shadow/`. | OK |
| 13 | 718, 719 | `## ARM` bullet "The Opus gate seat (SHADOW-HUB) runs every command"; `SHADOW-HUB.md:3` | Both name the Opus gate seat; the hub is `MODEL: Opus 5.5 (claude-opus-5-5)`, permission mode `dontAsk`, and "You are never the builder". | OK |
| 14 | 718, 719 | `grep -n PRECONDITION` on both | `:12 PRECONDITION: the X1 result is a DESK RECORD row and is clean`, in the header (above the first blank line). Text exact. | OK |
| 15 | 718, 719 | RULINGS rows via `ruling_row` (`:295-322`): `grep -n "^\| R<n> \|"` in `cto-<date>.md`; `git diff -U0 HEAD` on those files | R685 (`cto-2026-10-08.md:38`), R1069 (`cto-2026-10-11.md:74`), R598 (`cto-2026-10-06.md:97`), R1738 (`cto-2026-10-17.md:96`): each has one row with `HIS RULING` and `APPROVED`. `cto-2026-10-17.md` has no diff against HEAD. `cto-2026-10-08.md` differs from HEAD by one deleted `OWED` line (`:93`), not a ruling row; `git log -S"\| R685 \|"` finds `e1edc838`. | OK |
| 16 | 718, 719 | Command scan of both cards (`## ARM`, `## ROWS`, deploy gate, RESTARTS) | Launch line is the standing `sh /Users/cobalt/.claude/ops/desk-launch.sh shadow "<card>" --model gemini-4-argon-high`. Row proofs use `uv run pytest`, `COBALT_ENV=dev uv run pytest`, `uv run cobalt jobs restarts`, `grep -c -F`, `git show`/`diff`. The 719 live-measure line (`uv run cobalt strike measure …`, D1) is the desk's after the check, and `## NOT IN THIS JOB` forbids running it. `agy` appears only as the row's allow string of `SHADOW-HUB.md:22`. The cards add no new command string (R411/R412). | OK |
| 17 | 718, 719 | `grep -rn "X1 RESULT" prompts/2026-10-18`; `grep -n X1 reports/cto-2026-10-18.md` | No `X1 RESULT:` DESK RECORD row exists. R1835 (X1 is step 0 of the LOW card 717) and R1840 (MID/HIGH held until the X1 row) are the only X1 rows, and they set the rule. Card 717 has not run. | FAIL (open, blocks launch) |

## ISSUES

- B1 BLOCKS THE LAUNCH: the X1 result is not yet a DESK RECORD row (check 17). Card 717 (LOW) has to run its step 0 first. If it says `X1 RESULT: clean` and the desk writes that row, launch 718 and 719. If it says `decoy read` or `cwd taken in`, neither launches (K5 cwd-pin card first, R1804). The launcher does not read `PRECONDITION:` (R1840 and the 10-18 STATE line say so), so the desk's hold is the only gate.
- N1 NOTE: the two BASEs are old (718 `50b0cd87`, 10-08; 719 `e4586978`, 10-09), while main is `21d7c3e9` per the desk STATE. The cards took them from the 10-11 arms on purpose, so all three arms of a job build from the same tree. The cited `file:line`s are therefore proven at the BASE and not at main.
- N2 NOTE: the `TIP:` line is empty on both. The launcher's `build|shadow` arm does not require it. The desk fills TIP after the build, as the 10-11 cards did.
- N3 NOTE: the 719 DECISIONS D1 to D8 carry the desk's defaults, as card 372 did. The 719 D1 live run is a command string on no seat's allow line. It is the desk's, after the check, and is not part of this job.
- N4 NOTE: this seat did not run the `desk-launch.sh` gates; they were read only. `tree_state` is a no-op (no `TREE STATE:` key in either card).

PREFLIGHT DONE · cards: radar-display-fix-1018-gemini, s4-p1-1018-gemini · checks: 17 · fails: 1 · ready: YES
