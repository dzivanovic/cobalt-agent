#!/bin/sh
# deploy-smoke.sh [--dry-run] "<deploy card>"
# The card's `## MARKERS` and `## SMOKE READS` rows, each run as typed (card 20 deploy-steps, row
# D3; DEPLOY-HUB.md 4.7 (c), (d), (s)). Markers first, then smoke reads, in card order.
#
# A row's command is never handed to a shell: it is matched against the four shapes below and
# its arguments are taken out of it; any other command (or one carrying `$`, a backtick, `;`, `&`,
# `|`, `<`, `>`, `(`, `)`, `*`, `?` or `\` outside the SQL string) is RED, `not a mapped smoke
# command`, and not run:
#   ls <path> | ls "<path>"
#   grep -c -F "<fixed string>" <path>
#   curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/<path>   (`\?` read as `?`; three
#        tries, DEPLOY_SETTLE seconds apart; GREEN on `200`)
#   COBALT_ENV=production uv run cobalt db query <options> "<sql>"   (`\"` inside the SQL read as
#        `"`) — run only when the card's MIGRATIONS is not `none` and the SQL carries no `%`;
#        otherwise the row is SKIPPED and says why
# A marker (`- \`<cmd>\` · before <v> · after <v>`) is GREEN when its output is the `after` value;
# a value is `listed` (exit 0) or a backticked string (the output's last line equals it, or holds
# it when it is not a number). A smoke read (`- <label> · \`<cmd>\` · <expectation>`) is read by
# its expectation up to the first `;`: `exit 0, listed` · `exit 0, \`<v>\`` · `exit 0, a count of
# 1 or more` · `exit 0, one integer`; a row labelled `census`, or whose expectation says
# `recorded`, is a census: its output is recorded, never a gate. Any other expectation is RED.
# A `- ` line of either section not in its row form is RED (`not a marker row` / `not a smoke read
# row`) and not run; lines not starting `- ` are prose and skipped.
# One line per row `<label> · <command> · <output> · GREEN|RED|census|SKIPPED` (a marker's label
# is `marker <n>`); the last line `SMOKE GREEN` (exit 0) or `SMOKE RED: <labels>` (exit 1).
# Every call and its whole output also go to the log $WT/.deploy-logs/<JOB>-smoke-<timestamp>.log.
# A bad call: `REFUSED: <reason>` on stderr, exit 1.
# --dry-run: prints every command it WOULD run, in order (`WOULD RUN: …`; a row it would skip or
# refuse is `WOULD SKIP: …` / `WOULD REFUSE: …`), runs none (`curl`, `uv`, `grep` and `ls` of the
# rows never called), writes no log; last line `DRY RUN — nothing run: <n> commands`.
# THE DESK'S DRY RUN, typed once before the first real use:
#   sh /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh --dry-run "<deploy card>"
#
# COBALT_WT_ROOT stands in for /Users/cobalt/cobalt-wt, and DEPLOY_SETTLE (default 2) for the
# seconds between two curl tries, in tests/ops/test_deploy_smoke.py only.

export LC_ALL=C
set -u
set -f

WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
SETTLE=${DEPLOY_SETTLE:-2}
DBQ="COBALT_ENV=production uv run cobalt db query "
CURLQ="curl -s -o /dev/null -w %{http_code} "

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

dry=""
if [ "${1:-}" = --dry-run ]; then
    dry=1
    shift
fi
[ "$#" -eq 1 ] || refuse "usage: deploy-smoke.sh [--dry-run] \"<deploy card>\""
card=$1
[ -f "$card" ] || refuse "no such card: $card"

field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}
section() {
    awk -v h="## $1" '/^## /{on = ($0 == h); next} on && NF' "$card"
}

job=$(field JOB)
migrations=$(field MIGRATIONS)
[ -n "$migrations" ] || refuse "the card's MIGRATIONS is empty"
case "$job" in
    ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) logname=card ;;
    *) logname=$job ;;
esac

log=""
if [ -z "$dry" ]; then
    logdir="$WT/.deploy-logs"
    mkdir -p "$logdir" || refuse "mkdir failed: $logdir"
    log="$logdir/$logname-smoke-$(date +%Y%m%d-%H%M%S).log"
    : >> "$log" || refuse "cannot write the log: $log"
    printf 'deploy-smoke.sh %s\n' "$card" >> "$log"
fi

say() {
    printf '%s\n' "$*"
    [ -z "$log" ] || printf '%s\n' "$*" >> "$log"
}
note() {
    [ -z "$log" ] || printf '%s\n' "$*" >> "$log"
}
lastline() {
    printf '%s\n' "$1" | sed '/^[[:space:]]*$/d' | tail -n 1
}

reds=""
nwould=0

# plain_path <text>: a path as typed, unquoted (no blank) or in double quotes; sets $path or $why
plain_path() {
    path=$1
    case "$path" in
        \"*\") path=${path#\"}; path=${path%\"} ;;
        *" "*) why="an unquoted path holds a blank"; return 1 ;;
    esac
    case "$path" in
        ""|-*) why="no path"; return 1 ;;
        *[\"\$\`\;\&\|\<\>\(\)\*\?\\]*) why="the path holds a shell character"; return 1 ;;
    esac
    return 0
}

# shape <command>: sets $kind (ls|grep|curl|db) and its arguments, or $why; 0 when mapped
shape() {
    c=$1
    why=""
    case "$c" in
        "ls "*)
            plain_path "${c#ls }" || return 1
            kind=ls
            ;;
        'grep -c -F "'*)
            r=${c#grep -c -F \"}
            case "$r" in *\"\ *) ;; *) why="no closing quote"; return 1 ;; esac
            pat=${r%%\"*}
            case "$pat" in
                ""|*[\$\`\\]*) why="the pattern is empty or holds \$, a backtick or a backslash"; return 1 ;;
            esac
            plain_path "${r#*\" }" || return 1
            kind=grep
            ;;
        "$CURLQ"*)
            url=${c#"$CURLQ"}
            case "$url" in
                http://127.0.0.1:5010/*) ;;
                *) why="curl reads http://127.0.0.1:5010/ only"; return 1 ;;
            esac
            url=$(printf '%s' "$url" | sed 's/\\?/?/g')
            case "$url" in
                *[!A-Za-z0-9/:._?=\&-]*) why="the URL holds a character outside [A-Za-z0-9/:._?=&-]"; return 1 ;;
            esac
            kind=curl
            ;;
        "$DBQ"*)
            r=${c#"$DBQ"}
            opts=${r%%\"*}
            sql=${r#"$opts"}
            for o in $opts; do
                case "$o" in
                    *[!a-z-]*) why="a db query option outside [a-z-]: $o"; return 1 ;;
                esac
            done
            case "$sql" in
                \"*\") sql=${sql#\"}; sql=${sql%\"} ;;
                *) why="the SQL is not one double-quoted string at the end"; return 1 ;;
            esac
            bare=$(printf '%s' "$sql" | sed 's/\\"//g')
            case "$bare" in
                *[\"\$\`\\]*) why="the SQL holds \$, a backtick, a backslash or an unescaped quote"; return 1 ;;
            esac
            sql=$(printf '%s' "$sql" | sed 's/\\"/"/g')
            kind=db
            ;;
        *)
            why="no mapped shape"
            return 1
            ;;
    esac
    return 0
}

# skip_why: for a db row, why it does not run (empty when it runs)
skip_why() {
    sw=""
    if [ "$kind" = db ]; then
        if [ "$migrations" = none ]; then
            sw="skipped: MIGRATIONS is none"
        else
            case "$sql" in *%*) sw="skipped: the query carries % (the tool refuses it)" ;; esac
        fi
    fi
}

# run_shape: runs the mapped command; sets $out (whole), $rc
run_shape() {
    note "\$ $1"
    case "$kind" in
        ls) out=$(ls "$path" 2>&1); rc=$? ;;
        grep) out=$(grep -c -F -e "$pat" "$path" 2>&1); rc=$? ;;
        curl)
            tries=0
            while :; do
                tries=$((tries + 1))
                out=$(curl -s -o /dev/null -w '%{http_code}' "$url" 2>&1)
                rc=$?
                note "try $tries: $out [exit $rc]"
                [ "$out" = 200 ] && break
                [ "$tries" -lt 3 ] || break
                sleep "$SETTLE"
            done
            ;;
        db) out=$(COBALT_ENV=production uv run cobalt db query $opts "$sql" 2>&1); rc=$? ;;
    esac
    note "$out"
    note "[exit $rc]"
}

# value_is <spec>: the run's $out / $rc against `listed` or a backticked value
value_is() {
    case "$1" in
        listed) [ "$rc" -eq 0 ] ;;
        \`*\`)
            v=${1#\`}
            v=${v%\`}
            got=$(lastline "$out")
            [ "$got" = "$v" ] && return 0
            case "$v" in
                ""|*[!0-9]*) case "$got" in *"$v"*) return 0 ;; esac ;;
            esac
            return 1
            ;;
        *) return 2 ;;
    esac
}

red() {
    reds="${reds:+$reds, }$1"
}

# ---- MARKERS ---------------------------------------------------------------------------------
n=0
while IFS= read -r line; do
    case "$line" in "- "*) ;; *) continue ;; esac
    n=$((n + 1))
    label="marker $n"
    case "$line" in
        "- \`"*) ;;
        *)
            # a row not in the marker form is RED and said, never skipped
            if [ -n "$dry" ]; then printf 'WOULD REFUSE: %s — not a marker row\n' "$label"; continue; fi
            say "$label · ${line#- } · not a marker row (- \`<cmd>\` · before <v> · after <v>) · RED"
            red "$label"
            continue
            ;;
    esac
    after_tick=${line#- \`}
    cmd=${after_tick%%\`*}
    tail_=${after_tick#*\`}
    case "$tail_" in
        *" · before "*" · after "*) ;;
        *) say "$label · $cmd · no before / after on the row · RED"; red "$label"; continue ;;
    esac
    aft=${tail_##* · after }
    aft=$(printf '%s' "$aft" | sed 's/[[:space:]]*$//')
    bef=${tail_#* · before }
    bef=${bef%% · after *}
    if ! shape "$cmd"; then
        if [ -n "$dry" ]; then printf 'WOULD REFUSE: %s — %s\n' "$label" "$why"; continue; fi
        say "$label · $cmd · not a mapped smoke command: $why · RED"
        red "$label"
        continue
    fi
    skip_why
    if [ -n "$sw" ]; then
        if [ -n "$dry" ]; then printf 'WOULD SKIP: %s — %s\n' "$label" "$sw"; continue; fi
        say "$label · $cmd · $sw · SKIPPED"
        continue
    fi
    if [ -n "$dry" ]; then
        nwould=$((nwould + 1))
        printf 'WOULD RUN: %s\n' "$cmd"
        continue
    fi
    run_shape "$cmd"
    shown=$(lastline "$out")
    value_is "$aft"
    vr=$?
    if [ "$vr" -eq 0 ]; then
        say "$label · $cmd · ${shown:-nothing} · GREEN"
    elif [ "$vr" -eq 2 ]; then
        say "$label · $cmd · ${shown:-nothing} (after '$aft' is not listed or a backticked value) · RED"
        red "$label"
    else
        value_is "$bef" && shown="$shown (still the before value)"
        say "$label · $cmd · ${shown:-nothing} · RED"
        red "$label"
    fi
done <<EOF
$(section MARKERS)
EOF

# ---- SMOKE READS -----------------------------------------------------------------------------
while IFS= read -r line; do
    case "$line" in "- "*) ;; *) continue ;; esac
    rest=${line#- }
    case "$line" in
        "- "*" · \`"*) ;;
        *)
            # a row not in the smoke-read form is RED and said, never skipped
            label=${rest%% · *}
            if [ -n "$dry" ]; then printf 'WOULD REFUSE: %s — not a smoke read row\n' "$label"; continue; fi
            say "$label · $rest · not a smoke read row (- <label> · \`<cmd>\` · <expectation>) · RED"
            red "$label"
            continue
            ;;
    esac
    label=${rest%% · \`*}
    after_tick=${rest#*\`}
    cmd=${after_tick%%\`*}
    exp=${after_tick#*\`}
    exp=${exp# · }
    exp=${exp%%;*}
    exp=$(printf '%s' "$exp" | sed 's/[[:space:]]*$//')
    if ! shape "$cmd"; then
        if [ -n "$dry" ]; then printf 'WOULD REFUSE: %s — %s\n' "$label" "$why"; continue; fi
        say "$label · $cmd · not a mapped smoke command: $why · RED"
        red "$label"
        continue
    fi
    skip_why
    if [ -n "$sw" ]; then
        if [ -n "$dry" ]; then printf 'WOULD SKIP: %s — %s\n' "$label" "$sw"; continue; fi
        say "$label · $cmd · $sw · SKIPPED"
        continue
    fi
    if [ -n "$dry" ]; then
        nwould=$((nwould + 1))
        printf 'WOULD RUN: %s\n' "$cmd"
        continue
    fi
    run_shape "$cmd"
    shown=$(lastline "$out")
    census=""
    case "$label" in census|census\ *) census=1 ;; esac
    case "$exp" in *recorded*) census=1 ;; esac
    if [ -n "$census" ]; then
        say "$label · $cmd · ${shown:-nothing} · census"
        continue
    fi
    ok=1
    case "$exp" in
        "exit 0, listed") [ "$rc" -eq 0 ] && ok=0 ;;
        "exit 0, \`"*"\`")
            [ "$rc" -eq 0 ] && value_is "${exp#exit 0, }" && ok=0
            ;;
        "\`"*"\`")
            value_is "$exp" && ok=0
            ;;
        "exit 0, a count of 1 or more")
            case "$shown" in ""|*[!0-9]*) ;; *) [ "$rc" -eq 0 ] && [ "$shown" -ge 1 ] && ok=0 ;; esac
            ;;
        "exit 0, one integer"*)
            case "$shown" in ""|*[!0-9]*) ;; *) [ "$rc" -eq 0 ] && ok=0 ;; esac
            ;;
        *)
            say "$label · $cmd · ${shown:-nothing} (expectation '$exp' is not one this script reads) · RED"
            red "$label"
            continue
            ;;
    esac
    if [ "$ok" -eq 0 ]; then
        say "$label · $cmd · ${shown:-nothing} · GREEN"
    else
        say "$label · $cmd · ${shown:-nothing} · RED"
        red "$label"
    fi
done <<EOF
$(section "SMOKE READS")
EOF

if [ -n "$dry" ]; then
    printf 'DRY RUN — nothing run: %s commands\n' "$nwould"
    exit 0
fi
say "log: $log"
if [ -z "$reds" ]; then
    say "SMOKE GREEN"
    exit 0
fi
say "SMOKE RED: $reds"
exit 1
