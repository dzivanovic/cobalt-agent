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
from pydantic import ValidationError

from cobalt.archiver.collector import finviz_get, resolve_token, scrub
from cobalt.session import clock as session_clock_module
from cobalt.session.models import Session
from cobalt.vaultwrite import (
    AT_END,
    VaultWriter,
    VaultWriteStore,
    assert_write_target,
)

from .config import load_config
from .models import ListBlock, PoolBlock, ScreenBlock

if TYPE_CHECKING:
    from .sources import LegacyWatchlistsConfig


class ProposalRefused(RuntimeError):
    """Proposal/apply precondition failed before any write."""

    def __init__(self, message: object):
        super().__init__(scrub(str(message)))


HEADING_RE = re.compile(r"^##\s+(.+?)\s+—\s+(.+?)\s*$", re.MULTILINE)
_SCREEN_ORDINAL_RE = re.compile(r"^(?:Screen\s+)?(?P<number>[1-9][0-9]*)$", re.IGNORECASE)
_BOLD_COLON_INSIDE_RE = re.compile(
    r"^-\s+\*\*(?P<label>[^*]+?):\*\*\s*(?P<value>.*?)\s*$"
)
_BOLD_COLON_OUTSIDE_RE = re.compile(
    r"^-\s+\*\*(?P<label>[^*]+?)\*\*:\s*(?P<value>.*?)\s*$"
)
_BARE_FIELD_RE = re.compile(r"^-\s+(?P<label>[^:]+):\s*(?P<value>.*?)\s*$")
_INLINE_COLUMNS_RE = re.compile(
    r"(?:^|\s+·\s+)(?:\*\*)?columns(?:\s+\(`c=`\))?"
    r"(?::\*\*|\*\*:|:)\s*(?P<value>.*?)(?=\s+·\s+|$)",
    re.IGNORECASE,
)
_TIMING_SUFFIX_RE = re.compile(r"\s+\(after\s+(?P<time>\d\d:\d\d)\)\s*$", re.IGNORECASE)
_INTENT_START_RE = re.compile(r"\b(?:after|from)\s+(?P<time>\d\d:\d\d)\b", re.IGNORECASE)
_SUPPORTED_FIELDS = {"export", "filters", "sort", "columns", "active", "pasted", "intent"}


def canonical_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def artifact_sha256(value: dict) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def _slug(value: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^a-z0-9]+", "_", value.lower())).strip("_")


def _screen_marker_ids(heading_anchor: str, screen_name: str) -> tuple[str, str]:
    """Derive marker identifiers from the heading's durable screen ordinal.

    The display name is editable trader prose and also feeds the radar source
    key, so it cannot identify an L28-owned marker.  Both accepted real shapes
    (``Screen 3`` and the older fixture's ``3``) carry the same ordinal.
    """
    matched = _SCREEN_ORDINAL_RE.fullmatch(heading_anchor.strip())
    if matched is None:
        raise ProposalRefused(
            f"{screen_name}: heading anchor {heading_anchor!r} is not a stable "
            "screen ordinal ('Screen N' or 'N')"
        )
    number = int(matched.group("number"))
    section_id = f"radar-screen-{number}"
    return section_id, f"{section_id}-definition"


def _field_name(label: str) -> str | None:
    normalized = re.sub(r"\s+\(`(?:f|c)=`\)\s*$", "", label.strip(), flags=re.IGNORECASE)
    lowered = normalized.casefold()
    if lowered.startswith("pasted"):
        return "pasted"
    aliases = {
        "export call (derived)": "export",
        "filters": "filters",
        "sort": "sort",
        "columns": "columns",
        "active": "active",
        "intent": "intent",
    }
    return aliases.get(lowered)


def _section_fields(section: str, screen_name: str) -> dict[str, tuple[str, str]]:
    fields: dict[str, tuple[str, str]] = {}
    for source in section.splitlines():
        matched = (
            _BOLD_COLON_INSIDE_RE.match(source)
            or _BOLD_COLON_OUTSIDE_RE.match(source)
            or _BARE_FIELD_RE.match(source)
        )
        if matched is None:
            continue
        name = _field_name(matched.group("label"))
        if name not in _SUPPORTED_FIELDS:
            continue
        if name in fields:
            raise ProposalRefused(f"{screen_name}: duplicate prose field {matched.group('label').strip()}")
        fields[name] = (source, matched.group("value"))
    return fields


def _required_field(
    fields: dict[str, tuple[str, str]], name: str, screen_name: str
) -> tuple[str, str]:
    if name not in fields:
        raise ProposalRefused(f"{screen_name}: missing prose field {name.title()}")
    return fields[name]


def _inline_code(value: str, *, field: str, screen_name: str) -> str:
    values = re.findall(r"`([^`]+)`", value)
    if len(values) != 1:
        raise ProposalRefused(
            f"{screen_name}: {field} needs exactly one inline-code value; found {len(values)}"
        )
    return values[0]


def _query(raw: str, *, field: str, screen_name: str) -> dict[str, list[str]]:
    parsed = parse_qs(urlparse(raw).query, keep_blank_values=True)
    for name in ("f", "o", "c"):
        if len(parsed.get(name, [])) > 1:
            raise ProposalRefused(f"{screen_name}: {field} URL has ambiguous {name} parameters")
    return parsed


def _one(query: dict[str, list[str]], name: str) -> str | None:
    values = query.get(name, [])
    return values[0] if values else None


def _filter_tokens(value: str, *, screen_name: str) -> list[str]:
    chunks = re.findall(r"`([^`]+)`", value)
    tokens = [token.strip() for chunk in chunks for token in chunk.split(",") if token.strip()]
    if not tokens:
        raise ProposalRefused(f"{screen_name}: Filters has no inline-code filter tokens")
    return tokens


def _sort_code(value: str, *, screen_name: str) -> str:
    matched = re.match(r"\s*`(?P<code>-?[a-z0-9_]+)`(?:\s|$)", value)
    if matched is None:
        matched = re.match(r"\s*(?P<code>-?[a-z0-9_]+)(?:\s|$)", value)
    if matched is None:
        raise ProposalRefused(f"{screen_name}: Sort has no leading sort code")
    return matched.group("code")


def _columns(value: str, *, screen_name: str, source: str) -> list[int] | None:
    normalized = value.strip().strip("`")
    if normalized == "<same columns>":
        return None
    if normalized == "0-150":
        return list(range(151))
    if not re.fullmatch(r"\d+(?:,\d+)*", normalized):
        raise ProposalRefused(f"{screen_name}: {source} columns are not a numeric declaration")
    return [int(item) for item in normalized.split(",")]


def _screen_name_and_heading_time(raw_name: str) -> tuple[str, str | None]:
    suffix = _TIMING_SUFFIX_RE.search(raw_name)
    if suffix is None:
        return raw_name, None
    return raw_name[:suffix.start()].rstrip(), suffix.group("time")


def derive_screens(text: str) -> tuple[list[ScreenBlock], list[dict[str, object]]]:
    matches = list(HEADING_RE.finditer(text))
    if not matches:
        raise ProposalRefused("Screens note has no '## … — screen name' sections")
    screens: list[ScreenBlock] = []
    evidence: list[dict[str, object]] = []
    marker_sections: set[str] = set()
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        raw_name = match.group(2)
        section_id, unit_id = _screen_marker_ids(match.group(1), raw_name)
        if section_id in marker_sections:
            raise ProposalRefused(
                f"{raw_name}: duplicate stable screen ordinal {match.group(1)!r} "
                f"produces section id {section_id!r}"
            )
        marker_sections.add(section_id)
        section = text[match.end():end]
        fields = _section_fields(section, raw_name)
        export_line, export_value = _required_field(fields, "export", raw_name)
        filters_line, filters_value = _required_field(fields, "filters", raw_name)
        sort_line, sort_field_value = _required_field(fields, "sort", raw_name)

        export_raw = _inline_code(export_value, field="Export", screen_name=raw_name)
        export_query = _query(export_raw, field="Export", screen_name=raw_name)
        f_value = _one(export_query, "f")
        if not f_value:
            raise ProposalRefused(f"{raw_name}: Export line has no f parameter")
        prose_filters = _filter_tokens(filters_value, screen_name=raw_name)
        if prose_filters != f_value.split(","):
            raise ProposalRefused(f"{raw_name}: f mismatch between Export and Filters lines")

        pasted_line = pasted_query = None
        if "pasted" in fields:
            pasted_line, pasted_value = fields["pasted"]
            pasted_raw = _inline_code(pasted_value, field="Pasted", screen_name=raw_name)
            pasted_query = _query(pasted_raw, field="Pasted", screen_name=raw_name)
            pasted_f = _one(pasted_query, "f")
            if pasted_f is not None and pasted_f != f_value:
                raise ProposalRefused(f"{raw_name}: f mismatch between Export and Pasted URLs")

        sort_value = _sort_code(sort_field_value, screen_name=raw_name)
        for source_name, query in (("Export", export_query), ("Pasted", pasted_query)):
            declared = _one(query, "o") if query is not None else None
            if declared is not None and declared != sort_value:
                raise ProposalRefused(
                    f"{raw_name}: sort mismatch between {source_name} URL and Sort line"
                )

        inline = _INLINE_COLUMNS_RE.search(sort_field_value)
        if inline is not None and "columns" in fields:
            raise ProposalRefused(f"{raw_name}: duplicate prose field Columns")
        if inline is not None:
            columns_line, columns_value = sort_line, inline.group("value")
        elif "columns" in fields:
            columns_line, columns_value = fields["columns"]
        else:
            columns_line = None
            columns_value = None

        declarations: list[tuple[str, list[int], str]] = []
        if columns_value is not None:
            explicit = _columns(columns_value, screen_name=raw_name, source="prose")
            if explicit is not None:
                declarations.append(("prose", explicit, columns_line or sort_line))
        for source_name, query, source_line in (
            ("Export", export_query, export_line),
            ("Pasted", pasted_query, pasted_line),
        ):
            raw_columns = _one(query, "c") if query is not None else None
            if raw_columns is None:
                continue
            parsed_columns = _columns(raw_columns, screen_name=raw_name, source=source_name)
            if parsed_columns is not None:
                declarations.append((source_name, parsed_columns, source_line or ""))
        if not declarations:
            raise ProposalRefused(f"{raw_name}: columns are not resolvable from prose or URLs")
        columns = declarations[0][1]
        disagreement = [name for name, values, _line in declarations if values != columns]
        if disagreement:
            raise ProposalRefused(
                f"{raw_name}: columns mismatch among numeric declarations ({', '.join(disagreement)})"
            )

        display_name, heading_time = _screen_name_and_heading_time(raw_name)
        active_sources: list[str] = []
        if "active" in fields:
            active_line, active_value = fields["active"]
            active = re.fullmatch(
                r"\s*`?(\d\d:\d\d)`?\s+to\s+`?(\d\d:\d\d)`?\s*", active_value
            )
            if active is None:
                raise ProposalRefused(f"{raw_name}: Active must be HH:MM to HH:MM")
            active_from, active_to = active.group(1), active.group(2)
            active_sources = [active_line]
            active_to_sources = [active_line]
        else:
            from cobalt.taxonomy.loader import load_tunables

            tunables = load_tunables().by_key
            starts: list[tuple[str, str]] = []
            if heading_time is not None:
                starts.append((heading_time, match.group(0)))
            if "intent" in fields:
                intent_line, intent_value = fields["intent"]
                starts.extend((item.group("time"), intent_line) for item in _INTENT_START_RE.finditer(intent_value))
            distinct = list(dict.fromkeys(value for value, _source in starts))
            if len(distinct) > 1:
                raise ProposalRefused(f"{raw_name}: conflicting start times {distinct}")
            active_from = distinct[0] if distinct else tunables["session.premarket_open"].value
            active_to = tunables["session.aftermarket_close"].value
            active_sources = list(dict.fromkeys(source for _value, source in starts))
            active_to_sources = []
        try:
            block = ScreenBlock(
                screen=_slug(display_name), f=f_value, sort=sort_value, columns=columns,
                active_from=active_from, active_to=active_to, enabled=True,
            )
        except ValidationError as error:
            raise ProposalRefused(f"{raw_name}: invalid derived screen: {error}") from error
        if block.screen in {item.screen for item in screens}:
            raise ProposalRefused(f"{raw_name}: duplicate screen key {block.screen!r}")
        screens.append(block)
        evidence.append(
            {
                "heading": match.group(0),
                "section_id": section_id,
                "unit_id": unit_id,
                "export": export_line,
                "filters": filters_line,
                "sort": sort_line,
                "columns": columns_line or declarations[0][2],
                "active": active_sources[-1] if active_sources else None,
                "f_sources": [source for source in (filters_line, pasted_line, export_line) if source],
                "sort_sources": [source for source in (pasted_line, export_line if _one(export_query, "o") else None, sort_line) if source],
                "columns_sources": [
                    source for source in dict.fromkeys(
                        [source for _name, _values, source in declarations if source and source != (columns_line or declarations[0][2])]
                        + [columns_line or declarations[0][2]]
                    ) if source
                ],
                "active_from_sources": active_sources,
                "active_to_sources": active_to_sources,
            }
        )
    return screens, evidence


def _dump_field(name: str, value: object) -> str:
    return yaml.safe_dump({name: value}, sort_keys=False).strip()


def _render_screen(block: ScreenBlock, evidence: dict[str, object]) -> str:
    values = block.model_dump(exclude_none=True)
    fields = [
        ("screen", [evidence["heading"]]),
        ("f", evidence.get("f_sources", [evidence["export"]])),
        ("sort", evidence.get("sort_sources", [evidence["sort"]])),
        ("columns", evidence.get("columns_sources", [evidence["columns"]])),
        ("active_from", evidence.get("active_from_sources", [evidence["active"]])),
        ("active_to", evidence.get("active_to_sources", [evidence["active"]])),
    ]
    lines = ["```yaml"]
    for name, sources in fields:
        sources = [source for source in sources if source]
        if not sources:
            lines.append("# PROPOSED — no window stated in prose")
        else:
            for source in sources:
                lines.append(f"# from: {json.dumps(scrub(str(source)))}")
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
    print(scrub("".join(diff)), end="")


def _leading_comment_prose(source_text: str) -> str:
    lines: list[str] = []
    for line in source_text.splitlines():
        if line.startswith("#"):
            lines.append(line[1:].lstrip())
        elif not line.strip() and lines:
            lines.append("")
        else:
            break
    return "\n".join(lines).rstrip()


def render_lists(config: LegacyWatchlistsConfig, source_text: str | None = None) -> str:
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
    rules = _leading_comment_prose(source_text or "")
    intro = "# PROPOSED — derived from the committed tier rules."
    if rules:
        intro += "\n\n## Source derivation rules\n\n" + rules
    return "# Radar Lists\n\n" + intro + "\n\n" + "\n\n".join(blocks) + "\n"


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
        reader = csv.DictReader(io.StringIO(response.text))
        if reader.fieldnames is None or "Ticker" not in reader.fieldnames:
            raise ProposalRefused(
                f"{block.screen}: comparison response is not CSV with a Ticker header"
            )
        rows = list(reader)
        if any(None in row for row in rows):
            raise ProposalRefused(f"{block.screen}: comparison response has malformed CSV rows")
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
        {
            "section": evidence[index]["section_id"],
            "unit_id": evidence[index]["unit_id"],
            "placement": "at_end",
            "body": _render_screen(block, evidence[index]),
        }
        for index, block in enumerate(screens)
    ]
    units.append(
        {
            "section": evidence[-1]["section_id"],
            "unit_id": "radar-pool",
            "placement": "at_end",
            "body": "```yaml\n"
            + yaml.safe_dump(pool.model_dump(mode="json"), sort_keys=False).strip()
            + "\n```",
        }
    )
    artifact = build_artifact(
        "screens", target, hashlib.sha256(target_raw).hexdigest(),
        {"target_text": text, "pool_block": pool_raw.decode(), "ft_comparisons": comparisons}, units,
    )
    path, digest = write_artifact(artifact)
    print(scrub("\n\n".join(unit["body"] for unit in units)))
    _print_insertion_diff(target, text, units)
    print(f"artifact: {path}\nsha256: {digest}")


def lists_propose(args) -> None:
    from cobalt.vault import resolve_vault_path

    from .sources import LegacyWatchlistsConfig

    watchlists_path = Path(args.watchlists_yaml)
    try:
        raw = watchlists_path.read_bytes()
        config = LegacyWatchlistsConfig.model_validate(yaml.safe_load(raw))
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        raise ProposalRefused(f"invalid watchlists input {watchlists_path}: {error}") from error
    target = resolve_vault_path() / load_config().notes.lists
    if target.exists():
        raise ProposalRefused(f"Lists target already exists: {target}")
    note = render_lists(config, raw.decode())
    hashed = subprocess.run(
        ["git", "hash-object", str(watchlists_path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if hashed.returncode:
        raise ProposalRefused(
            f"git hash-object failed for {watchlists_path}: {hashed.stderr.strip()}"
        )
    blob = hashed.stdout.strip()
    artifact = build_artifact(
        "lists", target, "absent" if not target.exists() else hashlib.sha256(target.read_bytes()).hexdigest(),
        {"watchlists_yaml": raw.decode(), "watchlists_git_blob": blob},
        [{"section": None, "unit_id": None, "placement": "create_if_absent", "body": note}],
    )
    path, digest = write_artifact(artifact)
    print(note)
    _print_insertion_diff(target, "", artifact["units"])
    print(f"artifact: {path}\nsha256: {digest}")


def screens_validate(args) -> None:
    """Validate current prose, pool, Lists, and installed-block drift without writes."""
    from cobalt.taxonomy.loader import load_tunables
    from cobalt.vault import resolve_vault_path

    from .collector import DAILY_RETRIES_PER_REQUEST
    from .notes import FENCE_RE, parse_note, parse_note_bytes, plan_transport_demand
    from .sources import LegacyWatchlistsConfig, archive_targets

    cfg = load_config()
    vault = resolve_vault_path()
    screens_path = vault / cfg.notes.screens
    lists_path = vault / cfg.notes.lists
    try:
        screens_raw = screens_path.read_bytes()
        screens_text = screens_raw.decode("utf-8")
    except (OSError, UnicodeError) as error:
        raise ProposalRefused(f"Screens note unreadable {screens_path}: {error}") from error
    derived, evidence = derive_screens(screens_text)

    pool_path = Path(args.pool_block)
    try:
        pool_raw = pool_path.read_bytes()
        pool = PoolBlock.model_validate(yaml.safe_load(pool_raw))
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
        raise ProposalRefused(f"invalid pool-block file {pool_path}: {error}") from error
    unknown = sorted(set(pool.overrides) - {item.screen for item in derived})
    if unknown:
        raise ProposalRefused(f"pool-block overrides unknown screen(s) {unknown}")

    if lists_path.exists():
        lists = parse_note(lists_path, "lists")
    else:
        watchlists_path = Path(args.watchlists_yaml)
        try:
            watchlists_raw = watchlists_path.read_bytes()
            legacy = LegacyWatchlistsConfig.model_validate(yaml.safe_load(watchlists_raw))
            prospective = render_lists(legacy, watchlists_raw.decode()).encode()
        except (OSError, UnicodeError, ValueError, yaml.YAMLError) as error:
            raise ProposalRefused(
                f"Lists note is absent and prospective watchlists input is invalid "
                f"{watchlists_path}: {error}"
            ) from error
        lists = parse_note_bytes(lists_path, "lists", prospective)
    if not lists.ok:
        raise ProposalRefused(f"Lists validation failed: {'; '.join(lists.errors)}")

    tunables = load_tunables().by_key
    interval = int(tunables["radar.scan_interval"].value)
    ceiling_raw = tunables["radar.finviz_max_rpm"].value
    if ceiling_raw is None:
        raise ProposalRefused("radar.finviz_max_rpm is unmeasured")
    ceiling = int(ceiling_raw)
    list_blocks = [item.block for item in lists.blocks if isinstance(item.block, ListBlock)]
    chunk_count = sum(-(-len(block.tickers) // cfg.list_chunk_size) for block in list_blocks)
    # One total-demand computation for every consumer (L53): the same plan
    # `radar sources` and the resident use, daily bars and context included.
    demand = plan_transport_demand(
        pool,
        screen_count=len(derived),
        list_blocks=list_blocks,
        list_chunk_size=cfg.list_chunk_size,
        scan_interval=interval,
        context_tickers=len(cfg.context.tickers),
        daily_names=pool.cap,
        retries_per_request=DAILY_RETRIES_PER_REQUEST,
        ceiling_rpm=ceiling,
    )
    # L53: that same prospective radar demand joins every other consumer's,
    # over the radar's own window, through the ONE shared gate.
    from .notes import DemandConsumer, TotalDemandExceeded, check_total_demand, radar_window, scheduled_consumers

    refused: TotalDemandExceeded | None = None
    try:
        check_total_demand(
            [
                DemandConsumer(
                    name="radar", rpm=demand.steady_rpm, window=radar_window(tunables),
                    basis="proposed total",
                ),
                *[c for c in scheduled_consumers(ceiling=ceiling, tunables=tunables) if c.name != "radar"],
            ],
            subject="radar",
            ceiling=ceiling,
        )
    except TotalDemandExceeded as error:
        refused = error
    if demand.refusal is not None or refused is not None:
        reason = demand.refusal or "the total across every consumer exceeds the ceiling"
        raise ProposalRefused(
            f"pool budget exceeded: {reason}; planned_rpm={demand.steady_rpm:.2f} "
            f"(pool={demand.pool_rpm:.2f}, screens={len(derived)}, lists_chunks={chunk_count}, "
            f"context={demand.context_rpm:.2f}, daily_names={demand.daily_names}), "
            f"finviz_max_rpm={ceiling}, cap={pool.cap}, scan_interval={interval}"
            + (f"; {refused}" if refused is not None else "")
        ) from refused

    installed_status = "not installed"
    if FENCE_RE.search(screens_raw):
        installed = parse_note_bytes(screens_path, "screens", screens_raw)
        if not installed.ok:
            raise ProposalRefused(f"installed Screens blocks invalid: {'; '.join(installed.errors)}")
        installed_screens = {
            item.block.screen: item.block
            for item in installed.blocks
            if isinstance(item.block, ScreenBlock)
        }
        if set(installed_screens) != {item.screen for item in derived}:
            raise ProposalRefused(
                "installed/prose screen key drift: "
                f"installed={sorted(installed_screens)}, prose={sorted(item.screen for item in derived)}"
            )
        for block, sources in zip(derived, evidence, strict=True):
            current = installed_screens[block.screen]
            for field in ("f", "sort", "columns"):
                if getattr(current, field) != getattr(block, field):
                    raise ProposalRefused(f"{block.screen}: installed/prose {field} drift")
            for field, source_key in (
                ("active_from", "active_from_sources"),
                ("active_to", "active_to_sources"),
            ):
                if sources.get(source_key) and getattr(current, field) != getattr(block, field):
                    raise ProposalRefused(f"{block.screen}: installed/prose {field} drift")
        installed_pool = next(item.block for item in installed.blocks if item.key == "pool")
        if installed_pool != pool:
            raise ProposalRefused("installed/provided pool block drift")
        installed_status = "installed blocks match prose"

    print(scrub(f"Screens note: {screens_path}"))
    print(f"Screens sha256: {hashlib.sha256(screens_raw).hexdigest()}")
    print(scrub(f"Lists note: {lists_path}"))
    print(f"Lists sha256: {lists.note_sha256}")
    print(f"Pool sha256: {hashlib.sha256(pool_raw).hexdigest()}")
    for block in derived:
        print(f"{block.screen}: {block.active_from}-{block.active_to}")
    print(
        f"transport budget: {demand.steady_rpm:.2f}/{ceiling} rpm "
        f"(pool={demand.pool_rpm:.2f}, cap={pool.cap}, "
        f"screens={len(derived)}, lists_chunks={chunk_count}, "
        f"context={demand.context_rpm:.2f}, scan_interval={interval}s)"
    )
    drain = (
        "none" if demand.cold_drain_minutes is None
        else f"{demand.cold_drain_minutes:.1f} min at {demand.headroom_rpm:.2f} rpm headroom"
    )
    print(
        f"daily bars: {demand.daily_names} name(s) once per ET day, cold drain {drain}; "
        f"first cold cycle {demand.cold_cycle_seconds:.0f}s paced by the shared bucket"
    )
    print(f"drift: {installed_status}")
    print(f"archive targets: {len(archive_targets(lists))}")


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
