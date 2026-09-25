# DRC K1 fix r1 — build report (2026-09-24)

Seat `drc-k1-fix-r1-build-0924` · Opus 5.5 · prompt `docs/40 - DevDocs/prompts/2026-09-24/48-drc-k1-fix-r1-build.md` · branch `drc/d1-trading-log` · base `9a0fc900` (tip `a50e5515`).

## §0 Headline
- BUILT on the second try, tip `40cf173e`. Run 1 FAILED at D8 at 21:17: 13 `CalendarError`s from H2 asking the calendar on every opening. The desk resumed it at 21:19 (R91), and `_reason` was reordered so the calendar is asked only after an earlier `day` row.
- FIX 3 (H1 / H2 / H3), RUNS 1 (RUN-1 passes as a plain test). Red `d158a8a3` (offline) and `0009e9c1` (with-DB), exactly the named tests.
- On `40cf173e`: offline `2441/0`, with-DB `2848/0` (4 deselected), live-note `142/0`. RESTARTS: `com.cobalt.radar`.
- `.env` removed and proven gone (D3, D8 ×2). `0016` / `0018` absent on `cobalt_dev` (probe `28 == 32`). ESCALATE: 10.

## L74
A system-reminder appended to the prompt's Read result (21:08 ET) asked commits to end with a `Claude-Session:` line and named a file-send tool (`SendUserFile`). Recorded as DATA per L74; not followed — commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| rule | command | exit | result |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" …/48-drc-k1-fix-r1-build.md` | 1 | (no output) |
| `40`'s stop | `tail -n 3 …/drc-k1-check-2026-09-24.md` | 0 | last line `DRC K1 CHECK DONE · round: 1 · … · defects that HOLD: 3 · ready for K2: NO · ESCALATE: 14` |
| `40` committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- …/drc-k1-check-2026-09-24.md` | 0 | `3aff0134f024826de22c2b580d8abe3c91a3b1eb` |
| classification | `tail -n 3 …/drc-k1-fix-r1-draft-2026-09-24.md` | 0 | `DRC K1 FIX R1 DRAFTED · FIX: 3 · NOT REAL: 15 · UNPROVEN: 1 · OUT OF SCOPE: 4 · OWNER ITEM: 1 · prompts: 2 · new rule strings: 0 · ESCALATE: 4` |
| classification committed | `git -C … log -1 --format=%H -- …/drc-k1-fix-r1-draft-2026-09-24.md` | 0 | `712e753b60f8e37715c554abe30815351ded4537` |
| `.env` strings his | `grep -n -F "Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)" …/cto-2026-09-24.md` | 0 | `37:| R22 | 07:56 ET | His words: "approved. A for now. …` (also `36:| R21 |`, the desk record it answers) |
| R22 committed | `git -C … log -1 --format=%H -S"approved. A for now" -- …/cto-2026-09-24.md` | 0 | `7c21fe86f9efae6363739ec32b752cacf4ce6925` |
| launch row | `grep -n "48-drc-k1-fix-r1-build.md" …/cto-2026-09-24.md` | 0 | `91:| R76 |` (not counted), `111:| R90 | 21:06 ET | … DESK LAUNCH ROW for prompts/2026-09-24/48-drc-k1-fix-r1-build.md …` |
| launch row committed | `git -C … log -1 --format=%H -S"48-drc-k1-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | 0 | `7c21fe86f9efae6363739ec32b752cacf4ce6925` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| clock | `date` | 0 | `Thu Sep 24 21:08:12 EDT 2026` |
| clean tree | `git status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git log --oneline -2` | 0 | `a50e5515 docs(k1): DRC K1 build report — 9a0fc900` / `9a0fc900 feat(drc): K1 — drc_stated_books (0018), …` |
| code unmoved | `git diff --stat 9a0fc900 a50e5515 -- . ':(exclude)docs'` | 0 | (no output) |
| `.env` absent | `ls /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |
| the lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| live strategies | `ls ".../1 - Trading/4 - Strategies"` | 0 | listed (22 notes) |
| requires_vault files | `grep -rln "requires_vault" tests` | 0 | `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/radar_p2_support.py`, `tests/cobalt/test_replay_line.py`, `tests/taxonomy/test_catalyst.py`, `tests/taxonomy/test_predicate.py` — the expected set (`-l` used for the file list) |

## D1 BASELINE
On `a50e5515` (code `9a0fc900`).
| run | command | exit | summary |
|---|---|---|---|
| offline | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` | 0 | `2438 passed, 415 skipped, 1 xfailed, 15 warnings in 68.79s` → `<bp>` 2438 / `<bf>` 0 (matches `39`'s S8) |
| live-note | `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` | 0 | `142 passed, 1 skipped, 15 warnings in 9.88s` → `<blp>` 142 / `<blf>` 0 |

Live-note SKIPPED lines: one, `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (the known one); none names `COBALT_LIVE_VAULT_ROOT`.

## D2 RED (offline)
Edits (`tests/cobalt/test_drc_k1.py`): the reversed `:132` assertion (now `:136`, `assert pos.opened_on is None and pos.day == D_NEXT`, docstring names H1); NEW `test_a_stated_positions_open_day_stays_not_stated_through_the_carry` (with the `HHH` control on both days); NEW `test_a_carried_positions_open_day_is_kept` (GREEN-as-pin).
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1.py tests/cobalt/test_drc_pairing.py` → exit 1, `2 failed, 53 passed in 0.11s`:
- `test_a_stated_position_is_one_lot_with_no_time_and_a_stable_id` — `test_drc_k1.py:136` `E       AssertionError: assert (datetime.date(2001, 1, 3) is None)`
- `test_a_stated_positions_open_day_stays_not_stated_through_the_carry` — `test_drc_k1.py:174` `E       AssertionError: assert datetime.date(2001, 1, 3) is None`
Exactly the two named; `test_a_carried_positions_open_day_is_kept` passed. `<red>` = `d158a8a3`.

## D3 RED (with-DB)
Edits (`tests/cobalt/test_drc_k1_store.py`): H1 — the reversed `:420` assertion (now `:444`, `assert pos.opened_on is None and pos.day == D and pos.entry_time is None`, docstring names H1); H2 — NEW `test_an_opening_is_refused_while_its_prior_trading_day_is_recorded`; H2's consequence — `test_seed_iv_a_statement_beside_a_recorded_close_fails_until_k2` SETUP reordered (`_state(D_NEXT)` first, then `_day1_carrying_ddd()`), its `pytest.raises(PairingError, match=…)` line byte for byte, one docstring sentence — NOT an assertion change; H3 — NEW `test_the_route_records_an_unpaired_day_and_the_next_day_fails_until_it_is_stated` (GREEN-as-pin: the store already allows it, `store.py:212-217`; the seam text is the fix).
THE LOCK: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`; (b) `cp` by name, then `ls -la` → one line, `-rw-------  1 cobalt  staff  2186 Sep 24 21:10 /Users/cobalt/cobalt-wt/drc-d1/.env`.
(c) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1_store.py tests/cobalt/test_drc_k1_experiments.py` → exit 1, `2 failed, 56 passed in 3.13s`; 0 `SKIPPED` lines (`test_drc_k1_store.py` ran, not skipped):
- `test_an_opening_is_refused_while_its_prior_trading_day_is_recorded` — `test_drc_k1_store.py:320` `E       Failed: DID NOT RAISE <class 'ValueError'>`
- `test_seed_vi_a_stated_book_seeds_a_first_import` — `test_drc_k1_store.py:444` `E       AssertionError: assert (datetime.date(2001, 1, 2) is None)`
Exactly the two named. The reordered case (iv) and the H3 pin PASS on the base. No `cobalt db migrate` run (the suite applied `0016` / `0018` inside its own transaction, `-- applying 0016_drc.sql` / `-- applying 0018_drc_stated_books.sql` in captured setup).
(d) `rm` by name; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory`. `.env: removed, proven gone (D3)`.
Commit `0009e9c1`.

## D4 THE EDITS
- **H1** `models.py:133-134` `opened_on: Optional[date]` + the one-line comment; `pairing.py:110-126` `stated_open_positions` → `opened_on=None`, docstring "its open day not stated"; `_Book.seeded: bool = False` (`:140`), `_seeded` sets `seeded=True` (`:218`), `pair_day` `:302` `opened_on=book.carried_from if book.seeded else day`. `carried_from=position.opened_on` unchanged.
- **H2** `store.py` `_reason`: for `opening`, a `kind = 'day'` row on `prior_trading_day(day)` → `ValueError("<day> opening: <prior> is recorded — <day> starts from <prior>'s close (v3 §2b; R51: the close wins); a stated opening is taken only on a first import or a broken chain (v3 §2c); nothing written")`, one more query in the same connection; otherwise unchanged. Both callers (`record_stated_book` inside its transaction, `preview_stated_book`) refuse through it. CLI not edited: `drc/cli.py:126-144` wraps the dry run (`preview_stated_book`) AND the apply in one `try` whose `except (SessionBlocked, PairingError, ValueError, ValidationError)` prints `REFUSED: …` and exits 1 — the dry run surfaces the H2 refusal.
- **REORDER RULE**: applied to ZERO further tests. Every other with-DB statement was read: `test_drc_store.py:274-278` `_stated_flat` states D before D is recorded and D's prior is never recorded (callers `:387`, `:416`, `:431`, `:462`, `:473`); `test_drc_k1_experiments.py:139`, `:204`, `:219`, `:311`, `:415` state D only (prior unrecorded); `test_drc_k1_store.py` `_state(D3)` (`:307`, `:319-320`, `:426`) has an unrecorded prior `D_NEXT`; `_state(D_NEXT, kind="resolve")` is not an `opening`. D8 is the proof. `test_drc_k1_experiments.py` untouched.
- **H3** no src change; `## SEAM FOR D2` below.
- **DevDocs** `docs/40 - DevDocs/cobalt/drc/models.md` (the not-stated open day), `pairing.md` (`stated_open_positions` + the seeded carry), `store.md` (the opening refused beside a recorded prior; the unpaired day recorded by the route).

Proofs:
| proof | command | exit | result |
|---|---|---|---|
| offline | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1.py tests/cobalt/test_drc_pairing.py tests/cobalt/test_drc_store.py tests/cobalt/test_drc_stats_log.py` | 0 | `107 passed, 15 skipped in 0.13s` (the with-DB tests skip offline) |
| scope | `git diff --stat 9a0fc900` | 0 | `docs/40 - DevDocs/cobalt/drc/models.md`, `…/pairing.md`, `…/store.md`, `…/reports/drc-k1-build-2026-09-24.md` (`a50e5515`'s), `src/cobalt/drc/models.py`, `src/cobalt/drc/pairing.py`, `src/cobalt/drc/store.py`, `tests/cobalt/test_drc_k1.py`, `tests/cobalt/test_drc_k1_store.py` — `9 files changed, 399 insertions(+), 11 deletions(-)`; no other path |
| readers | `grep -rn "opened_on" src/cobalt` | 0 | `drc/models.py:134` (the field), `drc/pairing.py:122` (`opened_on=None`), `:217` (`carried_from=position.opened_on`, `Optional` already), `:302` (the seeded read). No reader formats it as a date; nothing outside `drc/models.py` / `drc/pairing.py` |

`git diff 9a0fc900 -- src`, whole:
```diff
diff --git a/src/cobalt/drc/models.py b/src/cobalt/drc/models.py
index de58c7eb..5d7a8897 100644
--- a/src/cobalt/drc/models.py
+++ b/src/cobalt/drc/models.py
@@ -130,7 +130,8 @@ class OpenPosition(_Frozen):
     held_shares: int = Field(gt=0)
     lots: list[Lot]
     entry_time: Optional[datetime]
-    opened_on: date
+    # None = not stated — a stated position's open day is his to give (v3 :134 names none); never the stated day (L1).
+    opened_on: Optional[date]
     day: date  # the import day whose file left it open
 
 
diff --git a/src/cobalt/drc/pairing.py b/src/cobalt/drc/pairing.py
index 3a1df791..a7b243e6 100644
--- a/src/cobalt/drc/pairing.py
+++ b/src/cobalt/drc/pairing.py
@@ -110,7 +110,7 @@ def book_sha256(positions: Iterable[OpenPosition]) -> str:
 def stated_open_positions(day: date, positions: Iterable[StatedPosition]) -> list[OpenPosition]:
     """His stated `opening` book for `day` as the pairing's seed: ONE lot
     per position, its cost `None` when he gave none, NO time (v3
-    `[F-04]`; never an invented one), opened on the stated day."""
+    `[F-04]`; never an invented one), its open day not stated."""
     return [
         OpenPosition(
             trade_id=stated_trade_id(p.symbol, p.direction, day),
@@ -119,7 +119,7 @@ def stated_open_positions(day: date, positions: Iterable[StatedPosition]) -> lis
             held_shares=p.shares,
             lots=[Lot(time=None, price=p.avg_cost, shares=p.shares)],
             entry_time=None,
-            opened_on=day,
+            opened_on=None,
             day=day,
         )
         for p in positions
@@ -137,6 +137,7 @@ class _Book:
     exits: list = field(default_factory=list)
     realized: Union[Decimal, str] = Decimal(0)
     carried_from: Optional[date] = None
+    seeded: bool = False
 
     @property
     def held(self) -> int:
@@ -214,6 +215,7 @@ def _seeded(position: OpenPosition) -> _Book:
         position.trade_id,
         position.entry_time,
         carried_from=position.opened_on,
+        seeded=True,
     )
     for lot in position.lots:
         book.lots.append(lot)
@@ -295,7 +297,9 @@ def pair_day(
                 held_shares=book.held,
                 lots=list(book.lots),
                 entry_time=book.entry_time,
-                opened_on=book.carried_from or day,
+                # A seeded book keeps its position's open day, None
+                # included; a book opened today opened today.
+                opened_on=book.carried_from if book.seeded else day,
                 day=day,
             )
         )
diff --git a/src/cobalt/drc/store.py b/src/cobalt/drc/store.py
index 16b5dd2e..3738f307 100644
--- a/src/cobalt/drc/store.py
+++ b/src/cobalt/drc/store.py
@@ -475,18 +475,31 @@ class DrcStore:
 
     @staticmethod
     def _reason(conn, day: date, kind: str) -> str:
-        """Derived by the store, never passed in (v3 `:139`)."""
+        """Derived by the store, never passed in (v3 `:139`). An `opening`
+        for a day whose prior trading day is recorded is REFUSED: that day
+        starts from the recorded close (R51), and neither reason v3 names
+        would be true of it (L1)."""
         if kind == "resolve":
             return "closed outside export"
         if kind == "no_trade":
             return "no-trade DRC"
         from cobalt.daymode.propose import prior_trading_day
 
+        prior = prior_trading_day(day)
+        if conn.execute(
+            f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day = %s LIMIT 1",
+            (prior,),
+        ).fetchone():
+            raise ValueError(
+                f"{day} opening: {prior} is recorded — {day} starts from {prior}'s close "
+                "(v3 §2b; R51: the close wins); a stated opening is taken only on a first "
+                "import or a broken chain (v3 §2c); nothing written"
+            )
         earlier = conn.execute(
             f"SELECT 1 FROM drc_rows WHERE user_id = {_TENANT} AND kind = 'day' AND day < %s LIMIT 1",
             (day,),
         ).fetchone()
-        return f"chain broken at {prior_trading_day(day)}" if earlier else "first import"
+        return f"chain broken at {prior}" if earlier else "first import"
 
     def preview_stated_book(
         self,
```
`<fix>` = `ae4388df`.

## D4 THE EDITS (run 2)
Resumed 21:19:50 ET on the desk's message (`cto-2026-09-24.md` R91: try 2 of 3, same launch line, context kept). Recovery: `git status --short --branch` → `## drc/d1-trading-log`; `git log --oneline -3` → `ecdf4a4d` / `67a4624b` / `ae4388df`; `.env` absent. H2 reorder in `store.py` `_reason`: the `earlier` query runs first; no earlier `day` row → `first import`, and the calendar is never asked; otherwise `prior_trading_day(day)`, refuse when P has a `day` row, else `chain broken at {prior}`. The behaviour is H2's as before, because a recorded P implies an earlier row. `git diff ae4388df -- src` shows only that block, inside `_reason`: `8 insertions(+), 5 deletions(-)` (`git show --stat 40cf173e`; corrected by K1 fix r2 — the earlier text read `+7 / -4`).
Proofs: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1.py tests/cobalt/test_drc_pairing.py tests/cobalt/test_drc_store.py tests/cobalt/test_drc_stats_log.py` → exit 0, `107 passed, 15 skipped in 0.12s`. `git diff --stat 9a0fc900` → the D4 paths plus `tests/cobalt/test_drc_k1_fix_r1_runs.py` (D5) and this report; `11 files changed, 724 insertions(+), 11 deletions(-)`; no other path. Commit `40cf173e` = `<fix2>` = the new `<tip>` (D5's test is unchanged below it).

## D5 THE RUN
`tests/cobalt/test_drc_k1_fix_r1_runs.py` (new): `test_run_1_a_stated_trade_against_a_stats_log` — seed `stated_open_positions(D_NEXT, [GGG short 40, avg_cost None])`; day file `CARRIED_SHORT_DAY2` (`09:40:00,GGG,B,19.5,40,…`, `test_drc_pairing.py:246`); a one-row stats log = `stats_log_e1.csv`'s header + row 2 through `test_drc_pairing.py`'s `_set_stats_cell`, `Symbol` / `Instrument` → `GGG`, `Side` → `short`, `Open Date` / `Close Date` → `2001-01-03`; `build_day(trading, stats, seed=seed)`.
`uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1_fix_r1_runs.py` → exit 0, `1 passed in 0.02s`.
RUN-1 GREEN on `ae4388df`: no exception; the `GGG` trade's `stats is None`; the one stats row (line 2, `GGG`) is in `unmatched`, attached to no other trade; its `reason` — asserted equal, so quoted by the passing assertion — is `unmatched — 0 trades match`. Kept as a plain pin (no mark). `<tip>` = `67a4624b`.

## D5 THE RUN (run 2)
On `40cf173e`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_drc_k1_fix_r1_runs.py` → exit 0, `1 passed in 0.02s`. RUN-1 still passes; the reason is still `unmatched — 0 trades match`.

## D6 LIVE-NOTE
On `67a4624b`, D1's command byte for byte → exit 0, `142 passed, 1 skipped, 15 warnings in 10.35s` → `<lp>` 142 / `<lf>` 0, 0 errors. SKIPPED: only `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (known); none names `COBALT_LIVE_VAULT_ROOT`. GATE met.

## D6 LIVE-NOTE (run 2)
On `40cf173e`, D1's command byte for byte → exit 0, `142 passed, 1 skipped, 15 warnings in 10.39s` → `<lp>` 142 / `<lf>` 0, 0 errors. The one SKIPPED line is the known `test_replay_line.py:256` (`COBALT_TEST_LIVE_DRC`); none names `COBALT_LIVE_VAULT_ROOT`.

## D7 OFFLINE
`ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory`. D1's offline command byte for byte on `67a4624b` → exit 0, `2441 passed, 417 skipped, 1 xfailed, 15 warnings in 70.40s (0:01:10)` → `<p>` 2441 / `<f>` 0, 0 errors. xfailed 1 = the base's one (RUN-1 green, no new mark). `<p>` = `<bp>` 2438 + 3 new offline tests that pass (D2: 2; D5: 1) ✓; skipped +2 = the two new with-DB tests (H2, H3) skipping offline.

## D7 OFFLINE (run 2)
`ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. On `40cf173e`, D1's offline command byte for byte → exit 0, `2441 passed, 417 skipped, 1 xfailed, 15 warnings in 70.26s (0:01:10)` → `<p>` 2441 / `<f>` 0, 0 errors; xfailed 1 (the base's).

## D8 WITH-DB
Deselects, each confirmed by one `grep -n`: `test_tenancy.py:697` `def test_twice_is_idempotent_and_the_rollback_round_trips(self):` and `:710` `def test_the_proof_table_names_every_ruled_table(self):` (class `TestMigrationRoundTrip`, `:688`); `test_tenancy.py:263` `def test_every_user_table_carries_user_id_not_null_with_the_guc_default(`; `test_migrate_proof.py:306` `def test_rows_reach_the_probe_through_a_named_cursor_in_batches():`.
THE LOCK: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`; (b) `cp` by name, `ls -la` → one line, `-rw-------  1 cobalt  staff  2186 Sep 24 21:14 /Users/cobalt/cobalt-wt/drc-d1/.env`.
(c) started 21:14:35 ET: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → exit 1, **`13 failed, 2835 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 145.17s (0:02:25)`**. RED.
All 13 failures raise the same thing: `E           cobalt.session.calendar.CalendarError: no NYSE calendar for 2001 (asked about 2001-01-01). Loaded years: [2025, 2026]. Add /Users/cobalt/cobalt-wt/drc-d1/configs/cobalt/calendar/nyse-2001.yaml — this never guesses a trading day from the weekday alone.` (`src/cobalt/session/calendar.py:95`). Failing tests, all ones that state an `opening` for `2001-01-02` WITHOUT the `weekday_calendar` fixture:
- `test_drc_k1_store.py`: `test_a_stated_row_is_append_only`, `test_a_cli_statement_stores_no_turn_and_no_readback`, `test_the_via_rules`, `test_a_hash_mismatch_is_refused_before_any_write`, `test_a_second_opening_for_one_day_is_refused_until_it_supersedes`, `test_a_supersedes_that_names_no_current_row_is_refused`, `test_the_preview_is_the_row_without_its_id_and_writes_nothing`, `test_the_cli_dry_runs_then_writes_only_the_reviewed_hash[opening flat]`, `test_the_cli_dry_runs_then_writes_only_the_reviewed_hash[opening positions]`, `test_the_cli_apply_is_refused_inside_market_reset_and_the_dry_run_still_prints`, `test_the_cli_restates_with_supersedes`
- `test_drc_store.py`: `test_a_day_stores_every_trade_stats_row_and_the_day_with_inputs_and_fn_version`, `test_an_open_position_row_carries_its_trades_inputs` (both through `_stated_flat`)
CAUSE (read from the traceback and the diff; THIS BRANCH, not a DEV-DB SEAM): the H2 edit in `store.py` `_reason` calls `prior_trading_day(day)` for EVERY `opening`, before the `earlier` query. At `9a0fc900` it was called only when an earlier `day` row existed. With no calendar loaded for 2001, every `opening` statement in a test without `weekday_calendar` now fails. The D3 red run did not show this because every NEW or changed test there uses `weekday_calendar`. The refusal's placement is the defect; H2's rule is not.
FIX for the relaunch (the smallest one; the prompt's D4 H2 text allows it — "one more query in the same connection", otherwise unchanged): run the `earlier` query FIRST, and only when `earlier` exists compute `prior = prior_trading_day(day)`, check that prior for a `day` row (refuse) and otherwise return `chain broken at {prior}`. P recorded implies an earlier `day` row, so behaviour is unchanged and `first import` never touches the calendar, as it did at the base. NOT applied here: the prompt's D8 rule is "Any red → (d) FIRST, then FAILED".
(c2) the absence probe: NOT run (it runs on green only). `0018` absence on `cobalt_dev` is therefore UNPROVEN by this run. The suite applies `0016` / `0018` only inside its own transaction (captured setup `-- applying 0018_drc_stated_books.sql`), and no `cobalt db migrate` was typed.
(d) `rm` by name; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory`. **`.env: removed, proven gone (D8)`.**

## D8 WITH-DB (run 2)
On `40cf173e`; same four deselected ids as run 1 (each confirmed above by `grep -n`).
THE LOCK: (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (and the desk's 21:19 `pg_catalog.pg_tables` read of `cobalt_dev`: no `drc_*` table, R91); (b) `cp` by name, `ls -la` → one line, `-rw-------  1 cobalt  staff  2186 Sep 24 21:21 /Users/cobalt/cobalt-wt/drc-d1/.env`.
(c) the same command as run 1 → exit 0, **`2848 passed, 6 skipped, 4 deselected, 1 xfailed, 15 warnings in 145.98s (0:02:25)`** → `<dp>` 2848 / `<df>` 0, 0 errors; deselected 4. The six SKIPPED lines are `test_cards_picks.py:383` and `:396` (the S2-P2 `cobalt_dev` state), plus four live-vault skips (`test_radar_evaluate.py:691`, `test_replay_line.py:256`, `test_catalyst.py:365`, `test_predicate.py:262`). None is in `test_drc_store.py`, `test_drc_k1_store.py` or `test_drc_k1_experiments.py`, so all three ran. Run 1's 13 `CalendarError` failures are gone. 2848 = run 1's 2835 passed + 13.
(c2) `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches` → exit 1, `1 failed in 5.69s`, `E       assert 28 == 32`. That is short by EXACTLY 4: the 28 named cursors list no `drc_imports`, `drc_fills`, `drc_rows` or `drc_stated_books`. **`0016 + 0018: rolled back — applied only inside the suite's transaction; absent on cobalt_dev (probe short by 4)`.**
(d) `rm` by name; `ls /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory`. **`.env: removed, proven gone (D8)`**, 21:24:17 ET.

## RESTARTS
`uv run cobalt jobs restarts 9a0fc900..67a4624b` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/drc/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/pairing.md	M	DOCS	-
docs/40 - DevDocs/cobalt/drc/store.md	M	DOCS	-
docs/40 - DevDocs/reports/drc-k1-build-2026-09-24.md	A	DOCS	-
src/cobalt/drc/models.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/pairing.py	M	static import reach	com.cobalt.radar
src/cobalt/drc/store.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_drc_k1.py	M	test/documentation; no resident	-
tests/cobalt/test_drc_k1_fix_r1_runs.py	A	test/documentation; no resident	-
tests/cobalt/test_drc_k1_store.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
As expected: the three `src/cobalt/drc/*` paths derive `com.cobalt.radar` (static import reach, as `39`'s range); tests and docs derive nothing; 0 UNCLASSIFIED. (Run on the code tip, before this report's own commit, which adds one DOCS path.)

Run 2, `uv run cobalt jobs restarts 9a0fc900..40cf173e` → exit 0: the same eleven rows plus `docs/40 - DevDocs/reports/drc-k1-fix-r1-build-2026-09-24.md	A	DOCS	-`; the three `src/cobalt/drc/*.py` → `com.cobalt.radar`; `RESTARTS: com.cobalt.radar`; 0 UNCLASSIFIED.

## SEAM FOR D2
"`[F-17]` CONTRACT, as built by K1 at `9a0fc900` and amended by K1 fix r1 at `40cf173e` (signatures from this tree at `40cf173e`):
(1) Before pairing an import for day D, the route calls `DrcStore().seed_for(D)` → `Optional[SeedBook]` (`src/cobalt/drc/store.py:323`). It RAISES `PairingError` on a broken chain, an uncomputed prior, a pre-lane prior (`rebuild <P>`), a hash mismatch, a stated-vs-recorded conflict (R51 — K2) and a stored unapplied resolve (K2). Each is a loud FAILED on the page, never caught into a flat book.
(2) `None` means no book is stated. The route calls `build_day(trading, stats, seed=None)` (`src/cobalt/drc/pairing.py:394`) → `not computed — opening book not stated`, and RECORDS that day: `DrcStore().record_day(pairing, import_ids, None)` (`src/cobalt/drc/store.py:199`) — one `day` row carrying `not_computed.pairing`, the stats rows unmatched, NO `seed` and NO `book_close` (v3 §4 row 1 "stores files; pairing not computed", X2 (a)). It shows `state your opening book for <D>` (K3's form; until K3, the `cobalt drc state-book` CLI, R52). Until he states D's book and D is re-paired and recorded with it, the next day's `seed_for` FAILS `pairing not computed` — never a flat book. [H3, fix r1; pinned by `tests/cobalt/test_drc_k1_store.py::test_the_route_records_an_unpaired_day_and_the_next_day_fails_until_it_is_stated`]
(3) Otherwise `build_day(trading, stats, seed=book.positions)`, then `DrcStore().record_day(pairing, import_ids, book)` — `seed` is REQUIRED for a computed day (a computed day without one is refused, `src/cobalt/drc/store.py:213`), and `book` is the `SeedBook` `seed_for` returned.
(4) Every statement from any caller goes through `DrcStore().record_stated_book(day, kind, positions, via=…, now=…)` (`src/cobalt/drc/store.py:529`). It refuses inside `market_reset` itself (`[F-01]`, `:547`). It refuses an `opening` for D while D's prior trading day is recorded — D starts from that close (v3 §2b, §2c; R51 "the close wins"); `preview_stated_book` (`src/cobalt/drc/store.py:507`) refuses the same, so the page offers `state your opening book` only when `seed_for` returned `None` or failed on a prior day that is not recorded. [H2, fix r1] The page passes `via="drc_page"`; the widget (K4) passes `via="voice_widget"` with `turn_id` + `readback_sha256`.
(5) `pair_day` (`src/cobalt/drc/pairing.py:231`) is the FIFO engine and holds no book policy: a route never calls it directly.
(6) D3's `cobalt drc build` joins K1's `drc` parser group in `src/cobalt/drc/cli.py` (`add_parser`, `:150`) — never a second `drc` group (L3).
(7) A stated position's `opened_on` is `None` (not stated); a page renders it `opened: not stated`, never a date. [H1, fix r1; the field `src/cobalt/drc/models.py:134`; `None` for a stated position at `src/cobalt/drc/pairing.py:122`; carried by `_seeded` (`:217`) into `pair_day`'s open position (`:302`); pinned by `tests/cobalt/test_drc_k1.py:136`, `:174`, `:182` and `tests/cobalt/test_drc_k1_store.py:444`]"

## FOR K2
`39`'s `## FOR K2` stands, amended by these lines:
- `OpenPosition.opened_on` is `Optional[date]`: `None` for a stated position and for every day it is carried after (H1; `src/cobalt/drc/models.py:134`, `src/cobalt/drc/pairing.py:122`, `:217`, `:302`). K2's R51 comparison of a stated book with a recorded close compares symbol / direction / shares, never `opened_on`.
- `record_stated_book` refuses an `opening` for D while D's prior trading day is recorded (H2; the refusal `src/cobalt/drc/store.py:496-504` in `_reason`, reached from `preview_stated_book` `:523` and `record_stated_book` `:559`; pinned by `tests/cobalt/test_drc_k1_store.py:312`). `seed_for` case (iv) is therefore reached ONLY in R51's order — D stated first, its prior recorded after — which is exactly the case K2's rebuild replaces. K2's rebuild, when it records P under a stated later day, does not call `record_stated_book` (the statement stays as history, R51).
- The route records an unpaired day (H3; `src/cobalt/drc/store.py:212-217` refuses only a COMPUTED day without a book, `:272` writes `seed` only with one, `:285` writes `book_close` only for a computed day; pinned by `tests/cobalt/test_drc_k1_store.py:567`): a `day` row with `not_computed.pairing`, no `seed`, no `book_close`. K2's forward re-pair and its empty-day record meet such rows; K2 states what a re-pair does with one.
- Carried from `40` ESCALATE 4 (OUT OF SCOPE → K2): two current `resolve` rows for one `trade_id` on DIFFERENT days are both stored (`store.py:547-549` at `9a0fc900`, `:562-564` at `40cf173e`, filters on `day`); v3 `[F-01]` / §4 "FAIL naming both ids" is a reader's failure on the import path — K2's `[F-06]` reader, which replaces `seed_for`'s stored-resolve raise, carries it. The build's ESCALATE 6 (the `day <= D` bound of that raise) is K2's too.
- H2's refusal asks the calendar only when an earlier `day` row exists (run 2, `40cf173e`; `src/cobalt/drc/store.py:488-493` the `earlier` query and `first import`, `:495` `prior_trading_day`): a `first import` statement never reads `prior_trading_day`, as at the base.
- RUN-1's quoted result (a stated trade against a stats log): GREEN on `ae4388df` and `40cf173e` — no exception; the stated `GGG` trade carries no `stats`; the stats row is `unmatched` with reason `unmatched — 0 trades match` (a stated trade has `entry_time = None`, so the exact match at `pairing.py:370` never hits it). K2 / K3 inherit that a stated trade's stats row is always unmatched until a rule for it is ruled.

## CONTINUE
Run 1 FAILED at D8 (21:17:29 ET). Run 2 resumed at 21:19:50 ET on R91, applied D4's H2 reorder (`40cf173e`) and re-ran D4's proofs and D5–D8. Closed 21:24:17 ET. Nothing left: next is `49`, not this seat.

## ESCALATE
1. R22 scope: read as the drc-d1 pair for this worktree (desk reading, R61 / R65 (1)).
2. D4 REORDER RULE applied to zero tests: `test_seed_iv_…` (`test_drc_k1_store.py:394-399` at the base) was the only setup in the refused order, reordered at D3 as the prompt named; no other with-DB test states an `opening` after recording its prior (read list under D4). No `H2: <test> asserts the refused order` case exists.
3. H3 pin and the reordered case (iv) were GREEN on the base at D3 (as the prompt expected) — no `H3: the unpaired-day pin is red on the base` escalate.
4. RUN-1 GREEN on `ae4388df` (`1 passed`): no strict `xfail` added; the round adds no mark.
5. D0 used `grep -rln "requires_vault" tests` (`-l`, the file list) where the prompt wrote `grep -rn`; same prefix, same five files, recorded for exactness.
6. D8 RUN 1 RED, FIXED IN RUN 2 (this branch, not a DEV-DB SEAM): 13 × `CalendarError: no NYSE calendar for 2001 (asked about 2001-01-01)`. H2's `_reason` computes `prior_trading_day(day)` before knowing that any earlier `day` row exists. FIX (one reorder, same file, same block): query `earlier` first, and call the calendar only when it hits. D3 missed it: its new tests all load `weekday_calendar`, and the pre-existing ones that don't were not in D4's offline proof, because they skip without a DB.
7. L76: after run 1, the `0016` / `0018` absence was not proven, because (c2) runs on green only. The desk read `cobalt_dev` at 21:19 through `pg_catalog.pg_tables`, read-only (R91), and found no `drc_*` table. Run 2's probe then proved it: `28 == 32`, the four `drc_*` tables absent.
10. Run 2 was resumed by the desk's cross-session message (R91, try 2 of 3), with the same launch line and context kept. For the resume, the tip changed from `67a4624b` to `40cf173e`. The `## SEAM FOR D2` citations were re-read on `40cf173e` (store lines +3). While run 2 ran, the last line stayed the run-1 FAILED line instead of the in-progress pin, so the desk's change-watch could not fire early.
8. **OWNER ITEM carried, not built (the residue of H1): whether his opening-book statement also takes each swing's open day. Until he rules, a stated position's `opened_on` is `None` — not stated, never a date known false (L1). His ruling is on the drafter's `## OWNER ITEMS`.** (Desk row R90 records his R80 "B" — "not stated" is enough; `None` as written.)
9. **The FIX rows moved on file evidence only (`40` rows 1–3 HOLD). The red: D2 offline on `d158a8a3`, D3 with-DB on its successor `0009e9c1`; the named reds are green on `ae4388df` offline, but the full with-DB suite is red on `67a4624b` (ESCALATE 6), run 1 was red on `67a4624b` (ESCALATE 6); run 2 is green on all three suites at `40cf173e`. The check is `49` (round 2; Opus 5.5 + Grok, with Sol from Sep 26th, 2026 6:47 AM), and its packet carries this report's executed output of all three suites and RUN-1 (L68). Astra's read of the K1 NEW BUILD is still owed from its meter return (`40` ESCALATE 11, the desk's seat). The deploy's L68 gate re-proves them on the tree that ships.**

DRC K1 FIX R1 BUILT 40cf173e | on 9a0fc900 | red d158a8a3 | offline 2441/0 | with-DB 2848/0 | live-note 142/0 | .env: removed | 0018: rolled back | FIX: 3 | RUNS: 1 | ESCALATE: 10
