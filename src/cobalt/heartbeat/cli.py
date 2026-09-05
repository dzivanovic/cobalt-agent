"""`cobalt heartbeat` — F18's command surface.

    cobalt heartbeat beat [--dry-run]     one beat (launchd runs this)
    cobalt heartbeat show                 probe and print, send nothing

`beat` is what `com.cobalt.heartbeat` runs every `heartbeat.interval_min`
minutes. It EXITS 0 on a red: a red heartbeat is the heartbeat working,
and a job row that flipped to `failed` every time something else was down
would make the heartbeat's own history useless. It exits non-zero only
when the beat itself could not run.
"""

from __future__ import annotations

import argparse
import sys

from cobalt import env

from .runner import run_beat, take_beat


def cmd_beat(args: argparse.Namespace) -> None:
    from cobalt.redact import install_log_guard

    install_log_guard()
    beat = run_beat(dry_run=args.dry_run)
    print(f"database: {env.resolve_db_name()}  (COBALT_ENV={env.resolve_env()})")
    print(beat.console())


def cmd_show(args: argparse.Namespace) -> None:
    """Probe and print. Writes nothing, sends nothing."""
    print(take_beat().console())


def add_parser(sub) -> None:
    hb = sub.add_parser("heartbeat", help="F18 heartbeat host (Charter §3 F18)")
    hsub = hb.add_subparsers(dest="command", required=True)

    beat = hsub.add_parser("beat", help="One beat: probe, write the note block, alert.")
    beat.add_argument("--dry-run", action="store_true", help="Probe and print; send/write nothing.")
    beat.set_defaults(func=cmd_beat)

    show = hsub.add_parser("show", help="Probe and print. Writes nothing, sends nothing.")
    show.set_defaults(func=cmd_show)


__all__ = ["add_parser"]
