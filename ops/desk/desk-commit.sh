#!/bin/sh
# desk-commit.sh "<message>" <path> …
# The desk's commit of its own files (card 17 A4): `git -C $REPO add -- <paths>` then
# `git -C $REPO commit -m "<message>" -- <paths>`. A relative path is taken from $REPO.
# Refused: no path; a path outside $REPO; any path under src/, configs/, ops/ or tests/.
# The exit status and output of the add and the commit are passed through (the pre-commit
# hook still decides). A refusal: "REFUSED: <reason>" on stderr, exit 1, nothing staged.
# REPO = ${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
export LC_ALL=C
REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}
refuse() { echo "REFUSED: $1" >&2; exit 1; }
[ $# -ge 1 ] && [ -n "$1" ] || refuse 'usage: desk-commit.sh "<message>" <path> …'
msg="$1"; shift
[ $# -ge 1 ] || refuse "no path to commit"
n=$#
i=0
while [ "$i" -lt "$n" ]; do
  p="$1"; shift
  rel=$(python3 - "$REPO" "$p" <<'PY'
import os, sys

repo, path = sys.argv[1:3]
root = os.path.realpath(repo)
full = os.path.realpath(os.path.join(root, path))
if not full.startswith(root + os.sep):
    sys.stderr.write("REFUSED: a path outside the repo: %s\n" % path)
    sys.exit(1)
rel = os.path.relpath(full, root)
top = rel.split(os.sep, 1)[0]
# the volume is case-insensitive: SRC/x.py is src/x.py
if top.lower() in ("src", "configs", "ops", "tests"):
    sys.stderr.write("REFUSED: a code path is not the desk's to commit: %s\n" % rel)
    sys.exit(1)
print(rel)
PY
) || exit 1
  set -- "$@" "$rel"
  i=$((i + 1))
done
git -C "$REPO" add -- "$@" || exit $?
git -C "$REPO" commit -m "$msg" -- "$@"
