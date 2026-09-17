"""Bar Archiver orchestration: the nightly full run and the on-demand
per-ticker backfill. Sequential, gentle rate, fail-loud per ticker —
one failure never aborts the run or gets silently skipped.

The database is not an argument anywhere in this module. `COBALT_ENV`
alone decides it (`cobalt.env.resolve_db_name()`, via `BarStore`) —
RULING 9 (2026-09-04). Before that this module threaded a
`db_name="cobalt_dev"` default through every entry point and exposed
it as a `--db-name` CLI flag, so the archiver kept writing PRODUCTION
bars into the dev database long after every other store had moved onto
the resolver. The flag is deleted rather than re-pointed: a per-run
override of the target database is exactly the hole RULING 7 closed
for `AsetConfig.db_name`.
"""

import asyncio
import sys

from loguru import logger

from .collector import CollectorError, fetch_bars, resolve_token
from .config import load_config
from .models import Interval
from .report import RunSummary, append_run_report
from .store import BarStore

GENTLE_SLEEP_SECONDS = 1.2


def _check_demand(targets: list[tuple[str, Interval]], mode: str) -> None:
    """L53 (S2-P4 R1-13/R2-5): the ONE shared total-demand gate, before the
    first request. The nightly run is the registry's `archiver` consumer; a
    manual backfill is unscheduled, so it counts against every window."""
    from cobalt.radar.notes import DemandConsumer, check_scheduled_demand

    if mode == "full":
        check_scheduled_demand("archiver")
        return
    backfill = DemandConsumer(
        name="backfill", rpm=min(len(targets), 60 / GENTLE_SLEEP_SECONDS), window=None,
        basis=f"{len(targets)} request(s), pacing bound, unscheduled",
    )
    check_scheduled_demand("backfill", extra=[backfill])


async def _run_targets(targets: list[tuple[str, Interval]], mode: str) -> RunSummary:
    _check_demand(targets, mode)
    summary = RunSummary(mode=mode)
    store = BarStore()
    store.ensure_schema()
    token = await resolve_token()

    total = len(targets)
    for i, (ticker, interval) in enumerate(targets, start=1):
        try:
            bars = await fetch_bars(ticker, interval, token)
            rows = store.upsert_bars(bars)
            summary.record_success(ticker, rows)
            logger.info(f"[{i}/{total}] {ticker}/{interval.value}: {rows} rows")
        except CollectorError as e:
            summary.record_failure(ticker, interval.value, str(e))
            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {e}")
        except Exception as e:
            # Any other unexpected error is still a per-ticker failure,
            # never a reason to abort the whole run or store partial data.
            summary.record_failure(ticker, interval.value, f"{type(e).__name__}: {e}")
            logger.error(f"[{i}/{total}] {ticker}/{interval.value}: FAILED — {type(e).__name__}: {e}")

        if i < total:
            await asyncio.sleep(GENTLE_SLEEP_SECONDS)

    return summary


async def run_full() -> RunSummary:
    """Nightly job: archive every enabled Lists-note archive target.

    Writes to whichever database `COBALT_ENV` names (RULING 9)."""
    cfg = load_config()
    targets = cfg.archive_targets()
    logger.info(f"Bar Archiver full run: {len(targets)} (ticker, interval) targets")
    summary = await _run_targets(targets, mode="full")
    path = append_run_report(summary)
    logger.info(
        f"Run complete: {len(summary.tickers)} tickers, {summary.rows_written} rows, "
        f"{len(summary.failures)} failures, {summary.duration_str()}. Report: {path}"
    )
    return summary


async def run_backfill(ticker: str) -> RunSummary:
    """On-demand: fetch the Lists note's backfill-default intervals.

    Same database rule as `run_full` — `COBALT_ENV`, never an argument.
    """
    cfg = load_config()
    targets = cfg.backfill_targets(ticker)
    logger.info(f"Bar Archiver backfill for {ticker}: {len(targets)} targets")
    summary = await _run_targets(targets, mode=f"backfill:{ticker}")
    path = append_run_report(summary)
    logger.info(
        f"Backfill complete: {summary.rows_written} rows, "
        f"{len(summary.failures)} failures, {summary.duration_str()}. Report: {path}"
    )
    return summary


def _archive_nightly() -> None:
    """The scheduled nightly run, inside its F17 job row.

    Only the FULL run is the job. A `--backfill TICKER` is an operator
    fetching one symbol on demand; recording it as the nightly run would
    mark the night satisfied and silence the MISSED probe for a run that
    never happened.
    """
    from cobalt.jobs.entrypoint import as_job

    with as_job("com.cobalt.archiver") as job:
        summary = asyncio.run(run_full())
        # THIS is what makes F18's "archiver freshness (last run + rows
        # written)" answerable without a second table.
        job.result = {
            "rows_written": summary.rows_written,
            "tickers": len(summary.tickers),
            "requests": summary.requests,
            "failures": len(summary.failures),
            "duration": summary.duration_str(),
        }
        if summary.failures:
            # Raised, so the job row lands on `failed` with its exit code
            # and its error text — F18 turns red on exactly this.
            raise RuntimeError(
                f"{len(summary.failures)} archiver failure(s): "
                + "; ".join(summary.failures[:5])
            )


def main() -> None:
    import os

    # Same rationale as aset/__main__.py: the old tree's config loader
    # used to dump vault secrets at DEBUG on import (fixed at the source
    # 2026-08-24; this is cheap standing insurance, left in place).
    os.environ.setdefault("LOGURU_LEVEL", "INFO")

    import argparse

    parser = argparse.ArgumentParser(prog="archiver", description="Cobalt Bar Archiver")
    parser.add_argument(
        "--backfill",
        metavar="TICKER",
        help="Fetch the backfill-default intervals for one ticker instead of the full nightly run.",
    )
    args = parser.parse_args()

    from cobalt.jobs.entrypoint import JobStopped

    if args.backfill:
        summary = asyncio.run(run_backfill(args.backfill))
        if summary.failures:
            sys.exit(1)
        return

    try:
        _archive_nightly()
    except JobStopped as e:
        # Exit 0: a deliberate stop is not a failure (F17d).
        print(f"NOT RUN — {e}")
    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
