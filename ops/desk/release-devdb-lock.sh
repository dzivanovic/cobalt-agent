#!/bin/sh
# release-devdb-lock.sh <worktree> — gives back the cobalt_dev lock that take-devdb-lock.sh took
# (L76 as amended, his 2026-10-01 R20; card 07 devdb-lock).
#
# INSTALLS AT: /Users/cobalt/.claude/ops/release-devdb-lock.sh, a symlink to this file (the desk's).
# THE HUB TYPES: sh /Users/cobalt/.claude/ops/release-devdb-lock.sh <WORKTREE>
#
# Removes /Users/cobalt/cobalt-wt/<worktree>/.env and the lock directory
# /Users/cobalt/cobalt-wt/.cobalt_dev.lock ONLY when the lock names this worktree, then proves both
# gone (`ls` prints nothing) and prints `lock released`. A lock held by another worktree is not
# touched, and neither is anything else. With no lock held, a `.env` in this worktree is not ours to
# remove (exit 3); with no lock and no `.env` there is nothing to give back (exit 0), and a lock
# another worktree takes meanwhile is never removed (check G2, G3).
#
# EXITS: 0 released and proven gone · 2 a bad worktree name, nothing touched · 3 the lock is held
# by another worktree, or no lock names this worktree and its .env is present, nothing touched ·
# 1 something is still there after the removal.
# COBALT_WT_ROOT stands in for /Users/cobalt/cobalt-wt in tests/ops/test_devdb_lock.py only.

export LC_ALL=C
set -u

WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
LOCK="$WT/.cobalt_dev.lock"

[ "$#" -eq 1 ] || { printf 'REFUSED: usage: release-devdb-lock.sh <worktree>\n' >&2; exit 2; }
wt=$1
case "$wt" in
    ""|.*|*[!A-Za-z0-9._-]*)
        printf "REFUSED: worktree '%s' is not one directory name [A-Za-z0-9._-]\n" "$wt" >&2
        exit 2
        ;;
esac
envf="$WT/$wt/.env"

mine=""
if [ -d "$LOCK" ]; then
    holder=$(cat "$LOCK/owner" 2>/dev/null)
    if [ "$holder" != "$wt" ]; then
        printf 'REFUSED: the cobalt_dev lock is held by %s, not %s; nothing touched\n' "${holder:-unknown}" "$wt" >&2
        exit 3
    fi
    mine=1
elif [ -e "$envf" ]; then
    printf 'REFUSED: no cobalt_dev lock names %s, so its .env is not ours to remove; nothing touched\n' "$wt" >&2
    exit 3
fi

rm -f "$envf"
# only the lock this worktree holds is removed: while it stands nobody else can take it, and with
# none held a lock taken meanwhile is another worktree's
if [ -n "$mine" ]; then
    rm -f "$LOCK/owner"
    rmdir "$LOCK"
fi
left=$(ls -d "$envf" 2>/dev/null)
if [ -n "$mine" ] && [ -d "$LOCK" ] && [ "$(cat "$LOCK/owner" 2>/dev/null)" = "$wt" ]; then
    left="$left $LOCK"
fi
if [ -n "$left" ]; then
    printf 'REFUSED: still present after the release: %s\n' "$left" >&2
    exit 1
fi
printf 'lock released\n'
