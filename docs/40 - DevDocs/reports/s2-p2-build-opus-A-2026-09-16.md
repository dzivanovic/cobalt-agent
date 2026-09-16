# REPORT — S2-P2 build, chunk A (STEP-1..3) — 2026-09-16

Seat: Opus 5, builder, headless (L29 floor, L50) · Branch `sprint-2/cards` · Worktree `~/cobalt-wt/s2-p2-cards` · Plan `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md` · No DB, no credentials (L41 interim) · Not committed (hub commits, L46).

## §0 Headline

- STEP-1 migrations 0006 (system) and 0007 (user), STEP-2 predicate grammar, and STEP-3 anatomy detectors plus the daily-bars collector are BUILT, with every STEP-1/2/3 amendment (Astra R1-1/2/3/4/8/9/10/12/13, R3-1).
- Suite: `1361 passed, 268 skipped` (`uv run pytest -q tests/cobalt tests/taxonomy`). The `requires_db` and `requires_vault` tests are written and SKIP offline; the hub runs them.
- The dry-run CLI `cobalt radar evaluate --replay` moves to chunk B, because it needs the S5 stage (allowed by the brief).
- ESCALATE: 2 (see bottom).

## Files changed (main..worktree)

| Area | File | Change |
|---|---|---|
| STEP-1 | `src/cobalt/db_migrations/0006_radar_score.sql` (+ `.rollback.sql`) | new: `radar_score_run`, `radar_score`, `radar_board_v`, `desk_regime`/`desk_packet`/`desk_grade`; `failed_stage` gains `evaluate` (name read from `pg_constraint`); owners, sequence grants, `REFERENCES` for `cobalt_user`; idempotent |
| STEP-1 | `src/cobalt/db_migrations/0007_radar_cards.sql` (+ `.rollback.sql`) | new: nullable sizing and 25 card columns on `aset_sizings`, manual-sized and radar-provenance CHECKs, DB-level one-open-radar-card partial unique index, `card_dots`, `card_dot_taps`, `radar_score_receipt` (stored values, not just hashes), UPDATE-refusing immutability trigger on receipt and taps, executable `radar_cards_v` and `shadow_agreement_v`; idempotent; the reverse deletes radar rows before restoring NOT NULL |
| STEP-1 | `src/cobalt/db_migrations/__init__.py` | 0006/0007 in `FORWARD`; reverses first in `REVERSE` |
| STEP-1 | `src/cobalt/db_migrations/placement.py` | 5 SYSTEM and 3 USER `CREATED_TABLES`; new `CREATED_VIEWS` (3) folded into `PLACEMENT` |
| STEP-1 | `src/cobalt/db_migrations/cli.py` | `TABLE_DIGEST_EXCLUDED_COLUMNS`, so the migrate proof excludes the 0007 card columns from the `aset_sizings` digest only |
| STEP-1 | `src/cobalt/radar/seam.py` | new: closed payload models for `radar_score.detail` / `desk_shadow` (R1-1) |
| STEP-2 | `src/cobalt/taxonomy/predicate.py` | new: tokenizer, recursive-descent parser, frozen Pydantic AST, `render`, `required_atoms` |
| STEP-2 | `src/cobalt/taxonomy/trade_def.py` | `Predicate` parses `expr` at validation; private `_ast`, `ast`, `required_atoms` |
| STEP-2 | `src/cobalt/taxonomy/vault_loader.py` | `_locate_predicate_errors`: note path, line, slug and expression on a parse failure |
| STEP-3 | `src/cobalt/radar/anatomy/{__init__,bars,indicators,leg,extension,structure,daily,registry,freshness}.py` | new: detectors (see DevDocs) |
| STEP-3 | `src/cobalt/radar/collector.py` | `DailyBarsSource` interface, `FinvizDailyBarsCollector` (ET-day cache, shared bucket), recursive `prune_cache`, `DAILY_RETRIES_PER_REQUEST` |
| STEP-3 | `src/cobalt/radar/notes.py` | `TransportDemand` + `plan_transport_demand` (every consumer, cold burst, retries, actual pacing); `load_sources(context_tickers=)` required |
| STEP-3 | `src/cobalt/radar/propose.py` | `screens validate` uses the same demand plan and prints the daily drain |
| STEP-3 | `src/cobalt/radar/config.py`, `configs/cobalt/radar.yaml` | required `context.tickers` (ships `[]`, per STEP-0 stale ETF coverage) |
| STEP-3 | `configs/cobalt/taxonomy/tunables.yaml` | `extension.path_a_volume_ma_bars` 20, `extension.path_a_volume_sigma` 2, `extension.leg_base` session_open, `range_break.htf_range` prior_session_high_low, all `replay_pending`; `extension.path_b_atr` consumer added |
| tests | `tests/cobalt/test_tenancy.py`, `test_radar_migration.py`, `test_radar_notes.py`, `test_radar_replay.py`, `test_radar_runner.py`, `test_radar_sources.py`, `test_sheet_daymode_probe.py` | amended: new migrations by name, stores `RadarStore`/`TraderSettingsStore` in the side lint, user_id assertion extended to `CREATED_TABLES`, `context_tickers=0`, probe list includes `radar` |
| DevDocs | new: `taxonomy/predicate.md`, `radar/seam.md`, `radar/anatomy/{__init__,bars,indicators,leg,extension,structure,daily,registry,freshness}.md` · updated: `db_migrations/{__init__,cli,placement}.md`, `radar/{collector,config,notes,propose}.md`, `taxonomy/{trade_def,vault_loader}.md` | agent-authored |

Fixtures under `tests/fixtures/radar/` are hub-cut; I used them but did not edit or add any. No Rubberband note content is in the repo.

## Tests added

| File | Tests |
|---|---|
| `tests/cobalt/test_radar_score_migration.py` | `test_0006_and_0007_are_registered_forward_in_order` · `test_rollback_selects_0007_then_0006_newest_first` · `test_placement_declares_the_new_tables_and_views_on_their_sides` · `test_0006_creates_only_system_relations_and_0007_only_user_relations` · `test_every_new_relation_is_owned_by_its_side_role` · `test_cross_side_references_are_granted_in_0006` · `test_every_user_table_carries_user_id_not_null_fk_and_guc_default` · `test_forward_ddl_is_guarded_for_a_second_run` · `test_views_have_executable_definitions` · `test_0006_widens_failed_stage_by_reading_the_constraint_from_the_catalog` · `test_radar_score_is_system_payload_only_no_trade_def_content_columns` · `test_0007_card_checks_and_one_open_radar_card_index` · `test_receipt_and_taps_are_immutable_at_the_database` · `test_0007_rollback_drops_dependents_before_columns_and_restores_not_null_last` · `test_digest_excludes_every_column_0007_adds_to_aset_sizings` · **requires_db (hub):** `test_migrate_twice_is_idempotent_on_cobalt_dev` · `test_owner_is_the_side_role` · `test_system_side_inserts_seam_rows_and_user_side_cannot` · `test_system_side_cannot_read_the_new_user_relations` · `test_user_side_reads_the_new_system_relations_qualified` · `test_new_user_tables_carry_user_id_not_null_with_guc_default` · `test_card_checks_index_and_receipt_immutability_on_cobalt_dev` |
| `tests/cobalt/test_tenancy.py` (amended) | `test_down_to_0004_selects_0007_0006_then_0005_reverse`; the placement/user_id/side-lint checks extended to the new tables and stores |
| `tests/cobalt/test_radar_seam.py` | `test_a_generic_detail_and_desk_shadow_validate_and_round_trip` · `test_unknown_keys_are_refused` · `test_an_atom_must_be_a_bare_reference_without_cfg_or_prose` · `test_a_symbol_is_one_lowercase_word_and_observation_names_are_identifiers` · `test_desk_shadow_grade_bounds_and_na_reasons_are_closed` · **`test_radar_score_carries_no_trade_def_content`** · requires_db: `test_no_system_side_row_contains_trade_def_or_settings_content` |
| `tests/taxonomy/test_predicate.py` | `test_every_inventory_form_parses_and_renders_stably` (every inventoried form) · `test_ast_is_frozen_pydantic` · `test_precedence_not_binds_tighter_than_and_binds_tighter_than_or` · `test_comparison_right_hand_bare_word_is_a_symbol_not_an_atom` · `test_in_takes_a_set_or_a_cfg_with_unit` · `test_relations_and_qualifiers_have_their_own_nodes` · `test_a_relation_word_followed_by_a_paren_is_a_call` · `test_named_argument_and_division` · `test_required_atoms_for_the_extension_reversal_predicates` · `test_required_atoms_names_calls_whole_and_skips_cfg_numbers_symbols` · `test_bad_expression_fails_loud_with_position_and_text` · `test_predicate_model_parses_expr_at_validation` · `test_ast_does_not_leak_into_the_stored_def_json` · `test_shipped_synthetic_note_parses` · `test_a_syntax_error_in_a_note_names_note_path_line_slug_and_expression` · `test_an_unknown_cfg_inside_an_expression_fails_loud` · **requires_vault (hub, `COBALT_LIVE_VAULT_ROOT`):** `test_all_live_defined_notes_parse_and_report_missing_atoms` |
| `tests/cobalt/test_radar_anatomy.py` | completeness: `test_first_minute_of_a_bucket_is_never_a_closed_working_bar` · `test_a_missing_second_minute_is_flagged_incomplete` · `test_complete_bucket_matches_the_archiver_aggregate_and_future_bars_are_ignored` · `test_odd_scan_time_closes_only_whole_buckets` · `test_rth_only_drops_premarket_buckets_at_the_session_boundary` · `test_real_shape_buckets_flag_completeness_by_minutes_present` · `test_real_shape_replay_never_reads_a_bar_after_as_of` · `test_mixed_tickers_or_non_i1_input_is_refused` · math: `test_wilder_atr_seed_warmup_and_independent_recompute` · `test_volume_band_uses_prior_n_population_sigma` · `test_legs_terminate_on_one_opposing_bar_and_dojis_continue` · `test_legs_mirror_for_a_down_run` · extension: `test_path_a_climax_bar_is_culminating_in_both_directions` · `test_high_volume_but_not_the_widest_body_is_not_path_a` · **`test_path_b_only_formation_is_not_evaluable`** · `test_quiet_run_is_not_instantiated` · `test_warm_up_and_incomplete_buckets_make_extension_unavailable` · `test_extension_params_come_from_tunables_rows` · `test_new_definition_tunables_are_replay_pending_dwv` · structure: `test_tracked_extreme_is_the_run_high_for_up_and_low_for_down` · `test_bar_break_trigger_clears_both_of_the_last_n_completed_bars` · `test_structural_stop_buffer_and_nudge` · daily: `test_parse_daily_export_shape_and_refusals` · `test_prior_session_never_reads_trade_date_or_later` · `test_daily_atr_on_real_shape_rows_matches_independent_recompute` · `test_htf_level_proximity_nearest_prior_level_in_daily_atr_units_symmetric` · `test_htf_day_count_continuity_up_and_down` · registry: `test_extension_reversal_shape_is_evaluable` · `test_unsupported_atoms_trigger_and_stop_are_named_missing` · `test_sequence_trigger_is_named_missing_not_a_crash` · `test_shipped_synthetic_def_reports_not_evaluable_with_its_missing_atoms` · `test_supported_atoms_are_exactly_the_s2_detectors` |
| `tests/cobalt/test_radar_daily.py` | `test_daily_collector_satisfies_the_collector_interface` · **`test_daily_fetch_once_per_name_per_day_cached`** (includes restart cache hit) · `test_cache_day_is_the_et_day_and_rolls_over_at_et_midnight` · `test_bad_daily_body_is_a_source_failure_and_nothing_is_cached` · `test_redirected_daily_fetch_degrades` · `test_retention_prunes_date_directories_with_a_nested_daily_dir` · `test_screener_cache_write_survives_an_old_day_with_nested_daily` · **`test_total_finviz_demand_refuses_when_sum_exceeds_ceiling_while_each_consumer_alone_passes`** · `test_cold_cache_burst_on_a_near_full_scan_describes_actual_pacing` · `test_collector_retry_constant_is_what_the_demand_check_uses` · `test_load_sources_counts_daily_and_context_in_the_ceiling` · `test_radar_config_declares_context_tickers` |
| `tests/cobalt/test_radar_freshness.py` (R1-12) | `test_rvol_observation_is_timestamped_with_its_source` · `test_duplicate_ticker_precedence_is_screen_then_note_order_then_source_id` · `test_missing_rvol_is_kept_as_an_explicit_none_never_dropped_or_zeroed` · `test_degraded_and_inactive_sources_carry_no_rvol` · `test_rvol_observed_at_must_be_aware` · `test_intraday_ttl_is_two_scan_intervals` · `test_intraday_observation_from_the_future_is_refused` · `test_previous_trading_day_skips_weekends_and_holidays` · `test_daily_ttl_is_the_session_boundary_not_a_wall_clock` · `test_policy_and_tunable_inputs_never_go_stale_on_a_wall_clock` |

Bold = the §4 name used exactly.

## Suite result (verbatim)

```
$ uv run pytest -q tests/cobalt tests/taxonomy
1361 passed, 268 skipped, 15 warnings in 24.59s
```

The 15 warnings are the existing litellm `asyncio.iscoroutinefunction` deprecation in `test_names_rule.py`.

## Not done here, and why

| Item | Why | Where it lands |
|---|---|---|
| `requires_db` tests executed (migrate twice, side-role owner/insert/refusal, receipt immutability, no system-side user content) | No DB or credentials for workers (L41 interim) | Hub, on `cobalt_dev` |
| `requires_vault` live-note grammar proof executed | Brief: the hub runs it. My read-only attempt needed an approval that isn't available headless | Hub: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q tests/taxonomy/test_predicate.py -k live` |
| Dry-run CLI `cobalt radar evaluate --replay <date> [--trade-def]` | Needs the S5 stage | Chunk B (STEP-4) |
| Persisting RVOL observations into the receipt; marking `input_stale` | Both are S5 writes; the pure decision functions (`anatomy/freshness.py`) land now | Chunk B (STEP-4) |
| "never a card" half of `test_def_without_evaluable_precondition_renders_not_evaluable_never_a_card` | Card creation is S5; the registry half (named missing atoms) is tested now | Chunk B |
| Context tickers (SPY + sector ETFs) joining S4 polling | STEP-0: 11 of 14 context tickers have had no bars since 2026-09-03; `context.tickers: []` is counted as zero demand, and the alignment dots will render N/A | Hub/Dejan once coverage is verified |

RESTARTS: not derived by the builder. The hub runs `cobalt jobs restarts main..HEAD`. Plan §5 expects `com.cobalt.radar` and `com.cobalt.aset`, because `tunables.yaml` and `radar.yaml` changed and `radar`/`taxonomy` modules are imported.

## ESCALATE (2)

1. **Out-of-process Finviz consumers are outside the total-demand plan (L53).** The plan counts every consumer inside the `com.cobalt.radar` resident: pool bars, screens, list chunks, context tickers and daily bars. It does not count three scheduled jobs that call the same Finviz transport without the resident's bucket. `com.cobalt.prefill-daily` runs at 05:15 ET, inside the premarket scanning session. `com.cobalt.prefill-drc` runs at 15:40 ET, inside RTH. `com.cobalt.archiver` runs at 20:30 ET, in the pause, so it doesn't collide. The prefill jobs' `p=d` fetches also duplicate the new daily cache. This gap existed before this build and is outside plan F18's scope (`notes.py`/`propose.py`). Needs a ruling: a cross-process demand ledger, prefill reading the daily cache, or accept as is.
2. **The grammar inventory came from the defs' last in-repo copy (commit `96c9159^`) plus the plan's named live forms, not from the live notes.** Parsing runs for every loaded def, so a form that exists only in the live notes would fail `cobalt taxonomy load` for the whole taxonomy (R1-4). The hub's `requires_vault` run is the gate and must pass before merge.
