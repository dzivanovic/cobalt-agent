# REPORT — S2-P2 build, chunk B (STEP-4..7) — 2026-09-16

Seat: Opus 5, builder, headless (L29 floor, L50) · Branch `sprint-2/cards` · Worktree `~/cobalt-wt/s2-p2-cards` · Plan `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md` · No DB, no credentials (L41 interim) · Not committed (hub commits, L46).

## §0 Headline

- **Built:**
  - STEP-4: S5 evaluate stage, runner wiring, the `--replay` dry run (writes nothing) and the cobalt_dev candidate harness;
  - STEP-5: dots and scoring;
  - STEP-6: snap-down ladder sizing, the tap/pass/dot/promote routes, and the R1-5 card-settings loader with `--sha256`;
  - STEP-7: health pills, 8 `card.health.*` rows, EMA9;
  - every STEP-4 Astra amendment (R1-6/7/11/14/15/16).
- **Suite:** `1465 passed, 278 skipped` (`uv run pytest -q tests/cobalt tests/taxonomy`). Chunk A was 1361/268.
- **Not run here:** the `requires_db` tests (8 new in `test_radar_cards_db.py`, 1 in `test_card_settings.py`) and the `requires_vault` S5 test are written and SKIP offline; the hub runs them. `cobalt validate` was not run (see "Could not do").
- **Changed a chunk A migration:** 0007 gains one idempotent partial unique index (one promoted card per trader), with a matching rollback line. Re-run `cobalt db migrate` on cobalt_dev before the DB tests.
- **ESCALATE: 5** (bottom).

## Files changed (worktree vs HEAD `3ebe3cc`)

| Area | File | Change |
|---|---|---|
| STEP-4 | `src/cobalt/radar/evaluate.py` | new: `evaluate_member` (three-valued predicate interpreter, direction from `valid_setups` relation, trigger/stop, factor observations, closed seam payload), `EvaluateStage` (publish ordering, create/refresh/expire, departed-member lifecycle, receipt), receipt chaining, `replay_receipt`, `formula_sha256` |
| STEP-4 | `src/cobalt/radar/evaluate_cli.py` | new: `replay_formations` (writes nothing), `CachedDailyBars`, `candidate_run` (cobalt_dev only, frozen D2 settings, simulated taps, full curve coverage, RVOL from the day's receipts) |
| STEP-4 | `src/cobalt/radar/runner.py` | `evaluator` + `ceiling_rpm` on `RadarRunner`; lifecycle polling inside the ceiling; S5 after S4 behind the gate; `failed_stage='evaluate'` stamping; `build_runner` wires the stage (rung from `DayModeStore` + `decided_or_stage1`) |
| STEP-4 | `src/cobalt/radar/store.py` | system-side seam methods: `admitted_members`, `memberships`, `i1_bars`, `latest_run_id`, `abandon_running_runs`, `open_score_run`, `put_scores` (re-validates seam models), `copy_card_values`, `finish_run`, `board`, `members_for_replay` |
| STEP-4 | `src/cobalt/radar/notes.py` | `LifecycleDemand` + `lifecycle_poll_demand` (total-demand check for departed-card tickers) |
| STEP-4 | `src/cobalt/radar/cli.py` | `radar evaluate --replay | --candidate [--trade-def --settings-file --sha256 --taps]` |
| STEP-4 | `src/cobalt/cards/expire.py` | `radar_deadline` (from `preferred_windows_ref`, persisted at formation), `radar_expiry` (stop-before-arm WATCH only → avoid → deadline; FILLED/terminal never) |
| STEP-4/6 | `src/cobalt/cards/store.py` | ARM invariant inside the locked `transition()`; `before_commit` on `transition`; unsized stop edit; `create_radar_card` (`ON CONFLICT … DO NOTHING` on the partial index + genesis + dots, one tx); `refresh_radar_card` (never overwrites taps); `expire_radar_card`; `write_receipt`, `receipts_chain`, `receipts_for_day`; `open_radar_cards`, `formation_consumed`, `radar_card`; `tap_key`, `tap_dot`, `set_promoted` (all row-locked) |
| STEP-4/6 | `src/cobalt/cards/radar.py` | new: `RadarCardSpec`, `FIELD_OWNERS`, `ladder_order` (null scores last, deterministic ties, promote to #2 below pinned, rank chip unchanged) |
| STEP-5 | `src/cobalt/cards/scoring.py` | new: `Dot`, `compute_dots` (shadow / desk N/A / human), `grade_from_curve`, `refresh_dots` (stale history), `conviction`, `suppression`, `proximity`, `card_score`, `proposed_key` (via `snap_down`), colours |
| STEP-6 | `src/cobalt/aset/engine.py` | `stop_distance` (factored out of `recompute_for_stop`), `LADDER_KEYS`, `KeyOption`, `key_ladder`, `snap_down`, `KeyRefused`, `size_at_key` |
| STEP-6 | `src/cobalt/aset/web.py` | `POST /radar/card/{id}/key` (A+/A/B/C/pass), `/dot/{factor}`, `/promote`, `/release`; JSON 4xx refusals; F6 `.htk` refusal unchanged; one daily-note unit per card |
| STEP-6 (R1-5) | `src/cobalt/settings/card.py` | new: typed schemas for the five keys, `load_card_file` (sha256 of bytes), `CardSettings.from_rows`, `CardSettingsReader` (per call), `cmd_load_card` (diff, one put with deletes, round trip) |
| STEP-6 (R1-5) | `src/cobalt/settings/cli.py`, `settings/store.py` | `--card` / `--sha256`; `put(..., delete=)` in the same transaction |
| STEP-7 | `src/cobalt/cards/health.py` | new: `HealthThresholds`, `EntrySnapshot`, participation/cost/dot/structural pills, loud `n/a` |
| STEP-7 | `src/cobalt/radar/anatomy/indicators.py` | `ema` + `EmaObservation` (EMA9; convention written down) |
| STEP-4 | `src/cobalt/taxonomy/store.py` | `loaded_for_evaluation()` |
| config | `configs/cobalt/taxonomy/tunables.yaml` | `card.dot.red_max` 3, `card.dot.amber_max` 6, the 8 `card.health.*` rows (P3 R2 table), all with consumers |
| migration | `src/cobalt/db_migrations/0007_radar_cards.sql` (+ `.rollback.sql`) | `aset_sizings_one_promoted_radar_card` partial unique index (idempotent; reverse drops it) |
| tests | `tests/cobalt/radar_p2_support.py` | shared support (not a test module): fixture loaders, the synthetic `example-anatomy-reversal` def built from the shipped example note, in-memory stores |
| DevDocs | new: `radar/evaluate.md`, `radar/evaluate_cli.md`, `cards/scoring.md`, `cards/health.md`, `cards/radar.md`, `settings/card.md` · updated: `radar/{runner,store,cli,notes}.md`, `radar/anatomy/indicators.md`, `cards/{store,expire}.md`, `aset/{engine,web}.md`, `settings/{store,cli}.md`, `taxonomy/store.md`, `db_migrations/__init__.md` | agent-authored |

I did not edit or add any fixture under `tests/fixtures/radar/`. No strategy-note content is in the repo; the synthetic def uses anatomy vocabulary only and its slug starts `example-` (names-rule lint). No new dependency.

## Tests added

Bold = the exact §4 name.

| File | Tests |
|---|---|
| `test_radar_keys.py` | **`test_keys_fixed_dollars_per_sheet_disabled_greyed_with_would_be_dollars`** · **`test_a_plus_tap_on_half_day_records_a_plus_and_sizes_at_a_70_with_notice`** · **`test_tap_snaps_down_only_refuses_when_nothing_enabled_below`** · `test_snap_down_skips_a_disabled_middle_key_and_never_lands_on_d` · `test_a_key_that_is_not_a_ladder_key_is_refused` · `test_stop_distance_keeps_the_side_check_and_needs_no_budget` |
| `test_card_settings.py` (R1-5) | `test_the_five_keys_and_nothing_else` · `test_a_reviewed_file_loads_with_its_hash_and_round_trips` · `test_bad_hash_refused` · `test_unknown_or_malformed_setting_refused` (8 cases) · `test_tunables_only_keys_are_refused_by_the_settings_loader` · `test_absent_dark_only_optional_keys_are_null_and_enabling_requires_them` · `test_the_runtime_reader_refuses_missing_cards_enabled_rather_than_defaulting` · `test_dry_run_prints_the_diff_and_the_hash_and_writes_nothing` · `test_apply_requires_the_hash_verifies_the_round_trip_and_is_one_put` · `test_a_failed_apply_leaves_the_store_untouched` · `test_settings_are_re_read_on_every_call_not_cached` · requires_db: `test_card_settings_apply_and_delete_round_trip_on_cobalt_dev` |
| `test_card_scoring.py` | **`test_computable_dots_scored_1_to_10_with_why_held_in_shadow`** · `test_curve_math_clips_and_rounds_half_up_once` · `test_missing_anchors_are_curve_unset_and_a_manual_factor_is_na` · **`test_judgment_dots_hollow_until_tapped_no_neutral_5`** · `test_desk_dots_are_shadow_na_until_ruled` · **`test_empty_tapped_set_conviction_null_never_zero`** · **`test_missing_required_computed_dot_suppresses_card_score_until_tapped`** · **`test_expired_required_input_suppresses_fresh_grade_history_labelled`** · **`test_card_score_is_round_conviction_times_proximity_times_100`** · **`test_proposed_key_none_without_conviction_and_only_enabled_grades`** · `test_dot_colours_from_the_tunable_thresholds` · `test_the_colour_thresholds_are_tunables_rows_with_consumers` · `test_dot_rows_refuse_a_grade_outside_1_to_10_and_a_bad_role` |
| `test_radar_cards_model.py` | **`test_every_card_field_is_badge_owned`** · **`test_card_carries_setup_trade_trigger_structural_stop_proposed_key_dots_with_why`** · `test_equal_scores_and_all_null_scores_order_deterministically` · **`test_promote_pins_to_2_rank_chip_unchanged_release_restores`** · `test_two_pinned_cards_keep_priority_over_a_promotion` · `test_one_promoted_card_at_most_and_terminal_cards_are_separate` |
| `test_card_health.py` | `test_the_eight_rows_are_the_p3_table` · `test_a_missing_health_row_fails_loud` · `test_participation_ok_warn_bad_at_the_thresholds` · `test_participation_missing_or_zero_baseline_is_loud_na` · `test_cost_ok_warn_bad_at_the_thresholds` · `test_missing_spread_is_loud_na` · `test_graded_dot_ok_warn_bad_and_judgment_dots_never_scored` · `test_structural_touched_warn_lost_on_close_bad_long_and_short` · `test_ema_seed_warmup_and_independent_recompute` · `test_card_health_is_every_class_with_alignment_na` |
| `test_radar_evaluate.py` | **`test_cards_enabled_false_writes_seam_rows_and_no_card`** · **`test_def_without_evaluable_precondition_renders_not_evaluable_never_a_card`** · **`test_path_b_only_formation_is_not_evaluable`** (S5 level) · **`test_one_open_radar_card_per_member_def_direction`** · `test_card_is_born_unsized_in_watch_with_formation_evidence_and_dots` · **`test_expiry_end_of_window_avoid_or_stop`** · `test_no_new_watch_after_the_deadline_and_no_duplicate_for_a_consumed_formation` · `test_a_genuinely_new_formation_is_not_blocked` · `test_stop_touched_before_formation_does_not_expire_the_card` · `test_armed_and_triggered_expire_on_deadline_filled_never` · `test_departed_member_card_keeps_refreshing_and_reentry_makes_no_second_card` · `test_filled_card_gets_an_entry_snapshot_and_health_pills` · `test_settings_are_read_on_every_cycle` · `test_missing_cards_enabled_setting_fails_loud_before_any_write` · `test_publish_is_the_last_write_and_a_failure_leaves_no_published_partial` · `test_a_crash_before_publish_is_abandoned_next_cycle_and_the_retry_makes_no_duplicate` · `test_a_card_refusal_does_not_lose_the_run_but_is_reported` · `test_run_hashes_present` · **`test_every_card_number_replays_from_stored_inputs`** · `test_a_dark_run_replays_from_its_receipt_too` · `test_receipt_chain_stores_deltas_and_refuses_a_tampered_chain` · `test_seam_rows_are_generic_and_carry_no_trade_def_content` · **`test_rubberband_precondition_on_pool_name_produces_card_within_one_scan_interval`** (S1–S5 through `RadarRunner`) · **`test_market_reset_drops_evaluate_stage`** · `test_evaluate_failure_stamps_failed_stage_and_s1_to_s4_stand` · `test_lifecycle_tickers_polled_only_inside_the_demand_ceiling` · requires_vault (hub): `test_live_defined_notes_evaluate_on_the_fixture_bars_and_only_the_evaluable_one_can_form` |
| `test_radar_evaluate_cli.py` | `test_replay_cli_writes_nothing_and_lists_formations` · `test_replay_filters_to_one_trade_def_and_names_not_evaluable_defs` · `test_candidate_harness_requires_full_curve_coverage` · `test_candidate_harness_refuses_outside_dev_and_without_enabled_settings` · `test_candidate_harness_persists_with_frozen_settings_and_simulated_taps` |
| `test_radar_card_routes.py` | `test_a_plus_key_tap_on_the_half_day_records_a_plus_sizes_at_a_70_with_notice` · `test_nothing_enabled_below_is_a_409_with_the_reason_and_no_write` · **`test_key_tap_refused_once_armed`** · `test_the_hotkey_file_mismatch_refusal_is_unchanged` · `test_pass_moves_watch_to_passed_by_you` · `test_a_bad_key_is_refused` · `test_dot_tap_recomputes_with_the_bands_and_todays_enabled_grades` · `test_promote_and_release_routes` · `test_card_routes_refuse_a_dev_instance_without_the_opt_in` |
| `test_radar_cards_db.py` (all requires_db, hub) | `test_s5_end_to_end_writes_on_cobalt_dev_and_replays` · `test_the_database_holds_one_open_radar_card_per_member_def_direction` · `test_unsized_arm_is_refused_inside_the_locked_transition_and_sized_arm_passes` (includes the key/ARM race) · `test_a_stop_edit_before_the_first_key_tap_keeps_sizing_null` · `test_manual_cards_are_unaffected` · `test_dot_taps_append_recompute_and_are_never_overwritten_by_a_scan` · `test_one_promoted_card_and_release` · `test_a_publish_failure_leaves_the_run_unpublished_on_cobalt_dev` |

**Test-first, precisely:** keys, card settings, scoring, card model, health, CLI and routes each ran red (collection error) before their module existed. For S5, `evaluate.py` was drafted before `test_radar_evaluate.py`. The runner-level §4 tests (`…within_one_scan_interval`, `…market_reset…`, `…failure_stamps…`, lifecycle) ran red first, because `RadarRunner` had no `evaluator` yet. The stage-level tests were written against the draft and failed on real defects, which were fixed:
- the stop-touch creation rule;
- the ticker-keyed open-card check for re-entry;
- an avoid assumption in the synthetic def.

## Suite result (verbatim)

```
$ uv run pytest -q tests/cobalt tests/taxonomy
1465 passed, 278 skipped, 15 warnings in 31.88s
```

The 15 warnings are the existing litellm `asyncio.iscoroutinefunction` deprecation in `test_names_rule.py`.

## Could not do, and why

| Item | Why | Where it lands |
|---|---|---|
| Run the `requires_db` tests (9) | No DB or credentials for workers (L41 interim) | Hub, on cobalt_dev, after `cobalt db migrate` (the 0007 index is new) |
| Run the `requires_vault` S5 test | Brief: the hub runs it | Hub: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q tests/cobalt/test_radar_evaluate.py -k live` |
| `cobalt validate` (plan §4 Suite row) | Needs `COBALT_ENV` set inline, which needs an approval not available headless | Hub: `COBALT_ENV=dev uv run cobalt validate` |
| Real two-session concurrency (simultaneous taps, key/ARM race) | The suite's rollback fixture shares one connection | The DB tests prove the lock ordering (state re-read under `FOR UPDATE`; the two partial unique indexes), not a live race |
| `cobalt jobs restarts main..HEAD` | Hub derives RESTARTS (L42) | Expected: `com.cobalt.radar` (runner, evaluate, cards, taxonomy imports; `tunables.yaml`) and `com.cobalt.aset` (web, engine, cards, settings; `tunables.yaml`) |
| STEP-8 panel wiring (`radar_panel` still raises FAILED on any radar card), STEP-9..12 | Outside chunk B | Chunk C / later steps |

## Decisions taken inside the plan's text (for review)

1. **"Formation" for the acceptance test.** A formation is `formed` with its structural stop still untouched by every closed bar since the formation bar closed.
   - On the FTFT fixture the formation first appears on the 11:22 ET bar. While the run extends, validity flickers minute by minute (valid 11:24, not 11:25, valid 11:26, not 11:27, steady from 11:28), because the stop re-anchors 2¢ over each new closed high.
   - The stage makes no card while an unclosed minute prints through the stop, and does not consume the formation.
   - The test proves no valid scan passes without a card, and that the card lands within one scan interval of the start of its valid window.
2. **Existing-card causes.** Stop-touched-before-arm reads the LIVE `stop`, and proximity reads the LIVE `entry`/`stop`. `trigger_price`/`structural_stop` stay immutable evidence (R1-7).
3. **`card.proposed_key` band units** are conviction 0–1 (mean tap ÷ 10), strictly descending. Dejan supplies the values at D2.
4. **Entry snapshot for health** is captured on the first scan that sees the card FILLED, not at the fill tick; `captured_at` records when. Spread has no source in S2, so `cost` is `n/a` everywhere.
5. **Refresh vs tap.** When a tap lands after the stage read a card, the scan's refresh leaves conviction/score/key to the tap route's recompute. That scan's receipt `published` numbers can then differ from the row until the next scan.
6. **Card refusals** (e.g. account mode unresolved) do not fail the run. They stamp `failed_stage='evaluate'`, so `/radar` shows FAILED loudly.

## ESCALATE (5)

1. **Receipt chaining vs R1-10 wording.**
   - Retaining every consumed bar's value on every scan is roughly 1 MB of JSONB per scan at a 50-name pool. So each receipt stores only new or changed rows (`rows_delta`) plus the full set's row count and sha256. Unchanged snapshots point to the previous receipt (`unchanged_since_receipt` + sha256), and replay walks the chain and refuses a mismatch.
   - Every value is still retained in receipts, and replay reads receipts exclusively.
   - But a single receipt is no longer self-contained, and a process restart starts a new full base.
   - Needs a ruling: accept chaining, or store full values per receipt and accept the storage.
2. **`curve_unset` suppresses the score.** The settled rule suppresses on any computed N/A untapped dot, so every card has `card_score = NULL` until D2 curves exist or every computed dot is tapped. That matches R11's "dark bundle has null scores", but it also means taps alone cannot rank a card while curves are unset.
3. **Candidate harness RVOL.** The harness reads RVOL from the day's receipts in cobalt_dev, so the hub must copy the production dark-run receipts (or equivalent captured observations) into cobalt_dev before `--candidate`. `--replay` has no RVOL at all (the RVOL dot shows `input_unavailable`; formations are unaffected).
4. **Deploy order at D1.** S5 fails loud (`failed_stage='evaluate'`, FAILED on `/radar`) until `radar.cards_enabled` exists in `trader_settings`. D1's dark-settings load must precede the `com.cobalt.radar` restart; the plan's §6 D1 order already does this. Also, the chunk A 0007 migration changed in this chunk (a new idempotent index).
5. **Alignment dots ship N/A (`DEFAULT_UNRULED`) through S2.** Per the hub's STEP-0 decision and plan §8 item 4, no with/flat/against map is computed, even though `card.alignment_default` is loadable. Owner and date for the authorizing ruling are still owed.
