## §0 Headline

Narrowed by elimination, not DB-proven: RTH's 2,107 `formed` rows most likely
die at `radar/evaluate.py:1955-1960` (`radar_expiry` stop-before-arm) on
every scan — silent, non-consuming, so the same formation re-forms and
re-fails next cycle, matching both the zero-card and the high-volume facts.
Aftermarket's 217 `formed` rows die separately at `evaluate.py:1948-1950`
(deadline 16:00 already passed). Every other condition in the funnel is
ruled out by reads alone (below). One query confirms or kills the stop-touch
reading. Defect, not intended, on current reads.

## Path

Conditions from one `formed` `radar_score` row to a card on `/radar`, in
call order inside `RadarEvaluator._evaluate` (`radar/evaluate.py:1851`) —
scores are written at `:1865` for every evaluation regardless of outcome,
so `formed` alone says nothing yet about a card:

| # | Condition | file:line |
|---|---|---|
| 1 | `settings.cards_enabled` true, else the whole create/refresh block is skipped | `radar/evaluate.py:1882` |
| 2 | `ev.evaluation == "formed"`, not `departed`, `ev.formation` set | `radar/evaluate.py:1940` |
| 3 | `(ticker, slug, direction)` not already in `open_keys` (this cycle's own open+just-created cards) | `radar/evaluate.py:1944`, built `:1890-1894`, `:1994` |
| 4 | `card_store.formation_consumed(ticker, slug, direction, formed_bar_ts)` — no existing `aset_sizings` row (any state) at this exact formation bar | `radar/evaluate.py:1946`, `cards/store.py:954-963` |
| 5 | `instant <= radar_deadline(preferred_windows_ref, trade_date).expires_at` | `radar/evaluate.py:1948-1950`, `cards/expire.py:254-261`, `:130-157` |
| 6 | `radar_expiry(state=WATCH, ..., bars_after_formation=ev.i1_after)` returns `None` — no i1 bar after the formation bar already crosses the stop (stop-before-arm) | `radar/evaluate.py:1951-1960`, `cards/expire.py:272-299` |
| 7 | `card_store.create_radar_card(spec, ...)` — `INSERT ... ON CONFLICT (pool_member_id, trade_def_slug, direction) WHERE state IN (WATCH,ARMED,TRIGGERED,FILLED) DO NOTHING` | `radar/evaluate.py:1984`, `cards/store.py:965-1014` |
| 8 | `card_id is not None` (the ON CONFLICT branch didn't fire) | `radar/evaluate.py:1992-1993` |
| 9 | `"user".radar_cards_v` (`WHERE c.origin = 'radar'`, no further filter) | `db_migrations/0007_radar_cards.sql:214-233` |
| 10 | `/radar` read: `radar_board_cards(day)` — open-state OR `state_at`(ET) = today | `cards/store.py:926-940`, `aset/radar_panel.py:764-773` |

Exceptions in the create loop (`try/except` at `:1983-1991`) are appended
to `outcome.refusals` and logged unconditionally at
`radar/runner.py:351-353` (`logger.error("radar S5 card refusals: …")`)
whenever non-empty, every cycle. `outcome.refusals` is also fed by the
open-card refresh loop (`:1890-1909`) when a card's def is no longer
loaded — irrelevant today (no open cards). #3-#6 and #8 are bare
`continue`/`None` with **no log line anywhere** on that path.

## Today

Given facts: `cards_enabled` True (round 1, DB); RTH 2,107 / aftermarket
217 `formed` rows; `radar_cards_v` 62 rows total, none dated today
(`/radar` "No radar cards today"); `radar.err` zero card lines, zero
error lines today.

| # | Verdict | Why |
|---|---|---|
| 1 | HOLDS | `cards_enabled` True (round 1 DB read) |
| 2 | HOLDS for exactly the 2,324 rows marked `formed` today — that is what the label means | by definition |
| 3 | HOLDS (doesn't block) | `open_keys` starts from `open_cards()` (`origin='radar'`, states WATCH/ARMED/TRIGGERED/FILLED), which is empty — zero cards exist today or are open at all; it only grows from a same-cycle success (`:1994`), and today has zero successes, so it never actually skips anything |
| 4 | HOLDS (doesn't block) | `formation_consumed` needs an existing `aset_sizings` row at the exact `(ticker, slug, direction, formed_bar_ts)` — zero radar cards were created today (fact: `radar_cards_v` shows none for today), so no today-dated `formed_at` can already be consumed; a stale prior-day row can't match (its own day's bar timestamp) |
| 5 | HOLDS for RTH (09:30-15:59), FAILS for aftermarket | `window_end_for` resolves `preferred_windows_ref` 'sheet: 9:59-4:00' ambiguously and falls back to session close 16:00 (round 1's `cards.expire` INFO line, same function, same ref) — RTH scans are all before 16:00, so `instant <= deadline` holds; all 217 aftermarket `formed` rows (post-16:22) are past it and die here, explained and expected once the stale-score/quiet-day pair rules were out |
| 6 | NOT CHECKABLE FROM READS, but the only surviving candidate for RTH's 2,107 | `SELECT id, ticker, direction, detail#>'{formation,stop}' AS stop, detail#>'{formation,trigger}' AS trigger, detail#>'{formation,formed_bar_ts}' AS formed_bar_ts, detail#>'{formation,formed_bar_end}' AS formed_bar_end FROM system.radar_score WHERE run_id = 1826 AND evaluation = 'formed'` for the stop/trigger/formation-bar-end, joined against `system.bars` i1 rows for those tickers between `formed_bar_end` and the run's `instant` — if every row shows an i1 bar already through the stop, this confirms; the code comment at `:1956-1960` states the formation is deliberately NOT consumed when this fires, so the same setup re-forming next scan (and dying here again) is exactly consistent with 2,107 `formed` rows and zero cards |
| 7-8 | HOLDS (doesn't block), ruled out by the log | the `INSERT` either raises (would log `radar S5 card refusals` — zero such lines today) or hits ON CONFLICT DO NOTHING (requires an existing OPEN card for that key — none exist today, per #3); neither is live |
| 9 | HOLDS (doesn't block) | view has no filter beyond `origin='radar'`, which `create_radar_card` always sets; not reachable since no row is ever inserted (#6) |
| 10 | HOLDS (doesn't block) | consistent with `/radar` showing zero: no rows exist to be open or terminal-today in the first place |

## What changed

`git log --oneline -20` on `src/cobalt/radar src/cobalt/aset/radar_panel.py src/cobalt/db_migrations`
shows every touching commit dated 2026-09-24 18:20 ET through 2026-09-25
12:34 ET (stale-score S1/S2 `d0274dc0`/`01ee8bcd`; H1 handicap STEP-2
through STEP-7 `8f178af2`…`9fb8a8e2`; the R95 replay fixes `d0898f75`
(shared member-prep, "no output byte changes" claimed, but does touch
`evaluate_member`'s `closed_i1`/`i1_after` construction — relevant given
#6 above) and `12fac3cd`; three merges into `deploy/stacked-0925`). None
is dated 09-26 or later — nothing in this path is new-to-Saturday's
`3349466f` merge beyond folding `main` in; round 1 already flagged that
whether `deploy/stacked-0925` (hence these commits) was live Friday
09-25 — when cards 384/385 formed successfully — or only went live in
Saturday's deploy is NOT CHECKABLE FROM READS (no deploy tags in this
worktree). That timing is what would tell us whether these commits are
even in scope, ahead of picking one to blame.

## ESCALATE

ASK DESK: run the `radar_score`/`system.bars` join in Today row #6 for
run 1826 (13 formed rows) to confirm or kill the stop-before-arm reading.
[next DB session]
ASK DESK: the creation timestamp (ET) of cards 384 (AKAM) and 385 (MSFT)
on 2026-09-25, against `deploy/stacked-0925`'s merge times (11:25-12:34
ET that day) — settles whether Friday's cards already ran under today's
code or under the pre-stack code, which decides whether R95/stale-score/H1
are in scope for today's break at all. [next DB session]

RADAR NO-CARDS READ 2 DONE · cause: narrowed to evaluate.py:1955-1960 stop-before-arm (RTH) + evaluate.py:1948-1950 deadline (aftermarket), unconfirmed by DB · intended: no · ESCALATE: 2
