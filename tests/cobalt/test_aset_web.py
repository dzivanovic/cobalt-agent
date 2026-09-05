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
    from cobalt.daymode.config import load_daymode_config

    cfg = load_daymode_config()
    monkeypatch.setattr(
        web_module,
        "_daymode_state",
        lambda: {
            "cfg": cfg,
            "day": None,
            "row": {"attested_sheet": "reduced_day.htk"},
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
    def test_replay_d2_absurd_fill_refused_no_note_write(self):
        # Real 2026-08-31 10:00:xx cards: a 2518.91 fill against an NVDA
        # card with entry 218.595 was persisted twice before the real
        # fill (218.91) came in. Must refuse outright now.
        form = dict(
            BASE_SIZE_FORM,
            actual_fill="2518.91",
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

    def test_size_allowed_when_production(self, monkeypatch):
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
        monkeypatch.setenv("COBALT_ENV", "production")
        text = web_module._render()
        assert "pre-beta slice 1 · PRODUCTION" in text
        assert "DEV INSTANCE" not in text


class TestMatchCheckAtTheSheet:
    """F6 at the write path — the Charter's own acceptance test, through
    the actual HTTP endpoint rather than the checker in isolation."""

    def _stub_daymode(self, monkeypatch, *, attested, mode=None):
        from cobalt.daymode.config import load_daymode_config

        cfg = load_daymode_config()
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
        assert "reload reduced_day.htk or overrule" in r.text
        assert "never reach AsetStore" not in r.text, "no card was written"

    def test_nothing_attested_refuses_too(self, monkeypatch):
        self._stub_daymode(monkeypatch, attested=None)
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "FAILED" in r.text
        assert "No hotkey file attested" in r.text
        assert "never reach AsetStore" not in r.text

    def test_a_key_outside_the_rung_is_refused(self, monkeypatch):
        """A+ on the reduced rung — the grade restriction, not the sheet."""
        self._stub_daymode(monkeypatch, attested="reduced_day.htk")
        r = client.post("/size", data=dict(BASE_SIZE_FORM, grade="A+"))
        assert "FAILED" in r.text
        assert "never reach AsetStore" not in r.text

    def test_the_matching_sheet_lets_the_card_through(self, monkeypatch):
        self._stub_daymode(monkeypatch, attested="reduced_day.htk")
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
        from cobalt.daymode import decided_or_stage1, load_daymode_config

        row = {"proposed": "reduced", "decided": "full"}
        assert "stage 1" in web_module._stage_label(row, self._at(8))
        assert decided_or_stage1(row, load_daymode_config(), self._at(8)) == "reduced", (
            "the floor holds before 09:00 — label and mode agree"
        )

    def test_after_0900_a_decision_reads_stage_2(self):
        from cobalt.daymode import decided_or_stage1, load_daymode_config

        row = {"proposed": "reduced", "decided": "full"}
        assert web_module._stage_label(row, self._at(10)) == "stage 2 (decided)"
        assert decided_or_stage1(row, load_daymode_config(), self._at(10)) == "full"

    def test_after_0900_undecided_says_the_floor_holds(self):
        from cobalt.daymode import decided_or_stage1, load_daymode_config

        row = {"proposed": "full", "decided": None}
        label = web_module._stage_label(row, self._at(10))
        assert "undecided" in label and "floor holds" in label
        assert decided_or_stage1(row, load_daymode_config(), self._at(10)) == "reduced"
