# f4-refresh-1010 — build report (F4-1, `prefill refresh`)

## §0 Headline
F4-1 `prefill refresh` is built on `ops/f4-refresh-1010`. The check fixed five findings (`98174119`); this fix round (R998) is at tip `edd5c076`. Fixed: X16 (his hand-typed stub table is never wrapped), X12 (a refresh that sees another's commit in flight writes nothing and exits 1; no lock), A4 (the create's day-mode block takes the caller's `when`). B5 is pinned: a refresh-created note equals `prefill daily`'s, byte for byte.
Deploy gate on `edd5c076` green: offline 4245/0, with-DB 5173/0, live-note 146/0. `cobalt_dev` is at 0013 (F2 = F0), no migration. RESTARTS: `com.cobalt.aset com.cobalt.radar`, and the new plist is bootstrapped once.
Three items for Dejan stay strict xfails: T2b (kept, R998), O1/A3 (carried: the degraded age needs a migration, so a follow-up card), and O2 (kept, FINAL :100).

## L74
A system notice in this session asked for a `Claude-Session:` line on commits. Recorded here once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md"` (19:10:35 EDT, `date`), output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md" · 0 · 3ec87ff8086dcd57b10e698458b2cad9e8c7f455
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-10 R849 row · grep -n "^| R849 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 136:| R849 | 07:13 ET | HIS RULING · APPROVED: option A, S5 pulled forward: build as much as possible this weekend, F4 then F5; he asks the brain for the full not-MVP list. Words: `cto-2026-10-10-words.md` R849. | APPLIED: areas/cobalt.md NOW at wake-up 07:55 |
RULING 2026-10-10 R849 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R849 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 2ef44c847a7c0c61e1f97f236fa50b9f8e991289
RULING 2026-10-10 R849 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
RULING 2026-10-10 R969 row · grep -n "^| R969 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 17:| R969 | 18:51 ET | HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL (`docs/30 - Design/F4-FINAL-2026-10-10.md`) and ops-hand D1-D5; words: `cto-2026-10-10-words.md` R969. Next: F4 card, F5 F20 F21 F23 re-point, ops-hand install. | APPLIED: LAWS.md L63, NOW at wake-up 18:55 |
RULING 2026-10-10 R969 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R969 |" -- "docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · 8f5586abab5f095375e2759a2377d91fc0f54d5c
RULING 2026-10-10 R969 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-10.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | see block below |
| BASE | `git show --stat d78c66a2` | 0 | `d78c66a2 docs(desk): R971 his Yes both confirms R969` · 2 files changed, 4 insertions(+) (`cto-2026-10-10-words.md` +3, `cto-2026-10-10.md` +1) |
| restarts, empty range | `uv run cobalt jobs restarts d78c66a2..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |
| callers `upsert_unit(` | `grep -rn -F "upsert_unit(" src/cobalt` | 0 | 18 hits: `drc/build.py:905`, `prefill/daily.py:583`, `prefill/trade_note.py:474`, `:522`, `daymode/note.py:159`, `heartbeat/runner.py:205`, `taxonomy/catalyst.py:404`, `taxonomy/cli.py:225`, `:516`, `taxonomy/note_migration.py:872`, `:880`, `replay/line.py:223`, `vaultwrite/writer.py:673` (def), `radar/propose.py:756`, `aset/daily_note.py:185`, `seatusage/runner.py:126` (plus `drc/build.py:29` docstring) |
| callers `merge3(` | `grep -rn -F "merge3(" src` | 0 | `merge.py:100` (def), `merge.py:171` (`merge_body`), `writer.py:735`, `:746`, `:762`, `:980` |
| callers `render_body(` | `grep -rn -F "render_body(" src` | 0 | `prefill/daily.py:405`, `daymode/note.py:83` (def), `daymode/note.py:163`; (`prefill/trade_note.py:140`, `:264` are `_render_body`, another function) |
| importers of `prefill.daily` | `grep -rn -F "from .daily import" src` | 0 | `prefill/drc.py:78`, `prefill/cli.py:25` (the `radar/anatomy/*` hits import `radar/anatomy/daily.py`, another module) |
| `read_plan` | `grep -n -F "def read_plan" src/cobalt/strike/detector.py` | 0 | `313:def read_plan() -> DemandPlan:` |
| `check_scheduled_demand` | `grep -n -F "def check_scheduled_demand" src/cobalt/radar/notes.py` | 0 | `384:def check_scheduled_demand(subject: str, *, radar_rpm: float \| None = None,` |
| `calendar_entries` | `grep -n -F "def calendar_entries" src/cobalt/jobs/config.py` | 0 | `198:    def calendar_entries(self) -> list[dict[str, int]]:` |
| `overrides_for` | `grep -n -F "def overrides_for" src/cobalt/vaultwrite/store.py` | 0 | `232:    def overrides_for(self, note: str) -> list[dict[str, Any]]:` |
| `to_et` | `grep -n -F "def to_et" src/cobalt/session/clock.py` | 0 | `262:    def to_et(ts: datetime) -> datetime:` |
| `daily_note_path` | `grep -n -F "def daily_note_path" src/cobalt/daymode/note.py` | 0 | `238:def daily_note_path(day: Optional[date] = None) -> Path:` |
| sizes | `wc -l <the rows' files>` | 0 | `daily.py` 594 · `cli.py` 74 · `config.py` 163 · `market.py` 96 · `writer.py` 1394 · `merge.py` 171 · `daymode/note.py` 270 · `prefill.yaml` 17 · `jobs.yaml` 352 · `tunables.yaml` 1075 · `daily.md.j2` 99 · `s2.yaml` 636 · `test_jobs.py` 932 · `test_jobs_reads.py` 238 · `test_finviz_consumers.py` 174 · `test_prefill_daily.py` 428 · `test_daymode_note.py` 228 |
| `## READ` report tail | `tail -n 3 "docs/30 - Design/F4-FINAL-2026-10-10.md"` | 0 | last line `none` (under `## OWNER ITEMS`) |

```
clock · date · 0 · Sat Oct 10 19:10:38 EDT 2026
status · git status --short --branch · 0 · ## ops/f4-refresh-1010
head · git log --oneline -1 · 0 · d78c66a2 docs(desk): R971 his Yes both confirms R969
diff · git diff --stat d78c66a2 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/f4-refresh-1010 · 0 · d78c66a2 docs(desk): R971 his Yes both confirms R969
env here · ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card `## RECORDS`, copied: HOUSE B at the check `mandatory — vault notes`; WRITER GATE (X7's Obsidian render, X8, X9, X10's real-note `--dry-run`, X15 need the live Mac, owed before the bootstrap); FINAL cites re-proved at BASE `d78c66a2` with the corrections listed in the card; PRECEDENT `01-drc-k3-card.md` shape; LADDER fallback; RESTARTS per FINAL SEAM §8 (aset, radar, the new one-shot loaded; the derived set is R1's); AMEND of the RESTARTS class home. Re-read here: `writer.py:556` is the `_commit` call inside `_persist_and_write` (Read, `writer.py:555-556`); `writer.py:836-839` is `_baseline` (Read); `strike/detector.py:313-319` is `read_plan` (grep above); `daily.py:479` is `datetime.now().astimezone()` (Read).

`<FP>`, copied whole before any run:
`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"`

## E0 BASELINE
On `d78c66a2`, no file changed (19:13 EDT start, `date` 19:12:58 before it):
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `4199 passed, 800 skipped, 1 xfailed, 36 warnings in 706.04s (0:11:46)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.20s`; the one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests written, no `src/` edit: `tests/cobalt/test_prefill_refresh_experiments.py` (A1, new), `tests/cobalt/test_prefill_refresh.py` (new; every new name imported inside each test), `tests/cobalt/test_daymode_note.py` (+3, X7), `tests/cobalt/test_prefill_daily.py` (the create test's template-shape assertions; every `when` moved to an aware ET instant, because the [F-30] rules stamp goes through `SessionClock.to_et`, which refuses a naive `when`).

**Offline**: `uv run pytest -q -p no:cacheprovider --color=no --tb=no -rfp <the four files>` → `42 failed, 28 passed, 41 skipped in 0.29s`. Every red's first line, by row:
- C1 (10 tests): `ImportError: cannot import name 'load_daily_refresh_config' from 'cobalt.prefill.config'` (and `'DailyRefreshConfig'`).
- C2 / T10 (6): `JobConfigError: unknown job label 'com.cobalt.prefill-refresh'`; `test_the_tunables_are_proposed_dwv` → `KeyError: 'prefill.refresh_interval_min'`; `test_the_smoke_row_watches_the_job` → `assert 0 == 1`; `test_the_template_names_both_one_shot_readers` → `assert ['com.cobalt.prefill-daily'] == ['com.cobalt....fill-refresh']`.
- M1 T3b: `AssertionError: assert ['| SPY | 11 ...33 |', 'NOTE'] == ['| SPY | 11 ...| IWM | 33 |']` / `At index 1 diff: '| QQQ | 22 |' != 'NOTE'` (NOTE comes after the replaced block). NEGATIVE CONTROL `test_negative_control_unequal_spans_keep_todays_order` PASSED on BASE.
- S1 T13 (12), T6 render half, X7: `ImportError: cannot import name 'format_stamp'` / `'refresh_note_path'` / `'stamp_context'`; `test_daymode_note.py` `TypeError: render_body() got an unexpected keyword argument 'when'` (2).
- D1 T5/X5: `ImportError: cannot import name 'run_daily_refresh'`; `test_x5_the_exception_leaves_the_as_job_block` → `AttributeError: <module 'cobalt.prefill.cli'> has no attribute 'run_daily_refresh'`; `test_prefill_refresh_is_a_subcommand` → `AttributeError … no attribute '_run_refresh'`.
- G1 (L53, X13 ×2, X14 ×3): `ImportError: cannot import name 'run_daily_refresh'` (the first call of each test).
- E1 T12: `ImportError: cannot import name 'run_daily_refresh'`.
- `test_prefill_refresh_experiments.py::test_a1_4…` (offline, prints only) PASSED.

**With-DB, ONE lock take** (19:32:23 EDT): `sh …/take-devdb-lock.sh f4-refresh-1010 90` → `lock taken: f4-refresh-1010` (exit 0); `ls -la /Users/cobalt/cobalt-wt/*/.env` → one line, `/Users/cobalt/cobalt-wt/f4-refresh-1010/.env`. `<FP>` → `<F0>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `TABLES 0011` / `FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`, `NOTHING WAS APPLIED`, which is `ops/desk/gate-lists.md:47-48` `## LEVEL 0013` exactly. NO forward.
- `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider --color=no --tb=no -rfxXp tests/cobalt/test_prefill_refresh.py tests/cobalt/test_daymode_note.py tests/cobalt/test_prefill_daily.py` → `66 failed, 40 passed, 1 xfailed in 2.91s`. The with-DB reds beyond the offline ones: every `TestOwnership`, `TestConcurrency`, `TestCreateStubDryRun`, `TestUntouchedUnits` test → `ImportError: cannot import name 'run_daily_refresh' from 'cobalt.prefill.daily'`; W1 `TestBodyFn::test_x4_body_fn_runs_on_every_attempt…` → `TypeError: VaultWriter.upsert_unit() got an unexpected keyword argument 'body_fn'` (its NEGATIVE CONTROL `test_negative_control_without_body_fn…` PASSED); X7 `test_f4_x7_the_stamp_is_there_once_after_a_second_write` → `assert [] == ['as of 10:00 ET']`; S1 `test_prefill_daily.py::test_create_path_renders_full_template` → `assert '<!-- cobalt:unit rules -->\nas of 05:15 ET · rules from Rules.md\n\n' in "---\ntags:…`; the X16 hand-typed leg is `XFAIL` (strict, the card's reason); every existing `test_prefill_daily.py` / `test_daymode_note.py` test PASSED with the aware `when`.
- A1 RUN, `COBALT_ENV=dev uv run pytest -q -rP -p no:cacheprovider --color=no tests/cobalt/test_prefill_refresh_experiments.py` → `4 passed in 0.49s`, output WHOLE (the purge line `vault_writes: purged 184 row(s) past 30-day retention` printed under each with-DB test is inside the rolled-back transaction):
```
A1-1 after his 06:00 edit: '| SPY | $512.34 his 06:00 | +9.99% |'
A1-1 call 1: action=unchanged overrides=1 SPY line='| SPY | $512.34 his 06:00 | +9.99% |' his line present=True
A1-1 call 2: action=updated overrides=0 SPY line='| SPY | $502.00 | +0.11% |' his line present=False
A1-1 call 3: action=updated overrides=0 SPY line='| SPY | $503.00 | +0.11% |' his line present=False
A1-2 last_after(trading/market_table) is None=False equals unit on disk=True value='| VIX |     |     |\n| --- | --- | --- |\n| SPY | $500.00 | +0.10% |\n| QQQ | $400.00 | +0.20% |\n| IWM | $200.00 | +0.30% |\n| BTC |     |     |'
A1-2 last_after(market_calendar/market_calendar) is None=False equals unit on disk=True value='- 08:30 ET — CPI'
A1-2 _render_template({}) raised nothing; 100 lines; trading unit body=['| VIX |     |     |', '| --- | --- | --- |', '| SPY |  |  |', '| QQQ |  |  |', '| IWM |  |  |', '| BTC |     |     |']
A1-2 _render_template({}) header line='####  T ' daily stop line='Daily HARD Stop: '
A1-3 plain stub: action=updated notes=["anchor not found (the market table under '### Trading') — section appended at the end of the note; nothing above it was touched (L28)."]
A1-3 plain stub: unit after='| VIX |     |     |\n| --- | --- | --- |\n| SPY | $501.00 | +0.11% |\n| QQQ | $401.00 | +0.21% |\n| IWM | $201.00 | +0.31% |\n| BTC |     |     |'
A1-3 plain stub: last_after equals unit=True
A1-3 plain stub: prefix bytes kept=True
A1-3 typed stub: action=updated overrides=0 notes=[]
A1-3 typed stub: unit after='| VIX |     |     |\n| --- | --- | --- |\n| SPY | $501.00 | +0.11% |\n| QQQ | $401.00 | +0.21% |\n| IWM | $201.00 | +0.31% |\n| BTC |     |     |'
A1-3 typed stub: hand-typed table bytes unchanged=False
A1-4 ADMITTED: peak_rpm=50.0 (49.95 + 0.05 == 50: True)
```
  A1 (1) loses his line at the 2nd call, as FINAL §3 predicts: no `DECISION A1-1`. A1 (3)'s hand-typed table bytes CHANGE: `DECISION A1-3` (under `## DECISIONS`). A1 (2): `last_after` is the unit body after create (not None); `_render_template({})` renders empty for missing keys. A1 (4), X17 as data: admitted, peak exactly `50.0`.
- `<FP>` again = `<F2>` = `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = `<F0>`. `sh …/release-devdb-lock.sh f4-refresh-1010` → `lock released`; `ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env` → `No such file or directory` (19:33:47 EDT). `.env: removed, proven gone (E2)`.

## E3 THE ROWS
Commit `fea889b5` `feat(f4-refresh-1010): prefill refresh — the trading and calendar units all day, ownership on every write attempt, form-B shared gate (C1 C2 M1 W1 O1 O2 S1 D1 G1 E1 U1 K1 DOC; L1 L3 L28 L53)` (21 files). Rows in the card's order; every `file:line` re-read before its edit (the Read calls above).

| row | what was built | greens (quoted) | mutation → first failing line (undone, `git diff --stat` back at the fix) |
|---|---|---|---|
| A1 | RUN, E2 (output above) | — | — |
| C1 | `DailyRefreshConfig`, `load_daily_refresh_config`, `REFRESH_UNITS` / `REFRESH_FIELDS` / `NO_SOURCE_FIELDS` in `prefill/config.py`; `daily_refresh:` in `prefill.yaml` | `TestDailyRefreshConfig` + `test_prefill_config.py` + `test_prefill_rules_gen.py` → `34 passed in 0.15s` | `if sourceless:` → `if False and sourceless:` → `2 failed, 8 passed`: `Failed: DID NOT RAISE <class 'cobalt.prefill.config.PrefillConfigError'>` (the VIX and BTC cases) |
| C2 | tunables `prefill.refresh_window` / `prefill.refresh_interval_min` (`proposed`, `dwv`); job row after `prefill-daily`; template readers; `ops/com.cobalt.prefill-refresh.plist` (105 entries); smoke row **K12.3** | `TestTheJobRow` + `test_jobs.py` + `test_jobs_reads.py` + `test_seat_usage.py` → `108 passed, 26 skipped in 4.18s`; `test_smoke.py`, `test_smoke_k3_sql.py`, `test_replay_demand.py`, `test_jobs_restarts.py`, `test_names_rule.py`, `test_session.py`, `test_finviz_consumers.py` → `138 passed, 8 skipped, 1 xfailed` | interval `30` → `20` → `3 failed, 3 passed`: `assert 155 == 105` |
| M1 | `merge3` untouched equal-length replace → inserts at their anchors | `TestMergeInsertAtAnchor` `2 passed`; with-DB `test_vaultwrite.py` whole (34) green unchanged inside the 654 below | `if False and not touched and …` → `AssertionError: assert ['| SPY | 11 ...33 |', 'NOTE'] == …`; NEGATIVE CONTROL broken (`if not touched and True:`) → `AssertionError: assert ['x', 'NOTE', 'y'] == ['x', 'y', 'NOTE']` |
| W1 | `upsert_unit(…, body_fn=None)`, called in `build` each attempt | `TestBodyFn` 2 passed (inside the 654) | `proposal = body` → `assert (0 == 2)` (X4 retry) and X4 two-refresh `KeyError: 'flags'` |
| O1 | `_Refresh.trading_proposal` (from `last_after`; HUMAN by (a)/(b); ticker / manual / stamp lines; sync revert whole-unit), `[F-36+]` baseline check | `TestOwnership` green but T2b (xfail, below) | HUMAN test → `False and …`: `5 failed` — T1 `assert 'VIX human' in 'as of 08:45 ET · SPY cobalt …'`, T2 `assert 'SPY human' in …`, T16a `assert (0 == 1)`, T17 `assert 0 == 1`, X2-dup `assert 0 == 1`. Proposal from the disk (`base = disk_text…`): T3 `assert 2 == 1` (NOTE duplicated), T16b `assert 2 == 1`, T2. `sync_revert = False and …`: T9 `assert ('| SPY | $523.00 | +0.10% |' in …)`. Baseline check off: T15 `RefreshError: FAILED: the trading unit or its baseline vanished …` |
| O2 | calendar whole-unit (`calendar_owned`, `skip_if` per attempt), live flag on the trading stamp, absent-with-his-text skip | T4, `test_o2_his_text_under_the_calendar_heading_is_not_wrapped` green | `return True or (…)` → T4 `assert 'as of 06:15 ... a second one' == 'as of 05:15 ... a second one'` |
| S1 | `format_stamp`, `stamp_context`, `refresh_note_path`; template stamps + VIX/BTC `n/a (manual)`; rules fill body stamped; `render_body(when=…)` | `TestStamp` (12), `TestTemplateShape`, `test_daymode_note.py` 18, `test_prefill_daily.py` green | `when.astimezone()` → `11 failed`: `assert 'as of 12:45 ET' == 'as of 08:45 ET'` … and `DID NOT RAISE <class 'cobalt.session.clock.SessionError'>`; daymode stamp dropped → `3 failed`: `assert ('**Day mode: ...t · keys A, B' == 'as of 09:00 ET'` |
| D1 | degraded carry, age from the last success, no FAILED; `RefreshNotClean` raised inside `as_job` | `TestDegraded` 3 passed | age from the attempt stamp → `assert 'SPY cobalt-degraded (finviz fetch failed; values as of 07:45)' in 'as of 08:15 ET · SPY cobalt-degraded (finviz fetch failed; values as of 08:15) …'`; no raise → `Failed: DID NOT RAISE <class 'RuntimeError'>` |
| G1 | `read_plan` imported from `strike.detector`; `check_refresh_demand`, `refresh_demand_consumer` (3/interval over the window); `_gated_fetch` | `TestSharedGate` 6 passed; T14 `test_finviz_consumers.py` → `3 passed, 1 xfailed` (its xfail untouched; only `:47-48` strings changed) | the refusal ignored (both guards `False and …`) → `5 failed`: `AssertionError: a refused gate issues no GET / assert 9 == 6`, X13 `assert 0 == 1` |
| E1 | `run_daily_refresh`, `ensure_daily_note`, `_ensure_note`, `read_rules_read_only`, stub path; `prefill refresh [--dry-run]`, `REFRESH_JOB` | T8, T11, T12, X6, X16 (run twice), `ensure_daily_note` test green; X16 hand-typed leg XFAIL (strict, card reason) | create through `regenerate_rules_config()` → `AssertionError: regenerate_rules_config was called by refresh` (T12, T8); writer `dry_run=False` → `assert not True … exists()` (T11, T12) |
| U1 | test only (T7) | green | refresh also upserts `rules` → `AssertionError: rules … + MUTATION` |
| K1 | `market.py` docstring; `daily.py:4` four slots | offline green | text only |
| DOC | dated lines in `prefill/daily.md` (+ `## SEAM`, + the F4 PDD), `cli.md`, `config.md`, `market.md`, `vaultwrite/README.md`, `daymode/note.md` | `test_placement.py` → `7 passed in 0.04s` | NEGATIVE CONTROL only |

Tests corrected during E3, named: (1) X12 fired on A's CALENDAR commit (A writes the calendar first) and passed vacuously; it now fires only on A's trading commit and asserts A's values were captured — then RED for its named reason; (2) the smoke row id `K12.2` collided with `test_drc_build.py:1041-1046` (`K12.2` is the retired prefill-drc row, pinned as gone) → renamed `K12.3`. `test_jobs.py` and `test_jobs_reads.py` needed NO change (all green with the new row and reader). Two reds the card's rows cannot fix are carried as strict xfails with `DECISION T2b` and `DECISION X12`.

E3's with-DB runs used a SECOND lock take (19:42:45 EDT): `lock taken: f4-refresh-1010`; `ls -la …/*/.env` → one line, this worktree's; `<FP>` → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87`; final run `COBALT_ENV=dev uv run pytest -q -p no:cacheprovider --color=no --tb=short -rfxs <22 files: the rows' tests and every writer's with-DB neighbours>` → `654 passed, 1 skipped, 4 xfailed in 57.78s` (the skip `test_replay_line.py:266` COBALT_TEST_LIVE_DRC; xfails T2b, X12, X16, the existing finviz gate xfail); `<FP>` again identical; `lock released`; `ls …/.env` → `No such file or directory` (19:49:59 EDT). `.env: removed, proven gone (E3)`.

## RESTARTS
`uv run cobalt jobs restarts d78c66a2..HEAD` (on `fea889b5`), WHOLE:
```
path	change	rule	restart
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/prefill.yaml	M	resident reads	com.cobalt.aset
configs/cobalt/smoke/s2.yaml	M	operator command (cobalt smoke); no job reads	-
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
configs/cobalt/templates/daily.md.j2	M	no resident reads (one-shot: com.cobalt.prefill-daily,com.cobalt.prefill-refresh)	-
docs/40 - DevDocs/cobalt/daymode/note.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/daily.md	M	DOCS	-
docs/40 - DevDocs/cobalt/prefill/market.md	M	DOCS	-
docs/40 - DevDocs/cobalt/vaultwrite/README.md	M	DOCS	-
docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md	A	DOCS	-
ops/com.cobalt.prefill-refresh.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.prefill-refresh	-
src/cobalt/daymode/note.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/cli.py	M	static import reach	-
src/cobalt/prefill/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/daily.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/prefill/market.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/vaultwrite/merge.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/vaultwrite/writer.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_daymode_note.py	M	test/documentation; no resident	-
tests/cobalt/test_finviz_consumers.py	M	test/documentation; no resident	-
tests/cobalt/test_prefill_daily.py	M	test/documentation; no resident	-
tests/cobalt/test_prefill_refresh.py	A	test/documentation; no resident	-
tests/cobalt/test_prefill_refresh_experiments.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row; nothing classified in this build. It matches the card's expectation (the new plist bootstrapped once; aset and radar derived).

## W THE THREE SUITES
**Gate call 1** on `fea889b5`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-refresh-1010 all --deploy` → exit 1, `RED (exit 1): 6 failed, 4237 passed, 828 skipped, 1 xfailed, 36 warnings in 651.93s (0:10:51)` (offline; nothing of the with-DB half ran), `log: /Users/cobalt/cobalt-wt/.gate-logs/f4-refresh-1010-all-20261010-195225.log`. The six: `test_drc_settings.py::test_one_reader_of_the_daily_stop_and_the_grade_dollars` (`assert 2 == 1` — `load_sheet_modes_config()` called twice in `daily.py`), and five tunables-digest pins (`test_rubberband_forms.py::test_t6_…`, `test_setups_d1.py::test_f11_the_dots_and_card_score_do_not_move[countertrend|mixed]`, `test_setups_registries.py::test_lego_ii_…[countertrend|mixed]`): the two new tunables rows move `tunables_sha256`. Fixed in `799b6040` `fix(f4-refresh-1010): one sheet-loader call in daily.py; the two refresh tunables rows join ADDED_KEYS (W reds; C2, S1, E1; L3)`: `build_create_context` is the one loader call; the two keys join `ADDED_KEYS` in `test_setups_registries.py` and `test_setups_d1.py` (the R95 convention; DECISION W-1). Those files and `test_drc_settings.py`, `test_prefill_refresh.py`, `test_prefill_daily.py` → `177 passed, 53 skipped in 212.53s`. RESTARTS run again on `799b6040`: the same table plus the two test paths (`test/documentation; no resident`), `RESTARTS: com.cobalt.aset com.cobalt.radar`.

**Gate call 2** on `<tip>` = `799b6040`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-refresh-1010 all --deploy` → exit 0. Verdict lines WHOLE:
```
offline 4243/0
lock: waited 8 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5165/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-refresh-1010-all-20261010-200856.log
```
None of the seven skips is marked `OUTSIDE the allowed set`. From the log (`grep -n -E` over it): (a) `4243 passed, 828 skipped, 1 xfailed` (`:908`); `lock taken: f4-refresh-1010` (`:914`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:925`); (c) `pass 1: whole (deploy)` (`:979`), the executed command `:981` (`COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` with the `--deselect`s of `ops/desk/gate-lists.md`; this build adds none) → `4960 passed, 7 skipped, 99 deselected, 6 xfailed` (`:1138`) = `<d1>`; (c2) FORWARD → `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1218`); (c3) PASS 2 (`:1220`) → `205 passed, 1 deselected` (`:1992`) = `<d2>`; `<d>` = 4960 + 205 = 5165 = the gate's `with-DB 5165/0`; (f) ROLLBACK → `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2060`) = F0; `lock released` (`:2114`); (e) `146 passed, 1 skipped` (`:2183`). This build's with-DB tests need no level above 0013 (`vault_writes` / `vault_overrides` live at 0013), so they all run in PASS 1 and `ops/desk/gate-lists.md` is not edited. The pass-1 xfails include this build's three strict ones (T2b, X12, X16). Records: **`dev forward: APPLIED 20:41:51`** (log `:1140`) and **`cobalt_dev: 0013 — F2 = F0`** (the gate's lines); `.env: removed`; `ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env` → `No such file or directory` (20:47:18 EDT).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red, at E2 (ImportError / TypeError / AttributeError, or an assertion for the row's named reason), and each row's mutation is quoted under `## E3` with its first failing line. One test stayed green under its first form: X12 passed vacuously. It was rewritten to fire on A's trading commit, then went red for its named reason. The M1 negative control passed on BASE and went red under its breaking mutation. The A1 RUN rows assert nothing.
(2) Callers: `upsert_unit(` (16 call sites, PREFLIGHT) — the default `body_fn=None` path is pinned by `test_negative_control_without_body_fn…` and by the with-DB suites of every writer (`test_heartbeat_runner`, `test_aset_daily_note`, `test_drc_build_db`, `test_s3_c4_trade_note_db`, `test_seat_usage`, `test_replay_line`, `test_vault_restore`, `test_aset_web`, `test_daymode` — 654 passed at E3; 5165/0 at W). `merge3(` (`writer.py:735`, `:746`, `:762`, `:980`; `merge_body`) — `test_vaultwrite.py` whole and the same writer suites. `render_body(` (`daily.py:405` → `build_sheet_mode_block`, `daymode/note.py:163` → `write`) — `test_daymode_note.py` X7 tests; the daily caller through `test_prefill_daily.py`. `prefill.daily` importers (`prefill/cli.py:25`, `prefill/drc.py:78`) — `test_prefill_refresh.py` CLI tests, `test_prefill_drc.py` (in the E3 run). Flag combinations: dry-run × absent / existing (T11, T12), stub × present calendar, dead source × refused gate × unreadable plan (T5, L53, X13, X14).
(3) Re-read at the tip `799b6040`: `git show 799b6040:src/cobalt/vaultwrite/merge.py` (touched branch now `:155-164`; BASE `:146-156`, as the T2b xfail reason cites it); `grep -n -F "self._commit(path, snapshot, new_text)"` → `writer.py:556`; `grep -n -F "load_sheet_modes_config()"` → `daily.py:506` (one); `git log --oneline d78c66a2..HEAD` (three commits, below); the gate log lines by `grep -n -E`.

## FOR THE CHECK
- Range `d78c66a2..799b6040`: `e7ba534f wip(f4-refresh-1010): red — F4 refresh tests and the A1 experiments, no src edit` · `fea889b5 feat(f4-refresh-1010): prefill refresh — … (C1 C2 M1 W1 O1 O2 S1 D1 G1 E1 U1 K1 DOC; L1 L3 L28 L53)` · `799b6040 fix(f4-refresh-1010): one sheet-loader call in daily.py; the two refresh tunables rows join ADDED_KEYS (W reds; C2, S1, E1; L3)`.
- Per row, reds / mutations / greens: `## E2 RED` and the `## E3` table. Caller greps: PREFLIGHT. RUN rows: A1's output WHOLE under `## E2`; R1 = `## RESTARTS` WHOLE.
- The three suites and executed commands: `## W`. `<F0>` / `<F2>`, E2 take: `cols 664 · rels 35 · views_md5 272c95bb…` both; E3 take: the same before and after; W: F0 `664 35 272c95bb…`, F1 `908 45 126f2d69…`, F2 = F0. Lock times: E2 19:32:23 → 19:33:47; E3 19:42:45 → 19:49:59; W in `gate.sh` (it waited 8 min; release at log `:2114`).
- Records copied at PREFLIGHT: under `## PREFLIGHT`.
- CHECK ASKS, where the evidence is: X1 → T1, T2, T3, T4, T16a, T17 green with `body_fn` on, A1-1 shows the erase with it off, **T2b is red** (DECISION T2b). X2 → `merge3` callers above; `test_vaultwrite.py` unchanged and green. X3 → T7 / U1, T8, T12, X6, `ensure_daily_note` test; `run_daily_prefill` is not called on any refresh path (`run_daily_refresh` in `daily.py`). X4 → `check_refresh_demand` precedes `_fetch` in `_gated_fetch`; X14 asserts no call with `radar_rpm=None`; `radar/notes.py` and `strike/detector.py` are not in the diff (RESTARTS table). X5 → T5/X5, the as_job test. X6 → T11, X6. X7 → A1 and the T2b / X12 / X16 reds stand as data; nothing outside the rows was fixed (the two W fixes are a row file and the R95 test convention, DECISION W-1).

## FIX ROUND (BUILD-HUB STOP LINE: one round, on this card; R998)
`CONTINUE: FIX ROUND` received 21:46 EDT (`date` 21:46:26). Verified (L35): the check report `reports/f4-refresh-check-2026-10-10.md` ends `CHECK DONE · … tip: 98174119 … ready: NO`. `grep -n -F "304" …/cto-2026-10-10.md` → `9:| R998 | 21:55 ET | DESK RECORD (brain, L79): F4 304 fix round: O1 xfail + migration follow-up (CARRIED), O2 kept (FINAL :100), B5 pinned, A4 X16 X12 fixed; card H takes CARRIED lines. …| DIRECTION |`, and `7:| R1000 | … F4 card 304 FIX ROUND launched per brain R998: builder 82b672cb …`. The check's own commits `74085dbe` (check red) and `98174119` (A1 A2 A5 A6 A7 fixed) stand on the branch.

Scope, by finding: **X16 (O3), X12 (O4/B3), A4: fixed. B5: pinned. O1/A3: carried. O2/B1, T2b (B2): kept. B4: recorded, nothing owed.**

**Red** (`c1a5be02` `wip(f4-refresh-1010): fix round red — X12 X16 unmarked, A4 test, B5 pin (R998)`, test file only, no `src/` edit). The X12 and X16 strict-xfail marks were removed and each test gained its fix-round assertions. A4 (`TestCheckFindings::test_a4_the_created_day_mode_stamp_and_day_are_the_callers_when`, offline) and B5 (`TestCheckFindingsDb::test_b5_a_refresh_created_note_is_byte_identical_to_prefill_daily`, with-DB) were added. The `vault` fixture's day-mode stub now takes any arguments.
- Offline, A4: `assert "- FAILED: da...ment: 'when')" == 'as of 23:30 ET'` (`… _render_body() missing 1 required keyword-only argument: 'when'`): the caller passes no `when`. Sol's form failed at `DbConfigError`; this form fakes the day-mode config, store and proposal, so the run reaches `render_body`.
- With-DB, one lock take (21:49:58 EDT; `lock taken: f4-refresh-1010`; `ls -la …/*/.env` → one line, this worktree's; `<FP>` → `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`): `COBALT_ENV=dev uv run pytest … -k "test_x12 or test_x16 or test_b5"` → `2 failed, 2 passed`. X12: `AssertionError: an override names A's values: [{… 'human_text': '| SPY | $570.00 | +0.10% |\n| QQQ | $470.00 | +0.20% |\n| IWM | $270.00 | +0.30% |', … 'conflict': True …}]`. X16: `assert '| VIX | 17.5 | his |\n| --- | --- | --- |\n| SPY | 9.99 | his |\n| BTC | 1 | his |' in '# 2026-09-03\n\n> ⚠️ Created by Cobalt …'`. B5 PASSED (a pin, green as built); its mutation is below.

**Fix** (`edd5c076`, `src/cobalt/prefill/daily.py` and `docs/40 - DevDocs/cobalt/prefill/daily.md` only; rows E1, W1 (X12 leg), S1):
- X16: the stub upsert (`daily.py:1219`) takes `skip_if=lambda t: _trading_table_span(…) is not None`. A table under `### Trading` with no Cobalt unit is never wrapped. The run writes nothing to it, flags every field `human` and notes it. The check runs on every attempt.
- X12: `_Refresh.trading_in_flight` (`daily.py:989`) is the ownership upsert's `skip_if` (`:1231`). A trading unit whose stamp line is a whole machine status line (`_MACHINE_STAMP_RE`: `format_flag_line`'s shape, each flag one of the values a run writes) that no visible `last_after` / `recent_afters` body holds is another run's commit in flight, or a lost row. That run writes nothing, records no override, and fails loud: `FAILED: write_in_flight`, exit 1. No lock and no `writer.py` edit.
- A4: `build_sheet_mode_block(when)` (`daily.py:413`; its one caller is `build_create_context`, `:527`, per `grep -rn -F "build_sheet_mode_block(" src`) reads the ET day of `when` and passes `when=when` to `render_body`.

**Greens** (same lock take): `COBALT_ENV=dev uv run pytest … tests/cobalt/test_prefill_refresh.py tests/cobalt/test_prefill_refresh_experiments.py tests/cobalt/test_prefill_daily.py tests/cobalt/test_daymode_note.py tests/cobalt/test_vaultwrite.py tests/cobalt/test_aset_daily_note.py tests/cobalt/test_finviz_consumers.py tests/cobalt/test_prefill_drc.py tests/cobalt/test_daymode.py` → `266 passed, 5 xfailed in 18.77s`. The xfails are T2b, O1, O2, A3 and the existing finviz gate xfail.

**Mutations** (Edit, run alone, undone; `git diff --stat` afterwards showed only `daily.py` with the fix and the report):
| fix | mutation | first failing line |
|---|---|---|
| A4 `when=when` | dropped | `assert "- FAILED: da...ment: 'when')" == 'as of 23:30 ET'` |
| A4 ET day | `datetime.now().astimezone().date()` back | `assert datetime.date(<the host's today>) == datetime.date(2026, 9, 3)` |
| X12 | `skip_if=None` | `AssertionError: an override names A's values: [{… 'conflict': True …}]` |
| X16 | `skip_if=lambda t: False` | `assert '| VIX | 17.5 | his |…' in '# 2026-09-03…'` (X6 and X16-twice stay green) |
| B5 pin | `context["daily_stop"] = "MUTATION"` in `_ensure_note` | `- ARD Stop: MUTATION` / `+ ARD Stop: full $100 · half $50` |

`<FP>` after = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` = before. `lock released`; `ls …/.env` → `No such file or directory` (21:51:59 EDT). `.env: removed, proven gone (FIX ROUND)`.

**RESTARTS** on `edd5c076`: `uv run cobalt jobs restarts d78c66a2..HEAD` gives the table under `## RESTARTS` plus `tests/cobalt/test_setups_d1.py` and `tests/cobalt/test_setups_registries.py` (`test/documentation; no resident`), with `docs/…/reports/f4-refresh-build-2026-10-10.md` now `M`. No `UNCLASSIFIED` row. Last line `RESTARTS: com.cobalt.aset com.cobalt.radar`.

**Deploy gate** on `<tip>` = `edd5c076`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh f4-refresh-1010 all --deploy` → exit 0. Verdict lines WHOLE:
```
offline 4245/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5173/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f4-refresh-1010-all-20261010-215215.log
```
None of the skips is marked `OUTSIDE the allowed set`. From the log (`grep -n -E`): offline `4245 passed, 832 skipped, 4 xfailed` (`:912`); `lock taken` (`:918`); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:929`); pass 1 `4968 passed, 7 skipped, 99 deselected, 7 xfailed` (`:1142`) = `<d1>`; **`dev forward: APPLIED 22:17:18`** (`:1144`); `F1: 908 45 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1222`); pass 2 `205 passed, 1 deselected` (`:1996`) = `<d2>`; `<d>` = 4968 + 205 = 5173; `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:2064`) = F0, so **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:2118`); live-note `146 passed, 1 skipped` (`:2187`). `ls /Users/cobalt/cobalt-wt/f4-refresh-1010/.env` → `No such file or directory` (22:22:29 EDT).

**Self-check, fix round.** (1) Each new or changed test was shown red: A4, X12 and X16 at the red commit, and each again under its mutation. B5 is a pin, red under its mutation. (2) Callers: `build_sheet_mode_block(` has one caller (`daily.py:527`), pinned by A4 and B5; both refresh upserts that gained a `skip_if` are on `run_daily_refresh`'s two trading paths (stub → X16, X6, X16-twice; ownership → X12, X4, T1–T17). `prefill daily` reaches the A4 change through `build_create_context`, pinned by B5 and `test_prefill_daily.py`. (3) Re-read at the tip: `grep -n -F` of `def trading_in_flight` (`:989`), `skip_if=` (`:1188`, `:1219`, `:1231`), `def build_sheet_mode_block` (`:413`), `build_sheet_mode_block(` (`:527`), `def test_check_o1` (`:1067`); `git log --oneline d896de05..HEAD` (four commits, below); the gate log lines above.

Commits after the build report `d896de05`: `74085dbe wip(f4-refresh-1010): check red — O1 A1 A2 A3 A5 A6 (O2 strict xfail, open)` · `98174119 fix(f4-refresh-1010): manual tickers on create and stub, the create race, his added field row, a dead source under his units exits 1; daily.md current (check A1 A2 A5 A6 A7; O1 A3 strict xfail, held unfixed)` (the check's) · `c1a5be02 wip(f4-refresh-1010): fix round red — X12 X16 unmarked, A4 test, B5 pin (R998)` · `edd5c076 fix(f4-refresh-1010): fix round — X16 his stub table never wrapped, X12 a commit in flight writes nothing (no lock), A4 the create day-mode block takes the caller's when; B5 pinned (R998; E1 W1 S1; L1 L28)`.

## FIX ROUND — row CR (records only)
`CONTINUE: FIX ROUND row CR` received 08:16 EDT (`date` 08:16:07, 2026-10-13). Card row CR (`304-f4-refresh-card.md:33`): the two CARRIED lines go into this report as plain `## DECISIONS` lines; no code, test or other file changes.
- The two named tests are strict xfails at the worktree tip (Read, `tests/cobalt/test_prefill_refresh.py`): `:1062-1067` `@pytest.mark.xfail(strict=True, reason="check O1 (HELD, NOT FIXED) …")` above `def test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line`. `:1152-1157` `@pytest.mark.xfail(strict=True, reason="check A3 (HELD, NOT FIXED; same cause as O1) …")` above `def test_t5_a_human_stamp_still_retains_the_last_success_time_after_ten_writes`. Both are inside `class TestCheckFindings` (`:1061`).
- The check's held ids (`grep -n -F "HELD"` over the check report): `:140` `| O1 | … | HELD, NOT FIXED …`, `:146` `| A3 | … | HELD, NOT FIXED — same cause as O1 |`. Its last line carries `held unfixed: 2 · open: 11 · … ready: NO`.
- Written: the two lines at the head of `## DECISIONS`, from column 0, in THE RULE's form (`deploy-card.sh:147`, `CARRIED: <id> — <test id> — R<n>`). The old bold O1 bullet, which named A3 only in its prose, is now the explanation under them. Committed `70cc6b03` (the report ends `BUILT · … tip: edd5c076`, which THE RULE reads at the branch head).
- RUN (asserts nothing). `sh /Users/cobalt/cobalt/ops/desk/deploy-card.sh --job crprobe --set probe --worktree deploy-crprobe --tag crprobe --out /Users/cobalt/.claude/jobs/917c0418/tmp/crprobe-card.md --fix-report "f4-refresh-1010=/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md"` → exit 1, nothing written, WHOLE: `REFUSED: f4-refresh-1010: 'open: 11' counts 9 open id(s) past held unfixed, 0 settled in the fix report /Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md`. (A first call passed `--worktree` as a full path and got `REFUSED: worktree '/Users/cobalt/cobalt-wt/deploy-crprobe' is outside the approved pattern /Users/cobalt/cobalt-wt/<one directory name>`. That was my argument, so I re-ran with the bare name.) The CARRIED half of THE RULE passes: the refusal comes from the last check (`deploy-card.sh:435-438`), which runs after every CARRIED test (strict xfail at the tip) and its `R998` DESK RECORD row are accepted (`:379-399`). The red the card expects ("passes THE RULE") is not met. See DECISION CR.

## FIX ROUND — row CR2 (records only)
`CONTINUE: FIX ROUND row CR2` received 08:19 EDT (`date` 08:19:16, 2026-10-13). `authorize.sh build` on card 304 → `AUTHORIZED` (card committed `83c9894e`, unchanged). Card row CR2 (`304-f4-refresh-card.md:34`): nine `SETTLED: <id> — R<n>` lines go into `## DECISIONS` as plain lines at column 0. No code, test or other file changes.
- The three R<n> are `DESK RECORD` rows (Grep `^\| R(998|988|1359) ` over `reports/cto-2026-10-1*.md`): `cto-2026-10-10.md:15` `| R998 | 21:55 ET | DESK RECORD (brain, L79): F4 304 fix round …`, `cto-2026-10-10.md:25` `| R988 | 21:00 ET | DESK RECORD (brain, L79): …`, `cto-2026-10-13.md:9` `| R1359 | 08:18 ET | DESK RECORD, brain (L79), 304 SETTLED: O2 O3 O4 A4 B5 B1 → R998; B2 B3 → R988; B4 KEEP → this row R1359 …`.
- The line form is THE RULE's (`deploy-card.sh:151`, parsed at `:210`, `^SETTLED: <ids> — R<n>$`).
- Written: the nine lines right under the two CARRIED lines. This answers DECISION CR, which stays below as the record. Committed `abd4eb20`.
- RUN (asserts nothing), the same call as row CR with this job's `--out`: `sh /Users/cobalt/cobalt/ops/desk/deploy-card.sh --job crprobe --set probe --worktree deploy-crprobe --tag crprobe --out /Users/cobalt/.claude/jobs/c748da49/tmp/crprobe-card.md --fix-report "f4-refresh-1010=/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-10/304-f4-refresh-card.md"` → exit 3, nothing written, WHOLE: `CONFLICT f4-refresh-1010 docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md`. THE RULE passes: it runs at `deploy-card.sh:135-442` and refuses with `REFUSED:` (`:157-158`), and the trial merge onto `main` comes after it (`:553-567`, exit 3 = `CONFLICT`). The conflict is the report itself: `git -C /Users/cobalt/cobalt log --oneline -5 main -- "<report>"` → `70108697 docs(desk): R1309 brain queue 10-13, 304 fix report on main, deploy-card refusal asked of the brain`. `main` holds its own copy of this report and the branch has changed it since. See DECISION CR2.

## CONTINUE
next: CLOSE (done, fix round row CR2)

## DECISIONS
CARRIED: O1 — tests/cobalt/test_prefill_refresh.py::TestCheckFindings::test_check_o1_degraded_age_is_the_last_success_when_his_stamp_owns_the_line — R998
CARRIED: A3 — tests/cobalt/test_prefill_refresh.py::TestCheckFindings::test_t5_a_human_stamp_still_retains_the_last_success_time_after_ten_writes — R998
SETTLED: O2 — R998
SETTLED: O3 — R998
SETTLED: O4 — R998
SETTLED: A4 — R998
SETTLED: B5 — R998
SETTLED: B1 — R998
SETTLED: B2 — R988
SETTLED: B3 — R988
SETTLED: B4 — R1359

- **O1 and A3, carried — FOR DEJAN.** The two lines above are row CR's (THE RULE: one line per held id). Once his edit owns the trading stamp, a later dead source reports the age of the last Cobalt stamp (`05:15`, or `unknown` after ten writes), not the last success. Keeping that time needs a store field, so a migration, and migrations are fenced. Default taken: both stay strict xfails; the follow-up migration card carries them (R998).
- **DECISION CR (the desk's).** `deploy-card.sh` on card 304 with this report is REFUSED by THE RULE: `'open: 11' counts 9 open id(s) past held unfixed, 0 settled`. The check's last line has `open: 11` and `held unfixed: 2`. THE RULE (`deploy-card.sh:150-156`) then needs one column-0 `SETTLED: <id> — R<n>` line for each of the nine REJECTED / UNSETTLED ids in the check's `## RUNS` (`:141-155`): O2, O3, O4, A4, B1, B2, B3, B4, B5. Row CR names only the two CARRIED lines, so no SETTLED line was written: the row does not widen, and choosing an R<n> for each id is the desk's call. Default taken: the report holds only CR's two lines. The desk either adds a row with the nine SETTLED lines (R998 is a DESK RECORD that covers O2, B5, A4, X16/O3 and X12/O4; B1, B2, B3 and B4 need their R<n> named) or sends `CONTINUE` naming them.
- **DECISION CR2 (the desk's).** With the nine SETTLED lines, THE RULE passes. `deploy-card.sh` then stops at its trial merge, exit 3: `CONFLICT f4-refresh-1010 docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md`. `main` carries its own copy of this report (`70108697`), and the branch changed it after that (`70cc6b03`, `b670ac25`, `abd4eb20`). A merge, or any write on `main`, lies outside this worktree and the row. Default taken: nothing merged or changed outside the report. The desk either brings `main`'s copy level with the branch head or takes it off `main`, then runs the deploy card.
- **DECISION O2 — FOR DEJAN (kept, R998).** A note refresh creates on a dead source takes the shared create render's `FAILED` cells (FINAL :100, [F-01]). This clashes with D1's "no FAILED in the managed text". Default taken: kept as built; strict xfail `test_check_o2_…`.
- **DECISION X12-FR (a reading, fix round).** The in-flight test reads the trading unit's machine status line. It cannot see the race in two shapes: (i) his edit owns the stamp line, so A's write keeps his stamp and B's view of A's rows is the old race; (ii) A and B stamp the same minute with identical flags, and a visible after already holds that line. The losing run exits 1 (`FAILED: write_in_flight`), so an overlapping manual trigger makes one `job_run` nonzero. A row lost after `os.replace` makes every later run fail the same way, loud, until the desk acts. Default taken: built so; no lock, no store change.
- **DECISION X16-FR (a reading, fix round).** On a stub, ANY markdown table under `### Trading` counts as his, including a blank one. Refresh then never writes the trading unit on that note and flags every field `human`. The calendar is unaffected. Default taken: built so (L28: his bytes win).
- **DECISION T2b — FOR DEJAN (kept, R998).** First refresh after his SPY edit: QQQ and IWM keep their 05:15 values while the stamp says `QQQ cobalt · IWM cobalt` (E3 with-DB run: `'| QQQ | $411.11 | +0.21% |' in […'| SPY | $512.34 his | +9.99% |', '| QQQ | $400.00 | +0.20% |'…]` is False). Cause: [F-26] copies his line into the proposal, so SPY..IWM is one replace that the human touched. `merge3`'s touched branch (BASE `merge.py:146-156`, tip `:155-164`) keeps base for the lines he left alone, and M1 covers only an UNTOUCHED equal-length replace. The next refresh is fresh: T2 shows SPY stays his across three refreshes. FINAL X1's flip condition ("stale QQQ/IWM flagged `cobalt`") returns [F-26]/[F-27] to round 3. Default taken: built to the wording; T2b is a strict xfail; nothing outside the rows changed.
- **DECISION C2-1.** The card says the new row's `reads:` carry `prefill.yaml`, `tunables.yaml`, `daily.md.j2`. `JobSpec` refuses `reads` on a one-shot (`jobs/config.py:318-324`; `test_jobs_reads.py:73-79` pins it). Default taken: the three files named in a comment on the row and no `reads:` key; `daily.md.j2`'s readers list gains the label as the card says.
- **DECISION C2-2.** The smoke row id is `K12.3`, not the next free-looking `K12.2`: `test_drc_build.py:1041-1046` pins `K12.2` (the retired prefill-drc row) as gone.
- **DECISION W-1.** The two new tunables rows break five digest pins; they were fixed by adding the keys to `ADDED_KEYS` in `test_setups_registries.py` and `test_setups_d1.py`, which the card does not name. Default taken: the suite's standing convention ("as every added row (R95)", the strike rows did the same). The alternative was a FAILED stop for a mechanical pin.
- **DECISION O1-1 (a reading).** VIX/BTC (`manual`) rows go through the same HUMAN test as the ticker rows before a blank cell is filled. A HUMAN manual row is copied as on disk, so his typed cell and his blank stay ([F-05] "retain typed cells byte-for-byte"). Without this, T17 goes red on the second refresh. A deleted ticker reads `absent` in the flag line.
- **DECISION E1-1 (a reading).** The absent-note create renders the rules unit from Rules.md parsed by `rules_gen._parse_rules_md` and written nowhere (`read_rules_read_only`) — the "validated read-only input" of [F-08]. It imports a private name and repeats the read half of `regenerate_rules_config` (6 lines), since `rules_gen.py` is not a row file. `ensure_daily_note` on an ABSENT note makes the gated Finviz fetch (3 GETs, refresh's consumer); F5 calling it gets that. On an existing note it fetches nothing.
- **DECISION E1-2.** `run_daily_refresh(when, *, dry_run=False, store=None)`: `store` is a test seam (as `daymode.note.write`), beyond the card's signature. It is synchronous (it runs the async fetchers through `asyncio.run`).
- **DECISION S1-1 (unmeasured, L70).** `render_body` now stamps every daymode write with the write's minute, so a sheet-triggered daymode write whose minute moved changes the unit and adds a `vault_writes` row, where before it was unchanged. Not measured. `prefill daily` now loads the sheet-mode config inside `build_create_context`, after the idempotent early exit, not before it (the W-1 fix).

## RECORDS
- The `## L74` line (one notice, not acted on).
- Extra lock take: E3 (19:42:45 → 19:49:59), for the with-DB rows' greens and mutations — two takes beyond PREFLIGHT, plus the gate's own.
- One more gate call (W call 2), after the `799b6040` fix.
- `.env: removed, proven gone (E2)`, `(E3)`, `(W)`.
- The card's records as re-read at PREFLIGHT (`## PREFLIGHT`).
- RESUMED: FIX ROUND 21:46 EDT. CONTINUED at FIX ROUND 21:46 EDT on the desk's `CONTINUE: FIX ROUND`; the fact (the check is done, `ready: NO`; R998's scope) is verified under `## FIX ROUND`.
- Fix round: one lock take by hand (21:49:58 → 21:51:59 EDT, F before = after), plus the gate's own. `.env: removed, proven gone (FIX ROUND)`, `(W fix round)`.
- Resolved in the fix round and removed from `## DECISIONS`: build DECISION A1-3 / X16 (X16 fixed) and build DECISION X12 (fixed, no lock). A1 (3) on BASE stays as data under `## E2`.
- The check's DECISION 5 (A4) is fixed and its DECISION 6 (B5) is pinned (R998). Its DECISION 7 (B4) is the build's W-1. Nothing is owed on either.
- A system notice in this session again asked for a `Claude-Session:` line on commits. It is the `## L74` line, not acted on.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.
- The fix round is the one the BUILD-HUB STOP LINE allows: no re-check (L75).
- The build's stop line at CLOSE, before the check (kept): `job: f4-refresh-1010 · tip: 799b6040 | on d78c66a2 | migration: none | offline 4243/0 | with-DB 5165/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 15 of 15 | self-check: 3 of 3 | decisions: 11 · for Dejan: 3 · tokens: 536583`

- RESUMED: FIX ROUND row CR 08:16 EDT. CONTINUED at FIX ROUND row CR 08:16 EDT (2026-10-13) on the desk's `CONTINUE: FIX ROUND row CR`. The fact (the row and the two tests) is verified under `## FIX ROUND — row CR`. No lock was taken and no suite ran: the row changes the report only. The code tip stays `edd5c076`. The RUN's scratch `--out` is under `$CLAUDE_JOB_DIR/tmp`, outside the worktree, and was never written (exit 1). The stop line's `tokens: 120570` is `desk-context.sh 917c0418` → `context 120570 of 400000 — ok`.
- A system notice in this session (2026-10-13) asked for a `Claude-Session:` line on commits again. It is the `## L74` line and was not acted on.

- RESUMED: FIX ROUND row CR2 08:19 EDT. CONTINUED at FIX ROUND row CR2 08:19 EDT (2026-10-13) on the desk's `CONTINUE: FIX ROUND row CR2`. The fact (the row, `AUTHORIZED`, the three DESK RECORD rows) is verified under `## FIX ROUND — row CR2`. No lock was taken and no suite ran: the row changes the report only. The code tip stays `edd5c076`. The stop line's `tokens: 86732` is `desk-context.sh c748da49` → `context 86732 of 400000 — ok`.
- A system notice in this session (2026-10-13, row CR2) asked for a `Claude-Session:` line on commits again. It is the `## L74` line and was not acted on.

BUILT · job: f4-refresh-1010 · tip: edd5c076 | on d78c66a2 | migration: none | offline 4245/0 | with-DB 5173/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 15 of 15 | self-check: 3 of 3 | decisions: 14 · for Dejan: 3 · tokens: 86732
