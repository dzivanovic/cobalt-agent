## §0 Headline
- Wrote `prompts/2026-10-06/37-radar-drought-survey-r3.md` in `19`'s shape: line 2 `RULINGS: 2026-10-06 R508`, seat `radar-survey3`, Sonnet 5.5.
- Production strings copy G2's shape (`bare-guard.py` `marked_read`): `COBALT_ENV=production uv run cobalt db query --side <user|system> --prod "<sql>"`, one `--prod`, no `#`, brace, `--allow-prod` or continuation line. G2 accepts them by reading.
- Reads: the four of round 1 plus run counts (5) and `failed_detail` (6a, 6b) for the 09-30 RED. Schema read from migrations 0004, 0006, 0007; nothing run.
- 1 decision for the desk.

## PROMPT
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/37-radar-drought-survey-r3.md`. Written by Write only; nothing run, no DB, no launch.

## DECISIONS
- ASK DESK: the launch line allows two strings beyond `19`'s and R411/R412: dev `--side user` (reads 1 and 2 live in `"user"`; round 2 failed on `--side system`) and the two production strings (`--side user --prod`, `--side system --prod`). Both are read-only `db query`. [now] Default taken: kept; drop them and reads 1 and 2 cannot run.

## RECORDS
- Read: `19`, round-2 report, round-1 report, `guard-g2-check` report, `ops/desk/bare-guard.py` (lines 847-891, G2 rows), `writing-rules.md`, `src/cobalt/db_query.py`, migrations 0004 and 0006 by grep.
- Column facts from files: `radar_membership.trade_date` (system); `radar_score` has no day, joins `radar_score_run.started_at` (system), which holds `cards_enabled`, `status`, `failed_detail`; `session_blocks.ts` (system, `session/store.py:88`); `aset_sizings.origin` (user, 0007). `aset_sizings.created_at` and the `trader_settings` columns are from the desk's prompt, not seen in a migration (L70: unproven); an error is recorded by the survey.
- Quoting shape `\"user\".table` copied from `prompts/2026-09-30/41-stacked-deploy-0930.md:151`.
- Not proven: a G2 dry run (no Bash command run; this seat's tools exclude it).

SURVEY PROMPT DRAFTED · prompt: 37-radar-drought-survey-r3.md · decisions: 1
