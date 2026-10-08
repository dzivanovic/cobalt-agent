#!/usr/bin/env python3
# stop-guard.py — a Claude Code Stop hook (card prompts/2026-10-03/09-worker-watch-card.md S1;
# his 2026-10-03 R24; the desk seat: card prompts/2026-10-06/66-desk-stop-guard-card.md, his
# 2026-10-06 R590). Reads the hook's JSON on stdin (`cwd`, `transcript_path`, `stop_hook_active`,
# `session_id`). Unreadable hook JSON -> exit 0.
# THE WORKER: a cwd under /Users/cobalt/cobalt-wt/<worktree>. stop_hook_active true -> exit 0
# (the turn ends; the worker path never loops). It finds the report through the card: the
# transcript's first user message (not isMeta) is the hub's launch message and names
# `CARD: '<card>'`; the report is that card's `CHECK REPORT:` when the message names
# CHECK-HUB.md, else its `REPORT:`. A first message that names no `CARD:` is a `prompt` seat ->
# exit 0 (S2). When the report's last non-blank line begins with a stop shape (STOP below) ->
# exit 0. Otherwise — prose, no first message, no report value, no report file — exit 2 with ONE
# stderr sentence (SENTENCE below). The worker path writes nothing. idle-wake.py (beside this
# file) reads the report with report_last_line().
# THE DESK: a cwd that is /Users/cobalt/cobalt or under it whose first user message's first
# `Read '<path>'` has the basename CTO-DESK-WAKEUP.md (bare-guard.py's desk rule), in a
# background session: that message's entry carries `"sessionKind": "bg"` (card 2026-10-08 106
# G1; a missing key or any other value is not the desk). Any other cwd or seat (the brain, a
# deploy, the close, a prompt seat, a foreground session that read the wake-up) -> exit 0.
# It reads the OWED block: the first non-blank lines under `## §5 CURRENT` of /Users/cobalt/cobalt/docs/40 - DevDocs/reports/
# cto-<ET date at the stop>.md — `owed: none`, or one line per item `OWED: <what> | live: <id>`,
# `OWED: <what> | live: watch <path>` or `OWED: <what> | waiting on Dejan`. An item is settled
# when it waits on Dejan or its live: is proven by one of two read commands, each run at most
# once per stop: `sh desk-list.sh` (beside this file; a row whose id is <id> or starts with it,
# <id> 8+ chars of [0-9a-f-], not named cto-desk) and PGREP below (a line containing <path>).
# Settled -> exit 0. Not settled (or no report, no section, no block) -> stderr ONE line
# `start it: <what>`, exit 2. THE DESK PATH WRITES: the count of blocks in a row in
# `<transcript_path>.desk-stop` (reset by a new message, removed when settled); at 3 blocks the
# next stop appends `<ISO time ET> <session_id> GAVE UP after 3 blocks — start it: <what>` to
# /Users/cobalt/cobalt-wt/.job-state/DESK-STOP, removes the count and exits 0. An unreadable
# session list (desk-list.sh missing, a non-zero exit or a timeout; card 2026-10-08 106 G2) is
# an unsettled item: stderr `session list unreadable — fix it`, exit 2, the same count and
# give-up (`… GAVE UP after 3 blocks — session list unreadable — fix it`). Any other error on
# the desk path (an unparseable block, an unreadable report or count, a failing pgrep) ->
# exit 0 with ONE stderr line `stop-guard: desk not guarded — <reason>`.
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
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

WT_ROOT = "/Users/cobalt/cobalt-wt"
REPO = "/Users/cobalt/cobalt"
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
# the desk seat (card prompts/2026-10-06/66-desk-stop-guard-card.md; his 2026-10-06 R590)
READ = re.compile(r"Read '([^']+)'")
DESK_HUB = "CTO-DESK-WAKEUP.md"
# the desk is a background session (card prompts/2026-10-08/106-desk-ops-fixes-card.md G1)
KIND = "sessionKind"
BACKGROUND = "bg"
DESK_STOP = WT_ROOT + "/.job-state/DESK-STOP"
CURRENT = "## §5 CURRENT"
ITEM = "OWED: "
NONE = "owed: none"
WAITING = "waiting on Dejan"
LIVE = "live: "
WATCH = "watch "
SESSION_ID = re.compile(r"[0-9a-f-]{8,}")
PGREP = ["pgrep", "-l", "-f", "wait-stop-line.sh|desk-watch.sh"]
BLOCKS = 3
UNREADABLE = "session list unreadable — fix it"


def worktree(cwd):
    """The worktree name when cwd is /Users/cobalt/cobalt-wt/<name>[/...], else None."""
    if not isinstance(cwd, str) or not cwd.startswith(WT_ROOT + "/"):
        return None
    name = cwd[len(WT_ROOT) + 1 :].split("/", 1)[0]
    return name or None


def first_user_entry(transcript_path):
    """The transcript's first user entry that is not isMeta, or None."""
    with open(transcript_path, encoding="utf-8") as f:
        for raw in f:
            try:
                entry = json.loads(raw)
            except ValueError:
                continue
            if entry.get("type") != "user" or entry.get("isMeta"):
                continue
            return entry
    return None


def first_user_text(transcript_path):
    """The text of the transcript's first user message that is not isMeta, or None."""
    entry = first_user_entry(transcript_path)
    if entry is None:
        return None
    content = entry.get("message", {}).get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return " ".join(
            c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text"
        )
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


class Unguarded(Exception):
    """The desk path cannot decide: the stop is let through with one stderr line (G5)."""


class ListUnreadable(Exception):
    """desk-list.sh failed or timed out: an unsettled item, never a pass (card 106 G2)."""


def is_desk(event):
    """cwd is the repo or under it, the first user entry carries `"sessionKind": "bg"` (card 106
    G1) and its message reads CTO-DESK-WAKEUP.md (G1)."""
    cwd = event.get("cwd")
    if not isinstance(cwd, str) or not (cwd == REPO or cwd.startswith(REPO + "/")):
        return False
    transcript = event.get("transcript_path")
    if not isinstance(transcript, str) or not transcript:
        return False
    try:
        entry = first_user_entry(transcript)
        if entry is None or entry.get(KIND) != BACKGROUND:
            return False
        text = first_user_text(transcript)
    except Exception:
        return False
    m = READ.search(text or "")
    return bool(m) and os.path.basename(m.group(1)) == DESK_HUB


def desk_report():
    """Today's desk report, by the ET date at the stop (G2)."""
    day = datetime.now(ZoneInfo("America/New_York")).date()
    return Path(REPO + "/docs/40 - DevDocs/reports/cto-%s.md" % day)


def owed_block(report):
    """The OWED block's items as (what, marker) pairs, [] for `owed: none`, or None when the file,
    the `## §5 CURRENT` line or the block is missing (G2). Raises Unguarded when unparseable."""
    try:
        text = report.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except (OSError, UnicodeDecodeError) as e:
        raise Unguarded("the report cannot be read: %s" % e)
    lines = [x.rstrip() for x in text.splitlines()]
    if CURRENT not in lines:
        return None
    rest = lines[lines.index(CURRENT) + 1 :]
    while rest and not rest[0]:
        rest = rest[1:]

    def item(line):
        # a bare `OWED: ` is rstripped to `OWED:`: an item with an empty <what> (check O1, A3)
        return line.startswith(ITEM) or line == ITEM.rstrip()

    if not rest or not (rest[0] == NONE or item(rest[0])):
        return None
    block = rest[:1]
    for line in rest[1:]:
        if not item(line):
            break
        block.append(line)
    if block[0] == NONE:
        if len(block) > 1:
            raise Unguarded("`owed: none` beside an OWED: line")
        return []
    items = []
    for line in block:
        parts = line[len(ITEM) :].split(" | ")
        if len(parts) > 2:
            raise Unguarded("more than one ' | ' in: %s" % line)
        what = parts[0].strip()
        if not what:
            raise Unguarded("an empty item in: %s" % line)
        marker = parts[1] if len(parts) == 2 else None
        if marker is not None and marker.strip() == "live:":
            raise Unguarded("an empty live: value in: %s" % line)
        items.append((what, marker))
    return items


def listed():
    """The (id, name) of every row desk-list.sh beside this file prints (G3). A non-zero exit (a
    missing desk-list.sh included) or a timeout raises ListUnreadable (card 106 G2)."""
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)), "desk-list.sh")
    try:
        out = subprocess.run(["sh", script], capture_output=True, encoding="utf-8", timeout=20)
    except subprocess.TimeoutExpired:
        raise ListUnreadable("desk-list.sh timed out")
    if out.returncode != 0:
        raise ListUnreadable("desk-list.sh exit %d" % out.returncode)
    rows = [row.split(" · ") for row in out.stdout.splitlines()]
    return [(f[0], f[1]) for f in rows if len(f) > 1]


def watched():
    """The command lines of the running watches (G3)."""
    try:
        out = subprocess.run(PGREP, capture_output=True, encoding="utf-8", timeout=10)
    except subprocess.TimeoutExpired:
        raise Unguarded("pgrep timed out")
    if out.returncode > 1:
        raise Unguarded("pgrep exit %d" % out.returncode)
    return out.stdout.splitlines() if out.returncode == 0 else []


def unsettled(items):
    """The first item that is neither waiting on Dejan nor live, or None (G2, G3). desk-list.sh
    and pgrep each run at most once, only when an item needs them."""
    seen = {}
    for what, marker in items:
        if marker == WAITING:
            continue
        if marker is not None and marker.startswith(LIVE + WATCH):
            path = marker[len(LIVE + WATCH) :]
            if "watch" not in seen:
                seen["watch"] = watched()
            # G2: `live: watch <absolute path>`; a relative path is none of the forms (check A2)
            if path.startswith("/") and any(path in line for line in seen["watch"]):
                continue
        elif marker is not None and marker.startswith(LIVE):
            sid = marker[len(LIVE) :]
            if SESSION_ID.fullmatch(sid):
                if "list" not in seen:
                    seen["list"] = listed()
                # the desk cannot name itself
                if any(i.startswith(sid) and name != "cto-desk" for i, name in seen["list"]):
                    continue
        return what
    return None


def desk(event):
    """The desk's stop (G2-G4): 0 settled or given up, 2 blocked. Raises on anything it cannot read."""
    count_file = Path(str(event.get("transcript_path")) + ".desk-stop")
    count = 0
    if event.get("stop_hook_active"):
        try:
            raw = count_file.read_text(encoding="utf-8").strip()
        except FileNotFoundError:
            raise Unguarded("stop_hook_active with no count file")
        if raw not in ("0", "1", "2", "3"):
            raise Unguarded("the count file holds %r" % raw)
        count = int(raw)
    report = desk_report()
    items = owed_block(report)
    if items is None:
        line = "start it: the OWED block under %s of %s" % (CURRENT, report)
    else:
        try:
            what = unsettled(items)
        except ListUnreadable:
            line = UNREADABLE
        else:
            line = None if what is None else "start it: %s" % what
    if line is None:
        count_file.unlink(missing_ok=True)
        return 0
    if count < BLOCKS:
        count_file.write_text("%d\n" % (count + 1), encoding="utf-8")
        sys.stderr.write("%s\n" % line)
        return 2
    when = datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds")
    os.makedirs(os.path.dirname(DESK_STOP), exist_ok=True)
    with open(DESK_STOP, "a", encoding="utf-8") as f:
        f.write("%s %s GAVE UP after %d blocks — %s\n" % (when, event.get("session_id") or "?", BLOCKS, line))
    count_file.unlink(missing_ok=True)
    return 0


def main():
    try:
        event = json.loads(sys.stdin.read())
        if not isinstance(event, dict):
            return 0
    except ValueError:
        return 0
    cwd = event.get("cwd")
    if worktree(cwd) is not None:
        return worker(event, cwd)
    if is_desk(event):
        try:
            return desk(event)
        except Exception as e:  # G5: fail open, never a loop
            reason = str(e) if isinstance(e, Unguarded) else "%s: %s" % (type(e).__name__, e)
            sys.stderr.write("stop-guard: desk not guarded — %s\n" % " ".join(reason.split()))
            return 0
    return 0


def worker(event, cwd):
    """The worker's stop, as before the desk seat (S1, S2)."""
    if event.get("stop_hook_active"):
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
