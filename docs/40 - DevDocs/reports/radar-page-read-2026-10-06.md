## §0 Headline
- Counts per source (read 1): table 26, view 26, lost 0.
- The view returns the same rows as the table: no, it does not return fewer, and not more (no join fan-out).
- All 26 rows pass the page WHERE (state date 2026-10-06 on every row; 4 are also open, WATCH).
- Cause rule fired: `state`. The page would select today's cards, yet his page was empty; this read cannot explain it.

## TABLE
Read 1 (production, user side):

| source | state | state date | count |
|---|---|---|---|
| table | EXPIRED | 2026-10-06 | 22 |
| table | WATCH | 2026-10-06 | 4 |
| view | EXPIRED | 2026-10-06 | 22 |
| view | WATCH | 2026-10-06 | 4 |

Totals (read 1): table 26 · view 26.

- View fewer than table? No. Equal in every `(state, state_date)` group; no fan-out.
- Table rows the page's WHERE would not select: 0 (every state date is 2026-10-06; the arms are OR). Page-selected count: 26 − 0 = 26.
- Cause rule, in order: view (no, 26 = 26) → state_at (no, 0 unselected) → `state` (yes: the page would select 26 rows yet showed none, 22 EXPIRED + 4 WATCH; not explained by this read).

## DECISIONS
- ASK DESK: the data is present and the WHERE passes, so the empty page is not in these rows. The next suspect is the page's read or render path (the `day` argument passed to `radar_board_cards`, a `TERMINAL` filter dropping EXPIRED, or the page reading a different DB or time). Default taken: no further production read, stopped. [2026-10-06]

## RECORDS
- `ls` of the report path: exit 1, absent, as required.
- Column greps on main (all confirmed): `aset/migrations/0001_aset_sizings.sql:8` created_at NOT NULL; `0006_aset_sizings_state.sql:26` state_at (nullable), `:1` state + state_at; `0008_aset_sizings_origin.sql:23` origin; `0009_aset_sizings_origin_not_null.sql:12` NOT NULL; `db_migrations/0007_radar_cards.sql:215` view exposes created_at, state, state_at; `:233` `WHERE c.origin = 'radar'`; `:229`, `:232` LEFT JOINs.
- First Bash call (an `ls` joined to `grep` by a pipe) was blocked by the bare-guard hook; no output, resent one command per call.
- Production read 1: the exact string in the prompt, one `--prod`, exit 0, no errors, no guard refusal. Only one production string was run.
- Counts only; no row content.

## MEASURE
`wc -c` of this report: 2437 bytes before this line was edited in (L71); about 2400 after.

READ DONE · table: 26 · view: 26 · lost: 0 · cause: state · decisions: 1
