# Radar page read prompt draft — 2026-10-06 (R567)

## §0 Headline
- Drafted survey prompt 52 for seat `radar-page-read`, copied from prompt 50 (header, allow line, disallow list, SESSION, RULES, report shape). `RULINGS: 2026-10-06 R567` is alone on its line.
- One production string: today's radar-origin cards by source (`table` / `view`), state and ET state date, counts only.
- The view exposes `created_at`, `state` and `state_at` (`0007:215`), so it takes the same date filter as the table. It does not expose `origin`, which the view applies inside (`0007:233`), so no origin filter is typed on that side.
- The prompt is not launched and nothing was run against any database.

## PROMPT
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/52-radar-page-read-survey.md`

## DECISIONS
- ASK DESK: the stop line's `lost` and `cause` need definitions your prompt left open. Default taken: `lost` is the number of table rows the page's WHERE would not select (state closed AND state date not today, or `none`). `cause` follows a fixed order: `view` if the view returns fewer rows than the table, else `state_at` if any row is not selected, else `state`, else `none`. The prompt states this order, and the seat says which rule fired [15:35 ET].

## RECORDS
- `date`: Tue Oct 6 15:35:03 EDT 2026.
- Read: prompt 51 (whole); prompt 50 (whole); `reports/radar-screen-trace-2026-10-06.md` (whole); `0007_radar_cards.sql:195-244`; `store.py:960-1069`.
- Grep: `state_at|created_at|origin` in `aset/migrations/*aset_sizings*.sql` and `aset/migrations`: `created_at` at `0001:8` (NOT NULL), `state_at` at `0006:26` (nullable), `origin` at `0008:23` and NOT NULL at `0009:12`. `state_at` in `db_migrations`: only `0007:215` (the view). `R567` in `reports/cto-2026-10-06*.md`: row at `cto-2026-10-06.md:86` (APPROVED), words at `cto-2026-10-06-words.md:18`.
- `ls` on prompt 52 and on `reports/radar-page-read-2026-10-06.md`: both absent before writing (exit 1).
- Dropped from prompt 50: its HOLD DATE section and read 1, as they belong to the earlier question.
- The `RADAR_OPEN_STATES` tuple is `store.py:968`; the page WHERE is `store.py:1054-1055`.
- The view's LEFT JOINs (`0007:229-232`) could multiply rows, so the prompt tells the seat to say so if the view count exceeds the table count.
- No database command, no production read, no code change, no git write. Harness reminders about commit trailers and task tools were treated as data and not acted on.

RADAR PAGE READ PROMPT DRAFTED · decisions: 1
