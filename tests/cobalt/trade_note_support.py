"""Shared helpers for the S3 C4 trade-note tests (F22, v3 §7).

Every vault write goes to a `tmp_path` vault (L28: the live vault is never
a test target). Offline tests write through the REAL `VaultWriter` with an
in-memory audit store standing in for `vault_writes` (the store's own
contract is proved in test_vaultwrite.py; the pattern is
test_replay_line.py's `MemoryWriteStore`). Constructed values only (L32).
"""

from __future__ import annotations

from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

from cobalt.prefill.config import PrefillPathsConfig

TRADES_DIR = "1 - Trading/2 - Trades"


class MemoryWriteStore:
    """`VaultWriteStore`'s read/write contract, in memory."""

    def __init__(self):
        self.rows: list[dict] = []
        self.overrides: list[dict] = []

    def last_after(self, note, section, unit):
        for row in reversed(self.rows):
            if (row["note"], row["section"], row["unit"]) == (note, section, unit):
                return row["unit_after"]
        return None

    def recent_afters(self, note, section, unit, limit=10):
        hits = [(r["id"], r["unit_after"]) for r in reversed(self.rows)
                if (r["note"], r["section"], r["unit"]) == (note, section, unit)]
        return hits[:limit]

    def get_write(self, write_id):
        return next((r for r in self.rows if r["id"] == write_id), None)

    def purge_expired(self, days=30):
        return 0

    def ensure_schema(self):
        return None

    @contextmanager
    def pending_write(self, *, overrides=None, **row):
        row = {**row, "id": len(self.rows) + 1, "ts": datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)}
        yield row["id"]
        self.rows.append(row)
        self.overrides.extend(overrides or [])


def make_paths() -> PrefillPathsConfig:
    return PrefillPathsConfig(
        trades_dir=TRADES_DIR,
        review_dir="1 - Trading/5 - Review",
        drc_filename_pattern="DRC-%Y-%m-%d.md",
        trade_filename_pattern="Trade-%Y-%m-%d %H-%M-%S -{ticker}.md",
    )


def make_vault(monkeypatch, tmp_path: Path) -> Path:
    """A `tmp_path` vault with the trades folder; the one resolver patched."""
    from cobalt.prefill import vault_writer as vault_writer_module

    vault_root = tmp_path / "vault"
    (vault_root / TRADES_DIR).mkdir(parents=True)
    monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: vault_root)
    return vault_root


def memory_writer(store: MemoryWriteStore | None = None, **kwargs):
    from cobalt.vaultwrite import VaultWriter

    return VaultWriter("prefill.trade_note", store=store or MemoryWriteStore(), **kwargs)
