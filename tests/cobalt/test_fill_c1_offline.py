"""S3 exits C1, offline: the drift setting (C1-5), `from_card` (C1-3),
the leg writer's connection rule (C1-2), `fill(conn=…)` (C1-4) and the
three refusals of a fill that is not THE fill (the move route, the CLI,
a fill with no price).

Constructed values only (L32); the drift P always comes from a
constructed settings store (L69).
"""

from __future__ import annotations

import argparse
from decimal import Decimal

import pytest

from cobalt.aset import engine
from cobalt.aset.engine import compute_fill_recompute, compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput, SizingResult

KEY = "fills.drift_warning_pct"
BANNER = "RE-READ STOP — setting fills.drift_warning_pct missing, warning not evaluated"


class Settings:
    def __init__(self, values):
        self._values = dict(values)

    def values(self):
        return dict(self._values)


def _original():
    return compute_sizing(
        SizingInput(
            ticker="TEST", grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"), entry=Decimal("10.0000"), stop=Decimal("9.9000"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )


def _card_row(**over):
    row = {
        "id": 42, "ticker": "TEST", "grade": "B", "direction": "long", "sheet_mode": "full",
        "risk_budget": Decimal("60.00"), "entry": Decimal("10.0000"), "stop": Decimal("9.9000"),
        "per_share_risk": Decimal("0.1000"), "shares": 600, "used_risk": Decimal("60.00"),
        "warnings": [], "last_price": None, "price_source": None,
    }
    row.update(over)
    return row


# ---------------------------------------------------------------------
# C1-5 — the ONE reader of fills.drift_warning_pct
# ---------------------------------------------------------------------


def test_the_reader_returns_none_when_the_key_is_absent():
    from cobalt.settings.fills import drift_warning_pct

    assert drift_warning_pct(Settings({})) is None


@pytest.mark.parametrize("value", [20, 30, 12.5])
def test_the_reader_returns_the_constructed_value(value):
    from cobalt.settings.fills import drift_warning_pct

    assert drift_warning_pct(Settings({KEY: value})) == Decimal(str(value))


@pytest.mark.parametrize("bad", [0, -5, "20", True, None, {"pct": 20}, [20]])
def test_a_bad_value_raises_naming_the_key(bad):
    from cobalt.settings.fills import drift_warning_pct
    from cobalt.settings.models import TraderSettingsError

    with pytest.raises(TraderSettingsError, match=KEY):
        drift_warning_pct(Settings({KEY: bad}))


def test_the_reader_reads_a_connection_through_the_one_query():
    from cobalt.settings.fills import drift_warning_pct

    class Conn:
        def __init__(self):
            self.seen = []

        def execute(self, sql, params):
            self.seen.append((sql, params))

            class R:
                def fetchone(self_inner):
                    return (20,)

            return R()

    conn = Conn()
    assert drift_warning_pct(conn) == Decimal("20")
    assert conn.seen == [("SELECT value FROM trader_settings WHERE key = %s", (KEY,))]


def test_the_hard_coded_25_is_gone():
    assert not hasattr(engine, "FILL_DISTANCE_WARNING_PCT")


@pytest.mark.parametrize(("p", "warned"), [(Decimal("20"), True), (Decimal("30"), False), (Decimal("27"), False)])
def test_the_warning_is_distance_change_pct_greater_than_p(p, warned):
    fill = compute_fill_recompute(_original(), Decimal("10.0270"), Decimal("5"), drift_warning_pct=p)
    assert fill.distance_change_pct == Decimal("27.00")
    assert fill.drift_warning_pct == p and fill.drift_warned is warned
    assert (fill.structural_warning is not None) is warned


def test_p_missing_evaluates_nothing():
    fill = compute_fill_recompute(_original(), Decimal("10.0270"), Decimal("5"), drift_warning_pct=None)
    assert fill.drift_warning_pct is None and fill.drift_warned is None
    assert fill.structural_warning is None


def test_the_typo_guard_is_unchanged():
    with pytest.raises(engine.SizingError, match="typo guard"):
        compute_fill_recompute(_original(), Decimal("11"), Decimal("5"), drift_warning_pct=Decimal("20"))


# ---------------------------------------------------------------------
# C1-3 — SizingResult.from_card, the only rebuild
# ---------------------------------------------------------------------


def test_from_card_copies_the_row():
    rebuilt = SizingResult.from_card(_card_row())
    assert rebuilt.input.entry == Decimal("10.0000") and rebuilt.input.stop == Decimal("9.9000")
    assert rebuilt.input.direction is Direction.LONG and rebuilt.input.risk_dollars == Decimal("60.00")
    assert rebuilt.per_share_risk == Decimal("0.1000") and rebuilt.shares == 600
    assert rebuilt.risk_budget == Decimal("60.00")


@pytest.mark.parametrize(
    "column", ["entry", "stop", "per_share_risk", "shares", "risk_budget", "direction"]
)
def test_from_card_refuses_a_null_naming_the_column(column):
    with pytest.raises(ValueError, match=column):
        SizingResult.from_card(_card_row(**{column: None}))


def test_from_card_takes_per_share_risk_and_shares_off_the_row_never_recomputing():
    rebuilt = SizingResult.from_card(_card_row(per_share_risk=Decimal("0.1200"), shares=500))
    assert rebuilt.per_share_risk == Decimal("0.1200") and rebuilt.shares == 500


# ---------------------------------------------------------------------
# C1-2 — the leg writer never runs on an autocommit connection
# ---------------------------------------------------------------------


def test_insert_entry_leg_refuses_an_autocommit_connection():
    from cobalt.cards.legs import insert_entry_leg

    class Conn:
        autocommit = True

        def execute(self, *a, **k):
            raise AssertionError("nothing may run")

    with pytest.raises(RuntimeError, match="transaction"):
        insert_entry_leg(
            Conn(), 42, shares=10, price=Decimal("10"), at=None, flag="confirmed",
            price_source="typed", price_asof=None, source="sheet", stop_in_force=Decimal("9.9"),
            session="rth", account_mode="sim", day_mode_id=None, attested_sheet=None,
            sheet_mismatch=True,
        )


# ---------------------------------------------------------------------
# C1-4 — fill(conn=…) follows transition()'s rule
# ---------------------------------------------------------------------


def test_fill_on_a_passed_connection_neither_commits_nor_closes(monkeypatch):
    from cobalt.cards import picks as picks_mod
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    class Conn:
        autocommit = False
        committed = closed = rolled_back = False

        def execute(self, sql, params=None):
            class R:
                def fetchone(self_inner):
                    return (CardState.TRIGGERED.value, "manual")

            return R()

        def commit(self):
            self.committed = True

        def close(self):
            self.closed = True

        def rollback(self):
            self.rolled_back = True

    store = CardStore("cobalt_dev")
    monkeypatch.setattr(store, "_connect", lambda **_k: (_ for _ in ()).throw(AssertionError("opened")))
    monkeypatch.setattr(store, "transition", lambda *a, **k: 9)
    monkeypatch.setattr(picks_mod, "record_pick", lambda *a: 5)
    conn = Conn()
    result = store.fill(7, actor=Actor.YOU, conn=conn)
    assert result.transition_ids == [9]
    assert not (conn.committed or conn.closed or conn.rolled_back)


def test_mark_filled_refuses_a_fill_with_no_price_before_touching_the_database(monkeypatch):
    from cobalt.aset.store import AsetStore

    store = AsetStore("cobalt_dev")
    monkeypatch.setattr(store, "_connect", lambda: (_ for _ in ()).throw(AssertionError("opened")))
    with pytest.raises(engine.SizingError, match="no price"):
        store.mark_filled(42, price=None, shares=10, flag="confirmed", price_source="typed",
                          price_asof=None, source="sheet", drift_settings=Settings({}))


# ---------------------------------------------------------------------
# The move route and the CLI never fill
# ---------------------------------------------------------------------


def _bare_page(monkeypatch):
    """The page chrome reads the day mode and his sheets from the database;
    these routes are tested for what they write into the banner and the
    result card, so the chrome is reduced to exactly those two."""
    from cobalt.aset import web as web_module

    monkeypatch.setattr(web_module, "_render",
                        lambda banner="", result="", form=None: banner + result)


def test_the_move_route_refuses_filled_naming_the_fill_route(monkeypatch):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module

    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")

    class Cards:
        def ensure_schema(self):
            pass

        def state_of(self, card_id):
            from cobalt.cards.models import CardState

            return CardState.TRIGGERED

        def fill(self, *a, **k):
            raise AssertionError("the move route must never fill")

        def transition(self, *a, **k):
            raise AssertionError("the move route must never write FILLED")

    monkeypatch.setattr(web_module, "CardStore", Cards)
    _bare_page(monkeypatch)
    r = TestClient(web_module.app).post("/card/7/move", data={"to": "FILLED"})
    assert "FAILED" in r.text and "this route never fills" in r.text and "POST /fill" in r.text
    assert "must never" not in r.text


def test_the_cli_refuses_filled_naming_the_fill_route(monkeypatch):
    from cobalt.cards import cli

    class Store:
        def state_of(self, card_id):
            from cobalt.cards.models import CardState

            return CardState.TRIGGERED

        def fill(self, *a, **k):
            raise AssertionError("the CLI must never fill")

        def transition(self, *a, **k):
            raise AssertionError("the CLI must never write FILLED")

    monkeypatch.setattr(cli, "_store", lambda: Store())
    with pytest.raises(SystemExit, match="never fills.*POST /fill"):
        cli.cmd_move(argparse.Namespace(card_id=7, to="FILLED", actor="you", reason=None))


# ---------------------------------------------------------------------
# /fill — the typed price and shares only; the P-missing banner
# ---------------------------------------------------------------------


class _FillRoute:
    FORM = {
        "card_row_id": "4242", "orig_timestamp": "2026-08-31T09:58:00-04:00",
        "actual_fill": "10.0270", "fill_shares": "77", "ticker": "TEST",
    }

    @staticmethod
    def install(monkeypatch, *, p):
        from types import SimpleNamespace

        from cobalt.aset import web as web_module
        from cobalt.aset.store import FillOutcome
        from cobalt.cards.models import FillResult

        monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
        seen = {}

        class Store:
            def __init__(self, db_name=None):
                pass

            def ensure_schema(self):
                pass

            def mark_filled(self, row_id, **kwargs):
                seen["row_id"], seen["kwargs"] = row_id, kwargs
                original = SizingResult.from_card(_card_row())
                return FillOutcome(
                    result=FillResult(transition_ids=[11], pick_recorded=True, pick_id=5),
                    recompute=compute_fill_recompute(original, kwargs["price"], Decimal("5"),
                                                     drift_warning_pct=p),
                    leg_id=1, sheet_mismatch=True,
                )

        def never(*a, **k):
            raise AssertionError("/fill must not re-size the posted form")

        monkeypatch.setattr(web_module, "AsetStore", Store)
        monkeypatch.setattr(web_module, "_parse_input", never)
        monkeypatch.setattr(web_module, "compute_sizing", never)
        monkeypatch.setattr(web_module, "save_fill_update",
                            lambda *a, **k: ("/dev/note.md", SimpleNamespace(action="appended")))
        _bare_page(monkeypatch)
        return seen


def _post(form):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module

    return TestClient(web_module.app).post("/fill", data=form)


def test_fill_passes_only_the_typed_price_and_shares(monkeypatch):
    seen = _FillRoute.install(monkeypatch, p=Decimal("20"))
    r = _post(_FillRoute.FORM)
    assert "marked FILLED" in r.text, r.text
    assert seen["row_id"] == 4242
    kw = seen["kwargs"]
    assert kw["price"] == Decimal("10.0270") and kw["shares"] == 77
    assert (kw["flag"], kw["price_source"], kw["source"], kw["price_asof"]) == (
        "confirmed", "typed", "sheet", None)
    assert BANNER not in r.text


@pytest.mark.parametrize("field", ["actual_fill", "fill_shares"])
def test_fill_with_no_price_or_no_shares_is_refused(monkeypatch, field):
    seen = _FillRoute.install(monkeypatch, p=Decimal("20"))
    r = _post(dict(_FillRoute.FORM, **{field: ""}))
    assert "FAILED" in r.text and "Nothing written" in r.text
    assert seen == {}


def test_fill_with_p_missing_is_recorded_and_bannered(monkeypatch):
    _FillRoute.install(monkeypatch, p=None)
    r = _post(_FillRoute.FORM)
    assert "marked FILLED" in r.text
    assert BANNER in r.text


def test_the_fill_form_asks_for_the_shares(monkeypatch):
    from cobalt.aset import web as web_module

    html_out = web_module._result_card(_original(), {"card_row_id": "1"})
    assert 'name="fill_shares"' in html_out
