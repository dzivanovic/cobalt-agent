"""Read-only SQL inspection command with a pure, fail-closed guard."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass

from psycopg import sql

from cobalt import db, env
from cobalt.db import Side
from cobalt.taxonomy.loader import load_tunables

REFUSED_WORDS = frozenset(
    "INSERT UPDATE DELETE MERGE TRUNCATE CREATE ALTER DROP GRANT REVOKE COPY "
    "CALL DO SET RESET LOCK VACUUM ANALYZE REFRESH COMMENT LISTEN NOTIFY "
    "PREPARE EXECUTE DEALLOCATE DISCARD INTO".split()
)
REFUSED_FUNCTIONS = frozenset(
    "set_config pg_sleep pg_terminate_backend pg_cancel_backend pg_read_file "
    "pg_read_binary_file pg_ls_dir nextval setval".split()
)


class QueryRefused(ValueError):
    """SQL failed the client-side read-only allowlist."""


@dataclass(frozen=True)
class Tokenized:
    words: tuple[str, ...]
    semicolons: tuple[int, ...]


def tokenize(statement: str) -> Tokenized:
    """Return bare SQL words and statement separators, ignoring quoted text."""
    words: list[str] = []
    semicolons: list[int] = []
    i = 0
    n = len(statement)
    while i < n:
        ch = statement[i]
        if ch.isspace():
            i += 1
            continue
        if statement.startswith("--", i):
            end = statement.find("\n", i + 2)
            i = n if end < 0 else end + 1
            continue
        if statement.startswith("/*", i):
            end = statement.find("*/", i + 2)
            if end < 0:
                raise QueryRefused("unterminated comment")
            i = end + 2
            continue
        if ch in "'\"":
            quote = ch
            i += 1
            while i < n:
                if statement[i] == quote:
                    if i + 1 < n and statement[i + 1] == quote:
                        i += 2
                        continue
                    i += 1
                    break
                i += 1
            else:
                raise QueryRefused("unterminated quoted value")
            continue
        if ch == "$":
            match = re.match(r"\$[A-Za-z_][A-Za-z0-9_]*\$|\$\$", statement[i:])
            if match:
                delimiter = match.group(0)
                end = statement.find(delimiter, i + len(delimiter))
                if end < 0:
                    raise QueryRefused("unterminated dollar-quoted value")
                i = end + len(delimiter)
                continue
        if ch == ";":
            semicolons.append(i)
            i += 1
            continue
        match = re.match(r"[A-Za-z_][A-Za-z0-9_$]*", statement[i:])
        if match:
            words.append(match.group(0).upper())
            i += len(match.group(0))
            continue
        i += 1
    return Tokenized(tuple(words), tuple(semicolons))


def guard_select(statement: str) -> str:
    """Accept exactly one side-effect-free SELECT/WITH statement."""
    parsed = tokenize(statement)
    if not parsed.words:
        raise QueryRefused("empty statement")
    if parsed.words[0] not in {"SELECT", "WITH"}:
        raise QueryRefused(parsed.words[0])
    trailing = statement.rstrip()
    separators = len(parsed.semicolons)
    if separators and trailing.endswith(";"):
        separators -= 1
    if separators:
        raise QueryRefused("multiple statements (;)")
    joined = " ".join(parsed.words)
    for clause in ("FOR UPDATE", "FOR SHARE", "FOR NO KEY UPDATE", "FOR KEY SHARE"):
        if clause in joined:
            raise QueryRefused(clause)
    for word in parsed.words:
        if word in REFUSED_WORDS:
            raise QueryRefused(word)
        lowered = word.lower()
        if (
            lowered in REFUSED_FUNCTIONS
            or lowered.startswith("pg_advisory_")
            or lowered.startswith("dblink")
            or lowered.startswith("lo_")
        ):
            raise QueryRefused(word)
    return trailing[:-1].rstrip() if trailing.endswith(";") else trailing


def _timeout_ms() -> int:
    row = load_tunables().by_key.get("db.query.timeout_s")
    if row is None:
        raise RuntimeError("tunables.yaml: missing db.query.timeout_s")
    return int(row.value) * 1000


def command(args: argparse.Namespace) -> None:
    try:
        statement = guard_select(args.sql)
    except QueryRefused as e:
        print(f"REFUSED SQL token: {e}", file=sys.stderr)
        raise SystemExit(2) from e

    side = Side(args.side)
    dbname = db.PROD_DB_NAME if args.prod else env.resolve_db_name()
    if dbname == db.PROD_DB_NAME and not args.prod:
        print("REFUSED database token: cobalt_brain requires --prod", file=sys.stderr)
        raise SystemExit(2)

    conn = db.connect(dbname, side=side, allow_prod=args.prod)
    conn.autocommit = False
    try:
        conn.execute("BEGIN READ ONLY")
        conn.execute(
            sql.SQL("SET LOCAL statement_timeout = {}").format(sql.Literal(_timeout_ms()))
        )
        current = conn.execute("SELECT current_user").fetchone()[0]
        if current != side.role:
            raise RuntimeError(f"current_user is {current!r}, expected {side.role!r}")
        query = sql.SQL("SELECT * FROM ({}) AS q LIMIT %s").format(sql.SQL(statement))
        cursor = conn.execute(query, (args.limit,))
        columns = [item.name for item in cursor.description]
        rows = cursor.fetchall()
        if args.format == "json":
            print(json.dumps([dict(zip(columns, row)) for row in rows], default=str))
        else:
            print("\t".join(columns))
            for row in rows:
                print("\t".join("" if value is None else str(value) for value in row))
    finally:
        conn.rollback()
        conn.close()


def add_query_parser(sub) -> None:
    query = sub.add_parser("query", help="Run a guarded, read-only SELECT")
    query.add_argument("--side", choices=[s.value for s in Side], required=True)
    query.add_argument("--prod", action="store_true")
    query.add_argument("--format", choices=("json", "table"), default="table")
    query.add_argument("--limit", type=int, default=1000)
    query.add_argument("sql")
    query.set_defaults(func=command)


__all__ = ["QueryRefused", "add_query_parser", "guard_select", "tokenize"]
