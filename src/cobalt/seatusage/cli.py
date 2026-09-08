"""`cobalt seat-usage` — the report's command surface.

    cobalt seat-usage run [--dry-run]   one run (launchd runs this)
    cobalt seat-usage show              print today's table, write nothing
    cobalt seat-usage gate              the L15 four-gate answer sheet

`run` is what `com.cobalt.seat-usage` executes every
`seat_usage.interval_min` minutes inside `seat_usage.window`. It goes
through the F17 wrapper, so a failure is a red job row with the reason
on it. `--dry-run` deliberately skips the wrapper: a rehearsal must
never leave a row saying the report was refreshed.
"""

from __future__ import annotations

import argparse

from cobalt import env

from .config import load_seat_usage_config
from .runner import run, run_as_job, today_et


def cmd_run(args: argparse.Namespace) -> None:
    from cobalt.redact import install_log_guard

    install_log_guard()
    outcome = run(dry_run=True) if args.dry_run else run_as_job()
    print(f"database: {env.resolve_db_name()}  (COBALT_ENV={env.resolve_env()})")
    print(outcome.console())


def cmd_show(args: argparse.Namespace) -> None:
    """Render today's table to stdout. Writes nothing, touches no file."""
    from . import ccusage as ccusage_mod
    from . import report as report_mod
    from cobalt.session import clock as clock_mod
    from cobalt.session.clock import session_clock

    cfg = load_seat_usage_config()
    day = today_et()
    usage = ccusage_mod.collect(cfg, day)
    print(
        report_mod.unit_body(
            cfg,
            usage,
            now=session_clock().to_et(clock_mod.now_utc()),
            previous=None,
            argv=ccusage_mod.argv(cfg, day),
        )
    )


def cmd_gate(args: argparse.Namespace) -> None:
    """The four-gate law's answer sheet, checked rather than claimed."""
    from . import ccusage as ccusage_mod

    cfg = load_seat_usage_config()
    print(f"tool          {cfg.tool.name}")
    print(f"pinned        {cfg.tool.version}")
    print(f"binary        {cfg.tool.binary_path}")
    print(f"license       {cfg.tool.license}")
    print(f"network       {'NONE at run time (--offline)' if cfg.tool.offline else 'ONLINE'}")
    print(f"report        {cfg.report_file}")
    try:
        found = ccusage_mod.assert_pinned(cfg)
    except ccusage_mod.CcusageError as e:
        print(f"installed     FAILED — {e}")
        raise SystemExit(1)
    print(f"installed     {found}  (matches the pin)")
    print(f"argv          {' '.join(ccusage_mod.argv(cfg, today_et()))}")


def add_parser(sub) -> None:
    su = sub.add_parser("seat-usage", help="The hourly seat-usage report (L15-gated ccusage).")
    ssub = su.add_subparsers(dest="command", required=True)

    r = ssub.add_parser("run", help="One run: collect, write today's unit in place.")
    r.add_argument(
        "--dry-run", action="store_true",
        help="Compute and diff everything; write nothing and record no job row.",
    )
    r.set_defaults(func=cmd_run)

    s = ssub.add_parser("show", help="Print today's table. Writes nothing.")
    s.set_defaults(func=cmd_show)

    g = ssub.add_parser("gate", help="The L15 four-gate answer sheet for the pinned tool.")
    g.set_defaults(func=cmd_gate)


__all__ = ["add_parser"]
