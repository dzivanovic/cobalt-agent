## §0 Headline
Survey prompt drafted: `prompts/2026-10-06/17-radar-drought-survey.md`, read-only seat `radar-survey`, Q1–Q6 in his order.
Shape copied from `prompts/2026-10-05/01-second-writer-survey.md`; read strings from `09-gain-measure-survey.md` plus the ones the card names.
One decision taken by default (below).

## PROMPT
- Path: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/17-radar-drought-survey.md`
- Lines: 41

## DECISIONS
- ASK DESK: the card says to copy `01`'s database read command; I copied only `Bash(COBALT_ENV=dev uv run cobalt db query --side system *)` and left out `01`'s lsof/ps/sleep strings (no process sampling here). The dev database may not hold radar days; the prompt says so and forbids `--prod`, so Q2 may come back `not answerable with the standing read strings`. Default taken: dev read only. [06:3x ET]

## RECORDS
- Read: `prompts/2026-10-06/16-draft-radar-drought-survey.md`, `prompts/2026-10-05/01-second-writer-survey.md`, head of `09-gain-measure-survey.md`, `topics/writing-rules.md`, `reports/cto-2026-10-06.md` (grep radar), `ls` of `reports/` and `prompts/2026-10-05/`.
- Written: `17-radar-drought-survey.md`, this report. No git write, no launch.
- Source names in the prompt come from the `reports/` listing; the radar job log paths and BACKLOG path are left for the surveyor to find (not located here).

SURVEY PROMPT DRAFTED · prompt: 17-radar-drought-survey.md · decisions: 1
