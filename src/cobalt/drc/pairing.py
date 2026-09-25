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
- a broken import chain (`check_contiguity`, the ASK-DESK safe default);
- a seed whose prior day's pairing was not computed (store.seed_for).

THE SEED. The book the day starts from, held by the caller: the prior
day's stored open positions (carried — each keeps its `trade_id` and
remaining FIFO lots, so realized P&L on the closing day uses the prices
the lots were opened at), or the positions he STATED for that day (v3
§2c option A). `unrealized: not computed` (v2 `[F-10]`). `build_day`'s
`seed=None` means NO BOOK WAS STATED: the day is not paired and says so,
`not computed — opening book not stated` — never an assumed flat book
(L1; v3 `:118` retires R22's "A for now"). A list, even `[]`, is the book
the caller holds. `pair_day` is the FIFO engine and holds no book policy.

A STATED lot with no cost carries no price: a reduction against it moves
shares only, and the trade's realized figure is the literal
`not computed — carried cost not stated` (v3 `[F-04]`), never a number.

THE BOOK HASH (`book_sha256`, v3 X4): sha256 of the canonical JSON of the
positions — `model_dump(mode="json")` sorted by `trade_id`, `json.dumps`
with sorted keys, `(",", ":")` separators, UTF-8. `[]` hashes `b"[]"`.

THE STATS MATCH (D1-4). EXACT on what both files carry: symbol +
direction + entry time to the second (E1: 4 of 4). No tolerance exists
(L53). A stats row matching zero or several trades is `unmatched`,
carried and shown, never dropped, never guessed.
"""

from __future__ import annotations

import hashlib
import json
from collections import deque
from dataclasses import dataclass, field
from datetime import date, datetime, time
from decimal import Decimal
from typing import Iterable, Optional, Union
from zoneinfo import ZoneInfo

from . import stats_log, trading_log
from .models import (
    CARRIED_COST_NOT_STATED,
    EXIT_NOT_IN_ANY_EXPORT,
    OPENING_NOT_STATED,
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
    ResolveInput,
    ResolveOutcome,
    StatedPosition,
    StatedResolve,
    StatsRow,
    Trade,
    TradeStatus,
    Unmatched,
)

#: Bumped whenever a derived figure's rule changes (L57). /2 (K1): an
#: unstated book is not paired; a stated lot may carry no cost. /3 (K2):
#: a later day is re-paired from the earlier close (R51); a resolve
#: closes a carried trade outside the export (`[F-06]`).
FN_VERSION = "drc.pairing/3"


def trade_id(symbol: str, direction: Direction, entry_time: datetime) -> str:
    """Stable across days: a carried trade keeps the id it opened with."""
    return f"{symbol}-{direction.value}-{entry_time.isoformat()}"


def stated_trade_id(symbol: str, direction: Direction, day: date) -> str:
    """A stated position has no entry time: its id names the day it was
    stated for, stable across restatements of that day (the drafter's pin,
    carried to the K1 check — v3 names no shape)."""
    return f"{symbol}-{direction.value}-stated-{day.isoformat()}"


def canonical_sha256(rows: list[dict]) -> str:
    """sha256 hex of `rows`' canonical JSON bytes — THE PINNED ENCODING
    (v3 X4). The caller orders `rows`; the keys are sorted here."""
    data = json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def book_sha256(positions: Iterable[OpenPosition]) -> str:
    """The book hash: the positions' JSON dumps sorted by `trade_id`."""
    return canonical_sha256(
        [p.model_dump(mode="json") for p in sorted(positions, key=lambda p: p.trade_id)]
    )


def stated_open_positions(day: date, positions: Iterable[StatedPosition]) -> list[OpenPosition]:
    """His stated `opening` book for `day` as the pairing's seed: ONE lot
    per position, its cost `None` when he gave none, NO time (v3
    `[F-04]`; never an invented one), its open day not stated."""
    return [
        OpenPosition(
            trade_id=stated_trade_id(p.symbol, p.direction, day),
            symbol=p.symbol,
            direction=p.direction,
            held_shares=p.shares,
            lots=[Lot(time=None, price=p.avg_cost, shares=p.shares)],
            entry_time=None,
            opened_on=None,
            day=day,
        )
        for p in positions
    ]


@dataclass
class _Book:
    symbol: str
    direction: Direction
    trade_id: str
    entry_time: Optional[datetime]
    lots: deque = field(default_factory=deque)
    entries: list = field(default_factory=list)
    exits: list = field(default_factory=list)
    realized: Union[Decimal, str] = Decimal(0)
    carried_from: Optional[date] = None
    seeded: bool = False

    @property
    def held(self) -> int:
        return sum(lot.shares for lot in self.lots)


def _avg(legs: list[Leg]) -> Optional[Decimal]:
    shares = sum(leg.shares for leg in legs)
    if not shares or any(leg.price is None for leg in legs):
        return None
    return sum(leg.price * leg.shares for leg in legs) / shares


def _trade(book: _Book, status: TradeStatus) -> Trade:
    # A resolved trade (K2, X11) is CLOSED with no exit leg when its exit
    # time or price is not stored: no exit time, never an invented one.
    exit_time = book.exits[-1].time if status is TradeStatus.CLOSED and book.exits else None
    return Trade(
        trade_id=book.trade_id,
        symbol=book.symbol,
        direction=book.direction,
        status=status,
        entry_time=book.entry_time,
        exit_time=exit_time,
        # A stated position has no entry time, so no hold time either.
        hold_seconds=(
            int((exit_time - book.entry_time).total_seconds())
            if exit_time and book.entry_time
            else None
        ),
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
        if lot.price is None:
            # A stated lot with no cost (v3 `[F-04]`): shares move, no
            # price arithmetic runs, and the figure says why.
            book.realized = CARRIED_COST_NOT_STATED
        elif book.realized != CARRIED_COST_NOT_STATED:
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
        seeded=True,
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


def resolved_trade(position: OpenPosition, resolve: StatedResolve) -> Trade:
    """A carried position closed outside the export (v3 `[F-06]`, X11),
    built THROUGH `_trade` from its seeded book. The exit leg exists only
    when both the exit price and time are stored (an exit leg is an
    execution, K1). Realized: no exit price → `EXIT_NOT_IN_ANY_EXPORT`; a
    lot with no cost → `CARRIED_COST_NOT_STATED`; else FIFO over the lots
    at the exit price, signed by direction — never a guess (L1, L57)."""
    book = _seeded(position)
    price = resolve.exit_price
    if price is None:
        book.realized = EXIT_NOT_IN_ANY_EXPORT
    elif any(lot.price is None for lot in book.lots):
        book.realized = CARRIED_COST_NOT_STATED
    else:
        long_ = book.direction is Direction.LONG
        book.realized = sum(
            ((price - lot.price) if long_ else (lot.price - price)) * lot.shares for lot in book.lots
        )
    if price is not None and resolve.exit_time is not None:
        book.exits.append(Leg(kind="exit", time=resolve.exit_time, price=price, shares=book.held, line=None))
    book.lots.clear()
    return _trade(book, TradeStatus.CLOSED)


def stated_differs(stated: Iterable[OpenPosition], close: Iterable[OpenPosition]) -> list[str]:
    """R51's comparison of his stated book with the recorded close: the
    two books as multisets of `(symbol, direction, shares)` — never the
    open day, the cost or the `trade_id` (`48` `## FOR K2`). Returns the
    sorted trade ids of every position in EITHER book with no equal
    counterpart in the other; `[]` when the books are equal."""
    unmatched: list[str] = []
    pools: dict[tuple, list[str]] = {}
    for p in sorted(close, key=lambda p: p.trade_id):
        pools.setdefault((p.symbol, p.direction, p.held_shares), []).append(p.trade_id)
    for p in sorted(stated, key=lambda p: p.trade_id):
        pool = pools.get((p.symbol, p.direction, p.held_shares))
        if pool:
            pool.pop(0)
        else:
            unmatched.append(p.trade_id)
    unmatched.extend(tid for pool in pools.values() for tid in pool)
    return sorted(unmatched)


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
                # A seeded book keeps its position's open day, None
                # included; a book opened today opened today.
                opened_on=book.carried_from if book.seeded else day,
                day=day,
            )
        )
    trades.sort(key=_trade_order)
    return DayPairing(day=day, trades=trades, open_positions=open_positions)


def _trade_order(t: Trade) -> tuple:
    # A stated position (no entry time) sorts first, by symbol — never
    # given an invented time to sort by.
    return (t.entry_time is not None, t.entry_time.timestamp() if t.entry_time else 0.0, t.symbol)


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
        # `open_time` is the combined date + time: None proves only that one
        # of the two cells is empty, so the pair is named jointly.
        empty = [
            c
            for c, v in (
                (stats_log.SYMBOL, row.symbol),
                (stats_log.SIDE, row.side),
                (f"{stats_log.OPEN_DATE} or {stats_log.OPEN_TIME}", row.open_time),
            )
            if v is None
        ]
        if empty:
            unmatched.append(Unmatched(row=row, reason=f"unmatched — empty: {', '.join(empty)}"))
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


def _apply_resolves(
    day: date,
    executions: list[Execution],
    seed: list[OpenPosition],
    resolves: Iterable[ResolveInput],
) -> tuple[list[OpenPosition], list[Trade], list[ResolveOutcome]]:
    """`[F-06]` on the day a resolve names: the day's export touches the
    symbol → the export is the truth and the resolve is superseded (R67);
    otherwise the position leaves the book as a resolved trade."""
    by_id = {p.trade_id: p for p in seed}
    touched = {e.symbol for e in executions}
    left, trades, outcomes = list(seed), [], []
    for r in resolves:
        tid = r.resolve.trade_id
        position = by_id.get(tid)
        if position is None:
            raise PairingError(f"{day}: resolve #{r.id} names {tid}, which {day}'s opening book does not hold")
        if position.symbol in touched:
            outcomes.append(ResolveOutcome(
                resolve_id=r.id, trade_id=tid, status="superseded",
                reason=f"superseded — {day}'s export touches {position.symbol} (R67: the export is the truth)",
            ))
            continue
        left.remove(position)
        trades.append(resolved_trade(position, r.resolve))
        outcomes.append(ResolveOutcome(
            resolve_id=r.id, trade_id=tid, status="applied",
            reason=f"applied — closed outside the export (resolve #{r.id})",
        ))
    return left, trades, outcomes


def build_day(
    trading: ParsedTradingLog,
    stats: Optional[ParsedStatsLog] = None,
    seed: Optional[Iterable[OpenPosition]] = None,
    resolves: Iterable[ResolveInput] = (),
) -> DayPairing:
    """A parsed day → its pairing (+ the stats match when a stats log is
    given). A step whose input columns are absent does not run and says
    so, `not computed — missing: <columns>` (R17 (5)). `seed=None` means
    no book was stated: the day is not paired, `not computed — opening
    book not stated` (L1, v3 §2c); a list, even `[]`, is the book.

    `resolves` (K2) are the stored resolves dated this day, each naming a
    position of `seed` (`SeedBook.resolves`); a not-computed day applies
    none. Their outcomes are `DayPairing.resolves`."""
    not_computed = dict(trading.result.not_computed)
    if "pairing" not in not_computed and seed is None:
        not_computed["pairing"] = OPENING_NOT_STATED
    if "pairing" in not_computed:
        pairing = DayPairing(day=trading.import_date, not_computed=not_computed)
        if stats is not None:
            pairing = pairing.model_copy(
                update={
                    "unmatched": [Unmatched(row=r, reason="unmatched — no trades were paired") for r in stats.rows],
                    "not_computed": {**pairing.not_computed, "match": "not computed — pairing did not run"},
                }
            )
        return pairing
    book, resolved, outcomes = _apply_resolves(
        trading.import_date, trading.executions, list(seed), resolves
    )
    pairing = pair_day(trading.executions, trading.import_date, book)
    if resolved or outcomes:
        trades = [*pairing.trades, *resolved]
        trades.sort(key=_trade_order)
        pairing = pairing.model_copy(update={"trades": trades, "resolves": outcomes})
    return match_stats(pairing, stats) if stats is not None else pairing


__all__ = [
    "FN_VERSION",
    "book_sha256",
    "build_day",
    "canonical_sha256",
    "check_contiguity",
    "match_stats",
    "pair_day",
    "resolved_trade",
    "stated_differs",
    "stated_open_positions",
    "stated_trade_id",
    "trade_id",
]
