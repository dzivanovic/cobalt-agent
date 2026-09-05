"""F17 vocabulary: what a job is, and what states it can be in.

Charter §3 F17 (L18): "every scheduled job is a persisted row with
state, timeout, heartbeat; failed = loud; kill phrase stops all."

The five states are the ruled set. Two of them are DERIVED BY THE
WATCHDOG rather than written by the job itself, and that is the whole
point of the feature: a job that fails loudly is easy, a job that stops
existing is the one that goes unnoticed for a week.

* `pending`  registered, never run
* `running`  the wrapper marked it started and it has not finished
* `done`     exited 0
* `failed`   exited non-zero, or raised — LOUD (F18 turns this red)
* `zombie`   still `running` past its timeout with a stale heartbeat.
             Nothing wrote this state; the watchdog concluded it.

`missed` is deliberately NOT a state. A one-shot that never ran has no
row to move — it is a fact about the ABSENCE of a run, computed at probe
time from the schedule, and writing it as a state would mean inventing a
run to attach it to.
"""

from __future__ import annotations

from enum import Enum


class JobKind(str, Enum):
    RESIDENT = "resident"
    ONE_SHOT = "one-shot"

    def __str__(self) -> str:
        return self.value


class JobState(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    ZOMBIE = "zombie"

    def __str__(self) -> str:
        return self.value


#: States F18 paints RED. `pending` is not red on its own — a job
#: registered this morning that has not reached its schedule yet is
#: fine; the MISSED probe is what catches one that should have run.
RED_STATES: frozenset[JobState] = frozenset({JobState.FAILED, JobState.ZOMBIE})


class Supervisor(str, Enum):
    """Who stamps `heartbeat_at` — and the row says so, so nothing
    pretends a process reported in when a probe spoke for it."""

    #: Cobalt's own code, through `jobs.wrapper`. The strongest signal:
    #: the process is alive AND running our code AND past our gates.
    SELF = "self"
    #: launchd holds a live PID. The watchdog stamps from that probe.
    LAUNCHD = "launchd"
    #: The process is not launchd's own child (it was spawned detached);
    #: its PID lives in a file. See com.cobalt.agent in jobs.yaml.
    PIDFILE = "pidfile"

    def __str__(self) -> str:
        return self.value


__all__ = ["RED_STATES", "JobKind", "JobState", "Supervisor"]
