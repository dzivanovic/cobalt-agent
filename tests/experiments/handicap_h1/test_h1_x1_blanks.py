"""X1 (v3; grok X1 / Fable X1): blank `Shares Float` / `Market Cap` on
EQUITY rows, per source, per retained day — plus the committed fixtures —
and (measure only, R54) the scans in which a source's handicap column is
DEAD: its header absent, or every equity row of that source blank, `-` or
unparseable by `_number` (STEP-4A's definition).

Counts and ratios only. STOPS the build (v3 / `29` §4) when a source is
MOSTLY blank: any (day, source) whose blank ratio on equity rows exceeds
one half is printed as `MOSTLY BLANK`.
"""

from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from h1_support import CAP_HEADER, FLOAT_HEADER, config, exports, retained_days, source_key

from cobalt.radar.config import is_not_equity
from cobalt.radar.runner import _number

FIXTURES = Path(__file__).resolve().parents[2] / "fixtures"


def _fixture_counts(path: Path, cfg):
    import csv
    import io

    rows = list(csv.DictReader(io.StringIO(path.read_text(encoding="utf-8-sig"))))
    equity = [r for r in rows if not is_not_equity(r, cfg.not_equity)]
    return (
        len(equity),
        sum(_number(r.get(FLOAT_HEADER)) is None for r in equity),
        sum(_number(r.get(CAP_HEADER)) is None for r in equity),
    )


def test_x1_blank_float_and_cap_per_source_per_day_and_dead_columns():
    cfg = config()
    for name in ("radar/pool-metrics.real-shape.csv", "replay/movers-gainers.real-shape.csv",
                 "replay/movers-losers.real-shape.csv"):
        n, bf, bc = _fixture_counts(FIXTURES / name, cfg)
        print(f"X1 fixture {name}: equity rows {n} · blank float {bf} · blank cap {bc}")
    mostly = 0
    total_scans = 0
    for day_dir in retained_days():
        rows_by = defaultdict(lambda: [0, 0, 0])            # source -> [equity rows, blank float, blank cap]
        pairs = defaultdict(lambda: [set(), set(), set()])  # source -> [pairs, blank-float pairs, blank-cap pairs]
        dead = defaultdict(lambda: [0, 0, 0])               # source -> [scans, float dead, cap dead]
        scans = set()
        for scan, source, header, rows in exports(day_dir, cfg):
            scans.add(scan.instant)
            key = source_key(source)
            equity = [r for r in rows if not is_not_equity(r, cfg.not_equity)]
            counts = rows_by[key]
            counts[0] += len(equity)
            for row in equity:
                ticker = row["Ticker"].strip().upper()
                pairs[key][0].add(ticker)
                if _number(row.get(FLOAT_HEADER)) is None:
                    counts[1] += 1
                    pairs[key][1].add(ticker)
                if _number(row.get(CAP_HEADER)) is None:
                    counts[2] += 1
                    pairs[key][2].add(ticker)
            # A list's chunks are one source: its column is LIVE in a scan
            # when ANY chunk carries one parseable equity cell.
            d = dead[(key, scan.instant)]
            d[0] |= int(bool(equity))
            d[1] |= int(FLOAT_HEADER in header and any(_number(r.get(FLOAT_HEADER)) is not None for r in equity))
            d[2] |= int(CAP_HEADER in header and any(_number(r.get(CAP_HEADER)) is not None for r in equity))
        total_scans += len(scans)
        print(f"X1 day {day_dir.name}: scans {len(scans)}")
        # [scans with ≥1 equity row, float dead, cap dead, scans with NO equity row]
        dead_by_source = defaultdict(lambda: [0, 0, 0, 0])
        dead_scans_any = set()       # scans where ANY source with equity rows has a dead column
        dead_scans_vacuous = set()   # the same, if a source with ZERO equity rows counted as dead
        for (key, instant), (has_equity, float_live, cap_live) in dead.items():
            agg = dead_by_source[key]
            if not has_equity:
                agg[3] += 1
                dead_scans_vacuous.add(instant)
                continue
            agg[0] += 1
            agg[1] += 0 if float_live else 1
            agg[2] += 0 if cap_live else 1
            if not (float_live and cap_live):
                dead_scans_any.add(instant)
                dead_scans_vacuous.add(instant)
        print(f"X1 day {day_dir.name}: scans with a DEAD column (R54: handicap inoperative for the scan) "
              f"{len(dead_scans_any)} of {len(scans)} · if a source with no equity row counted as dead: "
              f"{len(dead_scans_vacuous)} of {len(scans)}")
        for index, key in enumerate(sorted(rows_by)):
            n, bf, bc = rows_by[key]
            ratio_f = bf / n if n else 0.0
            ratio_c = bc / n if n else 0.0
            flag = " MOSTLY BLANK" if n and (ratio_f > 0.5 or ratio_c > 0.5) else ""
            mostly += bool(flag)
            p, pf, pc = (len(x) for x in pairs[key])
            s, df, dc, empty = dead_by_source[key]
            kind = key.split("-", 1)[0]
            print(
                f"X1 day {day_dir.name} {kind} source #{index + 1}: equity rows {n} · blank float {bf} "
                f"({ratio_f:.3%}) · blank cap {bc} ({ratio_c:.3%}) · pairs {p}, blank-float pairs {pf}, "
                f"blank-cap pairs {pc} · scans with equity rows {s}: float column DEAD in {df}, cap column "
                f"DEAD in {dc} · scans with NO equity row {empty}{flag}"
            )
    print(f"X1: retained days {len(retained_days())} · scans {total_scans} · (day, source) MOSTLY BLANK: {mostly}")
