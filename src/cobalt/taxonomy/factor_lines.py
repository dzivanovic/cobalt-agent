"""Line-level reading and editing of a def unit's `quality_factors:` block.

WHY TEXT, NOT YAML. A strategy note's Definition unit is the trader's
file: comments, spacing and item order are his. Re-dumping the parsed
mapping would rewrite every line of it. The two S2-P2 note changes —
the catalyst batch (R10) and the trail_fit draft (R5) — each touch ONE
item, so this module finds the block and its items by line and leaves
every other byte alone.

WHAT IT READS. Inside the unit body's fenced YAML block, the
`quality_factors:` key (block style only) and the sequence items under
it, at whatever indent the note uses (`    - name` as the shipped example
writes it, or `  - name` as a YAML dumper writes it). An item is its
`- ` line plus every following line indented deeper (a block mapping).
Blank and comment lines inside the block are kept and belong to no item.
Each item is parsed on its own with `yaml.safe_load` to get its name.

WHAT IT REFUSES, LOUD: no fence, no key or two keys, a flow-style list
(`quality_factors: [a, b]` — editing it by line would mean rewriting a
line he wrote), and any line inside the block it cannot classify.
"""

from __future__ import annotations

import re

import yaml
from pydantic import BaseModel, ConfigDict

_FENCE_OPEN_RE = re.compile(r"^\s*```ya?ml\s*$")
_FENCE_CLOSE_RE = re.compile(r"^\s*```\s*$")
_KEY_RE = re.compile(r"^(?P<indent> *)quality_factors:(?P<rest>.*)$")


class FactorLinesError(ValueError):
    """The unit's quality_factors block cannot be edited by line."""


class FactorItem(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str
    #: First line of the item and the line after its last, in unit-body lines.
    start: int
    end: int
    lines: tuple[str, ...]
    value: str | dict


class FactorBlock(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    key_line: int
    item_indent: int
    items: tuple[FactorItem, ...]

    @property
    def names(self) -> list[str]:
        return [item.name for item in self.items]

    def item(self, name: str) -> FactorItem | None:
        return next((item for item in self.items if item.name == name), None)


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _fence(lines: list[str]) -> tuple[int, int]:
    for i, line in enumerate(lines):
        if _FENCE_OPEN_RE.match(line):
            for j in range(i + 1, len(lines)):
                if _FENCE_CLOSE_RE.match(lines[j]):
                    return i + 1, j
            break
    raise FactorLinesError("the definition unit has no closed ```yaml fence")


def factor_block(lines: list[str]) -> FactorBlock:
    """The `quality_factors:` block of a unit body, split into lines."""
    start, close = _fence(lines)
    keys = [i for i in range(start, close) if _KEY_RE.match(lines[i])]
    if len(keys) != 1:
        raise FactorLinesError(f"expected exactly one `quality_factors:` key in the unit, found {len(keys)}")
    key = keys[0]
    match = _KEY_RE.match(lines[key])
    rest = match.group("rest").strip()
    if rest and not rest.startswith("#"):
        raise FactorLinesError(
            "`quality_factors:` is written flow-style on one line — Cobalt edits a factor list by line "
            "and will not rewrite that line; put one `- item` per line first"
        )
    key_indent = len(match.group("indent"))
    items: list[FactorItem] = []
    item_indent: int | None = None
    i = key + 1
    while i < close:
        line = lines[i]
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        indent = _indent(line)
        is_item = stripped == "-" or stripped.startswith("- ")
        if is_item and item_indent is None and indent >= key_indent:
            item_indent = indent
        if is_item and indent == item_indent:
            j = i + 1
            while j < close and lines[j].strip() and _indent(lines[j]) > item_indent:
                j += 1
            chunk = [ln[item_indent:] for ln in lines[i:j]]
            try:
                parsed = yaml.safe_load("\n".join(chunk))
            except yaml.YAMLError as e:
                raise FactorLinesError(f"quality_factors item at unit line {i + 1} does not parse: {e}") from e
            if not isinstance(parsed, list) or len(parsed) != 1:
                raise FactorLinesError(f"quality_factors item at unit line {i + 1} is not one sequence item")
            value = parsed[0]
            if isinstance(value, dict):
                name = value.get("name")
            else:
                name = value
            if not isinstance(name, str) or not name:
                raise FactorLinesError(f"quality_factors item at unit line {i + 1} has no name")
            items.append(FactorItem(name=name, start=i, end=j, lines=tuple(lines[i:j]), value=value))
            i = j
            continue
        if indent <= key_indent:
            break
        raise FactorLinesError(f"unexpected line inside quality_factors at unit line {i + 1}: {line!r}")
    if not items or item_indent is None:
        raise FactorLinesError("`quality_factors:` has no items")
    return FactorBlock(key_line=key, item_indent=item_indent, items=tuple(items))


def append_factor(lines: list[str], item_text: str) -> list[str]:
    """A new last item, at the block's own item indent."""
    block = factor_block(lines)
    at = block.items[-1].end
    return [*lines[:at], " " * block.item_indent + item_text, *lines[at:]]


def remove_factors(lines: list[str], names: set[str]) -> list[str]:
    """Every item whose name is in `names` removed; nothing else moves."""
    block = factor_block(lines)
    out = list(lines)
    for item in sorted((it for it in block.items if it.name in names), key=lambda it: it.start, reverse=True):
        del out[item.start:item.end]
    return out


def replace_factor(lines: list[str], name: str, item_text: str) -> list[str]:
    """The named item's lines replaced by one `item_text` line."""
    block = factor_block(lines)
    item = block.item(name)
    if item is None:
        raise FactorLinesError(f"no quality_factors item named {name!r}")
    return [*lines[:item.start], " " * block.item_indent + item_text, *lines[item.end:]]


__all__ = [
    "FactorBlock", "FactorItem", "FactorLinesError", "append_factor", "factor_block",
    "remove_factors", "replace_factor",
]
