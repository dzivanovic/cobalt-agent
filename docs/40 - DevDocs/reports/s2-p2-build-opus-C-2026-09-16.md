# REPORT — S2-P2 build, chunk C (STEP-8..12) — 2026-09-16

Seat: Opus 5, builder, headless (L29 floor, L50) · Branch `sprint-2/cards` · Worktree `~/cobalt-wt/s2-p2-cards` · Plan `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md` · No DB, no credentials (L41 interim) · Not committed (hub commits, L46).

## §0 Headline

- **Built:** STEP-8 (`/radar` ladder on `"user".radar_cards_v`: badges, hollow shadow dots, 1–10 tap strip, key row with snap notice, live promote/release, health pills; POST allowlist + GET sentinel tests; `cards trail-fit-draft`), STEP-9 (taxonomy v0.8 doc, schema 0.5 behind the 0.4 loader gate, `taxonomy catalyst-review` / `catalyst-apply`, Astra R2-4 existing-card catalyst dot), STEP-10 (`cards shadow-report`), STEP-11 (`radar audit-export --run | --replay`), STEP-12 (DevDocs, BACKLOG row, ADR-0009).
- **Suite:** `1527 passed, 282 skipped` (chunk B was 1465/278).
- **Changed chunk A/B code the plan's own text required:** migration 0007 (view columns, board join, shadow view shape) and `radar/evaluate.py` (R2-4: a def edited under an open card orphaned it). Re-run `cobalt db migrate` on cobalt_dev before the DB tests.
- **Not run here:** 3 new `requires_db` tests, 1 new `requires_vault` test (hub).
- **ESCALATE: 3** (bottom).

## Files changed (worktree vs HEAD `1a40c16`)

| Step | File | Change |
|---|---|---|
| 8 | `src/cobalt/aset/radar_panel.py` | P3 contract adapter and `order_cards` removed. `RadarCardRow` (exact view columns + dots; import refuses if columns ≠ `FIELD_OWNERS`), `DotView`/`KeyView`/`HealthView`/`CardView` rebuilt, `build_ladder_view` (one read, read-only rung, colour tunables, `ladder_order`), renderers for badges, dots, tap strip, key row, snap notice, promote/release, `PANEL_JS` delegated `fetch` POSTs + ladder re-fetch |
| 8 | `src/cobalt/cards/store.py` | `radar_board_cards(trade_date)`, `shadow_agreement(since)`, `receipt_for_run(run_id)` (read-only) |
| 8 | `src/cobalt/cards/radar.py` | `FIELD_OWNERS` + `last_price`, `pool_position` |
| 8 | `src/cobalt/cards/trail_fit_draft.py` | new: R5 draft, no apply path |
| 8/10 | `src/cobalt/cards/cli.py` | `trail-fit-draft`, `shadow-report` |
| 8/9/10 | `src/cobalt/db_migrations/0007_radar_cards.sql` | `radar_cards_v` + `last_price`, `pool_position`, board join on `radar_score_id`; `shadow_agreement_v` regrouped per factor × ET trading day with `deltas[]` (DROP IF EXISTS + CREATE OR REPLACE) |
| 9 | `src/cobalt/taxonomy/trade_def.py` | `SCHEMA_VERSION="0.5"`, `LOADER_SCHEMA_GATE="0.4"`, `standard_quality_factors`, scoped `schema_gate` |
| 9 | `src/cobalt/taxonomy/factor_lines.py` | new: line-level quality_factors reader/editor |
| 9 | `src/cobalt/taxonomy/catalyst.py` | new: review draft/render/parse, preflight, batch apply, resume, re-read gate |
| 9 | `src/cobalt/taxonomy/cli.py` | `catalyst-review`, `catalyst-apply` |
| 9 (R2-4) | `src/cobalt/radar/evaluate.py`, `src/cobalt/cards/scoring.py` | refresh by slug when the md5 changed; `factor_added` history; receipt `definition_md5`; replay uses it |
| 10 | `src/cobalt/cards/shadow_report.py` | new |
| 11 | `src/cobalt/radar/audit_export.py` | new; `radar/cli.py` `audit-export`; `radar/store.py` `score_run`, `scores_for_run` |
| 12 | `docs/30 - Design/TAXONOMY-DRAFT-v0_8.md`, `docs/10 - Decisions/ADR-0009-radar-cards-seam-and-precondition-ast.md`, `docs/00 - Project/BACKLOG.md` (NOW row) | new / updated |
| 12 | DevDocs new: `taxonomy/{catalyst,factor_lines,cli}.md`, `cards/{trail_fit_draft,shadow_report}.md`, `radar/audit_export.md` · rewritten: `aset/radar_panel.md` · updated: `aset/web.md`, `cards/{cli,radar,scoring,store}.md`, `radar/{cli,evaluate,store}.md`, `taxonomy/trade_def.md` | agent-authored |
| tests | `tests/cobalt/test_radar_panel.py` (contract-adapter tests moved out), `tests/taxonomy/test_trade_defs.py` (message match), `tests/cobalt/test_radar_cards_db.py` (+3) | amended |

`web.py` needed no change: its GET routes already call `build_radar_panel`, and the four POST routes came in chunk B. No fixture under `tests/fixtures/radar/` was edited or added. No new dependency. No vault or `~/cobalt` access.

## Tests added

| File | Tests |
|---|---|
| `test_radar_panel_cards.py` | `test_ladder_reads_radar_cards_v_rows_and_the_contract_adapter_is_gone` · `test_empty_ladder_is_explicit_and_needs_no_rung` · `test_ladder_inputs_fail_loud` (5) · `test_every_displayed_card_field_carries_its_owner_badge` · `test_computed_dots_render_hollow_shadow_with_engine_grade_and_why` · `test_a_tapped_dot_renders_filled_with_the_trader_grade` · `test_one_to_ten_tap_strip_on_every_dot_of_a_live_card_and_none_on_terminal` · `test_key_row_has_every_key_with_dollars_greyed_disabled_and_still_tappable` · `test_snap_notice_renders_amber_and_the_key_freezes_once_armed` · `test_proposed_key_without_conviction_says_tap_to_propose` · `test_promote_is_live_on_watch_cards_and_release_on_the_promoted_one` · `test_health_pills_render_from_the_stored_card_health` · **`test_ladder_renders_every_real_shape_card_state`** · `test_first_two_open_detail_order_and_terminal_below_active` · `test_outside_pool_label_and_pool_position` · `test_card_panel_escapes_why_and_notices` · `test_panel_javascript_posts_through_fetch_only_to_the_allowlisted_routes` · `test_rendered_page_with_cards_keeps_the_focus_law` · **`test_post_routes_are_exactly_the_explicit_allowlist`** · **`test_api_radar_pool_get_never_touches_sheet_write_schema_or_attestation_helpers`** (the carried sentinel) · `test_radar_get_with_cards_never_touches_sheet_write_schema_or_attestation_helpers` |
| `test_trail_fit_draft.py` | **`test_trail_fit_draft_never_applied`** · `test_a_note_already_human_says_so_and_no_trail_fit_anywhere_is_loud` |
| `test_catalyst.py` | `test_schema_is_0_5_and_the_loader_gate_stays_0_4` · **`test_at_0_5_a_def_without_catalyst_fails_loud`** · `test_the_override_is_scoped_and_an_unknown_schema_is_refused` · **`test_review_file_lists_every_defined_note_with_its_existing_catalyst_factors`** · `test_review_round_trips_and_parses_the_three_marks` · `test_a_bad_mark_is_refused` (3) · `test_the_review_command_refuses_to_overwrite_an_existing_file` · **`test_batch_apply_refuses_on_sha_mismatch_and_writes_nothing`** · `test_apply_adds_catalyst_everywhere_drops_only_marked_and_rereads_valid_at_0_5` · **`test_apply_never_removes_an_unmarked_catalyst_factor`** · `test_every_other_byte_of_the_note_is_untouched` · `test_a_unit_that_drifted_since_the_review_refuses_the_whole_batch_before_any_write` · `test_an_interrupted_batch_resumes_and_keeps_what_was_applied` · `test_a_human_edit_mid_batch_stops_the_batch_loudly` · `test_a_note_defined_after_the_review_refuses_the_batch` · `test_dry_run_writes_nothing_and_says_the_gate_is_unproven` · `test_factor_block_reads_both_indent_styles_and_mapping_items` · `test_flow_style_quality_factors_is_refused` · requires_vault (hub): `test_live_review_lists_every_defined_note_and_its_catalyst_factors_and_writes_nothing` |
| `test_radar_catalyst_dot.py` (R2-4) | `test_a_card_formed_before_the_def_gained_catalyst_gets_one_hollow_desk_na_dot` · `test_the_receipt_names_the_definition_used_and_replays_after_the_def_changed` · `test_a_card_formed_after_the_def_gained_catalyst_carries_it_from_birth` · `test_a_def_gone_from_the_loaded_set_is_still_a_loud_refusal` |
| `test_shadow_report.py` | `test_the_view_groups_by_factor_and_et_trading_day_and_keeps_every_delta` · `test_report_counts_sessions_pairs_median_and_within_two_per_factor` · `test_the_median_is_over_all_pairs_not_a_median_of_daily_medians` · `test_since_filters_by_trading_day` · `test_rendered_report_prints_gate_status_text_per_factor` · `test_no_pairs_is_said_plainly_not_rendered_as_an_empty_table` · `test_a_row_that_disagrees_with_its_own_deltas_is_refused` · `test_the_bar_is_required_never_defaulted` · `test_the_report_never_flips_anything` |
| `test_radar_audit_export.py` | `test_run_bundle_has_every_file_and_a_manifest_of_their_hashes` · `test_run_bundle_carries_bars_window_settings_tunables_ast_and_published_cards` · `test_the_card_numbers_recompute_from_the_bundle_files_alone` · `test_the_bundle_is_frozen_an_existing_nonempty_out_dir_is_refused` · `test_a_stored_hash_that_does_not_match_its_inputs_refuses` · `test_cobalts_own_replay_disagreeing_with_what_it_published_refuses` · `test_a_run_without_its_receipt_or_row_refuses` · `test_a_dark_run_exports_with_an_explicit_empty_card_list` · `test_replay_bundle_writes_nothing_to_stores_and_bundles_candidate_formations` · `test_cli_takes_exactly_one_of_run_or_replay_and_a_required_out` |
| `test_radar_cards_db.py` (requires_db, hub) | `test_shadow_agreement_v_pairs_taps_with_the_engine_grade_per_factor_and_et_day` · `test_audit_export_of_a_cobalt_dev_run_verifies_and_writes_the_bundle` · `test_the_ladder_reads_radar_cards_v_with_its_dots_on_cobalt_dev` |

Bold = a §4 sentence this chunk owns.

**Test-first:**
- Red before the code for: the panel file (fixture error: the view lacked `last_price`/`pool_position`), catalyst, trail-fit draft, shadow report and audit export (collection errors), and R2-4 (the stage refused to refresh: "md5 … no longer loaded").
- One exception: the `trade_def` schema gate was edited before `test_catalyst.py` existed, so its three gate tests passed on first run.

**Replaced:** P3's contract-adapter tests (`from_contract`, `order_cards`, the disabled `S2-P2` controls) were removed from `test_radar_panel.py`. They are re-specified in `test_radar_panel_cards.py` against rows the S5 stage produces from `bars-rubberband.real-shape.json` + `card-settings.real-shape.json`. No card fixture was invented.

## Suite result (verbatim)

```
$ uv run pytest -q tests/cobalt tests/taxonomy
1527 passed, 282 skipped, 15 warnings in 36.43s
```

The 15 warnings are the existing litellm `asyncio.iscoroutinefunction` deprecation.

## Could not do, and why

| Item | Why | Where it lands |
|---|---|---|
| Run the 3 new `requires_db` tests, plus chunk B's 9 | No DB for workers (L41 interim) | Hub, after `cobalt db migrate` on cobalt_dev. 0007 changed: the view gains 2 columns and a new join, and `shadow_agreement_v` is dropped and recreated |
| Run `test_live_review_lists_every_defined_note_…` | Vault test is hub-run | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q tests/taxonomy/test_catalyst.py -k live`. It drafts in memory, preflights at 0.5, writes nothing and asserts note mtimes unchanged |
| `panel-cards.real-shape.json` | Hub-cut fixture (plan §3); prod has no radar cards. The panel no longer reads `panel-cards.contract.json`; only P3's redaction test still loads it | Hub: cut from the dev replay, then retire the contract file |
| `cobalt validate`, CLI `--help` smoke, `cobalt jobs restarts main..HEAD` | Need `COBALT_ENV` inline, which the headless permission set refused. CLI registration is proven by parser tests instead | Hub. Expected RESTARTS: `com.cobalt.radar` (evaluate, store, cli) and `com.cobalt.aset` (radar_panel, cards store/scoring/radar, taxonomy trade_def) |
| Verify the new docs are not gitignored | `git check-ignore` was refused. `git status` lists them all as untracked (`??`), not ignored | Hub at commit |
| `docs/40 - DevDocs/INDEX.md` | Stale since before chunk A (no evaluate/predicate/scoring rows); outside this chunk's file list | Next sprint close |
| Real concurrent taps on the panel | Offline only | Live-morning acceptance (§6) |

## Decisions taken inside the plan's text (for review)

1. **The rung on `/radar` is read-only.** `DayModeStore.for_date` + `decided_or_stage1`, never `_daymode_state`, which can attest a note (P3 R1-3). It is read only when a card exists, so an empty ladder never fails on day-mode state.
2. **Disabled keys are greyed but tappable.** R8's snap-down needs the tap to reach the server; refusal happens server-side.
3. **Terminal cards on the ladder are today's only** (ET `state_at`).
4. **Shadow "sessions" are ET trading days.** The chunk A view grouped by the `premarket/rth` session value, which cannot count 10 sessions or filter `--since`. It now groups per factor × ET date and keeps `deltas[]`, so the median is over all pairs.
5. **Review marks:** `keep` | `drop` | `drop: a, b`. One row per defined note; drafts are excluded.
6. **Audit `--run` refuses** when re-derived hashes or Cobalt's own replay disagree, before any file is written. `--replay` bundles candidate rows only (`published: false`).

## ESCALATE (3)

1. **R2-4 exposed a chunk B gap, now fixed and flagged for review.** Adding `- catalyst` changes a def's md5, and the stage keyed open cards by md5. Every open card would have stopped refreshing at D3 ("no longer loaded") and never gained the dot. Fixed by falling back to the slug (the def's identity, ADR-0008 D3a); receipts now carry `definition_md5`; the view joins the board on `radar_score_id`. This changes `formula_sha256` (evaluate.py is a formula file). Needs the hub's DB proof and an Astra glance.
2. **`trail_fit` still suppresses every untapped card's score through S2.** The R5 draft exists, but nothing changes until Dejan edits his notes. With `curve_unset` also suppressing until D2 (chunk B ESCALATE 4), the F3 ranking stays tap-driven.
3. **The audit bundle and the catalyst review file hold user data** (definitions, settings, note paths, factor names). The review file's plan-default location is `docs/40 - DevDocs/reports/`, which is committed. Needs a ruling: commit the marked review file as the R10 record, or keep it gitignored (like the bundle's scratch path).
