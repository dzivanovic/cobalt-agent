# stt-model-fix preflight — card 126 — 2026-10-08

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 0a | read `ops/desk/desk-launch.sh` card validation (`:699`–`:761`, build `:894`–`:913`) against the card header | JOB `stt-model-fix-1008` `[a-z0-9-]`; LADDER, BRANCH `ops/stt-model-fix-1008` plain, WORKTREE `stt-model-fix-1008` in pattern, BASE `4f764e79` 8-hex, TIP and CHECK REPORT and HOUSE B empty (allowed on build), RULINGS `2026-10-08 R685` well formed; `## ROWS` present; no `«FILL` | OK |
| 0b | REPORT rule `:900`–`:903` | REPORT is `/Users/cobalt/cobalt-wt/stt-model-fix-1008/docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md`, inside `$WT/$wt/docs/40 - DevDocs/reports/*.md` | OK |
| 0c | `rev-parse --verify refs/heads/ops/stt-model-fix-1008`; `ls /Users/cobalt/cobalt-wt` | branch absent (exit 1), worktree absent, so `:909` does not refuse | OK |
| 0d | BASE commit; `diff --stat 4f764e79 main -- src tests ops configs` | commit exists; main is now `de7b573e`, diff prints nothing | OK |
| 0e | card committed and clean: `log -3 -- <card> <draft> cto-2026-10-08.md`; `diff --stat HEAD` on the three | last commit `97601c75`; diff prints nothing (`:759`–`:761` pass) | OK |
| 0f | header per `CARD.md` `:9`–`:62` | keys match example 1 (`:76`–`:85`); `DB` left out because row B touches `src/` (`:22`); body order ROWS, NOT IN THIS JOB, READ, CHECK ASKS, RECORDS | OK |
| 1 | `grep "^\| R685 \|" reports/cto-2026-10-08.md` (`ruling_row` `:244`–`:271`) | one row (line 38): `HIS RULING … APPROVED · HIS RULING`; committed. LADDER cites R687 (line 40), present | OK |
| 2 | read `transcribe.py:75`–`:104` | `_load_model` `local_files_only=True` at `:84`; `model_present` `:95`–`:104` local only; cache kept at `:91` | OK |
| 3 | read `web.py:56`–`:60`, `:140`–`:149` | `get_config` `:56`–`:60`; `model_present(get_config())` `:145`; red line `:146` `speech-to-text down (model missing)` | OK |
| 4 | read `start_aset.sh:33`–`:39`, `voice.yaml:17`–`:26`, `restarts.py:27`–`:40`, `:226`–`:264`, `test_jobs_restarts.py:93`–`:130`, `config.py:30`–`:35`, `:116`–`:167`, `test_voice_transcribe.py:28`–`:45` | `start_aset.sh:36` "fetched by the deploy step", `:37` the model dir; `voice.yaml:19` dev dir, `:23` `tiny.en`, `:25` `0d3d19a3…`; `OPS_TOOLS` `:36`; `:230` OPS_TOOLS rule, `:260`–`:262` UNCLASSIFIED; test `:97`–`:108` the template; `load_voice_config` `:120`–`:166`; `MODEL_ENV` `:34`; `needs_model` `:38`–`:43` | OK |
| 5 | `grep fetch-voice-models` in the design; `ls ops`; `grep voice-models deploy-2026-09-27.md` | design `:158`–`:159`, `:317` name the one fetch command; `ops/` has no fetch file; `tests/ops/` has no voice test; deploy report `:476` exit 1 expected, `:500` owed to V4 | OK |
| 6 | `ls -la /Users/cobalt/.cobalt /Users/cobalt/.cobalt/voice-models` | only `voice-scratch` (0700); `voice-models`: No such file or directory | OK |
| 7 | `ls -laL …/.cobalt-dev/voice-models/models--Systran--faster-whisper-tiny.en/blobs` and `snapshots/0d3d19a3…` | blobs 2,128,466 + 75,537,502 + 2,317 + 422,309 = 78,090,594 bytes; snapshot holds `config.json`, `model.bin`, `tokenizer.json`, `vocabulary.txt` as relative `../../blobs/…` links; `refs/main` present; `base.en`, `small.en` also there | OK |
| 8 | rows A–C against the draft report | cause (model dir never filled), the script, the `OPS_TOOLS` line and the restarts RUN match draft §0 and decisions 1–4; nothing extra | OK |
| 9 | row A script logic | `--from` is a local `download_model(local_files_only=True)` then `copytree(symlinks=True)` of `snapshot.parents[1]`: relative links stay inside the target (X2); the download is only in the no-`--from` branch; a missing snapshot exits 1 before any write; target comes from `load_voice_config()` so `MODEL_ENV` and `_check_path` apply (X3); `copytree` onto an existing repo folder raises and nothing is deleted (X1); no secret is read | OK |
| 10 | row A tests offline | download monkeypatched to raise, `HF_HUB_OFFLINE=1`, tmp dirs, a fake cache; test (5) reads the dev dir only; no `curl` or other binary | OK |
| 11 | red on BASE | row A: the script file is absent, so all five error at load; row B: `ops/fetch-voice-models.sh` and `ops/fetch_voice_models.py` hit `:260`–`:262` and escalate, controls (`ops/desktop.sh`-style negative) stay as in `:111`–`:128`; row C asserts nothing | OK |
| 12 | R411, R412 | every command the drafter ran is an existing one; the new script is the card's product (see NOTE 3) | OK |
| 13 | RESTARTS per path in `## RECORDS` | `ops/fetch-voice-models.sh`, `ops/fetch_voice_models.py` → `OPS_TOOLS`, rule `operator script; no Cobalt reader`, `()`; `restarts.py` by import reach (row C quotes); `tests/…` → `test/documentation; no resident` | OK |
| 14 | the post-deploy command runs the script with `COBALT_ENV` unset: `env.py:60`–`:70`, `vault.py:155`–`:164`, `config.py:92`–`:99`, `grep COBALT_ENV tests/conftest.py tests/ops/conftest.py` | `load_voice_config()` → `_check_path` → `resolve_vault_path()` → `env.resolve_env()` raises `EnvConfigError` when `COBALT_ENV` is unset (no default, RULING 7). The card's command `COBALT_VOICE_MODEL_DIR=… sh …/fetch-voice-models.sh --from …` sets no `COBALT_ENV`; the wrapper does not set it; nothing loads `.env`. The script would print `FAILED: … — EnvConfigError` and exit 1, not `voice model READY`. The tests are in `tests/ops/`, whose conftest does not pin `COBALT_ENV` (only `tests/cobalt/conftest.py:11` does), and the row A text does not say to set it | FAIL |

## ISSUES
- FAIL 14: the POST-DEPLOY run (`## RECORDS`) would fail on `COBALT_ENV` unset. Fix the card: type `COBALT_ENV=production` before `COBALT_VOICE_MODEL_DIR=…` in the POST-DEPLOY command (the resident's mode, `start_aset.sh:33`), and say in row A that the script's tests set `COBALT_ENV=dev` with `monkeypatch.setenv` (tests/ops has no pin), or the script sets nothing and the card names who does. The dev vault must exist for the dev case (it does on this Mac).
- NOTE 1: main moved to `de7b573e` after the drafter's `4f764e79`; `src tests ops configs` are identical, so `BASE` stands.
- NOTE 2: R685 reads as a standing ruling (a reported defect is the desk's to fix); its relay text names `/radar`. The launcher accepts it (`HIS RULING` + `APPROVED`, committed).
- NOTE 3: the post-deploy command is a new command that writes under `/Users/cobalt/.cobalt`; `DEPLOY-HUB.md` has no write step (draft decision 4) and the desk's allow line may not cover it. Decide before the deploy who types it (R411).
- NOTE 4: test (5) must read the committed dev `model_dir` (no `COBALT_VOICE_MODEL_DIR` override) as its source and copy to `tmp_path`; the card says "dev `model_dir`" and leaves the target override implicit. A builder can read it either way.
- NOTE 5: a target that already holds a partial `models--Systran--faster-whisper-tiny.en` folder makes `copytree` fail (`FAILED`, exit 1, nothing deleted). Lawful, but the card does not say it.

PREFLIGHT DONE · card: stt-model-fix-126 · checks: 15 · fails: 1 · ready: NO
