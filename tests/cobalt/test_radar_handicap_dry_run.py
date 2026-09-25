"""Float handicap H1 STEP-6 — the `h = 1` identity and the dry-run (v3
§7 (1), [F-16], X12).

Identity on the COMMITTED real-shape scan (L45): `decide()` with the block
ABSENT and with a block whose factor is 1 (this file's literal) — every
pre-H1 `Transition` field byte-identical, the order identical, `raw_rank
== rank` on every ranked row. The dry-run runs on a constructed cache day
built from the committed exports (pytest's `tmp_path`); the retained-day
identity is `tests/experiments/handicap_h1/test_x12_identity.py`.
"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

import pytest
from radar_migrated_support import migrated_radar, requires_db  # noqa: F401  (fixture)
from test_radar_handicap import FIXTURES, block, pool
from test_radar_handicap_dead import _scan
from test_radar_handicap_group import RTH_NOW
from test_radar_handicap_shadow import HEADERS

from cobalt.radar import handicap_dry_run as dry
from cobalt.radar.config import load_config
from cobalt.radar.models import HandicapBlock, PoolBlock
from cobalt.radar.notes import load_sources
from cobalt.radar.pool import Action, Transition, decide
from cobalt.radar.store import RadarStore

# ---------------------------------------------------------------------
# (i) IDENTITY on the committed real-shape scan
# ---------------------------------------------------------------------


@pytest.mark.parametrize("missing", ["apply", "skip"])
@pytest.mark.parametrize("combinator", ["any", "all"])
def test_block_absent_and_factor_one_are_byte_identical_on_the_committed_scan(missing, combinator):
    sources, candidates, _ = _scan()
    unit = PoolBlock(**{**pool(**block(factor="1", missing=missing, combinator=combinator)), "cap": 7})
    absent = unit.model_copy(update={"handicap": None})
    a = decide(list(candidates.values()), [], absent, sources, RTH_NOW, handicap_headers=HEADERS)
    b = decide(list(candidates.values()), [], unit, sources, RTH_NOW, handicap_headers=HEADERS)
    assert [dry.core(t) for t in a.transitions] == [dry.core(t) for t in b.transitions]
    assert a.degraded_sources == b.degraded_sources
    ranked = [t for t in b.transitions if t.rank is not None and t.action is not Action.HOLD]
    assert ranked and all(t.raw_rank == t.rank for t in ranked)
    assert all(t.handicap.effective_position == t.handicap.position for t in ranked)
    assert all(t.handicap_factor == Decimal(1) for t in ranked)


def test_core_fields_are_exactly_the_pre_h1_transition():
    assert set(dry.CORE_FIELDS) | {"raw_rank", "handicap_factor", "handicap"} == set(Transition.model_fields)


# ---------------------------------------------------------------------
# (ii) the dry-run function over a constructed cache day
# ---------------------------------------------------------------------


def _day(tmp_path: Path):
    """A two-scan cache day of the example note's one screen, built from
    the committed exports under `collector.py`'s naming."""
    day = tmp_path / "radar-cache" / "2026-09-03"
    day.mkdir(parents=True)
    shutil.copy(FIXTURES / "pool-metrics.real-shape.csv", day / "screen-example_session_scan-143000.csv")
    shutil.copy(FIXTURES / "screen-handicap.real-shape.csv", day / "screen-example_session_scan-143300.csv")
    parsed = load_sources(
        FIXTURES / "radar-screens.example.md", FIXTURES / "radar-lists.example.md",
        scan_interval=60, poll_interval=60, finviz_max_rpm=None, list_chunk_size=1, context_tickers=0,
    )
    return day, parsed


def test_the_dry_run_replays_every_scan_and_prints_the_f16_lines(tmp_path):
    day, parsed = _day(tmp_path)
    report = dry.dry_run(day, parsed, load_config(), HandicapBlock(**block(factor="0.5")))
    assert report.scans == 2 and len(report.lines) == 2 and report.configured
    text = dry.render(report)
    assert text[0] == "handicap-dry-run 2026-09-03 · n: 1 day, 2 scans (L8: descriptive)"
    assert text[2].startswith("headers read: Shares Float / Market Cap · five raw cells: ")
    assert len(report.raw_cells) == 5
    assert any(line.lost or line.kept or line.took for line in report.lines)
    assert text[-1].startswith("cut tiers, the day: ")
    assert not any("keeps its seat iff" in line for line in text)       # X2: never printed


def test_the_dry_run_without_a_block_is_the_h1_pass_only(tmp_path):
    day, parsed = _day(tmp_path)
    report = dry.dry_run(day, parsed, load_config(), None)
    assert not report.configured
    assert dry.render(report)[1] == "handicap: not configured — h = 1 pass only"
    assert all(not (line.kept or line.lost or line.took) for line in report.lines)


def test_the_identity_holds_over_the_constructed_day(tmp_path):
    day, parsed = _day(tmp_path)
    assert dry.identity_mismatches(day, parsed, load_config(), HandicapBlock(**block())) == (2, [])


def test_the_dry_run_names_an_inoperative_scan(tmp_path):
    day, parsed = _day(tmp_path)
    target = day / "screen-example_session_scan-143300.csv"
    lines = target.read_text().splitlines(keepends=True)
    index = lines[0].split(",").index('"Shares Float"')
    blanked = [lines[0]] + [
        ",".join("" if i == index else v for i, v in enumerate(line.split(","))) for line in lines[1:]
    ]
    target.write_text("".join(blanked))
    report = dry.dry_run(day, parsed, load_config(), HandicapBlock(**block()))
    assert "scans with the handicap INOPERATIVE (R54): 1 of 2" in dry.render(report)


# ---------------------------------------------------------------------
# (iii) the CLI's argparse entry — called here, never typed
# ---------------------------------------------------------------------


def _parser():
    from cobalt.radar.cli import add_parser

    parser = argparse.ArgumentParser()
    add_parser(parser.add_subparsers(dest="group"))
    return parser


def test_the_subcommand_takes_day_and_nothing_else():
    args = _parser().parse_args(["radar", "handicap-dry-run", "--day", "2026-09-03"])
    assert args.day == "2026-09-03" and args.func is dry.command
    with pytest.raises(SystemExit):
        _parser().parse_args(["radar", "handicap-dry-run", "--day", "2026-09-03", "--factor", "0.5"])


def test_a_day_not_in_the_cache_is_refused_loudly(tmp_path, monkeypatch):
    config = load_config()
    monkeypatch.chdir(tmp_path)          # `cache.dir` is cwd-relative, as in production
    args = _parser().parse_args(["radar", "handicap-dry-run", "--day", "2026-09-03"])
    with pytest.raises(dry.DryRunError, match=f"2026-09-03 is not in the cache {config.cache.dir}"):
        args.func(args)


def test_a_malformed_day_is_refused_loudly(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    args = _parser().parse_args(["radar", "handicap-dry-run", "--day", "yesterday"])
    with pytest.raises(dry.DryRunError, match="YYYY-MM-DD"):
        args.func(args)


# ---------------------------------------------------------------------
# (iv) the stored-membership comparison — with-DB, rows THIS test inserts
# ---------------------------------------------------------------------


@requires_db
def test_the_h1_pass_is_compared_with_stored_membership_read_only(migrated_radar):
    store = RadarStore("cobalt_dev")
    key = "h1_dry_run_test"
    # 10:00 and 10:03 ET on the suite's RTH day (the calendar knows 2026).
    first = datetime(2026, 9, 3, 14, 0, 0, 250000, tzinfo=timezone.utc)
    second = datetime(2026, 9, 3, 14, 3, 0, 750000, tzinfo=timezone.utc)
    ids = [int(first.timestamp() * 1000), int(second.timestamp() * 1000)]
    store.apply_membership(pool_key=key, scan_id=ids[0], now=first, session="rth", transitions=[
        Transition(ticker="AAA", action=Action.ADMIT, sources=["t"], source="t", rank=1, raw_rank=1),
        Transition(ticker="BBB", action=Action.ADMIT, sources=["t"], source="t", rank=2, raw_rank=2),
    ])
    store.apply_membership(pool_key=key, scan_id=ids[1], now=second, session="rth", transitions=[
        Transition(ticker="AAA", action=Action.RETAIN, sources=["t"], source="t", rank=1, raw_rank=1),
        Transition(ticker="BBB", action=Action.LEAVE, sources=["t"], excluded_by="config_cap"),
    ])
    rows = store.members_for_day(key, first.date())
    instants = [first.replace(microsecond=0), second.replace(microsecond=0)]
    assert dry.stored_mismatches([{"AAA", "BBB"}, {"AAA"}], instants, rows) == (2, 0, [])
    assert dry.stored_mismatches([{"AAA"}, {"AAA"}], instants, rows) == (
        2, 0, ["scan 0: stored-only 1 · replay-only 0"])
