# Survey: Scribe / memory layer — 2026-10-21

## §0 Headline
- Built and deployed: a search-your-history store (F21 "genesis"): import markdown, search by words, embed for meaning.
- Built and live in the new core: one safe path for writing into the vault notes (vaultwrite).
- The Scribe itself exists only in the old tree (`cobalt_agent`), which still runs; nothing in the new core replaces it.
- The nightly "dream" memory-consolidation job is one sentence in a 09-05 ruling: no design, no code, no owner.

| part | status | proof file:line |
|---|---|---|
| F21 design (two chunks, FTS floor then vectors) | DESIGNED, approved | `docs/30 - Design/F21-ADR-FINAL-2026-10-11.md:37`; approved: `areas/cobalt.md` NOW "APPROVED DESIGNS" |
| F21 chunk 1: `"user".genesis_chunk` table, import, search, CLI | BUILT, deployed | `src/cobalt/db_migrations/0026_genesis_chunk.sql:13`; `src/cobalt/genesis/search.py:1`; `src/cobalt/genesis/cli.py:1` |
| F21 chunk 2: vector column, embed route, `genesis embed` | BUILT, deployed 10-20 (`0e3d45e6`) | `src/cobalt/db_migrations/0028_genesis_vectors.sql:18`; `src/cobalt/genesis/embed.py:1`; `configs/cobalt/modelaccess.yaml:43`; `areas/cobalt.md` NOW line 1 |
| Whether anything has been imported into genesis_chunk in production | UNREAD (no data or run record read) | — |
| Vault write path (L28: marker-bounded, audited) | BUILT | `src/cobalt/vaultwrite/writer.py:1` |
| Scribe class (write note, daily note, search vault) | OLD TREE ONLY | `src/cobalt_agent/skills/productivity/scribe.py:19`; used at `src/cobalt_agent/brain/cortex.py:220` |
| Scribe persona/prompt (Ops department) | OLD TREE ONLY | `src/cobalt_agent/brain/ops.py:18`; `configs/prompts.yaml:60` |
| Old memory module (Postgres, cloud embedder, 1536-dim) | OLD TREE ONLY | `src/cobalt_agent/memory/postgres.py`; embedder calls cited at `F21-ADR-FINAL-2026-10-11.md:12` |
| Old agent still runs the Scribe and memory layer | OLD TREE ONLY | `configs/cobalt/jobs.yaml:133-136` |
| "Dream" consolidation job (nightly + pre-compact flush) | DESIGNED as one sentence; no code | `docs/30 - Design/memory-history-2026-09-20.md:17`, `:148`; `F21-ADR-FINAL-2026-10-11.md:122` ("neither exists in code") |
| Pinned always-loaded memory block, enforced by failing the write | DESIGNED (R4 ruling); new-core enforcement UNREAD | `memory-history-2026-09-20.md:71`; `RESEARCH-2026-09-05-memory-and-capture.md:23` |
| Observation store (O3: who/source/confidence/supersedes) | DESIGNED in option only; no code | `F21-ADR-FINAL-2026-10-11.md:122` |
| Agent-initiated recall (agent calls search on its own) | NONE (search is a CLI; no caller wired) | `src/cobalt/genesis/cli.py:35`; no other `genesis` caller found in the `src` grep |
| A new-core "Scribe" design file | NONE (no file in `docs/30 - Design` names it; `ls` checked) | `docs/30 - Design` listing |
| New-core Scribe code, or a data/config entry naming one | NONE | grep `-w scribe` over `src configs data tests`: only old-tree hits, comments (`src/cobalt/vault.py:38`) and `configs/cobalt/jobs.yaml:136` |

## DECISIONS
- ASK DESK: does the new core get a Scribe, or does the old tree's keep running as is until retirement? Default: keep the old one, write no card until F21 holds real data. [by 18:00 ET 10-21]
- ASK DESK: who owns the "dream" job and when does it get a design? Default: no owner this sprint (S5 stops 10-28); desk raises it at sprint close. [by 18:00 ET 10-21]
- ASK DESK: should recall be wired to a caller (a seat or the desk) before any Scribe work? Default: yes, one card to call `cobalt genesis search` from a seat. [by 18:00 ET 10-21]

## RECORDS
- Surveyed 2026-10-21 12:20 EDT, read-only; one file written, this one.
- Unread: production genesis_chunk contents, `data/` entries beyond the `-w scribe` grep (none matched), `INDEX.md` (its `-w scribe` grep matched nothing).
- The old tree is the main-checkout `src/cobalt_agent/`; the `cobalt-wt` worktrees were listed, not read.

SURVEY DONE · parts: 14 · decisions: 3
