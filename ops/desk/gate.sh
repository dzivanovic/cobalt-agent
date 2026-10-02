#!/bin/sh
# gate.sh <worktree name> <probe|offline|withdb|livenote|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration]
# — BUILD-HUB.md `## W`, the three suites, in ONE call, run from $WT/<worktree name> (card 19
# worker-steps S3).
#
# THE COMMANDS HAVE ONE HOME: every command this script runs is read from THAT WORKTREE's
# docs/40 - DevDocs/prompts/BUILD-HUB.md and run as written (eval): W (a) the offline run; W (b) the
# proof-only; the two backticked lines under W (c) and W (c3) that begin `COBALT_ENV=dev uv run
# pytest` (pass 1, pass 2); W (c2) the forward; W (c3r) the stray-row query; W (e) the live-note
# run; W (f) the rollback (its `--down-to` level is the level this script expects); and `<FP>`,
# the fingerprint query of `## THE LOCK`. A hub file that lacks one is refused. Every
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
#
# THE LOCK: `ls -la $WT/*/.env` first — any .env is a held lock (exit 4, nothing run). Then
# take-devdb-lock.sh <worktree> 90 and release-devdb-lock.sh <worktree> when BOTH sit beside this
# script; else BUILD-HUB.md THE LOCK's pair, `cp $REPO/.env $WT/<worktree>/.env` and `rm` of it,
# each followed by its `ls` proof. A trap on EVERY exit (a red, an error, INT, TERM, HUP) runs the
# rollback when the forward was started and not yet rolled back, then ALWAYS the release, and
# proves .env gone.
#
# THE LEVEL: `migrate --proof-only` prints no level number (src/cobalt/db_migrations/cli.py
# cmd_migrate, _print_probe). This script holds it to what it can read: exit 0, `on cobalt_dev`,
# and no `CHANGED`; else exit 5. The table itself is in the log, for the worker to read as W (b)
# says.
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

set -u
set -f

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
HERE=$(cd "$(dirname "$0")" && pwd)

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -ge 2 ] || refuse "usage: gate.sh <worktree name> <probe|offline|withdb|livenote|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration]"
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
        *) refuse "unknown argument '$1'" ;;
    esac
done
case "$mode" in
    withdb|all) ;;
    *) [ -z "$deselects$tickers$migration" ] || refuse "--deselect, --tickers and --migration belong to withdb and all" ;;
esac

dir="$WT/$name"
hub="$dir/docs/40 - DevDocs/prompts/BUILD-HUB.md"
[ -d "$dir" ] || refuse "no such worktree: $dir"
[ -f "$hub" ] || refuse "no hub file in the worktree: $hub"

tmp=$(mktemp -d "${TMPDIR:-/tmp}/gate.XXXXXX") || refuse "mktemp failed"

# ---- the commands, read from the hub file (each to $tmp/<key>) ----------------------------------
python3 - "$hub" "$tmp" <<'PY' || { rm -rf "$tmp"; refuse "the hub file does not hold every command gate.sh runs: $hub"; }
import re, sys
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
out = sys.argv[2]

def section(title):
    body, inside = [], False
    for line in lines:
        if line.startswith("## "):
            inside = line.startswith("## " + title)
            continue
        if inside:
            body.append(line)
    return body

def spans(line):
    return re.findall(r"`([^`]*)`", line)

def one(key, found):
    if len(found) != 1:
        sys.exit("%s: %d matches" % (key, len(found)))
    open("%s/%s" % (out, key), "w", encoding="utf-8").write(found[0])

w, lock = section("W "), section("THE LOCK")

def item(tag):
    return [l for l in w if l.startswith("- (%s) " % tag)]

def after(tag):
    found = []
    for i, l in enumerate(w):
        if l.startswith("- (%s) " % tag):
            for nxt in w[i + 1:]:
                s = nxt.strip()
                if s:
                    if s.startswith("`COBALT_ENV=dev uv run pytest ") and s.endswith("`") and s.count("`") == 2:
                        found.append(s[1:-1])
                    break
    return found

one("offline", [s for l in item("a") for s in spans(l) if s.startswith("uv run pytest ")])
one("proof", [s for l in item("b") for s in spans(l) if s == "COBALT_ENV=dev uv run cobalt db migrate --proof-only"])
one("pass1", after("c"))
one("forward", [s for l in item("c2") for s in spans(l) if s == "COBALT_ENV=dev uv run cobalt db migrate"])
one("pass2", after("c3"))
q = [s for l in item("c3r") for s in spans(l) if s.startswith("COBALT_ENV=dev uv run cobalt db query ")]
if len(q) == 1:
    q = [re.sub(r"\(<[^>]*>\)", "(__TICKERS__)", q[0])]
    if "(__TICKERS__)" not in q[0]:
        sys.exit("c3r: no (<…>) ticker list")
one("tickers", q)
one("livenote", [s for l in item("e") for s in spans(l) if s.startswith("COBALT_LIVE_VAULT_ROOT=")])
one("rollback", [s for l in item("f") for s in spans(l) if s.startswith("COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to ")])
one("fp", [s for l in lock for s in spans(l) if s.startswith('COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT count(*)')])
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
level=${ROLLBACK##* }

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

take() {
    note ""
    note "\$ ls -la $WT/*/.env"
    held_env
    if [ -n "$held" ]; then
        note "$held"
        say "cobalt_dev lock held — $held"
        exit 4
    fi
    note "no matches found"
    if [ -f "$HERE/take-devdb-lock.sh" ] && [ -f "$HERE/release-devdb-lock.sh" ]; then
        lockway=script
        note "\$ sh $HERE/take-devdb-lock.sh $name 90"
        sh "$HERE/take-devdb-lock.sh" "$name" 90 >> "$log" 2>&1
        rc=$?
        note "[exit $rc]"
        [ "$rc" -ne 4 ] || { say "cobalt_dev lock not free (take-devdb-lock.sh exit 4)"; exit 4; }
        [ "$rc" -eq 0 ] || { say "the lock take failed (take-devdb-lock.sh exit $rc)"; exit 1; }
        taken=1
    else
        lockway=cp
        taken=1
        note "\$ cp $REPO/.env $dir/.env"
        cp "$REPO/.env" "$dir/.env" >> "$log" 2>&1 || { say "the lock take failed (cp)"; exit 1; }
    fi
    note "\$ ls -la $WT/*/.env"
    held_env
    note "$held"
    [ "$held" = "$dir/.env" ] || { say "cobalt_dev lock not ours alone after the take — $held"; exit 4; }
}

release() {
    if [ "$lockway" = script ]; then
        note "\$ sh $HERE/release-devdb-lock.sh $name"
        sh "$HERE/release-devdb-lock.sh" "$name" >> "$log" 2>&1
        note "[exit $?]"
    else
        note "\$ rm $dir/.env"
        rm -f "$dir/.env"
    fi
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
# subshell: a failed query must reach its caller, and nothing it says may land in the value.
fingerprint() {
    run "$FP"
    frc=$?
    FPV=$(plain | sed -n '2p' | tr '\t' ' ')
    [ "$frc" -eq 0 ] && [ -n "$FPV" ] || { FPV="(the fingerprint query failed, exit $frc)"; return 1; }
}

# rollback_and_prove: W (f); 0 when <F2> = <F0>, else 6. It never exits: the trap calls it.
rollback_and_prove() {
    applied=""
    run "$ROLLBACK"
    rrc=$?
    fingerprint
    fp2=$FPV
    note "F2: $fp2"
    if [ "$fp2" = "$fp0" ]; then
        [ "$rrc" -eq 0 ] || say "the rollback exited $rrc; F2 = F0 (log)"
        return 0
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
    say "proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))"
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
    p2cmd=$PASS2
    for id in $deselects; do
        p1cmd="$p1cmd --deselect $id"
        p2cmd="$p2cmd $id"
    done
    suite "$p1cmd" || exit 1
    p1=$P
    skips=$(plain | grep '^SKIPPED')
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
