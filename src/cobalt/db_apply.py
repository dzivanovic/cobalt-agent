"""`cobalt db apply` — one approved DML file, one transaction (card 2026-10-12 417).

    cobalt db apply --side {user,system} [--prod] --sha256 <hex> <date>/<nn>-<name>-apply.sql

The file sits beside the card that approves it, under `PROMPTS_ROOT`; its
bytes are read once and must hash to `--sha256`, so the hash binds what
runs. In order, nothing opened until the last step:

  A2  the argument, the file and its hash;
  A1  the statement rule — an allowlist on Postgres's own parse tree
      (pglast, libpg_query), never on words: INSERT, UPDATE, DELETE or
      MERGE only (a SELECT only when one of its CTEs writes), no SELECT …
      INTO, no function off `ALLOWED_FUNCTIONS`. Every DDL statement,
      transaction control, SET, DO, CALL, COPY and EXPLAIN is refused; a
      schema change is a `db migrate` card;
  A3  with `--prod`, the newest backup snapshot no older than
      `BACKUP_MAX_AGE_S`;
  A4  ONE transaction on the side's own role, every statement echoed with
      its row count, each sent through the extended protocol (one command
      per piece), a commit after the last or a rollback on any failure.

Every refusal is `REFUSED: … — nothing opened` on stderr, exit 2.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from typing import Any

from pglast import parser as pg_parser

from cobalt import db, env
from cobalt.backup.config import load_backup_config
from cobalt.backup.restic import latest_snapshot_age
from cobalt.db import Side
from cobalt.db_migrations.cli import CODE_ROOT

#: The grammar the parser reads: pglast 7 is libpg_query's Postgres 17.
PARSER_PG_MAJOR = 17

#: The server the allowlist was proved against (`docker-compose.yml`
#: `pgvector/pgvector:pg16`). The PG17 grammar parses every PG16 DML
#: statement the allowlist admits; a statement PG16 refuses fails at the
#: server inside the one transaction and rolls back.
SERVER_PG_MAJOR = 16

#: The functions a statement may call, each by its FULL name as the parser
#: gives it. `now` is the house's `updated_at = now()`; a new entry is a
#: one-line card.
ALLOWED_FUNCTIONS = frozenset({("now",)})

#: The newest backup snapshot may be at most this old with `--prod` (brain
#: 2026-10-12, ask 5: a constant, never a tunable).
BACKUP_MAX_AGE_S = 900

STATEMENT_TIMEOUT = "60s"
LOCK_TIMEOUT = "5s"

#: Where an apply file lives: beside the card that approves it.
PROMPTS_ROOT = CODE_ROOT / "docs" / "40 - DevDocs" / "prompts"

_FILE = re.compile(r"20[0-9]{2}-[0-9]{2}-[0-9]{2}/[0-9]+-[a-z0-9-]+-apply\.sql")
_SHA256 = re.compile(r"[0-9a-f]{64}")

_WRITES = frozenset({"InsertStmt", "UpdateStmt", "DeleteStmt", "MergeStmt"})
_POSITION_KEYS = frozenset({"location", "stmt_location", "stmt_len"})


class ApplyRefused(RuntimeError):
    """A file, a statement or a backup the verb will not run."""


# ---- A1 the statement rule ----------------------------------------------------------------------

def parse(text: str) -> dict:
    """The whole parse of `text`, refused unless it parses, on the expected
    grammar, to at least one statement."""
    try:
        tree = json.loads(pg_parser.parse_sql_json(text))
    except pg_parser.ParseError as e:
        raise ApplyRefused(f"does not parse: {e}") from e
    major = tree.get("version", 0) // 10000
    if major != PARSER_PG_MAJOR:
        raise ApplyRefused(f"parser grammar {major} is not Postgres {PARSER_PG_MAJOR}")
    if not tree.get("stmts"):
        raise ApplyRefused("no statement")
    return tree


def _without_positions(node: Any) -> Any:
    if isinstance(node, dict):
        return {k: _without_positions(v) for k, v in node.items() if k not in _POSITION_KEYS}
    if isinstance(node, list):
        return [_without_positions(v) for v in node]
    return node


def _pieces(text: str, tree: dict) -> list[tuple[str, dict]]:
    """Each statement's own text (by BYTE offsets) with its tree, each piece
    re-parsed alone to that same tree, so the text that runs is the text
    that was checked."""
    raw = text.encode("utf-8")
    out = []
    for i, stmt in enumerate(tree["stmts"], 1):
        loc = stmt.get("stmt_location", 0)
        length = stmt.get("stmt_len", 0)
        piece = (raw[loc:loc + length] if length else raw[loc:]).decode("utf-8")
        try:
            alone = parse(piece)["stmts"]
        except ApplyRefused:
            alone = []
        if len(alone) != 1 or _without_positions(alone[0]) != _without_positions(stmt):
            raise ApplyRefused(
                f"statement {i} refused: its text does not parse alone to the statement checked"
            )
        out.append((piece, stmt["stmt"]))
    return out


def split_statements(text: str) -> list[str]:
    return [piece for piece, _ in _pieces(text, parse(text))]


def _walk(node: Any):
    """Every (key, value) pair anywhere below `node`."""
    if isinstance(node, dict):
        for k, v in node.items():
            yield k, v
            yield from _walk(v)
    elif isinstance(node, list):
        for v in node:
            yield from _walk(v)


def _funcname(call: dict) -> tuple[str, ...]:
    return tuple(part["String"]["sval"] for part in call.get("funcname", []))


def check_statement(tree: dict, i: int) -> None:
    """Refuse statement `i` unless every rule passes (each fail-closed)."""
    (top, body), = tree.items()
    # (r1) the top: one of the four writes, or a SELECT one of whose CTEs writes
    writes = top in _WRITES
    if top == "SelectStmt":
        ctes = (body.get("withClause") or {}).get("ctes", [])
        writes = any(
            next(iter(cte.get("CommonTableExpr", {}).get("ctequery", {})), None) in _WRITES
            for cte in ctes
        )
    if not writes:
        raise ApplyRefused(f"statement {i} refused: {top} is not INSERT, UPDATE, DELETE or MERGE")
    for key, value in _walk(body):
        # (r2) a nested statement node is one of the four or a SELECT
        if key[:1].isupper() and key.endswith("Stmt") and key not in _WRITES and key != "SelectStmt":
            raise ApplyRefused(f"statement {i} refused: {key} is not INSERT, UPDATE, DELETE or MERGE")
        # (r3) SELECT … INTO
        if key == "intoClause":
            raise ApplyRefused(f"statement {i} refused: SELECT … INTO creates a table")
        # (r4) every function call by its full name
        if key == "FuncCall":
            name = _funcname(value)
            if name not in ALLOWED_FUNCTIONS:
                raise ApplyRefused(
                    f"statement {i} refused: function {'.'.join(name)} is not on the apply list"
                )


def check_file(text: str) -> list[str]:
    """THE entry: parse, split, check every statement; the pieces A4 runs."""
    pieces = _pieces(text, parse(text))
    for i, (_, tree) in enumerate(pieces, 1):
        check_statement(tree, i)
    return [piece for piece, _ in pieces]


# ---- A2 the file and its hash -------------------------------------------------------------------

def read_file(name: str, sha256: str) -> str:
    """The file's text, read once, refused unless its bytes hash to `sha256`."""
    if not _SHA256.fullmatch(sha256):
        raise ApplyRefused(f"--sha256 {sha256!r} is not 64 lower-case hex")
    if not _FILE.fullmatch(name):
        raise ApplyRefused(f"file {name!r} is not <date>/<nn>-<name>-apply.sql")
    path = PROMPTS_ROOT / name
    if not path.is_file():
        raise ApplyRefused(f"no such file: {path}")
    raw = path.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != sha256:
        raise ApplyRefused(f"sha256 {got} is not the approved {sha256}")
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError as e:
        raise ApplyRefused(f"file {name!r} is not UTF-8: {e}") from e


# ---- A3 the backup line -------------------------------------------------------------------------

def backup_line(prod: bool) -> str:
    if not prod:
        return "backup: not checked (not --prod)"
    try:
        production = env.is_production()
    except env.EnvConfigError as e:
        raise ApplyRefused(f"--prod needs {env.ENV_VAR}={env.PRODUCTION}: {e}") from e
    if not production:
        raise ApplyRefused(f"--prod needs {env.ENV_VAR}={env.PRODUCTION}")
    cfg = load_backup_config()
    if not cfg.database.enabled or not cfg.armed:
        raise ApplyRefused("backup — no database dump armed")
    try:
        age = latest_snapshot_age(cfg)
    except Exception as e:  # an unmounted destination; the message is credential-free
        raise ApplyRefused(f"backup — {e}") from e
    if age is None:
        raise ApplyRefused("backup — no snapshot")
    seconds = int(age.total_seconds())
    if age.total_seconds() > BACKUP_MAX_AGE_S:
        raise ApplyRefused(
            f"backup — newest snapshot {seconds} s old, over BACKUP_MAX_AGE_S {BACKUP_MAX_AGE_S} s"
        )
    return f"backup: newest snapshot {seconds} s old (bound {BACKUP_MAX_AGE_S} s)"


# ---- A4 one transaction -------------------------------------------------------------------------

def apply_statements(conn, statements: list[str], *, side: Side | str) -> int:
    """Run `statements` in ONE transaction on `conn`; the exit code."""
    side = Side(side)
    n = len(statements)
    conn.autocommit = False
    try:
        conn.execute(f"SET LOCAL statement_timeout = '{STATEMENT_TIMEOUT}'")
        conn.execute(f"SET LOCAL lock_timeout = '{LOCK_TIMEOUT}'")
        major = int(conn.execute("SHOW server_version_num").fetchone()[0]) // 10000
        if major != SERVER_PG_MAJOR:
            conn.rollback()
            print(f"FAILED: server is Postgres {major}, apply is proved for {SERVER_PG_MAJOR} — ROLLED BACK")
            return 1
        current = conn.execute("SELECT current_user").fetchone()[0]
        if current != side.role:
            conn.rollback()
            print(f"FAILED: current_user is {current!r}, not {side.role!r} — ROLLED BACK")
            return 1
        total = 0
        for i, piece in enumerate(statements, 1):
            print(f"STATEMENT {i}/{n}: {piece.strip()}", flush=True)
            try:
                cursor = conn.execute(piece, prepare=True)
            except Exception as e:
                conn.rollback()
                print(f"FAILED at statement {i}: {type(e).__name__}: {e} — ROLLED BACK")
                return 1
            print(f"ROWS {i}: {cursor.rowcount}")
            total += max(cursor.rowcount, 0)
        conn.commit()
        print(f"COMMITTED · statements: {n} · rows: {total}")
        return 0
    finally:
        # A no-op after the commit; on every other path it undoes the
        # transaction before the connection goes.
        conn.rollback()
        conn.close()


# ---- A5 the verb --------------------------------------------------------------------------------

def _refuse(message: str) -> None:
    print(f"REFUSED: {message} — nothing opened", file=sys.stderr)
    raise SystemExit(2)


def command(args: argparse.Namespace) -> None:
    side = Side(args.side)
    try:
        text = read_file(args.file, args.sha256)
        statements = check_file(text)
        line = backup_line(args.prod)
        dbname = db.PROD_DB_NAME if args.prod else env.resolve_db_name()
    except (ApplyRefused, env.EnvConfigError) as e:
        _refuse(str(e))
    if dbname == db.PROD_DB_NAME and not args.prod:
        _refuse(f"database {db.PROD_DB_NAME} requires --prod")
    print(line)
    conn = db.connect(dbname, side=side, allow_prod=args.prod)
    code = apply_statements(conn, statements, side=side)
    if code:
        raise SystemExit(code)


def add_apply_parser(sub) -> None:
    apply = sub.add_parser("apply", help="Run one approved DML file in one transaction")
    apply.add_argument("--side", choices=[s.value for s in Side], required=True)
    apply.add_argument("--prod", action="store_true")
    apply.add_argument("--sha256", required=True, metavar="<64 hex>")
    apply.add_argument("file", metavar="<date>/<nn>-<name>-apply.sql")
    apply.set_defaults(func=command)


__all__ = [
    "ALLOWED_FUNCTIONS",
    "ApplyRefused",
    "BACKUP_MAX_AGE_S",
    "LOCK_TIMEOUT",
    "PARSER_PG_MAJOR",
    "PROMPTS_ROOT",
    "SERVER_PG_MAJOR",
    "STATEMENT_TIMEOUT",
    "add_apply_parser",
    "apply_statements",
    "check_file",
    "check_statement",
    "command",
    "parse",
    "split_statements",
]
