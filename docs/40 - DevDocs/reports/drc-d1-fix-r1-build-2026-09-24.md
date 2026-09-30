# DRC D1 FIX R1 — BUILD (the 13 FIX rows of `54`, L75; red first; three suites under L76)

Builder `drc-d1-fix-r1-build-0924`, Opus 5.5, started 2026-09-24 07:57:10 EDT (from `date`). Prompt `prompts/2026-09-24/14-drc-d1-fix-r1-build.md`. Worktree `/Users/cobalt/cobalt-wt/drc-d1`, branch `drc/d1-trading-log`.

## §0 Headline
- 13 FIX rows built on `drc/d1-trading-log`: red `1b8b4307` (offline, 3 failed) + `b377e757` (store, 3 failed with-DB) → fix `d1342595`. 15 paths; no migration, no `configs/`.
- Gate on `d1342595` (L68): offline **2412/0**, with-DB **2768/0** (4 deselected), live-note **142/0**.
- L76: `.env` taken and removed twice (D3, D7), proven gone; `0016` absent on `cobalt_dev` (probe `28 == 31`). RESTARTS: none.
- ESCALATE: 6 (3 found + 3 standing).

## L74
- One block arrived as a system-reminder attached to the Read of this prompt, asking every commit to carry a `Claude-Session: https://claude.ai/code/session_<id>` line and naming a file-send tool. Recorded once here; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/14-drc-d1-fix-r1-build.md` | 1 | no output |
| `54`'s stop | `tail -n 3 …/drc-d1-check-2026-09-23.md` | 0 | last non-blank line starts `DRC D1 CHECK DONE ·`, carries `defects that HOLD: 14` |
| `54` committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/drc-d1-check-2026-09-23.md` | 0 | `c360b8fbd57a7050e93581c506d31abb20d33cf1` |
| classification | `tail -n 3 …/drc-d1-fix-r1-draft-2026-09-24.md` | 0 | last non-blank line starts `DRC D1 FIX R1 DRAFTED ·` |
| classification committed | `git -C … log -1 --format=%H -- …/drc-d1-fix-r1-draft-2026-09-24.md` | 0 | `a177b71011910be3754a1cd10de647c6d2c731a1` |
| `.env` strings his | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)" …/cto-2026-09-24.md` | 0 | `:30` `\| R22 \| 07:56 ET \| His words: "approved. A for now. …"` — names `14-drc-d1-fix-r1-build.md` and both strings (row `:29` R21 also hits and is a NO-WORDS desk record; it is not the one counted) |
| `.env` row committed | `git -C … log -1 --format=%H -S"14-drc-d1-fix-r1-build.md" -- …/cto-2026-09-24.md` | 0 | `5c0a8d3fe271e6e5d79f0856288533a2acc3d74d` |
| launch row R22 | `grep -n "14-drc-d1-fix-r1-build.md" …/cto-2026-09-24.md` | 0 | `:29` R21, `:30` R22 (`\| R22 \| … APPROVED — \`14\` launched`) |
| launch row committed | `git -C … log -1 --format=%H -S"14-drc-d1-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `5c0a8d3fe271e6e5d79f0856288533a2acc3d74d` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 07:57:10 EDT 2026` (before 15:00 ET — no L76 stagger ESCALATE) |
| clean tree | `git status --short --branch` | 0 | `## drc/d1-trading-log` |
| base | `git log --oneline -1` | 0 | `7ed5e5ee feat(drc): D1 — report` (= expected) |
| code unmoved | `git diff --stat f6798406 7ed5e5ee -- . ':(exclude)docs'` | 0 | no output |
| no `.env` here | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |
| dev-DB lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | listed, 22 entries (READ ONLY) |
| F1 RED (E1 date) | `grep -rn -e … (D0's paths)` | 0 | **12 hits**: `src/cobalt/drc/trading_log.py:9`; `tests/cobalt/test_drc_detect.py:318`, `:324`; `tests/fixtures/drc/README.md:4`; `docs/40 - DevDocs/reports/drc-d1-build-2026-09-23.md:7`, `:54`, `:55`, `:56`, `:57`, `:71`, `:75`, `:341` |

## D1 BASELINE
On `7ed5e5ee`. Both runs were started before any D2 edit (collection had completed before the first test edit was written).
| leg | command | exit | summary |
|---|---|---|---|
| offline | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` | 0 | `2408 passed, 363 skipped, 1 xfailed, 15 warnings in 69.78s` → `<bp>` = 2408, `<bf>` = 0 |
| live-note | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` | 0 | `142 passed, 1 skipped, 15 warnings in 12.33s` → `<blp>` = 142, `<blf>` = 0 |

Live-note SKIPPED lines naming `COBALT_LIVE_VAULT_ROOT`: **none**. The one skip is `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — a different variable, not on this prompt's line (ESCALATE 1).

## D2 RED (offline)
Edits (test files only): F4a `test_drc_trading_log.py` (`+ assert p.result.line == E1.read_bytes().count(b"\n") + 1`); F4b `test_drc_stats_log.py` (`test_undecodable_bytes_on_a_data_line_name_that_line`); F5 + F2 `test_drc_pairing.py` (`test_an_empty_open_date_cell_is_never_reported_as_an_empty_open_time`, `test_a_carried_short_closes_on_the_next_days_buy_with_its_seed`, `test_a_first_import_reads_a_leading_buy_as_a_long_until_he_rules` — the two F2 tests are GREEN-as-pin, no src change backs them); F7 + F1 part 1 `test_drc_detect.py` (set status `pass` + `by_kind` names — GREEN-as-pin; the non-folders `2001-1-2` / `20010102` / `2001-01-02x`, the folder `2001-01-02` → `date(2001, 1, 2)` — GREEN on unchanged src). F5's stats mutation goes through a new `_set_stats_cell` helper in `test_drc_pairing.py` (the file's own `_set_cell` joins without quoting, which would break the stats log's quoted playbook cell).

`uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_trading_log.py tests/cobalt/test_drc_stats_log.py tests/cobalt/test_drc_pairing.py tests/cobalt/test_drc_detect.py` → exit 1, **`3 failed, 152 passed in 0.24s`** — exactly the three named:
| row | test | assertion line |
|---|---|---|
| F4a | `test_drc_trading_log.py::test_undecodable_bytes_after_the_header_fail_the_file` | `AssertionError: assert 1 == (15 + 1)` |
| F4b | `test_drc_stats_log.py::test_undecodable_bytes_on_a_data_line_name_that_line` | `assert 1 == (5 + 1)` |
| F5 | `test_drc_pairing.py::test_an_empty_open_date_cell_is_never_reported_as_an_empty_open_time` | `assert 'unmatched — ...te, Open Time' == 'unmatched — ... or Open Time'` |

F7 held: `s.status == "pass"` passed (no row 8 ESCALATE).

## D3 RED (with-DB)
Red commit (D2): `1b8b4307`. Edits of `tests/cobalt/test_drc_store.py`: F3 `test_a_prior_day_whose_pairing_was_not_computed_fails_the_seed` (the carry day-1 fixture with `Symbol` dropped from every record, `:340`'s split pattern); F8 `test_an_open_position_row_carries_its_trades_inputs`; F9 `test_a_degraded_file_stores_the_names_it_added` (widened as `test_drc_trading_log.py:93-99`, through the split pattern — E1's trading log has no quoted cell); F6 schema-qualified `"user".drc_imports` + `psycopg.errors.InsufficientPrivilege` (`import psycopg` added) — GREEN-as-pin; F8b `reason == f"PARTIAL — missing: {trading_log.ACCOUNT}"` (`from cobalt.drc import trading_log` added) — GREEN-as-pin.
| step | command | exit | result |
|---|---|---|---|
| (a) lock free | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| (b) take | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env` | 0 | by name, never read |
| (b) one holder | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | exactly one line: `/Users/cobalt/cobalt-wt/drc-d1/.env` |
| (c) red | `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_store.py` | 1 | **`3 failed, 29 passed in 1.14s`**; no `SKIPPED` line |
| (d) release | `rm /Users/cobalt/cobalt-wt/drc-d1/.env` | 0 | — |
| (d) proof | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |

| row | test | assertion line |
|---|---|---|
| F3 | `test_a_prior_day_whose_pairing_was_not_computed_fails_the_seed` | `Failed: DID NOT RAISE <class 'cobalt.drc.models.PairingError'>` |
| F8 | `test_an_open_position_row_carries_its_trades_inputs` | `AssertionError: assert {'trading_log_import_id': 1} == {'carried_lot...d': None, ...}` |
| F9 | `test_a_degraded_file_stores_the_names_it_added` | `AssertionError: assert 'trading_log_shape' == 'trading_log_shape: Added'` |

F6 and F8b passed (no row 7 ESCALATE). **`.env: removed, proven gone (D3)`.**

## D4 THE EDITS
Store red commit (D3): `b377e757`. Fix commit: **`d1342595`** (`<tip>`).
| row | file | change |
|---|---|---|
| F4 (3, 4) | `trading_log.py` `_rows`, `stats_log.py` `_rows` | `UnicodeDecodeError` → line `e.object.count(b"\n", 0, e.start) + 1` (message text unchanged; the whole file still fails with zero rows). Reading: `e.object` in place of the prompt's `data` — `utf-8-sig` strips a BOM before decoding, so `e.start` indexes the BOM-less bytes; the two agree when no BOM is present (every fixture, per `test_every_fixture_has_lf_line_endings_a_final_newline_and_no_bom`) and `e.object` stays right when one is (ESCALATE 3). |
| F5 (5) | `pairing.py` `match_stats` | empty names from `stats_log.SYMBOL`, `stats_log.SIDE`, and `f"{stats_log.OPEN_DATE} or {stats_log.OPEN_TIME}"` for `open_time is None`; the row stays `unmatched` and shown. |
| F3 (2) | `store.py` `seed_for` | after `check_contiguity`, one query in the same connection: a `kind='day'` row for the prior day whose `derived->'not_computed' ? 'pairing'` → `PairingError(f"{day}: the prior trading day {prior} has pairing not computed — its open positions are unknown; never assumed flat")`. `PairingError` imported from `.models`. `pairing.py` FAILS list: `- a seed whose prior day's pairing was not computed (store.seed_for).` |
| F2 (1) | `pairing.py` docstring, THE SEED | the prompt's sentence, verbatim (wrapped). No code change. |
| F8 (14) | `store.py` `record_day` | `trade_inputs[t.trade_id]` built once; the trade row and its open-position row store that same dict. |
| F9 (15) | `store.py` `record_import` | `degraded` = `f"{result.degraded}: {', '.join(result.extras)}"` when both are set, else `result.degraded`. No migration change: `0016_drc.sql:33` reads `    degraded        TEXT,` (no CHECK). |
| F1 (6) part 2 | `trading_log.py:9`, `tests/fixtures/drc/README.md:4`, `reports/drc-d1-build-2026-09-23.md` | the date removed / replaced by `<E1 date>`; his two file names replaced by `<trading-log file>.md` / `<stats-log file>.md`. No removed text quoted here (L32). |
| DevDocs | `docs/40 - DevDocs/cobalt/drc/{trading_log,stats_log,pairing,store}.md` | one sentence each where behaviour changed (decode line ×2, empty-cell reason, not-computed seed FAIL + open-position inputs + degraded names in `store.md`); the ONLY additions beyond the 11 paths → 15 paths in all. |

Proofs:
| proof | command | exit | result |
|---|---|---|---|
| D2's three green | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_trading_log.py tests/cobalt/test_drc_stats_log.py tests/cobalt/test_drc_pairing.py tests/cobalt/test_drc_detect.py` | 0 | `155 passed in 0.11s` |
| date gone | D0's `grep -rn -e "<E1 date>" -e … ` (the prompt's three date forms, same paths) | 1 | **0 hits** |
| names gone | the prompt's `grep -rn -i "<his two file-name stems>" src tests "docs/40 - DevDocs/reports/drc-d1-build-2026-09-23.md"` | 1 | 0 hits |
| paths | `git diff --stat 7ed5e5ee` (before the DevDocs edits) | 0 | exactly the 11 named paths, `11 files changed, 184 insertions(+), 42 deletions(-)` |
| src diff | `git diff 7ed5e5ee -- src` | 0 | quoted below |
| commit | `git add` 15 paths by name; `git commit …` | 0 | `d1342595`, `10 files changed, 65 insertions(+), 42 deletions(-)` (the 5 test files were already in `1b8b4307` / `b377e757`) |

`git diff 7ed5e5ee -- src` (taken before the docstring sentence was re-wrapped to the file's width — words unchanged):
```diff
--- a/src/cobalt/drc/pairing.py
+++ b/src/cobalt/drc/pairing.py
@@ -17,12 +17,13 @@ FAILS THE WHOLE FILE (`PairingError`, L1):
-- a broken import chain (`check_contiguity`, the ASK-DESK safe default).
+- a broken import chain (`check_contiguity`, the ASK-DESK safe default);
+- a seed whose prior day's pairing was not computed (store.seed_for).
@@
-(v2 `[F-10]`).
+(v2 `[F-10]`). A first import has no seed and no chain: a leading B there is read as an open, not a cover (the file cannot tell them apart); his ruling on that day is pending (fix r1 draft, OWNER ITEMS).
@@ -272,11 +273,19 @@ def match_stats(
+        # `open_time` is the combined date + time: None proves only that one
+        # of the two cells is empty, so the pair is named jointly.
         empty = [
-            c for c, v in zip(stats_log.MATCH_INPUTS, (row.symbol, row.side, row.open_time, row.open_time)) if v is None
+            c
+            for c, v in (
+                (stats_log.SYMBOL, row.symbol),
+                (stats_log.SIDE, row.side),
+                (f"{stats_log.OPEN_DATE} or {stats_log.OPEN_TIME}", row.open_time),
+            )
+            if v is None
         ]
         if empty:
-            unmatched.append(Unmatched(row=row, reason=f"unmatched — empty: {', '.join(dict.fromkeys(empty))}"))
+            unmatched.append(Unmatched(row=row, reason=f"unmatched — empty: {', '.join(empty)}"))
--- a/src/cobalt/drc/stats_log.py
+++ b/src/cobalt/drc/stats_log.py
@@ -291,7 +291,7 @@
-            raise StatsLogError(1, f"not UTF-8 text ({e.reason})") from None
+            raise StatsLogError(e.object.count(b"\n", 0, e.start) + 1, f"not UTF-8 text ({e.reason})") from None
--- a/src/cobalt/drc/store.py
+++ b/src/cobalt/drc/store.py
-from .models import DayPairing, Execution, ImportResult, Kind, OpenPosition, Outcome
+from .models import DayPairing, Execution, ImportResult, Kind, OpenPosition, Outcome, PairingError
@@ -110,7 +110,9 @@
-                    result.degraded,
+                    f"{result.degraded}: {', '.join(result.extras)}"
+                    if result.degraded and result.extras
+                    else result.degraded,
@@ -154,20 +156,17 @@
+        trade_inputs: dict[str, dict] = {}
         for t in pairing.trades:
             lines = sorted(leg.line for leg in [*t.entries, *t.legs] if leg.line is not None)
-            out.append((
-                "trade",
-                t.trade_id,
-                {
-                    "trading_log_import_id": trading_id,
-                    "fill_lines": lines,
-                    "carried_lots": [leg.model_dump(mode="json") for leg in t.entries if leg.carried],
-                    "stats_log_import_id": stats_id if t.stats else None,
-                    "stats_line": t.stats.line if t.stats else None,
-                },
-                t.model_dump(mode="json"),
-            ))
+            trade_inputs[t.trade_id] = {
+                "trading_log_import_id": trading_id,
+                "fill_lines": lines,
+                "carried_lots": [leg.model_dump(mode="json") for leg in t.entries if leg.carried],
+                "stats_log_import_id": stats_id if t.stats else None,
+                "stats_line": t.stats.line if t.stats else None,
+            }
+            out.append(("trade", t.trade_id, trade_inputs[t.trade_id], t.model_dump(mode="json")))
@@ -176,12 +175,8 @@
         for p in pairing.open_positions:
-            out.append((
-                "open_position",
-                p.trade_id,
-                {"trading_log_import_id": trading_id},
-                p.model_dump(mode="json"),
-            ))
+            # L57: the position is its trade's remainder — the same inputs.
+            out.append(("open_position", p.trade_id, trade_inputs[p.trade_id], p.model_dump(mode="json")))
@@ -238,6 +233,15 @@
             check_contiguity(day, prior, recorded)
+            if conn.execute(
+                f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} "
+                "AND kind = 'day' AND day = %s AND derived->'not_computed' ? 'pairing'",
+                (prior,),
+            ).fetchone():
+                raise PairingError(
+                    f"{day}: the prior trading day {prior} has pairing not computed — its open "
+                    "positions are unknown; never assumed flat"
+                )
--- a/src/cobalt/drc/trading_log.py
+++ b/src/cobalt/drc/trading_log.py
-THE SHAPE (E1, <E1 date>, `reports/drc-d1-build-2026-09-23.md` `## E1`):
+THE SHAPE (E1, `reports/drc-d1-build-2026-09-23.md` `## E1`):
@@ -187,7 +187,7 @@
-            raise TradingLogError(1, f"not UTF-8 text ({e.reason})") from None
+            raise TradingLogError(e.object.count(b"\n", 0, e.start) + 1, f"not UTF-8 text ({e.reason})") from None
```
(In the quote above the removed `-` line of `trading_log.py:9` shows `<E1 date>` in place of the literal, L32.)

## D5 LIVE-NOTE
On `d1342595`, D1's command byte for byte → exit 0, **`142 passed, 1 skipped, 15 warnings in 9.83s`** → `<lp>` = 142, `<lf>` = 0 (= D1's 142/0). No `SKIPPED` line naming `COBALT_LIVE_VAULT_ROOT`; the one skip is the same `COBALT_TEST_LIVE_DRC` line as D1 (ESCALATE 1). GATE: green.

## D6 OFFLINE
`ls /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. D1's command byte for byte on `d1342595` → exit 0, **`2412 passed, 366 skipped, 1 xfailed, 15 warnings in 68.79s`** → `<p>` = 2412, `<f>` = 0. Context: D1 `<bp>` 2408 + D2's 4 new offline tests (F4b, F5, F2 ×2) = 2412 ✓; skipped 363 + D3's 3 new with-DB tests (skipped offline by design) = 366 ✓. GATE: green.

## D7 WITH-DB
On `d1342595`, `cobalt_dev` only.
| step | command | exit | result |
|---|---|---|---|
| (a) lock free | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| (b) take | `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env` | 0 | by name, never read |
| (b) one holder | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 0 | exactly one line: `/Users/cobalt/cobalt-wt/drc-d1/.env` |
| (c) suite | `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` | 0 | **`2768 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 143.75s (0:02:23)`** → `<dp>` = 2768, `<df>` = 0; deselected 4 (= expected) |
| (d) `0016` probe | `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` | 1 | `1 failed in 5.75s`: `assert 28 == 31` — short by EXACTLY 3; the 28 cursor names listed carry no `drc_*` table |
| (e) release | `rm /Users/cobalt/cobalt-wt/drc-d1/.env` | 0 | — |
| (e) proof | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `No such file or directory` |

The 6 skips (none names Postgres; `test_drc_store.py` NOT skipped): `test_cards_picks.py:383` (card_score present on `cobalt_dev`), `:396` (real S2-P2 0007 applied), `test_radar_evaluate.py:691`, `test_catalyst.py:365`, `test_predicate.py:262` (`COBALT_LIVE_VAULT_ROOT not set` — run in D5's leg instead), `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC`, ESCALATE 1). No `cobalt db migrate` before or after.

**`0016: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 3)`.** **`.env: removed, proven gone (D7)`** (08:06 from `date`, after the rm).

## RESTARTS
`uv run cobalt jobs restarts 7ed5e5ee..d1342595` → exit 0. 15 rows: 5 `docs/…` `DOCS -`; `src/cobalt/drc/{pairing,stats_log,store,trading_log}.py` `static import reach -`; 5 `tests/cobalt/test_drc_*.py` + `tests/fixtures/drc/README.md` `test/documentation; no resident -`. **`RESTARTS: none`** (= expected; `db_migrations/` untouched).

## CONTINUE
done — D0–D7, RESTARTS and CLOSE complete; `.env` absent; nothing to resume.

## ESCALATE
1. **Live-note leg, a second vault variable:** `tests/cobalt/test_replay_line.py:256` skips on `requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — on base (D1) and tip (D5). It is not `COBALT_LIVE_VAULT_ROOT`, so the gate's rule holds, but that one live-note test never runs under this prompt's line. The desk decides whether the L68 live-note command should also set it.
2. **O1 wording is stale by one row:** the F2 docstring sentence (`pairing.py`) and the pin test's docstring say "his ruling … is pending", verbatim from this prompt. `cto-2026-09-24.md` R22 (07:56 ET) has since ruled O1 = **A for now** (first import taken as flat) and queued an OVERNIGHT-POSITION LANE design. Behaviour matches A; only the words lag. Not edited here (L75: nothing outside the F-rows); the desk words the next touch.
3. **F4 reading, `e.object` for `data`:** the line is counted in `e.object` (the bytes the codec actually decoded), not `data`. `utf-8-sig` drops a leading BOM first, so `e.start` indexes the BOM-less bytes; in a BOM-prefixed file, counting in `data` up to `e.start` stops 3 bytes short and names the previous line when the bad byte sits within 3 bytes after a newline. Identical on every committed fixture (no BOM). Stated for `15`.
4. **OWNER ITEM carried, not built:** a first import reads a leading B as an open long (pinned by `test_a_first_import_reads_a_leading_buy_as_a_long_until_he_rules`); his ruling is on the drafter's `## OWNER ITEMS`.
5. **L32, NOT this branch's to fix:** the E1 date stays in the branch's EARLIER commits (`04b05cd4..7ed5e5ee`) and in files on `main` (v2, `53`, `54`'s report, desk reports). A merge of this branch carries those commits; whether history is rewritten before the merge is the desk's call (drafter ESCALATE).
6. **The FIX rows moved on file evidence only** (`54` rows 1–11, 14, 15 HOLD). The red: D2 offline (3 failed) and D3 with-DB (3 failed) on `1b8b4307`/its successor `b377e757`, green on `d1342595`. The check is `15` (round 2; Opus 5.5 + Grok, with Sol from Sep 26th, 2026 6:47 AM), and its packet carries this report's executed output of all three suites (L68). The deploy's L68 gate re-proves them on the tree that ships.

DRC D1 FIX R1 BUILT d1342595 | on 7ed5e5ee | red 1b8b4307 | offline 2412/0 | with-DB 2768/0 | live-note 142/0 | .env: removed | 0016: rolled back | FIX: 13 | ESCALATE: 6
