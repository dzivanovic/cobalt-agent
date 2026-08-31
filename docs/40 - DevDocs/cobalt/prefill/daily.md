# `src/cobalt/prefill/daily.py`

## What it does
Morning Daily Note prefill. Renders `configs/cobalt/templates/
daily.md.j2` (Daily.md's structure verbatim, Templater `{{ }}` prompts
replaced by prefilled fields) if today's note doesn't exist yet;
otherwise appends a fenced "Cobalt Rules Check"/"Cobalt Prefill" block,
guarded by an `<!-- cobalt-prefill:daily:<date> -->` HTML-comment marker
so a second same-day run is a no-op, never a duplicate append. Never
reads existing content for mutation — only to check for that marker.

Market table (SPY/QQQ/IWM) and calendar fetches each fail independently
(one doesn't block the other); a failure renders FAILED cells + a
`> ⚠️` banner line, never a blank. VIX/BTC always render "n/a (manual)".

## Key functions/classes
- `format_market_cells(rows, error) -> dict` — table cell strings,
  pure/testable.
- `format_calendar_block(economic, earnings, error) -> str`.
- `format_rules_blocks(rules_cfg) -> (rules_block, adherence_block, mantras_block)`
  — also reused by `drc.py` for its own rule-adherence checklist
  ("copied from the morning note", i.e. the same config-driven source).
- `build_context(...) -> dict` — combines the above for the Jinja render.
- `run_daily_prefill(when=None) -> DailyPrefillResult` — the orchestrator;
  `action` is `"created" | "appended" | "skipped_idempotent"`.

## Data flow in/out
**In:** `prefill.market.fetch_market_table`, `prefill.calendar.fetch_*`,
`prefill.config.load_rules_config`, `aset.config.load_config().daily_note`
(the ONE daily-notes path, not duplicated here). **Out:** a written/
appended file under the resolved vault root, or a `VaultWriteError`/
`PrefillConfigError`/`VaultConfigError` raised loudly.

## Config it reads
`configs/dev/aset*.yaml` (daily_notes_dir/filename_pattern, via
`aset.config`), `configs/cobalt/rules.yaml`,
`configs/cobalt/templates/daily.md.j2`.
