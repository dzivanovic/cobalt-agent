# `src/cobalt/prefill/market.py`

## What it does
SPY/QQQ/IWM last price + change% for the morning Daily Note's market
table, via Finviz Elite's `/export/screener?v=111` (the confirmed
default view — DATA-SOURCE-MEMO 08-27 spike) with `t=` as the confirmed
direct multi-ticker override. Fails the whole call (never a partial
row) on any fetch/parse problem — the caller decides how to render
FAILED. VIX and BTC were never in `MARKET_TICKERS` — neither is a
Finviz stock/screener ticker. Slice 2.1 (2026-08-31): those two rows
are Dejan's, always blank, no "n/a (manual)" annotation anymore (the
`UNSERVABLE` dict that used to hold that text was dead code once
`daily.py` moved to per-row filling and was removed).

## Key functions/classes
- `MarketRow` — frozen dataclass: ticker, price (Decimal), change_pct (Decimal).
- `MARKET_TICKERS = ("SPY", "QQQ", "IWM")`.
- `fetch_market_table(tickers=MARKET_TICKERS) -> list[MarketRow]` — raises `PrefillFetchError`.

## Data flow in/out
**In:** Finviz Elite `/export/screener` CSV, token via
`aset.prefill.resolve_token()` (shared, one-path rule — no second
Finviz-auth implementation). **Out:** `list[MarketRow]` or a raised
`PrefillFetchError` (message scrubbed via `aset.prefill.scrub`, never
leaks the auth token).

## Config it reads
None directly — token resolution goes through `FinvizApiClient`'s
existing VaultManager machinery (see `aset/prefill.py`).

## 2026-10-10 — f4-refresh-1010
Docstring only: the SLICE 2.1 "no n/a (manual)" note on VIX/BTC is marked
superseded by the Charter (F4): they render `n/a (manual)` until a source
owns them. `fetch_market_table` is also called by `prefill refresh`, behind
the shared Finviz gate.
