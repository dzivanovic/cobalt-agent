# `src/cobalt/drc/build.py`

## What it does
The DRC build (DRC D3). `run_drc_build(event)` is the ONE entry D2 registered: `imports._run_build` calls it after the day's `day` row is committed (`record_day` on a file day, `rebuild` on a file-less no-trade day). It returns the note path, never an empty one (the seam's RETURN CONTRACT, F-10). It writes NO event state: `pending` / `running` / `done` / `failed` are D2's, around the call.

```
run_drc_build(event, *, deps=None) -> Path       the event's day, then every re-paired date
plan_note(day, *, deps, event, check) -> BuildPlan   rows + units, computed and rendered; nothing written
write_note(plan, *, deps) -> Path                create_if_absent + every unit upserted
build_date(day, *, deps, event, check) -> Path   plan → record_build → write_note
event_of(day, store)                             D2's event for a stored day (imports._event)
default_deps(vault_root=None, **over)            the real readers; tests pass BuildDeps
```

## The order, one date
1. **The first check** (D3-2): a `trades` event needs the day's current placed trading log AND stats log; a `no_trade` event from a statement needs `event.stated_book_id` == the day row's `inputs.no_trade_id`; a zero-execution file day needs its current trading log; every event needs the day row. Anything else raises `BuildError` and writes nothing.
2. **His template** (`drc.template`): only `{{date:YYYY-MM-DD}}` replaced; any other `{{` fails naming the line — before anything is written.
3. **The rows** (L57): one `build_trade` per stored trade (`ref` = trade id) and one `build_day` (`ref = 'build'`), each with `inputs` (the card snapshot `[F-19]`, the stats row, the window, the strategy titles read, the screenshot), `derived`, and `fn_version = drc.build/1`. Stored by `DrcStore.record_build`, which replaces only those two kinds.
4. **The note**: `create_if_absent` from the rendered template, then EVERY unit upserted (never the old create-then-return, L1). His voice units are created once (`skip_if` = the unit's open marker is in the note) and never rewritten (R99).
5. **The re-paired dates** (D3-2r, v3 `[F-03]`): for each date in the event day's `day.derived.repaired`, in date order, the SAME `build_date` (no first check; the day row must exist). A failure raises `BuildError: re-paired <date>: note <path> failed — <Type>: <message> · not rebuilt: <later dates>` — D2 lands the event `failed` with that text; the database stays as K2 committed it. A date in `derived.not_repaired` is not rebuilt; the event day's summary names it.

## What it reads (and never computes)
It pairs NOTHING: no `build_day`, `pair_day` or `seed_for` (`[F-17]` seam (5)). It renders the stored `trade` rows (a Trade's own figures and its matched stats row) and the `day` row (`not_computed`, `repaired`, `not_repaired`). A day with `not_computed.pairing` renders `pairing <the stored reason>` and every trade unit `not computed — <reason>`, never "no trades" (L1).
Beside the rows (`BuildDeps`): the day's cards (`AsetStore.for_date` / `counts_for_date`), D4's readers (`load_drc_settings` for the card window and `windows.*`; `daily_risk_values` for the daily stop), the rules checkboxes (`regenerate_rules_config`, inside the resident — F41), the daily note's four premarket keys (`Sleep:`, `Readiness:`, `RHR:`, `1% goal:`, R102 O11), the strategies folder (`drc.playbooks`), and the 21:10 replay row (`cobalt_jobs.last_result` of `com.cobalt.replay`).

## The figures it stores
- **Card match**: the nearest card at or before the first fill, same ticker and direction, within `limits.card_match_window_minutes`; the window unset → `card: not matched (window not given)` on every trade — loud, never a guessed window (X12's second half renders instead of failing; the build report's ESCALATE).
- **Risk** (B24 / A9 without the engine): planned = the card's risk budget; actual = |avg entry − card stop| × shares; overrun %; the daily stop for the ONE sheet the matched cards used, with the distance on gross P&L — `not given` when unset, `not computed` when the sheet is unknown.
- **Summary**: `PARTIAL — missing: <columns> · <kind> file <name>` first (R17 (5)); gross AND net P&L (R103 O21); W/L with the closed count; cards written / taken; screenshots bound / trades; `unmapped playbooks: <n>`. No rules line (R101). `miss line: pending (replay inputs not stored)` when the 21:10 run has not stored this date's line inputs.
- **Per trade** (B-rows the data fills): entries, exits and hold, P&L gross / net / commission, legs, card + fill, risk, planned R (stats log) + realized R `not computed (D5)`, target / MAE / MFE / best exit, ONE `stop:` line (the stats row's stop or `not given` — R17 (4), never computed), the window (B27), the seat (B28), losses before (B29), flags (card after fill, risk overrun), `carried from:`, `playbooks:` (every name in order, R114 / R116), the chart embed (B13). A value fed by a column a PARTIAL file lacks → `not computed — missing: <column>`.

## The 21:10 line (D3-3)
When the replay row is for this date and says `pending (no DRC)`, the build renders the line from the stored `line_inputs` (`replay.line.render_stored`) and writes it with `write_miss_line` under the replay's writer identity (`replay.nightly`), after `drc-rules`. When the row says the line was written, the build writes no second one.

## What it never does
No event state, no pairing, no statement, no leg write (D5), no `open_positions` unit (K3), no engine unit or rules line (R101), no `Grade:` / `Goal:` line (`[F-23]`), no daily-note write, no second template, no Jinja.

## 2026-09-29 — DRC D3 fix r1
F-3: the trade block's `stop:` line renders `_Stats.text("stop")`, like every other stats-fed value. So a trade left unmatched because a PARTIAL stats file lacks a match column reads `stop: not computed — missing: <columns>`, not `not given`. A matched row with no stop still reads `not given`, and a stop the row holds renders as-is (R17 (4)). F-4: the `facts` unit is added with `units.RISK_FACTS_PLACEMENT`, as the unit of its own section `drc-risk-facts` (see `units.md`); the unit order is unchanged.

## 2026-10-04 — DRC K3
`plan_note` computes ONE list, `build_day.derived["open_positions"]`, from the day's stored `book_close` / `open_position` / `seed` / `trade` rows (`_open_book`; inputs named in `build_day.inputs["open_positions"]`). Each entry holds the trade id, symbol, direction, held shares, the average cost of the held lots (`pairing._avg`, `None` when a lot has no price), `opened_on`, `days_held`, `new today` / `continuing open position`, `carried from` and `last execution`. `days_held` counts trading days through the one calendar; when the calendar does not cover the span it reads `not computed — <the calendar's reason>`. `open_overnight` is that list's length. A day with pairing not computed, a `book_stale` day, or a computed day with no `book_close` row has no list and one loud state line. The `drc-trades/open_positions` unit (before `reconcile`), the summary's `open overnight` line and the A31 unit `drc-open-items/open_positions` (after the drc-trades section) render it. A stored resolve id that is no longer current (`DrcStore.superseded_stated_ids`) is stored as `stale_resolves` and renders STALE. `build_date`: a note that fails after `record_build` re-records the date's `build_day` with `derived["note_stale"] = {note, error}` and raises; a clean build drops the key. `rebuild_notes(dates)` is the one notes loop, with two callers: `run_drc_build`'s re-paired dates and the page's statements (`imports.state_book` / `resolve`). The failure text is unchanged.
