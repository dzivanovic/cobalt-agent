#!/bin/sh
# desk-context.sh <session-id-prefix> [threshold]
# Read-only. Prints the desk's CURRENT context size in tokens, read from the last recorded
# model usage in its own transcript (~/.claude/projects/*/<id>*.jsonl, every project folder):
# input + cache_read + cache_creation. Prints REFRESH when >= threshold (default 400000,
# ruled 2026-09-23 R98). Writes nothing.
#
# desk-context.sh --guard
# The desk-size guard (ruled cto-2026-10-01 R8), run first by desk-launch.sh (every kind but
# `desk`) and wait-stop-line.sh. It measures THE DESK the same way: the caller's own session
# when basename $CLAUDE_JOB_DIR is a live `cto-desk` row of desk-list.sh, otherwise the
# `cto-desk` row with the smallest measure (the successor during a handover). Below 300,000 it
# prints nothing and exits 0; at 300,000 or more it prints
# "REFUSED: desk at <n> tokens — REFRESH first" and exits 3. No `cto-desk` row, or a measure
# that fails: "WARNING: desk size unread — guard skipped" on stderr, exit 0 — the guard never
# blocks on its own failure (DECISION G-A). Writes nothing.
PROJECTS=/Users/cobalt/.claude/projects
DESK_LIST=/Users/cobalt/.claude/ops/desk-list.sh
GUARD_AT=300000

# measure <id>: prints the size in tokens; status 2 when the id has no transcript
measure() {
    case "$1" in
        ""|*[!0-9a-f-]*) return 2 ;;
    esac
    [ "${#1}" -ge 8 ] || return 2
    f=$(ls -t "$PROJECTS"/*/"$1"*.jsonl 2>/dev/null | head -1)
    [ -n "$f" ] || return 2
    tail -r "$f" | grep -m1 '"usage"' | python3 -c '
import json,sys
u=json.loads(sys.stdin.read())["message"]["usage"]
print(u.get("input_tokens",0)+u.get("cache_read_input_tokens",0)+u.get("cache_creation_input_tokens",0))'
}

if [ "${1:-}" = "--guard" ]; then
    unread() {
        echo "WARNING: desk size unread — guard skipped" >&2
        exit 0
    }
    # the live cto-desk ids, from LIST rows "id · name · cwd · status · state"
    desks=$(sh "$DESK_LIST" 2>/dev/null | while IFS= read -r row; do
        rest=${row#* · }
        if [ "$rest" != "$row" ] && [ "${rest%% · *}" = "cto-desk" ]; then
            printf '%s\n' "${row%% · *}"
        fi
    done)
    [ -n "$desks" ] || unread
    own=""
    [ -z "${CLAUDE_JOB_DIR:-}" ] || own=$(basename "$CLAUDE_JOB_DIR")
    pick=""
    for d in $desks; do
        [ "$d" != "$own" ] || pick=$d
    done
    n=""
    for d in ${pick:-$desks}; do
        c=$(measure "$d" 2>/dev/null) || unread
        case "$c" in
            ""|*[!0-9]*) unread ;;
        esac
        if [ -z "$n" ] || [ "$c" -lt "$n" ]; then
            n=$c
        fi
    done
    if [ "$n" -ge "$GUARD_AT" ]; then
        echo "REFUSED: desk at $n tokens — REFRESH first"
        exit 3
    fi
    exit 0
fi

id="$1"; thr="${2:-400000}"
c=$(measure "$id")
s=$?
[ "$s" -ne 2 ] || { echo "no transcript for $id"; exit 2; }
[ "$s" -eq 0 ] || exit "$s"
python3 -c '
import sys
c=int(sys.argv[1]); thr=int(sys.argv[2])
print(f"context {c} of {thr} — " + ("REFRESH" if c>=thr else "ok"))' "$c" "$thr"
