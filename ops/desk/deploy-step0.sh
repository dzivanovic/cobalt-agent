#!/bin/sh
# deploy-step0.sh [--dry-run] "<deploy card>"
# deploy-step0.sh --window "<deploy card>"
# DEPLOY-HUB.md STEP-0 as ONE table (card 20 deploy-steps, row D1). Read-only: it writes nothing
# but its log ($WT/.deploy-logs/<JOB>-step0-<timestamp>.log); every git read runs with
# GIT_OPTIONAL_LOCKS=0, so not even the index is refreshed.
#
# One row per rule, `rule · command · exit · output` (the output is the first line, or `nothing`):
#   KEYS                 JOB BRANCH WORKTREE TIP REPORT RULINGS TAG MIGRATIONS SET are non-empty
#   SHIPS                ## SHIPS has rows; their heads are TIP, in order
#   P0 authorization     `authorize.sh deploy "<card>"` (the installed hub, the card committed and
#                        unchanged, the standing list and every RULINGS row proved as it proves them);
#                        its own rows are printed above it, prefixed `P0 `; it runs with
#                        LC_ALL=en_US.UTF-8 (it reads `«` and `·` as characters), while this script
#                        runs in LC_ALL=C, exported first
#   P1 window            `date` in ET; the first of P1 (i)–(v) that holds is named:
#                        (i) 20:00–20:59 ET of a trading day · (ii) 21:00 ET of a trading day to 04:00
#                        ET the next morning · (iii) a Saturday, a Sunday, Monday before 04:00 ET, or a
#                        market holiday: a `## RECORDS` line holding the word `holiday` and the day's
#                        date (YYYY-MM-DD) · (iv) a RULINGS row, committed and so at HEAD, holding
#                        `HIS RULING`, `APPROVED`, `L66` or `L43`, the word `overrules` (or
#                        `overruled`), and this card's JOB as a whole name. A trading day is Monday to
#                        Friday and not a holiday so named.
#   P2 check <n>         the ship's check report: its last non-blank line carries `held unfixed: 0`,
#                        `ready: YES` and every backticked literal of the row's last column, a `tip:`
#                        equal to the row's code tip, and
#                        neither starts `(run in progress` nor `FAILED`. A held defect carried by a
#                        ruling is not read here: such a line FAILS and the hub reads it (P2's text).
#   P2 committed <n>     `git log -1 --format=%H -- <report>` non-empty and `git diff --stat -- <report>` empty
#   P3 tip <n>           the code tip and the branch head re-read (`rev-parse --short=8`), the tip an
#                        ancestor of the head, nothing outside docs/ between them
#   P7 migrations        the migration numbers in `git show <head>:src/cobalt/db_migrations/` and not in
#                        `git show main:src/cobalt/db_migrations/`, over every head, EQUAL the 4-digit
#                        numbers before the first `·` of MIGRATIONS (none for `none`), and the hub's
#                        `git diff main <head> -- src/cobalt/db_migrations` holds nothing else: on a
#                        `none` card NOTHING; otherwise only added `NNNN_*.sql` files and the registry
#                        `__init__.py` (an edited or removed migration, or any other file, fails)
#   P8 census <label>    `launchctl print gui/501/<label>` for aset, radar, agent: pid and state,
#                        RECORDED, never a gate
#   disk                 `df -k <repo>`, recorded
#   main status          `git status --short --branch` of the repo, recorded
# NOT mirrored here (the hub keeps them): P4 the lock census, P5 the gate worktree, P6 the markers'
# before values (deploy-smoke.sh reads markers), P8's `path =` gate (deploy-outage.sh proves it
# before its first bootout).
# Last line: `STEP-0 OK — window: <(i)…(iv)>` (exit 0) or `FAILED STEP-0: <rule> — <detail>`
# (exit 1, the first rule that failed; every row is still printed). A bad call: `REFUSED: <reason>`
# on stderr, exit 1.
#
# --window: the P1 row alone; last line `WINDOW <(i)…(iv)>` (exit 0) or `FAILED STEP-0: window —
# <time>` (exit 1). deploy-outage.sh reads the window through it (one implementation). No log.
# --dry-run: prints every command it WOULD run, one per line, in the order a run makes them
# (`WOULD RUN: …`), runs none (`launchctl`,
# `git`, `date` never called), writes no log; last line `DRY RUN — nothing run: <n> commands`.
# THE DESK'S DRY RUN, typed once before the first real use:
#   sh /Users/cobalt/cobalt/ops/desk/deploy-step0.sh --dry-run "<deploy card>"
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_deploy_step0.py only.

export LC_ALL=C
set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
HERE=$(cd "$(dirname "$0")" && pwd)
REPORTS_REL="docs/40 - DevDocs/reports"
GIT_OPTIONAL_LOCKS=0
export GIT_OPTIONAL_LOCKS
RESIDENTS="com.cobalt.aset com.cobalt.radar com.cobalt.agent"
NOW_CMD="TZ=America/New_York date '+%u %H %M %Y-%m-%d %a'"

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

usage='usage: deploy-step0.sh [--dry-run | --window] "<deploy card>"'
mode=run
case "${1:-}" in
    --dry-run) mode=dry; shift ;;
    --window) mode=window; shift ;;
    -*) refuse "unknown option '$1'; $usage" ;;
esac
[ "$#" -eq 1 ] || refuse "$usage"
card=$1
[ -f "$card" ] || refuse "no such card: $card"

# field KEY -> the value of the card's first "KEY: value" line, trailing blanks cut (desk-launch.sh's)
field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}
# section TITLE -> the card's non-blank lines under "## TITLE", up to the next "## " heading
section() {
    awk -v h="## $1" '/^## /{on = ($0 == h); next} on && NF' "$card"
}

log=""
failed=""
nwould=0

say() {
    printf '%s\n' "$*"
    [ -z "$log" ] || printf '%s\n' "$*" >> "$log"
}

would() {
    nwould=$((nwould + 1))
    printf 'WOULD RUN: %s\n' "$*"
}

# row <rule> <command> <exit> <output> <ok: 0 or 1> [<detail on failure>]
row() {
    res=$(printf '%s\n' "$4" | sed '/^[[:space:]]*$/d' | sed -n '1p')
    [ -n "$res" ] || res=nothing
    say "$1 · $2 · $3 · $res"
    if [ -n "$log" ] && [ -n "$4" ]; then
        printf '%s\n' "$4" | sed 's/^/    | /' >> "$log"
    fi
    if [ "$5" -ne 0 ] && [ -z "$failed" ]; then
        failed="$1${6:+ — $6}"
    fi
}

job=$(field JOB)
rulings=$(field RULINGS)

# rel <path> -> the path relative to $REPO (as given when it lies elsewhere)
rel() {
    case "$1" in
        "$REPO"/*) printf '%s' "${1#"$REPO"/}" ;;
        *) printf '%s' "$1" ;;
    esac
}

# ---- P1 THE WINDOW ---------------------------------------------------------------------------
leap() {
    [ $(($1 % 4)) -eq 0 ] && { [ $(($1 % 100)) -ne 0 ] || [ $(($1 % 400)) -eq 0 ]; }
}

# prev_day YYYY-MM-DD -> the day before, YYYY-MM-DD
prev_day() {
    py=${1%%-*}
    pm=${1#*-}; pm=${pm%-*}; pm=${pm#0}
    pd=${1##*-}; pd=${pd#0}
    pd=$((pd - 1))
    if [ "$pd" -eq 0 ]; then
        pm=$((pm - 1))
        if [ "$pm" -eq 0 ]; then
            pm=12
            py=$((py - 1))
        fi
        case "$pm" in
            1|3|5|7|8|10|12) pd=31 ;;
            4|6|9|11) pd=30 ;;
            *) if leap "$py"; then pd=29; else pd=28; fi ;;
        esac
    fi
    printf '%04d-%02d-%02d' "$py" "$pm" "$pd"
}

# holiday YYYY-MM-DD: a ## RECORDS line holding the word holiday and the date
holiday() {
    section RECORDS | grep -i -F -e holiday | grep -q -F -e "$1"
}

# override: a RULINGS row of his, committed, that overrules L66 / L43 and names this JOB
override=""
find_override() {
    d=""
    for t in $(printf '%s\n' "$rulings" | sed -e 's/·/ /g' -e 's/[,;]/ /g'); do
        case "$t" in
            20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) d=$t ;;
            R[0-9]*)
                [ -n "$d" ] || continue
                f="$REPO/$REPORTS_REL/cto-$d.md"
                [ -f "$f" ] || continue
                line=$(grep "^| $t " "$f" | sed -n '1p')
                case "$line" in *"HIS RULING"*) ;; *) continue ;; esac
                case "$line" in *APPROVED*) ;; *) continue ;; esac
                case "$line" in *L66*|*L43*) ;; *) continue ;; esac
                # the hub's (iv): a row that OVERRULES the window, not one that names or affirms it
                case "$line" in *[Oo]verrul*) ;; *) continue ;; esac
                [ -n "$job" ] || continue
                # the JOB as a whole name: `x-set` is not named by `x-set-2`
                words=" $(printf '%s' "$line" | tr -c 'abcdefghijklmnopqrstuvwxyz0123456789-' ' ') "
                case "$words" in *" $job "*) ;; *) continue ;; esac
                c=$(git -C "$REPO" log -1 --format=%H -S"| $t |" -- "$REPORTS_REL/cto-$d.md" 2>/dev/null)
                [ -n "$c" ] || continue
                # the row as read, at HEAD (authorize.sh's proof): a working-tree rewrite is not his
                git -C "$REPO" show "HEAD:$REPORTS_REL/cto-$d.md" 2>/dev/null | grep -q -x -F -e "$line" || continue
                override="$d $t"
                return 0
                ;;
        esac
    done
    return 1
}

holds=""
window() {
    if [ "$mode" = dry ]; then
        would "$NOW_CMD"
        return 0
    fi
    now=$(TZ=America/New_York date '+%u %H %M %Y-%m-%d %a' 2>&1)
    rc=$?
    set -- $now
    if [ "$rc" -ne 0 ] || [ "$#" -ne 5 ]; then
        row "P1 window" "$NOW_CMD" "$rc" "$now" 1
        [ "$failed" != "P1 window" ] || failed="window — the clock is unreadable: $now"
        return 1
    fi
    u=$1 hh=$2 mm=$3 day=$4 wd=$5
    case "$u$hh$mm" in
        *[!0-9]*)
            row "P1 window" "$NOW_CMD" "$rc" "$now" 1
            [ "$failed" != "P1 window" ] || failed="window — the clock is unreadable: $now"
            return 1
            ;;
    esac
    h=${hh#0}
    yday=$(prev_day "$day")
    yu=$((u - 1))
    [ "$yu" -ne 0 ] || yu=7
    today_trading=1
    { [ "$u" -le 5 ] && ! holiday "$day"; } || today_trading=0
    yday_trading=1
    { [ "$yu" -le 5 ] && ! holiday "$yday"; } || yday_trading=0
    time="$wd $day $hh:$mm ET"
    holds=""
    if [ "$today_trading" -eq 1 ] && [ "$h" -eq 20 ]; then
        holds="(i)"; why="the 20:00-21:00 ET pause of a trading day"
    elif { [ "$today_trading" -eq 1 ] && [ "$h" -ge 21 ]; } || { [ "$h" -lt 4 ] && [ "$yday_trading" -eq 1 ]; }; then
        holds="(ii)"; why="the overnight idle after a trading day, before 04:00 ET"
    elif [ "$u" -ge 6 ] || { [ "$u" -eq 1 ] && [ "$h" -lt 4 ]; } || holiday "$day"; then
        holds="(iii)"; why="a non-trading day"
    elif find_override; then
        holds="(iv)"; why="his per-case override $override"
    fi
    if [ -n "$holds" ]; then
        row "P1 window" "$NOW_CMD" 0 "$time — holds: $holds $why" 0
        return 0
    fi
    row "P1 window" "$NOW_CMD" 0 "$time — none of (i)-(iv) holds" 1
    # the window's failure reads as P1 writes it: `window — <time>`
    [ "$failed" != "P1 window" ] || failed="window — $time"
    return 1
}

if [ "$mode" = window ]; then
    if window; then
        printf 'WINDOW %s\n' "$holds"
        exit 0
    fi
    printf 'FAILED STEP-0: %s\n' "$failed"
    exit 1
fi

# ---- the log ---------------------------------------------------------------------------------
case "$job" in
    ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) logname=card ;;
    *) logname=$job ;;
esac
if [ "$mode" = run ]; then
    logdir="$WT/.deploy-logs"
    mkdir -p "$logdir" || refuse "mkdir failed: $logdir"
    log="$logdir/$logname-step0-$(date +%Y%m%d-%H%M%S).log"
    : >> "$log" || refuse "cannot write the log: $log"
    printf 'deploy-step0.sh %s\n' "$card" >> "$log"
fi

# ---- KEYS and SHIPS --------------------------------------------------------------------------
missing=""
for k in JOB BRANCH WORKTREE TIP REPORT RULINGS TAG MIGRATIONS SET; do
    [ -n "$(field "$k")" ] || missing="$missing $k"
done
if [ -z "$missing" ]; then
    row KEYS "field JOB BRANCH WORKTREE TIP REPORT RULINGS TAG MIGRATIONS SET" 0 "all present" 0
else
    row KEYS "field JOB BRANCH WORKTREE TIP REPORT RULINGS TAG MIGRATIONS SET" 1 "empty:$missing" 1 "empty:$missing"
fi

tiplist=$(field TIP)
migrations=$(field MIGRATIONS)
ships=$(section SHIPS | awk -F'|' '$2 ~ /^ *[0-9]+ *$/')
nships=0
heads=""
if [ -n "$ships" ]; then
    nships=$(printf '%s\n' "$ships" | wc -l | tr -d ' ')
    heads=$(printf '%s\n' "$ships" | awk -F'|' '{print $5}' | tr -d '` ' | tr '\n' ' ' | sed 's/ *$//')
fi
tipnorm=$(printf '%s' "$tiplist" | tr -s ' ')
if [ "$nships" -ge 1 ] && [ "$heads" = "$tipnorm" ]; then
    row SHIPS "section SHIPS" 0 "$nships row(s), heads = TIP: $heads" 0
else
    row SHIPS "section SHIPS" 1 "$nships row(s), heads '$heads' against TIP '$tipnorm'" 1 "the ## SHIPS heads are not TIP: '$heads' against '$tipnorm'"
fi

# ---- P0 AUTHORIZATION ------------------------------------------------------------------------
acmd="LC_ALL=en_US.UTF-8 sh $HERE/authorize.sh deploy \"$card\""
if [ "$mode" = dry ]; then
    would "$acmd"
else
    # authorize.sh reads the hub title's `«` and `·` as characters: it runs in a UTF-8 locale
    # (LC_ALL=C stays first in this script; the caller's locale is not read)
    aout=$(LC_ALL=en_US.UTF-8 sh "$HERE/authorize.sh" deploy "$card" 2>&1)
    arc=$?
    printf '%s\n' "$aout" | while IFS= read -r l; do say "P0 $l"; done
    alast=$(printf '%s\n' "$aout" | sed '/^[[:space:]]*$/d' | tail -n 1)
    ok=1
    [ "$arc" -eq 0 ] && ok=0
    row "P0 authorization" "$acmd" "$arc" "$alast" "$ok" "$alast"
fi

# ---- P1 --------------------------------------------------------------------------------------
window

# ---- P2, P3 and the migration listings, per ship ---------------------------------------------
newnums=""
stray=""
mainlist=""
if [ "$mode" = dry ]; then
    would "git -C $REPO show main:src/cobalt/db_migrations/"
else
    mainlist=$(git -C "$REPO" show "main:src/cobalt/db_migrations/" 2>&1)
    mainrc=$?
fi
n=0
while IFS= read -r line; do
    [ -n "$line" ] || continue
    n=$((n + 1))
    branch=$(printf '%s\n' "$line" | awk -F'|' '{print $3}' | tr -d '` ')
    ctip=$(printf '%s\n' "$line" | awk -F'|' '{print $4}' | tr -d '` ')
    head=$(printf '%s\n' "$line" | awk -F'|' '{print $5}' | tr -d '` ')
    report=$(printf '%s\n' "$line" | awk -F'|' '{print $6}' | tr -d '`' | sed -e 's/^ *//' -e 's/ *$//')
    lits=$(printf '%s\n' "$line" | awk -F'|' '{print $7}' | grep -o '`[^`]*`' | tr -d '`')
    frep=$(printf '%s\n' "$line" | awk -F'|' '{print $8}' | tr -d '`' | sed -e 's/^ *//' -e 's/ *$//')
    # the card's D1 and the hub's P2: a clean check always carries these two, whatever the row names
    lits=$(printf 'held unfixed: 0\nready: YES\n%s\n' "$lits")
    rrel=$(rel "$report")
    c_tail="grep -v '^[[:space:]]*\$' \"$report\" | tail -n 1"
    c_log="git -C $REPO log -1 --format=%H -- \"$rrel\""
    c_diff="git -C $REPO diff --stat -- \"$rrel\""
    c_rp1="git -C $REPO rev-parse --verify --quiet --short=8 $ctip^{commit}"
    c_rp2="git -C $REPO rev-parse --verify --quiet --short=8 refs/heads/$branch^{commit}"
    c_rp="$c_rp1; $c_rp2"
    c_anc="git -C $REPO merge-base --is-ancestor $ctip $head"
    c_past="git -C $REPO diff --stat $ctip $head -- . ':(exclude)docs'"
    c_mig="git -C $REPO show $head:src/cobalt/db_migrations/"
    c_md="git -C $REPO diff --name-status --no-renames main $head -- src/cobalt/db_migrations"
    if [ "$mode" = dry ]; then
        for c in "$c_tail" "$c_log" "$c_diff" "$c_rp1" "$c_rp2" "$c_anc" "$c_past" "$c_mig" "$c_md"; do
            would "$c"
        done
        continue
    fi

    # P2: the check's stop line
    if [ -f "$report" ]; then
        last=$(grep -v '^[[:space:]]*$' "$report" | tail -n 1)
        why=""
        case "$last" in
            "(run in progress"*) why="the check is still running: $last" ;;
            FAILED*) why="the check FAILED: $last" ;;
        esac
        if [ -z "$why" ]; then
            while IFS= read -r lit; do
                [ -n "$lit" ] || continue
                case "$last" in
                    *"$lit"*) ;;
                    *) why="the last line lacks '$lit': $last"; break ;;
                esac
            done <<EOF
$lits
EOF
        fi
        if [ -z "$why" ]; then
            t=$(printf '%s\n' "$last" | grep -o -E '(^| )tip: [0-9a-f]{7,40}' | sed -n '1p' | sed 's/.*tip: //')
            case "$t" in
                "") why="the last line names no tip: $last" ;;
                "$ctip"*) ;;
                *) case "$ctip" in "$t"*) ;; *) why="its tip $t is not the row's code tip $ctip" ;; esac ;;
            esac
            # a fix round (his R376, L75): the row's `fix report` ends `BUILT · … tip: <code tip>` and
            # the check's tip is an ancestor of the code tip; the literals above stay the check's
            if [ -n "$why" ] && [ -n "$t" ] && [ -n "$frep" ]; then
                flast=""
                [ -f "$frep" ] && flast=$(grep -v '^[[:space:]]*$' "$frep" | tail -n 1)
                case "$flast" in
                    "BUILT ·"*"tip: $ctip"*)
                        if git -C "$REPO" merge-base --is-ancestor "$t" "$ctip" 2>/dev/null; then
                            why=""
                        else
                            why="$why, nor its ancestor (fix report $frep)"
                        fi ;;
                    *) why="$why; the fix report $frep does not end 'BUILT · … tip: $ctip': ${flast:-absent}" ;;
                esac
            fi
        fi
        ok=0
        [ -z "$why" ] || ok=1
        row "P2 check $n" "$c_tail" 0 "$last" "$ok" "$report — $why"
    else
        row "P2 check $n" "$c_tail" 1 "no such file" 1 "$report — absent"
    fi

    # P2: committed, and unchanged since
    clog=$(git -C "$REPO" log -1 --format=%H -- "$rrel" 2>&1)
    clrc=$?
    cdiff=$(git -C "$REPO" diff --stat -- "$rrel" 2>&1)
    cdrc=$?
    ok=1
    [ "$clrc" -eq 0 ] && [ -n "$clog" ] && [ "$cdrc" -eq 0 ] && [ -z "$cdiff" ] && ok=0
    dshow=$(printf '%s\n' "$cdiff" | sed -n '1p')
    row "P2 committed $n" "$c_log; $c_diff" "$clrc/$cdrc" "commit ${clog:-none}; diff: ${dshow:-nothing}" "$ok" "$report — commit '${clog:-none}', diff '${dshow:-nothing}'"

    # P3: the tips re-read
    rtip=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "$ctip^{commit}" 2>/dev/null)
    rhead=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "refs/heads/$branch^{commit}" 2>/dev/null)
    git -C "$REPO" merge-base --is-ancestor "$ctip" "$head" 2>/dev/null
    anc=$?
    past=$(git -C "$REPO" diff --stat "$ctip" "$head" -- . ':(exclude)docs' 2>&1)
    why=""
    if [ "$rtip" != "$ctip" ]; then
        why="code tip re-read '$rtip', the row has '$ctip'"
    elif [ "$rhead" != "$head" ]; then
        why="$branch is at '$rhead', the row has '$head'"
    elif [ "$anc" -ne 0 ]; then
        why="$ctip is not an ancestor of $head"
    elif [ -n "$past" ]; then
        why="$head adds paths outside docs/ past $ctip: $(printf '%s\n' "$past" | sed -n '1p')"
    fi
    ok=0
    [ -z "$why" ] || ok=1
    row "P3 tip $n" "$c_rp; $c_anc; $c_past" "$anc" "tip $rtip · head $rhead · ancestor exit $anc · past docs: ${past:-nothing}" "$ok" "$branch — $why"

    # the head's migration listing, against main's
    hlist=$(git -C "$REPO" show "$head:src/cobalt/db_migrations/" 2>&1)
    hrc=$?
    if [ "$hrc" -ne 0 ] || [ "$mainrc" -ne 0 ]; then
        row "P7 listing $n" "$c_mig" "$hrc" "$hlist" 1 "the migration listing is unreadable: $(printf '%s\n' "$hlist" | sed -n '1p')"
        continue
    fi
    added=$(printf '%s\n' "$hlist" | sed '1,2d' | while IFS= read -r f; do
        printf '%s\n' "$mainlist" | sed '1,2d' | grep -q -x -F -e "$f" || printf '%s\n' "$f"
    done)
    nums=$(printf '%s\n' "$added" | sed -n 's/^\([0-9][0-9][0-9][0-9]\)_.*\.sql$/\1/p' | sort -u | tr '\n' ' ' | sed 's/ *$//')
    newnums="$newnums $nums"
    row "P7 listing $n" "$c_mig" 0 "new against main: ${nums:-none}" 0

    # the hub's P7 diff: on a `none` card it prints NOTHING; otherwise only added NNNN_ files
    # (their numbers compared above) and the registry. An edited or removed migration is stray.
    mdiff=$(git -C "$REPO" diff --name-status --no-renames main "$head" -- src/cobalt/db_migrations 2>&1)
    mdrc=$?
    if [ "$mdrc" -ne 0 ]; then
        stray="$stray $(printf '%s\n' "$mdiff" | sed -n '1p')"
        continue
    fi
    isnone=""
    [ "$migrations" != none ] || isnone=1
    s=$(printf '%s\n' "$mdiff" | awk -F'\t' -v none="$isnone" '
        NF >= 2 {
            b = $2; sub(/.*\//, "", b)
            if (none == "" && $1 == "A" && b ~ /^[0-9][0-9][0-9][0-9]_.*\.sql$/) next
            if (none == "" && b == "__init__.py") next
            print $1 " " $2
        }' | tr '\n' ' ' | sed 's/ *$//')
    [ -z "$s" ] || stray="$stray $s"
done <<EOF
$ships
EOF

if [ "$mode" != dry ]; then
    got=$(printf '%s\n' $newnums | sed '/^$/d' | sort -u | tr '\n' ' ' | sed 's/ *$//')
    case "$migrations" in
        none) want="" ;;
        *) want=$(printf '%s\n' "$migrations" | sed 's/·.*//' | grep -o '[0-9][0-9][0-9][0-9]' | sort -u | tr '\n' ' ' | sed 's/ *$//') ;;
    esac
    stray=$(printf '%s' "$stray" | sed -e 's/^ *//' -e 's/ *$//')
    ok=1
    [ "$got" = "$want" ] && [ -z "$stray" ] && ok=0
    row "P7 migrations" "git -C $REPO show <head>:src/cobalt/db_migrations/ against main; git -C $REPO diff --name-status --no-renames main <head> -- src/cobalt/db_migrations" 0 "heads add: ${got:-none}; MIGRATIONS names: ${want:-none}; other migration changes: ${stray:-none}" "$ok" "the heads add '${got:-none}', MIGRATIONS names '${want:-none}', other migration changes '${stray:-none}'"
fi

# ---- RECORDED, never a gate: the census, the disk, main ---------------------------------------
for label in $RESIDENTS; do
    c="launchctl print gui/501/$label"
    if [ "$mode" = dry ]; then
        would "$c"
        continue
    fi
    out=$(launchctl print "gui/501/$label" 2>&1)
    rc=$?
    pid=$(printf '%s\n' "$out" | sed -n 's/^[[:space:]]*pid = \([0-9][0-9]*\).*/\1/p' | sed -n '1p')
    st=$(printf '%s\n' "$out" | sed -n 's/^[[:space:]]*state = \(.*\)$/\1/p' | sed -n '1p')
    row "P8 census $label" "$c" "$rc" "pid ${pid:-none} · state ${st:-none} (recorded)" 0
done

if [ "$mode" = dry ]; then
    would "df -k $REPO"
    would "git -C $REPO status --short --branch"
    printf 'DRY RUN — nothing run: %s commands\n' "$nwould"
    exit 0
fi
out=$(df -k "$REPO" 2>&1)
rc=$?
row disk "df -k $REPO" "$rc" "$(printf '%s\n' "$out" | tail -n 1) (recorded)" 0
out=$(git -C "$REPO" status --short --branch 2>&1)
rc=$?
dirty=$(printf '%s\n' "$out" | sed '1d' | sed '/^$/d' | wc -l | tr -d ' ')
row "main status" "git -C $REPO status --short --branch" "$rc" "$(printf '%s\n' "$out" | sed -n '1p') · $dirty other line(s) (recorded)" 0

say "log: $log"
if [ -z "$failed" ]; then
    say "STEP-0 OK — window: $holds"
    exit 0
fi
say "FAILED STEP-0: $failed"
exit 1
