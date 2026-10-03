## §0 Headline

OPEN — 2 readings, not distinguishable from reads. S1-S4 ran clean all day
(pool 50/50, zero ERROR lines in `radar.err` today — confirmed, whole-file
grep found ERROR only on 09-15/16/17/24, none today). S5 evaluate also ran
with zero error/refusal lines every cycle. That is consistent with (A) no
formation reached "formed" today (a quiet market day, intended) or (B)
`"user".trader_settings.radar.cards_enabled` is false (the dark-ship switch,
`settings/card.py:4,21`) — S5 then runs the same clean, silent way and skips
ALL card creation (`evaluate.py:1882`). Neither log distinguishes them; one
query does. Second, separate anomaly below (cards 416/437).

## Path

Conditions for one `formed` card to reach the `/radar` board, in order:

| # | Condition | file:line |
|---|---|---|
| 1 | session ∈ {PREMARKET,RTH,AFTERMARKET}, else cycle idles | `radar/runner.py:179-180` |
| 2 | S1 membership admits the ticker to the pool | `radar/pool.py` `decide()`, called `radar/runner.py:190-194` |
| 3 | S5 evaluator is wired (`radar.finviz_max_rpm` measured) | `radar/runner.py:79-81`, `:412-414` |
| 4 | `settings.cards_enabled` true, else the whole create/refresh block is skipped | `radar/evaluate.py:1778`, `:1882` |
| 5 | per (member, def): `evaluability(td).evaluable` | `radar/evaluate.py:1015-1022` |
| 6 | no `convention_refusals` (a convention row names a rule the code doesn't implement) | `radar/evaluate.py:1023-1030` |
| 7 | not `intraday_stale` (last closed i1 bar within 2× `radar.scan_interval`) | `radar/evaluate.py:1086-1088` |
| 8 | the predicate tree (3-valued interpreter) evaluates True; geometry guard: stop on protective side | `radar/evaluate.py:443-522`, `:862-866` |
| 9 | not already open/consumed for (ticker,slug,direction); still before `radar_deadline` | `radar/evaluate.py:1939-1950` |
| 10 | `create_radar_card` write | `radar/evaluate.py:1984` |
| 11 | `/radar` shows it: `card_store.radar_board_cards(day)` non-empty — open state OR terminal with `state_at` (ET) = today | `cards/store.py:926-940`, `aset/radar_panel.py:764-773` |

## Today

| # | Evidence | Verdict |
|---|---|---|
| 1 | `radar.err` "radar cycle: scanning scan_id=…" through RTH into AFTERMARKET, latest 16:22:50 today | HOLDS |
| 2 | desk R92: pool 50/50 admitted | HOLDS |
| 3 | zero "radar.finviz_max_rpm is unmeasured" / cycle "failed" lines today | HOLDS |
| 4 | `radar.cards_enabled` lives only in `"user".trader_settings` (set by `cobalt settings load --card`, a human-run command, not a deploy artifact — `settings/card.py:10-16`); no config file mirrors it | NOT CHECKABLE FROM READS — `SELECT value FROM trader_settings WHERE key='radar.cards_enabled'` (smoke query shape at `configs/cobalt/smoke/s2.yaml:178-186`) |
| 5-8 | `evaluate.py` has zero `logger.info` calls (confirmed by grep) and zero `logger.error`/refusal lines today — a quiet day and a silently-suppressed day produce byte-identical logs | NOT CHECKABLE FROM READS — needs `radar_score` rows for today's run_id (`evaluation` column distribution) or `cobalt radar evaluate --replay` |
| 9 | one INFO line recurring near close: `cards.expire:window_end_for:156 — falling back to session close (16:00) — preferred_windows_ref 'sheet: 9:59-4:00' not unambiguously resolvable` | informational only; narrows the deadline to 16:00 for affected defs, does not by itself explain a whole-day zero |
| 11 | `cards-expire.log`: cards 416 (SPCX), 437 (SOXL) WATCH→EXPIRED at 2026-09-28 16:00 ET | their `state_at` = today ET; per `cards/store.py:933-934` they should satisfy the terminal-OR-clause and appear on today's board regardless of whether any NEW card formed — so a literal zero-row "No radar cards today" (not just an empty active section) is itself unexplained unless the panel was read before 16:05 ET (before their expiry landed), which conflicts with the desk's "16:1x ET" timing as given | NOT CHECKABLE FROM READS — `SELECT * FROM radar_cards_v WHERE card_id IN (416,437)` and the exact screenshot/request timestamp settle it |

`handicap: not configured` (`aset/radar_panel.py:433-434`, `block.handicap is None`) is orthogonal — H1 handicap is unrelated to admission or card gating and was deployed shadow-only (commit `9fb8a8e2`); not implicated.

## Last card day

Last cards formed: 2026-09-25 (Fri) — card 384 AKAM, 385 MSFT, both WATCH→EXPIRED at close per `cards-expire.log`. 09-26/09-27 are Sat/Sun, no trading, no entries — consistent, not evidence of anything.

Today (Mon 09-28) is the first trading day on LIVE `deploy-2026-09-27` / `3349466f` (a merge of `main` into `deploy/stacked-0925`, made Sat 2026-09-27 18:42 ET — a weekend deploy per NN#16). `deploy-2026-09-25`/`deploy-2026-09-27` tags do not exist in this worktree's git history (`bad revision`) — the requested tag-range diff is NOT CHECKABLE FROM READS with the allowed tools; the deploy log (outside this session's read set) would name the exact commit range. From `git log` alone, commits merged into that branch since 09-24/09-25 touching this path: the H1 handicap feature (STEP-2 through STEP-7, migration 0014 — inert today, "not configured") and cards "stale score" S1/S2 (`d0274dc0`, `01ee8bcd`, migration 0015 — touches `evaluate.py`'s `intraday_stale`/`score_last` plumbing, landed 2026-09-24, so likely already live on 09-25 too, not new-to-09-27 on the evidence available here).

## ESCALATE

ASK DESK: run `SELECT value FROM trader_settings WHERE key='radar.cards_enabled'` and `SELECT evaluation, count(*) FROM radar_score WHERE run_id = (today's latest run_id) GROUP BY evaluation` to pick reading A vs B. [next DB session]
ASK DESK: confirm the `/radar` read's wall-clock timestamp against 16:05 ET (cards-expire) to settle whether cards 416/437 should have shown as terminal. [next DB session]

RADAR NO-CARDS READ DONE · cause: OPEN — 2 readings · intended: unknown · ESCALATE: 2
