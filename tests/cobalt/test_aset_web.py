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
    def __init__(self, db_name: str):
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
        monkeypatch.delenv("COBALT_ENV", raising=False)
        monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
        r = client.get("/api/prefill", params={"ticker": "NVDA"})
        assert r.status_code == 403
        assert "DEV instance" in r.json()["error"]

    def test_size_refused_when_not_production_and_not_allowed(self, monkeypatch):
        monkeypatch.delenv("COBALT_ENV", raising=False)
        monkeypatch.delenv("COBALT_ALLOW_DEV_ENTRY", raising=False)
        r = client.post("/size", data=BASE_SIZE_FORM)
        assert "FAILED" in r.text
        assert "DEV instance" in r.text
        assert "never reach AsetStore" not in r.text

    def test_fill_refused_when_not_production_and_not_allowed(self, monkeypatch):
        monkeypatch.delenv("COBALT_ENV", raising=False)
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
        monkeypatch.delenv("COBALT_ENV", raising=False)
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
        monkeypatch.delenv("COBALT_ENV", raising=False)
        text = web_module._render()
        assert "pre-beta slice 1 · DEV" in text
        assert "DEV INSTANCE" in text

    def test_header_shows_production_label_and_no_banner_when_production(self, monkeypatch):
        monkeypatch.setenv("COBALT_ENV", "production")
        text = web_module._render()
        assert "pre-beta slice 1 · PRODUCTION" in text
        assert "DEV INSTANCE" not in text
