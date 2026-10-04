#!/bin/sh
# desk-watch.sh <build|check|deploy|devfix|close> "<card or close report>" [max-seconds]
# Read-only. The desk's ONE watch command (card 17 A2). Derives the report from the card
# (build: REPORT; check: CHECK REPORT; deploy and devfix: REPORT; close: the path given)
# and the stop regex from the kind (build: BUILT|FAILED; check: CHECK DONE|FAILED; deploy:
# DEPLOYED|FAILED; devfix: REBUILT|FAILED; close: CLOSE PUSHED|FAILED; at line start).
# FIRST it reads the report's last non-blank line: already a stop line of that kind ->
# prints it, exit 0, no wait. Else it waits as wait-stop-line.sh does (the last non-blank
# line changed AND matching; a missing file is waited for), polling every DESK_WATCH_POLL
# seconds (default 20). max-seconds defaults to 7000; more is refused (the harness's
# background limit is two hours). On the limit: prints
# "STILL RUNNING after <n>s — last line: <line>", exit 2. A refusal: "REFUSED: <reason>"
# on stderr, exit 1. Writes nothing.
# THE IDLE EXIT (card 09 W1): every poll, after the stop-line read, runs the idle probe
# (`wait-stop-line.sh --idle`, beside this script; it reads desk-list.sh beside it and the WAKE
# file) for the watched session: the hub's LIST name — build <JOB>-build, check <JOB>-check,
# devfix <JOB>-devfix, deploy deploy-hub-<JOB>, close close-<mmdd> of close-<YYYY-MM-DD>.md —
# and, for build, check and devfix, WAKE lines naming the card's WORKTREE appended after the
# watch began and after the last poll that read the session busy (a WAKE line raised during a
# background run is spent by that poll, check O1). The session shown idle for two consecutive polls with the last line unchanged,
# or a new WAKE line while it is not busy -> prints "IDLE: <session> — <the WAKE line or
# "no WAKE line">" and the report's last five non-blank lines, exit 3. The session in no LIST
# row for two consecutive polls -> "GONE: <session>" and the same five lines, exit 3.
export LC_ALL=C
refuse() { echo "REFUSED: $1" >&2; exit 1; }
kind="$1"; src="$2"; max="${3:-7000}"; poll="${DESK_WATCH_POLL:-20}"
[ -n "$src" ] || refuse "usage: desk-watch.sh <build|check|deploy|devfix|close> <card or close report> [max-seconds]"
case "$max" in ''|*[!0-9]*) refuse "max-seconds is not a whole number: $max" ;; esac
[ "$max" -le 7000 ] || refuse "max-seconds $max is over 7000 (the background limit is two hours)"
case "$poll" in ''|0|*[!0-9]*) refuse "DESK_WATCH_POLL is not a whole number above 0: $poll" ;; esac
header() {
  [ -f "$src" ] || refuse "no card: $src"
  v=$(grep -m 1 "^$1: " "$src" | sed "s/^$1: //")
  [ -n "$v" ] || refuse "the card has no $1 value: $src"
  printf '%s\n' "$v"
}
case "$kind" in
  build)  report=$(header REPORT) || exit 1; re='^(BUILT|FAILED)' ;;
  check)  report=$(header 'CHECK REPORT') || exit 1; re='^(CHECK DONE|FAILED)' ;;
  deploy) report=$(header REPORT) || exit 1; re='^(DEPLOYED|FAILED)' ;;
  devfix) report=$(header REPORT) || exit 1; re='^(REBUILT|FAILED)' ;;
  close)  report="$src"; re='^(CLOSE PUSHED|FAILED)' ;;
  *) refuse "unknown kind: $kind" ;;
esac
wt=-
case "$kind" in
  build|check|devfix) job=$(header JOB) || exit 1; wt=$(header WORKTREE) || exit 1; session="$job-$kind" ;;
  deploy) job=$(header JOB) || exit 1; session="deploy-hub-$job" ;;
  close)
    b=$(basename "$report" .md)
    case "$b" in
      close-[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) md=${b#close-????-}; session="close-${md%-*}${md#*-}" ;;
      *) refuse "the close report is not close-<YYYY-MM-DD>.md: $report" ;;
    esac ;;
esac
here=$(dirname "$0")
[ -f "$here/wait-stop-line.sh" ] || refuse "wait-stop-line.sh (the idle probe) is not beside this script"
WAKE=/Users/cobalt/cobalt-wt/.job-state/WAKE
lastline() { grep -v '^[[:space:]]*$' "$1" 2>/dev/null | tail -1; }
matches() { printf '%s\n' "$1" | grep -qE "$re"; }
initial=$(lastline "$report")
if matches "$initial"; then
  printf '%s\n' "$initial"
  exit 0
fi
skip=0
[ ! -f "$WAKE" ] || skip=$(awk 'END { print NR }' "$WAKE")
prev=busy; seen=$initial
waited=0
while [ "$waited" -lt "$max" ]; do
  sleep "$poll"
  waited=$((waited + poll))
  cur=$(lastline "$report")
  if [ "$cur" != "$initial" ] && matches "$cur"; then
    printf '%s\n' "$cur"
    exit 0
  fi
  [ "$cur" = "$seen" ] || prev=busy
  seen=$cur
  out=$(sh "$here/wait-stop-line.sh" --idle "$session" "$wt" "$skip" "$prev" "$report")
  rc=$?
  case "$rc" in
    0) prev=$out; [ "$out" != busy ] || [ ! -f "$WAKE" ] || skip=$(awk 'END { print NR }' "$WAKE") ;;
    3) printf '%s\n' "$out"; exit 3 ;;
    *) exit "$rc" ;;
  esac
done
echo "STILL RUNNING after ${max}s — last line: $(lastline "$report")"
exit 2
