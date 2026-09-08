# `src/cobalt/db_migrations/placement.py`

## What it does
The map of which side every table is on. One map, three readers: the
suite's placement test (against what the database actually holds), the
store-side lint (every store names only its own side unqualified), and a
test asserting this map and `0002_move_tables.sql` agree.

## Key functions/classes
- `MOVED_TABLES` — the 12 that `0002` moves out of `public`.
- `SEEDED_TABLES` — created by `0001` on its side (`traders`).
- `MODULE_TABLES` — created by a feature module's own migration
  (`trade_defs`, `tunables`, `setup_trade_matrix`, `trader_settings`).
- `DECLARED_TABLES` — ruled before they are built (S2/S3), so the first
  migration that creates one has a side to create it on.
- `OLD_TREE_PUBLIC_TABLES` — the frozen 17. `public` is untouched
  (strangler rule) and a NEW table landing there fails the suite.
- `side_of(table)` / `tables_on(side)`.

## Gotchas
Two copies of the map exist — this one and the SQL's — because SQL
cannot import Python. A test makes a drift between them a failure rather
than a surprise.
