"""DRC D2 fix r2 — WITH-DB half (`prompts/2026-09-28/57-drc-d2-fix-r2-build.md`
`## F3`): F-10's file-less row on `drc_events`, and the NEGATIVE CONTROLS
of F-5 (the rollback's CHECKs compared whole) and F-6 (the event's
hashes asserted) — each control shows the input the OLD assertion let
through.

The harness BY IMPORT, never copied: `test_drc_d2_fix_r1_db.py`'s helpers,
`test_drc_store.py`'s `migrated` / `requires_db` / `D` / `D_NEXT`,
`test_drc_imports_db.py`'s `lane`, `test_drc_k1_store.py`'s `TEN_ET`.
Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76): `0016` / `0018` / `0019` are applied only
there. Constructed 2001 dates and symbols only (L32 / L45); every vault
write lands in the lane's `tmp_path` vault.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cobalt.db_migrations.cli import _apply

from test_drc_d2_fix_r1_db import (
    NOTE_PATH,
    ROLLBACK,
    SQL,
    _check_rows,
    _checks,
    _event_source_assertions,
    _events,
    _hashes_of,
    _no_trade_ids,
    _recorded_prior,
    _stored_hash_assertions,
    _stub_build,
    _to_0018,
)
from test_drc_imports_db import lane  # noqa: F401 — fixtures are used by name
from test_drc_k1_store import TEN_ET
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D_NEXT,
    migrated,
    requires_db,
    weekday_calendar,
)


# ---------------------------------------------------------------------
# F-10 — with-DB: a file-less build returning None is `failed` on the row
# ---------------------------------------------------------------------


@requires_db
def test_a_file_less_build_returning_none_is_failed_on_the_event_row(lane, migrated, monkeypatch):
    """F-10 (`drc-d2-fix-r1-check-2026-09-25.md` row 6 / `## FOR THE
    CLASSIFIER` item 6; seam §1 "`done` needs `note_path`",
    `0019_drc_events.sql:37`; L1): the `test_s1_1` shape with D3's stub
    returning `None` → the `drc_events` row is `failed` with
    `NO_NOTE_PATH`, `note_path` NULL, never `done`. RED on `b86271f9`: the
    row is `('stated_book', None, <id>, 'done', None, 'None')`."""
    from cobalt.drc import imports

    _recorded_prior()
    _stub_build(monkeypatch, lambda event: None)
    result = imports.no_trade(D_NEXT, now=TEN_ET)
    (statement,) = _no_trade_ids(migrated, D_NEXT)
    # getattr: on the base the constant is absent — the red must be the row.
    reason = getattr(imports, "NO_NOTE_PATH", "").format(note=None)
    assert _events(migrated, D_NEXT) == [("stated_book", None, statement, "failed", reason, None)]
    assert result.status_line == f"DRC build FAILED: build — {reason}"


# ---------------------------------------------------------------------
# F-5 — the NEGATIVE CONTROL of the rollback's CHECK comparison
# ---------------------------------------------------------------------


@requires_db
def test_a_constructed_short_value_list_passes_the_old_line_and_fails_the_whole_list(migrated):
    """F-5's NEGATIVE CONTROL (`drc-d2-fix-r1-check-2026-09-25.md` row 1 /
    item 1; the rollback's contract "both CHECKs come back exactly as
    `0016_drc.sql:35`–`:37`, `:42` declare them"): after `0019`'s rollback
    the value-list CHECK is dropped and re-added with the constructed list
    `('pending', 'failed')` — the OLD membership line still passes, the
    whole-list comparison against the `0018` tree fails."""
    _to_0018(migrated)
    before = sorted(d for _, d in _check_rows(migrated, "drc_imports"))
    _apply(migrated, [SQL, ROLLBACK])
    (name,) = [n for n, d in _check_rows(migrated, "drc_imports") if "'pending'::text" in d]
    migrated.execute(f'ALTER TABLE "user".drc_imports DROP CONSTRAINT {name}')
    migrated.execute("""ALTER TABLE "user".drc_imports ADD CHECK (event_state IN ('pending', 'failed'))""")
    checks = _checks(migrated, "drc_imports")
    assert any("event_state" in c and "'pending'::text" in c and "'failed'::text" in c for c in checks)
    assert sorted(d for _, d in _check_rows(migrated, "drc_imports")) != before


# ---------------------------------------------------------------------
# F-6 — the NEGATIVE CONTROL of the event's hashes
# ---------------------------------------------------------------------


@requires_db
def test_forged_event_hashes_fail_the_stored_hash_comparison(lane, migrated, monkeypatch):
    """F-6's NEGATIVE CONTROL (`drc-d2-fix-r1-check-2026-09-25.md` row 2 /
    item 2; seam §1 / L57 "the event object carries … its `book_sha256`
    and the seed row's `from_day` / `from_book_sha256`"): the file-less
    day's event matches the stored hashes; the same comparison on a copy
    with constructed hashes fails on EACH field. D3 row 0d: the control
    calls BOTH helpers of the `returns` branch on each one-field forgery —
    the old one passes it, the new one fails it."""
    from cobalt.drc import imports

    _recorded_prior()
    _stub_build(monkeypatch, lambda event: NOTE_PATH)
    result = imports.no_trade(D_NEXT, now=TEN_ET)
    (statement,) = _no_trade_ids(migrated, D_NEXT)
    book_sha256, seed_sha256 = _hashes_of(migrated, statement, D_NEXT)
    assert seed_sha256 is not None
    assert (result.event.stated_book_sha256, result.event.seed_from_book_sha256) == (book_sha256, seed_sha256)
    # D3 row 0d (`58` `## FOR DEJAN` 4: "It never shows the forged copy
    # passing the old assertions"): ONE field forged at a time — the OLD
    # helper PASSES the copy, the NEW stored-hash helper FAILS it.
    _event_source_assertions(result.event, statement)
    _stored_hash_assertions(result.event, migrated, statement)
    for field, value in (("stated_book_sha256", "c" * 64), ("seed_from_book_sha256", "b" * 64)):
        forged = result.event.model_copy(update={field: value})
        _event_source_assertions(forged, statement)
        with pytest.raises(AssertionError):
            _stored_hash_assertions(forged, migrated, statement)


# ---------------------------------------------------------------------
# D3 rows 0a / 0b — with-DB: an empty note path is `failed` on the row
# ---------------------------------------------------------------------


@requires_db
@pytest.mark.parametrize("returned", [Path(""), ""], ids=["Path('')", "empty"])
def test_a_file_less_build_returning_an_empty_path_is_failed_on_the_event_row(lane, migrated, monkeypatch, returned):
    """Rows 0a / 0b (`58` `## FOR DEJAN` 1 and 2), the file-less shape of
    F-10's test: the build stub returns `Path("")` (0a — RED on `6ebfe634`:
    the row `done` with `note_path` `'.'`) or `""` (0b — a PIN) → the
    `drc_events` row is `failed` with `NO_NOTE_PATH`, `note_path` NULL."""
    from cobalt.drc import imports

    _recorded_prior()
    _stub_build(monkeypatch, lambda event: returned)
    result = imports.no_trade(D_NEXT, now=TEN_ET)
    (statement,) = _no_trade_ids(migrated, D_NEXT)
    reason = imports.NO_NOTE_PATH.format(note=returned)
    assert _events(migrated, D_NEXT) == [("stated_book", None, statement, "failed", reason, None)]
    assert result.status_line == f"DRC build FAILED: build — {reason}"
