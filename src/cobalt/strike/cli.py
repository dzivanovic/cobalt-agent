"""CLI registration for the strike path (S4-P1)."""

from __future__ import annotations

from . import measure


def add_parser(sub) -> None:
    group = sub.add_parser("strike", help="F9 strike path: the live-feed re-measure")
    ssub = group.add_subparsers(dest="command", required=True)
    run = ssub.add_parser("measure", help="Re-measure Finviz-lite bar lag (measurement only; no DB, no vault)")
    run.add_argument("--names", required=True, help="Comma-separated tickers (at most strike.max_armed).")
    run.add_argument("--cadence", type=int, required=True, help="Seconds per cycle (at least strike.poll_interval_min).")
    run.add_argument("--minutes", type=int, required=True, help="Run length; the GET cap is derived from it.")
    run.add_argument("--out", required=True, help="Directory for strike-measure-<date>.jsonl and .md.")
    run.set_defaults(func=measure.command)
