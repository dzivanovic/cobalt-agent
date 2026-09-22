"""S2-P2 STEP-4: `cobalt radar evaluate --replay <date> [--trade-def slug]`
writes NOTHING (R3/R9), and the dev-persistence harness that produces
candidate rows for the L52-d audit is a separate path (Astra R1-11)."""

from __future__ import annotations

import asyncio
import hashlib
from datetime import date, datetime, timezone
from pathlib import Path

import pytest

import radar_p2_support as sup
from cobalt.radar import evaluate_cli
from cobalt.radar.evaluate_cli import (
    CandidateRefused,
    candidate_run,
    curve_coverage_gaps,
    replay_formations,
)
from cobalt.settings.card import load_card_file
from cobalt.session import session_clock

UTC = timezone.utc


class ReadOnlyRadar(sup.FakeRadarStore):
    """Every read works; every write is a test failure."""

    def members_for_day(self, pool_key, day):
        return [dict(m, trade_date=day) for m in self.members]

    def __getattribute__(self, name):
        if name in {"apply_membership", "put_pool", "stamp_failure", "stamp_poll", "abandon_running_runs",
                    "open_score_run", "put_scores", "copy_card_values", "finish_run"}:
            raise AssertionError(f"the dry-run replay called the write method {name}")
        return super().__getattribute__(name)


def _daily(ticker, day):
    return sup.fixture_daily(ticker, datetime(2026, 1, 6, 12, 0, tzinfo=UTC))


def test_replay_cli_writes_nothing_and_lists_formations():
    radar = ReadOnlyRadar(sup.members("FTFT", "BGFI"), {t: sup.fixture_bars(t) for t in ("FTFT", "BGFI")})
    lines = []
    report = replay_formations(
        sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
        defs_source=lambda: ([sup.loaded()], {}), daily_source=_daily, tunables=sup.engine_tunables(),
        defaults=sup.defaults(), clock=session_clock(), out=lines.append,
    )
    text = "\n".join(lines)
    assert report.scans > 100
    formed = [f for f in report.formations if f.ticker == "FTFT"]
    assert formed and formed[0].direction == "short" and formed[0].formed_bar_ts == datetime(2026, 1, 6, 16, 22, tzinfo=UTC)
    assert "FTFT example-anatomy-reversal FORMED short" in text
    assert report.path_b_only and "path B only" in text
    assert "writes: none" in text
    assert radar.runs == {} and radar.scores == {}


def test_replay_filters_to_one_trade_def_and_names_not_evaluable_defs():
    import yaml

    from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH
    from cobalt.taxonomy.trade_def import TradeDef

    text = EXAMPLE_NOTE_PATH.read_text()
    mapping = yaml.safe_load(text.split("```yaml\n", 1)[1].split("\n```", 1)[0])["trade_def"]
    shipped = sup.loaded(TradeDef.from_unit(mapping, slug="example-range-break", name="Example Range Break"),
                         md5="fedcba9876543210fedcba9876543210")
    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    lines = []
    report = replay_formations(
        sup.TRADE_DATE, pool_key="pool", slug_filter="example-range-break", radar_store=radar,
        defs_source=lambda: ([sup.loaded(), shipped], {}), daily_source=_daily, tunables=sup.engine_tunables(),
        defaults=sup.defaults(), clock=session_clock(), out=lines.append,
    )
    assert report.formations == []
    assert "Range(micro).instantiated" in report.not_evaluable["example-range-break"]
    assert any("not evaluable: missing atoms" in line for line in lines)
    with pytest.raises(SystemExit, match="no loaded trade_def"):
        replay_formations(
            sup.TRADE_DATE, pool_key="pool", slug_filter="nope", radar_store=radar,
            defs_source=lambda: ([sup.loaded()], {}), daily_source=_daily, tunables=sup.engine_tunables(),
            defaults=sup.defaults(), clock=session_clock(), out=lines.append,
        )


ENABLED = """\
card_settings:
  radar.cards_enabled: true
  card.proposed_key: {a_plus_min: 0.9, a_min: 0.8, b_min: 0.6, c_min: 0.4}
  card.curves:
    atrs_from_open: [[1, 2], [6, 9]]
    rvol: [[1, 1], [3, 6], [10, 10]]
    Extension.leg_count: [[2, 3], [20, 9]]
    htf_level_proximity: [[0, 9], [2, 2]]
"""


def _frozen(tmp_path: Path, text: str = ENABLED):
    path = tmp_path / "d2.yaml"
    path.write_text(text, encoding="utf-8")
    return load_card_file(path, expected_sha256=hashlib.sha256(text.encode()).hexdigest())[0]


def test_candidate_harness_requires_full_curve_coverage(tmp_path):
    frozen = _frozen(tmp_path, ENABLED.replace("    rvol: [[1, 1], [3, 6], [10, 10]]\n", ""))
    assert curve_coverage_gaps([sup.loaded()], frozen) == {"example-anatomy-reversal": ["rvol"]}
    assert curve_coverage_gaps([sup.loaded()], _frozen(tmp_path)) == {}


def test_candidate_harness_refuses_outside_dev_and_without_enabled_settings(tmp_path, monkeypatch):
    from cobalt import env

    monkeypatch.setenv(env.ENV_VAR, "production")
    with pytest.raises(CandidateRefused, match="cobalt_dev"):
        evaluate_cli.assert_dev_database()
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    evaluate_cli.assert_dev_database()
    dark = _frozen(tmp_path, "card_settings:\n  radar.cards_enabled: false\n")
    with pytest.raises(CandidateRefused, match="cards_enabled"):
        asyncio.run(candidate_run(
            sup.TRADE_DATE, frozen=dark, taps=[], pool_key="pool", radar_store=None, card_store=None,
            defs_source=lambda: ([sup.loaded()], {}), settings_values=lambda: {}, daily_source=None,
            tunables_loader=sup.engine_tunables, defaults_loader=sup.defaults, clock=session_clock(),
        ))


class DayRadar(sup.FakeRadarStore):
    def members_for_day(self, pool_key, day):
        return [dict(m, trade_date=day) for m in self.members]


class TappingCards(sup.FakeCardStore):
    def tap_dot(self, card_id, factor, grade, *, bands, enabled, now=None):
        self.tap(card_id, factor, grade)
        return {"card_id": card_id}


def test_candidate_harness_persists_with_frozen_settings_and_simulated_taps(tmp_path):
    from cobalt.radar.anatomy.freshness import RvolObservation
    from cobalt.radar.evaluate_cli import receipt_rvol, rvol_as_of

    frozen = _frozen(tmp_path)
    radar = DayRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    cards = TappingCards()
    live_settings = sup.fixture_settings_rows(**{"radar.cards_enabled": False})
    # The captured production observations: RVOL as the day's dark receipts retained it.
    dark_receipts = [{"observations": {"members": [{"rvol": {
        **RvolObservation(ticker="FTFT", value=4.2, observed_at=datetime(2026, 1, 6, 14, 40 + i, tzinfo=UTC),
                          source="screen:s", candidates=("screen:s",)).model_dump(mode="json"),
        "sha256": "x"}}]}} for i in range(3)]
    captured = receipt_rvol(dark_receipts)
    assert rvol_as_of(captured, datetime(2026, 1, 6, 14, 41, 30, tzinfo=UTC))["FTFT"].observed_at.minute == 41
    report = asyncio.run(candidate_run(
        sup.TRADE_DATE, frozen=frozen, taps=[{"factor": "trail_fit", "grade": 6}, {"factor": "setup_relation", "grade": 8}],
        pool_key="pool", radar_store=radar, card_store=cards, defs_source=lambda: ([sup.loaded()], {}),
        settings_values=lambda: dict(live_settings),
        daily_source=lambda ticker, now: _async(sup.fixture_daily(ticker, now)),
        tunables_loader=sup.engine_tunables, defaults_loader=sup.defaults, clock=session_clock(),
        start=datetime(2026, 1, 6, 16, 20, tzinfo=UTC), stop=datetime(2026, 1, 6, 16, 50, tzinfo=UTC),
        rvol_at=lambda at: {"FTFT": RvolObservation(ticker="FTFT", value=4.2, observed_at=at, source="screen:s",
                                                    candidates=("screen:s",))},
    ))
    assert report.run_ids and all(radar.runs[i]["status"] == "complete" for i in report.run_ids)
    assert all(radar.runs[i]["cards_enabled"] is True for i in report.run_ids)  # the frozen D2 settings, not live dark
    assert report.cards_created and report.taps_applied == 2 * len(report.cards_created)
    card = cards.cards[report.cards_created[0]]
    assert {d.factor: d.trader_grade for d in card["dots"]}["trail_fit"] == 6
    published = [r["tap_versions"]["cards"][0]["published"] for r in cards.receipts if r["tap_versions"]["cards"]]
    assert any(p["conviction"] is not None for p in published)
    assert published and all(p["card_score"] is None and "assumed_formation" in p["score_suppressed"]
                             for p in published)
    assert live_settings["radar.cards_enabled"] is False  # trader_settings never written


async def _async(value):
    return value
