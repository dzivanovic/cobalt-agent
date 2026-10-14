#!/bin/sh
# devdb-copy-env.sh <place|remove> <worktree> — the `.env` and the marker of a with-DB step that
# runs on its own copy of cobalt_dev (card 547 db-copy, his R1471). gate.sh calls it from beside
# itself in copy mode; no seat types it.
#
# place <worktree>: the copy's name is read from COBALT_DEV_DB_NAME and must match
# `cobalt_dev_[a-z0-9_]{1,39}` (50 characters in all; cobalt_dev and cobalt_brain themselves fail
# it), else exit 2 and nothing is touched. The marker /Users/cobalt/cobalt-wt/.devdb-copies/<worktree>
# (outside every worktree) is written with the name, then /Users/cobalt/cobalt/.env is copied to
# /Users/cobalt/cobalt-wt/<worktree>/.env BY NAME (never read or printed, L4 / L41), the way
# take-devdb-lock.sh copies it. A failed copy removes the marker and exits 1.
# remove <worktree>: removes that `.env` and the marker, proves both gone and prints
# `copy env removed`; exit 1 if either remains. It removes nothing else, and never the lock
# directory (that is release-devdb-lock.sh's alone).
#
# EXITS: 0 done · 2 a bad argument (verb, worktree not one directory name [A-Za-z0-9._-], no such
# worktree, a copy name outside the pattern), nothing touched · 1 the copy or the removal failed.
# COBALT_WT_ROOT and COBALT_REPO_ROOT stand in for /Users/cobalt/cobalt-wt and /Users/cobalt/cobalt
# in tests/ops/test_db_copy_1014.py only; gate.sh never sets them.

export LC_ALL=C
set -u

WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
MARKS="$WT/.devdb-copies"

bad() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 2
}

[ "$#" -eq 2 ] || bad "usage: devdb-copy-env.sh <place|remove> <worktree>"
verb=$1
wt=$2
case "$wt" in
    ""|.*|*[!A-Za-z0-9._-]*) bad "worktree '$wt' is not one directory name [A-Za-z0-9._-]" ;;
esac
envf="$WT/$wt/.env"
mark="$MARKS/$wt"

case "$verb" in
    place)
        [ -d "$WT/$wt" ] || bad "no such worktree: $WT/$wt"
        copy=${COBALT_DEV_DB_NAME:-}
        rest=${copy#cobalt_dev_}
        case "$copy" in
            cobalt_dev_?*) ;;
            *) bad "copy name '$copy' is not cobalt_dev_[a-z0-9_]{1,39}" ;;
        esac
        case "$rest" in
            *[!a-z0-9_]*) bad "copy name '$copy' is not cobalt_dev_[a-z0-9_]{1,39}" ;;
        esac
        [ "${#copy}" -le 50 ] || bad "copy name '$copy' is longer than 50 characters"
        mkdir -p "$MARKS" || exit 1
        printf '%s\n' "$copy" > "$mark" || exit 1
        if cp "$REPO/.env" "$envf"; then
            printf 'copy env placed: %s\n' "$wt"
            exit 0
        fi
        rm -f "$envf" "$mark"
        printf 'REFUSED: the .env copy failed; the marker is removed\n' >&2
        exit 1
        ;;
    remove)
        rm -f "$envf" "$mark"
        left=$(ls -d "$envf" "$mark" 2>/dev/null)
        if [ -n "$left" ]; then
            printf 'REFUSED: still present after the removal: %s\n' "$left" >&2
            exit 1
        fi
        printf 'copy env removed\n'
        ;;
    *) bad "verb '$verb' is neither place nor remove" ;;
esac
