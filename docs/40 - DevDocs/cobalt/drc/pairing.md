# `src/cobalt/drc/pairing.py`

## What it does
This module turns one import day's executions into trades, exit legs and
the positions left open. It then attaches each stats-log row to the ONE
trade it names. There is one pairing function (L3), and every derived
figure carries `FN_VERSION` (`drc.pairing/1`) when stored (L57).

## `pair_day(executions, day, seed=())`
- **FIFO, per symbol, oldest first.** Order comes from
  `trading_log.chronological`, and rows that share a `Time` are taken in
  reverse file order.
  - `B` opens or adds to a long, or reduces a short. E1 books a cover as
    `B`.
  - `SS` opens or adds to a short.
  - `S` reduces a long.
- **A trade closes at 0.** One leg per execution. `gross_pnl` is realized
  FIFO against the lots actually opened. `avg_entry` and `avg_exit` are
  share-weighted.
- **Open at file end (R67).** The trade is `open`, with `held_shares`,
  `unrealized = "not computed"` and an `OpenPosition` carrying its
  remaining lots. This is not a failure.
- **`trade_id`** is `<symbol>-<direction>-<entry time ISO>`. A carried
  trade keeps its id across days.
- **The seed** is the prior day's open positions. Each becomes a book
  whose entries are the carried lots (`carried=True`, no line). The
  closing day's P&L uses those lot prices, and `carried_from` names the
  opening day.

## `PairingError` — the whole file fails (L1)
- **A position taken through 0 in one execution.** E1 shows no reversal,
  so the export is not proven to book one.
- **`S` of a symbol with no long position.** This is "a carried symbol
  with no prior row (<symbol>); never assumed flat" (v2 `[F-10]`).
- **A side that contradicts the open position.** When the position came
  from the seed, the message says "contradicts the seed".
- **A seed whose lots disagree with its `held_shares`.**
- **An execution missing a pairing input.** This is a defensive check.
  The normal path for a `partial` file is `build_day` (below).

## `check_contiguity(day, prior_trading_day, recorded_days)`
This is the ASK-DESK safe default of D1-3. E1 starts flat, so the seed
has no cross-check inside the file.
- Once any earlier day is recorded, the prior TRADING day must be
  recorded too, as an import or a no-trade day. Otherwise the check
  fails, naming both days.
- The very first import passes.

The caller (`DrcStore.seed_for`) supplies
`daymode.propose.prior_trading_day`.

## `match_stats(pairing, stats)` (D1-4)
- **EXACT on what both files carry:** symbol + direction + entry time to
  the second. E1 matched 4 of 4. No tolerance exists (L53).
- A matched trade takes the row as `stats` and its `playbooks` list,
  every name in order.
- **Unmatched rows are shown, never dropped or guessed:**
  - a row matching 0 or several trades
  - a row with an empty match cell
  - two rows claiming one trade (both rows unmatched)

  Each goes to `unmatched` with its reason.
- If a `partial` stats log lacks a match input column, every row is
  `unmatched — missing: <columns>`, and `not_computed["match"]` says so.

## `build_day(trading, stats=None, seed=())`
This is the one entry for a parsed day. When the trading log's
`not_computed` carries `pairing`, it pairs nothing and says why. It then
does not match, and every stats row is unmatched with the reason given.
Nothing is defaulted.
