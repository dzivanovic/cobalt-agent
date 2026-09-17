# S2-P4 build — Chunk A (STEP-1, STEP-2, STEP-3) — Opus 5 headless — 2026-09-17

## §0 Headline
- Chunk A (STEP-1 migrations 0008/0009, STEP-2 value column, STEP-3 F3 picks) is **built in the working tree and not committed**. This is one run over the whole chunk: I verified the killed run's partial work (`6642416`), kept all of it, added two test strengthenings and wrote DevDocs for all 14 touched `.py` files (1 new page, 13 updated).
- Offline suite: `1215 passed, 257 skipped`. Every `requires_db` test is written and skips cleanly offline; **the hub runs them on cobalt_dev** (L41 interim). None has been run against a database yet.
- Every §4 test name owned by STEP-1/2/3 exists (tables below). Hub-cut fixtures untouched. No new dependency, no person/vendor name in any identifier.
- ESCALATE: 0. Open notes for the hub/reviewer: §5.

## §1 Files changed (whole chunk, vs `main`; excludes the hub's STEP-1 fixture commit `c87ec92`)

| File | Change |
|---|---|
| `src/cobalt/db_migrations/0008_radar_value_movers.sql` (+ `.rollback.sql`) | new, SYSTEM side: `radar_membership.rank_metric/rank_value`; `system.movers_daily` (owned by `cobalt_system`, `active` + `replay_run_id`, partial unique on active, `SELECT, REFERENCES` + sequence grant to `cobalt_user`) |
| `src/cobalt/db_migrations/0009_picks_missed.sql` (+ `.rollback.sql`) | new, USER side: `"user".picks`, `"user".missed` (owned by `cobalt_user`; `user_id NOT NULL` + FK + GUC default; immutable `receipt`; `run_seq`/`is_current`/`superseded_by`/`retired_by_run_id`; partial unique `missed_one_current_per_subject WHERE is_current`, formation-extended) |
| `src/cobalt/db_migrations/__init__.py` | FORWARD/REVERSE entries for 0008/0009 |
| `src/cobalt/db_migrations/cli.py` | `DIGEST_EXCLUDED_COLUMNS` += `rank_metric`, `rank_value` (R1-1) |
| `src/cobalt/db_migrations/placement.py` | `CREATED_TABLES`: `movers_daily` SYSTEM, `picks`/`missed` USER; `missed` removed from `DECLARED_TABLES` |
| `src/cobalt/radar/models.py` | `RankMetricName`; `OpenMember.rank_metric/rank_value` (R2-2) |
| `src/cobalt/radar/pool.py` | `_ranked` returns `values`; `Transition.rank_metric/rank_value` set on RETAIN/ADMIT/EXCLUDE, prior pair carried on HOLD; also fixes a latent `TypeError` in the list-union sort key |
| `src/cobalt/radar/store.py` | reads select both columns; writes them on RETAIN/EXCLUDE/INSERT; HOLD keeps its values via COALESCE; LEAVE untouched |
| `src/cobalt/aset/radar_panel.py` | `MembershipRecord`/`PoolRow` fields (R1-19); `value` column; `—` for NULL |
| `src/cobalt/cards/picks.py` | **new**: `record_pick`, pool/score snapshots, cohort rank + tie policy, `render_picks_report` |
| `src/cobalt/cards/models.py` | `FillResult` (typed, validated) |
| `src/cobalt/cards/store.py` | `fill()`: one USER transaction on every route, `SAVEPOINT pick`, `logger.error` on pick failure, returns `FillResult`; `filled_with_picks(day)` |
| `src/cobalt/cards/cli.py` | `cobalt cards picks [--date] [--cutoff]` (MISSING → exit 1); `move … FILLED` exits 1 when the pick was not recorded |
| `src/cobalt/cards/__init__.py` | exports `FillResult`, documents `picks.py` |
| `src/cobalt/aset/store.py` | `mark_filled` returns the `FillResult` (R1-5) |
| `src/cobalt/aset/web.py` | `_pick_banner`, appended on both HTTP fill routes |
| `tests/cobalt/test_p4_migrations.py` | new (strengthened this run) |
| `tests/cobalt/test_cards_picks.py` | new (strengthened this run) |
| `tests/cobalt/test_radar_pool.py`, `test_radar_store.py`, `test_radar_panel.py`, `test_radar_runner.py`, `test_aset_web.py`, `test_tenancy.py`, `test_radar_migration.py`, `test_cards.py`, `test_aset_store.py` | new tests; existing tests adapted to appended migrations and the `FillResult` return |
| `docs/40 - DevDocs/cobalt/cards/picks.md` | **new** page |
| `docs/40 - DevDocs/cobalt/{cards/store,cards/models,cards/cli,cards/__init__,aset/store,aset/web,aset/radar_panel,radar/models,radar/pool,radar/store,db_migrations/__init__,db_migrations/cli,db_migrations/placement}.md` | dated `2026-09-17 — S2-P4` sections |

This run changed only `test_p4_migrations.py`, `test_cards_picks.py` and the 14 DevDoc pages. Everything else is the killed run's work from `6642416`, which I verified line by line against the plan and kept unchanged.

## §2 Tests added (names)

**§4 names owned by chunk A — all present**

| §4 area | Test | File | Offline / requires_db |
|---|---|---|---|
| F3 | `test_fill_writes_exactly_one_pick_row_in_the_fill_transaction` | test_cards_picks | db |
| F3 | `test_pick_row_snapshots_pool_rank_metric_and_value_at_pick_time` | test_cards_picks | db |
| F3 | `test_pick_for_ticker_not_in_pool_records_not_in_pool_and_fill_succeeds` | test_cards_picks | db |
| F3 | `test_degraded_or_missing_pool_row_writes_named_nulls_never_refuses_fill` [missing/degraded/failed] | test_cards_picks | db |
| F3 | `test_pick_insert_failure_rolls_back_savepoint_only_fill_commits_banner_and_log` | test_cards_picks | db (this run: added log + banner asserts) |
| F3 | `test_picks_cli_reports_savepoint_gap_as_missing` | test_cards_picks | db |
| F3 | `test_card_score_rank_unavailable_before_p2_named_in_score_basis` | test_cards_picks | db |
| F3 | `test_picks_cli_lists_pick_and_rank_for_every_filled_card_and_exits_1_on_missing` | test_cards_picks | offline |
| Value | `test_rank_value_written_on_retain_exclude_insert_with_ranking_metric` | test_radar_store | offline |
| Value | `test_screen_override_metric_value_recorded_under_override_name` | test_radar_pool | offline |
| Value | `test_list_sourced_value_is_max_across_lists` | test_radar_pool | offline |
| Value | `test_hold_keeps_prior_value` | test_radar_pool | offline |
| Value | `test_pre_deploy_null_value_renders_dash` | test_radar_panel | offline |
| Value | `test_pool_view_shows_value_beside_metric_name` | test_radar_panel | offline |
| Tenancy | `test_placement_movers_daily_system_picks_and_missed_user`, `test_0009_user_tables_carry_user_id_not_null_fk_and_guc_default`, `test_rollback_down_to_0007_reverses_0009_then_0008_only`; `TestTenantGuc.test_every_user_table_carries_user_id_not_null_with_the_guc_default` (now covers CREATED_TABLES) | test_p4_migrations / test_tenancy | offline / db |

**Amendment coverage (Astra)**

| Amendment | Tests |
|---|---|
| R1-1 both orders, apply twice, reverse/reapply, digest | `test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership[p2_before_p4 / p4_before_p2]` (db), `test_0008_rank_columns_are_constrained_and_digest_excluded`, `test_0008_0009_name_nothing_of_the_p2_seam_so_either_merge_order_applies` |
| R1-2 owner/grants/real roles | `test_0008_owner_and_grants_for_movers_daily`, `test_side_roles_ownership_identity_guc_and_wrong_side_through_real_roles` (db) |
| R1-3 placement / one side | `test_0008_creates_only_system_objects_and_0009_only_user_tables`, `test_rollbacks_drop_only_their_own_objects`, `test_0008_0009_registered_forward_in_version_order_with_named_rollbacks` |
| R1-8 / R2-1 / R3-1 receipt + versioning | `test_missed_carries_an_immutable_receipt_and_current_versioning`, `test_missed_rerun_reconciles_in_the_ruled_order_against_the_live_unique_index` (db; this run: retire-without-replacement + current-with-successor CHECK asserts) |
| R1-4 one transaction, every route | `test_every_fill_route_runs_in_one_transaction_with_the_pick_savepoint[WATCH/ARMED/TRIGGERED manual/TRIGGERED radar]`, `test_pick_insert_failure_rolls_back_savepoint_only_and_logs_card_and_error_class[WATCH/TRIGGERED]`, `test_a_fill_transaction_failure_never_reports_success`, `test_a_savepoint_rollback_that_fails_fails_the_fill` |
| R1-5 typed result, both HTTP routes, figures persist | `test_fill_result_is_typed_and_a_recorded_pick_carries_its_id`, `TestPickNotRecordedBanner.test_fill_form_route[True/False]`, `.test_card_move_fill_route[True/False]`, `test_mark_filled_figures_persist_after_a_pick_failure` (db) |
| R1-6 USER reads, cohort includes pick, ties | `test_record_pick_reads_system_tables_qualified_on_the_passed_connection`, `test_user_side_reads_qualified_radar_tables` (db), `test_card_score_rank_ties_share_a_rank_and_the_cohort_includes_the_picked_card`, `test_score_basis_flips_to_card_score_when_the_p2_columns_are_present` (db), `test_no_taps_names_the_score_basis` (db), `test_picks_record_the_replay_inputs_for_pool_and_score_rank` |
| R1-7 FILLED transitions, K6 cutoff | `test_picks_cli_cutoff_keeps_pre_deploy_missing_visible_without_counting_it`, `test_picks_cli_command_exit_codes` |
| R1-19 query→model→HTML | `test_pool_view_shows_value_beside_metric_name`, `test_membership_row_without_the_value_columns_fails_loud`, `test_open_members_and_members_for_day_select_both_columns` |
| R2-2 OpenMember through resident scan | `test_open_member_values_flow_through_the_resident_scan_and_hold_preserves_them`, `test_ranked_transitions_carry_the_session_metric_and_value_on_retain_admit_exclude`, `test_hold_update_keeps_the_prior_pair_when_the_transition_carries_none`, `test_leave_does_not_touch_the_last_values`, `test_membership_values_round_trip_retain_and_hold_on_cobalt_dev` (db) |

## §3 Suite result (verbatim)

`uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider`:
```
1215 passed, 257 skipped, 15 warnings in 24.65s
```
The 15 warnings are the existing litellm `asyncio.iscoroutinefunction` DeprecationWarning in `tests/taxonomy/test_names_rule.py`.

P4 files alone, `-rs`: `25 passed, 17 skipped`. Every skip reads `requires_db: Postgres env settings not available`, and there are no errors.

## §4 Deviations from the plan's DDL text (each required by an amendment)

| Object | Plan text | Built | Why |
|---|---|---|---|
| `movers_daily` | `UNIQUE (trade_date, side, ticker)` | `active BOOLEAN`, `replay_run_id TEXT NOT NULL`, partial unique index `WHERE active` | R1-20/R2-1: rows are deactivated, never deleted, so the FK from `missed.mover_id` holds and a rerun can select a new row |
| `missed` | `replay_job_id`, `missed_one_per_subject` | `receipt JSONB NOT NULL`, `replay_run_id`, `run_seq`, `is_current`, `superseded_by`, `retired_by_run_id`, `formation_at`; partial unique `missed_one_current_per_subject` including `formation_at` and the formation member | R1-8, R2-1/R3-1, R1-21 |
| `missed` CHECKs | — | `is_current OR retired_by_run_id IS NOT NULL`; `superseded_by IS NULL OR NOT is_current`; formation rows need md5 + formation_at + member | makes the retire/insert/link order enforceable, not just conventional |
| `picks` | — | `pool_basis TEXT NOT NULL`, `score_inputs JSONB NOT NULL`, `created_at`; `transition_id` gains an FK to `"user".card_transitions` | R1-6 / L57 (the stored inputs that replay the rank); same-side FK |

## §5 What I could not do, and why

1. **No `requires_db` test was run** (17 in the P4 files, plus the adapted tenancy/radar-store DB tests). I have no database or credentials (L41 interim). The hub runs them on cobalt_dev with 0008/0009 applied. Two to watch there:
   - `TestFillWritesPick.test_score_basis_flips…` and `test_no_taps…` run `ALTER TABLE aset_sizings ADD COLUMN` on the shared rolled-back session. This needs the session role to own `aset_sizings`, which I did not verify.
   - The both-orders proof models P2 by adding only the two columns P4 reads (`card_score`, `conviction`), because P2's 0006/0007 are not in this tree. The hub reruns it after rebasing onto a tree with P2 merged.
2. **I cannot show "failing test first" for the inherited work.** The killed run left code and tests together in one wip commit, and there is no record of test-before-code order. The two assertions added in this run are `requires_db`, so they cannot go red offline either.
3. **P2 binding:** P2 is not merged into `main` (hub STEP-0 facts). I read P2's shipped names directly from `/Users/cobalt/cobalt-wt/s2-p2-cards/src/cobalt/db_migrations/0007_radar_cards.sql` (read-only): `aset_sizings.card_score INTEGER` and `conviction NUMERIC(8,6)`. They match what `picks.score_snapshot` reads. P4 duplicates no P2 table or seam. The cohort is P2 `origin='radar'` cards in WATCH/ARMED/TRIGGERED plus the picked card.
4. **P2 rollback interaction (R1-23):** if P2's 0007 rollback deletes radar cards that `picks`/`missed` reference, the NO ACTION foreign keys block it and it fails loud. That is "blocked, never silent". The hub's both-order rollback proof on populated data is still owed.
5. **Not verified by me:** `git check-ignore` on the new paths needed an approval this headless session could not get. The `.gitignore` carve-out `!docs/40 - DevDocs/**` covers them. The hub should confirm before committing.
6. **Out of scope for chunk A:** STEP-4..9 (replay job, cf-R, movers collector, miss line, smoke), the ADR-0010 note and the BACKLOG row. The replay-logic tests listed under R2-1 (bar correction, mover leaving the benchmark, identical-rerun idempotency, resume between steps) belong to STEP-5/6 code. Only their schema half (the retire/insert/link order against the live index) is covered here.
7. Staging file `scratch/p4-devdoc-sections.md` (gitignored `scratch/`) holds the DevDoc sections I appended. It is safe to delete.

RESTARTS (expected, per plan §5; the hub derives it with `cobalt jobs restarts main..HEAD`): `com.cobalt.radar` (radar/pool.py, radar/store.py, radar/models.py) and `com.cobalt.aset` (cards/*, aset/*). Chunk A adds no plist.
