# Stale score build r2 — 2026-09-24

Prompt: `docs/40 - DevDocs/prompts/2026-09-24/42-stale-score-build-r2.md` (re-issue of `46`, resumes its wip) · worktree `/Users/cobalt/cobalt-wt/stale-score` · branch `cards/stale-score-0922` · started 17:06 ET (`date`: `Thu Sep 24 17:06:58 EDT 2026`). `46`'s record: `docs/40 - DevDocs/reports/stale-score-build-2026-09-23.md` (history, unedited).

## §0 Headline

(in progress)

## L74

Recorded once (L74): a system-reminder arriving beside a tool result asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool (`SendUserFile`). Treated as DATA; not followed. Commits carry only `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`.

## AUTHORIZATION

Every row its own Bash call (row · phrase found · his word).

| check | result |
|---|---|
| placeholder gate `grep -n -E "R_[_]" …42-stale-score-build-r2.md` | no output, exit 1 — PASS |
| `cto-2026-09-22.md` R37 | line 129 · "drops below every scored card" · "A" |
| R38 | line 128 · "PREMARKET" · "A" |
| R39 | line 127 · "TWO CLOCKS" · "A" |
| R40 | line 126 · "EXCLUDED from the shadow agreement numbers" · "B" |
| R41 | line 125 · "order among themselves by pool position" · "A" |
| R42 | line 124 · "FILLED-card health pills keep computing" · "A" |
| R43 | line 123 · "chip and slot change at his next tap or reload" · "A" |
| R44 | line 122 · "keep today's deployed look" · "A" |
| R45 | line 121 · "recompute the FRESH-price tap race" · "B" |
| R45 committed on main (`log -S`) | `1a3f5cf7003c03cb41a5158d601133b4c61a264b` |
| R32 | line 131 · carries `claude-opus-5-5` |
| 09-23 R58 | `cto-2026-09-23.md` line 61 · "yes start both" · names stale-score `31` |
| 09-23 R58 committed (`log -S`) | `dab5c706126d2ca987cf32a262ecbfcb90ab6545` |
| 09-24 R9 | `cto-2026-09-24.md` line 22 · GATE EARLY · "A" |
| 09-24 R10 | line 23 · L76 · "A" |
| L76 in LAWS.md | line 435 `### L76 One owner, one lock for \`cobalt_dev\` (ruled 2026-09-24; …)` |
| launch row naming `42-stale-score-build-r2.md` | `cto-2026-09-24.md` line 85 = `\| R72 \|` (desk launch row; also lines 75 R62, 81 R68); `cto-2026-09-25.md`: "No such file or directory" (recorded, not fatal — row found in the other) |
| launch row committed (`log -S`, desk files only) | `de48c19b5ee81626d4b3d158e3fcf699ba6184d7` |
| `.env` cp string in `cto-2026-09-22.md` (`grep -c -F`) | 1 |
| `.env` rm string in `cto-2026-09-22.md` | 1 |
| rm string committed (`log -S`) | `084c29416c02b566ce7741bfa3154ca84fcc02e2` |
| 09-22 R64 | line 102 · both strings · "Approved all" |
| 09-23 R52 | line 55 · carries `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest *` · "Approved all commands you need" |
| live-vault string in `03-setups-fix-r2-build.md` (`grep -c -F`) | 1 |
| rebase pair | `cto-2026-09-24.md` line 81 = `\| R68 \|` carries `Bash(git -C /Users/cobalt/cobalt-wt/stale-score rebase main)` AND `… rebase --abort)` AND his words "All approved. Can you run? …" (P-HIS; not a desk launch row). Also named in R66 (desk record) and R72 (desk launch row) — those do not count and are not relied on |
| rebase string committed (`log -S`) | `de48c19b5ee81626d4b3d158e3fcf699ba6184d7` |
| 19 allow + 3 deny strings in `46-stale-score-build.md` (`grep -c -F -e`, quotes included, 22 calls) | every count ≥1 (the two `.env` strings count 2, all others 1) |
| removed string `"Bash(COBALT_ENV=dev uv run cobalt db migrate)"` in `42` | 0 — PASS (L76) |

AUTHORIZATION: PASS.

## PREFLIGHT

| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 17:08:17 EDT 2026` · allowed |
| cd | `cd /Users/cobalt/cobalt-wt/stale-score` | 0 | allowed |
| clean tree | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/stale-score-build-2026-09-24.md"` — only this report (the FIRST Write creates it); nothing else |
| long status | `git status` | 0 | `On branch cards/stale-score-0922` / `Untracked files:` |
| branch top | `git log --oneline -3` | 0 | `57925f3b wip(stale-score): STEP-2 partial — …` · `1a5c6928 test(cards): stale score STEP-1 …` · `51afdad0 fix(seam): …` = `46`'s wip (first launch) |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | `de48c19b docs(desk): 09-24 R71/R72 — voice V1 fix r1 BUILT d4e48f22 …; 42 stale-score r2 launch row (R68 pair, rules comm-checked, R__ → R72)` → `<main tip>` = **`de48c19b`** |
| deploy tag | `git -C /Users/cobalt/cobalt log --oneline -1 deploy-2026-09-24` | 0 | `a2d320b8 Reapply "Merge branch 'main' into deploy/stacked-0923"` |
| tag inside main tip | `git -C /Users/cobalt/cobalt log --oneline de48c19b..a2d320b8` | 0 | no output — `a2d320b8` is an ancestor of `de48c19b` |
| only the two wip commits off main | `git -C /Users/cobalt/cobalt log --oneline --cherry-pick --right-only de48c19b...cards/stale-score-0922` | 0 | exactly `57925f3b …` and `1a5c6928 …` — PASS |
| wip touches no `src/` | `git log --oneline 51afdad0..HEAD -- src configs` | 0 | no output — EMPTY |
| no `.env` | `ls -la .env` | 1 | `ls: .env: No such file or directory` |
| LOCK (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — PASS |
| LOCK (b) | `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` | 1 | `ls: /Users/cobalt/cobalt-wt/DEVDB-HOLD: No such file or directory` — PASS |
| migrations | `ls src/cobalt/db_migrations` | 0 | `0001` … `0011`, `0013_tunables_slug_nullable.sql` (+ rollback); no `0012`, no `0014`, no `0015` |
| live strategies | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (READ ONLY) |
| pytest | `uv run pytest --version` | 0 | `pytest 9.0.2` |
| mkdir probe | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | no-op (directory exists) |

No denial. PREFLIGHT: PASS.

### v2 cite → rebased line (re-located by symbol on the rebased tree; `46`'s `base line` at `51afdad0`)

Every symbol sits on the SAME line on the rebased tree as at `46`'s base (the setups code on `main` is patch-identical; nothing later on `main` touched these files).

| v2 cite | symbol | base line (`46`) | rebased line |
|---|---|---|---|
| `evaluate.py:340-364` (W3) | `class MemberEvaluation` | `:599-627` | `:599-627` |
| `evaluate.py:502` ([F-10] step 1) | `last_price = last_bar.close …` | `:920-921` (`base` `:922-926`) | `:921` (`base` `:922-926`) |
| `evaluate.py:517-524` | two `not_evaluable` returns | `:940-955` | `:942`, `:950` |
| `evaluate.py:529-534` (W1) | `intraday_staleness(...)` | `:960-965` | `:960-965` |
| `evaluate.py:598-599` | intraday `input_stale` return | `:1019-1021` | `:1019-1021` |
| `evaluate.py:624`, `:629` | daily `input_stale` returns | `:1072-1074`, `:1079-1082` | `:1072-1074`, `:1079-1082` |
| formed return | `result("formed", …)` | `:1119-1122` | `:1119-1122` |
| `evaluate.py:463-477` (W4) | `_factor_observations` `htf_level_proximity` | `:726-742` | `:695` def, `:726-742` |
| `evaluate.py:776-778`, `:803` | `refresh_card` entry fallback, return | `:1277-1279`, `:1299-1305` | `:1260` def, `:1277-1278`, `:1299-1305` |
| `evaluate.py:1043-1089`, `:1079` | `replay_receipt`, entry fallback | `:1544-1596`, `:1586` | `:1544-1596`, `:1586-1587` |
| `evaluate.py:1082` | `published_numbers` | `:1530-1541` | `:1530-1541` (called `:1589`, `:1940`, `:1991`) |
| `evaluate.py:1317-1349` | stage open-card loop | `:1823-1871` | `:1823-1871` (refresh `:1857`) |
| `evaluate.py:1384` | create call | `:1896-1897` | `:1896-1897` |
| `evaluate.py:928`, `:1253` | run payload / receipt version | `:1760`, `:1429` | `:1760`, `:1429` |
| — | `EVALUATOR_VERSION` / `DESK_FORMULA_VERSION` | `:160-161` | `:160-161` |
| — | `CardUpdate` | `evaluate.py:1223-1239` | `evaluate.py:1223-1239` (not in `store.py`) |
| `anatomy/freshness.py:106-120` | `intraday_staleness` | `radar/anatomy/freshness.py:106` | `radar/anatomy/freshness.py:106` |
| `scoring.py:254/264/265/312/319-330` | `suppression` / `proximity` / `card_score` / `CardScore` / `score_card` | `:255` / `:264` / `:274` / `:318` / `:329` | `:255` / `:264` / `:274` / `:318` / `:329` |
| `store.py:1016-1053` | `refresh_radar_card`, lock SELECT, taps-moved | `:1016`, `:1022-1026`, `:1029` | `:1016`, `:1024` (FOR UPDATE), `:1029` |
| `store.py:1182-1231` | `tap_dot`, suppression write | `:1182`, `:1220-1229` | `:1182`, lock `:1194`, `:1223-1224` |
| `cards/radar.py:167-183` | `ladder_order` | `:167` | `:167` |
| `audit_export.py:363` | `export_replay` scorer | `:364-365` | `:364` |
| `audit_export.py:244-259` | `export_run` replay + mismatch | `:245-260` | `:245-260` |
| `formations.py:145-149` | `SUPPORTED_EVALUATORS` / gate | `:83`, `:147` | `:83`, `:147` |
| `radar_panel.py:758` (X22) | `last=r.last_price` | `:758` | `:758` |
| `0007:255` | `shadow_agreement_v` | `0007:245-258`; `card_dot_taps` `:141-152` | `0007:245-258` (`WHERE t.engine_grade_at_tap IS NOT NULL` `:255`); `engine_grade_at_tap` `:147` |
| `0006:103-106` | `radar_score` / `radar_score_run` | `0006:66-87`, `:92-113` | `0006` `evaluator_version` `:76` |
| — | `shadow_agreement_v` placement | — | `placement.py:100` `Side.USER` |

## STEP-R

(1) PREFLIGHT report committed first: `[cards/stale-score-0922 9fb31e74] wip(stale-score): r2 PREFLIGHT before the rebase onto main` → `git status --porcelain` EMPTY. `git -C /Users/cobalt/cobalt log --oneline -1` re-read just before the rebase: `de48c19b` (unchanged).

(2) `git -C /Users/cobalt/cobalt-wt/stale-score rebase main` — exit 0, VERBATIM (35 skip lines condensed only in the middle; every line was `warning: skipped previously applied commit <sha>`):

```
warning: skipped previously applied commit 9b91667e
warning: skipped previously applied commit d31cf12a
… (33 more of the same shape) …
warning: skipped previously applied commit b007ce2e
warning: skipped previously applied commit 51afdad0
hint: use --reapply-cherry-picks to include skipped commits
hint: Disable this message with "git config set advice.skippedCherryPicks false"
Rebasing (1/3)Rebasing (2/3)Rebasing (3/3)Successfully rebased and updated refs/heads/cards/stale-score-0922.
```

No `CONFLICT` line. (3) not taken.

(4) PROOF:
- `git log --oneline -5` → `f17814c6 wip(stale-score): r2 PREFLIGHT before the rebase onto main` · `7bffdbcb wip(stale-score): STEP-2 partial — RED tests recorded; …` · `f0798537 test(cards): stale score STEP-1 first-gate experiments before S1 (v2 §7)` · `de48c19b docs(desk): 09-24 R71/R72 — …` · `b93718d0 docs(desk): 09-24 wake-up 8dda3057 — …`
- `git log --oneline HEAD..de48c19b` → no output (main tip is in HEAD)
- `git log --oneline de48c19b..HEAD` → exactly three lines (`f17814c6`, `7bffdbcb`, `f0798537`)
- `git diff --stat de48c19b -- src configs` → no output
- **`red <hash>` = `7bffdbcb`** (was `57925f3b`); STEP-1 `1a5c6928` → **`f0798537`**.

(5) RE-RUNS on the rebased tree (each `uv run pytest -q -s tests/experiments/stale_score/<module>`):
- X10: `X10: receipts=2 members=1 receipt_as_of=['2026-01-06T16:31:40+00:00'] rebuilt_as_of=['2026-01-06T16:31:40+00:00'] equal=True wall_clock=False` · `1 passed in 0.38s` — SAME as `46`.
- X18: `X18: fixed=False score_card_callers=4 on_score_last=0` — callers `audit_export.py:364`, `evaluate.py:1278`, `:1587`, `:1896`; old string `evaluate.py:160`, `formations.py:81` (comment), `:83`. X19: `X19: readers=2 compared_with_evaluator_version=0` (`evaluate.py:161`, `:1188`) · `2 passed in 0.15s` — SAME (no fifth caller).
- X20: `X20: reads_live_constant=True passes_that_value=True current_version_supported=True supported=['s2p2.2'] evaluator=s2p2.2` · X22: `X22: panel_calls_a_scorer=False scorers=[] last_site_display=True proximity_site_stored=True` · `2 passed in 0.13s` — SAME: `radar_panel.py` is NOT changed (R44).

(6) The `v2 cite → rebased line` table: under `## PREFLIGHT`.

(7) `grep -rn "score_last\|intraday_stale: bool" src/cobalt` → ONE hit `src/cobalt/radar/evaluate.py:696:    ext: ExtensionObservation, member: MemberInput, *, intraday_stale: bool, daily_ok: bool,` (the `_factor_observations` keyword; `score_last` absent), as `46` found. Version grep: `160:EVALUATOR_VERSION = "s2p2.2"` · `161:DESK_FORMULA_VERSION = "s2p2.1"` (+ `:1188`, `:1429`, `:1551`, `:1554`, `:1760`, `:2003`); `SUPPORTED_EVALUATORS` = `replay/formations.py:83` `frozenset({"s2p2.2"})`. **`main` carries `s2p2.2` (evaluator) / `s2p2.1` (desk) — the same strings `46` found; `46`'s T (vii) RED line `assert ('s2p2.2' == 's2p2.1'` still applies.** The bump is FROM these. `uv run cobalt jobs restarts de48c19b..HEAD` → 20 rows, every one `DOCS -` or `test/documentation; no resident -`; `RESTARTS: none`.

PROCESS NOTE (L35, stated plainly): between (7) and BASELINE I began STEP-2 C's `scoring.py` edit BEFORE BASELINE (out of the prompt's order). Caught before any run: every edit was reversed by hand and `git status --porcelain` printed EMPTY before BASELINE started, so BASELINE ran on the rebased tip exactly.

## BASELINE

`date` 17:12:08 ET. Tree = the rebased tip `f17814c6` (`git status --porcelain` EMPTY).

LIVE-NOTE (READ-ONLY, no lock): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (background) → `131 passed, 15 warnings in 24.99s`, exit 0; `SKIPPED` lines: 0 (`grep -c`). `AWAITING` lines VERBATIM:

```
AWAITING A RULING: backside
AWAITING A RULING: fashionably-late
AWAITING A DAY: hitchhiker
AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)
```

= R56's known state exactly (131 passed, 0 failed, no skip naming `COBALT_LIVE_VAULT_ROOT`, the four `AWAITING` lines).

OFFLINE: `uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider` (background) → summary VERBATIM: `15 failed, 2503 passed, 361 skipped, 1 xfailed, 15 warnings in 509.42s (0:08:29)` (exit 1). Every failure location is `tests/cobalt/test_stale_score.py` (`:91`, `:105`, `:120`, `:155`, `:181`, `:200`, `:226`, `:246`, the pydantic `AttributeError` of (vi), `:272`, `:302` ×2, (ix)'s `DID NOT RAISE`, (xi)'s `AttributeError`, `:406`) — exactly `46`'s 15 named REDs; no other id. The two live-note tests (`test_catalyst.py:365`, `test_predicate.py:262`) skip here by design (`COBALT_LIVE_VAULT_ROOT not set`) and run in the live-note suite above. Against `46`'s base (`2482 passed, 361 skipped, 0 failed`): `main`'s later commits add tests; the 15 are this build's own.

WITH-DB (`date` 17:21:11; THE LOCK (a) `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` · (b) `No such file or directory` → `cp` → (c) EXACTLY one line `-rw-------  1 cobalt  staff  2186 Sep 24 17:21 /Users/cobalt/cobalt-wt/stale-score/.env`): `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` (background) → summary VERBATIM: `15 failed, 2856 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 599.06s (0:09:59)`. Failures: the SAME 15 locations in `tests/cobalt/test_stale_score.py` as offline — no other id, no DEV-DB seam, no lock/deadlock line. Deselected: 2 (`TestMigrationRoundTrip`'s two). The 6 skips: `test_cards_picks.py:383`, `:396` (P2 columns present — by design), `test_radar_evaluate.py:695`, `test_catalyst.py:365`, `test_predicate.py:262` (`COBALT_LIVE_VAULT_ROOT not set` — run by the live-note suite), `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC` not set). TABLE-SET probe `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`: PASSED (not among the failures, not skipped) — no stray table on `cobalt_dev`. NO `cobalt db` before or after. (d) `rm /Users/cobalt/cobalt-wt/stale-score/.env` → `ls` → `ls: /Users/cobalt/cobalt-wt/stale-score/.env: No such file or directory` — `.env: removed, proven gone (BASELINE)`.

BASELINE: GREEN for this purpose — exactly the 15 named REDs in all runs; live-note = R56's known state. Running expectation from here: offline `2503 passed / 15 failed / 361 skipped`, with-DB `2856 / 15 / 6 / 2 deselected`.

## STEP-1 (carried)

`46`'s STEP-1 closed 17/17 AS EXPECTED at `1a5c6928`, rebased as **`f0798537`**. Re-run on the rebased tree (STEP-R (5)), each SAME as `46`: X10 `…equal=True wall_clock=False` · X18 `fixed=False score_card_callers=4 on_score_last=0` (no fifth caller) · X19 `readers=2 compared_with_evaluator_version=0` · X20 `reads_live_constant=True … supported=['s2p2.2'] evaluator=s2p2.2` · X22 `panel_calls_a_scorer=False scorers=[] …` (→ no panel change, R44). The other thirteen (X27, X1, X5a, X5b, X6, X7, X8, X11, X12, X14, X15, X26 and X10's companions) are `46`'s record, cited (`stale-score-build-2026-09-23.md` `## STEP-1`).

## STEP-2

### T (RED)
`46`'s file `tests/cobalt/test_stale_score.py` (17 tests), committed RED at `7bffdbcb`. Re-quoted from BASELINE's offline run on the rebased tree (`15 failed`), beside `46`'s — every one the SAME failure:

| T | test | RED line on the rebased tree | same as `46`? |
|---|---|---|---|
| (iii) X1 | `test_x1_all_dots_tapped_on_stale_bars_scores_nothing_and_names_the_close` | `AssertionError: card_score 64 published on stale bars` | yes |
| (iii) X5a | `test_x5a_no_closed_bar_today_gives_no_proximity_not_the_maximum` | `AssertionError: proximity 1 from no bar` | yes |
| (i) | `test_intraday_stale_is_required_and_set_on_every_return_path` | `test_stale_score.py:120: AssertionError` (no field) | yes |
| (ii) | `test_score_last_is_none_iff_stale_and_raises_on_a_fresh_member_without_a_price` | `ImportError: cannot import name 'score_last' from 'cobalt.cards.scoring'` | yes |
| (ii) X18 | `test_every_score_card_caller_takes_its_last_from_score_last` | `AssertionError: [('audit_export.py', 364, 'score = score_card(dots, last=ev.last_price if ev.last_price is not None else trigger, trig...'), …]` | yes |
| (iii) | `test_score_card_with_no_last_nulls_proximity_and_score_and_keeps_dot_reasons` | `AttributeError: module 'cobalt.cards.scoring' has no attribute 'stale_reason'` | yes |
| (iv) X12 | `test_null_proximity_publishes_json_null_never_the_string_none` | `AssertionError: assert <class 'decimal.Decimal'> == (Decimal \| None)` | yes |
| (v) X6 | `test_htf_level_proximity_on_stale_bars_is_input_stale_with_no_engine_grade` | `AssertionError: assert (False is True)` | yes |
| (vi) X14 | `test_daily_missing_input_stale_with_a_fresh_close_keeps_proximity` | `AttributeError: 'MemberEvaluation' object has no attribute 'intraday_stale'` | yes |
| (vii) | `test_one_new_version_string_and_the_previous_is_not_supported` | `AssertionError: assert ('s2p2.2' == 's2p2.1'` | yes |
| (viii) | `…refuses_another_version_by_name_before_the_replay[None]` | `AssertionError: replay_receipt reached — the version gate must refuse first` | yes |
| (viii) | `…[s2p2.2]` | same | yes |
| (ix) X11 | `test_audit_replay_path_never_emits_proximity_one_for_a_member_without_a_price` | `Failed: DID NOT RAISE <class 'cobalt.radar.evaluate.EvaluateError'>` | yes |
| (xi) R38 | `test_r38_premarket_stale_bar_nulls_and_the_next_bar_lifts_it_with_no_tap` | `AttributeError: 'MemberEvaluation' object has no attribute 'intraday_stale'` | yes |
| (xii) X27 | `test_stale_card_stage_and_replay_reason_are_byte_identical` | `AssertionError: assert (Decimal('0.919355') is None)` | yes |
| (x) R37+R41 | `test_r37_r41_…` | GREEN-as-pin | yes |
| (viii) guard | `test_audit_export_same_version_run_still_exports` | GREEN by design | yes |

No test was rewritten.

### C
Four source files, the narrowest change:
- `src/cobalt/cards/scoring.py`: `stale_reason(ev)`, `score_last(ev)` (raises `EvaluateError`, lazily imported — `evaluate` imports this module; `cards/store.py:897`'s lazy `OpenRadarCard` import is the precedent), `score_card(…, last: Decimal | None, stale_reason=None)` (a None `last` needs its reason, a price none — `ValueError` otherwise), `CardScore.proximity: Decimal | None`, `PROXIMITY_UNKNOWN = "bars stale — no proximity"`, `ET`.
- `src/cobalt/radar/evaluate.py`: `MemberEvaluation.intraday_stale: bool` (required, no default); computed right after `last_price` and carried in `base` (every return path); the old computation after the frames is removed; `htf_level_proximity` `stale=intraday_stale`; `refresh_card`, `replay_receipt` and the create call on `last=score_last(ev), stale_reason=stale_reason(ev)` — the two `card.entry` fallbacks DELETED; `CardUpdate.proximity: Decimal | None`; `published_numbers` JSON null; `EVALUATOR_VERSION = DESK_FORMULA_VERSION = "s2p2.3"` (bumped FROM `s2p2.2` / `s2p2.1`, the strings `main` carries).
- `src/cobalt/radar/audit_export.py`: the `[F-08]` version gate in `export_run` (every receipt of the chain; missing or ≠ `EVALUATOR_VERSION` → `AuditExportError` naming both versions, before the hash checks and before `replay_receipt`); the `--replay` scorer on `score_last` — the `else trigger` fallback DELETED; candidate `proximity` JSON null; `FORMULAS_IN_WORDS["proximity"]` names the null.
- `src/cobalt/replay/formations.py`: `SUPPORTED_EVALUATORS = frozenset({"s2p2.3"})` (previous string not kept).
- `src/cobalt/cards/store.py`: NOT touched — `CardUpdate` lives in `evaluate.py` (`46`'s table), so step 6 needs no `store.py` edit. `radar_panel.py`: NOT touched (X22).

`uv run pytest -q tests/cobalt/test_stale_score.py -p no:cacheprovider --tb=line` → `17 passed in 5.72s`.

X18 re-run (`uv run pytest -q -s tests/experiments/stale_score/test_x18_x19_callers.py`): `X18: fixed=True score_card_callers=4 on_score_last=4` — `audit_export.py:375`, `evaluate.py:1285` (`refresh_card`), `:1593` (`replay_receipt`), `:1902` (create), every one `last=score_last(ev), stale_reason=stale_reason(ev)`; old string left only in `formations.py:83` (a comment); `X19: readers=2 compared_with_evaluator_version=0` (`DESK_FORMULA_VERSION = "s2p2.3"` is its own literal) · `2 passed`.

R38 — NO session gate in the path: `intraday_staleness(*, observed_at, as_of, scan_interval)` (`radar/anatomy/freshness.py:106-120`) takes no session and no clock; `grep -rn "session\|RTH\|is_rth"` on that file hits only the DAILY rule's lines (`:25`, `:136-150`).

### A1
| test | old assertion | new assertion | why |
|---|---|---|---|
| `tests/cobalt/test_replay_runner.py:418` | `assert result.formation_replay == "s2p2.2"` | `assert result.formation_replay == "s2p2.3"` | the version singleton, `[F-08]` (vii) |
| `tests/cobalt/test_replay_runner.py:472` | `assert result.formation_replay == "s2p2.2"` | `assert result.formation_replay == "s2p2.3"` | same |

| `tests/cobalt/test_setups_d1.py:157` `_unmoved` — the shared normaliser behind `test_f11_nothing_but_health_moves_in_any_evaluation[countertrend\|full\|mixed\|shipped]` (`:207`), `test_setups_registries.py::_evaluation_dump` (→ 4 reds at `:190`) and `test_rubberband_forms.py::_non_formed` (→ `test_t6_non_formed_evaluations_are_byte_identical`, `:504`) | the dump = `ev.model_dump` minus `F11_MOVES` | also minus `intraday_stale` (the ADDED required field, [F-10]) and, on an intraday-stale evaluation, `observations.htf_level_proximity.stale` mapped back to `False` where the computed branch wrote it (the one carrying `inputs.last_price`) — v2 §2 C step 5, X6. The PINNED sha256 literals are unchanged and all match again | the file's own re-point pattern (`by_side` "added", `ema9` "mapped back") — same pins, same objects, only the two named by-design changes removed |

The 9 reds of the 17:33 offline run (`9 failed, 2509 passed, 365 skipped`, before the `_unmoved` re-point) were exactly these hashes; after it, `uv run pytest -q tests/cobalt/test_setups_d1.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_registries.py -p no:cacheprovider --tb=short` → `85 passed, 6 skipped in 202.43s`. A red that was NOT by design: none. `DEF_WRITTEN_*` pins untouched; the seam pin untouched.

EMPTY DIFFS (each its own call, "no output"): `git diff de48c19b -- src/cobalt/cards/health.py` (R42) · `git diff de48c19b -- src/cobalt/aset/radar_panel.py` (R44) · `git diff de48c19b -- tests/cobalt/test_radar_panel_cards.py` (seam pin) · `git diff de48c19b -- src/cobalt/cards/radar.py` (R37/R41).

### D
One paragraph each, appended: `docs/40 - DevDocs/cobalt/cards/scoring.md`, `…/radar/evaluate.md`, `…/radar/audit_export.md`, `…/replay/formations.md` (`## 2026-09-24 — stale score S1 …`).

### SUITE
- OFFLINE, first run 17:33 (before the `_unmoved` re-point): `9 failed, 2509 passed, 365 skipped, 1 xfailed, 15 warnings in 517.28s (0:08:37)`. The 9 were the A1 hashes above. The +4 skips were STEP-4's DB test file, drafted early; it is now parked as a docstring stub until STEP-4 (its full text is kept in scratch, so this step's suite lines are STEP-2's alone).
- OFFLINE, re-run 17:42:38 (`uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider`): **`2518 passed, 361 skipped, 1 xfailed, 15 warnings in 544.46s (0:09:04)`**, **0 failed**. Against BASELINE: `failed` 15 → 0 (the fifteen named), `passed` 2503 → 2518 (+15 = those fifteen; STEP-2 adds no new test), `skipped` 361 = 361.
- WITH-DB, inside THE LOCK (`## LANE` 17:42): `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` → **`2871 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 610.59s (0:10:10)`**, **0 failed**. That is 2856 + 15, with the same 6 skips and 2 deselected. The table-set probe (`test_migrate_proof.py`) passed: no line names it. No `cobalt db`. (d) `rm` → `ls: /Users/cobalt/cobalt-wt/stale-score/.env: No such file or directory`, so `.env` was removed and proven gone (STEP-2). The offline re-run started 12 s before this `cp`, and its unchanged 361 skips prove it stayed offline. From now on the offline and with-DB runs are not overlapped.

### COMMIT
`git status` (long) showed the 12 paths staged by name. `.env` was absent, and ignored if present. `[cards/stale-score-0922 d0274dc0] feat(cards): stale score S1 — intraday_stale, score_last, null proximity, reason, version gate (v2 §2 C 1–7, [F-08]; R37 R38 R41 R44)`. `git show --stat HEAD` → exactly the 12 named paths: the 4 DevDocs, this report, `scoring.py`, `audit_export.py`, `evaluate.py`, `formations.py`, `test_replay_runner.py`, `test_rubberband_forms.py`, `test_setups_d1.py` (`12 files changed, 364 insertions(+), 40 deletions(-)`).

## STEP-3

Modules (each its own, `tests/experiments/stale_score/`, run as `COBALT_ENV=dev uv run pytest -q -s tests/experiments/stale_score/<module>` inside THE LOCK, rows created inside the suite's rollback transaction — the folder's `conftest.py` re-exports `dev_db_tx`; nothing committed). Shared construction: `tests/cobalt/stale_db_support.py` (a `DevWorld` on the real `cobalt_dev` stores: one pool, one member, the S5 stage, bars FED by the test so a scan with no newer bar is stale by construction; `SCAN = 100`, this module's own constant, handed to the stage as a constructed `radar.scan_interval` row — L32/L69) and `tests/experiments/stale_score/stale_predicates.py` (X25's predicate and X30's bound, as SQL, with the `file:line` of every column). A "pre-C1" card = a formed card with its `assumed_formation` dot row deleted inside the transaction (v2 §1b: the only shape whose score is live when fresh). Run on STEP-2's commit (S1 built, S2 not): the modules that S2 flips assert S1's behaviour now and S2's after (`stale_db_support.s2_built()`). Each run had its own lock take (`## LANE` STEP-3 row: 14 takes, 17:53–17:55, every (a) `no matches found`, (b) `No such file`, (c) exactly our line, and (d) `No such file or directory`).

### X2
`X2: AS EXPECTED` (on S1). Output: `X2: s2_built=False fresh_score_present=True stale_proximity_null=True stale_score_null=True stale_reason_is_sentence=True tap_score_null=True tap_reason_kept=False tap_reason_after=None back_proximity_present=True back_score_present=True` · `1 passed in 0.58s`. The stale scan gives NULL proximity, NULL score and the sentence. A tap keeps the score NULL, but ERASES the sentence (`None`): this is `[F-06]`'s defect, which STEP-4 T (i) fixes. A fresh bar brings the score back with no tap.

### X3
`X3: AS EXPECTED` (W9 on S1). Output: `X3: s2_built=False taps_moved=True update_proximity_null=True row_proximity_null=True row_score_null=False row_reason_is_update_reason=False` · `1 passed in 0.39s`. The taps-moved branch leaves a live score (computed on the old, fresh proximity) beside a NULL proximity. STEP-4 T (ii) fixes it. First attempt: `CheckViolation … aset_sizings_radar_provenance`. My helper had left `radar_score_id` None, whereas the stage stamps it (`evaluate.py:1859`). That was a TEST-construction defect: the helper now stamps the card's own seam id, and the re-run passed.

### X13
`X13: AS EXPECTED` (on S1). Output: `X13: s2_built=False proximity_null=True score_null_after_tap=True reason_byte_identical=False reason_after=None` · `1 passed in 0.44s`. A tap while proximity is NULL keeps the score NULL, but the sentence is not kept (→ STEP-4).

### X16
`X16: AS EXPECTED`. Output: `X16: refreshed=True last_price_kept=True proximity_null=True score_null=True reason='bars stale — no closed bar'` · `1 passed in 0.40s`. With no bar this scan and the previous `last_price` 5.25 (this test's own construction), the column still holds 5.25 (`COALESCE`), proximity is NULL, and the reason is the no-bar sentence.

### X21
`X21: AS EXPECTED`. Output: `X21: pre_change_tap_engine_grade_present=True pairs_before=1 dot_engine_grade_after_stale_scan=None stale_tap_engine_grade_at_tap=None pairs_after=1 pre_change_tap_still_in_view=True` · `1 passed in 0.43s`. Once the stale scan has refreshed the dots, the `htf_level_proximity` dot carries no engine grade. A tap then records `engine_grade_at_tap` NULL and adds no pair. The earlier fresh-graded tap is still in `shadow_agreement_v`.

### X23
`X23: AS EXPECTED`. Output: `X23: survives_to_next_day_scan=True expired_by_that_scan=True state_after=EXPIRED published_proximity=None published_score=None reason='bars stale — no closed bar'` · `1 passed in 0.41s`. The card survives to the next trade date's first scan and is refreshed there (the refresh runs before the expiry in the stage loop), then expires on that same scan by its deadline. On `main` that one refresh published the `card.entry` fallback's proximity 1 (X5a), so ESCALATE 1 of the tribunal is a terminal-card artifact: one scan, then EXPIRED.

### X24
`X24: AS EXPECTED` (measurement). Output: `X24: ticker_days=660 with_missing_minutes=1 share=0.0015151515151515152 min_minutes=389 max_minutes=390 full_session=390 zero_volume_i1_bars=0 thinnest5_minutes=[390, 390, 390, 390, 390] thinnest5_zero_volume_minutes=[0, 0, 0, 0, 0] premarket_ticker_days=660 premarket_with_missing_minutes=629 premarket_min_minutes=11 premarket_full=330` · `1 passed in 0.46s`. Counts only (L32). Minutes with no prints are NOT stored as bars: there are no zero-volume bars anywhere, and 629 of 660 premarket ticker-days miss minutes (the minimum is 11 of 330). So a thin name's premarket `—` will be frequent, as v2 X24 foresaw. R38 "A" already ruled the every-session clock, so this is recorded, not re-opened (the first two runs of the module measured RTH only; the third added the premarket count).

### X9 (`cobalt_dev` half)
`X9: AS EXPECTED` (measurement). Output: `X9: cobalt_dev radar_cards=0 stale_seam_with_live_score=0`. `cobalt_dev` holds no committed radar card, so zero says nothing about production. The production half is the desk's (L41).

### X25 (`cobalt_dev` half)
`X25: AS EXPECTED` (measurement). Output: `X25: cobalt_dev htf_taps_with_engine_grade=0 stale_graded=0 stale_graded_pre_fix=0`. The production half is the desk's.

### X28 (`cobalt_dev` half)
`X28: AS EXPECTED` (measurement). Output: `X28: cobalt_dev receipts=0 proximity_one_on_stale_seam=0`. The production half is the desk's.

### X30
`X30: AS EXPECTED — decision (A)`. Output (`COBALT_ENV=dev uv run pytest -q -s tests/experiments/stale_score/test_x30_r40_discriminator_db.py`): `X30: seam_labels={'A': 'formed', 'B': 'input_stale', 'C': 'input_stale', 'D': 'input_stale'} x25_matched=['B', 'C', 'D'] x30_matched=['B', 'D'] post_fix_version=s2p2.3 pre_fix_versions=['s2p2.1', 's2p2.2'] post_fix_never_matched=True daily_missing_over_excluded=True decision=A` · `1 passed in 0.67s`. The one log line was expected: `ERROR … radar S5 daily bars for ZZX30 failed: failed: FileNotFoundError: no cached daily bars for ZZX30`, which is case D's constructed daily outage.
- **Join path** (`stale_predicates.py`, every column stored): `card_dot_taps.card_id` (`0007_radar_cards.sql:144`) → `aset_sizings.pool_member_id`, `trade_def_md5` → `radar_membership.pool_key` → the latest COMPLETE `radar_score_run` of that pool with `started_at <= t.at` (`0006_radar_score.sql:66-83`; `started_at` is the scan instant, `evaluate.py:1759`) → `radar_score` (`run_id`, `membership_id`, `trade_def_md5`, `evaluation`; `0006:92-109`). The user side can read all three system tables (`0006:198-200`, `0004:60`); `radar_cards_v` already joins across the same way (`0007:214-233`).
- **Stored pre-fix discriminator:** `radar_score_run.evaluator_version` (`0006:76`, written per run at `evaluate.py:1760`). It is bounded to the set of every `EVALUATOR_VERSION` in the code's history (`git log -G"^EVALUATOR_VERSION = " -- src/cobalt/radar/evaluate.py`: `s2p2.1`, `s2p2.2` only). A tap in a run at this code's version (`s2p2.3`), or at any later one, is provably never matched (C).
- **Over-exclusion, named (accepted: it only removes rows):** a pre-fix run whose `input_stale` meant "daily bars missing" (W3's second meaning) is matched too (D). The seam row carries no field that separates the two meanings.
- **Under-exclusion, named:** a card refreshed under an EDITED def (R2-4) has its seam rows under the current def's md5. The join keys on the card's formation md5 and misses them.
- **Decision table → (A):** the join is sound and a stored pre-fix discriminator exists. STEP-4 builds R40 as ONE additive migration, **`0015`** (SETTLED, L72 P-b).

### COMMIT
`[cards/stale-score-0922 3894d1a1] test(cards): stale score STEP-3 first-gate experiments before S2 + X30 (v2 §7; R40)`. `git show --stat HEAD` lists only the 14 named paths: this report, `tests/cobalt/stale_db_support.py`, `tests/experiments/stale_score/stale_predicates.py`, and the 11 `test_x*_db.py` modules. Result: `14 files changed, 751 insertions(+), 3 deletions(-)`.

## STEP-4

X30 decided (A), so STEP-4 builds the two writers AND migration `0015`.

### T (RED)
File: `tests/cobalt/test_stale_score_db.py`, 8 tests, `requires_db`, all inside the suite's rollback transaction; `0015` only inside rolled-back transactions. It was run on STEP-3's commit `3894d1a1` (`src/` = STEP-2's), inside THE LOCK (17:57): `COBALT_ENV=dev uv run pytest -q tests/cobalt/test_stale_score_db.py -p no:cacheprovider --tb=line` → `8 failed in 1.78s`. RED lines VERBATIM:

| T | test | RED line |
|---|---|---|
| (i) `[F-06]` | `test_a_tap_while_proximity_is_null_keeps_the_stored_sentence_and_publishes_no_score` | `AttributeError: 'NoneType' object has no attribute 'encode'` (the tap wrote `score_suppressed` NULL, erasing the sentence) |
| (i) `[F-06]` no stored sentence | `test_a_tap_while_proximity_is_null_and_no_sentence_is_stored_writes_proximity_unknown` | `AssertionError: assert (None is None and None == 'bars stale — no proximity')` |
| (ii) X3 | `test_taps_moved_with_a_null_proximity_writes_a_null_score_and_the_stale_reason` | `AssertionError: card_score 66 beside a NULL proximity` / `assert 66 is None` |
| (iii) **R45** | `test_r45_a_tap_racing_a_fresh_scan_scores_the_taps_conviction_on_this_scans_proximity` | `AssertionError: card_score 60 beside proximity 0.849462: expected 56 (the tap's conviction on this scan's proximity)` / `assert 60 == 56` (engine outputs of this run, copied verbatim; the test asserts the relation `card_score(tap conviction, this scan's proximity, locked reason)`, not these numbers) |
| (iv) registry | `test_0015_is_registered_after_0013_and_its_rollback_first` | `AssertionError: assert PosixPath('…/0013_tunables_slug_nullable.sql') == (PosixPath('…/db_migrations') / '0015_shadow_agreement_stale.sql')` |
| (iv) forward ×2 / rollback | `test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction` | `assert (' SELECT user...ext))::date);' == …) and 'evaluator_version' in " SELECT user_id, …"` (no exclusion yet) |
| (iv) behaviour | `test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones` | `FileNotFoundError: … '…/db_migrations/0015_shadow_agreement_stale.sql'` |
| (iv) X25 = drop | `test_r40_on_cobalt_dev_the_view_drops_exactly_x25s_pre_fix_count` | `FileNotFoundError: … '…/0015_shadow_agreement_stale.sql'` |

Deviation, stated (not built around): T (iv)'s VIEW-BEHAVIOUR tests apply `0015`'s text on the user-side connection that the stores share, i.e. inside the suite's own rolled-back transaction. That follows `test_assumed_store.py:258-278`'s precedent, and the seeding is done by the real stage. They do not seed through `db.apply_side` on `connect_migration`, because a hand-seeded radar `aset_sizings` row must satisfy about 20 NOT NULL / CHECK columns (`0007:66-82`). The forward-twice / rollback-restores-0007 test DOES use the prescribed `connect_migration` + `autocommit = False` + `_apply` + `conn.rollback()` in `finally` shape. Nothing is committed either way (L76).

### C
- `src/cobalt/cards/store.py` `tap_dot`: the lock SELECT also reads `score_suppressed`. While proximity is NULL: `suppressed = stored or PROXIMITY_UNKNOWN`, and `card_score` stays NULL (the existing `card_score()` guard). Conviction and the proposed key update as before ([F-06]).
- `src/cobalt/cards/store.py` `refresh_radar_card`: the lock SELECT also reads `conviction, score_suppressed`. The taps-moved branch computes `suppressed = update.score_suppressed if update.proximity is None else locked_score_suppressed` and `score = card_score(locked_conviction, update.proximity, suppressed)`, and its UPDATE also sets `card_score = %s, score_suppressed = %s`. That is R45 in Fable (i)'s words. One formula (`card_score()`), no SQL arithmetic.
- `src/cobalt/db_migrations/0015_shadow_agreement_stale.sql` + `.rollback.sql`: X25's predicate plus the stored discriminator (`radar_score_run.evaluator_version IN ('s2p2.1','s2p2.2')`) as a `NOT EXISTS` exclusion, with 0007's column list. The rollback is 0007's view, exact. Both are idempotent `CREATE OR REPLACE` + `ALTER VIEW … OWNER TO cobalt_user`.
- `src/cobalt/db_migrations/__init__.py`: registered in `FORWARD` after `0013` and in `REVERSE` before `0013`'s rollback, plus the docstring lines on `0008`'s pattern (including the `0014` / `0016–0018` seam note). `placement.py` is NOT changed: `shadow_agreement_v` stays `Side.USER` (`placement.py:100`), and no test says otherwise.
- `scoring.py`: not touched at STEP-4 (`PROXIMITY_UNKNOWN` was already defined at STEP-2).

### A1
| test | old assertion | new assertion | why |
|---|---|---|---|
| `test_archiver_migrations.py:80` | `FORWARD[-5:]` = 0008…0013 | `FORWARD[-6:]` = 0008…0013, `0015_shadow_agreement_stale.sql` | `0015` registered (R40, X30 (A)); every old name kept |
| `test_archiver_migrations.py:93` | `REVERSE[:5]` = 0013…0008 rollbacks | `REVERSE[:6]` = `0015…rollback`, 0013…0008 | same |
| `test_archiver_migrations.py:117` | `_rollback_paths("0009") == [0013, 0011, 0010]` | `== [0015, 0013, 0011, 0010]` | same (exact list, same strength) |
| `test_archiver_migrations.py:123` | `_rollback_paths("0007") == [0013 … 0008]` | `== [0015, 0013 … 0008]` | same |
| `test_archiver_migrations.py:146-147` | `numbers == [*range(1, 12), 13]`; `numbers[-3:-1] == [10, 11]` | `numbers == [*range(1, 12), 13, 15]`; `numbers[-4:-2] == [10, 11]` | same (exact list; the archiver pair's slice shifted by the one added file) |
| `test_assumed_store.py:244-245` | `FORWARD[-1]` / `REVERSE[0]` = `0013` | `FORWARD[-1]` / `REVERSE[0]` = `0015`, plus `FORWARD[-2]` / `REVERSE[1]` = `0013` | prompt: re-pointed to `0015`, the `0013` membership pins (`:242-243`) kept |
| `test_p4_migrations.py:101` | `_rollback_paths("0007") == [0013 … 0008]` | `== [0015, 0013 … 0008]` | same |
| `test_p4_migrations.py:111` | `above_0009 == [0013, 0011, 0010]` | `== [0015, 0013, 0011, 0010]` | same |
| `test_p4_migrations.py:117` | `_rollback_paths("0008") == [0013 … 0009]` | `== [0015, 0013 … 0009]` | same |
| `test_tenancy.py:514` | `selected[:5] == [0013 … 0008]` | `selected[:6] == [0015, 0013 … 0008]` | same |
| `test_radar_migration.py:34` | `[:5] == [0013 … 0008]` | `[:6] == [0015, 0013 … 0008]` | same |
| `test_radar_score_migration.py:103-121` | `newest_four` (5 names) at `[:5]` ×3 | + `0015…rollback` at the head, `[:6]` ×3 | same |

`test_migrate_proof.py:1528` (`_rollback_paths("0005")[0]`) is generic (it takes whichever file reverses first) and was left unchanged. No `test_radar_cards_db.py` assertion pinned the taps-moved or `tap_dot` behaviour that changed: every card there carries the `assumed_formation` dot, so its score is NULL on both code paths.

### D
Appended: `docs/40 - DevDocs/cobalt/cards/store.md` (the two branches), `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` (`0015`).

### SUITE
- OFFLINE, first run 17:59 (collected before the `test_archiver_migrations.py:146` re-point): `1 failed, 2517 passed, 369 skipped, 1 xfailed, 15 warnings in 527.13s (0:08:47)`. The one failure was `tests/cobalt/test_archiver_migrations.py:146: AssertionError` (`1…11 then 13, got [1, …, 11, 13, 15]`), the by-design registry pin (A1 above). It was re-pointed at 18:00, and `uv run pytest -q tests/cobalt/test_archiver_migrations.py -p no:cacheprovider --tb=short` → `53 passed, 10 skipped`. The skips went +8 (361 → 369): `test_stale_score_db.py`'s 8 `requires_db` tests skip offline.
- WITH-DB, inside THE LOCK (`## LANE` 18:00): `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` → **`2879 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 608.80s (0:10:08)`**, **0 failed**. That is 2871 + the 8 new `test_stale_score_db.py` tests, all GREEN; the 6 skips are the same, and 2 deselected. The run started AFTER the archiver re-point, so it carries it. Every existing rollback-transaction test now also applies `0015` inside its own transaction and stayed green: `test_archiver_migrations.py` `test_forward_creates_both_tables_on_the_system_side`, `test_migrate_twice_is_idempotent_for_the_two_new_tables`, `test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4`; `test_p4_migrations.py` `test_0008_0009_apply_twice_reverse_and_reapply_on_populated_membership[p2_before_p4\|p4_before_p2]`, `test_side_roles_ownership_identity_guc_and_wrong_side_through_real_roles`, `test_missed_rerun_reconciles_in_the_ruled_order_against_the_live_unique_index` (none is in a failure line; none is skipped). The table-set probe `test_migrate_proof.py` passed. No `cobalt db`; `0015` was never committed (proven at CLOSE by XL76). (d) `rm` → `ls: …/.env: No such file or directory`, so `.env` was removed and proven gone (STEP-4).
- OFFLINE re-run 18:11 (after the lock was released; `uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider`): **`2518 passed, 369 skipped, 1 xfailed, 15 warnings in 510.19s (0:08:30)`**, **0 failed**. `passed` is 2518, unchanged: STEP-4's 8 new tests are `requires_db` and skip offline. `skipped` is 361 + 8 = 369.
- R45 GREEN: `test_r45_a_tap_racing_a_fresh_scan_scores_the_taps_conviction_on_this_scans_proximity` passed. R40 GREEN: the four T (iv) tests passed, including `…drops_exactly_x25s_pre_fix_count`, which asserts that X25's `cobalt_dev` pre-fix count (0) equals the number of pairs the view drops.

### COMMIT
By explicit paths: `store.py`, `db_migrations/__init__.py`, the `0015` pair, `test_stale_score_db.py`, the 7 re-pointed test files, the 2 DevDocs, this report. The commit sha and `git show --stat HEAD` are recorded under `## STEP-5` (the commit carries this text).

## STEP-5

## EXPERIMENTS

`46`'s STEP-1 (17, by reference, `stale-score-build-2026-09-23.md` `## STEP-1`): X10, X27, X1, X5a, X5b, X6, X7, X8, X11, X12, X14, X15, X18, X19, X20, X22, X26 — each AS EXPECTED. X10, X18/X19 and X20/X22 were re-run on the rebased tree with the same result (STEP-R). X18 was re-run again after STEP-2 C with the flip (`on_score_last=4`).

This run:

## OWNER RULINGS AS BUILT

| ruling | test `file::name` | RED line | GREEN |
|---|---|---|---|
| R37 SINK (A) | `tests/cobalt/test_stale_score.py::test_r37_r41_a_null_watch_card_sinks_below_every_scored_one_and_nulls_order_by_pool_position` | GREEN-as-pin by design (`ladder_order` untouched; `git diff de48c19b -- src/cobalt/cards/radar.py` no output) | passed at STEP-2 (`17 passed`) |
| R38 PREMARKET (A) | `…::test_r38_premarket_stale_bar_nulls_and_the_next_bar_lifts_it_with_no_tap` | `AttributeError: 'MemberEvaluation' object has no attribute 'intraday_stale'` | passed at STEP-2; no session gate in `intraday_staleness` (`freshness.py:106-120`) |
| R39 TWO CLOCKS (A) | X15 (`46`, `test_x15_two_clocks.py`): the two clocks disagree both ways | — (measurement) | `46`'s X15 AS EXPECTED; `git diff de48c19b -- src/cobalt/radar/poller.py` at CLOSE |
| R40 EXCLUDED (B) | X30 decided (A). Then `tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones`, `::test_r40_on_cobalt_dev_the_view_drops_exactly_x25s_pre_fix_count`, `::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction`, `::test_0015_is_registered_after_0013_and_its_rollback_first` | `FileNotFoundError: … 0015_shadow_agreement_stale.sql` (×2); `assert (' SELECT user...' == …) and 'evaluator_version' in …`; `assert PosixPath('…0013…') == …/'0015_shadow_agreement_stale.sql'` | all four passed in the STEP-4 with-DB suite (`2879 passed`); `0015` never committed (XL76 at CLOSE) |
| R41 TIES (A) | the R37 test (NULL ties fall to `pool_position`: `[4, 2, 3, 1]`) | GREEN-as-pin | passed at STEP-2 |
| R42 PILLS UNCHANGED (A) | `git diff de48c19b -- src/cobalt/cards/health.py` | — | no output (STEP-2, CLOSE) |
| R43 WHEN THE LADDER MOVES (A) | X29 (STEP-5) | — (measurement) | see STEP-5 |
| R44 THE LOOK (A) | X22 re-run at STEP-R (`panel_calls_a_scorer=False`) + `git diff de48c19b -- src/cobalt/aset/radar_panel.py` + the seam pin `test_radar_panel_cards.py` untouched and GREEN | — | no output; seam pin green in every suite |
| R45 FRESH TAP RACE (B) | `tests/cobalt/test_stale_score_db.py::test_r45_a_tap_racing_a_fresh_scan_scores_the_taps_conviction_on_this_scans_proximity` | `AssertionError: card_score 60 beside proximity 0.849462: expected 56 (the tap's conviction on this scan's proximity)` | passed in the STEP-4 with-DB suite (`2879 passed`) |

## L52

- (a) Every number is traceable. Proximity comes only from a `last` that `score_last` returns (`src/cobalt/cards/scoring.py:354`), and all four callers of `score_card` use it (X18: `evaluate.py:1285`, `:1593`, `:1902`, `audit_export.py:375`). The three price fallbacks are deleted: `card.entry` twice and `trigger` once (CLOSE grep). A stale or absent `last` gives NULL plus a sentence that is a pure function of the evaluation (`scoring.py:342`), never a modelled value.
- (b) There is ONE authority. `card_score` orders WATCH (ADR-0009 D4). A NULL sinks by the existing nulls-last rule, and NULL ties fall to pool position; `cards/radar.py` `ladder_order` is unchanged (R37, R41). A tap cannot publish a number while proximity is NULL (STEP-4 `tap_dot`).
- (c) The seam is real artifacts:
  - the required field `MemberEvaluation.intraday_stale` (`evaluate.py:614`, set in `base` at `:938`);
  - the helper `score_last` and the sentence `stale_reason` (`scoring.py:354`, `:342`);
  - Optional proximity (`scoring.py:335`, `evaluate.py:1235`);
  - JSON null (`evaluate.py:1539`, `audit_export.py:385`);
  - the version singleton `s2p2.3` (`evaluate.py:162-163`, `replay/formations.py:84`) and the audit gate (`audit_export.py:218-226`);
  - `PROXIMITY_UNKNOWN` (`scoring.py:92`);
  - the two writer branches in `store.py` and, under X30 (A), the view migration `0015` (see STEP-4).
- (d) It is auditable. `audit-export` replays through the same helper and refuses another version by name before the replay (`test_stale_score.py` (viii)). The stage and replay texts are byte-identical (X27 / T (xii)), and the replay `as_of` is the receipt's (X10).

## CLOSE

## FOR THE DEPLOY

The deploy prompt's drafter copies these. This build runs none of them.
- **RESTARTS:** X17's table (STEP-5).
- **THE MIGRATION:** X30 decided (A), so there is one: `src/cobalt/db_migrations/0015_shadow_agreement_stale.sql` goes forward on production inside the deploy (`cobalt db migrate --allow-prod` is the deploy hub's, L61). The rollback file is `0015_shadow_agreement_stale.rollback.sql` (it restores 0007's view exactly). It is additive and view-only, with no data change. `FORWARD` order applies `0014` (H1, `43`) before `0015` if both ship in one set; `0016`/`0017`/`0018` belong to other branches. When H1 lands, its registry pins and this branch's (the `[:6]`/`[-6:]` lists and `numbers == [*range(1, 12), 13, 15]`) must be re-pointed together (L68 seam).
- **THE STACK (L68):** this branch is REBASED onto `de48c19b`, a descendant of `deploy-2026-09-24` = `a2d320b8`. Its deploy is rebase-then-ff (L54), or it goes as a sibling in the evening's stacked gate. Unmerged branches that share its paths: `## CLOSE` L68 table.
- **THE GATE (L68):** the deploy's integrated gate re-proves offline, with-DB and live-note on the combined tree. The with-DB gate takes the lock alone and MAY run `TestMigrationRoundTrip`; the deselect is this build's, under L76.
- **ROLLBACK:** the code revert (L54 / L68), plus the view rollback: `cobalt db migrate --rollback --down-to 0013`, which selects `0015`'s rollback alone as long as `0014` is not applied; with H1 applied, `--down-to 0014`.
- **THE VERSION GATE:** receipts written at `s2p2.3` are refused by the old code's `replay_receipt` (and by its audit's replay), and receipts at `s2p2.2` are refused by the new code's `audit-export` gate by name. So a rollback, or a run bundled across the cut, is refused rather than mis-replayed. Name this to the deploy's drafter.
- **THE PRODUCTION READS X9 / X25 / X28** are the desk's inputs to `44`, not the deploy's (L41). The SQL is `tests/experiments/stale_score/test_x9_stale_scored_cards_db.py` `X9`, `stale_predicates.py` `X25_TAPS` / `X30_TAPS`, and `test_x28_proximity_one_receipts_db.py` `X28`.

## FOR 44

The check packet carries the executed output of all three suites (L68). What to file-check:
- **The rebase:** `## STEP-R` (the verbatim output, the ancestry proof `HEAD..de48c19b` empty, and the re-runs).
- **One commit per step:** `## CLOSE` `git log`.
- **The seam artifacts:** `intraday_stale` on every return path (`evaluate.py:614`, `base` `:938`; T (i) covers 6 paths); `score_last` and X18's four callers; the three deleted fallbacks (CLOSE grep); the version singleton `s2p2.3` and the audit gate (`audit_export.py:218-226`, T (viii)).
- **STEP-4:** `tap_dot`'s branch and the taps-moved branch; the R45 race test (its RED line, then GREEN) and its code; X30's output and the decision taken; under (A), the `0015` pair and the rollback-transaction tests that prove it.
- **The experiments:** each one's line, with its verbatim output (`## EXPERIMENTS`).
- **The suites:** BASELINE's and CLOSE's three summaries (offline; with-DB with its deselect; live-note with its `AWAITING` lines), and the XL76 line.
- **The rest:** the empty-diff list, the restarts table, the L68 table, and the `## LANE` rows.
- **The A1 re-points:** the two version pins, and the shared `_unmoved` normaliser (`test_setups_d1.py:157`). Same pins, only the two by-design changes removed.

## LANE

| time (`date`) | (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` | (b) `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` | result |
|---|---|---|---|
| 17:08:17 (PREFLIGHT, for the record) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | pass (no copy yet) |
| 17:21:11 (BASELINE with-DB) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | pass → cp → (c) one line (ours) → run → (d) removed, proven gone |
| 18:00:4x (STEP-4 SUITE with-DB) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | pass → cp → (c) `-rw-------  1 cobalt  staff  2186 Sep 24 18:00 /Users/cobalt/cobalt-wt/stale-score/.env` → run → (d) removed 18:11, `No such file or directory` |
| 17:57 (STEP-4 T RED, `test_stale_score_db.py`) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | pass → cp → (c) `-rw-------  1 cobalt  staff  2186 Sep 24 17:57 /Users/cobalt/cobalt-wt/stale-score/.env` → run → (d) removed, `No such file or directory` |
| 17:53–17:55 (STEP-3: X2, X3 ×2, X13, X16, X21, X23, X24 ×3, X9, X25, X28, X30 — one take each, 14 takes) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` every time | `No such file or directory` every time | pass → cp → (c) exactly our one line → run → (d) removed, `ls` `No such file or directory` every time |
| 17:42:4x (STEP-2 SUITE with-DB) | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | pass → cp → (c) `-rw-------  1 cobalt  staff  2186 Sep 24 17:42 /Users/cobalt/cobalt-wt/stale-score/.env` → run → (d) removed ~17:53, proven gone |

## ESCALATE

1. **THE DESELECT (L76).** This build did not run `tests/cobalt/test_tenancy.py::TestMigrationRoundTrip`, because it commits every migration to `cobalt_dev`. The deploy's gate runs it.
2. **The version rule taken ([F-08]).** There is a separate bump on `main`'s string: `s2p2.2` / `s2p2.1` → `s2p2.3` for `EVALUATOR_VERSION`, `DESK_FORMULA_VERSION` and `SUPPORTED_EVALUATORS`, with the previous strings not kept. X20: the nightly binding reads the live constant, so no old binding is refused.
3. **The A1 re-points, one line each:**
   - `test_replay_runner.py:418`, `s2p2.2` → `s2p2.3`;
   - `test_replay_runner.py:472`, same;
   - `test_setups_d1.py:157` `_unmoved` (the shared normaliser behind D1's four F11 pins, the four registries pins at `test_setups_registries.py:190`, and `test_rubberband_forms.py` t6): minus the added `intraday_stale`, and the htf `stale` flag mapped back. The pinned hashes are unchanged.
   - STEP-4 registry pins, all with `0015` added at the head and every `0013` name kept: `test_archiver_migrations.py:80`, `:93`, `:117`, `:123`, `:146-147`; `test_assumed_store.py:244-247`; `test_p4_migrations.py:101`, `:111`, `:117`; `test_tenancy.py:514`; `test_radar_migration.py:34`; `test_radar_score_migration.py:103-122`.
4. **X9 / X25 / X28 production halves are the desk's (L41).** This build ran only the `cobalt_dev` halves: 0 / 0 / 0, because `cobalt_dev` holds no committed radar card, tap or receipt. The SQL to run read-only on production is in the three modules (named under `## FOR THE DEPLOY`).
5. **X30 decision (A), R40 built as `0015`.** Named over-exclusion (accepted, it only removes rows): a pre-fix run whose `input_stale` meant "daily bars missing" (W3) also drops its graded `htf_level_proximity` taps (X30 case D). Named under-exclusion: a card refreshed under an EDITED def (R2-4) has its seam rows under the current md5, and the join (formation md5) misses them. If the production X25 count shows such rows, a later migration can widen the join.
6. **L68 seams (unmerged branches sharing paths):** see the `## CLOSE` table. The registry pins are a seam with handicap H1 (`0014`) and with DRC D1 / voice V1 / DRC K1 (`0016`–`0018`). Whichever lands later re-points these same lists.
7. **X24 fact (not re-opened):** minutes without a print are NOT stored as bars. 629 of 660 premarket ticker-days on `cobalt_dev` miss minutes, and there are no zero-volume bars. A thin name's premarket `—` will therefore be frequent, as R38 "A" already ruled.
8. **T (iv) seeding deviation (stated):** the view-behaviour tests apply `0015` inside the suite's own rolled-back transaction (the `test_assumed_store.py:258-278` precedent, seeded by the real stage), not seeded through `db.apply_side` on `connect_migration`. The forward-twice / rollback test uses the prescribed `connect_migration` shape. Nothing is committed either way.
9. **Process note (L35).** STEP-2's `scoring.py` edit was begun before BASELINE, out of order. It was reversed by hand before any run (`git status --porcelain` empty), so BASELINE ran on the rebased tip.

## CONTINUE

next: STEP-5 (X4, X17, X29; drafts `test_x4_audit_stale_card.py`, `test_x29_ladder_render.py` in the folder; XL76 module written for CLOSE). STEP-4 SUITE done: offline 2518/0 (369 skipped), with-DB 2879/0; STEP-4 committed (see `### COMMIT`). (T RED recorded 17:57; C, A1, D written, uncommitted: store.py, 0015 pair, db_migrations/__init__.py, 7 re-pointed test files, test_stale_score_db.py, 2 DevDocs; offline run 17:59 `bpxw2jz50`, then the with-DB run inside THE LOCK — never overlapped), then COMMIT. STEP-3 committed `3894d1a1`; STEP-2 `d0274dc0`. STEP-4's T file parked as a stub (full text in `$CLAUDE_JOB_DIR/tmp/test_stale_score_db.py`). Earlier: the 17:33 offline run showed 9 reds outside `test_stale_score.py`; A1 in progress: `test_rubberband_forms.py` t6 + `test_setups_d1.py` `_unmoved` (shared normaliser: minus `intraday_stale`, htf `stale` mapped back) — subset re-run 17:38; then re-run the offline suite (C, A1, D written, uncommitted; `test_stale_score.py` 17 passed; offline suite running 17:33) then with-DB inside THE LOCK, then COMMIT by explicit paths (scoring.py, evaluate.py, audit_export.py, formations.py, test_replay_runner.py, the four DevDocs, this report). (BASELINE done: offline 2503/15, with-DB 2856/15 (2 deselected), live-note 131/0 = R56. Uncommitted drafts in the tree, NOT yet run: `tests/cobalt/stale_db_support.py`, `tests/cobalt/test_stale_score_db.py` (STEP-4 T), `tests/experiments/stale_score/stale_predicates.py` + the STEP-3 `*_db.py` modules; DevDoc STEP-2 paragraphs written. Scratch drafts: `$CLAUDE_JOB_DIR/tmp/0015_*.sql`, `t_iv_block.py`, `test_x29_ladder_render.py`.)

DONE: AUTHORIZATION (PASS), PREFLIGHT (PASS; `<main tip>` = `de48c19b`), STEP-R (rebase DONE — never redo: `red` = `7bffdbcb`, STEP-1 = `f0798537`, PREFLIGHT wip = `f17814c6`; re-runs X10/X18/X19/X20/X22 same as `46`).

(run in progress — step 5 of 5, next under ## CONTINUE)
