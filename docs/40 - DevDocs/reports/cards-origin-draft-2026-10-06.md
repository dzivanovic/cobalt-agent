# Cards origin survey prompt draft — 2026-10-06 (R560)

## §0 Headline
- Prompt 50 written: two production reads, per ET day since 09-20 by origin and setup with a day total, and the nine latest card days by state.
- Setup column is `trade_def_slug` (`0007_radar_cards.sql:32`); NULL on manual cards, printed `none`.
- Hold day found by grep: R117/R118, 2026-09-23 22:2x–22:3x ET.
- Neither query was run (no production command in this seat); both are checked by grep against the migrations only.

## PROMPT
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/50-cards-origin-survey.md`

## DECISIONS
- ASK DESK: read 2 takes "nine most recent trading days" as the nine most recent days holding any card, since no trading calendar table was read. Default taken: card days [15:20 ET].
- ASK DESK: read 1 uses `GROUPING SETS` and read 2 a `SELECT DISTINCT … LIMIT 9` subquery; neither was parsed against a database. A parse error makes the survey record the text and stop (no other production string). Default taken: send as written [15:20 ET].

## RECORDS
- Read: prompt 49; `37-radar-drought-survey-r3.md`; `Memory/areas/cobalt.md`; `Memory/topics/writing-rules.md`; `radar-drought-survey-r3-2026-10-06.md`; `radar-screen-trace-2026-10-06.md`.
- `ls reports/cards-origin-survey-2026-10-06.md`: exit 1, absent.
- Grep `aset_sizings` in `src/cobalt/**/*.sql`: `created_at` `aset/migrations/0001:8`; `state` `0006:22`; `origin` `0008:23`; `trade_def_slug` `db_migrations/0007:32`, constraint `:78`; `"user"` move `0002:46`.
- Hold dates: `reports/sitting-vwap-continuation-2026-09-24.md:24,54` (R118, 09-23 22:3x ET); `reports/sitting-second-chance-2026-09-24.md:25,85` (R117, 09-23 22:2x ET); BACKLOG `## PENDING SITTINGS` lines 607-608 (both `PENDING — UNHELD`). Grep of `cto-2026-10-06.md` and its words file: line 99 mentions both setups; not opened.
- `date`: Tue Oct 6 15:18:45 EDT 2026. HEAD `7ff517e8`.
- No database command, no code change, no git write.

CARDS ORIGIN SURVEY PROMPT DRAFTED · decisions: 2
