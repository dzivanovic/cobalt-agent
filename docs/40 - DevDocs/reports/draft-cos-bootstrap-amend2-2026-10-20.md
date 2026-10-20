## §0 Headline
- Card 929 amended in place: three fixes, nothing else changed.
- FAIL 6: R2197, R2198 cited by row id.
- FAIL 10: smoke row 5 expectation is `` `0` ``; its Traceback / UNPROVEN / `FAILED:` text moved to `## RECORDS`.
- Brain L79: `WAITS:` gains `hitl.page_base_url set`; tunables 933 line added to `## RECORDS`.
- `--dry-run` not run (not permitted to me); form proved by reading the script.

## DECISIONS
- none

## RECORDS
- 2026-10-20 17:50 ET (`date`: Tue Oct 20 17:48:33 EDT 2026 at the reads).
- Edited: `prompts/2026-10-20/929-deploy-cos-bootstrap-card.md` (WAITS line; SMOKE READS row 5; `## RECORDS` last-but-one block). No commit.
- Row ids proved: `reports/cto-2026-10-20.md` holds row R2197 (X13 PASS) and row R2198 (bootstrap card brief) — Grep.
- Row 5 form proved against `git show main:ops/desk/deploy-smoke.sh`: expectation = text after the command up to the first `;`; now `` `0` `` matches the `` "`"*"`" `` case, `value_is` takes the last output line equal to `0`. Command shape `grep -c -F "CoS turn FAILED" <unquoted path>` matches the grep shape (no `$ \` ; & | < > ( ) * ? \`). I cannot run `--dry-run`: no Bash permission for it; the desk runs it once before first use.
- `watchdog.py:441-449` proved against `git show main:src/cobalt/jobs/watchdog.py`; `git diff main` of that file is empty, and Grep shows `if spec.label in owed:` at 441 through the not-loaded `findings.append` at 448 (the closing `continue` is 449). It is the owed-label branch: an owed, unloaded label is OWED, not red.
- Reads: card 929, card 937, `areas/cobalt.md`, `topics/writing-rules.md`, `ops/desk/deploy-smoke.sh` (main), `watchdog.py` (main + working tree), `reports/cto-2026-10-20.md` (Grep R2197/R2198).
- Not read: preflight report `reports/cos-bootstrap-preflight-2026-10-20.md`; the two fixes were taken from card 937's text.

DRAFTED · decisions: 0
