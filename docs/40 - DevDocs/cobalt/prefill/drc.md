# `src/cobalt/prefill/drc.py`

## What it does
Evening DRC prefill. Pulls the day's cards (`AsetStore.for_date`,
America/New_York day boundary), groups by ticker in entry order, and
renders a Catalyst+Set-Up+Trade scaffold per entry: card values (grade,
entry, stop, shares, risk budget), a FILL UPDATE lookup, the re-entry
rule's "new written information" prompt on entry #2, a stand-down
notice on entry #3+, and an excitement-audit question if the matched
trade note's `strategy` is reversion-tagged
(`configs/cobalt/strategies.yaml`). Risk Parameters render from today's
actual sheet-mode cards, replacing DRC.md's stale R-multiple line. Same
create-vs-append-with-idempotency-marker principle as daily.py.

Cards don't carry Catalyst/Set-Up text or a strategy tag — those are
Dejan's (Trade Ideas table, trade-note `strategy` field), so per-entry
Catalyst/Set Up/Trade Notes lines stay blank prompts, only the
numeric/structural facts are prefilled.

## Key functions/classes
- `parse_fill_updates(daily_note_text) -> dict[naive_local_iso, fields]`
  — regex-parses `\`\`\`aset-fill` blocks (read-only; never touches the
  daily note itself).
- `find_trade_note_for_card(trades_dir, ticker, created_at) -> Path | None`
  — NEAREST-timestamp match within `FILL_MATCH_TOLERANCE_SECONDS` (30s).
  Exact-second matching would under-match: `AsetStore.save()`'s DB
  `created_at` and `save_card()`'s Python `when` (used for the trade
  note's own filename) are two separate clock reads a beat apart.
- `format_risk_parameters(cards, sheet_modes_cfg) -> str`.
- `format_tickers_block(grouped_entries) -> str`.
- `run_drc_prefill(for_date_=None) -> DrcPrefillResult`.

**Slice 2.1 (2026-08-31):** the rules block now comes from
`rules_gen.regenerate_rules_config()` (Rules.md is the source, not the
static `rules.yaml`) and renders via `daily.format_rules_checkbox_block`
+ `daily.apply_mode_aware_sizing` — the SAME single merged, tagged,
mode-aware checklist the morning note shows (no more separate
"Guardian rules" + "Rule adherence" split — see `daily.py`'s own
DevDoc). "Copied from the morning note's checklist" is now literally
true byte-for-byte, not just in spirit.

## Data flow in/out
**In:** `AsetStore.for_date`, the source day's daily note (read-only,
for fill lookups), matched trade notes (read-only, for strategy
lookups), `prefill.config` (rules/strategies/paths),
`aset.config.load_sheet_modes_config`. **Out:** a created/appended DRC
note under the resolved vault root, or a raised error.

## Config it reads
`configs/cobalt/prefill.yaml`, `rules.yaml`, `strategies.yaml`,
`configs/cobalt/aset.yaml` (sheet-mode dollar figures),
`configs/cobalt/templates/drc.md.j2`.
