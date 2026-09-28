# DRC — the overnight-position lane (v2, 2026-09-24) — ASTRA PENDING

Derived by seat `drc-overnight-derive-0924` (Opus 5.5, `claude-opus-5-5`), 10:23 ET Thu 2026-09-24, from:

- **The proposal:** `docs/30 - Design/DRC-OVERNIGHT-POSITION-PROPOSAL-2026-09-24.md` (committed `9a424242`). v2 is that proposal whole (§0–§9), each amended paragraph replaced or annotated in place and tagged `[F-nn]`; the tags index the fold table.
- **His rulings, never re-opened:** `cto-2026-09-24.md` R22 (the lane; O1 = A "for now"); `cto-2026-09-22.md` R65, R66, R67, R90, R93, R109; `cto-2026-09-23.md` R39.
- **Round-1 rulings, every seat that ruled (3 of 4):** Grok `scratch/tribunal-bars-0920/drc-overnight/r1/grok-ruling.md` (`TRIBUNAL R1: BUILD AFTER Q1 Q2 Q3 Q4 Q6 paste wording is folded`) · Gemini (optional fourth, 09-23 R96) `…/r1/gemini-ruling.md` (`TRIBUNAL R1: BUILD`) · the Anthropic seat, on `claude-opus-5-5` per 09-22 R109 and launch row `cto-2026-09-24.md` R32 (`Fable seat: yes` · `derive seat: claude-opus-5-5`), `docs/40 - DevDocs/reports/drc-overnight-tribunal-fable-r1-2026-09-24.md` (`BUILD AFTER re-pair triggers on every earlier-day record; stated-position model fields made Optional`) · **Astra: `METER — ASTRA PENDING`** (probe 09:3x: back Sat 09-26 06:47 ET; Astra reads this v2 / the FINAL then). Hub collation and file-check: `docs/40 - DevDocs/reports/drc-overnight-tribunal-2026-09-24.md`.
- **Fold table:** `docs/40 - DevDocs/reports/drc-overnight-tribunal-derive-2026-09-24.md` `## Fold table`.
- **Round 2:** ONE item (`R2-1`, the forward re-pair's trigger and inputs) — see that report's `## NEEDS ROUND 2`. Paragraphs it touches are marked `[R2-1 OPEN]`.

Committable: no ticker, price, share count or P&L of his (L32). The share figure in §1's R67 quote is his hypothetical in the ruling, not a trade.

---

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

`[F-20]` Erratum to B4 — Grok WRONG FACTS, verbatim: "`10-PROPOSAL.md` §1 B4: "see G-c". No G-c section exists in that file. The leading-`S` qualification itself is shown at `pairing.py:189-198`." (hub `GK29` HOLDS)

`[F-12]` §1 add — the Anthropic seat (a), verbatim: "§1 add: (vi) the stats-log rows are stored only in `drc_rows` `stats_row` rows (`store.py:170-186`), not in `drc_fills` (`0016_drc.sql:52-71`); (vii) a day recorded after a LATER day passes contiguity as a first import (`pairing.py:249`, pinned `test_drc_pairing.py:350-351`); (viii) the built `carried_from` holds the trade's OPEN day, not the prior book's day (`pairing.py:149`, `:231`; `test_drc_pairing.py:233`)." (hub `FC19`, `FC4`, `FC14` HOLD)

`[F-13]` §1 missed citations — Grok (a), verbatim: "Missed, not contradictory: - `seed_for` is uncalled outside its definition (§2). The carry is built and not wired to an import. - `store.py:193` stores `open_positions: len(...)` on the day row. That is a count of the book left open, not the book the day started from, and not a hash. - `pairing.py:113` copies `carried_from` onto the `Trade`. The proposal's date-only claim is still true; the cite list omitted this line. - `prior_trading_day` is also used by daymode (`propose.py:380`, `daymode/drc.py:152`). Those hits do not read `open_position` rows. - Prefill writes unit `drc-trades/tickers` (`prefill/drc.py:443`) and creates the note (`:427`). It does not write `open_positions`. - `upsert_unit` refuses to create a missing note (`writer.py:671-672`)." (hub `GK17` HOLDS; Gemini `GM4`: no missed READER — consistent)

S3 (the clause relied on): v3 itself still prints R2-2 as `OPEN FOR DEJAN` (`S3-EXITS-v3-2026-09-22.md:22`, `:141`); the ruling is `cto-2026-09-22.md` R67 (row line 99), recorded as F33 in v2 (`:50`) and in `areas/cobalt-product-definition.md:61`. Quoted, his words: "…your scenario where I exit 50 shares … and at the end of the day … still have open 50 shares, does not exist right now, but it should be considered as this is still open position for the next day … appear as continuing position as 50 shares and keep going that way and just call it an open position." Desk reading (4): "a position still open at the DRC carries to the next day as an OPEN POSITION with its held shares, continuing until closed." And (3): "the DAS trading-log import RECONCILES — DAS is the truth". (The share figure is his hypothetical in the ruling, not a trade.)

**Already designed and built:** the carry itself — day D's open positions stored, day D+1 seeded from them, one `trade_id`, FIFO lots with their original prices, loud failure on a leading sell with no seed, on a seed contradiction, on a broken chain, on a prior day not computed (B1–B7).

**Not designed or not built:** (i) the night-before signal HE sees — the `open_positions` unit is designed but unbuilt and parked in D5 behind S3 C2 (B9); (ii) any stored record of WHICH book a day started from (the seed is read at `store.py:245-250` and not recorded with the day; a day's `carried_from` is a date only, `models.py:168`, `pairing.py:82`, `:231`); (iii) any way to state an opening book when no prior DRC exists — today that case is B8, flat; (iv) a no-trade day's record: `check_contiguity` names "an import or a no-trade record" (`pairing.py:246`, `:252`) but no code writes a no-trade record (`grep -rn "no-trade\|no_trade" src/cobalt` hits only those two docstring lines and an unrelated comment); (v) what happens to later days when an earlier day is re-imported (`store.py:201-203` deletes and replaces the day's rows; nothing re-checks a later day seeded from them).

`[F-19]` Erratum to (iv) — Grok WRONG FACTS, verbatim: "`11-design-digest.md` UNPROVEN, the no-trade bullet: "the only hits are `pairing.py:246`, `:252` and an unrelated comment." §3 also hits `radar/seam.py:21` and `aset/web.py:311`. Neither writes a no-trade record, so (iv) still holds. The digest undercounts." (hub `GK28` HOLDS; the same line of the proposal, `:30`, carries the same undercount)

## 2. The gap

### 2a. The NIGHT-BEFORE SIGNAL

The evening DRC states the book it leaves open in two places, written by the same build run from the same `DayPairing`:

**Stored rows (exists, extended).** The day's `open_position` rows (B2) plus ONE new `drc_rows` row `kind = 'book_close'`, `ref = 'book'`: `derived = {count, trade_ids[], book_sha256}` where `book_sha256` = sha256 of the canonical JSON of the day's `open_positions` (sorted by `trade_id`); `inputs = {trading_log_import_id, seed_ref}` (§3). This row is what the next morning checks against; it exists on every recorded day, `count = 0` included, so "flat" is a stored fact, never an absence. `[F-15]` (the placement is the proposal's — see the fold table for the day-row alternative not taken; canonical encoding gated by X4)

**Note unit (designed, moved here).** `drc-trades/open_positions`, marker-bounded, stable id, upserted in place by the one DRC build function (L28, L40) — moved out of D5 (it needs `drc_rows`, not S3's legs). Fields, one block per open position plus a header line:

- header: `left open: <count>` · `book: <book_sha256 first 12>` · `next import starts from this book` — `left open: 0 — next import starts flat (stated by this DRC)` when the count is 0;
- per position: `trade_id` · symbol · direction · held shares · average cost of the held lots (from the stored lots; `not given` when a stated lot has no price, §2c) · `opened_on` · trading days held · `carried_from` (the day whose book it came from, or `stated <date>`) · status `new today` | `continuing open position` (v2 `:141`'s wording) · `last execution: <date>`.

`[F-24]` Erratum to the `carried_from` field — the Anthropic seat WRONG FACTS 2, verbatim: "Proposal `:43`, the unit's "`carried_from` (the day whose book it came from…)". The built `carried_from` is the trade's open day: `_seeded` sets it to `position.opened_on` (`pairing.py:149`), and that persists through `:231`. The test asserts it equals the open day (`test_drc_pairing.py:233`). For a trade carried more than one day these are different days." (hub `FC20` HOLDS "as a naming collision with the built field". §2b step 3 below replaces the bare date with the link object; the unit field renders that object's `day`. No rename is folded — the only rename offered sits inside a wording not taken, `[F-15]`.)

No figure in the unit is computed outside the stored row (v2 `:117`, L57). `[F-07]` (kept; Grok's Q7 reasoning renders `day <k>` from the stored `opened_on`, the seat's (c) stores it — no wording offered on Q7; this sentence stands)

`[F-11]` Q11 — the Anthropic seat, verbatim: "The `drc-trades/open_positions` unit leaves D5 for K3, built by the one DRC build (v2 D3 `build.py`). D5 keeps the reconcile unit only. The A31 `open items carried forward` line for open positions (v2 `:295`) renders from the same stored rows in the same build call. No second computation." (UNCHECKED by a hub — read by the derive at `DRC-AUTOMATION-v2-2026-09-22.md:295`: A31 lists "open positions (R67)". Grok, Gemini: ADOPT.)

### 2b. The MORNING READ

At the next import for day D (drop on `/drc`, or `cobalt drc build`):

1. `seed_for(D)` resolves `P = prior_trading_day(D)` (B7) and the chain (B5).
2. It reads `P`'s `book_close` row and `P`'s `open_position` rows, recomputes `book_sha256` over the rows and compares it with the stored one. Mismatch → FAILED `seed for D: <P>'s stored book does not match its own close row` (L1). A missing `book_close` on a recorded `P` → FAILED naming `P` (rows built before this lane: see §7 Q9).
3. The day records what it started from: ONE `drc_rows` row `kind = 'seed'`, `ref = 'book'`: `inputs = {source: carried | stated | no_trade_carry, from_day: P, from_book_sha256, stated_book_id}`, `derived = {count, trade_ids[]}`. Every carried trade's inputs gain `carried_from = {day: P, trade_id, from_book_sha256}` — the replay key (L57), replacing the bare date. `[F-24]` (see the erratum in §2a: the built field of the same name holds the open day)
4. Pairing runs with that seed (B3). The `/drc` page shows the morning line (§5) BEFORE the file is paired, so he sees what the import will assume.

Cases:

- **Gap day — weekend / holiday.** `prior_trading_day` skips it (B7); the Friday book seeds Monday. Nothing new.
- **Gap day — a trading day with no DRC.** R93 (`areas/cobalt-product-definition.md:63`): a DRC every market trading day, no-trade days carry his why. So a missing trading day is a broken chain → FAILED naming the missing day, with the remedy on the page (import that day, record its no-trade DRC, or state the book — §2c). The phantom-position scenario (v2 `:81`) is exactly this and stays loud.
- **A no-trade day with an open position.** The no-trade DRC is recorded by the same build with zero executions: `pair_day([], D, seed)` already returns the seed as D's open positions unchanged (`pairing.py:170-174`, `:220-234`); the day gets its `seed` row (`source: no_trade_carry`), its `book_close` row and the unit (`continuing open position`, `last execution` unchanged). This is new: no caller records an empty day today (§1 (iv)).
  - `[F-21]` Erratum — Grok WRONG FACTS, verbatim: "`10-PROPOSAL.md` §2b: `pair_day([], D, seed)` "returns the seed as D's open positions unchanged (`pairing.py:170-174`, `:220-234`)". The new `OpenPosition.day` is the no-trade day (`pairing.py:231`), not the prior day. `trade_id`, lots, and `opened_on` are unchanged. A test that expects the two days' `book_sha256` to be equal will fail if `day` is inside the hashed JSON, and that is not a defect." (hub `GK30` HOLDS)
  - `[F-05]` The no-trade input — the Anthropic seat Q5, verbatim: "The no-trade DRC (R93) is the only event that records a day with no executions. Its INPUT is one `drc_stated_books` row, `kind = 'no_trade'`, `positions = []`, `reason = 'no-trade DRC'`, written by `record_stated_book` when he records the no-trade DRC on `/drc` (his why stays his text in the note). `record_day` for a day with no trading-log import is refused unless that row exists, and the `day` row's inputs name its id. A trading day with neither an import nor that row is a broken chain." (hub `FC10` HOLDS; Grok, Gemini ADOPT the single trigger this keeps)
- **Partial overnight cover.** Seeded book reduced by the morning's exits, FIFO from the carried lots (`pairing.py:117-129`); realized P&L at the carried lot prices; the remainder is open at file end and carried again with the same `trade_id` (`pairing.py:220-234`). Built; this lane adds only the `seed` / `book_close` rows and the unit.
- **A carried position closed outside the export's window** (an execution after the export was cut, a broker action, an account transfer). Two sub-cases:
  - *the next file touches the symbol inconsistently* — a side contradicting the seed or a through-0 → FAILED "contradicts the seed" (`pairing.py:203-218`). Loud, built.
  - *the next file never touches it* — nothing can see it: the position is carried and shown `continuing open position` with `last execution: <date>` every evening. The remedy is his: (1) re-export the day that carries the missing execution and drop it — it supersedes that day's file (`store.py:88-97`, `:116`) and the lane re-pairs every later day forward (§3); or (2) when no export will ever carry it, the RESOLVE action on `/drc` (R90, `areas/cobalt-product-definition.md:62`: "give me way to resolve in DRC") records `closed outside the export` for that `trade_id` as a stated correction (§3 `drc_stated_books`), with an exit price only if he gives one — else realized P&L `not computed — exit not in any export`. `[F-06]` (the RESOLVE's full rule: §3 "RESOLVE")
- **An earlier day re-imported after later days were built.** `record_day` replaces `P`'s rows (`store.py:201-203`), so `P`'s `book_sha256` can change under a day already seeded from it. The lane re-pairs forward (§3 "forward re-pair"). `[R2-1 OPEN]` (whether a FIRST record of an earlier day, after a later day, also triggers it)

### 2c. The FIRST DAY / a broken chain

When there is no prior book to read — the first import ever (`pairing.py:248`) or a chain the page cannot close by importing the missing day — the opening book must come from somewhere. Today it is flat (B8), and the file cannot see a morning short cover: E1 books a cover as `B` (`pairing.py:6`), so a cover reads as a new long that stays open at file end (`test_drc_pairing.py:265-272`) — a silent phantom, exactly what L1 forbids once swings are real.

| Option | What happens on the first day / a broken chain | What it costs him | Residual risk |
|---|---|---|---|
| **A — Stated opening book** | The import stores the files (`drc_imports` / `drc_fills` as today) but pairing does not run: the day shows `not computed — opening book not stated`. `/drc` shows ONE line with two actions: `I started <D> flat` (one tap) or `list what I held` (per position: symbol, direction, shares, average cost optional). The same statement can be made in the voice / text widget: its read-back ("opening book for <D>: flat" / "<n> positions: …") and his confirm (09-23 R39 shape, L28 as amended 2026-09-23) call the same store function. Stored append-only in `drc_stated_books`; pairing then runs from it (`source: stated`). | One tap on the very first import; one tap (or a short list) after a broken chain he cannot close by importing. Nothing on ordinary days. | None silent: every opening book is either carried with a hash or his stated word. A stated position with no cost renders its realized P&L `not computed — carried cost not stated`. |
| **B — Explicit flat only** | As A, but the only statement accepted is `flat`. A day that did not start flat cannot be the first import; he starts the chain on a later flat day (or imports the earlier days). | One tap; cannot start or restart the chain on a day a swing is open. | None silent; a real swing at restart blocks the DRC until a flat day. |
| **C — Fail on evidence, flat otherwise** | Keep B8 (flat) and fail only when the file contradicts flat (a leading `S` — built, `pairing.py:194-198`); flag every position opened and still open on a first import `opened on a first import — check`. | Zero taps. | A cover read as a long is visible only as a flagged line he must notice; the next day seeds from it. Not fail-loud (L1). |

`[F-16]` Erratum to row A's widget sentence — Gemini (d), verbatim: "The morning 'state your book' statement is a DB input (`drc_stated_books`), not a vault edit, so the L28 voice-ordered edit clause does NOT apply to it; however, the general voice ACT confirm shape (`2.6`) does apply." (hub `GM11` HOLDS; Grok (d) and the seat (d) rule the same — `FC17` HOLDS. The "L28 as amended 2026-09-23" citation in row A is superseded by this line.)

**RECOMMENDATION: A.** It is the only option with no silent path (L1: "a missing carried position is a loud FAILED, never a silent flat" — the index-card line), it costs one tap in the common case (flat), it keeps a real swing representable on a restart (B cannot), and it reuses two paths already ruled: the `/drc` RESOLVE action (R90) and the voice-ordered confirm (09-23 R39). Under A, B8's pin test changes from "a leading buy is a long" to "a first import without a stated book does not pair", and O1 = A retires — which is R22's own instruction ("the lane replaces assume flat"), not a new ruling.

`[F-14]` Option A is the design every seat that ruled took (Grok, Gemini, the Anthropic seat; Astra PENDING). Grok (b), verbatim: "Under option A, every row of §4 is fail-loud. No pairing starts from a book that was neither a hash-checked carry nor his statement. Option C is not fail-loud, as the proposal says." The flat-tap residual — Grok (b) walk 1, verbatim: "If he taps flat instead, the `B` opens a long because a stated empty book is an empty seed (`pairing.py:189-193`). That long is his stated flat plus an ambiguous execution, not an assumed book. The same evening's unit lists it as `new today`. Accepted residual of his tap. It is visible before the next morning seeds it." (gated by X2). `[R2-1 OPEN]` the Anthropic seat holds one remaining assume path under A (an earlier day recorded after a later stated day; hub `FC3`, `FC22` HOLD, hub ESCALATE 2); both houses hold none — round 2.

## 3. Data model and write paths

**New table (append-only input): `"user".drc_stated_books`.** His word is an INPUT (like a dropped file), so it lives beside `drc_imports`, not in `drc_rows` — which `record_day` deletes and replaces per day (`store.py:201-203`).

`[F-01]` Q1 — Grok, verbatim: "Stated opening books and resolves live only in append-only `"user".drc_stated_books`, not as a `drc_rows` kind. `record_day` runs `DELETE FROM drc_rows` for that day (`store.py:202`) and would erase a statement stored there. The current row for a day and kind is the row whose id is not the `supersedes` of any other row (same predicate as `store.py:92-93`). Two current `opening` rows for one day, or two current `resolve` rows for one `trade_id`, FAIL naming both ids. `record_stated_book` refuses inside `market_reset`, the same gate as `VaultWriter._session_gate` (`writer.py:388`, §12)." (hub `GK1`–`GK4` HOLD; the refusal is gated by X6)

| Column | Type | Note |
|---|---|---|
| `id` | bigint identity PK | |
| `user_id` | int NOT NULL, tenant default + FK `"user".traders` | as `0016_drc.sql:22-24` |
| `day` | date NOT NULL | the day this book OPENS |
| `kind` | text CHECK IN (`opening`, `resolve`, `no_trade`) `[F-05]` | `opening` = §2c; `resolve` = a carried `trade_id` closed outside the export (§2b); `no_trade` = the no-trade DRC's input (§2b, `[F-05]`) |
| `positions` | jsonb NOT NULL, array | `opening`: `[]` = flat, else `{symbol, direction, shares, avg_cost|null}`; `resolve`: `{trade_id, exit_price|null, exit_time|null}`; `no_trade`: `[]` `[F-05]` |
| `book_sha256` | text CHECK hex-64 | sha256 of `positions`' canonical JSON |
| `via` | text CHECK IN (`drc_page`, `voice_widget`) | the caller |
| `turn_id` | text NULL | the widget turn (voice caller only) |
| `readback_sha256` | text NULL | the confirmed read-back's binding (voice caller only) |
| `reason` | text NOT NULL | `first import` / `chain broken at <day>` / `closed outside export` / `no-trade DRC` `[F-05]` |
| `supersedes` | bigint NULL FK self | a restatement; nothing is updated or deleted |
| `created_at` | timestamptz default now() | |

Append-only via the existing `"user".refuse_row_update()` trigger (the precedent cited at v3 `:137`). CHECK: a `resolve` row names exactly one `trade_id`.

(The `via` CHECK does not name the `cobalt drc state-book` CLI caller of `[F-10]`; no seat offered a value for it — a named gap for K1's build prompt to carry to its check, not filled here.)

**`drc_rows` (widened, no new table).** The `kind` CHECK (`0016_drc.sql:86`) gains `seed` and `book_close` (§2a, §2b). Unique `(user_id, day, kind, ref)` (`0016_drc.sql:95`) already gives one of each per day. `fn_version` → `drc.pairing/2` (`pairing.py:64`: "bumped whenever a derived figure's rule changes").

**The `carried_from` link (L57).** A carried trade's `inputs.carried_from = {day, trade_id, from_book_sha256}` or `{stated_book_id}`; the day's `seed` row names the same. Replay of any carried figure: read the `seed` row → the prior day's `book_close` (hash-checked) → its `open_position` rows → their inputs (`fill_lines`, `carried_lots`, `store.py:162-168`) → `drc_fills`. The link is by `(day, kind, ref)` + hash, never by `drc_rows.id`, because ids change when a day is re-recorded. `[F-15]` (kept: Grok (c) and Gemini (c) rule this chain replayable — `GM9`, `GK22` HOLD; Grok's condition: "The logical key survives only because Q3 rewrites every dependent day in the same transaction", which `[F-03]` folds)

**Forward re-pair.** `[F-03]` REPLACED — Grok Q3, verbatim: "Forward re-pair is automatic and all-or-nothing, in memory first. On a superseding import of day P, load fills from the current import only (the `drc_imports` row no other row supersedes). Pair every later recorded day in date order, each seeded from the new prior book. If any later day fails, write nothing and FAIL naming that day. If all pair, one database transaction replaces `drc_rows` for P and every later day. Note re-upserts run after the commit, in date order. A note failure leaves the database committed, marks that unit stale, and FAILs naming the note. The morning book is read from the database, never from the note." (hub `GK7`, `GK32` HOLD; gated by X7, X9)

`[R2-1 OPEN]` Round 2 settles: (i) whether the trigger is also a FIRST record of day P when a later day is already recorded; (ii) whether a later day's STATED seed is replaced by the carried book when they differ; (iii) where a re-paired day's stats rows come from. The errata below stand whatever round 2 decides.

`[F-23]` Erratum to the proposal's sentence ("re-pairs every later recorded day in date order from its stored `drc_fills` (the inputs are all kept …)") — the Anthropic seat WRONG FACTS 1, verbatim: "Proposal `:104`, "re-pairs every later recorded day … from its stored `drc_fills` (the inputs are all kept, `store.py:13-17`)". `drc_fills` has trading-log columns only (`0016_drc.sql:52-71`, `store.py:119-144`). The stats rows are only in `drc_rows` (`store.py:170-186`), which `record_day` deletes (`:201-203`), and `match_stats` needs them (`pairing.py:260-316`)." (hub `FC19` HOLDS)

`[F-25]` Erratum to the proposal's "nothing is replaced" — the Anthropic seat WRONG FACTS 3, verbatim: "Proposal `:104`, "nothing is replaced". `record_import` commits the superseding file in its own transaction before any pairing (`store.py:85-150`), and it becomes the day's newest file (`:88-97`). Only `drc_rows` can be all-or-nothing." (hub `FC8` HOLDS)

**RESOLVE.** `[F-06]` Q6 — Grok, verbatim: "A RESOLVE writes one `drc_stated_books` row `kind=resolve` for one `trade_id`. The trade is CLOSED, source stated. Realized P&L is computed only when every carried lot's price and `exit_price` are stored; otherwise the stored figure is `not computed — exit not in any export`, and the closed trade's inputs include the resolve row id. The close runs the Q3 forward re-pair so no later `book_close` still contains that `trade_id`. A later export that contains the closing execution supersedes the resolve and re-pairs from the export (R67: the export is the truth). A later export that still shows the shares open supersedes the resolve the same way and the position stays open. Never a silent close (R90)." (hub `GK10` HOLDS; how the CLOSED trade is emitted with no exit leg is gated by X11)

**Stated position without a cost.** `[F-04]` Q4 — Grok, verbatim: "A stated position may omit average cost. The carried lot stores that cost or null, and that null is the stored input. An exit against a null cost stores realized `not computed — carried cost not stated` and does not call the price arithmetic in `_reduce` (`pairing.py:117-129`)." (hub `GK8` HOLDS; `Lot.price` is required today, `models.py:98`. A stated position also carries no entry time while `OpenPosition.entry_time` is required, `models.py:110` — hub `FC9` HOLDS; whether the lane can pair a stated day at all is X3, and X3's failure branch is the design's named gap, never filled here.)

**Migration.** One `db_migrations` file + `.rollback.sql`: create `drc_stated_books`; widen `drc_rows.kind`. Number: next free at the L68 gate — `0016` is D1's (`0016_drc.sql:8-11`), and a `0017_voice_turns` is recorded on the voice branch (L76's evidence line), so ≥ `0018` as of today; the desk numbers it (§7 Q2 on folding into `0016` instead).

`[F-02]` Q2 — Grok, verbatim: "One new `db_migrations` file plus `.rollback.sql`. The desk numbers it at the L68 gate. Fold the `drc_rows.kind` widening into `0016_drc.sql` only when, at K1's cut, that file is still unmerged and `0016` is not applied on `cobalt_dev`. Otherwise a new file. Never a number already used by `0017_voice_turns.sql`." (hub `GK5` HOLDS, `0017` = `69c376bd`; `GK6` — an edited, already-applied `0016` leaves the old CHECK — is UNVERIFIABLE FROM READS → X5. The migration NUMBER is the gate's, L68.)

**Who writes what (L40: one expert per side effect).**

| Side effect | Writer | Callers |
|---|---|---|
| `drc_stated_books` rows, `seed` / `book_close` rows, forward re-pair | `DrcStore` (the one writer of every `drc_*` row, `store.py:1`) — new `record_stated_book`, extended `seed_for` / `record_day` | `/drc` page (D2's route), `cobalt drc build`, the `cobalt drc state-book` CLI `[F-10]`, the voice widget's ACT (its tool asks the store; it does not write) |
| `drc-trades/open_positions` unit, the seed line in `drc-summary/summary` | the ONE DRC build function (v2 D3 `build.py`, through `VaultWriter.upsert_unit`, v2 `:139`) | the build event only |
| his statement's note echo | none — the statement lives in Postgres; the note shows it only through the unit above (no reverse parse of his note, v3 `:226`) | — |

**Read-back proof (every chunk's check).** With-DB on `cobalt_dev`: (1) day 1 with a swing left open → `book_close.count = 1`, unit lists it; (2) day 2 import → `seed.source = carried`, `from_book_sha256` = day 1's, the carried trade's `trade_id` unchanged; (3) day 1 re-imported with a different file → day 2 re-paired or the import FAILS naming day 2; (4) first import without a statement → `not computed — opening book not stated`, zero trades; after `flat` → paired; (5) no-trade day between → its `seed` / `book_close` rows carry the position unchanged; (6) a missing trading day → FAILED naming it. Dev vault: unit bytes under its heading, his text byte-identical (v2 E3 shape). `[F-18]` (kept, and extended by `## First-gate experiments (L70)` below)

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
| Superseding import of an earlier day | forward re-pair; any later day failing → the whole import FAILED, nothing replaced `[F-03]` `[F-25]` (the superseding file's own import row stays committed; only `drc_rows` are all-or-nothing) | the later day and its reason | L1 |
| Re-paired day's note write fails `[F-03]` | database committed; that unit marked stale; FAILED naming the note | the note named; `/drc` shows the database book | L1 |
| Two current `opening` rows for one day, or two current `resolve` rows for one `trade_id` `[F-01]` | FAILED naming both ids | both ids | L1 |
| A day with no trading-log import and no `no_trade` row `[F-05]` | `record_day` refused | a broken chain on the next day | L1, R93 |
| Duplicate symbol in a seed | FAILED (built, `pairing.py:171-172`) | `seed carries <symbol> twice` | L1 |
| Seed lots ≠ seed held count | FAILED (built, `pairing.py:154-158`) | the symbol, both counts | L1 |
| Statement dropped inside `market_reset` | refused, as every DRC drop (v2 `:79`) — and `record_stated_book` itself refuses `[F-01]` | the refusal reason | v2 `[F-09]` |

No row assumes a book. `[R2-1 OPEN]` (the seat's earlier-day-recorded-later case)

## 5. What he sees

- **Evening, in the DRC note** (unit `drc-trades/open_positions`): `left open: <n> — tomorrow's import starts from these` · one line per position: symbol · long/short · shares held · avg cost · opened <date> · day <k> · `new today` / `continuing open position`. Flat: `left open: 0 — tomorrow starts flat`.
- **Evening, in the summary line** (`drc-summary/summary`): `open overnight: <n>`. (gated by X14: the section is on neither his note nor his template — hub `GK25` HOLDS)
- **Evening, in `open items carried forward` (A31)**: the open positions, from the same rows in the same build call `[F-11]`.
- **Next day, on `/drc` before he drops anything:** `Starting book from DRC <prior date>: <n> open (<symbols>)` — or `No prior DRC for <prior date> — import it, record its no-trade DRC, or state your book`.
- **After the drop:** `<k> carried closed · <m> still open → tonight's DRC`.
- **First day ever:** `State your opening book for <date>: [I was flat] [List positions]` — or say it to the widget and confirm the read-back.

## 6. Chunks

| Chunk | What | Files | Write path (L29) | Migration | Depends on | h |
|---|---|---|---|---|---|---|
| K1 Book records | `drc_stated_books` (kinds `opening`, `resolve`, `no_trade` `[F-05]`); `drc_rows.kind` + `seed` / `book_close`; `DrcStore.record_stated_book` (refuses inside `market_reset`, `[F-01]`); `seed_for` returns the book with its source + hash; `record_day` writes `seed` / `book_close`; `carried_from` link in inputs; first import without a statement → `not computed`; `FN_VERSION` → `drc.pairing/2`; the B8 pin test replaced; the `cobalt drc state-book` CLI `[F-10]` | `drc/store.py`, `drc/pairing.py`, `drc/models.py`, new migration + rollback, `db_migrations/placement.py`, tests | DB — yes | YES (next free, §3) | D1 merged | 5 + 0.5 `[F-10]` |
| K2 No-trade carry + forward re-pair | the empty-day record (`pair_day([], D, seed)` + `record_day`, on a `no_trade` input `[F-05]`); forward re-pair on a superseding file `[F-03]` `[R2-1 OPEN]`; RESOLVE's re-pair `[F-06]`; the failures of §4 rows 2, 4, 5, 13 | `drc/store.py`, `drc/pairing.py`, tests | DB — yes | — | K1 | 4 |
| K3 Surfaces | the `open_positions` unit (moved from D5) + the summary count via the one build + the A31 line from the same rows `[F-11]`; `/drc` morning line, state-your-book form, RESOLVE `closed outside the export` | D3's `drc/build.py`, D2's `aset/web.py` `/drc` route, `drc/imports.py` | vault + DB — yes | — | K1, K2, D2, D3 | 5 |
| K4 Voice caller | a widget ACT tool `state opening book` / `resolve carried position`: parse, read-back, confirm → `DrcStore.record_stated_book` (voice FINAL §2.6 shape, `[F-16]`) | voice tool registry (V3's) | DB — yes (through the store) | — | K1, voice V3 built | 2 |

4 chunks, 16 h seat hours (5+4+5+2; estimates, no measurement — the 0.4× fix-round factor of v2 `:171` stays UNVERIFIED). All four are write paths (L29: Opus 5 floor, never auto mode on a write path). One migration (K1). `[F-10]` v2: 16.5 h with the CLI's +0.5 h (the proposal's own Q10 estimate, UNVERIFIED); round 2 may move K2 (the seat's Q3 estimate +1 h, UNVERIFIED).

**Order** (`close-2026-09-23.md:261`: D1 → D4 → D2 → D3): K1 + K2 after D1 merges, in parallel with D4 (L72 — they share no file with D4: D4 is `settings/models.py`, v2 `:178`); they must land in the same deploy as D2 + D3 (v2 `:181`: D2 and D3 land together) so that production's first import never runs B8. K3 is built on top of D2 + D3 (same deploy if checked in time — L43 — else the next evening; until K3 lands, K1's `not computed — opening book not stated` has no form, so K1 + K2 without K3 is lawful only if D2/D3 also wait — §7 Q10). K4 after voice V3; until then the page is the one caller.

`[F-10]` Q10 — the Anthropic seat, verbatim: "K1 may land in any deploy on its own. It is a library with no production caller. D2 and D3 are never deployed without K1 and K2 and at least one caller of `record_stated_book`: K3's form, or the `cobalt drc state-book` CLI (+0.5 h to K1, the same store function, L3). K3 lands in the same deploy as D2 + D3 when it is checked in time (L43). Otherwise the CLI stands in." (hub `FC13` HOLDS; Grok (e) and Gemini (e) rule K1 alone inert — `GK13`, `GM12` HOLD. This supersedes the paragraph above where they differ: D2/D3 do not wait for K3.)

`[F-17]` (e) — the Anthropic seat, verbatim: "K1 is not held for D2 / D3, and D2 / D3 are held for K1 + K2 (Q10)." Grok (e), verbatim, on the seam: "D2's route is not in this packet, so "D2 calls `pair_day`" is the proposal's seam, not a located call. L72: that seam is a shared contract and belongs in both prompts before either build launches. The stacked gate does not decide it." The landing set, the deploy order and the migration number are the desk's lane at its L43 / L68 gate — stated here as what the rulings leave, not ruled by this file.

## 7. Open to the tribunal

As ruled in round 1 (details in the fold table):

1. **Stated books: separate input table or a `drc_rows` kind?** → separate append-only table, `[F-01]` (Grok's wording; 3 of 3 ruling seats).
2. **Migration** → `[F-02]` (Grok's wording). X5 gates the fold into `0016`.
3. **Forward re-pair** → `[F-03]` (Grok's wording) for a superseding import; `[R2-1 OPEN]` for the trigger's scope, a stated later seed, and the stats-row source.
4. **Stated position without a cost** → yes, `[F-04]` (Grok's wording); the absent entry time is X3.
5. **No-trade day** → the no-trade DRC is the only event (3 of 3), with a stored `no_trade` input, `[F-05]`.
6. **Closed outside the export** → `[F-06]` (Grok's wording); X11 gates the no-exit CLOSED trade.
7. **Aging** → no alert (3 of 3); `day <k>` and `last execution` only. `[F-07]`
8. **Morning mention outside `/drc`** → not in this lane (3 of 3). `[F-08]`
9. **Days recorded before this lane** → FAIL + `rebuild <day>`; the migration computes nothing (3 of 3). `[F-09]`
10. **Landing set** → `[F-10]`, `[F-17]` (the desk plans it).
11. **The `open_positions` unit leaves D5** → yes, `[F-11]`.

## 8. Owner items

None. Every question above is a design question the houses can settle (L67 as amended 2026-09-24). Retiring O1 = A is R22's own instruction ("A for now" + the lane that replaces it), not a new decision. His two inputs the lane depends on are already ruled: DAS is the truth (R67), and a DRC every trading day (R93). (Round 1: every seat that ruled wrote `none`.)

## 9. Sources

- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-24.md:31` (R22), `:38` (R29).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-22.md:99` (R67).
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` — L1 `:29-31`, L28 `:160-166`, L32 `:185-189`, L35 `:202-205`, L40 `:227-228`, L43 `:240-243`, L57 `:316-317`, L67 `:366-373`, L68 `:380-384`, L72 `:405-407`, L76 `:435-436`.
- `/Users/cobalt/cobalt/docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md:50`, `:79`, `:81`, `:94`, `:117`, `:139`, `:141`, `:165`, `:171`, `:175-181`, `:183`, `:191`, `:207`; `:295` (A31, `[F-11]`, read by the derive).
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
- v2 additions: the round-1 rulings named in the header; the hub file-check rows cited at each `[F-nn]`.

---

## First-gate experiments (L70)

Each runs on `cobalt_dev` (under L76's one lock) or in the dev vault, before the chunk it gates; X12 alone reads one of his own files and is a hub-run read (L41). Named-by and the hub's dedup id (`E-n`, `X-C`) in brackets. The proposal's UNPROVEN rows, as the rulings leave them: the hour estimates stay unproven (no experiment gates them); `0017` is settled (`69c376bd`, hub `GK31`); the no-trade grep is settled (four hits, none a writer, `GK28`); the transaction shape is X7; S3 still printing R2-2 OPEN is true and does not gate this lane (R67 is the ruling).

**Before K1**

| X | Experiment | Named by | Result that changes the design |
|---|---|---|---|
| X1 | Proposal read-back (1), (2): day 1 leaves one open position; day 2 imports, the carried `trade_id` unchanged, `seed.source = carried`, `from_book_sha256` = day 1's. | proposal; grok X1 [E-10] | a changed `trade_id` or source → K1's seed record is wrong |
| X2 | Proposal read-back (4) plus the cover: first import, no statement → `not computed`, zero trades, no `book_close`; state the short, drop a leading `B` → one CLOSED trade, `book_close` count 0; fresh chain, state flat, leading `B` → one OPEN long listed by the evening unit. | proposal; grok X2 [E-10] | the long missing from the unit → the flat tap must FAIL when the file still holds a position opened that day (grok X2) |
| X3 | Stated position, cost null and entry time null, next day's file closes it: realized is the literal `not computed — carried cost not stated`, `_reduce` not applied, no exception at `pairing.py:69`, `:105`, `:235`. | grok X10; seat X5 [E-3] | an exception or any numeric P&L → the stated-position model is incomplete (the named gap of `[F-04]`) |
| X4 | Hash the same `open_position` rows twice in two processes (canonical JSON sorted by `trade_id`); compare with the stored `book_close`. | grok X7 [E-7] | different hex → the canonical encoding is fixed before K1, or the morning check false-FAILs |
| X5 | Apply an edited `0016` on a `cobalt_dev` where the old `0016` applied; insert `kind = 'seed'`. | grok Q2 / hub `GK6` [X-C] | the CHECK unchanged → a new numbered file, never the fold (`[F-02]`'s "Otherwise") |
| X6 | `record_stated_book` called inside `market_reset` (the widget's tool at 20:15 ET with a constructed clock included): refused, no row. Also gates K4. | grok X9; seat X9 [E-6] | the row commits while the note write is refused → `[F-01]`'s refusal is not what was built |

**Before K2**

| X | Experiment | Named by | Result that changes the design |
|---|---|---|---|
| X7 | Proposal read-back (3), both halves: re-import day 1 with a file that closes the swing while day 2's re-pair fails (day 1's and day 2's old `drc_rows` both present, import FAILED naming day 2); then every day pairs, the database commits, and the day-2 note upsert fails (database has the new hashes, day-2 unit stale, `/drc` shows the database book). | proposal; grok X3, X4; gemini X1; seat X1, X3 [E-1] | any day half-replaced, or the page showing the old note, or the database rolling back with the note → `[F-03]`'s one-transaction / stale-mark shape changes |
| X8 | Proposal read-back (5), (6): a no-trade day between carries `source: no_trade_carry` and the same `trade_id`; a missing trading day FAILs naming it and writes no seed. | proposal; grok X1 [E-10] | a miss → K2's empty-day record is wrong |
| X9 | Supersede day 1's import, re-pair day 2: day 2's executions are the current import's fills only; re-pair an unchanged later day from its fills and its stored `stats_row` rows → identical `derived` and `inputs`. | grok X8; seat X2 [E-4] | superseded fills paired again (double book), or stats rows only recoverable from the kept file bytes → K2 gains a D2 dependency (R2-1 (iii)) |
| X10 | Record Wed stated `flat`, then Tue (a first file) leaving a short open: is Wed re-paired from Tue's book, and does the page show the stated-vs-carried difference? | seat X7 [E-5] | the trigger stays "superseding file" only → the gap R2-1 names remains; its result is round 2's evidence |
| X11 | A resolve with no exit price on a carried trade: CLOSED, `legs = []`, realized `not computed — exit not in any export`, no `IndexError` at `pairing.py:97`. Also gates K3. | seat X8 [E-9] | an exception → the resolved trade is not built through `_trade` |
| X12 | His real export for a no-trade day (the E1 shape) — a hub-run read (L41): does a header-only file parse to 0 executions, `parsed`? | seat X6 [E-10] | it parses → it may also serve as the no-trade input beside `[F-05]`'s row; it does not → the `no_trade` row is the only input |

**Before K3**

| X | Experiment | Named by | Result that changes the design |
|---|---|---|---|
| X13 | After a green X7, put an older `unit_after` of `drc-trades/open_positions` back on disk (the Sync-revert shape, L28); run the next build: the seed hash still matches the database rows, `sync_revert_of` recorded, the unit rewritten from the rows unless he changed a line. | grok X5; gemini X2; seat X4 [E-2] | any reader using the unit text as the next day's book → that reverse parse is removed; the hash design changes |
| X14 | On a copy of his note shape (no `drc-summary`, no `open_positions` section), upsert unit `drc-trades/open_positions` and unit `drc-summary/summary`. | grok X6 [E-8] | the summary upsert refuses an absent section → the evening count is the `open_positions` header only, and `drc-summary/summary` leaves this lane |
| X15 | Dev vault: unit bytes under their heading, his text byte-identical (v2 E3 shape). | proposal | his text changed → K3's unit write is wrong |

## Dissents, verbatim

No seat said `REJECT` or `DO NOT BUILD` (hub `## ESCALATE` closing paragraph). Carried here: wordings a seat offered that v2 does not follow.

- **Gemini, Q3** — "`ADOPT WITH a staged set, the note re-upserts after the DB`" — reasoning, verbatim: "Automatic forward re-pair matches deterministic replay, but vault writes (`upsert_unit`) cannot be rolled back. Failing scenario: DB re-pairs day 2 and day 3; day 2's note upsert succeeds, but day 3's DB update fails. The DB rolls back, leaving day 2's note displaying a new book while the DB retains the old book, breaking L57. A staged set commits the DB first, leaving notes safely stale on failure." — not folded: hub `GM3` DOES NOT HOLD as an objection (the proposal already orders DB first, notes after); `[F-03]` keeps that order.
- **Gemini, WRONG FACTS** — "none" — not folded: hub `GM13` DOES NOT HOLD.
- **The Anthropic seat, Q2** — "The lane's migration is always a NEW numbered `db_migrations` file with its `.rollback.sql`. The number is the desk's at the L68 gate. `0016` is never edited after D1's check. The file creates `"user".drc_stated_books` (kind CHECK `opening`, `resolve`, `no_trade`) and its append-only trigger. It does not change `drc_rows` (see (c))." — not followed: it rests on its (c), not taken; Grok's house wording is taken.
- **The Anthropic seat, Q3** — its wording (1)–(4) (report `:41`) — carried whole into round 2 (`R2-1`), not folded.
- **The Anthropic seat, Q4** — its wording (report `:53`) — not followed: its crash claim is UNVERIFIABLE FROM READS (hub `FC26`) → X3; its Optional list is itself incomplete (hub `FC9`: `Leg.price`, `Trade.avg_entry` also required).
- **The Anthropic seat, Q6** — its wording (report `:64`) — not followed: its `_trade` path claim is UNVERIFIABLE FROM READS (hub `FC24`) → X11; Grok's house wording is taken.
- **The Anthropic seat, (c)** — "The book close and the seed live on the day's EXISTING `day` row (`store.py:187-197`, unique per day `0016:95`). No `book_close` or `seed` kinds, and no `drc_rows.kind` CHECK change. …" (report `:108`, whole) — not followed: it competes with the kinds Grok's Q2 wording and Grok's / Gemini's replay chains are written on (see `[F-15]` in the fold table).
- **The Anthropic seat, (d)** — its wording (report `:111`) — not followed: its last sentence cites `VOICE-v3-FINAL-2026-09-23.md:142`, which is side A of voice R2-2, not the side L28 was amended with (`LAWS.md:166`: side B); Gemini's (d) sentence is taken (`[F-16]`).

## The bar

- **L1 — no assumed book.** Every opening book is a hash-checked carry, his stated word (`opening`), or a no-trade DRC's stored input (`[F-05]`); a first import without a statement does not pair; every §4 row FAILs loud or carries a stored reason. One case is OPEN: an earlier day recorded after a later stated day (`R2-1`) — held by the seat, denied by both houses; round 2 decides whether v2 has an assume path there.
- **L2 — watcher standard.** The re-pair is deterministic code inside the import's request (`[F-03]`, in memory first); no poller, no LLM anywhere in the path.
- **L3 — one path.** One store function for every caller of a statement — page, CLI, widget (`[F-10]`, `[F-16]`); one build writes the unit and the A31 line from the same rows (`[F-11]`); a resolve re-pairs through the same forward re-pair (`[F-06]`).
- **L28 — vault writes.** The unit is marker-bounded, stable-id, upserted by the one build; his text wins; a note failure marks the unit stale and never rolls back the database (`[F-03]`); the Sync-revert clause is X13; his statement is a database input, not a voice-ordered vault edit (`[F-16]`).
- **L40 — one expert per side effect.** `DrcStore` writes every `drc_*` row including `drc_stated_books`; the build writes the unit; the widget's tool asks the store (§3 table).
- **L57 — replay.** Carried figures replay through `seed` → prior `book_close` (hash) → `open_position` rows → `drc_fills`; a stated cost, a no-trade input and a resolve exit are stored rows in `drc_stated_books`; a missing price is stored as `not computed` with its reason (`[F-04]`, `[F-06]`); the stats-row source of a re-paired day is `R2-1` (iii) with X9.
