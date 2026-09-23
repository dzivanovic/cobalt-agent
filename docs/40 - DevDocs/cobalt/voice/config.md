# `src/cobalt/voice/config.py`

## What it does
Loads `configs/cobalt/voice.yaml` into `VoiceConfig`: the scratch and model
directories, the speech-to-text engine / model / pinned revision / compute
type, the W7 engine tunables (`max_clip_s`, `max_upload_bytes`,
`stt_timeout_s`, `confirm_ttl_s`, `scratch_max_age_s`, `history_turns`),
the Plan route NAME and the socket peers allowed on `/voice/*`.

## Fail-loud (L1, L10)
Every key is required; an unknown key crashes; `stt_engine` has one legal
value (no cloud engine exists — W4); `allowed_peers` must be IP literals.

## The path refusals (FINAL §5)
`scratch_dir` and `model_dir` — from the file, or from
`COBALT_VOICE_SCRATCH_DIR` / `COBALT_VOICE_MODEL_DIR` (production's
explicit override, the same pattern as `COBALT_VAULT_PATH`, exported by
`ops/start_aset.sh`) — are refused when relative, under `docs/`, under the
repo root, under the production vault, or under the resolved vault. Audio
must never reach git, the vault or a backup (R18 (b)).

## Backup sources — checked by the suite, not by the resident
A path under a `configs/cobalt/backup.yaml` source is refused when the
caller passes `backup_sources=`. The ASET resident does NOT read
`backup.yaml`: doing so would make that file a resident read, contradicting
`configs/cobalt/jobs.yaml`'s declared no-resident-read and L42's restart
derivation (`test_jobs_restarts.py` pins the readers). Today's two sources
(the vault; `data/.cobalt_vault` under the repo root) are already refused
by the vault and repo checks, and `test_voice_config.py` loads the
committed dev paths AND the production overrides with every real backup
source passed. The choice is an ESCALATE in the V1 build report.

## G2 / K5
`scratch_max_age_s ≤ stt_timeout_s` is refused: V4's probe counts files
older than `scratch_max_age_s`, and a file younger than one transcribe is
never "old". (Under R2-1 side B the sweep runs only at process start, so
no in-process sweep can fire mid-transcribe.)
