#!/bin/sh
# house-probe.sh [--card <card>] [grok] [gemini] [sol] — asks each named outside house for one word;
# when none is named, grok and gemini, and `sol grok gemini` when the card's header carries the line
# below; prints one line per house in that order (card 19 worker-steps S5; card 298 S3, his
# 2026-10-10 R920, R921):
#   <house>: UP                        the answer, trimmed, is `OK`
#   <house>: OUT — <first line>        anything else: the first non-blank line it printed
#                                      (stdout, else stderr, else `(no output)`)
#   <house>: OUT — TIMEOUT             no answer within the limit: 180 s each, the probes in parallel
# Exit 0 always. A bad call (an unknown or repeated house; `--card` with no path, a path that is not
# a readable file, or given twice; `sol` named without the line): `REFUSED: <reason>` on stderr, exit 1.
#
# THE LINE: in the card's header (the lines before the first line starting `## `), one whole line from
# column 0 `HOUSE A: OpenAI — his <date> R<n>`, nothing after; authorize.sh proves it like a ruling.
#
# THE SPELLINGS:
#   sol     only with the header line; CHECK-HUB.md PREFLIGHT's Sol probe, exactly:
#           codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "Reply with only the word OK." < /dev/null
#   grok    CHECK-HUB.md `## 1` (5)'s Grok launch with the probe prompt, run from $WT/agy-trial, the
#           model pinned (his 2026-10-03 R3: every Grok seat runs grok-4.7; card 2026-10-03/03 L7):
#           grok -m grok-4.7 --sandbox cobalt-job --allow "Write($WT/agy-trial/scratch/tribunal-bars-0920/**)" -p "Reply with only the word OK."
#   gemini  CHECK-HUB.md `## 1` (5)'s Gemini launch with the probe prompt and a 3-minute print
#           timeout, run from $WT/agy-trial:
#           agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m --add-dir $WT/agy-trial --print="Reply with only the word OK."
# A trailing `[exited with code <n>]` line is dropped before the answer is read.
#
# COBALT_WT_ROOT stands in for /Users/cobalt/cobalt-wt, and HOUSE_PROBE_LIMIT (whole seconds) for
# the 180-second limit, in tests/ops/test_house_probe.py only.

export LC_ALL=C
set -u
set -f

WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
LIMIT=${HOUSE_PROBE_LIMIT:-180}
PROMPT="Reply with only the word OK."

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

case "$LIMIT" in
    ""|*[!0-9]*) refuse "HOUSE_PROBE_LIMIT '$LIMIT' is not a whole number of seconds" ;;
esac
houses=""
card=""
carded=""
while [ "$#" -gt 0 ]; do
    h=$1
    shift
    if [ "$h" = "--card" ]; then
        [ -z "$carded" ] || refuse "--card given twice"
        [ "$#" -gt 0 ] && [ -n "$1" ] || refuse "--card needs a path"
        [ -f "$1" ] && [ -r "$1" ] || refuse "--card $1 is not a readable file"
        card=$1
        carded=1
        shift
        continue
    fi
    case "$h" in
        sol|grok|gemini) ;;
        *) refuse "house '$h' is none of sol, grok, gemini" ;;
    esac
    case " $houses " in
        *" $h "*) refuse "house '$h' named twice" ;;
    esac
    houses="$houses $h"
done

# the header line (above): Sol is probed only with it (his 2026-10-10 R920)
openai=""
if [ -n "$card" ] && sed -n '/^## /q;p' "$card" \
    | grep -q -x -e 'HOUSE A: OpenAI — his 20[0-9][0-9]-[0-9][0-9]-[0-9][0-9] R[0-9][0-9]*'; then
    openai=1
fi
case " $houses " in
    *" sol "*)
        [ -n "$openai" ] || refuse "house 'sol' is probed only when the card header carries \"HOUSE A: OpenAI — his <date> R<n>\" (his 2026-10-10 R920)"
        ;;
esac
if [ -z "$houses" ]; then
    if [ -n "$openai" ]; then
        houses=" sol grok gemini"
    else
        houses=" grok gemini"
    fi
fi

tmp=$(mktemp -d "${TMPDIR:-/tmp}/house-probe.XXXXXX") || refuse "mktemp failed"
trap 'rm -rf "$tmp"' EXIT

start() {
    case "$1" in
        sol)
            codex exec --skip-git-repo-check -m gpt-5.6-sol -s read-only -c model_reasoning_effort="high" "$PROMPT" < /dev/null \
                > "$tmp/sol.out" 2> "$tmp/sol.err" &
            ;;
        grok)
            (cd "$WT/agy-trial" && exec grok -m grok-4.7 --sandbox cobalt-job --allow "Write($WT/agy-trial/scratch/tribunal-bars-0920/**)" -p "$PROMPT") \
                < /dev/null > "$tmp/grok.out" 2> "$tmp/grok.err" &
            ;;
        gemini)
            (cd "$WT/agy-trial" && exec agy --model gemini-3.1-pro-high --mode accept-edits --sandbox --print-timeout 3m --add-dir "$WT/agy-trial" --print="$PROMPT") \
                < /dev/null > "$tmp/gemini.out" 2> "$tmp/gemini.err" &
            ;;
    esac
    printf '%s\n' "$!" > "$tmp/$1.pid"
}

for h in $houses; do
    start "$h"
done

waited=0
while :; do
    running=""
    for h in $houses; do
        kill -0 "$(cat "$tmp/$h.pid")" 2>/dev/null && running=1
    done
    [ -n "$running" ] && [ "$waited" -lt "$LIMIT" ] || break
    sleep 1
    waited=$((waited + 1))
done

for h in $houses; do
    pid=$(cat "$tmp/$h.pid")
    if kill -0 "$pid" 2>/dev/null; then
        pkill -P "$pid" 2>/dev/null
        kill "$pid" 2>/dev/null
        wait "$pid" 2>/dev/null
        printf '%s: OUT — TIMEOUT\n' "$h"
        continue
    fi
    wait "$pid" 2>/dev/null
    answer=$(sed '/^\[exited with code [0-9]*\]$/d' "$tmp/$h.out" | sed -e 's/^[[:space:]]*//' -e 's/[[:space:]]*$//' | sed '/^$/d')
    if [ "$answer" = "OK" ]; then
        printf '%s: UP\n' "$h"
        continue
    fi
    said=$(sed '/^[[:space:]]*$/d' "$tmp/$h.out" | sed -n '1p')
    [ -n "$said" ] || said=$(sed '/^[[:space:]]*$/d' "$tmp/$h.err" | sed -n '1p')
    [ -n "$said" ] || said="(no output)"
    printf '%s: OUT — %s\n' "$h" "$said"
done
exit 0
