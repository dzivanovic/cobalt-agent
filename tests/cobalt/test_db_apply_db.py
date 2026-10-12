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


E2E = {
    # (a) one refused statement
    "a": (f"DROP TABLE {T}\n", 2, ["REFUSED: statement 1 refused: DropStmt"], None),
    # (b) a refused statement after an allowed one: nothing is sent
    "b": (f"{BUMP};\nDROP TABLE {T}\n", 2, ["REFUSED: statement 2 refused: DropStmt"], None),
    # (c) an allowed file: one transaction, row counts echoed
    "c": (f"{BUMP};\nINSERT INTO {T} VALUES (4, 1)\n", 0,
          ["ROWS 1: 3", "ROWS 2: 1", "COMMITTED · statements: 2 · rows: 4"],
          [(1, 11), (2, 21), (3, 31), (4, 1)]),
}


@requires_db
@pytest.mark.parametrize("case", list(E2E))
def test_command_end_to_end_checks_the_whole_file_before_any_statement_runs(scratch, tmp_path, monkeypatch, capsys, case):
    """A7: `command` through db.connect → the allowlist → apply_statements on cobalt_dev."""
    import argparse
    import hashlib

    import cobalt.db_apply as db_apply

    text, code, wants, after = E2E[case]
    name = "2026-10-12/1-e2e-apply.sql"
    (tmp_path / "2026-10-12").mkdir()
    (tmp_path / name).write_bytes(text.encode())
    monkeypatch.setattr(db_apply, "PROMPTS_ROOT", tmp_path)
    monkeypatch.setenv("COBALT_ENV", "dev")
    ns = argparse.Namespace(file=name, sha256=hashlib.sha256(text.encode()).hexdigest(), side="user", prod=False)
    before = rows()
    if code:
        with pytest.raises(SystemExit) as raised:
            db_apply.command(ns)
        assert raised.value.code == code
    else:
        db_apply.command(ns)
    out = capsys.readouterr()
    text_out = out.out + out.err
    for want in wants:
        assert want in text_out, (want, text_out)
    if code:
        assert "STATEMENT 1/" not in text_out, text_out
        assert rows() == before
    else:
        assert rows() == after


@requires_db
def test_t9_the_server_refuses_two_commands_in_one_prepared_piece(scratch, capsys):
    assert apply([f"{BUMP}; {BUMP}"]) == 1
    out = capsys.readouterr().out
    assert "FAILED at statement 1" in out and "ROLLED BACK" in out, out
    assert rows() == BEFORE
