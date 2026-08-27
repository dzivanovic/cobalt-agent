# `src/cobalt/archiver/store.py`

## What it does
Persistence for archived bars, into `bars` in `cobalt_dev`. Idempotent
by construction: PK `(ticker, interval, ts)` plus `ON CONFLICT ... DO
UPDATE` means re-running a night, or re-backfilling a ticker that
already has bars, never duplicates a row — it refreshes the existing
one in place. DDL lives in exactly one file
(`migrations/0001_bars.sql`), executed here, not duplicated.

## Key functions/classes
- `MIGRATION_SQL` — path to the one DDL file.
- `BarStore(db_name="cobalt_dev")` — thin wrapper around
  `cobalt.db.connect(self.db_name)`. Never called with `"cobalt_brain"`
  anywhere in this package; `db.connect` refuses it regardless.
  - `.ensure_schema()` — `CREATE TABLE IF NOT EXISTS`, idempotent,
    called once at the start of every run.
  - `.upsert_bars(bars) -> int` — batches all bars from one fetch into
    a single `executemany` with `ON CONFLICT (ticker, interval, ts) DO
    UPDATE SET open=EXCLUDED.open, ...` (updates OHLCV, not the key).
    `DO UPDATE` rather than `DO NOTHING` is deliberate: a re-pulled bar
    that Finviz has since finalized/revised should overwrite the
    earlier (possibly provisional) values, not freeze at first-seen.
    Returns the row count attempted (not the count actually changed —
    Postgres doesn't cheaply distinguish insert vs. update per row in
    an `executemany`, and the caller only needs "how many bars did this
    fetch contribute" for the run report).
  - `.count_rows()` — total row count, used by the store's own tests
    to verify idempotency (before/after an upsert of an already-seen key).

## Data flow in/out
**In:** a `list[Bar]` (from `collector.fetch_bars`).
**Out:** the row count, or a raised exception (connection/schema
failure) — `runner.py` catches broadly and treats it as a per-ticker
failure, same as a `CollectorError`. Writes to the `bars` table in
whichever database `db_name` names (`cobalt_dev` in every real call site).

## Config it reads
None directly — `db_name` is passed in by the caller (`runner.py`);
actual connection parameters come from `cobalt.db.connect`'s
environment-variable read.
