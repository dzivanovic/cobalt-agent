"""The setups one build's stored-session experiments (X1, X2, X7, X13, X15,
X16, X18 — FINAL `## First-gate experiments (L70)`).

They read `cobalt_dev`'s stored `system.bars` INSIDE the suite's rollback
transaction and print COUNTS and RATIOS only — no ticker, no date (L32) —
asserting nothing about the trader's trades (R24).

No `tests/experiments/__init__.py` is created (main has none; the unmerged
`bars/chunk-e-0920` adds one — an L68 seam). This folder reuses the
new-core fixtures of `tests/cobalt/conftest.py` (the rollback transaction,
the `dev` pin, the frozen clock) by loading that module and re-exporting
them, so there is ONE copy of the transaction mechanism.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_COBALT_TESTS = Path(__file__).resolve().parents[2] / "cobalt"
sys.path.insert(0, str(_COBALT_TESTS))

_spec = importlib.util.spec_from_file_location("cobalt_tests_conftest", _COBALT_TESTS / "conftest.py")
_conftest = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_conftest)

mock_postgres_memory = _conftest.mock_postgres_memory
dev_env = _conftest.dev_env
dev_db_tx = _conftest.dev_db_tx
frozen_session_clock = _conftest.frozen_session_clock
