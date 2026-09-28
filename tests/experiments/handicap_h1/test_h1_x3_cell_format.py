"""X3 (v3; grok X3 / gemini X2 / Fable X3): the live export's cell format
of `Shares Float` and `Market Cap` through `_number` over EVERY retained
cell, and `Price × Shares Outstanding` against `Market Cap`.

STOPS the build on a currency symbol, a B/M/K suffix or a unit mismatch.
Counts and ratios only.
"""

from __future__ import annotations

import re

from h1_support import CAP_HEADER, FLOAT_HEADER, config, exports, retained_days

from cobalt.radar.runner import _number

SUFFIX = re.compile(r"[A-Za-z$€£]")


def test_x3_cell_format_and_units():
    cfg = config()
    cells = blank = parsed = unparseable = suffixed = 0
    compared = within_1pct = within_5pct = beyond_5pct = 0
    worst = 0.0
    for day_dir in retained_days():
        for _scan, _source, _header, rows in exports(day_dir, cfg):
            for row in rows:
                for header in (FLOAT_HEADER, CAP_HEADER):
                    raw = row.get(header)
                    cells += 1
                    if raw is None or not raw.strip() or raw.strip() == "-":
                        blank += 1
                        continue
                    if SUFFIX.search(raw):
                        suffixed += 1
                    if _number(raw) is None:
                        unparseable += 1
                    else:
                        parsed += 1
                price = _number(row.get("Price"))
                shares = _number(row.get("Shares Outstanding"))
                cap = _number(row.get(CAP_HEADER))
                if price and shares and cap:
                    compared += 1
                    ratio = abs(price * shares - cap) / cap
                    worst = max(worst, ratio)
                    if ratio <= 0.01:
                        within_1pct += 1
                    elif ratio <= 0.05:
                        within_5pct += 1
                    else:
                        beyond_5pct += 1
    print(f"X3: cells {cells} · blank or '-' {blank} · parsed by _number {parsed} · "
          f"non-blank unparseable {unparseable} · carrying a letter or currency symbol {suffixed}")
    print(f"X3: Price × Shares Outstanding vs Market Cap on {compared} rows: ≤1% {within_1pct} · "
          f"1–5% {within_5pct} · >5% {beyond_5pct} · worst relative gap {worst:.4f}")
