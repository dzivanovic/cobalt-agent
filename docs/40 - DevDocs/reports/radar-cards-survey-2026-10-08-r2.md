## §0 Headline
- Cards 19 (read 1): 14 EXPIRED, 5 WATCH.
- View 19 (read 2): the ladder query selects them.
- Poll failures 2, failed stage `bars` (read 3, snapshot); formations 43 (read 5); blocks 0 (read 4).
- Cause: `display`. Read 2 is above 0, yet his page showed none.

## COUNTS
| read | key | count |
|---|---|---|
| 1 | EXPIRED | 14 |
| 1 | WATCH | 5 |
| 1 | total | 19 |
| 2 | ladder query | 19 |
| 3 | bars · scanning · pools | 1 |
| 3 | bars · scanning · poll failures | 2 |
| 4 | session blocks | 0 (no rows) |
| 5 | evaluations formed | 354 |
| 5 | formations distinct | 43 |

- Read 3 is a snapshot of the latest scan, not a log of the day.
- Cause rule: `display` fired (read 2 = 19 > 0).

## DECISIONS
- ASK DESK: the data is in the table and the view and passes the ladder query; the fault is on the page read or render path (`day` argument, TERMINAL filter, DB or clock the page reads). Default taken: no further production read. [2026-10-08]

## RECORDS
- `ls` of the report path: exit 1, absent, as required.
- First Bash call (`ls` piped to `grep`) was blocked by the bare-guard hook; no output; resent one command per call.
- Column greps on main, all confirmed: `aset/migrations/0001_aset_sizings.sql:8` created_at; `0006_aset_sizings_state.sql:22` state, `:26` state_at; `0008_aset_sizings_origin.sql:23` origin; `db_migrations/0007_radar_cards.sql:214-215` view exposes created_at, state, state_at, `:233` `origin = 'radar'`; `0004_radar_pool.sql:11-12` failed_stage, `:22` poll_failures, `:7` state, `:17` members, `:6` pool_key (CHECK there lists membership, pool_row, mirror, bars; `0006_radar_score.sql:58-59` adds evaluate); `session/migrations/0001_session_blocks.sql:15` ts, `0002_session_blocks_kind.sql:19` kind; `0006_radar_score.sql:94` run_id, `:95` membership_id, `:97` trade_def_md5, `:99` evaluation, `:72` started_at.
- Production reads 1-5: the exact strings in the prompt, one `--prod` each, all exit 0, no errors, no guard refusal. Read 4 returned the header only.
- Counts only; no row content.

## MEASURE
`wc -c` of this report: about 2300 bytes.

READ DONE · cards: 19 · view: 19 · poll failures: 2 · formations: 43 · cause: display · decisions: 1
