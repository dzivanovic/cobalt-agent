"""Typed records for DRC D1 (Pydantic, L1: invalid data never constructs).

`None` is the one spelling of "the file does not carry this" — a
renderer prints it `not given`; nothing here ever fills it with a
default, a zero or a guess (R91, L1). A field that a later step could not
compute because an input column was absent is named on the result's
`not_computed`, never defaulted (R17 (5)).

A STATED position (K1, v3 `[F-04]`) is his word, not a fill: it may carry
no cost and no time. Its lot, its entry leg and its open position then
hold `None` for both — never an invented figure — and a realized figure
against a missing cost is the literal `CARRIED_COST_NOT_STATED`, never a
number (v3 X3).
"""

from __future__ import annotations

import re
from datetime import date
from decimal import Decimal
from enum import Enum
from typing import Literal, Optional, Union

# Every DRC time is timezone-aware: a naive time fails validation (L1).
from pydantic import AwareDatetime as datetime
from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

NOT_GIVEN = "not given"

#: A realized figure against a stated lot with no cost (v3 `[F-04]`).
CARRIED_COST_NOT_STATED = "not computed — carried cost not stated"
#: A day whose opening book was never stated (v3 §2c option A, §4 row 1).
OPENING_NOT_STATED = "not computed — opening book not stated"

_HEX64 = re.compile(r"^[0-9a-f]{64}$")


class Kind(str, Enum):
    """What a dropped file IS, decided by its header alone (R114)."""

    TRADING_LOG = "trading_log"
    STATS_LOG = "stats_log"


class Outcome(str, Enum):
    """Per-file import outcome (R17 (5))."""

    PARSED = "parsed"
    PARTIAL = "partial"
    FAILED = "failed"
    IGNORED = "ignored"


class ExecSide(str, Enum):
    """The trading log's OWN side codes, exactly the three E1 shows. A
    code outside this set fails the row, and so the whole file (L1)."""

    BUY = "B"
    SELL = "S"
    SELL_SHORT = "SS"


class Direction(str, Enum):
    LONG = "long"
    SHORT = "short"


class TradeStatus(str, Enum):
    CLOSED = "closed"
    OPEN = "open"


class _Frozen(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")


class Execution(_Frozen):
    """One row of the trading log. Its DATE is the import date the
    caller passed (R17 (3)); its clock time is the row's own time column,
    read as ET. Every field of a column the file lacks is None."""

    line: int = Field(ge=2)
    time: Optional[datetime] = None
    symbol: Optional[str] = None
    side: Optional[ExecSide] = None
    price: Optional[Decimal] = Field(default=None, gt=0)
    qty: Optional[int] = Field(default=None, gt=0)
    route: Optional[str] = None
    broker: Optional[str] = None
    account: Optional[str] = None
    order_type: Optional[str] = None
    order_id: Optional[str] = None


class Leg(_Frozen):
    """One fill that moved a trade's position: an entry (open / add) or
    an exit (reduce / close). One leg per execution row — split fills
    are never merged (nothing is guessed about which belong together)."""

    kind: Literal["entry", "exit"]
    time: Optional[datetime]   # None only on a STATED entry (K1)
    price: Optional[Decimal]   # None only on a STATED entry with no cost
    shares: int = Field(gt=0)
    line: Optional[int] = None  # None = a lot carried in from a prior day
    carried: bool = False

    @model_validator(mode="after")
    def _an_exit_is_a_fill(self) -> "Leg":
        if self.kind == "exit" and (self.time is None or self.price is None):
            raise ValueError("an exit leg is an execution: its time and price are required")
        return self


class Lot(_Frozen):
    """An open FIFO lot: what is still held, at what price, since when.
    A STATED lot may carry no time and no cost (`None`, v3 `[F-04]`)."""

    time: Optional[datetime]
    price: Optional[Decimal]
    shares: int = Field(gt=0)


class OpenPosition(_Frozen):
    """A position open at the end of a day (R67) — the next day's seed.
    A STATED position has no `entry_time` (K1): never an invented one."""

    trade_id: str
    symbol: str
    direction: Direction
    held_shares: int = Field(gt=0)
    lots: list[Lot]
    entry_time: Optional[datetime]
    # None = not stated — a stated position's open day is his to give (v3 :134 names none); never the stated day (L1).
    opened_on: Optional[date]
    day: date  # the import day whose file left it open


class StatsRow(_Frozen):
    """What ONE row of the stats log carries. Every figure is Optional:
    `None` renders `not given` (R91). `stop` is filled ONLY from a stats-log
    stop column read by a RULED header name — E1 has none, so it is None
    on every row today (R17 (4)); it is never computed from anything."""

    line: int = Field(ge=2)
    symbol: Optional[str] = None
    side: Optional[Direction] = None
    open_time: Optional[datetime] = None
    close_time: Optional[datetime] = None
    entry: Optional[Decimal] = None
    exit: Optional[Decimal] = None
    stop: Optional[Decimal] = None
    target: Optional[Decimal] = None
    assumed_rr: Optional[Decimal] = None
    realized_rr: Optional[Decimal] = None
    price_mae: Optional[Decimal] = None
    price_mfe: Optional[Decimal] = None
    position_mae: Optional[Decimal] = None
    position_mfe: Optional[Decimal] = None
    best_exit: Optional[Decimal] = None
    best_exit_price: Optional[Decimal] = None
    best_exit_time: Optional[datetime] = None
    gross_pnl: Optional[Decimal] = None
    net_pnl: Optional[Decimal] = None
    commission: Optional[Decimal] = None
    fee: Optional[Decimal] = None
    quantity: Optional[Decimal] = None
    executions: Optional[int] = None
    playbooks: list[str] = Field(default_factory=list)


class Trade(_Frozen):
    """One FIFO trade: flat → position → flat (closed), or still held at
    file end (open, R67). Figures come from the executions; the stats-log
    figures ride on `stats` only when exactly one stats row matched."""

    trade_id: str
    symbol: str
    direction: Direction
    status: TradeStatus
    entry_time: Optional[datetime]     # None: a stated position (K1)
    exit_time: Optional[datetime] = None
    hold_seconds: Optional[int] = None
    avg_entry: Optional[Decimal]       # None when any entry has no stated cost
    avg_exit: Optional[Decimal] = None
    shares: int = Field(gt=0)          # every share entered on this trade
    held_shares: int = Field(ge=0)     # 0 when closed
    # Realized on this day's exits only; the literal when any exit met a
    # stated lot with no cost (v3 `[F-04]`) — never None, never a 0.
    gross_pnl: Union[Decimal, Literal["not computed — carried cost not stated"]]
    unrealized: Literal["not computed"] = "not computed"
    entries: list[Leg]
    legs: list[Leg]                    # the exit legs
    carried_from: Optional[date] = None
    playbooks: list[str] = Field(default_factory=list)
    stats: Optional[StatsRow] = None

    @property
    def net_pnl(self) -> Optional[Decimal]:
        """His stats log's own net figure, never computed here."""
        return None if self.stats is None else self.stats.net_pnl

    @property
    def commissions(self) -> Optional[Decimal]:
        """His stats log's own commission figure, never computed here."""
        return None if self.stats is None else self.stats.commission


class Detection(_Frozen):
    """What `detect_kind` decided from a file's first line (R114)."""

    name: str
    kind: Optional[Kind] = None
    outcome: Outcome
    reason: str
    missing: list[str] = Field(default_factory=list)
    extras: list[str] = Field(default_factory=list)

    @property
    def degraded(self) -> Optional[str]:
        """`<kind>_shape` when the header carries names the parser does
        not know (L9: loud, still parsed)."""
        if self.kind is not None and self.extras:
            return f"{self.kind.value}_shape"
        return None

    @property
    def partial_flag(self) -> Optional[str]:
        """The LOUD flag a partial file carries to the page and the DRC."""
        if self.outcome is Outcome.PARTIAL:
            return f"PARTIAL — missing: {', '.join(self.missing)}"
        return None


class ImportResult(_Frozen):
    """One file's result: `parsed` / `partial` / `failed` / `ignored`,
    with the reason and, for a failure, the line that failed it."""

    name: str
    kind: Optional[Kind] = None
    outcome: Outcome
    reason: str = ""
    line: Optional[int] = None
    missing: list[str] = Field(default_factory=list)
    extras: list[str] = Field(default_factory=list)
    not_computed: dict[str, str] = Field(default_factory=dict)

    @property
    def degraded(self) -> Optional[str]:
        if self.kind is not None and self.extras:
            return f"{self.kind.value}_shape"
        return None

    @property
    def partial_flag(self) -> Optional[str]:
        if self.outcome is Outcome.PARTIAL:
            return f"PARTIAL — missing: {', '.join(self.missing)}"
        return None


class ParsedTradingLog(_Frozen):
    result: ImportResult
    import_date: date
    executions: list[Execution] = Field(default_factory=list)


class ParsedStatsLog(_Frozen):
    result: ImportResult
    rows: list[StatsRow] = Field(default_factory=list)


class Unmatched(_Frozen):
    """A stats row that paired with zero or with several trades — carried
    and SHOWN, never dropped, never guessed (D1-4)."""

    row: StatsRow
    reason: str


class DayPairing(_Frozen):
    """One day's pairing: trades, the positions left open, the stats
    rows that did not pair, and every step that could not run."""

    day: date
    trades: list[Trade] = Field(default_factory=list)
    open_positions: list[OpenPosition] = Field(default_factory=list)
    unmatched: list[Unmatched] = Field(default_factory=list)
    not_computed: dict[str, str] = Field(default_factory=dict)


class PairingError(ValueError):
    """The whole file FAILS (L1): a reversal through 0, a seed the file
    contradicts, a carried symbol with no prior row, a broken chain."""


# ---------------------------------------------------------------------
# K1 — the book a day starts from (v3 §2b, §2c, §3)
# ---------------------------------------------------------------------

StatedKind = Literal["opening", "resolve", "no_trade"]
#: Who made a statement (R52 (a): the third literal is `cli`).
Via = Literal["drc_page", "voice_widget", "cli"]


class StatedPosition(_Frozen):
    """One position of a stated `opening` book: his word, not a fill.
    `avg_cost` is optional (v3 `[F-04]`): `None` is stored as `None`."""

    symbol: str = Field(min_length=1)
    direction: Direction
    shares: int = Field(gt=0)
    avg_cost: Optional[Decimal] = Field(default=None, gt=0)


class StatedResolve(_Frozen):
    """The one position of a `resolve` statement: a carried `trade_id`
    closed outside the export (v3 `[F-06]`). Its effect is K2's."""

    trade_id: str = Field(min_length=1)
    exit_price: Optional[Decimal] = Field(default=None, gt=0)
    exit_time: Optional[datetime] = None


class StatedBook(_Frozen):
    """One stated-book row, as `DrcStore` stores it (v3 `:128-141`). `id` and
    `created_at` are None on a preview (nothing written)."""

    id: Optional[int] = None
    day: date
    kind: StatedKind
    positions: list[dict]  # the canonical JSON the hash is taken over
    book_sha256: str
    via: Via
    turn_id: Optional[str] = None
    readback_sha256: Optional[str] = None
    reason: str
    supersedes: Optional[int] = None
    created_at: Optional[datetime] = None

    @field_validator("book_sha256")
    @classmethod
    def _hex64(cls, v: str) -> str:
        if not _HEX64.match(v):
            raise ValueError("book_sha256 must be 64 lowercase hex characters")
        return v


class SeedBook(_Frozen):
    """The book a day's pairing starts from, with where it came from
    (L57, v3 §2b step 3): `carried` from the prior day's hash-checked
    close, or `stated` by his `opening` statement. K2 adds
    `no_trade_carry`."""

    source: Literal["carried", "stated"]
    positions: list[OpenPosition]
    from_day: Optional[date] = None
    from_book_sha256: str
    stated_book_id: Optional[int] = None

    @field_validator("from_book_sha256")
    @classmethod
    def _hex64(cls, v: str) -> str:
        if not _HEX64.match(v):
            raise ValueError("from_book_sha256 must be 64 lowercase hex characters")
        return v

    @model_validator(mode="after")
    def _source_names_its_link(self) -> "SeedBook":
        if self.source == "carried" and (self.from_day is None or self.stated_book_id is not None):
            raise ValueError("a carried book names its from_day and no stated_book_id")
        if self.source == "stated" and (self.stated_book_id is None or self.from_day is not None):
            raise ValueError("a stated book names its stated_book_id and no from_day")
        return self


__all__ = [
    "CARRIED_COST_NOT_STATED",
    "NOT_GIVEN",
    "OPENING_NOT_STATED",
    "DayPairing",
    "Detection",
    "Direction",
    "ExecSide",
    "Execution",
    "ImportResult",
    "Kind",
    "Leg",
    "Lot",
    "OpenPosition",
    "Outcome",
    "PairingError",
    "ParsedStatsLog",
    "ParsedTradingLog",
    "SeedBook",
    "StatedBook",
    "StatedKind",
    "StatedPosition",
    "StatedResolve",
    "StatsRow",
    "Trade",
    "TradeStatus",
    "Unmatched",
    "Via",
]
