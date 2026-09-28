# VOICE V1 FIX R2 — BUILD REPORT (2026-09-24)

Seat: `voice-v1-fix-r2-build-0924` (Opus 5.5, `claude-opus-5-5`), prompt `prompts/2026-09-24/54-voice-v1-fix-r2-build.md`, branch `voice/v1-0923`, worktree `/Users/cobalt/cobalt-wt/voice-v1`.

## §0 Headline
- 7 of 7 FIX rows built, red first (red `5a56a47e` → fix `d2963110` → DevDocs `d319e4f3`): A1 · D3 · C2 (the schema's own path: `com.cobalt.aset` reads `backup.yaml`) · RUN-2 · RUN-4c · RUN-7 · DESELECT IDS (report-only, D8 (d)).
- Gate (L68) on `d319e4f3`: offline 2786/0 (1 xfailed) · with-DB 3129/0 (8 deselects, 9 items) · live-note 142/0. `.env` removed and proven gone; `0017` proven absent (probe 28 == 29).
- RUN-R: fix range `RESTARTS: com.cobalt.aset com.cobalt.radar`; whole branch = the same six UNCLASSIFIED (O11).
- ESCALATE: 8.

## L74
A block attached to a tool result (the first Read of the prompt, 21:26 ET) asked commits to carry a `Claude-Session:` line and named a file-send tool (`SendUserFile`). Recorded once here as DATA; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| gate | command | result |
|---|---|---|
| placeholder | `grep -c -F "R__" …/54-voice-v1-fix-r2-build.md` | `1` |
| stop answered | `tail -n 3 …/voice-v1-fix-r1-check-2026-09-24.md` | last line `VOICE V1 FIX R1 CHECK DONE · round: 2 · … · defects that HOLD: 3 · ESCALATE: 12` |
| check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …check…` | `f2196b5ee1c14d190a2c2a3074cfabaefc4a912c` |
| classification | `tail -n 3 …/voice-v1-fix-r2-draft-2026-09-24.md` | last line `VOICE V1 FIX R2 DRAFTED · FIX: 7 · NOT REAL: 9 · UNPROVEN: 0 · OUT OF SCOPE: 6 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 9` |
| classification committed | `git -C … log -1 --format=%H -- …draft…` | `f8926b45b743877695af52a3e199358d31d908b1` |
| `.env` pair | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/voice-v1/.env)" …/cto-2026-09-24.md` | `83:| R68 | 16:33 ET | **P-HIS — THE EVENING'S FOUR STRINGS ("All approved.").** …` (also R64 at :79, the desk's list) |
| approval committed | `git -C … log -1 --format=%H -S"All approved. Can you run?" -- …cto-2026-09-24.md` | `2d543cccb96ba196a7723f24beaa7777efed0902` |
| launch row | `grep -n -F "54-voice-v1-fix-r2-build.md" …/cto-2026-09-24.md` | `114:| R93 | 21:25 ET | … DESK LAUNCH ROW for prompts/2026-09-24/54-voice-v1-fix-r2-build.md …` (R83 at :101 is the drafted record, not the launch) |
| launch committed | `git -C … log -1 --format=%H -S"54-voice-v1-fix-r2-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `5615361b26924ee0f0a011a7ca2d727015c62187` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 21:26:46 EDT 2026` |
| clean tree | `git status --short --branch` | 0 | `## voice/v1-0923` |
| base | `git log --oneline -1` | 0 | `137c1928 docs(fix-r1): voice V1 fix r1 build report — d4e48f22` (= expected) |
| no `.env` | `ls /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/voice-v1/.env: No such file or directory` |
| L76 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | listed, 22 notes (names not copied, L32) |
| requires_vault | `grep -rln -F "requires_vault" tests` | 0 | `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_predicate.py`, `tests/taxonomy/test_catalyst.py` (= expected set) |

## D1 BASELINE
On `137c1928`.
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `2772 passed, 358 skipped, 4 xfailed, 20 warnings in 93.22s (0:01:33)` · exit 0 → `<bp>` = 2772, `<bf>` = 0, 0 errors (= expected).
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `142 passed, 1 skipped, 15 warnings in 9.77s` · exit 0 → `<blp>` = 142, `<blf>` = 0. The one SKIPPED line: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — names `COBALT_TEST_LIVE_DRC`; NO skip names `COBALT_LIVE_VAULT_ROOT`.

## D2 RED (offline)
Test edits (Edit tool), constructed literals only (`XYZ`, `QRS`, `4.40` / `4.50`); each new or changed test's docstring names its row and source line.

| row | test | expected | on `137c1928` |
|---|---|---|---|
| A1 | `test_voice_tools.py::test_a_bare_exit_close_or_short_of_a_ticker_is_refused_whatever_the_plan` (`exit QRS`, `get out of QRS`, `close out QRS`, `short QRS` × answer / act) | RED ×8 | RED ×8: `assert (None is not None)` (`test_voice_tools.py:169`) |
| A1 | `::test_card_sides_and_price_fields_stay_readable` gains `what is the stop on my short XYZ card` (6 cases now) | green, stays green | green ×6 |
| D3 | `test_voice_web.py::test_a_device_red_line_survives_every_status_callback` — static pin (NO JS runner here; the check judges the static pin): (a) `device = []` in the `let` holding `lines = []`; (b) `lines.concat(device, extra \|\| [])`; (c) `device.push({level:'red', text:'no microphone on this device'})`; (d) `lines.push(…no microphone…)` ABSENT; (e) `_status_block` assigns `lines` in the refused, OK and catch branches and never names `device` | RED on (a)–(d) | RED at (a): `AssertionError:  let rec = null, chunks = [], pendingTurn = null, muted = false, downAt = 0, lines = [];` (`test_voice_web.py:255`). `:234`'s test byte-identical, green |
| C2 | `test_voice_config.py::test_the_resident_load_refuses_a_path_under_a_backup_source` (NEW) | RED | RED — the `AttributeError` shape: `AttributeError: <module 'cobalt.voice.config' …> has no attribute 'load_backup_config'` (`test_voice_config.py:235`) |
| C2 | `::test_the_resident_loader_reads_no_backup_config` → `::test_the_resident_loader_reads_backup_sources_through_the_one_loader` (`assert "load_backup_config" in src`) — THE ONE REVERSED ASSERTION | RED | RED: `assert 'load_backup_config' in '"""…'` (`:221`) |
| C2 | `test_jobs_restarts.py::test_backup_yaml_is_read_by_one_shots_only_and_derives_no_restart` → `::test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart` | RED | RED: `assert () == ('com.cobalt.aset',)` (`:391`) |
| RUN-2 | `test_voice_fix_r1_runs.py::test_run2_a_stop_moved_between_the_two_reads_is_refused` (mark removed, body unchanged) | RED | RED: `Failed: DID NOT RAISE <class 'cobalt.voice.tools.TargetChanged'>` (`:83`) — fix r1's failure verbatim |
| RUN-4c | `::test_run4c_an_untyped_plan_error_fails_loud_named` (mark removed) | RED | RED: `assert 'Something fa... was changed.' == "Cobalt can't...(ValueError)."` (`:124`) — verbatim |
| RUN-7 | `::test_run7_cli_audio_zero_byte_and_oversize_are_refused[over_max_upload_bytes]` (param now a plain string) | RED | RED: `Failed: DID NOT RAISE <class 'SystemExit'>` (`:175`) — verbatim; `[zero]` green |
| DS | none (report-only, D8 (d) and the stop line) | — | — |

C2's restarts pin, derived by READING the call sites (`grep -rn -F "load_voice_config" src` → `turn.py:111`, `web.py:59`, `cli.py:56`; then each caller's callers):
| reader added to `EXPECTED_BACKUP_YAML_READERS` | why (file:line) |
|---|---|
| `cobalt.voice.config.load_voice_config` | calls `load_backup_config()` after D3 (`config.py`) |
| `cobalt.voice.web.get_config` | `web.py:59` |
| `cobalt.voice.turn.default_deps` | `turn.py:111` |
| `cobalt.voice.cli.cmd_turn` | `cli.py:56`, and `_run` at `:49/:63/:65` |
| `cobalt.voice.cli._run` | `cli.py:70` `default_deps()` |
| `cobalt.voice.web.get_deps` | `web.py:66` `default_deps()` |
| `cobalt.voice.web.peer_gate` | `web.py:72` `get_config()` |
| `cobalt.voice.web.voice_turn` | `web.py:97` `get_config()`, `:118` `_run` |
| `cobalt.voice.web._run` | `web.py:86` `get_deps()` |
| `cobalt.voice.web._tap` | `web.py:127` `_run` |
| `cobalt.voice.web.voice_confirm` / `voice_cancel` | `web.py:132` / `:137` `_tap` |
| `cobalt.voice.web.status_lines` | `web.py:145` `get_config()` |
| `cobalt.voice.web.voice_status` | `web.py:154` `status_lines()` |
| `cobalt.voice.web.voice_startup` | `web.py:160` `get_config()` |
15 readers, all `cobalt.voice.*` — none outside `cobalt.voice.*` and the existing twelve. Entrypoints gained: `peer_gate`, `voice_turn`, `voice_confirm`, `voice_cancel`, `voice_status` (the `/voice/*` routes — `aset/web.py:90` `app.include_router(voice_web.router)`), `voice_startup` (`aset/web.py:91` startup hook) → all run inside `com.cobalt.aset`; `cmd_turn` → `cobalt voice turn`, an operator command (`grep -rn -F "voice" ops` → only the two `start_aset.sh` exports at `:35`, `:37`; no plist runs it). **Also changed in that same test (not named by the prompt, needed by it):** the `referrers` pin gains `cobalt.voice.web.<module>` (the route decorators' `Depends(peer_gate)`), `cobalt.aset.web.<module>` (`add_event_handler("startup", voice_web.voice_startup)`) and `cobalt.voice.cli.add_parser` (`set_defaults(func=cmd_turn)`); the `no_resident_read(...)` block becomes `no_resident_read("configs/cobalt/backup.yaml") is None` + `readers_of(...) == ["com.cobalt.aset"]` (the schema refuses both). `row.rule` = `"resident reads"`, read from `src/cobalt/jobs/restarts.py:204` (`rule = (rule + "; " if rule else "") + "resident reads"`). `test_backup_yaml_reader_proof_goes_red_through_any_wrapper` NOT edited.

Run `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_voice_tools.py tests/cobalt/test_voice_web.py tests/cobalt/test_voice_config.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_voice_fix_r1_runs.py tests/cobalt/test_voice_card_stop.py tests/cobalt/test_voice_turn.py tests/cobalt/test_voice_cli.py` → `15 failed, 250 passed in 9.02s` · exit 1. The 15: A1 8 · D3 1 · C2 3 · RUN-2 1 · RUN-4c 1 · RUN-7 oversize 1 — EXACTLY the named set; every other test passed (the A1 NOT-refused set 6/6, `:234`, `test_backup_yaml_reader_proof_goes_red_through_any_wrapper` ×3).
Committed `git add` (5 paths) + `git commit` → **`<red>` = `5a56a47e`** `wip(fix-r2): voice V1 fix r2 red tests — …`.

## D3 THE EDITS
Built: A1 · D3 · C2 · RUN-2 · RUN-4c · RUN-7 (the six code rows; DS is report-only).
- **A1** `tools.py` `_ORDER`: ONE alternative added, exactly `(?<!the )(?<!my )(?<!a )short (?-i:[A-Z]{1,5})\b|(exit|close out|close|get out of) (?-i:[A-Z]{1,5})\b`; existing alternatives and the sentence unchanged; the `:50-52` comment gains one sentence.
- **D3** `web.py` widget: `let … lines = [], device = [];` · `banner()` draws `lines.concat(device, extra || [])` · `:300` pushes to `device`. Status fetch unchanged.
- **C2** `config.py`: module import `from cobalt.backup.config import BackupConfigError, load_backup_config`; `backup_sources is None` → `[Path(p) for p in load_backup_config().sources]`, a `BackupConfigError` → `VoiceConfigError` naming it; the refusal runs through the existing `_check_path` loop. Docstring paragraph and the module docstring clause replaced (one sentence each, C2 / FINAL :118 / L42). `jobs.yaml`: `com.cobalt.aset` `reads:` gains `"configs/cobalt/backup.yaml"` with the one-line comment (the prompt's `_config` written as the real name `_CONFIG`, `voice/web.py:49`) and the removed entry's `because:` provenance as comment lines beside it; the `no_resident_reads` entry for it removed. `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_jobs_restarts.py` → `18 passed in 8.51s` — no `JobConfigError`; the walk's readers / entrypoints / referrers equal the D2 pins.
- **RUN-2** `card_stop.py`: `StopMoved(CardStateError)` carrying the fresh card; `set_card_stop(…, *, expect_from_stop=None)` raises it before `record_stop_edit` when the stop it reads differs; `__all__` gains `StopMoved`. `tools.py` `execute_stop` passes `expect_from_stop=pending.from_stop`; `StopMoved` → `TargetChanged(stop_dry_run(e.card, Decimal(pending.to_stop), ttl_s=ttl_s, now=…))`. The route passes nothing (unchanged).
- **RUN-4c** `turn.py`: after `except agent_mod.PlanFailed`, `except Exception as e` → `_Fail("voice_plan", f"Cobalt can't think right now ({type(e).__name__}).", red=True, detail=…)`.
- **RUN-7** `cli.py` `--audio`: bytes read once; `len > cfg.max_upload_bytes` → `_fail("the audio file <path> exceeds <n> bytes (max_upload_bytes)")` before the lock and any turn; the same bytes go into `TurnInput`.

Proofs:
- D2's command, byte for byte → `265 passed in 10.13s` · exit 0 → **0 failed**, no `xfailed` (the three RUN marks are gone).
- `git diff --stat 137c1928` → 12 paths, exactly the named set: `configs/cobalt/jobs.yaml`, `src/cobalt/aset/card_stop.py`, `src/cobalt/voice/{cli,config,tools,turn,web}.py`, `tests/cobalt/{test_jobs_restarts,test_voice_config,test_voice_fix_r1_runs,test_voice_tools,test_voice_web}.py` — `12 files changed, 185 insertions(+), 53 deletions(-)`.
- `git diff 137c1928 -- src configs` read WHOLE (7 files). It is identical to `git show d2963110 -- src configs` (the fix commit holds every src/config change: `7 files changed, 65 insertions(+), 33 deletions(-)`); hunks in order: `jobs.yaml` (+6 reads lines, −9 `no_resident_reads` lines) · `card_stop.py` (`StopMoved`, the keyword, the check, `__all__`) · `cli.py` (the one read + bound) · `config.py` (module docstring, import, docstring, the `backup_sources is None` block) · `tools.py` (comment, `_ORDER` alternative, `StopMoved` import, the try/except) · `turn.py` (the `except Exception` branch) · `web.py` (`device`, `banner`, `device.push`). `git show d2963110 -- src configs` is the verbatim record.
Committed `git add` (12 paths) + `git commit` → **`<fix>` = `d2963110`** (the 5 test paths were already at `5a56a47e`, so the commit carries the 7 src/config paths).
- `grep -rn -F "VaultWriter" src/cobalt/voice` → no hits (exit 1); `grep -rn -F "vaultwrite" src/cobalt/voice` → no hits (exit 1). No vault write path, none new (L28).

## D4 DEVDOCS AND SCOPE
Edited where behaviour changed, one to three sentences each, agent-authored: `docs/40 - DevDocs/cobalt/voice/{tools,web,config,turn,cli}.md` and `docs/40 - DevDocs/cobalt/aset/card_stop.md`. `config.md`'s "Backup sources — checked by the suite, not by the resident" paragraph REPLACED by "Backup sources — checked on every load, the resident's included" (C2). Committed `docs(voice-v1): fix r2 DevDocs (L75)` → `6 files changed, 38 insertions(+), 16 deletions(-)` → **`<tip>` = `d319e4f3`**.

## D6 LIVE-NOTE
On `d319e4f3`, D1's command byte for byte → `142 passed, 1 skipped, 15 warnings in 9.74s` · exit 0 → `<lp>` = 142, `<lf>` = 0, 0 errors. The one SKIPPED line is D1's (`tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`); none names `COBALT_LIVE_VAULT_ROOT`. GATE met.

## D7 OFFLINE
`ls /Users/cobalt/cobalt-wt/voice-v1/.env` → `ls: /Users/cobalt/cobalt-wt/voice-v1/.env: No such file or directory` (exit 1). D1's offline command byte for byte on `d319e4f3` → `2786 passed, 358 skipped, 1 xfailed, 20 warnings in 92.41s (0:01:32)` · exit 0 → `<p>` = 2786, `<f>` = 0, 0 errors; xfailed 1 (`43`'s own; the three fix r1 RUN marks are gone). `<p>` − `<bp>` = 14 = the new offline tests of D2 that pass (A1 8 + the readable short-side case 1 + D3 1 + C2's new test 1 = 11; the two renamed C2 tests replace their base versions) + the three former xfails. Skips unchanged at 358. GATE met.

## D8 WITH-DB
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1) — lock free.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/voice-v1/.env` (exit 0; never read or printed). `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly one line: `-rw-------  1 cobalt  staff  2186 Sep 24 21:36 /Users/cobalt/cobalt-wt/voice-v1/.env`. **`.env` ON DISK from here until (f).**
- (c) Deselect proof, `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider <the five ids>` → `5 failed, 5 warnings in 32.17s` · exit 1. Per id (failure headers at output lines 3 / 50 / 102 / 222 / 353):
  - `test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction` — FAILED `psycopg.errors.UndefinedTable: relation "voice_turns" does not exist`
  - `test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries` — FAILED, same
  - `test_voice_store.py::test_single_flight_under_two_real_connections` — FAILED, same
  - `test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both` — FAILED, same (at its cleanup `DELETE FROM voice_turns WHERE session_id = $1`, `test_voice_confirm.py:251` → `store.py:196`)
  - `test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` — FAILED: first `AssertionError: the upload never reached the scratch dir` (`test_voice_lifecycle.py:167` — the served turn could not create its row), then the cleanup `DELETE FROM voice_turns` → `UndefinedTable` (`:210`). It SIGKILLed only the servers it started.
  None passed, none skipped → `voice_turns` does NOT exist on `cobalt_dev`.
- (d) Command as run, on `d319e4f3`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` → `3129 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 169.22s (0:02:49)` · exit 0 → `<dp>` = 3129, `<df>` = 0, 0 errors; deselected 9 as expected (`TestMigrationRoundTrip` carries 2). `<dp>` − `36`'s 3115 = 14 = D7's delta. SKIPPED (6): `test_cards_picks.py:383` (S2-P2's `card_score` column is present on cobalt_dev), `test_cards_picks.py:396` (real S2-P2 0007 applied), `test_radar_evaluate.py:691`, `test_catalyst.py:365`, `test_predicate.py:262` (`COBALT_LIVE_VAULT_ROOT` not set — run at D6), `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC` not set). `test_voice_store.py`'s `test_forward_creates_the_table_user_side_and_rollback_drops_it_cleanly` and `test_no_bytes_column_in_either_catalog` are neither deselected nor in the SKIPPED list → RAN and passed (0 failed), applying `0017` inside their own transaction and rolling it back. No `cobalt db migrate`, before or after. GATE met.
- (e) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → `1 failed in 5.88s`, as expected: `AssertionError: every table's rows must stream through its own NAMED (server-side) cursor; …` `assert 28 == 29` — SHORT BY EXACTLY 1. The 28 named cursors listed run `cobalt_probe_archive_incidents` … `cobalt_probe_vault_writes`; NO `cobalt_probe_voice_turns`. **`0017: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 1)`.**
- (f) `rm /Users/cobalt/cobalt-wt/voice-v1/.env` (exit 0) → `ls /Users/cobalt/cobalt-wt/voice-v1/.env` → `ls: /Users/cobalt/cobalt-wt/voice-v1/.env: No such file or directory` (21:40 ET). **`.env: removed, proven gone (D8)`.**

## RESTARTS
RUN-R (L42 — C2 changes the registry's derivation, so the derivation is RUN).
- `uv run cobalt jobs restarts 137c1928..d319e4f3` → exit 0. Table: `configs/cobalt/jobs.yaml` → `registry; register, no restart`, `-`; the 6 `docs/40 - DevDocs/cobalt/…` → `DOCS`, `-`; `src/cobalt/aset/card_stop.py`, `src/cobalt/voice/{config,tools,turn,web}.py` → `static import reach`, `com.cobalt.aset,com.cobalt.radar`; `src/cobalt/voice/cli.py` → `static import reach`, `com.cobalt.radar`; the 5 test paths → `test/documentation; no resident`, `-`. Last line: `RESTARTS: com.cobalt.aset com.cobalt.radar`. As expected: voice src and `card_stop.py` derive `com.cobalt.aset` (and `com.cobalt.radar`, which imports `cobalt.cli`); `jobs.yaml` as the registry derives; tests and docs derive nothing.
- `uv run cobalt jobs restarts 04b05cd4..d319e4f3` → exit 1, `FAILED: RestartError: one or more changed paths were unclassified`. `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. UNCLASSIFIED (6, the same six `36` recorded — O11, the desk's): `configs/cobalt/agents/voice.yaml`, `configs/cobalt/modelaccess.yaml`, `configs/cobalt/voice.yaml` (UNCLASSIFIED CONFIG), `ops/start_aset.sh`, `pyproject.toml`, `uv.lock` (UNCLASSIFIED). Nothing new.
- What C2 now makes true: a later change to `configs/cobalt/backup.yaml` derives a `com.cobalt.aset` restart (`rule: resident reads`) — the D2 pin `test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart` proves it and is green at D7 / D8.

## CONTINUE
next: none — CLOSE done (red `5a56a47e`, fix `d2963110`, tip `d319e4f3`; all three suites green; `.env` removed; report committed at CLOSE).

## ESCALATE
1. **DESELECTS (fix r2's FIX row, L68): the eight `--deselect` ids of D8 (d), verbatim: `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` · `tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` · `tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (three carried from `14`) · `tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction` · `tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries` · `tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections` · `tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both` · `tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped` (five V1, proven at (c)).**
2. **L76 left five V1 with-DB tests UNRUN in this build (`D8` (c) proves why): the store round-trip and reaper, X-X13's two real-connection races, and X-E7, plus RUN-1's timing. Each needs `voice_turns` COMMITTED on a database. They run at the stacked L68 gate with `0017` applied and rolled back before its stop line (L76's second clause) — the desk's ruling (`37` ESCALATE 8 / 12), not this build's.**
3. **OUT OF SCOPE, carried: D6 — `tests/cobalt/test_radar_panel_cards.py` changed outside `43`'s list; its revert would turn the `/radar` byte-equality red, so it was NOT taken; the desk rules the boundary. X-E10 — the FINAL's column routes 'an unexpected native / GPL package' to TRIBUNAL ROUND 2 (FINAL `:285`); not this build's.**
4. **The FIX rows moved on file evidence only (`37` FOR THE CLASSIFIER, 3 HOLD, + C2 and three red RUNS, classified in `reports/voice-v1-fix-r2-draft-2026-09-24.md`). The red: D2 offline on `5a56a47e`, green on `d2963110`. The check is `55` — ROUND 3, THE LAST (Opus 5.5 + Grok, with Sol from Sep 26th, 2026 6:47 AM); a HOLD there goes to him as ONE message (override or design round), never a round 4. Its packet carries this report's executed output of all three suites and RUN-R (L68). The deploy's L68 gate re-proves them on the tree that ships. The DEVICE SESSION (E1 E3 E5 E8 X3) stays OWED before any ship; D3's runtime behaviour on a real device is part of it (no JS runner here).**
5. **C2 test-edit scope (D2):** `test_backup_yaml_readers_are_pinned_and_derive_the_aset_restart` also needed its `referrers` pin (+ `cobalt.voice.web.<module>`, `cobalt.aset.web.<module>`, `cobalt.voice.cli.add_parser`) and its `no_resident_read` block (→ `is None` + `readers_of == [com.cobalt.aset]`) changed — the prompt named the reader set, entrypoints, rule and restarts; these two are the same test's pins that the schema's own path forces. No other test touched.
6. **C2 widens static import reach, by design of the one loader:** `cobalt.voice.config` now imports `cobalt.backup.config` at module level (the monkeypatch target the prompt names), so `com.cobalt.aset`'s import reach includes the `cobalt.backup` package (its `__init__` imports `.restic`). By the classifier's static-import rule (a READING — no `src/cobalt/backup/` path is in this range, so it was not run), a `src/cobalt/backup/*.py` change now derives a `com.cobalt.aset` restart as well as the `configs/cobalt/backup.yaml` one — true of the running process, which does import that code. The deploy prompt names it.
7. **The `jobs.yaml` comment** carries the prompt's text with `voice/web.py _config` written as the real module global `_CONFIG` (`voice/web.py:49`).
8. **L74:** one block recorded once under `## L74`, not followed.

VOICE V1 FIX R2 BUILT d319e4f3 | on 137c1928 | red 5a56a47e | offline 2786/0 | with-DB 3129/0 | live-note 142/0 | .env: removed | 0017: rolled back | FIX: 7 of 7 | RUNS: 1 | deselects: TestMigrationRoundTrip, test_every_user_table_carries_user_id_not_null_with_the_guc_default, test_rows_reach_the_probe_through_a_named_cursor_in_batches, test_store_round_trip_and_single_flight_in_the_suite_transaction, test_the_reaper_fails_stale_rows_and_never_retries, test_single_flight_under_two_real_connections, test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both, test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped | ESCALATE: 8
