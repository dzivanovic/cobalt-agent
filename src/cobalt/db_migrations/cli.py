"""`cobalt db migrate [--allow-prod] [--rollback] [--proof-only]` — ADR-0008's harness.

WHAT IT PRINTS IS THE POINT. A migration that moves twelve tables between
schemas and adds a column to six of them is a migration whose claim
("nothing was lost") has to be checkable by looking, not by trusting. So
every run captures, per table, BEFORE and AFTER:

  * where it lives (`public` / `system` / `"user"`),
  * `count(*)`,
  * a content digest over the rows, ordered by the primary key,
  * how long taking that proof cost, in wall seconds.

THE DIGEST IS FOLDED ROW BY ROW IN THIS PROCESS (2026-09-18). It used to
be one server-side value — the whole table concatenated with `'|'` and
hashed in a single expression — and on 2026-09-18 that is exactly what
killed a production deploy: `system.bars` holds 8,410,174 rows, the
concatenation passed Postgres's 1 GB varlena ceiling, and the run died
with `ProgramLimitExceeded` in the BEFORE proof, before the first
`-- applying` line. `cobalt_dev` was green on the same command, so the
gate could not see it. The rows now arrive through a NAMED (server-side)
cursor in batches of `PROBE_BATCH_SIZE` and are folded into one
`hashlib.md5()` — the separator written BETWEEN rows and never after the
last, no rows at all hashing the empty string. Those are precisely the
bytes the old aggregate produced, so **every digest keeps its old value**
and proof tables printed before that date stay comparable. Memory is
constant and there is no size ceiling left.

Two designs were rejected and are recorded so they are not re-proposed:
hashing each row and digesting the hashes (32 bytes per row is 269 MB at
today's row count and hits 1 GB again near 33M rows — a later ceiling is
still a ceiling), and exempting bulk tables from the content digest (a
weaker proof exactly where the most data lives).

THE DIGEST EXCLUDES every column added by these migrations: `user_id`,
`vault_outcome`, and `vault_reason`. A digest over the whole row would
differ before and after by construction and would prove nothing. Taking
it over `to_jsonb(t)` minus those columns makes the two digests comparable,
and an inequality is a real finding: the rows themselves changed. `to_jsonb`
serialises keys in a stable order, so the digest does not depend on
column order either — which matters, because `SET SCHEMA` and `ADD
COLUMN` both touch the catalog the naive `row::text` reads.

ORDERED BY THE PRIMARY KEY, read from the catalog per table rather than
hard-coded: `bars` is keyed `(ticker, interval, ts)`, `day_modes` by
`trade_date`, `cobalt_jobs` by `label`, the rest by `id`.

`--rollback` runs the registered reverse migrations newest-first
and prints the same proof table. Running `migrate`, then `--rollback`,
then `migrate` again must land on the same digests — the suite asserts
exactly that round-trip on `cobalt_dev`.

`--proof-only` takes the BEFORE proof over every table the harness knows,
prints it with its timings, and applies NOTHING. Its transaction is
opened READ ONLY, so a bug in this flag's own handling cannot write
either — the server refuses; and REPEATABLE READ, so the whole table
carries ONE picture of the database out of the window rather than a
different snapshot per table. It exists because the 09-18 defect cost a
resident outage to discover: this is the command a deploy preflights
while everything is still up. It is refused together with `--rollback` /
`--down-to`, which exist to apply things.

`--allow-prod` reaches `cobalt_brain` without flipping the process into
production mode (RULING 7's one-off-tooling seam). Without it the target
is whatever `COBALT_ENV` resolves. `--proof-only` is under the same gate:
read-only or not, it does not open a production connection by itself.
"""

from __future__ import annotations

import argparse
import hashlib
import time
from typing import Iterable, Iterator, Optional

import psycopg
from psycopg import IsolationLevel, sql

from cobalt import db, env

from . import FORWARD, REVERSE
from .placement import CREATED_TABLES, MOVED_TABLES, SEEDED_TABLES

#: Columns introduced by the registered migrations. Excluding them makes a
#: populated row comparable before and after a shape-only migration.
DIGEST_EXCLUDED_COLUMNS = (
    "user_id",
    "vault_outcome",
    "vault_reason",
    "account_mode",
    "pool_member_id",
)

#: Columns a registered migration adds to ONE table, excluded from that
#: table's digest only. Per table rather than global because names like
#: `scan_id` or `why` would otherwise silently drop out of the digests of
#: the new seam tables that carry them as real content.
TABLE_DIGEST_EXCLUDED_COLUMNS: dict[str, tuple[str, ...]] = {
    # 0007_radar_cards.sql — the radar card columns.
    "aset_sizings": (
        "trade_def_slug", "trade_def_md5", "setup_ref", "trigger_type",
        "trigger_price", "stop_ref", "structural_stop", "formed_at",
        "expires_at", "why", "proposed_key", "tapped_grade", "sized_grade",
        "snap_notice", "conviction", "proximity", "card_score",
        "score_suppressed", "radar_score_id", "scan_id", "formula_sha256",
        "tunables_sha256", "settings_sha256", "health", "promoted_at",
    ),
}

#: Where a new-core table may legitimately be found, in look-up order.
SEARCHED_SCHEMAS = ("public", "user", "system")

#: Rows fetched per round trip from the server-side cursor the digest
#: reads. Big enough that a million-row table is a hundred fetches, small
#: enough that no batch is a memory event: the whole point of the
#: 2026-09-18 rewrite is that neither side ever holds the table.
PROBE_BATCH_SIZE = 10_000


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


def _row_json(table: str) -> sql.Composed:
    """`to_jsonb(t)` minus the columns these migrations add to `table`.

    Split out so the digest expression has ONE definition: the streamed
    proof builds its SELECT from it, and the suite's byte-compatibility
    oracle — the only surviving copy of the old aggregate — builds the
    old expression from the same thing, which is what makes the two
    values comparable rather than merely similar.
    """
    row_json: sql.Composable = sql.SQL("to_jsonb(t)")
    for column in DIGEST_EXCLUDED_COLUMNS + TABLE_DIGEST_EXCLUDED_COLUMNS.get(table, ()):
        row_json = sql.SQL("({row_json} - {column})").format(
            row_json=row_json, column=sql.Literal(column)
        )
    return row_json


def _digest_rows(row_texts: Iterable[str]) -> tuple[int, str]:
    """Fold row texts into `(how many, their digest)` in ONE pass.

    THE COUNT COMES OUT OF THE FOLD (2026-09-18, review finding F1). It
    used to be a separate `SELECT count(*)`, and two statements under
    READ COMMITTED take two snapshots: on a table being written to, the
    printed `rows` could belong to one snapshot and the digest to
    another — a self-contradictory proof line, and `bars` read twice for
    the privilege. Counting the rows the cursor actually yields makes the
    pair self-consistent by construction, whatever lands mid-probe.

    Client memory is one batch, not one row: `_stream_row_texts` fetches
    `PROBE_BATCH_SIZE` rows per round trip. What is never held is the
    table, or the concatenation of it.

    The bytes are the ones a `'|'`-joined aggregate of the same rows in
    the same order would have produced: the separator goes BETWEEN rows
    and never after the last, and no rows at all digest the empty string
    (which is what the old expression's `coalesce(..., '')` arm meant).
    That equality is not an implementation detail — it is what lets a
    proof table printed today be compared with one printed before the
    2026-09-18 rewrite.
    """
    digest = hashlib.md5()
    rows = 0
    for row_text in row_texts:
        if rows:
            digest.update(b"|")
        digest.update(row_text.encode("utf-8"))
        rows += 1
    return rows, digest.hexdigest()


def _stream_row_texts(conn, table: str, query) -> Iterator[str]:
    """Yield `query`'s single text column through a server-side cursor.

    NAMED, therefore server-side: an unnamed psycopg cursor reads the
    whole result set into this process, which would move the 1 GB
    ceiling rather than remove it. `itersize` is what makes the server
    hand the rows over in batches instead of all at once.
    """
    with conn.cursor(name=f"cobalt_probe_{table}") as cursor:
        cursor.itersize = PROBE_BATCH_SIZE
        cursor.execute(query)
        for (row_text,) in cursor:
            yield row_text


def _probe(conn, table: str) -> dict:
    """(schema, rows, digest, seconds) for `table`, wherever it lives.

    `seconds` is wall time and it is a deliverable, not decoration: this
    probe runs twice inside a resident outage, so its cost is part of the
    deploy plan.
    """
    started = time.perf_counter()
    schema = _schema_of(conn, table)
    if schema is None:
        return {
            "schema": None,
            "rows": None,
            "digest": None,
            "seconds": time.perf_counter() - started,
        }
    pk = _pk_columns(conn, schema, table)
    rel = sql.Identifier(schema, table)
    stream = sql.SQL(
        "SELECT ({row_json})::text FROM {rel} AS t ORDER BY {order}"
    ).format(
        row_json=_row_json(table),
        rel=rel,
        order=sql.SQL(", ").join(sql.Identifier("t", c) for c in pk),
    )
    # ONE statement for both numbers: the count is the rows the cursor
    # yields, so no concurrent write can put the count and the digest on
    # different snapshots — and an 8.4M-row table is read once, not twice.
    rows, digest = _digest_rows(_stream_row_texts(conn, table, stream))
    return {
        "schema": schema,
        "rows": rows,
        "digest": digest,
        "seconds": time.perf_counter() - started,
    }


def _probe_all(conn) -> dict[str, dict]:
    tables = {**MOVED_TABLES, **SEEDED_TABLES, **CREATED_TABLES}
    return {t: _probe(conn, t) for t in sorted(tables)}


def _total_seconds(probe: dict[str, dict]) -> float:
    return sum(p["seconds"] for p in probe.values())


def _verdict(
    name: str, before: dict, after: dict, *, direction: str = "FORWARD"
) -> str:
    """Direction-aware classification, pure so abort ordering is testable."""
    if before["schema"] is None and after["schema"] is None:
        return "ABSENT"
    if before["digest"] == after["digest"] and before["rows"] == after["rows"]:
        return "OK"
    if direction == "FORWARD" and before["schema"] is None:
        return "CREATED"
    if (
        direction == "ROLLBACK"
        and name in CREATED_TABLES
        and before["schema"] is not None
        and after["schema"] is None
    ):
        return "DROPPED"
    return "CHANGED"


def _proof_verdicts(
    before: dict[str, dict], after: dict[str, dict], *, direction: str = "FORWARD"
) -> dict[str, str]:
    return {
        name: _verdict(name, before[name], after[name], direction=direction)
        for name in before
    }


def _print_proof(
    before: dict[str, dict], after: dict[str, dict], *, direction: str = "FORWARD"
) -> int:
    """Render the proof table. Returns the number of CHANGED digests."""
    tables = {**MOVED_TABLES, **SEEDED_TABLES, **CREATED_TABLES}
    header = (
        f"{'table':<20} {'side':<7} {'schema before -> after':<26} "
        f"{'rows':<15} {'probe secs':<15} {'digest before -> after':<21} verdict"
    )
    print(header)
    print("-" * len(header))
    changed = 0
    for name in sorted(tables):
        b, a = before[name], after[name]
        where = f"{b['schema'] or '-'} -> {a['schema'] or '-'}"
        rows = f"{'-' if b['rows'] is None else b['rows']} -> " \
               f"{'-' if a['rows'] is None else a['rows']}"
        secs = f"{b['seconds']:.2f} -> {a['seconds']:.2f}"
        dig = f"{(b['digest'] or '-')[:8]} -> {(a['digest'] or '-')[:8]}"
        verdict = _verdict(name, b, a, direction=direction)
        if verdict == "CHANGED":
            changed += 1
        print(
            f"{name:<20} {tables[name].value:<7} {where:<26} {rows:<15} "
            f"{secs:<15} {dig:<21} {verdict}"
        )
    print("-" * len(header))
    print(
        f"{len(tables)} table(s) proven; digest excludes "
        f"{', '.join(DIGEST_EXCLUDED_COLUMNS)}"
        + "".join(
            f"; {table}: {len(cols)} card column(s) added by 0007"
            for table, cols in TABLE_DIGEST_EXCLUDED_COLUMNS.items()
        )
        + ". "
        + ("content UNCHANGED on every table."
           if changed == 0
           else f"{changed} table(s) CHANGED — investigate before proceeding.")
    )
    _print_cost(before, after)
    return changed


def _print_cost(before: dict[str, dict], after: dict[str, dict]) -> None:
    """What the proof itself cost, because it is spent inside an outage."""
    b, a = _total_seconds(before), _total_seconds(after)
    slowest = max(before, key=lambda name: before[name]["seconds"])
    print(
        f"proof cost: BEFORE {b:.1f} s + AFTER {a:.1f} s = total {b + a:.1f} s; "
        f"slowest table {slowest} ({before[slowest]['seconds']:.1f} s before)."
    )


def _print_probe(probe: dict[str, dict], *, dbname: str) -> None:
    """`--proof-only`'s table: one state, with the full digests.

    The full 32 characters rather than the migrate table's 8, because
    this output exists to be carried out of the window and compared with
    a later run's — a prefix is enough to read, not enough to trust.
    """
    tables = {**MOVED_TABLES, **SEEDED_TABLES, **CREATED_TABLES}
    header = (
        f"{'table':<20} {'side':<7} {'schema':<8} {'rows':<12} "
        f"{'digest':<34} secs"
    )
    print(header)
    print("-" * len(header))
    for name in sorted(tables):
        p = probe[name]
        rows = "-" if p["rows"] is None else str(p["rows"])
        print(
            f"{name:<20} {tables[name].value:<7} {p['schema'] or '-':<8} "
            f"{rows:<12} {p['digest'] or '-':<34} {p['seconds']:.2f}"
        )
    print("-" * len(header))
    total = _total_seconds(probe)
    print(
        f"{len(tables)} table(s) probed on {dbname}; digest excludes "
        f"{', '.join(DIGEST_EXCLUDED_COLUMNS)}"
        + "".join(
            f"; {table}: {len(cols)} card column(s) added by 0007"
            for table, cols in TABLE_DIGEST_EXCLUDED_COLUMNS.items()
        )
        + f". Proof cost: total {total:.1f} s — and a migration pays it TWICE "
        "(before and after), inside the outage."
    )
    print("NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.")


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


def _assert_utf8(conn) -> None:
    """The digest's byte-compatibility rests on the database encoding.

    The old aggregate hashed a server-side text value, whose bytes are in
    the DATABASE encoding; the fold hashes `str.encode("utf-8")`. The two
    agree exactly when that encoding is UTF-8 — and silently disagree on
    non-ASCII rows when it is not, which is the one way this rewrite
    could lie. Checked once per run rather than assumed (L1).
    """
    encoding = conn.execute("SHOW server_encoding").fetchone()[0]
    if encoding.upper().replace("-", "").replace("_", "") != "UTF8":
        raise MigrationError(
            f"the database's server_encoding is {encoding!r}, not UTF8. The "
            "content digest is folded client-side as UTF-8 bytes, so on this "
            "database it would not equal the value the proof has always "
            "printed. Fix the encoding or the fold, not the comparison."
        )


def _connect(dbname: str, *, allow_prod: bool, read_only: bool):
    """The harness's ONE connection (ADR-0008 D1: one `connect_migration`).

    `read_only=True` is not a convention this module promises to honour —
    psycopg opens every transaction with `BEGIN ... READ ONLY`, so the
    SERVER refuses a write even if the code asks for one.

    REPEATABLE READ, AND IT IS THE POINT OF THE WHOLE PROOF (2026-09-18).
    `cmd_migrate` takes the BEFORE probe, applies, and takes the AFTER
    probe, then rolls back on any `CHANGED` verdict. At Postgres's default
    READ COMMITTED every probe STATEMENT takes its own snapshot, so the
    AFTER probe also sees whatever OTHER sessions committed in between —
    and on production `system.bars` makes one probe ≈46 s, so that window
    is ≈100 s wide. A deploy only takes the two RESIDENTS down:
    `com.cobalt.heartbeat` (every 15 minutes) and `com.cobalt.seat-usage`
    (hourly) keep updating `system.cobalt_jobs`, `cobalt_redactions` is
    append-only telemetry, `vault_writes` grows with any vault write. One
    such commit inside the window made a GOOD migration read `CHANGED`
    and roll the whole thing back, with the residents already stopped:
    a clean failure, but an outage for nothing.

    At REPEATABLE READ the snapshot is taken at this transaction's first
    statement and BOTH probes read THAT snapshot plus this transaction's
    OWN changes — which is exactly the question the proof was written to
    answer: "did THIS migration change existing content?". Other
    sessions' commits are invisible to both probes, so they cannot fail a
    good migration; the migration's own writes are still seen, so the
    proof still proves something.

    The price is named and accepted: if another session commits a change
    to a row this migration then modifies, the server raises
    `could not serialize access…` rather than applying it. Nothing is
    applied, `cmd_migrate`'s `except` path rolls back, and the operator
    is told what happened — see the message there.

    Set here, before the first statement, because psycopg refuses to
    change the isolation level of a transaction already in progress and
    applies these attributes at the next `BEGIN`. `db.connect_migration`
    hands back an AUTOCOMMIT connection whose `SET search_path` /
    `set_config` have already committed, so nothing is open yet.
    """
    conn = db.connect_migration(dbname, allow_prod=allow_prod)
    try:
        if read_only:
            conn.read_only = True
        conn.isolation_level = IsolationLevel.REPEATABLE_READ
        conn.autocommit = False
        _assert_utf8(conn)
    except BaseException:
        conn.close()
        raise
    return conn


def cmd_migrate(args: argparse.Namespace) -> None:
    proof_only = args.proof_only
    if proof_only and (args.rollback or args.down_to):
        raise MigrationError(
            "--proof-only takes the proof and applies NOTHING, so it cannot be "
            "combined with --rollback or --down-to, whose whole job is to apply "
            "the reverse migrations. Run the proof first, then the rollback."
        )
    if args.rollback and not args.down_to:
        targets = ", ".join(path.name for path in REVERSE)
        raise MigrationError(
            "--rollback requires --down-to NNNN before any connection is opened; "
            f"registered reverse targets newest-first: {targets}"
        )
    dbname = db.PROD_DB_NAME if args.allow_prod else env.resolve_db_name()
    direction = "ROLLBACK" if args.rollback else "FORWARD"
    paths = _rollback_paths(args.down_to) if args.rollback else FORWARD

    if proof_only:
        print(f"cobalt db migrate — PROOF ONLY on {dbname} (READ ONLY, nothing applied)")
        conn = _connect(dbname, allow_prod=args.allow_prod, read_only=True)
        try:
            probe = _probe_all(conn)
        finally:
            conn.rollback()
            conn.close()
        print()
        _print_probe(probe, dbname=dbname)
        return

    print(f"cobalt db migrate — {direction} on {dbname}")
    conn = _connect(dbname, allow_prod=args.allow_prod, read_only=False)
    try:
        before = _probe_all(conn)
        _apply(conn, paths)
        after = _probe_all(conn)
        verdicts = _proof_verdicts(before, after, direction=direction)
        if "CHANGED" in verdicts.values():
            conn.rollback()
        else:
            conn.commit()
    except psycopg.errors.SerializationFailure as e:
        # The named price of REPEATABLE READ (see `_connect`). Postgres's
        # own text ("could not serialize access due to concurrent
        # update") tells an operator nothing about what to do at 20:40
        # on a deploy, so it is wrapped rather than re-raised bare.
        conn.rollback()
        raise MigrationError(
            "the migration could not serialize access: another session "
            "committed a change to a row this migration then modified, while "
            "this transaction held its REPEATABLE READ snapshot. NOTHING WAS "
            "APPLIED — the transaction was rolled back. Something is still "
            "writing to a table this migration touches: stop it (a resident, "
            "a scheduled one-shot, another session) and run the migration "
            f"again. Postgres said: {e}"
        ) from e
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()

    print()
    changed = _print_proof(before, after, direction=direction)
    if changed:
        raise MigrationError(
            f"{changed} table(s) changed content across the migration. The "
            "transaction was rolled back before commit; compare against the pg_dump."
        )


def _migration_version(path) -> int:
    try:
        return int(path.name.split("_", 1)[0])
    except (ValueError, IndexError) as e:
        raise MigrationError(f"migration filename has no numeric prefix: {path.name}") from e


def _rollback_paths(down_to: str | None):
    if down_to is None:
        raise MigrationError("--rollback requires --down-to NNNN")
    try:
        target = int(down_to)
    except ValueError as e:
        raise MigrationError(f"--down-to must be a migration number, got {down_to!r}") from e
    paths = tuple(path for path in REVERSE if _migration_version(path) > target)
    if not paths:
        raise MigrationError(f"no registered migrations are newer than {down_to}")
    return paths


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
        "--down-to",
        metavar="NNNN",
        help="Required with --rollback; reverse only migrations newer than NNNN.",
    )
    migrate.add_argument(
        "--rollback",
        action="store_true",
        help="Reverse registered migrations: heartbeat columns dropped, tables moved to public.",
    )
    migrate.add_argument(
        "--proof-only",
        action="store_true",
        help="Take the proof (rows, digest, seconds) in a READ ONLY transaction "
             "and apply nothing. Preflight this before a deploy window.",
    )
    migrate.set_defaults(func=cmd_migrate)

    from cobalt.db_query import add_query_parser

    add_query_parser(gsub)


__all__ = [
    "DIGEST_EXCLUDED_COLUMNS",
    "PROBE_BATCH_SIZE",
    "MigrationError",
    "TABLE_DIGEST_EXCLUDED_COLUMNS",
    "add_parser",
    "cmd_migrate",
]
