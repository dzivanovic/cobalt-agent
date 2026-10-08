#!/bin/sh
# close-timer.sh — the nightly close, started by a timer (his ruling cto-2026-10-02 R44,
# direction row 7; card 2026-10-03 05 close-timer). launchd runs it from
# ops/desk/com.cobalt.close-timer.plist at 21:05 ET and hourly 22:05 … 03:05 ET.
#
# HIS INSTALL — typed once, at the Mac, by him (nothing else installs it):
#   mkdir -p /Users/cobalt/cobalt-wt/.timer-logs
#     (first: launchd's own log paths, StandardOutPath / StandardErrorPath, need the folder
#     before the first fire)
#   cp /Users/cobalt/cobalt/ops/desk/com.cobalt.close-timer.plist ~/Library/LaunchAgents/
#   launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.cobalt.close-timer.plist
# The one read that proves it:
#   launchctl print gui/$(id -u)/com.cobalt.close-timer
#   → the job is listed, with its calendar triggers (the card expects the next fire time there;
#     this build could not run launchctl to confirm the field).
#
# WHAT ONE FIRE DOES, in order (each line on stdout, which the plist logs):
#   1. <date> = the EVENING's ET date (TZ=America/New_York): before 04:00 ET (a fire after
#      midnight) it is yesterday's ET date, else today's (card row T1, X2). So the 00:05–03:05
#      fires after a finished close stop at 4. as DONE ALREADY, one line each.
#   2. desk-launch.sh absent → "REFUSED: …", exit 1.
#   3. no live `cto-desk` row in desk-list.sh's rows (a row with an id, the field before the
#      first ` · `, whose name field is exactly cto-desk) → the desk-missing notify below; the
#      fire goes on unchanged. A live `deploy-hub-*` session (the name field) →
#      "DEFERRED: deploy live — <name>", exit 0; launchd fires again on the hour.
#      desk-list.sh missing or unreadable → the desk-missing notify, then "REFUSED: …", exit 1
#      (a close never launches beside a deploy it cannot rule out; desk-launch.sh refuses the
#      same).
#   4. reports/close-<date>.md ends in its stop line (`CLOSE PUSHED …`) → "DONE ALREADY", exit 0.
#   5. otherwise `sh <repo>/ops/desk/desk-launch.sh close <date>` once, its output appended to
#      <wt>/.timer-logs/close-<date>.log; "LAUNCHED: close <date> — exit <n> — log <path>" and
#      the launcher's status. desk-launch.sh keeps every refusal of its own (the hour, a live
#      deploy, a report that already exists, the desk-size guard).
#
# THE TWO NOTIFIES (card 2026-10-08 106 G4; his 10-08 R660, R662): every REFUSED line, and
# `desk missing — relaunch with desk-launch.sh desk`, go out once each as a Mattermost DM
# `close-timer: <line>` through cobalt.notify.send_dm: a subshell sources $HOME/.cobalt_key (the
# ops/run_backup.sh form; the key is never echoed) and runs `uv run --project <repo> python -c …`.
# A failed send prints `NOTIFY FAILED: exit <n>`; the exit code stays the fire's own.
# COBALT_NOTIFY, when set, is run as `$COBALT_NOTIFY "close-timer: <line>"` instead (the test's
# stub sender; no key is read).
#
# COBALT_REPO_ROOT, COBALT_WT_ROOT and COBALT_DESK_LIST stand in for the three paths in
# tests/ops/test_close_timer.py only.
export LC_ALL=C

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
DESK_LIST=${COBALT_DESK_LIST:-/Users/cobalt/.claude/ops/desk-list.sh}
LAUNCH="$REPO/ops/desk/desk-launch.sh"
REPORTS="$REPO/docs/40 - DevDocs/reports"

# notify <line>: one Mattermost DM `close-timer: <line>` through cobalt.notify.send_dm (card
# 2026-10-08 106 G4). The key is sourced in a subshell only, never echoed; a failed send prints
# one line and changes nothing else.
notify() {
    if [ -n "${COBALT_NOTIFY:-}" ]; then
        "$COBALT_NOTIFY" "close-timer: $1"
    else
        (
            [ -f "$HOME/.cobalt_key" ] || exit 78
            . "$HOME/.cobalt_key"
            uv run --project "$REPO" python -c 'import sys; from cobalt.notify import send_dm; send_dm(sys.argv[1])' "close-timer: $1"
        )
    fi
    sent=$?
    [ "$sent" -eq 0 ] || printf 'NOTIFY FAILED: exit %s\n' "$sent"
}

refuse() {
    printf 'REFUSED: %s\n' "$*"
    notify "REFUSED: $*"
    exit 1
}

DESK_MISSING="desk missing — relaunch with desk-launch.sh desk"

# closed <date>: the close report of that date ends in its stop line
closed() {
    f="$REPORTS/close-$1.md"
    [ -f "$f" ] || return 1
    last=$(grep -v '^[[:space:]]*$' "$f" | tail -n 1)
    case "$last" in
        "CLOSE PUSHED "*) return 0 ;;
    esac
    return 1
}

# 1. the date: one read of the ET clock
now=$(TZ=America/New_York date '+%Y-%m-%d %H')
today=${now% *}
hour=${now#* }
case "$today" in
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
    *) refuse "the ET clock read '$now' is not a date" ;;
esac
cday=$today
if [ "$hour" -lt 4 ]; then
    cday=$(date -j -v-1d -f %Y-%m-%d "$today" +%Y-%m-%d) || refuse "the previous date of $today is unreadable"
fi

# 2. the launcher
[ -f "$LAUNCH" ] || refuse "no launcher: $LAUNCH"

# 3. a live deploy hub (rows "id · name · cwd · status · state")
[ -f "$DESK_LIST" ] || { notify "$DESK_MISSING"; refuse "no session list: $DESK_LIST"; }
rows=$(sh "$DESK_LIST" 2>/dev/null) || { notify "$DESK_MISSING"; refuse "the session list is unreadable: $DESK_LIST"; }
# a live desk: a row with an id (the field before the first ` · `) named exactly cto-desk
desk=""
while IFS= read -r row; do
    rest=${row#* · }
    [ "$rest" != "$row" ] || continue
    [ -n "${row%% · *}" ] || continue
    [ "${rest%% · *}" != "cto-desk" ] || desk=1
done <<ROWS
$rows
ROWS
[ -n "$desk" ] || notify "$DESK_MISSING"
hub=""
while IFS= read -r row; do
    rest=${row#* · }
    [ "$rest" != "$row" ] || continue
    name=${rest%% · *}
    case "$name" in
        deploy-hub-*) hub=$name; break ;;
    esac
done <<ROWS
$rows
ROWS
if [ -n "$hub" ]; then
    printf 'DEFERRED: deploy live — %s\n' "$hub"
    exit 0
fi

# 4. the close of that date already done
if closed "$cday"; then
    printf 'DONE ALREADY: close %s\n' "$cday"
    exit 0
fi

# 5. the launch, once
logs="$WT/.timer-logs"
mkdir -p "$logs" || refuse "cannot make $logs"
log="$logs/close-$cday.log"
printf '%s fire: close %s\n' "$(date '+%Y-%m-%d %H:%M:%S %Z')" "$cday" >> "$log"
sh "$LAUNCH" close "$cday" >> "$log" 2>&1
status=$?
printf 'LAUNCHED: close %s — exit %s — log %s\n' "$cday" "$status" "$log"
exit "$status"
