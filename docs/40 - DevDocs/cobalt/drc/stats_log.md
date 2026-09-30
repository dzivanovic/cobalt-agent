# `src/cobalt/drc/stats_log.py`

## What it does
This module parses his trade journal's daily log, one row per trade,
into `StatsRow` records. It sits behind the `TradeStatsSource` interface
(L9), and `StatsLogSource` is today's only source. R91: entries,
targets, assumed and realized R:R come from this log. MAE, MFE and best
exit come from it only because the log carries them.

A file reaches `StatsLogSource.parse(data, detection)` only after
`detect.detect_kind` classified it `stats_log` (R114).

## The constants
- **`REQUIRED`** — 48 names. These are E1's header in order, minus the
  one vendor-named column. That column is never in code (L31): it is
  neither required nor read. `detect` imports this constant.
- **`MATCH_INPUTS`** — symbol, side, open date, open time.
- **`STOP_COLUMN = None`** — see below.

## The stop (09-23 R17 (4))
`StatsRow.stop` is read ONLY from a stop column of THIS log, by a RULED
header name. E1's header has none, so no name is ruled and the stop is
`None` (`not given`) on every row. The build report's `## ESCALATE`
carries the question to the desk.

The stop is never computed. Not from the dollar-risk column, the target,
the reward ratio, the realized R:R, the prices or the quantity, alone or
together. A test proves that a row with all of these set still yields
`stop = None`.

If his export gains a stop column, `detect` reports it as an extra
(`stats_log_shape`, loud). Reading it is a later change, made on his
ruling of the name and with a new real-shape fixture.

## Times
- The open and close date+time pairs are read as America/New_York
  wall-clock time. The suffix must be `EDT` or `EST`; any other suffix
  fails the file. This is the same zone as the trading log's `Time`.
- **Reading, stated:** the suffix is not checked against the date's real
  DST state. The fixture keeps E1's `EDT` on a constructed January date.
  Both files are read as ET wall clock, so the match compares like with
  like.
- `Best Exit Time` is `YYYY-MM-DD HH:MM:SS UTC`, read as UTC.

## Playbooks (R114)
`split_playbooks(cell)` splits on the comma and strips each name. Empty
pieces are dropped, order is kept, and nothing is de-duplicated or
picked. An empty cell gives `[]`. The separate `Setups` column is never
read as a playbook. Mapping a name to a setup is D3's job (R116).

## Fail-loud, partial, degraded
- **Fail-loud.** One bad cell fails the whole file, naming the line,
  with zero rows. Bad cells include a non-number, a side other than
  `long`/`short`, a bad date or clock or zone, a non-integer execution
  count, and a wrong cell count. A non-UTF-8 byte fails the file on the
  line the byte sits on.
- **Empty cells.** An empty cell in a numeric column is `None`. E1 has
  many legitimately blank figures.
- **Partial.** An absent column's field is `None` on every row. If a
  match input is absent, `result.not_computed["match"]` names it, and
  `pairing.match_stats` leaves every row `unmatched — missing: <columns>`.
- **Degraded.** An added column raises `stats_log_shape`. So does E1's
  own vendor-named column, under the literal D1-2a rule (ASK DESK).
