# `tests/cobalt/test_aset_config.py`

## What it does
Tests `config.py`'s fail-loud loading behavior and the `ServerConfig`
schema. Every "bad config" test writes a throwaway file to `tmp_path`
and monkeypatches `CONFIG_PATH`/`LOCAL_CONFIG_PATH` to point at it —
none of them touch the real `configs/dev/` files.

## Key functions/classes (what's covered, not defined)
- `test_committed_dev_config_is_valid` — the one test that DOES load the
  real, ambient config (whatever `configs/dev/aset*.yaml` currently
  resolves to); only asserts loose invariants (`account_size > 0`, etc.)
  so it stays true regardless of which local overrides are active.
- Missing file, non-mapping YAML, unknown key, missing required field
  (`broker_hard_stop`), non-positive `account_size` — all crash with
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

## Data flow in/out
Writes/reads throwaway YAML files under pytest's `tmp_path`.

## Config it reads
Indirectly, `configs/dev/aset.yaml` (only in
`test_committed_dev_config_is_valid`); every other test isolates itself
via monkeypatched paths.
