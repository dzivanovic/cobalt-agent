"""Shared vault-write plumbing for the prefill engine (one-path rule —
daily.py, trade_note.py, and drc.py all go through this, not three
copies of the same resolve/gate/write logic).

Every write passes through cobalt.vault's ONE resolver and shared
"outside the repo" safety gate before touching disk. Directory creation
is refused, same as aset/daily_note.py — folder policy is a Vault
Session decision, not something Cobalt improvises.
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


def write_new(path: Path, content: str) -> None:
    """Write a brand-new file. Refuses to clobber an existing one — the
    caller (e.g. daily.py) must already have branched on read_if_exists()
    being None; this is a second, cheap guard against a race."""
    if path.exists():
        raise VaultWriteError(f"REFUSED: {path} already exists — use append_block, not write_new.")
    path.write_text(content, encoding="utf-8")


def append_block(path: Path, content: str) -> None:
    """Append-only forever: existing content is never read for mutation,
    only for the caller's own idempotency-marker check beforehand."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(content)


def overwrite(path: Path, content: str) -> None:
    """Replace a file's full content. Scoped to ONE legitimate case in
    this package: trade_note.py refreshing its own Cobalt-owned
    frontmatter keys on an idempotent re-run, after merging them onto
    whatever the file already had (Dejan's manual edits preserved by the
    caller before calling this, never by this function)."""
    path.write_text(content, encoding="utf-8")
