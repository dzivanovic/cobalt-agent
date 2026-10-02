JOB: dev-rebuild
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R18
BRANCH: ops/dev-rebuild-1002
WORKTREE: dev-rebuild-1002
BASE: 6ae3f133
TIP:
REPORT: /Users/cobalt/cobalt-wt/dev-rebuild-1002/docs/40 - DevDocs/reports/dev-rebuild-build-2026-10-02.md
CHECK REPORT:
HOUSE A: none — overruled 2026-10-02 R47
HOUSE B:
TREE STATE: row T
RULINGS: 2026-10-02 R14, 2026-10-02 R18, 2026-10-02 R47

## ROWS

| row | what | red first | files |
|---|---|---|---|
| D1 | `rebuild_table(conn, schema, table, *, dry_run)` in a new module `src/cobalt/db_migrations/dev_rebuild.py`: in the caller's ONE transaction, read BEFORE, rebuild the table so every dropped column slot is freed, read AFTER, compare. BEFORE / AFTER = `max(attnum)`, dropped count, live count, row count, row digest (the migrate proof's own per-table digest in `cli.py`, one implementation, L3) and a `pg_catalog` digest of: live columns in order (name, type, collation, default, NOT NULL, identity, generated, storage, statistics target), constraints, indexes (with names), triggers, RLS enabled / forced and every policy, owner, table and column grants, comments, foreign keys OUT and IN, sequences owned by the table and their `last_value`, every view that depends on the table (definition and grants), reloptions, replica identity. Rule: commit only if every AFTER equals BEFORE except `max_attnum` = live and dropped = 0; else `RebuildMismatch` naming each differing field, nothing kept. `dry_run=True` rolls back after the compare whatever it shows | with-DB, in a new `tests/cobalt/test_dev_rebuild_db.py`, on `db.connect_migration(env.DEV_DB_NAME)` with `autocommit = False`, rolled back at the end: a constructed scratch table in `"user"` (identity id, a default, a NOT NULL, a CHECK, an index, a trigger, RLS on with one policy, a grant, a comment, a child table with an FK into it, a view over it, three rows) gets 5 columns added and dropped; after `rebuild_table` → `max_attnum` = live, dropped 0, rows and catalog digest equal. Negative control: a monkeypatched rebuild step that skips the grant → `RebuildMismatch` naming grants, and the table's BEFORE read back unchanged. RED on `BASE`: `ModuleNotFoundError: cobalt.db_migrations.dev_rebuild` | `src/cobalt/db_migrations/dev_rebuild.py`, `tests/cobalt/test_dev_rebuild_db.py`, `docs/40 - DevDocs/cobalt/db_migrations/dev_rebuild.md` |
| D2 | `cobalt db dev-rebuild <schema>.<table> [--dry-run] [--lock-timeout-s N]`, a subcommand beside `migrate` and `query` in `add_parser` (`src/cobalt/db_migrations/cli.py:797`). Refuses with exit 2 and NO connection opened: `COBALT_ENV` not `dev`; a schema other than `system` or `user`; a name outside `[a-z0-9_]`. After connecting through the one factory (`db.connect_migration(env.DEV_DB_NAME)`, L4: no secret read, printed or passed), refuses with exit 2 and nothing sent but the read: `current_database()` not `cobalt_dev`. Sets the migrate path's `lock_timeout` first (0 refused, as `migrate`). Prints BEFORE and AFTER lines, then exactly one of `REBUILT <schema>.<table> · max_attnum <b> → <a> · rows <n> = <n> · catalog digest equal`, `DRY RUN — ROLLED BACK · <the same fields>`, `FAILED: <field differences> — ROLLED BACK` (exit 1). No `--allow-prod` flag exists on this subcommand | offline, a new `tests/cobalt/test_dev_rebuild_cli.py`: `COBALT_ENV=production`, unset, and `dev` with `system.x;drop` each exit 2 with `db.connect_migration` monkeypatched to raise if called; a fake connection answering `cobalt_brain` → exit 2 and the only statement sent is the database read; `--lock-timeout-s 0` → exit 2; `--allow-prod` → argparse exit 2. RED on `BASE`: `invalid choice: 'dev-rebuild'` | `src/cobalt/db_migrations/cli.py`, `tests/cobalt/test_dev_rebuild_cli.py`, `docs/40 - DevDocs/cobalt/db_migrations/cli.md` |
| D3 | The table this job exists for: `"user".aset_sizings` (created by `src/cobalt/aset/migrations/0001_aset_sizings.sql`, altered by `aset/migrations/0002`–`0009` and registry `0004`, `0007`, `0021`, `0022`) passes D1's rule. Its dependents at `0013` include `"user".radar_cards_v`, the FKs in from `card_dots`, `radar_score_receipt`, the `0009` picks tables (`0021` `legs` and `0022` `prediction_records` above `0013`) | with-DB, in `tests/cobalt/test_dev_rebuild_db.py`: `rebuild_table(conn, "user", "aset_sizings", dry_run=True)` on `cobalt_dev` at `0013` → every field equal, `max_attnum` AFTER = live, rolled back. RED on `BASE`: the module import | `tests/cobalt/test_dev_rebuild_db.py` |
| T | TREE STATE. RUN — asserts nothing. The new with-DB tests run at `0013` inside THE PASS-1 COMMAND as written (they live in `tests/cobalt`, need no migration above `0013`, and roll back): `grep -n -F "test_dev_rebuild" "docs/40 - DevDocs/prompts/BUILD-HUB.md"` and the same on `DEPLOY-HUB.md` → no hit (no deselect owed); W (c)'s `-rs` output shows both files ran and none skipped. A test that needs a level above `0013` → it is deselected in pass 1 and added to pass 2 in both files, exactly as executed | — (tool output quoted) | `docs/40 - DevDocs/prompts/BUILD-HUB.md`, `docs/40 - DevDocs/prompts/DEPLOY-HUB.md` |

## NOT IN THIS JOB
- A real rebuild of any table on `cobalt_dev`: the build runs only the rolled-back tests. The real run is a dev-maintenance job on `DEVFIX-HUB.md` (card `12-devfix-route-card.md`).
- A launch-line or allow-string change; `STANDING-LIST.md`; `desk-launch.sh`.
- Any production path: no `--allow-prod`, no `cobalt_brain`, no `COBALT_ENV=production` test that opens a connection.
- A registry migration; `aset/migrations/`; the slot guard (card `13-slot-guard-card.md`).
- Recreating `cobalt_dev` from scratch.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-2026-10-01-1.md` `## L68 GATE` (c) and `## DECISIONS` 2.
- `/Users/cobalt/cobalt-wt/devdb-rebuild-1002/rebuild_aset_sizings.py` and `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/devdb-rebuild-2026-10-02.md`, if present at launch: the one-off this job makes standard (its dependents list and its digest are the reference; its `REBUILT` or `FAILED` line is quoted in PREFLIGHT).
- `src/cobalt/db_migrations/cli.py`: `add_parser` (~797), `cmd_migrate` (~575), `_apply` (~485), the proof digest and `DEFAULT_LOCK_TIMEOUT_S`.
- `src/cobalt/db.py`: `connect_migration`, `DEV_DB_NAME`; `src/cobalt/env.py:45`.
- `src/cobalt/db_query.py` `add_query_parser` (the read-only sibling's shape).
- `tests/cobalt/test_radar_score_migration.py` `_migration_conn` (~299): the rolled-back with-DB pattern.

## CHECK ASKS
- X1 Trace every path from `cobalt db dev-rebuild` to a connection: can any argument, environment or fallback reach `cobalt_brain`?
- X2 Name any `pg_catalog` property of a table the D1 digest misses and that a rebuild could lose (partitioning, publication membership, inheritance, column options, extended statistics, security labels, event-trigger effects).
- X3 Does the rebuild hold its locks for one transaction only, and does a refused compare leave the original table byte-for-byte (catalog and rows)?

## RECORDS
- RESTARTS class homes: `src/cobalt/db_migrations/dev_rebuild.py` and `cli.py` → `src/cobalt/jobs/restarts.py` "static import reach" (`:210`); `tests/cobalt/*` → "test/documentation" (`:239`); `docs/…` → DOCS (`:219`). No `configs/` path. (the drafter, 06:27 ET)
- At 06:30 ET `ls -la /Users/cobalt/cobalt-wt/devdb-rebuild-1002/` → `rebuild_aset_sizings.py` (33295 bytes, 06:30); its report ends `(run in progress)`. Its `digest()` (~108) and `rebuild()` (~363) cover owner and table / column ACLs, constraints, triggers, policies, FKs in, owned sequences, dependent views by depth; D1 makes that the standard, generalized to any `system` / `"user"` table. The script is uncommitted in a directory outside git: the builder reads it, never copies it whole without the D1 tests.
- `0007_radar_cards.sql` lines 32–56 hold 25 `ADD COLUMN` on `aset_sizings`; the deploy report quotes the proof footer as 29. Card 13 row S0 measures it.
