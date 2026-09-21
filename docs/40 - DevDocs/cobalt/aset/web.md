# `src/cobalt/aset/web.py`

S2-P3 adds the read-only Trade Radar page and pool-refresh API beside the existing S2-P1 LIVE/SIM attestation, validation, and card-write surface. The ASET header links to `/radar`.

## S2-P3 read-only radar routes

- `GET /radar` calls `build_radar_panel(since=None, snapshot=True)` and composes the ladder-first (card ladder above the pool view, R3 2026-09-21) page with `render_radar_page()`. `?frame=phone` adds the 390/366 px preview frame.
- `GET /api/radar/pool?since=<aware ISO timestamp>` validates the required client cursor, calls the same builder in refresh mode, and returns the Pydantic pool dump plus the HTML from `render_pool()`.

These handlers do not call `_render`, `_daymode_state`, `_open_cards_section`, schema initialization, attestation, or any persistence helper. A panel build failure becomes a visible escaped FAILED page; an API input refusal is 422, and a source/build failure is a loud 503 JSON response. No POST route was added.

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
  `daily_note.save_card`, then (**Slice 2**)
  `prefill.trade_note.upsert_trade_note` — four steps in one action.
  Failure ordering is deliberately layered so a partial failure is never
  silent: a sizing/config error (including a disabled-grade refusal)
  never reaches persistence; a persistence failure is reported before
  any note write is attempted; a note-append failure
  (`DailyNoteRefused`) after a successful persist is reported as
  "Persisted ... but daily-note append FAILED" rather than losing the
  fact that the DB row exists; a trade-note write failure
  (`PrefillConfigError`/`VaultWriteError`) after a successful daily-note
  append is reported the same way ("... but trade-note write FAILED"),
  again without losing the earlier confirmations. On full success,
  `orig_timestamp` is set into the form dict (from the `(path, when)`
  `save_card` now returns) before rendering the result card, so the
  fill form can link back to this card, and the banner names the
  created/updated trade-note path. Live-verified: a disabled grade
  posted directly (bypassing the dropdown) writes nothing to Postgres,
  the daily note, or a trade note, and renders the "not enabled ... no
  trade (SAW)" FAILED banner.
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
`daily_note.py` for the daily-note vault write, and (Slice 2)
`cobalt.prefill.trade_note.upsert_trade_note` for the per-card trade
note.

## Config it reads
`AsetConfig` in full, via `load_config()`, and `SheetModesConfig` via
`load_sheet_modes_config()` — both called fresh on every request (no
caching), so editing `configs/dev/aset*.yaml` or
`configs/cobalt/aset.yaml` takes effect on the next page load with no
server restart. Also (Slice 2) `configs/cobalt/prefill.yaml` via
`cobalt.prefill.config.load_prefill_paths()`, for the trade-note step.

---

## S1-P2 change (2026-09-04) — F6 banner, F7 controls

### The FULL/HALF toggle is gone
The sheet mode is **set by the day mode in force**, not chosen
("risk set everywhere except the `.htk`", Charter M4). It renders as a
read-only line; changing it means deciding or overruling the day mode.

### The day-mode banner
`_daymode_state()` / `_daymode_banner()` render the stage, the mode in
force, the sheet it sizes from, the keys the rung permits, and the
`.htk` match result — using **the same `assert_sheet_matches` call the
write path makes**, so the banner cannot say "matched" while `/size`
refuses. A config or database failure renders a loud banner rather than
a 500 (a sheet that will not paint is a sheet he cannot trade beside),
and because every write re-checks, a degraded banner can never let a
card through.

An attestation `<select>` lists the real DAS filenames and posts to
`/attest`.

### `POST /size` — two F6 refusals, both before any write
The day mode is resolved *before* parsing (the parse needs the sheet),
but the **refusals run after `compute_sizing`** so a typo'd stop still
reports as a typo'd stop rather than hiding behind a hotkey complaint.
Nothing is persisted at that point, so a refusal leaves no row and no
note to unwind. Both refusals are logged.

### `POST /card/{id}/move` and `/card/{id}/stop`
Every button in the open-cards list is rendered **from `cards.ALLOWED`**,
so no illegal button can be drawn and no legal edge can be missing.
`MISSED` and `DISARM` prompt for their required reason client-side
(mirroring `store._assert_reason`) rather than posting an empty field
and reading a refusal.

`/card/{id}/stop` writes **no transition row** (decision 11) — the edit
rides in the next transition's evidence. The amber `YOURS` badge shows
in `WATCH`/`FILLED`; every other state renders the 🔒 lock and says why.

### Radar card taps (S2-P2 STEP-6) — JSON routes for the panel's fetch POSTs
Every refusal is a named 4xx (`{"status": "REFUSED", "reason"}`), logged. All routes check the dev-entry opt-in (403) and `assert_writable` first. The row locks and the ARM invariant live in `CardStore`, so the sheet's `/card/{id}/move` gets them too.

- `POST /radar/card/{id}/key` with `grade=A+|A|B|C|pass`:
  - `pass` is WATCH → PASSED, actor you.
  - A key resolves today's rung (`_daymode_state`; unresolved → 409) and keeps the F6 `.htk` mismatch refusal unchanged (`assert_sheet_matches` → 409).
  - It sizes through `engine.size_at_key` on the card's LIVE entry/stop, at `sheet_for(mode)` dollars and `enabled_grades_for(mode)`. Nothing enabled below → 409, no write. Otherwise `CardStore.tap_key` (a non-WATCH card → 409).
  - Then ONE daily-note card block via `save_card(cfg, result, when=card.created_at)`: the card's stable unit, so a re-tap updates that block and no scan ever writes the note. A note refusal returns 500 with what was persisted.
- `POST /radar/card/{id}/dot/{factor}` with `grade=1..10` (else 422) calls `CardStore.tap_dot`, with bands from `CardSettingsReader().current()` (read per request) and today's enabled grades.
- `POST /radar/card/{id}/promote` and `/release` call `CardStore.set_promoted`.

### S2-P2 chunk C (STEP-8) — the panel is wired; the routes are unchanged
`web.py` itself did not change in chunk C. `GET /radar` and `GET /api/radar/pool` still call `build_radar_panel` and nothing else; the builder now also reads today's radar cards from `"user".radar_cards_v` and renders the key row, the dot tap strips and promote/release, whose clicks are `fetch` POSTs to the four `/radar/card/{id}/…` routes above. The S2-P3 line "No POST route was added" is superseded: the explicit allowlist test (`test_post_routes_are_exactly_the_explicit_allowlist`) now pins every POST path the app serves — `/size`, `/fill`, `/attest`, `/card/{card_id}/move`, `/card/{card_id}/stop` and the four radar card routes — and keeps `/`, `/radar`, `/api/radar/pool`, `/api/health`, `/api/prefill` GET-only. Both radar GETs are covered by fail-on-call sentinels for `_render`, `_daymode_state`, `_open_cards_section`, `_read_back_note_attestation`, `_write_daymode_note` and every store's `ensure_schema`. The panel resolves today's rung READ-ONLY (`DayModeStore.for_date` + `decided_or_stage1`), never through `_daymode_state`, which can attest a note.

---

## 2026-09-17 — S2-P4: "pick not recorded" banner

`_pick_banner(card_id, filled)` returns the red FAILED-idiom banner when
`filled.pick_recorded` is False, and an empty string otherwise. The banner
names the error, says the fill stands, and points to `cobalt cards picks`.
Both fill routes **append** it after their unchanged success banner:
- `POST /fill` (the actual-fill form, via `AsetStore.mark_filled`)
- `POST /card/{id}/move` with `to=FILLED` (via `CardStore.fill`; reads
  `transition_ids` from the result)

Tests: `test_aset_web.TestPickNotRecordedBanner`.
