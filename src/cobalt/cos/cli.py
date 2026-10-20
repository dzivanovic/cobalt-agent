"""CLI registration for the chief of staff (F20 C4d; L10). Read and dry-run only.

`cobalt cos run` runs the resident loop (the plist's own entry is
`python -m cobalt.cos.run`); `--dry-run` prints the session's options and
starts nothing. There is no approve subcommand (F-21).

`cobalt cos probe <item>` runs ONE live first-gate item (card 877) on a real
session in a scratch HOME: no DM, no store, no job row (`cos/probe.py`).
"""

from __future__ import annotations

#: The live first-gate items the probe runs (F20 FINAL `## First-gate experiments`).
PROBE_ITEMS = ("X2", "X10", "X11", "X12", "X3", "X14", "X17")


def _run(args) -> None:
    from .run import main

    raise SystemExit(main(["--dry-run"] if args.dry_run else []))


def _probe(args) -> None:
    from .probe import main

    raise SystemExit(main(args.item))


def add_parser(sub) -> None:
    group = sub.add_parser("cos", help="F20 chief of staff: the resident session (read and dry-run only) "
                                         "and its first-gate probe")
    csub = group.add_subparsers(dest="command", required=True)
    run = csub.add_parser("run", help="Run the CoS resident loop (com.cobalt.cos)")
    run.add_argument("--dry-run", action="store_true",
                     help="Print the session options (allowlist, env names, mode); start nothing.")
    run.set_defaults(func=_run)
    probe = csub.add_parser("probe", help="Run one live first-gate item on a scratch CoS session "
                                          "(prints one PROBE <item> OK|FAIL line)")
    probe.add_argument("item", choices=PROBE_ITEMS)
    probe.set_defaults(func=_probe)
