"""DRC K3 — THE SURFACES, WITH-DB half (card `01-drc-k3-card.md`; v3 §3's
read-back proof through the page actions).

The DRC harness BY IMPORT (`test_drc_store.py`'s `migrated` /
`weekday_calendar` / `requires_db`; `test_drc_k1_store.py`'s `TEN_ET` /
`RESET_ET` / `_row`; `test_drc_imports_db.py`'s `_drop`; `test_drc_build.py`'s
`_deps`). Everything runs inside `migrated`'s never-committed transaction
(L76; the card's TREE STATE: no forward is left applied). D3's build runs
with `_deps` over the REAL `DrcStore` and a `tmp_path` vault. Constructed
2001 dates and symbols only (L32 / L45).
"""

from __future__ import annotations

import pytest

from cobalt.drc.store import DrcStore

from test_drc_build import _deps, _note, _unit_body
from test_drc_imports_db import _drop
from test_drc_k1_store import RESET_ET, TEN_ET, _row, _state
from test_drc_k2_experiments import EEE_ROUND
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)

EXIT_NOT_IN_ANY_EXPORT = "not computed — exit not in any export"


@pytest.fixture
def k3_lane(migrated, weekday_calendar, tmp_path, monkeypatch):
    """A `tmp_path` vault; D3's build with `_deps` over the real store (its
    cards, settings and replay reads constructed); the session block store
    quiet. Returns the vault root."""
    from cobalt.drc import build
    from cobalt.session.store import SessionBlockStore
    from cobalt.vault import DRC_IMPORTS_REL

    from test_drc_build import _vault

    root = _vault(tmp_path)
    (root / DRC_IMPORTS_REL).mkdir(parents=True, exist_ok=True)
    monkeypatch.setenv("COBALT_VAULT_PATH", str(root))
    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: None)
    monkeypatch.setattr(build, "default_deps", lambda vault_root=None, **over: _deps(DrcStore(), root))
    return root


def _stated(conn):
    return conn.execute(
        'SELECT kind, via, positions, supersedes FROM "user".drc_stated_books ORDER BY id').fetchall()


@requires_db
def test_superseded_stated_ids_reads_the_current_predicate(migrated, weekday_calendar):
    """K3-4 (a): `DrcStore.superseded_stated_ids(ids)` — the ids no longer
    current (another row's `supersedes`); a current id and an unknown id are
    not in it. A READ: no row written."""
    first = _state(D, kind="resolve", positions=[{"trade_id": "DDD-long-x"}])
    second = _state(D_NEXT, kind="resolve", positions=[{"trade_id": "DDD-long-x"}], supersedes=first.id)
    before = _stated(migrated)
    assert DrcStore().superseded_stated_ids([first.id, second.id, 999_999]) == {first.id}
    assert DrcStore().superseded_stated_ids([]) == set()
    assert _stated(migrated) == before


@requires_db
def test_i_was_flat_writes_one_drc_page_opening_and_the_first_import_pairs(k3_lane, migrated):
    """v3 §3 read-back (4): a first import with no statement is unpaired; the
    page's `[I was flat]` → ONE `drc_stated_books` row `opening` / `drc_page`
    / `[]`; the day rebuilt and paired; its note's unit `left open: …`."""
    from cobalt.drc import imports

    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    assert "pairing" in _row(migrated, D, "day")[1]["not_computed"]
    result = imports.state_book(D, [], now=TEN_ET)
    assert _stated(migrated) == [("opening", "drc_page", [], None)]
    assert result.status_line == "rebuilt: 2001-01-02", result
    assert _row(migrated, D, "book_close")[1]["count"] == 1
    assert _unit_body(_note(k3_lane), "drc-trades", "open_positions")[0].startswith("left open: 1 — ")


@requires_db
def test_a_listed_book_is_written_only_with_the_previewed_sha(k3_lane, migrated):
    from cobalt.drc import imports

    ggg = {"symbol": "GGG", "direction": "short", "shares": 40, "avg_cost": None}
    preview = imports.state_book(D, [ggg], now=TEN_ET)
    assert _stated(migrated) == []
    bad = imports.state_book(D, preview.preview.positions, expected_sha256="0" * 64, now=TEN_ET)
    assert bad.refused.endswith("— nothing written") and _stated(migrated) == []
    imports.state_book(D, preview.preview.positions, expected_sha256=preview.preview.sha256, now=TEN_ET)
    ((kind, via, positions, _),) = _stated(migrated)
    assert (kind, via, [p["symbol"] for p in positions]) == ("opening", "drc_page", ["GGG"])


@requires_db
def test_resolve_closes_the_carried_trade_and_the_unit_and_a31_drop_it(k3_lane, migrated):
    """v3 §3 read-back (2) + (6): day 1 leaves DDD open; day 2 carries it
    (`continuing open position`); RESOLVE with no exit price → one `resolve`
    row via `drc_page`, the rebuild, the note re-upserted: the unit and A31
    no longer list it; the page shows it CLOSED with the literal."""
    from cobalt.drc import imports

    imports.state_book(D, [], now=TEN_ET)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    _drop(D_NEXT, EEE_ROUND, STATS.read_bytes())
    tid = _row(migrated, D, "book_close")[1]["trade_ids"][0]
    assert "continuing open position" in _unit_body(_note(k3_lane, D_NEXT), "drc-trades", "open_positions")[1]
    preview = imports.resolve(D_NEXT, tid, now=TEN_ET)
    done = imports.resolve(D_NEXT, tid, expected_sha256=preview.preview.sha256, now=TEN_ET)
    assert done.status_line == "rebuilt: 2001-01-03", done
    assert _stated(migrated)[-1][:2] == ("resolve", "drc_page")
    assert _unit_body(_note(k3_lane, D_NEXT), "drc-trades", "open_positions") == [
        "left open: 0 — tomorrow starts flat (stated by this DRC)"]
    assert _unit_body(_note(k3_lane, D_NEXT), "drc-open-items", "open_positions") == [
        "open items carried forward — open positions: none"]
    view = imports.day_view(D_NEXT, vault_root=k3_lane)
    assert any(line.startswith(f"{tid}: CLOSED · realized {EXIT_NOT_IN_ANY_EXPORT}") for line in view.resolves)


@requires_db
def test_inside_market_reset_the_page_writes_no_row(k3_lane, migrated):
    from cobalt.drc import imports

    assert imports.state_book(D, [], now=RESET_ET).refused == imports.RESET_REFUSAL
    assert imports.resolve(D, "DDD-long-x", now=RESET_ET).refused == imports.RESET_REFUSAL
    assert _stated(migrated) == []
