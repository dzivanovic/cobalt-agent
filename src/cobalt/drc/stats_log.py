"""The stats-log parser (DRC D1-4) — his trade journal's daily log, one
row per trade (R91: entries, targets, assumed and realized R:R, MAE/MFE,
best exit, playbooks).

READ BY HEADER NAME, REACHED ONLY THROUGH `detect` (R114): the file's
own name and extension are never read.

THE STOP (09-23 R17 (4)). `StatsRow.stop` is read ONLY from a stop
column of THIS log, by header name, and only when that name is a RULED
one. E1's 49-name header carries no stop column, so no name is ruled
(`STOP_COLUMN = None`) and the stop is None — `not given` — on every
row. It is NEVER computed: not from the dollar risk column, the target,
the R:R, the prices or the quantity, alone or together. The day his
export gains a stop column, `detect` reports it as an extra
(`stats_log_shape`, loud); reading it is a later change on his ruling of
the name, with a new real-shape fixture (L45).

TIMES. `Open Date` + `Open Time` (`HH:MM:SS EDT`/`EST`) and the close
pair are read as America/New_York wall-clock time — the same zone as the
trading log's `Time` (E1: 4 of 4 trades pair to the second). The
suffix must be an ET abbreviation; anything else fails the file. The
best-exit time is `YYYY-MM-DD HH:MM:SS UTC`, read as UTC.

PLAYBOOKS (R114). The playbook column is a LIST: one cell may carry
several names (E1: one quoted cell, `, `-separated). Split on the comma,
each name stripped, empty pieces dropped, ORDER KEPT, never
de-duplicated, never one picked. The separate setups column is never
read as a playbook. No name → setup mapping here (D3, R116).

FAIL-LOUD (L1), PARTIAL (R17 (5)) and DEGRADED (L9) follow the trading
log's rules: a bad cell fails the whole file naming the line; an absent
column's field is None on every row; an added column raises
`stats_log_shape`.
"""

from __future__ import annotations

import csv
import io
import re
from datetime import date, datetime, time, timezone
from decimal import Decimal, InvalidOperation
from typing import Optional, Protocol
from zoneinfo import ZoneInfo

from pydantic import ValidationError

from .models import Detection, Direction, ImportResult, Kind, Outcome, ParsedStatsLog, StatsRow

ET = ZoneInfo("America/New_York")

ACCOUNT_NAME = "Account Name"
SYMBOL = "Symbol"
SIDE = "Side"
OPEN_DATE = "Open Date"
OPEN_TIME = "Open Time"
CLOSE_DATE = "Close Date"
CLOSE_TIME = "Close Time"
ENTRY = "Entry Price"
EXIT = "Exit Price"
TARGET = "Initial Target"
ASSUMED_RR = "Reward Ratio"
REALIZED_RR = "Realized RR"
PRICE_MAE = "Price MAE"
PRICE_MFE = "Price MFE"
POSITION_MAE = "Position MAE"
POSITION_MFE = "Position MFE"
BEST_EXIT = "Best Exit"
BEST_EXIT_PRICE = "Best Exit Price"
BEST_EXIT_TIME = "Best Exit Time"
GROSS_PNL = "Gross P&L"
NET_PNL = "Net P&L"
COMMISSION = "Commission"
FEE = "Fee"
QUANTITY = "Quantity"
EXECUTIONS = "Executions"
PLAYBOOK = "Playbook"

#: Every non-empty column name E1's stats-log header shows, in its order,
#: EXCEPT the one column whose name carries a vendor's name (L31: never
#: in code — neither required nor read). THE one copy: `detect` imports
#: it, nothing retypes it (L3). No stop column: E1 has none (R17 (4)).
REQUIRED: tuple[str, ...] = (
    ACCOUNT_NAME,
    "Adjusted Cost",
    "Adjusted Proceeds",
    "Avg Buy Price",
    "Avg Sell Price",
    "Exit Efficiency",
    BEST_EXIT,
    BEST_EXIT_PRICE,
    BEST_EXIT_TIME,
    CLOSE_DATE,
    CLOSE_TIME,
    COMMISSION,
    "Custom Tags",
    "Duration",
    ENTRY,
    EXECUTIONS,
    EXIT,
    GROSS_PNL,
    "Trade Risk",
    TARGET,
    "Instrument",
    "Spread Type",
    "Mistakes",
    NET_PNL,
    "Net ROI",
    OPEN_DATE,
    OPEN_TIME,
    "Pips",
    ASSUMED_RR,
    "Points",
    POSITION_MAE,
    POSITION_MFE,
    PRICE_MAE,
    PRICE_MFE,
    REALIZED_RR,
    "Return Per Pip",
    "Reviewed",
    "Setups",
    SIDE,
    "Status",
    PLAYBOOK,
    SYMBOL,
    "Ticks Value",
    "Ticks Per Contract",
    FEE,
    "Swap",
    "Rating",
    QUANTITY,
)

#: What the trade match reads (D1-4). A `partial` stats log missing any of
#: these leaves every row `unmatched — missing: <columns>` (R17 (5)).
MATCH_INPUTS: tuple[str, ...] = (SYMBOL, SIDE, OPEN_DATE, OPEN_TIME)

#: The ruled header name of his export's stop field. NONE is ruled: E1
#: carries no stop column, and the name is his to give (R17 (4), ASK
#: DESK in the build report). While None, `StatsRow.stop` is None.
STOP_COLUMN: Optional[str] = None

#: StatsRow field ← column, for the plain decimal figures.
_DECIMALS: dict[str, str] = {
    "entry": ENTRY,
    "exit": EXIT,
    "target": TARGET,
    "assumed_rr": ASSUMED_RR,
    "realized_rr": REALIZED_RR,
    "price_mae": PRICE_MAE,
    "price_mfe": PRICE_MFE,
    "position_mae": POSITION_MAE,
    "position_mfe": POSITION_MFE,
    "best_exit": BEST_EXIT,
    "best_exit_price": BEST_EXIT_PRICE,
    "gross_pnl": GROSS_PNL,
    "net_pnl": NET_PNL,
    "commission": COMMISSION,
    "fee": FEE,
    "quantity": QUANTITY,
}
if STOP_COLUMN is not None:  # pragma: no cover - no stop name is ruled yet
    _DECIMALS["stop"] = STOP_COLUMN

_CLOCK_ET = re.compile(r"^(\d{2}):(\d{2}):(\d{2}) (EDT|EST)$")
_UTC_STAMP = re.compile(r"^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2}) UTC$")
_DATE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
_INT = re.compile(r"^\d+$")


class StatsLogError(ValueError):
    def __init__(self, line: int, message: str):
        super().__init__(f"line {line}: {message}")
        self.line = line


class TradeStatsSource(Protocol):
    """Where per-trade statistics come from (L9)."""

    kind: Kind

    def parse(self, data: bytes, detection: Detection) -> ParsedStatsLog:
        ...


def split_playbooks(cell: str) -> list[str]:
    """One playbook cell → every name in it, in order (R114)."""
    return [piece.strip() for piece in cell.split(",") if piece.strip()]


def _decimal(value: str, column: str, line: int) -> Optional[Decimal]:
    if value == "":
        return None
    try:
        d = Decimal(value)
    except InvalidOperation:
        raise StatsLogError(line, f"column {column!r}: {value!r} is not a number") from None
    if not d.is_finite():
        raise StatsLogError(line, f"column {column!r}: {value!r} is not a finite number")
    return d


def _date(value: str, column: str, line: int) -> Optional[date]:
    if value == "":
        return None
    m = _DATE.match(value)
    try:
        if not m:
            raise ValueError
        return date(int(m[1]), int(m[2]), int(m[3]))
    except ValueError:
        raise StatsLogError(line, f"column {column!r}: {value!r} is not YYYY-MM-DD") from None


def _clock(value: str, column: str, line: int) -> Optional[time]:
    if value == "":
        return None
    m = _CLOCK_ET.match(value)
    try:
        if not m:
            raise ValueError
        return time(int(m[1]), int(m[2]), int(m[3]))
    except ValueError:
        raise StatsLogError(
            line, f"column {column!r}: {value!r} is not 'HH:MM:SS EDT' / 'HH:MM:SS EST'"
        ) from None


def _utc(value: str, column: str, line: int) -> Optional[datetime]:
    if value == "":
        return None
    m = _UTC_STAMP.match(value)
    try:
        if not m:
            raise ValueError
        return datetime(*(int(m[i]) for i in range(1, 7)), tzinfo=timezone.utc)
    except ValueError:
        raise StatsLogError(line, f"column {column!r}: {value!r} is not 'YYYY-MM-DD HH:MM:SS UTC'") from None


def _combine(day: Optional[date], clock: Optional[time]) -> Optional[datetime]:
    if day is None or clock is None:
        return None
    return datetime.combine(day, clock, tzinfo=ET)


class StatsLogSource:
    """The one `TradeStatsSource` today: his journal's daily log."""

    kind = Kind.STATS_LOG

    def parse(self, data: bytes, detection: Detection) -> ParsedStatsLog:
        if detection.kind is not Kind.STATS_LOG or detection.outcome not in (
            Outcome.PARSED,
            Outcome.PARTIAL,
        ):
            raise ValueError(
                f"{detection.name}: the stats-log parser is reached only through "
                f"detect_kind → stats_log (got {detection.kind}, {detection.outcome.value})"
            )
        try:
            rows = self._rows(data)
        except StatsLogError as e:
            return ParsedStatsLog(
                result=ImportResult(
                    name=detection.name,
                    kind=Kind.STATS_LOG,
                    outcome=Outcome.FAILED,
                    reason=f"{detection.name}: {e}",
                    line=e.line,
                    missing=list(detection.missing),
                    extras=list(detection.extras),
                )
            )
        absent = [c for c in MATCH_INPUTS if c in detection.missing]
        not_computed = {"match": f"not computed — missing: {', '.join(absent)}"} if absent else {}
        return ParsedStatsLog(
            rows=rows,
            result=ImportResult(
                name=detection.name,
                kind=Kind.STATS_LOG,
                outcome=detection.outcome,
                reason=detection.partial_flag or "",
                missing=list(detection.missing),
                extras=list(detection.extras),
                not_computed=not_computed,
            ),
        )

    def _rows(self, data: bytes) -> list[StatsRow]:
        try:
            text = data.decode("utf-8-sig")
        except UnicodeDecodeError as e:
            raise StatsLogError(1, f"not UTF-8 text ({e.reason})") from None
        records = list(csv.reader(io.StringIO(text, newline="")))
        header = records[0]
        at = {name: i for i, name in enumerate(header) if name in REQUIRED}
        while len(records) > 1 and records[-1] == []:
            records.pop()
        out: list[StatsRow] = []
        for offset, record in enumerate(records[1:]):
            line = offset + 2
            if len(record) != len(header):
                raise StatsLogError(line, f"{len(record)} cells where the header has {len(header)}")

            def cell(column: str) -> Optional[str]:
                return record[at[column]] if column in at else None

            fields: dict[str, object] = {"line": line}
            for field, column in _DECIMALS.items():
                value = cell(column)
                if value is not None:
                    fields[field] = _decimal(value, column, line)
            symbol = cell(SYMBOL)
            if symbol:
                fields["symbol"] = symbol
            side = cell(SIDE)
            if side:
                try:
                    fields["side"] = Direction(side)
                except ValueError:
                    raise StatsLogError(line, f"column {SIDE!r}: {side!r} is not long / short") from None
            executions = cell(EXECUTIONS)
            if executions:
                if not _INT.match(executions):
                    raise StatsLogError(line, f"column {EXECUTIONS!r}: {executions!r} is not a whole number")
                fields["executions"] = int(executions)
            for field, (d_col, t_col) in {
                "open_time": (OPEN_DATE, OPEN_TIME),
                "close_time": (CLOSE_DATE, CLOSE_TIME),
            }.items():
                d = _date(cell(d_col) or "", d_col, line) if d_col in at else None
                t = _clock(cell(t_col) or "", t_col, line) if t_col in at else None
                fields[field] = _combine(d, t)
            if BEST_EXIT_TIME in at:
                fields["best_exit_time"] = _utc(cell(BEST_EXIT_TIME) or "", BEST_EXIT_TIME, line)
            playbook = cell(PLAYBOOK)
            fields["playbooks"] = split_playbooks(playbook) if playbook is not None else []
            try:
                out.append(StatsRow(**fields))  # type: ignore[arg-type]
            except ValidationError as e:  # pragma: no cover - every field is typed above
                first = e.errors()[0]
                raise StatsLogError(line, f"{'.'.join(str(p) for p in first['loc'])}: {first['msg']}") from None
        return out


__all__ = [
    "MATCH_INPUTS",
    "REQUIRED",
    "STOP_COLUMN",
    "StatsLogError",
    "StatsLogSource",
    "TradeStatsSource",
    "split_playbooks",
]
