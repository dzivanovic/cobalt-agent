# archiver-429-1009 — build report (2026-10-09)

Card: `docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md` · BUILD-HUB.md · base `fa968552` · branch `ops/archiver-429-1009`

## §0 Headline

Built all 3 rows on `fa968552`, tip `188190dc`. A Finviz 429 is now its own error type (`FinvizRateLimited`, carrying `Retry-After`). The nightly run retries the same target at most 3 times. Every wait is at least 1.2 s and the run's waits add up to 600 s at most; a backfill never retries. `Run complete:` always says `retried <n> (waited <s> s)` and names the retried targets.
All three suites passed: offline 4143/0, with-DB 5032/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and `.env` is removed.
2 decisions, none for Dejan: RESTARTS lists `com.cobalt.aset` beside `com.cobalt.radar`, and on a 429 some failure text now reads `FinvizRateLimited:` where it read `CollectorError:`.

## L74

One system reminder asked for a `Claude-Session:` line on commits. It is recorded under `## RECORDS` and was not acted on.

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md"` (23:53 EDT), exit 0, output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md" · 0 · f772032da5559e1c8c36076ad5666494baecda09
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

Rows: rule · command · exit · output.

- MECHANICAL · `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · 0 · whole:
```
clock · date · 0 · Fri Oct  9 23:53:54 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/archiver-429-1009
    ?? "docs/40 - DevDocs/reports/archiver-429-build-2026-10-09.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · fa968552 docs(desk): https deploy card 208 drafted, three decisions asked of the brain
diff · git diff --stat fa968552 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/archiver-429-1009 · 0 · fa968552 docs(desk): https deploy card 208 drafted, three decisions asked of the brain
env here · ls /Users/cobalt/cobalt-wt/archiver-429-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- BASE · `git show --stat fa968552` · 0 · `fa968552 docs(desk): https deploy card 208 drafted, three decisions asked of the brain` — 4 files under `docs/40 - DevDocs/` (`208-deploy-https-card.md`, `cto-2026-10-09.md`, `https-deploy-fixround-draft-2026-10-09.md`, `https-only-fixround-2026-10-09.md`), 75 insertions, 1 deletion.
- SYMBOLS (each `grep -n -F`, exit 0):
  - `GENTLE_SLEEP_SECONDS` runner.py → `30:GENTLE_SLEEP_SECONDS = 1.2`, `76`, `120`, `265: await asyncio.sleep(GENTLE_SLEEP_SECONDS)`, `342: await asyncio.sleep(GENTLE_SLEEP_SECONDS)`
  - `class CollectorError` collector.py → `57:class CollectorError(RuntimeError):`
  - `async def ` collector.py → `78:async def resolve_token()`, `175:async def finviz_get(`, `219:async def fetch_bars(`
  - `def ` runner.py → `59:def _backfill_window`, `80:def _check_demand`, `182:async def _run_targets(`, `237:async def _upsert_targets(`, `303:async def _append_targets(`, `429:async def run_full()`, `445:async def run_backfill(`, `462:def _archive_nightly()`
  - `class RunSummary` report.py → `103:class RunSummary:`; `def append_run_report` → `228:def append_run_report(summary: RunSummary) -> Path:`
  - collector.py `:213–215` read: `response.raise_for_status()` / `except httpx.HTTPStatusError as e:` / `raise CollectorError(f"Finviz HTTP failed: {scrub(str(e))}") from e`; `:234–237` `except Exception as e: raise CollectorError(f"Fetch failed for {ticker}/{interval.value}: …") from e`
  - runner.py `:249` `bars = await fetch(ticker, interval, token)` (upsert), `:309` same (append), `:438–441` the `Run complete:` f-string, `:456` `Backfill complete:`, `:482–485` the `RuntimeError` join.
  - `radar/notes.py:368` `name="archiver", rpm=60 / GENTLE_SLEEP_SECONDS,`; `:349` `from cobalt.archiver.runner import GENTLE_SLEEP_SECONDS`
  - `configs/cobalt/jobs.yaml:205` `- label: com.cobalt.archiver` … `:214 timeout_s: 2400`, `:215 schedule: {at: "20:30", weekdays: [1, 2, 3, 4, 5]}`
  - tests: `test_archiver_runner.py:188 def run(`, `:196 def fetcher(`, `:208 def _no_sleep_no_token(`, `:284 test_upsert_keeps_the_run_report_row_byte_for_byte`, `:303 test_the_complete_list_of_upsert_mode_additions_is_pinned`; `test_archiver_collector.py:169 test_finviz_transport_reports_followed_redirect_before_status`
- CALLERS:
  - `grep -rn -F "fetch_bars(" src` → `runner.py:169 return await fetch_bars(ticker, interval, token)`, `collector.py:219` (def), `archiver/cli.py:331 return await fetch_bars(ticker, interval, token)`, `radar/throttle.py:175 await fetch_bars(ticker, Interval.I1, credential, on_metrics=observe)`, `replay/movers.py:393 … self._fetch_bars(…)` (an attribute, not this function's name)
  - `grep -rn -F "finviz_get(" src` → `collector.py:231`, `radar/collector.py:176`, `radar/collector.py:276`, `radar/propose.py:449`, `radar/throttle.py:196`
  - `grep -rn -F "CollectorError" src` → archiver only (`runner.py:22,255,310`; `collector.py` raises) plus `strike/measure.py:24` (a docstring). `grep -rn -F "except CollectorError" src` → `runner.py:255`, `runner.py:310` only.
  - `grep -rn -F "_run_targets(" src tests` → `runner.py:436` (run_full), `runner.py:453` (run_backfill), `tests/cobalt/test_archiver_runner.py:190`, `tests/cobalt/test_replay_demand.py:77`
  - `grep -rn -F "run_full(" src tests` → `runner.py:429` (def), `runner.py:473` (`_archive_nightly`)
- `wc -l`: collector.py 251 · runner.py 533 · report.py 277 · test_archiver_collector.py 193 · test_archiver_runner.py 924 · test_archiver_report.py 101.
- `## READ` names no report (no `tail -n 3` owed).
- CARD RECORDS, copied and re-read where my list reaches:
  - `logs/archiver.err` — re-read with Read: `:32431` `2026-10-09 20:35:38.041 | ERROR | cobalt.archiver.runner:_upsert_targets:257 - [231/1000] DKNG/i2: FAILED — Fetch failed for DKNG/i2: Finviz HTTP failed: Client error '429 Too Many Requests' …`; `:33220` `Run complete: 210 tickers, 3308843 rows, 18 failures, 24m13s`; `:33221` `F17: com.cobalt.archiver FAILED — RuntimeError: 18 archiver failure(s): DKNG/i2: …`. Holds.
  - Retry bound (X2) arithmetic: carried as the desk's; re-derived at W/FOR THE CHECK from the constants built.
  - `logs/radar.err:44531–44538`: not re-read (not needed by a row).
  - `git -C /Users/cobalt/cobalt diff --stat f5010068 HEAD -- src tests ops`: not re-run (not a listed shape for that form); the code read here at `fa968552` matches the card's line numbers (`runner.py:257` is the `logger.error` of `_upsert_targets`).
  - `tunables.yaml:782` → `- key: archiver.write_mode` (re-read at main).
  - RESTARTS expectation: run at RESTARTS.
  - Approval row R685: proven at AUTHORIZATION.
- `uv run cobalt jobs restarts fa968552..HEAD` · 0 · (it built the `.venv` first) the only row is the untracked report: `docs/40 - DevDocs/reports/archiver-429-build-2026-10-09.md	A	DOCS	-` · `RESTARTS: none`.
- PROVEN BY FIRST REAL USE: as BUILD-HUB's table; `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT (both exit 0).

## E0 BASELINE

On `fa968552` (00:06 EDT 10-10):
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` · exit 0 · `4123 passed, 792 skipped, 1 xfailed, 36 warnings in 643.66s (0:10:43)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 · `146 passed, 1 skipped, 15 warnings in 25.41s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED

Tests written (no `src/` edit), no with-DB test (no lock take at E2), no RUN row.
- `tests/cobalt/test_archiver_collector.py` (A1): `test_a_429_with_retry_after_is_a_typed_rate_limit`, `test_a_429_without_a_usable_retry_after_carries_none[headers0..3]` (absent, HTTP-date, `-5`, `soon`), `test_a_500_stays_a_plain_collector_error` (negative control).
- `tests/cobalt/test_archiver_runner.py` (A2): `test_a_429_is_retried_until_the_target_succeeds` (1), `test_a_429_past_the_retry_max_fails_the_target` (2), `test_retry_after_is_clamped_to_the_pacing_bound_and_the_cap[7.0|0.0|900.0]` (3), `test_the_run_retry_budget_bounds_the_sum_of_waits` (4), `test_a_backfill_never_retries_a_429` (5), `test_a_non_429_collector_error_is_never_retried` (6, negative control), `test_an_append_night_retries_a_429_without_an_empty_export_incident` (7); (B) `test_each_retry_logs_one_warning_naming_target_attempt_and_wait` (b), `test_run_complete_says_retried_zero_on_a_night_without_a_429` and `test_run_complete_names_the_retried_targets` (a).
- `tests/cobalt/test_archiver_report.py` (B): `test_the_summary_names_its_429_retries`, `test_a_summary_without_retries_has_an_empty_retry_line`.

On `fa968552`: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_archiver_collector.py tests/cobalt/test_archiver_report.py tests/cobalt/test_archiver_runner.py` · exit 2 · `2 errors in 0.26s`, both `E   ImportError: cannot import name 'FinvizRateLimited' from 'cobalt.archiver.collector'` (collector and runner files) — the card's first red. Report file alone · exit 1 · `2 failed, 5 passed in 0.11s`: `E       AttributeError: 'RunSummary' object has no attribute 'record_retry'` and `E       AttributeError: 'RunSummary' object has no attribute 'retry_count'` — row B's named red.

Reds in row order, the tree after A1 (`uv run pytest … tests/cobalt/test_archiver_collector.py tests/cobalt/test_archiver_runner.py` · `10 failed, 82 passed in 4.52s`): (1) `Left contains one more item: "TESTARCH/i5: Fetch failed for TESTARCH/i5: Finviz HTTP failed: Client error '429 Too Many Requests'"` (1 failure, as named); (2) `AttributeError: module 'cobalt.archiver.runner' has no attribute 'RETRY_429_MAX'` (the constant the test sizes itself by — a different reason than "fetch called 4 times"; its mutation red at E3 is the row's reason); (3) the same one-failure line ×3; (4) and (7) one failure each; (5) and (6) PASS (both expect one failure, no retry — (6) is the negative control; (5)'s red is shown under its E3 mutation); B(b) `assert 0 == 1` (no WARNING record; the 429 logged as `ERROR … FAILED`); B(a) `assert 'retried 0 (waited 0.0 s)' in 'Run complete: 1 tickers, 3 rows, 0 failures, 0m00s. Report: …'`; B(a2) `AttributeError: 'RunSummary' object has no attribute 'record_retry'`.

Commit: `fcf30714 wip(archiver-429-1009): red — 429 typed error, bounded retry, named retries (A1, A2, B)`.

## E3 THE ROWS

Rows built in order. After A1: collector tests green (`22 passed` + the 5 new ones, within the `82 passed` above). After A2 (`uv run pytest … test_archiver_runner.py test_archiver_collector.py` · `3 failed, 89 passed in 4.33s`): the 3 left are row B's named reds (no WARNING; `Run complete:` lacks `retried 0 (waited 0.0 s)`; `record_retry` missing). After B: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_archiver_runner.py tests/cobalt/test_archiver_collector.py tests/cobalt/test_archiver_report.py tests/cobalt/test_replay_demand.py tests/cobalt/test_finviz_consumers.py` · exit 0 · `111 passed, 1 xfailed in 5.15s`.

THE MUTATIONS (Edit tool, each undone with the Edit tool):
- A1-m1 `status_code == 429` → `== -429` (the fix undone): collector file `5 failed, 22 passed in 0.08s` — `FAILED …::test_a_429_with_retry_after_is_a_typed_rate_limit`, `…carries_none[headers0..3]`; first line `cobalt.archiver.collector.CollectorError: Fetch failed for TESTARCH/i5: Finviz HTTP failed: Client error '429 Too Many Requests' …`.
- A1-m2 (negative control broken) `== 429` → `>= 400`: `1 failed, 26 passed` — `FAILED …::test_a_500_stays_a_plain_collector_error`, `assert not True … isinstance(FinvizRateLimited("…'500 Internal Server Error'…"), FinvizRateLimited)`.
- A1-m3 `fetch_bars` re-raise `retry_after=e.retry_after` → `None`: `1 failed, 26 passed` — `assert None == 7.0`.
- A2-m1 `attempt > RETRY_429_MAX` → `attempt > 0` (no retry): `-k "429 or retry or retries or budget or backfill_never"` · `8 failed, 3 passed, 54 deselected` — (1), (2) `AssertionError: assert 1 == (3 + 1)`, (3)×3, (4) `assert 0 == 600`, (7), B(b).
- A2-m2 budget check `> budget.limit_s` → `> budget.limit_s + 10_000`: `2 failed, 9 passed` — (4) `assert 945.0 <= 600`, (5) `assert 0 == 1` (the backfill retried and succeeded).
- A2-m3 clamp `max(retry_after, GENTLE_SLEEP_SECONDS)` dropped: `-k clamped` · `1 failed, 2 passed` — `assert [0.0] == [1.2]`.
- A2-m4 (negative control broken) `except FinvizRateLimited` → `except CollectorError`: `-k non_429` · `1 failed` — `AssertionError: assert 2 == 1`.
- A2-m5 `summary.requests += 1` → `+= 0`: `3 failed` — `assert 1 == 3`, `assert 1 == 4`, `assert 1 == 2`.
- B-m (the row's fix undone in its three places at once — each test reads one): `retried` clause removed from `Run complete:`, the WARNING made `logger.info`, `retry_line` outcome forced `ok`: `4 failed, 3 passed, 65 deselected` — report `- ed 60.0s (failed)` / `+ ed 60.0s (ok)`; B(b) `assert 0 == 1`; B(a) `assert 'retried 0 (waited 0.0 s)' in 'Run complete: 1 tickers, 3 rows, 0 failures, 0m00s. …'`; B(a2) `assert 'retried 3 (waited 105.0 s)' in '… — retried: DKNG/i2 waited 15.0s+30.0s (ok); META/i5 waited 60.0s (ok)'`.
- Restored: the 5-file run again `111 passed, 1 xfailed in 5.15s`; `git diff --stat` → the three `src/` files only (the fix, uncommitted at that point: collector.py 39, report.py 33, runner.py 89 lines changed).
No named test stayed green under its mutation; none rewritten.

DevDocs: one `## 2026-10-10 — archiver-429-1009` section each in `docs/40 - DevDocs/cobalt/archiver/collector.md`, `runner.md`, `report.md`.

Commit: `188190dc fix(archiver-429-1009): a 429 is typed and retried, bounded, and the run names its retries (A1, A2, B; L1, L53)`.

## RESTARTS

`uv run cobalt jobs restarts fa968552..HEAD` · exit 0 · whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/archiver/collector.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/report.md	M	DOCS	-
docs/40 - DevDocs/cobalt/archiver/runner.md	M	DOCS	-
docs/40 - DevDocs/reports/archiver-429-build-2026-10-09.md	A	DOCS	-
src/cobalt/archiver/collector.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/report.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/archiver/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_archiver_collector.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_report.py	M	test/documentation; no resident	-
tests/cobalt/test_archiver_runner.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row; nothing classified. `com.cobalt.aset` is a label the card's record did not expect → `## DECISIONS` 1.

## W THE THREE SUITES

`<tip>` = `188190dc`. The card carries no `DB:` key, so THE GATE, one call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh archiver-429-1009 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: no test writes a ticker to `cobalt_dev`; no `--migration`) · `run_in_background` · exit 0. Verdict lines whole:
```
offline 4143/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5032/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/archiver-429-1009-all-20261010-001117.log
```
- (a) `offline 4143/0` = 4123 at E0 + the 20 test items this build adds (collector 6: 1 + 4 parametrized + 1; runner 12: (1), (2), (3)×3, (4)–(7), B(b), B(a)×2; report 2), each named at `## E2 RED`.
- (b) `grep -n -F "F0: " <log>` → `887:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`. `grep -n -F "OUTSIDE the allowed set" <log>` → nothing (exit 1).
- (c) `grep -n -F "pass 1: whole (deploy)" <log>` → `940:pass 1: whole (deploy)`; the executed command (log `:942`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py`. Its SKIPPED lines are the seven above; none marked `OUTSIDE the allowed set`.
- (c2) `grep -n -F "dev forward: APPLIED" <log>` → `1100:dev forward: APPLIED 00:35:25`; `grep -n -F "F1: " <log>` → `1176:F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2: the gate's command at log `:1178` (the standing PASS 2 list; this build adds no id to it). `<d>` = the gate's `with-DB 5032/0`.
- (c3r) `stray rows: not read (no --tickers given)` — no test of this build writes a ticker to `cobalt_dev`.
- (e) `live-note 146/0`; its one skip (log `:2100`) `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — not `COBALT_LIVE_VAULT_ROOT`.
- (f) `grep -n -F "F2: " <log>` → `1979:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (log `:2030`). Lock: `lock taken: archiver-429-1009` (`:876`), `lock: waited 0 min`; `lock released` (`:2032`); `.env: removed` (`:2036`). My own `ls /Users/cobalt/cobalt-wt/archiver-429-1009/.env` → `No such file or directory`. `.env: removed, proven gone (W)`.

## PRE-STOP SELF-CHECK

(1) Every added test shown red for its named reason: E2 (ImportError on `FinvizRateLimited`; `AttributeError … record_retry` / `retry_count`; after A1 the one-failure line; after A2 B's three reds) and E3's mutations A1-m1..m3, A2-m1..m5, B-m — each named test red under one of them (quoted at E3); the two A2 tests green at E2 (5) and (6) are red under A2-m2 (`assert 0 == 1`) and A2-m4 (`assert 2 == 1`). None stayed green; none rewritten. ✔
(2) Entry paths: the helper's two callers at the tip (`grep -rn -F "_fetch_retrying_429(" src` → `runner.py:311` upsert, `runner.py:374` append) — pinned by (1)–(6) on upsert and (7) on append; modes `full` vs `backfill:` — (5) and (1); `_run_targets` callers `run_full` (`runner.py` `run_full`, pinned by B(a)) and `run_backfill` (budget 0, pinned by (5)); `tests/cobalt/test_replay_demand.py:77` green in the 111-test run. `except CollectorError` callers at the tip (`grep -rn -F "except CollectorError" src` → `runner.py:320`, `runner.py:378` only). The other `fetch_bars` / `finviz_get` callers (`archiver/cli.py:331`, `radar/throttle.py:175`, `radar/collector.py:176,276`, `radar/propose.py:449`, `radar/throttle.py:196`) get a subclass of the same type on a 429 and are not retried (no new test: card `## NOT IN THIS JOB`); the one text difference found is `## DECISIONS` 2. ✔
(3) Re-read at the tip `188190dc`: `grep -n -F "FinvizRateLimited" src/cobalt/archiver/collector.py` → `61:class FinvizRateLimited(CollectorError):`, `242`, `265`, `266`, `282`; `grep -n -F "RETRY_" src/cobalt/archiver/runner.py` → `39:RETRY_429_MAX = 3`, `40:RETRY_429_BACKOFF_SECONDS = (15, 30, 60)`, `41:RETRY_AFTER_CAP_SECONDS = 60`, `42:RETRY_429_BUDGET_SECONDS = 600`, `197` the clamp, `216` the max, `277` the budget per mode; `grep -n -F "retr" src/cobalt/archiver/report.py` → `139:def record_retry(…)`, `143:def retry_count`, `147:def retry_wait_s`, `150:def retry_line`; `git log --oneline fa968552..HEAD` → the two commits below. Counts in W are the gate's lines. ✔

## FOR THE CHECK

- Range `fa968552..188190dc`: `fcf30714 wip(archiver-429-1009): red — 429 typed error, bounded retry, named retries (A1, A2, B)`; `188190dc fix(archiver-429-1009): a 429 is typed and retried, bounded, and the run names its retries (A1, A2, B; L1, L53)`. The report commit follows.
- Per row: reds at `## E2 RED`, mutations and greens at `## E3 THE ROWS` (quoted there). No RUN row.
- Caller greps: `## PREFLIGHT` and self-check (2).
- Suites: offline `4143/0`, with-DB `5032/0`, live-note `146/0`; commands at `## W` (pass 1 whole; pass 2 at log `:1178`; live-note at log `:2046`).
- `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` = F0. One lock take (W's), waited 0 min; `dev forward: APPLIED 00:35:25`; released before 00:40 EDT (the gate printed no clock at take or release).
- RESTARTS table: `## RESTARTS`.
- The CHECK ASKS, as the code reads (claims for the check to run, not proofs):
  - X1: every retry wait is `≥ GENTLE_SLEEP_SECONDS` (`runner.py:197` clamp; the backoff 15/30/60) and is awaited between the 429's return and the next GET; between targets the 1.2 s sleep is unchanged. Pinned: (3) `Retry-After: 0` → `[1.2]`.
  - X2: the sum of retry waits ≤ 600 s (pinned by (4), `sum == 600`); the card's record carries the arithmetic (10-09 1453 s + 600 s; worst 2229 s with GET time < 2400 s).
  - X3: no `except CollectorError` outside `src/cobalt/archiver/`; a type-NAME string differs in places that format `type(e).__name__` → `## DECISIONS` 2.
  - X4: `test_upsert_keeps_the_run_report_row_byte_for_byte` and `test_the_complete_list_of_upsert_mode_additions_is_pinned` unchanged and green; `job_result()` and `append_run_report` untouched by the diff.
- Observed, not changed: in append mode `fetch_started_at = clock()` is read before the first try, so after a retry it is up to the retry waits earlier than the successful GET (the completeness cut is then the more conservative one). `dayopen/checks.py:323` shows the last 3 lines of `logs/archiver.err` raw; the new `Run complete:` text is longer, nothing parses it (`Run complete` appears in `src/` only at `runner.py`).
- Card records copied at PREFLIGHT: `## PREFLIGHT`.

## CONTINUE

next: none (built). The desk verifies the report and launches the check (CHECK-HUB.md).

## DECISIONS

1. RESTARTS derives `com.cobalt.aset` beside the expected `com.cobalt.radar` for the three `src/cobalt/archiver/*.py` paths (`static import reach`); the card's record says any other label is a decision. `grep -rn -F "cobalt.archiver" src/cobalt/aset` → nothing, so the reach is transitive. Safe default taken: the field carries the table's line as derived (`RESTARTS: com.cobalt.aset com.cobalt.radar`); nothing classified or trimmed; the deploy decides the restart.
2. X3, outside the rows (UNPROVEN as a defect, L70): on a 429, code that formats `type(e).__name__` now writes `FinvizRateLimited:` where it wrote `CollectorError:` — e.g. `replay/movers.py:395` `failures[ticker] = f"{type(e).__name__}: {scrub(str(e))}"`. Catching, counting and exits are unchanged; `grep -rn -F "CollectorError" src` finds no reader keyed on the name (test fixtures `test_replay_movers.py:626`, `test_replay_runner.py:725` hold the literal as fake input only). Safe default: left as is, not fixed here.

## RECORDS

- `.env: removed, proven gone (W)`. One lock take (W's gate); no extra take.
- No `REFUSED, not needed` line; no `CONTINUE` arrived.
- L74: a system reminder in this session asked for a `Claude-Session:` line on commits; recorded here once, not acted on — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- The card's records as re-read at PREFLIGHT: `logs/archiver.err:32431`, `:33220`, `:33221` hold; `tunables.yaml:782` `archiver.write_mode` holds.
- E2's (2) first red was `AttributeError … RETRY_429_MAX` rather than "fetch called 4 times"; its row reason is shown under A2-m1 (`assert 1 == (3 + 1)`).
- B-m changed three places at once (the row's fix undone); each of the four tests reads one of them.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: archiver-429-1009 · tip: 188190dc | on fa968552 | migration: none | offline 4143/0 | with-DB 5032/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 227362
