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
from datetime import datetime, timedelta, timezone
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


def _ladder(rows, *, rung="reduced", now=SCAN0 + timedelta(seconds=200)):
    return panel.build_ladder_view(
        card_store=RowStore(rows), settings_store=Settings(SETTINGS_ROWS), clock=session_clock(), now=now,
        tunables_loader=_tunables(), rung_source=lambda instant, cfg: rung,
    )


# ---------------------------------------------------------------------
# the adapter: radar_cards_v rows, never a contract fixture
# ---------------------------------------------------------------------


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
    assert "FILLED" not in rendered.replace('data-state="FILLED"', "")


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
PIN_HEALTHY_POOL_SHA256 = "f2e79add6bc4d4286b381154b071b04ec9e7887467ffd15b0f499e9d62181552"
PIN_HEALTHY_LADDER_SHA256 = "e617c53c1479314b6074de5409f289238479be31fbbd789b4ee19849f55370d7"
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
}
GET_ONLY = {"/", "/radar", "/api/radar/pool", "/api/health", "/api/prefill"}


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
