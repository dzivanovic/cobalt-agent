#!/bin/sh
# authorize.sh <build|check|deploy> "<card>" — the AUTHORIZATION block of the kind's fixed file
# (BUILD-HUB.md, CHECK-HUB.md or DEPLOY-HUB.md) run as ONE call (card 19 worker-steps S1). Read-only.
#
# Prints one row per rule, `rule · command · exit · result` (the result is the first line the
# command printed, or `nothing`):
#   INSTALLED            the fixed file holds no install token (grep exit 1)
#   PLACEHOLDER          the card holds no placeholder token (grep exit 1)
#   CARD COMMITTED       `git -C $REPO log -1 --format=%H -- <card>` is non-empty
#   CARD UNCHANGED       `git -C $REPO diff --stat -- <card>` is empty
#   STANDING LIST <date> R<n> row|committed|at HEAD
#                        the row the fixed file's title names (`INSTALL: <date> R<n>`, the first one)
#   RULING <date> R<n> row|committed|at HEAD
#                        every `<date> R<n>` of the card's RULINGS (`none` → no row; `<date> R1, R2`
#                        and several dates are read as written)
#   HOUSE A|HOUSE B overruled <date> R<n> row|committed|at HEAD
#                        a HOUSE line that ends `overruled <date> R<n>`
# A row `<date> R<n>` is proved by: `grep -n "^| R<n> " $REPO/docs/40 - DevDocs/reports/cto-<date>.md`
# → ONE line holding `HIS RULING` and `APPROVED` (row); `git -C $REPO log -1 --format=%H -S"| R<n> |"
# -- <that file>` non-empty (committed); and that same line present in the file at HEAD, so an
# APPROVED typed into the working tree over a committed unapproved row does not pass (at HEAD).
# Last line: `AUTHORIZED` (exit 0) or `FAILED: authorization mismatch — <the first rule that failed>`
# (exit 1). A bad call: `REFUSED: <reason>` on stderr, exit 1.
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_authorize.py only.

set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
PROMPTS="$REPO/docs/40 - DevDocs/prompts"
REPORTS_REL="docs/40 - DevDocs/reports"

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 2 ] || refuse "usage: authorize.sh <build|check|deploy> <card>"
case "$1" in
    build) hub=BUILD-HUB.md ;;
    check) hub=CHECK-HUB.md ;;
    deploy) hub=DEPLOY-HUB.md ;;
    *) refuse "kind '$1' is none of build, check, deploy" ;;
esac
fixed="$PROMPTS/$hub"
card=$2
[ -f "$fixed" ] || refuse "no fixed file: $fixed"
[ -f "$card" ] || refuse "no such card: $card"
case "$card" in
    "$REPO"/*) ;;
    *) refuse "the card is not under $REPO: $card" ;;
esac
case "$card" in
    *..*) refuse "the card path holds '..'" ;;
esac
card_rel=${card#"$REPO"/}

failed=""

# row <rule> <command> <exit> <output> <ok: 0 or 1>
row() {
    if [ -z "$4" ]; then
        res=nothing
    else
        res=$(printf '%s\n' "$4" | sed -n '1p')
    fi
    printf '%s · %s · %s · %s\n' "$1" "$2" "$3" "$res"
    if [ "$5" -ne 0 ] && [ -z "$failed" ]; then
        failed=$1
    fi
}

# field KEY → the value of the card's first "KEY: value" line, trailing blanks cut
field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}

# prove <label> <date> <R<n>>: the row, its commit, and the row at HEAD
prove() {
    label="$1 $2 $3"
    rel="$REPORTS_REL/cto-$2.md"
    file="$REPO/$rel"
    if [ -f "$file" ]; then
        out=$(grep -n "^| $3 " "$file")
        rc=$?
    else
        out="no such file: $file"
        rc=2
    fi
    ok=1
    line=""
    if [ "$rc" -eq 0 ] && [ "$(printf '%s\n' "$out" | wc -l | tr -d ' ')" -eq 1 ]; then
        case "$out" in
            *"HIS RULING"*APPROVED*) ok=0 ;;
        esac
        line=${out#*:}
    fi
    row "$label row" "grep -n \"^| $3 \" \"$file\"" "$rc" "$out" "$ok"

    out=$(git -C "$REPO" log -1 --format=%H -S"| $3 |" -- "$rel" 2>&1)
    rc=$?
    ok=1
    [ "$rc" -eq 0 ] && [ -n "$out" ] && ok=0
    row "$label committed" "git -C $REPO log -1 --format=%H -S\"| $3 |\" -- \"$rel\"" "$rc" "$out" "$ok"

    ok=1
    if [ -n "$line" ] && git -C "$REPO" show "HEAD:$rel" 2>/dev/null | grep -q -x -F -e "$line"; then
        ok=0
        out="the row as grepped"
    else
        out="the row as grepped is not in HEAD:$rel"
    fi
    row "$label at HEAD" "git -C $REPO show \"HEAD:$rel\"" "$ok" "$out" "$ok"
    # the at-HEAD miss is the commit's failure: name it so
    case "$failed" in
        "$label at HEAD") failed="$label committed" ;;
    esac
}

# rulings <label> <text>: every `<date> R<n>` of a RULINGS value
rulings() {
    date=""
    seen=""
    for t in $(printf '%s\n' "$2" | sed -e 's/·/ /g' -e 's/[,;]/ /g'); do
        case "$t" in
            20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) date=$t ;;
            R[0-9]*)
                case "$t" in
                    R*[!0-9]*) row "$1" "field RULINGS" 1 "unreadable token '$t' in: $2" 1; return ;;
                esac
                if [ -z "$date" ]; then
                    row "$1" "field RULINGS" 1 "R<n> before any date in: $2" 1
                    return
                fi
                prove "$1" "$date" "$t"
                seen=1
                ;;
            *) row "$1" "field RULINGS" 1 "unreadable token '$t' in: $2" 1; return ;;
        esac
    done
    [ -n "$seen" ] || row "$1" "field RULINGS" 1 "no <date> R<n> in: $2" 1
}

out=$(grep -n -E "«INSTAL[L]" "$fixed")
rc=$?
ok=1
[ "$rc" -eq 1 ] && ok=0
row INSTALLED "grep -n -E \"«INSTAL[L]\" \"$fixed\"" "$rc" "$out" "$ok"

out=$(grep -n -E "«FIL[L]" "$card")
rc=$?
ok=1
[ "$rc" -eq 1 ] && ok=0
row PLACEHOLDER "grep -n -E \"«FIL[L]\" \"$card\"" "$rc" "$out" "$ok"

out=$(git -C "$REPO" log -1 --format=%H -- "$card_rel" 2>&1)
rc=$?
ok=1
[ "$rc" -eq 0 ] && [ -n "$out" ] && ok=0
row "CARD COMMITTED" "git -C $REPO log -1 --format=%H -- \"$card_rel\"" "$rc" "$out" "$ok"

out=$(git -C "$REPO" diff --stat -- "$card_rel" 2>&1)
rc=$?
ok=1
[ "$rc" -eq 0 ] && [ -z "$out" ] && ok=0
row "CARD UNCHANGED" "git -C $REPO diff --stat -- \"$card_rel\"" "$rc" "$out" "$ok"

title=$(sed -n '1p' "$fixed")
sl=$(printf '%s\n' "$title" | sed -n 's/^[^«]*INSTALL: \(20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\) \(R[0-9][0-9]*\)[^0-9].*$/\1 \2/p')
if [ -z "$sl" ]; then
    row "STANDING LIST" "sed -n 1p \"$fixed\"" 1 "the title names no INSTALL: <date> R<n>: $title" 1
else
    prove "STANDING LIST" ${sl% *} ${sl#* }
fi

r=$(field RULINGS)
case "$r" in
    none) ;;
    "") row "RULING" "field RULINGS" 1 "RULINGS is empty" 1 ;;
    *) rulings RULING "$r" ;;
esac

for h in "HOUSE A" "HOUSE B"; do
    v=$(field "$h")
    case "$v" in
        *overruled*)
            o=$(printf '%s\n' "$v" | sed -n 's/^.*overruled \(20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\) \(R[0-9][0-9]*\)$/\1 \2/p')
            if [ -z "$o" ]; then
                row "$h overruled" "field $h" 1 "no 'overruled <date> R<n>' at the end of: $v" 1
            else
                prove "$h overruled" ${o% *} ${o#* }
            fi
            ;;
    esac
done

if [ -z "$failed" ]; then
    printf 'AUTHORIZED\n'
    exit 0
fi
printf 'FAILED: authorization mismatch — %s\n' "$failed"
exit 1
