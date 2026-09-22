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

`58aa823 feat(setups): STEP-1 rubberband can form — direction from anatomy, unclassified setup, geometry guard, untappable assumed_formation dot (FINAL C1, R40 B)` — `git show --stat HEAD`: 24 files, 1361 insertions(+), 139 deletions(-); every path one named above (7 DevDocs + this report, 7 `src/` files, 6 re-pointed test files, 3 new test files). `tests/cobalt/test_taxonomy_store.py` (STEP-2's X20 test, drafted early) left out on purpose.

## STEP-2

C2 — the registries, the mirrored frame, the interpreter shapes, the assumed store (FINAL §2, §4, §7-B, §8; R2-3 by X20, R2-4 = B per R50).

### X (before C)

**X20 — RUN FIRST.** `tests/cobalt/test_taxonomy_store.py::test_x20_a_sync_with_one_null_slug_row` (the `store` fixture inside the suite's rollback transaction; the `LoadedTunable` built with `model_construct` because the model types `slug: str`) — cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_taxonomy_store.py -k x20 -s` → rm → `ls` "No such file". VERBATIM: `X20: NotNullViolation: null value in column "slug" of relation "tunables" violates not-null constraint` · `1 passed, 14 deselected in 0.10s` — the test asserts `store.slugs() == [] and store.tunable_keys() == []` after the failed sync: the WHOLE sync rolled back (the example def's upsert included).

**The three reads B rests on, re-read on this branch:**
- (R1) HOLDS — `src/cobalt/radar/evaluate.py:1253-1255` (after STEP-1's line shift): `engine_rows = dict(self.tunables_loader())` / `defs, user_rows = self.defs_source()` / `tunables = merge_tunables(engine_rows, user_rows)`; the resident's `defs_source` is `TradeDefStore.loaded_for_evaluation` — `taxonomy/store.py:127` `SELECT key, row FROM tunables ORDER BY key`, `:132` `{key: TunableRow.model_validate(row) …}` — bare rows, no reader identity.
- (R2) HOLDS — `grep -rn "INTO tunables\|FROM tunables\|UPDATE tunables" src/cobalt`: the only writer is `taxonomy/store.py:185` `INSERT INTO tunables (key, row, slug, loaded_at)` inside `sync`, which prunes at `:202` `DELETE FROM tunables WHERE NOT (key = ANY(%s)) RETURNING key`.
- (R3) HOLDS — `taxonomy/migrations/0001_trade_defs.sql:63` `slug       TEXT NOT NULL REFERENCES trade_defs(slug) ON DELETE CASCADE,`.

**DECISION TABLE ROW:** R1 and R2 HOLD and X20 = violation + rollback → **R2-3 = B WITH its migration.** Home: the database-wide registry `src/cobalt/db_migrations/` (a rollback cannot live in `taxonomy/migrations/`, which `ensure_schema` runs forward on every load). Number: main carries 0001–0011; the unmerged `bars/chunk-2-0920` carries `0012_bars_partitioned_parent` (`git -C /Users/cobalt/cobalt log --oneline --name-only main..bars/chunk-2-0920 -- src/cobalt/db_migrations` → `02d67a6 … 0012_bars_partitioned_parent.sql`, `.rollback.sql`, `__init__.py`, `placement.py`); `bars/chunk-1a-0920` adds no number → **`0013_tunables_slug_nullable`** — an L68 seam on `db_migrations/__init__.py` with `bars/chunk-2-0920`.

### T (RED)

New: `tests/cobalt/test_setups_registries.py` (registries, E8/E9, the frame property, X4/X6/X12/X18/X21/X25, R2-4 B publication and the per-card reads, the closure + convention rows, X8's `source` half, Lego (ii) pins) and `tests/cobalt/test_assumed_store.py` (reader, hole-fill X19, F1 not widened, writer + X23 on `tmp_path`, dry-run, migration 0013). Run on the START-of-step code (STEP-1, `58aa823`): the `-rA` listing shows 34 FAILED, 14 PASSED, 3 SKIPPED (counted from its lines; the run printed no summary line in the captured output). RED lines verbatim, one per kind:

| test | RED |
|---|---|
| the five tables | `ModuleNotFoundError: No module named 'cobalt.radar.formation'` |
| the registry keeps no constants | `AssertionError: SUPPORTED_ATOMS` |
| E8 domain | `assert not True` (`Evaluability(evaluable=True, …)` for `Extension.state IN {reverting, backside}`) |
| E9 registry ⇔ interpreter | `AssertionError: ('example-anatomy-reversal', ('Unsupported(arith)',))` — the registry calls an Arith precondition evaluable, the interpreter refuses it |
| F-04 / R2F-12 / X6 / X18 | `ModuleNotFoundError: No module named 'cobalt.radar.anatomy.frame'` |
| B published row / X21 | `AttributeError: 'MemberEvaluation' object has no attribute 'by_side'` |
| B publication rule | `ImportError: cannot import name 'publish_frames' from 'cobalt.radar.evaluate'` |
| B per-card read (open short card, long frame avoided) | `cobalt.radar.evaluate.EvaluateError: AttributeError: 'MemberEvaluation' obj…` |
| convention row | `KeyError: 'anatomy.orientation.extension'` |
| closure names the row key | `AssertionError: assert ('A-01',) == ('anatomy.ori...n.extension',)` |
| ruled / unimplemented label / X8 source half | `ImportError: cannot import name 'CONVENTION_LABELS' …` / `KeyError: 'anatomy.orientation.extension'` |
| closure with an assumed cfg / detector key | `AttributeError: type object 'TunableSource' has no attribute 'ASSUMED'` |
| `TunableSource.ASSUMED` | `ValueError: 'assumed' is not a valid TunableSource` |
| reader | `ImportError: cannot import name 'load_assumed_tunables' …` · `ImportError: cannot import name 'assumed_note_text' from 'cobalt.taxonomy.cli'` |
| X19 fill | `ValidationError: 1 validation error for TunableRow` (source `assumed`) · `TaxonomyConfigError: user tunable row(s) ['range.wic…` (a ruling row cannot fill) |
| dry-run | `ImportError: cannot import name 'assumed_report' from 'cobalt.taxonomy.cli'` |
| 0013 registered | `AssertionError: assert (PosixPath('…/0013_tunables_slug_nullable.sql') in FORWARD` |

GREEN on the start code by design: the six Lego (ii) pins (below), X4 (the cent-grid sweep: 0 inequalities — see X), X25 and X12 on today's short card, `a detector reads only its own TUNABLE_KEYS`, and the loud-collision rows of X19 that hold today (a `sheet` / `dwv` user row, a strategy-note row on an engine key). With-DB (writer, X23, migration) skipped offline; run under SUITE.

**Lego (ii) byte-identity PINS, captured on the START-of-step code** (sha256 over every `MemberEvaluation.model_dump(mode="json")` on FTFT + BGFI, two-minute scans, and over every card the stage makes on the FTFT formed scans), excluding ONLY: on `MemberEvaluation` `by_side`; on `Formation` `side_frame`, `anchor`, `trigger_outcome`, `stop_outcome` (the fields this step adds); on the card `formula_sha256` (new formula bytes by construction) and the `assumed_formation` dot's `engine_inputs` / `engine_why` (R2-2.2 B: the closure replaces STEP-1's constant — the dot now names the convention ROW key): countertrend `fd2f49725ecd80817bfacd857fc349817b7c75a462992c1a0c567e3932b78ad8` · full `7d868974df741d145c01ced9ce498532b2545f7d061ad4ed7a1c33a5cdd2a44f` · mixed `a8b8f0989a987cab67f30d2754d323e23d982f6e845876269df029831471d024` · shipped `da0f0ef1aa0179ea2b07adf9f6ac4d64eec24dd705152b7e8eee4a2326877be7` (= STEP-1's T6 pin) · cards countertrend `7a0e5796e33ebbd01e68c6b7c66c6946c0a0419258f6adc3bf81f8811573450a` · cards mixed `5c4dcce2c86b4ffb5526c25274b26578dcf24509c8ce119d0c8dde0629d9a3a7`.

**The A-01 convention's row key** is the companion's key NAME for it, `anatomy.orientation.extension` (a key name is anatomy, FINAL §8; its value in committed config is `null`). `ASSUMED_CONVENTIONS` and the dot name that row key; `A-01` stays the design's label in comments and DevDocs.

### C

| file | change |
|---|---|
| `src/cobalt/radar/formation/__init__.py` (new) | the package: the five tables, keyed by the def's own data |
| `src/cobalt/radar/formation/triggers.py` (new) | `TriggerOutcome {state, price, ref_bar_ts, kind, inputs, why, level}` + `.unmirrored(side)`; `TRIGGERS = {bar_break: BarBreak}` (`serves({bars_cleared})`, `structure.bar_break_trigger` re-registered); `trigger_resolver` |
| `src/cobalt/radar/formation/stops.py` (new) | `StopOutcome {price, placement, ref, inputs, why, structural, extreme}` + `.unmirrored`; `STRUCTURAL_REFS = {snapback_candle, turn_low: tracked extreme}`; `STOPS = {structural_extreme}`; `stop_resolver` |
| `src/cobalt/radar/formation/atoms.py` (new) | `AtomValue` (moved from `evaluate.py`); `ATOMS` (the four served atoms: value kind, producible domain, price flag, `tunable_keys`, conventions); `RELATIONS = {}`; `predicate_gaps` — the ONE shape walk |
| `src/cobalt/radar/anatomy/frame.py` (new) | `mirror_bars`, `mirror_daily`, `Frame`, `build_frame` (detectors run inside the frame; Extension + HTF atoms moved here) |
| `src/cobalt/radar/anatomy/registry.py` | its three constants DELETED; `evaluability` reads the tables + `predicate_gaps` (E8 `∌`, E9 `Unsupported(<kind>)`) |
| `src/cobalt/radar/evaluate.py` | one Frame per side; `on_side` evaluates the long-side text per frame; trigger / stop via the registries, un-mirrored into `Formation`; A-01 in frame terms; `publish_frames` (R2-4.1 B, `by_side`); the stage reads `by_side[card.direction]` for the avoid that expires a card; `Formation` + `side_frame`, `anchor`, `trigger_outcome`, `stop_outcome`; `SideOutcome`; `ASSUMED_CONVENTIONS` = the row key; `CONVENTION_LABELS`; `convention_refusals`; `closure_keys` / `assumed_closure` (R2-2.2 B); `FORMULA_FILES` + `formation/*.py`; two needless `dict(tunables)` copies in the cfg path removed (X22's instrumentation needs the reads) |
| `src/cobalt/taxonomy/tunables.py` | `TunableSource.ASSUMED` |
| `src/cobalt/taxonomy/loader.py` | `merge_tunables` hole-fill `_fills_hole` (B's R2-3.2, the four clauses) |
| `src/cobalt/taxonomy/vault_loader.py` | `ASSUMED_NOTE` / `ASSUMED_SECTION` / `ASSUMED_UNIT`; `LoadedTunable.slug` optional; `load_assumed_tunables` (global / per_trade of a loaded def; per_indicator REFUSED — F1 not widened; source assumed / ruling); appended in `load_vault_trade_defs`; duplicate suppliers refused; the strategy-note reader refuses `source: assumed` |
| `src/cobalt/taxonomy/cli.py` | `assumed_note_text`, `write_assumed` (existing `VaultWriter`: `create_if_absent` + `upsert_unit`), `cmd_assumed_write`, `assumed_report` / `cmd_tunables_assumed`; subcommands `assumed write --from … --dry-run\|--apply` and `tunables --assumed` |
| `src/cobalt/db_migrations/0013_tunables_slug_nullable.sql` + `.rollback.sql` (new), `db_migrations/__init__.py` | the migration pair registered in `FORWARD` / `REVERSE` |
| `configs/cobalt/taxonomy/tunables.yaml` | ONE added row, `anatomy.orientation.extension` (unit `label`, `value: null`, `status: proposed`, `dynamic: false`, consumer = the side-binding line) |

`taxonomy/store.py` needs no code change (a `None` slug passes through). `seam.py` untouched (R2-4 = B adds no seam field). Not touched: `vaultwrite/`, `cards/`, `aset/`, `taxonomy/migrations/`.

### A1

| test | old assertion | new assertion | FINAL tag |
|---|---|---|---|
| `test_radar_anatomy.py` import + `test_supported_atoms_are_exactly_the_s2_detectors` | `registry.SUPPORTED_ATOMS == frozenset({4 atoms})` | `frozenset(formation.atoms.ATOMS) == frozenset({the same 4 atoms})`; the other use reads the same table | §2.5 (constants deleted) |
| `test_rubberband_forms.py::test_t3_…` | monkeypatch `evaluate.structural_stop`; published note `stop_wrong_side` | patch `formation.stops.structural_stop` (frame coordinates: `+1.00`); `by_side["short"].note == "stop_wrong_side"`, published `not_formed`, no formation, no card | §2.3, R2-4.1 B |
| `test_rubberband_forms.py` T5 (a) offline + with-DB, T5 (c)(5) | `assumed_keys == ["A-01"]`, `"A-01" in engine_why` | `== ["anatomy.orientation.extension"]`, that key in `engine_why` | R2-2.2 B (the closure replaces the constant) |
| `test_rubberband_forms.py` T6 formed-def pins | exclusions `{setup_ref, assumed_keys}`; card `tunables_sha256` as is | + STEP-2's added Formation fields; `tunables_sha256` asserted = snapshot WITH the convention row and mapped to the snapshot WITHOUT it (the pin's start value) | §2.4, R2-2.2 B |
| `test_rubberband_forms.py` T6 non-formed pins | raw dumps | minus `by_side` and minus E9's `Unsupported(<kind>)` (+ its seam marker) — `without_e9_shapes` | R2-4.1 B, §2.5 E9 |
| `test_setups_registries.py` Lego (ii) pins (this step's own T) | formation `assumed_keys` as dumped | `anatomy.orientation.extension` mapped back to `A-01`; the card's `tunables_sha256` mapped as above; E9 names stripped — exactly the three by-design changes, everything else byte-identical | R2-2.2 B, §2.5 |
| `test_replay_formations.py::test_the_days_second_formation_is_refused_by_the_geometry_guard` (STEP-1's) | published `("not_formed", "stop_wrong_side", None)` | `by_side["short"]` carries `stop_wrong_side`; published `not_formed`, formation None | R2-4.1 B |
| `test_archiver_migrations.py` ×4, `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py` | tails / heads end at `0011`; `1…11 contiguous` | the exact lists with `0013_tunables_slug_nullable` added (heads `[:4]` → `[:5]`, `FORWARD[-4:]` → `[-5:]`); `numbers == [1…11, 13]` exactly | R2-3 = B (migration); L68 seam with `bars/chunk-2-0920` |

DEFECTS of the change, fixed in the CODE / own test, not re-pointed: `test_tenancy.py::test_no_unquoted_user_schema_reference_in_python` flagged `user.` in `loader._fills_hole` → parameter renamed `supplied`; `tests/taxonomy/test_names_rule.py` flagged my test's non-`example_` per-trade key → `example_not_loaded`; `setups_shapes.every_scan` cached by md5 alone, and two neutral notes with the same YAML body share one (the slug is frontmatter) → cache key `(slug, md5, ticker)`; the F-04 test compared `None` extension prices and read incomplete trigger windows → guarded. No assertion removed, no skip / xfail added.

### X

- **X20 — violation + rollback** (above) → R2-3 = B WITH migration 0013.
- **X19 — PASS** (the built predicate's truth table, one test per clause, + the two holes: a per-trade row never fills a global key; a strategy-note row never fills an engine key; duplicates refused).
- **X23 — PASS on `tmp_path`**: after the owner-style hand edit of one row's `source`, a second write changing two other values produced exactly this diff (verbatim, paths elided): `-  value: 0.5` / `+  value: 0.55` … `-  value: 1` / `+  value: 2`; the hand-edited `source: ruling` line survived; the second write landed. → one marker unit for all rows works. The real dev vault: **UNPROVEN (dev vault) — no command string; the desk proves the writer there before the production write (L28 "writers off until proven on the dev vault with a diff")**.
- **Writer proof (L28)**: `created` then `updated`; diff 1 = the whole template (`+# Assumed defaults` … `+<!-- /cobalt:section assumed -->`), diff 2 = the unit body `-tunables: []` → `+tunables:` / `+- key: range.wick_ratio_max` …; `vault_writes` rows inside the rollback transaction.
- **X22 — PASS**: instrumented reads ⊆ declared closure on every sampled scan, both frames — mixed / countertrend reads `anatomy.orientation.extension`, the three `extension.*` keys, `range.wick_ratio_max` (the closure's own read of the def's `radar_watch` cfg), `stop.buffer`; full shape reads the four without `stop.buffer`; declared = those six.
- **X8 (`source` half) — PASS offline and with-DB** (see SUITE): after the convention row reads `ruling`, the open card keeps the dot, null score, suppression; a new formation carries `assumed_keys == ()`.
- **X21 — PASS**: selection deterministic; replay of the receipt reproduces `by_side` exactly.
- **X25 — PASS**: the board row, the dry-run replay and the card read `short` from a mirrored-frame formation. `grep -rn "\.direction\b\|\[\"direction\"\]\|'direction'"` over `radar/store.py`, `radar/audit_export.py`, `radar/evaluate_cli.py`, `aset/radar_panel.py`, `replay/formations.py`: `radar/store.py:408` writes the published row's `direction`; the panel reads the CARD's direction (`radar_panel.py:743`, `:746`, `:1001`); the nightly binding reads the `ReplayFormation.direction` (`formations.py:159` …). None assumes the long side.
- **X18 — offline PASS**: `X18: scans=175 differences={'atrs_from_open': 0, 'Extension.leg_count': 0, 'htf_level_proximity': 0}` → computing them once on the real bars (B's R2-4.2) is consistent. Stored-day half: see `## EXPERIMENTS` (X2 first).
- **X12 — PASS**: the mirrored-frame card's trigger, stop, raw, rounded, extreme are positive; directions `short`; extreme side `high`; `why` names `short` only; no negative atom number.
- **X4 — PASS**: `_on_ten_cent_grid(Decimal('-10.00'))` True, `(-10.04)` False; the `structural_stop` sweep over 4.80–6.20 (whole and half cents) × buffers 0.01 / 0.02 / 0.05 × both sides: 0 inequalities.
- **X6 — `X6: a negative-price archiver Bar constructs`** → nothing would stop a round trip, so the Frame wraps `WorkingBar` only (asserted).
- **X7 (offline) — 0 `both_sides`** on 392 scans for each of mixed / countertrend / full.
- **X5 (offline) — PASS**: `X5 offline: defs=3 frames=2 members=50 runs_s=[0.65, 0.64, 0.68] p95~max=0.68s budget=100.0s` (the stored-day run is at the deploy).
- **Frame property F-04 — PASS** on every scan of the committed day (Extension predicates, prices, tracked extreme, `bar_break` both ways, the stop); R2F-12 — the mirrored daily series gives the same HTF day count.

- **Stored-session experiments** (`tests/experiments/setups_one/`, with-DB, counts only; a `conftest.py` inside the folder re-exports `tests/cobalt/conftest.py`'s fixtures — no `tests/experiments/__init__.py`, an L68 seam with `bars/chunk-e-0920`):
  - **X2** — `X2: stored i1 sessions=11 names=60 rows=451362 names-per-session min=60 max=60` → the stored-session experiments CAN run.
  - **X7 stored — PASS**: `X7 stored: sessions=10 grid=30min {'rubberband': {'scans': 7200, 'both_sides': 0, 'formed': 0}, 'rubberband-without-htf-avoid': {'scans': 7200, 'both_sides': 0, 'formed': 104}}` — the full shape forms 0 because its day-1 HTF avoid is UNKNOWN without the daily series (the daily leg is UNPROVEN in the worktree).
  - **X18 stored — PASS for two of three**: `X18 stored: sessions=10 {'scans': 7200, 'atrs_from_open_diff': 0, 'leg_count_diff': 0} htf_level_proximity=UNPROVEN (daily leg)` — runs at the deploy from `~/cobalt`.

### D

New: `radar/formation/__init__.md`, `formation/triggers.md`, `formation/stops.md`, `formation/atoms.md`, `radar/anatomy/frame.md`. Appended (one dated paragraph each): `radar/anatomy/registry.md`, `radar/evaluate.md` (the Frame, R2-4 = B with the row's letter, the closure; the ONE bump covers it), `taxonomy/tunables.md`, `taxonomy/loader.md` (hole-fill, R2-3 = B, X20's line), `taxonomy/vault_loader.md` (the reader; "an absent note = no assumed rows"), `taxonomy/store.md` + `db_migrations/__init__.md` (0013 and its rollback), `taxonomy/cli.md` (the writer and the dry-run).

### SUITE

- `uv run pytest -q tests/cobalt tests/taxonomy` (background) → `2302 passed, 361 skipped, 1 xfailed, 15 warnings in 166.93s (0:02:46)` — 0 failed. Against STEP-1 (2251 / 356): +51 passed = this step's new offline tests (`test_setups_registries.py`, `test_assumed_store.py`, `test_setups_x5.py`); +5 skipped = its new with-DB tests (skipped offline).
- cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_registries.py tests/cobalt/test_assumed_store.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_replay_formations.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_p4_migrations.py tests/cobalt/test_radar_migration.py tests/cobalt/test_tenancy.py tests/experiments/setups_one -s -q` (the printed X-lines above come from this run) → rm → `ls` "No such file"; then the same set without `-s` → **`299 passed in 586.47s (0:09:46)`** (it includes the stored-session experiment module) → rm → `ls -la .env` → `ls: .env: No such file or directory`.

### COMMIT

Three commits (two `wip` checkpoints across the API 529 interruption, then the step commit): `a94fd17` (X20 + migration 0013), `61a283f` (assumed store, registries, frame, publication, closure), `c74436c feat(setups): STEP-2 registries, mirrored frame, interpreter shapes, assumed store — R2-3 B by X20, R2-4 B per row (FINAL C2)` — `git show --stat HEAD` for `c74436c`: 30 files, 618 insertions(+), 30 deletions(-); every path one named above.

## STEP-3

C3a: D1 shared indicators, session levels and the premarket warm-up (FINAL §3 D1, §5; [F-10], [F-11], [F-14 · X11]).

### X (before C)

- **X1**: `tests/experiments/setups_one/test_x1_premarket_seed.py`, with-DB, counts only.
  - Commands: cp → `COBALT_ENV=dev uv run pytest -q tests/experiments/setups_one/test_x1_premarket_seed.py -s` → rm → `ls -la .env` → `ls: .env: No such file or directory`.
  - VERBATIM: `X1 pool: sessions=10 pool_sessions=0 name_sessions=0 working_tf=2m share_by_period={9: None, 14: None, 21: None}` · `X1 stored: sessions=10 pool_sessions=0 name_sessions=600 working_tf=2m share_by_period={9: 0.813, 14: 0.743, 21: 0.65}`.
  - Reading: `cobalt_dev` holds no `radar_membership` rows for its 10 stored sessions, so the POOL share is UNPROVEN in this worktree and runs at the deploy. Over every stored name, 81% / 74% / 65% of name-sessions have ≥9 / ≥14 / ≥21 complete premarket 2m buckets by 09:30. The seed applies to most names. Per Grok ("do not drop the seed, report the rate"), the rate is reported and the seed is kept.
- **X11**: run on the START code (scratch probe, not committed). An `AtomOutcome` was constructed for every planned D1 atom × declared reason.
  - Every atom spelling passed `validate_atom`.
  - Failures, verbatim: `X11 FAIL EMA9 insufficient_seed 1 validation error for AtomOutcome | unavailable` (the same line for EMA21, EMA9.slope, slope_norm(EMA9), slope_norm(VWAP), ATR(working_tf)) and `X11 FAIL EMA9.slope slope_norm.bars_unset …` (the same for both `slope_norm(...)`).
  - → the closed reason list changes inside the step, named: `seam.UnavailableReason` gains `insufficient_seed` and `slope_norm.bars_unset`. No atom spelling changes.

### T (RED)

New: `tests/cobalt/test_setups_d1.py`. The [F-10] and [F-11] sentences are tests, with golden pins captured on the START code (`c74436c`): four evaluation pins (countertrend, full, mixed, shipped), two card pins (dots + card_score over a day of stage scans) and the X14 FILLED-card pins. It also holds each detector on constructed series and on the committed day, the ATOMS rows, the new tunable rows, the F-04 property for the new atoms, the closure, X22 for the laziness, and X11.

Run on the start code: `20 failed, 8 passed`. The 8 PASS by design: the 6 pins, X14 and X22. RED lines, one per kind:

| test | RED |
|---|---|
| seeded ATR / EMA, seed rule | `ImportError: cannot import name 'premarket_buckets' from 'cobalt.radar.anatomy.frame'` · `ImportError: cannot import name 'seeded' from 'cobalt.radar.anatomy.indicators'` |
| detectors | `ModuleNotFoundError: No module named 'cobalt.radar.anatomy.session_levels'` (`.slope`, `.in_play` likewise) |
| ATOMS rows | `ImportError: cannot import name 'slope' from 'cobalt.radar.anatomy'` |
| tunable rows | `KeyError: 'slope_norm.bars'` |
| frames / F-04 / unset key / InPlay departed | `ImportError: cannot import name 'member_frames' from 'cobalt.radar.evaluate'` |
| a D1 def evaluable | `AssertionError: assert False` |
| closure | `AssertionError: assert {'dayrange.se...pe_norm.bars'} <= frozenset({…})` |
| X11 | `AttributeError: 'AtomResolver' object has no attribute 'reasons'` |

The own-test defects found in this run were fixed in the test, not in code:
- `test_f10_atr_working…` bounded `checked > 150`, but the day has 107 scans with an RTH-run ATR → `> 100`.
- After C, X11 asserted that every atom declares a reason; `InPlay.state` is always known → exempted by name.

### C

| file | change |
|---|---|
| `src/cobalt/radar/anatomy/indicators.py` | `Seeded`, `seeded(fn, premarket, run, period)` (the ONE warm-up rule over `ema` / `wilder_atr` — [F-10] "one function, two named inputs"), `WARMUP_CONVENTION` |
| `src/cobalt/radar/anatomy/session_levels.py` (new) | `day_range` (+ `upper_third`, `A-06`), `vwap` (RTH-anchored typical price on i1, `A-12`), `premarket_levels`, `prior_day_levels` (via `daily.prior_session`) |
| `src/cobalt/radar/anatomy/slope.py` (new) | `slope`, `slope_norm` (zero ATR → unknown), `slope_bars` (`A-11`, null → `_unset`), `flat`, `flat_threshold` (`A-09` / `A-10`, per_indicator — F1 not widened) |
| `src/cobalt/radar/anatomy/in_play.py` (new) | `in_play_state`, domain `{active, departed}` |
| `src/cobalt/radar/anatomy/frame.py` | `premarket_buckets`, `minute_bars`, `SessionInputs`, `LazyAtoms`; `Frame.premarket` / `.warm` / `.number`; the D1 resolvers (lazy, mirrored with the frame) |
| `src/cobalt/radar/formation/atoms.py` | 16 D1 rows; `AtomResolver.reasons` (the existing four rows declare theirs) |
| `src/cobalt/radar/evaluate.py` | `_closed_i1`, `_daily_ok`, `_build_frames` (one builder), `member_frames`; `ema9` = the seeded EMA9; seam observation `atr_seeded`; `CONVENTION_LABELS` for the three conventions |
| `src/cobalt/radar/seam.py` | `UnavailableReason` + `insufficient_seed`, `slope_norm.bars_unset` (X11) |
| `configs/cobalt/taxonomy/tunables.yaml` | `slope_norm.bars` (engine row, unit `bars`, null, proposed, global); `frame.warmup_source`, `dayrange.session`, `vwap.anchor` (label rows, null) |

`flat(x, window)` is built as a detector but is not yet an atom. Its window argument and `between` are STEP-5's (prompt STEP-5 files). `EVALUATOR_VERSION` is unchanged: STEP-1's one bump covers it (R44).

### A1

| test | old assertion | new assertion | FINAL tag |
|---|---|---|---|
| `test_radar_anatomy.py::test_unsupported_atoms_trigger_and_stop_are_named_missing` | missing ∋ `VWAP` | the same set minus `VWAP` (now served) | §3 D1 |
| `test_radar_anatomy.py::test_supported_atoms_are_exactly_the_s2_detectors` | the four S2 atoms | the four + the 16 D1 atoms, exactly | §3 D1 |
| `test_setups_registries.py` Lego (ii) evaluation pins ×4 | STEP-2 normalisation | + STEP-3's exact normalisation: `ema9` restored to its RTH-only value, the `atr_seeded` observation dropped, and the served D1 atoms re-added to a not-evaluable def's `missing` | [F-10], [F-11], §3 D1 |
| `test_setups_registries.py` Lego (ii) card pins ×2, `test_rubberband_forms.py` T6 formed card | `tunables_sha256` mapped without the A-01 row | mapped without it AND the four STEP-3 rows | §3 D1 / §5 (new rows) |
| `test_rubberband_forms.py` T6 non-formed pins | STEP-2 normalisation | + the same STEP-3 normalisation | [F-10], [F-11] |

No assertion was removed, and no skip or xfail was added.

### X (on the changed code)

- **X14: PASS.** `X14: filled-card refreshes=138 non-health numbers moved=False health moved=True`. Only `health` moves, so the F-10 deploy note stands.
- **X11: PASS.** `X11: atoms=20 failures=[]`.
- **[F-11] pins: PASS.** The four evaluation pins and the two card pins are byte-identical under the named exclusions (`ema9`, `atr_seeded`, and the shipped def's newly served `DayRange.upper_third`).
- **X22 (laziness): PASS.** A Rubberband def reads none of `slope_norm.bars`, the three conventions or the flat thresholds.
- **F-04 for the D1 atoms: PASS** on the committed day.

### D

- New: `radar/anatomy/session_levels.md`, `slope.md`, `in_play.md`.
- Appended: `radar/anatomy/indicators.md` (seeding), `frame.md` (warm series, lazy D1 atoms), `radar/formation/atoms.md` (the rows, `reasons`), `radar/seam.md` (X11's two reasons), `radar/evaluate.md`. The last one states: "`health` of open cards moves (EMA9 seeded); the ONE `EVALUATOR_VERSION` bump of STEP-1 covers it — nothing deploys between steps (R44)".
- SLIP, recorded: my first attempt at the `indicators.md` append was a Bash `printf … >>` (a redirect the prompt forbids). It sat on a permission dialog and the CTO desk cancelled it with Esc. Nothing was written. It was re-done with the Edit tool per the desk's message. From here, file content goes only through Write / Edit.

### SUITE

- `uv run pytest -q tests/cobalt tests/taxonomy` (background) → `2330 passed, 361 skipped, 1 xfailed, 15 warnings in 293.88s (0:04:53)`, 0 failed. Against STEP-2 (2302 / 361), the +28 passed are exactly `test_setups_d1.py`'s 28 tests. The first full run found the 9 A1 rows above; they were re-pointed, then rerun green.
- **X5 re-run: PASS.** `X5 offline: defs=3 frames=2 members=50 runs_s=[1.31, 1.3, 1.31] p95~max=1.31s budget=100.0s`. At STEP-2 it was 0.68 s; the increase is the per-member one-minute bar split. No new def this step, so the def count is unchanged.
- cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_registries.py tests/cobalt/test_setups_d1.py tests/cobalt/test_assumed_store.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_replay_formations.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_p4_migrations.py tests/cobalt/test_radar_migration.py tests/cobalt/test_tenancy.py tests/experiments/setups_one` → **`328 passed in 783.36s (0:13:03)`** (= 299 + 28 + X1) → rm → `ls -la .env` → `ls: .env: No such file or directory`.

### COMMIT

`9c286e9 feat(setups): STEP-3 shared indicators, session levels, premarket warm-up (FINAL C3a)`. `git show --stat HEAD`: 23 files, 1507 insertions(+), 54 deletions(-); every path is one named above.

## STEP-4

C3b: D2 Range(micro) + pivots, D3 opening-drive roles, `range_break`, `consolidation_low` → the drive-then-range setup (hitchhiker) (FINAL §3 D2/D3, §2.2, §2.3, §4 row 1; [F-12]).

### T (RED)

New: `tests/cobalt/test_setups_hitchhiker.py`. It holds X16 as a `leg.py` byte pin computed in the test with `hashlib`, pivots, Range(micro) on definition-written constructed series (drive then range, megaphone, unset keys / seed / incomplete bucket), the opening drive under A-07 and under the literal reading, the atoms / rows / trigger / stop, the `IN cfg(band) min` shape and a unit mismatch, and the per-setup acceptance: `test_hitchhiker_path_*` on a definition-written day and its mirror, committed defaults, X7, the geometry guard and X11. The corpus gains the neutral `shape-drive-then-range` note in `setups_shapes.SHAPES` (`hitchhiker`), with its own per-trade band row and this build's constructed fills for the step's null engine holes (`D2_CONSTRUCTED`, L69).

Run on the START code (`9c286e9`, `-rA`): 18 FAILED in the new module plus `test_setups_lego.py::test_every_unlocked_setup_shape_is_evaluable`; PASSED by design: X7 and the geometry guard (nothing forms yet), and the lego property (the unevaluable shape is skipped). RED lines, one per kind:

| test | RED |
|---|---|
| X16 pin | `AssertionError: assert '2f3b3abc2b9e...4df43cb7782c8' == 'PIN'` → the start digest `2f3b3abc2b9e9b634d4a5d050c352ade8853f5a9221be7cee5f4df43cb7782c8` pasted, now a GUARD |
| pivots / micro-range / roles | `ModuleNotFoundError: No module named 'cobalt.radar.anatomy.pivots'` (`.micro_range`, `.leg_roles` likewise) |
| atoms | `ImportError: cannot import name 'leg_roles' from 'cobalt.radar.anatomy'` |
| rows | `KeyError: 'range.micro.touch_tolerance_atr'` |
| trigger / stop | `KeyError: <TriggerType.RANGE_BREAK: 'range_break'>` |
| `IN cfg(band) min` | `AssertionError: assert False` · `AssertionError: assert 'Unsupported(unit:min)' in ('Range(micro).height', '...` |
| shape evaluable / forms / lego (4) | `AssertionError: ('Leg(opening_drive).terminated_by', 'Range(micro).duration', 'Range(micro).instantiated', 'Range(micro).low', 'Range(micro).wick_ratio', 'Unsupported(in)', ...)` |

One own-test defect, fixed in the test before C: the first megaphone test proved "no Range" through a touch failure, not through the divergence rule. It now has two touches per side, and a second assertion shows that a wider flat limit makes the same bars a Range.

### X (before C: the pure detectors built, not yet wired into the stage)

Order, stated: the three pure detector modules were written first and their 8 unit tests went green. X13 and X15 then ran on them BEFORE any stage, registry, trigger, stop or interpreter change (`tests/experiments/setups_one/test_x13_x15_drive.py`, with-DB, counts only). Commands: cp → `COBALT_ENV=dev uv run pytest -q tests/experiments/setups_one/test_x13_x15_drive.py -s -p no:cacheprovider` → rm → `ls -la .env` → `ls: .env: No such file or directory`.

- **X13**, VERBATIM: `X13: name_sessions=600 median(atr_seeded/rth_tr_mean, n)={'09:40': (0.532, 446), '09:50': (0.687, 446), '10:00': (0.788, 600)} median(atr_seeded/rth_atr14, n)={'09:40': (None, 0), '09:50': (None, 0), '10:00': (0.79, 600)} open_drive_ranges_by_10:00={'seeded': 190, 'rth_tr_mean': 231}`.
  - RTH-only ATR(14) has no value at 09:40 / 09:50 (E7: n = 0). The RTH-weighted comparison is the mean true range of the RTH bars there are.
  - The median ratio is **well under 1** (0.53 → 0.79). With the seeded ATR, 190 name-sessions have a micro-Range by 10:00 inside `open_drive`; with the RTH-weighted one, 231.
  - → the FINAL's line fires: "early ATR-scaled tolerances need an RTH-weighted ATR, and `A-05` changes for ATR while staying for the EMAs" → **ESCALATE 9. No key changes.** The detector reads the frame's seeded `ATR(working_tf)` as built.
- **X15** (detector level, both frames, constructed params, band 5–30 min; pool admission not read), VERBATIM: `X15 (detector level, both frames): {'name_sessions': 600, 'drive_then_range': 241, 'forms_a07': 36, 'forms_literal': 5}`.
  - → "The literal reading forms → `A-07` is not needed as worded": it forms, on 5 name-sessions against 36 under A-07 → **ESCALATE 10.** `A-07` is kept as the FINAL words it.

The pure detectors and the experiment were committed as a wip checkpoint (`6b0172e`, RECOVERY RULE) before the wiring.

### C

| file | change |
|---|---|
| `src/cobalt/radar/anatomy/pivots.py` (new) | `pivots(bars, n)` (strict, `n` each side), `pivot_n`; `TUNABLE_KEYS = ("pivot.n",)` |
| `src/cobalt/radar/anatomy/micro_range.py` (new) | `detect_micro_range` (the longest non-diverging window with ≥ k touches per bound; `bound_type`, `duration`, `height`, `wick_ratio`, `instantiated_ts`, `base_bar_ts`), `range_params` (null → `<key>_unset`); `A-03`, `A-04` |
| `src/cobalt/radar/anatomy/leg_roles.py` (new) | `opening_drive` (`A-07`, Gemini's wording [F-12]), `opening_drive_literal` (X15 only), `max_retrace` |
| `src/cobalt/radar/anatomy/frame.py` | the D2 / D3 lazy atoms; `Frame.objects` (`Range(micro)`, `Leg(opening_drive)`) |
| `src/cobalt/radar/formation/atoms.py` | 10 rows; `AtomResolver.unit`; `predicate_gaps` accepts `IN cfg(band) <unit>`; `unit_mismatch` |
| `src/cobalt/radar/formation/anchors.py` (new) | `ANCHORS` (`Extension`, `Range(micro)`), `anchor_for` (FINAL §2.4) |
| `src/cobalt/radar/formation/triggers.py` | `RangeBreak {ref: Range(micro).bound \| .top}` |
| `src/cobalt/radar/formation/stops.py` | `STRUCTURAL_REFS` + `consolidation_low`, `range_base` (= `Range.base`) |
| `src/cobalt/radar/evaluate.py` | the anchor in `on_side` (the Extension branch byte-identical); `_in_band` + `evaluate_node(units=)`; an interpreter `Unsupported` reaches the seam through `seam_safe_missing_atoms`; `card_why` assembled from the resolvers' `why` for a non-Extension anchor |
| `src/cobalt/radar/seam.py` | `UnavailableReason` + the four D2 / D3 `_unset` reasons (X11) |
| `configs/cobalt/taxonomy/tunables.yaml` | `range.micro.touch_tolerance_atr` (`A-03`, atr), `range.micro.bound_flat_slope_atr` (`A-04`, atr), `leg.consolidation_max_retrace` (`A-07`, ratio): engine rows, null, proposed, global |

Not changed: `leg.py` (X16 pin GREEN on the tip); `registry.py` (it reads the tables); the card, replay, audit and CLI readers, because `Formation.trigger` stays a `TriggerLevel`.

A DEFECT of my change, found while wiring and fixed in the CODE: an absent band row would have read as a unit mismatch. It now fails loud in `cfg()`.

### A1

| test | old assertion | new assertion | FINAL tag |
|---|---|---|---|
| `test_radar_anatomy.py::test_unsupported_atoms_trigger_and_stop_are_named_missing` | missing = {`Range(micro).instantiated`, `Leg(pullback)`, `touched`, `trigger:range_break`, `stop:structural_extreme:range_base`} | = {`Leg(pullback)`, `touched`} exactly | §3 D2, §2.2, §2.3 |
| `test_radar_anatomy.py::test_supported_atoms_are_exactly_the_s2_detectors` | the STEP-3 set | + the 10 D2 / D3 atoms, exactly | §3 D2, D3 |
| `test_radar_evaluate.py::test_def_without_evaluable_precondition_renders_not_evaluable_never_a_card` | `Range(micro).instantiated` ∈ missing; `Trigger(range_break)` ∈ seam missing | missing == (`Extension(day).state`,) exactly; it is in the seam's missing | §3 D2, §2.2, §2.3 |
| `test_radar_evaluate_cli.py::test_replay_filters_to_one_trade_def_and_names_not_evaluable_defs` | `Range(micro).instantiated` ∈ the def's not-evaluable list | `Extension(day).state` ∈ it | §3 D2 |
| shipped-def pins: `test_setups_d1.py` [F-11] (shipped), `test_setups_registries.py` Lego (ii) (shipped), `test_rubberband_forms.py` T6 non-formed | STEP-3's re-add of the served D1 atoms | the ONE shared normaliser `_served_later(ld)`, derived from the def itself: its named atoms served now, `trigger:range_break`, `stop:structural_extreme:range_base`, and `Unsupported(in)` for its band precondition, re-added; the seam list is recomputed by `seam_safe_missing_atoms` | §3 D2, §2.2, §2.3, §4 row 1 |
| card pins: [F-11] dots / card_score ×2, Lego (ii) cards ×2, T6 formed card | `tunables_sha256` mapped without the STEP-3 rows | … and without STEP-4's three rows | §3 D2 / D3 (new rows) |
| `test_setups_x5.py` (this build's own) | the stage merged engine rows only | + the corpus's constructed fills and each note's per-trade rows, so the range detector runs rather than stopping at `_unset` | X5 ("the def count grown") |
| `tests/experiments/setups_one/test_x7_x18_stored.py` (this build's own) | every shape on the engine rows | each shape on its own merged rows (Rubberband's are the engine's, unchanged) | X7 for the new def |

Own-test defect: `tests/taxonomy/test_names_rule.py` refused my note's per-trade key (`shape_drive_then_range.…`, L31 / ADR-0008 D5). The note slug became `example-drive-then-range`, and its key is `example_drive_then_range.range_duration_band`. No assertion was removed, and no skip or xfail was added.

### X (on the changed code)

- **Per-setup acceptance, hitchhiker (FINAL §9 gates 1–5, [F-16] (1)–(5)):**
  - (1) The shape forms on NO scan of the committed day (FTFT, BGFI), with constructed config. FTFT: on 22 scans the drive reads `consolidation`, and on 68 a micro-Range instantiates, but the band and upper-third preconditions never hold with them (a False, never an unknown). BGFI is stale by design. → `hitchhiker` joins `AWAITING_A_DAY`. Its path forms on the definition-written day (`test_hitchhiker_path_forms_long_on_the_definition_written_day`: long, formed bar 09:46 ET, trigger 11.00 = the top, stop = `structural_stop(10.85, long, 0.02)`, anchor `Range(micro)`) and on its mirror (short, trigger 9.00, `mirrored`).
  - (2) The property holds with `AWAITING_A_DAY == {rubberband, hitchhiker}`.
  - (3) The live-note test: `NOT RUN (skipped by design; the deploy runs it and a SKIP is RED — [F-16] (2))`.
  - (4) The corpus shape is evaluable: `test_every_unlocked_setup_shape_is_evaluable` GREEN, with the text avoid human (L11).
  - (5) The geometry guard holds for every formation (the definition-written ones; none on the committed day).
  - At committed defaults the shape stays unknown, with `_unset` in the note (never a guess).
- **X7 hitchhiker offline:** `X7 hitchhiker: scans=392 formed=0 both_sides=0` → PASS (vacuous on this day: nothing forms). Stored half: see SUITE.
- **X11 hitchhiker:** `X11 hitchhiker: atoms=7 failures=[]` → PASS. The build-wide X11 over every served atom is also GREEN.
- **X16:** `X16: leg.py sha256=2f3b3abc2b9e9b634d4a5d050c352ade8853f5a9221be7cee5f4df43cb7782c8` equals the START pin → PASS. `Extension.leg_count` is unchanged: every Rubberband pin (STEP-1 T6, Lego (ii), [F-11]) is GREEN.
- **X5:** `X5 offline: defs=4 frames=2 members=50 runs_s=[1.79, 1.77, 1.78] p95~max=1.79s budget=100.0s` → PASS.

### D

- New: `radar/anatomy/pivots.md`, `micro_range.md`, `leg_roles.md`, `radar/formation/anchors.md`.
- Appended: `radar/anatomy/frame.md`, `radar/formation/atoms.md`, `triggers.md`, `stops.md`, `radar/evaluate.md`, `radar/seam.md`.

### SUITE

- **Offline.** `uv run pytest -q tests/cobalt tests/taxonomy` (background).
  - The first run: `13 failed, 2338 passed, 361 skipped, 1 xfailed`. The failures are the A1 rows above plus the names-rule own-test defect.
  - After the re-points: **`2351 passed, 361 skipped, 1 xfailed, 15 warnings in 306.03s (0:05:06)`**, 0 failed. Against STEP-3 (2330 / 361), the +21 are exactly `test_setups_hitchhiker.py`'s 21 tests.
- **With-DB.** cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_registries.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_hitchhiker.py tests/cobalt/test_setups_lego.py tests/cobalt/test_assumed_store.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_replay_formations.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_evaluate_cli.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_p4_migrations.py tests/cobalt/test_radar_migration.py tests/cobalt/test_tenancy.py tests/experiments/setups_one` → **`386 passed, 1 skipped in 1136.44s (0:18:56)`**.
  - The skip, from `-rs` on `test_radar_evaluate.py`: `SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` (gate 3, NOT RUN by design).
- **X7 / X18 stored** (after the stored module was pointed at each shape's own rows): `COBALT_ENV=dev uv run pytest -q tests/experiments/setups_one/test_x7_x18_stored.py -s` → `X7 stored: sessions=10 grid=30min {'rubberband': {'scans': 7200, 'both_sides': 0, 'formed': 0}, 'hitchhiker': {'scans': 7200, 'both_sides': 0, 'formed': 17}, 'rubberband-without-htf-avoid': {'scans': 7200, 'both_sides': 0, 'formed': 104}}` · `X18 stored: sessions=10 {'scans': 7200, 'atrs_from_open_diff': 0, 'leg_count_diff': 0} htf_level_proximity=UNPROVEN (daily leg)` → `1 passed`.
  - **X7 hitchhiker stored: PASS.** It forms on 17 grid scans of the stored sessions, never on both frames.
- rm → `ls -la .env` → `ls: .env: No such file or directory`.

### COMMIT

`6b0172e wip(setups-one): STEP-4 partial — …` (the checkpoint), then `94897cc feat(setups): STEP-4 micro-range, pivots, opening-drive roles, range_break, consolidation_low — hitchhiker (FINAL C3b)`. `git show --stat HEAD`: 28 files, 635 insertions(+), 59 deletions(-); every path is one named above. Long-form `git status` came before it.

## STEP-5

C4: the D4 Extension lifecycle, `indicator_cross`, `measured_fraction`, `recent_higher_low`, `between` + `flat`, Arith → backside and fashionably-late (FINAL §3 D4, §2.2, §2.3, §4; [F-03 · X10]).

### T (RED)

New: `tests/cobalt/test_setups_d4.py`. It holds:

- the start pin of every `ExtensionObservation` field on the committed day;
- the NN#16 guard: while `A-08` is null, `Extension.state` is today's value on every scan;
- X10 and its control, both on a definition-written day: a run down, a culminating bucket, the turn, a snapback, higher highs and higher lows above a rising EMA9, and a micro-Range whose middle base is the counter-pivot;
- the lifecycle on constructed series;
- `indicator_cross`, `measured_fraction`, `recent_higher_low`, Arith, a null `cfg`, `between` + `flat`;
- the two shapes' evaluability, the fashionably-late path and its F1 reading at defaults, X7 ×2 and X11 ×2.

The corpus gains `backside` (`example-extension-backside`) and `fashionably-late` (`example-extension-late-cross`), with this build's constructed fills `D4_CONSTRUCTED` (L69).

Run on the START code (`94897cc`): **18 failed, 4 passed**. The 4 are X7 ×2 and X11 ×2, vacuous with nothing served. The start pin `86254c33003cf4767709ceb927cc96052c7ca6b96ce1e4e744287b62c98166b5` was read from its own failure and pasted; it is now a GUARD. RED lines, one per kind:

| test | RED |
|---|---|
| Extension pin | `AssertionError: assert '86254c33003c...87b62c98166b5' == 'PIN'` |
| lifecycle | `ImportError: cannot import name 'LifecycleParams' from 'cobalt.radar.anatomy.extension'` |
| the domain / the row | `AssertionError: assert frozenset({'c...ing', 'none'}) == frozenset({'b... 'reverting'})` |
| `indicator_cross` | `KeyError: <TriggerType.INDICATOR_CROSS: 'indicator_cross'>` |
| `measured_fraction` | `ImportError: cannot import name 'measured_fraction_price' from 'cobalt.radar.formation.stops'` |
| `recent_higher_low` | `AssertionError: assert <StructuralRef.RECENT_HIGHER_LOW: 'recent_higher_low'> in {…}` |
| Arith | `cobalt.radar.evaluate.Unsupported: operand shape 'arith' is not evaluable i…` |
| a null cfg | `cobalt.radar.evaluate.Unsupported: cannot compare Decimal('0.5') > None` |
| `between` | `AssertionError: assert 'between' in {}` · `ImportError: cannot import name 'flat_between' …` |
| shapes / paths | `AssertionError: ('Extension.state∌backside', 'stop:structural_extreme:recent_higher_low')` · `('Extension.state∌backside', 'Extension.state∌reverting', 'between', 'cross', 'flat(EMA9, window: 15 min / working_tf)', 'stop:measured_fraction', ...)` |

Own-test defects, fixed in the test:

- The first micro-Range of the constructed day had its base-touch buckets' highs inside the touch tolerance of the top, so the touches merged into one. It was also too long, so EMA9 caught up with its low. Rewritten from the definition as a sharper rally, then a 7-bucket range with 2 buckets after the deep base.
- The first fashionably-late path assertion was a placeholder (`in (formed, not_formed, avoided)`). It is now the full formation at 10:30 ET.

### X (X10 FIRST, on the changed code — D4 must exist)

- **X10: FAIL.** VERBATIM: `X10: FAIL evaluation=not_evaluable direction=None long=not_evaluable/Extension path B only — catalyst unknown in S2 (R4) short=not_formed/None`.
  - The day recovers past the open, so the Extension's direction (sign of last − open, `extension.py:96-103`) flips to up. The long frame's culminating bar is gone and only path B remains; the short frame has no culmination. The backside shape NEVER FORMS.
  - The control, the same construction before it passes the open, forms LONG: anchor Extension, stop `recent_higher_low`, geometry guard held.
  - The FINAL's line fires: "`A-01` is not applied to the D4 states as §1 words it", and it offers two fixes, choosing neither → **the backside and fashionably-late acceptances STOP; D4 is KEPT; both defs are pinned `AWAITING_A_RULING`** (`test_setups_lego.AWAITING_A_RULING`, never `AWAITING_A_DAY`). `ASK DESK: X10 failed — which fix, Grok's or Fable's? [05:1x]`. Safe default: neither is built → ESCALATE 12.
- **What still runs (Lego-style path proofs, [F-21]):**
  - The fashionably-late shape forms LONG at 10:30 ET on the definition-written day: trigger `indicator_cross` (the EMA9 over VWAP cross bar's close), stop `measured_fraction(entry, turn_low 8.30, 0.4)`, geometry guard held.
  - At production defaults it reads `flat_threshold.ema9_unset` → **`AWAITING_A_RULING: F1`**.
  - Backside's path is the X10 control above.
- **X7 offline:** `X7 backside: scans=392 formed=0 both_sides=0` · `X7 fashionably-late: scans=392 formed=0 both_sides=0` → PASS (vacuous: nothing forms on the committed day). The stored half runs in SUITE.
- **X11:** `X11 backside: atoms=6 failures=[]` · `X11 fashionably-late: atoms=3 failures=[]` → PASS. No new seam reason was needed: the `between` reasons are node-level unknowns, never an `AtomOutcome`.
- **X5:** `X5 offline: defs=6 frames=2 members=50 runs_s=[2.97, 2.96, 3.03] p95~max=3.03s budget=100.0s` → PASS.

### C

| file | change |
|---|---|
| `src/cobalt/radar/anatomy/extension.py` | `LIFECYCLE_KEYS`, `LifecycleParams`, `lifecycle_params`, `LifecycleObservation`, `extension_lifecycle` (turn, `reverting` by `A-08`, `backside` by HH / HL above a rising EMA9); `detect_extension` untouched |
| `src/cobalt/radar/anatomy/frame.py` | `Extension.state` served lazily (today's value while `A-08` is null); objects `series`, `turn_index`, `cross_index`, `atr`, `tunables` |
| `src/cobalt/radar/formation/atoms.py` | `Extension.state` domain + keys + reasons; `RELATIONS["between"]`; `flat_between`, `window_bars`, `_between_gaps`, `relation_operand_names`, `BETWEEN_EVENTS`; Arith `*` / `/` in `predicate_gaps` |
| `src/cobalt/radar/formation/triggers.py` | `IndicatorCross` |
| `src/cobalt/radar/formation/stops.py` | `recent_higher_low` (latest pivot low in the micro-Range), `MeasuredFraction`, `measured_fraction_price`; resolvers take `trigger=` |
| `src/cobalt/radar/anatomy/registry.py` | a served relation's own operands are not unserved atoms |
| `src/cobalt/radar/evaluate.py` | Arith in `_value` (÷0 → `division_by_zero`); a null `cfg` → `<key>_unset` (a latent defect fixed); `_between` + `evaluate_node(context=)`; `stop_resolver(...).resolve(..., trigger=trigger)`; `stop_ref` from the stop outcome |
| `configs/cobalt/taxonomy/tunables.yaml` | `extension.snapback_bars_cleared` (`A-08`, bars, null, proposed, global). `A-11` was already a row (STEP-3); `backside_hh_min` / `_hl_min` were already ruled rows |

No convention row is added: this step's resolvers implement no new convention (ESCALATE 13).

### A1

| test | old assertion | new assertion | FINAL tag |
|---|---|---|---|
| `test_setups_registries.py::test_the_five_tables_exist_and_serve_the_rubberband_bricks` | the `Extension.state` domain == {culminating, none} | == {culminating, reverting, backside, none} | §3 D4 |
| `test_setups_registries.py::test_e8_a_symbol_outside_the_atoms_domain_is_not_evaluable` | `IN {reverting, backside}` is ∌-named | `IN {building, resuming}` is ∌-named (no rule produces them); `IN {reverting, backside}` is now evaluable | §3 D4, §2.5 E8 |
| `test_setups_d1.py::test_x22_a_rubberband_def_reads_no_d1_key` | reads ∩ D1 keys = ∅ | reads ∩ (D1 keys − the declared closure) = ∅ AND reads ⊆ the declared closure (`Extension.state` now declares `slope_norm.bars`; `assumed_closure` reads it at formation) | §3 D4, R2-2.2 B |
| card pins: [F-11] ×2, Lego (ii) ×2, T6 formed card | `tunables_sha256` mapped without STEP-3/4's rows | … and without `extension.snapback_bars_cleared` | §3 D4 (new row) |
| `test_setups_lego.py` | the property over every evaluable shape | minus `AWAITING_A_RULING` = {backside, fashionably-late}, named with X10's result | X10 (prompt STEP-5) |

No assertion was removed, and no skip or xfail was added.

### D

- Appended: `radar/anatomy/extension.md` (D4, NN#16, X10), `frame.md`, `registry.md`, `radar/formation/atoms.md`, `triggers.md`, `stops.md`, `radar/evaluate.md`.

### SUITE

- **Offline.** `uv run pytest -q tests/cobalt tests/taxonomy` (background).
  - The first run: `8 failed, 2366 passed` — the A1 rows above.
  - After the re-points: **`2374 passed, 361 skipped, 1 xfailed, 15 warnings in 348.58s (0:05:48)`**, 0 failed.
  - Against STEP-4 (2351 / 361), the +23 are exactly `test_setups_d4.py`'s 23 collected tests. The RED run had 22; `test_fashionably_late_at_production_defaults_reads_its_f1_holes` was added when the path test was tightened.
- **With-DB.** cp → `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_registries.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_hitchhiker.py tests/cobalt/test_setups_d4.py tests/cobalt/test_setups_lego.py tests/cobalt/test_assumed_store.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_taxonomy_store.py tests/cobalt/test_radar_score_migration.py tests/cobalt/test_replay_formations.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_evaluate_cli.py tests/cobalt/test_archiver_migrations.py tests/cobalt/test_p4_migrations.py tests/cobalt/test_radar_migration.py tests/cobalt/test_tenancy.py tests/experiments/setups_one -s` → **`409 passed, 1 skipped in 1258.53s (0:20:58)`**. The skip is the live-note proof, by design.
  - Its experiment lines, VERBATIM: `X7 stored: sessions=10 grid=30min {'rubberband': {'scans': 7200, 'both_sides': 0, 'formed': 0}, 'hitchhiker': {'scans': 7200, 'both_sides': 0, 'formed': 17}, 'backside': {'scans': 7200, 'both_sides': 0, 'formed': 0}, 'fashionably-late': {'scans': 7200, 'both_sides': 0, 'formed': 7}, 'rubberband-without-htf-avoid': {'scans': 7200, 'both_sides': 0, 'formed': 104}}` → **X7 stored backside / fashionably-late: PASS.** (Fashionably-late formed on 7 grid scans, with this build's constructed F1 fills.) X18 stored is unchanged (`0 / 0`, htf UNPROVEN). X1, X2, X13 and X15 are unchanged from their first runs.
- rm → `ls -la .env` → `ls: .env: No such file or directory`.

## ESCALATE

(running list; the ALWAYS items (i)–(xii) are written at CLOSE)

1. **PREFLIGHT consumers not named by INDEX CARD 5** — `replay/runner.py:56`, `:219-223` (reads `SUPPORTED_EVALUATORS`; follows the STEP-1 update), `replay/models.py:263`, `radar/store.py:383-385`, `db_migrations/cli.py:111`, `cards/radar.py:55`, `:61`. None changed what a step must do.
2. **The Lego baseline has two lines beyond the drafter's three** — `taxonomy/trade_def.py:637` (a schema comment naming a corpus example) and `radar/anatomy/registry.py:3` (the registry docstring). Recorded in the baseline with their reasons; STEP-9 (i) compares against the recorded set.
3. **The R1-21 "two real formations of one (ticker, def)" fixture no longer exists on the committed day.** The start-of-step replay's two formations were (a) the with-trend LONGS (gone by A-01; X17: point (5) refuses all 71) and (b) a second countertrend formation first seen at 18:45:00 UTC with the last close (6.89) already through the short's stop — now `not_formed: stop_wrong_side` by §9 point (5). Tried to restore it with engine-config variants (`bars_cleared` 1/2/3; `stop.buffer`; `extension.path_a_volume_sigma` / `_ma_bars`): always ONE formation. The two-row / extended-key / unique-index assertions now run on the real row + a copy differing ONLY in `formation_at` (named in the module docstring). Closed by the DB-backed fixture-cut job (a stored day where the definition forms twice). Not a code defect.
4. **Health pills see the dot.** A FILLED card's `card_health` dot class includes every computed dot, so it shows one extra `n/a` pill for `assumed_formation` ("N/A — assumed_formation has no graded value"). Honest and harmless; `cards/health.py` is outside STEP-1's files and was NOT changed. `ASK DESK: should the health dot class skip assumed_formation? [20:44]` — safe default: unchanged.
5. **The geometry guard also refuses a formation whose stop is already through at the scan** (point (5)'s last-close clause) — on the replay's 100 s grid this removes the countertrend def's 18:42 formation that the start-of-step replay listed. That is the FINAL's rule as built (X17 PASS); stated here because `--replay` formation counts for the synthetic def drop from 2 to 1 on the committed day.
6. **A full `COBALT_ENV=dev` run shows 11 reds outside this build's files** — archiver append / migration tests (`archive_progress`, `archive_incidents` absent in `cobalt_dev`) and one migrate-proof cursor test. They name tables this build never touches; whether they are red on main too was not run (L70: UNPROVEN, not a defect of this build). The prompt's with-DB set is green.
7. **X1's POOL share is UNPROVEN in the worktree.** `cobalt_dev` has no `system.radar_membership` rows for its 10 stored sessions (`pool_sessions=0`). The share was reported over every stored name instead (0.813 / 0.743 / 0.65 for periods 9 / 14 / 21) and labelled `stored`, never mixed into the pool share. The pool reading runs at the deploy.
8. **A cancelled Bash call (process slip).** STEP-3's first DevDoc append was a Bash redirect. It waited on a permission dialog until the CTO desk cancelled it (L63). No content was written, and it was re-done with the Edit tool. Per the desk, the rule for the rest of the build is: file content only through Write / Edit, and any denied Bash call → wip-commit + FAILED.
   **A second one, STEP-4:** `shasum -a 256 src/cobalt/radar/anatomy/leg.py` is not in the allowlist. It waited on a dialog until the desk cancelled it at 04:09; nothing ran. X16's digest is computed inside the pytest module with `hashlib` instead. Also recorded: STEP-3's pre-commit check used `git status --porcelain`, not the long form the prompt names (from STEP-4 on: long form). And earlier `uv run python -c …` probes (read-only parses and the STEP-3 pin capture) are not in the allowlist either. They ran unprompted, but from here none are used: pins come from a test's own failure output.
9. **X13 fires its fail line.** The median `atr_seeded` / RTH-weighted ATR is 0.532 at 09:40, 0.687 at 09:50 and 0.788 at 10:00, "well under 1". The FINAL: "early ATR-scaled tolerances need an RTH-weighted ATR, and `A-05` changes for ATR while staying for the EMAs." No key changed. `A-03` / `A-04` tolerances scale with the seeded `ATR(working_tf)` as built. `ASK DESK: X13 says early ATR tolerances are tight — does A-05 change for ATR? [04:1x]` — safe default: unchanged.
10. **X15: the literal reading forms (5 name-sessions; A-07 forms 36).** The FINAL: "The literal reading forms → `A-07` is not needed as worded." `A-07` is kept as the FINAL words it (built, `leg_roles.opening_drive`); the literal reading exists only for X15 (`opening_drive_literal`). Whether A-07 amends the taxonomy is his, after cards (FINAL Open point 7).
11. **A constructed literal matched a companion value (hygiene fix, STEP-4).** STEP-3's `test_setups_d1.py` used `slope_norm.bars = 3` as its own constructed window, and that equals the companion's assumed `A-11` value (seen in a grep of key names). Changed to 4 in STEP-4 so no companion value sits in a committed file. Every other constructed literal (`D2_CONSTRUCTED`) was chosen not to match a value seen.
12. **X10 FAILED → backside and fashionably-late are `AWAITING_A_RULING`.** On a day that recovers past the open, the Extension's direction (sign of last − open) flips and the backside shape never forms. The FINAL offers two fixes: Grok's ("they bind side only through the mirrored frame on their own long-side text") and Fable's ("the Extension's direction is stamped at its culminating bar and held through `reverting` / `backside`"). It chooses neither. `ASK DESK: X10 failed — which fix, Grok's or Fable's? [05:1x]`. Safe default: neither is built. D4 is kept. Both paths are proven on definition-written days (the backside control; the fashionably-late path).
13. **D4 and Rubberband (a decision for the desk).** Growing `Extension.state` past `culminating` means that, once `A-08` is filled, a culminated Extension reads `reverting` after its snapback, and Rubberband's `Extension.state == culminating` stops re-forming on those scans. The first formation, and so the card, is unchanged. Built safe default: while `A-08` is null (committed config), `Extension.state` reads exactly today's value, so Rubberband is byte-identical now (every pin GREEN) and in production until the assumed note fills `A-08`. Also, `Extension.state` does NOT declare the warm-up convention (`frame.warmup_source`, A-05) in its closure, even though the lifecycle's rising-EMA9 test uses the seeded EMA9. Declaring it would mark every Rubberband card "assumed: frame.warmup_source" at committed config, where the lifecycle never runs. `ASK DESK: once A-08 is filled, should Rubberband's precondition hold through reverting, and should Extension.state declare A-05? [05:1x]` — safe default: as built.
14. **A null `cfg()` was compared as `None` (a latent defect, fixed at STEP-5).** Before, a predicate against a null engine row (the drive-then-range shape's `Range(micro).wick_ratio > cfg(range.wick_ratio_max)`) raised `Unsupported` and made the def `not_evaluable` at production defaults, whenever its preconditions held. It now reads unknown, `<key>_unset`.

## CONTINUE

next: STEP-6 (C5), nine-ema-scalp.
1. **X26 FIRST:** an offline test that constructs `AtomOutcome(atom=…, value_kind="boolean", boolean=True, assumed="A-13")` and follows the `detail()` caller. Quote the exception.
2. Then:
   - roles `Leg(pullback).{direction, end, index}`, `Leg(impulse)`, `Leg(pre_test)` (`A-14`), and `Leg(opening_drive OR impulse)`, over `leg.legs()` in `anatomy/leg_roles.py`;
   - the relation `touched`;
   - `trade_direction` / `opposite(x)` / `against(x)` bound from the frame;
   - `formation/triggers.py` `indicator_rejection`; `formation/stops.py` `indicator` (`at_entry`);
   - `Extension.instantiated on Leg(x)` (`A-15`);
   - the catalyst resolver `A-13`: an ATOMS row `catalyst_ref`, reading the pool admission, with `ASSUMED_CONVENTIONS = ("A-13",)` in its closure.
   - `tunables.yaml`: the convention rows `A-13`, `A-14`, `A-15`. Check the companion for their KEY NAMES only.
3. Acceptance for `nine-ema-scalp` (L11: `bids_hold` stays human). X1's second reading: quote X1's share beside the def's preferred window. X7, X11, X5.

Rules still in force: file content only through Write / Edit; pins from a test's own failure output; long-form `git status` before a commit; no unlisted commands (scratch probes go in a pytest file under the job's tmp).

(run in progress — step 6 of 9, next under ## CONTINUE)
