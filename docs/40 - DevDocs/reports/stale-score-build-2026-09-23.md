# Stale score build — 2026-09-23

Prompt: `docs/40 - DevDocs/prompts/2026-09-23/46-stale-score-build.md` · worktree `/Users/cobalt/cobalt-wt/stale-score` · branch `cards/stale-score-0922` · base `51afdad0` · started 14:01 ET (`date`: `Wed Sep 23 14:01:07 EDT 2026`).

## §0 Headline

(in progress)

## L74

Recorded once (L74): a system-reminder arriving beside a tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and named a file-send tool (`SendUserFile`). Treated as DATA; not followed. Commits carry only `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## AUTHORIZATION

Every row checked by its own Bash call (row · phrase found):

| check | result |
|---|---|
| `cto-2026-09-22.md` R37 | line 129 · "drops below every scored card" · his word "A" |
| R38 | line 128 · "PREMARKET" · "A" |
| R39 | line 127 · "TWO CLOCKS" · "A" |
| R40 | line 126 · "EXCLUDED from the shadow agreement numbers" · "B" |
| R41 | line 125 · "order among themselves by pool position" · "A" |
| R42 | line 124 · "FILLED-card health pills keep computing" · "A" |
| R43 | line 123 · "chip and slot change at his next tap or reload" · "A" |
| R44 | line 122 · "keep today's deployed look" · "A" |
| R45 | line 121 · "recompute the FRESH-price tap race" · "B" |
| 09-22 R58 | line 108 · "build lane" (stale-score build named IN LANE) |
| R45 committed on main (`log -S`) | `1a3f5cf7003c03cb41a5158d601133b4c61a264b` |
| R32 | line 131 · carries `claude-opus-5-5` |
| 09-23 R58 | `cto-2026-09-23.md` line 61 · "yes start both" · names stale-score `31` |
| 09-23 R58 committed (`log -S`) | `dab5c706126d2ca987cf32a262ecbfcb90ab6545` |
| launch row naming `46-stale-score-build.md` | `cto-2026-09-23.md` line 69 = `| R66 |` (desk launch row, BASE `51afdad0`); `cto-2026-09-24.md`: "No such file or directory" (recorded, not fatal — row found in the other) |
| launch row committed (`log -S`, desk files only) | `ba7af71449b16e01301dffd74c43d956433ff2fc` |
| `.env` cp string in `cto-2026-09-22.md` (`grep -c -F`) | 1 |
| `.env` rm string in `cto-2026-09-22.md` | 1 |
| rm string committed (`log -S`) | `084c29416c02b566ce7741bfa3154ca84fcc02e2` |
| R64 | line 102 · both strings · "Approved all" |
| 20 allow + 3 deny strings in `31-stale-score-build.md` (`grep -c -F -e`, quotes included, 23 calls) | every count ≥1 (the two `.env` strings count 2, all others 1) |

AUTHORIZATION: PASS. One discrepancy recorded (not an authorization gate): launch row R66 says "Migration, if its STEP-3 builds one: `0016` (reserved, R63)", and R62/R63 (`cto-2026-09-23.md` lines 65–66) give `0015` to DRC D1 — this prompt says `0015` is this build's (settled). → ESCALATE 1; decided at STEP-3 only if X30 = (A).

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Wed Sep 23 14:02:16 EDT 2026` · allowed |
| THE BASE | title line bold sha | — | `51afdad0` (8 hex) · filled |
| clean tree | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/stale-score-build-2026-09-23.md"` — only this report (the prompt's FIRST Write creates it before PREFLIGHT); nothing else |
| long status | `git status` | 0 | `On branch cards/stale-score-0922` / `Untracked files:` |
| cut | `git log --oneline -1` | 0 | `51afdad0 fix(seam): re-pin the healthy-ladder SHA to the setups ladder change (L68 seam, 09-23)` = BASE (first launch) |
| seam pin in base | `git log --oneline b007ce2e..51afdad0` | 0 | `51afdad0 fix(seam): …` — NON-EMPTY |
| base test-only above b007ce2e | `git log --oneline b007ce2e..51afdad0 -- src configs` | 0 | no output — EMPTY |
| setups branch tip | `git -C /Users/cobalt/cobalt log --oneline -1 setups/seven-0921` | 0 | `9efddbc5 docs(seam): build report — 51afdad0` — differs from BASE (a docs commit above it); RECORDED, not fatal |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `ba7af714 docs(desk): 09-23 R65 seam fix built (0 defect); seam check + stale-score launch rows` |
| own commits | `git log --oneline 51afdad0..HEAD` | 0 | no output — EMPTY |
| no `.env` | `ls -la .env` | 1 | `ls: .env: No such file or directory` |
| LANE GATE (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — PASS |
| LANE GATE (b) | `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` | 1 | `ls: /Users/cobalt/cobalt-wt/DEVDB-HOLD: No such file or directory` — PASS |
| migrations | `ls src/cobalt/db_migrations` | 0 | newest `0013_tunables_slug_nullable.sql` (+ rollback); no `0012`, no `0014`, no `0015` |
| no helper yet | `grep -rn "score_last\|intraday_stale: bool" src/cobalt` | 0 | ONE hit: `src/cobalt/radar/evaluate.py:696:    ext: ExtensionObservation, member: MemberInput, *, intraday_stale: bool, daily_ok: bool,` — the keyword of `_factor_observations`, not a `MemberEvaluation` field; `score_last` absent → ESCALATE 2 (informational) |
| version | `grep -n "EVALUATOR_VERSION\|DESK_FORMULA_VERSION\|SUPPORTED_EVALUATORS" src/cobalt/radar/evaluate.py` | 0 | `160:EVALUATOR_VERSION = "s2p2.2"` · `161:DESK_FORMULA_VERSION = "s2p2.1"` (+ uses at 1188, 1429, 1551, 1554, 1760, 2003). `SUPPORTED_EVALUATORS` is NOT in `evaluate.py`: it lives in `src/cobalt/replay/formations.py:83` = `frozenset({"s2p2.2"})` (imported by `replay/runner.py:56`). Bump FROM `s2p2.2` (evaluator) / `s2p2.1` (desk) |
| cd | `cd /Users/cobalt/cobalt-wt/stale-score` | 0 | allowed |
| pytest | `uv run pytest --version` | 0 | `pytest 9.0.2` (uv created `.venv`, 248 packages) |
| restarts probe | `uv run cobalt jobs restarts 51afdad0..HEAD` | 0 | `docs/40 - DevDocs/reports/stale-score-build-2026-09-23.md	A	DOCS	-` / `RESTARTS: none` (the untracked report is in the range's working tree) |
| mkdir probe | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | no-op (directory exists) |

No denial. PREFLIGHT: PASS.

### v2 cite → base line (v2 cites main `3ceb469`; re-located by symbol at `51afdad0`)

| v2 cite | symbol | base line |
|---|---|---|
| `evaluate.py:340-364` (W3) | `class MemberEvaluation` | `evaluate.py:599-627` |
| `evaluate.py:502` ([F-10] step 1) | `last_price = last_bar.close …` in `evaluate_member` | `evaluate.py:920-921` (`base` dict `:922-926`) |
| `evaluate.py:517-524` (not_evaluable return) | `evaluability` / `convention_refusals` returns | `evaluate.py:940-955` (two `not_evaluable` returns, before the flag) |
| `evaluate.py:529-534` (W1) | `intraday_staleness(...)` call | `evaluate.py:960-965` |
| `evaluate.py:598-599` (intraday `input_stale`) | `if intraday_stale: return both(result("input_stale", …))` | `evaluate.py:1019-1021` |
| `evaluate.py:624`, `:629` (daily `input_stale`) | `no_daily_bars` returns in `on_side` | `evaluate.py:1072-1074`, `:1079-1082` |
| formed return | `result("formed", …)` | `evaluate.py:1119-1122` |
| `evaluate.py:463-477` (W4) | `_factor_observations` `htf_level_proximity` | `evaluate.py:726-742` |
| `evaluate.py:776-778`, `:803` (W6/W7) | `refresh_card` `last = … else card.entry` | `evaluate.py:1277-1279`, return `:1299-1305` |
| `evaluate.py:1043-1089`, `:1079` (W17) | `replay_receipt`, entry fallback | `evaluate.py:1544-1596`, fallback `:1586` |
| `evaluate.py:1082` | `published_numbers` | `evaluate.py:1530-1541` (called `:1589`, `:1940`, `:1991`) |
| `evaluate.py:1317-1349` (W5, stage loop) | `_evaluate` open-card loop | `evaluate.py:1823-1871` (refresh `:1857`) |
| `evaluate.py:1324-1328` (X26 slug match) | `by_slug` / `formation_changes` branch | `evaluate.py:1829-1835` |
| `evaluate.py:1384` (create call) | `score_card(fresh, last=ev.last_price, …)` | `evaluate.py:1896-1897` |
| `evaluate.py:928`, `:1253` (version on run/receipt) | `open_score_run` payload / `build_receipt` | `evaluate.py:1760`, `:1429` |
| — | `EVALUATOR_VERSION` / `DESK_FORMULA_VERSION` | `evaluate.py:160-161` |
| — | `SUPPORTED_EVALUATORS` | `replay/formations.py:83` (check `:147`) |
| — | `CardUpdate` (prompt: "`cards/store.py` `CardUpdate`") | `evaluate.py:1223-1239` — it lives in `evaluate.py`; `store.py` has no `CardUpdate` → STEP-2 needs no `store.py` edit |
| `anatomy/freshness.py:106-120` | `intraday_staleness` | `src/cobalt/radar/anatomy/freshness.py:106-120` (path is under `radar/`) — no session gate in it |
| `scoring.py:254` / `:264` / `:265` / `:312` / `:319-330` | `proximity` / `card_score` / `CardScore` / `score_card` | `scoring.py:264-271` / `:274-277` / `:318-326` / `:329-346` |
| `scoring.py:247-251` (W15) | `suppression` | `scoring.py:255-261` |
| `store.py:1016-1053`, `:1022-1026`, `:1029-1037` (W8/W9) | `refresh_radar_card`, lock SELECT, taps-moved | `store.py:1016-1053`, `:1022-1026`, `:1029-1037` (unchanged) |
| `store.py:1182-1231`, `:1217-1222` (W10) | `tap_dot`, suppression write | `store.py:1182-1236`, `:1220-1229` |
| `cards/radar.py:167-183` (W16) | `ladder_order` | `cards/radar.py:167-183` |
| `audit_export.py:363` (W22) | `export_replay` `score_card(… else trigger …)` | `audit_export.py:364-365` |
| `audit_export.py:244-259` | `export_run` replay + mismatch | `audit_export.py:245-260` |
| `formations.py:145-149` | `formation_candidates` gate | `formations.py:147-151` |
| `radar_panel.py:758` (X22) | `build_ladder_view` `last=r.last_price` | `radar_panel.py:758` |
| `0007:255` | `shadow_agreement_v` | `0007_radar_cards.sql:245-258`; `card_dot_taps` `:141-152` (`engine_grade_at_tap` `:147`) |
| `0006:103-106` | `radar_score` / `radar_score_run` | `0006_radar_score.sql:66-87` (`evaluator_version` `:76`), `:92-113` |

## BASELINE

`date` 14:04 ET (launch of the run). OFFLINE `uv run pytest -q tests/cobalt tests/taxonomy -p no:cacheprovider` (background), summary VERBATIM:

`2482 passed, 361 skipped, 1 xfailed, 15 warnings in 529.60s (0:08:49)` — exit 0, **0 failed**.

WITH-DB: 14:13:43 the LANE GATE (a) found `/Users/cobalt/cobalt-wt/drc-d1/.env` (DRC D1 build `53`, R62) → lane held, `.env` NOT copied (`## LANE`). The with-DB baseline must run on the BASE tree, so it is taken before STEP-2's first `src/` edit; offline STEP-1 (experiments only, no `src/` change) runs meanwhile.

## STEP-1

Folder `tests/experiments/stale_score/`: a `conftest.py` inside it re-exports `tests/cobalt/conftest.py`'s fixtures (the setups_one shape); NO `tests/experiments/__init__.py` created (the base has none). `stale_support.py` = shared construction (FTFT real-shape fixture, `SCAN = 100` the module's own literal, close-age = ttl + 1). Experiments the fix FLIPS (X6, X11, X12, X14's flag, X18's assertion, X26's flag) branch on `FIXED` (= `score_last` exists) so the CLOSE re-run on the tip proves the flip instead of going red. Every run: `uv run pytest -q -s tests/experiments/stale_score/<module>` (X1/X5a: `uv run pytest -q tests/cobalt/test_stale_score.py -k "x1_ or x5a" -p no:cacheprovider`). Order as the prompt lists; X10 first.

### X10
`X10: AS EXPECTED` — n = 1 member, 2 receipts. Output: `X10: receipts=2 members=1 receipt_as_of=['2026-01-06T16:31:40+00:00'] rebuilt_as_of=['2026-01-06T16:31:40+00:00'] equal=True wall_clock=False` · `1 passed in 0.33s`. `rebuild_members` takes `as_of` from the receipt (`evaluate.py:1481`); the stale rule is L57-sound. No design stop.

### X27
`X27: AS EXPECTED` — n = 1 stale card. Output: `X27: evaluation=input_stale note='intraday bars older than 2 x radar.scan_interval' cards=1 stage='required computed dot N/A and untapped — atrs_from_open: input_stale; Extension.leg_count: input_stale; trail_fit: MANUAL; assumed_formation: ASSUMED (tap to grade)' replay='…same…' byte_identical=True published_equals_recomputed=True` · `1 passed in 0.35s`. No gap at the base (one text path: `score_card` → `published_numbers` on both sides); STEP-2 T (xii) re-proves it with the stale sentence.

### X1
`X1: AS EXPECTED (RED on the base)` — written ONCE as STEP-2's test `tests/cobalt/test_stale_score.py::test_x1_all_dots_tapped_on_stale_bars_scores_nothing_and_names_the_close`. RED line: `E       AssertionError: card_score 64 published on stale bars` (`proximity=Decimal('0.919355')`, `conviction=Decimal('0.7')`, `last_price=Decimal('5.5750')`). n = 1.

### X5a
`X5a: AS EXPECTED (RED on the base)` — STEP-2's test `…::test_x5a_no_closed_bar_today_gives_no_proximity_not_the_maximum`. RED line: `E       AssertionError: proximity 1 from no bar` (`card_score=70`: the `card.entry` fallback scores conviction at its ceiling). n = 1. Summary: `2 failed, 15 deselected in 0.63s`.

### X5b
`X5b: AS EXPECTED` — `X5b: bars=895 prior_session_bars=895 last_price=None last_bar_ts=None consumed=0 evaluation=input_stale`. All-prior-session bars → `last_bar` None (`_closed_i1` keeps today's ET date only, `evaluate.py:861-863`) → X5a's path; C nulls either way. n = 895 bars.

### X6
`X6: AS EXPECTED (the W4 defect confirmed by the engine)` — `X6: fixed=False evaluation=input_stale last_price_present=True daily_present=True obs_stale=False obs_value_present=True dot_na_reason=None dot_engine_grade_present=True atrs_from_open_stale=True`. On stale bars `htf_level_proximity` is graded from the stale price (no flag) while its siblings are stale → STEP-2 T (v). n = 1.

### X7
`X7: AS EXPECTED` — `X7: fresh_active=[2, 1, 5, 3, 4] stale_active=[2, 1, 5, 3, 4] unpromoted_active=[2, 1, 3, 4, 5] promoted=[5] pinned_fresh=[2, 1] pinned_stale=[2, 1] null_chip=[3]`. A promoted NULL WATCH card stays promoted; pinned order unchanged; unpromoted NULL sinks last. n = 5 entries.

### X8
`X8: AS EXPECTED` — `X8: by_side={'long': 'input_stale', 'short': 'input_stale'} stale_scan_cause=None past_deadline_cause=deadline stored_bar_through_stop_cause=stop_before_arm`. n = 3 cases.

### X11
`X11: AS EXPECTED (the W22 fallback confirmed)` — `X11: fixed=False re_evaluations=1 evaluations=['formed'] candidate_proximities=['1'] error=None`. The `--replay` scorer emits proximity `1` for a member without a price (reachable only by construction: a formed evaluation always has a fresh bar) → STEP-2 T (ix). n = 1.

### X12
`X12: AS EXPECTED` — `X12: fixed=False null_proximity_refused_as='decimal_type' null_proximity_json=None card_score_json=null string_None_in_payload=False`. A null proximity cannot be constructed at the base (`CardUpdate.proximity: Decimal`); a null score already publishes JSON null → STEP-2 T (iv). n = 2 payloads.

### X14
`X14: AS EXPECTED` — `X14: fixed=False evaluation=input_stale note="avoid unknown: ['no_daily_bars']" close_age_s=0.0 intraday_stale_field=None proximity=0.919355 card_score=64`. Daily-missing `input_stale` with a fresh close keeps proximity (Q10) → STEP-2 T (vi) keeps it. n = 1.

### X15
`X15: AS EXPECTED` — `X15: scan=100 max_age=180 rth_open_age=210 rth(stamp,score_stale)=(True, False) premarket_close_age=201 premarket(stamp,score_stale)=(False, True)` (both limits are the module's constructions). The two clocks disagree both ways, as R39 accepts; the stamp code (`poller.py:121`) is not touched. n = 2.

### X18
`X18: AS EXPECTED` — 4 callers, 0 on `score_last` at the base: `audit_export.py:364` (`… else trigger`), `evaluate.py:1278` (`refresh_card`), `evaluate.py:1587` (`replay_receipt`), `evaluate.py:1896` (create). Old string: `evaluate.py:160`, `formations.py:81` (comment), `formations.py:83`. Repo greps, verbatim: `grep -rn "score_card(" src` → the same 4 calls + `scoring.py:329:def score_card(`; `grep -rn "s2p2.2" src tests` → the 3 `src` hits + `tests/cobalt/test_replay_runner.py:418`, `:472` (A1 candidates) + this build's own test literals. Re-run at STEP-2's end.

### X19
`X19: AS EXPECTED` — `X19: readers=2 compared_with_evaluator_version=0` (`evaluate.py:161` definition, `:1188` `desk_shadow`). Nothing compares it with `EVALUATOR_VERSION`; it moves with the singleton by the version rule.

### X20
`X20: AS EXPECTED` — `X20: reads_live_constant=True passes_that_value=True current_version_supported=True supported=['s2p2.2'] evaluator=s2p2.2`. The nightly binding reads the LIVE module constant (`replay/runner.py:219`), not a stored string → no old binding is refused once both move together; nothing unioned.

### X22
`X22: AS EXPECTED` — `X22: panel_calls_a_scorer=False scorers=[] last_site_display=True proximity_site_stored=True`. Display only → `radar_panel.py` is NOT changed (R44).

### X26
`X26: AS EXPECTED` — `X26: fixed=False formation_changes=[] evaluability_equal=True refused_evaluation=not_evaluable last_price_present=True intraday_stale_on_not_evaluable=absent`. `evaluability` reads formation fields only (`registry.py:47-71`), so a catalyst-scope edit cannot change it; a `not_evaluable` with an empty diff still arises from a convention row (a tunables change) — it returns before the base computes the flag, so [F-10]'s "every return path" is load-bearing. n = 1.

STEP-1: 17 experiments, 17 AS EXPECTED, 0 NOT, 0 UNPROVEN. No stop.

## STEP-2

### T (RED)
File `tests/cobalt/test_stale_score.py` (17 tests; new `src/` symbols imported INSIDE each test so every test goes red on its own). Run against the BASE code (`src/` untouched): `uv run pytest -q tests/cobalt/test_stale_score.py -p no:cacheprovider --tb=line` → `15 failed, 2 passed in 6.17s`. RED lines VERBATIM:

| T | test | RED line |
|---|---|---|
| (iii) X1 | `test_x1_all_dots_tapped_on_stale_bars_scores_nothing_and_names_the_close` | `AssertionError: card_score 64 published on stale bars` |
| (iii) X5a | `test_x5a_no_closed_bar_today_gives_no_proximity_not_the_maximum` | `AssertionError: proximity 1 from no bar` |
| (i) | `test_intraday_stale_is_required_and_set_on_every_return_path` | `assert (None is not None)` (no such field) |
| (ii) | `test_score_last_is_none_iff_stale_and_raises_on_a_fresh_member_without_a_price` | `ImportError: cannot import name 'score_last' from 'cobalt.cards.scoring'` |
| (ii) X18 | `test_every_score_card_caller_takes_its_last_from_score_last` | `AssertionError: [('audit_export.py', 364, 'score = score_card(dots, last=ev.last_price if ev.last_price is not None else trigger, …` |
| (iii) | `test_score_card_with_no_last_nulls_proximity_and_score_and_keeps_dot_reasons` | `AttributeError: module 'cobalt.cards.scoring' has no attribute 'stale_reason'` |
| (iv) X12 | `test_null_proximity_publishes_json_null_never_the_string_none` | `AssertionError: assert <class 'decimal.Decimal'> == (Decimal \| None)` |
| (v) X6 | `test_htf_level_proximity_on_stale_bars_is_input_stale_with_no_engine_grade` | `AssertionError: assert (False is True)` (`FactorObservation(… stale=False …)`) |
| (vi) X14 | `test_daily_missing_input_stale_with_a_fresh_close_keeps_proximity` | `AttributeError: 'MemberEvaluation' object has no attribute 'intraday_stale'` |
| (vii) | `test_one_new_version_string_and_the_previous_is_not_supported` | `AssertionError: assert ('s2p2.2' == 's2p2.1'` |
| (viii) | `test_audit_export_refuses_another_version_by_name_before_the_replay[None]` | `AssertionError: replay_receipt reached — the version gate must refuse first` |
| (viii) | `…[s2p2.2]` | `AssertionError: replay_receipt reached — the version gate must refuse first` |
| (ix) X11 | `test_audit_replay_path_never_emits_proximity_one_for_a_member_without_a_price` | `Failed: DID NOT RAISE <class 'cobalt.radar.evaluate.EvaluateError'>` |
| (xi) R38 | `test_r38_premarket_stale_bar_nulls_and_the_next_bar_lifts_it_with_no_tap` | `AttributeError: 'MemberEvaluation' object has no attribute 'intraday_stale'` |
| (xii) X27 | `test_stale_card_stage_and_replay_reason_are_byte_identical` | `AssertionError: assert (Decimal('0.919355') is None)` |
| (x) R37+R41 | `test_r37_r41_a_null_watch_card_sinks_below_every_scored_one_and_nulls_order_by_pool_position` | GREEN-as-pin (`ladder_order` untouched; red if the WATCH key stops putting NULL last or NULL ties stop falling to `pool_position`) |
| (viii) guard | `test_audit_export_same_version_run_still_exports` | GREEN by design (the gate must not refuse a same-version run) |

### C
Not started — LANE STOP at 14:15:34 (the with-DB BASELINE must run on the base tree before the first `src/` edit; `## LANE`).

## STEP-3

## STEP-4

## STEP-5

## EXPERIMENTS

## OWNER RULINGS AS BUILT

## L52

## CLOSE

## FOR THE DEPLOY

## FOR 50

## LANE

| time (`date`) | (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` | (b) `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` | result |
|---|---|---|---|
| 14:02:16 (PREFLIGHT) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | pass (no copy needed yet) |
| 14:15:34 (retry before STEP-2 C) | `-rw-------  1 cobalt  staff  2186 Sep 23 14:15 /Users/cobalt/cobalt-wt/drc-d1/.env` | `No such file or directory` | **LANE STOP** — held by `/Users/cobalt/cobalt-wt/drc-d1/.env` |
| 14:13:43 (BASELINE with-DB) | `-rw-------  1 cobalt  staff  2186 Sep 23 14:13 /Users/cobalt/cobalt-wt/drc-d1/.env` | `No such file or directory` | **HELD by `/Users/cobalt/cobalt-wt/drc-d1/.env`** — no copy; offline STEP-1 runs on (no gate needed); gate re-tried before any `src/` change |

## ESCALATE

1. **MIGRATION NUMBER CONFLICT (L72 P-b).** This prompt settles `0015` as this build's R40 view migration (under X30 (A)), `0016` = DRC D1. The desk's launch rows say otherwise: R66 (`cto-2026-09-23.md:69`) "Migration, if its STEP-3 builds one: `0016` (reserved, R63)"; R62 (`:65`) gives `0015` to DRC D1 (`53`); R63 (`:66`) "0015 D1, 0016 reserved for stale-score's conditional migration, 0017 voice". I pick neither silently. It matters only if X30 = (A). `ASK DESK: which number does the R40 view migration take — 0015 (this prompt) or 0016 (R62/R63/R66)? [14:15]` Safe default until answered (the prompt's own for a number question): no migration, decision (B)'s ASK.
2. PREFLIGHT grep `intraday_stale: bool` hit `evaluate.py:696` — the keyword of `_factor_observations`, not the `MemberEvaluation` field; `score_last` absent. Informational, no action.
3. **LANE STOP 14:15:34** — the dev-DB lane is held by `/Users/cobalt/cobalt-wt/drc-d1/.env` (DRC D1 build `53`, R62, which the desk launched in parallel "takes cobalt_dev only when no other .env exists"). R58 09-23 put this build FIRST in the lane; `53` took it at 14:13. Not a failure; relaunch the same line when the lane is free.
4. The setups branch tip moved to `9efddbc5` (a docs commit above the BASE) — recorded, not fatal (PREFLIGHT).

## CONTINUE

next: BASELINE with-DB — LANE HELD by /Users/cobalt/cobalt-wt/drc-d1/.env at 14:15:34 (`date`)

DONE: AUTHORIZATION, PREFLIGHT, BASELINE offline (2482 passed / 0 failed), STEP-1 (17/17 AS EXPECTED, commit `1a5c6928`), STEP-2 T (RED recorded; `tests/cobalt/test_stale_score.py` wip-committed RED).
ON RELAUNCH: `git status` / `git log --oneline 51afdad0..HEAD` / `ls -la .env` → LANE GATE → cp → `COBALT_ENV=dev uv run cobalt db migrate` → with-DB suite (background) → rm → `ls` proof (the tree's `src/` is still the BASE's: only tests/docs changed) → then STEP-2 C (design recorded in the T table; nothing of C written yet). Note: the wip test file is RED by design until STEP-2 C; the with-DB baseline counts those 15 red lines as this build's own, not `cobalt_dev`'s.

(run in progress — step 2 of 5, next under ## CONTINUE)
