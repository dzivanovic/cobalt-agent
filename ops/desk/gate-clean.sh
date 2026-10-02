#!/bin/sh
# gate-clean.sh "<deploy card>"
# Removes the gate worktree and gate branch of a deploy that FAILED before anything merged
# (card 18 desk-tools-b, row B2). It reads the card's JOB, BRANCH, WORKTREE, REPORT and TAG.
# It needs, each proven first (else REFUSED on stderr, exit 1, nothing removed):
#   - the WORKTREE a plain name: exactly $WT/<one directory name>, never agy-trial, never a
#     symlink, and registered with git as a worktree with BRANCH checked out;
#   - BRANCH a gate branch: deploy/<name>;
#   - REPORT under $REPORTS/deploy-*.md, present, its last non-blank line starting `FAILED`;
#   - no tag TAG and no tag pre-<JOB>;
#   - main not containing the gate branch's head, unless that head is itself on main's
#     first-parent line (the gate was cut there and nothing of it ever landed);
#   - no .env in the gate worktree, and no lock directory ($WT/.cobalt_dev.lock) it owns.
# Then `git -C $REPO worktree remove --force <gate worktree>` and `git -C $REPO branch -D <gate
# branch>`, each printed first as `RUN: …`; the last line `gate-clean: <worktree> and <branch> removed`.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).

set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
REPORTS="$REPO/docs/40 - DevDocs/reports"
LOCK="$WT/.cobalt_dev.lock"

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 1 ] || refuse "usage: gate-clean.sh \"<deploy card>\""
card=$1
[ -f "$card" ] || refuse "no such card: $card"

# field KEY -> the value of the first "KEY: value" line, trailing blanks cut (desk-launch.sh's)
field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}
job=$(field JOB)
branch=$(field BRANCH)
wt=$(field WORKTREE)
report=$(field REPORT)
tag=$(field TAG)

case "$job" in
    ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) refuse "JOB '$job' must be [a-z0-9-]" ;;
esac
case "$branch" in
    deploy/*) ;;
    *) refuse "BRANCH '$branch' is not a gate branch (deploy/<name>)" ;;
esac
case "$branch" in
    *[!A-Za-z0-9._/-]*|*..*) refuse "BRANCH '$branch' is not a plain branch name" ;;
esac
case "$tag" in
    ""|*[!A-Za-z0-9._-]*|-*) refuse "TAG '$tag' is not a plain tag name" ;;
esac

# ---- the worktree: exactly $WT/<one directory name>, a real directory, git's, on BRANCH -------
case "$wt" in
    ""|.*|*[!A-Za-z0-9._-]*) refuse "worktree '$wt' is outside the approved pattern $WT/<one directory name>" ;;
esac
[ "$wt" != "agy-trial" ] || refuse "worktree 'agy-trial' is the check hubs' scratch tree, never a gate"
path="$WT/$wt"
[ ! -L "$path" ] || refuse "$path is a symlink"
[ -d "$path" ] || refuse "no gate worktree at $path"
registered=$(git -C "$REPO" worktree list --porcelain | awk -v p="worktree $path" -v b="branch refs/heads/$branch" '
    $0 == p { on = 1; next }
    /^worktree / { on = 0 }
    on && $0 == b { print "yes" }')
[ "$registered" = "yes" ] || refuse "$path is not a worktree of $REPO with $branch checked out"

# ---- the report: FAILED --------------------------------------------------------------------
case "$report" in
    "$REPORTS"/deploy-*.md) ;;
    *) refuse "REPORT '$report' is not $REPORTS/deploy-<name>.md" ;;
esac
[ -f "$report" ] || refuse "the deploy report is missing: $report"
last=$(grep -v '^[[:space:]]*$' "$report" | tail -n 1)
case "$last" in
    FAILED*) ;;
    *) refuse "the deploy report does not end FAILED: $last" ;;
esac

# ---- nothing of the gate landed --------------------------------------------------------------
if git -C "$REPO" rev-parse --verify --quiet "refs/tags/$tag" >/dev/null; then
    refuse "tag $tag exists: the deploy got that far"
fi
if git -C "$REPO" rev-parse --verify --quiet "refs/tags/pre-$job" >/dev/null; then
    refuse "tag pre-$job exists: the deploy got that far"
fi
ghead=$(git -C "$REPO" rev-parse --verify --quiet "refs/heads/$branch^{commit}") || refuse "no branch $branch"
if git -C "$REPO" merge-base --is-ancestor "$ghead" main; then
    git -C "$REPO" rev-list --first-parent main | grep -q -x -F "$ghead" \
        || refuse "main contains the gate's head $ghead (merged from the gate): its commits are main's"
fi

# ---- the lock --------------------------------------------------------------------------------
[ ! -e "$path/.env" ] && [ ! -L "$path/.env" ] || refuse "$path/.env exists: the gate holds the cobalt_dev lock (L76)"
if [ -f "$LOCK/owner" ] && [ "$(sed -n '1p' "$LOCK/owner")" = "$wt" ]; then
    refuse "the lock directory $LOCK is owned by $wt"
fi

# ---- remove ----------------------------------------------------------------------------------
printf 'RUN: git -C %s worktree remove --force %s\n' "$REPO" "$path"
git -C "$REPO" worktree remove --force "$path" || refuse "worktree remove failed; the branch is kept"
printf 'RUN: git -C %s branch -D %s\n' "$REPO" "$branch"
git -C "$REPO" branch -D "$branch" || { printf 'gate-clean: %s removed; branch -D %s FAILED\n' "$path" "$branch"; exit 1; }
printf 'gate-clean: %s and %s removed\n' "$path" "$branch"
