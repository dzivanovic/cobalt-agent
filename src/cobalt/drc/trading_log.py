"""The trading-log parser (DRC D1-2) — his broker platform's daily
execution export, one row per fill.

READ BY HEADER NAME, REACHED ONLY THROUGH `detect`. A file arrives here
after `detect.detect_kind` classified it `trading_log`, complete or
`partial` (R114, R17 (5)). The name and extension of the file are never
read — his files end `.md` and change name every day.

THE SHAPE (E1, `reports/drc-d1-build-2026-09-23.md` `## E1`):
ten named columns and a trailing empty cell, newest row first, `Time` as
`HH:MM:SS` with NO date and NO zone, side codes `B` / `S` / `SS`.

THE DATE IS THE IMPORT DATE (R17 (3)). The file has no date column, so
every execution's date is the `import_date` the caller passes — the
`<date>` folder or the upload's date — combined with the row's `Time` as
America/New_York wall-clock time (E1 proved ET: 4 of 4 trades pair to the
second against the stats log's `EDT` open and close times). Nothing reads
a date from the file and nothing infers one.

FAIL-LOUD (L1). Every row validates on the columns the file HAS, or the
WHOLE file is `failed`, naming the line — a partial file is missing
COLUMNS, never skipped ROWS. An added column is not a failure: the file
parses and carries `degraded: trading_log_shape` naming it (L9).

ONE BUCKET (R94). The account column is read and stored per execution;
it never gates, splits or fails anything.
"""

from __future__ import annotations

import csv
import io
import re
from datetime import date, datetime, time
from decimal import Decimal, InvalidOperation
from typing import Protocol
from zoneinfo import ZoneInfo

from pydantic import ValidationError

from .models import (
    Detection,
    Execution,
    ImportResult,
    Kind,
    Outcome,
    ParsedTradingLog,
)

#: The zone E1 evidences for `Time` (see the module docstring).
ET = ZoneInfo("America/New_York")

TIME = "Time"
SYMBOL = "Symbol"
SIDE = "Side"
PRICE = "Price"
QTY = "Qty"
ROUTE = "Route"
BROKER = "Broker"
ACCOUNT = "Account"
TYPE = "Type"
ORDER_ID = "Cloid"

#: Every non-empty column name E1's trading-log header shows, in its
#: order. THE one copy: `detect` imports it, nothing retypes it (L3).
REQUIRED: tuple[str, ...] = (TIME, SYMBOL, SIDE, PRICE, QTY, ROUTE, BROKER, ACCOUNT, TYPE, ORDER_ID)

#: What FIFO pairing reads. A `partial` file missing any of these parses,
#: and pairing says `not computed — missing: <columns>` (R17 (5)).
PAIRING_INPUTS: tuple[str, ...] = (TIME, SYMBOL, SIDE, PRICE, QTY)

_FIELD = {
    TIME: "time",
    SYMBOL: "symbol",
    SIDE: "side",
    PRICE: "price",
    QTY: "qty",
    ROUTE: "route",
    BROKER: "broker",
    ACCOUNT: "account",
    TYPE: "order_type",
    ORDER_ID: "order_id",
}

_CLOCK = re.compile(r"^(\d{2}):(\d{2}):(\d{2})$")
_PRICE = re.compile(r"^\d+(\.\d+)?$")
_QTY = re.compile(r"^\d+$")


class TradingLogError(ValueError):
    """One row broke the file (L1). Carries the line it failed on."""

    def __init__(self, line: int, message: str):
        super().__init__(f"line {line}: {message}")
        self.line = line


class ExecutionSource(Protocol):
    """Where executions come from (L9). Swap the export → a new source,
    nothing upstream notices."""

    kind: Kind

    def parse(self, data: bytes, import_date: date, detection: Detection) -> ParsedTradingLog:
        ...


def _decode(data: bytes) -> str:
    return data.decode("utf-8-sig")


def _cell(value: str, column: str, line: int) -> object:
    """One cell of a present column → its typed value, or a loud error."""
    if value == "":
        raise TradingLogError(line, f"column {column!r} is empty")
    if column == TIME:
        m = _CLOCK.match(value)
        if not m:
            raise TradingLogError(line, f"column {column!r}: {value!r} is not HH:MM:SS")
        try:
            return time(int(m[1]), int(m[2]), int(m[3]))
        except ValueError:
            raise TradingLogError(line, f"column {column!r}: {value!r} is not a clock time") from None
    if column == PRICE:
        if not _PRICE.match(value):
            raise TradingLogError(line, f"column {column!r}: {value!r} is not a price")
        try:
            return Decimal(value)
        except InvalidOperation:  # pragma: no cover - the regex admits only decimals
            raise TradingLogError(line, f"column {column!r}: {value!r} is not a price") from None
    if column == QTY:
        if not _QTY.match(value):
            raise TradingLogError(line, f"column {column!r}: {value!r} is not a whole quantity")
        return int(value)
    return value


class TradingLogSource:
    """The one `ExecutionSource` today: the daily execution export."""

    kind = Kind.TRADING_LOG

    def parse(self, data: bytes, import_date: date, detection: Detection) -> ParsedTradingLog:
        """Parse `data` for `import_date`. Never raises for bad data: a
        bad file comes back `failed` with its reason and line, and no
        executions (zero rows stored — L1)."""
        if detection.kind is not Kind.TRADING_LOG or detection.outcome not in (
            Outcome.PARSED,
            Outcome.PARTIAL,
        ):
            raise ValueError(
                f"{detection.name}: the trading-log parser is reached only through "
                f"detect_kind → trading_log (got {detection.kind}, {detection.outcome.value})"
            )
        try:
            executions = self._rows(data, import_date)
        except TradingLogError as e:
            return ParsedTradingLog(
                import_date=import_date,
                result=ImportResult(
                    name=detection.name,
                    kind=Kind.TRADING_LOG,
                    outcome=Outcome.FAILED,
                    reason=f"{detection.name}: {e}",
                    line=e.line,
                    missing=list(detection.missing),
                    extras=list(detection.extras),
                ),
            )
        absent = [c for c in PAIRING_INPUTS if c in detection.missing]
        not_computed = {"pairing": f"not computed — missing: {', '.join(absent)}"} if absent else {}
        return ParsedTradingLog(
            import_date=import_date,
            executions=executions,
            result=ImportResult(
                name=detection.name,
                kind=Kind.TRADING_LOG,
                outcome=detection.outcome,
                reason=detection.partial_flag or "",
                missing=list(detection.missing),
                extras=list(detection.extras),
                not_computed=not_computed,
            ),
        )

    def _rows(self, data: bytes, import_date: date) -> list[Execution]:
        try:
            text = _decode(data)
        except UnicodeDecodeError as e:
            raise TradingLogError(e.object.count(b"\n", 0, e.start) + 1, f"not UTF-8 text ({e.reason})") from None
        records = list(csv.reader(io.StringIO(text, newline="")))
        header = records[0]
        present = {name: i for i, name in enumerate(header) if name in _FIELD}
        unnamed = [i for i, name in enumerate(header) if name == ""]
        # Trailing blank lines are not rows; a blank line INSIDE the file is.
        while len(records) > 1 and records[-1] == []:
            records.pop()
        out: list[Execution] = []
        for offset, record in enumerate(records[1:]):
            line = offset + 2
            if len(record) != len(header):
                raise TradingLogError(
                    line, f"{len(record)} cells where the header has {len(header)}"
                )
            for i in unnamed:
                if record[i] != "":
                    raise TradingLogError(line, f"a value {record[i]!r} under an unnamed column")
            fields: dict[str, object] = {"line": line}
            for column, i in present.items():
                fields[_FIELD[column]] = _cell(record[i], column, line)
            clock = fields.get("time")
            if clock is not None:
                fields["time"] = datetime.combine(import_date, clock, tzinfo=ET)  # type: ignore[arg-type]
            try:
                out.append(Execution(**fields))  # type: ignore[arg-type]
            except ValidationError as e:
                first = e.errors()[0]
                raise TradingLogError(
                    line, f"{'.'.join(str(p) for p in first['loc'])}: {first['msg']}"
                ) from None
        return out


def chronological(executions: list[Execution]) -> list[Execution]:
    """Oldest first. The export is newest-first, so rows sharing one
    `Time` are taken in REVERSE file order (a later line = an earlier
    fill). E1's evidence: the one scale-in whose first `Time` carries two
    fills at two prices has the stats log's `Entry Price` equal to the
    lower line's price (`## E1` of the build report)."""
    return sorted(executions, key=lambda e: (e.time, -e.line))  # type: ignore[arg-type, operator]


__all__ = [
    "ET",
    "PAIRING_INPUTS",
    "REQUIRED",
    "ExecutionSource",
    "TradingLogError",
    "TradingLogSource",
    "chronological",
]
