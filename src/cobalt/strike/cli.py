"""CLI registration for the strike path (S4-P1)."""

from __future__ import annotations

from datetime import date

from . import measure, week


def add_parser(sub) -> None:
    group = sub.add_parser("strike", help="F9 strike path: the live-feed re-measure and the week report")
    ssub = group.add_subparsers(dest="command", required=True)
    run = ssub.add_parser("measure", help="Re-measure Finviz-lite bar lag (measurement only; no DB, no vault)")
    run.add_argument("--names", required=True, help="Comma-separated tickers (at most strike.max_armed).")
    run.add_argument("--cadence", type=int, required=True, help="Seconds per cycle (at least strike.poll_interval_min).")
    run.add_argument("--minutes", type=int, required=True, help="Run length; the GET cap is derived from it.")
    run.add_argument("--out", required=True, help="Directory for strike-measure-<date>.jsonl and .md.")
    run.set_defaults(func=measure.command)
    # S4-P2 S6 (DECISION E8): read-only.
    report = ssub.add_parser("week", help="F9 week report: detect and panel lag per ET day (read only)")
    report.add_argument("--from", dest="start", type=date.fromisoformat, default=None,
                        help="First ET date, inclusive (default: Monday of this week).")
    report.add_argument("--to", dest="end", type=date.fromisoformat, default=None,
                        help="Last ET date, inclusive (default: today).")
    report.set_defaults(func=week.command)
