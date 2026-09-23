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


def test_the_cli_calls_the_one_turn_function():
    assert "run_turn(" in inspect.getsource(vcli)


def test_a_text_turn(recorded, capsys):
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "what are my open cards"]))
    assert recorded[0].text == "what are my open cards" and recorded[0].source == "cli"
    assert "constructed reply" in capsys.readouterr().out


def test_dry_run_prints_the_plan_and_the_change(recorded, capsys):
    vcli.cmd_turn(_parse(["voice", "turn", "--text", "move the stop on XYZ to 4.50", "--dry-run"]))
    assert recorded[0].dry_run is True
    out = capsys.readouterr().out
    assert '"plan"' in out and '"change"' in out


def test_confirm_is_refused_in_production(recorded, monkeypatch):
    monkeypatch.setenv("COBALT_ENV", "production")
    with pytest.raises(SystemExit) as e:
        vcli.cmd_turn(_parse(["voice", "turn", "--confirm", "turn-abc"]))
    assert e.value.code != 0 and recorded == []


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
