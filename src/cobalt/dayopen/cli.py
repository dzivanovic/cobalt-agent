"""`cobalt day-open` — RULED 2026-09-14, A.

    cobalt day-open [--date YYYY-MM-DD] [--json]
    cobalt day-open verdict "<one line>"

The bare command runs the six checks, writes
`docs/40 - DevDocs/reports/day-open-<date>.md` (a later run the same day
writes `day-open-<date>-<HHMMSS>.md` beside it — never a replacement),
and prints the VERDICT table. `--json` prints the same content as JSON
and writes nothing. `verdict` appends a
`SEAT VERDICT:` line to that day's report — the local seat's only write
path under the Qwen allowlist, through Cobalt rather than the shell
(see `cobalt.dayopen`'s module docstring for why).
"""

from __future__ import annotations

import argparse
import sys
from datetime import date

from cobalt.session.clock import SessionClock, now_utc

from . import runner
from .report import (
    ReportPathError,
    append_verdict,
    render_json,
    render_verdict_section,
    write_report,
)


def _parse_date(raw: str) -> date:
    try:
        return date.fromisoformat(raw)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"--date must be YYYY-MM-DD, got {raw!r}: {e}") from e


def cmd_run(args: argparse.Namespace) -> None:
    report = runner.run(report_date=args.date)
    if args.json:
        # Prints only. The 09-15 deploy smoke's `--json` run rewrote the
        # seat's report; a read-only flag writes nothing to disk.
        print(render_json(report))
        return
    try:
        path = write_report(report)
    except ReportPathError as e:
        print(f"FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    if path.name != f"day-open-{report.report_date:%Y-%m-%d}.md":
        print(f"NOTE: the day's report already exists and was NOT replaced — wrote {path.name} beside it")
    print(f"wrote {path}")
    print()
    print(render_verdict_section(report))


def cmd_verdict(args: argparse.Namespace) -> None:
    today = SessionClock.to_et(now_utc()).date()
    try:
        path = append_verdict(today, args.line)
    except ReportPathError as e:
        print(f"FAILED: {e}", file=sys.stderr)
        sys.exit(1)
    print(f"appended to {path}")


def add_parser(sub) -> None:
    day_open = sub.add_parser("day-open", help="The morning sweep (RULED 2026-09-14, A).")
    day_open.add_argument(
        "--date", type=_parse_date, default=None,
        help="Report date, YYYY-MM-DD (default: today's ET date).",
    )
    day_open.add_argument("--json", action="store_true", help="Print the report as JSON.")
    day_open.set_defaults(func=cmd_run)

    dsub = day_open.add_subparsers(dest="command")
    verdict = dsub.add_parser("verdict", help="Append a SEAT VERDICT line to today's report.")
    verdict.add_argument("line", help="One line — the local seat's verdict.")
    verdict.set_defaults(func=cmd_verdict)


__all__ = ["add_parser"]
