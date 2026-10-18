# `src/cobalt/prefill/daily.py`

## What it does
Morning Daily Note prefill, a caller of the ONE write path (L28).
Renders `configs/cobalt/templates/daily.md.j2` through
`create_if_absent` when today's note does not exist; otherwise fills
each of its FOUR marker-bounded units (`SLOT_SPECS`) with `upsert_unit`,
which three-way merges and never overwrites his text:
- **rules / rules** — the config-driven, mode-aware rules checkbox list
  + mantras, placed after the second "I WILL NOT TOLERATE…" line.
- **daymode / sheet_mode** — rendered by `daymode.note`, placed after
  the rules section.
- **trading / market_table** — the market table under "### Trading".
  VIX/BTC render `n/a (manual)` (F4 [F-05]; the Slice 2.1 blank cells
  are superseded) and a value he types stays his.
- **market_calendar / market_calendar** — under "### Market Calendar:".

A unit already written is skipped (a second run is a zero-diff no-op),
except a body carrying `FAILED` from a dead source, which is retried
through the merge (`slot_state`). A missing anchor is not a run
failure: the section is appended at the end of the note. Pre-L28 notes
with `<!-- cobalt-slot:NAME -->` markers read as filled.

Market/calendar fetch failures at create render `FAILED: <reason>`
text, never blank. F4 (below) adds `run_daily_refresh` for the trading
and calendar units all day.

## Key functions/classes
- `format_market_row(ticker, rows, error) -> (col2, col3)` — one of
  SPY/QQQ/IWM only.
- `format_calendar_block(economic, earnings, error) -> str`.
- `format_sizing_rule_text(text, sheet_modes_cfg) -> str` — content-
  detected (regex on "B = $N, A = $N"), not tied to a rule id/position:
  splices in `"B = $30 half / $60 full, A = $70 half / $135 full"`
  (from `aset.config.load_sheet_modes_config()`, the SAME source ASET's
  sheet already uses) wherever that pattern appears; every other rule's
  text is untouched. `apply_mode_aware_sizing(rules, cfg)` maps this
  over a rule list (via `RuleItem.model_copy`, never mutates the input).
- `format_rules_checkbox_block(rules) -> str` — ONE tagged checkbox
  list, `- [ ] {text} #{category}` — the rules ARE the adherence boxes
  now; no separate read-only list, no separate adherence list. Also
  used by `drc.py` for its own "copied from the morning note" checklist.
- `format_mantras_block(rules_cfg) -> str`.
- `format_mode_hint(cards) -> str` — "if aset exposes the current mode
  at run time, show it" (Dejan's item 2): the only real runtime "current
  mode" signal aset has is today's own cards (`AsetStore.for_date`) —
  empty string if none yet (true most mornings at 05:15).
- `SLOT_SPECS`, `slot_state(text, section, unit)`, the placements
  (`RULES_PLACEMENT`, `DAYMODE_PLACEMENT`, `TRADING_PLACEMENT`,
  `MARKET_CALENDAR_PLACEMENT`) — the four units and where an absent one
  goes. `SlotAnchorNotFound` is kept as a type only; it is never raised.
- `run_daily_prefill(when=None) -> DailyPrefillResult` — the
  orchestrator. `action` is `"created" | "filled" | "skipped_idempotent"`;
  `filled_slots`/`skipped_slots` name exactly what happened, for the CLI
  to report ("a non-empty slot is skipped and reported").

## Data flow in/out
**In:** `prefill.market.fetch_market_table`, `prefill.calendar.fetch_*`,
`prefill.rules_gen.regenerate_rules_config` (regenerates
`configs/cobalt/rules.yaml` from the vault's Rules.md on every run —
not the old static `load_rules_config`), `aset.config.load_config()
.daily_note` + `load_sheet_modes_config()`, `aset.store.AsetStore.for_date`
(best-effort, for the mode hint only — a DB error there is swallowed,
not a run failure). **Out:** a written/edited file under the resolved
vault root, or a raised `VaultWriteError`/`RulesSourceError`/
`VaultConfigError`.

## Config it reads
`configs/dev/aset*.yaml` (daily_notes_dir/filename_pattern, db_name),
`configs/cobalt/aset.yaml` (sheet-mode dollars, via `load_sheet_modes_config`),
the vault's `1 - Trading/5 - Review/Rules.md` (via `regenerate_rules_config`,
NOT the committed `rules.yaml` directly — that's now a generated cache),
`configs/cobalt/templates/daily.md.j2`.

---

## 2026-09-25 — DRC D4-3: the daily note reads the daily-stop key (R95 / R102)

The template's `Daily HARD Stop:` line no longer carries a number — it
renders `{{ daily_stop }}`. `run_daily_prefill` fills it from the ONE
reader, `cobalt.settings.drc.daily_risk_values()`, through
`format_daily_stop(risk, error=None)`: `full $X · half $Y` per sheet, and
`not given` for an absent key (never the old literal, never blank). A
settings read that fails renders `FAILED: daily stop unreadable (…)` in the
new note and logs the error type — the 05:15 run is not lost. The line only
appears in a note the template CREATES; an existing note's line is his and
is not touched. The rest of the template is unchanged.

## 2026-10-10 — f4-refresh-1010
F4 (F4 FINAL F4-1): `run_daily_refresh(when, *, dry_run, store=None)` — the
`prefill refresh` engine — re-renders `trading/market_table` and
`market_calendar/market_calendar` of today's ET note; `format_stamp`,
`ensure_daily_note`, `refresh_note_path`, `stamp_context`,
`build_create_context` (the ONE create render, now shared by `daily` and
`refresh`), `check_refresh_demand` / `refresh_demand_consumer` (the shared
Finviz gate, form B), `read_rules_read_only` and `RefreshResult` added. The
template's four Cobalt units carry an `as of HH:MM ET` stamp (rules:
`· rules from Rules.md`; trading: the per-field flag line; calendar:
`· calendar <flag>`), and VIX/BTC render `n/a (manual)`. The rules unit's
fill body leads with its stamp. Docstring: four slots, not three.

## SEAM
The three signatures F5 imports (F4 FINAL `## SEAM` §2, [F-31]), byte for byte:
- `cobalt.daymode.note.daily_note_path(day)`, fed `SessionClock.to_et(when).date()`
- `cobalt.prefill.daily.ensure_daily_note(writer, when) -> WriteResult`
- `cobalt.prefill.daily.format_stamp(when: datetime) -> str`

`ensure_daily_note` needs an aware `when` (a naive one raises `SessionError`),
writes through the caller's writer (its dry-run included), creates an absent
note through the shared render from read-only inputs (Rules.md parsed, never
`regenerate_rules_config` nor `load_rules_config`), and returns
`skipped_exists` for a note that exists, never replacing it. `format_stamp`
returns `as of HH:MM ET` through `SessionClock.to_et`, never the host zone.

## PDD — F4, prefill all day (ownership flags)
- **Purpose.** Charter:82-87 — the note's Cobalt blocks are stamped, refresh
  on a config cadence and on a manual trigger, his text is never touched,
  VIX/BTC read a loud `n/a (manual)` until owned.
- **Entry.** `uv run prefill refresh [--dry-run]` (`prefill/cli.py`), job
  `com.cobalt.prefill-refresh`: one-shot, every `prefill.refresh_interval_min`
  (30) inside `prefill.refresh_window` (05:45-15:45 ET), weekdays; plist
  `ops/com.cobalt.prefill-refresh.plist` (105 entries = `calendar_entries()`).
- **Config.** `prefill.yaml` `daily_refresh:` → `DailyRefreshConfig`
  (`units` exactly the two; `fields` exactly SPY/QQQ/IWM/VIX/BTC, each
  `cobalt|manual`; VIX/BTC `cobalt` refused — no source).
- **Ownership** ([F-26], [F-27]), decided inside `upsert_unit` on every write
  attempt (`body_fn`): the proposal is `last_after`'s unit body; a ticker /
  manual / stamp line is HIS when the on-disk line differs from `last_after`'s
  (and the whole unit is not a recent Cobalt body — a sync revert), or when an
  override row's `human_text` holds the on-disk line; his line is copied, a
  Cobalt row is the fresh fetch, a deleted or renamed row is not resurrected,
  blank manual cells become `n/a (manual)`. The calendar is whole-unit: written
  only when the on-disk body is `last_after` or a recent after (`skip_if`, also
  per attempt); its live flag rides on the trading stamp line.
- **Degraded** ([F-28]). A dead source or a refused gate keeps the last values,
  flags `<T> cobalt-degraded (<why>; values as of HH:MM)` with the LAST
  SUCCESS's time (read from Cobalt's own stamps in `last_after` and the recent
  afters), never the word FAILED in the unit, and the job exits 1
  (`RefreshNotClean` raised inside `as_job`).
- **Gate** (form B, R2-4). `read_plan()` (the strike loop's plan) first; no
  plan / no headroom → refused here, never `radar_rpm=None`; else
  `check_scheduled_demand("prefill-refresh", radar_rpm=planned, extra=[3 /
  interval rpm over the window])`. Refused → nothing requested.
- **Absent note / stub** ([F-08], [F-35], [F-36+]). Absent → `ensure_daily_note`
  creates it and the run ends. A note without the trading unit → the two units
  are appended at their placements (the write seeds the baseline); a unit
  already on disk with no baseline → nothing written, exit 1,
  `FAILED: baseline_missing`.
- **Never** a write to `rules`, `daymode`, `market_context`, heartbeat, cards;
  never `regenerate_rules_config`, `load_rules_config`, `run_daily_prefill`.
- **Known reds, carried to him** (build report `## DECISIONS`): T2b (adjacent
  rows stale one refresh after his edit, flagged `cobalt`), X12 (commit-window
  race records an override naming the other run's values), X16 (a hand-typed
  table in a stub's trading placement is overwritten).

## 2026-10-10 — f4-refresh-1010 check: four fixes in the refresh path
A `manual` SPY/QQQ/IWM in `daily_refresh.fields` renders `n/a (manual)` and its flag on create and on a stub (A1); a create that loses the race to another writer refreshes that writer's note on the ownership path instead of raising (A2); a field row he adds flags that field `human` (A5); a dead or refused source exits 1 even when every field it serves is his, and the report names the source (A6). The page's Slice 2.1 text above now describes the four-unit L28 writer (A7). Still open: the degraded age when his stamp owns the line (O1/A3), `FAILED` cells in a refresh-created note on a dead source (O2/B1).

## 2026-10-10 — f4-refresh-1010 fix round (R998)
X16: on a stub, a table he typed under `### Trading` is his; the trading upsert's `skip_if` refuses to wrap it, nothing is written, and the fields read `human`. X12 (no lock): `_Refresh.trading_in_flight` is the ownership upsert's `skip_if`. A trading unit whose machine status line (`_MACHINE_STAMP_RE`) is held by no visible `vault_writes` after belongs to another run's commit in flight. That run writes nothing, records no override and exits 1 (`FAILED: write_in_flight`). A4: `build_sheet_mode_block(when)` reads the ET day of the caller's aware `when` and stamps with it, never the wall clock. B5 is pinned: a refresh-created note is byte-identical to `prefill daily`'s. Supersedes the X12/X16 lines of "Known reds" above; T2b stays. Carried: O1/A3 (strict xfail; needs a migration, follow-up card).
