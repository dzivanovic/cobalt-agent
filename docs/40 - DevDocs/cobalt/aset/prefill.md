# `src/cobalt/aset/prefill.py`

## What it does
Fetches the last price for a ticker from Finviz Elite, for the sheet's
"tab out to fetch" prefill. **Fail-loud and secret-safe:** any failure
(bad token, network error, unparseable CSV) raises `PrefillError` — the
sheet shows FAILED, it never guesses a price — and every error message
is scrubbed so the Finviz auth token can never leak into a response or
a log line.

Reuses the old tree's `FinvizApiClient` **only** for its vault-token
resolution (`_resolve_vault_credentials`) — a deliberate, narrow,
one-directional read across the strangler boundary (old tree stays
untouched; new core is allowed to *read* from it, never the reverse).
The actual HTTP fetch targets `/export/stock` directly rather than
reusing `FinvizApiClient.get_quote`, because that method's endpoint
(`quote_export.ashx`) now 301-redirects and the old client can't be
edited (strangler rule) — see `docs/90 - References/finvizstockapi.png` for
the current endpoint shape.

## Key functions/classes
- `PrefillError(RuntimeError)` — the one error type this module raises.
- `scrub(text) -> str` — regex-redacts any `auth=<token>` substring
  (`_AUTH_RE`) an underlying library (httpx) baked into an exception
  message, replacing it with `auth=REDACTED`. Applied to every error
  string before it's raised.
- `resolve_token() -> str` — **(renamed from `_resolve_token`, Slice 2)**
  instantiates `FinvizApiClient`, calls its private
  `_resolve_vault_credentials`, wraps any failure in a scrubbed
  `PrefillError`. Made public specifically so `prefill/market.py` and
  `prefill/calendar.py` can reuse it (one-path rule — no second Finviz-
  auth implementation) instead of re-resolving the token themselves.
- `fetch_last_price(ticker) -> tuple[Decimal, str]` — normalizes the
  ticker, resolves the token, GETs `elite.finviz.com/export/stock`
  (`p=d`, daily), parses the CSV response, and returns `(price, source
  description)` from the first present column in `CLOSE_KEYS = (Close,
  close, Last, Price)`. Raises `PrefillError` at every failure point:
  empty ticker, token resolution failure, HTTP failure, empty CSV,
  unparseable or non-positive price, no matching column.

## Data flow in/out
**In:** a ticker string (from `web.py`'s `/api/prefill?ticker=`).
Reads the Finviz API token from VaultManager via `FinvizApiClient`
(`COBALT_MASTER_KEY` must be set in the environment for the vault to
unlock).
**Out:** `(Decimal price, str source)`, or a raised, scrubbed
`PrefillError`. No persistence — this is a pure fetch, the caller
decides what to do with the result.

## Config it reads
No ASET YAML config. Reads the Finviz API token from VaultManager
(`finviz.com::api_token`) via the old tree's `FinvizApiClient` and
`config.py`'s `COBALT_MASTER_KEY`/vault-unlock machinery.
