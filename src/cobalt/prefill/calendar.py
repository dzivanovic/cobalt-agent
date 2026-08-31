"""Economic + earnings calendar prefill: today's rows from Finviz
Elite's `/export/calendar/{economic|earnings}?dateFrom=<date>`
(DATA-SOURCE-MEMO 08-27 spike: CONFIRMED, a narrow rolling window —
`dateFrom` filters WITHIN that window, not a historical archive). The
raw response spans several days beyond `dateFrom`, so this module
filters down to exactly the requested date before returning.

Columns confirmed by a live probe (2026-08-31), quoted here since the
memo only recorded column *counts*, not names:
  economic: Event, Date, Time, Impact, For, Actual, Expected, Prior
  earnings: Date, Ticker, Company, Market Cap, EPS Estimate, EPS Actual,
            EPS Surprise, EPS GAAP Estimate, EPS GAAP Actual,
            EPS GAAP Surprise, Revenue Estimate, Revenue Actual,
            Revenue Surprise, 1-Day Price Reaction

No events on a given date is a legitimate empty result (not a failure);
only a fetch/parse problem raises PrefillFetchError.
"""

import csv
import io
from dataclasses import dataclass
from datetime import date

import httpx

from cobalt.aset.prefill import resolve_token, scrub

from .errors import PrefillFetchError


@dataclass(frozen=True)
class EconomicEvent:
    event: str
    time: str
    impact: str
    expected: str
    prior: str


@dataclass(frozen=True)
class EarningsEvent:
    ticker: str
    company: str
    time: str


async def _fetch_calendar_csv(kind: str, for_date: date, token: str) -> list[dict]:
    url = f"https://elite.finviz.com/export/calendar/{kind}"
    params = {"dateFrom": for_date.isoformat(), "auth": token}
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
    except Exception as e:
        raise PrefillFetchError(
            f"Finviz calendar/{kind} fetch failed: {scrub(str(e))}"
        ) from e
    return list(csv.DictReader(io.StringIO(response.text)))


async def fetch_economic_events(for_date: date) -> list[EconomicEvent]:
    """Today's economic-calendar rows, sorted by time. Raises
    PrefillFetchError on a fetch/parse failure — never a partial guess."""
    token = await resolve_token()
    rows = await _fetch_calendar_csv("economic", for_date, token)
    target = for_date.isoformat()
    events = [
        EconomicEvent(
            event=(row.get("Event") or "").strip(),
            time=(row.get("Time") or "").strip(),
            impact=(row.get("Impact") or "").strip(),
            expected=(row.get("Expected") or "").strip(),
            prior=(row.get("Prior") or "").strip(),
        )
        for row in rows
        if (row.get("Date") or "").strip() == target
    ]
    events.sort(key=lambda e: e.time)
    return events


async def fetch_earnings_events(for_date: date) -> list[EarningsEvent]:
    """Today's earnings-calendar rows, sorted by time. Raises
    PrefillFetchError on a fetch/parse failure — never a partial guess."""
    token = await resolve_token()
    rows = await _fetch_calendar_csv("earnings", for_date, token)
    target = for_date.isoformat()
    events = []
    for row in rows:
        raw_date = (row.get("Date") or "").strip()
        if not raw_date.startswith(target):
            continue
        time_part = raw_date[len(target):].strip()
        events.append(
            EarningsEvent(
                ticker=(row.get("Ticker") or "").strip(),
                company=(row.get("Company") or "").strip(),
                time=time_part,
            )
        )
    events.sort(key=lambda e: e.time)
    return events
