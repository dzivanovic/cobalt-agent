#!/bin/sh
# order-open.sh
# Read-only. Prints the facts the desk needs before an order's first launch (card 18
# desk-tools-b, row B3), one block each, each headed by its name on a line of its own:
#   LOCK       every $WT/*/.env, the lock directory $WT/.cobalt_dev.lock and its owner, or `free`
#   SESSIONS   the live rows of `claude agents --json` (a row with a pid): id name cwd status state
#   WINDOW     from the clock in America/New_York: `pause` 20:00–21:00 on a weekday; `overnight`
#              21:00–04:00 after a weekday; `weekend`; else `closed — a deploy needs his dated
#              order`. Holidays are not known to it, and it says so. ORDER_OPEN_NOW=<ISO time>
#              overrides the clock (a time without a zone is New York time).
#   MAIN       `git -C $REPO rev-list --count origin/main..main`, and whether main's tree has
#              uncommitted tracked changes
#   WORKTREES  each directory under $WT: its branch, `merged` or `unmerged` against main, the age
#              in days of its last commit
#   HOUSES     the output of house-probe.sh beside this script when that file exists, else `not probed`
# It changes nothing (git runs with GIT_OPTIONAL_LOCKS=0, so no index refresh is written) and
# always exits 0.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).

set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}
LOCK="$WT/.cobalt_dev.lock"
GIT_OPTIONAL_LOCKS=0
export GIT_OPTIONAL_LOCKS
here=$(dirname "$0")

echo "LOCK"
held=""
for f in "$WT"/*/.env; do
    if [ -e "$f" ] || [ -L "$f" ]; then
        echo ".env: $f"
        held=1
    fi
done
if [ -d "$LOCK" ]; then
    owner=$(sed -n '1p' "$LOCK/owner" 2>/dev/null)
    echo "lock directory: $LOCK owner ${owner:-unknown}"
    held=1
fi
[ -n "$held" ] || echo "free"

echo "SESSIONS"
claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
except Exception:
    print("unreadable (claude agents --json)")
    sys.exit(0)
live = [a for a in rows if isinstance(a, dict) and a.get("pid")]
for a in live:
    print(" ".join(str(a.get(k, "?")) for k in ("id", "name", "cwd", "status", "state")))
if not live:
    print("none live")
' 2>/dev/null || echo "unreadable (claude agents --json)"

echo "WINDOW"
python3 -c '
import datetime as dt, os, sys
from zoneinfo import ZoneInfo
ny = ZoneInfo("America/New_York")
raw = os.environ.get("ORDER_OPEN_NOW", "")
if raw:
    try:
        t = dt.datetime.fromisoformat(raw)
    except ValueError:
        print("window: unknown — ORDER_OPEN_NOW %r is not an ISO time" % raw)
        print("holidays are not known to this script")
        sys.exit(0)
    t = t.replace(tzinfo=ny) if t.tzinfo is None else t.astimezone(ny)
else:
    t = dt.datetime.now(ny)
wd, h = t.weekday(), t.hour
prev = (wd - 1) % 7
if wd < 5 and h == 20:
    w = "pause"
elif wd < 5 and h >= 21:
    w = "overnight"
elif h < 4 and prev < 5:
    w = "overnight"
elif wd >= 5 or (h < 4 and prev >= 5):
    w = "weekend"
else:
    w = "closed — a deploy needs his dated order"
print("window: " + w)
print("now: " + t.strftime("%Y-%m-%d %H:%M %A") + " ET" + (" (ORDER_OPEN_NOW)" if raw else ""))
print("holidays are not known to this script: a market holiday is the desk'"'"'s read")
' 2>/dev/null || echo "window: unknown (python3 failed)"

echo "MAIN"
if git -C "$REPO" rev-parse --verify --quiet refs/remotes/origin/main >/dev/null 2>&1; then
    echo "ahead of origin/main: $(git -C "$REPO" rev-list --count origin/main..main 2>/dev/null)"
else
    echo "ahead of origin/main: unknown (no origin/main in $REPO)"
fi
dirty=$(git -C "$REPO" status --porcelain --untracked-files=no 2>/dev/null)
if [ -n "$dirty" ]; then
    echo "uncommitted tracked changes: yes ($(printf '%s\n' "$dirty" | wc -l | tr -d ' ') path(s))"
else
    echo "uncommitted tracked changes: no"
fi

echo "WORKTREES"
now=$(date +%s)
seen=""
for d in "$WT"/*/; do
    d=${d%/}
    [ -d "$d" ] || continue
    seen=1
    name=${d##*/}
    br=$(git -C "$d" rev-parse --abbrev-ref HEAD 2>/dev/null) || { echo "$name: not a git worktree"; continue; }
    if [ "$br" = "HEAD" ]; then
        state="detached"
    elif git -C "$REPO" merge-base --is-ancestor "refs/heads/$br" main 2>/dev/null; then
        state="merged"
    else
        state="unmerged"
    fi
    ct=$(git -C "$d" log -1 --format=%ct 2>/dev/null)
    if [ -n "$ct" ]; then
        age="$(( (now - ct) / 86400 )) days"
    else
        age="no commit"
    fi
    echo "$name: branch $br · $state · $age"
done
[ -n "$seen" ] || echo "none"

echo "HOUSES"
if [ -f "$here/house-probe.sh" ]; then
    sh "$here/house-probe.sh" 2>&1 || echo "house-probe.sh exited non-zero"
else
    echo "not probed"
fi
exit 0
