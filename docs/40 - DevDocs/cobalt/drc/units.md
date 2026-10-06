# `src/cobalt/drc/units.py`

## What it does
The DRC note's Cobalt units, RENDER ONLY (DRC D3). Every function turns stored rows — the build's `build_trade` / `build_day` rows and K's `trade` rows — into a unit body. It reads no file, setting, card or clock and computes no figure the rows do not hold (`build.py` computes and stores).

## The units and their placements (v2 §6)
| section / unit | where | body |
|---|---|---|
| `drc-summary/summary` | directly under his date line (`date_line_placement`) | PARTIAL lines first, then pairing / not re-paired / miss-line notes, P&L, W/L, cards, screenshots, unmapped playbooks |
| `drc-day/no_trade` + `drc-day/voice-no-trades` | directly under the summary (`DAY_PLACEMENT`), no-trade days only | `no trades — <date> · cards written: <n>` and the Cobalt heading `### Why no trades today:`; then HIS blank unit (created once) |
| `drc-day/premarket` | same section | `premarket — sleep … · 1% goal … · meditated / tone / hotkey: not given` |
| `drc-risk/pnl`, `facts`, `risk_parameters` | under `### PnL on the day:` (`PNL_PLACEMENT`; `\s` matches his U+00A0) | `PnL: gross … · net …`; the daily stop + per-trade risk; the sheet-mode line |
| `drc-trades/tickers` | under `### Catalyst + Set Up + Trades` | `trades: <n>` (or `not computed — …`, or `0 — a no-trade day`) |
| `drc-trades/trade-<id>` + `voice-<id>` | same section, one pair per trade | the B-rows block; HIS blank unit next to it (created once, R99) |
| `drc-trades/reconcile` | same section | `legs: not built` / `adjustment pending (legs writer not built)` (R90 / R67, before D5) |
| `drc-rules/rules_check` | the end of the note | `prefill.drc`'s checkboxes + cards with no trade |

A section is ONE marked block (`vaultwrite.markers` refuses a duplicate), so `drc-risk`'s three units sit together under the PnL heading — `facts` cannot also sit above his `How I managed risk` paragraph without a second section name (ESCALATE in the build report). A trade the current rows no longer carry keeps its voice unit; its `trade-<id>` unit is rewritten to ONE line, `orphaned — trade <id> is not in the current trading log`, directly above it (E8).

## What it never writes
A line beginning `Grade:` or `Goal:` (the 09:00 reader's regexes, `[F-23]`); a rules line or engine unit (R101); the `open_positions` unit (K3).

## 2026-09-29 — DRC D3 fix r1 (F-4)
`facts` is now `drc-risk-facts/facts`, the one unit of its OWN section. `RISK_FACTS_PLACEMENT` (`^###\s*How I managed risk`) puts it directly under his `### How I managed risk:` heading, above his paragraph (v2 §13 A9 "facts above his paragraph"). It needs its own section because a section is one marked block and `markers.find_section` refuses a duplicate: `facts` cannot sit above that paragraph while `pnl` stays under `### PnL on the day:`. `drc-risk` keeps `pnl` and `risk_parameters` under the PnL heading. This supersedes the `drc-risk/…facts…` table row and the paragraph after the table.

## 2026-10-04 — DRC K3
New: `OPEN_POSITIONS` (`drc-trades/open_positions`, v3 §2a / §5) and `OPEN_ITEMS` (`drc-open-items/open_positions`, A31 `open items carried forward`), placed by `OPEN_ITEMS_PLACEMENT`, directly after the drc-trades section. `open_positions(day_row)` renders `left open: <n> — tomorrow's import starts from these · book: <first 12 of the close hash>` and one line per position (`<symbol> · <long|short> · <shares> · avg cost … · opened … · day … · <new today|continuing open position> · carried from … · last execution … · <trade_id>`). A flat close reads `left open: 0 — tomorrow starts flat (stated by this DRC)`, and the loud states render as one line. `open_items(day_row)` renders the same list, `none` at 0. `summary` gains ONE line, `open overnight: <n>` (or the loud state). `stale_resolve(id, effect_day)` is the one STALE wording, shared with the page. Every value is a key of `build_day.derived`. This supersedes the `never writes … the open_positions unit (K3)` clause above.

## 2026-10-04 — DRC D5
`reconcile(day_row, builds)` (it took the day row alone before) renders from the stored keys only.

Per matched trade:
- `<label> · card #<id> · running read from <basis>`, then `entry leg: not written — …` when the card has no entry leg (D5-a).
- One line per leg seq: `seq <k> <kind>: DAS <shares>@<price> <time> · Cobalt … (leg #<id>, <flag>, <source>) — <match | fields differ | DAS exit with no Cobalt leg | Cobalt leg with no DAS execution> · held after: DAS <n> · Cobalt <n>`.
- His rows as `history: leg #…`.
- The status: `adjusted to DAS: <k> rows (<ids>)`, `legs match the export — nothing to adjust`, `adjustment not written — <carried trade | re-paired date | dry run (plan only)>` or `nothing written — <refusal>`.
- `running after: <n> · DAS position: <n>` after a write.

`no trade matched a card — nothing to reconcile` when none matched. Every unresolved item (`unresolved_line(item)`: `unresolved: card <id> — <refusal>`) follows, here and at the end of `open_items` (A31). This supersedes the table's `legs: not built` row.

## 2026-10-04 — drc-d5 check
`_diff_line` reads the stored keys `export` / `export_only` and `reconcile` reads `export_held` (no vendor name in an identifier, L31; check A2). The rendered words are unchanged.

## 2026-10-06 — drc-d5 O1 + B2
The `reconcile` docstring names the new status form, `adjusted to DAS: <k> rows (<ids>) — then refused: <refusal>`, which `reconcile._status` stores. The renderer is unchanged.
