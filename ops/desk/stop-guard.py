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
# when it waits on Dejan and its <what> holds `R<digits>` (else `start it: ask him: <what>`), or
# its live: is proven by one of two read commands, each run at most once per stop:
# `sh desk-list.sh` (beside this file; a row whose id is <id> or starts with it, <id> 8+ chars
# of [0-9a-f-], not named cto-desk; a row named brain settles only a <what> containing brain)
# and PGREP below (a line containing <path>). Every item settled, the first line under
# `## §5 CURRENT` before the next `## ` line that starts with `|` and whose first cell starts
# with QUEUE is unsettled: `start it: <its third cell>` (card 164 G7; his 2026-10-09 R724).
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
# THE DESK'S SIZE AND STATE EVERY TURN (card 2026-10-13 458; his 2026-10-13 R1323), only when
# desk-context.sh stands beside this file and stop_hook_active is false: it runs
# `sh desk-context.sh <session_id> 300000` (20 s) and puts, before the OWED line, `UPDATE §5
# CURRENT NOW` when `## §5 CURRENT` holds no `STATE AT <hh:mm>` line of the ET hour now, then
# `DESK SIZE <n> / 300,000` (or `DESK SIZE UNREAD — <first output line or the exit>`). At
# 300,000 or more the size line is REFRESH_NOW below; the first such stop writes
# `<transcript_path>.desk-refresh` (the order time) and starts `python3 <this file> --forced
# <session_id> <transcript_path>` detached; a later stop with a one-line order file sends
# WRITE_HANDOVER once (a second line). Per-turn lines alone: exit 2, count file 0. A report
# whose last line is `HANDOVER: predecessor <this session> ` prints no per-turn line.
# THE FORCED REFRESH (`--forced`, no stdin): waits DESK_REFRESH_TURN_WAIT (600) s from the order
# for its second line, then DESK_REFRESH_LINE_WAIT (300) s for a new `HANDOVER:` line; a line
# naming this session as predecessor ends it. Then: another live cto-desk -> nothing; else the
# FORCED line (no new line came) committed by desk-commit.sh, `sh desk-launch.sh desk`, `claude
# stop <id>`, `claude rm <id>`, each logged to /Users/cobalt/cobalt-wt/.job-state/DESK-REFRESH.
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
import time
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
    # SHADOW-HUB.md's two stop lines (card 2026-10-11 324 S4)
    "SHADOW BUILT ·",
    "SHADOW ROLE ·",
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
QUEUE = "QUEUE"
# a table cell boundary: a pipe not escaped as `\|`
CELL = re.compile(r"(?<!\\)\|")
WAITING = "waiting on Dejan"
# a waiting item settles only with the row it was asked in (card 164 G7 (b))
ASKED = re.compile(r"\bR\d+\b")
# the brain seat's session name (prompts/BRAIN-HUB.md `--name brain`; card 164 G7 (c))
BRAIN = "brain"
LIVE = "live: "
WATCH = "watch "
SESSION_ID = re.compile(r"[0-9a-f-]{8,}")
PGREP = ["pgrep", "-l", "-f", "wait-stop-line.sh|desk-watch.sh"]
BLOCKS = 3
UNREADABLE = "session list unreadable — fix it"
# the per-turn size and state, the order at 300k and the forced refresh (card 458; his 10-13 R1323)
ET = ZoneInfo("America/New_York")
CONTEXT = "desk-context.sh"
SIZE_AT = 300000
MEASURED = re.compile(r"context (\d+) of %d — (ok|REFRESH)" % SIZE_AT)
STAMP = re.compile(r"^STATE AT (\d\d):(\d\d)$")
UPDATE = "UPDATE §5 CURRENT NOW"
REFRESH_NOW = (
    "REFRESH NOW: (1) write the HANDOVER line and §5 CURRENT, "
    "(2) run sh /Users/cobalt/.claude/ops/desk-launch.sh desk, (3) stop."
)
WRITE_HANDOVER = "WRITE HANDOVER NOW"
HANDOVER = "HANDOVER:"
PREDECESSOR = re.compile(r"HANDOVER: predecessor ([0-9a-f-]{8,}) ")
DESK_REFRESH = WT_ROOT + "/.job-state/DESK-REFRESH"
TURN_WAIT = ("DESK_REFRESH_TURN_WAIT", 600)
LINE_WAIT = ("DESK_REFRESH_LINE_WAIT", 300)
POLL = 5


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


def report_lines(report):
    """The report's lines, rstripped, or None when the file is missing: the one read of the
    report (card 164 G7 (a)). Raises Unguarded when it cannot be read."""
    try:
        text = report.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except (OSError, UnicodeDecodeError) as e:
        raise Unguarded("the report cannot be read: %s" % e)
    return [x.rstrip() for x in text.splitlines()]


def owed_block(lines):
    """The OWED block's items as (what, marker) pairs, [] for `owed: none`, or None when the file,
    the `## §5 CURRENT` line or the block is missing (G2). Raises Unguarded when unparseable."""
    if lines is None or CURRENT not in lines:
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


def queued(lines):
    """The first `## §5 CURRENT` table row whose first cell starts with QUEUE, as its third cell
    (`prompt · tab`), or the whole row when it has fewer than three cells; None when there is
    none (card 164 G7 (a))."""
    for line in lines[lines.index(CURRENT) + 1 :]:
        if line.startswith("## "):
            break
        if not line.startswith("|"):
            continue
        # the cells between the edge pipes; an escaped `\|` stays inside its cell (check A1, A3, B2)
        cells = CELL.split(line.strip())[1:]
        if cells and not cells[-1]:
            cells = cells[:-1]
        if cells and cells[0].strip().startswith(QUEUE):
            return cells[2].strip() if len(cells) >= 3 else line.strip()
    return None


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
    """The line's text after `start it: ` for the first item that is neither waiting on Dejan with
    an `R<n>` in its <what> nor live, or None (G2, G3; card 164 G7 (b), (c)). desk-list.sh and
    pgrep each run at most once, only when an item needs them."""
    seen = {}
    for what, marker in items:
        if marker == WAITING:
            if ASKED.search(what):
                continue
            return "ask him: %s" % what
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
                # the desk cannot name itself; the brain's id settles only a brain item (G7 (c))
                if any(
                    i.startswith(sid)
                    and (name not in ("cto-desk", BRAIN) or (name == BRAIN and BRAIN in what))
                    for i, name in seen["list"]
                ):
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
    lines = report_lines(report)
    items = owed_block(lines)
    if items is None:
        line = "start it: the OWED block under %s of %s" % (CURRENT, report)
    else:
        try:
            what = unsettled(items)
        except ListUnreadable:
            line = UNREADABLE
        else:
            if what is None:
                what = queued(lines)
            line = None if what is None else "start it: %s" % what
    # after the OWED read: an unguarded stop never writes an order it does not show (check O1)
    turn = [] if event.get("stop_hook_active") else per_turn(event, lines)
    if line is None and turn:
        # the per-turn lines alone: the continuation's stop reads a count (card 458 S1)
        count_file.write_text("0\n", encoding="utf-8")
        sys.stderr.write("".join("%s\n" % x for x in turn))
        return 2
    if line is None:
        count_file.unlink(missing_ok=True)
        return 0
    if count < BLOCKS:
        count_file.write_text("%d\n" % (count + 1), encoding="utf-8")
        sys.stderr.write("".join("%s\n" % x for x in turn + [line]))
        return 2
    when = datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds")
    os.makedirs(os.path.dirname(DESK_STOP), exist_ok=True)
    with open(DESK_STOP, "a", encoding="utf-8") as f:
        f.write("%s %s GAVE UP after %d blocks — %s\n" % (when, event.get("session_id") or "?", BLOCKS, line))
    count_file.unlink(missing_ok=True)
    return 0


def here(name):
    """The path of `name` beside this file."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), name)


def now_iso():
    return datetime.now(ET).isoformat(timespec="seconds")


def handed_over(line, sid):
    """`HANDOVER: predecessor <p> …` with the session id starting <p> (8+ chars): the desk refreshed."""
    m = PREDECESSOR.match(line)
    return bool(m) and bool(sid) and sid.startswith(m.group(1))


def stamped(lines):
    """`## §5 CURRENT` holds, before the next `## `, a STATE AT line of the ET hour now (card 458 R2)."""
    if lines is None or CURRENT not in lines:
        return False
    hour = datetime.now(ET).hour
    for line in lines[lines.index(CURRENT) + 1 :]:
        if line.startswith("## "):
            break
        m = STAMP.match(line)
        if m and int(m.group(1)) == hour:
            return True
    return False


def measure(script, sid):
    """(<n>, None) from desk-context.sh's plain mode, or (None, <first output line or the exit>)."""
    try:
        out = subprocess.run(
            ["sh", script, sid, str(SIZE_AT)], capture_output=True, encoding="utf-8", timeout=20
        )
    except subprocess.TimeoutExpired as e:
        # its first output line before the timeout, when it printed one (check G2)
        raw = e.stdout or ""
        raw = raw.decode("utf-8", "replace") if isinstance(raw, bytes) else raw
        first = (raw.strip().splitlines() or [""])[0].strip()
        return None, first or "timed out after 20 s"
    first = (out.stdout.strip().splitlines() or [""])[0].strip()
    m = MEASURED.fullmatch(first)
    if out.returncode == 0 and m:
        return int(m.group(1)), None
    return None, first or "exit %d" % out.returncode


def per_turn(event, lines):
    """The desk's per-turn lines (card 458 S1-S3), [] when desk-context.sh is not beside this file
    or the desk has refreshed (the report's last line names it predecessor)."""
    script = here(CONTEXT)
    if not os.path.exists(script):
        return []
    sid = str(event.get("session_id") or "")
    body = [x for x in lines or [] if x.strip()]
    if body and handed_over(body[-1], sid):
        return []
    out = [] if stamped(lines) else [UPDATE]
    n, unread = measure(script, sid)
    if n is None:
        out.append("DESK SIZE UNREAD — %s" % unread)
    elif n < SIZE_AT:
        out.append("DESK SIZE %s / 300,000" % f"{n:,}")
    else:
        out.append(order(event, sid))
    return out


def order(event, sid):
    """At 300k: the first order starts the forced refresh once; a one-line order file gets the
    final message once (card 458 S2, S3 (a))."""
    transcript = str(event.get("transcript_path"))
    order_file = Path(transcript + ".desk-refresh")
    try:
        held = order_file.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        order_file.write_text(now_iso() + "\n", encoding="utf-8")
        try:
            subprocess.Popen(
                [sys.executable, os.path.abspath(__file__), "--forced", sid, transcript],
                stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                start_new_session=True,
            )
        except OSError as e:
            refresh_log(sid, "start --forced", "-", str(e))
        return REFRESH_NOW
    if len(held) == 1:
        with open(order_file, "a", encoding="utf-8") as f:
            f.write(now_iso() + "\n")
        return WRITE_HANDOVER
    return REFRESH_NOW


def refresh_log(sid, step, code, first):
    """One line of the forced refresh's record (card 458 S3; the DESK-STOP precedent)."""
    os.makedirs(os.path.dirname(DESK_REFRESH), exist_ok=True)
    with open(DESK_REFRESH, "a", encoding="utf-8") as f:
        f.write("%s %s %s — %s — %s\n" % (now_iso(), sid[:8], step, code, " ".join(first.split())))


def seconds(pair):
    """DESK_REFRESH_* as desk-handover.sh reads DESK_HANDOVER_WAIT: a whole number of seconds."""
    name, default = pair
    raw = os.environ.get(name, str(default))
    if not raw.isdigit():
        raise Unguarded("%s '%s' is not a number of seconds" % (name, raw))
    return int(raw)


def when(text):
    """The epoch time of an ET ISO line, or None."""
    try:
        return datetime.fromisoformat(text.strip()).timestamp()
    except ValueError:
        return None


def forced(sid, transcript):
    """The forced refresh (card 458 S3 (b)): never waits for Dejan; a failed step is logged and
    the next one still runs."""
    report = desk_report()
    order_file = Path(transcript + ".desk-refresh")
    try:
        turn_wait, line_wait = seconds(TURN_WAIT), seconds(LINE_WAIT)
    except Unguarded as e:
        refresh_log(sid, "refused", "-", str(e))
        return 1

    def held():
        try:
            return order_file.read_text(encoding="utf-8").splitlines()
        except OSError:
            return []

    def handovers():
        try:
            lines = report_lines(report) or []
        except Unguarded:
            lines = []
        return [x for x in lines if x.startswith(HANDOVER)]

    def refreshed():
        return any(handed_over(x, sid) for x in handovers())

    h0 = len(handovers())
    first = held()
    deadline = (when(first[0]) if first else None) or time.time()
    deadline += turn_wait
    while True:
        if refreshed():
            refresh_log(sid, "refreshed itself", 0, "")
            return 0
        lines = held()
        if len(lines) >= 2:
            start = when(lines[1]) or time.time()
            break
        if time.time() >= deadline:
            start = time.time()
            break
        time.sleep(min(POLL, max(0, deadline - time.time())))
    deadline = start + line_wait
    while True:
        if refreshed():
            refresh_log(sid, "refreshed itself", 0, "")
            return 0
        if len(handovers()) > h0:
            new = True
            break
        if time.time() >= deadline:
            new = False
            break
        time.sleep(min(POLL, max(0, deadline - time.time())))

    try:
        rows = listed()
    except ListUnreadable as e:
        refresh_log(sid, "desk-list.sh", "-", str(e))
        rows = []

    def own(i):
        return SESSION_ID.fullmatch(i) is not None and (sid.startswith(i) or i.startswith(sid))

    others = [i for i, name in rows if name == "cto-desk" and not own(i)]
    if others:
        refresh_log(sid, "live cto-desk %s" % others[0], "-", "launch nothing")
        return 0

    def step(name, argv):
        try:
            out = subprocess.run(argv, capture_output=True, encoding="utf-8", timeout=600)
        except (OSError, subprocess.TimeoutExpired) as e:
            refresh_log(sid, name, "-", "%s: %s" % (type(e).__name__, e))
            return
        text = (out.stdout.strip() or out.stderr.strip()).splitlines()
        refresh_log(sid, name, out.returncode, text[0] if text else "")

    if not new:
        line ="HANDOVER: FORCED — no line from %s; successor reconciles" % sid[:8]
        try:
            text = report.read_text(encoding="utf-8")
            with open(report, "a", encoding="utf-8") as f:
                f.write(("" if not text or text.endswith("\n") else "\n") + line + "\n")
            refresh_log(sid, line, 0, "")
        except OSError as e:
            refresh_log(sid, line, "-", str(e))
        step("desk-commit.sh", ["sh", here("desk-commit.sh"), "docs(desk): HANDOVER FORCED %s" % sid[:8], str(report)])
    step("desk-launch.sh desk", ["sh", here("desk-launch.sh"), "desk"])
    # the old desk's own cto-desk row first, then any other prefix row (check G1)
    ids = [i for i, name in rows if own(i) and name == "cto-desk"] + [
        i for i, name in rows if own(i) and name != "cto-desk"
    ]
    if ids:
        step("claude stop %s" % ids[0], ["claude", "stop", ids[0]])
        step("claude rm %s" % ids[0], ["claude", "rm", ids[0]])
    return 0


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--forced":
        try:
            return forced(sys.argv[2], sys.argv[3])
        except Exception as e:
            refresh_log(sys.argv[2], "error", "-", "%s: %s" % (type(e).__name__, e))
            return 1
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
