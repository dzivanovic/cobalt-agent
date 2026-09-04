"""Vault path RESOLUTION for the prefill engine — no longer a writer.

Renamed in role (not in file, to keep the diff honest) on 2026-09-03 by
LAW L28: `write_new`, `append_block` and `overwrite` are DELETED. They
were three separate ways to put bytes into a vault file, which is
exactly the shape the law abolishes — there is now one, and it is
`cobalt.vaultwrite.VaultWriter`. What remains here is the path work
daily.py / drc.py / trade_note.py still need: resolve a vault-relative
target through cobalt.vault's ONE resolver, apply the shared "outside
the repo" gate, and read a file if it exists.

Directory creation is still refused — folder policy is a Vault Session
decision, not something Cobalt improvises.
"""

from pathlib import Path
from typing import Optional

from cobalt.vault import VaultConfigError, VaultWriteRefused, assert_within_vault, resolve_vault_path


class VaultWriteError(RuntimeError):
    """Write refused — safety gate failed or target directory missing."""


def resolve_target(vault_relative_dir: str, filename: str) -> Path:
    try:
        vault_root = resolve_vault_path()
    except VaultConfigError as e:
        raise VaultWriteError(f"Vault path unresolved: {e}") from e
    path = vault_root / vault_relative_dir / filename
    if not path.parent.is_dir():
        raise VaultWriteError(
            f"Target directory missing: {path.parent} — refusing to create "
            "vault structure (folder policy is a Vault Session decision)."
        )
    try:
        assert_within_vault(path)
    except VaultWriteRefused as e:
        raise VaultWriteError(str(e)) from e
    return path


def resolve_dir(vault_relative_dir: str) -> Path:
    """Resolve a vault-relative directory for read-only use (e.g. listing
    trade notes to match against cards) — no existence/gate check beyond
    resolving the vault root itself; callers that list its contents
    already tolerate a missing directory (empty listing)."""
    try:
        vault_root = resolve_vault_path()
    except VaultConfigError as e:
        raise VaultWriteError(f"Vault path unresolved: {e}") from e
    return vault_root / vault_relative_dir


def read_if_exists(path: Path) -> Optional[str]:
    return path.read_text(encoding="utf-8") if path.exists() else None
