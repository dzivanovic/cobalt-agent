## §0 Headline
Prompt 406 written: `prompts/2026-10-12/406-strike-alert-read.md`, shape of 388, Sonnet 5.5, auto, one `--add-dir`, allowedTools = Read, Write, Grep, `Bash(date*)` and only the R686 string. Not launched.

## DECISIONS
- ASK DESK: the R686 allow string is `Bash(COBALT_ENV=production uv run cobalt db query *)`, from `settings.json:54` and card 120 lines 23, 46; no `--allowedTools` copy of it is in card 120 itself. I used that string. Default: keep. [before launch]
- ASK DESK: the query selects by `seam_at` window 10:45-11:15 ET, since the `transition_id` for ASTS is unknown to me and unproven. Default: keep; the prompt quotes all rows in the window. [before launch]
- ASK DESK: the table is written unqualified (`strike_alerts`, `--side user`); the prompt allows one fallback with `\"user\".`. I did not run the query to prove which works (no DB command). Default: keep. [before launch]
- ASK DESK: the K5 row for the R686 read string on the desk line is still owed (R1198); I did not touch it. Default: desk adds it. [before launch]

## RECORDS
- `ops/desk/bare-guard.py:967` `PROD_READ` leading words; `:971-1006` `prod_read` (one `--prod`, `--side` in user/system, no other PROD word); `:1074` G2 denies production unless `prod_read`.
- `tests/ops/test_bare_guard.py:420` `PROD_QUERY` shape; `:447-451` `PROD_READS`.
- `.claude/settings.json` (`/Users/cobalt/.claude/settings.json:54`) allow `Bash(COBALT_ENV=production uv run cobalt db query *)`.
- `docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md:23,46` card 120 O1, the one production read.
- `src/cobalt/db_migrations/0024_strike_alerts.sql:16-29` columns `id, user_id, transition_id, seam_at, pushed_at, shown_at, dm_at, dm_result, created_at`; `src/cobalt/aset/strike.py:142` `_RECORD`, `:180-191` upsert, `:202-203` DM claim, `:209-211` dm_result.
- `prompts/2026-10-12/388-survey-blockers.md:1` the shape copied.
- `reports/cto-2026-10-12.md:7-9` R1196-R1198, the alert and the direction.

DRAFTED · decisions: 4
