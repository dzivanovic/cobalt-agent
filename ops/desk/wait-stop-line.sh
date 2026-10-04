#!/bin/sh
# wait-stop-line.sh <report-file> <extended-regex> [max-seconds] [session] [worktree]
# Read-only. Watches the LAST NON-BLANK LINE of a report file (the desk's watch convention:
# key on the last line only, never a header or a quoted body line). Records that line at
# start-up and waits until the last line BOTH matches <regex> AND differs from the one that
# was already there -- so an append-style report whose previous run left its own stop line
# last does not fire immediately. Prints the new line, exits 0. Exits 2 on timeout.
# Writes nothing.
# First the desk-size guard (cto-2026-10-01 R8): desk-context.sh --guard, installed beside this
# script; at 300,000 tokens or more it prints its REFUSED line and this script exits 3 before
# its loop.
# THE IDLE EXIT (card 09 W1): with [session] (the LIST name, e.g. <job>-build), every poll also
# runs the --idle probe below; it exits 3 with an `IDLE:` or `GONE:` line and the report's last
# five non-blank lines (stdout; the guard's exit 3 prints `REFUSED:` instead). The WAKE lines it
# reads are those naming [worktree], else the worktree of the report path
# (/Users/cobalt/cobalt-wt/<worktree>/…; a check or devfix report on main names none, so give
# [worktree]), appended after the watch began and after the last poll that read the session busy
# (a line raised during a background run is spent, check O1). Without [session] the watch is as
# before.
#
# wait-stop-line.sh --idle <session> <worktree|-> <wake-lines-at-start> <previous> <report>
# The one idle probe, run per poll by this script and by desk-watch.sh. Reads desk-list.sh
# beside this script (rows `id · name · cwd · status · state`) and the WAKE file
# /Users/cobalt/cobalt-wt/.job-state/WAKE (idle-wake.py writes `<time> <worktree> IDLE <line>`).
# The session is: busy when any row of that name is not `idle`, or is `idle` with state
# `working` (a background run keeps `working` after the turn ends, R117), or the listing is
# unreadable (desk-list.sh exits non-zero); idle when every row of that name is `idle` with
# another state; gone when no row has that name. A new WAKE line for the worktree while the
# session is not busy -> `IDLE: <session> — <the WAKE line>`, exit 3. idle twice in a row
# (<previous> = idle) -> `IDLE: <session> — no WAKE line`, exit 3; gone twice in a row ->
# `GONE: <session>`, exit 3. Otherwise it prints the state (busy|idle|gone), exit 0; the caller
# passes it back as <previous> and resets it to busy when the report's last line changed.
# No desk-list.sh beside this script -> `REFUSED: …` on stderr, exit 1.
export LC_ALL=C
WT=/Users/cobalt/cobalt-wt
WAKE="$WT/.job-state/WAKE"
lastline() { grep -v '^[[:space:]]*$' "$1" 2>/dev/null | tail -1; }
if [ "${1:-}" = "--idle" ]; then
  session="$2"; wt="$3"; skip="$4"; prev="$5"; report="$6"
  list="$(dirname "$0")/desk-list.sh"
  [ -f "$list" ] || { echo "REFUSED: desk-list.sh is not beside this script: $list" >&2; exit 1; }
  if rows=$(sh "$list" 2>/dev/null); then
    state=$(printf '%s\n' "$rows" | awk -F ' · ' -v s="$session" '
      $2 == s { n++; if ($4 == "idle" && $5 != "working") idle++ }
      END { if (n == 0) print "gone"; else if (idle == n) print "idle"; else print "busy" }')
  else
    state=busy
  fi
  wake=""
  if [ "$wt" != "-" ] && [ -f "$WAKE" ]; then
    wake=$(tail -n +"$((skip + 1))" "$WAKE" | awk -v wt="$wt" '$2 == wt && $3 == "IDLE"' | tail -1)
  fi
  fire() {
    printf '%s\n' "$1"
    grep -v '^[[:space:]]*$' "$report" 2>/dev/null | tail -5
    exit 3
  }
  [ -z "$wake" ] || [ "$state" = busy ] || fire "IDLE: $session — $wake"
  [ "$state:$prev" != "idle:idle" ] || fire "IDLE: $session — no WAKE line"
  [ "$state:$prev" != "gone:gone" ] || fire "GONE: $session"
  printf '%s\n' "$state"
  exit 0
fi
sh "$(dirname "$0")/desk-context.sh" --guard || exit $?
f="$1"; re="$2"; max="${3:-3600}"; session="${4:-}"; waited=0
initial=$(lastline "$f")
if [ -n "$session" ]; then
  wt=${5:--}
  [ "$wt" != - ] || case "$f" in "$WT"/*/*) wt=${f#"$WT"/}; wt=${wt%%/*} ;; esac
  skip=0
  [ ! -f "$WAKE" ] || skip=$(awk 'END { print NR }' "$WAKE")
  prev=busy; seen=$initial
fi
while [ "$waited" -lt "$max" ]; do
  cur=$(lastline "$f")
  if [ "$cur" != "$initial" ] && printf '%s\n' "$cur" | grep -qE "$re"; then
    printf '%s\n' "$cur"
    exit 0
  fi
  if [ -n "$session" ]; then
    [ "$cur" = "$seen" ] || prev=busy
    seen=$cur
    out=$(sh "$0" --idle "$session" "$wt" "$skip" "$prev" "$f")
    rc=$?
    case "$rc" in
      0) prev=$out; [ "$out" != busy ] || [ ! -f "$WAKE" ] || skip=$(awk 'END { print NR }' "$WAKE") ;;
      3) printf '%s\n' "$out"; exit 3 ;;
      *) exit "$rc" ;;
    esac
  fi
  sleep 20
  waited=$((waited + 20))
done
echo "TIMEOUT after ${max}s — last line was: $(lastline "$f")"
exit 2
