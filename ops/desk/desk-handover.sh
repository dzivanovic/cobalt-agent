#!/bin/sh
# desk-handover.sh <predecessor id>
# Ends a predecessor CTO desk safely (card 18 desk-tools-b, row B4; checklist H2, H2a).
#   1. REFUSED unless `claude agents --json` lists the id with the session name `cto-desk`.
#   2. Runs `wait-desk-idle.sh <predecessor> <newest desk report> 600` beside this script
#      (DESK_HANDOVER_WAIT=<seconds> shortens the wait).
#   3. The wait returns (exit 0: the turn ended, the state is no longer `working`, or the row is
#      gone) → `claude stop <predecessor>`, then `claude rm <predecessor>`, each printed first as
#      `RUN: …`, each alone. An exit 0 that is not `turn ended REFRESHED` is re-read first
#      (the wait returns 0 when its own list read fails): still `working`, no state or an
#      unreadable list → REFUSED, nothing stopped. The wait times out (exit 2) → it stops only when `claude agents
#      --json` now shows the predecessor's state is not `working`; still `working` → `REFUSED:
#      predecessor still working`, exit 1. Any other exit of the wait, a row gone at that read,
#      or an unreadable list → REFUSED, nothing stopped.
# REFUSED (stderr, exit 1, nothing stopped): an id outside [0-9a-f-] or shorter than 8; no desk
# report cto-<date>.md; wait-desk-idle.sh not beside this script.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt).

export LC_ALL=C
set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
REPORTS="$REPO/docs/40 - DevDocs/reports"
here=$(dirname "$0")

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 1 ] || refuse "usage: desk-handover.sh <predecessor id>"
pred=$1
case "$pred" in
    ""|*[!0123456789abcdef-]*) refuse "predecessor id '$pred' holds a character outside [0-9a-f-]" ;;
esac
[ "${#pred}" -ge 8 ] || refuse "predecessor id '$pred' is shorter than 8 characters"
wait_for=${DESK_HANDOVER_WAIT:-600}
case "$wait_for" in
    ""|*[!0-9]*) refuse "DESK_HANDOVER_WAIT '$wait_for' is not a number of seconds" ;;
esac
[ -f "$here/wait-desk-idle.sh" ] || refuse "wait-desk-idle.sh is not beside this script"
newest=$(ls "$REPORTS" 2>/dev/null | grep -E '^cto-[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$' | sort | tail -n 1)
[ -n "$newest" ] || refuse "no desk report cto-<date>.md under $REPORTS"

# row -> "<name><TAB><state>" for the predecessor, or ABSENT, or UNREADABLE
row() {
    claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
except Exception:
    print("UNREADABLE")
    sys.exit(0)
a = next((a for a in rows if isinstance(a, dict) and a.get("id") == sys.argv[1]), None)
print("ABSENT" if a is None else "%s\t%s" % (a.get("name", ""), a.get("state", "")))
' "$pred" 2>/dev/null || echo UNREADABLE
}
tab=$(printf '\t')

info=$(row)
case "$info" in
    UNREADABLE|"") refuse "the session list is unreadable (claude agents --json)" ;;
    ABSENT) refuse "no session $pred in claude agents --json" ;;
esac
name=${info%%"$tab"*}
[ "$name" = "cto-desk" ] || refuse "session $pred is named '$name', not cto-desk"

waited=$(sh "$here/wait-desk-idle.sh" "$pred" "$REPORTS/$newest" "$wait_for")
rc=$?
printf '%s\n' "$waited"
case "$rc" in
    0)
        # the wait also returns 0 when its own list read failed (it prints "<id>: " with no
        # state, check O1): only a REFRESHED turn end stands alone; any other return is re-read
        said=$(printf '%s\n' "$waited" | sed -n '1p')
        if [ "$said" != "$pred: turn ended REFRESHED" ]; then
            info=$(row)
            case "$info" in
                UNREADABLE|"") refuse "the wait returned '$said' and the session list is unreadable; nothing stopped" ;;
                ABSENT) ;;
                *)
                    state=${info#*"$tab"}
                    case "$state" in
                        working|"") refuse "the wait returned '$said' but $pred is still ${state:-of no state}; nothing stopped" ;;
                    esac
                    ;;
            esac
        fi
        ;;
    2)
        info=$(row)
        case "$info" in
            UNREADABLE|"") refuse "the wait timed out and the session list is unreadable; nothing stopped" ;;
            ABSENT) refuse "the wait timed out and $pred is gone from the list; nothing to stop" ;;
        esac
        state=${info#*"$tab"}
        [ "$state" != "working" ] || refuse "predecessor still working"
        ;;
    *) refuse "wait-desk-idle.sh exited $rc; nothing stopped" ;;
esac

printf 'RUN: claude stop %s\n' "$pred"
claude stop "$pred" || refuse "claude stop $pred failed; claude rm not run"
printf 'RUN: claude rm %s\n' "$pred"
claude rm "$pred" || { printf 'desk-handover: %s stopped; claude rm FAILED\n' "$pred"; exit 1; }
printf 'desk-handover: %s stopped and removed\n' "$pred"
