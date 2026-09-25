"""H1 fix round 1, F1 — ONE named harness for every `migrated_radar` test
(`handicap-h1-check-2026-09-24.md:323`, `## FOR THE CLASSIFIER` row 1;
`43` XL76 (A): "`test · fixture dev_db_tx → migrated_radar · assertions
unchanged`"; L76 "one owner").

OFFLINE: no test names both fixtures. `dev_db_tx` is `autouse=True`
(`tests/cobalt/conftest.py:133`), so dropping the NAME changes nothing at
run time: this test pins the NAMED intent `43` stated ("moved").
WITH-DB: the run-time half — does `dev_db_tx`'s connection hold an open
transaction on `cobalt_dev` beside `migrated_radar`'s? A RUN, never an
argument (L70). Read-only; both connections are rolled back by their
fixtures.
"""

from __future__ import annotations

import ast
from pathlib import Path

from radar_migrated_support import migrated_radar, requires_db  # noqa: F401  (fixture)

TESTS = Path(__file__).resolve().parent
BOTH = {"migrated_radar", "dev_db_tx"}
# The with-DB probe below names both ON PURPOSE (it measures the pair).
PROBE = Path(__file__).name


def _usefixtures(decorators) -> set[str]:
    names: set[str] = set()
    for decorator in decorators:
        if (
            isinstance(decorator, ast.Call)
            and isinstance(decorator.func, ast.Attribute)
            and decorator.func.attr == "usefixtures"
        ):
            names |= {arg.value for arg in decorator.args if isinstance(arg, ast.Constant)}
    return names


def stacked_tests() -> list[str]:
    """Every `tests/cobalt/test_*.py` test whose fixture names — its own
    `usefixtures` marks, its classes' marks and its parameters — hold BOTH
    `migrated_radar` and `dev_db_tx`."""
    found: list[str] = []
    for path in sorted(TESTS.glob("test_*.py")):
        if path.name == PROBE:
            continue
        tree = ast.parse(path.read_text())

        def collect(nodes, prefix: str, inherited: set[str]) -> None:
            for node in nodes:
                if isinstance(node, ast.ClassDef):
                    collect(node.body, f"{prefix}{node.name}::", inherited | _usefixtures(node.decorator_list))
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name.startswith("test_"):
                    params = {a.arg for a in node.args.args + node.args.kwonlyargs}
                    names = inherited | _usefixtures(node.decorator_list) | params
                    if BOTH <= names:
                        found.append(f"{path.name}::{prefix}{node.name}")

        collect(tree.body, "", set())
    return found


def test_no_migrated_radar_caller_also_names_dev_db_tx():
    """F1 (`45` `## FOR THE CLASSIFIER` row 1, `:323`): every membership
    test runs on ONE named harness — `migrated_radar`, which itself declares
    the autouse `dev_db_tx` (set up first, patched over, torn down last)."""
    stacked = stacked_tests()
    assert stacked == [], f"tests naming both migrated_radar and dev_db_tx: {stacked}"
