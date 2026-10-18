#!/bin/sh
# checkin-timer.sh — the check-in ping, started by a timer (his 2026-10-18 R1854 B;
# card 2026-10-18 751 checkin-install). launchd runs it from
# ops/desk/com.cobalt.checkin-timer.plist at 06:00, 12:00, 18:00 and 24:00 ET.
#
# HIS INSTALL — typed once, at the Mac, by him (nothing else installs it):
#   mkdir -p /Users/cobalt/cobalt-wt/.timer-logs
#     (first: launchd's own log paths, StandardOutPath / StandardErrorPath, need the folder
#     before the first fire)
#   cp /Users/cobalt/cobalt/ops/desk/com.cobalt.checkin-timer.plist ~/Library/LaunchAgents/
#   launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.checkin-timer.plist
# The one read that proves it:
#   launchctl print gui/$(id -u)/com.cobalt.checkin-timer
#   → the job is listed, with its calendar triggers (the card expects the next fire time there;
#     this build could not run launchctl to confirm the field).
#
# WHAT ONE FIRE DOES, in order (each line on stdout, which the plist logs):
#   1. desk-launch.sh absent → "REFUSED: no launcher: <path>", one notify, exit 1.
#   2. desk-list.sh missing or unreadable → the desk-missing notify, then "REFUSED: …", exit 1.
#   3. no live row named exactly cto-desk (a row with an id, the field before the first ` · `,
#      whose name field is exactly cto-desk) → "DESK MISSING: no check-in sent", one notify
#      `desk missing — relaunch with desk-launch.sh desk`, no launch, exit 1. A cwd that merely
#      holds the words is not a desk.
#   4. the live rows named exactly checkin-ping, every one, judged by AGE, never by state (R117:
#      an ended --bg row can stay `working`; card 751 F1, brain L79 (a)). The age is the row's
#      `startedAt` in `claude agents --json` (epoch milliseconds), matched by id; no numeric
#      startedAt, or an unreadable listing, is an unknown age and counts as stale. A row older
#      than PING_MAX_AGE_MIN is closed with `desk-done.sh <id> --replaced` before the launch,
#      "CLOSED STALE PING: <its last stdout line>"; a non-zero exit or a last line starting KEPT
#      → "REFUSED: close of stale ping <id> failed — <last line>", one notify, exit 1, no launch.
#      A younger row → "DEFERRED: ping live — <id>", exit 0, no launch, even when a stale row
#      was closed. A check-in that finds a 6-hour-old ping is never deferred.
#   5. otherwise `sh <repo>/ops/desk/desk-launch.sh prompt "<repo>/docs/40 - DevDocs/prompts/CHECKIN-PING.md"`
#      once, its output appended to <wt>/.timer-logs/checkin-<ET date>.log after a
#      "<time> fire: checkin" line; "LAUNCHED: checkin — exit <n> — log <path>". A non-zero exit
#      also notifies "REFUSED: launcher exit <n> — log <path>" and the fire exits with that status.
#      No date arithmetic and no slot: the ping seat reads the clock.
#
# THE NOTIFIES: every REFUSED line, and `desk missing — relaunch with desk-launch.sh desk`, go
# out once each as a Mattermost DM `checkin-timer: <line>` through cobalt.notify.send_dm: a
# subshell sources $HOME/.cobalt_key (the ops/run_backup.sh form; the key is never echoed) and
# runs `uv run --project <repo> python -c …`. A failed send prints `NOTIFY FAILED: exit <n>`;
# the exit code stays the fire's own. A send that returns `sent=False` exits 3 from the sender,
# prints `NOTIFY FAILED: not sent (sent=False)`, and the fire runs on to its own path but exits
# 1 where it would exit 0.
# COBALT_NOTIFY, when set, is run as `$COBALT_NOTIFY "checkin-timer: <line>"` instead (the test's
# stub sender; no key is read).
#
# COBALT_REPO_ROOT, COBALT_WT_ROOT and COBALT_DESK_LIST stand in for the three paths, and
# COBALT_AGENTS_CMD and COBALT_DESK_DONE for the age source and the close, in
# tests/ops/test_checkin_install_1018.py only.
export LC_ALL=C

PING_MAX_AGE_MIN=30

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
DESK_LIST=${COBALT_DESK_LIST:-/Users/cobalt/.claude/ops/desk-list.sh}
AGENTS_CMD=${COBALT_AGENTS_CMD:-claude agents --json}
DESK_DONE=${COBALT_DESK_DONE:-$REPO/ops/desk/desk-done.sh}
LAUNCH="$REPO/ops/desk/desk-launch.sh"
PING="$REPO/docs/40 - DevDocs/prompts/CHECKIN-PING.md"

# notify <line>: one Mattermost DM `checkin-timer: <line>` through cobalt.notify.send_dm. The key
# is sourced in a subshell only, never echoed; a failed send prints one line and changes nothing
# else; a `sent=False` (exit 3) also marks the fire unsent.
unsent=""
notify() {
    if [ -n "${COBALT_NOTIFY:-}" ]; then
        "$COBALT_NOTIFY" "checkin-timer: $1"
    else
        (
            [ -f "$HOME/.cobalt_key" ] || exit 78
            . "$HOME/.cobalt_key"
            uv run --project "$REPO" python -c 'import sys; from cobalt.notify import send_dm; sys.exit(0 if send_dm(sys.argv[1]).sent else 3)' "checkin-timer: $1"
        )
    fi
    sent=$?
    if [ "$sent" -eq 3 ]; then
        printf 'NOTIFY FAILED: not sent (sent=False)\n'
        unsent=1
    elif [ "$sent" -ne 0 ]; then
        printf 'NOTIFY FAILED: exit %s\n' "$sent"
    fi
}

# finish <code>: the fire's exit; an unsent notify turns an exit 0 into 1
finish() {
    [ "$1" -ne 0 ] || [ -z "$unsent" ] || exit 1
    exit "$1"
}

refuse() {
    printf 'REFUSED: %s\n' "$*"
    notify "REFUSED: $*"
    exit 1
}

DESK_MISSING="desk missing — relaunch with desk-launch.sh desk"

# 1. the launcher
[ -f "$LAUNCH" ] || refuse "no launcher: $LAUNCH"

# 2. the session list (rows "id · name · cwd · status · state")
[ -f "$DESK_LIST" ] || { notify "$DESK_MISSING"; refuse "no session list: $DESK_LIST"; }
rows=$(sh "$DESK_LIST" 2>/dev/null) || { notify "$DESK_MISSING"; refuse "the session list is unreadable: $DESK_LIST"; }

# 3. a live desk: a row with an id (the field before the first ` · `) named exactly cto-desk
desk=""
while IFS= read -r row; do
    rest=${row#* · }
    [ "$rest" != "$row" ] || continue
    [ -n "${row%% · *}" ] || continue
    [ "${rest%% · *}" != "cto-desk" ] || desk=1
done <<ROWS
$rows
ROWS
if [ -z "$desk" ]; then
    printf 'DESK MISSING: no check-in sent\n'
    notify "$DESK_MISSING"
    exit 1
fi

# 4. every live check-in ping (the name field exactly checkin-ping; the id is the field before
# ` · `), judged by age: older than PING_MAX_AGE_MIN, or of unknown age, is closed; younger defers
ping_ids=""
while IFS= read -r row; do
    rest=${row#* · }
    [ "$rest" != "$row" ] || continue
    id=${row%% · *}
    [ -n "$id" ] || continue
    [ "${rest%% · *}" = "checkin-ping" ] || continue
    ping_ids="$ping_ids $id"
done <<ROWS
$rows
ROWS
young=""
if [ -n "$ping_ids" ]; then
    # one read of the listing; "<id> young" for each ping id whose numeric startedAt is in the limit
    agents=$($AGENTS_CMD 2>/dev/null) || agents=""
    ages=$(printf '%s\n' "$agents" | python3 -c '
import json, sys, time
limit = int(sys.argv[1]) * 60 * 1000
now = time.time() * 1000
try:
    rows = json.load(sys.stdin)
except Exception:
    rows = []
started = {}
for a in rows if isinstance(rows, list) else []:
    if isinstance(a, dict) and a.get("id"):
        started[str(a["id"])] = a.get("startedAt")
for pid in sys.argv[2:]:
    s = started.get(pid)
    if isinstance(s, str) and s.isdigit():
        s = int(s)
    if isinstance(s, (int, float)) and not isinstance(s, bool) and now - s <= limit:
        print(pid, "young")
' "$PING_MAX_AGE_MIN" $ping_ids 2>/dev/null)
    for id in $ping_ids; do
        case "
$ages
" in
            *"
$id young
"*)
                [ -n "$young" ] || young=$id
                continue ;;
        esac
        closed=$(sh "$DESK_DONE" "$id" --replaced)
        rc=$?
        closed=$(printf '%s\n' "$closed" | grep -v '^[[:space:]]*$' | tail -n 1)
        case "$closed" in
            KEPT*) rc=1 ;;
        esac
        [ "$rc" -eq 0 ] || refuse "close of stale ping $id failed — $closed"
        printf 'CLOSED STALE PING: %s\n' "$closed"
    done
fi
if [ -n "$young" ]; then
    printf 'DEFERRED: ping live — %s\n' "$young"
    finish 0
fi

# 5. the launch, once; the log name is today's ET date, with no slot arithmetic
logs="$WT/.timer-logs"
mkdir -p "$logs" || refuse "cannot make $logs"
et=$(TZ=America/New_York date '+%Y-%m-%d')
log="$logs/checkin-$et.log"
printf '%s fire: checkin\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" >> "$log"
sh "$LAUNCH" prompt "$PING" >> "$log" 2>&1
status=$?
printf 'LAUNCHED: checkin — exit %s — log %s\n' "$status" "$log"
if [ "$status" -ne 0 ]; then
    notify "REFUSED: launcher exit $status — log $log"
fi
finish "$status"
