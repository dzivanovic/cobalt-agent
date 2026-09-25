"""C7 — tools, code templates, the figures check, hard refusals (FINAL §2.4).

READ tools return stored data and the reply is rendered by a CODE
TEMPLATE; `radar.pool` goes through the very function the
`/api/radar/pool` route is; nothing calls `/size` or the sizer or
computes a score / rank / grade / size. The figures check [F-05] drops a
`say` whose numbers are not in the tool result. Orders / platforms →
`refuse` with ONE fixed sentence; settings / rules / strategy →
`unsupported` naming the owner's command ([R3F-11]); anything else →
`unsupported` "I can't do that yet". Constructed values only (L32).
"""

from __future__ import annotations

import inspect
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.voice import registry
from cobalt.voice import tools as tl
from cobalt.voice.models import Plan

AGENT = registry.load_agent()

CARD = {"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "entry": Decimal("4.6000"),
        "stop": Decimal("4.4000"), "shares": 250, "grade": "B"}
CARD2 = {"id": 12, "ticker": "QRS", "direction": "short", "state": "FILLED", "entry": Decimal("12.2000"),
         "stop": Decimal("12.6000"), "shares": None, "grade": "A"}


def test_the_code_implements_exactly_the_registry_tools():
    assert set(tl.READ_TOOLS) | set(tl.ACT_TOOLS) == registry.KNOWN_TOOLS
    assert set(AGENT.tools) <= registry.KNOWN_TOOLS


# --- templates ------------------------------------------------------------------


def test_open_cards_template():
    assert tl.render_open_cards([CARD, CARD2]) == (
        "You have 2 open cards: XYZ long, WATCH, stop 4.40; QRS short, FILLED, stop 12.60.")
    assert tl.render_open_cards([]) == "You have no open cards."
    assert tl.render_open_cards([CARD]).startswith("You have 1 open card:")


def test_numbers_template_reads_stored_fields_only():
    assert tl.render_numbers(CARD) == "XYZ long, card 11, WATCH: entry 4.60, stop 4.40, 250 shares, grade B."
    assert tl.render_numbers(CARD2) == "QRS short, card 12, FILLED: entry 12.20, stop 12.60, unsized, grade A."


def _pool(current, stale=False):
    return {"pool": {"pool_key": "constructed", "stale": stale, "members": len(current), "cap": 20,
                     "current": [{"ticker": t, "position": i + 1} for i, t in enumerate(current)]},
            "html": "<ignored/>"}


def test_pool_template():
    assert tl.render_pool(_pool(["XYZ", "QRS", "LMN"])) == "Radar pool: 3 names — XYZ, QRS, LMN."
    assert tl.render_pool(_pool([])) == "The radar pool is empty."
    assert tl.render_pool(_pool(["XYZ"], stale=True)) == "Radar pool (STALE): 1 name — XYZ."


def test_pool_template_names_at_most_ten():
    names = [f"T{i:02d}" for i in range(14)]
    out = tl.render_pool(_pool(names))
    assert out.startswith("Radar pool: 14 names — T00, ") and out.endswith("and 4 more.")


def test_radar_pool_goes_through_the_route_function_itself(monkeypatch):
    import cobalt.aset.web as web

    calls = []

    def fake_route(since=None):
        calls.append(since)
        return _pool(["XYZ"])

    monkeypatch.setattr(web, "api_radar_pool", fake_route)
    assert tl.read_pool() == _pool(["XYZ"])
    assert calls == [None]


def test_a_failed_pool_read_is_named(monkeypatch):
    import cobalt.aset.web as web
    from fastapi.responses import JSONResponse

    monkeypatch.setattr(web, "api_radar_pool", lambda since=None: JSONResponse(
        status_code=503, content={"status": "FAILED", "error": "constructed radar failure"}))
    with pytest.raises(tl.ToolReadFailed) as e:
        tl.read_pool()
    assert "constructed radar failure" in str(e.value)


def test_no_tool_reaches_the_sizer_or_computes_a_score():
    src = inspect.getsource(tl).replace(tl.__doc__, "")  # code, not the module docstring
    for forbidden in ("compute_sizing", "size_at_key", "recompute_for_stop", "/size", "card_score",
                      "rank_value", "compute_fill"):
        assert forbidden not in src, forbidden


# --- the figures check [F-05] ------------------------------------------------------


@pytest.mark.parametrize("say,result,ok", [
    ("Your XYZ stop is 4.40.", "stop 4.40", True),
    ("Your XYZ stop is 4.45.", "stop 4.40", False),
    ("You have 2 cards.", "You have 2 open cards", True),
    ("Stop is 4.4.", "stop 4.40", False),          # not the same token
    ("Stop is 440.", "stop 4.40", False),          # per-character digits do not pass
    ("Stop is 4.", "stop 4.40", False),
    ("All good.", "anything", True),
    ("Twelve cards.", "You have 2 open cards", True),  # a number word is not a numeric token
])
def test_figures_check(say, result, ok):
    assert tl.figures_ok(say, result) is ok


def test_a_failing_say_is_dropped_and_the_template_spoken():
    assert tl.compose_reply("You have 9 cards.", "You have 2 open cards: …") == "You have 2 open cards: …"
    assert tl.compose_reply("Here you go.", "You have 2 open cards: …") == "Here you go. You have 2 open cards: …"
    assert tl.compose_reply(None, "T.") == "T."


# --- hard refusals ------------------------------------------------------------------


def _plan(kind, tool=None):
    return Plan(kind=kind, tool=tool, args={}, say=None)


@pytest.mark.parametrize("text", [
    "buy 100 XYZ", "sell half my QRS", "cancel my order on XYZ", "short QRS at market",
    "cover my XYZ position", "place a limit order for XYZ at 4.50", "send a market order", "flatten XYZ",
])
def test_orders_are_refused_whatever_the_plan_says(text):
    for plan in (_plan("act", "cards.set_stop"), _plan("answer", "cards.open"), _plan("clarify")):
        r = tl.code_refusal(text, plan, AGENT)
        assert r is not None and r.kind == "refuse" and r.reply == tl.REFUSE_SENTENCE


@pytest.mark.parametrize("text", [
    "log into Lightspeed", "open DAS and buy 100 XYZ", "send it to TradeStation", "open CenterPoint",
    "switch my trading platform", "short 100 QRS", "go long XYZ", "go short QRS", "exit my XYZ position",
    "close my position in XYZ", "get me out of QRS", "take profits on XYZ", "scale out of QRS",
])
@pytest.mark.parametrize("kind", ["answer", "act"])
def test_platform_and_order_phrasings_are_refused_whatever_the_plan(text, kind):
    """A1 (voice-v1-check-a-2026-09-24.md FOR THE CLASSIFIER 1; FINAL :84 HARD
    REFUSALS — "touches his trading platform"): platform names and order
    verbs are refused by code whatever the Plan's kind. `open DAS and buy 100
    XYZ` is the control (refused through `buy` before this fix)."""
    plan = _plan("answer", "cards.open") if kind == "answer" else _plan("act", "cards.set_stop")
    r = tl.code_refusal(text, plan, AGENT)
    assert r is not None and r.kind == "refuse" and r.reply == tl.REFUSE_SENTENCE


@pytest.mark.parametrize("text", ["exit QRS", "get out of QRS", "close out QRS", "short QRS"])
@pytest.mark.parametrize("kind", ["answer", "act"])
def test_a_bare_exit_close_or_short_of_a_ticker_is_refused_whatever_the_plan(text, kind):
    """A1, fix r2 (voice-v1-fix-r1-check-2026-09-24.md:140, :157; FINAL :84
    HARD REFUSALS — "anything that places, changes or cancels an order"; the
    `_ORDER` comment's own "never a bare exit/close"): a bare exit / close /
    close out / get out of / share-count-free short OF A TICKER is an order,
    refused by code whatever the Plan's kind."""
    plan = _plan("answer", "cards.open") if kind == "answer" else _plan("act", "cards.set_stop")
    r = tl.code_refusal(text, plan, AGENT)
    assert r is not None and r.kind == "refuse" and r.reply == tl.REFUSE_SENTENCE


@pytest.mark.parametrize("text", [
    "move the stop on the XYZ short to 4.50", "what is the stop on my long XYZ card", "read my open cards",
    "what did the pool close at", "how many shares on the second XYZ card",
    # A1, fix r2 (voice-v1-fix-r1-check-2026-09-24.md:140): the short-side
    # mirror of the long case above — a card side stays readable.
    "what is the stop on my short XYZ card",
])
def test_card_sides_and_price_fields_stay_readable(text):
    """A1's NOT-refused set: a card side (`long` / `short`) and a price field
    (`close`) are never refused on their own."""
    for plan in (_plan("answer", "cards.open"), _plan("act", "cards.set_stop")):
        assert tl.code_refusal(text, plan, AGENT) is None


@pytest.mark.parametrize("text", [
    "set my max risk to 200", "change my daily stop to 500", "enable grade C",
    "change the pullback rule to two legs", "turn off the radar volume filter",
    "update my strategy settings", "raise the risk per trade",
])
def test_trading_logic_is_unsupported_naming_the_owners_command(text):
    r = tl.code_refusal(text, _plan("act", "cards.set_stop"), AGENT)
    assert r is not None and r.kind == "unsupported"
    assert "cobalt settings load --card <file> --sha256 <hash> --apply" in r.reply
    assert r.reason == "trading_logic"


@pytest.mark.parametrize("text", [
    "move the stop on XYZ to 4.50", "what are my open cards", "what's my stop on XYZ",
    "move the stop on the XYZ short to 4.95", "what is on radar", "yes", "no",
])
def test_ordinary_requests_are_not_refused(text):
    assert tl.code_refusal(text, _plan("act", "cards.set_stop"), AGENT) is None


def test_a_trading_logic_tool_is_never_executed():
    agent = AGENT.model_copy(deep=True)
    agent.tools["cards.set_stop"].trading_logic = True
    r = tl.code_refusal("move the stop on XYZ to 4.50", _plan("act", "cards.set_stop"), agent)
    assert r is not None and r.kind == "unsupported" and r.reason == "trading_logic"


def test_the_plan_kinds_refuse_and_unsupported_get_fixed_sentences():
    r = tl.code_refusal("do the thing", _plan("refuse"), AGENT)
    assert r.kind == "refuse" and r.reply == tl.REFUSE_SENTENCE
    r = tl.code_refusal("write my journal", _plan("unsupported"), AGENT)
    assert r.kind == "unsupported" and r.reply == tl.UNSUPPORTED_SENTENCE and r.reason == "unsupported"


# --- the act's dry run ([F-09]) and X-X5's guard ------------------------------------


NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def test_the_dry_run_computes_the_exact_change_without_writing():
    p = tl.stop_dry_run(CARD, Decimal("4.50"), ttl_s=60, now=NOW)
    assert (p.card_id, p.ticker, p.card_state, p.from_stop, p.to_stop) == (11, "XYZ", "WATCH", "4.40", "4.50")
    assert p.expires_at == NOW + timedelta(seconds=60)
    assert p.readback == "Stop on XYZ long, card 11: from 4.40 to 4.50. Say yes, or tap Confirm."
    assert p.target_sha256 == tl.sha256_text("11|4.40|4.50|WATCH")
    assert p.diff_sha256 == tl.sha256_text("cards.set_stop|11|stop|4.40->4.50")


def test_the_same_change_hashes_the_same_and_a_different_one_does_not():
    a = tl.stop_dry_run(CARD, Decimal("4.50"), ttl_s=60, now=NOW)
    b = tl.stop_dry_run(CARD, Decimal("4.500"), ttl_s=60, now=NOW)
    c = tl.stop_dry_run({**CARD, "stop": Decimal("4.4100")}, Decimal("4.50"), ttl_s=60, now=NOW)
    assert a.target_sha256 == b.target_sha256 and a.diff_sha256 == b.diff_sha256
    assert a.target_sha256 != c.target_sha256


@pytest.mark.parametrize("to_stop", ["450", "44.1", "0.44", "0.04"])
def test_x5_guard_clarifies_a_stop_far_from_the_current_one(to_stop):
    with pytest.raises(tl.Clarify) as e:
        tl.stop_dry_run(CARD, Decimal(to_stop), ttl_s=60, now=NOW)
    assert "point" in str(e.value) and to_stop in str(e.value)


def test_the_same_stop_is_not_a_change():
    with pytest.raises(tl.Clarify):
        tl.stop_dry_run(CARD, Decimal("4.4"), ttl_s=60, now=NOW)
