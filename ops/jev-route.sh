#!/bin/sh
# The JEV keyed router wrapper (card 2026-10-18/715 W1, his 2026-10-18 R1830, F12).
# Run as `sh /Users/cobalt/cobalt/ops/jev-route.sh --day <YYYY-MM-DD>` by the nightly close
# (CLOSE-HUB.md STEP 7b), the one place that runs it. The shape of
# ops/run_classify_trial.sh@f4e8de85:13-25. The key file (the one ops/run_backup.sh uses) is
# sourced into this shell only and reaches the exec'd `uv` process and nothing else; no
# session, prompt, command line, log or report carries it (L41). The router reads the
# OpenRouter key from VaultManager at call time; this script never reads, prints or exports it.
# The arguments are checked before any other line runs: a refused call never sources the key.
set -e

[ "$#" -eq 2 ] || exit 64
[ "$1" = "--day" ] || exit 64
case "$2" in
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) ;;
    *) exit 64 ;;
esac

export COBALT_VAULT_FILE="/Users/cobalt/cobalt/data/.cobalt_vault"
cd /Users/cobalt/cobalt

KEY_FILE="$HOME/.cobalt_key"
[ -f "$KEY_FILE" ] || exit 78   # EX_CONFIG, as ops/run_backup.sh
. "$KEY_FILE"

exec uv run cobalt classify route --day "$2" --run
