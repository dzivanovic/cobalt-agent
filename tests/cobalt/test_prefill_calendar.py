"""Calendar prefill tests: date-window filtering + fail-loud, no live
network."""

from datetime import date

import httpx
import pytest

from cobalt.prefill import calendar as calendar_module
from cobalt.prefill.calendar import (
    EarningsEvent,
    EconomicEvent,
    fetch_earnings_events,
    fetch_economic_events,
)
from cobalt.prefill.errors import PrefillFetchError


def _fake_client(text: str, status_code: int = 200):
    class _Response:
        def __init__(self):
            self.text = text
            self.status_code = status_code

        def raise_for_status(self):
            if self.status_code >= 400:
                request = httpx.Request("GET", "https://elite.finviz.com/export/calendar")
                raise httpx.HTTPStatusError(
                    "error", request=request, response=httpx.Response(status_code, request=request)
                )

    class _Client:
        def __init__(self, *a, **kw):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            return False

        async def get(self, url, params=None):
            return _Response()

    return _Client


@pytest.fixture(autouse=True)
def fake_token(monkeypatch):
    async def _token():
        return "faketoken"

    monkeypatch.setattr(calendar_module, "resolve_token", _token)


ECONOMIC_CSV = (
    "Event,Date,Time,Impact,For,Actual,Expected,Prior\n"
    '"Dallas Fed Manufacturing Index",2026-08-31,10:30,2,"Aug","","","1.3"\n'
    '"3-Month Bill Auction",2026-08-31,11:30,1,"","","","3.715%"\n'
    '"LMI Logistics Managers Index",2026-09-01,06:00,1,"Aug","","","68.9"\n'
)

EARNINGS_CSV = (
    "Date,Ticker,Company,Market Cap,EPS Estimate,EPS Actual,EPS Surprise,"
    "EPS GAAP Estimate,EPS GAAP Actual,EPS GAAP Surprise,Revenue Estimate,"
    "Revenue Actual,Revenue Surprise,1-Day Price Reaction\n"
    '2026-08-31 08:30,BLRX,"Bioline Rx Ltd ADR",12.19,0,,,0,,,0.5,,,7.31\n'
    '2026-09-01 08:30,LX,"LexinFintech Holdings Ltd ADR",144.5,,0.0446,,,0.0446,,,473.6,,-7.62\n'
)


async def test_fetch_economic_events_filters_to_date(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client(ECONOMIC_CSV))
    events = await fetch_economic_events(date(2026, 8, 31))
    assert events == [
        EconomicEvent(event="Dallas Fed Manufacturing Index", time="10:30", impact="2", expected="", prior="1.3"),
        EconomicEvent(event="3-Month Bill Auction", time="11:30", impact="1", expected="", prior="3.715%"),
    ]


async def test_fetch_earnings_events_filters_to_date_and_splits_time(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client(EARNINGS_CSV))
    events = await fetch_earnings_events(date(2026, 8, 31))
    assert events == [EarningsEvent(ticker="BLRX", company="Bioline Rx Ltd ADR", time="08:30")]


async def test_no_events_is_empty_not_an_error(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client(ECONOMIC_CSV))
    events = await fetch_economic_events(date(2026, 12, 25))
    assert events == []


async def test_fetch_calendar_http_error_raises(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client("", status_code=500))
    with pytest.raises(PrefillFetchError, match="calendar/economic fetch failed"):
        await fetch_economic_events(date(2026, 8, 31))
