# `src/cobalt/archiver/store.py`

## What it does
Persistence for archived bars, into `bars` in whichever database
`COBALT_ENV` names — `cobalt_brain` in production, `cobalt_dev` in dev
and under the test suite (RULING 9, 2026-09-04). Idempotent
by construction: PK `(ticker, interval, ts)` plus `ON CONFLICT ... DO
UPDATE` means re-running a night, or re-backfilling a ticker that
already has bars, never duplicates a row — it refreshes the existing
one in place. DDL lives in exactly one file
(`migrations/0001_bars.sql`), executed here, not duplicated.

## Key functions/classes
- `MIGRATION_SQL` — path to the one DDL file.
- `BarStore(db_name=None)` — thin wrapper around
  `cobalt.db.connect(self.db_name)`, where `self.db_name` is
  `db_name or env.resolve_db_name()`. The argument is a TEST/TOOLING
  seam only, exactly as on `AsetStore` and `VaultWriteStore`; every
  real call site passes nothing. Until RULING 9 the default was the
  literal `"cobalt_dev"`, which is how three weeks of production
  nightly runs archived into the dev database.
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
failure, same as a `CollectorError`. Writes to the `bars` table in the
database the resolver returns.

## Config it reads
No config file. The database comes from `COBALT_ENV` via
`cobalt.env.resolve_db_name()` — unset raises at boot rather than
defaulting. Actual connection parameters come from `cobalt.db.connect`'s
environment-variable read.

## Gotchas
- **`bars` lives in `cobalt_brain` as of RULING 9** (2026-09-04),
  migrated with all 4,563,539 rows (dump → schema via `ensure_schema()`
  → `pg_restore --data-only` → identical md5 over PK-ordered rows →
  `cobalt_dev.bars` dropped). There are no sequences on this table —
  the PK is composite, not an identity column — so nothing needed
  resetting, unlike the RULING 7 migration.
- The table carries one row of **pre-fixture test residue**:
  `TESTARCH/i5/2026-08-28 09:30Z`, written by `test_archiver_store.py`
  before the autouse transaction fixture existed, and carried into
  `cobalt_brain` by a migration that had to be byte-exact to prove
  itself. It is outside RULING 8's named scope and was left in place
  deliberately. `TESTARCH` is in no watchlist tier, so no real run can
  reproduce it.
