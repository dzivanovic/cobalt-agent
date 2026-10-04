#!/usr/bin/env python3
# idle-wake.py — a Claude Code Notification hook (card prompts/2026-10-03/09-worker-watch-card.md
# N1; his 2026-10-03 R24). Reads the hook's JSON on stdin. It acts only on the idle kind
# (`notification_type` "idle_prompt": the session has waited for input 60 s or more; his install
# also sets the entry's matcher to "idle_prompt") from a cwd under /Users/cobalt/cobalt-wt/<worktree>.
# Then it appends ONE line to /Users/cobalt/cobalt-wt/.job-state/WAKE (the folder made when
# absent): `<ISO time, ET, with its offset> <worktree> IDLE <the report's last non-blank line,
# or "no report">`. The report is found as stop-guard.py finds it (report_last_line, beside this
# file). The desk's watch (desk-watch.sh, wait-stop-line.sh) and the runner read the file.
# Exit 0 always: it never blocks, and an error inside it writes nothing. Runs no subprocess.
import importlib.util
import json
import os
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

WT_ROOT = "/Users/cobalt/cobalt-wt"
WAKE = WT_ROOT + "/.job-state/WAKE"


def stop_guard():
    """stop-guard.py beside this file, loaded as a module (no bytecode written)."""
    sys.dont_write_bytecode = True
    here = os.path.dirname(os.path.abspath(__file__))
    spec = importlib.util.spec_from_file_location("stop_guard", os.path.join(here, "stop-guard.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    try:
        event = json.loads(sys.stdin.read())
        if not isinstance(event, dict) or event.get("notification_type") != "idle_prompt":
            return 0
        guard = stop_guard()
        cwd = event.get("cwd")
        name = guard.worktree(cwd)
        if name is None:
            return 0
        last = guard.report_last_line(event.get("transcript_path") or "", cwd)
        when = datetime.now(ZoneInfo("America/New_York")).isoformat(timespec="seconds")
        line = "%s %s IDLE %s\n" % (when, name, "no report" if last is None else last)
        os.makedirs(os.path.dirname(WAKE), exist_ok=True)
        with open(WAKE, "a", encoding="utf-8") as f:
            f.write(line)
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
