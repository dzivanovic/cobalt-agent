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
