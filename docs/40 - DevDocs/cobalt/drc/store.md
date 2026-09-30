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
       `closed outside export` / `no-trade DRC`. An `opening` for a day
       whose prior trading day is recorded is refused with a
       `ValueError`, nothing written — that day starts from P's close
       (K1 fix r1, H2); `preview_stated_book` refuses the same.
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
  A not-computed day with `seed=None` IS recorded by the route (K1 fix
  r1, H3): one `day` row carrying `not_computed.pairing`, no `seed`, no
  `book_close`, so the next day's `seed_for` fails `pairing not computed`
  until D is stated and re-paired.
- `STATED_TABLE` names the table for a caller's printout.

## 2026-09-25 — DRC K2 (no-trade carry, forward re-pair, R51, resolve)
- **`record_day(pairing, import_ids, seed)`**: same signature, same
  return (rows written for `pairing.day`). It now also:
  - refuses a pairing with no trading-log id unless a current `no_trade`
    statement exists for the day; the `day` row then names `no_trade_id`
    (`[F-05]`);
  - re-pairs every LATER recorded day, in date order, when one exists.
    Each later day goes through `_repair`, its seed read from the
    previous day's in-memory close (`_Close`). All days are written in
    ONE transaction. If any later day raises, the error is
    `PairingError "<P>: not recorded — the forward re-pair of <N>
    failed: …"`, and nothing in `drc_rows` is written (the import row
    stays committed, `[F-25]`). A not-computed day stops the chain: the
    later days keep their rows and are listed in the `day` row's
    `derived.not_repaired`. The days that were re-paired are listed in
    `derived.repaired`. Both keys are written only when a later day
    exists.
- **`rebuild(day) -> list[date]`**: the one re-pair of a day from its
  STORED inputs, then forward. Its inputs:
  - the fills of the CURRENT trading-log import (a `failed` one FAILS;
    a `partial` one → `not_computed.pairing` = its stored reason), or
    the day's `no_trade` statement (the seed then becomes
    `no_trade_carry`);
  - the stored `stats_row` rows, re-matched with `missing = []`, or kept
    unchanged when `not_computed.match` was stored;
  - the seed from `_seed`, the same rule as `seed_for`.
  It returns the dates written, the rebuilt day first.
- **`seed_for` / `_seed`**: one rule, with an optional in-memory overlay.
  - A stated opening beside a recorded prior close no longer raises. The
    carried book is returned with `stated_book_id` and `stated_differs`
    (`pairing.stated_differs`, R51).
  - `_with_resolves` is the `[F-06]` reader. Two current resolves for
    one trade FAIL, naming both ids. A resolve dated D that names a held
    trade → `SeedBook.resolves`. One that names a trade an earlier export
    closed → a `superseded` outcome. Any other resolve dated D FAILS.
    A resolve dated before D whose trade is still held, and which was not
    superseded on its own day, FAILS with `rebuild <R>`.
- **`stated_difference(day)`**: the R51 line `stated book for <N>
  differed from <P>'s close: <ids>`, read from the stored `seed` row, or
  `None`.
- **`has_current_import`, `has_chain_through`**: reads the CLI uses to
  decide whether `--apply` rebuilds.
- Row additions:
  - `seed.inputs.no_trade_id` (no-trade carry);
  - `seed.derived.stated_differs` (a carried book naming a statement);
  - `trade.inputs.resolve_id` (an applied resolve);
  - `day.derived.resolves` (every outcome, when any).
  The rebuild never writes `drc_stated_books` (R51, L7).

## 2026-09-25 — DRC K2 fix r1
A resolve's key is now its trade id on any day: `record_stated_book`
refuses a second current one (naming `#id (day)`) and accepts a
restatement across days, whose rebuild starts at `effect_day(day,
supersedes)` — the earlier day (F-1). A stopped chain now writes
`derived.book_stale = {root, reason}` on each later day's own `day` row,
and `_carried` refuses a marked prior; `record_day` and `_repair` share
one no-trade seed rule (`_no_trade_seed`); a re-pair rebuilds the stats
input with its own file's missing columns and always re-matches it; a
partial import re-pairs through `trading_log.pairing_not_computed`, as
its first record did (F-2 … F-5).

## 2026-09-25 — DRC K2 fix r2
New read `stated_day(stated_id)`: the `day` of one `drc_stated_books` row,
current or superseded, or `ValueError` for an unknown id. It is the one
read of a stated row's day (L3). `effect_day` now calls it, and its result
and its raise are unchanged. The CLI's rebuild trigger calls it too, to
test the superseded row's day for a recorded chain (F-1r2).

## 2026-09-25 — DRC D2 (the input event)
Two methods, nothing else of the store moved. **`mark_event(import_id,
state, error=None)`** moves the `DrcInputsPlaced` event on a stored
`trading_log` import row (`event_state` / `event_updated_at` /
`event_error`, `0016_drc.sql:35-37`) under `SELECT … FOR UPDATE`: L18's
moves only (`EVENT_MOVES`: pending → running | failed, running → done |
failed; ANY state → `pending` is a re-fire); `failed` must name its
reason and no other state carries one; an illegal move or a non-trading-
log row is refused, nothing written. It is not session-gated: the drop
that fires it is gated at its start (`imports.place`). **`event_for(day)`**
is a READ: the event on the day's CURRENT trading-log import (`import_id`,
`state`, `updated_at`, `error`, all `None` without one) plus the stored
rows it is built from — every `drc_imports` row of the day with `current`
and its `fills` count, the `day` row, the trade ids, and the row count
per kind. The event's payload is never stored (L57).

## 2026-09-28 — DRC D2 fix r1 (the event home, the screenshot writer)
`docs/30 - Design/DRC-D2-SEAM-2026-09-25.md` §1 / §2 (R64). THE EVENT
HOME moves to `"user".drc_events` (`0019_drc_events`; `TABLES` names it):
ONE row per source — a trading-log import (`source = import`) or a
current `no_trade` statement (`source = stated_book`, the file-less
no-trade day). **`fire_event(day, *, import_id=None, stated_book_id=None)
-> int`** is the ONLY way a row reaches `pending`: exactly one source; an
import must be a stored `trading_log` of `day`, a statement the CURRENT
`no_trade` statement of `day` (`_no_trade_id`); anything else refused
naming why, nothing written; a re-fire moves the source's row back to
`pending` with its error and note path cleared. **`mark_event(event_id,
state, error=None, *, note_path=None)`** is keyed by the event id; the
moves are `EVENT_MOVES` (unchanged) and never to `pending`; `failed` names
its reason, `done` the note path the build returned. **`event_for(day)`**
keeps every key and reads the event by the three-step rule (the current
trading-log import's; else the current `no_trade` statement's; else
none), adding `event_id`, `source`, `note_path`, `stated_book_id` /
`stated_book_sha256` (with no current trading log: the day's current
`no_trade` statement, fired or not) and `seed` (the day's `seed` row
inputs, read only); the `imports` rows lose their `event_*` keys.
**`record_screenshot(day, name, data, trade_key) -> int`** is the ONE
writer of `kind = 'screenshot'` rows: refuses empty bytes, a non-PNG /
JPEG header and an empty key; `supersedes` the current screenshot row of
the same day + key; nothing overwritten or deleted. `record_import`,
`models.Kind` and `detect_set` are untouched.

## 2026-09-29 — DRC D3: `record_build` and its read
**`rows_for(day) -> list[dict]`** reads every `drc_rows` row of the day
(`kind`, `ref`, `inputs`, `derived`, `fn_version`), oldest first — the
build renders only what these hold (L57). **`record_build(day, rows) ->
int`** is the ONE writer of the build's two kinds, `build_trade` and
`build_day` (`0020_drc_build_kinds`): it replaces exactly those two kinds
for the day in one transaction and touches no K kind; a row of any other
kind is refused, nothing written. K2's `record_day` / `rebuild` delete
EVERY kind of a day they re-pair — the build rows with them — and the DRC
build re-builds them for each re-paired date (D3-2r). Both methods sit at
the class's end, so no seam line above them moved.

## Tests
`tests/cobalt/test_drc_store.py` has an offline half (the SQL, the
registry, the placement map, the one-writer grep). Its with-DB half
applies `FORWARD` inside the test's own migration-connection transaction,
which is always rolled back. It hands the store a savepoint proxy over
that connection. So the tables exist only inside the test, and no
migration is ever committed to `cobalt_dev`.
