"""S2-P2 STEP-8 — the `/radar` ladder wired to `"user".radar_cards_v`.

REAL SHAPE, NOT INVENTED (L45). The card rows here are not a fixture file:
they are what the S5 evaluate stage writes when it runs over the hub-cut
bars fixture (`bars-rubberband.real-shape.json`) with the hub-cut settings
fixture — the same rows `panel-cards.real-shape.json` will hold once the
hub cuts it from the dev replay (plan §3) — projected onto the view's
columns. States beyond WATCH are reached by the transitions the card
store allows (a sized key tap, then ARMED / TRIGGERED / FILLED), and the
FILLED card's health pills come from a real refresh scan.
"""

from __future__ import annotations

import asyncio
import copy
import hashlib
import html
import json
import re
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

import radar_p2_support as sup
import test_radar_panel as pool_tests
from cobalt.aset import radar_panel as panel
from cobalt.aset import web as web_module
from cobalt.aset.engine import size_at_key
from cobalt.aset.models import Direction, Grade
from cobalt.cards.models import CardState
from cobalt.cards.radar import FIELD_OWNERS
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import EvaluateStage
from cobalt.session import session_clock
from cobalt.settings.models import TraderSettings

UTC = timezone.utc
SCAN0 = datetime(2026, 1, 6, 16, 30, tzinfo=UTC)
ENABLED = {
    "radar.cards_enabled": True,
    "card.proposed_key": {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4},
    "card.curves": {
        "atrs_from_open": [[1, 2], [6, 9]],
        "rvol": [[1, 1], [3, 6], [10, 10]],
        "Extension.leg_count": [[2, 3], [20, 9]],
        "htf_level_proximity": [[0, 9], [2, 2]],
    },
}
SETTINGS_ROWS = sup.fixture_settings_rows(**ENABLED)
TRADER = TraderSettings._build(SETTINGS_ROWS, where="fixture")


# ---------------------------------------------------------------------
# rows from the real evaluator
# ---------------------------------------------------------------------


def _stage(radar, cards, instant):
    async def daily(ticker, now):
        return sup.fixture_daily(ticker, now)

    return EvaluateStage(
        radar_store=radar, card_store=cards, defs_source=lambda: ([sup.loaded()], {}),
        settings_values=lambda: dict(SETTINGS_ROWS), daily_source=daily,
        tunables_loader=sup.engine_tunables, defaults_loader=sup.defaults, clock=session_clock(),
        now=lambda: instant[0],
    )


def _scan(stage, radar, instant, at):
    instant[0] = at
    rvol = {m["ticker"]: RvolObservation(ticker=m["ticker"], value=4.2, observed_at=at, source="screen:s",
                                         candidates=("screen:s",)) for m in radar.members}
    return asyncio.run(stage.run(pool_key="pool", scan_id=int(at.timestamp() * 1000), session="RTH",
                                 instant=at, rvol=rvol, pool_unit={"pool_block": {"cap": 50}}, gate=sup.Gate()))


def _view_row(card: dict, radar, *, run_id: int, state_at: datetime) -> dict:
    """One `"user".radar_cards_v` row (its exact columns) plus the card's dots."""
    member = next(m for m in radar.members if m["id"] == card["pool_member_id"])
    score = radar.scores[card["radar_score_id"]]
    row = {
        "card_id": card["id"], "user_id": 1, "created_at": SCAN0, "ticker": card["ticker"],
        "direction": card["direction"], "state": card["state"], "state_at": state_at, "session": card["session"],
        "account_mode": "live", "pool_member_id": card["pool_member_id"], "trade_def_slug": card["trade_def_slug"],
        "trade_def_md5": card["trade_def_md5"], "setup_ref": card["setup_ref"], "trigger_type": card["trigger_type"],
        "trigger_price": card["trigger_price"], "stop_ref": card["stop_ref"], "structural_stop": card["structural_stop"],
        "entry": card["entry"], "stop": card["stop"], "formed_at": card["formed_at"], "expires_at": card["expires_at"],
        "why": card["why"], "proposed_key": card.get("proposed_key"), "tapped_grade": card.get("tapped_grade"),
        "sized_grade": card.get("sized_grade"), "snap_notice": card.get("snap_notice"), "grade": card["grade"],
        "risk_budget": card["risk_budget"], "shares": card["shares"], "used_risk": card["used_risk"],
        "conviction": card.get("conviction"), "proximity": card["proximity"], "card_score": card.get("card_score"),
        "score_suppressed": card.get("score_suppressed"), "radar_score_id": card["radar_score_id"],
        "scan_id": card["scan_id"], "formula_sha256": card["formula_sha256"],
        "tunables_sha256": card["tunables_sha256"], "settings_sha256": card["settings_sha256"],
        "health": card.get("health"), "promoted_at": card.get("promoted_at"),
        "board_score_id": score["id"], "board_run_id": run_id, "board_evaluation": score["evaluation"],
        "board_started_at": radar.runs[run_id]["started_at"], "outside_pool": member.get("left_at") is not None,
        "last_price": Decimal("5.48"), "pool_position": member["last_rank"],
    }
    assert set(row) == set(FIELD_OWNERS), sorted(set(row) ^ set(FIELD_OWNERS))
    return {**row, "dots": list(card["dots"])}


def _sized(card: dict, tapped: Grade) -> dict:
    sizing = size_at_key(
        tapped, ticker=card["ticker"], entry=card["entry"], stop=card["stop"], direction=Direction(card["direction"]),
        sheet_modes=TRADER.sheet_modes, sheet=TRADER.daymode.sheet_for("reduced"),
        enabled=TRADER.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("50"),
    )
    return {**card, "tapped_grade": sizing.tapped_grade.value, "sized_grade": sizing.sized_grade.value,
            "grade": sizing.sized_grade.value, "risk_budget": sizing.result.risk_budget,
            "shares": sizing.result.shares, "used_risk": sizing.result.used_risk, "snap_notice": sizing.snap_notice}


@pytest.fixture(scope="module")
def evaluated():
    """Every state the ladder renders, each from the evaluator's own card."""
    radar = sup.FakeRadarStore(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    cards = sup.FakeCardStore()
    instant = [SCAN0]
    stage = _stage(radar, cards, instant)
    _scan(stage, radar, instant, SCAN0)
    base = copy.deepcopy(cards.cards[1])
    # FILLED: the next scan sees the card filled and writes its health pills.
    cards.cards[1] = _sized(cards.cards[1], Grade.A_PLUS) | {"state": "FILLED"}
    _scan(stage, radar, instant, SCAN0 + timedelta(seconds=100))
    filled = copy.deepcopy(cards.cards[1])
    assert filled["health"] and filled["health"]["pills"]
    run_id = max(radar.runs)
    rows = []
    variants = [
        (1, base, "WATCH"),
        (2, _sized(base, Grade.A_PLUS), "ARMED"),
        (3, _sized(base, Grade.A), "TRIGGERED"),
        (4, filled, "FILLED"),
        (5, base, "PASSED"),
        (6, base, "EXPIRED"),
    ]
    for card_id, card, state in variants:
        row = _view_row({**card, "id": card_id, "state": state}, radar, run_id=run_id, state_at=SCAN0)
        rows.append(row)
    return {"rows": rows, "base": base, "radar": radar}


class RowStore:
    def __init__(self, rows=None, error=None):
        self.rows = rows or []
        self.error = error
        self.days = []

    def radar_board_cards(self, trade_date):
        self.days.append(trade_date)
        if self.error:
            raise self.error
        return copy.deepcopy(self.rows)


class Settings:
    def __init__(self, values):
        self._values = values

    def values(self):
        return copy.deepcopy(self._values)


def _tunables():
    rows = sup.engine_tunables()
    return lambda: SimpleNamespace(by_key=rows)


#: S3 C3: the FILLED card's position, constructed (L32) — the IN-TRADE block
#: reads it through `position_reader`, so the ladder (and its pin) never
#: depends on what a database holds.
POSITION = panel.InTradeView(
    running=100, basis="legs", realized_value=None, realized_provisional=True,
    realized_reason="not computed — zero risk unit", stop_owner="cobalt",
    distance_change_pct=None, drift_warning_pct=None, drift_warned=None,
    legs=[panel.LegView(id=1, seq=0, kind="entry", shares=100, price=Decimal("5.48"), flag="estimated",
                        price_source="last_poll", at=SCAN0, stop_in_force=Decimal("5.81"), preset=None,
                        held_stated=None)],
)


def _ladder(rows, *, rung="reduced", now=SCAN0 + timedelta(seconds=200)):
    return panel.build_ladder_view(
        card_store=RowStore(rows), settings_store=Settings(SETTINGS_ROWS), clock=session_clock(), now=now,
        tunables_loader=_tunables(), rung_source=lambda instant, cfg: rung,
        position_reader=lambda card_id: POSITION,
    )


# ---------------------------------------------------------------------
# the adapter: radar_cards_v rows, never a contract fixture
# ---------------------------------------------------------------------


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_ladder_reads_radar_cards_v_rows_and_the_contract_adapter_is_gone(evaluated):
    assert not hasattr(panel.CardView, "from_contract")
    store = RowStore(evaluated["rows"])
    view = panel.build_ladder_view(
        card_store=store, settings_store=Settings(SETTINGS_ROWS), clock=session_clock(),
        now=SCAN0 + timedelta(seconds=200), tunables_loader=_tunables(), rung_source=lambda i, c: "reduced",
    )
    assert store.days == [session_clock().to_et(SCAN0).date()]
    assert [c.state for c in view.active] == [CardState.ARMED, CardState.TRIGGERED, CardState.FILLED, CardState.WATCH]
    assert {c.state for c in view.terminal} == {CardState.PASSED, CardState.EXPIRED}
    assert view.empty_message is None


def test_empty_ladder_is_explicit_and_needs_no_rung():
    view = panel.build_ladder_view(
        card_store=RowStore([]), settings_store=Settings({}), clock=session_clock(), now=SCAN0,
        tunables_loader=_tunables(), rung_source=lambda i, c: (_ for _ in ()).throw(AssertionError("rung read")),
    )
    assert view.active == [] and view.terminal == [] and view.empty_message == "No radar cards today"


def test_radar_today_shape_renders_five_watch_and_fourteen_expired(evaluated):
    """R685 CONTROL: the 10-08 survey's shape (5 WATCH + 14 EXPIRED, one ET day) reaches the page."""
    watch, expired = evaluated["rows"][0], evaluated["rows"][5]
    assert watch["state"] == "WATCH" and expired["state"] == "EXPIRED"
    rows = []
    for template, count in ((watch, 5), (expired, 14)):
        for _ in range(count):
            n = len(rows) + 1
            # 13:40Z .. 19:40Z = 09:40 .. 15:40 ET on 2026-10-08, constructed (L32)
            rows.append(copy.deepcopy(template) | {"card_id": 100 + n, "ticker": f"TST{n:02d}",
                                                   "state_at": datetime(2026, 10, 8, 13, 40, tzinfo=UTC) + timedelta(minutes=20 * n)})
    store = RowStore(rows)
    # 21:30 ET on 10-08: the UTC date has already rolled to 10-09
    now = datetime(2026, 10, 9, 1, 30, tzinfo=UTC)
    view = panel.build_ladder_view(
        card_store=store, settings_store=Settings(SETTINGS_ROWS), clock=session_clock(), now=now,
        tunables_loader=_tunables(), rung_source=lambda instant, cfg: "reduced", position_reader=lambda card_id: POSITION,
    )
    assert store.days == [date(2026, 10, 8)]
    assert len(view.active) == 5 and {c.state for c in view.active} == {CardState.WATCH}
    assert len(view.terminal) == 14 and {c.state for c in view.terminal} == {CardState.EXPIRED}
    assert view.empty_message is None
    rendered = panel.render_ladder(view)
    assert rendered.count('<article class="ladder-item') == 5
    assert "TERMINAL · 14" in rendered and "EXPIRED · 14" in rendered
    assert "No radar cards today" not in rendered


def test_hidden_cards_stay_hidden_by_the_store_where(monkeypatch):
    """R685 CONTROL: yesterday's terminal cards are left out by the store's WHERE, never by the page."""
    from cobalt.cards.store import CardStore

    calls = []

    class Cursor:
        description = []

        def fetchall(self):
            return []

    class Conn:
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

        def execute(self, sql, params=None):
            calls.append((sql, params))
            return Cursor()

    monkeypatch.setattr(CardStore, "_connect", lambda self, **kwargs: Conn())
    assert CardStore("not_a_db").radar_board_cards(date(2026, 10, 8)) == []
    assert len(calls) == 1
    sql, params = calls[0]
    assert "state = ANY(%s)" in sql
    assert "(state_at AT TIME ZONE 'America/New_York')::date = %s" in sql
    # check A3: open states OR today's ET day, never both required
    assert "state = ANY(%s) OR (state_at AT TIME ZONE 'America/New_York')::date = %s" in sql
    assert CardStore.RADAR_OPEN_STATES == ("WATCH", "ARMED", "TRIGGERED", "FILLED")
    assert params == (list(CardStore.RADAR_OPEN_STATES), date(2026, 10, 8))
    terminal = {s.value for s in (CardState.CLOSED, CardState.PASSED, CardState.EXPIRED, CardState.MISSED)}
    assert not terminal & set(params[0])


def test_hidden_cards_control_rejects_and_instead_of_or(monkeypatch):
    from cobalt.cards.store import CardStore

    def broken(self, trade_date):
        with self._connect() as conn:
            conn.execute(
                "SELECT * FROM radar_cards_v WHERE state = ANY(%s) "
                "AND (state_at AT TIME ZONE 'America/New_York')::date = %s "
                "ORDER BY card_id",
                (list(self.RADAR_OPEN_STATES), trade_date),
            )
        return []

    monkeypatch.setattr(CardStore, "radar_board_cards", broken)
    with pytest.raises(AssertionError):
        test_hidden_cards_stay_hidden_by_the_store_where(monkeypatch)


@pytest.mark.parametrize("case", ["read", "row", "dot", "rung", "settings"])
def test_ladder_inputs_fail_loud(evaluated, case):
    rows = copy.deepcopy(evaluated["rows"])
    store, settings, rung = RowStore(rows), Settings(SETTINGS_ROWS), (lambda i, c: "reduced")
    if case == "read":
        store = RowStore(error=RuntimeError("offline"))
    elif case == "row":
        del rows[0]["trigger_price"]
    elif case == "dot":
        rows[0]["dots"] = [{"factor": "rvol"}]
    elif case == "rung":
        rung = lambda i, c: (_ for _ in ()).throw(RuntimeError("day mode unresolved"))  # noqa: E731
    elif case == "settings":
        settings = Settings({"radar.cards_enabled": True})
    with pytest.raises(panel.RadarPanelError, match="FAILED"):
        panel.build_ladder_view(card_store=store, settings_store=settings, clock=session_clock(), now=SCAN0,
                                tunables_loader=_tunables(), rung_source=rung)


# ---------------------------------------------------------------------
# badges, dots, the tap strip, keys, promote, health
# ---------------------------------------------------------------------


def test_every_displayed_card_field_carries_its_owner_badge(evaluated):
    view = _ladder(evaluated["rows"])
    card = view.active[-1]
    assert card.badges == FIELD_OWNERS
    rendered = panel.render_ladder(view)
    for field in panel.BADGED_FIELDS:
        badge = FIELD_OWNERS[field]
        assert re.search(rf'data-field="{field}"[^>]*>.*?<span class="badge badge-{badge.lower()}">{badge}</span>',
                         rendered, re.S), field


def test_computed_dots_render_hollow_shadow_with_engine_grade_and_why(evaluated):
    card = _ladder(evaluated["rows"]).active[-1]
    dots = {d.factor: d for d in card.dots}
    assert dots["rvol"].role == "shadow" and dots["rvol"].hollow and dots["rvol"].engine_grade is not None
    assert dots["rvol"].why and dots["rvol"].colour in (0, 1, 2)
    assert dots["trail_fit"].na_reason == "MANUAL" and dots["trail_fit"].hollow
    assert dots["setup_relation"].role == "human" and dots["setup_relation"].hollow
    assert dots["setup_relation"].engine_grade is None and dots["setup_relation"].shown_grade is None
    assert dots["market_alignment"].na_reason == "DEFAULT_UNRULED"
    rendered = panel.render_ladder(_ladder(evaluated["rows"]))
    assert 'class="dot hollow role-shadow' in rendered and 'class="dot hollow role-human' in rendered
    assert "shadow " in rendered


def test_a_tapped_dot_renders_filled_with_the_trader_grade(evaluated):
    rows = copy.deepcopy(evaluated["rows"])
    rows[0]["dots"] = [d.model_copy(update={"trader_grade": 7}) if d.factor == "setup_relation" else d
                       for d in rows[0]["dots"]]
    card = next(c for c in _ladder(rows).active if c.id == 1)
    dot = next(d for d in card.dots if d.factor == "setup_relation")
    assert not dot.hollow and dot.shown_grade == 7 and dot.trader_grade == 7


def test_one_to_ten_tap_strip_on_every_dot_of_a_live_card_and_none_on_terminal(evaluated):
    view = _ladder(evaluated["rows"])
    rendered = panel.render_ladder(view)
    watch = next(c for c in view.active if c.state is CardState.WATCH)
    for dot in watch.dots:
        strip = re.search(
            rf'<div class="tap-strip" data-card-id="{watch.id}" data-factor="{re.escape(dot.factor)}"[^>]*>(.*?)</div>',
            rendered, re.S,
        )
        assert strip, dot.factor
        assert re.findall(r'data-grade="(\d+)"', strip.group(1)) == [str(n) for n in range(1, 11)]
    for card in view.terminal:
        assert f'class="tap-strip" data-card-id="{card.id}"' not in rendered


def test_key_row_has_every_key_with_dollars_greyed_disabled_and_still_tappable(evaluated):
    view = _ladder(evaluated["rows"])
    watch = next(c for c in view.active if c.state is CardState.WATCH)
    keys = {k.grade: k for k in watch.keys}
    assert list(keys) == ["A+", "A", "B", "C"]
    assert keys["A+"].enabled is False and keys["A+"].dollars == Decimal("170")
    assert keys["A"].enabled and keys["A"].dollars == Decimal("70")
    rendered = panel.render_ladder(view)
    assert re.search(rf'<button class="key key-disabled" data-card-id="{watch.id}" data-key="A\+"[^>]*>A\+ · \$170', rendered)
    assert f'data-card-id="{watch.id}" data-key="pass"' in rendered
    tag = re.search(rf'<button class="key key-disabled" data-card-id="{watch.id}"[^>]*>', rendered).group(0)
    assert not re.search(r"\sdisabled(\s|>|=)", tag), tag  # greyed, never the HTML disabled attribute


def test_snap_notice_renders_amber_and_the_key_freezes_once_armed(evaluated):
    view = _ladder(evaluated["rows"])
    armed = next(c for c in view.active if c.state is CardState.ARMED)
    assert armed.tapped_grade == "A+" and armed.sized_grade == "A" and armed.snap_notice
    rendered = panel.render_ladder(view)
    assert f'<div class="snap-notice">{armed.snap_notice.replace("$", "$")}' in rendered.replace("&#x27;", "'")
    assert f'data-card-id="{armed.id}" data-key=' not in rendered


def test_proposed_key_without_conviction_says_tap_to_propose(evaluated):
    watch = next(c for c in _ladder(evaluated["rows"]).active if c.state is CardState.WATCH)
    assert watch.proposed_key is None and watch.card_score is None
    rendered = panel.render_ladder(_ladder(evaluated["rows"]))
    assert "tap to propose" in rendered
    assert "score suppressed" in rendered


def test_promote_is_live_on_watch_cards_and_release_on_the_promoted_one(evaluated):
    rows = copy.deepcopy(evaluated["rows"])
    extra = copy.deepcopy(rows[0]) | {"card_id": 7, "ticker": "BGFI"}
    rows.append(extra)
    view = _ladder(rows)
    rendered = panel.render_ladder(view)
    assert 'title="S2-P2" disabled' not in rendered
    assert re.search(r'<button class="promote" data-card-id="\d+" data-promote="promote"[^>]*>promote ↑</button>', rendered)
    rows[-1]["promoted_at"] = SCAN0
    view = _ladder(rows)
    promoted = next(c for c in view.active if c.id == 7)
    assert promoted.promoted and view.active.index(promoted) == 3  # pinned three keep priority
    assert 'data-card-id="7" data-promote="release"' in panel.render_ladder(view)


def test_health_pills_render_from_the_stored_card_health(evaluated):
    view = _ladder(evaluated["rows"])
    filled = next(c for c in view.active if c.state is CardState.FILLED)
    labels = {h.label: h.status for h in filled.health}
    assert labels["cost"] == "n/a" and labels["alignment"] == "n/a"
    rendered = panel.render_ladder(view)
    assert 'class="health n-a"' in rendered and "cost · n/a" in rendered
    assert "IN-TRADE" in rendered


def test_ladder_renders_every_real_shape_card_state(evaluated):
    rendered = panel.render_ladder(_ladder(evaluated["rows"]))
    for label in ("WATCH", "ARMED · LOCKED", "TRIGGERED", "IN-TRADE", "PASSED", "EXPIRED"):
        assert label in rendered
    # The STATE reads IN-TRADE, never FILLED; the one "FILLED" is the TRIGGERED
    # card's tap label, the design's words (S3 C3, v3 §2 "FILLED @ [price] [shares]").
    assert "FILLED" not in rendered.replace('data-state="FILLED"', "").replace(">FILLED @</button>", "")


def test_first_two_open_detail_order_and_terminal_below_active(evaluated):
    rendered = panel.render_ladder(_ladder(evaluated["rows"]))
    assert rendered.count('class="ladder-item open"') == 2
    assert 'id="collapse-all"' in rendered and 'id="top-two"' in rendered
    first = rendered.index('data-detail="levels"')
    indices = [rendered.index(f'data-detail="{name}"', first) for name in ("levels", "rank", "news", "notes", "chart")]
    assert indices == sorted(indices)
    terminal_at = rendered.index('class="terminal"')
    assert rendered.rindex('class="ladder-item') < terminal_at < rendered.index('class="terminal-row"')


def test_outside_pool_label_and_pool_position(evaluated):
    rows = copy.deepcopy(evaluated["rows"])
    rows[3]["outside_pool"] = True
    rendered = panel.render_ladder(_ladder(rows))
    assert "OUTSIDE POOL" in rendered


def test_card_panel_escapes_why_and_notices(evaluated):
    rows = copy.deepcopy(evaluated["rows"])
    rows[0]["why"] = '<script data-x="bad">&'
    rendered = panel.render_ladder(_ladder(rows))
    assert "<script data-x" not in rendered and "&lt;script data-x" in rendered


# ---------------------------------------------------------------------
# the STALE badge (R36 2026-09-21): pool row + card, a second rendering of
# `poll_failures`. The pool view comes from the pool suite's own helpers.
# ---------------------------------------------------------------------

# GOLDEN PINS captured on main's code (`5b208a0`), GREEN there — from then on a GUARD.
# LADDER pin re-captured 2026-09-23 on setups/seven-0921 (b007ce2e): the setups ladder change adds the assumed_formation dot (R2-2 = B); healthy bars still add nothing (seam-fix-build-2026-09-23.md D3).
# LADDER pin re-captured 2026-09-28 on s3/exits-c3 (was 0ac9b5d0…): C3 adds the TRIGGERED tap (ARMED), the FILLED @ / PASS taps (TRIGGERED) and the IN-TRADE block over the constructed POSITION; healthy bars still add nothing (s3-exits-c3-build-2026-09-28.md E3).
# LADDER pin re-captured 2026-10-07 on ops/radar-direction-color-1007 (was b018e70e…): R625 adds the strip and title direction class and the strip arrow; healthy bars still add nothing.
# LADDER pin re-captured 2026-10-07 on ops/radar-arm-disarm-1007 (was b3174d30…): R627 adds the ARM tap (WATCH) and the DISARM tap with its reason (ARMED); healthy bars still add nothing.
# LADDER pin re-captured 2026-10-08 on ops/disarm-one-tap-1008 (was 9a52577c…): R689 replaces the typed DISARM reason with the DISARM toggle and its five reason chips (ARMED); healthy bars still add nothing.
PIN_HEALTHY_POOL_SHA256 = "f2e79add6bc4d4286b381154b071b04ec9e7887467ffd15b0f499e9d62181552"
PIN_HEALTHY_LADDER_SHA256 = "1866a7ad92de42fd7552f5e7b39673b3c95060cd5570250e3492695dff92c427"
PIN_HEALTHY_API_SHA256 = "450b3415c2346c8b13b53932c5175f56ee6af78877ca9fc8086ca824601c5462"

# Tonight's `mirrorDegraded` line, byte for byte as main has it (`radar_panel.py:1127`).
MIRROR_DEGRADED_LINE = r""" function mirrorDegraded(layer){const line=document.getElementById('degraded-line'); const parts=Array.from(layer.querySelectorAll('.refresh-failure,.panel-banner.degraded,.panel-banner.stale')).map(x=>x.innerHTML); const text=parts.join(' | '); if(line.innerHTML!==text){line.innerHTML=text;} const none=parts.length===0; if(line.hidden!==none){line.hidden=none;}}"""

BADGE_RE = r'<span class="bars-stale" title="[^"]*">STALE</span>'


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def _badge_html(tip: str) -> str:
    return f'<span class="bars-stale" title="{html.escape(tip)}">STALE</span>'


def _stale_case(evaluated, *, row=True, card=True, gure=True):
    """The pool view for a stale set built on `_bars_poll_failed_pool` with tickers
    that come FROM THE FIXTURES: the one current member of `_small_snapshot()`,
    the evaluated cards' ticker (a card outside the pool) and the fixture's GURE."""
    row_ticker = pool_tests._pool_row_ticker()
    card_ticker = evaluated["rows"][0]["ticker"]
    pool_tickers = {member["ticker"] for member in pool_tests._small_snapshot()[1]}
    assert card_ticker not in pool_tickers and "GURE" not in pool_tickers
    assert {r["ticker"] for r in evaluated["rows"]} == {card_ticker}
    failures = []
    if row:
        failures.append(pool_tests._failure(row_ticker, "stale", "2026-01-05 15:19:00+00:00"))
    if card:
        failures.append(pool_tests._failure(card_ticker, "error", "2026-01-05 15:30:00+00:00"))
    if gure:
        failures.append(pool_tests._failure("GURE", "stale", "2026-01-05 14:40:00+00:00"))
    pool_row, members = pool_tests._bars_poll_failed_pool(failures=failures)
    built, _ = pool_tests._build(pool_row=pool_row, members=members)
    assert [banner.title for banner in built.pool.banners] == ["BARS POLL FAILED"]
    return SimpleNamespace(
        row_ticker=row_ticker,
        card_ticker=card_ticker,
        tips={item["ticker"]: pool_tests._tip(item) for item in failures},
        pool=built.pool,
    )


def _page(pool, ladder, phone_frame=False):
    return panel.render_radar_page(panel.RadarPanelView(pool=pool, ladder=ladder), phone_frame=phone_frame)


@pytest.mark.parametrize("phone_frame", [False, True])
def test_bars_stale_badge_marks_exactly_the_failing_tickers(evaluated, phone_frame):
    case = _stale_case(evaluated)
    ladder_view = _ladder(evaluated["rows"])
    page = _page(case.pool, ladder_view, phone_frame)
    if phone_frame:
        assert 'class="phone-frame"' in page
    row_badge = _badge_html(case.tips[case.row_ticker])
    card_badge = _badge_html(case.tips[case.card_ticker])

    pool = pool_tests._pool_layer(page)
    assert pool.count('class="bars-stale"') == 1
    assert f'<td class="ticker">{case.row_ticker}{row_badge}</td>' in pool
    rows = re.findall(r'<tr data-episode-id="\d+" data-category="(\w+)">(.*?)</tr>', pool, re.S)
    assert [category for category, body in rows if "bars-stale" in body] == ["current"]
    assert {category for category, _ in rows} == {"current", "departed", "excluded"}
    banner = case.pool.banners[0].detail
    for tip in case.tips.values():
        assert tip in banner
    assert "GURE" in banner

    ladder = page[page.index('id="ladder-layer"') : page.index('id="pool-layer"')]
    articles = dict(re.findall(r'<article class="ladder-item[^"]*" data-card-id="(\d+)">(.*?)</article>', ladder, re.S))
    assert sorted(articles) == sorted(str(card.id) for card in ladder_view.active)
    assert len(ladder_view.active) == 4
    for card in ladder_view.active:
        body = articles[str(card.id)]
        armed = card.state is CardState.ARMED
        assert f"<b>{case.card_ticker}{card_badge}</b>" in body
        assert re.search(
            r'<span class="field" data-field="last_price">last <span class="badge badge-[\w-]+">[^<]+</span> '
            rf"<b>[^<]*</b>{re.escape(card_badge)}</span>",
            body,
        )
        assert ("trigger-distance" in body) == armed
        if armed:
            assert re.search(rf'<div class="trigger-distance">last [^<]+{re.escape(card_badge)} · trigger', body)
        assert body.count('class="bars-stale"') == (3 if armed else 2)
    terminal = ladder[ladder.index('class="terminal"') :]
    assert terminal.count('class="terminal-row"') == len(ladder_view.terminal) == 2
    assert "bars-stale" not in terminal
    assert "GURE" not in ladder
    markup = pool_tests._main_markup(page)
    assert markup.count('class="bars-stale"') == 1 + 4 * 2 + 1
    titles = re.findall(r'<span class="bars-stale" title="([^"]*)"', markup)
    assert set(titles) == {case.tips[case.row_ticker], case.tips[case.card_ticker]}
    assert not any("GURE" in title for title in titles)


@pytest.mark.parametrize("phone_frame", [False, True])
def test_bars_stale_badge_absent_and_output_unchanged_when_healthy(evaluated, phone_frame):
    """The pins are a GUARD: captured on main's code, they hold on the change too."""
    healthy, _ = pool_tests._build()
    assert healthy.pool.banners == []
    ladder_view = _ladder(evaluated["rows"])
    page = _page(healthy.pool, ladder_view, phone_frame)
    pool_html = panel.render_pool(healthy.pool)
    ladder_html = panel.render_ladder(ladder_view)
    api_json = json.dumps(panel.pool_api_payload(healthy.pool), sort_keys=True)
    for text in (pool_html, ladder_html, api_json, pool_tests._main_markup(page)):
        assert "bars-stale" not in text
    assert 'class="bars-stale"' not in page and "data-bars-stale" not in page
    assert _sha(pool_html) == PIN_HEALTHY_POOL_SHA256, _sha(pool_html)
    assert _sha(ladder_html) == PIN_HEALTHY_LADDER_SHA256, _sha(ladder_html)
    assert _sha(api_json) == PIN_HEALTHY_API_SHA256, _sha(api_json)


def test_bars_stale_badge_marks_a_lifecycle_card_outside_the_pool(evaluated):
    case = _stale_case(evaluated, row=False, gure=False)
    ladder_view = _ladder(evaluated["rows"])
    assert case.pool.banners[0].detail.startswith(f"{case.card_ticker} error since ")
    page = _page(case.pool, ladder_view)
    pool = pool_tests._pool_layer(page)
    assert 'class="bars-stale"' not in pool  # its ticker has no pool row
    assert case.card_ticker not in re.findall(r'<td class="ticker">([^<]*)', pool)
    strip = f"<b>{case.card_ticker}{_badge_html(case.tips[case.card_ticker])}</b>"
    assert page.count(strip) == len(ladder_view.active) == 4  # keyed by ticker, not pool membership


def test_bars_stale_badge_marks_only_the_stale_ticker_among_active_cards(evaluated):
    """F2 (round 2): the card-strip badge must single out the stale ticker
    among two active cards of different tickers, never every active card.
    No parametrize over phone_frame here — X4 covers the frame."""
    rows = copy.deepcopy(evaluated["rows"])
    extra = copy.deepcopy(rows[0]) | {"card_id": 7, "ticker": "BGFI"}
    rows.append(extra)
    ladder_view = _ladder(rows)
    assert {c.ticker for c in ladder_view.active} == {"FTFT", "BGFI"}
    assert "BGFI" not in {m["ticker"] for m in pool_tests._small_snapshot()[1]}

    def _articles(page):
        ladder = page[page.index('id="ladder-layer"') : page.index('id="pool-layer"')]
        return dict(
            re.findall(r'<article class="ladder-item[^"]*" data-card-id="(\d+)">(.*?)</article>', ladder, re.S)
        )

    # CASE 1 — FTFT stale, BGFI healthy
    case1 = _stale_case(evaluated, row=False, gure=False)
    assert case1.card_ticker == "FTFT"
    page1 = _page(case1.pool, ladder_view)
    articles1 = _articles(page1)
    ftft_badge = _badge_html(case1.tips["FTFT"])
    for card in ladder_view.active:
        if card.ticker == "FTFT":
            assert f"<b>FTFT{ftft_badge}</b>" in articles1[str(card.id)]
    bgfi_article1 = articles1["7"]
    assert "bars-stale" not in bgfi_article1
    assert "<b>BGFI</b>" in bgfi_article1
    plain_articles = _articles(_page(pool_tests._build()[0].pool, ladder_view))
    assert bgfi_article1 == plain_articles["7"]

    # CASE 2 — BGFI stale, FTFT healthy
    failures2 = [pool_tests._failure("BGFI", "error", "2026-01-05 15:30:00+00:00")]
    pool_row2, members2 = pool_tests._bars_poll_failed_pool(failures=failures2)
    built2, _ = pool_tests._build(pool_row=pool_row2, members=members2)
    tip_bgfi = pool_tests._tip(failures2[0])
    badge_bgfi = _badge_html(tip_bgfi)
    page2 = _page(built2.pool, ladder_view)
    articles2 = _articles(page2)
    bgfi_article2 = articles2["7"]
    assert f"<b>BGFI{badge_bgfi}</b>" in bgfi_article2
    assert bgfi_article2.count('class="bars-stale"') == 2
    assert "trigger-distance" not in bgfi_article2
    for card in ladder_view.active:
        if card.ticker == "FTFT":
            assert "bars-stale" not in articles2[str(card.id)]
    markup2 = pool_tests._main_markup(page2)
    assert markup2.count('class="bars-stale"') == 2


@pytest.mark.parametrize("path", ["/radar", "/radar?frame=phone"])
def test_bars_stale_badge_renders_on_the_card_through_the_real_radar_route(monkeypatch, evaluated, path):
    """F3 (round 2): the card badge must render through the REAL `/radar`
    route (build_radar_panel → render_radar_page, unmonkeypatched), not only
    through the pure renderer functions tests (a)-(c) and X3 call directly."""
    rows = copy.deepcopy(evaluated["rows"])
    extra = copy.deepcopy(rows[0]) | {"card_id": 7, "ticker": "BGFI"}
    rows.append(extra)
    ladder_view = _ladder(rows)
    case = _stale_case(evaluated, gure=False)
    assert case.row_ticker != "BGFI" and case.card_ticker == "FTFT"
    monkeypatch.setattr(
        web_module, "build_radar_panel",
        lambda **kw: panel.RadarPanelView(pool=case.pool, ladder=ladder_view),
    )
    response = TestClient(web_module.app).get(path)
    assert response.status_code == 200

    ladder = response.text[response.text.index('id="ladder-layer"') : response.text.index('id="pool-layer"')]
    ftft_badge = _badge_html(case.tips[case.card_ticker])
    expected_ftft = len([c for c in ladder_view.active if c.ticker == "FTFT"])
    assert ladder.count(f"<b>FTFT{ftft_badge}</b>") == expected_ftft
    # Each active card's ticker prints twice: once in the strip (badge-eligible)
    # and once, plain, in the detail pane's own "ticker" field (never badged —
    # `_field(card, "ticker", "ticker", card.ticker)`, radar_panel.py:1040).
    assert ladder.count("<b>BGFI</b>") == 2
    articles = dict(
        re.findall(r'<article class="ladder-item[^"]*" data-card-id="(\d+)">(.*?)</article>', ladder, re.S)
    )
    assert "bars-stale" not in articles["7"]

    pool = pool_tests._pool_layer(response.text)
    row_badge = _badge_html(case.tips[case.row_ticker])
    assert f'<td class="ticker">{case.row_ticker}{row_badge}</td>' in pool

    if "phone" in path:
        assert 'class="phone-frame"' in response.text

    expected = panel.render_radar_page(
        panel.RadarPanelView(pool=case.pool, ladder=ladder_view), phone_frame="phone" in path
    )
    # voice V1: /radar carries the voice widget partial before </body>, nothing else changes
    from cobalt.voice.web import widget_html

    expected = expected.replace("</body>", widget_html() + "</body>", 1)
    assert response.text == expected


def test_bars_stale_follows_the_refreshed_pool_fragment_and_never_moves_the_ladder(evaluated):
    ladder_view = _ladder(evaluated["rows"])
    steps = [_stale_case(evaluated), None, _stale_case(evaluated, card=False)]  # stale -> healthy -> stale
    for step in steps:
        if step is None:
            healthy, _ = pool_tests._build()
            fragment = panel.pool_api_payload(healthy.pool)["html"]
            assert "data-bars-stale" not in fragment and "bars-stale" not in fragment
            continue
        fragment = panel.pool_api_payload(step.pool)["html"]
        tag = re.search(r'<section id="pool-layer"[^>]*>', fragment).group(0)
        attr = re.search(r'data-bars-stale="([^"]*)"', tag)
        assert attr, tag
        assert tag.index("data-watermark") < tag.index("data-bars-stale")
        assert json.loads(html.unescape(attr.group(1))) == step.tips
        assert f'<td class="ticker">{step.row_ticker}{_badge_html(step.tips[step.row_ticker])}</td>' in fragment
        # THE LADDER DOES NOT MOVE — take the badges out and it is main's ladder, byte for byte.
        marked = panel.render_ladder(ladder_view, bars_stale=step.tips)
        plain = panel.render_ladder(ladder_view)
        assert re.sub(BADGE_RE, "", marked) == plain
        assert (marked != plain) == (step.card_ticker in step.tips)
        bare_pool = panel.render_pool(step.pool.model_copy(update={"bars_stale_tickers": {}}))
        assert " data-bars-stale=" not in bare_pool and "bars-stale" not in bare_pool
        assert re.sub(r' data-bars-stale="[^"]*"', "", re.sub(BADGE_RE, "", panel.render_pool(step.pool))) == bare_pool
    js = panel.PANEL_JS
    assert "function mirrorStale(layer)" in js
    assert js.index("mirrorDegraded(next)") < js.index("mirrorStale(next)") < js.index("catch(error)")
    start = js.index("function mirrorStale(")
    body = js[start : js.index("\n", start)]
    for needed in ("dataset.barsStale", "JSON.parse(", "querySelectorAll('.ladder-item')", ".strip b", "firstChild"):
        assert needed in body, needed
    for forbidden in ("refreshLadder", "fetch(", "classList", "sort(", "appendChild", "insertBefore",
                      "replaceWith", "innerHTML", "cursor="):
        assert forbidden not in body, forbidden
    assert "window.setInterval(refreshPool,interval)" in js
    assert MIRROR_DEGRADED_LINE in js


# ---------------------------------------------------------------------
# R625 2026-10-07: the strip and the title say long or short by colour
# ---------------------------------------------------------------------

ARROW = {"long": "↑", "short": "↓"}

#: Card 89 row B, byte for byte: the existing tokens and the dots' existing fills.
DIRECTION_CSS = (
    ".strip.dir-long{background:#0f2a1c;border-color:var(--green)}"
    ".strip.dir-short{background:#3a1119;border-color:var(--red)}"
    ".card-title.dir-long{color:var(--green)}"
    ".card-title.dir-short{color:var(--red)}"
)
#: `PANEL_CSS` lines at BASE d2b53d6d (`radar_panel.py:1496`, `:1498`–`:1501`), quoted.
BASE_ROOT_LINE = (
    ":root{color-scheme:dark;--surface:#0d1117;--card:#11151c;--border:#1f2531;--text:#e6e9ef;--muted:#7d8595;"
    "--blue:#4f8dff;--amber:#d9a24a;--green:#35c77a;--red:#ef5b6b}"
)
BASE_MEDIA_LINES = (
    "@media (max-width:1149px){.expanded{grid-template-columns:1fr}.detail-pane{grid-row:2}}",
    "@media (max-width:700px){.strip{grid-template-columns:75px 70px 1fr}.strip span:nth-child(4){display:none}"
    ".radar-wrap{padding:10px}.pool-stats{text-align:left}.layer-head{align-items:flex-start;flex-direction:column}"
    "table{display:block;overflow-x:auto}}",
    "@media (max-width:430px){body,.phone-frame{width:100%}.radar-wrap{width:366px;max-width:100%;padding:8px}"
    ".expanded{padding:5px}.card-pane,.detail-pane{padding:11px}.card-title strong{font-size:24px}"
    ".strip{padding:0 8px}.terminal-row{grid-template-columns:75px 65px 1fr}.terminal-row time{display:none}}",
)
BASE_PHONE_LINE = (
    ".phone-frame{width:390px;margin:auto;border:12px solid #05070a;border-radius:26px}"
    ".phone-frame .radar-wrap{width:366px;padding:8px}"
)


def _directed(rows, direction):
    rows = copy.deepcopy(rows)
    for row in rows:
        row["direction"] = direction
    return rows


def _ladder_articles(page):
    ladder = page[page.index('id="ladder-layer"') : page.index('id="pool-layer"')]
    return dict(re.findall(r'<article class="ladder-item[^"]*" data-card-id="(\d+)">(.*?)</article>', ladder, re.S))


def _strip_and_title(body):
    strip = re.search(r'<button class="strip[^"]*".*?</button>', body, re.S).group(0)
    title = re.search(r'<div class="card-title[^"]*">.*?</div>', body, re.S).group(0)
    return strip, title


@pytest.mark.parametrize("phone_frame", [False, True])
@pytest.mark.parametrize("direction", ["long", "short"])
def test_radar_direction_strip_and_title_carry_the_direction_class_and_arrow(evaluated, direction, phone_frame):
    ladder_view = _ladder(_directed(evaluated["rows"], direction))
    healthy, _ = pool_tests._build()
    page = _page(healthy.pool, ladder_view, phone_frame)
    articles = _ladder_articles(page)
    assert len(ladder_view.active) == 4 and sorted(articles) == sorted(str(c.id) for c in ladder_view.active)
    arrow = ARROW[direction]
    for card in ladder_view.active:
        assert card.direction == direction
        strip, title = _strip_and_title(articles[str(card.id)])
        assert strip.startswith(f'<button class="strip dir-{direction}" type="button"'), strip
        # mirrorStale reads `.strip b`'s first text node: the ticker stays the `<b>`'s first child;
        # the arrow opens the THIRD span, and the strip keeps its four children.
        assert re.match(
            rf'<button class="strip dir-{direction}" type="button" data-toggle-card="{card.id}">'
            rf"<span>#\d+ · [^<]*</span><b>{re.escape(card.ticker)}</b>"
            rf'<span><span class="direction {direction}">{arrow}</span> '
            rf"{re.escape(html.escape(card.setup))} → {re.escape(html.escape(card.trade))}</span>"
            r"<span>[^<]*</span></button>$",
            strip,
        ), strip
        assert title.startswith(f'<div class="card-title dir-{direction}">'), title
        assert f'<span class="direction {direction}">{arrow}</span>' in title
        assert ARROW["short" if direction == "long" else "long"] not in strip + title


def test_radar_unknown_direction_is_marked_never_guessed(evaluated):
    card = _ladder(evaluated["rows"]).active[0].model_copy(update={"direction": None})
    assert card.direction is None
    rendered = panel.render_ladder(panel.LadderView(active=[card], terminal=[], empty_message=None))
    body = re.search(r'<article class="ladder-item[^"]*" data-card-id="\d+">(.*?)</article>', rendered, re.S).group(1)
    strip, title = _strip_and_title(body)
    for part in (title, strip):
        assert "↑" not in part and "↓" not in part, part  # never a guessed direction
        assert "dir-long" not in part and "dir-short" not in part, part
        assert "dir-unknown" in part and "direction ?" in part, part
    assert strip.startswith('<button class="strip dir-unknown" type="button"'), strip
    assert '<span><span class="direction unknown">direction ?</span> ' in strip
    assert title.startswith('<div class="card-title dir-unknown">'), title
    assert '<span class="direction unknown">direction ?</span>' in title


@pytest.mark.parametrize("direction", [None, "sideways"])
def test_radar_row_without_a_valid_direction_still_fails_loud(evaluated, direction):
    """CONTROL (card 89 row A): no neutral card is ever built from a row; the row still fails loud."""
    rows = copy.deepcopy(evaluated["rows"])
    rows[0]["direction"] = direction
    with pytest.raises(panel.RadarPanelError, match="FAILED: invalid radar card row"):
        _ladder(rows)


def test_radar_direction_tint_reuses_existing_colours():
    lines = panel.PANEL_CSS.splitlines()
    assert DIRECTION_CSS in lines
    at = lines.index(DIRECTION_CSS)
    assert lines[at - 1].startswith("*{box-sizing:border-box}") and lines[at + 1] == BASE_MEDIA_LINES[0]
    rest = "\n".join(lines[:at] + lines[at + 1 :])
    colours = re.findall(r"#[0-9a-fA-F]{6}\b", DIRECTION_CSS)
    assert colours == ["#0f2a1c", "#3a1119"]
    for colour in colours:
        assert colour in rest, colour
    assert "dir-unknown" not in panel.PANEL_CSS
    assert BASE_ROOT_LINE in lines and BASE_PHONE_LINE in lines
    for line in BASE_MEDIA_LINES:
        assert line in lines, line


def _expanded_without_direction(body):
    """The `expanded` block minus its title and the three fields that differ by direction by design."""
    block = body[body.index('<div class="expanded"') : body.index("</aside></div>") + len("</aside></div>")]
    block, titles = re.subn(r'<div class="card-title[^"]*">.*?</div>', "", block, count=1, flags=re.S)
    block, levels = re.subn(r'<span class="field">[12]R <b>[^<]*</b></span>', "", block)
    block, fields = re.subn(
        r'<span class="field" data-field="direction">direction <span class="badge[^"]*">[^<]*</span> '
        r"<b>(?:long|short)</b></span>",
        "",
        block,
    )
    block, running = re.subn(r'(<div class="running"><b>[^<]*</b> · )(?:long|short)( · )', r"\1\2", block)
    # The same 1R / 2R targets (`:908`, by the sign) print again in the IN-TRADE head (`:1351`).
    block, exits = re.subn(r"(<b>IN-TRADE</b> · stop [^<]* · next exits )[^<]* / [^<]*(</div>)", r"\1\2", block)
    assert (titles, levels, fields) == (1, 2, 1) and running in (0, 1) and exits == running
    return block, running


@pytest.mark.parametrize("phone_frame", [False, True])
def test_radar_direction_touches_only_strip_and_title(evaluated, phone_frame):
    healthy, _ = pool_tests._build()
    ladder_view = _ladder(evaluated["rows"])
    page = _page(healthy.pool, ladder_view, phone_frame)
    articles = _ladder_articles(page)
    for body in articles.values():
        assert body.count("dir-") == 2, body.count("dir-")
        assert re.findall(r'class="([^"]*)dir-', body) == ["strip ", "card-title "]
    ladder = page[page.index('id="ladder-layer"') : page.index('id="pool-layer"')]
    assert ladder.count("dir-") == 2 * len(ladder_view.active)
    assert "dir-" not in ladder[ladder.index('class="terminal"') :]

    renders = {}
    for direction in ("long", "short"):
        view = _ladder(_directed(evaluated["rows"], direction))
        assert {c.state for c in view.active} == {CardState.WATCH, CardState.ARMED, CardState.TRIGGERED,
                                                  CardState.FILLED}
        renders[direction] = (view, _ladder_articles(_page(healthy.pool, view, phone_frame)))
    (long_view, long_articles), (short_view, short_articles) = renders["long"], renders["short"]
    assert sorted(long_articles) == sorted(short_articles)
    fills = 0
    for card_id in long_articles:
        long_block, long_running = _expanded_without_direction(long_articles[card_id])
        short_block, short_running = _expanded_without_direction(short_articles[card_id])
        assert long_block == short_block, card_id
        assert long_running == short_running
        fills += long_running
    assert fills == 1  # the FILLED card's IN-TRADE running line
    watch = [c for c in long_view.active if c.state is CardState.WATCH]
    assert len(watch) == 1
    for articles_by_id in (long_articles, short_articles):
        block = re.search(r'<div class="state-block watch-state">.*?</div>', articles_by_id[str(watch[0].id)]).group(0)
        assert re.fullmatch(
            r'<div class="state-block watch-state"><b>WATCH</b> · proposed key [^<]+ · trigger [^<]+ · stop [^<]+</div>',
            block,
        ), block


@pytest.mark.parametrize("direction", [[], {}])
def test_radar_any_other_direction_is_marked_never_guessed(evaluated, direction):
    card = _ladder(evaluated["rows"]).active[0].model_copy(
        update={"direction": direction}
    )
    rendered = panel.render_ladder(
        panel.LadderView(active=[card], terminal=[], empty_message=None)
    )
    body = re.search(
        r'<article class="ladder-item[^"]*" data-card-id="\d+">(.*?)</article>',
        rendered,
        re.S,
    ).group(1)
    strip, title = _strip_and_title(body)
    for part in (strip, title):
        assert "dir-unknown" in part
        assert "direction ?" in part
        assert "dir-long" not in part and "dir-short" not in part
        assert "↑" not in part and "↓" not in part


# ---------------------------------------------------------------------
# R627 — the ARM tap (WATCH) and the DISARM tap with its reason (ARMED)
# ---------------------------------------------------------------------

ARM_KEY_CSS = ".s3-form button.arm-key{min-height:44px;padding:0 14px}"
ARM_TAP = (
    '<input type="hidden" name="source" value="panel">'
    '<button type="button" data-tap="1" class="arm-key">ARM</button>'
)
#: R719: the ARM tap on an unsized card — HTML `disabled`, its reason in the label.
ARM_UNSIZED_TAP = (
    '<input type="hidden" name="source" value="panel">'
    '<button type="button" data-tap="1" class="arm-key" disabled title="tap a key first">ARM · tap a key first</button>'
)
#: R689: the DISARM reason chips, literal here; the render test asserts them equal to `panel.DISARM_REASONS`.
DISARM_CHIPS = ("setup broke", "no volume", "market turned", "changed mind", "other")
DISARM_CHIP_TAPS = [
    '<input type="hidden" name="source" value="panel">'
    f'<input type="hidden" name="reason" value="{chip}">'
    f'<button type="button" data-tap="1" class="arm-key danger">{chip}</button>'
    for chip in DISARM_CHIPS
]
DISARM_TOGGLE = '<button class="disarm-toggle" type="button" data-dot-toggle="disarm">DISARM</button>'
DISARM_CHIPS_CSS = (
    ".disarm-toggle{min-height:44px;padding:0 14px;background:var(--card);border:1px solid var(--red);"
    "color:var(--red);border-radius:7px}.tap-strip.disarm-chips{grid-template-columns:repeat(auto-fit,"
    "minmax(120px,1fr));margin-top:6px}"
)
#: R719: the inert ARM's one CSS line, the `.45` of `.key-disabled`.
ARM_UNSIZED_CSS = ".s3-form button.arm-key:disabled{opacity:.45;cursor:not-allowed}"
#: BASE's (`6f55636b`) render of the ARMED card's `/triggered` block (its inner markup), sha256.
BASE_ARMED_TRIGGERED_TAP_SHA256 = "f91f7966b24284029c58e8415491d5a526673efdc5eff26dba9cc9e33099b846"
#: BASE's (`6f55636b`) `PANEL_JS`, sha256: R689 changes not one byte of the script.
BASE_PANEL_JS_SHA256 = "326400594ef47fdd85fc8d130e75ec2aaaff6558b37204a4873dc9059ff2e67a"
#: BASE's (`f6350cc4`) render of what R627 does not touch, sha256 of each fragment of
#: `_ladder(evaluated["rows"])` — the TRIGGERED and FILLED articles and the terminal section.
BASE_TRIGGERED_ARTICLE_SHA256 = "194886823f9810a554de693cc3e8a8ab128aa503ceee773028cc35cbf79a6e7f"
BASE_FILLED_ARTICLE_SHA256 = "5a522d9c06df4f3fbac199e82b6a111e6a9c38d882bcea786b784b326fc42a87"
BASE_TERMINAL_SHA256 = "c1021a1b3e63e2fd680fb9723d4879f3d579e9bc977ef4cf2552fa3385ed1906"


def _tap_blocks(fragment, path):
    return re.findall(
        rf'<div class="s3-form" data-card-id="(\d+)" data-path="{re.escape(path)}" data-card-tap="1">(.*?)</div>',
        fragment, re.S,
    )


@pytest.mark.parametrize("phone_frame", [False, True])
def test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only(evaluated, phone_frame):
    healthy, _ = pool_tests._build()
    ladder_view = _ladder(evaluated["rows"])
    page = _page(healthy.pool, ladder_view, phone_frame)
    articles = _ladder_articles(page)
    ids = {card.state: str(card.id) for card in ladder_view.active}
    watch, armed = ids[CardState.WATCH], ids[CardState.ARMED]
    assert _tap_blocks(articles[watch], "/arm") == [(watch, ARM_TAP)]
    # R689: one DISARM toggle and one closed chip tray, siblings in one cell (the toggle's
    # `parentElement` holds the tray PANEL_JS opens); five chip blocks, in list order.
    assert articles[armed].count('data-dot-toggle="disarm"') == 1
    assert panel.DISARM_REASONS == DISARM_CHIPS
    assert articles[armed].count(f'class="tap-strip disarm-chips" data-card-id="{armed}" hidden') == 1
    chip_blocks = _tap_blocks(articles[armed], "/disarm")
    assert chip_blocks == [(armed, tap) for tap in DISARM_CHIP_TAPS]
    cell = (
        f'<div class="disarm-cell">{DISARM_TOGGLE}<div class="tap-strip disarm-chips" data-card-id="{armed}" hidden>'
        + "".join(
            f'<div class="s3-form" data-card-id="{armed}" data-path="/disarm" data-card-tap="1">{tap}</div>'
            for tap in DISARM_CHIP_TAPS
        )
        + "</div></div>"
    )
    assert articles[armed].count(cell) == 1
    tray = cell[cell.index('<div class="tap-strip disarm-chips"') :]
    for forbidden in ("data-key", "data-grade", "data-factor"):
        assert forbidden not in cell, forbidden  # the key, grade and dot handlers never take a chip
    assert 'type="text"' not in articles[armed] and "<input name=" not in tray
    assert 'data-path="/disarm"' not in articles[watch] and 'data-path="/arm"' not in articles[armed]
    for card_id, body in articles.items():
        if card_id not in (watch, armed):
            assert '"/arm"' not in body and '"/disarm"' not in body, card_id
            assert 'data-dot-toggle="disarm"' not in body, card_id
    ladder = page[page.index('id="ladder-layer"') : page.index('id="pool-layer"')]
    assert '<input name="reason"' not in ladder and "disarm reason (required)" not in ladder
    assert ladder.count('data-path="/arm"') == 1 and ladder.count('data-path="/disarm"') == 5
    terminal = ladder[ladder.index('class="terminal"') :]
    assert "/arm" not in terminal and "/disarm" not in terminal
    assert "data-key" not in ARM_TAP  # the [data-key] handler runs before [data-tap]
    lines = panel.PANEL_CSS.splitlines()
    assert ARM_KEY_CSS in lines
    assert lines[lines.index(ARM_KEY_CSS) - 1].startswith(".s3-form{display:inline-flex;")
    assert lines[lines.index(ARM_KEY_CSS) + 1] == DISARM_CHIPS_CSS
    assert "display" not in DISARM_CHIPS_CSS  # `.tap-strip[hidden]{display:none}` still hides the closed tray


#: R719: the store's ARM rule (`cards/store.py:310`), the four sizing columns.
SIZING_COLUMNS = ("grade", "risk_budget", "shares", "used_risk")


def _arm_rows(evaluated):
    """R719: the fixture's WATCH row (born unsized) and a sized WATCH copy of
    the ARMED row (sized through `_sized`), card 7."""
    rows = {row["state"]: row for row in evaluated["rows"]}
    unsized = copy.deepcopy(rows["WATCH"])
    sized = copy.deepcopy(rows["ARMED"]) | {"card_id": 7, "state": "WATCH"}
    return unsized, sized


def _arm_block(row):
    """The one card's view and its `/arm` blocks, rendered alone."""
    view = _ladder([row])
    (card,) = view.active
    return card, _tap_blocks(panel.render_ladder(view), "/arm")


def _arm_tag(block):
    return re.search(r'<button[^>]*class="arm-key"[^>]*>', block).group(0)


def test_arm_is_inert_on_an_unsized_watch_card_and_live_once_sized(evaluated):
    unsized_row, sized_row = _arm_rows(evaluated)
    assert all(unsized_row[c] is None for c in SIZING_COLUMNS)
    assert all(sized_row[c] is not None for c in SIZING_COLUMNS)
    unsized, unsized_blocks = _arm_block(unsized_row)
    sized, sized_blocks = _arm_block(sized_row)
    assert unsized.state is CardState.WATCH and sized.state is CardState.WATCH
    assert unsized_blocks == [(str(unsized.id), ARM_UNSIZED_TAP)]
    assert sized_blocks == [(str(sized.id), ARM_TAP)]
    assert unsized.sized is False and sized.sized is True
    assert re.search(r"\sdisabled(\s|>|=)", _arm_tag(unsized_blocks[0][1]))  # the inverse of the key row's rule
    assert not re.search(r"\sdisabled(\s|>|=)", _arm_tag(sized_blocks[0][1]))
    lines = panel.PANEL_CSS.splitlines()
    assert lines[lines.index(DISARM_CHIPS_CSS) + 1] == ARM_UNSIZED_CSS


@pytest.mark.parametrize("column", SIZING_COLUMNS)
def test_arm_stays_inert_while_any_sizing_column_is_empty(evaluated, column):
    """R719: the page's rule is the store's four-column list, not `sized_grade` alone."""
    _, sized_row = _arm_rows(evaluated)
    row = sized_row | {column: None}
    card, blocks = _arm_block(row)
    assert card.sized is False
    assert row["sized_grade"] is not None
    assert blocks == [(str(card.id), ARM_UNSIZED_TAP)]


def test_the_disarm_chips_ride_the_existing_tray_and_tap_paths():
    """R689 CONTROL: the two PANEL_JS paths the chips ride, pinned as text, and the
    script byte-identical to BASE. Green on BASE and after."""
    source = panel.PANEL_JS
    assert hashlib.sha256(source.encode()).hexdigest() == BASE_PANEL_JS_SHA256, _sha(source)
    toggle = ("const dot=target.closest('[data-dot-toggle]');\n"
              "   if(dot){const tray=dot.parentElement.querySelector('.tap-strip'); if(tray){tray.hidden=!tray.hidden;} return;}")
    grade = "const grade=target.closest('.tap-strip [data-grade]');"
    tap = ("if(tap){const block=tap.closest('[data-card-tap]'); const body={}; "
           "block.querySelectorAll('input[name]').forEach(function(field){if(field.type==='checkbox'&&!field.checked)"
           "{return;} body[field.name]=field.value;}); post(block.dataset.cardId,block.dataset.path,body); return;}")
    for text in (toggle, grade, tap):
        assert source.count(text) == 1, text
    click = source[source.index("document.addEventListener('click'") :]
    assert click.index(toggle) < click.index(grade) < click.index("const tap=target.closest('[data-tap]');")
    assert click.index("const tap=target.closest('[data-tap]');") < click.index(tap)
    # both tick guards hold while a tray (a chip tray included) is open
    tick = pool_tests._js_body(pool_tests.TICK_HEAD)
    assert tick.count("querySelector('.tap-strip:not([hidden])')") == 2
    assert source.count(".tap-strip:not([hidden])") == 2


@pytest.mark.parametrize("phone_frame", [False, True])
def test_disarm_chips_leave_arm_and_triggered_unchanged(evaluated, phone_frame):
    """R689 CONTROL: the WATCH card's ARM tap and the ARMED card's TRIGGERED tap
    are BASE's, byte for byte."""
    healthy, _ = pool_tests._build()
    ladder_view = _ladder(evaluated["rows"])
    articles = _ladder_articles(_page(healthy.pool, ladder_view, phone_frame))
    ids = {card.state: str(card.id) for card in ladder_view.active}
    watch, armed = ids[CardState.WATCH], ids[CardState.ARMED]
    assert _tap_blocks(articles[watch], "/arm") == [(watch, ARM_TAP)]
    triggered = _tap_blocks(articles[armed], "/triggered")
    assert [card_id for card_id, _ in triggered] == [armed]
    assert _sha(triggered[0][1]) == BASE_ARMED_TRIGGERED_TAP_SHA256, _sha(triggered[0][1])


def _articles_by_state(view, articles):
    return {card.state: articles[str(card.id)] for card in view.active}


@pytest.mark.parametrize("phone_frame", [False, True])
def test_radar_arm_disarm_leaves_keys_sheet_and_other_states_unchanged(evaluated, phone_frame):
    healthy, _ = pool_tests._build()
    ladder_view = _ladder(evaluated["rows"])
    page = _page(healthy.pool, ladder_view, phone_frame)
    by_state = _articles_by_state(ladder_view, _ladder_articles(page))
    watch_card = next(card for card in ladder_view.active if card.state is CardState.WATCH)
    key_row = panel._key_row(watch_card)
    assert key_row in by_state[CardState.WATCH]
    assert len(watch_card.keys) == 4 and key_row.count('data-key="') == 5 and 'data-key="pass"' in key_row
    assert _sha(by_state[CardState.TRIGGERED]) == BASE_TRIGGERED_ARTICLE_SHA256, _sha(by_state[CardState.TRIGGERED])
    assert _sha(by_state[CardState.FILLED]) == BASE_FILLED_ARTICLE_SHA256, _sha(by_state[CardState.FILLED])
    ladder = page[page.index('id="ladder-layer"') : page.index('id="pool-layer"')]
    terminal = ladder[ladder.index('<details class="terminal"') :]
    assert _sha(terminal) == BASE_TERMINAL_SHA256, _sha(terminal)


def _sheet_card(state):
    return {"id": 9, "state": state, "ticker": "TEST", "grade": "A", "direction": "long", "shares": 100,
            "session": "RTH", "stop": Decimal("9.90"), "origin": "radar", "account_mode": "live"}


def test_the_sheet_keeps_its_arm_and_disarm_buttons():
    watch = web_module._card_controls(_sheet_card("WATCH"))
    assert (
        '<form method="post" action="/card/9/move" style="display:inline">'
        '<input type="hidden" name="to" value="ARMED"><input type="hidden" name="reason" value="">'
        '<button type="submit">ARM</button></form>'
    ) in watch
    armed = web_module._card_controls(_sheet_card("ARMED"))
    assert (
        '<form method="post" action="/card/9/move" style="display:inline">'
        '<input type="hidden" name="to" value="WATCH"><input type="hidden" name="reason" value="">'
        '<button type="submit" class="danger" onclick="return askReason(this,\'DISARM\')">DISARM</button></form>'
    ) in armed
    assert "/radar/card/" not in watch + armed


# ---------------------------------------------------------------------
# JavaScript: fetch POST only, focus law
# ---------------------------------------------------------------------


def test_panel_javascript_posts_through_fetch_only_to_the_allowlisted_routes():
    source = panel.PANEL_JS
    assert "method:'POST'" in source
    for route in ("/radar/card/'+", "/key", "/dot/", "/promote", "/release"):
        assert route in source
    for forbidden in ("alert(", "confirm(", "prompt(", ".focus(", "autofocus", "<form", "XMLHttpRequest",
                      "location.reload", "submit("):
        assert forbidden not in source


def test_rendered_page_with_cards_keeps_the_focus_law(evaluated):
    rendered = panel.render_ladder(_ladder(evaluated["rows"])).lower()
    for forbidden in ("<form", 'method="post"', "alert(", "prompt(", "confirm(", ".focus(", "autofocus",
                      'http-equiv="refresh"'):
        assert forbidden not in rendered


# ---------------------------------------------------------------------
# routes: the explicit POST allowlist, and the GET sentinels
# ---------------------------------------------------------------------

POST_ALLOWLIST = {
    "/size", "/fill", "/attest", "/card/{card_id}/move", "/card/{card_id}/stop",
    "/radar/card/{card_id}/key", "/radar/card/{card_id}/dot/{factor}",
    "/radar/card/{card_id}/promote", "/radar/card/{card_id}/release",
    "/settings/daily", "/settings/daily/apply",
    "/drc/import", "/drc/no-trade", "/drc/scan",  # DRC D2-4 (the /drc import page)
    "/drc/state-book", "/drc/resolve",  # DRC K3-9 (his statements, inside D2's block)
    # voice V1 (FINAL §9): the widget's turn and its Confirm / Cancel taps
    "/voice/turn", "/voice/confirm", "/voice/cancel",
    # S3 exits C3 (v3 §2 / §3 / §5): the trade taps, one block after /release
    "/radar/card/{card_id}/triggered", "/radar/card/{card_id}/fill", "/radar/card/{card_id}/pass",
    "/radar/card/{card_id}/exit", "/radar/card/{card_id}/held", "/radar/card/{card_id}/correct",
    "/radar/card/{card_id}/stop", "/radar/card/{card_id}/stop/reset",
    "/radar/card/{card_id}/arm", "/radar/card/{card_id}/disarm",  # R627: ARM / DISARM, after /stop/reset
}
GET_ONLY = {"/", "/radar", "/api/radar/pool", "/api/health", "/api/prefill", "/drc"}


def test_post_routes_are_exactly_the_explicit_allowlist():
    posts, gets = set(), {}
    for route in web_module.app.routes:
        methods = getattr(route, "methods", None) or set()
        if "POST" in methods:
            posts.add(route.path)
        if route.path in GET_ONLY:
            gets[route.path] = methods
    assert posts == POST_ALLOWLIST
    for path in GET_ONLY:
        assert gets[path] <= {"GET", "HEAD"}, (path, gets[path])
    radar_posts = {p for p in posts if "radar" in p}
    assert all(p.startswith("/radar/card/{card_id}/") for p in radar_posts)


def _sentinels(monkeypatch):
    for name in ("_render", "_daymode_state", "_open_cards_section", "_read_back_note_attestation",
                 "_write_daymode_note"):
        monkeypatch.setattr(
            web_module, name,
            lambda *args, _name=name, **kwargs: (_ for _ in ()).throw(AssertionError(f"sentinel {_name}")),
        )
    for cls, method in ((web_module.DayModeStore, "ensure_schema"), (web_module.CardStore, "ensure_schema"),
                        (web_module.AsetStore, "ensure_schema")):
        monkeypatch.setattr(
            cls, method,
            lambda *args, _name=f"{cls.__name__}.{method}", **kwargs: (_ for _ in ()).throw(AssertionError(_name)),
        )


def test_api_radar_pool_get_never_touches_sheet_write_schema_or_attestation_helpers(monkeypatch, evaluated):
    calls = []
    sentinel_view = SimpleNamespace(pool=SimpleNamespace())
    monkeypatch.setattr(web_module, "now_utc", lambda: SCAN0 + timedelta(seconds=300))
    monkeypatch.setattr(web_module, "build_radar_panel", lambda **kw: calls.append(kw) or sentinel_view)
    monkeypatch.setattr(web_module, "pool_api_payload", lambda pool: {"pool": "ok", "html": "<section></section>"})
    _sentinels(monkeypatch)
    client = TestClient(web_module.app)
    response = client.get("/api/radar/pool?since=2026-01-06T16:00:00%2B00:00")
    assert response.status_code == 200, response.text
    assert response.json() == {"pool": "ok", "html": "<section></section>"}
    assert calls == [{"since": datetime(2026, 1, 6, 16, 0, tzinfo=UTC), "snapshot": False,
                      "now": SCAN0 + timedelta(seconds=300)}]
    assert client.post("/api/radar/pool?since=2026-01-06T16:00:00%2B00:00").status_code == 405


def test_radar_get_with_cards_never_touches_sheet_write_schema_or_attestation_helpers(monkeypatch, evaluated):
    ladder = _ladder(evaluated["rows"])
    pool_view = SimpleNamespace(scan_interval=100)
    view = SimpleNamespace(pool=pool_view, ladder=ladder)
    monkeypatch.setattr(web_module, "build_radar_panel", lambda **kw: view)
    monkeypatch.setattr(web_module, "render_radar_page",
                        lambda v, phone_frame=False: "<html>" + panel.render_ladder(v.ladder) + "</html>")
    _sentinels(monkeypatch)
    response = TestClient(web_module.app).get("/radar")
    assert response.status_code == 200 and "TRADE RADAR" in response.text
    assert TestClient(web_module.app).post("/radar").status_code == 405
