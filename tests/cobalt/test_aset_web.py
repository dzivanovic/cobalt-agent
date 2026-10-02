"""Web-layer tests for the ASET sheet's fail-loud rejection paths
(slice 2.1a, 2026-08-31). These only exercise branches that raise
BEFORE any Postgres/vault I/O — persistence helpers are monkeypatched
to raise if reached at all, proving the rejection happens up front,
never warn-and-write.

Model/engine-level rejections (wrong-side stop, stop-distance typo
guard, fill-distance typo guard) are covered exhaustively in
test_aset_engine.py; this file covers what's specific to web.py: the
entry_ticker stale-carry-over guard (D1) and that the endpoints wire
rejections through without ever touching the store or the vault.
"""

import pytest
from fastapi.testclient import TestClient

from cobalt.aset import web as web_module

client = TestClient(web_module.app)


def _offline_daymode_config():
    from cobalt.aset.models import Grade
    from cobalt.daymode.config import SIGNAL_IDS, DayModeConfig

    return DayModeConfig(
        reduced_sheet="half",
        reduced_enabled_grades=[Grade.A, Grade.B],
        enabled_modes=["reduced"],
        hotkey_file_template="{sheet}.htk",
        stepdowns=[
            {"signal": signal, "effect": "none", "because": "offline web fixture"}
            for signal in SIGNAL_IDS
        ],
        sheet_order=["half", "full"],
        account_enabled_grades=[Grade.A, Grade.B],
    )


def _offline_sheet_modes_config():
    from cobalt.aset.config import SheetModeGrades, SheetModesConfig
    from cobalt.aset.models import Grade

    grades = SheetModeGrades(A_plus=4, A=3, B=2, C=1, D=0)
    return SheetModesConfig(
        sheets={"half": grades, "full": grades},
        order=["half", "full"],
        enabled_grades=[Grade.A, Grade.B],
    )


class _NeverCallStore:
    def __init__(self, db_name: str | None = None):
        raise AssertionError("a rejected card must never reach AsetStore")


def _never_call_save_fill_update(*args, **kwargs):
    raise AssertionError("a rejected fill must never reach save_fill_update")


@pytest.fixture(autouse=True)
def no_persistence(monkeypatch):
    monkeypatch.setattr(web_module, "AsetStore", _NeverCallStore)
    monkeypatch.setattr(web_module, "save_fill_update", _never_call_save_fill_update)
    # This test process never sets COBALT_ENV=production — it's exercising
    # web.py's own rejection paths, not the dev-entry fence (2026-09-02
    # incident follow-up, see cobalt.vault's inverse guard + web.py's
    # DevEntryRefused). Opt in explicitly so that gate doesn't shadow the
    # guards under test here.
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")

    # F6 (S1-P2): /size now refuses a card whose attested `.htk` does not
    # match the day mode in force, and refuses outright when nothing has
    # been attested. These tests are about web.py's OWN guards (the
    # entry-ticker backstop, the stop-side/typo rejects, the dev fence),
    # so the day mode is stubbed into the matched state — otherwise every
    # one of them would stop at the F6 banner and prove nothing about the
    # guard it names. The F6 refusal itself is tested in TestMatchCheckAtTheSheet
    # below and in tests/cobalt/test_daymode.py.
    cfg = _offline_daymode_config()
    monkeypatch.setattr(web_module, "load_sheet_modes_config", _offline_sheet_modes_config)
    monkeypatch.setattr(
        web_module,
        "_daymode_state",
        lambda: {
            "cfg": cfg,
            "day": None,
            "row": {"attested_sheet": cfg.hotkey_file_for_mode(cfg.lowest_enabled)},
            "mode": cfg.lowest_enabled,
            "stage": "stage 1 (system rule)",
            "error": None,
        },
    )


BASE_SIZE_FORM = {
    "ticker": "NVDA",
    "grade": "B",
    "direction": "long",
    "sheet_mode": "full",
    "entry": "218.595",
    "stop": "217.90",
    "entry_ticker": "NVDA",
}


class TestEntryTickerGuard:
    """D1 (2026-08-31): typing a new ticker and hitting Enter submits
    before the JS blur handler ever runs, carrying the previous ticker's
    entry/stop verbatim. entry_ticker is the server-side backstop."""

    def test_mismatched_entry_ticker_refused(self):
        form = dict(BASE_SIZE_FORM, entry_ticker="INTC")  # stale — ticker is NVDA
        r = client.post("/size", data=form)
        assert r.status_code == 200
        assert "FAILED" in r.text
        assert "stale carry-over" in r.text

    def test_blank_entry_ticker_refused(self):
        form = dict(BASE_SIZE_FORM, entry_ticker="")
        r = client.post("/size", data=form)
        assert "FAILED" in r.text
        assert "stale carry-over" in r.text

    def test_replay_d1_nvda_carried_intc_numbers(self):
        # Real 2026-08-31 09:58:45 card: ticker changed to NVDA but entry
        # (90.72)/stop (90.25) were INTC's, carried verbatim.
        form = {
            "ticker": "NVDA",
            "grade": "B",
            "direction": "long",
            "sheet_mode": "full",
            "entry": "90.72",
            "stop": "90.25",
            "entry_ticker": "INTC",
        }
        r = client.post("/size", data=form)
        assert "FAILED" in r.text
        assert "stale carry-over" in r.text

    def test_matching_entry_ticker_proceeds_past_the_guard(self):
        # Not asserting success (AsetStore is stubbed to raise on
        # instantiation) — asserting the guard itself doesn't fire: the
        # form clears _parse_input's ticker-context check and reaches
        # persistence, where the stub's message surfaces instead.
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "stale carry-over" not in r.text
        assert "never reach AsetStore" in r.text


class TestStopSideAndDistanceRejectAtWebLayer:
    def test_wrong_side_stop_refused_no_persist(self):
        form = dict(BASE_SIZE_FORM, stop="219.50")  # long stop above entry
        r = client.post("/size", data=form)
        assert "FAILED" in r.text
        assert "Long stop" in r.text

    def test_pcg_impossible_stop_refused_no_persist(self):
        # Real 2026-08-31 09:40:06 card: SHORT, entry 13.379, stop 17.72
        # (~32% away) — correct side, absurd distance.
        form = {
            "ticker": "PCG",
            "grade": "B",
            "direction": "short",
            "sheet_mode": "full",
            "entry": "13.379",
            "stop": "17.72",
            "entry_ticker": "PCG",
        }
        r = client.post("/size", data=form)
        assert "FAILED" in r.text
        assert "typo guard" in r.text

    def test_empty_entry_refused(self):
        form = dict(BASE_SIZE_FORM, entry="")
        r = client.post("/size", data=form)
        assert "FAILED" in r.text


class TestAbsurdFillRejectAtWebLayer:
    def test_replay_d2_absurd_fill_refused_no_note_write(self, monkeypatch):
        # Real 2026-08-31 10:00:xx cards: a 2518.91 fill against an NVDA
        # card with entry 218.595 was persisted twice before the real
        # fill (218.91) came in. Must refuse outright now.
        #
        # S3 C1: the guard runs inside THE fill (`mark_filled`, on the card
        # row read under its lock, rebuilt by `from_card`), so the store
        # here runs the real engine on that card's row and nothing else.
        from decimal import Decimal

        from cobalt.aset.engine import compute_fill_recompute
        from cobalt.aset.models import SizingResult

        row = {
            "ticker": "TEST", "grade": "B", "direction": "long", "sheet_mode": "full",
            "risk_budget": Decimal("60"), "entry": Decimal("220.0000"), "stop": Decimal("218.0000"),
            "per_share_risk": Decimal("2.0000"), "shares": 30, "used_risk": Decimal("60.00"),
            "warnings": [], "last_price": None, "price_source": None,
        }

        class Store:
            def __init__(self, db_name=None):
                pass

            def ensure_schema(self):
                pass

            def mark_filled(self, row_id, *, price, **kwargs):
                compute_fill_recompute(SizingResult.from_card(row), price, Decimal("5"),
                                       drift_warning_pct=Decimal("20"))
                raise AssertionError("the guard must refuse first")

        monkeypatch.setattr(web_module, "AsetStore", Store)
        form = dict(
            BASE_SIZE_FORM,
            actual_fill="2518.91",
            fill_shares="30",
            card_row_id="4242",
            orig_timestamp="2026-08-31T09:58:00-04:00",
        )
        r = client.post("/fill", data=form)
        assert "FAILED" in r.text
        assert "typo guard" in r.text

    def test_corrected_fill_passes_the_guard(self):
        # The real corrected fill that followed (218.91) — not asserting
        # a full success page, just that the typo guard itself doesn't
        # fire. Since 2026-09-03 (L28 step 3) the next thing the handler
        # demands is the card's aset_sizings row id, because the fill
        # recompute now UPDATEs that row (it used to persist nothing);
        # this form has none, so it stops there — still before any DB or
        # vault I/O, which is what this test is really about.
        form = dict(
            BASE_SIZE_FORM,
            actual_fill="218.91",
            orig_timestamp="2026-08-31T09:58:00-04:00",
        )
        r = client.post("/fill", data=form)
        assert "typo guard" not in r.text
        assert "No aset_sizings row id on this form" in r.text
        assert "never reach save_fill_update" not in r.text
        assert "never reach AsetStore" not in r.text

    def test_fill_with_a_card_row_id_reaches_the_store(self):
        """The fill recompute must persist. With a row id present the
        handler goes on to the store (stubbed here to prove it is
        reached at all) instead of stopping at the guard."""
        form = dict(
            BASE_SIZE_FORM,
            actual_fill="218.91",
            fill_shares="30",
            orig_timestamp="2026-08-31T09:58:00-04:00",
            card_row_id="4242",
        )
        r = client.post("/fill", data=form)
        assert "never reach AsetStore" in r.text


class TestDefect3TwoDistinctHandlers:
    """Defect 3 (2026-09-01): a second trade on the SAME ticker kept
    showing card 1's grade/direction/entry/stop/fill-block until Compute
    was hit again — the old code only reset on a ticker CHANGE, and used
    one handler (handleTicker) with an entryDirty flag to decide whether
    to preserve or overwrite entry, conflating "new card" and "just
    refresh the price" into a single ambiguous path.

    The served page is plain JS (no build step, no browser test harness
    in this repo), so these are structural regression tests on the
    served source: they pin the presence of two separate, unconditional
    handlers and the absence of the old single-handler-with-a-flag
    shape, so a future edit can't silently reintroduce it. They do not
    substitute for exercising the page in a real browser."""

    def test_two_distinct_handlers_exist(self):
        assert "async function onTickerBlur(" in web_module.JS
        assert "async function refetchLastPrice(" in web_module.JS
        assert "async function handleTicker(" not in web_module.JS

    def test_blur_reset_is_unconditional_not_gated_on_ticker_change(self):
        blur_fn = web_module.JS.split("async function onTickerBlur(")[1].split("\n\n")[0]
        assert "currentTicker = t" in blur_fn  # still tracked, for the input-listener guard
        # but the reset itself is never conditioned on a ticker-changed check
        assert "t !== currentTicker" not in blur_fn
        assert "t === currentTicker" not in blur_fn
        assert "clearForNewCard()" in blur_fn

    def test_refetch_does_not_reset_other_fields(self):
        refetch_fn = web_module.JS.split("async function refetchLastPrice(")[1].split("\n\n")[0]
        assert "clearForNewCard" not in refetch_fn
        assert "$('stop')" not in refetch_fn
        assert "$('grade')" not in refetch_fn
        assert "$('direction')" not in refetch_fn
        # both last_price and entry ARE refreshed, unconditionally
        assert "$('last_price').value = price" in refetch_fn
        assert "$('entry').value = price" in refetch_fn

    def test_clear_for_new_card_resets_grade_and_direction(self):
        clear_fn = web_module.JS.split("function clearForNewCard(){")[1].split("\n }")[0]
        assert "$('grade').value" in clear_fn
        assert "setDir(" in clear_fn
        # sheet_mode is a day setting, not a card setting — must survive
        assert "sheet_mode" not in clear_fn

    def test_entry_dirty_machinery_fully_removed(self):
        # Dead once both paths are unconditional — no flag left to rot
        # (the phrase still appears in an explanatory comment above).
        assert "let entryDirty" not in web_module.JS
        assert "markEntryDirty" not in web_module.JS
        assert "entryHint" not in web_module.JS
        assert "entry_dirty" not in web_module._render()


class TestDevEntryFence:
    """2026-09-02 ("TSLA id 127") incident follow-up: a non-production
    instance must refuse ticker fetch / sizing / fill by default, so a
    stale dev tab can't quietly take a live entry — the module-wide
    COBALT_ALLOW_DEV_ENTRY=1 fixture (see no_persistence above) is
    overridden per-test here to exercise the fence itself."""

    def test_prefill_refused_when_not_production_and_not_allowed(self, monkeypatch):
        monkeypatch.setenv("COBALT_ENV", "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
        r = client.get("/api/prefill", params={"ticker": "NVDA"})
        assert r.status_code == 403
        assert "DEV instance" in r.json()["error"]

    def test_size_refused_when_not_production_and_not_allowed(self, monkeypatch):
        monkeypatch.setenv("COBALT_ENV", "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "FAILED" in r.text
        assert "DEV instance" in r.text
        assert "never reach AsetStore" not in r.text

    def test_fill_refused_when_not_production_and_not_allowed(self, monkeypatch):
        monkeypatch.setenv("COBALT_ENV", "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
        form = dict(
            BASE_SIZE_FORM,
            actual_fill="218.91",
            orig_timestamp="2026-08-31T09:58:00-04:00",
        )
        r = client.post("/fill", data=form)
        assert "FAILED" in r.text
        assert "DEV instance" in r.text
        assert "never reach save_fill_update" not in r.text

    def test_size_allowed_when_explicitly_opted_in(self, monkeypatch):
        monkeypatch.setenv("COBALT_ENV", "dev")  # RULING 7: dev is declared, not inferred
        monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "DEV instance" not in r.text
        assert "never reach AsetStore" in r.text

    @staticmethod
    def _settings_stay_on_dev(monkeypatch):
        """ADR-0008 D3.4 consequence, made explicit.

        The sheet's grade ladder and rung now come from
        `"user".trader_settings`, so a process that declares itself
        PRODUCTION resolves them out of `cobalt_brain` — which is exactly
        right in production and exactly wrong in a test that flips the
        flag only to check a header label. These two tests pin the
        settings read to `cobalt_dev` so they keep testing the fence and
        the label, and nothing else.
        """
        # Keep this entirely offline.  The autouse fixture already gives
        # web.py synthetic config objects; restate the patches here because
        # these tests deliberately flip COBALT_ENV to production.
        monkeypatch.setattr(web_module, "load_sheet_modes_config", _offline_sheet_modes_config)
        monkeypatch.setattr(web_module, "load_daymode_config", _offline_daymode_config)

    def test_size_allowed_when_production(self, monkeypatch):
        self._settings_stay_on_dev(monkeypatch)
        monkeypatch.setenv("COBALT_ENV", "production")
        monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "DEV instance" not in r.text
        assert "never reach AsetStore" in r.text

    def test_header_shows_dev_label_and_red_banner_when_not_production(self, monkeypatch):
        monkeypatch.setenv("COBALT_ENV", "dev")  # RULING 7: dev is declared, not inferred
        text = web_module._render()
        assert "pre-beta slice 1 · DEV" in text
        assert "DEV INSTANCE" in text

    def test_header_shows_production_label_and_no_banner_when_production(self, monkeypatch):
        self._settings_stay_on_dev(monkeypatch)
        monkeypatch.setenv("COBALT_ENV", "production")
        text = web_module._render()
        assert "pre-beta slice 1 · PRODUCTION" in text
        assert "DEV INSTANCE" not in text


class TestMatchCheckAtTheSheet:
    """F6 at the write path — the Charter's own acceptance test, through
    the actual HTTP endpoint rather than the checker in isolation."""

    def _stub_daymode(self, monkeypatch, *, attested, mode=None):
        cfg = _offline_daymode_config()
        monkeypatch.setattr(
            web_module,
            "_daymode_state",
            lambda: {
                "cfg": cfg,
                "day": None,
                "row": ({"attested_sheet": attested} if attested else {}),
                "mode": mode or cfg.lowest_enabled,
                "stage": "stage 1 (system rule)",
                "error": None,
            },
        )

    def test_full_sheet_attested_on_a_reduced_day_refuses_the_card(self, monkeypatch):
        """'He loads the full sheet on a half day -> card refused with
        the reason' (Charter §3 F6)."""
        self._stub_daymode(monkeypatch, attested="full.htk")
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "FAILED" in r.text
        assert "sheet FULL loaded, day mode REDUCED" in r.text
        assert "reload half.htk or overrule" in r.text
        assert "never reach AsetStore" not in r.text, "no card was written"

    def test_nothing_attested_refuses_too(self, monkeypatch):
        self._stub_daymode(monkeypatch, attested=None)
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "FAILED" in r.text
        assert "No hotkey file attested" in r.text
        assert "never reach AsetStore" not in r.text

    def test_a_key_outside_the_rung_is_refused(self, monkeypatch):
        """A+ on the reduced rung — the grade restriction, not the sheet."""
        self._stub_daymode(monkeypatch, attested="half.htk")
        r = client.post("/size", data=dict(BASE_SIZE_FORM, grade="A+"))
        assert "FAILED" in r.text
        assert "never reach AsetStore" not in r.text

    def test_the_matching_sheet_lets_the_card_through(self, monkeypatch):
        self._stub_daymode(monkeypatch, attested="half.htk")
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "never reach AsetStore" in r.text, "reached persistence"

    def test_an_unresolved_day_mode_refuses_every_card(self, monkeypatch):
        monkeypatch.setattr(
            web_module,
            "_daymode_state",
            lambda: {"cfg": None, "day": None, "row": None, "mode": None,
                     "stage": "UNRESOLVED", "error": "ConfigError: daymode.yaml missing"},
        )
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "FAILED" in r.text
        assert "Day mode unresolved" in r.text


def test_real_checkbox_shape_preserves_account_mode_and_renders_both_fields(
    tmp_path, monkeypatch
):
    """A daily-note sheet tick updates only the sheet; LIVE/SIM remains explicit."""
    cfg = _offline_daymode_config()
    note = tmp_path / "daily.md"
    note.write_text(
        "<!-- cobalt:section daymode -->\n"
        "<!-- cobalt:unit sheet_mode -->\n"
        ".htk loaded — tick ONE:\n"
        "- [x] half.htk\n"
        "- [ ] full.htk\n"
        "<!-- /cobalt:unit sheet_mode -->\n"
        "<!-- /cobalt:section daymode -->\n"
    )
    monkeypatch.setattr(web_module.daymode_note, "daily_note_path", lambda _day: note)

    class Store:
        def __init__(self):
            self.calls = []

        def attest_sheet(self, day, *, filename, account_mode=None):
            self.calls.append((day, filename, account_mode))

        def for_date(self, _day):
            return {"attested_sheet": "half.htk", "account_mode": "live"}

    store = Store()
    day = __import__("datetime").date(2026, 9, 11)
    row = web_module._read_back_note_attestation(
        cfg, day, {"attested_sheet": None, "account_mode": "live"}, store
    )
    assert store.calls == [(day, "half.htk", None)]
    assert row["account_mode"] == "live"

    rendered = web_module._daymode_banner(
        {
            "cfg": cfg,
            "row": row,
            "mode": cfg.lowest_enabled,
            "stage": "stage 1 (system rule)",
            "error": None,
            "account_mode": "live",
            "account_error": None,
        }
    )
    assert '<option value="half.htk" selected>' in rendered
    assert '<select name="account_mode">' in rendered
    assert '<option value="live" selected>LIVE</option>' in rendered


class TestCardControls:
    """The open-cards action row is rendered FROM the edge table, so a
    state the table can reach but the sheet has no label for is a
    KeyError at render time — a blank sheet mid-morning, not a caught
    bug. This is how `CLOSED` was missed on the first pass."""

    def test_every_state_has_a_button_label(self):
        from cobalt.cards.models import ALLOWED, CardState

        card = {
            "id": 1, "ticker": "NVDA", "grade": "B", "direction": "long",
            "shares": 100, "stop": "9.50", "session": "rth", "state": "WATCH",
        }
        for state in CardState:
            if not ALLOWED[state]:
                continue      # terminal: no action row to draw
            html_out = web_module._card_controls(dict(card, state=state.value))
            assert f'st-{state.value}' in html_out
            for target in ALLOWED[state]:
                assert f'value="{target.value}"' in html_out, (
                    f"{state.value} -> {target.value} has no button"
                )

    def test_a_filled_card_offers_close_and_an_editable_stop(self):
        card = {
            "id": 1, "ticker": "NVDA", "grade": "B", "direction": "long",
            "shares": 100, "stop": "9.50", "session": "rth", "state": "FILLED",
        }
        html_out = web_module._card_controls(card)
        assert ">CLOSE<" in html_out
        assert "YOURS" in html_out, "stop is editable in-trade (decision 11)"

    def test_an_armed_card_locks_the_stop_and_shows_why(self):
        card = {
            "id": 1, "ticker": "NVDA", "grade": "B", "direction": "long",
            "shares": 100, "stop": "9.50", "session": "rth", "state": "ARMED",
        }
        html_out = web_module._card_controls(card)
        assert "YOURS" not in html_out
        assert "locked in ARMED" in html_out
        assert "key frozen from ARMED onward" in html_out
        assert ">DISARM<" in html_out


class TestPickNotRecordedBanner:
    """S2-P4 R2 / Astra R1-5: both HTTP fill paths keep their success
    banner and APPEND a red "pick not recorded" banner when the fill
    committed without its pick."""

    GAP = None

    @staticmethod
    def _result(recorded: bool):
        from cobalt.cards.models import FillResult

        if recorded:
            return FillResult(transition_ids=[11, 12, 13], pick_recorded=True, pick_id=5)
        return FillResult(transition_ids=[11, 12, 13], pick_recorded=False, pick_id=None,
                          pick_error="UndefinedTable: relation \"picks\" does not exist")

    def _fill_form(self):
        return dict(BASE_SIZE_FORM, actual_fill="218.91", fill_shares="30",
                    orig_timestamp="2026-08-31T09:58:00-04:00", card_row_id="4242")

    def _stub_fill_route(self, monkeypatch, recorded):
        from decimal import Decimal
        from types import SimpleNamespace

        from cobalt.aset.engine import compute_fill_recompute, compute_sizing
        from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
        from cobalt.aset.store import FillOutcome

        result = self._result(recorded)
        original = compute_sizing(
            SizingInput(ticker="TEST", grade=Grade.B, direction=Direction.LONG, sheet_mode=SheetMode.FULL,
                        risk_dollars=Decimal("60"), entry=Decimal("220.0000"), stop=Decimal("218.0000")),
            [Grade.A, Grade.B], Decimal("10"),
        )

        class Store:
            def __init__(self, db_name=None):
                pass

            def ensure_schema(self):
                pass

            def mark_filled(self, row_id, **kwargs):
                return FillOutcome(
                    result=result,
                    recompute=compute_fill_recompute(original, kwargs["price"], Decimal("5"),
                                                     drift_warning_pct=Decimal("20")),
                    leg_id=1, sheet_mismatch=False,
                )

        monkeypatch.setattr(web_module, "AsetStore", Store)
        monkeypatch.setattr(web_module, "save_fill_update",
                            lambda *a, **k: ("/dev/note.md", SimpleNamespace(action="appended")))
        monkeypatch.setattr(web_module, "_open_cards_section", lambda: "")

    @pytest.mark.parametrize("recorded", [True, False])
    def test_fill_form_route(self, monkeypatch, recorded):
        self._stub_fill_route(monkeypatch, recorded)
        r = client.post("/fill", data=self._fill_form())
        assert "aset_sizings id 4242 marked FILLED" in r.text, "the success banner stays"
        assert ("pick not recorded" in r.text) is (not recorded)
        if not recorded:
            assert 'class="failed"' in r.text and "UndefinedTable" in r.text
            assert "cobalt cards picks" in r.text

    def test_card_move_no_longer_fills(self, monkeypatch):
        """S3 C1 (v3 §2 [F-22]): the move route never fills — a FILLED
        with no price is the radar fill that recorded no price (F8). The
        one HTTP fill path is /fill, through `mark_filled`."""

        class Cards:
            def ensure_schema(self):
                pass

            def state_of(self, card_id):
                from cobalt.cards.models import CardState

                return CardState.WATCH

            def fill(self, card_id, **kwargs):
                raise AssertionError("the move route must never fill")

        monkeypatch.setattr(web_module, "CardStore", Cards)
        monkeypatch.setattr(web_module, "_open_cards_section", lambda: "")
        r = client.post("/card/7/move", data={"to": "FILLED"})
        assert "FAILED" in r.text and "this route never fills" in r.text and "POST /fill" in r.text
        assert "the move route must never fill" not in r.text


def _sheet_card(card_id: int, state: str, origin: str = "manual") -> dict:
    """One open card as `CardStore.open_cards()` returns it. Constructed
    values only (L32)."""
    from decimal import Decimal

    return {
        "id": card_id, "ticker": f"ZZQ{card_id}", "grade": "B", "direction": "long",
        "shares": 12, "stop": Decimal("63.2000"), "session": "rth", "state": state,
        "origin": origin, "account_mode": "sim",
    }


class TestNoCardAboveTheForm:
    """aset-interim-close S2 (his R13, 2026-10-01): "I don't want any cards
    to ever be above the form". The open-cards block renders BELOW the
    `/size` form on every response that renders `/`; `{banner}` and
    `{result}` stay above it."""

    @staticmethod
    def _stub_cards(monkeypatch):
        from cobalt.cards.models import CardState

        class Cards:
            def ensure_schema(self):
                pass

            def open_cards(self):
                return [_sheet_card(41, "WATCH"), _sheet_card(42, "FILLED")]

            def filled_with_picks(self, day):
                return []

            def state_of(self, card_id):
                return CardState.WATCH

            def transition(self, card_id, to_state, **kwargs):
                return 9001

        monkeypatch.setattr(web_module, "CardStore", Cards)
        monkeypatch.setattr(
            web_module, "_sheet_in_trade",
            lambda card: '<div class="intrade-stub"></div>' if card["state"] == "FILLED" else "",
        )

    @staticmethod
    def _assert_the_form_comes_first(text: str):
        form_at = text.index('action="/size"')
        cards_at = text.index("Open cards (F7)")
        assert form_at < cards_at, "the open-cards label renders above the new-card form"
        assert form_at < text.index('class="intrade-stub"'), "a FILLED card's in-trade block is above the form"
        assert text.index('id="banner"') < form_at and text.index('id="resultCard"') < form_at, (
            "{banner} and {result} stay above the form"
        )

    def test_get_renders_every_card_below_the_form(self, monkeypatch):
        self._stub_cards(monkeypatch)
        r = client.get("/")
        assert r.status_code == 200
        assert "ZZQ41" in r.text and "ZZQ42" in r.text, "both cards are on the page"
        self._assert_the_form_comes_first(r.text)

    def test_a_move_result_renders_every_card_below_the_form(self, monkeypatch):
        self._stub_cards(monkeypatch)
        r = client.post("/card/41/move", data={"to": "ARMED"})
        assert "→ ARMED (card_transitions id(s) 9001)" in r.text, r.text[:400]
        self._assert_the_form_comes_first(r.text)


class TestSheetCloseAtEntry:
    """aset-interim-close S3 (his R13): CLOSE on `/` closes a FILLED card
    with nothing typed — ONE flat exit leg for every running share at the
    entry fill price, `estimated`, through the one leg writer
    (`legs.record_exit`, whose `_close_if_zero` writes FILLED -> CLOSED).
    The route never writes CLOSED itself. Constructed values only (L32)."""

    @staticmethod
    def _world(monkeypatch, *, state="FILLED", running=12, entry=True, price_source="typed", filled_today=()):
        from decimal import Decimal

        from cobalt.cards import legs
        from cobalt.cards.models import CardState

        calls = {"exit": [], "transition": []}

        class Cards:
            def ensure_schema(self):
                pass

            def state_of(self, card_id):
                return CardState(state)

            def filled_with_picks(self, day):
                return [{"card_id": cid, "origin": origin, "state": "CLOSED"} for cid, origin in filled_today]

            def transition(self, *a, **k):
                calls["transition"].append((a, k))
                raise AssertionError("the move route must never write CLOSED itself")

        entry_leg = {"id": 501, "card_id": 31, "seq": 0, "kind": "entry", "shares": 12,
                     "price": Decimal("64.1000"), "flag": "confirmed", "price_source": price_source,
                     "stop_in_force": Decimal("63.2000")}
        position = legs.Position(
            card={"id": 31, "ticker": "ZZQX", "direction": "long", "state": state,
                  "stop": Decimal("63.2000"), "structural_stop": None},
            legs=[entry_leg] if entry else [],
            running=legs.Running(
                shares=running, basis=legs.BASIS_LEGS if entry else legs.BASIS_SHARES, base_shares=12,
                exit_shares=12 - running, entry_leg_id=501 if entry else None,
                entry_price=Decimal("64.1000") if entry else None, state=state,
            ),
            realized=legs.RealizedR(legs.REALIZED_R_ID, None, False, None, "not computed — constructed"),
        )

        def record_exit(card_id, **kwargs):
            calls["exit"].append((card_id, kwargs))
            return legs.ExitResult(leg_id=502, shares=kwargs["running_before"],
                                   running_before=kwargs["running_before"], running_after=0,
                                   closed=True, transition_id=77)

        monkeypatch.setattr(legs, "read_position", lambda card_id: position)
        monkeypatch.setattr(legs, "record_exit", record_exit)
        monkeypatch.setattr(web_module, "CardStore", Cards)
        monkeypatch.setattr(web_module, "_leg_note", lambda *a, **k: None)
        monkeypatch.setattr(web_module, "_render", lambda banner="", result="", form=None: banner + result)
        return calls

    @staticmethod
    def _the_one_flat_leg(calls, *, price_source):
        from decimal import Decimal

        assert not calls["transition"], "CLOSED is written by the leg writer, never by the route"
        ((card_id, kwargs),) = calls["exit"]
        assert kwargs.pop("now") is not None
        assert (card_id, kwargs) == (31, {
            "preset": "flat", "shares": None, "price": Decimal("64.1000"), "price_source": price_source,
            "price_asof": None, "flag": "estimated", "source": "sheet", "running_before": 12,
        })

    def test_a_filled_manual_card_closes_flat_at_entry_with_nothing_typed(self, monkeypatch):
        calls = self._world(monkeypatch)
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "never closes" not in r.text, r.text
        self._the_one_flat_leg(calls, price_source="typed")
        assert "FAILED" not in r.text and 'class="failed"' not in r.text
        assert "CLOSED" in r.text and "12 sh @ 64.1000" in r.text and "estimated" in r.text

    def test_a_filled_radar_card_closes_the_same_way(self, monkeypatch):
        """A radar card listed on `/` gets the same CLOSE (drawn from the
        edge table) and the same leg; its entry leg's source rides along."""
        assert ">CLOSE<" in web_module._card_controls(_sheet_card(31, "FILLED", origin="radar"))
        calls = self._world(monkeypatch, price_source="last_poll")
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "never closes" not in r.text, r.text
        self._the_one_flat_leg(calls, price_source="last_poll")
        assert "FAILED" not in r.text

    @pytest.mark.parametrize("state, running", [("FILLED", 0), ("WATCH", 0)])
    def test_nothing_running_or_not_filled_is_refused_and_nothing_is_written(self, monkeypatch, state, running):
        calls = self._world(monkeypatch, state=state, running=running)
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "FAILED" in r.text and "REFUSED card 31" in r.text and "Nothing written" in r.text
        assert calls == {"exit": [], "transition": []}

    def test_a_card_with_no_entry_leg_is_refused_and_nothing_is_written(self, monkeypatch):
        calls = self._world(monkeypatch, entry=False)
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "FAILED" in r.text and "REFUSED card 31" in r.text and "no entry leg" in r.text
        assert calls == {"exit": [], "transition": []}

    @pytest.mark.parametrize("to, says", [("FILLED", "this route never fills"), ("BOGUS", "ValueError")])
    def test_the_other_refusals_are_unchanged(self, monkeypatch, to, says):
        calls = self._world(monkeypatch)
        r = client.post("/card/31/move", data={"to": to})
        assert "FAILED" in r.text and says in r.text
        assert calls == {"exit": [], "transition": []}


class TestSheetCloseBannerSaysWhereTheLegIsListed:
    """check of aset-interim-close, house A F2: the sheet lists a CLOSED
    card's estimated legs only for a MANUAL card whose FILLED transition
    is today (`_sheet_closed_estimated` → `filled_with_picks(_today_et())`).
    The CLOSE banner says "listed for correction" only when that is so
    (L35). Constructed values only (L32)."""

    def test_a_card_filled_before_today_is_not_called_listed(self, monkeypatch):
        TestSheetCloseAtEntry._world(monkeypatch, filled_today=())
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "CLOSED" in r.text and "estimated" in r.text, r.text
        assert "listed for correction" not in r.text, "the banner says listed; the sheet will not list it"
        assert "not listed on this sheet" in r.text

    def test_a_manual_card_filled_today_is_called_listed(self, monkeypatch):
        TestSheetCloseAtEntry._world(monkeypatch, filled_today=((31, "manual"),))
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "listed for correction" in r.text and "not listed" not in r.text, r.text

    def test_a_radar_card_filled_today_is_not_called_listed_on_the_sheet(self, monkeypatch):
        TestSheetCloseAtEntry._world(monkeypatch, filled_today=((31, "radar"),))
        r = client.post("/card/31/move", data={"to": "CLOSED"})
        assert "listed for correction" not in r.text and "not listed on this sheet" in r.text, r.text


class TestTheFormStaysUnderHim:
    """aset-interim-close S4 (his R13: "anytime I refresh it because I jump
    from one field to another, it will move the page all the way to the
    top"). S1 found two paths in the page script: Enter in a field submits
    the `/size` form (a full-page POST; the new page opens at the top), and
    the ticker reset empties `#banner` / `#resultCard` above the form (the
    form moves up). Structural tests on the served source, as Defect 3's:
    no browser harness exists in this repo."""

    def test_enter_in_a_sizing_field_moves_to_the_next_field_and_never_submits(self):
        assert 'action="/size" id="sizeForm"' in web_module._render()
        marker = "$('sizeForm').addEventListener('keydown'"
        assert marker in web_module.JS, "no Enter guard on the sizing form"
        handler = web_module.JS.split(marker)[1].split("\n   });")[0]
        assert "e.key !== 'Enter'" in handler
        assert "e.preventDefault()" in handler
        assert ".focus()" in handler

    def test_the_ticker_reset_keeps_the_form_where_it_was(self):
        clear_fn = web_module.JS.split("function clearForNewCard(){")[1].split("\n }")[0]
        assert "$('sizeForm').getBoundingClientRect().top" in clear_fn, "the reset does not measure the form"
        assert "window.scrollBy(0," in clear_fn
        assert clear_fn.index("getBoundingClientRect") < clear_fn.index("$('resultCard').innerHTML = ''"), (
            "the form's place is measured before anything above it is emptied"
        )
        # check of aset-interim-close, house A F3: the delta is new − old (the
        # form moved up → negative → scroll up by as much), measured after
        # BOTH boxes above the form are emptied, and that delta is scrolled.
        moved = "const moved = $('sizeForm').getBoundingClientRect().top - formTop;"
        assert moved in clear_fn, "the delta is not new top − old top"
        assert clear_fn.index(moved) > clear_fn.index("$('banner').innerHTML = ''"), (
            "the delta is measured before everything above the form is emptied"
        )
        assert "if (moved) window.scrollBy(0, moved);" in clear_fn, "the delta is not what is scrolled"


class TestDayModeBannerStage:
    """The stage LABEL and the MODE must come from one rule. Otherwise the
    banner can read "stage 2 (decided)" while showing the stage-1 floor —
    exactly what happens pre-09:00 on a day whose proposal was answered."""

    @staticmethod
    def _at(hour):
        from datetime import datetime
        from zoneinfo import ZoneInfo

        return datetime(2026, 9, 3, hour, 30, tzinfo=ZoneInfo("America/New_York"))

    def test_pre_0900_reads_stage_1_even_when_decided(self):
        from cobalt.daymode import decided_or_stage1

        row = {"proposed": "reduced", "decided": "full"}
        assert "stage 1" in web_module._stage_label(row, self._at(8))
        assert decided_or_stage1(row, _offline_daymode_config(), self._at(8)) == "reduced", (
            "the floor holds before 09:00 — label and mode agree"
        )

    def test_after_0900_a_decision_reads_stage_2(self):
        from cobalt.daymode import decided_or_stage1

        row = {"proposed": "reduced", "decided": "full"}
        assert web_module._stage_label(row, self._at(10)) == "stage 2 (decided)"
        assert decided_or_stage1(row, _offline_daymode_config(), self._at(10)) == "full"

    def test_after_0900_undecided_says_the_floor_holds(self):
        from cobalt.daymode import decided_or_stage1

        row = {"proposed": "full", "decided": None}
        label = web_module._stage_label(row, self._at(10))
        assert "undecided" in label and "floor holds" in label
        assert decided_or_stage1(row, _offline_daymode_config(), self._at(10)) == "reduced"
