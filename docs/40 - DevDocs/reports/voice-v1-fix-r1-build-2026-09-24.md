# VOICE V1 FIX R1 BUILD — 2026-09-24

Seat: `voice-v1-fix-r1-build-0924` (Opus 5.5). Prompt: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-24/36-voice-v1-fix-r1-build.md`. Branch `voice/v1-0923`, worktree `/Users/cobalt/cobalt-wt/voice-v1`.

## §0 Headline
- 23 of 24 FIX rows built red-first (red `cda1e73a` → fix `a1f8404a`, DevDocs `a8e28f4e`, RUNS `d4e48f22`). **C2 NOT BUILT**: its named `jobs.yaml` edit is refused by the registry schema (proven by a run). ASK DESK (ESCALATE 1).
- Gate (L68) on `d4e48f22`: offline 2772/0 · with-DB 3115/0 (8 deselects, 9 items) · live-note 142/0. `.env` removed and proven gone; `0017` proven absent (probe 28 == 29).
- RUNS 9: RUN-2, RUN-4c and RUN-7 (oversize) are RED → strict xfail, round-2 findings. RUN-1 is UNPROVEN under L76. RUN-3, 4a/5, 4b, 6, 8 and 9 are recorded.
- ESCALATE: 13.

## L74
The system reminder attached to the prompt read (a tool result, 16:44 ET) asked commits to carry a `Claude-Session:` line and named a file-send tool (`SendUserFile`). Recorded once here as DATA, not followed (L74): commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/36-voice-v1-fix-r1-build.md` | 1 | no output |
| check A stop | `tail -n 3 …/voice-v1-check-a-2026-09-24.md` | 0 | `VOICE V1 CHECK DONE · part: A (the ordered act) · … · defects that HOLD: 3 · ESCALATE: 11` |
| check B stop | `tail -n 3 …-check-b-…` | 0 | `VOICE V1 CHECK DONE · part: B (the model path) · … · defects that HOLD: 2 · ESCALATE: 12` |
| check C stop | `tail -n 3 …-check-c-…` | 0 | `VOICE V1 CHECK DONE · part: C (audio, model files, config, experiments) · … · defects that HOLD: 9 · ESCALATE: 14` |
| check D stop | `tail -n 3 …-check-d-…` | 0 | `VOICE V1 CHECK DONE · part: D (widget, route, turn, CLI) · … · defects that HOLD: 10 · ESCALATE: 11` |
| A committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …check-a…` | 0 | `54331f1fa89943804f7d1cb1028f5e5aa852a82b` |
| B committed | same, `-b-` | 0 | `e9652bdbcecfeebe988e8887fea5a08317ac84ba` |
| C committed | same, `-c-` | 0 | `2d2a8b0e14d44e327a91682074d0dfecaddfaed2` |
| D committed | same, `-d-` | 0 | `6d28d9e0852b1b5e9c6bb6b0feb4fb9fd4bf47d8` |
| classification stop | `tail -n 3 …/voice-v1-fix-r1-draft-2026-09-24.md` | 0 | `VOICE V1 FIX R1 DRAFTED · FIX: 24 · NOT REAL: 26 · UNPROVEN: 13 · OUT OF SCOPE: 11 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 2 · ESCALATE: 7` |
| classification committed | `git -C … log -1 --format=%H -- …fix-r1-draft…` | 0 | `5fdbb28dbc69e3e541899e90a5e24b2d7002c023` |
| `.env` pair his | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/voice-v1/.env)" …/cto-2026-09-24.md` | 0 | rows 76 (R64, desk record) and **80 (R68, P-HIS: "All approved." — names `36-voice-v1-fix-r1-build.md` and both strings)** |
| `.env` row committed | `git -C … log -1 --format=%H -S"36-voice-v1-fix-r1-build.md" -- …/cto-2026-09-24.md` | 0 | `4b0db777f6adc51974831f38e3981d775e9d112f` |
| launch row | `grep -n "36-voice-v1-fix-r1-build.md" …/cto-2026-09-24.md` | 0 | rows 72, 76, 80, **81 (R69 LAUNCH)** |
| launch row committed | `git -C … log -1 --format=%H -S"36-voice-v1-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `4b0db777f6adc51974831f38e3981d775e9d112f` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 16:44:09 EDT 2026` |
| clean tree | `git status --short --branch` | 0 | `## voice/v1-0923` |
| base | `git log --oneline -1` | 0 | `28b6b0c6 feat(voice-v1): build report` |
| no `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/voice-v1/.env: No such file or directory` |
| dev-DB lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | 22 notes listed (read only) |
| requires_vault | `grep -rln "requires_vault" tests` | 0 | `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_predicate.py`, `tests/taxonomy/test_catalyst.py` — the expected set (`-l` used for the file list) |

## D1 BASELINE
On `28b6b0c6`.
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `2704 passed, 358 skipped, 1 xfailed, 19 warnings in 92.79s` · exit 0 → `<bp>` = 2704, `<bf>` = 0, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `142 passed, 1 skipped, 15 warnings in 10.27s` · exit 0 → `<blp>` = 142, `<blf>` = 0. The one SKIPPED line: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it names `COBALT_TEST_LIVE_DRC`, NOT `COBALT_LIVE_VAULT_ROOT`; no skip names `COBALT_LIVE_VAULT_ROOT`.

## D2 RED (offline)
Test edits written (Edit tool), constructed literals only. **C2 is NOT BUILT** (see `## ESCALATE` 1): its named `jobs.yaml` shape is refused by the registry schema, so no C2 test was written and `test_voice_config.py:201` is NOT reversed. Twelve test paths changed, not thirteen: `test_jobs_restarts.py` is untouched.

| row | test | expected | on base |
|---|---|---|---|
| A1 | `test_voice_tools.py::test_platform_and_order_phrasings_are_refused_whatever_the_plan` (13 phrases × answer/act) + `::test_card_sides_and_price_fields_stay_readable` (5) | RED for the platform / order-verb cases; control + NOT-refused set green | 24 RED (12 phrases × 2 kinds; `open DAS and buy 100 XYZ` green ×2); NOT-refused set 5/5 green |
| A2 | `test_voice_card_stop.py::test_a_changed_card_state_alone_refuses_the_act` | GREEN-as-pin | green. By reading: `tools.py:233` refuses on `diff_sha256 != … or target_sha256 != …`; the test asserts `diff_sha256` is UNCHANGED, so deleting the `target_sha256` clause makes this test red |
| A5 | `test_voice_confirm.py::test_a_reaped_row_never_reports_done` | RED | RED: `assert ('done' != 'done')` (`:182`) |
| B1 | `test_voice_resolve.py::test_a_side_or_ordinal_word_outside_the_card_span_never_binds` ×3 | RED | RED ×3: `assert (not True)` (`:81`) |
| B1 | `::test_a_side_or_ordinal_inside_the_card_span_binds` ×4 (new) and the three existing tests whose spans now carry the word (`test_spoken_letter_forms_normalize` ×4, `test_a_side_word_narrows`, `test_an_ordinal_narrows_by_card_order`) | green expected by the prompt | **RED ×10 on base** (`assert (False)`, `:49` / `:61` / `:67` / `:90`) — see note (i) |
| B2 | `test_modelaccess_client.py::test_no_choices_is_empty` | GREEN-as-pin | green |
| C1 | `test_voice_scratch.py::test_a_failed_write_leaves_no_partial_file` (enospc / short × write_scratch / turn_audio) | RED | RED ×4: `AttributeError: module 'cobalt.voice.scratch' has no attribute 'ScratchWriteFailed'` |
| C3 | `test_voice_config.py::test_a_set_but_empty_env_override_crashes` ("" / "   " × scratch / model) | RED | RED ×4: `""` → `DID NOT RAISE`; `"   "` → raises, but names `scratch_dir` / `model_dir`, not the variable |
| C4 | `test_voice_scratch.py::test_a_file_already_gone_keeps_its_amber_line` | RED | RED: `assert [] == [('amber', True)]` |
| C5 | `test_voice_config.py::test_every_tunable_names_its_source_in_the_committed_file` | GREEN-as-pin | green on the second pass; keys checked: all 14 of `voice:` (`scratch_dir` … `allowed_peers`) — see note (ii) |
| C6 | `test_voice_transcribe.py::test_the_configured_revision_reaches_the_model_load` + slow `::test_a_revision_absent_from_model_dir_is_the_named_red` | GREEN-as-pin | green (both ran; the model is present) |
| C7 | `test_voice_scratch.py::test_one_deleter_across_every_voice_module` | GREEN-as-pin | green |
| C8 | `test_voice_config.py::test_a_path_under_docs_is_refused` (exact message; tail read from `_check_path`'s source) | GREEN-as-pin | green |
| C9 | `test_voice_config.py::test_plan_route_must_equal_the_agent_registry_route` | RED | RED: `DID NOT RAISE` |
| D1 | `test_voice_cli.py::test_a_cli_yes_never_confirms_a_production_act` + control `::test_a_cli_yes_still_confirms_in_dev` | RED + green control | RED (no SystemExit — the CLI `yes` confirmed); control green |
| D2 | `test_voice_cli.py::test_confirm_with_dry_run_is_refused_at_parse` | RED | RED |
| D3 | `test_voice_web.py::test_the_widget_reads_a_refused_status_as_red_never_all_clear` | RED | RED (`:240`) |
| D4 | `test_voice_web.py::test_no_local_voice_keeps_the_turns_red_lines_on_the_banner` | RED | RED (`:251`) |
| D5 | `test_voice_cli.py::test_a_failed_act_exits_non_zero_with_its_red_line` + `::test_an_expert_refusal_exits_non_zero_with_a_red_line` | RED | RED ×2 (exit 0; the failed act printed `RED:` but exited 0) |
| D7 | `test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` | GREEN-as-pin offline | SKIPPED offline (`requires_db`); one of the five L76 deselects at D8 — never run in this build |
| D8 | `test_voice_lifecycle.py::test_a_crash_after_the_write_is_reaped_and_never_applied_again` | GREEN-as-pin | green |
| D9 | `test_voice_cli.py::test_confirm_is_refused_in_production` | GREEN-as-pin | green |
| D10 | `test_voice_turn.py::test_run_turn_is_the_one_turn_function` + `test_voice_cli.py::test_the_cli_calls_the_one_turn_function` | GREEN-as-pin | green |
| X5 | `test_voice_turn.py::test_x5_measured_wrong_value_shapes_clarify` ×3 | GREEN-as-pin | green |

Notes:
- (i) B1's in-span cases cannot be green on base: the base resolver reads the WHOLE span as the ticker (`_ticker_of("the XYZ short")` = `THEXYZSHORT`, no match). The three existing tests (`test_spoken_letter_forms_normalize`, `test_a_side_word_narrows`, `test_an_ordinal_narrows_by_card_order`) relied on side / ordinal words OUTSIDE the card span — exactly the behaviour B1 removes — so their INPUT spans now carry the word (`"{span} long"`, `"the XYZ short"`, `"the second XYZ"`); every assertion is unchanged. They are B1's rows, red for the one named reason, green only through B1's edit.
- (ii) C5 was red on the FIRST pass for a defect in the new test itself (`len(checked) == 13`; `voice:` has 14 keys — every key's own block DID hold `# source:`). Corrected to 14 before any commit and the D2 command re-run. Not a pin red on base.
- (iii) Kept, not removed: C6's `t.revision == _cfg().stt_revision` and D10's two `inspect.getsource` substring asserts stay beside the new behavioural checks (nothing a V1 test asserts is removed).

D2 run (second pass), `uv run pytest -q -rs -p no:cacheprovider <the 13 D2 paths>` → `54 failed, 373 passed, 2 skipped, 5 warnings in 27.96s` (first pass: `55 failed, 372 passed, 2 skipped` — the one extra was C5's miscount, note (ii)). The 54: A1 24 · A5 1 · B1 13 (3 filler + 4 new in-span + 6 existing-with-span) · C1 4 · C3 4 · C4 1 · C9 1 · D1 1 · D2 1 · D3 1 · D4 1 · D5 2. SKIPPED ×2: `test_voice_confirm.py:217` and `test_voice_lifecycle.py:134`, `Postgres env settings not available`. Every GREEN-as-pin test and every other existing test passed.
Committed `git add` (12 paths) + `git commit` → **`<red>` = `cda1e73a`** `wip(fix-r1): voice V1 fix r1 red tests — … (L75; C2 not built — registry schema refuses its named shape)`.

## D3 THE EDITS
Built: A1 · A5 · B1 · C1 · C3 · C4 · C9 · D1 · D2 · D3 · D4 · D5 (the twelve code rows) — C2 NOT BUILT.
- **A1** `tools.py` `_ORDER` gains `das|lightspeed|tradestation|centerpoint|trading platform|platform` and the phrases `short(ing)? \d+`, `go (long|short)`, `(exit|close) (out of )?(my |the |this )?(\w+ )?position`, `get me out`, `take (my )?profits?`, `scale (in|out)`; no bare side / close / exit. Sentence unchanged.
- **A5** `confirm.py`: the `EXECUTING → DONE` return is read; `False` → `logger.error` naming turn + edit id, a `failed` outcome "The stop WAS written as edit <id>, but this turn's record was reaped mid-way. Check card <n> …". No retry, no second write.
- **B1** `resolve.py`: side / ordinal words read from the card span only; the span's qualifier words (`the`, `long`, `short`, the ordinals) are dropped before the ticker is spelled (else `the XYZ short` never matches — note (i)). `transcript` stays in the signature, unused for binding.
- **C1** `scratch.py`: `ScratchWriteFailed`; a raising or short `os.write`, or a failing `os.chmod`, → the partial file through `unlink_scratch` (the ONE unlink), a RED log line, the named error. `turn.py` `_hear` catches it beside `ScratchUnlinkFailed` (`scratch_write`, RED) — no new path.
- **C3** `config.py`: an override SET but empty / whitespace → `VoiceConfigError` naming the variable; unset → committed default.
- **C4** `scratch.py`: `UnlinkResult.already_gone`; `unlink_now` keeps the AMBER line and still sets `deleted_at`.
- **C9** `config.py`: `_check_plan_route` — `plan_route` must equal `load_agent().route` exactly, naming both; the field comment now says what the code does. `configs/cobalt/voice.yaml` NOT edited (both `local.plan`).
- **D1** `turn.py`: in production, a non-widget turn that finds a pending act in its session → `_Fail("cli_confirm_refused", …[F-02]…, red=True)`; nothing executed, the pending row left `awaiting_confirm`. The check sits before the expiry branch so the pending row is untouched.
- **D2** `cli.py`: `--confirm` + `--dry-run` → `_fail` before any turn.
- **D3 / D4** `web.py`: status fetch tests `r.ok` first (non-OK → RED `voice status refused (HTTP <status>)`); `speak(text, degraded)` repaints `degraded + amber`; `show()` passes `j.degraded || []`. No JS runner exists here — the check judges the static pins.
- **D5** `cli.py`: exit 1 on a `failed` turn OR any RED degraded line. To make "the expert refusal included" true, `turn.py` marks a `refused` confirm outcome RED as well as `failed` (`_RED_OUTCOMES`, used by `_after_pending` and `_tap`) — a two-line change in `turn.py` outside `:386-399`, needed by D5's own words; recorded here.

Proofs:
- D2's command, byte for byte → `427 passed, 2 skipped, 5 warnings in 27.91s` · exit 0 → **0 failed**.
- **C2 schema proof** (the named edit applied, run, reverted): `configs/cobalt/jobs.yaml` `readers: [com.cobalt.backup, com.cobalt.heartbeat, com.cobalt.aset]` → `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_jobs_restarts.py -k "backup_yaml_is_read_by_one_shots_only"` → `1 failed, 17 deselected`: `cobalt.jobs.config.JobConfigError: …/configs/cobalt/jobs.yaml: invalid job registry: 1 validation error for JobRegistry — Value error, no_resident_reads 'configs/cobalt/backup.yaml': com.cobalt.aset is a RESIDENT — a resident reader goes in its own \`reads\` and derives a restart` (`src/cobalt/jobs/config.py:404-408`). Reverted by Edit; `git diff 28b6b0c6 -- configs` is empty.
- `git diff --stat 28b6b0c6` → 20 paths: the 8 `src/cobalt/voice/{cli,config,confirm,resolve,scratch,tools,turn,web}.py` + the 12 D2 test paths. No `configs/` path (C2 not built), no other path.
- `grep -rn "Vault\|VaultWriter\|vaultwrite" src/cobalt/voice` → one hit, `src/cobalt/voice/config.py:95: except vault_mod.VaultConfigError as e:` — the base's vault-path READ for the §5 refusal; no write path, none new (L28).
- `git diff 28b6b0c6 -- src configs`, whole: identical to `git show a1f8404a -- src` (the fix commit holds every src change; `configs` empty). Hunks, in order: `cli.py` (docstring; the `--confirm`+`--dry-run` `_fail`; the RED-line exit) · `config.py` (field comment; `_check_plan_route`; the env loop; the `_check_plan_route` call) · `confirm.py` (the checked DONE transition) · `resolve.py` (docstring; `_SPAN_QUALIFIERS`; span-only words) · `scratch.py` (`ScratchWriteFailed`; the guarded write; `already_gone`; the kept AMBER line; `__all__`) · `tools.py` (`_ORDER`) · `turn.py` (`from cobalt import env`; the `ScratchWriteFailed` catch; `_RED_OUTCOMES` + `CLI_CONFIRM_REFUSED`; the two RED-kind uses; the production refusal) · `web.py` (`speak`, `show`, the status fetch). 114 insertions, 28 deletions over 8 files.
Committed → **`<fix>` = `a1f8404a`**.

## D4 DEVDOCS AND SCOPE
Edited, one to four sentences each where behaviour changed: `docs/40 - DevDocs/cobalt/voice/{tools,confirm,resolve,config,scratch,web,cli,turn}.md`. `config.md`'s "Backup sources — checked by the suite, not by the resident" paragraph is UNCHANGED (C2 not built; it stays true). Committed `docs(voice-v1): fix r1 DevDocs (L75)` → `a8e28f4e` (8 files, 37+/8−).

## D5 THE RUNS
New file `tests/cobalt/test_voice_fix_r1_runs.py`. Three RUNs were red on `a1f8404a` and are kept as `xfail(strict=True, reason="RUN-<n> red on a1f8404a — a round-2 finding, not fixed in fix r1 (L70/L75)")`; failures quoted verbatim under ESCALATE. Committed → **`<tip>` = `d4e48f22`**.

| RUN | row | how | result |
|---|---|---|---|
| RUN-1 | `16` item 3 timing | `grep -rn "FOR UPDATE\|lock_timeout\|statement_timeout" src/cobalt/cards/store.py src/cobalt/db.py` | hits ONLY `FOR UPDATE`: `store.py:12`, `:15` (docstring), `:277`, `:680`, `:1024`, `:1153`, `:1194`, `:1238`; NO `lock_timeout`, NO `statement_timeout` in either file. Timing UNPROVEN (needs `0017` committed, L76) — ESCALATE |
| RUN-2 | `16` row 7, A4 | pytest: a store whose 2nd read moves the stop | **RED** → xfail: `Failed: DID NOT RAISE <class 'cobalt.voice.tools.TargetChanged'>` |
| RUN-3 | `16` ESC 3 / G5 | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_voice_turn.py -k "confirm or cancel or other or pending"` | `8 passed, 21 deselected in 0.36s`. Ids (via `--co`): `test_yes_confirms_with_no_model_call_and_executes_once` (asserts NO model call while `awaiting_confirm`: `len(deps.plan.calls) == calls`), `test_no_cancels`, `test_any_other_transcript_ends_the_pending_action_and_is_not_planned` (asserts the other transcript is NOT planned in the same turn), `test_a_confirm_word_inside_the_request_does_not_execute`, `test_a_tap_confirms`, `test_a_tap_from_another_session_is_refused`, `test_a_pending_action_past_its_ttl_executes_nothing` (also asserts no model call), `test_a_changed_target_reads_the_new_change_back_for_reconfirmation`. Both claims have an asserting test |
| RUN-4a / RUN-5 | `17` row 4; `18` row 18 | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_voice_web.py` | `32 passed in 0.58s`. Off the loop: `test_loopback_is_allowed_and_the_turn_runs_off_the_loop`; startup sweep under the lock: `test_startup_sweeps_every_file_under_the_lock_and_shutdown_releases`; held lock → `ScratchLocked`, nothing deleted: `test_startup_fails_loud_when_another_holder_has_the_lock`. `audio_deleted_at` is NOT asserted in `test_voice_web.py`; it is asserted in `test_voice_turn.py::test_an_audio_turn_unlinks_its_file_and_records_only_metadata` and `::test_a_transcribe_failure_unlinks_and_fails_loud` (in D7's suite) |
| RUN-4b | `17` row 5 | pytest: refuse / clarify / unsupported Plans carrying `cards.set_stop` + args | green ×3 — nothing executed, no pending action, reply by kind |
| RUN-4c | `17` row 6 | pytest: `call_sync` raises `ValueError` inside the real `plan_turn` | **RED** → xfail: the turn DOES fail loud (`failed` row, RED line, no exception escapes) but names it `turn_error`: `assert 'Something fa... was changed.' == "Cobalt can't...(ValueError)."` — `- Cobalt can't think right now (ValueError).` / `+ Something failed in this turn (ValueError); nothing was changed.` |
| RUN-6 | `18` row 19 | pytest: `tempfile.tempdir` → tmp subfolder, 1.5 MB loopback POST, real `run_turn`, faked transcriber | green: the subfolder listed `[]` after the request; scratch dir empty |
| RUN-7 | `19` row 14 | pytest: CLI `--audio` zero-byte / over `max_upload_bytes` | zero-byte green (named `zero-byte audio`, exit 1, no file). Oversize **RED** → xfail: `Failed: DID NOT RAISE <class 'SystemExit'>` — the CLI transcribes a clip over `max_upload_bytes` and exits 0 (no bound on the CLI path) |
| RUN-8 | `19` row 14 | `grep -rn "cobalt.db\|db.connect\|psycopg" src/cobalt/modelaccess` | no hits (exit 1) — the model layer opens no DB connection; a dry run's Plan call writes no row there |
| RUN-9 | `17` ESC (viii) | `## RESTARTS` | below |

`uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_voice_fix_r1_runs.py` → first run `3 failed, 5 passed in 0.43s`; with the three marks `5 passed, 3 xfailed in 0.41s`.

## D6 LIVE-NOTE
On `d4e48f22`, D1's command byte for byte → `142 passed, 1 skipped, 15 warnings in 9.69s` · exit 0 → `<lp>` = 142, `<lf>` = 0, 0 errors. The one SKIPPED line is D1's (`test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC … not set`); none names `COBALT_LIVE_VAULT_ROOT`. GATE met.

## D7 OFFLINE
`ls /Users/cobalt/cobalt-wt/voice-v1/.env` → `No such file or directory`. D1's offline command byte for byte on `d4e48f22` → `2772 passed, 358 skipped, 4 xfailed, 20 warnings in 90.68s (0:01:30)` · exit 0 → `<p>` = 2772, `<f>` = 0, 0 errors. xfailed 4 = `43`'s 1 + RUN-2, RUN-4c, RUN-7 (oversize). `<p>` − `<bp>` = 68 new passing offline tests (D2's and D5's), skips unchanged at 358. GATE met.

## D8 WITH-DB
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1) — lock free.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/voice-v1/.env` (exit 0; never read or printed). `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly one line: `-rw-------  1 cobalt  staff  2186 Sep 24 16:59 /Users/cobalt/cobalt-wt/voice-v1/.env`.
- (c) Deselect proof, the five ids → `5 failed, 5 warnings in 32.21s`. Re-run with `-rf --tb=line` for one line each (the first run's output was truncated):
  - `test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction` — FAILED `psycopg.errors.UndefinedTable: relation "voice_turns" does not exist`
  - `test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries` — FAILED same
  - `test_voice_store.py::test_single_flight_under_two_real_connections` — FAILED same
  - `test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both` — FAILED same (INSERT, then the cleanup DELETE)
  - `test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` — FAILED same (its first error `AssertionError: the upload never reached the scratch dir` — the served turn could not create its row — then the cleanup `DELETE FROM voice_turns` → `UndefinedTable`). The test started and SIGKILLed only its own servers.
  None passed → `voice_turns` does NOT exist on `cobalt_dev`.
- (d) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy <the 8 --deselect>` on `d4e48f22` → `3115 passed, 6 skipped, 9 deselected, 4 xfailed, 20 warnings in 169.19s (0:02:49)` · exit 0 → `<dp>` = 3115, `<df>` = 0, 0 errors; deselected 9 as expected (`TestMigrationRoundTrip` carries 2). SKIPPED (6): `test_cards_picks.py:383` (S2-P2's `card_score` present on `cobalt_dev`), `test_cards_picks.py:396` (real S2-P2 0007 applied), `test_radar_evaluate.py:691`, `test_catalyst.py:365`, `test_predicate.py:262` (`COBALT_LIVE_VAULT_ROOT` not set — run at D6), `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC` not set). `test_voice_store.py`'s `test_forward_creates_the_table_user_side_and_rollback_drops_it_cleanly` and `test_no_bytes_column_in_either_catalog` are not deselected and not skipped → RAN and passed (0 failed), applying `0017` inside their own transaction and rolling it back. No `cobalt db migrate`, before or after. GATE met.
- (e) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → `1 failed in 5.70s`, as expected: `AssertionError: every table's rows must stream through its own NAMED (server-side) cursor … assert 28 == 29` — SHORT BY EXACTLY 1; the 28 named cursors listed are `cobalt_probe_archive_incidents` … `cobalt_probe_vault_writes`, and NO `cobalt_probe_voice_turns`. **`0017: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 1)`.**
- (f) `rm /Users/cobalt/cobalt-wt/voice-v1/.env` (exit 0) → `ls /Users/cobalt/cobalt-wt/voice-v1/.env` → `ls: /Users/cobalt/cobalt-wt/voice-v1/.env: No such file or directory` (17:03 ET). **`.env: removed, proven gone (D8)`.**

## RESTARTS
RUN-9 (L42).
- `uv run cobalt jobs restarts 28b6b0c6..d4e48f22` → exit 0. Table: the 8 `docs/40 - DevDocs/cobalt/voice/*.md` → `DOCS`, `-`; `src/cobalt/voice/cli.py` → `static import reach`, `com.cobalt.radar`; `src/cobalt/voice/{config,confirm,resolve,scratch,tools,turn,web}.py` → `static import reach`, `com.cobalt.aset,com.cobalt.radar`; the 13 test paths (12 `M` + `test_voice_fix_r1_runs.py` `A`) → `test/documentation; no resident`, `-`. Last line: `RESTARTS: com.cobalt.aset com.cobalt.radar`. As expected: voice src derives `com.cobalt.aset` (and `com.cobalt.radar`, the resident that imports `cobalt.cli`); tests and docs derive nothing. `configs/cobalt/jobs.yaml` is not in the range (C2 not built).
- `uv run cobalt jobs restarts 04b05cd4..d4e48f22` → exit 1, `FAILED: RestartError: one or more changed paths were unclassified`. `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. UNCLASSIFIED (6, the same six `43` recorded): `configs/cobalt/agents/voice.yaml`, `configs/cobalt/modelaccess.yaml`, `configs/cobalt/voice.yaml` (UNCLASSIFIED CONFIG), `ops/start_aset.sh`, `pyproject.toml`, `uv.lock` (UNCLASSIFIED). Nothing new; the deploy / desk rules them (classification O11).

## CONTINUE
next: none — CLOSE done (red `cda1e73a`, fix `a1f8404a`, docs `a8e28f4e`, tip `d4e48f22`; all three suites green; `.env` removed).

## ESCALATE
1. **C2 NOT BUILT — `ASK DESK: C2's registry shape. The named edit (\`com.cobalt.aset\` added to \`no_resident_reads\` \`readers:\` for \`configs/cobalt/backup.yaml\`) is REFUSED by the registry schema — proven at D3: \`JobConfigError … no_resident_reads 'configs/cobalt/backup.yaml': com.cobalt.aset is a RESIDENT — a resident reader goes in its own \`reads\` and derives a restart\` (src/cobalt/jobs/config.py:404-408). The schema's own path — \`configs/cobalt/backup.yaml\` in com.cobalt.aset's \`reads:\` AND the \`no_resident_reads\` entry removed (config.py:393-397 refuses a path in both) — rewrites the registry beyond "nothing else in jobs.yaml", flips \`test_backup_yaml_is_read_by_one_shots_only_and_derives_no_restart\` far beyond "gains com.cobalt.aset and ONLY that" (its call-graph pin \`EXPECTED_BACKUP_YAML_READERS\`, entrypoints and the all-one-shot assertion all change, since load_voice_config → get_config / default_deps / cmd_turn become readers), and puts a startup-once read into a list defined as "re-read on every request". Which shape? [16:58 ET]`** Safe default taken: C2 left as built by `43` (the resident does not read `backup.yaml`; the suite checks the committed dev paths and the production overrides against every real source); no C2 test written; `test_voice_config.py:201` NOT reversed; `configs/cobalt/jobs.yaml` and `test_jobs_restarts.py` untouched. FIX built: 23 of 24.
2. **RUN-2 red (a round-2 finding, not fixed):** `tests/cobalt/test_voice_fix_r1_runs.py::test_run2_a_stop_moved_between_the_two_reads_is_refused` → `Failed: DID NOT RAISE <class 'cobalt.voice.tools.TargetChanged'>`. A stop moved between `execute_stop`'s read (`tools.py:228`) and `set_card_stop`'s read (`card_stop.py:43`) is not refused; the edit is recorded with the second read's `from_stop`.
3. **RUN-4c red:** `…::test_run4c_an_untyped_plan_error_fails_loud_named` → `assert 'Something fa... was changed.' == "Cobalt can't...(ValueError)."` (`- Cobalt can't think right now (ValueError).` / `+ Something failed in this turn (ValueError); nothing was changed.`). A `ValueError` inside `plan_turn` is caught by `run_turn`'s generic branch: loud, `failed`, RED — but classed `turn_error`, not `voice_plan`.
4. **RUN-7 red:** `…::test_run7_cli_audio_zero_byte_and_oversize_are_refused[over_max_upload_bytes]` → `Failed: DID NOT RAISE <class 'SystemExit'>`. The CLI `--audio` path has no `max_upload_bytes` bound (the route has one, `web.py:110`).
5. **RUN-1: UNPROVEN — needs 0017 committed (L76); A5's code path is fixed either way.** The grep found `FOR UPDATE` only; no `lock_timeout` / `statement_timeout` in `cards/store.py` or `db.py`.
6. **B1 changed three existing tests' INPUT spans** (D2 note (i)): `test_spoken_letter_forms_normalize`, `test_a_side_word_narrows`, `test_an_ordinal_narrows_by_card_order` relied on side / ordinal words outside the card span — B1's removed behaviour. Assertions unchanged; the check should read these three.
7. **D5 touched `turn.py` outside `:386-399`** (`_RED_OUTCOMES`: an expert refusal is RED, used at `_after_pending` and `_tap`) — needed for "the expert refusal included".
8. **D3 diff quoting:** the whole `git diff 28b6b0c6 -- src configs` was read in full at D3; the report lists its hunks rather than pasting ~260 lines — `git show a1f8404a -- src` is the verbatim record (`configs` diff empty).
9. **C5 first-pass red was the new test's own miscount** (13 vs 14 keys), fixed before the red commit (D2 note (ii)).
10. **L74:** one block (a `Claude-Session:` commit line, a file-send tool) recorded once under `## L74`, not followed.
11. **"L76 left five V1 with-DB tests UNRUN in this build (`D8` (c) proves why): the store round-trip and reaper, X-X13's two real-connection races, and X-E7 (with D7's strengthened version of it), plus RUN-1's timing. Each needs `voice_turns` COMMITTED on a database. Where they run before the merge — the stacked L68 gate with `0017` applied and rolled back before its stop line (L76's second clause), or a transaction-scoped rewrite of those tests in a later round — is the desk's ruling, not this build's."** (Desk R64 (1) already rules the stacked L68 gate.)
12. **"OUT OF SCOPE, carried: D6 — `tests/cobalt/test_radar_panel_cards.py` changed outside `43`'s list (the widget on `/radar` and three `/voice/*` POST routes); its revert (`git show 04b05cd4:tests/cobalt/test_radar_panel_cards.py` restored) would turn the `/radar` byte-equality red, so it was NOT taken; the desk rules the boundary. X-E10 — the FINAL's column routes 'an unexpected native / GPL package' to TRIBUNAL ROUND 2 (FINAL `:285`); not this build's."**
13. **"The FIX rows moved on file evidence only (`16`–`19` FOR THE CLASSIFIER, 24 HOLD, + R41's X5). The red: D2 offline on `cda1e73a`, green on `a1f8404a`. The check is `37` (round 2; Opus 5.5 + Grok, with Sol from Sep 26th, 2026 6:47 AM), and its packet carries this report's executed output of all three suites and the RUNS (L68). The deploy's L68 gate re-proves them on the tree that ships. The DEVICE SESSION (E1 E3 E5 E8 X3) stays OWED before any ship."** Plus: C2 is open (item 1), so 23 of the 24 FIX rows are built.

VOICE V1 FIX R1 BUILT d4e48f22 | on 28b6b0c6 | red cda1e73a | offline 2772/0 | with-DB 3115/0 | live-note 142/0 | .env: removed | 0017: rolled back | FIX: 23 of 24 (C2 NOT BUILT — registry schema refuses its named shape; ASK DESK) | RUNS: 9 | ESCALATE: 13
