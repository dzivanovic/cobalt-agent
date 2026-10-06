# Radar screen trace prompt draft — 2026-10-06

## §0 Headline
- Drafted the code-trace survey prompt for Opus 5.5 seat `radar-screen-trace` (5607 bytes).
- It traces route → page query → gates, compares the writer's radar row against the page's filter, checks 14-day changes, and stops at a `file:line` or `NOT FOUND IN CODE`.
- No database, no `uv`, no production read on its allow line.

## PROMPT
`/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/48-radar-screen-trace-survey.md`
Report it writes: `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-screen-trace-2026-10-06.md`. Stop line carries `tokens: <n>` (L71).

## DECISIONS
None.

## RECORDS
- Read: prompt 47; `prompts/2026-10-06/37-radar-drought-survey-r3.md` (header form); both radar-drought reports; `topics/writing-rules.md`; `areas/cobalt.md`; `LAWS.md` L36, L71, L74.
- `ls` of `prompts/2026-10-06/` (48 absent before the write) and of both report paths (both absent, exit 1 as expected); `ls` of `src/cobalt/cards/expire.py` and `src/cobalt/settings/card.py` (both exist).
- `git -C /Users/cobalt/cobalt rev-parse --short HEAD`: e3128cd3.
- `wc -c` on the new prompt: 5607. New file, no before.
- Paths and `file:line` leads in the prompt (`evaluate.py`, `cards/expire.py`, `settings/card.py`) come from the two prior reports; only the two paths above were re-proven here, the prompt tells the seat to prove every line it cites.
- Writes: the new prompt and this report. No database, no git write, no launch.

RADAR SCREEN TRACE PROMPT DRAFTED · decisions: 0
