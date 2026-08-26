# `src/cobalt/aset/web.py`

## What it does
The ASET sheet's surface: a single-page FastAPI app (modeled on the
`trade-reporter` reference's simple Flask pattern) that renders the
form, handles prefill/compute/save, and re-renders the same page with a
result or FAILED banner. No templating engine — HTML is built with
f-strings and `html.escape` on every user-controlled value. No client
framework — a small inline `<script>` handles tab-out prefill, the
entry-field "dirty" tracking, the LONG/SHORT toggle, and the daily-stop
cap clamp.

Fail-loud is enforced at two layers: the client-side JS clamps the
daily-stop input visually, and every POST handler independently calls
`enforce_broker_cap` server-side — the browser is never trusted alone.

## Key functions/classes
- `app = FastAPI(...)` — `docs_url=None, redoc_url=None` (no OpenAPI UI
  for a single-purpose internal tool).
- `CSS`, `JS` — inline string constants injected into the page.
- `_options`, `_render`, `_failed`, `_parse_input`, `_result_card` —
  private helpers. `_render` is the page-builder: loads config fresh
  every call, computes the daily-stop prefill
  (`daily_stop_default or temp_prefill_daily_stop(account_size)`,
  clamped to `broker_hard_stop`), and interpolates the form's prior
  values back in (so a failed submission doesn't lose what was typed).
- `@app.get("/")` `index()` — renders the blank/prefilled form.
- `@app.get("/api/prefill")` `api_prefill(ticker)` — calls
  `prefill.fetch_last_price`, returns JSON `{ticker, price, source}` or
  a 502 `{"error": ...}`. This is what the JS `prefill()` function
  calls on ticker blur or "Re-fetch."
- `@app.post("/size")` `size(request)` — parses the form into a
  `SizingInput`, runs `enforce_broker_cap` then `compute_sizing`,
  persists via `AsetStore` (schema ensured first), and re-renders with
  the result card. Any `SizingError`/`ConfigError` (or anything else)
  renders a FAILED banner instead — nothing is ever silently swallowed.
- `@app.post("/note")` `note(request)` — same validation path, but
  **recomputes** the sizing fresh (no re-read from `aset_sizings`) and
  calls `daily_note.save_card` instead of persisting to Postgres again.
  Catches `DailyNoteRefused` alongside the sizing/config errors.

## Data flow in/out
**In:** form POSTs from the browser (`ticker`, `grade`, `direction`,
`daily_stop`, `entry`, `stop`, plus hidden `last_price`/`price_source`
carried through from a prior prefill); `ticker` query param on
`/api/prefill`.
**Out:** rendered HTML (all three routes that return pages), or JSON
(`/api/prefill`). Delegates all actual work: `engine.py` for math,
`prefill.py` for the Finviz fetch, `store.py` for persistence,
`daily_note.py` for the vault write.

## Config it reads
`AsetConfig` in full, via `load_config()` — called fresh on every
request (no caching), so editing `configs/dev/aset*.yaml` takes effect
on the next page load with no server restart.
