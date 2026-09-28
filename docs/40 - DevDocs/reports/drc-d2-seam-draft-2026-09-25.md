# DRC D2 seam draft — 2026-09-25

Seat: `drc-d2-seam-draft-0925` (Opus 5.5, `claude-opus-5-5`). Prompt: `docs/40 - DevDocs/prompts/2026-09-25/30-draft-drc-d2-seam.md`. Authorization: `grep -n "^| R61 " cto-2026-09-25.md` → `70:| R61 | 10:03 ET | … 30-draft-drc-d2-seam.md …` (PASS). Started `Fri Sep 25 10:04:02 EDT 2026`; seam document written `10:11:46 EDT`. Tip read: `6777c463`.

## §0 Headline
- **Written:** the seam document `docs/30 - Design/DRC-D2-SEAM-2026-09-25.md` (40,836 B). Nothing committed, nothing run against a DB, nothing launched.
- **X-NT:** option (B). ONE `"user".drc_events` table holds the event for both day types; its source is the trading-log import or the current `no_trade` statement. `drc_imports.event_*` is dropped. The migration is the desk's next free number, sketched. It builds in the D2 fix round (row S-1).
- **Screenshot writer:** option (A′), a separate `DrcStore.record_screenshot`, with `Kind` untouched. It builds in the same D2 fix round (row S-2).
- **ESCALATE 4.** One of them moves a v2 rule: `[F-35]`'s placement sentence (the desk's call).

## L74
One block arrived appended to a tool result (the Read of this prompt, 10:04 ET). It was a system-reminder asking that commit messages end with a `Claude-Session:` line, and it named a file-send tool. I recorded it here as DATA and did not follow it. This run makes no commit and sends no file.

## READS
| source | lines read |
|---|---|
| `LAWS.md` | in full (L1–L76) |
| D2 build report (branch, `10163d51`) | whole: §0, E1 X-NT `:94`, `:101`, SEAM FOR D3 `:200`–`:209`, FOR K3 `:211`–`:216`, ESCALATE `:221`–`:236` |
| `07-drc-d2-build.md` | `:45` (D2-3), `:46` (D2-3b), `:47` (D2-3c), `:104`–`:108`, `:166`–`:170` |
| `09-drc-d3-build.md` | `:1`, `:12`, `:27`–`:28`, `:37`, `:44`, `:48`, `:87`–`:88`, `:143`; grep of every `0019` / `screenshot` / `event_for` line |
| v2 `DRC-AUTOMATION-v2-2026-09-22.md` | `:66`, `:76`–`:82`, `:89`, `:119`, `:205`, `:211`, `:222`–`:223`, `:321` |
| v3 `DRC-OVERNIGHT-POSITION-v3-2026-09-24.md` | `:90`, `:96`–`:99`, `:133`–`:139`, `:227`, `:239`, `:247`–`:248`, `:268` |
| `0016_drc.sql` @ tip | `:1`–`:95` |
| `0018_drc_stated_books.sql` @ tip | `:1`–`:63` |
| `store.py` @ tip | `:97`–`:121`, `:172`–`:895` (`record_import`, `record_day`, `rebuild`, `effect_day`, `EVENT_MOVES`, `mark_event`, `event_for`, `_current_import`, `_no_trade_id`, `_repair`, `_no_trade_seed`, `_commit`, `_rows`, `seed_for`) |
| `imports.py` @ tip | `:30`–`:95`, `:128`–`:175`, `:218`–`:300`, `:300`–`:392`, `:405`–`:600`, `:640`–`:721` |
| `models.py` @ tip | `:38`–`:52` (`Kind`) |
| `detect.py` / `cli.py` / `web.py` / `writer.py` @ tip | grep hits: `detect.py:143`, `:152`, `:160`; `cli.py:5`, `:99`–`:100`; `web.py:1567`–`:1577`; `writer.py:312`, `:416`, `:499`, `:1031`–`:1049`, `:1093` |
| K2 fix r1 report (branch) | `## SEAM FOR D2`, `## FOR K3` (`:172`–`:192`) |
| `cto-2026-09-25.md` | R59, R61 |

## THE TWO READINGS
**ITEM 1: option (B), one `drc_events` table.**
- **The event row.** Every `DrcInputsPlaced` state lives on one `drc_events` row, keyed by its source: the current trading-log import, or the current `drc_stated_books` row with `kind = 'no_trade'` (v3 `[F-05]`, `:99`, `:268`).
- **Why a new table.** The existing homes are closed: `mark_event` accepts only a trading log (`store.py:440`), `drc_stated_books` is append-only (`0018:49`–`:51`), and `drc_rows` is rewritten on every re-pair (`store.py:758`).
- **The old columns go.** `drc_imports.event_*` (`0016:35`–`:37`, `:42`) is dropped in the same migration. It never shipped, so the state keeps one home (L3).
- **The store gains** `fire_event` (the only way to `pending`). `mark_event` is re-keyed by event id and stores `note_path` on `done`. `event_for` picks import-first, then statement.
- **The event gains** `event_id`, `stated_book_id`, `stated_book_sha256`, and the seed row's `from_day` / `from_book_sha256` (L57). `import_id` becomes optional.
- **The file-less path.** A new `imports.no_trade_event` runs pending → `rebuild(effect_day)` → running → `run_drc_build` → done | failed. `no_trade` calls it (replacing `NO_TRADE_WAITS`, `imports.py:87`, `:566`, `:683`), and so does the CLI's `--no-trade --apply` (`cli.py:99`), so there is one path (L3).
- **D3's view.** D3 sees the same entry with `import_id = None`.
- **Chunk.** The D2 fix round, never `09` (`09:48`).

**ITEM 2: option (A′), `DrcStore.record_screenshot`.**
- **The writer.** `record_screenshot(day, name, data, trade_key)` is the ONE writer of `kind = 'screenshot'` rows (`0016:26`, `:29`, `:39`). It supersedes by day + key.
- **The drop zone** (`imports.py:361`–`:374`) is un-refused. The key must be a trade of the current computed log; the bytes go through `write_import_bytes`; a READY day re-fires.
- **`Kind` stays unchanged.** `detect_set` iterates `Kind` and names every missing member absent (`detect.py:143`, `:152`, `:160`), so adding `SCREENSHOT` would change both-placed.
- **ASK DESK 2: confirmed as built.** A hand-dropped image stays `ignored`: no header names a trade (R114, v2 `:89`). It binds only through the drop zone's own write.
- **D3's seam.** `screenshot_import_ids`, `orphaned`, B13 embeds only non-orphaned bound rows, and zero rows → no embed plus `0 / <n>`.
- **Chunk.** The same D2 fix round.

**Records.**
- **ESC 11:** ITEM 1's home stores the note path, `drc_events.note_path`, required on `done`. D3 still derives the path at write time (`09:37`).
- **ESC 12:** unchanged and correct. The doors are gated at their start, and gating `mark_event` would strand runs in `running` (L18).
- **ESC 13:** correct, and stated as a rule. Dot-names are the writer's own temp files (`writer.py:1093`) and OS files; R114's "any name" governs visible files.

## ALTERNATIVES REJECTED
| item | option | clause |
|---|---|---|
| 1 | (A) columns on `drc_stated_books` | L3: two homes for one state machine; breaks v3's append-only rule (`0018:12`, `:49`–`:51`) as well as `[F-35]` |
| 1 | (C) state on the `day` row's `derived` | L18 / `[F-08]`: `pending` precedes the `day` row (`imports.py:417` before `:439`–`:448`); a refused route leaves no row for `failed` (`store.py:313`–`:317`, `:344`–`:346`); `_commit`'s per-day DELETE (`store.py:758`) erases state on every forward re-pair |
| 1 | (D) `drc_imports` kind `no_trade`, no bytes | L1: a synthetic file row in a table that holds one row per dropped file (`0016:13`), with `parse_status` claiming `parsed`; L3: the input stored twice; L57: a restated `no_trade` leaves the row naming a superseded input |
| 1 | (E) no stored event | L18 "no fire-and-forget"; v2 `[F-08]` (`:77`) "A dead request leaves `failed`, never `done`" |
| 2 | (A) `Kind.SCREENSHOT` + `record_import(trade_key)` | breaks D1's `detect_set` (`detect.py:143`, `:152`, `:160`); `Kind` = "what a dropped file IS, by header" (`models.py:44`) |
| 2 | (B) D3 carries it | `09:48` NOT IN D3 ("the import page and the event state machine (D2)"); L3 / L40 (a second importer) |
| 2 | (C) a later chunk | L1: D3's summary `0 / <n>` would read as "none dropped" while none can be; needs a `09:37` change and a later chunk. It is the FALLBACK only (ESCALATE 2) |

## OWNER ITEMS
NONE.

## ESCALATE
1. **v2 `[F-35]`'s placement sentence moves** (`v2:76`, mirrored in `0016_drc.sql:3`–`:5`). The event state moves from `drc_imports` to one `drc_events` table. This is the ONE reading, and adopting or returning it is the desk's call. If returned, `09:28` is filled `NOT SETTLED`.
2. **Seam rows S-1 / S-2 in a D2 fix round.** This reads L75 as governing check findings, not desk-issued seam rows. If the desk refuses that reading, S-1 becomes its own D2 seam chunk before `09`, and S-2 falls back to option (C) with a `09:37` line change.
3. **Migration order.** `09:44` pins `0019` for D3. S-1's migration is "the desk's next free number". The desk orders the two and re-points `09:1`, `:44`, `:100`, `:128`, `:143`, `:158`, `:161` for whichever file moves. The absence probe becomes short by 5.
4. **Carried, not changed.** A first-ever recorded day that is a no-trade day, with no import and no chain, keeps `stated; <D> has no import yet` (`imports.py:567`). AMENDED C7's trigger does not rebuild, so no `day` row and no event, and R93 is unmet for that day. The remedy is a K-lane item, not this seam.

DRC D2 SEAM DRAFTED · X-NT home: B one drc_events table · migration: next free, sketched · builds in: D2 fix round · screenshot writer: A′ D2 fix round · owner items: 0 · ESCALATE: 4
