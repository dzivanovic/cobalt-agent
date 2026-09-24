# DRC — the overnight-position lane (PROPOSAL, 2026-09-24)

ONE-house proposal under L67 (Opus 5.5, seat `drc-overnight-draft-0924`). Ladder `S3-P3 · F14`. Input to the tribunal (Fable · Astra · Grok; Gemini optional fourth). Nothing here is built or ruled. No ticker, price, share count or P&L of his appears in this file (L32). Every claim about built code is `file:line` at branch `drc/d1-trading-log`, code tip `d1342595` (branch tip `38a70947` adds only the fix-r1 build report — `git show --stat 38a70947`: 1 file, docs).

## 0. What he asked

His words (`cto-2026-09-24.md` R22, 07:56 ET, verbatim): "approved. A for now. We need to design the lane in which last nights DRC informs the next day that there is swing position. You will know night before that position is left open and this is already improted".

Reading, one sentence: the evening DRC import already knows which positions were left open, states them in the DRC note and in stored rows, and the next trading day's import starts from exactly those positions — never from an assumed flat book — with O1 = A ("first import taken as flat") retired by a stated opening book wherever no prior DRC exists.

## 1. What v2 + D1 already do

| # | Item | Where (design) | Where (built) | Status |
|---|---|---|---|---|
| B1 | A symbol not at 0 at file end is an OPEN trade with its held shares, not a failure | v2 `DRC-AUTOMATION-v2-2026-09-22.md:81` (R67, F33) | `pairing.py:220-234` (every book left at file end → `TradeStatus.OPEN` + an `OpenPosition`) | DESIGNED + BUILT |
| B2 | The open position is stored in `drc_rows` as the next day's seed, with its inputs (L57) | v2 `:81`, `:94` | `store.py:177-179` (`kind = 'open_position'`, inputs = its trade's inputs); `0016_drc.sql:80-95` (`drc_rows`, unique `(user_id, day, kind, ref)`) | DESIGNED + BUILT |
| B3 | Next-day pairing seeds each symbol from the prior day's open positions, keeps ONE `trade_id`, realizes P&L only on that day's exits, `unrealized: not computed` | v2 `:81` (`[F-10]`) | `store.py:220-250` (`seed_for`), `pairing.py:143-159` (`_seeded`: lots + `carried_from`), `:162-174`, `models.py:165` (`unrealized`), `models.py:102-112` (`OpenPosition`: `trade_id`, lots, `opened_on`, `day`) | DESIGNED + BUILT |
| B4 | "A carried position with no prior row = FAILED naming the symbol (never assumed flat)"; a file contradicting the seed FAILS | v2 `:94` | `pairing.py:194-198` (a sell with no long → `PairingError` naming the symbol, "never assumed flat"); `:203-218` (through-0 / wrong side "contradicts the seed") | DESIGNED + BUILT — for a leading `S` only (see G-c) |
| B5 | A broken chain FAILS: once any earlier day is recorded, the prior trading day must be recorded too | v2 `:81` (Fable scenario, carried to E1) | `pairing.py:239-254` (`check_contiguity`, the D1-3 safe default, "the very first import has no history and passes" `:248`); called at `store.py:235` | BUILT (a safe default, not a ruled design) |
| B6 | A prior day whose pairing was not computed FAILS the seed | — | `store.py:236-244` | BUILT (fix r1) |
| B7 | Weekends and holidays are skipped by the NYSE calendar, not by the chain | — | `daymode/propose.py:300-308` (`prior_trading_day`), used at `store.py:223-225` | BUILT |
| B8 | First import = flat (O1 = A "for now"): a leading `B` opens a long, a leading `SS` a short | fix r1 draft `## OWNER ITEMS` O1 (`drc-d1-fix-r1-draft-2026-09-24.md:69`); R22 | `pairing.py:26-28` (docstring), `:189-193`; pinned by `tests/cobalt/test_drc_pairing.py:265-272` | BUILT (ruled "for now") |
| B9 | The note unit `drc-trades/open_positions`: "symbol, side, held shares, trade_id, day opened; on the next day's DRC the same trade appears as `continuing open position` until closed" | v2 `:141`; assigned to D5 at v2 `:179` | — | DESIGNED, NOT BUILT (D5 waits on S3 C2, v2 `:181`) |
| B10 | E1 row: "whether a day-file starts flat or lists overnight positions"; UNPROVEN list: "flat start → E1" | v2 `:191`, `:207` | E1 result recorded in code: "E1 starts flat, so a seed has no cross-check" `pairing.py:244-245`; "E1: a cover is `B`" `pairing.py:6` | PROVEN by E1: the export starts flat and carries no overnight rows |

S3 (the clause relied on): v3 itself still prints R2-2 as `OPEN FOR DEJAN` (`S3-EXITS-v3-2026-09-22.md:22`, `:141`); the ruling is `cto-2026-09-22.md` R67 (row line 99), recorded as F33 in v2 (`:50`) and in `areas/cobalt-product-definition.md:61`. Quoted, his words: "…your scenario where I exit 50 shares … and at the end of the day … still have open 50 shares, does not exist right now, but it should be considered as this is still open position for the next day … appear as continuing position as 50 shares and keep going that way and just call it an open position." Desk reading (4): "a position still open at the DRC carries to the next day as an OPEN POSITION with its held shares, continuing until closed." And (3): "the DAS trading-log import RECONCILES — DAS is the truth". (The share figure is his hypothetical in the ruling, not a trade.)

**Already designed and built:** the carry itself — day D's open positions stored, day D+1 seeded from them, one `trade_id`, FIFO lots with their original prices, loud failure on a leading sell with no seed, on a seed contradiction, on a broken chain, on a prior day not computed (B1–B7).

**Not designed or not built:** (i) the night-before signal HE sees — the `open_positions` unit is designed but unbuilt and parked in D5 behind S3 C2 (B9); (ii) any stored record of WHICH book a day started from (the seed is read at `store.py:245-250` and not recorded with the day; a day's `carried_from` is a date only, `models.py:168`, `pairing.py:82`, `:231`); (iii) any way to state an opening book when no prior DRC exists — today that case is B8, flat; (iv) a no-trade day's record: `check_contiguity` names "an import or a no-trade record" (`pairing.py:246`, `:252`) but no code writes a no-trade record (`grep -rn "no-trade\|no_trade" src/cobalt` hits only those two docstring lines and an unrelated comment); (v) what happens to later days when an earlier day is re-imported (`store.py:201-203` deletes and replaces the day's rows; nothing re-checks a later day seeded from them).

## 2. The gap

### 2a. The NIGHT-BEFORE SIGNAL

The evening DRC states the book it leaves open in two places, written by the same build run from the same `DayPairing`:

**Stored rows (exists, extended).** The day's `open_position` rows (B2) plus ONE new `drc_rows` row `kind = 'book_close'`, `ref = 'book'`: `derived = {count, trade_ids[], book_sha256}` where `book_sha256` = sha256 of the canonical JSON of the day's `open_positions` (sorted by `trade_id`); `inputs = {trading_log_import_id, seed_ref}` (§3). This row is what the next morning checks against; it exists on every recorded day, `count = 0` included, so "flat" is a stored fact, never an absence.

**Note unit (designed, moved here).** `drc-trades/open_positions`, marker-bounded, stable id, upserted in place by the one DRC build function (L28, L40) — moved out of D5 (it needs `drc_rows`, not S3's legs). Fields, one block per open position plus a header line:

- header: `left open: <count>` · `book: <book_sha256 first 12>` · `next import starts from this book` — `left open: 0 — next import starts flat (stated by this DRC)` when the count is 0;
- per position: `trade_id` · symbol · direction · held shares · average cost of the held lots (from the stored lots; `not given` when a stated lot has no price, §2c) · `opened_on` · trading days held · `carried_from` (the day whose book it came from, or `stated <date>`) · status `new today` | `continuing open position` (v2 `:141`'s wording) · `last execution: <date>`.

No figure in the unit is computed outside the stored row (v2 `:117`, L57).

### 2b. The MORNING READ

At the next import for day D (drop on `/drc`, or `cobalt drc build`):

1. `seed_for(D)` resolves `P = prior_trading_day(D)` (B7) and the chain (B5).
2. It reads `P`'s `book_close` row and `P`'s `open_position` rows, recomputes `book_sha256` over the rows and compares it with the stored one. Mismatch → FAILED `seed for D: <P>'s stored book does not match its own close row` (L1). A missing `book_close` on a recorded `P` → FAILED naming `P` (rows built before this lane: see §7 Q9).
3. The day records what it started from: ONE `drc_rows` row `kind = 'seed'`, `ref = 'book'`: `inputs = {source: carried | stated | no_trade_carry, from_day: P, from_book_sha256, stated_book_id}`, `derived = {count, trade_ids[]}`. Every carried trade's inputs gain `carried_from = {day: P, trade_id, from_book_sha256}` — the replay key (L57), replacing the bare date.
4. Pairing runs with that seed (B3). The `/drc` page shows the morning line (§5) BEFORE the file is paired, so he sees what the import will assume.

Cases:

- **Gap day — weekend / holiday.** `prior_trading_day` skips it (B7); the Friday book seeds Monday. Nothing new.
- **Gap day — a trading day with no DRC.** R93 (`areas/cobalt-product-definition.md:63`): a DRC every market trading day, no-trade days carry his why. So a missing trading day is a broken chain → FAILED naming the missing day, with the remedy on the page (import that day, record its no-trade DRC, or state the book — §2c). The phantom-position scenario (v2 `:81`) is exactly this and stays loud.
- **A no-trade day with an open position.** The no-trade DRC is recorded by the same build with zero executions: `pair_day([], D, seed)` already returns the seed as D's open positions unchanged (`pairing.py:170-174`, `:220-234`); the day gets its `seed` row (`source: no_trade_carry`), its `book_close` row and the unit (`continuing open position`, `last execution` unchanged). This is new: no caller records an empty day today (§1 (iv)).
- **Partial overnight cover.** Seeded book reduced by the morning's exits, FIFO from the carried lots (`pairing.py:117-129`); realized P&L at the carried lot prices; the remainder is open at file end and carried again with the same `trade_id` (`pairing.py:220-234`). Built; this lane adds only the `seed` / `book_close` rows and the unit.
- **A carried position closed outside the export's window** (an execution after the export was cut, a broker action, an account transfer). Two sub-cases:
  - *the next file touches the symbol inconsistently* — a side contradicting the seed or a through-0 → FAILED "contradicts the seed" (`pairing.py:203-218`). Loud, built.
  - *the next file never touches it* — nothing can see it: the position is carried and shown `continuing open position` with `last execution: <date>` every evening. The remedy is his: (1) re-export the day that carries the missing execution and drop it — it supersedes that day's file (`store.py:88-97`, `:116`) and the lane re-pairs every later day forward (§3); or (2) when no export will ever carry it, the RESOLVE action on `/drc` (R90, `areas/cobalt-product-definition.md:62`: "give me way to resolve in DRC") records `closed outside the export` for that `trade_id` as a stated correction (§3 `drc_stated_books`), with an exit price only if he gives one — else realized P&L `not computed — exit not in any export`.
- **An earlier day re-imported after later days were built.** `record_day` replaces `P`'s rows (`store.py:201-203`), so `P`'s `book_sha256` can change under a day already seeded from it. The lane re-pairs forward (§3 "forward re-pair").

### 2c. The FIRST DAY / a broken chain

When there is no prior book to read — the first import ever (`pairing.py:248`) or a chain the page cannot close by importing the missing day — the opening book must come from somewhere. Today it is flat (B8), and the file cannot see a morning short cover: E1 books a cover as `B` (`pairing.py:6`), so a cover reads as a new long that stays open at file end (`test_drc_pairing.py:265-272`) — a silent phantom, exactly what L1 forbids once swings are real.

| Option | What happens on the first day / a broken chain | What it costs him | Residual risk |
|---|---|---|---|
| **A — Stated opening book** | The import stores the files (`drc_imports` / `drc_fills` as today) but pairing does not run: the day shows `not computed — opening book not stated`. `/drc` shows ONE line with two actions: `I started <D> flat` (one tap) or `list what I held` (per position: symbol, direction, shares, average cost optional). The same statement can be made in the voice / text widget: its read-back ("opening book for <D>: flat" / "<n> positions: …") and his confirm (09-23 R39 shape, L28 as amended 2026-09-23) call the same store function. Stored append-only in `drc_stated_books`; pairing then runs from it (`source: stated`). | One tap on the very first import; one tap (or a short list) after a broken chain he cannot close by importing. Nothing on ordinary days. | None silent: every opening book is either carried with a hash or his stated word. A stated position with no cost renders its realized P&L `not computed — carried cost not stated`. |
| **B — Explicit flat only** | As A, but the only statement accepted is `flat`. A day that did not start flat cannot be the first import; he starts the chain on a later flat day (or imports the earlier days). | One tap; cannot start or restart the chain on a day a swing is open. | None silent; a real swing at restart blocks the DRC until a flat day. |
| **C — Fail on evidence, flat otherwise** | Keep B8 (flat) and fail only when the file contradicts flat (a leading `S` — built, `pairing.py:194-198`); flag every position opened and still open on a first import `opened on a first import — check`. | Zero taps. | A cover read as a long is visible only as a flagged line he must notice; the next day seeds from it. Not fail-loud (L1). |

**RECOMMENDATION: A.** It is the only option with no silent path (L1: "a missing carried position is a loud FAILED, never a silent flat" — the index-card line), it costs one tap in the common case (flat), it keeps a real swing representable on a restart (B cannot), and it reuses two paths already ruled: the `/drc` RESOLVE action (R90) and the voice-ordered confirm (09-23 R39). Under A, B8's pin test changes from "a leading buy is a long" to "a first import without a stated book does not pair", and O1 = A retires — which is R22's own instruction ("the lane replaces assume flat"), not a new ruling.

## 3. Data model and write paths

**New table (append-only input): `"user".drc_stated_books`.** His word is an INPUT (like a dropped file), so it lives beside `drc_imports`, not in `drc_rows` — which `record_day` deletes and replaces per day (`store.py:201-203`).

| Column | Type | Note |
|---|---|---|
| `id` | bigint identity PK | |
| `user_id` | int NOT NULL, tenant default + FK `"user".traders` | as `0016_drc.sql:22-24` |
| `day` | date NOT NULL | the day this book OPENS |
| `kind` | text CHECK IN (`opening`, `resolve`) | `opening` = §2c; `resolve` = a carried `trade_id` closed outside the export (§2b) |
| `positions` | jsonb NOT NULL, array | `opening`: `[]` = flat, else `{symbol, direction, shares, avg_cost|null}`; `resolve`: `{trade_id, exit_price|null, exit_time|null}` |
| `book_sha256` | text CHECK hex-64 | sha256 of `positions`' canonical JSON |
| `via` | text CHECK IN (`drc_page`, `voice_widget`) | the caller |
| `turn_id` | text NULL | the widget turn (voice caller only) |
| `readback_sha256` | text NULL | the confirmed read-back's binding (voice caller only) |
| `reason` | text NOT NULL | `first import` / `chain broken at <day>` / `closed outside export` |
| `supersedes` | bigint NULL FK self | a restatement; nothing is updated or deleted |
| `created_at` | timestamptz default now() | |

Append-only via the existing `"user".refuse_row_update()` trigger (the precedent cited at v3 `:137`). CHECK: a `resolve` row names exactly one `trade_id`.

**`drc_rows` (widened, no new table).** The `kind` CHECK (`0016_drc.sql:86`) gains `seed` and `book_close` (§2a, §2b). Unique `(user_id, day, kind, ref)` (`0016_drc.sql:95`) already gives one of each per day. `fn_version` → `drc.pairing/2` (`pairing.py:64`: "bumped whenever a derived figure's rule changes").

**The `carried_from` link (L57).** A carried trade's `inputs.carried_from = {day, trade_id, from_book_sha256}` or `{stated_book_id}`; the day's `seed` row names the same. Replay of any carried figure: read the `seed` row → the prior day's `book_close` (hash-checked) → its `open_position` rows → their inputs (`fill_lines`, `carried_lots`, `store.py:162-168`) → `drc_fills`. The link is by `(day, kind, ref)` + hash, never by `drc_rows.id`, because ids change when a day is re-recorded.

**Forward re-pair.** When a superseding file for day P is recorded, the store re-pairs every later recorded day in date order from its stored `drc_fills` (the inputs are all kept, `store.py:13-17`), each seeded from the new book. The superseding import succeeds only if every later day pairs; the first later day that fails FAILS the import naming that day and its reason, and nothing is replaced (one transaction or a staged set, §7 Q3). Each rebuilt day's note units are re-upserted by the build (human text preserved, L28).

**Migration.** One `db_migrations` file + `.rollback.sql`: create `drc_stated_books`; widen `drc_rows.kind`. Number: next free at the L68 gate — `0016` is D1's (`0016_drc.sql:8-11`), and a `0017_voice_turns` is recorded on the voice branch (L76's evidence line), so ≥ `0018` as of today; the desk numbers it (§7 Q2 on folding into `0016` instead).

**Who writes what (L40: one expert per side effect).**

| Side effect | Writer | Callers |
|---|---|---|
| `drc_stated_books` rows, `seed` / `book_close` rows, forward re-pair | `DrcStore` (the one writer of every `drc_*` row, `store.py:1`) — new `record_stated_book`, extended `seed_for` / `record_day` | `/drc` page (D2's route), `cobalt drc build`, the voice widget's ACT (its tool asks the store; it does not write) |
| `drc-trades/open_positions` unit, the seed line in `drc-summary/summary` | the ONE DRC build function (v2 D3 `build.py`, through `VaultWriter.upsert_unit`, v2 `:139`) | the build event only |
| his statement's note echo | none — the statement lives in Postgres; the note shows it only through the unit above (no reverse parse of his note, v3 `:226`) | — |

**Read-back proof (every chunk's check).** With-DB on `cobalt_dev`: (1) day 1 with a swing left open → `book_close.count = 1`, unit lists it; (2) day 2 import → `seed.source = carried`, `from_book_sha256` = day 1's, the carried trade's `trade_id` unchanged; (3) day 1 re-imported with a different file → day 2 re-paired or the import FAILS naming day 2; (4) first import without a statement → `not computed — opening book not stated`, zero trades; after `flat` → paired; (5) no-trade day between → its `seed` / `book_close` rows carry the position unchanged; (6) a missing trading day → FAILED naming it. Dev vault: unit bytes under its heading, his text byte-identical (v2 E3 shape).

## 4. Failure modes

| Situation | What the import does | What he sees | Law |
|---|---|---|---|
| First import ever, no statement | stores files; pairing `not computed — opening book not stated` | `/drc`: `state your opening book for <D>: [flat] [list]` | L1 |
| Prior trading day not recorded (no import, no no-trade DRC) | FAILED naming the missing day | the missing day + three remedies (import it · record its no-trade DRC · state the book) | L1, R93 |
| Prior day's pairing not computed | FAILED (built, `store.py:236-244`) | `<P> has pairing not computed — its open positions are unknown` | L1 |
| Prior day recorded before this lane (no `book_close`) | FAILED naming the day | `rebuild <P>` (re-pairs it from stored fills) | L1, L57 |
| `book_close` hash ≠ its `open_position` rows | FAILED naming the day | `stored book of <P> does not match` | L1, L57 |
| Leading sell on a symbol with no seed | FAILED naming the symbol (built, `pairing.py:194-198`) | the line and symbol | L1 |
| File contradicts a carried position (side, through-0) | FAILED naming the line (built, `pairing.py:203-218`) | the line, `contradicts the seed` | L1 |
| Carried position untouched by the file | carried unchanged | `continuing open position · last execution <date> · day k` | R67 |
| Partial cover of a carried position | realized on carried lots; remainder carried, same `trade_id` | both in the unit | R67, L57 |
| Carried position closed outside every export | carried (nothing can see it) until he acts | RESOLVE on `/drc`; a re-export supersedes | R90, L1 |
| RESOLVE without an exit price | trade CLOSED, source stated | realized `not computed — exit not in any export` | L57 |
| Stated position without a cost | carried; its exits realized `not computed — carried cost not stated` | same text | L57 |
| Superseding import of an earlier day | forward re-pair; any later day failing → the whole import FAILED, nothing replaced | the later day and its reason | L1 |
| Duplicate symbol in a seed | FAILED (built, `pairing.py:171-172`) | `seed carries <symbol> twice` | L1 |
| Seed lots ≠ seed held count | FAILED (built, `pairing.py:154-158`) | the symbol, both counts | L1 |
| Statement dropped inside `market_reset` | refused, as every DRC drop (v2 `:79`) | the refusal reason | v2 `[F-09]` |

No row assumes a book.

## 5. What he sees

- **Evening, in the DRC note** (unit `drc-trades/open_positions`): `left open: <n> — tomorrow's import starts from these` · one line per position: symbol · long/short · shares held · avg cost · opened <date> · day <k> · `new today` / `continuing open position`. Flat: `left open: 0 — tomorrow starts flat`.
- **Evening, in the summary line** (`drc-summary/summary`): `open overnight: <n>`.
- **Next day, on `/drc` before he drops anything:** `Starting book from DRC <prior date>: <n> open (<symbols>)` — or `No prior DRC for <prior date> — import it, record its no-trade DRC, or state your book`.
- **After the drop:** `<k> carried closed · <m> still open → tonight's DRC`.
- **First day ever:** `State your opening book for <date>: [I was flat] [List positions]` — or say it to the widget and confirm the read-back.

## 6. Chunks

| Chunk | What | Files | Write path (L29) | Migration | Depends on | h |
|---|---|---|---|---|---|---|
| K1 Book records | `drc_stated_books`; `drc_rows.kind` + `seed` / `book_close`; `DrcStore.record_stated_book`; `seed_for` returns the book with its source + hash; `record_day` writes `seed` / `book_close`; `carried_from` link in inputs; first import without a statement → `not computed`; `FN_VERSION` → `drc.pairing/2`; the B8 pin test replaced | `drc/store.py`, `drc/pairing.py`, `drc/models.py`, new migration + rollback, `db_migrations/placement.py`, tests | DB — yes | YES (next free, §3) | D1 merged | 5 |
| K2 No-trade carry + forward re-pair | the empty-day record (`pair_day([], D, seed)` + `record_day`); forward re-pair on a superseding file; the failures of §4 rows 2, 4, 5, 13 | `drc/store.py`, `drc/pairing.py`, tests | DB — yes | — | K1 | 4 |
| K3 Surfaces | the `open_positions` unit (moved from D5) + the summary count via the one build; `/drc` morning line, state-your-book form, RESOLVE `closed outside the export` | D3's `drc/build.py`, D2's `aset/web.py` `/drc` route, `drc/imports.py` | vault + DB — yes | — | K1, K2, D2, D3 | 5 |
| K4 Voice caller | a widget ACT tool `state opening book` / `resolve carried position`: parse, read-back, confirm → `DrcStore.record_stated_book` | voice tool registry (V3's) | DB — yes (through the store) | — | K1, voice V3 built | 2 |

4 chunks, 16 h seat hours (5+4+5+2; estimates, no measurement — the 0.4× fix-round factor of v2 `:171` stays UNVERIFIED). All four are write paths (L29: Opus 5 floor, never auto mode on a write path). One migration (K1).

**Order** (`close-2026-09-23.md:261`: D1 → D4 → D2 → D3): K1 + K2 after D1 merges, in parallel with D4 (L72 — they share no file with D4: D4 is `settings/models.py`, v2 `:178`); they must land in the same deploy as D2 + D3 (v2 `:181`: D2 and D3 land together) so that production's first import never runs B8. K3 is built on top of D2 + D3 (same deploy if checked in time — L43 — else the next evening; until K3 lands, K1's `not computed — opening book not stated` has no form, so K1 + K2 without K3 is lawful only if D2/D3 also wait — §7 Q10). K4 after voice V3; until then the page is the one caller.

## 7. Open to the tribunal

1. **Stated books: separate input table or a `drc_rows` kind?** Proposed: separate append-only table — his statement is an input; `drc_rows` is replaced per day (`store.py:201-203`) and would delete it.
2. **Migration: new numbered file, or fold into `0016` if D1 has not deployed when K1 builds?** Proposed: fold into `0016` only if D1 is unmerged at K1's cut (one DRC set, one rollback); otherwise the next free number. The desk numbers at L68.
3. **Forward re-pair: automatic, or refuse the superseding import until he rebuilds later days?** Proposed: automatic, all-or-nothing — the inputs are stored, the pairing is deterministic (L2), and a failure names the later day. Houses to settle one transaction vs staged set (the note re-upserts are vault writes outside the DB transaction: DB first, notes after, a note failure leaves the DB rebuilt and the note unit marked stale).
4. **Stated position without a cost:** allowed, realized P&L `not computed — carried cost not stated`? Proposed: yes (L57: never guessed).
5. **No-trade day:** the no-trade DRC (R93) is the event that records the carry — any other trigger? Proposed: no other trigger; a trading day with neither an import nor a no-trade DRC is a broken chain.
6. **Closed outside the export:** RESOLVE as a `drc_stated_books` `resolve` row, trade CLOSED with source stated. Proposed: yes; a later export carrying the execution supersedes the resolve (the export is truth, R67).
7. **Aging:** alert on a long-carried untouched position? Proposed: no alert (a swing is lawful); display `day <k>` and `last execution` only.
8. **Morning mention outside `/drc`** (09:00 reader / daily note): Proposed: not in this lane — the 09:00 reader stays unchanged (v2 `:165`); a wider quote is v2's later slice L7 (v2 `:183`).
9. **Days recorded before this lane** (no `book_close`): FAIL naming the day and offer `rebuild <day>`, or backfill in the migration? Proposed: FAIL + rebuild (the migration computes nothing; rebuild is the same pairing from stored fills).
10. **Landing set:** K1 + K2 with D2 + D3, and K3 in the same deploy or D2/D3 wait for it? Proposed: K1–K3 land with D2 + D3 as one set; if K3 is not checked in time, D2/D3 land with K1's first-import refusal worded to point at `cobalt drc state-book` (a CLI caller of the same store function, added to K1 at +0.5 h) — never with B8 in production.
11. **The `open_positions` unit leaves D5** (it needs no legs; D5 waits on S3 C2, v2 `:181`). Proposed: yes; D5 keeps the reconcile unit only.

## 8. Owner items

None. Every question above is a design question the houses can settle (L67 as amended 2026-09-24). Retiring O1 = A is R22's own instruction ("A for now" + the lane that replaces it), not a new decision. His two inputs the lane depends on are already ruled: DAS is the truth (R67), and a DRC every trading day (R93).

## 9. Sources

- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-24.md:31` (R22), `:38` (R29).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-22.md:99` (R67).
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` — L1 `:29-31`, L28 `:160-166`, L32 `:185-189`, L35 `:202-205`, L40 `:227-228`, L43 `:240-243`, L57 `:316-317`, L67 `:366-373`, L68 `:380-384`, L72 `:405-407`, L76 `:435-436`.
- `/Users/cobalt/cobalt/docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md:50`, `:79`, `:81`, `:94`, `:117`, `:139`, `:141`, `:165`, `:171`, `:175-181`, `:183`, `:191`, `:207`.
- `/Users/cobalt/cobalt/docs/30 - Design/S3-EXITS-v3-2026-09-22.md:22`, `:137`, `:141`, `:226`.
- `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/drc/pairing.py:6`, `:26-28`, `:64`, `:82`, `:117-129`, `:143-159`, `:162-174`, `:189-198`, `:203-218`, `:220-234`, `:239-254`.
- `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/drc/models.py:102-112`, `:165`, `:168`.
- `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/drc/store.py:1`, `:13-17`, `:88-97`, `:116`, `:162-168`, `:177-179`, `:201-203`, `:220-250`.
- `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0016_drc.sql:8-11`, `:22-24`, `:80-95`.
- `/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/daymode/propose.py:300-308`.
- `/Users/cobalt/cobalt-wt/drc-d1/tests/cobalt/test_drc_pairing.py:249-262`, `:265-272`.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/drc-d1-fix-r1-draft-2026-09-24.md:69` (O1).
- `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-d1-fix-r1-build-2026-09-24.md:228`, `:230` (ESCALATE 2, 4).
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/areas/cobalt-product-definition.md:61`, `:62`, `:63`, `:75`.
- `/Users/cobalt/cobalt/docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md:88`, `:127-142` (read-back / confirm; voice-ordered edit path).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-2026-09-23.md:261` (D4 → D2 → D3 order).
- His DRC note shape: `/Users/cobalt/Vault/Think/1 - Trading/5 - Review/DRC-2026-09-23.md` headings `:5-291` (`### Catalyst + Set Up + Trades` `:62`, `### Cobalt Rules Check` `:291`) — headings only read.
