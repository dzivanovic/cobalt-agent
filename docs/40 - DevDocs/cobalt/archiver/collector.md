# `src/cobalt/archiver/collector.py`

## What it does
Fetches and validates one `(ticker, interval)`'s bars from Finviz's
`/export/stock`. Fail-loud, secret-safe: any shape mismatch — wrong
columns, malformed rows, unparseable prices, or (critically) dates
lacking a time-of-day component — raises `CollectorError`. Nothing
partial or guessed is ever returned; the caller (`runner.py`) treats
any `CollectorError` as a per-ticker failure, logged and counted, never
silently skipped and never stored.

Reuses `FinvizApiClient`'s vault-backed token resolution only (same
one-directional strangler-boundary read as `aset/prefill.py`) — the old
tree stays untouched.

## Key functions/classes
- `EXPECTED_COLUMNS` — `["Date", "Open", "High", "Low", "Close",
  "Volume"]`, the confirmed shape from DATA-SOURCE-MEMO.md.
- `CollectorError(RuntimeError)` — the one error type.
- `scrub(text)` — redacts `auth=<token>` from any string before it's
  raised, logged, or returned.
- `resolve_token()` — wraps `FinvizApiClient._resolve_vault_credentials`
  with a scrubbed `CollectorError` on failure.
- `_parse_finviz_datetime(raw) -> datetime` — handles two observed
  Finviz date-string shapes: clean 12-hour (`"04:00 AM"`, from
  `i1/i2/i5`) and a quirky 24-hour-hour-with-bolted-on-suffix form
  (`"15:45 PM"`, observed on `i15/i30`). **A date with no time
  component at all is not a parsing edge case — it's the exact shape
  Finviz returns when `p=` wasn't recognized and it silently fell back
  to daily.** Since this archiver never requests daily, that shape is
  always treated as a failure, never a valid row.
- `parse_csv_response(text, ticker, interval) -> list[Bar]` — pure
  parsing/validation, no I/O. Factored out from `fetch_bars` so it's
  directly unit-testable against known-good and known-bad response
  text without a network call.
- `fetch_bars(ticker, interval, token) -> list[Bar]` — the network
  wrapper: GETs `/export/stock?t=…&p=…&auth=…`, then delegates to
  `parse_csv_response`.

## Data flow in/out
**In:** a ticker, a validated `Interval`, and a pre-resolved token (the
caller resolves it once per run, not once per request).
**Out:** a `list[Bar]`, or a raised `CollectorError`. No persistence,
no rate-limiting here — `runner.py` owns both (the gentle-rate sleep
and the `BarStore` write).

## Config it reads
None directly — reads the Finviz API token from VaultManager
(`finviz.com::api_token`) via `FinvizApiClient`, same as `aset/prefill.py`.
