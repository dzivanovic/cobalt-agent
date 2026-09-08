# Open questions — Trade Radar Card v0.1

## Product / behaviour
1. **Per-dot weights.** Should conviction weight categories (e.g. Catalyst 2.0, Rel-vol 1.5, Spread 1.0)? Where are weights configured — global, per setup family, per `trade_def`? UI is ready (score is opaque).
2. **Scale-out presets.** ½ / ⅓ / flat are DAS-literal. Do we want plan-driven presets (⅓ at 1R, ⅓ at 2R, runner) that light up as price reaches each level, or per-grade defaults (C-trades take profit faster)?
3. **Hotkey naming.** Card renders `{DAYMODE}-{KEY}-{SIDE}` (e.g. `HALF-B-LONG`). Confirm against the real DAS hotkey file; is there a per-`trade_def` prefix?
4. **Plan branch slot.** Header reserves `plan branch · empty`. What does a populated branch look like — alternate trigger/stop pairs? Separate cards?
5. **Judgment dots — which variables?** Currently Tape and Conviction. Should judgment scores persist per ticker across the day, and do they expire?
6. **Stop override authority.** When the trader edits the stop, does Cobalt keep proposing its own (and show drift), or does the trader's stop become the plan until reset?
7. **Attempt counter reset.** Per ticker per day is assumed. Does a `passed` count as an attempt? Does a `missed` (triggered while disarmed)?
8. **Trade health thresholds.** What turns a variable amber vs red (e.g. rel-vol < 60 % of entry = ↓, < 40 % = ↓↓)? Needs a rule per category.
9. **Expired.** Is there a time window per `trade_def` after which a WATCH card expires, and should the card show a countdown?

## Surface / layout
10. **Host.** Obsidian plugin pane vs. browser window. Obsidian implies a single-column ~600–750 px pane; the ladder handles that, but a native plugin decides scroll, focus, and hotkey capture.
11. **Detail column contents.** Reserved *notes · chart · news*. Which come first, and does the chart need to be live (TradingView embed) or a static snapshot?
12. **Terminal section on desktop.** Currently below the ladder in the mock. In the real pane: collapsed footer, separate tab, or scroll?
13. **Phone → desktop handoff.** If the trader taps ACCEPT on the phone, does the desktop card arm? Assumes shared state.

## Data / integration
14. **Live data source** for `last`, rel-vol, spread, and health re-checks — polling interval and what "stale" looks like on the card.
15. **`enabled_grades` source.** Per `trade_def` is assumed; confirm whether day-mode or account state can further restrict it.
16. **Fill event.** The fill recompute assumes a single fill price. Partial fills / averaging?

## Deferred (not blocking handoff)
- Per-dot weights UI.
- ½ / ⅓ glyph legibility at 11 px (trader accepted as-is; alternative: spell out HALF / THIRD).
- Fluid breakpoints below 560 px card width between phone (366 px) and desktop.
