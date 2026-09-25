# `src/cobalt/drc/models.py`

## What it does
The typed records of DRC D1. Every record is a frozen Pydantic model
with `extra="forbid"`, so invalid data never constructs (L1). Every time
field is a pydantic `AwareDatetime`, imported under the local name
`datetime`, so a naive time fails validation.

## The one rule: `None` means "the file does not carry this"
- A figure the file lacks is `None`, and a renderer prints it
  `NOT_GIVEN` (`"not given"`, R91).
- Nothing here defaults a figure to zero or guesses it.
- A step that could not run because an input column was absent is named
  in a `not_computed` map (R17 (5)). It is never silently skipped.

## The records
- `Kind` — `trading_log` / `stats_log`. These are the L31 names: no vendor
  name enters an enum value.
- `Outcome` — `parsed` / `partial` / `failed` / `ignored`.
- `ExecSide` — the trading log's own side codes, exactly the three E1
  shows (`B`, `S`, `SS`). Any other code fails the row, and so the
  whole file.
- `Direction`, `TradeStatus` (`closed` / `open`).
- `Execution` — one trading-log row.
  - Every field except `line` is Optional. A `partial` file leaves an
    absent column's field `None`.
  - `time` is the import date (R17 (3)) combined with the row's clock
    time as ET.
- `Leg` — one entry or exit fill.
  - One leg per execution row. Split fills are never merged.
  - A `line` of `None` with `carried=True` is a lot brought in from a
    prior day.
- `Lot`, `OpenPosition` — what a day leaves open (R67). This is the next
  day's seed. It keeps the remaining FIFO lots, so the realized P&L on
  the day a position closes uses the prices it was really opened at.
- `StatsRow` — whatever one stats-log row carries:
  - entry, exit and target
  - assumed and realized R:R
  - price and position MAE/MFE
  - best exit, gross/net, commission, fee, quantity, executions
  - `playbooks: list[str]`, every name in order (R114)

  **`stop` is never computed** (R17 (4)). It is filled only from a
  stats-log stop column read by a ruled header name, and E1 has none.
- `Trade` — one FIFO trade.
  - `entries` and `legs` (the exits).
  - `gross_pnl` is realized on this day's exits only.
  - An open trade has `held_shares > 0` and `unrealized = "not computed"`.
  - `net_pnl` and `commissions` are PROPERTIES that read the matched
    stats row's own figures. They are never computed here, because the
    trading log carries no commission column.
- `Detection`, `ImportResult` — per-file verdicts.
  - `partial_flag` is the loud text `PARTIAL — missing: <columns>`.
  - `degraded` is `<kind>_shape` when the header carries names the
    parser does not know (L9: loud, still parsed).
- `DayPairing` — one day's trades, the positions it leaves open, the
  unmatched stats rows and the steps not computed.
- `PairingError` — the whole-file failure of pairing.

## 2026-09-24 — DRC K1 (the overnight-position lane)
- **A stated position has no cost and no time** (v3 `[F-04]`).
  - The time and price of `Lot` may be `None`, and so may those of an
    entry `Leg`.
  - `OpenPosition.entry_time`, `Trade.entry_time` and `Trade.avg_entry`
    may also be `None`.
  - `OpenPosition.opened_on` may be `None` (K1 fix r1, H1): a stated
    position's open day is not stated, never the stated day (L1).
  - An EXIT `Leg` still requires both its time and its price (a
    validator).
- **`Trade.gross_pnl`** is a `Decimal` or exactly the literal
  `CARRIED_COST_NOT_STATED` (`not computed — carried cost not stated`).
  It is never `None` and never `0`.
- **`OPENING_NOT_STATED`** is `not computed — opening book not stated`.
  It is the `pairing` reason of a day with no stated book.
- **`StatedPosition`** and **`StatedResolve`** are the validated position
  shapes of an `opening` or `resolve` statement.
- **`StatedBook`** is one `drc_stated_books` row. Its `id` is `None` on a
  preview.
- **`SeedBook`** is the book a day starts from: `source` is `carried` or
  `stated`, plus `positions`, `from_day`, `from_book_sha256` (hex-64) and
  `stated_book_id`. A validator ties each source to its own link. K2
  adds `no_trade_carry`.
- `StatedKind` and `Via` are the `drc_stated_books` domains (R52:
  `drc_page` / `voice_widget` / `cli`).

## 2026-09-25 — DRC K2
- **`SeedBook.source`** gains `no_trade_carry`: a prior close carried
  through a no-trade day. It must name `from_day` and `no_trade_id`, and
  no `stated_book_id`.
- **New `SeedBook` fields**:
  - `stated_differs` (sorted trade ids);
  - `no_trade_id`;
  - `resolves` (a list of `ResolveInput`);
  - `resolve_outcomes` (a list of `ResolveOutcome`).
- **The validator**:
  - A `carried` book MAY name his statement (`stated_book_id`, R51: the
    close wins and the statement is kept as history). When it does, it
    must pass `stated_differs` explicitly, `[]` when the books are equal
    — the comparison is never left unstated (L7).
  - `stated_differs` requires `stated_book_id`.
  - A `stated` book carries no difference.
- **`ResolveInput`** (`id`, `resolve: StatedResolve`) is a stored
  resolve as a pairing input. **`ResolveOutcome`** (`resolve_id`,
  `trade_id`, `status` `applied` / `superseded`, `reason`) is what
  became of it. `DayPairing.resolves` lists the outcomes.
- **`Trade.gross_pnl`** also takes `EXIT_NOT_IN_ANY_EXPORT` (`not
  computed — exit not in any export`, v3 `[F-06]`, §4 row 11).
