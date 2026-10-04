#!/bin/sh
# stage-copy.sh <source> <dest> — a check hub's copy of one file for an outside house (his 2026-10-01 R37).
# The house CLIs read only inside agy-trial, so a file is copied there by command, never retyped by a model.
# Source: a file under a job worktree /Users/cobalt/cobalt-wt/<tree>/ or the main tree's docs/.
# Dest: a path under /Users/cobalt/cobalt-wt/agy-trial/scratch/; its parent folders are made.
# Prints `COPIED <bytes> <dest>` after cmp proves the copy byte-identical; anything else exits 1.

export LC_ALL=C
refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

[ "$#" -eq 2 ] || refuse "usage: stage-copy.sh <source> <dest>"
src=$1
dst=$2

case "$src$dst" in
    *..*) refuse "a path holds '..'" ;;
esac
case "$src" in
    /Users/cobalt/cobalt-wt/agy-trial/*) refuse "the source sits inside agy-trial: $src" ;;
    /Users/cobalt/cobalt-wt/*/*|"/Users/cobalt/cobalt/docs/"*) ;;
    *) refuse "the source is not under a job worktree or the main tree's docs/: $src" ;;
esac
case "$dst" in
    /Users/cobalt/cobalt-wt/agy-trial/scratch/*/*) ;;
    *) refuse "the dest is not under /Users/cobalt/cobalt-wt/agy-trial/scratch/: $dst" ;;
esac
case "$src" in
    */.env|*/.env.*) refuse "never a .env file: $src" ;;
esac
[ -f "$src" ] && [ ! -L "$src" ] || refuse "no such plain file: $src"

mkdir -p "$(dirname "$dst")" || refuse "mkdir failed: $(dirname "$dst")"
cp "$src" "$dst" || refuse "cp failed: $src -> $dst"
cmp -s "$src" "$dst" || refuse "the copy differs from its source: $dst"
printf 'COPIED %s %s\n' "$(wc -c < "$dst" | tr -d ' ')" "$dst"
