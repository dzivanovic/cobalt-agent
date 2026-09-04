"""The ONE connection factory for the new core.

TRIAGE secrets law: DSNs are composed at runtime from parts, URL-encoded
(closes the @-in-password bug class), never logged. Parts come from the
environment today (POSTGRES_HOST/PORT/USER/PASSWORD); the vault-parts
composition replaces the env read when the ruled .env/DATABASE_URL
redesign (TRIAGE 2.7) lands. Two-phase boot stays possible because this
is plain application code, not dotenv.
"""

import os
from urllib.parse import quote

import psycopg

from cobalt import env

# Re-exported so existing importers of db.PROD_DB_NAME keep working;
# cobalt/env.py is the definition of record (RULING 7).
PROD_DB_NAME = env.PROD_DB_NAME
DEV_DB_NAME = env.DEV_DB_NAME


class DbConfigError(RuntimeError):
    """Missing/invalid database settings — crash, never fall back."""


def connect(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection:
    """Open a Postgres connection to `dbname`, composing the DSN from parts.

    RULING 7: `cobalt_brain` is reachable when this process has declared
    itself production (`COBALT_ENV=production`) — that declaration is
    what makes a production entrypoint a production entrypoint, and the
    stores now take their database name from `env.resolve_db_name()`
    rather than from a config file. `allow_prod=True` remains for
    one-off tooling (the migration harness) that must reach prod without
    flipping the whole process into production mode.

    Everything else still refuses: a dev run, a test, or a process with
    `COBALT_ENV` unset cannot open `cobalt_brain` (NN#16).
    """
    if dbname == PROD_DB_NAME and not allow_prod:
        try:
            declared_production = env.is_production()
        except env.EnvConfigError:
            declared_production = False  # unset is definitively not production
        if not declared_production:
            raise DbConfigError(
                f"Refusing to connect to production database '{PROD_DB_NAME}': "
                f"this process has not declared {env.ENV_VAR}={env.PRODUCTION} "
                "(NN#16 / RULING 7). Pass allow_prod=True only from migration "
                "tooling that must reach prod deliberately."
            )

    parts = {
        "POSTGRES_HOST": os.getenv("POSTGRES_HOST"),
        "POSTGRES_USER": os.getenv("POSTGRES_USER"),
        "POSTGRES_PASSWORD": os.getenv("POSTGRES_PASSWORD"),
    }
    missing = [name for name, value in parts.items() if not value]
    if missing:
        raise DbConfigError(
            f"Missing Postgres settings: {', '.join(missing)}. "
            "Fail-loud: no default credentials, no silent fallback."
        )
    port = os.getenv("POSTGRES_PORT", "5432")

    dsn = (
        "postgresql://"
        f"{quote(parts['POSTGRES_USER'], safe='')}:"
        f"{quote(parts['POSTGRES_PASSWORD'], safe='')}@"
        f"{parts['POSTGRES_HOST']}:{port}/{quote(dbname, safe='')}"
    )
    return psycopg.connect(dsn, autocommit=True)
