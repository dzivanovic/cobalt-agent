"""`cobalt cards` — the state machine's command surface.

    cobalt cards state <id>
    cobalt cards history <id>
    cobalt cards move <id> --to STATE [--actor you|cobalt] [--reason ...]
    cobalt cards backfill [--dry-run]
    cobalt cards expire [--at ISO8601] [--dry-run]
    cobalt cards edges

`edges` prints the edge table straight from `models.ALLOWED` — the
DevDocs page is generated from it, so the wiki cannot drift from what the
store actually enforces.

`expire` is what launchd runs at 16:05 ET (`com.cobalt.cards-expire`).
It takes `--at` for the same reason `session now` does: the tests freeze
the clock rather than sleeping until 16:05.
"""

from __future__ import annotations

import argparse
from datetime import datetime

from cobalt import env
from cobalt.session.clock import ET, now_utc, session_clock

from .expire import expire_due
from .models import FILL_TARGET, Actor, CardState, edge_table_markdown
from .store import CardStore


def _store() -> CardStore:
    store = CardStore()
    store.ensure_schema()
    return store


def _at(args: argparse.Namespace) -> datetime:
    if not getattr(args, "at", None):
        return now_utc()
    ts = datetime.fromisoformat(args.at)
    if ts.tzinfo is None:
        raise SystemExit(
            f"--at {args.at!r} has no timezone. Sessions are defined in ET and "
            "storage is UTC; pass an offset (…-05:00) or a 'Z'."
        )
    return ts


def cmd_state(args: argparse.Namespace) -> None:
    store = _store()
    print(f"card {args.card_id}: {store.state_of(args.card_id)}")


def cmd_history(args: argparse.Namespace) -> None:
    rows = _store().history(args.card_id)
    if not rows:
        print(f"no transitions recorded for card {args.card_id}")
        return
    for row in rows:
        frm = row["from_state"] or "(genesis)"
        print(
            f"{row['id']:>7}  {row['at'].astimezone(ET):%Y-%m-%d %H:%M:%S %Z}  "
            f"{frm:>9} -> {row['to_state']:<9} {row['session']:<12} "
            f"{row['actor']:<7} {row['reason'] or ''}"
        )
        if row["evidence"]:
            print(f"{'':>9}evidence: {row['evidence']}")


def cmd_move(args: argparse.Namespace) -> None:
    store = _store()
    before = store.state_of(args.card_id)
    to_state = CardState(args.to)
    # ONE PATH TO FILLED (S1-P3) — the CLI takes the same route the sheet
    # and the actual-fill form take, so a manual card gets its missing
    # rows here too and a radar card is refused here too.
    if to_state is FILL_TARGET:
        tids = store.fill(
            args.card_id,
            actor=Actor(args.actor),
            reason=args.reason,
            evidence={"via": "cobalt cards move"},
        )
    else:
        tids = [
            store.transition(
                args.card_id,
                to_state,
                actor=Actor(args.actor),
                reason=args.reason,
                evidence={"via": "cobalt cards move"},
            )
        ]
    tid = ", ".join(str(i) for i in tids)
    print(f"card {args.card_id}: {before} -> {args.to}  (card_transitions id {tid})")


def cmd_backfill(args: argparse.Namespace) -> None:
    # NOT `_store()`: that applies every migration including
    # `state SET NOT NULL`, which fails on precisely the un-backfilled
    # rows this command exists to fix. `backfill()` prepares its own
    # schema without the constraint and applies it afterwards.
    store = CardStore()
    print(f"database  : {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    today = session_clock().to_et(now_utc()).date()
    print(f"today (ET): {today}")
    counts = store.backfill(today=today, dry_run=args.dry_run)
    total = counts.pop("_total")
    for state, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        if n:
            print(f"  {state:<10} {n}")
    print(f"  {'TOTAL':<10} {total}")
    print("ROLLED BACK (dry run)." if args.dry_run else "COMMITTED.")
    if not args.dry_run:
        # Only now can 0007's NOT NULL apply — same two-step the F1
        # session backfill uses.
        store.ensure_schema()
        print("NOT NULL applied (ensure_schema clean).")


def cmd_expire(args: argparse.Namespace) -> None:
    store = _store()
    ts = _at(args)
    print(f"database  : {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    print(f"checked at: {session_clock().to_et(ts):%Y-%m-%d %H:%M:%S %Z}")
    moved = expire_due(store, now=ts, dry_run=args.dry_run)
    if not moved:
        print("no cards past their window.")
        return
    for row in moved:
        print(
            f"  card {row['card_id']:<6} {row['ticker']:<6} {row['from_state']:<9} "
            f"-> EXPIRED   window {row['window_end']} ({row['window_source']})"
        )
    print(f"{len(moved)} card(s) {'would be' if args.dry_run else ''} expired.")


def cmd_edges(args: argparse.Namespace) -> None:
    print(edge_table_markdown())


def add_parser(sub) -> None:
    """Mounted by `cobalt.cli`. The cards module owns its own commands."""
    cards = sub.add_parser("cards", help="F7 card state machine (Charter §3 F7)")
    csub = cards.add_subparsers(dest="command", required=True)

    state = csub.add_parser("state", help="The current state of one card.")
    state.add_argument("card_id", type=int)
    state.set_defaults(func=cmd_state)

    history = csub.add_parser("history", help="Every transition of one card.")
    history.add_argument("card_id", type=int)
    history.set_defaults(func=cmd_history)

    move = csub.add_parser("move", help="Move a card through a legal edge.")
    move.add_argument("card_id", type=int)
    move.add_argument("--to", required=True, choices=[s.value for s in CardState])
    move.add_argument("--actor", default=Actor.YOU.value, choices=[a.value for a in Actor])
    move.add_argument("--reason", default=None)
    move.set_defaults(func=cmd_move)

    backfill = csub.add_parser(
        "backfill", help="Give every state-less card a state + genesis transition."
    )
    backfill.add_argument("--dry-run", action="store_true", help="Classify, write nothing.")
    backfill.set_defaults(func=cmd_backfill)

    expire = csub.add_parser("expire", help="EXPIRE open cards past their window.")
    expire.add_argument("--at", help="ISO 8601 instant WITH offset, instead of now.")
    expire.add_argument("--dry-run", action="store_true", help="Report, write nothing.")
    expire.set_defaults(func=cmd_expire)

    edges = csub.add_parser("edges", help="Print the edge table (source of the DevDoc).")
    edges.set_defaults(func=cmd_edges)


__all__ = ["add_parser"]
