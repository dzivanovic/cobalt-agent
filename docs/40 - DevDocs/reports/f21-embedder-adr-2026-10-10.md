# ADR (proposal) · F21 embedder: local vs cloud · 2026-10-10

STATUS: **PROPOSED**. The L67 tribunal comes next. No F21 build starts before the SDK spike report and this ADR's tribunal (`s5-weekend-and-parked-answer-2026-10-10.md`, Lane C).
Code basis: main code commit `d0a5fbb8`; the working tree's `src/` and `configs/` diff against it is empty.

## Context
- The gate. `TRIAGE.md:43` (08-22) says: "Local-vs-cloud embedder ADR GATES the memory port". The reasons it gives are local-first, routing, and "1536-dim baked into 4 tables → migration either way". The ADR was never written (`memory-history-2026-09-20.md:200`, H3), and the ADR register still lists the embedder among the first ADRs "to land" (`docs/10 - Decisions/README.md:9-11`).
- F21 needs it. The Charter's acceptance test for F21 is "Cobalt answers 'why is the stop buffer 0.02' from the imported record", using Ledger + vault history "through its own memory pipeline" (`MVP-CHARTER-v0_2.md:200-203`; LADDER:935). No sprint builds that pipeline (`memory-history-2026-09-20.md:201`, H4). Option O3 (one table with FTS + pgvector) "needs the embedder ADR first" (`memory-history-2026-09-20.md:224`, and the cost-of-being-wrong row at :225).
- The old code calls a cloud embedder. `src/cobalt_agent/memory/postgres.py:243` and `:762` call LiteLLM `embedding(model="text-embedding-3-small")` with an `OPENAI_API_KEY` (:747, :754; a dummy key for a local endpoint, :759). On failure they return a zero vector (:264) or `None` (:259).
- Four old tables hard-code 1536 dimensions: `memory_logs.embedding` (`postgres.py:725`), `browser_fast_path.task_hash_embedding` (`postgres.py:196`), `news_events.embedding` (`schema.sql:87`) and `trades.trader_note_embedding` (`schema.sql:187`).
- The new core has no embedder and no memory module. `src/cobalt/` holds no `embed`/`pgvector` code (grep; one false hit in `smoke/checks.py:253`), and `memory-history`'s `topics/memory-system.md:8` agrees.
- The only model-access path in the new core is `configs/cobalt/modelaccess.yaml`. It has one route, `local.plan`, which points at LM Studio on `127.0.0.1:1234` (:18-22). The schema accepts only `lane: local` and `kind: openai_compatible` (`src/cobalt/modelaccess/config.py:43-44`). It refuses any `fallback` key (:125-126), and "A non-local lane is the routing tribunal's to add (L23/L25 frozen)" (:73-74).
- Laws:
  - L5: embeddings that bypass the routing layer are routing bypasses (LAWS:120).
  - L21: local when available (:175).
  - L22: the fast wire carries "memory machinery"; LiteLLM→Anthropic API is paid (:178).
  - L23: local trumps cloud even when cloud is free (:181).
  - L24: metered APIs are the narrowest rung (:184).
  - L25: cloud fallback is an exception handler, never a route (:188).
  - L41: processes hold secrets, never models (:249).
  - L5 and L21–L27 are FROZEN until the routing tribunal rules (LAWS:104).

## Options
| | **A. Local embedder** (LM Studio local lane, new `local.embed` route) | **B. Cloud embedder through the routing layer** (e.g. `text-embedding-3-small`) | **C. None yet** (Postgres FTS only; vectors deferred) |
|---|---|---|---|
| Laws | Fits L21/L23/L24 rung 1. It uses the existing loopback-only lane (`config.py:43`, :73) | Needs a non-local lane, which is "the routing tribunal's to add" (`config.py:73-74`). That means L5/L23/L24 are touched while frozen (LAWS:104). It also needs a metered key (L24 rung 3, L41) | Touches no frozen law |
| Build size | New route kind or schema fields (the current schema requires chat-only keys `think_policy`, `max_output_tokens`, `response_format`, :48, :55) and one table with a vector column | Same table, plus a metered credential path, a cost footer and a fallback policy, none of which exist | One table with `tsvector` and a CLI. Smallest |
| Meets F21's test? | Yes | Yes | Likely yes: the answer is literal text in the Ledger ("Stop buffer default = fixed 0.02", `PROJECT-LEDGER.md:326`; also :370, :1791), so a keyword search for "stop buffer" finds it |
| Risk | Embedding model on the host is UNKNOWN (`~/.lmstudio/` is outside the repo, `jobs.yaml:106-107`). Contention: chat calls on the same server queued 60–72 s (`modelaccess.yaml:31-33`) | Outage takes recall down (L23's 08-28 reason, LAWS:181); spend; blocked by the freeze | No recall by meaning; synonyms are missed |

## Decision (default)
**A, staged on C. Never B in Phase 1.**
1. F21 ships FTS first (C) as its floor. The acceptance fact is literal text (`PROJECT-LEDGER.md:326`), so F21 does not wait on vectors.
2. Vectors come from a local embedder on the existing local lane, through `modelaccess` (L5: no out-of-band call). There is one new route, `local.embed`, and no fallback key (`config.py:125-126` stays).
3. The dimension is config, recorded with the model name on every row. The new table lives in the new core. **It does not reuse the four 1536-dim tables**, which stay untouched (TRIAGE KEEP-CONCEPT/REBUILD, `memory-system.md:8`). So the "migration either way" in TRIAGE:43 does not arise.
4. The model is not named here. Which embedding models LM Studio has is UNKNOWN. The F21 card's preflight proves one is loaded and answers on `/v1/embeddings`. If none is loaded, F21 lands FTS-only and vectors become a follow-up card. Cloud is never the substitute.
5. Cloud (B) can come back only by a routing-tribunal ruling that adds a non-local lane (`config.py:73-74`; L25's "by ruling, not by fallback", LAWS:188).

Why: B is blocked by frozen law and by the schema in code. C alone meets the acceptance test but leaves H1/H6 (recall by meaning, the "dream" job) without a base. A costs nothing per call, follows L23, and the staging means F21 never blocks on it.

## Cost and storage (what can be proven)
- Corpus: `PROJECT-LEDGER.md` is 515,281 bytes and 3,765 lines (`wc -c`, `grep -c`). The memory folder is 984 KB on disk (`du -sk`). That is about 1.5 MB of text. The rest of "vault history" has no size proven here (UNKNOWN).
- Vector storage: pgvector stores `vector(n)` as 4·n + 8 bytes (pgvector's published layout, not proven in this repo). That is 6,152 B a row at 1536 dims and 3,080 B at 768. At an ASSUMED 2,000 bytes per chunk, ~1.5 MB is ~750 chunks, so ~4.6 MB of vectors at 1536 dims or ~2.3 MB at 768. **Storage does not decide this.**
- Cloud spend: the token count is ~1.5 MB ÷ ~4 bytes/token ≈ 375k tokens (a heuristic, not measured). The repo carries no price for `text-embedding-3-small`, so cost is UNKNOWN. A for that corpus is $0 marginal (L24 rung 1).
- Local throughput and latency of an embedding model on the host: UNKNOWN (no measurement exists, and the X-E4 numbers at `modelaccess.yaml:31-35` are chat Plan calls).

## Consequences
- `modelaccess` grows a second route shape. The schema change is the routing lane's file ("The routing build extends THIS file", `modelaccess.yaml:12-13`), so the tribunal must say whether a local-only embed route counts as a routing change under the freeze (LAWS:104).
- Embeds share LM Studio with `local.plan` (a voice turn). Embeds must run as a batch job off the voice path, or they starve it (`modelaccess.yaml:31-33`).
- A model swap later means re-embedding the new table only. It is a job, not a migration of the four old tables.
- The "dream" job (R4, Charter:398) and the observation store (O3) inherit this choice.
- The old `OPENAI_API_KEY` embedding path (`postgres.py:745-764`) is not ported.

## What the tribunal must test
1. Does a loopback-only `local.embed` route violate the routing freeze (LAWS:104), or is it inside L21/L23 as already ruled? If it violates the freeze, F21 is C-only until the routing tribunal rules.
2. Is FTS alone enough for the acceptance test? Run the query "why is the stop buffer 0.02" against an FTS index of the Ledger in `cobalt_dev`. Do the top hits include `PROJECT-LEDGER.md:326`/:370/:1791?
3. Is a host embedding model present, and what are its dimension, throughput and p95 on `/v1/embeddings`? These are UNKNOWN today.
4. Contention: do batch embeds delay a `local.plan` call past its 15 s timeout (`modelaccess.yaml:34`)?
5. A new table versus reusing `public.memory_logs`. The default is new. Check grants: the new-core roles have none on `public.*` (`memory-history-2026-09-20.md`, U1).
6. Does the SDK spike (Lane C) change anything here? For example, does the F20 chassis need the same recall index (LADDER:925-928)?
