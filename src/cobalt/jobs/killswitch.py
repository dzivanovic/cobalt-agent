"""F17d: the kill phrase. One flag, checked by every wrapper.

Charter §3 F17 / L18: "kill phrase stops all."

    cobalt stop     # resident jobs exit cleanly, one-shots refuse to start
    cobalt resume   # clears it

WHY THE FLAG IS IN POSTGRES and not a file. Cobalt's jobs run as
separate launchd processes with no shared memory, and the one thing they
already all reach is the database. A file would work equally well until
the day one job runs from a different working directory — and the failure
mode of a kill switch nobody's process could see is that it silently does
not stop anything.

WHAT "STOPS" MEANS, precisely, because it is not "kill -9":

* a one-shot REFUSES TO START. It marks nothing, writes nothing, exits 0
  with a loud line. Exiting non-zero would paint F18 red for a state the
  operator deliberately caused.
* a resident EXITS CLEANLY at its next heartbeat — it finishes what it is
  holding and stops, rather than being torn out of a write.

The flag does NOT reach into the database or the vault to undo anything.
It stops new work; it does not roll back work in flight.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from loguru import logger

from .config import load_job_registry
from .store import JobStore


@dataclass(frozen=True)
class KillState:
    active: bool
    phrase: Optional[str]
    set_by: Optional[str]
    set_at: Optional[object]

    def describe(self) -> str:
        if not self.active:
            return "kill switch CLEAR — jobs run normally"
        when = f" at {self.set_at:%Y-%m-%d %H:%M:%S %Z}" if self.set_at else ""
        return (
            f"KILL SWITCH ACTIVE — set by {self.set_by or 'unknown'}{when} "
            f"(phrase: {self.phrase!r}). One-shots refuse to start; residents exit "
            "cleanly at their next heartbeat. Clear it with `cobalt resume`."
        )


def read(store: Optional[JobStore] = None) -> KillState:
    store = store or JobStore()
    row = store.kill_switch()
    return KillState(
        active=bool(row.get("active")),
        phrase=row.get("phrase"),
        set_by=row.get("set_by"),
        set_at=row.get("set_at"),
    )


def is_active(store: Optional[JobStore] = None) -> bool:
    """Fail OPEN, deliberately, and loudly.

    If the database cannot be reached the answer is "not stopped". The
    alternative — a database blip silently stopping every scheduled job
    on the host — is a far worse failure than one run happening after a
    stop was requested, and it would look exactly like the kill switch
    working correctly.
    """
    try:
        return read(store).active
    except Exception as e:  # noqa: BLE001
        logger.error(
            "F17: could not read the kill switch ({}: {}) — treating it as CLEAR. "
            "A database blip must not silently stop every job on this host.",
            type(e).__name__, e,
        )
        return False


def engage(*, by: str, phrase: Optional[str] = None, store: Optional[JobStore] = None) -> KillState:
    store = store or JobStore()
    store.ensure_schema()
    registry = load_job_registry()
    store.set_kill_switch(active=True, phrase=phrase or registry.kill_phrase, by=by)
    state = read(store)
    logger.error(state.describe())      # ERROR: this is a loud, visible act
    return state


def clear(*, by: str, store: Optional[JobStore] = None) -> KillState:
    store = store or JobStore()
    store.ensure_schema()
    store.set_kill_switch(active=False, phrase=None, by=by)
    state = read(store)
    logger.warning("F17: kill switch CLEARED by {} — jobs run normally again.", by)
    return state


def matches_kill_phrase(text: str) -> bool:
    """Does an inbound message carry the kill phrase?

    Exists for the Mattermost DM listener the moment one lands in the new
    core. The phrase is CONFIG (`configs/cobalt/jobs.yaml`), compared
    case-insensitively on a stripped line — a stop that failed because of
    a trailing space would be the worst possible bug in this feature.
    """
    registry = load_job_registry()
    return text.strip().upper() == registry.kill_phrase.strip().upper()


def matches_resume_phrase(text: str) -> bool:
    registry = load_job_registry()
    return text.strip().upper() == registry.resume_phrase.strip().upper()


__all__ = [
    "KillState",
    "clear",
    "engage",
    "is_active",
    "matches_kill_phrase",
    "matches_resume_phrase",
    "read",
]
