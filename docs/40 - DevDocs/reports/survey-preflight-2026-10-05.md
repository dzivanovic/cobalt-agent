# Survey prompt preflight — 2026-10-05

Prompt: `prompts/2026-10-05/01-second-writer-survey.md` · ruling R326 (`reports/cto-2026-10-03.md:332`)

## CHECKS
| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `grep -c "^RULINGS:"` / `grep -n "^RULINGS:"` | `1` / `2:RULINGS: 2026-10-03 R326`. `grep -c "^\| R326 "` on the 10-03 report → `1`; row 332 holds `HIS RULING` and `APPROVED`. `git diff --stat` on the 10-03 report → empty (clean). Launcher `ruling_row` (`ops/desk/desk-launch.sh:238`–`:265`): exactly one `\| R<n> \|` row, holds HIS RULING + APPROVED, `git log -S` finds it, and `git show HEAD:` matches the row (`:262`–`:264`). | OK |
| 2 | read the `--allowedTools` line against R326 | Strings: `Read`, `Write`, `Edit`, `Bash(COBALT_ENV=dev uv run cobalt db query --side system *)`, `Bash(lsof -nP -iTCP:5432*)`, `Bash(lsof -a -p *)`, `Bash(ps -o *)`, `Bash(sleep *)`, `Bash(git -C /Users/cobalt/cobalt show*)`, `Bash(git -C /Users/cobalt/cobalt log*)`, `Bash(ls *)`, `Bash(grep *)`, `Bash(tail *)`, `Bash(wc *)`, `Bash(date*)`. R326 approves: "second-writer survey gets its 5 read strings, this seat only" (brain-direction `:140`: "its five read-only strings"). Neither row nor words file lists the five by text; the five on the line are the db query, two `lsof`, `ps -o`, `sleep` (the drafter's reading). Plain reads (`Read`, `ls`, `grep`, `tail`, `wc`, `date`, `git show`, `git log`) are fine. `Write` and `Edit` are write paths R326 does not name. | FAIL |
| 3 | deny list | `AskUserQuestion`, `EnterWorktree`, `Bash(git push*)`, `Bash(git commit*)` present, plus pytest, db migrate, `--prod` query, `take-devdb-lock.sh`, `ps e*`, `ps -E*`. | OK |
| 4 | `grep -n "%"`; grep for write verbs | `%` appears only on line 1 in "No `%` in a query string" (no query string holds one; queries use `strpos` instruction). Write-verb grep (`INSERT INTO\|UPDATE system\|DELETE FROM\|CREATE TABLE\|DROP \|ALTER TABLE .* ADD`) → `0`. Model line: `Sonnet 5.5 (claude-sonnet-5-5)`. | OK |
| 5 | report path, stop line, `grep -c -F "«FILL"` | One report path: `reports/second-writer-survey-2026-10-05.md`. Last line is one line: `SURVEY DONE · … ` or `FAILED: <reason>`. `«FILL` → `0`. | OK |
| 6 | `git diff --stat -- <file>` / `git log -1 --format=%h -- <file>` | empty / `2caec3df` | OK |

## ISSUES
- Check 2 FAIL: `Write` and `Edit` are write strings R326 does not name (R326 covers only the five read strings). `Edit` is not needed (the seat writes one new report); `Write` is needed for the report, so the desk must either get R326 to name `Write` for that one report or run the survey with it as a recorded exception. Also: R326's text does not list the five strings, so the desk should confirm the drafter's five (db query, `lsof -nP -iTCP:5432*`, `lsof -a -p *`, `ps -o *`, `sleep *`).

PREFLIGHT DONE · prompt: second-writer-survey · checks: 6 · fails: 1 · ready: NO
