"""CLI entrypoints: `uv run prefill daily` and (F4) `uv run prefill refresh`.

`prefill drc` is RETIRED (DRC D3, v2 §8 `[F-22]`, F39): the DRC note is
built by the input-driven build, `cobalt drc build` (K1's `drc` group) —
one creator of the note, one CLI (L3). Its job `com.cobalt.prefill-drc`
left `configs/cobalt/jobs.yaml` and `ops/` in the same deploy.

Same secret-leak mitigation as aset/__main__.py and archiver/runner.py:
prefill.market/calendar import aset.prefill, which transitively imports
FinvizApiClient — cap loguru at INFO before that import chain runs.
"""

import os

os.environ.setdefault("LOGURU_LEVEL", "INFO")

import argparse  # noqa: E402
import asyncio  # noqa: E402
import sys  # noqa: E402

from loguru import logger  # noqa: E402

from cobalt.jobs.entrypoint import JobStopped, as_job  # noqa: E402

from datetime import datetime, timezone  # noqa: E402

from .daily import run_daily_prefill, run_daily_refresh  # noqa: E402

DAILY_JOB = "com.cobalt.prefill-daily"
#: F4 (FINAL §4.1): the scheduled refresh AND the manual trigger.
REFRESH_JOB = "com.cobalt.prefill-refresh"


class RefreshNotClean(RuntimeError):
    """A refresh that degraded a field or wrote nothing it should have.
    Raised INSIDE the `as_job` block: an exception leaving it is the only
    way `job_run` records `exit_code=1` (jobs/wrapper.py:177-198, [F-28])."""


def _run_daily(dry_run: bool) -> None:
    # F17: the run is a persisted row with a state, a timeout and a
    # heartbeat. `skip=dry_run` because a dry run is not a run — see
    # cobalt/jobs/entrypoint.py.
    with as_job(DAILY_JOB, skip=dry_run) as job:
        result = asyncio.run(run_daily_prefill(dry_run=dry_run))
        job.result = {
            "action": result.action,
            "filled": result.filled_slots,
            "skipped": result.skipped_slots,
            "path": str(result.path),
        }
    # L28.4: every report and run log shows the unified diff.
    report = result.report()
    logger.info(report)
    print(report)


def _run_refresh(dry_run: bool) -> None:
    with as_job(REFRESH_JOB, skip=dry_run) as job:
        result = run_daily_refresh(datetime.now(timezone.utc), dry_run=dry_run)
        job.result = {
            "action": result.action,
            "path": str(result.path),
            "flags": result.flags,
            "degraded": result.degraded,
            "failures": result.failures,
        }
        # L28.4: every report and run log shows the unified diff — printed
        # before the nonzero exit, so a degraded run still shows its diff.
        report = result.report()
        logger.info(report)
        print(report)
        if result.exit_code != 0:
            raise RefreshNotClean(result.summary())


def main() -> None:
    parser = argparse.ArgumentParser(prog="prefill", description="Cobalt Daily prefill engine")
    sub = parser.add_subparsers(dest="command", required=True)

    # --dry-run on EVERY entrypoint (L28): compute the whole edit, print
    # the unified diff, write nothing — not to the note, not to Postgres.
    daily_parser = sub.add_parser("daily", help="Prefill today's Daily Note.")
    daily_parser.add_argument(
        "--dry-run", action="store_true", help="Show the unified diff; write nothing."
    )

    refresh_parser = sub.add_parser(
        "refresh", help="Re-render today's trading and calendar units (scheduled and manual)."
    )
    refresh_parser.add_argument(
        "--dry-run", action="store_true", help="Show the unified diff; write nothing."
    )

    args = parser.parse_args()

    try:
        if args.command == "refresh":
            _run_refresh(args.dry_run)
        else:
            _run_daily(args.dry_run)
    except JobStopped as e:
        # Exit 0 — see cobalt/cli.py's note. A deliberate stop is not a
        # failure and must not turn the heartbeat red.
        print(f"NOT RUN — {e}")
    except Exception as e:
        logger.error(f"prefill {args.command} FAILED: {type(e).__name__}: {e}")
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
