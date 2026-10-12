"""`cobalt db apply` (card 2026-10-12 417, rows A1-A5): the one production DML verb.

Offline: the parser is pglast (libpg_query), no database. Every statement case goes through
`check_file`, the module's one entry; every command case goes through `command` with
`db.connect` replaced by a stub that raises `AssertionError("connected")`, so a refusal is
proved to come before the one connection opens. Every statement, table, file and hash here is
constructed.
"""

from __future__ import annotations

import argparse
import hashlib
import inspect
import json
import sys
from datetime import timedelta
from types import SimpleNamespace

import pytest

import cobalt.db_apply as db_apply
from cobalt.backup.restic import BackupError
from cobalt.db import Side
from cobalt.db_apply import ApplyRefused, check_file, split_statements

SOURCE = inspect.getsource(db_apply)
FILE = "2026-10-12/1-x-apply.sql"
SQL = b"UPDATE t SET a = 1;\n"


def refused(text: str, *want: str) -> str:
    with pytest.raises(ApplyRefused) as raised:
        check_file(text)
    msg = str(raised.value)
    for w in want:
        assert w in msg, msg
    return msg


# ---- A1 D1 refused at the top (r1), one per kind -----------------------------------------------

D1 = [
    ("CREATE INDEX i ON t (a)", "statement 1 refused: IndexStmt"),
    ("ALTER TABLE t ADD COLUMN y int", "statement 1 refused: AlterTableStmt"),
    ('DROP TABLE "user".t', "statement 1 refused: DropStmt"),
    ("TRUNCATE t", "statement 1 refused: TruncateStmt"),
    ("GRANT SELECT ON t TO cobalt_system", "statement 1 refused: GrantStmt"),
    ("REVOKE SELECT ON t FROM cobalt_user", "statement 1 refused: GrantStmt"),
    ("COMMENT ON TABLE t IS 'x'", "statement 1 refused: CommentStmt"),
    ("BEGIN", "statement 1 refused: TransactionStmt"),
    ("COMMIT", "statement 1 refused: TransactionStmt"),
    ("ROLLBACK", "statement 1 refused: TransactionStmt"),
    ("SAVEPOINT s", "statement 1 refused: TransactionStmt"),
    ("SET ROLE cobalt_system", "statement 1 refused: VariableSetStmt"),
    ("RESET ROLE", "statement 1 refused: VariableSetStmt"),
    ("SELECT 1", "statement 1 refused: SelectStmt"),
    ("SELECT set_config('a', 'b', false)", "statement 1 refused: SelectStmt"),
    ("DO $$ BEGIN END $$", "statement 1 refused: DoStmt"),
    ("CALL p()", "statement 1 refused: CallStmt"),
    ("COPY t FROM '/tmp/x'", "statement 1 refused: CopyStmt"),
    ("EXPLAIN ANALYZE DELETE FROM t", "statement 1 refused: ExplainStmt"),
    ("WITH x AS (SELECT 1) SELECT * FROM x", "statement 1 refused: SelectStmt"),
    # DDL hidden
    ("-- note\nDROP TABLE t", "statement 1 refused: DropStmt"),
    ("/* c */ alter table t add column y int", "statement 1 refused: AlterTableStmt"),
    ("UPDATE t SET a = 1; DROP TABLE t", "statement 2 refused: DropStmt"),
    ("UPDATE t SET a = 1;/* x */drop table t", "statement 2 refused: DropStmt"),
    ("UPDATE t SET a = 1; COMMIT", "statement 2 refused: TransactionStmt"),
]


@pytest.mark.parametrize("text,want", D1, ids=[t for t, _ in D1])
def test_d1_every_statement_that_is_not_dml_is_refused_at_the_top(text, want):
    refused(text, want, "is not INSERT, UPDATE, DELETE or MERGE")


# ---- A1 D2 does not parse, or no statement -----------------------------------------------------

D2 = [
    ("FROBNICATE t", "does not parse: "),
    ("/* open", "does not parse: "),
    ("UPDATE t SET a = 'open", "does not parse: "),
    ("", "no statement"),
    ("-- only a comment", "no statement"),
]


@pytest.mark.parametrize("text,want", D2, ids=["frobnicate", "open comment", "open literal", "empty", "comment"])
def test_d2_a_text_that_does_not_parse_or_holds_no_statement_is_refused(text, want):
    refused(text, want)


# ---- A1 D3 pass, one piece each ----------------------------------------------------------------

D3 = [
    "UPDATE t SET a = '; DROP TABLE t'",
    "UPDATE t SET a = $$;DROP TABLE t$$",
    "INSERT INTO t (a) VALUES (1) -- DROP TABLE t",
    "DELETE FROM t WHERE a = 1",
    "MERGE INTO t USING s ON t.a = s.a WHEN MATCHED THEN UPDATE SET b = s.b",
    "UPDATE t SET a = '-- x; /* y'",
    'UPDATE "t--x" SET a = 1',
    "UPDATE t SET a = $tag$;DROP TABLE t$tag$",
    "UPDATE t SET a = 'é'",
    "UPDATE t SET a = U&'x'",
    "WITH d AS (DELETE FROM t RETURNING a) UPDATE u SET a = 0 WHERE a IN (SELECT a FROM d)",
    "WITH d AS (DELETE FROM t RETURNING a) INSERT INTO u SELECT a FROM d",
    "WITH d AS (DELETE FROM t RETURNING a) SELECT a FROM d",
]


@pytest.mark.parametrize("text", D3)
def test_d3_dml_passes_as_one_piece(text):
    pieces = check_file(text)
    assert pieces == [text], pieces


# ---- A1 D4 the allowlist edges -----------------------------------------------------------------

@pytest.mark.parametrize("text", [
    "UPDATE t SET b = now() WHERE a = 1",
    "INSERT INTO t (a, b) VALUES (1, now()) RETURNING now()",
])
def test_d4_now_is_the_one_function_that_passes(text):
    assert len(check_file(text)) == 1


D4 = [
    ("UPDATE t SET b = now() WHERE a IN (SELECT a FROM u WHERE c = upper('x'))", "upper"),
    ("UPDATE t SET b = coalesce(lower('X'), 'y')", "lower"),
    ("WITH d AS (SELECT set_config('role', 'cobalt_system', false) AS x) UPDATE t SET a = 1 FROM d", "set_config"),
    ("UPDATE t SET a = 1 RETURNING pg_terminate_backend(1)", "pg_terminate_backend"),
    ("UPDATE t SET b = pg_catalog.now()", "pg_catalog.now"),
    ("UPDATE t SET a = 1 WHERE pg_sleep(100) IS NULL", "pg_sleep"),
    ("INSERT INTO t SELECT * FROM dblink('x', 'select 1') AS r(a int)", "dblink"),
]


@pytest.mark.parametrize("text,name", D4, ids=[n for _, n in D4])
def test_d4_a_function_off_the_list_is_refused_wherever_it_sits(text, name):
    refused(text, f"statement 1 refused: function {name} is not on the apply list")


# ---- A1 D5 the old holes, red against the new rules --------------------------------------------

INTO = "statement 1 refused: SELECT … INTO creates a table"
TOP2 = "statement 2 refused: DropStmt"


def fn(name: str) -> str:
    return f"statement 1 refused: function {name} is not on the apply list"


D5 = [
    ("WITH d AS (DELETE FROM t RETURNING a) SELECT a INTO u FROM d", INTO),
    ("WITH d AS (DELETE FROM t RETURNING 1 AS insert) SELECT insert INTO u FROM d", INTO),
    ("UPDATE t SET a = \"set_config\"('role', 'cobalt_system', false)", fn("set_config")),
    ('UPDATE t SET a = "pg_terminate_backend"(1)', fn("pg_terminate_backend")),
    ("UPDATE t SET a = pg_catalog.\"SET_CONFIG\"('a', 'b', false)", fn("pg_catalog.SET_CONFIG")),
    ('UPDATE t SET a = "pg_advisory_lock"(1)', fn("pg_advisory_lock")),
    ("UPDATE t SET a = '\"' AND \"set_config\"('a', 'b', false) = '\"'", fn("set_config")),
    ("UPDATE t SET a = E'\\''; DROP TABLE t; -- '", TOP2),
    ("UPDATE t SET a = 1 -- x" + "\r" + "; DROP TABLE t", TOP2),
    ("UPDATE t SET a = $é$ ' $é$; DROP TABLE t; -- '", TOP2),
    ("UPDATE t AS aé$b$ SET a = 1; DROP TABLE t; UPDATE t AS aé$b$ SET a = 1", TOP2),
    ("UPDATE t SET a = U&\"\\0073et_config\"('a', 'b', false)", fn("set_config")),
    ("UPDATE t SET a = U&\"!0073et_config\" UESCAPE '!' ('a', 'b', false)", fn("set_config")),
    ("/* /* */ UPDATE t SET a = 1 */ DROP TABLE t", "statement 1 refused: DropStmt"),
    ("UPDATE t SET a = query_to_xml('select set_config(''role'', ''cobalt_system'', false)', true, true, '')::text",
     fn("query_to_xml")),
]


@pytest.mark.parametrize("text,want", D5, ids=[f"d5-{i}" for i in range(len(D5))])
def test_d5_the_old_holes_are_refused_by_the_tree(text, want):
    refused(text, want)


# ---- A1 D6 the split, by byte offsets ----------------------------------------------------------

def test_d6_two_statements_split_into_two_pieces_without_their_semicolons():
    pieces = split_statements("UPDATE t SET a = 1;\n\nINSERT INTO t VALUES (2);\n")
    assert [p.strip() for p in pieces] == ["UPDATE t SET a = 1", "INSERT INTO t VALUES (2)"], pieces
    assert not any(";" in p for p in pieces), pieces


def test_d6_offsets_count_bytes_not_characters():
    assert split_statements("UPDATE t SET a = 'é';UPDATE t SET b = 1")[1].strip() == "UPDATE t SET b = 1"


# ---- A1 D7 the constants -----------------------------------------------------------------------

def test_d7_the_list_is_now_alone_and_the_grammar_is_postgres_16():
    from pglast import parser as pg_parser

    assert db_apply.ALLOWED_FUNCTIONS == frozenset({("now",)})
    assert db_apply.PARSER_PG_MAJOR == 16
    assert json.loads(pg_parser.parse_sql_json("SELECT 1"))["version"] // 10000 == 16
    assert "db_query" not in SOURCE


# ---- A2 the file and its hash, before any connection -------------------------------------------

def never_connect(*_a, **_k):
    raise AssertionError("connected")


@pytest.fixture
def prompts(tmp_path, monkeypatch):
    monkeypatch.setattr(db_apply, "PROMPTS_ROOT", tmp_path)
    monkeypatch.setattr(db_apply.db, "connect", never_connect)
    monkeypatch.setenv("COBALT_ENV", "dev")
    (tmp_path / "2026-10-12").mkdir()
    (tmp_path / FILE).write_bytes(SQL)
    return tmp_path


def args(file: str = FILE, *, sha: str | None = None, side: str = "user", prod: bool = False,
         raw: bytes = SQL) -> argparse.Namespace:
    return argparse.Namespace(file=file, sha256=sha or hashlib.sha256(raw).hexdigest(), side=side, prod=prod)


def exit_of(ns: argparse.Namespace) -> int:
    with pytest.raises(SystemExit) as raised:
        db_apply.command(ns)
    return raised.value.code


def test_h0_negative_control_a_good_file_reaches_the_connection(prompts):
    with pytest.raises(AssertionError, match="connected"):
        db_apply.command(args())


def test_h1_a_file_changed_after_its_hash_is_refused_before_connecting(prompts, capsys):
    want = hashlib.sha256(SQL).hexdigest()
    (prompts / FILE).write_bytes(SQL.replace(b"1", b"2"))
    assert exit_of(args(sha=want)) == 2
    err = capsys.readouterr().err
    assert "REFUSED: sha256 " in err and f"is not the approved {want}" in err and "nothing opened" in err, err


H2 = {
    "dotdot": dict(file="../x-apply.sql"),
    "no apply": dict(file="2026-10-12/1-x.sql"),
    "space": dict(file="2026-10-12/1-x y-apply.sql"),
    "absolute": dict(file="/abs/2026-10-12/1-x-apply.sql"),
    "absent": dict(file="2026-10-12/2-y-apply.sql"),
    "63 hex": dict(sha="a" * 63),
    "upper hex": dict(sha=hashlib.sha256(SQL).hexdigest().upper()),
}


@pytest.mark.parametrize("case", list(H2))
def test_h2_a_bad_argument_is_refused_before_connecting(prompts, capsys, case):
    assert exit_of(args(**H2[case])) == 2
    err = capsys.readouterr().err
    assert err.startswith("REFUSED: ") and "nothing opened" in err, err


def test_h3_a_file_that_is_not_utf8_is_refused(prompts, capsys):
    raw = b"UPDATE t SET a = '\xff';\n"
    (prompts / FILE).write_bytes(raw)
    assert exit_of(args(raw=raw)) == 2
    assert "REFUSED: " in capsys.readouterr().err


def test_a_refused_statement_is_refused_before_connecting(prompts, capsys):
    raw = b"UPDATE t SET a = 1; DROP TABLE t;\n"
    (prompts / FILE).write_bytes(raw)
    assert exit_of(args(raw=raw)) == 2
    assert "statement 2 refused: DropStmt" in capsys.readouterr().err


# ---- A3 the backup line, with --prod only ------------------------------------------------------

def armed(enabled: bool = True, destinations: int = 1):
    return SimpleNamespace(database=SimpleNamespace(enabled=enabled), armed=[object()] * destinations)


@pytest.fixture
def prod(prompts, monkeypatch):
    monkeypatch.setenv("COBALT_ENV", "production")
    monkeypatch.setattr(db_apply, "load_backup_config", lambda *a, **k: armed())
    return monkeypatch


def age(seconds):
    return lambda *a, **k: None if seconds is None else timedelta(seconds=seconds)


def test_b1_no_database_dump_is_refused(prod, capsys):
    prod.setattr(db_apply, "load_backup_config", lambda *a, **k: armed(enabled=False))
    prod.setattr(db_apply, "latest_snapshot_age", age(1))
    assert exit_of(args(prod=True)) == 2
    assert "REFUSED: backup — no database dump armed" in capsys.readouterr().err


def test_b1_no_armed_destination_is_refused(prod, capsys):
    prod.setattr(db_apply, "load_backup_config", lambda *a, **k: armed(destinations=0))
    prod.setattr(db_apply, "latest_snapshot_age", age(1))
    assert exit_of(args(prod=True)) == 2
    assert "REFUSED: backup — no database dump armed" in capsys.readouterr().err


def test_b2_no_snapshot_is_refused(prod, capsys):
    prod.setattr(db_apply, "latest_snapshot_age", age(None))
    assert exit_of(args(prod=True)) == 2
    assert "REFUSED: backup — no snapshot" in capsys.readouterr().err


def test_b3_a_snapshot_over_the_bound_is_refused_naming_both_numbers(prod, capsys):
    over = db_apply.BACKUP_MAX_AGE_S + 1
    prod.setattr(db_apply, "latest_snapshot_age", age(over))
    assert exit_of(args(prod=True)) == 2
    err = capsys.readouterr().err
    assert f"newest snapshot {over} s old, over BACKUP_MAX_AGE_S {db_apply.BACKUP_MAX_AGE_S} s" in err, err


def test_b4_an_unmounted_destination_is_refused_with_its_message(prod, capsys):
    def raising(*_a, **_k):
        raise BackupError("ssd: /Volumes/x is not mounted (constructed)")
    prod.setattr(db_apply, "latest_snapshot_age", raising)
    assert exit_of(args(prod=True)) == 2
    assert "ssd: /Volumes/x is not mounted (constructed)" in capsys.readouterr().err


def test_b5_prod_without_cobalt_env_is_refused_before_the_backup_is_read(prompts, monkeypatch, capsys):
    monkeypatch.delenv("COBALT_ENV", raising=False)
    monkeypatch.setattr(db_apply, "load_backup_config", never_connect)
    monkeypatch.setattr(db_apply, "latest_snapshot_age", never_connect)
    assert exit_of(args(prod=True)) == 2
    assert "REFUSED: " in capsys.readouterr().err


def test_b6_a_fresh_snapshot_passes_to_the_connection(prod, capsys):
    prod.setattr(db_apply, "latest_snapshot_age", age(db_apply.BACKUP_MAX_AGE_S - 1))
    with pytest.raises(AssertionError, match="connected"):
        db_apply.command(args(prod=True))
    out = capsys.readouterr().out
    assert f"backup: newest snapshot {db_apply.BACKUP_MAX_AGE_S - 1} s old (bound {db_apply.BACKUP_MAX_AGE_S} s)" in out


def test_b6_without_prod_the_backup_is_not_checked(prompts, capsys):
    with pytest.raises(AssertionError, match="connected"):
        db_apply.command(args())
    assert "backup: not checked (not --prod)" in capsys.readouterr().out


def test_b7_the_bound_is_a_constant_never_a_tunable():
    assert db_apply.BACKUP_MAX_AGE_S == 900
    assert "load_tunables" not in SOURCE


# ---- A4 one transaction, each statement echoed with its row count ------------------------------

class FakeCursor:
    def __init__(self, row=None, rowcount=-1):
        self.row = row
        self.rowcount = rowcount

    def fetchone(self):
        return self.row


class FakeConn:
    """Records every call; statement `fail_at` (1-based) raises."""

    def __init__(self, *, role="cobalt_user", version="160004", fail_at=None):
        self.role, self.version, self.fail_at = role, version, fail_at
        self.autocommit = True
        self.events: list = []
        self.sent = 0

    def execute(self, query, params=None, **kw):
        q = str(query)
        self.events.append(("execute", q, kw))
        if q == "SHOW server_version_num":
            return FakeCursor((self.version,))
        if q == "SELECT current_user":
            return FakeCursor((self.role,))
        if q.startswith("SET LOCAL "):
            return FakeCursor()
        self.sent += 1
        if self.sent == self.fail_at:
            raise RuntimeError("constructed failure")
        return FakeCursor(rowcount=self.sent)

    def commit(self):
        self.events.append(("commit",))

    def rollback(self):
        self.events.append(("rollback",))

    def close(self):
        self.events.append(("close",))

    def statements(self):
        return [e for e in self.events if e[0] == "execute" and e[2].get("prepare")]


THREE = ["UPDATE t SET a = 1", "UPDATE t SET a = 2", "UPDATE t SET a = 3"]


def run(conn, statements=THREE, side=Side.USER):
    return db_apply.apply_statements(conn, statements, side=side)


def test_t1_a_failing_statement_rolls_back_and_stops(capsys):
    conn = FakeConn(fail_at=2)
    assert run(conn) == 1
    out = capsys.readouterr()
    text = out.out + out.err
    for want in ("STATEMENT 1/3", "ROWS 1:", "STATEMENT 2/3", "FAILED at statement 2", "ROLLED BACK"):
        assert want in text, (want, text)
    assert "STATEMENT 3/3" not in text
    assert ("commit",) not in conn.events
    assert ("rollback",) in conn.events


def test_t2_all_pass_commit_once_after_the_last(capsys):
    conn = FakeConn()
    assert run(conn) == 0
    names = [e[0] for e in conn.events]
    assert names.count("commit") == 1
    last_statement = max(i for i, e in enumerate(conn.events) if e[0] == "execute")
    assert names.index("commit") > last_statement
    assert "COMMITTED · statements: 3 · rows: 6" in capsys.readouterr().out


def test_t3_a_session_not_on_the_side_role_sends_no_statement(capsys):
    conn = FakeConn(role="postgres")
    assert run(conn) == 1
    assert conn.sent == 0
    assert ("commit",) not in conn.events


def test_t7_the_preamble_runs_in_order_and_every_statement_is_prepared():
    conn = FakeConn()
    run(conn)
    executed = [e[1] for e in conn.events if e[0] == "execute"]
    assert executed[:4] == [
        "SET LOCAL statement_timeout = '60s'",
        "SET LOCAL lock_timeout = '5s'",
        "SHOW server_version_num",
        "SELECT current_user",
    ], executed
    assert [e[1] for e in conn.statements()] == THREE
    assert all(e[2] == {"prepare": True} for e in conn.events if e[0] == "execute" and e[1] in THREE)
    assert conn.autocommit is False


def test_t8_a_server_of_another_major_sends_no_statement(capsys):
    conn = FakeConn(version="170002")
    assert run(conn) == 1
    assert conn.sent == 0
    assert ("rollback",) in conn.events
    out = capsys.readouterr()
    assert "FAILED: server is Postgres 17, the parser reads 16 — ROLLED BACK" in out.out + out.err


SENTINELS = ("sentinel-pg-pw-0417", "sentinel-app-pw-0417")


def test_t4_no_secret_reaches_the_output(monkeypatch, capsys):
    monkeypatch.setenv("POSTGRES_PASSWORD", SENTINELS[0])
    monkeypatch.setenv("COBALT_DB_PASSWORD", SENTINELS[1])
    run(FakeConn(fail_at=2))
    run(FakeConn())
    out = capsys.readouterr()
    for s in SENTINELS:
        assert s not in out.out and s not in out.err
    for word in ("psycopg.connect", "os.getenv", "os.environ", ".env"):
        assert word not in SOURCE, word


# ---- A5 the verb -------------------------------------------------------------------------------

HEX = "0" * 64


class Parsed(Exception):
    pass


def parse_cli(monkeypatch, argv: list[str]) -> argparse.Namespace:
    from cobalt import cli

    seen = {}
    real = argparse.ArgumentParser.parse_args

    def capture(self, *a, **k):
        seen["ns"] = real(self, *a, **k)
        raise Parsed

    monkeypatch.setattr(argparse.ArgumentParser, "parse_args", capture)
    monkeypatch.setattr(sys, "argv", ["cobalt", *argv])
    with pytest.raises(Parsed):
        cli.main()
    return seen["ns"]


def test_v1_the_cli_parses_db_apply_to_its_command(monkeypatch):
    ns = parse_cli(monkeypatch, ["db", "apply", "--side", "user", "--prod", "--sha256", HEX, FILE])
    assert ns.func is db_apply.command
    assert (ns.side, ns.prod, ns.sha256, ns.file) == ("user", True, HEX, FILE)


@pytest.mark.parametrize("drop", ["--side", "--sha256"])
def test_v2_side_and_sha256_are_required(monkeypatch, drop):
    argv = ["db", "apply", "--side", "user", "--sha256", HEX, FILE]
    i = argv.index(drop)
    del argv[i:i + 2]
    with pytest.raises(SystemExit) as raised:
        parse_cli(monkeypatch, argv)
    assert raised.value.code == 2


def test_v3_there_is_no_ddl_flag(monkeypatch):
    with pytest.raises(SystemExit) as raised:
        parse_cli(monkeypatch, ["db", "apply", "--side", "user", "--sha256", HEX, "--ddl", "yes", FILE])
    assert raised.value.code == 2
