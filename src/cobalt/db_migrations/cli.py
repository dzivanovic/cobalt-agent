"""`cobalt db migrate [--allow-prod] [--rollback]` — ADR-0008's harness.

WHAT IT PRINTS IS THE POINT. A migration that moves twelve tables between
schemas and adds a column to six of them is a migration whose claim
("nothing was lost") has to be checkable by looking, not by trusting. So
every run captures, per table, BEFORE and AFTER:

  * where it lives (`public` / `system` / `"user"`),
  * `count(*)`,
  * a content digest: `md5(string_agg(row::text, '|' ORDER BY <pk>))`.

THE DIGEST EXCLUDES `user_id`. The forward migration ADDS that column to
the six user-side tables, so a digest over the whole row would differ
before and after by construction and would prove nothing. Taking it over
`to_jsonb(t) - 'user_id'` means the two digests are comparable and an
inequality is a real finding: the rows themselves changed. `to_jsonb`
serialises keys in a stable order, so the digest does not depend on
column order either — which matters, because `SET SCHEMA` and `ADD
COLUMN` both touch the catalog the naive `row::text` reads.

ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.

`--rollback` runs `0002_move_tables.rollback.sql` (catalog-only reverse)
and prints the same proof table. Running `migrate`, then `--rollback`,
then `migrate` again must land on the same digests — the suite asserts
exactly that round-trip on `cobalt_dev`.

`--allow-prod` reaches `cobalt_brain` without flipping the process into
production mode (RULING 7's one-off-tooling seam). Without it the target
is whatever `COBALT_ENV` resolves.
"""

from __future__ import annotations

import argparse
from typing import Optional

from psycopg import sql

from cobalt import db, env

from . import FORWARD, REVERSE
from .placement import MOVED_TABLES, SEEDED_TABLES

#: The tenancy column the digest ignores — see the module docstring.
TENANCY_COLUMN = "user_id"

#: Where a new-core table may legitimately be found, in look-up order.
SEARCHED_SCHEMAS = ("public", "user", "system")


class MigrationError(RuntimeError):
    """The migration could not be run or could not be proven."""


def _schema_of(conn, table: str) -> Optional[str]:
    row = conn.execute(
        "SELECT schemaname FROM pg_tables "
        "WHERE tablename = %s AND schemaname = ANY(%s) LIMIT 1",
        (table, list(SEARCHED_SCHEMAS)),
    ).fetchone()
    return row[0] if row else None


def _pk_columns(conn, schema: str, table: str) -> list[str]:
    rows = conn.execute(
        """
        SELECT a.attname
        FROM pg_index i
        JOIN pg_attribute a
          ON a.attrelid = i.indrelid AND a.attnum = ANY(i.indkey)
        WHERE i.indrelid = (quote_ident(%s) || '.' || quote_ident(%s))::regclass
          AND i.indisprimary
        ORDER BY array_position(i.indkey::int2[], a.attnum)
        """,
        (schema, table),
    ).fetchall()
    if not rows:
        raise MigrationError(
            f"{schema}.{table} has no primary key, so its rows cannot be put in a "
            "deterministic order and no content digest can be taken. Every "
            "new-core table has one; this is a real finding, not a tooling gap."
        )
    return [r[0] for r in rows]


def _probe(conn, table: str) -> dict:
    """(schema, rows, digest) for `table`, wherever it currently lives."""
    schema = _schema_of(conn, table)
    if schema is None:
        return {"schema": None, "rows": None, "digest": None}
    pk = _pk_columns(conn, schema, table)
    query = sql.SQL(
        "SELECT count(*), "
        "md5(coalesce(string_agg((to_jsonb(t) - {tenancy})::text, '|' ORDER BY {order}), '')) "
        "FROM {rel} AS t"
    ).format(
        tenancy=sql.Literal(TENANCY_COLUMN),
        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
        rel=sql.Identifier(schema, table),
    )
    rows, digest = conn.execute(query).fetchone()
    return {"schema": schema, "rows": int(rows), "digest": digest}


def _probe_all(conn) -> dict[str, dict]:
    tables = {**MOVED_TABLES, **SEEDED_TABLES}
    return {t: _probe(conn, t) for t in sorted(tables)}


def _print_proof(before: dict[str, dict], after: dict[str, dict]) -> int:
    """Render the proof table. Returns the number of CHANGED digests."""
    tables = {**MOVED_TABLES, **SEEDED_TABLES}
    header = (
        f"{'table':<20} {'side':<7} {'schema before -> after':<26} "
        f"{'rows':<15} {'digest before -> after':<21} verdict"
    )
    print(header)
    print("-" * len(header))
    changed = 0
    for name in sorted(tables):
        b, a = before[name], after[name]
        where = f"{b['schema'] or '-'} -> {a['schema'] or '-'}"
        rows = f"{'-' if b['rows'] is None else b['rows']} -> " \
               f"{'-' if a['rows'] is None else a['rows']}"
        dig = f"{(b['digest'] or '-')[:8]} -> {(a['digest'] or '-')[:8]}"
        if b["schema"] is None and a["schema"] is None:
            verdict = "ABSENT"
        elif b["digest"] == a["digest"] and b["rows"] == a["rows"]:
            verdict = "OK"
        elif b["schema"] is None:
            verdict = "CREATED"
        else:
            verdict = "CHANGED"
            changed += 1
        print(
            f"{name:<20} {tables[name].value:<7} {where:<26} {rows:<15} "
            f"{dig:<21} {verdict}"
        )
    print("-" * len(header))
    print(
        f"{len(tables)} table(s) proven; digest = md5(string_agg((to_jsonb(row) - "
        f"'{TENANCY_COLUMN}')::text, '|' ORDER BY pk)). "
        + ("content UNCHANGED on every table."
           if changed == 0
           else f"{changed} table(s) CHANGED — investigate before proceeding.")
    )
    return changed


def _apply(conn, paths) -> None:
    """Run whole .sql files, one transaction for the lot.

    Each file is handed to the server ENTIRE rather than split on ';':
    these migrations are DO blocks, and a splitter would cut them at the
    first semicolon inside the body. psycopg uses the simple query
    protocol when there are no parameters, which accepts multiple
    statements — and the migrations take no parameters by design.
    """
    for path in paths:
        print(f"-- applying {path.name}")
        conn.execute(path.read_text())


def cmd_migrate(args: argparse.Namespace) -> None:
    dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
    direction = "ROLLBACK" if args.rollback else "FORWARD"
    paths = REVERSE if args.rollback else FORWARD

    print(f"cobalt db migrate — {direction} on {dbname}")
    conn = db.connect_migration(dbname, allow_prod=args.allow_prod)
    conn.autocommit = False
    try:
        before = _probe_all(conn)
        _apply(conn, paths)
        after = _probe_all(conn)
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()

    print()
    changed = _print_proof(before, after)
    if changed:
        raise MigrationError(
            f"{changed} table(s) changed content across the migration. The "
            "migration is committed; the proof is not clean — compare against the "
            "pg_dump taken before this run."
        )


def add_parser(sub) -> None:
    group = sub.add_parser("db", help="Database migrations (ADR-0008 two-layer model)")
    gsub = group.add_subparsers(dest="command", required=True)

    migrate = gsub.add_parser(
        "migrate",
        help="Create the system/\"user\" schemas and move every new-core table.",
    )
    migrate.add_argument(
        "--allow-prod",
        action="store_true",
        help="Target cobalt_brain (run from ~/cobalt only, outside market hours).",
    )
    migrate.add_argument(
        "--rollback",
        action="store_true",
        help="Reverse 0002: every table back to public, user_id dropped.",
    )
    migrate.set_defaults(func=cmd_migrate)


__all__ = ["MigrationError", "add_parser", "cmd_migrate"]
