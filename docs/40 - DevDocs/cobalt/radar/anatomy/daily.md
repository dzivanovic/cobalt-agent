# `src/cobalt/radar/anatomy/daily.py`

## What it does
Parses the daily export and computes the higher-timeframe references (R5): the prior session, daily ATR, `htf_level_proximity` and `RangeBreak(HTF).day_count`. The series comes from `radar.collector.FinvizDailyBarsCollector`.

## Key functions/classes
- `parse_daily_csv(text, ticker)` requires exactly `Date,Open,High,Low,Close,Volume` with `MM/DD/YYYY` dates. A time-of-day component (an intraday body), any other column set, an empty body or a bad cell raises.
- `DailySeries` holds strictly increasing sessions. `before(trade_date)` keeps sessions STRICTLY before the trade date, because a mid-session export can carry today's partial row.
- `prior_session`, `daily_atr` (Wilder 14 over every prior session).
- `htf_level_proximity(series, trade_date, last_price) -> HtfProximity` = min(|last − prior high|, |last − prior low|) ÷ daily ATR, in `daily_atr` units. It names the reference level, with `prior_high` on an exact tie.
- `htf_range_break(series, trade_date, session_high=, session_low=) -> HtfRangeBreak`: UP when the session high exceeds the prior high, DOWN when the session low undercuts the prior low. The count is 1 plus the consecutive prior sessions that broke the session before them in the same direction. An outside day has no direction and no count; this is reported, never guessed.

## Gotchas
`NoDailyBars` means no prior session exists. A zero daily ATR refuses proximity rather than divide. The HTF range is the prior-session high/low (`range_break.htf_range`, replay_pending).
