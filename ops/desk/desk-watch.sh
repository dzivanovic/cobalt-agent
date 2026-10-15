#!/bin/sh
# desk-watch.sh <build|check|deploy|devfix|shadow|prodwrite|close> "<card or close report>" [max-seconds]
# Reads, and at a stop line closes (card 2026-10-15 580 C2, C4 below). The desk's ONE watch command (card 17 A2). Derives the report from the card
# (build: REPORT; check: CHECK REPORT; deploy, devfix, shadow and prodwrite: REPORT; close: the path
# given) and the stop regex from the kind (build: BUILT|FAILED; check: CHECK DONE|FAILED; deploy:
# DEPLOYED|FAILED; devfix: REBUILT|FAILED; shadow: SHADOW BUILT|SHADOW ROLE|FAILED; prodwrite:
# WRITTEN|FAILED; close: CLOSE PUSHED|FAILED; at line start). Kind shadow (card 2026-10-11 324 S4)
# watches the gate seat <JOB>-gate; kind prodwrite (card 2026-10-12 392 W5) the seat prodwrite-<JOB>.
# FIRST it reads the report's last non-blank line: already a stop line of that kind ->
# prints it, exit 0, no wait. Else it waits as wait-stop-line.sh does (the last non-blank
# line changed AND matching; a missing file is waited for), polling every DESK_WATCH_POLL
# seconds (default 20). max-seconds defaults to 7000; more is refused (the harness's
# background limit is two hours). On the limit: prints
# "STILL RUNNING after <n>s — last line: <line>", exit 2. A refusal: "REFUSED: <reason>"
# on stderr, exit 1. It writes only the FINISHED line below (and C4's install-ops links).
# THE CLOSE (card 2026-10-15 580 C2), after a printed stop line, the exit status unchanged: for
# build, check, devfix and shadow a FAILED line prints `KEPT <session>: FAILED, kept until CONTINUE
# or a replacement (W8)`; any other is CLEAN when the worktree /Users/cobalt/cobalt-wt/<WORKTREE>
# is clean, the report committed and every LIST row of the session idle (wait-stop-line.sh's
# rule), polled every DESK_WATCH_POLL s for up to DESK_WATCH_CLOSE_WAIT s (default 120). Clean and
# ONE listed row -> `sh desk-done.sh <id> "<report>" <kind>` (beside this script), its last stdout
# line printed last; else `KEPT <id>: <tree not clean|report not committed|session busy>` or
# `KEPT <session>: <n> listed sessions` / `no listed session`. A deploy's DEPLOYED line is clean
# when the session is idle; its FAILED line prints `KEPT <session>: FAILED deploy, closed through
# desk-done.sh by the desk`; prodwrite and close print `KEPT <session>: closed through desk-done.sh
# by the desk`. Each non-FAILED close or KEPT of these, prodwrite and close included, appends
# `<ISO time ET> <id> <session> <first word>` to /Users/cobalt/cobalt-wt/.job-state/FINISHED
# (stop-guard.py's record, C3), one line per listed id (`-` when none is listed); the close-wait's
# last sleep is cut to what is left of it (check 2026-10-15 A1-A3).
# desk-done.sh not beside this script -> the line goes to stderr only, nothing waits or is written.
# INSTALL-OPS (card 580 C4): a deploy's `DEPLOYED <TAG> <stack-final> …` line whose set (`git -C
# <repo> diff --name-only pre-<JOB> <stack-final>`) holds an ops/desk/ path runs `sh desk-launch.sh
# install-ops` (beside this script) and prints its last line last (`install-ops FAILED: <first
# line>` on a non-zero exit); no such path -> nothing; a FAILED line, no tag, an unreadable diff or
# no desk-launch.sh beside -> one stderr line `install-ops not run: <reason>`.
# THE IDLE EXIT (card 09 W1): every poll, after the stop-line read, runs the idle probe
# (`wait-stop-line.sh --idle`, beside this script; it reads desk-list.sh beside it and the WAKE
# file) for the watched session: the hub's LIST name — build <JOB>-build, check <JOB>-check,
# devfix <JOB>-devfix, deploy deploy-hub-<JOB>, prodwrite prodwrite-<JOB>, close close-<mmdd> of close-<YYYY-MM-DD>.md —
# and, for build, check and devfix, WAKE lines naming the card's WORKTREE appended after the
# watch began and after the last poll that read the session busy (a WAKE line raised during a
# background run is spent by that poll, check O1). The session shown idle for two consecutive polls with the last line unchanged,
# or a new WAKE line while it is not busy -> prints "IDLE: <session> — <the WAKE line or
# "no WAKE line">" and the report's last five non-blank lines, exit 3. The session in no LIST
# row for two consecutive polls -> "GONE: <session>" and the same five lines, exit 3.
export LC_ALL=C
refuse() { echo "REFUSED: $1" >&2; exit 1; }
kind="$1"; src="$2"; max="${3:-7000}"; poll="${DESK_WATCH_POLL:-20}"
[ -n "$src" ] || refuse "usage: desk-watch.sh <build|check|deploy|devfix|shadow|prodwrite|close> <card or close report> [max-seconds]"
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
  shadow) report=$(header REPORT) || exit 1; re='^(SHADOW BUILT|SHADOW ROLE|FAILED)' ;;
  prodwrite) report=$(header REPORT) || exit 1; re='^(WRITTEN|FAILED)' ;;
  close)  report="$src"; re='^(CLOSE PUSHED|FAILED)' ;;
  *) refuse "unknown kind: $kind" ;;
esac
wt=-
case "$kind" in
  build|check|devfix) job=$(header JOB) || exit 1; wt=$(header WORKTREE) || exit 1; session="$job-$kind" ;;
  shadow) job=$(header JOB) || exit 1; wt=$(header WORKTREE) || exit 1; session="$job-gate" ;;
  deploy) job=$(header JOB) || exit 1; session="deploy-hub-$job" ;;
  prodwrite) job=$(header JOB) || exit 1; session="prodwrite-$job" ;;
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
# ---- THE CLOSE (card 2026-10-15 580 C2) ----
FINISHED=/Users/cobalt/cobalt-wt/.job-state/FINISHED
# listed: "<id> <status> <state>" of each LIST row of the session; exit 1 when LIST is unreadable
listed() {
  all=$(sh "$here/desk-list.sh" 2>/dev/null) || return 1
  printf '%s\n' "$all" | awk -F ' · ' -v s="$session" '$2 == s { print $1, $4, $5 }'
}
# unclean: the first of tree not clean, report not committed, session busy; nothing when clean
unclean() {
  if [ "$wt" != - ]; then
    [ -z "$(git -C "/Users/cobalt/cobalt-wt/$wt" status --short 2>&1)" ] || { echo "tree not clean"; return; }
    rdir=$(dirname "$report")
    { [ -z "$(git -C "$rdir" status --short -- "$report" 2>&1)" ] \
      && [ -n "$(git -C "$rdir" log -1 --format=%h -- "$report" 2>/dev/null)" ]; } \
      || { echo "report not committed"; return; }
  fi
  mine=$(listed) || { echo "session busy"; return; }
  printf '%s\n' "$mine" | awk 'NF && !($2 == "idle" && $3 != "working") { b = 1 } END { exit !b }' \
    && echo "session busy"
}
# close_worker <stop line>: its one line on stdout (see the header)
close_worker() {
  case "$1" in
    FAILED*)
      case "$kind" in
        prodwrite|close) echo "KEPT $session: closed through desk-done.sh by the desk" ;;
        deploy) echo "KEPT $session: FAILED deploy, closed through desk-done.sh by the desk" ;;
        *) echo "KEPT $session: FAILED, kept until CONTINUE or a replacement (W8)" ;;
      esac
      return ;;
  esac
  # check 2026-10-15 A2: a WRITTEN prodwrite or a CLOSE PUSHED close is KEPT for the desk and
  # recorded like any other clean finish; it waits for nothing
  why=""; cw=0
  if [ "$kind" != prodwrite ] && [ "$kind" != close ]; then
    cw=${DESK_WATCH_CLOSE_WAIT:-120}
    case "$cw" in ''|*[!0-9]*) cw=120 ;; esac
    why=$(unclean)
  fi
  spent=0
  # check 2026-10-15 A1: the last sleep is cut to what is left of the close-wait
  while [ -n "$why" ] && [ "$spent" -lt "$cw" ]; do
    nap=$poll
    [ $((cw - spent)) -ge "$nap" ] || nap=$((cw - spent))
    sleep "$nap"
    spent=$((spent + nap))
    why=$(unclean)
  done
  mine=$(listed) || mine=""
  n=$(printf '%s\n' "$mine" | awk 'NF { n++ } END { print n + 0 }')
  rid=-
  [ "$n" -ne 1 ] || rid=$(printf '%s\n' "$mine" | awk 'NF { print $1 }')
  # check 2026-10-15 A3: two or more listed rows record each id, so stop-guard.py can name them
  ids=$rid
  [ "$n" -le 1 ] || ids=$(printf '%s\n' "$mine" | awk 'NF { print $1 }')
  if [ "$kind" = prodwrite ] || [ "$kind" = close ]; then
    said="KEPT $session: closed through desk-done.sh by the desk"
  elif [ -n "$why" ]; then
    [ "$rid" != - ] && said="KEPT $rid: $why" || said="KEPT $session: $why"
  elif [ "$n" -eq 0 ]; then
    said="KEPT $session: no listed session"
  elif [ "$n" -gt 1 ]; then
    said="KEPT $session: $n listed sessions"
  else
    out=$(sh "$here/desk-done.sh" "$rid" "$report" "$kind")
    rc=$?
    said=$(printf '%s\n' "$out" | grep -v '^[[:space:]]*$' | tail -n 1)
    [ -n "$said" ] || said="KEPT $rid: desk-done.sh exit $rc"
  fi
  at=$(TZ=America/New_York date +%Y-%m-%dT%H:%M:%S%z)
  if mkdir -p "$(dirname "$FINISHED")"; then
    for fid in $ids; do
      printf '%s %s %s %s\n' "$at" "$fid" "$session" "${1%% *}" >> "$FINISHED"
    done
  fi
  echo "$said"
}
# install_ops <stop line> (card 580 C4): a DEPLOYED set touching ops/desk/ -> install-ops
install_ops() {
  case "$1" in
    "DEPLOYED "*) ;;
    *) echo "install-ops not run: not a DEPLOYED line" >&2; return ;;
  esac
  final=$(printf '%s\n' "$1" | awk '{ print $3 }')
  case "$final" in
    [0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]) ;;
    *) echo "install-ops not run: no 8-hex merged head in the DEPLOYED line" >&2; return ;;
  esac
  [ -f "$here/desk-launch.sh" ] || { echo "install-ops not run: desk-launch.sh is not beside this script" >&2; return; }
  repo=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
  git -C "$repo" rev-parse -q --verify "refs/tags/pre-$job" >/dev/null 2>&1 \
    || { echo "install-ops not run: no tag pre-$job" >&2; return; }
  set_=$(git -C "$repo" diff --name-only "pre-$job" "$final" 2>/dev/null) \
    || { echo "install-ops not run: git diff pre-$job $final unreadable" >&2; return; }
  printf '%s\n' "$set_" | grep -q '^ops/desk/' || return 0
  ran=$(sh "$here/desk-launch.sh" install-ops 2>&1)
  if [ $? -eq 0 ]; then
    printf '%s\n' "$ran" | tail -n 1
  else
    echo "install-ops FAILED: $(printf '%s\n' "$ran" | sed -n '1p')"
  fi
}
# closeout <stop line>: called at both stop-line exits; never changes the exit status
closeout() {
  if [ -f "$here/desk-done.sh" ]; then
    close_worker "$1"
  else
    echo "KEPT $session: desk-done.sh is not beside this script" >&2
  fi
  [ "$kind" != deploy ] || install_ops "$1"
}
initial=$(lastline "$report")
if matches "$initial"; then
  printf '%s\n' "$initial"
  closeout "$initial"
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
    closeout "$cur"
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
