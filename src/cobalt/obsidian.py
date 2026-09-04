"""Is Obsidian running? — the probe RULING 6 asks for.

WHY THIS EXISTS. Cobalt and Obsidian are two unsynchronised writers to
the same files, and the vault reaches Dejan's other devices only through
Obsidian Sync — which means through a *running* Obsidian process on this
Mac. On 2026-09-04 that assumption broke in the most expensive way
available: `prefill-daily` created `2026-09-04.md` correctly at 05:15
(write_id 525-528, all four rows in `vault_writes`), but no Obsidian
instance had run on the Mac since the 15.7.9 reboot the evening before.
Cobalt's 118 lines never reached Sync, and at 06:30 the Obsidian
daily-notes plugin on the trading PC created its own bare template for
the same date and Sync propagated THAT back over the Mac's copy. Every
byte Cobalt wrote was correct, audited, and invisible.

A vault write with no Obsidian process is therefore not a success. It is
a write to a directory nobody is watching. This module is the probe that
lets the writer say so (RULING 6 / 3d) and — once the thin heartbeat
lane is built — lets the heartbeat go red on it (3c).

Deliberately `pgrep`, not a PID file or a port check: Obsidian is a GUI
app supervised by launchd (`ops/com.cobalt.obsidian.plist`), it exposes
no health endpoint, and the question being asked is exactly "is there a
process". `-x` matches the main app process only, never the
`Obsidian Helper (Renderer)` children, so the count is the count of
running Obsidian instances.
"""

import shutil
import subprocess

PROCESS_NAME = "Obsidian"

# The exact ERROR line RULING 6.3d specifies for the writer's run report.
NOT_SYNCING_ERROR = "written; Obsidian not running — will not sync"


class ObsidianProbeError(RuntimeError):
    """The probe itself could not run — never reported as "not running"."""


def obsidian_pids() -> list[int]:
    """PIDs of running Obsidian main processes (empty list = not running).

    Fail-loud: an unusable `pgrep` raises rather than returning `[]`.
    "The probe is broken" and "Obsidian is down" are different facts and
    must never be collapsed into the same answer — collapsing them is
    how a red condition becomes invisible.
    """
    pgrep = shutil.which("pgrep")
    if pgrep is None:
        raise ObsidianProbeError("pgrep not found on PATH — cannot probe for Obsidian.")
    proc = subprocess.run(
        [pgrep, "-x", PROCESS_NAME], capture_output=True, text=True, timeout=10
    )
    if proc.returncode == 0:
        return [int(line) for line in proc.stdout.split() if line.strip().isdigit()]
    if proc.returncode == 1:
        return []  # documented pgrep exit code: no matching process
    raise ObsidianProbeError(
        f"pgrep -x {PROCESS_NAME} failed with exit {proc.returncode}: "
        f"{proc.stderr.strip() or '(no stderr)'}"
    )


def is_running() -> bool:
    """True when at least one Obsidian main process exists."""
    return bool(obsidian_pids())


def sync_status() -> tuple[bool, str]:
    """`(running, human_readable)` — the one call the writer and the
    heartbeat both make, so they can never disagree about the wording."""
    pids = obsidian_pids()
    if pids:
        return True, f"Obsidian running (pid {', '.join(str(p) for p in pids)})"
    return False, NOT_SYNCING_ERROR
