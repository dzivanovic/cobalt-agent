"""R692 — the radar's price floor (card 137), offline.

The radar removes every stock priced at or below `price_floor`
(`configs/cobalt/radar.yaml`) ONCE per scan, in `RadarRunner._collect`,
after every screen and list row is gathered and before `decide()` ranks
anything (F1). An ADMITTED member read under the floor departs at once
with `excluded_by=price_floor` (F2); a radar WATCH card on a floored
ticker goes to EXPIRED, nothing else moves (F3); the floor is the
config's, never a literal (F4); the departed / excluded reads hide
`price_floor` rows and every DRC-side reader asks for them back (F5).

Every ticker, price and date here is constructed (L32).
"""

from __future__ import annotations

import asyncio
import inspect
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from types import SimpleNamespace
from zoneinfo import ZoneInfo

import pytest
from loguru import logger

import cobalt
from cobalt.cards.models import CardState, IllegalTransition
from cobalt.cards.store import CardStore
from cobalt.radar import runner as runner_module
from cobalt.radar.collector import ScreenerSnapshot
from cobalt.radar.config import load_config
from cobalt.radar.models import OpenMember
from cobalt.radar.notes import load_sources
from cobalt.radar.pool import Action, decide
from cobalt.radar.runner import RadarRunner, StageDropped
from cobalt.radar.store import RadarStore
from cobalt.session.models import Session

from test_radar_runner import ActiveClock, Poller, Settings

ET = ZoneInfo("America/New_York")
#: 10:30 ET on a constructed trading day: the example screen is active.
INSTANT = datetime(2026, 9, 3, 14, 30, tzinfo=timezone.utc)
TODAY = INSTANT.astimezone(ET).date()
HEADER = ("Ticker", "Volume", "Relative Volume", "Asset Type", "Industry", "Price")
SRC = Path(cobalt.__file__).parent


def _row(ticker: str, price: str | None, *, rvol: str = "1") -> dict:
    """One export row of an ordinary stock; `price=None` leaves the
    `Price` key out (an export without the column)."""
    row = {"Ticker": ticker, "Volume": "2", "Relative Volume": rvol, "Asset Type": "", "Industry": "Capital Markets"}
    if price is not None:
        row["Price"] = price
    return row


class Collector:
    def __init__(self, screen=(), listed=(), *, list_fails: bool = False):
        self.screen_rows, self.list_rows, self.list_fails = list(screen), list(listed), list_fails

    async def screen(self, _block, now):
        return ScreenerSnapshot("screen-synthetic", now, tuple(self.screen_rows), HEADER)

    async def listed(self, _block, now):
        if self.list_fails:
            raise RuntimeError("synthetic list failure")
        return [ScreenerSnapshot("list-synthetic", now, tuple(self.list_rows), HEADER)]


class Radar:
    def __init__(self, open_rows=()):
        self.open_rows = [dict(row) for row in open_rows]
        self.transitions: list = []
        self.pools: list[dict] = []

    def pool_row(self, _key):
        return None

    def open_members(self, _key):
        return [dict(row) for row in self.open_rows]

    def apply_membership(self, **kwargs):
        self.transitions = kwargs["transitions"]
        kwargs["before_commit"]()

    def put_pool(self, row, **kwargs):
        self.pools.append(dict(row))
        kwargs["before_commit"]()

    def stamp_failure(self, *_args, **kwargs):
        kwargs["before_commit"]()

    def stamp_poll(self, *_args, **kwargs):
        kwargs["before_commit"]()


class Cards:
    """A recording card store: the two calls the floor stage may make."""

    def __init__(self, cards=(), *, fail: BaseException | None = None):
        self.cards, self.fail = list(cards), fail
        self.calls: list = []
        self.evidence: list[dict] = []

    def open_radar_cards(self):
        self.calls.append("open_radar_cards")
        return self.cards

    def transition(self, card_id, to_state, *, actor, evidence=None, reason=None, before_commit=None, **_kwargs):
        self.calls.append(("transition", card_id, to_state.value, actor.value, reason))
        self.evidence.append(evidence)
        if self.fail is not None:
            raise self.fail
        if before_commit:
            before_commit()
        return 1


def _card(card_id: int, ticker: str, state: str):
    return SimpleNamespace(card_id=card_id, ticker=ticker, state=state)


def _parsed():
    return load_sources(
        Path("tests/fixtures/radar/radar-screens.example.md"),
        Path("tests/fixtures/radar/radar-lists.example.md"),
        scan_interval=60, poll_interval=60, finviz_max_rpm=100, list_chunk_size=50, context_tickers=0,
    )


def _runner(collector, *, radar=None, config=None, card_store=None) -> RadarRunner:
    parsed = _parsed()
    events: list = []
    extra = {} if card_store is None else {"card_store": card_store}
    return RadarRunner(
        config=config or load_config(), sources_loader=lambda: parsed, collector=collector,
        radar_store=radar or Radar(), settings_store=Settings(events), poller=Poller(events),
        clock=ActiveClock(Session.RTH), now=lambda: INSTANT, **extra,
    )


def _collect(runner: RadarRunner, open_rows=()):
    return asyncio.run(runner._collect(runner.sources_loader(), INSTANT, [dict(r) for r in open_rows]))


def _decide(runner: RadarRunner, candidates, source_sets, open_rows=()):
    parsed = runner.sources_loader()
    return decide(
        candidates, [OpenMember(**row) for row in open_rows],
        [item.block for item in parsed.screens.blocks + parsed.lists.blocks],
        source_sets, INSTANT, handicap_headers=runner.config.export.handicap_headers,
    )


def _admitted(ticker: str, sources: list[str]) -> dict:
    return {"ticker": ticker, "sources": sources, "entered_at": INSTANT - timedelta(minutes=30),
            "below_cap_streak": 0, "last_rank": 1, "trade_date": TODAY, "rank_metric": None, "rank_value": None}


def _of(transitions, ticker: str) -> list[tuple]:
    return [(t.action, t.excluded_by.value if t.excluded_by else None) for t in transitions if t.ticker == ticker]


def _seen(source_sets) -> set[str]:
    return {t for s in source_sets for t in (*s.tickers, *s.metrics)}


# ---------------------------------------------------------------------
# F1 — the filter, once, after every source is gathered
# ---------------------------------------------------------------------


def test_a_row_at_or_below_the_floor_never_becomes_a_candidate():
    runner = _runner(Collector(
        screen=[_row("AAFA", "4.99"), _row("AAFB", "5.00"), _row("AAFC", "5.01")],
        listed=[_row("AAFD", "4.99")],
    ))
    candidates, source_sets = _collect(runner)
    assert {c.ticker for c in candidates} == {"AAFC"}
    assert not _seen(source_sets) & {"AAFA", "AAFB", "AAFD"}
    decision = _decide(runner, candidates, source_sets)
    assert {t.ticker for t in decision.transitions} == {"AAFC"}


def test_the_floor_is_read_from_the_config():
    config = load_config().model_copy(update={"price_floor": Decimal("10.00")})
    runner = _runner(Collector(screen=[_row("CFGA", "9.99"), _row("CFGB", "10.00"), _row("CFGC", "10.01")]),
                     config=config)
    candidates, source_sets = _collect(runner)
    assert {c.ticker for c in candidates} == {"CFGC"}
    assert not _seen(source_sets) & {"CFGA", "CFGB"}


def test_a_row_with_no_price_is_kept_and_flagged():
    lines: list[str] = []
    sink = logger.add(lambda message: lines.append(message.record["message"]), level="DEBUG")
    try:
        runner = _runner(Collector(
            screen=[_row("NOPA", ""), _row("NOPB", "-"), _row("NOPC", "n/a")],
            listed=[_row("NOPD", None)],
        ))
        for _ in range(2):  # two cycles of one ET day
            candidates, source_sets = _collect(runner)
    finally:
        logger.remove(sink)
    tickers = {"NOPA", "NOPB", "NOPC", "NOPD"}
    assert {c.ticker for c in candidates} == tickers
    metrics = {t: m for s in source_sets for t, m in s.metrics.items()}
    assert {t: metrics[t]["price"] for t in tickers} == dict.fromkeys(tickers)
    for ticker in tickers:
        flagged = [line for line in lines if line.startswith(f"radar price unknown: {ticker} ")]
        assert len(flagged) == 1, (ticker, lines)
        assert flagged[0].endswith("— kept")


def test_a_ticker_floored_by_one_source_is_removed_from_every_source():
    runner = _runner(Collector(screen=[_row("TWOS", "5.20"), _row("KEEP", "8.00")], listed=[_row("TWOS", "4.90")]))
    candidates, source_sets = _collect(runner)
    assert {c.ticker for c in candidates} == {"KEEP"}
    assert "TWOS" not in _seen(source_sets)
    assert runner._floored == {"TWOS": Decimal("4.90")}


def test_the_floor_boundaries_behave_as_before():
    """F4: the shipped config's 5.00 — equal is removed, a cent under is
    removed, a cent over is kept."""
    assert load_config().price_floor == Decimal("5.00")
    runner = _runner(Collector(screen=[_row("BNDA", "5.00"), _row("BNDB", "4.99"), _row("BNDC", "5.01")]))
    candidates, _sets = _collect(runner)
    assert {c.ticker for c in candidates} == {"BNDC"}


def test_no_floor_literal_in_the_radar():
    for path in (SRC / "radar" / "runner.py", SRC / "radar" / "config.py"):
        text = path.read_text(encoding="utf-8")
        for literal in ("5.00", "5.0", 'Decimal("5'):
            assert literal not in text, (path.name, literal)
    assert "self.config.price_floor" in (SRC / "radar" / "runner.py").read_text(encoding="utf-8")


def test_the_removal_is_logged_once_per_source():
    lines: list[str] = []
    sink = logger.add(lambda message: lines.append(message.record["message"]), level="DEBUG")
    try:
        _collect(_runner(Collector(screen=[_row("LOGA", "1.00"), _row("LOGB", "2.00")], listed=[_row("LOGC", "3.00")])))
    finally:
        logger.remove(sink)
    removed = [line for line in lines if line.startswith("radar price floor ")]
    assert len(removed) == 2, removed
    assert any("removed 2 (LOGA, LOGB)" in line and line.startswith("radar price floor 5") for line in removed)
    assert any("removed 1 (LOGC)" in line for line in removed)


# ---------------------------------------------------------------------
# F2 — an admitted member that crosses under departs at once
# ---------------------------------------------------------------------


def test_an_admitted_member_that_crosses_under_departs_with_price_floor():
    radar = Radar([_admitted("AAA", ["screen:example_session_scan@000000000000"])])
    runner = _runner(Collector(screen=[_row("AAA", "4.80"), _row("BBB", "6.00")]), radar=radar)
    asyncio.run(runner.cycle())
    assert _of(radar.transitions, "AAA") == [(Action.LEAVE, "price_floor")]


def test_a_floored_member_held_by_a_degraded_source_still_departs_once():
    radar = Radar([_admitted("AAA", ["list:index_heavyweights@000000000000"])])
    runner = _runner(Collector(screen=[_row("AAA", "4.80")], list_fails=True), radar=radar)
    result = asyncio.run(runner.cycle())
    assert _of(radar.transitions, "AAA") == [(Action.LEAVE, "price_floor")]
    assert result.decision.degraded
    assert not any(t.action is Action.HOLD for t in radar.transitions)


def test_a_never_admitted_episode_under_the_floor_closes_without_price_floor():
    never = {**_admitted("BBB", ["screen:example_session_scan@000000000000"]), "entered_at": None}
    radar = Radar([never])
    runner = _runner(Collector(screen=[_row("BBB", "4.80")]), radar=radar)
    asyncio.run(runner.cycle())
    assert _of(radar.transitions, "BBB") == [(Action.LEAVE, None)]


def test_a_member_back_above_the_floor_is_a_candidate_again():
    radar = Radar([_admitted("AAA", ["screen:example_session_scan@000000000000"])])
    collector = Collector(screen=[_row("AAA", "4.80")])
    runner = _runner(collector, radar=radar)
    asyncio.run(runner.cycle())
    assert _of(radar.transitions, "AAA") == [(Action.LEAVE, "price_floor")]
    radar.open_rows = []  # the LEAVE closed the episode
    collector.screen_rows = [_row("AAA", "5.01")]
    asyncio.run(runner.cycle())
    assert _of(radar.transitions, "AAA") == [(Action.ADMIT, None)]


def test_a_floored_fund_member_departs_as_price_floor_not_not_equity():
    radar = Radar([_admitted("FND", ["screen:example_session_scan@000000000000"])])
    fund = {**_row("FND", "3.00"), "Industry": "Exchange Traded Fund"}
    runner = _runner(Collector(screen=[fund]), radar=radar)
    asyncio.run(runner.cycle())
    assert _of(radar.transitions, "FND") == [(Action.LEAVE, "price_floor")]


# ---------------------------------------------------------------------
# F3 — WATCH -> EXPIRED; nothing else moves
# ---------------------------------------------------------------------


OPEN_CARDS = [
    _card(1, "AAA", "WATCH"), _card(2, "AAA", "ARMED"), _card(3, "AAA", "TRIGGERED"),
    _card(4, "AAA", "FILLED"), _card(5, "BBB", "WATCH"),
]


def test_a_watch_card_under_the_floor_expires():
    cards = Cards(OPEN_CARDS)
    runner = _runner(Collector(screen=[_row("AAA", "4.80"), _row("BBB", "6.00")]), card_store=cards)
    result = asyncio.run(runner.cycle())
    assert cards.calls == ["open_radar_cards", ("transition", 1, "EXPIRED", "cobalt", "price floor")]
    (evidence,) = cards.evidence
    assert evidence["via"] == "radar.price_floor"
    assert evidence["price"] == "4.80"
    assert Decimal(evidence["floor"]) == load_config().price_floor
    assert evidence["scan_id"] == result.scan_id
    assert result.state == "scanning" and result.failed_stage is None


def test_no_floored_ticker_reads_no_card():
    cards = Cards(OPEN_CARDS)
    runner = _runner(Collector(screen=[_row("AAA", "6.00")]), card_store=cards)
    asyncio.run(runner.cycle())
    assert cards.calls == []


def test_an_expiry_failure_is_stamped_evaluate_and_the_cycle_goes_on():
    radar = Radar()
    cards = Cards(OPEN_CARDS, fail=RuntimeError("synthetic card failure"))
    runner = _runner(Collector(screen=[_row("AAA", "4.80")]), radar=radar, card_store=cards)
    result = asyncio.run(runner.cycle())
    assert result.state == "scanning"
    assert result.failed_stage == "evaluate"
    assert result.detail.startswith("price floor expiry failed: ")
    assert radar.pools[-1]["failed_stage"] == "evaluate"
    assert radar.pools[-1]["failed_detail"].startswith("price floor expiry failed: ")


def test_an_illegal_transition_is_logged_not_raised():
    cards = Cards(OPEN_CARDS, fail=IllegalTransition(CardState.EXPIRED, CardState.EXPIRED, 1))
    runner = _runner(Collector(screen=[_row("AAA", "4.80")]), card_store=cards)
    result = asyncio.run(runner.cycle())
    assert result.state == "scanning" and result.failed_stage is None


def test_a_reset_crossing_at_the_expiry_drops_the_cycle():
    cards = Cards(OPEN_CARDS, fail=StageDropped("dropped at price_floor:card"))
    runner = _runner(Collector(screen=[_row("AAA", "4.80")]), card_store=cards)
    result = asyncio.run(runner.cycle())
    assert (result.state, result.failed_stage) == ("dropped", "membership")


def test_the_replay_runner_has_no_card_store():
    assert "card_store" not in inspect.getsource(runner_module._scan_replay)


def test_build_runner_hands_one_card_store_to_both_stages():
    source = inspect.getsource(runner_module.build_runner)
    assert source.count("CardStore()") == 1
    assert source.count("card_store=card_store") == 2


def test_open_radar_cards_reads_radar_origin_only():
    """The control for his manual sheet cards: the one read the stage
    makes never returns an `origin = 'manual'` card."""
    assert "WHERE origin = 'radar'" in inspect.getsource(CardStore.open_radar_cards)


# ---------------------------------------------------------------------
# F5 — hidden from the departed and excluded reads, kept for the DRC
# ---------------------------------------------------------------------


DRC_CALLERS = {
    "radar/store.py": 1,  # members_for_replay
    "replay/runner.py": 1,
    "radar/evaluate_cli.py": 2,
    "radar/audit_export.py": 1,
    "radar/handicap_dry_run.py": 1,
}


def test_every_drc_caller_asks_for_price_floor_rows():
    for rel, count in DRC_CALLERS.items():
        lines = [line for line in (SRC / rel).read_text(encoding="utf-8").splitlines() if ".members_for_day(" in line]
        assert len(lines) == count, (rel, lines)
        assert all("price_floor_rows=True" in line for line in lines), (rel, lines)
    (panel,) = [line for line in (SRC / "aset" / "radar_panel.py").read_text(encoding="utf-8").splitlines()
                if ".members_for_day(" in line]
    assert "price_floor_rows" not in panel


class _Conn:
    def __init__(self):
        self.statements: list[tuple[str, tuple]] = []

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def execute(self, sql, params=None):
        self.statements.append((sql, params))
        return SimpleNamespace(description=[], fetchall=lambda: [])


def test_members_for_day_filters_price_floor_rows_unless_asked():
    conn = _Conn()
    store = RadarStore(connect=lambda: conn)
    store.members_for_day("primary", TODAY)
    store.members_for_day("primary", TODAY, price_floor_rows=True)
    (hidden_sql, hidden_params), (all_sql, all_params) = conn.statements
    assert "excluded_by IS DISTINCT FROM 'price_floor'" in hidden_sql
    assert "price_floor" not in all_sql
    assert hidden_params == all_params == ("primary", TODAY)
