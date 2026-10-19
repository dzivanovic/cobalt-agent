"""Split one UTF-8 markdown file into chunks at its structure (card 468 G2, G3).

THE STRUCTURE, NEVER A SIZE NUMBER (DECISION D3). A blank line ends a block.
A paragraph is one chunk; a list item is one chunk (its indented or lazy
continuation lines with it); a table row is one chunk (the `|---|` separator
row is none); a fenced block is one chunk, blank lines and all. A heading is
no chunk of its own: its text rides on the first chunk of its section, and a
heading with nothing under it before the next heading (or the end) is kept as
its own chunk, so no heading text is ever dropped. A thematic break (`---`)
is no chunk. Line numbers are 1-based and inclusive; a line is what a
newline ends (a form feed or U+2028 is no line break).

LOUD (L1, F-14). A missing path, a directory, an unreadable file, a
non-UTF-8 file, an empty file or one that yields no chunk raises
`GenesisImportError` naming the path; nothing here writes anything.
"""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path


class GenesisImportError(Exception):
    """A source that cannot be imported. Raised before any write."""


@dataclass(frozen=True)
class Chunk:
    seq: int
    line_start: int
    line_end: int
    body: str


@dataclass(frozen=True)
class Source:
    #: The path exactly as it was given, the row's `source`.
    source: str
    sha256: str
    chunks: tuple[Chunk, ...]


_HEADING = re.compile(r"^ {0,3}#{1,6}(\s|$)")
_LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])(\s|$)")
_TABLE_ROW = re.compile(r"^\s*\|")
_TABLE_SEPARATOR = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
_THEMATIC_BREAK = re.compile(r"^ {0,3}([-*_])(\s*\1){2,}\s*$")
_FENCE = re.compile(r"^ {0,3}(```|~~~)")


def chunk_markdown(text: str) -> list[Chunk]:
    """The chunks of `text`, in order, `seq` from 1."""
    # A line is what `\n` ends (grep -n, an editor): str.splitlines() would
    # also break at a form feed or U+2028 and shift every later line (check O2).
    lines = [line.removesuffix("\r") for line in text.split("\n")]
    blocks: list[tuple[int, int, list[str]]] = []  # (start, end, lines), 1-based
    heading: tuple[int, str] | None = None
    current: list = []  # [start, end, lines] of the open block

    def close() -> None:
        nonlocal current, heading
        if not current:
            return
        start, end, body = current
        if heading is not None:
            start, body = heading[0], [heading[1], *body]
            heading = None
        blocks.append((start, end, body))
        current = []

    def flush_heading() -> None:
        nonlocal heading
        if heading is not None:
            blocks.append((heading[0], heading[0], [heading[1]]))
            heading = None

    i = 0
    while i < len(lines):
        number, line = i + 1, lines[i]
        if _FENCE.match(line):
            close()
            marker = _FENCE.match(line).group(1)
            end = i
            while end + 1 < len(lines):
                end += 1
                if lines[end].strip().startswith(marker):
                    break
            current = [number, end + 1, lines[i:end + 1]]
            close()
            i = end + 1
            continue
        if not line.strip():
            close()
        elif _HEADING.match(line):
            close()
            flush_heading()
            heading = (number, line.rstrip())
        elif _THEMATIC_BREAK.match(line) and not current:
            pass
        elif _TABLE_SEPARATOR.match(line) and _TABLE_ROW.match(line):
            close()
        elif _TABLE_ROW.match(line):
            close()
            current = [number, number, [line.rstrip()]]
            close()
        elif _LIST_ITEM.match(line):
            close()
            current = [number, number, [line.rstrip()]]
        elif current:
            current[1] = number
            current[2].append(line.rstrip())
        else:
            current = [number, number, [line.rstrip()]]
        i += 1
    close()
    flush_heading()
    return [Chunk(seq=n, line_start=s, line_end=e, body="\n".join(b))
            for n, (s, e, b) in enumerate(blocks, 1)]


def read_source(path: str) -> Source:
    """Read, decode and chunk the one file at `path` (as given), or raise."""
    p = Path(path)
    if not p.exists():
        raise GenesisImportError(f"{path}: no such file")
    if p.is_dir():
        raise GenesisImportError(f"{path}: is a directory, not a markdown file")
    try:
        data = p.read_bytes()
    except OSError as e:
        raise GenesisImportError(f"{path}: unreadable ({e.strerror or e})") from e
    if not data:
        raise GenesisImportError(f"{path}: empty file")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as e:
        raise GenesisImportError(f"{path}: not UTF-8 ({e.reason} at byte {e.start})") from e
    chunks = chunk_markdown(text.removeprefix("﻿"))
    if not chunks:
        raise GenesisImportError(f"{path}: yields no chunk")
    return Source(source=path, sha256=hashlib.sha256(data).hexdigest(), chunks=tuple(chunks))


__all__ = ["Chunk", "GenesisImportError", "Source", "chunk_markdown", "read_source"]
