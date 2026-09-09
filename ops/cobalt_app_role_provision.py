#!/usr/bin/env python
"""Mint `cobalt_app` — the non-superuser login the application uses.

This closes ADR-0008 D1 Revision 2's KNOWN LIMIT, stated in
`db_migrations/0001_schemas.sql` and escalated as item 3 of the
2026-09-08 ADR report:

    "The login role is still the docker superuser, and a superuser
    bypasses every grant check. After the factory's SET ROLE the
    session's CURRENT role is a non-superuser and the grants bite, so
    per-store enforcement is real — but a connection that skips the
    factory keeps full power."

`cobalt_app` is that closure. It is `LOGIN NOINHERIT`, holds no privilege
of its own, and is a member of `cobalt_system`, `cobalt_user` and
`cobalt_backup`. Under NOINHERIT a session that has not called `SET ROLE`
— that is, one that skipped `cobalt.db.connect()` — can read NOTHING.
The lint test stops being the only thing holding the line; the server is.

WHAT IT IS NOT, and every one of these is written out rather than left to
a default, so that `\\du` shows exactly what was asked for:
NOSUPERUSER, NOCREATEDB, NOCREATEROLE, NOREPLICATION, NOBYPASSRLS.

THE MECHANISM IS `ops/pg_role.py` — the same one that minted the
`mattermost` role on 2026-09-05: SCRAM verifier computed locally so the
plaintext never crosses the socket, the value never in an argv, `.env`
written with Python file I/O, a copy in VaultManager which IS the F19
literal-guard enrolment. This file carries only what differs: the role,
its key names, its memberships and its `.env` block.

ROLES ARE CLUSTER-WIDE. `CREATE ROLE` writes a shared catalog, so this
runs once against the live cluster and the role exists for every database
on the server. The GRANTs are per-database and are NOT: this script
grants `CONNECT` on `cobalt_dev` and on nothing else. Reaching
`cobalt_brain` is a separate, named LIVE step —

    GRANT CONNECT ON DATABASE cobalt_brain TO cobalt_app;

— deliberately left out of this script so that a dev-side provisioning
run cannot, by itself, give a new credential a path into production
(NN#16). Until that step runs, `psql -U cobalt_app -d cobalt_brain` is
`permission denied for database "cobalt_brain"`, and the report proves it.

WHY `PUBLIC`'s CONNECT DOES NOT MAKE THAT GRANT REDUNDANT. It would, if
it were still there: Postgres grants `CONNECT` to `PUBLIC` on every new
database. The 2026-09-05 Mattermost work revoked it on `cobalt_brain` and
`cobalt_dev`, which is why an explicit grant is needed here at all — and
why the `cobalt_brain` refusal above is a real fence rather than an
accident of ordering.

Run:  uv run python ops/cobalt_app_role_provision.py
"""

from __future__ import annotations

import sys
from pathlib import Path

from dotenv import load_dotenv
from psycopg import sql

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pg_role  # noqa: E402  (same directory; see the module docstring)
from pg_role import ProvisionError  # noqa: E402

ROLE = "cobalt_app"

#: One name per concept: "the app login". `cobalt.db.Credential.APP`
#: carries these same two strings and is the definition of record; they
#: are repeated here only because this script runs before anything
#: imports the new core.
USER_KEY = "COBALT_DB_USER"
PASSWORD_KEY = "COBALT_DB_PASSWORD"

#: The three NOLOGIN side roles from `db_migrations/0001_schemas.sql`.
#: `cobalt_app` reaches each of them by `SET ROLE` and by nothing else.
MEMBERSHIPS = ("cobalt_system", "cobalt_user", "cobalt_backup")

#: The database this script may grant CONNECT on. `cobalt_brain` is a
#: LIVE step, printed and not run — see the module docstring.
DEV_DATABASE = "cobalt_dev"

ENV_BLOCK = """
# The application's Postgres login (2026-09-09, ADR-0008 D1 Rev 2 closed).
# `cobalt_app`: LOGIN NOINHERIT, non-superuser, member of cobalt_system /
# cobalt_user / cobalt_backup — it holds nothing until db.connect()'s
# SET ROLE. Read by cobalt.db.Credential.APP.
#
# POSTGRES_USER/POSTGRES_PASSWORD above are UNCHANGED and still mean the
# docker superuser: docker-compose interpolates them for the container,
# the old tree reads them, and cobalt.db uses them for migrations and
# bootstrap ONLY.
#
# Bootstrap tier: cobalt.db._open() composes its DSN from the environment
# before anything can open the vault. A copy lives in VaultManager as
# COBALT_DB_PASSWORD, which is what enrols it in F19's literal guard.
# Minted by ops/cobalt_app_role_provision.py — never edit by hand.
{user_key}={role}
{password_key}={password}
"""


def grant_memberships(conn) -> None:
    """`GRANT <side roles> TO cobalt_app`. Membership, not privilege:
    under NOINHERIT these are doors, not keys in a pocket."""
    with conn.cursor() as cur:
        cur.execute(
            sql.SQL("GRANT {roles} TO {role}").format(
                roles=sql.SQL(", ").join(sql.Identifier(r) for r in MEMBERSHIPS),
                role=sql.Identifier(ROLE),
            )
        )


def grant_connect(conn, dbname: str) -> None:
    with conn.cursor() as cur:
        cur.execute(
            sql.SQL("GRANT CONNECT ON DATABASE {db} TO {role}").format(
                db=sql.Identifier(dbname), role=sql.Identifier(ROLE)
            )
        )


def report_attributes(conn) -> None:
    """Print what the server says the role IS — never what we asked for.
    'Trust the artifact, never the report' applies to our own scripts."""
    with conn.cursor() as cur:
        cur.execute(
            "SELECT rolsuper, rolinherit, rolcreaterole, rolcreatedb, "
            "rolcanlogin, rolreplication, rolbypassrls "
            "FROM pg_roles WHERE rolname = %s",
            (ROLE,),
        )
        row = cur.fetchone()
    names = ("super", "inherit", "createrole", "createdb", "login", "replication", "bypassrls")
    print("  " + ", ".join(f"{n}={v}" for n, v in zip(names, row)))


def main() -> int:
    load_dotenv(pg_role.ENV_FILE)

    from cobalt import db  # the ONE connection factory (TRIAGE secrets law)

    pg_role.preflight_env((USER_KEY, PASSWORD_KEY))

    # BOOTSTRAP credential: CREATE ROLE and GRANT are superuser-class
    # acts, which is exactly what `connect_migration` is for. `postgres`
    # rather than a Cobalt database: a shared-catalog write belongs
    # nowhere in particular.
    with db.connect_migration("postgres") as conn:
        if pg_role.role_exists(conn, ROLE):
            raise ProvisionError(
                f"Role {ROLE!r} already exists in Postgres but .env holds no "
                "password for it. Resolve that by hand — do not guess."
            )

        password = pg_role.generate_password()
        pg_role.create_login_role(
            conn, ROLE, pg_role.scram_sha256_verifier(password), inherit=False
        )
        print(f"  role {ROLE!r} created (LOGIN NOINHERIT, no superuser/createdb/createrole)")
        report_attributes(conn)

        grant_memberships(conn)
        print(f"  membership granted: {', '.join(MEMBERSHIPS)}")

        grant_connect(conn, DEV_DATABASE)
        print(f"  CONNECT granted on {DEV_DATABASE} (and on NOTHING else — see the docstring)")

        pg_role.append_env_block(
            ENV_BLOCK.format(
                user_key=USER_KEY, role=ROLE, password_key=PASSWORD_KEY, password=password
            )
        )
        print(f"  .env: {USER_KEY} and {PASSWORD_KEY} written (mode 0600 preserved)")

        pg_role.store_in_vault(PASSWORD_KEY, password)
        print(f"  vault: stored as {PASSWORD_KEY} — F19 literal guard enrolment")

        pg_role.verify_login(ROLE, password)

        del password

    print(f"\n  {pg_role.LENGTH} characters, generated with secrets.choice, never printed.")
    print(
        "\n  NOT DONE HERE, by design (NN#16): "
        "GRANT CONNECT ON DATABASE cobalt_brain TO cobalt_app.\n"
        "  That is a LIVE step in the deploy plan; until it runs this role "
        "cannot reach production."
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ProvisionError as exc:
        print(f"REFUSED: {exc}", file=sys.stderr)
        sys.exit(1)
