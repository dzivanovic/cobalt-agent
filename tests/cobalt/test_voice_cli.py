"""C13 — `cobalt voice turn --audio <file> | --text "<text>" [--confirm <turn_id>] [--dry-run]`.

The CLI is the turn function's third caller ([F-01]). `--dry-run` prints
the Plan, the resolution and the exact change and writes nothing.
`--confirm <turn_id>` is REFUSED when COBALT_ENV=production (FINAL [F-02];
L37 — no house confirms a production act). `--audio` takes the scratch-dir
lock for its turn and refuses, named, when a server holds it.
"""

from __future__ import annotations

import argparse
import inspect
import json

import pytest

from cobalt.voice import cli as vcli
from cobalt.voice import config as vc
from cobalt.voice import scratch as sc
from cobalt.voice.models import TurnOutcome, TurnState


def _parse(argv):
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    vcli.add_parser(sub)
    return p.parse_args(argv)


@pytest.fixture
def recorded(tmp_path, monkeypatch):
    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "scratch"))
    monkeypatch.setenv(vc.MODEL_ENV, str(tmp_path / "models"))
    calls = []

    def fake(inp, deps):
        calls.append(inp)
        return TurnOutcome(turn_id="turn-cli", state=TurnState.DONE, reply="constructed reply",
                           dry_run={"plan": {"kind": "answer"}, "resolution": {}, "change": None} if inp.dry_run else None)

    monkeypatch.setattr(vcli, "run_turn", fake)
    monkeypatch.setattr(vcli, "default_deps", lambda: object())
    return calls


def test_the_cli_calls_the_one_turn_function(recorded):
    """D10 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 10): behavioural —
    the `run_turn` name the CLI uses is called once, with the CLI's source."""
    assert "run_turn(" in inspect.getsource(vcli)
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "what are my open cards"]))
    assert len(recorded) == 1 and recorded[0].source == "cli"


def test_a_text_turn(recorded, capsys):
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "what are my open cards"]))
    assert recorded[0].text == "what are my open cards" and recorded[0].source == "cli"
    assert "constructed reply" in capsys.readouterr().out


def test_dry_run_prints_the_plan_and_the_change(recorded, capsys):
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "move the stop on XYZ to 4.50", "--dry-run"]))
    assert recorded[0].dry_run is True
    out = capsys.readouterr().out
    assert '"plan"' in out and '"change"' in out


def test_confirm_is_refused_in_production(recorded, monkeypatch, capsys):
    monkeypatch.setenv("COBALT_ENV", "production")
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--confirm", "turn-abc"]))
    assert e.value.code != 0 and recorded == []
    # D9 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 9): the refusal's text
    assert "FAILED: --confirm is refused in production" in capsys.readouterr().err


def test_confirm_with_dry_run_is_refused_at_parse(recorded, capsys):
    """D2 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 2; FINAL :188
    [F-02] "`--dry-run` … with no write"): a confirm is a write — the pair is
    refused, named, before any turn runs."""
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--confirm", "turn-abc", "--dry-run"]))
    assert e.value.code != 0 and recorded == []
    err = capsys.readouterr().err
    assert "--confirm" in err and "--dry-run" in err


# --- the real turn function with in-memory deps (the turn tests' own fakes) -----------------


@pytest.fixture
def mem(tmp_path, monkeypatch):
    from test_voice_turn import AGENT, CARDS, NOW, STOP_ACT, FakePlanner, FakeTranscriber, MemStore

    from cobalt.voice import turn as tn

    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "scratch"))
    monkeypatch.setenv(vc.MODEL_ENV, str(tmp_path / "models"))
    cfg = vc.load_voice_config()
    executed = []

    def execute(p):
        executed.append(p)
        return type("E", (), {"stop_edit_id": 777})()

    d = tn.TurnDeps(cfg=cfg, agent=AGENT, store=MemStore(), transcriber=FakeTranscriber(),
                    plan=FakePlanner({"move the stop on XYZ to 4.50": STOP_ACT}), read_cards=lambda: list(CARDS),
                    read_pool=lambda: {"pool": {"current": [], "stale": False}},
                    execute=execute, now=lambda: NOW, plan_timeout_s=15, probe_duration=lambda p: 1.2)
    d.executed = executed
    monkeypatch.setattr(vcli, "default_deps", lambda: d)
    return d


def _pending_via_cli(mem) -> str:
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "move the stop on XYZ to 4.50"]))
    (tid,) = [t for t, r in mem.store.rows.items() if r["state"] == "awaiting_confirm"]
    return tid


def test_a_cli_yes_never_confirms_a_production_act(mem, monkeypatch, capsys):
    """D1 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 1; FINAL :188
    [F-02] "in production an ACT is confirmed only by the widget … No house,
    the desk included, confirms a production act (L37)")."""
    monkeypatch.setenv("COBALT_ENV", "production")
    tid = _pending_via_cli(mem)
    capsys.readouterr()
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--text", "yes"]))
    assert e.value.code != 0
    assert mem.executed == [], "execute is never called"
    assert mem.store.get(tid)["state"] == "awaiting_confirm", "the pending act is left for the widget"
    out = capsys.readouterr().out
    assert "[F-02]" in out and "RED:" in out
    (refused,) = [r for r in mem.store.rows.values() if r.get("failure_class") == "cli_confirm_refused"]
    assert refused["state"] == "failed"


def test_a_cli_yes_still_confirms_in_dev(mem, monkeypatch):
    """D1's control: under COBALT_ENV=dev the same pair confirms."""
    monkeypatch.setenv("COBALT_ENV", "dev")
    tid = _pending_via_cli(mem)
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "yes"]))
    assert len(mem.executed) == 1 and mem.store.get(tid)["state"] == "done"


def test_a_failed_act_exits_non_zero_with_its_red_line(mem, monkeypatch, capsys):
    """D5 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 5; FINAL §7, L1):
    a confirm whose act fails exits NON-ZERO and prints the RED line."""
    monkeypatch.setenv("COBALT_ENV", "dev")
    tid = _pending_via_cli(mem)

    def boom(p):
        raise RuntimeError("constructed failure inside the act")

    mem.execute = boom
    capsys.readouterr()
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--confirm", tid]))
    assert e.value.code != 0
    assert "RED:" in capsys.readouterr().out


def test_an_expert_refusal_exits_non_zero_with_a_red_line(mem, monkeypatch, capsys):
    """D5: the expert refuses the act → non-zero, RED printed."""
    from cobalt.cards import CardStateError

    monkeypatch.setenv("COBALT_ENV", "dev")
    _pending_via_cli(mem)

    def refuse(p):
        raise CardStateError("REFUSED: constructed — the stop is not editable")

    mem.execute = refuse
    capsys.readouterr()
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--text", "yes"]))
    assert e.value.code != 0
    assert "RED:" in capsys.readouterr().out


def test_confirm_in_dev_is_a_tap(recorded):
    vcli.cmd_turn(_parse(["voice", "turn", "--confirm", "turn-abc", "--session", "cli-sess"]))
    assert recorded[0].tap == "confirm" and recorded[0].pending_turn_id == "turn-abc"


def test_audio_takes_the_lock_and_refuses_when_a_server_holds_it(recorded, tmp_path):
    clip = tmp_path / "clip.webm"
    clip.write_bytes(b"\x1aE\xdf\xa3synthesized")
    cfg = vc.load_voice_config()
    held = sc.DirectoryLock(cfg.scratch_dir)
    try:
        with pytest.raises(SystemExit) as e:
            vcli.cmd_turn(_parse(["voice", "turn", "--audio", str(clip)]))
        assert e.value.code != 0 and recorded == []
    finally:
        held.release()
    vcli.cmd_turn(_parse(["voice", "turn", "--audio", str(clip)]))
    assert recorded[0].audio == clip.read_bytes() and recorded[0].content_type == "audio/webm"
    sc.DirectoryLock(cfg.scratch_dir).release()  # the CLI released it


def test_an_unknown_audio_extension_is_refused(recorded, tmp_path):
    clip = tmp_path / "clip.flac"
    clip.write_bytes(b"x")
    with pytest.raises(SystemExit):
        vcli.cmd_turn(_parse(["voice", "turn", "--audio", str(clip)]))


def test_the_cli_is_registered_on_the_cobalt_command():
    import cobalt.cli as root

    src = inspect.getsource(root)
    assert "from cobalt.voice import cli as voice_cli" in src and "voice_cli.add_parser(sub)" in src
