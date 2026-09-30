# DRC merge fix r2 build 2026-09-28 — seat `drc-merge-fix-r2-build`

## §0 Headline
- `7cdc5774` sits on `0e75e46d` (over `4fc270c7`) and holds 2 rows: G2 in `src/` (the `0018` rollback guarded with `to_regclass`) and G1 in tests (the `0015` registry pins). R0 reproduced `17`'s 3 reds, and T turned them green.
- Offline `3547/0` · with-DB `4066/0` (4057 + 9) · live-note `146/0`.
- The repeated `--down-to 0013` on `cobalt_dev` is a no-op: F3 = F2 = F0. `cobalt_dev: 0013`. `.env` is removed (lock released 13:28:30 EDT).
- RESTARTS: every resident, because of the UNCLASSIFIED `.clinerules` from main. ESCALATE: 3 (1 escalate, 2 records).

## L74
The session's attribution guidance asked commits to carry a `Claude-Session:` line and named a file-send tool. Commits carry exactly the strings `32` types (`Co-Authored-By` only). Recorded once.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| placeholder gate 1 | `grep -n -E "R_[_]" ".../32-drc-merge-fix-r2-build.md"` | 1 | (nothing) |
| placeholder gate 2 | `grep -n -F "FILL AT LAUNCH" ".../32-drc-merge-fix-r2-build.md"` | 0 | `22:` only (the gate's own line) |
| launch row | `grep -n "^\| R70 " <desk file>` | 0 | `78:\| R70 \| 13:08 ET \| — DESK LAUNCH ROW: \`32-drc-merge-fix-r2-build.md\` (Opus 5.5, acceptEdits, cwd \`~/cobalt-wt/drc-d1\`) on \`4fc270c7\` (tip \`0e75e46d\`, main \`20139f3d\`); \`comm\` vs \`17\` line 5: 0 new; no with-DB run in flight (\`.env\` no matches 13:08; \`30\` is read-only). \| LAUNCHED \|` |
| row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"32-drc-merge-fix-r2-build.md" -- ".../cto-2026-09-28.md"` | 0 | `e8f148d7980370f600c2d19bf4151452c456371a` |
| fix-round ruling | `grep -n "^\| R68 " <desk file>` | 0 | `76:\| R68 \| 12:57 ET \| — DESK LAUNCH ROW: \`31-draft-drc-merge-fix-r2.md\` …` `\| LAUNCHED \|` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../drc-merge-fix-r2-draft-2026-09-28.md"` | 0 | `e8f148d7980370f600c2d19bf4151452c456371a` |
| classification stop line | `tail -n 3 ".../drc-merge-fix-r2-draft-2026-09-28.md"` | 0 | `DRC MERGE FIX R2 DRAFTED · FIX: 3 · NOT REAL: 0 · UNPROVEN: 0 · OUT OF SCOPE: 1 · OWNER ITEM: 0 · code change: src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql, tests/cobalt/test_stale_score_db.py · prompts: 2 · new rule strings: 0 · ESCALATE: 1` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 13:08:53 EDT 2026` |
| tree quiet | `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -2` | 0 | `0e75e46d wip(drc-merge-fix-r1): W (c1) — with-DB pass 1 red (U1, U2 proven + 1 new red, 0018 rollback on absent drc_rows)` / `4fc270c7 test(drc-merge): fix r1 — registry pins re-stated to the merged numeric order` |
| no code since fix r1 | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline 4fc270c7..HEAD -- src tests configs` | 0 | (empty) |
| merge parents | `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%p 5bb1f4b5` | 0 | `10163d51 daf36e01` |
| main at launch | `git -C /Users/cobalt/cobalt log -1 --format=%h main` | 0 | `72ca55cb` (the desk read `20139f3d` at 13:08; main moved since) |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| lock (ours) | `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |

## LOCK
(a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1). `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env` (exit 0, not read). `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly one line, ours: `-rw-------  1 cobalt  staff  2186 Sep 28 13:09 /Users/cobalt/cobalt-wt/drc-d1/.env`. **L76 lock taken 13:09:16 EDT.**

(b) `<FP>` (typed exactly; exit 0) → `<F0>` = `17`'s expected value:
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
`COBALT_ENV=dev uv run cobalt db migrate --proof-only` (exit 0):
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.56
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   181          0a47d3e8f772c8182e55526e1d20e2a6   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
drc_fills            user    -        -            -                                  0.00
drc_imports          user    -        -            -                                  0.00
drc_rows             user    -        -            -                                  0.00
drc_stated_books     user    -        -            -                                  0.00
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
33 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. Proof cost: total 5.6 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 0e75e46d (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/drc-d1
```
`drc_*` and `voice_turns` read `-`; no `CHANGED`. (`cobalt_redactions` reads 181 rows against `17`'s 180 at 12:41; a data row, not a schema change; `<F0>` is unchanged.) `DIRTY: 1 path(s)` = this untracked report.
`<LV>` (typed exactly; exit 0):
```
cols_0014	slug_nullable_0013
0	True
```
`cols_0014` = 0, `slug_nullable_0013` = `True` (the client prints the boolean as `True`, the prompt's `t`) → **`cobalt_dev` at `0013`**. Status rule after the first `uv run`: `## drc/d1-trading-log` + this report `??` only.

## R0 RED
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → LISTED. `COBALT_ENV=dev uv run pytest -q -rfs -p no:cacheprovider tests/cobalt/test_stale_score_db.py tests/cobalt/test_radar_handicap_store.py` on `0e75e46d` (`run_in_background`, exit 1). Summary and every `FAILED` line (ANSI codes stripped):
```
FAILED tests/cobalt/test_stale_score_db.py::test_0015_is_registered_after_0013_and_its_rollback_first - AssertionError: assert PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt...
FAILED tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction - psycopg.errors.UndefinedTable: relation "user.drc_rows" does not exist
FAILED tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply - psycopg.errors.UndefinedTable: relation "user.drc_rows" does not exist
3 failed, 16 passed in 2.11s
```
The detail: `:159` `E AssertionError: assert PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0017_voice_turns.sql') == (PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations') / '0015_shadow_agreement_stale.sql')` (`FORWARD[-2]` is 0017). Both `UndefinedTable` reds print `E LINE 7: DELETE FROM "user".drc_rows WHERE kind IN ('seed', 'book_clo...` (output lines 67 and 181). The set is exactly `17`'s three. Status rule: `## drc/d1-trading-log` + this report `??` only.

## THE ROWS
Each OLD block was read (Read tool) at its stated lines, verbatim. No `LINE MOVED`.
- **G1** `tests/cobalt/test_stale_score_db.py:159–162` · old `FORWARD[-2]` / `REVERSE[1]` (0015) and `FORWARD[-4]` / `REVERSE[3]` (0013) · new `FORWARD[-4]` / `REVERSE[3]` (0015) and `FORWARD[-6]` / `REVERSE[5]` (0013). Four pins, none added; the paths and names are unchanged.
- **G2** `src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql:7–10` · old: the three unguarded `drc_rows` statements · new: the same three statements, indented, inside `DO $migration$ BEGIN IF to_regclass('"user".drc_rows') IS NULL THEN RETURN; END IF; … END $migration$;` (now `:7–17`). Lines 1–6 and the `DROP TABLE IF EXISTS` line are byte for byte.

G2 proof greps (each exit 0):
```
$ grep -n -F "to_regclass" ".../0018_drc_stated_books.rollback.sql"
9:    IF to_regclass('"user".drc_rows') IS NULL THEN
$ grep -n -F "DROP TABLE IF EXISTS" ".../0018_drc_stated_books.rollback.sql"
18:DROP TABLE IF EXISTS "user".drc_stated_books;
$ grep -n -F "his statements live ONLY here" ".../0018_drc_stated_books.rollback.sql"
3:-- his statements live ONLY here; re-state them after a re-apply. The
```
`wc -l` → `18`, so `:18` is the last line.

## T TARGETED
`git -C /Users/cobalt/cobalt-wt/drc-d1 diff --stat` (exit 0) — exactly the 2 row files:
```
 .../db_migrations/0018_drc_stated_books.rollback.sql      | 15 +++++++++++----
 tests/cobalt/test_stale_score_db.py                       |  8 ++++----
 2 files changed, 15 insertions(+), 8 deletions(-)
```
`git -C /Users/cobalt/cobalt-wt/drc-d1 diff` (exit 0), WHOLE:
```
diff --git a/src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql b/src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql
index bc68ed23..64a97e05 100644
--- a/src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql
+++ b/src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql
@@ -4,8 +4,15 @@
 -- `seed` / `book_close` rows are derived and are deleted too — re-recording
 -- a day rebuilds them from its stored imports.
 
-DELETE FROM "user".drc_rows WHERE kind IN ('seed', 'book_close');
-ALTER TABLE "user".drc_rows DROP CONSTRAINT IF EXISTS drc_rows_kind_check;
-ALTER TABLE "user".drc_rows ADD CONSTRAINT drc_rows_kind_check
-    CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day'));
+DO $migration$
+BEGIN
+    IF to_regclass('"user".drc_rows') IS NULL THEN
+        RETURN;
+    END IF;
+    DELETE FROM "user".drc_rows WHERE kind IN ('seed', 'book_close');
+    ALTER TABLE "user".drc_rows DROP CONSTRAINT IF EXISTS drc_rows_kind_check;
+    ALTER TABLE "user".drc_rows ADD CONSTRAINT drc_rows_kind_check
+        CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day'));
+END
+$migration$;
 DROP TABLE IF EXISTS "user".drc_stated_books;
diff --git a/tests/cobalt/test_stale_score_db.py b/tests/cobalt/test_stale_score_db.py
index 05838a74..4563091f 100644
--- a/tests/cobalt/test_stale_score_db.py
+++ b/tests/cobalt/test_stale_score_db.py
@@ -156,10 +156,10 @@ def _predicates():
 def test_0015_is_registered_after_0013_and_its_rollback_first():
     from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
 
-    assert FORWARD[-2] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql"
-    assert REVERSE[1] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql"
-    assert FORWARD[-4].name == "0013_tunables_slug_nullable.sql"
-    assert REVERSE[3].name == "0013_tunables_slug_nullable.rollback.sql"
+    assert FORWARD[-4] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql"
+    assert REVERSE[3] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql"
+    assert FORWARD[-6].name == "0013_tunables_slug_nullable.sql"
+    assert REVERSE[5].name == "0013_tunables_slug_nullable.rollback.sql"
 
 
 def test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction():
```
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → LISTED. The R0 command again (`run_in_background`, exit 0), summary WHOLE:
```
19 passed in 2.06s
```
0 failed, 0 errors; R0's three reds pass.

With the tables present: `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → LISTED. `COBALT_ENV=dev uv run pytest -q -rfs -p no:cacheprovider tests/cobalt/test_drc_k1_store.py tests/cobalt/test_drc_k1_experiments.py tests/cobalt/test_drc_store.py` (`run_in_background`, exit 0), summary WHOLE:
```
88 passed in 3.93s
```
0 failed, 0 errors, and no `FAILED` or `SKIPPED` line was printed (`-rfs`). The three named tests are defined in those files: `test_drc_k1_store.py:213` `test_the_drc_rows_kind_check_is_widened_under_its_proven_name`, `:221` `test_the_rollback_drops_the_table_restores_the_check_and_deletes_the_derived_rows`, `test_drc_k1_experiments.py:359` `test_x5_pass_0018_widens_the_kind_check_and_its_rollback_narrows_it`. With no skip, they passed. Status rule: `## drc/d1-trading-log`, the 2 row files ` M`, and this report `??` only.

## FIX COMMIT
`cd /Users/cobalt/cobalt-wt/drc-d1`; `git add "tests/cobalt/test_stale_score_db.py"`; `git add "src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql"`; `git commit` with `32`'s three `-m` strings (exit 0) → `[drc/d1-trading-log 7cdc5774] fix(drc-merge): fix r2 — 0018 rollback a no-op on absent drc_rows; 0015 registry pin re-stated` / `2 files changed, 15 insertions(+), 8 deletions(-)`. `date` → `Mon Sep 28 13:11:33 EDT 2026`.
`git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%h%x20%p` → `7cdc5774 0e75e46d`. **`<fix tip>` = `7cdc5774`**, parent `0e75e46d`.
`git -C /Users/cobalt/cobalt-wt/drc-d1 show --stat --format=%h 7cdc5774`:
```
7cdc5774

 .../db_migrations/0018_drc_stated_books.rollback.sql      | 15 +++++++++++----
 tests/cobalt/test_stale_score_db.py                       |  8 ++++----
 2 files changed, 15 insertions(+), 8 deletions(-)
```
The stat abbreviates the first path, so `git -C /Users/cobalt/cobalt-wt/drc-d1 show --name-only --format=%h 7cdc5774` gives the full names:
```
7cdc5774

src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql
tests/cobalt/test_stale_score_db.py
```
The paths are exactly the 2 rows.

## W WITH-DB
(a)–(b) were taken at `## LOCK` (13:09:16 EDT); the lock has been held since.

(c1) PASS 1 at `0013` on `7cdc5774`. `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → LISTED. The executed command, WHOLE (`run_in_background`, exit 0):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
```
Summary and every `SKIPPED` line (ANSI codes stripped):
```
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
4057 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 658.21s (0:10:58)
```
GATE green: 0 failed, 0 errors, 9 deselected. **`<d1>` = 4057** = the expected 4057 (`17`'s 4054 + the 3); 6 skipped = expected. No `DeadlockDetected`. Status rule: `## drc/d1-trading-log` + this report `??` only.

(c2) FORWARD: `ls -la …/.env` → LISTED. `COBALT_ENV=dev uv run cobalt db migrate` (FOREGROUND, exit 0):
```
cobalt db migrate — FORWARD on cobalt_dev
-- applying 0001_schemas.sql
-- applying 0002_move_tables.sql
-- applying 0003_heartbeat_vault_outcome.sql
-- applying 0004_radar_pool.sql
-- applying 0005_heartbeat_note_absent.sql
-- applying 0006_radar_score.sql
-- applying 0007_radar_cards.sql
-- applying 0008_radar_value_movers.sql
-- applying 0009_picks_missed.sql
-- applying 0010_archive_progress.sql
-- applying 0011_archive_incidents.sql
-- applying 0013_tunables_slug_nullable.sql
-- applying 0014_radar_handicap.sql
-- applying 0015_shadow_agreement_stale.sql
-- applying 0016_drc.sql
-- applying 0017_voice_turns.sql
-- applying 0018_drc_stated_books.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> system           0 -> 0          0.01 -> 0.00    d41d8cd9 -> d41d8cd9  OK
archive_progress     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.42 -> 5.48    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           182 -> 182      0.00 -> 0.00    a2204cda -> a2204cda  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
drc_fills            user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
drc_imports          user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
drc_rows             user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
drc_stated_books     user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
missed               user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
movers_daily         system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
picks                user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               187 -> 187      0.01 -> 0.01    2c8181e1 -> 2c8181e1  OK
voice_turns          user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
----------------------------------------------------------------------------------------------------------------------
33 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.5 s + AFTER 5.5 s = total 11.0 s; slowest table bars (5.4 s before).
code: 7cdc5774 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/drc-d1
```
The whole FORWARD tuple ran (0001…0011 idempotent). `0014`, `0015`, `0016`, `0017` and `0018` applied in that order. Every pre-existing table is `OK` and there is no `CHANGED`. Created: `drc_fills`, `drc_imports`, `drc_rows`, `drc_stated_books`, `voice_turns`. (`cobalt_redactions` reads 182, up from 181 at LOCK; it is unchanged across the migrate.) **`dev forward: APPLIED 13:23:31 EDT`**.
`<FP>` (exit 0) → `<F1>`:
```
cols	rels	views_md5
796	40	5727e9dfb418376cc48722a3601ca7c3
```

(d) PASS 2 at `0018`: `ls -la …/.env` → LISTED. The executed command, WHOLE (`run_in_background`, exit 0):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
```
Summary:
```
9 passed, 5 warnings in 136.93s (0:02:16)
```
(The 5 warnings are `PytestUnknownMarkWarning: Unknown pytest.mark.slow`.) GATE green: 0 failed, 0 errors. **`<d2>` = 9**, so **`<d>` = 4057 + 9 = 4066**.

(e) LIVE-NOTE: `ls -la …/.env` → LISTED. `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (`run_in_background`, exit 0):
```
SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
146 passed, 1 skipped, 15 warnings in 25.51s
```
GATE green: 0 failed. The only skip is the known `COBALT_TEST_LIVE_DRC` skip; no skip names `COBALT_LIVE_VAULT_ROOT`. **`<l>` = 146**.

(f) step 1: `ls -la …/.env` → LISTED. `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (FOREGROUND, exit 0), WHOLE:
```
cobalt db migrate — ROLLBACK on cobalt_dev
-- applying 0018_drc_stated_books.rollback.sql
-- applying 0017_voice_turns.rollback.sql
-- applying 0016_drc.rollback.sql
-- applying 0015_shadow_agreement_stale.rollback.sql
-- applying 0014_radar_handicap.rollback.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> system           0 -> 0          0.01 -> 0.00    d41d8cd9 -> d41d8cd9  OK
archive_progress     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.56 -> 5.43    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           182 -> 182      0.00 -> 0.00    a2204cda -> a2204cda  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
drc_fills            user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
drc_imports          user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
drc_rows             user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
drc_stated_books     user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
missed               user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
movers_daily         system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
picks                user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               187 -> 187      0.01 -> 0.01    2c8181e1 -> 2c8181e1  OK
voice_turns          user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
----------------------------------------------------------------------------------------------------------------------
33 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.6 s + AFTER 5.5 s = total 11.1 s; slowest table bars (5.6 s before).
code: 7cdc5774 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/drc-d1
```
`0018`, `0017`, `0016`, `0015` and `0014` were reversed, newest first. Nothing at or below `0013` ran. `<FP>` (exit 0) → `<F2>`:
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
**`cobalt_dev: 0013 — F2 = F0 (664 · 35 · 272c95bbb12241e3611e4b36326ccf87)`**

(f) step 2, THE REPEATED ROLLBACK (`drc_rows` now absent): `ls -la …/.env` → LISTED. `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` AGAIN (FOREGROUND, **exit 0**), WHOLE:
```
cobalt db migrate — ROLLBACK on cobalt_dev
-- applying 0018_drc_stated_books.rollback.sql
-- applying 0017_voice_turns.rollback.sql
-- applying 0016_drc.rollback.sql
-- applying 0015_shadow_agreement_stale.rollback.sql
-- applying 0014_radar_handicap.rollback.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> system           0 -> 0          0.01 -> 0.00    d41d8cd9 -> d41d8cd9  OK
archive_progress     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.53 -> 5.50    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           182 -> 182      0.00 -> 0.00    a2204cda -> a2204cda  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
drc_fills            user    - -> -                     - -> -          0.00 -> 0.00    - -> -                ABSENT
drc_imports          user    - -> -                     - -> -          0.00 -> 0.00    - -> -                ABSENT
drc_rows             user    - -> -                     - -> -          0.00 -> 0.00    - -> -                ABSENT
drc_stated_books     user    - -> -                     - -> -          0.00 -> 0.00    - -> -                ABSENT
missed               user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
movers_daily         system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
picks                user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               187 -> 187      0.01 -> 0.01    2c8181e1 -> 2c8181e1  OK
voice_turns          user    - -> -                     - -> -          0.00 -> 0.00    - -> -                ABSENT
----------------------------------------------------------------------------------------------------------------------
33 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.6 s + AFTER 5.5 s = total 11.1 s; slowest table bars (5.5 s before).
code: 7cdc5774 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/drc-d1
```
The same five files ran, with no error; the five `0016`–`0018` tables read `ABSENT`. `<FP>` (exit 0) → `<F3>`:
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
**`repeated rollback: no-op — F3 = F2 = F0`**. G2's contract holds on the real `cobalt_dev`: at `4fc270c7` this same call failed with `UndefinedTable` (`17`'s `:180` red).

(f) step 3: `rm /Users/cobalt/cobalt-wt/drc-d1/.env` (exit 0). `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` (exit 1). `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1). **`.env: removed, proven gone (L76 lock released 13:28:30 EDT)`**

## O OFFLINE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` on `7cdc5774` (`run_in_background`, exit 0), summary WHOLE:
```
3547 passed, 525 skipped, 1 xfailed, 20 warnings in 556.93s (0:09:16)
```
GATE green: 0 failed, 0 errors. **`<p>` = 3547** = the expected 3547; 525 skipped = expected. Status rule: `## drc/d1-trading-log` + this report `??` only (read 13:38:10 EDT).

## RESTARTS
`ls -la …/.env` → `No such file or directory`. `uv run cobalt jobs restarts 10163d51..7cdc5774` → **exit 1** (`RestartError`: one path is unclassified). The table has 751 lines. The first foreground run's output was truncated in the tool display, so the same command was run again (`run_in_background`) to read it whole from its output file. Below are every non-`DOCS` row and the header/footer lines, verbatim (`grep -n -v -F "<TAB>DOCS<TAB>"` of the output file). The 523 `DOCS` rows (output lines 5–7 `AGENTS.md`, `CLAUDE.md`, `QWEN.md`, and 16–535, every path under `docs/`) each read `DOCS	-` and derive no restart. They are left out here to keep the report readable.
```
1:FAILED: RestartError: one or more changed paths were unclassified
2:path	change	rule	restart
3:.clinerules	M	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
4:ESCALATE: unclassified path .clinerules
8:configs/cobalt/agents/voice.yaml	A	resident reads	com.cobalt.aset
9:configs/cobalt/jobs.yaml	M	registry; register, no restart	-
10:configs/cobalt/modelaccess.yaml	A	resident reads	com.cobalt.aset
11:configs/cobalt/radar.yaml	M	resident reads	com.cobalt.radar
12:configs/cobalt/rules.yaml	M	no resident reads (one-shot: com.cobalt.prefill-daily,com.cobalt.prefill-drc)	-
13:configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
14:configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
15:configs/cobalt/voice.yaml	A	resident reads	com.cobalt.aset
536:ops/start_aset.sh	M	resident reads	com.cobalt.aset
537:pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
538:src/cobalt/aset/card_stop.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
539:src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
540:src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
541:src/cobalt/cards/health.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
542:src/cobalt/cards/scoring.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
543:src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
544:src/cobalt/cli.py	M	static import reach	com.cobalt.radar
545:src/cobalt/db_migrations/0013_tunables_slug_nullable.rollback.sql	A	non-Python src asset	-
546:src/cobalt/db_migrations/0013_tunables_slug_nullable.sql	A	non-Python src asset	-
547:src/cobalt/db_migrations/0014_radar_handicap.rollback.sql	A	non-Python src asset	-
548:src/cobalt/db_migrations/0014_radar_handicap.sql	A	non-Python src asset	-
549:src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql	A	non-Python src asset	-
550:src/cobalt/db_migrations/0015_shadow_agreement_stale.sql	A	non-Python src asset	-
551:src/cobalt/db_migrations/0017_voice_turns.rollback.sql	A	non-Python src asset	-
552:src/cobalt/db_migrations/0017_voice_turns.sql	A	non-Python src asset	-
553:src/cobalt/db_migrations/0018_drc_stated_books.rollback.sql	M	non-Python src asset	-
554:src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
555:src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
556:src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
557:src/cobalt/modelaccess/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
558:src/cobalt/modelaccess/adapters.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
559:src/cobalt/modelaccess/client.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
560:src/cobalt/modelaccess/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
561:src/cobalt/modelaccess/guard.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
562:src/cobalt/modelaccess/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
563:src/cobalt/radar/anatomy/extension.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
564:src/cobalt/radar/anatomy/frame.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
565:src/cobalt/radar/anatomy/in_play.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
566:src/cobalt/radar/anatomy/indicators.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
567:src/cobalt/radar/anatomy/leg_roles.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
568:src/cobalt/radar/anatomy/micro_range.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
569:src/cobalt/radar/anatomy/pivots.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
570:src/cobalt/radar/anatomy/range_break.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
571:src/cobalt/radar/anatomy/registry.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
572:src/cobalt/radar/anatomy/session_levels.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
573:src/cobalt/radar/anatomy/slope.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
574:src/cobalt/radar/audit_export.py	M	static import reach	com.cobalt.radar
575:src/cobalt/radar/cli.py	M	static import reach	com.cobalt.radar
576:src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
577:src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
578:src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
579:src/cobalt/radar/formation/__init__.py	A	static import reach	-
580:src/cobalt/radar/formation/anchors.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
581:src/cobalt/radar/formation/atoms.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
582:src/cobalt/radar/formation/stops.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
583:src/cobalt/radar/formation/triggers.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
584:src/cobalt/radar/handicap.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
585:src/cobalt/radar/handicap_dry_run.py	A	static import reach	com.cobalt.radar
586:src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
587:src/cobalt/radar/pool.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
588:src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
589:src/cobalt/radar/seam.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
590:src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
591:src/cobalt/replay/cli.py	M	static import reach	com.cobalt.radar
592:src/cobalt/replay/formations.py	M	static import reach	com.cobalt.radar
593:src/cobalt/replay/line.py	M	static import reach	com.cobalt.radar
594:src/cobalt/replay/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
595:src/cobalt/replay/movers.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
596:src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
597:src/cobalt/smoke/checks.py	M	static import reach	com.cobalt.radar
598:src/cobalt/taxonomy/cli.py	M	static import reach	com.cobalt.radar
599:src/cobalt/taxonomy/loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
600:src/cobalt/taxonomy/tunables.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
601:src/cobalt/taxonomy/vault_loader.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
602:src/cobalt/voice/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
603:src/cobalt/voice/agent.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
604:src/cobalt/voice/cli.py	A	static import reach	com.cobalt.radar
605:src/cobalt/voice/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
606:src/cobalt/voice/confirm.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
607:src/cobalt/voice/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
608:src/cobalt/voice/registry.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
609:src/cobalt/voice/resolve.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
610:src/cobalt/voice/scratch.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
611:src/cobalt/voice/store.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
612:src/cobalt/voice/tools.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
613:src/cobalt/voice/transcribe.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
614:src/cobalt/voice/turn.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
615:src/cobalt/voice/web.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
616–747: tests/** and tests/fixtures/** (132 rows), each `test/documentation; no resident	-`
748:uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
749:RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
(The 132 `tests/` rows 616–747 were read verbatim. Every one has rule `test/documentation; no resident` and restart `-`.) `RESTARTS:` = `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. That set comes from the UNCLASSIFIED `.clinerules` row, which maps to all residents (L42: unproven → all). → `ESCALATE: UNCLASSIFIED .clinerules`. The range is `10163d51..7cdc5774`, so it carries the whole merge from main. `.clinerules`, `uv.lock` and `pyproject.toml` arrive through the merge. Fix r2 itself adds one row: `0018_drc_stated_books.rollback.sql`, `non-Python src asset`, `-`.

## FOR 08
Re-issued WHOLE; supersedes `17`'s partial `## FOR 08`.
- `<fix tip>` `7cdc5774`, parent `0e75e46d` (over `4fc270c7`, fix r1). The merge commit `5bb1f4b5` has parents `10163d51` and `daf36e01`. `<main at launch>` = `72ca55cb`.
- `git -C /Users/cobalt/cobalt rev-list --count main..drc/d1-trading-log` → `70` ahead. `git -C /Users/cobalt/cobalt rev-list --count drc/d1-trading-log..main` → `26` behind. `git -C /Users/cobalt/cobalt diff --stat daf36e01 main -- . ':(exclude)docs'` → empty (exit 0): main moved docs-only since the merge.
- FORWARD and REVERSE as merged (`git -C /Users/cobalt/cobalt-wt/drc-d1 show HEAD:src/cobalt/db_migrations/__init__.py`, `:106–145`):
```
#: Applied in this order, every time, every file idempotent.
FORWARD = (
    MIGRATIONS_DIR / "0001_schemas.sql",
    MIGRATIONS_DIR / "0002_move_tables.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.sql",
    MIGRATIONS_DIR / "0004_radar_pool.sql",
    MIGRATIONS_DIR / "0005_heartbeat_note_absent.sql",
    MIGRATIONS_DIR / "0006_radar_score.sql",
    MIGRATIONS_DIR / "0007_radar_cards.sql",
    MIGRATIONS_DIR / "0008_radar_value_movers.sql",
    MIGRATIONS_DIR / "0009_picks_missed.sql",
    MIGRATIONS_DIR / "0010_archive_progress.sql",
    MIGRATIONS_DIR / "0011_archive_incidents.sql",
    MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql",
    MIGRATIONS_DIR / "0014_radar_handicap.sql",
    MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql",
    MIGRATIONS_DIR / "0016_drc.sql",
    MIGRATIONS_DIR / "0017_voice_turns.sql",
    MIGRATIONS_DIR / "0018_drc_stated_books.sql",
)

#: `--rollback`, newest first. 0001 is deliberately NOT reversed.
REVERSE = (
    MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql",
    MIGRATIONS_DIR / "0017_voice_turns.rollback.sql",
    MIGRATIONS_DIR / "0016_drc.rollback.sql",
    MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql",
    MIGRATIONS_DIR / "0014_radar_handicap.rollback.sql",
    MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql",
    MIGRATIONS_DIR / "0011_archive_incidents.rollback.sql",
    MIGRATIONS_DIR / "0010_archive_progress.rollback.sql",
    MIGRATIONS_DIR / "0009_picks_missed.rollback.sql",
    MIGRATIONS_DIR / "0008_radar_value_movers.rollback.sql",
    MIGRATIONS_DIR / "0007_radar_cards.rollback.sql",
    MIGRATIONS_DIR / "0006_radar_score.rollback.sql",
    MIGRATIONS_DIR / "0005_heartbeat_note_absent.rollback.sql",
    MIGRATIONS_DIR / "0004_radar_pool.rollback.sql",
    MIGRATIONS_DIR / "0003_heartbeat_vault_outcome.rollback.sql",
    MIGRATIONS_DIR / "0002_move_tables.rollback.sql",
)
```
  `grep -n -F "0018_drc_stated_books" ".../db_migrations/__init__.py"` → FORWARD entry `:124`, REVERSE entry `:129` (docstring hits `:62`, `:66`, `:72`). Next free: `0019` (`08`'s `drc_events`), `0020` (D3), `0021` (S3 exits C1, off main).
- THE ROLLBACK CONTRACT `08`–`11` inherit: every rollback on this tree is a no-op on absent objects (`IF EXISTS`, or `0013`'s / G2's `DO $migration$` + `to_regclass` guard). `08`'s `0019` rollback keeps it. The repeated `--down-to 0013` of W (f) step 2 is the proof shape.
- Anchors on the fix tip (`grep -n -F`, each exit 0):
  - `src/cobalt/db_migrations/placement.py:100` `"drc_stated_books": Side.USER,`
  - `src/cobalt/aset/web.py:1152` `@app.post("/attest", response_class=HTMLResponse)`
  - `src/cobalt/aset/web.py:1557` `@app.get("/drc", response_class=HTMLResponse)`
  - `src/cobalt/aset/web.py:1512` `async def radar_card_release(card_id: int):`
  - `src/cobalt/cli.py:512` `drc_cli.add_parser(sub)`
  - `src/cobalt/replay/line.py:60` `MIN_N_FOR_AVERAGE = 30`
  - `src/cobalt/taxonomy/vault_loader.py:91` `STRATEGIES_DIR = "1 - Trading/4 - Strategies"`
- Counts on the fix tip: `15`'s `<p0>` 2588 on `10163d51` → `<p>` **3547** offline (525 skipped, 1 xfailed). `<d1>` 4057 + `<d2>` 9 = `<d>` **4066** with-DB. `<l>` **146** live-note. `<F0>` = `<F2>` = `<F3>` = 664 · 35 · `272c95bbb12241e3611e4b36326ccf87`; `<F1>` (at `0018`) = 796 · 40 · `5727e9dfb418376cc48722a3601ca7c3`.
- THE WITH-DB DESELECT SET: the eight arguments (nine tests) W (c1) ran with are the merged tree's. `08`'s three arguments (four tests) no longer describe a green pass at `0013`.
- THE REGISTRY PINS `08` MUST RE-STATE when it adds `0019` (`grep -n -F "0018_drc_stated_books"` per file on the fix tip):
  - `test_assumed_store.py:255,256` (`FORWARD[-1]`, `REVERSE[0]`)
  - `test_drc_k1_store.py:116,124` (`names[-3:]` and the rollback list; `:45,:46` are the SQL / ROLLBACK paths, `:3` the docstring)
  - `test_drc_store.py:66,68,143`
  - `test_radar_handicap_store.py:85`
  - `test_voice_store.py:59`
  - `test_stale_score_db.py` pins by slot, not by name: `FORWARD[` → `:159` `FORWARD[-4]` (0015), `:161` `FORWARD[-6]` (0013); `REVERSE[` → `:160` `REVERSE[3]` (0015), `:162` `REVERSE[5]` (0013). Adding `0019` moves each by one.
  - `test_p4_migrations.py:102,117,128`
  - `test_radar_migration.py:35`
  - `test_radar_score_migration.py:104`
  - `test_tenancy.py:516`
  - `test_archiver_migrations.py:94,102,130,140`
- RESTARTS (`10163d51..7cdc5774`, derived under `## RESTARTS`): `com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`. It is widened to all residents by the UNCLASSIFIED `.clinerules` (ESCALATE 1).
- `CLAUDE.md` in the worktree is main's stub (R33 (4)).

## FOR THE CHECK
- R0: summary `3 failed, 16 passed` and its 3 `FAILED` lines under `## R0 RED`.
- T: `git diff --stat` and `git diff` WHOLE, plus both summaries (`19 passed`; `88 passed`), under `## T TARGETED`.
- G2's three proof greps (`:9` `to_regclass`, `:18` `DROP TABLE IF EXISTS`, `:3` the COST line) under `## THE ROWS`.
- Fix commit `7cdc5774`: `show --stat` and `--name-only` under `## FIX COMMIT` (2 paths, exactly the rows).
- Suites: O `3547 passed, 525 skipped, 1 xfailed`. W (c1) `4057 passed, 6 skipped, 9 deselected, 1 xfailed`. W (d) `9 passed`. W (e) `146 passed, 1 skipped`.
- W's two executed commands, (c1) and (d), quoted WHOLE under `## W WITH-DB`.
- Fingerprints: `<F0>` 664 · 35 · `272c95bb…`; `<LV>` `0 · True`; `<F1>` 796 · 40 · `5727e9df…`; `<F2>` = `<F3>` = `<F0>`.
- The two rollback outputs, (f) steps 1 and 2, WHOLE under `## W WITH-DB`.
- Lock: taken 13:09:16 EDT, released 13:28:30 EDT. Forward applied 13:23:31 EDT.
- RESTARTS table under `## RESTARTS` (523 `DOCS` rows summarised, every other row verbatim).
- `LINE MOVED`: none.
- No path edited outside the 2 row files; no row edited beyond its OLD block.

## CONTINUE
next: CLOSE (all steps done; lock released; `cobalt_dev` at 0013)

## ESCALATE
1. ESCALATE: UNCLASSIFIED `.clinerules` (`cobalt jobs restarts 10163d51..7cdc5774` row 3, exit 1). It arrives through the merge from main, not through fix r1 or r2. It widens `RESTARTS:` to every resident. This is the DRC deploy's L42 item. [13:38 EDT]
2. RECORD: `## RESTARTS` quotes the 751-line table with its 523 `DOCS` rows summarised as a count and a line range. `32` asks for the table WHOLE. Every non-`DOCS` row, the header, the ESCALATE line and the `RESTARTS:` line are verbatim. The first foreground run's display was truncated, so the same listed command was re-run in the background to read the full output.
3. RECORD: `<main at launch>` read `72ca55cb`; the desk read `20139f3d` at 13:08. Main moved in between. `git diff --stat daf36e01 main -- . ':(exclude)docs'` is empty, so main is still docs-only since the merge.

DRC MERGE FIX R2 BUILT 7cdc5774 | on 4fc270c7 | files: 2 (src 1, tests 1) | offline 3547/0 | with-DB 4066/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | FIX: 2 | ESCALATE: 3
