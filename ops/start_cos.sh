#!/bin/bash
# Wrapper for com.cobalt.cos.plist (F20), in the shape of ops/start_aset.sh.
# The plist stays secret-free: COBALT_MASTER_KEY is sourced here from
# ~/.cobalt_key so the resident can open the Mattermost credential. The
# Agent SDK's CLI child never sees it: cobalt/cos/session.py spawns it with
# exactly PATH, HOME, USER, LANG and COBALT_ENV (FINAL §4, card DECISION 5).
#
# BUILT, NOT LOADED: com.cobalt.cos ships `enabled: false`; nothing runs
# this script until the deploy's D14 checklist, T10 and X1.

set -e

export COBALT_ENV="production"

REPO_ROOT="/Users/cobalt/cobalt"
LOG_DIR="$REPO_ROOT/logs"
mkdir -p "$LOG_DIR"

KEY_FILE="$HOME/.cobalt_key"
if [ -f "$KEY_FILE" ]; then
    # shellcheck disable=SC1090
    source "$KEY_FILE"
else
    echo "WARNING: $KEY_FILE not found — the Mattermost credential cannot be unlocked." >&2
fi

cd "$REPO_ROOT"
# The venv python is exec'd directly (the aset-orphan rule of start_aset.sh):
# launchd's pid IS the python. The sync first keeps pyproject.toml / uv.lock
# read at every start; under `set -e` a failed sync exits here.
uv sync --inexact
exec "$REPO_ROOT/.venv/bin/python" -m cobalt.cos.run
