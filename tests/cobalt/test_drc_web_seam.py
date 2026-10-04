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
#: DRC K3-9: the state-your-book form and RESOLVE are appended INSIDE D2's block.
D2_ROUTES = {("get", "/drc"), ("post", "/drc/import"), ("post", "/drc/no-trade"), ("post", "/drc/scan"),
             ("post", "/drc/state-book"), ("post", "/drc/resolve")}

#: The last top-level def before D2's block. Until the 2026-09-30 seam it was
#: `radar_card_release`; S3 exits C3's trade-tap block sits directly after
#: `/release` (S-WEB) and ends with this helper, and `/drc` stays last (S-4).
LAST_EXISTING = "_sheet_closed_estimated"


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
    last_existing = _index(LAST_EXISTING)
    d2 = BODY[last_existing + 1 :]
    return d4, d2


def test_d4s_block_sits_directly_after_attest_and_holds_its_four_names():
    d4, _ = _blocks()
    assert {n.name for n in d4 if hasattr(n, "name")} == D4_NAMES
    assert {r for n in d4 for r in _routes(n)} == {("post", "/settings/daily"), ("post", "/settings/daily/apply")}


def _d2_is_last(body, last_existing: str = "radar_card_release") -> list[str]:
    """D2 fix r1 F-2 (`drc-d2-check-2026-09-25.md:143`, `:179`): over the
    WHOLE module body — every route-decorated function of `D2_ROUTES` sits
    after EVERY route-decorated function that is not D2's, and the route
    functions after `radar_card_release` are exactly D2's. The offenders,
    listed; `[]` when the block is last."""
    routed = [(i, n) for i, n in enumerate(body) if _routes(n)]
    d2 = [(i, n.name) for i, n in routed if _routes(n) & D2_ROUTES]
    others = [(i, n.name) for i, n in routed if not (_routes(n) & D2_ROUTES)]
    offenders = [
        f"{name}: a D2 route before {other}"
        for i, name in d2
        for j, other in others
        if i < j
    ]
    anchor = [i for i, n in enumerate(body) if getattr(n, "name", None) == last_existing]
    if not anchor:
        offenders.append(f"{last_existing}: not a top-level def")
    else:
        after = {name for i, name in [*d2, *others] if i > anchor[0]}
        offenders += [f"{name}: not in D2's block after {last_existing}" for _, name in d2 if name not in after]
        offenders += [f"{name}: after {last_existing} but not D2's" for i, name in others if i > anchor[0]]
    return offenders


def test_d2s_block_sits_at_the_end_after_every_existing_route():
    _, d2 = _blocks()
    assert d2, "D2's /drc block is not at the end of web.py"
    assert {r for n in d2 for r in _routes(n)} == D2_ROUTES
    assert _d2_is_last(BODY, LAST_EXISTING) == []


def test_the_last_block_check_flags_a_drc_route_placed_before_an_existing_one():
    """F-2's NEGATIVE CONTROL: a constructed module source with one `/drc`
    route placed BEFORE a non-D2 route → `_d2_is_last` names it."""
    src = (
        "@app.get('/drc')\ndef drc_page(): ...\n"
        "@app.post('/cards/release')\ndef radar_card_release(): ...\n"
        "@app.post('/drc/import')\ndef drc_import(): ...\n"
    )
    offenders = _d2_is_last(ast.parse(src).body)
    assert offenders and all(o.startswith("drc_page: ") for o in offenders), offenders
    assert "drc_page: a D2 route before radar_card_release" in offenders


def test_the_two_blocks_reference_nothing_defined_in_the_other():
    d4, d2 = _blocks()
    d4_names, d2_names = _defined(d4), _defined(d2)
    assert not (_referenced(d2) & d4_names), _referenced(d2) & d4_names
    assert not (_referenced(d4) & d2_names), _referenced(d4) & d2_names


def test_d2s_block_edits_no_existing_helper():
    """Only NEW names are defined in D2's block — no existing name is
    re-bound (a redefinition would edit a helper the rest of the file uses)."""
    _, d2 = _blocks()
    before = _defined(BODY[: _index(LAST_EXISTING) + 1])
    assert not (_defined(d2) & before), _defined(d2) & before


def test_the_one_reference_into_d4s_block_from_outside_is_daymode_banners():
    d4, d2 = _blocks()
    outside = [n for n in BODY if n not in d4 and n not in d2]
    callers = [n.name for n in outside if hasattr(n, "name") and "_settings_daily_form" in _referenced([n])]
    assert callers == ["_daymode_banner"]
