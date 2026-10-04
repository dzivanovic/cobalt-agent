#!/bin/sh
# desk-row.sh "<status>" "<text>"
# Appends ONE row to today's desk report $REPORTS/cto-<today>.md (card 17 A4), after the
# last line that starts with "| R<digits> |" and before the first "## §5" heading:
#   | R<n> | <HH:MM> ET | <text> | <status> |
# n = the highest R number of any row line in the file + 1; the time is `date +%H:%M`.
# Refused: a missing day file; no row line, or no "## §5" after the last one; a status or
# text that is empty or holds a table bar or a newline; a row over 300 characters (the
# pre-commit hook's `size` rule: a LAUNCHED row is counted without its backticked spans).
# Prints the row. Commits nothing. A refusal: "REFUSED: <reason>" on stderr, exit 1, the
# file untouched. REPORTS = ${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}/docs/40 - DevDocs/reports
export LC_ALL=C
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
REPORTS="$REPO/docs/40 - DevDocs/reports"
refuse() { echo "REFUSED: $1" >&2; exit 1; }
[ $# -eq 2 ] || refuse 'usage: desk-row.sh "<status>" "<text>"'
day="$REPORTS/cto-$(date +%Y-%m-%d).md"
[ -f "$day" ] || refuse "no desk report for today: $day"
python3 - "$day" "$(date +%H:%M)" "$1" "$2" <<'PY'
import re, sys

day, clock, status, text = sys.argv[1:5]

def refuse(why):
    sys.stderr.write("REFUSED: %s\n" % why)
    sys.exit(1)

for name, cell in (("status", status), ("text", text)):
    if not cell.strip():
        refuse("the %s is empty" % name)
    if "|" in cell:
        refuse("the %s holds a table bar" % name)
    if "\n" in cell or "\r" in cell:
        refuse("the %s holds a newline" % name)

def size(row):
    # the pre-commit hook's rule (ops/desk/pre-commit `size`)
    if row.rstrip().endswith("| LAUNCHED |"):
        row = re.sub(r"`[^`]*`", "", row)
    return len(row)

lines = open(day, "rb").read().decode("utf-8").split("\n")
ROW = re.compile(r"\| R(\d+) \|")
numbers = [int(m.group(1)) for m in (ROW.match(line) for line in lines) if m]
section5 = next((i for i, line in enumerate(lines) if line.startswith("## §5")), None)
if section5 is None:
    refuse("the desk report has no ## §5 heading: %s" % day)
rows = [i for i, line in enumerate(lines[:section5]) if ROW.match(line)]
if not rows:
    refuse("the desk report has no row line before ## §5: %s" % day)
row = "| R%d | %s ET | %s | %s |" % (max(numbers) + 1, clock, text, status)
if size(row) > 300:
    refuse("the row is %d characters, over 300 (cut it; detail goes to the words file)" % size(row))
lines.insert(rows[-1] + 1, row)
open(day, "wb").write("\n".join(lines).encode("utf-8"))
print(row)
PY
