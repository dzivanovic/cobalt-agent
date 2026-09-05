"""`pg_dump` for the backup, wherever the server actually lives.

THIS HOST HAS NO `pg_dump` ON PATH. Postgres runs in the `cobalt_memory`
container (docker-compose, OrbStack), and the client shipped inside that
image is the one guaranteed to match the server — 16.12 against 16.12.
Dumping through `docker exec` is therefore not a workaround, it is the
only version-correct client on the machine. A host binary is preferred
when one exists, because a backup that needs Docker running is a backup
with one more thing that can be down.

The password reaches the client through the child's environment, never a
command line and never a file.
"""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

from loguru import logger

#: The compose service that runs Postgres. Named here rather than
#: discovered, so a second Postgres container can never be dumped by
#: accident.
CONTAINER = "cobalt_memory"


class DumpError(RuntimeError):
    """The dump could not be taken. Message carries no credential."""


def _parts() -> tuple[str, str, str]:
    """(host, user, password) — the same env parts `cobalt.db` composes
    its DSN from, so there is one answer to 'which server'."""
    host = os.getenv("POSTGRES_HOST") or "localhost"
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    missing = [n for n, v in (("POSTGRES_USER", user), ("POSTGRES_PASSWORD", password)) if not v]
    if missing:
        raise DumpError(f"missing connection part(s): {', '.join(missing)}")
    return host, user, password  # type: ignore[return-value]


def dump_database_to(name: str, out: Path) -> Path:
    """Plain-format `pg_dump` of `name` into `out`. Returns `out`."""
    host, user, password = _parts()
    out.parent.mkdir(parents=True, exist_ok=True)

    host_binary = shutil.which("pg_dump")
    if host_binary:
        cmd = [host_binary, "-h", host, "-U", user, "-d", name, "--format=plain"]
        env = {**os.environ, "PGPASSWORD": password}
        where = "host pg_dump"
    else:
        docker = shutil.which("docker")
        if docker is None:
            raise DumpError(
                "neither pg_dump nor docker is on PATH, so there is no way to reach "
                f"the {name} server. Install libpq (`brew install libpq`) or make "
                "Docker available to the backup job."
            )
        cmd = [docker, "exec", "-e", f"PGPASSWORD={password}", CONTAINER,
               "pg_dump", "-h", "127.0.0.1", "-U", user, "-d", name, "--format=plain"]
        env = dict(os.environ)
        where = f"pg_dump inside {CONTAINER}"

    with out.open("wb") as fh:
        proc = subprocess.run(cmd, stdout=fh, stderr=subprocess.PIPE, env=env, timeout=1800)
    if proc.returncode != 0:
        tail = (proc.stderr or b"").decode(errors="replace").strip().splitlines()[-3:]
        raise DumpError(f"{where} exited {proc.returncode}: {' / '.join(tail)}")

    size = out.stat().st_size
    # pg_dump exits 0 on an empty database, and an empty dump is the
    # backup that looks green and restores nothing.
    if size == 0 or b"PostgreSQL database dump complete" not in out.read_bytes()[-4096:]:
        raise DumpError(
            f"the {name} dump is {size} bytes and does not end with pg_dump's own "
            "completion marker — it is truncated, not a backup."
        )
    logger.info("backup: {} via {} — {:.1f} MB", name, where, size / 1e6)
    return out


__all__ = ["CONTAINER", "DumpError", "dump_database_to"]
