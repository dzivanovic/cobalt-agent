#!/bin/sh
# job-clean.sh "<job card>"
# Removes a landed job's worktree and branch (card 18 desk-tools-b, row B2). It reads the card's
# BRANCH and WORKTREE. It needs, each proven first (else REFUSED on stderr, exit 1, nothing removed):
#   - the WORKTREE a plain name: exactly $WT/<one directory name>, never agy-trial, never a
#     symlink, and registered with git as a worktree with BRANCH checked out;
#   - `git -C $REPO merge-base --is-ancestor <BRANCH> main` to hold (the job landed);
#   - the worktree clean (`git status --porcelain` empty) and holding no .env.
# Then `git -C $REPO worktree remove <worktree>` and `git -C $REPO branch -d <branch>` (never
# forced), each printed first as `RUN: …`; the last line `job-clean: <worktree> and <branch> removed`.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).

export LC_ALL=C
set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 1 ] || refuse "usage: job-clean.sh \"<job card>\""
card=$1
[ -f "$card" ] || refuse "no such card: $card"

# field KEY -> the value of the first "KEY: value" line, trailing blanks cut (desk-launch.sh's)
field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}
branch=$(field BRANCH)
wt=$(field WORKTREE)

case "$branch" in
    ""|*[!A-Za-z0-9._/-]*|-*|*..*) refuse "BRANCH '$branch' is not a plain branch name" ;;
esac
[ "$branch" != "main" ] || refuse "BRANCH is main"

# ---- the worktree: exactly $WT/<one directory name>, a real directory, git's, on BRANCH -------
case "$wt" in
    ""|.*|*[!A-Za-z0-9._-]*) refuse "worktree '$wt' is outside the approved pattern $WT/<one directory name>" ;;
esac
[ "$wt" != "agy-trial" ] || refuse "worktree 'agy-trial' is the check hubs' scratch tree, never a job's"
path="$WT/$wt"
[ ! -L "$path" ] || refuse "$path is a symlink"
[ -d "$path" ] || refuse "no job worktree at $path"
registered=$(git -C "$REPO" worktree list --porcelain | awk -v p="worktree $path" -v b="branch refs/heads/$branch" '
    $0 == p { on = 1; next }
    /^worktree / { on = 0 }
    on && $0 == b { print "yes" }')
[ "$registered" = "yes" ] || refuse "$path is not a worktree of $REPO with $branch checked out"

# ---- landed, clean, no lock ------------------------------------------------------------------
git -C "$REPO" merge-base --is-ancestor "refs/heads/$branch" main || refuse "$branch is not merged into main"
[ -z "$(git -C "$path" status --porcelain)" ] || refuse "$path is not clean (git status --porcelain)"
[ ! -e "$path/.env" ] && [ ! -L "$path/.env" ] || refuse "$path/.env exists: the job holds the cobalt_dev lock (L76)"

# ---- remove ----------------------------------------------------------------------------------
printf 'RUN: git -C %s worktree remove %s\n' "$REPO" "$path"
git -C "$REPO" worktree remove "$path" || refuse "worktree remove failed; the branch is kept"
printf 'RUN: git -C %s branch -d %s\n' "$REPO" "$branch"
git -C "$REPO" branch -d "$branch" || { printf 'job-clean: %s removed; branch -d %s FAILED\n' "$path" "$branch"; exit 1; }
printf 'job-clean: %s and %s removed\n' "$path" "$branch"
