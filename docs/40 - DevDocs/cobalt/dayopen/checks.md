# `src/cobalt/dayopen/checks.py`

The six fixed checks, C1-C6, each doing its own collection AND rendering
its own verdict (same shape as `cobalt.heartbeat.probes`) so one broken
check never takes the rest of the sweep down — every expected failure
mode (missing file, launchd/DB error, unparseable report) becomes
`Verdict.ERROR`, never an uncaught exception.

- **C1** `launchctl print com.cobalt.radar` — PASS iff `state=running`
  with a pid.
- **C2** `radar_membership` rows for the report date (`system` side,
  read-only transaction, the same factory `cobalt db query` uses) —
  count, first five rows by `first_seen_at`, and the session's
  `rank_metric` read from the `radar.pool` mirror row in
  `"user".trader_settings` (supplementary — never fails C2 on its own).
  PASS iff count > 0 and the first row's `first_seen_at` (ET) is at or
  after `session.premarket_open`.
- **C3** the newest `OK|RED  radar  ...` line in `logs/heartbeat.log`.
  PASS unless it is RED on a trading day at/after
  `session.premarket_open` — a RED line on a weekend/holiday, or before
  the open, is idle and exempt (RULED EXPECT, 2026-09-14).
- **C4** `system.session_blocks` rows with `actor ~ '^vaultwrite:heartbeat:'`
  — a REGEX operator, never `LIKE` with `%`: the exact S4 bug
  (`ProgrammingError: only '%s', '%b', '%t' are allowed ..., got '%'`)
  from `docs/40 - DevDocs/reports/day-open-2026-09-14.md`. PASS iff the
  count equals `dayopen.c4_expected_session_blocks`.
- **C5** `docs/30 - Design/archiver-runs.md`'s last table row +
  `logs/archiver.err`'s last 3 lines. PASS iff `Failures` is 0 and the
  row's `Date (UTC)` (converted to ET) is the previous trading day.
- **C6** every beat header in `logs/heartbeat.log` since
  `session.aftermarket_close` the prior evening, plus any `logs/heartbeat.err`
  line containing "FAILED" in that window. PASS iff at least one beat
  ran, the largest gap between beats is at most
  `dayopen.c6_max_gap_min`, and there is no FAILED line.

`previous_trading_day()` is the one calendar-walk helper, shared by C5.
