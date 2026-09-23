"""C13 — X-E7: the lifecycle under a crash (FINAL `## First-gate experiments` E7).

(c) grok's case, IN PROCESS: a crash after the expert's write committed and
    before the row reached `done` (an exception injected at exactly that
    point) → the row stays `executing` → the reaper fails it → the stop was
    applied ONCE and is never applied again (a second confirm finds no
    pending action).
(a) + (b), WITH-DB, a REAL server this test starts: `kill -9` of the dev
    ASET server (the pid this test holds) mid-turn, LESS than
    `scratch_max_age_s` after the upload, no later turn → the audio file is
    still on disk after the kill → a second server process starts → its
    start sweep deletes it (side B deletes EVERY file; an age-gated sweep
    would have kept it) → the row, past its limit, is reaped `failed`.
The audio is synthesized at test time (`say` → PyAV); nothing is committed.
"""

from __future__ import annotations

import os
import shutil
import signal
import socket
import subprocess
import sys
import time
import uuid
from datetime import timedelta
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.voice import confirm as cf
from cobalt.voice import tools as tl
from cobalt.voice.models import TurnState
from cobalt.voice.store import reap_limits

from test_voice_confirm import CARD, NOW, MemStore

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


# --- (c) grok's case ---------------------------------------------------------------------------


class CrashBeforeDone(MemStore):
    def transition(self, turn_id, expected, new, *, at, **fields):
        if new is TurnState.DONE:
            raise RuntimeError("constructed crash: the process died after the expert committed")
        return super().transition(turn_id, expected, new, at=at, **fields)

    def reap(self, *, now, limits):
        out = []
        for tid, row in self.rows.items():
            if row["state"] == "executing":
                row.update(state="failed", failure_class="reaped_executing")
                out.append((tid, "executing"))
        return out


def test_a_crash_after_the_write_is_reaped_and_never_applied_again():
    s = CrashBeforeDone()
    p = tl.stop_dry_run(CARD, Decimal("4.50"), ttl_s=60, now=NOW)
    s.put("t-pending", TurnState.AWAITING_CONFIRM, pending_action=p.model_dump(mode="json"))
    writes = []

    def execute(pending):
        writes.append((pending.card_id, pending.to_stop))  # the expert committed
        return type("E", (), {"stop_edit_id": 9})()

    with pytest.raises(RuntimeError):
        cf.confirm_pending(s, s.get("t-pending"), now=NOW, execute=execute)
    assert s.get("t-pending")["state"] == "executing"
    assert s.reap(now=NOW + timedelta(hours=1), limits=reap_limits(stt_timeout_s=20, plan_timeout_s=15)) == [
        ("t-pending", "executing")]
    again = cf.confirm_pending(s, s.get("t-pending"), now=NOW, execute=execute)
    assert again.kind == "no_pending"
    assert writes == [(11, "4.50")], "the stop was applied once and never again"


# --- (a) + (b): a real server, killed -9 mid-turn, then restarted --------------------------------


def _free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _serve(port: int, scratch: Path) -> subprocess.Popen:
    env = dict(os.environ, COBALT_ENV="dev", COBALT_VOICE_SCRATCH_DIR=str(scratch))
    return subprocess.Popen([sys.executable, "-m", "uvicorn", "cobalt.aset.web:app", "--host", "127.0.0.1",
                             "--port", str(port), "--log-level", "warning"], env=env,
                            stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def _wait_up(port: int, proc: subprocess.Popen, secs: float = 60) -> None:
    import httpx

    end = time.time() + secs
    while time.time() < end:
        if proc.poll() is not None:
            raise AssertionError(f"server exited rc={proc.returncode}: {proc.stderr.read()[-800:]!r}")
        try:
            if httpx.get(f"http://127.0.0.1:{port}/voice/status", timeout=2).status_code == 200:
                return
        except httpx.HTTPError:
            pass
        time.sleep(0.3)
    raise AssertionError("server did not come up")


def _synth_long(tmp: Path) -> bytes:
    from test_voice_transcribe import synth

    text = " ".join(["what are my open cards and what is on radar right now"] * 5)
    return synth(tmp, text, name="e7").read_bytes()


@pytest.mark.slow
@requires_db
@pytest.mark.skipif(shutil.which("say") is None, reason="macOS `say` absent")
def test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped(tmp_path):
    import threading

    import httpx

    from cobalt.voice.store import VoiceTurnStore

    scratch = tmp_path / "scratch"
    audio = _synth_long(tmp_path)
    session = f"sess-e7-{uuid.uuid4().hex[:8]}"
    port = _free_port()
    first = _serve(port, scratch)
    second = None
    store = VoiceTurnStore(connect=lambda: _raw_connect())
    try:
        _wait_up(port, first)

        def post():
            try:
                httpx.post(f"http://127.0.0.1:{port}/voice/turn", data={"session": session},
                           files={"audio": ("clip.webm", audio, "audio/webm;codecs=opus")}, timeout=120)
            except httpx.HTTPError:
                pass  # the server is killed under it — expected

        th = threading.Thread(target=post, daemon=True)
        th.start()
        end = time.time() + 30
        while time.time() < end and not [p for p in scratch.glob("turn-*")]:
            time.sleep(0.02)
        files = [p for p in scratch.glob("turn-*")]
        assert files, "the upload never reached the scratch dir"
        first.send_signal(signal.SIGKILL)  # the pid THIS test started
        first.wait(timeout=10)
        assert files[0].exists(), "(b) the killed turn's audio is still on disk before the restart"
        second = _serve(port, scratch)
        _wait_up(port, second)
        assert not files[0].exists(), "(b) side B's start sweep deletes the leftover, whatever its age"
        assert [p.name for p in scratch.iterdir()] == [".lock"]
        rows = [r for r in _rows(store, session)]
        assert len(rows) == 1 and rows[0]["state"] in ("received", "transcribing", "planned", "failed")
        from datetime import datetime, timezone

        # The server stamped its row with the REAL clock; the suite freezes
        # `session.clock.now_utc` at 2026-09-03, so the reap uses real time.
        store.reap(now=datetime.now(timezone.utc) + timedelta(minutes=10),
                   limits=reap_limits(stt_timeout_s=20, plan_timeout_s=15))
        row = store.get(rows[0]["turn_id"])
        assert row["state"] == "failed", row["state"]
        if row["failure_class"] is not None and row["failure_class"].startswith("reaped_"):
            assert row["failed_at"] is not None
    finally:
        for p in (first, second):
            if p is not None and p.poll() is None:
                p.send_signal(signal.SIGKILL)
                p.wait(timeout=10)
        store.delete_test_rows(session)


def _raw_connect():
    from cobalt import env
    from cobalt.db import Side

    return _RAW(env.DEV_DB_NAME, side=Side.USER)


def _rows(store, session):
    with store._connect() as conn:
        cur = conn.execute("SELECT turn_id, state FROM voice_turns WHERE session_id = %s", (session,))
        return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]


from cobalt import db as _db  # noqa: E402

_RAW = _db.connect  # unpatched: bound at import, before the suite's fixture replaces it
