"""Finviz `/export/stock` intraday-bar fetcher. Fail-loud, secret-safe.

Reuses the existing vault-backed `FinvizApiClient` for token resolution
only (same one-directional read-across-the-strangler-boundary pattern
as `aset/prefill.py`) — the old tree stays untouched.

Per DATA-SOURCE-MEMO.md's confirmed findings:
- `p=` is a validated enum here (Interval) — bare/unrecognized values
  silently return the full daily dataset with no error. Any response
  whose dates lack a time-of-day component is exactly that failure
  mode and is rejected loudly, never stored.
- Response columns are always exactly Date, Open, High, Low, Close,
  Volume — a mismatch is also rejected loudly.
- Finviz's own date strings are inconsistently formatted between
  intervals (`i1/i2/i5` give clean 12-hour "04:00 AM"; `i15/i30` have
  been observed giving a 24-hour hour with a bolted-on AM/PM suffix
  like "15:45 PM") — `_parse_finviz_datetime` handles both.
"""

import csv
import io
import re
from datetime import datetime
from decimal import Decimal, InvalidOperation

import httpx

from cobalt_agent.skills.research.finviz_api import FinvizApiClient

from .models import Bar, Interval

EXPECTED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]
_AUTH_RE = re.compile(r"auth=[^&\s'\"]+")


class CollectorError(RuntimeError):
    """Fetch or shape-validation failure — never store, never guess."""


def scrub(text: str) -> str:
    return _AUTH_RE.sub("auth=REDACTED", text)


async def resolve_token() -> str:
    client = FinvizApiClient()
    try:
        return await client._resolve_vault_credentials(client.FINVIZ_DOMAIN)
    except Exception as e:
        raise CollectorError(f"Finviz token resolution failed: {scrub(str(e))}") from e


def _parse_finviz_datetime(raw: str) -> datetime:
    raw = raw.strip()
    parts = raw.split(" ")
    if len(parts) < 2:
        # No time-of-day component at all -> this is the daily-fallback
        # shape (bare/unrecognized p= silently returns daily). We never
        # request daily, so this is always a failure, never a valid row.
        raise CollectorError(
            f"Date {raw!r} has no time-of-day component — Finviz likely "
            "fell back to daily (unrecognized interval), refusing to store."
        )
    date_part, time_part = parts[0], parts[1]

    # Clean 12-hour form: "04:00 AM" / "06:52 AM" (date_part time_part meridiem)
    try:
        return datetime.strptime(raw, "%m/%d/%Y %I:%M %p")
    except ValueError:
        pass

    # Observed quirk: a 24-hour hour with a bolted-on AM/PM suffix, e.g.
    # "08/26/2026 15:45 PM". Parse the 24-hour time, ignore the suffix.
    try:
        return datetime.strptime(f"{date_part} {time_part}", "%m/%d/%Y %H:%M")
    except ValueError:
        pass

    raise CollectorError(f"Unparseable Finviz datetime: {raw!r}")


def parse_csv_response(text: str, ticker: str, interval: Interval) -> list[Bar]:
    """Pure parsing/validation — no I/O. Raises CollectorError on any
    shape mismatch; never returns a partial or guessed result."""
    rows = list(csv.reader(io.StringIO(text)))
    if not rows:
        raise CollectorError(f"Empty response for {ticker}/{interval.value}.")

    header = rows[0]
    if header != EXPECTED_COLUMNS:
        raise CollectorError(
            f"Unexpected columns for {ticker}/{interval.value}: {header} "
            f"(expected {EXPECTED_COLUMNS})"
        )

    if len(rows) == 1:
        raise CollectorError(f"No data rows for {ticker}/{interval.value}.")

    bars: list[Bar] = []
    for row in rows[1:]:
        if len(row) != 6:
            raise CollectorError(
                f"Malformed row for {ticker}/{interval.value}: {row!r}"
            )
        date_s, open_s, high_s, low_s, close_s, vol_s = row
        try:
            ts = _parse_finviz_datetime(date_s)
            bars.append(
                Bar(
                    ticker=ticker,
                    interval=interval,
                    ts=ts,
                    open=Decimal(open_s),
                    high=Decimal(high_s),
                    low=Decimal(low_s),
                    close=Decimal(close_s),
                    volume=int(Decimal(vol_s)),
                )
            )
        except (InvalidOperation, ValueError) as e:
            raise CollectorError(
                f"Unparseable row for {ticker}/{interval.value}: {row!r} ({e})"
            ) from e

    return bars


async def fetch_bars(ticker: str, interval: Interval, token: str) -> list[Bar]:
    """Fetch one (ticker, interval)'s bars over the network, then
    validate/parse via `parse_csv_response`."""
    ticker = ticker.strip().upper()
    url = "https://elite.finviz.com/export/stock"
    params = {"t": ticker, "p": interval.value, "auth": token}
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
    except Exception as e:
        raise CollectorError(
            f"Fetch failed for {ticker}/{interval.value}: {scrub(str(e))}"
        ) from e

    return parse_csv_response(response.text, ticker, interval)
