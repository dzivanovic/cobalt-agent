# `src/cobalt/prefill/daily.py`

## What it does
Morning Daily Note prefill. **Rewritten Slice 2.1 (2026-08-31)** from
Dejan's review of the first live note: fills IN PLACE inside his actual
section layout, never appends a block below it. Renders
`configs/cobalt/templates/daily.md.j2` (his layout verbatim, Cobalt
slots inline) if today's note doesn't exist; otherwise edits the
existing file's three Cobalt slots independently:
- **rules** — the config-driven, mode-aware rules checkbox list +
  sheet-mode line + mantras. Anchor: the line "I WILL NOT TOLERATE THE
  MISTAKE OF HAVING MORE THAN 3 LOSSES IN A ROW IN A TRADING DAY" —
  inserted right after it.
- **trading** — SPY/QQQ/IWM rows only, under "### Trading". VIX/BTC are
  never touched by this module at all (always Dejan's, always blank in
  a fresh note — no "n/a (manual)" text anymore).
- **market_calendar** — under "### Market Calendar:".

Each slot: if its `<!-- cobalt-slot:NAME -->` marker is already present
anywhere in the file, skip (already handled). Else, if the slot's
current content is blank (or a prior unmarked FAILED attempt —
retryable), fill it and add the marker. Else (Dejan already has real
content there, e.g. he hand-typed the Trading table this morning before
Cobalt ran) skip, report, and add NO marker — leaves the door open if
he ever clears it. An anchor that can't be found at all (`### Trading`
missing, etc.) raises `SlotAnchorNotFound` for the WHOLE run — the
edit plan is built entirely in memory first, so a failure never leaves
a partially-edited file on disk. The trading slot is per-row: a marker
is only added if at least one of SPY/QQQ/IWM was actually blank and
got filled; if all three were already Dejan's, nothing is written and
no marker appears (a later run keeps re-checking, cheaply, correctly).

Market/calendar fetch failures still render `FAILED: <reason>` text
into the slot content, deliberately WITHOUT setting the marker, so a
later run retries them (fail-loud without permanently blocking retry).

## Key functions/classes
- `format_market_row(ticker, rows, error) -> (col2, col3)` — one of
  SPY/QQQ/IWM only.
- `format_calendar_block(economic, earnings, error) -> str`.
- `format_sizing_rule_text(text, sheet_modes_cfg) -> str` — content-
  detected (regex on "B = $N, A = $N"), not tied to a rule id/position:
  splices in `"B = $30 half / $60 full, A = $70 half / $135 full"`
  (from `aset.config.load_sheet_modes_config()`, the SAME source ASET's
  sheet already uses) wherever that pattern appears; every other rule's
  text is untouched. `apply_mode_aware_sizing(rules, cfg)` maps this
  over a rule list (via `RuleItem.model_copy`, never mutates the input).
- `format_rules_checkbox_block(rules) -> str` — ONE tagged checkbox
  list, `- [ ] {text} #{category}` — the rules ARE the adherence boxes
  now; no separate read-only list, no separate adherence list. Also
  used by `drc.py` for its own "copied from the morning note" checklist.
- `format_mantras_block(rules_cfg) -> str`.
- `format_mode_hint(cards) -> str` — "if aset exposes the current mode
  at run time, show it" (Dejan's item 2): the only real runtime "current
  mode" signal aset has is today's own cards (`AsetStore.for_date`) —
  empty string if none yet (true most mornings at 05:15).
- `_fill_rules_slot` / `_fill_trading_slot` / `_fill_market_calendar_slot`
  — the three per-slot in-place editors, each taking/returning
  `list[str]` (line-based, not append-only — see module docstring).
  `SlotFillPlan` accumulates `filled`/`skipped` for the result/CLI report.
- `SlotAnchorNotFound(RuntimeError)` — an expected heading/anchor line
  is missing from an existing note; aborts the whole run.
- `run_daily_prefill(when=None) -> DailyPrefillResult` — the
  orchestrator. `action` is `"created" | "filled" | "skipped_idempotent"`;
  `filled_slots`/`skipped_slots` name exactly what happened, for the CLI
  to report ("a non-empty slot is skipped and reported").

## Data flow in/out
**In:** `prefill.market.fetch_market_table`, `prefill.calendar.fetch_*`,
`prefill.rules_gen.regenerate_rules_config` (regenerates
`configs/cobalt/rules.yaml` from the vault's Rules.md on every run —
not the old static `load_rules_config`), `aset.config.load_config()
.daily_note` + `load_sheet_modes_config()`, `aset.store.AsetStore.for_date`
(best-effort, for the mode hint only — a DB error there is swallowed,
not a run failure). **Out:** a written/edited file under the resolved
vault root, or a raised `VaultWriteError`/`RulesSourceError`/
`SlotAnchorNotFound`/`VaultConfigError`.

## Config it reads
`configs/dev/aset*.yaml` (daily_notes_dir/filename_pattern, db_name),
`configs/cobalt/aset.yaml` (sheet-mode dollars, via `load_sheet_modes_config`),
the vault's `1 - Trading/5 - Review/Rules.md` (via `regenerate_rules_config`,
NOT the committed `rules.yaml` directly — that's now a generated cache),
`configs/cobalt/templates/daily.md.j2`.
