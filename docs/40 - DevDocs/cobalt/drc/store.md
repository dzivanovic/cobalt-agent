# `src/cobalt/drc/store.py`

## What it does
`DrcStore` is the ONE writer of the three `drc_*` tables (L40). It is
pinned to the USER side (`SIDE = Side.USER`, L32), and its connection
comes from the one factory (`db.connect`). The database is chosen by
`COBALT_ENV` (RULING 7).

The store creates no table. Migration `db_migrations/0016_drc.sql`
does, through `cobalt db migrate`. `ensure_schema()` checks the schemas
and the three tables exist. If they are missing it raises
`SchemaMissingError`, which names the command to run.

## Writes
- **`record_import(import_date, result, data, executions=())`** — one
  `drc_imports` row per file.
  - The row carries the kind, the name, the sha256 of the exact bytes,
    and `parse_status` (`parsed` / `partial` / `failed`).
  - `reason` holds the `PARTIAL — missing: …` flag or the failure,
    `failed_line` the failing line, and `degraded` the shape flag.
  - `supersedes` points at the same day's latest file of that kind, so
    nothing is ever overwritten.
  - Unless the file failed, one `drc_fills` row is written per execution.
    A failed file stores zero fills. It is one transaction.
  - An `ignored` file, or one with no kind, is refused: it is listed,
    never stored.
- **`record_day(pairing, import_ids)`** — replaces the day's `drc_rows`
  in one transaction. It writes one row each for:
  - every trade (`ref` = `trade_id`)
  - every open position (the next day's seed, R67)
  - every stats row (`ref` = `line <n>`, with `match` = `matched` or the
    `unmatched — …` reason, so it is shown, never dropped)
  - the day itself: counts and `not_computed`

  Every row stores its `inputs` (import ids, fill lines, carried lots,
  the stats line), its `derived` value (the record's JSON) and
  `fn_version` = `pairing.FN_VERSION` (L57).

## Reads
**`seed_for(day)`** first checks that the chain of recorded days is
unbroken. It gets the prior trading day from
`daymode.propose.prior_trading_day`, then runs
`pairing.check_contiguity` against every earlier `day` row. Only then
does it return the prior trading day's `open_position` rows as
`OpenPosition`s. The very first import returns `[]`. A broken chain
raises `PairingError`: the position is never assumed flat, and a phantom
is never carried.

## Tests
`tests/cobalt/test_drc_store.py` has an offline half (the SQL, the
registry, the placement map, the one-writer grep). Its with-DB half
applies `FORWARD` inside the test's own migration-connection transaction,
which is always rolled back. It hands the store a savepoint proxy over
that connection. So the tables exist only inside the test, and no
migration is ever committed to `cobalt_dev`.
