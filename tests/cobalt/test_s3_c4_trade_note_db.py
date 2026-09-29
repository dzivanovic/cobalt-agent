"""S3 exits C4 — F22 end to end on `cobalt_dev` (v3 §7; L1, L3, L28, L40).

With-DB, inside the suite's rolled-back transaction with M1 applied there
(`legs_db_support.apply_0021`), so these hold at `0021` and leave nothing
applied (L76). Every vault write goes to a `tmp_path` vault (the one
resolver patched); `vault_writes` / `vault_overrides` rows land in the
suite's transaction and are rolled back. The radar card is the S2-P2
`world` fixture's evaluator card (synthetic `ZZPB`); the manual card is
`legs_db_support.manual_card` (`TEST`). The suite clock is frozen at
2026-09-03 14:00:00 UTC = 10:00:00 ET, so every fill note is named
`Trade-2026-09-03 10-00-00 -<ticker>.md`. Constructed values only (L32).
"""

from __future__ import annotations

import os
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from legs_db_support import card_row, legs_of, manual_card
from test_radar_cards_db import TICKER, world  # noqa: F401  (the fixture)
from test_s3_c3_panel_db import LAST, _armed, _filled, panel_world  # noqa: F401  (the fixture)
from trade_note_support import TRADES_DIR, make_vault

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

RESET = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)   # 20:30 ET — market_reset
RADAR_NOTE = f"Trade-2026-09-03 10-00-00 -{TICKER}.md"
MANUAL_NOTE = "Trade-2026-09-03 10-00-00 -TEST.md"
FAILED_PREFIX = "FILLED — trade note NOT written: "
LEG_NOT_WRITTEN = "leg saved, note unit NOT written"


@pytest.fixture
def note_world(panel_world, monkeypatch):  # noqa: F811
    from cobalt.aset import web as web_module

    # the tmp_path vault is panel_world's (`make_vault` once per tmp_path, C4 fix r1 F1)
    # C1's /fill writes its daily-note FILL UPDATE too (O4 A); stubbed —
    # no vault write outside tmp_path in a test (L28).
    monkeypatch.setattr(web_module, "save_fill_update",
                        lambda *a, **k: ("/dev/null", SimpleNamespace(action="stubbed")))
    return panel_world


def _notes(world):  # noqa: F811
    return sorted(p.name for p in (world["vault"] / TRADES_DIR).iterdir())


def _note(world, name):  # noqa: F811
    return world["vault"] / TRADES_DIR / name


def _unit(text: str, unit: str) -> list[str]:
    from cobalt.prefill.trade_note import LEGS_SECTION
    from cobalt.vaultwrite.markers import find_section

    lines = text.split("\n")
    sec = find_section(lines, LEGS_SECTION)
    assert sec is not None, text
    return sec.units[unit].body(lines)


def _fm(path):
    from cobalt.vaultwrite.frontmatter import split_frontmatter

    return split_frontmatter(path.read_text())[0]


def _manual_fill(world, card_id, price="10.10", shares="100"):  # noqa: F811
    return world["client"].post("/fill", data={
        "card_row_id": str(card_id), "orig_timestamp": "2026-09-03T10:00:00-04:00",
        "actual_fill": price, "fill_shares": shares})


def _exit(world, card_id, *, preset="half", price="5.6000", running_before=100, **extra):  # noqa: F811
    return world["client"].post(f"/radar/card/{card_id}/exit", data={
        "preset": preset, "price": price, "running_before": str(running_before), "prefill": "", **extra})


def _retry(card_id, capsys):
    from cobalt.cards import cli

    cli.cmd_trade_note(SimpleNamespace(card_id=card_id))
    return capsys.readouterr().out


def _break_the_note_writer(monkeypatch):
    from cobalt.prefill import trade_note as trade_note_module
    from cobalt.prefill.vault_writer import VaultWriteError

    def broken(*a, **k):
        raise VaultWriteError("constructed vault failure")

    monkeypatch.setattr(trade_note_module, "upsert_trade_note", broken)


# ---------------------------------------------------------------------
# C4-2 — the fill event
# ---------------------------------------------------------------------


def test_a_radar_fill_writes_its_note_the_path_and_leg_0(note_world):
    card_id = _filled(note_world, shares=100, price=str(LAST))   # the untouched prefill → estimated
    assert _notes(note_world) == [RADAR_NOTE]
    path = _note(note_world, RADAR_NOTE)
    row = card_row(note_world["aset"], card_id)
    assert row["trade_note_path"] == f"{TRADES_DIR}/{RADAR_NOTE}"
    front = _fm(path)
    assert front["entry_price"] == "5.4800" and front["entry_time"] == "2026-09-03 10:00"
    assert front["trade_def"] == row["trade_def_slug"]
    for key in ("exit_price", "exit_time", "profit_loss", "RVOL"):
        assert front[key] is None, key
    assert _unit(path.read_text(), "leg-0") == ["entry · 100 sh @ 5.4800 · 10:00 · estimated"]


def test_a_manual_fill_writes_its_note_with_trade_def_blank(note_world):
    card_id = manual_card(note_world["aset"])
    response = _manual_fill(note_world, card_id)
    assert response.status_code == 200 and "marked FILLED" in response.text, response.text[-1500:]
    assert f"trade note created: {TRADES_DIR}/{MANUAL_NOTE}" in response.text
    path = _note(note_world, MANUAL_NOTE)
    front = _fm(path)
    assert front["entry_price"] == "10.1000" and front["entry_time"] == "2026-09-03 10:00"   # the entry leg's price
    for key in ("trade_def", "exit_price", "exit_time", "profit_loss", "RVOL"):
        assert front[key] is None, key
    assert card_row(note_world["aset"], card_id)["trade_note_path"] == f"{TRADES_DIR}/{MANUAL_NOTE}"
    assert _unit(path.read_text(), "leg-0") == ["entry · 100 sh @ 10.1000 · 10:00 · confirmed"]


def test_two_cards_one_ticker_one_second_is_refused_never_merged(note_world):
    """X16: the second fill's note would be the first's file — refused loud,
    its `trade_note_path` NULL, the first note untouched."""
    first, second = manual_card(note_world["aset"]), manual_card(note_world["aset"])
    assert _manual_fill(note_world, first).status_code == 200
    before = _note(note_world, MANUAL_NOTE).read_text()
    response = _manual_fill(note_world, second, price="10.20")
    assert "marked FILLED" in response.text
    assert FAILED_PREFIX in response.text and f"cobalt cards trade-note {second}" in response.text
    assert card_row(note_world["aset"], second)["trade_note_path"] is None
    assert card_row(note_world["aset"], first)["trade_note_path"] == f"{TRADES_DIR}/{MANUAL_NOTE}"
    assert _note(note_world, MANUAL_NOTE).read_text() == before
    assert note_world["cards"].state_of(second).value == "FILLED"


def test_a_vault_write_failure_leaves_the_card_filled_and_the_path_null(note_world, monkeypatch, capsys):
    card_id = manual_card(note_world["aset"])
    with monkeypatch.context() as patch:
        _break_the_note_writer(patch)
        response = _manual_fill(note_world, card_id)
    assert "marked FILLED" in response.text
    assert (f"{FAILED_PREFIX}constructed vault failure · trade_note_path NULL · retry: "
            f"cobalt cards trade-note {card_id}") in response.text, response.text[-1500:]
    assert note_world["cards"].state_of(card_id).value == "FILLED"
    assert card_row(note_world["aset"], card_id)["trade_note_path"] is None
    assert _notes(note_world) == []
    out = _retry(card_id, capsys)   # the writer back (the context closed); the retry
    assert f"trade note created: {_note(note_world, MANUAL_NOTE)}" in out and "leg-0: updated" in out, out
    assert card_row(note_world["aset"], card_id)["trade_note_path"] == f"{TRADES_DIR}/{MANUAL_NOTE}"
    assert _notes(note_world) == [MANUAL_NOTE]


def test_a_radar_fill_with_a_failed_note_says_so_and_the_retry_writes_every_leg(note_world, monkeypatch, capsys):
    card_id = _armed(note_world)
    client = note_world["client"]
    assert client.post(f"/radar/card/{card_id}/triggered").status_code == 200
    with monkeypatch.context() as patch:
        from cobalt.prefill import trade_note as trade_note_module
        from cobalt.prefill.vault_writer import VaultWriteError

        def broken(*a, **k):
            raise VaultWriteError("constructed vault failure")

        patch.setattr(trade_note_module, "upsert_trade_note", broken)
        filled = client.post(f"/radar/card/{card_id}/fill", data={"price": "5.5000", "shares": "100", "prefill": ""})
        assert filled.status_code == 200, filled.text
        assert filled.json()["trade_note_path"] is None
        assert filled.json()["notice"].startswith(f"{FAILED_PREFIX}constructed vault failure"), filled.json()
        # a leg on a card with NULL trade_note_path: saved, no unit, nothing in the vault
        half = _exit(note_world, card_id)
        assert half.status_code == 200, half.text
        assert half.json()["notice"].startswith(LEG_NOT_WRITTEN), half.json()
        assert _notes(note_world) == []
    out = _retry(card_id, capsys)
    assert "leg-0: updated" in out and "leg-1: updated" in out, out
    text = _note(note_world, RADAR_NOTE).read_text()
    assert _unit(text, "leg-0") == ["entry · 100 sh @ 5.5000 · 10:00 · confirmed"]
    assert _unit(text, "leg-1") == ["exit half · 50 sh @ 5.6000 · 10:00 · confirmed"]
    # a leg after the retry → the same file, one unit per seq
    flat = _exit(note_world, card_id, preset="flat", price="5.7000", running_before=50, confirm="1")
    assert flat.status_code == 200 and flat.json()["closed"] is True, flat.text
    text = _note(note_world, RADAR_NOTE).read_text()
    assert _notes(note_world) == [RADAR_NOTE]
    for unit in ("leg-0", "leg-1", "leg-2"):
        assert text.count(f"<!-- cobalt:unit {unit} -->") == 1
    assert _unit(text, "leg-2") == ["exit flat · 50 sh @ 5.7000 · 10:00 · confirmed"]


def test_a_fill_that_rolls_back_writes_no_note(note_world, monkeypatch):
    from cobalt.aset.store import AsetStore

    card_id = _armed(note_world)            # ARMED, not TRIGGERED: the fill refuses by name
    refused = note_world["client"].post(f"/radar/card/{card_id}/fill",
                                        data={"price": "5.5000", "shares": "100", "prefill": ""})
    assert refused.status_code == 409
    assert note_world["client"].post(f"/radar/card/{card_id}/triggered").status_code == 200

    def cache_fails(self, conn, row_id, fill, **kw):
        raise RuntimeError("constructed cache failure")

    monkeypatch.setattr(AsetStore, "_update_fill_cache", cache_fails)
    client = TestClient(note_world["client"].app, raise_server_exceptions=False)
    rolled = client.post(f"/radar/card/{card_id}/fill", data={"price": "5.5000", "shares": "100", "prefill": ""})
    assert rolled.status_code == 500
    assert note_world["cards"].state_of(card_id).value == "TRIGGERED"
    assert card_row(note_world["aset"], card_id)["trade_note_path"] is None
    assert _notes(note_world) == []


# ---------------------------------------------------------------------
# C4-3 — leg units
# ---------------------------------------------------------------------


def test_a_half_writes_leg_1_and_its_correction_rewrites_the_same_unit(note_world):
    card_id = _filled(note_world, shares=100, price="5.4800")
    assert _exit(note_world, card_id).status_code == 200
    path = _note(note_world, RADAR_NOTE)
    assert _unit(path.read_text(), "leg-1") == ["exit half · 50 sh @ 5.6000 · 10:00 · confirmed"]
    (exit_leg,) = [leg for leg in legs_of(note_world["aset"], card_id) if leg["kind"] == "exit"]
    corrected = note_world["client"].post(f"/radar/card/{card_id}/correct",
                                          data={"leg_id": str(exit_leg["id"]), "price": "5.6100"})
    assert corrected.status_code == 200, corrected.text
    text = path.read_text()
    assert text.count("<!-- cobalt:unit leg-1 -->") == 1
    assert _unit(text, "leg-1") == ["exit half · 50 sh @ 5.6100 · 10:00 · confirmed"]


def test_his_edit_of_a_leg_line_wins_over_a_correction(note_world):
    from cobalt.vaultwrite import VaultWriteStore

    card_id = _filled(note_world, shares=100, price="5.4800")
    assert _exit(note_world, card_id).status_code == 200
    path = _note(note_world, RADAR_NOTE)
    path.write_text(path.read_text().replace("50 sh @ 5.6000", "50 sh @ 5.6050 (my print)"))
    (exit_leg,) = [leg for leg in legs_of(note_world["aset"], card_id) if leg["kind"] == "exit"]
    corrected = note_world["client"].post(f"/radar/card/{card_id}/correct",
                                          data={"leg_id": str(exit_leg["id"]), "price": "5.6100"})
    assert corrected.status_code == 200, corrected.text
    assert _unit(path.read_text(), "leg-1") == ["exit half · 50 sh @ 5.6050 (my print) · 10:00 · confirmed"]
    overrides = VaultWriteStore().overrides_for(str(path))
    assert [o["human_text"] for o in overrides] == ["exit half · 50 sh @ 5.6050 (my print) · 10:00 · confirmed"]
    current = [leg for leg in legs_of(note_world["aset"], card_id) if leg["kind"] == "exit"][-1]
    assert str(current["price"]) == "5.6100"          # the DB leg is never changed from the note


def test_a_close_through_one_confirmed_exit_fills_his_blank_exit_keys(note_world):
    card_id = _filled(note_world, shares=100, price="5.4800")
    flat = _exit(note_world, card_id, preset="flat", price="5.7000", confirm="1")
    assert flat.status_code == 200 and flat.json()["closed"] is True, flat.text
    front = _fm(_note(note_world, RADAR_NOTE))
    assert (front["exit_price"], front["exit_time"]) == ("5.7000", "2026-09-03 10:00")
    assert front["profit_loss"] is None and front["RVOL"] is None


def test_a_close_through_two_exits_fills_exit_time_and_leaves_exit_price_blank(note_world):
    card_id = _filled(note_world, shares=100, price="5.4800")
    path = _note(note_world, RADAR_NOTE)
    path.write_text(path.read_text().replace("exit_price:\n", 'exit_price: "5.5100"\n'))   # his value
    assert _exit(note_world, card_id).status_code == 200
    flat = _exit(note_world, card_id, preset="flat", price="5.7000", running_before=50, confirm="1")
    assert flat.json()["closed"] is True, flat.text
    front = _fm(path)
    assert front["exit_time"] == "2026-09-03 10:00"
    assert front["exit_price"] == "5.5100"            # his, never overwritten


# ---------------------------------------------------------------------
# C4-06 — a tap price is a positive number
# ---------------------------------------------------------------------


def test_a_nan_exit_price_is_refused_before_the_writer(note_world):
    card_id = _filled(note_world, shares=100, price="5.4800")
    before = legs_of(note_world["aset"], card_id)
    response = _exit(note_world, card_id, price="NaN")
    assert response.status_code == 422, response.text
    assert response.json()["reason"] == "REFUSED: the exit price 'NaN' is not a positive price. Nothing written."
    assert legs_of(note_world["aset"], card_id) == before


def test_a_negative_correction_price_is_refused_verbatim(note_world):
    card_id = _filled(note_world, shares=100, price="5.4800")
    (entry,) = legs_of(note_world["aset"], card_id)
    client = TestClient(note_world["client"].app, raise_server_exceptions=False)
    response = client.post(f"/radar/card/{card_id}/correct", data={"leg_id": str(entry["id"]), "price": "-1"})
    assert response.status_code == 422, response.text
    assert response.json()["reason"] == "REFUSED: the corrected price '-1' is not a positive price. Nothing written."
    assert legs_of(note_world["aset"], card_id) == [entry]


# ---------------------------------------------------------------------
# C4-4 — the retry CLI; the session gate
# ---------------------------------------------------------------------


def test_the_retry_in_market_reset_is_refused_and_writes_nothing(note_world, monkeypatch, capsys):
    from cobalt.session import clock

    card_id = _filled(note_world, shares=100, price="5.4800")
    path = _note(note_world, RADAR_NOTE)
    before = path.read_text()
    monkeypatch.setattr(clock, "now_utc", lambda: RESET)
    with pytest.raises(SystemExit, match="MARKET RESET"):
        _retry(card_id, capsys)
    assert path.read_text() == before
    assert card_row(note_world["aset"], card_id)["trade_note_path"] == f"{TRADES_DIR}/{RADAR_NOTE}"


def test_the_retry_refuses_a_card_that_is_not_filled(note_world, capsys):
    card_id = manual_card(note_world["aset"])            # TRIGGERED
    with pytest.raises(SystemExit, match="FILLED or CLOSED"):
        _retry(card_id, capsys)
    assert _notes(note_world) == []


# ---------------------------------------------------------------------
# C4 fix r1 — RUN U1 (L70): run, never argued. It PRINTS what happened
# and asserts NOTHING about the outcome.
# ---------------------------------------------------------------------


def test_run_u1_a_nan_or_negative_price_posted_to_the_manual_fill(note_world):
    from test_s3_c3_panel_db import _counts

    client = TestClient(note_world["client"].app, raise_server_exceptions=False)
    print("\nRUN U1 · POST /fill on a fresh manual card per input")
    for price in ("NaN", "-1"):
        card_id = manual_card(note_world["aset"])
        before = _counts(note_world)
        response = client.post("/fill", data={
            "card_row_id": str(card_id), "orig_timestamp": "2026-09-03T10:00:00-04:00",
            "actual_fill": price, "fill_shares": "100"})
        after = _counts(note_world)
        row = card_row(note_world["aset"], card_id)
        print(f"U1 /fill card {card_id} actual_fill={price!r} → {response.status_code} · "
              f"body[:200]={response.text[:200]!r}")
        print(f"U1   counts before {before} · after {after} · legs {before['legs']} → {after['legs']}")
        print(f"U1   card row: state={row['state']!r} actual_fill={row['actual_fill']!r} "
              f"trade_note_path={row['trade_note_path']!r}")


# ---------------------------------------------------------------------
# X3 on the real `vault_writes` store (the offline finding, repeated)
# ---------------------------------------------------------------------


def test_x3_human_wins_once_on_the_real_store(tmp_path, monkeypatch):
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    vault = make_vault(monkeypatch, tmp_path)
    path = vault / TRADES_DIR / "Trade-2026-09-03 10-00-00 -TEST.md"
    store = VaultWriteStore()
    store.ensure_schema()
    body = "entry · 100 sh @ 10.0000 · 10:00 · confirmed"
    template = ("---\nsymbol: TEST\n---\n\n<!-- cobalt:section cobalt-legs -->\n"
                "<!-- /cobalt:section cobalt-legs -->\n")
    VaultWriter("prefill.trade_note", store=store).create_if_absent(path, template)
    VaultWriter("prefill.trade_note", store=store).upsert_unit(path, "cobalt-legs", "leg-0", body)
    path.write_text(path.read_text().replace("10.0000", "10.0100 (my fill)"))
    first = VaultWriter("prefill.trade_note", store=store).upsert_unit(path, "cobalt-legs", "leg-0", body)
    kept_first = "(my fill)" in path.read_text()
    second = VaultWriter("prefill.trade_note", store=store).upsert_unit(path, "cobalt-legs", "leg-0", body)
    kept_second = "(my fill)" in path.read_text()
    print(f"\nX3 real store: retry 1 {first.action} kept={kept_first} overrides={len(first.overrides)} · "
          f"retry 2 {second.action} kept={kept_second} overrides={len(second.overrides)} · "
          f"override rows {len(store.overrides_for(str(path)))}")
    assert (kept_first, kept_second) == (True, False)
