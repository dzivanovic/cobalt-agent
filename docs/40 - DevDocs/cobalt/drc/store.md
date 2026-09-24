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
    `failed_line` the failing line, and `degraded` the shape flag
    followed by the added column names (`trading_log_shape: Added`).
  - `supersedes` points at the same day's latest file of that kind, so
    nothing is ever overwritten.
  - Unless the file failed, one `drc_fills` row is written per execution.
    A failed file stores zero fills. It is one transaction.
  - An `ignored` file, or one with no kind, is refused: it is listed,
    never stored.
- **`record_day(pairing, import_ids)`** — replaces the day's `drc_rows`
  in one transaction. It writes one row each for:
  - every trade (`ref` = `trade_id`)
  - every open position (the next day's seed, R67), storing the same
    `inputs` as its trade row
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
`pairing.check_contiguity` against every earlier `day` row. If the prior
trading day's `day` row says pairing was not computed, it raises
`PairingError`: that day's open positions are unknown. Only then
does it return the prior trading day's `open_position` rows as
`OpenPosition`s. The very first import returns `[]`. A broken chain
raises `PairingError`: the position is never assumed flat, and a phantom
is never carried.

## 2026-09-24 — DRC K1 (book records)
- **`record_stated_book(day, kind, positions, *, via, turn_id,
  readback_sha256, supersedes, expected_sha256, now)`** is THE one
  writer of `drc_stated_books` (L3, L40). Every caller uses it: the
  page, the widget and the CLI. It runs in this order:
  1. `assert_writable` runs first, so every caller is refused inside
     `market_reset` (`[F-01]`, X6).
  2. The positions are validated by kind: `opening` =
     `StatedPosition`s, one symbol at most once; `resolve` = exactly one
     `StatedResolve`; `no_trade` = `[]`.
  3. The `via` rules are checked: `turn_id` and `readback_sha256` are
     BOTH given for `voice_widget`, and neither is given for any other
     caller.
  4. `book_sha256` is taken over the canonical rows (an `opening` is
     sorted by symbol). A different `expected_sha256` is refused before
     any write.
  5. Under `LOCK TABLE … SHARE ROW EXCLUSIVE`:
     - `reason` is derived: `first import` / `chain broken at <P>` /
       `closed outside export` / `no-trade DRC`.
     - A current row of the same day and kind (and, for a resolve, the
       same trade_id) is refused unless `supersedes` names it.
     - A `supersedes` that names no single current row is refused.
     - Then one INSERT.
  A `resolve` or `no_trade` row is stored only; its effect is K2's.
- **`preview_stated_book(…)`** returns the same row, without its id. It
  runs no gate and makes no write.
- **`seed_for(day)`** now returns `Optional[SeedBook]`. Let P be the
  prior trading day:
  - P recorded and not computed → FAIL.
  - P recorded with no `book_close` → FAIL naming `rebuild <P>`.
  - The recomputed hash ≠ the stored hash → FAIL.
  - P recorded and a current `opening` row for the day → FAIL. This is
    K2's R51 rebuild.
  - P recorded otherwise → carried.
  - P not recorded, with a statement → stated.
  - P not recorded, no statement, an earlier day recorded → the
    contiguity FAIL.
  - Nothing at all → `None`.
  Two current openings FAIL, naming both ids. So does a current resolve
  of a returned `trade_id` (until K2).
- **`record_day(pairing, import_ids, seed)`** — `seed` is REQUIRED, and a
  computed pairing with `seed=None` is refused. It writes:
  - `seed` / `book` (inputs `source`, `from_day`, `from_book_sha256`,
    `stated_book_id`; derived `count`, `trade_ids`);
  - `book_close` / `book` on every computed day (derived `count`,
    `trade_ids`, `book_sha256`; inputs `trading_log_import_id`,
    `seed_ref`);
  - `inputs.carried_from` on a carried trade: `{day, trade_id,
    from_book_sha256}` or `{stated_book_id}`;
  - `stated_book_id` on the `day` row when the book was stated.
- `STATED_TABLE` names the table for a caller's printout.

## Tests
`tests/cobalt/test_drc_store.py` has an offline half (the SQL, the
registry, the placement map, the one-writer grep). Its with-DB half
applies `FORWARD` inside the test's own migration-connection transaction,
which is always rolled back. It hands the store a savepoint proxy over
that connection. So the tables exist only inside the test, and no
migration is ever committed to `cobalt_dev`.
