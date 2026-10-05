"""DRC D5 — THE RECONCILE, WITH-DB half (card `prompts/2026-10-04/03-drc-d5-card.md`
rows D5-2, D5-3; v2 `:80`, S-C2, R90).

The real writer (`cobalt.cards.legs`), the real `DrcStore`, D2's route
(`imports.place` → the event → `run_drc_build`) and K3-7's RESOLVE. Everything
runs inside `test_drc_store.py`'s `migrated` transaction — FORWARD applied
there, `0021` (`legs`) with it, never committed (L76); the legs writer's own
connection is that transaction's savepoint proxy (`db.connect` patched by
`migrated`). Row T: the gate runs this file in PASS 2 (the legs writer at
`0021`) and deselects it in PASS 1 (`ops/desk/gate-lists.md`).

The card is a manual `TEST` card saved, armed, triggered and filled through
the sheet's own store (`legs_db_support`); the build's card list is that row
with `created_at` set inside the constructed day's match window (the card
match is D3's, `limits.card_match_window_minutes` = 30 here). Constructed
2001 dates, the constructed `TEST` symbol and prices only (L32 / L45); every
note in a `tmp_path` vault. Ticker written to `aset_sizings`: `TEST`.
"""

from __future__ import annotations

import argparse
import importlib
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from cobalt.drc.store import DrcStore
from cobalt.session.clock import ET

from legs_db_support import card_row, fill_kwargs, legs_of, manual_card, patch_daymode
from test_drc_build import _note, _Settings, _unit_body, _vault
from test_drc_imports_db import _drop
from test_drc_k1_store import TEN_ET
from test_drc_k2_experiments import EEE_ROUND, _log
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)
from test_replay_line import MemoryWriteStore

#: The suite's frozen instant (`conftest.FROZEN_NOW`, 10:00 ET): his fill and taps.
FROZEN = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
#: In the constructed day's window: 5 minutes before the first fill.
CARD_CREATED = datetime(2001, 1, 2, 9, 35, tzinfo=ET)
#: TEST long 100 @ 10.1, out 50 @ 10.25 and 50 @ 10.4 — closed.
TEST_ROUND = _log(
    "10:05:00,TEST,S,10.4,50,ROUTE1,BRK1,ACCT1,Margin,H0000000000603,",
    "09:50:00,TEST,S,10.25,50,ROUTE1,BRK1,ACCT1,Margin,H0000000000602,",
    "09:40:00,TEST,B,10.1,100,ROUTE2,BRK2,ACCT1,Margin,H0000000000601,",
)
#: TEST long 100 @ 10.1, out 60 @ 10.25 — 40 held at file end (X11's export).
TEST_OPEN = _log(
    "09:50:00,TEST,S,10.25,60,ROUTE1,BRK1,ACCT1,Margin,H0000000000605,",
    "09:40:00,TEST,B,10.1,100,ROUTE2,BRK2,ACCT1,Margin,H0000000000604,",
)


@pytest.fixture
def d5_lane(migrated, weekday_calendar, tmp_path, monkeypatch):
    """A `tmp_path` vault; THE build's own `default_deps` (so its legs door is
    the production one) with the non-leg readers constructed; the session
    block store quiet; the sheet's store. Returns (root, aset, cards) —
    `cards` is the list the build's card read returns."""
    from cobalt.aset.store import AsetStore
    from cobalt.session.store import SessionBlockStore
    from cobalt.vault import DRC_IMPORTS_REL

    build = importlib.import_module("cobalt.drc.build")  # the module `imports` calls (K3's lane note)
    root = _vault(tmp_path)
    (root / DRC_IMPORTS_REL).mkdir(parents=True, exist_ok=True)
    monkeypatch.setenv("COBALT_VAULT_PATH", str(root))
    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: None)
    patch_daymode(monkeypatch)
    cards: list[dict] = []
    real = build.default_deps

    def deps(vault_root=None, **over):
        return real(
            root, store=DrcStore(), cards=lambda day: list(cards),
            card_counts=lambda day: (len(cards), len(cards)), drc_settings=lambda: _Settings(30),
            daily_stop=lambda: {"full": None, "half": None},
            risk_parameters=lambda c: "no sheet-mode cards today",
            rules_block=lambda: "- [ ] constructed rule one #process", daily_note=lambda day: None,
            replay_result=lambda: None, write_store=MemoryWriteStore(), now=lambda: TEN_ET, **over,
        )

    monkeypatch.setattr(build, "default_deps", deps)
    aset = AsetStore("cobalt_dev")
    aset.ensure_schema()
    return root, aset, cards


def _filled(aset, *, shares: int = 100, price: str = "10.10") -> int:
    card_id = manual_card(aset)
    aset.mark_filled(card_id, **fill_kwargs(price=price, shares=shares, p=20))
    return card_id


def _listed(aset, cards, card_id) -> None:
    cards.append({**card_row(aset, card_id), "created_at": CARD_CREATED})


def _tap(card_id, preset, running_before, price):
    from cobalt.cards import legs

    return legs.record_exit(
        card_id, preset=preset, price=Decimal(price), price_source="last_poll", price_asof=FROZEN,
        flag="estimated", source="panel", running_before=running_before, now=FROZEN,
    )


def _running(aset, card_id) -> int:
    from cobalt.cards import legs

    with aset._connect() as conn:
        return legs.running_shares(conn, card_id).shares


def _reconcile(root, day=D):
    return _unit_body(_note(root, day), "drc-trades", "reconcile")


def _a31(root, day=D):
    return _unit_body(_note(root, day), "drc-open-items", "open_positions")


@requires_db
def test_d5_2_with_db_a_half_tapped_at_a_price_the_export_disagrees_with_is_corrected_naming_the_import(
    d5_lane, migrated
):
    """D5-2 (the row's red): ½ off tapped at 10.20, the export says 50 @
    10.25 then 50 @ 10.40 → after the event's build a `trading_log`
    correction of the tapped leg naming the import, every new row naming it,
    and running = the export's 0 (the card CLOSED by the writer)."""
    from cobalt.drc import imports

    root, aset, cards = d5_lane
    card = _filled(aset)
    tap = _tap(card, "half", 100, "10.20")
    _listed(aset, cards, card)
    imports.state_book(D, [], now=TEN_ET)
    result = _drop(D, TEST_ROUND, STATS.read_bytes())
    assert result.status_line.startswith("READY → DRC built"), result
    import_id = DrcStore().event_for(D)["import_id"]
    rows = legs_of(aset, card)
    fixes = [r for r in rows if r["corrects"] == tap.leg_id]
    assert fixes, f"no correction of the tapped leg #{tap.leg_id}: {[(r['id'], r['source']) for r in rows]}"
    (fix,) = fixes
    assert (fix["source"], fix["source_import_id"], fix["price"]) == ("trading_log", import_id, Decimal("10.2500"))
    assert all(r["source_import_id"] == import_id for r in rows if r["source"] == "trading_log")
    assert {r["source"] for r in rows if r["source"] != "trading_log"} == {"sheet", "panel"}  # his rows stay
    assert _running(aset, card) == 0
    assert card_row(aset, card)["state"] == "CLOSED"
    written = [r["id"] for r in rows if r["source"] == "trading_log"]
    assert f"  adjusted to DAS: {len(written)} rows ({', '.join(f'#{i}' for i in written)})" in _reconcile(root)


@requires_db
def test_d5_2_with_db_negative_control_the_dry_run_adds_no_legs_row(d5_lane, migrated, monkeypatch, capsys):
    """D5-2 negative control: the same day, `cobalt drc build --dry-run`
    (`plan_note` alone) → no `legs` row added. The route's own build is held
    (D2's `BuildNotBuilt` path) so the dry run meets the un-reconciled legs."""
    from cobalt.drc import cli, imports

    root, aset, cards = d5_lane
    card = _filled(aset)
    _tap(card, "half", 100, "10.20")
    _listed(aset, cards, card)
    imports.state_book(D, [], now=TEN_ET)

    def held(event):
        raise imports.BuildNotBuilt("held for the dry run")

    monkeypatch.setattr(imports, "_run_build", held)
    _drop(D, TEST_ROUND, STATS.read_bytes())
    before = legs_of(aset, card)
    cli.cmd_build(argparse.Namespace(date=D, dry_run=True, no_trades=False))
    out = capsys.readouterr().out
    assert "DRY RUN: nothing written" in out, out
    assert legs_of(aset, card) == before


@requires_db
def test_d5_3_with_db_x11_refused_built_carried_offered_and_cleared_by_resolve(d5_lane, migrated):
    """D5-3 (the row's red, X11's shape): his flat tap CLOSED the card on 100,
    the export shows 60 out → the writer refuses (`closed_off_zero`); the DRC
    is built with `unresolved: card <id> — <refusal>` in the reconcile unit
    and A31; the next day's build carries it and its page offers K3-7's
    RESOLVE beside it; after the resolve row for that trade it is gone."""
    from cobalt.drc import imports

    root, aset, cards = d5_lane
    card = _filled(aset)
    _tap(card, "flat", 100, "10.20")
    assert card_row(aset, card)["state"] == "CLOSED"
    _listed(aset, cards, card)
    imports.state_book(D, [], now=TEN_ET)
    result = _drop(D, TEST_OPEN, STATS.read_bytes())
    assert result.status_line.startswith("READY → DRC built"), result
    prefix = f"unresolved: card {card} — REFUSED card {card}: CLOSED has no way back"
    assert any(l.startswith(prefix) for l in _reconcile(root)), _reconcile(root)
    assert any(l.startswith(prefix) for l in _a31(root)), _a31(root)
    assert _running(aset, card) == 0 and card_row(aset, card)["state"] == "CLOSED"  # never forced

    nxt = _drop(D_NEXT, EEE_ROUND, STATS.read_bytes())
    assert nxt.status_line.startswith("READY → DRC built"), nxt
    assert any(l.startswith(prefix) for l in _reconcile(root, D_NEXT)), _reconcile(root, D_NEXT)
    assert any(l.startswith(prefix) for l in _a31(root, D_NEXT))
    view = imports.day_view(D_NEXT, vault_root=root)
    (offer,) = view.unresolved
    assert offer.line.startswith(prefix) and offer.resolve is True and offer.trade_id in view.carried

    preview = imports.resolve(D_NEXT, offer.trade_id, now=TEN_ET)
    done = imports.resolve(D_NEXT, offer.trade_id, expected_sha256=preview.preview.sha256, now=TEN_ET)
    assert done.status_line == "rebuilt: 2001-01-03", done
    assert not any(l.startswith("unresolved:") for l in _reconcile(root, D_NEXT)), _reconcile(root, D_NEXT)
    assert not any(l.startswith("unresolved:") for l in _a31(root, D_NEXT))
    assert any(l.startswith(prefix) for l in _reconcile(root))  # D's own note keeps its record
