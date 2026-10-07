#!/bin/sh
# job-clean.sh "<job card>"
# job-clean.sh salvage <worktree-name>
# Card mode: removes a landed job's worktree and branch (card 18 desk-tools-b, row B2). It reads the card's
# BRANCH and WORKTREE. It needs, each proven first (else REFUSED on stderr, exit 1, nothing removed):
#   - the WORKTREE a plain name: exactly $WT/<one directory name>, never agy-trial, never a
#     symlink, and registered with git as a worktree with BRANCH checked out;
#   - `git -C $REPO merge-base --is-ancestor <BRANCH> main` to hold (the job landed);
#   - the worktree clean (`git status --porcelain` empty) and holding no .env.
# Then `git -C $REPO worktree remove <worktree>` and `git -C $REPO branch -d <branch>` (never
# forced), each printed first as `RUN: …`; the last line `job-clean: <worktree> and <branch> removed`.
# Salvage mode (worktree-salvage, R613): a stale or broken tree is inspected, its work saved, then removed.
#   - The name passes the card mode's checks and must be a registered worktree of $REPO, not on main.
#   - INSPECT report on stdout, one fact per line, before any refusal or change: worktree, branch
#     (or detached), merged into main, ahead of main (and each commit), status lines, .env, locked,
#     git operation in progress, ignored paths (ignored files are not saved).
#   - Then REFUSED (exit 1, nothing changed) when: .env is there (the cobalt_dev lock, L76); the tree is
#     locked; a rebase, merge, cherry-pick, revert or bisect is in progress; an index entry is marked
#     skip-worktree or assume-unchanged (status cannot see its edits); the wip branch below already
#     exists or is not a valid branch name. Untracked files count even when the config hides them.
#   - A dirty tree, or a detached HEAD not on main: `switch -c wip/<worktree>-salvage-<YYYYMMDD>` (it carries
#     the changes), then `add -A` and `commit` when the tree is dirty; then `SALVAGED: <wip> <n> files <m>
#     commits ahead`. A clean tree on an unmerged branch prints `SALVAGED: <branch> 0 files <m> commits ahead`.
#   - Then `git -C $REPO worktree remove <worktree>`; the tree's branch is deleted with `branch -d` only when
#     merged into main, else kept; a wip branch is always kept. Never forced. The last line:
#     `job-clean salvage: removed <worktree>; deleted <branch or none>; kept <branches or none>`.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).

export LC_ALL=C
set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

# plain_worktree NAME -> path="$WT/NAME", refused unless a plain name of a real, non-symlink directory
plain_worktree() {
    case "$1" in
        ""|.*|*[!A-Za-z0-9._-]*) refuse "worktree '$1' is outside the approved pattern $WT/<one directory name>" ;;
    esac
    [ "$1" != "agy-trial" ] || refuse "worktree 'agy-trial' is the check hubs' scratch tree, never a job's"
    path="$WT/$1"
    [ ! -L "$path" ] || refuse "$path is a symlink"
    [ -d "$path" ] || refuse "no job worktree at $path"
}

salvage() {
    name=$1
    plain_worktree "$name"

    # ---- git's stanza for exactly this path ---------------------------------------------------
    stanza=$(git -C "$REPO" worktree list --porcelain | awk -v p="worktree $path" '
        $0 == p { on = 1; print; next }
        /^worktree / || $0 == "" { on = 0 }
        on { print }')
    [ -n "$stanza" ] || refuse "$path is not a registered worktree of $REPO"
    b=$(printf '%s\n' "$stanza" | sed -n 's|^branch refs/heads/||p')
    detached=no
    if printf '%s\n' "$stanza" | grep -q '^detached$'; then detached=yes; fi
    locked=no
    if printf '%s\n' "$stanza" | grep -q -E '^locked( |$)'; then locked=yes; fi
    [ -n "$b" ] || [ "$detached" = yes ] || refuse "$path has neither a branch nor a detached HEAD"
    [ "$b" != "main" ] || refuse "$path has main checked out"
    head=$(git -C "$path" rev-parse --verify -q HEAD) || refuse "$path has no HEAD commit"

    # ---- inspect: every fact read before any refusal below and before any change --------------
    git -C "$REPO" merge-base --is-ancestor "$head" main
    case $? in
        0) merged=yes ;;
        1) merged=no ;;
        *) refuse "merge-base failed for $path" ;;
    esac
    ahead=$(git -C "$path" rev-list --count main..HEAD) || refuse "rev-list failed for $path"
    commits=$(git -C "$path" log --format='%H %s' main..HEAD) || refuse "log failed for $path"
    # -unormal: a status.showUntrackedFiles=no config must not hide an untracked file (check O1)
    status=$(git -C "$path" status --porcelain -unormal) || refuse "status failed for $path"
    n=0
    [ -z "$status" ] || n=$(printf '%s\n' "$status" | wc -l | tr -d ' ')
    ignored=$(git -C "$path" status --porcelain --ignored) || refuse "status --ignored failed for $path"
    ignored=$(printf '%s\n' "$ignored" | awk '/^!! / { k++ } END { print k + 0 }')
    # index entries status never shows: skip-worktree (S) or assume-unchanged (lower case) (check O2)
    hidden=$(git -C "$path" ls-files -v) || refuse "ls-files failed for $path"
    hidden=$(printf '%s\n' "$hidden" | awk '/^(S|[a-z]) / { k++ } END { print k + 0 }')
    env=no
    if [ -e "$path/.env" ] || [ -L "$path/.env" ]; then env=yes; fi
    ops=""
    for m in rebase-merge rebase-apply MERGE_HEAD CHERRY_PICK_HEAD REVERT_HEAD BISECT_LOG; do
        at=$(git -C "$path" rev-parse --git-path "$m") || refuse "rev-parse --git-path failed for $path"
        case $at in /*) ;; *) at="$path/$at" ;; esac
        if [ -e "$at" ]; then ops="${ops:+$ops }$m"; fi
    done

    printf 'INSPECT: worktree %s\n' "$path"
    if [ "$detached" = yes ]; then
        printf 'INSPECT: branch (detached at %.8s)\n' "$head"
    else
        printf 'INSPECT: branch %s\n' "$b"
    fi
    printf 'INSPECT: merged into main: %s\n' "$merged"
    printf 'INSPECT: ahead of main: %s\n' "$ahead"
    [ -z "$commits" ] || printf '%s\n' "$commits" | awk '{ printf "INSPECT:   %s %s\n", substr($1, 1, 8), substr($0, length($1) + 2) }'
    printf 'INSPECT: status: %s lines\n' "$n"
    [ -z "$status" ] || printf '%s\n' "$status" | sed 's/^/INSPECT:   /'
    printf 'INSPECT: .env: %s\n' "$env"
    printf 'INSPECT: locked: %s\n' "$locked"
    printf 'INSPECT: git operation in progress: %s\n' "${ops:-none}"
    printf 'INSPECT: ignored: %s paths, never saved\n' "$ignored"

    # ---- refusals: nothing has changed yet ----------------------------------------------------
    [ "$env" = no ] || refuse "$path/.env exists: the job holds the cobalt_dev lock (L76)"
    [ "$locked" = no ] || refuse "$path is locked (git worktree lock)"
    [ -z "$ops" ] || refuse "$path has a git operation in progress: $ops"
    [ "$hidden" -eq 0 ] || refuse "$path has $hidden index entries hidden from status (skip-worktree or assume-unchanged)"
    wip=""
    if [ "$n" -gt 0 ] || { [ "$detached" = yes ] && [ "$merged" = no ]; }; then
        D=$(date +%Y%m%d)
        wip="wip/$name-salvage-$D"
        git -C "$REPO" check-ref-format --branch "$wip" >/dev/null 2>&1 || refuse "$wip is not a valid branch name"
        if git -C "$REPO" show-ref --verify --quiet "refs/heads/$wip"; then refuse "$wip already exists"; fi
    fi

    # ---- salvage: the work goes to the wip branch before anything is removed ------------------
    if [ -n "$wip" ]; then
        if [ "$detached" = yes ]; then on="(detached at $(printf '%.8s' "$head"))"; else on=$b; fi
        printf 'RUN: git -C %s switch -c %s\n' "$path" "$wip"
        git -C "$path" switch -c "$wip" || refuse "salvage stopped at switch; nothing removed; the tree is on $on"
        if [ "$n" -gt 0 ]; then
            printf 'RUN: git -C %s add -A\n' "$path"
            git -C "$path" add -A || refuse "salvage stopped at add; nothing removed; the tree is on $wip"
            msg="wip: salvage $name $D (job-clean.sh salvage)"
            printf 'RUN: git -C %s commit -q -m "%s"\n' "$path" "$msg"
            git -C "$path" commit -q -m "$msg" || refuse "salvage stopped at commit; nothing removed; the tree is on $wip"
        fi
        printf 'SALVAGED: %s %s files %s commits ahead\n' "$wip" "$n" "$ahead"
    elif [ "$merged" = no ]; then
        printf 'SALVAGED: %s 0 files %s commits ahead\n' "$b" "$ahead"
    fi

    # ---- remove: the tree, then its branch only when merged; a wip branch is always kept -------
    printf 'RUN: git -C %s worktree remove %s\n' "$REPO" "$path"
    git -C "$REPO" worktree remove "$path" || refuse "worktree remove failed; every branch is kept"
    deleted=none
    kept=""
    failed=no
    if [ -n "$b" ]; then
        if git -C "$REPO" merge-base --is-ancestor "refs/heads/$b" main; then
            printf 'RUN: git -C %s branch -d %s\n' "$REPO" "$b"
            if git -C "$REPO" branch -d "$b" >&2; then
                deleted=$b
            else
                # the last line still names every branch kept (check A1)
                printf 'kept: %s (branch -d failed)\n' "$b"
                printf 'job-clean salvage: branch -d %s failed; it is kept\n' "$b" >&2
                kept=$b
                failed=yes
            fi
        else
            printf 'kept: %s (not merged)\n' "$b"
            kept=$b
        fi
    fi
    if [ -n "$wip" ]; then
        printf 'kept: %s (salvage)\n' "$wip"
        kept="${kept:+$kept }$wip"
    fi
    printf 'job-clean salvage: removed %s; deleted %s; kept %s\n' "$path" "$deleted" "${kept:-none}"
    [ "$failed" = no ] || exit 1
    exit 0
}

if [ "$#" -eq 2 ] && [ "$1" = "salvage" ]; then
    salvage "$2"
fi
[ "$#" -eq 1 ] || refuse "usage: job-clean.sh \"<job card>\" | job-clean.sh salvage <worktree-name>"
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
plain_worktree "$wt"
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
