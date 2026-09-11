"""Fail-loud Bar Archiver target loading from the Radar Lists note.

The note is read and validated once at the start of each run. This module
never writes or mirrors it, and there is no YAML or built-in target fallback.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from cobalt.radar.notes import ParsedNote, parse_note
from cobalt.radar.sources import archive_targets, backfill_targets

from .collector import scrub
from .models import Interval

REPO_ROOT = Path(__file__).resolve().parents[3]


class ConfigError(RuntimeError):
    """Lists-note resolution or validation failed — crash loudly."""

    def __init__(self, message: object):
        super().__init__(scrub(str(message)))


@dataclass(frozen=True)
class ArchiverConfig:
    """A validated, single-read Lists note with runner-facing target methods."""

    note: ParsedNote

    def archive_targets(self) -> list[tuple[str, Interval]]:
        return archive_targets(self.note)

    def backfill_targets(self, ticker: str) -> list[tuple[str, Interval]]:
        return backfill_targets(self.note, ticker)


def _configured_lists_path() -> Path:
    from cobalt.radar.config import load_config as load_radar_config
    from cobalt.vault import resolve_vault_path

    return resolve_vault_path() / load_radar_config().notes.lists


def load_config(note_path: Path | None = None) -> ArchiverConfig:
    """Read and validate the configured Lists note without any side effects."""

    try:
        path = note_path if note_path is not None else _configured_lists_path()
        parsed = parse_note(path, "lists")
        # Exercise the exact Stage 1 derivation paths now so a malformed or
        # incomplete note fails before the runner opens its store or token.
        archive_targets(parsed)
        backfill_targets(parsed, "VALIDATION")
    except (RuntimeError, TypeError, ValueError) as error:
        raise ConfigError(error) from error
    return ArchiverConfig(parsed)


__all__ = ["ArchiverConfig", "ConfigError", "load_config"]
