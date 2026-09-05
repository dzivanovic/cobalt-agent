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


__all__ = ["MASTER_KEY_ENV", "VAULT_FILE", "LiteralGuard", "load_literals", "reset_cache"]
