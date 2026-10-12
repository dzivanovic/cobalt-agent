#!/bin/sh
# authorize.sh <build|check|deploy|shadow|prodwrite> "<card>" — the AUTHORIZATION block of the kind's
# fixed file (BUILD-HUB.md, CHECK-HUB.md, DEPLOY-HUB.md, SHADOW-HUB.md or PRODWRITE-HUB.md) run as ONE
# call (card 19 worker-steps S1; shadow: card 2026-10-11 324 S4; prodwrite: card 2026-10-12 392 W4).
# Read-only.
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
#                        every column-0 HOUSE line that ends `overruled <date> R<n>`
#   HOUSE A OpenAI <date> R<n> row|committed|at HEAD
#                        a HOUSE A line `OpenAI — his <date> R<n>` (the Sol probe, his OpenAI meter)
#   WRITE RULING <date> R<n> row|committed|at HEAD
#                        kind prodwrite only: the card's ONE `WRITE RULING: <date> R<n>` (the ruling
#                        that names its production write, K3); absent or empty fails as `WRITE RULING`
#   SQL FILE committed|SQL FILE unchanged|SQL SHA256|SQL CARD BLOCK
#                        kind prodwrite, when the card's ONE `## ROWS` command is a `db apply` (card
#                        2026-10-12 417 K2): the file `prompts/<last word>` is committed, unchanged
#                        since, its `shasum -a 256` is the command's `--sha256`, and it is byte-equal
#                        to the card's ONE `## SQL` block (a line ```sql, the lines, a line ```)
# A row `<date> R<n>` is proved by: `grep -n "^| R<n> " $REPO/docs/40 - DevDocs/reports/cto-<date>.md`
# → ONE line holding `HIS RULING` and `APPROVED` (row); `git -C $REPO log -1 --format=%H -S"| R<n> |"
# -- <that file>` non-empty (committed); and that same line present in the file at HEAD, so an
# APPROVED typed into the working tree over a committed unapproved row does not pass (at HEAD).
# Last line: `AUTHORIZED` (exit 0) or `FAILED: authorization mismatch — <the first rule that failed>`
# (exit 1). A bad call: `REFUSED: <reason>` on stderr, exit 1.
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_authorize.py only.

export LC_ALL=C
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

[ "$#" -eq 2 ] || refuse "usage: authorize.sh <build|check|deploy|shadow|prodwrite> <card>"
kind=$1
case "$1" in
    build) hub=BUILD-HUB.md ;;
    check) hub=CHECK-HUB.md ;;
    deploy) hub=DEPLOY-HUB.md ;;
    # card 2026-10-11 324 S4: the shadow gate seat, its rows as build's
    shadow) hub=SHADOW-HUB.md ;;
    # card 2026-10-12 392 W4: the production-write seat, its rows as deploy's plus WRITE RULING
    prodwrite) hub=PRODWRITE-HUB.md ;;
    *) refuse "kind '$1' is none of build, check, deploy, shadow, prodwrite" ;;
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
# the first `INSTALL: <date> R<n>` with no `«` before it; read by byte (LC_ALL=C: a bracket
# `[^«]` would be two one-byte members, and the `·` before INSTALL shares one of them)
sl=$(printf '%s\n' "$title" | awk '{
    i = index($0, "INSTALL: ")
    if (i == 0 || index(substr($0, 1, i - 1), "«") > 0) exit
    rest = substr($0, i + 9)
    if (match(rest, /^20[0-9][0-9]-[0-9][0-9]-[0-9][0-9] R[0-9]+[^0-9]/))
        print substr(rest, 1, 10) " " substr(rest, 12, RLENGTH - 12)
}')
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

# every column-0 `HOUSE A:` / `HOUSE B:` line of the whole card, not only `field`'s first, so a
# first `HOUSE A: OpenAI…` line hides no later overrule from the proof (card 298 check O1)
for h in "HOUSE A" "HOUSE B"; do
    IFS='
'
    set -- $(sed -n "s/^$h: *//p" "$card" | sed 's/[[:space:]]*$//')
    unset IFS
    for v in "$@"; do
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
done

# every column-0 `HOUSE A: OpenAI…` line of the whole card (not only the first HOUSE A line, as
# `field` reads), each proved like a ruling; a tail, no `his` or `overruled` fails (card 298 S4)
IFS='
'
set -- $(sed -n 's/^HOUSE A: *\(OpenAI.*\)$/\1/p' "$card" | sed 's/[[:space:]]*$//')
unset IFS
for v in "$@"; do
    o=$(printf '%s\n' "$v" | sed -n 's/^OpenAI — his \(20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\) \(R[0-9][0-9]*\)$/\1 \2/p')
    if [ -z "$o" ]; then
        row "HOUSE A OpenAI" "field HOUSE A" 1 "no 'OpenAI — his <date> R<n>' alone on the line: $v" 1
    else
        prove "HOUSE A OpenAI" ${o% *} ${o#* }
    fi
done

# kind prodwrite (card 392 W4): the ONE ruling that names the write, proved as every RULINGS row
if [ "$kind" = "prodwrite" ]; then
    w=$(field "WRITE RULING")
    o=$(printf '%s\n' "$w" | sed -n 's/^\(20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\) \(R[0-9][0-9]*\)$/\1 \2/p')
    if [ "$(grep -c '^WRITE RULING:' "$card")" -ne 1 ]; then
        row "WRITE RULING" "field WRITE RULING" 1 "not ONE 'WRITE RULING:' line in the card" 1
    elif [ -z "$o" ]; then
        row "WRITE RULING" "field WRITE RULING" 1 "WRITE RULING is not '<date> R<n>': '$w'" 1
    else
        prove "WRITE RULING" ${o% *} ${o#* }
    fi
fi

# kind prodwrite, a `db apply` card (card 2026-10-12 417 K2): its file re-proved as the launcher
# proves it (desk-launch.sh prodwrite arm) — committed, unchanged, its sha256 the command's, and
# byte-equal to the card's ONE `## SQL` block. The ONE `## ROWS` command is read as the launcher
# reads it; a card of any other verb prints no SQL row.
if [ "$kind" = "prodwrite" ]; then
    wrows=$(awk '/^## /{insec = ($0 ~ /^## ROWS[ \t]*$/); next}
        insec && /^[|]/ {
            gsub(/\\[|]/, "\001")
            if ($0 ~ /^[|][ \t:|-]*$/) next
            split($0, c, "|"); h = c[3]; gsub(/^[ \t]+|[ \t]+$/, "", h)
            if (h == "command") next
            print
        }' "$card")
    wcmd=""
    if [ -n "$wrows" ] && [ "$(printf '%s\n' "$wrows" | grep -c '')" -eq 1 ]; then
        wcmd=$(printf '%s\n' "$wrows" | awk -F'|' '{print $3}' | tr -d '`' | tr '\001' '|' \
            | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')
    fi
    wverb=${wcmd#"COBALT_ENV=production uv run cobalt "}
    if [ "$wverb" != "$wcmd" ] && [ "$(printf '%s\n' "$wverb" | awk '{print $1 " " $2}')" = "db apply" ]; then
        sql_file=$(printf '%s\n' "$wverb" | awk '{print $NF}')
        sql_sha=$(printf '%s\n' "$wverb" | awk '{for (i = 1; i < NF; i++) if ($i == "--sha256") {print $(i + 1); exit}}')
        sql_rel="docs/40 - DevDocs/prompts/$sql_file"
        sql_path="$REPO/$sql_rel"

        out=$(git -C "$REPO" log -1 --format=%H -- "$sql_rel" 2>&1)
        rc=$?
        ok=1
        [ "$rc" -eq 0 ] && [ -n "$out" ] && ok=0
        # committed means in HEAD: a path deleted there and written back untracked is not (check 417 A2)
        git -C "$REPO" cat-file -e "HEAD:$sql_rel" 2>/dev/null || { ok=1; out="$out (not in HEAD)"; }
        row "SQL FILE committed" "git -C $REPO log -1 --format=%H -- \"$sql_rel\"" "$rc" "$out" "$ok"

        # unchanged against HEAD, so a staged edit is a change (check 417 O3)
        out=$(git -C "$REPO" diff --stat HEAD -- "$sql_rel" 2>&1)
        rc=$?
        ok=1
        [ "$rc" -eq 0 ] && [ -z "$out" ] && [ -f "$sql_path" ] && ok=0
        [ -f "$sql_path" ] || out="no such file: $sql_path"
        row "SQL FILE unchanged" "git -C $REPO diff --stat HEAD -- \"$sql_rel\"" "$rc" "$out" "$ok"

        out=$(shasum -a 256 "$sql_path" 2>&1)
        rc=$?
        ok=1
        [ "$rc" -eq 0 ] && [ -n "$sql_sha" ] && [ "${out%% *}" = "$sql_sha" ] && ok=0
        [ "$ok" -eq 0 ] || out="$out (the command's --sha256: ${sql_sha:-none})"
        row "SQL SHA256" "shasum -a 256 \"$sql_path\"" "$rc" "$out" "$ok"

        shape=$(awk '!fence && /^## / {insec = ($0 ~ /^## SQL[ \t]*$/); if (insec) secs++; next}
            insec && /^```/ {fences++; if (fences == 1) opener = $0; else closer = $0; fence = !fence}
            END {print ((secs == 1 && fences == 2 && opener == "```sql" && closer == "```") ? "one" : "not one")}' "$card")
        ok=1
        if [ "$shape" != "one" ]; then
            out="the card's ## SQL section is not ONE fenced sql block"
        elif awk '!fence && /^## / {insec = ($0 ~ /^## SQL[ \t]*$/); next}
                insec && /^```/ {fence = !fence; next}
                insec && fence {print}' "$card" | cmp -s - "$sql_path"; then
            ok=0
            out="the card's ## SQL block is the file byte for byte"
        else
            out="the card's ## SQL block is not the file byte for byte"
        fi
        row "SQL CARD BLOCK" "awk <the card's ## SQL block> | cmp -s - \"$sql_path\"" "$ok" "$out" "$ok"
    fi
fi

if [ -z "$failed" ]; then
    printf 'AUTHORIZED\n'
    exit 0
fi
printf 'FAILED: authorization mismatch — %s\n' "$failed"
exit 1
