#!/bin/sh
# preflight.sh <build|check> "<card>" — the MECHANICAL rows of BUILD-HUB.md / CHECK-HUB.md PREFLIGHT
# in ONE call, read-only, run from the job's worktree $WT/<WORKTREE> (card 19 worker-steps S2).
#
# Prints one row per rule, `rule · command · exit · output`; an output of more than one line follows
# its row, each line indented four spaces:
#   clock         date
#   status        `git status --short --branch` is exactly `## <BRANCH>`
#   head          `git log --oneline -1`: build — BASE, or a `wip(<JOB>):` commit; check — TIP, or
#                 docs-only commits above it (`git log --stat --format=%h <TIP>..HEAD`, its paths read
#                 with --name-only, every one under docs/)
#   diff          build: `git diff --stat <BASE>` (empty while HEAD is BASE)
#   main repo     build: `git -C $REPO log --oneline -1 <BRANCH>` is HEAD
#   env here      no .env in this worktree
#   env anywhere  no .env under $WT/*/
#   report        check: the build REPORT's last non-blank line starts
#                 `BUILT · job: <JOB> · tip: <TIP>` and carries `self-check: 3 of 3`
#   range         check: `git log --oneline <BASE>..<TIP>` (quoted)
# NOT here: the card's symbol greps, the lock probe, the house probes (judgment, gate.sh probe,
# house-probe.sh). Last line: `PREFLIGHT OK` (exit 0) or `FAILED PREFLIGHT: <the first rule that
# failed>` (exit 1). A bad call: `REFUSED: <reason>` on stderr, exit 1.
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_preflight.py only.

set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 2 ] || refuse "usage: preflight.sh <build|check> <card>"
kind=$1
card=$2
case "$kind" in
    build|check) ;;
    *) refuse "kind '$kind' is neither build nor check" ;;
esac
[ -f "$card" ] || refuse "no such card: $card"

field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}

job=$(field JOB)
branch=$(field BRANCH)
wt=$(field WORKTREE)
base=$(field BASE)
tip=$(field TIP)
report=$(field REPORT)
for k in JOB BRANCH WORKTREE BASE; do
    [ -n "$(field "$k")" ] || refuse "the card's $k is empty"
done
if [ "$kind" = check ]; then
    [ -n "$tip" ] || refuse "the card's TIP is empty (a check needs it)"
    [ -n "$report" ] || refuse "the card's REPORT is empty (a check needs it)"
fi
case "$wt" in
    ""|.*|*[!A-Za-z0-9._-]*) refuse "WORKTREE '$wt' is not one directory name [A-Za-z0-9._-]" ;;
esac
dir="$WT/$wt"
[ -d "$dir" ] || refuse "no such worktree: $dir"
cd "$dir" || refuse "cd failed: $dir"

failed=""

# row <rule> <command> <exit> <output> <ok: 0 or 1>
row() {
    n=$(printf '%s' "$4" | grep -c '')
    if [ -z "$4" ]; then
        res=nothing
    elif [ "$n" -le 1 ]; then
        res=$4
    else
        res="($n lines)"
    fi
    printf '%s · %s · %s · %s\n' "$1" "$2" "$3" "$res"
    [ "$n" -le 1 ] || printf '%s\n' "$4" | sed 's/^/    /'
    if [ "$5" -ne 0 ] && [ -z "$failed" ]; then
        failed=$1
    fi
}

out=$(date)
row clock "date" $? "$out" 0

out=$(git status --short --branch 2>&1)
rc=$?
ok=1
[ "$rc" -eq 0 ] && [ "$out" = "## $branch" ] && ok=0
row status "git status --short --branch" "$rc" "$out" "$ok"

head=$(git rev-parse --verify -q HEAD)
out=$(git log --oneline -1 2>&1)
rc=$?
ok=1
if [ "$kind" = build ]; then
    base_full=$(git rev-parse --verify -q "$base^{commit}")
    subject=$(git log -1 --format=%s)
    if [ -n "$base_full" ] && [ "$head" = "$base_full" ]; then
        ok=0
    else
        case "$subject" in
            "wip($job):"*) ok=0 ;;
        esac
    fi
    row head "git log --oneline -1" "$rc" "$out" "$ok"
else
    tip_full=$(git rev-parse --verify -q "$tip^{commit}")
    if [ -n "$tip_full" ] && [ "$head" = "$tip_full" ]; then
        ok=0
        row head "git log --oneline -1" "$rc" "$out" "$ok"
    else
        above=$(git log --stat --format=%h "$tip..HEAD" 2>&1)
        arc=$?
        if [ -n "$tip_full" ] && [ "$arc" -eq 0 ] && git merge-base --is-ancestor "$tip_full" HEAD; then
            others=$(git log --format= --name-only "$tip..HEAD" | grep -v '^$' | grep -v '^docs/')
            [ -n "$(git log --format=%h "$tip..HEAD")" ] && [ -z "$others" ] && ok=0
        fi
        row head "git log --oneline -1; git log --stat --format=%h $tip..HEAD" "$arc" "$out
$above" "$ok"
    fi
fi

if [ "$kind" = build ]; then
    out=$(git diff --stat "$base" 2>&1)
    rc=$?
    ok=1
    if [ "$rc" -eq 0 ]; then
        if [ -z "$out" ] || [ "$head" != "$(git rev-parse --verify -q "$base^{commit}")" ]; then
            ok=0
        fi
    fi
    row diff "git diff --stat $base" "$rc" "$out" "$ok"

    out=$(git -C "$REPO" log --oneline -1 "$branch" 2>&1)
    rc=$?
    ok=1
    [ "$rc" -eq 0 ] && [ "$(git -C "$REPO" rev-parse --verify -q "refs/heads/$branch")" = "$head" ] && ok=0
    row "main repo" "git -C $REPO log --oneline -1 $branch" "$rc" "$out" "$ok"
fi

if [ -e "$dir/.env" ]; then
    row "env here" "ls $dir/.env" 0 "$dir/.env" 1
else
    row "env here" "ls $dir/.env" 1 "No such file or directory" 0
fi

found=""
set +f
for f in "$WT"/*/.env; do
    [ -e "$f" ] && found="$found$f
"
done
set -f
found=$(printf '%s' "$found" | sed '/^$/d')
if [ -n "$found" ]; then
    row "env anywhere" "ls -la $WT/*/.env" 0 "$found" 1
else
    row "env anywhere" "ls -la $WT/*/.env" 1 "no matches found" 0
fi

if [ "$kind" = check ]; then
    if [ -f "$report" ]; then
        last=$(grep -v '^[[:space:]]*$' "$report" | tail -n 1)
        ok=1
        case "$last" in
            "BUILT · job: $job · tip: $tip"*"self-check: 3 of 3"*) ok=0 ;;
        esac
        row report "tail -n 3 \"$report\"" 0 "$last" "$ok"
    else
        row report "tail -n 3 \"$report\"" 1 "no such file: $report" 1
    fi
    out=$(git log --oneline "$base..$tip" 2>&1)
    rc=$?
    ok=1
    [ "$rc" -eq 0 ] && ok=0
    row range "git log --oneline $base..$tip" "$rc" "$out" "$ok"
fi

if [ -z "$failed" ]; then
    printf 'PREFLIGHT OK\n'
    exit 0
fi
printf 'FAILED PREFLIGHT: %s\n' "$failed"
exit 1
