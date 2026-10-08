## §0 Headline
Survey prompt 115 drafted from precedent 52, re-pointed to R678: five production reads, `RULINGS: 2026-10-08 R678` on line 2.
Cause rule stated: `display` / `card-writing` / `none`.
Setups table not provable on main: stated `not recorded`.
One decision: the block name column.

## CHANGES
- New `prompts/2026-10-08/115-radar-cards-survey.md`: seat `radar-cards-survey`, launch and allow lines copied from 52, report path `reports/radar-cards-survey-2026-10-08.md`.
- Read 1 `"user".aset_sizings` origin radar by state; read 2 the ladder query on `"user".radar_cards_v`; read 3 `system.radar_pool` failed_stage and `poll_failures`; read 4 `system.session_blocks` by `kind`; read 5 `system.radar_score` with `formed` joined to `system.radar_score_run`.
- Reads 3 to 5 use `--side system` (placement.py:40, :66, :69, :70), allowed by the copied allow line.

## DECISIONS
- ASK DESK: "block name" in read 4 has no column of that name; the survey groups by `session_blocks.kind` (`session/store.py:126`), not by `actor` or `reason`. Default taken: `kind`. [2026-10-08]
- Read 3 is a snapshot: `system.radar_pool` holds one row per pool (`0004_radar_pool.sql:5`) and `poll_failures` is a JSONB array on it, so it is not a day total. The prompt says so. No decision needed.
- Read 5 "formations" counts `radar_score` rows with `evaluation = 'formed'` per run day; a distinct member-and-definition count is reported beside the raw evaluations. No setups table is provable, so that stage reads `not recorded`.

## RECORDS
- Read `prompts/2026-10-06/52-radar-page-read-survey.md` (whole), `topics/writing-rules.md`, `src/cobalt/cards/store.py:1030-1074` (`radar_board_cards` at :1047-1061), `db_migrations/0004_radar_pool.sql` (whole), `session/migrations/0001_session_blocks.sql` (whole), `db_migrations/0006_radar_score.sql:60-114`, `db_migrations/0009_picks_missed.sql:44-84`, `db_migrations/0007_radar_cards.sql:210-236`.
- Grep on main: `failed_stage` (radar_pool column, 0004:11; 'evaluate' added 0006:58-59); `RADAR_OPEN_STATES =` at `store.py:968`; `session_blocks` (`session/store.py:126` groups by `kind`; `0002_session_blocks_kind.sql:19` adds `kind`); `placement.py` lines 28, 40, 66, 67, 69, 70.
- Grep for a formations table: only `"user".missed` (kind `formation`, a nightly replay of misses, `0009_picks_missed.sql:68`), not today's live formations; rejected. `system.radar_score` `evaluation = 'formed'` (`0006_radar_score.sql:99-100`) used instead.
- `ls` of `prompts/2026-10-08/` and the draft report path (absent before writing).
- No database, no production command, no git write, no launch.
- Column lines for `aset_sizings` (`0001:8`, `0006:22`, `:26`, `0008:23`, `0002_move_tables.sql:46`) are copied from prompt 52 and not re-grepped here.

RADAR CARDS SURVEY DRAFTED · decisions: 1
