"""The HITL vocabulary (F20 FINAL §2 `hitl/models.py`)."""

from __future__ import annotations

#: The first action catalog: nothing else (FINAL §1, §8).
ACTIONS = ("agents.create", "agents.deactivate")

#: The row's status, as the table's CHECK constraint spells it.
STATUSES = ("pending", "approved", "denied", "expired", "executed", "failed")

#: Terminal outcomes the CoS reports once each (DM + one session line).
REPORTED = ("executed", "failed", "denied", "expired")

__all__ = ["ACTIONS", "REPORTED", "STATUSES"]
