"""`cobalt backup` — run, status, restore.

    cobalt backup run                 snapshot every armed destination
    cobalt backup run --dry-run       say what it would do, touch nothing
    cobalt backup status              armed destinations + newest snapshot age
    cobalt backup restore <dest> <id> --into DIR [--include PATH]

`run` goes through `as_job`, so a manual catch-up run IS a run of
com.cobalt.backup: it lands in `cobalt_jobs`, and it stops the MISSED
probe firing an hour later.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from .config import load_backup_config
from .restic import latest_snapshot_age, restore, snapshot

LABEL = "com.cobalt.backup"


def add_parser(sub) -> None:
    p = sub.add_parser("backup", help="Nightly restic backup of the vault + cobalt_brain.")
    s = p.add_subparsers(dest="backup_cmd", required=True)

    run = s.add_parser("run", help="Snapshot every armed destination.")
    run.add_argument("--dry-run", action="store_true",
                     help="Say what it would do; write nothing, touch no jobs row.")
    run.set_defaults(func=_run)

    st = s.add_parser("status", help="Armed destinations and newest snapshot age.")
    st.set_defaults(func=_status)

    rs = s.add_parser("restore", help="Restore a snapshot (or one path from it).")
    rs.add_argument("destination")
    rs.add_argument("snapshot_id")
    rs.add_argument("--into", required=True, type=Path)
    rs.add_argument("--include", default=None,
                    help="Restore only this path from the snapshot.")
    rs.set_defaults(func=_restore)


def _run(args) -> int:
    from cobalt.jobs.entrypoint import as_job

    with as_job(LABEL, skip=args.dry_run) as job:
        result = snapshot(dry_run=args.dry_run)
        job.result = result.as_result()
        for r in result.results:
            print(r.describe())
        if args.dry_run:
            print("DRY RUN — nothing written, no jobs row touched.")
    return 0


def _status(args) -> int:
    cfg = load_backup_config()
    print(f"forget policy: {cfg.forget.describe()}")
    print(f"sources      : {', '.join(str(p) for p in cfg.sources)}")
    print(f"database     : {cfg.database.name}" if cfg.database.enabled else "database     : OFF")
    for d in cfg.destinations:
        state = "ARMED" if d.enabled else "off"
        print(f"  {d.name:<5} {d.kind:<5} {state:<5} {d.repo or '(no repo configured)'}")
    if not cfg.armed:
        print("\nNO DESTINATION IS ARMED — there is no backup. See the comment at the "
              "top of configs/cobalt/backup.yaml for what each leg is missing.")
        return 1
    age = latest_snapshot_age(cfg)
    print(f"\nnewest snapshot: {'NONE' if age is None else f'{age.total_seconds()/3600:.1f} h old'}")
    return 0


def _restore(args) -> int:
    into = restore(args.destination, args.snapshot_id, args.into, include=args.include)
    print(f"restored into {into}")
    return 0


__all__ = ["LABEL", "add_parser"]
