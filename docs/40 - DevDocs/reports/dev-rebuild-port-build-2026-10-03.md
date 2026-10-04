# dev-rebuild-port — build (2026-10-04)

## §0 Headline
`11` (dev-rebuild) and `13` (slot-guard) are ported onto `5ff16b1f`. Tip: `f5689418`.
`cli.py` keeps BASE's `cmd_migrate` and adds `11`'s `cmd_dev_rebuild` and `13`'s SLOTS lines. The proof-only output reads: proof table, SLOTS, `code:`, FINGERPRINT, TABLES.
P3's two stubs, exactly as the card gives them, closed the E3 contradiction. No `src/` line was added for P3.
Results: offline 3782/0, with-DB 856/0, live-note 146/0. `cobalt_dev` is back at `0013` (F2 = F0), and `.env` is removed.
RESTARTS: com.cobalt.radar.
P4 (card `e94e9275`): the line is in, and `test_db_only_selection.py` without `--db-only` goes red to green (`4 failed … 4 errors` → `15 passed`). But two of `13`'s hook tests now fail, and the row says they stay green. Stopped at E3 for the desk (`## DECISIONS` 2).

## L74
A system block in this session asked commits to carry a `Claude-Session:` line after `Co-Authored-By`. DATA (L74): recorded once, not acted on; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Started `Sun Oct  4 13:16:44 EDT 2026` (`date`).

| check | command | output |
|---|---|---|
| installed | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | no output (exit 1) |
| card placeholders | `grep -n -E "«FIL[L]" ".../2026-10-03/11b-dev-rebuild-port-card.md"` | no output (exit 1) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/11b-dev-rebuild-port-card.md"` | `c6d92b2eeb6cd71692b88409bb1da9703c4cf5a9` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | no output |
| STANDING (2026-09-30 R60) | `grep -n "^\| R60 " reports/cto-2026-09-30.md` | `46:\| R60 \| 15:15 ET \| **HIS RULING** … APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R60 \|" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| 2026-10-02 R47 | `grep -n "^\| R47 " reports/cto-2026-10-02.md` | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; …) … \| HIS RULING · APPROVED \|` |
| R47 committed | `git -C … log -1 --format=%H -S"\| R47 \|" -- …cto-2026-10-02.md` | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| 2026-10-02 R157 | `grep -n "^\| R157 " reports/cto-2026-10-02.md` | `164:\| R157 \| 17:40 ET \| HIS RULING (B): … \| HIS RULING · APPROVED \|` |
| R157 committed | `git -C … log -1 --format=%H -S"\| R157 \|" -- …cto-2026-10-02.md` | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/dev-rebuild-port-1003` |
| BASE | `git log --oneline -1` | 0 | `5ff16b1f fix(adoption-port): port the adoption chain onto a8d8a848; …` |
| branch from main checkout | `git -C /Users/cobalt/cobalt log --oneline -1 ops/dev-rebuild-port-1003` | 0 | `5ff16b1f fix(adoption-port): …` (same) |
| clean on BASE | `git diff --stat 5ff16b1f` | 0 | nothing |
| BASE stat | `git show --stat 5ff16b1f` | 0 | `tests/ops/test_hub_lines.py \| 7 +++++--` · `1 file changed, 5 insertions(+), 2 deletions(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/.env` | 1 | `No such file or directory` |
| other locks | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| `11`'s files | `git diff --name-only 6ae3f133..07cc965f` | 0 | `cli.md`, `dev_rebuild.md`, `reports/dev-rebuild-build-2026-10-02.md`, `src/cobalt/db_migrations/cli.py`, `dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `test_dev_rebuild_db.py` |
| `13`'s files | `git diff --name-only 1df251b9..05c8b7fa` | 0 | `cli.md`, `dev_rebuild.md`, `reports/slot-guard-build-2026-10-02.md`, `cli.py`, `dev_rebuild.py`, `tests/cobalt/conftest.py`, `test_dev_rebuild_cli.py`, `test_dev_rebuild_db.py` |
| BASE is `03d`'s tip | READ `prompts/2026-10-03/36-11b-card-preflight-r2.md` line 8 | — | "BASE `5ff16b1f` is card `03d`'s built tip on branch `ops/adoption-port-1003`" → P1 keeps BASE's TABLES / FINGERPRINT lines |
| symbol | `grep -n "def cmd_migrate" src/cobalt/db_migrations/cli.py` | 0 | `684:def cmd_migrate(args: argparse.Namespace) -> None:` |
| callers | `grep -rn -F "cmd_migrate(" src` | 0 | `src/cobalt/db_migrations/cli.py:684:def cmd_migrate(…)` (dispatched through argparse `set_defaults`) |
| symbol | `grep -n -F "FINGERPRINT" src/cobalt/db_migrations/cli.py` | 0 | `64`, `375`, `378:FINGERPRINT_SQL = (`, `449`, `462`, `463:    return f"FINGERPRINT cols {cols} · rels {rels} · views_md5 {views_md5}"`, `958:    "FINGERPRINT_SQL",` |
| symbol | `grep -n -F "TABLES " src/cobalt/db_migrations/cli.py` | 0 | `66`, `413`, `414`, `422`, `437:        return "TABLES none"`, `439:        return f"TABLES {some[-1]}"`, `443` |
| symbol absent at BASE | `grep -n -F "cmd_dev_rebuild" src/cobalt/db_migrations/cli.py` | 1 | nothing |
| BASE `01` guard | `grep -n -F "_guarded_reach" tests/cobalt/conftest.py` | 0 | `132:def _guarded_reach(item, tripped: list) -> None:`, `256`, `286 … # lock-relief G1, check X1`, `312 … # lock-relief G1` |
| `13` hook absent at BASE | `grep -n -F "pytest_sessionstart" tests/cobalt/conftest.py` | 1 | nothing |
| new files absent | `ls src/cobalt/db_migrations/dev_rebuild.py tests/cobalt/test_dev_rebuild_db.py tests/cobalt/test_dev_rebuild_cli.py ".../db_migrations/dev_rebuild.md"` | 1 | four `No such file or directory` |
| sizes | `wc -l cli.py cli.md conftest.py` | 0 | `964 src/cobalt/db_migrations/cli.py` · `375 docs/…/db_migrations/cli.md` · `393 tests/cobalt/conftest.py` |
| READ tail | `tail -n 3 reports/dev-rebuild-check-2026-10-02.md` | 0 | `CHECK DONE · job: dev-rebuild · pass: 1 · tip: 68dddee3 · … · ready: YES · decisions: 0 · for Dejan: 0` |
| READ tail | `tail -n 3 reports/slot-guard-check-2026-10-02.md` | 0 | `CHECK DONE · job: slot-guard · pass: 1 · tip: 05c8b7fa · … · ready: YES · decisions: 0 · for Dejan: 0` |
| RESTARTS empty | `uv run cobalt jobs restarts 5ff16b1f..HEAD` | 0 | `path	change	rule	restart` · `RESTARTS: none` |

Card records, copied and re-read:
- RESTARTS homes: `11`'s build report `## RESTARTS` (`grep -n -F "static import reach" …/dev-rebuild-1002/…/dev-rebuild-build-2026-10-02.md`) → `132:src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar` · `133:src/cobalt/db_migrations/dev_rebuild.py	A	static import reach	com.cobalt.radar`. `grep -n -F "test/documentation; no resident" src/cobalt/jobs/restarts.py` → `246:            rule = "test/documentation; no resident"`. `grep -n -F "DOCS" src/cobalt/jobs/restarts.py` → `228:            output.append(Classification(path, item.change, "DOCS", ()))`. Hold.
- TREE STATE `unchanged`: `test_dev_rebuild_db.py` runs in pass 1 at `0013`, no deselect, no pass-2 id. Proven at W (c).
- BASE: `5ff16b1f` = `03d`'s built tip (r2 preflight line 8; its check 1: `merge-base --is-ancestor 5ff16b1f ops/adoption-port-1003` exit 0).
- Preflight: `reports/11b-card-preflight-2026-10-03-r2.md` last line `PREFLIGHT DONE · card: 11b · checks: 9 · fails: 0 · ready: YES`; it counts the merged test file as `8 + 5 − 4 shared = 9`.
- Judge 10-03 21:39 ET: replaces `13b`; `11` restarts `com.cobalt.radar`. Not re-readable by a listed command beyond the report quotes above.

Proven by first real use: as the hub's table (lock scripts, `<FP>`, `--proof-only`, `COBALT_ENV=dev uv run pytest`, migrate, rollback, `git add` / `git commit`, `uv run pytest`). `uv run cobalt jobs restarts` proven above.

`<FP>`, typed exactly: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
On `5ff16b1f`, no file written while the offline run was in flight.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `3751 passed, 746 skipped, 1 xfailed, 36 warnings in 601.11s (0:10:01)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.51s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Written, no `src/` edit:
- `tests/cobalt/test_dev_rebuild_db.py`: Write tool with `07cc965f`'s content (read from `/Users/cobalt/cobalt-wt/dev-rebuild-1002`, whose tree `git -C … diff --stat 07cc965f` shows equal) → `git diff --no-index --stat <that file> tests/cobalt/test_dev_rebuild_db.py` → nothing; then by Edit `05c8b7fa`'s one added block (`SL` and `test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings`) appended after `11`'s `test_check_o4`.
- `tests/cobalt/test_dev_rebuild_cli.py`: Write with `07cc965f`'s content → `--no-index --stat` against `dev-rebuild-1002`'s → nothing; then by Edit `05c8b7fa`'s added S1 / S2 block → `git diff --no-index --stat /Users/cobalt/cobalt-wt/slot-guard-1002/tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_cli.py` → nothing (`git -C …/slot-guard-1002 diff --stat 05c8b7fa -- tests/cobalt/… src "docs/40 - DevDocs/cobalt"` → nothing, so that tree is `05c8b7fa`'s for these paths).

Offline:
- `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_db.py` → `E   ModuleNotFoundError: No module named 'cobalt.db_migrations.dev_rebuild'` · `1 error in 0.13s` (collection of the DB file).
- `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py` → `31 failed in 0.07s`. The 12 D2 tests (`11`): `argparse.ArgumentError: argument command: invalid choice: 'dev-rebuild' (choose from migrate, query)` (`:39`) — `11`'s named red. The 16 S1 / S2 tests and the 3 hook tests (`13`): `ModuleNotFoundError: No module named 'cobalt.db_migrations.dev_rebuild'` (`:270`, `:278`, `:295` ×2, `:303`, `:318`, `:357` ×4, `:381` ×5, `:389`, `:419` ×3). On BASE the module itself is absent, so `13`'s `cannot import name 'slot_report'` reads one step earlier as the module import; the name does not exist either way.

With-DB, lock take 1 (E2), taken 13:31:42, released 13:32:17:
- `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh dev-rebuild-port-1003 90` (background) → `lock taken: dev-rebuild-port-1003`, exit 0. `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  4 13:31 /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/.env`.
- `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables, `drc_*`, `legs`, `prediction_records`, `voice_turns` read `-`; `NOTHING WAS APPLIED`; `code: 5ff16b1f (DIRTY: 3 path(s))`; `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`; `TABLES 0011` → `0013`. NO forward.
- `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` → `E   ModuleNotFoundError: No module named 'cobalt.db_migrations.dev_rebuild'` · `ERROR tests/cobalt/test_dev_rebuild_db.py` · `1 error in 0.09s` — the red of `11`'s D1 / D3 / O1–O4 and of `13`'s S1 with-DB test on BASE.
- `<FP>` again → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>`.
- `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh dev-rebuild-port-1003` → `lock released`; `ls …/dev-rebuild-port-1003/.env` → `No such file or directory`. `.env: removed, proven gone (E2)`.

Commit `10ca044c wip(dev-rebuild-port): red — 11's and 13's tests before any src edit (P1, P2)`.

**P4 (card `e94e9275`) — the nested-session red, on the P3 tip `f5689418`** (conftest unchanged since; HEAD `53fed116` is the report commit). The row writes no new test: its red is the existing `tests/cobalt/test_db_only_selection.py` run without `--db-only`.
- Offline, before the take: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_db_only_selection.py` → `13 passed, 2 skipped, 12 warnings in 1.48s` (skips `:617`, `:643`: `Postgres env settings not available`).
- Lock take 3 (P4, the card's ONE take for red and green), taken 15:13:22 (`date`): `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh dev-rebuild-port-1003 90` (background) → `lock taken: dev-rebuild-port-1003`, exit 0. `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  4 15:13 /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/.env`.
- `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed (`drc_*`, `legs`, `prediction_records`, `voice_turns` read `-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `SLOTS WARN user.aset_sizings max_attnum 1358 of 1600 · dropped 1304 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)`; `code: 53fed116 (DIRTY: 1 path(s))`; `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`; `TABLES 0011` (the `0013` reading of E2 and W). NO forward.
- RED: `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_db_only_selection.py` printed a traceback too long for the tool to show whole (`INTERNALERROR> … conftest.py, line 162, in pytest_sessionstart` → `conn = REAL_CONNECT(env.DEV_DB_NAME, side=db.Side.SYSTEM)` → `conftest.py, line 331, in guarded_psycopg_connect` → `conftest.py, line 78, in require_offline_skip` → `AssertionError: with-DB test without an offline skip mark: tests/cobalt/test_db_only_selection.py::test_with_db_only_a_run_deselects_every_unmarked_item`). The same command, again with `-rfE --tb=line --show-capture=no` → **`4 failed, 11 passed, 12 warnings, 4 errors in 1.60s`**. FAILED and ERROR on each of `test_with_db_only_a_run_deselects_every_unmarked_item`, `test_without_db_only_a_run_keeps_every_item` (`:145: IndexError: list index out of range`), `test_a_reach_a_store_swallowed_still_fails_the_test_at_teardown` (`:185: AssertionError: assert [] == ['passed']`), `test_an_unmarked_open_through_real_connect_is_refused_before_any_connection` (`:203: AssertionError: assert [] == ['failed']`). Each ERROR is `E   Failed: with-DB test without an offline skip mark: <that id>`. This is the card's red: `4 failed … 4 errors`, `conftest.py:78 require_offline_skip`.

## E3 THE ROWS
Every source file was read before its edit: `07cc965f`'s from `/Users/cobalt/cobalt-wt/dev-rebuild-1002` (its tree = `07cc965f`, `git -C … diff --stat 07cc965f` → nothing), `05c8b7fa`'s from `/Users/cobalt/cobalt-wt/slot-guard-1002` (`git -C … diff --stat 05c8b7fa -- tests/cobalt/… src "docs/40 - DevDocs/cobalt"` → nothing) or `git show 05c8b7fa:<path>`. Byte equality is proven by `git diff --no-index --stat <source file> <port file>` → nothing; the committed-blob pairs follow at the wip commit.

**P1 — `11` first.**
- Written whole from `07cc965f`, each `--no-index --stat` → nothing: `src/cobalt/db_migrations/dev_rebuild.py`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md`, `docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md`; the two test files at E2.
- SETTLED `src/cobalt/db_migrations/cli.py` by Edit: BASE's file plus `11`'s hunks (`import sys`, `NoReturn`; `_content_digest` and `_probe` calling it; `_open` and `_connect` calling it; `_checked_lock_timeout` and `cmd_migrate` calling it; `_DEV_REBUILD_NAME`, `_refuse`, `cmd_dev_rebuild`; the `dev-rebuild` subparser; `"cmd_dev_rebuild"` in `__all__`). `11`'s `import re` was already BASE's line. BASE is `03d`'s tip, so BASE's `cmd_migrate` stands with its TABLES / FINGERPRINT lines.
  - `git diff 07cc965f -- src/cobalt/db_migrations/cli.py` → only BASE's lines: the module docstring's `--proof-only ENDS WITH TWO MORE LINES` paragraph, the `_code_line` docstring's three lines, `FINGERPRINT_SQL`, `_CREATE_TABLE`, `_table_creators`, `_tables_line`, `_fingerprint_line`, `_level_lines`, `level = _level_lines(conn, probe)` with its print loop, `"FINGERPRINT_SQL"` in `__all__`.
  - `git diff --stat 5ff16b1f -- src/cobalt/db_migrations/cli.py` → `176 insertions(+), 26 deletions(-)`, against `11`'s own `git diff --stat 6ae3f133 07cc965f -- …cli.py` `177 insertions(+), 26 deletions(-)`. The one line fewer is `import re`, which BASE already carries.
- SETTLED `docs/40 - DevDocs/cobalt/db_migrations/cli.md` by Edit: `11`'s `## 2026-10-02 — dev-rebuild` section at `11`'s place, before `## 2026-09-30 — f15-p1`. `git diff 5ff16b1f -- …cli.md` → only `11`'s section (3 lines); `git diff 07cc965f -- …cli.md` → only BASE's `## 2026-10-03 — adoption-scripts` section.
- Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_db.py tests/cobalt/test_migrate_proof.py tests/cobalt/test_migrate_level.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_tenancy.py tests/cobalt/test_db_query.py tests/cobalt/test_radar_migration.py` → `19 failed, 107 passed, 80 skipped in 1.80s`. The 19 failures are all `13`'s tests, red for `13`'s named reason now that the module exists: `ImportError: cannot import name 'slot_report' from 'cobalt.db_migrations.dev_rebuild'` (`:270` …), `… 'slot_verdict'` (`:381`, `:389`), `AttributeError: … has no attribute 'slot_report'` (`:426`). `11`'s 12 D2 tests and every neighbour pass (`test_tenancy`'s one-caller lint, `test_migrate_level`, `test_migrate_proof` among them).
- MUTATION P1-M1 (undoes the `COBALT_ENV` refusal: `if mode != env.DEV:` → `if False:`): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py -k "not s1 and not s2"` → `1 failed, 11 passed, 19 deselected in 0.04s`; `E   AssertionError: db.connect_migration was called` on `test_refused_with_exit_2_and_no_connection[production-user.aset_sizings]`. Undone.
- MUTATION P1-M2 (undoes the `current_database()` refusal: `if current != env.DEV_DB_NAME:` → `if False:`): same command → `1 failed, 11 passed, 19 deselected in 0.04s`; `E   assert ['SELECT curr...eout = '30s'"] == ['SELECT current_database()']` · `Left contains one more item: "SET LOCAL lock_timeout = '30s'"`. Undone.

**P2 — `13` on top, by Edit onto P1's result.**
- `src/cobalt/db_migrations/dev_rebuild.py`: `13`'s three hunks (`SLOT_LIMIT`, `SLOT_FAIL_HEADROOM`; the slot-read block `_SLOT_REPORT`, `slot_report`, `slot_lines`, `slot_verdict`; five `__all__` names). `git diff --no-index …/slot-guard-1002/…/dev_rebuild.py …` → only `11`'s O1–O5 lines (module docstring tablespace clause, `_TABLE_SHAPE` tablespace reads, the `table` section's access method and TOAST, the `indexes` section's statistics targets, the views' column defaults, `_capture`'s tablespace refusal, `am_q` / `toast_options` / `index_stats`, `USING`, `SET (toast.…)`, the index `SET STATISTICS` loop, the view `SET DEFAULT` loop). `git diff --no-index --stat …/dev-rebuild-1002/…/dev_rebuild.py …` → `68 insertions(+)`, which is `13`'s `git diff --stat 1df251b9 05c8b7fa` count for the file.
- `src/cobalt/db_migrations/cli.py`: `13`'s hunks onto P1's text (`SLOT_WARN_AT`; `_slot_lines`; `slots = _slot_lines(conn)` and its print loop in the proof-only branch and in the forward / rollback branch; `"SLOT_WARN_AT"` in `__all__`). `git diff --no-index …/slot-guard-1002/…/cli.py …` → only BASE's lines (the list above, P1). In the proof-only branch both sides stand in full: `probe`, then `slots = _slot_lines(conn)` (`13`), then `level = _level_lines(conn, probe)` (BASE); printed: the proof table, the SLOTS line(s) (`13`), `code:`, then FINGERPRINT and TABLES (BASE).
- `tests/cobalt/conftest.py`: `13`'s slot-guard block (`_SLOTS_WARN`, `pytest_sessionstart`, `pytest_terminal_summary`) after BASE's lock-relief G1 / P1 block. `git diff 05c8b7fa -- tests/cobalt/conftest.py` → only BASE's lines (the G1 / P1 block, the `dev_db_tx` / `real_connect` guard lines); `git diff --stat 5ff16b1f -- tests/cobalt/conftest.py` → `45 insertions(+)` = `13`'s count.
- `tests/cobalt/test_dev_rebuild_cli.py`: `05c8b7fa`'s, byte-equal (E2). `tests/cobalt/test_dev_rebuild_db.py`: `07cc965f`'s plus `13`'s block at the end. `grep -c "^def test_"` → `9` = 8 (`07cc965f`) + 5 (`05c8b7fa`) − 4 shared by name (`test_d1_rebuild_frees_every_dropped_slot_and_keeps_rows_and_catalog`, `test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept`, `test_d1_dry_run_rolls_back_after_the_compare`, `test_d3_aset_sizings_passes_the_rule_as_a_dry_run_at_0013`).
- `docs/…/cli.md`: `13`'s `## 2026-10-02 — slot-guard` section after `11`'s; `git diff 05c8b7fa -- …cli.md` → only BASE's section. `docs/…/dev_rebuild.md`: `13`'s section after `11`'s check notes; `git diff --no-index …/slot-guard-1002/…/dev_rebuild.md …` → only `11`'s `## 2026-10-02 — dev-rebuild check` section.
- `docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md`: Write from `git show 05c8b7fa:<path>` (saved output); `git diff --no-index --stat <saved output> <file>` → nothing.
- Run: the P1 command above → **`3 failed, 123 passed, 80 skipped in 1.85s`**:
  - `test_dev_rebuild_cli.py::test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table[proof-only]` and `[proof-only-production]` (`13`'s, byte-equal to `05c8b7fa`): `src/cobalt/db_migrations/cli.py:846: level = _level_lines(conn, probe)` → `cli.py:484: present = {t: probe[t]["schema"] is not None for t in CREATED_TABLES}` → `E   KeyError: 'radar_pool'`. The test stubs `_probe_all` to `{}` and does not stub BASE's `_level_lines`. Its asserts also require `lines[-3:] == ["<proof table>", WARN_FULL, "<code line>"]` (`:361`) and proof-only statements `== ["SAVEPOINT", "SELECT", "RELEASE"]` (`:368`), while BASE prints FINGERPRINT and TABLES after `code:` and sends `SET LOCAL search_path` and `FINGERPRINT_SQL` on the same connection.
  - `test_migrate_level.py::test_proof_only_ends_with_the_fingerprint_then_the_tables_line` (BASE's; not in this card's files): `:173: assert "SET LOCAL search_path TO " in conn.events[0]` → `E   AssertionError: assert ('SET LOCAL search_path TO ' in 'SAVEPOINT cobalt_slots')`. It requires `conn.events[1:] == [cli.FINGERPRINT_SQL, "ROLLBACK", "CLOSE"]` (`:174`), and `13`'s slot read now sends its savepoint and SELECT on that connection.
  - No order of the two reads in `cmd_migrate` passes both. Slots after level still leaves `13`'s `KeyError` and `lines[-3:]`, and it leaves BASE's `events[1:]` with the savepoint statements in it. Both tests can pass only if a test file gains a line that is in neither parent, or one side's behaviour is dropped. `## DECISIONS` 1.
- MUTATION P2-M1 (`slot_lines`: `m >= warn_at` → `m > warn_at`): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py` → `3 failed, 28 passed in 0.05s`; the new red is `:299: AssertionError: … 'SLOTS ok · highest user.aset_sizings 1200 of 1600' != 'SLOTS WARN user.aset_sizings max_attnum 1200 of 1600 · …'` (`[1200-…]`), beside the two contradiction reds above. Undone.
- MUTATION P2-M2 (the hook's `if verdict == "fail":` → `if False:` in `conftest.py`): `… tests/cobalt/test_dev_rebuild_cli.py -k "hook"` → `1 failed, 2 passed, 28 deselected in 0.03s`; `:442: AssertionError: the hook did not stop the run`. Undone.
- After the undos: `git diff --no-index --stat …/dev-rebuild-1002/…/dev_rebuild.py src/cobalt/db_migrations/dev_rebuild.py` → `68 insertions(+)`; `git diff 05c8b7fa --stat -- tests/cobalt/conftest.py tests/cobalt/test_dev_rebuild_cli.py` → `conftest.py | 109 +++…--` (`106 insertions(+), 3 deletions(-)`, BASE's lines only), with the test file unchanged.
- The with-DB greens of P1 / P2 are not run yet. They run at W, or at an extra take once the desk answers.

STOPPED at E3, 13:44 ET (`date` → `Sun Oct  4 13:44:13 EDT 2026`). No lock is held: E2's take was released at 13:32:17, and nothing has been applied on `cobalt_dev`. Wip commit `71d6eb50`.

**RESUMED 13:47 (`date` → `Sun Oct  4 13:47:23 EDT 2026`) on `CONTINUE: E3`.** RECOVERY: `git status --short --branch` → `## ops/dev-rebuild-port-1003`; `git log --oneline -3` → `71d6eb50`, `10ca044c`, `5ff16b1f`; `ls -la …/.env` → `No such file or directory`. Fact verified: `git -C /Users/cobalt/cobalt log -2 --format="%h %s" -- "<card>"` → `a7a1630a docs(desk): R194 11b row P3 (judge: proof-only stubs); resume E3`; `diff --stat` → nothing; `«FIL[L]` → nothing (exit 1).

**P3 — the `--proof-only` seam, two stub lines (card row P3).**
- Re-read: `grep -n -F "_probe_all" tests/cobalt/test_dev_rebuild_cli.py` → `330:    monkeypatch.setattr(cli, "_probe_all", lambda c: {})`; `… tests/cobalt/test_migrate_level.py` → `156:    monkeypatch.setattr(cli, "_probe_all", lambda c: {`; precedent `grep -n -F "_level_lines" tests/cobalt/test_migrate_proof.py` → `1541`, `1765`.
- (a) after `:330`: `    monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])`. (b) after the `_probe_all` stub's closing `})` (`:158`): `    monkeypatch.setattr(cli, "_slot_lines", lambda conn: [])`.
- `git diff 05c8b7fa -- tests/cobalt/test_dev_rebuild_cli.py` → one hunk `@@ -328,6 +328,7 @@`, one line added: `+    monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])`. `git diff 5ff16b1f -- tests/cobalt/test_migrate_level.py` → one hunk `@@ -156,6 +156,7 @@`, one line added: `+    monkeypatch.setattr(cli, "_slot_lines", lambda conn: [])`.
- No `src/` line changed. `cli.py:840`–`857` (Read): `probe = _probe_all(conn)`, `slots = _slot_lines(conn)`, `level = _level_lines(conn, probe)`; printed `_print_probe`, the `slots` lines, `_code_line()`, the `level` lines. The order stays proof table, SLOTS, `code:`, FINGERPRINT, TABLES.
- Green: the P1 command → **`126 passed, 80 skipped in 1.84s`** (0 failed; was `3 failed, 123 passed`).
- MUTATION P3-M1 ((a) removed by Edit): `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py` → `2 failed, 29 passed in 0.07s`; `cli.py:484: KeyError: 'radar_pool'` on `test_s1_…[proof-only]` and `[proof-only-production]`. Restored.
- MUTATION P3-M2 ((b) removed by Edit): `… tests/cobalt/test_migrate_level.py` → `1 failed, 11 passed, 1 skipped in 0.04s`; `:173: AssertionError: assert ('SET LOCAL search_path TO ' in 'SAVEPOINT cobalt_slots')`. Restored.
- MUTATION P2-M1 re-run on the fixed tree (`dev_rebuild.py:817` `m >= warn_at` → `m > warn_at`): `… tests/cobalt/test_dev_rebuild_cli.py` → `1 failed, 30 passed in 0.07s`; `:299: AssertionError: … 'SLOTS ok · highest user.aset_sizings 1200 of 1600' != 'SLOTS WARN user.aset_sizings max_attnum 1200 of 1600 · …'` (`test_s1_the_two_ends_of_the_warn_edge[1200-…]`), now the only red. Undone.
- After the undos `git diff --stat` → only the report and the two one-line test additions.
- No module changed in P3, so it adds no DevDocs module line (P1 / P2's `cli.md` and `dev_rebuild.md` lines are `11`'s and `13`'s own).
- Commit `f5689418 fix(dev-rebuild-port): port 11 (dev-rebuild) and 13 (slot-guard) onto 5ff16b1f; the two --proof-only seam stubs (P1, P2, P3; L3, L72)`.

**P4 — the nested-session seam (card row P4), inside lock take 3.**
- Re-read: `tests/cobalt/conftest.py:148`–`156` (Read): `def pytest_sessionstart(session):`, its docstring ending `:154` `untouched."""`, then `:155` `if not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")):`. `import os` is at `:44`.
- Edit, exactly the row's line as the hook's first statement after its docstring: `    if os.getenv("PYTEST_CURRENT_TEST"):` + `        return`. One docstring sentence was added: "A nested session (a pytester run started from a running test, when pytest has set `PYTEST_CURRENT_TEST`) never opens `cobalt_dev`; a top-level session start still reads the slots."
- Green, the card's command in the same take: `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_db_only_selection.py` → **`15 passed, 12 warnings in 1.79s`** (all 15 PASSED in the `-rA` lines). The top-level session still read the slots: `SLOTS WARN user.aset_sizings max_attnum 1358 of 1600 · dropped 1304 · live 54 · …` printed at its summary.
- The row's second check FAILS. `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py -k hook` → **`2 failed, 1 passed, 28 deselected in 0.06s`**:
  - `test_s2_the_hook_stops_the_run_with_exit_3_naming_the_table`: `:443: AssertionError: the hook did not stop the run`
  - `test_s2_the_hook_warns_in_the_summary_and_does_not_stop`: `:455: AssertionError: assert [] == ['SLOTS WARN ...s (dev only)']`
  - `test_s2_the_hook_is_silent_below_the_warn_mark` passes (it asserts no stop and no line, which an early return also gives).
  - The same command after the release, with `.env` gone → the same `2 failed, 1 passed, 28 deselected in 0.03s`, same two lines. It does not depend on `.env`.
- Why, read from the code (`test_dev_rebuild_cli.py:414`–`438`): `_run_the_hook` calls `conftest.pytest_sessionstart(...)` directly from inside a running test. Pytest sets `PYTEST_CURRENT_TEST` for every running test, so P4's new first statement returns before `slot_report` and `slot_verdict` are reached. The row's two checks cannot both hold with only the row's line. Making `13`'s hook tests green needs one more line in neither parent, for example `monkeypatch.delenv("PYTEST_CURRENT_TEST")` in `_run_the_hook` beside its `setenv` lines (`:423`–`:424`). The row's exception covers "this one line only" (`## NOT IN THIS JOB` line 1), so I did not write it. `## DECISIONS` 2.
- Not run: P4's mutation and E3's remaining steps. They wait for the desk's word.
- `<FP>` again, same take → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>`.
- `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh dev-rebuild-port-1003` → `lock released`; `ls …/dev-rebuild-port-1003/.env` → `No such file or directory`; `date` → `Sun Oct  4 15:14:38 EDT 2026`. `.env: removed, proven gone (P4)`.

STOPPED at E3 (row P4), 15:14 ET. No lock is held, and nothing was applied on `cobalt_dev` in this take.

## RESTARTS
`uv run cobalt jobs restarts 5ff16b1f..HEAD` (HEAD `f5689418`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md	A	DOCS	-
docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md	A	DOCS	-
docs/40 - DevDocs/reports/dev-rebuild-port-build-2026-10-03.md	M	DOCS	-
docs/40 - DevDocs/reports/slot-guard-build-2026-10-02.md	A	DOCS	-
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/dev_rebuild.py	A	static import reach	com.cobalt.radar
tests/cobalt/conftest.py	M	test/documentation; no resident	-
tests/cobalt/test_dev_rebuild_cli.py	A	test/documentation; no resident	-
tests/cobalt/test_dev_rebuild_db.py	A	test/documentation; no resident	-
tests/cobalt/test_migrate_level.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row. The classes match the card's RECORDS homes (`11`'s `com.cobalt.radar` lines, `:246` tests, `:228` DOCS).

## W THE THREE SUITES
`<tip>` = `f5689418`.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → **`3782 passed, 755 skipped, 1 xfailed, 36 warnings in 600.03s (0:10:00)`**. 0 failed, 0 errors. `<p>` = 3782. Against E0 (`3751 passed, 746 skipped`), +31 passed is the 31 tests of `tests/cobalt/test_dev_rebuild_cli.py` (`11`'s 12 D2, `13`'s 16 S1 / S2 and 3 hook tests). +9 skipped is `tests/cobalt/test_dev_rebuild_db.py`'s with-DB tests, which skip offline. Added by this build: those two files, plus one line each in `_migrate_output` and `test_proof_only_ends_with_the_fingerprint_then_the_tables_line` (P3).
- (b) Lock take 2 (W): `sh /Users/cobalt/.claude/ops/take-devdb-lock.sh dev-rebuild-port-1003 90` (background) → `lock taken: dev-rebuild-port-1003`, exit 0, at 13:59:19 (`date`). `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `-rw-------  1 cobalt  staff  2186 Oct  4 13:59 /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/.env`.
  - `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`.
  - `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed (`drc_*`, `legs`, `prediction_records`, `voice_turns` read `-`); `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `SLOTS WARN user.aset_sizings max_attnum 1286 of 1600 · dropped 1232 · live 54 · fix: cobalt db dev-rebuild user.aset_sizings (dev only)`; `code: f5689418 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/dev-rebuild-port-1003`; `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`; `TABLES 0011`. This is the same reading E2 took at `0013` (E2: `TABLES 0011`, same FINGERPRINT). The printed order is the ported one: proof table, SLOTS, `code:`, FINGERPRINT, TABLES. The DIRTY path is this report.
- (c) PASS 1, executed whole (this build adds no deselect; TREE STATE unchanged): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py`
  → (background, exit 0) **`683 passed, 7 skipped, 3846 deselected, 2 xfailed, 12 warnings in 118.98s (0:01:58)`**. 0 failed, 0 errors. `<d1>` = 683. The SKIPPED lines, each with its reason:
  - `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev`
  - `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
  - `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
  - `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
  - `tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read`
  - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
  - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
  The slot-guard session hook (`13`, conftest) printed at the end of the run: `SLOTS WARN user.aset_sizings max_attnum 1286 of 1600 · dropped 1232 · live 54 · …` (a warn, not a stop).
  - This build's with-DB ids by name, same take at `0013`: `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` → `9 passed in 0.58s`. PASSED: `test_d1_rebuild_frees_every_dropped_slot_and_keeps_rows_and_catalog`, `test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept`, `test_d1_dry_run_rolls_back_after_the_compare`, `test_d3_aset_sizings_passes_the_rule_as_a_dry_run_at_0013`, `test_check_o1_toast_reloptions_survive_the_rebuild`, `test_check_o2_a_view_column_default_survives_the_rebuild`, `test_check_o3_the_table_access_method_survives_the_rebuild`, `test_check_o4_an_index_column_statistics_target_survives_the_rebuild`, `test_s1_slot_report_on_cobalt_dev_matches_the_slot_read_for_aset_sizings`. These are P1's and P2's with-DB greens (E2 red: `ModuleNotFoundError`).
- (c2) FORWARD: `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `cobalt db migrate — FORWARD on cobalt_dev`; `-- applying` `0001_schemas.sql` … `0011_archive_incidents.sql`, `0013_tunables_slug_nullable.sql`, `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0016_drc.sql`, `0017_voice_turns.sql`, `0018_drc_stated_books.sql`, `0019_drc_events.sql`, `0020_drc_build_kinds.sql`, `0021_legs.sql`, `0022_prediction_records.sql`, in FORWARD order. This build adds no migration. Verdicts: `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records`, `voice_turns` CREATED; every other table OK; `36 table(s) proven; … content UNCHANGED on every table.`; no `CHANGED`. `SLOTS WARN user.aset_sizings max_attnum 1290 of 1600 · dropped 1232 · live 58 · …`; `code: f5689418 (DIRTY: 1 path(s))`.
  **`dev forward: APPLIED 14:02`** (`date` → `Sun Oct  4 14:02:15 EDT 2026`).
  - `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, executed whole (this build adds nothing; TREE STATE unchanged): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`
  → (background, exit 0) **`173 passed, 1 deselected, 5 warnings in 219.30s (0:03:39)`**; `grep -c -F "PASSED"` on its output → `173`; `grep -n -F "SKIPPED"` → nothing. 0 failed, 0 errors. `<d2>` = 173; no id of this build is in pass 2. `<d>` = 683 + 173 = **856**.
- (c3r) NOTHING LEFT BEHIND: `tests/cobalt/test_dev_rebuild_db.py` writes no `aset_sizings` ticker. `grep -n -i -F "ticker"` → nothing; its `INSERT`s (`:85`, `:86`, `:207`) go to the scratch tables `SCRATCH = "zz_dev_rebuild_scratch"` (`:34`) and `CHILD = "zz_dev_rebuild_child"` (`:35`). With no ticker to put in the hub's `IN (…)`, the leftover check is run on those tables. `ls -la …/.env` listed, then `COBALT_ENV=dev uv run cobalt db query --side user "SELECT n.nspname, c.relname FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE starts_with(c.relname, 'zz_dev_rebuild')"` → header only, no rows. (An earlier form with `LIKE 'zz_dev_rebuild%'` was refused by the query tool: `FAILED: ProgrammingError: only '%s', '%b', '%t' are allowed as placeholders, got '%''`. It read nothing.)
- (c4) not applicable: this build adds no migration.
- (f) ROLLBACK: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `-- applying` `0022_prediction_records.rollback.sql`, `0021_legs…`, `0020_drc_build_kinds…`, `0019_drc_events…`, `0018_drc_stated_books…`, `0017_voice_turns…`, `0016_drc…`, `0015_shadow_agreement_stale…`, `0014_radar_handicap.rollback.sql`, newest first. The 8 created tables are DROPPED and every other table OK; `content UNCHANGED on every table.`. `SLOTS WARN user.aset_sizings max_attnum 1322 of 1600 · dropped 1268 · live 54 · …`.
  - `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **`cobalt_dev: 0013 — F2 = F0`**.
  - `sh /Users/cobalt/.claude/ops/release-devdb-lock.sh dev-rebuild-port-1003` → `lock released`; `ls /Users/cobalt/cobalt-wt/dev-rebuild-port-1003/.env` → `No such file or directory`; `date` → `Sun Oct  4 14:07:06 EDT 2026`. `.env: removed, proven gone (W)`.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 25.84s`**. The skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red for its named reason:
- `11`'s 12 D2 tests: E2 `argparse.ArgumentError: argument command: invalid choice: 'dev-rebuild'`; mutations P1-M1 (`E   AssertionError: db.connect_migration was called`) and P1-M2 (`Left contains one more item: "SET LOCAL lock_timeout = '30s'"`).
- `11`'s 8 with-DB tests and `13`'s S1 with-DB test: E2 with-DB `ModuleNotFoundError: No module named 'cobalt.db_migrations.dev_rebuild'`.
- `13`'s 16 S1 / S2 tests: E3 `ImportError: cannot import name 'slot_report'` / `'slot_verdict'`; mutation P2-M1 re-run on the fixed tree, `:299` `'SLOTS ok · …' != 'SLOTS WARN …'`.
- `13`'s 3 hook tests: P2-M2 `:442: AssertionError: the hook did not stop the run`.
- P3 (a): P3-M1 `cli.py:484: KeyError: 'radar_pool'` ×2. P3 (b): P3-M2 `:173: AssertionError: assert ('SET LOCAL search_path TO ' in 'SAVEPOINT cobalt_slots')`.
- No test stayed green under its mutation; none was rewritten.

(2) Every entry path is pinned:
- `cmd_migrate` has one definition (`grep -rn -F "cmd_migrate(" src` → `cli.py:684` only, argparse dispatch). Its four flag shapes (proof-only, forward, rollback, proof-only + allow-prod) are pinned by `test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table[…]`. BASE's proof-only tail is pinned by `test_proof_only_ends_with_the_fingerprint_then_the_tables_line`.
- `cmd_dev_rebuild` (new, absent at BASE per `grep -n -F "cmd_dev_rebuild"` exit 1) is pinned by the 12 D2 tests: env refusal, database refusal, argument shapes.
- `slot_lines` / `slot_verdict` are pinned at both readers, `cli._slot_lines` (S1) and the conftest session hook (3 hook tests), plus the warn edge (`test_s1_the_two_ends_of_the_warn_edge`).
- The with-DB rebuild paths (dry run, real, refused grant) are pinned by the 9 with-DB tests, all PASSED at `0013` in W.

(3) Re-read at the tip `f5689418`:
- `git show f5689418 --stat` → `tests/cobalt/test_dev_rebuild_cli.py | 1 +`, `tests/cobalt/test_migrate_level.py | 1 +`.
- `grep -n -F "_level_lines" tests/cobalt/test_dev_rebuild_cli.py` → `331:` (the line after `:330`). `grep -n -F "_slot_lines" tests/cobalt/test_migrate_level.py` → `159:`.
- `grep -c "^def test_" tests/cobalt/test_dev_rebuild_db.py` → `9`.
- `cli.py:840`–`857` read at the tip.
- `git diff --stat 07cc965f -- src/cobalt/db_migrations/dev_rebuild.py tests/cobalt/test_dev_rebuild_db.py "<11's build report>"` → `dev_rebuild.py | 68 +`, `test_dev_rebuild_db.py | 24 +`: `13`'s lines only, and `11`'s report byte-equal.
- `git diff --stat 05c8b7fa -- dev_rebuild.py test_dev_rebuild_db.py test_dev_rebuild_cli.py "<13's build report>" conftest.py` → `66 +/-` (`11`'s O1–O5), `53 +` (`11`'s tests beyond the shared 4), `cli test | 1 +` (P3 (a)), `conftest.py | 109` (BASE's lines); `13`'s report byte-equal.

## FOR THE CHECK
- Range `5ff16b1f..f5689418`:
  - `10ca044c wip(dev-rebuild-port): red — 11's and 13's tests before any src edit (P1, P2)`
  - `71d6eb50 wip(dev-rebuild-port): E3 — P2 and BASE contradict on the --proof-only output (test_dev_rebuild_cli.py proof-only ids vs test_migrate_level.py)`
  - `f5689418 fix(dev-rebuild-port): port 11 (dev-rebuild) and 13 (slot-guard) onto 5ff16b1f; the two --proof-only seam stubs (P1, P2, P3; L3, L72)`
  - The report commit follows.
- Per row, the reds, mutations and greens: `## E2 RED`, `## E3 THE ROWS` (P1, P2, P3), and `## PRE-STOP SELF-CHECK` (1).
- Hash pairs (X1): `## PRE-STOP SELF-CHECK` (3), the two `git diff --stat <parent>` calls at the tip.
- P3's two lines (X1b): `## E3` P3, each `git diff <parent> --` showing one added line; `cli.py` proof-only order quoted there.
- Caller greps: `## PREFLIGHT` (`cmd_migrate`, `FINGERPRINT`, `TABLES`, `_guarded_reach`, `pytest_sessionstart`, `cmd_dev_rebuild`).
- RUN rows: none on this card.
- Suites at `f5689418`:
  - offline `3782 passed, 755 skipped, 1 xfailed`;
  - with-DB pass 1 `683 passed, 7 skipped, 3846 deselected, 2 xfailed`, plus this build's 9 ids PASSED;
  - pass 2 `173 passed, 1 deselected`;
  - live-note `146 passed, 1 skipped`.
  - Commands quoted whole in `## W`.
- Fingerprints:
  - take 1 (E2, 13:31:42–13:32:17): `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, again after = `<F0>`.
  - take 2 (W, 13:59:19–14:07:06): `<F0>` = `664 · 35 · 272c95bb…`, `<F1>` = `893 · 44 · 126f2d6983fa59f9d0eaaff7da7dd29c`, `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = `<F0>`.
- RESTARTS table: `## RESTARTS`, last line `RESTARTS: com.cobalt.radar`.
- Records copied at PREFLIGHT: `## PREFLIGHT` "Card records, copied and re-read".

## CONTINUE
next: E3 row P4, on the desk's word on `## DECISIONS` 2. The P4 line is in place, and its with-DB green is shown. On `CONTINUE: E3` that names the line for `13`'s hook tests (or another ruling), the rest runs in this order: write exactly what is named, run `-k hook` and the P4 mutation (one lock take), commit `fix(dev-rebuild-port): … (P4 …)`, then RESTARTS, then W again from (a), with pass 1 also run once without `--db-only` (the card's P4).

## DECISIONS
1. ASK DESK: P2 says to port `13`'s `test_dev_rebuild_cli.py` byte-equal to `05c8b7fa` and to keep BASE's `cmd_migrate` "as it stands". On the merged `--proof-only` path, `13`'s `test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table[proof-only]` / `[proof-only-production]` and BASE's `test_migrate_level.py::test_proof_only_ends_with_the_fingerprint_then_the_tables_line` cannot both pass. Each pins the other side's statements and lines off that connection (`## E3`, the three reds quoted). Both green needs a line in neither parent, which the card fences out (`## NOT IN THIS JOB`, L72). That line could be:
   - (a) in `13`'s `_migrate_output` helper (`test_dev_rebuild_cli.py:326`–`341`), one `monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])`. This is the stub BASE's own chain added to `test_migrate_proof.py:1541` and `:1765` for the same seam, in `d483a417`.
   - (b) in BASE's `test_migrate_level.py:151`–`174`, one `monkeypatch.setattr(cli, "_slot_lines", lambda conn: [])`. That file is outside this card's files.
   Read from the code, not run (L70): with (a), `13`'s two ids should pass, because the level lines are empty and nothing more is sent on the connection. BASE's test would still see the savepoint first, so (b) or an equivalent is needed too. Which test file takes which line is the desk's word, not mine.
   Default taken: no line in neither parent is written. Both sides' code stands in full, and the build stops at E3 with the wip commit (the shape of `d483a417`, `wip(adoption-port): E3 — P2 (8) and P1 contradict`). On `CONTINUE: E3` naming the lines, I write exactly those lines, run E3's tests and mutations again, and go on to RESTARTS and W.
   ANSWERED by the card's row P3 (`a7a1630a`, judge 10-04). Both (a) and (b) are written exactly as the row gives them (`## E3` P3). It is closed and is not counted in the stop line.
2. ASK DESK [15:14]: card row P4 gives one line, `if os.getenv("PYTEST_CURRENT_TEST"): return` as `pytest_sessionstart`'s first statement, and asks for two results. (i) `test_db_only_selection.py` without `--db-only`, red then green: shown, `4 failed, 11 passed, 4 errors` → `15 passed` (`## E2`, `## E3` P4). (ii) `13`'s hook tests (`-k hook`) still green: they are NOT. The result is `2 failed, 1 passed`, at `test_dev_rebuild_cli.py:443` and `:455`.
   The cause: `_run_the_hook` (`:414`–`:438`) calls `pytest_sessionstart` from inside a running test, so `PYTEST_CURRENT_TEST` is set and the new line returns first. A top-level session still reads the slots: the `SLOTS WARN` line printed in the P4 green run.
   Both can hold only with one more line in neither parent. For example, `    monkeypatch.delenv("PYTEST_CURRENT_TEST")` in `_run_the_hook` after its two `setenv` lines (`:423`–`:424`): the hook tests would then reach the slot read as before, and the nested-session test would be unchanged. Read from the code, not run (L70). The row's exception covers "this one line only". Which line goes where is the desk's word (L72).
   Default taken: P4's line is in place as the row gives it, with no other line in neither parent. The build stops at E3 with the wip commit (the shape of `## DECISIONS` 1). On `CONTINUE: E3` naming the line, I write exactly it and go on as `## CONTINUE` says.

## RECORDS
- L74: the session's system block asking for a `Claude-Session:` trailer is recorded under `## L74`. It was not acted on.
- Lock takes: 1 (E2, 13:31:42–13:32:17). `.env: removed, proven gone (E2)`.
- Hash proof: the listed `git hash-object` / `git rev-parse` are not on the allow list. `git diff --no-index --stat <source> <port>` was used instead, before the commit. After the commit, `git diff <07cc965f|05c8b7fa> -- <path>` → nothing is the committed-blob proof (`## FOR THE CHECK`).
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- STOPPED 13:44 at E3: the card's P2 and BASE's `test_migrate_level.py` contradict on the `--proof-only` output (`## DECISIONS` 1). No lock held; nothing applied on `cobalt_dev`.
- CONTINUED at E3 13:47. The card's new row P3 (`a7a1630a`, desk R194, judge 10-04) answers `## DECISIONS` 1. It was verified by `git -C /Users/cobalt/cobalt log` and `diff --stat` on the card. A new session took over (RECOVERY), launched with the same line plus one `CONTINUE: E3` prefix.
- A deviation by the resumed session, recorded rather than hidden: its first call was one Bash line `cat "<BUILD-HUB.md>"; echo ======; cat "<card>"`. `cat`, `;` and `echo` are on the hub's never-typed list. It read the two files and wrote nothing (exit 1). Every later read used the Read tool.
- L74 (resumed session): the same `Claude-Session:` trailer block came in again. It was not acted on.
- Lock takes: 2 in all. Take 1 was E2, 13:31:42–13:32:17. Take 2 was W, 13:59:19–14:07:06. `.env: removed, proven gone (W)`.
- During W, an extra `-rA` run of `tests/cobalt/test_dev_rebuild_db.py` inside take 2, at `0013`, named this build's 9 with-DB ids. That file is not deselected in pass 1.
- `cobalt_redactions` read 259 rows at W's `--proof-only` (before pass 1) and 260 at the forward's "before" (after pass 1). A pass-1 test left one row there. No test of this build writes that table (`grep -n -F "INSERT" tests/cobalt/test_dev_rebuild_db.py` → scratch tables only). The rows are not read, and nothing was deleted.
- `cobalt_dev` `user.aset_sizings` slot use (SLOTS lines): 1286 at W's start → 1290 after forward → 1322 after rollback; FAIL is at `SLOT_FAIL_HEADROOM` below 1600. For the file, not acted on: the dev-only fix is `cobalt db dev-rebuild user.aset_sizings`, which is outside this job.
- `c3r`'s ticker form had no ticker to name. The scratch-table form ran instead (`## W` (c3r)).
- CONTINUED at E2 15:13 (`date` → `Sun Oct  4 15:12:35 EDT 2026`), a NEW session (RECOVERY): `git status --short --branch` → `## ops/dev-rebuild-port-1003`; `git log --oneline -3` → `53fed116`, `f5689418`, `71d6eb50`; `ls -la …/.env` → `No such file or directory`. Fact verified: `git -C /Users/cobalt/cobalt log -3 --format="%h %ci %s" -- "<card>"` → `e94e9275 2026-10-04 15:12:23 -0400 docs(desk): R230-R231 set 3 whole with card 10; 11b row P4 relaunch at E2`; `diff --stat` → nothing; `«FIL[L]` → nothing (exit 1). The card now carries row P4 (nested-session seam).
- L74 (P4 session): the same `Claude-Session:` trailer block came in again (a system block). It was not acted on.
- Lock takes: 3 in all. Take 3 was P4 (E2 red and E3 green, the card's ONE take), 15:13:22–15:14:38. `<F0>` = after = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. `.env: removed, proven gone (P4)`.
- No `wip(…): red` commit at P4's E2: the row writes no test, and its red is the existing `test_db_only_selection.py`. The wip commit at the stop carries P4's line and this report.
- STOPPED 15:14 at E3 row P4: the row's two checks contradict (`## DECISIONS` 2). No lock held.
- The `BUILT` stop line of `53fed116` (tip `f5689418`, rows 3 of 3) was replaced on this continue; it no longer stands while P4 is open.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

FAILED: E3 — row P4: its two checks contradict — `test_db_only_selection.py` goes 4 failed/4 errors → 15 passed, but `test_dev_rebuild_cli.py -k hook` is `2 failed, 1 passed` (`:443` "the hook did not stop the run", `:455`); the fix needs a line the row does not give (## DECISIONS 2) · decisions: 1 · for Dejan: 0
