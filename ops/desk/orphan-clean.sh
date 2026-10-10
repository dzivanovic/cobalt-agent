#!/bin/sh
# orphan-clean.sh <label>          the DRY RUN (the default): finds, verifies and prints; signals nothing
# orphan-clean.sh --kill <label>   the only call that signals: each verified orphan, by pid only
# Finds a resident's python child left behind with ppid 1 by a bootout (card 229 orphan-clean-1010,
# rows O1-O4; reports/cto-2026-10-10.md R851 the incident, R853 the cause, R854 SIGTERM ignored,
# R855 his ruling). Any other label, a second label, an unknown flag or a flag after the label:
# `REFUSED: <reason>` on stderr, exit 1, nothing read.
#
# THE LABEL TABLE (closed, one entry):
#   aset   job com.cobalt.aset · argv `python -m cobalt.aset` · lock /Users/cobalt/.cobalt/voice-scratch/.lock
#          (ops/start_aset.sh:35, src/cobalt/voice/scratch.py:43, taken at src/cobalt/voice/web.py:161)
#          · port 5010 (src/cobalt/aset/config.py:82)
#
# WHAT IT RUNS, in order, and nothing else (read only up to the first kill):
#   ps -A -o pid= -o ppid= -o command=      the process table. A CANDIDATE has ppid 1 and a command
#                                           that is, split on blanks, exactly `<path>/python[3[.N]] -m
#                                           cobalt.<label>`; no substring, no pattern over the line.
#   launchctl print gui/501/<job>           the job's pid: a non-zero exit whose whole answer is the
#                                           one line `Could not find service "<job>" in domain for
#                                           user gui: 501` = no job pid; one top-level `state = running`
#                                           and one `pid = <n>` = the job pid, SPARED, never signalled;
#                                           any other shape REFUSED.
#   lsof -nP -a -p <pid> -Fn -- <lock>      VERIFIED when it prints `n<lock>`;
#   lsof -nP -a -p <pid> -iTCP:<port> -sTCP:LISTEN -Fp   VERIFIED when it prints `p<pid>`.
#                                           Both run at verify and again before EACH signal (neither
#                                           held then: REFUSED). The pid written inside .lock is never
#                                           proof (scratch.py:212 writes it, release at
#                                           scratch.py:225-231 never clears it).
#   ps -p <pid> -o ppid= -o lstart= -o command=   the identity of each verified pid, read at verify
#                                           (ppid 1 and the candidate's own command, else UNVERIFIED:
#                                           pid reuse), again before EACH signal (unchanged, else
#                                           REFUSED: pid reuse) and once a second while waiting.
#   kill -TERM <pid>, then kill -KILL <pid> when the same process is still there after the grace
#                                           (--kill only; each printed first as `RUN: kill -<SIG> <pid>`).
#   sleep 1                                 between identity reads, up to the grace (10 s) per signal.
#   mktemp -d, rm -rf of that one directory, grep, sed, printf: the script's own scratch and parsing.
# A candidate holding neither lock nor port, a ps that exits non-zero, an lsof that exits non-zero
# with stderr, a ps line
# that does not parse, or an unknown launchctl shape: `UNVERIFIED: <pid> — <why>` and REFUSED,
# exit 1, nothing signalled in the whole run.
# TOUCHES: nothing but the signals above to the verified pids; no file outside its mktemp directory.
#
# Lines: CANDIDATE / SPARED / VERIFIED / UNVERIFIED, then WOULD KILL (dry run) or RUN / KILLED /
# FAILED (--kill). Last line `orphan-clean: <label> dry-run · verified <n> · spared <m> · killed 0`,
# `orphan-clean: <label> · verified <n> · spared <m> · killed <k>`, or `orphan-clean: <label> · none found`.
#
# TEST-ONLY, in tests/ops/test_orphan_clean.py only: ORPHAN_CLEAN_KILL (the command that sends a
# signal; default the shell's kill) and ORPHAN_CLEAN_GRACE (whole seconds; default 10).

export LC_ALL=C
set -u
set -f

KILL=${ORPHAN_CLEAN_KILL:-kill}
GRACE=${ORPHAN_CLEAN_GRACE:-10}
TAB=$(printf '\t')

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

case "$GRACE" in
    ""|*[!0-9]*) refuse "ORPHAN_CLEAN_GRACE '$GRACE' is not a whole number of seconds" ;;
esac

mode=dry
case "$#" in
    1) label=$1 ;;
    2) [ "$1" = "--kill" ] || refuse "usage: orphan-clean.sh [--kill] <label>; got '$1 $2'"
       mode=kill
       label=$2 ;;
    *) refuse "usage: orphan-clean.sh [--kill] <label>" ;;
esac
case "$label" in
    aset)
        JOB=com.cobalt.aset
        MODULE=cobalt.aset
        LOCK=/Users/cobalt/.cobalt/voice-scratch/.lock
        PORT=5010
        ;;
    *) refuse "label '$label' is not in the label table (aset)" ;;
esac

tmp=$(mktemp -d "${TMPDIR:-/tmp}/orphan-clean.XXXXXX") || refuse "mktemp failed"
trap 'rm -rf "$tmp"' EXIT

first_line() {
    sed -n '/[^[:space:]]/{p;q;}' "$1"
}

# is_candidate WORD... -> 0 when the words are exactly <path>/python[3[.N]] -m cobalt.<label>
is_candidate() {
    [ "$#" -eq 3 ] && [ "$2" = "-m" ] && [ "$3" = "$MODULE" ] || return 1
    case "$1" in
        */*) ;;
        *) return 1 ;;
    esac
    case "${1##*/}" in
        python|python3) return 0 ;;
        python3.*)
            case "${1##*/python3.}" in
                ""|*[!0-9]*) return 1 ;;
            esac
            return 0 ;;
    esac
    return 1
}

# ident_of PID -> $ident: the `ps -p` reading, empty when the pid is gone
ident_of() {
    ps -p "$1" -o ppid= -o lstart= -o command= < /dev/null > "$tmp/id.out" 2> "$tmp/id.err"
    rc=$?
    ident=$(sed -n '1p' "$tmp/id.out")
    if [ "$rc" -ne 0 ] && [ -s "$tmp/id.err" ]; then
        printf 'UNVERIFIED: %s — ps -p exited %s: %s\n' "$1" "$rc" "$(first_line "$tmp/id.err")"
        refuse "ps -p $1 exited $rc: $(first_line "$tmp/id.err")"
    fi
    [ "$rc" -eq 0 ] || ident=""
}

# prove PID -> $proof: `lock`, `port`, `both`, `none`, or `error: <why>` (the lsof proof, O2 (3))
prove() {
    proof=none
    lsof -nP -a -p "$1" -Fn -- "$LOCK" < /dev/null > "$tmp/lsof.out" 2> "$tmp/lsof.err"
    rc=$?
    if [ "$rc" -ne 0 ] && [ -s "$tmp/lsof.err" ]; then
        proof="error: lsof (lock) exited $rc: $(first_line "$tmp/lsof.err")"
        return
    fi
    if [ "$rc" -eq 0 ] && grep -q -x -F "n$LOCK" "$tmp/lsof.out"; then
        proof=lock
    fi
    lsof -nP -a -p "$1" -iTCP:"$PORT" -sTCP:LISTEN -Fp < /dev/null > "$tmp/lsof.out" 2> "$tmp/lsof.err"
    rc=$?
    if [ "$rc" -ne 0 ] && [ -s "$tmp/lsof.err" ]; then
        proof="error: lsof (port) exited $rc: $(first_line "$tmp/lsof.err")"
        return
    fi
    if [ "$rc" -eq 0 ] && grep -q -x -F "p$1" "$tmp/lsof.out"; then
        if [ "$proof" = lock ]; then proof=both; else proof=port; fi
    fi
}

# ---- O2 (1) the candidates --------------------------------------------------------------------
ps -A -o pid= -o ppid= -o command= > "$tmp/ps.out" 2> "$tmp/ps.err"
rc=$?
if [ "$rc" -ne 0 ]; then
    printf 'UNVERIFIED: ? — ps -A exited %s: %s\n' "$rc" "$(first_line "$tmp/ps.err")"
    refuse "ps -A exited $rc: $(first_line "$tmp/ps.err")"
fi
: > "$tmp/candidates"
while IFS= read -r line; do
    set -- $line
    [ "$#" -gt 0 ] || continue
    if [ "$#" -lt 3 ]; then
        printf 'UNVERIFIED: ? — ps line does not parse: %s\n' "$line"
        refuse "a ps line does not parse; nothing signalled"
    fi
    case "$1$2" in
        *[!0-9]*)
            printf 'UNVERIFIED: ? — ps line does not parse: %s\n' "$line"
            refuse "a ps line does not parse; nothing signalled" ;;
    esac
    pid=$1
    ppid=$2
    shift 2
    [ "$ppid" = 1 ] || continue
    is_candidate "$@" || continue
    printf '%s %s\n' "$pid" "$*" >> "$tmp/candidates"
done < "$tmp/ps.out"

if [ ! -s "$tmp/candidates" ]; then
    printf 'orphan-clean: %s · none found\n' "$label"
    exit 0
fi

# ---- O2 (2) the job's own pid -----------------------------------------------------------------
launchctl print "gui/501/$JOB" < /dev/null > "$tmp/lc" 2>&1
rc=$?
jobpid=""
# `Could not find service` counts only as launchctl's whole answer: a non-zero exit and that one line
if [ "$rc" -ne 0 ] && [ "$(grep -c '[^[:space:]]' "$tmp/lc")" = 1 ] \
        && [ "$(first_line "$tmp/lc")" = "Could not find service \"$JOB\" in domain for user gui: 501" ]; then
    jobpid=""
elif [ "$rc" -ne 0 ]; then
    refuse "launchctl print gui/501/$JOB exited $rc: $(first_line "$tmp/lc") (unverifiable, L1)"
else
    state=$(sed -n "s/^${TAB}state = //p" "$tmp/lc")
    jobpid=$(sed -n "s/^${TAB}pid = //p" "$tmp/lc")
    [ "$state" = "running" ] || refuse "launchctl print gui/501/$JOB: state is not one 'running' line (unverifiable, L1)"
    case "$jobpid" in
        ""|*[!0-9]*) refuse "launchctl print gui/501/$JOB: not one 'pid = <n>' line (unverifiable, L1)" ;;
    esac
fi

# ---- O2 (3)-(4) verify each candidate; all or nothing -----------------------------------------
verified=""
nv=0
ns=0
bad=0
while IFS= read -r line; do
    pid=${line%% *}
    command=${line#* }
    printf 'CANDIDATE: %s ppid 1 %s\n' "$pid" "$command"
    if [ "$pid" = "$jobpid" ]; then
        printf "SPARED: %s is %s's own pid\n" "$pid" "$JOB"
        ns=$((ns + 1))
        continue
    fi
    prove "$pid"
    case "$proof" in
        error:*)
            printf 'UNVERIFIED: %s — %s\n' "$pid" "${proof#error: }"
            bad=1
            continue ;;
        none)
            printf 'UNVERIFIED: %s — holds neither lock %s nor port :%s\n' "$pid" "$LOCK" "$PORT"
            bad=1
            continue ;;
    esac
    case "$proof" in lock|both) printf 'VERIFIED: %s holds lock %s\n' "$pid" "$LOCK" ;; esac
    case "$proof" in port|both) printf 'VERIFIED: %s listens on :%s\n' "$pid" "$PORT" ;; esac
    # the identity a signal is checked against (O4): same ppid 1, start time and command. The
    # reading must still be the candidate (ppid 1, its exact command after the 5-word lstart),
    # or the pid was reused after ps -A
    ident_of "$pid"
    set -- $ident
    if [ "$#" -lt 7 ] || [ "$1" != 1 ]; then
        printf 'UNVERIFIED: %s — ps -p no longer shows it with ppid 1\n' "$pid"
        bad=1
        continue
    fi
    shift 6
    if [ "$*" != "$command" ]; then
        printf 'UNVERIFIED: %s — ps -p shows another command: %s\n' "$pid" "$*"
        bad=1
        continue
    fi
    printf '%s\n' "$ident" > "$tmp/ident.$pid"
    verified="$verified $pid"
    nv=$((nv + 1))
done < "$tmp/candidates"

[ "$bad" -eq 0 ] || refuse "a candidate is unverified; nothing signalled"

# ---- O3 the dry run ---------------------------------------------------------------------------
if [ "$mode" = dry ]; then
    for pid in $verified; do
        printf 'WOULD KILL: %s\n' "$pid"
    done
    printf 'orphan-clean: %s dry-run · verified %s · spared %s · killed 0\n' "$label" "$nv" "$ns"
    exit 0
fi

# ---- O4 the kill, by pid only -----------------------------------------------------------------
# gone PID -> 0 once the reading differs from the one taken at verify, polled up to the grace
gone() {
    waited=0
    while :; do
        ident_of "$1"
        [ "$ident" = "$saved" ] || return 0
        [ "$waited" -lt "$GRACE" ] || return 1
        sleep 1
        waited=$((waited + 1))
    done
}

# signal PID SIG -> 0 when gone after it
signal() {
    ident_of "$1"
    [ "$ident" = "$saved" ] || refuse "$1 changed before $2"
    # the lock or port proof again, at the moment of the signal (X1)
    prove "$1"
    case "$proof" in
        error:*)
            printf 'UNVERIFIED: %s — %s\n' "$1" "${proof#error: }"
            refuse "$1 is unverifiable before $2" ;;
        none)
            printf 'UNVERIFIED: %s — holds neither lock %s nor port :%s before %s\n' "$1" "$LOCK" "$PORT" "$2"
            refuse "$1 no longer holds the lock or port before $2" ;;
    esac
    printf 'RUN: kill -%s %s\n' "$2" "$1"
    "$KILL" "-$2" "$1" < /dev/null
    gone "$1"
}

nk=0
for pid in $verified; do
    IFS= read -r saved < "$tmp/ident.$pid"
    if signal "$pid" TERM; then
        printf 'KILLED: %s (TERM)\n' "$pid"
    elif signal "$pid" KILL; then
        printf 'KILLED: %s (KILL)\n' "$pid"
    else
        printf 'FAILED: %s survived KILL\n' "$pid"
        exit 1
    fi
    nk=$((nk + 1))
done
printf 'orphan-clean: %s · verified %s · spared %s · killed %s\n' "$label" "$nv" "$ns" "$nk"
exit 0
