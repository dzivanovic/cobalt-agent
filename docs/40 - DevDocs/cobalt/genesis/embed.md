# `src/cobalt/genesis/embed.py`

`run_embed(store, *, config=None, embed=None, out=print)`, the body of `cobalt genesis embed` (F21 chunk 2). One preflight call of the `local.embed` route on `PREFLIGHT_TEXT` (synthetic): no vector → prints `vectors: DEGRADED`, writes nothing, raises `GenesisEmbedError` (F-03). Then `store.check_embed_dim(probe.dim)` before any write (F-02). Then every NULL-vector chunk, one per call, each written as it lands; a failed call or a chunk over `MAX_CHUNK_CHARS` (2046: the model's 2048-token context less two special tokens, one character per token at worst) stays NULL and is named. The last line is `vectors: embedded <n> · failed <n> · over-length <n> · of <n> NULL`; any chunk left NULL raises (exit 1). No in-flight rule (T4 dropped by X3 / X9). The embedder is `cobalt.modelaccess.embed_sync`, read at call time.

## 2026-10-19 — f21-vectors-1013
New module (card 469 V5).
