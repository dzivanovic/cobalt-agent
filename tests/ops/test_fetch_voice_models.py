"""stt-model-fix-1008 row A — `ops/fetch_voice_models.py`, the one model-fetch command.

Every test is offline: `HF_HUB_OFFLINE=1`, the script's one download call
raises, and the target is a `tmp_path` subdir named by
`COBALT_VOICE_MODEL_DIR`. `COBALT_ENV` is unset in every test: the script
reads no mode, and the unset case is the post-deploy case.
"""

from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import pytest
import yaml

from cobalt.voice import config as vc
from cobalt.voice import transcribe as tr
from cobalt.voice import web

SCRIPT = vc.REPO_ROOT / "ops" / "fetch_voice_models.py"
_VOICE = yaml.safe_load(vc.CONFIG_PATH.read_text())["voice"]
MODEL = _VOICE["stt_model"]
REV = _VOICE["stt_revision"]
REPO_DIR = f"models--Systran--faster-whisper-{MODEL}"
SNAP_FILES = ("model.bin", "config.json", "tokenizer.json", "vocabulary.txt")
SENTINEL = object()


def _load_script():
    spec = importlib.util.spec_from_file_location("fetch_voice_models", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture
def env(tmp_path, monkeypatch):
    target = tmp_path / "target"
    target.mkdir()
    monkeypatch.setenv("COBALT_VOICE_MODEL_DIR", str(target))
    monkeypatch.setenv("HF_HUB_OFFLINE", "1")
    monkeypatch.delenv("COBALT_ENV", raising=False)
    mod = _load_script()
    calls = []

    def no_network(*a, **k):
        calls.append((a, k))
        raise AssertionError("a download was attempted")

    monkeypatch.setattr(mod, "_download", no_network)
    return mod, target, calls


@pytest.fixture
def fake_load(monkeypatch):
    monkeypatch.setattr(tr, "_load_model", lambda cfg: SENTINEL)


def _fake_source(root: Path) -> Path:
    repo = root / REPO_DIR
    (repo / "blobs").mkdir(parents=True)
    (repo / "refs").mkdir()
    (repo / "refs" / "main").write_text(REV)
    snap = repo / "snapshots" / REV
    snap.mkdir(parents=True)
    for i, name in enumerate(SNAP_FILES):
        blob = f"blob{i:040d}"
        (repo / "blobs" / blob).write_bytes(f"constructed {name}".encode())
        os.symlink(f"../../blobs/{blob}", snap / name)
    return root


def _cfg(model_dir: Path):
    return vc.VoiceConfig.model_construct(model_dir=model_dir, stt_model=MODEL, stt_revision=REV,
                                          stt_compute_type=_VOICE["stt_compute_type"])


def test_copy_from_a_local_source_makes_the_model_present(env, fake_load, tmp_path, capsys):
    mod, target, calls = env
    src = _fake_source(tmp_path / "src")
    assert mod.main(["--from", str(src)]) == 0
    out = capsys.readouterr().out.strip().splitlines()
    assert out[-1].startswith(f"voice model READY: {MODEL} {REV} at ")
    assert tr.model_present(_cfg(target.resolve()))
    link = target / REPO_DIR / "snapshots" / REV / "model.bin"
    assert link.is_symlink()
    assert not os.path.isabs(os.readlink(link))
    assert link.resolve().is_relative_to(target.resolve())
    assert calls == []


def test_a_source_without_the_pinned_snapshot_fails_and_writes_nothing(env, fake_load, tmp_path, capsys):
    mod, target, calls = env
    empty = tmp_path / "empty"
    empty.mkdir()
    assert mod.main(["--from", str(empty)]) == 1
    out = capsys.readouterr().out.strip().splitlines()
    assert out[-1].startswith(f"FAILED: the pinned {MODEL} {REV} snapshot is not under ")
    assert not list(target.glob("models--*"))
    assert calls == []


def test_a_present_model_is_left_alone(env, fake_load, tmp_path, capsys):
    mod, target, calls = env
    src = _fake_source(tmp_path / "src")
    assert mod.main(["--from", str(src)]) == 0
    blob = next((target / REPO_DIR / "blobs").iterdir())
    before = blob.stat().st_mtime_ns
    capsys.readouterr()
    assert mod.main(["--from", str(src)]) == 0
    assert capsys.readouterr().out.strip().splitlines()[-1].startswith("voice model READY")
    assert blob.stat().st_mtime_ns == before
    assert calls == []


def test_the_banner_clears_once_the_model_is_copied(env, fake_load, tmp_path, monkeypatch):
    mod, target, _calls = env
    monkeypatch.setattr(web, "_CONFIG", _cfg(target.resolve()))
    monkeypatch.setattr(web, "_SWEEP_LINES", [])
    missing = {"level": "red", "text": "speech-to-text down (model missing)"}
    assert missing in web.status_lines()
    src = _fake_source(tmp_path / "src")
    assert mod.main(["--from", str(src)]) == 0
    assert missing not in web.status_lines()


def test_the_real_pinned_model_copies_and_loads_offline(env, capsys):
    mod, target, calls = env
    src = Path(_VOICE["model_dir"])
    if not tr.model_present(_cfg(src)):
        pytest.skip("speech-to-text model absent from the dev model_dir")
    assert mod.main(["--from", str(src)]) == 0
    assert capsys.readouterr().out.strip().splitlines()[-1].startswith(f"voice model READY: {MODEL} {REV} at ")
    assert tr.model_present(_cfg(target.resolve()))
    for name in SNAP_FILES:
        assert (target / REPO_DIR / "snapshots" / REV / name).resolve().is_relative_to(target.resolve())
    assert calls == []


def test_a_partial_target_folder_fails_and_deletes_nothing(env, fake_load, tmp_path, capsys):
    mod, target, calls = env
    partial = target / REPO_DIR
    (partial / "blobs").mkdir(parents=True)
    (partial / "blobs" / "x").write_bytes(b"constructed partial bytes")
    src = _fake_source(tmp_path / "src")
    assert mod.main(["--from", str(src)]) == 1
    last = capsys.readouterr().out.strip().splitlines()[-1]
    assert last.startswith("FAILED: ")
    assert REPO_DIR in last
    assert (partial / "blobs" / "x").read_bytes() == b"constructed partial bytes"
    assert not (partial / "snapshots").exists()
    assert calls == []


def test_a_target_under_the_repo_is_refused(env, fake_load, tmp_path, monkeypatch, capsys):
    mod, _target, calls = env
    under_docs = vc.REPO_ROOT / "docs" / "voice-models-constructed"
    monkeypatch.setenv("COBALT_VOICE_MODEL_DIR", str(under_docs))
    assert "COBALT_ENV" not in os.environ
    src = _fake_source(tmp_path / "src")
    assert mod.main(["--from", str(src)]) == 1
    assert capsys.readouterr().out.strip().splitlines()[-1].startswith("FAILED: ")
    assert not under_docs.exists()
    assert calls == []
