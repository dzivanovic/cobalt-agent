# `src/cobalt/aset/web.py`

## What it does
The ASET sheet's surface: a single-page FastAPI app (modeled on the
`trade-reporter` reference's simple Flask pattern) that renders the
form, handles prefill/compute/fill, and re-renders the same page with a
result or FAILED banner. No templating engine — HTML is built with
f-strings and `html.escape` on every user-controlled value. No client
framework — a small inline `<script>` handles tab-out prefill, the
ticker/entry state model, the LONG/SHORT and FULL/HALF toggles, and the
live risk-budget hint.

Fail-loud is enforced end to end: any `SizingError`/`ConfigError` (or
anything else) from a POST handler renders a visible FAILED banner
instead of a blank or guessed result — nothing is ever silently
swallowed.

**State principle (iteration 3, Dejan):** the TICKER defines the
decision context. Changing the ticker = new decision = full reset.
Within one ticker, entry tracks the last fetched price until Dejan
manually edits it (`entryDirty`), and that dirty flag only resets on a
ticker change — not on every re-fetch. Because this is a server-rendered
app with a full page reload on every POST, `entryDirty` (and, since
iteration 4, the fill-linkage timestamp) is threaded through hidden form
fields (`entry_dirty`, `orig_timestamp`), not held only in JS state that
would reset on navigation.

**Iteration 4 (2026-08-28, ruled by Dejan):** the daily-stop input and
its broker-cap clamp are gone, replaced by a FULL/HALF sheet-mode
toggle (fixed dollar risk per grade, from `configs/cobalt/aset.yaml`).
"Compute & persist" (`/size`) now persists to Postgres **and** appends
to the daily note in the same action — the old separate `POST /note`
route is deleted. A new `POST /fill` route recomputes shares at an
actual fill price and appends a linked FILL UPDATE block.

**Config-completion follow-up (2026-08-28, ruled by Dejan):** the grade
dropdown now lists the **full ladder** (A+/A/B/C/D), not just A/B.
Grades outside `SheetModesConfig.enabled_grades` render as **disabled**
`<option>`s with a suffixed label ("no trade (SAW)" for C/D, "reserved"
for A+) — the native `disabled` attribute makes them structurally
unselectable via the dropdown (verified live: `curl`ing the page shows
`<option value="A+" disabled>A+ — reserved</option>` etc.), and
`compute_sizing` refuses server-side too (`enabled_grades` passed
explicitly at both call sites) in case a stale/direct POST bypasses the
dropdown. Enabling a grade is a `configs/cobalt/aset.yaml` edit only —
no code change, verified by `test_enabled_grades_is_config_driven` in
the engine test suite.

## Key functions/classes
- `app = FastAPI(...)` — `docs_url=None, redoc_url=None` (no OpenAPI UI
  for a single-purpose internal tool).
- `CSS`, `JS` — inline string constants injected into the page. `JS`
  implements: `setDir`/`setMode` (LONG/SHORT and FULL/HALF toggles, each
  driving a hidden field), `updateModeHint` (reads `window.
  SHEET_MODE_DOLLARS` + the current mode/grade to show a live "risk
  budget: $X" hint — mirrors the retired `window.BROKER_CAP` clamp
  pattern), `markEntryDirty`/`showEntryHint`/`clearForNewTicker`/
  `handleTicker`/`doFetch` (the iteration-3 ticker/entry state model,
  unchanged in iteration 4).
- `FORM_FIELDS` — the hidden-field set threaded through every POST/
  result form: `ticker, grade, direction, sheet_mode, entry, stop,
  last_price, price_source, entry_dirty, orig_timestamp`. No more
  `daily_stop`; `orig_timestamp` is new (iteration 4) — the canonical
  timestamp of the last-computed card, empty until one exists.
- `_render`, `_failed`, `_grade_options`, `_resolve_risk_dollars`,
  `_parse_input`, `_result_card` — private helpers.
  - `_GRADE_DISABLED_SUFFIX` — the label suffix per non-enabled grade
    (`Grade.A_PLUS -> "reserved"`, `Grade.C`/`Grade.D_SAW -> "no trade
    (SAW)"`), so the option text explains *why* it's greyed, not just
    that it is.
  - `_grade_options(sheet_modes_cfg, selected)` — builds the grade
    `<select>`'s options by iterating **all** of `Grade` (not just
    `enabled_grades`): enabled grades get a plain label and stay
    selectable; disabled grades get the suffixed label plus the HTML
    `disabled` attribute. Replaced the generic `_options()` helper
    (deleted — no longer used anywhere) since this needs a per-option
    `disabled` flag, not just a value/label pair.
  - `_render` — the page-builder: loads `AsetConfig` and
    `SheetModesConfig` fresh every call, builds the grade dropdown via
    `_grade_options`, injects `window.SHEET_MODE_DOLLARS` (full/half ×
    **all five grades** — harmless to include disabled ones since the
    dropdown structurally can't select them, and it means a future
    grade enable needs no JS change either) and the iteration-3
    `window.INITIAL_TICKER`/`INITIAL_ENTRY_DIRTY`, and interpolates the
    form's prior values back in (so a failed submission doesn't lose
    what was typed).
  - `_resolve_risk_dollars(sheet_modes_cfg, mode, grade)` — looks up the
    dollar figure via `sheet_modes_cfg.dollars_for`, which now resolves
    every real grade (including C/D/A+) without raising. The
    `Decimal("1")` placeholder-on-exception path only still exists for a
    genuinely invalid `grade`/`sheet_mode` string (not a valid enum
    member at all) — it lets `SizingInput` construction proceed so
    Pydantic's own field validation produces the real error, instead of
    a raw `ValueError` from this function.
  - `_parse_input(form, sheet_modes_cfg)` — builds a `SizingInput`,
    resolving `risk_dollars` via `_resolve_risk_dollars` rather than
    reading it off the form (it's derived, not user-entered).
  - `_result_card(result, form, fill=None)` — renders the sizing result
    table plus, when `fill` is passed, a second card showing the
    recomputed shares/used-risk/share-delta/distance-change and any
    structural warning. Always renders the "Actual fill $" form
    (`POST /fill`) with `FORM_FIELDS` threaded through as hidden inputs.
- `@app.get("/")` `index()` — renders the blank/prefilled form.
- `@app.get("/api/prefill")` `api_prefill(ticker)` — calls
  `prefill.fetch_last_price`, returns JSON `{ticker, price, source}` or
  a 502 `{"error": ...}`. Unchanged by iteration 4.
- `@app.post("/size")` `size(request)` — parses the form into a
  `SizingInput`, calls `compute_sizing(inp, sheet_modes_cfg.enabled_grades)`,
  persists via `AsetStore` (schema ensured first), then calls
  `daily_note.save_card` — all three steps in one action. Failure
  ordering is deliberately layered so a partial failure is never silent:
  a sizing/config error (including a disabled-grade refusal) never
  reaches persistence; a persistence failure is reported before any note
  write is attempted; a note-append failure (`DailyNoteRefused`) after a
  successful persist is reported as "Persisted ... but daily-note append
  FAILED" rather than losing the fact that the DB row exists. On full
  success, `orig_timestamp` is set into the form dict (from the
  `(path, when)` `save_card` now returns) before rendering the result
  card, so the fill form can link back to this card. Live-verified: a
  disabled grade posted directly (bypassing the dropdown) writes nothing
  to Postgres or the note and renders the "not enabled ... no trade
  (SAW)" FAILED banner.
- `@app.post("/fill")` `fill(request)` — parses the form the same way,
  **recomputes** the original sizing fresh (no re-read from
  `aset_sizings` — deterministic recompute, same pattern the old
  `/note` route used, also passing `enabled_grades`), requires a
  non-empty `orig_timestamp` (raises `SizingError` if missing —
  "compute & persist a card first"), calls `engine.compute_fill_recompute`,
  then `daily_note.save_fill_update`. No new Postgres row. Catches
  `SizingError`/`ConfigError`/`DailyNoteRefused` alongside a catch-all,
  same FAILED-banner pattern as `/size`.

## Data flow in/out
**In:** form POSTs from the browser (`ticker`, `grade`, `direction`,
`sheet_mode`, `entry`, `stop`, plus hidden `last_price`/`price_source`/
`entry_dirty`/`orig_timestamp` carried through from prior actions;
`actual_fill` additionally on `/fill`); `ticker` query param on
`/api/prefill`.
**Out:** rendered HTML (all routes that return pages), or JSON
(`/api/prefill`). Delegates all actual work: `engine.py` for math,
`prefill.py` for the Finviz fetch, `store.py` for persistence,
`daily_note.py` for the vault write.

## Config it reads
`AsetConfig` in full, via `load_config()`, and `SheetModesConfig` via
`load_sheet_modes_config()` — both called fresh on every request (no
caching), so editing `configs/dev/aset*.yaml` or
`configs/cobalt/aset.yaml` takes effect on the next page load with no
server restart.
