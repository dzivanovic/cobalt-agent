BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Thu Sep 24 08:44:53 EDT 2026

## DIGEST FOR THE DESK

Closing line: `TRIBUNAL R1: BUILD AFTER re-pair triggers on every earlier-day record; stated-position model fields made Optional`

| Item | Verdict | Gist (ADOPT WITH / REJECT) |
|---|---|---|
| Q1 | ADOPT | — |
| Q2 | ADOPT WITH | always a new numbered file; never re-open checked `0016`; with (c) it only creates `drc_stated_books` |
| Q3 | ADOPT WITH | trigger on ANY earlier-day record, not only supersede; stats rows not in `drc_fills`; one DB transaction spanning days |
| Q4 | ADOPT WITH | a stated position has no entry time either; name the Optional fields and the trade_id shape |
| Q5 | ADOPT WITH | the no-trade DRC needs a stored input row: `drc_stated_books` kind `no_trade` |
| Q6 | ADOPT WITH | resolve cannot go through `_trade` (`exits[-1]`); an export-superseded resolve applies nothing |
| Q7 | ADOPT | — |
| Q8 | ADOPT | — |
| Q9 | ADOPT | — |
| Q10 | ADOPT WITH | K1 can land alone (no caller today); D2+D3 need K1+K2 plus a statement caller |
| Q11 | ADOPT WITH | A31's open-positions line renders from the same rows in the same build call |
| (a) | ADOPT WITH | B1–B10 hold; three misses: stats rows, out-of-order record, `carried_from` = opened_on |
| (b) | ADOPT WITH | C confirmed not fail-loud; one assume path left: an earlier day recorded after a later stated day |
| (c) | ADOPT WITH | book hash + seed go on the existing `day` row; the link key is not named `carried_from` |
| (d) | ADOPT WITH | the statement uses voice FINAL §2.6 (a DB ACT), not L28's vault clause; market_reset refusal in the store |
| (e) | ADOPT WITH | the dependency runs one way: D2+D3 need K1+K2; K1 alone is a no-op |
| (f) | ADOPT | — |

Experiments named: X1 re-pair all-or-nothing · X2 re-pair idempotence from stored rows · X3 note re-upsert after DB commit · X4 Sync revert of the unit vs the DB hash · X5 a stated no-cost, no-time position through `pair_day` · X6 a header-only export on a no-trade day · X7 an earlier day recorded after a later stated day · X8 a resolve with no exit price · X9 market_reset refusal of the widget caller.
Owner items: none.
WITHDRAWN sentences: 0.
ESCALATE: 1.

## Rulings

**Q1: ADOPT.**
The table must be separate. `record_day` deletes every `drc_rows` row of the day before it inserts (`store.py:201-203`), so a statement stored as a `drc_rows` kind would be deleted the next time that day is re-recorded. Example: he states the opening book for day D (a `drc_rows` row). D is re-imported at 17:00, the DELETE runs, and his statement is gone. The next build then reads D as `not computed — opening book not stated` again. The append-only trigger exists: `"user".refuse_row_update()` at `0007_radar_cards.sql:105-113`, attached at `:190` and `:199`.

**Q2: ADOPT WITH** "The lane's migration is always a NEW numbered `db_migrations` file with its `.rollback.sql`. The number is the desk's at the L68 gate. `0016` is never edited after D1's check. The file creates `"user".drc_stated_books` (kind CHECK `opening`, `resolve`, `no_trade`) and its append-only trigger. It does not change `drc_rows` (see (c))."
Reasoning. The proposal's conditional ("fold into 0016 only if D1 is unmerged at K1's cut") leaves two possible shapes. It also changes a migration that D1's check has already passed, and a changed migration means D1's check has to run again. Proven numbering: 0016 is D1's (`d583f6fd`). 0017 is `voice_turns` (`69c376bd`, from `git log --all -- src/cobalt/db_migrations`). Main ends at 0011 (`git log main -- src/cobalt/db_migrations` → `d4e2fdc2` 0010/0011 is the last). So the proposal's "≥ 0018" holds as of today; its UNPROVEN row 2 is now proven.

**Q3: ADOPT WITH** "FORWARD RE-PAIR. (1) Trigger: every time the store records day P and a LATER day is already recorded. This covers a superseding file for P AND a first file for P recorded after a later day (a later day recorded first is lawful today: `test_drc_pairing.py:350-351`). The later day N whose prior trading day is P is re-paired from P's carried book, and so is every recorded day after N, in date order. If N's seed was STATED, the carried book replaces it (DAS is the truth, R67): the stated row stays in `drc_stated_books` as history, and the page shows `stated book for <N> differed from <P>'s close: <trade_ids>`. (2) Inputs of each re-paired day: its executions from `drc_fills` of the import ids its own `day` row names (`store.py:190`). Its stats rows come from its own stored `stats_row` rows (`derived.row`, `store.py:170-186`) and its `not_computed.match` (`store.py:195`), read before the delete, because `drc_fills` holds no stats-log rows. (3) All-or-nothing covers `drc_rows` only: P and every re-paired day are written in ONE DB transaction by one new store method (today `record_day` commits per call, `store.py:198-212`). The superseding file's `drc_imports` / `drc_fills` rows are committed by `record_import` before pairing (`store.py:85-150`) and stay. On failure the page shows `<P>: file <name> stored, not applied — <day>: <reason>`. P's `day` row keeps naming the import ids its rows came from. (4) Note re-upserts run after the DB commit, one per day, through the one build. A failed note write leaves that day's event `failed` (v2 `[F-08]`) and the page names it."
Reasoning. Failing scenario for the proposal's trigger ("when a superseding file for day P is recorded", `:104`):
- He imports Tue first ever and states `flat`.
- Wed imports and seeds from Tue.
- Then he drops Mon for the first time. `check_contiguity(Mon, …, [Tue, Wed])` passes because `earlier` is empty (`pairing.py:249-250`), and Mon states a book and leaves a short of 40 open.
- Mon's file does not supersede anything, so no re-pair runs.
- Tue stays paired from `flat`. Tue's `B 40` cover has been read as a new long 40 that carries into Wed: a phantom, with Mon's stored close contradicting it.

Failing scenario for "from its stored drc_fills": `match_stats` (`pairing.py:260-316`) needs a `ParsedStatsLog`. `drc_fills` has trading-log columns only (`0016_drc.sql:52-71`), and the stats rows exist only in the day's `drc_rows` (`store.py:170-186`), which the DELETE removes (`:201-203`).

Cost: one store method plus the read-before-delete, inside K2. Estimate +1 h, UNVERIFIED (the seat's estimate).

**Q4: ADOPT WITH** "A STATED position becomes an `OpenPosition` with `trade_id = <symbol>-<direction>-stated-<drc_stated_books.id>`, `entry_time = null`, `opened_on = null` (rendered `opened before <day> — stated`) and one lot `{time: null, price: avg_cost|null, shares}`. K1 makes these fields Optional for this source only: `Lot.time`, `Lot.price`, `OpenPosition.entry_time` / `opened_on`, `Trade.entry_time`, `Trade.hold_seconds`, `Trade.gross_pnl`. A validator refuses `None` on any lot built from an execution. On a day where `_reduce` consumes a price-less lot, that trade's realized figure is `not computed — carried cost not stated`. The trade sort orders a null `entry_time` first. `match_stats` never matches a null `entry_time`. Allowed: yes, never guessed (L57)."
Reasoning. The proposal's `positions` shape `{symbol, direction, shares, avg_cost|null}` (`:89`) has no entry time, so the question is wider than cost. Today these fields are required: `Lot.price` and `Lot.time` (`models.py:97-98`), `OpenPosition.entry_time` (`:110`), `Trade.gross_pnl` (`:164`). `trade_id()` calls `entry_time.isoformat()` (`pairing.py:69`), `_trade` subtracts `entry_time` (`:105`), and the sort keys on it (`:235`). Failing scenario: he states "short 40, no cost". `OpenPosition.model_validate` rejects the missing `entry_time`, so the first import crashes. That is loud, but the lane can never pair a stated day. Cost: models.py + pairing.py inside K1, estimate +1 h, UNVERIFIED. Proof: X5.

**Q5: ADOPT WITH** "The no-trade DRC (R93) is the only event that records a day with no executions. Its INPUT is one `drc_stated_books` row, `kind = 'no_trade'`, `positions = []`, `reason = 'no-trade DRC'`, written by `record_stated_book` when he records the no-trade DRC on `/drc` (his why stays his text in the note). `record_day` for a day with no trading-log import is refused unless that row exists, and the `day` row's inputs name its id. A trading day with neither an import nor that row is a broken chain."
Reasoning. The proposal's empty day (`:60`) writes a `day` row whose inputs are `{"import_ids": {}}` (`store.py:190`). Nothing stored separates "he recorded a no-trade DRC" from "a build ran with no files". Failing scenario:
- Mon leaves a swing open.
- On Tue he traded, but has not dropped the file yet.
- A `cobalt drc build --date Tue` run with no files, or a caller bug, records an empty Tue. The chain is now "closed", and Wed seeds from a Tue that never happened.

Cost: one CHECK value on the new table. X6 checks whether a header-only export can also serve as this input.

**Q6: ADOPT WITH** "RESOLVE writes a `drc_stated_books` `resolve` row whose `day` is the DRC day he resolves on. It removes that `trade_id` from that day's seed before the day's executions are paired, and the day is re-recorded (with forward re-pair, Q3). The resolved trade is emitted as one CLOSED `Trade` with `legs = []`, `exit_time = exit_time|null`, `avg_exit = exit_price|null`. Realized is computed FIFO over the carried lots only when an exit price is given, else `not computed — exit not in any export`. It is not built through `_trade` (`pairing.py:97` reads `exits[-1]`). A resolve whose `trade_id` is absent from the seed after a re-pair applies nothing and is shown `superseded by export <file>`. If the day's file later sells that symbol with no position, it FAILs as today (`pairing.py:194-198`)."
Reasoning. R90 holds: his choice is recorded and never silently closed ("If export has opened, leave it opened, and give me way to resolve in DRC"). Failing scenarios for the proposal as written:
- A resolve with no exit price reaches `_trade(book, CLOSED)` with `book.exits == []`, which is an IndexError at `pairing.py:97`.
- Mon's re-export later carries the close, and the forward re-pair removes the trade from Wed's seed. Wed's resolve row then names a `trade_id` that is not in the book, and nothing says what happens to it.

**Q7: ADOPT.** A swing is lawful (R67). An aging threshold would be his value (L53), and he has named none. `day <k>` and `last execution` show the age without inventing one.

**Q8: ADOPT.** R22 asks that the night before informs the next day. The note unit (evening) and the `/drc` morning line do that. The 09:00 reader reads the prior DRC note's fields (`daymode/drc.py:85-165`) and needs no change for this lane.

**Q9: ADOPT.** FAIL naming the day, then `rebuild <day>`, is the one path, and the migration computes nothing. Production holds no such days: `drc` exists on no main path (`grep -rn seed_for /Users/cobalt/cobalt/src/cobalt` → none), and nothing calls `record_day` / `seed_for` even on D1 (every hit is a definition). The case exists only on `cobalt_dev`. The rebuild uses Q3's inputs (executions plus the stored stats rows).

**Q10: ADOPT WITH** "K1 may land in any deploy on its own. It is a library with no production caller. D2 and D3 are never deployed without K1 and K2 and at least one caller of `record_stated_book`: K3's form, or the `cobalt drc state-book` CLI (+0.5 h to K1, the same store function, L3). K3 lands in the same deploy as D2 + D3 when it is checked in time (L43). Otherwise the CLI stands in."
Reasoning. The proof is in (e). K2 belongs in the set for this reason: R93 means a DRC every trading day. Without K2 a no-trade day cannot be recorded, so the next day FAILs contiguity (`pairing.py:250-254`) and needs a restatement every time. That is loud, but it is a daily manual step.

**Q11: ADOPT WITH** "The `drc-trades/open_positions` unit leaves D5 for K3, built by the one DRC build (v2 D3 `build.py`). D5 keeps the reconcile unit only. The A31 `open items carried forward` line for open positions (v2 `:295`) renders from the same stored rows in the same build call. No second computation."
Reasoning. The unit needs `drc_rows` only, while D5 waits on S3 C2 (v2 `:181`). v2's A31 row also lists open positions, so without this wording D3 could compute them a second time (L3).

**(a) THE FACT BASE: ADOPT WITH** "§1 add: (vi) the stats-log rows are stored only in `drc_rows` `stats_row` rows (`store.py:170-186`), not in `drc_fills` (`0016_drc.sql:52-71`); (vii) a day recorded after a LATER day passes contiguity as a first import (`pairing.py:249`, pinned `test_drc_pairing.py:350-351`); (viii) the built `carried_from` holds the trade's OPEN day, not the prior book's day (`pairing.py:149`, `:231`; `test_drc_pairing.py:233`)."
Checked, every one HOLDS:
- B1 `pairing.py:220-234`
- B2 `store.py:177-179`, `0016:80-95`
- B3 `store.py:220-250`, `pairing.py:143-159`, `:162-174`, `models.py:165`, `:102-112`
- B4 `:194-198`, `:203-218`
- B5 `:239-254` (`:248` "the very first import has no history and passes"), `store.py:235`
- B6 `:236-244`
- B7 `propose.py:300-308`, `store.py:223-225`
- B8 `pairing.py:26-28`, `:189-193`, test `:265-272`
- B9 v2 `:141`, `:179`, `:181`
- B10 `pairing.py:244-245`, `:6`
- The gap list (i)–(v) holds.
- Readers and writers of `open_position`: `record_day` writes it (`store.py:179`), `seed_for` is the only reader (`:246-248`), and nothing else, main included.
- No path re-pairs a later day. No path records a no-trade day.
- Missed writer, relevant to K3: production's `prefill/drc.py:443` writes the `drc-trades/tickers` unit today (D3 retires it).

**(b) L1 — NO ASSUMED BOOK: ADOPT WITH** Q3 (1) as the fix for the one assume path found.
- Option C is confirmed not fail-loud. Walk: first import Mon, file `B 40` at 09:40 (a cover). C reads it as a long 40, open at file end (pinned `test_drc_pairing.py:265-272`). Tue's file never touches the symbol, so the long carries every day, flagged only on Mon.
- Under A:
  - A first-import cover waits for his statement.
  - A no-trade Tue between Mon and Wed carries the book through its `no_trade` row (Q5).
  - A skipped trading day FAILs Wed (`pairing.py:250-254`).
  - A position closed outside every export shows `continuing open position` daily until RESOLVE (R90).
- Remaining assume path: an earlier day recorded after a later stated day (the Q3 scenario). The later day keeps a book that the carry contradicts, and nothing re-checks it.
- The §4 rows hold as fail-loud.

**(c) L57 — REPLAY: ADOPT WITH** "The book close and the seed live on the day's EXISTING `day` row (`store.py:187-197`, unique per day `0016:95`). No `book_close` or `seed` kinds, and no `drc_rows.kind` CHECK change. `derived` gains `book_sha256` (sha256 of the canonical JSON of the day's `open_position` rows' `derived`, sorted by `ref`) and `trade_ids`, beside the `open_positions` count it already stores. `inputs` gains `seed = {source: carried | stated | no_trade_carry, from_day, from_book_sha256, stated_book_id}`. The per-trade replay key is `inputs.seed_link = {day, trade_id, from_book_sha256}`, NOT `carried_from`, which already means the open day in `derived` (`pairing.py:149`). A day whose `seed.from_book_sha256` differs from its prior day's current `book_sha256` is STALE: shown loud and re-paired forward (Q3). `day <k>` and the held-lot average cost are stored in each `open_position` row's `derived` by `record_day`, not computed at render (§2a's own sentence, `:45`)."
Reasoning. The `day` row already holds, on every recorded day, the open-position count, which is the "flat is a stored fact" the proposal wants (`store.py:193`). It is also the row `seed_for` already reads (`:227-244`). Putting the book there is smaller: two fewer kinds, no CHECK change, and the morning read is one row instead of three. The link survives delete-and-replace because it is keyed by `(day, kind, ref)` plus the hash, never by id. After a re-record of P, a stale later day is detected by the hash, and that detection is the hash's real job. The self-hash check (`:52`, over rows written in the same transaction) can fail only on a bug. What is stored: the stated cost and the resolve exit, both in `drc_stated_books`. What is not: a replaced day's previous derived values. That was already true before this lane (`store.py:201-203`), and its inputs stay.

**(d) L28 / L40 — THE UNIT AND THE STATEMENT: ADOPT WITH** "The statement is a DB input, not a vault edit. L28's 2026-09-23 voice clause (LAWS.md:166 — a vault field span) does not apply. The widget caller follows the voice FINAL §2.6 ACT shape (`VOICE-v3-FINAL-2026-09-23.md:88`): the owning expert's dry-run (`DrcStore.record_stated_book`, dry-run), its `diff_sha256`, a read-back, his confirm, then the same store function. `record_stated_book` itself refuses inside `market_reset` for every caller. A note edit of the unit never changes the book. Its lasting fix is RESOLVE or a restatement (voice FINAL `:142`)."
Reasoning. One writer per side effect holds: `DrcStore` writes `drc_stated_books` and `drc_rows`, and the one build writes the unit through `upsert_unit` (`writer.py:644`, refusing an absent note at `:672`), after `create_if_absent` (`:559`). Failing scenario for the proposal's §4 last row: at 20:15 ET he tells the widget "I started Monday flat" and confirms. The vault gate is vault-only (main `writer.py:401`, "F1 GUARDS THE VAULT, NOT THE REPO"), and v2 `:79`'s refusal sits in the upload route. So the DB row is written, and the build's note write is then refused, leaving the note stale until 21:00.

**(e) THE LANDING SET: ADOPT WITH** "K1 is not held for D2 / D3, and D2 / D3 are held for K1 + K2 (Q10)."
Reasoning. No production path can call `seed_for`, `record_day` or `record_import` today:
- On the D1 tree every hit is a definition (`store.py:70`, `:153`, `:220`).
- Main has no `drc` package (`grep -rn seed_for /Users/cobalt/cobalt/src/cobalt` → none).

The callers arrive with D2 (`drc/imports.py`, `aset/web.py`) and D3 (`build.py`) (v2 `:176-177`). So the dependency is one-way: D2+D3 → K1+K2. What Q10's CLI adds: a caller when K3 misses the deploy, so that the first import is never stuck.

**(f) EXPERIMENTS FIRST: ADOPT.** The all-or-nothing re-pair across the DB and the note, the Sync revert of the unit against the DB hash, and the other runnable claims are X1–X9 below. None is argued here.

## Self-attack

GREP LIST (`/Users/cobalt/cobalt-wt/drc-d1/src/cobalt`, plus main where named). Writers and readers found:
- `seed_for`: defined at `store.py:220`, no caller in either tree.
- `record_day`: defined at `store.py:153`, no caller.
- `record_import`: defined at `store.py:70`, no caller.
- `check_contiguity`: defined at `pairing.py:239`, called only at `store.py:235`.
- `pair_day`: defined at `pairing.py:162`, called only by `build_day`, `:337`.
- `_seeded`: `pairing.py:143`, called at `:173`.
- `prior_trading_day`: `propose.py:300`, called by `store.py:225`, `propose.py:380`, `daymode/drc.py:152`.
- `carried_from`: `models.py:168`, `pairing.py:82`, `:113`, `:149` (= `position.opened_on`), `:231`. Main: none.
- `open_position(s)`: written at `store.py:179`, read at `:246-248`, count at `:193`, model `:260`, CHECK `0016:86`. Main: none (`replay/cards.py:110` is an unrelated rule name).
- `OpenPosition`: `models.py:102`, `pairing.py:143`, `:165`, `:224`, `:322`, `store.py:220`, `:250`.
- `FN_VERSION`: `pairing.py:64`, written at `store.py:210`.
- `refuse_row_update`: `0007_radar_cards.sql:105-113`, `:190`, `:199`, rollback `:32`, on both trees.
- `drc_rows`: `store.py:202` (DELETE), `:207` (INSERT), `:230`, `:237`, `:246` (reads), `0016:80-95`, `placement.py:94`. Main `placement.py:111` (declared only).
- `drc_fills` and `drc_imports`: `store.py` only on D1. Main: none.
- `create_if_absent`: `writer.py:559`, `prefill/drc.py:427`.
- `upsert_unit`: `writer.py:644`.
- `market_reset`: main `writer.py:36`, `:388`, `:401`, `aset/web.py:950`.
- no-trade: `pairing.py:246`, `:252`, `radar/seam.py:21`, `aset/web.py:311`.
- Lane names (`book_close` …): none on either tree.

Walked against the list:
- Q3's "no caller" and (e)'s "no production path" hold (no call site of `seed_for` / `record_day` / `record_import`).
- (c)'s claim that `seed_for` already reads the `day` row holds (`store.py:230-240`).
- Q4's field list holds against `models.py:97-98`, `:110`, `:164` and `pairing.py:69`, `:105`, `:235`.
- Q6's IndexError path holds (`pairing.py:97`).
- (d)'s vault-only gate holds (main `writer.py:401`).

WITHDRAWN: none. Every sentence above was checked against the list, and none was contradicted.

## Experiments (L70)

The proposal's read-back proofs (1)–(6) (`:116`) are KEPT. Added:
- X1: On `cobalt_dev`, record Mon (a long 40 left open), Tue (untouched) and Wed (`S 40`). Re-import Mon with a file that closes the long. Pass: the Wed re-pair FAILs (sell with no long), and the Mon–Wed `drc_rows` are unchanged byte for byte, while Mon's new `drc_imports` row exists and the page names Wed. Fail: any day partially replaced, meaning Q3 (3)'s one-transaction method is not what was built.
- X2: Re-pair an unchanged later day from its `drc_fills` and its stored `stats_row` rows. Pass: identical `derived` and `inputs`. Fail: the stats rows are sourced from the kept file bytes under `_imports/drc/<date>/` (D2), and K2 gains a D2 dependency.
- X3: On the dev vault, re-pair two days with the second note write refused (a simulated `market_reset`). Pass: DB rebuilt, day-2 event `failed`, page names it, and a re-run after 21:00 makes the unit current. Fail: Q3 (4) needs a stale marker in the DB.
- X4: On the dev vault, write the unit v1 then v2, and put v1's bytes back as a Sync revert. Pass: the next build records `sync_revert_of` and writes current text, and the day row's `book_sha256` is unchanged (it never reads note bytes). Fail: the build reads the unit, and that reverse parse is removed.
- X5: Run `pair_day` with a stated position (short 40, cost and entry time null) and a day file `B 40`. Pass: CLOSED, realized `not computed — carried cost not stated`, no TypeError at `pairing.py:69`, `:105`, `:235`. Fail: Q4's Optional set is incomplete.
- X6: His real export for a no-trade day (the E1 shape). Pass: a header-only file parses to 0 executions, `parsed`, so it may also serve as the no-trade input. Fail: the `no_trade` row is the only input.
- X7: Record Wed stated `flat`, then Tue (first file) leaving a short 40 open. Pass: Wed is re-paired from Tue's book (the cover closes the short), and the page shows the stated-vs-carried difference. Fail: Q3 (1) is not built.
- X8: A resolve with no exit price on a carried trade. Pass: the trade is CLOSED with `legs = []` and realized `not computed — exit not in any export`, with no IndexError at `pairing.py:97`.
- X9: `record_stated_book` called by the widget's tool at 20:15 ET on `cobalt_dev` with a constructed clock. Pass: refused with the reason, no row.

## OWNER (after the tribunal)

none — every question here is a design question the houses settle (L67 as amended 2026-09-24). R67 already rules that DAS wins over a stated book (Q3 (1)).

## WRONG FACTS

1. Proposal `:104`, "re-pairs every later recorded day … from its stored `drc_fills` (the inputs are all kept, `store.py:13-17`)". `drc_fills` has trading-log columns only (`0016_drc.sql:52-71`, `store.py:119-144`). The stats rows are only in `drc_rows` (`store.py:170-186`), which `record_day` deletes (`:201-203`), and `match_stats` needs them (`pairing.py:260-316`).
2. Proposal `:43`, the unit's "`carried_from` (the day whose book it came from…)". The built `carried_from` is the trade's open day: `_seeded` sets it to `position.opened_on` (`pairing.py:149`), and that persists through `:231`. The test asserts it equals the open day (`test_drc_pairing.py:233`). For a trade carried more than one day these are different days.
3. Proposal `:104`, "nothing is replaced". `record_import` commits the superseding file in its own transaction before any pairing (`store.py:85-150`), and it becomes the day's newest file (`:88-97`). Only `drc_rows` can be all-or-nothing.
4. Proposal `:30` (iv), "hits only those two docstring lines and an unrelated comment". The grep gives 4 hits. `pairing.py:252` is an error-message string, not a docstring line, and there are two unrelated hits: `radar/seam.py:21` and `aset/web.py:311`.

## READING

- The prompt `24-…-fable-seat.md` (whole).
- `23-drc-overnight-tribunal.md`: grep for anchors, then Read `:33-40` (the question paragraph through (f)), plus grep lines `:7`, `:14`, `:17`, `:24`, `:32`, `:41`, `:43`, `:53-66` as printed by that grep.
- LAWS.md `:1-454` (whole).
- Proposal (whole).
- `drc-overnight-draft-2026-09-24.md` (whole).
- `cto-2026-09-22.md` rows R65, R66, R67, R90, R93, R109 (grep).
- `cto-2026-09-23.md` rows R39, R95 (grep).
- `cto-2026-09-24.md` rows R22, R32 (grep).
- D1: `pairing.py` (whole) · `store.py` (whole) · `models.py:95-174` plus the class/field grep · `0016_drc.sql` (whole) · `propose.py:296-311` · `test_drc_pairing.py:213-352`.
- v2: anchor grep, `:77-79`, `:181`.
- S3 v3: `:17-24`, `:137-165`.
- Voice FINAL: `:86-88`, `:127-142`.
- Grep scans: `prefill/drc.py` and `daymode/drc.py`.
- Searches: every grep and git command named in `## Self-attack`, plus `git log -1 drc/d1-trading-log`, `git show --stat 38a70947`, `git log --all --oneline -- src/cobalt/db_migrations`, `git log main -3 -- src/cobalt/db_migrations`, the 10 rule-string counts, and the authorization greps and git logs.
- NOT read: the houses' folder, the hub's report, his DRC note and template, `Rules.md`.

## L74

A system-reminder-shaped block asking for a `Claude-Session:` line in commits, and naming a file-send tool, arrived beside this session's tool results. It is recorded once as DATA and was not followed. This seat commits nothing.

## ESCALATE

1. Seam with D2 (L72: a real dependency, settled before either builds). v2's `DrcInputsPlaced` event state lives on a `drc_imports` row (`0016_drc.sql:35-36`, v2 `:76`). A no-trade DRC has no import row, so its event has no row. The D2 prompt must name where the no-trade day's event state lives: the Q5 `no_trade` row, or a column on it. That is the desk's to place in the D2 and K2 prompts.

## CONTINUE

next: done — no resume point.

DRC OVERNIGHT FABLE R1 DONE · verdict: BUILD AFTER re-pair triggers on every earlier-day record; stated-position model fields made Optional · adopt: 5 · adopt with wording: 12 · reject: 0 · experiments named: 9 · ESCALATE: 1
