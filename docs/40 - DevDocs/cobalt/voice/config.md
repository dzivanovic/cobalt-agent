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
Since fix r1: a directory override that is SET but empty crashes naming the
variable (unset still means the committed value), and `plan_route` must
equal the agent registry's `route` exactly (`_check_plan_route`), or the
load crashes naming both.

## The path refusals (FINAL §5)
`scratch_dir` and `model_dir` — from the file, or from
`COBALT_VOICE_SCRATCH_DIR` / `COBALT_VOICE_MODEL_DIR` (production's
explicit override, the same pattern as `COBALT_VAULT_PATH`, exported by
`ops/start_aset.sh`) — are refused when relative, under `docs/`, under the
repo root, under the production vault, or under the resolved vault. Audio
must never reach git, the vault or a backup (R18 (b)).

## Backup sources — checked on every load, the resident's included
A path under any `configs/cobalt/backup.yaml` source is refused. A caller
may pass `backup_sources=`; when none are passed (the ASET resident's
call), `load_voice_config` reads them through the one loader,
`cobalt.backup.config.load_backup_config()`, and a `BackupConfigError`
becomes a `VoiceConfigError` naming it (fix r2, C2; FINAL :118). So
`backup.yaml` sits in `com.cobalt.aset`'s `reads:` in
`configs/cobalt/jobs.yaml`, and a change to it derives that resident's
restart (L42) — the resident caches the voice config at its first load
(`voice/web.py` `get_config`), so only a restart re-reads it.

## G2 / K5
`scratch_max_age_s ≤ stt_timeout_s` is refused: V4's probe counts files
older than `scratch_max_age_s`, and a file younger than one transcribe is
never "old". (Under R2-1 side B the sweep runs only at process start, so
no in-process sweep can fire mid-transcribe.)

## 2026-10-01 — voice-peers
The committed `allowed_peers` in `configs/cobalt/voice.yaml` is localhost plus the five tailnet devices' IP literals (cobalt, badass, dejans-s25, fedora, msi), per his ruling 2026-09-28 R95, re-stated 2026-10-01 R14; no code changed, and the resident `com.cobalt.aset` re-reads it only at a restart.
