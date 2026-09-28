"""DRC D2 fix r1 — OFFLINE half (`prompts/2026-09-28/08-drc-d2-fix-r1-build.md`
`## F2`): the seam rows of `docs/30 - Design/DRC-D2-SEAM-2026-09-25.md`
(S-1 §1 tests 9, 10; S-2 §2 tests 5, 6) and the fix row F-1 of the
round-1 check (`drc-d2-check-2026-09-25.md:138`, `:174`).

The harness is `test_drc_imports.py`'s, BY IMPORT (`world` / `page`, the
`_Drc` double); every D2 symbol is imported INSIDE its test, so each test
is its own red on the base. Constructed values only (L32 / L45 / L69);
every vault write lands in a `tmp_path` vault.
"""

from __future__ import annotations

import sys
import types
from datetime import date
from pathlib import Path

import pytest

from cobalt.drc.models import SeedBook

from test_drc_imports import PNG, page, world  # noqa: F401 — fixtures are used by name
from test_drc_store import D, E1, STATS

HEX = "a" * 64
NOTE_PATH = "constructed/DRC-note.md"
#: A constructed flat book, so the double's pairing is computed.
FLAT = SeedBook(source="stated", positions=[], stated_book_id=1, from_book_sha256=HEX)


def _stub_build(monkeypatch, run):
    """D3's ONE entry, `cobalt.drc.build.run_drc_build`, as a stub (E11's shape)."""
    module = types.ModuleType("cobalt.drc.build")
    module.run_drc_build = run
    monkeypatch.setitem(sys.modules, "cobalt.drc.build", module)


def _ready_day(world):
    """A READY, computed day on the double: both logs placed from a flat book."""
    from cobalt.drc import imports

    world.drc.seed = FLAT
    imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    return world.drc.event_for(D)["trades"]


# ---------------------------------------------------------------------
# S-1 — the event model (§1 test 9) and the file-less page line (§1 test 10)
# ---------------------------------------------------------------------


def test_s1_9_the_event_names_exactly_one_source_and_a_stated_source_carries_no_file():
    """S-1 §1 test 9 (`DRC-D2-SEAM-2026-09-25.md:90`–`:93`, `:177`): the
    MODEL RULE — exactly one of `import_id` / `stated_book_id`; a stated
    source forces `no_trade`, no stats, no screenshots, no partial, no
    sha256s and a hex-64 `stated_book_sha256`; every breach is a
    `ValidationError` (L1). Both valid shapes are accepted."""
    from pydantic import ValidationError

    from cobalt.drc.imports import DrcInputsPlaced

    file_day = DrcInputsPlaced(date=D, event_id=1, import_id=7, kind="trades")
    assert (file_day.import_id, file_day.stated_book_id) == (7, None)
    file_less = DrcInputsPlaced(
        date=D, event_id=2, import_id=None, stated_book_id=3, stated_book_sha256=HEX, kind="no_trade",
        seed_from_day=date(2001, 1, 1), seed_from_book_sha256=HEX,
    )
    assert (file_less.import_id, file_less.stated_book_id, file_less.seed_from_day) == (None, 3, date(2001, 1, 1))

    stated = dict(import_id=None, stated_book_id=3, stated_book_sha256=HEX, kind="no_trade")
    breaches = {
        "no source": dict(import_id=None, kind="no_trade"),
        "two sources": dict(stated, import_id=7),
        "stated + trades": dict(stated, kind="trades"),
        "stated + stats": dict(stated, stats_import_id=8),
        "stated + screenshot": dict(stated, screenshot_import_ids=[9]),
        "stated + partial": dict(stated, partial={"8": ["Commission"]}),
        "stated + sha256s": dict(stated, sha256s={"8": HEX}),
        "stated, no book hash": dict(stated, stated_book_sha256=None),
        "stated, a bad book hash": dict(stated, stated_book_sha256="not-a-hash"),
    }
    for name, fields in breaches.items():
        with pytest.raises(ValidationError):
            DrcInputsPlaced(date=D, event_id=1, **fields)
            pytest.fail(f"accepted: {name}")


def test_s1_10_a_done_file_less_day_shows_its_stored_note_path_and_no_trade_waits_is_gone(world, monkeypatch):
    """S-1 §1 test 10 (`DRC-D2-SEAM-2026-09-25.md:110`, `:178`; `08` HOLD 2,
    `drc-d2-check-2026-09-25.md:137`): a `done` file-less day's `GET /drc`
    line is `no-trade day recorded → DRC built: <note_path>` (the path the
    event row stores), through `day_view` + `drc_page.render`; the
    `NO_TRADE_WAITS` constant is gone from `cobalt.drc.imports` and from
    every file under `src`."""
    from cobalt.aset import drc_page
    from cobalt.drc import imports

    _stub_build(monkeypatch, lambda event: NOTE_PATH)
    world.drc.days[date(2001, 1, 1)] = object()  # a recorded chain before D
    result = imports.no_trade(D)
    assert result.status_line == f"no-trade day recorded → DRC built: {NOTE_PATH}"
    view = imports.day_view(D)
    line = f"no-trade day recorded → DRC built: {NOTE_PATH}"
    assert view.state == "no-trade" and view.status_line == line
    assert f'<div class="status">{line}</div>' in drc_page.render(view)
    assert not hasattr(imports, "NO_TRADE_WAITS")
    src = Path(imports.__file__).resolve().parents[1]
    assert [p for p in src.rglob("*.py") if "NO_TRADE_WAITS" in p.read_text()] == []


# ---------------------------------------------------------------------
# S-2 — the screenshot writer (§2 tests 5, 6)
# ---------------------------------------------------------------------


def test_s2_5_kind_names_only_the_two_logs_and_detect_set_is_unchanged():
    """S-2 §2 test 5 (`DRC-D2-SEAM-2026-09-25.md:217`, `:245`): the guard —
    `set(Kind)` is the two logs, and `detect_set` over a drop of the two
    logs (a PNG beside them listed `ignored`) passes as built. GREEN on
    the base by design: it pins what S-2 must not touch."""
    from cobalt.drc.detect import detect_set
    from cobalt.drc.models import Kind

    assert set(Kind) == {Kind.TRADING_LOG, Kind.STATS_LOG}
    logs = [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())]
    verdict = detect_set(logs)
    assert (verdict.status, verdict.reason) == ("pass", "one file per kind")
    assert set(verdict.by_kind) == {Kind.TRADING_LOG, Kind.STATS_LOG}
    with_image = detect_set([*logs, ("shot.png", PNG)])
    assert (with_image.status, with_image.reason) == ("pass", "one file per kind")
    assert [d.name for d in with_image.ignored] == ["shot.png"]


def test_s2_6_the_page_counts_a_written_screenshot_row(world):
    """S-2 §2 test 6 (`DRC-D2-SEAM-2026-09-25.md:246`): `screenshots bound /
    trades` counts the row the drop zone wrote."""
    from cobalt.drc import imports

    trades = _ready_day(world)
    assert trades
    before = imports.day_view(D).counts["screenshots bound / trades"]
    assert before == f"0 / {len(trades)}"
    imports.place(D, [("shot.png", PNG)], trade_key=trades[0])
    counts = imports.day_view(D).counts
    assert counts["screenshots bound / trades"] == f"1 / {len(trades)}"
    assert counts["trades without a screenshot"] == len(trades) - 1


# ---------------------------------------------------------------------
# F-1 — an uncaught exception after `pending` fails the event
# ---------------------------------------------------------------------


@pytest.mark.parametrize(
    "step, exc",
    [
        ("seed", RuntimeError("constructed seed failure")),
        ("inputs", OSError("constructed read failure")),
        ("record", TypeError("constructed pairing failure")),
    ],
    ids=["seed", "inputs", "record"],
)
def test_an_uncaught_exception_after_pending_fails_the_event(world, monkeypatch, step, exc):
    """F-1 (`08` HOLD 3, `drc-d2-check-2026-09-25.md:138`, `:174`; L18, v2
    `[F-08]`; `07` D2-3 "any exception → `failed` with the reason; never
    `done` on an exception"): an exception other than `_LoadError` /
    `PairingError` / `ValueError` at the `seed`, `inputs` or `record` step
    → `place()` RETURNS; the event is `failed` with `<step> — <Type>:
    <message>`; nothing moves it to `running`. RED on the base: the
    exception escapes and the event stays `pending` (`imports.py:431`,
    `:440`, `:449`)."""
    from cobalt.drc import imports

    def _raise(*args, **kwargs):
        raise exc

    if step == "seed":
        monkeypatch.setattr(world.drc, "seed_for", _raise)
    elif step == "inputs":
        monkeypatch.setattr(imports, "_load", _raise)
    else:
        monkeypatch.setattr(imports, "build_day", _raise)
    result = imports.place(D, [("t.md", E1.read_bytes()), ("s.md", STATS.read_bytes())])
    reason = f"{step} — {type(exc).__name__}: {exc}"
    (event,) = world.drc.events
    assert (event["state"], event["error"]) == ("failed", reason)
    assert result.status_line == f"DRC build FAILED: {reason}"
    assert "mark_event:running" not in world.drc.writes
    assert world.drc.writes[-1] == "mark_event:failed"
