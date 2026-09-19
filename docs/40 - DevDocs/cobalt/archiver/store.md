# `src/cobalt/archiver/store.py`

S2-P1 adds the optional `before_commit` seam to `upsert_bars` and a `(ticker, interval)` watermark read. The hook runs last inside the transaction.

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

---

## 2026-09-19 — the fold: ONE range read, `bars_in_range`

The two sections below are history and stay as written. What is LIVE
after `sprint-2/p4` landed and this branch rebased onto it: the store
has exactly ONE range read, `bars_in_range`, and both of the methods
those sections describe are gone into it (L3, spec O-5 — the fold the
append path's own docstring said was owed "at integration").

```
bars_in_range(conn, ticker, interval, start, end, *,
              end_inclusive=True, as_bars=False)
```

The two reads were the same SELECT differing on three axes, and each is
now a parameter instead of a second copy:

| axis | archiver (was `_bars_in_range`) | replay (was `bars_between`) |
|---|---|---|
| connection | the caller's transaction | `conn=None` → the store opens and closes its own |
| end bound | `end_inclusive=True` → `[start, end]` | `end_inclusive=False` → `[start, end)` |
| rendering | `{ts: BarValues}`, normalised to `NUMERIC(14,4)` / integer volume | `as_bars=True` → `list[Bar]`, oldest first |

**Neither caller's result changed.** The archiver must still pass its
own connection — §8's pre-commit re-check compares against rows read
inside the repair's `target_transaction`, and a read on another
connection cannot see them. Replay passes `None` because it owns no
transaction. The SQL now always selects `ticker, interval` as well, so
one row shape serves both renderings; the dict is built from the same
columns it was built from before.

Call sites: `archiver/runner.py`, `archiver/shadow.py`,
`archiver/cli.py` (connection, closed bound, dict);
`replay/runner.py` ×2 and `replay/movers.py` (`None`, half-open,
`list[Bar]`).

---

## 2026-09-19 — the append path (FINAL design §3 V2-1, §4, §9)

`upsert_bars` IS UNCHANGED, byte for byte. `git diff main -- src/cobalt/archiver/store.py`
shows **148 insertions and 0 deletions**; two tests pin the method
(`DO UPDATE SET` present, `DO NOTHING` absent, `return len(rows)`,
signature `(self, bars, *, before_commit)`). That matters because §5's
mode isolation says a night in `upsert` mode writes exactly what it
writes today, and because the RADAR POLLER calls this method — R8 keeps
the live poller untouched.

Everything added below it TAKES A CONNECTION. §4: one transaction on one
connection per target holds the stored-range read, the inserts, the
progress write, the incident writes and the accepted outcome, so a crash
between any two of them commits none of them. The offline tests prove
this with a recording fake that counts `commit`/`rollback`/`close` calls
and a fixture that makes `_connect` itself an assertion failure.

- `target_transaction()` — the context manager that opens that one
  connection (`autocommit=False`), commits on a clean exit and rolls
  back on any exception. A failed or withheld target's transaction is
  rolled back here; its failure EVIDENCE is persisted afterwards in a
  SECOND small transaction by the runner (Astra, V3-2), because evidence
  written inside the doomed transaction dies with it.
- `insert_new_bars(conn, bars) -> int` — `ON CONFLICT (ticker, interval,
  ts) DO NOTHING`. This one clause is the owner's ruling: a key already
  stored is left exactly as it is, whatever the vendor now says about
  it. **The count is the server's `rowcount`, never `len(rows)`** — a
  bar the poller committed between this transaction's range read and
  this statement is a CONFLICT, not an insert, and reporting it as
  written would break §7's identity `incoming_only = inserted +
  concurrent_conflicts`. If the driver cannot say, the run FAILS (L1).
- `_bars_in_range(conn, ticker, interval, start, end)` — the ONE range
  read, private and connection-taking (spec O-5). Returns
  `{ts: BarValues}`, already normalised to `NUMERIC(14,4)` / integer
  volume, so `reconcile.compare` decides on values rather than on
  renderings.
- `ARCHIVE_RUN_LOCK_KEY` / `try_acquire_run_lock(conn, what=…)` /
  `release_run_lock(conn)` — §9's run-level lock. ONE constant key,
  **session level, not transaction level**: a repair re-checks the quiet
  window immediately before COMMIT and rolls back when it has closed
  (§8), and `pg_try_advisory_xact_lock` would hand the lock away at that
  rollback while the command was still running. `what` turns the refusal
  into an `ArchiveLockError` for callers that cannot continue.

### Gotchas added by this change
- **The lock does not protect against the poller.** The poller does not
  take it (R8), so it serialises the archiver against ITSELF and against
  repairs. The protection on the poller side is the quiet window, and
  that rests on an ESTIMATED cycle bound — the recorded dissent (spec
  §13, O-2).
- **Cross-branch (spec O-5, L3).** `sprint-2/p4` adds
  `BarStore.bars_between()`, which opens its own connection. After both
  land there must be ONE range read: the second lander folds them into
  one method taking an optional connection. A test here asserts this
  branch adds exactly one read and that it takes a connection.
- The new `Interval` import is on its own line so the diff against main
  stays purely additive.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

Declares `SIDE = Side.SYSTEM` (ADR-0008 D2 — the side is chosen PER STORE, never per process).
`bars` is market history any trader's strategies read.

`_connect()` passes it to the factory; `ensure_schema()` asserts the two-layer schemas exist before running its own DDL, naming `cobalt db migrate` if they do not.

---

## 2026-09-17 — S2-P4: `bars_between`

`bars_between(ticker, interval, start, end)` returns `Bar` models with
`start <= ts < end`, oldest first. It is a plain read and the nightly
replay's only bar read: coverage checks, counterfactual R, and the movers
archive re-check.
