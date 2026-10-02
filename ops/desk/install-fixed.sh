#!/bin/sh
# install-fixed.sh "<fixed file>" <YYYY-MM-DD> <R<n>>
# Installs a fixed file whose title still carries the install token (card 17 A6).
# It proves the row first: the lines of $REPORTS/cto-<date>.md that start "| R<n> |" are
# exactly ONE, holding "HIS RULING" and "APPROVED", and
# `git -C $REPO log -1 --format=%H -S"| R<n> |" -- <that file>` is non-empty, and the
# same row line stands in that file at HEAD (an uncommitted edit of the row is no proof); else
# "REFUSED: no approved, committed row". It accepts only a file directly under
# $REPO/docs/40 - DevDocs/prompts/ whose FIRST line holds the token («INSTALL); it replaces,
# in line 1 only, the span from that guillemet to its closing guillemet with
# "INSTALL: <date> R<n> of his approval of STANDING-LIST.md" (a leading DRAFT-style note is
# left to the build that wrote the file), proves no token is left in the file, and prints
# the old and the new line 1. Commits nothing. A refusal: "REFUSED: <reason>" on stderr,
# exit 1, the file untouched. REPO = ${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
REPORTS="$REPO/docs/40 - DevDocs/reports"
refuse() { echo "REFUSED: $1" >&2; exit 1; }
file="$1"; date="$2"; r="$3"
[ $# -eq 3 ] || refuse 'usage: install-fixed.sh "<fixed file>" <YYYY-MM-DD> <R<n>>'
printf '%s\n' "$date" | grep -qE '^[0-9]{4}-[0-9]{2}-[0-9]{2}$' || refuse "not a date: $date"
n=${r#R}
case "$n" in ''|*[!0-9]*) refuse "not a row number: $r" ;; esac
day="$REPORTS/cto-$date.md"
[ -f "$day" ] || refuse "no approved, committed row: no desk report $day"
rows=$(grep -c "^| R$n |" "$day")
[ "$rows" = 1 ] || refuse "no approved, committed row: $rows lines start | R$n | in $day"
row=$(grep "^| R$n |" "$day")
case "$row" in *"HIS RULING"*) ;; *) refuse "no approved, committed row: R$n holds no HIS RULING" ;; esac
case "$row" in *APPROVED*) ;; *) refuse "no approved, committed row: R$n holds no APPROVED" ;; esac
commit=$(git -C "$REPO" log -1 --format=%H -S"| R$n |" -- "docs/40 - DevDocs/reports/cto-$date.md")
[ -n "$commit" ] || refuse "no approved, committed row: R$n of cto-$date.md is not committed"
git -C "$REPO" show "HEAD:docs/40 - DevDocs/reports/cto-$date.md" 2>/dev/null | grep -qxF -- "$row" \
  || refuse "no approved, committed row: R$n of cto-$date.md differs from its line at HEAD"
python3 - "$file" "$REPO/docs/40 - DevDocs/prompts" "INSTALL: $date R$n of his approval of STANDING-LIST.md" <<'PY'
import os, sys

path, prompts, install = sys.argv[1:4]
TOKEN = "«INSTALL"

def refuse(why):
    sys.stderr.write("REFUSED: %s\n" % why)
    sys.exit(1)

if not os.path.isfile(path):
    refuse("no file: %s" % path)
if os.path.realpath(os.path.dirname(os.path.abspath(path))) != os.path.realpath(prompts):
    refuse("not a file directly under %s: %s" % (prompts, path))
raw = open(path, "rb").read().decode("utf-8")
first, sep, rest = raw.partition("\n")
start = first.find(TOKEN)
if start < 0:
    refuse("line 1 holds no install token: %s" % first)
close = first.find("»", start)
if close < 0:
    refuse("the install token on line 1 is not closed: %s" % first)
new = first[:start] + install + first[close + 1:]
out = new + sep + rest
left = out.count(TOKEN)
if left:
    refuse("%d install token(s) would be left in the file; nothing changed" % left)
open(path, "wb").write(out.encode("utf-8"))
print("old line 1: " + first)
print("new line 1: " + new)
PY
