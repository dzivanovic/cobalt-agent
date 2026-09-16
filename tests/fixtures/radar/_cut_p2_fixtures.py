"""Deterministic, re-runnable cut of the S2-P2 evaluator fixtures (plan §3,
L45 real-shape rule) from production reads saved under the hub's scratch
directory. Never reads the live DB/Finviz itself, never invents a row.

Inputs (raw reads, paths given via env so raw prod data is never committed):
  P2_FIXTURE_RAW_BARS      `cobalt db query --format json` output of
                            system.bars i1 rows for the two fixture tickers
                            on the real anchor day
  P2_FIXTURE_RAW_DAILY_<T> one Finviz /export/stock?p=d CSV per ticker
                            (env var name suffixed with the ticker)
  P2_FIXTURE_RAW_SETTINGS  `cobalt db query --format json` output of the
                            trader_settings F13 keys

Outputs, written under this file's own directory:
  bars-rubberband.real-shape.json
  daily-bars.real-shape.csv
  card-settings.real-shape.json
"""

from __future__ import annotations

import csv
import io
import json
import os
import re
from datetime import date, datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent

# STEP-0 fact: two most-traded pool names of 2026-09-14 by last_rank
# (radar_membership; no Rubberband trade note exists to cut from — see
# report §1). Real anchor day never appears in output (leak scan checks
# for the literal "2026-09-1" pattern).
FIXTURE_TICKERS = ["FTFT", "BGFI"]
REAL_ANCHOR_DATE = date(2026, 9, 14)
SYNTHETIC_ANCHOR_DATE = date(2026, 1, 6)
DELTA_DAYS = (SYNTHETIC_ANCHOR_DATE - REAL_ANCHOR_DATE).days

_DATETIME_RE = re.compile(
    r"^(\d{4})-(\d{2})-(\d{2})([ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:\+00:00)?)$"
)


def _shift_datetime_str(value: str) -> str:
    m = _DATETIME_RE.match(value)
    if not m:
        return value
    year, month, day, rest = m.groups()
    d = date(int(year), int(month), int(day)) + timedelta(days=DELTA_DAYS)
    return f"{d.isoformat()}{rest}"


def cut_bars() -> None:
    raw_path = os.environ["P2_FIXTURE_RAW_BARS"]
    with open(raw_path) as f:
        rows = json.load(f)
    assert rows, "expected at least one bar row"
    assert {r["ticker"] for r in rows} <= set(FIXTURE_TICKERS)
    out = []
    for r in rows:
        row = dict(r)
        row["ts"] = _shift_datetime_str(row["ts"])
        out.append(row)
    out.sort(key=lambda r: (r["ticker"], r["ts"]))
    dest = HERE / "bars-rubberband.real-shape.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(out)} bars)")


# Trimmed to the trailing window a daily-level detector actually needs
# (prior-session H/L/C + ATR-14 warm-up); the source export is years of
# history and committing it whole would be real-shape but pointlessly
# large, not more faithful. Real rows, just fewer of them.
_DAILY_TRIM_ROWS = 40


def cut_daily() -> None:
    all_rows: list[dict] = []
    for ticker in FIXTURE_TICKERS:
        env_key = f"P2_FIXTURE_RAW_DAILY_{ticker}"
        raw_path = os.environ[env_key]
        with open(raw_path) as f:
            text = f.read()
        reader = list(csv.DictReader(io.StringIO(text)))
        assert reader, f"no daily rows for {ticker}"
        trimmed = reader[-_DAILY_TRIM_ROWS:]
        # Re-date the trimmed window so its last row lands on the
        # synthetic anchor day, offsets among rows kept (calendar-day
        # deltas from the real source, weekends/holidays included as
        # Finviz reported them).
        last_real_date = datetime.strptime(trimmed[-1]["Date"], "%m/%d/%Y").date()
        row_delta_days = (SYNTHETIC_ANCHOR_DATE - last_real_date).days
        for row in trimmed:
            d = datetime.strptime(row["Date"], "%m/%d/%Y").date() + timedelta(
                days=row_delta_days
            )
            all_rows.append({"Ticker": ticker, "Date": d.isoformat(), **{
                k: v for k, v in row.items() if k != "Date"
            }})
    dest = HERE / "daily-bars.real-shape.csv"
    with dest.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"])
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"wrote {dest} ({len(all_rows)} rows)")


def cut_settings() -> None:
    raw_path = os.environ["P2_FIXTURE_RAW_SETTINGS"]
    with open(raw_path) as f:
        rows = json.load(f)
    assert rows, "expected trader_settings rows"
    dest = HERE / "card-settings.real-shape.json"
    dest.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(rows)} keys)")


def main() -> None:
    cut_bars()
    cut_daily()
    cut_settings()


if __name__ == "__main__":
    main()
