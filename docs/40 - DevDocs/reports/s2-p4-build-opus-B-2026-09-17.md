# S2-P4 build — Chunk B (STEP-4, STEP-5, STEP-6, STEP-7) — Opus 5 headless — 2026-09-17

## §0 Headline
- Chunk B is **built in the working tree and not committed**: the new `com.cobalt.replay` job (`src/cobalt/replay/` + jobs.yaml row + plist), F12 card replay with cf-R and versioned receipts, F13 movers + benchmark + the shared L53 total-demand gate at every pre-request site, the `radar.benchmark` optional-settings loader, and the DRC miss line.
- Required suite `uv run pytest -q tests/cobalt tests/taxonomy`: **1310 passed, 262 skipped**. Chunk B files alone: 101 passed, 5 skipped. Every skip is `requires_db` or `requires_vault`, and none errors.
- 15 DevDoc pages: 7 new (`cobalt/replay/*`) and 8 updated. Hub-cut fixtures are untouched. No new dependency.
- **ESCALATE: 3** (§5). E1 blocks deploy: with the ceiling unchanged, the L53 gate refuses the archiver and replay, as plan §8 item 4 predicted.

## §1 Files changed

| File | Change |
|---|---|
| `src/cobalt/replay/__init__.py` | new: package map |
| `src/cobalt/replay/models.py` | new: every Pydantic value (`CardCandidate`, `MissRow`, `MoversExport`, `StoredMover`, `Episode`, `ReplayResult` …), errors, canonical hashing, `FORMULA_VERSION`, the exact formation line |
| `src/cobalt/replay/cards.py` | new: pure `replay_card` (coverage, trigger, W/H horizon, `bar_start + 1 min <= H`, gap-through fill, same-bar stop wins, gates rule_10 → window → state with `(at, id)`, as-of-trigger stop), `replay_from_receipt`, `resolve_window` (public resolver), `session_close_for`, `MissedStore` (USER: candidates, positions, current, retire → insert → link `reconcile`) |
| `src/cobalt/replay/movers.py` | new: `MoversCollector` (unfiltered exports, i1 fetches, bucket + L53 gate), `parse_movers` (sort-order check), `retained_exports` (history never refetched), pure `benchmark_misses`, `archive_movers` (coverage re-check, deadline fit), `MoversStore` (SYSTEM, deactivate-never-delete) |
| `src/cobalt/replay/line.py` | new: `render_line` (n always, avg only at n ≥ 30, input_stale surfaced), zero-width `after_drc_rules` placement, `drc_note_path`, `write_miss_line` (existing note only, `DrcNoteAbsent`) |
| `src/cobalt/replay/runner.py` | new: `archiver_precondition` (tonight's occurrence), `replay_deadline`, `formation_replay` adapter, `ReplayDeps`, `run_nightly` (per-side phases, `StepFailed`, archive failures fail at end) |
| `src/cobalt/replay/cli.py` | new: `cobalt replay nightly [--date] [--dry-run]` in `as_job(skip=dry_run)`, `default_deps` (no `ensure_schema` on a dry run) |
| `src/cobalt/radar/notes.py` | `DemandWindow`/`DemandConsumer`/`TotalDemand`, **`check_total_demand`**, `scheduled_consumers`, `radar_window`, `replay_window`, `check_scheduled_demand`; `load_sources` gains `radar_window=`/`other_consumers=` and calls the gate; `configured_sources` passes the registry's consumers |
| `src/cobalt/radar/propose.py` | proposal budget check routed through `check_total_demand` |
| `src/cobalt/archiver/runner.py` | `_check_demand` before the first request (nightly = `archiver` consumer; backfill = unbounded consumer) |
| `src/cobalt/archiver/store.py` | `bars_between` read |
| `src/cobalt/settings/models.py` | `BENCHMARK_KEY`, `BenchmarkSettings`, `OPTIONAL_SETTING_KEYS/MODELS` — not in `SETTING_KEYS` |
| `src/cobalt/settings/cli.py` | `load --optional <file> --sha256 <hash>`: hash before parse, per-key diff, `assert_writable`, round trip |
| `src/cobalt/jobs/restarts.py` | a new one-shot plist derives `bootstrap once: <label>`, no restart (R1-22) |
| `src/cobalt/cli.py` | mounts `cobalt replay` |
| `configs/cobalt/jobs.yaml` | `com.cobalt.replay`: one-shot, `supervisor: self`, `timeout_s: 1800`, `{at: "21:05", weekdays: [1..5]}` |
| `configs/cobalt/taxonomy/tunables.yaml` | `replay.backup_margin_s: 300` (duration, `proposed`, source ruling = plan R1-16's 21:35) |
| `ops/com.cobalt.replay.plist` | new: `COBALT_ENV=production`, `COBALT_VAULT_PATH`, Mon–Fri 21:05, `uv run cobalt replay nightly` |
| `tests/cobalt/test_replay_{cards,demand,line,movers,runner}.py`, `test_settings_optional.py` | new |
| `tests/cobalt/test_jobs_restarts.py` | + 1 test |
| `docs/40 - DevDocs/cobalt/replay/{__init__,models,cards,movers,line,runner,cli}.md` | new pages |
| `docs/40 - DevDocs/cobalt/{settings/models,settings/cli,radar/notes,radar/propose,archiver/runner,archiver/store,jobs/restarts,cli}.md` | dated `2026-09-17 — S2-P4` sections |

## §2 Tests added (names)

**§4 sentences owned by STEP-4..7**

| §4 area | Test | File | offline / db / vault |
|---|---|---|---|
| F12 | `test_nightly_report_lists_misses_with_the_gate_or_variable_that_excluded_them` | runner | offline |
| F12 | `test_trigger_on_unarmed_card_is_missed_row_unarmed` | cards | offline (real card 302) |
| F12 | `test_gate_order_rule_10_then_window_then_state` | cards | offline (real card 308 + vectors) |
| F12 | `test_trade_count_band_unset_recorded_in_gate_detail_never_excluded_by` | cards | offline |
| F12 | `test_uncrossed_card_writes_no_row` | cards | offline (real card 309) |
| F12 | `test_cf_r_stop_touched_first_is_minus_one` | cards | offline (real card 304) |
| F12 | `test_cf_r_same_bar_stop_and_trigger_stop_wins` | cards | offline |
| F12 | `test_cf_r_gap_through_fills_at_bar_open` | cards | offline (R1-9 vector −3R + real card 303) |
| F12 | `test_cf_r_horizon_end_close_window_or_1600` | cards | offline |
| F12 | `test_mfe_r_stored_as_observation` | cards | offline |
| F12 | `test_every_missed_number_replays_from_stored_inputs` | cards | offline (5 real misses) |
| F12 | `test_stale_bars_write_no_row_and_count_input_stale` | cards | offline |
| F12 | `test_formation_replay_unavailable_logs_exact_line_no_rows` | runner | offline |
| F12 | `test_rerun_is_idempotent` | cards | offline |
| F13 | `test_tesla_class_mover_absent_from_pool_appears_in_miss_line_with_excluded_by` | movers | offline (real CTNT) |
| F13 | `test_admitted_mover_is_not_a_miss` | movers | offline (real AEHL) |
| F13 | `test_never_admitted_episode_supplies_its_excluded_by` | movers | offline (real DAIC, config_cap) |
| F13 | `test_movers_archived_regardless_of_watchlist` | movers | offline |
| F13 | `test_benchmark_settings_absent_or_malformed_fails_loud` | movers | offline |
| F13 | `test_benchmark_key_not_in_required_setting_keys` | movers | offline |
| F13 / L53 | `test_total_finviz_demand_refuses_when_sum_exceeds_ceiling_while_replay_alone_passes` | demand | offline; drives the replay exports + bars sites and the archiver runner site |
| Miss line | `test_miss_line_upserts_drc_misses_unit_idempotent` | line | offline |
| Miss line | `test_human_edit_to_miss_line_wins_and_logs_override` | line | offline |
| Miss line | `test_drc_note_absent_fails_loud_and_creates_nothing` | line | offline |
| Miss line | `test_miss_line_sum_carries_n_and_average_insufficient_below_30` | line | offline |
| Miss line | `test_dry_run_writes_nothing_and_prints_diff` | line | offline |
| Miss line | `test_live_drc_shape_accepts_the_unit_placement` | line | **requires_vault** (hub; read-only; `COBALT_TEST_LIVE_DRC=<note path>`) |
| Job | `test_replay_refuses_when_archiver_not_done_today` | runner | offline |
| Job | `test_step_failure_names_step_and_earlier_steps_stand` | runner | offline |
| Job | `cobalt validate` green with the new row + plist | — | **not run** (§4.2); `test_registry_and_ops_carry_the_replay_job_with_matching_schedule` covers the registry ↔ plist mirror |

**Amendment coverage**

| Amendment | Tests |
|---|---|
| R1-9 planned_entry vs fill_price | `test_cf_r_gap_through_fills_at_bar_open`, `test_mfe_r_stored_as_observation` |
| R1-10 / R2-4 / R3-2 horizon | `test_r1_10_explicit_time_window_on_an_early_close_day_never_runs_past_the_close`, `test_r1_10_a_stop_only_in_the_bar_starting_at_h_is_excluded`, `test_r1_10_trigger_at_exactly_h_writes_no_row_input_stale`, `test_r1_10_after_window_trigger_gets_the_session_close_horizon`, `test_r1_10_ambiguous_prose_takes_the_resolver_fallback` |
| R1-11 states, ties, stop edits, close boundary | `test_r1_11_state_mapping_is_exhaustive_over_card_states`, `test_r1_11_terminal_states_map_with_their_reason[MISSED/EXPIRED/PASSED]`, `test_r1_11_simultaneous_transitions_order_by_id_and_refuse_without_one`, `test_r1_11_historically_edited_stop_is_read_as_of_the_trigger`, `test_r1_11_position_closed_at_the_trigger_instant_is_not_open` |
| R1-12 coverage | `test_r1_12_partial_day_wrong_day_and_no_bars_are_input_stale_and_a_full_quiet_day_is_no_trigger`, `test_coverage_records_gaps_without_gating_on_them`, `test_archive_counts_failures_and_incomplete_coverage_and_never_marks_them_archived`, `test_archive_skips_tickers_already_covered_and_dry_run_fetches_nothing` |
| R1-8 / R2-1 / R3-1 versioned receipts | `test_reconcile_insert_supersede_retire_and_identical_rerun_against_the_live_index` (db), `test_reconcile_failure_between_retire_and_insert_rolls_the_whole_run_back` (db) |
| R1-13 / R2-5 L53 | `test_radar_load_sources_counts_the_other_consumers_in_its_window`, `test_disjoint_windows_contribute_zero_and_unbounded_windows_always_count`, `test_unmeasured_ceiling_refuses`, `test_scheduled_consumers_read_the_registry_and_never_omit_the_archiver` |
| R1-14 settings seam | `test_settings_optional.py`: `test_optional_key_round_trip_applies_and_rereads`, `test_dry_run_prints_the_diff_and_writes_nothing`, `test_hash_mismatch_and_a_missing_hash_on_apply_refuse`, `test_absent_or_malformed_benchmark_refuses[×5]`, `test_apply_inside_the_market_reset_pause_refuses`, `test_the_benchmark_never_joins_the_required_keys` |
| R1-15 precondition | `test_r1_15_precondition_refuses[previous-day done / same-day early manual run / running / failed / done with a nonzero exit / incoherent times / absent row]`, `test_r1_15_tonights_occurrence_passes_across_the_utc_date_line` |
| R1-16 deadline | `test_r1_16_deadline_is_the_backup_less_the_margin_and_the_margin_itself_refuses`, `test_r1_16_a_slow_but_heartbeating_collector_is_cut_at_the_deadline_with_no_vault_write`, `test_r1_16_a_deadline_passing_between_steps_stops_before_the_vault_write`, `test_archive_refuses_work_that_cannot_fit_before_the_deadline` |
| R1-17 dry run | `test_dry_run_through_the_cli_writes_nothing_and_prints_rows_and_the_line_diff` (as_job skip, no reconcile/mark/upsert/cache/ensure_schema, DRC bytes unchanged), `test_dry_run_export_is_not_cached` |
| R1-18 placement + L28 cases | `test_r1_18_first_unit_lands_zero_width_right_after_the_drc_rules_close_marker`, `test_r1_18_missing_anchor_appends_at_the_end_and_touches_nothing_above`, `test_r1_18_malformed_marker_refuses_and_changes_no_byte`, `test_human_edit_to_miss_line_wins_and_logs_override`, `test_r1_18_sync_revert_takes_cobalt_text_without_an_override`, `test_r1_18_mtime_conflict_aborts_and_never_clobbers_the_concurrent_edit` |
| R1-20 reruns / sides / history | `test_r1_20_changed_top_n_rerun_deactivates_never_deletes_and_identical_rerun_is_a_noop` (db), `test_r1_20_a_ticker_on_both_sides_resolves_to_one_missed_row`, `test_r1_20_multiple_never_admitted_episodes_pick_the_most_recent`, `test_r1_20_an_unavailable_historical_date_refuses`, `test_r1_20_a_retained_historical_export_is_read_not_refetched`, `test_r2_3_a_retry_after_a_commit_boundary_resumes_idempotently` |
| R1-21 formations | `test_formation_replay_unavailable_logs_exact_line_no_rows`, `test_r1_21_a_present_but_incompatible_p2_fails_loud` (positive half **not built**, E2) |
| R1-22 restarts | `test_a_new_one_shot_plist_derives_an_explicit_bootstrap_and_no_restart` |
| R2-3 side phases | `test_r2_3_each_phase_runs_on_its_own_side_and_the_wrong_side_is_refused` (db), `test_r2_3_a_retry_after_a_commit_boundary_resumes_idempotently` |
| Other | `test_parse_real_movers_exports_rank_in_export_order_and_hash_the_raw_bytes`, `test_parse_reads_asset_type_from_a_full_column_export`, `test_parse_refuses_the_wrong_sort_and_a_missing_column`, `test_change_pct_parsing_is_strict`, `test_request_count_and_sides`, `test_not_equity_movers_leave_the_benchmark_and_unreported_asset_type_stays_in`, `test_line_lists_three_movers_then_counts_the_rest_and_surfaces_input_stale`, `test_archive_failures_are_counted_and_fail_the_job_at_the_end`, `test_benchmark_absent_fails_the_movers_step_loud`, `test_drc_note_absent_fails_the_line_step_and_creates_nothing` |

## §3 Suite result (verbatim)

`uv run pytest -q tests/cobalt tests/taxonomy`:
```
1310 passed, 262 skipped, 15 warnings in 26.34s
```
The 15 warnings are the existing litellm DeprecationWarning (as in chunk A).

Chunk B files, `-rs`: `101 passed, 5 skipped`. Skips: `requires_db: Postgres env settings not available` (×4) and `requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (×1).

## §4 What I could not do, and why

1. **No `requires_db` or `requires_vault` test ran.** There are 5 in chunk B. I have no DB, no credentials and no vault access (L41 interim). The hub runs them on cobalt_dev with 0008/0009 applied. The vault test reads a live DRC note and never writes it.
2. **`cobalt validate` and `cobalt jobs restarts main..HEAD` were not run.** This headless session's permission layer asked for approval I could not grant. The hub runs both and attaches the RESTARTS table. Expected result:
   - `com.cobalt.replay` bootstraps once.
   - `radar/notes.py` and `radar/propose.py` → `com.cobalt.radar`.
   - `archiver/*` and `settings/*` → by static import reach.
   - `tunables.yaml` → its resident readers.
3. **Failing test first was recorded only in part.** I ran red before implementing for:
   - the demand gate (ImportError),
   - movers and line (ModuleNotFoundError),
   - the runner (collection error),
   - restarts (assertion on `'plist in diff'`).

   I did not record red for STEP-5 (`cards.py`, whose code preceded its tests in this session) or for the settings-loader tests.
4. **R1-21's positive half is not built** (E2). That covers two formations under the extended key, existing-card suppression, and cf-R through P2's evaluator.
5. **Out of scope for chunk B:** STEP-8 (ADR-0010, BACKLOG row) and STEP-9 (`cobalt smoke s2`).
6. **Recorded facts and interpretations:**
   - **Historical `--date` precondition.** `cobalt_jobs` keeps one row per label, so a past date needs a clean archiver run started at or after that night's 20:30 occurrence. Per-ticker bar coverage is still checked.
   - **Dry run and Finviz.** A dry run for *today* still makes the 2 live export requests (no cache write, no bar fetch). A `--date` dry run makes none.
   - **Real-shape fixture outcomes.**
     - Card 309 (hub note: "crossed") never traded through **after** it was created, so it is `no_trigger`.
     - Cards 303 and 305 have 0.055 and 0.06 planned risk and gapped fills, so the one formula gives −39.9091R and −23.3333R. That is correct per R4/R1-9; flagged for Dejan's first read of the line.
   - **Asset Type.**
     - The movers fixtures were cut without `c=`, so they have no Asset Type column.
     - The real `c=0-150` export (`pool-metrics.real-shape.csv`) leaves Asset Type blank for all 20 stocks.
     - Blank or absent is recorded `unreported` and the mover stays in the benchmark.
     - Radar's own `not_equity` check depends on that column too. That check is outside P4, but the fact is noted.
   - **Test name vs L31.** `test_tesla_class_…` is kept verbatim from plan §4. It uses a company name as a class label, not a person or vendor; the reviewer may rename it under L31.
   - **P2 merge conflicts to expect:**
     - `settings/cli.py`: P2's `--card` path and this `--optional` path should become one loader.
     - `radar/notes.py`: P2's daily-bars consumer must join `scheduled_consumers`.
7. The scratch file `scratch/p4b-devdoc-append.py` (gitignored) appended the DevDoc sections. It is safe to delete.

## §5 ESCALATE (3)

1. **E1 — the L53 gate refuses the archiver and replay under the unchanged ceiling (deployment gate, plan §8 item 4).**
   - The archiver's defined rpm is its pacing bound, 60 / 1.2 s = **50 rpm**, over its watchdog window 20:30–22:00. Alone that is above `radar.finviz_max_rpm` = 40, so `check_scheduled_demand("archiver")` refuses the nightly run.
   - Replay's window (21:05–21:35) overlaps it, so replay refuses too.
   - Radar (04:00–20:00) is disjoint and unaffected.
   - Merging this as built turns the nightly archiver RED.
   - **RULING needed (Dejan):** the ceiling number, or the archiver's pacing or window. The build does not change either.
2. **E2 — P2's shipped formation contract cannot be bound (R1-21).** Recorded read-only from `/Users/cobalt/cobalt-wt/s2-p2-cards` (not merged):
   - Callable: `cobalt.radar.evaluate_cli.replay_formations(day, *, pool_key, slug_filter, radar_store, defs_source, daily_source, tunables, defaults, clock, out) -> ReplayReport`.
   - `ReplayFormation` fields: `seen_at, ticker, slug, direction, trigger, stop, formed_bar_ts`.
   - Capability marker: `cobalt.radar.evaluate.EVALUATOR_VERSION = "s2p2.1"`.

   There is no `membership_id`, no trade_def md5 and no receipt reference, so a `kind='formation'` row cannot satisfy 0009's CHECK. The adapter:
   - logs the exact unavailable line while P2 is absent;
   - **fails loud when P2 is present** (incompatible, or compatible but unbound).

   So after P2 merges, the replay job fails at step `formations` until P2's `ReplayFormation` gains those fields and the binding is built. The owner is P2's amendment or a P4 follow-up, by ruling.
3. **E3 — the dev end-to-end on the fixture day will read every card as stale.** The hub-cut fixtures keep EDT UTC offsets on a shifted February date. `cobalt replay nightly --date 2026-02-10` on cobalt_dev asks the real calendar for the February close (21:00 UTC), but the bars end at 20:10 UTC. Every card will be `input_stale`. The committed tests pass the anchor's real close explicitly. The hub should run the dev e2e on a dev day whose stored bars carry that day's real offsets. The run also needs retained `movers-<side>-*.csv` under `data/radar-cache/<date>/` and a done archiver row.

RESTARTS (expected; the hub derives it with `cobalt jobs restarts main..HEAD`): `com.cobalt.radar` (radar/notes.py, radar/propose.py; plus chunk A), `com.cobalt.aset` (chunk A), and any resident that reads `tunables.yaml`. `ops/com.cobalt.replay.plist` → bootstrap once, no restart.
