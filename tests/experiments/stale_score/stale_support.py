"""Shared construction for the stale-score experiments (not a test module).

Real shape (L45): the FTFT bars, daily bars and card settings are the
hub-cut fixtures under `tests/fixtures/radar/`; the def is the repo's one
synthetic anatomy-only def (`radar_p2_support.anatomy_def`). Every clock
age is driven OFF the passed `SCAN` (close-age = ttl + 1, v2 X1) — `SCAN`
is this module's own literal, never a value of the trader's (L32, L69).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import radar_p2_support as sup
from cobalt.aset.models import Grade
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import MemberInput, card_dots, evaluate_member
from cobalt.session import session_clock
from cobalt.settings.card import CardSettings

UTC = timezone.utc
ET = ZoneInfo("America/New_York")
#: This module's own scan interval (seconds) — a construction, not his value.
SCAN = 100
TTL = 2 * SCAN
#: The base world's first card-forming scan (`test_radar_evaluate.SCAN0`).
SCAN0 = datetime(2026, 1, 6, 16, 30, tzinfo=UTC)


def bars_before(cut: datetime):
    """The FTFT fixture bars that opened before `cut`."""
    return tuple(b for b in sup.fixture_bars("FTFT") if b.ts < cut)


def member(as_of: datetime, bars, *, daily=True, rvol=True) -> MemberInput:
    return MemberInput(
        membership_id=100, ticker="FTFT", trade_date=sup.TRADE_DATE, as_of=as_of, bars=tuple(bars),
        daily=sup.fixture_daily("FTFT", as_of) if daily else None, daily_status="cache-hit" if daily else "absent",
        rvol=RvolObservation(ticker="FTFT", value=4.2, observed_at=as_of, source="screen:s",
                             candidates=("screen:s",)) if rvol else None,
        pool_position=1,
    )


def stale_as_of(bars) -> datetime:
    """close-age = ttl + 1 s: the last bar closes at `ts + 1 min`."""
    return bars[-1].ts + timedelta(minutes=1) + timedelta(seconds=TTL + 1)


def evaluate(m: MemberInput, ld=None):
    return evaluate_member(ld or sup.loaded(), m, tunables=sup.engine_tunables(), defaults=sup.defaults(),
                           scan_interval=SCAN, clock=session_clock())


def settings(**card) -> CardSettings:
    from test_radar_evaluate import ENABLED_CARD

    return CardSettings.from_rows(sup.fixture_settings_rows(**(card or ENABLED_CARD)))


ENABLED = list(Grade)

#: True once STEP-2's helper exists: the experiments the fix flips assert
#: the base's behaviour before it and the fixed behaviour after it, so the
#: CLOSE re-run on the tip proves the flip rather than going red on it.
FIXED = hasattr(__import__("cobalt.cards.scoring", fromlist=["x"]), "score_last")


def tapped_pre_c1_card(grade: int = 7):
    """The base world's first card (formed at SCAN0), re-dotted as a card
    opened BEFORE C1: no `assumed_formation` dot, every dot tapped `grade`
    (v2 §1b: the live defect on such cards)."""
    from test_radar_evaluate import World

    world = World()
    world.scan(SCAN0)
    card = world.cards.open_radar_cards()[0]
    fresh = evaluate(member(SCAN0, bars_before(SCAN0)))
    dots = card_dots(sup.loaded(), fresh, settings(), SCAN0, ())
    tapped = [d.model_copy(update={"trader_grade": grade, "tapped_at": SCAN0}) for d in dots]
    return card.model_copy(update={"dots": tapped})
