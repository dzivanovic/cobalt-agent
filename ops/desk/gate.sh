#!/bin/sh
# gate.sh <worktree name> <probe|offline|withdb|livenote|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration] [--deploy]
# — BUILD-HUB.md `## W`, the three suites, in ONE call, run from $WT/<worktree name> (card 19
# worker-steps S3).
#
# THE COMMANDS HAVE ONE HOME: every command this script runs is read from THAT WORKTREE's
# ops/desk/gate-lists.md and run as written (eval) — never from a hub file (card 2026-10-03/03
# adoption-scripts L2): `## OFFLINE` W (a); `## PROOF ONLY` W (b); `## PASS 1` W (c); `## FORWARD`
# W (c2); `## PASS 2` W (c3); `## STRAY ROWS` W (c3r); `## LIVE-NOTE` W (e); `## ROLLBACK` W (f),
# whose `--down-to` must be the `## LEVEL <nnnn>` level; `## FINGERPRINT` `<FP>`; `## ALLOWED
# SKIPS`; and `## LEVEL <nnnn>`, the TABLES and FINGERPRINT lines the proof-only must print. Each
# section holds ONE backticked line; a lists file that lacks one is refused. Every
# `--deselect <id>` is added to pass 1 as `--deselect <id>` and appended to pass 2 as `<id>`.
#
# MODES
#   probe     PREFLIGHT's lock probe: the take, <FP>, the proof-only, the release.
#   offline   W (a).
#   withdb    W (b) the take, <F0>, the proof-only; (c) pass 1; (c2) the forward, <F1>; (c3) pass 2;
#             (c3r) the stray-row read for --tickers (skipped, and said, when none is given);
#             (c4) with --migration, forward and rollback again after (f); (f) the rollback,
#             <F2> = <F0> field for field; the release.
#   livenote  W (e); refused while this worktree's .env is present; a SKIPPED line naming
#             COBALT_LIVE_VAULT_ROOT is a red.
#   all       offline, withdb, livenote, in that order; it stops at the first that is not green.
#   --deploy  (withdb, all; card 2026-10-03/03c M3, his 2026-10-02 R154) THE DEPLOY'S WHOLE PASS 1:
#             `## PASS 1` with its one ` --db-only` token removed, everything else byte-equal,
#             printing `pass 1: whole (deploy)`; a PASS 1 that does not hold that token exactly
#             once is refused before anything runs. Without it pass 1 is `## PASS 1` as written.
#
# THE LOCK (card 2026-10-03/03c M2): taken ONLY by take-devdb-lock.sh <worktree> 90 and given back
# by release-devdb-lock.sh <worktree>, both beside this script (probe, withdb and all are refused
# before anything runs when either is missing). The take's own retry — every 60 s for 90 min — is
# the wait: a held lock is waited for, never refused at once; exit 4 only when the take exits 4.
# After it `lock: waited <n> min` (the take's start and end `date`), then `ls -la $WT/*/.env` must
# show this worktree's alone. A trap on EVERY exit (a red, an error, INT, TERM, HUP) runs the
# rollback when the forward was started and not yet rolled back, then ALWAYS the release, and
# proves .env gone.
#
# THE LEVEL: `migrate --proof-only` ends with a `TABLES …` and a `FINGERPRINT …` line (L1). This
# script prints `LEVEL <nnnn>` only when both equal the two halves of `## LEVEL <nnnn>`, with exit 0,
# `on cobalt_dev` and no `CHANGED`; else exit 5, printing both lines as read. After the rollback
# it requires the same two lines again, and <F2> = <F0>; else exit 6. A pass-1 SKIPPED line that
# no `## ALLOWED SKIPS` item covers is printed `OUTSIDE the allowed set: <line>` (the exit does
# not change: the builder quotes every skip, the deploy gate judges them).
#
# OUTPUT: everything to $WT/.gate-logs/<worktree>-<mode>-<timestamp>.log. Stdout is the verdict
# only: `offline <p>/0`, `with-DB <d>/0` (pass 1 + pass 2), `live-note <l>/0`, every SKIPPED line
# of pass 1, `cobalt_dev: <level> — F2 = F0`, `.env: removed`, `log: <path>`; on a red, the first
# 20 failing lines (FAILED / ERROR lines, else the last 20 lines).
# EXIT: 0 green · 1 a suite red or errored, stray rows (DECISION 0), or a bad call (`REFUSED:` on
# stderr) · 4 the lock not free · 5 cobalt_dev not clean at the start · 6 <F2> ≠ <F0> after the
# rollback (`cobalt_dev NOT back at <level>`).
#
# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for /Users/cobalt/cobalt and /Users/cobalt/cobalt-wt
# in tests/ops/test_gate.py only.

export LC_ALL=C
set -u
set -f
# every environment prefix a command carries is the hub's own spelling: none comes from the caller
unset COBALT_ENV COBALT_LIVE_VAULT_ROOT

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
HERE=$(cd "$(dirname "$0")" && pwd)

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -ge 2 ] || refuse "usage: gate.sh <worktree name> <probe|offline|withdb|livenote|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration] [--deploy]"
name=$1
mode=$2
shift 2
case "$name" in
    ""|.*|*[!A-Za-z0-9._-]*) refuse "worktree '$name' is not one directory name [A-Za-z0-9._-]" ;;
esac
case "$mode" in
    probe|offline|withdb|livenote|all) ;;
    *) refuse "mode '$mode' is none of probe, offline, withdb, livenote, all" ;;
esac
deselects=""
tickers=""
migration=""
deploy=""
while [ "$#" -gt 0 ]; do
    case "$1" in
        --deselect)
            [ "$#" -ge 2 ] || refuse "--deselect needs a test id"
            case "$2" in
                ""|-*|*[!A-Za-z0-9_./:\[\]-]*) refuse "test id '$2' holds a character outside [A-Za-z0-9_./:[]-]" ;;
            esac
            deselects="$deselects $2"
            shift 2
            ;;
        --tickers)
            [ "$#" -ge 2 ] || refuse "--tickers needs A,B,…"
            case "$2" in
                ""|,*|*,|*,,*|*[!A-Z0-9.,]*) refuse "tickers '$2' are not A,B,… of [A-Z0-9.]" ;;
            esac
            tickers=$2
            shift 2
            ;;
        --migration) migration=1; shift ;;
        --deploy) deploy=1; shift ;;
        *) refuse "unknown argument '$1'" ;;
    esac
done
case "$mode" in
    withdb|all) ;;
    *) [ -z "$deselects$tickers$migration$deploy" ] || refuse "--deselect, --tickers, --migration and --deploy belong to withdb and all" ;;
esac
# the lock is taken by the two lock scripts beside this script and by nothing else (03c M2)
case "$mode" in
    probe|withdb|all)
        [ -f "$HERE/take-devdb-lock.sh" ] && [ -f "$HERE/release-devdb-lock.sh" ] \
            || refuse "the lock scripts are not beside gate.sh: $HERE/take-devdb-lock.sh, $HERE/release-devdb-lock.sh"
        ;;
esac

dir="$WT/$name"
lists="$dir/ops/desk/gate-lists.md"
[ -d "$dir" ] || refuse "no such worktree: $dir"
[ -f "$lists" ] || refuse "no lists file in the worktree: $lists"

tmp=$(mktemp -d "${TMPDIR:-/tmp}/gate.XXXXXX") || refuse "mktemp failed"

# ---- the commands and the level, read from the lists file (each to $tmp/<key>) ------------------
python3 - "$lists" "$tmp" <<'PY' || { rm -rf "$tmp"; refuse "the lists file does not hold every command gate.sh runs: $lists"; }
import re, sys
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
out = sys.argv[2]

sections, title = {}, None
for line in lines:
    if line.startswith("## "):
        title = line[3:].strip()
        if title in sections:
            sys.exit("## %s: twice" % title)
        sections[title] = []
    elif title is not None and line.strip():
        sections[title].append(line.strip())

def one(title):
    body = sections.get(title)
    if body is None:
        sys.exit("no ## %s" % title)
    if len(body) != 1 or not re.fullmatch(r"`[^`]+`", body[0]):
        sys.exit("## %s: not ONE backticked line" % title)
    return body[0][1:-1]

def put(key, value):
    open("%s/%s" % (out, key), "w", encoding="utf-8").write(value)

for title, key in (("OFFLINE", "offline"), ("PROOF ONLY", "proof"), ("PASS 1", "pass1"), ("FORWARD", "forward"),
                   ("PASS 2", "pass2"), ("LIVE-NOTE", "livenote"), ("ROLLBACK", "rollback"),
                   ("FINGERPRINT", "fp"), ("ALLOWED SKIPS", "skips")):
    put(key, one(title))
q = re.sub(r"\(<[^>]*>\)", "(__TICKERS__)", one("STRAY ROWS"))
if "(__TICKERS__)" not in q:
    sys.exit("## STRAY ROWS: no (<…>) ticker list")
put("tickers", q)
levels = [t for t in sections if t.startswith("LEVEL")]
if len(levels) != 1 or not re.fullmatch(r"LEVEL [0-9]{4}", levels[0]):
    sys.exit("not ONE ## LEVEL <nnnn>: %s" % levels)
level = levels[0][len("LEVEL "):]
m = re.fullmatch(r"(TABLES [0-9]{4}) · (FINGERPRINT cols [0-9]+ · rels [0-9]+ · views_md5 [0-9a-f]{32})", one(levels[0]))
if not m:
    sys.exit("## %s: not `TABLES <nnnn> · FINGERPRINT cols <c> · rels <r> · views_md5 <m>`" % levels[0])
if not one("ROLLBACK").endswith(" --down-to " + level):
    sys.exit("## ROLLBACK does not go --down-to %s" % level)
put("level", level)
put("tables", m.group(1))
put("fingerprint", m.group(2))
# the deploy's whole pass 1 (03c M3): the ONE ` --db-only` token removed, nothing else; empty
# when PASS 1 does not hold that token exactly once (a --deploy run is then refused)
whole, n = re.subn(r" --db-only(?= |$)", "", one("PASS 1"))
put("pass1_deploy", whole if n == 1 else "")
PY

OFFLINE=$(cat "$tmp/offline")
PROOF=$(cat "$tmp/proof")
PASS1=$(cat "$tmp/pass1")
FORWARD=$(cat "$tmp/forward")
PASS2=$(cat "$tmp/pass2")
TICKERS_Q=$(cat "$tmp/tickers")
LIVENOTE=$(cat "$tmp/livenote")
ROLLBACK=$(cat "$tmp/rollback")
FP=$(cat "$tmp/fp")
level=$(cat "$tmp/level")
TABLES_AT=$(cat "$tmp/tables")
FINGERPRINT_AT=$(cat "$tmp/fingerprint")
PASS1_DEPLOY=$(cat "$tmp/pass1_deploy")
[ -z "$deploy" ] || [ -n "$PASS1_DEPLOY" ] || { rm -rf "$tmp"; refuse "--deploy: ## PASS 1 does not hold ' --db-only' exactly once: $lists"; }

logdir="$WT/.gate-logs"
mkdir -p "$logdir" || { rm -rf "$tmp"; refuse "mkdir failed: $logdir"; }
log="$logdir/$name-$mode-$(date +%Y%m%d-%H%M%S).log"
: >> "$log" || { rm -rf "$tmp"; refuse "cannot write the log: $log"; }
esc=$(printf '\033')

say() {
    printf '%s\n' "$*"
    printf '%s\n' "$*" >> "$log"
}

note() {
    printf '%s\n' "$*" >> "$log"
}

# run <command>: eval'd from $dir as the hub spells it; output to $tmp/seg and the log; its exit
run() {
    note ""
    note "\$ $1"
    (cd "$dir" && eval "$1") > "$tmp/seg" 2>&1
    rc=$?
    cat "$tmp/seg" >> "$log"
    note "[exit $rc]"
    return "$rc"
}

plain() {
    sed "s/${esc}\[[0-9;]*m//g" "$tmp/seg"
}

# count <word>: the number before <word> on the pytest summary line (0 when absent)
count() {
    printf '%s\n' "$summary" | awk -v w="$1" '{for (i = 1; i < NF; i++) if (index($(i + 1), w) == 1) n = $i} END {print n + 0}'
}

# suite <command>: run it, read its summary; sets P; 0 green, 1 red (the red lines printed)
suite() {
    run "$1"
    rc=$?
    summary=$(plain | grep -E '[0-9]+ (passed|failed|error|errors|skipped|deselected)|no tests ran' | tail -n 1)
    P=$(count passed)
    f=$(count failed)
    e=$(count error)
    if [ "$rc" -eq 0 ] && [ "$f" -eq 0 ] && [ "$e" -eq 0 ] && [ "$P" -gt 0 ]; then
        return 0
    fi
    say "RED (exit $rc): ${summary:-no pytest summary line}"
    reds=$(plain | grep -E '^(FAILED|ERROR)' | head -n 20)
    [ -n "$reds" ] || reds=$(plain | tail -n 20)
    say "$reds"
    return 1
}

# ---- the lock --------------------------------------------------------------------------------
taken=""
applied=""
fp0=""

held_env() {
    held=""
    set +f
    for f in "$WT"/*/.env; do
        [ -e "$f" ] && held="$held $f"
    done
    set -f
    held=${held# }
}

# the take WAITS (03c M2): no pre-check of its own; take-devdb-lock.sh retries a held lock every
# 60 s for 90 min, and only its exit 4 is "not free"
take() {
    lockway=script
    # taken BEFORE the take: a signal while it waits is handled after it returns, and the
    # release gives back only a lock that names this worktree (release-devdb-lock.sh)
    taken=1
    note ""
    note "\$ date"
    t0=$(date +%s)
    note "\$ sh $HERE/take-devdb-lock.sh $name 90"
    sh "$HERE/take-devdb-lock.sh" "$name" 90 >> "$log" 2>&1
    rc=$?
    note "[exit $rc]"
    note "\$ date"
    t1=$(date +%s)
    say "lock: waited $(( (t1 - t0) / 60 )) min"
    [ "$rc" -eq 0 ] || taken=""
    [ "$rc" -ne 4 ] || { say "cobalt_dev lock not free (take-devdb-lock.sh exit 4)"; exit 4; }
    [ "$rc" -eq 0 ] || { say "the lock take failed (take-devdb-lock.sh exit $rc)"; exit 1; }
    note "\$ ls -la $WT/*/.env"
    held_env
    note "$held"
    [ "$held" = "$dir/.env" ] || { say "cobalt_dev lock not ours alone after the take — $held"; exit 4; }
}

release() {
    note "\$ sh $HERE/release-devdb-lock.sh $name"
    sh "$HERE/release-devdb-lock.sh" "$name" >> "$log" 2>&1
    note "[exit $?]"
    taken=""
    note "\$ ls $dir/.env"
    if [ -e "$dir/.env" ]; then
        say ".env: STILL PRESENT — $dir/.env"
        return 1
    fi
    note "No such file or directory"
    say ".env: removed"
}

# fingerprint: <FP> into FPV (its value row, fields blank-separated); the query's exit. Never in a
# subshell: a failed query must reach its caller, and nothing it says may land in the value. The
# value row is the line after the `cols rels views_md5` header, never a line number: stderr shares
# the segment, and a warning above the header must not make the header the value (check O1).
fingerprint() {
    run "$FP"
    frc=$?
    FPV=$(plain | awk -F '\t' 'h { print; exit } $1 == "cols" && $2 == "rels" && $3 == "views_md5" { h = 1 }' | tr '\t' ' ')
    [ "$frc" -eq 0 ] && [ -n "$FPV" ] || { FPV="(the fingerprint query failed, exit $frc)"; return 1; }
}

# level_read: the last TABLES and FINGERPRINT lines of the proof-only just run, into TL and FL;
# 0 when both equal the two halves of gate-lists.md `## LEVEL <nnnn>`
level_read() {
    TL=$(plain | grep '^TABLES ' | tail -n 1)
    FL=$(plain | grep '^FINGERPRINT ' | tail -n 1)
    [ "$TL" = "$TABLES_AT" ] && [ "$FL" = "$FINGERPRINT_AT" ]
}

level_said() {
    say "read: ${TL:-(no TABLES line)}"
    say "read: ${FL:-(no FINGERPRINT line)}"
}

# rollback_and_prove: W (f); 0 when <F2> = <F0> and the proof-only's level lines are
# `## LEVEL <nnnn>`'s again, else 6. It never exits: the trap calls it.
rollback_and_prove() {
    applied=""
    run "$ROLLBACK"
    rrc=$?
    fingerprint
    fp2=$FPV
    note "F2: $fp2"
    if [ "$fp2" = "$fp0" ]; then
        [ "$rrc" -eq 0 ] || say "the rollback exited $rrc; F2 = F0 (log)"
        run "$PROOF"
        level_read && return 0
        say "cobalt_dev NOT back at $level — F2 = F0, but the proof-only's level lines after the rollback are not gate-lists.md ## LEVEL $level"
        level_said
        say "DECISION 0: cobalt_dev NOT back at $level"
        return 6
    fi
    say "cobalt_dev NOT back at $level — F0 $fp0 · F2 $fp2 (rollback exit $rrc)"
    say "DECISION 0: cobalt_dev NOT back at $level"
    return 6
}

cleanup() {
    st=$?
    trap - EXIT
    trap '' INT TERM HUP
    if [ -n "$applied" ]; then
        rollback_and_prove || st=6
    fi
    if [ -n "$taken" ]; then
        release || { [ "$st" -ne 0 ] || st=1; }
    fi
    if [ -e "$dir/.env" ] && [ -n "${lockway:-}" ]; then
        say ".env: STILL PRESENT — $dir/.env"
        [ "$st" -ne 0 ] || st=1
    fi
    rm -rf "$tmp"
    printf 'log: %s\n' "$log"
    exit "$st"
}
trap cleanup EXIT
trap 'exit 129' HUP
trap 'exit 130' INT
trap 'exit 143' TERM

proof_clean() {
    run "$PROOF"
    rc=$?
    first=$(plain | sed -n '1p')
    case "$first" in
        *"on cobalt_dev"*) ;;
        *) say "cobalt_dev not at $level at the start: the proof-only is not on cobalt_dev — $first"; exit 5 ;;
    esac
    if [ "$rc" -ne 0 ] || plain | grep -q -w CHANGED; then
        say "cobalt_dev not at $level at the start: the proof-only exited $rc or shows CHANGED (log)"
        exit 5
    fi
    if ! level_read; then
        say "cobalt_dev not at $level at the start: the proof-only's level lines are not gate-lists.md ## LEVEL $level"
        level_said
        exit 5
    fi
    say "proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))"
    say "LEVEL $level"
}

# ---- the modes --------------------------------------------------------------------------------
do_offline() {
    suite "$OFFLINE" || exit 1
    say "offline $P/0"
}

do_livenote() {
    [ ! -e "$dir/.env" ] || refuse "livenote runs with .env absent; $dir/.env is present"
    suite "$LIVENOTE" || exit 1
    if plain | grep '^SKIPPED' | grep -q COBALT_LIVE_VAULT_ROOT; then
        say "RED: a skip names COBALT_LIVE_VAULT_ROOT"
        say "$(plain | grep '^SKIPPED' | grep COBALT_LIVE_VAULT_ROOT)"
        exit 1
    fi
    say "live-note $P/0"
}

do_probe() {
    take
    fingerprint || { say "the fingerprint query failed (log)"; exit 1; }
    fp0=$FPV
    say "Fp: $fp0"
    proof_clean
    release || exit 1
}

do_withdb() {
    take
    fingerprint || { say "the fingerprint query failed (log)"; exit 1; }
    fp0=$FPV
    note "F0: $fp0"
    proof_clean
    p1cmd=$PASS1
    if [ -n "$deploy" ]; then
        p1cmd=$PASS1_DEPLOY
        say "pass 1: whole (deploy)"
    fi
    p2cmd=$PASS2
    for id in $deselects; do
        p1cmd="$p1cmd --deselect $id"
        p2cmd="$p2cmd $id"
    done
    suite "$p1cmd" || exit 1
    p1=$P
    # each pass-1 skip, marked when no `## ALLOWED SKIPS` item covers it: an item's path (with its
    # `:<line>`) is followed by `:` on the line, and every other word but a `test_…` label is on it
    skips=$(plain | grep '^SKIPPED' | python3 -c '
import sys
items = [i.split() for i in open(sys.argv[1], encoding="utf-8").read().split(" · ") if i.strip()]
def covered(line):
    return any(line.find(w[0] + ":") >= 0 and all(x in line for x in w[1:] if not x.startswith("test_"))
               for w in items)
for line in sys.stdin.read().splitlines():
    print(line if covered(line) else "OUTSIDE the allowed set: " + line)
' "$tmp/skips")
    applied=1
    note "dev forward: APPLIED $(date +%H:%M:%S)"
    run "$FORWARD" || { say "RED: the forward migrate failed (log)"; exit 1; }
    if plain | grep -q -w CHANGED; then
        say "RED: the forward migrate shows CHANGED (log)"
        exit 1
    fi
    fingerprint || { say "the fingerprint query failed after the forward (log)"; exit 1; }
    note "F1: $FPV"
    suite "$p2cmd" || exit 1
    p2=$P
    stray=""
    if [ -n "$tickers" ]; then
        note "\$ ls -la $dir/.env"
        ls -la "$dir/.env" >> "$log" 2>&1
        list=$(printf '%s' "$tickers" | sed -e "s/,/','/g" -e "s/^/'/" -e "s/\$/'/")
        q=$(printf '%s\n' "$TICKERS_Q" | sed "s/(__TICKERS__)/($list)/")
        run "$q" || { say "the stray-row query failed"; exit 1; }
        rows=$(plain | sed '1d' | sed '/^[[:space:]]*$/d')
        if [ -n "$rows" ]; then
            stray=$(printf '%s\n' "$rows" | cut -f1 | tr '\n' ' ' | sed 's/ *$//')
        else
            say "stray rows: none ($tickers)"
        fi
    else
        say "stray rows: not read (no --tickers given)"
    fi
    rollback_and_prove || exit 6
    if [ -n "$migration" ]; then
        applied=1
        run "$FORWARD" || { say "RED: the second forward failed (log)"; exit 1; }
        applied=""
        run "$ROLLBACK"
        fingerprint
        fp3=$FPV
        note "F (c4): $fp3"
        if [ "$fp3" != "$fp0" ]; then
            say "cobalt_dev NOT back at $level after (c4) — F0 $fp0 · F $fp3"
            exit 6
        fi
        say "forward, back, forward, back — F = F0 twice"
    fi
    say "cobalt_dev: $level — F2 = F0"
    release || exit 1
    say "with-DB $((p1 + p2))/0"
    [ -z "$skips" ] || say "$skips"
    if [ -n "$stray" ]; then
        say "DECISION 0: the suite left $stray rows on cobalt_dev"
        exit 1
    fi
}

lockway=""
case "$mode" in
    probe) do_probe ;;
    offline) do_offline ;;
    withdb) do_withdb ;;
    livenote) do_livenote ;;
    all) do_offline; do_withdb; do_livenote ;;
esac
exit 0
