"""The ONE vault write path (LAW L28). See writer.py's docstring."""

from .markers import MarkerError, legacy_slot_present
from .merge import Override, merge3, merge_body
from .store import VaultWriteStore, sha256_text
from .writer import (
    AT_END,
    NoteChangedOnDisk,
    Placement,
    VaultWriteError,
    VaultWriter,
    WriteResult,
    after_pattern,
    assert_write_target,
    wrap_span,
)

__all__ = [
    "AT_END",
    "MarkerError",
    "NoteChangedOnDisk",
    "Override",
    "Placement",
    "VaultWriteError",
    "VaultWriteStore",
    "VaultWriter",
    "WriteResult",
    "after_pattern",
    "assert_write_target",
    "legacy_slot_present",
    "merge3",
    "merge_body",
    "sha256_text",
    "wrap_span",
]
