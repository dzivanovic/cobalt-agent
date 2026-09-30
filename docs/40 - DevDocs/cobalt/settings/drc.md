# `src/cobalt/settings/drc.py`

## What it does
The DRC settings family's readers, and the ASET change line's proposal
(DRC D4; v2 §5 T9 [F-18] / [F-16]; his rulings R95 / R96 / R102). Added
2026-09-25.

- `load_drc_settings(conn=None) -> DrcSettings` — THE reader of the DRC
  keys (`account.*`, `limits.card_match_window_minutes`, `windows.*`,
  `goal.*`; the models are in `settings/models.py`). A key with no row is
  `None`; a present row that does not validate raises
  `TraderSettingsError` naming the key (a stored value known false is a
  defect, L1).
- `daily_risk_values(conn=None) -> DailyRisk` — THE ONLY function on any
  DRC or daily-note path that returns the daily stop or the dollars per
  grade (L3). `daily_stop` is `{sheet: Decimal | None}` from the
  `account.daily_stop_*` rows; `sheet_modes` is `load_sheet_modes_config()`
  — the existing `aset.sheet_modes` row — and `grade_dollars` is
  `{sheet: {grade: dollars}}`, sheets low to high. A missing
  `aset.sheet_modes` row is that loader's own loud `ConfigError`.
- `propose_daily_change(form, conn=None) -> DailyChange` — the change
  line's review: validates every posted field against what is stored now
  and returns `payload` (only the rows that change), `diff`
  (`(field, old, new)`, `not given` for an absent old value) and `sha256`
  (`settings.cli.payload_sha256`). A blank daily-stop field leaves that key
  alone; a blank grade is refused ("a grade with no dollar"). Every
  failure names its field, all of them are raised together as
  `DailyChangeInvalid`, and no payload is built — so a partial write cannot
  be proposed. The grade dollars travel as ONE rebuilt `aset.sheet_modes`
  row (validated as a whole `SheetModesConfig`, `enabled_grades` kept).
- `change_line_fields(risk)` — the inputs the page renders; `shown(v)` —
  a value or `not given`.

## `conn`
The settings source: a `TraderSettingsStore`, or anything with
`.values() -> {key: value}`; `None` opens the default store. D3's
`drc-risk/facts` unit calls `daily_risk_values(conn)` and
`load_drc_settings(conn)` — never a second reader (the L72 seam). The
grade dollars always come through `load_sheet_modes_config()`, which opens
its own store.

## What it does NOT do
It writes nothing. The write is `settings.cli.apply_settings`, called by
the ASET page's `/settings/daily/apply` and by `cobalt settings load`.
No rule→checker map, no checker ids (R101). No `grades.*` copy.

## Tests
`tests/cobalt/test_drc_settings.py` (offline, constructed store) and
`tests/cobalt/test_drc_settings_db.py` (E10 / X12 / the apply, on
`cobalt_dev` inside the rollback).
