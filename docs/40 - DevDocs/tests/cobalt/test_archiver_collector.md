# `tests/cobalt/test_archiver_collector.py`

## What it does
Tests `collector.py`'s datetime parsing and CSV shape validation —
pure-function tests, no network. Response shapes are drawn directly
from DATA-SOURCE-MEMO.md's fetched samples, including the two
real-world date-format quirks and the daily-fallback failure shape.

## Key functions/classes (what's covered, not defined)
- `_parse_finviz_datetime` — clean 12-hour form; the observed 24-hour-
  plus-bolted-on-suffix quirk (`"15:45 PM"`); a bare date with no time
  component (the daily-fallback failure — asserted to raise, not to
  silently parse as midnight or similar); a genuinely unparseable string.
- `parse_csv_response` — a valid 2-row intraday response parses
  correctly end to end (columns, ticker, interval, volume, close all
  checked); the **exact** daily-fallback shape (10 years of plain
  `MM/DD/YYYY` dates, mirroring what a bare/unrecognized `p=` actually
  returns) is rejected, not silently accepted; wrong column set, empty
  response, header-only response, wrong row length, and an unparseable
  price field are all rejected with a specific, matched error message.

## Data flow in/out
None — everything is constructed CSV text in memory, no I/O.

## Config it reads
None.
