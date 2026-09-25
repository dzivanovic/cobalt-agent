"""DRC D2 — the first-gate experiments E5 / E11 / X13 / X-NT (L70), run
BEFORE any D2 code (`prompts/2026-09-25/07-drc-d2-build.md` `## E1`).

- E5 is offline: the ASET stack's multipart parse, with the transitive
  `python-multipart` (v2 `:109`).
- E11 (stub) and X13 are written as RED tests against the not-yet-built
  `cobalt.drc.imports` (every D2 symbol is imported INSIDE the test body,
  so each is its own red until the code exists); their pass conditions
  are D2-5 and D2-3's.
- X-NT is a with-DB fact of the base: can an EXISTING path write a
  `drc_imports` row that carries no file (the no-trade event's home)?

E2 (screenshot legibility) is moot under R91; E7 (LAN reach from the
trading PC) is an ops read after the deploy. Neither runs here.

Constructed dates and symbols, D1's fixtures only (L32 / L45). WITH-DB
tests run inside `test_drc_store.py`'s never-committed migration
transaction (L76): nothing here commits a migration.
"""

from __future__ import annotations

import sys
import types
from datetime import date

import psycopg
import pytest

# Module level, not inside the test: under `from __future__ import
# annotations` a route's annotation is a string FastAPI resolves in the
# MODULE's globals (E5's first run failed on exactly that — see the report).
from fastapi import FastAPI, File, Form, UploadFile
from fastapi.testclient import TestClient

from cobalt.drc.models import ImportResult, Kind, Outcome
from cobalt.drc.store import DrcStore

from test_drc_k1_store import TEN_ET, _raises, _state
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    DAY1,
    E1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)


# ---------------------------------------------------------------------
# E5 — v2 `:109`
# ---------------------------------------------------------------------


def test_e5_multipart_uploadfile_parses_with_the_transitive_dependency():
    """E5 (v2 `:109`): "multipart `UploadFile` in the dev ASET app with the
    transitive `python-multipart`" — PASS: "works → pin direct; fails →
    the dependency is added knowingly, still not a new package". A minimal
    FastAPI app with one `UploadFile` route; the TestClient posts D1's
    trading-log fixture bytes; the route reads the same bytes back."""
    app = FastAPI()

    @app.post("/probe")
    async def probe(date: str = Form(...), files: list[UploadFile] = File(...)):
        return {
            "date": date,
            "files": [{"name": f.filename, "data": (await f.read()).hex()} for f in files],
        }

    data = E1.read_bytes()
    response = TestClient(app).post(
        "/probe",
        data={"date": "2001-01-02"},
        files=[("files", ("constructed.md", data, "application/octet-stream"))],
    )
    assert response.status_code == 200, response.text
    body = response.json()
    assert body["date"] == "2001-01-02"
    assert [f["name"] for f in body["files"]] == ["constructed.md"]
    assert bytes.fromhex(body["files"][0]["data"]) == data


# ---------------------------------------------------------------------
# E11 (stub) — v2 `:115`
# ---------------------------------------------------------------------


def _stub_build(monkeypatch, run):
    """D3's ONE entry, `cobalt.drc.build.run_drc_build`, as a stub."""
    module = types.ModuleType("cobalt.drc.build")
    module.run_drc_build = run
    monkeypatch.setitem(sys.modules, "cobalt.drc.build", module)


def _vault(tmp_path, monkeypatch):
    root = tmp_path / "vault"
    (root / "1 - Trading" / "5 - Review").mkdir(parents=True)
    monkeypatch.setenv("COBALT_VAULT_PATH", str(root))
    return root


@requires_db
def test_e11_stub_a_build_that_raises_after_pending_leaves_the_row_failed(
    migrated, weekday_calendar, tmp_path, monkeypatch
):
    """E11 (v2 `:115`): "Kill the ASET request after `pending` and before
    `done`. Pass: the row is `failed` and the page is not `DRC built`."
    The STUB half (D2-5): a build that raises after `pending` → `failed`
    with the reason; a build that returns → `done`. (The dead-REQUEST kill
    is re-proven by D3 on the real build.)"""
    from cobalt.drc import imports

    _vault(tmp_path, monkeypatch)

    def _raise(event):
        raise RuntimeError("constructed kill after pending")

    _stub_build(monkeypatch, _raise)
    _state(D)
    result = imports.place(D, [("a.md", DAY1.read_bytes()), ("b.md", STATS.read_bytes())], now=TEN_ET)
    event = DrcStore().event_for(D)
    assert event["state"] == "failed"
    assert "constructed kill after pending" in event["error"]
    assert "DRC built" not in result.status_line
    assert "DRC built" not in imports.render_status(imports.day_view(D))


@requires_db
def test_e11_stub_a_build_that_returns_leaves_the_row_done(
    migrated, weekday_calendar, tmp_path, monkeypatch
):
    """E11 (stub), the other half: a build that returns → `done`, and only
    then `READY → DRC built: <note path>`."""
    from cobalt.drc import imports

    _vault(tmp_path, monkeypatch)
    _stub_build(monkeypatch, lambda event: "constructed/DRC-note.md")
    _state(D)
    result = imports.place(D, [("a.md", DAY1.read_bytes()), ("b.md", STATS.read_bytes())], now=TEN_ET)
    assert DrcStore().event_for(D)["state"] == "done"
    assert result.status_line == "READY → DRC built: constructed/DRC-note.md"


# ---------------------------------------------------------------------
# X13 — v2 `:119`
# ---------------------------------------------------------------------


@requires_db
def test_x13_a_superseding_log_that_drops_a_bound_trade_lists_the_binding_orphaned(
    migrated, weekday_calendar, tmp_path, monkeypatch
):
    """X13 (v2 `:119`): "a superseding export that changes or drops a
    trade's key after a screenshot was bound to it: is the binding listed
    as orphaned, silently re-bound, or deleted". D2-3's rule: listed
    `orphaned: <file> — trade <key> not in the current trading log` on the
    page and on the event — never re-bound, never deleted."""
    from cobalt.drc import imports
    from test_drc_k2_experiments import EEE_ROUND

    _vault(tmp_path, monkeypatch)
    _stub_build(monkeypatch, lambda event: "constructed/DRC-note.md")
    _state(D)
    imports.place(D, [("a.md", DAY1.read_bytes()), ("b.md", STATS.read_bytes())], now=TEN_ET)
    with DrcStore()._connect() as conn:
        key = conn.execute(
            "SELECT ref FROM drc_rows WHERE day = %s AND kind = 'trade' ORDER BY ref LIMIT 1", (D,)
        ).fetchone()[0]
        # The screenshot row's SHAPE is 0016's (`kind = 'screenshot'`, a
        # `trade_key`); constructed here because no store path writes one
        # on this tree (the build report's ESCALATE names the gap).
        shot = conn.execute(
            "INSERT INTO drc_imports (import_date, kind, name, sha256, trade_key, parse_status) "
            "VALUES (%s, 'screenshot', 'shot.png', %s, %s, 'parsed') RETURNING id",
            (D, "0" * 64, key),
        ).fetchone()[0]
    result = imports.place(D, [("c.md", EEE_ROUND)], now=TEN_ET)
    line = f"orphaned: shot.png — trade {key} not in the current trading log"
    assert line in result.orphaned
    assert result.event is not None and line in result.event.orphaned
    from cobalt.aset import drc_page

    assert line in drc_page.render(imports.day_view(D))
    with DrcStore()._connect() as conn:
        assert conn.execute(
            "SELECT trade_key, supersedes FROM drc_imports WHERE id = %s", (shot,)
        ).fetchone() == (key, None)


# ---------------------------------------------------------------------
# X-NT — drafter-named (D2-3c)
# ---------------------------------------------------------------------


@requires_db
def test_xnt_a_file_less_no_trade_event_row_has_no_home_in_the_ruled_schema(migrated):
    """X-NT (D2-3c): pass condition "a file-less `no_trade` event row can be
    written by an existing path". Attempted two ways, inside the suite's
    rollback: (1) the ONE writer, `DrcStore().record_import`, with an
    `ImportResult` that carries no file kind; (2) a direct insert of a
    `drc_imports` row with no name / sha256, and with a `no_trade` kind.
    EXPECTED from reads: every one refused (the store's `ValueError`; the
    table's NOT NULL; its `kind` CHECK)."""
    with pytest.raises(ValueError) as refused:
        DrcStore().record_import(
            D, ImportResult(name="no-trade day", kind=None, outcome=Outcome.PARSED), b"", ()
        )
    assert str(refused.value) == "no-trade day: an parsed file of no kind is listed, never stored"

    _raises(
        psycopg.errors.NotNullViolation,
        "INSERT INTO drc_imports (import_date, kind, parse_status, event_state, event_updated_at) "
        "VALUES (%s, 'trading_log', 'parsed', 'pending', now())",
        (D,),
    )
    _raises(
        psycopg.errors.CheckViolation,
        "INSERT INTO drc_imports (import_date, kind, name, sha256, parse_status, event_state, "
        "event_updated_at) VALUES (%s, 'no_trade', 'no-trade day', %s, 'parsed', 'pending', now())",
        (D, "0" * 64),
    )


@requires_db
def test_xnt_the_one_writer_takes_a_file_less_row_only_by_forging_a_file_kind(migrated):
    """X-NT, the one existing path that DOES write: `record_import` with a
    file KIND and zero bytes. It is not a home — it forges a trading-log
    file the day never had (L1): the day then HAS a current trading-log
    import, which K2's `_repair` reads before any no-trade statement."""
    import_id = DrcStore().record_import(
        D, ImportResult(name="no-trade day", kind=Kind.TRADING_LOG, outcome=Outcome.PARSED), b"", ()
    )
    assert isinstance(import_id, int)
    assert DrcStore().has_current_import(D, Kind.TRADING_LOG)
