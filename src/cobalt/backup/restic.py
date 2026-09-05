"""The restic mechanism: snapshot, forget, restore, freshness.

WHY A DUMP INSIDE THE SNAPSHOT and not a file on disk. A `.sql` lying in
`~/cobalt-backups` from some earlier night backs up whatever age it
happens to be. The dump is written fresh at the start of every run and
deleted at the end of it, so "the database at snapshot time" is the only
thing a snapshot can contain.

WHY IT STAGES AT A FIXED PATH and not in `tempfile.mkdtemp()`. Found by
the first restore drill (2026-09-04): a temp directory gives the dump a
new random path every night, so inside the repository the database lives
at `/var/folders/4b/.../cobalt-backup-egp09dbp/cobalt_brain.sql` on
Friday and somewhere else on Saturday. `restic restore --include` needs a
path you can type, and on the day it is needed nobody wants to list a
snapshot to find out where the database went. `STAGING` is that stable
path, and it is emptied in a `finally` so a 360 MB dump never outlives
the run that made it.

WHY `restic` IS RUN AS A SUBPROCESS with an explicit env. The repository
password reaches it through `RESTIC_PASSWORD` in the child's environment
and nowhere else — never a command line (visible in `ps`), never a file
on disk, never a log line. Same for the B2 keys.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

from loguru import logger

from .config import BackupConfig, Destination, load_backup_config

#: The tag every snapshot this module writes carries, so `forget` can
#: never prune something a human put in the same repository by hand.
TAG = "cobalt-nightly"

#: Where the database dump is staged so it has ONE path inside every
#: snapshot. Restoring it is then always:
#:     restic restore <id> --target DIR \
#:         --include /Users/cobalt/cobalt-backups/staging/cobalt_brain.sql
STAGING = Path.home() / "cobalt-backups" / "staging"


class BackupError(RuntimeError):
    """A backup could not be taken. Message is already credential-free."""


@dataclass
class SnapshotResult:
    destination: str
    snapshot_id: str
    files_new: int
    files_changed: int
    bytes_added: int
    forgotten: int = 0

    def describe(self) -> str:
        return (
            f"{self.destination}: snapshot {self.snapshot_id} — "
            f"{self.files_new} new / {self.files_changed} changed, "
            f"{self.bytes_added / 1e6:.1f} MB added, {self.forgotten} pruned"
        )


@dataclass
class BackupRun:
    """What F18 gets to report."""

    results: list[SnapshotResult] = field(default_factory=list)
    db_dump_bytes: int = 0

    def as_result(self) -> dict:
        return {
            "snapshots": len(self.results),
            "destinations": [r.destination for r in self.results],
            "snapshot_ids": {r.destination: r.snapshot_id for r in self.results},
            "bytes_added": sum(r.bytes_added for r in self.results),
            "db_dump_bytes": self.db_dump_bytes,
        }


def _binary() -> str:
    exe = shutil.which("restic")
    if exe is None:
        raise BackupError(
            "restic is not on PATH. It is the ruled tool (ledger 2026-09-04: "
            "'restic → B2 + SSD, NOT Time Machine'); install it with "
            "`brew install restic` rather than substituting another tool."
        )
    return exe


def _env(cfg: BackupConfig, dest: Destination) -> dict[str, str]:
    """Child environment carrying the credentials, and nothing else new.

    Raises rather than running unauthenticated: restic would otherwise
    prompt, and a prompt inside launchd is a job that hangs until its
    timeout instead of failing in the first second.
    """
    from cobalt.backup.secrets import vault_value

    env = dict(os.environ)
    env["RESTIC_PASSWORD"] = vault_value(cfg.password_vault_key)
    if dest.kind == "b2":
        env["B2_ACCOUNT_ID"] = vault_value(cfg.b2_key_id_vault_key)
        env["B2_ACCOUNT_KEY"] = vault_value(cfg.b2_app_key_vault_key)
    return env


def _run(args: list[str], env: dict[str, str], timeout: int = 3600) -> str:
    """Run restic. stderr is folded into the error, never logged raw."""
    proc = subprocess.run(
        [_binary(), *args], env=env, capture_output=True, text=True, timeout=timeout
    )
    if proc.returncode != 0:
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-4:]
        raise BackupError(f"restic {args[0]} exited {proc.returncode}: {' / '.join(tail)}")
    return proc.stdout


def dump_database(name: str, into: Path) -> Path:
    """A fresh `pg_dump` of `name`, into `into`. Returns the file."""
    from .pgdump import dump_database_to

    return dump_database_to(name, into / f"{name}.sql")


def snapshot(cfg: Optional[BackupConfig] = None, *, dry_run: bool = False) -> BackupRun:
    """Take one snapshot per armed destination. Fresh DB dump included."""
    cfg = cfg or load_backup_config()
    if not cfg.armed:
        raise BackupError(
            "no backup destination is enabled. Both legs of the ruling (external "
            "SSD, Backblaze B2) are off in configs/cobalt/backup.yaml — see the "
            "comment there for what each one is still missing. Refusing to exit 0 "
            "having written nothing."
        )
    run = BackupRun()
    STAGING.mkdir(parents=True, exist_ok=True)
    try:
        targets = [str(p) for p in cfg.sources]
        if cfg.database.enabled:
            dump = dump_database(cfg.database.name, STAGING)
            run.db_dump_bytes = dump.stat().st_size
            targets.append(str(dump))
            logger.info("backup: {} dumped, {:.1f} MB", cfg.database.name, run.db_dump_bytes / 1e6)
        for dest in cfg.armed:
            if dry_run:
                logger.info("backup: DRY RUN — would snapshot {} to {}", targets, dest.name)
                continue
            run.results.append(_snapshot_one(cfg, dest, targets))
    finally:
        # The dump is 360 MB today. It exists for the length of the run
        # and nothing else may depend on finding it afterwards.
        for leftover in STAGING.glob("*.sql"):
            leftover.unlink(missing_ok=True)
    return run


def _snapshot_one(cfg: BackupConfig, dest: Destination, targets: list[str]) -> SnapshotResult:
    env = _env(cfg, dest)
    base = ["-r", dest.restic_repo()]
    args = [*base, "backup", "--json", "--tag", TAG]
    for pat in cfg.excludes:
        args += ["--exclude", pat]
    args += targets

    summary = None
    for line in _run(args, env).splitlines():
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        if msg.get("message_type") == "summary":
            summary = msg
    if summary is None:
        raise BackupError(f"{dest.name}: restic backup produced no summary line")

    res = SnapshotResult(
        destination=dest.name,
        snapshot_id=summary.get("snapshot_id", "?")[:8],
        files_new=summary.get("files_new", 0),
        files_changed=summary.get("files_changed", 0),
        bytes_added=summary.get("data_added", 0),
    )
    # Retention runs with the SAME tag filter as the write, so a snapshot
    # a human took by hand into this repository is never in scope.
    out = _run([*base, "forget", "--tag", TAG, "--prune", "--json",
                *cfg.forget.restic_args()], env)
    try:
        removed = json.loads(out or "[]")
        res.forgotten = sum(len(g.get("remove") or []) for g in removed)
    except json.JSONDecodeError:
        res.forgotten = 0
    logger.info("backup: {}", res.describe())
    return res


def latest_snapshot_age(cfg: Optional[BackupConfig] = None) -> Optional[timedelta]:
    """Age of the newest tagged snapshot across armed destinations.

    `None` means the question could not be answered — no armed
    destination, or none holds a snapshot. The probe renders that as
    `??`, which is red but separately marked, so an operator knows they
    are looking at ignorance rather than at a diagnosis.
    """
    cfg = cfg or load_backup_config()
    newest: Optional[datetime] = None
    for dest in cfg.armed:
        out = _run(["-r", dest.restic_repo(), "snapshots", "--tag", TAG, "--json"],
                   _env(cfg, dest), timeout=120)
        for snap in json.loads(out or "[]"):
            when = datetime.fromisoformat(snap["time"].replace("Z", "+00:00"))
            if newest is None or when > newest:
                newest = when
    if newest is None:
        return None
    return datetime.now(timezone.utc) - newest


def restore(dest_name: str, snapshot_id: str, into: Path,
            cfg: Optional[BackupConfig] = None, *, include: Optional[str] = None) -> Path:
    """Restore `snapshot_id` (or a path inside it) into `into`."""
    cfg = cfg or load_backup_config()
    dest = next((d for d in cfg.destinations if d.name == dest_name), None)
    if dest is None:
        raise BackupError(
            f"unknown destination {dest_name!r}. Configured: "
            f"{', '.join(d.name for d in cfg.destinations)}."
        )
    into.mkdir(parents=True, exist_ok=True)
    args = ["-r", dest.restic_repo(), "restore", snapshot_id, "--target", str(into)]
    if include:
        args += ["--include", include]
    _run(args, _env(cfg, dest))
    return into


__all__ = [
    "TAG",
    "BackupError",
    "BackupRun",
    "SnapshotResult",
    "dump_database",
    "latest_snapshot_age",
    "restore",
    "snapshot",
]
