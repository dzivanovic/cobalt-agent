"""DRC D3 fix round 1 — the WITH-DB rows (`prompts/2026-09-29/08-drc-d3-fix-r1-build.md`
`## THE FIX ROWS`, L75): F-2 red first on `a8c622ca`; F-7 / F-8's negative
controls (the old assertions pass where the new helpers FAIL, L35).

The harness is reused BY IMPORT, never copied: `test_drc_build_db.py`'s
`built` and its helpers, `test_drc_imports_db.py`'s `lane` / `_drop`,
`test_drc_store.py`'s `migrated` / `weekday_calendar` / `requires_db` /
`D` / `D_NEXT`, `test_drc_k1_store.py`'s `_state` / `TEN_ET`. Everything
runs inside `test_drc_store.py`'s never-committed migration transaction on
`cobalt_dev` (L76). Constructed 2001 dates and symbols only (L32 / L45).

THE STAMP (F-2). Every miss-line row is written by the one writer
(`replay.line.write_miss_line` through `VaultWriter` / `VaultWriteStore`).
`vault_writes.ts` is the table's `DEFAULT now()` — the transaction's start,
not the writer's clock — so the constructed stamp is set on that writer's
own row by its `write_id`, inside the rolled-back transaction.
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from cobalt.drc.store import DrcStore

from test_drc_build_db import CARD, _build_rows, _event, _note, _note_rebuilt, _snapshot_holds, _summary_text, built  # noqa: F401
from test_drc_imports_db import _drop, lane  # noqa: F401 — fixtures are used by name
from test_drc_k1_store import TEN_ET, _state
from test_drc_k2_experiments import EEE_ROUND
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    E1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)

ET = ZoneInfo("America/New_York")
#: A constructed note that is NOT the day's DRC note (F-2 (b)).
OTHER_DAY = date(2001, 1, 5)


def _k10_2(day: date):
    """K10.2 as committed, through `checks.default_deps(prod=False)`'s read
    path inside the migration transaction, its day bound to `day`."""
    from cobalt.smoke import checks
    from cobalt.smoke.config import SUITES_DIR, load_suite

    from test_smoke import ctx

    check = {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}["K10.2"]
    return checks.evaluate(check, ctx(prod=False, last_trading_day=day), checks.default_deps(prod=False))


def _writer():
    from cobalt.replay.line import WRITER
    from cobalt.vaultwrite import VaultWriter
    from cobalt.vaultwrite.store import VaultWriteStore

    return VaultWriter(WRITER, store=VaultWriteStore(), now=lambda: TEN_ET)


def _miss_line(conn, note: Path, at: datetime) -> int:
    """The miss line written to `note` by the one writer, its row stamped `at`."""
    from cobalt.replay.line import write_miss_line

    result = write_miss_line(note, "misses: constructed", writer=_writer())
    assert result.write_id is not None
    conn.execute('UPDATE "user".vault_writes SET ts = %s WHERE id = %s', (at, result.write_id))
    return result.write_id


# ---------------------------------------------------------------------
# F-2 — K10.2 counts the day's DRC note, not the write's clock date
# ---------------------------------------------------------------------


@requires_db
def test_f2_a_miss_line_written_the_next_morning_passes_k10_2(built, migrated):
    """F-2 (a) (`drc-d3-check-2026-09-25.md:103`; `09-28/10` D3-6 "PASS when
    `done` and both present"): D's event `done` with its note, the miss
    line written to that note the NEXT morning (stamped `D_NEXT` 10:00 ET)
    → K10.2 PASS for D."""
    from cobalt.smoke.models import Verdict

    _state(D)
    _drop(D, E1.read_bytes(), STATS.read_bytes())
    state, _, note_path = _event(migrated, D)
    assert state == "done" and note_path
    _miss_line(migrated, Path(note_path), datetime(D_NEXT.year, D_NEXT.month, D_NEXT.day, 10, 0, tzinfo=ET))
    out = _k10_2(D)
    assert out.verdict is Verdict.PASS, out.detail


@requires_db
def test_f2_another_notes_miss_line_never_passes_k10_2(built, migrated):
    """F-2 (b): D's event `done`, D's note with NO miss line, a miss line
    written to ANOTHER constructed note and stamped on D → K10.2 FAIL for D
    (another note's write never counts)."""
    from cobalt.smoke.models import Verdict

    root, _, _ = built
    _state(D)
    _drop(D, E1.read_bytes(), STATS.read_bytes())
    state, _, note_path = _event(migrated, D)
    assert state == "done" and note_path
    other = _note(root, OTHER_DAY)
    _writer().create_if_absent(other, Path(note_path).read_text())
    _miss_line(migrated, other, datetime(D.year, D.month, D.day, 10, 0, tzinfo=ET))
    assert "<!-- cobalt:section drc-misses -->" not in Path(note_path).read_text()
    out = _k10_2(D)
    assert out.verdict is Verdict.FAIL, out.detail
    assert "writes ge 1 (actual 0)" in out.detail, out.detail


# ---------------------------------------------------------------------
# F-7 / F-8 — the negative controls (L35: a test that cannot fail is not proof)
# ---------------------------------------------------------------------


@requires_db
def test_f7_the_snapshot_helper_fails_after_a_rebuild_with_the_changed_card(built, migrated):
    """F-7 (`drc-d3-check-2026-09-25.md:110`): the same card change, then a
    RE-BUILD of D through the build's own function with the same deps → the
    rows and the note carry the new stop, so `_snapshot_holds(…, build-time
    stop)` FAILS; the old re-read of the Python dict alone could not."""
    root, cards, real_build = built
    cards.append(dict(CARD))
    _state(D)
    _drop(D, E1.read_bytes(), STATS.read_bytes())
    before = _build_rows(migrated, D)
    _snapshot_holds(migrated, root, before, Decimal("49.9"))
    cards[0]["stop"] = Decimal("48.0")
    real_build.run_drc_build(real_build.event_of(D, DrcStore()), deps=real_build.default_deps())
    with pytest.raises(AssertionError):
        _snapshot_holds(migrated, root, before, Decimal("49.9"))
    _snapshot_holds(migrated, root, _build_rows(migrated, D), Decimal("48.0"))


@requires_db
def test_f8_the_rebuilt_note_helper_fails_on_an_unrewritten_note(built, migrated):
    """F-8 (`drc-d3-check-2026-09-25.md:111`): the helper run on the
    before-text as if it were the after-text (the later day's note never
    re-written) FAILS, while `is_file()` on the same note passes."""
    root, _, _ = built
    _state(D_NEXT)
    _drop(D_NEXT, EEE_ROUND, STATS.read_bytes())
    before_text = _summary_text(root, D_NEXT)
    (day_row,) = [r for r in _build_rows(migrated, D_NEXT) if r[1] == "build_day"]
    assert _note(root, D_NEXT).is_file()
    with pytest.raises(AssertionError):
        _note_rebuilt(root, D_NEXT, before_text, day_row)
