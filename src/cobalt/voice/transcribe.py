"""Local speech-to-text: the `Transcriber` protocol and its one engine,
`FasterWhisperTranscriber` (FINAL §2.3; v2 [F-03], [F-08]).

CPU faster-whisper with the size, pinned revision and compute type X-E2
chose (`configs/cobalt/voice.yaml`), loaded from `model_dir` with
`local_files_only=True` — never a download at run time; a missing model
is the named RED `speech-to-text down (model missing)`. No cloud engine
exists (W4, L23): there is nothing to fall back to, the text box works.

OFF THE LOOP (FINAL §2.3 / [F-04]): the route awaits `transcribe_async`,
which runs the decode in a worker thread under `stt_timeout_s`. A timeout
fails the turn by name; the decode thread cannot be killed and finishes on
its own (the file it reads was already unlinked by the turn's `finally:`
— X-X20 measured that a decode survives its file's unlink).

The model object is loaded ONCE per process (per model / revision /
compute type / directory) and shared; loading is serialized.
"""

from __future__ import annotations

import asyncio
import concurrent.futures
import threading
import time
from pathlib import Path
from typing import Protocol, runtime_checkable

from pydantic import BaseModel, ConfigDict

from .config import VoiceConfig

_HUMAN = {
    "model_missing": "model missing",
    "timeout": "timeout",
    "undecodable": "audio undecodable",
    "engine_error": "engine error",
}


class SttDown(RuntimeError):
    """Speech-to-text failed. `str()` is the widget's RED line."""

    def __init__(self, kind: str, detail: str = ""):
        self.kind = kind
        self.detail = detail
        super().__init__(f"speech-to-text down ({_HUMAN.get(kind, kind)})")


class Transcript(BaseModel):
    """What the engine returned, AS RETURNED (the stored inputs, L57)."""

    model_config = ConfigDict(extra="forbid")

    text: str
    language: str
    duration_s: float
    no_speech_prob: list[float]
    avg_logprob: list[float]
    engine: str
    model: str
    revision: str
    stt_ms: int


@runtime_checkable
class Transcriber(Protocol):
    def transcribe(self, path: Path) -> Transcript: ...


_MODELS: dict[tuple, object] = {}
_LOAD = threading.Lock()


def _load_model(cfg: VoiceConfig):
    key = (str(cfg.model_dir), cfg.stt_model, cfg.stt_revision, cfg.stt_compute_type)
    with _LOAD:
        if key in _MODELS:
            return _MODELS[key]
        try:
            from faster_whisper import WhisperModel

            model = WhisperModel(cfg.stt_model, device="cpu", compute_type=cfg.stt_compute_type,
                                 download_root=str(cfg.model_dir), local_files_only=True,
                                 revision=cfg.stt_revision)
        except Exception as e:  # noqa: BLE001 - classified below
            name = type(e).__name__
            if "LocalEntryNotFound" in name or "NotFound" in name or isinstance(e, (FileNotFoundError, OSError)):
                raise SttDown("model_missing", name) from None
            raise SttDown("engine_error", name) from None
        _MODELS[key] = model
        return model


def model_present(cfg: VoiceConfig) -> bool:
    """Is the pinned model on disk? Local lookup only — never a download."""
    try:
        from faster_whisper.utils import download_model

        path = Path(download_model(cfg.stt_model, local_files_only=True, cache_dir=str(cfg.model_dir),
                                   revision=cfg.stt_revision))
    except Exception:  # noqa: BLE001 - absent is the answer
        return False
    return (path / "model.bin").exists()


def probe_duration_s(path: Path) -> float:
    """The clip's length from its container, before any decode (max_clip_s)."""
    try:
        import av

        with av.open(str(path)) as c:
            if c.duration:
                return c.duration / 1_000_000
            s = c.streams.audio[0]
            if s.duration and s.time_base:
                return float(s.duration * s.time_base)
            total = 0
            rate = s.rate or 48000
            for frame in c.decode(audio=0):
                total += frame.samples
            return total / rate
    except SttDown:
        raise
    except Exception as e:  # noqa: BLE001 - any container error is one named failure
        raise SttDown("undecodable", type(e).__name__) from None


class FasterWhisperTranscriber:
    engine = "faster-whisper"

    def __init__(self, cfg: VoiceConfig):
        self.cfg = cfg

    def transcribe(self, path: Path) -> Transcript:
        model = _load_model(self.cfg)
        t0 = time.perf_counter()
        try:
            segments, info = model.transcribe(str(path), language="en", beam_size=5, vad_filter=False,
                                              condition_on_previous_text=False)
            segments = list(segments)
        except SttDown:
            raise
        except Exception as e:  # noqa: BLE001
            name = type(e).__name__
            kind = "undecodable" if ("av." in type(e).__module__ or "InvalidData" in name) else "engine_error"
            raise SttDown(kind, name) from None
        return Transcript(
            text=" ".join(s.text.strip() for s in segments).strip(),
            language=info.language,
            duration_s=float(info.duration),
            no_speech_prob=[float(s.no_speech_prob) for s in segments],
            avg_logprob=[float(s.avg_logprob) for s in segments],
            engine=self.engine,
            model=self.cfg.stt_model,
            revision=self.cfg.stt_revision,
            stt_ms=max(1, int((time.perf_counter() - t0) * 1000)),
        )


#: ONE engine chosen by config (`stt_engine`); a second is a config value
#: and a class here, by measurement (FINAL §2.3).
ENGINES = {"faster-whisper": FasterWhisperTranscriber}


def make_transcriber(cfg: VoiceConfig) -> Transcriber:
    return ENGINES[cfg.stt_engine](cfg)


def transcribe_with_timeout(transcriber: Transcriber, path: Path, *, timeout_s: float) -> Transcript:
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=1, thread_name_prefix="voice-stt")
    try:
        fut = pool.submit(transcriber.transcribe, path)
        try:
            return fut.result(timeout=timeout_s)
        except concurrent.futures.TimeoutError:
            raise SttDown("timeout", f"no transcript within {timeout_s} s") from None
    finally:
        pool.shutdown(wait=False)


async def transcribe_async(transcriber: Transcriber, path: Path, *, timeout_s: float) -> Transcript:
    """The route's path: never blocks the event loop."""
    return await asyncio.to_thread(transcribe_with_timeout, transcriber, path, timeout_s=timeout_s)


__all__ = ["ENGINES", "FasterWhisperTranscriber", "SttDown", "Transcriber", "Transcript",
           "make_transcriber", "model_present", "probe_duration_s", "transcribe_async",
           "transcribe_with_timeout"]
