"""Deterministic, re-runnable cut of the S2-P4 replay/picks fixtures
(plan STEP-1, L45 real-shape rule) from production reads saved under the
hub's scratch directory. Never reads the live DB/Finviz itself, never
invents a row.

Anchor day: real STEP-0 day (see the hub's report `## STEP-0 facts` for
the exact date), aset_sizings ids 302-312: CRWD/MU/INTC. Confirmed
against system.bars i1 that CRWD 302/303/304/305 and MU 308/309 crossed
their WATCH entry level without ever arming or triggering — genuine
"missed" cards (the case F13's miss line exists for) — while CRWD 306,
MU 307/310, INTC 311/312 armed, triggered, filled and closed. No
PASSED-state card exists anywhere in the aset_sizings read window since
the STEP-0 query's start date (card_transitions checked for all 29
rows) — recorded as a real gap, never invented. Shifted to synthetic
2026-02-10 (the leak scan in plan STEP-1 row 4 requires no literal real
anchor-month date string survive under tests/fixtures/ — this docstring
therefore never spells it out either).

Inputs, all raw production-read output, none queried by this script:
  scratch/step0-sizings.json           aset_sizings, `--format json`
                                        (desk-staged per the CTO desk's
                                        report §4 R4 — see the hub's
                                        report for the exact timestamp)
  scratch/card-transitions-day-raw.tsv card_transitions cards 302-312,
                                        `--format table`
  RAW_BARS_SOURCE (below)              system.bars i1, CRWD/MU/INTC,
                                        anchor day 13:00-20:10 UTC (the
                                        window from first card creation
                                        through the 20:05 ET
                                        market_reset expiry — premarket
                                        bars before the first card
                                        existed play no role, same
                                        real-shape-trim rationale as
                                        P2's _cut_p2_fixtures.py daily
                                        window), `--format table`,
                                        persisted verbatim by the
                                        harness because of its size;
                                        copied into scratch/ by this
                                        script as the L45 raw-output
                                        record before transforming
  RAW_MEMBERSHIP_SOURCE (below)        system.radar_membership, full
                                        anchor day, `--format table`,
                                        same persist-then-copy handling
  scratch/pool-metrics-raw.csv         one cached Finviz screen CSV,
                                        `cp` from data/radar-cache/
  scratch/movers-{gainers,losers}-raw.csv
                                        live Finviz /export/screener
                                        v=152 o=-change / o=change,
                                        unfiltered, no filter param, via
                                        _fetch_movers.py (deleted after
                                        its one run)

Outputs:
  tests/fixtures/replay/cards-day.real-shape.json
  tests/fixtures/replay/bars-day.real-shape.json
  tests/fixtures/replay/membership-day.real-shape.json
  tests/fixtures/replay/movers-gainers.real-shape.csv
  tests/fixtures/replay/movers-losers.real-shape.csv
  tests/fixtures/radar/pool-metrics.real-shape.csv
"""

from __future__ import annotations

import csv
import io
import json
import re
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent  # tests/fixtures/replay/
RADAR_DIR = HERE.parent / "radar"
SCRATCH = Path(__file__).resolve().parents[3] / "scratch"

REAL_ANCHOR = date(2026, 9, 14)
SYNTH_ANCHOR = date(2026, 2, 10)
DELTA_DAYS = (SYNTH_ANCHOR - REAL_ANCHOR).days

_DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
_HEX_SUFFIX_RE = re.compile(r"@[0-9a-f]{12}")

# Exact stdout of the two approved `cobalt db query --prod --format
# table` reads (plan STEP-1 rows 2 and 2m), persisted verbatim by the
# harness under its own tool-output store because of their size. Real
# production-read output, not invented; copied into scratch/ below.
RAW_BARS_SOURCE = Path(
    "/Users/cobalt/.claude/projects/-Users-cobalt-cobalt-wt-s2-p4/"
    "4f911896-df95-4888-9f12-6038117d288e/tool-results/b9h4bhyxf.txt"
)
RAW_MEMBERSHIP_SOURCE = Path(
    "/Users/cobalt/.claude/projects/-Users-cobalt-cobalt-wt-s2-p4/"
    "4f911896-df95-4888-9f12-6038117d288e/tool-results/boetnggei.txt"
)

_INT_FIELDS = {
    "id",
    "card_id",
    "volume",
    "rank_at_entry",
    "last_rank",
    "below_cap_streak",
    "opened_scan_id",
    "last_scan_id",
    "closed_scan_id",
}


def _shift_dates(text: str) -> str:
    def repl(m: re.Match) -> str:
        d = date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
        if d.year == REAL_ANCHOR.year and d.month == REAL_ANCHOR.month:
            return (d + timedelta(days=DELTA_DAYS)).isoformat()
        return m.group(0)

    return _DATE_RE.sub(repl, text)


def _anonymize(text: str) -> str:
    return _HEX_SUFFIX_RE.sub("@000000000000", _shift_dates(text))


def _cast_row(row: dict) -> dict:
    out = {}
    for k, v in row.items():
        if v == "":
            out[k] = None
        elif k in _INT_FIELDS:
            out[k] = int(v)
        else:
            out[k] = v
    return out


def _tsv_rows(text: str) -> list[dict]:
    return [_cast_row(r) for r in csv.DictReader(io.StringIO(text), delimiter="\t")]


def cut_cards_day() -> None:
    sizings_raw = json.loads((SCRATCH / "step0-sizings.json").read_text())
    day_cards = [r for r in sizings_raw if r["created_at"].startswith(str(REAL_ANCHOR))]
    assert day_cards, "no sizings for the anchor day"
    sizings = json.loads(_anonymize(json.dumps(day_cards)))

    trans_text = (SCRATCH / "card-transitions-day-raw.tsv").read_text()
    transitions = json.loads(_anonymize(json.dumps(_tsv_rows(trans_text))))

    dest = HERE / "cards-day.real-shape.json"
    dest.write_text(
        json.dumps({"sizings": sizings, "transitions": transitions}, indent=2, sort_keys=True) + "\n"
    )
    print(f"wrote {dest} ({len(sizings)} sizings, {len(transitions)} transitions)")


def cut_bars_day() -> None:
    raw_text = RAW_BARS_SOURCE.read_text()
    (SCRATCH / "bars-day-raw.tsv").write_text(raw_text)
    rows = _tsv_rows(raw_text)
    assert rows, "expected bars rows"
    anonymized = json.loads(_anonymize(json.dumps(rows)))
    dest = HERE / "bars-day.real-shape.json"
    dest.write_text(json.dumps(anonymized, indent=2, sort_keys=True) + "\n")
    print(f"wrote {dest} ({len(anonymized)} bars)")


def cut_membership_day() -> None:
    raw_text = RAW_MEMBERSHIP_SOURCE.read_text()
    (SCRATCH / "membership-day-raw.tsv").write_text(raw_text)
    rows = _tsv_rows(raw_text)
    assert rows, "expected membership rows"
    anonymized_rows = json.loads(_anonymize(json.dumps(rows)))

    # Synthesized PoolRow-shaped status block, matching the top-level
    # "pool" key of tests/fixtures/radar/panel-pool.real-shape.json
    # (P3). Not a derived production value — a plausible end-of-day
    # snapshot shape for STEP-2's PoolRow tests; the substantive data
    # for rank_metric/rank_value tests is the real "membership" list.
    pool_block = {
        "budget": {"planned_rpm": 36.6},
        "cap": 50,
        "degraded": False,
        "degraded_sources": [],
        "failed_detail": None,
        "failed_stage": None,
        "last_poll_at": None,
        "last_scan_at": f"{SYNTH_ANCHOR.isoformat()} 20:05:03.002850+00:00",
        "last_scan_id": 1000000000000,
        "last_scan_ms": 85,
        "members": 50,
        "poll_failures": [],
        "pool_key": "primary",
        "session": "close",
        "sources": [],
        "state": "scanning",
        "updated_at": f"{SYNTH_ANCHOR.isoformat()} 20:05:03.002850+00:00",
    }
    dest = HERE / "membership-day.real-shape.json"
    dest.write_text(
        json.dumps({"membership": anonymized_rows, "pool": pool_block}, indent=2, sort_keys=True) + "\n"
    )
    print(f"wrote {dest} ({len(anonymized_rows)} episodes)")


def cut_pool_metrics() -> None:
    raw_text = (SCRATCH / "pool-metrics-raw.csv").read_text()
    anonymized = _anonymize(raw_text)
    lines = anonymized.splitlines(keepends=True)
    trimmed = lines[:21]  # header + 20 rows
    dest = RADAR_DIR / "pool-metrics.real-shape.csv"
    dest.write_text("".join(trimmed))
    print(f"wrote {dest} ({len(trimmed) - 1} rows)")


def cut_movers() -> None:
    for side in ("gainers", "losers"):
        raw_text = (SCRATCH / f"movers-{side}-raw.csv").read_text()
        lines = raw_text.splitlines(keepends=True)
        trimmed = lines[:61]  # header + 60 rows
        dest = HERE / f"movers-{side}.real-shape.csv"
        dest.write_text("".join(trimmed))
        print(f"wrote {dest} ({len(trimmed) - 1} rows); header: {lines[0].strip()}")


def main() -> None:
    HERE.mkdir(parents=True, exist_ok=True)
    cut_cards_day()
    cut_bars_day()
    cut_membership_day()
    cut_pool_metrics()
    cut_movers()


if __name__ == "__main__":
    main()
