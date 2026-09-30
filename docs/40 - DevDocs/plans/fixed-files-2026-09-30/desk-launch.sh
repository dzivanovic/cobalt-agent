#!/bin/sh
# DRAFT — NOT INSTALLED — TESTED IN PART: the third-pass copy ran in the 09-30 scratch test (item 1:
# every kind and every refusal run passed; defects D1, D2). The fourth-pass changes — the `close`
# kind, the write-path-mode refusal, the own-`.env` resume (D1), the spaced-path refusal — are NOT
# TESTED.
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
#   sh /Users/cobalt/.claude/ops/desk-launch.sh build|check "<card>" [PASS-2] <step>   (a NEW worker at
#        that CONTINUE step — only when the launch line must change, the session died, the
#        judgment seat finds a misread, or the worker measures above 250,000 tokens)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh desk                                   (its successor)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh prompt "<absolute prompt path>"        (a one-off prompt)
#   sh /Users/cobalt/.claude/ops/desk-launch.sh close <YYYY-MM-DD> [<step>]            (the nightly close
#        of that day: after the 21:00 ET pause on the day itself, or any time later for a missed
#        night — the morning desk's first act; <step> = a NEW worker at that CONTINUE step)
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
#   desk  : `cd /Users/cobalt/cobalt`; the wake-up's own launch line — the ONE backticked
#           `claude --bg …` span on the `- LAUNCH` line of prompts/CTO-DESK-WAKEUP.md.
#   prompt: `cd <the cwd the prompt names>`; the prompt's own launch line — the ONE
#           `claude --bg "Read '<that prompt file>' and follow it exactly." …` it holds (a line
#           of its own, or a backticked span), for a drafter, a tribunal and its seats, a brain
#           tab. READ-ONLY LINES ONLY: every write-path launch is a fixed file.
#   close : `cd /Users/cobalt/cobalt`; CLOSE-HUB.md's `claude --bg` line, `<date>` and `<mmdd>`
#           filled (a resume: its message starting `CONTINUE: <step>. `).
# It prints each command on stderr as `RUN: <command>` before it runs it, and exits with the
# status of the last one. DESK_LAUNCH_DRY=1 in the environment prints the three commands on
# stdout and runs nothing (for the scratch test; the desk's line has no string for it).
#
# IT REFUSES (exit 1, "REFUSED: <reason>" on stderr, nothing run):
#   - to run at all from a path that holds a space (install under /Users/cobalt/.claude/ops/);
#   - a kind that is none of build, check, deploy, desk, prompt, close; a fixed file, a wake-up
#     file or a prompt file still a draft, not committed on main, or changed since its commit;
#   - kind `close`: a date not YYYY-MM-DD, a date after today (ET), today's date before 21:00 ET,
#     a first launch whose close report already exists, a resume without it, or ANY live
#     `deploy-hub-` session (read from `claude agents --json`; unreadable = refused);
#   - kind `prompt`: a line whose permission mode is a write-path mode — `acceptEdits` or
#     `dontAsk` (the fixed files' mode) — or `bypassPermissions`, or not stated; the close file
#     handed over as a prompt; a line that carries a write string — `git add`, `git commit`, `git merge` (also
#     in their `git -C <path>` spelling, and the whole-git `Bash(git *)`), `uv run`,
#     `launchctl`, `COBALT_ENV=`; a line without the two dialog denies (L63), without
#     `--remote-control` and `--name`, or that reads another file than the one named; a card
#     or a fixed file handed over as a prompt; a prompt that names no cwd;
#   - kind `desk`: a wake-up line that does not name `cto-desk`;
#   - PASS-2 on anything but a check whose report's last line is pass 1's `CHECK DONE` with
#     `house B: needed`; a first check launch whose report already exists;
#   - an incomplete card: a header key its kind needs is empty, a «FILL token stands
#     anywhere, a body section its kind needs is missing, the card is not committed on main
#     or differs from its commit (this is the whole of the card gate: no launch row is read);
#   - a worktree outside the approved pattern /Users/cobalt/cobalt-wt/<one directory name>;
#   - a with-DB launch (build, check, deploy) while any /Users/cobalt/cobalt-wt/*/.env exists
#     (L76; the check session takes the lock). ONE EXCEPTION (scratch D1): a launch that names a
#     resume step (a NEW worker at a CONTINUE step; a deploy's STEP-D0) skips the job's OWN
#     worktree's .env — the fixed file's RECOVERY clears it first — and still refuses any other;
#   - a launch line in which an absolute path sits under no --add-dir (the 09-30 outage);
#   - a production db query string in a deploy card that contains "%".
#
# THE LAUNCH LINE HAS ONE HOME: the fixed file's single line beginning "claude --bg " (the
# wake-up's LAUNCH line for `desk`; the prompt's own line for `prompt`). This script copies
# that line, fills its tokens from the card and runs it with `eval`; every value it fills is
# checked against a closed character set first. It holds no allow string of its own except
# the two patterns the deploy line's tokens expand to (DEPLOY-HUB.md).

set -u

REPO=/Users/cobalt/cobalt
WT=/Users/cobalt/cobalt-wt
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

# run_launch <dir> <line> <note>: the cd and the line; DESK_LAUNCH_DRY=1 prints both, runs nothing
run_launch() {
    if [ "${DESK_LAUNCH_DRY:-0}" = "1" ]; then
        printf '%s\n' "cd $1"
        printf '%s\n' "$2"
        exit 0
    fi
    [ -d "$1" ] || refuse "no such directory: $1"
    printf 'RUN: cd %s\n' "$1" >&2
    cd "$1" || refuse "cd failed: $1"
    printf 'RUN: %s\n' "$2" >&2
    eval "$2"
    status=$?
    printf '%s\n' "$3" >&2
    exit "$status"
}

[ "$#" -ge 1 ] || refuse "usage: desk-launch.sh <build|check|deploy> <card> [PASS-2] [<resume step>] | desk | prompt <prompt file> | close <YYYY-MM-DD> [<resume step>]"
kind=$1

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
    run_launch "$REPO" "$line" "reminder: no desk commit on main and no deploy launch until the close's stop line; the close pushes main itself (L55 as amended)"
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
    for w in "git add" "git commit" "git merge" "Bash(git *)" "uv run" "launchctl" "COBALT_ENV="; do
        case "$line" in
            *"$w"*) refuse "write string '$w' on a prompt line: a write-path launch is a fixed file" ;;
        esac
    done
    case "$line" in
        *"Bash(git -C "*" add "*|*"Bash(git -C "*" commit "*|*"Bash(git -C "*" merge "*) refuse "a git -C write string on a prompt line: a write-path launch is a fixed file" ;;
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
    check_paths "$line"
    run_launch "$dir" "$line" "reminder: one Grok hub at a time (L15); the tab and the §5 row are the desk's"
fi

[ "$#" -ge 2 ] && [ "$#" -le 4 ] || refuse "usage: desk-launch.sh <build|check|deploy> <absolute card path> [PASS-2] [<resume step>]"
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
    deploy) fixed="$PROMPTS/DEPLOY-HUB.md" ;;
    *) refuse "kind '$kind' is none of build, check, deploy, desk, prompt, close" ;;
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
    none) [ "$kind" = "deploy" ] || refuse "incomplete card: RULINGS is 'none' only on a deploy card" ;;
    *) refuse "incomplete card: RULINGS must start '<date> R<n>' (a deploy card with nothing carried: 'none')" ;;
esac
# the tree-state owner (build, check): 'unchanged' or 'row <id>'
tree_state() {
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

merges=""
prod=""
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
    lock_free
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
    [ -d "$WT/$wt" ] || refuse "the build's worktree $WT/$wt does not exist"
    [ -n "$step" ] || [ ! -e "$WT/$wt/.env" ] || refuse "$WT/$wt/.env exists: the build did not release the lock (L76)"
    [ -f "$report" ] || refuse "the build report does not exist: $report"
    head=$(git -C "$WT/$wt" rev-parse --abbrev-ref HEAD) || refuse "$WT/$wt is not a git worktree"
    [ "$head" = "$branch" ] || refuse "$WT/$wt is on '$head', the card says '$branch'"
    [ -z "$(git -C "$WT/$wt" status --porcelain)" ] || refuse "$WT/$wt is not clean (the check session commits there)"
    lock_free
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
    fi
    lock_free
    ;;
esac

# ---- the launch line: copied from the fixed file, tokens filled from the card ---------------
n=$(grep -c '^claude --bg ' "$fixed")
[ "$n" -eq 1 ] || refuse "the fixed file must hold exactly one launch line; found $n in $fixed"
line=$(grep '^claude --bg ' "$fixed" | sed \
    -e "s|<card>|$card|g" \
    -e "s|<job>|$job|g" \
    -e "s|<worktree>|$wt|g" \
    -e "s|<branch>|$branch|g" \
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
    note="reminder: no other with-DB launch until this build's stop line (L76)"
    ;;
check)
    dir="$WT/$wt"
    note="reminder: one Grok hub at a time (L15); no other house hub running; no other with-DB launch until the stop line (the check takes the lock); measure the session at its stop line (desk-context.sh)"
    ;;
deploy)
    [ -n "$step" ] || add="git -C $REPO worktree add -b $branch $WT/$wt main"
    dir="$REPO"
    note="reminder: no desk commit on main and no with-DB launch until the stop line; a hub hung after its first bootout: stop it and at once run this script again with STEP-D0"
    ;;
esac

if [ "${DESK_LAUNCH_DRY:-0}" = "1" ]; then
    [ -z "$add" ] || printf '%s\n' "$add"
    run_launch "$dir" "$line" "$note"
fi

if [ -n "$add" ]; then
    printf 'RUN: %s\n' "$add" >&2
    if [ "$kind" = "build" ]; then
        git -C "$REPO" worktree add -b "$branch" "$WT/$wt" "$base" || refuse "worktree add failed; nothing launched"
    else
        git -C "$REPO" worktree add -b "$branch" "$WT/$wt" main || refuse "worktree add failed; nothing launched"
    fi
fi
run_launch "$dir" "$line" "$note"
