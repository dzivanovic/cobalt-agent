# `src/cobalt/settings/models.py`

## What it does
`TraderSettings` — the two objects the runtime already used
(`SheetModesConfig`, `DayModeConfig`), unchanged, built from seven rows
instead of two committed YAML files.

## Key functions/classes
- `SETTING_KEYS` — seven dotted paths: `aset.sheet_modes`,
  `aset.enabled_grades`, and five `daymode.*`.
- `TraderSettings.from_db(store)` — the runtime's ONLY reader.
- `TraderSettings.from_yaml(dir | texts=)` — SEEDING ONLY. `texts=` is
  how `--from-git` reads the files out of history without putting them
  back in the working tree.
- `rows()` / `rows_from_yaml()` — the row layout, both directions.
- `diff(other)` — `{key: (mine, theirs)}`; the Revision-3 proof.

## Why one row per top-level setting
Not per blob: every diff would read "aset changed", useless in a
`--dry-run` when you need to know which knob moved. Not per leaf: that
splits a Pydantic-validated object across rows and a half-applied update
validates nowhere. A top-level setting is the unit that is validated and
ruled as a whole, so `source` and `updated_at` are per-setting facts.

## Gotchas
Both halves are built TOGETHER, because `reduced_enabled_grades` may only
narrow `aset.enabled_grades` and that cross-check has to keep firing now
that the two live in separate rows. A Pydantic failure is re-raised as
`TraderSettingsError` naming the rows, not a file that is no longer the
source.

---

## 2026-09-17 — S2-P4: `radar.benchmark` (ruling R5, Astra R1-14)

- `BENCHMARK_KEY = "radar.benchmark"`, and `BenchmarkSettings {top_n > 0,
  min_move_pct > 0}` (frozen, extra forbidden). `from_rows(rows)` is the
  runtime reader. An absent row or a malformed value raises
  `TraderSettingsError`, never a default. `row()` gives the jsonable value.
- The key is OPTIONAL and is **not** in `SETTING_KEYS` (plan F14): a required
  key crashes the ASET sheet when missing, and a missing benchmark must fail
  only the replay's movers step.
- `OPTIONAL_SETTING_KEYS` / `OPTIONAL_SETTING_MODELS` are the one registry
  of optional keys and their models. The `--optional` loader and every
  reader use it.

---

## 2026-09-25 — DRC D4-1: the DRC key families (SPEC §7 names; v2 [F-16] / [F-18])

- ONE ROW PER LEAF, keyed by the dotted SPEC path, like the `daymode.*`
  rows. Four family models, every field `Optional` (absent → `None` →
  callers print `not given`, L1): `DrcAccountSettings`
  (`daily_stop_full`, `daily_stop_half`: Decimal > 0),
  `DrcLimitsSettings` (`card_match_window_minutes`: strict int > 0),
  `DrcWindowsSettings` (`premarket_end` HH:MM; `first_window_minutes`
  strict int > 0; `prime` / `dead` / `second` as `[start, end]` HH:MM with
  start < end), `DrcGoalSettings` (`primary` / `metric` non-empty text;
  `target_pct` `[low, high]` within 0–100, low ≤ high;
  `switch_threshold_pct` 0–100).
- `DRC_FAMILIES` (family → model), `DRC_SETTING_KEYS` (the 12 dotted keys),
  `DAILY_STOP_KEYS` (sheet id → its daily-stop key).
- `DrcKey(key)` is the registry adapter for one leaf: `validate(value)`
  returns the typed leaf or raises `TraderSettingsError` NAMING THE KEY (a
  stored null is refused too); `from_rows(rows).row()` gives the JSON
  value, like `BenchmarkSettings`.
- Every DRC key is in `OPTIONAL_SETTING_KEYS` (and `OPTIONAL_SETTING_MODELS`
  maps it to its `DrcKey`), NEVER in `SETTING_KEYS`: a missing DRC key must
  not touch the ASET sheet's reader.
- Left out on purpose: `grades.*` (the dollars per grade are the existing
  `aset.sheet_modes` row — a copy is an L3 defect), `account.sheet_mode_default`
  (the day mode rules which sheet a day uses), `sleep_trigger.*` and the
  other `limits.*` names (no reader yet; no rule→checker map, R101).
- `TraderSettingsError` now sits above these models (they raise it); its
  meaning is unchanged.
