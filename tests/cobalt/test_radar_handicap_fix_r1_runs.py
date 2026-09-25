"""H1 fix round 1 — the three RUNS for the UNPROVEN rows (L70; the
classification `reports/handicap-h1-fix-r1-draft-2026-09-24.md` rows 5,
6, 10). Each RUN PRINTS what it measures; a red RUN is a result, kept
under a strict xfail and never fixed here (L75).

Constructed values only — this file's literals, never his (L32).
"""

from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path

from radar_migrated_support import migrated_radar, requires_db  # noqa: F401  (fixture)

from cobalt.radar.config import load_config
from cobalt.radar.handicap import HandicapRecord
from cobalt.radar.models import SourceSet
from cobalt.radar.notes import load_sources
from cobalt.radar.pool import Action, Transition

FIXTURES = Path(__file__).resolve().parents[1] / "fixtures" / "radar"
RTH = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
BLOCK = (
    b"handicap:\n"
    b"  float_below_m: 13\n"
    b"  market_cap_below_m: 444\n"
    b"  factor: 0.65\n"
    b"  missing: skip\n"
    b"  mode: shadow\n"
    b"  combinator: all\n"
)
FLOAT_M = Decimal("12.5")
CAP_M = Decimal("321.25")


def _with_handicap(payload: bytes) -> bytes:
    """`BLOCK` as the last key of the note's one pool block (X4's shape)."""
    start = payload.index(b"kind: pool")
    end = payload.index(b"\n```", start)
    return payload[: end + 1] + BLOCK.rstrip(b"\n") + payload[end:]


def _load(screens: Path, finviz_max_rpm):
    return load_sources(
        screens, FIXTURES / "radar-lists.example.md",
        scan_interval=60, poll_interval=60, finviz_max_rpm=finviz_max_rpm,
        list_chunk_size=load_config().list_chunk_size, context_tickers=0,
    )


def test_run_1_x4_load_path_under_h1(tmp_path):
    """RUN-1 (`45` ESCALATE 2, `handicap-h1-check-2026-09-24.md:328`:
    X4's `pool_error` text not printed). A complete constructed block in the
    example note's pool block, through X4's own harness config
    (`finviz_max_rpm=None`), then with a constructed ceiling set."""
    screens = tmp_path / "screens.md"
    screens.write_bytes(_with_handicap((FIXTURES / "radar-screens.example.md").read_bytes()))
    unmeasured = _load(screens, None)
    print(f"RUN-1: pool_error = {unmeasured.pool_error}")
    assert unmeasured.pool_error is None or "handicap" not in unmeasured.pool_error
    measured = _load(screens, 90)
    print(f"RUN-1: pool_error (finviz_max_rpm=90) = {measured.pool_error}")
    print(f"RUN-1: pool.handicap present = {measured.pool is not None and measured.pool.handicap is not None}")
    assert measured.pool_error is None


def _pool_unit() -> dict:
    """`runner.py:327-331`'s expression, over a constructed `SourceSet`."""
    source_sets = [SourceSet(
        source="screen:run2@000000000000", kind="screen", tickers=["RUNB"],
        metrics={"RUNB": {"volume": 1.0, "rvol": 2.0, "float_m": FLOAT_M, "market_cap_m": CAP_M}},
    )]
    return {
        "pool_block": None,
        "frozen": False,
        "source_sets": [item.model_dump(mode="json") for item in source_sets],
    }


def test_run_2_a_the_pool_unit_round_trips_the_two_metrics():
    """RUN-2 (a) (`45` ESCALATE 2, `:328`: X5's stored half). OFFLINE: the
    dump serialized as `CardStore.write_receipt` does
    (`json.dumps(row["pool_unit"], default=str)`, `cards/store.py:1083`)
    and loaded back. `SourceSet.metrics` is typed float, so the Decimals
    are carried as floats; the comparison is as strings."""
    loaded = json.loads(json.dumps(_pool_unit(), default=str))
    metrics = loaded["source_sets"][0]["metrics"]["RUNB"]
    same = str(metrics["float_m"]) == str(FLOAT_M) and str(metrics["market_cap_m"]) == str(CAP_M)
    print(f"RUN-2 (a): source_sets[0].metrics keys {sorted(metrics)} · float_m {metrics['float_m']} "
          f"== {FLOAT_M}: {str(metrics['float_m']) == str(FLOAT_M)} · market_cap_m {metrics['market_cap_m']} "
          f"== {CAP_M}: {str(metrics['market_cap_m']) == str(CAP_M)}")
    assert {"float_m", "market_cap_m"} <= set(metrics) and same


@requires_db
def test_run_2_b_a_stored_receipt_carries_the_two_metrics(migrated_radar):
    """RUN-2 (b), WITH-DB inside `migrated_radar`: ONE receipt through
    `CardStore("cobalt_dev").write_receipt`, its foreign keys seeded by the
    stores' own public calls (`RadarStore.apply_membership` for the
    `radar_pool` row, `RadarStore.open_score_run` for the run), read back
    with one SELECT."""
    from cobalt.cards.store import CardStore
    from cobalt.radar.store import RadarStore

    key = "h1_fix_r1_run2"
    radar = RadarStore("cobalt_dev")
    radar.apply_membership(pool_key=key, scan_id=9930001, now=RTH, session="rth", transitions=[
        Transition(ticker="RUNB", action=Action.ADMIT, sources=["t"], source="t", rank=1, raw_rank=1),
    ])
    run_id = radar.open_score_run({
        "pool_key": key, "scan_id": 9930001, "previous_run_id": None, "session": "rth", "started_at": RTH,
        "cards_enabled": False, "evaluator_version": "run2", "formula_sha256": "f", "tunables_sha256": "t",
        "settings_sha256": "s", "cohort_sha256": "c",
    })
    cards = CardStore("cobalt_dev")
    receipt = cards.write_receipt({
        "run_id": run_id, "pool_key": key, "scan_id": 9930001, "evaluated_at": RTH,
        "ordered_cohort": [], "tie_policy": "rank_then_ticker", "pool_unit": _pool_unit(),
        "pool_unit_sha256": "h", "tunables_snapshot": [], "settings_snapshot": {},
        "definitions_snapshot": {}, "tap_versions": {}, "observations": [],
    })
    with cards._connect() as conn:
        (stored,) = conn.execute("SELECT pool_unit FROM radar_score_receipt WHERE id = %s", (receipt,)).fetchone()
    metrics = stored["source_sets"][0]["metrics"]["RUNB"]
    print(f"RUN-2 (b): stored source_sets[0].metrics keys {sorted(metrics)}")
    assert {"float_m", "market_cap_m"} <= set(metrics)


def _record(position: int, effective_position: int) -> HandicapRecord:
    return HandicapRecord(
        float_m=Decimal("7.5"), market_cap_m=Decimal("88"), verdict="yes", reason="float",
        missing_rule="skip", mode="shadow", position=position, effective_position=effective_position,
        source="screen:run3@000000000000", block_sha256="1" * 64,
    )


@requires_db
def test_run_3_a_a_ranked_leave_after_a_handicapped_retain(migrated_radar):
    """RUN-3 (a) (`45` ESCALATE 6, `:332`; check row `:260`). v3 is SILENT
    on a LEAVE row's three columns, so this measures and asserts NO policy:
    ADMIT → RETAIN at factor < 1 → a ranked cap LEAVE, through the store's
    public calls, then `members_for_day`."""
    from cobalt.radar.store import RadarStore

    store = RadarStore("cobalt_dev")
    key = "h1_fix_r1_run3"
    leave = Transition(ticker="RUNC", action=Action.LEAVE, sources=["t"], source="t", rank=6, raw_rank=6,
                       excluded_by="config_cap", handicap_factor=Decimal("0.65"), handicap=_record(6, 9))
    for scan_id, minutes, transition in (
        (9940001, 0, Transition(ticker="RUNC", action=Action.ADMIT, sources=["t"], source="t", rank=2,
                                raw_rank=2, handicap_factor=Decimal("0.65"), handicap=_record(2, 4))),
        (9940002, 1, Transition(ticker="RUNC", action=Action.RETAIN, sources=["t"], source="t", rank=3,
                                raw_rank=3, handicap_factor=Decimal("0.65"), handicap=_record(3, 5))),
        (9940003, 2, leave),
    ):
        store.apply_membership(pool_key=key, transitions=[transition], scan_id=scan_id,
                               now=RTH + timedelta(minutes=minutes), session="rth")
    rows = [row for row in store.members_for_day(key, RTH.date()) if row["left_at"] is not None]
    (row,) = rows
    effective = row["handicap"]["effective_position"] if row["handicap"] else None
    print(f"RUN-3 (a): departed row raw_rank {row['raw_rank']} · handicap_factor {row['handicap_factor']} · "
          f"effective_position {effective} · the LEAVE transition's raw_rank {leave.raw_rank}")
    assert row["ticker"] == "RUNC"


def test_run_3_b_the_departed_row_renders():
    """RUN-3 (b), OFFLINE: the departed row as (a)'s store leaves it (the
    RETAIN's record kept, factor < 1) rendered the way the panel renders
    departed rows — `_row(item, "departed", …)` → `_handicap_cell`. It
    asserts only that it renders."""
    from cobalt.aset import radar_panel as panel

    record = panel.MembershipRecord.model_validate({
        "id": 1, "pool_key": "h1_fix_r1_run3", "ticker": "RUNC", "trade_date": RTH.date(),
        "first_seen_at": RTH, "entered_at": RTH, "left_at": RTH + timedelta(minutes=2), "source": "t",
        "sources": ["t"], "rank_at_entry": 2, "last_rank": 3, "below_cap_streak": 0,
        "excluded_by": "config_cap", "session": "rth", "opened_scan_id": 9940001, "last_scan_id": 9940003,
        "closed_scan_id": 9940003, "rank_metric": None, "rank_value": None, "raw_rank": 3,
        "handicap_factor": Decimal("0.6500"), "handicap": _record(3, 5).model_dump(mode="json"),
    })
    cell = panel._handicap_cell(panel._row(record, "departed", None))
    print(f"RUN-3 (b): departed row renders the HANDICAP (shadow) badge: {'HANDICAP (shadow)' in cell}")
    print(f"RUN-3 (b): rendered cell: {cell}")
    assert isinstance(cell, str)
