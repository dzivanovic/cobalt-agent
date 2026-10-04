#!/bin/sh
# stage-set.sh "<card>" "<dest folder>" — a check's whole reading set staged in ONE call for a house
# that reads only inside agy-trial (CHECK-HUB.md `## 1` (1)–(3); card 19 worker-steps S4).
#
# The dest must sit under $WT/agy-trial/scratch/ and be empty or absent. Everything is read from
# git, never from the working files:
#   diff.md                 the heading line `## 1` (1) gives, then `git log -p <BASE>..<TIP> -- .
#                           ":(exclude)docs"` run in the job worktree $WT/<WORKTREE>
#   rulings.md              for each `<date> R<n>` of RULINGS, its `grep -n "^| R<n> " "<cto-<date>.md>"`
#                           command line, then what it prints (RULINGS: none → that line alone)
#   files/<card name>       the card at HEAD of $REPO
#   files/<report name>     the build REPORT at HEAD of the job worktree (the report is committed
#                           above TIP, so TIP does not hold it)
#   files/wt/<path>         every path of `git diff --name-only <BASE>..<TIP>` that exists at TIP,
#                           written from `git show <TIP>:<path>`
# Every copied file is proved: `git hash-object --no-filters <copy>` equals the blob id it came from.
# Prints `<bytes> <path>` per file, then `STAGED <n> files · <total bytes> · commits <k>` (k = the
# `^commit ` lines of diff.md). It never writes a .env: a .env path in the range is refused before
# anything is written. Any mismatch or failed write removes what it wrote, leaves the dest empty
# (or absent, if it was), and exits 1. A bad call: `REFUSED: <reason>` on stderr, exit 1.
# The files a card's `## READ` names by symbol are not derivable; the hub adds those with
# stage-copy.sh.
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_stage_set.py only.

export LC_ALL=C
set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
SCRATCH="$WT/agy-trial/scratch"

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 2 ] || refuse "usage: stage-set.sh <card> <dest folder>"
card=$1
dest=$2
case "$dest" in
    *..*|*/./*|*/.) refuse "the dest path holds '..' or '.': $dest" ;;
    "$SCRATCH"/?*) ;;
    *) refuse "the dest is not under $SCRATCH/: $dest" ;;
esac
dest=${dest%/}
[ -f "$card" ] || refuse "no such card: $card"
case "$card" in
    "$REPO"/*) ;;
    *) refuse "the card is not under $REPO: $card" ;;
esac
case "$card" in
    *..*) refuse "the card path holds '..'" ;;
esac
card_rel=${card#"$REPO"/}

field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}
for k in WORKTREE BASE TIP REPORT RULINGS; do
    [ -n "$(field "$k")" ] || refuse "the card's $k is empty"
done
wt=$(field WORKTREE)
base=$(field BASE)
tip=$(field TIP)
report=$(field REPORT)
rulings=$(field RULINGS)
case "$wt" in
    .*|*[!A-Za-z0-9._-]*) refuse "WORKTREE '$wt' is not one directory name [A-Za-z0-9._-]" ;;
esac
job="$WT/$wt"
[ -d "$job" ] || refuse "no such worktree: $job"
case "$report" in
    "$job"/*) ;;
    *) refuse "the REPORT is not inside the job worktree $job: $report" ;;
esac
report_rel=${report#"$job"/}
git -C "$job" rev-parse --verify -q "$base^{commit}" >/dev/null || refuse "BASE '$base' is not a commit"
git -C "$job" rev-parse --verify -q "$tip^{commit}" >/dev/null || refuse "TIP '$tip' is not a commit"

if [ -e "$dest" ]; then
    [ -d "$dest" ] || refuse "the dest is not a folder: $dest"
    [ -z "$(ls -A "$dest")" ] || refuse "the dest is not empty: $dest"
    existed=1
else
    existed=""
fi

# every path the range touches, in any commit: none may be a .env, none may need quoting
touched=$(git -C "$job" -c core.quotepath=off log --format= --name-only "$base..$tip") || refuse "git log failed on $base..$tip"
printf '%s\n' "$touched" | while IFS= read -r p; do
    case "$p" in
        .env|.env.*|*/.env|*/.env.*) printf 'REFUSED: a .env path in the range: %s\n' "$p" >&2; exit 1 ;;
        '"'*) printf 'REFUSED: a path git must quote: %s\n' "$p" >&2; exit 1 ;;
    esac
done || exit 1
paths=$(git -C "$job" -c core.quotepath=off diff --name-only "$base..$tip") || refuse "git diff failed on $base..$tip"

fail() {
    printf 'FAILED: %s\n' "$*" >&2
    rm -rf "$dest"
    [ -z "$existed" ] || mkdir "$dest"
    exit 1
}

mkdir -p "$dest/files/wt" || fail "mkdir failed: $dest"

# copy <git dir> <rev:path> <dest file>: written from git show, proved by hash-object
copy() {
    mkdir -p "$(dirname "$3")" || fail "mkdir failed for $3"
    git -C "$1" show "$2" > "$3" || fail "git show $2 failed"
    want=$(git -C "$1" rev-parse "$2") || fail "git rev-parse $2 failed"
    got=$(git -C "$1" hash-object --no-filters "$3") || fail "git hash-object failed on $3"
    [ "$got" = "$want" ] || fail "$3 differs from $2 ($got, not $want)"
}

{
    printf '=== git log -p %s..%s -- . ":(exclude)docs" (in %s) ===\n' "$base" "$tip" "$job"
    git -C "$job" log -p "$base..$tip" -- . ":(exclude)docs"
} > "$dest/diff.md" || fail "git log -p failed"

{
    if [ "$rulings" = none ]; then
        printf 'RULINGS: none\n'
    else
        date=""
        for t in $(printf '%s\n' "$rulings" | sed -e 's/·/ /g' -e 's/[,;]/ /g'); do
            case "$t" in
                20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) date=$t ;;
                R[0-9]*)
                    file="$REPO/docs/40 - DevDocs/reports/cto-$date.md"
                    printf 'grep -n "^| %s " "%s"\n' "$t" "$file"
                    grep -n "^| $t " "$file"
                    printf '\n'
                    ;;
                *) printf 'unreadable RULINGS token: %s\n' "$t" ;;
            esac
        done
    fi
} > "$dest/rulings.md"

copy "$REPO" "HEAD:$card_rel" "$dest/files/$(basename "$card")"
copy "$job" "HEAD:$report_rel" "$dest/files/$(basename "$report")"

printf '%s\n' "$paths" | {
    while IFS= read -r p; do
        [ -n "$p" ] || continue
        git -C "$job" cat-file -e "$tip:$p" 2>/dev/null || continue
        copy "$job" "$tip:$p" "$dest/files/wt/$p"
    done
} || fail "a copy under files/wt failed"

n=0
total=0
listing=$(cd "$dest" && find . -type f | sed 's|^\./||' | LC_ALL=C sort)
while IFS= read -r f; do
    [ -n "$f" ] || continue
    b=$(wc -c < "$dest/$f" | tr -d ' ')
    printf '%s %s\n' "$b" "$dest/$f"
    n=$((n + 1))
    total=$((total + b))
done <<EOF
$listing
EOF
k=$(grep -c '^commit ' "$dest/diff.md")
printf 'STAGED %s files · %s bytes · commits %s\n' "$n" "$total" "$k"
