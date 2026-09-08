"""F19's literal guard — the half no regex can do.

Four of the credentials rotated on 2026-08-23 are USERNAMES AND
PASSWORDS: smbtraining.com, rt.smbtraining.com, financialjuice.com,
finviz.com. A human password has no shape. A regex broad enough to match
one matches ordinary prose; one narrow enough to spare prose does not
match the password. So they are matched LITERALLY, against the values
VaultManager already holds.

THE RULES THIS MODULE KEEPS, and they are not negotiable:

* values live in memory only, for the life of the process;
* nothing is ever logged, printed, persisted or returned — a hit is
  reported by its VAULT KEY NAME (`finviz.com::password`), never by its
  value, which is the same discipline the patterns keep;
* a locked vault is NOT an error. `COBALT_MASTER_KEY` is absent from
  every environment except the ones that need it, and the pattern half of
  the guard still runs. The literal half reports itself as unavailable so
  that "no literals loaded" is visible rather than assumed.

WHY THIS DOES NOT IMPORT `cobalt_agent.security.vault`. The strangler
rule (CLAUDE.md): the old tree stays untouched and nothing new imports
it. This reads the same encrypted file with the same key and the same
Fernet — 20 lines, no dependency across the boundary, and it never
writes. `cobalt.vault` was carved out of the old resolver the same way.
"""

from __future__ import annotations

import json
import os
from functools import lru_cache
from pathlib import Path
from typing import Optional

from loguru import logger

REPO_ROOT = Path(__file__).resolve().parents[3]

#: The same file `cobalt_agent.security.vault.VaultManager` reads.
VAULT_FILE = REPO_ROOT / "data" / ".cobalt_vault"

MASTER_KEY_ENV = "COBALT_MASTER_KEY"


class LiteralGuard:
    """Vault values, longest first, keyed by their vault name.

    Longest first because a shorter secret can be a substring of a longer
    one (a password inside a DSN, say); replacing the long one first
    means the short match never sees the text it would have mangled.
    """

    def __init__(self, values: dict[str, str], *, available: bool, reason: str = ""):
        self.available = available
        self.reason = reason
        self._by_name = dict(values)
        self._ordered = sorted(values.items(), key=lambda kv: -len(kv[1]))

    def __len__(self) -> int:
        return len(self._ordered)

    @property
    def names(self) -> list[str]:
        """Vault key NAMES only. Never the values — this is what a report
        or a test is allowed to see."""
        return sorted(self._by_name)

    def items(self):
        return list(self._ordered)


def _empty(reason: str) -> LiteralGuard:
    return LiteralGuard({}, available=False, reason=reason)


@lru_cache(maxsize=1)
def load_literals(min_length: int = 8) -> LiteralGuard:
    """Read the vault into memory, or say why it could not be read.

    Cached for the life of the process: the alternative is decrypting the
    vault on every outbound line, which would put the master key through
    a hot path for no gain.
    """
    key = os.getenv(MASTER_KEY_ENV)
    if not key:
        return _empty(
            f"{MASTER_KEY_ENV} is not set on this process — the literal half of the "
            "exfiltration guard is INACTIVE (the pattern half still runs)."
        )
    if not VAULT_FILE.exists():
        return _empty(f"vault file {VAULT_FILE} does not exist — literal guard INACTIVE.")
    try:
        from cryptography.fernet import Fernet

        data = json.loads(Fernet(key.encode()).decrypt(VAULT_FILE.read_bytes()).decode())
    except Exception as e:  # noqa: BLE001 - the REASON matters, the contents never appear
        return _empty(
            f"vault could not be opened ({type(e).__name__}) — literal guard INACTIVE. "
            "Note: the exception text is deliberately not included; a decryption error "
            "can echo material back."
        )

    values: dict[str, str] = {}
    for name, value in data.items():
        for leaf_name, leaf in _leaves(name, value):
            if isinstance(leaf, str) and len(leaf) >= min_length:
                values[leaf_name] = leaf
    logger.debug(
        "F19 literal guard: {} value(s) loaded from the vault (names only: {})",
        len(values),
        ", ".join(sorted(values)),
    )
    return LiteralGuard(values, available=True)


def _leaves(name: str, value):
    """Flatten a vault entry. `MATTERMOST_CREDS` holds a JSON object with
    a url and a token; the token must be guarded even though its parent
    entry is not itself a string."""
    if isinstance(value, str):
        try:
            parsed = json.loads(value)
        except (ValueError, TypeError):
            yield name, value
            return
        if isinstance(parsed, dict):
            for k, v in parsed.items():
                yield from _leaves(f"{name}.{k}", v)
            return
        yield name, value
        return
    if isinstance(value, dict):
        for k, v in value.items():
            yield from _leaves(f"{name}.{k}", v)


def reset_cache() -> None:
    """Test seam. Production never calls this."""
    load_literals.cache_clear()





# ---------------------------------------------------------------------
# Named-secret access — the new core's ONE read/write path to the vault
# ---------------------------------------------------------------------
#
# WHY THIS LIVES HERE and not in a module of its own. This file already
# owns `VAULT_FILE` + `MASTER_KEY_ENV` and already decrypts the vault; a
# second module that opened the same file with the same Fernet would be
# the duplicate implementation the one-path rule kills on sight. The F19
# guard above READS every value; `email-auth` needs to read three by name
# and write two. Same file, same key, same rules — so, same module.
#
# This is the first WRITE the new core makes to the vault. The old tree's
# `VaultManager._save_vault` is the shape being matched (Fernet over a
# JSON object, whole file rewritten); it is deliberately NOT imported —
# strangler rule — and this version writes ATOMICALLY, which the old one
# does not: a truncated `.cobalt_vault` is every credential at once.


class VaultAccessError(RuntimeError):
    """The vault could not be read or written. NEVER carries material."""


def _unlock() -> tuple[str, dict]:
    """(master key, decrypted vault). Raises rather than returning empty:
    a caller asking for a named secret is not served by a silent {}."""
    key = os.getenv(MASTER_KEY_ENV)
    if not key:
        raise VaultAccessError(
            f"{MASTER_KEY_ENV} is not set on this process — the vault cannot be "
            "unlocked. Set it on the job that needs the credential."
        )
    if not VAULT_FILE.exists():
        raise VaultAccessError(f"vault file {VAULT_FILE} does not exist.")
    try:
        from cryptography.fernet import Fernet

        return key, json.loads(Fernet(key.encode()).decrypt(VAULT_FILE.read_bytes()).decode())
    except Exception as e:  # noqa: BLE001 - the KIND matters; the text can echo material
        raise VaultAccessError(
            f"vault could not be opened ({type(e).__name__}). The exception text is "
            "deliberately omitted — a decryption error can echo the material back."
        ) from None


def read_secret(name: str) -> Optional[str]:
    """One named secret, or None if it is absent. Never logged."""
    _, data = _unlock()
    value = data.get(name)
    return value if isinstance(value, str) else None


def has_secret(name: str) -> bool:
    """Presence only — the answer a heartbeat probe is allowed to have."""
    _, data = _unlock()
    return isinstance(data.get(name), str) and bool(data[name])


def put_secret(name: str, value: str) -> None:
    """Write one named secret. Atomic, and the value never leaves memory.

    ATOMIC BY TEMP-FILE + RENAME, for the reason `VaultWriter` is: a
    process killed mid-`write_bytes` on this file does not lose one
    secret, it loses all fifteen. `os.replace` on the same filesystem is
    atomic, so the file on disk is always a complete vault — the old one
    or the new one, never a prefix of either.

    The literal guard's cache is cleared afterwards so the newly stored
    value is enrolled in F19 immediately, in this same process, rather
    than at the next restart. That is what makes a freshly minted refresh
    token unleakable by the very command that minted it.
    """
    if not isinstance(value, str) or not value:
        raise VaultAccessError(f"refusing to store an empty secret under {name!r}.")
    key, data = _unlock()
    data[name] = value

    from cryptography.fernet import Fernet

    payload = Fernet(key.encode()).encrypt(json.dumps(data).encode())
    tmp = VAULT_FILE.with_suffix(VAULT_FILE.suffix + f".tmp.{os.getpid()}")
    try:
        tmp.write_bytes(payload)
        os.chmod(tmp, 0o600)
        os.replace(tmp, VAULT_FILE)
    finally:
        if tmp.exists():
            tmp.unlink()
    reset_cache()
    logger.info("vault: secret {!r} stored ({} bytes, value never logged).", name, len(value))


def secret_names() -> list[str]:
    """Every key in the vault. NAMES only — this is what a report or a
    probe may see, and the vault has no other public listing."""
    _, data = _unlock()
    return sorted(data)


__all__ = [
    "MASTER_KEY_ENV",
    "VAULT_FILE",
    "LiteralGuard",
    "VaultAccessError",
    "has_secret",
    "load_literals",
    "put_secret",
    "read_secret",
    "reset_cache",
    "secret_names",
]
