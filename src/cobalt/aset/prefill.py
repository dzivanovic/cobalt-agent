"""Last-price prefill from Finviz Elite.

Token resolution reuses the existing FinvizApiClient vault machinery
(KEEP-AS-IS seed); the fetch itself targets the documented current
endpoint /export/stock (see docs/90 - References/finvizstockapi.png) because
the old client's legacy quote_export.ashx now 301-redirects and the old
tree must stay untouched (strangler rule).

Fail-loud and secret-safe: missing or ambiguous data raises PrefillError
(the sheet shows FAILED, never a guessed price), and every error message
is scrubbed so the auth token can never leak into responses or logs.
Grade and stops are ALWAYS Dejan's input; this module never touches them.
"""

import csv
import io
import re
from decimal import Decimal, InvalidOperation

import httpx

from cobalt_agent.skills.research.finviz_api import FinvizApiClient

CLOSE_KEYS = ("Close", "close", "Last", "Price")
_AUTH_RE = re.compile(r"auth=[^&\s'\"]+")


class PrefillError(RuntimeError):
    """Prefill data unavailable — surface FAILED, do not guess."""


def scrub(text: str) -> str:
    """Redact any auth token that an underlying library baked into an error."""
    return _AUTH_RE.sub("auth=REDACTED", text)


async def resolve_token() -> str:
    client = FinvizApiClient()
    try:
        return await client._resolve_vault_credentials(client.FINVIZ_DOMAIN)
    except Exception as e:
        raise PrefillError(f"Finviz token resolution failed: {scrub(str(e))}") from e


async def fetch_last_price(ticker: str) -> tuple[Decimal, str]:
    """Return (last_price, source_description) for `ticker` or raise PrefillError."""
    ticker = ticker.strip().upper()
    if not ticker:
        raise PrefillError("Empty ticker.")

    token = await resolve_token()
    url = "https://elite.finviz.com/export/stock"
    params = {"t": ticker, "p": "d", "auth": token}
    try:
        async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
    except Exception as e:
        raise PrefillError(
            f"Finviz stock export fetch failed for {ticker}: {scrub(str(e))}"
        ) from e

    rows = list(csv.DictReader(io.StringIO(response.text)))
    if not rows:
        raise PrefillError(f"Finviz returned no rows for {ticker}.")

    last_row = rows[-1]
    for key in CLOSE_KEYS:
        value = last_row.get(key)
        if value in (None, ""):
            continue
        try:
            price = Decimal(str(value))
        except InvalidOperation as e:
            raise PrefillError(
                f"Unparseable price {value!r} in column {key!r} for {ticker}."
            ) from e
        if price <= 0:
            raise PrefillError(f"Non-positive price {price} for {ticker}.")
        return price, f"finviz /export/stock {key} ({len(rows)} rows)"

    raise PrefillError(
        f"No close-like column for {ticker}; got columns {list(last_row)[:10]}"
    )
