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

PROD_DB_NAME = "cobalt_brain"


class DbConfigError(RuntimeError):
    """Missing/invalid database settings — crash, never fall back."""


def connect(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection:
    """Open a Postgres connection to `dbname`, composing the DSN from parts.

    Refuses the production database unless `allow_prod` is passed
    explicitly (NN#16: build work never touches prod).
    """
    if dbname == PROD_DB_NAME and not allow_prod:
        raise DbConfigError(
            f"Refusing to connect to production database '{PROD_DB_NAME}' "
            "from build code (NN#16). Pass allow_prod=True only from "
            "deployed production entrypoints."
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
