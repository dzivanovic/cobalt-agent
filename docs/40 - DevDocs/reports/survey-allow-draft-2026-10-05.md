## §0 Headline
- Survey prompt `01-second-writer-survey.md` launch line: `"Write"` and `"Edit"` replaced by one path-scoped Edit rule.
- Report path in the prompt matches the rule exactly.
- `git diff` shows one line changed (1 insertion, 1 deletion), the launch line.
- Body writes no file other than the report.

## DECISIONS
- None.

## RECORDS
- Old: `--allowedTools "Read" "Write" "Edit" "Bash(COBALT_ENV=dev uv run cobalt db query --side system *)" …`
- New: `--allowedTools "Read" "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/second-writer-survey-2026-10-05.md)" "Bash(COBALT_ENV=dev uv run cobalt db query --side system *)" …`
- Body grep (write/edit/create/append/save): only line 50 "Write the report last" and line 1 "Write only the report" ask for a write; both name the report. No FAIL.

SURVEY ALLOW LINE CHANGED · decisions: 0
