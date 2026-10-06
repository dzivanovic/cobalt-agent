# survey preflight r2 — 2026-10-05

§0: prompt `01-second-writer-survey.md` passes all 6 checks. One `RULINGS:` line, one path-scoped `Edit(...)` rule, no bare `Write`/`Edit`, deny list complete, committed and clean.

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `grep -c "^RULINGS:" <prompt>` | `1` | OK |
| 1b | `grep -n "^RULINGS:" <prompt>` | `2:RULINGS: 2026-10-03 R326` | OK |
| 1c | `grep -c "^\| R326 " cto-2026-10-03.md` | `1`; row 332 reads `HIS RULING: A on all three … second-writer survey gets its 5 read strings, this seat only … \| HIS RULING · APPROVED` | OK |
| 1d | `git diff --stat -- cto-2026-10-03.md <prompt>` ; `grep -n ruling_row ops/desk/desk-launch.sh` | diff empty (committed, equal at HEAD); `ruling_row()` at `:238` | OK |
| 2 | the prompt's `--allowedTools`, line 1 | `Read` · `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/second-writer-survey-2026-10-05.md)` · `Bash(COBALT_ENV=dev uv run cobalt db query --side system *)` · `Bash(lsof -nP -iTCP:5432*)` · `Bash(lsof -a -p *)` · `Bash(ps -o *)` · `Bash(sleep *)` · `Bash(git -C /Users/cobalt/cobalt show*)` · `Bash(git -C /Users/cobalt/cobalt log*)` · `Bash(ls *)` · `Bash(grep *)` · `Bash(tail *)` · `Bash(wc *)` · `Bash(date*)`. No bare `Write`/`Edit`; one `Edit(...)`, its path after the `//` equals the REPORT path `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/second-writer-survey-2026-10-05.md`. Five R326 strings + git reads + plain reads only; no `git add\|commit`, no `db migrate\|insert\|update\|delete` | OK |
| 3 | the prompt's `--disallowedTools` | `AskUserQuestion` · `EnterWorktree` · `Bash(git push*)` · `Bash(git commit*)` (plus pytest, `db migrate`, `--prod`, `take-devdb-lock.sh`, `ps e*`, `ps -E*`) | OK |
| 4a | `grep -c "%" <prompt>` ; `grep -n -o ".\{40\}%.\{40\}"` | `1` — line 1 only, the prose `No \`%\` in a query string: use \`strpos\``; no query string has `%` | OK |
| 4b | `grep -n -i -E "INSERT\|UPDATE\|DELETE\|DROP\|ALTER\|TRUNCATE" <prompt>` | `:5`, `:17`, `:19`, `:20`, `:48` — prose, table CONTEXT cells, and the sighting definition; no query string carries a write verb (all queries are `SELECT`) | OK |
| 4c | model line | `MODEL: Sonnet 5.5 (\`claude-sonnet-5-5\`)` | OK |
| 5a | `grep -c "reports/second-writer-survey-2026-10-05.md" <prompt>` | `2` (the `Edit` rule and `## REPORT`), one path | OK |
| 5b | `grep -c -F "«FILL" <prompt>` | `0` | OK |
| 5c | read of the prompt | `## SESSION` line says write only the report; step 5 "Write the report last"; last line is the one-line `SURVEY DONE · … \| FAILED: <reason>` stop line | OK |
| 6 | `git diff --stat -- <prompt>` ; `git log -1 --format=%h -- <prompt>` | empty ; `bbd3b4c0` | OK |

## ISSUES
None.

PREFLIGHT DONE · prompt: second-writer-survey-r2 · checks: 6 · fails: 0 · ready: YES
