"""F17 task integrity, minimal (Charter §3 F17, L18).

Every scheduled job is a persisted row with a state, a timeout and a
heartbeat; a failure is loud; a kill phrase stops all of them.

* `config.py`     — the registry, `configs/cobalt/jobs.yaml`, one row per
                    launchd label. `cobalt validate` cross-checks it
                    against `ops/*.plist`.
* `store.py`      — the `jobs` table and the kill switch.
* `wrapper.py`    — `with job_run(label) as run:` — marks running/done/
                    failed with the exit code and stamps `heartbeat_at`
                    at least every `timeout_s / jobs.heartbeat_fraction`.
* `watchdog.py`   — ZOMBIE (running past timeout with a stale heartbeat)
                    and MISSED (a one-shot past its cadence with no run).
                    Both red. Residents someone else supervises are
                    PROBED here, and `heartbeat_source` records that a
                    probe spoke for them.
* `killswitch.py` — `cobalt stop` / `cobalt resume`.
"""

from .config import JobConfigError, JobRegistry, JobSpec, load_job_registry
from .killswitch import KillState
from .models import RED_STATES, JobKind, JobState, Supervisor
from .store import JobStore, JobStoreError
from .watchdog import Finding, sweep
from .wrapper import JobRun, JobStopped, job_run, should_keep_running

__all__ = [
    "RED_STATES",
    "Finding",
    "JobConfigError",
    "JobKind",
    "JobRegistry",
    "JobRun",
    "JobSpec",
    "JobState",
    "JobStopped",
    "JobStore",
    "JobStoreError",
    "KillState",
    "Supervisor",
    "job_run",
    "load_job_registry",
    "should_keep_running",
    "sweep",
]
