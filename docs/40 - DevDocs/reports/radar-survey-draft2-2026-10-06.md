# Radar survey draft 2 2026-10-06

## §0 Headline
- Wrote `prompts/2026-10-06/19-radar-drought-survey-r2.md` in `17`'s shape: line 2 `RULINGS: 2026-10-06 R508`, seat `radar-survey2`, four reads from round 1, report `reports/radar-drought-survey-r2-2026-10-06.md`.
- Two points need the desk before launch (below).

## PROMPT
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/19-radar-drought-survey-r2.md`

## DECISIONS
ASK DESK: `01` line 1 spells the `--prod` string only as a disallow (`Bash(COBALT_ENV=dev uv run cobalt db query --side system --prod*)`). Confirm it as an allow [before launch]. Default taken: that exact string is in `--allowedTools`, no deny of it; the dev string (`--side system *`) is copied exactly.
ASK DESK: round 1 gave one literal SELECT (read 1). Reads 2–4 were prose, so the prompt states them as prose with the table and column names from round 1 (`origin`, `created_at`, `trade_date`, `evaluation`, `detail`); the seat composes the SELECT. Confirm the column names or give literals [before launch]. Default taken: prose, no invented SQL.

## RECORDS
- Read: prompt `18`, `17`, line 1 of `01`, round-1 report, `topics/writing-rules.md`.
- Wrote: prompt `19`, this report. No Bash, no database, no git write.
- Kept `17`'s allow list (cut, sort, uniq included) and added `01`'s deny set (commit, pytest, migrate, lock script, `ps e*`, `ps -E*`) beside `awk`.

SURVEY PROMPT DRAFTED · prompt: 19-radar-drought-survey-r2.md · decisions: 2
