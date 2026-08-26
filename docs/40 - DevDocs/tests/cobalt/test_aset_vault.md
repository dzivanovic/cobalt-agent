# `tests/cobalt/test_aset_vault.py`

## What it does
Tests `vault.resolve_vault_path()`'s fail-loud behavior and precedence
(env override wins over config file). One test does hit the real,
committed `configs/dev/vault.yaml` (asserting only `is_dir()`, so it
stays true regardless of exactly where the vault lives); every other
test isolates itself via `monkeypatch` on `CONFIG_PATH` or the env var,
using `tmp_path`.

## Key functions/classes (what's covered, not defined)
- `test_committed_config_resolves_the_real_vault` — the one ambient test.
- `test_env_override_wins_over_config` — `COBALT_VAULT_PATH` takes
  precedence.
- `test_env_override_rejects_missing_path` — env pointing at a
  nonexistent directory still fails loud.
- `test_missing_config_and_no_env_crashes` — the base "unset" case.
- `test_config_pointing_at_missing_path_crashes` — config file valid
  YAML, but the path it names doesn't exist.
- `test_config_resolves_a_real_directory` — the happy path via a fake
  config file.
- `test_unknown_key_rejected` — `extra="forbid"` enforced.

## Data flow in/out
None persistent — writes throwaway YAML under `tmp_path` where needed.

## Config it reads
`configs/dev/vault.yaml` (only in the one ambient test).
