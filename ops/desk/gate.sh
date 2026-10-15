#!/bin/sh
# gate.sh <worktree name> <probe|offline|withdb|livenote|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration] [--deploy] [--deploy-gate]
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
#   --deploy-gate  (offline, all; card 2026-10-13/521) `## OFFLINE OPS` (tests/ops) runs after
#             `## OFFLINE` whatever the diff holds, printing `tests/ops: run (deploy gate)`; without
#             it tests/ops runs only on an ops diff from `git merge-base main HEAD` (ops_reason).
#             DEPLOY-HUB's gate call and a check's W type it; a build's W does not.
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
# THE COPY (card 547 db-copy, his R1471): copy mode is ON only when the lists file holds BOTH
# `## COPY CREATE` and `## COPY DROP`, each ONE backticked line holding the token `<COPY>` once
# (one without the other, or another token count, is refused before anything runs), AND the call
# passes --copy (check O2, A1); without --copy every line of a run is the lock's as above, whatever
# the lists file holds, and --copy without both sections is refused before anything runs. --copy
# reaches withdb and all only; no deploy line passes it. In copy mode the worktree name must be
# [a-z0-9-] (`REFUSED: copy mode needs a worktree name of [a-z0-9-]`, check O3), so the copy's
# name, `cobalt_dev_` + the worktree name with `-` turned to `_`, is one to one;
# over 50 characters in all is refused (`REFUSED: copy name too long`), never truncated. The lock
# is held SHORT: the take, <F0> and the proof-only on cobalt_dev (the template) as above, then
# `## COPY DROP` (a leftover of a crashed run of this worktree; its failure is logged, not fatal)
# and `## COPY CREATE` (a failure prints `copy not created`, exit 1), then the release.
# devdb-copy-env.sh place copies .env back by name and writes the marker
# $WT/.devdb-copies/<worktree>; COBALT_DEV_DB_NAME=<copy> is exported, and the fingerprint, the
# proof-only (`on <copy>`), the passes, the forward, the stray rows and the rollback run on the
# copy, the verdict lines unchanged but for `copy: <copy> created` and `copy: <copy> dropped`.
# On every exit the trap drops the copy (`copy: <copy> NOT dropped` → exit 1; the next run of the
# same worktree clears it) and devdb-copy-env.sh remove takes .env and the marker, BEFORE the lock
# release. The lock's `.env` check skips another worktree's marked .env, never this one's. A
# deploy gate and a lock-mode run still hold the lock whole, and a take waits for them.
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
# THE COPY's name is exported by this script alone, never taken from the caller
unset COBALT_DEV_DB_NAME

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
HERE=$(cd "$(dirname "$0")" && pwd)

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -ge 2 ] || refuse "usage: gate.sh <worktree name> <probe|offline|withdb|livenote|all> [--deselect <test id>]… [--tickers <A,B,…>] [--migration] [--deploy] [--deploy-gate]"
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
deploy_gate=""
copy_on=""
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
        --deploy-gate) deploy_gate=1; shift ;;
        --copy) copy_on=1; shift ;;
        *) refuse "unknown argument '$1'" ;;
    esac
done
case "$mode" in
    withdb|all) ;;
    *) [ -z "$deselects$tickers$migration$deploy" ] || refuse "--deselect, --tickers, --migration and --deploy belong to withdb and all" ;;
esac
case "$mode" in
    offline|all) ;;
    *) [ -z "$deploy_gate" ] || refuse "--deploy-gate belongs to offline and all" ;;
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

for title, key in (("OFFLINE", "offline"), ("OFFLINE OPS", "offline_ops"), ("PROOF ONLY", "proof"), ("PASS 1", "pass1"), ("FORWARD", "forward"),
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
OFFLINE_OPS=$(cat "$tmp/offline_ops")
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

# ---- the copy: `## COPY CREATE` and `## COPY DROP`, both or neither (THE COPY above) -------------
python3 - "$lists" "$tmp" <<'PY' || { rm -rf "$tmp"; refuse "gate-lists.md holds half a copy mode: $lists"; }
import re, sys
lines = open(sys.argv[1], encoding="utf-8").read().splitlines()
out = sys.argv[2]

sections, title = {}, None
for line in lines:
    if line.startswith("## "):
        title = line[3:].strip()
        sections[title] = []
    elif title is not None and line.strip():
        sections[title].append(line.strip())

def one(title):
    body = sections[title]
    if len(body) != 1 or not re.fullmatch(r"`[^`]+`", body[0]):
        sys.exit("## %s: not ONE backticked line" % title)
    if body[0].count("<COPY>") != 1:
        sys.exit("## %s: not exactly one <COPY>" % title)
    return body[0][1:-1]

have = [t for t in ("COPY CREATE", "COPY DROP") if t in sections]
if len(have) == 1:
    sys.exit("only ## %s" % have[0])
if have:
    for title, key in (("COPY CREATE", "copy_create"), ("COPY DROP", "copy_drop")):
        open("%s/%s" % (out, key), "w", encoding="utf-8").write(one(title))
PY
COPY_CREATE=""
COPY_DROP=""
if [ -f "$tmp/copy_create" ]; then
    COPY_CREATE=$(cat "$tmp/copy_create")
    COPY_DROP=$(cat "$tmp/copy_drop")
fi
[ -z "$deploy" ] || [ -n "$PASS1_DEPLOY" ] || { rm -rf "$tmp"; refuse "--deploy: ## PASS 1 does not hold ' --db-only' exactly once: $lists"; }
# THE COPY is ON only with --copy AND both sections (check O2, A1): a call without --copy is lock mode
if [ -n "$copy_on" ]; then
    case "$mode" in
        withdb|all) ;;
        *) rm -rf "$tmp"; refuse "--copy belongs to withdb and all" ;;
    esac
    [ -n "$COPY_CREATE" ] || { rm -rf "$tmp"; refuse "--copy needs both ## COPY CREATE and ## COPY DROP in gate-lists.md: $lists"; }
fi

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
        [ -e "$f" ] || continue
        # THE COPY: another worktree's marked .env is its copy's, not the lock; this one's never skips
        n=${f%/.env}
        n=${n##*/}
        [ "$n" = "$name" ] || [ ! -e "$WT/.devdb-copies/$n" ] || continue
        held="$held $f"
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

# release [short]: `short` is THE COPY's release after the create: its `.env: removed` goes to the
# log only, so stdout keeps the one `.env: removed` of the step's end
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
    if [ "${1:-}" = short ]; then
        note ".env: removed"
    else
        say ".env: removed"
    fi
}

# ---- the copy (THE COPY above) ----------------------------------------------------------------
copy=""
made=""
placed=""

# copy_name: the copy's name into $copy; refused over 50 characters in all, never truncated
copy_name() {
    [ -f "$HERE/devdb-copy-env.sh" ] || refuse "copy mode: devdb-copy-env.sh is not beside gate.sh: $HERE/devdb-copy-env.sh"
    # check O3: only `-` is mapped, so two worktrees never share a copy name
    case "$name" in
        *[!a-z0-9-]*) refuse "copy mode needs a worktree name of [a-z0-9-]" ;;
    esac
    copy="cobalt_dev_$(printf '%s' "$name" | tr 'A-Z' 'a-z' | tr -c 'a-z0-9' '_')"
    [ "${#copy}" -le 50 ] || refuse "copy name too long: $copy (${#copy} characters; 50 in all)"
}

# copy_cmd <command>: the list line with its one <COPY> token replaced by the copy's name
copy_cmd() {
    printf '%s' "${1%%<COPY>*}$copy${1#*<COPY>}"
}

# copy_create: a leftover of this worktree dropped (logged, not fatal), then the create. `made` is
# set BEFORE the create: a signal that lands while it runs is handled after it returns, and the trap
# then drops the copy (check O1); a create that fails clears it, so nothing is dropped (test (7))
copy_create() {
    run "$(copy_cmd "$COPY_DROP")" || note "the leftover drop of $copy exited non-zero (not fatal)"
    made=1
    run "$(copy_cmd "$COPY_CREATE")" || { made=""; say "copy not created"; exit 1; }
    say "copy: $copy created"
}

# copy_drop: the drop, with COBALT_DEV_DB_NAME unset; 1 when it fails
copy_drop() {
    made=""
    unset COBALT_DEV_DB_NAME
    if run "$(copy_cmd "$COPY_DROP")"; then
        say "copy: $copy dropped"
        return 0
    fi
    say "copy: $copy NOT dropped"
    return 1
}

# copy_env <place|remove>: devdb-copy-env.sh beside this script, its output to the log
copy_env() {
    note "\$ sh $HERE/devdb-copy-env.sh $1 $name"
    COBALT_DEV_DB_NAME=$copy sh "$HERE/devdb-copy-env.sh" "$1" "$name" >> "$log" 2>&1
    crc=$?
    note "[exit $crc]"
    return "$crc"
}

# copy_end: step 5 — the drop, the `.env` and the marker removed and proven gone; 1 on a failure
copy_end() {
    cst=0
    [ -z "$made" ] || copy_drop || cst=1
    if [ -n "$placed" ]; then
        placed=""
        copy_env remove || cst=1
        note "\$ ls $dir/.env $WT/.devdb-copies/$name"
        if [ -e "$dir/.env" ] || [ -e "$WT/.devdb-copies/$name" ]; then
            say ".env: STILL PRESENT — $dir/.env"
            return 1
        fi
        note "No such file or directory"
        say ".env: removed"
    fi
    return "$cst"
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
    # THE COPY: dropped and its .env and marker removed BEFORE the lock release
    if [ -n "$made$placed" ]; then
        copy_end || { [ "$st" -ne 0 ] || st=1; }
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

# proof_clean [<copy>]: on cobalt_dev, or with THE COPY's name on that copy, whose two lines go to
# the log only (stdout keeps today's lines)
proof_clean() {
    on=${1:-cobalt_dev}
    tell=say
    [ -z "${1:-}" ] || tell=note
    run "$PROOF"
    rc=$?
    first=$(plain | sed -n '1p')
    case "$first" in
        *"on $on"*) ;;
        *) say "cobalt_dev not at $level at the start: the proof-only is not on $on — $first"; exit 5 ;;
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
    $tell "proof-only: on $on, nothing CHANGED — the table is in the log (W (b))"
    $tell "LEVEL $level"
}

# ---- the modes --------------------------------------------------------------------------------
# ops_reason (card 2026-10-13/521 T2): why `## OFFLINE OPS` runs, into OPS_WHY; empty when it does
# not. With --deploy-gate always (`deploy gate`); otherwise only when the branch's diff from
# `git merge-base main HEAD` touches ops/, tests/ops/, docs/40 - DevDocs/prompts/ or .claude/ (the
# first such path); a merge-base or a diff that fails → run (`no base`). The paths are read
# unquoted (core.quotePath=false): a quoted non-ASCII name would miss the prefixes (check O1)
ops_reason() {
    OPS_WHY=""
    if [ -n "$deploy_gate" ]; then
        OPS_WHY="deploy gate"
        return
    fi
    base=$(git -C "$dir" merge-base main HEAD 2>/dev/null) && [ -n "$base" ] || { OPS_WHY="no base"; return; }
    paths=$(git -C "$dir" -c core.quotePath=false diff --name-only --no-renames "$base" 2>/dev/null) || { OPS_WHY="no base"; return; }
    OPS_WHY=$(printf '%s\n' "$paths" | grep -E '^(ops/|tests/ops/|docs/40 - DevDocs/prompts/|\.claude/)' | head -n 1)
}

do_offline() {
    suite "$OFFLINE" || exit 1
    p0=$P
    ops_reason
    if [ -n "$OPS_WHY" ]; then
        say "tests/ops: run ($OPS_WHY)"
        suite "$OFFLINE_OPS" || exit 1
        P=$((p0 + P))
    else
        say "tests/ops: skipped (no ops paths)"
    fi
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
    if [ -n "$copy" ]; then
        # THE COPY: made under the lock, the lock given back, the rest on the copy
        copy_create
        release short || exit 1
        placed=1
        copy_env place || { say "copy: the .env of $copy was not placed (log)"; exit 1; }
        export COBALT_DEV_DB_NAME=$copy
        fingerprint || { say "the fingerprint query failed on $copy (log)"; exit 1; }
        fp0=$FPV
        note "F0 ($copy): $fp0"
        proof_clean "$copy"
    fi
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
    if [ -n "$copy" ]; then
        copy_end || exit 1
    else
        release || exit 1
    fi
    say "with-DB $((p1 + p2))/0"
    [ -z "$skips" ] || say "$skips"
    if [ -n "$stray" ]; then
        say "DECISION 0: the suite left $stray rows on cobalt_dev"
        exit 1
    fi
}

lockway=""
# THE COPY: the name is read, and refused, before anything runs
case "$mode" in
    withdb|all) [ -z "$copy_on" ] || copy_name ;;
esac
case "$mode" in
    probe) do_probe ;;
    offline) do_offline ;;
    withdb) do_withdb ;;
    livenote) do_livenote ;;
    all) do_offline; do_withdb; do_livenote ;;
esac
exit 0
