"""`cobalt cards` — the state machine's command surface.

    cobalt cards state <id>
    cobalt cards history <id>
    cobalt cards legs <id>
    cobalt cards trade-note <id>
    cobalt cards move <id> --to STATE [--actor you|cobalt] [--reason ...]
    cobalt cards backfill [--dry-run]
    cobalt cards expire [--at ISO8601] [--dry-run]
    cobalt cards edges
    cobalt cards picks [--date YYYY-MM-DD] [--cutoff ISO8601]

`edges` prints the edge table straight from `models.ALLOWED` — the
DevDocs page is generated from it, so the wiki cannot drift from what the
store actually enforces.

`expire` is what launchd runs at 16:05 ET (`com.cobalt.cards-expire`).
It takes `--at` for the same reason `session now` does: the tests freeze
the clock rather than sleeping until 16:05.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime
from decimal import Decimal

from cobalt import env
from cobalt.session.clock import ET, now_utc, session_clock

from .expire import expire_due
from .models import FILL_TARGET, Actor, CardState, edge_table_markdown
from .picks import PickReportRow, render_picks_report
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
    to_state = CardState(args.to)
    if to_state is FILL_TARGET:
        # ONE PATH TO FILLED (S3 C1, v3 §2 [F-22]): a fill carries his
        # price and shares and lands with its entry leg in one transaction
        # (`AsetStore.mark_filled`). This command has neither, so it never
        # fills — refused before anything is read or written.
        raise SystemExit(
            f"REFUSED card {args.card_id}: `cobalt cards move … {FILL_TARGET.value}` never fills. "
            "A fill is written only by the fill — the sheet's POST /fill with the price and "
            "shares the broker filled."
        )
    if to_state is CardState.CLOSED:
        # CLOSED ONLY BY THE ZERO-RUNNING LEG (S3 C2 fix r1, v3 §2): the leg
        # writer that brings running to 0 writes FILLED -> CLOSED in its own
        # transaction (`cards.legs`). Refused before anything is read.
        raise SystemExit(
            f"REFUSED card {args.card_id}: cobalt cards move … {CardState.CLOSED.value} never closes. "
            "A card closes only when an exit leg, a correction or a held count brings running to 0."
        )
    store = _store()
    before = store.state_of(args.card_id)
    tid = store.transition(
        args.card_id,
        to_state,
        actor=Actor(args.actor),
        reason=args.reason,
        evidence={"via": "cobalt cards move"},
    )
    print(f"card {args.card_id}: {before} -> {args.to}  (card_transitions id {tid})")


def cmd_legs(args: argparse.Namespace) -> None:
    """S3 C2-7: one card's CURRENT legs, THE running read and its basis,
    realized R (`realized_r.1`) and whether it is provisional, and who owns
    the stop. READ ONLY: no schema call, nothing written — the running read
    takes the card lock on a transaction that is rolled back."""
    from .legs import LegRefused, read_position

    try:
        pos = read_position(args.card_id)
    except LegRefused as refused:
        raise SystemExit(str(refused))
    card = pos.card
    print(f"card {card['id']}  {card['ticker']}  {card['direction']}  {card['state']}  "
          f"stop {card['stop']}  cobalt stop {card['structural_stop'] if card['structural_stop'] is not None else '—'}")
    print(f"{'id':>7} {'seq':>3} {'kind':<5} {'shares':>6} {'price':>10} {'flag':<9} {'source':<11} "
          f"{'preset':<6} {'run_before':>10} {'stop':>10} {'corrects':>8} {'held':>5}")
    for leg in pos.legs:
        print(
            f"{leg['id']:>7} {leg['seq']:>3} {leg['kind']:<5} {leg['shares']:>6} {leg['price']:>10} "
            f"{leg['flag']:<9} {leg['source']:<11} {leg['preset'] or '—':<6} {leg['running_before']:>10} "
            f"{leg['stop_in_force']:>10} {leg['corrects'] or '—':>8} "
            f"{'—' if leg['held_stated'] is None else leg['held_stated']:>5}"
        )
    print(f"running: {pos.running.shares} (basis: {pos.running.basis})")
    r = pos.realized
    figure = r.reason if r.value is None else f"{r.value.quantize(Decimal('0.01'))}"
    print(f"realized R: {figure} {'provisional' if r.provisional else 'final'} [{r.function_id}]")
    print(f"stop owner: {CardStore().stop_owner(args.card_id)}")


def cmd_trade_note(args: argparse.Namespace) -> None:
    """S3 C4-4: re-write one FILLED or CLOSED card's trade note — the SAME
    writer as the fill (`upsert_trade_note`, create or update) and one
    `upsert_unit` per current leg seq; sets `trade_note_path`. Prints the
    path and each unit's action. A refusal (`market_reset`, a card not
    FILLED / CLOSED, a path another card holds) exits non-zero, verbatim;
    any failure after the gate leaves `trade_note_path` NULL (L1)."""
    from cobalt.prefill.trade_note import write_card_note
    from cobalt.session import SessionBlocked

    try:
        note = write_card_note(args.card_id, retry=True)
    except SessionBlocked as blocked:
        raise SystemExit(f"REFUSED card {args.card_id}: {blocked} Nothing written.")
    except Exception as failed:
        raise SystemExit(
            f"FAILED card {args.card_id}: trade note NOT written: {failed} — trade_note_path NULL"
        )
    print(f"card {args.card_id}: trade note {note.action}: {note.path}")
    for unit, action in note.units:
        print(f"  {unit}: {action}")
    print(f"trade_note_path: {note.relative}")


def cmd_picks(args: argparse.Namespace) -> None:
    """F3: pick vs rank for every FILLED transition on one ET day.

    Exit 1 when any counted FILLED transition has no pick row (MISSING).
    `--cutoff` (the P4 deploy instant) keeps earlier gaps visible but not
    counted — the K6 smoke check's comparison window.
    """
    day = date.fromisoformat(args.date) if args.date else session_clock().to_et(now_utc()).date()
    cutoff = None
    if args.cutoff:
        cutoff = datetime.fromisoformat(args.cutoff)
        if cutoff.tzinfo is None:
            raise SystemExit(
                f"--cutoff {args.cutoff!r} has no timezone; pass an offset (…-04:00) or a 'Z'."
            )
    rows = [PickReportRow(**row) for row in _store().filled_with_picks(day)]
    if not rows:
        print(f"no FILLED transitions on {day.isoformat()}")
        return
    text, missing = render_picks_report(rows, day=day, cutoff=cutoff)
    print(text)
    if missing:
        raise SystemExit(1)


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
    from cobalt.jobs.entrypoint import as_job

    with as_job("com.cobalt.cards-expire", skip=args.dry_run) as job:
        job.result = _expire(args)


def _expire(args: argparse.Namespace) -> dict:
    store = _store()
    ts = _at(args)
    print(f"database  : {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    print(f"checked at: {session_clock().to_et(ts):%Y-%m-%d %H:%M:%S %Z}")
    moved = expire_due(store, now=ts, dry_run=args.dry_run)
    if not moved:
        print("no cards past their window.")
        return {"expired": 0}
    for row in moved:
        print(
            f"  card {row['card_id']:<6} {row['ticker']:<6} {row['from_state']:<9} "
            f"-> EXPIRED   window {row['window_end']} ({row['window_source']})"
        )
    print(f"{len(moved)} card(s) {'would be' if args.dry_run else ''} expired.")
    return {"expired": len(moved), "card_ids": [r["card_id"] for r in moved]}


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

    legs = csub.add_parser(
        "legs", help="One card's current legs, running (and its basis), realized R, stop owner. Read only."
    )
    legs.add_argument("card_id", type=int)
    legs.set_defaults(func=cmd_legs)

    trade_note = csub.add_parser(
        "trade-note",
        help="Re-write a FILLED or CLOSED card's trade note and one unit per current leg; sets trade_note_path.",
    )
    trade_note.add_argument("card_id", type=int)
    trade_note.set_defaults(func=cmd_trade_note)

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

    picks = csub.add_parser(
        "picks", help="F3: pick vs pool/card-score rank for every FILLED card that day."
    )
    picks.add_argument("--date", help="ET trading day YYYY-MM-DD (default: today ET).")
    picks.add_argument(
        "--cutoff",
        help="ISO 8601 instant WITH offset; gaps before it print but do not fail (K6).",
    )
    picks.set_defaults(func=cmd_picks)

    trail = csub.add_parser(
        "trail-fit-draft",
        help="Write the trail_fit -> source: human review DRAFT (R5). Touches no note; no apply exists.",
    )
    trail.add_argument("--out", help="Draft path (default: docs/40 - DevDocs/reports/trail-fit-draft-<date>.md).")
    trail.set_defaults(func=_trail_fit_draft)

    shadow = csub.add_parser(
        "shadow-report",
        help="Per-factor shadow agreement vs card.shadow_promotion_bar (STEP-10). Read-only; flips nothing.",
    )
    shadow.add_argument("--since", help="First ET trading date to include (YYYY-MM-DD).")
    shadow.set_defaults(func=_shadow_report)


def _trail_fit_draft(args: argparse.Namespace) -> None:
    from .trail_fit_draft import cmd_trail_fit_draft

    cmd_trail_fit_draft(args)


def _shadow_report(args: argparse.Namespace) -> None:
    from .shadow_report import cmd_shadow_report

    cmd_shadow_report(args)


__all__ = ["add_parser"]
