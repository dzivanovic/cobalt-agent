"""Market snapshot prefill: SPY/QQQ/IWM last price + change%, via
Finviz Elite's `/export/screener` (v=111, the confirmed default view —
DATA-SOURCE-MEMO §1 Screener: `No., Ticker, Company, Sector, Industry,
Country, Market Cap, P/E, Price, Change, Volume`), with `t=` as the
confirmed direct multi-ticker override.

VIX and BTC are NOT servable by this endpoint — neither is a Finviz
stock/screener ticker. Callers (daily.py) render "n/a (manual)" for
those two, loudly, never a blank cell.

Fail-loud, secret-safe: reuses aset.prefill's token resolution + auth-
token scrubbing (one-path rule — no second Finviz-auth implementation).
"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

import csv
import io

import httpx

from cobalt.aset.prefill import resolve_token, scrub

from .errors import PrefillFetchError

MARKET_TICKERS: tuple[str, ...] = ("SPY", "QQQ", "IWM")

# Confirmed default screener view (DATA-SOURCE-MEMO 08-27 spike):
# No., Ticker, Company, Sector, Industry, Country, Market Cap, P/E,
# Price, Change, Volume.
_SCREENER_VIEW = "111"

UNSERVABLE = {
    "VIX": "n/a (manual) — VIX is not a Finviz stock/screener ticker",
    "BTC": "n/a (manual) — BTC is not a Finviz stock/screener ticker",
}


@dataclass(frozen=True)
class MarketRow:
    ticker: str
    price: Decimal
    change_pct: Decimal


def _parse_decimal(raw: str, ticker: str, column: str) -> Decimal:
    cleaned = raw.strip().rstrip("%")
    try:
        return Decimal(cleaned)
    except InvalidOperation as e:
        raise PrefillFetchError(
            f"Unparseable {column} {raw!r} for {ticker} in screener response."
        ) from e


async def fetch_market_table(
    tickers: tuple[str, ...] = MARKET_TICKERS,
) -> list[MarketRow]:
    """Fetch (price, change%) for every ticker in `tickers`. Raises
    PrefillFetchError with no partial/guessed rows — one bad ticker fails
    the whole call; the daily-note prefill decides how to surface it."""
    if not tickers:
        raise PrefillFetchError("No tickers requested.")

    token = await resolve_token()
    url = "https://elite.finviz.com/export/screener"
    params = {"v": _SCREENER_VIEW, "t": ",".join(tickers), "auth": token}
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
    except Exception as e:
        raise PrefillFetchError(f"Finviz screener fetch failed: {scrub(str(e))}") from e

    rows = list(csv.DictReader(io.StringIO(response.text)))
    if not rows:
        raise PrefillFetchError(f"Finviz screener returned no rows for {tickers}.")

    by_ticker = {(r.get("Ticker") or "").strip().upper(): r for r in rows}

    result: list[MarketRow] = []
    for ticker in tickers:
        row = by_ticker.get(ticker)
        if row is None:
            raise PrefillFetchError(f"Finviz screener response missing {ticker}.")
        price_raw = row.get("Price")
        change_raw = row.get("Change")
        if price_raw in (None, "") or change_raw in (None, ""):
            raise PrefillFetchError(
                f"Finviz screener row for {ticker} missing Price/Change: {row!r}"
            )
        result.append(
            MarketRow(
                ticker=ticker,
                price=_parse_decimal(price_raw, ticker, "Price"),
                change_pct=_parse_decimal(change_raw, ticker, "Change"),
            )
        )
    return result
