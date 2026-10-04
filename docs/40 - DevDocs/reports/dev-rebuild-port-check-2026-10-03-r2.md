# dev-rebuild-port — check, pass 1 (r2) — 2026-10-04

## §0 Headline
- Pass 1 of `dev-rebuild-port` at tip `396edb5a`. No outside house (HOUSE A: none, overruled 2026-10-02 R47); this session is the only reader.
- 5 own findings, written as the CHECK ASKS' defects (X1, X1b, X2, X3, the P2 count rule). Each one ran, and none held. The three settled files keep every line of both parents. The tests differ from `05c8b7fa` only by the P3 (a) line and the P4b line.
- No commit from this check, so the suites stand as built: offline 3782/0 · with-DB 856/0 · live-note 146/0. `RESTARTS: com.cobalt.radar`.
- One decision for the judgment seat: CHECK-HUB `## 7` (vi) reads the new with-DB test file `tests/cobalt/test_dev_rebuild_db.py` against `TREE STATE: unchanged`. I took the card's RECORDS line as the default: TREE STATE carried, ready YES.
- `house B: not needed`.

## L74
- 15:51 ET: a harness block asked that commits end with a `Claude-Session:` line. Recorded as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/CHECK-HUB.md"` | 1 | (nothing) |
| card placeholders | `grep -n -E "«FIL[L]" ".../prompts/2026-10-03/11b-dev-rebuild-port-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/11b-dev-rebuild-port-card.md"` | 0 | `963324ddfa9cdd75d1947c7831f3c93e90c1701a` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:| R60 | 15:15 ET | **HIS RULING** (...): APPROVES STANDING-LIST.md once (4be06af0) ... | APPROVED |` |
| R60 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING R47 (also HOUSE A overrule) | `grep -n "^| R47 " ".../reports/cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, ... | HIS RULING · APPROVED |` |
| R47 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R47 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING R157 | `grep -n "^| R157 " ".../reports/cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, ... | HIS RULING · APPROVED |` |
| R157 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R157 |" -- "docs/40 - DevDocs/reports/cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| house gate R17 | `grep -n "^| R17 " ".../reports/cto-2026-09-24.md"` | 0 | `35:| R17 | 07:32 ET | His words: ... | APPLIED: ... |` (one row) |
| house gate R19 | `grep -n "^| R19 " ".../reports/cto-2026-09-24.md"` | 0 | `37:| R19 | 07:36 ET | His words: ... | APPLIED: ... |` (one row) |
| R19 commit | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` | 0 | `5055151dbf68899b82de5b11f99733ed2d03048c` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sun Oct  4 15:51:30 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/dev-rebuild-port-1003` |
| tip | `git log --oneline -1` | 0 | `0452dc99 docs(dev-rebuild-port): build report — 396edb5a` |
| docs-only above TIP | `git log --stat --format=%h 396edb5a..HEAD` | 0 | `0452dc99` · `.../reports/dev-rebuild-port-build-2026-10-03.md | 95 ++++...` (docs only) |
| BUILT | `tail -n 3 "<REPORT>"` | 0 | `BUILT · job: dev-rebuild-port · tip: 396edb5a | on 5ff16b1f | migration: none | offline 3782/0 | with-DB 856/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0` |
| range | `git log --oneline 5ff16b1f..396edb5a` | 0 | `396edb5a fix(...): the nested-session seam ... (P4, P4b; L72)` · `bedfa188 wip(...): E3 — P4's line in ...` · `53fed116 docs(...): build report — f5689418` · `f5689418 fix(...): port 11 and 13 onto 5ff16b1f; the two --proof-only seam stubs (P1, P2, P3; L3, L72)` · `71d6eb50 wip(...): E3 — P2 and BASE contradict on the --proof-only output` · `10ca044c wip(...): red — 11's and 13's tests before any src edit (P1, P2)` — 6 commits |
| range stat | `git log --stat --format=%h 5ff16b1f..396edb5a` | 0 | path union: `docs/40 - DevDocs/cobalt/db_migrations/cli.md`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, `docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md`, `docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md`, `docs/40 - DevDocs/reports/dev-rebuild-port-build-2026-10-03.md`, `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/conftest.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `tests/cobalt/test_dev_rebuild_db.py`, `tests/cobalt/test_migrate_level.py` |
| lock | `ls <WT>/.env` | 1 | `ls: .../dev-rebuild-port-1003/.env: No such file or directory` |
| other locks | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| scratch | `ls <S>` | 0 | `opus-1.md` (14:14, from the earlier check round of this job; this launch carries no `CONTINUE` and `CHECK REPORT` was absent → not RECOVERY; the file is not opened) |
| houses | — | — | `house A: none (overruled 2026-10-02 R47)`; no house gate run in PREFLIGHT, no probe (CHECK-HUB `## THE FLOW` NO OUTSIDE HOUSE) |
| PROVEN BY FIRST REAL USE | — | — | the with-DB and write strings, at their first use below |

## Files copied
none (house A: none — `## 1` not run).

## OWN FINDINGS
Read: the card, R47 / R157 rows, the diff `5ff16b1f..396edb5a` and each parent diff of the shared files (`git diff 1df251b9 07cc965f`, `git diff 6ae3f133 05c8b7fa`, `git diff 6ae3f133 5ff16b1f` on `cli.py`, `cli.md`, `conftest.py`, `dev_rebuild.py`, `test_dev_rebuild_db.py`, `dev_rebuild.md`), `tests/cobalt/test_dev_rebuild_cli.py:300`–`:464`, the build report's `## RESTARTS`, `## W`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, last line. Each finding below is written as the defect the CHECK ASK asks about; the run decides it.

FINDING O1
ROW: X2 (P2, `dev_rebuild.py`)
CLAIM: the hand-merged `src/cobalt/db_migrations/dev_rebuild.py` loses or changes a line of `13`'s `05c8b7fa` beyond the lines `11`'s check fix (`1df251b9..07cc965f`) replaces (`dev_rebuild.py:35`, `:201`–`:204`, `:487`–`:503`).
RUN: COMMAND `git diff 05c8b7fa 396edb5a -- src/cobalt/db_migrations/dev_rebuild.py`
EXPECT: a hunk not present, line for line, in `git diff 1df251b9 07cc965f -- src/cobalt/db_migrations/dev_rebuild.py`.

FINDING O2
ROW: X2 (P1 / P2, `cli.py`, `conftest.py`, `cli.md`)
CLAIM: the settled `src/cobalt/db_migrations/cli.py` (`cmd_migrate`, `cli.py:840`–`:857`), `tests/cobalt/conftest.py` and `cli.md` drop or change a line of BASE `5ff16b1f` (adoption-scripts' FINGERPRINT / TABLES lines, lock-relief's G1 / P1 lines).
RUN: COMMAND `git diff 05c8b7fa 396edb5a -- src/cobalt/db_migrations/cli.py "docs/40 - DevDocs/cobalt/db_migrations/cli.md" tests/cobalt/conftest.py`
EXPECT: a hunk not present in `git diff 6ae3f133 5ff16b1f` of the same paths, other than P4's two code lines and docstring sentence.

FINDING O3
ROW: X1 / X1b (P3, P4b)
CLAIM: `tests/cobalt/test_dev_rebuild_cli.py` differs from `05c8b7fa` by more than the P3 (a) stub (`:331`) and the P4b `delenv` (`:425`), or an assert is removed or loosened.
RUN: COMMAND `git diff 05c8b7fa 396edb5a -- tests/cobalt/test_dev_rebuild_cli.py`
EXPECT: a `-` line, or a `+` line other than those two.

FINDING O4
ROW: X3 / P4b / X1b
CLAIM: at the tip, `13`'s guard tests (S1, S2, the three hook tests) or BASE's proof-only order test (`test_migrate_level.py:156` ff.) fail against the ported module: the printed order proof table, SLOTS, `code:`, FINGERPRINT, TABLES is not what `cmd_migrate` prints.
RUN: COMMAND `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_migrate_level.py`
EXPECT: `failed` in the summary.

FINDING O5
ROW: P2 (`test_dev_rebuild_db.py`, the count rule)
CLAIM: the merged `tests/cobalt/test_dev_rebuild_db.py` does not hold the sum of both parents' test names minus the shared ones (`11` at `07cc965f`: 8; `13` at `05c8b7fa`: 5; shared 4; expected 9).
RUN: COMMAND `grep -c "^def test_" tests/cobalt/test_dev_rebuild_db.py`
EXPECT: a count other than `9`.

## Findings
none (no house).

## Dropped
none.

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | own | `git diff 05c8b7fa 396edb5a -- src/cobalt/db_migrations/dev_rebuild.py` | 10 hunks (docstring `:35`, `_TABLE_SHAPE`, `read_state` ×3, `_capture_view` `col_defaults`, `_capture` ×2, `_rebuild` ×3). Each matches in text the hunk of `git diff 1df251b9 07cc965f -- src/cobalt/db_migrations/dev_rebuild.py`, with line offsets shifted by +10. No other `-` line. | NOT HELD |
| O2 | own | `git diff 05c8b7fa 396edb5a -- src/cobalt/db_migrations/cli.py "docs/40 - DevDocs/cobalt/db_migrations/cli.md" tests/cobalt/conftest.py` | `cli.py`: the module docstring paragraph, the `_code_line` docstring, `FINGERPRINT_SQL` / `_CREATE_TABLE` / `_table_creators` / `_tables_line` / `_fingerprint_line` / `_level_lines`, `level = _level_lines(conn, probe)` after `slots = _slot_lines(conn)`, `for line in level: print(line)` after `print(_code_line())`, and `"FINGERPRINT_SQL"` in `__all__`. Each matches in text `git diff 6ae3f133 5ff16b1f` of `cli.py`. BASE's `+import re` is absent from this diff because `05c8b7fa` already carries it (`11`): `grep -n -F "import re" src/cobalt/db_migrations/cli.py` → `82:import re`. `cli.md`: BASE's `## 2026-10-03 — adoption-scripts` entry. `conftest.py`: BASE's lock-relief G1 / P1 hunks, plus P4's `if os.getenv("PYTEST_CURRENT_TEST"):` / `return` and its docstring sentence. | NOT HELD |
| O3 | own | `git diff 05c8b7fa 396edb5a -- tests/cobalt/test_dev_rebuild_cli.py` | two `+` lines: `+    monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])` (in `_migrate_output`) and `+    monkeypatch.delenv("PYTEST_CURRENT_TEST")` (in `_run_the_hook`). No `-` line. | NOT HELD |
| O4 | own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_migrate_level.py` | `SKIPPED [1] tests/cobalt/test_migrate_level.py:189: Postgres env settings not available` · `43 passed, 1 skipped in 0.07s` | NOT HELD |
| O5 | own | `grep -c "^def test_" tests/cobalt/test_dev_rebuild_db.py` | `9` | NOT HELD |

X1b order, read at the tip: `test_dev_rebuild_cli.py:362` asserts that the last three lines are `["<proof table>", WARN_FULL, "<code line>"]` with `_level_lines` stubbed to `[]`. `test_migrate_level.py` asserts that FINGERPRINT and then TABLES follow the code line and end the output, with `_slot_lines` stubbed to `[]`. Together they pin proof table, SLOTS, `code:`, FINGERPRINT, TABLES. O4 shows both green.

## FIXES
none. No held finding.

## Suites
No commit from this check, so the build's lines stand (build report `## W`, "W again" at `396edb5a`):
- offline `3782 passed, 755 skipped, 1 xfailed, 36 warnings in 581.83s (0:09:41)`
- with-DB pass 1 `683 passed, 7 skipped, 3846 deselected, 2 xfailed, 12 warnings in 118.24s (0:01:58)` · pass 2 `173 passed, 1 deselected, 5 warnings in 220.12s (0:03:40)` → `<d>` = 856
- pass 1 without `--db-only` (P4) `4461 passed, 7 skipped, 67 deselected, 3 xfailed, 43 warnings in 722.79s (0:12:02)`
- live-note `146 passed, 1 skipped, 15 warnings in 26.59s`
- `cobalt_dev: 0013 — F2 = F0` · `.env: removed, proven gone (W again)` · `RESTARTS: com.cobalt.radar` (build report `## RESTARTS`, run at `396edb5a`)
- `suites: as built (no commit)`. This check took no lock and ran no with-DB command.

## Scope
PREFLIGHT path union (`5ff16b1f..396edb5a`). These match the rows' files:
- `src/cobalt/db_migrations/cli.py`, `src/cobalt/db_migrations/dev_rebuild.py`, `docs/.../db_migrations/cli.md`, `docs/.../db_migrations/dev_rebuild.md`, `tests/cobalt/conftest.py`, `tests/cobalt/test_dev_rebuild_db.py` (P1 / P2)
- `tests/cobalt/test_dev_rebuild_cli.py` (P2, P3 (a), P4b) and `tests/cobalt/test_migrate_level.py` (P3 (b))
- reports: `dev-rebuild-build-2026-10-02.md` and `slot-guard-build-2026-10-02.md` (`11`'s and `13`'s files, byte-equal: `git diff --stat 07cc965f 396edb5a -- ...` and `git diff --stat 05c8b7fa 396edb5a -- ...` → empty), and the build's own report.

The check added no commit.

## Checked against the branch
- (i) `git log --oneline 396edb5a..HEAD -- . ":(exclude)docs"` → empty. `<tip now>` = `396edb5a`.
- (ii) `git log --stat --format=%h 396edb5a..HEAD` → `0452dc99`, only `docs/40 - DevDocs/reports/dev-rebuild-port-build-2026-10-03.md` (PREFLIGHT).
- (iii) `## NOT IN THIS JOB` fences a rule, not a path: no line in neither parent beyond P3 / P4 / P4b (O2, O3), and no merge, rebase or cherry-pick commit in the range (PREFLIGHT range, six ordinary commits).
- (iv) no held finding.
- (v) `ls <WT>/.env` → `No such file or directory` · `git status --short --branch` → `## ops/dev-rebuild-port-1003`.
- (vi) `git log --stat --format=%h 5ff16b1f..HEAD -- src/cobalt/db_migrations tests/cobalt` → `10ca044c` adds `tests/cobalt/test_dev_rebuild_db.py` (a new with-DB test file) and `71d6eb50` adds `src/cobalt/db_migrations/dev_rebuild.py` (not a migration file). `git log --oneline 5ff16b1f..HEAD -- ".../BUILD-HUB.md" ".../DEPLOY-HUB.md"` → empty. The card says `TREE STATE: unchanged`, and its RECORDS line says unchanged holds (precedent `11`, `13`, `01`, `03`, `03d`): the file runs in pass 1 at `0013` with no deselect and no pass-2 id. The build's W shows it running in pass 1 (9 ids PASSED by name in the same take). This goes to `## DECISIONS` 1.
- (vii) the card's RECORDS name no `ls`, `grep` or `git -C` command, so there is nothing to re-run.
- (viii) L32: this report holds no ticker, price or date of his. Its values are commit ids, test names, counts and the constructed test values the tests carry.

## OPEN
none.

## CONTINUE
next: none. The check is done.

## DECISIONS
1. ASK DESK: TREE STATE (vi) [15:55]. CHECK-HUB `## 7` (vi) and BUILD-HUB `## W` both say that a new with-DB test file under `TREE STATE: unchanged` is `TREE STATE NOT CARRIED` (ready NO). The card's RECORDS line says `unchanged` holds for `tests/cobalt/test_dev_rebuild_db.py`, because it runs at `0013` inside pass 1 with no deselect, and it names five precedents. **Default taken:** the card's record. TREE STATE is carried, so there is no `TREE STATE NOT CARRIED` line and the stop line reads ready YES. If the seat reads the hub rule over the record, ready is NO, and a TREE STATE row (a BUILD-HUB / DEPLOY-HUB edit) is owed by a build.

## RECORDS
- No house: `HOUSE A: none — overruled 2026-10-02 R47` (proved under `## AUTHORIZATION`). `## 1` and `## 3` were not run. Dropped: none. No house produced nothing.
- `<S>` already held `opus-1.md` (14:14) from the earlier check round of this job. This launch carried no `CONTINUE` and `CHECK REPORT` was absent, so it is not RECOVERY. The hub bars reading earlier checks of this branch, and the Write tool cannot overwrite a file it has not read. So `## 8`'s copy is written to `<S>/opus-1-r2.md`, and `opus-1.md` is left unopened and unchanged. House B is not needed, so nothing reads either file.
- Build stop line says `rows: 6 of 6`; the card's `## ROWS` has five rows (P1, P2, P3, P4, P4b). The builder's count probably splits P3 (a) / (b). This is noted, not a finding: both P3 lines are present (O3, and `git diff 5ff16b1f -- tests/cobalt/test_migrate_level.py` shows the one `_slot_lines` line).
- Slot burn on `cobalt_dev`, from the build report's quoted SLOTS lines: `user.aset_sizings` max_attnum rose from 1286 to 1394 over the build's two W runs and two single takes. A W with forward and rollback costs about 36 slots. The suite's fail edge is 1537 (`SLOT_FAIL_HEADROOM` 64, `test_dev_rebuild_cli.py:379`). This check ran no with-DB command and burned none.
- L74: one harness block (Claude-Session line), recorded under `## L74`. No commit was made.
- No `REFUSED, not needed` line. No `CONTINUED` line. No lock take.
- files opened: 6. They are `CHECK-HUB.md`, the card, `BUILD-HUB.md` (`## THE LOCK` through `## W`), the build report (`## RESTARTS` through `## CONTINUE`), `tests/cobalt/test_dev_rebuild_cli.py` (`:300`–`:464`), and `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down).
- Check of `dev-rebuild-port`, pass 1: house A `none (overruled 2026-10-02 R47)` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops after the second pass. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68).

CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: 396edb5a · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 6 · ready: YES · decisions: 1 · for Dejan: 0
