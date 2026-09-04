# `src/cobalt/env.py`

## What it does
The **one environment resolver** for the new core. `COBALT_ENV` decides
the database and (via `cobalt/vault.py`) the vault root. There is no
default for either: unset or unknown raises at boot.

RULING 7 (2026-09-04, ADR-0005). Before it, the vault defaulted to dev
when `COBALT_ENV` was unset while the database was read from
`configs/dev/aset.local.yaml`'s `db_name` for *every* caller — so the
production ASET sheet and both prefill jobs wrote live trading cards
into `/Users/cobalt/Vault/Think` and their L28 audit trail into
`cobalt_dev`, interleaved with pytest rows.

## Key functions/classes
- `EnvConfigError(RuntimeError)` — `COBALT_ENV` unset/unknown, or a
  destructive target refused.
- `ENV_VAR = "COBALT_ENV"`, `PRODUCTION = "production"`, `DEV = "dev"`.
- `PROD_DB_NAME = "cobalt_brain"`, `DEV_DB_NAME = "cobalt_dev"`.
- `resolve_env() -> str` — the one entry point. `production` or `dev`,
  or raises.
- `is_production() -> bool` — note it **raises** when unset. The old
  `os.getenv(...) == "production"` shape answered `False`, which is the
  silent default this ruling removes.
- `resolve_db_name() -> str` — takes no argument and reads no config
  file, deliberately: a per-component `db_name` is exactly how
  production came to write into `cobalt_dev`.
- `assert_destructive_target(db_name) -> None` — raises unless
  `db_name == "cobalt_dev"`. Hard-coded, NOT keyed on `COBALT_ENV`.

## Data flow in/out
**In:** the `COBALT_ENV` environment variable, and nothing else. No
YAML, no `.env` key, no argument.
**Out:** `"production"`/`"dev"`, or a database name, or an exception.

## Config it reads
None. That is the design: this module is the thing a config file must
not be able to override.

## Safety properties
- **No default, anywhere.** An unset flag fails the database resolution
  and the vault resolution identically. A process that has not said
  which environment it is in does not get to guess.
- **The destructive guard is orthogonal to the environment.**
  `assert_destructive_target()` refuses `cobalt_brain` even when
  `COBALT_ENV=production` — the shell where every other guard has
  already stood aside. `COBALT_ENV` decides where the application reads
  and writes; it must never decide where a TRUNCATE lands.
- **`extra="forbid"` on `AsetConfig`** means re-adding `db_name:` to a
  config file is a loud crash, not a quietly honoured override.

## Who calls it
- `cobalt/vault.py` — `resolve_vault_path()` calls `resolve_env()`
  first and unconditionally.
- `cobalt/db.py` — gates `cobalt_brain` on `is_production()`.
- `cobalt/aset/store.py`, `cobalt/vaultwrite/store.py` — both default
  `db_name=None` and call `resolve_db_name()`.
- `cobalt/aset/web.py` — the sheet prints the resolved database in its
  own page banner, so "which database am I writing to" is visible
  without reading a config file.
- `cobalt/devdb.py` — the guarded destructive helper.

## Tests
`tests/cobalt/test_env.py` — 29 cases: unset/unknown/empty-string all
raise; the db name follows the mode; the vault raises on an unset flag
and resolves Think in production with no `COBALT_VAULT_PATH`; the
factory refuses `cobalt_brain` from dev and from an unset environment;
the destructive guard refuses six non-dev names including from inside a
production shell; the shipped config files on disk carry no `db_name`;
both stores follow the resolver and raise rather than default.

## Gotchas
- `is_production()` raises rather than returning `False`. Callers that
  genuinely want "not production, whatever that means" must catch
  `EnvConfigError` — `db.connect()` does exactly this, because for the
  purpose of refusing production access, unset is definitively not
  production.
- The test suite pins `COBALT_ENV=dev` autouse in
  `tests/cobalt/conftest.py`. A test that needs another value must
  `monkeypatch.setenv` it.
- A running process keeps the environment it was launched with. Changing
  a plist and reloading the job does NOT change a process that survived
  the bootout (`AbandonProcessGroup`) — see Defect 1, 2026-09-01, and
  `com.cobalt.agent` in ADR-0005.
