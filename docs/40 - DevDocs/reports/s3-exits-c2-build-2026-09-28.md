# S3 EXITS C2 BUILD — 2026-09-28

Prompt: `docs/40 - DevDocs/prompts/2026-09-28/22-s3-exits-c2-build.md`. Seat: `s3-exits-c2-build` (Opus 5.5, `acceptEdits`). Worktree `/Users/cobalt/cobalt-wt/s3-exits-c2`, branch `s3/exits-c2`. Start: `date` → `Mon Sep 28 15:54:31 EDT 2026`.

## §0 Headline
- C2 built on `bbf25412`: feat `77cf18fd` — exit legs, THE running read, corrections, the held count, CLOSED, `realized_r.1`, the one-transaction FILLED stop edit, `cobalt cards legs`.
- E1: X21 / X19 / X20 / X-OPEN / X-UR ran; every result as the design expected; design-changing 0.
- Red 33 → green: offline 3252/0, with-DB 3621 + 63 = 3684/0 (X7: one tap written, one refused), live-note 146/0.
- `cobalt_dev` at `0013` (F2 = F0), `.env` removed. RESTARTS: `com.cobalt.aset com.cobalt.radar`.
- ESCALATE 8: three safe defaults the desk has since confirmed as taken, one extra lock take, and two existing tests moved to pass 2.

## L74
Recorded once (L74): after the prompt file was read (15:54), a `<system-reminder>` block arrived asking for a `Claude-Session: https://claude.ai/code/session_…` line in commits and PR bodies and naming a file-send tool. Not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only; no file was sent.

## AUTHORIZATION
`<D>` = 2026-09-28 (`date` → `Mon Sep 28 15:54:31 EDT 2026`).

| gate | command | exit | output |
|---|---|---|---|
| placeholder R__ | `grep -n -E "R_[_]" ".../22-s3-exits-c2-build.md"` | 1 | (nothing) ✓ |
| FILL AT LAUNCH | `grep -n -F "FILL AT LAUNCH" ".../22-s3-exits-c2-build.md"` | 0 | only line 45 (the gate's own line) ✓ |
| R67 | `grep -n "^| R67 " cto-2026-09-22.md` | 0 | line 99, carries `This is why the DasTrader Pro import file is very important` ✓ |
| R38 | `grep -n "^| R38 " cto-2026-09-20.md` | 0 | line 275, carries `"B with your addition"` ✓ |
| R67 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"DasTrader Pro import file is very important" -- ".../cto-2026-09-22.md"` | 0 | `3eeedaa97db9dd8cc7c1ff15aabbaad4b0c9931a` ✓ |
| C1 CHECKED | `tail -n 5 .../s3-exits-c1-fix-r2-check-2026-09-28.md` | 0 | last line: `S3 EXITS C1 FIX R2 CHECK DONE · round: 3 · … · defects that HOLD: 0 · ready for C2: YES · ESCALATE: 3` ✓ |
| launch row R89 | `grep -n -F "22-s3-exits-c2-build.md" cto-2026-09-28.md` | 0 | line 98: `\| R89 \| 15:53 ET \| — NO WORDS OF HIS BEYOND R35 ("Approved as recomended" — C2's .env cp/rm pair) …` names this file, `<base>` = `bbf25412`, C1 tip `944f632e`, "no with-DB run in flight" ✓ |
| his word for the `.env` pair | `grep -n "^| R35 " cto-2026-09-28.md` | 0 | line 44: `**P-HIS — "Approved as recomended"** … (1) the 8 .env cp/rm strings … C2–C4 pairs the same shape re-pathed to s3-exits-c2 …` ✓ |
| R89 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"22-s3-exits-c2-build.md" -- ".../cto-2026-09-28.md"` | 0 | `040526c8106496434c9a3b7c2d3d9046d44777df` ✓ |

AUTHORIZATION: PASS.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 15:54:31 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## s3/exits-c2` + `?? "docs/40 - DevDocs/reports/s3-exits-c2-build-2026-09-28.md"` (this report, written first per `20`'s REPORT rule) |
| base | `git log --oneline -1` | 0 | `bbf25412 docs(s3-c1): S3 exits C1 fix r2 build report — 944f632e` ✓ |
| no code above C1 tip | `git -C /Users/cobalt/cobalt log --oneline 944f632e..s3/exits-c2 -- src tests configs` | 0 | (empty) ✓ |
| no .env here | `ls /Users/cobalt/cobalt-wt/s3-exits-c2/.env` | 1 | `No such file or directory` ✓ |
| no .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` ✓ |
| symbol | `grep -n "def insert_entry_leg" src/cobalt/cards/legs.py` | 0 | `38:def insert_entry_leg(` |
| symbol | `grep -n "def mark_filled" src/cobalt/aset/store.py` | 0 | `198:    def mark_filled(` |
| symbol | `grep -n "def record_stop_edit" src/cobalt/cards/store.py` | 0 | `672:    def record_stop_edit(` |
| symbol | `grep -n "in_trade_shares" src/cobalt/cards/store.py` | 0 | `749:                in_trade_shares=shares if state is CardState.FILLED else None,` |
| symbol | `grep -n "legs_current_v" src/cobalt/db_migrations/0021_legs.sql` | 0 | `1:`, `93:CREATE OR REPLACE VIEW "user".legs_current_v AS`, `98:ALTER VIEW …` |
| live notes | `ls ".../1 - Trading/4 - Strategies"` | 0 | 22 notes listed (9 EMA Reclaim … VWAP Continuation) |
| restarts | `uv run cobalt jobs restarts bbf25412..HEAD` | 0 | only this report (`DOCS`, `-`); `RESTARTS: none` ✓ |

PREFLIGHT: PASS.

## E0 BASELINE
On `<base>` `bbf25412` (no src file edited; the offline run collected before any test file of this build existed).
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (foreground) → **`146 passed, 1 skipped, 15 warnings in 26.89s`**; the one skip `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — no skip names `COBALT_LIVE_VAULT_ROOT`.
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, started 15:5x) → **`3246 passed, 410 skipped, 1 xfailed, 20 warnings in 572.53s (0:09:32)`**, exit 0 — 0 failed, 0 errors (= C1 fix r2's `<p>` 3246). Read `date` → `Mon Sep 28 16:05:17 EDT 2026`.

## E1 EXPERIMENTS
Test file `tests/cobalt/test_s3_c2_experiments.py`, written before any src edit and committed `80e0c8a2 wip(s3-c2): E1 experiments`.

**Lock take 1 (E1 + E2 reds), `20`'s W (b)–(c2) + (f) shape.**
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found` · (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c2/.env`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 28 16:05 /Users/cobalt/cobalt-wt/s3-exits-c2/.env` · **L76 lock taken 16:05:25**.
- `<FP>` (copied whole from `48` line 103, as C1 fix r2's report quotes it):
```
COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*) FROM pg_catalog.pg_attribute a JOIN pg_catalog.pg_class c ON c.oid = a.attrelid JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND a.attnum > 0 AND NOT a.attisdropped) AS cols, (SELECT count(*) FROM pg_catalog.pg_class c JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace WHERE n.nspname IN ('system', 'user') AND c.relkind IN ('r', 'p', 'v')) AS rels, (SELECT md5(string_agg(schemaname || '.' || viewname || ':' || definition, ',' ORDER BY schemaname, viewname)) FROM pg_catalog.pg_views WHERE schemaname IN ('system', 'user')) AS views_md5"
```
  → `cols rels views_md5` / `664 35 272c95bbb12241e3611e4b36326ccf87` → **`F0` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= C1's F0).
- `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `legs` and `voice_turns` `-` (absent): **`cobalt_dev` at `0013`**; `aset_sizings 1 · 0824685c…`, `card_stop_edits 1 · 7599f9ab…`, `card_transitions 4 · f181e76b…`, `cobalt_redactions 183 · d15f9c1f…`, `session_blocks 6 · b650702d…`; `NOTHING WAS APPLIED`; `code: bbf25412 (DIRTY: 4 path(s))`.
- FORWARD `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `-- applying 0001_schemas.sql` … `0013_tunables_slug_nullable.sql`, `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0017_voice_turns.sql`, `0021_legs.sql`; `legs … CREATED`, `voice_turns … CREATED`, every other table `OK`, `content UNCHANGED on every table.` → **`dev forward: APPLIED 16:05:53`**.
- Each `COBALT_ENV=dev` call was directly preceded by `ls -la /Users/cobalt/cobalt-wt/s3-exits-c2/.env` (LISTED).

E1 run: `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no tests/cobalt/test_s3_c2_experiments.py` → **`5 passed in 0.32s`**.

| X | command / test | result (today, code at `<c1 tip>`) | design-changing |
|---|---|---|---|
| **X21** | `test_x21_today_session_b_does_not_wait` — two REAL sessions: A = `record_stop_edit` (WATCH card `X21LK`, stop 9.90 → 9.85) paused right after its `SELECT … FOR UPDATE`; B = `SELECT id FROM aset_sizings WHERE id = %s FOR UPDATE NOWAIT` | PASSED: B **`acquired`** — B does NOT wait (the autocommit connection released A's lock). The design's EXPECTED. Real rows deleted in `finally`, `X21LK` count 0 asserted. | no |
| **X20** | `test_x20_today_a_stop_between_planned_entry_and_fill_is_refused` — long, planned 10.00 / 9.90 / $10 → 100 sh; `mark_filled` at 10.05 (66 sh; `recomputed_shares` 66 asserted); FILLED stop edit to 10.02 | PASSED: `SizingError` `must be below entry` (planned-entry side check). EXPECTED. | no |
| **X20** | `test_x20_today_used_risk_is_the_planned_distance_on_the_planned_shares` — same card; stop to 9.95 | PASSED: `used_risk` **5.00** (0.05 × 100), `shares` 100. EXPECTED. | no |
| **X19** | `test_x19_today_used_risk_is_priced_on_the_planned_shares_not_the_held` — same card filled 66 at the drifted 10.05; stop to 9.85 | PASSED: `used_risk` **15.00** = \|10.00 − 9.85\| × 100 planned, `per_share_risk` 0.1500 — priced on the planned shares and the planned entry, not the 66 held at 10.05 (the live defect, v3 §5). | no |
| **X-OPEN** | `test_x_open_a_filled_card_survives_the_session_boundary_and_one_expiry_cycle` — the X20 card FILLED at the suite's instant (Thu 09-03 10:00 ET); `cards.expire.expire_due(…, now=Fri 09-04 10:00 ET)` | PASSED: not in the moved list; state `FILLED`; last transition `FILLED`. `expire_due` considers only `EXPIRABLE` = WATCH / ARMED / TRIGGERED (`cards/expire.py:71`, `:182`); the radar path `expire_radar_card` refuses FILLED by `IllegalTransition`, logged (`cards/store.py:1093-1109`, read). The "takes a leg the next day" half needs C2's writer: written red at E2 (`test_legs_c2_db.py::test_x_open_a_filled_card_takes_a_leg_the_next_day`). | no |
| **X-UR** | read: `grep -rn "used_risk" src/cobalt/aset src/cobalt/cards` | Render sites of `used_risk`: `aset/web.py:849` (`Total used risk` on the sheet's result card), `aset/radar_panel.py:249` (the panel model's `used_risk` field), `aset/web.py:834` (`Recomputed used risk`, the fill cache's `recomputed_used_risk`). Writers: `aset/store.py:147` (save), `cards/store.py:760` (stop edit), `cards/store.py:1208` (radar key tap); reads `cards/store.py:276` (ARM invariant), `aset/store.py:446`, `:463`; `cards/radar.py:60` (field owner map). Recorded for C3: an exit leaves `used_risk` at the pre-exit count until the next stop edit; C2 does not change that. | no |

X: **5 of 5 run** (X21, X19, X20, X-OPEN, X-UR); **design-changing: 0**.

## E2 RED
Tests only; committed `8c4f116f wip(s3-c2): red` before any src edit. Files: `tests/cobalt/test_legs_c2_db.py` (with-DB, suite transaction + `apply_0021`; X7 on REAL connections), `tests/cobalt/test_realized_r.py` (offline), and `tests/cobalt/test_s3_c2_experiments.py` with X21 / X19 / X20 flipped to their after-C2 values (today's values stay in `80e0c8a2` and the E1 table).

Run inside lock take 1, at `0021` (after `ls -la …/.env` LISTED): `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_realized_r.py` → **`33 failed, 1 passed in 0.80s`**. The one PASSED is X-OPEN's expiry half (it holds today and after). Each red, quoted (the `--tb=line` reason):
| test | red |
|---|---|
| `test_x21_after_c2_session_b_waits_on_the_stop_edit_lock` | `AssertionError: assert 'acquired' == 'waits'` |
| `test_x20_after_c2_a_stop_between_planned_entry_and_fill_is_accepted` | `cobalt.aset.engine.SizingError: Long stop (10.02) must be below entry (10.0000) — refusing, not warning.` |
| `test_x20_after_c2_used_risk_is_the_fill_distance_on_the_running_shares` | `AssertionError: 0.10 (fill 10.05 - 9.95) x 66 running / assert Decimal('5.00') == Decimal('6.60')` |
| `test_x19_after_c2_used_risk_is_priced_on_the_shares_he_holds` | `AssertionError: assert Decimal('15.00') == Decimal('13.20')` |
| `test_legs_c2_db.py` — ½ on 100; stale / duplicate tap; ⅓ on 1; flat ✓ → CLOSED; a failing close rolls the leg back; leg on a non-FILLED card; typed > running; trading-log exit needs its import id; a card filled before C1 (basis); correction of a non-current row; correction off 0 on CLOSED; correction past the entry; correction to 0 → CLOSED; entry-price correction rewrites the cache; trading-log correction; the held count; FILLED stop edit on held shares; reset → `kind = 'reset'`, owner; reset refusals; `market_reset` refuses every writer; X-OPEN next-day leg; `cobalt cards legs`; **X7** | each `AttributeError: module 'cobalt.cards.legs' has no attribute 'record_exit'` / `'running_shares'`, or `ImportError: cannot import name 'LegRefused'` (X7: `cannot import name 'ExitResult'`… from the same import line) — 23 tests, the writers do not exist |
| `test_realized_r.py` (6: long, short, provisional, zero unit, no entry leg, no exit yet) | `ImportError: cannot import name 'realized_r' from 'cobalt.cards.legs'` |

Lock take 1 closed (W (f) shape): ROLLBACK `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `-- applying 0021_legs.rollback.sql`, `0017_voice_turns.rollback.sql`, `0015_shadow_agreement_stale.rollback.sql`, `0014_radar_handicap.rollback.sql`; `legs … DROPPED`, `voice_turns … DROPPED`, every other table `OK` (rows and digests as before the forward: `aset_sizings 1 · 0824685c`, `card_stop_edits 1 · 7599f9ab`, `card_transitions 4 · f181e76b`, `cobalt_redactions 183 · d15f9c1f`), `content UNCHANGED on every table.` `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` → **`cobalt_dev: 0013 — F2 = F0`**. `rm /Users/cobalt/cobalt-wt/s3-exits-c2/.env`; `ls …/s3-exits-c2/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` — **`.env: removed, proven gone (E1/E2) — L76 lock released 16:06:50`** (held 16:05:25 → 16:06:50).

## E3 THE ROWS
Feat commit **`77cf18fd`** `feat(s3): C2 — exit legs, running, corrections, held count, CLOSED, realized R, the FILLED stop edit (v3 §2–§3 / §5, R67, R38)` — 7 files, 925 insertions, 89 deletions. No migration; nothing in `radar/`, `prefill/`, `drc/`, `settings/models.py`, `aset/` (C2-6 needed no `engine.py` change: `recompute_for_stop` is passed the fill price as its `entry`).
| row | built | files |
|---|---|---|
| C2-1 | `running_shares(conn, card_id) -> Running` — THE running read; takes the card lock itself (re-entrant); basis `legs` / `recomputed_shares` / `shares` | `src/cobalt/cards/legs.py` |
| C2-2 | `record_exit(…) -> ExitResult` — gate first; one connection, autocommit off, `SELECT * … FOR UPDATE`; FILLED only; stale tap refused; presets ⌊/2⌋ ⌊/3⌋ flat typed; zero / over-running refused; seq = max current + 1; CLOSED in the same transaction | `legs.py` |
| C2-3 | `record_correction(…) -> CorrectionResult` — current-row check; over-entry / CLOSED-off-0 refused; to 0 → CLOSED; entry-price correction rewrites the fill cache (plan at the fill, stored P) | `legs.py` |
| C2-4 | `record_held(card_id, held, *, source, now)` — S-HELD entry correction; CLOSED refused with the exact text; held 0 → CLOSED | `legs.py` |
| C2-5 | `realized_r(card_row, current_legs) -> RealizedR` (`realized_r.1`), pure | `legs.py` |
| C2-6 | `CardStore.record_stop_edit(…, kind='edit')` one transaction, lock to commit; FILLED prices from the entry-leg price (else `actual_fill`, else `entry`) on `running_shares`; never writes `shares`; reset only to `structural_stop` (NULL → refused, O19 A); `stop_owner(card_id)` | `src/cobalt/cards/store.py` |
| C2-7 | `cobalt cards legs <card_id>` (read only, via `legs.read_position`, rolled back) | `src/cobalt/cards/cli.py` |
| C2-8 | DevDocs `cards/legs.md` (writers, refusals, S-C2), `cards/store.md` (C2-6), `cards/cli.md` (the `legs` row) | `docs/40 - DevDocs/cobalt/cards/` |

**Pre-check (lock take 2, not in the prompt's plan; same L76 procedure)** before the feat commit: `.env` copied 16:11:07 (`ls -la …/*/.env` → only this worktree's); `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` (F0); FORWARD → `0014`, `0015`, `0017`, `0021` applied, `legs` / `voice_turns` CREATED, `content UNCHANGED`. First run of the C2 files + neighbours HUNG at `test_a_failing_close_rolls_the_leg_back_with_it` (bash timeout 600 s, stopped with TaskStop): the test's `monkeypatch.undo()` also undid the suite's `db.connect` patch, so its next read went to a real session and waited on the suite transaction's `apply_0021` locks — a TEST defect; fixed to restore only its own patch (in `77cf18fd`). Re-run: `COBALT_ENV=dev uv run pytest -q -rA … tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_realized_r.py` → **`34 passed in 1.17s`**; `… tests/cobalt/test_cards.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_aset_web.py` → **`127 passed in 4.73s`**. ROLLBACK to `0013` (`legs`, `voice_turns` DROPPED; every table `OK`, rows as before); `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` → `F2 = F0`; `.env` removed, `ls` → `No such file or directory` — **lock released 16:22:50**.

## W THE THREE SUITES
`<tip>` = `77cf18fd` (the feat commit; every suite runs on that tree).
- **(a) offline:** `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, 16:23 → 16:32, no `.env`) → **`3252 passed, 438 skipped, 1 xfailed, 20 warnings in 559.92s (0:09:19)`**, exit 0 — 0 failed, 0 errors → **`<p>` = 3252** (E0 3246 + the 6 offline `realized_r` tests; the new with-DB files skip offline).
- **(b) LOCK (W, lock take 3):** `ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found` · `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/s3-exits-c2/.env` · `ls -la …/*/.env` → exactly `-rw-------  1 cobalt  staff  2186 Sep 28 16:32 /Users/cobalt/cobalt-wt/s3-exits-c2/.env` · **L76 lock taken 16:32:38**. `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` → **`F0`**. `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → `legs` / `voice_turns` `-`: **`0013`**; rows / digests as at E1 (`aset_sizings 1 · 0824685c…`, `card_stop_edits 1 · 7599f9ab…`, `card_transitions 4 · f181e76b…`, `cobalt_redactions 183 · d15f9c1f…`, `session_blocks 6 · b650702d…`, `vault_writes 187 · 2c8181e1…`); `code: 77cf18fd (DIRTY: 1 path(s))` (this report). Every `COBALT_ENV=dev` call below directly preceded by `ls -la …/s3-exits-c2/.env` (LISTED).
- **(c) PASS 1 at `0013`** (background, started 16:33); the executed command WHOLE — C1 fix r2's (c) byte for byte plus four deselects for C2's `0021` tests:
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk
```
  → **`3621 passed, 6 skipped, 63 deselected, 1 xfailed, 20 warnings in 649.34s (0:10:49)`**, exit 0; read 16:43:58 → **`<d1>` = 3621** (63 deselected = C1's 33 + C2's 30: 23 in `test_legs_c2_db.py`, 5 in `test_s3_c2_experiments.py`, 2 in `test_cards.py`). The six SKIPPED lines, verbatim: `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof` (same six as C1).
- **(c2) FORWARD:** `COBALT_ENV=dev uv run cobalt db migrate` (foreground) → `-- applying 0001_schemas.sql` … `0013`, then `0014_radar_handicap.sql`, `0015_shadow_agreement_stale.sql`, `0017_voice_turns.sql`, `0021_legs.sql`; `legs … CREATED`, `voice_turns … CREATED`, every other table `OK`; `content UNCHANGED on every table.`; no `CHANGED`. The forward's BEFORE probe reads `cobalt_redactions 184 · 86d03bb7` (183 at (b)): +1 during pass 1 — the known outside writer (`test_redact.py:393`, R61 OWED), as in C1. **`dev forward: APPLIED 16:44:15`**. `<FP>` → `773 38 126f2d6983fa59f9d0eaaff7da7dd29c` → **`F1` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`** (= C1's F1).
- **(c3) PASS 2 at `0021`** (background, 16:44); the executed command WHOLE — C1's (c3) nine ids + its two files, plus C2's `0021` tests:
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk -rA
```
  → **`63 passed, 5 warnings in 137.64s (0:02:17)`**, exit 0, no SKIPPED, no FAILED line → **`<d2>` = 63** (C1's 33 + C2's 30, X7 and X21 on real connections among them). **`<d>` = 3621 + 63 = 3684.**
- **(c3r) nothing left behind:** `COBALT_ENV=dev uv run cobalt db query --side user "SELECT ticker, count(*) FROM aset_sizings WHERE ticker IN ('X7CT', 'X21LK', 'X1RF', 'TEST') GROUP BY ticker"` → `ticker count` (no rows); `… "SELECT count(*) FROM legs"` → `0`.
- **X22** — not repeated (C2 adds no migration, per the prompt).
- **(e) live-note:** `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → **`146 passed, 1 skipped, 15 warnings in 26.11s`**; the one skip `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — none names `COBALT_LIVE_VAULT_ROOT` → **`<l>` = 146**.
- **(f) ROLLBACK:** `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (foreground) → `0021`, `0017`, `0015`, `0014` reversed; `legs … DROPPED`, `voice_turns … DROPPED`, every other table `OK` (`cobalt_redactions 184 -> 184 86d03bb7 OK`), `content UNCHANGED on every table.` `<FP>` → `664 35 272c95bbb12241e3611e4b36326ccf87` → **`F2` = `F0` field for field → `cobalt_dev: 0013 — F2 = F0`** (16:47:40).
- **Lock (d):** `rm /Users/cobalt/cobalt-wt/s3-exits-c2/.env`; `ls …/s3-exits-c2/.env` → `No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — **`.env: removed, proven gone (W) — L76 lock released 16:47:44`** (held 16:32:38 → 16:47:44). `0021` not applied.

## RESTARTS
`uv run cobalt jobs restarts bbf25412..77cf18fd` (explicit shas; this untracked report is outside the range), exit 0 — the table WHOLE:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/cards/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/legs.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/store.md	M	DOCS	-
src/cobalt/cards/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/cards/legs.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_legs_c2_db.py	A	test/documentation; no resident	-
tests/cobalt/test_realized_r.py	A	test/documentation; no resident	-
tests/cobalt/test_s3_c2_experiments.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row.

## SEAM FOR C3
Every `file:line` read on `<tip>` `77cf18fd` (greps at 16:2x).
- **The lock** every C2 writer takes: `SELECT * FROM aset_sizings WHERE id = %s FOR UPDATE` (`cards/legs.py:154`, `_lock_card`); `running_shares` re-takes it (`legs.py:302`); `record_stop_edit` takes `SELECT entry, direction, risk_budget, state, structural_stop, actual_fill FROM aset_sizings WHERE id = %s FOR UPDATE` (`cards/store.py:737-738`). One connection per write, `autocommit = False`, one commit, rollback on any exception. Every writer runs the session gate (`assert_writable`) FIRST: in `market_reset` it raises `cobalt.session.SessionBlocked` and nothing is read or written.
- **Writers and signatures:**
  - `record_exit(card_id, *, preset, shares=None, price, price_source, price_asof, flag, source, running_before, now, source_import_id=None) -> ExitResult(leg_id, shares, running_before, running_after, closed, transition_id)` — `legs.py:375`. `preset ∈ PRESETS = ("half", "third", "flat", "typed")` (`:53`); `shares` only with `typed`. The panel posts the `running_before` its screen showed (read it from `running_shares` / `read_position`). CLOSED: `transition_id` is the FILLED → CLOSED row, evidence `{"leg_id": <leg>}` (`_close_if_zero`, `legs.py:228-240`; actor YOU).
  - `record_correction(leg_id, *, price=None, at=None, flag=None, price_source=None, shares=None, source, now, source_import_id=None) -> CorrectionResult(leg_id, corrects, running_after, closed, transition_id)` — `legs.py:486`. A changed price REQUIRES `price_source`; it is `confirmed` unless `flag` is given (the ✓ confirm of an `estimated` flat = a correction with the typed price, `price_source='typed'`).
  - `record_held(card_id, held, *, source, now) -> CorrectionResult` — `legs.py:607`.
  - `CardStore.record_stop_edit(card_id, *, from_stop, to_stop, actor=Actor.YOU, now=None, kind='edit') -> int` — `cards/store.py:682`; `kind` ∈ `STOP_EDIT_KINDS = ('edit', 'reset')` (`store.py:77-79`); the ↺ control passes `kind='reset'` with `to_stop` = the card's `structural_stop`. Do not render ↺ on a card with NULL `structural_stop` (O19 A: refused if called).
  - `CardStore.stop_owner(card_id) -> 'yours' | 'cobalt'` — `store.py:849` (`STOP_OWNER_YOURS` / `STOP_OWNER_COBALT`, `:80-81`).
- **Refusals C3 renders verbatim** — all `LegRefused(CardStateError)` (`legs.py:68`) with `.code`, except the stop edit's (`CardStateError`) and the engine's side check (`SizingError`):
  | code | text (`<…>` filled at run time) | raised at |
  |---|---|---|
  | `stale` | `REFUSED: screen said <posted>, now <computed> — tap again` | `legs.py:419` |
  | `zero_preset` | `REFUSED card <id>: ½ of <running> is 0 — use flat or type` (⅓ for third; `flat` of 0 → `flat of 0 is 0 — use flat or type`) | `:363` |
  | `over_running` | `REFUSED card <id>: an exit of <n> shares is more than the <running> still held. Nothing written.` | `:367` |
  | `typed_shares` | `REFUSED card <id>: a typed exit names its share count (> 0), got <x>. Nothing written.` / `REFUSED card <id>: the <preset> preset computes its own shares — <x> typed with it. Use typed. Nothing written.` | `:347`, `:355` |
  | `preset` | `REFUSED card <id>: preset <p> is not one of ('half', 'third', 'flat', 'typed').` | `:406` |
  | `not_filled` | `REFUSED card <id>: an exit leg needs a FILLED card — it is <STATE>. Nothing written.` (exit, `:412`); `… a correction needs a FILLED or CLOSED card — it is <STATE>. Nothing written.` (`:536`); `… a held count needs a FILLED card — it is <STATE>. Nothing written.` (`:639`) | |
  | `import_id` | `REFUSED: a trading-log row names the import it came from — source_import_id is required with source = 'trading_log'. Nothing written.` / `REFUSED: source_import_id is carried only by a trading-log row, not by source <s>. Nothing written.` (`:162`, `:168`); held: `REFUSED: a held count is his statement — the trading log reconciles through record_correction with its source_import_id. Nothing written.` (`:625`) | |
  | `not_current` | `REFUSED: leg <id> is not the current row of seq <n> on card <c> — the current row is <cur>. Correct that one. Nothing written.` | `:546` |
  | `over_entry` | `REFUSED card <id>: the exits would total <x> shares against an entry of <y>. Nothing written.` | `:560` |
  | `closed_off_zero` | `REFUSED card <id>: CLOSED has no way back — this correction would leave <n> shares running. Nothing written.` | `:567` |
  | `closed_held` | `CLOSED has no way back — correct the exit instead` | `:637` |
  | `no_entry_leg` | `REFUSED card <id>: filled before C1, it has no entry leg for the held count to correct (running is read from <basis>). Nothing written.` | `:646` |
  | `held_zero_no_exit` | `REFUSED card <id>: holding 0 with no exit recorded — record the exit (flat) instead. Nothing written.` | `:653` |
  | `held` / `shares` / `no_change` / `price_source` / `no_leg` | argument refusals, each `REFUSED: … Nothing written.` | `:631`, `:526`, `:518`, `:520`, `:532` |
  | `no_position` | `card <id> is <STATE> with no entry leg — it holds no position.` | `:324` |
  | stop edit (`CardStateError`) | `REFUSED: the stop is not editable in <STATE>. Decision 11 — …`; `REFUSED card <id>: a reset returns the stop to Cobalt's structural stop, and this card has none (a manual card) — no Cobalt stop to reset to. Type the stop instead. Nothing written.`; `REFUSED card <id>: a reset goes to Cobalt's structural stop <s>, not <t>. Nothing written.`; `REFUSED card <id>: stop-edit kind <k> is not one of ('edit', 'reset').` | `store.py:747`, `:755`, `:761`, `:718` |
  | side check (`SizingError`) | `Long stop (<t>) must be below entry (<fill price>) — refusing, not warning.` (in FILLED the "entry" is the fill price) | `aset/engine.py:105-112` |
- **`running_shares`' `basis`** (`legs.py:57-59`): `legs` · `recomputed_shares` · `shares`. `Running(shares, basis, base_shares, exit_shares, entry_leg_id, entry_price, state)` (`:78`). `running_shares(conn, card_id)` needs an open non-autocommit transaction; C3's render reads through `read_position(card_id) -> Position(card, legs, running, realized)` (`:719`, rolled back, writes nothing).
- **`realized_r`'s return shape** (`legs.py:683`): `RealizedR(function_id='realized_r.1', value: Decimal | None, provisional: bool, r_unit: Decimal | None, reason: str | None)`; `reason` ∈ `not computed — zero risk unit`, `not computed — no entry leg`. Never stored; C3 renders `value` with `provisional`.
- **X-UR** (E1): `used_risk` render sites `aset/web.py:849` (Total used risk, sheet result card) and `aset/radar_panel.py:249` (panel model field); `aset/web.py:834` renders the cache's `recomputed_used_risk`. An exit leaves `used_risk` at the pre-exit count until the next stop edit (C2 does not change that; the stop edit prices on the running shares).
- **S-C2 as built:** `record_exit` / `record_correction` accept `source = 'trading_log'` only with `source_import_id` (`_check_source`, `legs.py:160-172`); rows are appended, his rows never touched (proven: `test_a_trading_log_correction_needs_its_import_id_and_leaves_his_rows_untouched`); CLOSED only when running reaches 0; refusals raised by name. No trading-log caller built.
- **Unchanged for C3:** `mark_filled` (`aset/store.py:198`) is THE fill; the S-WEB placement rule of `20` holds for C3's routes.

## FOR THE CHECK
- Range `<base>..<tip>` = `bbf25412..77cf18fd`: `80e0c8a2 wip(s3-c2): E1 experiments` · `8c4f116f wip(s3-c2): red` · `77cf18fd feat(s3): C2 — exit legs, running, corrections, held count, CLOSED, realized R, the FILLED stop edit (v3 §2–§3 / §5, R67, R38)`. The report commit follows.
- Suites on `77cf18fd`: offline `3252 passed, 438 skipped, 1 xfailed` (0 failed); with-DB pass 1 `3621 passed, 6 skipped, 63 deselected, 1 xfailed` + pass 2 `63 passed` = 3684 (0 failed); live-note `146 passed, 1 skipped` (the known `COBALT_TEST_LIVE_DRC` skip).
- Fingerprints (W): `F0` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`; `F1` = `773 · 38 · 126f2d6983fa59f9d0eaaff7da7dd29c`; `F2` = `F0`. The same F0 / F2 at E1 and the pre-check.
- Lock takes: E1+E2 16:05:25 → 16:06:50 (`0021` applied 16:05:53, rolled back before 16:06:50); pre-check 16:11:07 → 16:22:50; W 16:32:38 → 16:47:44 (`0021` applied 16:44:15 → rolled back 16:47:40). Each F2 = F0.
- E1 table: X21, X19, X20 (×2), X-OPEN, X-UR — 5 of 5 run, design-changing 0 (all as the design EXPECTED today).
- Worth the checker's eye: ESCALATE 4 (the cache rewrite's plan-at-fill and whether it is a second cache writer under L3); ESCALATE 6 (two existing tests moved to pass 2); the FILLED stop edit's side check now runs against the fill price (a stop between the planned entry and the fill is accepted — X20); `record_stop_edit`'s `edit` INSERT leaves `kind` to its 0021 default, so WATCH edits stay writable at `0013`.
- The stop line is the last line of this file.

## CONTINUE
- next: none. The desk verifies the artifact (L35) and launches `23-s3-exits-c2-check.md`.

## ESCALATE
1. Owner defaults taken (R35 (5): the drafter's A defaults), one line each:
   - O1 A — ½ = ⌊running/2⌋, ⅓ = ⌊running/3⌋ (`legs.py` `_preset_shares`).
   - O14 A — the preset set ½ · ⅓ · flat · typed (`PRESETS`).
   - O15 A — realized R on the ACTUAL unit only; no planned-unit output.
   - O19 A — a reset on a card with NULL `structural_stop` is refused; C3 does not render ↺ there.
   - O21 A — a card filled before C1 reads `recomputed_shares`, else `shares`; `basis` names which.
   - O22 A — a correction or held count that brings running to 0 closes the card in the same transaction.
2. ASK DESK: the FILLED → CLOSED row written by a `trading_log` leg or correction carries `actor = you` (the design's actor for "his leg that brings running to 0"; the trading log is his broker's record of his own exit). Safe default taken: `you`, evidence `{"leg_id": …}` exactly. [16:3x]
3. ASK DESK: a held count and a correction copy the corrected row's `at` (the entry's time stays the fill's; S-HELD names price / price_source / price_asof as copied and is silent on `at`). The instant he made the statement is not stored — `legs` has no recorded-at column and C2 adds no migration. Safe default taken: copy. [16:3x]
4. ASK DESK: the entry-price correction's cache rewrite is its own UPDATE in `legs.py` (`_rewrite_fill_cache`), not `AsetStore._update_fill_cache` — that function stamps `filled_at = now()` and `aset/store.py` is not one of C2's files. It recomputes through the one rebuild (`SizingResult.from_card`) and `compute_fill_recompute`, against the plan AT THE FILL (the card with the entry leg's `stop_in_force` as its stop — a FILLED stop edit has moved the card's stop since) and the P stored at the fill; `filled_at` / `drift_warning_pct` untouched. The checker should judge whether this is a second writer of the cache under L3 / v3 Q4. [16:3x]
   — A cross-session message signed `cto-desk` (arrived during W (a)) answered items 2–4: "the safe defaults you took stand (actor = you; held count / correction copy `at`; `_rewrite_fill_cache` as built). Record them in the report as taken; checker `23` judges item 4 under L3." Recorded: items 2–4 stand as TAKEN; nothing in the build changed on it.
5. Process: a SECOND lock take (the pre-check, 16:11:07 → 16:22:50) that the prompt's plan did not name — same L76 procedure, F2 = F0, `.env` proven gone. Its first run HUNG on a test defect (`monkeypatch.undo()` undoing the suite's `db.connect` patch → a real session blocked behind the suite transaction's `apply_0021` locks); the run was stopped (TaskStop) — the killed process's suite transaction rolled back with its connection; the test was fixed before the feat commit.
6. Two EXISTING with-DB tests now need `0021` (the FILLED stop edit reads `legs_current_v`): `test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled` and `test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk` — deselected from pass 1, run in pass 2 (W). Deploy note: C2's FILLED stop edit and `stop_owner` need `0021` applied with the code.
7. L74: the block is recorded once under `## L74`.
8. **C2 is checked by `23-s3-exits-c2-check.md` (a NEW build's chunk: Opus 5.5 · Astra · Grok, L67) before C3 stacks on it; the builder decided nothing.**

S3 EXITS C2 BUILT 77cf18fd | on bbf25412 | migration none (0021 rolled back) | X: 5 of 5 run, design-changing: 0 | offline 3252/0 | with-DB 3684/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | ESCALATE: 8
