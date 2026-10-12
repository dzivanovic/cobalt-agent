#!/bin/sh
# deploy-card.sh --job <name> --set <word> --worktree <dir> --tag <tag> --out "<new card path>" [--tickers "<A,B,…>"]
#                [--rulings "<list>"] [--fix-report "<job>=<fix report path>"]… "<job card>" …
# Writes ONE new file, the deploy card at --out, in the format of prompts/CARD.md, from checked
# job cards, in the order given (card 18 desk-tools-b, row B1; DEPLOY-HUB.md STEP-0 P2 and P3).
# Per job card it reads JOB, LADDER, BRANCH and CHECK REPORT; the code tip is the `tip:` of that
# check report's last non-blank line; the branch head is `git -C $REPO rev-parse --short=8 <BRANCH>`.
# REFUSED (exit 1, nothing written), naming the job and the reason, when: the check report is
# absent, not committed, or modified since its commit; its last line lacks `held unfixed: 0` or
# `ready: YES`, or names no tip; the code tip is not an ancestor of the head; the head adds
# anything outside docs/ past the code tip. A fix round (R376, L75; CARD.md :48; launcher-1010 row A,
# R810): `--fix-report "<job>=<path>"` names that job's fix report under $REPORTS, read at the
# branch head (`git show <head>:<rel>`, never a copy on main); its last line `BUILT · … tip: <hex>`
# gives the row's code tip, the check's tip its ancestor, and the path fills the `fix report`
# cell. REFUSED: an empty value, a job no card names, a path outside $REPORTS/*.md or holding
# '|' or a backtick (the cell's own characters), a report absent at the head,
# a last line not `BUILT ·` with a `tip:`, a check tip not an ancestor of the fix tip; the head
# rules above then read against the fix tip. A held check (card 317, R993): with a --fix-report, a
# last line carrying `held unfixed: <n>`, n >= 1, is read by THE RULE below (one FIXED or CARRIED
# line per held id) and its row carries `held unfixed: <n>` and `ready: NO`; without one it is
# refused as above. Also refused: an --out path that exists, a worktree
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

usage="usage: deploy-card.sh --job <name> --set <word> --worktree <dir> --tag <tag> --out \"<new card path>\" [--rulings \"<list>\"] [--tickers \"<A,B,…>\"] [--fix-report \"<job>=<fix report path>\"]… \"<job card>\" …"
name="" set="" wt="" tag="" out="" rulings="none" tickers="none" fixes=""
while [ "$#" -gt 0 ]; do
    case "$1" in
        --job) [ "$#" -ge 2 ] || refuse "$usage"; name=$2; shift 2 ;;
        --set) [ "$#" -ge 2 ] || refuse "$usage"; set=$2; shift 2 ;;
        --worktree) [ "$#" -ge 2 ] || refuse "$usage"; wt=$2; shift 2 ;;
        --tag) [ "$#" -ge 2 ] || refuse "$usage"; tag=$2; shift 2 ;;
        --out) [ "$#" -ge 2 ] || refuse "$usage"; out=$2; shift 2 ;;
        --rulings) [ "$#" -ge 2 ] || refuse "$usage"; rulings=$2; shift 2 ;;
        --tickers) [ "$#" -ge 2 ] || refuse "$usage"; tickers=$2; shift 2 ;;
        --fix-report) [ "$#" -ge 2 ] || refuse "$usage"
            case "$2" in *"$nl"*) refuse "--fix-report holds a line break" ;; esac
            [ -n "$2" ] || refuse "--fix-report '' must be <job>=<fix report path>"
            fixes="$fixes$2$nl"; shift 2 ;;
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
# card 63 N8: the build's --tickers for the gate's stray-row read, gate.sh's own pattern (:100)
case "$tickers" in
    none) ;;
    ""|,*|*,|*,,*|*[!A-Z0-9.,]*) refuse "--tickers '$tickers' must be none or A,B,… of [A-Z0-9.]" ;;
esac
# launcher-1010 row A: each --fix-report is <job>=<a report under $REPORTS>, one per job
fixjobs=""
while IFS= read -r fx; do
    [ -n "$fx" ] || continue
    fjob=${fx%%=*}
    fpath=${fx#*=}
    [ "$fjob" != "$fx" ] || refuse "--fix-report '$fx' must be <job>=<fix report path>"
    case "$fjob" in
        ""|*[!abcdefghijklmnopqrstuvwxyz0123456789-]*|-*) refuse "--fix-report job '$fjob' must be [a-z0-9-]" ;;
    esac
    case " $fixjobs " in
        *" $fjob "*) refuse "--fix-report names job '$fjob' twice" ;;
    esac
    case "$fpath" in
        *..*) refuse "$fjob: --fix-report path holds '..': $fpath" ;;
        # the path is a backticked cell of the SHIPS row: '|' or '`' would split or reshape it
        *'|'*|*'`'*) refuse "$fjob: --fix-report path holds '|' or a backtick: $fpath" ;;
        "$REPORTS"/*.md) ;;
        *) refuse "$fjob: --fix-report path is not $REPORTS/<name>.md: $fpath" ;;
    esac
    fixjobs="${fixjobs:+$fixjobs }$fjob"
done <<FIXES
$fixes
FIXES
{ [ -e "$out" ] || [ -L "$out" ]; } && refuse "--out exists: $out (this script writes a new card only)"
[ -d "$(dirname "$out")" ] || refuse "--out's folder does not exist: $(dirname "$out")"
git -C "$REPO" rev-parse --verify --quiet "refs/heads/main^{commit}" >/dev/null || refuse "no branch main in $REPO"

# field <file> KEY -> the value of the first "KEY: value" line, trailing blanks cut (desk-launch.sh's)
field() {
    sed -n "s/^$2: *//p" "$1" | sed -n '1p' | sed 's/[[:space:]]*$//'
}

# ---- THE RULE (card 317 held-closed-1010, R993): a held check ships on its fix round ---------
# One text, byte for byte, in deploy-card.sh, desk-launch.sh and deploy-step0.sh (pinned by
# tests/ops/test_deploy_card.py). held_n <line>: the n of the line's `held unfixed: <n>` when
# n >= 1 (an exact number: `held unfixed: 10` is 10), else nothing.
# held_rule <who> <check report> <its last line> <code tip> <branch head> <fix report or ''>:
# the line carries `ready: NO` and `open: <m>`, m >= n. The held ids (card 397, R1157) are the
# union, each id counted once, of `## RUNS` lines `- <id> · … HELD, NOT FIXED …` and table rows
# `| <id> | … | <verdict> |` whose last cell holds `**HELD**`, and of `## FIXES` lines
# `- <id>: … HELD, NOT FIXED …` (from column 0; the id trimmed, [A-Za-z0-9._-]+); a `## RUNS`
# bullet whose verdict is `**HELD**` alone is not one. There are exactly n, and an id twice in
# one section is refused. The fix report lies under the reports folder, is read at
# the branch head and ends `BUILT · … tip: <code tip>`; it holds, from column 0, exactly ONE line
# per held id, `FIXED: <id> — <test id>` or `CARRIED: <id> — <test id> — R<n>`, and none for an
# id the check does not list (<test id> = tests/<path>.py::<name>). A FIXED test exists at the
# code tip with no xfail (no decorator of its def, no `pytestmark`); a CARRIED test exists there
# with a decorator holding `xfail` and `strict=True`. When m > n it also holds exactly one line
# `SETTLED: <id> — R<n>` for each of m - n distinct ids, each a `## RUNS` bullet or table row
# whose verdict starts `REJECTED` or `UNSETTLED`, never a held id; a SETTLED line is no FIXED or
# CARRIED line. The R<n> of a CARRIED or SETTLED line is a `| R<n> |` row carrying `DESK RECORD`:
# the first such row of the `reports/cto-<date>.md` files at HEAD dated on or after the check
# report's date (<date> from its file name), read newest first (R1160).
# A static read: no test is run. The first refusal sets held_why (naming <who> and the id) and
# returns 1; the check report is never written.
held_n() {
    printf '%s\n' "$1" | grep -o -E '(^| )held unfixed: [0-9]+( |$)' | sed -n '1p' \
        | sed -e 's/^ *held unfixed: //' -e 's/ *$//' | grep -E '^[1-9][0-9]*$'
}
# held_row <R<n>> -> the `| R<n> |` line of the newest desk report in hr_ctos holding one, or nothing
held_row() {
    printf '%s\n' "$hr_ctos" | while IFS= read -r hr_cto; do
        [ -n "$hr_cto" ] || continue
        hr_hit=$(git -C "$REPO" show "HEAD:${hr_reports#"$REPO"/}/$hr_cto" 2>/dev/null \
            | awk -v r="| $1 |" 'index($0, r) == 1' | sed -n '1p')
        if [ -n "$hr_hit" ]; then
            printf '%s\n' "$hr_hit"
            break
        fi
    done
}
held_rule() {
    hr_who=$1 hr_check=$2 hr_last=$3 hr_tip=$4 hr_head=$5 hr_frep=$6
    held_why=""
    hr_reports="$REPO/docs/40 - DevDocs/reports"
    hr_n=$(held_n "$hr_last")
    hr_runs=$(awk '/^## /{on = ($0 == "## RUNS"); next}
        on && /^- [A-Za-z0-9._-]+ · / && index($0, "HELD, NOT FIXED") {sub(/^- /, ""); sub(/ · .*/, ""); print}
        on && /^[|]/ {n = split($0, c, "|"); id = c[2]; v = c[n]; if (n > 2 && v ~ /^[ \t]*$/) v = c[n - 1]
            sub(/^[ \t]+/, "", id); sub(/[ \t]+$/, "", id); if (id ~ /^[A-Za-z0-9._-]+$/ && index(v, "**HELD**")) print id}' "$hr_check")
    hr_fixes=$(awk '/^## /{on = ($0 == "## FIXES"); next}
        on && /^- [A-Za-z0-9._-]+: / && index($0, "HELD, NOT FIXED") {sub(/^- /, ""); sub(/: .*/, ""); print}' "$hr_check")
    # the ids of `## RUNS`, then those of `## FIXES` that `## RUNS` does not name
    hr_ids=$({ printf '%s\n' "$hr_runs" | sed 's/^/R /'; printf '%s\n' "$hr_fixes" | sed 's/^/F /'; } \
        | awk '$2 == "" {next} $1 == "R" {r[$2] = 1; print $2; next} !r[$2] {print $2}')
    hr_k=$(printf '%s\n' "$hr_ids" | grep -c .)
    hr_list=$(printf '%s\n' "$hr_ids" | grep . | tr '\n' ' ' | sed 's/ *$//')
    hr_list=${hr_list:-none}
    hr_where="## RUNS"
    [ -z "$hr_fixes" ] || hr_where="## RUNS and ## FIXES"
    hr_m=$(printf '%s\n' "$hr_last" | grep -o -E '(^| )open: [0-9]+( |$)' | sed -n '1p' \
        | sed -e 's/^ *open: //' -e 's/ *$//' -e 's/^0*\([0-9]\)/\1/')
    if ! printf '%s\n' "$hr_last" | grep -q -E '(^| )ready: NO( |$)'; then
        held_why="$hr_who: the check's last line says 'held unfixed: $hr_n' (held ids: $hr_list) but not 'ready: NO': $hr_last"
        return 1
    fi
    if [ -z "$hr_m" ] || [ "$hr_m" -lt "$hr_n" ]; then
        held_why="$hr_who: the check's last line says 'held unfixed: $hr_n' (held ids: $hr_list) but not 'open: $hr_n': $hr_last"
        return 1
    fi
    if [ "$hr_k" != "$hr_n" ]; then
        held_why="$hr_who: the check $hr_check lists $hr_k HELD, NOT FIXED row(s) under $hr_where ($hr_list), its last line says 'held unfixed: $hr_n'"
        return 1
    fi
    if [ -n "$(printf '%s\n' "$hr_runs" | grep . | sort | uniq -d)" ]; then
        held_why="$hr_who: the check $hr_check lists a held id twice under ## RUNS ($hr_list)"
        return 1
    fi
    if [ -n "$(printf '%s\n' "$hr_fixes" | grep . | sort | uniq -d)" ]; then
        held_why="$hr_who: the check $hr_check lists a held id twice under ## FIXES ($hr_list)"
        return 1
    fi
    if [ -z "$hr_frep" ]; then
        held_why="$hr_who: held id $(printf '%s\n' "$hr_ids" | sed -n '1p') has no FIXED line in the fix report (none named)"
        return 1
    fi
    case "$hr_frep" in
        "$hr_reports"/*.md) ;;
        *) held_why="$hr_who: the fix report $hr_frep of held id(s) $hr_list is not $hr_reports/<name>.md"; return 1 ;;
    esac
    if ! hr_blob=$(git -C "$REPO" show "$hr_head:${hr_frep#"$REPO"/}" 2>/dev/null); then
        held_why="$hr_who: the fix report $hr_frep of held id(s) $hr_list is absent at the branch head $hr_head"
        return 1
    fi
    hr_flast=$(printf '%s\n' "$hr_blob" | grep -v '^[[:space:]]*$' | tail -n 1)
    case "$hr_flast" in
        "BUILT ·"*"tip: $hr_tip"*) ;;
        *) held_why="$hr_who: the fix report $hr_frep of held id(s) $hr_list does not end 'BUILT · … tip: $hr_tip': $hr_flast"; return 1 ;;
    esac
    # one normalized line per FIXED or CARRIED line: `F <id> <path> <name> -` or `C <id> <path> <name> R<n>`
    hr_lines=$(printf '%s\n' "$hr_blob" | sed -n -E \
        -e 's#^FIXED: ([A-Za-z0-9._-]+) — (tests/[A-Za-z0-9._/-]+\.py)::([A-Za-z0-9_]+)$#F \1 \2 \3 -#p' \
        -e 's#^CARRIED: ([A-Za-z0-9._-]+) — (tests/[A-Za-z0-9._/-]+\.py)::([A-Za-z0-9_]+) — (R[0-9]+)$#C \1 \2 \3 \4#p')
    while IFS=' ' read -r hr_kind hr_id hr_path hr_name hr_row; do
        [ -n "$hr_id" ] || continue
        if ! printf '%s\n' "$hr_ids" | grep -q -x -F -e "$hr_id"; then
            held_why="$hr_who: the fix report $hr_frep names $hr_id, which is no HELD, NOT FIXED id of the check $hr_check"
            return 1
        fi
    done <<HELD_LINES
$hr_lines
HELD_LINES
    while IFS= read -r hr_id; do
        [ -n "$hr_id" ] || continue
        hr_c=$(printf '%s\n' "$hr_lines" | awk -v id="$hr_id" '$2 == id' | grep -c .)
        if [ "$hr_c" -eq 0 ]; then
            held_why="$hr_who: held id $hr_id has no FIXED line in the fix report $hr_frep"
            return 1
        fi
        if [ "$hr_c" -ne 1 ]; then
            held_why="$hr_who: held id $hr_id has $hr_c FIXED or CARRIED lines in the fix report $hr_frep"
            return 1
        fi
    done <<HELD_IDS
$hr_ids
HELD_IDS
    hr_date=$(printf '%s\n' "${hr_check##*/}" | sed -n 's/.*-\([0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]\)\.md$/\1/p')
    hr_desk="$hr_reports/cto-$hr_date.md"
    # the desk reports a CARRIED or SETTLED R<n> is read in: dated on or after the check, newest first
    hr_ctos=""
    if [ -n "$hr_date" ]; then
        hr_ctos=$(git -C "$REPO" ls-tree --name-only "HEAD:${hr_reports#"$REPO"/}" 2>/dev/null \
            | grep -E '^cto-[0-9]{4}-[0-9]{2}-[0-9]{2}[.]md$' | awk -v d="cto-$hr_date.md" '$0 >= d' | sort -r)
    fi
    while IFS=' ' read -r hr_kind hr_id hr_path hr_name hr_row; do
        [ -n "$hr_id" ] || continue
        hr_label=FIXED
        [ "$hr_kind" = F ] || hr_label=CARRIED
        hr_shape=absent
        case "$hr_path" in
            *..*) ;;
            *)
                if hr_src=$(git -C "$REPO" show "$hr_tip:$hr_path" 2>/dev/null); then
                    # `absent`, or the def's decorators (`strict`, `xfail` or `plain`) and ` pytestmark`
                    # when a `pytestmark` statement (module or class) holds xfail. The def is the
                    # column-0 one when there is one; its decorators are the `@` lines directly
                    # above it, each with its bracketed continuation lines, comments skipped
                    hr_shape=$(printf '%s\n' "$hr_src" | awk -v name="$hr_name" '
                        function judge(t, s) {
                            if (index(t, "xfail") && index(t, "strict=True")) return "strict"
                            if (index(t, "xfail") && s != "strict") return "xfail"
                            return s
                        }
                        function decos(s, e,   j, t, depth) {
                            depth = 0
                            for (j = s; j < e; j++) {
                                if (line[j] ~ /^[ \t]*#/) continue
                                if (depth == 0 && line[j] !~ /^[ \t]*@/) return 0
                                t = line[j]
                                depth += gsub(/[([{]/, "", t)
                                t = line[j]
                                depth -= gsub(/[])}]/, "", t)
                            }
                            return depth == 0
                        }
                        { line[NR] = $0 }
                        END {
                            pm = 0; inpm = 0; pind = 0
                            for (i = 1; i <= NR; i++) {
                                ind = match(line[i], /[^ \t]/) - 1
                                c = substr(line[i], ind + 1, 1)
                                if (line[i] ~ /^[ \t]*pytestmark/) { inpm = 1; pind = ind }
                                else if (inpm && (line[i] ~ /^[ \t]*$/ || (ind <= pind && c != ")" && c != "]"))) inpm = 0
                                if (inpm && index(line[i], "xfail")) pm = 1
                            }
                            d = 0
                            for (i = 1; i <= NR; i++) if (line[i] ~ ("^def " name "\\(")) { d = i; break }
                            if (!d) for (i = 1; i <= NR; i++) if (line[i] ~ ("^[ \t]+def " name "\\(")) { d = i; break }
                            if (!d) { print "absent"; exit }
                            top = d
                            for (i = d - 1; i >= 1 && line[i] !~ /^[ \t]*$/; i--) {
                                if (line[i] ~ /^[ \t]*(async[ \t]+)?(def|class)[ \t]/) break
                                if (line[i] ~ /^[ \t]*@/ && decos(i, d)) top = i
                            }
                            shape = "plain"; deco = ""
                            for (i = top; i < d; i++) {
                                if (line[i] ~ /^[ \t]*#/) continue
                                if (line[i] ~ /^[ \t]*@/) { if (deco != "") shape = judge(deco, shape); deco = line[i] }
                                else deco = deco " " line[i]
                            }
                            if (deco != "") shape = judge(deco, shape)
                            print shape (pm ? " pytestmark" : "")
                        }')
                fi
                ;;
        esac
        hr_test="$hr_path::$hr_name"
        case "$hr_kind $hr_shape" in
            *" absent")
                held_why="$hr_who: $hr_label test $hr_test of $hr_id is absent at $hr_tip"
                return 1 ;;
            "F plain") ;;
            F*)
                held_why="$hr_who: FIXED test $hr_test of $hr_id is marked xfail"
                return 1 ;;
            "C strict"*) ;;
            *)
                held_why="$hr_who: CARRIED test $hr_test of $hr_id is not a strict xfail"
                return 1 ;;
        esac
        if [ "$hr_kind" = C ]; then
            case "$(held_row "$hr_row")" in
                *"DESK RECORD"*) ;;
                *)
                    held_why="$hr_who: CARRIED $hr_id names $hr_row, which is no DESK RECORD row of $hr_desk"
                    return 1 ;;
            esac
        fi
    done <<HELD_LINES
$hr_lines
HELD_LINES
    # `open:` past held unfixed: m - n REJECTED or UNSETTLED ids, one SETTLED line each (card 397)
    hr_open=$(awk '/^## /{on = ($0 == "## RUNS"); next}
        function opened(v) { sub(/^[ \t*]+/, "", v); return v ~ /^(REJECTED|UNSETTLED)/ }
        on && /^- [A-Za-z0-9._-]+ · / {v = $0; while ((p = index(v, " · ")) > 0) v = substr(v, p + length(" · "))
            if (opened(v)) {sub(/^- /, ""); sub(/ · .*/, ""); print}}
        on && /^[|]/ {n = split($0, c, "|"); id = c[2]; v = c[n]; if (n > 2 && v ~ /^[ \t]*$/) v = c[n - 1]
            sub(/^[ \t]+/, "", id); sub(/[ \t]+$/, "", id); if (id ~ /^[A-Za-z0-9._-]+$/ && opened(v)) print id}' "$hr_check")
    hr_settled=$(printf '%s\n' "$hr_blob" | sed -n -E 's#^SETTLED: ([A-Za-z0-9._-]+) — (R[0-9]+)$#\1 \2#p')
    while IFS=' ' read -r hr_id hr_row; do
        [ -n "$hr_id" ] || continue
        if printf '%s\n' "$hr_ids" | grep -q -x -F -e "$hr_id"; then
            held_why="$hr_who: the fix report $hr_frep settles $hr_id, which is a held id of the check $hr_check"
            return 1
        fi
        if ! printf '%s\n' "$hr_open" | grep -q -x -F -e "$hr_id"; then
            held_why="$hr_who: the fix report $hr_frep settles $hr_id, which is no REJECTED or UNSETTLED id under ## RUNS of the check $hr_check"
            return 1
        fi
        hr_c=$(printf '%s\n' "$hr_settled" | awk -v id="$hr_id" '$1 == id' | grep -c .)
        if [ "$hr_c" -ne 1 ]; then
            held_why="$hr_who: SETTLED $hr_id has $hr_c SETTLED lines in the fix report $hr_frep"
            return 1
        fi
        case "$(held_row "$hr_row")" in
            *"DESK RECORD"*) ;;
            *)
                held_why="$hr_who: SETTLED $hr_id names $hr_row, which is no DESK RECORD row of $hr_desk"
                return 1 ;;
        esac
    done <<HELD_SETTLED
$hr_settled
HELD_SETTLED
    hr_s=$(printf '%s\n' "$hr_settled" | grep -c .)
    if [ "$hr_s" -ne $((hr_m - hr_n)) ]; then
        held_why="$hr_who: 'open: $hr_m' counts $((hr_m - hr_n)) open id(s) past held unfixed, $hr_s settled in the fix report $hr_frep"
        return 1
    fi
    return 0
}
# ---- end of THE RULE --------------------------------------------------------------------------

# ---- every job card: its check, its tip, its head (P2, P3) -----------------------------------
ladder=""
heads=""
ships=""
markers=""
smokes=""
records=""
migs=""
jobs=""
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
    # the job's fix report, read before the check line's refusals: with one, a line carrying
    # `held unfixed: <n>`, n >= 1, takes THE RULE's path below (card 317 H1)
    frep=$(printf '%s' "$fixes" | sed -n "s/^$job=//p" | sed -n '1p')
    hn=""
    [ -z "$frep" ] || hn=$(held_n "$last")
    if [ -z "$hn" ]; then
        printf '%s\n' "$last" | grep -q -E '(^| )held unfixed: 0( |$)' || refuse "$job: the check's last line lacks 'held unfixed: 0': $last"
        printf '%s\n' "$last" | grep -q -E '(^| )ready: YES( |$)' || refuse "$job: the check's last line lacks 'ready: YES': $last"
    fi
    tip=$(printf '%s\n' "$last" | grep -o -E '(^| )tip: [0-9a-f]{7,40}' | sed -n '1p' | sed 's/.*tip: //')
    [ -n "$tip" ] || refuse "$job: the check's last line names no tip: $last"
    ctip=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "$tip^{commit}") || refuse "$job: code tip '$tip' is not a commit in $REPO"
    head=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "refs/heads/$branch^{commit}") || refuse "$job: no branch '$branch' in $REPO"
    jobs="$jobs $job"
    # a fix round: the code tip is the fix report's `tip:`, read at the head; the check's tip its ancestor
    fixcell=""
    if [ -n "$frep" ]; then
        fblob=$(git -C "$REPO" show "$head:${frep#"$REPO"/}" 2>/dev/null) || refuse "$job: the fix report is absent at the branch head $head: $frep"
        flast=$(printf '%s\n' "$fblob" | grep -v '^[[:space:]]*$' | tail -n 1)
        ftip=""
        case "$flast" in
            "BUILT ·"*) ftip=$(printf '%s\n' "$flast" | grep -o -E '(^| )tip: [0-9a-f]{8,40}' | sed -n '1p' | sed 's/.*tip: //') ;;
        esac
        [ -n "$ftip" ] || refuse "$job: the fix report's last line is not 'BUILT ·' with a 'tip:': $flast"
        fixtip=$(git -C "$REPO" rev-parse --verify --quiet --short=8 "$ftip^{commit}") || refuse "$job: fix tip '$ftip' is not a commit in $REPO"
        git -C "$REPO" merge-base --is-ancestor "$ctip" "$fixtip" || refuse "$job: the check's tip $ctip is not an ancestor of the fix tip $fixtip"
        ctip=$fixtip
        # card 317 H1: a held check line needs a FIXED or CARRIED line per held id
        if [ -n "$hn" ]; then
            held_rule "$job" "$creport" "$last" "$fixtip" "$head" "$frep" || refuse "$held_why"
        fi
        fixcell=" \`$frep\`"
        records="$records- $job: fix report \`$frep\` at \`$head\` last line: $flast$nl"
    fi
    git -C "$REPO" merge-base --is-ancestor "$ctip" "$head" || refuse "$job: code tip $ctip is not an ancestor of the head $head of $branch"
    past=$(git -C "$REPO" diff --name-only "$ctip" "$head" -- . ':(exclude)docs')
    [ -z "$past" ] || refuse "$job: the head $head adds paths outside docs/ past the code tip $ctip: $(printf '%s' "$past" | tr '\n' ' ')"

    heads="${heads:+$heads }$head"
    if [ -z "$hn" ]; then
        ships="$ships| $n | \`$branch\` | \`$ctip\` | \`$head\` | \`$creport\` | \`held unfixed: 0\` and \`ready: YES\` |$fixcell |$nl"
    else
        # a held row carries the check line's own literals (card 317 H1)
        ships="$ships| $n | \`$branch\` | \`$ctip\` | \`$head\` | \`$creport\` | \`held unfixed: $hn\` and \`ready: NO\` |$fixcell |$nl"
    fi
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
for fjob in $fixjobs; do
    case "$jobs " in
        *" $fjob "*) ;;
        *) refuse "--fix-report names job '$fjob', which is no JOB of the job cards given" ;;
    esac
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
TICKERS: $tickers

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
$ships
## MARKERS
$markers
## SMOKE READS
$smokes
## RECORDS
$records- written by deploy-card.sh at $now (\`date\`); trial merge of the heads onto main in order: clean"

( set -C; printf '%s\n' "$text" > "$out" ) 2>/dev/null || refuse "could not write --out (it exists now, or the folder is not writable): $out"
printf 'deploy-card: %s written (%s job(s), TIP %s)\n' "$out" "$#" "$heads"
