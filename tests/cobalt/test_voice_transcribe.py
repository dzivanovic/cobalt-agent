"""C5 — the Transcriber (FINAL §2.3; X-E2 chose tiny.en, CPU, int8).

The speech tests SYNTHESIZE their audio at test time — macOS `say` → PyAV →
webm/opus 48 kHz mono (the container E1 is EXPECTED to fix) — into tmp_path.
Nothing audio is committed. They are marked `slow` and skip ONLY when the
pinned model is absent from the dev model_dir (that skip is counted and
named in the build report's CLOSE). `slow` is not a registered marker in
pyproject.toml (only N1 may touch that file in this build) — pytest warns
about it; the mark is still a real, selectable mark.
"""

from __future__ import annotations

import asyncio
import shutil
import subprocess
import threading
import time
from fractions import Fraction
from pathlib import Path

import av
import pytest

from cobalt.voice import config as vc
from cobalt.voice import transcribe as tr

CFG = None


def _cfg():
    global CFG
    if CFG is None:
        CFG = vc.load_voice_config()
    return CFG


@pytest.fixture
def needs_model():
    """Evaluated INSIDE the test, after conftest pins COBALT_ENV=dev — a
    collection-time skipif would read an unset environment as "absent"."""
    if not tr.model_present(_cfg()):
        pytest.skip("speech-to-text model absent from the dev model_dir")


needs_say = pytest.mark.skipif(shutil.which("say") is None, reason="macOS `say` absent")


def synth(tmp_path: Path, text: str, name: str = "clip") -> Path:
    """`say` → AIFF → webm/opus 48 kHz mono, explicit monotonic pts."""
    aiff = tmp_path / f"{name}.aiff"
    subprocess.run(["say", "-v", "Samantha", "-o", str(aiff), text], check=True)
    dst = tmp_path / f"{name}.webm"
    with av.open(str(aiff)) as inp, av.open(str(dst), "w", format="webm") as out:
        st = out.add_stream("libopus", rate=48000)
        st.layout = "mono"
        rs = av.AudioResampler(format="s16", layout="mono", rate=48000, frame_size=st.codec_context.frame_size or 960)
        pts = 0

        def emit(frames):
            nonlocal pts
            for f in frames:
                f.pts, f.time_base = pts, Fraction(1, 48000)
                pts += f.samples
                for p in st.encode(f):
                    out.mux(p)

        for fr in inp.decode(audio=0):
            fr.pts = None
            emit(rs.resample(fr))
        emit(rs.resample(None))
        for p in st.encode(None):
            out.mux(p)
    return dst


@pytest.mark.slow
@needs_say
def test_synthesized_speech_is_transcribed_with_its_fields(tmp_path, needs_model):
    clip = synth(tmp_path, "what are my open cards")
    t = tr.FasterWhisperTranscriber(_cfg()).transcribe(clip)
    assert "open cards" in t.text.lower()
    assert t.engine == "faster-whisper" and t.model == "tiny.en" and t.revision == _cfg().stt_revision
    assert t.language == "en" and 0.5 < t.duration_s < 5
    assert t.stt_ms > 0 and len(t.no_speech_prob) >= 1 and len(t.avg_logprob) == len(t.no_speech_prob)


@pytest.mark.slow
@needs_say
def test_the_same_clip_gives_the_same_text_twice(tmp_path, needs_model):
    clip = synth(tmp_path, "move the stop on X Y Z to four point five zero")
    t = tr.FasterWhisperTranscriber(_cfg())
    assert t.transcribe(clip).text == t.transcribe(clip).text


@pytest.mark.slow
@needs_say
def test_duration_is_probed_before_any_decode(tmp_path):
    clip = synth(tmp_path, "what is on radar")
    d = tr.probe_duration_s(clip)
    assert 0.3 < d < 5


def test_the_configured_revision_reaches_the_model_load(monkeypatch, tmp_path):
    """C6 (voice-v1-check-c-2026-09-24.md FOR THE CLASSIFIER 6; FINAL [F-08]
    pinned model): the configured `stt_revision` is the revision argument of
    the model-load call itself (a captured fake loader), local files only."""
    import faster_whisper

    captured: list[dict] = []

    class FakeWhisperModel:
        def __init__(self, name, **kw):
            captured.append({"name": name, **kw})

        def transcribe(self, path, **kw):
            info = type("I", (), {"language": "en", "duration": 1.0})()
            return iter([]), info

    cfg = _cfg().model_copy(update={"stt_revision": "ab" * 20})
    monkeypatch.setattr(faster_whisper, "WhisperModel", FakeWhisperModel)
    monkeypatch.setattr(tr, "_MODELS", {})
    t = tr.FasterWhisperTranscriber(cfg).transcribe(tmp_path / "never-read.webm")
    assert len(captured) == 1
    assert captured[0]["revision"] == "ab" * 20 and captured[0]["local_files_only"] is True
    assert captured[0]["name"] == cfg.stt_model and t.revision == "ab" * 20


@pytest.mark.slow
def test_a_revision_absent_from_model_dir_is_the_named_red(tmp_path, monkeypatch, needs_model):
    """C6 (b): the model IS present, but a config naming a revision that is
    not in `model_dir` → the named RED `speech-to-text down (model missing)`."""
    cfg = _cfg().model_copy(update={"stt_revision": "f" * 40})
    monkeypatch.setattr(tr, "_MODELS", {})
    assert tr.model_present(cfg) is False
    with pytest.raises(tr.SttDown) as e:
        tr.FasterWhisperTranscriber(cfg).transcribe(tmp_path / "never-read.webm")
    assert e.value.kind == "model_missing"
    assert str(e.value) == "speech-to-text down (model missing)"


def test_a_missing_model_is_a_named_red(tmp_path, monkeypatch):
    empty = tmp_path / "models"
    empty.mkdir()
    monkeypatch.setenv(vc.MODEL_ENV, str(empty))
    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "scratch"))
    cfg = vc.load_voice_config()
    assert tr.model_present(cfg) is False
    with pytest.raises(tr.SttDown) as e:
        tr.FasterWhisperTranscriber(cfg).transcribe(tmp_path / "never-read.webm")
    assert e.value.kind == "model_missing"
    assert str(e.value) == "speech-to-text down (model missing)"


def test_a_file_that_is_not_audio_is_a_named_failure(tmp_path):
    bad = tmp_path / "x.webm"
    bad.write_bytes(b"not audio at all")
    with pytest.raises(tr.SttDown) as e:
        tr.probe_duration_s(bad)
    assert e.value.kind == "undecodable"


class _Slow:
    def __init__(self, secs):
        self.secs = secs

    def transcribe(self, path):
        time.sleep(self.secs)
        return tr.Transcript(text="x", language="en", duration_s=1.0, no_speech_prob=[0.1],
                             avg_logprob=[-0.2], engine="fake", model="fake", revision="0" * 40, stt_ms=1)


def test_the_timeout_is_a_named_red():
    with pytest.raises(tr.SttDown) as e:
        tr.transcribe_with_timeout(_Slow(1.0), Path("/nonexistent"), timeout_s=0.2)
    assert e.value.kind == "timeout"


def test_transcribe_runs_off_the_event_loop():
    async def main():
        ticks = 0

        async def ticker():
            nonlocal ticks
            while True:
                await asyncio.sleep(0.05)
                ticks += 1

        t = asyncio.create_task(ticker())
        out = await tr.transcribe_async(_Slow(0.6), Path("/nonexistent"), timeout_s=5)
        t.cancel()
        return out, ticks

    out, ticks = asyncio.run(main())
    assert out.text == "x" and ticks >= 6


def test_the_transcriber_is_a_protocol_with_one_engine():
    assert isinstance(tr.FasterWhisperTranscriber(_cfg()), tr.Transcriber)
    assert tr.ENGINES == {"faster-whisper": tr.FasterWhisperTranscriber}
