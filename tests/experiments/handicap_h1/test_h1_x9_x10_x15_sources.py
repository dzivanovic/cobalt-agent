"""Three cache reads over every retained day (v3 first-gate experiments),
one test each, counts only:

X9  (grok X11): both handicap headers present in every LIST export and
    every SCREEN export? STOPS the build when lists lack them.
X10 (Fable X4): one ticker in two or more sources in ONE scan — are its
    float / cap cells (or their blankness) equal? Recorded, not a stop.
X15 (gemini X1 / grok / Fable (c)(1), measure only — it gates H2): screen
    exports where a not-equity row sits AHEAD of an equity row inside the
    export's own order (the fund hole of [R2F-02]; not fixed here).
"""

from __future__ import annotations

from collections import defaultdict

from h1_support import CAP_HEADER, FLOAT_HEADER, config, exports, retained_days

from cobalt.radar.config import is_not_equity


def test_x9_both_headers_in_list_and_screen_exports():
    cfg = config()
    seen = defaultdict(int)
    lacking = defaultdict(int)
    for day_dir in retained_days():
        for _scan, source, header, _rows in exports(day_dir, cfg):
            kind = source.split("-", 1)[0]
            seen[kind] += 1
            lacking[(kind, "float")] += FLOAT_HEADER not in header
            lacking[(kind, "cap")] += CAP_HEADER not in header
    for kind in sorted(seen):
        print(f"X9: {kind} exports {seen[kind]} · lacking the float header {lacking[(kind, 'float')]} · "
              f"lacking the cap header {lacking[(kind, 'cap')]}")


def test_x10_one_ticker_in_two_sources_in_one_scan():
    cfg = config()
    multi = float_equal = float_differ = cap_equal = cap_differ = 0
    for day_dir in retained_days():
        by_scan = defaultdict(lambda: defaultdict(list))
        for scan, source, _header, rows in exports(day_dir, cfg):
            for row in rows:
                by_scan[scan.instant][row["Ticker"].strip().upper()].append(
                    ((row.get(FLOAT_HEADER) or "").strip(), (row.get(CAP_HEADER) or "").strip())
                )
        for tickers in by_scan.values():
            for cells in tickers.values():
                if len(cells) < 2:
                    continue
                multi += 1
                floats = {c[0] for c in cells}
                caps = {c[1] for c in cells}
                float_equal += len(floats) == 1
                float_differ += len(floats) > 1
                cap_equal += len(caps) == 1
                cap_differ += len(caps) > 1
    print(f"X10: (scan, ticker) pairs carried by ≥2 sources {multi} · float cells equal {float_equal}, "
          f"differ {float_differ} · cap cells equal {cap_equal}, differ {cap_differ}")


def test_x15_not_equity_ahead_of_equity_inside_a_screen():
    cfg = config()
    for day_dir in retained_days():
        screens = with_hole = 0
        for _scan, source, _header, rows in exports(day_dir, cfg):
            if not source.startswith("screen-"):
                continue
            screens += 1
            flags = [is_not_equity(row, cfg.not_equity) for row in rows]
            first_fund = next((i for i, f in enumerate(flags) if f), None)
            with_hole += first_fund is not None and any(not f for f in flags[first_fund + 1:])
        print(f"X15 day {day_dir.name}: screen exports {screens} · with a not-equity row ahead of an "
              f"equity row {with_hole}")
