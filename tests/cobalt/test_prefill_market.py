"""Market table prefill tests: parsing + fail-loud, no live network."""

import httpx
import pytest

from cobalt.prefill import market as market_module
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow, fetch_market_table


class _FakeResponse:
    def __init__(self, text: str, status_code: int = 200):
        self.text = text
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            request = httpx.Request("GET", "https://elite.finviz.com/export/screener")
            raise httpx.HTTPStatusError(
                "error", request=request, response=httpx.Response(self.status_code, request=request)
            )


def _fake_client(text: str, status_code: int = 200):
    class _Client:
        def __init__(self, *a, **kw):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, *a):
            return False

        async def get(self, url, params=None):
            return _FakeResponse(text, status_code)

    return _Client


@pytest.fixture(autouse=True)
def fake_token(monkeypatch):
    async def _token():
        return "faketoken"

    monkeypatch.setattr(market_module, "resolve_token", _token)


SCREENER_CSV = (
    "No.,Ticker,Company,Sector,Industry,Country,Market Cap,P/E,Price,Change,Volume\n"
    '1,SPY,"SPDR S&P 500",,,,,,500.12,0.34%,1000\n'
    '2,QQQ,"Invesco QQQ",,,,,,450.55,-0.20%,2000\n'
    '3,IWM,"iShares Russell 2000",,,,,,210.03,1.05%,3000\n'
)


async def test_fetch_market_table_parses_price_and_change(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client(SCREENER_CSV))
    rows = await fetch_market_table()
    assert rows == [
        MarketRow(ticker="SPY", price=_d("500.12"), change_pct=_d("0.34")),
        MarketRow(ticker="QQQ", price=_d("450.55"), change_pct=_d("-0.20")),
        MarketRow(ticker="IWM", price=_d("210.03"), change_pct=_d("1.05")),
    ]


async def test_fetch_market_table_missing_ticker_raises(monkeypatch):
    csv_missing_iwm = (
        "No.,Ticker,Company,Sector,Industry,Country,Market Cap,P/E,Price,Change,Volume\n"
        '1,SPY,"SPDR S&P 500",,,,,,500.12,0.34%,1000\n'
        '2,QQQ,"Invesco QQQ",,,,,,450.55,-0.20%,2000\n'
    )
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client(csv_missing_iwm))
    with pytest.raises(PrefillFetchError, match="missing IWM"):
        await fetch_market_table()


async def test_fetch_market_table_empty_response_raises(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client(""))
    with pytest.raises(PrefillFetchError, match="no rows"):
        await fetch_market_table()


async def test_fetch_market_table_http_error_raises_scrubbed(monkeypatch):
    monkeypatch.setattr(httpx, "AsyncClient", _fake_client("", status_code=500))
    with pytest.raises(PrefillFetchError, match="fetch failed"):
        await fetch_market_table()


def _d(s: str):
    from decimal import Decimal

    return Decimal(s)
