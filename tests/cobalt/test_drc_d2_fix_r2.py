"""DRC D2 fix r2 — OFFLINE half (`prompts/2026-09-28/57-drc-d2-fix-r2-build.md`
`## F2`): the fix rows of the round-2 check (`drc-d2-fix-r1-check-2026-09-25.md`)
that run without a database — F-10 (a build that returns no note path is
`failed`, never `done`) and F-8's negative control (the `NO_TRADE_WAITS`
search rooted at `src`). D3 (`prompts/2026-09-28/10-drc-d3-build.md` rows
0a–0c, D2's round-3 HOLDs carried by 09-29 R1 (1)) adds the empty-path
cases and RUN-5's control.

The harness BY IMPORT: `test_drc_imports.py`'s `world` and its `_Drc`
double, `test_drc_d2_fix_r1.py`'s `_stub_build` / `_ready_day` /
`_holders`; every D2 symbol imported INSIDE its test. Constructed values
only (L32 / L45 / L69); every vault write lands in a `tmp_path` vault.
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from test_drc_d2_fix_r1 import _holders, _ready_day, _stub_build
from test_drc_imports import world  # noqa: F401 — fixtures are used by name
from test_drc_store import D

NEEDLE = b"NO_TRADE_WAITS"


# ---------------------------------------------------------------------
# F-10 — a build that returns no note path is `failed`, never `done`
# ---------------------------------------------------------------------


@pytest.mark.parametrize("day_type", ["file", "file_less"])
def test_a_build_that_returns_none_fails_the_event(world, monkeypatch, day_type):
    """F-10 (`drc-d2-fix-r1-check-2026-09-25.md` row 6 / `## FOR THE
    CLASSIFIER` item 6; the `done` ⇔ `note_path` contract — seam §1
    "`done` needs `note_path`", `0019_drc_events.sql:37`, v2 `[F-08]`; L1):
    D3's build returns `None` → the event lands `failed` with the step
    `build` and `NO_NOTE_PATH`, its `note_path` unset, never `done` — on a
    READY file day (`place`) and on a file-less no-trade day (`no_trade`).
    RED on `b86271f9`: the event is `done` with the note path `'None'`."""
    from cobalt.drc import imports

    _stub_build(monkeypatch, lambda event: None)
    if day_type == "file":
        _ready_day(world)
    else:
        world.drc.days[date(2001, 1, 1)] = object()  # a recorded chain before D
        result = imports.no_trade(D)
    (event,) = world.drc.events
    # getattr: on the base the constant is absent — the red must be the
    # event's state, not an ImportError.
    reason = getattr(imports, "NO_NOTE_PATH", "").format(note=None)
    assert (event["state"], event["error"], event["note_path"]) == ("failed", reason, None)
    assert "mark_event:done" not in world.drc.writes
    assert imports.day_view(D).status_line == f"DRC build FAILED: event — {reason}"
    if day_type == "file_less":
        assert (result.status_line, result.note_path) == (f"DRC build FAILED: build — {reason}", None)


# ---------------------------------------------------------------------
# D3 row 0a / 0b — every note path whose text is empty is `failed`
# (`drc-d2-fix-r2-check-2026-09-28.md` `## FOR DEJAN` 1 and 2; 09-29 R1 (1))
# ---------------------------------------------------------------------


@pytest.mark.parametrize("returned", [Path(""), "   ", ""], ids=["Path('')", "whitespace", "empty"])
@pytest.mark.parametrize("day_type", ["file", "file_less"])
def test_a_build_returning_an_empty_note_path_fails_the_event(world, monkeypatch, day_type, returned):
    """Rows 0a / 0b (`58` `## FOR DEJAN` 1: "a build returning `Path("")`
    stores `"."` and lands `done` … A whitespace-only string also lands
    `done`"; 2: "F-10's empty-string branch … is exercised by no test"). The
    seam's RETURN CONTRACT — a NON-EMPTY note path — read as: every value
    whose `str()` is empty, whitespace-only or `"."` (what `Path("")`
    renders) is `failed` with `build — ` + `NO_NOTE_PATH`, its `note_path`
    unset, never `done`. RED on `6ebfe634` for `Path("")` / `"   "`: the
    event is `('done', None, '.')` / `('done', None, '   ')`; `""` is 0b's
    PIN (green on the base)."""
    from cobalt.drc import imports

    _stub_build(monkeypatch, lambda event: returned)
    if day_type == "file":
        _ready_day(world)
    else:
        world.drc.days[date(2001, 1, 1)] = object()  # a recorded chain before D
        result = imports.no_trade(D)
    (event,) = world.drc.events
    reason = imports.NO_NOTE_PATH.format(note=returned)
    assert (event["state"], event["error"], event["note_path"]) == ("failed", reason, None)
    assert "mark_event:done" not in world.drc.writes
    if day_type == "file_less":
        assert (result.status_line, result.note_path) == (f"DRC build FAILED: build — {reason}", None)


# ---------------------------------------------------------------------
# D3 row 0c — the NEGATIVE CONTROL of RUN-5's strengthened assertion
# (`58` `## FOR DEJAN` 3)
# ---------------------------------------------------------------------


def test_the_old_page_check_passes_where_the_binding_line_helpers_fail():
    """Row 0c's control: `shot.png` appears on a constructed page (1) in a
    line WITHOUT its trade key, (2) in the exact line of a binding that is
    NOT current. The OLD check (`"shot.png" in page`) passes on both; the
    NEW helpers fail — `_binding_listed` on (1), `_binding_not_listed` on
    (2)."""
    from test_drc_d2_fix_r1_runs import KEY, _binding_line, _binding_listed, _binding_not_listed

    keyless = ["screenshot shot.png — not checked, pairing not computed"]
    page = f'<div class="line loud">{keyless[0]}</div>'
    assert "shot.png" in page  # the old assertion
    with pytest.raises(AssertionError):
        _binding_listed(keyless, page, "shot.png", KEY)

    stale = [_binding_line("shot.png", KEY), _binding_line("shot2.png", KEY)]
    page = "".join(f'<div class="line loud">{line}</div>' for line in stale)
    assert "shot.png" in page  # the old assertion
    with pytest.raises(AssertionError):
        _binding_not_listed(stale, page, "shot.png", KEY)


# ---------------------------------------------------------------------
# F-8 — the negative control of the `NO_TRADE_WAITS` search
# ---------------------------------------------------------------------


def test_the_needle_outside_the_package_is_found_only_from_the_src_root(tmp_path):
    """F-8's NEGATIVE CONTROL (`drc-d2-fix-r1-check-2026-09-25.md` row 4 /
    item 4; seam §1 test 10 "`grep -rn -F "NO_TRADE_WAITS" src` is
    EMPTY"): a constructed `src` tree with the needle in a NON-Python file
    OUTSIDE the package — `_holders` from the `src` root names it; from
    the old root's shape (`src/cobalt`) it does not."""
    src = tmp_path / "src"
    (src / "cobalt" / "drc").mkdir(parents=True)
    (src / "cobalt" / "drc" / "clean.py").write_text("X = 1\n")
    holder = src / "other_pkg" / "x.txt"
    holder.parent.mkdir()
    holder.write_bytes(b"constructed " + NEEDLE + b" line\n")
    assert _holders(src, NEEDLE) == [holder]
    assert _holders(src / "cobalt", NEEDLE) == []
