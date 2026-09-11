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

TIMEZONE (ADR-0007, 2026-09-04). Finviz's export carries a bare ET
wall clock with no offset and no tz name — "09/03/2026 09:30 AM" is
09:30 *America/New_York*. Until ADR-0007 this parser returned that
naive value unchanged, psycopg handed it to a `timestamptz` column,
and Postgres (session `TimeZone = Etc/UTC`) stamped it `09:30+00`.
4.75M rows were therefore ET digits wearing a UTC label: every one of
them wrong by the ET offset, and every join against them wrong by the
same. The corpus was reinterpreted in place by ADR-0007; this parser
is the other half — it localizes to `America/New_York` (DST-aware, so
the offset is the one that applied on that date) and converts to UTC
before the value ever reaches a `Bar`. Bars are tz-aware UTC from
here on; sessions are reasoned about in ET by `cobalt.session`, never
by wall clock.
"""

import csv
import io
import re
import time
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from typing import Callable
from zoneinfo import ZoneInfo

import httpx
from pydantic import BaseModel, ConfigDict

from cobalt_agent.skills.research.finviz_api import FinvizApiClient

from .models import Bar, Interval

EXPECTED_COLUMNS = ["Date", "Open", "High", "Low", "Close", "Volume"]
_AUTH_RE = re.compile(r"auth=[^&\s'\"]+")

# Finviz's export timestamps are bare ET wall clock (ADR-0007).
FINVIZ_TZ = ZoneInfo("America/New_York")


class CollectorError(RuntimeError):
    """Fetch or shape-validation failure — never store, never guess."""


class FetchMetrics(BaseModel):
    """Observable facts for one Finviz request, with no URL or credential."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    status: int | None = None
    redirect_statuses: tuple[int, ...] = ()
    elapsed_ms: float
    bytes: int = 0
    content_type: str | None = None
    error: str | None = None


def scrub(text: str) -> str:
    return _AUTH_RE.sub("auth=REDACTED", text)


async def resolve_token() -> str:
    client = FinvizApiClient()
    try:
        return await client._resolve_vault_credentials(client.FINVIZ_DOMAIN)
    except Exception as e:
        raise CollectorError(f"Finviz token resolution failed: {scrub(str(e))}") from e


def _parse_finviz_datetime(raw: str) -> datetime:
    """Parse one Finviz date cell into a tz-aware UTC datetime.

    The string is a bare ET wall clock. It is localized to
    `America/New_York` and converted to UTC (ADR-0007) — the returned
    value is ALWAYS tz-aware, never naive.
    """
    return _parse_finviz_wall_clock(raw).replace(tzinfo=FINVIZ_TZ).astimezone(
        timezone.utc
    )


def _parse_finviz_wall_clock(raw: str) -> datetime:
    """The naive ET wall clock exactly as Finviz wrote it. Format handling
    only — the timezone is applied by `_parse_finviz_datetime`."""
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


async def finviz_get(
    path: str,
    params: dict[str, object],
    token: str,
    *,
    on_metrics: Callable[[FetchMetrics], None] | None = None,
) -> httpx.Response:
    """The sole Finviz HTTP transport used by new-core collectors.

    Metrics are emitted before HTTP status handling so callers can observe
    redirects and throttling without growing a second HTTP implementation.
    """
    clean_path = "/" + path.lstrip("/")
    url = f"https://elite.finviz.com{clean_path}"
    request_params = {**params, "auth": token}
    started = time.perf_counter()
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(url, params=request_params)
    except httpx.TransportError as e:
        metrics = FetchMetrics(
            elapsed_ms=(time.perf_counter() - started) * 1000,
            error=type(e).__name__,
        )
        if on_metrics is not None:
            on_metrics(metrics)
        raise CollectorError(f"Finviz transport failed: {scrub(str(e))}") from e

    metrics = FetchMetrics(
        status=response.status_code,
        redirect_statuses=tuple(item.status_code for item in response.history),
        elapsed_ms=(time.perf_counter() - started) * 1000,
        bytes=len(response.content),
        content_type=response.headers.get("content-type"),
    )
    if on_metrics is not None:
        on_metrics(metrics)
    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise CollectorError(f"Finviz HTTP failed: {scrub(str(e))}") from e
    return response


async def fetch_bars(
    ticker: str,
    interval: Interval,
    token: str,
    *,
    on_metrics: Callable[[FetchMetrics], None] | None = None,
) -> list[Bar]:
    """Fetch one (ticker, interval)'s bars over the network, then
    validate/parse via `parse_csv_response`."""
    ticker = ticker.strip().upper()
    params = {"t": ticker, "p": interval.value}
    try:
        response = await finviz_get(
            "/export/stock", params, token, on_metrics=on_metrics
        )
    except Exception as e:
        raise CollectorError(
            f"Fetch failed for {ticker}/{interval.value}: {scrub(str(e))}"
        ) from e

    return parse_csv_response(response.text, ticker, interval)


__all__ = [
    "CollectorError",
    "EXPECTED_COLUMNS",
    "FetchMetrics",
    "fetch_bars",
    "finviz_get",
    "parse_csv_response",
    "resolve_token",
    "scrub",
]
