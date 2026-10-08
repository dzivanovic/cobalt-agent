#!/bin/sh
# The installed launcher (installed 2026-09-30, his R63); its kinds are tested in tests/ops/.
#
# desk-launch.sh <kind> [<card or prompt>] [PASS-2] [<resume step>] — the one way the CTO desk
# launches ANY session. His rulings: cto-2026-09-30.md R34 (the brain's RULED PROCESS, item 4),
# R38 (the second loop: the script RUNS the launch; no launch-row field, no launch-row gate),
# R45 (the third pass: the kinds `desk` and `prompt`; `check <card> PASS-2`) and the nightly
# close ("Yes, I want all this", brain tab, 09-30: the kind `close`).
#
# WOULD INSTALL AT: /Users/cobalt/.claude/ops/desk-launch.sh
# (the desk's tracked allow "Bash(sh /Users/cobalt/.claude/ops/*)" already covers it). EVERY ops
# script installs under /Users/cobalt/.claude/ops/ — a path with no space: a quoted spaced script
# path matches no allow string and opens a dialog (scratch item 6b). This script refuses to run
# from a path that holds a space.
#
# WHAT THE DESK TYPES — ONE bare command per launch, and nothing else:
#   sh /Users/cobalt/.claude/ops/desk-launch.sh build  "<absolute card path>"
#   sh /Users/cobalt/.claude/ops/desk-launch.sh check  "<absolute card path>"
#   sh /Users/cobalt/.claude/ops/desk-launch.sh check  "<absolute card path>" PASS-2   (house B + the second Opus)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh deploy "<absolute card path>"
#   sh /Users/cobalt/.claude/ops/desk-launch.sh deploy "<absolute card path>" STEP-D0  (the one resume)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh recut "<absolute deploy card path>"    (a deploy whose
#        gate FAILED, recut and relaunched in ONE call: card 2026-10-03/03 adoption-scripts L5)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh devfix "<absolute card path>"          (one dev-maintenance
#        job on cobalt_dev: DEVFIX-HUB.md, card 12 devfix-route; a resume names its step as build)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh build|check "<card>" [PASS-2] <step>   (a NEW worker at
#        that CONTINUE step — only when the launch line must change, the session died, the
#        judgment seat finds a misread, or the worker measures above 250,000 tokens)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh desk                                   (its successor)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "<absolute prompt path>"        (a one-off prompt)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh brain "<absolute handover path>" [--fable]  (the
#        standing brain seat on BRAIN-HUB.md, card 07 brain-hub; after he has stopped the brain
#        before it; Opus by default, `--fable` for a design or high-effort session, card 07b P5)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh close <YYYY-MM-DD> [<step>]            (the nightly close
#        of that day: after the 21:00 ET pause on the day itself, or any time later for a missed
#        night — the morning desk's first act; <step> = a NEW worker at that CONTINUE step)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh install-ops                            (links the ops
#        scripts into /Users/cobalt/.claude/ops; the desk runs it after a deploy; launches nothing)
# The desk types no `cd`, no `git worktree add` and no `claude --bg`: its own `claude --bg`
# allow goes (DESK-LINE.md), so a launch outside this script has no listed string. Before the
# command the desk writes its own §4 launch row (L34) — no hub reads it; after it the desk
# reads LIST.
#
# WHAT IT DOES: reads the card or prompt, refuses what must not launch, then RUNS the launch
# itself, in a subshell of its own (the desk's cwd does not move):
#   build : `git -C /Users/cobalt/cobalt worktree add -b <BRANCH> <worktree> <BASE>` when the
#           worktree does not exist yet; `cd <worktree>`; the fixed file's `claude --bg` line.
#   check : `cd <the job's worktree>`; the fixed file's `claude --bg` line (PASS-2: the same
#           line, its message starting `PASS-2. `).
#   deploy: `git -C /Users/cobalt/cobalt worktree add -b <BRANCH> <worktree> main` (not on a
#           STEP-D0 resume); `cd /Users/cobalt/cobalt`; the fixed file's `claude --bg` line.
#   devfix: as build — `git -C /Users/cobalt/cobalt worktree add -b <BRANCH> <worktree> <BASE>`
#           when the worktree does not exist yet; `cd <worktree>`; DEVFIX-HUB.md's `claude --bg`
#           line with <card>, <job>, <worktree>, <table>, <proof test> filled.
#   recut : for a deploy card whose REPORT's last line starts `FAILED` and names no `rollback:
#           used`: `gate-clean.sh <card>` (beside this script; its refusals stand); the card's
#           BRANCH, WORKTREE and TAG get `-attempt<n>` (n = the highest attempt present on those
#           values, on a branch, tag, worktree or report of the same names, + 1; the first gate is
#           attempt 1) and REPORT `<its name>-attempt<n>.md`, each printed `KEY: old -> new` after
#           `RECUT: <job> attempt <n>`; `desk-commit.sh` commits the card; `desk-row.sh RECORD
#           "RECUT <job> attempt <n> — <the failed last line>"`; then this script's `deploy` kind on
#           the recut card (its own checks, its worktree add, its line, its WATCH line).
#           DESK_LAUNCH_DRY=1 makes that last launch dry; the recut's own steps run.
#   desk  : `cd /Users/cobalt/cobalt`; the wake-up's own launch line — the ONE backticked
#           `claude --bg …` span on the `- LAUNCH` line of prompts/CTO-DESK-WAKEUP.md.
#   prompt: `cd <the cwd the prompt names>`; the prompt's own launch line — the ONE
#           `claude --bg "Read '<that prompt file>' and follow it exactly." …` it holds (a line
#           of its own, or a backticked span), for a drafter, a tribunal and its seats.
#           READ-ONLY LINES ONLY: every write-path launch is a fixed file.
#   brain : `cd /Users/cobalt/cobalt`; BRAIN-HUB.md's `claude --bg` line with <handover> filled;
#           with `--fable`, its one ` --model claude-opus-5-5 ` becomes ` --model claude-fable-5-1 `.
#   close : `cd /Users/cobalt/cobalt`; CLOSE-HUB.md's `claude --bg` line, `<date>` and `<mmdd>`
#           filled (a resume: its message starting `CONTINUE: <step>. `).
#   install-ops: no launch. Every regular file ops/desk/*.sh and ops/desk/*.py of the repo
#           (/Users/cobalt/cobalt) is linked into the link folder (/Users/cobalt/.claude/ops, or
#           $COBALT_OPS_LINK_DIR in tests/ops/test_install_ops.py) as <link folder>/<name> ->
#           <repo>/ops/desk/<name>, printing `LINKED <name>`; a plain regular file at the name is
#           replaced by that link in one rename (card 2026-10-08 106 G3), printing
#           `REPLACED: <name>` when it differed from the repo copy (`cmp -s`) and nothing when
#           identical; a failed replace is `REFUSED: install-ops: the replace failed: <path>`,
#           exit 1. A link (to the repo, elsewhere or dangling) or any other kind at the name is
#           left untouched and printed `KEPT <name>`; a link is never re-pointed. Last line
#           `install-ops: <n> linked, <r> replaced, <m> kept`, exit 0. No argument (one more is
#           REFUSED).
# It prints each command on stderr as `RUN: <command>` before it runs it, and exits with the
# status of the last one. DESK_LAUNCH_DRY=1 in the environment prints the three commands on
# stdout and runs nothing (for the scratch test; the desk's line has no string for it).
# A build, check, deploy, devfix or close launch that exits 0 ends its stdout with
# `WATCH: sh <this script's folder>/desk-watch.sh <kind> "<card or close report>"` (card 21 L4);
# under DESK_LAUNCH_DRY=1 that line follows the dry lines on stderr.
#
# FIRST, every kind but `desk` runs the desk-size guard (`desk-context.sh --guard`, cto-2026-10-01
# R8): at 300,000 tokens or more it prints "REFUSED: desk at <n> tokens — REFRESH first" on
# stdout and this script exits 3, nothing run.
#
# IT REFUSES (exit 1, "REFUSED: <reason>" on stderr, nothing run):
#   - to run at all from a path that holds a space (install under /Users/cobalt/.claude/ops/);
#   - a kind that is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops; a fixed file, a wake-up
#     file or a prompt file still a draft, not committed on main, or changed since its commit;
#   - kind `recut`: any argument after the card ("recut takes one argument, the card"), before
#     the desk-size guard;
#   - kind `close`: a date not YYYY-MM-DD, a date after today (ET), today's date before 21:00 ET,
#     a first launch whose close report already exists, a resume without it, or ANY live
#     `deploy-hub-` session (read from `claude agents --json`; unreadable = refused);
#   - kind `prompt`: a line whose permission mode is a write-path mode — `acceptEdits` or
#     `dontAsk` (the fixed files' mode) — or `bypassPermissions`, or not stated; the close file
#     handed over as a prompt; a line that carries a write string — `git add`, `git commit`, `git merge` (also
#     in their `git -C <path>` spelling, and the whole-git `Bash(git *)`), `uv run`,
#     `launchctl`, `COBALT_ENV=` (card 21 F5: a string in --disallowedTools is never one; one in
#     --allowedTools passes when the prompt's one `RULINGS:` line cites rows that are HIS RULING +
#     APPROVED and committed, L7a); a line without the two dialog denies (L63), without
#     `--remote-control` and `--name`, or that reads another file than the one named; a card
#     or a fixed file handed over as a prompt; a prompt that names no cwd; a line that names
#     `--name brain` or `--remote-control brain` (the brain seat launches by the kind `brain` only);
#     a line that types `PROD-READ:` other than the stamp this script appends after `follow it
#     exactly.` for a proven production-read RULINGS row (card 21 guard-g2 R1, his 2026-10-06 R511;
#     kept for prompts in flight, read by no rule since his 2026-10-08 R686);
#   - kind `desk`: a wake-up line that does not name `cto-desk`;
#   - kind `brain`: a handover that is not a .md file directly under $PROMPTS/<YYYY-MM-DD>/, holds
#     a character outside [A-Za-z0-9 ._/-] or '..', does not exist, or still holds a «FILL token;
#     a BRAIN-HUB.md not installed, not committed or changed, without exactly one launch line, or
#     whose line does not name the seat `brain` or does not hold ` --model claude-opus-5-5 ` exactly
#     once; a third argument other than `--fable`; and ANY live session named `brain` (read from
#     desk-list.sh beside this script; unreadable = refused): a brain is stopped only on his word
#     (2026-09-30 R76), so its successor launches after he has stopped it;
#   - PASS-2 on anything but a check whose report's last line is pass 1's `CHECK DONE` with
#     `house B: needed`; a first check launch whose report already exists;
#   - an incomplete card: a header key its kind needs is empty, a «FILL token stands
#     anywhere, a body section its kind needs is missing, the card is not committed on main
#     or differs from its commit (this is the whole of the card gate: no launch row is read);
#   - a worktree outside the approved pattern /Users/cobalt/cobalt-wt/<one directory name>;
#   - a deploy while the cobalt_dev lock is held: any /Users/cobalt/cobalt-wt/*/.env, or the lock
#     directory /Users/cobalt/cobalt-wt/.cobalt_dev.lock (L76). A build or check LAUNCHES while
#     another session holds the lock (L76 as amended, his 2026-10-01 R20, card 07 devdb-lock): it
#     takes the lock at its with-DB steps through take-devdb-lock.sh, and waits for it there;
#   - kind `devfix`: TABLE not system.<name> or user.<name> (<name> in [a-z0-9_]); PROOF TEST not
#     tests/cobalt/<file>.py with an optional ::<name> in [A-Za-z0-9_:.]; REPORT not
#     $REPORTS/devfix-<name>.md, or already present on a first launch; BASE not a commit on main;
#     the cobalt_dev lock held (any worktree's .env, or the lock directory); a worktree on
#     another branch than the card's;
#   - a resume (a NEW worker at a CONTINUE step; a deploy's STEP-D0) while another worktree's .env
#     exists. ONE EXCEPTION (scratch D1): the job's OWN worktree's .env, and for a deploy its own
#     lock directory, are skipped — the fixed file's RECOVERY clears them first;
#   - a launch line in which an absolute path sits under no --add-dir (the 09-30 outage);
#   - a production db query string in a deploy card that contains "%";
#   - kinds build, check, deploy, devfix (card 21 L1): a `<date> R<n>` of RULINGS, or the row a
#     HOUSE A / HOUSE B line names after `overruled`, that is not ONE line of
#     $REPORTS/cto-<date>.md starting `| R<n> |` with HIS RULING and APPROVED, committed so;
#   - kind check, not PASS-2 (L2): a build report whose last non-blank line does not start
#     `BUILT · job: <JOB> · tip: <TIP>`; on a first pass-1 launch, a branch head that TIP is not
#     an ancestor of, or that adds more than docs past TIP (check O2);
#   - kind deploy, not STEP-D0 (L3): a `## SHIPS` table with no row, or a TIP head that is the
#     branch head of no row (R41); a `## SHIPS` row whose branch head TIP does not list (check O1),
#     whose check report is absent, uncommitted or changed, whose last line lacks a literal of the row or names another tip, whose branch head
#     moved, whose code tip is not its ancestor, or whose head adds more than docs past it.
#
# THE LAUNCH LINE HAS ONE HOME: the fixed file's single line beginning "claude --bg " (the
# wake-up's LAUNCH line for `desk`; the prompt's own line for `prompt`). This script copies
# that line, fills its tokens from the card and runs it with `eval`; every value it fills is
# checked against a closed character set first. It holds no allow string of its own except
# the two patterns the deploy line's tokens expand to (DEPLOY-HUB.md).

export LC_ALL=C
set -u

# COBALT_REPO_ROOT and COBALT_WT_ROOT stand in for these two in tests/ops/test_devdb_lock.py only
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
PROMPTS="$REPO/docs/40 - DevDocs/prompts"
REPORTS="$REPO/docs/40 - DevDocs/reports"

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

# an ops script runs only from a path with no space (scratch item 6b; install: /Users/cobalt/.claude/ops/)
case "$0" in
    *" "*) refuse "desk-launch.sh runs only from a path with no space (install it under /Users/cobalt/.claude/ops/): $0" ;;
esac

# committed <what> <file>: the file is on main, unchanged and unstaged since its commit
committed() {
    [ -n "$(git -C "$REPO" log -1 --format=%H -- "$2")" ] || refuse "$1 is not committed on main: $2"
    git -C "$REPO" diff --quiet -- "$2" || refuse "$1 differs from its commit: $2"
    git -C "$REPO" diff --cached --quiet -- "$2" || refuse "$1 is staged, not committed: $2"
}

# check_paths <line>: every absolute /Users/ path inside an allow string sits under one --add-dir root
check_paths() {
    bad=$(printf '%s\n' "$1" | awk '
{
    n = split($0, w, " ")
    r = 0
    for (i = 1; i < n; i++) if (w[i] == "--add-dir") roots[++r] = w[i + 1]
    inallow = 0
    for (i = 1; i <= n; i++) {
        if (w[i] == "--allowedTools") { inallow = 1; continue }
        if (w[i] == "--disallowedTools") inallow = 0
        if (!inallow) continue
        k = index(w[i], "/Users/")
        if (k == 0) continue
        p = substr(w[i], k)
        gsub(/[")*]+$/, "", p)
        ok = 0
        for (j = 1; j <= r; j++) if (p == roots[j] || index(p, roots[j] "/") == 1) ok = 1
        if (!ok) print p
    }
}')
    [ -z "$bad" ] || refuse "a listed path sits under no --add-dir: $bad"
}

# the folder this script was called from (the WATCH line names desk-watch.sh beside it)
here=$(cd "$(dirname "$0")" && pwd)

# run_launch <dir> <line> <note> [<watch>]: the cd and the line; DESK_LAUNCH_DRY=1 prints both, runs
# nothing. <watch> (card 21 L4) is printed as the last stdout line of a launch that exits 0; under
# DESK_LAUNCH_DRY=1 it follows the dry lines on stderr, so the dry stdout stays the cd and the line
run_launch() {
    if [ "${DESK_LAUNCH_DRY:-0}" = "1" ]; then
        printf '%s\n' "cd $1"
        printf '%s\n' "$2"
        [ -z "${4:-}" ] || printf '%s\n' "$4" >&2
        exit 0
    fi
    [ -d "$1" ] || refuse "no such directory: $1"
    printf 'RUN: cd %s\n' "$1" >&2
    cd "$1" || refuse "cd failed: $1"
    printf 'RUN: %s\n' "$2" >&2
    eval "$2"
    status=$?
    printf '%s\n' "$3" >&2
    [ "$status" -ne 0 ] || [ -z "${4:-}" ] || printf '%s\n' "$4"
    exit "$status"
}
# watch_line <kind> <card or close report>: the line the desk runs in the background
watch_line() {
    printf 'WATCH: sh %s/desk-watch.sh %s "%s"' "$here" "$1" "$2"
}

# the ruling rows (card 21 L1): every `<date> R<n>` of RULINGS (`none` needs no row) and the row
# a HOUSE A / HOUSE B line names after `overruled` is ONE line of $REPORTS/cto-<date>.md that starts
# `| R<n> |`, holds HIS RULING and APPROVED, and stands so in the committed file (BUILD-HUB.md
# `## AUTHORIZATION`); the prompt kind's RULINGS line is read the same way (F5)
ruling_row() {
    rdate=${1%% *}
    rn=${1#* }
    case "$rdate" in
        20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
        *) refuse "incomplete card: RULINGS item '$1' is not '<date> R<n>'" ;;
    esac
    case "$rn" in
        R*) ;;
        *) refuse "incomplete card: RULINGS item '$1' is not '<date> R<n>'" ;;
    esac
    case "${rn#R}" in
        ""|*[!0123456789]*) refuse "incomplete card: RULINGS item '$1' is not '<date> R<n>'" ;;
    esac
    rfile="$REPORTS/cto-$rdate.md"
    n=0
    [ ! -f "$rfile" ] || n=$(grep -c "^| $rn |" "$rfile")
    [ "$n" -ne 0 ] || refuse "ruling $1: no such row in $rfile — the desk writes his row and commits it before the launch"
    [ "$n" -eq 1 ] || refuse "ruling $1: not one row ($n lines start '| $rn |' in $rfile) — keep one row per number"
    row=$(grep "^| $rn |" "$rfile")
    case "$row" in
        *"HIS RULING"*APPROVED*|*APPROVED*"HIS RULING"*) ;;
        *) refuse "ruling $1: not HIS RULING + APPROVED: $row — launch after his word is recorded" ;;
    esac
    [ -n "$(git -C "$REPO" log -1 --format=%H -S"| $rn |" -- "$rfile")" ] \
        && git -C "$REPO" show "HEAD:docs/40 - DevDocs/reports/cto-$rdate.md" 2>/dev/null | grep -q -x -F -- "$row" \
        || refuse "ruling $1: not committed — commit $rfile"
}
# ruling_items <list>: ruling_row for each comma-separated `<date> R<n>`
ruling_items() {
    rest=$1
    while [ -n "$rest" ]; do
        item=${rest%%,*}
        if [ "$item" = "$rest" ]; then rest=""; else rest=${rest#*,}; fi
        item=$(printf '%s' "$item" | sed 's/^[[:space:]]*//; s/[[:space:]]*$//')
        ruling_row "$item"
    done
}

# tool_list <line> <allow|deny|rest>: the words of a launch line in its --allowedTools list, its
# --disallowedTools list, or neither; a "…" span is one word, a list ends at the next unquoted --flag
tool_list() {
    printf '%s\n' "$1" | awk -v want="$2" '
{
    s = $0; n = length(s); tok = ""; inq = 0; mode = "rest"; out = ""
    for (i = 1; i <= n + 1; i++) {
        c = (i <= n) ? substr(s, i, 1) : " "
        if (c == "\\" && i < n) { tok = tok c substr(s, i + 1, 1); i++; continue }
        if (c == "\"") inq = !inq
        if (c == " " && !inq) {
            if (tok != "") {
                if (tok == "--allowedTools") mode = "allow"
                else if (tok == "--disallowedTools") mode = "deny"
                else if (substr(tok, 1, 2) == "--") mode = "rest"
                if (mode == want) out = out " " tok
            }
            tok = ""
        } else tok = tok c
    }
    print out
}'
}

[ "$#" -ge 1 ] || refuse "usage: desk-launch.sh <build|check|deploy|devfix> <card> [PASS-2] [<resume step>] | desk | prompt <prompt file> | brain <handover file> [--fable] | close <YYYY-MM-DD> [<resume step>] | install-ops"
kind=$1
# recut takes the card and nothing else, refused before anything runs (card 03 L5, AMENDED
# 10-03, ASK DESK 13: an ignored argument is a guess)
[ "$kind" != "recut" ] || [ "$#" -le 2 ] || refuse "recut takes one argument, the card"

# ---- the desk-size guard (cto-2026-10-01 R8): every kind but `desk`, before anything else -----
# desk-context.sh --guard, installed beside this script, refuses while the desk measures
# 300,000 tokens or more; this script then exits with its status and its line unchanged. The
# successor launch (`desk`) is never guarded, so a REFRESH can always complete.
if [ "$kind" != "desk" ]; then
    sh "$(dirname "$0")/desk-context.sh" --guard || exit $?
fi

# ---- kind close: the nightly close of one day (RULED — THE NIGHTLY CLOSE) -----------------------
if [ "$kind" = "close" ]; then
    [ "$#" -ge 2 ] && [ "$#" -le 3 ] || refuse "usage: desk-launch.sh close <YYYY-MM-DD> [<resume step>]"
    cday=$2
    step=${3:-}
    case "$cday" in
        20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
        *) refuse "close: '$cday' is not a date YYYY-MM-DD" ;;
    esac
    [ "$(date -j -f %Y-%m-%d "$cday" +%Y-%m-%d 2>/dev/null)" = "$cday" ] || refuse "close: '$cday' is not a calendar date"
    fixed="$PROMPTS/CLOSE-HUB.md"
    [ -f "$fixed" ] || refuse "the fixed file is not installed: $fixed"
    if grep -q '«INSTALL' "$fixed"; then
        refuse "the fixed file still carries its «INSTALL token (his approval row is not filled): $fixed"
    fi
    committed "the fixed file" "$fixed"
    # the hour: after the 21:00 ET pause on the day itself; any later day = a missed night
    today=$(TZ=America/New_York date +%Y-%m-%d)
    hour=$(TZ=America/New_York date +%H)
    cn=$(printf '%s' "$cday" | tr -d '-')
    tn=$(printf '%s' "$today" | tr -d '-')
    [ "$cn" -le "$tn" ] || refuse "close: $cday is after today ($today, ET)"
    if [ "$cn" -eq "$tn" ] && [ "$hour" -lt 21 ]; then
        refuse "close: today's close launches after the 21:00 ET pause; it is ${hour}h ET"
    fi
    # never while a deploy hub is live (the close commits and pushes main)
    live=$(claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
except Exception:
    print("UNREADABLE")
    sys.exit(0)
hit = 0
for a in rows:
    if a.get("pid") and str(a.get("name", "")).startswith("deploy-hub-"):
        print("%s %s" % (a.get("id", "?"), a.get("name")))
        hit = 1
if not hit:
    print("NONE")
' 2>/dev/null || echo UNREADABLE)
    case "$live" in
        NONE) ;;
        ""|UNREADABLE*) refuse "close: the session list is unreadable (claude agents --json); a close never launches beside a deploy it cannot rule out" ;;
        *) refuse "close: a deploy hub is live — the close waits for its stop line: $live" ;;
    esac
    creport="$REPORTS/close-$cday.md"
    if [ -n "$step" ]; then
        case "$step" in
            *[!A-Za-z0-9.\ -]*) refuse "resume step '$step' holds a character outside [A-Za-z0-9 .-]" ;;
        esac
        [ -f "$creport" ] || refuse "a close resume needs its report: $creport"
    else
        [ ! -e "$creport" ] || refuse "the close report already exists: $creport (a new worker names its CONTINUE step)"
    fi
    n=$(grep -c '^claude --bg ' "$fixed")
    [ "$n" -eq 1 ] || refuse "the fixed file must hold exactly one launch line; found $n in $fixed"
    mmdd=$(printf '%s' "$cday" | cut -c6-7,9-10)
    line=$(grep '^claude --bg ' "$fixed" | sed -e "s|<date>|$cday|g" -e "s|<mmdd>|$mmdd|g")
    [ -z "$step" ] || line=$(printf '%s\n' "$line" | sed "s|^claude --bg \"Read |claude --bg \"CONTINUE: $step. Read |")
    case "$line" in
        *"<"*|*">"*) refuse "the launch line still holds an unfilled token" ;;
    esac
    check_paths "$line"
    run_launch "$REPO" "$line" "reminder: no desk commit on main and no deploy launch until the close's stop line; the close pushes main itself (L55 as amended)" "$(watch_line close "$creport")"
fi

# ---- kind desk: the wake-up's own launch line (the successor at REFRESH, L64) ----------------
if [ "$kind" = "desk" ]; then
    [ "$#" -eq 1 ] || refuse "usage: desk-launch.sh desk"
    wake="$PROMPTS/CTO-DESK-WAKEUP.md"
    [ -f "$wake" ] || refuse "no wake-up file: $wake"
    committed "the wake-up file" "$wake"
    n=$(grep -c '^- LAUNCH .*`claude --bg ' "$wake")
    [ "$n" -eq 1 ] || refuse "the wake-up must hold exactly one SEAT PROFILE LAUNCH line; found $n"
    line=$(sed -n 's/^- LAUNCH .*`\(claude --bg [^`]*\)`.*$/\1/p' "$wake")
    [ -n "$line" ] || refuse "no backticked launch line on the wake-up's LAUNCH line"
    case "$line" in
        *"--remote-control cto-desk --name cto-desk"*) ;;
        *) refuse "the wake-up's launch line does not name cto-desk" ;;
    esac
    case "$line" in
        *bypassPermissions*) refuse "the wake-up's launch line carries bypassPermissions (L55)" ;;
    esac
    check_paths "$line"
    run_launch "$REPO" "$line" "reminder: the HANDOVER line and HANDOVER DONE message are yours (checklist REFRESH HOW); the successor ends you"
fi

# ---- kind prompt: a one-off prompt's own launch line, read-only lines only ------------------
if [ "$kind" = "prompt" ]; then
    [ "$#" -eq 2 ] || refuse "usage: desk-launch.sh prompt <absolute prompt path>"
    pfile=$2
    case "$pfile" in
        "$PROMPTS"/*.md) ;;
        *) refuse "a prompt lives under $PROMPTS" ;;
    esac
    case "$pfile" in
        *[!A-Za-z0-9\ ._/-]*) refuse "the prompt path holds a character outside [A-Za-z0-9 ._/-]" ;;
        *..*) refuse "the prompt path holds '..'" ;;
        *-card.md) refuse "a card is launched by its kind (build, check, deploy), never as a prompt" ;;
        */BUILD-HUB.md|*/CHECK-HUB.md|*/DEPLOY-HUB.md|*/CLOSE-HUB.md|*/CTO-DESK-WAKEUP.md) refuse "a fixed file is launched by its kind, never as a prompt" ;;
    esac
    [ -f "$pfile" ] || refuse "no such prompt: $pfile"
    committed "the prompt" "$pfile"
    n=$(grep -c 'claude --bg "Read ' "$pfile")
    [ "$n" -eq 1 ] || refuse "a prompt must hold exactly one launch line (claude --bg \"Read …); found $n in $pfile"
    line=$(sed -n 's/^\(claude --bg "Read .*\)$/\1/p' "$pfile")
    [ -n "$line" ] || line=$(sed -n 's/^.*`\(claude --bg "Read [^`]*\)`.*$/\1/p' "$pfile")
    [ -n "$line" ] || refuse "the launch line is neither a line of its own nor a backticked span: $pfile"
    # the brain seat has one path, the kind `brain` (card 07 B5, check O1; L3): each value of
    # --name and --remote-control as eval hands it to claude, blanks and quotes stripped (check r2 O1)
    seats=$(printf '%s\n' "$line" | grep -o -e '--name[ =]*[^ ]*' -e '--remote-control[ =]*[^ ]*' | sed -e 's/^--[a-z-]*[ =]*//' | tr -d "\"'")
    case "
$seats
" in
        *"
brain
"*) refuse "a brain seat launches by desk-launch.sh brain <handover>" ;;
    esac
    case "$line" in
        *"Read '$pfile' and follow it exactly."*) ;;
        *) refuse "the launch line does not read this prompt file by its absolute path" ;;
    esac
    # every write-path launch is a fixed file: refuse the write-path modes and the write strings
    case "$line" in
        *bypassPermissions*) refuse "bypassPermissions (L55)" ;;
    esac
    pm_n=$(printf '%s\n' "$line" | grep -o -e '--permission-mode' | wc -l | tr -d ' ')
    [ "$pm_n" -le 1 ] || refuse "the launch line states --permission-mode more than once"
    [ "$pm_n" -eq 1 ] || refuse "the launch line states no --permission-mode (L62)"
    # the mode word: quotes, '=' and blanks stripped (scratch test 2, D4); only auto and plan pass
    pm=$(printf '%s\n' "$line" | sed -n 's/.*--permission-mode[ =]*\([^ ]*\).*/\1/p' | tr -d "\"'")
    case "$pm" in
        auto|plan) ;;
        *) refuse "permission mode '$pm': a one-off prompt runs auto or plan; every write-path launch is a fixed file (build, check, deploy, close)" ;;
    esac
    # card 21 F5: a string in --disallowedTools is never a write string; one in --allowedTools passes
    # only when the prompt's one RULINGS line cites rows that are HIS RULING + APPROVED and committed
    # (L7a, ruling_row); one anywhere else on the line, or without such a line, is refused as before
    scan="$(tool_list "$line" allow) $(tool_list "$line" rest)"
    outside=$(tool_list "$line" rest)
    ruled=0
    prulings=$(sed -n 's/^RULINGS:[[:space:]]*//p' "$pfile")
    if [ "$(grep -c '^RULINGS:' "$pfile")" -eq 1 ] && [ -n "$prulings" ] && [ "$prulings" != "none" ]; then
        ( ruling_items "$prulings" ) 2>/dev/null && ruled=1
    fi
    for w in "git add" "git commit" "git merge" "Bash(git *)" "uv run" "launchctl" "COBALT_ENV="; do
        case "$scan" in
            *"$w"*)
                case "$outside" in
                    *"$w"*) ruled=0 ;;
                esac
                [ "$ruled" -eq 1 ] || refuse "write string '$w' on a prompt line: a write-path launch is a fixed file" ;;
        esac
    done
    case "$outside" in
        *"Bash(git -C "*" add "*|*"Bash(git -C "*" commit "*|*"Bash(git -C "*" merge "*) ruled=0 ;;
    esac
    case "$scan" in
        *"Bash(git -C "*" add "*|*"Bash(git -C "*" commit "*|*"Bash(git -C "*" merge "*)
            [ "$ruled" -eq 1 ] || refuse "a git -C write string on a prompt line: a write-path launch is a fixed file" ;;
    esac
    case "$line" in
        *'"AskUserQuestion"'*'"EnterWorktree"'*) ;;
        *) refuse "the launch line does not deny the dialog tools (L63)" ;;
    esac
    case "$line" in
        *"--remote-control "*"--name "*) ;;
        *) refuse "the launch line carries no --remote-control and --name (every helper is visible)" ;;
    esac
    case "$line" in
        *"<"*|*">"*) refuse "the launch line holds an unfilled token" ;;
    esac
    dir=$(sed -n 's/^.*`cd \(\/Users\/cobalt\/[^`]*\)`.*$/\1/p' "$pfile" | sed -n '1p')
    [ -n "$dir" ] || dir=$(sed -n 's/^cd \(\/Users\/cobalt\/.*\)$/\1/p' "$pfile" | sed -n '1p')
    [ -n "$dir" ] || refuse "the prompt names no cwd (a line or a backticked span: cd <absolute path>)"
    case "$dir" in
        "$REPO"|"$WT"/*) ;;
        *) refuse "the prompt's cwd '$dir' is neither $REPO nor under $WT" ;;
    esac
    case "$dir" in
        *[!A-Za-z0-9._/-]*|*..*) refuse "the prompt's cwd holds a character outside [A-Za-z0-9._/-]" ;;
    esac
    # card 21 guard-g2 R1 (his 2026-10-06 R511): a committed, clean prompt whose one RULINGS line
    # cites ONE `<date> R<n>` whose row is HIS RULING + APPROVED and committed (ruling_row), its file
    # clean, and names production reads launches with ` PROD-READ: <date> R<n>` after `follow it
    # exactly.`, kept for prompts in flight and read by no rule since his 2026-10-08 R686. A line that
    # already types `PROD-READ:` is refused unless it holds exactly that stamp, once, in that place;
    # it is then not stamped twice. The row's status cell starts APPROVED (not DISAPPROVED) and it
    # names a production read as words (not `production ready`) (check A1, B4)
    stamp=""
    if [ "$(grep -c '^RULINGS:' "$pfile")" -eq 1 ]; then
        case "$prulings" in
            *,*|"") ;;
            *)
                if ( ruling_row "$prulings" ) 2>/dev/null \
                    && git -C "$REPO" diff --quiet -- "$REPORTS/cto-${prulings%% *}.md" \
                    && grep "^| ${prulings#* } |" "$REPORTS/cto-${prulings%% *}.md" | grep -q -F "| APPROVED" \
                    && grep "^| ${prulings#* } |" "$REPORTS/cto-${prulings%% *}.md" | grep -q -i -E "production reads?([^[:alpha:]]|$)"; then
                    stamp=" PROD-READ: $prulings"
                fi ;;
        esac
    fi
    pre="Read '$pfile' and follow it exactly."
    case "$line" in
        *PROD-READ:*)
            [ -n "$stamp" ] || refuse "the launch line types PROD-READ: but its RULINGS row proves no production read (one row, HIS RULING + APPROVED, committed, naming production reads; his 2026-10-06 R511)"
            pr_n=$(printf '%s\n' "$line" | grep -o -F 'PROD-READ:' | wc -l | tr -d ' ')
            case "$line" in
                *"$pre$stamp\" "*) ;;
                *) pr_n=0 ;;
            esac
            [ "$pr_n" -eq 1 ] || refuse "the launch line types a PROD-READ: marker other than the launcher's stamp '$stamp', once, after 'follow it exactly.' (his 2026-10-06 R511)" ;;
        *)
            [ -z "$stamp" ] || line="${line%%"$pre"*}$pre$stamp${line#*"$pre"}" ;;
    esac
    # check O5, A5: the message eval hands to claude is the Read sentence and, when proven, the
    # stamp, closed there; text after it could join into a marker (`PROD""-READ:`, an empty
    # expansion) that the literal test above never sees
    case "$line" in
        "claude --bg \"$pre$stamp\" "*) ;;
        *) refuse "the launch line types text after 'follow it exactly.' other than the launcher's stamp '$stamp' (his 2026-10-06 R511)" ;;
    esac
    check_paths "$line"
    run_launch "$dir" "$line" "reminder: one Grok hub at a time (L15); the tab and the §5 row are the desk's"
fi

# ---- kind brain: the standing brain seat on its handover file (card 07 brain-hub) -------------
if [ "$kind" = "brain" ]; then
    # card 07b P5 (his 10-04 R189): the line's Opus by default; `--fable` puts Fable on it instead,
    # for a design or high-effort session the brain itself asks for; any other value is refused
    { [ "$#" -eq 2 ] || { [ "$#" -eq 3 ] && [ "$3" = "--fable" ]; }; } \
        || refuse "usage: desk-launch.sh brain <absolute handover path> [--fable]"
    handover=$2
    case "$handover" in
        *..*) refuse "the handover path holds '..': $handover" ;;
        *[!A-Za-z0-9\ ._/-]*) refuse "the handover path holds a character outside [A-Za-z0-9 ._/-]: $handover" ;;
    esac
    # a .md file directly under $PROMPTS/<YYYY-MM-DD>/
    hrest=${handover#"$PROMPTS"/}
    hday=${hrest%%/*}
    hname=${hrest#*/}
    case "$handover" in
        "$PROMPTS"/*/*.md) ;;
        *) refuse "a brain handover lives under $PROMPTS/<YYYY-MM-DD>/: $handover" ;;
    esac
    case "$hday" in
        20[0123456789][0123456789]-[0123456789][0123456789]-[0123456789][0123456789]) ;;
        *) refuse "a brain handover lives under $PROMPTS/<YYYY-MM-DD>/, not '$hday': $handover" ;;
    esac
    case "$hname" in
        */*) refuse "a brain handover lives directly under $PROMPTS/$hday/: $handover" ;;
    esac
    [ -f "$handover" ] || refuse "no such handover: $handover"
    if grep -n '«FILL' "$handover" >&2; then
        refuse "the handover still holds a fill token (the lines above): $handover"
    fi
    fixed="$PROMPTS/BRAIN-HUB.md"
    [ -f "$fixed" ] || refuse "the fixed file is not installed: $fixed"
    if grep -q '«INSTALL' "$fixed"; then
        refuse "the fixed file still carries its «INSTALL token (his approval row is not filled): $fixed"
    fi
    committed "the fixed file" "$fixed"
    n=$(grep -c '^claude --bg ' "$fixed")
    [ "$n" -eq 1 ] || refuse "the fixed file must hold exactly one launch line; found $n in $fixed"
    line=$(grep '^claude --bg ' "$fixed" | sed -e "s|<handover>|$handover|g")
    case "$line" in
        *"--remote-control brain --name brain"*) ;;
        *) refuse "the brain line does not name the seat brain (--remote-control brain --name brain)" ;;
    esac
    case "$line" in
        *bypassPermissions*) refuse "the brain line carries bypassPermissions (L55)" ;;
    esac
    # exactly one Opus word on the hub's line; `--fable` replaces that word and nothing else
    opus=" --model claude-opus-5-5 "
    after=${line#*"$opus"}
    # the blank the first word ends on may open a second: look again from that blank
    case " $after" in
        " $line"|*"$opus"*) refuse "the brain line does not default to --model claude-opus-5-5" ;;
    esac
    [ "$#" -eq 2 ] || line="${line%%"$opus"*} --model claude-fable-5-1 $after"
    case "$line" in
        *"<"*|*">"*) refuse "the launch line still holds an unfilled token" ;;
    esac
    check_paths "$line"
    # never beside a live brain (his 2026-09-30 R76: a brain is stopped only on his word); the
    # session list is desk-list.sh beside this script, rows "id · name · cwd · status · state"
    list="$(dirname "$0")/desk-list.sh"
    rows=$(sh "$list" 2>/dev/null) || refuse "the session list is unreadable ($list); a brain never launches beside a brain it cannot rule out"
    live=$(printf '%s\n' "$rows" | while IFS= read -r row; do
        rest=${row#* · }
        if [ "$rest" != "$row" ] && [ "${rest%% · *}" = "brain" ]; then
            printf '%s ' "${row%% · *}"
        fi
    done)
    [ -z "$live" ] || refuse "a session named brain is live (${live% }): a brain is stopped only on his word (2026-09-30 R76); launch its successor after he has stopped it"
    run_launch "$REPO" "$line" "reminder: the tab and the §5 row are the desk's; the brain is stopped only on his word (R76)"
fi

# ---- kind install-ops: link the ops scripts into the link folder; launches nothing (card 16) --
# A plain regular file at the name is replaced by the link in one rename (card 2026-10-08 106
# G3): `ln -s` to a dot-name, then `mv` over the name, so the name never goes missing. Any other
# existing name, a link (even a dangling one) or a directory, is KEPT untouched.
if [ "$kind" = "install-ops" ]; then
    [ "$#" -eq 1 ] || refuse "usage: desk-launch.sh install-ops"
    links=${COBALT_OPS_LINK_DIR:-/Users/cobalt/.claude/ops}
    [ -d "$links" ] || refuse "install-ops: no link folder $links"
    linked=0
    replaced=0
    kept=0
    for src in "$REPO"/ops/desk/*.sh "$REPO"/ops/desk/*.py; do
        [ -f "$src" ] && [ ! -L "$src" ] || continue
        name=$(basename "$src")
        if [ -f "$links/$name" ] && [ ! -L "$links/$name" ]; then
            same=""
            ! cmp -s "$src" "$links/$name" || same=1
            { ln -s "$src" "$links/.$name.new" && mv "$links/.$name.new" "$links/$name"; } \
                || refuse "install-ops: the replace failed: $links/$name"
            [ -n "$same" ] || printf 'REPLACED: %s\n' "$name"
            replaced=$((replaced + 1))
        elif [ -e "$links/$name" ] || [ -L "$links/$name" ]; then
            printf 'KEPT %s\n' "$name"
            kept=$((kept + 1))
        else
            ln -s "$src" "$links/$name" || refuse "install-ops: the link failed: $links/$name"
            printf 'LINKED %s\n' "$name"
            linked=$((linked + 1))
        fi
    done
    printf 'install-ops: %s linked, %s replaced, %s kept\n' "$linked" "$replaced" "$kept"
    exit 0
fi

[ "$#" -ge 2 ] && [ "$#" -le 4 ] || refuse "usage: desk-launch.sh <build|check|deploy|devfix|recut> <absolute card path> [PASS-2] [<resume step>]"
card=$2
step=""
pass2=""
for a in "${3:-}" "${4:-}"; do
    case "$a" in
        "") ;;
        PASS-2) pass2=1 ;;
        *) [ -z "$step" ] || refuse "two resume steps: '$step' and '$a'"
           step=$a ;;
    esac
done
[ -z "$pass2" ] || [ "$kind" = "check" ] || refuse "PASS-2 is an option of kind check only"

# ---- the kind is a fixed file -------------------------------------------------------------
case "$kind" in
    build)  fixed="$PROMPTS/BUILD-HUB.md" ;;
    check)  fixed="$PROMPTS/CHECK-HUB.md" ;;
    deploy|recut) fixed="$PROMPTS/DEPLOY-HUB.md" ;;
    devfix) fixed="$PROMPTS/DEVFIX-HUB.md" ;;
    *) refuse "kind '$kind' is none of build, check, deploy, devfix, recut, desk, prompt, brain, close, install-ops" ;;
esac
[ -f "$fixed" ] || refuse "the fixed file is not installed: $fixed"
if grep -q '«INSTALL' "$fixed"; then
    refuse "the fixed file still carries its «INSTALL token (his approval row is not filled): $fixed"
fi
# the line this script will eval comes from that file: it must be the committed one
[ -n "$(git -C "$REPO" log -1 --format=%H -- "$fixed")" ] || refuse "the fixed file is not committed on main: $fixed"
git -C "$REPO" diff --quiet -- "$fixed" || refuse "the fixed file differs from its commit: $fixed"
git -C "$REPO" diff --cached --quiet -- "$fixed" || refuse "the fixed file is staged, not committed: $fixed"

# ---- the card: where it lives, what its path may contain ------------------------------------
case "$card" in
    "$PROMPTS"/*-card.md) ;;
    *) refuse "the card must be $PROMPTS/<date>/<nn>-<job>-card.md" ;;
esac
case "$card" in
    *[!A-Za-z0-9\ ._/-]*) refuse "the card path holds a character outside [A-Za-z0-9 ._/-]" ;;
    *..*) refuse "the card path holds '..'" ;;
esac
[ -f "$card" ] || refuse "no such card: $card"
if grep -n '«FILL' "$card" >&2; then
    refuse "incomplete card: the «FILL tokens listed above still stand"
fi

# field KEY -> the value of the first "KEY: value" line, trailing blanks cut
field() {
    sed -n "s/^$1: *//p" "$card" | sed -n '1p' | sed 's/[[:space:]]*$//'
}
need() {
    for k in "$@"; do
        [ -n "$(field "$k")" ] || refuse "incomplete card: '$k' is empty"
    done
}
section() {
    grep -q "^## $1" "$card" || refuse "incomplete card: no '## $1' section"
}
hex8() {
    case "$2" in
        *[!0-9a-f]*) refuse "incomplete card: $1 '$2' is not 8 hex characters" ;;
    esac
    [ "${#2}" -eq 8 ] || refuse "incomplete card: $1 '$2' is not 8 hex characters"
}
commit_exists() {
    git -C "$REPO" rev-parse --verify --quiet "$2^{commit}" >/dev/null || refuse "$1 '$2' is not a commit in $REPO"
}

need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS
job=$(field JOB)
branch=$(field BRANCH)
wt=$(field WORKTREE)
base=$(field BASE)
tip=$(field TIP)
report=$(field REPORT)
tag=$(field TAG)
rulings=$(field RULINGS)

case "$job" in
    *[!a-z0-9-]*|-*) refuse "incomplete card: JOB '$job' must be [a-z0-9-]" ;;
esac
case "$branch" in
    *[!A-Za-z0-9._/-]*|-*|*..*) refuse "incomplete card: BRANCH '$branch' is not a plain branch name" ;;
esac
case "$rulings" in
    20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]\ R[0-9]*) ;;
    none) [ "$kind" = "deploy" ] || [ "$kind" = "recut" ] || refuse "incomplete card: RULINGS is 'none' only on a deploy card" ;;
    *) refuse "incomplete card: RULINGS must start '<date> R<n>' (a deploy card with nothing carried: 'none')" ;;
esac
# the tree-state owner (build, check): optional (card 2026-10-03/03c M4); a card that carries the
# key still says 'unchanged' or 'row <id>'
tree_state() {
    grep -q '^TREE STATE:' "$card" || return 0
    case "$(field "TREE STATE")" in
        unchanged|row\ ?*) ;;
        *) refuse "incomplete card: TREE STATE must be 'unchanged' or 'row <id>'" ;;
    esac
}

# ---- the worktree sits in the approved pattern ---------------------------------------------
case "$wt" in
    .*|*[!A-Za-z0-9._-]*) refuse "worktree '$wt' is outside the approved pattern $WT/<one directory name>" ;;
esac
[ "$wt" != "agy-trial" ] || refuse "worktree 'agy-trial' is the check hubs' scratch tree, never a job's"

# ---- the card is committed on main, unchanged since ----------------------------------------
[ -n "$(git -C "$REPO" log -1 --format=%H -- "$card")" ] || refuse "the card is not committed on main: $card"
git -C "$REPO" diff --quiet -- "$card" || refuse "the card differs from its commit: $card"
git -C "$REPO" diff --cached --quiet -- "$card" || refuse "the card is staged, not committed: $card"

# ---- the ruling rows (card 21 L1): build, check, deploy, devfix ------------------------------
# (ruling_row and ruling_items sit above the kinds: the prompt kind reads them too, card 21 F5)
ruling_rows() {
    [ "$rulings" = "none" ] || ruling_items "$rulings"
    for k in "HOUSE A" "HOUSE B"; do
        v=$(field "$k")
        case "$v" in
            *overruled*) ;;
            *) continue ;;
        esac
        over=$(printf '%s\n' "$v" | sed -n 's/.*overruled \(20[0-9-]* R[0-9]*\).*/\1/p')
        [ -n "$over" ] || refuse "incomplete card: $k '$v' names no '<date> R<n>' after 'overruled'"
        ruling_row "$over"
    done
}
ruling_rows

# ---- per kind: the rest of the card, the tree, the lock -------------------------------------
# with a resume step the job's OWN worktree's .env is skipped (its RECOVERY clears it first, scratch
# D1); a .env in any other worktree is still refused
lock_free() {
    own=""
    [ -z "$step" ] || own="$WT/$wt/.env"
    for f in "$WT"/*/.env; do
        [ "$f" != "$own" ] || continue
        [ ! -e "$f" ] || refuse "with-DB launch refused: the cobalt_dev lock is held ($f) (L76)"
    done
}
# the lock directory take-devdb-lock.sh makes (deploy only); a STEP-D0 resume skips its own gate's
lock_dir_free() {
    [ -e "$WT/.cobalt_dev.lock" ] || return 0
    holder=$(cat "$WT/.cobalt_dev.lock/owner" 2>/dev/null)
    if [ -n "$step" ] && [ "$holder" = "$wt" ]; then
        return 0
    fi
    refuse "with-DB launch refused: the cobalt_dev lock is held by ${holder:-unknown} ($WT/.cobalt_dev.lock) (L76)"
}

# every check committed and clean (card 21 L3; DEPLOY-HUB.md STEP-0 P2 and P3), for each row of
# `## SHIPS`: | # | branch | code tip | branch head | check report | its stop line must carry |
ships_checked() {
    rows=$(awk '/^## /{insec = ($0 ~ /^## SHIPS/)} insec && /^\| *[0-9]+ *\|/' "$card")
    # every head TIP merges is the branch head of a row: a head with no row is merged with no
    # check proven by anyone (2026-10-02 R41, the judge seat's answer to this build's DECISION 3)
    [ -n "$rows" ] || refuse "deploy: ## SHIPS has no row; TIP head ${tip%% *} is checked by no row — add its ## SHIPS row and commit its check report"
    for h in $tip; do
        printf '%s\n' "$rows" | awk -F'|' -v h="$h" '{gsub(/[` \t]/, "", $5); if ($5 == h) found = 1} END {exit !found}' \
            || refuse "deploy: TIP head $h is the branch head of no ## SHIPS row — add its ## SHIPS row and commit its check report"
    done
    while IFS= read -r srow; do
        [ -n "$srow" ] || continue
        sbranch=$(ship_cell "$srow" 3)
        ctip=$(ship_cell "$srow" 4)
        shead=$(ship_cell "$srow" 5)
        crep=$(ship_cell "$srow" 6)
        carry=$(printf '%s\n' "$srow" | awk -F'|' '{print $7}')
        frep=$(ship_cell "$srow" 8)
        case "$sbranch" in
            ""|*[!A-Za-z0-9._/-]*|-*|*..*) refuse "incomplete card: SHIPS branch '$sbranch' is not a plain branch name" ;;
        esac
        hex8 "SHIPS code tip" "$ctip"
        hex8 "SHIPS branch head" "$shead"
        # P3: the row's branch head is the same value TIP lists (check O1)
        case " $tip " in
            *" $shead "*) ;;
            *) refuse "deploy $sbranch: the branch head $shead is no head TIP lists — add it to TIP, or drop its ## SHIPS row" ;;
        esac
        case "$crep" in
            "$REPORTS"/*.md) ;;
            *) refuse "incomplete card: SHIPS check report '$crep' is not $REPORTS/<name>.md" ;;
        esac
        lits=$(printf '%s\n' "$carry" | grep -o '`[^`]*`' | tr -d '`')
        [ -n "$lits" ] || refuse "incomplete card: SHIPS row of $sbranch names no backticked literal its stop line must carry"
        # P2: the check report exists, is committed and unmodified, and its last line is clean
        [ -f "$crep" ] || refuse "deploy $sbranch: no check report — commit $crep"
        { [ -n "$(git -C "$REPO" log -1 --format=%H -- "$crep")" ] \
            && git -C "$REPO" diff --quiet -- "$crep" \
            && git -C "$REPO" diff --cached --quiet -- "$crep"; } \
            || refuse "deploy $sbranch: the check report is not committed or differs from its commit — commit $crep"
        clast=$(grep -v '^[[:space:]]*$' "$crep" | tail -n 1)
        while IFS= read -r lit; do
            case "$clast" in
                *"$lit"|*"$lit "*) ;;
                *) refuse "deploy $sbranch: its stop line lacks '$lit' — the check is not clean: $clast" ;;
            esac
        done <<LITS
$lits
LITS
        ltip=$(printf '%s\n' "$clast" | sed -n 's/.* tip: \([0-9a-f]*\).*/\1/p')
        # a small fix after the check (his R376, LAWS L75): the check's tip is an ancestor of the
        # code tip, and the row's `fix report`, read at the row's branch head (`git show`, card 63
        # N6: never a copy on main), ends `BUILT · … tip: <code tip>`
        fixed_ok() {
            [ -n "$frep" ] || return 1
            case "$frep" in
                "$REPORTS"/*.md) ;;
                *) return 1 ;;
            esac
            fblob=$(git -C "$REPO" show "$shead:${frep#"$REPO"/}" 2>/dev/null) || return 1
            git -C "$REPO" merge-base --is-ancestor "$ltip" "$ctip" 2>/dev/null || return 1
            flast=$(printf '%s\n' "$fblob" | grep -v '^[[:space:]]*$' | tail -n 1)
            case "$flast" in
                "BUILT ·"*"tip: $ctip"*) return 0 ;;
            esac
            return 1
        }
        [ -n "$ltip" ] && { [ "$ltip" = "$ctip" ] || [ "$ltip" = "$shead" ] || fixed_ok; } \
            || refuse "deploy $sbranch: the check's tip '$ltip' is neither the code tip $ctip nor the branch head $shead — the check is not clean: $clast"
        # P3: the branch head is the row's, the code tip its ancestor, and the head adds docs only
        bhead=$(git -C "$REPO" rev-parse --short=8 "$sbranch" 2>&1)
        [ "$bhead" = "$shead" ] \
            || refuse "deploy $sbranch: the branch head is $bhead, the row says $shead — the head moved: $bhead"
        git -C "$REPO" merge-base --is-ancestor "$ctip" "$shead" 2>/dev/null \
            || refuse "deploy $sbranch: the code tip $ctip is not an ancestor of $shead — the head moved: $shead"
        moved=$(git -C "$REPO" diff --stat "$ctip" "$shead" -- . ':(exclude)docs' 2>&1)
        [ -z "$moved" ] \
            || refuse "deploy $sbranch: the head adds more than docs past $ctip — the head moved: $(printf '%s' "$moved" | tr '\n' ' ')"
    done <<ROWS
$rows
ROWS
}
# ship_cell <row> <n>: the n-th '|' field of a SHIPS row, blanks and backticks cut
ship_cell() {
    printf '%s\n' "$1" | awk -F'|' -v i="$2" '{print $i}' | tr -d '`' | sed 's/^[[:space:]]*//; s/[[:space:]]*$//'
}

merges=""
prod=""
table=""
proof=""
case "$kind" in
build)
    [ -z "$tag" ] || refuse "this is a deploy card (TAG is set); kind 'build' needs a job card"
    section ROWS
    tree_state
    hex8 BASE "$base"
    commit_exists BASE "$base"
    case "$report" in
        "$WT/$wt/docs/40 - DevDocs/reports/"*.md) ;;
        *) refuse "incomplete card: REPORT must be $WT/$wt/docs/40 - DevDocs/reports/<name>.md" ;;
    esac
    if [ -d "$WT/$wt" ]; then
        head=$(git -C "$WT/$wt" rev-parse --abbrev-ref HEAD) || refuse "$WT/$wt is not a git worktree"
        [ "$head" = "$branch" ] || refuse "$WT/$wt is on '$head', the card says '$branch'"
        [ -z "$(git -C "$WT/$wt" status --porcelain)" ] || refuse "$WT/$wt is not clean"
    else
        git -C "$REPO" show-ref --verify --quiet "refs/heads/$branch" && refuse "branch '$branch' exists but its worktree $WT/$wt does not"
    fi
    # a build launches while the lock is held (R20); a resume still refuses another worktree's .env
    [ -z "$step" ] || lock_free
    ;;
check)
    [ -z "$tag" ] || refuse "this is a deploy card (TAG is set); kind 'check' needs a job card"
    need TIP "CHECK REPORT" "HOUSE B"
    section ROWS
    tree_state
    case "$(field "HOUSE B")" in
        "as needed"|"mandatory — vault notes"*|"mandatory — sizing"*) ;;
        *) refuse "incomplete card: HOUSE B must be 'as needed', 'mandatory — vault notes' or 'mandatory — sizing'" ;;
    esac
    hex8 BASE "$base"
    hex8 TIP "$tip"
    commit_exists BASE "$base"
    commit_exists TIP "$tip"
    git -C "$REPO" merge-base --is-ancestor "$base" "$tip" || refuse "BASE '$base' is not an ancestor of TIP '$tip'"
    creport=$(field "CHECK REPORT")
    case "$creport" in
        "$REPORTS"/*.md) ;;
        *) refuse "incomplete card: CHECK REPORT must be $REPORTS/<name>.md" ;;
    esac
    if [ -n "$pass2" ] && [ -z "$step" ]; then
        # the second pass: only on pass 1's own stop line, and only when it asks for house B
        [ -f "$creport" ] || refuse "PASS-2 needs pass 1's report: $creport"
        last=$(grep -v '^[[:space:]]*$' "$creport" | tail -n 1)
        case "$last" in
            "CHECK DONE"*"pass: 1"*"house B: needed"*) ;;
            *) refuse "PASS-2 launches only on a pass-1 stop line that says 'house B: needed'; the report ends: $last" ;;
        esac
    elif [ -z "$pass2" ] && [ -z "$step" ]; then
        [ ! -e "$creport" ] || refuse "the check report already exists: a second pass is PASS-2, a new worker names its CONTINUE step"
    fi
    # the build is built (card 21 L2): the build report's last non-blank line starts
    # `BUILT · job: <JOB> · tip: <TIP>`; a PASS-2 launch keeps the test it has (above)
    if [ -z "$pass2" ]; then
        [ -f "$report" ] || refuse "not built — no build report: $report"
        last=$(grep -v '^[[:space:]]*$' "$report" | tail -n 1)
        case "$last" in
            "BUILT · job: $job · tip: $tip"|"BUILT · job: $job · tip: $tip "*) ;;
            *) refuse "not built — $last" ;;
        esac
    fi
    [ -d "$WT/$wt" ] || refuse "the build's worktree $WT/$wt does not exist"
    [ -n "$step" ] || [ ! -e "$WT/$wt/.env" ] || refuse "$WT/$wt/.env exists: the build did not release the lock (L76)"
    [ -f "$report" ] || refuse "the build report does not exist: $report"
    head=$(git -C "$WT/$wt" rev-parse --abbrev-ref HEAD) || refuse "$WT/$wt is not a git worktree"
    [ "$head" = "$branch" ] || refuse "$WT/$wt is on '$head', the card says '$branch'"
    [ -z "$(git -C "$WT/$wt" status --porcelain)" ] || refuse "$WT/$wt is not clean (the check session commits there)"
    # a first pass-1 launch: the branch head is TIP or adds docs only past it (CHECK-HUB.md
    # PREFLIGHT; check O2). A resume or a PASS-2 sits on the check's own commits and is not re-read
    if [ -z "$pass2" ] && [ -z "$step" ]; then
        git -C "$WT/$wt" merge-base --is-ancestor "$tip" HEAD \
            || refuse "the tip is not the code tip — TIP $tip is not an ancestor of the branch head; set TIP to the branch's code tip"
        past=$(git -C "$WT/$wt" log --format= --name-only "$tip..HEAD" -- . ':(exclude)docs' | sed '/^$/d' | sort -u | tr '\n' ' ')
        [ -z "$past" ] || refuse "the tip is not the code tip — the branch adds ${past}past TIP $tip; set TIP to the branch's code tip"
    fi
    # a check launches while the lock is held (R20); a resume still refuses another worktree's .env
    [ -z "$step" ] || lock_free
    ;;
deploy)
    need TIP TAG MIGRATIONS SET
    section SHIPS
    section MARKERS
    section "SMOKE READS"
    [ "$base" = "main" ] || refuse "incomplete card: a deploy card's BASE is the literal 'main'"
    case "$report" in
        "$REPORTS"/deploy-*.md) ;;
        *) refuse "incomplete card: a deploy REPORT must be $REPORTS/deploy-<name>.md (the pre-commit guard lets only that path through)" ;;
    esac
    case "$tag" in
        *[!A-Za-z0-9._-]*) refuse "incomplete card: TAG '$tag' is not a plain tag name" ;;
    esac
    for h in $tip; do
        hex8 TIP "$h"
        commit_exists TIP "$h"
        merges="$merges \"Bash(git -C $WT/$wt merge --no-edit $h)\""
    done
    merges=${merges# }
    case "$(field MIGRATIONS)" in
        none) ;;
        none*) refuse "incomplete card: MIGRATIONS is 'none' alone, or the numbers" ;;
        *)
            section READ-BACK
            prod='"Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod --proof-only)" "Bash(COBALT_ENV=production uv run cobalt db migrate --allow-prod)" "Bash(COBALT_ENV=production uv run cobalt db query *)"'
            ;;
    esac
    if grep 'db query' "$card" | grep -q '%'; then
        refuse "a db query string in the card contains '%' (the tool refuses it; use strpos)"
    fi
    if [ -n "$step" ]; then
        [ "$step" = "STEP-D0" ] || refuse "a deploy resumes at STEP-D0 only, never '$step'"
        [ -d "$WT/$wt" ] || refuse "a resume needs the gate worktree $WT/$wt"
    else
        [ ! -e "$WT/$wt" ] || refuse "the gate worktree $WT/$wt already exists: a relaunch is 'desk-launch.sh deploy <card> STEP-D0'"
        [ ! -e "$report" ] || refuse "the deploy report already exists: $report"
        # not on a STEP-D0 resume: P2 and P3, before the gate worktree is added
        ships_checked
    fi
    lock_free
    lock_dir_free
    ;;
devfix)
    need TABLE "PROOF TEST"
    table=$(field TABLE)
    proof=$(field "PROOF TEST")
    table_bad=""
    case "$table" in
        system.*|user.*) ;;
        *) table_bad=1 ;;
    esac
    # the letters spelled out: under a UTF-8 locale a range a-z also matches capitals
    case "${table#*.}" in
        ""|*[!abcdefghijklmnopqrstuvwxyz0123456789_]*) table_bad=1 ;;
    esac
    [ -z "$table_bad" ] || refuse "incomplete card: TABLE '$table' is not system.<name> or user.<name> with <name> in [a-z0-9_]"
    proof_bad=""
    rest=${proof#tests/cobalt/}
    [ "$rest" != "$proof" ] || proof_bad=1
    pfile=${rest%%::*}
    case "$pfile" in
        *.py) ;;
        *) proof_bad=1 ;;
    esac
    case "${pfile%.py}" in
        ""|*[!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_]*) proof_bad=1 ;;
    esac
    if [ "$pfile" != "$rest" ]; then
        case "${rest#*::}" in
            ""|*[!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_:.]*) proof_bad=1 ;;
        esac
    fi
    [ -z "$proof_bad" ] || refuse "incomplete card: PROOF TEST '$proof' is not tests/cobalt/<file>.py with an optional ::<name> in [A-Za-z0-9_:.]"
    report_bad=""
    case "$report" in
        "$REPORTS"/devfix-*.md) ;;
        *) report_bad=1 ;;
    esac
    case "${report#"$REPORTS"/}" in
        */*|*[!ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-]*) report_bad=1 ;;
    esac
    [ -z "$report_bad" ] || refuse "incomplete card: a devfix REPORT must be $REPORTS/devfix-<name>.md"
    [ -n "$step" ] || [ ! -e "$report" ] || refuse "the devfix report already exists: $report (a new worker names its CONTINUE step)"
    hex8 BASE "$base"
    commit_exists BASE "$base"
    git -C "$REPO" merge-base --is-ancestor "$base" main || refuse "BASE '$base' is not a commit on main"
    if [ -d "$WT/$wt" ]; then
        head=$(git -C "$WT/$wt" rev-parse --abbrev-ref HEAD) || refuse "$WT/$wt is not a git worktree"
        [ "$head" = "$branch" ] || refuse "$WT/$wt is on '$head', the card says '$branch'"
    fi
    # the devfix holds the lock from its first step to its stop line: never launched beside a holder
    lock_free
    lock_dir_free
    ;;
recut)
    # RECUT (card 2026-10-03/03 adoption-scripts L5): a deploy whose gate FAILED, in ONE call
    need TAG
    [ "$base" = "main" ] || refuse "recut: '$card' is no deploy card (its BASE is not the literal 'main')"
    case "$report" in
        "$REPORTS"/deploy-*.md) ;;
        *) refuse "recut: REPORT is not $REPORTS/deploy-<name>.md: $report" ;;
    esac
    case "$tag" in
        *[!A-Za-z0-9._-]*) refuse "incomplete card: TAG '$tag' is not a plain tag name" ;;
    esac
    [ -f "$report" ] || refuse "recut: no deploy report: $report"
    last=$(grep -v '^[[:space:]]*$' "$report" | tail -n 1)
    case "$last" in
        FAILED*) ;;
        *) refuse "recut: the deploy report does not end FAILED: $last" ;;
    esac
    case "$last" in
        *"rollback: used"*) refuse "recut: the failed deploy names 'rollback: used' — its STEP-5 ran; a recut is not the desk's: $last" ;;
        *"|"*) refuse "recut: the failed line holds a table bar, which desk-row.sh refuses: $last" ;;
    esac
    # the attempt: the highest -attempt<k> on the card's four values, a branch, a tag, a worktree
    # or a report of the same base names, + 1 (the first gate is attempt 1); never a name in use
    strip() { printf '%s\n' "$1" | sed 's/-attempt[0-9][0-9]*$//'; }
    attempt_of() { printf '%s\n' "$1" | sed -n 's/.*-attempt\([0-9][0-9]*\)$/\1/p'; }
    bb=$(strip "$branch")
    bw=$(strip "$wt")
    bt=$(strip "$tag")
    br=$(strip "${report%.md}")
    n=1
    seen() {
        k=$(attempt_of "$1")
        [ -z "$k" ] || [ "$k" -le "$n" ] || n=$k
    }
    for v in "$branch" "$wt" "$tag" "${report%.md}"; do
        seen "$v"
    done
    for v in $(git -C "$REPO" for-each-ref --format='%(refname:short)' "refs/heads/$bb-attempt*" "refs/tags/$bt-attempt*"); do
        seen "$v"
    done
    for v in "$WT/$bw"-attempt* "$br"-attempt*.md; do
        [ -e "$v" ] && seen "${v%.md}"
    done
    n=$((n + 1))
    nb="$bb-attempt$n"
    nw="$bw-attempt$n"
    nt="$bt-attempt$n"
    nr="$br-attempt$n.md"
    ! git -C "$REPO" show-ref --verify --quiet "refs/heads/$nb" || refuse "recut: branch $nb exists"
    ! git -C "$REPO" show-ref --verify --quiet "refs/tags/$nt" || refuse "recut: tag $nt exists"
    [ ! -e "$WT/$nw" ] || refuse "recut: $WT/$nw exists"
    [ ! -e "$nr" ] || refuse "recut: $nr exists"
    # card 63 N7: a failed line too long for desk-row.sh's 300 keeps its head through the first
    # ` — ` and its tail from the last ` · rollback:`, the middle cut to fit and marked `…`; a line
    # that fits, lacks either mark, or cannot fit even so is left as it is (refused below)
    last=$(python3 -c '
import sys
pre, last = sys.argv[1:3]
def size(t): return len("| R0000 | 00:00 ET | %s | RECORD |" % (pre + t))
i, j = last.find(" — "), last.rfind(" · rollback:")
if size(last) > 300 and i >= 0 and j >= i + 3:
    head, mid, tail = last[:i + 3], last[i + 3:j], last[j:]
    room = 300 - size(head + "…" + tail)
    if room >= 0:
        last = head + mid[:room] + "…" + tail
print(last)' "RECUT $job attempt $n — " "$last") && [ -n "$last" ] \
        || refuse "recut: the failed line could not be fitted to desk-row.sh's 300 (python3)"
    text="RECUT $job attempt $n — $last"
    rlen=$(python3 -c 'import sys; print(len("| R0000 | 00:00 ET | %s | RECORD |" % sys.argv[1]))' "$text")
    [ "$rlen" -le 300 ] || refuse "recut: the desk row would be $rlen characters, over desk-row.sh's 300: $text"
    # 1. the failed gate, by gate-clean.sh (it refuses when anything of the gate landed)
    printf 'RUN: sh %s/gate-clean.sh "%s"\n' "$here" "$card"
    sh "$here/gate-clean.sh" "$card" || exit 1
    # 2. the card's four values
    sed -e "s|^BRANCH: .*|BRANCH: $nb|" -e "s|^WORKTREE: .*|WORKTREE: $nw|" \
        -e "s|^TAG: .*|TAG: $nt|" -e "s|^REPORT: .*|REPORT: $nr|" "$card" > "$card.recut" \
        && mv "$card.recut" "$card" || refuse "recut: the card edit failed; the gate is cleaned: $card"
    printf 'RECUT: %s attempt %s\n' "$job" "$n"
    printf 'BRANCH: %s -> %s\n' "$branch" "$nb"
    printf 'WORKTREE: %s -> %s\n' "$wt" "$nw"
    printf 'TAG: %s -> %s\n' "$tag" "$nt"
    printf 'REPORT: %s -> %s\n' "$report" "$nr"
    # 3. the commit, 4. the desk row
    sh "$here/desk-commit.sh" "docs(desk): RECUT $job attempt $n" "$card" \
        || refuse "recut: desk-commit.sh failed; the gate is cleaned, the card edited and not committed: $card"
    sh "$here/desk-row.sh" RECORD "$text" || refuse "recut: desk-row.sh failed; the card is committed: $card"
    # 5. the deploy kind's launch on the recut card (DESK_LAUNCH_DRY=1 makes it dry)
    exec sh "$0" deploy "$card"
    ;;
esac

# ---- the launch line: copied from the fixed file, tokens filled from the card ---------------
n=$(grep -c '^claude --bg ' "$fixed")
[ "$n" -eq 1 ] || refuse "the fixed file must hold exactly one launch line; found $n in $fixed"
line=$(grep '^claude --bg ' "$fixed" | sed \
    -e "s|<card>|$card|g" \
    -e "s|<job>|$job|g" \
    -e "s|<tag>|$tag|g" \
    -e "s|<worktree>|$wt|g" \
    -e "s|<branch>|$branch|g" \
    -e "s|<table>|$table|g" \
    -e "s|<proof test>|$proof|g" \
    -e "s|<tip merges>|$merges|" \
    -e "s|<prod migrate strings>|$prod|")
if [ -n "$step" ]; then
    case "$step" in
        *[!A-Za-z0-9.\ -]*) refuse "resume step '$step' holds a character outside [A-Za-z0-9 .-]" ;;
    esac
    line=$(printf '%s\n' "$line" | sed "s|^claude --bg \"Read |claude --bg \"CONTINUE: $step. Read |")
fi
if [ -n "$pass2" ]; then
    # the message then starts `PASS-2. ` (before any `CONTINUE: <step>. `): CHECK-HUB.md `## PASS 2`
    line=$(printf '%s\n' "$line" | sed "s|^claude --bg \"|claude --bg \"PASS-2. |")
fi
case "$line" in
    *"<"*|*">"*) refuse "the launch line still holds an unfilled token" ;;
esac

check_paths "$line"

# ---- run the launch: the worktree add (when one is needed), the cd, the line -----------------
add=""
case "$kind" in
build)
    [ -d "$WT/$wt" ] || add="git -C $REPO worktree add -b $branch $WT/$wt $base"
    dir="$WT/$wt"
    note="reminder: the build takes the cobalt_dev lock only at its with-DB steps and waits for it there (L76, R20); no deploy launch while it holds it"
    ;;
check)
    dir="$WT/$wt"
    note="reminder: one Grok hub at a time (L15); no other house hub running; the check takes the cobalt_dev lock only at its with-DB steps and waits for it there (L76, R20); measure the session at its stop line (desk-context.sh)"
    ;;
deploy)
    [ -n "$step" ] || add="git -C $REPO worktree add -b $branch $WT/$wt main"
    dir="$REPO"
    note="reminder: no desk commit on main until the stop line; builds and checks may launch, their with-DB steps wait for the lock the gate holds to its stop line (L76, R20); a hub hung after its first bootout: stop it and at once run this script again with STEP-D0"
    ;;
devfix)
    [ -d "$WT/$wt" ] || add="git -C $REPO worktree add -b $branch $WT/$wt $base"
    dir="$WT/$wt"
    note="reminder: the devfix holds the cobalt_dev lock from its first step to its stop line (L76); no deploy launch until then; watch: wait-stop-line.sh <its REPORT> '^(REBUILT|FAILED)'; the report is the desk's to commit"
    ;;
esac

watch=$(watch_line "$kind" "$card")
if [ "${DESK_LAUNCH_DRY:-0}" = "1" ]; then
    [ -z "$add" ] || printf '%s\n' "$add"
    run_launch "$dir" "$line" "$note" "$watch"
fi

if [ -n "$add" ]; then
    printf 'RUN: %s\n' "$add" >&2
    if [ "$kind" = "build" ] || [ "$kind" = "devfix" ]; then
        git -C "$REPO" worktree add -b "$branch" "$WT/$wt" "$base" || refuse "worktree add failed; nothing launched"
    else
        git -C "$REPO" worktree add -b "$branch" "$WT/$wt" main || refuse "worktree add failed; nothing launched"
    fi
fi
run_launch "$dir" "$line" "$note" "$watch"
