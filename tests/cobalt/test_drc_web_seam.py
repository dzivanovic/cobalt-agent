"""THE `aset/web.py` SEAM between D4 and D2 (L72; the seam of record,
`drc-d4-fix-r1-build-2026-09-25.md:200`–`:211` + the restored bullet of
`drc-d4-fix-r2-build-2026-09-25.md:159`).

"`src/cobalt/aset/web.py` holds TWO new route blocks and they share
nothing. D4's settings change-line block (`POST /settings/daily`,
`POST /settings/daily/apply`, and any helper they alone use) sits
DIRECTLY AFTER the `/attest` route … D2's `/drc` block (`GET /drc`,
`POST /drc/import`, `POST /drc/no-trade`, `POST /drc/scan`, and any
helper they alone use) sits at the END of the file, after every existing
route. Neither block calls, imports or edits a helper of the other."

Read from the source with `ast` — top-level statements, by position.
`_daymode_banner`'s call of `_settings_daily_form()` sits OUTSIDE both
blocks (the one reference into D4's block from outside it) and is not a
cross-block reference.
"""

from __future__ import annotations

import ast
from pathlib import Path

from cobalt.aset import web

SOURCE = Path(web.__file__).read_text()
TREE = ast.parse(SOURCE)
BODY = TREE.body

D4_NAMES = {"_settings_daily_form", "_settings_daily_review", "settings_daily", "settings_daily_apply"}
D2_ROUTES = {("get", "/drc"), ("post", "/drc/import"), ("post", "/drc/no-trade"), ("post", "/drc/scan")}


def _index(name: str) -> int:
    for i, node in enumerate(BODY):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == name:
            return i
    raise AssertionError(f"{name} is not a top-level def of web.py")


def _routes(node) -> set[tuple[str, str]]:
    out = set()
    for dec in getattr(node, "decorator_list", []):
        if (
            isinstance(dec, ast.Call)
            and isinstance(dec.func, ast.Attribute)
            and isinstance(dec.func.value, ast.Name)
            and dec.func.value.id == "app"
            and dec.args
            and isinstance(dec.args[0], ast.Constant)
        ):
            out.add((dec.func.attr, dec.args[0].value))
    return out


def _defined(nodes) -> set[str]:
    names: set[str] = set()
    for node in nodes:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            for t in targets:
                for n in ast.walk(t):
                    if isinstance(n, ast.Name):
                        names.add(n.id)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            names.update((a.asname or a.name).split(".")[0] for a in node.names)
    return names


def _referenced(nodes) -> set[str]:
    return {
        n.id if isinstance(n, ast.Name) else n.attr
        for node in nodes
        for n in ast.walk(node)
        if isinstance(n, (ast.Name, ast.Attribute))
    }


def _blocks():
    attest = _index("attest")
    d4_end = _index("card_move")  # the next existing route after D4's block
    d4 = BODY[attest + 1 : d4_end]
    last_existing = _index("radar_card_release")
    d2 = BODY[last_existing + 1 :]
    return d4, d2


def test_d4s_block_sits_directly_after_attest_and_holds_its_four_names():
    d4, _ = _blocks()
    assert {n.name for n in d4 if hasattr(n, "name")} == D4_NAMES
    assert {r for n in d4 for r in _routes(n)} == {("post", "/settings/daily"), ("post", "/settings/daily/apply")}


def test_d2s_block_sits_at_the_end_after_every_existing_route():
    _, d2 = _blocks()
    assert d2, "D2's /drc block is not at the end of web.py"
    assert {r for n in d2 for r in _routes(n)} == D2_ROUTES
    assert _index("radar_card_release") < min(BODY.index(n) for n in d2)


def test_the_two_blocks_reference_nothing_defined_in_the_other():
    d4, d2 = _blocks()
    d4_names, d2_names = _defined(d4), _defined(d2)
    assert not (_referenced(d2) & d4_names), _referenced(d2) & d4_names
    assert not (_referenced(d4) & d2_names), _referenced(d4) & d2_names


def test_d2s_block_edits_no_existing_helper():
    """Only NEW names are defined in D2's block — no existing name is
    re-bound (a redefinition would edit a helper the rest of the file uses)."""
    _, d2 = _blocks()
    before = _defined(BODY[: _index("radar_card_release") + 1])
    assert not (_defined(d2) & before), _defined(d2) & before


def test_the_one_reference_into_d4s_block_from_outside_is_daymode_banners():
    d4, d2 = _blocks()
    outside = [n for n in BODY if n not in d4 and n not in d2]
    callers = [n.name for n in outside if hasattr(n, "name") and "_settings_daily_form" in _referenced([n])]
    assert callers == ["_daymode_banner"]
