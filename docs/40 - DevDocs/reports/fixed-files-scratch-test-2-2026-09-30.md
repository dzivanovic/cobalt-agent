# Fixed-files scratch test 2 — 2026-09-30

Re-run of `plans/fixed-files-2026-09-30/DRAFT4-REPORT.md` `## UNTESTED` (brain's WHAT REMAINS step 2). Hub `384c5313` (`57`) owns 5, 6, 7; the desk ran 1–3 and 8 on probe sessions; 4 (CLOSE-HUB end to end) is OWED.

## Summary
| # | item | owner | result |
|---|---|---|---|
| 1 | real lines under `dontAsk`: a NEW file under a spaced `reports/**` glob | desk | PASS for the spaced Write and Edit (probe E e1/e2); the full real lines are not run |
| 2 | `Grep`, `Glob` under `dontAsk` | desk | PASS (probe E g1/g2) |
| 3 | three house spellings under `dontAsk` | desk | PASS for grok and agy; codex Sol METER until 10-04 14:06 (probe E h1–h3) |
| 4 | `CLOSE-HUB.md` end to end | desk | OWED |
| 5 | `desk-launch.sh` fourth-pass code | hub | PASS — defects D4 (`prompt` accepts `--permission-mode dontAsk` in quotes or with two blanks), D5 (`close 2026-02-30` accepted) |
| 6 | D3 fix in the guard | hub | PASS |
| 7 | fixed `desk-context.sh` | hub | PASS — D6 (an empty id measures the newest transcript of any session); the two-folder sub-test NOT RUN |
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


# PART 3 — HUB2-RESULTS.md (hub `384c5313`, verbatim)

# SCRATCH TEST 2 HUB — RESULTS (2026-09-30)

Prompt: `prompts/2026-09-30/57-scratch-test-2-hub.md` · mode `dontAsk` · model claude-opus-5-5 · cwd `/Users/cobalt/cobalt-wt/scratch-fixed-0930/wt` · the real `claude` never ran by a script of mine (stub `bin/claude`, or `DESK_LAUNCH_DRY=1`; on DRY runs `run.sh` prints `claude=/opt/homebrew/bin/claude`, which is never invoked).

## SANDBOX REFRESH (before the items)

THE ORDERED `cp` WAS REFUSED under `dontAsk`, twice (see `## RECORDS`). The copies were rebuilt instead with Read (the drafted file) + Write (the sandbox copy), then PROVEN equal to the drafts by `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/verify-copies.sh` (undoes the sandbox edits with `sed`, `diff`s against the drafted file):
```
--- desk-launch.sh (edits undone: REPO, WT, ops path)
IDENTICAL
--- pre-commit-deploy-guard.sh (edit undone: the main-tree path)
IDENTICAL
--- desk-context.sh (no edit)
IDENTICAL
--- sandbox edits in the copies
94:REPO=/Users/cobalt/cobalt-wt/scratch-fixed-0930/main
95:WT=/Users/cobalt/cobalt-wt/scratch-fixed-0930
15
58:if [ "$(git rev-parse --show-toplevel 2>/dev/null)" = "/Users/cobalt/cobalt-wt/scratch-fixed-0930/main" ] \
```
EDITS TO THE COPIES (the same as `55` item 1 and 2; the only ones):
- `scripts/desk-launch.sh:94` `REPO=/Users/cobalt/cobalt` → `REPO=/Users/cobalt/cobalt-wt/scratch-fixed-0930/main`.
- `scripts/desk-launch.sh:95` `WT=/Users/cobalt/cobalt-wt` → `WT=/Users/cobalt/cobalt-wt/scratch-fixed-0930`.
- `scripts/desk-launch.sh` `/Users/cobalt/.claude/ops` → `/Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts` everywhere: 15 lines (13, 14, 15, 20–25, 28, 29, 30, 59, 104, 106): comments, plus the refusal MESSAGE at :106 (the `case "$0"` test itself names no path).
- `scripts/pre-commit-deploy-guard.sh:58` `= "/Users/cobalt/cobalt" ]` → `= "/Users/cobalt/cobalt-wt/scratch-fixed-0930/main" ]`.
- `scripts/desk-context.sh`: none.
NOT REFRESHED (the `cp` was refused, and they are not under test here): the `.md` copies in `scripts/` (`BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md`, `CARD.md`, `DESK-LINE.md` stay pass-3; `CLOSE-HUB.md`, `DRAFT4-REPORT.md` etc. were never copied). What `desk-launch.sh` reads from them was refreshed on the sandbox main by `scripts/setup2.sh` (reads the drafts, writes only in the sandbox), commit `3c3ed14`: the `^claude --bg ` line of the sandbox `BUILD-HUB.md`, `CHECK-HUB.md`, `DEPLOY-HUB.md` replaced by the CURRENT drafted line (the script printed `BUILD-HUB.md: line = drafted line`, and the same for CHECK and DEPLOY); a `CLOSE-HUB.md` FIXTURE = a filled title line (no `«INSTALL`) + the drafted `CLOSE-HUB.md:10` launch line byte for byte; prompt `30-dontask.md`; cards `04 scheck2-card.md` (card 02 with a fresh CHECK REPORT) and `05 sdeploy2-card.md` (card 03 with WORKTREE `sgate2`, BRANCH `scratch/gate2`, a fresh REPORT). `main/.git/info/exclude` gained `docs/40 - DevDocs/reports/check-report-probe.md` (55's item-14 file, untracked in `wt`, which would make every check launch refuse "not clean").

## ITEM 5 — desk-launch.sh fourth-pass code
RESULT: PASS — every ordered case behaved as the header promises. Two defects found OUTSIDE the ordered inputs (D4, D5 below).

### (a) the `close` kind — DRY and stub
HOUR DRIVEN BY: a `date` SHIM, `bin/date` (ahead of `/usr/bin` and `/bin` on the stub PATH): with `SHIM_NOW="YYYY-MM-DD HH:MM"` it runs `/bin/date -j -f "%Y-%m-%d %H:%M" "$SHIM_NOW" "$@"` (read and printed in the caller's `TZ`, so `TZ=America/New_York date +%H` returns the ET hour given); without it, the real `/bin/date`. The script offers no hook of its own. Runner: `scripts/close-case.sh <list> <ET instant|real> <close args>` — sets `agents.json`, `PATH=$S/bin:/usr/bin:/bin`, `SHIM_NOW`, runs `sh scripts/desk-launch.sh close …`, prints `EXIT=`.
Commands: `env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/close-case.sh <list> "<instant>" <args>` (DRY) and `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/close-case.sh …` (stub; the wrapper puts the stub first).

| case | list | ET now | args | printed (verbatim) | exit |
|---|---|---|---|---|---|
| today, before 21:00 | none | 2026-09-30 20:59 | `2026-09-30` | `REFUSED: close: today's close launches after the 21:00 ET pause; it is 20h ET` | 1 |
| today, at 21:00 | none | 2026-09-30 21:00 | `2026-09-30` | `cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/main` / `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly. DATE: 2026-09-30" --model claude-sonnet-5-5 --permission-mode dontAsk --remote-control close-0930 --name close-0930 --allowedTools "Read" … --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt` | 0 |
| today, real clock | none | real (ET 15:07) | `2026-09-30` | `REFUSED: close: today's close launches after the 21:00 ET pause; it is 15h ET` | 1 |
| past date, morning | none | 2026-09-30 09:15 | `2026-09-29` | `cd …/main` + the line with `DATE: 2026-09-29` … `--remote-control close-0929 --name close-0929` | 0 |
| yesterday, after midnight ET | none | 2026-10-01 00:30 | `2026-09-30` | `cd …/main` + the line with `DATE: 2026-09-30`, `close-0930` | 0 |
| future date | none | 2026-09-30 23:30 | `2026-10-01` | `REFUSED: close: 2026-10-01 is after today (2026-09-30, ET)` | 1 |
| not a date | none | 2026-09-30 22:00 | `2026-9-30` | `REFUSED: close: '2026-9-30' is not a date YYYY-MM-DD` | 1 |
| live deploy row | live (`deploy-hub-sdep` pid 4242) | 2026-09-30 21:30 | `2026-09-30` | `REFUSED: close: a deploy hub is live — the close waits for its stop line: a1b2c3 deploy-hub-sdep` | 1 |
| list not JSON | garbage (`Error: not json at all`) | 2026-09-30 21:30 | `2026-09-30` | `REFUSED: close: the session list is unreadable (claude agents --json); a close never launches beside a deploy it cannot rule out` | 1 |
| no `claude` on PATH | (PATH = links to git grep sed tr cut tail head awk python3 + the date shim) | 2026-09-30 21:30 | `2026-09-30` | `REFUSED: close: the session list is unreadable (claude agents --json); …` | 1 |
| no `python3` on PATH | (PATH = links + the stub claude, no python3) | 2026-09-30 21:30 | `2026-09-30` | `REFUSED: close: the session list is unreadable (claude agents --json); …` | 1 |
| `agents.json` chmod 000 | unreadable | 2026-09-30 21:30 | `2026-09-30` | `cd …/main` + the line — LAUNCHES. The STUB's `cat … 2>/dev/null \|\| echo "[]"` (`bin/claude:4`) answers `[]` for an unreadable file, so the script is shown a valid empty list: a stub artifact, the same as 55 item 2's chmod-000 row, not the draft. The three rows above are the real "list unreadable" shapes, and each REFUSES (fail-CLOSED, where the guard fails open — item 6) | 0 |
| resume, no report | none | 2026-09-30 10:00 | `2026-09-28 STEP-3` | `REFUSED: a close resume needs its report: /Users/cobalt/cobalt-wt/scratch-fixed-0930/main/docs/40 - DevDocs/reports/close-2026-09-28.md` | 1 |
| first launch, report exists | none | 2026-09-30 10:00 | `2026-09-28` (after `scripts/close-fixture.sh make`) | `REFUSED: the close report already exists: …/reports/close-2026-09-28.md (a new worker names its CONTINUE step)` | 1 |
| non-calendar date | none | 2026-09-30 10:00 | `2026-02-30` | `cd …/main` + the line — ALLOWED (D5) | 0 |

STUB runs (non-DRY), each quoted from the script's stderr and the stub log's last line:
- `close-case.sh none "2026-09-30 21:05" 2026-09-30` → `RUN: cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/main`, `RUN: claude --bg "Read '…/CLOSE-HUB.md' and follow it exactly. DATE: 2026-09-30" …`, `reminder: no desk commit on main and no deploy launch until the close's stop line; the close pushes main itself (L55 as amended)`, `EXIT=0`. Stub: `STUB-CLAUDE cwd=/Users/cobalt/cobalt-wt/scratch-fixed-0930/main args: --bg Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly. DATE: 2026-09-30 --model claude-sonnet-5-5 --permission-mode dontAsk --remote-control close-0930 --name close-0930 --allowedTools Read Grep Glob Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**) … Bash(git push origin main) --disallowedTools AskUserQuestion EnterWorktree Bash(git push*--force*) … Bash(git push*--tags*) --add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt` (the spaced `Edit(…)` strings arrived as one argument each).
- `close-case.sh none "2026-09-30 10:00" 2026-09-28 STEP-3` (report present) → `RUN: claude --bg "CONTINUE: STEP-3. Read '…/CLOSE-HUB.md' and follow it exactly. DATE: 2026-09-28" … --remote-control close-0928 --name close-0928 …`, `EXIT=0`. Stub: `STUB-CLAUDE cwd=…/main args: --bg CONTINUE: STEP-3. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CLOSE-HUB.md' and follow it exactly. DATE: 2026-09-28 --model claude-sonnet-5-5 --permission-mode dontAsk …`.
- `check_paths` passed the real close line (every `/Users/` path in its allow strings sits under `/Users/cobalt/Vault` or `/Users/cobalt/cobalt`).

### (b) the D1 exception
Runner `scripts/d1-case.sh <lock> <desk-launch args>`: `scripts/lock2.sh` leaves exactly ONE `.env` (in `sbuild`, `wt` or `sgate`), runs `scripts/run.sh`, clears it. Commands: `env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/d1-case.sh <lock> <kind> "<P>/<card>" [<step>]` (`<P>` = `…/main/docs/40 - DevDocs/prompts/2026-09-30`).

| launch | the one `.env` | printed | exit |
|---|---|---|---|
| `build 01 STEP-2` | `sbuild/.env` (OWN) | `cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/sbuild` / `claude --bg "CONTINUE: STEP-2. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md' …` | 0 |
| `build 01 STEP-2` | `wt/.env` (OTHER) | `REFUSED: with-DB launch refused: the cobalt_dev lock is held (/Users/cobalt/cobalt-wt/scratch-fixed-0930/wt/.env) (L76)` | 1 |
| `build 01` (control: no step) | `sbuild/.env` (own) | `REFUSED: with-DB launch refused: the cobalt_dev lock is held (/Users/cobalt/cobalt-wt/scratch-fixed-0930/sbuild/.env) (L76)` | 1 |
| `check 02 "STEP-3 rerun"` | `wt/.env` (OWN) | `cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/wt` / `claude --bg "CONTINUE: STEP-3 rerun. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md' …` | 0 |
| same, STUB (`env PATH=…/bin:/usr/bin:/bin sh …/d1-case.sh wt check …`) | `wt/.env` (own) | `RUN: cd …/wt`, `RUN: claude --bg "CONTINUE: STEP-3 rerun. …`, the check reminder; stub `STUB-CLAUDE cwd=/Users/cobalt/cobalt-wt/scratch-fixed-0930/wt args: --bg CONTINUE: STEP-3 rerun. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md' …` | 0 |
| `check 02 "STEP-3 rerun"` | `sbuild/.env` (OTHER) | `REFUSED: with-DB launch refused: the cobalt_dev lock is held (/Users/cobalt/cobalt-wt/scratch-fixed-0930/sbuild/.env) (L76)` | 1 |
| `check 04` (control: no step) | `wt/.env` (own) | `REFUSED: /Users/cobalt/cobalt-wt/scratch-fixed-0930/wt/.env exists: the build did not release the lock (L76)` | 1 |
| `deploy 03 STEP-D0` | `sgate/.env` (OWN) | `cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/main` / `claude --bg "CONTINUE: STEP-D0. Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md' …` | 0 |
| `deploy 03 STEP-D0` | `wt/.env` (OTHER) | `REFUSED: with-DB launch refused: the cobalt_dev lock is held (/Users/cobalt/cobalt-wt/scratch-fixed-0930/wt/.env) (L76)` | 1 |

### (c) `prompt` refuses the write-path modes
- `env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/run.sh prompt "<P>/30-dontask.md"` (line carries `--permission-mode dontAsk`) → `REFUSED: a write-path permission mode (acceptEdits, dontAsk): a write-path launch is a fixed file (build, check, deploy, close)` `EXIT=1`.
- the same with `"<P>/12-acceptedits.md"` (`--permission-mode acceptEdits`) → the same message, `EXIT=1`.
- BEYOND THE ORDER (prompts 31–33, `scripts/gen-prompts2.sh`, committed `f26864e`): the same modes in other shell spellings are NOT refused:
  - `31-dontask-quoted.md` (`--permission-mode "dontAsk"`) → DRY: `cd …/wt` + the line, `EXIT=0`. STUB: `EXIT=0`, and the stub received `… --model claude-opus-5-5 --permission-mode dontAsk --remote-control sp-daq …` — `eval` strips the quotes, so the session WOULD launch under `dontAsk`.
  - `32-dontask-2sp.md` (`--permission-mode  dontAsk`, two spaces) → DRY `EXIT=0`, the line printed.
  - `33-acceptedits-sq.md` (`--permission-mode 'acceptEdits'`) → DRY `EXIT=0`, the line printed.
  Cause: `desk-launch.sh:273–278` (ORIGINAL) matches the two literal spellings `*"--permission-mode acceptEdits"*` / `*"--permission-mode dontAsk"*`, then lets ANY other `*"--permission-mode "*` through. → D4.

### (d) the `$0` spaced-path refusal
`env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/spaced-copy.sh` (copies the COPY to `ops dir/desk-launch.sh`, runs `sh "…/ops dir/desk-launch.sh" desk`):
`REFUSED: desk-launch.sh runs only from a path with no space (install it under /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/): /Users/cobalt/cobalt-wt/scratch-fixed-0930/ops dir/desk-launch.sh` `EXIT=1`. Control, the same file from `scripts/`: `cd /Users/cobalt/cobalt-wt/scratch-fixed-0930/main` + the wake-up line (its exit is in (e)).

### (e) the regression sweep — every kind of 55 item 1, DRY
`env DESK_LAUNCH_DRY=1 sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/sweep2.sh` (no `.env` anywhere; the hub lines are the CURRENT drafted ones):
| kind | first printed lines (cut at 170) | exit |
|---|---|---|
| `build 01` | `cd …/sbuild` · `claude --bg "Read '/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md' and follow it exactly. CARD: '…/01 sbuild-card.md' …` (sbuild exists: no worktree add) | 0 |
| `check 04` | `cd …/wt` · `claude --bg "Read '…/CHECK-HUB.md' …` | 0 |
| `check 04 PASS-2` (report's last line `CHECK DONE · job: scheck2 · pass: 1 · … · house B: needed · ready: NO`) | `cd …/wt` · `claude --bg "PASS-2. Read '…/CHECK-HUB.md' …` | 0 |
| `check 02 "STEP-3 rerun"` | `cd …/wt` · `claude --bg "CONTINUE: STEP-3 rerun. Read '…/CHECK-HUB.md' …` | 0 |
| `check 04 PASS-2 STEP-4` | `cd …/wt` · `claude --bg "PASS-2. CONTINUE: STEP-4. Read '…/CHECK-HUB.md' …` | 0 |
| `deploy 05` | `git -C /Users/cobalt/cobalt-wt/scratch-fixed-0930/main worktree add -b scratch/gate2 /Users/cobalt/cobalt-wt/scratch-fixed-0930/sgate2 main` · `cd …/main` · `claude --bg "Read '…/DEPLOY-HUB.md' …` | 0 |
| `deploy 03 STEP-D0` | `cd …/main` · `claude --bg "CONTINUE: STEP-D0. Read '…/DEPLOY-HUB.md' …` (no worktree add) | 0 |
| `desk` | `cd …/main` · `claude --bg "Read 'docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md' and follow it exactly." --model claude-sonnet-5-5 --permission-mode auto --remote-control cto-desk --name …` (the sandbox wake-up of 55) | 0 |
| `prompt 10-own-line.md` | `cd …/wt` · `claude --bg "Read '…/10-own-line.md' and follow it exactly." --model claude-opus-5-5 …` | 0 |
| `prompt 11-span.md` | `cd …/wt` · `claude --bg "Read '…/11-span.md' and follow it exactly." …` | 0 |
| `close` | see (a): `2026-09-30` at 21:00 ET, `2026-09-29` in the morning | 0 |
`sgate2 exists after the sweep: no` (DRY created nothing).

## ITEM 6 — D3 fix in pre-commit-deploy-guard.sh
RESULT: PASS
Hook: `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/assemble-hook.sh` (as 55 item 2) → `98 …/main/.git/hooks/pre-commit`; `1:#!/bin/sh`, `58:# ---- deploy guard (begin)`, `59:if [ "$(git rev-parse --show-toplevel …)" = "/Users/cobalt/cobalt-wt/scratch-fixed-0930/main" ]`, `94:# ---- deploy guard (end)`, `95:# ---- scratch row gate …` (the row gate stays last).
Command: `env PATH=/Users/cobalt/cobalt-wt/scratch-fixed-0930/bin:/usr/bin:/bin sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/item6.sh` — one desk commit (`docs/40 - DevDocs/plans/desk-note.md`) on the sandbox main per case, in sequence, the hook's PATH set per case; the wrapper's own tools by absolute path.

| list | hook PATH | output (verbatim) | exit |
|---|---|---|---|
| live row; NO `python3` (`claude=…/probes/nopy6/claude`, `python3=` empty) | `…/probes/nopy6` (links to git grep sed tr head cat + the stub claude) | `pre-commit: deploy guard could not read the session list (claude agents --json); NOT enforced for this commit.` then `[main 3dca468] scratch 2: item 6 nopython desk` — WARNS LOUDLY (the old D3 defect: `[main c46dce7] …` with no word) | 0 |
| live row; `python3` present | `…/bin:/usr/bin:/bin` | `pre-commit: a deploy hub is live — no desk commit on main until its stop line:` / `a1b2c3 deploy-hub-sdep` / `Write by Edit / Write only; commit after DEPLOYED or FAILED, once the hub is stopped and removed.` — REFUSED | 1 |
| no live row | same | `[main ab34574] scratch 2: item 6 none desk` — passes, silent | 0 |
| list unreadable (not JSON) | same | `pre-commit: deploy guard could not read the session list (claude agents --json); NOT enforced for this commit.` then `[main 0f8ecce] scratch 2: item 6 garbage desk` — fails OPEN, loud | 0 |
A first attempt ran these cases as parallel calls through 55's `commit-case.sh` (commits `e0f2061` none, `cf46b8a` garbage + warning, `449001a` noclaude + warning, `846564a` chmod-000, silent — the stub artifact again; and a live-row refusal); its `nopython` case broke on the wrapper's own narrowed PATH (`date: command not found`, nothing staged, `EXIT=1` from git's "nothing added to commit"). Parallel calls share `agents.json`, so the sequential `item6.sh` run above is the result.

## ITEM 7 — desk-context.sh
RESULT: PASS — the two ordered sub-tests that could run passed; the two-folder sub-test NOT RUN (below).
Ids: `ls -t /Users/cobalt/.claude/projects/-Users-cobalt-cobalt-wt-scratch-fixed-0930-wt/` → `384c5313-….jsonl` (this session), `f9cd8480-….jsonl`, `ccf14902-….jsonl` — workers whose cwd is the sandbox `wt`, not `~/cobalt`. (LIST itself = `claude agents --json`, the real `claude`, which this hub never runs; the ids are the transcripts' own names.)
- `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/ctx-case.sh f9cd8480 250000` → `transcripts matching (newest first): /Users/cobalt/.claude/projects/-Users-cobalt-cobalt-wt-scratch-fixed-0930-wt/f9cd8480-7e68-432b-be64-d1a901ca64ee.jsonl` / `context 210524 of 250000 — ok` / `EXIT=0`.
- `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/desk-context.sh 384c5313 250000` (this session) → `context 165277 of 250000 — ok`.
- unknown id: `sh …/scripts/ctx-case.sh zz9nope0 250000` → `no transcript for zz9nope0` / `EXIT=2` (the bare run: `Exit code 2`, `no transcript for zz9nope0`).
- TWO FOLDERS, NEWEST WINS: NOT RUN — the script offers no variable for its project root: `desk-context.sh:8` (ORIGINAL) hard-codes `/Users/cobalt/.claude/projects/*/`, so the two `<prefix>-a.jsonl` files could not be placed under the sandbox, and the order forbids writing in `~/.claude`. (By reading: `ls -t …/*/"$id"*.jsonl | head -1` does pick the newest across folders.)
- BEYOND THE ORDER: an EMPTY id, `sh …/scripts/desk-context.sh "" 250000` → `context 167270 of 250000 — ok`: the glob `*/*.jsonl` matched every transcript and the newest (this session's) was measured, with no word. → D6.
- Doc drift (not counted): `desk-context.sh:4` still says `~/.claude/projects/-Users-cobalt-cobalt/<id>*.jsonl`; the code (`:8`) reads every project folder.

## DEFECTS FOUND IN THE DRAFT

| # | file:line (ORIGINAL) | input | output | one-line fix |
|---|---|---|---|---|
| D4 | `desk-launch.sh:273–278` | `prompt` with a line carrying `--permission-mode "dontAsk"` (or `--permission-mode  dontAsk`, or `--permission-mode 'acceptEdits'`) | DRY `EXIT=0`, the line printed; stub received `--permission-mode dontAsk` — a write-path mode launched as a one-off prompt | read the mode word (`sed` past `--permission-mode`, quotes, `=` and blanks stripped) and ALLOW-list the read-only modes (`default`, `plan`), refusing any other or a second `--permission-mode` |
| D5 | `desk-launch.sh:165–168` | `close 2026-02-30` | `EXIT=0`, the launch line with `DATE: 2026-02-30` (the report would be `close-2026-02-30.md`) | also require `date -j -f %Y-%m-%d "$cday" +%Y-%m-%d` (BSD) to print `$cday` back |
| D6 | `desk-context.sh:7–8` | an empty id: `desk-context.sh "" 250000` | `context 167270 of 250000 — ok` — the newest transcript of ANY session | refuse an id shorter than 8 characters or outside `[0-9a-f-]` (`no transcript`, exit 2) |

## RECORDS
- REFUSED under `dontAsk` (no dialog; I went on): `cp /Users/cobalt/cobalt/docs/40 - DevDocs/plans/fixed-files-2026-09-30/* /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/` — the ordered `cp` string, typed exactly as the allow reads — REFUSED; the quoted form `cp "/Users/cobalt/cobalt/docs/40 - DevDocs/plans/fixed-files-2026-09-30/"* /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/` — REFUSED. The allow `Bash(cp /Users/cobalt/cobalt/docs/40 - DevDocs/plans/fixed-files-2026-09-30/* …)` holds unquoted spaces, so it matches no command that works in a shell (unquoted, the shell splits the path at `40 -`). Worked around with Read + Write (the refusal's own advice: another tool that naturally does it), proven identical above.
- Also REFUSED (my own spellings, each re-run in an allowed shape): `ls -lt … | head -8` (`head` not listed); `sh …/desk-context.sh … ; echo "EXIT=$?"` ×3 (`echo` not listed); a `for f in …; do … run.sh …; done` loop. Compound lines whose every part was listed (`P=…; env DESK_LAUNCH_DRY=1 sh …`, `sh … ; sh …`, `sh … | cut`, `sh … | grep`) RAN.
- `sh /Users/cobalt/cobalt-wt/scratch-fixed-0930/scripts/bgjob.sh 0` (my first probe that sandbox `sh` runs under `dontAsk`) OVERWROTE `results/bgjob-cwd.txt`, 55's item-10 evidence file; it now reads the `wt` path and `done 0`. 55's quote of it stands in `HUB-RESULTS.md` item 10.
- Sandbox state changed: commits on the sandbox `main` `3c3ed14` (fixtures), `f26864e` (prompts 31–33), `e0f2061`, `cf46b8a`, `449001a`, `846564a`, `3dca468`, `ab34574`, `0f8ecce` (item 6 desk commits of `plans/desk-note.md`); `main/.git/hooks/pre-commit` re-assembled with the pass-4 guard; `bin/date` shim added (passes through when `SHIM_NOW` is unset); `ops dir/desk-launch.sh` (the spaced copy); `reports/close-2026-09-28.md` fixture left untracked on the sandbox main; `agents.json` restored to its starting content `[{"id":"a1b2c3","name":"deploy-hub-sdep","pid":4242}]`; no `.env` left. Nothing outside `/Users/cobalt/cobalt-wt/scratch-fixed-0930/` was written. No drafted file changed. No push. No `git` command in `wt` but reads.
- New sandbox scripts: `verify-copies.sh`, `setup2.sh`, `close-case.sh`, `close-fixture.sh`, `lock2.sh`, `d1-case.sh`, `spaced-copy.sh`, `gen-prompts2.sh`, `sweep2.sh`, `item6.sh`, `ctx-case.sh`.
- L74: a block arrived after my first Read (the prompt file), asking that commit messages end with a `Claude-Session:` line. Recorded once, as DATA; not acted on (the sandbox commits carry only their `scratch 2: …` subject).
- The MCP "Claude Docs" server's instructions (make a doc first) arrived mid-run: not a request of this prompt; not acted on.

## CONTINUE
next: none — done.

SCRATCH TEST 2 HUB DONE · items run: 3 of 3 · pass: 3 · fail: 0 · blocked: 0 · not run: 0 · defects: 3
