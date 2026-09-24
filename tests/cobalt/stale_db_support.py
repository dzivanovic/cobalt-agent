"""Shared `cobalt_dev` construction for the stale-score S2 tests
(`test_stale_score_db.py`) and the STEP-3 experiments (v2 §7 "before S2").
Not a test module.

Real shape (L45): the FTFT fixture bars under a synthetic ticker, the
repo's one synthetic anatomy-only def, the hub-cut card settings. Every row
is written inside the suite's rolled-back `cobalt_dev` transaction
(`conftest.dev_db_tx`) — nothing is committed. The bars are FED by the test
(`feed(cut)`), so a scan with no newer bar is stale by construction. `SCAN`
is this module's own scan interval, handed to the stage as a constructed
tunables row; every clock age is driven off it (close-age = ttl + 1, v2
X1). No value of the trader's is read or asserted (L32, L69).
"""

from __future__ import annotations

import asyncio
import inspect
import os
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

import radar_p2_support as sup

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def s2_built() -> bool:
    """True once STEP-4's `tap_dot` branch exists: the experiments the S2
    writers flip assert the S1-only behaviour before it and the S2 behaviour
    after it, so a re-run on the tip proves the flip instead of going red."""
    from cobalt.cards.store import CardStore

    return "PROXIMITY_UNKNOWN" in inspect.getsource(CardStore.tap_dot)

UTC = timezone.utc
SCAN0 = datetime(2026, 1, 6, 16, 30, tzinfo=UTC)
#: This module's own scan interval (seconds) — a construction, not his value.
SCAN = 100
TTL = 2 * SCAN
ENABLED = {
    "radar.cards_enabled": True,
    "card.proposed_key": {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4},
    "card.curves": {"atrs_from_open": [[1, 2], [6, 9]], "rvol": [[1, 1], [3, 6], [10, 10]],
                    "Extension.leg_count": [[2, 3], [20, 9]], "htf_level_proximity": [[0, 9], [2, 2]]},
}
HTF = "htf_level_proximity"


def tunables() -> dict:
    """The engine tunables with `radar.scan_interval` set to this module's `SCAN`."""
    from cobalt.taxonomy.tunables import TunableRow

    rows = dict(sup.engine_tunables())
    row = rows["radar.scan_interval"]
    rows["radar.scan_interval"] = TunableRow.model_validate({**row.model_dump(mode="json"), "value": SCAN})
    return rows


def bars_before(cut: datetime) -> list:
    return [b for b in sup.fixture_bars("FTFT") if b.ts < cut]


def stale_as_of(bars) -> datetime:
    """close-age = ttl + 1 s: the last bar closes at `ts + 1 min`."""
    return bars[-1].ts + timedelta(minutes=1) + timedelta(seconds=TTL + 1)


def bands():
    from cobalt.settings.card import CardSettings

    return CardSettings.from_rows(ENABLED).proposed_key


def enabled():
    from cobalt.aset.models import Grade

    return [Grade.A, Grade.B, Grade.C]


class DevWorld:
    """One pool, one member, the S5 stage on the real `cobalt_dev` stores."""

    def __init__(self, *, ticker: str, pool: str, defs=None, daily_fails: bool = False):
        from cobalt.archiver.store import BarStore
        from cobalt.cards.store import CardStore
        from cobalt.radar.evaluate import EvaluateStage
        from cobalt.radar.store import RadarStore
        from cobalt.session import session_clock
        from cobalt.settings.store import TraderSettingsStore

        self.ticker, self.pool = ticker, pool
        self.radar, self.cards = RadarStore("cobalt_dev"), CardStore("cobalt_dev")
        self.settings, self.bar_store = TraderSettingsStore("cobalt_dev"), BarStore("cobalt_dev")
        self.cards.ensure_schema()
        with self.radar._connect() as conn:
            conn.execute(
                "INSERT INTO radar_pool (pool_key, state, session, members) VALUES (%s, 'scanning', 'rth', 1) "
                "ON CONFLICT DO NOTHING", (pool,),
            )
            self.member_id = conn.execute(
                "INSERT INTO radar_membership (pool_key, ticker, trade_date, first_seen_at, entered_at, source, "
                "sources, rank_at_entry, last_rank, session, opened_scan_id, last_scan_id) VALUES "
                "(%s, %s, %s, %s, %s, 'screen', '[]', 1, 1, 'rth', -77, -77) RETURNING id",
                (pool, ticker, sup.TRADE_DATE, SCAN0 - timedelta(hours=2), SCAN0 - timedelta(hours=2)),
            ).fetchone()[0]
        rows = sup.fixture_settings_rows(**ENABLED)
        rows["aset.account_mode"] = "sim"
        self.settings.put(rows, source="test")
        self.defs = defs or [sup.loaded()]
        self.daily_fails = daily_fails

        async def daily(t, now):
            if self.daily_fails:
                raise FileNotFoundError(f"no cached daily bars for {t}")
            return sup.fixture_daily("FTFT", now).model_copy(update={"ticker": t})

        self.stage = EvaluateStage(
            radar_store=self.radar, card_store=self.cards, defs_source=lambda: (self.defs, {}),
            settings_values=self.settings.values, daily_source=daily, tunables_loader=tunables,
            defaults_loader=sup.defaults, clock=session_clock(), now=lambda: SCAN0,
            members_at=lambda _pool, _at: self.radar.admitted_members(pool),
        )

    def feed(self, cut: datetime) -> None:
        """Store the FTFT fixture bars that opened before `cut`, under this ticker."""
        self.bar_store.upsert_bars([b.model_copy(update={"ticker": self.ticker}) for b in bars_before(cut)])

    def scan(self, at: datetime):
        from cobalt.radar.anatomy.freshness import RvolObservation

        self.stage.now = lambda: at
        return asyncio.run(self.stage.run(
            pool_key=self.pool, scan_id=int(at.timestamp() * 1000), session="RTH", instant=at,
            rvol={self.ticker: RvolObservation(ticker=self.ticker, value=4.2, observed_at=at, source="screen:s",
                                               candidates=("screen:s",))},
            pool_unit={"pool_block": None}, gate=lambda _label: (lambda: None),
        ))

    def row(self, card_id: int) -> dict:
        with self.cards._connect() as conn:
            r = conn.execute(
                "SELECT proximity, conviction, card_score, score_suppressed, last_price, proposed_key "
                "FROM aset_sizings WHERE id = %s", (card_id,),
            ).fetchone()
        return dict(zip(("proximity", "conviction", "card_score", "score_suppressed", "last_price",
                         "proposed_key"), r))

    def as_pre_c1(self, card_id: int) -> None:
        """A card opened BEFORE C1 (v2 §1b): no `assumed_formation` dot."""
        with self.cards._connect() as conn:
            conn.execute("DELETE FROM card_dots WHERE card_id = %s AND factor = 'assumed_formation'", (card_id,))

    def dots(self, card_id: int) -> list[str]:
        with self.cards._connect() as conn:
            return [r[0] for r in conn.execute(
                "SELECT factor FROM card_dots WHERE card_id = %s ORDER BY position", (card_id,)).fetchall()]

    def engine_grade(self, card_id: int, factor: str):
        with self.cards._connect() as conn:
            return conn.execute("SELECT engine_grade FROM card_dots WHERE card_id = %s AND factor = %s",
                                (card_id, factor)).fetchone()[0]

    def tap(self, card_id: int, factor: str, grade: int, at: datetime) -> dict:
        return self.cards.tap_dot(card_id, factor, grade, bands=bands(), enabled=enabled(), now=at)

    def tap_all(self, card_id: int, grade: int, at: datetime) -> None:
        for factor in self.dots(card_id):
            self.tap(card_id, factor, grade, at)

    def open_card(self, card_id: int):
        return next(c for c in self.cards.open_radar_cards() if c.card_id == card_id)

    def formed_card(self) -> int:
        """Feed the bars before SCAN0, scan at SCAN0 (fresh) → the one created card."""
        self.feed(SCAN0)
        outcome = self.scan(SCAN0)
        assert outcome.created, outcome.refusals
        return outcome.created[0]


def scored_pre_c1_card(world: DevWorld, grade: int = 7) -> int:
    """A formed, pre-C1 card with every dot tapped: a live, non-null score."""
    card_id = world.formed_card()
    world.as_pre_c1(card_id)
    world.tap_all(card_id, grade, SCAN0 + timedelta(seconds=10))
    return card_id


def evaluation(at: datetime, bars):
    """The pure evaluator on the FTFT fixture at `at` (the stage's own read,
    for the race tests that must interleave a tap between read and write)."""
    from cobalt.radar.anatomy.freshness import RvolObservation
    from cobalt.radar.evaluate import MemberInput, evaluate_member
    from cobalt.session import session_clock

    member = MemberInput(
        membership_id=100, ticker="FTFT", trade_date=sup.TRADE_DATE, as_of=at, bars=tuple(bars),
        daily=sup.fixture_daily("FTFT", at), daily_status="cache-hit",
        rvol=RvolObservation(ticker="FTFT", value=4.2, observed_at=at, source="screen:s", candidates=("screen:s",)),
        pool_position=1,
    )
    return evaluate_member(sup.loaded(), member, tunables=tunables(), defaults=sup.defaults(),
                           scan_interval=SCAN, clock=session_clock())


def update_for(world: DevWorld, card_id: int, at: datetime, bars):
    """What the stage computes for the card at `at` (its read), not yet written."""
    from cobalt.radar.evaluate import refresh_card
    from cobalt.settings.card import CardSettings

    card = world.open_card(card_id)
    update = refresh_card(card, evaluation(at, bars), sup.loaded(), CardSettings.from_rows(ENABLED), enabled(),
                          at=at, thresholds=None)
    with world.cards._connect() as conn:  # the stage stamps the seam row id the same way (evaluate.py:1859)
        score_id = conn.execute("SELECT radar_score_id FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()[0]
    return update.model_copy(update={"radar_score_id": score_id})


__all__ = ["DevWorld", "Decimal", "ENABLED", "HTF", "SCAN", "SCAN0", "TTL", "bars_before", "evaluation",
           "requires_db", "s2_built", "scored_pre_c1_card", "stale_as_of", "tunables", "update_for"]
