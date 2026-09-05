"""`cobalt session` — the F1 clock's command surface.

    cobalt session now [--at ISO8601]
    cobalt session backfill [--dry-run]
    cobalt session blocks [--limit N]

`now` answers the two questions Dejan actually asks at 18:30 on a
Thursday — what session is it, and when does that change — and it prints
what makes the day what it is (weekend / holiday / early close), because
"overnight" on its own is not an explanation.

`backfill` is the migration half of the `session` column: the value of an
EXISTING row cannot be derived in SQL, because it depends on the NYSE
calendar. So it is computed here, through the same resolver every write
uses, and only then does the NOT NULL migration apply.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

from cobalt import db, env
from cobalt.aset.store import MIGRATIONS_DIR as ASET_MIGRATIONS
from cobalt.aset.store import AsetStore
from cobalt.session.clock import ET, now_utc, session_clock
from cobalt.session.store import SessionBlockStore
from cobalt.vaultwrite.store import MIGRATIONS_DIR as VAULTWRITE_MIGRATIONS
from cobalt.vaultwrite.store import VaultWriteStore

#: (table, timestamp column, the migration that ADDS the nullable column)
BACKFILL_TARGETS = (
    ("aset_sizings", "created_at", ASET_MIGRATIONS / "0004_aset_sizings_session.sql"),
    ("vault_writes", "ts", VAULTWRITE_MIGRATIONS / "0002_vault_writes_session.sql"),
)


def _exec_file(conn, path: Path) -> None:
    lines = path.read_text().splitlines()
    sql = "\n".join(line for line in lines if not line.strip().startswith("--"))
    for statement in sql.split(";"):
        statement = statement.strip()
        if statement:
            conn.execute(statement)


def cmd_now(args: argparse.Namespace) -> None:
    clock = session_clock()
    if args.at:
        ts = datetime.fromisoformat(args.at)
        if ts.tzinfo is None:
            raise SystemExit(
                f"--at {args.at!r} has no timezone. Sessions are defined in ET and "
                "storage is UTC; pass an offset (…+00:00) or a 'Z'."
            )
    else:
        ts = now_utc()

    et = clock.to_et(ts)
    session = clock.session(ts)
    when, nxt = clock.next_boundary(ts)
    when_et = when.astimezone(ET)
    delta = when - ts
    hours, rem = divmod(int(delta.total_seconds()), 3600)
    minutes = rem // 60

    print(f"session   : {session}")
    print(f"clock     : {et:%Y-%m-%d %H:%M:%S %Z}  ({ts.astimezone(timezone.utc):%H:%M:%S} UTC)")
    print(f"day       : {clock.calendar.describe(et.date())}")
    print(f"next      : {nxt} at {when_et:%Y-%m-%d %H:%M %Z} (in {hours}h {minutes:02d}m)")
    if session is not None and str(session) == "market_reset":
        print("STATUS    : WRITES BLOCKED — market_reset hard block (Charter §3 F1)")


def cmd_backfill(args: argparse.Namespace) -> None:
    clock = session_clock()
    db_name = env.resolve_db_name()
    print(f"database  : {db_name}  (COBALT_ENV={env.resolve_env()})")

    # RULING 2026-09-04 (S1-P3): migration tooling stays ungated inside
    # market_reset — and never runs quietly there. One loud line, one row
    # in the counter F18 shows. Outside the window this does nothing.
    from cobalt.session import note_ungated

    note_ungated(
        "session.backfill",
        target=db_name,
        why="stamping `session` on existing rows is migration tooling, run "
            "deliberately by a human, and it names the database it wrote",
    )

    conn = db.connect(db_name, allow_prod=True)
    conn.autocommit = False
    try:
        with conn.cursor() as cur:
            for table, ts_col, add_migration in BACKFILL_TARGETS:
                _exec_file(conn, add_migration)  # nullable column, idempotent

                cur.execute(f"SELECT count(*) FROM {table} WHERE session IS NULL")
                todo = cur.fetchone()[0]
                cur.execute(f"SELECT count(*) FROM {table}")
                total = cur.fetchone()[0]
                print(f"{table:<14} rows={total:<8} null session={todo}")
                if not todo:
                    continue

                cur.execute(
                    f"SELECT id, {ts_col} FROM {table} WHERE session IS NULL ORDER BY id"
                )
                updates = [(clock.session(ts).value, row_id) for row_id, ts in cur.fetchall()]
                cur.executemany(
                    f"UPDATE {table} SET session = %s WHERE id = %s", updates
                )
                print(f"{table:<14} backfilled {cur.rowcount if cur.rowcount and cur.rowcount > 0 else len(updates)} row(s)")

                cur.execute(f"SELECT count(*) FROM {table} WHERE session IS NULL")
                left = cur.fetchone()[0]
                if left:
                    raise SystemExit(f"ABORT: {left} {table} row(s) still NULL after backfill")

            for table, _, _ in BACKFILL_TARGETS:
                cur.execute(
                    f"SELECT session, count(*) FROM {table} GROUP BY 1 ORDER BY 2 DESC"
                )
                counts = ", ".join(f"{s}={c}" for s, c in cur.fetchall()) or "(empty)"
                print(f"{table:<14} {counts}")

        if args.dry_run:
            conn.rollback()
            print("ROLLED BACK (dry run).")
            return
        conn.commit()
        print("COMMITTED.")
    except BaseException:
        conn.rollback()
        print("ROLLED BACK (error).")
        raise
    finally:
        conn.close()

    # Only now can NOT NULL apply. ensure_schema() runs every migration
    # including 000{3,5}; it is the same call every entrypoint makes, so
    # if it passes here it passes there.
    AsetStore().ensure_schema()
    VaultWriteStore().ensure_schema()
    SessionBlockStore().ensure_schema()
    print("NOT NULL applied (ensure_schema clean on both tables).")


def cmd_blocks(args: argparse.Namespace) -> None:
    rows = SessionBlockStore().recent(limit=args.limit)
    if not rows:
        print("no session blocks recorded")
        return
    for row in rows:
        print(
            f"{row['id']:>6}  {row['ts'].astimezone(ET):%Y-%m-%d %H:%M:%S %Z}  "
            f"{row['session']:<13} {row['actor']:<34} {row['target'] or '-'}"
        )


def add_parser(sub) -> None:
    """Mounted by `cobalt.cli`. Kept here so the session module owns its
    own command surface (one path)."""
    session = sub.add_parser("session", help="F1 session clock (Charter §3 F1)")
    ssub = session.add_subparsers(dest="command", required=True)

    now = ssub.add_parser("now", help="Current session and the next boundary.")
    now.add_argument("--at", help="ISO 8601 instant WITH offset, instead of now.")
    now.set_defaults(func=cmd_now)

    backfill = ssub.add_parser(
        "backfill", help="Stamp `session` on existing rows, then apply NOT NULL."
    )
    backfill.add_argument("--dry-run", action="store_true", help="Compute, write nothing.")
    backfill.set_defaults(func=cmd_backfill)

    blocks = ssub.add_parser("blocks", help="Recent market_reset refusals.")
    blocks.add_argument("--limit", type=int, default=20)
    blocks.set_defaults(func=cmd_blocks)


__all__ = ["add_parser", "cmd_backfill", "cmd_blocks", "cmd_now"]
