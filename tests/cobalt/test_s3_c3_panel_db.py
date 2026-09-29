"""S3 exits C3 — the panel end to end on `cobalt_dev` (v3 §2 / §3 / §5;
R67, R38).

With-DB, inside the suite's rolled-back transaction with M1 applied there
(`legs_db_support.apply_0021`), so these hold at `0013` and at `0021`
alike and leave nothing applied (L76). The radar card is the S2-P2
`world` fixture's evaluator card (synthetic ticker `ZZPB`, the hub-cut
real-shape bars), key-tapped and ARMED by his taps; every later move is a
POST through TestClient to the C3 routes, and every "from the rendered
page" value is read out of the ladder's own HTML. The manual card is
`legs_db_support.manual_card` (ticker `TEST`, 10.0000 / 9.9000).

Constructed values only (L32): the last price 5.4800 is set on the test's
own card inside the rolled-back transaction.
"""

from __future__ import annotations

import html as html_lib
import os
import re
from datetime import datetime, timezone
from decimal import Decimal
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from legs_db_support import apply_0021, fill_kwargs, manual_card, patch_daymode
from test_radar_cards_db import SCAN0, TICKER, world  # noqa: F401  (the fixture)

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: 20:30 ET on 2026-09-02 — inside market_reset (the C1 / C2 tests' instant).
RESET = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)
LAST = Decimal("5.4800")
COUNTED = ("aset_sizings", "legs", "card_transitions", "card_stop_edits", "picks")


@pytest.fixture
def panel_world(world, monkeypatch):  # noqa: F811
    from cobalt.aset import web as web_module
    from cobalt.aset.store import AsetStore

    patch_daymode(monkeypatch)
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    aset = AsetStore("cobalt_dev")
    aset.ensure_schema()
    apply_0021(aset)
    world["aset"] = aset
    world["client"] = TestClient(web_module.app)
    return world


def _armed(world) -> int:  # noqa: F811
    from cobalt.aset.engine import size_at_key
    from cobalt.aset.models import Direction, Grade
    from cobalt.cards import Actor, CardState
    from cobalt.settings.models import TraderSettings

    card_id = world["scan"](SCAN0).created[0]
    cards = world["cards"]
    trader = TraderSettings.from_db(world["settings"])
    record = cards.radar_card(card_id)
    sizing = size_at_key(
        Grade.A_PLUS, ticker=TICKER, entry=record["entry"], stop=record["stop"],
        direction=Direction(record["direction"]), sheet_modes=trader.sheet_modes, sheet="half",
        enabled=trader.daymode.enabled_grades_for("reduced"), max_stop_distance_pct=Decimal("10"),
    )
    cards.tap_key(card_id, sizing)
    cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
    with cards._connect() as conn:
        conn.execute("UPDATE aset_sizings SET last_price = %s WHERE id = %s", (LAST, card_id))
    return card_id


def _filled(world, *, shares: int = 100, price: str = "5.4800") -> int:  # noqa: F811
    card_id = _armed(world)
    client = world["client"]
    assert client.post(f"/radar/card/{card_id}/triggered").status_code == 200
    response = client.post(f"/radar/card/{card_id}/fill",
                           data={"price": price, "shares": str(shares), "prefill": str(LAST)})
    assert response.status_code == 200, response.text
    return card_id


def _render(world) -> str:  # noqa: F811
    from cobalt.aset import radar_panel as panel
    from cobalt.session import clock, session_clock

    view = panel.build_ladder_view(
        card_store=world["cards"], settings_store=world["settings"], clock=session_clock(),
        now=clock.now_utc(), rung_source=lambda _at, _cfg: "reduced",
    )
    return panel.render_ladder(view)


def _fragment(rendered: str, card_id: int) -> str:
    """The card's ladder item (active) and / or its terminal legs block."""
    starts = [m.start() for m in re.finditer(
        rf'<(?:article|div) class="(?:ladder-item[^"]*|terminal-legs)" data-card-id="{card_id}"', rendered)]
    if not starts:
        raise AssertionError(f"card {card_id} not rendered")
    parts = []
    for start in starts:
        stop = re.search(r'<article |<div class="terminal-row"|<div class="terminal-legs"|</section>',
                         rendered[start + 1:])
        parts.append(rendered[start:start + 1 + stop.start() if stop else len(rendered)])
    return "".join(parts)


def _form(fragment: str, path: str, **match) -> dict:
    """The fields one rendered tap posts to `path` (`/radar/card/<id>/<tap>`)
    — the panel's `<div data-card-tap>` (posted by the panel script) or the
    sheet's `<form>`; an unticked checkbox posts nothing, as in both."""
    card_id, tail = re.fullmatch(r"/radar/card/(\d+)(/.+)", path).groups()
    blocks = re.findall(
        rf'<(div|form) class="s3-form[^"]*" data-card-id="{card_id}" data-path="{re.escape(tail)}"[^>]*>(.*?)</\1>',
        fragment, re.S,
    )
    for _tag, form in blocks:
        fields = {}
        for tag in re.findall(r"<input[^>]*>", form):
            if 'type="checkbox"' in tag:
                continue
            name = re.search(r'name="([^"]+)"', tag)
            value = re.search(r'value="([^"]*)"', tag)
            if name:
                fields[name.group(1)] = html_lib.unescape(value.group(1)) if value else ""
        if all(fields.get(k) == v for k, v in match.items()):
            return fields
    raise AssertionError(f"no form {path} {match} in the fragment")


def _history(world, card_id):  # noqa: F811
    return world["cards"].history(card_id)


def _legs(world, card_id):  # noqa: F811
    with world["aset"]._connect() as conn:
        cur = conn.execute("SELECT * FROM legs_current_v WHERE card_id = %s ORDER BY seq", (card_id,))
        return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]


def _running(world, card_id):  # noqa: F811
    from cobalt.cards import legs

    return legs.read_position(card_id).running.shares


def _counts(world) -> dict:  # noqa: F811
    with world["aset"]._connect() as conn:
        return {t: conn.execute(f"SELECT count(*) FROM {t}").fetchone()[0] for t in COUNTED}


# ---------------------------------------------------------------------
# TRIGGERED, FILLED
# ---------------------------------------------------------------------


def test_the_triggered_tap_writes_one_transition_by_you_with_the_last_price(panel_world):
    card_id = _armed(panel_world)
    before = len(_history(panel_world, card_id))
    response = panel_world["client"].post(f"/radar/card/{card_id}/triggered")
    assert response.status_code == 200, response.text
    history = _history(panel_world, card_id)
    assert len(history) == before + 1
    last = history[-1]
    assert (last["from_state"], last["to_state"], last["actor"]) == ("ARMED", "TRIGGERED", "you")
    assert last["evidence"]["last_price"] == str(LAST) and last["evidence"]["last_price_at"] is None


def test_the_triggered_card_renders_its_fill_form_prefilled_from_the_last_price(panel_world):
    card_id = _armed(panel_world)
    panel_world["client"].post(f"/radar/card/{card_id}/triggered")
    fields = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/fill")
    assert fields["price"] == str(LAST) and fields["prefill"] == str(LAST)


def test_a_fill_from_the_untouched_prefill_is_an_estimated_last_poll_entry_leg(panel_world):
    card_id = _armed(panel_world)
    client = panel_world["client"]
    client.post(f"/radar/card/{card_id}/triggered")
    fields = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/fill")
    response = client.post(f"/radar/card/{card_id}/fill", data=fields)
    assert response.status_code == 200, response.text
    (entry,) = _legs(panel_world, card_id)
    assert (entry["kind"], entry["price_source"], entry["flag"], entry["source"]) == (
        "entry", "last_poll", "estimated", "panel")
    assert entry["price"] == LAST
    assert panel_world["cards"].state_of(card_id).value == "FILLED"


def test_a_fill_with_an_edited_price_is_a_typed_confirmed_entry_leg(panel_world):
    card_id = _filled(panel_world, price="5.4700")
    (entry,) = _legs(panel_world, card_id)
    assert (entry["price"], entry["price_source"], entry["flag"]) == (Decimal("5.4700"), "typed", "confirmed")


def test_a_fill_with_no_price_is_refused_and_nothing_is_written(panel_world):
    card_id = _armed(panel_world)
    client = panel_world["client"]
    client.post(f"/radar/card/{card_id}/triggered")
    before = _counts(panel_world)
    response = client.post(f"/radar/card/{card_id}/fill", data={"price": "", "shares": "100", "prefill": ""})
    assert response.status_code == 422
    assert response.json()["reason"].startswith(f"REFUSED card {card_id}: a fill with no price.")
    assert _counts(panel_world) == before


def test_pass_moves_a_triggered_card_to_passed(panel_world):
    card_id = _armed(panel_world)
    client = panel_world["client"]
    client.post(f"/radar/card/{card_id}/triggered")
    assert client.post(f"/radar/card/{card_id}/pass").status_code == 200
    last = _history(panel_world, card_id)[-1]
    assert (last["to_state"], last["actor"]) == ("PASSED", "you")


# ---------------------------------------------------------------------
# IN-TRADE: exits from the rendered page
# ---------------------------------------------------------------------


def test_a_half_from_the_rendered_page_then_the_same_half_again_is_refused(panel_world):
    card_id = _filled(panel_world, shares=100)
    client = panel_world["client"]
    fragment = _fragment(_render(panel_world), card_id)
    half = _form(fragment, f"/radar/card/{card_id}/exit", preset="half")
    assert half["running_before"] == "100"
    assert client.post(f"/radar/card/{card_id}/exit", data=half).status_code == 200
    assert _running(panel_world, card_id) == 50
    again = client.post(f"/radar/card/{card_id}/exit", data=half)
    assert again.status_code == 409
    assert again.json()["reason"] == "REFUSED: screen said 100, now 50 — tap again"
    assert len([l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]) == 1


def test_an_untouched_flat_is_estimated_closes_the_card_and_is_listed_for_correction(panel_world):
    card_id = _filled(panel_world, shares=100)
    client = panel_world["client"]
    flat = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/exit", preset="flat")
    assert client.post(f"/radar/card/{card_id}/exit", data=flat).status_code == 200
    exits = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert [(l["flag"], l["price_source"], l["shares"]) for l in exits] == [("estimated", "last_poll", 100)]
    assert panel_world["cards"].state_of(card_id).value == "CLOSED"
    listed = _fragment(_render(panel_world), card_id)
    correct = _form(listed, f"/radar/card/{card_id}/correct", leg_id=str(exits[0]["id"]))
    # the ✓ on the listed leg: a correction with his typed price → confirmed
    correct["price"] = "5.3900"
    response = client.post(f"/radar/card/{card_id}/correct", data=correct)
    assert response.status_code == 200, response.text
    (fixed,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (fixed["flag"], fixed["price_source"], fixed["price"], fixed["corrects"]) == (
        "confirmed", "typed", Decimal("5.3900"), exits[0]["id"])


def test_a_flat_with_the_check_and_a_typed_price_is_confirmed_and_closes(panel_world):
    card_id = _filled(panel_world, shares=100)
    flat = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/exit", preset="flat")
    flat.update(price="5.3800", confirm="1")
    response = panel_world["client"].post(f"/radar/card/{card_id}/exit", data=flat)
    assert response.status_code == 200, response.text
    (leg,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (leg["flag"], leg["price_source"], leg["price"]) == ("confirmed", "typed", Decimal("5.3800"))
    assert panel_world["cards"].state_of(card_id).value == "CLOSED"
    assert _history(panel_world, card_id)[-1]["evidence"]["leg_id"] == leg["id"]


def test_holding_50_is_the_entry_correction_and_running_is_50(panel_world):
    card_id = _filled(panel_world, shares=100)
    fields = _form(_fragment(_render(panel_world), card_id), f"/radar/card/{card_id}/held")
    fields["held"] = "50"
    response = panel_world["client"].post(f"/radar/card/{card_id}/held", data=fields)
    assert response.status_code == 200, response.text
    entry = next(l for l in _legs(panel_world, card_id) if l["kind"] == "entry")
    assert (entry["held_stated"], entry["shares"], entry["flag"]) == (50, 50, "confirmed")
    assert _running(panel_world, card_id) == 50


def test_a_correction_of_an_estimated_leg_is_confirmed(panel_world):
    card_id = _filled(panel_world, shares=100, price=str(LAST))  # untouched prefill → estimated entry
    fragment = _fragment(_render(panel_world), card_id)
    (entry,) = _legs(panel_world, card_id)
    fields = _form(fragment, f"/radar/card/{card_id}/correct", leg_id=str(entry["id"]))
    fields["price"] = "5.4600"
    response = panel_world["client"].post(f"/radar/card/{card_id}/correct", data=fields)
    assert response.status_code == 200, response.text
    (fixed,) = _legs(panel_world, card_id)
    assert (fixed["flag"], fixed["price_source"], fixed["price"]) == ("confirmed", "typed", Decimal("5.4600"))


# ---------------------------------------------------------------------
# the stop: YOURS, Cobalt's beside it, ↺
# ---------------------------------------------------------------------


def test_a_stop_edit_shows_yours_and_the_delta_and_the_reset_gives_it_back(panel_world):
    card_id = _filled(panel_world, shares=100)
    client = panel_world["client"]
    with panel_world["aset"]._connect() as conn:
        (structural,) = conn.execute("SELECT structural_stop FROM aset_sizings WHERE id = %s", (card_id,)).fetchone()
    assert structural is not None
    assert client.post(f"/radar/card/{card_id}/stop", data={"to_stop": "5.7000"}).status_code == 200
    assert panel_world["cards"].stop_owner(card_id) == "yours"
    fragment = _fragment(_render(panel_world), card_id)
    assert '<span class="yours">YOURS</span>' in fragment
    assert f"Δ {Decimal('5.7000') - structural}" in fragment
    assert f"Cobalt stop {structural}" in fragment and f"↺ {structural}" in fragment
    response = client.post(f"/radar/card/{card_id}/stop/reset", data={})
    assert response.status_code == 200, response.text
    assert panel_world["cards"].stop_owner(card_id) == "cobalt"
    with panel_world["aset"]._connect() as conn:
        kind, to_stop = conn.execute(
            "SELECT kind, to_stop FROM card_stop_edits WHERE card_id = %s ORDER BY id DESC LIMIT 1", (card_id,)
        ).fetchone()
    assert (kind, to_stop) == ("reset", structural)
    fragment = _fragment(_render(panel_world), card_id)
    assert '<span class="yours">YOURS</span>' not in fragment and f"Cobalt stop {structural}" in fragment


def test_p_missing_renders_the_re_read_stop_line(panel_world):
    card_id = _filled(panel_world, shares=100)  # the world's settings carry no fills.drift_warning_pct
    fragment = _fragment(_render(panel_world), card_id)
    assert "RE-READ STOP — setting fills.drift_warning_pct missing, warning not evaluated" in fragment


def test_a_manual_card_gets_its_in_trade_controls_on_the_sheet_and_no_reset(panel_world):
    from cobalt.aset import web as web_module

    aset = panel_world["aset"]
    card_id = manual_card(aset)
    aset.mark_filled(card_id, **fill_kwargs(price="10.10", shares=100, p=20))
    sheet = web_module._open_cards_section()
    start = sheet.index(f"#{card_id} ·")
    end = sheet.find('<div class="crow">', start)
    fragment = sheet[start:] if end < 0 else sheet[start:end]
    fields = _form(fragment, f"/radar/card/{card_id}/exit", preset="half")
    assert fields["source"] == "sheet" and fields["running_before"] == "100"
    # the sheet's own wording ("↺ reset = re-enter the card stop", v3 §5) stays on
    # its row; the IN-TRADE block renders no ↺ control and nothing posts a reset
    in_trade = fragment[fragment.index('<div class="in-trade"'):]
    assert "↺" not in in_trade and "/stop/reset" not in fragment
    assert "Cobalt stop NULL — no Cobalt stop" in in_trade
    refused = panel_world["client"].post(f"/radar/card/{card_id}/stop/reset", data={"source": "sheet"})
    assert refused.status_code == 409
    assert "this card has none (a manual card) — no Cobalt stop to reset to" in html_lib.unescape(refused.text)
    # the sheet's own half, through the same route
    response = panel_world["client"].post(f"/radar/card/{card_id}/exit", data={**fields, "price": "10.20"})
    assert response.status_code == 200, response.text
    (leg,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (leg["source"], leg["shares"], leg["flag"]) == ("sheet", 50, "confirmed")


# ---------------------------------------------------------------------
# nothing written where nothing may be
# ---------------------------------------------------------------------


def test_market_reset_refuses_every_post_and_writes_nothing(panel_world, monkeypatch):
    from cobalt.session import clock

    card_id = _filled(panel_world, shares=100)
    entry = _legs(panel_world, card_id)[0]
    before = _counts(panel_world)
    monkeypatch.setattr(clock, "now_utc", lambda: RESET)
    client = panel_world["client"]
    posts = [
        ("triggered", {}), ("fill", {"price": "5.48", "shares": "10", "prefill": "5.48"}), ("pass", {}),
        ("exit", {"preset": "half", "price": "5.40", "prefill": "5.40", "running_before": "100"}),
        ("held", {"held": "50"}), ("correct", {"leg_id": str(entry["id"]), "price": "5.39"}),
        ("stop", {"to_stop": "5.70"}), ("stop/reset", {}),
    ]
    for path, data in posts:
        response = client.post(f"/radar/card/{card_id}/{path}", data=data)
        assert response.status_code == 409, (path, response.text)
        assert "inside MARKET RESET" in response.json()["reason"], path
    assert _counts(panel_world) == before


def test_get_radar_and_the_in_trade_render_write_nothing(panel_world):
    card_id = _filled(panel_world, shares=100)
    before = _counts(panel_world)
    assert panel_world["client"].get("/radar").status_code == 200
    fragment = _fragment(_render(panel_world), card_id)
    assert "running 100 sh" in fragment
    assert _counts(panel_world) == before


# ---------------------------------------------------------------------
# C3 fix r1 — F2: `/correct` binds the URL's card; F3: the sheet lists a
# CLOSED manual card's estimated leg
# ---------------------------------------------------------------------


def _filled_manual(world) -> int:  # noqa: F811
    """A manual card filled through THE fill (100 sh @ 10.10, P = 20)."""
    aset = world["aset"]
    card_id = manual_card(aset)
    aset.mark_filled(card_id, **fill_kwargs(price="10.10", shares=100, p=20))
    return card_id


def _sheet_flat(world, card_id: int, *, price: str = "10.20"):  # noqa: F811
    """A flat from the sheet with a typed price and NO ✓ — `estimated`."""
    return world["client"].post(f"/radar/card/{card_id}/exit", data={
        "source": "sheet", "preset": "flat", "price": price, "prefill": "", "running_before": "100",
    })


def test_a_correction_posted_on_one_card_never_writes_another_cards_leg(panel_world):
    card_a = _filled(panel_world, shares=100)
    card_b = _filled_manual(panel_world)
    flat = _sheet_flat(panel_world, card_b)
    assert flat.status_code == 200, flat.text
    (b_exit,) = [l for l in _legs(panel_world, card_b) if l["kind"] == "exit"]
    assert b_exit["flag"] == "estimated"
    legs_b, before = _legs(panel_world, card_b), _counts(panel_world)
    response = panel_world["client"].post(f"/radar/card/{card_a}/correct",
                                          data={"leg_id": str(b_exit["id"]), "price": "10.2500"})
    assert response.status_code == 422, (response.status_code, response.text[:300], _legs(panel_world, card_b))
    assert "is not a current leg of card" in response.json()["reason"]
    assert _legs(panel_world, card_b) == legs_b
    assert _counts(panel_world) == before


def test_a_sheet_flat_without_the_check_closes_and_is_listed_for_correction(panel_world, monkeypatch):
    from cobalt.aset import web as web_module

    # C1's /fill, with its daily-note write stubbed (no vault write in a test, L28)
    monkeypatch.setattr(web_module, "save_fill_update",
                        lambda *a, **k: ("/dev/null", SimpleNamespace(action="stubbed")))
    client = panel_world["client"]
    card_id = manual_card(panel_world["aset"])
    filled = client.post("/fill", data={"card_row_id": str(card_id), "orig_timestamp": "2026-09-03T10:05:00-04:00",
                                        "actual_fill": "10.10", "fill_shares": "100"})
    assert filled.status_code == 200 and panel_world["cards"].state_of(card_id).value == "FILLED", filled.text[:500]
    flat = _sheet_flat(panel_world, card_id)
    assert flat.status_code == 200, flat.text[:500]
    assert panel_world["cards"].state_of(card_id).value == "CLOSED"
    (leg,) = [l for l in _legs(panel_world, card_id) if l["kind"] == "exit"]
    assert (leg["flag"], leg["price_source"]) == ("estimated", "typed")
    page = client.get("/")
    assert page.status_code == 200
    fields = _form(page.text, f"/radar/card/{card_id}/correct", leg_id=str(leg["id"]))
    assert fields["source"] == "sheet"


# ---------------------------------------------------------------------
# C3 fix r1 — RUN R1 / RUN R2 (L70): run, never argued. They PRINT what
# happened and assert NOTHING about the outcome.
# ---------------------------------------------------------------------


def _day_modes(world) -> int:  # noqa: F811
    with world["aset"]._connect() as conn:
        return conn.execute("SELECT count(*) FROM day_modes").fetchone()[0]


def test_run_r1_a_nan_or_negative_price_posted_to_the_taps(panel_world):
    from cobalt.aset import web as web_module

    client = TestClient(web_module.app, raise_server_exceptions=False)
    radar = _filled(panel_world, shares=100, price=str(LAST))  # the untouched prefill → an estimated entry
    half = _form(_fragment(_render(panel_world), radar), f"/radar/card/{radar}/exit", preset="half")
    (entry,) = _legs(panel_world, radar)
    triggered = manual_card(panel_world["aset"])  # TRIGGERED
    posts = [
        (f"/radar/card/{radar}/exit", {**half, "price": "NaN"}),
        (f"/radar/card/{radar}/exit", {**half, "price": "-1"}),
        (f"/radar/card/{triggered}/fill", {"price": "NaN", "shares": "100", "prefill": ""}),
        (f"/radar/card/{radar}/correct", {"leg_id": str(entry["id"]), "price": "-1"}),
    ]
    print(f"\nRUN R1 · radar card {radar} (FILLED, entry leg {entry['id']} estimated) · manual card {triggered} "
          f"(TRIGGERED) · counted {COUNTED} (legs among them)")
    for path, data in posts:
        before = _counts(panel_world)
        response = client.post(path, data=data)
        after = _counts(panel_world)
        print(f"R1 POST {path} price={data['price']!r} → {response.status_code} · body[:200]={response.text[:200]!r}")
        print(f"R1   counts before {before} · after {after} · legs {before['legs']} → {after['legs']}")
    print(f"R1 legs of {radar} now: {[(l['id'], l['kind'], str(l['price']), l['flag']) for l in _legs(panel_world, radar)]}")
    print(f"R1 state of {triggered} now: {panel_world['cards'].state_of(triggered).value}")


def test_run_r2_the_sheet_get_and_the_radar_get_count_every_row(panel_world):
    from cobalt.aset import web as web_module

    client = TestClient(web_module.app, raise_server_exceptions=False)
    live = _filled_manual(panel_world)
    closed = _filled_manual(panel_world)
    flat = _sheet_flat(panel_world, closed)
    print(f"\nRUN R2 · manual card {live} FILLED · manual card {closed} after a sheet flat without ✓: "
          f"{flat.status_code}, {panel_world['cards'].state_of(closed).value}, legs "
          f"{[(l['kind'], l['flag']) for l in _legs(panel_world, closed)]}")
    before, days_before = _counts(panel_world), _day_modes(panel_world)
    sheet = client.get("/")
    after_sheet, days_sheet = _counts(panel_world), _day_modes(panel_world)
    radar = client.get("/radar")
    after_radar, days_radar = _counts(panel_world), _day_modes(panel_world)
    print(f"R2 GET / → {sheet.status_code} · carries /radar/card/{closed}/correct: "
          f"{f'/radar/card/{closed}/correct' in sheet.text} · carries /radar/card/{live}/exit: "
          f"{f'/radar/card/{live}/exit' in sheet.text}")
    print(f"R2   counts before {before} · after GET / {after_sheet} · legs {before['legs']} → {after_sheet['legs']}")
    print(f"R2   day_modes before {days_before} · after GET / {days_sheet}")
    print(f"R2 GET /radar → {radar.status_code} · page carries FAILED: {'FAILED' in radar.text}")
    print(f"R2   counts after GET /radar {after_radar} · legs {after_radar['legs']} · day_modes {days_radar}")
