"""lock-relief G1 + P1 — "skipped offline" means "needs the database".

G1, THE GUARD (`tests/cobalt/conftest.py`): a test that reaches `cobalt_dev`
— a call of `fake_connect` inside `dev_db_tx`, or of `_open` inside
`real_connect` — and carries no `skipif` mark (its own, its class's or its
module's `pytestmark`) fails with `with-DB test without an offline skip mark:
<nodeid>`. The autouse open of `dev_db_tx` itself is not a reach. Every OTHER
door is closed statically here: a test module that names `REAL_CONNECT`, calls
`psycopg.connect`, or defines or requests a fixture named `migrated` (or
`migrated_<x>`) carries a `skipif` mark at module level or on each such test
(`conftest.py` and the helper modules are read as the modules that import
them).

P1, THE SELECTION: `--db-only` keeps an item only when it carries at least
one `skipif` mark and deselects every other item. It stands on G1: a test the
selection drops either never reaches the database or is refused by the guard.

The helpers live in `tests/cobalt/conftest.py`, which pytest loads as a
plugin and no test imports by name; `_conftest()` fetches that module from the
plugin manager. Constructed items come from `pytester` (an inner collection
in its own temp directory). No value of the trader's is read (L32).
"""

from __future__ import annotations

import ast
import os
from pathlib import Path

import pytest

pytest_plugins = ["pytester"]

TESTS = Path(__file__).resolve().parent
CONFTEST = TESTS / "conftest.py"
GUARD_MESSAGE = "with-DB test without an offline skip mark: "

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _conftest(config):
    """`tests/cobalt/conftest.py` as pytest loaded it."""
    for plugin in config.pluginmanager.get_plugins():
        path = getattr(plugin, "__file__", None)
        if path and Path(path).resolve() == CONFTEST:
            return plugin
    raise LookupError(f"{CONFTEST} is not a loaded plugin")


# ---------------------------------------------------------------------
# Constructed items: marked three ways, and unmarked
# ---------------------------------------------------------------------

FUNCTION_AND_CLASS = """
import pytest

@pytest.mark.skipif(True, reason="constructed")
def test_marked_on_the_function():
    pass

@pytest.mark.skipif(True, reason="constructed")
class TestMarkedOnTheClass:
    def test_inside(self):
        pass

class TestMarkedInTheClassBody:
    pytestmark = pytest.mark.skipif(True, reason="constructed")

    def test_inside(self):
        pass

def test_unmarked():
    pass

@pytest.mark.skip(reason="constructed: a skip, not a skipif")
def test_skip_is_not_skipif():
    pass

@pytest.mark.usefixtures("tmp_path")
def test_another_mark_only():
    pass
"""

MODULE_MARK = """
import pytest

pytestmark = [pytest.mark.skipif(True, reason="constructed")]

def test_marked_on_the_module():
    pass
"""

KEPT = {
    "test_marked_on_the_function",
    "TestMarkedOnTheClass::test_inside",
    "TestMarkedInTheClassBody::test_inside",
    "test_marked_on_the_module",
}
DROPPED = {"test_unmarked", "test_skip_is_not_skipif", "test_another_mark_only"}


def _short(item) -> str:
    return item.nodeid.split("::", 1)[1]


@pytest.fixture
def constructed_items(pytester):
    return pytester.getitems(FUNCTION_AND_CLASS) + pytester.getmodulecol(MODULE_MARK).collect()


def test_the_mark_finder_sees_a_skipif_on_the_function_the_class_and_the_module(request, constructed_items):
    marks = _conftest(request.config).offline_skip_marks
    found = {_short(item) for item in constructed_items if marks(item)}
    assert found == KEPT
    for item in constructed_items:
        assert all(mark.name == "skipif" for mark in marks(item))


def test_the_mark_finder_sees_nothing_on_an_unmarked_test(request, constructed_items):
    marks = _conftest(request.config).offline_skip_marks
    unmarked = {_short(item) for item in constructed_items if not marks(item)}
    assert unmarked == DROPPED


def test_db_only_keeps_marked_three_ways_and_drops_unmarked(request, constructed_items):
    """P1's keep rule: at least one `skipif` mark (own, class or module)."""
    kept, dropped = _conftest(request.config).db_only_split(list(constructed_items))
    assert {_short(item) for item in kept} == KEPT
    assert {_short(item) for item in dropped} == DROPPED
    assert len(kept) + len(dropped) == len(constructed_items)


def test_the_db_only_option_is_registered_and_off_by_default(request):
    """P1: `--db-only` is an option of this run; without it nothing changes."""
    assert request.config.getoption("--db-only") is False


def test_the_guard_refuses_an_unmarked_item_and_passes_a_marked_one(request, constructed_items):
    require = _conftest(request.config).require_offline_skip
    by_name = {_short(item): item for item in constructed_items}
    require(by_name["test_marked_on_the_module"])
    with pytest.raises(AssertionError) as refused:
        require(by_name["test_unmarked"])
    assert str(refused.value) == GUARD_MESSAGE + by_name["test_unmarked"].nodeid


# ---------------------------------------------------------------------
# The static doors
# ---------------------------------------------------------------------

DOOR_NAME = "REAL_CONNECT"
#: `dev_db_tx`'s autouse open is not a reach (card G1); its `fake_connect`
#: is the runtime guard's.
NOT_A_DOOR = {"dev_db_tx"}


def _is_migrated(name: str) -> bool:
    return name == "migrated" or name.startswith("migrated_")


def _is_skipif_call(node) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "skipif"
        and isinstance(node.func.value, ast.Attribute)
        and node.func.value.attr == "mark"
    )


def _is_psycopg_connect(node) -> bool:
    return (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "connect"
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "psycopg"
    )


def _is_fixture(fn) -> bool:
    for deco in fn.decorator_list:
        target = deco.func if isinstance(deco, ast.Call) else deco
        if isinstance(target, ast.Attribute) and target.attr == "fixture":
            return True
        if isinstance(target, ast.Name) and target.id == "fixture":
            return True
    return False


def _usefixtures(exprs) -> set[str]:
    names: set[str] = set()
    for expr in exprs:
        for node in ast.walk(expr):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "usefixtures"
            ):
                names |= {a.value for a in node.args if isinstance(a, ast.Constant) and isinstance(a.value, str)}
    return names


def _pytestmark(body) -> list:
    return [
        stmt.value
        for stmt in body
        if isinstance(stmt, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "pytestmark" for t in stmt.targets)
    ]


class _Reader:
    """Every module under `tests/cobalt/`, read once; a module is judged
    with the doors of the helper modules it imports and of `conftest.py`."""

    def __init__(self, sources: dict[str, str]):
        self.trees = {name: ast.parse(text) for name, text in sources.items()}
        self._imports: dict[str, tuple[dict, dict, list]] = {}
        self._skipif: dict[str, set[str]] = {}
        self._users: dict[str, set[str]] = {}

    # -- imports: local name -> (module, attr); alias -> module; star modules
    def imports(self, mod: str):
        if mod not in self._imports:
            names, aliases, stars = {}, {}, []
            for stmt in self.trees[mod].body:
                if isinstance(stmt, ast.ImportFrom) and stmt.module in self.trees and not stmt.level:
                    for alias in stmt.names:
                        if alias.name == "*":
                            stars.append(stmt.module)
                        else:
                            names[alias.asname or alias.name] = (stmt.module, alias.name)
                elif isinstance(stmt, ast.Import):
                    for alias in stmt.names:
                        if alias.name in self.trees:
                            aliases[alias.asname or alias.name] = alias.name
            self._imports[mod] = (names, aliases, stars)
        return self._imports[mod]

    def skipif_names(self, mod: str) -> set[str]:
        if mod not in self._skipif:
            self._skipif[mod] = set()
            own = {
                t.id
                for stmt in self.trees[mod].body
                if isinstance(stmt, ast.Assign) and _is_skipif_call(stmt.value)
                for t in stmt.targets
                if isinstance(t, ast.Name)
            }
            names, _aliases, stars = self.imports(mod)
            got = own | {local for local, (src, attr) in names.items() if attr in self.skipif_names(src)}
            for src in stars:
                got |= self.skipif_names(src)
            self._skipif[mod] = got
        return self._skipif[mod]

    def is_skipif(self, mod: str, expr) -> bool:
        if isinstance(expr, (ast.List, ast.Tuple)):
            return any(self.is_skipif(mod, e) for e in expr.elts)
        if _is_skipif_call(expr):
            return True
        if isinstance(expr, ast.Name):
            return expr.id in self.skipif_names(mod)
        if isinstance(expr, ast.Attribute) and isinstance(expr.value, ast.Name):
            src = self.imports(mod)[1].get(expr.value.id)
            return src is not None and expr.attr in self.skipif_names(src)
        return False

    # -- the defs of a module, each with its class context
    def defs(self, mod: str):
        for stmt in self.trees[mod].body:
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                yield stmt, None
            elif isinstance(stmt, ast.ClassDef):
                for inner in stmt.body:
                    if isinstance(inner, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        yield inner, stmt

    def door_names(self, mod: str) -> tuple[set[str], set[str]]:
        """(names whose load reaches a door, fixture names whose request does)."""
        names, _aliases, stars = self.imports(mod)
        loads = {DOOR_NAME} | {local for local, (src, attr) in names.items() if attr in self.users(src)}
        for src in stars:
            loads |= self.users(src)
        fixtures = set(loads)
        if "conftest" in self.trees and mod != "conftest":
            fixtures |= self.users("conftest")
        return loads, fixtures

    def reaches(self, mod: str, fn, cls, loads: set[str], fixtures: set[str]) -> bool:
        if _is_fixture(fn) and _is_migrated(fn.name):
            return True
        requested = {a.arg for a in fn.args.args + fn.args.kwonlyargs}
        requested |= _usefixtures(fn.decorator_list)
        requested |= _usefixtures(_pytestmark(self.trees[mod].body))
        if cls is not None:
            requested |= _usefixtures(cls.decorator_list) | _usefixtures(_pytestmark(cls.body))
        if any(_is_migrated(n) or n in fixtures for n in requested):
            return True
        aliases = self.imports(mod)[1]
        for node in ast.walk(fn):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load) and node.id in loads:
                return True
            if (
                isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id in aliases
                and (node.attr == DOOR_NAME or node.attr in self.users(aliases[node.value.id]))
            ):
                return True
            if _is_psycopg_connect(node):
                return True
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "getfixturevalue"
                and any(
                    isinstance(a, ast.Constant) and isinstance(a.value, str)
                    and (_is_migrated(a.value) or a.value in fixtures)
                    for a in node.args
                )
            ):
                return True
        return False

    def users(self, mod: str) -> set[str]:
        """The top-level defs of `mod` that reach a door, directly or through
        another (a helper call, a fixture request)."""
        if mod in self._users:
            return self._users[mod]
        self._users[mod] = set()
        loads, fixtures = self.door_names(mod)
        found: set[str] = set()
        while True:
            more = {
                fn.name
                for fn, cls in self.defs(mod)
                if cls is None
                and fn.name not in found
                and not (mod == "conftest" and fn.name in NOT_A_DOOR)
                and self.reaches(mod, fn, None, loads | found, fixtures | found)
            }
            if not more:
                break
            found |= more
        self._users[mod] = found
        return found

    def unmarked(self, mod: str) -> list[str]:
        """Every test of `mod` that reaches a door and carries no skipif mark."""
        if any(self.is_skipif(mod, expr) for expr in _pytestmark(self.trees[mod].body)):
            return []
        loads, fixtures = self.door_names(mod)
        local = self.users(mod)
        out = []
        for fn, cls in self.defs(mod):
            if not fn.name.startswith("test"):
                continue
            if cls is not None and not cls.name.startswith("Test"):
                continue
            if not self.reaches(mod, fn, cls, loads | local, fixtures | local):
                continue
            marks = list(fn.decorator_list)
            if cls is not None:
                marks += cls.decorator_list + _pytestmark(cls.body)
            if not any(self.is_skipif(mod, m) for m in marks):
                where = f"{cls.name}::{fn.name}" if cls is not None else fn.name
                out.append(f"{mod}.py::{where}")
        return out


def unmarked_door_users(sources: dict[str, str]) -> list[str]:
    reader = _Reader(sources)
    return [hit for mod in sorted(sources) if mod.startswith("test_") for hit in reader.unmarked(mod)]


def _tree_sources() -> dict[str, str]:
    return {path.stem: path.read_text() for path in sorted(TESTS.glob("*.py"))}


def test_every_door_to_cobalt_dev_carries_an_offline_skip_mark():
    """G1's static half: REAL_CONNECT, psycopg.connect and the `migrated`
    fixtures are reached only by tests that skip offline."""
    assert unmarked_door_users(_tree_sources()) == []


# -- the static reader on constructed modules: each door, each mark form

_SUPPORT = '''
import os
import pytest
from cobalt import db

requires_db = pytest.mark.skipif(not os.getenv("X"), reason="constructed")

@pytest.fixture
def migrated_world(monkeypatch):
    yield db.connect_migration("cobalt_dev")
'''

_CONFTEST = '''
import pytest
from cobalt import db
REAL_CONNECT = db.connect

@pytest.fixture(autouse=True)
def dev_db_tx():
    yield REAL_CONNECT("cobalt_dev")

@pytest.fixture
def real_connect():
    def _open():
        return REAL_CONNECT("cobalt_dev")
    yield _open
'''

_DOORS_UNMARKED = '''
import psycopg
import pytest
from cobalt import db
from world_support import migrated_world

REAL_CONNECT = db.connect

def _helper():
    return REAL_CONNECT("cobalt_dev")

@pytest.fixture
def opened():
    return _helper()

@pytest.fixture
def migrated(monkeypatch):
    yield None

def test_names_the_door():
    REAL_CONNECT("cobalt_dev")

def test_calls_psycopg():
    psycopg.connect("dbname=cobalt_dev")

def test_through_a_helper():
    _helper()

def test_through_a_local_fixture(opened):
    pass

def test_requests_migrated(migrated):
    pass

@pytest.mark.usefixtures("migrated_world")
def test_uses_a_support_fixture():
    pass

def test_requests_real_connect(real_connect):
    pass

def test_asks_for_migrated_by_name(request):
    request.getfixturevalue("migrated")

class TestInAClass:
    def test_names_the_door(self):
        REAL_CONNECT("cobalt_dev")

def test_offline_only():
    assert 1 + 1 == 2
'''

_DOORS_MARKED = '''
import os
import psycopg
import pytest
import world_support as ws
from cobalt import db
from world_support import migrated_world, requires_db

REAL_CONNECT = db.connect
local_db = pytest.mark.skipif(not os.getenv("X"), reason="constructed")

@local_db
def test_names_the_door():
    REAL_CONNECT("cobalt_dev")

@pytest.mark.skipif(not os.getenv("X"), reason="constructed")
def test_calls_psycopg():
    psycopg.connect("dbname=cobalt_dev")

@requires_db
@pytest.mark.usefixtures("migrated_world")
def test_uses_a_support_fixture():
    pass

@ws.requires_db
def test_requests_real_connect(real_connect):
    pass

@requires_db
class TestDecorated:
    def test_names_the_door(self):
        REAL_CONNECT("cobalt_dev")

class TestBodyMark:
    pytestmark = [pytest.mark.integration, requires_db]

    def test_names_the_door(self):
        REAL_CONNECT("cobalt_dev")
'''

_MODULE_MARKED = '''
import pytest
from world_support import requires_db

pytestmark = [requires_db, pytest.mark.integration]

def test_requests_migrated(migrated_world):
    pass
'''


def test_the_static_reader_finds_each_door_unmarked():
    found = unmarked_door_users({
        "conftest": _CONFTEST, "world_support": _SUPPORT, "test_doors": _DOORS_UNMARKED,
    })
    assert found == [
        "test_doors.py::test_names_the_door",
        "test_doors.py::test_calls_psycopg",
        "test_doors.py::test_through_a_helper",
        "test_doors.py::test_through_a_local_fixture",
        "test_doors.py::test_requests_migrated",
        "test_doors.py::test_uses_a_support_fixture",
        "test_doors.py::test_requests_real_connect",
        "test_doors.py::test_asks_for_migrated_by_name",
        "test_doors.py::TestInAClass::test_names_the_door",
    ]


def test_the_static_reader_accepts_each_mark_form():
    assert unmarked_door_users({
        "conftest": _CONFTEST, "world_support": _SUPPORT,
        "test_marked": _DOORS_MARKED, "test_module_marked": _MODULE_MARKED,
    }) == []


def test_the_autouse_open_of_dev_db_tx_is_not_a_door():
    """A test module with no door of its own is never judged by conftest's
    autouse `dev_db_tx` (which names REAL_CONNECT)."""
    assert unmarked_door_users({
        "conftest": _CONFTEST, "test_plain": "def test_plain(dev_db_tx):\n    pass\n",
    }) == []


# ---------------------------------------------------------------------
# The runtime guard, with the database
# ---------------------------------------------------------------------


@requires_db
def test_an_unmarked_reach_through_the_suite_factory_fails_with_the_guard_message(request):
    """G1 at run time: this test's own item, made to look unmarked, reaches
    `fake_connect` (the patched `db.connect`): the guard's check refuses it
    with the message, before any savepoint is taken — no second connection.
    The record the guard fails a test on at teardown is cleared here."""
    from cobalt import db, env

    require = _conftest(request.config).require_offline_skip
    db.connect(env.DEV_DB_NAME, side=db.Side.SYSTEM)  # marked: the reach passes
    record = request.getfixturevalue("offline_skip_guard")
    item = request.node
    item.iter_markers = lambda name=None: iter(())
    try:
        with pytest.raises(AssertionError) as direct:
            require(item)
        with pytest.raises(AssertionError) as through:
            db.connect(env.DEV_DB_NAME, side=db.Side.SYSTEM)
    finally:
        del item.iter_markers
    assert str(direct.value) == GUARD_MESSAGE + item.nodeid
    assert str(through.value) == GUARD_MESSAGE + item.nodeid
    assert record == [GUARD_MESSAGE + item.nodeid]
    record.clear()
