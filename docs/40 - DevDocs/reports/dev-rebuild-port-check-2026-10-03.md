# dev-rebuild-port — CHECK, pass 1 (2026-10-04)

## §0 Headline
Pass 1 of `dev-rebuild-port` at `f5689418`, Opus alone (house A none, overruled 2026-10-02 R47). 9 own findings, every one run.
X1 / X1b / X2 / X3 hold for the port: hash pairs equal, P3 is exactly two stub lines, no line of `07cc965f` or `05c8b7fa` lost, `13`'s guard tests hit the ported hook. With both real reads the proof-only order is proof table, SLOTS, `code:`, FINGERPRINT, TABLES (O1, run green, removed).
One held: O8, a stale `_code_line` docstring (`cli.py:169`). Its fix is fenced (a line in neither parent), so it's out of scope and goes to `## DECISIONS` 1.
No commit; suites as built. `ready: YES`, house B not needed.

## L74
- At session start a system reminder asked commits to end with a `Claude-Session:` line. Recorded once here as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sun Oct  4 14:09:53 EDT 2026` |
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/11b-dev-rebuild-port-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/11b-dev-rebuild-port-card.md"` | 0 | `e42d24ae77430f26965263be5ba2dffd5675a575` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING 2026-09-30 R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...) APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING 2026-10-02 R47 (also the HOUSE A overrule) | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` |
| R47 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING 2026-10-02 R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week ... | HIS RULING · APPROVED |` |
| R157 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gate R17 | `grep -n "^| R17 " ".../cto-2026-09-24.md"` | 0 | `35:| R17 | 07:32 ET | His words: ... STANDING: Bash(grok *) is a PRE-APPROVED string ... | APPLIED ... |` |
| house gate R19 | `grep -n "^| R19 " ".../cto-2026-09-24.md"` | 0 | `37:| R19 | 07:36 ET | His words: ... STANDING: the four house strings are pre-approved ... | APPLIED ... |` |
| R19 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- ".../cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/dev-rebuild-port-1003` |
| tip | `git log --oneline -1` | 0 | `53fed116 docs(dev-rebuild-port): build report — f5689418` |
| docs-only above TIP | `git log --stat --format=%h f5689418..HEAD` | 0 | `53fed116` · `.../reports/dev-rebuild-port-build-2026-10-03.md | 123 ++++…` (docs only) |
| built | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: dev-rebuild-port · tip: f5689418 | on 5ff16b1f | migration: none | offline 3782/0 | with-DB 856/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 5ff16b1f..f5689418` | 0 | `f5689418 fix(...) port 11 ... and 13 ...` · `71d6eb50 wip(...) E3 — P2 and BASE contradict ...` · `10ca044c wip(...) red — 11's and 13's tests ...` (3 commits) |
| range stat | `git log --stat --format=%h 5ff16b1f..f5689418` | 0 | f5689418: `tests/cobalt/test_dev_rebuild_cli.py +1`, `tests/cobalt/test_migrate_level.py +1` · 71d6eb50: `docs/.../db_migrations/cli.md +6`, `docs/.../db_migrations/dev_rebuild.md +24`, `reports/dev-rebuild-build-2026-10-02.md +210`, `reports/dev-rebuild-port-build-2026-10-03.md +142`, `reports/slot-guard-build-2026-10-02.md +315`, `src/cobalt/db_migrations/cli.py 235 +/-`, `src/cobalt/db_migrations/dev_rebuild.py +879`, `tests/cobalt/conftest.py +45` · 10ca044c: `tests/cobalt/test_dev_rebuild_cli.py +463`, `tests/cobalt/test_dev_rebuild_db.py +249` |
| lock (own) | `ls <WT>/.env` | 1 | `No such file or directory` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)` — card header `HOUSE A: none — overruled 2026-10-02 R47`; no house gate run as a launch gate, no probe. `HOUSE B: as needed` |

Path union (for `## Scope`): `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/conftest.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py`, `tests/cobalt/test_migrate_level.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, three reports under `docs/40 - DevDocs/reports/`.

## Files copied
none — house A: none (overruled 2026-10-02 R47); `## 1` not run.

## OWN FINDINGS
Written before any run of step 4 (the git reads below were part of the read, (3)). No house list exists to open.

FINDING O1
ROW: X1b (P3)
CLAIM: With neither seam stubbed, the merged `--proof-only` path (`src/cobalt/db_migrations/cli.py:844`–`856`) does not print proof table, SLOTS, `code:`, FINGERPRINT, TABLES in that order, or sends the slot read's statements anywhere but before the level read's; no test runs both real reads together (P3's stubs each silence one side: `tests/cobalt/test_dev_rebuild_cli.py:331`, `tests/cobalt/test_migrate_level.py:159`).
RUN: TEST — `tests/cobalt/test_dev_rebuild_cli.py`, `test_check_o1_proof_only_runs_both_real_reads_in_the_ruled_order` (a `SlotConn` subclass answering `FINGERPRINT_SQL`'s `fetchone`; real `_slot_lines` and real `_level_lines`; `_probe_all`, `_print_probe`, `_code_line` stubbed as `_migrate_output` does).
EXPECT: on a defect, `lines[-5:] == ["<proof table>", WARN_FULL, "<code line>", "FINGERPRINT …", "TABLES …"]` or the statement-order assertion fails.

FINDING O2
ROW: X1
CLAIM: `tests/cobalt/test_dev_rebuild_cli.py` is not `05c8b7fa`'s plus the one P3 (a) line, or `13`'s build report is not byte-equal.
RUN: COMMAND — `git diff 05c8b7fa f5689418 -- tests/cobalt/test_dev_rebuild_cli.py "docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md"`
EXPECT: on a defect, more than the one `+    monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])` line, or a hunk in the report.

FINDING O3
ROW: X1
CLAIM: `11`'s build report `docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md` is not byte-equal to `07cc965f`'s.
RUN: COMMAND — `git diff 07cc965f f5689418 --stat -- "docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md"`
EXPECT: on a defect, one stat line.

FINDING O4
ROW: X2
CLAIM: A line of `05c8b7fa` (which carries `11`'s build and `13`) is lost or changed in the settled `src/cobalt/db_migrations/cli.py` or `docs/40 - DevDocs/cobalt/db_migrations/cli.md`.
RUN: COMMAND — `git diff 05c8b7fa f5689418 -- src/cobalt/db_migrations/cli.py "docs/40 - DevDocs/cobalt/db_migrations/cli.md"`
EXPECT: on a defect, a `-` line in either file.

FINDING O5
ROW: X2
CLAIM: A line of `11`'s check fix (`07cc965f`) is lost in `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_db.py` or `dev_rebuild.md`.
RUN: COMMAND — `git diff 07cc965f f5689418 -- src/cobalt/db_migrations/dev_rebuild.py tests/cobalt/test_dev_rebuild_db.py "docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md"`
EXPECT: on a defect, a `-` line, or a `+` hunk other than `13`'s own (`git diff 1df251b9 05c8b7fa -- <same paths>`).

FINDING O6
ROW: X2
CLAIM: A line of `13`'s slot-guard block in `tests/cobalt/conftest.py` is lost or weakened by the hand-merge with BASE's G1 / P1 lines.
RUN: COMMAND — `git diff 1df251b9 05c8b7fa -- tests/cobalt/conftest.py` beside `git diff 5ff16b1f f5689418 -- tests/cobalt/conftest.py`
EXPECT: on a defect, the two `+` blocks differ.

FINDING O7
ROW: X3
CLAIM: `13`'s guard tests (`tests/cobalt/test_dev_rebuild_cli.py:381`–`464`) do not reach the ported `tests/cobalt/conftest.py` hook and the ported `cobalt.db_migrations.dev_rebuild`.
RUN: COMMAND — `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py -k s2`
EXPECT: on a defect, an error, a skip or `0 selected`.

FINDING O8
ROW: SCOPE (P1 / P2 docstrings)
CLAIM: `_code_line`'s docstring (`src/cobalt/db_migrations/cli.py:169`–`171`, BASE's words) says the code line is "the line after the proof table" in both outputs, but the merge prints the SLOTS line(s) between them (`cli.py:851`–`854`; forward `:933`–`937`).
RUN: COMMAND — `grep -n -F "The line after the proof table" src/cobalt/db_migrations/cli.py`
EXPECT: `169:    The line after the proof table in both the proof-only and the forward`.

FINDING O9
ROW: SCOPE (fence: no `git merge` / `rebase` / `cherry-pick`)
CLAIM: A commit in the range is a merge.
RUN: COMMAND — `git log --merges --oneline 5ff16b1f..f5689418`
EXPECT: on a defect, one line.

## Findings
none — no house.

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | Edit added `_LevelSlotConn` + `test_check_o1_proof_only_runs_both_real_reads_in_the_ruled_order` to `tests/cobalt/test_dev_rebuild_cli.py`; `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py::test_check_o1_proof_only_runs_both_real_reads_in_the_ruled_order` | `1 passed in 0.05s` | NOT HELD — removed again by Edit; `git status --short --branch` → `## ops/dev-rebuild-port-1003` (tree back at the tip). X1b answered: with both real reads the output is proof table, SLOTS, `code:`, FINGERPRINT, TABLES; statements SAVEPOINT, SELECT, RELEASE, then `SET LOCAL search_path`, `FINGERPRINT_SQL`; nothing committed |
| O2 | own | `git diff 05c8b7fa f5689418 -- tests/cobalt/test_dev_rebuild_cli.py "docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md"` | one hunk `@@ -328,6 +328,7 @@`, one line `+    monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])`; nothing for the report | NOT HELD |
| O3 | own | `git diff 07cc965f f5689418 --stat -- "docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md"` | (nothing) | NOT HELD |
| O4 | own | `git diff 05c8b7fa f5689418 --stat -- src/cobalt/db_migrations/cli.py "docs/40 - DevDocs/cobalt/db_migrations/cli.md"` (and the full diff, read) | `cli.md | 3 +` · `cli.py | 114 +++…-` · `116 insertions(+), 1 deletion(-)`. The one `-` is `    The LAST line of both the proof-only and the forward output, so a`, replaced by BASE's docstring; `git log --oneline -S"The LAST line of both the proof-only and the forward output, so a" -- src/cobalt/db_migrations/cli.py` → `d483a417 wip(adoption-port): …` (BASE's chain removed it) · `50deb26c feat(db-migrate): …` (added before `11`). Every `+` is BASE's (FINGERPRINT / TABLES / level lines, `"FINGERPRINT_SQL"`) | NOT HELD — no line of `11` or `13` lost |
| O5 | own | `git diff 07cc965f f5689418 --stat -- src/cobalt/db_migrations/dev_rebuild.py tests/cobalt/test_dev_rebuild_db.py "docs/.../dev_rebuild.md"` beside `git diff 1df251b9 05c8b7fa --stat -- <same>` | both: `dev_rebuild.md | 3 +` · `dev_rebuild.py | 68 +…` · `test_dev_rebuild_db.py | 24 +…` · `95 insertions(+)`; full diffs read: same hunk text, offsets only | NOT HELD — X2: `11`'s O1–O5 kept whole, `13`'s hunks identical |
| O6 | own | `git diff 1df251b9 05c8b7fa -- tests/cobalt/conftest.py` beside `git diff 5ff16b1f f5689418 -- tests/cobalt/conftest.py` | both one `+45` block, `_SLOTS_WARN`, `pytest_sessionstart`, `pytest_terminal_summary`, text identical | NOT HELD |
| O7 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py -k s2` | `9 passed, 22 deselected in 0.05s` | NOT HELD — X3: `_suite_conftest` resolves `tests/cobalt/conftest.py` (the ported one, `test_dev_rebuild_cli.py:395`–`403`) and patches the ported `cobalt.db_migrations.dev_rebuild.slot_report` (`:420`, `:427`); builder's P2-M2 mutation showed the hook test red |
| O8 | own | `grep -n -F "The line after the proof table" src/cobalt/db_migrations/cli.py` | `169:    The line after the proof table in both the proof-only and the forward`; `grep -n -F "for line in slots" src/cobalt/db_migrations/cli.py` → `852:`, `934:` (SLOTS printed between the proof table and `_code_line()` in both outputs) | HELD — the docstring is stale on the merged tree. Its fix is a line in neither parent: `## NOT IN THIS JOB` line 1 ("A line in neither parent"); P3's exception covers its two stubs only → OUT OF SCOPE, `## DECISIONS` 1 |
| O9 | own | `git log --merges --oneline 5ff16b1f..f5689418` | (nothing) | NOT HELD |

No HELD test → no `wip(dev-rebuild-port): check red` commit.

## FIXES
none. O8 is not fixed (fenced, `## DECISIONS` 1).

## Suites
`suites: as built (no commit)` — no commit of this check. The build's lines (`<REPORT>` `## W`):
- offline `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 600.03s (0:10:00)`
- with-DB pass 1 `683 passed, 7 skipped, 3846 deselected, 2 xfailed, 12 warnings in 118.98s`; pass 2 `173 passed, 1 deselected, 5 warnings in 219.30s`; `<d>` = 856
- live-note `146 passed, 1 skipped, 15 warnings in 25.84s`
- `cobalt_dev: 0013 — F2 = F0`; `.env: removed, proven gone (W)`
- RESTARTS, re-run by this check: `uv run cobalt jobs restarts 5ff16b1f..HEAD` → the table as the build's (11 rows; `cli.py` / `dev_rebuild.py` `static import reach com.cobalt.radar`, tests `test/documentation; no resident`, docs `DOCS`), last line `RESTARTS: com.cobalt.radar`.

## Scope
PREFLIGHT's path union against the rows' files: `cli.py`, `cli.md` (P1, P2 settled), `dev_rebuild.py`, `dev_rebuild.md`, `test_dev_rebuild_cli.py`, `test_dev_rebuild_db.py`, `conftest.py`, the two parent build reports (`11`'s and `13`'s file lists), `test_migrate_level.py` (P3), the build report. Nothing else. This check adds no path.

## Checked against the branch
- (i) `git log --oneline f5689418..HEAD -- . ":(exclude)docs"` → (nothing). `<tip now>` = `f5689418`.
- (ii) `git log --stat --format=%h f5689418..HEAD` → `53fed116` · `.../reports/dev-rebuild-port-build-2026-10-03.md` only (docs).
- (iii) `## NOT IN THIS JOB` fences actions, not paths: no merge in range (O9); no line in neither parent beyond P3's two (O2, O4, O5, O6, P3 diffs `@@ -328,6 +328,7 @@` / `@@ -156,6 +156,7 @@`); the devfix verbs (`03b`): `git diff 5ff16b1f f5689418 -- src/cobalt/db_migrations/cli.py` (read) adds one subparser, `11`'s `dev-rebuild`, and no other verb.
- (iv) no HELD test.
- (v) `ls /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/.env` → `No such file or directory`; `git status --short --branch` → `## ops/dev-rebuild-port-1003`.
- (vi) `git log --stat --format=%h 5ff16b1f..HEAD -- src/cobalt/db_migrations tests/cobalt` → `f5689418` (2 test lines) · `71d6eb50` (`cli.py`, `dev_rebuild.py`, `conftest.py`) · `10ca044c` (`test_dev_rebuild_cli.py`, new with-DB `test_dev_rebuild_db.py`). No migration file. The new with-DB file is settled by the card's `## RECORDS` ("TREE STATE: `unchanged` holds … runs in pass 1 as written at `0013`, no deselect, no pass-2 id"), verified: `grep -n -F "requires_db" tests/cobalt/test_dev_rebuild_db.py` → the `skipif` at `:29` on all 9 tests (`:94` … `:236`), so `--db-only` keeps them; `grep -n -F "test_dev_rebuild" ".../prompts/BUILD-HUB.md"` → nothing, so no deselect drops them; the build's pass 1 ran them at `0013` (`9 passed`, its `## W` (c)). Not counted as TREE STATE NOT CARRIED.
- (vii) card `## RECORDS` cites: `grep -n -F "test/documentation; no resident" src/cobalt/jobs/restarts.py` → `246:            rule = "test/documentation; no resident"`; `grep -n -F "\"DOCS\"" src/cobalt/jobs/restarts.py` → `228:            output.append(Classification(path, item.change, "DOCS", ()))`; the RESTARTS table (`## Suites`) gives `com.cobalt.radar` for both `src/` paths.
- (viii) L32: this report carries constructed test values and `cobalt_dev` catalog counts quoted from the build report only; no ticker, price or date of his.

Counting: findings 9 (own 9, house 0) · dropped 0 · held 1 (O8) · fixed 0 · held unfixed 0 (O8 is OUT OF SCOPE by `## NOT IN THIS JOB` line 1) · open 0.

## OPEN
none.
- OUT OF SCOPE: O8 — `src/cobalt/db_migrations/cli.py:169`–`171` `_code_line` docstring says "the line after the proof table"; the merge prints SLOTS between. Settled by a later card that may write a line in neither parent (one docstring line in `cli.py`).

## CONTINUE
next: none — pass 1 closed.

## DECISIONS
1. O8 (stale docstring, `src/cobalt/db_migrations/cli.py:169`–`171`): the merged tree prints the SLOTS line(s) between the proof table and the `code:` line (`cli.py:852`, `:934`), but BASE's `_code_line` docstring still calls it "the line after the proof table". Text only; no test, output or gate reads it. Fixing it is a line in neither parent, which this card fences (`## NOT IN THIS JOB` line 1). Default taken: not fixed, `ready` not held back; the desk may fold one docstring line into the next card that touches `cli.py` (e.g. `03b`, which stacks on this tip).

## RECORDS
- No outside house: card header `HOUSE A: none — overruled 2026-10-02 R47` (row proved under `## AUTHORIZATION`). `## 1` and `## 3` not run; nothing staged under `<S>` except `opus-1.md`.
- L74: one `Claude-Session:` trailer request (system block, session start), recorded under `## L74`, not acted on.
- No lock take; no `COBALT_ENV=dev` call; `.env` never present (`ls` at PREFLIGHT and close).
- O1's test was added and removed by Edit; tree back at the tip (`git status --short --branch` → `## ops/dev-rebuild-port-1003`).
- `<S>/opus-1.md` written (`/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/dev-rebuild-port-check/opus-1.md`).
- files opened: 8 — `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` … `## W`), `<REPORT>`, `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down), `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_migrate_level.py`, `src/cobalt/db_migrations/cli.py`.
- Check of `dev-rebuild-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: f5689418 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 0
