#!/bin/sh
# card-fill.sh "<card>" [--no-house "<date> R<n>"]
# Fills a job card for its check from the build's stop line (card 17 A3). Reads the card's
# REPORT, takes its last non-blank line, and refuses unless it starts
# "BUILT · job: <the card's JOB> · tip: <8 hex>" and carries "self-check: 3 of 3".
# Then, editing ONLY header lines (those above the card's first blank line):
#   TIP:          <- that tip
#   CHECK REPORT: <- $REPORTS/<JOB>-check-<today>.md when empty
#   HOUSE B:      <- "as needed" when empty (a filled value is kept)
# With --no-house, a header line "HOUSE A: none — overruled <date> R<n>" is added after
# CHECK REPORT unless a HOUSE A line is there. Prints each changed line as "old → new"
# ("nothing changed" when none). Commits nothing; a second run changes nothing.
# A refusal: "REFUSED: <reason>" on stderr, exit 1, the card untouched.
# REPORTS = ${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}/docs/40 - DevDocs/reports
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
REPORTS="$REPO/docs/40 - DevDocs/reports"
refuse() { echo "REFUSED: $1" >&2; exit 1; }
card="$1"
[ -n "$card" ] || refuse 'usage: card-fill.sh "<card>" [--no-house "<date> R<n>"]'
[ -f "$card" ] || refuse "no card: $card"
house=""
if [ $# -gt 1 ]; then
  [ "$2" = "--no-house" ] && [ $# -eq 3 ] || refuse 'usage: card-fill.sh "<card>" [--no-house "<date> R<n>"]'
  house="$3"
  printf '%s\n' "$house" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2} R[0-9]+$' \
    || refuse "--no-house wants \"<YYYY-MM-DD> R<n>\", got: $house"
fi
today=$(date +%Y-%m-%d)
python3 - "$card" "$REPORTS" "$today" "$house" <<'PY'
import re, sys

card, reports, today, house = sys.argv[1:5]

def refuse(why):
    sys.stderr.write("REFUSED: %s\n" % why)
    sys.exit(1)

raw = open(card, "rb").read()
lines = raw.decode("utf-8").split("\n")
end = next((i for i, line in enumerate(lines) if line.strip() == ""), len(lines))
header = lines[:end]

def find(key):
    hits = [i for i, line in enumerate(header) if line == key + ":" or line.startswith(key + ": ")]
    if len(hits) > 1:
        refuse("the card's header has %d %s lines" % (len(hits), key))
    return hits[0] if hits else None

def value(i):
    return header[i].split(":", 1)[1].strip()

at = {k: find(k) for k in ("JOB", "REPORT", "TIP", "CHECK REPORT", "HOUSE B", "HOUSE A")}
for key in ("JOB", "REPORT", "TIP", "CHECK REPORT", "HOUSE B"):
    if at[key] is None:
        refuse("the card's header has no %s line" % key)
job, report = value(at["JOB"]), value(at["REPORT"])
if not job:
    refuse("the card's JOB is empty")
if not report:
    refuse("the card's REPORT is empty")
try:
    text = open(report, encoding="utf-8").read()
except OSError as e:
    refuse("cannot read the REPORT %s (%s)" % (report, e.strerror))
last = next((line for line in reversed(text.split("\n")) if line.strip()), "")
m = re.match(r"BUILT · job: (\S+) · tip: ([0-9a-f]{8})(?=\s|$)", last)
if not m or m.group(1) != job:
    refuse("the report's last line is not a BUILT line of job %s: %s" % (job, last))
if "self-check: 3 of 3" not in last:
    refuse("the BUILT line does not carry self-check: 3 of 3: %s" % last)
tip = m.group(2)

changes = []

def put(i, new):
    if header[i] != new:
        changes.append("%s → %s" % (header[i], new))
        header[i] = new

put(at["TIP"], "TIP: " + tip)
if not value(at["CHECK REPORT"]):
    put(at["CHECK REPORT"], "CHECK REPORT: %s/%s-check-%s.md" % (reports, job, today))
if not value(at["HOUSE B"]):
    put(at["HOUSE B"], "HOUSE B: as needed")
if house and at["HOUSE A"] is None:
    new = "HOUSE A: none — overruled " + house
    header.insert(at["CHECK REPORT"] + 1, new)
    changes.append("(no line) → " + new)

if not changes:
    print("nothing changed")
    sys.exit(0)
open(card, "wb").write("\n".join(header + lines[end:]).encode("utf-8"))
for change in changes:
    print(change)
PY
