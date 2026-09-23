"""FIFO pairing, carried positions and the stats match (DRC D1-3 / D1-4).

ONE pairing function (L3): `pair_day`. Executions are taken oldest
first (`trading_log.chronological`), per symbol, FIFO:

- `B` opens or adds to a long, or reduces a short (E1: a cover is `B`);
- `SS` opens or adds to a short;
- `S` reduces a long.

A trade closes when its position returns to 0. A position still held at
file end is an OPEN trade with its held shares (R67), never a failure.

FAILS THE WHOLE FILE (`PairingError`, L1):
- one execution taking a position THROUGH 0 (E1 shows no reversal, so
  the export is not proven to book one that way — v2 `[F-13]`);
- a sell of a symbol with no long position, or a side that contradicts
  the open position — with no seed that is "a carried symbol with no
  prior row", named (v2 `[F-10]`);
- a file contradicting the seed of a carried position;
- a broken import chain (`check_contiguity`, the ASK-DESK safe default).

THE SEED. The prior day's stored open positions; each keeps its
`trade_id` and remaining FIFO lots, so realized P&L on the closing day
uses the prices the lots were opened at. `unrealized: not computed`
(v2 `[F-10]`).

THE STATS MATCH (D1-4). EXACT on what both files carry: symbol +
direction + entry time to the second (E1: 4 of 4). No tolerance exists
(L53). A stats row matching zero or several trades is `unmatched`,
carried and shown, never dropped, never guessed.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from datetime import date, datetime, time
from decimal import Decimal
from typing import Iterable, Optional
from zoneinfo import ZoneInfo

from . import stats_log, trading_log
from .models import (
    DayPairing,
    Direction,
    ExecSide,
    Execution,
    Leg,
    Lot,
    OpenPosition,
    PairingError,
    ParsedStatsLog,
    ParsedTradingLog,
    StatsRow,
    Trade,
    TradeStatus,
    Unmatched,
)

#: Bumped whenever a derived figure's rule changes (L57).
FN_VERSION = "drc.pairing/1"


def trade_id(symbol: str, direction: Direction, entry_time: datetime) -> str:
    """Stable across days: a carried trade keeps the id it opened with."""
    return f"{symbol}-{direction.value}-{entry_time.isoformat()}"


@dataclass
class _Book:
    symbol: str
    direction: Direction
    trade_id: str
    entry_time: datetime
    lots: deque = field(default_factory=deque)
    entries: list = field(default_factory=list)
    exits: list = field(default_factory=list)
    realized: Decimal = Decimal(0)
    carried_from: Optional[date] = None

    @property
    def held(self) -> int:
        return sum(lot.shares for lot in self.lots)


def _avg(legs: list[Leg]) -> Optional[Decimal]:
    shares = sum(leg.shares for leg in legs)
    if not shares:
        return None
    return sum(leg.price * leg.shares for leg in legs) / shares


def _trade(book: _Book, status: TradeStatus) -> Trade:
    exit_time = book.exits[-1].time if status is TradeStatus.CLOSED else None
    return Trade(
        trade_id=book.trade_id,
        symbol=book.symbol,
        direction=book.direction,
        status=status,
        entry_time=book.entry_time,
        exit_time=exit_time,
        hold_seconds=int((exit_time - book.entry_time).total_seconds()) if exit_time else None,
        avg_entry=_avg(book.entries),
        avg_exit=_avg(book.exits),
        shares=sum(leg.shares for leg in book.entries),
        held_shares=book.held,
        gross_pnl=book.realized,
        entries=list(book.entries),
        legs=list(book.exits),
        carried_from=book.carried_from,
    )


def _reduce(book: _Book, e: Execution) -> None:
    remaining = e.qty
    while remaining:
        lot = book.lots[0]
        take = min(lot.shares, remaining)
        per_share = e.price - lot.price if book.direction is Direction.LONG else lot.price - e.price
        book.realized += per_share * take
        remaining -= take
        if take == lot.shares:
            book.lots.popleft()
        else:
            book.lots[0] = Lot(time=lot.time, price=lot.price, shares=lot.shares - take)
    book.exits.append(Leg(kind="exit", time=e.time, price=e.price, shares=e.qty, line=e.line))


def _open(e: Execution, direction: Direction) -> _Book:
    book = _Book(e.symbol, direction, trade_id(e.symbol, direction, e.time), e.time)
    _add(book, e)
    return book


def _add(book: _Book, e: Execution) -> None:
    book.lots.append(Lot(time=e.time, price=e.price, shares=e.qty))
    book.entries.append(Leg(kind="entry", time=e.time, price=e.price, shares=e.qty, line=e.line))


def _seeded(position: OpenPosition) -> _Book:
    book = _Book(
        position.symbol,
        position.direction,
        position.trade_id,
        position.entry_time,
        carried_from=position.opened_on,
    )
    for lot in position.lots:
        book.lots.append(lot)
        book.entries.append(Leg(kind="entry", time=lot.time, price=lot.price, shares=lot.shares, carried=True))
    if book.held != position.held_shares:
        raise PairingError(
            f"seed for {position.symbol}: lots hold {book.held} shares, the seed says "
            f"{position.held_shares}"
        )
    return book


def pair_day(
    executions: Iterable[Execution],
    day: date,
    seed: Iterable[OpenPosition] = (),
) -> DayPairing:
    """Executions of ONE import day → trades + the positions left open."""
    books: dict[str, _Book] = {}
    seeded: set[str] = set()
    for position in seed:
        if position.symbol in books:
            raise PairingError(f"seed carries {position.symbol} twice")
        books[position.symbol] = _seeded(position)
        seeded.add(position.symbol)

    execs = list(executions)
    for e in execs:
        absent = [
            c for c, v in zip(trading_log.PAIRING_INPUTS, (e.time, e.symbol, e.side, e.price, e.qty)) if v is None
        ]
        if absent:
            raise PairingError(f"line {e.line}: pairing needs {', '.join(absent)}")

    trades: list[Trade] = []
    for e in trading_log.chronological(execs):
        book = books.get(e.symbol)
        where = f"line {e.line} ({e.symbol} {e.side.value} {e.qty})"
        seed_note = " — contradicts the seed" if e.symbol in seeded else ""
        if book is None:
            if e.side is ExecSide.BUY:
                books[e.symbol] = _open(e, Direction.LONG)
            elif e.side is ExecSide.SELL_SHORT:
                books[e.symbol] = _open(e, Direction.SHORT)
            else:
                raise PairingError(
                    f"{where}: a sell of {e.symbol} with no long position — a carried symbol "
                    f"with no prior row ({e.symbol}); never assumed flat"
                )
            continue
        long_ = book.direction is Direction.LONG
        if (long_ and e.side is ExecSide.BUY) or (not long_ and e.side is ExecSide.SELL_SHORT):
            _add(book, e)
        elif (long_ and e.side is ExecSide.SELL) or (not long_ and e.side is ExecSide.BUY):
            if e.qty > book.held:
                raise PairingError(
                    f"{where}: takes a {book.held}-share {book.direction.value} position through 0 "
                    f"in one execution{seed_note} — the export is not proven to book a reversal"
                )
            _reduce(book, e)
            if book.held == 0:
                trades.append(_trade(book, TradeStatus.CLOSED))
                del books[e.symbol]
                seeded.discard(e.symbol)
        else:
            raise PairingError(
                f"{where}: {e.side.value} while {book.held} shares {book.direction.value} are held"
                f"{seed_note or ' — contradicts the open position'}"
            )

    open_positions: list[OpenPosition] = []
    for book in books.values():
        trades.append(_trade(book, TradeStatus.OPEN))
        open_positions.append(
            OpenPosition(
                trade_id=book.trade_id,
                symbol=book.symbol,
                direction=book.direction,
                held_shares=book.held,
                lots=list(book.lots),
                entry_time=book.entry_time,
                opened_on=book.carried_from or day,
                day=day,
            )
        )
    trades.sort(key=lambda t: (t.entry_time, t.symbol))
    return DayPairing(day=day, trades=trades, open_positions=open_positions)


def check_contiguity(
    day: date,
    prior_trading_day: date,
    recorded_days: Iterable[date],
) -> None:
    """The ASK-DESK safe default of D1-3 (E1 starts flat, so a seed has no
    cross-check): once ANY earlier day is recorded, the PRIOR TRADING DAY
    must be recorded too — an import or a no-trade day — or a lawfully
    skipped day would seed a phantom position. Fails loud, invents
    nothing. The very first import has no history and passes."""
    earlier = {d for d in recorded_days if d < day}
    if earlier and prior_trading_day not in earlier:
        raise PairingError(
            f"{day}: the prior trading day {prior_trading_day} has no import and no no-trade "
            f"record, while {max(earlier)} does — a skipped day would carry a phantom position"
        )


_ET = ZoneInfo("America/New_York")


def match_stats(
    pairing: DayPairing,
    stats: ParsedStatsLog,
) -> DayPairing:
    """Attach each stats row to the ONE trade it names, exactly."""
    absent = [c for c in stats_log.MATCH_INPUTS if c in stats.result.missing]
    if absent:
        why = f"unmatched — missing: {', '.join(absent)}"
        return pairing.model_copy(
            update={
                "unmatched": [Unmatched(row=r, reason=why) for r in stats.rows],
                "not_computed": {**pairing.not_computed, "match": f"not computed — missing: {', '.join(absent)}"},
            }
        )

    claims: dict[str, list[StatsRow]] = {}
    unmatched: list[Unmatched] = []
    for row in stats.rows:
        empty = [
            c for c, v in zip(stats_log.MATCH_INPUTS, (row.symbol, row.side, row.open_time, row.open_time)) if v is None
        ]
        if empty:
            unmatched.append(Unmatched(row=row, reason=f"unmatched — empty: {', '.join(dict.fromkeys(empty))}"))
            continue
        hits = [
            t
            for t in pairing.trades
            if t.symbol == row.symbol and t.direction is row.side and t.entry_time == row.open_time
        ]
        if len(hits) != 1:
            unmatched.append(Unmatched(row=row, reason=f"unmatched — {len(hits)} trades match"))
            continue
        claims.setdefault(hits[0].trade_id, []).append(row)

    by_id: dict[str, StatsRow] = {}
    for tid, rows in claims.items():
        if len(rows) == 1:
            by_id[tid] = rows[0]
        else:
            unmatched.extend(Unmatched(row=r, reason=f"unmatched — {len(rows)} stats rows claim one trade") for r in rows)

    trades = [
        t.model_copy(update={"stats": by_id[t.trade_id], "playbooks": list(by_id[t.trade_id].playbooks)})
        if t.trade_id in by_id
        else t
        for t in pairing.trades
    ]
    unmatched.sort(key=lambda u: u.row.line)
    return pairing.model_copy(update={"trades": trades, "unmatched": unmatched})


def build_day(
    trading: ParsedTradingLog,
    stats: Optional[ParsedStatsLog] = None,
    seed: Iterable[OpenPosition] = (),
) -> DayPairing:
    """A parsed day → its pairing (+ the stats match when a stats log is
    given). A step whose input columns are absent does not run and says
    so, `not computed — missing: <columns>` (R17 (5))."""
    if "pairing" in trading.result.not_computed:
        pairing = DayPairing(day=trading.import_date, not_computed=dict(trading.result.not_computed))
        if stats is not None:
            pairing = pairing.model_copy(
                update={
                    "unmatched": [Unmatched(row=r, reason="unmatched — no trades were paired") for r in stats.rows],
                    "not_computed": {**pairing.not_computed, "match": "not computed — pairing did not run"},
                }
            )
        return pairing
    pairing = pair_day(trading.executions, trading.import_date, seed)
    return match_stats(pairing, stats) if stats is not None else pairing


__all__ = [
    "FN_VERSION",
    "build_day",
    "check_contiguity",
    "match_stats",
    "pair_day",
    "trade_id",
]
