#!/bin/bash
# Wrapper for com.cobalt.backup.plist. Exists so the plist stays
# secret-free: COBALT_MASTER_KEY is sourced here from ~/.cobalt_key (the
# same key file cobalt.sh and ops/start_aset.sh use), never written into
# EnvironmentVariables. Without it the restic repository password cannot
# be unlocked and the run fails loud in its first second — which is the
# correct outcome, and far better than restic prompting for a password
# inside launchd and hanging until its timeout.
#
# The Postgres connection parts come from the repo .env, the same file
# docker-compose interpolates, because this host has no host-side
# pg_dump and the dump goes through the cobalt_memory container (see
# src/cobalt/backup/pgdump.py).
#
# NOT LOADED INTO LAUNCHD as of 2026-09-04 — see the header of
# ops/pending/com.cobalt.backup.plist for why.
set -e

export COBALT_ENV="production"
export COBALT_VAULT_PATH="/Users/cobalt/Vault/Think"

REPO_ROOT="/Users/cobalt/cobalt"
cd "$REPO_ROOT"

KEY_FILE="$HOME/.cobalt_key"
if [ -f "$KEY_FILE" ]; then
    source "$KEY_FILE"
else
    echo "ERROR: $KEY_FILE not found — the restic repository password cannot be unlocked." >&2
    exit 78   # EX_CONFIG, the same signature the 09-03 prefill failure used
fi

# POSTGRES_HOST / USER / PASSWORD for the dump.
set -a; . "$REPO_ROOT/.env"; set +a

LOG_DIR="$REPO_ROOT/logs"
mkdir -p "$LOG_DIR"
exec /Users/cobalt/.local/bin/uv run cobalt backup run
