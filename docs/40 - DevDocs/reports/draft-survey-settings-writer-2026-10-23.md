## §0 Headline
- Survey prompt written: `prompts/2026-10-23/1017-survey-settings-writer.md` (Opus 5.5, 3 production reads P1-P3, 4 questions, report `reports/survey-settings-writer-2026-10-23.md`).
- Proven on main: the table keeps no history (only `source`, `updated_at`); five write paths; there is no `POST /settings`, the route is `POST /settings/daily/apply`.
- Nothing committed, no other file changed.

## DECISIONS
- ASK DESK: the prompt's launch line also disallows `cobalt settings*` and `git commit*`; the brief's list did not name them. Default taken: kept (read-only). [08:13 ET]
- ASK DESK: the brief says "POST /settings route"; main has `POST /settings/daily` (review, writes nothing) and `POST /settings/daily/apply`. Default taken: prompt names the real routes. [08:13 ET]

## RECORDS
- 08:11 ET `date`. Read: `prompts/2026-10-08/115-radar-cards-survey.md`, `Memory/topics/writing-rules.md`.
- Proven on main (grep/read): `db_query.py:98-103,156-158,209-215` (flags); `ops/desk/bare-guard.py:992-1031` (G2 `prod_read`); `settings/migrations/0001_trader_settings.sql:29-46`; `settings/store.py:60-117`; `settings/cli.py:76-118,207,237,317`; `settings/card.py:61,67,296-303,322-325`; `aset/web.py:1328,1343-1369`; `radar/notes.py:737-751`; `radar/runner.py:320`; `db_migrations/0004_radar_pool.sql:73-76`; `settings/models.py:54,232,238-247`; `env.py:38,44,78`.
- Existence checked: `reports/f5-gate-run-2026-10-21.md`, `prompts/2026-10-21/1000-cos-env-load-card.md`; `reports/survey-settings-writer-2026-10-23.md` absent.
- Not read: the desk scripts under `ops/desk/` named in Q3 (the survey seat reads them); the log files.
- 08:13 ET `date`. Production reads: none.

DRAFTED · decisions: 2
