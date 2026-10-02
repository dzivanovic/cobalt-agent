JOB: launcher-checks
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: ops/launcher-checks-1002
WORKTREE: launcher-checks-1002
BASE: 63649058
TIP:
REPORT: /Users/cobalt/cobalt-wt/launcher-checks-1002/docs/40 - DevDocs/reports/launcher-checks-build-2026-10-02.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: unchanged
RULINGS: 2026-10-02 R47, 2026-10-02 R39

## ROWS

WHY: three launches of 10-01 started a worker that failed in its first minute on something the desk had left undone (a ruling row not approved, check reports not committed, a tip that was a docs-only head). `desk-launch.sh` now runs those proofs itself and refuses BEFORE a session starts, printing the fix. Every refusal is `REFUSED: <what> — <the fix>` on stderr, exit 1, nothing launched, no worktree added.

| row | what | red first | files |
|---|---|---|---|
| L1 | THE RULING ROWS, for the kinds `build`, `check`, `deploy`, `devfix`: every `<date> R<n>` of the card's `RULINGS` (the value `none` needs no row), and the row a `HOUSE A` or `HOUSE B` line names after `overruled`, must be ONE line of `$REPORTS/cto-<date>.md` that starts bar, `R<n>`, bar and holds both `HIS RULING` and `APPROVED`, and must be committed (`git -C $REPO log -1 --format=%H -S` of that `R<n>` cell on that file non-empty). A miss refuses, naming the row and which of the three failed (no such row · not `HIS RULING` + `APPROVED` · not committed). One function, called from each of the four kinds after the card-committed check | `tests/ops/test_desk_launch_prechecks.py`, on the `desk` fixture shape of `tests/ops/test_devdb_lock.py` (a tmp repo with the fixed files, a job card, a deploy card, a stub `claude`) plus a committed `cto-2026-01-02.md` holding an approved row R1: a build launches (the stub `claude` is called). Then each of these refuses with its reason and the stub is NOT called: the card cites R2, which is absent; R1 reads `RECORD` instead of `HIS RULING`; R1 is `APPROVED` only in the working tree; a `HOUSE A: none — overruled 2026-01-02 R9` line whose row is absent. RED on `BASE`: the launches go through | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` |
| L2 | THE BUILD IS BUILT, kind `check`: the card's `REPORT` exists and its last non-blank line starts `BUILT · job: <JOB> · tip: <TIP>`; else `REFUSED: not built — <the line>`. A `PASS-2` launch keeps the test it has | in the same test file: a check launches on a report ending in the `BUILT` line for the card's job and tip; a last line `FAILED: W — x`, a `BUILT` line for another tip, a missing report → each refuses, the stub not called. RED on `BASE`: the three launch | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` |
| L3 | EVERY CHECK COMMITTED AND CLEAN, kind `deploy`, not on a `STEP-D0` resume (`DEPLOY-HUB.md` STEP-0 P2 and P3, run before the gate worktree is added). For each row of the card's `## SHIPS` table (columns: number, branch, code tip, branch head, check report, the literals its stop line must carry): the check report exists, is committed and unmodified; its last non-blank line holds every backticked literal of the row's last column; the line's `tip:` equals the row's code tip, or equals the row's branch head when that head adds only docs past the code tip; `git rev-parse --short=8 <branch>` equals the row's branch head; the code tip is an ancestor of the head; and `git diff --stat <code tip> <branch head> -- . ':(exclude)docs'` is empty (a head that adds only docs is accepted, as the hub accepts it). A miss refuses, naming the branch and the failed proof, with the fix (`commit <file>` · `the check is not clean: <line>` · `the head moved: <output>`) | in the same test file, on a deploy card with one `## SHIPS` row and a committed check report ending `CHECK DONE … tip: <tip> … held unfixed: 0 … ready: YES`: the deploy launches and the gate worktree is added. Then one fact broken at a time → each refuses, the stub not called, and NO gate worktree or branch exists afterwards: the report uncommitted; `ready: NO`; `held unfixed: 1`; a `src/` commit on the branch past the code tip; the row's branch head stale. A docs-only commit past the code tip (the row's head updated) launches. RED on `BASE`: every one launches | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` |
| L4 | THE WATCH LINE AND THE HEADER. After a launch of kind `build`, `check`, `deploy`, `devfix` or `close` that exits 0, the script prints on stdout one last line: `WATCH: sh <the folder this script was called from>/desk-watch.sh <kind> "<card or close report>"` (the desk runs that line in the background; `desk-watch.sh` is card 17's). Under `DESK_LAUNCH_DRY=1` it is printed after the dry lines. The header's lines 2–5 (`DRAFT — NOT INSTALLED — TESTED IN PART …`) are replaced by one line stating that this is the installed launcher (installed 2026-09-30, his R63) and that its kinds are tested in `tests/ops/` | in the same test file: the build launch's stdout ends with the `WATCH:` line naming `build` and the card; a refused launch prints no `WATCH:` line; `grep -c "NOT INSTALLED" ops/desk/desk-launch.sh` → 0, quoted. RED on `BASE`: no `WATCH:` line | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` |
| L5 | THE FIXTURES OF THE OTHER LAUNCHER TESTS. Row L1 makes every launch need its ruling row. The tmp cards of `tests/ops/test_devdb_lock.py`, `tests/ops/test_desk_launch_devfix.py` and `tests/ops/test_desk_size_guard.py` (where they launch a card) gain a committed `cto-<date>.md` with the approved row their `RULINGS` line cites, and the check card a report ending in the `BUILT` line L2 needs. Fixture lines only: no assertion of those files changes, and none is removed | RUN — asserts nothing new: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `0 failed`, quoted, with each of those files' test counts equal to their counts on `BASE` (quoted before and after) | `tests/ops/test_devdb_lock.py`, `tests/ops/test_desk_launch_devfix.py`, `tests/ops/test_desk_size_guard.py` |
| L6 | THE CLASSES, in `docs/40 - DevDocs/prompts/STANDING-LIST.md`: a new section `## CLASSES — approved once, 2026-10-02 R39`, placed after `## NEVER` and before the `.env` pattern section, in that file's table shape (string · for · can touch · never touches). (a) `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` and its installed spelling `Bash(sh /Users/cobalt/.claude/ops/*)`: any script under `ops/desk/` that reached `main` through a build, a check and a deploy; on his settings and on every fixed file's line. (b) `Bash(COBALT_ENV=dev uv run cobalt db *)`: any dev-only `cobalt db` verb, on the build, check, devfix and deploy lines; `Bash(COBALT_ENV=production*)` is DENIED on the build, check and devfix lines. (c) each kind's own report glob under `docs/40 - DevDocs/reports/`. And one sentence: a string inside a class is used and recorded and is not brought to him; a string outside every class is NEW and is asked for by itself. NO launch line changes in this job: the lines take the classes in tomorrow's adoption card | RUN — asserts nothing: `grep -n -F "## CLASSES" "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → one line; the section quoted whole in the report | `docs/40 - DevDocs/prompts/STANDING-LIST.md` |

## NOT IN THIS JOB
- Any launch line, allow string or `--add-dir` of a fixed file; `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, `DEVFIX-HUB.md`, `CARD.md`.
- The `devfix` kind and the `install-ops` kind as they stand on `BASE`; the desk-size guard; the lock tests' assertions.
- `RECUT`, a pre-check of the RESTARTS class homes of a card's files, the row and commit written by the launcher: tomorrow.
- `desk-watch.sh` itself (card `17`); the launcher only prints its line.
- `.claude/settings.json`.

## READ
- `ops/desk/desk-launch.sh` whole at `BASE`: `refuse`, `committed`, `check_paths`, `run_launch`, `field`, `need`, `section`, `commit_exists`, `lock_free`, the per-kind `case` (where L1–L3 are called), the last block (where L4 prints).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` STEP-0 P2 and P3; `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md` `## AUTHORIZATION`: the proofs L1 and L3 copy. The launcher runs the same commands; the hubs keep theirs.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CARD.md` `## SHIPS`: the table L3 parses.
- `tests/ops/test_devdb_lock.py`: the `desk` fixture and `launch` helper L1–L5 build on.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-10-01-1.md` `## DECISIONS` 1: the docs-only head L3 must accept.

## CHECK ASKS
- X1 Can a launch still start a worker whose first AUTHORIZATION or PREFLIGHT step is sure to fail on a ruling row, an uncommitted check report or a moved tip? Write the test.
- X2 Can a pre-check refuse a card the hub would accept (an old-shape check line with its own literals, a `RULINGS: none` deploy, a `STEP-D0` resume, a `PASS-2` launch)?
- X3 When L3 refuses, is any worktree, branch or file left behind?
- X4 Did any assertion of the three older test files change?

## RECORDS
- RESTARTS class homes: `ops/desk/desk-launch.sh` → the `ops/desk/` rule (card 15, on your base through 16 and 12); `tests/ops/*` → test/documentation (`restarts.py:239`); `docs/…` → DOCS (`:219`). No `src/`, no `configs/`. (the brain, 09:15 ET)
- The three launches this card would have refused: 10-01 R9 (build launched before his row was approved), 10-01 R6 (deploy with uncommitted check reports), `deploy-2026-10-01-1.md` DECISIONS 1 (a check `tip:` that was the docs-only head).
- The classes are his 2026-10-02 R39. `sh` is not on your line: the launcher runs only through its tests.
- His order sets aside the outside house for this card (`reports/brain-direction-2026-10-02.md` row 10).
