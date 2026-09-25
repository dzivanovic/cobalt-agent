"""X18 + X19 (v2 §7, before S1; re-run at STEP-2's end).

X18: every `score_card(` call in `src/` and every occurrence of the version
string the build bumps FROM. After STEP-2 every caller passes
`last=score_last(...)` and the old string is gone from `src/`.
X19: who reads `DESK_FORMULA_VERSION` — anything comparing it to
`EVALUATOR_VERSION` moves with the singleton.
"""

from __future__ import annotations

import re
from pathlib import Path

from stale_support import FIXED

SRC = Path(__file__).resolve().parents[3] / "src"
#: The evaluator / desk strings at the base (PREFLIGHT, `evaluate.py:160-161`).
OLD_EVALUATOR = "s2p2.2"
OLD_DESK = "s2p2.1"


def _hits(pattern: str):
    rx = re.compile(pattern)
    out = []
    for path in sorted(SRC.rglob("*.py")):
        for n, line in enumerate(path.read_text().splitlines(), 1):
            if rx.search(line):
                out.append((path.relative_to(SRC.parent).as_posix(), n, line.strip()))
    return out


def test_x18_every_score_card_caller_and_the_old_version_string():
    calls = [h for h in _hits(r"\bscore_card\(") if not h[2].startswith("def ")]
    on_helper = [h for h in calls if "last=score_last(" in h[2]]
    old = _hits(re.escape(OLD_EVALUATOR))
    print(f"X18: fixed={FIXED} score_card_callers={len(calls)} on_score_last={len(on_helper)}")
    for path, n, line in calls:
        print(f"X18:   caller {path}:{n}: {line}")
    for path, n, line in old:
        print(f"X18:   old-string {path}:{n}: {line}")
    assert calls
    if FIXED:
        assert len(on_helper) == len(calls), [c for c in calls if c not in on_helper]
        assert not [h for h in old if "SUPPORTED_EVALUATORS" in h[2] or "_VERSION =" in h[2]]


def test_x19_who_reads_desk_formula_version():
    readers = _hits(r"\bDESK_FORMULA_VERSION\b")
    compared = [h for h in readers if "EVALUATOR_VERSION" in h[2]]
    print(f"X19: readers={len(readers)} compared_with_evaluator_version={len(compared)}")
    for path, n, line in readers:
        print(f"X19:   {path}:{n}: {line}")
    assert readers and not compared
