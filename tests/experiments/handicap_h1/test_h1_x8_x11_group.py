"""Two group-verdict reads over every retained day, under a CONSTRUCTED
block — this build's literals from `h1_support.constructed_block`
(thresholds 20 / 300, combinator `any`), never his. At STEP-1 no verdict
function exists yet, so the `any` test is stated inline here, strict `<`
as v3 §3 says; `_number` is production's parser.

X8 (grok X9): equity rows of the low-float morning screen that fall
    OUTSIDE the group. Never a stop; any > 0 means the dry-run never prints
    "in the group by construction". The screen is picked by the substring
    `low_float` in its key — the key itself is never printed.
X11 (Fable X5): tickers whose verdict FLIPS between scans of one day.
    STOP only when a day's flips exceed a tenth of that day's in-group
    names (ASK DESK below that).
"""

from __future__ import annotations

from collections import defaultdict
from decimal import Decimal

from h1_support import CAP_HEADER, FLOAT_HEADER, config, constructed_block, exports, retained_days

from cobalt.radar.config import is_not_equity
from cobalt.radar.runner import _number

BLOCK = constructed_block()


def verdict(row) -> str:
    float_m, cap_m = _number(row.get(FLOAT_HEADER)), _number(row.get(CAP_HEADER))
    meets = [
        value is not None and Decimal(str(value)) < threshold
        for value, threshold in ((float_m, BLOCK["float_below_m"]), (cap_m, BLOCK["market_cap_below_m"]))
    ]
    if any(meets):
        return "yes"
    if float_m is None or cap_m is None:
        return "unknown"
    return "no"


def test_x8_low_float_screen_rows_outside_the_constructed_group():
    cfg = config()
    for day_dir in retained_days():
        counts = defaultdict(int)
        for _scan, source, _header, rows in exports(day_dir, cfg):
            if not (source.startswith("screen-") and "low_float" in source):
                continue
            for row in rows:
                if is_not_equity(row, cfg.not_equity):
                    continue
                counts["equity rows"] += 1
                counts[verdict(row)] += 1
        print(f"X8 day {day_dir.name}: low-float screen equity rows {counts['equity rows']} · in group "
              f"{counts['yes']} · OUTSIDE {counts['no']} · unknown {counts['unknown']}")


def test_x11_verdict_flips_between_scans_of_one_day():
    cfg = config()
    for day_dir in retained_days():
        by_ticker: dict[str, list[tuple]] = defaultdict(list)
        for scan, source, _header, rows in exports(day_dir, cfg):
            for row in rows:
                if is_not_equity(row, cfg.not_equity):
                    continue
                by_ticker[row["Ticker"].strip().upper()].append((scan.instant, source, verdict(row)))
        in_group = flips = 0
        for observations in by_ticker.values():
            per_scan = {}
            for instant, source, value in sorted(observations):
                per_scan.setdefault(instant, value)  # the first source in name order
            ordered = [per_scan[k] for k in sorted(per_scan)]
            in_group += "yes" in ordered
            flips += any(a != b for a, b in zip(ordered, ordered[1:]))
        limit = in_group / 10
        print(f"X11 day {day_dir.name}: tickers {len(by_ticker)} · in group at least once {in_group} · "
              f"verdict flipped within the day {flips} · a tenth of in-group {limit:.1f} · "
              f"over: {flips > limit}")
