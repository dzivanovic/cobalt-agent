# `src/cobalt/voice/transcribe.py`

## What it does
Local speech-to-text. `Transcriber` is the protocol (path in, `Transcript`
out: text, language, duration, the engine's per-segment `no_speech_prob`
and `avg_logprob` AS RETURNED, engine, model, revision, `stt_ms`).
`FasterWhisperTranscriber` is the one engine (`ENGINES`), picked by
`stt_engine` in `configs/cobalt/voice.yaml`.

## Local only, pinned
CPU faster-whisper, with the size / revision / compute type X-E2 measured
(`tiny.en`, `0d3d19a3…`, `int8`), loaded from `model_dir` with
`local_files_only=True` — never a download at run time. The model loads
once per process and is shared. `model_present()` answers "is the pinned
model on disk" with a local lookup only.

## Named failures (`SttDown`)
`str()` is the widget's RED line: `speech-to-text down (model missing)`,
`(timeout)`, `(audio undecodable)`, `(engine error)`. No cloud engine
exists to fall back to (W4); the text box keeps working.

## Off the loop
`transcribe_async` → `asyncio.to_thread` → `transcribe_with_timeout`, a
worker thread bounded by `stt_timeout_s`. A timed-out decode cannot be
killed; it finishes on its own after the turn has already failed and
unlinked its file (X-X20: a decode survives its file's unlink).
`probe_duration_s` reads the clip length from the container before any
decode, so `max_clip_s` is enforced first.
