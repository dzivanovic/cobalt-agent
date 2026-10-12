"""`cobalt db apply` A4 with-DB (card 2026-10-12 417): one transaction on `cobalt_dev`.

The scratch table `"user".zz_db_apply_scratch` is built through the one migration factory
(`db.connect_migration(env.DEV_DB_NAME)`), COMMITTED so a second connection can read it, and
dropped in a `finally` (no stray table). `apply_statements` runs over `db.connect` on the user
side, as the verb does; a SECOND connection reads the rows back, so a rollback is proved across
sessions. Every table, row and value is constructed.

Every connection here is the REAL factory, never the suite's savepoint proxy:
`dev_db_tx` (conftest) patches `db.connect` to one shared connection whose
transaction stays open to the end of the test, so a commit there is no commit,
a "second connection" is the same session, and the table locks it takes block
the fixture's `DROP TABLE` until that transaction ends — after the teardown
that waits for it (the hang of the first A7 run).
"""

from __future__ import annotations

import os
import threading

import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_apply import apply_statements

#: The UNPATCHED factory, bound at import (the `test_fill_transaction_db.py`
#: precedent): `dev_db_tx` patches `db.connect` per test, and collection runs before it.
REAL_CONNECT = db.connect

#: A7's fence: `command` runs in a daemon thread joined this long; a thread
#: still alive is a hang, and the test fails red instead of stalling.
HANG_S = 120

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
        c.execute("SET lock_timeout = '30s'")  # a lock wait fails loud, never hangs the run
        c.execute(f"DROP TABLE IF EXISTS {T}")
        c.execute(f"CREATE TABLE {T} (id int PRIMARY KEY, qty int NOT NULL)")
        c.execute(f"INSERT INTO {T} VALUES (1, 10), (2, 20), (3, 30)")
        c.execute(f"GRANT SELECT, INSERT, UPDATE ON {T} TO cobalt_user")
        yield
    finally:
        c.execute(f"DROP TABLE IF EXISTS {T}")
        c.close()


def rows() -> list[tuple[int, int]]:
    """The table as a separate autocommit session reads it; closed before it returns."""
    c = REAL_CONNECT(env.DEV_DB_NAME, side=Side.USER)
    try:
        return [tuple(r) for r in c.execute(f"SELECT id, qty FROM {T} ORDER BY id").fetchall()]
    finally:
        c.close()


def apply(statements: list[str]) -> int:
    return apply_statements(REAL_CONNECT(env.DEV_DB_NAME, side=Side.USER), statements, side=Side.USER)


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
    monkeypatch.setattr(db, "connect", REAL_CONNECT)  # the verb's own factory, not the suite's proxy
    monkeypatch.setenv("COBALT_ENV", "dev")
    ns = argparse.Namespace(file=name, sha256=hashlib.sha256(text.encode()).hexdigest(), side="user", prod=False)
    before = rows()
    result: dict = {}

    def run() -> None:
        try:
            db_apply.command(ns)
            result["code"] = 0
        except SystemExit as e:
            result["code"] = e.code
        except BaseException as e:  # noqa: BLE001 — carried to the test thread
            result["error"] = e

    thread = threading.Thread(target=run, daemon=True)
    thread.start()
    thread.join(HANG_S)
    assert not thread.is_alive(), f"command still running after {HANG_S} s: a hang"
    if "error" in result:
        raise result["error"]
    assert result["code"] == code
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
