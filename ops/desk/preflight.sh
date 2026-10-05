#!/bin/sh
# preflight.sh <build|check> "<card>" — the MECHANICAL rows of BUILD-HUB.md / CHECK-HUB.md PREFLIGHT
# in ONE call, read-only, run from the job's worktree $WT/<WORKTREE> (card 19 worker-steps S2).
#
# Prints one row per rule, `rule · command · exit · output`; an output of more than one line follows
# its row, each line indented four spaces:
#   clock         date
#   status        `git status --short --branch` is exactly `## <BRANCH>`, or that line and ONE
#                 `?? <path>` line whose path is the card's REPORT (a check: REPORT or CHECK
#                 REPORT) inside this worktree, printing `status: clean but the report
#                 (untracked, expected)` (card 2026-10-03/03c M1); any other line fails
#   head          `git log --oneline -1`: build — BASE, or a `wip(<JOB>):` commit; check — TIP, or
#                 docs-only commits above it (`git log --stat --format=%h <TIP>..HEAD`, its paths read
#                 with --name-only, every one under docs/); a PASS-2 check (CHECK REPORT's last
#                 non-blank line starts `CHECK DONE · job: <JOB> · pass: 1` and carries
#                 `house B: needed`) reads that line's `tip:` in place of TIP (card 20 F2)
#   diff          build: `git diff --stat <BASE>` (empty while HEAD is BASE)
#   main repo     build: `git -C $REPO log --oneline -1 <BRANCH>` is HEAD
#   env here      no .env in this worktree
#   env anywhere  information only: `siblings holding .env: <paths, or none>` (another worktree's
#                 .env is a held lock, which the take waits for); never fails the PREFLIGHT
#   report        check: the build REPORT's last non-blank line starts
#                 `BUILT · job: <JOB> · tip: <TIP>` and carries `self-check: <k> of 3` (k 0-3);
#                 k below 3 also prints `report: self-check <k> of 3 (recorded)` (card 20 F1)
#   range         check: `git log --oneline <BASE>..<TIP>` (quoted)
# NOT here: the card's symbol greps, the lock probe, the house probes (judgment, gate.sh probe,
# house-probe.sh). Last line: `PREFLIGHT OK` (exit 0) or `FAILED PREFLIGHT: <the first rule that
# failed>` (exit 1). A bad call: `REFUSED: <reason>` on stderr, exit 1.
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_preflight.py only.

export LC_ALL=C
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
expected=""
[ "$rc" -eq 0 ] && [ "$out" = "## $branch" ] && ok=0
# card 03c M1: the card's own report (a check's: REPORT or CHECK REPORT), untracked, as the ONE
# line under the branch line — the hub's first Write makes it before PREFLIGHT. Nothing else.
if [ "$ok" -ne 0 ] && [ "$rc" -eq 0 ] && [ "$(printf '%s\n' "$out" | sed -n '1p')" = "## $branch" ] \
    && [ "$(printf '%s\n' "$out" | grep -c '')" -eq 2 ]; then
    other=$(printf '%s\n' "$out" | sed -n '2p')
    own="$report"
    [ "$kind" != check ] || own="$own
$(field "CHECK REPORT")"
    while IFS= read -r r; do
        rel=""
        case "$r" in
            "$dir"/*) rel=${r#"$dir"/} ;;
            "$REPO"/*) rel=${r#"$REPO"/} ;;
        esac
        [ -n "$rel" ] || continue
        if [ "$other" = "?? $rel" ] || [ "$other" = "?? \"$rel\"" ]; then
            ok=0
            expected=1
        fi
    done <<OWN
$own
OWN
fi
row status "git status --short --branch" "$rc" "$out" "$ok"
[ -z "$expected" ] || printf 'status: clean but the report (untracked, expected)\n'

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
    # card 20 F2 (CHECK-HUB.md:120): on a PASS-2 launch the head reference is pass 1's `tip:`, read
    # from CHECK REPORT's last non-blank line when it starts `CHECK DONE · job: <JOB> · pass: 1` and
    # carries `house B: needed`; any other state keeps the card's TIP.
    ref=$tip
    check_report=$(field "CHECK REPORT")
    if [ -n "$check_report" ] && [ -f "$check_report" ]; then
        pass1=$(grep -v '^[[:space:]]*$' "$check_report" | tail -n 1)
        case "$pass1" in
            "CHECK DONE · job: $job · pass: 1 ·"*"house B: needed"*)
                ref=""
                case "$pass1" in
                    *"· tip: "*)
                        ref=${pass1#*· tip: }
                        ref=${ref%% ·*}
                        ;;
                esac
                case "$ref" in
                    ""|*[!0-9a-f]*) ref="" ;;
                esac
                ;;
        esac
    fi
    tip_full=""
    [ -z "$ref" ] || tip_full=$(git rev-parse --verify -q "$ref^{commit}")
    if [ -n "$tip_full" ] && [ "$head" = "$tip_full" ]; then
        ok=0
        row head "git log --oneline -1" "$rc" "$out" "$ok"
    else
        above=$(git log --stat --format=%h "$ref..HEAD" 2>&1)
        arc=$?
        if [ -n "$tip_full" ] && [ "$arc" -eq 0 ] && git merge-base --is-ancestor "$tip_full" HEAD; then
            others=$(git log --format= --name-only "$ref..HEAD" | grep -v '^$' | grep -v '^docs/')
            [ -n "$(git log --format=%h "$ref..HEAD")" ] && [ -z "$others" ] && ok=0
        fi
        row head "git log --oneline -1; git log --stat --format=%h $ref..HEAD" "$arc" "$out
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

# A sibling's .env is information, never this job's failure (card 02 A9; his 10-01 R20: the take waits).
found=""
set +f
for f in "$WT"/*/.env; do
    [ -e "$f" ] || continue
    [ "$f" = "$dir/.env" ] && continue
    found="${found:+$found, }$f"
done
set -f
if [ -n "$found" ]; then
    row "env anywhere" "ls -la $WT/*/.env" 0 "siblings holding .env: $found" 0
else
    row "env anywhere" "ls -la $WT/*/.env" 1 "siblings holding .env: none" 0
fi

if [ "$kind" = check ]; then
    if [ -f "$report" ]; then
        last=$(grep -v '^[[:space:]]*$' "$report" | tail -n 1)
        ok=1
        case "$last" in
            "BUILT · job: $job · tip: $tip"*"self-check: "[0-3]" of 3"*)
                ok=0
                k=${last#*self-check: }
                k=${k%% of 3*}
                ;;
        esac
        row report "tail -n 3 \"$report\"" 0 "$last" "$ok"
        # card 20 F1 (BUILD-HUB.md:97, CHECK-HUB.md:61): a lower self-check count is recorded, not failed.
        [ "$ok" -ne 0 ] || [ "$k" = 3 ] || printf 'report: self-check %s of 3 (recorded)\n' "$k"
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
