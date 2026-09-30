# `src/cobalt/prefill/trade_note.py`

## What it does
Creates/updates "1 - Trading/2 - Trades/&lt;Trade-...&gt;.md" for every
computed ASET card, using the Individual Trade Template's frontmatter
shape, so the daily note's Trade Execution dataview table lights up.
Cobalt owns exactly five frontmatter fields (date, symbol, direction,
stop_price, entry_price); everything else (exit_price, entry_time,
exit_time, profit_loss, strategy, RVOL) is created blank and, on any
later re-run against the same filename, is read back and preserved
verbatim — only the five owned keys refresh. RVOL is always blank
today: ASET's sizing engine doesn't fetch it (see `aset/prefill.py`),
so blank is the honest state, not a guess.

## Key functions/classes
- `upsert_trade_note(result, when, prefill_paths) -> (Path, "created" | "updated")`.
- `_cobalt_fields`, `_render_frontmatter`, `_render_body` — pure formatting.
- `_split_frontmatter(content) -> (dict | None, body_str)` — YAML
  frontmatter parse for the update path; `None` fm on a file with no
  recognizable frontmatter block raises `VaultWriteError` rather than
  guessing how to merge into it.

## Data flow in/out
**In:** an `aset.models.SizingResult` + its card timestamp + the
resolved trades directory (`vault_writer.resolve_target`). **Out:** a
created or in-place-frontmatter-updated file, or `VaultWriteError`.

## Config it reads
`configs/cobalt/prefill.yaml` (trades_dir, trade_filename_pattern) via
the caller-supplied `PrefillPathsConfig`.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

`FIELD_ORDER` carries `trade_def` where it carried `strategy` (ADR-0008
D4): a new note gets the trade's ID, blank, as DEJAN'S field. Rendered
UNQUOTED alongside `date` and `symbol` — the migration writes the slug
unquoted into every existing note, so quoting it on the next Cobalt write
would make his line and Cobalt's differ and record an override on a value
nobody changed.

`frontmatter_span` and `_split_frontmatter` moved to
`vaultwrite/frontmatter.py` and are imported from there.

---

## 2026-09-29 — S3 exits C4: the trade note at the fill (F22, v3 §7)

ONE writer for both origins (L3). `upsert_trade_note(card, when, prefill_paths, *, entry_price, fills=None, legs_section=False, create_only=False, writer=None, db_name=None, dry_run=False) -> (Path, "created" | "updated")` takes the CARD (a mapping with `ticker`, `direction`, `stop`), not a `SizingResult`:
- `/size` (O4 A) passes the card's values, the sizing time and the planned entry. The sizing note is byte-for-byte as before.
- The FILL passes the card row, the FILLED transition time in ET and the entry leg's price. The new note carries, after his template body (`_render_body`, the code copy, unchanged — X14 proved it equal to his template's shape), ONE Cobalt section `cobalt-legs` (`<!-- cobalt:section cobalt-legs -->`), whose units are `leg-<seq>`.
- `create_only` (the fill event): a file already at the path is another card's (X16: two cards, one ticker, one second). It raises `TradeNoteRefused` and is never merged.

His keys — O5 / O6 = A (09-28 R35 (3)): `his_fills(card, legs)` gives one value per key, from one source each:
- `entry_time` ← the FILLED transition time (ET, `%Y-%m-%d %H:%M`);
- `exit_time` ← the CLOSED transition time (ET);
- `exit_price` ← the price of the one current exit leg, when the card CLOSED through exactly ONE `confirmed` exit leg;
- `trade_def` ← the card's `trade_def_slug` (a radar card; a manual card has none).

The merge sets such a key ONLY when the file's value is blank (`key:`, `""`, null). A value he wrote, or one Cobalt filled earlier, is kept. A key absent from his file is never added back: the merge renders only the keys present, `_render_frontmatter(…, every_key=False)`. `profit_loss` and `RVOL` are never written. Cobalt's five keys refresh as before.

The fill event, the units and the retry:
- `write_card_note(card_id, *, retry=False, …) -> CardNoteResult(path, relative, action, units)`, called after the fill's commit and by `cobalt cards trade-note`:
  - the session gate first;
  - then `AsetStore.card_for_note` and `cards.legs.read_position` (`legs_current_v`);
  - the path from the FILLED time and `trade_filename_pattern`, claimed through `AsetStore.set_trade_note_path` (a path another card holds is refused);
  - `upsert_trade_note` (the fill: `create_only`; the retry: create or update);
  - one `upsert_unit(path, 'cobalt-legs', 'leg-<seq>', render_leg_line(leg))` per current leg.
  - Any failure after the gate sets `trade_note_path` NULL and re-raises.
- `write_leg_unit(card_id, leg_id, *, closed, …)`: after a leg / correction / held-count commit, rewrites the `leg-<seq>` unit of that leg. A correction rewrites the SAME unit.
  - `trade_note_path` NULL or its file absent → `TradeNoteRefused`, nothing written.
  - `closed` also runs `upsert_trade_note`, so his blank exit keys are filled.
- `render_leg_line(leg)`: `<exit|entry> <preset> · <shares> sh @ <price> · <HH:MM> · <estimated|confirmed>`. An entry has no preset (`entry · …`). A held-count row is `holding <held_stated> (stated) · <HH:MM>`. HH:MM is the leg's `at` in ET.

Human wins through `VaultWriter`'s merge (an override row). The DB leg is never changed from the note (no reverse parse). X3's measured limit (human wins ONCE — the next write of that unit replaces his line) is the writer's, and is ESCALATEd in the C4 build report.

Tests: `tests/cobalt/test_s3_c4_trade_note_offline.py`, `tests/cobalt/test_s3_c4_trade_note_db.py`, `tests/cobalt/test_s3_c4_experiments.py` (X14 / X3 / X16 / X18; the stripped real-shape template fixture is `tests/fixtures/trade_note/individual-trade-template.stripped.md`).

---

## 2026-09-29 — S3 exits C4 fix r1

The test guard: `tests/cobalt/conftest.py` autouse fixture `trade_note_path_guard` wraps this module's `resolve_target`; a path outside the pytest base temp raises before any read or write and fails the test at teardown (the web note helpers swallow exceptions). A test that writes a trade note gets a `tmp_path` vault through `trade_note_support.make_vault` (`panel_world` does; `note_world` reuses it).

## 2026-09-29 — S3 exits C4 fix r2

The frontmatter merge keeps his raw lines: `_merge_frontmatter_lines` writes an existing note's block back line by line, in his order, byte for byte; only Cobalt's five and a blank key of his that has a fill are rendered (a block it cannot map line by line onto its keys is refused, nothing written).
