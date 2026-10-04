# dev-rebuild-port — build (2026-10-04)

## §0 Headline
(written at CLOSE)

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

STOPPED at E3, 13:44 ET (`date` → `Sun Oct  4 13:44:13 EDT 2026`). No lock is held: E2's take was released at 13:32:17, and nothing has been applied on `cobalt_dev`. Wip commit below.

## RESTARTS

## W THE THREE SUITES

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: E3 — on the desk's answer to `## DECISIONS` 1: write the named line(s), re-run E3's offline tests and the P2 mutations, then one extra lock take for the with-DB greens (or go straight to W), the `fix(dev-rebuild-port):` commit, RESTARTS, W.

## DECISIONS
1. ASK DESK: P2 says to port `13`'s `test_dev_rebuild_cli.py` byte-equal to `05c8b7fa` and to keep BASE's `cmd_migrate` "as it stands". On the merged `--proof-only` path, `13`'s `test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table[proof-only]` / `[proof-only-production]` and BASE's `test_migrate_level.py::test_proof_only_ends_with_the_fingerprint_then_the_tables_line` cannot both pass. Each pins the other side's statements and lines off that connection (`## E3`, the three reds quoted). Both green needs a line in neither parent, which the card fences out (`## NOT IN THIS JOB`, L72). That line could be:
   - (a) in `13`'s `_migrate_output` helper (`test_dev_rebuild_cli.py:326`–`341`), one `monkeypatch.setattr(cli, "_level_lines", lambda conn, probe: [])`. This is the stub BASE's own chain added to `test_migrate_proof.py:1541` and `:1765` for the same seam, in `d483a417`.
   - (b) in BASE's `test_migrate_level.py:151`–`174`, one `monkeypatch.setattr(cli, "_slot_lines", lambda conn: [])`. That file is outside this card's files.
   Read from the code, not run (L70): with (a), `13`'s two ids should pass, because the level lines are empty and nothing more is sent on the connection. BASE's test would still see the savepoint first, so (b) or an equivalent is needed too. Which test file takes which line is the desk's word, not mine.
   Default taken: no line in neither parent is written. Both sides' code stands in full, and the build stops at E3 with the wip commit (the shape of `d483a417`, `wip(adoption-port): E3 — P2 (8) and P1 contradict`). On `CONTINUE: E3` naming the lines, I write exactly those lines, run E3's tests and mutations again, and go on to RESTARTS and W.

## RECORDS
- L74: the session's system block asking for a `Claude-Session:` trailer is recorded under `## L74`. It was not acted on.
- Lock takes: 1 (E2, 13:31:42–13:32:17). `.env: removed, proven gone (E2)`.
- Hash proof: the listed `git hash-object` / `git rev-parse` are not on the allow list. `git diff --no-index --stat <source> <port>` was used instead, before the commit. After the commit, `git diff <07cc965f|05c8b7fa> -- <path>` → nothing is the committed-blob proof (`## FOR THE CHECK`).
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- STOPPED 13:44 at E3: the card's P2 and BASE's `test_migrate_level.py` contradict on the `--proof-only` output (`## DECISIONS` 1). No lock held; nothing applied on `cobalt_dev`.

FAILED: E3 — P2 and BASE contradict on --proof-only: 13's test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table[proof-only|proof-only-production] (byte-equal to 05c8b7fa) and BASE's test_migrate_level.py::test_proof_only_ends_with_the_fingerprint_then_the_tables_line cannot both pass without a line in neither parent — KeyError: 'radar_pool' / AssertionError: assert ('SET LOCAL search_path TO ' in 'SAVEPOINT cobalt_slots') · decisions: 1 · for Dejan: 0
