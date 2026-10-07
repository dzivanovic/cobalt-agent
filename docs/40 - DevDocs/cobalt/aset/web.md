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

---

## 2026-09-23 — voice V1: `set_card_stop` extracted (FINAL [F-06])

The body of `POST /card/{id}/stop` moved, unchanged, into
`cobalt.aset.card_stop.set_card_stop(card_id, to_stop)` — the ONE card-stop
function the voice act also calls (L3). The route now calls it and renders
exactly as before: the success banner from the returned `StopEdit`
(`from_stop` → `to_stop`), and the same `_failed(...)` banners for
`CardStateError`, `SessionBlocked`, `DevEntryRefused`, `InvalidOperation`
and anything else. `_check_entry_allowed` stays HERE; `card_stop.py`
imports it at call time. Pin: `tests/cobalt/test_voice_card_stop.py`
(five route outputs captured on the base, byte-identical after).

### Voice V1 wiring
- `app.include_router(voice_web.router)` — the `/voice/*` routes
  (`voice/web.md`). The POST allowlist test now names `/voice/turn`,
  `/voice/confirm`, `/voice/cancel`.
- `app.add_event_handler("startup", voice_web.voice_startup)` (and the
  matching shutdown): before the first request, the voice scratch-dir lock
  and side B's start sweep; a lock held by another process FAILS the ASET
  start loud (X-X22 measured an orphaned child outliving its job).
- The widget partial: `_render` places `voice_web.widget_html()` before
  `</body>` on the sheet; `GET /radar` places the same partial into the
  panel's page (after the panel renders, touching no sheet helper — the
  `/radar` sentinels still hold).

---

## 2026-09-25 — DRC D4-4: the settings change line (R96 / R102)

His daily stop and dollars per grade are changed HERE, from the sheet,
into the central settings (`"user".trader_settings`).

- `_settings_daily_form()` is appended by `_daymode_banner` right after the
  attestation form (both the resolved and the UNRESOLVED banner). It reads
  the current values through `settings.drc.daily_risk_values()` — the one
  reader — and renders one input per daily-stop key and per sheet × grade
  (`aset.sheet_modes.<sheet>.<A_plus|A|B|C|D>`). It never raises: an
  unreadable setting renders a FAILED block.
- `POST /settings/daily` → `settings.drc.propose_daily_change(form)` → the
  per-key diff (old → new), the payload's sha256, and an Apply form that
  posts the same inputs plus that hash. Writes nothing. A bad field
  (non-number, ≤ 0, a blank grade, a non-zero D) is refused naming it.
- `POST /settings/daily/apply` rebuilds the proposal against what is stored
  NOW, refuses if its sha256 is not the reviewed one, then calls
  `settings.cli.apply_settings` — the same function `cobalt settings load
  --apply` uses — with `source="aset.change_line@sha256:<hash>"`,
  `actor="aset.settings"`. Inside `market_reset` it is refused with the
  guard's reason and "Nothing written." `Settings saved` is shown only after
  `apply_settings` returned, i.e. after the read-back equalled the payload.
- THE SEAM WITH D2 (L72): this route block sits directly after `/attest`;
  D2's `/drc` block goes at the end of the file; they share no helper.

Tests: `tests/cobalt/test_drc_settings.py` (offline, constructed store),
`tests/cobalt/test_drc_settings_db.py` (`cobalt_dev`, rollback).

---

## 2026-09-25 — DRC D2-4: the `/drc` import page

The block at the END of the file (THE SEAM, L72: it shares nothing with
D4's block after `/attest`; its own imports — `date` as `_drc_date`,
`File` / `Form` / `UploadFile`, `cobalt.drc.imports` as `drc_imports`,
`drc_page` — sit inside it). The routes own no side effect (L40):
- `GET /drc?date=YYYY-MM-DD` (default today ET) → `drc_imports.day_view`
  → `drc_page.render`. Writes nothing. A date that is not a date → the
  FAILED page.
- `POST /drc/import` (multipart: `date`, `files` — one or more, any name,
  NO kind field — optional `trade_key`) → `drc_imports.place`.
- `POST /drc/no-trade` (`date`) → `drc_imports.no_trade`.
- `POST /drc/scan` (`date`) → `drc_imports.scan_folder` (a non-date is
  the FAILED page; nothing read).
- `_drc_render(day, result)` reads the day's cards (`AsetStore.for_date`,
  read only; a failed read is a FAILED line) for the "cards with no
  trade" count. Any exception is the FAILED page, never a blank.

Tests: `tests/cobalt/test_drc_imports.py` (TestClient, offline double),
`tests/cobalt/test_drc_imports_db.py` (TestClient, `cobalt_dev`
rollback), `tests/cobalt/test_drc_web_seam.py` (the seam, by `ast`).

---

## 2026-09-28 — S3 exits C3: the trade taps (v3 §2 / §3 / §5; R67, R38)

ONE block, directly after `POST /radar/card/{card_id}/release` (S-WEB: never
after `/attest`, never a second block at the file's end). A route owns no side
effect (L40): it parses the form and calls C1 / C2's writers and the stores'
reads — nothing else.

| route | form fields | calls | notes |
|---|---|---|---|
| `POST /radar/card/{id}/triggered` | — | `CardStore.transition(TRIGGERED, actor=YOU)` | ARMED → TRIGGERED is his tap until S4 (O7 A). Evidence `{via, last_price, last_price_at}`: `last_price` from the card's `radar_cards_v` row; `last_price_at` is `null` — no column stores the bar time (X6-R). |
| `POST /radar/card/{id}/fill` | `price`, `shares`, `prefill` | `AsetStore.mark_filled(…, price_asof=None, source=<source>)` — THE fill (S-FILL) | untouched prefill → `last_poll` / `estimated`; a typed or edited price → `typed` / `confirmed`; no price → `mark_filled`'s own refusal (422), nothing written. |
| `POST /radar/card/{id}/pass` | — | `CardStore.transition(PASSED, actor=YOU)` | |
| `POST /radar/card/{id}/exit` | `preset`, `shares` (typed), `price`, `prefill`, `running_before`, `confirm` | `legs.record_exit` | `running_before` = the count the screen rendered (R67: C2 refuses a stale / duplicate tap). ½ ⅓ typed follow the prefill rule; **flat** commits `confirmed` only with `confirm=1` (its price then `typed`), otherwise `estimated` — listed for correction. No price / no `running_before` → a 422 argument refusal, nothing written. |
| `POST /radar/card/{id}/held` | `held` | `legs.record_held` | HOLDING X (S-HELD). |
| `POST /radar/card/{id}/correct` | `leg_id`, `price`, `shares` | `legs.record_correction` | a typed price names `price_source='typed'` → `confirmed` (the ✓ on an estimated leg). |
| `POST /radar/card/{id}/stop` | `to_stop` | `card_stop.set_card_stop` → `record_stop_edit(kind='edit')` | the one card-stop function (L3). |
| `POST /radar/card/{id}/stop/reset` | — | `CardStore.record_stop_edit(kind='reset', to_stop=structural_stop)` | ↺ (R38). `structural_stop` from the card's `radar_cards_v` row; a card with none (manual) posts its current stop and the writer refuses by name (O19 A). |

`_card_tap(card_id, request, gate, work)` runs every tap: `source` (`panel` —
the default — or `sheet`), the dev-entry guard, the session gate
(`assert_writable(gate)`, FIRST, as the other radar taps), then `work`.
Refusals, verbatim: `DevEntryRefused` 403 · `_TapInputRefused` /
`SizingError` / `InvalidOperation` 422 · `CardStateError` (incl.
`LegRefused`) / `IllegalTransition` / `SessionBlocked` 409 · `ConfigError`
503. `_tap_reply`: the panel gets JSON (`{"status": "ok", …}` /
`_refused`'s `{"status": "REFUSED", "reason": …}`); `source=sheet` gets the
sheet page (`_render`) with the saved / FAILED banner and the same status.

Helpers (new, in the block): `S3_TAP_SOURCES`, `_TapInputRefused`,
`_tap_price`, `_tap_int`, `_tap_price_source`, `_tap_board_row`,
`_tap_reply`, `_card_tap`, `_sheet_in_trade`.

**C3-4 — the manual card on the sheet.** X-M: `/radar` reads
`radar_cards_v`, which is `origin = 'radar'`, so a FILLED manual card is not
on the panel. `_open_cards_section` now appends `_sheet_in_trade(card)` after
each row: for a FILLED manual card, `radar_panel.render_in_trade(…,
structural_stop=None, last=None, source="sheet")` — the SAME forms posting to
the SAME routes (plain `<form method="post">` here; the sheet has no fetch
script). No ↺ (no Cobalt stop; the row's own "↺ reset = re-enter the card
stop" wording stays, v3 §5); price fields empty (no last price is read here).
`_card_controls` is unchanged — its FILLED row still carries the edge-table
CLOSE button, which posts to C2 fix r1's F1 refusal.

Tests: `tests/cobalt/test_s3_c3_panel_offline.py` (routes through TestClient
with recorders, refusals verbatim, `market_reset`, the S-WEB seam),
`tests/cobalt/test_s3_c3_panel_db.py` (end to end on `cobalt_dev`, inside the
suite transaction with `0021` applied there). The POST allowlist in
`test_radar_panel_cards.py` names the eight routes.

## 2026-09-29 — S3 exits C3 fix r1
- F2 (2026-09-29): `radar_card_correct` reads `legs.read_position(card_id)` (rolled back) before `record_correction`; a `leg_id` that is not one of the URL card's current legs → 422 `REFUSED card <id>: leg <leg> is not a current leg of card <id> — reload the card. Nothing written.`
- F3 (2026-09-29): `_sheet_closed_estimated` (beside `_sheet_in_trade`) lists, below the live cards and even when none is live, each MANUAL card `filled_with_picks(<today ET>)` returns CLOSED — its `estimated` legs only, through `radar_panel.render_estimated_legs`, each `✓ correct` posting `/radar/card/<id>/correct` with `source=sheet`; a failed read says `FAILED · position unreadable: …` on that card. Window: cards filled today (ET).
- F4 (2026-09-29): `_sheet_in_trade`'s failed read renders the `_failed(…)` line AND `radar_panel.render_stop_block(…, structural_stop=None, owner=None, source="sheet")` — his stop, `Cobalt stop NULL — no Cobalt stop`, no ↺.

## 2026-09-29 — S3 exits C4: the note calls (F22, v3 §7) and C4-06

Every note call runs AFTER the DB writer returned (its transaction committed), in the same request, and never inside it:
- `/size` (O4 A): passes the card's values (`id`, `ticker`, `direction`, `stop`) and the planned entry to the one writer `upsert_trade_note`; the sizing note is unchanged.
- `/fill` (manual) and `POST /radar/card/{id}/fill`: `_fill_note(card_id)` → `prefill.trade_note.write_card_note`. It writes the note at the FILLED transition's time, `leg-0`, and `aset_sizings.trade_note_path`.
  - On ANY failure the card stays FILLED, `trade_note_path` is NULL, and the page shows `FILLED — trade note NOT written: <reason> · trade_note_path NULL · retry: cobalt cards trade-note <id>`: a `warn` div on the sheet; the panel's `notice`, first.
  - The panel payload carries `trade_note_path`. A second card with the same ticker in the same second is refused (X16), never merged.
- `/radar/card/{id}/exit`, `/held`, `/correct` (panel and sheet alike): `_leg_note(card_id, leg_id, closed=…)` → `write_leg_unit`. It writes the unit `leg-<seq>` of the leg the writer returned; a correction rewrites the same unit, and a held count rewrites `leg-0`.
  - `trade_note_path` NULL, its file absent, or any failure → the notice (panel) / banner (sheet) `leg saved, note unit NOT written: <reason> · retry: cobalt cards trade-note <id>`. Nothing is written in the vault.
  - A commit that CLOSED the card also fills his blank exit keys.
- Refusals return before the writer, as before: nothing committed, nothing to note.
- C4-06: `_tap_price` (the one tap-price parser) refuses a parsed price that is not finite or not `> 0` (the `legs.price` rule `CHECK (price > 0)`): `REFUSED: <what> <raw!r> is not a positive price. Nothing written.` → 422 through `_card_tap`, before any writer. Before this, `/exit price=NaN` → 200 and a NaN leg was stored, and `/correct price=-1` → 500.
- Tests: `tests/cobalt/test_s3_c4_trade_note_db.py`, and the `/size` call in `tests/cobalt/test_s3_c4_trade_note_offline.py`.

## 2026-09-30 — f15-p1
`POST /radar/card/{id}/dot/{factor}` passes `settings=` (the `CardSettings` it reads) to `CardStore.tap_dot` instead of `bands=settings.proposed_key` (F15 `[F-05]`); the store writes the tap's prediction record with that settings' `sha256()`.

## 2026-10-01 — aset-interim-close
His R13. (S2) `_render` draws the open-cards block (`_open_cards_section`) BELOW the `/size` form, now `id="sizeForm"`, on every response that renders `/`; `{banner}` and `{result}` stay above it. (S3) `POST /card/{id}/move` with `to=CLOSED` calls `_sheet_close_at_entry`: a FILLED card with shares running gets ONE flat exit leg through `legs.record_exit`, at the entry leg's price and with the entry leg's `price_source`, `flag='estimated'` and `source='sheet'`. The writer's `_close_if_zero` writes FILLED -> CLOSED; the route never writes CLOSED itself. A card that is not FILLED, has nothing running or has no entry leg is refused by name with nothing written. (S4) In the page script, Enter in a sizing field moves to the next field and never submits the form, and `clearForNewCard` scrolls by what the form moved, so emptying `#banner` / `#resultCard` above it leaves the form where it was. Tests: `TestNoCardAboveTheForm`, `TestSheetCloseAtEntry`, `TestTheFormStaysUnderHim` in `tests/cobalt/test_aset_web.py`, and `test_the_move_route_closes_only_through_the_zero_running_leg` in `tests/cobalt/test_legs_c2_offline.py`.

## 2026-10-01 — aset-interim-close check
The CLOSE banner says where the estimated leg is listed for correction only when that is true (`_sheet_listing`). It says "listed for correction under the form" for a MANUAL card whose FILLED transition is today, which is the set `_sheet_closed_estimated` lists through the same `filled_with_picks(_today_et())` read. Any other card gets "not listed on this sheet". A failed read is said in the banner and never raised, because the leg is already saved. Tests: `TestSheetCloseBannerSaysWhereTheLegIsListed`. `TestTheFormStaysUnderHim::test_the_ticker_reset_keeps_the_form_where_it_was` now pins the delta's sign (new top − old top) and that it is measured after both boxes are emptied. `test_sheet_close_evidence_is_via_aset_sheet` is `xfail(strict=True)`: the transition's evidence `via=aset.sheet` needs `cards/legs.py`, which the card fences off.

## 2026-10-07 — radar-arm-disarm
R627: two radar taps, appended after `/radar/card/{id}/stop/reset`, both through `_card_tap` → `CardStore.transition` with `actor=you`. `POST /radar/card/{id}/arm` moves WATCH → ARMED (`evidence via=<source>.arm`); the route checks nothing, so an unsized card, a non-WATCH card (a second ARM tap included: `ARMED -> ARMED is not a legal card transition`) and market reset are the store's refusals, each shown verbatim as 409, nothing written. `POST /radar/card/{id}/disarm` moves ARMED → WATCH with the posted free-text `reason` (stripped; over 80 characters → 422 `REFUSED: a DISARM reason is at most 80 characters, got <n>. Nothing written.`); an empty reason is the store's `_assert_reason` refusal (409). The sheet's `/card/{id}/move` and `_card_controls` are unchanged. Tests: `tests/cobalt/test_s3_c3_panel_offline.py` (`GatedCards`, the ARM / DISARM tests, market reset, route order).
