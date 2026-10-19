# draft-cos-gate-run — 2026-10-19

## §0 Headline
- DRAFTED `prompts/2026-10-19/873-cos-gate-run.md`: seat `cos-gate-run`, first pass runs X20, X11, X12, X3, X14, X17, X1, X13, X2, X10 in the design's order (`F20-FINAL-2026-10-11.md:82-91`); D14, agent stopped, X15, X18 are `NOT RUN` and wait for his word; a second pass on CONTINUE records them.
- One report `reports/cos-gate-run-2026-10-19.md`: `## RESULTS` 14 `GATE RESULT` lines in the owed-list order, `## DECISIONS` (his one question first), `## RECORDS`, last line `GATES DONE · ok · fail · not run`.
- No item names a shell command: the drafter wrote each probe as one `.venv/bin/python -c` or `launchctl` call on a `local.cos-gate-*` label; every session's tools are stubbed; no keychain command.
- The line as told (`acceptEdits`) is refused by `desk-launch.sh prompt` (decision 1). Committed nothing.

## DECISIONS
1. ASK DESK: `desk-launch.sh prompt` admits only `auto` or `plan` (`/Users/cobalt/.claude/ops/desk-launch.sh:780-784`, outside the repo, read on disk); the line carries `acceptEdits` as the card says, so the launch is refused. Default: the line stands; the desk launches it by a kind that admits `acceptEdits`, or changes the word to `auto`. [16:01]
2. ASK DESK: `launchctl` in `--allowedTools` passes only when the prompt's one `RULINGS:` line cites rows that are HIS RULING + APPROVED (`desk-launch.sh:785-790`). The drafter copied card 730's `R1055, R1112, R1833` (`808-deploy-f20-cos-card.md:8`). Default: the desk confirms them or names the row; refused → nothing runs. [16:01]
3. ASK DESK: the named build report `reports/f20-cos-fr1-build-2026-10-19.md` is on no branch (`git log --all` → nothing); the build report is `f20-cos-fr1-build-2026-10-18.md` (on main, last `83919213`; B0 lines `:79-89`). Default: the 10-18 file is the one. [16:01]
4. ASK DESK: `deploy-step-c.sh --bootstrap-only` admits any non-empty result (`ops/desk/deploy-step-c.sh:185-186`): a card with `FAIL` or `NOT RUN` lines passes. Default: the desk copies the 14 lines into a bootstrap-only card only when all 14 read `OK`. [16:01]
5. ASK DESK: the design names procedures, not commands (`F20-FINAL-2026-10-11.md:72-93`); every probe command in 873 is the drafter's, and `Bash(/Users/cobalt/cobalt/.venv/bin/python -c *)` is a wide allow string. Probes run the prod tree's venv in dev (no `COBALT_ENV`), so no `uv run` syncs it. Default: as drafted. [16:01]
6. ASK DESK: X11/X10 plant the user-config MCP server under a scratch HOME, never his `~/.claude.json`; whether the CLI authenticates under that HOME is unproven. Default: it cannot → both `NOT RUN` with the CLI's message. [16:01]
7. ASK DESK: X1/X13 (`:88`) ask for a run "after a reboot with no login shell"; 873 runs both as LaunchAgents in `gui/501` on the current boot (plists in `data/cos/gate/`, git-ignored at `.gitignore:6`). `claude auth status` as X1's status command is unproven. Default: the current boot stands; an unknown subcommand → X1 `FAIL` with the CLI's message. [16:01]
8. ASK DESK: X14/X17 need 20 synthetic DMs (`:86-87`); the repo fixture holds 3 posts (`tests/cobalt/fixtures/cos/dm-posts.redacted.json`). 873 carries 20 constructed DMs on stubbed tools; X17's pass rule (Sonnet's failed count and turns median not above Opus's) is the drafter's reading of `:87`. Default: as drafted. [16:01]
9. ASK DESK: X18 is "on dev" in the design (`:92`) and owed after his trading day by L79; no command is traced. Default: the desk relays the measured time in the CONTINUE; this seat restarts nothing. [16:01]
10. ASK DESK: X15 needs a DM on the dev bot, and `hitl.page_base_url` is null (`tunables.yaml:1038-1039`, the card refuses to send). Default: the desk relays his phone read; this seat sends no DM. [16:01]
11. ASK DESK: B0 also owes `cos.poll_interval_s`, `hitl.request_ttl_min` (both `value: null`, `tunables.yaml:1008-1009`, `:1026-1027`; `cos/session.py:76-85` raises on null) and the L7 / L41 fold texts; none is in the 14-item owed list (`data/deploy/bootstrap-owed.json:4`). Default: the desk rules them before any bootstrap-only card. [16:01]

## RECORDS
- `date` 15:54 at start, 16:01 at the draft. main `29250739` (`git rev-parse --short=8 main`); `git diff --stat main --` every cited repo file → nothing, so working-tree lines are main's.
- Read: `872-draft-cos-gate-run.md`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `topics/writing-rules.md`; precedent `868-draft-hub-cos-restart.md`.
- `git show main:` `808-deploy-f20-cos-card.md` (`:21` the LAUNCHD line), `730-f20-card.md` (`:42` B0, `:37` C4a), `F20-FINAL-2026-10-11.md` (`:72-93` experiments, `:119` R7/D14), `f20-cos-fr1-build-2026-10-18.md`.
- Grep: `f20-cos-fr1-check-2026-10-19.md` (no gate-item results); `CARD.md:69`; `DEPLOY-HUB.md:89-94`, `:145` (4.6L-BO); `deploy-step-c.sh:165-195`.
- Read on disk: `configs/cobalt/jobs.yaml:120-145` (`:136` the four duties); `ops/com.cobalt.cos.plist`; `ops/start_cos.sh`; `src/cobalt/cos/session.py`, `cli.py`, `run.py`, `tools.py`; `agents/registry.py`; `redact/guard.py:80`; `configs/cobalt/agents/cos.yaml`; `tunables.yaml:987-1046`; `data/deploy/bootstrap-owed.json`; `desk-launch.sh:125-150`, `:487-512`, `:770-830`.
- `ls`: `/opt/homebrew/bin/claude` → the claude-code CLI; `.venv/lib/python3.14/site-packages/claude_agent_sdk` present.

DRAFTED · decisions: 11
