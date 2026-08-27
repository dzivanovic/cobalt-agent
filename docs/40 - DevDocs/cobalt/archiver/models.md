# `src/cobalt/archiver/models.py`

## What it does
The Bar Archiver's data contracts: the validated interval enum and the
one row shape everything else in the package moves around.

## Key functions/classes
- `Interval(str, Enum)` — `I1, I2, I5, I15, I30` only. Deliberately
  excludes `h`/`d`/`w`/`m`: hourly isn't used by any tier, and
  daily/weekly/monthly are never archived (Finviz serves 10y+ of those
  on demand — DATA-SOURCE-MEMO.md). This is the footgun-law enum: bare
  or unrecognized `p=` values silently return daily data from Finviz
  with no error, so the type system is the first line of defense.
- `Bar` — `ticker`, `interval: Interval`, `ts: datetime`, `open/high/
  low/close: Decimal`, `volume: int (>= 0)`. `extra="forbid"`.

## Data flow in/out
None — pure data models, constructed by `collector.py` and consumed by
`store.py`.

## Config it reads
None.
