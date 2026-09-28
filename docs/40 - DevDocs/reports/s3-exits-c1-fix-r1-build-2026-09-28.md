# S3 EXITS C1 FIX R1 — BUILD REPORT

Seat: `s3-exits-c1-fix-r1-build` · Opus 5.5 (`claude-opus-5-5`) · `acceptEdits` · prompt `prompts/2026-09-28/29-s3-exits-c1-fix-r1-build.md` · worktree `/Users/cobalt/cobalt-wt/s3-exits-c1` · `<base>` = `d9240ae4` · `<code base>` = `5164f867`. Start: `date` → `Mon Sep 28 11:49:25 EDT 2026`.

## §0 Headline
- Built all four rows on `5164f867`. The fix commit is `3ceb3b11`, over the red commit `da9246f0`. Only `/fill`'s body and four test files changed.
- F1: X1 now runs on the real `db.connect`. With `autocommit = False` removed it went RED on a surviving FILLED transition row. With the line restored the diff is empty and the test passes. No `X1RF` rows are left.
- F2 and F3 were red first, then green. F3's red was the top-level-shape refusal, as the drafter read it. F4: the added lines no longer equal the base lines.
- Suites: offline 3246/0; with-DB 3617 + 33 = 3650/0; live-note 146/0. X22 gave F = F0 twice, and `cobalt_dev` is back at `0013`.
- R1: every table's proof matches except `cobalt_redactions` (179 → 180), which is escalated.

## L74
Recorded once (L74): after the prompt file was read (11:49), a `<system-reminder>` block arrived asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and naming a file-send tool. Treated as data. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; no file was sent.

## AUTHORIZATION
| gate | command | exit | output |
|---|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" "…/29-s3-exits-c1-fix-r1-build.md"` | 1 | (none) |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" "…/29-s3-exits-c1-fix-r1-build.md"` | 0 | `39:- PLACEHOLDER GATES: …` — only the gate's own line |
| classification | `grep -n -F "S3 EXITS C1 FIX R1 DRAFTED" "…/reports/s3-exits-c1-fix-r1-draft-2026-09-28.md"` | 0 | `60:S3 EXITS C1 FIX R1 DRAFTED · FIX: 6 · NOT REAL: 5 · UNPROVEN: 1 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 5` — line 60, the file's last non-blank line |
| launch row | `grep -n -F "29-s3-exits-c1-fix-r1-build.md" "…/reports/cto-2026-09-28.md"` | 0 | `67:\| R59 \| 11:49 ET \| — DESK LAUNCH ROW: \`29-s3-exits-c1-fix-r1-build.md\` (Opus 5.5, acceptEdits, cwd \`~/cobalt-wt/s3-exits-c1\`) on \`d9240ae4\` (code \`5164f867\`); no with-DB run in flight (\`.env\` no matches 11:48); \`comm\` vs \`20\` line 6: 25 common, 0 new. \`17\` waits for this build's lock release (L76). \| LAUNCHED \`5642d589\` 11:49 \|` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"29-s3-exits-c1-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` | 0 | `73680ff7e233e72f363fe2f942ffcb3fabb1505a` |

Authorization: HOLDS (R59 names this file, carries `d9240ae4` and `no with-DB run in flight`; committed in `73680ff7`). Note: R59 says `25 common`; this prompt's line 7 says `27 common (24 allow + 3 deny)` — recorded under `## ESCALATE`, not a gate.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 11:49:25 EDT 2026` |
| branch clean | `git status --short --branch` | 0 | `## s3/exits-c1` |
| base | `git log --oneline -1` | 0 | `d9240ae4 docs(s3-c1): S3 exits C1 build report — 5164f867` |
| no `.env` here | `ls /Users/cobalt/cobalt-wt/s3-exits-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s3-exits-c1/.env: No such file or directory` |
| lock free | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| migrations | `ls src/cobalt/db_migrations` | 0 | `0021_legs.sql`, `0021_legs.rollback.sql` present; highest = `0021` (list: 0001 … 0011, 0013, 0014, 0015, 0017, 0021, `cli.py`, `placement.py`) |
| symbol | `grep -n "def mark_filled" src/cobalt/aset/store.py` | 0 | `198:    def mark_filled(` |
| symbol | `grep -n -F "conn.autocommit = False" src/cobalt/aset/store.py` | 0 | `119:        conn.autocommit = False` · `268:        conn.autocommit = False` (268 is inside `mark_filled`) |
| symbol | `grep -n "def _update_fill_cache" src/cobalt/aset/store.py` | 0 | `360:    def _update_fill_cache(self, conn, row_id: int, fill: FillRecompute) -> None:` |
| symbol | `grep -n "REAL_CONNECT" tests/cobalt/conftest.py` | 0 | `57:REAL_CONNECT = db.connect` · `158:    real = REAL_CONNECT(env.DEV_DB_NAME, side=db.Side.SYSTEM)` · `215:        conn = REAL_CONNECT(dbname, side=side)` |
| symbol | `grep -n -F "save_fill_update(" src/cobalt/aset/web.py` | 0 | `1128:        note_path, note_write = save_fill_update(cfg, fill_result, orig_timestamp)` |
| symbol | `grep -n "DRIFT_NOT_EVALUATED" src/cobalt/aset/web.py` | 0 | `71:from cobalt.settings.fills import DRIFT_NOT_EVALUATED` · `1159:        banner += f'<div class="warn">⚠ {html.escape(DRIFT_NOT_EVALUATED)}</div>'` |
| symbol | `grep -n "FILE_ROOT =" src/cobalt/settings/card.py` | 0 | `74:FILE_ROOT = "card_settings"` |
| symbol | `grep -n "class _FillRoute" tests/cobalt/test_fill_c1_offline.py` | 0 | `294:class _FillRoute:` |
| restarts empty | `uv run cobalt jobs restarts d9240ae4..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |

## E0 BASELINE
On `<base>` `d9240ae4` (no src edit during the run; pytest collected the tree at 11:51, before the first test edit of this build — the E2 test edits landed after collection, as C1's E0 recorded for its own).
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, 11:51 → ~11:59) → **`3244 passed, 409 skipped, 1 xfailed, 20 warnings in 554.05s (0:09:14)`**, exit 0 — 0 failed, 0 errors (= C1's `<p>` 3244). Read `date` → `Mon Sep 28 11:59:41 EDT 2026`.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (foreground, ~11:57, none of its four files edited) → **`146 passed, 1 skipped, 15 warnings in 25.63s`**; the one skip: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests only; no src file edited. Written:
- **F1** `tests/cobalt/test_fill_transaction_db.py::test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back` — module-level `REAL_CONNECT = _db.connect` (bound at import, before `dev_db_tx` patches it; the `test_voice_store.py` `RAW_CONNECT` precedent — a `from conftest import` is ambiguous with three `conftest.py` in `tests/`); the test asserts `db.connect is not REAL_CONNECT`, then `monkeypatch.setattr(db, "connect", REAL_CONNECT)` so the store, `CardStore` and every read open real connections. It does NOT use the `aset` fixture (no `ensure_schema`, no `apply_0021` inside the suite transaction — that DDL would hold locks the real connections wait on). Two constructed manual cards, ticker `X1RF`, `legs_db_support`'s `ENTRY` / `STOP`, walked WATCH → ARMED → TRIGGERED on the real factory. Execution order: **(b) first, then (a)** — so a fill path that writes outside its transaction goes red on what (b) left behind (the transition row, the leg), not on the control; the (b) exception text (`no_such_column`) is asserted AFTER the state reads for the same reason. (b) reads on a fresh `REAL_CONNECT` per statement: FILLED transition rows 0, legs 0, state TRIGGERED, picks = the pre-fill count, `actual_fill` NULL. (a) the control on the second card: FILLED, one FILLED row, one leg, `actual_fill` = the typed price, `pick_recorded` true, picks = 1. `finally`: one real connection deletes by card id `legs`, then `picks`, then `aset_sizings` (`card_transitions` / `card_stop_edits` cascade — `ON DELETE CASCADE`, `cards/migrations/0001_card_transitions.sql:13`, `0002_card_stop_edits.sql:17`), then asserts zero `aset_sizings` rows and zero joined `legs` rows for `X1RF`. Not run here (real `0021` needed: W (c3) / (c3m)).
- **F2** `tests/cobalt/test_fill_c1_offline.py::test_a_note_failure_after_the_commit_keeps_the_p_missing_banner` (`[p missing]`) and `::test_a_note_failure_after_the_commit_keeps_the_drift_warning` (`[P = 20, the 27 % fill]`; the success path's drift warning = `engine.STRUCTURAL_WARNING` in the result card, `aset/web.py:825-828`), both through `_FillRoute.install` with `save_fill_update` replaced by one raising `DailyNoteRefused("constructed note refusal")`.
- **F3** `tests/cobalt/test_s3_c1_experiments.py:76`: `pytest.raises(TraderSettingsError, match="unknown card setting 'fills.drift_warning_pct'")`; the constructed file unchanged.

Offline red, `date` → `Mon Sep 28 11:54:02 EDT 2026`: `uv run pytest -q -rf --tb=line -p no:cacheprovider --color=no tests/cobalt/test_fill_c1_offline.py tests/cobalt/test_s3_c1_experiments.py` → exit 1, **`3 failed, 39 passed, 3 skipped in 0.42s`**:
- F2 `[p missing]` — `test_fill_c1_offline.py:392`: `AssertionError: <div class="failed">FAILED` / `constructed note refusal</div>` / `assert 'marked FILLED' in '<div class="failed">FAILED\nconstructed note refusal</div>'` (only the failure banner renders; no `marked FILLED`, no `DRIFT_NOT_EVALUATED`).
- F2 `[P = 20]` — `test_fill_c1_offline.py:403`: the same — `assert 'marked FILLED' in '<div class="failed">FAILED\nconstructed note refusal</div>'` (no drift warning either).
- F3 — `test_s3_c1_experiments.py:76`: `E   cobalt.settings.card.CardSettingsError: …/card.yaml: expected exactly one top-level mapping 'card_settings'` → `AssertionError: Regex pattern did not match.` / `Expected regex: "unknown card setting 'fills.drift_warning_pct'"` — the top-level-shape refusal, as the drafter read it. F3 is a real FIX (not "already held").

**F4** equality read at `<code base>` (the file is unchanged since `5164f867`; values not quoted, L32): `grep -n -F "<entry value>" tests/cobalt/test_aset_web.py` → `:101` (base `BASE_SIZE_FORM`), `:183` (base comment), `:196`, `:581`; `grep -n -F "<stop value>" …` → `:102` (base), `:196`, `:581`; `grep -n -F "\"<ticker>\"" …` → `:97`, `:103`, `:129`, `:195`, `:323`, `:516`, `:531`, `:540`, `:580`.
| added line (C1, per `git diff c1dc476d 5164f867 -- tests/cobalt/test_aset_web.py`) | fields | base line | equal |
|---|---|---|---|
| `:195-197` (the D2 replay card row: ticker, entry, stop, and the derived per-share risk / shares / used risk) | ticker, entry, stop | `:97`, `:101`, `:102` (`BASE_SIZE_FORM`); `:183` (comment) | **yes** |
| `:580-581` (`_stub_fill_route`'s `SizingInput`) | ticker, entry, stop | `:97`, `:101`, `:102`; `:183` | **yes** |

## E3 THE ROWS
`wip(s3-c1-fix-r1): red` = `da9246f0` (tests only, before any src edit). Fix commit `3ceb3b11` `fix(s3-c1): fix r1 — X1 on the real factory, the drift outcome after a note failure, X-S card-load proof, constructed values (L75)` (12:00:12) — `git diff --stat` before it: `src/cobalt/aset/web.py | 35`, `tests/cobalt/test_aset_web.py | 10`, `tests/cobalt/test_s3_c1_experiments.py | 4` (32 insertions, 17 deletions).
| row | built | file:line at `3ceb3b11` |
|---|---|---|
| F1 | the test only (written at E2, `da9246f0`); no src change — the code holds, the proof was missing. Its red is W (c3m). `legs_db_support.py` unchanged (the test builds its `X1RF` `SizingInput` itself). | `tests/cobalt/test_fill_transaction_db.py` |
| F2 | `/fill` body only: `save_fill_update` moved out of the pre-commit `try` into its own `try` after it (`aset/web.py:1141-1154`). Any exception there renders `_failed(…)` — the same text rule as the pre-commit handler (`str(e)` for the six named refusal types, `Type: e` otherwise) — plus `aset_sizings id <n> marked FILLED — the daily-note write failed after the DB commit; the FILL UPDATE is NOT in the journal.`; then the shared tail every post-commit path runs: `_pick_banner` (`:1168`), the exact `DRIFT_NOT_EVALUATED` banner when `drift_warned is None` (`:1169-1172`), and `_result_card(original, form, fill=fill_result)` (`:1173-1177`, the success path's render, so a warned drift shows `STRUCTURAL_WARNING`). Every refusal before `mark_filled` returns is the unchanged `try`/`except` (`:1061-1139`). No other route, no render helper, no new route. The pick banner is kept on the note-failure path as on success (it is the same shared tail). | `src/cobalt/aset/web.py` |
| F3 | the constructed file now `card_settings:\n  fills.drift_warning_pct: 20\n` (under `FILE_ROOT`, `settings/card.py:74`), so the refusal is `settings/card.py:270-273` "unknown card setting". | `tests/cobalt/test_s3_c1_experiments.py:74-79` |
| F4 | the two C1-added places get constructed values: ticker `TEST`; entry / stop `220.0000` / `218.0000` (the row's per-share risk `2.0000`, shares `30`, used risk `60.00` = 60 / 2). The posted fills are unchanged base-form values: the absurd fill stays > 5 % from entry (typo guard refuses), the corrected fill stays < 5 % (passes the guard). Base lines `:97`, `:101`, `:102`, `:103`, `:129`, `:183` and every other line C1 did not add are untouched. | `tests/cobalt/test_aset_web.py:195-197`, `:580-581` |

F4 after-read: `grep -n -F "<entry value>" tests/cobalt/test_aset_web.py` → `:101`, `:183` only; `grep -n -F "<stop value>" …` → `:102` only — the added lines no longer carry them: **`equal: no`** for both.

Offline re-run of the E2 command on the edited tree → `..........................................sss` **`42 passed, 3 skipped in 0.50s`**, exit 0, 0 failed. `-rA` run (`uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_aset_web.py tests/cobalt/test_fill_c1_offline.py tests/cobalt/test_s3_c1_experiments.py -k "note_failure or card_load_path or TestAbsurdFill or TestPickNotRecorded"`) → `9 passed, 73 deselected in 0.40s`; PASSED lines:
```
PASSED tests/cobalt/test_aset_web.py::TestAbsurdFillRejectAtWebLayer::test_replay_d2_absurd_fill_refused_no_note_write
PASSED tests/cobalt/test_aset_web.py::TestAbsurdFillRejectAtWebLayer::test_corrected_fill_passes_the_guard
PASSED tests/cobalt/test_aset_web.py::TestAbsurdFillRejectAtWebLayer::test_fill_with_a_card_row_id_reaches_the_store
PASSED tests/cobalt/test_aset_web.py::TestPickNotRecordedBanner::test_fill_form_route[True]
PASSED tests/cobalt/test_aset_web.py::TestPickNotRecordedBanner::test_fill_form_route[False]
PASSED tests/cobalt/test_aset_web.py::TestPickNotRecordedBanner::test_card_move_no_longer_fills
PASSED tests/cobalt/test_fill_c1_offline.py::test_a_note_failure_after_the_commit_keeps_the_p_missing_banner
PASSED tests/cobalt/test_fill_c1_offline.py::test_a_note_failure_after_the_commit_keeps_the_drift_warning
PASSED tests/cobalt/test_s3_c1_experiments.py::test_xs_the_card_load_path_refuses_the_drift_key
```

## W THE THREE SUITES
`<tip>` = `3ceb3b11` (the fix commit; every suite below runs on that tree).
- **(a) offline:** `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, 12:00 → 12:09, no `.env`) → **`3246 passed, 410 skipped, 1 xfailed, 20 warnings in 551.37s (0:09:11)`**, exit 0 — 0 failed, 0 errors → **`<p>` = 3246** (= 3244 + F2's two offline tests; +1 skipped = F1, with-DB). Read 12:09:38.

`<FP>` — copied whole from `prompts/2026-09-27/48-stack-seam-fix-r2-build.md` line 103, typed exactly:
```
COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"
```
- **(b) LOCK:** `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` · `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c1/.env` · `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 28 12:09 /Users/cobalt/cobalt-wt/s3-exits-c1/.env` · **L76 lock taken 12:09:42**. `ls -la …/s3-exits-c1/.env` (LISTED), `<FP>` → `cols	rels	views_md5` / `664	35	272c95bbb12241e3611e4b36326ccf87` → **`<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= C1's F0). `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → **`<P0>`**, WHOLE:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.02
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.68
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   179          1d147fe7e1e2bf7ee0733886fc9ec5b4   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
legs                 user    -        -            -                                  0.00
missed               user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
movers_daily         system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
picks                user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.01
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
30 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 28 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.8 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 3ceb3b11 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/s3-exits-c1
```
`legs` and `voice_turns` absent (`-`): `cobalt_dev` is at **`0013`**. The one dirty path is this untracked report.
- **(c) PASS 1 at `0013`** — `ls -la …/.env` (LISTED), started 12:10:24 (`date`), background; the executed command WHOLE (C1 report `## W THE THREE SUITES` (c), byte for byte — 48 W (c1)'s eight `--deselect` arguments + the two C1 files):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py
```
→ **`3617 passed, 6 skipped, 33 deselected, 1 xfailed, 20 warnings in 641.13s (0:10:41)`**, exit 0; read 12:21:17 → **`<d1>` = 3617** (= C1's 3615 + F2's two). 33 deselected = 9 (48's) + 24 (the two C1 files, now incl. F1). The six SKIPPED lines are C1's known set verbatim: `test_cards_picks.py:388` (card_score present), `:401` (real 0007 applied), `test_radar_evaluate.py:695`, `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC`), `test_catalyst.py:365`, `test_predicate.py:262`.
- **(c2) FORWARD:** `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate` (foreground, timeout 600000) → `cobalt db migrate — FORWARD on cobalt_dev`; `-- applying` `0001_schemas.sql` … `0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0017_voice_turns.sql`, `0021_legs.sql` in that order; proof table: `legs  user  - -> user  - -> 0 … - -> d41d8cd9  CREATED`, `voice_turns  user  - -> user  - -> 0 … CREATED`, every other table `OK` (e.g. `aset_sizings 1 -> 1 0824685c -> 0824685c OK`, `card_transitions 4 -> 4 f181e76b -> f181e76b OK`, `cobalt_redactions 180 -> 180 5acf3646 -> 5acf3646 OK`); `30 table(s) proven; … content UNCHANGED on every table.`; `code: 3ceb3b11 (DIRTY: 1 path(s))`. No `CHANGED`. **`dev forward: APPLIED 12:21:32`**. `ls -la …/.env` (LISTED), `<FP>` → `773	38	126f2d6983fa59f9d0eaaff7da7dd29c` → **`<F1>` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`** (= C1's F1).
- **(c3) PASS 2 at `0021`:** `ls -la …/.env` (LISTED), started 12:22:00, background; the executed command WHOLE (C1 report (c3), byte for byte — 48 W (d)'s nine ids, the two C1 files, `-rA` last):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py -rA
```
→ **`33 passed, 5 warnings in 136.60s (0:02:16)`**, exit 0, no SKIPPED line; read 12:24:22 → **`<d2>` = 33** (= C1's 32 + F1). **`<d>` = 3617 + 33 = 3650.** Every PASSED line:
```
PASSED tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips
PASSED tests/cobalt/test_tenancy.py::TestMigrationRoundTrip::test_the_proof_table_names_every_ruled_table
PASSED tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default
PASSED tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches
PASSED tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction
PASSED tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries
PASSED tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections
PASSED tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both
PASSED tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
PASSED tests/cobalt/test_legs_db.py::test_an_update_is_refused_by_the_append_only_trigger
PASSED tests/cobalt/test_legs_db.py::test_a_second_original_of_one_seq_is_refused_by_the_index
PASSED tests/cobalt/test_legs_db.py::test_a_second_original_entry_is_refused_whatever_its_seq
PASSED tests/cobalt/test_legs_db.py::test_a_correction_and_a_correction_of_a_correction_are_accepted_and_the_view_shows_one_row_per_seq
PASSED tests/cobalt/test_legs_db.py::test_user_id_defaults_from_the_tenant_guc
PASSED tests/cobalt/test_legs_db.py::test_a_trading_log_row_needs_its_import_id_and_no_other_source_carries_one
PASSED tests/cobalt/test_legs_db.py::test_held_stated_lives_only_on_an_entry_correction
PASSED tests/cobalt/test_legs_db.py::test_sheet_mismatch_is_on_the_original_entry_and_nowhere_else
PASSED tests/cobalt/test_legs_db.py::test_the_value_checks_hold
PASSED tests/cobalt/test_legs_db.py::test_card_stop_edits_kind_defaults_to_edit_and_refuses_anything_else
PASSED tests/cobalt/test_legs_db.py::test_0021_applies_twice
PASSED tests/cobalt/test_fill_transaction_db.py::test_a_fill_writes_the_transition_the_entry_leg_and_the_cache_together
PASSED tests/cobalt/test_fill_transaction_db.py::test_x1_a_failing_cache_update_rolls_the_whole_fill_back_on_an_autocommit_factory
PASSED tests/cobalt/test_fill_transaction_db.py::test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back
PASSED tests/cobalt/test_fill_transaction_db.py::test_a_fill_with_no_price_is_refused_and_writes_nothing
PASSED tests/cobalt/test_fill_transaction_db.py::test_a_manual_fill_with_a_null_structural_stop_succeeds_and_its_leg_carries_the_card_stop
PASSED tests/cobalt/test_fill_transaction_db.py::test_sheet_mismatch_is_true_with_nothing_attested
PASSED tests/cobalt/test_fill_transaction_db.py::test_sheet_mismatch_is_false_when_the_attested_sheet_is_the_day_modes_sheet
PASSED tests/cobalt/test_fill_transaction_db.py::test_sheet_mismatch_is_true_when_the_attested_sheet_is_another_sheet
PASSED tests/cobalt/test_fill_transaction_db.py::test_the_27_percent_fill_warns_at_p20_and_not_at_p30[20-True]
PASSED tests/cobalt/test_fill_transaction_db.py::test_the_27_percent_fill_warns_at_p20_and_not_at_p30[30-False]
PASSED tests/cobalt/test_fill_transaction_db.py::test_p_missing_records_the_fill_and_leaves_the_warning_unevaluated
PASSED tests/cobalt/test_fill_transaction_db.py::test_market_reset_refuses_the_fill_and_writes_nothing
PASSED tests/cobalt/test_fill_transaction_db.py::test_for_date_keeps_its_columns
```
F1's PASS includes its control (a): the real fill of the second `X1RF` card asserted `pick_recorded` true and picks = 1 — the fill path DOES write a pick for a manual card (`cards/store.py:544` `_record_pick` after the FILLED hop → `cards/picks.py:244` `record_pick`, no origin condition), so (b)'s "picks = pre-fill count (0)" is a real negative.
- **(c3m) F1 MUTATION RED (L70):** Edit `src/cobalt/aset/store.py` — deleted the one `conn.autocommit = False` line in `mark_filled` (`:268`). `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider "tests/cobalt/test_fill_transaction_db.py::test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back"` → exit 1, **RED**:
```
>           assert after["filled_rows"] == 0, f"a FILLED transition row survived the failed fill: {after}"
E           AssertionError: a FILLED transition row survived the failed fill: {'state': 'FILLED', 'actual_fill': None, 'filled_rows': 1, 'legs': 0, 'picks': 0}
E           assert 1 == 0
tests/cobalt/test_fill_transaction_db.py:263: AssertionError
FAILED tests/cobalt/test_fill_transaction_db.py::test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back - AssertionError: a FILLED transition row survived the failed fill: {'state':...
1 failed in 0.35s
```
— on the real factory, without `autocommit = False`, the FILLED transition and the card state were durable before the failure (the leg writer then refused the autocommit connection, so no leg). Edit restored the line; `git diff -- src/cobalt/aset/store.py` → **empty** (no output, exit 0). Re-run of the same id (`ls -la …/.env` LISTED first) → `PASSED tests/cobalt/test_fill_transaction_db.py::test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back` / **`1 passed in 0.35s`**. Cleanup proof, each after `ls -la …/.env` (LISTED): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT count(*) FROM aset_sizings WHERE ticker = 'X1RF'"` → `count` / **`0`**; `COBALT_ENV=dev uv run cobalt db query --side user "SELECT count(*) FROM legs l JOIN aset_sizings a ON a.id = l.card_id WHERE a.ticker = 'X1RF'"` → `count` / **`0`** (12:24:38). `design-changing: no`.
- Note: `cobalt_redactions` read `179` rows in `<P0>` (12:09) and `180 -> 180` at the forward (12:21) — the row count grew between the two reads, before any migration statement (the forward's BEFORE probe already says 180). Carried to (f2).
- **(f) ROLLBACK #1:** `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `cobalt db migrate — ROLLBACK on cobalt_dev`; `-- applying 0021_legs.rollback.sql`, `0017_voice_turns.rollback.sql`, `0015_shadow_agreement_stale.rollback.sql`, `0014_radar_handicap.rollback.sql`; `legs  user  user -> -  0 -> - … DROPPED`, `voice_turns … DROPPED`, every other table `OK`; `content UNCHANGED on every table.` `ls -la …/.env` (LISTED), `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` → **`<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`** (12:25:25).
- **(c4) X22 (information):** after rollback #1, `<FP>` = `<F0>` (above). FORWARD again: `COBALT_ENV=dev uv run cobalt db migrate` → the same 16 `-- applying` lines ending `0021_legs.sql`, `legs … CREATED`, `voice_turns … CREATED`, every other table `OK`, `content UNCHANGED on every table.` — **`dev forward: APPLIED 12:25:40`**; `<FP>` → `773	38	126f2d6983fa59f9d0eaaff7da7dd29c` (= `<F1>`). ROLLBACK #2: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `0021`, `0017`, `0015`, `0014` reversed, `legs … DROPPED`, `voice_turns … DROPPED`, `content UNCHANGED on every table.` (12:25:57); `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` → **`cobalt_dev: 0013 — F2 = F0`** once more. **`X22: forward, back, forward, back — F = F0 twice`**; `design-changing: no`.
- **(e) live-note:** `ls -la …/.env` (LISTED), `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 25.56s`**; the one skip `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT` → **`<l>` = 146**.
- **(f2) RUN R1's row proof:** `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → **`<P2>`**, WHOLE:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.63
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   180          5acf3646ea44438bed7e762ecd328ee7   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
legs                 user    -        -            -                                  0.00
missed               user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
movers_daily         system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
picks                user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.01
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.01
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
30 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 28 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.7 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 3ceb3b11 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/s3-exits-c1
```
  `<P0>` vs `<P2>`, rows + digest, table by table — EQUAL: `archive_incidents`, `archive_progress`, `aset_sizings` (1 · `0824685c…`), `bars` (1043443 · `2769919a…`), `card_dot_taps`, `card_dots`, `card_stop_edits` (1 · `7599f9ab…`), `card_transitions` (4 · `f181e76b…`), `cobalt_email_sends` (2), `cobalt_jobs` (13), `cobalt_kill_switch` (1), `day_modes` (2 · `f2ffb4d4…`), `desk_grade`, `desk_packet`, `desk_regime`, `legs` (absent both), `missed`, `movers_daily`, `picks` (0 · empty digest), `radar_membership`, `radar_pool`, `radar_score`, `radar_score_receipt`, `radar_score_run`, `session_blocks` (6), `traders` (1), `vault_overrides` (6), `vault_writes` (187), `voice_turns` (absent both) — 29 of 30. DIFFERENT: **`cobalt_redactions` `179 · 1d147fe7e1e2bf7ee0733886fc9ec5b4` → `180 · 5acf3646ea44438bed7e762ecd328ee7`** → ESCALATE `R1: cobalt_redactions 179 1d147fe7… → 180 5acf3646…`. The change was already present at the forward's BEFORE probe (12:21, `180 -> 180`), so it happened between 12:09 and 12:21, during pass 1; no migration step changed it (every migrate's before/after row is `180 -> 180 OK`). Not attributed from reads: `grep -rln "cobalt_redactions" src tests` → `src/cobalt/redact/store.py` (the writer) and two tests (`test_migrate_proof.py`, `test_tenancy.py`, both pass-2-only and run later). C1's own `<P0>` at 10:00 read `177`, so this table also grew between C1's run and this one.
- **Lock (d):** `rm /Users/cobalt/cobalt-wt/s3-exits-c1/.env`; `ls /Users/cobalt/cobalt-wt/s3-exits-c1/.env` → `ls: /Users/cobalt/cobalt-wt/s3-exits-c1/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — **`.env: removed, proven gone (W) — L76 lock released 12:26:45`** (held 12:09:42 → 12:26:45). `aset/store.py` = the commit (`git diff` empty, (c3m)); `0021` not applied.

## RESTARTS
`uv run cobalt jobs restarts d9240ae4..3ceb3b11` (explicit shas; the untracked report is outside the range), exit 0 — the table WHOLE:
```
path	change	rule	restart
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_aset_web.py	M	test/documentation; no resident	-
tests/cobalt/test_fill_c1_offline.py	M	test/documentation; no resident	-
tests/cobalt/test_fill_transaction_db.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c1_experiments.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row.

## SEAM FOR C2
Re-issued whole; every `file:line` read on `<tip>` `3ceb3b11`. This fix changed no file below other than `aset/web.py` (`/fill` body) and the tests. Each line is re-cited, not carried over from C1.
- **The leg writer** `src/cobalt/cards/legs.py:38` `insert_entry_leg(conn, card_id, *, shares, price, at, flag, price_source, price_asof, source, stop_in_force, session, account_mode, day_mode_id, attested_sheet, sheet_mismatch) -> int`. Connection rule (`:30` `_assert_in_transaction`, refusal `:31-34`): it runs only on the caller's open transaction and refuses a connection with `autocommit` true. It never opens, commits, rolls back or closes. `ENTRY_SEQ = 0` (`:27`). C2 adds here: the exit-leg writer, the ONE running-share function, the correction writer and the S-HELD writer.
- **THE fill** `src/cobalt/aset/store.py:198` `mark_filled(row_id, *, price, shares, flag, price_source, price_asof, source, now=None, drift_settings=None) -> FillOutcome`; `FillOutcome` is at `:38`. Transaction shape:
  - price and shares are refused before any connection is opened;
  - config and the ladder are read;
  - `conn = self._connect()` (`:267`), then `conn.autocommit = False` (`:268`);
  - `SELECT * FROM aset_sizings WHERE id = %s FOR UPDATE` (`:271`);
  - `SizingResult.from_card` (`:283`), P (`:284`), `compute_fill_recompute` (`:285`);
  - `CardStore.fill(conn=conn)` (`:287`), `_attestation` (`:307`), `legs.insert_entry_leg` (`:308`), `_update_fill_cache` (`:325`, def `:360`);
  - ONE `conn.commit()` (`:326`); `except BaseException: conn.rollback(); raise` (`:327-329`).
  
  **F1 proved this shape on the real factory:** without `:268`, the FILLED transition survives a failed fill ((c3m) red).
- **The lock statement:**
  - `transition()` takes it at `cards/store.py:276-277`: `SELECT state, grade, risk_budget, shares, used_risk FROM aset_sizings WHERE id = %s FOR UPDATE`.
  - `fill(conn=…)` reads `SELECT state, origin FROM aset_sizings WHERE id = %s` (`cards/store.py:493`) on the caller's transaction, which is already locked.
  - `mark_filled` takes `SELECT * … FOR UPDATE` (`aset/store.py:271`).
  - Signatures: `fill()` at `cards/store.py:429` (`conn=None` `:438`); `transition()` at `:239` (`conn=None` `:249`).
- **DDL as applied** (`src/cobalt/db_migrations/0021_legs.sql`):
  - table `"user".legs` `:37`;
  - `legs_one_original_per_seq` `:71`; `legs_one_original_entry` `:73`;
  - trigger `legs_append_only` → `"user".refuse_row_update()` `:83`;
  - view `"user".legs_current_v` `:93`.
  
  Proven on `cobalt_dev` again by pass 2 (`test_legs_db.py`, 11 PASSED) and X22 (F = F0 twice).
- **`card_stop_edits.kind`:** `0021_legs.sql:104`, `TEXT NOT NULL DEFAULT 'edit'`, `CHECK (kind IN ('edit', 'reset'))`. No writer sets `reset` yet.
- **`drift_warning_pct` / `drift_warned`:** columns at `0021_legs.sql:113-114`, written only by `_update_fill_cache` (`aset/store.py:360`).
  - Engine: `aset/engine.py:266`; the comparator is at `:310`; `STRUCTURAL_WARNING` is at `:42`.
  - `FillRecompute` fields: `aset/models.py:185-186`.
  - Reader `settings/fills.py:49`; key at `:26`; `DRIFT_NOT_EVALUATED` at `:29`.
- **`record_stop_edit`'s FILLED path — UNCHANGED, left for C2:** `cards/store.py:672`. It runs on an autocommit `with self._connect() as conn` (`:706`) and reads `… FOR UPDATE` at `:709`. `in_trade_shares=shares if state is CardState.FILLED else None` (`:749`) is the planned `shares` column.
- **X-S (R43 (5)):** NO. `fills.drift_warning_pct` is refused by every load path. The card path is now proven on the key check itself: `settings/card.py:270-273` "unknown card setting", F3. The key lands after DRC D4 is on main. Until then every fill records P as NULL, bannered.
- **ADD — `/fill`'s post-commit render (F2):**
  - `aset/web.py:1141-1154`: once `mark_filled` has returned, a `save_fill_update` exception renders `_failed(…)` plus `aset_sizings id <n> marked FILLED — the daily-note write failed after the DB commit; the FILL UPDATE is NOT in the journal.`
  - Then the shared post-commit tail: `_pick_banner` (`:1168`), the exact `DRIFT_NOT_EVALUATED` banner when `drift_warned is None` (`:1169-1172`), and `_result_card(original, form, fill=fill_result)` (`:1173-1177`).
  - Pre-commit refusals are unchanged (`:1061-1139`).
  - C3's panel fill should render the same outcome after its own post-commit side effects.
- **ADD — the real-factory test pattern (F1) for C2's with-DB fill tests:** `tests/cobalt/test_fill_transaction_db.py`:
  - `REAL_CONNECT = _db.connect` bound at import (`:30`); `_real_read` opens a fresh real connection per read (`:186`).
  - In the test (`:197`): assert `db.connect is not REAL_CONNECT`, then `monkeypatch.setattr(_db, "connect", REAL_CONNECT)` (`:215`).
  - No `aset` fixture: no `ensure_schema` or `apply_0021` DDL inside the suite transaction, which would lock tables the real connections need.
  - A constructed ticker; every card id is recorded in `written`.
  - `finally` (`:278`): delete `legs`, then `picks`, then `aset_sizings` by card id on a real connection, then assert zero rows for the ticker.
  - It runs only in pass 2, against the real `0021`.

## FOR THE CHECK
- Range `<base>..<tip>` = `d9240ae4..3ceb3b11`. `git log --oneline d9240ae4..HEAD`:
  - `3ceb3b11 fix(s3-c1): fix r1 — X1 on the real factory, the drift outcome after a note failure, X-S card-load proof, constructed values (L75)`
  - `da9246f0 wip(s3-c1-fix-r1): red`
  
  The report commit follows.
- **F1**
  - Red = the mutation (c3m): `AssertionError: a FILLED transition row survived the failed fill: {'state': 'FILLED', 'actual_fill': None, 'filled_rows': 1, 'legs': 0, 'picks': 0}` at `test_fill_transaction_db.py:263`.
  - Restored: `git diff -- src/cobalt/aset/store.py` is empty.
  - Green: `PASSED …::test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back` / `1 passed in 0.35s`. Pass 2 also PASSED it.
  - Cleanup: `X1RF` `aset_sizings` 0, joined `legs` 0.
  - Control (a): one pick per real manual fill (`_record_pick`, `cards/store.py:544`, unconditional).
- **F2**
  - Red: `test_fill_c1_offline.py:392` and `:403`, `assert 'marked FILLED' in '<div class="failed">FAILED\nconstructed note refusal</div>'`.
  - Green: `PASSED …::test_a_note_failure_after_the_commit_keeps_the_p_missing_banner`, `PASSED …::test_a_note_failure_after_the_commit_keeps_the_drift_warning`.
- **F3**
  - Red: `CardSettingsError: …/card.yaml: expected exactly one top-level mapping 'card_settings'` → `Regex pattern did not match`.
  - Green: `PASSED tests/cobalt/test_s3_c1_experiments.py::test_xs_the_card_load_path_refuses_the_drift_key`.
- **F4**
  - Before: `equal: yes` ×2. After: `equal: no` ×2 (values not quoted).
  - The typo-guard and pick-banner tests still pass: `test_replay_d2_absurd_fill_refused_no_note_write`, `test_fill_form_route[True]`, `test_fill_form_route[False]` are PASSED.
- **R1:** `<P0>` vs `<P2>` are equal on 29 of 30 tables. `cobalt_redactions` went 179 → 180 (ESCALATE).
- **Three suites:**
  - offline `3246 passed, 410 skipped, 1 xfailed` (0 failed);
  - with-DB pass 1 `3617 passed, 6 skipped, 33 deselected, 1 xfailed` + pass 2 `33 passed` = 3650 (0 failed);
  - live-note `146 passed, 1 skipped` (the known `COBALT_TEST_LIVE_DRC` skip).
- **Fingerprints:**
  - `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`
  - `<F1>` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`
  - `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, twice (12:25:25, after 12:25:57)
- **Lock:**
  - taken 12:09:42 → released 12:26:45.
  - `0021` applied 12:21:32 → rolled back by 12:25:25.
  - `0021` applied 12:25:40 → rolled back 12:25:57.
- The stop line is the last line of this file.

## CONTINUE
- next: none. The run is closed. The desk verifies the artifact (L35) and launches `30-s3-exits-c1-fix-r1-check.md`.

## ESCALATE
1. `R1: cobalt_redactions 179 1d147fe7e1e2bf7ee0733886fc9ec5b4 → 180 5acf3646ea44438bed7e762ecd328ee7`.
   - The one table whose `<P0>` and `<P2>` differ.
   - The row was added between 12:09 and 12:21, while pass 1 ran. Every migrate probe read it as `180 -> 180 OK`.
   - Not attributed from reads. The writer is `src/cobalt/redact/store.py`.
   - C1's `<P0>` read 177 at 10:00, so the table grows outside these runs too.
   - Information for the desk. No fix row touched it.
2. The desk's item (L32): the base replay lines `tests/cobalt/test_aset_web.py:101` / `:183` still carry a real card's values.
   - They predate C1 and are not touched here (L75).
   - The same ticker also appears at base lines `:97`, `:103`, `:129`, `:323`, `:516`, `:531`, `:540`, none added by C1. Line numbers only; values not quoted.
3. F1 runs its steps in the order (b) then (a), the reverse of the prompt's listing. The mutation red then names what the failed fill left behind (the transition row), not the control.
   - The assertions are the prompt's.
   - `ASK DESK: keep (b)-before-(a) in test_x1_real_factory…? [12:26 ET, date → Mon Sep 28 12:26:45 EDT 2026]` Safe default taken: kept.
4. F2 keeps `_pick_banner` on the note-failure path. It is the shared post-commit tail, and a missing pick stays loud. The prompt listed the failure banner, the marked-FILLED line, the drift banner and the result card.
   - `ASK DESK: keep the pick banner on the post-commit note-failure path? [12:26 ET]` Safe default taken: kept.
5. The launch row R59 says `comm … 25 common`; this prompt's line 7 says `27 common (24 allow + 3 deny)`. Recorded; not a gate.
6. L74: the block is recorded once under `## L74`.
7. **C1 fix r1 is checked by `30-s3-exits-c1-fix-r1-check.md` (round 2 of ≤3: Opus 5.5 · Sol · Grok, L67) before C2 stacks on it; the builder decided nothing.**

S3 EXITS C1 FIX R1 BUILT 3ceb3b11 | on 5164f867 | migration 0021: rolled back | offline 3246/0 | with-DB 3650/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | FIX: 4 | RUNS: 1 | ESCALATE: 7
