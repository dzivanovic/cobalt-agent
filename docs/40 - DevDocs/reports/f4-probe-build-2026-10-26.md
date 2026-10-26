# f4-probe — build report 2026-10-26

## §0 Headline

- `prefill probe X15` is built: dev only, in process on one virtual clock, a mock transport that counts every request per minute and answers 429 past the 50th. The radar is a stand-in at 40 rpm; the strike loop is the real `StrikeDetector.tick` over 5 constructed ARMED cards; the refresh is the real `_gated_fetch` at 08:43.
- Two X7 pins added (missing/None refresh tunable refused; the daymode unit keeps one `as of` line after `daymode.note.write`). Both were green on BASE.
- Three suites green on `2e0d5f77b`: offline 4993/0, with-DB 5965/0, live-note 148/0. `cobalt_dev` is back at 0013 (F2 = F0), `.env` removed, RESTARTS: none.
- Not a RUN row: a mutation run printed the default X15 shape as `FAIL`, peak 53/min at 08:43, 3 × 429 (DECISION 3). The gate seat's run decides.

## L74

One block arrived as a system reminder mid-session, asking that commit messages also carry a `Claude-Session:` line. Recorded once here; acted on none. Every commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION

`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0, whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-26/1047-f4-probe-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-26/1047-f4-probe-card.md" · 0 · 11ac13c7c7f5e232e143d799ac265193960245e5
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-26/1047-f4-probe-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 90:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:

```
clock · date · 0 · Mon Oct 26 08:14:09 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-probe
head · git log --oneline -1 · 0 · 596ca32ff docs(desk): R2470 f4-gate-run done, X9 asked of the brain
diff · git diff --stat 596ca32f · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f4-probe · 0 · 596ca32ff docs(desk): R2470 f4-gate-run done, X9 asked of the brain
env here · ls /Users/cobalt/cobalt-wt/f4-probe/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat 596ca32f` | 0 | `596ca32ff docs(desk): R2470 f4-gate-run done, X9 asked of the brain` · `docs/40 - DevDocs/reports/cto-2026-10-26.md | 5 +--` · `.../40 - DevDocs/reports/f4-gate-run-2026-10-26.md | 41 ++++` · `2 files changed, 44 insertions(+), 2 deletions(-)` |
| P1 main | `grep -n -F "def main" src/cobalt/prefill/cli.py` | 0 | `77:def main() -> None:` (refresh parser read at `:88-93`) |
| P2 env | `grep -n -F "def resolve_env" src/cobalt/env.py` | 0 | `60:def resolve_env() -> str:` |
| P2 clients | `grep -n -F "httpx.AsyncClient(" src/cobalt/archiver/collector.py src/cobalt/prefill/market.py src/cobalt/prefill/calendar.py` | 0 | `collector.py:222`, `market.py:68`, `calendar.py:52` (each `async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:`) |
| P2 every client | `grep -rn -F "httpx.AsyncClient(" src/cobalt` | 0 | the three above plus `prefill/checkpoints.py:232`, `aset/prefill.py:55` (not on the X15 path; the probe's client patch covers every `httpx.AsyncClient` alike) |
| X15 symbols | `grep -n -E "async def finviz_get\|async def fetch_bars\|class TokenBucket\|class StrikeDetector\|class DemandPlan\|async def tick\|def read_plan\|def poll_interval" …` | 0 | `archiver/collector.py:205 finviz_get`, `:255 fetch_bars`, `radar/collector.py:42 TokenBucket`, `strike/detector.py:80 DemandPlan`, `:103 poll_interval`, `:131 StrikeDetector`, `:238 tick`, `:313 read_plan` |
| X15 refresh | `grep -n -E "async def _gated_fetch\|def check_refresh_demand\|def refresh_demand_consumer\|async def fetch_market_table\|…" …` | 0 | `daily.py:759 refresh_demand_consumer`, `:780 check_refresh_demand`, `:800 _gated_fetch`, `market.py:55 fetch_market_table`, `calendar.py:62 fetch_economic_events`, `:83 fetch_earnings_events` |
| T2 daymode | `grep -n -E "^def render_body\|^def write\|format_stamp\(" src/cobalt/daymode/note.py` | 0 | `83:def render_body(`, `105: format_stamp(...)`, `140:def write(` |
| T2 config | `grep -rn -F "def load_daymode_config" src/cobalt/daymode` | 0 | `config.py:309:def load_daymode_config(sheet_modes=None) -> DayModeConfig:` |
| FINAL rows | `grep -n -E "…X7…X15" "docs/30 - Design/F4-FINAL-2026-10-10.md"` | 0 | `213:| X7 | Config, clock, rendering: …` · `221:| X15 | Strike loop and refresh in one minute (Opus seat, round 3) | … "dev, 5 synthetic ARMED cards, radar planned 40, ceiling 50, …"` |
| tunables | grep of `configs/cobalt/taxonomy/tunables.yaml` | 0 | `702: - key: radar.finviz_max_rpm` / `703: value: 50`; `735 strike.poll_interval_min 2`; `744 strike.max_armed 5`; `1148 prefill.refresh_window "05:45-15:45"`; `1160 prefill.refresh_interval_min 30` |
| wc | `wc -l src/cobalt/prefill/cli.py tests/cobalt/test_prefill_refresh.py "…/prefill/cli.md" "…/prefill/daily.md"` | 0 | `113`, `1268`, `42`, `160` |
| READ reports | — | — | `## READ` names no report |
| restarts | `uv run cobalt jobs restarts 596ca32f..HEAD` | 0 | `docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md A DOCS -` (this uncommitted report, in the working tree) · `RESTARTS: none` |

Records copied from the card (`## RECORDS`):
- F4 gate 1045 — X15 load gate by probe card f4-probe (+X7 two offline tests) — brain 9b07db5a. Re-read: `grep -n -F "| R2463 " ".../reports/cto-2026-10-26.md"` → `25:| R2463 | 07:57 ET | DESK RECORD (brain 9b07db5a, L79): F4 gate 1045 — … X15 load gate by probe card f4-probe (+X7 two offline tests); … | APPROVED — pending fold |`. `git -C /Users/cobalt/cobalt log --oneline -1 9b07db5a` → exit 128 `unknown revision` (the brain's hash is not a commit of this repo; not re-readable from my list).
- DECISION 1 (in process, virtual clock, mock transport), DECISION 2 (radar stand-in at 40 rpm through `finviz_get`), DECISION 3 (BAND HIGH): the drafter's; built as written.
- ARITHMETIC (drafter, not a result): headroom 10, 5 names → `poll_interval` 30 s = 10 rpm; radar 40 + strike 10 = 50; refresh's 3 GETs fall in one minute. Re-read: `strike/detector.py:103-108` as quoted.
- RULINGS R1863: proved by `authorize.sh` above.

The with-DB strings are proven at W's first take (no with-DB red in this card).

## E0 BASELINE

- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4974 passed, 878 skipped, 4 xfailed, 36 warnings in 746.80s (0:12:26)`. The one skip naming `COBALT_LIVE_VAULT_ROOT` (`test_predicate.py:262`) belongs to this offline run.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 26.44s`. The skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, and none names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_refresh_probe.py tests/cobalt/test_prefill_refresh.py -k "test_refresh_probe or x7_"` → `2 failed, 4 passed, 74 deselected, 13 errors in 0.88s`. All 14 probe tests are red for the row's reason (P1, P2, X15, C1). The 13 that use the `probe` fixture error at setup, and `test_the_probe_is_mounted_and_lists_x15` fails, each with the same first line:
`AssertionError: usage: prefill [-h] {daily,refresh} ... prefill: error: argument command: invalid choice: 'probe' (choose from daily, refresh)`.
T1 (4 parametrized cases) passed on BASE. T2 first failed on BASE, but not on behaviour: the card's "real `load_daymode_config()`" opens the database (`daymode/config.py:309-326` → `TraderSettings.from_db()` → `DbConfigError: Missing Postgres settings for the APP credential …`). I rewrote it to use `test_daymode_note._cfg()`, the offline config the daymode tests use (DECISION 1). After that: `uv run pytest … tests/cobalt/test_prefill_refresh.py -k x7_` → `5 passed, 74 deselected in 0.78s`, so T1 and T2 are green on BASE as the card expected. No with-DB red, so no lock was taken. Commit `5e03b1db5 wip(f4-probe): red — probe tests, the two X7 pins (P1, P2, X15, C1, T1, T2)`.

## E3 THE ROWS

- P1/P2/X15/C1: new `src/cobalt/prefill/refresh_probe.py`. `prefill/cli.py` gets a `probe` parser with `item` (`choices=PROBE_ITEMS`); its handler runs before the `try`, outside `as_job`, and does `sys.exit(refresh_probe.main(args.item))`.
- After the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_refresh_probe.py` → `14 passed in 93.52s`. The card's offline suite (`test_refresh_probe.py test_prefill_refresh.py test_finviz_consumers.py`) → `65 passed, 28 skipped, 4 xfailed in 97.49s`. After D0, the same three plus `test_placement.py` → `72 passed, 28 skipped, 4 xfailed in 97.51s`.
- THE MUTATIONS. Each was made with Edit, run alone, then undone with Edit; `git diff --stat` afterwards showed only the uncommitted rows' files (`cli.py | 12`, `test_refresh_probe.py | 2`), with `daily.py` and `daymode/note.py` back to clean.

| row | mutation | test | first failing line |
|---|---|---|---|
| P1 | `add_parser("probe-mutant"` | `test_the_probe_is_mounted_and_lists_x15` | `invalid choice: 'probe' (choose from daily, refresh, probe-mutant)` · 1 failed |
| P2 (a) | `_dev_only()` call removed | `test_production_and_unset_env_are_refused` | `assert (1, 'PROBE X1...L :221, L75)') == (1, 'PROBE X1...n (dev only)')` · 1 failed |
| P2 (b) | the `AsyncHTTPTransport.handle_async_request` guard removed | `test_a_request_off_the_mock_transport_fails` | `assert (0, 'PROBE X1...ate admitted') == (1, 'PROBE X1...rror network')` · 1 failed |
| P2 (c) | the `market.resolve_token` patch removed | `test_no_write_no_db_no_token_no_launchctl` | `AssertionError: PROBE X15 FAIL error AssertionError` · 1 failed. Before this run I extended the test to also patch `cobalt.prefill.market.resolve_token` and `calendar.resolve_token` to raise, so that it pins those names. |
| X15 pass rule | `if peak > ceiling or throttled:` → `if False:` | `test_x15_a_minute_above_50_fails_and_names_the_consequence` | `PROBE X15 OK peak 63/min at 08:43 · … · 429 63 (radar=56, strike=7) …` `assert (0 == 1)` · 1 failed |
| X15 ceiling at the mock | `in_minute >= self.ceiling + 100` | same | `assert 200 == 429` · 1 failed |
| X15 redirect | the 302 hop returned unrecorded | `test_x15_a_redirect_is_counted` | `assert [200, 200] == [302, 200]` · 1 failed |
| X15 gate | `if ledger.refresh.refused is not None:` → `if False:` | `test_x15_refresh_gate_refusal_is_not_run` | `assert 0 == 3` · 1 failed |
| X15 count | minute count drops `refresh` | `test_x15_counts_every_consumer_per_minute` | `{'08:43': 40} != {'08:43': 43}` · 1 failed |
| X15 clause | `records[0].path` appended to the clause | `test_x15_clause_holds_no_query_or_token` | `AssertionError: /export` · 1 failed |
| C1 control | `choices=PROBE_ITEMS` removed | `test_an_unknown_item_is_refused` | `assert 1 == 2` · 2 failed (X7, X99) |
| C1 line | `EXIT = {OK: 0, FAIL: 0, NOT_RUN: 0}` | `test_x15_prints_one_line_and_exits_by_verdict` | `assert 0 == 1`, `assert 0 == 3` · 2 failed, 1 passed (the OK case, unaffected) |
| T1 | `daily.py:767` `… or rows[k].value is None` removed; then `k not in rows and False` | `test_x7_a_missing_or_unmeasured_refresh_tunable_is_refused` | `TypeError: int() argument must be … not 'NoneType'` · 2 failed; then `KeyError: 'prefill.refresh_interval_min'` · 4 failed |
| T2 | `daymode/note.py:105` stamp line and its blank removed | `test_x7_the_daymode_unit_still_starts_as_of_after_a_later_daymode_write` | `re.match('^as of \\d\\d:\\d\\d ET$', '**Day mode: REDUCED** — stage-1 · …')` · 1 failed |

- D0: one `## 2026-10-26 — f4-probe` section appended to `docs/40 - DevDocs/cobalt/prefill/cli.md` and one to `…/prefill/daily.md`.
- Commit `2e0d5f77b feat(f4-probe): prefill probe X15 on a virtual clock, the two X7 pins (P1, P2, X15, C1, T1, T2, D0; L1, L3, L28, L32, L45)`.
- DEPLOY PROOF reads on this tree (the "before" reads belong to the deploy):
  - `ls …/f4-probe/src/cobalt/prefill/refresh_probe.py` → listed
  - `grep -c -F "PROBE_ITEMS = (" …/refresh_probe.py` → `1`
  - `grep -c -F "test_x7_the_daymode_unit_still_starts_as_of_after_a_later_daymode_write" …/test_prefill_refresh.py` → `1`
  - `ls /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` → listed

## RESTARTS

`uv run cobalt jobs restarts 596ca32f..HEAD` (R1) → exit 0, whole:

```
path	change	rule	restart
docs/40 - DevDocs/cobalt/prefill/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-probe-build-2026-10-26.md	A	DOCS	-
src/cobalt/prefill/cli.py	M	static import reach	-
src/cobalt/prefill/refresh_probe.py	A	static import reach	-
tests/cobalt/test_prefill_refresh.py	M	test/documentation; no resident	-
tests/cobalt/test_refresh_probe.py	A	test/documentation; no resident	-
RESTARTS: none
```

No UNCLASSIFIED row. `grep -rn -F "refresh_probe" src configs` → only `prefill/cli.py:96,98,105,107` and the module itself. No resident and no `configs/` entry reaches it (X6).

## W THE THREE SUITES

`sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-probe all --deploy` (no `--deselect`, no `--tickers`: this build adds no with-DB test and writes no ticker to `cobalt_dev`) → exit 0, the verdict lines whole:

```
tests/ops: skipped (no ops paths)
offline 4993/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5965/0
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
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-probe-all-20261026-084152.log
```

No SKIPPED line is marked `OUTSIDE the allowed set`.

- (a) offline: `4993 passed, 878 skipped, 4 xfailed, 36 warnings in 818.46s` (log :957). `<p>` = 4993 = E0's 4974 + the 19 this build adds (14 in `test_refresh_probe.py`, 5 in `test_prefill_refresh.py::TestStamp` x7_).
- (b) `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :975), `LEVEL 0013`.
- (c) PASS 1, executed command (log :1033): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect …` (the gate-lists' 29 standing `--deselect`s; none added by this build) → `5721 passed, 9 skipped, 138 deselected, 7 xfailed, 43 warnings in 986.72s` (log :1203).
- (c3) PASS 2 → `244 passed, 1 deselected, 5 warnings in 245.91s` (log :2186). `<d>` = 5721 + 244 = 5965. This build has no with-DB test of its own.
- (c3r) `stray rows: not read (no --tickers given)`: this build writes no ticker to `cobalt_dev`.
- (e) live-note → `148 passed, 1 skipped, 15 warnings in 26.60s` (log :2387).
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (log :2260) = F0 → `cobalt_dev: 0013 — F2 = F0`. Lock: `lock taken: f4-probe` (log :964, `lock: waited 0 min`), `lock released` (log :2316). `ls /Users/cobalt/cobalt-wt/f4-probe/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK

1. Every added test was shown red. The 14 probe tests are red on BASE with `invalid choice: 'probe'` (E2). T1 and T2 are pins, green on BASE. Every test is also red under its E3 mutation (table above). `test_no_write…` was strengthened before its mutation run; no named test stayed green under its own mutation.
2. Entry paths:
   - `refresh_probe.main` has one caller, `cli.py:107` (grep in RESTARTS), pinned by every probe test through `cli.main()`.
   - The flag combinations are pinned: env production / unset (P2), items X15 / X7 / X99 (C1), and the three verdicts (C1 parametrized).
   - `_gated_fetch`'s other callers (`daily.py:845`, `:1113`) are unchanged and pinned by `test_prefill_refresh.py`.
   - Both refusal keys and both shapes (absent, None) are pinned by T1's 4 cases.
3. Every figure in this report was re-read from tool output at the tip:
   - `grep -n -F "F0: "` / `"F2: "` / `"pass 1: whole (deploy)"` / `"passed"` on the gate log
   - `grep -rn -F "refresh_probe" src configs`
   - the three DEPLOY PROOF reads
   - `git commit` outputs for both commits

## FOR THE CHECK

- `596ca32f..2e0d5f77b`:
  - `5e03b1db5 wip(f4-probe): red — probe tests, the two X7 pins (P1, P2, X15, C1, T1, T2)`
  - `2e0d5f77b feat(f4-probe): prefill probe X15 on a virtual clock, the two X7 pins (P1, P2, X15, C1, T1, T2, D0; L1, L3, L28, L32, L45)`
- Reds, mutations and greens per row: `## E2 RED`, `## E3 THE ROWS`.
- Caller greps: `## PREFLIGHT` (symbols, the five `httpx.AsyncClient(` sites) and `## RESTARTS` (`refresh_probe` callers).
- R1 (RUN row) output: `## RESTARTS`, whole.
- Three suites, the executed pass 1 command, and F0 / F2: `## W`. `<F1>`: not taken (no migration, no FORWARD). Lock taken and released inside `gate.sh` (log :964, :2316).
- Records copied at PREFLIGHT: `## PREFLIGHT`.
- For the check's X3: `_strike` awaits the real `StrikeDetector.tick` with `fetch=fetch_bars`. `_refresh` awaits the real `daily._gated_fetch`, which runs its own gate and then `fetch_market_table`, `fetch_economic_events` and `fetch_earnings_events`. `ProbeTransport.handle` records every hop, a 302 included.

## CONTINUE

next: none (BUILT) — the desk verifies and launches the check

## DECISIONS

- DECISION 1 (T2): the card names "the real `load_daymode_config()`", but it reads `"user".trader_settings` (`daymode/config.py:309-326`) and raised `DbConfigError` offline. Safe default taken: the offline row uses `test_daymode_note._cfg()`, a valid `DayModeConfig` with the `reduced` rung. What the pin proves (one `as of` first line after `daymode.note.write`, bytes outside the unit unchanged) is the same.
- DECISION 2 (test_finviz_consumers): `refresh_probe.py` hands `finviz_get` and `fetch_bars` to its consumers by reference and never spells `elite.finviz.com`. The inventory regex in `test_finviz_consumers.py` therefore does not list it, and that file passes unchanged. Every request it makes ends at its `MockTransport`, and a real transport is stopped (`FAIL error network`), so it is not a consumer of the real ceiling. Safe default: no inventory entry (the file is outside the rows). ASK DESK: should a future live variant of X15 (DECISION 1 of the card, the brain's) add `prefill/refresh_probe.py` to `CONSUMERS`?
- DECISION 3 (X15, UNPROVEN, L70): this was not a RUN row and no probe was run outside a test. The P2 (a) mutation run printed the default X15 shape (5 cards, radar 40, plan 40/10, ceiling 50) as `PROBE X15 FAIL peak 53/min at 08:43 · per minute 08:40=50, 08:41=50, 08:42=50, 08:43=53, 08:44=50, 08:45=50 · radar 240 · strike 60 · refresh 3 · 429 3 (radar=3) · strike interval 30 s · refresh gate admitted → strike/refresh residual cannot ship as named; …`. This matches the card's ARITHMETIC: radar 40 + strike 10 = 50, plus 3 refresh GETs in one minute. If the gate seat's run shows the same, FINAL `:221`'s strike-side reservation row is owed on its own card before the refresh plist loads (L75). Not fixed here.

## RECORDS

- `.env: removed, proven gone (W)`: `ls /Users/cobalt/cobalt-wt/f4-probe/.env` → `No such file or directory`.
- No extra lock take; no command refused; no CONTINUE received.
- L74: one system-reminder block asked for a `Claude-Session:` commit line; not followed (`## L74`).
- `git -C /Users/cobalt/cobalt log --oneline -1 9b07db5a` → exit 128: the brain's hash in the card's first record is not a commit in this repo.
- The card's records, as re-read at PREFLIGHT: see `## PREFLIGHT`.
- Run time: a small-setup X15 run takes about 17 s. Each strike tick re-reads the tunables and the job registry through `check_strike_demand` (real code, unchanged). `test_refresh_probe.py` takes about 93 s whole.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: f4-probe · tip: 2e0d5f77b | on 596ca32f | migration: none | offline 4993/0 | with-DB 5965/0 | live-note 148/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 264605
