"""DRC D4 — the with-DB proofs of the DRC settings family (v2 §9 D4, §10).

Every test runs inside the suite's rollback transaction on `cobalt_dev`
(tests/cobalt/conftest.py `dev_db_tx`): nothing written here survives the
test. Every asserted value is a value THIS file constructed (L69) — no
test reads, or asserts, a value already stored in `"user".trader_settings`.

E10 and X12 are the first-gate experiments (L70): they were written and
run BEFORE any D4 source edit.
"""

from __future__ import annotations

import os

import pytest

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: SPEC §7's DRC key NAMES this slice reads (names only, L32). Spelled
#: here, not imported, so E10 / X12 could run before the code existed.
DRC_KEYS = (
    "account.daily_stop_full",
    "account.daily_stop_half",
    "limits.card_match_window_minutes",
    "windows.premarket_end",
    "windows.first_window_minutes",
    "windows.prime",
    "windows.dead",
    "windows.second",
    "goal.primary",
    "goal.metric",
    "goal.target_pct",
    "goal.switch_threshold_pct",
)


def _clear_drc_rows():
    """Inside the rollback: make sure no DRC key row is present."""
    from cobalt.settings.store import TraderSettingsStore

    TraderSettingsStore().put({}, source="test:d4-clear", delete=DRC_KEYS)


# ---------------------------------------------------------------------
# E10 / X12 — the first gate (L70)
# ---------------------------------------------------------------------


@requires_db
def test_e10_a_new_drc_key_lands_without_a_migration():
    """E10 (grok, v2 :114): "Insert one new `trader_settings` key on
    `cobalt_dev` with no migration. Pass: D4 stays migration-free. Fail:
    D4 gains the migration the desk numbers."

    One constructed `account.*` row through the store's EXISTING put,
    read back raw from `trader_settings`."""
    from cobalt.settings.store import TraderSettingsStore

    store = TraderSettingsStore()
    _clear_drc_rows()
    outcome = store.put({"account.daily_stop_full": "250"}, source="test:e10")
    assert outcome == {"account.daily_stop_full": "created"}
    raw = [r for r in store.rows() if r["key"] == "account.daily_stop_full"]
    assert len(raw) == 1
    assert raw[0]["value"] == "250"
    assert raw[0]["source"] == "test:e10"


@requires_db
def test_x12_size_still_sizes_without_drc_keys(monkeypatch):
    """X12 (the Fable seat, v2 :118): "cobalt_dev without the DRC key rows
    → `/size` still serves and sizes; `cobalt drc build` fails naming the
    missing key (T5's `OPTIONAL_SETTING_KEYS` placement)." — the `/size`
    half (the `cobalt drc build` half is D3's). A GREEN-as-pin on the base.
    """
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.aset.daily_note import DailyNoteRefused
    from test_aset_web import (
        BASE_SIZE_FORM,
        _offline_daymode_config,
        _offline_sheet_modes_config,
    )

    _clear_drc_rows()

    class _Store:
        db_name = "cobalt_dev"

        def ensure_schema(self):
            return None

        def save(self, result):
            return 1

        def account_mode_for(self, row_id):
            return "sim"

    def _refuse_note(cfg, result):
        raise DailyNoteRefused("x12: no daily-note write in this test")

    cfg = _offline_daymode_config()
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    monkeypatch.setattr(web_module, "AsetStore", _Store)
    monkeypatch.setattr(web_module, "save_card", _refuse_note)
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
    r = TestClient(web_module.app).post("/size", data=dict(BASE_SIZE_FORM))
    assert r.status_code == 200
    assert '<div class="shares">' in r.text, r.text[-2000:]
    assert "shares</span>" in r.text


@requires_db
def test_x12_every_drc_field_is_none_without_rows():
    """X12 (v2 :118), the reader half: with no DRC key rows,
    `load_drc_settings` returns every field `None` — absent is `not
    given`, never a default (L1)."""
    from cobalt.settings.drc import load_drc_settings

    _clear_drc_rows()
    drc = load_drc_settings(None)
    for family in ("account", "limits", "windows", "goal"):
        model = getattr(drc, family)
        for name in type(model).model_fields:
            assert getattr(model, name) is None, f"{family}.{name}"


# ---------------------------------------------------------------------
# E3 — the change line against cobalt_dev (inside the rollback)
# ---------------------------------------------------------------------


def _constructed_sheets():
    """Constructed grade dollars, written over whatever `cobalt_dev` holds
    INSIDE the rollback, so every asserted value is this file's (L69)."""
    return {
        "aset.sheet_modes": {
            "sheets": {
                "half": {"A_plus": "8", "A": "7", "B": "30", "C": "2", "D": "0"},
                "full": {"A_plus": "16", "A": "14", "B": "60", "C": "4", "D": "0"},
            },
            "order": ["half", "full"],
        },
        "aset.enabled_grades": ["A", "B"],
    }


def _change_form(**over):
    rows = _constructed_sheets()["aset.sheet_modes"]
    form = {"account.daily_stop_full": "", "account.daily_stop_half": ""}
    for sheet, grades in rows["sheets"].items():
        for g, v in grades.items():
            form[f"aset.sheet_modes.{sheet}.{g}"] = v
    form.update(over)
    return form


@pytest.fixture
def change_page(monkeypatch):
    from fastapi.testclient import TestClient
    from test_aset_web import _offline_daymode_config, _offline_sheet_modes_config

    from cobalt.aset import web as web_module
    from cobalt.aset.config import SheetModesConfig
    from cobalt.settings.models import DAYMODE_KEYS, TraderSettings
    from cobalt.settings.store import TraderSettingsStore

    store = TraderSettingsStore()
    _clear_drc_rows()
    cfg = _offline_daymode_config()
    # A COHERENT constructed set: the sheet rows AND the day-mode rows they
    # are cross-checked against (`reduced_enabled_grades` may only narrow
    # `aset.enabled_grades`), so no pre-existing `cobalt_dev` row is mixed in.
    sheets = _constructed_sheets()
    sm = SheetModesConfig(**sheets["aset.sheet_modes"], enabled_grades=sheets["aset.enabled_grades"])
    daymode_rows = {
        k: v for k, v in TraderSettings(sheet_modes=sm, daymode=cfg).rows().items() if k in DAYMODE_KEYS
    }
    store.put({**sheets, **daymode_rows}, source="test:d4-sheets")
    monkeypatch.setattr(web_module, "load_sheet_modes_config", _offline_sheet_modes_config)
    monkeypatch.setattr(
        web_module,
        "_daymode_state",
        lambda: {
            "cfg": cfg, "day": None,
            "row": {"attested_sheet": cfg.hotkey_file_for_mode(cfg.lowest_enabled)},
            "mode": cfg.lowest_enabled, "stage": "stage 1 (system rule)", "error": None,
        },
    )
    return TestClient(web_module.app), store


@requires_db
def test_e3_a_good_apply_writes_through_the_store_and_reads_back(change_page):
    from cobalt.settings.drc import propose_daily_change

    client, store = change_page
    form = _change_form(**{"account.daily_stop_full": "31337", "aset.sheet_modes.full.B": "61"})
    proposal = propose_daily_change(form)
    r = client.post("/settings/daily/apply", data=dict(form, sha256=proposal.sha256))
    assert "Settings saved" in r.text, r.text[-2000:]
    values = store.values()
    for key, value in proposal.payload.items():
        assert values[key] == value, key
    assert values["account.daily_stop_full"] == "31337"
    assert values["aset.sheet_modes"]["sheets"]["full"]["B"] == "61"
    # The trace the store keeps: the row's own source (carrying the
    # payload hash) and its updated_at.
    row = [r for r in store.rows() if r["key"] == "account.daily_stop_full"][0]
    assert proposal.sha256 in row["source"]
    assert row["updated_at"] is not None


@requires_db
def test_e3_an_apply_inside_market_reset_writes_nothing(change_page, monkeypatch):
    from datetime import datetime, timezone

    from cobalt.session import clock as clock_mod
    from cobalt.settings.drc import propose_daily_change

    client, store = change_page
    before = store.rows()
    form = _change_form(**{"account.daily_stop_full": "31337"})
    sha = propose_daily_change(form).sha256
    monkeypatch.setattr(clock_mod, "now_utc", lambda: datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc))
    r = client.post("/settings/daily/apply", data=dict(form, sha256=sha))
    assert "FAILED" in r.text and "MARKET RESET" in r.text
    after = store.rows()
    assert len(after) == len(before)
    assert after == before


@requires_db
def test_e3_a_two_key_apply_with_one_bad_key_writes_neither(change_page):
    client, store = change_page
    before = store.rows()
    form = _change_form(**{"account.daily_stop_full": "31337", "aset.sheet_modes.full.B": "-1"})
    r = client.post("/settings/daily/apply", data=dict(form, sha256="0" * 64))
    assert "FAILED" in r.text and "aset.sheet_modes.full.B" in r.text
    assert store.rows() == before
    assert "account.daily_stop_full" not in store.values()
