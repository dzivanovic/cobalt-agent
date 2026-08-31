# `src/cobalt/prefill/calendar.py`

## What it does
Today's economic + earnings calendar rows for the morning Daily Note,
via Finviz Elite's `/export/calendar/{economic|earnings}?dateFrom=<date>`
(DATA-SOURCE-MEMO 08-27 spike: CONFIRMED, a narrow rolling window — the
response spans several days beyond `dateFrom`, so this module filters
down to exactly the requested date). Columns are quoted verbatim from a
live probe (2026-08-31) since the memo only recorded counts, not names.
No events on a date is a legitimate empty result, not a failure — only
a fetch/parse problem raises.

## Key functions/classes
- `EconomicEvent` — event, time, impact, expected, prior.
- `EarningsEvent` — ticker, company, time.
- `fetch_economic_events(for_date) -> list[EconomicEvent]`, sorted by time.
- `fetch_earnings_events(for_date) -> list[EarningsEvent]`, sorted by time.

## Data flow in/out
**In:** Finviz Elite `/export/calendar/*` CSV, token via
`aset.prefill.resolve_token()`. **Out:** sorted event lists, or a raised
`PrefillFetchError` (scrubbed).

## Config it reads
None directly.
