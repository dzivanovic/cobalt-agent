"""The ONE connection factory for the new core.

TRIAGE secrets law: DSNs are composed at runtime from parts, URL-encoded
(closes the @-in-password bug class), never logged. Parts come from the
environment today (POSTGRES_HOST/PORT/USER/PASSWORD); the vault-parts
composition replaces the env read when the ruled .env/DATABASE_URL
redesign (TRIAGE 2.7) lands. Two-phase boot stays possible because this
is plain application code, not dotenv.

ADR-0008 (two-layer data model) adds the SIDE. Cobalt's tables live in
two schemas — `system` (the engine any trader plugs strategies into) and
`"user"` (that trader's own data, never shipped to anyone else) — and
**the side is chosen per store, never per process**. Every store declares
`SIDE = Side.USER | Side.SYSTEM`; this factory turns that declaration
into three session settings on the connection it hands back:

    SET ROLE <cobalt_user | cobalt_system>
    SET search_path TO <that side's schema ONLY>   -- no public
    SET cobalt.trader_id = <configs/cobalt/tenant.yaml>

so a wrong-side statement fails loud twice over: relation-not-found (it
is not on the search_path) or permission denied (the role has no grant).
Cross-side reads are written schema-qualified (`system.bars`) and never
resolved through the search_path.

`side` IS REQUIRED. A call without it raises `DbConfigError` rather than
picking one — a connection whose side nobody chose is a connection whose
grants nobody chose.

`user` is a reserved word in PostgreSQL 16, so the schema name is always
quoted. In this module that is `psycopg.sql.Identifier`, never an
f-string; a suite lint test fails on any unquoted reference to that
schema anywhere under src/cobalt.

THE ONE `psycopg.connect` IN THE NEW CORE IS IN THIS FILE, and a suite
test greps for a second one. That is the enforcement behind the
one-factory law until the non-superuser `cobalt_app` login lands
(ADR-0008 D1 Revision 2, owed as its own ops prompt).
"""

import os
from enum import Enum
from typing import Optional
from urllib.parse import quote

import psycopg
from psycopg import sql

from cobalt import env, tenant

# Re-exported so existing importers of db.PROD_DB_NAME keep working;
# cobalt/env.py is the definition of record (RULING 7).
PROD_DB_NAME = env.PROD_DB_NAME
DEV_DB_NAME = env.DEV_DB_NAME


class Side(Enum):
    """Which half of the data model a connection is opened against.

    The value IS the schema name, and the role is `cobalt_<value>` — one
    name everywhere (ADR-0008 ruling 0, Revision 1). The word "trader"
    survives only inside table and field names (`trader_settings`,
    `traders`, `trader_id`, `trade_key`), never as a side.
    """

    USER = "user"
    SYSTEM = "system"

    @property
    def schema(self) -> str:
        return self.value

    @property
    def role(self) -> str:
        return f"cobalt_{self.value}"


class DbConfigError(RuntimeError):
    """Missing/invalid database settings — crash, never fall back."""


class SchemaMissingError(DbConfigError):
    """The two-layer schemas are not there yet — run `cobalt db migrate`."""


def _prod_gate(dbname: str, allow_prod: bool) -> None:
    """RULING 7: `cobalt_brain` needs a production declaration."""
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


def _open(dbname: str) -> psycopg.Connection:
    """Compose the DSN from parts and open. THE ONLY `psycopg.connect`."""
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


def apply_side(conn, side: Side, *, trader: Optional[int] = None) -> None:
    """Pin `conn` to one side: role, search_path, tenant GUC.

    Split out of `connect()` because the test suite's transaction fixture
    (RULING 7.1d) hands every store a savepoint proxy over ONE real
    connection and must pin it the same way — one path, so a test cannot
    accidentally run with wider grants than production does.

    `SET ROLE` is checked against the SESSION user, not the current role,
    so a connection already pinned to one side can be re-pinned to the
    other. Both settings are session-scoped and transactional: a rollback
    puts them back, which is exactly what the proxy wants.
    """
    ident = sql.Identifier(side.schema)  # `user` is reserved — always quoted
    conn.execute(sql.SQL("SET ROLE {}").format(sql.Identifier(side.role)))
    conn.execute(sql.SQL("SET search_path TO {}").format(ident))
    # set_config(...,  is_local => false) = session scope, and it takes the
    # value as a PARAMETER, so the tenant id never reaches the server as
    # interpolated SQL.
    conn.execute(
        "SELECT set_config(%s, %s, false)",
        (tenant.TRADER_GUC, str(tenant.trader_id() if trader is None else trader)),
    )


def connect(
    dbname: str, *, side: Side, allow_prod: bool = False
) -> psycopg.Connection:
    """Open a Postgres connection to `dbname`, pinned to `side`.

    RULING 7: `cobalt_brain` is reachable when this process has declared
    itself production (`COBALT_ENV=production`) — that declaration is
    what makes a production entrypoint a production entrypoint, and the
    stores now take their database name from `env.resolve_db_name()`
    rather than from a config file. `allow_prod=True` remains for
    one-off tooling (the migration harness) that must reach prod without
    flipping the whole process into production mode.

    Everything else still refuses: a dev run, a test, or a process with
    `COBALT_ENV` unset cannot open `cobalt_brain` (NN#16).

    ADR-0008: `side` is keyword-only and REQUIRED. Python raises TypeError
    on a call that omits it; the explicit check below turns a `None` or a
    string passed by a caller that half-migrated into the same loud
    `DbConfigError` every other config mistake gets.
    """
    if not isinstance(side, Side):
        raise DbConfigError(
            f"db.connect() needs side=Side.USER or side=Side.SYSTEM, got {side!r}. "
            "The side is chosen PER STORE (ADR-0008 D1): a connection whose side "
            "nobody chose is a connection whose grants nobody chose."
        )
    _prod_gate(dbname, allow_prod)
    conn = _open(dbname)
    try:
        apply_side(conn, side)
    except BaseException:
        conn.close()
        raise
    return conn


def connect_migration(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection:
    """The MIGRATION HARNESS's connection: no `SET ROLE`, no side.

    `cobalt db migrate` creates the schemas and the side roles, moves
    tables between schemas and transfers ownership — every one of which is
    an act the side roles are deliberately not able to perform on each
    other. So it runs as the login role, with `search_path` pinned to
    `public` (where the tables still are before 0002 runs) and the tenant
    GUC set (so a migration that inserts a user-side row is stamped like
    any other write).

    This is the ONE exception to `connect(side=...)` and it lives in this
    module, next to the only `psycopg.connect` call, precisely so it
    cannot become a second factory somewhere else.
    """
    _prod_gate(dbname, allow_prod)
    conn = _open(dbname)
    try:
        conn.execute("SET search_path TO public")
        conn.execute(
            "SELECT set_config(%s, %s, false)",
            (tenant.TRADER_GUC, str(tenant.trader_id())),
        )
    except BaseException:
        conn.close()
        raise
    return conn


def assert_schemas_exist(conn) -> None:
    """Fail loud if the two-layer schemas are not there yet.

    Called at the top of every store's `ensure_schema()`. Without it, a
    store on a pre-ADR-0008 database would run `CREATE TABLE IF NOT
    EXISTS <unqualified>` with a `search_path` naming a schema that does
    not exist, and Postgres's message for that ("no schema has been
    selected to create in") names nothing an operator can act on.
    """
    rows = conn.execute(
        "SELECT nspname FROM pg_namespace WHERE nspname IN ('system', 'user')"
    ).fetchall()
    found = {r[0] for r in rows}
    missing = {s.schema for s in Side} - found
    if missing:
        raise SchemaMissingError(
            f"schema(s) {', '.join(sorted(missing))} do not exist in this database. "
            "The two-layer data model (ADR-0008) has not been migrated here — run "
            "`cobalt db migrate` (add --allow-prod for cobalt_brain) before any "
            "store touches a table."
        )


__all__ = [
    "DEV_DB_NAME",
    "PROD_DB_NAME",
    "DbConfigError",
    "SchemaMissingError",
    "Side",
    "apply_side",
    "assert_schemas_exist",
    "connect",
    "connect_migration",
]
