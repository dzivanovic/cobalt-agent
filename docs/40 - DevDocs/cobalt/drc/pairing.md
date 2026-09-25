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
  - a row with an empty match cell. The reason names only what is proven
    empty: `Symbol`, `Side`, or `Open Date or Open Time` (the row carries
    only the combined entry time, so an empty date and an empty time are
    named jointly)
  - two rows claiming one trade (both rows unmatched)

  Each goes to `unmatched` with its reason.
- If a `partial` stats log lacks a match input column, every row is
  `unmatched — missing: <columns>`, and `not_computed["match"]` says so.

## `build_day(trading, stats=None, seed=())`
This is the one entry for a parsed day. When the trading log's
`not_computed` carries `pairing`, it pairs nothing and says why. It then
does not match, and every stats row is unmatched with the reason given.
Nothing is defaulted.

## 2026-09-24 — DRC K1: `drc.pairing/2`
- **B8 is replaced.** The signature is now `build_day(trading,
  stats=None, seed=None)`, and `seed=None` means NO BOOK WAS STATED.
  - The day is not paired: `not_computed["pairing"] = "not computed —
    opening book not stated"`, with no trades.
  - Every stats row is `unmatched — no trades were paired`.
  - A list, even `[]`, is the book the caller holds.
  - `pair_day` is unchanged. It is the FIFO engine and holds no book
    policy.
  - This retires O1 = A (R22, v3 `:118`).
- **A stated lot with no cost.** When `_reduce` meets one, it still
  reduces the shares, but it runs no price arithmetic. The trade's
  `gross_pnl` becomes `CARRIED_COST_NOT_STATED`.
  - `hold_seconds` is `None` when there is no entry time.
  - `avg_entry` is `None` when any entry has no price.
  - Trades with no entry time sort first, then by symbol.
- **`book_sha256(positions)`** takes the positions'
  `model_dump(mode="json")`, sorted by `trade_id`, and passes them to
  **`canonical_sha256(rows)`**.
  - The encoding is `json.dumps(sort_keys=True, separators=(",", ":"),
    ensure_ascii=False)`, as UTF-8.
  - `[]` hashes `b"[]"`.
  - This is the encoding pinned by X4.
- **`stated_open_positions(day, positions)`** turns his stated book into
  a seed.
  - Each position gets ONE lot `(time=None, price=avg_cost)`,
    `entry_time=None` and `opened_on=None` (K1 fix r1, H1: its open day
    is not stated; a seeded book keeps its position's `opened_on`, `None`
    included, on every carry, and only a book opened by an execution
    takes the day).
  - Its `trade_id` comes from **`stated_trade_id`**:
    `<symbol>-<direction>-stated-<day>`. This is the drafter's pin, and
    it is stable across restatements.
