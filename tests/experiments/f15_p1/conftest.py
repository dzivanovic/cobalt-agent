"""F15 P1's first-gate RUN rows (card 61, `## ROWS` X5, X9, X12, X13).

Outside the suites, run by explicit path with `-rP`. Each prints what it
measured and asserts nothing about the design (L70). This folder reuses
the new-core fixtures of `tests/cobalt/conftest.py` (the rollback
transaction, the `dev` pin, the frozen clock) exactly as
`tests/experiments/stale_score/conftest.py` does, so there is ONE copy of
the transaction mechanism.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_COBALT_TESTS = Path(__file__).resolve().parents[2] / "cobalt"
sys.path.insert(0, str(_COBALT_TESTS))

_spec = importlib.util.spec_from_file_location("cobalt_tests_conftest_f15_p1", _COBALT_TESTS / "conftest.py")
_conftest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_conftest)

mock_postgres_memory = _conftest.mock_postgres_memory
dev_env = _conftest.dev_env
dev_db_tx = _conftest.dev_db_tx
frozen_session_clock = _conftest.frozen_session_clock
