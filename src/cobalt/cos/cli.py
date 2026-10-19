"""CLI registration for the chief of staff (F20 C4d; L10). Read and dry-run only.

`cobalt cos run` runs the resident loop (the plist's own entry is
`python -m cobalt.cos.run`); `--dry-run` prints the session's options and
starts nothing. There is no approve subcommand (F-21).
"""

from __future__ import annotations


def _run(args) -> None:
    from .run import main

    raise SystemExit(main(["--dry-run"] if args.dry_run else []))


def add_parser(sub) -> None:
    group = sub.add_parser("cos", help="F20 chief of staff: the resident session (read and dry-run only)")
    csub = group.add_subparsers(dest="command", required=True)
    run = csub.add_parser("run", help="Run the CoS resident loop (com.cobalt.cos)")
    run.add_argument("--dry-run", action="store_true",
                     help="Print the session options (allowlist, env names, mode); start nothing.")
    run.set_defaults(func=_run)
