"""S2-P2 STEP-4 — scan-job stage S5 evaluate (R1, R2, R4, R9) and its
amendments (Astra R1-6/7/11/14/15/16).

Real-shape bars/daily/settings fixtures, the shipped synthetic
anatomy-only def, in-memory stores (`radar_p2_support`). The FTFT fixture
forms Extension path A on the 11:22 ET (16:22 UTC) 2-minute bar: first
visible to a scan at 16:24 UTC; path B only before that.
"""

from __future__ import annotations

import asyncio
import os
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

import radar_p2_support as sup
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import (
    EvaluateError,
    EvaluateStage,
    ReplayError,
    canonical_sha256,
    evaluate_member,
    replay_receipt,
    seam_safe_missing_atoms,
)
from cobalt.radar.runner import StageDropped
from cobalt.session import session_clock

UTC = timezone.utc
FORMED = datetime(2026, 1, 6, 16, 22, tzinfo=UTC)
#: The base scan. The 16:22 formation is visible from 16:24, but until the
#: run settles the next unclosed minute prints through the 2¢ stop over the
#: still-rising extreme (no card, re-evaluated next scan); by 16:30 the
#: tracked extreme is 5.79, the stop 5.81, the trigger 5.50 — a card lands.
SCAN0 = datetime(2026, 1, 6, 16, 30, tzinfo=UTC)

ENABLED_CARD = {
    "radar.cards_enabled": True,
    "card.proposed_key": {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4},
    "card.curves": {
        "atrs_from_open": [[1, 2], [6, 9]],
        "rvol": [[1, 1], [3, 6], [10, 10]],
        "Extension.leg_count": [[2, 3], [20, 9]],
        "htf_level_proximity": [[0, 9], [2, 2]],
    },
}


class World:
    def __init__(self, *, cards_enabled=True, defs=None, tickers=("FTFT",), card=None):
        self.radar = sup.FakeRadarStore(sup.members(*tickers), {t: sup.fixture_bars(t) for t in tickers})
        self.cards = sup.FakeCardStore()
        card_rows = ENABLED_CARD if cards_enabled else {"radar.cards_enabled": False}
        self.settings = sup.fixture_settings_rows(**(card or card_rows))
        self.defs = defs or [sup.loaded()]
        self.instant = [SCAN0]
        self.daily_calls = []
        self.stage = EvaluateStage(
            radar_store=self.radar, card_store=self.cards,
            defs_source=lambda: (self.defs, {}),
            settings_values=lambda: dict(self.settings),
            daily_source=self._daily, tunables_loader=sup.engine_tunables,
            defaults_loader=sup.defaults, clock=session_clock(), now=lambda: self.instant[0],
        )
        self.gate = sup.Gate()

    async def _daily(self, ticker, now):
        self.daily_calls.append(ticker)
        return sup.fixture_daily(ticker, now)

    def scan(self, at: datetime):
        self.instant[0] = at
        rvol = {t["ticker"]: RvolObservation(ticker=t["ticker"], value=4.2, observed_at=at, source="screen:s",
                                             candidates=("screen:s",)) for t in self.radar.members}
        return asyncio.run(self.stage.run(
            pool_key="pool", scan_id=int(at.timestamp() * 1000), session="RTH", instant=at, rvol=rvol,
            pool_unit={"pool_block": {"cap": 50}, "source_sets": []}, gate=self.gate,
        ))


def _ev(outcome, ticker="FTFT"):
    return [e for e in outcome.evaluations if e.ticker == ticker]


# ---------------------------------------------------------------------
# F8 acceptance (§4)
# ---------------------------------------------------------------------


def test_cards_enabled_false_writes_seam_rows_and_no_card():
    world = World(cards_enabled=False)
    outcome = world.scan(SCAN0)
    assert [e.evaluation for e in outcome.evaluations] == ["formed"]
    assert len(world.radar.scores) == 1 and world.radar.runs[1]["status"] == "complete"
    assert world.radar.runs[1]["cards_enabled"] is False
    assert len(world.cards.receipts) == 1
    assert world.cards.cards == {} and world.cards.transitions == []
    assert world.radar.board("pool")[0]["evaluation"] == "formed"
    assert world.radar.board("pool")[0]["card_score"] is None


def test_def_without_evaluable_precondition_renders_not_evaluable_never_a_card():
    import yaml

    from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH
    from cobalt.taxonomy.trade_def import TradeDef

    text = EXAMPLE_NOTE_PATH.read_text()
    mapping = yaml.safe_load(text.split("```yaml\n", 1)[1].split("\n```", 1)[0])["trade_def"]
    shipped = TradeDef.from_unit(mapping, slug="example-range-break", name="Example Range Break")
    world = World(defs=[sup.loaded(shipped, md5="fedcba9876543210fedcba9876543210")])
    outcome = world.scan(SCAN0)
    ev = outcome.evaluations[0]
    assert ev.evaluation == "not_evaluable" and ev.formation is None
    # Setups one build STEP-4 serves its Range(micro) atoms, `range_break`
    # and `range_base` (FINAL §3 D2, §2.2, §2.3): the one atom still missing
    # is its avoid's `Extension(day).state`.
    assert ev.missing == ("Extension(day).state",)
    assert "Extension(day).state" in ev.detail.missing_atoms
    assert world.cards.cards == {}
    assert world.radar.runs[1]["status"] == "complete"


def test_seam_safe_missing_atoms_replaces_a_free_word_atom_with_a_generic_marker():
    """S3 detectors are unbuilt, so a live note's precondition is free to
    name a placeholder atom that isn't real anatomy vocabulary yet (e.g.
    a two-word descriptive label) — the closed seam still refuses free
    text (L32), but the WHOLE evaluate run must not crash on it (a
    production incident: `evaluate_member` used to raise a pydantic
    ValidationError straight out of the not-evaluable branch)."""
    safe = seam_safe_missing_atoms(["Level_ref(HTF resistance)", "DayRange", "DayRange"])
    assert safe == ("DayRange", "unspecified_atom")


def test_def_with_a_free_word_missing_atom_is_not_evaluable_not_a_crash():
    td = sup.anatomy_def(preconditions=[{"expr": "Level_ref(free text here) == culminating"}])
    world = World(defs=[sup.loaded(td, md5="deadbeefdeadbeefdeadbeefdeadbeef")])
    outcome = world.scan(SCAN0)
    ev = outcome.evaluations[0]
    assert ev.evaluation == "not_evaluable"
    assert "unspecified_atom" in ev.detail.missing_atoms
    assert "Level_ref(free text here)" in ev.missing  # user-side field: raw text kept for local reporting
    assert world.cards.cards == {}


def test_path_b_only_formation_is_not_evaluable():
    world = World()
    outcome = world.scan(datetime(2026, 1, 6, 16, 0, tzinfo=UTC))
    ev = outcome.evaluations[0]
    assert ev.evaluation == "not_evaluable" and ev.detail.extension_path == "B_only"
    assert "catalyst" in ev.note
    assert world.cards.cards == {}


def test_one_open_radar_card_per_member_def_direction():
    world = World()
    world.scan(SCAN0)
    world.scan(SCAN0 + timedelta(seconds=100))
    world.scan(SCAN0 + timedelta(seconds=200))
    assert len(world.cards.cards) == 1
    card = world.cards.cards[1]
    assert (card["pool_member_id"], card["trade_def_slug"], card["direction"]) == (100, "example-anatomy-reversal", "short")
    # a concurrent writer already holds the open card: the database conflict is "already open", never a second row
    world2 = World()
    world2.cards.create_radar_card = lambda spec, **kw: None
    outcome = world2.scan(SCAN0)
    assert outcome.created == [] and world2.radar.runs[1]["status"] == "complete"


def test_card_is_born_unsized_in_watch_with_formation_evidence_and_dots():
    world = World()
    outcome = world.scan(SCAN0)
    assert outcome.created == [1]
    card = world.cards.cards[1]
    assert card["state"] == "WATCH" and card["origin"] == "radar"
    assert card["grade"] is None and card["risk_budget"] is None and card["shares"] is None
    assert card["trigger_price"] == card["entry"] and card["structural_stop"] == card["stop"]
    assert card["formed_at"] == FORMED
    assert card["why"] and card["setup_ref"] == "unclassified" and card["trigger_type"] == "bar_break"
    # the deadline is resolved from preferred_windows_ref at formation and persisted (R1-16)
    assert card["expires_at"] == datetime(2026, 1, 6, 15, 30, tzinfo=ZoneInfo("America/New_York"))
    genesis = world.cards.transitions[0]
    assert genesis["from"] is None and genesis["actor"] == "cobalt"
    assert genesis["evidence"]["run_id"] == 1 and genesis["evidence"]["formation_bar_ts"] == FORMED.isoformat()
    assert genesis["evidence"]["atoms"]
    dots = {d.factor: d for d in card["dots"]}
    assert dots["rvol"].role == "shadow" and dots["rvol"].engine_grade is not None
    assert dots["trail_fit"].na_reason == "MANUAL"
    assert card["card_score"] is None and "trail_fit" in card["score_suppressed"]
    # the seam row carries the card's values, copied at run time
    assert world.radar.scores[1]["proximity"] == card["proximity"]


def test_expiry_end_of_window_avoid_or_stop():
    # deadline: a window that closes at 11:50 ET
    td = sup.anatomy_def(preferred_windows_ref="anatomy: 09:45-11:50")
    world = World(defs=[sup.loaded(td)])
    world.scan(SCAN0)
    world.scan(datetime(2026, 1, 6, 16, 52, tzinfo=UTC))
    assert world.cards.cards[1]["state"] == "EXPIRED"
    assert world.cards.transitions[-1]["evidence"]["cause"] == "deadline"

    # avoid turning true: leg count passes 16 after creation
    td = sup.anatomy_def(avoid=[{"expr": "NOT Extension.instantiated"}, {"expr": "Extension.leg_count >= 16"}])
    world = World(defs=[sup.loaded(td)])
    world.scan(datetime(2026, 1, 6, 16, 30, tzinfo=UTC))
    assert world.cards.cards[1]["state"] == "WATCH"
    world.scan(datetime(2026, 1, 6, 16, 50, tzinfo=UTC))
    assert world.cards.cards[1]["state"] == "EXPIRED"
    assert world.cards.transitions[-1]["evidence"]["cause"] == "avoid"

    # stop touched before arm: the run makes a new high above the 5.81 stop
    world = World()
    world.scan(SCAN0)
    world.scan(datetime(2026, 1, 6, 17, 30, tzinfo=UTC))
    assert world.cards.cards[1]["state"] == "EXPIRED"
    assert world.cards.transitions[-1]["evidence"]["cause"] == "stop_before_arm"


def test_no_new_watch_after_the_deadline_and_no_duplicate_for_a_consumed_formation():
    td = sup.anatomy_def(preferred_windows_ref="anatomy: 09:45-11:20")
    world = World(defs=[sup.loaded(td)])
    world.scan(SCAN0)  # 11:30 ET, past an 11:20 deadline
    assert world.cards.cards == {}
    world = World()
    world.scan(SCAN0)
    world.cards.cards[1]["state"] = "PASSED"
    world.scan(SCAN0 + timedelta(seconds=100))  # same 16:22 formation still culminating
    assert len(world.cards.cards) == 1


def test_a_genuinely_new_formation_is_not_blocked():
    world = World()
    world.scan(SCAN0)
    world.cards.cards[1]["state"] = "PASSED"
    world.cards.cards[1]["formed_at"] = FORMED - timedelta(minutes=30)  # an earlier, different formation
    world.scan(SCAN0 + timedelta(seconds=100))
    assert len(world.cards.cards) == 2 and world.cards.cards[2]["formed_at"] == FORMED


def test_stop_touched_before_formation_does_not_expire_the_card():
    from cobalt.cards import expire as expire_mod
    from cobalt.cards.models import CardState
    from cobalt.radar import evaluate as evaluate_mod

    # The rule: only bars that open after the formation bar CLOSED count.
    stop = Decimal("5.81")
    before = [sup.fixture_bars("FTFT")[0].model_copy(update={"ts": FORMED, "high": Decimal("6.00")})]
    assert expire_mod.radar_expiry(
        state=CardState.WATCH, now=SCAN0, expires_at=SCAN0 + timedelta(hours=1), avoided=False,
        direction="short", stop=stop, bars_after_formation=[],
    ) is None
    after = [before[0].model_copy(update={"ts": FORMED + timedelta(minutes=2)})]
    assert expire_mod.radar_expiry(
        state=CardState.WATCH, now=SCAN0, expires_at=SCAN0 + timedelta(hours=1), avoided=False,
        direction="short", stop=stop, bars_after_formation=after,
    ).cause == "stop_before_arm"
    # ...and the stage hands radar_expiry only post-formation bars.
    seen = []
    real = evaluate_mod.radar_expiry

    def spy(**kw):
        seen.append(kw)
        return real(**kw)

    world = World()
    world.scan(SCAN0)
    evaluate_mod.radar_expiry = spy
    try:
        world.scan(SCAN0 + timedelta(seconds=100))
    finally:
        evaluate_mod.radar_expiry = real
    refresh = [kw for kw in seen if kw["expires_at"] == world.cards.cards[1]["expires_at"]]
    assert refresh and all(b.ts >= FORMED + timedelta(minutes=2) for kw in refresh for b in kw["bars_after_formation"])
    assert before[0].ts < FORMED + timedelta(minutes=2)
    assert world.cards.cards[1]["state"] == "WATCH"


def test_armed_and_triggered_expire_on_deadline_filled_never():
    for state, expected in (("ARMED", "EXPIRED"), ("TRIGGERED", "EXPIRED"), ("FILLED", "FILLED")):
        td = sup.anatomy_def(preferred_windows_ref="anatomy: 09:45-11:50")
        world = World(defs=[sup.loaded(td)])
        world.scan(SCAN0)
        world.cards.cards[1]["state"] = state
        world.scan(datetime(2026, 1, 6, 16, 52, tzinfo=UTC))
        assert world.cards.cards[1]["state"] == expected, state
    # stop touch never expires an ARMED card
    world = World()
    world.scan(SCAN0)
    world.cards.cards[1]["state"] = "ARMED"
    world.scan(datetime(2026, 1, 6, 17, 30, tzinfo=UTC))
    assert world.cards.cards[1]["state"] == "ARMED"


def test_departed_member_card_keeps_refreshing_and_reentry_makes_no_second_card():
    world = World()
    world.scan(SCAN0)
    world.radar.members[0]["left_at"] = SCAN0 + timedelta(seconds=50)
    outcome = world.scan(SCAN0 + timedelta(seconds=100))
    assert outcome.refreshed == [1] and outcome.created == []
    assert [e.departed for e in outcome.evaluations] == [True]
    # re-entry: a new membership episode for the same ticker
    world.radar.members.append({**world.radar.members[0], "id": 200, "left_at": None})
    outcome = world.scan(SCAN0 + timedelta(seconds=200))
    assert outcome.created == [] and len(world.cards.cards) == 1
    assert world.stage.lifecycle_tickers(["AAA"]) == ["FTFT"]
    assert world.stage.lifecycle_tickers(["FTFT"]) == []


def test_filled_card_gets_an_entry_snapshot_and_health_pills():
    world = World()
    world.scan(SCAN0)
    world.cards.cards[1]["state"] = "FILLED"
    world.scan(SCAN0 + timedelta(seconds=100))
    health = world.cards.cards[1]["health"]
    assert health["entry_snapshot"]["rvol"] == "4.2"
    classes = {p["klass"] for p in health["pills"]}
    assert classes == {"participation", "cost", "dot", "structural"}
    assert next(p for p in health["pills"] if p["klass"] == "cost")["status"] == "n/a"
    first = health["entry_snapshot"]
    world.scan(SCAN0 + timedelta(seconds=200))
    assert world.cards.cards[1]["health"]["entry_snapshot"] == first  # captured once


def test_settings_are_read_on_every_cycle():
    world = World(cards_enabled=False)
    world.scan(SCAN0)
    assert world.cards.cards == {}
    world.settings.update(ENABLED_CARD)
    world.scan(SCAN0 + timedelta(seconds=100))
    assert len(world.cards.cards) == 1


def test_missing_cards_enabled_setting_fails_loud_before_any_write():
    world = World()
    world.settings.pop("radar.cards_enabled")
    with pytest.raises(Exception, match="radar.cards_enabled"):
        world.scan(SCAN0)
    assert world.radar.runs == {}


# ---------------------------------------------------------------------
# Publish ordering across the two sides (R1-14)
# ---------------------------------------------------------------------


def test_publish_is_the_last_write_and_a_failure_leaves_no_published_partial():
    world = World()
    world.scan(SCAN0)
    assert world.radar.writes[-1] == "finish:complete"
    assert world.gate.labels.index("evaluate:receipt") < world.gate.labels.index("evaluate:publish")
    world.cards.fail_on = "receipt"
    with pytest.raises(EvaluateError, match="receipt"):
        world.scan(SCAN0 + timedelta(seconds=100))
    assert world.radar.runs[2]["status"] == "failed"
    assert all(s["run_id"] == 1 for s in world.radar.board("pool"))


def test_a_crash_before_publish_is_abandoned_next_cycle_and_the_retry_makes_no_duplicate():
    world = World()
    world.gate.drop_at = "evaluate:publish"
    with pytest.raises(StageDropped):
        world.scan(SCAN0)
    assert world.radar.runs[1]["status"] == "running"
    assert world.radar.board("pool") == []
    assert len(world.cards.cards) == 1  # the user-side card landed before the crash
    world.gate.drop_at = None
    world.scan(SCAN0 + timedelta(seconds=100))
    assert world.radar.runs[1]["status"] == "failed" and "abandoned" in world.radar.runs[1]["failed_detail"]
    assert world.radar.runs[2]["status"] == "complete"
    assert len(world.cards.cards) == 1


def test_a_card_refusal_does_not_lose_the_run_but_is_reported():
    world = World()
    world.cards.fail_on = "create"
    outcome = world.scan(SCAN0)
    assert outcome.refusals and "account mode" in outcome.refusals[0]
    assert world.radar.runs[1]["status"] == "complete"


# ---------------------------------------------------------------------
# Replay from stored inputs (L57, R1-10)
# ---------------------------------------------------------------------


def test_run_hashes_present():
    world = World()
    world.scan(SCAN0)
    run = world.radar.runs[1]
    for key in ("formula_sha256", "tunables_sha256", "settings_sha256", "cohort_sha256"):
        assert len(run[key]) == 64 and int(run[key], 16) >= 0
    assert run["evaluator_version"]
    card = world.cards.cards[1]
    assert card["formula_sha256"] == run["formula_sha256"] and card["settings_sha256"] == run["settings_sha256"]


def test_every_card_number_replays_from_stored_inputs():
    world = World()
    world.scan(SCAN0)
    world.cards.tap(1, "trail_fit", 7)
    world.cards.tap(1, "tape_absorption_at_bound", 8)
    world.scan(SCAN0 + timedelta(seconds=100))
    card = world.cards.cards[1]
    assert card["conviction"] is not None
    assert card["card_score"] is None and "assumed_formation" in card["score_suppressed"]
    receipts = list(world.cards.receipts)
    published_scores = {s["membership_id"]: s for s in world.radar.scores.values() if s["run_id"] == 2}

    # everything moves or vanishes afterwards: settings, the note, the bars, the taps
    world.settings["card.curves"] = {"rvol": [[0, 10], [1, 1]]}
    world.defs = []
    world.radar.bars.clear()
    world.cards.taps.clear()

    evaluations, cards = replay_receipt(receipts, clock=session_clock())
    assert [c.recomputed for c in cards] == [c.published for c in cards]
    assert cards and cards[0].recomputed["card_score"] == card["card_score"]
    replayed = {e.membership_id: e for e in evaluations}
    assert replayed[100].evaluation == published_scores[100]["evaluation"]
    assert replayed[100].detail.model_dump(mode="json") == published_scores[100]["detail"]
    assert replayed[100].inputs_sha256 == published_scores[100]["inputs_sha256"]


def test_a_dark_run_replays_from_its_receipt_too():
    world = World(cards_enabled=False)
    world.scan(SCAN0)
    world.scan(SCAN0 + timedelta(seconds=100))
    receipts = list(world.cards.receipts)
    world.radar.bars.clear()
    evaluations, cards = replay_receipt(receipts, clock=session_clock())
    assert cards == []
    assert [e.detail.model_dump(mode="json") for e in evaluations] == [
        s["detail"] for s in world.radar.scores.values() if s["run_id"] == 2
    ]


def test_receipt_chain_stores_deltas_and_refuses_a_tampered_chain():
    world = World()
    world.scan(SCAN0)
    world.scan(SCAN0 + timedelta(seconds=100))
    first, second = world.cards.receipts
    base = first["observations"]["members"][0]["bars"]
    delta = second["observations"]["members"][0]["bars"]
    assert second["observations"]["base_receipt_id"] == first["id"]
    assert len(delta["rows_delta"]) < len(base["rows_delta"]) and delta["row_count"] > base["row_count"]
    assert second["tunables_snapshot"] == {"unchanged_since_receipt": first["id"],
                                           "sha256": first["tunables_snapshot"]["sha256"]}
    with pytest.raises(ReplayError):
        replay_receipt([second], clock=session_clock())  # the base is missing
    tampered = [first, {**second}]
    tampered[0] = {**first, "observations": {**first["observations"], "members": [
        {**first["observations"]["members"][0],
         "bars": {**base, "rows_delta": [{**base["rows_delta"][0], "close": "999"}, *base["rows_delta"][1:]]}},
    ]}}
    with pytest.raises(ReplayError, match="sha256"):
        replay_receipt(tampered, clock=session_clock())


def test_seam_rows_are_generic_and_carry_no_trade_def_content():
    import json

    world = World()
    world.scan(SCAN0)
    row = json.dumps(world.radar.scores[1], default=str)
    card_why = world.cards.cards[1]["why"]
    for forbidden in ("example-anatomy-reversal", "Example Anatomy Reversal", "overextension", "bars_cleared", card_why,
                      "snapback_candle", "09:45-15:30"):
        assert forbidden not in row, forbidden


# ---------------------------------------------------------------------
# Through the runner: S1-S5 (R1)
# ---------------------------------------------------------------------


from cobalt.radar.config import load_config  # noqa: E402
from cobalt.radar.collector import ScreenerSnapshot  # noqa: E402
from cobalt.radar.notes import load_sources  # noqa: E402
from cobalt.radar.poller import PollResult  # noqa: E402
from cobalt.radar.runner import RadarRunner  # noqa: E402


#: R16 "C": not-equity is a non-blank `Asset Type` OR a fund `Industry`,
#: so an ordinary stock carries a BLANK `Asset Type` and an ordinary
#: industry — which is what Finviz actually returns for one.
_SCREEN_HEADER = ("Ticker", "Volume", "Relative Volume", "Asset Type", "Industry")


class _Collector:
    async def screen(self, _block, now):
        return ScreenerSnapshot("screen-synthetic", now,
                                ({"Ticker": "FTFT", "Volume": "9", "Relative Volume": "4.2",
                                  "Asset Type": "", "Industry": "Capital Markets"},),
                                _SCREEN_HEADER)

    async def listed(self, _block, now):
        return [ScreenerSnapshot("list-synthetic", now, (), _SCREEN_HEADER)]


class _Pool:
    def __init__(self):
        self.failures = []

    def pool_row(self, _key): return None
    def open_members(self, _key): return []
    def apply_membership(self, **kw): kw["before_commit"]()
    def put_pool(self, _row, **kw): kw["before_commit"]()
    def stamp_poll(self, *_a, **kw): kw["before_commit"]()

    def stamp_failure(self, _key, **kw):
        self.failures.append((kw["failed_stage"], kw["failed_detail"]))


class _Settings:
    def values(self): return {}
    def put(self, _rows, *, source, before_commit=None):
        before_commit()
        return {}


class _Poller:
    def __init__(self):
        self.polled = []

    async def poll(self, members, *, before_commit, **_kw):
        self.polled.append([m.ticker for m in members])
        return PollResult([], {m.ticker: 0 for m in members})


def _runner(world, clock, now, *, poller=None, pool=None, ceiling=40):
    parsed = load_sources(
        Path("tests/fixtures/radar/radar-screens.example.md"), Path("tests/fixtures/radar/radar-lists.example.md"),
        scan_interval=100, poll_interval=100, finviz_max_rpm=ceiling, list_chunk_size=50, context_tickers=0,
    )
    return RadarRunner(
        config=load_config(), sources_loader=lambda: parsed, collector=_Collector(), radar_store=pool or _Pool(),
        settings_store=_Settings(), poller=poller or _Poller(), clock=clock, now=now,
        evaluator=world.stage, ceiling_rpm=ceiling,
    )


def test_rubberband_precondition_on_pool_name_produces_card_within_one_scan_interval():
    world = World()
    clock = session_clock()
    t = [datetime(2026, 1, 6, 16, 20, tzinfo=UTC)]
    runner = _runner(world, clock, lambda: t[0])
    scans, created_at = [], None
    while t[0] <= datetime(2026, 1, 6, 16, 40, tzinfo=UTC):
        world.instant[0] = t[0]
        result = asyncio.run(runner.cycle())
        assert result.failed_stage is None, result.detail
        scans.append(t[0])
        if world.cards.cards and created_at is None:
            created_at = t[0]
        t[0] += timedelta(seconds=100)
    assert created_at is not None

    # Formation, judged independently of the stage: the def evaluates
    # `formed` AND its structural stop is untouched by every closed bar
    # since the formation bar closed. The stop re-anchors 2¢ over the
    # run's high as each bucket closes, so while the run still extends the
    # formation flickers minute by minute (valid 16:24, not 16:25, valid
    # 16:26, not 16:27, steady from 16:28). What the stage can guarantee
    # at its cadence: no scan at which the formation was valid passes
    # without a card, and the card lands within one scan interval of the
    # start of the valid window it lands in.
    from cobalt.cards.expire import radar_expiry
    from cobalt.cards.models import CardState

    def valid(at):
        ev = evaluate_member(sup.loaded(), sup_member(sup.fixture_bars("FTFT"), at),
                             tunables=sup.engine_tunables(), defaults=sup.defaults(), scan_interval=100,
                             clock=session_clock())
        return ev.evaluation == "formed" and radar_expiry(
            state=CardState.WATCH, now=at, expires_at=at + timedelta(hours=1), avoided=False,
            direction=ev.formation.trade_direction, stop=ev.formation.stop.price,
            bars_after_formation=list(ev.i1_after),
        ) is None

    assert created_at == next(at for at in scans if valid(at))
    window_start = created_at.replace(second=0)
    assert valid(window_start)
    while valid(window_start - timedelta(minutes=1)):
        window_start -= timedelta(minutes=1)
    assert timedelta(0) <= created_at - window_start <= timedelta(seconds=100), (window_start, created_at)
    assert all(run["status"] == "complete" for run in world.radar.runs.values())


def test_market_reset_drops_evaluate_stage():
    world = World()
    world.gate.drop_at = None

    class Crossing:
        def __init__(self):
            self.real = session_clock()
            self.calls = 0
            self.calendar = self.real.calendar

        def session(self, instant):
            from cobalt.session.models import Session
            return Session.MARKET_RESET if self.cross else self.real.session(instant)

        def to_et(self, value):
            return self.real.to_et(value)

    clock = Crossing()
    clock.cross = False
    pool = _Pool()
    runner = _runner(world, clock, lambda: SCAN0, pool=pool)
    original = world.stage.run

    async def crossing_run(**kw):
        gate = kw["gate"]

        def crossed(label):
            check = gate(label)

            def run_check():
                if label == "evaluate:scores":
                    clock.cross = True
                check()
            return run_check
        return await original(**{**kw, "gate": crossed})

    world.stage.run = crossing_run
    result = asyncio.run(runner.cycle())
    assert result.state == "dropped" and result.failed_stage == "evaluate"
    assert world.radar.board("pool") == [] and world.radar.scores == {}
    assert world.cards.cards == {} and world.cards.receipts == []


def test_evaluate_failure_stamps_failed_stage_and_s1_to_s4_stand():
    world = World()
    world.radar.fail_on = "scores"
    pool, poller = _Pool(), _Poller()
    runner = _runner(world, session_clock(), lambda: SCAN0, pool=pool, poller=poller)
    world.instant[0] = SCAN0
    result = asyncio.run(runner.cycle())
    assert result.state == "scanning" and result.failed_stage == "evaluate"
    assert pool.failures and pool.failures[-1][0] == "evaluate" and "synthetic seam failure" in pool.failures[-1][1]
    assert poller.polled == [["FTFT"]]
    assert world.radar.runs[1]["status"] == "failed"


def test_lifecycle_tickers_polled_only_inside_the_demand_ceiling():
    world = World()
    world.scan(SCAN0)
    world.radar.members[0]["left_at"] = SCAN0  # FTFT departed, its card is open
    world.radar.members.append({"id": 300, "ticker": "BGFI", "trade_date": sup.TRADE_DATE,
                                "entered_at": SCAN0, "left_at": None, "last_rank": 1})
    world.radar.bars["BGFI"] = sup.fixture_bars("BGFI")

    class BgfiCollector(_Collector):
        async def screen(self, _block, now):
            return ScreenerSnapshot("screen-synthetic", now,
                                    ({"Ticker": "BGFI", "Volume": "9", "Relative Volume": "1",
                                      "Asset Type": "", "Industry": "Capital Markets"},),
                                    _SCREEN_HEADER)

    poller = _Poller()
    runner = _runner(world, session_clock(), lambda: SCAN0 + timedelta(seconds=100), poller=poller)
    runner.collector = BgfiCollector()
    world.instant[0] = SCAN0 + timedelta(seconds=100)
    asyncio.run(runner.cycle())
    assert poller.polled[-1] == ["BGFI", "FTFT"]

    tight = _Poller()
    pool = _Pool()
    runner = _runner(world, session_clock(), lambda: SCAN0 + timedelta(seconds=200), poller=tight, pool=pool)
    runner.collector = BgfiCollector()
    runner.ceiling_rpm = runner.sources_loader().planned_rpm  # no headroom for one more name
    world.instant[0] = SCAN0 + timedelta(seconds=200)
    result = asyncio.run(runner.cycle())
    assert tight.polled[-1] == ["BGFI"]
    assert any("lifecycle" in detail for _stage, detail in pool.failures)
    assert result.failed_stage is not None


# ---------------------------------------------------------------------
# requires_vault — the live strategy note, end to end (hub-run)
# ---------------------------------------------------------------------

LIVE_VAULT_ENV = "COBALT_LIVE_VAULT_ROOT"
requires_vault = pytest.mark.skipif(not os.getenv(LIVE_VAULT_ENV),
                                    reason=f"{LIVE_VAULT_ENV} not set — the hub runs the live-note proof")


@requires_vault
def test_live_defined_notes_evaluate_on_the_fixture_bars_and_only_the_evaluable_one_can_form(capsys):
    """FINAL §9 gate 3 / [F-16] (2): for every def the registry calls
    evaluable — never `Setup(relation)` in a `not_evaluable` outcome, and
    `formed` in its outcome set unless its own avoid is `avoided` on those
    scans or it is pinned in `AWAITING_A_DAY` (printed). A def the registry
    does NOT call evaluable is `not_evaluable` on every scan. The deploy runs
    this with `COBALT_LIVE_VAULT_ROOT` set; a SKIP there is RED, pinned in
    AWAITING_A_DAY, AWAITING_A_RULING or AWAITING_AN_ENGINE_FILL while its hole
    is null (printed), or proven on its committed day through gate 2's check
    with his merged rows (FINAL §9 gate 3, "on its fixture day")."""
    from cobalt.radar.anatomy.registry import evaluability
    from cobalt.taxonomy.vault_loader import load_vault_trade_defs
    from test_setups_lego import AWAITING_A_DAY, AWAITING_A_RULING, AWAITING_AN_ENGINE_FILL, _forms_on_a_committed_day
    import setups_shapes as shapes

    loaded = load_vault_trade_defs(vault_root=Path(os.environ[LIVE_VAULT_ENV]))
    defs = [sup.LoadedDef(slug=d.slug, md5=d.md5, definition=d.definition) for d in loaded.defs]
    user_rows = {t.key: t.row for t in loaded.user_tunables}
    tunables = {**sup.engine_tunables(), **user_rows}
    bars = sup.fixture_bars("FTFT")
    seen, missing = {}, {}
    for minute in range(0, 180, 2):
        at = datetime(2026, 1, 6, 15, 0, tzinfo=UTC) + timedelta(minutes=minute)
        member = sup_member(bars, at)
        for ld in defs:
            ev = evaluate_member(ld, member, tunables=tunables, defaults=sup.defaults(), scan_interval=100,
                                 clock=session_clock())
            seen.setdefault(ld.slug, set()).add(ev.evaluation)
            if ev.evaluation == "not_evaluable":
                missing.setdefault(ld.slug, set()).update(ev.missing)
    with capsys.disabled():
        for slug, outcomes in sorted(seen.items()):
            print(f"{slug}: {sorted(outcomes)}")
    for ld in defs:
        outcomes = seen[ld.slug]
        if not evaluability(ld.definition).evaluable:
            assert outcomes == {"not_evaluable"}, ld.slug
            continue
        assert "Setup(relation)" not in missing.get(ld.slug, set()), ld.slug
        if ld.slug in AWAITING_A_DAY or ld.slug in AWAITING_A_RULING:
            with capsys.disabled():
                print(f"AWAITING A {'DAY' if ld.slug in AWAITING_A_DAY else 'RULING'}: {ld.slug}")
            continue
        if "formed" in outcomes or "avoided" in outcomes:
            continue
        # FINAL §9 gate 3: formed "on its fixture day" — gate 2's committed-day
        # check (test_setups_lego), run on HIS live def with HIS merged rows.
        assert ld.slug in shapes.SHAPES, (ld.slug, sorted(outcomes))
        forms = _forms_on_a_committed_day(ld.slug, shapes.SHAPES[ld.slug], ld, tunables)
        holes = [key for key in AWAITING_AN_ENGINE_FILL.get(ld.slug, ())
                 if tunables.get(key) is None or tunables[key].value is None]
        if holes:
            # Pinned like gate 2's `<slug>_without_its_engine_fill` tests: the
            # hole's row is not in his vault yet; the day it is, this asserts forms.
            with capsys.disabled():
                print(f"AWAITING ITS ENGINE FILL: {ld.slug} ({', '.join(holes)} null)")
            assert not forms, (ld.slug, holes)
            continue
        assert forms, (ld.slug, sorted(outcomes))


def sup_member(bars, at):
    from cobalt.radar.evaluate import MemberInput

    return MemberInput(
        membership_id=100, ticker="FTFT", trade_date=sup.TRADE_DATE, as_of=at, bars=tuple(bars),
        daily=sup.fixture_daily("FTFT", at), daily_status="cache-hit",
        rvol=RvolObservation(ticker="FTFT", value=4.2, observed_at=at, source="screen:s", candidates=("screen:s",)),
    )
