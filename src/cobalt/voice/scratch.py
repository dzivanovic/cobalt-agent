"""Ephemeral audio: the scratch directory's ONE writer, ONE unlink, the
start sweep (R2-1 SIDE B — his letter, R56) and the directory lock.

THE LIFE OF A CLIP (FINAL §5). The upload handler writes
`<scratch_dir>/<turn_id>.<ext>` (dir 0700, file 0600, extension from a
CLOSED content-type map), the Transcriber reads it, and it is unlinked in a
`finally:` — right after the transcript, or on any failure of the turn.
Audio never reaches the database, the vault or git (R18 (b)).

THE START SWEEP — SIDE B. On every ASET process start, before the first
request is served, EVERY file in `scratch_dir` is deleted (no age test);
one AMBER line per file deleted, one RED line per unlink that fails (L9).

THE DIRECTORY LOCK (X-X22). Side B's premise — "no turn of a new process
is live, so any file present is a leftover" — is FALSE when an orphaned
child of a killed job still serves: X-X22 measured a python child alive and
holding its port while launchd respawned the job. So the serving process
takes an exclusive non-blocking `flock` on `<scratch_dir>/.lock` BEFORE the
sweep and holds it for its lifetime. If another process holds it, the sweep
deletes NOTHING, says RED naming the holder's pid, and the start FAILS
(`ScratchLocked`, L1). The CLI's `--audio` path takes the same lock for the
length of its turn.

ONE UNLINK (L3): `unlink_scratch()` is the only place that removes a file
here — the turn and the sweep both call it.
"""

from __future__ import annotations

import fcntl
import os
import re
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from loguru import logger

from .models import DegradedLine

LOCK_NAME = ".lock"
_TURN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9-]{7,63}$")

#: The CLOSED content-type map (base type, parameters stripped). E1 (the
#: device session) fixes what the phone and the trading PC actually send;
#: the widget's `isTypeSupported` chain asks for these in this order.
CONTENT_TYPES = {
    "audio/webm": "webm",
    "audio/ogg": "ogg",
    "audio/mp4": "m4a",
    "audio/x-m4a": "m4a",
    "audio/wav": "wav",
    "audio/x-wav": "wav",
}
EXTENSIONS = {v: k for k, v in reversed(list(CONTENT_TYPES.items()))}


class ScratchRefused(RuntimeError):
    """A write or a sweep that must not happen — named."""


class ScratchUnlinkFailed(RuntimeError):
    """A turn's own audio could not be deleted — the turn FAILS loud."""


class ScratchLocked(RuntimeError):
    """Another process holds the scratch directory — nothing was deleted."""

    def __init__(self, directory: Path, holder_pid: Optional[int]):
        self.directory = directory
        self.holder_pid = holder_pid
        who = f"pid {holder_pid}" if holder_pid else "an unknown process"
        super().__init__(
            f"voice scratch dir {directory} is locked by {who} — the start sweep deleted NOTHING. "
            "A process still owns this directory (X-X22: an orphan can outlive its job); "
            "find it and stop it before this process may serve voice turns."
        )


def ensure_dir(directory: Path) -> Path:
    """Create the directory 0700 (parents included) or tighten it to 0700."""
    directory = Path(directory)
    if directory.is_symlink():
        raise ScratchRefused(f"voice scratch dir {directory} is a symlink — refused")
    directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    os.chmod(directory, 0o700)
    return directory


def ext_for(content_type: str) -> str:
    base = (content_type or "").split(";", 1)[0].strip().lower()
    ext = CONTENT_TYPES.get(base)
    if ext is None:
        raise ScratchRefused(
            f"unsupported audio content type {content_type!r} — the closed map is {sorted(CONTENT_TYPES)}"
        )
    return ext


def write_scratch(directory: Path, turn_id: str, data: bytes, content_type: str) -> Path:
    """THE ONE WRITER of the scratch directory."""
    if not isinstance(turn_id, str) or not _TURN_ID.match(turn_id):
        raise ScratchRefused(f"turn id {turn_id!r} is not a scratch file name")
    if not data:
        raise ScratchRefused("zero-byte audio — nothing was recorded")
    ext = ext_for(content_type)
    directory = ensure_dir(directory)
    path = directory / f"{turn_id}.{ext}"
    if path.parent != directory:  # pragma: no cover - the regex already forbids it
        raise ScratchRefused(f"{path} is outside {directory}")
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError:
        raise ScratchRefused(f"{path.name} already exists — one file per turn") from None
    try:
        os.write(fd, data)
    finally:
        os.close(fd)
    os.chmod(path, 0o600)
    return path


@dataclass
class UnlinkResult:
    ok: bool
    line: DegradedLine


def unlink_scratch(path: Path, reason: str) -> UnlinkResult:
    """THE ONE UNLINK (L3): the turn's `finally:` and the start sweep."""
    try:
        os.unlink(path)
    except FileNotFoundError:
        return UnlinkResult(True, DegradedLine(level="amber", text=f"voice scratch {Path(path).name} already gone ({reason})"))
    except OSError as e:
        text = f"voice scratch {Path(path).name} could NOT be deleted ({reason}): {type(e).__name__}"
        logger.error("RED {}", text)
        return UnlinkResult(False, DegradedLine(level="red", text=text))
    return UnlinkResult(True, DegradedLine(level="amber", text=f"voice scratch {Path(path).name} deleted ({reason})"))


@dataclass
class HeldAudio:
    """A turn's scratch file for the length of the turn."""

    path: Path
    size: int
    deleted_at: Optional[datetime] = None
    lines: list[DegradedLine] = field(default_factory=list)

    def unlink_now(self, reason: str) -> None:
        if self.deleted_at is not None:
            return
        r = unlink_scratch(self.path, reason)
        if not r.ok:
            self.lines.append(r.line)
            raise ScratchUnlinkFailed(r.line.text)
        self.deleted_at = datetime.now(timezone.utc)


@contextmanager
def turn_audio(directory: Path, turn_id: str, data: bytes, content_type: str) -> Iterator[HeldAudio]:
    """Write the clip, hand it to the turn, and unlink it in `finally:` —
    on success, on a transcribe failure, on a Plan failure, on anything."""
    path = write_scratch(directory, turn_id, data, content_type)
    held = HeldAudio(path=path, size=len(data))
    try:
        yield held
    finally:
        held.unlink_now("turn finally")


class DirectoryLock:
    """Exclusive, non-blocking `flock` on `<scratch_dir>/.lock` for the life
    of the serving process (or of one CLI `--audio` turn)."""

    def __init__(self, directory: Path):
        self.directory = ensure_dir(Path(directory))
        self.path = self.directory / LOCK_NAME
        self._fd: Optional[int] = os.open(self.path, os.O_RDWR | os.O_CREAT, 0o600)
        try:
            fcntl.flock(self._fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            holder = self._read_holder()
            os.close(self._fd)
            self._fd = None
            logger.error("RED voice scratch dir {} locked by pid {} — start sweep deleted nothing",
                         self.directory, holder)
            raise ScratchLocked(self.directory, holder) from None
        os.chmod(self.path, 0o600)
        os.ftruncate(self._fd, 0)
        os.pwrite(self._fd, str(os.getpid()).encode(), 0)

    def _read_holder(self) -> Optional[int]:
        try:
            raw = os.pread(self._fd, 32, 0).decode().strip()
            return int(raw) if raw else None
        except (OSError, ValueError):
            return None

    @property
    def held(self) -> bool:
        return self._fd is not None

    def release(self) -> None:
        if self._fd is not None:
            try:
                fcntl.flock(self._fd, fcntl.LOCK_UN)
            finally:
                os.close(self._fd)
                self._fd = None


@dataclass
class SweepReport:
    deleted: int = 0
    failed: int = 0
    lines: list[DegradedLine] = field(default_factory=list)


def start_sweep(directory: Path, lock: DirectoryLock) -> SweepReport:
    """SIDE B: delete EVERY file in the scratch dir — only under the lock."""
    if not lock.held or Path(lock.directory) != Path(directory):
        raise ScratchRefused("the start sweep runs only while THIS process holds the scratch-dir lock")
    report = SweepReport()
    for entry in sorted(Path(directory).iterdir()):
        if entry.name == LOCK_NAME:
            continue
        if entry.is_dir() and not entry.is_symlink():
            line = DegradedLine(level="red", text=f"voice scratch holds an unexpected directory {entry.name}")
            logger.error("RED {}", line.text)
            report.failed += 1
            report.lines.append(line)
            continue
        r = unlink_scratch(entry, "start sweep — a turn died mid-way")
        if r.ok:
            report.deleted += 1
            logger.warning("AMBER {}", r.line.text)
        else:
            report.failed += 1
        report.lines.append(r.line)
    return report


__all__ = [
    "CONTENT_TYPES", "DirectoryLock", "EXTENSIONS", "HeldAudio", "LOCK_NAME", "ScratchLocked",
    "ScratchRefused", "ScratchUnlinkFailed", "SweepReport", "UnlinkResult", "ensure_dir", "ext_for",
    "start_sweep", "turn_audio", "unlink_scratch", "write_scratch",
]
