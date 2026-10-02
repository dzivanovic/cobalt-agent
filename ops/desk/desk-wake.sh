#!/bin/sh
# desk-wake.sh [<own session id>]
# Read-only. Prints what a waking CTO desk reads (card 18 desk-tools-b, row B4; replaces the
# reads of CTO-DESK-WAKEUP.md STEP 0.1 and READ 3–6), in this order, each under a `== <name> ==`
# heading:
#   LAST LINE     the last non-blank line of the newest $REPORTS/cto-<date>.md (a HANDOVER line or not)
#   SESSIONS      the live rows of `claude agents --json` (a row with a pid): id name cwd status state
#   §0            that report's `## §0` block
#   §4 ROWS       its §4 rows from the first one at or after the time of its last `HANDOVER:` line
#                 (every row when it has none)
#   §5 CURRENT    its `## §5 CURRENT` block, up to `## §5 HISTORY`
#   PENDING FOLD  every row of that report and the desk report before it holding
#                 `APPROVED — pending fold`, the first 300 characters of each
#   PROMPTS       the names in $PROMPTS/<today, New York>/
#   GIT           `git -C $REPO log --oneline -5`
#   CONTEXT       with a session id: the line desk-context.sh (beside this script) prints for it
# A desk report is a file named exactly cto-YYYY-MM-DD.md (a -words file is never read). It
# writes nothing. REFUSED (exit 1): an id outside [0-9a-f-] or shorter than 8; no desk report.
# Roots: COBALT_REPO_ROOT (default /Users/cobalt/cobalt), COBALT_WT_ROOT (default /Users/cobalt/cobalt-wt).

set -u

REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
PROMPTS="$REPO/docs/40 - DevDocs/prompts"
REPORTS="$REPO/docs/40 - DevDocs/reports"
GIT_OPTIONAL_LOCKS=0
export GIT_OPTIONAL_LOCKS
here=$(dirname "$0")

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -le 1 ] || refuse "usage: desk-wake.sh [<own session id>]"
id=${1:-}
if [ "$#" -eq 1 ]; then
    case "$id" in
        ""|*[!0123456789abcdef-]*) refuse "session id '$id' holds a character outside [0-9a-f-]" ;;
    esac
    [ "${#id}" -ge 8 ] || refuse "session id '$id' is shorter than 8 characters"
fi

reports=$(ls "$REPORTS" 2>/dev/null | grep -E '^cto-[0-9]{4}-[0-9]{2}-[0-9]{2}\.md$' | sort)
newest=$(printf '%s\n' "$reports" | sed '/^$/d' | tail -n 1)
[ -n "$newest" ] || refuse "no desk report cto-<date>.md under $REPORTS"
previous=$(printf '%s\n' "$reports" | sed '/^$/d' | tail -n 2 | sed -n '1p')
[ "$previous" != "$newest" ] || previous=""
today=$(TZ=America/New_York date +%Y-%m-%d)

# the desk report's parts: one mode per call, the file(s) after it
PARTS='
import re, sys
mode, files = sys.argv[1], sys.argv[2:]
lines = open(files[0], encoding="utf-8").read().splitlines()

def block(start, stop):
    out, on = [], False
    for line in lines:
        if on and stop(line):
            break
        if on:
            out.append(line)
        if not on and line == start:
            on = True
    return out

if mode == "s0":
    s0 = next((l for l in lines if l.startswith("## §0")), None)
    print("\n".join(block(s0, lambda l: l.startswith("## "))) if s0 else "no ## §0 block")
elif mode == "s4":
    s4 = next((l for l in lines if l.startswith("## §4")), None)
    rows = [l for l in block(s4, lambda l: l.startswith("## ")) if re.match(r"^\| R[0-9]+ \|", l)] if s4 else []
    hand = [m.group(1) for m in (re.match(r"^HANDOVER: .* at ([0-9]{2}:[0-9]{2}) ET", l) for l in lines) if m]
    if not hand:
        print("== §4 ROWS (no HANDOVER line: every row) ==")
        print("\n".join(rows))
    else:
        t = hand[-1]
        first = next((i for i, r in enumerate(rows)
                      if (m := re.match(r"^\| R[0-9]+ \| ([0-9]{2}:[0-9]{2}) ", r)) and m.group(1) >= t), len(rows))
        print("== §4 ROWS since the last HANDOVER at %s ET ==" % t)
        print("\n".join(rows[first:]))
elif mode == "s5":
    print("\n".join(block("## §5 CURRENT", lambda l: l.startswith("## §5 HISTORY"))))
elif mode == "pending":
    for f in files:
        name = f.rsplit("/", 1)[-1]
        hits = [l for l in open(f, encoding="utf-8").read().splitlines()
                if l.startswith("| R") and "APPROVED — pending fold" in l]
        print("%s: %d row(s)" % (name, len(hits)))
        for l in hits:
            print(l[:300])
'

echo "== LAST LINE ($newest) =="
grep -v '^[[:space:]]*$' "$REPORTS/$newest" | tail -n 1

echo "== SESSIONS =="
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

echo "== §0 =="
python3 -c "$PARTS" s0 "$REPORTS/$newest"
python3 -c "$PARTS" s4 "$REPORTS/$newest"
echo "== §5 CURRENT =="
python3 -c "$PARTS" s5 "$REPORTS/$newest"

echo "== PENDING FOLD =="
if [ -n "$previous" ]; then
    python3 -c "$PARTS" pending "$REPORTS/$previous" "$REPORTS/$newest"
else
    python3 -c "$PARTS" pending "$REPORTS/$newest"
fi

echo "== PROMPTS $today =="
if [ -d "$PROMPTS/$today" ]; then
    ls "$PROMPTS/$today"
else
    echo "none ($PROMPTS/$today does not exist)"
fi

echo "== GIT =="
git -C "$REPO" log --oneline -5

if [ -n "$id" ]; then
    echo "== CONTEXT =="
    if [ -f "$here/desk-context.sh" ]; then
        sh "$here/desk-context.sh" "$id"
    else
        echo "desk-context.sh is not beside this script"
    fi
fi
exit 0
