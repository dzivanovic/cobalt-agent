# `src/cobalt/db_migrations/dev_rebuild.py`

## What it does
Rebuilds one `system` / `"user"` table on `cobalt_dev` so that every dropped column slot is freed. Postgres never reuses a dropped column's `attnum`: on 2026-10-01 `"user".aset_sizings` reached `max_attnum 1581` of the 1600 limit (`deploy-2026-10-01-1.md`). The rebuild keeps its result only when it can prove that nothing else changed.

In the caller's ONE transaction it takes ACCESS EXCLUSIVE on the table, outside a savepoint. Under the savepoint it reads BEFORE, rebuilds, reads AFTER and compares. The result is kept only if every AFTER value equals BEFORE, except that `max_attnum` must equal `live` and `dropped` must be 0. Anything else raises `RebuildMismatch`, which names each differing field, and the savepoint is rolled back. `dry_run=True` rolls the savepoint back after the compare, whatever it shows. The module never commits; `cobalt db dev-rebuild` does that (`cli.md`).

## Key functions/classes
- `rebuild_table(conn, schema, table, *, dry_run) -> RebuildResult` — the rule above.
- `read_state(conn, schema, table) -> TableState` — `max_attnum`, `dropped`, `live`, `rows`, `row_digest` (the migrate proof's `cli._content_digest` over the whole `to_jsonb(t)`, L3), and `sections`, a `pg_catalog` digest by name. The sections are `table` (owner, reloptions, RLS enabled / forced, replica identity, comment, shape), `grants` (table and column ACLs), `columns`, `constraints`, `fks_out`, `fks_in`, `indexes`, `triggers`, `policies`, `sequences` (with `last_value`) and `views` (every dependent view by depth, with definition and grants).
- `differences(before, after)` — the rule's field list.
- `RebuildRefused` — a precondition or shape this module does not handle is refused, never guessed (L1). This covers a schema outside `system` / `user`, an autocommit connection, rules, inheritance or partitions, publications, extended statistics, security labels, a serial-style owned sequence, a virtual generated column, and a dependent that is not a plain view.

## Origin
This generalizes the one-off `rebuild_aset_sizings.py` (`devdb-rebuild-2026-10-02.md`, `REBUILT · aset_sizings max_attnum 1581 → 54`) from one table to any `system` / `"user"` table.

## 2026-10-02 — dev-rebuild
New module (rows D1, D3). Tests: `tests/cobalt/test_dev_rebuild_db.py`, which is with-DB, rolled back, and runs at `0013`.

## 2026-10-02 — dev-rebuild check
The check found four things the digest missed and the rebuild lost (O1–O4). The `table` section now reads the access method and the TOAST reloptions, and the rebuild re-makes both. The `indexes` section reads each index column's statistics target, and the `views` section reads each view column's default; the rebuild re-sets both. A table or index outside the default tablespace is now refused (O5). Tests: `test_check_o1`–`test_check_o4`.

## 2026-10-02 — slot-guard
Adds the slot read (S1, S2): `slot_report(conn)` returns `(schema, table, max_attnum, dropped, live)` for every `system` / `"user"` table, highest first, in one catalog query; `cobalt db migrate` and the with-DB suite's session start both call it (L3). `slot_lines(rows, warn_at)` returns one `SLOTS WARN … · fix: cobalt db dev-rebuild <schema>.<table> (dev only)` line per table at or above `warn_at`, else one `SLOTS ok · highest <schema>.<table> <n> of 1600`. `slot_verdict(rows, warn_at, fail_headroom)` returns `fail` when any table has fewer than `fail_headroom` free slots, `warn` when any is at or above `warn_at`, else `ok`. New constants: `SLOT_LIMIT` (1600) and `SLOT_FAIL_HEADROOM` (64).
