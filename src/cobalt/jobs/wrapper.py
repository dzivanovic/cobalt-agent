"""F17b: the wrapper every scheduled job runs inside.

Charter §3 F17: "marks running/done/failed with exit code and stamps
heartbeat_at at least every timeout_s/3 for long jobs."

TWO WAYS IN, one implementation:

    # a Python entry point (prefill, archiver, cards-expire, …)
    with job_run("com.cobalt.archiver") as run:
        summary = do_the_work()
        run.result = {"rows_written": summary.rows_written}

    # anything else, from a plist
    uv run cobalt jobs run com.cobalt.prefill-daily -- uv run prefill daily

WHAT IT GUARANTEES, in order:

1. THE KILL SWITCH IS CHECKED FIRST. A stopped Cobalt does not start a
   one-shot at all — except the heartbeat, whose validated registry flag
   keeps the watcher running so it can report the stop itself.
2. `running` is marked before the work, with `started_at`.
3. A BEATER THREAD stamps `heartbeat_at` every `timeout_s /
   jobs.heartbeat_fraction` (5 min for the 15-min archiver window). This
   is the ONLY thing that distinguishes a long job from a hung one — the
   archiver legitimately runs 23 minutes, so "started and did not
   finish" cannot be the zombie test.
4. `done` (exit 0) or `failed` (exit code + the exception, redacted
   through F19 on the way into the column) — and `failed` is LOUD.
5. The exception is RE-RAISED. The wrapper reports; it never swallows.

The beater thread is a daemon: if the job process dies hard, the thread
dies with it, `heartbeat_at` stops advancing, and the watchdog draws the
right conclusion. A thread that outlived its job would keep a dead job
looking alive, which is the exact failure this feature exists to catch.
"""

from __future__ import annotations

import threading
import traceback
from contextlib import contextmanager
from typing import Any, Optional

from loguru import logger

from . import killswitch
from .config import JobSpec, load_job_registry
from .store import JobStore

#: The tunables row governing how often a long job stamps (F16).
HEARTBEAT_FRACTION_KEY = "jobs.heartbeat_fraction"

#: Exit code a job uses when the kill switch turned it away. ZERO, on
#: purpose — see guarantee 1.
STOPPED_EXIT_CODE = 0


class JobStopped(RuntimeError):
    """The kill switch is engaged; this run did not happen."""


def heartbeat_fraction() -> int:
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(HEARTBEAT_FRACTION_KEY)
    if row is None:
        raise RuntimeError(
            f"tunable {HEARTBEAT_FRACTION_KEY!r} is missing from tunables.yaml — the "
            "wrapper reads its stamp interval from config and has no built-in "
            "default (F16)."
        )
    return int(row.value)


class _Beater:
    """Stamps `heartbeat_at` on a timer until the run ends."""

    def __init__(self, store: JobStore, label: str, every_s: float):
        self.store = store
        self.label = label
        self.every_s = max(1.0, every_s)
        self._stop = threading.Event()
        self._thread = threading.Thread(
            target=self._loop, name=f"beat:{label}", daemon=True
        )

    def _loop(self) -> None:
        while not self._stop.wait(self.every_s):
            try:
                self.store.beat(self.label)
            except Exception as e:  # noqa: BLE001
                # A missed stamp is not a reason to kill the job. It IS a
                # reason to say so: the watchdog may conclude ZOMBIE from
                # this, and an operator needs the other half of the story.
                logger.error(
                    "F17: heartbeat stamp FAILED for {} ({}: {}) — the job is still "
                    "running; the watchdog may see a stale heartbeat.",
                    self.label, type(e).__name__, e,
                )

    def __enter__(self) -> "_Beater":
        self._thread.start()
        return self

    def __exit__(self, *exc) -> None:
        self._stop.set()


class JobRun:
    """Handle a wrapped job can hang its result on."""

    def __init__(self, spec: JobSpec):
        self.spec = spec
        self.label = spec.label
        #: Whatever the run wants F18 to be able to report — the
        #: archiver's `rows_written` is what makes "archiver freshness
        #: (last run + rows written)" answerable.
        self.result: Optional[dict[str, Any]] = None


@contextmanager
def job_run(
    label: str,
    *,
    store: Optional[JobStore] = None,
    register: bool = True,
    allow_prod: bool = False,
):
    """Run a block as a registered job. See the module docstring."""
    registry = load_job_registry()
    spec = registry.spec(label)
    store = store or JobStore()

    def bookkeeping(stage: str, operation) -> bool:
        try:
            operation()
            return True
        except Exception as e:  # noqa: BLE001 - heartbeat must still launch
            if not spec.kill_switch_exempt:
                raise
            logger.error(
                "F17: {} {} FAILED ({}: {}) — heartbeat subprocess WILL STILL RUN; "
                "its database probe and out-of-band alert own this outage.",
                label, stage, type(e).__name__, e,
            )
            return False

    bookkeeping(
        "schema setup", lambda: store.ensure_schema(allow_prod=allow_prod)
    )
    if register:
        bookkeeping(
            "registration", lambda: store.register(spec, allow_prod=allow_prod)
        )

    if killswitch.is_active(store):
        state = killswitch.read(store)
        if not spec.kill_switch_exempt:
            logger.error("F17: {} REFUSED TO START — {}", label, state.describe())
            raise JobStopped(state.describe())
        logger.error(
            "F17: {} is kill-switch EXEMPT and WILL RUN — {}",
            label,
            state.describe(),
        )

    bookkeeping("mark_running", lambda: store.mark_running(label))
    run = JobRun(spec)
    every_s = spec.timeout_s / heartbeat_fraction()
    logger.info(
        "F17: {} RUNNING (timeout {}s, heartbeat every {:.0f}s)",
        label, spec.timeout_s, every_s,
    )
    try:
        with _Beater(store, label, every_s):
            yield run
    except BaseException as e:
        error = f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}"
        finish = store.mark_wrapper_finished if spec.kill_switch_exempt else store.mark_finished
        bookkeeping(
            "mark_finished",
            lambda: finish(
                label,
                exit_code=1,
                error=error,
                result=run.result,
            ),
        )
        logger.error("F17: {} FAILED — {}: {}", label, type(e).__name__, e)
        raise            # the wrapper reports; it never swallows
    finish = store.mark_wrapper_finished if spec.kill_switch_exempt else store.mark_finished
    bookkeeping(
        "mark_finished",
        lambda: finish(label, exit_code=0, result=run.result),
    )
    logger.info("F17: {} DONE", label)


def should_keep_running(label: str, *, store: Optional[JobStore] = None) -> bool:
    """A RESIDENT's own loop check. `False` means exit cleanly now.

    Residents call this where they can stop without tearing out of a
    write. Cobalt's residents today are supervised by launchd rather than
    wrapped (see jobs.yaml), so this exists for the first new-core
    resident — the S2 radar poller — and for anything the chief of staff
    grows into.
    """
    if killswitch.is_active(store):
        logger.error(
            "F17: kill switch engaged — {} is exiting cleanly at its next safe point.",
            label,
        )
        return False
    return True


__all__ = [
    "HEARTBEAT_FRACTION_KEY",
    "STOPPED_EXIT_CODE",
    "JobRun",
    "JobStopped",
    "heartbeat_fraction",
    "job_run",
    "should_keep_running",
]
