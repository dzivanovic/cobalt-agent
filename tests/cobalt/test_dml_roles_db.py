"""Migration 0025 `dml_roles` with-DB (card 2026-10-13 448 G1): what the apply roles may and
may not do, read from `cobalt_dev`'s catalog at `0025`.

Every read goes through the one migration factory (`db.connect_migration(env.DEV_DB_NAME)`,
as `test_db_apply_db.py` opens it), closed in a `finally`; nothing is committed. G1f and G1g
change the catalog only inside one transaction that is rolled back. A later side table
without its grant fails G1b (the CARD.md migration checklist, card 448 C1).
"""

from __future__ import annotations

import os

import pytest
from psycopg import sql

from cobalt import db, env
from cobalt.db_migrations import MIGRATIONS_DIR

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

SQL = MIGRATIONS_DIR / "0025_dml_roles.sql"
ROLLBACK = MIGRATIONS_DIR / "0025_dml_roles.rollback.sql"

#: (apply role, its own schema, the other side's schema)
SIDES = [("cobalt_apply_user", "user", "system"), ("cobalt_apply_system", "system", "user")]

ALLOWED = ("SELECT", "INSERT", "UPDATE", "DELETE")
NEVER = ("TRUNCATE", "REFERENCES", "TRIGGER")


@pytest.fixture
def conn():
    c = db.connect_migration(env.DEV_DB_NAME)
    try:
        yield c
    finally:
        c.rollback()
        c.close()


def one(conn, query, params=()):
    return conn.execute(query, params).fetchone()[0]


def relations(conn, schema: str, kinds: tuple[str, ...]) -> list[tuple[int, str, str]]:
    return conn.execute(
        "SELECT c.oid, c.relname, pg_get_userbyid(c.relowner) FROM pg_class c "
        "JOIN pg_namespace n ON n.oid = c.relnamespace "
        "WHERE n.nspname = %s AND c.relkind = ANY(%s) ORDER BY c.relname",
        (schema, list(kinds)),
    ).fetchall()


def door(conn, role: str) -> list[tuple]:
    return conn.execute(
        "SELECT m.set_option FROM pg_auth_members m "
        "JOIN pg_roles r ON r.oid = m.roleid JOIN pg_roles u ON u.oid = m.member "
        "WHERE r.rolname = %s AND u.rolname = %s",
        (role, db.APP_ROLE),
    ).fetchall()


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1a_the_role_is_nologin_powerless_and_a_member_of_nothing(conn, role, schema, other):
    rows = conn.execute(
        "SELECT rolcanlogin, rolsuper, rolcreatedb, rolcreaterole, rolbypassrls, rolinherit "
        "FROM pg_roles WHERE rolname = %s",
        (role,),
    ).fetchall()
    assert len(rows) == 1, rows
    assert tuple(rows[0]) == (False,) * 6, rows[0]
    memberships = one(
        conn,
        "SELECT count(*) FROM pg_auth_members m JOIN pg_roles r ON r.oid = m.member "
        "WHERE r.rolname = %s",
        (role,),
    )
    assert memberships == 0


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1b_every_relation_of_its_schema_is_dml_only_and_not_owned(conn, role, schema, other):
    tables = relations(conn, schema, ("r", "p", "v", "m", "f"))
    assert tables, schema
    for oid, name, owner in tables:
        for priv in ALLOWED:
            assert one(conn, "SELECT has_table_privilege(%s::name, %s::oid, %s::text)", (role, oid, priv)), (
                f"{schema}.{name}: {role} lacks {priv}")
        for priv in NEVER:
            assert not one(conn, "SELECT has_table_privilege(%s::name, %s::oid, %s::text)", (role, oid, priv)), (
                f"{schema}.{name}: {role} holds {priv}")
        assert owner != role, f"{schema}.{name} is owned by {role}"


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1c_usage_on_its_own_schema_only_and_never_create(conn, role, schema, other):
    assert one(conn, "SELECT has_schema_privilege(%s::name, %s::text, 'USAGE')", (role, schema))
    assert not one(conn, "SELECT has_schema_privilege(%s::name, %s::text, 'CREATE')", (role, schema))
    assert not one(conn, "SELECT has_schema_privilege(%s::name, %s::text, 'USAGE')", (role, other))


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1d_every_sequence_of_its_schema_has_usage(conn, role, schema, other):
    sequences = relations(conn, schema, ("S",))
    assert sequences, schema
    for oid, name, _ in sequences:
        assert one(conn, "SELECT has_sequence_privilege(%s::name, %s::oid, 'USAGE')", (role, oid)), (
            f"{schema}.{name}: {role} lacks USAGE")


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1e_the_door_cobalt_app_may_set_role(conn, role, schema, other):
    rows = door(conn, role)
    assert rows, f"no pg_auth_members row from {role} to {db.APP_ROLE}"
    assert [tuple(r) for r in rows] == [(True,)], rows


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1f_a_table_the_side_role_creates_later_gets_the_grant(conn, role, schema, other):
    table = sql.SQL("{}.zz_dml_roles_default").format(sql.Identifier(schema))
    conn.autocommit = False
    try:
        conn.execute(sql.SQL("SET LOCAL ROLE {}").format(sql.Identifier(f"cobalt_{schema}")))
        conn.execute(sql.SQL("CREATE TABLE {} (id int)").format(table))
        name = table.as_string(conn)
        assert one(conn, "SELECT has_table_privilege(%s::name, %s::text, 'UPDATE')", (role, name))
    finally:
        conn.rollback()


@requires_db
def test_g1g_the_rollback_revokes_the_grants_and_keeps_the_role_and_the_door(conn):
    traders = '"user".traders'
    conn.autocommit = False
    try:
        conn.execute(ROLLBACK.read_text())
        assert not one(conn, "SELECT has_table_privilege('cobalt_apply_user', %s::text, 'UPDATE')", (traders,))
        assert one(conn, "SELECT count(*) FROM pg_roles WHERE rolname = 'cobalt_apply_user'") == 1
        assert door(conn, "cobalt_apply_user"), "the rollback revoked the door"
        conn.execute(SQL.read_text())
        assert one(conn, "SELECT has_table_privilege('cobalt_apply_user', %s::text, 'UPDATE')", (traders,))
    finally:
        conn.rollback()


@requires_db
@pytest.mark.parametrize("role,schema,other", SIDES)
def test_g1h_default_privileges_are_dml_only(conn, role, schema, other):
    rows = conn.execute(
        "SELECT d.defaclobjtype, x::text FROM pg_default_acl d "
        "JOIN pg_namespace n ON n.oid = d.defaclnamespace "
        "CROSS JOIN LATERAL unnest(d.defaclacl) AS x "
        "WHERE n.nspname = %s AND x::text LIKE %s",
        (schema, f"{role}=%"),
    ).fetchall()
    assert rows, f"no pg_default_acl entry names {role} in {schema}"
    want = {"r": "arwd", "S": "U"}
    for kind, item in rows:
        letters = item.split("=", 1)[1].split("/", 1)[0]
        assert letters == want.get(kind), f"{schema}: {kind} {item}"
    kinds = sorted(kind for kind, _ in rows)
    # one pair per FOR ROLE of 0025 (4): the side role and the migration login
    assert kinds == ["S", "S", "r", "r"], rows
