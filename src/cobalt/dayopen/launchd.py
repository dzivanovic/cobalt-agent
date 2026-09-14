"""C1's collector: `launchctl print gui/<uid>/<label>`.

Deliberately a SEPARATE parser from `cobalt.jobs.watchdog.launchctl_status`,
which shells out to `launchctl list` (tab-separated, no `runs` counter).
C1 is specified against the `launchctl print` shape captured in
`docs/40 - DevDocs/reports/day-open-2026-09-14.md` (S1):

    state = running
    runs = 1
    pid = 27385
    last exit code = (never exited)

`launchctl print` and `launchctl list` are two different launchd command
surfaces reporting the same daemon; a second parser here is not the
one-path rule's second copy of the same thing (L3) — nothing in this
module reads or writes what `launchctl_status` reads or writes, and nothing
here duplicates job-registry state.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from typing import Optional

#: One `key = value` line, e.g. "	state = running". Case- and
#: whitespace-tolerant; `launchctl print` indents with tabs.
_FIELD_RE = re.compile(r"^\s*(state|runs|pid|last exit code)\s*=\s*(.+?)\s*$")


class LaunchdPrintError(RuntimeError):
    """`launchctl print` could not be run — a real command failure, not a
    parse gap. C1 renders this as ERROR(command failed), never a guess."""


@dataclass(frozen=True)
class LaunchdPrintStatus:
    label: str
    state: Optional[str]
    pid: Optional[int]
    last_exit_code: Optional[str]
    runs: Optional[int]
    raw: str

    @property
    def running_with_pid(self) -> bool:
        return self.state == "running" and self.pid is not None


def parse_launchctl_print(label: str, text: str) -> LaunchdPrintStatus:
    """Pure parse: `launchctl print`'s raw stdout -> the four C1 fields.

    Takes the FIRST occurrence of each field (the top-level values;
    `launchctl print` nests sub-blocks — spawn cache, endpoints — that
    can repeat a key name deeper in the same dump).
    """
    fields: dict[str, str] = {}
    for line in text.splitlines():
        match = _FIELD_RE.match(line)
        if match:
            key, value = match.group(1), match.group(2)
            fields.setdefault(key, value)

    pid_raw = fields.get("pid")
    pid = int(pid_raw) if pid_raw and pid_raw.lstrip("-").isdigit() else None
    runs_raw = fields.get("runs")
    runs = int(runs_raw) if runs_raw and runs_raw.isdigit() else None
    return LaunchdPrintStatus(
        label=label,
        state=fields.get("state"),
        pid=pid,
        last_exit_code=fields.get("last exit code"),
        runs=runs,
        raw=text,
    )


def launchctl_print(label: str, *, timeout: float = 5.0) -> LaunchdPrintStatus:
    """Run `launchctl print gui/<uid>/<label>` for real.

    Fail-loud (L1): a `launchctl` binary that cannot be found or a
    command that exits non-zero RAISES rather than reporting a fake
    "not running" — "the probe is broken" and "the job is gone" are
    different facts.
    """
    binary = shutil.which("launchctl") or "/bin/launchctl"
    if not os.path.exists(binary):
        raise LaunchdPrintError("launchctl not found — cannot probe launchd jobs.")
    target = f"gui/{os.getuid()}/{label}"
    try:
        proc = subprocess.run(
            [binary, "print", target], capture_output=True, text=True, timeout=timeout
        )
    except (OSError, subprocess.TimeoutExpired) as e:
        raise LaunchdPrintError(f"`launchctl print {target}` failed to run: {e}") from e
    if proc.returncode != 0:
        raise LaunchdPrintError(
            f"`launchctl print {target}` exited {proc.returncode}: "
            f"{proc.stderr.strip() or proc.stdout.strip() or '(no output)'}"
        )
    return parse_launchctl_print(label, proc.stdout)


__all__ = [
    "LaunchdPrintError",
    "LaunchdPrintStatus",
    "launchctl_print",
    "parse_launchctl_print",
]
