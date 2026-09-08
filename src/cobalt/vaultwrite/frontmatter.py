"""The ONE frontmatter reader for the vault (one-path rule).

Obsidian frontmatter is a `---` fenced YAML block that must be the very
first bytes of a note. That constraint is why it cannot be bounded by
L28 markers (an HTML comment above the opening `---` stops it being
frontmatter; one inside stops it being YAML) and why `VaultWriter` treats
it as the single structurally-located region in the whole write path —
see `frontmatter_span` below.

WHY THIS FILE EXISTS. The same regex was written out twice, in
`prefill/trade_note.py` and `prefill/drc.py`, and ADR-0008's vault-backed
trade_def loader would have been the third copy. Three parsers of the
same bytes is three chances to disagree about what a note says, so the
regex and the split live here and every caller imports them.

READ-ONLY. Nothing here writes: a frontmatter WRITE goes through
`VaultWriter.upsert_region` and only through it (LAW L28 / ADR-0004).
"""

from __future__ import annotations

import re
from typing import Any, Optional

import yaml

#: `\A` — it is the head of the file or it is not frontmatter.
FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)


class FrontmatterError(RuntimeError):
    """The frontmatter block is present but is not a YAML mapping."""


def split_frontmatter(content: str) -> tuple[Optional[dict[str, Any]], str]:
    """`(frontmatter mapping | None, the body after it)`.

    `None` means the note has no frontmatter block at all — a fact, not
    an error; the callers that require one say so themselves. A block
    that is present but does not parse as a mapping IS an error: silently
    treating a malformed header as absent is how a note ends up written
    as if it had no `trade_def:` key.
    """
    m = FRONTMATTER_RE.match(content)
    if not m:
        return None, content
    parsed = yaml.safe_load(m.group(1))
    if parsed is None:
        return {}, content[m.end():]
    if not isinstance(parsed, dict):
        raise FrontmatterError(
            f"frontmatter is a {type(parsed).__name__}, not a mapping — "
            "refusing to read a note whose header does not parse."
        )
    return parsed, content[m.end():]


def frontmatter_span(lines: list[str]) -> Optional[tuple[int, int]]:
    """The `---` ... `---` block at the head of the file, as a line span.

    Markers cannot bound it (see the module docstring), so this is the ONE
    structurally-located region in the whole write path — the `locate`
    every `VaultWriter.upsert_region` call on a frontmatter passes.

    The span INCLUDES both `---` lines, so the body a caller writes back
    must include them too.
    """
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return (0, i + 1)
    return None


__all__ = [
    "FRONTMATTER_RE",
    "FrontmatterError",
    "frontmatter_span",
    "split_frontmatter",
]
