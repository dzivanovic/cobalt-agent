# Gain-measure survey prompt — preflight

Prompt: `prompts/2026-10-05/09-gain-measure-survey.md` · read-only, one file written (this report).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `grep -n "^| R362 " reports/cto-2026-10-05.md` | `35:| R362 \| 10-05 07:09 ET \| HIS RULING (brain relay): a drafter now writes a read-only gain-measure survey prompt … \| HIS RULING · APPROVED \|` | OK |
| 1b | `git -C /Users/cobalt/cobalt log -1 --format=%h -S"\| R362 \|" -- reports/cto-2026-10-05.md` | `f309f2dc` (committed) | OK |
| 2 | Read of prompt line 1 (launch line) | One launch line. `desk-launch.sh prompt` on `…/prompts/2026-10-05/09-gain-measure-survey.md` (its own path); `--model claude-sonnet-5-5`; `--remote-control gain-survey --name gain-survey`; `--disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" "Bash(git commit*)" "Bash(awk *)"`; allow list holds no awk, no `bypassPermissions`, no DB, `uv run` or production command; Write/Edit only, scoped by the SESSION text to the report | OK |
| 3 | Read of prompt lines 1, 9, 38 | SESSION: "read-only: no database, no code, no production command, no git write… Write and Edit touch the report only." RULES line 9: "From a job report read only `## §0`, `## DECISIONS`, the L68 GATE and lock lines (found by `grep -n`) and the last line (`tail -n 1`…). Never a whole job report." Report path is `reports/gain-measure-survey-2026-10-05.md` | OK |
| 4a | `ls -1` of the 14 named SOURCE files (cto ×3, close ×6, brain-direction-2026-10-02, seat-usage, job-stats-2026-09-30, deploy-s3-1005, writing-rules) plus `01-second-writer-survey.md` | all 15 listed, no error | OK |
| 4b | `ls -1 …/deploy-*-100[3-5].md` | `deploy-s3-1005`, `deploy-set1-1003`, `deploy-set2-1003`, `deploy-set2b-1003`, `deploy-set2c-1003`, `deploy-set2d-1003`, `deploy-set3-1004`, `deploy-set3b-1004` | OK |
| 4c | `sed -n '143,149p' reports/desk-tools-a-check-2026-10-02.md` | (a) `595.72s (0:09:55)`; (b) lock taken `13:20:16 EDT`; (c) `709.60s (0:11:49)`; (c3) `220.14s (0:03:40)`; (f) released `13:37:22 EDT` → 13:20:16 to 13:37:22 = 17 min 06 s | OK |
| 5 | Read of prompt lines 1, 19–38 | Q1–Q7 present and match the order; "not recorded" rule (RULES line 7); report shape §0 Headline / TABLE / DECISIONS / RECORDS; stop line `SURVEY DONE · jobs: <n> · not recorded: <n>` or `FAILED: <reason>`; timing line: "if its window meets the second-writer survey (17:5x), the second-writer survey runs first" | OK |
| 6a | `git -C /Users/cobalt/cobalt diff --stat -- prompts/2026-10-05/09-gain-measure-survey.md` | empty | OK |
| 6b | `git -C /Users/cobalt/cobalt log -1 --format=%h -- prompts/2026-10-05/09-gain-measure-survey.md` | `d8cefe3a` (on main) | OK |

Notes (not fails):
- The baseline "17 min 06 s" is not a literal in lines 143–149; it is the difference of the two quoted times. The 709.60 / 595.72 / 220.14 values are literal.
- Baseline "14 lock FAILED on 10-02" is the order's own figure. `grep -c -i "lock FAILED" reports/cto-2026-10-02.md` → `4` (lines, not occurrences), so the 14 was not reproduced by me. The prompt only quotes it beside the results.

## ISSUES

None.

PREFLIGHT DONE · prompt: 09 · checks: 10 · fails: 0 · ready: YES
