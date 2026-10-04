#!/bin/sh
# take-devdb-lock.sh <worktree> <minutes> — takes the ONE cobalt_dev lock (L76 as amended, his
# 2026-10-01 R20; card 07 devdb-lock). A with-DB step of a build, a check or a deploy gate runs it
# before its first COBALT_ENV=dev call and releases with release-devdb-lock.sh at the step's end.
#
# INSTALLS AT: /Users/cobalt/.claude/ops/take-devdb-lock.sh, a symlink to this file (the desk's).
# THE HUB TYPES: sh /Users/cobalt/.claude/ops/take-devdb-lock.sh <WORKTREE> 90
#
# THE LOCK IS THE MKDIR: `mkdir /Users/cobalt/cobalt-wt/.cobalt_dev.lock` either creates the
# directory or fails, atomically, so two takes at once never both win (today's `ls` then `cp`
# could). The winner writes its worktree name into the lock's `owner` file, then copies
# /Users/cobalt/cobalt/.env to /Users/cobalt/cobalt-wt/<worktree>/.env BY NAME (never read or
# printed, L4 / L41). A held lock is tried again every 60 s up to <minutes>; then exit 4 with
# `cobalt_dev lock not free in <minutes> min (held by <worktree>)`.
#
# EXITS: 0 taken · 2 a bad argument (worktree not one directory name [A-Za-z0-9._-], or minutes
# not a whole number), nothing touched · 4 not free in time, nothing touched · 1 the copy failed
# (the lock is given back).
# COBALT_WT_ROOT and COBALT_REPO_ROOT stand in for /Users/cobalt/cobalt-wt and /Users/cobalt/cobalt
# in tests/ops/test_devdb_lock.py only; the hubs never set them.

export LC_ALL=C
set -u

WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
LOCK="$WT/.cobalt_dev.lock"

bad() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 2
}

[ "$#" -eq 2 ] || bad "usage: take-devdb-lock.sh <worktree> <minutes>"
wt=$1
minutes=$2
case "$wt" in
    ""|.*|*[!A-Za-z0-9._-]*) bad "worktree '$wt' is not one directory name [A-Za-z0-9._-]" ;;
esac
case "$minutes" in
    ""|*[!0-9]*) bad "minutes '$minutes' is not a whole number" ;;
esac
[ -d "$WT/$wt" ] || bad "no such worktree: $WT/$wt"

tries=0
while :; do
    if mkdir "$LOCK" 2>/dev/null; then
        printf '%s\n' "$wt" > "$LOCK/owner"
        if cp "$REPO/.env" "$WT/$wt/.env"; then
            printf 'lock taken: %s\n' "$wt"
            exit 0
        fi
        rm -f "$WT/$wt/.env" "$LOCK/owner"
        rmdir "$LOCK"
        printf 'REFUSED: the .env copy failed; the lock is given back\n' >&2
        exit 1
    fi
    [ "$tries" -lt "$minutes" ] || break
    tries=$((tries + 1))
    sleep 60
done
holder=$(cat "$LOCK/owner" 2>/dev/null)
printf 'cobalt_dev lock not free in %s min (held by %s)\n' "$minutes" "${holder:-unknown}" >&2
exit 4
