"""STALE SCORE S1 — no fresh `last` → no proximity → no score (v2 §2 C
steps 1–7; `[F-06]` `[F-08]` `[F-10]` `[F-13]` `[F-14]` `[F-16]`; owner
rulings R37 R38 R41 R44 of `cto-2026-09-22.md`).

Real shape (L45): the FTFT fixture bars / daily bars / card settings and
the repo's synthetic anatomy-only def (`radar_p2_support`). Every clock age
is driven OFF the passed `SCAN` — close-age = ttl + 1 (v2 X1) — and `SCAN`
is this module's own literal, never a value of the trader's (L32, L69).
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytest

import radar_p2_support as sup
from cobalt.aset.models import Grade
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import MemberInput, card_dots, evaluate_member, refresh_card
from cobalt.session import session_clock
from cobalt.settings.card import CardSettings
from test_radar_evaluate import ENABLED_CARD, SCAN0, World

UTC = timezone.utc
ET = ZoneInfo("America/New_York")
#: This module's own scan interval (seconds) — a construction, not his value.
SCAN = 100
TTL = 2 * SCAN
ENABLED = list(Grade)


def _bars_before(cut: datetime):
    return tuple(b for b in sup.fixture_bars("FTFT") if b.ts < cut)


def _member(as_of: datetime, bars, *, daily=True) -> MemberInput:
    return MemberInput(
        membership_id=100, ticker="FTFT", trade_date=sup.TRADE_DATE, as_of=as_of, bars=tuple(bars),
        daily=sup.fixture_daily("FTFT", as_of) if daily else None, daily_status="cache-hit" if daily else "absent",
        rvol=RvolObservation(ticker="FTFT", value=4.2, observed_at=as_of, source="screen:s", candidates=("screen:s",)),
        pool_position=1,
    )


def _evaluate(m: MemberInput, ld=None):
    return evaluate_member(ld or sup.loaded(), m, tunables=sup.engine_tunables(), defaults=sup.defaults(),
                           scan_interval=SCAN, clock=session_clock())


def _settings() -> CardSettings:
    return CardSettings.from_rows(sup.fixture_settings_rows(**ENABLED_CARD))


def _stale_as_of(bars) -> datetime:
    """close-age = ttl + 1 s (the last bar closes at `ts + 1 min`)."""
    return bars[-1].ts + timedelta(minutes=1) + timedelta(seconds=TTL + 1)


def _tapped_pre_c1_card(grade: int = 7):
    """The base world's first card, re-dotted as a card opened before C1:
    no `assumed_formation` dot, every dot tapped (v2 §1b)."""
    world = World()
    world.scan(SCAN0)
    card = world.cards.open_radar_cards()[0]
    fresh = _evaluate(_member(SCAN0, _bars_before(SCAN0)))
    dots = card_dots(sup.loaded(), fresh, _settings(), SCAN0, ())
    return card.model_copy(update={"dots": [d.model_copy(update={"trader_grade": grade, "tapped_at": SCAN0})
                                            for d in dots]})


def _close_hms(bar_ts: datetime) -> str:
    return (bar_ts + timedelta(minutes=1)).astimezone(ET).strftime("%H:%M:%S")


# ---------------------------------------------------------------------
# (iii) X1 · X5a — the RED-on-base experiments (v2 §7 "before S1")
# ---------------------------------------------------------------------


def test_x1_all_dots_tapped_on_stale_bars_scores_nothing_and_names_the_close():
    """X1: every dot tapped, bars stale by one second past the ttl → no
    proximity, no score, and the reason names that close time."""
    card = _tapped_pre_c1_card()
    kept = _bars_before(SCAN0)
    at = _stale_as_of(kept)
    ev = _evaluate(_member(at, kept))
    update = refresh_card(card, ev, sup.loaded(), _settings(), ENABLED, at=at, thresholds=None)
    assert update.card_score is None, f"card_score {update.card_score} published on stale bars"
    assert update.proximity is None
    assert update.score_suppressed == (
        f"bars stale — last close {_close_hms(kept[-1].ts)} ET, older than 2 × radar.scan_interval"
    )


def test_x5a_no_closed_bar_today_gives_no_proximity_not_the_maximum():
    """X5a: `last_bar` None → the base substitutes `card.entry` (proximity
    1, the maximum); after the fix proximity is NULL with the no-bar reason."""
    card = _tapped_pre_c1_card()
    at = SCAN0
    ev = _evaluate(_member(at, ()))
    update = refresh_card(card, ev, sup.loaded(), _settings(), ENABLED, at=at, thresholds=None)
    assert update.proximity is None, f"proximity {update.proximity} from no bar"
    assert update.card_score is None
    assert update.score_suppressed == "bars stale — no closed bar"


# ---------------------------------------------------------------------
# (i) the required field, on every return path ([F-10])
# ---------------------------------------------------------------------


def test_intraday_stale_is_required_and_set_on_every_return_path():
    from cobalt.radar.evaluate import MemberEvaluation
    from cobalt.taxonomy.tunables import TunableRow

    field = MemberEvaluation.model_fields.get("intraday_stale")
    assert field is not None and field.is_required() and field.annotation is bool
    kept = _bars_before(SCAN0)
    fresh, stale = _member(SCAN0, kept), _member(_stale_as_of(kept), kept)
    # not_evaluable (1): the registry refuses the def — returns before any bar is read
    refused_def = sup.loaded(sup.anatomy_def(preconditions=[{"expr": "Level_ref(free text here) == culminating"}]))
    # not_evaluable (2): a convention row names a rule the code does not implement
    rows = dict(sup.engine_tunables())
    key = "anatomy.orientation.extension"
    rows[key] = TunableRow.model_validate({**rows[key].model_dump(mode="json"), "value": "unimplemented_label"})
    convention = evaluate_member(sup.loaded(), fresh, tunables=rows, defaults=sup.defaults(), scan_interval=SCAN,
                                 clock=session_clock())
    daily_missing = _evaluate(_member(SCAN0, kept, daily=False), sup.loaded(sup.anatomy_def(
        avoid=[{"expr": "NOT Extension.instantiated"}, {"expr": "RangeBreak(HTF).day_count == 1"}])))
    cases = {
        "not_evaluable fresh": (_evaluate(fresh, refused_def), False),
        "not_evaluable stale": (_evaluate(stale, refused_def), True),
        "convention fresh": (convention, False),
        "intraday input_stale": (_evaluate(stale), True),
        "daily input_stale": (daily_missing, False),
        "formed": (_evaluate(fresh), False),
    }
    labels = {name: ev.evaluation for name, (ev, _) in cases.items()}
    assert labels == {"not_evaluable fresh": "not_evaluable", "not_evaluable stale": "not_evaluable",
                      "convention fresh": "not_evaluable", "intraday input_stale": "input_stale",
                      "daily input_stale": "input_stale", "formed": "formed"}
    assert {name: ev.intraday_stale for name, (ev, _) in cases.items()} == {
        name: want for name, (_, want) in cases.items()}


# ---------------------------------------------------------------------
# (ii) score_last — the ONE `last` rule ([F-13], [F-14])
# ---------------------------------------------------------------------


def test_score_last_is_none_iff_stale_and_raises_on_a_fresh_member_without_a_price():
    from cobalt.cards.scoring import score_last
    from cobalt.radar.evaluate import EvaluateError

    kept = _bars_before(SCAN0)
    fresh = _evaluate(_member(SCAN0, kept))
    stale = _evaluate(_member(_stale_as_of(kept), kept))
    assert score_last(fresh) == kept[-1].close and score_last(stale) is None
    assert stale.last_price == kept[-1].close  # the real last print is kept; only proximity drops
    broken = fresh.model_copy(update={"last_price": None})
    with pytest.raises(EvaluateError, match="no last price"):
        score_last(broken)


def test_every_score_card_caller_takes_its_last_from_score_last():
    """X18 as a test: no `score_card(` caller in `src/` passes a `last` that
    `score_last` did not return; the three price fallbacks are gone."""
    import re
    from pathlib import Path

    src = Path(__file__).resolve().parents[2] / "src"
    calls = []
    for path in sorted(src.rglob("*.py")):
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if re.search(r"\bscore_card\(", line) and not line.strip().startswith("def "):
                calls.append((path.name, n, line.strip()))
    assert len(calls) == 4, calls  # refresh_card, replay_receipt, the create call, audit_export
    assert all("last=score_last(" in line for _, _, line in calls), calls
    for path in (src / "cobalt" / "radar" / "evaluate.py", src / "cobalt" / "radar" / "audit_export.py"):
        text = path.read_text()
        assert "else card.entry" not in text and 'else Decimal(card["entry"])' not in text
        assert "else trigger" not in text


# ---------------------------------------------------------------------
# (iii) score_card(last=None) and the reason ([F-16], [F-06])
# ---------------------------------------------------------------------


def test_score_card_with_no_last_nulls_proximity_and_score_and_keeps_dot_reasons():
    from cobalt.cards import scoring

    kept = _bars_before(SCAN0)
    at = _stale_as_of(kept)
    ev = _evaluate(_member(at, kept))
    dots = card_dots(sup.loaded(), ev, _settings(), at, ())  # computed dots stale, untapped
    reason = scoring.stale_reason(ev)
    score = scoring.score_card(dots, last=None, stale_reason=reason, trigger=Decimal("5.50"), stop=Decimal("5.81"),
                               bands=_settings().proposed_key, enabled=ENABLED)
    assert score.proximity is None and score.card_score is None
    assert reason == f"bars stale — last close {_close_hms(kept[-1].ts)} ET, older than 2 × radar.scan_interval"
    assert score.score_suppressed == f"{reason}; {scoring.suppression(dots)}"
    assert scoring.PROXIMITY_UNKNOWN == "bars stale — no proximity"
    with pytest.raises(ValueError):
        scoring.score_card(dots, last=None, stale_reason=None, trigger=Decimal("5.50"), stop=Decimal("5.81"),
                           bands=None, enabled=ENABLED)
    with pytest.raises(ValueError):
        scoring.score_card(dots, last=kept[-1].close, stale_reason=reason, trigger=Decimal("5.50"),
                           stop=Decimal("5.81"), bands=None, enabled=ENABLED)


# ---------------------------------------------------------------------
# (iv) Optional proximity, JSON null (X12)
# ---------------------------------------------------------------------


def test_null_proximity_publishes_json_null_never_the_string_none():
    import json

    from cobalt.cards.scoring import CardScore
    from cobalt.radar.evaluate import CardUpdate, published_numbers

    assert CardScore.model_fields["proximity"].annotation == (Decimal | None)
    update = CardUpdate(card_id=1, proximity=None, conviction=None, card_score=None, score_suppressed="s",
                        proposed_key=None, dots=[], health=None, radar_score_id=None)
    payload = published_numbers(update)
    assert payload["proximity"] is None and payload["card_score"] is None
    assert '"None"' not in json.dumps(payload)


# ---------------------------------------------------------------------
# (v) htf_level_proximity carries the stale flag (X6) · (vi) daily-missing (X14)
# ---------------------------------------------------------------------


def test_htf_level_proximity_on_stale_bars_is_input_stale_with_no_engine_grade():
    kept = _bars_before(SCAN0)
    at = _stale_as_of(kept)
    ev = _evaluate(_member(at, kept))
    assert ev.last_price is not None
    obs = ev.observations["htf_level_proximity"]
    dot = {d.factor: d for d in card_dots(sup.loaded(), ev, _settings(), at, ())}["htf_level_proximity"]
    assert obs.stale is True and dot.na_reason == "input_stale" and dot.engine_grade is None
    fresh = _evaluate(_member(SCAN0, kept))
    fresh_dot = {d.factor: d for d in card_dots(sup.loaded(), fresh, _settings(), SCAN0, ())}["htf_level_proximity"]
    assert fresh.observations["htf_level_proximity"].stale is False and fresh_dot.engine_grade is not None


def test_daily_missing_input_stale_with_a_fresh_close_keeps_proximity():
    ld = sup.loaded(sup.anatomy_def(avoid=[{"expr": "NOT Extension.instantiated"},
                                           {"expr": "RangeBreak(HTF).day_count == 1"}]))
    kept = _bars_before(SCAN0)
    ev = _evaluate(_member(SCAN0, kept, daily=False), ld)
    assert ev.evaluation == "input_stale" and ev.intraday_stale is False
    update = refresh_card(_tapped_pre_c1_card(), ev, ld, _settings(), ENABLED, at=SCAN0, thresholds=None)
    assert update.proximity is not None and update.card_score is not None


# ---------------------------------------------------------------------
# (vii) ONE new version string ([F-08], X19, X20)
# ---------------------------------------------------------------------


def test_one_new_version_string_and_the_previous_is_not_supported():
    from cobalt.radar.evaluate import DESK_FORMULA_VERSION, EVALUATOR_VERSION
    from cobalt.replay.formations import SUPPORTED_EVALUATORS

    previous = {"s2p2.1", "s2p2.2"}  # the base's two strings (PREFLIGHT, evaluate.py:160-161)
    assert EVALUATOR_VERSION == DESK_FORMULA_VERSION and EVALUATOR_VERSION.startswith("s2p2.")
    assert EVALUATOR_VERSION not in previous
    assert SUPPORTED_EVALUATORS == frozenset({EVALUATOR_VERSION})


# ---------------------------------------------------------------------
# (viii) the audit-export version gate ([F-08]) · (ix) X11
# ---------------------------------------------------------------------


def _world_with_two_runs():
    world = World()
    world.scan(SCAN0)
    world.scan(SCAN0 + timedelta(seconds=SCAN))
    return world


@pytest.mark.parametrize("written", [None, "s2p2.2"])
def test_audit_export_refuses_another_version_by_name_before_the_replay(tmp_path, monkeypatch, written):
    from cobalt.radar import audit_export as ax
    from test_radar_audit_export import GENERATED, RunStores

    world = _world_with_two_runs()
    for receipt in world.cards.receipts:
        if written is None:
            receipt["observations"].pop("evaluator_version")
        else:
            receipt["observations"]["evaluator_version"] = written

    def never(*_a, **_k):
        raise AssertionError("replay_receipt reached — the version gate must refuse first")

    monkeypatch.setattr(ax, "replay_receipt", never)
    stores = RunStores(world)
    with pytest.raises(ax.AuditExportError) as refused:
        ax.export_run(2, radar_store=stores, card_store=stores, out=tmp_path / "b", clock=session_clock(),
                      generated_at=GENERATED)
    message = str(refused.value)
    assert "evaluator version" in message and repr(written) in message
    assert "replay disagrees" not in message and "own replay failed" not in message


def test_audit_export_same_version_run_still_exports(tmp_path):
    from cobalt.radar import audit_export as ax
    from test_radar_audit_export import GENERATED, RunStores

    stores = RunStores(_world_with_two_runs())
    manifest = ax.export_run(2, radar_store=stores, card_store=stores, out=tmp_path / "b", clock=session_clock(),
                             generated_at=GENERATED)
    assert manifest.self_check["all_equal"] is True


def test_audit_replay_path_never_emits_proximity_one_for_a_member_without_a_price(tmp_path, monkeypatch):
    """X11: the `--replay` scorer no longer substitutes `trigger`; a fresh
    formed member without a last price is a loud error (L1)."""
    from cobalt.radar import audit_export as ax
    from cobalt.radar.evaluate import EvaluateError
    from test_radar_audit_export import GENERATED
    from test_radar_evaluate_cli import ReadOnlyRadar, _daily

    real = ax.evaluate_member
    monkeypatch.setattr(ax, "evaluate_member",
                        lambda *a, **k: real(*a, **k).model_copy(update={"last_price": None}))
    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    with pytest.raises(EvaluateError):
        ax.export_replay(
            sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
            defs_source=lambda: ([sup.loaded()], {}), daily_source=_daily, tunables=sup.engine_tunables(),
            defaults=sup.defaults(), settings_values=sup.fixture_settings_rows(**{"radar.cards_enabled": False}),
            clock=session_clock(), out=tmp_path / "b", generated_at=GENERATED,
        )
    assert not (tmp_path / "b").exists()


# ---------------------------------------------------------------------
# (x) R37 + R41 — the ladder (existing rule, pinned)
# ---------------------------------------------------------------------


def test_r37_r41_a_null_watch_card_sinks_below_every_scored_one_and_nulls_order_by_pool_position():
    """GREEN-as-pin: `ladder_order` is untouched (R37, R41); this turns red
    if the WATCH key stops putting NULL scores last, or ties among NULLs stop
    falling to `pool_position`."""
    from cobalt.cards.models import CardState
    from cobalt.cards.radar import LadderEntry, ladder_order

    def entry(card_id, score, pool):
        return LadderEntry(card_id=card_id, state=CardState.WATCH, card_score=score, pool_position=pool,
                           ticker=f"T{card_id}", state_at=SCAN0)

    order = ladder_order([entry(1, None, 2), entry(2, 12, 9), entry(3, None, 1), entry(4, 70, 5)])
    assert [p.card_id for p in order.active] == [4, 2, 3, 1]
    assert [p.rank_chip for p in order.active] == [1, 2, 3, 4]


# ---------------------------------------------------------------------
# (xi) R38 — premarket, the evaluator's every-session clock
# ---------------------------------------------------------------------


def test_r38_premarket_stale_bar_nulls_and_the_next_bar_lifts_it_with_no_tap():
    """The store held no newer bar at the first premarket scan (a poll gap);
    by the next scan the bars have landed. No session gate: the freshness
    helper `intraday_staleness` takes no session and no clock."""
    card = _tapped_pre_c1_card()
    premarket = [b for b in sup.fixture_bars("FTFT") if b.ts.astimezone(ET).hour < 9]
    kept = premarket[:10]
    at = _stale_as_of(kept)
    lifted_at = at + timedelta(seconds=SCAN)
    assert lifted_at.astimezone(ET).hour < 9  # both scans before 09:30 ET
    ev = _evaluate(_member(at, kept))
    stale = refresh_card(card, ev, sup.loaded(), _settings(), ENABLED, at=at, thresholds=None)
    assert ev.intraday_stale is True and stale.proximity is None and stale.card_score is None
    ev2 = _evaluate(_member(lifted_at, premarket))
    lifted = refresh_card(card, ev2, sup.loaded(), _settings(), ENABLED, at=lifted_at, thresholds=None)
    assert ev2.intraday_stale is False and lifted.proximity is not None and lifted.card_score is not None
    assert lifted.conviction == stale.conviction  # the same taps: nothing was tapped in between


# ---------------------------------------------------------------------
# (xii) X27 — stage text = replay text, byte for byte
# ---------------------------------------------------------------------


def test_stale_card_stage_and_replay_reason_are_byte_identical():
    from cobalt.radar.evaluate import replay_receipt

    world = World()
    world.scan(SCAN0)
    kept = _bars_before(SCAN0)
    world.radar.bars["FTFT"] = list(kept)
    world.scan(_stale_as_of(kept))
    card = world.cards.cards[1]
    _, replayed = replay_receipt(list(world.cards.receipts), clock=session_clock())
    assert card["proximity"] is None and card["card_score"] is None
    assert card["score_suppressed"].startswith(f"bars stale — last close {_close_hms(kept[-1].ts)} ET")
    assert replayed[0].recomputed["score_suppressed"].encode() == card["score_suppressed"].encode()
    assert replayed[0].recomputed == replayed[0].published
