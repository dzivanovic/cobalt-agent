"""DRC D2 fix r1 — THE RUNS (L70: each UNPROVEN row of the round-1 check
becomes a cheap run whose output the build report quotes;
`prompts/2026-09-28/08-drc-d2-fix-r1-build.md` `## F5`). A RUN that is red
on the fix is a RESULT, kept under a strict `xfail` for round 3 — never
fixed in this round (L70 / L75).

Each run states what it observed as a `UserWarning` (the suite's warnings
summary is the quotable output) and asserts its PASS condition.

The harness BY IMPORT (`test_drc_imports_db.py`'s `lane` / `_drop` /
`_fingerprint` / `_page`, `test_drc_k1_store.py`'s `_state` / `TEN_ET`,
`test_drc_imports.py`'s `world`); constructed 2001 dates and symbols only
(L32 / L45); every vault write in a `tmp_path` vault; every with-DB row
inside `test_drc_store.py`'s never-committed migration transaction (L76).
"""

from __future__ import annotations

import re
import sys
import types
import warnings
from datetime import date

import pytest

from cobalt.drc.models import PairingError
from cobalt.drc.store import DrcStore

from test_drc_imports import PNG, world  # noqa: F401 — fixtures are used by name
from test_drc_imports_db import _drop, _fingerprint, _page, lane  # noqa: F401
from test_drc_k1_store import TEN_ET, _state
from test_drc_k2_experiments import _log
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    E1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)

#: RUN-3's constructed target: a name no other test writes.
RUN3_NAME = "run3-constructed-target.md"
#: A trading log with the fixture's header and ONE malformed row (side `X`).
FAILED_LOG = _log("09:45:00,EEE,X,40.0,15,ROUTE2,BRK2,ACCT1,Margin,H0000000000405,")


def _status(page: str) -> str:
    return re.search(r'<div class="status">(.*?)</div>', page, re.S).group(1)


def _stub_build(monkeypatch, run):
    module = types.ModuleType("cobalt.drc.build")
    module.run_drc_build = run
    monkeypatch.setitem(sys.modules, "cobalt.drc.build", module)


# ---------------------------------------------------------------------
# RUN-1 — `08` HOLD 10 (`drc-d2-check-2026-09-25.md:145`, `:181`)
# ---------------------------------------------------------------------


@requires_db
@pytest.mark.xfail(strict=True, reason="RUN-1 red on 8e8762ca — a round-3 finding, not fixed in fix r1 (L70/L75)")
def test_run1_a_superseding_log_that_parses_failed_never_carries_the_superseded_close(lane, migrated):
    """RUN-1 (`08` HOLD 10, `:145`, `:181`: "a superseding trading log that
    parses FAILED makes the state `waiting for: trading log` and fires no
    event … the day's `drc_rows` … still come from the superseded file").
    A stated day, a good drop, then a superseding log that parses FAILED;
    (i) `GET /drc?date=D` — its status line and file line; (ii)
    `seed_for(D_NEXT)` — raises, or returns a book. PASS (L1, v3 `[F-03]`
    the current file): nothing downstream reads rows the CURRENT file no
    longer supports — a raise, or a page line naming the stale rows."""
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    failed = _drop(D, FAILED_LOG)
    page = _page(lane, D)
    status = _status(page)
    file_line = next(f.text() for f in failed.files)
    try:
        book = DrcStore().seed_for(D_NEXT)
        outcome = (
            f"RETURNS a {book.source} book from {book.from_day}: {len(book.positions)} open "
            f"({', '.join(p.trade_id for p in book.positions)})"
        )
    except PairingError as e:
        book, outcome = None, f"RAISES: {e}"
    warnings.warn(
        f"RUN-1: GET /drc?date=2001-01-02 status line = {status!r}; the file line = {file_line!r}; "
        f"seed_for(2001-01-03) {outcome}",
        UserWarning,
    )
    assert book is None or "stale" in status, outcome


# ---------------------------------------------------------------------
# RUN-2 — `08` file-check row 11 (`:146`)
# ---------------------------------------------------------------------


@requires_db
@pytest.mark.xfail(strict=True, reason="RUN-2 red on 8e8762ca — a round-3 finding, not fixed in fix r1 (L70/L75)")
def test_run2_a_get_during_a_running_build_does_not_show_the_live_run_failed(lane, migrated, monkeypatch):
    """RUN-2 (`08` row 11, `:146`: "a GET during a running build shows
    FAILED 'left running'"). E11's stub build reads `imports.day_view(D)`
    while the event is `running` (the GET's read, in the same request)
    and records its status line. PASS (L1 both ways: a live run is not
    reported dead): the recorded line is not `DRC build FAILED`."""
    from cobalt.drc import imports

    seen: list[str] = []

    def _build(event):
        seen.append(imports.day_view(D).status_line)
        return "constructed/DRC-note.md"

    _stub_build(monkeypatch, _build)
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    (line,) = seen
    warnings.warn(f"RUN-2: day_view(2001-01-02) while the event is running = {line!r}", UserWarning)
    assert not line.startswith("DRC build FAILED"), line


# ---------------------------------------------------------------------
# RUN-3 — `08` `:151`, OPUS: "whether the with-DB tests' `VaultWriteStore`
# rows commit outside the rollback". The two tests run IN THIS ORDER
# (pytest runs a file's tests in definition order).
# ---------------------------------------------------------------------


@requires_db
def test_run3_a_a_drop_writes_its_vault_write_row(lane, migrated):
    """RUN-3 (a): a `_drop`-shaped upload in the `tmp_path` vault → its
    `vault_writes` row naming the constructed target, read back in the
    same test (inside the migration transaction)."""
    from cobalt.drc import imports

    imports.place(D, [(RUN3_NAME, DAY1.read_bytes())], now=TEN_ET)
    rows = migrated.execute(
        'SELECT note, writer FROM "user".vault_writes WHERE note LIKE %s', (f"%{RUN3_NAME}",)
    ).fetchall()
    warnings.warn(f"RUN-3 (a): vault_writes rows naming {RUN3_NAME} inside the test = {len(rows)} "
                  f"({[w for _, w in rows]})", UserWarning)
    assert len(rows) == 1 and rows[0][1] == "drc.import"


@requires_db
def test_run3_b_nothing_of_the_previous_test_survives(migrated):
    """RUN-3 (b): after (a), `vault_writes` holds NO row naming its
    constructed target — the row was rolled back with (a)'s transaction
    (an invariant, never a stored value, L69)."""
    n = migrated.execute(
        'SELECT count(*) FROM "user".vault_writes WHERE note LIKE %s', (f"%{RUN3_NAME}",)
    ).fetchone()[0]
    warnings.warn(f"RUN-3 (b): vault_writes rows naming {RUN3_NAME} after (a) = {n}", UserWarning)
    assert n == 0


# ---------------------------------------------------------------------
# RUN-4 — `08` `:151`, OPUS: "whether `AsetStore().for_date` writes"
# ---------------------------------------------------------------------


@requires_db
def test_run4_the_real_cards_read_inside_get_drc_writes_nothing(lane, migrated, monkeypatch):
    """RUN-4 (`08` `:151`). F-3's fingerprint around `GET /drc`, with the
    REAL `AsetStore` restored (the `lane` fixture replaces it with a
    double, so F-3's own GET never runs `AsetStore().for_date` — the
    prompt's premise; ESCALATE). PASS: the whole-schema fingerprint (every
    table's `pg_stat_xact_user_tables` counter + the `drc_*` md5s) is equal
    before and after."""
    from cobalt.aset import store as aset_store
    from cobalt.aset import web as web_module

    monkeypatch.setattr(web_module, "AsetStore", aset_store.AsetStore)
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    before = _fingerprint(migrated)
    page = _page(lane, D)
    after = _fingerprint(migrated)
    moved = sorted(k for k in before.keys() | after.keys() if before.get(k) != after.get(k))
    counters = sorted(k.removeprefix("writes:") for k in after if k.startswith("writes:"))
    warnings.warn(
        f"RUN-4: GET /drc?date=2001-01-02 with the real AsetStore — cards line "
        f"{'FAILED: cards unreadable' in page and 'unreadable' or 'read'}; moved = {moved}; "
        f"counters read ({len(counters)}): {counters}",
        UserWarning,
    )
    assert moved == []


# ---------------------------------------------------------------------
# RUN-5 — `08` `:151`, GROK: "whether a not-computed day has trade rows so
# `_orphans`' `_computed` guard hides an orphan" (offline)
# ---------------------------------------------------------------------


def test_run5_a_not_computed_days_unbound_screenshot_is_listed_somewhere(world):
    """RUN-5 (`08` `:151`). On the `_Drc` double: a day whose `day` row
    carries `not_computed.pairing` (no book stated) and ONE current
    screenshot row whose key is not a trade → what `_orphans` returns and
    whether the page lists the binding anywhere. PASS (X13, D2-3: "listed
    `orphaned`, never re-bound, never deleted"): listed somewhere."""
    from cobalt.aset import drc_page
    from cobalt.drc import imports

    imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    view = world.drc.event_for(D)
    assert "pairing" in view["day"]["derived"]["not_computed"]
    world.drc.record_screenshot(D, "shot.png", PNG, "ZZZ-long-constructed")
    view = world.drc.event_for(D)
    orphans = imports._orphans(view)
    page = drc_page.render(imports.day_view(D))
    listed = "shot.png" in page
    warnings.warn(
        f"RUN-5: trades on the not-computed day = {len(view['trades'])}; _orphans(view) = {orphans!r}; "
        f"shot.png on the page = {listed}",
        UserWarning,
    )
    assert listed
