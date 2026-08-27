# `tests/cobalt/test_aset_config.py`

## What it does
Tests `config.py`'s fail-loud loading behavior for both configs
(`AsetConfig` / `load_config()` and, since iteration 4,
`SheetModesConfig` / `load_sheet_modes_config()`) and the `ServerConfig`
schema. Every "bad config" test writes a throwaway file to `tmp_path`
and monkeypatches the relevant `*_PATH` constant to point at it — none
of them touch the real `configs/dev/` or `configs/cobalt/` files except
the two "committed config is valid" tests.

**Iteration 4 (2026-08-28):** `COMPLETE` (the fixture YAML string) lost
`broker_hard_stop` — retired from `AsetConfig`. A new
`COMPLETE_SHEET_MODES` fixture and `TestSheetModesConfig` class cover
the new config entirely.

## Key functions/classes (what's covered, not defined)
- `test_committed_dev_config_is_valid` — the one `AsetConfig` test that
  DOES load the real, ambient config; only asserts loose invariants
  (`account_size > 0`, etc.) so it stays true regardless of which local
  overrides are active.
- Missing file, non-mapping YAML, unknown key, missing required field
  (`account_size`), non-positive `account_size` — all crash with
  `ConfigError` (or a Pydantic validation error for direct model
  construction).
- `ServerConfig` — default is loopback (`test_server_defaults_to_loopback`,
  deliberately unit-level against a fresh `ServerConfig()`, not
  `load_config()`, so it doesn't depend on whatever `bind:` value is
  live in Dejan's local file); `bind="lan"` resolves `.host` to
  `0.0.0.0`; unknown `bind` value and out-of-range `port` both rejected;
  a config file with no `server:` section at all still loads, defaulted
  to loopback (never silently exposed to the LAN).
- `test_local_override_wins_and_must_be_complete` — the local file
  replaces the base file's values, and an *incomplete* local file
  crashes rather than silently falling back to the base file's missing
  keys.
- `TestSheetModesConfig` — `test_committed_config_is_valid` loads the
  real `configs/cobalt/aset.yaml`; `test_dollars_for_matches_das_hotkey_values`
  hard-asserts the exact committed numbers (full A 135/B 60, half A
  70/B 30) — this is the test that would fail loudly if the config ever
  drifted from Dejan's actual hotkey files; `test_dollars_for_rejects_non_tradeable_grade`
  covers grade C; missing-file and missing-grade both crash with
  `ConfigError`; non-positive dollar values rejected at the Pydantic
  layer.

## Data flow in/out
Writes/reads throwaway YAML files under pytest's `tmp_path`.

## Config it reads
Indirectly, `configs/dev/aset.yaml` (only in
`test_committed_dev_config_is_valid`) and `configs/cobalt/aset.yaml`
(only in `TestSheetModesConfig.test_committed_config_is_valid` and
`test_dollars_for_*`); every other test isolates itself via
monkeypatched paths.
