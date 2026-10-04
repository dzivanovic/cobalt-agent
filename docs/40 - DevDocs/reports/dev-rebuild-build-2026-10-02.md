# dev-rebuild — build report 2026-10-02

## §0 Headline

D1, D2 and D3 are built on `1df251b9`: `cobalt db dev-rebuild` and `dev_rebuild.rebuild_table`. Every red, mutation and green is quoted under E2 and E3. T is a RUN with no hub edit owed.
The three suites are green on `1df251b9`: offline 3781/0, with-DB 4384 + 171 = 4555/0, live-note 146/0. `cobalt_dev` is back at `0013` with F2 = F0, and `.env` is removed.
The build stopped once at W (b) because `ops-glob-1002` held the lock, and was CONTINUED at 08:44 on the desk's message, verified. RESTARTS: `com.cobalt.radar`. Decisions: none.
Facts for the desk are under `## RECORDS`: `aset_sizings` is at `max_attnum 198` again, and one W cycle costs 72 slots. The card's `radar_score_receipt` FK is not in the catalog.

## L74

At 07:58 ET, a harness system reminder asked that commits end with a `Claude-Session: https://claude.ai/code/session_011U5r7zrnhKq7mdTh3P75g2` line. It is recorded here once and no action is taken on it. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

| check | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Fri Oct  2 07:58:58 EDT 2026` |
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-02/11-dev-rebuild-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-02/11-dev-rebuild-card.md"` | 0 | `6af9a27ce789d19744325d324822aaece130070a` |
| card clean | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST R60 | `grep -n "^| R60 " ".../reports/cto-2026-09-30.md"` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** ... APPROVES STANDING-LIST.md once (4be06af0) ... \| APPROVED \|` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"\| R60 \|" -- ".../cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| R14 | `grep -n "^| R14 " ".../cto-2026-10-02.md"` | 0 | `21:\| R14 \| 06:18 ET \| HIS RULING: approves ... rebuild_aset_sizings.py ... standard dev-fix card owed ... \| HIS RULING · APPROVED \|` |
| R14 committed | `git -C ... log -1 --format=%H -S"\| R14 \|" -- ".../cto-2026-10-02.md"` | 0 | `02cfa29178cec4dcb95e4b43336b1ddf9118a69a` |
| R18 | `grep -n "^| R18 " ".../cto-2026-10-02.md"` | 0 | `25:\| R18 \| 06:23 ET \| HIS RULING (L73 override of L61, this launch only) ... the missing standard scripts get built ... \| HIS RULING · APPROVED \|` |
| R18 committed | `git -C ... log -1 --format=%H -S"\| R18 \|" -- ...` | 0 | `bc3a5da1b2e123af5959fa6ca2e5afe24b3a6303` |
| R47 | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only ... \| HIS RULING · APPROVED \|` |
| R47 committed | `git -C ... log -1 --format=%H -S"\| R47 \|" -- ...` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |

All of these pass.

## PREFLIGHT

| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/dev-rebuild-1002` + `?? "docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md"`: the only untracked file is this report, created by the hub's first Write |
| base | `git log --oneline -1` | 0 | `6ae3f133 docs(desk): 10-02 HANDOVER 54b9449c to 30eca1db` |
| branch in main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/dev-rebuild-1002` | 0 | `6ae3f133 docs(desk): 10-02 HANDOVER 54b9449c to 30eca1db` |
| no diff | `git diff --stat 6ae3f133` | 0 | (nothing) |
| base stat | `git show --stat 6ae3f133` | 0 | `docs/40 - DevDocs/reports/cto-2026-10-02.md \| 12 ++++++++++--` · `1 file changed, 10 insertions(+), 2 deletions(-)` |
| .env absent | `ls /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` | 1 | `No such file or directory` |
| no lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` |
| symbol | `grep -n -F "def add_parser" src/cobalt/db_migrations/cli.py` | 0 | `797:def add_parser(sub) -> None:` |
| symbol | `grep -n -F "def cmd_migrate" src/cobalt/db_migrations/cli.py` | 0 | `575:def cmd_migrate(args: argparse.Namespace) -> None:` |
| symbol | `grep -n -F "def _apply" src/cobalt/db_migrations/cli.py` | 0 | `485:def _apply(conn, paths) -> None:` |
| symbol | `grep -n -F "DEFAULT_LOCK_TIMEOUT_S" src/cobalt/db_migrations/cli.py` | 0 | `141:DEFAULT_LOCK_TIMEOUT_S = 30` · `653` · `823` · `826` · `844` |
| symbol | `grep -n -F "def connect_migration" src/cobalt/db.py` | 0 | `269:def connect_migration(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection:` |
| symbol | `grep -n -F "DEV_DB_NAME" src/cobalt/db.py` | 0 | `86:DEV_DB_NAME = env.DEV_DB_NAME` · `328:    "DEV_DB_NAME",` |
| symbol | `src/cobalt/env.py:45` (Read) | — | `DEV_DB_NAME = "cobalt_dev"` |
| symbol | `grep -n -F "def add_query_parser" src/cobalt/db_query.py` | 0 | `209:def add_query_parser(sub) -> None:` |
| symbol | `grep -n -F "def _migration_conn" tests/cobalt/test_radar_score_migration.py` | 0 | `299:def _migration_conn():` |
| wc | `wc -l <cli.py> <cli.md> <BUILD-HUB.md> <DEPLOY-HUB.md>` | 0 | `851` · `372` · `111` · `184` (new files: `dev_rebuild.py`, `dev_rebuild.md`, two test files) |
| READ | `ls -la /Users/cobalt/cobalt-wt/devdb-rebuild-1002/` | 0 | `rebuild_aset_sizings.py` 33212 bytes, `Oct  2 06:33` (the card's record said 33295 bytes at 06:30, so the file changed after the card was written) |
| READ tail | `tail -n 3 ".../reports/devdb-rebuild-2026-10-02.md"` | 0 | `REBUILT · aset_sizings max_attnum 1581 → 54 · rows 1 = 1 · FP F1 = F0 · proof test: PASSED · cobalt_dev: 0013 · .env: removed · decisions: 0 · for Dejan: 0` |
| READ tail | `tail -n 3 ".../reports/deploy-2026-10-01-1.md"` | 0 | `FAILED: gate — G (c) — tests/cobalt/test_radar_score_migration.py::test_card_checks_index_and_receipt_immutability_on_cobalt_dev (TooManyColumns: cobalt_dev "user".aset_sizings 1581/1600 column slots) · rollback: not used · decisions: 2 · for Dejan: 0` |
| T | `grep -n -F "test_dev_rebuild" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| T | `grep -n -F "test_dev_rebuild" ".../prompts/DEPLOY-HUB.md"` | 1 | (nothing) |
| RESTARTS | `uv run cobalt jobs restarts 6ae3f133..HEAD` | 0 | `docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md A DOCS -` · `RESTARTS: none` (the tool includes the untracked report; no code path) |

Card `## RECORDS` copied:
- RESTARTS class homes: `dev_rebuild.py` / `cli.py` → static import reach; `tests/cobalt/*` → test/documentation; `docs/…` → DOCS. This is re-read at RESTARTS.
- The one-off script: the size has changed since the card was written (33212 bytes at 06:33, not 33295 at 06:30). Its report now ends `REBUILT · aset_sizings max_attnum 1581 → 54`, not `(run in progress)`. `digest()` is at :108 and `rebuild()` at :363, both confirmed by Read.
- `0007` has 25 `ADD COLUMN`; the deploy quotes 29. This belongs to card 13 and is not re-read here. The proof-only footer below prints `aset_sizings: 29 card column(s)`, which is the length of `TABLE_DIGEST_EXCLUDED_COLUMNS["aset_sizings"]`.

THE LOCK PROBE (take 0, reads only), taken at 08:00 and released at 08:00:27:
- `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (exit 1)
- `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` → exit 0
- `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 08:00 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env`
- `<FP>` (typed exactly as BUILD-HUB gives it) → `<Fp>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 36 tables probed and no `CHANGED`. `legs`, `prediction_records`, `voice_turns` and `drc_*` are absent, which places `cobalt_dev` at `0013`. `aset_sizings user 1 0824685c130da3c7cb7f0e76191a6819`. Footer: `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.` · `code: 6ae3f133 (DIRTY: 1 path(s))`. The full table is under `## FOR THE CHECK`.
- `rm .../dev-rebuild-1002/.env` → 0; `ls .../.env` → `No such file or directory`. `.env: removed, proven gone (PREFLIGHT)`.

PROVEN BY FIRST REAL USE: as in the hub's table.

## E0 BASELINE

- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, on `6ae3f133`, exit 0) → `3769 passed, 673 skipped, 1 xfailed, 25 warnings in 604.82s (0:10:04)`: 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.95s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC ... not set`, and no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED

Written: `tests/cobalt/test_dev_rebuild_db.py` (D1 ×3, D3 ×1, with-DB) and `tests/cobalt/test_dev_rebuild_cli.py` (D2, offline, 12 tests). No `src/` edit.

- The first draft of the DB file imported `from cobalt.db_migrations import dev_rebuild`. Its red was `ImportError: cannot import name 'dev_rebuild' from 'cobalt.db_migrations'`, not the row's reason, so it was rewritten as `import cobalt.db_migrations.dev_rebuild as dev_rebuild`.
- The first draft of the CLI file imported `dev_rebuild` at module top, which would have made its red an import error rather than `invalid choice`. It was rewritten so the module is imported after the parse.
- Offline: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_cli.py` → `12 failed in 0.06s`. Every red reads `argparse.ArgumentError: argument command: invalid choice: 'dev-rebuild' (choose from migrate, query)`. That includes the `--allow-prod` test, whose assert shows `cobalt db: error: argument command: invalid choice: 'dev-rebuild'`.
- Offline: `uv run pytest ... tests/cobalt/test_dev_rebuild_db.py` → collection error `E   ModuleNotFoundError: No module named 'cobalt.db_migrations.dev_rebuild'`.
- With-DB, ONE lock take (taken 08:13, released 08:14:18): `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `cp …/.env` · `ls -la` → `-rw-------  1 cobalt  staff  2186 Oct  2 08:13 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` · `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` · `--proof-only` → the same 36-table picture as PREFLIGHT (`aset_sizings user 1 0824685c130da3c7cb7f0e76191a6819`; the tables above `0013` absent; no CHANGED; `code: 6ae3f133 (DIRTY: 3 path(s))`). Level `0013`; NO forward.
  - `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` → `E   ModuleNotFoundError: No module named 'cobalt.db_migrations.dev_rebuild'` · `ERROR tests/cobalt/test_dev_rebuild_db.py` · `1 error in 0.09s`.
  - `<FP>` again → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>`. `rm .env`; `ls` → `No such file or directory`. `.env: removed, proven gone (E2)`.
- RUN row T: there is no RUN command at E2. Its greps ran at PREFLIGHT (no hit in either hub file), and its W (c) reading is taken at W.
- Commit `fe638d17 wip(dev-rebuild): red — D1 D2 D3 tests before any src edit`.

## E3 THE ROWS

Before editing, every `file:line` the card names was re-read from the file: `cli.py` `add_parser` :797, `cmd_migrate` :575, `_apply` :485, `_probe` / `_digest_rows`, `DEFAULT_LOCK_TIMEOUT_S` :141; `db.py` `connect_migration` :269; `env.py` :45; `db_query.py` `add_query_parser` :209; `test_radar_score_migration.py` `_migration_conn` :299.

**D1** — new `src/cobalt/db_migrations/dev_rebuild.py`. `rebuild_table` takes ACCESS EXCLUSIVE outside a savepoint and runs everything else under `conn.transaction()` (a savepoint, because the caller's transaction is already open). BEFORE = `read_state`, then `_rebuild` (the one-off's capture / detach / create / copy / reattach, generalized by schema), then AFTER = `read_state`, then `differences`. A mismatch raises `RebuildMismatch(fields)` and the savepoint rolls back. `dry_run` raises `psycopg.Rollback()`. The module never commits. The row digest is the migrate proof's per-table digest, extracted in `cli.py` as `_content_digest` (`_probe` now calls it, L3) over the whole `to_jsonb(t)`. The catalog sections are `table`, `grants`, `columns`, `constraints`, `fks_out`, `fks_in`, `indexes`, `triggers`, `policies`, `sequences` (with `last_value`) and `views`. Unhandled shapes raise `RebuildRefused`.
- With-DB green, then two findings fixed in the rows' files:
  1. The negative control first read `Failed: DID NOT RAISE <class '…RebuildMismatch'>`. The scratch table's `GRANT SELECT, INSERT … TO cobalt_user` is most likely already covered by the schema's default privileges, so skipping the grant step changed nothing. The test now adds grants no default gives (`GRANT SELECT … TO cobalt_system WITH GRANT OPTION`, `GRANT UPDATE (note) … TO cobalt_system`) and asserts that `grants` sees both. `_restore_acl` now also revokes from every grantee a fresh relation carries, so the schema's default privileges cannot leave grants the original did not have.
  2. D3 first read `AssertionError: radar_score_receipt`. At `0013` the catalog holds no FK between `aset_sizings` and `radar_score_receipt`: the `fks_out` lines go to `system.radar_membership`, `system.radar_score` and `"user".traders`. The FKs in come from `0007` `card_dots` (:121) and `card_dot_taps` (:144) and from `0009` `picks` (:19) and `missed` (:71). The test now asserts those four (record under `## RECORDS`).
- Green, with-DB, extra lock take 2 (08:19–08:20:56): `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_dev_rebuild_db.py` → `PASSED …test_d1_rebuild_frees_every_dropped_slot_and_keeps_rows_and_catalog` · `PASSED …test_d1_negative_control_a_skipped_grant_is_refused_and_nothing_is_kept` · `PASSED …test_d1_dry_run_rolls_back_after_the_compare` · `PASSED …test_d3_aset_sizings_passes_the_rule_as_a_dry_run_at_0013` · `4 passed in 0.38s`.
- MUTATION M1 (undoes D1: `_rebuild(...)` → `pass`) → `4 failed in 0.21s`; first line `E   cobalt.db_migrations.dev_rebuild.RebuildMismatch: AFTER differs from BEFORE in: max_attnum, dropped`. The negative control reads `assert ('max_attnum', 'dropped') == ('grants',)`. Undone.
- MUTATION M2 (breaks the negative control: `differences` skips `grants`) → `1 failed, 3 passed in 0.30s`; `E   Failed: DID NOT RAISE <class 'cobalt.db_migrations.dev_rebuild.RebuildMismatch'>` on `test_d1_negative_control_…`. Undone.

**D3** — test only. MUTATION M3 (the view reattach loop iterates `cap["views"][:0]`) → `4 failed in 0.33s`; D3's red reads `RebuildMismatch: AFTER differs from BEFORE in: views`. Undone. M1 also turns D3 red: `aset_sizings` currently carries dropped slots again, as the read below shows.
- A read I added (lock held, `ls -la …/.env` listed first): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT max(a.attnum) …, count(*) FILTER (WHERE a.attisdropped) …, count(*) FILTER (WHERE NOT a.attisdropped) … '\"user\".aset_sizings'::regclass …"` → `max_attnum 126 · dropped 72 · live 54`.
- `<FP>` at the end of take 2 → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` (= `<F0>`). `rm .env`; `ls` → `No such file or directory`. `.env: removed, proven gone (E3)`.

**D2** — `cli.py`: `cmd_dev_rebuild` and the `dev-rebuild` subparser (`target`, `--dry-run`, `--lock-timeout-s`; no `--allow-prod`). `_checked_lock_timeout` is now shared with `cmd_migrate`. `_open` is the one `connect_migration` call line, which `_connect` now uses. The rows' neighbour `tests/cobalt/test_tenancy.py` first went red on two lints: `TestOneFactoryLint::test_connect_migration_has_exactly_one_caller` (`Found: ['…cli.py:571', '…cli.py:834', '…cli.py:877']`) and `TestReservedWordLint::test_no_unquoted_user_schema_reference_in_python` (`…cli.py:963`, a help string). Both were fixed in `cli.py`: the single `_open` line, a docstring without the call form, and a reworded help string.
- Green offline: `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/cobalt/test_dev_rebuild_cli.py tests/cobalt/test_dev_rebuild_db.py tests/cobalt/test_migrate_proof.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_tenancy.py tests/cobalt/test_db_query.py` → `89 passed, 74 skipped in 1.92s`. An earlier, wider neighbour run (also `test_p4_migrations`, `test_legs_migration`, `test_radar_migration`, `test_f15_p1_records_offline`, `test_archiver_migrations`) → `174 passed, 88 skipped in 2.33s`. `test_placement.py` + `test_jobs_restarts.py` → `25 passed in 11.84s`.
- MUTATION M4 (undoes the `COBALT_ENV` refusal: `if mode != env.DEV` → `if False`) → `1 failed, 11 passed`; `E   AssertionError: db.connect_migration was called` on `test_refused_with_exit_2_and_no_connection[production-user.aset_sizings]`. Undone.
- MUTATION M5 (undoes the `current_database()` refusal). The first run was red for an incidental reason (`AttributeError: 'FakeConn' object has no attribute 'transaction'`), so the test was rewritten: `rebuild_table` is stubbed, and the statement list is asserted before the exit code. Re-run → `1 failed, 11 passed`; `E   assert ['SELECT curr...eout = '30s'"] == ['SELECT current_database()']` · `Left contains one more item: "SET LOCAL lock_timeout = '30s'"`. Undone.
- `git diff --stat` after the undos → only the intended edits (`cli.md` 3, `cli.py` 203, the two test files); `grep -n -F "MUTATION"` on both modules → nothing.

**T** — RUN. `grep -n -F "test_dev_rebuild"` on `BUILD-HUB.md` and on `DEPLOY-HUB.md` → no hit (PREFLIGHT). The new with-DB tests need no level above `0013`: they pass at `0013` (take 2), so no deselect is owed and neither hub file changes. The W (c) `-rs` reading is under `## W`.

DevDocs: `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` (new, `## 2026-10-02 — dev-rebuild`) and `cli.md` (`## 2026-10-02 — dev-rebuild`).

Commit `1df251b9 feat(dev-rebuild): cobalt db dev-rebuild frees a dev table's dropped column slots, kept only on an equal compare (D1, D2, D3; L1, L3, L4, L76)`.

## RESTARTS

`uv run cobalt jobs restarts 6ae3f133..HEAD` (HEAD `1df251b9`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md	A	DOCS	-
docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md	A	DOCS	-
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/dev_rebuild.py	A	static import reach	com.cobalt.radar
tests/cobalt/test_dev_rebuild_cli.py	A	test/documentation; no resident	-
tests/cobalt/test_dev_rebuild_db.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
There is no `UNCLASSIFIED` row and no `configs/` path. This matches the card's record (static import reach / test / DOCS).

## W THE THREE SUITES

`<tip>` = `1df251b9`.
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, exit 0) → `3781 passed, 677 skipped, 1 xfailed, 25 warnings in 591.83s (0:09:51)`; `grep -c -F "FAILED"` on the output → `0`. `<p>` = 3781. Against E0 that is +12 passed (the 12 tests in `tests/cobalt/test_dev_rebuild_cli.py`) and +4 skipped (`SKIPPED [1] tests/cobalt/test_dev_rebuild_db.py:94` / `:126` / `:141` / `:154: Postgres env settings not available`, which are this build's with-DB tests and run in (c)).
- (b) THE LOCK (a) at 08:32: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `-rw-------  1 cobalt  staff  2186 Oct  2 08:25 /Users/cobalt/cobalt-wt/ops-glob-1002/.env`. **The lock is held by another worktree.** I did not take it. `ls /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` → `No such file or directory`, and no migration of mine is applied (no forward was run).
- CONTINUED 08:44. (b) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `cp …/.env` · `ls -la` → `-rw-------  1 cobalt  staff  2186 Oct  2 08:44 /Users/cobalt/cobalt-wt/dev-rebuild-1002/.env` (lock taken 08:44). `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `--proof-only` → 36 tables; the tables above `0013` read `-`; no CHANGED; `NOTHING WAS APPLIED`; `code: d7574799 (DIRTY: 1 path(s))`. `cobalt_dev` is at `0013`.
- (c) PASS 1, background, the hub's command byte for byte with NO added deselect (this build's with-DB tests need no level above `0013`) → `4384 passed, 7 skipped, 65 deselected, 3 xfailed, 31 warnings in 707.47s (0:11:47)`, exit 0. The SKIPPED lines are `test_cards_picks.py:388` (S2-P2's card_score column is present on cobalt_dev), `test_cards_picks.py:401` (real S2-P2 0007 applied …), `test_radar_evaluate.py:695` (COBALT_LIVE_VAULT_ROOT), `test_replay_line.py:266` (COBALT_TEST_LIVE_DRC), `test_s3_c4_experiments.py:95` (COBALT_LIVE_VAULT_ROOT), `test_catalyst.py:365` and `test_predicate.py:262` (COBALT_LIVE_VAULT_ROOT). These are the seven of `deploy-2026-10-01-1.md`, and none names `test_dev_rebuild`. `<d1>` = 4384. RUN row T: both new files ran in pass 1 and none skipped.
- (c2) FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `-- applying 0001_schemas.sql` … `0013` … `0014` … `0022_prediction_records.sql`. Every pre-existing table is `OK`. `drc_events`, `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `legs`, `prediction_records` and `voice_turns` are `CREATED`. `content UNCHANGED on every table.` This build adds no migration. **dev forward: APPLIED 08:56:59.** `<FP>` → `<F1>` = `cols 893 · rels 44 · views_md5 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, background, the hub's command byte for byte with nothing added (no test of this build was deselected in pass 1) → `171 passed, 1 deselected, 5 warnings in 222.71s (0:03:42)`, exit 0; no SKIPPED, FAILED or ERROR line. `<d2>` = 171. `<d>` = 4384 + 171 = **4555**. This build has no `-rA` id of its own in pass 2; its with-DB tests ran in pass 1.
- (c3r) NOTHING LEFT BEHIND: `ls -la …/dev-rebuild-1002/.env` → listed. My with-DB tests write NO row into `aset_sizings` (D3 only rebuilds inside a rolled-back savepoint), so there is no ticker to list. What they could leave is their scratch relations, so I ran an added read: `COBALT_ENV=dev uv run cobalt db query --side user "SELECT n.nspname, c.relname, c.relkind FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE left(c.relname, 14) = 'zz_dev_rebuild' OR left(c.relname, 14) = 'zz_rebuild_old'"` → header only, **no rows**. A first form with `LIKE 'zz_dev_rebuild%'` was refused by the query tool's placeholder parser (`FAILED: ProgrammingError: only '%s', '%b', '%t' are allowed as placeholders, got '%''`) and was rewritten with `left()`. The added read `aset_sizings` slots at the top level → `max_attnum 198 · dropped 140 · live 58`.
- (c4) not applicable: this build adds no migration.
- (f) `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `-- applying 0022_prediction_records.rollback.sql` … `0014_radar_handicap.rollback.sql`, newest first. The eight tables above `0013` read `DROPPED` and every other table `OK`: `content UNCHANGED on every table.` `<FP>` → `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field. **cobalt_dev: 0013 — F2 = F0.** The added read of `aset_sizings` at `0013` → `max_attnum 198 · dropped 144 · live 54`. The lock's (d): `rm …/.env`; `ls …/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`. `.env: removed, proven gone (W)`; lock released at 09:01:47.
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 25.26s`. The only skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), and none names `COBALT_LIVE_VAULT_ROOT`. `<l>` = 146.
- TREE STATE (row T): the diff adds `tests/cobalt/test_dev_rebuild_db.py`, a with-DB test that runs at `0013` inside pass 1 as written, and nothing under `src/cobalt/db_migrations/` that is a migration. So both hub files are unchanged, which is exactly what (c) and (c3) executed.

## PRE-STOP SELF-CHECK

1. **Every added or changed test was shown red for its named reason against a mutation or a negative control, and any test that stayed green was rewritten.**
   - D2: all 12 CLI tests went red at E2 with `invalid choice: 'dev-rebuild'`. M4 turned the production refusal red with `db.connect_migration was called`. M5 turned the database-read refusal red with `Left contains one more item: "SET LOCAL lock_timeout = '30s'"`; that was after a rewrite, because the first M5 red was incidental.
   - D1: the three tests went red at E2 with `ModuleNotFoundError`, then under M1 with `RebuildMismatch: … max_attnum, dropped`. Under M2 the negative control read `DID NOT RAISE`.
   - D1's negative control had been green for the wrong reason (`DID NOT RAISE` at first) and was rewritten.
   - D3: red at E2 with `ModuleNotFoundError`, then under M3 with `RebuildMismatch: … views`.
   - The three outcome-line tests (`REBUILT` / `DRY RUN` / `FAILED`) went red at E2 (`invalid choice`). They pin the CLI's commit-only branch, which D2 does not name as its fix, so no separate mutation was run on it. Every test is backed.
2. **Every entry path of each rule is pinned by a test.**
   - `rebuild_table(` has one caller, `cli.py:897` (the grep at tip), pinned by the three CLI outcome tests. Its direct use is pinned by the four DB tests.
   - `_content_digest(` callers are `cli.py:361` (`_probe`), pinned by the existing migrate-proof tests, which ran green in the offline run, pass 1, and the (c2) and (f) proof tables. The other caller is `dev_rebuild.py:198`, pinned by D1 and D3.
   - `_checked_lock_timeout(` callers are `cli.py:687` (`cmd_migrate`), pinned by the existing `test_migrate_proof.py` lock-timeout tests (offline green), and `cli.py:876`, pinned by `test_lock_timeout_zero_is_refused_with_exit_2_and_no_connection`.
   - `_open` (the one call, `cli.py:534`) is pinned by `test_tenancy`'s one-caller lint and by `test_a_connection_to_another_database_sends_only_the_read` (`opened == [("cobalt_dev", {"allow_prod": False})]`).
   - The flag combinations covered are `--dry-run`, `--lock-timeout-s 5`, `--lock-timeout-s 0` and `--allow-prod`. The env states covered are production, unset and dev, and the targets `system.x;drop`, `public.…`, upper case and no dot.
3. **Every `file:line`, count and quote in the report was re-read from tool output at the tip.** At tip these were re-run: `grep -n -F "connect_migration(" …cli.py` → `534`, `def cmd_dev_rebuild` → `834`, `def rebuild_table` → `734`, the three caller greps above, `git log --oneline 6ae3f133..HEAD`, and `wc -l` (`dev_rebuild.py` 771, `cli.py` 1002). The suite summaries are quoted from their outputs.

## FOR THE CHECK

- Range `6ae3f133..1df251b9` (code tip). Commits: `fe638d17 wip(dev-rebuild): red — D1 D2 D3 tests before any src edit` · `1df251b9 feat(dev-rebuild): cobalt db dev-rebuild frees a dev table's dropped column slots, kept only on an equal compare (D1, D2, D3; L1, L3, L4, L76)` · `d7574799 wip(dev-rebuild): W (b) — cobalt_dev lock held by ops-glob-1002` (report only) · the report commit.
- Per row, the reds, mutations and greens are quoted under `## E2 RED` and `## E3 THE ROWS`. The caller greps are under PRE-STOP SELF-CHECK (2). RUN row T is under E3 / W.
- Suites: offline `3781 passed, 677 skipped, 1 xfailed` (the W (a) command) · pass 1 `4384 passed, 7 skipped, 65 deselected, 3 xfailed` (the hub's PASS-1 COMMAND byte for byte, nothing added) · pass 2 `171 passed, 1 deselected` (the hub's PASS-2 COMMAND byte for byte, nothing added) · live-note `146 passed, 1 skipped`.
- Fingerprints per lock take:
  - take 0 (PREFLIGHT, 08:00–08:00:27): `<Fp>` 664 / 35 / `272c95bb…`
  - take 1 (E2, 08:13–08:14:18): `<F0>` = after, 664 / 35 / `272c95bb…`
  - take 2 (E3 extra, 08:19–08:20:56): before = after, 664 / 35 / `272c95bb…`
  - take 3 (W, 08:44–09:01:47): `<F0>` 664 / 35 / `272c95bbb12241e3611e4b36326ccf87` · `<F1>` 893 / 44 / `126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` 664 / 35 / `272c95bbb12241e3611e4b36326ccf87`
- The RESTARTS table is under `## RESTARTS` and its last line is `RESTARTS: com.cobalt.radar`.
- The records copied at PREFLIGHT are under `## PREFLIGHT`.
- Notes for the check asks:
  - X1: the dbname is the literal `env.DEV_DB_NAME`, through `_open(..., allow_prod=False)`, after a `COBALT_ENV == dev` check, and `db._prod_gate` would refuse `cobalt_brain` in any case.
  - X2: `read_state`'s `table` section counts partitions, inheritance, publications, extended statistics and security labels, and `_capture` refuses any non-zero count. Column options, storage, compression and statistics target are in `columns`. Index-level column statistics and event-trigger effects are not read.
  - X3: the lock is taken outside the savepoint and held to the caller's transaction end, and the negative control proves `read_state` after a refusal equals BEFORE.

## CONTINUE

next: none. The build is closed.

## DECISIONS

none

## RECORDS

- Extra lock take (take 2, E3, 08:19–08:20:56): run before W so the with-DB greens and the D1 / D3 mutations were not first seen at W. `.env` was removed and proven gone, and `<FP>` = `<F0>`.
- The card's D3 text names `radar_score_receipt` among the FKs into `aset_sizings`. At `0013` the catalog has none: the FKs in are `card_dots`, `card_dot_taps`, `picks` and `missed`, and the FKs out go to `system.radar_membership`, `system.radar_score` and `"user".traders`. The D3 test asserts what the catalog holds.
- At 08:20, `cobalt_dev` `"user".aset_sizings` reads `max_attnum 126 · dropped 72 · live 54`: 72 slots dropped again since the one-off's `1581 → 54`. This build rebuilt nothing for real (`## NOT IN THIS JOB`).
- The card's record said the one-off script was 33295 bytes at 06:30. At launch it is 33212 bytes, `Oct  2 06:33`.
- L74: one harness reminder asking for a `Claude-Session:` trailer, recorded under `## L74` and not acted on.
- STOPPED 08:32 at W (b): lock held by `/Users/cobalt/cobalt-wt/ops-glob-1002/.env`. The wip commit is `d7574799`.
- CONTINUED at W (b) 08:44, on the `cto-desk` message `CONTINUE: the cobalt_dev lock is free now (ops-glob BUILT, its .env removed …)`. I verified it myself: `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` (exit 1). The message names a step and states a fact; it grants nothing.
- The slot count, measured. `aset_sizings` stood at `max_attnum 126 · dropped 72` at 08:20 and at `max_attnum 198 · dropped 144` after this build's one W forward and rollback (09:01). One W cycle therefore costs 72 slots, so about 19 more W cycles reach 1600. The fix is out of this job: the real rebuild is card `12` and the slot guard is card `13`.
- The one added read at (c3r) whose first form was refused: `LIKE '…%'` through `cobalt db query` → `ProgrammingError: only '%s', '%b', '%t' are allowed as placeholders`. It was rewritten with `left()`.
- Lock takes: 0 (PREFLIGHT), 1 (E2), 2 (E3, extra), 3 (W). Each ended `.env: removed, proven gone`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: dev-rebuild · tip: 1df251b9 | on 6ae3f133 | migration: none | offline 3781/0 | with-DB 4555/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
