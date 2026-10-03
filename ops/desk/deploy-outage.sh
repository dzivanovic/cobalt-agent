#!/bin/sh
# deploy-outage.sh [--dry-run] "<deploy card>" <restart set> <MERGED|NOT MERGED>
# The outage of DEPLOY-HUB.md STEP-4 as ONE script (card 20 deploy-steps, row D2), on the labels
# of <restart set> only (comma-separated: com.cobalt.aset, com.cobalt.radar, com.cobalt.agent).
# The merge is NOT here: the hub merged before it calls this script and gives the state as the
# third argument; `NOT MERGED` is refused with no call made.
#
# Before anything goes down (each failure: `REFUSED: <reason>` on stderr, exit 1, nothing down):
#   the arguments (a label outside the three, an empty or repeated label, any other state);
#   the window again: `deploy-step0.sh --window "<card>"` (P1, one implementation);
#   every label proven restorable (rule E): aset and radar `launchctl print gui/501/<label>` →
#   `state = running` and `path = ` EXACTLY the plist this script bootstraps
#   ($REPO/ops/com.cobalt.aset.plist, $LAUNCHAGENTS/com.cobalt.radar.plist), the plist present;
#   the agent `cobalt.sh status` → ONLINE. The pid of each is recorded as `pid before`.
# Then, in order (STEP-4 4.2, 4.6):
#   1. each label down: aset / radar `launchctl bootout gui/501/<label>`, then `launchctl print`
#      must answer `Could not find service` (one more read after DEPLOY_SETTLE seconds); the agent
#      `cobalt.sh stop`, then `cobalt.sh status` OFFLINE.
#   2. each label up: aset / radar `launchctl bootstrap gui/501 <plist>` (`Bootstrap failed: 5` →
#      one retry), then `launchctl print` → `state = running` with a pid ≠ the pid before (loaded
#      but not running → `launchctl kickstart -k gui/501/<label>` once); the agent
#      `launchctl kickstart gui/501/com.cobalt.agent`, then `cobalt.sh status` ONLINE, a new pid.
#   3. each aset / radar of the set re-read by `launchctl print`: one not running here (it dropped
#      while a later label came up) is brought up again by step 2's calls, with the line
#      `<label> · not running at the final read (<state>): brought up again`; then
#      `cobalt.sh status` → ONLINE (the agent in the set and not ONLINE here is down again: the
#      trap kickstarts it).
# THE TRAP, on EXIT, INT, TERM, HUP, QUIT, USR1, USR2 and ALRM: every label booted out (or whose
# bootout began) and not yet up is brought up by step 2's calls (a label found running counts as
# up); the trap ignores those signals while it restores. When it brought every one up it prints
# `RESIDENTS UP (trap)`.
# A SIGKILL cannot be trapped: that one ending is the hub's (THE ONE RESUME, STEP-5 (3)).
# Output: one line per label `<label> · pid before <n> · pid after <n|down>`, then the last line
# `OUTAGE DONE <seconds>s` (exit 0) or `FAILED OUTAGE: <label> — <reason> · residents: up: <labels>
# · down: <labels>` (exit 1). Every call and its output also goes to the log
# $WT/.deploy-logs/<JOB>-outage-<timestamp>.log. It never touches a label outside the set.
# --dry-run: prints every command it WOULD run, in order (`WOULD RUN: …`), runs none (`launchctl`,
# `cobalt.sh`, `date` never called), writes no log; the arguments are still checked (NOT MERGED is
# refused); last line `DRY RUN — nothing run: <n> commands`.
# THE DESK'S DRY RUN, typed once before the first real use:
#   sh /Users/cobalt/cobalt/ops/desk/deploy-outage.sh --dry-run "<deploy card>" com.cobalt.aset,com.cobalt.radar MERGED
#
# COBALT_REPO_ROOT, COBALT_WT_ROOT and COBALT_LAUNCHAGENTS stand in for /Users/cobalt/cobalt,
# /Users/cobalt/cobalt-wt and /Users/cobalt/Library/LaunchAgents, and DEPLOY_SETTLE (default 2)
# for the seconds between a call and its re-read, in tests/ops/test_deploy_outage.py only.

export LC_ALL=C
set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
LAUNCHAGENTS=${COBALT_LAUNCHAGENTS:-/Users/cobalt/Library/LaunchAgents}
SETTLE=${DEPLOY_SETTLE:-2}
HERE=$(cd "$(dirname "$0")" && pwd)
COBALT_SH="$REPO/cobalt.sh"

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

usage="usage: deploy-outage.sh [--dry-run] \"<deploy card>\" <restart set, comma-separated labels> <MERGED|NOT MERGED>"
dry=""
if [ "${1:-}" = --dry-run ]; then
    dry=1
    shift
fi
[ "$#" -eq 3 ] || refuse "$usage"
card=$1
set_arg=$2
state=$3
[ -f "$card" ] || refuse "no such card: $card"
# the script enters $REPO below: a card given relative to the caller is read from the caller's dir
case "$card" in
    /*) ;;
    *) card="$(pwd)/$card" ;;
esac
case "$state" in
    MERGED) ;;
    "NOT MERGED") refuse "the state is NOT MERGED: the outage runs only after the hub's merge; nothing is down" ;;
    *) refuse "the state '$state' is neither MERGED nor NOT MERGED" ;;
esac
case "$set_arg" in
    ""|,*|*,|*,,*) refuse "the restart set '$set_arg' is not <label>[,<label>…]" ;;
esac
labels=""
for l in $(printf '%s' "$set_arg" | tr ',' ' '); do
    case "$l" in
        com.cobalt.aset|com.cobalt.radar|com.cobalt.agent) ;;
        *) refuse "'$l' is not a resident this script restores (com.cobalt.aset, com.cobalt.radar, com.cobalt.agent)" ;;
    esac
    case " $labels " in
        *" $l "*) refuse "'$l' is named twice in the restart set" ;;
    esac
    labels="${labels:+$labels }$l"
done

job=$(sed -n 's/^JOB: *//p' "$card" | sed -n '1p' | sed 's/[[:space:]]*$//')
case "$job" in
    ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) logname=card ;;
    *) logname=$job ;;
esac

plist_of() {
    case "$1" in
        com.cobalt.aset) printf '%s' "$REPO/ops/com.cobalt.aset.plist" ;;
        com.cobalt.radar) printf '%s' "$LAUNCHAGENTS/com.cobalt.radar.plist" ;;
    esac
}

key_of() {
    printf '%s' "${1#com.cobalt.}"
}

# ---- the dry run: every command, in order, none run -------------------------------------------
if [ -n "$dry" ]; then
    n=0
    would() {
        n=$((n + 1))
        printf 'WOULD RUN: %s\n' "$*"
    }
    would "sh $HERE/deploy-step0.sh --window \"$card\""
    for l in $labels; do
        case "$l" in
            com.cobalt.agent) would "$COBALT_SH status" ;;
            *) would "launchctl print gui/501/$l" ;;
        esac
    done
    would "date +%s"
    for l in $labels; do
        case "$l" in
            com.cobalt.agent) would "$COBALT_SH stop"; would "$COBALT_SH status" ;;
            *) would "launchctl bootout gui/501/$l"; would "launchctl print gui/501/$l" ;;
        esac
    done
    for l in $labels; do
        case "$l" in
            com.cobalt.agent) would "launchctl kickstart gui/501/com.cobalt.agent"; would "$COBALT_SH status" ;;
            *) would "launchctl bootstrap gui/501 $(plist_of "$l")"; would "launchctl print gui/501/$l" ;;
        esac
    done
    would "date +%s"
    for l in $labels; do
        [ "$l" = com.cobalt.agent ] || would "launchctl print gui/501/$l"
    done
    would "$COBALT_SH status"
    printf 'DRY RUN — nothing run: %s commands\n' "$n"
    exit 0
fi

# ---- the log ---------------------------------------------------------------------------------
# cobalt.sh reads its pid file relative to the repo, as the hub runs it from there
cd "$REPO" || refuse "cannot enter $REPO"
logdir="$WT/.deploy-logs"
mkdir -p "$logdir" || refuse "mkdir failed: $logdir"
log="$logdir/$logname-outage-$(date +%Y%m%d-%H%M%S).log"
: >> "$log" || refuse "cannot write the log: $log"

say() {
    printf '%s\n' "$*"
    printf '%s\n' "$*" >> "$log"
}
note() {
    printf '%s\n' "$*" >> "$log"
}
first() {
    printf '%s\n' "$1" | sed '/^[[:space:]]*$/d' | sed -n '1p'
}

note "deploy-outage.sh \"$card\" $set_arg $state"

# ---- the window, again -----------------------------------------------------------------------
note "\$ sh $HERE/deploy-step0.sh --window \"$card\""
wout=$(sh "$HERE/deploy-step0.sh" --window "$card" 2>&1)
wrc=$?
note "$wout"
note "[exit $wrc]"
if [ "$wrc" -ne 0 ]; then
    wlast=$(printf '%s\n' "$wout" | sed '/^[[:space:]]*$/d' | tail -n 1)
    refuse "window — ${wlast#FAILED STEP-0: window — }; nothing is down"
fi

# lc <args…>: launchctl, logged; sets $out and $rc
lc() {
    note "\$ launchctl $*"
    out=$(launchctl "$@" 2>&1)
    rc=$?
    note "$out"
    note "[exit $rc]"
}

# agent <verb>: cobalt.sh, logged; sets $out and $rc
agent() {
    note "\$ $COBALT_SH $1"
    out=$("$COBALT_SH" "$1" 2>&1)
    rc=$?
    note "$out"
    note "[exit $rc]"
}

# read_label <label>: launchctl print → $pstate (running|loaded|gone|error), $ppid, $ppath
read_label() {
    lc print "gui/501/$1"
    ppid=$(printf '%s\n' "$out" | sed -n 's/^[[:space:]]*pid = \([0-9][0-9]*\).*/\1/p' | sed -n '1p')
    ppath=$(printf '%s\n' "$out" | sed -n 's/^[[:space:]]*path = \(.*\)$/\1/p' | sed -n '1p')
    if [ "$rc" -eq 0 ]; then
        if printf '%s\n' "$out" | grep -q -E '^[[:space:]]*state = running$'; then
            pstate=running
        else
            pstate=loaded
        fi
    elif [ "$rc" -eq 113 ] || printf '%s\n' "$out" | grep -q -F "Could not find service"; then
        pstate=gone
    else
        pstate=error
    fi
}

# agent_pid: cobalt.sh status → $apid when ONLINE, else empty
agent_pid() {
    agent status
    apid=$(printf '%s\n' "$out" | sed -n 's/.*ONLINE (PID: \([0-9][0-9]*\)).*/\1/p' | sed -n '1p')
}

# ---- every label proven restorable before anything goes down (rule E) -------------------------
for l in $labels; do
    k=$(key_of "$l")
    if [ "$l" = com.cobalt.agent ]; then
        [ -x "$COBALT_SH" ] || refuse "$COBALT_SH is not an executable file; nothing is down"
        agent_pid
        [ -n "$apid" ] || refuse "$l is not ONLINE before the outage: $(first "$out"); nothing is down"
        eval "before_$k=\$apid"
        continue
    fi
    p=$(plist_of "$l")
    [ -f "$p" ] || refuse "$l: no plist at $p, so its bootstrap could not restore it; nothing is down"
    read_label "$l"
    [ "$pstate" = running ] || refuse "$l is not running before the outage ($pstate): $(first "$out"); nothing is down"
    [ "$ppath" = "$p" ] || refuse "$l is loaded from '$ppath'; the bootstrap of $p would not restore it; nothing is down"
    eval "before_$k=\$ppid"
done

# ---- the trap: every label down comes back up on every exit -----------------------------------
down=""
cur=""
reason=""
done_ok=""

remove_down() {
    nd=""
    for d in $down; do
        [ "$d" = "$1" ] || nd="${nd:+$nd }$d"
    done
    down=$nd
}

# up_one <label> <main|trap>: bring one label up; 0 when it runs, else 1 with $why
up_one() {
    why=""
    k=$(key_of "$1")
    eval "b=\${before_$k:-}"
    if [ "$1" = com.cobalt.agent ]; then
        lc kickstart gui/501/com.cobalt.agent
        tries=0
        apid=""
        while [ "$tries" -lt 3 ]; do
            agent_pid
            [ -z "$apid" ] || break
            tries=$((tries + 1))
            sleep "$SETTLE"
        done
        if [ -z "$apid" ]; then
            why="not ONLINE after kickstart: $(first "$out")"
            return 1
        fi
        eval "after_$k=\$apid"
        if [ "$2" = main ] && [ "$apid" = "$b" ]; then
            why="the pid is unchanged ($apid): not restarted"
            return 1
        fi
        return 0
    fi
    p=$(plist_of "$1")
    lc bootstrap gui/501 "$p"
    if [ "$rc" -ne 0 ]; then
        bout=$out
        case "$out" in
            *"Bootstrap failed: 5"*)
                sleep "$SETTLE"
                lc bootstrap gui/501 "$p"
                bout=$out
                ;;
        esac
    fi
    read_label "$1"
    if [ "$pstate" = loaded ]; then
        lc kickstart -k "gui/501/$1"
        sleep "$SETTLE"
        read_label "$1"
    fi
    if [ "$pstate" != running ]; then
        why="not running after bootstrap ($pstate): $(first "${bout:-$out}")"
        return 1
    fi
    eval "after_$k=\$ppid"
    if [ "$2" = main ] && [ "$ppid" = "$b" ]; then
        why="the pid is unchanged ($ppid): not restarted"
        return 1
    fi
    return 0
}

lines() {
    for l in $labels; do
        k=$(key_of "$l")
        eval "b=\${before_$k:-none}"
        case " $down " in
            *" $l "*) a=down ;;
            *) eval "a=\${after_$k:-\$b}" ;;
        esac
        say "$l · pid before $b · pid after $a"
    done
}

on_exit() {
    xrc=$?
    trap '' INT TERM HUP QUIT USR1 USR2 ALRM
    trap - EXIT
    [ -z "$done_ok" ] || exit "$xrc"
    restored=""
    for l in $down; do
        bout=""
        if up_one "$l" trap; then
            remove_down "$l"
            restored=1
        else
            note "trap: $l — $why"
        fi
    done
    lines
    if [ -n "$restored" ] && [ -z "$down" ]; then
        say "RESIDENTS UP (trap)"
    fi
    upl=""
    for l in $labels; do
        case " $down " in
            *" $l "*) ;;
            *) upl="${upl:+$upl,}$l" ;;
        esac
    done
    dl=$(printf '%s' "$down" | tr ' ' ',')
    say "FAILED OUTAGE: ${cur:--} — ${reason:-exit $xrc} · residents: up: ${upl:-none} · down: ${dl:-none}"
    exit 1
}

on_signal() {
    reason="signal $1"
    exit 1
}

fail() {
    cur=$1
    reason=$2
    exit 1
}

trap on_exit EXIT
trap 'on_signal INT' INT
trap 'on_signal TERM' TERM
trap 'on_signal HUP' HUP
# every other signal whose default ends the shell, so the EXIT trap still runs (QUIT kills sh
# without it)
trap 'on_signal QUIT' QUIT
trap 'on_signal USR1' USR1
trap 'on_signal USR2' USR2
trap 'on_signal ALRM' ALRM

t0=$(date +%s)

# ---- 1. each label down ----------------------------------------------------------------------
for l in $labels; do
    cur=$l
    # in the list BEFORE the call: a signal during it still brings the label back
    down="${down:+$down }$l"
    if [ "$l" = com.cobalt.agent ]; then
        agent stop
        agent_pid
        [ -z "$apid" ] || fail "$l" "still ONLINE after cobalt.sh stop: $(first "$out")"
        continue
    fi
    lc bootout "gui/501/$l"
    read_label "$l"
    if [ "$pstate" = running ] || [ "$pstate" = loaded ]; then
        sleep "$SETTLE"
        read_label "$l"
    fi
    case "$pstate" in
        gone) ;;
        running|loaded) fail "$l" "still loaded after bootout" ;;
        *) fail "$l" "launchctl print exit $rc after bootout: $(first "$out")" ;;
    esac
done

# ---- 2. each label up ------------------------------------------------------------------------
for l in $labels; do
    cur=$l
    bout=""
    up_one "$l" main || fail "$l" "$why"
    remove_down "$l"
done

# ---- 3. every label still up, the agent ONLINE -------------------------------------------------
t1=$(date +%s)
# a label that dropped after its own bootstrap (while a later one came up) is down again: it is
# brought up once more by its own way, said on a line; a failure there is the trap's
for l in $labels; do
    [ "$l" != com.cobalt.agent ] || continue
    read_label "$l"
    [ "$pstate" != running ] || continue
    say "$l · not running at the final read ($pstate): brought up again"
    cur=$l
    down="${down:+$down }$l"
    bout=""
    up_one "$l" main || fail "$l" "$why"
    remove_down "$l"
done
cur=com.cobalt.agent
agent_pid
if [ -z "$apid" ]; then
    # the agent of the set dropped after its start: down again, so the trap kickstarts it
    case " $labels " in
        *" com.cobalt.agent "*) down="${down:+$down }com.cobalt.agent" ;;
    esac
    fail com.cobalt.agent "cobalt.sh status is not ONLINE: $(first "$out")"
fi

done_ok=1
lines
secs=$((t1 - t0))
say "OUTAGE DONE ${secs}s"
exit 0
