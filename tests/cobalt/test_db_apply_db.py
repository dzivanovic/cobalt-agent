"""`cobalt db apply` A4 with-DB (card 2026-10-12 417): one transaction on `cobalt_dev`.

The scratch table `"user".zz_db_apply_scratch` is built through the one migration factory
(`db.connect_migration(env.DEV_DB_NAME)`), COMMITTED so a second connection can read it, and
dropped in a `finally` (no stray table). `apply_statements` runs over `db.connect` on the user
side, as the verb does; a SECOND connection reads the rows back, so a rollback is proved across
sessions. Every table, row and value is constructed.
"""

from __future__ import annotations

import os

import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_apply import apply_statements

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

T = '"user".zz_db_apply_scratch'
BUMP = f"UPDATE {T} SET qty = qty + 1"
BEFORE = [(1, 10), (2, 20), (3, 30)]


@pytest.fixture
def scratch():
    c = db.connect_migration(env.DEV_DB_NAME)
    try:
        c.execute(f"DROP TABLE IF EXISTS {T}")
        c.execute(f"CREATE TABLE {T} (id int PRIMARY KEY, qty int NOT NULL)")
        c.execute(f"INSERT INTO {T} VALUES (1, 10), (2, 20), (3, 30)")
        c.execute(f"GRANT SELECT, INSERT, UPDATE ON {T} TO cobalt_user")
        yield
    finally:
        c.execute(f"DROP TABLE IF EXISTS {T}")
        c.close()


def rows() -> list[tuple[int, int]]:
    c = db.connect(env.DEV_DB_NAME, side=Side.USER)
    try:
        return [tuple(r) for r in c.execute(f"SELECT id, qty FROM {T} ORDER BY id").fetchall()]
    finally:
        c.close()


def apply(statements: list[str]) -> int:
    return apply_statements(db.connect(env.DEV_DB_NAME, side=Side.USER), statements, side=Side.USER)


@requires_db
def test_t5_a_failing_second_statement_rolls_the_first_back(scratch, capsys):
    assert apply([BUMP, 'INSERT INTO "user".zz_db_apply_absent VALUES (1)']) == 1
    out = capsys.readouterr().out
    assert "ROWS 1: 3" in out and "FAILED at statement 2" in out and "ROLLED BACK" in out, out
    assert rows() == BEFORE


@requires_db
def test_t6_both_statements_commit_together(scratch, capsys):
    assert apply([BUMP, f"INSERT INTO {T} VALUES (4, 1)"]) == 0
    out = capsys.readouterr().out
    assert "ROWS 1: 3" in out and "ROWS 2: 1" in out, out
    assert "COMMITTED · statements: 2 · rows: 4" in out, out
    assert rows() == [(1, 11), (2, 21), (3, 31), (4, 1)]


@requires_db
def test_t9_the_server_refuses_two_commands_in_one_prepared_piece(scratch, capsys):
    assert apply([f"{BUMP}; {BUMP}"]) == 1
    out = capsys.readouterr().out
    assert "FAILED at statement 1" in out and "ROLLED BACK" in out, out
    assert rows() == BEFORE
