#!/bin/sh
# deploy-card.sh --job <name> --set <word> --worktree <dir> --tag <tag> --out "<new card path>"
#                [--rulings "<list>"] "<job card>" …
# Writes ONE new file, the deploy card at --out, in the format of prompts/CARD.md, from checked
# job cards, in the order given (card 18 desk-tools-b, row B1; DEPLOY-HUB.md STEP-0 P2 and P3).
# Per job card it reads JOB, LADDER, BRANCH and CHECK REPORT; the code tip is the `tip:` of that
# check report's last non-blank line; the branch head is `git -C $REPO rev-parse --short=8 <BRANCH>`.
# REFUSED (exit 1, nothing written), naming the job and the reason, when: the check report is
# absent, not committed, or modified since its commit; its last line lacks `held unfixed: 0` or
# `ready: YES`, or names no tip; the code tip is not an ancestor of the head; the head adds
# anything outside docs/ past the code tip. Also refused: an --out path that exists, a worktree
# outside $WT/<one directory name>, a value outside its character set.
# It then TRIAL-MERGES the heads onto main in order with `git merge-tree --write-tree` (git
# objects only: no branch, worktree, ref, index or working-tree change); a conflict exits 3 with
# `CONFLICT <job> <paths>` on stdout and nothing written.
# The card: JOB, LADDER (the first job card's), BRANCH deploy/<name>, WORKTREE, BASE main, TIP
# (the heads, in order), REPORT $REPORTS/deploy-<name>.md, RULINGS (none unless given), TAG, SET,
# MIGRATIONS (none, or the «FILL placeholder listing the changed files); ## SHIPS; ## MARKERS and
# ## SMOKE READS from each job card's ## DEPLOY PROOF section (a line carrying `· before ` and
# `· after ` is a marker, any other line a smoke read), else the «FILL placeholder; ## RECORDS.
# The «FILL placeholder is the token desk-launch.sh refuses: an incomplete card cannot launch.
# It commits nothing, and no git read of it rewrites the index (GIT_OPTIONAL_LOCKS=0; the check
# report's commit is proven by blob ids, never by `git diff`, which refreshes the index).
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).

export LC_ALL=C
set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
REPORTS="$REPO/docs/40 - DevDocs/reports"
# no git read here refreshes and rewrites the index: --out is the one file written
GIT_OPTIONAL_LOCKS=0
export GIT_OPTIONAL_LOCKS
nl='
'

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

usage="usage: deploy-card.sh --job <name> --set <word> --worktree <dir> --tag <tag> --out \"<new card path>\" [--rulings \"<list>\"] \"<job card>\" …"
name="" set="" wt="" tag="" out="" rulings="none"
while [ "$#" -gt 0 ]; do
    case "$1" in
        --job) [ "$#" -ge 2 ] || refuse "$usage"; name=$2; shift 2 ;;
        --set) [ "$#" -ge 2 ] || refuse "$usage"; set=$2; shift 2 ;;
        --worktree) [ "$#" -ge 2 ] || refuse "$usage"; wt=$2; shift 2 ;;
        --tag) [ "$#" -ge 2 ] || refuse "$usage"; tag=$2; shift 2 ;;
        --out) [ "$#" -ge 2 ] || refuse "$usage"; out=$2; shift 2 ;;
        --rulings) [ "$#" -ge 2 ] || refuse "$usage"; rulings=$2; shift 2 ;;
        --) shift; break ;;
        -*) refuse "unknown option '$1'; $usage" ;;
        *) break ;;
    esac
done
[ "$#" -ge 1 ] || refuse "no job card given; $usage"
[ -n "$name" ] && [ -n "$set" ] && [ -n "$wt" ] && [ -n "$tag" ] && [ -n "$out" ] || refuse "$usage"

case "$name" in
    *[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) refuse "--job '$name' must be [a-z0-9-]" ;;
esac
case "$set" in
    *[!A-Za-z0-9-]*|-*) refuse "--set '$set' must be one word [A-Za-z0-9-]" ;;
esac
case "$tag" in
    *[!A-Za-z0-9._-]*|-*|.*) refuse "--tag '$tag' is not a plain tag name" ;;
esac
case "$wt" in
    .*|*[!A-Za-z0-9._-]*) refuse "worktree '$wt' is outside the approved pattern $WT/<one directory name>" ;;
esac
[ "$wt" != "agy-trial" ] || refuse "worktree 'agy-trial' is the check hubs' scratch tree, never a gate"
case "$rulings" in
    none) ;;
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\ R[0-9]*) ;;
    *) refuse "--rulings must start '<date> R<n>', or be omitted for 'none'" ;;
esac
case "$rulings" in
    *"$nl"*) refuse "--rulings holds a line break" ;;
esac
{ [ -e "$out" ] || [ -L "$out" ]; } && refuse "--out exists: $out (this script writes a new card only)"
[ -d "$(dirname "$out")" ] || refuse "--out's folder does not exist: $(dirname "$out")"
git -C "$REPO" rev-parse --verify --quiet "refs/heads/main^{commit}" >/dev/null || refuse "no branch main in $REPO"

# field <file> KEY -> the value of the first "KEY: value" line, trailing blanks cut (desk-launch.sh's)
field() {
    sed -n "s/^$2: *//p" "$1" | sed -n '1p' | sed 's/[[:space:]]*$//'
}

# ---- every job card: its check, its tip, its head (P2, P3) -----------------------------------
ladder=""
heads=""
ships=""
markers=""
smokes=""
records=""
migs=""
n=0
for card in "$@"; do
    n=$((n + 1))
    [ -f "$card" ] || refuse "no such job card: $card"
    job=$(field "$card" JOB)
    branch=$(field "$card" BRANCH)
    creport=$(field "$card" "CHECK REPORT")
    [ -n "$job" ] || refuse "job card $card: JOB is empty"
    case "$job" in
        *[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) refuse "job card $card: JOB '$job' must be [a-z0-9-]" ;;
    esac
    [ -n "$branch" ] || refuse "$job: BRANCH is empty"
    case "$branch" in
        *[!A-Za-z0-9._/-]*|-*|*..*) refuse "$job: BRANCH '$branch' is not a plain branch name" ;;
    esac
    [ -n "$creport" ] || refuse "$job: CHECK REPORT is empty"
    if [ "$n" -eq 1 ]; then
        ladder=$(field "$card" LADDER)
        [ -n "$ladder" ] || refuse "$job: LADDER is empty (the first job card's LADDER heads the deploy card)"
    fi

    [ -f "$creport" ] || refuse "$job: the check report is absent: $creport"
    # committed and unchanged: the file, its index entry and HEAD's blob are one object
    # (blob reads only: `git diff` would refresh and rewrite the index)
    rel=$(git -C "$REPO" ls-files --full-name --error-unmatch -- "$creport" 2>/dev/null) || refuse "$job: the check report is not committed: $creport"
    committed_blob=$(git -C "$REPO" rev-parse --verify --quiet "HEAD:$rel") || refuse "$job: the check report is not committed: $creport"
    index_blob=$(git -C "$REPO" ls-files -s -- "$creport" | awk '{print $2}')
    file_blob=$(git -C "$REPO" hash-object -- "$creport")
    [ "$index_blob" = "$committed_blob" ] || refuse "$job: the check report is staged, not committed: $creport"
    [ "$file_blob" = "$committed_blob" ] || refuse "$job: the check report is modified since its commit: $creport"
    last=$(grep -v '^[[:space:]]*$' "$creport" | tail -n 1)
    printf '%s\n' "$last" | grep -q -E '(^| )held unfixed: 0( |$)' || refuse "$job: the check's last line lacks 'held unfixed: 0': $last"
    printf '%s\n' "$last" | grep -q -E '(^| )ready: YES( |$)' || refuse "$job: the check's last line lacks 'ready: YES': $last"
    tip=$(printf '%s\n' "$last" | grep -o -E '(^| )tip: [0-9a-f]{7,40}' | sed -n '1p' | sed 's/.*tip: //')
    [ -n "$tip" ] || refuse "$job: the check's last line names no tip: $last"
    ctip=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "$tip^{commit}") || refuse "$job: code tip '$tip' is not a commit in $REPO"
    head=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "refs/heads/$branch^{commit}") || refuse "$job: no branch '$branch' in $REPO"
    git -C "$REPO" merge-base --is-ancestor "$ctip" "$head" || refuse "$job: code tip $ctip is not an ancestor of the head $head of $branch"
    past=$(git -C "$REPO" diff --name-only "$ctip" "$head" -- . ':(exclude)docs')
    [ -z "$past" ] || refuse "$job: the head $head adds paths outside docs/ past the code tip $ctip: $(printf '%s' "$past" | tr '\n' ' ')"

    heads="${heads:+$heads }$head"
    ships="$ships| $n | \`$branch\` | \`$ctip\` | \`$head\` | \`$creport\` | \`held unfixed: 0\` and \`ready: YES\` |$nl"
    records="$records- $job: check \`$creport\` last line: $last$nl- $job: head \`git -C $REPO rev-parse --short=8 $branch\` → \`$head\`; code tip \`$ctip\`$nl"
    # what the head changes since it left main (three dots): a migration main gained is not the head's
    changed=$(git -C "$REPO" diff --name-only "main...$head" -- src/cobalt/db_migrations)
    [ -z "$changed" ] || migs="${migs:+$migs }$(printf '%s' "$changed" | tr '\n' ' ' | sed 's/ $//')"

    # ## DEPLOY PROOF: its non-blank lines up to the next "## " heading
    proof=$(awk '/^## /{on = ($0 == "## DEPLOY PROOF"); next} on && NF' "$card")
    if [ -z "$proof" ]; then
        markers="$markers- «FILL: markers for $job (its job card has no ## DEPLOY PROOF)»$nl"
        smokes="$smokes- «FILL: smoke reads for $job (its job card has no ## DEPLOY PROOF)»$nl"
    else
        m=$(printf '%s\n' "$proof" | grep -F -e '· before ' | grep -F -e '· after ')
        s=$(printf '%s\n' "$proof" | awk 'index($0, "· before ") == 0 || index($0, "· after ") == 0')
        if [ -n "$m" ]; then markers="$markers$m$nl"; else markers="$markers- «FILL: markers for $job (its ## DEPLOY PROOF holds none)»$nl"; fi
        if [ -n "$s" ]; then smokes="$smokes$s$nl"; else smokes="$smokes- «FILL: smoke reads for $job (its ## DEPLOY PROOF holds none)»$nl"; fi
    fi
done

# ---- the trial merge onto main, in order: git objects only, nothing else moves ---------------
cur=$(git -C "$REPO" rev-parse --verify "refs/heads/main^{commit}")
n=0
for card in "$@"; do
    n=$((n + 1))
    job=$(field "$card" JOB)
    head=$(printf '%s\n' "$heads" | tr ' ' '\n' | sed -n "${n}p")
    result=$(git -C "$REPO" merge-tree --write-tree --name-only --no-messages "$cur" "$head")
    status=$?
    case "$status" in
        0) ;;
        1)
            paths=$(printf '%s\n' "$result" | sed '1d' | sed '/^$/d' | sort -u | tr '\n' ' ' | sed 's/ $//')
            printf 'CONFLICT %s %s\n' "$job" "$paths"
            exit 3
            ;;
        *) refuse "$job: the trial merge could not run (git merge-tree exit $status)" ;;
    esac
    tree=$(printf '%s\n' "$result" | sed -n '1p')
    cur=$(GIT_AUTHOR_NAME=deploy-card GIT_AUTHOR_EMAIL=deploy-card@localhost \
        GIT_COMMITTER_NAME=deploy-card GIT_COMMITTER_EMAIL=deploy-card@localhost \
        git -C "$REPO" commit-tree "$tree" -p "$cur" -p "$head" -m "deploy-card trial merge") \
        || refuse "$job: the trial merge could not record its step"
done

# ---- the card ------------------------------------------------------------------------------
if [ -z "$migs" ]; then
    migrations="none"
else
    migrations="«FILL: the numbers in FORWARD order · production at <level> · creates: <objects> · old code on the new schema: <why> — changed against main: ${migs}»"
fi
now=$(TZ=America/New_York date '+%Y-%m-%d %H:%M ET')

text="JOB: $name
LADDER: $ladder
BRANCH: deploy/$name
WORKTREE: $wt
BASE: main
TIP: $heads
REPORT: $REPORTS/deploy-$name.md
RULINGS: $rulings
TAG: $tag
MIGRATIONS: $migrations
SET: $set

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
$ships
## MARKERS
$markers
## SMOKE READS
$smokes
## RECORDS
$records- written by deploy-card.sh at $now (\`date\`); trial merge of the heads onto main in order: clean"

( set -C; printf '%s\n' "$text" > "$out" ) 2>/dev/null || refuse "could not write --out (it exists now, or the folder is not writable): $out"
printf 'deploy-card: %s written (%s job(s), TIP %s)\n' "$out" "$#" "$heads"
