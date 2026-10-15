#!/bin/sh
# result-read.sh KEY — print the value of KEY from a result file whose CONTENT comes on stdin
# (card 2026-10-14/548 RF1, his R1471 item (3)).
#
# A result file sits beside a report, its name the report's with `.md` cut and `.result` added. A
# BUILT or CHECK DONE seat writes it in the same step as the stop line, from the same values, and
# commits it with the report; the deploy gates (deploy-step0.sh P2, deploy-card.sh, desk-launch.sh
# P2) read it through this helper. The caller feeds the content (a file, or a blob read at a
# commit) and decides "no file" itself: it then reads the stop line as before.
#
# FORMAT: plain text, one key=value per line, split at the FIRST `=`; a blank line means nothing;
# no quote, no comment. KEYS are the stop line's own fields, lower case, `_` for a space, `-` or
# `.`, none added. The card's explicit `env` (the `.env` field) wins over that rule, which would
# give `_env`.
# BUILT keys: job tip on migration offline with_db live_note cobalt_dev env restarts rows self_check decisions for_dejan tokens
# CHECK DONE keys: job pass tip house_a findings dropped held fixed held_unfixed open house_b offline with_db live_note cobalt_dev env restarts files_opened ready decisions for_dejan tokens
#
# OUT: the value of KEY on stdout, exit 0. REFUSED (exit 1, `REFUSED: ...` on stderr, nothing on
# stdout): a non-blank line that is not key=value with a key of the two lists, a key that repeats,
# KEY absent or empty, KEY outside the lists.
# read-only: it reads stdin and prints; no write, no network.

export LC_ALL=C
set -u

refuse() {
    printf 'REFUSED: %s\n' "$*" >&2
    exit 1
}

known() {
    case "$1" in
        job|tip|on|migration|offline|with_db|live_note|cobalt_dev|env|restarts|rows|self_check|decisions|for_dejan|tokens|pass|house_a|findings|dropped|held|fixed|held_unfixed|open|house_b|files_opened|ready)
            return 0 ;;
    esac
    return 1
}

[ "$#" -eq 1 ] || refuse "usage: result-read.sh KEY (the result file's content on stdin)"
want=$1
known "$want" || refuse "'$want' is no result-file key"

seen=" "
value=""
found=""
while IFS= read -r line || [ -n "$line" ]; do
    case "$line" in
        *[![:space:]]*) ;;
        *) continue ;;
    esac
    case "$line" in
        *=*) ;;
        *) refuse "a line is not key=value: $line" ;;
    esac
    key=${line%%=*}
    known "$key" || refuse "'$key' is no result-file key: $line"
    case "$seen" in
        *" $key "*) refuse "the key '$key' repeats" ;;
    esac
    seen="$seen$key "
    if [ "$key" = "$want" ]; then
        found=1
        value=${line#*=}
    fi
done

[ -n "$found" ] || refuse "the key '$want' is absent"
[ -n "$value" ] || refuse "the key '$want' is empty"
printf '%s\n' "$value"
