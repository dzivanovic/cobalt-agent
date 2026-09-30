#!/bin/sh
# wait-stop-line.sh <report-file> <extended-regex> [max-seconds]
# Read-only. Watches the LAST NON-BLANK LINE of a report file (the desk's watch convention:
# key on the last line only, never a header or a quoted body line). Records that line at
# start-up and waits until the last line BOTH matches <regex> AND differs from the one that
# was already there -- so an append-style report whose previous run left its own stop line
# last does not fire immediately. Prints the new line, exits 0. Exits 2 on timeout.
# Writes nothing.
f="$1"; re="$2"; max="${3:-3600}"; waited=0
lastline() { grep -v '^[[:space:]]*$' "$1" 2>/dev/null | tail -1; }
initial=$(lastline "$f")
while [ "$waited" -lt "$max" ]; do
  cur=$(lastline "$f")
  if [ "$cur" != "$initial" ] && printf '%s\n' "$cur" | grep -qE "$re"; then
    printf '%s\n' "$cur"
    exit 0
  fi
  sleep 20
  waited=$((waited + 20))
done
echo "TIMEOUT after ${max}s — last line was: $(lastline "$f")"
exit 2
