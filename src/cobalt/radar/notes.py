"""Single-read parser and user-side mirror for radar source notes."""

from __future__ import annotations

import hashlib
import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import ValidationError

from cobalt.session import session_clock
from cobalt.session.clock import now_utc
from cobalt.session.models import Session
from cobalt.settings.store import TraderSettingsStore

from .config import RadarConfig, load_config
from .models import ExcludeBlock, ListBlock, PoolBlock, ScreenBlock

FENCE_RE = re.compile(rb"```yaml[ \t]*\r?\n(.*?)\r?\n```", re.DOTALL)


class RadarNoteError(RuntimeError):
    """A note or one of its fenced units is missing/invalid."""


@dataclass(frozen=True)
class ParsedBlock:
    key: str
    block: ScreenBlock | PoolBlock | ListBlock | ExcludeBlock
    sha256: str


@dataclass
class ParsedNote:
    path: Path
    kind: Literal["screens", "lists"]
    note_sha256: str | None = None
    blocks: list[ParsedBlock] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    missing: bool = False

    @property
    def ok(self) -> bool:
        return not self.missing and not self.errors

    def by_key(self) -> dict[str, ParsedBlock]:
        return {block.key: block for block in self.blocks}


@dataclass
class ParsedSources:
    screens: ParsedNote
    lists: ParsedNote
    pool: PoolBlock | None
    pool_error: str | None = None
    planned_rpm: float | None = None

    @property
    def frozen(self) -> bool:
        return self.pool is None or self.pool_error is not None


def _failure(kind: str, index: int, error: Exception) -> str:
    return f"{kind} block {index}: {error}"


def parse_note(path: Path, kind: Literal["screens", "lists"]) -> ParsedNote:
    """Read bytes exactly once and parse every yaml fence; none are skipped."""
    result = ParsedNote(path=path, kind=kind)
    try:
        payload = path.read_bytes()
    except FileNotFoundError:
        result.missing = True
        result.errors.append(f"{path}: missing")
        return result
    except OSError as e:
        result.errors.append(f"{path}: unreadable: {e}")
        return result
    result.note_sha256 = hashlib.sha256(payload).hexdigest()

    for index, match in enumerate(FENCE_RE.finditer(payload), start=1):
        body = match.group(1)
        digest = hashlib.sha256(body).hexdigest()
        try:
            raw = yaml.safe_load(body)
            if not isinstance(raw, dict):
                raise ValueError("fenced YAML must be a mapping")
            block_kind = raw.get("kind")
            if kind == "screens":
                if block_kind is None:
                    model = ScreenBlock(**raw)
                    key = f"screen.{model.screen}"
                elif block_kind == "pool":
                    model = PoolBlock(**raw)
                    key = "pool"
                else:
                    raise ValueError(f"unknown or wrong-note kind {block_kind!r}")
            else:
                if block_kind is None:
                    model = ListBlock(**raw)
                    key = f"list.{model.list}"
                elif block_kind == "exclude":
                    model = ExcludeBlock(**raw)
                    key = "exclude"
                else:
                    raise ValueError(f"unknown or wrong-note kind {block_kind!r}")
            if key in {item.key for item in result.blocks}:
                raise ValueError(f"duplicate block key {key!r}")
            result.blocks.append(ParsedBlock(key, model, digest))
        except (yaml.YAMLError, ValidationError, ValueError) as e:
            result.errors.append(_failure(kind, index, e))

    if kind == "screens":
        pools = [item for item in result.blocks if item.key == "pool"]
        if len(pools) != 1:
            result.errors.append(f"screens note: expected exactly one pool block, found {len(pools)}")
        elif not result.errors:
            screen_keys = {
                item.block.screen for item in result.blocks if isinstance(item.block, ScreenBlock)
            }
            unknown = sorted(set(pools[0].block.overrides) - screen_keys)
            if unknown:
                result.errors.append(f"pool block: overrides name unknown screen key(s) {unknown}")
    else:
        excludes = [item for item in result.blocks if item.key == "exclude"]
        if len(excludes) > 1:
            result.errors.append(f"lists note: expected at most one exclude block, found {len(excludes)}")
        defaults = [
            item for item in result.blocks
            if isinstance(item.block, ListBlock) and item.block.backfill_default
        ]
        if len(defaults) != 1:
            result.errors.append(
                f"lists note: expected exactly one backfill_default list, found {len(defaults)}"
            )
    return result


def load_sources(
    screens_path: Path,
    lists_path: Path,
    *,
    scan_interval: int,
    poll_interval: int,
    finviz_max_rpm: int | None,
    list_chunk_size: int,
) -> ParsedSources:
    screens = parse_note(screens_path, "screens")
    lists = parse_note(lists_path, "lists")
    pool_item = next((item for item in screens.blocks if item.key == "pool"), None)
    pool = pool_item.block if pool_item and isinstance(pool_item.block, PoolBlock) else None
    result = ParsedSources(screens=screens, lists=lists, pool=pool)
    if not screens.ok:
        result.pool_error = "; ".join(screens.errors)
        return result
    if pool is None:
        result.pool_error = "pool block missing"
        return result
    if not lists.ok:
        # A list failure degrades that source, but a valid pool still governs.
        return result
    if finviz_max_rpm is None:
        result.pool_error = "radar.finviz_max_rpm is unmeasured"
        return result
    active_screens = sum(
        isinstance(item.block, ScreenBlock) and item.block.enabled for item in screens.blocks
    )
    list_requests = sum(
        math.ceil(len(item.block.tickers) / list_chunk_size)
        for item in lists.blocks
        if isinstance(item.block, ListBlock) and item.block.enabled and item.block.radar
    )
    planned = pool.cap * 60 / poll_interval + (active_screens + list_requests) * 60 / scan_interval
    result.planned_rpm = planned
    if planned > finviz_max_rpm:
        result.pool_error = (
            f"pool budget exceeded: planned_rpm={planned:.2f}, "
            f"finviz_max_rpm={finviz_max_rpm}, cap={pool.cap}, "
            f"active_screens={active_screens}, list_chunks={list_requests}"
        )
    return result


def configured_sources(config: RadarConfig | None = None) -> ParsedSources:
    from cobalt.taxonomy.loader import load_tunables
    from cobalt.vault import resolve_vault_path

    cfg = config or load_config()
    values = load_tunables().by_key
    vault = resolve_vault_path()
    rpm = values["radar.finviz_max_rpm"].value
    return load_sources(
        vault / cfg.notes.screens,
        vault / cfg.notes.lists,
        scan_interval=int(values["radar.scan_interval"].value),
        poll_interval=int(values["radar.poll_interval"].value),
        finviz_max_rpm=None if rpm is None else int(rpm),
        list_chunk_size=cfg.list_chunk_size,
    )


def _mirror_rows(parsed: ParsedSources, before: dict[str, Any]) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for note in (parsed.screens, parsed.lists):
        note_key = f"radar.note.{note.kind}"
        note_status = "missing" if note.missing else ("parse_failed" if note.errors else "ok")
        rows[note_key] = {
            "block": None,
            "block_sha256": None,
            "note_sha256": note.note_sha256,
            "status": note_status,
            "error": "; ".join(note.errors) or None,
        }
        for item in note.blocks:
            key = f"radar.{item.key}"
            status = "ok"
            error = None
            if item.key == "pool" and parsed.pool_error:
                status, error = "parse_failed", parsed.pool_error
            rows[key] = {
                "block": item.block.model_dump(mode="json"),
                "block_sha256": item.sha256,
                "note_sha256": note.note_sha256,
                "status": status,
                "error": error,
            }
    current_keys = set(rows)
    for key, old in before.items():
        if key.startswith("radar.") and key not in current_keys:
            rows[key] = {
                "block": None,
                "block_sha256": None,
                "note_sha256": None,
                "status": "removed",
                "error": None,
            }
    return rows


def mirror_sources(
    parsed: ParsedSources,
    *,
    store: TraderSettingsStore | None = None,
    before_commit=None,
    now=None,
) -> dict[str, str]:
    instant = now or now_utc()
    if session_clock().session(instant) is Session.MARKET_RESET:
        raise RadarNoteError("radar mirror refused in market_reset before opening a transaction")
    target = store or TraderSettingsStore()
    before = target.values()
    if all(
        isinstance(before.get(f"radar.note.{note.kind}"), dict)
        and before[f"radar.note.{note.kind}"].get("note_sha256") == note.note_sha256
        for note in (parsed.screens, parsed.lists)
    ):
        return {
            f"radar.note.{note.kind}": "unchanged"
            for note in (parsed.screens, parsed.lists)
        }
    rows = _mirror_rows(parsed, before)
    note_hash = parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"
    return target.put(
        rows,
        source=f"vault:radar-notes@{note_hash[:12]}",
        before_commit=before_commit,
    )


__all__ = [
    "ParsedBlock", "ParsedNote", "ParsedSources", "RadarNoteError",
    "configured_sources", "load_sources", "mirror_sources", "parse_note",
]
