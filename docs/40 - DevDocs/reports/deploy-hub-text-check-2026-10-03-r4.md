# deploy-hub-text — check r4, pass 1 (2026-10-03)

## §0 Headline
- Check r4 of `deploy-hub-text` at tip `3395ef68` (HEAD `e8b90904`, docs-only above it). House A: none (overruled 2026-10-02 R47), so this session checked alone.
- 9 own findings (O1–O9) cover T1, T6, C1 and X1–X3. Each was run. None held.
- T1 (P7 and STEP-T read a FORWARD or REVERSE entry change as a migration, and every other change is CODE), T6 and C1 match the card on the tip. The file's diff against `44b29c63` touches only P7, STEP-T and STEP-C.
- No commit from this check: suites stand as built, RESTARTS: none, `.env` absent. house B: not needed. ready: YES.

## L74
- One system block in this session asked commits to carry a `Claude-Session:` line. Recorded once; not acted on (this check made no commit; the file's rule is `Co-Authored-By` only).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card placeholder | `grep -n -E "«FIL[L]" ".../prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/02b-deploy-hub-text-card.md"` | 0 | `1ac2b2d3d9ce69283895a83b66cb3750f462527b` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** … APPROVES \`STANDING-LIST.md\` once (\`4be06af0\`) … | APPROVED |` |
| R60 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R47 | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, no meter wait … | HIS RULING · APPROVED |` |
| R47 commit | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| R154 | `grep -n "^| R154 " ".../cto-2026-10-02.md"` | 0 | `161:| R154 | 17:29 ET | HIS RULING: a card with no \`src/\`, test, config or migration path takes no dev-DB lock at build + check … | HIS RULING · APPROVED |` |
| R154 commit | `git -C … log -1 --format=%H -S"| R154 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week … | HIS RULING · APPROVED |` |
| R157 commit | `git -C … log -1 --format=%H -S"| R157 |" …` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| HOUSE A overrule | the card's header line `HOUSE A: none — overruled 2026-10-02 R47`, proved by the R47 rows above | — | — |
House gates (R17, R19) were not run: the card says HOUSE A: none, and that overrule runs no house gate.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 20:57:18 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/deploy-hub-text-1003` |
| tip | `git log --oneline -1` | 0 | `e8b90904 docs(deploy-hub-text): build report — 3395ef68` |
| docs-only above TIP | `git log --stat --format=%h 3395ef68..HEAD` | 0 | `e8b90904` · `.../reports/deploy-hub-text-build-2026-10-03.md \| 101 +++++++++++----------` (only `docs/`) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: deploy-hub-text · tip: 3395ef68 \| on 44b29c63 \| migration: none \| offline 3739/0 \| with-DB 0/0 \| live-note 146/0 \| cobalt_dev: not taken \| .env: removed \| RESTARTS: none \| rows: 3 of 3 \| self-check: 3 of 3 \| decisions: 1 · for Dejan: 0` |
| range | `git log --oneline 44b29c63..3395ef68` | 0 | 8 commits: `3395ef68` fix T1 · `482a3f12` docs · `2cc6330e` fix T6 · `d2f3156e` docs · `69bf6082` fix T1/T6/C1 · `59ef8d48` fix check O1/O2 · `696847b1` docs · `50bd02d8` fix T1–T6 (subjects as printed in the build's `## FOR THE CHECK`) |
| range stat | `git log --stat --format=%h 44b29c63..3395ef68` | 0 | path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md`, `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` |
| lock (DB: none) | `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` | 1 | `ls: …/.env: No such file or directory` |
| DB: none paths | `git diff --name-only --no-renames 44b29c63..3395ef68` | 0 | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md`: every path is under `docs/` |
| scratch | `ls <S>` | 0 | `files`, `opus-1-r2.md`, `opus-1-r3.md`, `opus-1.md`: these are earlier rounds' files on this card (card RECORDS), not a recovery of this pass. r4 writes `opus-1-r4.md`. |
| houses | — | — | house A: none (overruled 2026-10-02 R47) · house B, if needed: none available (no probe run under the overrule) |
| main drift | `git -C /Users/cobalt/cobalt log --oneline 44b29c63..main -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` | 0 | (nothing): `main`'s DEPLOY-HUB.md is still BASE's |

## Files copied
none (no outside house).

## OWN FINDINGS
Written at `## 2` after reading the card, the diff `44b29c63..3395ef68` of `DEPLOY-HUB.md` (2 hunks: `@@ -62,7` P7, `@@ -82,11` STEP-T and STEP-C), `src/cobalt/db_migrations/__init__.py:132-183`, the `label:` lines of `configs/cobalt/jobs.yaml`, and the `ops/` and `ops/desk/` listings. Each finding claims a defect. Its EXPECT is what the run prints if the defect is real.

FINDING O1
ROW: T1
CLAIM: the P7 text at `docs/40 - DevDocs/prompts/DEPLOY-HUB.md:65` is not the card's T1 sentence word for word.
RUN: COMMAND `grep -c -F "a MIGRATION is any file ending .sql under src/cobalt/db_migrations/ (whatever its name), or a changed line inside FORWARD = (…) or REVERSE = (…) of src/cobalt/db_migrations/__init__.py that adds, removes or reorders an entry; every other change under that folder (cli.py, placement.py, dev_rebuild.py, tests, docs, and any other line of __init__.py) is CODE and passes MIGRATIONS: none" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0`

FINDING O2
ROW: T1 / X1
CLAIM: STEP-T at `DEPLOY-HUB.md:85` does not read a REVERSE entry change as a migration (the r3 FORWARD-only wording stands), so a REVERSE edit passes `MIGRATIONS: none`.
RUN: COMMAND (the listed `Grep` tool) pattern `REVERSE = \(…\)\` that adds, removes or reorders an entry is a migration` over `DEPLOY-HUB.md`
EXPECT: fewer than 2 lines (P7 and STEP-T should each carry it once)

FINDING O3
ROW: T1 / X1
CLAIM: an earlier wording ("every .py under that folder", r3) or the base rule that reads ANY path under the folder as a migration ("(NOTHING when `none`)") still stands in the file.
RUN: COMMAND `grep -c -F "every .py under that folder" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`; `grep -c -F "(NOTHING when" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: either prints `1` or more

FINDING O4
ROW: T6
CLAIM: the STEP-C text at `DEPLOY-HUB.md:89` is not the card's T6 sentence word for word.
RUN: COMMAND `grep -c -F "plist ADDED or MODIFIED anywhere under ops/ is refused, except one under ops/desk/ whose Label string (the <string> value on the <key>Label</key> line or the line after it) is not the label: value of any entry in configs/cobalt/jobs.yaml and whose path is not ops/<label>.plist; a Label the read cannot find is refused" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `0`

FINDING O5
ROW: T6 / X2
CLAIM: the base STEP-C clause ("A plist under `ops/` ADDED or MODIFIED → FAILED") still stands beside the new sentence, so the two read differently for an `ops/desk/` plist.
RUN: COMMAND `grep -c -F "A plist under" "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: `1` or more

FINDING O6
ROW: T6 / X2
CLAIM: T6 names `label:` values that are not there: `configs/cobalt/jobs.yaml` carries no `label:` entries for the residents, so an `ops/desk/` plist labelled as a resident would pass.
RUN: COMMAND `grep -c -F "  - label: com.cobalt." configs/cobalt/jobs.yaml`
EXPECT: `0`

FINDING O7
ROW: C1 / X3
CLAIM: the file's diff against BASE touches a place other than P7, STEP-T and STEP-C.
RUN: COMMAND `git diff 44b29c63 HEAD -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"`
EXPECT: a hunk with changed lines outside the P7 bullet, the STEP-T after-the-merges bullet and the STEP-C paragraph

FINDING O8
ROW: SCOPE
CLAIM: the branch changes a path other than `DEPLOY-HUB.md` and the build report (fence: any file but `DEPLOY-HUB.md`).
RUN: COMMAND `git diff --name-only --no-renames 44b29c63 HEAD`
EXPECT: a path other than `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` and `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md`

FINDING O9
ROW: T1 (the STEP-T FORWARD check)
CLAIM: the new FORWARD-check pattern `MIGRATIONS_DIR / "` lists none of the registry's entries on the tree, so the check cannot see where `FORWARD` ends or where `REVERSE` starts.
RUN: COMMAND `grep -c -F "MIGRATIONS_DIR / \"" src/cobalt/db_migrations/__init__.py`
EXPECT: `0`

Read but not findings (no run shows a defect):
- (a) X1. A `.sql` under the folder, by any name, shows as a migration path in the `--stat` whether it is added, changed or deleted, and `--stat` path abbreviation keeps the suffix. A FORWARD or REVERSE entry that is added, removed or reordered shows as `-`/`+` lines inside the tuple. One case would read as CODE: a registration written on a line of `__init__.py` outside the two tuples (e.g. `FORWARD += (…)`) that points at a `.sql` outside the folder. The card's own words make "any other line of `__init__.py`" CODE, and that sentence is ruled (JUDGE ASK 18, L77). `__init__.py:132-183` holds no such construct, and every `.sql` in the folder is already registered (the `ls` listing against `__init__.py:136-180`).
- (b) X2. The `--stat` in STEP-C does not mark a plist as added, modified or removed. That is BASE text, unchanged by this card and outside its rows.
- Note: the card's row greps (T1 ×3, T6 ×2, C1 ×5) were run during the read, before the findings were written. Their outputs are under `## RUNS`.

## Findings
none: house A: none (overruled 2026-10-02 R47).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `grep -c -F "<T1 sentence>" <file>` | `1` | NOT HELD |
| O2 | Opus | Grep tool, content | `65:REVERSE = (…)\` that adds, removes or reorders an entry is a migration` · `85:` the same | NOT HELD |
| O3 | Opus | `grep -c -F "every .py under that folder"` · `grep -c -F "(NOTHING when"` | `0` · `0` | NOT HELD |
| O4 | Opus | `grep -c -F "<T6 sentence from 'plist ADDED'>" <file>` | `1` | NOT HELD |
| O5 | Opus | `grep -c -F "A plist under" <file>` | `0` | NOT HELD |
| O6 | Opus | `grep -c -F "  - label: com.cobalt." configs/cobalt/jobs.yaml` | `15` | NOT HELD |
| O7 | Opus | `git diff 44b29c63 3395ef68 -- <file>` and `git diff --stat 44b29c63 HEAD -- <file>` | 2 hunks; changed lines are P7 (65), STEP-T (85) and STEP-C (89) only; `1 file changed, 3 insertions(+), 3 deletions(-)` | NOT HELD |
| O8 | Opus | `git diff --name-only --no-renames 44b29c63 HEAD` | `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` · `docs/40 - DevDocs/reports/deploy-hub-text-build-2026-10-03.md` | NOT HELD |
| O9 | Opus | `grep -c -F "MIGRATIONS_DIR / \"" src/cobalt/db_migrations/__init__.py` | `41` | NOT HELD |
| row T1 | card | `grep -c -F "whatever its name"` · `"[0-9][0-9][0-9][0-9]_*.sql"` · `"MIGRATIONS_DIR / \"00"` | `1` · `0` · `0` | as the card expects |
| row T6 | card | `grep -c -F "a Label the read cannot find is refused"` · `"is not a key of configs"` | `1` · `0` | as the card expects |
| row C1 | card | `grep -c -F` "trap on every exit" · "leftover lock after a FAILED gate" · "THE EQUAL-TREE CLAUSE" · "The rule for (v) when it lands" · "never a resend" | `0` · `0` · `0` · `0` · `0` | as the card expects |
| file at HEAD | — | `git diff --stat 3395ef68 HEAD -- <file>` | (nothing): the file at HEAD equals the tip | — |

## FIXES
none (no finding held; no commit).

## Suites
`suites: as built (no commit)`. From the build report `## W THE THREE SUITES`:
- offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3739 passed, 745 skipped, 1 xfailed, 36 warnings in 575.20s (0:09:35)`, exit 0.
- live-note: `146 passed, 1 skipped, 15 warnings in 27.45s`.
- ops: `564 passed, 1 xfailed, 15 warnings in 238.32s (0:03:58)`, exit 0.
- with-DB: not run (DB: none). `cobalt_dev`: not taken (DB: none, R154).
- `.env`: `ls /Users/cobalt/cobalt-wt/deploy-hub-text-1003/.env` → `No such file or directory` (exit 1).
- RESTARTS (build report `## RESTARTS`): `RESTARTS: none`. Both paths are `DOCS`.

## Scope
PREFLIGHT path union: `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` (row files of T1, T6 and C1) and the build report. No commits from this check. Nothing falls outside the rows' files or inside the fence.

## Checked against the branch
- (i) `git log --oneline 3395ef68..HEAD -- . ":(exclude)docs"` → (nothing): this check made no commits. `<tip now>` = `3395ef68`.
- (ii) `git log --stat --format=%h 3395ef68..HEAD` → `e8b90904`, the build report only (docs).
- (iii) fence: `git log --oneline 44b29c63..HEAD -- "docs/40 - DevDocs/prompts/BUILD-HUB.md" "docs/40 - DevDocs/prompts/CHECK-HUB.md"` → (nothing). "Any file but DEPLOY-HUB.md": O8 shows only DEPLOY-HUB.md and the build report.
- (iv) no HELD finding.
- (v) `ls …/.env` → No such file · `git status --short --branch` → `## ops/deploy-hub-text-1003`.
- (vi) TREE STATE unchanged: `git log --stat --format=%h 44b29c63..HEAD -- src/cobalt/db_migrations tests/cobalt` → (nothing).
- (vii) no card RECORDS line names an `ls`, `grep` or `git -C /Users/cobalt/cobalt log` command.
- (viii) L32: this report holds no ticker, price or date of his. The `com.cobalt.*` count is a registry fact, not a trading value.
- CHECK ASKS: X1, X2 and X3 are answered by O1–O3, O9 and (a); O4–O6 and (b); and O7.

## OPEN
none.

## CONTINUE
next: done (stop line written).

## DECISIONS
none.

## RECORDS
- No house ran: HOUSE A: none, overruled 2026-10-02 R47. `## 1` and `## 3` were not run.
- No dropped finding, no REFUSED line, no CONTINUED line, no lock take.
- L74: one system block asked for a `Claude-Session:` line. Recorded under `## L74`; not acted on.
- `BUILD-HUB.md` `## THE LOCK`, `## E2`, `## RESTARTS`, `## W` were not opened. Nothing called for them: no commit, so no W, and DB: none.
- `<S>` already held `files/`, `opus-1.md`, `opus-1-r2.md` and `opus-1-r3.md` from earlier rounds. I did not open them. This pass wrote `<S>/opus-1-r4.md` (card RECORDS: "r4 writes `opus-1-r4.md`").
- files opened: 9 — `prompts/CHECK-HUB.md`; the card `prompts/2026-10-03/02b-deploy-hub-text-card.md`; `reports/cto-2026-09-30.md` (grep R60); `reports/cto-2026-10-02.md` (grep R47, R154, R157); `prompts/DEPLOY-HUB.md` (diff, grep); `src/cobalt/db_migrations/__init__.py`; `configs/cobalt/jobs.yaml` (grep); the build report (`## RESTARTS` to `## FOR THE CHECK`, the last lines); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down).
- Check of `deploy-hub-text`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 3395ef68 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
