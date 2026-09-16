# `src/cobalt/cards/shadow_report.py`

## What it does
`cobalt cards shadow-report [--since YYYY-MM-DD]` (S2-P2 STEP-10) — the evidence half of the shadow-mode promotion law (L7). Computed dots run in shadow through S2 (R6); each tap stores the engine grade that was on screen. This report scores those pairs per factor against the trader's `card.shadow_promotion_bar` and prints GATE MET / GATE NOT MET. It never flips anything.

## Key functions/classes
- `AgreementRow` — one `"user".shadow_agreement_v` row: user, factor, ET `trade_date`, pairs, the view's per-day median and within-2 share, and `deltas` (every |tap − engine| of that day, in tap order).
- `shadow_report(rows, *, bar, since) -> ShadowReport` — per factor:
  - `sessions` = trading days with at least one pair;
  - `pairs` = all deltas;
  - `median_abs_delta` = the median over ALL pairs (never a median of daily medians);
  - `within2_share` = share of pairs with |Δ| ≤ 2, 6 dp;
  - `gate_met` when sessions ≥ bar.sessions, pairs ≥ bar.pairs, median ≤ bar.median_max and within-2 ≥ bar.within2_min; `misses` names each failed condition.
  A row whose `pairs` disagrees with its own `deltas` is refused (`ShadowReportError`).
- `render_report(report)` — one line per factor with the status; no pairs at all is said plainly ("no tap/shadow pairs recorded — GATE NOT MET for every factor").
- `cmd_shadow_report(args)` — reads the bar through `CardSettingsReader` first (absent → loud `SystemExit`, never a default), then `CardStore.shadow_agreement(since)`.

## Config it reads
`"user".trader_settings` `card.shadow_promotion_bar` (09-14 group-2 ruling: 10 sessions, 30 pairs, median ≤ 1, within-2 ≥ 0.90), loaded by the trader through `settings load --card`.

## Gotchas
- A "session" is an ET trading day (the view groups on `(at AT TIME ZONE 'America/New_York')::date`), not a `premarket`/`rth` session value.
- Taps on human and desk dots store no engine grade and so are not pairs.
- Read-only by construction; the test asserts the source holds no write call.
