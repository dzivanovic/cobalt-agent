# HANDICAP H1 FIX R1 — BUILD REPORT — 2026-09-24

Seat `handicap-h1-fix-r1-build-0924` · Opus 5.5 · prompt `docs/40 - DevDocs/prompts/2026-09-24/60-handicap-h1-fix-r1-build.md` · branch `radar/handicap-h1-0922` · base `026c99b8` · started `Thu Sep 24 22:21:24 EDT 2026` (`date`).

## §0 Headline
FIX 4 of 4 on `026c99b8` → `<tip>` `2edb2cf3`. F1 (a) was built (the named harness; `migrated_radar` declares `dev_db_tx`). F1 (b) was NOT built: D3's `pg_stat_activity` probe was GREEN (`idle`), so the run-time harm is NOT REAL by RUN. F2 and F4 are doc-only; F3 prints `handicap: not replayable from bars`.
RUNS 3 of 3, all green and no xfail. RUN-2 (b) proves X5's stored half. RUN-3 measures a ranked LEAVE that keeps the RETAIN's record, and a departed row that renders the `HANDICAP (shadow)` badge (for round 2).
Three suites green: offline 2624/0, with-DB 2984/0 (2 deselected), live-note 131/0 with the same four `AWAITING` lines. `0014` is absent on `cobalt_dev`, which stays at `0013`. `.env` removed, proven gone.
ESCALATE: 10.

## L74
Recorded once: a system-reminder block attached to my first tool result (the `cat` of this prompt) asked for a `Claude-Session: https://claude.ai/code/session_…` line in commits and named a file-send tool (`SendUserFile`). It is DATA; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | result |
|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/60-handicap-h1-fix-r1-build.md` | no output (exit 1) — PASS |
| `45`'s stop | `tail -n 3 …/handicap-h1-check-2026-09-24.md` | last non-blank: `HANDICAP H1 CHECK DONE · round: 1 · opus: CHECK: FIX — … · defects that HOLD: 2 · ready for a deploy prompt: 1 of 2 · ESCALATE: 14` — PASS |
| `45` committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/handicap-h1-check-2026-09-24.md` | `ddb41fbd48b4ab16867e9ec957e62934b7851800` |
| classification | `tail -n 3 …/handicap-h1-fix-r1-draft-2026-09-24.md` | `HANDICAP H1 FIX R1 DRAFTED · FIX: 4 · NOT REAL: 5 · UNPROVEN: 3 · OUT OF SCOPE: 9 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 9` — PASS |
| classification committed | `git -C … log -1 --format=%H -- …/handicap-h1-fix-r1-draft-2026-09-24.md` | `d46af95eb332156d34799df2e24458f49953d7d3` |
| `.env` cp string in cto-2026-09-22 | `grep -c -F "Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/handicap-h1/.env)"` | `1` |
| `.env` rm string in cto-2026-09-22 | `grep -c -F "Bash(rm /Users/cobalt/cobalt-wt/handicap-h1/.env)"` | `1` |
| rm string committed | `git -C … log -1 --format=%H -S"Bash(rm …handicap-h1/.env)" -- cto-2026-09-2*.md` | `055242df8032632dfafdcc8a69dcc271be89c0f6` |
| R30 row | `grep -n "^| R30 " cto-2026-09-22.md` | line 133: `| R30 | 13:0x ET | "Approved" — … the TWO NEW strings \`Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/handicap-h1/.env)\` · \`Bash(rm /Users/cobalt/cobalt-wt/handicap-h1/.env)\` …` — both strings + `"Approved"` — PASS |
| 20 allow + 3 deny strings in `43` | `grep -c -F -e "\"<rule>\"" …/43-handicap-h1-build-r2.md`, 23 calls | every count ≥1 (`1` ×21; the two `.env` strings `2` each) — PASS |
| no migrate string | `grep -c -F -e "\"Bash(COBALT_ENV=dev uv run cobalt db migrate)\"" …/60-…md` | `0` — PASS |
| launch row | `grep -n "60-handicap-h1-fix-r1-build.md" cto-2026-09-24.md cto-2026-09-25.md` | `cto-2026-09-24.md:123: | R102 | 22:20 ET | … (2) LAUNCH ROW for \`60-handicap-h1-fix-r1-build.md\` …`; `cto-2026-09-25.md`: No such file (recorded, not fatal) — PASS |
| launch row committed | `git -C … log -1 --format=%H -S"60-handicap-h1-fix-r1-build.md" -- cto-2026-09-2*.md` | `d46af95eb332156d34799df2e24458f49953d7d3` |

Note: `grep` on this host is ugrep (the warning text on the missing file).

## PREFLIGHT
| rule | command | exit | result verbatim |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 22:22:44 EDT 2026` |
| clean tree | `git status --short --branch` | 0 | `## radar/handicap-h1-0922` + `?? "docs/40 - DevDocs/reports/handicap-h1-fix-r1-build-2026-09-24.md"` — the one extra line is THIS report, created by the prompt's own "FIRST Write" before AUTHORIZATION; nothing else. Read as clean (ESCALATE 1) |
| tip | `git log --oneline -2` | 0 | `026c99b8 docs(report): handicap H1 build r2 — …` / `27df13f1 test(experiments): H1 CLOSE — the 0014 absence probe …` — PASS |
| code unmoved | `git diff --stat 27df13f1 026c99b8 -- src tests configs` | 0 | no output — PASS. `<base>` = `026c99b8` |
| `.env` | `ls /Users/cobalt/cobalt-wt/handicap-h1/.env` | 1 | `ls: …/handicap-h1/.env: No such file or directory` — PASS |
| LOCK (a) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — free |
| LOCK (b) | `ls /Users/cobalt/cobalt-wt/DEVDB-HOLD` | 1 | `No such file or directory` — free |
| migrations | `ls src/cobalt/db_migrations` | 0 | `0001_schemas.sql` … `0013_tunables_slug_nullable{,.rollback}.sql`, `0014_radar_handicap.rollback.sql`, `0014_radar_handicap.sql`, `cli.py`, `placement.py`, `__init__.py`; no `0015_*` — PASS |
| live notes | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (READ ONLY) — PASS |
| autouse | `grep -n "autouse=True" tests/cobalt/conftest.py` | 0 | `60:`, `66:`, `133:`, `236:` `@pytest.fixture(autouse=True)` — `:133` present — PASS |
| callers | `grep -rn "migrated_radar" tests/cobalt` | 0 | `radar_migrated_support.py:1,72,86`; `test_radar_handicap_store.py:7,17,195,200,223`; `test_radar_handicap_dry_run.py:21,158`; `test_radar_panel.py:20,1225`; `test_radar_store.py:9,166`; `test_cards_picks.py:22,332,343,353,363` — the six expected files |
| F2 target | `grep -n "the rule X2 tallies" src/cobalt/radar/handicap_dry_run.py` | 0 | `337:    """The tier that decided one cut ([F-16]; the rule X2 tallies): a name` — ONE |
| F2 target | `grep -n "X2 (grok): 40 of 118" …/handicap_dry_run.py` | 0 | `484:    # X2 (grok): 40 of 118 marginal seats on the retained RTH day were decided` — ONE |
| F3 absent | `grep -rn "not replayable" src/cobalt` | 1 | no output — EMPTY |
| F4 target | `grep -n "NOT MET until he answers R2-1" "docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md"` | 0 | `252:` — ONE |
| pytest | `uv run pytest --version` | 0 | `pytest 9.0.2` |
| restarts probe | `uv run cobalt jobs restarts 026c99b8..HEAD` | 0 | `docs/…/handicap-h1-fix-r1-build-2026-09-24.md A DOCS -` · `RESTARTS: none` (it reads the working tree too: this untracked report) |

## D1 BASELINE
- Offline `uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider` → `2619 passed, 365 skipped, 1 xfailed, 15 warnings in 498.27s (0:08:18)`, exit 0 — `0 failed`, 0 errors. `<bp>` = 2619 / `<bf>` = 0. Equals `43`'s CLOSE.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs tests/cobalt/test_radar_evaluate.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `131 passed, 15 warnings in 24.27s`, exit 0; no `SKIPPED` line; `AWAITING` lines: `AWAITING A RULING: backside` · `AWAITING A RULING: fashionably-late` · `AWAITING A DAY: hitchhiker` · `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)` — exactly `43`'s four.
- With-DB baseline: `43`'s CLOSE record (`2976 passed … 2 deselected`, 0 failed), per the prompt.

## D2 RED (offline)
Tests written (constructed literals only):
- **F1** `tests/cobalt/test_radar_migrated_harness.py::test_no_migrated_radar_caller_also_names_dev_db_tx` — AST read of every `tests/cobalt/test_*.py`: fixture names = the test's `usefixtures` marks + its classes' marks + its parameters; lists any test holding BOTH. The file itself is skipped by name: its D3 with-DB probe names both ON PURPOSE (the prompt's signature `(dev_db_tx, migrated_radar)`), stated in the module.
- **F3** `tests/cobalt/test_radar_replay.py::test_replay_from_bars_reports_handicap_not_replayable` — the `:192` harness's fakes (`ReplayRadarStore`, `ReplaySettingsStore`, `ReplayClock`, patched `Path` / `configured_sources` / `load_config` / `session_clock` / `load_tunables`, `capsys`), window `09:59`–`10:02`, the example note's pool block carrying a CONSTRUCTED `HandicapBlock` (this test's own literals). (i) summary line carries `handicap: not replayable from bars`; (ii) every transition with a `raw_rank` has `handicap_factor` in `(None, Decimal(1))`, and at least one exists (non-vacuous). (ii) is asserted on what the fake store received.

Run `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_migrated_harness.py tests/cobalt/test_radar_replay.py` → `2 failed, 4 passed in 0.69s`. Failures:
- `E       AssertionError: tests naming both migrated_radar and dev_db_tx: ['test_cards_picks.py::TestFillWritesPick::test_fill_writes_exactly_one_pick_row_in_the_fill_transaction', 'test_cards_picks.py::TestFillWritesPick::test_pick_row_snapshots_pool_rank_metric_and_value_at_pick_time', 'test_cards_picks.py::TestFillWritesPick::test_pick_for_ticker_not_in_pool_records_not_in_pool_and_fill_succeeds', 'test_cards_picks.py::TestFillWritesPick::test_degraded_or_missing_pool_row_writes_named_nulls_never_refuses_fill', 'test_radar_panel.py::test_members_for_day_db_returns_both_open_and_left_and_scopes_pool_and_day']` — exactly `45`'s five.
- `E       AssertionError: assert 'handicap: not replayable from bars' in 'replay 2026-09-03: cycles=4 admit=5 leave=0'` (`test_radar_replay.py:398`) — F3 (i).
(ii) is not reached on the base (it sits after (i)). It is a pin: F3's fix changes only the `print` line, never a transition, so (ii)'s result after the fix is its result on the base (D4 proof).

## D3 RED (with-DB)
Test added: `test_a_migrated_radar_test_holds_one_transaction_on_cobalt_dev(dev_db_tx, migrated_radar)` (`@requires_db`): (i) asserts `"migrated_radar" in db.connect.__qualname__`; (ii) `SELECT state FROM pg_stat_activity WHERE pid = %s` with `dev_db_tx.info.backend_pid`, through `migrated_radar`'s connection, printed and asserted `!= 'idle in transaction'`; (iii) prints whether the two backends differ. Read-only.
Under THE LOCK (`## LANE` row D3): `COBALT_ENV=dev uv run pytest -q -rs -s -p no:cacheprovider tests/cobalt/test_radar_migrated_harness.py` → `1 failed, 1 passed in 0.31s`. The one failure is D2's offline F1 red (the same five names, unchanged — F1 (a) not yet built); the probe PASSED. Printed:
```
F1 probe: dev_db_tx backend state = 'idle'
F1 probe: two connections = True
```
**F1 probe: GREEN — the second connection is idle; F1's run-time harm NOT REAL by RUN (L70).** `dev_db_tx`'s connection is opened with `autocommit=True` (`src/cobalt/db.py:199`), its `apply_side` runs there, and nothing executes on it once `migrated_radar` re-patches `db.connect`: two connections, one open transaction. D4 builds F1 (a) ONLY; F1 (b) is NOT built.
`.env: removed, proven gone (D3)`.

## D4 THE EDITS
- **F1 (a), built:** `test_cards_picks.py:330` `usefixtures("dev_db_tx", "pick_pool")` → `usefixtures("pick_pool")`; `test_radar_panel.py:1223` `usefixtures("dev_db_tx")` removed; `radar_migrated_support.py` `migrated_radar(monkeypatch)` → `migrated_radar(monkeypatch, dev_db_tx)` + the one docstring sentence. No assertion touched.
- **F1 (b): NOT built** — D3's probe GREEN (`idle`).
- **F2 — DOC-ONLY, stated as such: no behaviour changes, no red possible; the check reads the text.** `_cut_tier` docstring and `render` comment replaced with the prompt's wording. The rest of the docstring read against `:342-357`: stickiness (`cut.rank <= seats`) → held (`held and cut.rank <= pool.cap`) → priority (group differs / no last) → `first_from` → `position` — every clause matches, none changed.
- **F3:** one hunk in `_scan_replay`: a comment line + ` · handicap: not replayable from bars` on the summary `print`, unconditional.
- **F4 — DOC-ONLY, ONE LINE, stated as such.** v3 `:252` row (c).
- **DevDocs:** `runner.md` +1 sentence (replay reports `handicap: not replayable from bars`); `handicap_dry_run.md` +1 sentence (the cut tier is [F-16]'s per-cut rule (X12), not X2's per-scan tally).

Proofs:
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_migrated_harness.py tests/cobalt/test_radar_replay.py tests/cobalt/test_cards_picks.py tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_handicap_dry_run.py` → `115 passed, 16 skipped in 1.04s` — 0 failed. D2's two reds pass, F3 (ii) included (so (ii) was a pin on the base: only the `print` changed).
- `git diff --stat 026c99b8` → exactly the ten named paths:
```
 docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md   |  2 +-
 docs/40 - DevDocs/cobalt/radar/handicap_dry_run.md |  2 +-
 docs/40 - DevDocs/cobalt/radar/runner.md           |  1 +
 src/cobalt/radar/handicap_dry_run.py               |  6 +-
 src/cobalt/radar/runner.py                         |  3 +-
 tests/cobalt/radar_migrated_support.py             |  3 +-
 tests/cobalt/test_cards_picks.py                   |  2 +-
 tests/cobalt/test_radar_migrated_harness.py        | 85 ++++++++++++++++++++++
 tests/cobalt/test_radar_panel.py                   |  1 -
 tests/cobalt/test_radar_replay.py                  | 70 ++++++++++++++++++
 10 files changed, 165 insertions(+), 10 deletions(-)
```
- `git diff 026c99b8 -- src tests/cobalt/radar_migrated_support.py tests/cobalt/test_cards_picks.py tests/cobalt/test_radar_panel.py`, whole:
```diff
--- a/src/cobalt/radar/handicap_dry_run.py
+++ b/src/cobalt/radar/handicap_dry_run.py
@@ -334,7 +334,7 @@ def _group(transition: Transition) -> str:
-    """The tier that decided one cut ([F-16]; the rule X2 tallies): a name
+    """The tier that decided one cut ([F-16], X12: the tier of every cut; NOT X2's per-scan marginal-seat tally, which ranks held first and stops at one tier per scan — test_h1_x2_marginal_seat.py _tier): a name
@@ -481,9 +481,7 @@ def render(report: DryRun) -> list[str]:
-    # X2 (grok): 40 of 118 marginal seats on the retained RTH day were decided
-    # by stickiness or priority, so the "keeps its seat iff p ≤ h × c"
-    # sentence is never printed; the tier tally says what decided each cut.
+    # X2 (grok, the per-scan marginal-seat experiment): 40 of 118 marginal seats on the retained RTH day were decided by stickiness or priority, so the "keeps its seat iff p ≤ h × c" sentence is never printed. The tally below is _cut_tier's per-cut rule ([F-16], X12), not X2's.
--- a/src/cobalt/radar/runner.py
+++ b/src/cobalt/radar/runner.py
@@ -548,9 +548,10 @@ async def _scan_replay(args) -> None:
+    # v3 §3: replay-from-bars has no float or cap — it reports so and does not guess (R54's missing-header case stores factor 1).
     print(
         f"replay {trade_day}: cycles={counts['cycles']} "
-        f"admit={counts['admit']} leave={counts['leave']}"
+        f"admit={counts['admit']} leave={counts['leave']} · handicap: not replayable from bars"
     )
--- a/tests/cobalt/radar_migrated_support.py
+++ b/tests/cobalt/radar_migrated_support.py
@@ -8,6 +8,7 @@
+dev_db_tx is autouse (conftest.py), so it is declared here: set up first, patched over, torn down last; tests name migrated_radar alone.
@@ -69,7 +70,7 @@ class SavepointProxy:
-def migrated_radar(monkeypatch):
+def migrated_radar(monkeypatch, dev_db_tx):
--- a/tests/cobalt/test_cards_picks.py
+++ b/tests/cobalt/test_cards_picks.py
@@ -327,7 +327,7 @@ def pick_pool(monkeypatch):
-@pytest.mark.usefixtures("dev_db_tx", "pick_pool")
+@pytest.mark.usefixtures("pick_pool")
--- a/tests/cobalt/test_radar_panel.py
+++ b/tests/cobalt/test_radar_panel.py
@@ -1220,7 +1220,6 @@ requires_db = pytest.mark.skipif(
-@pytest.mark.usefixtures("dev_db_tx")
```
(context lines trimmed to the hunk headers; `handicap_dry_run.py`'s diff is docstring / comment lines only; `runner.py` is one hunk inside `_scan_replay`.)
- v3 diff: ONE `-` / ONE `+`:
  - `-| (c) seam as a real artifact | **NOT MET until he answers R2-1.** The seam is … is OPEN FOR DEJAN — R2-1. … Met on the day his A/B lands. |`
  - `+| (c) seam as a real artifact | **MET — R2-1 RULED B [R26].** The seam is … is ruled B [R26]: \`position\` = \`raw_rank\`; \`effective_position\` = the would-be pool-wide rank. … Met on his R26 (12:28 ET 2026-09-22). [R26] |`
- `git diff 026c99b8 -- tests/cobalt/conftest.py src/cobalt/radar/pool.py src/cobalt/radar/store.py src/cobalt/db_migrations src/cobalt/aset configs` → no output.

## D5 THE RUNS
New file `tests/cobalt/test_radar_handicap_fix_r1_runs.py`, five tests, constructed literals only (a block of this file's own six values; `12.5` / `321.25`; tickers `RUNB` / `RUNC`).
- RUN-1: X4's `with_handicap` shape on `radar-screens.example.md`, `load_sources` with X4's `finviz_max_rpm=None`, then `90`.
- RUN-2 (a): `runner.py:327-331`'s `pool_unit` expression over a constructed `SourceSet`, `json.dumps(…, default=str)` as `write_receipt` does, loaded back. `SourceSet.metrics` is typed `float`, so the Decimals ride as floats; compared as strings.
- RUN-2 (b) (with-DB): seed helper — no existing test helper seeds `radar_score_run`; the FKs are seeded through the STORES' OWN PUBLIC CALLS, not a new seeding path: `RadarStore.apply_membership` (writes the `radar_pool` row, `store.py:90-94`) and `RadarStore.open_score_run` (`store.py:395-407`), then `CardStore.write_receipt`, one `SELECT pool_unit …` through `CardStore._connect()` (ESCALATE 3).
- RUN-3 (a) (with-DB): ADMIT → RETAIN at factor `0.65` → ranked `config_cap` LEAVE carrying `raw_rank 6` and its own record, via `RadarStore.apply_membership`, then `members_for_day`. Asserts only that the departed row returns.
- RUN-3 (b): a `MembershipRecord` shaped as (a)'s store leaves it (RETAIN's record, factor `0.6500`, `raw_rank 3`) → `panel._row(record, "departed", None)` → `panel._handicap_cell`. Asserts only that it renders.

Run `uv run pytest -q -rs -s -p no:cacheprovider tests/cobalt/test_radar_handicap_fix_r1_runs.py` → `3 passed, 2 skipped in 0.10s` (the two with-DB halves skip here; D8 runs them). Lines:
```
RUN-1: pool_error = radar.finviz_max_rpm is unmeasured
RUN-1: pool_error (finviz_max_rpm=90) = None
RUN-1: pool.handicap present = True
RUN-2 (a): source_sets[0].metrics keys ['float_m', 'market_cap_m', 'rvol', 'volume'] · float_m 12.5 == 12.5: True · market_cap_m 321.25 == 321.25: True
RUN-3 (b): departed row renders the HANDICAP (shadow) badge: True
RUN-3 (b): rendered cell: <span class="badge badge-cobalt" title="owner COBALT">HANDICAP (shadow)</span><div class="handicap-line">float 7.5M / cap $88M → group (float) · pos 3 → 5</div>
```
RUN-1 GREEN: the remaining `pool_error` is `radar.finviz_max_rpm is unmeasured` — the harness's `None`, not `handicap`; with a ceiling set it is `None` and the block parses. RUN-2 (a) GREEN. RUN-3 (b): a departed row whose stored factor is < 1 DOES render the `HANDICAP (shadow)` badge (no category guard) — measured, no policy asserted; for round 2 (ESCALATE). No red RUN offline → no xfail added.

## D6 LIVE-NOTE
On `<tip>` `2edb2cf3`, D1's command byte for byte → `131 passed, 15 warnings in 24.02s`, exit 0 — 0 failed, 0 errors; no `SKIPPED` line; `AWAITING` lines: `AWAITING A RULING: backside` · `AWAITING A RULING: fashionably-late` · `AWAITING A DAY: hitchhiker` · `AWAITING ITS ENGINE FILL: vwap-continuation (dist.k.vwap null)` — identical to D1. `<lp>` = 131 / `<lf>` = 0.

## D7 OFFLINE
`ls …/handicap-h1/.env` → `No such file or directory`. D1's command on `<tip>` `2edb2cf3` → `2624 passed, 368 skipped, 1 xfailed, 15 warnings in 504.13s (0:08:24)`, exit 0 — 0 failed, 0 errors. `<p>` = 2624 / `<f>` = 0. xfailed 1 = the base's one (no red RUN, no new xfail).
Counts: passed 2624 = `<bp>` 2619 + 5 new offline tests (F1 static, F3, RUN-1, RUN-2 (a), RUN-3 (b)). Skipped 368 = 365 + 3 new with-DB-only tests (the F1 probe, RUN-2 (b), RUN-3 (a)) — counted from the new files' `@requires_db` marks, the three `SKIPPED` rows D3/D5 showed.

## D8 WITH-DB
THE LOCK: `## LANE` row D8. No `cobalt db migrate` at any point.
- (1) `COBALT_ENV=dev uv run pytest -q -rs tests/cobalt tests/taxonomy -p no:cacheprovider --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip` → `2984 passed, 6 skipped, 2 deselected, 1 xfailed, 15 warnings in 589.19s (0:09:49)`, exit 0 — 0 failed, 0 errors. `<dp>` = 2984 / `<df>` = 0; deselected 2. 2984 = `43`'s 2976 + 8 new (the 5 offline + the 3 with-DB of this round). The six skips (verbatim): `test_cards_picks.py:388` (S2-P2's card_score column is present on cobalt_dev), `test_cards_picks.py:401` (real S2-P2 0007 applied …), `test_radar_evaluate.py:695`, `test_replay_line.py:256`, `test_catalyst.py:365`, `test_predicate.py:262` — the same six as `43`'s; none is one of the five F1 callers, `test_radar_store.py`, `test_radar_handicap_store.py` or `test_radar_handicap_dry_run.py`. Table-set probe `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches`: not among the skips, no test failed or errored → GREEN in it.
- (2) `COBALT_ENV=dev uv run pytest -q -rs -s -p no:cacheprovider tests/cobalt/test_radar_migrated_harness.py tests/cobalt/test_radar_handicap_fix_r1_runs.py` → `7 passed in 0.45s`. Printed:
```
F1 probe: dev_db_tx backend state = 'idle'
F1 probe: two connections = True
RUN-1: pool_error = radar.finviz_max_rpm is unmeasured
RUN-1: pool_error (finviz_max_rpm=90) = None
RUN-1: pool.handicap present = True
RUN-2 (a): source_sets[0].metrics keys ['float_m', 'market_cap_m', 'rvol', 'volume'] · float_m 12.5 == 12.5: True · market_cap_m 321.25 == 321.25: True
RUN-2 (b): stored source_sets[0].metrics keys ['float_m', 'market_cap_m', 'rvol', 'volume']
RUN-3 (a): departed row raw_rank 3 · handicap_factor 0.6500 · effective_position 5 · the LEAVE transition's raw_rank 6
RUN-3 (b): departed row renders the HANDICAP (shadow) badge: True
RUN-3 (b): rendered cell: <span class="badge badge-cobalt" title="owner COBALT">HANDICAP (shadow)</span><div class="handicap-line">float 7.5M / cap $88M → group (float) · pos 3 → 5</div>
```
  F1 probe under F1 (a): `idle` (as at D3). RUN-2 (b) GREEN: a stored receipt's `pool_unit` carries `float_m` and `market_cap_m` — X5's stored half PROVEN. RUN-3 (a): the ranked LEAVE stores none of its own three values — the departed row keeps the RETAIN's (`raw_rank 3`, factor `0.6500`, `effective_position 5`) while the LEAVE carried `raw_rank 6`; with (b), the departed row renders the `HANDICAP (shadow)` badge from that kept record. Measured, no policy asserted (round 2).
- (3) `COBALT_ENV=dev uv run pytest -q -s tests/experiments/handicap_h1/test_xl76_membership_harness.py` → `3 passed in 0.17s`: `XL76: callers=11` (the 9 of `43` + RUN-2 (b) + RUN-3 (a)) · `XL76: apply_ms=34` · `XL76: harness_applies=True` · **`XL76: 0014_columns_on_cobalt_dev=0`**.
  `0014: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (XL76)` · `cobalt_dev: 0013`.
- (d) `.env: removed, proven gone (D8)` — `ls …/handicap-h1/.env` → `No such file or directory` (22:53:21).

## RESTARTS
`uv run cobalt jobs restarts 026c99b8..2edb2cf3`:
```
path	change	rule	restart
docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/handicap_dry_run.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
src/cobalt/radar/handicap_dry_run.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/radar_migrated_support.py	M	test/documentation; no resident	-
tests/cobalt/test_cards_picks.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_fix_r1_runs.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_migrated_harness.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
0 UNCLASSIFIED. `runner.py` also derives `com.cobalt.aset` (static import reach) beside the expected `com.cobalt.radar` — recorded (ESCALATE 6), not a stop.

## FOR THE DEPLOY
"Nothing new beyond the fix tip. The H1 range the deploy stacks is `f6643d41..<the fix report commit>` (the build's code `27df13f1`, its report `026c99b8`, this round's red / fix / RUNS commits `94c855ff`..`2edb2cf3` (red `94c855ff`, probe `5db7ec0b`, fix `7b8e5c94`, RUNS `2edb2cf3`), this report). `43`'s `## FOR THE DEPLOY` stands UNCHANGED: the migration `0014_radar_handicap` (and its rollback file), `DIGEST_EXCLUDED`, the forward order (residents down → merge → migrate → residents up → block ABSENT → only then the desk writes his block, `mode: shadow`, parser proof), the ROLLBACK ORDER (the desk removes the block FIRST), and the production dry-run as the deploy's own acceptance. RESTARTS: the table above (`com.cobalt.aset com.cobalt.radar`; the same residents as `43`'s range). This round adds: `migrated_radar` now DECLARES `dev_db_tx` (the deploy's with-DB gate, which takes the lock alone and runs `TestMigrationRoundTrip`, sees the same harness); replay-from-bars prints `handicap: not replayable from bars` (a one-shot CLI, no resident). No new migration, no config change, no new string."

## FOR 61
- Commits: `<red>` `94c855ff`, D3 probe `5db7ec0b`, `<fix>` `7b8e5c94`, `<tip>` `2edb2cf3`, and this report's commit.
- D2's RED summary and both failures (`## D2`); D3's probe: GREEN `idle` → F1 (b) not built (`## D3`).
- D4's quoted diffs: `src`, `radar_migrated_support.py`, the two caller files, the v3 line, the `handicap_dry_run.py` docstring / comment (`## D4`); the `conftest.py` / `pool.py` / `store.py` / migrations / `aset` / `configs` diff: empty.
- D5 and D8 (2) `RUN-` lines; D6 `131 passed` + the four `AWAITING`; D7 `2624 passed, 368 skipped, 1 xfailed`; D8 `2984 passed, 6 skipped, 2 deselected, 1 xfailed`, table-set probe green, `XL76: 0014_columns_on_cobalt_dev=0`, `.env: removed, proven gone (D3, D8)`; the restarts table; `## LANE`.
- F2 and F4 are DOC-ONLY: no red, read the text.

## LANE
| step | (a) `.env` glob | (b) DEVDB-HOLD | (c) after cp | (d) release |
|---|---|---|---|---|
| PREFLIGHT | `no matches found` | No such file | — (read only) | — |
| D3 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | one line: `-rw-------  1 cobalt  staff  2186 Sep 24 22:31 /Users/cobalt/cobalt-wt/handicap-h1/.env` | `rm` → no output; `ls …/handicap-h1/.env` → `No such file or directory` (22:32:04) — `.env: removed, proven gone (D3)` |
| D8 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` | `No such file or directory` | one line: `-rw-------  1 cobalt  staff  2186 Sep 24 22:42 /Users/cobalt/cobalt-wt/handicap-h1/.env` | `rm` → no output; `ls …/handicap-h1/.env` → `No such file or directory` (22:53:21) — `.env: removed, proven gone (D8)` |

## CONTINUE
done — CLOSE written (commits `94c855ff`, `5db7ec0b`, `7b8e5c94`, `2edb2cf3` + this report). CLOSE, before the report commit: `git status --short --branch` → `## radar/handicap-h1-0922` + `?? "docs/40 - DevDocs/reports/handicap-h1-fix-r1-build-2026-09-24.md"` (only this report); `git log --oneline 026c99b8..HEAD` → `2edb2cf3` RUNS · `7b8e5c94` fix · `5db7ec0b` probe · `94c855ff` red. The post-commit `git status` / `ls .env` are quoted in the session's closing reply (writing them here would dirty the tree).

## ESCALATE
1. PREFLIGHT `git status --short --branch` printed a second line: this report, untracked, created by the prompt's own "FIRST Write … `next: AUTHORIZATION`" before D0. Nothing else was dirty; read as clean, not a stop.
2. **D3 F1 probe: GREEN** (`dev_db_tx backend state = 'idle'`, two connections). F1's run-time harm NOT REAL by RUN (L70); F1 (b) NOT built; F1 (a) built. Under F1 (a) at D8: `idle` again.
3. **RUN-2 (b) seed path:** no existing with-DB TEST helper seeds `radar_score_run` (`test_radar_score_migration.py:424` is inline SQL inside a test; `radar_p2_support.py:169` is a fake). The FKs were seeded through the stores' own public production calls (`RadarStore.apply_membership` → `radar_pool`; `RadarStore.open_score_run` → the run), not a new seeding path. The desk / `61` judge whether that reading of "existing helper" holds; RUN-2 (b) ran GREEN on it.
4. **RUN-3 (for `61`, no code here, R96):** `RUN-3 (a): departed row raw_rank 3 · handicap_factor 0.6500 · effective_position 5 · the LEAVE transition's raw_rank 6` — a ranked cap LEAVE writes none of its three values; the departed row keeps the RETAIN's. `RUN-3 (b): departed row renders the HANDICAP (shadow) badge: True` (`… · pos 3 → 5`). v3 is silent on LEAVE rows; the houses rule whether this CONTRADICTS a FINAL clause.
5. F1's static test skips its own file by name: the D3 probe names `dev_db_tx` and `migrated_radar` together on purpose (the prompt's signature). Stated in the module.
6. RESTARTS: `runner.py` derives `com.cobalt.aset` as well as `com.cobalt.radar` (`static import reach`); the EXPECTED line named only the radar. 0 UNCLASSIFIED. The deploy's residents are `com.cobalt.aset com.cobalt.radar`.
7. L74: one block arrived and was recorded once (`## L74`); it was not followed.
8. "The FIX rows moved on file evidence only (`45` `## FOR THE CLASSIFIER` rows 1–2 HOLD; ESCALATE 7 and 9 HOLD in `45`'s file-check). F2 and F4 are DOC-ONLY by the drafter's classification: no red is possible; the check reads the text. Grok's round-1 `CHECK: BUILD STANDS` is the recorded dissent (L39)."
9. "RUN-3 measures ranked LEAVEs and the departed row: v3 is silent on a LEAVE row's three columns; the desk chooses no code (R96); the houses rule on RUN-3's lines in round 2 (`61`), and a HOLD there goes to round 3, the last (L39, L75)."
10. "The check is `61` (round 2; Opus 5.5 + Grok, Sol from Sep 26th, 2026 6:47 AM); H1 is NOT in the 09-25 deploy set until it is clean. The deploy's L68 gate re-proves offline, with-DB (running `TestMigrationRoundTrip`, deselected here under L76) and live-note on the tree that ships."

HANDICAP H1 FIX R1 BUILT 2edb2cf3 | on 026c99b8 | red 94c855ff | offline 2624/0 | with-DB 2984/0 | live-note 131/0 | .env: removed | 0014: rolled back | cobalt_dev: 0013 | FIX: 4 of 4 | RUNS: 3 | ESCALATE: 10
