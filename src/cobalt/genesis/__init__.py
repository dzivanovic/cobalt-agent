"""F21 chunk 1, the FTS floor (F21 FINAL F-01, F-02, F-14, F-15; card 2026-10-13 468).

`chunk` splits one UTF-8 markdown file into chunks at its structure, `store`
writes one source's chunks to `"user".genesis_chunk` (migration 0026), and
`search` is THE one recall entry: F20, the dream job and O3 read through it
and nothing else (L3). No model call anywhere in this package.
"""

from .chunk import Chunk, GenesisImportError, Source, chunk_markdown, read_source

__all__ = ["Chunk", "GenesisImportError", "Source", "chunk_markdown", "read_source"]
