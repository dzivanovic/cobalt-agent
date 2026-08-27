# `tests/cobalt/test_archiver_report.py`

## What it does
Tests `report.py`'s header-on-create behavior and — the load-bearing
one — that the markdown table never gets broken by interleaved content
across multiple runs, including runs with failures.

## Key functions/classes (what's covered, not defined)
- `test_first_run_writes_header_then_one_row` — a fresh file gets the
  title + table header + separator + exactly one data row.
- `test_second_run_appends_without_rewriting_header` — the header
  appears exactly once across two runs; the second run's failure count
  shows up correctly in its row.
- `test_table_stays_contiguous_across_failures` — the specific
  regression this file guards against: every line from the table's
  first row onward must start with `|`, even after a run that recorded
  failures. (An earlier draft of `report.py` interleaved a bulleted
  failure-detail list between rows, which breaks markdown table
  rendering for every row appended after it — caught and removed before
  this ever shipped; the test stays as a permanent guard.)

## Data flow in/out
Writes to a `tmp_path`-backed fake `REPORT_PATH` (monkeypatched) — never
touches the real `docs/30 - Design/archiver-runs.md`.

## Config it reads
None.
