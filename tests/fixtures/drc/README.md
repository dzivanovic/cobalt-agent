# DRC D1 fixtures — stripped real shape (L45 / L32, consent R103)

These four files are cut from E1: one real trading day of his two daily
files (`1 - Trading/5 - Review/_imports/drc/<E1 date>/`, R91 / R92 /
R114). They carry E1's SHAPE and none of his VALUES.

Detection never reads a file's name or extension (R114). The `.csv`
names here mean nothing. His real files end `.md`, and a test re-reads
these bytes under `.md`, `.csv` and no extension.

## What was kept, byte for byte
- **The header line of each kind.** Every column name, their order, the
  trading log's trailing delimiter (an empty eleventh cell), and the
  line ending. `trading_log_e1.csv`, `trading_log_carry_day1.csv` and
  `trading_log_carry_seed.csv` share one header. `stats_log_e1.csv` has
  the stats log's 49-name header. Its last column carries a vendor name.
  That name stays only here, byte-identical, and never enters code
  (L31).
- **Formats.**
  - Delimiter `,`. LF line endings, a final newline, no BOM.
  - `Time` as `HH:MM:SS`, with no date and no zone.
  - The stats log's `HH:MM:SS EDT` open/close times, `YYYY-MM-DD` dates,
    and `YYYY-MM-DD HH:MM:SS UTC` best-exit times (or an empty cell).
  - The side codes `B` / `S` / `SS` and `long` / `short`, and the
    trading log's two `Type` codes.
  - Decimal spellings, including a price written with one decimal.
  - Both blank-cell spellings: empty, and quoted empty `""`.
  - The one quoted multi-name playbook cell, separated by `, `.

## What structure was kept (E1 has it)
- The rows are newest-first.
- Split fills share one order id. There are 3 such pairs, and one pair
  has two different prices at the same `Time`.
- A scale-in: one long trade adds at a second `Time` before its first
  exit. It then scales out over 3 exit fills at 2 `Time`s.
- A short opened with `SS` and covered with `B`. One short covers in
  two partial exits.
- There are 3 symbols and 4 trades, and one trade overlaps another in
  time.
- One stats row per trade. The multi-playbook trade carries **two**
  playbook names in ONE quoted cell (R114: two setups added onto each
  other before the first closed).

## What E1 does not have (named, not invented)
- A second account (E1 shows 1 distinct value).
- A reversal through 0 in one execution.
- A position open at file end, or an overnight row.
- Order-log rows.
- A stop column in the stats log (R17 (4)).

Tests build these cases from one-line mutations of these fixtures, with
constructed literals.

## What was stripped and constructed
- Every value was replaced by a constructed one of the same format:
  - account ids → `ACCT1`
  - symbols → `AAA`, `BBB`, `CCC` (and `DDD` / `EEE` / `FFF` in the
    carry pair)
  - dates → `2001-01-02`
  - routes / brokers → `ROUTE<n>` / `BRK<n>`
  - order ids → `H` + 13 digits
  - times, prices, quantities, P&L, R:R, MAE/MFE, scores → our own
    numbers
- **Playbook names are constructed (R117).** They are never his:
  - `Alpha Setup Long, Beta Setup Long` (the multi-name cell)
  - `Gamma Setup Long` and `Delta Pattern Short` (one name each, with
    a ` Long` / ` Short` suffix)
  - `Omega Setup` (one name, no suffix)

  So D3's strip-and-match rule sees names both with and without a
  suffix.
- **The carry pair is CONSTRUCTED (R114).** He "did not leave any open
  trades overnight", so E1 has no carry. Both files use E1's exact
  header and formats:
  - `trading_log_carry_day1.csv` is a day that ends with one long
    position still open (`DDD`, 30 shares held) beside one closed
    trade.
  - `trading_log_carry_seed.csv` is the next day. Its first execution
    closes that position, and it has one fresh short round trip.

No value of his is in this folder.
