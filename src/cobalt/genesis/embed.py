"""`cobalt genesis embed`: the one-shot embed command (F21 chunk 2; card 469 V5; FINAL F-03, F-09, F-14, F-15).

PREFLIGHT FIRST (F-03). One call of the `local.embed` route on a synthetic
sentence. No vector → `vectors: DEGRADED` is printed, nothing is written, the
run exits non-zero; F21 stays FTS-only. Never a zero vector, never exit 0
claiming vectors.

THEN, BEFORE ANY WRITE (F-02): the store checks the route's `dim` against
`genesis_chunk.embedding`'s declared dimension and crashes on a mismatch.

THEN ONE CHUNK PER CALL. Every chunk whose `embedding` is NULL is embedded and
committed as it lands, so a stopped run resumes where it stopped (checkpoint
and resume: a re-run embeds only the NULL rows). A failed call leaves that
row's FTS body and NULL vector; the run goes on and exits non-zero naming the
count (F-14).

NO IN-FLIGHT RULE (T4 dropped). Probe r2 X3: Plan max 1960 ms with an embed
loop in flight; X9: contended p95 2058 ms, 0/65 at 15 s or more, 65/65 parsed
(`reports/f21-host-probe-r2-2026-10-13.md`), so G1's signal does not bind.

THE CHUNK LENGTH (stated, F-14). The chunker cuts at structure, never at a
size (DECISION D3): a paragraph, list item, table row or fenced block is one
chunk of any length, so the chunker has no maximum. The embed model's context
is 2048 tokens; its WordPiece tokens each cover at least one character and the
model adds two special tokens, so a chunk of at most 2046 characters always
fits. A longer chunk is not sent (a server may truncate it silently): it stays
NULL, is named, and counts toward the non-zero exit.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

from cobalt import modelaccess
from cobalt.modelaccess import ModelCallError
from cobalt.modelaccess.config import ModelAccessConfig, load_routes

from .store import GenesisEmbedError

#: The one registry route this command calls (configs/cobalt/modelaccess.yaml).
ROUTE = "local.embed"
#: Synthetic: no text of his ever reaches the preflight (L32).
PREFLIGHT_TEXT = "genesis embed preflight: one synthetic sentence, no user text."
#: 2048-token context less the two special tokens; one character per token at worst (above).
MAX_CHUNK_CHARS = 2046


@dataclass(frozen=True)
class EmbedRun:
    pending: int
    embedded: int
    failed: int
    over_length: int


def run_embed(store, *, config: Optional[ModelAccessConfig] = None, embed: Optional[Callable] = None,
              out: Callable[[str], None] = print) -> EmbedRun:
    """Preflight, dimension check, then every NULL-vector chunk; raises
    `GenesisEmbedError` on DEGRADED, a dimension mismatch, or any chunk left NULL."""
    cfg = config or load_routes()
    embed = embed or modelaccess.embed_sync
    try:
        probe = embed(ROUTE, PREFLIGHT_TEXT, caller="genesis.embed.preflight", config=cfg)
    except ModelCallError as e:
        out("vectors: DEGRADED")
        raise GenesisEmbedError(
            f"vectors: DEGRADED — the {ROUTE} preflight returned no vector ({e.kind}: {e.detail}); "
            "nothing written, genesis stays FTS-only") from None
    store.check_embed_dim(probe.dim)

    pending = store.null_chunks()
    embedded = failed = over_length = 0
    for chunk_id, body in pending:
        if len(body) > MAX_CHUNK_CHARS:
            over_length += 1
            out(f"over-length: chunk {chunk_id} is {len(body)} characters (> {MAX_CHUNK_CHARS}); left NULL")
            continue
        try:
            result = embed(ROUTE, body, caller="genesis.embed", config=cfg)
        except ModelCallError as e:
            failed += 1
            out(f"failed: chunk {chunk_id} — {e.kind}; left NULL")
            continue
        store.set_embedding(chunk_id, result.vector, model=result.model_returned, dim=result.dim)
        embedded += 1
    run = EmbedRun(pending=len(pending), embedded=embedded, failed=failed, over_length=over_length)
    out(f"vectors: embedded {embedded} · failed {failed} · over-length {over_length} · of {len(pending)} NULL")
    if failed or over_length:
        raise GenesisEmbedError(
            f"{failed + over_length} of {len(pending)} chunk(s) left with no vector "
            f"(failed {failed}, over-length {over_length}); their FTS bodies stand, a re-run retries the NULL rows")
    return run


__all__ = ["EmbedRun", "MAX_CHUNK_CHARS", "PREFLIGHT_TEXT", "ROUTE", "run_embed"]
