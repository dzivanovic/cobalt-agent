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
test greps for a second one.

TWO CREDENTIALS, ONE NAME EACH (2026-09-09 — ADR-0008 D1 Revision 2's
owed ops prompt). Until today the factory logged in as the docker
SUPERUSER, and a superuser bypasses every grant check: the `SET ROLE` in
`apply_side` made the grants bite for that session, but a connection
that skipped the factory kept full power, and the lint test was the only
thing holding that line. So the login is split by PURPOSE, and each
purpose has exactly one name:

  `Credential.APP`        COBALT_DB_USER / COBALT_DB_PASSWORD
                          -> `cobalt_app`: LOGIN, NOINHERIT, no
                          superuser, no createdb / createrole /
                          replication / bypassrls. A member of
                          `cobalt_system`, `cobalt_user` and
                          `cobalt_backup` — and NOINHERIT means it holds
                          none of their privileges until a `SET ROLE`,
                          so a connection that skips `apply_side` can
                          read nothing at all. `connect()` uses this,
                          which is every store, every job, every probe.

  `Credential.BOOTSTRAP`  POSTGRES_USER / POSTGRES_PASSWORD
                          -> the docker superuser. Its meaning is
                          unchanged and must not change: docker-compose
                          interpolates this pair for the container's own
                          superuser and the old tree reads it too.
                          MIGRATIONS AND BOOTSTRAP ONLY — `CREATE ROLE`,
                          `ALTER ... OWNER`, `SET SCHEMA`: the acts the
                          side roles are deliberately unable to perform.

THERE IS NO FALLBACK BETWEEN THEM. A missing `COBALT_DB_*` raises
`DbConfigError` naming both variables rather than quietly reaching for
`POSTGRES_*`. Running the whole application as superuser because one
line was missing from `.env` is exactly the failure this split exists to
make impossible, and a silent fallback would reintroduce it.
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


#: The non-superuser application login (item A, 2026-09-09). The role's
#: password lives in VaultManager under `COBALT_DB_PASSWORD` — which IS
#: its F19 literal-guard enrolment — and in `.env` as the bootstrap tier,
#: exactly like `MATTERMOST_DB_PASSWORD` (2026-09-05 precedent).
APP_ROLE = "cobalt_app"


class Credential(Enum):
    """WHICH login a connection authenticates as. See the module
    docstring: `APP` for everything the application does, `BOOTSTRAP`
    for migrations and bootstrap only. The value is the (user, password)
    environment-variable pair — one name per concept, written down once.
    """

    APP = ("COBALT_DB_USER", "COBALT_DB_PASSWORD")
    BOOTSTRAP = ("POSTGRES_USER", "POSTGRES_PASSWORD")

    @property
    def user_env(self) -> str:
        return self.value[0]

    @property
    def password_env(self) -> str:
        return self.value[1]


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


def _open(dbname: str, credential: Credential = Credential.APP) -> psycopg.Connection:
    """Compose the DSN from parts and open. THE ONLY `psycopg.connect`.

    `POSTGRES_HOST` / `POSTGRES_PORT` are the ADDRESS and are shared by
    both credentials — there is one server, and which login you use has
    nothing to do with where it is. Only the user/password pair changes,
    which is why `Credential` carries exactly that pair.
    """
    host = os.getenv("POSTGRES_HOST")
    user = os.getenv(credential.user_env)
    password = os.getenv(credential.password_env)

    missing = [
        name
        for name, value in (
            ("POSTGRES_HOST", host),
            (credential.user_env, user),
            (credential.password_env, password),
        )
        if not value
    ]
    if missing:
        raise DbConfigError(
            f"Missing Postgres settings for the {credential.name} credential: "
            f"{', '.join(missing)}. That credential is composed from "
            f"{credential.user_env} and {credential.password_env} (plus "
            "POSTGRES_HOST/POSTGRES_PORT, shared). Fail-loud: no default "
            "credentials, and NO FALLBACK to the other pair — running the "
            "application as the bootstrap superuser because a line is missing "
            "from .env is the failure this split exists to prevent."
        )
    port = os.getenv("POSTGRES_PORT", "5432")

    dsn = (
        "postgresql://"
        f"{quote(user, safe='')}:"  # type: ignore[arg-type]
        f"{quote(password, safe='')}@"  # type: ignore[arg-type]
        f"{host}:{port}/{quote(dbname, safe='')}"
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

    2026-09-09: this authenticates as `Credential.APP` — `cobalt_app`,
    NOINHERIT and non-superuser. The `SET ROLE` in `apply_side` is now
    what makes the connection able to read anything at all, rather than
    what makes an already-omnipotent session behave.
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

    SUPERUSER: MIGRATIONS AND BOOTSTRAP ONLY. This is the one caller of
    `Credential.BOOTSTRAP` (`POSTGRES_USER`/`POSTGRES_PASSWORD` — the
    docker superuser), and it stays that way. Everything the application
    does goes through `connect()` as `cobalt_app`.

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
    conn = _open(dbname, Credential.BOOTSTRAP)
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
    "APP_ROLE",
    "DEV_DB_NAME",
    "PROD_DB_NAME",
    "Credential",
    "DbConfigError",
    "SchemaMissingError",
    "Side",
    "apply_side",
    "assert_schemas_exist",
    "connect",
    "connect_migration",
]
