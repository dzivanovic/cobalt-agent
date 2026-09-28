"""C4 — the scratch lifecycle, R2-1 SIDE B (his letter, R56) + the directory lock.

* The upload handler is the directory's ONE writer: `<scratch_dir>/<turn_id>.<ext>`,
  dir 0700 (made by code), file 0600, extension from a CLOSED content-type map.
* ONE `unlink_scratch(path, reason)` for the turn's `finally:` and for the sweep (L3).
* The start sweep deletes EVERY file (no age test), AMBER per file, RED per
  failed unlink — but only while holding the directory lock; a lock held by
  another process (X-X22's orphan) → the sweep deletes NOTHING and the start
  fails loud, naming the holder.
Files here are synthesized bytes in tmp_path; no audio is committed.
"""

from __future__ import annotations

import os
import stat
import subprocess
import sys
import textwrap
import time
from pathlib import Path

import pytest

from cobalt.voice import scratch as sc


@pytest.fixture
def sdir(tmp_path) -> Path:
    return tmp_path / "voice-scratch"


def _mode(p: Path) -> int:
    return stat.S_IMODE(p.stat().st_mode)


# --- the one writer ----------------------------------------------------------


def test_write_creates_the_dir_0700_and_the_file_0600(sdir):
    p = sc.write_scratch(sdir, "turn-abc12345", b"\x1aE\xdf\xa3constructed", "audio/webm;codecs=opus")
    assert p == sdir / "turn-abc12345.webm"
    assert _mode(sdir) == 0o700 and _mode(p) == 0o600
    assert p.read_bytes().startswith(b"\x1aE\xdf\xa3")


@pytest.mark.parametrize("ctype,ext", [("audio/webm", "webm"), ("audio/webm;codecs=opus", "webm"),
                                       ("audio/ogg;codecs=opus", "ogg"), ("audio/mp4", "m4a"),
                                       ("audio/mp4;codecs=mp4a.40.2", "m4a"), ("audio/wav", "wav")])
def test_the_extension_comes_from_the_closed_map(sdir, ctype, ext):
    assert sc.write_scratch(sdir, "turn-0000aaaa", b"x", ctype).suffix == f".{ext}"


@pytest.mark.parametrize("ctype", ["application/octet-stream", "text/plain", "video/webm", "", "audio/flac"])
def test_an_unknown_content_type_fails_named(sdir, ctype):
    with pytest.raises(sc.ScratchRefused) as e:
        sc.write_scratch(sdir, "turn-0000aaaa", b"x", ctype)
    assert "content type" in str(e.value)


@pytest.mark.parametrize("turn_id", ["../escape", "a/b", "", ".lock", "x" * 200, "turn id"])
def test_no_write_lands_anywhere_but_the_scratch_dir(sdir, turn_id):
    with pytest.raises(sc.ScratchRefused):
        sc.write_scratch(sdir, turn_id, b"x", "audio/webm")
    assert not (sdir.parent / "escape.webm").exists()


def test_a_second_write_of_the_same_turn_is_refused(sdir):
    sc.write_scratch(sdir, "turn-0000aaaa", b"x", "audio/webm")
    with pytest.raises(sc.ScratchRefused):
        sc.write_scratch(sdir, "turn-0000aaaa", b"y", "audio/webm")


def test_an_empty_payload_is_refused(sdir):
    with pytest.raises(sc.ScratchRefused):
        sc.write_scratch(sdir, "turn-0000aaaa", b"", "audio/webm")


@pytest.mark.parametrize("mode", ["enospc", "short"])
@pytest.mark.parametrize("via", ["write_scratch", "turn_audio"])
def test_a_failed_write_leaves_no_partial_file(sdir, monkeypatch, mode, via):
    """C1 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 1; FINAL §5 / §7
    scratch RED, L1): a raising or SHORT `os.write` is a named scratch
    error, the partial file is unlinked, and a RED line names the write."""
    import errno

    from loguru import logger

    real_write = os.write

    def fake_write(fd, data):
        if mode == "enospc":
            raise OSError(errno.ENOSPC, "constructed: no space left on device")
        return real_write(fd, bytes(data)[: len(data) - 1])  # short by one byte

    monkeypatch.setattr(os, "write", fake_write)
    lines: list[str] = []
    sink = logger.add(lambda m: lines.append(str(m)), level="ERROR")
    try:
        with pytest.raises(sc.ScratchWriteFailed) as e:
            if via == "write_scratch":
                sc.write_scratch(sdir, "turn-0000aaaa", b"synthesized-bytes", "audio/webm")
            else:
                with sc.turn_audio(sdir, "turn-0000aaaa", b"synthesized-bytes", "audio/webm"):
                    pass
    finally:
        logger.remove(sink)
    assert "write" in str(e.value).lower()
    assert list(sdir.glob("turn-0000aaaa.*")) == []
    assert any("RED" in l and "write" in l.lower() for l in lines), lines


def test_a_too_open_existing_dir_is_tightened_to_0700(sdir):
    sdir.mkdir(mode=0o755)
    os.chmod(sdir, 0o755)
    sc.write_scratch(sdir, "turn-0000aaaa", b"x", "audio/webm")
    assert _mode(sdir) == 0o700


# --- the one unlink -----------------------------------------------------------


def test_unlink_removes_and_reports(sdir):
    p = sc.write_scratch(sdir, "turn-0000aaaa", b"x", "audio/webm")
    r = sc.unlink_scratch(p, "turn_done")
    assert r.ok is True and not p.exists()
    assert "deleted" in r.line.text and "turn_done" in r.line.text


def test_a_failed_unlink_is_red(sdir):
    p = sc.write_scratch(sdir, "turn-0000aaaa", b"x", "audio/webm")
    os.chmod(sdir, 0o500)
    try:
        r = sc.unlink_scratch(p, "turn_done")
    finally:
        os.chmod(sdir, 0o700)
    assert not r.ok and r.line.level == "red" and p.exists()


def test_the_turn_context_unlinks_on_success(sdir):
    with sc.turn_audio(sdir, "turn-0000aaaa", b"x", "audio/webm") as held:
        assert held.path.exists()
    assert not held.path.exists() and held.deleted_at is not None


def test_the_turn_context_unlinks_on_an_exception(sdir):
    with pytest.raises(RuntimeError):
        with sc.turn_audio(sdir, "turn-0000aaaa", b"x", "audio/webm") as held:
            raise RuntimeError("constructed failure between write and transcript")
    assert not held.path.exists() and held.deleted_at is not None


def test_the_turn_context_fails_loud_when_its_unlink_fails(sdir):
    with pytest.raises(sc.ScratchUnlinkFailed):
        with sc.turn_audio(sdir, "turn-0000aaaa", b"x", "audio/webm") as held:
            os.chmod(sdir, 0o500)
    os.chmod(sdir, 0o700)
    assert held.path.exists() and held.deleted_at is None  # never silently left: it raised


def test_a_file_already_gone_keeps_its_amber_line(sdir):
    """C4 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 4; FINAL §5 "AMBER
    line per file"): the unlink finds no file → `deleted_at` is set AND the
    AMBER `already gone` line is kept on the held audio."""
    sdir.mkdir(mode=0o700)
    held = sc.HeldAudio(path=sdir / "turn-gone0001.webm", size=1)
    held.unlink_now("turn finally")
    assert held.deleted_at is not None
    assert [(l.level, "already gone" in l.text) for l in held.lines] == [("amber", True)]


def test_the_turn_context_early_unlink_is_idempotent(sdir):
    with sc.turn_audio(sdir, "turn-0000aaaa", b"x", "audio/webm") as held:
        held.unlink_now("transcribed")
        assert not held.path.exists()
    assert held.deleted_at is not None


# --- the start sweep: side B, behind the directory lock --------------------------


def _leftovers(sdir: Path, n: int = 3) -> list[Path]:
    return [sc.write_scratch(sdir, f"turn-left{i:04d}", b"synthesized-bytes", "audio/webm") for i in range(n)]


def test_the_start_sweep_deletes_every_file_with_an_amber_line_each(sdir):
    files = _leftovers(sdir)
    lock = sc.DirectoryLock(sdir)
    try:
        report = sc.start_sweep(sdir, lock)
        assert [p.exists() for p in files] == [False] * 3
        assert [l.level for l in report.lines] == ["amber"] * 3
        assert report.deleted == 3 and report.failed == 0
        assert (sdir / sc.LOCK_NAME).exists()  # the lock file is not audio; never swept
    finally:
        lock.release()


def test_the_sweep_has_no_age_test(sdir):
    files = _leftovers(sdir, 1)
    now = time.time()
    os.utime(files[0], (now, now))  # brand new — side B deletes it anyway
    lock = sc.DirectoryLock(sdir)
    try:
        assert sc.start_sweep(sdir, lock).deleted == 1
    finally:
        lock.release()


def test_a_failed_sweep_unlink_is_red(sdir):
    _leftovers(sdir, 1)
    lock = sc.DirectoryLock(sdir)
    os.chmod(sdir, 0o500)
    try:
        report = sc.start_sweep(sdir, lock)
    finally:
        os.chmod(sdir, 0o700)
        lock.release()
    assert report.failed == 1 and report.lines[0].level == "red"


def _hold_lock_in_child(sdir: Path):
    code = textwrap.dedent(f"""
        import fcntl, os, sys, time
        fd = os.open({str(sdir / sc.LOCK_NAME)!r}, os.O_CREAT | os.O_RDWR, 0o600)
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.ftruncate(fd, 0); os.write(fd, str(os.getpid()).encode())
        print("HELD", flush=True)
        time.sleep(30)
    """)
    p = subprocess.Popen([sys.executable, "-c", code], stdout=subprocess.PIPE, text=True)
    assert p.stdout.readline().strip() == "HELD"
    return p


def test_a_lock_held_by_another_process_deletes_nothing_and_fails_loud_naming_it(sdir):
    files = _leftovers(sdir)
    holder = _hold_lock_in_child(sdir)
    try:
        with pytest.raises(sc.ScratchLocked) as e:
            lock = sc.DirectoryLock(sdir)
            sc.start_sweep(sdir, lock)
        assert str(holder.pid) in str(e.value)
        assert e.value.holder_pid == holder.pid
        assert all(p.exists() for p in files), "a held lock must delete NOTHING"
    finally:
        holder.kill()  # the child THIS test started, by the pid it holds
        holder.wait()


def test_the_lock_is_exclusive_within_one_process_too(sdir):
    a = sc.DirectoryLock(sdir)
    try:
        with pytest.raises(sc.ScratchLocked):
            sc.DirectoryLock(sdir)
    finally:
        a.release()
    b = sc.DirectoryLock(sdir)  # released → takeable again
    b.release()


def test_the_lock_names_its_own_pid(sdir):
    lock = sc.DirectoryLock(sdir)
    try:
        assert (sdir / sc.LOCK_NAME).read_text().strip() == str(os.getpid())
        assert _mode(sdir / sc.LOCK_NAME) == 0o600
    finally:
        lock.release()


def test_the_sweep_refuses_without_the_lock(sdir):
    _leftovers(sdir, 1)
    lock = sc.DirectoryLock(sdir)
    lock.release()
    with pytest.raises(sc.ScratchRefused):
        sc.start_sweep(sdir, lock)


def test_one_unlink_function_serves_turn_and_sweep():
    import inspect

    src = inspect.getsource(sc)
    assert src.count("os.unlink(") == 1, "L3: exactly one unlink call in the voice scratch module"


def test_one_deleter_across_every_voice_module():
    """C7 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 7; L3): every
    deleter spelling (`os.unlink(`, `os.remove(`, `.unlink(`,
    `shutil.rmtree(`) across EVERY src/cobalt/voice/*.py → exactly ONE, in
    scratch.py's `unlink_scratch`."""
    import inspect
    import re

    deleter = re.compile(r"os\.remove\(|shutil\.rmtree\(|\.unlink\(")  # `.unlink(` covers `os.unlink(`
    voice_dir = Path(sc.__file__).parent
    hits = {p.name: len(deleter.findall(p.read_text())) for p in sorted(voice_dir.glob("*.py"))}
    assert sum(hits.values()) == 1, hits
    assert hits["scratch.py"] == 1, hits
    assert len(deleter.findall(inspect.getsource(sc.unlink_scratch))) == 1
