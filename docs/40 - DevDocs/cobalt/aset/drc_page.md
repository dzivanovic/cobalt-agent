# `src/cobalt/aset/drc_page.py`

## What it does
The HTML of the `/drc` page (DRC D2-4) — the ASET app's third page
template, beside the sheet (`web._render`) and the radar
(`radar_panel`). Pure rendering: `render(view, result=None, *,
cards_error=None, css="")` turns a `cobalt.drc.imports.DayView` (and,
after an action, its `PlaceResult`) into the page; `failed_page(message,
css)` is the loud FAILED page. It reads, computes and writes nothing.

## What the page shows
- the date picker; THIS ACTION (the refusal / message, each file's line,
  any orphan, the action's status line) when an action just ran;
- the day's status line, then the event line;
- STARTING BOOK: the morning line and the R51 line; the unpaired / stale
  notes;
- FILES: each current file — `✓ … parsed`, `… PARTIAL — missing: …`
  (loud), `FAILED: … — <reason>`, orphans;
- COUNTS (`not given` for an unknown value; a cards read that failed is a
  FAILED line, never a blank);
- TRADES: one drop zone per trade (drop, click or paste an image — the
  trade-reporter interaction pattern only), posting `/drc/import` with its
  `trade_key`;
- DROP: the multi-file upload (no kind picker, R114), the folder's
  not-yet-imported files, the scan button and "No trades today".

Attribute values are escaped with quotes (`_e`); text nodes escape `<`,
`>`, `&` only (`_t`), so a line reads exactly as the store returned it.
