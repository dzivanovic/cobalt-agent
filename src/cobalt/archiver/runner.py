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


async def _run_targets(targets: list[tuple[str, Interval]], mode: str) -> RunSummary:
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
    """Nightly job: archive tier_a + tier_b per their configured intervals.

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
    """On-demand: fetch ALL tier_a intervals for one ticker (a new name
    joining tier_a, or a manual re-fill). Same database rule as
    `run_full` — `COBALT_ENV`, never an argument."""
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
        help="Fetch all tier_a intervals for one ticker on demand, instead of the full nightly run.",
    )
    args = parser.parse_args()

    if args.backfill:
        summary = asyncio.run(run_backfill(args.backfill))
    else:
        summary = asyncio.run(run_full())

    if summary.failures:
        sys.exit(1)


if __name__ == "__main__":
    main()
