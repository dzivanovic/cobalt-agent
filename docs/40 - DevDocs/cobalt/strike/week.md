# `src/cobalt/strike/week.py`

`cobalt strike week [--from <date>] [--to <date>]` (DECISION E8), read-only: the seam rows of the ET range (`StrikeAlertStore.seam_rows_between`, `seam_kind`) and their `strike_alerts` records. Per ET day and in total: TRIGGERED / MISSED counts; DETECT lag `seen_at − bar_close_at` and PANEL lag `shown_at − bar_close_at` for the close-based policies; `intrabar` apart, its PANEL lag `shown_at − seen_at` (DECISION E5); n · p50 · p95 · max by P1's nearest rank (`measure._stats` / `percentile`); DMs and their results; triggers never shown. Unwatchable / capped cards are said to live in the radar's log only (P1 records no count). Last line: `F9 CRITERION MET <n>/<n> ≤ <s> s` or `NOT MET — <k> of <n> over <s> s` against `strike.alert_criterion_s`, a never-shown trigger counted over; no trigger → `NOT MET — no TRIGGERED in range`. Default range: Monday of this ET week through today.

## 2026-10-09 — s4-p2-1009
New module (S4-P2 S6).
