#!/bin/bash
# Wrapper for com.cobalt.aset.plist. Exists so the LaunchAgent plist
# itself stays secret-free: COBALT_MASTER_KEY is sourced here from
# ~/.cobalt_key (same key file cobalt.sh's `start` case uses), never
# written into the plist's EnvironmentVariables. Without it, the ASET
# sheet's own pages still serve, but its Finviz last-price prefill
# (/api/prefill) fails every call — VaultManager can't unlock.
#
# Best-effort log rotation: since launchd binds stdout/stderr to
# StandardOutPath/StandardErrorPath once at process spawn (no SIGHUP-
# style reopen support, and this script does not touch aset's own
# Python code per this session's scope), rotation happens HERE, once
# per (re)start — at boot (RunAtLoad) or any KeepAlive relaunch after a
# crash — not live mid-run. See ops/README.md.
#
# NN#16 dev/prod vault split (formalized 2026-08-31): configs/dev/
# vault.yaml's committed default now points at the DEV skeleton vault
# (~/dev-vault-cobalt), not the real one — see src/cobalt/vault.py.
# This is PRODUCTION, so it explicitly overrides back to the real vault
# via COBALT_VAULT_PATH. Without this line ASET would silently start
# writing sizing cards into the dev vault instead of Dejan's real one.
#
# Defect 1 fix (2026-09-01): COBALT_ENV=production is this launcher's
# own declaration of intent — cobalt.vault.resolve_vault_path() refuses
# outright if it ever sees this flag alongside a non-Think root (stale
# process, wrong override, etc.), so a misconfigured production run
# fails loud on its next write instead of silently going to dev-vault-
# cobalt for hours. See src/cobalt/vault.py.

set -e

export COBALT_VAULT_PATH="/Users/cobalt/Vault/Think"
export COBALT_ENV="production"

REPO_ROOT="/Users/cobalt/cobalt"
LOG_DIR="$REPO_ROOT/logs"
LOG_FILE="$LOG_DIR/aset.log"
ERR_FILE="$LOG_DIR/aset.err"
MAX_BYTES=$((5 * 1024 * 1024))  # 5MB
KEEP=5

mkdir -p "$LOG_DIR"

rotate_if_large() {
    local file="$1"
    if [ -f "$file" ] && [ "$(stat -f%z "$file" 2>/dev/null || echo 0)" -gt "$MAX_BYTES" ]; then
        mv "$file" "${file}.$(date +%Y%m%d%H%M%S)"
        # keep only the KEEP most recent rotated files
        ls -t "${file}".* 2>/dev/null | tail -n +$((KEEP + 1)) | xargs -r rm --
    fi
}
rotate_if_large "$LOG_FILE"
rotate_if_large "$ERR_FILE"

KEY_FILE="$HOME/.cobalt_key"
if [ -f "$KEY_FILE" ]; then
    # shellcheck disable=SC1090
    source "$KEY_FILE"
else
    echo "WARNING: $KEY_FILE not found — Finviz prefill will fail (vault can't unlock)." >&2
fi

cd "$REPO_ROOT"
# Resolve uv via PATH, not a hardcoded prefix: on this machine uv lives
# at ~/.local/bin/uv, not /opt/homebrew/bin/uv (the path the older
# archiver/mainframe plists hardcode — see ops/README.md's note on that
# discrepancy). The plist's own EnvironmentVariables PATH includes
# ~/.local/bin, so a bare `uv` resolves correctly here.
exec uv run python -m cobalt.aset
