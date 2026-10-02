#!/bin/sh
# desk-done.sh <session id> "<report>" <build|check|deploy|devfix|close> [<tab>]
# Closes a finished worker in one call (card 17 A5; checklist W8). Reads the report's last
# non-blank line against the kind's stop words (as desk-watch.sh):
#   a DONE line (build: BUILT; check: CHECK DONE; deploy: DEPLOYED; devfix: REBUILT;
#   close: CLOSE PUSHED) -> `claude stop <id>`, `claude rm <id>`, and with a tab
#   `herdr tab close <tab>`, each printed before it runs; a failing step stops the
#   script with exit 1 naming it.
#   a FAILED line of a build or a check -> REFUSED: the worker is kept for CONTINUE.
#   a FAILED line of a deploy, a devfix or a close -> closed like a DONE line.
#   any other last line -> REFUSED: still running.
# A session whose name in `claude agents --json` starts with "brain" or is "cto-desk" is
# REFUSED (his 2026-09-30 R76: a brain is stopped only on his word); so is a session not
# in that list, or a list that cannot be read. A refusal: "REFUSED: <reason>" on stderr,
# exit 1, no stop, no rm, no tab close.
refuse() { echo "REFUSED: $1" >&2; exit 1; }
id="$1"; report="$2"; kind="$3"; tab="$4"
[ -n "$id" ] && [ -n "$report" ] && [ -n "$kind" ] && [ $# -le 4 ] \
  || refuse 'usage: desk-done.sh <session id> "<report>" <build|check|deploy|devfix|close> [<tab>]'
case "$kind" in
  build)  done_re='^BUILT' ;;
  check)  done_re='^CHECK DONE' ;;
  deploy) done_re='^DEPLOYED' ;;
  devfix) done_re='^REBUILT' ;;
  close)  done_re='^CLOSE PUSHED' ;;
  *) refuse "unknown kind: $kind" ;;
esac
[ -f "$report" ] || refuse "no report: $report"
last=$(grep -v '^[[:space:]]*$' "$report" | tail -1)
if printf '%s\n' "$last" | grep -qE "$done_re"; then
  :
elif printf '%s\n' "$last" | grep -qE '^FAILED'; then
  case "$kind" in
    build|check) refuse "FAILED — the worker is kept for CONTINUE: $last" ;;
  esac
else
  refuse "still running — last line: $last"
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
step() {
  echo "+ $*"
  "$@" || { rc=$?; echo "FAILED STEP: $* (exit $rc)" >&2; exit 1; }
}
step claude stop "$id"
step claude rm "$id"
[ -z "$tab" ] || step herdr tab close "$tab"
