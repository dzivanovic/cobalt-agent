"""`cobalt jobs` — F17's command surface, plus `cobalt stop` / `resume`.

    cobalt jobs list                     the table, as F18 reads it
    cobalt jobs register                 upsert every row from jobs.yaml
    cobalt jobs check                    run the watchdog, print findings
    cobalt jobs run LABEL -- CMD ARGS    wrap any command as that job
    cobalt stop  [--phrase "COBALT STOP"]
    cobalt resume

`jobs run` is the plist-facing half of the wrapper: a launchd job whose
program is not Python (or is a `uv run` of something else) gets its row,
its heartbeat and its exit code by being launched through this.
"""

from __future__ import annotations

import argparse
import subprocess
import sys

from cobalt import env

from . import killswitch
from .config import load_job_registry
from .models import RED_STATES
from .store import JobStore
from .watchdog import sweep
from .wrapper import JobStopped, job_run


def _store() -> JobStore:
    store = JobStore()
    store.ensure_schema()
    return store


def cmd_list(args: argparse.Namespace) -> None:
    store = _store()
    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    print(killswitch.read(store).describe())
    rows = store.all()
    if not rows:
        print("\nno jobs registered — run `cobalt jobs register`")
        return
    red_values = {s.value for s in RED_STATES}
    print(
        f"\n{'LABEL':<28} {'KIND':<9} {'STATE':<9} {'SRC':<8} {'LAST FINISH':<20} "
        f"{'EXIT':<5} CADENCE"
    )
    for r in rows:
        finish = f"{r['finished_at']:%Y-%m-%d %H:%M:%S}" if r["finished_at"] else "-"
        mark = " !" if r["state"] in red_values else "  "
        print(
            f"{r['label']:<28} {r['kind']:<9} {r['state']:<9}{mark[1]} "
            f"{r['heartbeat_source']:<8} {finish:<20} "
            f"{'-' if r['exit_code'] is None else r['exit_code']:<5} "
            f"{r['expected_cadence'] or '(resident)'}"
        )
        if r["last_error"]:
            print(f"{'':>28}   last_error: {r['last_error'][:160]}")


def cmd_register(args: argparse.Namespace) -> None:
    store = _store()
    registry = load_job_registry()
    labels = store.register_all(registry)
    print(f"database: {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    print(f"registered {len(labels)} job(s):")
    for label in labels:
        spec = registry.spec(label)
        print(f"  {label:<28} {spec.kind!s:<9} supervisor={spec.supervisor!s:<8} "
              f"timeout={spec.timeout_s}s  {spec.cadence or '(resident)'}")


def cmd_check(args: argparse.Namespace) -> None:
    findings = sweep()
    for f in findings:
        print(f.line())
    bad = [f for f in findings if not f.ok]
    print(f"\n{len(findings)} job(s) checked, {len(bad)} RED.")
    if bad:
        sys.exit(1)


def cmd_run(args: argparse.Namespace) -> None:
    """Wrap an arbitrary command as `label`. Its exit code is ours."""
    if not args.command:
        raise SystemExit("nothing to run — pass the command after `--`")
    try:
        with job_run(args.label) as run:
            proc = subprocess.run(args.command)
            run.result = {"argv": args.command, "returncode": proc.returncode}
            if proc.returncode != 0:
                raise RuntimeError(
                    f"{args.label}: `{' '.join(args.command)}` exited "
                    f"{proc.returncode}"
                )
    except JobStopped as e:
        # Exit 0: a deliberate stop is not a failure and must not paint
        # F18 red for a state the operator caused on purpose.
        print(f"NOT RUN — {e}")
        return
    print(f"{args.label}: exit 0")


def cmd_stop(args: argparse.Namespace) -> None:
    state = killswitch.engage(by=args.by, phrase=args.phrase)
    print(state.describe())


def cmd_resume(args: argparse.Namespace) -> None:
    state = killswitch.clear(by=args.by)
    print(state.describe())


def add_parser(sub) -> None:
    jobs = sub.add_parser("jobs", help="F17 task integrity (Charter §3 F17)")
    jsub = jobs.add_subparsers(dest="command", required=True)

    lst = jsub.add_parser("list", help="Every job row, as F18 reads it.")
    lst.set_defaults(func=cmd_list)

    reg = jsub.add_parser("register", help="Upsert every row from configs/cobalt/jobs.yaml.")
    reg.set_defaults(func=cmd_register)

    check = jsub.add_parser("check", help="Run the watchdog (zombie / missed).")
    check.set_defaults(func=cmd_check)

    run = jsub.add_parser("run", help="Run a command wrapped as a registered job.")
    run.add_argument("label")
    run.add_argument("command", nargs=argparse.REMAINDER)
    run.set_defaults(func=cmd_run)


def add_stop_parsers(sub) -> None:
    """`cobalt stop` / `cobalt resume` — top-level, not under `jobs`.

    Deliberately: the kill phrase is the thing you reach for when
    something is wrong, and `cobalt jobs killswitch engage` is not what
    anyone types at that moment.
    """
    stop = sub.add_parser("stop", help="Engage the kill phrase — stop all jobs (F17d).")
    stop.add_argument("--phrase", default=None, help="Defaults to jobs.yaml's kill_phrase.")
    stop.add_argument("--by", default="cli", help="Who is stopping (recorded).")
    stop.set_defaults(func=cmd_stop)

    resume = sub.add_parser("resume", help="Clear the kill phrase (F17d).")
    resume.add_argument("--by", default="cli", help="Who is resuming (recorded).")
    resume.set_defaults(func=cmd_resume)


__all__ = ["add_parser", "add_stop_parsers"]
