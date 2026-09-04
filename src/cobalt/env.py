"""The ONE environment resolver: `COBALT_ENV` decides database and vault.

RULING 7 (2026-09-04). Before this module there were two independent,
silent defaults and they disagreed with each other:

* the **vault** defaulted to dev (`configs/dev/vault.yaml` →
  `~/dev-vault-cobalt`) whenever `COBALT_ENV` was unset, and
* the **database** defaulted to `cobalt_dev` from
  `configs/dev/aset.local.yaml`'s `db_name` — for *every* caller,
  production included.

So the production ASET sheet and both prefill jobs wrote live trading
cards into `/Users/cobalt/Vault/Think` and their audit trail into
`cobalt_dev`, side by side with pytest's temp-vault rows. The 09-03
incident reconstruction depended on `vault_writes` rows 525-528 that
were sitting in the dev database, and the DRC reported "17 cards" when
2 were real because 15 stray `TEST`/`FORDATE` rows from the test suite
shared the table. See `docs/00 - Project/INCIDENT-2026-09-03-notes.md`.

**The law this module enforces:**

1. `COBALT_ENV` ∈ {`production`, `dev`}. Unset or anything else raises
   at boot with a one-line message. There is NO default — not for the
   database, not for the vault. Nothing resolves silently to either.
2. `production` → database `cobalt_brain`, vault `/Users/cobalt/Vault/Think`.
   `dev` → database `cobalt_dev`, vault from `configs/dev/vault.yaml`
   (or `COBALT_VAULT_PATH`), which must NOT be inside the real vault.
3. The database is NOT configurable per-component any more. `db_name`
   is gone from `AsetConfig`; a store that needs a database asks this
   module. A config file cannot route production writes to dev again.

`cobalt.vault.resolve_vault_path()` is the vault half and calls in
here for the mode; this module owns the mode and the database name.
"""

import os

ENV_VAR = "COBALT_ENV"

PRODUCTION = "production"
DEV = "dev"
VALID_ENVS = (PRODUCTION, DEV)

PROD_DB_NAME = "cobalt_brain"
DEV_DB_NAME = "cobalt_dev"

# The only database any destructive helper may ever touch (RULING 7.1c).
DESTRUCTIVE_DB_ALLOWLIST = (DEV_DB_NAME,)

_DB_BY_ENV = {
    PRODUCTION: PROD_DB_NAME,
    DEV: DEV_DB_NAME,
}


class EnvConfigError(RuntimeError):
    """`COBALT_ENV` unset or unknown — crash at boot, never guess."""


def resolve_env() -> str:
    """Return `production` or `dev`, or raise. The one entry point."""
    raw = os.getenv(ENV_VAR)
    if raw in VALID_ENVS:
        return raw
    got = "unset" if raw is None else repr(raw)
    raise EnvConfigError(
        f"{ENV_VAR} is {got} — set it to one of {', '.join(VALID_ENVS)}. "
        "There is no default: production means cobalt_brain + the real "
        "vault, dev means cobalt_dev + the dev vault (RULING 7)."
    )


def is_production() -> bool:
    """True in production, False in dev. Raises if `COBALT_ENV` is unset."""
    return resolve_env() == PRODUCTION


def resolve_db_name() -> str:
    """The database this process must use, from `COBALT_ENV` alone.

    Deliberately takes no argument and reads no config file: a per-
    component `db_name` is exactly how production came to write into
    `cobalt_dev`.
    """
    return _DB_BY_ENV[resolve_env()]


def assert_destructive_target(db_name: str) -> None:
    """Refuse a truncate/drop/reset against anything but `cobalt_dev`.

    RULING 7.1c. Hard-coded on purpose — not read from config, not
    keyed on `COBALT_ENV`, not overridable by an env var. A destructive
    helper run by accident inside a production shell must still refuse.
    """
    if db_name not in DESTRUCTIVE_DB_ALLOWLIST:
        raise EnvConfigError(
            f"REFUSED: destructive operation targeted '{db_name}'. Destructive "
            f"helpers may only ever touch {', '.join(DESTRUCTIVE_DB_ALLOWLIST)} "
            "(RULING 7.1c) — this is hard-coded and cannot be overridden."
        )
