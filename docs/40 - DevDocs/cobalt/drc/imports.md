# `src/cobalt/drc/imports.py`

## What it does
The ONE place a DRC input enters Cobalt (DRC D2; v2 §2–§3, v3 §2b / §5).
Two doors, one pipeline (L3):
- **`place(day, files, trade_key=None, *, from_folder=False, now, vault_root)`**
  — the `/drc` upload. `files` is `[(his file name, bytes)]`; there is no
  kind argument (R114).
- **`scan_folder(day_text, *, now, vault_root)`** — the files he drops by
  hand into `1 - Trading/5 - Review/_imports/drc/<date>/` (09-23 R17 (2)).
  It lists the TOP-LEVEL files only (never a sub-folder, `_reference/` or
  a non-date folder; hidden names skipped), marks a file whose name AND
  sha256 already sit on a row for the date `already imported`, and hands
  every other file, as ONE set, to `place(…, from_folder=True)`. The only
  difference: the bytes writer is not called — nothing in the folder is
  written, renamed, moved or deleted.
- **`no_trade(day, *, now)`** — "No trades today" (R93 as v3 `[F-05]`).

Every door is refused inside `market_reset` first (`assert_writable`),
with `refused: market reset 20:00–21:00 — drop again after 21:00` (R102):
nothing read, nothing stored.

## `place()` step by step
1. **Kind by header** (R114): D1's `detect.detect_set` over the drop, and
   `detect_kind` per file. Two files of one kind → the WHOLE drop refused
   `FAILED: <kind> ambiguous — <name 1>, <name 2>`, nothing stored. A
   header matching neither kind → `ignored`, listed, not stored. A header
   failure (both kinds, a duplicated column) → `FAILED`, not stored.
2. **Bytes** (upload only): `VaultWriter("drc.import").write_import_bytes`
   under his own name (a taken name → `<stem>.<n><ext>`; the row records
   the name actually stored).
3. **Parse**: `TradingLogSource().parse(data, day, detection)` — the rows'
   date is the drop's `day` (R17 (3)) — or `StatsLogSource().parse`.
4. **Row**: `DrcStore().record_import(day, result, data, executions)` —
   the ONE writer; its `supersedes` makes the new file the day's current
   one of its kind. A `partial` file is stored and parsed and counts as
   placed (R17 (5)); a `failed` one is stored with its reason and line and
   zero fills.
5. **State** (L2, deterministic, from the stored rows via `event_for`):
   `waiting for: trading log` · `waiting for: stats log` · `READY` ·
   `no-trade` (a placed trading log with ZERO executions — no stats log
   needed).
6. On `READY` / `no-trade`, **the event** on the day's CURRENT
   trading-log import row: `mark_event(id, "pending")`, then THE `[F-17]`
   ROUTE exactly as K1 / K2 built it — `seed_for(day)` (a `PairingError`
   → `failed` with the raise text verbatim, files kept) → `build_day(…,
   seed=None)` + `record_day(…, None)` when no book is stated, else
   `build_day(…, seed=book.positions, resolves=book.resolves)` +
   `record_day(…, book)` (a raise → `failed`, verbatim, `drc_rows`
   unchanged) → `running` → D3's `cobalt.drc.build.run_drc_build(event)`
   → `done`, or `failed` with the reason on ANY exception. Until D3 exists
   the import fails and the event lands `failed: build not built (D3)`.
   A file placed by an EARLIER drop is re-read from the day's folder and
   sha256-checked against its row before it is parsed again (missing or
   changed bytes FAIL — nothing assumed).
7. **The event** `DrcInputsPlaced{date, import_id, stats_import_id,
   screenshot_import_ids, sha256s, partial, kind, orphaned}` is BUILT from
   the stored rows, never stored (L57).

With a `trade_key` the files are screenshots: an empty file or one with
no PNG / JPEG header FAILS; a real image is refused too, `screenshot
binding not built` — `record_import` / `Kind` carry no screenshot and no
`trade_key` on this tree (the D2 build report's ESCALATE). Nothing is
stored or bound. The ORPHAN rule (X13) is built and proven on a
constructed screenshot row: a current screenshot whose `trade_key` the
current computed day no longer carries is listed `orphaned: <file> —
trade <key> not in the current trading log`, on the page and in the
event — never re-bound, never deleted.

## `no_trade()`
Refused on a non-trading date (the one calendar: `day` is a trading day
when `prior_trading_day(day + 1) == day`) and on a date whose current
trading log carries executions (naming the count). Otherwise
`DrcStore().record_stated_book(day, "no_trade", [], via="drc_page",
now=…)` — a refusal of the store shown verbatim — then AMENDED C7's
trigger: `rebuild(effect_day(day, None))` when the day has a current
trading-log import or `has_chain_through(day)` (a raise → `not rebuilt:
<reason>`, the statement kept), else `stated; <day> has no import yet`.
A FILE-LESS no-trade day has no event row in the ruled schema (X-NT): the
build is NOT called, and the page says `no-trade day recorded — its DRC
build waits on the no-trade event home (ESCALATE X-NT)`.

## The page's reads
`day_view(day, *, cards, vault_root)` → `DayView`, READS ONLY: the
morning line (`seed_for` → `Starting book from DRC <P>: <n> open
(<symbols>)`, each position `opened: <date | not stated>`; `None` →
`state your opening book for <D> — until the form ships: cobalt drc
state-book --opening <D> …`; a raise verbatim, plus `No prior DRC for <P>
— import it, record its no-trade DRC, or state your book` when it names a
missing prior day), the R51 line (`stated_difference`), the unpaired /
stale / not-re-paired notes read from the `day` row, the current files,
the orphans, the folder's files not on a row, the counts, and the status
line. `render_status(view)` is that one line.

## 2026-09-28 — DRC D2 fix r1
`docs/30 - Design/DRC-D2-SEAM-2026-09-25.md` §1 / §2 (R64) and the
round-1 check's F-1. THE EVENT: `DrcInputsPlaced` gains `event_id`,
`stated_book_id`, `stated_book_sha256`, `seed_from_day`,
`seed_from_book_sha256`; `import_id` is optional; the model rule (exactly
one source; a stated source is `no_trade` with no stats, screenshots,
partial or file sha256s and a hex-64 statement hash) is a validator.
`_fire` fires through `DrcStore.fire_event(day, import_id=…)` and moves
by the event id, its order unchanged, `done` storing the note path; ANY
exception after `pending` lands `failed` — the named ones verbatim, any
other as `<step> — <Type>: <message>` — never left `pending` /
`running`. THE FILE-LESS DAY: **`no_trade_event(day, stated_book_id, *,
now=None)`** — `fire_event(stated_book_id=…)` → the rebuild (a refusal →
`failed`, `not rebuilt: …`, the statement kept) → `running` → the build
→ `done` | `failed`; `no_trade` calls it for a day with no trading log (a
zero-execution log's event stays its import's), and so does the CLI's
`state-book --no-trade --apply`. `NO_TRADE_WAITS` is gone; `_state` is
`no-trade` for a file-less day with a current `no_trade` statement; the
page's `done` line reads the stored note path for both day types. THE
SCREENSHOT DROP: a PNG / JPEG on a trade of the day's current computed
trading log → the bytes writer, then `DrcStore.record_screenshot`; a key
not in the log is `FAILED: trade <key> is not in the current trading
log`, nothing bound or written; a READY day re-fires. `SCREENSHOT_NOT_BUILT`
is gone.

## 2026-09-28 — DRC D2 fix r2
The round-2 check's fix rows (`drc-d2-fix-r1-check-2026-09-25.md`). A
BUILD THAT RETURNS NO NOTE PATH (F-10): in `_fire` and `no_trade_event`,
D3's build returning `None` or an empty path lands the event `failed`
through the one `fail()` with the step `build` and
**`NO_NOTE_PATH`** (`the build returned no note path (None) — never done
(L1)`), never `done` — `done` is written only with a non-empty note path
(the `drc_events` CHECK's `done` ⇔ `note_path` contract). A NOT-COMPUTED
DAY'S SCREENSHOTS (F-11): `day_view` lists each current screenshot binding
in the page's notes as `screenshot <name> — trade <key>: not checked,
pairing not computed`; `_orphans`, `event.orphaned` and the counts are
unchanged (X13's orphan lines stay a computed day's).

## Tests
`tests/cobalt/test_drc_imports.py` (offline, an in-memory `DrcStore`
double), `tests/cobalt/test_drc_imports_db.py` (with-DB, inside
`test_drc_store.py`'s rolled-back migration transaction),
`tests/cobalt/test_drc_d2_experiments.py` (E5 / E11 / X13 / X-NT),
`tests/cobalt/test_drc_d2_fix_r1.py` / `test_drc_d2_fix_r1_db.py` /
`test_drc_d2_fix_r1_runs.py` (D2 fix r1), `test_drc_d2_fix_r2.py` /
`test_drc_d2_fix_r2_db.py` (D2 fix r2).
