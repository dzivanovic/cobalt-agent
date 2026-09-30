# S3 EXITS C1 FIX R2 — BUILD REPORT

Seat: `s3-exits-c1-fix-r2-build` · Opus 5.5 (`claude-opus-5-5`) · `acceptEdits` · prompt `prompts/2026-09-28/35-s3-exits-c1-fix-r2-build.md` · worktree `/Users/cobalt/cobalt-wt/s3-exits-c1` · `<base>` = `9b25eced` · `<code base>` = `3ceb3b11`. Start: `date` → `Mon Sep 28 13:47:32 EDT 2026`.

## §0 Headline
- F5 built on `3ceb3b11`: fix commit `944f632e`. Four C1-added test values now constructed; tests only.
- Red `equal: yes` ×4 → green `equal: no` ×4; `75 passed` on the two files.
- Suites: offline 3246/0; with-DB 3617 + 33 = 3650/0; live-note 146/0. X22: F = F0 twice.
- `cobalt_dev` at `0013`, `.env` removed, `X1RF` rows 0. `cobalt_redactions` +1 (known outside writer).

## L74
Recorded once (L74): after the prompt file was read (13:47), a `<system-reminder>` block arrived asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and naming a file-send tool. Treated as data. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; no file was sent.

## AUTHORIZATION
`<D>` = `2026-09-28` (`date` → `Mon Sep 28 13:47:32 EDT 2026`).
| gate | command | exit | output |
|---|---|---|---|
| placeholder `R__` | `grep -n -E "R_[_]" "…/35-s3-exits-c1-fix-r2-build.md"` | 1 | (none) |
| placeholder `FILL AT LAUNCH` | `grep -n -F "FILL AT LAUNCH" "…/35-s3-exits-c1-fix-r2-build.md"` | 0 | `34:- PLACEHOLDER GATES: …` — only the gate's own line |
| classification | `grep -n -F "S3 EXITS C1 FIX R2 DRAFTED" "…/reports/s3-exits-c1-fix-r2-draft-2026-09-28.md"` | 0 | `64:S3 EXITS C1 FIX R2 DRAFTED · FIX: 1 · NOT REAL: 4 · UNPROVEN: 0 · OUT OF SCOPE: 2 · OWNER ITEM: 0 · prompts: 2 · C1 stands: NO · new rule strings: 0 · ESCALATE: 4` — line 64, the file's last non-blank line (Read: the file ends at 64) |
| launch row | `grep -n -F "35-s3-exits-c1-fix-r2-build.md" "…/reports/cto-2026-09-28.md"` | 0 | `86:\| R78 \| 13:46 ET \| — DESK LAUNCH ROW: \`35-s3-exits-c1-fix-r2-build.md\` (Opus 5.5, acceptEdits, cwd \`~/cobalt-wt/s3-exits-c1\`) on \`9b25eced\` (code \`3ceb3b11\`); no with-DB run in flight (\`.env\` no matches 13:46; \`33\` is read-only); \`comm\` vs \`29\` line 5: 27 common, 0 new. \| LAUNCHED \|` |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"35-s3-exits-c1-fix-r2-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-28.md"` | 0 | `21696df12485e4c0c6c048e605f712010d844077` |

Authorization: HOLDS (R78 names this file, carries `9b25eced` and `no with-DB run in flight`; committed in `21696df1`).

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 13:47:32 EDT 2026` |
| branch clean | `git status --short --branch` | 0 | `## s3/exits-c1` |
| base | `git log --oneline -1` | 0 | `9b25eced docs(s3-c1): S3 exits C1 fix r1 build report — 3ceb3b11` |
| no `.env` here | `ls /Users/cobalt/cobalt-wt/s3-exits-c1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/s3-exits-c1/.env: No such file or directory` |
| lock free | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| migrations | `ls src/cobalt/db_migrations` | 0 | `0021_legs.sql`, `0021_legs.rollback.sql` present; highest = `0021` (list: 0001 … 0011, 0013, 0014, 0015, 0017, 0021, `__init__.py`, `__pycache__`, `cli.py`, `placement.py`) |
| symbol | `grep -n -F "fill_shares=" tests/cobalt/test_aset_web.py` | 0 | hits at `:217`, `:251`, `:567` (values not quoted, L32) |
| symbol | `grep -n -F "orig_timestamp" tests/cobalt/test_fill_c1_offline.py` | 0 | hit at `:296` (value not quoted) |
| symbol | `grep -n "FROZEN_NOW =" tests/cobalt/conftest.py` | 0 | hit at `:233` (the suite's constructed instant; 14:00 UTC = `2026-09-03T10:00:00-04:00`) |
| symbol | `grep -n "class _FillRoute" tests/cobalt/test_fill_c1_offline.py` | 0 | `294:class _FillRoute:` |
| restarts empty | `uv run cobalt jobs restarts 9b25eced..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |

## E0 BASELINE
On `<base>` `9b25eced` (no file edited before both runs collected).
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (foreground, ~13:48) → **`146 passed, 1 skipped, 15 warnings in 26.12s`**; the one skip: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT`.
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, started ~13:48) → **`3246 passed, 410 skipped, 1 xfailed, 20 warnings in 558.30s (0:09:18)`**, exit 0 — 0 failed, 0 errors (= fix r1's `<p>` 3246). Read `date` → `Mon Sep 28 13:57:43 EDT 2026`.

## E2 RED
A read; no file edited. Values not quoted (L32).
- `git diff c1dc476d 3ceb3b11 -- tests/cobalt/test_aset_web.py` shows the three `fill_shares` lines as `+` (C1-added): hunk `@@ -178,13 +178,44 @@` (the `+` `fill_shares` line = `3ceb3b11:217`), `@@ -217,6 +248,7 @@` (`:251`), `@@ -532,13 +564,23 @@` (`:567`, the `_fill_form` line changed `-`/`+` to add it). The same diff shows `c1dc476d:188` (hunk `-178`, the 11th line: `178` blank, `179` blank, `180` class, `181` def, `182-184` comment, `185` `form = dict(`, `186` `BASE_SIZE_FORM,`, `187` `actual_fill`, `188` `orig_timestamp`) as a context line — the base replay card's `orig_timestamp`.
- `git show 5164f867:tests/cobalt/test_aset_web.py` — C1's replay row (`row = {` at `:194`, the `"shares"` field on `:197`, same layout as `3ceb3b11:194-197`, F4 changed values only) — read.
- `test_fill_c1_offline.py:296` (`_FillRoute.FORM`, `3ceb3b11`) — read at PREFLIGHT (`grep -n -F "orig_timestamp"`). The file came in with C1 (`c57634f8`, `eb642f05`, per the classification #5).

| # | added value (C1) at `3ceb3b11` | base line it is read against | equal |
|---|---|---|---|
| 1 | `tests/cobalt/test_aset_web.py:217` `fill_shares` | `5164f867:tests/cobalt/test_aset_web.py:197` `"shares"` | **yes** |
| 2 | `tests/cobalt/test_aset_web.py:251` `fill_shares` | `5164f867:tests/cobalt/test_aset_web.py:197` `"shares"` | **yes** |
| 3 | `tests/cobalt/test_aset_web.py:567` `fill_shares` | `5164f867:tests/cobalt/test_aset_web.py:197` `"shares"` | **yes** |
| 4 | `tests/cobalt/test_fill_c1_offline.py:296` `orig_timestamp` | `c1dc476d:tests/cobalt/test_aset_web.py:188` `orig_timestamp` | **yes** |

RED: `equal: yes` ×4.

## E3 THE ROWS
Edit only; only the row's two files. `git diff --stat` before the commit: `tests/cobalt/test_aset_web.py | 6 +++---`, `tests/cobalt/test_fill_c1_offline.py | 2 +-` (4 insertions, 4 deletions). Fix commit **`944f632e`** `fix(s3-c1): fix r2 — C1's added test values constructed (L32, L75)` (13:58, `date` → `Mon Sep 28 13:58:05 EDT 2026` after it).
| row | built | file:line at `944f632e` |
|---|---|---|
| F5 | the three C1-added `fill_shares` values → `"30"` (the constructed replay row's `shares`, `test_aset_web.py:197`); `_FillRoute.FORM`'s `orig_timestamp` → `"2026-09-03T10:00:00-04:00"` (the suite's constructed instant, `conftest.py:233` `FROZEN_NOW`, 14:00 UTC). NOT touched: `:567`'s `actual_fill`, every `orig_timestamp` in `test_aset_web.py`, every base line. | `tests/cobalt/test_aset_web.py:217`, `:251`, `:567`; `tests/cobalt/test_fill_c1_offline.py:296` |

After-read (the PREFLIGHT greps): `grep -n -F "fill_shares=" tests/cobalt/test_aset_web.py` → `217`, `251`, `567`, each now the constructed `"30"`; `grep -n -F "orig_timestamp" tests/cobalt/test_fill_c1_offline.py` → `296`, now the constructed instant.
| # | value at `944f632e` | base line | equal |
|---|---|---|---|
| 1 | `test_aset_web.py:217` `fill_shares` | `5164f867:…test_aset_web.py:197` `"shares"` | **no** |
| 2 | `test_aset_web.py:251` `fill_shares` | same | **no** |
| 3 | `test_aset_web.py:567` `fill_shares` | same | **no** |
| 4 | `test_fill_c1_offline.py:296` `orig_timestamp` | `c1dc476d:…test_aset_web.py:188` | **no** |

Offline: `uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_aset_web.py tests/cobalt/test_fill_c1_offline.py` (13:58) → **`75 passed in 0.62s`**, exit 0, 0 failed. The PASSED lines the row names:
```
PASSED tests/cobalt/test_aset_web.py::TestAbsurdFillRejectAtWebLayer::test_replay_d2_absurd_fill_refused_no_note_write
PASSED tests/cobalt/test_aset_web.py::TestAbsurdFillRejectAtWebLayer::test_corrected_fill_passes_the_guard
PASSED tests/cobalt/test_aset_web.py::TestAbsurdFillRejectAtWebLayer::test_fill_with_a_card_row_id_reaches_the_store
PASSED tests/cobalt/test_aset_web.py::TestPickNotRecordedBanner::test_fill_form_route[True]
PASSED tests/cobalt/test_aset_web.py::TestPickNotRecordedBanner::test_fill_form_route[False]
PASSED tests/cobalt/test_aset_web.py::TestPickNotRecordedBanner::test_card_move_no_longer_fills
PASSED tests/cobalt/test_fill_c1_offline.py::test_fill_passes_only_the_typed_price_and_shares
PASSED tests/cobalt/test_fill_c1_offline.py::test_fill_with_no_price_or_no_shares_is_refused[actual_fill]
PASSED tests/cobalt/test_fill_c1_offline.py::test_fill_with_no_price_or_no_shares_is_refused[fill_shares]
PASSED tests/cobalt/test_fill_c1_offline.py::test_fill_with_p_missing_is_recorded_and_bannered
PASSED tests/cobalt/test_fill_c1_offline.py::test_a_note_failure_after_the_commit_keeps_the_p_missing_banner
PASSED tests/cobalt/test_fill_c1_offline.py::test_a_note_failure_after_the_commit_keeps_the_drift_warning
```
(The last six are every `test_fill_c1_offline.py` test that posts `_FillRoute.FORM`, `:348-405`.)

## W THE THREE SUITES
`<tip>` = `944f632e` (the fix commit; every suite below runs on that tree).
- **(a) offline:** `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, 13:58 → 14:07, no `.env`) → **`3246 passed, 410 skipped, 1 xfailed, 20 warnings in 554.95s (0:09:14)`**, exit 0 — 0 failed, 0 errors → **`<p>` = 3246** (= E0; F5 changes values, not test counts). Read `date` → `Mon Sep 28 14:07:48 EDT 2026`.

`<FP>` — copied whole from `prompts/2026-09-27/48-stack-seam-fix-r2-build.md` line 103, typed exactly:
```
COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"
```
- **(b) LOCK:** `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` · `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c1/.env` · `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 28 14:07 /Users/cobalt/cobalt-wt/s3-exits-c1/.env` · **L76 lock taken 14:07:57**. `ls -la …/s3-exits-c1/.env` (LISTED), `<FP>` → `cols	rels	views_md5` / `664	35	272c95bbb12241e3611e4b36326ccf87` → **`<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= fix r1's F0). `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → **`<P0>`**, WHOLE:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.66
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   182          a2204cda0dcef1616682ab2723c9db1c   0.00
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
30 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 28 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.7 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 944f632e (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/s3-exits-c1
```
`legs` and `voice_turns` absent (`-`): `cobalt_dev` is at **`0013`**. The one dirty path is this untracked report. `cobalt_redactions` reads 182 here (fix r1's `<P2>` read 180 at 12:26; the table moved between runs, outside this build — the known outside writer).
- **(c) PASS 1 at `0013`** — `ls -la …/.env` (LISTED; a `date` call ran between it and the pytest call, 14:08:27 — recorded, not a DB call), started 14:08:27, background; the executed command WHOLE (fix r1 report `## W THE THREE SUITES` (c), byte for byte):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py
```
→ **`3617 passed, 6 skipped, 33 deselected, 1 xfailed, 20 warnings in 648.03s (0:10:48)`**, exit 0; read 14:19:30 → **`<d1>` = 3617** (= fix r1's). The six SKIPPED lines, verbatim: `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof` (the three live-vault skips are this with-DB pass's; the live-note leg is (e)).
- **(c2) FORWARD:** `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate` (foreground, timeout 600000) → `cobalt db migrate — FORWARD on cobalt_dev`; `-- applying` `0001_schemas.sql` … `0013_tunables_slug_nullable.sql`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0017_voice_turns.sql`, `0021_legs.sql` in that order; proof table: `legs  user  - -> user  - -> 0 … - -> d41d8cd9  CREATED`, `voice_turns  user  - -> user  - -> 0 … - -> d41d8cd9  CREATED`, every other table `OK` (e.g. `aset_sizings 1 -> 1 0824685c -> 0824685c OK`, `card_transitions 4 -> 4 f181e76b -> f181e76b OK`, `cobalt_redactions 183 -> 183 d15f9c1f -> d15f9c1f OK`); `30 table(s) proven; … content UNCHANGED on every table.`; `code: 944f632e (DIRTY: 1 path(s))`. No `CHANGED`. **`dev forward: APPLIED 14:19:44`**. `ls -la …/.env` (LISTED), `<FP>` → `773	38	126f2d6983fa59f9d0eaaff7da7dd29c` → **`<F1>` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`** (= fix r1's F1).
- **(c3) PASS 2 at `0021`:** `ls -la …/.env` (LISTED), started ~14:19:55, background; the executed command WHOLE (fix r1 report (c3), byte for byte):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py -rA
```
→ **`33 passed, 5 warnings in 137.19s (0:02:17)`**, exit 0, no SKIPPED line; read 14:22:15 → **`<d2>` = 33**. **`<d>` = 3617 + 33 = 3650.** Every PASSED line:
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
- **(c3r) F1's ROWS GONE:** each after `ls -la …/.env` (LISTED): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT count(*) FROM aset_sizings WHERE ticker = 'X1RF'"` → `count` / **`0`**; `COBALT_ENV=dev uv run cobalt db query --side user "SELECT count(*) FROM legs l JOIN aset_sizings a ON a.id = l.card_id WHERE a.ticker = 'X1RF'"` → `count` / **`0`** (~14:22:20).
- **(f) ROLLBACK #1:** `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `cobalt db migrate — ROLLBACK on cobalt_dev`; `-- applying 0021_legs.rollback.sql`, `0017_voice_turns.rollback.sql`, `0015_shadow_agreement_stale.rollback.sql`, `0014_radar_handicap.rollback.sql`; `legs  user  user -> -  0 -> - … DROPPED`, `voice_turns … DROPPED`, every other table `OK` (`cobalt_redactions 183 -> 183 d15f9c1f -> d15f9c1f OK`); `content UNCHANGED on every table.` `ls -la …/.env` (LISTED), `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` → **`<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`** (14:22:35).
- **(c4) X22 (information):** after rollback #1, `<FP>` = `<F0>` (above). FORWARD again: `COBALT_ENV=dev uv run cobalt db migrate` → the same 16 `-- applying` lines ending `0021_legs.sql`, `legs … CREATED`, `voice_turns … CREATED`, every other table `OK`, `content UNCHANGED on every table.` — **`dev forward: APPLIED 14:22:51`**; `<FP>` → `773	38	126f2d6983fa59f9d0eaaff7da7dd29c` (= `<F1>`). ROLLBACK #2: `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` → `0021`, `0017`, `0015`, `0014` reversed, `legs … DROPPED`, `voice_turns … DROPPED`, `content UNCHANGED on every table.` (14:23:04); `<FP>` → `664	35	272c95bbb12241e3611e4b36326ccf87` → **`cobalt_dev: 0013 — F2 = F0`** once more. **`X22: forward, back, forward, back — F = F0 twice`**; `design-changing: no`. Each call after `ls -la …/.env` (LISTED).
- **(e) live-note:** `ls -la …/.env` (LISTED), `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 26.08s`**; the one skip `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT` → **`<l>` = 146**.
- **(f2) THE ROW PROOF:** `ls -la …/.env` (LISTED), `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → **`<P2>`**, WHOLE:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.62
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   183          d15f9c1f9bdde494213ee85dfae221b5   0.00
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
30 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 28 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007; card_stop_edits: 1 card column(s) added by 0007. Proof cost: total 5.7 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 944f632e (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/s3-exits-c1
```
  `<P0>` vs `<P2>`, rows + digest, table by table — EQUAL: `archive_incidents`, `archive_progress`, `aset_sizings` (1 · `0824685c…`), `bars` (1043443 · `2769919a…`), `card_dot_taps`, `card_dots`, `card_stop_edits` (1 · `7599f9ab…`), `card_transitions` (4 · `f181e76b…`), `cobalt_email_sends` (2 · `fba8cf9f…`), `cobalt_jobs` (13 · `8d9b0861…`), `cobalt_kill_switch` (1 · `2e590e87…`), `day_modes` (2 · `f2ffb4d4…`), `desk_grade`, `desk_packet`, `desk_regime`, `legs` (absent both), `missed`, `movers_daily`, `picks` (0 · empty digest), `radar_membership`, `radar_pool`, `radar_score`, `radar_score_receipt`, `radar_score_run`, `session_blocks` (6 · `b650702d…`), `traders` (1 · `a64e0148…`), `vault_overrides` (6 · `6a8b0520…`), `vault_writes` (187 · `2c8181e1…`), `voice_turns` (absent both) — 29 of 30 equal. The known outside writer: **`cobalt_redactions` `182 · a2204cda0dcef1616682ab2723c9db1c` → `183 · d15f9c1f9bdde494213ee85dfae221b5`** (+1; already 183 at the forward's BEFORE probe, 14:19, so it moved during pass 1 — consistent with the classification's named writer `tests/cobalt/test_redact.py:393`; not attributed by a run here). Recorded; not a gate; not an ESCALATE (it grew by exactly 1).
- **Lock (d):** `rm /Users/cobalt/cobalt-wt/s3-exits-c1/.env`; `ls /Users/cobalt/cobalt-wt/s3-exits-c1/.env` → `ls: /Users/cobalt/cobalt-wt/s3-exits-c1/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — **`.env: removed, proven gone (W) — L76 lock released 14:23:44`** (held 14:07:57 → 14:23:44). `0021` not applied.

## RESTARTS
`uv run cobalt jobs restarts 9b25eced..944f632e` (explicit shas; the untracked report is outside the range), exit 0 — the table WHOLE:
```
path	change	rule	restart
tests/cobalt/test_aset_web.py	M	test/documentation; no resident	-
tests/cobalt/test_fill_c1_offline.py	M	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## SEAM FOR C2
Re-issued whole; every `file:line` read on `<tip>` `944f632e`. `git diff --stat 3ceb3b11 944f632e -- src` → empty: no `src` line moved in this fix; each line below was re-read on this tree (greps and Read at 13:59–14:00).
- **The leg writer** `src/cobalt/cards/legs.py:38` `insert_entry_leg(conn, card_id, *, shares, price, at, flag, price_source, price_asof, source, stop_in_force, session, account_mode, day_mode_id, attested_sheet, sheet_mismatch) -> int`. Connection rule: `_assert_in_transaction` (`:30`, called at `:63`) — it runs only on the caller's open transaction and refuses a connection with `autocommit` true; it never opens, commits, rolls back or closes. `ENTRY_SEQ = 0` (`:27`). C2 adds here: the exit-leg writer, the ONE running-share function, the correction writer and the S-HELD writer.
- **THE fill** `src/cobalt/aset/store.py:198` `mark_filled(row_id, *, price, shares, flag, price_source, price_asof, source, now=None, drift_settings=None) -> FillOutcome`; `FillOutcome` at `:38`. Transaction shape:
  - price and shares refused before any connection (`:252-262`);
  - config and the ladder read (`:264-265`);
  - `conn = self._connect()` (`:267`), then `conn.autocommit = False` (`:268`);
  - `SELECT * FROM aset_sizings WHERE id = %s FOR UPDATE` (`:271`);
  - `SizingResult.from_card` (`:283`), P (`:284`), `compute_fill_recompute` (`:285`);
  - `CardStore.fill(conn=conn)` (`:287`), `_attestation` (`:307`), `legs.insert_entry_leg` (`:308`), `_update_fill_cache` (`:325`, def `:360`);
  - ONE `conn.commit()` (`:326`); `except BaseException: conn.rollback(); raise` (`:327-329`).

  F1 proved this shape on the real factory (fix r1 (c3m)); pass 2 here PASSED `test_x1_real_factory_a_failing_cache_update_rolls_the_whole_fill_back` again.
- **The lock statement:**
  - `transition()` (`cards/store.py:239`, `conn=None`) takes `… FROM aset_sizings WHERE id = %s FOR UPDATE` at `:277`.
  - `fill(conn=…)` (`cards/store.py:429`) reads the card on the caller's transaction, already locked.
  - `mark_filled` takes `SELECT * … FOR UPDATE` (`aset/store.py:271`).
- **DDL as applied** (`src/cobalt/db_migrations/0021_legs.sql`): table `"user".legs` `:37`; `legs_one_original_per_seq` `:71`; `legs_one_original_entry` `:73`; trigger `legs_append_only` `:83`; view `"user".legs_current_v` `:93`. Proven on `cobalt_dev` again by pass 2 (`test_legs_db.py`, 11 PASSED) and X22 (F = F0 twice).
- **`card_stop_edits.kind`:** `0021_legs.sql:104-105`, `TEXT NOT NULL DEFAULT 'edit'`, `CHECK (kind IN ('edit', 'reset'))`. No writer sets `reset` yet.
- **`drift_warning_pct` / `drift_warned`:** columns at `0021_legs.sql:113-114`, written only by `_update_fill_cache` (`aset/store.py:360`). `DRIFT_NOT_EVALUATED` imported at `aset/web.py:71`.
- **`record_stop_edit`'s FILLED path — UNCHANGED, left for C2:** `cards/store.py:672`; its `… FOR UPDATE` read at `:709`.
- **X-S (R43 (5)):** NO. `fills.drift_warning_pct` stays refused by every load path (F3 of fix r1, `test_s3_c1_experiments.py::test_xs_the_card_load_path_refuses_the_drift_key`, green in (a)). Until the key lands, every fill records P as NULL, bannered.
- **`/fill`'s post-commit render (F2):** `save_fill_update` at `aset/web.py:1145` in its own post-commit `try`; the shared tail `_pick_banner` (`:1168`), the `DRIFT_NOT_EVALUATED` banner (`:1172`), `_result_card(original, form, fill=fill_result)` (`:1175`). C3's panel fill renders the same outcome after its own post-commit side effects.
- **The real-factory test pattern (F1)** for C2's with-DB fill tests, `tests/cobalt/test_fill_transaction_db.py`: `REAL_CONNECT = _db.connect` bound at import (`:30`); `_real_read` (`:186`) opens a fresh real connection per read (`:190`); in the test (`:197`) assert `_db.connect is not REAL_CONNECT` (`:214`), then `monkeypatch.setattr(_db, "connect", REAL_CONNECT)` (`:215`); no `aset` fixture; a constructed ticker; `finally` (`:278`) deletes `legs`, `picks`, `aset_sizings` by card id on a real connection (`:279`) and asserts zero rows. It runs only in pass 2, against the real `0021`.
- **ADD — constructed values only (F5):** C2's own tests use a `TEST`-style ticker, the constructed prices (`220.0000` / `218.0000`, the replay row `test_aset_web.py:194-197`), constructed share counts (`30`) and the suite's constructed instant (`FROZEN_NOW`, `tests/cobalt/conftest.py:233`) — never a ticker, price, share count or date of his.

## FOR THE CHECK
- Range `<base>..<tip>` = `9b25eced..944f632e`. `git log --oneline 9b25eced..HEAD` → `944f632e fix(s3-c1): fix r2 — C1's added test values constructed (L32, L75)`. The report commit follows.
- **F5**
  - Red (E2, a read at `3ceb3b11`): `equal: yes` ×4 — `test_aset_web.py:217`, `:251`, `:567` `fill_shares` vs `5164f867:…test_aset_web.py:197` `"shares"`; `test_fill_c1_offline.py:296` `orig_timestamp` vs `c1dc476d:…test_aset_web.py:188`.
  - Green (E3, at `944f632e`): `equal: no` ×4; `75 passed in 0.62s`, including every `TestAbsurdFillRejectAtWebLayer` and `TestPickNotRecordedBanner` test and the six `_FillRoute.FORM` posters (PASSED lines under `## E3 THE ROWS`).
  - Diff: 4 insertions, 4 deletions in the two named files; no `src`, no base line.
- **Three suites:**
  - offline `3246 passed, 410 skipped, 1 xfailed` (0 failed);
  - with-DB pass 1 `3617 passed, 6 skipped, 33 deselected, 1 xfailed` + pass 2 `33 passed` = 3650 (0 failed);
  - live-note `146 passed, 1 skipped` (the known `COBALT_TEST_LIVE_DRC` skip).
- **Fingerprints:** `<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `<F1>` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; `<F2>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`, twice (14:22:35, 14:23:04).
- **Row proof:** `<P0>` vs `<P2>` equal on 29 of 30 tables; `cobalt_redactions` 182 → 183 (+1, the known outside writer).
- **`X1RF`:** `aset_sizings` 0, joined `legs` 0.
- **Lock:** taken 14:07:57 → released 14:23:44. `0021` applied 14:19:44 → rolled back 14:22:35; applied 14:22:51 → rolled back 14:23:04.
- **Procedure note:** before pass 1 (W (c)) a `date` call ran between the `ls -la …/.env` (LISTED) and the `COBALT_ENV=dev` pytest call; every other `COBALT_ENV=dev` call was directly preceded by the `ls -la`.
- The stop line is the last line of this file.

## CONTINUE
- next: none. The desk verifies the artifact (L35) and launches `36-s3-exits-c1-fix-r2-check.md`.

## ESCALATE
1. `cobalt_redactions` `<P0>` `182 · a2204cda0dcef1616682ab2723c9db1c` → `<P2>` `183 · d15f9c1f9bdde494213ee85dfae221b5` (+1, during pass 1). The desk's OWED item (R61; writer named in the classification #1); no fix row here.
2. L74: the block is recorded once under `## L74`.
3. **C1 fix r2 is checked by `36-s3-exits-c1-fix-r2-check.md` (round 3 of ≤3, THE LAST: Opus 5.5 · Sol · Grok, L67) before C2 stacks on it; the builder decided nothing.**

S3 EXITS C1 FIX R2 BUILT 944f632e | on 3ceb3b11 | migration 0021: rolled back | offline 3246/0 | with-DB 3650/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | FIX: 1 | RUNS: 0 | ESCALATE: 3
