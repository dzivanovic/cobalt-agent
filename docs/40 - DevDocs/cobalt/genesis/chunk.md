# `src/cobalt/genesis/chunk.py`

`chunk_markdown(text) -> list[Chunk]` splits at structure, never at a size number (DECISION D3): a blank line ends a block; a paragraph, a list item (with its continuation lines), a table row (the `|---|` separator is none) and a fenced block are each one chunk; a heading rides on its section's first chunk, or is its own chunk when nothing follows it before the next heading; a thematic break is none. `Chunk(seq, line_start, line_end, body)`, lines 1-based inclusive.

`read_source(path) -> Source(source, sha256, chunks)` reads one file as given and raises `GenesisImportError` naming the path for a missing path, a directory, an unreadable file, a non-UTF-8 file, an empty file or one that yields no chunk (L1, F-14). It writes nothing.

## 2026-10-19 — f21-genesis-1013
New module (card 468 G2, G3).
Check (card 820, O2): lines are split at `\n` only (a trailing `\r` dropped), not `str.splitlines()`, so a form feed or U+2028 inside a line no longer shifts the line ranges.
