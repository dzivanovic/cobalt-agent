"""F5 — `system.market_checkpoints` on `cobalt_dev` (card 731 row K12; FINAL §6 with-DB; X9, X14).

`0029_market_checkpoints` is applied inside the suite's rolled-back
transaction only (L76, the `test_strike_stream_db.py` `apply_0024` shape);
the gate runs this file in PASS 2 (`ops/desk/gate-lists.md`). The run's
vault is F4's `tmp_path` vault and every Finviz / model / DM seam is the
offline file's fake. Constructed figures and dates only (L32).
"""

from __future__ import annotations

import os
from datetime import date

import pytest

from test_checkpoints_offline import DAY, at, cp, run  # noqa: F401 — the fixture
from test_prefill_refresh import finviz, plan, vault  # noqa: F401 — F4's fixtures

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
pytestmark = [requires_db, pytest.mark.integration]


def _migration(name: str) -> str:
    from cobalt.db_migrations import MIGRATIONS_DIR

    return (MIGRATIONS_DIR / name).read_text()


def _store(applied: bool = True):
    from cobalt.prefill.checkpoints import CheckpointStore

    store = CheckpointStore("cobalt_dev")
    if applied:
        with store._connect() as conn:
            conn.execute(_migration("0029_market_checkpoints.sql"))
    return store


def _exists(store) -> bool:
    with store._connect() as conn:
        return conn.execute("SELECT to_regclass('system.market_checkpoints') IS NOT NULL").fetchone()[0]


def test_migration_round_trip():
    store = _store()
    assert _exists(store)
    with store._connect() as conn:
        conn.execute(_migration("0029_market_checkpoints.rollback.sql"))
    assert not _exists(store)
    with store._connect() as conn:
        conn.execute(_migration("0029_market_checkpoints.sql"))
        conn.execute(_migration("0029_market_checkpoints.sql"))  # idempotent
    assert _exists(store)
    figures = {"indices": {"SPY": {"price": "500.00", "change_pct": "0.10"}}, "sectors": None}
    row_id = store.upsert(DAY, "07:45", figures=figures, source_status={"finviz-screener": "ok"},
                          delta={"lines": [], "groups_failed": None}, narrative_status="pending",
                          write_status="pending", vault_write_id=None, fetched_at=at(7, 45))
    row = store.get(DAY, "07:45")
    assert row["id"] == row_id and row["figures"] == figures and row["vault_write_id"] is None
    assert row["trade_date"] == DAY and row["slot"] == "07:45"
    assert store.slots_on(DAY) == {"07:45"}


def test_unique_rerun_keeps_one_row(cp):  # noqa: F811
    cp.store = _store()
    run(cp, "0745", at(7, 45))
    first = cp.store.get(DAY, "07:45")
    cp.indices["SPY"] = ("502.00", "0.40")
    run(cp, "0745", at(7, 50))
    second = cp.store.get(DAY, "07:45")
    assert second["id"] == first["id"]
    assert second["figures"]["indices"]["SPY"]["price"] == "502.00"
    with cp.store._connect() as conn:
        assert conn.execute("SELECT count(*) FROM market_checkpoints WHERE trade_date = %s AND slot = %s",
                            (DAY, "07:45")).fetchone()[0] == 1


def test_0815_base_is_a_copy(cp):  # noqa: F811
    cp.store = _store()
    run(cp, "0745", at(7, 45))
    run(cp, "0815", at(8, 15))
    row = cp.store.get(DAY, "08:15")
    assert row["base_slot"] == "07:45"
    assert row["base_figures"] == cp.store.get(DAY, "07:45")["figures"]
    replay = (row["base_figures"], row["delta"])
    cp.indices["SPY"] = ("590.00", "1.90")
    run(cp, "0745", at(8, 14))  # a later 07:45 re-run, inside its window, with new figures
    assert cp.store.get(DAY, "07:45")["figures"]["indices"]["SPY"]["price"] == "590.00"
    again = cp.store.get(DAY, "08:15")
    assert (again["base_figures"], again["delta"]) == replay, "08:15 replays its own copy (X9, L57)"


def test_purge_with_a_checkpoint_row_succeeds():
    from cobalt.vaultwrite import VaultWriteStore

    store = _store()
    writes = VaultWriteStore("cobalt_dev")
    writes.ensure_schema()
    with writes.pending_write(note="/constructed/note.md", section="market_context", unit="checkpoint_0745",
                              before=None, after="x", unit_before=None, unit_after="x", hash_before=None,
                              hash_after="0" * 64, writer="prefill.checkpoint", run_id="constructed",
                              session="premarket") as write_id:
        pass
    with writes._connect() as conn:
        conn.execute("UPDATE vault_writes SET ts = now() - interval '40 days' WHERE id = %s", (write_id,))
    store.upsert(date(2026, 8, 3), "07:45", figures={"indices": None, "sectors": None}, vault_write_id=write_id)
    assert writes.purge_expired() >= 1
    with writes._connect() as conn:
        assert conn.execute("SELECT count(*) FROM vault_writes WHERE id = %s", (write_id,)).fetchone()[0] == 0
    assert store.get(date(2026, 8, 3), "07:45")["vault_write_id"] == write_id, "no FK: the pointer outlives the row"
