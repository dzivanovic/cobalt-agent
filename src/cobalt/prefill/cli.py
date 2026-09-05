"""CLI entrypoint: `uv run prefill daily` / `uv run prefill drc`.

Same secret-leak mitigation as aset/__main__.py and archiver/runner.py:
prefill.market/calendar import aset.prefill, which transitively imports
FinvizApiClient — cap loguru at INFO before that import chain runs.
"""

import os

os.environ.setdefault("LOGURU_LEVEL", "INFO")

import argparse  # noqa: E402
import asyncio  # noqa: E402
import sys  # noqa: E402
from datetime import date  # noqa: E402

from loguru import logger  # noqa: E402

from cobalt.jobs.entrypoint import JobStopped, as_job  # noqa: E402

from .daily import run_daily_prefill  # noqa: E402
from .drc import run_drc_prefill  # noqa: E402

DAILY_JOB = "com.cobalt.prefill-daily"
DRC_JOB = "com.cobalt.prefill-drc"


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


def _run_drc(target_date: str | None, dry_run: bool) -> None:
    for_date_ = date.fromisoformat(target_date) if target_date else None
    with as_job(DRC_JOB, skip=dry_run) as job:
        result = asyncio.run(run_drc_prefill(for_date_=for_date_, dry_run=dry_run))
        job.result = {"action": result.action, "path": str(result.path)}
    report = result.report()
    logger.info(report)
    print(report)


def main() -> None:
    parser = argparse.ArgumentParser(prog="prefill", description="Cobalt DRC & Daily prefill engine")
    sub = parser.add_subparsers(dest="command", required=True)

    # --dry-run on EVERY entrypoint (L28): compute the whole edit, print
    # the unified diff, write nothing — not to the note, not to Postgres.
    daily_parser = sub.add_parser("daily", help="Prefill today's Daily Note.")
    daily_parser.add_argument(
        "--dry-run", action="store_true", help="Show the unified diff; write nothing."
    )

    drc_parser = sub.add_parser("drc", help="Prefill the evening DRC draft.")
    drc_parser.add_argument("--date", help="Target date YYYY-MM-DD (default: today).")
    drc_parser.add_argument(
        "--dry-run", action="store_true", help="Show the unified diff; write nothing."
    )

    args = parser.parse_args()

    try:
        if args.command == "daily":
            _run_daily(args.dry_run)
        else:
            _run_drc(args.date, args.dry_run)
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
