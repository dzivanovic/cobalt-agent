"""Deterministic, re-runnable cut of the setups fixture-cut fixtures (prompt
`12-setups-fixture-cut.md`, L45 real-shape rule) from production reads saved
under the hub's scratch directory. Never reads the live DB itself, never
invents, edits, re-orders or re-prices a bar; the cutter only re-dates.

Usage:
  uv run python tests/fixtures/radar/_cut_setups_fixtures.py \
      <slug> <real day YYYY-MM-DD> <synthetic day YYYY-MM-DD> \
      <raw bars json path> <raw membership json path> <daily csv path>
  uv run python tests/fixtures/radar/_cut_setups_fixtures.py --remove <slug>

Outputs, written next to this file:
  bars-setups-<slug>.real-shape.json
  daily-bars-setups-<slug>.real-shape.csv
  membership-setups-<slug>.real-shape.json

The real day is NEVER a literal in this file or in any output — it comes in
by argv only, and is used solely to compute the re-dating delta.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

HERE = Path(__file__).parent

_DATETIME_RE = re.compile(
    r"^(\d{4})-(\d{2})-(\d{2})([ T]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:\+00:00)?)?$"
)

#: Precedent's trim window (`_cut_p2_fixtures.py`): the trailing daily rows a
#: daily-level detector actually needs (prior-session H/L/C + ATR warm-up).
_DAILY_TRIM_ROWS = 40

#: Membership columns the real loaders' shapes (`admitted_at`, `MemberInput`)
#: actually read for this cut: id, ticker, trade_date, entered_at, left_at.
#: `session`, `rank_at_entry`, `last_rank` are dropped — not read by that path.
_MEMBERSHIP_KEEP = ("ticker", "trade_date", "entered_at", "left_at")


def _shift_datetime_str(value: str, delta_days: int) -> str:
    m = _DATETIME_RE.match(value)
    if not m:
        return value
    year, month, day, rest = m.groups()
    d = date(int(year), int(month), int(day)) + timedelta(days=delta_days)
    return f"{d.isoformat()}{rest or ''}"


def _shift_value(value, delta_days: int):
    if isinstance(value, str):
        return _shift_datetime_str(value, delta_days)
    return value


#: The harness's own `run_in_background` output-file wrapper appends this
#: trailing marker after a command's real stdout — never part of the tool's
#: own output. Stripped ONLY as this exact trailing shape; anything else that
#: fails to parse is a fail-loud SystemExit (L1), never hand-repaired.
_BG_TRAILER_RE = re.compile(r"\n*\[exited with code -?\d+\]\n*$")


def _load_json(path: str, what: str) -> list[dict]:
    with open(path) as f:
        text = f.read()
    text = _BG_TRAILER_RE.sub("", text)
    try:
        rows = json.loads(text)
    except json.JSONDecodeError as e:
        raise SystemExit(f"{what} at {path} did not parse as JSON: {e}")
    if not rows:
        raise SystemExit(f"{what} at {path} is empty")
    return rows


def cut_membership(slug: str, delta_days: int, raw_membership_path: str) -> list[dict]:
    rows = _load_json(raw_membership_path, "raw membership")
    out = []
    for i, r in enumerate(rows, start=1):
        row = {"id": i}
        for k in _MEMBERSHIP_KEEP:
            row[k] = _shift_value(r[k], delta_days)
        out.append(row)
    dest = HERE / f"membership-setups-{slug}.real-shape.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(out)} rows)")
    return out


def cut_bars(slug: str, delta_days: int, raw_bars_path: str, membership_tickers: set[str]) -> int:
    rows = _load_json(raw_bars_path, "raw bars")
    assert {r["ticker"] for r in rows} <= membership_tickers, "a bar ticker is not in the membership rows"
    out = []
    for r in rows:
        row = {k: _shift_value(v, delta_days) for k, v in r.items()}
        out.append(row)
    out.sort(key=lambda r: (r["ticker"], r["ts"]))
    dest = HERE / f"bars-setups-{slug}.real-shape.json"
    dest.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(out)} bars)")
    return len(out)


def cut_daily(slug: str, ticker: str, synthetic_day: date, daily_csv_path: str) -> int:
    """Re-dates onto the SAME trading calendar the engine checks staleness
    against (`daily_staleness` / `previous_trading_day`): the last real row
    lands on the synthetic trade day itself (the precedent's rule), and each
    earlier row walks back one TRADING day at a time on that calendar. A
    uniform calendar-day delta (the precedent's shape, `_shift_datetime_str`)
    only reproduces the right adjacency when the real and synthetic anchor
    days share a weekday; this holds for any pairing because it walks the
    actual trading calendar instead of assuming one. Real rows, same order,
    just re-dated — no bar invented, edited, re-ordered or re-priced."""
    from cobalt.radar.anatomy.freshness import previous_trading_day
    from cobalt.session import session_clock

    path = Path(daily_csv_path)
    if not path.exists():
        raise SystemExit(f"no daily cache file at {path}")
    text = path.read_text(encoding="utf-8-sig")
    reader = list(csv.DictReader(io.StringIO(text)))
    if not reader:
        raise SystemExit(f"no daily rows for {ticker} at {path}")
    trimmed = reader[-_DAILY_TRIM_ROWS:]
    is_trading_day = session_clock().calendar.is_trading_day
    dates = [synthetic_day]
    while len(dates) < len(trimmed):
        dates.append(previous_trading_day(dates[-1], is_trading_day))
    dates.reverse()
    all_rows = []
    for row, d in zip(trimmed, dates):
        all_rows.append({"Ticker": ticker, "Date": d.isoformat(), **{
            k: v for k, v in row.items() if k != "Date"
        }})
    dest = HERE / f"daily-bars-setups-{slug}.real-shape.csv"
    with dest.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Ticker", "Date", "Open", "High", "Low", "Close", "Volume"])
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"wrote {dest} ({len(all_rows)} rows)")
    return len(all_rows)


def remove(slug: str) -> None:
    for name in (
        f"bars-setups-{slug}.real-shape.json",
        f"daily-bars-setups-{slug}.real-shape.csv",
        f"membership-setups-{slug}.real-shape.json",
    ):
        p = HERE / name
        if p.exists():
            p.unlink()
            print(f"removed {p}")
        else:
            print(f"absent (nothing to remove): {p}")


def main(argv: list[str]) -> None:
    if argv[:1] == ["--remove"]:
        remove(argv[1])
        return
    slug, real_day_s, synthetic_day_s, raw_bars_path, raw_membership_path, daily_csv_path = argv
    real_day = date.fromisoformat(real_day_s)
    synthetic_day = date.fromisoformat(synthetic_day_s)
    delta_days = (synthetic_day - real_day).days

    membership_rows = cut_membership(slug, delta_days, raw_membership_path)
    tickers = {r["ticker"] for r in membership_rows}
    n_bars = cut_bars(slug, delta_days, raw_bars_path, tickers)
    assert n_bars > 0, "expected at least one bar"
    for ticker in sorted(tickers):
        cut_daily(slug, ticker, synthetic_day, daily_csv_path)


if __name__ == "__main__":
    main(sys.argv[1:])
