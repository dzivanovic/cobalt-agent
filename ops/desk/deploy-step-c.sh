#!/bin/sh
# deploy-step-c.sh "<deploy card>" <m0> <BRANCH>
# deploy-step-c.sh --bootstrap-only "<deploy card>" com.cobalt.<label>
# deploy-step-c.sh --owed-clear "<deploy card>" com.cobalt.<label>
# DEPLOY-HUB.md STEP-C as one script (card 2026-10-13/496 plist-step-c, rows C1, DF1, BO1).
# No git write, no `launchctl`, no merge: the hub types `launchctl` at its step 4.6L from the
# strings desk-launch.sh generates (row L1), never this script. Its ONE named write is
# $REPO/data/deploy/bootstrap-owed.json (gitignored): written at step C for a `deferred` label,
# its entry removed by --owed-clear. Smoke K18 and the watchdog sweep read that file (row OW1).
#
# THE CARD'S LINES: the deploy card's `## LAUNCHD` (at most one section), one line per label:
#   com.cobalt.<label> · add|change|deferred · <build card path>:<row id> · dry run: <command>|none
#   a `deferred` line ends ` · gate: <item>, <item>, …` (the gate items owed before its bootstrap)
# <label> is [a-z0-9-]+; the build card path is `prompts/…-card.md` under `docs/40 - DevDocs/`,
# read from $REPO at `main`.
#
# STEP-C: `git -C $REPO diff --name-status <m0> <BRANCH> -- configs ops`; for each plist under ops/:
#   A or M under ops/desk/   today's exception, word for word (DEPLOY-HUB.md STEP-C): its Label
#                            string (on the <key>Label</key> line or the line after it) is no
#                            `label:` of configs/cobalt/jobs.yaml at <BRANCH> and the path is not
#                            ops/<label>.plist → `EXCEPTION: <path> — …`; a Label the read cannot
#                            find is refused
#   A or M at ops/com.cobalt.<label>.plist   admitted only when (1) a `## LAUNCHD` line names the
#                            label, (2) the status matches its mode (A: add or deferred; M: change),
#                            (3) the plist's Label string at <BRANCH> is com.cobalt.<label>, (4) the
#                            label is not agent, aset or radar, (5) the named build card row's
#                            `files` cell names ops/com.cobalt.<label>.plist
#   D anywhere under ops/    `RETIRE OWED: <label>` (the hub records it)
#   any other plist, status  refused
#   A `## LAUNCHD` line whose label the diff neither adds nor changes is refused (card and tree
#   disagree). Out: one line per plist `ADMITTED: com.cobalt.<label> · add|change` (a deferred one
#   `… · add · deferred`, then `BOOTSTRAP OWED: com.cobalt.<label> — <gate items>`) or
#   `REFUSED: <path> — <reason>`; last line `STEP-C: ADMITTED <n>` (exit 0) or
#   `FAILED: C — <paths>: installing or changing a launchd job is not on this list; the desk runs it
#   as its own job · rollback: not used` (exit 1). The owed file is written only on exit 0.
#
# --bootstrap-only (row BO1): no diff, no merge. ADMITTED only when the card's `## LAUNCHD` names
#   the label `add`, the plist on `main` carries that Label, the owed file lists the label, and the
#   card holds one column-0 line `GATE RESULT: com.cobalt.<label> · <item> · <result>` for every
#   gate item the owed file lists. Out: `ADMITTED: com.cobalt.<label> · bootstrap-only` and
#   `STEP-C: ADMITTED 1` (exit 0), or `REFUSED: …` and `FAILED: BO — …` (exit 1).
# --owed-clear: after the hub's 4.6L print found the label loaded: the card names the label and the
#   owed file lists it → its entry removed, `OWED CLEARED: com.cobalt.<label>` (exit 0).
# A bad call: `REFUSED: <reason>` on stderr, exit 1.
#
# COBALT_REPO_ROOT stands in for /Users/cobalt/cobalt in tests/ops/test_deploy_step_c.py only.

export LC_ALL=C
set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
OWED="$REPO/data/deploy/bootstrap-owed.json"
DEVDOCS="docs/40 - DevDocs"
FAILTEXT='installing or changing a launchd job is not on this list; the desk runs it as its own job · rollback: not used'
TAB=$(printf '\t')

die() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

usage='usage: deploy-step-c.sh "<deploy card>" <m0> <BRANCH> | --bootstrap-only|--owed-clear "<deploy card>" com.cobalt.<label>'
mode=stepc
case "${1:-}" in
    --bootstrap-only) mode=bo; shift ;;
    --owed-clear) mode=clear; shift ;;
    -*) die "unknown option '$1'; $usage" ;;
esac
if [ "$mode" = stepc ]; then
    [ "$#" -eq 3 ] || die "$usage"
    card=$1 m0=$2 branch=$3
    case "$m0$branch" in
        *[!A-Za-z0-9._/-]*|-*|*..*) die "<m0> '$m0' or <BRANCH> '$branch' is not a plain ref" ;;
    esac
else
    [ "$#" -eq 2 ] || die "$usage"
    card=$1 want=$2
    case "$want" in
        com.cobalt.*) ;;
        *) die "the label '$want' is not com.cobalt.<label>" ;;
    esac
    case "${want#com.cobalt.}" in
        ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*) die "the label '$want' is not com.cobalt.<[a-z0-9-]+>" ;;
    esac
fi
[ -f "$card" ] || die "no such card: $card"
case "$card" in
    *'"'*|*'\'*) die "the card path holds a quote or a backslash: $card" ;;
esac
[ "$(grep -c '^## LAUNCHD' "$card")" -le 1 ] || die "the card holds more than one '## LAUNCHD' section"

# the card's `## LAUNCHD` lines, parsed and shape-checked, one per line:
#   OK<TAB>label<TAB>mode<TAB>build card path<TAB>row<TAB>dry run<TAB>gate   or   BAD<TAB>line<TAB>reason
launchd=$(awk '/^## /{on = ($0 == "## LAUNCHD"); next} on && NF' "$card" | awk -F ' · ' '
{
    l = $0; sub(/^- /, "", l)
    n = split(l, f, / · /)
    lab = f[1]; mode = f[2]; ref = f[3]; dry = f[4]; gate = (n == 5) ? f[5] : ""
    bad = ""
    if (n < 4 || n > 5) bad = "not four or five fields separated by \" · \""
    else if (lab !~ /^com\.cobalt\.[a-z0-9-]+$/) bad = "label is not com.cobalt.<[a-z0-9-]+>"
    else if (seen[lab]++) bad = "label repeated"
    else if (mode != "add" && mode != "change" && mode != "deferred") bad = "mode is not add, change or deferred"
    else if (ref !~ /^prompts\/[A-Za-z0-9._\/-]+-card\.md:[A-Za-z0-9]+$/ || ref ~ /\.\./) bad = "build card is not prompts/<…>-card.md:<row>"
    else if (dry != "dry run: none" && dry !~ /^dry run: COBALT_ENV=production uv run [a-z0-9-]+( [a-z0-9-]+)?( [a-z0-9-]+)?( [a-z0-9-]+)? --dry-run$/) bad = "dry run is not none or COBALT_ENV=production uv run <1-4 words> --dry-run"
    else if (mode == "deferred" && gate !~ /^gate: [A-Za-z0-9 ._-]+(, [A-Za-z0-9 ._-]+)*$/) bad = "a deferred line ends \" · gate: <item>, <item>\""
    else if (mode != "deferred" && n == 5) bad = "only a deferred line carries a gate field"
    if (bad != "") { print "BAD\t" $0 "\t" bad; next }
    k = index(ref, ":"); sub(/^gate: /, "", gate)
    print "OK\t" lab "\t" mode "\t" substr(ref, 1, k - 1) "\t" substr(ref, k + 1) "\t" dry "\t" gate
}')

# card_field <label> <n>: the n-th field of the label's OK line (2 label, 3 mode, 4 path, 5 row, 7 gate)
card_field() {
    printf '%s\n' "$launchd" | awk -F "$TAB" -v l="$1" -v i="$2" '$1 == "OK" && $2 == l {print $i}'
}

# plist_label <rev> <path>: the <string> on the <key>Label</key> line or the line after it
plist_label() {
    git -C "$REPO" show "$1:$2" 2>/dev/null | awk '
        !done && f { if (match($0, /<string>[^<]*<\/string>/)) { print substr($0, RSTART + 8, RLENGTH - 17); done = 1 } f = 0; next }
        !done && /<key>Label<\/key>/ {
            rest = $0; sub(/.*<key>Label<\/key>/, "", rest)
            if (match(rest, /<string>[^<]*<\/string>/)) { print substr(rest, RSTART + 8, RLENGTH - 17); done = 1 } else f = 1
        }'
}

# row_files <build card path> <row>: the last cell of the row `| <row> | …` in the card at main
row_files() {
    git -C "$REPO" show "main:$DEVDOCS/$1" 2>/dev/null | awk -F '|' -v r="$2" '
        { c = $2; gsub(/^[ \t]+|[ \t]+$/, "", c) }
        c == r { for (i = NF; i > 0; i--) { v = $i; gsub(/^[ \t]+|[ \t]+$/, "", v); if (v != "") { print v; exit } } }'
}

# owed_entries: the owed file's entry lines (one label per line), or nothing
owed_entries() {
    [ -f "$OWED" ] || return 0
    grep '^  "com\.cobalt\.[a-z0-9-]*": ' "$OWED" | sed 's/,$//'
}

# owed_write <entries>: the owed file from entry lines, commas between, one write
owed_write() {
    mkdir -p "$REPO/data/deploy" || die "cannot make $REPO/data/deploy"
    printf '%s\n' "$1" | awk 'NF { e[++n] = $0 } END {
        print "{"; for (i = 1; i <= n; i++) print e[i] (i < n ? "," : ""); print "}" }' > "$OWED.tmp" \
        && mv "$OWED.tmp" "$OWED" || die "cannot write $OWED"
}

refused=""
paths=""
refuse_path() {
    printf 'REFUSED: %s — %s\n' "$1" "$2"
    refused=1
    case " $paths " in
        *" $1 "*) ;;
        *) paths="${paths:+$paths }$1" ;;
    esac
}

# BAD lines are refused in every mode
bads=$(printf '%s\n' "$launchd" | awk -F "$TAB" '$1 == "BAD" {print $2 "\t" $3}')
if [ -n "$bads" ]; then
    while IFS="$TAB" read -r bl br; do
        refuse_path "## LAUNCHD $bl" "$br"
    done <<EOF
$bads
EOF
fi

if [ "$mode" != stepc ]; then
    entry=$(owed_entries | grep -F "\"$want\": " || true)
    [ -n "$(card_field "$want" 2)" ] || refuse_path "$want" "the card's ## LAUNCHD names no line for this label"
    [ -n "$entry" ] || refuse_path "$want" "data/deploy/bootstrap-owed.json does not list this label"
    if [ "$mode" = bo ] && [ -z "$refused" ]; then
        [ "$(card_field "$want" 3)" = add ] || refuse_path "$want" "a bootstrap-only line's mode is add"
        [ "$(plist_label main "ops/$want.plist")" = "$want" ] \
            || refuse_path "$want" "ops/$want.plist on main does not carry Label $want"
        items=$(printf '%s\n' "$entry" | sed -n 's/.*"gate": \[\(.*\)\].*/\1/p' \
            | awk '{ n = split($0, a, /", "/); for (i = 1; i <= n; i++) { v = a[i]; gsub(/"/, "", v); print v } }')
        [ -n "$items" ] || refuse_path "$want" "the owed entry lists no gate item"
        while IFS= read -r it; do
            [ -n "$it" ] || continue
            # a column-0 line with a non-empty result after the item
            awk -v p="GATE RESULT: $want · $it · " 'index($0, p) == 1 && length($0) > length(p) {f = 1} END {exit !f}' "$card" \
                || refuse_path "$want" "no recorded result for gate item '$it' (GATE RESULT: $want · $it · <result>)"
        done <<EOF
$items
EOF
    fi
    if [ -n "$refused" ]; then
        printf 'FAILED: BO — %s: the bootstrap is refused · rollback: not used\n' "$want"
        exit 1
    fi
    if [ "$mode" = bo ]; then
        printf 'ADMITTED: %s · bootstrap-only\n' "$want"
        printf 'STEP-C: ADMITTED 1\n'
        exit 0
    fi
    owed_write "$(owed_entries | grep -v -F "\"$want\": ")"
    printf 'OWED CLEARED: %s\n' "$want"
    exit 0
fi

# ---- STEP-C ---------------------------------------------------------------------------------
diff=$(git -C "$REPO" diff --name-status "$m0" "$branch" -- configs ops 2>&1) \
    || { printf 'FAILED: C — git diff %s %s exit — %s · rollback: not used\n' "$m0" "$branch" "$diff"; exit 1; }
jobs_labels=$(git -C "$REPO" show "$branch:configs/cobalt/jobs.yaml" 2>/dev/null \
    | sed -n 's/^[[:space:]]*-[[:space:]]*label:[[:space:]]*//p' | tr -d "\"'" | sed 's/[[:space:]]*$//')
admitted=0
touched=" "
owed_new=""

while IFS="$TAB" read -r st path rest; do
    [ -n "$st" ] || continue
    case "$path" in
        ops/*.plist) ;;
        *) continue ;;
    esac
    case "$st" in
        D)
            case "$path" in
                ops/com.cobalt.*.plist) lab=${path#ops/}; lab=${lab%.plist} ;;
                *) lab=$(plist_label "$m0" "$path"); [ -n "$lab" ] || lab=$path ;;
            esac
            printf 'RETIRE OWED: %s\n' "$lab"
            continue
            ;;
        A|M) ;;
        *) refuse_path "$path" "status $st: only an added (A) or modified (M) plist is read"; continue ;;
    esac
    case "$path" in
        ops/desk/*)
            lab=$(plist_label "$branch" "$path")
            if [ -z "$lab" ]; then
                refuse_path "$path" "no Label string found"
            elif printf '%s\n' "$jobs_labels" | grep -q -x -F -e "$lab"; then
                refuse_path "$path" "Label $lab is a label: of configs/cobalt/jobs.yaml"
            elif [ "$path" = "ops/$lab.plist" ]; then
                refuse_path "$path" "path is ops/<label>.plist"
            else
                printf 'EXCEPTION: %s — ops/desk, Label %s is no jobs.yaml label (not a launchd job of this list)\n' "$path" "$lab"
            fi
            continue
            ;;
        ops/com.cobalt.*.plist)
            name=${path#ops/com.cobalt.}; name=${name%.plist}
            case "$name" in
                ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*)
                    refuse_path "$path" "label is not [a-z0-9-]+"; continue ;;
            esac
            ;;
        *) refuse_path "$path" "a plist outside ops/desk/ and ops/com.cobalt.<label>.plist"; continue ;;
    esac
    want="com.cobalt.$name"
    touched="$touched$want "
    lmode=$(card_field "$want" 3)
    if [ -z "$lmode" ]; then
        refuse_path "$path" "no ## LAUNCHD line names $want"
        continue
    fi
    case "$st:$lmode" in
        A:add|A:deferred|M:change) ;;
        *) refuse_path "$path" "diff status $st does not match the line's mode $lmode"; continue ;;
    esac
    got=$(plist_label "$branch" "$path")
    if [ "$got" != "$want" ]; then
        refuse_path "$path" "its Label string is '${got:-not found}', not $want"
        continue
    fi
    case "$name" in
        agent|aset|radar) refuse_path "$path" "$want is a resident STEP-R's gate keeps"; continue ;;
    esac
    cpath=$(card_field "$want" 4)
    crow=$(card_field "$want" 5)
    files=$(row_files "$cpath" "$crow")
    case "$files" in
        *"$path"*) ;;
        *) refuse_path "$path" "build card $cpath (main) row $crow's files cell does not name $path"; continue ;;
    esac
    admitted=$((admitted + 1))
    if [ "$lmode" = deferred ]; then
        printf 'ADMITTED: %s · add · deferred\n' "$want"
        gate=$(card_field "$want" 7)
        printf 'BOOTSTRAP OWED: %s — %s\n' "$want" "$gate"
        items=$(printf '%s' "$gate" | sed 's/, /", "/g')
        owed_new="$owed_new
  \"$want\": {\"gate\": [\"$items\"], \"card\": \"$card\"}"
    else
        printf 'ADMITTED: %s · %s\n' "$want" "$([ "$st" = A ] && echo add || echo change)"
    fi
done <<EOF
$diff
EOF

# a line whose label the diff neither adds nor changes: card and tree disagree
for lab in $(printf '%s\n' "$launchd" | awk -F "$TAB" '$1 == "OK" {print $2}'); do
    case "$touched" in
        *" $lab "*) ;;
        *) refuse_path "ops/$lab.plist" "## LAUNCHD names $lab but the diff neither adds nor changes ops/$lab.plist" ;;
    esac
done

if [ -n "$refused" ]; then
    printf 'FAILED: C — %s: %s\n' "$paths" "$FAILTEXT"
    exit 1
fi
if [ -n "$owed_new" ]; then
    keep=$(owed_entries)
    for lab in $(printf '%s\n' "$owed_new" | sed -n 's/^  "\(com\.cobalt\.[a-z0-9-]*\)": .*/\1/p'); do
        keep=$(printf '%s\n' "$keep" | grep -v -F "\"$lab\": " || true)
    done
    owed_write "$keep$owed_new"
fi
printf 'STEP-C: ADMITTED %s\n' "$admitted"
exit 0
