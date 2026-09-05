"""The decorator half of F17b — one line at each scheduled entry point.

    from cobalt.jobs.entrypoint import as_job

    with as_job("com.cobalt.prefill-daily", skip=args.dry_run) as run:
        ...

WHY A SEPARATE HELPER and not `job_run` directly. Three things every
entry point needs and none of them belongs in the wrapper:

* `skip=` — a DRY RUN IS NOT A RUN. `prefill daily --dry-run` writes
  nothing and must not satisfy the MISSED probe, or "I checked what it
  would do" would silence the alarm that says it never did it.
* F19's LOG GUARD, installed once, here. Every scheduled job writes to
  `logs/*.log`, those files are read over Tailscale and pasted into
  reports, and a secret reaches a log the same way it reaches a DM.
  Installing it at the entry point means a new job gets it by using this.
* the STOPPED case exits 0 with a printed line rather than a traceback.

An ad-hoc `uv run prefill daily` goes through this too, and that is
correct: a manual catch-up run IS a run of that job, it belongs in the
row, and it should stop the MISSED probe firing an hour later.
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Optional

from loguru import logger

from .wrapper import JobRun, JobStopped, job_run


@contextmanager
def as_job(label: str, *, skip: bool = False, store=None):
    """Wrap a scheduled entry point. Yields a `JobRun`, or a bare one
    when `skip` is set."""
    from cobalt.redact import install_log_guard

    install_log_guard()

    if skip:
        logger.info(
            "F17: {} is a DRY RUN — no jobs row is touched. A dry run is not a run, "
            "and must not satisfy the MISSED probe.",
            label,
        )
        from .config import load_job_registry

        yield JobRun(load_job_registry().spec(label))
        return

    with job_run(label, store=store) as run:
        yield run


__all__ = ["JobStopped", "as_job"]
