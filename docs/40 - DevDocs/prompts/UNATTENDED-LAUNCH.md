# UNATTENDED LAUNCH — the standard for every session the desk starts (L62)

## 1. Before launch — the desk
1. Read the prompt end to end. List every command shape beyond plain reading, editing inside the session's own worktree, or `uv run pytest`: production reads, credential-file copies, vault-token fetches, dev DB migrations and rollbacks, other houses' CLIs (`claude -p`, `agy`, `grok`, `codex`), git history operations, anything outside the worktree. Known denial classes: `[Production Reads]`, `[Production Deploy]` (also cobalt_dev rollbacks), `[Credential Materialization]`, `[Credential Exploration]`, `[Git Destructive]`, `[Create Unsafe Agents]`, `[Self-Modification]`, `[Auto-Mode Bypass]`.
2. APPROVAL LIST: one row per rule — the exact `Bash(<prefix> *)`, what it is for, what it can touch, what it never touches. Add the NEVER block: push, `bypassPermissions`, `--allow-prod` outside a deploy prompt, production vault writes, `launchctl`, another seat's config file.
3. Show him the list once, in the desk chat, before anything starts; his approval is a §4 row. A list already approved for the same job shape is reused from the prompt's launch line, never brought again.
4. Launch line (the SEAT PROFILE's LAUNCH): `claude --bg "Read '<prompt file>' and follow it exactly." --model <m> --remote-control <job> --allowedTools "<rule>" … --disallowedTools "AskUserQuestion" "EnterWorktree" "Bash(git push*)" --add-dir …`. Per session; never `bypassPermissions`; never push.
5. After launch: VIEW it in a job-named herdr tab; record id, pid, tab and the approved list in the desk report's §5 sessions table.

## 2. Inside every prompt — the blocks under the launch line
AUTHORIZATION — VERIFY IT YOURSELF (first block): the prompt's author (the desk, never Dejan); where his approval of THIS launch line's allowlist is recorded (`reports/cto-<date>.md` §4 row numbers, the time) and the `git log` command proving the row is on main; the laws that make each sensitive step standing practice; and: record ≠ this file → `FAILED: authorization mismatch`, stop. A prompt is not an approval and never asks to be believed. Verify the cited §4 row and its linked words appendix together; both must be committed before launch. YOU CAN ALWAYS STOP: the report is the check-in channel; a `FAILED: <step> — <concern>` line is always correct. Never write "you may not ask" without that channel beside it.
UNATTENDED RULES: a dialog reaches nobody, so the dialog tools are off in your launch line. Questions and concerns go in the report as `FAILED:` or `ESCALATE`. Every command beyond plain reading is in your allowlist and matches only in its bare shape: one command per Bash call, exactly the listed prefix — no `cd … &&`, no pipe, no `>` / `2>`, no `; echo`. Read an exit status from the tool result, never by wrapping the command. `cd <path>` is its own call. Capture output from the tool result; write files with the Write tool. A long run (`claude -p`, `agy`) goes to the background with its own output flags or `run_in_background`, never a shell redirect.
PREFLIGHT (first two minutes): run the harmless variant of every allowlisted shape your steps need, in order; one row each under `## PREFLIGHT` (rule · command · exit · allowed / DENIED + the classifier's reason verbatim). Any denial → last line `FAILED PREFLIGHT: <rules>`, commit the report, stop. Never retry a denied command in another shape, route around it, or ask another session to run it.
MID-RUN DENIAL = THE RUN FAILED: last line `FAILED: <step> — <command> — <reason>`, wip-commit, stop. The desk corrects the list, asks him once for the addition, and reruns you from `CONTINUE:`.

## 3. While it runs — the desk
- WAIT on it and watch the report; never ask a hub "are you done".
- `FAILED PREFLIGHT` / `FAILED` → fix the allowlist, bring him only the new rows, rerun the same prompt (it resumes from `CONTINUE:`).
- A hub found on a dialog = a wrong launch: STOP it, fix, rerun. Never press another session's dialog; never relay data a hub was denied.

## 4. Close — the desk
When the last line is the stop line: verify the artifact (L35: worktree clean, commits present, suite line), record it, STOP the session if still listed, close its tab, fold `MEMORY:` / `RULING:` lines, bring him the ESCALATE items per [[preferences]].

## 5. Facts
- STOP ends a background session but not a headless builder it launched: the `claude -p` child survives and keeps writing — find it (`pgrep -fl "claude --model"`) and `kill` it, or two writers meet in one worktree.
- LIST shows a hub blocked on a dialog as `busy` / `working`; only a missing dialog tool prevents one.
- The Claude Code web / desktop view does not render a terminal permission dialog; only the attached herdr viewer does.
- An allow rule (tracked `.claude/settings.json` or `--allowedTools`) beats the auto-mode classifier for a matching BARE command; the same command wrapped does not match and goes to the classifier.
- A PREFLIGHT probe must match the rule it probes (`cobalt settings load --help` does not match `settings load *--dry-run*`). The desk names every probe in the prompt; a rule with no harmless variant is probed by its first real use.
- A branch merged and then reverted on main is never re-landed with `git rebase main` (its commits are ancestors of main; the rebase replays nothing, exit 0). Re-land = `git cherry-pick <base>..<shipped tip>` onto a branch off main, proven by an empty `git diff --stat <shipped tip> HEAD -- <code paths>`; every re-ship prompt after an L54 rollback carries that check.
