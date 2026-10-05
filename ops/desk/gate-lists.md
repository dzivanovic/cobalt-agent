# gate-lists.md — every command ops/desk/gate.sh runs, and the level it holds cobalt_dev to

The ONE home of the pass lists (card 2026-10-03/03 adoption-scripts, row L2; brain-unattended
2026-10-02 A 7). gate.sh reads THIS file from the worktree it gates, never a hub file. Each
`## <name>` holds exactly one backticked line, run as written. A build that adds a with-DB test
needing a level above `0013` edits this file and nothing else: its `--deselect <id>` at the end
of PASS 1, its id at the end of PASS 2. Until card 02 makes BUILD-HUB.md and DEPLOY-HUB.md point
here, the hub lines and these stay byte-equal (tests/ops/test_gate.py).

`## LEVEL <nnnn>`: the two lines `cobalt db migrate --proof-only` prints last (L1), as cobalt_dev
must show them at that level, `TABLES …` and `FINGERPRINT …` joined by ` · `; the ROLLBACK goes
`--down-to` that same level. ALLOWED SKIPS: the skips DEPLOY-HUB.md STEP-G (c) allows, ` · `
between items; an item is a path (with `:<line>` when the hub gives one), the test's name when
the hub names one (a `test_…` word: pytest's `-rs` line does not print it, so it is a label), and
the words its reason must hold.

## OFFLINE
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`

## PROOF ONLY
`COBALT_ENV=dev uv run cobalt db migrate --proof-only`

## PASS 1
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --db-only --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py`

## FORWARD
`COBALT_ENV=dev uv run cobalt db migrate`

## PASS 2
`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones tests/cobalt/test_drc_d5_db.py tests/cobalt/test_drc_d5_experiments_db.py tests/cobalt/test_f15_p2_replay_db.py`

## STRAY ROWS
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN (<every constructed ticker your with-DB tests write, each quoted>) GROUP BY ticker"`

## LIVE-NOTE
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py`

## ROLLBACK
`COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013`

## FINGERPRINT
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## ALLOWED SKIPS
`tests/cobalt/test_cards_picks.py:388 · tests/cobalt/test_cards_picks.py:401 · tests/cobalt/test_radar_evaluate.py:695 · tests/taxonomy/test_catalyst.py:365 · tests/taxonomy/test_predicate.py:262 · test_replay_line.py COBALT_TEST_LIVE_DRC · tests/cobalt/test_s3_c4_experiments.py test_x14_live_his_template_strips_to_the_committed_fixture`

## LEVEL 0013
`TABLES 0011 · FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`
