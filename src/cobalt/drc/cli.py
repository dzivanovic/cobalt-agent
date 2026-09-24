"""`cobalt drc` — the DRC command group (K1; D3's `cobalt drc build`
joins THIS group later, never a second one, L3).

    cobalt drc state-book --opening DAY (--flat | --position SYMBOL DIRECTION SHARES [AVG_COST] ...)
    cobalt drc state-book --no-trade DAY
    cobalt drc state-book --resolve DAY TRADE_ID [--exit-price P] [--exit-time T]
        [--supersedes ID] [--apply --sha256 HASH]

The landing set's statement caller while K3's `/drc` form is not checked
(R52 (c); v3 `[F-10]`). DRY-RUN BY DEFAULT: it prints the row it would
write and its `book_sha256`, and writes nothing. It writes only with
`--apply --sha256 <that hash>` — L7's interim clause: his chat word plus
the hash approve, and what is written is byte-identical to what was
reviewed (the `cobalt settings load` shape).

It inserts NOTHING itself (L3, L40): the preview and the write are both
`DrcStore`'s, with `via = cli` (R52 (a)); `turn_id` and `readback_sha256`
stay NULL (voice caller only). It writes no vault note (L28).
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from pydantic import ValidationError

from cobalt.session import SessionBlocked

from .models import PairingError, StatedBook

VIA = "cli"


@dataclass(frozen=True)
class StateBookRequest:
    """What one `state-book` invocation asks for, validated for shape
    (the store validates the positions themselves)."""

    day: date
    kind: str
    positions: list[dict] = field(default_factory=list)
    supersedes: Optional[int] = None
    apply: bool = False
    sha256: Optional[str] = None


def _day(text: str) -> date:
    try:
        return date.fromisoformat(text)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"not a YYYY-MM-DD day: {text!r}") from e


def _aware(text: str) -> datetime:
    try:
        ts = datetime.fromisoformat(text)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"not an ISO-8601 time: {text!r}") from e
    if ts.tzinfo is None:
        raise argparse.ArgumentTypeError(f"{text!r} has no UTC offset — a naive time is refused")
    return ts


def _refuse(message: str) -> None:
    print(f"cobalt drc state-book: {message}")
    raise SystemExit(2)


def request_from_args(args: argparse.Namespace) -> StateBookRequest:
    """The parsed flags → one request, or exit 2 naming the misuse."""
    positions: list[dict] = []
    if args.opening is not None:
        kind, day = "opening", args.opening
        if bool(args.flat) == bool(args.position):
            _refuse("--opening takes exactly one of --flat or --position")
        for values in args.position or []:
            if len(values) not in (3, 4):
                _refuse(f"--position takes SYMBOL DIRECTION SHARES [AVG_COST], got {len(values)} value(s)")
            symbol, direction, shares, *cost = values
            positions.append({
                "symbol": symbol, "direction": direction, "shares": shares,
                "avg_cost": cost[0] if cost else None,
            })
    else:
        if args.flat or args.position:
            _refuse("--flat / --position belong to --opening only")
        if args.no_trade is not None:
            kind, day = "no_trade", args.no_trade
        else:
            kind = "resolve"
            try:
                day = _day(args.resolve[0])
            except argparse.ArgumentTypeError as e:
                _refuse(f"--resolve: {e}")
            trade_id = args.resolve[1]
            positions.append({"trade_id": trade_id, "exit_price": args.exit_price, "exit_time": args.exit_time})
    if kind != "resolve" and (args.exit_price is not None or args.exit_time is not None):
        _refuse("--exit-price / --exit-time belong to --resolve only")
    if args.apply and not args.sha256:
        _refuse("--apply writes only the reviewed row: pass --sha256 <the printed book_sha256>")
    return StateBookRequest(
        day=day, kind=kind, positions=positions, supersedes=args.supersedes,
        apply=bool(args.apply), sha256=args.sha256,
    )


def _print_row(row: StatedBook) -> None:
    print(f"day: {row.day.isoformat()}")
    print(f"kind: {row.kind}")
    print(f"positions: {json.dumps(row.positions, sort_keys=True, separators=(',', ':'), ensure_ascii=False)}")
    print(f"reason: {row.reason}")
    print(f"via: {row.via}")
    print(f"supersedes: {row.supersedes if row.supersedes is not None else '-'}")
    print(f"book_sha256: {row.book_sha256}")


def cmd_state_book(args: argparse.Namespace) -> None:
    from .store import DrcStore

    req = request_from_args(args)
    store = DrcStore()
    try:
        if not req.apply:
            preview = store.preview_stated_book(
                req.day, req.kind, req.positions, via=VIA, supersedes=req.supersedes
            )
            print("cobalt drc state-book — DRY RUN\n")
            _print_row(preview)
            print(
                "\nDRY RUN — nothing written. To write: the same command with "
                f"--apply --sha256 {preview.book_sha256}"
            )
            return
        row = store.record_stated_book(
            req.day, req.kind, req.positions, via=VIA, supersedes=req.supersedes,
            expected_sha256=req.sha256,
        )
    except (SessionBlocked, PairingError, ValueError, ValidationError) as e:
        print(f"REFUSED: {e}")
        raise SystemExit(1) from e
    print("cobalt drc state-book — APPLY\n")
    _print_row(row)
    print(f"\nwritten: {DrcStore.STATED_TABLE} #{row.id} (book_sha256 {row.book_sha256})")


def add_parser(sub) -> None:
    group = sub.add_parser("drc", help="The DRC (daily report card) commands")
    gsub = group.add_subparsers(dest="command", required=True)

    state = gsub.add_parser(
        "state-book",
        help="State a day's opening book, a no-trade DRC, or a resolve (dry run unless --apply --sha256).",
    )
    what = state.add_mutually_exclusive_group(required=True)
    what.add_argument("--opening", metavar="DAY", type=_day, help="The book DAY opened with.")
    what.add_argument("--no-trade", dest="no_trade", metavar="DAY", type=_day,
                      help="DAY's no-trade DRC input.")
    what.add_argument("--resolve", nargs=2, metavar=("DAY", "TRADE_ID"),
                      help="A carried trade closed outside the export.")
    state.add_argument("--flat", action="store_true", help="--opening: nothing was held.")
    state.add_argument(
        "--position", action="append", nargs="+", metavar="VALUE",
        help="--opening: SYMBOL DIRECTION SHARES [AVG_COST]; repeatable.",
    )
    state.add_argument("--exit-price", dest="exit_price", metavar="P", help="--resolve: the exit price, if known.")
    state.add_argument("--exit-time", dest="exit_time", metavar="T", type=_aware,
                       help="--resolve: ISO-8601 with its UTC offset, if known.")
    state.add_argument("--supersedes", type=int, metavar="ID", help="The current row this restates.")
    state.add_argument("--apply", action="store_true", help="Write the row (needs --sha256).")
    state.add_argument("--sha256", metavar="HASH", help="The book_sha256 the dry run printed.")
    state.set_defaults(func=cmd_state_book)


__all__ = ["StateBookRequest", "add_parser", "cmd_state_book", "request_from_args"]
