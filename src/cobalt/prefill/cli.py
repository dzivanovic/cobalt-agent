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

from .daily import run_daily_prefill  # noqa: E402
from .drc import run_drc_prefill  # noqa: E402


def _run_daily() -> None:
    result = asyncio.run(run_daily_prefill())
    logger.info(f"Daily prefill: {result.action} — {result.path}")
    print(f"{result.action}: {result.path}")


def _run_drc(target_date: str | None) -> None:
    for_date_ = date.fromisoformat(target_date) if target_date else None
    result = asyncio.run(run_drc_prefill(for_date_=for_date_))
    logger.info(f"DRC prefill: {result.action} — {result.path} ({result.card_count} cards)")
    print(f"{result.action}: {result.path} ({result.card_count} cards)")


def main() -> None:
    parser = argparse.ArgumentParser(prog="prefill", description="Cobalt DRC & Daily prefill engine")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("daily", help="Prefill (or append to) today's Daily Note.")

    drc_parser = sub.add_parser("drc", help="Prefill (or append to) the evening DRC draft.")
    drc_parser.add_argument("--date", help="Target date YYYY-MM-DD (default: today).")

    args = parser.parse_args()

    try:
        if args.command == "daily":
            _run_daily()
        else:
            _run_drc(args.date)
    except Exception as e:
        logger.error(f"prefill {args.command} FAILED: {type(e).__name__}: {e}")
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
