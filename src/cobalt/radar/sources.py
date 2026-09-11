"""Archive/backfill target derivation from the Lists note."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field

from cobalt.archiver.collector import scrub
from cobalt.archiver.models import Interval

from .config import load_config
from .models import ListBlock
from .notes import ParsedNote, RadarNoteError, parse_note


class LegacyTier(BaseModel):
    """Retired watchlists.yaml tier shape, retained only for migration proof."""

    model_config = ConfigDict(extra="forbid")

    description: str = Field(min_length=1)
    intervals: list[Interval]
    tickers: list[str]


class LegacyWatchlistsConfig(BaseModel):
    """Historical YAML schema used by propose/diff, never by the archiver."""

    model_config = ConfigDict(extra="forbid")

    tier_a: LegacyTier
    tier_b: LegacyTier
    tier_c: LegacyTier

    def archive_targets(self) -> list[tuple[str, Interval]]:
        return [
            (ticker, interval)
            for tier in (self.tier_a, self.tier_b)
            for ticker in tier.tickers
            for interval in tier.intervals
        ]

    def backfill_targets(self, ticker: str) -> list[tuple[str, Interval]]:
        return [(ticker, interval) for interval in self.tier_a.intervals]


def _parsed(note: Path | ParsedNote) -> ParsedNote:
    parsed = note if isinstance(note, ParsedNote) else parse_note(Path(note), "lists")
    if not parsed.ok:
        raise RadarNoteError(
            scrub(f"{parsed.path}: Lists note invalid: {'; '.join(parsed.errors)}")
        )
    return parsed


def archive_targets(note: Path | ParsedNote) -> list[tuple[str, Interval]]:
    targets = {
        (ticker, interval)
        for item in _parsed(note).blocks
        if isinstance(item.block, ListBlock) and item.block.enabled
        for ticker in item.block.tickers
        for interval in item.block.archive
    }
    return sorted(targets, key=lambda item: (item[0], item[1].value))


def backfill_targets(note: Path | ParsedNote, ticker: str) -> list[tuple[str, Interval]]:
    blocks = [
        item.block for item in _parsed(note).blocks
        if isinstance(item.block, ListBlock) and item.block.backfill_default and item.block.enabled
    ]
    if len(blocks) != 1:
        raise RadarNoteError(
            scrub(f"Lists note needs exactly one enabled backfill_default; found {len(blocks)}")
        )
    return [(ticker.strip().upper(), interval) for interval in blocks[0].archive]


def _yaml_at_revision(revision: str):
    proc = subprocess.run(
        ["git", "show", f"{revision}:configs/cobalt/watchlists.yaml"],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode:
        raise RadarNoteError(
            scrub(f"git show watchlists at {revision} failed: {proc.stderr.strip()}")
        )
    try:
        return LegacyWatchlistsConfig.model_validate(yaml.safe_load(proc.stdout))
    except (ValueError, yaml.YAMLError) as error:
        raise RadarNoteError(scrub(f"watchlists at {revision} invalid: {error}")) from error


def archiver_diff(note: Path | ParsedNote, revision: str) -> list[str]:
    parsed = _parsed(note)
    old = _yaml_at_revision(revision)
    lines: list[str] = []
    note_archive = {(t, i.value) for t, i in archive_targets(parsed)}
    yaml_archive = {(t, i.value) for t, i in old.archive_targets()}
    for value in sorted(note_archive - yaml_archive):
        lines.append(f"+ archive {value[0]} {value[1]}")
    for value in sorted(yaml_archive - note_archive):
        lines.append(f"- archive {value[0]} {value[1]}")
    sample = next((t for t, _ in sorted(yaml_archive)), "EXAMPLE")
    note_backfill = {(t, i.value) for t, i in backfill_targets(parsed, sample)}
    yaml_backfill = {(t, i.value) for t, i in old.backfill_targets(sample)}
    for value in sorted(note_backfill - yaml_backfill):
        lines.append(f"+ backfill {value[0]} {value[1]}")
    for value in sorted(yaml_backfill - note_backfill):
        lines.append(f"- backfill {value[0]} {value[1]}")
    return lines


def command(args) -> None:
    from cobalt.vault import resolve_vault_path

    cfg = load_config()
    path = resolve_vault_path() / cfg.notes.lists
    parsed = _parsed(path)
    payload = {
        "note": str(path),
        "note_sha256": parsed.note_sha256,
        "archive_targets": [(t, i.value) for t, i in archive_targets(parsed)],
    }
    if args.archiver_diff:
        lines = archiver_diff(parsed, args.yaml_rev)
        if lines:
            print("\n".join(lines))
        else:
            print("archiver diff: empty")
    elif args.json:
        print(json.dumps(payload, sort_keys=True))
    else:
        print(f"{path}: {len(parsed.blocks)} blocks ok")
        print(f"archive targets: {len(payload['archive_targets'])}")


__all__ = [
    "LegacyWatchlistsConfig", "archive_targets", "archiver_diff",
    "backfill_targets",
]
