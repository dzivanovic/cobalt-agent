# stt-model-draft — 2026-10-08

## §0 Headline
- Cause: production's model directory `/Users/cobalt/.cobalt/voice-models` (`ops/start_aset.sh:37`) does not exist, so `model_present` (`src/cobalt/voice/transcribe.py:95`–`:104`) is false and `status_lines` (`src/cobalt/voice/web.py:145`–`:146`) raises the RED banner.
- The code and the path are right. The design's one fetch command, `ops/fetch-voice-models.sh`, was never built; the 09-27 deploy recorded the empty directory as owed to V4.
- The pinned `tiny.en` snapshot (78,090,594 bytes) is already on this Mac in the dev directory, so the fix is a local copy and nothing is downloaded.
- Card `126`: build that script (copy with `--from`, download only without it) plus an `OPS_TOOLS` line. After the deploy, the desk runs it once and the banner clears with no restart.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md`: build card, `JOB: stt-model-fix-1008`, `BASE: 4f764e79`, rows A (script + 5 offline tests, banner test included), B (`restarts.py` `OPS_TOOLS`), C (restarts RUN).
- Post-deploy command, in the card's `## RECORDS`: `COBALT_VOICE_MODEL_DIR=/Users/cobalt/.cobalt/voice-models sh /Users/cobalt/cobalt/ops/fetch-voice-models.sh --from /Users/cobalt/.cobalt-dev/voice-models`.

## DECISIONS
1. Shape: a BUILD card, not a one-row OPS card. No existing command installs the model, and a download is not the only fix, because the snapshot is on disk. So neither branch of the prompt fits. Default taken: build the design's named one-fetch script (`VOICE-TTS-DRAFT-FINAL-2026-09-25.md:158`–`:159`, `:317`) with a local-copy path. A raw `cp -R` row was not taken, because no hub step runs a write and it would bypass the one-path rule (L3).
2. `REPORT` path: the prompt gave `/Users/cobalt/cobalt/docs/…/stt-model-fix-build-2026-10-08.md`; `CARD.md` requires the build report inside the worktree. Default taken: `CARD.md`, `/Users/cobalt/cobalt-wt/stt-model-fix-1008/docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md`. Both are absent.
3. `DB` key left out: row B touches `src/cobalt/jobs/restarts.py`, which `CARD.md` excludes from `none`. Without that line, the two new `ops/` paths escalate as `UNCLASSIFIED` (`restarts.py:260`–`:262`).
4. The production run is the desk's, after the deploy (`DEPLOY-HUB.md` has no write step). It needs no restart, because `model_present` runs per `/voice/status` call.

## RECORDS
- `grep model missing|speech-to-text src/` → `voice/web.py:146`, `voice/transcribe.py:1`, `:7`, `:34`, `:47`, `voice/store.py:60` (11:3x ET).
- Read `voice/transcribe.py` 1–190, `voice/web.py` 110–169 and `:56`–`:60`, `voice/config.py:120`–`:166`, `configs/cobalt/voice.yaml` (whole; `:19`, `:23`, `:25`), and `ops/start_aset.sh:25`–`:50`.
- `grep COBALT_VOICE_MODEL_DIR|voice-models|tiny.en` over `ops src scripts pyproject.toml` → only `ops/start_aset.sh:37` and `voice/config.py:8`, `:34`. A `Grep download_model|local_files_only=False|snapshot_download` in `src/cobalt` returns only `transcribe.py:98`, `:100` (local only).
- `ls -la /Users/cobalt/.cobalt/voice-models` → `No such file or directory`; `/Users/cobalt/.cobalt` holds only `voice-scratch`.
- `ls -la` of the dev model dir lists `models--Systran--faster-whisper-{tiny,base,small}.en`. The tiny.en snapshot `0d3d19a3…` holds 4 relative links; `ls -laL blobs` sizes sum to 78,090,594 bytes.
- `ls /Users/cobalt/cobalt/ops`: no fetch script. Design `VOICE-TTS-DRAFT-FINAL-2026-09-25.md:158`–`:159`, `:317` names `ops/fetch-voice-models.sh` as the one fetch command.
- `reports/deploy-2026-09-27.md:476`, `:500` and `reports/voice-v1-build-2026-09-23.md:452` record the model as not fetched (V4 step).
- `src/cobalt/jobs/restarts.py:29`–`:38`, `:230`, `:238`–`:264`; `tests/cobalt/test_jobs_restarts.py:95`–`:139`; `tests/cobalt/test_voice_transcribe.py:30`–`:50`.
- `DEPLOY-HUB.md` grep: no step runs a write or an install; smoke reads only.
- `git -C /Users/cobalt/cobalt rev-parse main` → `4f764e79e860bf14fe9ea7b4b387e15b532bd11f`. `git -C /Users/cobalt/cobalt diff --stat main -- src tests ops configs` printed nothing. `date` → 2026-10-08 11:37 EDT.
- The report and worktree paths, `stt-model-fix-build-2026-10-08.md`, `stt-model-draft-2026-10-08.md` and `/Users/cobalt/cobalt-wt/stt-model-fix-1008`, were all absent before writing.
- Nothing was downloaded, installed or written outside the card and this report. No git write.

STT CARD DRAFTED · decisions: 4
