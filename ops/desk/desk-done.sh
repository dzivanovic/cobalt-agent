#!/bin/sh
# desk-done.sh <session id> "<report>" <build|check|deploy|devfix|prodwrite|close|shadow> [<tab>]
# desk-done.sh <session id> --replaced [<tab>]
# Closes a finished worker in one call (card 17 A5; checklist W8); THE ONE CLOSE RULE (card
# 2026-10-15 580 C1, L79): every close goes through this script. Reads the report's last
# non-blank line against the kind's stop words (as desk-watch.sh):
#   a DONE line (build: BUILT; check: CHECK DONE; deploy: DEPLOYED; devfix: REBUILT;
#   prodwrite: WRITTEN; close: CLOSE PUSHED; shadow: SHADOW BUILT or SHADOW ROLE, card 386 L9)
#   -> `claude stop <id>`, `claude rm <id>`, and with a tab `herdr tab close <tab>`, each printed
#   before it runs; a failing step stops the script with exit 1 naming it.
#   a FAILED line of a build, a check or a shadow -> REFUSED: the worker is kept for CONTINUE.
#   a FAILED line of a prodwrite -> REFUSED: the seat is kept for the desk to read its backup
#   line (card 2026-10-12 392 W5 D2; it never resumes).
#   a FAILED line of a deploy, a devfix or a close -> closed like a DONE line.
#   any other last line -> REFUSED: still running.
# `--replaced` (the launcher's session its new launch replaces, card 580 C2) skips only the
# report read and the stop-word rules; the refusals, the tab lookup and the proof stay.
# A session whose name in `claude agents --json` starts with "brain" or is "cto-desk" is
# REFUSED (his 2026-09-30 R76: a brain is stopped only on his word); so is a session not
# in that list, or a list that cannot be read. A refusal: "REFUSED: <reason>" on stderr,
# exit 1, no stop, no rm, no tab close.
# THE TAB (card 580 C1 (a)): with no <tab>, the panes of `herdr pane list` (JSON, parsed, never
# split on blanks) whose terminal_title_stripped is the session's name: one gives its tab_id,
# none gives no tab, two or more -> `KEPT <id>: <n> tabs titled <name>` on stdout, exit 1, before
# any stop (an unreadable pane list: `KEPT <id>: pane list unreadable`). A passed <tab> wins.
# A session with no name looks up no tab; a tab holding a pane titled cto-desk or brain* ->
# `KEPT <id>: tab <tab> also holds a brain or the desk`, before any stop (check 2026-10-15 O1, O2).
# THE PROOF (card 580 C1 (b)), after the last close: `CLOSED <id>` as the last stdout line only
# when no row of `sh desk-list.sh` (beside this script) has an id starting <id>, no row of
# `claude agents --json` has that id, and no pane of `herdr pane list` sits in the closed tab;
# else `KEPT <id>: <LIST row|claude agents row|tab> still present` or `KEPT <id>: <LIST|claude
# agents --json|pane list> unreadable` on stdout, exit 1. It writes no file.
export LC_ALL=C
refuse() { echo "REFUSED: $1" >&2; exit 1; }
kept() { echo "KEPT $id: $1"; exit 1; }
USAGE='usage: desk-done.sh <session id> "<report>" <build|check|deploy|devfix|prodwrite|close|shadow> [<tab>] | desk-done.sh <session id> --replaced [<tab>]'
id="$1"
if [ "${2:-}" = "--replaced" ]; then
  replaced=1; report=""; kind=""; tab="${3:-}"
  [ -n "$id" ] && [ $# -le 3 ] || refuse "$USAGE"
else
  replaced=""; report="$2"; kind="$3"; tab="$4"
  [ -n "$id" ] && [ -n "$report" ] && [ -n "$kind" ] && [ $# -le 4 ] || refuse "$USAGE"
fi
if [ -z "$replaced" ]; then
case "$kind" in
  build)  done_re='^BUILT' ;;
  check)  done_re='^CHECK DONE' ;;
  deploy) done_re='^DEPLOYED' ;;
  devfix) done_re='^REBUILT' ;;
  prodwrite) done_re='^WRITTEN' ;;
  close)  done_re='^CLOSE PUSHED' ;;
  # card 386 L9: a shadow worker's FAILED line is kept for CONTINUE as a build's is (below)
  shadow) done_re='^SHADOW (BUILT|ROLE)'; kind=build ;;
  *) refuse "unknown kind: $kind" ;;
esac
[ -f "$report" ] || refuse "no report: $report"
last=$(grep -v '^[[:space:]]*$' "$report" | tail -1)
if printf '%s\n' "$last" | grep -qE "$done_re"; then
  :
elif printf '%s\n' "$last" | grep -qE '^FAILED'; then
  case "$kind" in
    build|check) refuse "FAILED — the worker is kept for CONTINUE: $last" ;;
    prodwrite) refuse "FAILED — the prodwrite seat is kept for the desk to read its backup line: $last" ;;
  esac
else
  refuse "still running — last line: $last"
fi
fi
name=$(claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
    hit = [a for a in rows if isinstance(a, dict) and a.get("id") == sys.argv[1]]
except Exception:
    sys.exit(3)
if len(hit) != 1:
    sys.exit(4)
print(hit[0].get("name") or "")
' "$id")
case $? in
  0) ;;
  4) refuse "session $id is not in claude agents --json" ;;
  *) refuse "claude agents --json could not be read" ;;
esac
case "$name" in
  brain*|cto-desk) refuse "$id is $name: a brain or the desk is stopped only on his word (2026-09-30 R76)" ;;
esac
# panes <title|tab> <value>: the tab_id of each pane titled <value>, or the pane_id of each pane in
# tab <value>; exit 3 when `herdr pane list` fails or is not JSON (cto-desk.sh's walk)
panes() {
  out=$(herdr pane list 2>/dev/null) || return 3
  printf '%s\n' "$out" | python3 -c '
import json, sys
by, value = sys.argv[1:3]
try:
    doc = json.load(sys.stdin)
except Exception:
    sys.exit(3)
def walk(node):
    if isinstance(node, list):
        for item in node:
            yield from walk(item)
    elif isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
for row in walk(doc):
    if "pane_id" not in row:
        continue
    if by == "title" and row.get("terminal_title_stripped") == value:
        print(row.get("tab_id") or "")
    elif by == "tab" and row.get("tab_id") == value:
        print(row["pane_id"])
    elif by == "titles" and row.get("tab_id") == value:
        print(row.get("terminal_title_stripped") or "")
' "$1" "$2"
}
# check 2026-10-15 O1: a session with no name finds no tab (an empty title matches untitled panes)
if [ -z "$tab" ] && [ -n "$name" ]; then
  found=$(panes title "$name") || kept "pane list unreadable"
  n=$(printf '%s' "$found" | grep -c '')
  [ "$n" -le 1 ] || kept "$n tabs titled $name"
  tab=$found
fi
# check 2026-10-15 O2: a tab that also holds the desk's or a brain's pane is never closed
if [ -n "$tab" ]; then
  titles=$(panes titles "$tab") || kept "pane list unreadable"
  ! printf '%s\n' "$titles" | grep -qE '^(cto-desk|brain.*)$' \
    || kept "tab $tab also holds a brain or the desk"
fi
step() {
  echo "+ $*"
  "$@" || { rc=$?; echo "FAILED STEP: $* (exit $rc)" >&2; exit 1; }
}
step claude stop "$id"
step claude rm "$id"
[ -z "$tab" ] || step herdr tab close "$tab"
# the proof: the LIST row, the claude agents --json row, the tab
rows=$(sh "$(dirname "$0")/desk-list.sh" 2>/dev/null) || kept "LIST unreadable"
printf '%s\n' "$rows" | awk -F ' · ' -v id="$id" 'index($1, id) == 1 { found = 1 } END { exit !found }' \
  && kept "LIST row still present"
claude agents --json 2>/dev/null | python3 -c '
import json, sys
try:
    rows = json.load(sys.stdin)
    assert isinstance(rows, list)
except Exception:
    sys.exit(3)
sys.exit(4 if any(isinstance(a, dict) and a.get("id") == sys.argv[1] for a in rows) else 0)
' "$id"
case $? in
  0) ;;
  4) kept "claude agents row still present" ;;
  *) kept "claude agents --json unreadable" ;;
esac
if [ -n "$tab" ]; then
  left=$(panes tab "$tab") || kept "pane list unreadable"
  [ -z "$left" ] || kept "tab still present"
fi
echo "CLOSED $id"
