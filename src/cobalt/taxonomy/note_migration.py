"""One-off: migrate the 22 strategy notes to the ADR-0008 D3 shape.

`cobalt taxonomy migrate-strategy-notes --dry-run | --apply [--note SLUG]`

THREE EDITS PER NOTE, all through `VaultWriter` and nothing else (L28):

1. **The definition unit** (`upsert_unit`, section `definition`, unit
   `trade_def:<slug>`) — TEXTUAL line edits on the fenced YAML that is
   already there. Not a re-serialisation: `yaml.safe_dump` would reorder
   keys, drop every comment a human wrote next to a rule, and re-flow
   every block. The rule is "touch the lines that change and no others".
   * drop `  id:` and `  name:` — the frontmatter owns both (rulings a/e);
   * where the YAML's name differed from the frontmatter's, append the old
     name to `aliases:` (ruling e) — one line edited;
   * fold the variable registry into `quality_factors[]` (ruling b.2): an
     entry whose registry row was all-defaults stays a bare string with
     its trailing comment; one with a non-default `source`/`tier`/
     `frontier` becomes a one-line flow mapping, comment kept.
   * a DRAFT's unit gets the partial mapping its setup x trade matrix row
     provides (ruling b.1), commented as a draft.

2. **The tunables unit** (`upsert_unit`, unit `tunables:<slug>`) — this
   trader's own `per_trade(...)` rows, copied VERBATIM out of
   `configs/cobalt/taxonomy/tunables.yaml` with the comments that belong
   to them, and deleted from that file in the same commit (ruling b.3).
   A new unit id is appended inside the section, so it lands directly
   after the definition unit.

3. **The frontmatter** (`upsert_region`, the one marker-less carve-out) —
   `category:` out, `class:`/`family:` in, filled from the loaded def.
   `category:` is removed ONLY if it is blank; a value there is a human's
   and the note is refused and reported, never overwritten.

WHERE THE DELETED INPUTS COME FROM. The setup x trade matrix and the 13
variable registries were deleted in the commit that made the vault the
truth, and they are USER data — putting them back in the working tree,
even briefly, would undo that. So this command reads them straight out of
git (`git show <rev>:<path>`), deterministically, at the revision named
below. That is also why this module is a one-off and says so: when the 22
notes are migrated it has nothing left to do.

IT PROVES ITSELF. For every populated note the command asserts that the
def it is about to write is the SAME def, by comparing canonical md5s of
the before and after mappings with `id`/`name` stripped and
`quality_factors` reduced back to names — the same canonicalisation the
pre-deletion proof used. A drift fails the whole run, loudly, before
anything is written.
"""

from __future__ import annotations

import hashlib
import re
import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml

from cobalt.vault import resolve_vault_path
from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.frontmatter import frontmatter_span, split_frontmatter
from cobalt.vaultwrite.markers import find_section

from .loader import TUNABLES_PATH
from .slug import trade_key
from .trade_def import TradeDef
from .vault_loader import (
    DEFINITION_SECTION,
    DEF_UNIT_PREFIX,
    STRATEGIES_DIR,
    TUNABLES_UNIT_PREFIX,
    VaultTaxonomyError,
)

#: The revision the deleted inputs are read from — the parent of the
#: commit that removed them. A repo fact, not user data.
PRE_DELETION_REV = "96c9159^"
GRID_PATH = "configs/cobalt/taxonomy/cameron_grid.yaml"
VARIABLES_PATH = "configs/cobalt/taxonomy/variables/{yaml_id}.yaml"

#: The frontmatter region's section label. Distinct from the trade note's
#: (`trade-frontmatter`) so the two note types never share a baseline row.
FRONTMATTER_SECTION = "strategy-frontmatter"
FRONTMATTER_REGION = "frontmatter"

WRITER_NAME = "taxonomy.migrate_strategy_notes"

#: `QualityFactor`'s defaults. A registry entry equal to these on every
#: attribute contributes nothing, so its item stays a bare string.
_FACTOR_DEFAULTS = {
    "scale_min": 1,
    "scale_max": 10,
    "source": "human",
    "tier": "judgment",
    "why_template": "",
    "status": "stub",
    "frontier": False,
}
#: Emitted in this order when a factor has to become a mapping. Fixed so
#: two runs of this command produce the same bytes.
_FACTOR_ORDER = ("source", "tier", "frontier", "scale_min", "scale_max")

_FENCE_OPEN_RE = re.compile(r"^\s*```ya?ml\s*$")
_FENCE_CLOSE_RE = re.compile(r"^\s*```\s*$")
_ITEM_RE = re.compile(r"^(\s*-\s+)([^#]*?)(\s*#.*)?$")
_CFG_TOKEN_RE = re.compile(r"cfg\(([a-zA-Z0-9_.]+)\)")

#: A `# --- ... ---` line in tunables.yaml groups several rows; it belongs
#: to the FILE, not to the row under it, so it is not copied into a note.
_GROUP_HEADER_RE = re.compile(r"^\s*#\s*-{2,}.*$")


class NoteMigrationError(VaultTaxonomyError):
    """The migration cannot proceed on a note — refuse, never guess."""


# ---------------------------------------------------------------------
# Inputs recovered from git
# ---------------------------------------------------------------------


def _git_show(path: str, rev: str) -> str:
    proc = subprocess.run(
        ["git", "show", f"{rev}:{path}"],
        cwd=Path(__file__).resolve().parents[3],
        capture_output=True,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        raise NoteMigrationError(
            f"could not read {path} at {rev} from git: "
            f"{proc.stderr.strip().splitlines()[-1] if proc.stderr else 'unknown error'}. "
            "The setup x trade matrix and the variable registries are USER data and "
            "were deleted on purpose; this one-off migration reads them from history "
            "rather than putting them back in the working tree."
        )
    return proc.stdout


def load_matrix(rev: str = PRE_DELETION_REV) -> dict[str, list[dict[str, str]]]:
    """`{trade id: [{setup_ref, relation}, ...]}` — ruling b.1's source."""
    raw = yaml.safe_load(_git_show(GRID_PATH, rev))
    return raw["valid_setups"]


def load_registry(yaml_id: str, rev: str = PRE_DELETION_REV) -> dict[str, dict[str, Any]]:
    """`{factor name: non-default attributes}` for one trade."""
    raw = yaml.safe_load(_git_show(VARIABLES_PATH.format(yaml_id=yaml_id), rev))
    out: dict[str, dict[str, Any]] = {}
    for entry in raw["variables"]:
        extras = {
            k: v
            for k, v in entry.items()
            if k != "name" and v != _FACTOR_DEFAULTS.get(k, object())
        }
        out[entry["name"]] = extras
    return out


# ---------------------------------------------------------------------
# The canonical-md5 proof, same shape as the pre-deletion one
# ---------------------------------------------------------------------


def canonical_md5(mapping: dict[str, Any], *, drop_aliases: bool = False) -> str:
    """md5 of a def mapping, canonicalised the way the proof does it.

    `id`/`name` stripped and `quality_factors` reduced to plain names, so
    the value is comparable with the PRE-DELETION proof's table — that is
    the number this command prints, and it is the one recorded in the
    deletion commit.

    `drop_aliases=True` additionally removes `aliases[]`, and is used for
    the DRIFT CHECK only. Ruling e deliberately appends the YAML's old
    name to that list, so a before/after comparison that included it would
    always differ and would prove nothing; the alias move is asserted
    exactly and separately (`assert_alias_move`) instead of being hashed.
    """
    skip = set(TradeDef.INJECTED_FIELDS) | ({"aliases"} if drop_aliases else set())
    body = {k: v for k, v in mapping.items() if k not in skip}
    if "quality_factors" in body:
        body["quality_factors"] = [
            q["name"] if isinstance(q, dict) else q for q in body["quality_factors"]
        ]
    text = yaml.safe_dump(body, sort_keys=True, default_flow_style=False)
    return hashlib.md5(text.encode("utf-8")).hexdigest()


def assert_alias_move(
    before: dict[str, Any], after: dict[str, Any], *, yaml_name: str, fm_name: str
) -> None:
    """`aliases[]` gained the old YAML name, and nothing else (ruling e)."""
    expected = list(before.get("aliases") or [])
    if yaml_name != fm_name:
        expected.append(yaml_name)
    actual = list(after.get("aliases") or [])
    if actual != expected:
        raise NoteMigrationError(
            f"aliases[] moved wrongly: expected {expected!r}, got {actual!r}. "
            "Ruling e appends the YAML's old display name and touches nothing else."
        )


# ---------------------------------------------------------------------
# Textual editors
# ---------------------------------------------------------------------


def _fence_span(lines: list[str]) -> Optional[tuple[int, int]]:
    """(first body line, line of the closing fence) of the YAML block."""
    for i, line in enumerate(lines):
        if _FENCE_OPEN_RE.match(line):
            for j in range(i + 1, len(lines)):
                if _FENCE_CLOSE_RE.match(lines[j]):
                    return (i + 1, j)
            return None
    return None


def _quote_alias(name: str) -> str:
    """A flow-sequence item that YAML would mis-parse gets quoted."""
    if re.search(r"[,:\[\]{}#&*!|>'\"%@`]", name) or name != name.strip():
        escaped = name.replace('"', '\\"')
        return f'"{escaped}"'
    return name


def edit_definition_unit(
    body: str, *, fm_name: str, registry: dict[str, dict[str, Any]]
) -> tuple[str, list[str]]:
    """Apply rulings a, e and b.2 to a populated definition unit's body.

    Returns (new body, notes). Every line the rules do not name is
    byte-identical on the way out.
    """
    lines = body.split("\n")
    span = _fence_span(lines)
    if span is None:
        raise NoteMigrationError("the definition unit has no fenced YAML block")
    start, end = span
    notes: list[str] = []

    out: list[str] = list(lines[:start])
    yaml_name: Optional[str] = None
    alias_line: Optional[int] = None
    name_line_index: Optional[int] = None
    in_quality = False

    for i in range(start, end):
        line = lines[i]

        if re.match(r"^  id:(\s|$)", line):
            notes.append("dropped `id:` (the frontmatter slug is the id — ruling a)")
            continue

        if re.match(r"^  name:(\s|$)", line):
            yaml_name = _scalar(line.split(":", 1)[1])
            name_line_index = len(out)
            notes.append("dropped `name:` (the frontmatter name wins — ruling e)")
            continue

        # No `\s` after the colon on purpose: a BLOCK sequence
        # (`aliases:` then `    - X`) must reach `_append_alias` and be
        # refused there, not fall through and grow a second `aliases:` key.
        if re.match(r"^  aliases:", line):
            alias_line = len(out)
            out.append(line)
            continue

        if re.match(r"^  quality_factors:\s*$", line):
            in_quality = True
            out.append(line)
            continue

        if in_quality:
            # The block ends at the next key at the mapping's own indent.
            if line.strip() and not line.startswith("    "):
                in_quality = False
                out.append(line)
                continue
            rewritten = _rewrite_factor_line(line, registry)
            if rewritten != line:
                notes.append(f"folded registry attributes into {line.strip()[:40]!r}")
            out.append(rewritten)
            continue

        out.append(line)

    # --- ruling e: the YAML's own name joins aliases[] when it differed
    if yaml_name is not None and yaml_name != fm_name:
        quoted = _quote_alias(yaml_name)
        if alias_line is not None:
            out[alias_line] = _append_alias(out[alias_line], quoted)
            notes.append(f"appended {yaml_name!r} to aliases[] (ruling e)")
        else:
            insert_at = name_line_index if name_line_index is not None else start
            out.insert(insert_at, f"  aliases: [{quoted}]")
            notes.append(f"added aliases: [{yaml_name!r}] (ruling e)")

    out.extend(lines[end:])
    return "\n".join(out), notes


def _scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def _append_alias(line: str, quoted: str) -> str:
    """`  aliases: [A, B]` -> `  aliases: [A, B, <quoted>]`."""
    m = re.match(r"^(\s*aliases:\s*\[)(.*)(\]\s*)$", line)
    if not m:
        raise NoteMigrationError(
            f"aliases[] is not a one-line flow sequence, refusing to edit it: {line!r}"
        )
    head, inner, tail = m.groups()
    inner = f"{inner.rstrip()}, {quoted}" if inner.strip() else quoted
    return f"{head}{inner}{tail}"


def _rewrite_factor_line(line: str, registry: dict[str, dict[str, Any]]) -> str:
    m = _ITEM_RE.match(line)
    if not m:
        return line
    prefix, value, comment = m.group(1), m.group(2).rstrip(), m.group(3) or ""
    if not value or value.startswith("{"):
        return line
    name = _scalar(value)
    extras = registry.get(name)
    if not extras:
        return line          # all-defaults: a bare string, comment kept
    parts = [f"name: {name}"]
    for key in _FACTOR_ORDER:
        if key in extras:
            parts.append(f"{key}: {_yaml_scalar(extras[key])}")
    for key in sorted(set(extras) - set(_FACTOR_ORDER)):
        parts.append(f"{key}: {_yaml_scalar(extras[key])}")
    return f"{prefix}{{{', '.join(parts)}}}{comment}"


def _yaml_scalar(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, str):
        return value if re.match(r"^[A-Za-z0-9_.-]+$", value) else yaml.safe_dump(
            value, default_flow_style=True
        ).strip().rstrip("\n...").strip()
    return str(value)


def draft_unit_body(rows: list[dict[str, str]]) -> str:
    """Ruling b.1: a draft's unit carries its matrix row and says so."""
    lines = [
        "```yaml",
        "# partial — draft; the loader skips this until the def is complete",
        "# (ADR-0008 D3). These rows are this trade's setup x trade matrix",
        "# entry, moved here when that file left the repo — the def's own",
        "# valid_setups[] is the matrix's truth now.",
        "trade_def:",
        "  valid_setups:",
    ]
    for row in rows:
        lines.append(
            f"    - {{setup_ref: {row['setup_ref']}, relation: {row['relation']}}}"
        )
    lines.append("```")
    return "\n".join(lines)


def tunables_unit_body(slug: str, blocks: list[str]) -> str:
    """This trader's per-trade rows, verbatim, in their own unit."""
    key = trade_key(slug)
    lines = [
        "```yaml",
        f"# {key}'s own tunable rows — USER data, moved out of",
        "# configs/cobalt/taxonomy/tunables.yaml by ADR-0008 D3 b.3.",
        "# A separate unit from the definition on purpose: replay writes a",
        "# row's `status`, and a status write that re-rendered the def unit",
        "# would rewrite the def and every comment in it.",
        "tunables:",
    ]
    for block in blocks:
        lines.extend(block.split("\n"))
    lines.append("```")
    return "\n".join(lines)


def edit_frontmatter(
    lines: list[str], *, trade_class: Optional[str], families: list[str]
) -> tuple[str, list[str]]:
    """`category:` out (only if blank), `class:`/`family:` in after `name:`."""
    out: list[str] = []
    notes: list[str] = []
    name_index: Optional[int] = None
    saw_category = False

    for line in lines:
        m = re.match(r"^category:(.*)$", line)
        if m:
            saw_category = True
            if m.group(1).strip():
                raise NoteMigrationError(
                    f"frontmatter `category:` is not blank ({m.group(1).strip()!r}). "
                    "ADR-0008 D3 ruling d allows deleting a Cobalt-seeded BLANK key "
                    "only — a value there is a human's. Refusing this note."
                )
            notes.append("removed blank `category:` (ruling d)")
            continue
        out.append(line)
        if re.match(r"^name:\s", line):
            name_index = len(out)

    if not saw_category:
        notes.append("no `category:` key to remove")

    class_line = f"class: {trade_class}" if trade_class else "class:"
    family_line = f"family: [{', '.join(families)}]" if families else "family: []"
    existing = {i for i, line in enumerate(out) if re.match(r"^(class|family):", line)}
    if existing:
        for i in sorted(existing):
            if out[i].startswith("class:"):
                out[i] = class_line
            else:
                out[i] = family_line
        notes.append("updated existing `class:`/`family:`")
    else:
        at = name_index if name_index is not None else 1
        out[at:at] = [class_line, family_line]
        notes.append(f"inserted `{class_line}` and `{family_line}` after `name:`")

    return "\n".join(out), notes


# ---------------------------------------------------------------------
# tunables.yaml: lift the per-trade rows out
# ---------------------------------------------------------------------


@dataclass
class TunableLift:
    """The per-trade row blocks, keyed by the trade they belong to, plus
    the remaining text of `tunables.yaml`."""

    blocks: dict[str, list[str]]
    remaining_text: str
    rekeyed: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


def lift_per_trade_rows(
    text: Optional[str] = None, *, slug_by_key: dict[str, str]
) -> TunableLift:
    """Split `tunables.yaml` into per-trade row blocks and what remains.

    A row's BLOCK is its own lines plus the contiguous comment lines
    directly above it — except a `# --- ... ---` group header, which is a
    device of the file and belongs to no single row.

    `slug_by_key` maps a scope's trade key to the slug whose note the rows
    belong to; a key with no note is a loud failure, not a silent skip.
    """
    source = TUNABLES_PATH.read_text(encoding="utf-8") if text is None else text
    lines = source.split("\n")

    starts = [i for i, line in enumerate(lines) if re.match(r"^  - key:\s", line)]
    if not starts:
        raise NoteMigrationError(f"{TUNABLES_PATH} has no rows")
    bounds = list(zip(starts, starts[1:] + [len(lines)]))

    lift = TunableLift(blocks={}, remaining_text="")
    drop: set[int] = set()
    for start, stop in bounds:
        # A row's own lines stop at the first blank/comment run before the
        # next row; keep trailing blanks with the gap, not with the row.
        end = stop
        while end > start and (
            not lines[end - 1].strip() or lines[end - 1].lstrip().startswith("#")
        ):
            end -= 1
        row_lines = lines[start:end]
        # The block is a one-item YAML sequence once its two-space file
        # indent is removed; `[0]` is that item.
        row = yaml.safe_load("\n".join(line[2:] for line in row_lines))[0]
        scope = row["scope"]
        m = re.match(r"^per_trade\(([a-z0-9_]+)\)$", scope)
        if m is None:
            continue

        head = start
        while head > 0 and lines[head - 1].lstrip().startswith("#") and not _GROUP_HEADER_RE.match(lines[head - 1]):
            head -= 1
        block_lines = lines[head:end]

        key = m.group(1)
        slug = slug_by_key.get(key)
        if slug is None:
            raise NoteMigrationError(
                f"tunable row {row['key']!r} has scope {scope!r} but no strategy note "
                f"claims the slug for trade key {key!r}. A per-trade row without its "
                "trade is a key nothing can resolve — refusing to move it."
            )
        want = trade_key(slug)
        if want != key:
            block_lines = [
                re.sub(rf"(?<![a-z0-9_]){re.escape(key)}(?=[.)])", want, line)
                for line in block_lines
            ]
            lift.rekeyed.append(f"{key}.* -> {want}.* (ruling a)")
        lift.blocks.setdefault(slug, []).extend(block_lines)
        drop.update(range(head, end))

    kept = [line for i, line in enumerate(lines) if i not in drop]
    # Collapse the blank-line runs the removals left behind.
    collapsed: list[str] = []
    for line in kept:
        if not line.strip() and collapsed and not collapsed[-1].strip():
            continue
        collapsed.append(line)
    lift.remaining_text = "\n".join(collapsed)
    return lift


# ---------------------------------------------------------------------
# Planning and applying
# ---------------------------------------------------------------------


@dataclass
class NotePlan:
    slug: str
    name: str
    path: Path
    is_draft: bool
    #: The id the YAML unit authored, before this run drops it. Ruling a
    #: makes the slug the id, and for one trade the two do not agree
    #: (`trade_key(slug)` != the old id) — this is how the tunables lift
    #: learns which note a `per_trade(<old id>)` row belongs to, without
    #: any trade name being written into this repo.
    yaml_id: Optional[str] = None
    def_body: Optional[str] = None
    tunables_body: Optional[str] = None
    frontmatter_body: Optional[str] = None
    md5: Optional[str] = None
    notes: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def plan_notes(
    vault_root: Optional[Path] = None,
    *,
    only_slug: Optional[str] = None,
    rev: str = PRE_DELETION_REV,
) -> tuple[list[NotePlan], TunableLift]:
    """Compute every edit. Reads the vault and git; writes nothing."""
    root = Path(vault_root) if vault_root is not None else resolve_vault_path()
    directory = root / STRATEGIES_DIR
    if not directory.is_dir():
        raise NoteMigrationError(f"strategy notes directory not found: {directory}")

    matrix = load_matrix(rev)
    plans: list[NotePlan] = []
    all_plans: list[NotePlan] = []

    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if fm is None or not fm.get("trade_def"):
            raise NoteMigrationError(f"{path.name}: no `trade_def:` in the frontmatter")
        slug = fm["trade_def"]
        plan = _plan_one(path, root, text, fm, matrix, rev)
        all_plans.append(plan)
        if only_slug is None or slug == only_slug:
            plans.append(plan)

    # A row's scope names the trade by the id its YAML unit authored, and
    # ruling a re-keys one of those to its slug's `trade_key`. Both
    # spellings are therefore accepted, and both are READ FROM THE NOTES —
    # nothing in this repo has to know a trade's name to do it.
    slug_by_key: dict[str, str] = {}
    for plan in all_plans:
        slug_by_key[trade_key(plan.slug)] = plan.slug
        if plan.yaml_id:
            slug_by_key[plan.yaml_id] = plan.slug

    lift = lift_per_trade_rows(slug_by_key=slug_by_key)
    for plan in plans:
        blocks = lift.blocks.get(plan.slug)
        if blocks:
            plan.tunables_body = tunables_unit_body(plan.slug, blocks)
            plan.notes.append(f"{len(blocks and [b for b in blocks if b.lstrip().startswith('- key:')])} per-trade tunable row(s) moved in")
    return plans, lift


def _plan_one(path, root, text, fm, matrix, rev) -> NotePlan:
    slug = fm["trade_def"]
    name = str(fm.get("name") or "").strip()
    if not name:
        raise NoteMigrationError(f"{path.name}: frontmatter `name:` is missing")

    lines = text.splitlines()
    section = find_section(lines, DEFINITION_SECTION)
    if section is None:
        raise NoteMigrationError(f"{path.name}: no `{DEFINITION_SECTION}` section")
    unit = section.units.get(f"{DEF_UNIT_PREFIX}{slug}")
    if unit is None:
        raise NoteMigrationError(f"{path.name}: no `{DEF_UNIT_PREFIX}{slug}` unit")
    body = "\n".join(unit.body(lines))

    plan = NotePlan(slug=slug, name=name, path=path, is_draft=False)

    fence = _fence_span(body.split("\n"))
    populated = fence is not None and any(
        l.strip() for l in body.split("\n")[fence[0]:fence[1]]
    )

    if populated:
        before = yaml.safe_load("\n".join(body.split("\n")[fence[0]:fence[1]]))["trade_def"]
        plan.yaml_id = before.get("id")

        if plan.yaml_id is None:
            # ALREADY MIGRATED. A unit with no authored `id:` has been
            # through this command (or was written to the final contract
            # in the first place), so there is nothing to drop, nothing to
            # fold and no registry to read. Saying so and moving on is
            # what makes a second `--apply` a true no-op rather than a
            # KeyError — a migration you cannot re-run is a migration you
            # cannot trust halfway through.
            plan.notes.append("already in the ADR-0008 D3 shape — def untouched")
            plan.def_body = None
            trade_class = before.get("class")
            families = list(before.get("family") or [])
            return _finish_frontmatter(plan, lines, trade_class, families, path)

        registry = load_registry(plan.yaml_id, rev)
        new_body, notes = edit_definition_unit(body, fm_name=name, registry=registry)
        after_span = _fence_span(new_body.split("\n"))
        after = yaml.safe_load(
            "\n".join(new_body.split("\n")[after_span[0]:after_span[1]])
        )["trade_def"]

        drift_before = canonical_md5(before, drop_aliases=True)
        drift_after = canonical_md5(after, drop_aliases=True)
        if drift_before != drift_after:
            raise NoteMigrationError(
                f"{path.name}: the edit CHANGED the def. Canonical md5 (aliases "
                f"excluded) {drift_before} -> {drift_after}. These edits may only "
                "drop id/name, extend aliases[] and attach registry attributes to "
                "quality_factors[]; nothing else. Refusing the whole run."
            )
        assert_alias_move(
            before, after, yaml_name=str(before.get("name", "")), fm_name=name
        )
        # The number the pre-deletion proof printed, re-asserted here.
        plan.md5 = canonical_md5(before)
        plan.def_body = new_body if new_body != body else None
        plan.notes.extend(notes)
        trade_class, families = after.get("class"), list(after.get("family") or [])
    else:
        plan.is_draft = True
        rows = matrix.get(trade_key(slug))
        if rows is None:
            plan.def_body = None
            plan.warnings.append(
                f"no setup x trade matrix row for trade key {trade_key(slug)!r} — the "
                "unit is left EMPTY and this note stays a draft. The matrix keys that "
                "no note claims are reported at the end of the run; pairing one to a "
                "note is a ruling, not something this command may guess."
            )
        else:
            plan.def_body = draft_unit_body(rows)
            plan.notes.append(f"seeded {len(rows)} matrix row(s) as a partial def")
        trade_class, families = None, []

    return _finish_frontmatter(plan, lines, trade_class, families, path)


def _finish_frontmatter(plan, lines, trade_class, families, path) -> NotePlan:
    fm_span = frontmatter_span(lines)
    if fm_span is None:
        raise NoteMigrationError(f"{path.name}: no frontmatter block")
    fm_lines = lines[fm_span[0]:fm_span[1]]
    new_fm, fm_notes = edit_frontmatter(
        fm_lines, trade_class=trade_class, families=families
    )
    plan.frontmatter_body = new_fm if new_fm != "\n".join(fm_lines) else None
    plan.notes.extend(fm_notes)
    return plan


@dataclass
class NoteOutcome:
    slug: str
    path: Path
    actions: dict[str, str] = field(default_factory=dict)
    write_ids: dict[str, Optional[int]] = field(default_factory=dict)
    diffs: dict[str, str] = field(default_factory=dict)
    md5: Optional[str] = None
    notes: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


def apply_plans(
    plans: list[NotePlan], *, dry_run: bool, db_name: Optional[str] = None
) -> list[NoteOutcome]:
    store = VaultWriteStore(db_name)
    store.ensure_schema()
    writer = VaultWriter(WRITER_NAME, store=store, dry_run=dry_run)

    outcomes: list[NoteOutcome] = []
    for plan in plans:
        outcome = NoteOutcome(
            slug=plan.slug, path=plan.path, md5=plan.md5,
            notes=list(plan.notes), warnings=list(plan.warnings),
        )
        if plan.def_body is not None:
            r = writer.upsert_unit(
                plan.path, DEFINITION_SECTION, f"{DEF_UNIT_PREFIX}{plan.slug}",
                plan.def_body,
            )
            outcome.actions["def"] = r.action
            outcome.write_ids["def"] = r.write_id
            outcome.diffs["def"] = r.diff
        if plan.tunables_body is not None:
            r = writer.upsert_unit(
                plan.path, DEFINITION_SECTION, f"{TUNABLES_UNIT_PREFIX}{plan.slug}",
                plan.tunables_body,
            )
            outcome.actions["tunables"] = r.action
            outcome.write_ids["tunables"] = r.write_id
            outcome.diffs["tunables"] = r.diff
        if plan.frontmatter_body is not None:
            r = writer.upsert_region(
                plan.path, FRONTMATTER_SECTION, FRONTMATTER_REGION,
                plan.frontmatter_body, locate=frontmatter_span,
            )
            outcome.actions["frontmatter"] = r.action
            outcome.write_ids["frontmatter"] = r.write_id
            outcome.diffs["frontmatter"] = r.diff
        outcomes.append(outcome)
    return outcomes


def write_tunables_yaml(lift: TunableLift, *, dry_run: bool) -> str:
    """Remove the lifted rows from `tunables.yaml`. Returns a diff.

    NOT a vault write — `configs/cobalt/taxonomy/tunables.yaml` is repo
    config, so this is an ordinary file edit and its audit trail is the
    commit that carries it.
    """
    from difflib import unified_diff

    before = TUNABLES_PATH.read_text(encoding="utf-8")
    after = lift.remaining_text
    if not after.endswith("\n"):
        after += "\n"
    diff = "\n".join(
        unified_diff(
            before.splitlines(), after.splitlines(),
            fromfile=f"{TUNABLES_PATH.name} (before)",
            tofile=f"{TUNABLES_PATH.name} (after)",
            lineterm="",
        )
    )
    if not dry_run and after != before:
        TUNABLES_PATH.write_text(after, encoding="utf-8")
    return diff


#: The Templater file new strategy notes are stamped from. It is a
#: HUMAN-TREE file, not a Cobalt-written note: it has no markers, its
#: frontmatter is not the first bytes of the file (a Templater block is),
#: and `VaultWriter` would have nothing to address. So this one edit is a
#: plain deterministic file write, its diff IS the artifact, and it
#: follows the 09-06 R4 hand-work precedent — recorded, not hidden.
STRATEGY_TEMPLATE = "5 - Templates/Strategy.md"


def migrate_strategy_template(
    vault_root: Optional[Path] = None, *, dry_run: bool
) -> tuple[Optional[Path], str]:
    """`category:` -> `class:` + `family: []` in the strategy template."""
    from difflib import unified_diff

    root = Path(vault_root) if vault_root is not None else resolve_vault_path()
    path = root / STRATEGY_TEMPLATE
    if not path.exists():
        return None, f"(no {STRATEGY_TEMPLATE} in this vault — nothing to do)"

    before = path.read_text(encoding="utf-8")
    out: list[str] = []
    seen = False
    for line in before.split("\n"):
        m = re.match(r"^category:(.*)$", line)
        if m and not seen:
            if m.group(1).strip():
                raise NoteMigrationError(
                    f"{STRATEGY_TEMPLATE}: `category:` is not blank "
                    f"({m.group(1).strip()!r}) — refusing to delete a human's value."
                )
            seen = True
            out.append("class:")
            out.append("family: []")
            continue
        out.append(line)
    after = "\n".join(out)
    if not seen:
        return path, f"({STRATEGY_TEMPLATE}: no `category:` line — already migrated)"

    diff = "\n".join(
        unified_diff(
            before.splitlines(), after.splitlines(),
            fromfile=f"{STRATEGY_TEMPLATE} (before)",
            tofile=f"{STRATEGY_TEMPLATE} (after)",
            lineterm="",
        )
    )
    if not dry_run and after != before:
        path.write_text(after, encoding="utf-8")
    return path, diff


def unclaimed_matrix_keys(
    plans: list[NotePlan], rev: str = PRE_DELETION_REV
) -> list[str]:
    """Matrix rows no note claims — a ruling, not a guess.

    A note claims a matrix key by its slug's `trade_key` OR by the id its
    YAML unit authored (ruling a re-keys one trade, and the matrix still
    spells it the old way).
    """
    claimed = {trade_key(p.slug) for p in plans}
    claimed |= {p.yaml_id for p in plans if p.yaml_id}
    return sorted(set(load_matrix(rev)) - claimed)


__all__ = [
    "FRONTMATTER_REGION",
    "FRONTMATTER_SECTION",
    "PRE_DELETION_REV",
    "NoteMigrationError",
    "NoteOutcome",
    "NotePlan",
    "TunableLift",
    "apply_plans",
    "assert_alias_move",
    "canonical_md5",
    "draft_unit_body",
    "edit_definition_unit",
    "edit_frontmatter",
    "STRATEGY_TEMPLATE",
    "lift_per_trade_rows",
    "load_matrix",
    "load_registry",
    "migrate_strategy_template",
    "plan_notes",
    "tunables_unit_body",
    "unclaimed_matrix_keys",
    "write_tunables_yaml",
]
