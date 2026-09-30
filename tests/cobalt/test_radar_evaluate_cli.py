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
    # STEP-4 of the setups one build serves the Range(micro) atoms (FINAL §3 D2).
    assert "Extension(day).state" in report.not_evaluable["example-range-break"]
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
    def tap_dot(self, card_id, factor, grade, *, settings, enabled, now=None):
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


# ---------------------------------------------------------------------
# The nightly replay's formations step (`cto-2026-09-24.md` R95;
# `reports/replay-deadline-fix-draft-2026-09-24.md` FIX 1 + FIX 2)
# ---------------------------------------------------------------------


def _replay(**kw):
    radar = ReadOnlyRadar(sup.members("FTFT", "BGFI"), {t: sup.fixture_bars(t) for t in ("FTFT", "BGFI")})
    lines: list[str] = []
    report = replay_formations(
        sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
        defs_source=lambda: ([sup.loaded()], {}), daily_source=_daily, tunables=sup.engine_tunables(),
        defaults=sup.defaults(), clock=session_clock(), out=lines.append, **kw,
    )
    return report, lines


def test_replay_formations_is_unchanged_by_the_shared_prep():
    """`cto-2026-09-24.md` R95 (`replay-deadline-fix-draft-2026-09-24.md` FIX 1):
    the replay with one member prep per scan equals the OLD loop re-stated
    here — `evaluate_member` per def with no prep — in its formations,
    counts, path-B lines and printed lines; an uncut replay plans and
    evaluates the same scans and names no cut."""
    from cobalt.radar.evaluate import MemberInput, evaluate_member
    from cobalt.radar.evaluate_cli import ReplayFormation, admitted_at, scan_instants

    report, lines = _replay()

    clock, rows, ld = session_clock(), sup.engine_tunables(), sup.loaded()
    members = [dict(m, trade_date=sup.TRADE_DATE) for m in sup.members("FTFT", "BGFI")]
    bars = {t: sup.fixture_bars(t) for t in ("FTFT", "BGFI")}
    first = min(m["entered_at"] for m in members)
    formations, counts, path_b, ref_lines = [], {}, [], []
    seen, b_seen = set(), set()
    instants = scan_instants(sup.TRADE_DATE, clock, int(rows["radar.scan_interval"].value), first)
    for instant in instants:
        for m in admitted_at(members, instant):
            inp = MemberInput(membership_id=m["id"], ticker=m["ticker"], trade_date=sup.TRADE_DATE, as_of=instant,
                              bars=tuple(b for b in bars[m["ticker"]] if b.ts < instant),
                              daily=_daily(m["ticker"], sup.TRADE_DATE), daily_status="cache-hit", rvol=None,
                              pool_position=m.get("last_rank"))
            ev = evaluate_member(ld, inp, tunables=rows, defaults=sup.defaults(),
                                 scan_interval=int(rows["radar.scan_interval"].value), clock=clock)
            counts[ev.evaluation] = counts.get(ev.evaluation, 0) + 1
            if ev.evaluation == "formed" and ev.formation is not None:
                key = (m["ticker"], ld.slug, ev.formation.formed_bar_ts.isoformat())
                if key not in seen:
                    seen.add(key)
                    f = ev.formation
                    formations.append(ReplayFormation(
                        seen_at=instant, ticker=m["ticker"], slug=ld.slug, direction=f.trade_direction,
                        trigger=str(f.trigger.price), stop=str(f.stop.price), formed_bar_ts=f.formed_bar_ts,
                        membership_id=ev.membership_id, trade_def_md5=ev.md5, score_inputs_sha256=ev.inputs_sha256))
                    ref_lines.append(
                        f"{clock.to_et(instant):%H:%M:%S} ET {m['ticker']} {ld.slug} FORMED {f.trade_direction} "
                        f"trigger {f.trigger.price} stop {f.stop.price} "
                        f"(formation bar {clock.to_et(f.formed_bar_ts):%H:%M} ET)")
            elif ev.evaluation == "not_evaluable" and ev.detail.extension_path == "B_only":
                if (m["ticker"], ld.slug) not in b_seen:
                    b_seen.add((m["ticker"], ld.slug))
                    line = (f"{clock.to_et(instant):%H:%M:%S} ET {m['ticker']} {ld.slug} path B only "
                            "— not evaluable in S2 (catalyst unknown, R4)")
                    path_b.append(line)
                    ref_lines.append(line)
    ref_lines.append(
        f"replay {sup.TRADE_DATE}: scans={len(instants)} formations={len(formations)} "
        f"path_b_only={len(path_b)} counts={dict(sorted(counts.items()))} writes: none")

    assert report.formations == formations
    assert report.counts == counts
    assert report.path_b_only == path_b
    assert lines == ref_lines
    assert report.scans_planned == report.scans == len(instants)
    assert report.cut_before is None


def test_replay_formations_stops_before_the_scan_the_cut_names_and_says_so():
    """`cto-2026-09-24.md` R95 (`replay-deadline-fix-draft-2026-09-24.md` FIX 2):
    `cut_at` is asked before each scan instant; from the k-th it answers
    True, so scans 1..k-1 are evaluated, the k-th is `cut_before`, nothing
    at or after it is a formation, and the cut is printed — never silent (L1)."""
    k = 60
    asked: list = []

    def cut_at(instant):
        asked.append(instant)
        return len(asked) >= k

    report, lines = _replay(cut_at=cut_at)
    full, _ = _replay()
    assert report.scans == k - 1
    assert report.scans_planned == full.scans_planned == full.scans
    assert report.cut_before == asked[k - 1]
    assert all(f.seen_at < report.cut_before for f in report.formations)
    at = session_clock().to_et(report.cut_before)
    text = "\n".join(lines)
    assert "CUT — the deadline stopped the formations replay before the" in text
    assert f"before the {at:%H:%M:%S} ET scan ({k - 1} of {full.scans} scans evaluated)" in text
    assert lines[-1].endswith(f"· CUT before {at:%H:%M:%S} ET")
