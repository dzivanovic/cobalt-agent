"""The stale-score build's first-gate experiments (v2 §7, X1–X30).

Offline modules (STEP-1, STEP-5) drive the pure evaluator on the committed
real-shape fixtures; `cobalt_dev` modules (STEP-3) write their own rows
INSIDE the suite's rollback transaction. Each prints COUNTS, booleans and
engine outputs only — no value of the trader's (L32), nothing about his
trades (R24).

No `tests/experiments/__init__.py` is created (the base has none — the
setups one build's folder uses the same shape). This folder reuses the
new-core fixtures of `tests/cobalt/conftest.py` (the rollback
transaction, the `dev` pin, the frozen clock) by loading that module and
re-exporting them, so there is ONE copy of the transaction mechanism.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_COBALT_TESTS = Path(__file__).resolve().parents[2] / "cobalt"
sys.path.insert(0, str(_COBALT_TESTS))

_spec = importlib.util.spec_from_file_location("cobalt_tests_conftest_stale_score", _COBALT_TESTS / "conftest.py")
_conftest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_conftest)

mock_postgres_memory = _conftest.mock_postgres_memory
dev_env = _conftest.dev_env
dev_db_tx = _conftest.dev_db_tx
frozen_session_clock = _conftest.frozen_session_clock
