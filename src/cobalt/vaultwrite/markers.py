"""Marker syntax and parsing for the ONE vault write path (LAW L28).

Two nested marker kinds, both HTML comments so Obsidian's reading view
hides them:

    <!-- cobalt:section NAME -->   ...   <!-- /cobalt:section NAME -->
    <!-- cobalt:unit ID -->        ...   <!-- /cobalt:unit ID -->

A SECTION is the only region of a note Cobalt is allowed to write
inside (L28.2). A UNIT is the atomic thing Cobalt writes: it carries a
stable id, so the same id always updates in place instead of appending
a second copy. Anything inside a section that is not inside one of its
units is human text and is carried through verbatim, in position.

Everything here is line-based and deterministic — no regex over the
whole file, no LLM, no "closest match" guessing. Unbalanced, duplicated
or malformed markers raise `MarkerError`: a note whose markers don't
parse is never written to (fail-loud law).
"""

import re
from dataclasses import dataclass, field
from typing import Optional

SECTION_OPEN = "<!-- cobalt:section {name} -->"
SECTION_CLOSE = "<!-- /cobalt:section {name} -->"
UNIT_OPEN = "<!-- cobalt:unit {id} -->"
UNIT_CLOSE = "<!-- /cobalt:unit {id} -->"

# Deliberately narrow: a marker name is an identifier, never free text.
NAME_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:+-]*$")

_SECTION_OPEN_RE = re.compile(r"^\s*<!--\s*cobalt:section\s+(\S+)\s*-->\s*$")
_SECTION_CLOSE_RE = re.compile(r"^\s*<!--\s*/cobalt:section\s+(\S+)\s*-->\s*$")
_UNIT_OPEN_RE = re.compile(r"^\s*<!--\s*cobalt:unit\s+(\S+)\s*-->\s*$")
_UNIT_CLOSE_RE = re.compile(r"^\s*<!--\s*/cobalt:unit\s+(\S+)\s*-->\s*$")

# Transitional read-compat only (see writer.py's legacy_slot_present):
# the pre-L28 marker pair. NEVER written by this module; historical
# notes are not retro-marked (L28 step 1).
LEGACY_SLOT_OPEN = "<!-- cobalt-slot:{name} -->"


class MarkerError(RuntimeError):
    """Markers are malformed, unbalanced, duplicated or nested wrongly —
    refuse the write rather than guess where a section really ends."""


@dataclass(frozen=True)
class UnitBlock:
    """One `<!-- cobalt:unit ID -->` block. `open_line`/`close_line` are
    indices into the note's line list; the body is the lines strictly
    between them."""

    id: str
    open_line: int
    close_line: int

    def body(self, lines: list[str]) -> list[str]:
        return lines[self.open_line + 1 : self.close_line]


@dataclass(frozen=True)
class SectionBlock:
    name: str
    open_line: int
    close_line: int
    units: dict[str, UnitBlock] = field(default_factory=dict)

    def body(self, lines: list[str]) -> list[str]:
        return lines[self.open_line + 1 : self.close_line]

    def text(self, lines: list[str]) -> str:
        """The section INCLUDING its own markers — this is what gets
        persisted as before/after in vault_writes."""
        return "\n".join(lines[self.open_line : self.close_line + 1])


def validate_name(name: str, kind: str) -> str:
    if not NAME_RE.match(name or ""):
        raise MarkerError(
            f"Invalid {kind} name {name!r} — must match {NAME_RE.pattern} "
            "(no spaces, no free text; ids are stable identifiers)."
        )
    return name


def section_open(name: str) -> str:
    return SECTION_OPEN.format(name=validate_name(name, "section"))


def section_close(name: str) -> str:
    return SECTION_CLOSE.format(name=validate_name(name, "section"))


def unit_open(unit_id: str) -> str:
    return UNIT_OPEN.format(id=validate_name(unit_id, "unit"))


def unit_close(unit_id: str) -> str:
    return UNIT_CLOSE.format(id=validate_name(unit_id, "unit"))


def render_unit(unit_id: str, body: str) -> list[str]:
    """A unit as lines: open marker, body, close marker."""
    body_lines = body.split("\n") if body != "" else []
    return [unit_open(unit_id), *body_lines, unit_close(unit_id)]


def render_section(name: str, body_lines: list[str]) -> list[str]:
    return [section_open(name), *body_lines, section_close(name)]


def find_section(lines: list[str], name: str) -> Optional[SectionBlock]:
    """Locate one section by name, with its units. None if absent."""
    validate_name(name, "section")
    open_idx: Optional[int] = None
    close_idx: Optional[int] = None
    for i, line in enumerate(lines):
        m = _SECTION_OPEN_RE.match(line)
        if m and m.group(1) == name:
            if open_idx is not None:
                raise MarkerError(
                    f"Duplicate opening marker for section {name!r} "
                    f"(lines {open_idx + 1} and {i + 1}) — refusing to write."
                )
            open_idx = i
            continue
        m = _SECTION_CLOSE_RE.match(line)
        if m and m.group(1) == name:
            if open_idx is None:
                raise MarkerError(
                    f"Closing marker for section {name!r} at line {i + 1} with "
                    "no opening marker — refusing to write."
                )
            if close_idx is not None:
                raise MarkerError(
                    f"Duplicate closing marker for section {name!r} "
                    f"(lines {close_idx + 1} and {i + 1}) — refusing to write."
                )
            close_idx = i

    if open_idx is None:
        return None
    if close_idx is None:
        raise MarkerError(
            f"Section {name!r} opens at line {open_idx + 1} but never closes — "
            "refusing to write into an unbounded region."
        )
    return SectionBlock(
        name=name,
        open_line=open_idx,
        close_line=close_idx,
        units=_find_units(lines, open_idx + 1, close_idx, name),
    )


def _find_units(lines: list[str], start: int, end: int, section_name: str) -> dict[str, UnitBlock]:
    units: dict[str, UnitBlock] = {}
    open_stack: list[tuple[str, int]] = []
    for i in range(start, end):
        m = _UNIT_OPEN_RE.match(lines[i])
        if m:
            if open_stack:
                raise MarkerError(
                    f"Unit {m.group(1)!r} opens at line {i + 1} while unit "
                    f"{open_stack[-1][0]!r} is still open — units never nest."
                )
            open_stack.append((m.group(1), i))
            continue
        m = _UNIT_CLOSE_RE.match(lines[i])
        if m:
            if not open_stack or open_stack[-1][0] != m.group(1):
                raise MarkerError(
                    f"Unit closing marker {m.group(1)!r} at line {i + 1} does not "
                    "match the open unit — refusing to write."
                )
            unit_id, open_line = open_stack.pop()
            if unit_id in units:
                raise MarkerError(
                    f"Duplicate unit id {unit_id!r} in section {section_name!r} "
                    f"(lines {units[unit_id].open_line + 1} and {open_line + 1}) — "
                    "a unit id is unique by construction; refusing to write."
                )
            units[unit_id] = UnitBlock(id=unit_id, open_line=open_line, close_line=i)
    if open_stack:
        raise MarkerError(
            f"Unit {open_stack[-1][0]!r} opens at line {open_stack[-1][1] + 1} but "
            f"never closes inside section {section_name!r} — refusing to write."
        )
    return units


def all_sections(lines: list[str]) -> list[SectionBlock]:
    """Every section in a note, in file order. Used by create_if_absent to
    seed baselines for the units a freshly rendered template contains."""
    names: list[str] = []
    for line in lines:
        m = _SECTION_OPEN_RE.match(line)
        if m and m.group(1) not in names:
            names.append(m.group(1))
    out = []
    for name in names:
        block = find_section(lines, name)
        if block is not None:
            out.append(block)
    return out


def legacy_slot_present(text: str, name: str) -> bool:
    """True if the PRE-L28 `<!-- cobalt-slot:NAME -->` marker is in the
    note. Read-only compatibility: historical notes are not retro-marked
    (L28), so a note already filled by the old writer is treated as
    already-filled for that slot and skipped, never duplicated. Delete
    this once no unretired note carries the old markers."""
    return LEGACY_SLOT_OPEN.format(name=name) in text
