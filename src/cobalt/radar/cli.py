"""CLI registration for radar operations."""

from __future__ import annotations

from . import throttle
from . import config
from . import replay
from . import runner
from . import propose
from . import sources


def add_parser(sub) -> None:
    group = sub.add_parser("radar", help="Radar source, pool, and polling operations")
    rsub = group.add_subparsers(dest="command", required=True)
    probe = rsub.add_parser("throttle-probe", help="Measure Finviz request tolerance")
    probe.add_argument("--names", type=int, default=50)
    probe.add_argument("--grids", default="60,30,15,10")
    probe.add_argument("--cycles", type=int, default=3)
    probe.set_defaults(func=throttle.command)

    check = rsub.add_parser("check", help="Validate radar config and tunables")
    check.set_defaults(func=config.command)

    replay_build = rsub.add_parser("replay-build", help="Build replay snapshots from system.bars")
    replay_build.add_argument("day")
    replay_build.set_defaults(func=replay.replay_build_command)

    run = rsub.add_parser("run", help="Run the resident radar loop")
    run.set_defaults(func=runner.run_command)

    scan = rsub.add_parser("scan", help="Run one radar scan")
    scan.add_argument("--once", action="store_true")
    scan.add_argument("--replay")
    scan.add_argument("--from", dest="from_time")
    scan.add_argument("--to", dest="to_time")
    scan.set_defaults(func=runner.scan_command)

    screens = rsub.add_parser("screens", help="Propose/apply Screens note blocks")
    ssub = screens.add_subparsers(dest="screens_command", required=True)
    screens_propose = ssub.add_parser("propose")
    screens_propose.add_argument("--pool-block", required=True)
    screens_propose.add_argument("--ft-compare", action="store_true")
    screens_propose.set_defaults(func=propose.screens_propose)
    screens_apply = ssub.add_parser("apply")
    _apply_args(screens_apply, "screens")

    lists = rsub.add_parser("lists", help="Propose/apply Lists note")
    lsub = lists.add_subparsers(dest="lists_command", required=True)
    lists_propose = lsub.add_parser("propose")
    lists_propose.set_defaults(func=propose.lists_propose)
    lists_apply = lsub.add_parser("apply")
    _apply_args(lists_apply, "lists")

    source_cmd = rsub.add_parser("sources", help="Validate and list note-derived sources")
    source_cmd.add_argument("--json", action="store_true")
    source_cmd.add_argument("--archiver-diff", action="store_true")
    source_cmd.add_argument("--yaml-rev", default="HEAD")
    source_cmd.set_defaults(func=sources.command)


def _apply_args(parser, kind: str) -> None:
    parser.add_argument("--proposal", required=True)
    parser.add_argument("--hitl", required=True)
    parser.add_argument("--sha256", required=True)
    parser.set_defaults(func=propose.apply, proposal_kind=kind)


__all__ = ["add_parser"]
