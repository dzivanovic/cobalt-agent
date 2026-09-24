"""Voice V1 fix round 1 — the RUNS (L70): each UNPROVEN row of the
classification (`reports/voice-v1-fix-r1-draft-2026-09-24.md`, U2 U5 U6 U8
U9) as a cheap run whose output the build report quotes. A RUN that is red
on the fix commit is a RESULT for round 2, kept here as a strict xfail and
never fixed in fix r1 (L70 / L75). Constructed values only (L32).
"""

from __future__ import annotations

import argparse
import tempfile
from datetime import datetime, timezone
from decimal import Decimal

import pytest
from fastapi.testclient import TestClient

from cobalt.voice import agent as ag
from cobalt.voice import cli as vcli
from cobalt.voice import config as vc
from cobalt.voice import tools as tl
from cobalt.voice import turn as tn
from cobalt.voice.models import Plan, TurnState

from test_voice_turn import AGENT, CARDS, NOW, FakePlanner, FakeTranscriber, MemStore


@pytest.fixture
def deps(tmp_path, monkeypatch):
    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "scratch"))
    monkeypatch.setenv(vc.MODEL_ENV, str(tmp_path / "models"))
    cfg = vc.load_voice_config()
    executed = []

    def execute(p):
        executed.append(p)
        return type("E", (), {"stop_edit_id": 777})()

    d = tn.TurnDeps(cfg=cfg, agent=AGENT, store=MemStore(), transcriber=FakeTranscriber(),
                    plan=FakePlanner(), read_cards=lambda: list(CARDS),
                    read_pool=lambda: {"pool": {"current": [], "stale": False}},
                    execute=execute, now=lambda: NOW, plan_timeout_s=15, probe_duration=lambda p: 1.2)
    d.executed = executed
    return d


# --- RUN-2: the card is read twice ----------------------------------------------------------


@pytest.mark.xfail(strict=True, reason="RUN-2 red on a1f8404a — a round-2 finding, not fixed in fix r1 (L70/L75)")
def test_run2_a_stop_moved_between_the_two_reads_is_refused(monkeypatch):
    """RUN-2 (voice-v1-check-a-2026-09-24.md row 7, A4, NOT CHECKABLE FROM
    READS): `execute_stop` reads the card (tools.py `read_open_cards`), then
    `set_card_stop` reads it again (card_stop.py:43). A stop moved between
    the two reads must REFUSE the act (`TargetChanged`) with no stop edit."""
    from cobalt.aset import web as web_module

    reads = {"n": 0}
    edits = []

    class TwoReads:
        def __init__(self, db_name=None):
            pass

        def ensure_schema(self):
            pass

        def open_cards(self):
            reads["n"] += 1
            stop = Decimal("4.4000") if reads["n"] == 1 else Decimal("4.4200")  # moved after the first read
            return [{"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "stop": stop,
                     "entry": Decimal("4.6000"), "shares": 250, "grade": "B"}]

        def record_stop_edit(self, card_id, *, from_stop, to_stop):
            edits.append((card_id, from_stop, to_stop))
            return 601

    monkeypatch.setattr(web_module, "CardStore", TwoReads)
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    card = {"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "stop": Decimal("4.4000")}
    pending = tl.stop_dry_run(card, Decimal("4.50"), ttl_s=60, now=datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc))
    with pytest.raises(tl.TargetChanged):
        tl.execute_stop(pending)
    assert edits == [], f"a stop edit was recorded over a moved stop: {edits}"


# --- RUN-4b: kind dispatch ------------------------------------------------------------------


@pytest.mark.parametrize("kind,reply", [
    ("refuse", tl.REFUSE_SENTENCE), ("clarify", tn.CLARIFY_TEMPLATE), ("unsupported", tl.UNSUPPORTED_SENTENCE),
])
def test_run4b_a_non_act_plan_carrying_a_tool_executes_nothing(deps, kind, reply):
    """RUN-4b (voice-v1-check-b-2026-09-24.md row 5, carried to D): a Plan of
    kind refuse / clarify / unsupported that STILL carries a tool and args →
    no tool executed, no pending action, answered by kind."""
    text = "move the stop on QRS to 12.25"
    deps.plan = FakePlanner({text: Plan(kind=kind, tool="cards.set_stop",
                                        args={"card": {"span": "QRS"}, "stop": {"span": "12.25"}})})
    out = tn.run_turn(tn.TurnInput(session_id="sess-run4b", source="test", text=text), deps)
    assert deps.executed == [] and out.pending_turn_id is None
    assert out.reply == reply
    assert deps.store.pending_for_session("sess-run4b") is None


# --- RUN-4c: an untyped error inside plan_turn -------------------------------------------------


@pytest.mark.xfail(strict=True, reason="RUN-4c red on a1f8404a — a round-2 finding, not fixed in fix r1 (L70/L75)")
def test_run4c_an_untyped_plan_error_fails_loud_named(deps, monkeypatch):
    """RUN-4c (voice-v1-check-b-2026-09-24.md row 6, carried to D): a
    `ValueError` (config / budget) raised inside `plan_turn` → the turn FAILS
    loud with the `Cobalt can't think right now (<class>)` RED and a
    `failed` row — never an unhandled exception out of `run_turn`."""

    def budget_refusal(req, config=None):
        raise ValueError("constructed budget refusal")

    monkeypatch.setattr(ag, "call_sync", budget_refusal)
    deps.plan = ag.plan_turn
    out = tn.run_turn(tn.TurnInput(session_id="sess-run4c", source="test", text="what are my open cards"), deps)
    assert out.state is TurnState.FAILED
    assert deps.store.get(out.turn_id)["state"] == "failed"
    assert out.reply == "Cobalt can't think right now (ValueError)."
    assert any(l.level == "red" and l.text == out.reply for l in out.degraded)


# --- RUN-6: where Starlette spools a large upload -------------------------------------------------


def test_run6_a_large_upload_leaves_nothing_in_the_temp_dir(deps, tmp_path, monkeypatch):
    """RUN-6 (voice-v1-check-c-2026-09-24.md row 19, NOT CHECKABLE FROM
    READS): with `tempfile.tempdir` pointed at a tmp_path subfolder, a
    loopback POST of a 1.5 MB constructed audio body to `/voice/turn`
    (transcriber faked) — list the subfolder after the request. Anything
    listed = the upload was spooled outside `scratch_dir` and left there."""
    from cobalt.aset import web as aset_web
    from cobalt.voice import web as vw

    spool = tmp_path / "spool"
    spool.mkdir()
    monkeypatch.setattr(tempfile, "tempdir", str(spool))
    monkeypatch.setattr(vw, "get_config", lambda: deps.cfg)
    monkeypatch.setattr(vw, "get_deps", lambda: deps)
    body = b"\x1aE\xdf\xa3" + b"\x00" * (1_500_000 - 4)
    r = TestClient(aset_web.app, client=("127.0.0.1", 51000)).post(
        "/voice/turn", data={"session": "sess-run6"}, files={"audio": ("clip.webm", body, "audio/webm")})
    assert r.status_code == 200, r.text
    left = sorted(p.name for p in spool.iterdir())
    assert left == [], f"left in the spool dir after the request: {left}"
    assert [p for p in deps.cfg.scratch_dir.glob("*") if p.name != ".lock"] == []


# --- RUN-7: the CLI's --audio bounds ----------------------------------------------------------------


def _parse(argv):
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    vcli.add_parser(sub)
    return p.parse_args(argv)


@pytest.mark.parametrize("size", [
    "zero",
    pytest.param("over_max_upload_bytes", marks=pytest.mark.xfail(
        strict=True, reason="RUN-7 red on a1f8404a — a round-2 finding, not fixed in fix r1 (L70/L75)")),
])
def test_run7_cli_audio_zero_byte_and_oversize_are_refused(deps, tmp_path, monkeypatch, capsys, size):
    """RUN-7 (voice-v1-check-d-2026-09-24.md row 14; FINAL [F-19]): the CLI
    `--audio` with a zero-byte file and with a file over `max_upload_bytes`
    → a named refusal each, non-zero exit, no scratch file left."""
    monkeypatch.setattr(vcli, "default_deps", lambda: deps)
    clip = tmp_path / "clip.webm"
    clip.write_bytes(b"" if size == "zero" else b"\x1aE\xdf\xa3" + b"\x00" * deps.cfg.max_upload_bytes)
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--audio", str(clip)]))
    assert e.value.code != 0
    out = capsys.readouterr()
    assert ("zero-byte" if size == "zero" else "exceeds") in (out.out + out.err)
    assert [p for p in deps.cfg.scratch_dir.glob("*") if p.name != ".lock"] == []
