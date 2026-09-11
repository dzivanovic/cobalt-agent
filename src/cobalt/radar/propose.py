"""Deterministic radar-note proposals and artifact-exact HITL apply."""

from __future__ import annotations

import asyncio
import csv
import difflib
import hashlib
import io
import json
import re
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING
from urllib.parse import parse_qs, urlparse

import yaml

from cobalt.archiver.collector import finviz_get, resolve_token, scrub
from cobalt.session import clock as session_clock_module
from cobalt.session.models import Session
from cobalt.vaultwrite import (
    AT_END,
    VaultWriteStore,
    VaultWriter,
    assert_write_target,
)

from .config import load_config
from .models import PoolBlock, ScreenBlock

if TYPE_CHECKING:
    from cobalt.archiver.config import WatchlistsConfig


class ProposalRefused(RuntimeError):
    """Proposal/apply precondition failed before any write."""

    def __init__(self, message: object):
        super().__init__(scrub(str(message)))


HEADING_RE = re.compile(r"^##\s+(.+?)\s+—\s+(.+?)\s*$", re.MULTILINE)


def canonical_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_sha256(value: dict) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _slug(value: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value.lower())).strip("_")


def derive_screens(text: str) -> tuple[list[ScreenBlock], list[dict[str, str | None]]]:
    matches = list(HEADING_RE.finditer(text))
    if not matches:
        raise ProposalRefused("Screens note has no '## … — screen name' sections")
    screens: list[ScreenBlock] = []
    evidence: list[dict[str, str]] = []
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end():end]

        def line(label: str) -> str:
            found = re.search(rf"^- (?:\*\*)?{re.escape(label)}(?:\*\*)?:\s*(.+?)\s*$", section, re.MULTILINE)
            if not found:
                raise ProposalRefused(f"{match.group(2)}: missing prose field {label}")
            return found.group(0)

        export_line, filters_line, sort_line, columns_line = (
            line("Export call (derived)"), line("Filters"), line("Sort"), line("Columns")
        )
        export_raw = export_line.split(":", 1)[1].strip().strip("`")
        query = parse_qs(urlparse(export_raw).query)
        if not query.get("f"):
            raise ProposalRefused(f"{match.group(2)}: Export line has no f parameter")
        f_value = query["f"][0]
        prose_filters = re.findall(r"`([a-z0-9_.]+)`", filters_line)
        if prose_filters != f_value.split(","):
            raise ProposalRefused(
                f"{match.group(2)}: f mismatch between Export and Filters lines"
            )
        sort_value = sort_line.split(":", 1)[1].strip().strip("`")
        if query.get("o", [None])[0] != sort_value:
            raise ProposalRefused(f"{match.group(2)}: sort mismatch between Export and Sort lines")
        columns_raw = columns_line.split(":", 1)[1].strip().strip("`")
        if query.get("c", [None])[0] != columns_raw:
            raise ProposalRefused(f"{match.group(2)}: columns mismatch between Export and Columns lines")
        if columns_raw == "0-150":
            columns = list(range(151))
        else:
            columns = [int(value) for value in columns_raw.split(",")]
        active = re.search(r"^- Active:\s*`(\d\d:\d\d)`\s+to\s+`(\d\d:\d\d)`", section, re.MULTILINE)
        if active is None:
            from cobalt.taxonomy.loader import load_tunables

            tunables = load_tunables().by_key
            active_from = tunables["session.premarket_open"].value
            active_to = tunables["session.aftermarket_close"].value
            active_line = None
        else:
            active_from, active_to = active.group(1), active.group(2)
            active_line = active.group(0)
        block = ScreenBlock(
            screen=_slug(match.group(2)), f=f_value, sort=sort_value, columns=columns,
            active_from=active_from, active_to=active_to, enabled=True,
        )
        screens.append(block)
        evidence.append(
            {"heading": match.group(0), "export": export_line, "filters": filters_line,
             "sort": sort_line, "columns": columns_line,
             "active": active_line}
        )
    return screens, evidence


def _dump_field(name: str, value: object) -> str:
    return yaml.safe_dump({name: value}, sort_keys=False).strip()


def _render_screen(block: ScreenBlock, evidence: dict[str, str | None]) -> str:
    values = block.model_dump(exclude_none=True)
    fields = [
        ("screen", evidence["heading"]),
        ("f", evidence["export"]),
        ("sort", evidence["sort"]),
        ("columns", evidence["columns"]),
        ("active_from", evidence["active"]),
        ("active_to", evidence["active"]),
    ]
    lines = ["```yaml"]
    for name, source in fields:
        if source is None:
            lines.append("# PROPOSED — no window stated in prose")
        else:
            lines.append(f"# from: {json.dumps(source)}")
        lines.append(_dump_field(name, values.pop(name)))
    lines.append("# PROPOSED — enabled for the generated radar block")
    lines.append(_dump_field("enabled", values.pop("enabled")))
    for name, value in values.items():
        lines.append("# PROPOSED — derived from the recorded comparison")
        lines.append(_dump_field(name, value))
    lines.append("```")
    return "\n".join(lines)


def _print_insertion_diff(target: Path, original: str, units: list[dict]) -> None:
    addition = "\n\n".join(unit["body"] for unit in units)
    separator = "" if not original or original.endswith("\n") else "\n"
    proposed = original + separator + addition + "\n"
    diff = difflib.unified_diff(
        original.splitlines(keepends=True),
        proposed.splitlines(keepends=True),
        fromfile=str(target),
        tofile=str(target),
    )
    print("".join(diff), end="")


def render_lists(config: "WatchlistsConfig") -> str:
    blocks = []
    for key in ("tier_a", "tier_b", "tier_c"):
        tier = getattr(config, key)
        block = {
            "list": key,
            "description": tier.description,
            "tickers": tier.tickers,
            "radar": True,
            "archive": [item.value for item in tier.intervals],
            "backfill_default": key == "tier_a",
            "enabled": True,
        }
        blocks.append("```yaml\n" + yaml.safe_dump(block, sort_keys=False).strip() + "\n```")
    return (
        "# Radar Lists\n\n# PROPOSED — derived from the committed tier rules.\n\n"
        + "\n\n".join(blocks) + "\n"
    )


def build_artifact(kind: str, target: Path, target_sha: str, inputs: dict, units: list[dict]) -> dict:
    return {
        "version": 1,
        "kind": kind,
        "target_note": str(target),
        "target_note_sha256": target_sha,
        "inputs": inputs,
        "units": units,
    }


def write_artifact(artifact: dict, *, directory: Path = Path("data/radar-proposals")) -> tuple[Path, str]:
    digest = artifact_sha256(artifact)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{artifact['kind']}-{digest}.json"
    path.write_bytes(canonical_bytes(artifact) + b"\n")
    return path, digest


async def _ft_diff(block: ScreenBlock, token: str) -> dict:
    base = {"v": 152, "f": block.f, "o": block.sort, "c": "0"}
    sets = []
    for ft in (None, 4):
        params = dict(base)
        if ft is not None:
            params["ft"] = ft
        metrics = []
        response = await finviz_get("/export/screener", params, token, on_metrics=metrics.append)
        if not metrics:
            raise ProposalRefused(f"{block.screen}: comparison transport emitted no metrics")
        if metrics[-1].redirect_statuses:
            raise ProposalRefused(
                f"{block.screen}: comparison redirected {list(metrics[-1].redirect_statuses)}"
            )
        rows = list(csv.DictReader(io.StringIO(response.text)))
        sets.append({row.get("Ticker", "") for row in rows if row.get("Ticker")})
    return {"without": len(sets[0]), "with_4": len(sets[1]), "symmetric_difference": sorted(sets[0] ^ sets[1])}


def screens_propose(args) -> None:
    from cobalt.vault import resolve_vault_path

    cfg = load_config()
    target = resolve_vault_path() / cfg.notes.screens
    target_raw = target.read_bytes()
    text = target_raw.decode("utf-8")
    screens, evidence = derive_screens(text)
    pool_raw = Path(args.pool_block).read_bytes()
    try:
        pool = PoolBlock.model_validate(yaml.safe_load(pool_raw))
    except Exception as e:
        raise ProposalRefused(f"invalid pool-block file {args.pool_block}: {e}") from e
    unknown = sorted(set(pool.overrides) - {item.screen for item in screens})
    if unknown:
        raise ProposalRefused(f"pool-block overrides unknown screen(s) {unknown}")
    comparisons = []
    if args.ft_compare:
        token = asyncio.run(resolve_token())
        for index, block in enumerate(screens):
            result = asyncio.run(_ft_diff(block, token))
            comparisons.append(result)
            if result["symmetric_difference"]:
                screens[index] = block.model_copy(update={"ft": 4})
    units = [
        {"section": evidence[index]["heading"][3:], "unit_id": f"radar-screen-{block.screen}", "placement": "at_end", "body": _render_screen(block, evidence[index])}
        for index, block in enumerate(screens)
    ]
    units.append({"section": evidence[-1]["heading"][3:], "unit_id": "radar-pool", "placement": "at_end", "body": "```yaml\n" + yaml.safe_dump(pool.model_dump(mode="json"), sort_keys=False).strip() + "\n```"})
    artifact = build_artifact(
        "screens", target, hashlib.sha256(target_raw).hexdigest(),
        {"target_text": text, "pool_block": pool_raw.decode(), "ft_comparisons": comparisons}, units,
    )
    path, digest = write_artifact(artifact)
    print("\n\n".join(unit["body"] for unit in units))
    _print_insertion_diff(target, text, units)
    print(f"artifact: {path}\nsha256: {digest}")


def lists_propose(args) -> None:
    from cobalt.vault import resolve_vault_path
    from cobalt.archiver.config import CONFIG_PATH as watchlists_path
    from cobalt.archiver.config import WatchlistsConfig

    raw = watchlists_path.read_bytes()
    config = WatchlistsConfig.model_validate(yaml.safe_load(raw))
    target = resolve_vault_path() / load_config().notes.lists
    if target.exists():
        raise ProposalRefused(f"Lists target already exists: {target}")
    note = render_lists(config)
    blob = subprocess.run(["git", "hash-object", str(watchlists_path)], capture_output=True, text=True, check=True).stdout.strip()
    artifact = build_artifact(
        "lists", target, "absent" if not target.exists() else hashlib.sha256(target.read_bytes()).hexdigest(),
        {"watchlists_yaml": raw.decode(), "watchlists_git_blob": blob},
        [{"section": None, "unit_id": None, "placement": "create_if_absent", "body": note}],
    )
    path, digest = write_artifact(artifact)
    print(note)
    _print_insertion_diff(target, "", artifact["units"])
    print(f"artifact: {path}\nsha256: {digest}")


def apply(args) -> None:
    path = Path(args.proposal)
    artifact = json.loads(path.read_text(encoding="utf-8"))
    digest = artifact_sha256(artifact)
    if digest != args.sha256:
        raise ProposalRefused(f"artifact sha256 changed: expected {args.sha256}, got {digest}")
    expected_kind = getattr(args, "proposal_kind", artifact.get("kind"))
    if artifact.get("kind") != expected_kind:
        raise ProposalRefused(
            f"proposal kind mismatch: command is {expected_kind}, artifact is {artifact.get('kind')}"
        )
    target = Path(artifact["target_note"])
    if hasattr(args, "proposal_kind"):
        from cobalt.vault import resolve_vault_path

        cfg = load_config()
        relative = cfg.notes.screens if expected_kind == "screens" else cfg.notes.lists
        expected_target = resolve_vault_path() / relative
        if target != expected_target:
            raise ProposalRefused(
                f"proposal target mismatch: expected {expected_target}, got {target}"
            )
    current = hashlib.sha256(target.read_bytes()).hexdigest() if target.exists() else "absent"
    if current != artifact["target_note_sha256"]:
        raise ProposalRefused(
            f"target note sha256 changed: expected {artifact['target_note_sha256']}, got {current}"
        )
    if artifact["kind"] == "screens" and "```yaml" in target.read_text(encoding="utf-8"):
        raise ProposalRefused("target Screens note already contains fenced YAML blocks")
    if not str(args.hitl).strip():
        raise ProposalRefused("apply requires a non-empty HITL token")
    if session_clock_module.current_session() is Session.MARKET_RESET:
        raise ProposalRefused("apply refused during market_reset")
    try:
        assert_write_target(target)
    except Exception as e:
        raise ProposalRefused(scrub(str(e))) from e
    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter(f"radar.{artifact['kind']}.apply", store=store, run_id=args.hitl)
    results = []
    if artifact["kind"] == "lists":
        results.append(writer.create_if_absent(target, artifact["units"][0]["body"]))
    else:
        for unit in artifact["units"]:
            results.append(writer.upsert_unit(target, unit["section"], unit["unit_id"], unit["body"], placement=AT_END))
    for result in results:
        if result.write_id is None:
            raise ProposalRefused(f"apply did not write {result.path}: {result.action}")
        print(f"write_id {result.write_id}: cobalt vault restore --write-id {result.write_id}")


__all__ = [
    "ProposalRefused", "apply", "artifact_sha256", "build_artifact",
    "derive_screens", "render_lists", "write_artifact",
]
