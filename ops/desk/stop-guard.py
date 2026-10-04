#!/usr/bin/env python3
# stop-guard.py — a Claude Code Stop hook (card prompts/2026-10-03/09-worker-watch-card.md S1;
# his 2026-10-03 R24). Reads the hook's JSON on stdin (`cwd`, `transcript_path`,
# `stop_hook_active`). stop_hook_active true -> exit 0 (the turn ends; the hook never loops).
# A cwd not under /Users/cobalt/cobalt-wt/<worktree> -> exit 0 without reading anything (the
# desk, the brain, a deploy and the close run in /Users/cobalt/cobalt). For a worker it finds
# the report through the card: the transcript's first user message (not isMeta) is the hub's
# launch message and names `CARD: '<card>'`; the report is that card's `CHECK REPORT:` when the
# message names CHECK-HUB.md, else its `REPORT:`. A first message that names no `CARD:` is a
# `prompt` seat -> exit 0 (S2). When the report's last non-blank line begins with a stop shape
# (STOP below) -> exit 0. Otherwise — prose, no first message, no report value, no report
# file — exit 2 with ONE stderr sentence (SENTENCE below). Unreadable hook JSON -> exit 0.
# Writes nothing. idle-wake.py (beside this file) reads the report with report_last_line().
#
# HIS INSTALL (card row I1; his 2026-10-03 R77), after set 2 is DEPLOYED: the value of "hooks"
# in user settings ~/.claude/settings.json (not main's tracked .claude/settings.json), pasted
# once. Three entries: bare-guard.py on every Bash call, this file on every Stop, idle-wake.py
# on the idle notification.
# INSTALL BEGIN
# {
#   "PreToolUse": [
#     {"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"}]}
#   ],
#   "Stop": [
#     {"hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py"}]}
#   ],
#   "Notification": [
#     {"matcher": "idle_prompt", "hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py"}]}
#   ]
# }
# INSTALL END
import json
import re
import sys
from pathlib import Path

WT_ROOT = "/Users/cobalt/cobalt-wt"
# the stop shapes of BUILD-HUB `## STOP LINE` and `## UNATTENDED RULES` (b), CHECK-HUB, DEPLOY-HUB
# and DEVFIX-HUB, and the line a worker keeps while it runs (RECOVERY)
STOP = (
    "BUILT ·",
    "CHECK DONE ·",
    "DEPLOYED ",
    "REBUILT ·",
    "FAILED",
    "FAILED PREFLIGHT",
    "ASK DESK:",
    "(run in progress",
)
SENTENCE = (
    "NOT A REFUSAL. Your report's last line is not a stop line. Write the step's stop line, "
    "or FAILED: <step> — <what> — <reason>, or ASK DESK: <one question>, then stop."
)
CARD = re.compile(r"CARD: '([^']+)'")


def worktree(cwd):
    """The worktree name when cwd is /Users/cobalt/cobalt-wt/<name>[/...], else None."""
    if not isinstance(cwd, str) or not cwd.startswith(WT_ROOT + "/"):
        return None
    name = cwd[len(WT_ROOT) + 1 :].split("/", 1)[0]
    return name or None


def first_user_text(transcript_path):
    """The text of the transcript's first user message that is not isMeta, or None."""
    with open(transcript_path, encoding="utf-8") as f:
        for raw in f:
            try:
                entry = json.loads(raw)
            except ValueError:
                continue
            if entry.get("type") != "user" or entry.get("isMeta"):
                continue
            content = entry.get("message", {}).get("content")
            if isinstance(content, str):
                return content
            if isinstance(content, list):
                return " ".join(
                    c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"
                )
            return None
    return None


def report_path(transcript_path, cwd):
    """The report the card of the launch message names, or None."""
    text = first_user_text(transcript_path)
    m = CARD.search(text or "")
    if not m:
        return None
    key = "CHECK REPORT: " if "CHECK-HUB.md" in text else "REPORT: "
    for line in Path(m.group(1)).read_text(encoding="utf-8").splitlines():
        if line.startswith(key):
            value = line[len(key) :].strip()
            return (Path(cwd) / value) if value else None
    return None


def report_last_line(transcript_path, cwd):
    """The report's last non-blank line ('' for a report with none), or None: no report."""
    try:
        path = report_path(transcript_path, cwd)
        if path is None:
            return None
        lines = [x.rstrip() for x in path.read_text(encoding="utf-8").splitlines() if x.strip()]
    except (OSError, ValueError, AttributeError):
        return None
    return lines[-1] if lines else ""


def main():
    try:
        event = json.loads(sys.stdin.read())
        if not isinstance(event, dict):
            return 0
    except ValueError:
        return 0
    if event.get("stop_hook_active"):
        return 0
    cwd = event.get("cwd")
    if worktree(cwd) is None:
        return 0
    try:
        text = first_user_text(event.get("transcript_path") or "")
    except (OSError, ValueError):
        text = None
    if text is not None and not CARD.search(text):
        return 0
    last = report_last_line(event.get("transcript_path") or "", cwd)
    if last is not None and last.startswith(STOP):
        return 0
    sys.stderr.write(SENTENCE + "\n")
    return 2


if __name__ == "__main__":
    sys.exit(main())
