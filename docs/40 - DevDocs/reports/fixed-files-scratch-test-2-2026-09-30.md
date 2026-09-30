# Fixed-files scratch test 2 — 2026-09-30

Re-run of `plans/fixed-files-2026-09-30/DRAFT4-REPORT.md` `## UNTESTED` (brain's WHAT REMAINS step 2). Hub `384c5313` (`57`) owns 5, 6, 7; the desk ran 1–3 and 8 on probe sessions; 4 (CLOSE-HUB end to end) is OWED.

## Summary
| # | item | owner | result |
|---|---|---|---|
| 1 | real lines under `dontAsk`: a NEW file under a spaced `reports/**` glob | desk | PASS for the spaced Write and Edit (probe E e1/e2); the full real lines are not run |
| 2 | `Grep`, `Glob` under `dontAsk` | desk | PASS (probe E g1/g2) |
| 3 | three house spellings under `dontAsk` | desk | PASS for grok and agy; codex Sol METER until 10-04 14:06 (probe E h1–h3) |
| 4 | `CLOSE-HUB.md` end to end | desk | OWED |
| 5–7 | script, guard, `desk-context.sh` | hub | PENDING (`HUB2-RESULTS.md`) |
| 8 | the new desk denies on those exact paths | desk | PASS — `.git`, `.claude`, `cobalt/ops` refused with no dialog; control Write ok; no stray file (probe F) |

# PART 1 — probe E (verbatim)

# Probe E results
- step 0: Write result file — succeeded, no permission dialog.
- e1: Write `.../docs/40 - DevDocs/reports/e1.md` content `e1` — result: "File created successfully at: /Users/cobalt/cobalt-wt/scratch-fixed-0930/probes/dontask/docs/40 - DevDocs/reports/e1.md"; no permission dialog.
- e2: Edit e1.md `e1` -> `e1 edited` — result: "The file .../docs/40 - DevDocs/reports/e1.md has been updated successfully."; no permission dialog.
- g1: Grep pattern `PROBE` path probes/dontask — result: "Found 4 files: PROBE-E.md, probe-d-result.md, PROBE-D.md, PROBE-B.md"; no permission dialog.
- g2: Glob `*.md` path probes/dontask — result: PROBE-B.md, PROBE-D.md, probe-d-result.md, PROBE-E.md, docs/40 - DevDocs/reports/e1.md, probe-e-result.md; no permission dialog.
- h1a: Bash `cd /Users/cobalt/cobalt-wt/agy-trial` — result: "(Bash completed with no output)"; no permission dialog.
- h1: Bash `grok --sandbox cobalt-job -p "Reply with only the word OK."` (cwd agy-trial) — result: "OK"; no permission dialog.
- h2: Bash `agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 20m --add-dir /Users/cobalt/cobalt-wt/agy-trial --print="Reply with only the word OK."` — result: "OK."; no permission dialog.
- h3: Bash `codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null` — result: Exit code 1; codex v0.154.0 ran (workdir agy-trial, sandbox read-only, effort high) then "ERROR: You've hit your usage limit. Upgrade to Pro (https://chatgpt.com/explore/pro), visit https://chatgpt.com/codex/settings/usage to purchase more credits or try again at Oct 4th, 2026 2:06 PM." (printed twice); no permission dialog.
PROBE E DONE

# PART 2 — probe F (verbatim)

# PROBE F results
- step 0: Write probe-f-result.md -> "File created successfully at: .../probe-f-result.md (file state is current in your context — no need to Read it back)". No dialog.
- f2: Write /Users/cobalt/.claude/probe-f-f2.txt content `f2` -> "<tool_use_error>File is in a directory that is denied by your permission settings.</tool_use_error>". No dialog.
- f3: Write .../probes/dontask/f3.txt content `f3` -> "File created successfully at: /Users/cobalt/cobalt-wt/scratch-fixed-0930/probes/dontask/f3.txt (file state is current in your context — no need to Read it back)". No dialog.
- f4: Write /Users/cobalt/cobalt/ops/probe-f-f4.txt content `f4` -> "<tool_use_error>File is in a directory that is denied by your permission settings.</tool_use_error>". No dialog.
- f1: Write /Users/cobalt/cobalt/.git/probe-f-f1.txt content `f1` -> "<tool_use_error>File is in a directory that is denied by your permission settings.</tool_use_error>". No dialog.
PROBE F DONE
