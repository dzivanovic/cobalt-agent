"""`cobalt smoke <suite>` — RULED 2026-09-15, R6 B (plan-s2-p4 STEP-9).

    cobalt smoke s2 --cutoff <ISO8601 with offset> [--date YYYY-MM-DD] [--prod] [--json]

Loads `configs/cobalt/smoke/<suite>.yaml` (a bad file crashes with its
line), runs every check read-only, prints the numbered verdict table and
OVERALL, and writes `docs/40 - DevDocs/reports/<suite>-smoke-<date>.md`.
`--json` prints the same content and writes nothing.

`--cutoff` is the P4 deploy instant (the D1 merge time from the deploy
report). It is REQUIRED and has no default: K3/K6 compare only rows at or
after it, and a guessed cutoff would silently widen or narrow what they
judge (L1). `--prod` has `cobalt db query`'s meaning — the production
database is refused without it.

Exit code: 0 GREEN, 1 AMBER or RED, so a scripted run cannot mistake a
red smoke for a green one.
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime

from cobalt.session.clock import now_utc

from . import report as report_mod
from .checks import SmokeDeps, build_context, default_deps, run_suite
from .config import load_suite, suite_path
from .models import Overall, SmokeReport


def run(
    suite_name: str, *, cutoff: datetime, report_date: date | None = None,
    now: datetime | None = None, prod: bool = False, deps: SmokeDeps | None = None,
) -> SmokeReport:
    """Load, contextualise, run. Writes nothing — `cmd_run` owns the file."""
    from cobalt.jobs.config import load_job_registry
    from cobalt.taxonomy.loader import load_tunables

    suite = load_suite(suite_path(suite_name))
    now = now or now_utc()
    registry = load_job_registry()
    ctx = build_context(
        now=now, report_date=report_date, cutoff=cutoff, prod=prod,
        anchor_spec=registry.spec(suite.day_anchor_job),
        tunables={key: row.value for key, row in load_tunables().by_key.items()},
    )
    outcomes = run_suite(suite, ctx, deps or default_deps(prod=prod))
    return report_mod.build_report(suite.suite, suite.title, ctx, outcomes, generated_at=now)


def _cutoff(raw: str) -> datetime:
    try:
        value = datetime.fromisoformat(raw)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"--cutoff must be ISO 8601, got {raw!r}") from e
    if value.tzinfo is None or value.utcoffset() is None:
        raise argparse.ArgumentTypeError(f"--cutoff {raw!r} has no offset; pass …-04:00 or Z")
    return value


def _date(raw: str) -> date:
    try:
        return date.fromisoformat(raw)
    except ValueError as e:
        raise argparse.ArgumentTypeError(f"--date must be YYYY-MM-DD, got {raw!r}") from e


def cmd_run(args: argparse.Namespace) -> None:
    rep = run(args.suite, cutoff=args.cutoff, report_date=args.date, prod=args.prod)
    if args.json:
        print(report_mod.render_json(rep))
    else:
        path = report_mod.write_report(rep, reports_dir=report_mod.REPORTS_DIR)
        print(f"wrote {path}\n")
        print(report_mod.render_table(rep))
    if rep.overall is not Overall.GREEN:
        sys.exit(1)


def add_parser(sub) -> None:
    smoke = sub.add_parser("smoke", help="Read-only sprint smoke checklist (S2-P4 R6).")
    smoke.add_argument("suite", help="Suite name: configs/cobalt/smoke/<suite>.yaml (e.g. s2).")
    smoke.add_argument("--cutoff", type=_cutoff, required=True,
                       help="Deploy instant, ISO 8601 with offset (K3/K6 compare rows at/after it).")
    smoke.add_argument("--date", type=_date, default=None, help="Report date (default: today ET).")
    smoke.add_argument("--prod", action="store_true", help="Read the production database.")
    smoke.add_argument("--json", action="store_true", help="Print JSON; write no report file.")
    smoke.set_defaults(func=cmd_run)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cobalt")
    add_parser(parser.add_subparsers(dest="group", required=True))
    return parser


__all__ = ["add_parser", "build_parser", "run"]
