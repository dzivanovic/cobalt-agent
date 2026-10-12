#!/bin/sh
# scratch-clean.sh "<path>"
# Removes ONE untracked or ignored path (a file, or a directory with all below it) inside an agent
# workspace (card 2026-10-12/389 cleanup-class, row C1; his 2026-10-12 R1138 part 1, K1; LAWS L81).
# Every test below is read before anything is removed (else REFUSED on stderr, exit 1, nothing removed):
#   (1) exactly one argument;
#   (2) absolute, no newline, no `..` component;
#   (3) it exists (a dangling link counts as there, then fails (4));
#   (4) no symlink hop: `realpath` of the path equals the path byte for byte (a link, a link
#       directory on the way, a `.` component, a doubled or trailing `/`: refused);
#   (5) under one root, strictly below it:
#       (a) $WT/<name>/… with <name> a plain directory name, never agy-trial, $WT/<name> not a
#           symlink and registered as exactly `worktree $WT/<name>` in `git worktree list
#           --porcelain` of $REPO; never $WT/<name> itself;
#       (b) $CLAUDE_JOB_DIR/tmp/… with CLAUDE_JOB_DIR exactly $JOBS/<plain name> and its tmp a real
#           directory; never the tmp directory itself;
#   (6) never .git: no component named .git in any case, no .git entry anywhere below a directory;
#   (7) never .env (the cobalt_dev lock, L76): no component that names .env as bare-guard.py
#       is_env reads it (any case, a glob name matching .env, a name holding a brace), no such
#       entry below a directory;
#   (8) git proves it: root (a) the parent's `rev-parse --show-toplevel` is $WT/<name> (no nested
#       repo), `ls-files --error-unmatch` fails (nothing tracked at or below it)
#       and `status --porcelain --ignored -unormal` prints lines, every one `?? ` or `!! `;
#       root (b) the parent is not inside a git work tree.
# Then `RUN: rm -rf -- <path>` first, the one removal, a proof the path is gone, and the last line
# `scratch-clean: removed <path>`, exit 0.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default
# /Users/cobalt/cobalt-wt), COBALT_JOBS_ROOT (default /Users/cobalt/.claude/jobs).

export LC_ALL=C
set -u
unset GIT_DIR GIT_WORK_TREE GIT_INDEX_FILE GIT_COMMON_DIR

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
JOBS=${COBALT_JOBS_ROOT:-/Users/cobalt/.claude/jobs}
NL='
'

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

# plain NAME -> true when NAME is one plain directory name (job-clean.sh plain_worktree's pattern)
plain() {
    case "$1" in
        ""|.*|*[!A-Za-z0-9._-]*) return 1 ;;
    esac
    return 0
}

# forbidden NAME -> prints `.git` or `.env` when NAME is one, in any case (is_env: a dot name
# that, read as a glob, matches .env; a name holding a brace may expand to .env, as is_env
# brace-expands it: refused as .env, check G1)
forbidden() {
    lc=$(printf '%s' "$1" | tr 'A-Z' 'a-z')
    [ "$lc" != ".git" ] || { printf '.git'; return 0; }
    case "$lc" in
        *[{}]*) printf '.env'; return 0 ;;
    esac
    case "$lc" in
        .*) case ".env" in $lc) printf '.env'; return 0 ;; esac ;;
    esac
    return 0
}

# ---- (1) one argument, (2) its shape ---------------------------------------------------------
[ "$#" -eq 1 ] || refuse 'usage: scratch-clean.sh "<path>"'
p=$1
case "$p" in
    *"$NL"*) refuse "the path holds a newline" ;;
esac
case "$p" in
    /*) ;;
    *) refuse "'$p' is not an absolute path" ;;
esac
case "$p/" in
    */../*) refuse "$p has a .. component" ;;
esac

# ---- (3) it exists, (4) no symlink hop ---------------------------------------------------------
[ -e "$p" ] || [ -L "$p" ] || refuse "$p does not exist"
real=$(realpath -- "$p" 2>/dev/null) || refuse "$p does not resolve (a dangling link)"
[ "$real" = "$p" ] || refuse "$p is not its own realpath ($real): a link, a link on the way, a . or an extra /"

# ---- (5) under one root, strictly below it ----------------------------------------------------
root=""
case "$p" in
    "$WT"/*)
        rest=${p#"$WT"/}
        name=${rest%%/*}
        [ "$name" != "$rest" ] || refuse "$p is a worktree itself or $WT itself, never a scratch path"
        rel=${rest#*/}
        plain "$name" || refuse "$WT/$name is outside the approved pattern $WT/<one directory name>"
        [ "$name" != "agy-trial" ] || refuse "agy-trial is the check hubs' scratch tree, never cleaned here"
        tree="$WT/$name"
        [ ! -L "$tree" ] || refuse "$tree is a symlink"
        [ -d "$tree" ] || refuse "no worktree at $tree"
        list=$(git -C "$REPO" worktree list --porcelain 2>/dev/null) || refuse "git worktree list failed for $REPO"
        printf '%s\n' "$list" | grep -q -x -F -- "worktree $tree" || refuse "$tree is not a registered worktree of $REPO"
        root=wt
        ;;
esac
if [ -z "$root" ]; then
    jd=${CLAUDE_JOB_DIR-}
    [ -n "$jd" ] || refuse "$p is outside $WT/<worktree> and CLAUDE_JOB_DIR is unset"
    case "$jd" in
        "$JOBS"/*) ;;
        *) refuse "$p is outside $WT/<worktree>, and CLAUDE_JOB_DIR '$jd' is not $JOBS/<one name>" ;;
    esac
    plain "${jd#"$JOBS"/}" || refuse "CLAUDE_JOB_DIR '$jd' is not $JOBS/<one plain name>"
    [ ! -L "$jd" ] && [ -d "$jd" ] || refuse "CLAUDE_JOB_DIR $jd is not a real directory"
    [ ! -L "$jd/tmp" ] && [ -d "$jd/tmp" ] || refuse "$jd/tmp is not a real directory"
    case "$p" in
        "$jd/tmp"/*) ;;
        *) refuse "$p is outside $WT/<worktree> and $jd/tmp/" ;;
    esac
    root=job
fi

# ---- (6) never .git, (7) never .env: each component, then each entry below ---------------------
set -f
old=$IFS
IFS=/
for c in $p; do
    hit=$(forbidden "$c")
    [ -z "$hit" ] || { IFS=$old; refuse "$p names $hit"; }
done
IFS=$old
if [ -d "$p" ]; then
    below=$(find "$p" -name '.*' -print 2>/dev/null) || refuse "find failed under $p"
    IFS=$NL
    for f in $below; do
        hit=$(forbidden "${f##*/}")
        [ -z "$hit" ] || { IFS=$old; refuse "$p holds $hit below it: $f"; }
    done
    IFS=$old
fi
set +f

# ---- (8) git proves it ---------------------------------------------------------------------------
if [ "$root" = wt ]; then
    # a nested repo's work tree is never the worktree's, ignored or not (check O4)
    top=$(git -C "${p%/*}" rev-parse --show-toplevel 2>/dev/null)
    [ "$top" = "$tree" ] || refuse "$p sits inside another git work tree ($top), not $tree"
    if git --literal-pathspecs -C "$tree" ls-files --error-unmatch -- "$rel" >/dev/null 2>&1; then
        refuse "$p is tracked, or holds a tracked file"
    fi
    st=$(git --literal-pathspecs -C "$tree" status --porcelain --ignored -unormal -- "$rel" 2>/dev/null) \
        || refuse "git status failed for $p"
    [ -n "$st" ] || refuse "git shows nothing untracked or ignored at $p"
    bad=$(printf '%s\n' "$st" | grep -v -e '^?? ' -e '^!! ')
    [ -z "$bad" ] || refuse "git status shows $p is not wholly untracked or ignored"
else
    inside=$(git -C "${p%/*}" rev-parse --is-inside-work-tree 2>/dev/null)
    [ "$inside" != "true" ] || refuse "$p sits inside a git work tree"
fi

# ---- remove --------------------------------------------------------------------------------------
printf 'RUN: rm -rf -- %s\n' "$p"
rm -rf -- "$p" 2>/dev/null
[ ! -e "$p" ] && [ ! -L "$p" ] || refuse "rm left $p"
printf 'scratch-clean: removed %s\n' "$p"
exit 0
