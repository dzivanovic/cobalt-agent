# S2-P4 build — chunk E2 (R1-21 positive half + Grok BLOCKER 2) — Opus 5 headless — 2026-09-18

## §0 Headline
- **BUILT**, in the worktree, not committed. R1-21's positive half is bound to S2-P2's SHIPPED contract: `ReplayFormation` gained `membership_id`, `trade_def_md5` and `score_inputs_sha256` (all values `evaluate_member` already returned — no schema change, no write, no new seam), and `src/cobalt/replay/formations.py` turns P2's formations into `kind='formation'` miss rows through the ONE cf-R formula.
- Grok BLOCKER 2 is resolved by binding to the shipped names, not by a shim: the callable is `cobalt.radar.evaluate_cli.replay_formations`, the capability marker is `cobalt.radar.evaluate.EVALUATOR_VERSION`. Both imported statically (L42). The plan's single `cobalt.radar.evaluate` is wrong against the tree — ESCALATE 1.
- The 6 red tests are green; `test_r1_21_a_present_but_incompatible_p2_fails_loud` still passes (and now actually injects its incompatible module — ESCALATE 2).
- `uv run pytest -q tests/cobalt tests/taxonomy`: **1704 passed, 306 skipped, 2 xfailed** (was 6 failed / 1673 passed).
- **ESCALATE: 4.** No STOP: every field 0009's `missed` CHECK needs is obtainable from what P2's read-only replay already holds.

## §1 S2-P2's SHIPPED contract — recorded from the tree BEFORE any code

Read at `src/cobalt/radar/evaluate_cli.py` and `src/cobalt/radar/evaluate.py` on this branch (rebased on P2 `976528f`). Verified by running it, not by reading alone.

| Fact | Shipped value | Source |
|---|---|---|
| module (replay entrypoint) | `cobalt.radar.evaluate_cli` | `evaluate_cli.py:1-36` (module docstring), `:125` |
| callable | `replay_formations(day, *, pool_key, slug_filter, radar_store, defs_source, daily_source, tunables, defaults, clock, out=print)` | `evaluate_cli.py:125-137` |
| writes | **none** — reads membership + `system.bars` + the radar cache and re-evaluates through the same `evaluate_member` the resident runs | docstring `:10-18`; `test_replay_cli_writes_nothing_and_lists_formations` |
| returns | `ReplayReport(day, scans, formations, path_b_only, not_evaluable, counts)` | `evaluate_cli.py:75-83` |
| per-formation type (BEFORE E2) | `ReplayFormation(seen_at, ticker, slug, direction, trigger, stop, formed_bar_ts)` — frozen, `extra="forbid"` | `evaluate_cli.py:63-72` |
| capability marker | `cobalt.radar.evaluate.EVALUATOR_VERSION = "s2p2.1"` | `evaluate.py:132` |
| second marker (not used, recorded) | `DESK_FORMULA_VERSION = "s2p2.1"`, `formula_sha256()` over `FORMULA_FILES` | `evaluate.py:133`, `:161` |
| dedup identity inside the replay | `(ticker, slug, formation.formed_bar_ts)` | `evaluate_cli.py:184` |
| member id already in scope | `member["id"]` → `MemberInput.membership_id` → `MemberEvaluation.membership_id` | `evaluate_cli.py:176`; `evaluate.py:316, 344` |
| trade_def md5 already in scope | `LoadedDef.md5` → `MemberEvaluation.md5` | `evaluate.py:305, 345` |
| evaluation input digest already in scope | `MemberEvaluation.inputs_sha256` | `evaluate.py:356, 515` |
| the RETAINED score receipt | `system.radar_score` — `UNIQUE (run_id, membership_id, trade_def_md5)`, `inputs_sha256 TEXT NOT NULL`, index on `(membership_id, trade_def_md5)`; written by `RadarStore.put_scores` from exactly those three fields | `0006_radar_score.sql:92-113`; `radar/store.py:398-415`; `evaluate.py:1293-1299` |
| how a card links to it | `aset_sizings.radar_score_id` ← `RadarCardSpec(radar_score_id=score_ids[(ev.membership_id, ev.md5)])` | `evaluate.py:1386-1391`; `0007_radar_cards.sql` |
| formation → card price mapping | `RadarCardSpec.entry = trigger_price`, `.stop = structural_stop`, i.e. `Formation.trigger.price` / `Formation.stop.price` | `cards/radar.py:117-121`; `evaluate.py:1390-1391` |
| one-open-card rule the suppression key mirrors | `UNIQUE (pool_member_id, trade_def_slug, direction) WHERE origin='radar' AND state IN (WATCH,ARMED,TRIGGERED,FILLED)` | `0007_radar_cards.sql:90-92` |

**Run-verified**, before code, over P2's own hub-cut fixture (`bars-rubberband.real-shape.json`, `sup.members("FTFT","BGFI")`, the shipped example def):

```
FORMATION {'seen_at': 2026-01-06 16:25+00, 'ticker': 'FTFT', 'slug': 'example-anatomy-reversal',
           'direction': 'short', 'trigger': '4.8500', 'stop': '5.37', 'formed_bar_ts': 2026-01-06 16:22+00}
FORMATION {'seen_at': 2026-01-06 18:45+00, 'ticker': 'FTFT', 'slug': 'example-anatomy-reversal',
           'direction': 'short', 'trigger': '5.6000', 'stop': '6.61', 'formed_bar_ts': 2026-01-06 18:42+00}
counts {'not_formed': 163, 'input_stale': 192, 'not_evaluable': 24, 'formed': 85}
```

Two same-day formations of ONE (ticker, trade_def) come out of P2's own fixture — R1-21's case is a real artifact, not a constructed one.

### What 0009 needs, and where each field comes from

`CHECK (kind <> 'formation' OR (trade_def_md5 IS NOT NULL AND formation_at IS NOT NULL AND pool_member_id IS NOT NULL))`, plus `missed_one_current_per_subject`'s `COALESCE(formation_at,…)` and `CASE WHEN kind='formation' THEN pool_member_id END`.

| `missed` column | Populated from | Needed a P2 change? |
|---|---|---|
| `pool_member_id` | `ReplayFormation.membership_id` ← `ev.membership_id` | yes — field added |
| `trade_def_md5` | `ReplayFormation.trade_def_md5` ← `ev.md5` | yes — field added |
| `formation_at` | `ReplayFormation.formed_bar_ts` (already shipped) | no |
| `trigger_ts` | the bar THIS replay found the trigger on — a different column, not `formation_at` | no |
| `entry` / `stop` | `Decimal(trigger)` / `Decimal(stop)`, the live card path's own mapping | no |
| score-receipt reference (in `receipt` JSONB, L57) | `ReplayFormation.score_inputs_sha256` ← `ev.inputs_sha256` + the natural key `(membership_id, trade_def_md5)` into `system.radar_score` | yes — field added |

**No STOP.** The one field that could have forced one — "the retained score-receipt reference" — is obtainable without a write or a schema change, because `MemberEvaluation.inputs_sha256` is the same digest `RadarStore.put_scores` stores in `system.radar_score.inputs_sha256` for the same `(membership_id, trade_def_md5)`. It is **content-addressed, not a row id**: P2's `--replay` path reads no receipt row, so it cannot report a score id. Every formation receipt therefore carries `{"table": "system.radar_score", "column": "inputs_sha256", "key": {membership_id, trade_def_md5}, "inputs_sha256": …, "note": "content-addressed: P2's read-only replay reads no receipt row and reports no score id"}`. A resolver looks the row up by key and matches the digest; a mismatch means the resident evaluated different inputs, which is visible rather than silent. **ESCALATE 3.**

## §2 Plan vs shipped — the name difference (Grok BLOCKER 2)

| | Plan (`plan-s2-p4-2026-09-15.md:184, :189`) | Shipped (this tree) |
|---|---|---|
| entrypoint | "if `cobalt.radar.evaluate` imports (P2 merged), call its replay" | `cobalt.radar.evaluate_cli.replay_formations` |
| capability marker | "its capability/version marker" (module unnamed) | `cobalt.radar.evaluate.EVALUATOR_VERSION` |

**The code follows the shipped layout.** These are two modules with two distinct roles, both imported statically in `replay/runner.py` — not one name accepted in two spellings (L3). The pre-E2 code's `except ModuleNotFoundError` clause listed both names but only ever *attempted* `evaluate_cli`; it now imports both, and a `ModuleNotFoundError` naming anything else is re-raised (a broken dependency inside P2 is not "P2 is not deployed" — new test).

**ESCALATE 1: the plan line is wrong against the tree** and should be corrected to name `cobalt.radar.evaluate_cli.replay_formations` (entrypoint) and `cobalt.radar.evaluate.EVALUATOR_VERSION` (marker). Not fixed here — plan text is not this chunk's to edit.

## §3 Files changed

| File | Change |
|---|---|
| `src/cobalt/radar/evaluate_cli.py` | **P2 side, additive only.** `ReplayFormation` gains `membership_id: int`, `trade_def_md5` (32-hex), `score_inputs_sha256` (64-hex) + a docstring saying what each is and why; `replay_formations` populates all three from `ev.membership_id` / `ev.md5` / `ev.inputs_sha256`, already in scope at the append. No other line touched; P2's own tests unchanged and green. |
| `src/cobalt/replay/formations.py` | **new.** `SUPPORTED_EVALUATORS`, `FORMATION_REQUIRED_FIELDS`, the P2 contract constants, `FormationSources`, `FormationContext`, `formation_candidates`, `replay_formation` (pure), `replay_formation_from_receipt`, `formation_misses`. Holds **no** `cobalt.radar` import, so replay still loads when P2 is absent. |
| `src/cobalt/replay/cards.py` | `counterfactual(...)` extracted from `replay_card` — the ONE formula, now called by both paths (L3); `stop_at` is the only thing that differs (a card walks its stop-edit history, a formation hands over P2's structural stop). `_bar_json` → `bar_json` (public: one receipt-bar spelling). New `MissedStore.radar_cards(trade_date)` USER read. `replay_card`'s behaviour is byte-for-byte the same — its 26 tests pass untouched. |
| `src/cobalt/replay/models.py` | `Counterfactual`, `CfOutcome`, `RadarCardRef`, `FormationCandidate`, `FormationReplay`, `FormationCounts`, `FormationOutcome`; `ReplayResult` gains the five formation counts. |
| `src/cobalt/replay/runner.py` | `formation_replay` now BINDS (returns `FormationOutcome`): two static imports, field check, capability-marker check, half-wiring refusal, then P2's own `replay_formations` → `formation_misses`. `formations_step` builds the context, prints each miss, reconciles `kind='formation'`, records the counts. `ReplayDeps` gains `formation_sources`. |
| `src/cobalt/replay/line.py` | the formation segment when the binding runs: `formations: N not taken (no_card) · cf-R Σ ±x.xR, n=N [· suppressed K] [· input_stale K]`. The `unavailable` text is untouched. |
| `src/cobalt/replay/cli.py` | `formation_sources` production wiring (pool key, `RadarStore`, `TradeDefStore().loaded_for_evaluation`, `CachedDailyBars(cache).load`, tunables, defaults, clock) — imports `cobalt.radar` lazily inside the factory; summary line carries the formation counts. |
| `tests/cobalt/test_replay_formations.py` | **new**, 21 tests (1 `requires_db`). |
| `tests/cobalt/test_replay_runner.py` | absence is now injected (`unavailable_formations` stub) or simulated at the import (`p2_absent`); 5 new tests. |
| `docs/40 - DevDocs/cobalt/replay/formations.md` | **new page.** |
| `docs/40 - DevDocs/cobalt/{radar/evaluate_cli,replay/{__init__,cards,cli,line,models,runner}}.md` | dated `2026-09-18 — chunk E2` sections. |

No migration, no change to 0009 or its CHECK, no nullable shortcut, no new table, no ceiling/cadence/config change, no ranking or score reaching the card (L52 — this module writes only `"user".missed`, which no card reads).

## §4 Tests — red before, green after

### 4.1 The six that were red (build2 §1), all from one cause

All six failed with `ReplayError: S2-P2 formation replay is present but incompatible: missing ['membership_id', 'trade_def_md5']` — the adapter written when P2 was absent meeting P2's shipped model. **All six now pass.**

| Test | Fix |
|---|---|
| `test_nightly_report_lists_misses_with_the_gate_or_variable_that_excluded_them` | `fake_deps` injects `unavailable_formations` — the same injection every other store gets. These tests are about the run's order, commits and failures, not about the P2 binding. |
| `test_r2_3_a_retry_after_a_commit_boundary_resumes_idempotently` | as above |
| `test_archive_failures_are_counted_and_fail_the_job_at_the_end` | as above |
| `test_drc_note_absent_fails_the_line_step_and_creates_nothing` | as above |
| `test_dry_run_through_the_cli_writes_nothing_and_prints_rows_and_the_line_diff` | as above |
| `test_formation_replay_unavailable_logs_exact_line_no_rows` | **rewritten, not relaxed**: `monkeypatch.delitem(sys.modules, …)` only makes the next `import` re-read P2 from disk. Absence is now simulated at the import itself (`builtins.__import__` raises `ModuleNotFoundError` for both P2 module names). Still asserts the exact line and no rows. |

### 4.2 New tests, with their observed red

**All 21 tests in `tests/cobalt/test_replay_formations.py` — red before, at collection (verbatim):**
```
tests/cobalt/test_replay_formations.py:37: in <module>
    from cobalt.replay.formations import (
E   ModuleNotFoundError: No module named 'cobalt.replay.formations'
```
after: `20 passed, 1 skipped in 5.62s` (the skip is the `requires_db` one).

| Test | What it proves |
|---|---|
| `test_p2_replay_formation_carries_the_membership_id_md5_and_score_receipt_reference` | the P2-side change: a real run populates all three fields; the two formations carry two different digests; a second real run reproduces both (determinism) |
| `test_the_shipped_capability_marker_is_the_one_replay_binds_to` | `EVALUATOR_VERSION ∈ SUPPORTED_EVALUATORS` |
| `test_two_same_day_formations_of_one_ticker_and_def_persist_as_two_rows_under_the_extended_key` | **R1-21's case.** Two rows, `formation_at` 16:22 and 18:42, one member, one md5; the two subject keys differ **in index 5 only** (the `formation_at` slot) |
| `test_every_formation_row_satisfies_0009s_formation_check` | md5 / formation_at / pool_member_id all non-null; `card_id`/`mover_id` null; `excluded_by='no_card'` |
| `test_two_formation_rows_land_under_the_live_unique_index` (`requires_db`) | both rows insert through `MissedStore.reconcile` under the real partial unique index; skips cleanly offline |
| `test_an_existing_open_radar_card_for_member_def_direction_suppresses_the_miss` | suppression: 2 candidates, 0 rows, 2 suppressed |
| `test_a_card_on_a_different_member_def_or_direction_does_not_suppress` ×3 | the key is the (member, def, direction) triple, nothing looser |
| `test_cf_r_for_a_formation_is_the_one_formula_over_p2s_own_trigger_and_stop` | exact numbers from P2's own trigger/stop over the real tape: fill 5.3880 (gap-through, R1-9), stop exit 16:45, **cf_r −2.9000 / mfe_r 20.1000**; second formation fill 7.1100, **cf_r −27.0000 / mfe_r 118.5000** |
| `test_every_formation_number_replays_from_its_stored_receipt` | L57: `replay_formation_from_receipt` reproduces `inputs_sha256`, cf_r, mfe_r and the subject |
| `test_the_receipt_retains_the_p2_contract_facts_and_the_score_receipt_reference` | the receipt carries `p2_contract` (version, module, callable) and `score_receipt` (table, key, digest); gate order and `trade_count_band: unset` |
| `test_the_window_comes_from_the_one_public_resolver` | the horizon uses `resolve_window(None, day)`, not a second resolver |
| `test_formations_whose_trigger_never_traded_through_write_no_row` | the shipped def's own two formations never traded through — 2 candidates, 0 rows, 2 `no_trigger` |
| `test_bars_that_do_not_cover_the_day_are_input_stale_and_write_no_row`, `test_a_formation_with_no_bars_at_all_is_input_stale` | R1-12: counted, surfaced, never a fake R |
| `test_an_unsupported_evaluator_version_refuses` | loud on a marker this binding was not written against |
| `test_a_formation_whose_stop_sits_on_the_wrong_side_of_its_trigger_refuses` | the shared formula's own guard fires for a formation subject |
| `test_candidates_carry_every_field_the_row_needs` | the candidate mapping is P2's values, unaltered |
| `test_replay_formation_refuses_a_formation_stamped_for_another_day` | a formation from another ET date refuses |
| `test_formation_sources_name_every_argument_p2s_entrypoint_takes` | `FormationSources` is checked against `inspect.signature(replay_formations)` — the contract cannot drift silently |

**New in `tests/cobalt/test_replay_runner.py`:**

| Test | Observed red | After |
|---|---|---|
| `test_the_nightly_run_binds_to_p2s_shipped_replay_and_reconciles_its_formation_misses` | `TypeError: fake_deps() got an unexpected keyword argument 'formation_source'` (the seam did not exist) | passes: `formation_replay == "s2p2.1"`, 1 candidate → 1 row, `cf_r −1.0000 / mfe_r 0.8521`, trigger 15:47 UTC, the `MISS formation MU short member=202 formed=…` line, `formations: 1 not taken (no_card) · cf-R Σ −1.0R, n=1` on the miss line, and `radar_cards` → `reconcile:formation` → `upsert_unit` in order |
| `test_an_open_radar_card_for_the_formations_subject_suppresses_it_in_the_run` | same `TypeError` | passes: 1 candidate, 0 misses, 1 suppressed, **no** `missed.reconcile:formation` call |
| `test_r1_21_an_unsupported_p2_capability_marker_fails_loud` | before the edit `formation_replay` had no marker check — it raised `"present and carries the required fields, but replay's binding to it is not built"`, so `match="incompatible: evaluator version 's9p9.0'"` did not match | passes |
| `test_a_compatible_p2_with_no_sources_refuses_rather_than_half_wiring` | same message, `match="no formation sources"` did not match | passes |
| `test_an_unrelated_missing_module_is_never_read_as_p2_absent` | **no red** — this guards behaviour the pre-E2 code already had (`e.name not in {…}` re-raises). A regression guard, recorded as such rather than claimed as tests-first. | passes |

`test_r1_21_a_present_but_incompatible_p2_fails_loud` is **kept and strengthened**, not deleted: it was passing for the wrong reason. `import a.b.c as x` reads the attribute on the parent package before `sys.modules`, so the old `monkeypatch.setitem` alone never replaced the real module — the test was asserting against shipped P2, which happened to lack the fields. Once P2 gained them it failed, observed verbatim:
```
E       AssertionError: Regex pattern did not match.
E         Expected regex: 'incompatible.*membership_id'
E         Actual message: 'S2-P2 formation replay is present and compatible, but replay was given no formation sources — refusing rather than running a half-wired binding (R1-21)'
```
It now sets the package attribute as well, so its hand-built incompatible model is the one the adapter sees, and it passes on the real refusal. **ESCALATE 2.**

### 4.3 Real-shape fixtures (L45)

Nothing here hand-writes a `ReplayFormation`. Every formation comes out of a real `replay_formations` run:

| Case | Source |
|---|---|
| two same-day formations of one (ticker, def), both traded through | P2's own `bars-rubberband.real-shape.json` (FTFT), the shipped example def with one real `valid_setups.relation` value swapped to `with_trend` through P2's own `radar_p2_support.anatomy_def(**overrides)` helper |
| two same-day formations, neither traded through | the shipped def exactly as `radar_p2_support` ships it (`countertrend`) |
| the end-to-end nightly run | P2's evaluator over **P4's own** `bars-day.real-shape.json` → one real MU formation that triggers and stops out |

The `with_trend` variant is used because it is the variant whose two formations both traded through their trigger on the real tape — the only way to show two ROWS rather than two candidates. Both variants are exercised; the no-trigger one is a test in its own right. No fixture file was added, edited or invented.

**Note for Dejan's first read of the line:** the FTFT pair's planned risk is 0.02 (trigger 5.35 / stop 5.33), so the one formula gives −2.9R and −27.0R. That is correct arithmetic on a 2-cent stop, and the same class of figure as the −39.9R card already flagged in the 09-17 chunk-B report.

## §5 Suite results (verbatim)

`uv run pytest -q tests/cobalt tests/taxonomy`:
```
1704 passed, 306 skipped, 2 xfailed, 15 warnings in 51.91s
```
(Branch baseline before this chunk, build2 §1: `6 failed, 1673 passed, 305 skipped, 2 xfailed`. The 15 warnings are the pre-existing litellm `DeprecationWarning`.)

`uv run pytest -q tests/cobalt/test_replay_runner.py tests/cobalt/test_radar_evaluate*.py`:
```
60 passed, 2 skipped in 12.10s
```

`uv run pytest -q tests/cobalt/test_replay_formations.py`:
```
20 passed, 1 skipped in 5.62s
```

`uv run cobalt jobs restarts main..HEAD` (classifies the working tree too):
```
src/cobalt/radar/evaluate_cli.py   M   static import reach   com.cobalt.radar
src/cobalt/replay/formations.py    A   static import reach   com.cobalt.radar
src/cobalt/replay/runner.py        M   static import reach   com.cobalt.radar
src/cobalt/replay/models.py        M   static import reach   com.cobalt.aset,com.cobalt.radar
docs/40 - DevDocs/cobalt/replay/formations.md   A   DOCS   -
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
This chunk adds **no new resident** to the branch's existing RESTARTS line and **no new UNCLASSIFIED** row (the one `UNCLASSIFIED` on `.gitignore` is pre-existing in the range, not from this chunk).

## §6 What I could not do, and why

1. **No `requires_db` test ran.** One was written (`test_two_formation_rows_land_under_the_live_unique_index`); it skips cleanly offline and is the only proof that two formation rows survive the live partial unique index. The hub runs it on `cobalt_dev` with 0008/0009 applied. It seeds its own `radar_pool` + `radar_membership` row (the `pool_member_id` FK) inside the autouse `dev_db_tx` rollback.
2. **`cobalt validate` was not run** — the same permission wall chunk B hit. `cobalt jobs restarts` did run (above), and `import cobalt.replay.cli` is clean.
3. **Per-test red for three of the five new runner tests is honest but indirect.** The permission layer refused `git restore src` / `git apply -R` / `patch -R`, so I could not re-run the new suite against the pre-E2 source to capture a clean red for each. §4.2 states exactly what was observed for each test and marks the one test (`…never_read_as_p2_absent`) that guards existing behaviour and had no red at all.
4. **The DevDocs `INDEX.md` page list does not carry `cobalt/replay/*` at all** — chunk B's seven pages were never indexed either. I added `formations.md` as a page and did not index it, rather than index one page of eight. Pre-existing gap, named here, not fixed by this chunk.
5. **The formation window is `resolve_window(None, day)`**, so `W = session close` for every formation. That is not a shortcut taken here: `ReplayFormation` carries no window, and the plan's E2 scope names exactly three fields to add. It is the same limitation the 09-18 follow-up already recorded as ESCALATE 3 (`MissedStore.candidates()` has no window seam either), and it resolves with that ticket, not separately. **ESCALATE 4.**

## §7 ESCALATE (4)

1. **The plan's entrypoint name is wrong against the tree (Grok BLOCKER 2, root cause).** `plan-s2-p4-2026-09-15.md:184` and `:189` name `cobalt.radar.evaluate`. Shipped: the callable and its model are in `cobalt.radar.evaluate_cli`, the capability marker `EVALUATOR_VERSION` is in `cobalt.radar.evaluate`. The code follows the shipped layout and imports both statically; no shim accepts two spellings (L3). **The plan text needs the correction** — not this chunk's file to edit.
2. **`test_r1_21_a_present_but_incompatible_p2_fails_loud` was green for the wrong reason before this chunk.** `monkeypatch.setitem(sys.modules, …)` does not override `import a.b.c as x`, which reads the parent package's attribute first. The test was asserting against the real shipped module. It now sets both and asserts on its own hand-built incompatible model. **Worth a sweep: any other test in the tree that injects a module by `sys.modules` alone is injecting nothing.**
3. **The score-receipt reference is content-addressed, by necessity.** P2's `--replay` writes nothing and reads no receipt row, so it cannot report a `system.radar_score` id — only the natural key `(membership_id, trade_def_md5)` plus that row's `inputs_sha256`. This is enough to resolve the receipt and enough to detect divergence, and it needed no write and no schema change (so: not a STOP). If a hard FK to the score row is ever wanted, that is a P2-side change (the replay would have to read `system.radar_score`) and a `missed` schema change — a ruling, not a build decision.
4. **Formation horizons are always the session close.** `ReplayFormation` carries no window and the live radar path's own `radar_deadline(preferred_windows_ref, …)` is not in the replay contract, so `resolve_window(None, day)` applies and the `window` gate can never fire for a formation (recorded in `gate_detail`, not hidden). Same root cause as the 09-18 follow-up's ESCALATE 3 (replay's missing window seam); whoever wires the trade_def-attachment detector must wire both, or formation horizons silently diverge from the live path the day a real window is used.

---

RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar · suite 1704 passed / 0 failed · ESCALATE 4 · not committed (the hub commits)
