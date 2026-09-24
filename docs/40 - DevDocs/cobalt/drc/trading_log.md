# `src/cobalt/drc/trading_log.py`

## What it does
This module parses his daily execution export, one row per fill, into
`Execution` records. It sits behind the `ExecutionSource` interface
(L9). `TradingLogSource` is today's only source.

A file reaches `TradingLogSource.parse(data, import_date, detection)`
only after `detect.detect_kind` classified it `trading_log`, complete or
`partial` (R114). Any other detection raises. The file's name and
extension are never read.

## The constants (the one copy — `detect` imports them)
- `REQUIRED` — the ten column names E1's header shows, in order: `TIME`,
  `SYMBOL`, `SIDE`, `PRICE`, `QTY`, `ROUTE`, `BROKER`, `ACCOUNT`, `TYPE`,
  `ORDER_ID`.
- `PAIRING_INPUTS` — the five pairing reads (time, symbol, side, price,
  quantity), built from the same names and never retyped.

## The date (09-23 R17 (3))
The file has no date column. Every execution's date is the `import_date`
the caller passes (the `<date>` folder, or the upload's date). The row's
`Time` (`HH:MM:SS`) is combined with that date as America/New_York
wall-clock time (`ET`). E1 proved the zone: 4 of 4 trades pair to the
second against the stats log's `EDT` times. Nothing reads a date from
the file.

## Fail-loud (L1)
Every row validates on the columns the file has. Otherwise the WHOLE
file comes back `failed`, with `line` and a reason naming the file and
the line, and with zero executions. These fail the file:
- an empty cell
- a time that is not `HH:MM:SS`
- a price that is not a positive decimal
- a quantity that is not a positive whole number
- a side outside `B` / `S` / `SS`
- a wrong cell count
- a value under the unnamed trailing column
- a blank line inside the file
- non-UTF-8 bytes, reported on the line the bad byte sits on

Trailing blank lines at end of file are not rows.

## Partial and degraded (R17 (5), L9)
- A `partial` file parses on the columns it has. An absent column's
  field is `None` on every execution.
- If any pairing input is absent, `result.not_computed["pairing"]` reads
  `not computed — missing: <columns>`.
- The result is `partial`, with `missing` set, and `reason` carrying the
  loud `PARTIAL — missing: …` flag.
- An added column parses and sets `degraded: trading_log_shape`, naming
  it. A reorder alone changes nothing.

## Accounts (R94)
The account column is read and stored per execution. It is ONE bucket:
never a gate, a split or a failure.

## Order: `chronological(executions)`
Oldest first. E1 is newest-first, so rows that share one `Time` are
taken in REVERSE file order: sort by `(time, -line)`. E1's evidence is
recorded in the build report's `## E1`. The one scale-in whose first
`Time` carries two fills at two prices has the stats log's entry price
equal to the fill on the lower line.
