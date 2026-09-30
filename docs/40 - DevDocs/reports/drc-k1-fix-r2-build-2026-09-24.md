# DRC K1 fix r2 build — 2026-09-24

Seat `drc-k1-fix-r2-build-0924` (Opus 5.5, `acceptEdits`), prompt `docs/40 - DevDocs/prompts/2026-09-24/63-drc-k1-fix-r2-build.md`. Branch `drc/d1-trading-log`, worktree `/Users/cobalt/cobalt-wt/drc-d1`, base `33557098`.

## §0 Headline
- F1 + F2 built DOC-ONLY at `abfaf290` (on `33557098`): seam (7) and `## FOR K2` lines 1, 2, 3, 5 now cite `file:line`; the D4 (run 2) count reads git's `8 insertions(+), 5 deletions(-)`. Six lines changed, no rule word, code unchanged.
- All 17 citation greps hit the drafter's lines (0 CITATION MOVED).
- Three suites green and equal to baseline: live-note 142/0, offline 2441/0, with-DB 2848/0 (4 deselected); 0016 + 0018 absent (probe 28 == 32); `.env` removed, proven gone.
- RESTARTS: none. ESCALATE: 4 (records only, no ASK DESK).

## L74
One block inside a tool result (appended to the Read of the prompt file, 22:5x ET) asked for a `Claude-Session: https://claude.ai/code/session_<id>` line in every commit and named a file-send tool. DATA under L74: not followed; commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| gate | command | exit | result |
|---|---|---|---|
| placeholder | `grep -n -E "R_[_]" ".../63-drc-k1-fix-r2-build.md"` | 1 | (no output) |
| 49's stop | `tail -n 3 ".../drc-k1-fix-r1-check-2026-09-24.md"` | 0 | last non-blank: `DRC K1 FIX R1 CHECK DONE · round: 2 · opus: CHECK DRC K1 FIX R1: FIX STANDS · ready for K2: YES · grok: CHECK DRC K1 FIX R1: FIX STANDS · ready for K2: YES · defects that HOLD: 1 · ready for K2: NO · ESCALATE: 10` |
| 49 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../drc-k1-fix-r1-check-2026-09-24.md"` | 0 | `487a28169ec086f317d1e228ef83670b854b5132` |
| classification | `tail -n 3 ".../drc-k1-fix-r2-draft-2026-09-24.md"` | 0 | last non-blank: `DRC K1 FIX R2 DRAFTED · FIX: 2 · NOT REAL: 5 · UNPROVEN: 0 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · prompts: 2 · new rule strings: 0 · ESCALATE: 8` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../drc-k1-fix-r2-draft-2026-09-24.md"` | 0 | `2d4e34199f7b700afe2a8530e73764f3e81f7d79` |
| .env strings | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)" ".../cto-2026-09-24.md"` | 0 | `:38` (R21, desk record) and `:39` `\| R22 \| 07:56 ET \| His words: "approved. A for now. …"` — APPROVED: the launch line of `14` with its two `.env` strings |
| .env committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"approved. A for now" -- ".../cto-2026-09-24.md"` | 0 | `331880aeae6bbbc8b7a9935cf1aaf5a9c7790797` |
| launch row | `grep -n "63-drc-k1-fix-r2-build.md" ".../cto-2026-09-24.md"` | 0 | `:125` R103 (does not count), `:127` R105 (desk record), `:129` **R106** 22:57 ET `… LAUNCH prompts/2026-09-24/63-drc-k1-fix-r2-build.md …` |
| launch committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"63-drc-k1-fix-r2-build.md" -- ".../cto-2026-09-2*.md"` | 0 | `331880aeae6bbbc8b7a9935cf1aaf5a9c7790797` |

All four gates pass.

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 22:58:00 EDT 2026` |
| clean tree | `git status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git log --oneline -2` | 0 | `33557098 docs(k1-fix-r1): DRC K1 fix r1 build report — 40cf173e` / `40cf173e fix(drc): K1 fix r1 — _reason asks the calendar only after an earlier day row (D8 red)` |
| code unmoved | `git diff --stat 40cf173e 33557098 -- src tests configs` | 0 | (empty) |
| no .env | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |
| lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live folder | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | listed, 22 `.md` notes (names not copied, L32) |
| live-note files | `grep -rln "requires_vault" tests` | 0 | `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_predicate.py`, `tests/taxonomy/test_catalyst.py` — the EXPECTED set |

`<base>` = `33557098`. BASELINE (fix r1 run 2 on `40cf173e`, not re-run): offline `2441 passed, 417 skipped, 1 xfailed`; with-DB `2848 passed, 6 skipped, 4 deselected, 1 xfailed`; live-note `142 passed, 1 skipped`.

## D1 THE EDITS (DOC-ONLY)
No red is possible and none was run: no behaviour changes. Every citation confirmed by ONE `grep -n -F` on this tree (code = `40cf173e`'s); every hit equals the drafter's EXPECTED line — 0 `CITATION MOVED`.

| `grep -n -F` string | file | hit (verbatim) |
|---|---|---|
| `opened_on: Optional` | `src/cobalt/drc/models.py` | `134:    opened_on: Optional[date]` |
| `opened_on=None` | `src/cobalt/drc/pairing.py` | `122:            opened_on=None,` |
| `carried_from=position.opened_on` | `src/cobalt/drc/pairing.py` | `217:        carried_from=position.opened_on,` |
| `opened_on=book.carried_from` | `src/cobalt/drc/pairing.py` | `302:                opened_on=book.carried_from if book.seeded else day,` |
| `def test_a_stated_position_is_one_lot_with_no_time_and_a_stable_id` | `tests/cobalt/test_drc_k1.py` | `129:def test_a_stated_position_is_one_lot_with_no_time_and_a_stable_id():` |
| `pos.opened_on is None and pos.day == D_NEXT` | `tests/cobalt/test_drc_k1.py` | `136:    assert pos.opened_on is None and pos.day == D_NEXT` |
| `assert by_symbol["GGG"].opened_on is None` | `tests/cobalt/test_drc_k1.py` | `174:    assert by_symbol["GGG"].opened_on is None` |
| `assert carried["GGG"].opened_on is None` | `tests/cobalt/test_drc_k1.py` | `182:    assert carried["GGG"].opened_on is None` |
| `pos.opened_on is None and pos.day == D and pos.entry_time is None` | `tests/cobalt/test_drc_k1_store.py` | `444:    assert pos.opened_on is None and pos.day == D and pos.entry_time is None` |
| `is recorded — {day} starts from` | `src/cobalt/drc/store.py` | `501:                f"{day} opening: {prior} is recorded — {day} starts from {prior}'s close "` (Read: the `if` at `496`, `raise` `500`–`504`) |
| `reason = self._reason(conn, day, kind)` | `src/cobalt/drc/store.py` | `523:` and `559:            reason = self._reason(conn, day, kind)` |
| `def test_an_opening_is_refused_while_its_prior_trading_day_is_recorded` | `tests/cobalt/test_drc_k1_store.py` | `312:def test_an_opening_is_refused_while_its_prior_trading_day_is_recorded(migrated, weekday_calendar):` |
| `computed = "pairing" not in pairing.not_computed` | `src/cobalt/drc/store.py` | `212:        computed = "pairing" not in pairing.not_computed` (Read: `if computed and seed is None:` `213`, `raise` to `217`) |
| `if seed is not None:` | `src/cobalt/drc/store.py` | `272:        if seed is not None:` |
| `if computed:` | `src/cobalt/drc/store.py` | `285:        if computed:` |
| `def test_the_route_records_an_unpaired_day_and_the_next_day_fails_until_it_is_stated` | `tests/cobalt/test_drc_k1_store.py` | `567:def test_the_route_records_an_unpaired_day_and_the_next_day_fails_until_it_is_stated(migrated, weekday_calendar):` |
| `earlier = conn.execute(` | `src/cobalt/drc/store.py` | `488:        earlier = conn.execute(` (Read: `return "first import"` at `493`) |
| `prior = prior_trading_day(day)` | `src/cobalt/drc/store.py` | `334:` and `495:        prior = prior_trading_day(day)` |

F2's count: `git show --stat 40cf173e` → exit 0, last line `1 file changed, 8 insertions(+), 5 deletions(-)` — as EXPECTED.

Edits applied (Edit tool): F1 (a) `:256`, F1 (b) `:260`, F1 (c) `:261`, F1 (d) `:262`, F1 (e) `:264`, F2 `:186` — text as the prompt states, lines as read (all unmoved).

Proofs:
- `git diff 33557098 -- "docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md"` → exit 0; two hunks (`@@ -183,7 +183,7 @@`, `@@ -253,15 +253,15 @@`), EXACTLY six `-` / six `+` lines: `:186`, `:256`, `:260`, `:261`, `:262`, `:264`. Each `+` equals its `-` with only the citation added (F2: `: \`+7 / -4\` lines inside \`_reason\`.` → `, inside \`_reason\`: \`8 insertions(+), 5 deletions(-)\` (\`git show --stat 40cf173e\`; corrected by K1 fix r2 — the earlier text read \`+7 / -4\`).`). Whole diff quoted under `## FOR 64`.
- `git diff --stat 33557098 -- src tests configs` → exit 0, (empty).
- `git diff --stat 33557098` → ` docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md | 12 ++++++------` / ` 1 file changed, 6 insertions(+), 6 deletions(-)` — one path.
- Commit → `[drc/d1-trading-log abfaf290] docs(k1-fix-r2): DRC K1 fix r2 — seam (7) and FOR K2 cite file:line; D4 (run 2) count from git (L35, L75, 09-24)` / `1 file changed, 6 insertions(+), 6 deletions(-)`. `git log --oneline -1` → `abfaf290 …`. **`<tip>` = `abfaf290`.**

## D2 LIVE-NOTE
On `abfaf290`: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` (background) → exit 0.
- Summary: `142 passed, 1 skipped, 15 warnings in 9.71s` — `<lp>` / `<lf>` = `142` / `0`; = baseline.
- Only SKIPPED line: `SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (the known one). No SKIPPED names `COBALT_LIVE_VAULT_ROOT`. 0 failed, 0 errors.

## D3 OFFLINE
On `abfaf290`: `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `No such file or directory`. `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → exit 0.
- Summary (output line 434): `2441 passed, 417 skipped, 1 xfailed, 15 warnings in 68.25s (0:01:08)` — `<p>` / `<f>` = `2441` / `0`; = baseline.
- `grep -c "FAILED"` on the output → `0`; `grep -c "ERROR"` → `0`; 386 `SKIPPED` summary lines (grouped `[n]`, 417 tests — the DB-gated set without `.env`).

## D4 WITH-DB
Deselected ids, each confirmed by one `grep -n`:
| id | hit |
|---|---|
| `test_tenancy.py::TestMigrationRoundTrip::test_twice_is_idempotent_and_the_rollback_round_trips` | `697:    def test_twice_is_idempotent_and_the_rollback_round_trips(self):` (class `688:class TestMigrationRoundTrip:`) |
| `test_tenancy.py::TestMigrationRoundTrip::test_the_proof_table_names_every_ruled_table` | `710:    def test_the_proof_table_names_every_ruled_table(self):` |
| `test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default` | `263:    def test_every_user_table_carries_user_id_not_null_with_the_guc_default(` |
| `test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` | `306:def test_rows_reach_the_probe_through_a_named_cursor_in_batches():` |

THE LOCK:
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` — lock free.
- (b) `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 0 (by name, never read) at `Thu Sep 24 23:01:08 EDT 2026`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly one line, `/Users/cobalt/cobalt-wt/drc-d1/.env`.
- (c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` (background) → exit 0.
  - Summary (line 54): `2848 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 148.08s (0:02:28)` — `<dp>` / `<df>` = `2848` / `0`; deselected `4`; = baseline. `grep -c "FAILED"` → `0`, `grep -c "ERROR"` → `0`.
  - Every SKIPPED line (48–53):
    - `tests/cobalt/test_cards_picks.py:383: S2-P2's card_score column is present on cobalt_dev`
    - `tests/cobalt/test_cards_picks.py:396: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged`
    - `tests/cobalt/test_radar_evaluate.py:691: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof`
    - `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`
    - `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft`
    - `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`
  - `test_drc_store.py`, `test_drc_k1_store.py`, `test_drc_k1_experiments.py` are NOT skipped: `grep -c "test_drc"` on the output → `0` (no skip, fail or error line names any `test_drc*` file).
- (c2) ABSENCE PROBE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → exit 1, `1 failed in 5.63s`, `E       assert 28 == 32` (`test_migrate_proof.py:316: AssertionError`). The 28 named cursors listed carry no `cobalt_probe_drc_*` — short by exactly the four `drc_imports`, `drc_fills`, `drc_rows`, `drc_stated_books`: THE KNOWN SHAPE. **0016 + 0018: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 4).**
- (d) `rm /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 0; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → exit 1, `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` at `Thu Sep 24 23:04:06 EDT 2026`. **`.env: removed, proven gone (D4)`.** No `db migrate` of any spelling was run.

## RESTARTS
`uv run cobalt jobs restarts 33557098..abfaf290` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md	M	DOCS	-
RESTARTS: none
```
One row, as EXPECTED; no resident; 0 UNCLASSIFIED.

## FOR 64
- Commit `<tip>` = `abfaf290` `docs(k1-fix-r2): DRC K1 fix r2 — seam (7) and FOR K2 cite file:line; D4 (run 2) count from git (L35, L75, 09-24)`, parent `33557098`. No `wip(k1-fix-r2):` commit. This report is committed above it (docs only).
- D1's `grep -n -F` table as read: see `## D1 THE EDITS (DOC-ONLY)` — every citation's real line equals the drafter's EXPECTED line: models `:134`; pairing `:122`, `:217`, `:302`; test_drc_k1 `:129`, `:136`, `:174`, `:182`; test_drc_k1_store `:312`, `:444`, `:567`; store `:212` (refusal `:213`–`:217`), `:272`, `:285`, `:488` (`first import` `:493`), `:334` / `:495`, `:501` (refusal `if` `:496`–`:504`), `:523` / `:559`.
- `git show --stat 40cf173e` last line: `1 file changed, 8 insertions(+), 5 deletions(-)`.
- `git diff 33557098 -- "docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md"`, whole (the `index 16b5dd2e..3738f307` in the first hunk header is quoted text inside the fix r1 report, not a header of this diff):
```
diff --git a/docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md b/docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md
index 2fe33ffd..98eab3f8 100644
--- a/docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md	
+++ b/docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md	
@@ -183,7 +183,7 @@ index 16b5dd2e..3738f307 100644
 `<fix>` = `ae4388df`.
 
 ## D4 THE EDITS (run 2)
-Resumed 21:19:50 ET on the desk's message (`cto-2026-09-24.md` R91: try 2 of 3, same launch line, context kept). Recovery: `git status --short --branch` → `## drc/d1-trading-log`; `git log --oneline -3` → `ecdf4a4d` / `67a4624b` / `ae4388df`; `.env` absent. H2 reorder in `store.py` `_reason`: the `earlier` query runs first; no earlier `day` row → `first import`, and the calendar is never asked; otherwise `prior_trading_day(day)`, refuse when P has a `day` row, else `chain broken at {prior}`. The behaviour is H2's as before, because a recorded P implies an earlier row. `git diff ae4388df -- src` shows only that block: `+7 / -4` lines inside `_reason`.
+Resumed 21:19:50 ET on the desk's message (`cto-2026-09-24.md` R91: try 2 of 3, same launch line, context kept). Recovery: `git status --short --branch` → `## drc/d1-trading-log`; `git log --oneline -3` → `ecdf4a4d` / `67a4624b` / `ae4388df`; `.env` absent. H2 reorder in `store.py` `_reason`: the `earlier` query runs first; no earlier `day` row → `first import`, and the calendar is never asked; otherwise `prior_trading_day(day)`, refuse when P has a `day` row, else `chain broken at {prior}`. The behaviour is H2's as before, because a recorded P implies an earlier row. `git diff ae4388df -- src` shows only that block, inside `_reason`: `8 insertions(+), 5 deletions(-)` (`git show --stat 40cf173e`; corrected by K1 fix r2 — the earlier text read `+7 / -4`).
 Proofs: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1.py tests/cobalt/test_drc_pairing.py tests/cobalt/test_drc_store.py tests/cobalt/test_drc_stats_log.py` → exit 0, `107 passed, 15 skipped in 0.12s`. `git diff --stat 9a0fc900` → the D4 paths plus `tests/cobalt/test_drc_k1_fix_r1_runs.py` (D5) and this report; `11 files changed, 724 insertions(+), 11 deletions(-)`; no other path. Commit `40cf173e` = `<fix2>` = the new `<tip>` (D5's test is unchanged below it).
 
 ## D5 THE RUN
@@ -253,15 +253,15 @@ Run 2, `uv run cobalt jobs restarts 9a0fc900..40cf173e` → exit 0: the same ele
 (4) Every statement from any caller goes through `DrcStore().record_stated_book(day, kind, positions, via=…, now=…)` (`src/cobalt/drc/store.py:529`). It refuses inside `market_reset` itself (`[F-01]`, `:547`). It refuses an `opening` for D while D's prior trading day is recorded — D starts from that close (v3 §2b, §2c; R51 "the close wins"); `preview_stated_book` (`src/cobalt/drc/store.py:507`) refuses the same, so the page offers `state your opening book` only when `seed_for` returned `None` or failed on a prior day that is not recorded. [H2, fix r1] The page passes `via="drc_page"`; the widget (K4) passes `via="voice_widget"` with `turn_id` + `readback_sha256`.
 (5) `pair_day` (`src/cobalt/drc/pairing.py:231`) is the FIFO engine and holds no book policy: a route never calls it directly.
 (6) D3's `cobalt drc build` joins K1's `drc` parser group in `src/cobalt/drc/cli.py` (`add_parser`, `:150`) — never a second `drc` group (L3).
-(7) A stated position's `opened_on` is `None` (not stated); a page renders it `opened: not stated`, never a date. [H1, fix r1]"
+(7) A stated position's `opened_on` is `None` (not stated); a page renders it `opened: not stated`, never a date. [H1, fix r1; the field `src/cobalt/drc/models.py:134`; `None` for a stated position at `src/cobalt/drc/pairing.py:122`; carried by `_seeded` (`:217`) into `pair_day`'s open position (`:302`); pinned by `tests/cobalt/test_drc_k1.py:136`, `:174`, `:182` and `tests/cobalt/test_drc_k1_store.py:444`]"
 
 ## FOR K2
 `39`'s `## FOR K2` stands, amended by these lines:
-- `OpenPosition.opened_on` is `Optional[date]`: `None` for a stated position and for every day it is carried after (H1). K2's R51 comparison of a stated book with a recorded close compares symbol / direction / shares, never `opened_on`.
-- `record_stated_book` refuses an `opening` for D while D's prior trading day is recorded (H2). `seed_for` case (iv) is therefore reached ONLY in R51's order — D stated first, its prior recorded after — which is exactly the case K2's rebuild replaces. K2's rebuild, when it records P under a stated later day, does not call `record_stated_book` (the statement stays as history, R51).
-- The route records an unpaired day (H3): a `day` row with `not_computed.pairing`, no `seed`, no `book_close`. K2's forward re-pair and its empty-day record meet such rows; K2 states what a re-pair does with one.
+- `OpenPosition.opened_on` is `Optional[date]`: `None` for a stated position and for every day it is carried after (H1; `src/cobalt/drc/models.py:134`, `src/cobalt/drc/pairing.py:122`, `:217`, `:302`). K2's R51 comparison of a stated book with a recorded close compares symbol / direction / shares, never `opened_on`.
+- `record_stated_book` refuses an `opening` for D while D's prior trading day is recorded (H2; the refusal `src/cobalt/drc/store.py:496-504` in `_reason`, reached from `preview_stated_book` `:523` and `record_stated_book` `:559`; pinned by `tests/cobalt/test_drc_k1_store.py:312`). `seed_for` case (iv) is therefore reached ONLY in R51's order — D stated first, its prior recorded after — which is exactly the case K2's rebuild replaces. K2's rebuild, when it records P under a stated later day, does not call `record_stated_book` (the statement stays as history, R51).
+- The route records an unpaired day (H3; `src/cobalt/drc/store.py:212-217` refuses only a COMPUTED day without a book, `:272` writes `seed` only with one, `:285` writes `book_close` only for a computed day; pinned by `tests/cobalt/test_drc_k1_store.py:567`): a `day` row with `not_computed.pairing`, no `seed`, no `book_close`. K2's forward re-pair and its empty-day record meet such rows; K2 states what a re-pair does with one.
 - Carried from `40` ESCALATE 4 (OUT OF SCOPE → K2): two current `resolve` rows for one `trade_id` on DIFFERENT days are both stored (`store.py:547-549` at `9a0fc900`, `:562-564` at `40cf173e`, filters on `day`); v3 `[F-01]` / §4 "FAIL naming both ids" is a reader's failure on the import path — K2's `[F-06]` reader, which replaces `seed_for`'s stored-resolve raise, carries it. The build's ESCALATE 6 (the `day <= D` bound of that raise) is K2's too.
-- H2's refusal asks the calendar only when an earlier `day` row exists (run 2, `40cf173e`): a `first import` statement never reads `prior_trading_day`, as at the base.
+- H2's refusal asks the calendar only when an earlier `day` row exists (run 2, `40cf173e`; `src/cobalt/drc/store.py:488-493` the `earlier` query and `first import`, `:495` `prior_trading_day`): a `first import` statement never reads `prior_trading_day`, as at the base.
 - RUN-1's quoted result (a stated trade against a stats log): GREEN on `ae4388df` and `40cf173e` — no exception; the stated `GGG` trade carries no `stats`; the stats row is `unmatched` with reason `unmatched — 0 trades match` (a stated trade has `entry_time = None`, so the exact match at `pairing.py:370` never hits it). K2 / K3 inherit that a stated trade's stats row is always unmatched until a rule for it is ruled.
 
 ## CONTINUE
```
- `git diff --stat 33557098 -- src tests configs` → (empty). `git diff --stat 33557098` → one path, `1 file changed, 6 insertions(+), 6 deletions(-)`.
- D2 live-note: `142 passed, 1 skipped, 15 warnings in 9.71s` (skip: `test_replay_line.py:256` `COBALT_TEST_LIVE_DRC`).
- D3 offline: `2441 passed, 417 skipped, 1 xfailed, 15 warnings in 68.25s (0:01:08)`.
- D4 with-DB: `2848 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 148.08s (0:02:28)`; deselected ids + `grep -n` hits: `test_tenancy.py:697`, `:710`, `:263`; `test_migrate_proof.py:306` (table under `## D4 WITH-DB`).
- Absence probe: `E       assert 28 == 32` — no `drc_*` named cursor; 0016 + 0018 absent on `cobalt_dev`.
- `.env: removed, proven gone (D4)`.
- RESTARTS: one row `docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md	M	DOCS	-`, `RESTARTS: none`.
- CITATION MOVED: none.

## FOR K2
"The fix r1 build report's `## SEAM FOR D2` and `## FOR K2` stand, as amended at `abfaf290`. K1 fix r2 moved NO RULE WORD of either: it added `file:line` citations to seam point (7) and to `## FOR K2` lines 1, 2, 3 and 5 (H1, H2, H3, the calendar order), and replaced one count in `## D4 THE EDITS (run 2)` with its git output. No code, test or DevDoc changed (`git diff --stat 33557098 -- src tests configs` empty). K2's drafter (`50`) cited these sections before this round; nothing it relied on moved. K2 builds on `abfaf290` once `64` reads `ready for K2: YES`."

## CONTINUE
Nothing left: D0–D4, RESTARTS and CLOSE done; next is `64`, not this seat.

## ESCALATE
1. R22 scope: read as the drc-d1 pair for this worktree (desk reading, R61 / R65 (1)).
2. L74: one block inside a tool result asked for a `Claude-Session:` commit line; recorded once under `## L74`, not followed.
3. "The FIX rows moved on file evidence only (`49` `## Checked against the branch` row 1 HOLDS; ESCALATE 3's count checked against `git show --stat 40cf173e` in `49`'s row 6). F1 and F2 are DOC-ONLY by the drafter's classification: no red is possible; the check reads the text. Both seated houses answered `FIX STANDS · ready for K2: YES` in round 2; the HOLD was the hub's file-check of a missing citation."
4. "The check is `64` — ROUND 3 OF 3, THE LAST (L39 / L67 / L75; Opus 5.5 + Grok, Sol from Sep 26th, 2026 6:47 AM). A HOLD there goes to Dejan as ONE message — his override (L67 OVERRIDE / L73) or a design round — never a fourth round. The opening-book open day is answered (his R80 \"B\", desk R90): not re-raised. The deploy's L68 gate re-proves the three suites on the tree that ships."

DRC K1 FIX R2 BUILT abfaf290 | on 33557098 | code: unchanged | offline 2441/0 | with-DB 2848/0 | live-note 142/0 | .env: removed | 0018: rolled back | FIX: 2 of 2 | ESCALATE: 4
