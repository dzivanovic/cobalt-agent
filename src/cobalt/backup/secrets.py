"""One vault read, for the backup's credentials.

The value is fetched, handed to a subprocess environment, and never
returned anywhere it could be logged. The error path names the KEY and
never the value, and never the decryption exception's text — a
decryption error can echo material back (same reasoning as
`cobalt.redact.secrets`).
"""

from __future__ import annotations

import json
import os

from cobalt.redact.secrets import MASTER_KEY_ENV, VAULT_FILE


class VaultUnavailable(RuntimeError):
    """The vault could not be opened, or the key is not in it."""


def vault_value(key: str) -> str:
    """The vault value for `key`. Raises rather than returning "".

    An empty password is not a degraded backup, it is a repository
    nobody can open later — so this refuses instead of falling back.
    """
    master = os.getenv(MASTER_KEY_ENV)
    if not master:
        raise VaultUnavailable(
            f"{MASTER_KEY_ENV} is not set on this process, so {key!r} cannot be "
            "unlocked. The backup job sources it in its wrapper "
            "(ops/run_backup.sh), exactly as ops/start_aset.sh does."
        )
    if not VAULT_FILE.exists():
        raise VaultUnavailable(f"vault file {VAULT_FILE} does not exist")
    try:
        from cryptography.fernet import Fernet

        data = json.loads(Fernet(master.encode()).decrypt(VAULT_FILE.read_bytes()).decode())
    except Exception as e:  # noqa: BLE001 — the TYPE is safe to name, the text is not
        raise VaultUnavailable(
            f"vault could not be opened ({type(e).__name__}); the exception text is "
            "deliberately omitted."
        ) from None

    value = data.get(key)
    if isinstance(value, dict):  # nested shape, e.g. MATTERMOST_CREDS.token
        raise VaultUnavailable(f"vault key {key!r} is a mapping, not a value")
    if not isinstance(value, str) or not value:
        raise VaultUnavailable(
            f"vault key {key!r} is missing or empty. Store it with the same tool that "
            "holds MATTERMOST_CREDS; nothing about this credential belongs in git, "
            "in a plist, or in configs/cobalt/backup.yaml."
        )
    return value


__all__ = ["VaultUnavailable", "vault_value"]
