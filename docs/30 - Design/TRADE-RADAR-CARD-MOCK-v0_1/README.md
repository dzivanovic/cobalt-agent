# TRADE-RADAR-CARD-MOCK v0.1

Design package for the Cobalt Trade Radar card — a four-state mission-control card for day traders, hosted in Obsidian (or a browser window) beside DAS.

```
card-spec.md          states, sizes, fields, owners, math, data contract
decisions.md          what was decided and why (numbered)
open-questions.md     unresolved product / layout / integration items
prototype.html        self-contained interactive mock (open in any browser, offline)
states/
  phone-01-watch.png
  phone-02-armed.png
  phone-03-triggered-alert.png      ← the push alert
  phone-04-in-trade.png
  desktop-ladder-composite.png      ← ladder, #1 + #2 open, detail column
  desktop-terminal-states.png
source/
  Trade Radar.dc.html               surface: sample data, ranking, ladder, terminal, spec sheet
  RadarCard.dc.html                 the card component (all states / sizes)
  support.js                        runtime for the .dc.html files
```

## Using the prototype
- Top-right tabs preview the leader (#1) in each state.
- Click any ladder strip to expand/collapse; `↑` promotes to #2; `collapse all` / `top 2`.
- Tap a hollow semaphore dot → score 1–10; ranks update live.
- Stop field: type a value, Enter commits, Esc cancels; `↺` restores Cobalt's stop.
- In-trade: pick a trail, scale out (½ / ⅓ / flat / typed), watch health pills.
- Tweaks (host panel): clock, day mode, daily stop, degraded-stop demo, radar width (620–1600 px) to test fit beside DAS.

## Sample data
Eight tickers (ROST, TSLA, MSTR, BJ, COIN, BABA, MRNA, FLO) with fabricated but internally consistent levels. Not market data.

## Version
v0.1 — 2026-09-04. Design mock only; no live data, no DAS integration.
