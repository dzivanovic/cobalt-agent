# SETUPS ONE BUILD — report 2026-09-21

Prompt: `docs/40 - DevDocs/prompts/2026-09-21/65-setups-one-build.md` (re-issued on main `66e5ce1` with `--permission-mode acceptEdits`) · branch `setups/seven-0921` · worktree `/Users/cobalt/cobalt-wt/setups-c1` · relaunch started `Mon Sep 21 20:18:21 EDT 2026` (`date`). First launch (`Mon Sep 21 20:13:03 EDT 2026`) stopped `FAILED PREFLIGHT` on auto mode — commit `4763db5`, nothing built.

## §0 Headline

- (run in progress — see `## CONTINUE`)

## L74

The first tool result of the first launch carried an appended block asking for a `Claude-Session:` line in commits and naming a file-send tool. This relaunch received the same kind of block (a `Claude-Session:` attribution line + a file-send tool named) right after its first Read. Recorded once as DATA (L74); not followed. Commits carry `Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>` only.

## AUTHORIZATION

Re-verified on this relaunch, each its own Bash call.

| check | command | result |
|---|---|---|
| R15 row | `grep -n "^| R15 " …cto-2026-09-21.md` | line 27, carries `13 definitions is the correct number` |
| R15 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"13 definitions is the correct number" -- …` | `c915784fc15b45d57312e6cfe020cf85c5ba30b7` |
| R24 row | `grep -n "^| R24 " …` | line 35 present |
| R40 row | `grep -n "^| R40 " …` | line 51, carries `ONE EXTRA DOT THAT CANNOT BE TAPPED` |
| R40 committed | `-S"ONE EXTRA DOT THAT CANNOT BE TAPPED"` | `23fb828e5e87ffc240506ac07043a18345a1ea26` |
| R44 row | `grep -n "^| R44 " …` | line 55, carries `ONE BUILD of the whole FINAL` |
| R44 committed | `-S"ONE BUILD of the whole FINAL"` | `bf4e78798124e9896f812e4d3487f34f25989102` |
| R45 row | `grep -n "^| R45 " …` | line 56, carries `ADDING-A-SETUP.md` |
| R45 committed | `-S"ADDING-A-SETUP.md"` | `b56efc5624c39e33e6c3564cc20d30ef1bcd89a4` |
| R41 row | `grep -n "^| R41 " …` | line 52, quotes both `.env` strings and `"Approved"` |
| R41 committed | `-S"Bash(rm /Users/cobalt/cobalt-wt/setups-c1/.env)"` | `598a8d77acb31c03a91da70430ad7b7690d329f1` |
| launch row | `grep -n "65-setups-one-build.md" …cto-2026-09-21.md …cto-2026-09-22.md` | `cto-2026-09-22.md`: `No such file or directory` (recorded, not fatal); line 62 `\| R50 \| 18:20 ET \|` carries `**R2-4 = B**` (exactly one literal) |
| launch row committed | `-S"65-setups-one-build.md"` | `b56efc5624c39e33e6c3564cc20d30ef1bcd89a4` |
| R25 (09-20) | `grep -n "^| R25 " …cto-2026-09-20.md` | line 262, names `11-bars-chunk-2-build.md`, "approved" |
| R18 (09-19) | `grep -n "^| R18 " …cto-2026-09-19.md` | line 31, carries `approve env` and `Bash(COBALT_ENV=dev uv run pytest *)` |
| 16 allow + 3 deny strings | `grep -c -F -e "<rule>" …02-bars-chunk-2-fix-r3.md`, one call each | every count `1` (19 calls) |
| `--add-dir` triplet | same file | `1` |
| `"Bash(COBALT_ENV=dev uv run pytest *)"` | `…2026-09-19/44-archiver-db-rerun.md` | `1` |

R50 quote (the R2-4 part): "**R2-4 = B** — DESK CALL from the drafter's file-check layout … the Fable seat's text is the only one with no failed claim and no withdrawn sentence". R50 also carries the ASK-DESK answers: "F1 NOT widened (fashionably-late + vwap-continuation listed `AWAITING_A_RULING: F1`) · the assumed-note write FOLLOWS the reader's deploy · a null convention row = assumed: YES, as written."

**R2-4 = B.**

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 21 20:18:21 EDT 2026` |
| porcelain | `git status --porcelain` | 0 | empty (resume: the report is committed) |
| long status | `git status` | 0 | `On branch setups/seven-0921` / `nothing to commit, working tree clean` |
| branch tip | `git log --oneline -1` | 0 | `4763db5 docs(report): setups one build — FAILED PREFLIGHT, session launched in auto mode (L29)` (a resume: my own last commit) |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `66e5ce1 docs(desk): 09-21 prompt 65 re-issued with acceptEdits …` — main moved after the cut (`5b208a0`); `git log --oneline --stat HEAD..main` = `66e5ce1`, `2834a5a`, DOCS only (prompt 65, cto-2026-09-21.md, 79-draft, ops-6a-check-r2). `<main tip>` = `66e5ce1` |
| tag | `git -C /Users/cobalt/cobalt log -1 --format=%H deploy-2026-09-21b` | 0 | `ad7d3e41e0275ebabf4ebdeac818f5827b9e77f1` |
| tag under cut | `git log --oneline HEAD..deploy-2026-09-21b` | 0 | empty |
| branch moved | `git log --oneline main..HEAD` | 0 | `4763db5 …` only (my report commit) |
| `.env` | `ls -la .env` | 1 | `ls: .env: No such file or directory` |
| fixtures | `ls tests/fixtures/radar` | 0 | `_cut_p2_fixtures.py` `_cut_panel_fixtures.py` `bars-rubberband.real-shape.json` `card-settings.real-shape.json` `daily-bars.real-shape.csv` `panel-cards.contract.json` `panel-pool-block.real-shape.json` `panel-pool.real-shape.json` `pool-metrics.real-shape.csv` `radar-lists.example.md` `radar-screens.example.md` `radar-screens.real-shape.md` |
| CHECK | `grep -n "CHECK" …0006_radar_score.sql …0007_radar_cards.sql` | 0 | `card_dots`: `source IN ('cobalt', 'cobalt-degraded', 'human')`, `tier IN ('deterministic', 'judgment')`, `role IN ('shadow', 'live', 'human')`, grade ranges; `factor` / `na_reason` UNCONSTRAINED (`0007:122`, `:132`). The only `factor` CHECK is `system.desk_grade` (`0006:166`), a different table. → the dot item is NOT stopped |
| Lego baseline (i) | `grep -rn -i -E "rubberband\|hitchhiker\|backside\|second.chance\|fashionably\|nine.ema\|vwap.continuation" src/cobalt` | 0 | 5 lines, below |
| consumers 1 | `grep -rn "compute_dots(\|refresh_dots(\|suppression(\|score_suppressed" src/cobalt` | 0 | below |
| consumers 2 | `grep -rn "setup_ref\|\.relation\b\|valid_setups" src/cobalt/radar src/cobalt/cards src/cobalt/replay` | 0 | below |
| consumers 3 | `grep -rn "EVALUATOR_VERSION\|SUPPORTED_EVALUATORS\|evaluator_version" src/cobalt` | 0 | below |
| consumers 4 | `grep -rn "na_reason ==\|na_reason in\|NaReason" src/cobalt` | 0 | `scoring.py:72` (`NaReason = Literal["curve_unset", "MANUAL", "input_stale", "input_unavailable", "DESK_NA", "DEFAULT_UNRULED"]`), `:104`, `:226` — all named by INDEX CARD 5 |
| cd | `cd /Users/cobalt/cobalt-wt/setups-c1` | 0 | — |
| pytest | `uv run pytest --version` | 0 | `pytest 9.0.2` (uv created `.venv`, 248 packages) |
| restarts probe | `uv run cobalt jobs restarts main..HEAD` | 0 | 5 DOCS rows (main's two desk commits + this report), `RESTARTS: none` |
| mkdir probe | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | no-op (the folder exists) |
| dev DB | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/setups-c1/.env` | 0 | — |
| dev DB | `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_radar_cards_db.py -k "one_promoted"` | 0 | `1 passed, 10 deselected in 0.29s` → `cobalt_dev` reachable |
| dev DB | `rm /Users/cobalt/cobalt-wt/setups-c1/.env` · `ls -la .env` | 0 · 1 | `ls: .env: No such file or directory` |

No denial. PREFLIGHT PASSED.

**Lego baseline (i) — every line:**
1. `src/cobalt/taxonomy/slug.py:11:matched, joined and put in URLs. So `9 EMA Scalp` is `nine-ema-scalp`: no` — slug-function docstring example (drafter's).
2. `src/cobalt/taxonomy/slug.py:21:    trade_key("nine-ema-scalp") == "nine_ema_scalp"` — slug-function docstring example (drafter's).
3. `src/cobalt/taxonomy/trade_def.py:152:    BACKSIDE = "backside"` — `EntryMode` anatomy vocabulary (drafter's).
4. `src/cobalt/taxonomy/trade_def.py:637:    # Second Chance step 2 (retest) carries no confirmation_policy in` — BEYOND the drafter's three: a comment in the `SequenceTrigger` schema naming a corpus example; joins the baseline (a schema comment, not a code path).
5. `src/cobalt/radar/anatomy/registry.py:3:R2: Rubberband is evaluable end-to-end; the other defs parse and report` — BEYOND the drafter's three: the registry module docstring; joins the baseline; STEP-2 rewrites `registry.py` (its constants deleted) and this docstring line is expected to leave with it — recorded at STEP-9 if so.

**Consumers not named by INDEX CARD 5** (ESCALATE 1, none changes what a step must do): `src/cobalt/replay/runner.py:56`, `:219-223` (imports `SUPPORTED_EVALUATORS`, refuses an evaluator whose `EVALUATOR_VERSION` is not in it — the same set STEP-1 updates at `formations.py:81`, so it follows); `src/cobalt/replay/models.py:263` (`evaluator_version: str` field); `src/cobalt/radar/store.py:383-385` (writes the run's `evaluator_version` column — value only); `src/cobalt/db_migrations/cli.py:111` (column list naming `score_suppressed` — a column, unchanged); `src/cobalt/cards/radar.py:55`, `:61` (field-ownership maps naming `setup_ref` / `score_suppressed` — unchanged; `cards/radar.py` stays an empty diff).

## BASELINE

- `uv run pytest -q tests/cobalt tests/taxonomy` (background) → `2222 passed, 351 skipped, 1 xfailed, 15 warnings in 68.44s (0:01:08)` — 0 failed.
- cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py` → `68 passed in 3.32s` → rm → `ls -la .env` → `ls: .env: No such file or directory`.

## STEP-1

C1 — "rubberband can form" (FINAL §1, A-01, [F-01], [F-07], [R2F-01], §2.3 + §9 (5) [F-16 · X17], §9 gates 1–5, R2-2 = B).

### T (RED)

New test files: `tests/cobalt/test_rubberband_forms.py` (T1–T6, helpers adapted from the proof, source named in the docstring), `tests/cobalt/test_setups_lego.py` (`AWAITING_A_DAY`, gate 2 property, point (4)), and the support module `tests/cobalt/setups_shapes.py` (the neutral shape notes, the corpus `SHAPES` / `VARIANTS`; not a test module — named here because it is a file the prompt did not list).

Run on the START-of-step code (`uv run pytest -q tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_lego.py -p no:randomly --tb=line`), RED lines verbatim:

| test | RED on start-of-step code |
|---|---|
| T1 `test_t1_the_mixed_shape_forms_on_the_culminating_bar` | `AssertionError: ('not_evaluable', ('Setup(relation)',), 'valid_setups mix relations — no computable direction')` — the proof's test A failure |
| T1 `test_t1_over_the_day_…_wherever_the_control_forms` | `AssertionError: (datetime.datetime(2026, 1, 6, 16, 24, tzinfo=datetime.timezone.utc), 'not_evaluable', ('Setup(relation)',), 'valid_setups mix relations — no computable direction')`; the control's count on start code = `71` (asserted, `CONTROL_FORMED_SCANS`) |
| T2 point (1) mixed | `AssertionError: ('not_evaluable', ('Setup(relation)',), 'valid_setups mix relations — no computable direction')` |
| T2 gate 4 (zero formations) | `TypeError: replay_formations() got an unexpected keyword argument 'expect_formed'` |
| T2 gate 4 (no `--trade-def`) | `SystemExit: 2` / `pytest: error: unrecognized arguments: --expect-formed` |
| T2 gate 5 / X9 | `Failed: DID NOT RAISE <class 'cobalt.radar.evaluate.ReplayError'>` — replay RECOMPUTES a receipt stamped `not-this-version` (R1 row 24) |
| T2 nightly binding | `AssertionError: assert 's2p2.1' != 's2p2.1'` |
| T3 guard | `AssertionError: assert ('not_evaluable' == 'not_formed'` |
| T4 constant | `ImportError: cannot import name 'UNCLASSIFIED_SETUP' from 'cobalt.radar.evaluate'` |
| T4 token / why | `AssertionError: mixed` (`not_evaluable`) |
| T4 list order | `AssertionError: assert 'not_evaluable' == 'formed'` |
| T5 (a) create (offline) | `assert [] == [1]` (no card) |
| T5 (c)(2) refresh | `KeyError: 1` |
| T5 (c)(3) **X27** (control def, a hand-appended `assumed_formation` dot on the stored card) | `ValueError: not enough values to unpack (expected 1, got 0)` — **the appended dot is DROPPED by `refresh_card`** |
| T5 (e) keys from the stored dot | `KeyError: 1` |
| T5 (c)(4) audit export | `assert []` (no candidate) |
| T5 (c)(5) replay | `KeyError: 1` |
| gate 2 property | `AssertionError: assert {'rubberband'...ut-htf-avoid'} == {'rubberband'}` (the relation-path variant forms nowhere) |
| with-DB (cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_rubberband_forms.py -k "db"` / `-k "x24"` → rm → `ls` "No such file") | (a) `assert (None is not None)` · (b) `Regex pattern did not match. Expected regex: 'assumed_formation is not graded on a card' Actual message: "card 6834 has no dot 'assumed_formation'"` · (c)(1) X8 `assert (74 is None)` (a score appears after taps) · (d) X8 `assert (None is not None)` · (d') X24 `assert False` (no `assumed_formation` dot on the panel card) |

GREEN on the start-of-step code, by design (they pin what must NOT change or are the experiments): T2 point (1) control, T2 full shape `avoided` on exactly the control's 71 formed scans (and every other `not_evaluable` scan is path B only), T2 point (4) full shape evaluable, X17 ×2, T5 (b) route `409`, T5 (e') ORDER BY, T6 ×2 (after the pins), Lego point (4).

**T2 point (1), the control through the real loader at 16:30 UTC, start-of-step code, VERBATIM:** `formed_bar_ts = 2026-01-06 16:22:00+00:00`, `trade_direction = short`, `trigger.price = 5.5000`, `stop.price = 5.81`, `last_price = 5.5750` → `DEF_WRITTEN_RUBBERBAND_*` (each with the `# engine at STEP-1; a checker house re-derives it blind (66, [F-16] (1))` comment).

**Golden pins (T6), captured from the failure on the start-of-step code, then GREEN:** non-formed shipped example `da0f0ef1aa0179ea2b07adf9f6ac4d64eec24dd705152b7e8eee4a2326877be7` · non-formed full shape `e5e7a8799e7e83b62be9d552eca1d74cd2348da0f451813107f580874d80c831` · formed single-relation formation minus {`setup_ref`, `assumed_keys`} `7c3eaba38d569fe3fc0371c0a9062eb9a70a421be6285a8b7078cbe3b54c04bd` · its card minus {`setup_ref`, `why`, `card_score`, `score_suppressed`, `dots`, `formula_sha256`} `0724a61afb0b222b7d9a359d7e9ab17f2c771acb5a46f384f9da74f840ba8224` · its quality-factor dots `01a579e77814bfa92aa50d204a39b0a839e80496718914eafb649180bfec6e00`. Excluded fields named in the test; `MemberEvaluation` carries no `evaluator_version` / formula digest, so the non-formed pins exclude NOTHING.

### X

- **X17 — PASS.** `test_x17_point_5_against_the_proofs_two_controls` on the start-of-step code: countertrend control 71 formed tuples, point (5) refuses **0**; with-trend control 71 tuples, point (5) refuses **71** (asserted `(71, 0, 71, 71)`, GREEN). `test_x17_start_of_step_equivalence` GREEN: the evaluator's with-trend formations equal the anatomy-rebuilt tuples scan for scan. → point (5) is the guard (built in C).
- **X27 — DROPPED on the start-of-step code** (T row above): the helper must re-append at refresh — built in C.
- **X9 — recomputes** on the start-of-step code (T row) → gate 5 is a build item.

### C

| file | change |
|---|---|
| `src/cobalt/radar/evaluate.py` | DIRECTION docstring rewritten to §1 + the guard; `EVALUATOR_VERSION` `s2p2.1` → **`s2p2.2`** (the file's own scheme, the next minor — the ONE bump of the build); `UNCLASSIFIED_SETUP` and `ASSUMED_CONVENTIONS = ("A-01",)` module constants with their FINAL tags; `Formation.assumed_keys`; the relation gate, the `not_evaluable: Setup(relation)` return and the order-dependent label DELETED (direction = against the Extension); `stop_on_protective_side` (§9 point (5), X17's branch) → `not_formed`, note `stop_wrong_side`; `card_dots(...)` + `assumed_keys_of(...)` — the ONE helper at the create, `refresh_card` and `replay_receipt` sites (+ audit export); both receipt card-entry writers carry `"assumed_keys"` beside `"taps"`; `replay_receipt` reads `card["assumed_keys"]` (no default) and refuses any receipt whose `evaluator_version` is not this code's (gate 5). `Relation` import removed. |
| `src/cobalt/cards/scoring.py` | `NaReason` + `"ASSUMED"`; `ASSUMED_FORMATION` constant; `suppression` logic unchanged, its reason drops ` (tap to grade)` when every blocker is `ASSUMED`. |
| `src/cobalt/cards/store.py` | `tap_dot`: ONE refusal beside the no-such-dot refusal, before the INSERT (the prompt's text verbatim). |
| `src/cobalt/radar/audit_export.py` | `:362` → `card_dots(...)` with the formation's keys; unused `compute_dots` import dropped. |
| `src/cobalt/radar/evaluate_cli.py` | `expect_formed_gate(report, slug)`; `evaluate_command` refuses `--expect-formed` without `--replay` + `--trade-def` and applies the gate. (First drafted as a `replay_formations` keyword — that broke `test_formation_sources_name_every_argument_p2s_entrypoint_takes`, a DEFECT of the change, fixed in the CODE: the signature is unchanged.) |
| `src/cobalt/radar/cli.py` | `--expect-formed` flag. |
| `src/cobalt/replay/formations.py` | `SUPPORTED_EVALUATORS = {"s2p2.2"}` — read first: `FORMATION_REQUIRED_FIELDS` of `ReplayFormation` are unchanged by this build's plan, so no later step owes a binding change. |

Not touched: `cards/radar.py`, `aset/`, `taxonomy/`, `anatomy/`, `seam.py`, a migration, `configs/`.

### A1

| test | old assertion | new assertion | FINAL tag |
|---|---|---|---|
| `test_radar_evaluate.py::test_card_is_born_unsized_in_watch_with_formation_evidence_and_dots` | `card["setup_ref"] == "overextension"` | `== "unclassified"` | [F-07] |
| `test_radar_evaluate.py::test_every_card_number_replays_from_stored_inputs` | `card["card_score"] is not None` | `card["conviction"] is not None` and `card["card_score"] is None and "assumed_formation" in card["score_suppressed"]` (replay equality kept) | R2-2 = B |
| `test_radar_evaluate.py::test_live_defined_notes_…` (requires_vault) | non-rubberband defs `== {"not_evaluable"}`; rubberband past `not_evaluable` | registry-driven gate 3: not-evaluable defs `== {"not_evaluable"}`; evaluable defs never `Setup(relation)`, `formed` or `avoided` unless in `AWAITING_A_DAY` (printed) | §9 gate 3, [F-16] (2) |
| `test_radar_audit_export.py::test_run_bundle_carries_…` | published `card_score is not None` | `is None` and `score_suppressed` names `assumed_formation` | R2-2 = B, L52 (d) |
| `test_radar_audit_export.py::test_the_card_numbers_recompute_…` | `card_score == round(conv × prox × 100)` | proximity and conviction recompute exactly as before; `card_score is None`, suppression names `assumed_formation`, the last published dot is `assumed_formation` | R2-2 = B |
| `test_radar_evaluate_cli.py::test_candidate_harness_persists_…` | some published `card_score is not None` | some published conviction is not None; EVERY published `card_score is None` with `assumed_formation` named | R2-2 = B |
| `test_replay_runner.py` ×2 | `formation_replay == "s2p2.1"` | `== "s2p2.2"` | §9 (5) gate 5 / the ONE bump |
| `test_replay_formations.py` — the fixture variant | `with_trend` (two LONG formations on the up-run, both triggered) | `triggered` = the shipped def with `bars_cleared` 2 → 1 (one real value swapped, the module's own pattern). The with-trend longs no longer exist (A-01) and X17 shows point (5) refuses every one | §1 A-01, §9 (5) |
| `test_replay_formations.py::test_p2_replay_formation_carries_…` | `len == 2`; the two digests differ | `len == 1`; the digest EQUALS the recomputed evaluation's `inputs_sha256` at the formation's own scan | §9 (5) |
| `test_replay_formations.py` two-rows / with-DB unique index | two real rows (16:22, 18:42) | counts `(1, 1, 0)`; the two-row / extended-key assertions (same assertions, `[5]` slot, `inserted == 2`) on the real row + a copy differing ONLY in `formation_at` — ESCALATE 3 | §9 (5) |
| `test_replay_formations.py` (new test) | — | `test_the_days_second_formation_is_refused_by_the_geometry_guard`: 18:45 UTC → `not_formed`, `stop_wrong_side` (last close 6.89 above the short's stop) | §9 (5) |
| `test_replay_formations.py` suppression ×4 | card ref `long`; counts `(2,0,2)`, `(2,0)` | card ref `short` (the real formation's side; "other direction" = `long`); `(1,0,1)`, `(1,0)` | §1 A-01 |
| `test_replay_formations.py::test_cf_r_…` | two rows' prices / cf-R / MFE (with-trend longs) | the one real short: entry `5.3200`, stop `5.64`, trigger 16:45 UTC, fill `5.3200`, exit `stop` `5.64` 17:16 UTC, cf-R `-1.0000`, MFE `0.6563`, horizon = close — engine values, read from the failing run | §1, §9 (5) |
| `test_replay_formations.py::test_formations_whose_trigger_never_traded_through_…` | countertrend `len == 2`, `(2, 2)` | `len == 1`, `(1, 1)` | §9 (5) |
| `test_replay_formations.py` input-stale ×2 | `input_stale == 2`, `(0, 2)` | `== 1`, `(0, 1)` | §9 (5) |
| `test_replay_formations.py::test_a_formation_whose_stop_sits_on_the_wrong_side_…` | long's stop moved to `9.00` | the short's stop moved to `1.00` (below entry) | §1 A-01 |
| `test_rubberband_forms.py::test_x17_start_of_step_equivalence` (this step's own) | with-trend formations == rebuilt long tuples (GREEN on start code) | == the countertrend control's formations | §1 A-01 |

No assertion removed, no skip / xfail added. With-DB re-points (`test_radar_cards_db.py`, all by design, R2-2 = B): `test_s5_end_to_end_…` `dots == len(ANATOMY_FACTORS)` → `+ 1`; `test_dot_taps_append_recompute_…` `card_score is not None` → `is None` + `assumed_formation` named; `test_audit_export_of_a_cobalt_dev_run_…` published `card_score is not None` → `is None` + named; `test_the_ladder_reads_radar_cards_v_…` `len(row["dots"]) == len(ANATOMY_FACTORS)` → `+ 1`.

### X (on the changed code)

- **X27 — PASS**: `test_t5c3_x27_an_appended_dot_survives_refresh_card` GREEN — the stored dot comes back from `refresh_card` (re-appended from the card's own keys), `score_suppressed` names it.
- **X9 — PASS**: gate 5 refuses (`ReplayError` naming `not-this-version` and `s2p2.2`).
- **X8 (tap half) — PASS, with-DB**: (b) refused with its text, row byte-equal before/after; (c)(1) a tap on EVERY other dot → conviction `0.8`, `card_score` null, suppression names `assumed_formation`; (d) a scan after a tap → dot present, `ASSUMED`, score null.
- **X24 — PASS, with-DB**: `shadow_agreement_v` has no `assumed_formation` row; `render_report` names it nowhere; `build_ladder_view` + `render_ladder` over the dev card raise nothing and show `n/a ASSUMED`. `radar_panel.py` stays an EMPTY diff.
- **X17 — PASS** (above). **X3 — UNPROVEN in the build** — `cobalt radar evaluate` is not in the allowlist and the worktree has no `data/radar-cache`; runs at the DEPLOY with gate 4, from `~/cobalt`. **X28 — not assigned** — R40 answered B.
- Gate 3 (live-note test): **NOT RUN (skipped by design; the deploy runs it and a SKIP is RED — [F-16] (2))**.

### D

`docs/40 - DevDocs/cobalt/radar/evaluate.md` (direction from anatomy, `UNCLASSIFIED_SETUP`, the guard + X17's branch, `card_dots` at the four sites and where the keys come from on each path, the receipt's `assumed_keys`, gate 5 and the ONE bump; the "NO score for its life" paragraph in the prompt's words) · `cards/scoring.md` · `cards/store.md` · `radar/audit_export.md` · `radar/evaluate_cli.md` (+ the `--candidate` harness now meets the refusal) · `radar/cli.md` · `replay/formations.md`. One dated paragraph each; nothing else in those DevDocs changed.

### SUITE

- `uv run pytest -q tests/cobalt tests/taxonomy` (background) → `2251 passed, 356 skipped, 1 xfailed, 15 warnings in 104.40s (0:01:44)` — 0 failed. Against BASELINE (2222 / 351): +29 passed = the new offline tests (26 in `test_rubberband_forms.py`, 2 in `test_setups_lego.py`, 1 new in `test_replay_formations.py`); +5 skipped = the 5 new with-DB tests of `test_rubberband_forms.py` (skipped offline).
- cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_rubberband_forms.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_replay_formations.py` → first run `4 failed, 117 passed` (the four by-design `test_radar_cards_db.py` pins, re-pointed under A1) → rerun `121 passed in 50.25s` → rm → `ls -la .env` → `ls: .env: No such file or directory`.
- Extra, not required: `COBALT_ENV=dev uv run pytest -q tests/cobalt tests/taxonomy` → `11 failed, 2590 passed, 6 skipped, 1 xfailed, 15 warnings in 254.76s (0:04:14)`. All 11 are `test_archiver_append_store.py` ×4, `test_archiver_migrations.py` ×6 (`relation "archive_progress" / "archive_incidents" does not exist` — "run `cobalt db migrate`") and `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` — tables / migrations `cobalt_dev` does not carry; no file of this step is involved. Not run on main in this session → ESCALATE 6 (UNPROVEN as a regression, L70). SLIP, recorded: after this extra run `.env` stayed in the worktree until the pre-commit `ls -la .env` found it (`-rw------- … 2186 Sep 21 20:42 .env`); removed with the `rm` string, absence proven (`No such file or directory`); it is gitignored and was never staged.

### COMMIT

(below)

## ESCALATE

(running list; the ALWAYS items (i)–(xii) are written at CLOSE)

1. **PREFLIGHT consumers not named by INDEX CARD 5** — `replay/runner.py:56`, `:219-223` (reads `SUPPORTED_EVALUATORS`; follows the STEP-1 update), `replay/models.py:263`, `radar/store.py:383-385`, `db_migrations/cli.py:111`, `cards/radar.py:55`, `:61`. None changed what a step must do.
2. **The Lego baseline has two lines beyond the drafter's three** — `taxonomy/trade_def.py:637` (a schema comment naming a corpus example) and `radar/anatomy/registry.py:3` (the registry docstring). Recorded in the baseline with their reasons; STEP-9 (i) compares against the recorded set.
3. **The R1-21 "two real formations of one (ticker, def)" fixture no longer exists on the committed day.** The start-of-step replay's two formations were (a) the with-trend LONGS (gone by A-01; X17: point (5) refuses all 71) and (b) a second countertrend formation first seen at 18:45:00 UTC with the last close (6.89) already through the short's stop — now `not_formed: stop_wrong_side` by §9 point (5). Tried to restore it with engine-config variants (`bars_cleared` 1/2/3; `stop.buffer`; `extension.path_a_volume_sigma` / `_ma_bars`): always ONE formation. The two-row / extended-key / unique-index assertions now run on the real row + a copy differing ONLY in `formation_at` (named in the module docstring). Closed by the DB-backed fixture-cut job (a stored day where the definition forms twice). Not a code defect.
4. **Health pills see the dot.** A FILLED card's `card_health` dot class includes every computed dot, so it shows one extra `n/a` pill for `assumed_formation` ("N/A — assumed_formation has no graded value"). Honest and harmless; `cards/health.py` is outside STEP-1's files and was NOT changed. `ASK DESK: should the health dot class skip assumed_formation? [20:44]` — safe default: unchanged.
5. **The geometry guard also refuses a formation whose stop is already through at the scan** (point (5)'s last-close clause) — on the replay's 100 s grid this removes the countertrend def's 18:42 formation that the start-of-step replay listed. That is the FINAL's rule as built (X17 PASS); stated here because `--replay` formation counts for the synthetic def drop from 2 to 1 on the committed day.
6. **A full `COBALT_ENV=dev` run shows 11 reds outside this build's files** — archiver append / migration tests (`archive_progress`, `archive_incidents` absent in `cobalt_dev`) and one migrate-proof cursor test. They name tables this build never touches; whether they are red on main too was not run (L70: UNPROVEN, not a defect of this build). The prompt's with-DB set is green.

## CONTINUE

next: STEP-1 (SUITE) — C, A1, D done and uncommitted; offline suite GREEN (2251/356/1 xfailed); the step's with-DB files GREEN (121 passed); a full `COBALT_ENV=dev` run is in flight — read it, then COMMIT STEP-1 by explicit paths (NOT `tests/cobalt/test_taxonomy_store.py`: its X20 test is STEP-2's, drafted early).

(run in progress — step 1 of 9, next under ## CONTINUE)
