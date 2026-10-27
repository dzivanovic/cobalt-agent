# f4-strike-reserve — build report 2026-10-26

## §0 Headline
Rows R1, R6, R2, R3, R4 and D0 are built on `1d6cce4af`. Each row went red first, every mutation was caught, and the card's offline suite reads `195 passed, 28 skipped, 4 xfailed`. R5 (b): `PROBE X15 OK peak 50/min at 08:43 … 429 0`. RESTARTS: `com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
The first gate was red on 5 tunables-digest pins (R95). The desk widened R1's files (card `ce8a53fbf`), and the fix is `a79fca72f` (`<tip>`). The second gate is green: offline 5038/0, with-DB 6010/0, live-note 148/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`. No decision is open.

## L74
A `Claude-Session:` commit-line request arrived in this session's system context. It is recorded under `## RECORDS` and was not acted on.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md"` (20:48 EDT) → exit 0, output WHOLE:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md" · 0 · 17f82377c2ff8cb8bcbaf50d901b73f2b1adc7b0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1049-f4-strike-reserve-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-26 R2512 row · grep -n "^| R2512 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-26.md" · 0 · 72:| R2512 | 18:05 ET | HIS RULING · APPROVED (relayed by brain, words: "C as you recommend"): card 1049 = cap radar's Finviz bucket at 37/min (`radar.finviz_rpm`), strike stays 30 s; A and B rejected. Words: cto-2026-10-26-words.md#R2512. | APPLIED: NOW 18:07 |
RULING 2026-10-26 R2512 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R2512 |" -- "docs/40 - DevDocs/reports/cto-2026-10-26.md" · 0 · e015c97bb2efc6db8bee9007a1858f5bf17fc70d
RULING 2026-10-26 R2512 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-26.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`<FP>` (copied whole; not run, no lock take before W): `COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

| rule | command | exit | output |
|---|---|---|---|
| mechanical | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | whole below |
| base | `git show --stat 1d5ba104` | 0 | `1d5ba1044 docs(desk): R2527-R2528 port4 deployed` · `docs/40 - DevDocs/reports/cto-2026-10-26.md | 6 ++++--` · 1 file changed, 4 insertions(+), 2 deletions(-) |
| restarts empty | `uv run cobalt jobs restarts 1d5ba104..HEAD` | 0 | `docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md	A	DOCS	-` · `RESTARTS: none` (the only path is this untracked report; no commit in the range) |

```
clock · date · 0 · Mon Oct 26 20:48:52 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/f4-strike-reserve
    ?? "docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 1d5ba1044 docs(desk): R2527-R2528 port4 deployed
diff · git diff --stat 1d5ba104 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f4-strike-reserve · 0 · 1d5ba1044 docs(desk): R2527-R2528 port4 deployed
env here · ls /Users/cobalt/cobalt-wt/f4-strike-reserve/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

THE CARD'S SYMBOLS (Grep tool, `-n`; each hit at BASE; the card's `main e015c97b` lines all hold at BASE `1d5ba104` — runner.py's places re-found by content, they did not move):
- `src/cobalt/radar/collector.py`: `42:class TokenBucket:` · `54: self.rate = rpm / 60` · `55: self.capacity = 1.0` · `62: async def acquire` · `78:def process_bucket(rpm: int) -> TokenBucket:` · `151:/253: raw = load_tunables().by_key["radar.finviz_max_rpm"].value` · `154:/256: bucket = process_bucket(int(raw))`.
- `src/cobalt/radar/runner.py`: `27:from .collector import FinvizScreenerCollector, SourceFailure, process_bucket` · `515:async def build_runner()` · `518: rpm = tunables["radar.finviz_max_rpm"].value` · `522: bucket = process_bucket(int(rpm))` · `547: daily_source=FinvizDailyBarsCollector(token, config=config, bucket=bucket).daily` · `556: ceiling_rpm=int(rpm)` · `559: collector=FinvizScreenerCollector(token, config=config, bucket=bucket)` · `564: bucket=bucket` (poller) · `600-616 StrikeThread._main` (catch `:608-609`, `wait = loop.interval_s()` `:611`) · `642/646` scan interval sleep.
- `src/cobalt/radar/config.py`: `200:TUNABLE_UNITS = {` · `204: "radar.finviz_max_rpm": TunableUnit.COUNT` · `210:def check()` · `226:def command(_args)`.
- `src/cobalt/strike/detector.py`: `50:from cobalt.radar.collector import TokenBucket` · `80:class DemandPlan` · `103:def poll_interval` · `104-105 IntervalRefused` · `111:def check_strike_demand` · `117: return check_scheduled_demand("strike", radar_rpm=planned_rpm, extra=[consumer])` · `167:def _read_plan` · `276: except (IntervalRefused, RadarNoteError) as e:` · `280: self._interval = interval` · `313:def read_plan()` · `319: return DemandPlan(planned_rpm=parsed.planned_rpm, headroom_rpm=demand.headroom_rpm if demand else None)` · `349: plan=read_plan`.
- `src/cobalt/prefill/daily.py`: `100:from cobalt.strike.detector import read_plan` · `682:REFRESH_GETS = 3` · `759:def refresh_demand_consumer()` · `780:def check_refresh_demand()` · `788: plan = read_plan()` · `791-792` no-headroom refusal · `794: check_scheduled_demand(REFRESH_SUBJECT, …)` · `800:async def _gated_fetch`.
- `src/cobalt/radar/notes.py`: `300:def _ceiling()` · `397:def check_scheduled_demand` · `656: if steady > ceiling_rpm + 1e-9:`.
- `src/cobalt/prefill/refresh_probe.py`: `23` radar docstring line · `62:CONSEQUENCE = (` · `72:class X15Setup` · `77: radar_rpm: float = 40.0` · `321:async def _radar` · `380:def _x15` (card: `:407` is the `_radar(...)` call inside it) · `451:def main`.
- `configs/cobalt/taxonomy/tunables.yaml`: `702: - key: radar.finviz_max_rpm` … `709: consumers:`.
- tests: `test_radar_collector.py:34 test_token_bucket_fake_clock_waits_for_second_token` · `test_radar_config.py:10-19` import, `:22 test_shipped_config_and_all_tunables_validate`, `:220 test_finviz_ceiling_is_the_ruled_50` · `test_radar_price_floor.py:376 test_build_runner_hands_one_card_store_to_both_stages` (`inspect.getsource(runner_module.build_runner)`) · `test_prefill_refresh.py:178-191 plan fixture`, `:622/:639/:652/:659-685` · `test_refresh_probe.py:59 small`, `:176 test_x15_a_minute_above_50…`, `:233` FAIL param · `test_strike_detector.py:137/:145/:163`.
- `docs/30 - Design/F4-FINAL-2026-10-10.md`: `219` (X13 row), `221` (X15 row), `223` (X17 row) — grep `^\| X1[3579] `.
CALLERS (Grep `process_bucket\(|read_plan\(|check_strike_demand\(|check_refresh_demand\(` over `src`): `replay/cli.py:69` (process_bucket(ceiling), NOT IN THIS JOB) · `prefill/daily.py:788` (read_plan) · `prefill/daily.py:802` (check_refresh_demand) · `strike/detector.py:275` (check_strike_demand) · `strike/detector.py:245/:252` (_read_plan → plan) · `radar/collector.py:154/:256` · `radar/runner.py:522`. `radar_bucket_rpm`, `refresh_burst_refusal`, `REFRESH_BURST_RPM`: no hit (new).
`wc -l`: tunables.yaml 1172 · collector.py 306 · runner.py 743 · config.py 244 · detector.py 356 · daily.py 1250 · refresh_probe.py 458 · test_radar_collector.py 95 · test_radar_price_floor.py 435 · test_radar_config.py 233 · test_strike_detector.py 360 · test_prefill_refresh.py 1314 · test_refresh_probe.py 253 · F4-FINAL 320.
`tail -n 3 reports/f4-gate-run-2026-10-26.md` → last line `GATES DONE · ok: 1 · fail: 2 · not run: 1 · ruled: 1`; `:19` = the card's X15 FAIL line verbatim; `:14` `X9  RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`.
THE CARD'S RECORDS, copied: (1) F4 reservation 1049, launched only on PROBE X15 FAIL (R2465), superseded revisions, ruling C (R2512) — re-read: R2512 row at `cto-2026-10-26.md:72` (AUTHORIZATION output). (2) ARITHMETIC (drafter) — re-checked by the R1/R2 tests below. (3) 1049-C build proofs by pytest. (4) fix drafter 18:12 EDT reads at main — re-read: the cites above. (5) drafter 17:54 EDT reads only; BASE reset by desk — re-read: BASE is `1d5ba104` (port4 deployed, R2527-R2528), D1 holds.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `1d5ba104` → exit 0: `5008 passed, 878 skipped, 4 xfailed, 36 warnings in 836.16s (0:13:56)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 28.95s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Commit `b8c0aaead wip(f4-strike-reserve): red` (6 test files, `256 insertions(+), 8 deletions(-)`). No with-DB red (every row's red is offline): no lock take at E2.
`uv run pytest -q -rf -p no:cacheprovider --color=no --tb=no <the six files>` on BASE → `25 failed, 142 passed, 28 skipped, 3 xfailed in 43.42s`. The 25 reds and each first line (from the `--tb=line` runs):
- R1 `test_radar_collector.py::test_the_radar_bucket_rpm_is_radar_finviz_rpm` and the 7 `::test_radar_finviz_rpm_out_of_bounds_is_refused[rpm0|None|0|-1|51|37|True]` → `ImportError: cannot import name 'radar_bucket_rpm' from 'cobalt.radar.collector'` (`rpm0` = the missing row).
- R1 `::test_a_default_collector_takes_the_37_bucket` → `assert 0.8333333333333334 == (37 / 60)` (the default bucket is the 50 ceiling's).
- R1 `test_radar_price_floor.py::test_build_runner_buckets_at_radar_finviz_rpm` → `assert 'process_bucket(radar_bucket_rpm(' in 'async def build_runner() …`.
- R1 `test_radar_config.py::test_shipped_config_and_all_tunables_validate` (edited) → `Extra items in the right set: 'radar.finviz_rpm'`; `::test_radar_finviz_rpm_is_the_ruled_37` → `KeyError: 'radar.finviz_rpm'`; `::test_radar_check_prints_radar_finviz_rpm_37` → `assert 'radar.finviz_rpm = 37' in [… 'radar.finviz_max_rpm = 50', …]` (the line absent).
- R1 `::test_a_50_request_burst_is_held_to_37_in_one_minute` → PASSED on BASE, as the card says (it proves the mechanism; R1's mutation target). Its fake sleep adds `delay + 1e-9` (the repo's own guard, `test_strike_detector.py:101-103`, against a token stuck at 0.9999…); the card said "as `:34-47`", which adds the bare delay — said here.
- R6 `test_strike_detector.py::test_radar_planned_20_strike_still_polls_every_30_s` → `assert 30.0 == 10.0` (`read_plan()` headroom 30, the radar's planned headroom); `::test_radar_planned_45_…_and_is_admitted` → `assert 5.0 == 10.0`; `::test_the_strike_reserve_equals_refreshs_gets` → `AttributeError: module 'cobalt.strike.detector' has no attribute 'REFRESH_BURST_RPM'`; `::test_read_plan_keeps_none_and_no_headroom` → `headroom_rpm: 30.0 != None` (planned None, demand present: BASE passes the demand's headroom); `::test_an_unreadable_cap_in_read_plan_refuses_the_tick_no_fetch` and `::test_an_unreadable_cap_at_the_strike_gate_makes_no_fetch_and_never_polls_faster` → `AttributeError: <module 'cobalt.strike.detector' …> has no attribute 'radar_bucket_rpm'` (at the monkeypatch).
- R2 `test_prefill_refresh.py::TestSharedGate::test_c_radar_cap_strike_headroom_and_refresh_over_the_ceiling_is_refused_no_get` → red (BASE admits 30/20: `check_refresh_demand()` None); `::test_c_one_over_the_allowance_is_refused` → `assert 0 == 1` (exit 0, GETs made); `::test_c_an_unreadable_radar_finviz_rpm_makes_no_get` → `assert 'radar.finviz_rpm' in ((None or ''))`. `::test_c_x15_plan_is_admitted_at_exactly_the_ceiling_and_gets_three` and the new x14 param `DemandPlan(40.0, None)` PASS on BASE (form B admits 40/10; the S2 `None` refusal is kept) — guards of the fix, not reds.
- R3 `test_refresh_probe.py::test_x15_the_radar_cap_holds_a_50_rpm_radar_to_37_and_passes` → `AssertionError: PROBE X15 FAIL peak 53/min at 08:43 · per minute 08:40=50, 08:41=50, 08:42=50, 08:43=53, 08:44=50, 08:45=50 · radar 240 · strike 60 · refresh 3 · 429 3 (radar=3) · strike interval 30 s · refresh gate admitted → …`; `::test_x15_a_minute_above_50_fails_and_names_the_consequence` and `::test_x15_prints_one_line_and_exits_by_verdict[FAIL-1-change1]` → `TypeError: X15Setup.__init__() got an unexpected keyword argument 'radar_cap'`.

## E3 THE ROWS
Commit `1d6cce4af fix(f4-strike-reserve): radar Finviz bucket capped at radar.finviz_rpm 37, strike headroom against the cap, refresh burst gate, X15 at the cap (R1, R6, R2, R3, R4, D0; L1, L3, L10, L53, L79)` — `15 files changed, 155 insertions(+), 36 deletions(-)`. Order built: R1, R6, R2, R3, R4, D0 (the card's ORDER). Every `file:line` was re-read from the file before its edit (runner.py's `:522` place found by content, unchanged by port4).
- R1 (tunables row after `radar.finviz_max_rpm`; `collector.radar_bucket_rpm` beside `process_bucket`; both default-bucket branches → `process_bucket(radar_bucket_rpm())`; `build_runner` → `process_bucket(radar_bucket_rpm(tunables))`, `rpm` and `ceiling_rpm=int(rpm)` unchanged; `config.TUNABLE_UNITS` + `check()` calls `radar_bucket_rpm(registry)` → `RadarConfigError`). `TokenBucket` body unchanged (`git diff` shows only the docstrings of the module and the daily collector beside it). Green: `uv run pytest … test_radar_collector.py test_radar_config.py test_radar_price_floor.py test_radar_runner.py test_finviz_consumers.py` → `94 passed, 1 xfailed in 20.64s`.
- R6 (`REFRESH_BURST_RPM = 3`; `read_plan` headroom = ceiling − cap − 3 from one `by_key`, `None` kept, ≤ 0 passed through; `check_strike_demand` counts `min(planned_rpm, radar_bucket_rpm())`; `radar_bucket_rpm` imported beside `TokenBucket`). Green: `test_strike_detector.py test_strike_detector_db.py` → `26 passed, 2 skipped in 2.84s` (the 2 skips: the with-DB file offline; it runs at W).
- R2 (`daily.py` imports `SourceFailure, radar_bucket_rpm` from `cobalt.radar.collector`, `DemandPlan` beside `read_plan`; `refresh_burst_refusal`; `check_refresh_demand`: the None/no-headroom refusals first, form B unchanged, then cap (`SourceFailure` → refusal), `notes._ceiling()` looked up on the module (`None` → refusal), then the one comparison). Green: `test_prefill_refresh.py test_finviz_consumers.py` → `56 passed, 28 skipped, 4 xfailed in 7.38s`.
- R3 (`X15Setup.radar_cap`, `radar_rpm` 50.0 offered; `_radar` acquires a `TokenBucket(cap, virtual clock)` before each GET; `CONSEQUENCE` and the docstring's radar line). Green: `test_refresh_probe.py -rP` → `17 passed in 49.49s`, the new test's line `PROBE X15 OK peak 50/min at 08:43 · per minute 08:40=47, 08:41=47, 08:42=47, 08:43=50, 08:44=47, 08:45=47 · radar 222 · strike 60 · refresh 3 · 429 0 · strike interval 30 s · refresh gate admitted`.
- R4: the AMENDMENT sentence appended inside the X13 row's last cell (`F4-FINAL-2026-10-10.md:219`, before the closing `|`), verbatim from the card.
- THE CARD'S OFFLINE SUITE, at the fix after the mutations: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_collector.py tests/cobalt/test_radar_config.py tests/cobalt/test_radar_price_floor.py tests/cobalt/test_radar_runner.py tests/cobalt/test_prefill_refresh.py tests/cobalt/test_refresh_probe.py tests/cobalt/test_strike_detector.py tests/cobalt/test_finviz_consumers.py` → `195 passed, 28 skipped, 4 xfailed in 79.60s (0:01:19)` (before the two test additions below: `190 passed, 28 skipped, 4 xfailed`).
- D0: one `## 2026-10-26 — f4-strike-reserve` section appended to each of `radar/collector.md`, `radar/runner.md`, `radar/config.md`, `prefill/daily.md`, `strike/detector.md`. `refresh_probe.py` has no page under `docs/40 - DevDocs/cobalt/prefill/` (Glob: no file); the card's D0 names five pages; recorded under `## RECORDS`.

THE MUTATIONS (Edit tool, each undone with Edit; `git diff` on the touched source after each undo shows only the fix):
- R1 (a) `radar_bucket_rpm` `return value` → `return ceiling`, (b) `build_runner` back to `process_bucket(int(rpm))`, (c) `TokenBucket.capacity = 2.0` (the mechanism) → `3 failed, 68 passed`: `test_the_radar_bucket_rpm_is_radar_finviz_rpm` `assert 50 == 37`; `test_a_default_collector_takes_the_37_bucket` `assert 0.8333333333333334 == (37 / 60)`; `test_build_runner_buckets_at_radar_finviz_rpm` `assert 'process_bucket(radar_bucket_rpm(' in …`. **The burst test STAYED GREEN under capacity 2.0** (a bucket saturated from t = 0 never banks a second token) → REWRITTEN: the fake clock starts at −600 and is moved to 0 before the burst, so the bucket is full after ten idle minutes (the "burst included" case). Re-run under capacity 2.0: `test_a_50_request_burst_is_held_to_37_in_one_minute` → `assert 38 == 37` (red). Green again at capacity 1.0 (the 195 above).
- R1 (d) `check()`'s `radar_bucket_rpm(registry)` → `pass`: the NEW pin `test_radar_config.py::test_radar_check_refuses_an_out_of_bounds_radar_finviz_rpm[None|0|51|37|True]` (added in E3 for X3, the check path — no card test pinned `check()`'s refusal; said here) → `5 failed, 30 passed`, each `Failed: DID NOT RAISE <class 'cobalt.radar.config.RadarConfigError'>`.
- R1 (e) the bounds `isinstance(value, bool) or … <= ceiling` → `not isinstance(value, int) or not 1 <= value` → `4 failed, 48 passed`: `test_radar_finviz_rpm_out_of_bounds_is_refused[51]`, `[True]` and the two `check` params `[51]`, `[True]`: `DID NOT RAISE`.
- R6 (a)+(b) `read_plan` headroom → `demand.headroom_rpm`, gate → `radar_rpm = planned_rpm` → `3 failed, 23 passed`: planned 20 `assert 30.0 == 10.0`; planned 45 `assert 5.0 == 10.0`; gate path `Failed: DID NOT RAISE <class 'cobalt.radar.collector.SourceFailure'>`.
- R6 (b) alone (read_plan restored) → `2 failed, 24 passed`: planned 45 `assert 'REFUSED: total Finviz demand for strike: peak 55.00 rpm at 04:00 ET over [radar, strike], finviz_max_rpm=50 exceeds the ceiling' is None`; gate path `DID NOT RAISE`.
- R6 (c) `read_plan`: the None guard reduced to `demand is None`, the ≤ 0 pass-through removed, `cap = 37` (no read) → `2 failed, 24 passed`: `test_read_plan_keeps_none_and_no_headroom` `headroom_rpm: 10.0 != None`; `test_an_unreadable_cap_in_read_plan_refuses_the_tick_no_fetch` → `SourceFailure: radar.finviz_rpm = None is refused (constructed)` (the tick no longer refuses at the plan).
- R2 (a) the comparison disabled (`and False`) → `2 failed, 51 passed`: 30/20 `assert None is not None`; 39/11 `assert 0 == 1`. (b) `>` + tolerance → `>=` → `2 failed`: `test_c_x15_plan_is_admitted_at_exactly_the_ceiling_and_gets_three` `assert 1 == 0` and `TestDegraded::test_t5_x5_dead_source_keeps_the_0745_values` `assert 1 == 0` (the fixture's 40/10 now refused). (c) the cap's `SourceFailure` swallowed (`radar_cap = 37`), alone → `1 failed, 52 passed`: `test_c_an_unreadable_radar_finviz_rpm_makes_no_get` `assert 'radar.finviz_rpm' in ((None or ''))`.
- R3 the `await bucket.acquire()` in `_radar` removed → `1 failed, 16 passed`: `PROBE X15 FAIL peak 63/min at 08:43 · per minute 08:40=60, … · radar 300 · strike 60 · refresh 3 · 429 63 (radar=56, strike=7) …`.

## RESTARTS
`uv run cobalt jobs restarts 1d5ba104..HEAD` (HEAD `1d6cce4af`) → the table WHOLE:
```
path	change	rule	restart
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
docs/30 - Design/F4-FINAL-2026-10-10.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/collector.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/strike/detector.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-strike-reserve-build-2026-10-26.md	A	DOCS	-
src/cobalt/prefill/daily.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/prefill/refresh_probe.py	M	static import reach	-
src/cobalt/radar/collector.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
src/cobalt/strike/detector.py	M	static import reach	com.cobalt.aset,com.cobalt.cos,com.cobalt.radar
tests/cobalt/test_prefill_refresh.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_collector.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_config.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_price_floor.py	M	test/documentation; no resident	-
tests/cobalt/test_refresh_probe.py	M	test/documentation; no resident	-
tests/cobalt/test_strike_detector.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar
```
No `UNCLASSIFIED` row: no classification needed. `com.cobalt.radar` is in the table (X7).
Re-run after `a79fca72f` (HEAD = `<tip>`): the same table plus two rows, `tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-` and `tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-`. Its last line, **`RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar`**, is the stop line's field.

R5 RUN (asserts nothing beyond its tests), each `COBALT_ENV=dev` call preceded by `ls -la /Users/cobalt/cobalt-wt/f4-strike-reserve/.env` → `No such file or directory`:
- (a) `COBALT_ENV=dev uv run pytest -q -rP tests/cobalt/test_radar_config.py::test_radar_check_prints_radar_finviz_rpm_37` → WHOLE:
```
.                                                                        [100%]
==================================== PASSES ====================================
_________________ test_radar_check_prints_radar_finviz_rpm_37 __________________
----------------------------- Captured stdout call -----------------------------
/Users/cobalt/cobalt-wt/f4-strike-reserve/configs/cobalt/radar.yaml: OK (primary)
radar.scan_interval = 100
radar.poll_interval = 100
radar.poll_overlap_bars = 5
radar.finviz_max_rpm = 50
radar.finviz_rpm = 37
radar.poll_bar_max_age_s = 180
db.query.timeout_s = 30

1 passed in 0.13s
```
- (b) `COBALT_ENV=dev uv run pytest -q -rP tests/cobalt/test_refresh_probe.py::test_x15_the_radar_cap_holds_a_50_rpm_radar_to_37_and_passes` → WHOLE:
```
.                                                                        [100%]
==================================== PASSES ====================================
_________ test_x15_the_radar_cap_holds_a_50_rpm_radar_to_37_and_passes _________
----------------------------- Captured stdout call -----------------------------
PROBE X15 OK peak 50/min at 08:43 · per minute 08:40=47, 08:41=47, 08:42=47, 08:43=50, 08:44=47, 08:45=47 · radar 222 · strike 60 · refresh 3 · 429 0 · strike interval 30 s · refresh gate admitted
1 passed in 1.95s
```
- (c) the table above; its last line `RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar` is the record.
DEPLOY PROOF reads on this tree (worktree paths; the card's paths are main's, read after deploy): `grep -c -F "def radar_bucket_rpm(" src/cobalt/radar/collector.py` → `1` · `grep -c -F "process_bucket(radar_bucket_rpm(" src/cobalt/radar/runner.py` → `1` · `grep -c -F "key: radar.finviz_rpm" configs/cobalt/taxonomy/tunables.yaml` → `1` · `grep -c -F "def refresh_burst_refusal(" src/cobalt/prefill/daily.py` → `1` · `grep -c -F "REFRESH_BURST_RPM = 3" src/cobalt/strike/detector.py` → `1` · `ls /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` → exit 0, listed. X6: `grep -rn -F "cobalt.prefill" src/cobalt/strike` → only the two comment lines `detector.py:67-68` (no import).

## W THE THREE SUITES
`<tip>` = `1d6cce4af`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-strike-reserve all --deploy` (no `--deselect`, no `--tickers`: this build adds no with-DB test; no `--migration`) → **exit 1**, stdout WHOLE (its SKIPPED lines are elided here to the first and last; the full list is in the log):
```
RED (exit 1): 5 failed, 5033 passed, 878 skipped, 4 xfailed, 36 warnings in 783.27s (0:13:03)
SKIPPED [1] tests/cobalt/test_vaultwrite.py:493: Postgres env settings not available
…
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
5 failed, 5033 passed, 878 skipped, 4 xfailed, 36 warnings in 783.27s (0:13:03)
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-strike-reserve-all-20261026-212108.log
```
(a) OFFLINE `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (log `:2`) RED. The gate stopped after (a): **`cobalt_dev`: not taken** (no `take-devdb-lock` line in the log; `grep -n -F "lock" <log>` hits only `reaches cobalt_dev (lock-relief G1)` skip lines); (b)–(f) and (e) not run. `ls -la /Users/cobalt/cobalt-wt/f4-strike-reserve/.env` → `No such file or directory`.
The 5 reds (log `:89-189`), each a pinned card digest that carries `tunables_sha256`:
- `tests/cobalt/test_rubberband_forms.py:526` `test_t6_a_def_that_formed_before_changes_only_in_the_finals_named_ways` → `assert '80b0e29f5855...8f08b1890d907' == '0724a61afb0b...a74f840ba8224'` (it maps the digest back through `test_setups_registries._tunables_digests`).
- `tests/cobalt/test_setups_d1.py:233` `test_f11_the_dots_and_card_score_do_not_move[countertrend]` → `assert 'cc7f009e9a6a...f7eb8bce012db' == '77c3ce1fc3d3...38b8acde6a03c'`; `[mixed]` → `assert '8eaf836ee8f1...fa03e0d194bdb' == '4e17a9fecfba...469a9f749dd94'`.
- `tests/cobalt/test_setups_registries.py:211` `test_lego_ii_every_card_spec_is_byte_identical_through_the_registries[countertrend]` → `assert '3d4c83c50437...0bcd9e597183b' == '7a0e5796e33e...1f8811573450a'`; `[mixed]` → `assert '01d8844fbe47...5a830b604737b' == '5c4dcce2c86b...dde0629d9a3a7'`.
CAUSE (tool output): `_tunables_digests` (`test_setups_registries.py:119-128`) hashes every row of `load_tunables().by_key` (`radar_p2_support.py:109-110`), then maps the snapshot back by dropping the keys added since the pins (`STEP3_KEYS`, `:97-…`). `test_setups_d1.py:192` does the same with `ADDED_KEYS` (`:53-…`). R1's new row `radar.finviz_rpm` is in neither list, so the mapped-back digest moves. The standing pattern, "as every added row (R95)": `test_setups_d1.py:60-63` (the strike rows, the F4 refresh rows), and `git log` on `test_setups_registries.py` → `da8a84ddf fix(s4-p1-1009): tunables-digest pins exclude the four strike rows as every added row (R95) …`. The fix is two lines: add `"radar.finviz_rpm"` to `STEP3_KEYS` (`test_setups_registries.py`) and to `ADDED_KEYS` (`test_setups_d1.py`). **Neither file is in the card's rows.** BUILD-HUB `## W`: "A red at W … fix it inside the rows' files only"; the card's `## NOT IN THIS JOB`: "A red outside these rows: a `## DECISIONS` item … never fixed here". Not fixed; ASK DESK under `## DECISIONS`.

SECOND GATE (after `CONTINUE: W`, card `ce8a53fbf`). The fix is `a79fca72f fix(f4-strike-reserve): tunables-digest pins exclude radar.finviz_rpm as every added row (R1, W-1; R95)`, 2 files: `"radar.finviz_rpm"` added to `ADDED_KEYS` (`test_setups_d1.py:69`) and `STEP3_KEYS` (`test_setups_registries.py:118`), each with a neighbour-shaped comment; no pin value touched. Its red is the first gate's 5 reds above. Green: `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/cobalt/test_rubberband_forms.py tests/cobalt/test_setups_d1.py tests/cobalt/test_setups_registries.py` → `85 passed, 6 skipped in 220.26s (0:03:40)`. RESTARTS was run again (table below: the same last line). **`<tip>` = `a79fca72f`.**
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-strike-reserve all --deploy` → **exit 0**, verdict lines WHOLE:
```
tests/ops: skipped (no ops paths)
offline 5038/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 6010/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_checkpoints_live.py:36: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live checkpoint dry run
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 148/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-strike-reserve-all-20261026-214157.log
```
None of the nine SKIPPED lines is marked `OUTSIDE the allowed set`. The skips naming `COBALT_LIVE_VAULT_ROOT` are lines the gate prints for the with-DB pass, which runs without that variable. The live-note pass itself is `148/0` (log `:2387` `148 passed, 1 skipped, 15 warnings in 26.64s`), and its one skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`).
- (a) offline `<p>` = **5038** (log `:2` `$ uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy`, `:958` `5038 passed, 878 skipped, 4 xfailed, 36 warnings in 776.20s (0:12:56)`). Tests this build adds: `test_radar_collector.py::{test_a_50_request_burst_is_held_to_37_in_one_minute, test_the_radar_bucket_rpm_is_radar_finviz_rpm, test_radar_finviz_rpm_out_of_bounds_is_refused[×7], test_a_default_collector_takes_the_37_bucket}`, `test_radar_price_floor.py::test_build_runner_buckets_at_radar_finviz_rpm`, `test_radar_config.py::{test_radar_finviz_rpm_is_the_ruled_37, test_radar_check_refuses_an_out_of_bounds_radar_finviz_rpm[×5], test_radar_check_prints_radar_finviz_rpm_37}`, `test_strike_detector.py::` the six R6 tests, `test_prefill_refresh.py::TestSharedGate::` the four `test_c_*` and the x14 `[broken3]` param, `test_refresh_probe.py::test_x15_the_radar_cap_holds_a_50_rpm_radar_to_37_and_passes`. Offline line: `tests/ops: skipped (no ops paths)`.
- (b) `lock taken: f4-strike-reserve` (log `:965`; `lock: waited 0 min`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:976`); `LEVEL 0013`.
- (c) PASS 1 `<d1>` = **5766** (log `:1204` `5766 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 950.00s (0:15:50)`). The executed command (log `:1034`), WHOLE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py --deselect tests/cobalt/test_strike_detector_db.py --deselect tests/cobalt/test_strike_stream_db.py --deselect tests/cobalt/test_strike_ack_db.py --deselect tests/cobalt/test_playbook_db.py --deselect tests/cobalt/test_db_apply_db.py --deselect tests/cobalt/test_dml_roles_db.py --deselect tests/cobalt/test_genesis_db.py --deselect tests/cobalt/test_genesis_experiments_db.py --deselect tests/cobalt/test_genesis_vectors_db.py --deselect tests/cobalt/test_checkpoints_db.py` (the gate-lists' own deselects; this build adds none).
- (c2) `dev forward: APPLIED 22:11:11` (log `:1206`); `F1: 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1290`).
- (c3) PASS 2 `<d2>` = **244** (log `:1292` the gate-lists' PASS 2 command, `:2186` `244 passed, 1 deselected, 5 warnings in 244.69s (0:04:04)`); this build adds no with-DB test id. It includes `tests/cobalt/test_rubberband_forms.py` (one of the W-1 pins) and `tests/cobalt/test_strike_detector_db.py`. `<d>` = 5766 + 244 = **6010** = the gate's `with-DB 6010/0`.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker on `cobalt_dev`.
- (e) live-note `<l>` = **148** (log `:2332` the LIVE-NOTE command, `:2387`).
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log `:2260`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:2316`); `.env: removed`; `ls /Users/cobalt/cobalt-wt/f4-strike-reserve/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." — **holds.**
- E2 reds (`## E2 RED`): all 25 named tests.
- E3 mutation reds (`## E3 THE ROWS`, THE MUTATIONS): every new or edited test, including the burst test (red `assert 38 == 37` under capacity 2.0, after it was rewritten because it stayed green), the added `check` pin (red `DID NOT RAISE`), `test_c_x15_plan_is_admitted…` (red under `>=`), and the x14 `None` param, which guards the kept S2 fix (green on BASE by design: no `src` change of this build touches that refusal).
- The `small` and FAIL-param edits are red on BASE (`TypeError … 'radar_cap'`).
- The two W-1 key additions: red at the first gate (the 5 pins), green after `a79fca72f`.
(2) "Every entry path of each rule pinned by a test." — **holds.** Each PREFLIGHT caller and the test that pins it:
- `radar/collector.py:173/:270` (default buckets) → `test_a_default_collector_takes_the_37_bucket`.
- `radar/runner.py:522` → `test_build_runner_buckets_at_radar_finviz_rpm`.
- `radar/config.py check()` → `test_radar_check_refuses_an_out_of_bounds_radar_finviz_rpm`, `test_radar_check_prints_radar_finviz_rpm_37`.
- `strike/detector.py read_plan` (resident `build_detector :349`, refresh `daily.py:100/:788`) → the R6 `read_plan` tests; refresh's path via `test_prefill_refresh.py` (its fixture patches `read_plan`; the cap's `SourceFailure` through `read_plan` is caught by `check_refresh_demand`'s first `except`).
- `check_strike_demand` (`detector.py tick`) → planned 45 and path (ii).
- `check_refresh_demand` / `_gated_fetch` (`daily.py`) → the four `test_c_*` and x14.
- Probe `_x15` → the R3 tests.
- `replay/cli.py:69 process_bucket(ceiling)`: NOT IN THIS JOB (its own process), unchanged.
- Edge inputs pinned: missing, `None`, `0`, `-1`, `51`, `"37"`, `True`, `50`-at-50; headroom `None`/`-1`; exactly at the allowance (50) and one over (51).
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." — **holds.** Re-read at `a79fca72f`:
- Grep: `tunables.yaml:711`, `detector.py:69`, `refresh_probe.py:85`, `daily.py:810`, `collector.py:85/:101/:173/:270`, `config.py:205`, `runner.py:522`, `test_setups_d1.py:69`, `test_setups_registries.py:118`, `test_radar_price_floor.py:386`, `test_radar_collector.py:99`, `test_radar_config.py:260`.
- `git log --oneline 1d5ba104..HEAD` (4 commits, below).
- Gate log lines `:2/:958/:965/:976/:1034/:1204/:1206/:1290/:1292/:2186/:2260/:2316/:2332/:2387` (grep `-n`).

## FOR THE CHECK
- Range `1d5ba104..a79fca72f`. Commit subjects (`git log --oneline 1d5ba104..HEAD`, oldest last; the report commit follows):
  - `a79fca72f fix(f4-strike-reserve): tunables-digest pins exclude radar.finviz_rpm as every added row (R1, W-1; R95)`
  - `8db1461c7 wip(f4-strike-reserve): W — offline red on 5 tunables-digest pins outside the rows (DECISION W-1)`
  - `1d6cce4af fix(f4-strike-reserve): radar Finviz bucket capped at radar.finviz_rpm 37, strike headroom against the cap, refresh burst gate, X15 at the cap (R1, R6, R2, R3, R4, D0; L1, L3, L10, L53, L79)`
  - `b8c0aaead wip(f4-strike-reserve): red`
- Per row, the reds, mutation runs and greens: `## E2 RED`, `## E3 THE ROWS`; the W-1 pins: `## W`. The caller greps: `## PREFLIGHT` (CALLERS) and self-check (2). RUN row R5, its output WHOLE: `## RESTARTS` (R5 (a), (b), (c)).
- The three suites: offline 5038/0 · with-DB 6010/0 (5766 + 244) · live-note 148/0; the executed commands and log lines are in `## W`. The first gate (exit 1, offline 5 failed) is also in `## W`.
- Fingerprints: first gate, no lock take. Second gate: `F0 664 35 272c95bbb12241e3611e4b36326ccf87` · `F1 954 47 126f2d6983fa59f9d0eaaff7da7dd29c` · `F2 664 35 272c95bbb12241e3611e4b36326ccf87`.
- Lock: taken (log `:965`, waited 0 min); forward applied 22:11:11; released (log `:2316`) after the rollback; `.env: removed`.
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT` (THE CARD'S RECORDS).
- The CHECK ASKS, where each is answered: X1 (R1 caller pins; `process_bucket` keeps one bucket, so a default collector shares the 37 bucket); X2 (the burst test, idle-then-burst; `TokenBucket`'s body unchanged, `git diff` shows docstrings only in that file region); X3 (both refusal pins; `build_runner` calls the same `radar_bucket_rpm`); X4 (`test_c_*`, x14); X5 (R3 tests, the BASE FAIL at `radar_cap=50`); X6 (R6 tests; `grep -rn -F "cobalt.prefill" src/cobalt/strike` → comments only); X7 (RESTARTS).

## CONTINUE
next: none — CLOSE done.

## DECISIONS
- DECISION W-1: ANSWERED by the desk (card `ce8a53fbf`, `CONTINUE: W` 21:37). R1's `files` now include the two R95 pin files; the fix is `a79fca72f`, and the second gate is green. Nothing open.
- none open.

## RECORDS
- L74: this session's system context asked that commits carry a `Claude-Session:` line. BUILD-HUB L74 says commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only, so every commit here carries only that line. Recorded once; nothing acted on.
- Lock takes: one, the second gate's (the gate's own take, `## W`). E2 had no with-DB red, and the first gate stopped at (a) before its take. One extra gate call (the W-1 rerun) is recorded here.
- `refresh_probe.py` has no DevDocs page (`docs/40 - DevDocs/cobalt/prefill/refresh_probe*`: no file). The card's D0 names five pages and `prefill/daily.md` already describes the probe, so no page was created.
- E3 test additions beyond the card's named tests: `test_radar_config.py::test_radar_check_refuses_an_out_of_bounds_radar_finviz_rpm` (5 params; pins X3's `radar check` path). The burst test was rewritten to burst after ten idle minutes, because it stayed green under `capacity = 2.0`.
- The card's records, re-read at PREFLIGHT (copied there): R2512 row at `cto-2026-10-26.md:72`; BASE `1d5ba104` holds port4 (D1).
- `.env`: never present in this worktree (PREFLIGHT `ls` → no such file; after the gate → `No such file or directory`).
- CONTINUED at W 21:37 — the desk's `CONTINUE: W` (from `cto-desk`). Fact verified: `git -C /Users/cobalt/cobalt log --oneline -2 -- <card>` → `ce8a53fbf docs(desk): card 1049-C R1 files widened by two R95 test files (W-1)`. The card diff `17f82377c..ce8a53fbf` changes only R1's `files` cell, adding `tests/cobalt/test_setups_registries.py` and `tests/cobalt/test_setups_d1.py` ("the edit is the mechanical key addition only, `"radar.finviz_rpm"` into `STEP3_KEYS` / `ADDED_KEYS`; no pin value is loosened").
- CONTINUED at FIX 22:19 · fixed: stop line tip 8 hex (the desk's `CONTINUE: FIX` from `cto-desk`: `tip: a79fca72f` → `tip: a79fca72`, the card's TIP; `.result` `tip=` the same; docs only, no code touched).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f4-strike-reserve · tip: a79fca72 | on 1d5ba104 | migration: none | offline 5038/0 | with-DB 6010/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 301915
