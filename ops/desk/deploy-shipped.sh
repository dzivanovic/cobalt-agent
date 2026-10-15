#!/bin/sh
# deploy-shipped.sh "<card>"                  the paths the deploy of <card> ships
# deploy-shipped.sh --job <JOB>               the same; the card found on main by its JOB
# deploy-shipped.sh --moved <rev> "<card>"    those of them that moved on main since <rev>
# deploy-shipped.sh --moved <rev> --job <JOB>
# The shipped paths (his R1471, card 546), one per line, sorted, unique: every file
# `git diff --name-only --no-renames main...<head>` lists over every head of the card's TIP: line,
# plus docs/40 - DevDocs/prompts/DEPLOY-HUB.md (the live hub reads it). --moved prints those of
# them that `git diff --name-only --no-renames <rev> main -- <path>` lists; nothing when none.
# --job: the card is the ONE file of `git grep -l -e "^JOB: <JOB>$" main -- "docs/40 - DevDocs/prompts"`
# that also holds the line `BASE: main` (a build or check card's BASE is 8 hex); <JOB> is [A-Za-z0-9_-].
# Refused: no card, or more than one, for --job; a card path outside prompts/; no TIP: line or no
# head on it; a TIP head that is not 8 hex or does not resolve; a --moved rev that does not resolve.
# A refusal: "REFUSED: <reason>" on stderr, exit 1, nothing on stdout (the pre-commit deploy guard
# reads it as "freeze all"). Read only: no git write (GIT_OPTIONAL_LOCKS=0).
# REPO = ${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
export LC_ALL=C
set -f
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
GIT_OPTIONAL_LOCKS=0
export GIT_OPTIONAL_LOCKS
PROMPTS="docs/40 - DevDocs/prompts"
HUB="$PROMPTS/DEPLOY-HUB.md"
nl='
'
refuse() { echo "REFUSED: $1" >&2; exit 1; }
g() { git -C "$REPO" -c core.quotePath=false --literal-pathspecs "$@"; }

rev=""
if [ "${1:-}" = "--moved" ]; then
    [ $# -ge 2 ] && [ -n "$2" ] || refuse 'usage: deploy-shipped.sh --moved <rev> "<card>" | --moved <rev> --job <JOB>'
    rev=$2
    shift 2
    g rev-parse --verify --quiet "$rev^{commit}" >/dev/null || refuse "the --moved rev does not resolve: $rev"
fi
g rev-parse --verify --quiet "refs/heads/main^{commit}" >/dev/null || refuse "no branch main in $REPO"

if [ "${1:-}" = "--job" ]; then
    [ $# -eq 2 ] && [ -n "$2" ] || refuse 'usage: deploy-shipped.sh --job <JOB>'
    job=$2
    case "$job" in
        *[!A-Za-z0-9_-]*) refuse "a JOB outside [A-Za-z0-9_-]: $job" ;;
    esac
    # git grep has no -x: the whole-line match is the anchored pattern (the JOB holds no regex char)
    found=$(g grep -l -e "^JOB: $job\$" main -- "$PROMPTS" 2>/dev/null)
    [ $? -le 1 ] || refuse "git grep for JOB: $job failed"
    card=""
    n=0
    while IFS= read -r hit; do
        [ -n "$hit" ] || continue
        path=${hit#main:}
        if g grep -q -e '^BASE: main$' main -- "$path" 2>/dev/null; then
            card=$path
            n=$((n + 1))
        fi
    done <<EOF
$found
EOF
    [ "$n" -ge 1 ] || refuse "no deploy card on main with JOB: $job and BASE: main"
    [ "$n" -eq 1 ] || refuse "$n deploy cards on main with JOB: $job and BASE: main"
    text=$(g show "main:$card" 2>/dev/null) || refuse "cannot read main:$card"
else
    [ $# -eq 1 ] && [ -n "$1" ] || refuse 'usage: deploy-shipped.sh [--moved <rev>] "<card>" | [--moved <rev>] --job <JOB>'
    [ -f "$1" ] || refuse "no card file: $1"
    root=$(cd "$REPO/$PROMPTS" 2>/dev/null && pwd -P) || refuse "no $PROMPTS in $REPO"
    dir=$(cd "$(dirname -- "$1")" 2>/dev/null && pwd -P) || refuse "no card file: $1"
    case "$dir/" in
        "$root"/*) ;;
        *) refuse "a card path outside $PROMPTS: $1" ;;
    esac
    text=$(cat -- "$1") || refuse "cannot read $1"
fi

[ "$(printf '%s\n' "$text" | grep -c '^TIP:')" -eq 1 ] || refuse "the card holds no single TIP: line"
heads=$(printf '%s\n' "$text" | sed -n 's/^TIP:[[:space:]]*//p')
[ -n "$heads" ] || refuse "no head on the card's TIP: line"

out=""
for h in $heads; do
    case "$h" in
        *[!0-9a-f]*) refuse "a TIP head that is not 8 hex: $h" ;;
    esac
    [ ${#h} -eq 8 ] || refuse "a TIP head that is not 8 hex: $h"
    g rev-parse --verify --quiet "$h^{commit}" >/dev/null || refuse "a TIP head that does not resolve: $h"
    d=$(g diff --name-only --no-renames "main...$h" 2>/dev/null) || refuse "git diff main...$h failed"
    out="$out$d$nl"
done
list=$(printf '%s%s\n' "$out" "$HUB" | sed '/^$/d' | sort -u)

if [ -z "$rev" ]; then
    printf '%s\n' "$list"
    exit 0
fi
moved=""
while IFS= read -r p; do
    [ -n "$p" ] || continue
    m=$(g diff --name-only --no-renames "$rev" main -- "$p" 2>/dev/null) || refuse "git diff $rev main -- $p failed"
    [ -z "$m" ] || moved="$moved$m$nl"
done <<EOF
$list
EOF
[ -z "$moved" ] || printf '%s' "$moved" | sort -u
exit 0
