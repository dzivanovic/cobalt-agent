"""The float-handicap H1 build's first-gate experiments (v3 `## First-gate
experiments (L70)`; `prompts/2026-09-24/43-handicap-h1-build-r2.md` STEP-1).

They read the retained screener cache and the trader's notes READ-ONLY and
print COUNTS and RATIOS only — no ticker next to a threshold, no value of
his, no cap, no `first_from` time (L32). A block a module needs is
CONSTRUCTED there from literals of the builder's choosing, never his.

No `tests/experiments/__init__.py` is created (main has none; the unmerged
`bars/chunk-e-0920` adds one and `cards/stale-score-0922` adds its own
`tests/experiments/stale_score/` — L68 seams). Like `setups_one/`, this
folder reuses the new-core fixtures of `tests/cobalt/conftest.py` (the
rollback transaction, the `dev` pin, the frozen clock) by loading that
module and re-exporting them, so there is ONE copy of the mechanism.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_COBALT_TESTS = _HERE.parents[1] / "cobalt"
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_COBALT_TESTS))

_spec = importlib.util.spec_from_file_location("cobalt_tests_conftest_h1", _COBALT_TESTS / "conftest.py")
_conftest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_conftest)

mock_postgres_memory = _conftest.mock_postgres_memory
dev_env = _conftest.dev_env
dev_db_tx = _conftest.dev_db_tx
frozen_session_clock = _conftest.frozen_session_clock
