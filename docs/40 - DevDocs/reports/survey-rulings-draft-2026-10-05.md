# Survey RULINGS line — draft report 2026-10-05

## §0 Headline
- Added `RULINGS: 2026-10-03 R326` as line 2 of `prompts/2026-10-05/01-second-writer-survey.md`.
- `git diff` shows exactly one added line, no other change.
- R326 row exists once, `HIS RULING · APPROVED`, committed (last touch `6ac85389`).
- Not committed by me (no git write); the desk commits before launch.

## DECISIONS
- ASK DESK: which five strings on the survey's allow line are "the five read strings" of R326? I named the five I read as read-only (below); default: left all untouched. [before launch]
- ASK DESK: commit the survey prompt (the launcher's F5 check reads the RULINGS line from the file, not HEAD, but the desk's usual commit-before-launch applies). Default: left uncommitted. [before launch]

## RECORDS
**Launcher rule** (`/Users/cobalt/.claude/ops/desk-launch.sh`, prompt kind, `:451`–`:460`):
- `:457` `prulings=$(sed -n 's/^RULINGS:[[:space:]]*//p' "$pfile")`
- `:458` `if [ "$(grep -c '^RULINGS:' "$pfile")" -eq 1 ] && [ -n "$prulings" ] && [ "$prulings" != "none" ]; then ( ruling_items "$prulings" ) 2>/dev/null && ruled=1`
- Rule: exactly one line starting `RULINGS:` at column 0; `<date> R<n>` resolves to `reports/cto-<date>.md` (`:252`); `ruling_row` (`:238`–`:265`) needs exactly one `| R<n> |` row holding `HIS RULING` and `APPROVED`, committed and equal to the row at HEAD. Only then may a write string (e.g. `COBALT_ENV=`) sit in `--allowedTools`.

**R326 row proof**
- `grep -n "^| R326 " …/reports/cto-2026-10-03.md` → `332:| R326 | 10-05 06:19 ET | HIS RULING: A on all three — … second-writer survey gets its 5 read strings, this seat only; … | HIS RULING · APPROVED |`
- `git log -1 --format=%h -- …/cto-2026-10-03.md` → `6ac85389`; file not in `git status` modified list at session start.

**Line position**: line 2, directly after the one-line `MODEL: … SESSION: …` header, before the blank line and `# SURVEY: …` heading. `grep -c "^RULINGS:"` → 1. `git diff -U0` → `@@ -1,0 +2 @@` + `RULINGS: 2026-10-03 R326`.

**Allow-line read strings, unchanged**: (1) `Bash(COBALT_ENV=dev uv run cobalt db query --side system *)`, (2) `Bash(lsof -nP -iTCP:5432*)`, (3) `Bash(lsof -a -p *)`, (4) `Bash(ps -o *)`, (5) `Bash(sleep *)`. Not edited.

SURVEY RULINGS LINE ADDED · decisions: 2
