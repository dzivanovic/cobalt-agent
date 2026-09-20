---
title: MEMORY — the true history
date: 2026-09-20
status: research (no rulings, no proposals, nothing built or deleted)
seat: research hub `memory-history-0920`, Opus 5, background, read-only
ordered_by: Dejan, 2026-09-20 — `cto-2026-09-20.md` §4 R11
---

# MEMORY — the true history

## §0 Headline

- **The brief's premise is wrong and the error is itself the story.** Production `cobalt_brain` holds **48 tables in 3 schemas** (public 17, system 16, user 15), not "17 tables", and **all five named pillars exist**: `public.memory_logs`, `graph_nodes`, `graph_edges`, `hitl_proposals`, `browser_fast_path`. The "17" is the public schema alone — and that schema *is* the Hippocampus plus the Gemini market-data tables.
- **They exist and they are inert.** Since the Postgres server started 2026-09-05 03:24 UTC: `memory_logs` +15 rows; `graph_nodes`, `graph_edges`, `hitl_proposals`, `browser_fast_path` **+0**. In production logs the old agent booted PostgresMemory **61 times** between 09-05 22:18 and 09-18 08:00 and did exactly one thing each time — re-ran its CREATE TABLE statements. Zero writes logged.
- **It was never reused, and the record says why: one unwritten document.** TRIAGE.md:43 (2026-08-22) — *"Local-vs-cloud embedder ADR **GATES** the memory port."* That ADR is named in the ADR register and **was never written**. Everything in Thread 1 sits behind it. `src/cobalt/` has **no memory module**; its only contact with the five pillars is a frozen do-not-touch list.
- **Thread 2: the path out was designed, dated, and deferred — not forgotten.** `RESEARCH-2026-09-05` copied Hermes's *pinned block + write-fails-at-cap* half and put its *FTS+vector archive + agent-initiated recall* half in "**F21/S5, not before**". Today the block is **3,993 / 4,000** with 7 characters of margin. A path out exists for `preferences.md` (→ `topics/working-contract.md`, 11 KB, used). **For INDEX.md itself there is none, and nothing anywhere searches an evicted line.**
- **Thread 3: "dream" is one sentence, never a design.** Ruled 09-05 (R4), parked at F21/S5, no ADR, no backlog row, no code. The hand substitute ruled 09-15 has been **blocked since 09-17**: `SESSION-CLOSE.md` steps 3–4 order the close hub to write memory, `L58` forbids it — three closes in a row wrote nothing there. **"gzip on a cadence" and "time machine" appear nowhere in seven weeks of record; they were first said on 2026-09-20.**
- **His before/after promise WAS built — and aimed at the wrong tree.** `user.vault_writes` carries `before/after/unit_before/unit_after/hash_before/hash_after`, 1,345 live rows — for *his* vault notes, under L28. The memory folder gets none of it, and that table forgets at **30 days** (the only enforced retention in the system besides a 7-day radar cache and restic's 14/8/12).
- **The number he asked for: 72 % (29 of 40 concrete facts are in memory) — but the average hides it.** cto reports 83 %, closes 87 %, `tribunal-analyst-2026-09-14` **100 %**, `tribunal-routing-2026-09-13` (6 MB, the largest folder) **12 %**. Memory is not uniformly forgetful; it forgets **whatever no close folded**.
- **COVERAGE: swept 24,877 · hit 1,180 · read 671 at line level + 58 in full. This history does NOT sample.** One correction that caused today: `ASSESSMENT.md` §4 ordered CLAUDE.md:95's "5-pillar" wording fixed on **2026-08-22**; 30 days later it is unchanged, and it is what sent the desk looking for five tables that were in front of it.

---

## §1 THE TIMELINE

Every line: date · what happened · who · file:line. Undated claims are in `## Undated` at the end of this section.

### Era 1 — the Gemini build (2026-02-09 → 2026-04-07): everything in Thread 1 was built here

| Date | Event | Source |
|---|---|---|
| 2026-02-09 | **Postgres memory first appears.** "added postgres memory and secure docker stack" | git `8c5c0c1` |
| 2026-02-12 | **"Level 3 Upgrade — RAG Memory (Postgres+Vector)"** — `memory_logs` + embeddings | git `8463874` (cited `01-memory.md` §9) |
| 2026-02-15 | `memory/{base,core,postgres}.py` land in the src layout | git `9a775af` |
| 2026-02-19 | Postgres adapter routed via `POSTGRES_HOST` | git `705344b` |
| 2026-02-23 | **ADR-005 "Agentic RAG — Memory as a Tool" ACCEPTED.** Specifies `memory_logs`, cosine search, **an ivfflat index on `embedding`**, and **three retention rules**: PREFERENCE = keep forever · MARKET CONTEXT = expire after 24 h · SESSION = expire at end of conversation | `docs/_archive/gemini-era-vault-side/.../ADR-005 Agentic RAG.md` |
| 2026-02-23 | **PRD-010 "Continuous Memory System" marked ✅ Implemented.** Names "**the Hippocampus**" and all four tables. Its "Future Enhancements" list: **1. Memory Compression (periodic summarization of old memories) · 2. Contextual Retrieval · 3. Memory Expiration (TTL cleanup)** | `.../Requirements/PRD-010 Continuous Memory System.md` |
| 2026-02-26 | **ADR-011 "The Vector Librarian" ACCEPTED** — `ingest_knowledge.py` embeds `.py`/`.yaml`/`.md`; **"Omni-Memory: leveraged the existing `PostgresMemory` class so that all project files, config playbooks, and historical chat logs reside in the same searchable vector space."** Risk recorded: *"requires continuous updating to prevent stale data retrieval. Mitigation planned via automated background syncs."* | `.../ADR-011 Vector Librarian.md`; git `8c6c5d8` |
| 2026-02-27 | `browser_fast_path` + ivfflat index built ("pgvector fast path") | git `b090110` |
| 2026-02-28 | **ADR-013 "GraphRAG and Watcher Daemon"** built — `graph_nodes`/`graph_edges` in Postgres rather than Neo4j, Universal Extractor, Delta Engine | git `333c2c3`; `.../ADR-013 …md` |
| 2026-03-01 | `hitl_proposals` runtime DDL + persistent HITL approvals | git `cf9cf4f` |
| 2026-03-04 → 03-06 | **The only five rows `hitl_proposals` ever held** were written (all `approved`; browser ×4, write_file ×1) | `01-memory.md` §2 |
| 2026-03-08 07:01 | **The graph is written once and never again** — one AST snapshot of `src/` in a 12-second window: 655 nodes, 610 edges, **every edge `CONTAINS`** | git `37f51ed`; `01-memory.md` §1 |
| 2026-03-18 | **The only row `browser_fast_path` ever held** (Finviz "Morning Up Gapper") | `01-memory.md` H-5 |
| 2026-04-07 | **ADR-015's "5-Pillar Relational Schema" integrated** — `schema.sql`, 13 market-data tables (Entities/Physics/Catalysts/Engine/Execution). **This, not the memory tables, is what "5-Pillar" means.** | git `cc14caa`; `.../ADR-015 …md` |
| 2026-04-07 → 2026-08-21 | **Nothing touches `src/cobalt_agent/memory/` again.** Last commit to the module is `cc14caa` | `git log -- src/cobalt_agent/memory/` |

### Era 2 — the assessment and the gate (2026-08-21 → 2026-08-22)

| Date | Event | Source |
|---|---|---|
| 2026-08-21 | **CLAUDE.md gains the line that caused this job**: *"Memory layer: PostgresMemory ('Hippocampus') — 5-pillar schema (memory_logs w/ 1536-dim embeddings, graph_nodes, graph_edges, hitl_proposals, browser_fast_path)"* — conflating ADR-015's market-data schema with PRD-010's memory tables | `CLAUDE.md:95`, git `6ec3d33` |
| 2026-08-21 | **COBALT-REQUIREMENTS.md** carries the same conflation (*"alongside the existing 5-pillar memory schema"*) and, separately, **INFRA-2: the vault redesign whose structure "serves as Dejan's second brain and Cobalt's second brain combined"** — **this is the sibling, in the canonical requirements** | `COBALT-REQUIREMENTS.md:138`, `:342-350` |
| 2026-08-21 | **Pass 1 forensics on the Hippocampus.** `memory_logs` **871 rows, 2026-02-15 → 2026-08-21, only 18 in the last 30 days**; 835 embedded, including **203 Obsidian-vault chunks + 170 source-code chunks**; **no vector index on `memory_logs`**; graph frozen since 03-08; `FastPathCache`'s vector half a tautology burning one OpenAI call per lookup | `docs/20 - Assessment/01-memory.md` |
| **2026-08-22** | **ASSESSMENT.md §4 "Things to correct in CLAUDE.md (facts found wrong)" orders the conflation fixed**: *"'5-pillar schema with memory_logs…' — memory_logs/graph_\*/browser_fast_path/hitl_proposals come from runtime DDL, the 5-Pillar file is `schema.sql` (13 tables)."* **Never done. Still wrong today.** | `docs/20 - Assessment/ASSESSMENT.md:187` |
| **2026-08-22** | **TRIAGE §2.1 rules every memory component** (10 rows) — `PostgresMemory` core **KEEP-CONCEPT / REBUILD**, `HITLProposalStore` **REBUILD**, `MemoryProvider` **KEEP-AS-IS**, JSON store / `_hilt_` trio / `FastPathCache` / `ingest_knowledge.py` **KILL** | `TRIAGE.md:27-42` |
| **2026-08-22** | **THE GATE.** *"OpenAI embedding call sites \| REDESIGN \| **Local-vs-cloud embedder ADR GATES the memory port** (Req §4 local-first, §8 routing; 1536-dim baked into 4 tables → migration either way)"* | `TRIAGE.md:43` |
| 2026-08-22 | The 5-Pillar schema is **escalated to REDESIGN** — *"Concept itself questioned. Two schema universes (runtime DDL vs schema.sql) … no design rationale ever written."* (The rationale did exist, in the vault-side ADRs above — it had not been read.) | `TRIAGE.md:44` |
| 2026-08-22 | Design-session register names the outputs: **data-model ADR + embedder ADR (gate the memory port)** | `TRIAGE.md:189` |
| 2026-08-22 | `L6` agent north star adopts the **Hermes-agent/BuzzBot/GrokBot** pattern — about *agent architecture*, not memory | `TRIAGE.md:17` |

### Era 3 — the Obsidian memory (2026-09-03 → 2026-09-06)

| Date | Event | Source |
|---|---|---|
| 2026-09-03 | **ClaudeClaw kit filed as L15 reference only, never executed by Code.** (It contains a complete memory architecture: FTS5 + embeddings + salience decay + 5-layer retrieval. Never adopted, never cited in a ruling.) | `_imports/anthropic-2026-09-05/areas/cobalt-product-definition.md:10`; `docs/90 - References/claudeclaw-kit/` |
| 2026-09-04 | *"backup with proven restore first — restic → B2 + SSD, **NOT Time Machine**"* — the only pre-09-20 use of the phrase, and it means the macOS product | `PROJECT-LEDGER.md:651` |
| **2026-09-05** | **RESEARCH-2026-09-05-memory-and-capture.md** — the design document of record. Names **Hermes** explicitly: *"MEMORY.md ≈2,200 chars + USER.md ≈1,375 chars pinned; **SQLite FTS+vector archive; agent-initiated recall**; nudge\_interval reflection; flush before compaction; write fails at cap."* Adopts the pinned-block half. Defers the archive half: *"**Postgres side (F21/S5, not before)**: one generic observation store (text, about-whom, source, time, confidence, supersedes, embedding) — concepts as rows, not tables; consolidation job rewrites Cobalt-owned sections through L28 and refreshes INDEX. Retrieval algorithmic (FTS + pgvector); LLM only at synthesis."* Defines **Consolidation ("dreams")**: *"Dream = nightly beside the archiver + on demand before a compact; conservative … volume-driven cadence."* | `docs/30 - Design/RESEARCH-2026-09-05-memory-and-capture.md` §1 |
| **2026-09-05** | **R4 RULED (Dejan) — the memory home.** INDEX/profile/preferences; **"Always-loaded block ≤ ~4K chars, enforced by failing the write, never truncation"**; provenance on every line; superseded marked not deleted; *"Consolidation ('dream') = Cobalt nightly job + pre-compact flush in Code, volume-driven cadence; **Cobalt-side placement = F21/S5**"* | `PROJECT-LEDGER.md:797` |
| 2026-09-05 | Honcho **PARKED**; patterns kept: provenance per memory, domain as tag not partition, peers first-class, **scheduled conservative consolidation, levels of recall** | `PROJECT-LEDGER.md:808` |
| 2026-09-05 | Timeline ruling: **"Cobalt-side memory = S5, not before."** | `PROJECT-LEDGER.md:822` |
| **2026-09-06** | **R1 DONE — the memory folder is built by hand.** *"always-loaded block **3,993 chars, cap 4,000 held**"*; export frozen at `_imports/anthropic-2026-09-05/` (21 files); *"Cobalt-side (**budget enforcement, consolidation job, pre-compact flush, MCP exposure**) = S5/F21, not before."* | `PROJECT-LEDGER.md:827` |
| 2026-09-05 | **restic backup ARMED** — sources `/Users/cobalt/Vault/Think` + a fresh `cobalt_brain` dump; retention **14 daily / 8 weekly / 12 monthly**; SSD only, **B2 still off — one copy** | `configs/cobalt/backup.yaml` |
| 2026-09-06 | **ADR-0008 two-layer data model** delivered (the data-model half of TRIAGE:189). **The embedder half was not.** | `docs/10 - Decisions/ADR-0008-two-layer-data-model.md`; `PROJECT-LEDGER.md:827` R2 |

### Era 4 — the index fills, the law hardens, the path never arrives (2026-09-12 → 2026-09-20)

| Date | Event | Source |
|---|---|---|
| 2026-09-12 | **L56 ruled** — *"The **Obsidian + Postgres** memory layer in `6 - Permanent/Memory/` is THE memory for every agent; no house keeps a private store."* (Names both; points only at the folder.) | `LAWS.md:292-293` |
| 2026-09-13 | **Mechanism ruling**: LAWS.md becomes the only canonical current law; the ledger is the dated record; the fold is a job at every close | `LAWS.md:16` |
| 2026-09-13 | The ledger tribunal measures the block at **3,864** and records **O23**: adding a LAWS.md pointer line to INDEX would breach the cap. Its rule for a breach: *"**fail the write and report the actual total; never truncate**"* — **no destination for what would have to come out** | `0 - Inbox/tribunal-ledger-2026-09-13/WAKEUP-draft.md:10,:73` |
| 2026-09-13 | **R6 (Dejan): "HITL IS A CONVENTION, NOT A MECHANISM."** The `hitl_proposals` rebuild TRIAGE ordered was never built; *"no code path to `radar screens/lists apply`"*. **OWED.** | `PROJECT-LEDGER.md:1288` |
| 2026-09-13 | The routing tribunal runs: 35 files, **6.0 MB**, in `0 - Inbox/tribunal-routing-2026-09-13/`. Astra R2 never completed (Codex limit); **cross-review OWED**. One incident: the hub ran `git checkout --` on CLAUDE.md and briefly discarded a peer session's work | `.../tribunal-routing-2026-09-13/HUB-REPORT.md` |
| 2026-09-14 | The analyst tribunal runs (1.6 MB). **Its substance is folded into `areas/cobalt-houses.md` the same week.** | `Memory/areas/cobalt-houses.md:42-46` |
| **2026-09-15** | **The chat-side memory is exported and the interim is written down.** `README-PLACE-ME.md`: *"**Why it went stale, and the rule that stops it** — The chat CTO office kept its own memory (Anthropic's), and the session-close write only touched the ledger and LAWS. From 09-15 the close is not complete until the memory folder is updated … **The Cobalt-side nightly consolidation job (F21 / S5) automates it later; until then the close hub does it by hand from the ledger appendix.**"* | `Memory/_imports/anthropic-2026-09-15/README-PLACE-ME.md` |
| 2026-09-15 | `SESSION-CLOSE.md` ruled. **Step 5 is the only eviction rule in the system**: *"the total must stay under 4,000. Over = the close FAILS: trim preferences, **move the cut wording to `topics/working-contract.md`**, re-measure."* | `docs/40 - DevDocs/SESSION-CLOSE.md` step 5 |
| 2026-09-16 | **L58 ruled** — the memory folder and LAWS.md are written **only by the CTO desk, by hand**, until a Cobalt memory command exists. *"**A hub never writes the memory folder or this file.**"* | `LAWS.md:304-306` |
| **2026-09-17 21:48** | **A memory file is destroyed and recovered.** The desk used `Write` on `areas/cobalt.md` having read 14 lines; the file was truncated to its NOW head. **Recovered in 4 minutes from the 21:40 restic snapshot.** Rule added: never `Write` an existing memory file | `Memory/topics/cto-desk.md:62`; `cto-2026-09-17.md:284` |
| **2026-09-17 → 09-19** | **Three closes in a row write nothing to the memory folder.** `SESSION-CLOSE.md` steps 3–4 name the close hub as the runner; L58.7 forbids it. Both cannot be obeyed | `laws-audit-2026-09-20.md` C2; `close-2026-09-18.md:68`; `close-2026-09-19.md` |
| 2026-09-17 | Starter kit written up (generalising the 09-05/06 build). Its §2 prescribes `<MEM>/reports/` — **one dated report per working day inside the memory folder. That folder was never created.** | `docs/40 - DevDocs/prompts/STARTER-KIT-memory-desk.md` |
| 2026-09-18 | Production measured: **`system.bars` 1,330 MB, ≈390,000 new bars a trading day, "no retention, pruning or partitioning"** | `PROJECT-LEDGER.md:1527`; `cto-2026-09-18.md` §25 |
| 2026-09-19 | Close prints the block at **3,993 / 4,000 — "PASS, 7 characters of margin"** | `close-2026-09-19.md` §0 |
| **2026-09-20 06:15–09:26** | The desk's last memory writes: INDEX, LAWS, LAWS-HISTORY, two areas files, then `cobalt.md` + `cto-desk.md` at 09:26 | file mtimes, memory tree |
| **2026-09-20 10:1x** | **R11 — this research ordered.** *"the biggest issue here is not disc clutter, but memory that all houses rely on that is forgetful"*; *"we designed our memory not to ever forget, but it seems like it never actually adds any information to it other than just simple stuff, and on close of CTO desk."* **First recorded use of "time machine" and "gzip on a cadence" for memory.** | `cto-2026-09-20.md` §4 R11 |
| **2026-09-20 (today)** | **R3 "DETACH + cold file, never DROP" is recommended for `bars`** — the exact keep-recent-hot / push-old-to-a-compressed-file shape he wants for memory, designed today for a different table | `docs/30 - Design/bars-lifecycle-brief-2026-09-20.md` §2.2 |

### Undated

- The conflation's *origin*: whether "5-pillar" was applied to the memory tables in conversation before it reached `CLAUDE.md` on 2026-08-21. The two frozen exports do not contain it.
- Which writer produced the 15 `memory_logs` rows inserted since 2026-09-05 (see `## UNVERIFIED` U1/U2).
- PRD-010 is dated `2025-02-23` in its own frontmatter — a year typo; its content matches the 2026-02-23 ADR-005 sprint exactly. Treated as 2026-02-23 above.

---

## §2 THE MATURITY LADDER

Six rungs: **SAID** → **DECIDED** → **DESIGNED** → **BUILT** → **DEPLOYED** → **USED**. `·` = not reached.

### Thread 1 — Hippocampus / graph / vector

| # | Component | SAID | DECIDED | DESIGNED | BUILT | DEPLOYED | USED | Stopped at — and what stopped it |
|---|---|---|---|---|---|---|---|---|
| 1 | `MemoryProvider` ABC | 02-08 | 08-22 KEEP-AS-IS | — | 02-15 | yes | yes (old tree) | **DECIDED** for the new core — never ported. No new-core memory module exists to port it into |
| 2 | `MemorySystem` JSON fallback | 02-08 | 08-22 KILL | — | 02-15 | yes | yes | **USED** — correctly dying in place with the old tree |
| 3 | `PostgresMemory` core / `memory_logs` | 02-09 | 08-22 **REBUILD** | ADR-005 02-23 | 02-12 | yes | **871 rows @08-21; +15 since 09-05** | **DECIDED** for the rebuild — **blocked by the unwritten embedder ADR (row 10)** |
| 4 | Graph memory `graph_nodes`/`graph_edges` | 02-28 | 08-22 (with 3) | ADR-013 02-28 | 02-28 | yes | **once**: 655/610, 2026-03-08 07:01, all `CONTAINS` | **USED-once** — the Universal Extractor never persisted a non-AST entity; 0 inserts since 09-05 |
| 5 | `FastPathCache` / `browser_fast_path` | 02-27 | 08-22 KILL | PRD-010 | 02-27 | yes | **1 row**, 2026-03-18 | **USED-once** — its vector half was a tautology costing one OpenAI call per lookup (`01-memory.md` H-5) |
| 6 | `hitl_proposals` + `HITLProposalStore` | 03-01 | 08-22 **REBUILD** | ADR-007 | 03-01 | yes | **5 rows**, 03-04…06 | **DECIDED** — *"HITL is a convention, not a mechanism … OWED"* (LEDGER:1288, 09-13) |
| 7 | `_hilt_` trio | — | 08-22 KILL | — | 03-01 | yes | **never called** | **BUILT** — dead on arrival, three methods, zero callers |
| 8 | Vector Librarian / `ingest_knowledge.py` ("Omni-Memory") | 02-26 | 08-22 KILL | ADR-011 02-26 | 02-26 | yes | **once**: 203 vault + 170 code chunks | **BUILT** — ADR-011's own mitigation, *"automated background syncs"*, was never built; the index went stale by design |
| 9 | 5-Pillar market-data schema (`schema.sql`) | — | 08-22 **REDESIGN** | ADR-015 | 04-07 | yes | partial (instruments 345, market_snapshots 2,209; 10 of 13 never written) | **DECIDED** — the Data-Model session produced ADR-0008 for the *new* core; these 13 tables were left frozen in `public` |
| 10 | **Local-vs-cloud embedder ADR** | 08-22 | **08-22 (TRIAGE:43, :189)** | · | · | · | · | **DECIDED — and it is the gate.** Rows 1, 3, 4, 5, 8 all wait on it. Only mention in `docs/10 - Decisions/` is the README listing it as still to come |
| 11 | Memory tests → real `cobalt_dev` integration | 08-21 | 08-22 REDESIGN | · | · | · | · | **DECIDED** — the mock-SQL suites TRIAGE called protection-free are still the only ones |
| 12 | ADR-005 retention rules (PREFERENCE / 24 h / session) | 02-23 | 02-23 | **02-23** | · | · | · | **DESIGNED** — no expiry code exists in either tree. Enforced by nobody |
| 13 | ANN index on `memory_logs.embedding` | 02-23 | 02-23 | **02-23 (ADR-005 ivfflat)** | · | · | · | **DESIGNED** — verified absent today; the only vector index in the DB is on `browser_fast_path` (0 rows used) |
| 14 | Memory compression + TTL expiry | **02-23 (PRD-010 "Future Enhancements")** | · | · | · | · | · | **SAID** — and never said again until 2026-09-20 |
| 15 | The sibling: "Dejan's second brain and Cobalt's second brain combined" (INFRA-2) | **08-21** | · | · | · | · | · | **SAID** — the vault-structure ADR on TRIAGE's register was never written |

### Thread 2 — the Hermes-shaped index

| # | Component | SAID | DECIDED | DESIGNED | BUILT | DEPLOYED | USED | Stopped at — and what stopped it |
|---|---|---|---|---|---|---|---|---|
| 16 | The memory home (INDEX + profile + preferences + areas/topics) | 09-05 | **R4 09-05** | 09-05 research | **09-06 by hand** | every session | **USED — 27 files, 265 KB** | **USED.** The one component that completed |
| 17 | The 4,000-character cap, "fail the write, never truncate" | 09-05 | **R4 09-05** | 09-05 | 09-15 as `SESSION-CLOSE.md` step 5 | yes | **USED — 3,993/4,000 measured at every close** | **USED** — as a human procedure. No code enforces it |
| 18 | The path out **for `preferences.md`** → `topics/working-contract.md` | 09-05 | 09-05/06 | starter kit rule 4 | by hand | yes | **USED — 11 KB sitting in it** | **USED.** This is the half he remembers being built — and it was |
| 19 | The path out **for `INDEX.md` itself** | · | · | · | · | · | · | **NOTHING.** Never said, never designed. INDEX is the only index; a pointer removed from it points nowhere |
| 20 | Retrieval over evicted content (Hermes's FTS + vector archive, agent-initiated recall) | **09-05** | **09-05 — "F21/S5, not before"** | · | · | · | · | **DECIDED-DEFERRED.** The deferral is explicit and dated. It has not moved in 15 days |
| 21 | The generic observation store (text, about-whom, source, time, confidence, supersedes, embedding; FTS + pgvector) | 09-05 | 09-05 | **09-05 research §1** | · | · | · | **DESIGNED** — one paragraph, no ADR, no backlog row, on no sprint |
| 22 | MCP exposure of the memory folder to chat models | 09-05 | 09-05 (F21/S5) | 09-05 (noted: needs public OAuth, Tailscale insufficient) | · | · | · | **DECIDED-DEFERRED** |

### Thread 3 — dreaming, pruning, compression, a time machine

| # | Component | SAID | DECIDED | DESIGNED | BUILT | DEPLOYED | USED | Stopped at — and what stopped it |
|---|---|---|---|---|---|---|---|---|
| 23 | The "dream" consolidation job (nightly + pre-compact flush) | 09-05 | **R4 09-05** | · | · | · | · | **DECIDED.** One sentence in R4 and its copies. No ADR, no design doc, no backlog row, no code. Placed at F21/S5 |
| 24 | Hand consolidation at close (the declared interim) | 09-15 | **09-15** | `SESSION-CLOSE.md` steps 3–4 | 09-15 | 09-15 → 09-17 | **USED then BROKE** | **DEPLOYED-then-blocked.** L58.7 forbids the hub to write the folder that steps 3–4 tell it to write. 3 of 3 closes since 09-17 wrote nothing |
| 25 | **F21 Genesis import** (ledger + vault history into `cobalt_brain` through the memory pipeline) | 08-28 charter | **ratified, on the ladder S5 = 2026-10-15 → 10-28** | acceptance test written (*"Cobalt answers 'why is the stop buffer 0.02' from the imported record"*) | · | · | · | **DECIDED.** **It consumes "the memory pipeline" and no sprint builds one.** F21 is the ladder's ONLY memory line |
| 26 | Pruning / condensing after consolidation | **09-05** ("conservative … add/replace/remove ops, zero writes is fine") | · | · | · | · | · | **SAID** |
| 27 | Compression / gzip on a cadence over the tree | **2026-09-20** | · | · | · | · | · | **SAID — today, and nowhere before.** Zero occurrences in 24,877 files |
| 28 | "Time machine": last month fresh in the index, index → deeper archive | **2026-09-20** | · | · | · | · | · | **SAID — today.** The *restore* half exists (row 29); the *index into it* was never said before today |
| 29 | Restic snapshots over the whole vault (incl. the memory folder) | 09-04 | 09-04 ("restic → B2 + SSD, NOT Time Machine") | `configs/cobalt/backup.yaml` | 09-05 | yes | **USED — it restored `areas/cobalt.md` on 09-17** | **USED.** 14 daily / 8 weekly / 12 monthly. **One copy: B2 still off.** A restore path, not a retrieval path |
| 30 | **Before/after state on any file change** | 08-21 | L28 | ADR-0004 | **built** | yes | **USED — `user.vault_writes`, 1,345 rows, `before`/`after`/`unit_before`/`unit_after`/`hash_before`/`hash_after`** | **USED — aimed at the human vault's marked units, not at the memory folder. And it forgets at 30 days** (`vaultwrite/store.py:247-256`, purged by `writer.py:453`) |

**TOTALS — 30 components tracked.**

*Highest rung ever reached* (did it ever actually get used?): **reached USED 14** (rows 1,2,3,4,5,6,8,9,16,17,18,24,29,30) · reached BUILT but never used 1 (row 7, the `_hilt_` trio — three methods, zero callers) · reached DESIGNED 3 (12,13,21) · reached DECIDED 6 (10,11,20,22,23,25) · reached SAID only 5 (14,15,26,27,28) · **reached nothing at all: 1 (row 19, the path out of INDEX.md — never said, never designed, does not exist).**

*Where each one stopped and stands today* — this is the harder number: **exactly three of the thirty are doing memory's job today — rows 16, 17 and 18**, the memory home, the 4,000-character cap and the `preferences → working-contract` path out. All three are hand-maintained by one seat. All three live inside the 4,000-character block. Of the other eleven that ever reached USED: five are Gemini-era and frozen (3,4,5,6,8), two are correctly dying in place with the old tree (1,2), one is partial and frozen (9), one worked for two days and is blocked (24), and two work but point at something other than the memory folder (29 restic, 30 `vault_writes`).

The six buckets sum to thirty: USED 14 + BUILT-never-used 1 + DESIGNED 3 + DECIDED 6 + SAID 5 + nothing 1.

**Counting the way the brief asked: reached USED 14 · stopped at SAID or DECIDED 11 · stopped at DESIGNED 3.**

---

## §3 THE CROSS-REFERENCE

**Q: Was the Obsidian memory ever meant to REPLACE Hippocampus, or to SIT BESIDE it? — He is right. The record says SIBLING, every time it says anything, and it never once says replace.**

| Date | What the record says | Reading |
|---|---|---|
| 2026-02-26 | ADR-011: *"**Omni-Memory**: leveraged the existing `PostgresMemory` class so that all project files, config playbooks, and **historical chat logs** reside in the same searchable vector space"* — and it ingested **203 Obsidian-vault chunks** | The sibling was not only planned, **it was briefly real**: the vault was in the vector store in February |
| 2026-08-21 | `COBALT-REQUIREMENTS.md` INFRA-2: the redesigned vault *"serves as **Dejan's second brain and Cobalt's second brain combined**"* | Sibling, in the canonical requirements |
| 2026-09-05 | Research §1 puts the Obsidian folder and *"the Postgres side (F21/S5)"* in **one design, two tiers** — folder = hot/pinned, Postgres = the searchable archive | Sibling, explicitly, with the Postgres tier dated |
| 2026-09-12 | `L56`: *"The **Obsidian + Postgres** memory layer in `6 - Permanent/Memory/` is THE memory for every agent"* | **Sibling in the law's words, single-tier in the law's path.** The one sentence where the two readings collide |
| never | No ruling anywhere says the folder replaces the Hippocampus | Searched: 24,877 files |

**Where the threads agree.** All three name the same missing piece from three directions: Thread 1 wants a searchable store beside the folder; Thread 2 wants somewhere for an evicted line to go; Thread 3 wants somewhere to put a condensed day. **They are one component — row 21, the generic observation store — designed once on 2026-09-05 and never built.**

**Where they duplicate.** Rows 12, 14, 26 and 27 are the same idea said four times across seven months (ADR-005 retention 02-23 · PRD-010 compression 02-23 · R4 "conservative ops" 09-05 · gzip 09-20). **Each time it was recorded as a future enhancement; none ever got an owner or a date.** That repetition is itself evidence of the forgetfulness he named — the system re-derived the same requirement four times because the first three were not reachable.

**Where they contradict.**
1. **L56 vs practice.** L56 says the memory is "Obsidian + Postgres". The Postgres half exists, has 871+ rows, and **no role used by the new core can read it** — `public.*` is owned by role `cobalt` with no grants to `cobalt_system`/`cobalt_user`. The law names a component the system cannot reach.
2. **L58 vs `SESSION-CLOSE.md`.** Ruled 09-16 and 09-15 respectively, one week apart, in direct collision (`laws-audit-2026-09-20.md` C2). Practice follows L58; the consequence is that the close — the one moment the day's material is in one place — is the one actor forbidden to write it down.
3. **`CLAUDE.md:95` vs the database, since 2026-08-22.** The correction was ordered and never applied. Every house wakes up on that line.

**The mind-change, dated.** Nobody changed their mind. **On 2026-09-05 Dejan's own ruling (R4) deferred the Postgres sibling to F21/S5**, and on 2026-09-06 R1 restated it. The sibling was not abandoned — it was scheduled for 2026-10-15, and the schedule is still standing. What was never noticed is that **F21 assumes a pipeline that no sprint builds**.

---

## §4 THE HOLES — every promise not kept, ordered by what it costs today

| # | The promise | Ruling / date | What was done instead | What it costs today |
|---|---|---|---|---|
| **H1** | **A retrieval path for anything outside the 4,000-character block** (Hermes's FTS+vector archive, agent-initiated recall) | 09-05 research; deferred F21/S5 by R4 | Nothing. `INDEX.md`'s one-line descriptions **are** the retrieval layer: a future session reads 35 lines and guesses which file to open | **The forgetfulness itself.** 6 MB of routing tribunal is 12 % recalled; 20 MB of reports/prompts/inbox are unsearchable by any agent |
| **H2** | **The close writes the day into memory** | 09-15 `README-PLACE-ME.md` + `SESSION-CLOSE.md` steps 3–4 | **L58.7 forbids the hub to do it.** 3 of 3 closes since 09-17 wrote nothing; the desk must redo it by hand later | Exactly his sentence: *"it never actually adds any information to it other than … on close of CTO desk"* — and worse, the close is structurally barred from it |
| **H3** | **The embedder ADR, which gates the memory port** | TRIAGE:43, 08-22 | Never written. The ADR README still lists it as "to land" | **Rows 1, 3, 4, 5, 8 are all frozen behind one unwritten document.** The whole of Thread 1 is blocked on a decision nobody has been asked to make |
| **H4** | **F21: ledger + vault history into `cobalt_brain` "through the memory pipeline"** | Charter §3, ratified; ladder S5 2026-10-15 → 10-28 | Scheduled. **No sprint builds the pipeline it consumes.** F21 is the ladder's only memory row | The reconstruction he is asking for is already on the ladder in four weeks — resting on nothing |
| **H5** | **Correct `CLAUDE.md:95`'s "5-pillar" wording** | `ASSESSMENT.md` §4, **2026-08-22** | Never done; unchanged for 30 days | **It caused this investigation.** Every house wakes on a false statement about its own memory |
| **H6** | **The "dream" consolidation job** | R4, 09-05 | One sentence. No ADR, no design, no backlog row, no code, no owner | The day's material is structured by hand or not at all |
| **H7** | **Memory retention: PREFERENCE keep-forever / MARKET CONTEXT 24 h / SESSION expiry** | ADR-005, 2026-02-23 | Nothing. `memory_logs` has **no expiry, no dedup, no ANN index** | The store that was meant to be curated is an undifferentiated 871-row grab-bag of system logs, code chunks and chat turns |
| **H8** | **Before/after state on any file change or update** | L28 / ADR-0004 | **Built and running — for the human vault's marked units.** The memory folder is written with `Write`/`Edit` by hand and produces **no before/after row at all** | The one file class where a bad write already destroyed content (09-17) is the one class with no diff record. Restic's 14 dailies are the entire safety net |
| **H9** | **`<MEM>/reports/` — one dated report per working day, inside memory** | Starter kit §2, 09-17 | Never created. Reports live in the repo at `docs/40 - DevDocs/reports/` (3.4 MB, 121 files) | The memory folder has no record of the days; it has only the conclusions someone hand-copied |
| **H10** | **The sibling: "Dejan's second brain and Cobalt's second brain combined"** | INFRA-2, `COBALT-REQUIREMENTS.md`, 08-21 | The vault-structure ADR on TRIAGE's register was never written | The combined second brain remains two separate brains, one of which is unreadable by the other |
| **H11** | **`ingest_knowledge.py`'s "automated background syncs" to stop stale retrieval** | ADR-011, 02-26 | Never built | The 203 vault chunks and 170 code chunks in `memory_logs` are a February photograph of a tree that has changed completely |
| **H12** | **Any retention anywhere else** | — | Three rules exist, all enforced by code: `vault_writes` 30 d · radar cache 7 d · restic 14/8/12. **Nothing else has one** | `system.bars` 1,372 MB and +390k rows a trading day; `docs/` 1,229 files; the vault inbox 11 MB — all growing forever, enforced by nobody |

---

## §5 RECONSTRUCTION — OPTIONS WITH COSTS

**Nothing here is a decision.** Five options, priced. They compose; they are not exclusive.

### The question each one answers
A fact is *reachable* when an agent that does not already know it exists can find it from a question. Today exactly one mechanism makes a fact reachable: **a human wrote a one-line description into a 35-line INDEX.** Everything below is a second mechanism.

| | **O1 — Fix the two laws** | **O2 — An index file per corpus** | **O3 — The observation store as designed (row 21)** | **O4 — Cold-tier the corpora** | **O5 — Re-point the before/after record** |
|---|---|---|---|---|---|
| **What it is** | Resolve L58 vs `SESSION-CLOSE.md` (H2) and correct `CLAUDE.md:95` (H5). No build | A committed `INDEX.md` per corpus (`reports/`, `prompts/`, `0 - Inbox/`) — one line per artifact: date, what it settled, whether memory holds it. Hand- or job-written | Build the 09-05 design: one table (text, about-whom, source, time, confidence, supersedes, embedding), FTS + pgvector, a `cobalt memory` command, grants to `cobalt_system` | `bars`'s R3 shape applied to documents: last N days hot in the tree, older `tar`'d to a cold file, the index keeps the pointer | Extend L28's `vault_writes` to cover `6 - Permanent/Memory/` and drop the 30-day purge for that class |
| **Answers** | H2, H5 | **H1 partially**, H9 | **H1, H3, H4, H6, H7, H10** | H12, the disc-clutter half he said is *not* the issue | **H8** |
| **Cost** | One ruling and one commit. Hours | ~1 chunk for a generator + the hand pass on 121 reports / 272 prompts / 181 inbox files. Days, mostly reading | **The largest.** Needs the embedder ADR first (H3), then a schema, a writer, a retriever, a CLI, grants, tests. Two sprints at the ladder's current rate, and it is what F21 (S5) already assumes | 1–2 chunks. Deterministic, reversible | Small: the write path exists; it is a caller and a retention exemption |
| **Cost of being wrong** | Near zero — both are reversible edits | Low. A stale index line is a wrong pointer, not a lost file | High if the embedder choice is wrong: **1536 dims are baked into 4 live tables**; changing it is a migration either way (TRIAGE:43 said exactly this) | Low with `DETACH`-to-file semantics, as today's bars brief argues; **never** `DROP` | Low. Worst case the table grows; it is text |
| **What it does NOT fix** | Nothing becomes searchable | Nothing is *searched*; a human still reads an index | Does not fix the closes (O1) or the before/after gap (O5) | Does not make anything reachable | Does not make anything reachable |
| **Earliest honest date** | Today | This week | Gated on the embedder ADR; S5 at the earliest, and F21 already occupies that slot | Any time | This week |

**Three observations he should have before choosing, not as advice but as fact.**
1. **O3 is already scheduled.** F21 sits in S5 (2026-10-15 → 10-28) and its acceptance test is precisely a reachability test — *"Cobalt answers 'why is the stop buffer 0.02' from the imported record."* The decision may be less "build a memory layer" than "**F21 has no foundation; does the foundation go in front of it or inside it?**"
2. **The gate is one document, not one sprint.** H3 is an ADR, not a build. Nothing in Thread 1 can start until local-vs-cloud embedding is ruled, and that ruling is a morning's work that has been outstanding for 30 days.
3. **O1 is free and it is the one he actually complained about.** *"it never adds any information … other than on close"* is, mechanically, L58.7 colliding with `SESSION-CLOSE.md` steps 3–4. That collision is 4 days old and has already eaten three closes.

**What the three threads look like closed.** Thread 1 closes when the embedder is ruled and the new core has a grant and a module (O3). Thread 2 closes when an evicted line has a destination *and* something searches it (O3 + O2). Thread 3 closes when a job writes the day and a cold tier holds the rest (O3 + O4), with O5 giving every memory change a diff. **O1 and O2 are reachable this week and require no new machinery; O3 is the real answer and it has a prerequisite that is a document.**

---

## UNVERIFIED

- **U1 — Exact row counts, oldest and newest row for the five pillars.** The sanctioned read path's roles (`cobalt_system`, `cobalt_user`) have **no grant** on `public.*`, which is owned by role `cobalt`. Estimates used above are `pg_class.reltuples` (`memory_logs` 743, `graph_nodes` 655, `graph_edges` 610) and the 2026-08-21 assessment's exact counts (871 / 655 / 610 / 5 / 1). Settles it: `docker exec -i cobalt_memory psql -U cobalt -d cobalt_brain -c "SELECT count(*), min(timestamp), max(timestamp) FROM public.memory_logs"` and the same for `graph_nodes`, `graph_edges`, `hitl_proposals`, `browser_fast_path`.
- **U2 — What the 15 rows inserted into `memory_logs` since 2026-09-05 03:24 UTC contain, and which writer produced them.** Settles it: `docker exec -i cobalt_memory psql -U cobalt -d cobalt_brain -c "SELECT timestamp, source, left(content,120) FROM public.memory_logs ORDER BY timestamp DESC LIMIT 20"`.
- **U3 — Whether `pg_stat` counters were reset by hand since the 2026-09-05 postmaster start.** `SELECT stats_reset FROM pg_stat_database WHERE datname=current_database()` returned **empty**, which I read as "never since start"; a hand reset would also present this way. All "+N since 09-05" figures above depend on this reading.
- **U4 — Whether `main.py:54-55`'s two boot markers still write on every old-agent start.** `add_log` logs nothing on success, so the 61 logged boots prove DDL, not writes. Settled by U2's content read.
- **U5 — Whether the `mattermost` database holds anything memory-shaped.** Not inspected: it is a product database with its own recovery story (ADR-0006) and `cobalt db query` cannot reach it. Settles it: `docker exec -i cobalt_memory psql -U cobalt -d mattermost -c "\dt"`.
- **U6 — Anything said in chat between 2026-08-21 and 2026-09-15 that never reached a file.** The two frozen `_imports` exports are the only verbatim record and neither mentions Hippocampus, pgvector, graph memory, dreaming or eviction. **No command settles this.** If the sibling was discussed in chat before 09-05, that discussion is gone.
- **U7 — `docs/90 - References/assets/`** (licensed material, local-only, never committed) was not swept, per CLAUDE.md. It is reference material, not project record.

## What I could not read

- **The five pillars' rows** — permission denied for both new-core roles (U1, U2). Everything I state about their *contents* comes from the 2026-08-21 assessment, which read them directly; everything about their *activity since 2026-09-05* comes from `pg_stat_all_tables` and production logs.
- **`pg_database_size()`** — `InsufficientPrivilege: permission denied for database cobalt_brain`. Table-level sizes were readable and are used instead.
- **Twenty-one files over 400 KB were excluded from the line-level read**, by name: 5 Obsidian plugin bundles (`dataview`, `excalidraw`, `quickadd`, `templater`, `get-stock-information` — third-party JS); 5 tribunal capture artefacts (`tribunal-ledger-…/rounds/astra-r1-capture.md`, `astra-r1-citation-audit.json`, `tribunal-routing-…/astra/EVIDENCE-INDEX.txt`, `astra/source-cache.json`, `rounds/astra-r2-capture.log`); 2 `_archive/captures` review transcripts; 2 Finviz HTML page dumps; 5 log files (`archiver.err`, `aset.err`, `radar.err`, `manual_backfill_20260903.log`, `mattermost_session.log`); `uv.lock`; `cobalt_context.txt` (the stale February snapshot CLAUDE.md warns about). **Each of the seven substantive ones was then grepped separately for the core pattern; all hits were quotations of `CLAUDE.md:95` or `placement.py`'s table list — nothing new.** `mattermost_session.log` was analysed in full for `cobalt_agent.memory.postgres` lines (the 61-boot finding).
- **`venv/`** — 22,110 third-party library files inside the desk's 23,969 count. Swept by the wide pattern; not read. The substantive project corpus is **1,859 files**.
- **The Phase-A hit list was not committed as a file.** The seat line permits exactly one committed file and this is it; the full accounting is below and the lists are in the job's scratch directory.

### Coverage, as hard numbers

| Measure | Count |
|---|---|
| Files swept | **24,877** — project 23,969 (of which `venv/` 22,110; substantive 1,859) + vault `Think/` 908 (memory tree 55, a subset) |
| Files hit, wide pattern (26 terms incl. `index`, `archive`, `vector`, `snapshot`) | **1,180** — project 938 (excl. `venv/`, `data/`), vault 242, of which memory tree 20 |
| Files hit, core pattern (19 memory-specific terms) | **671** — project 527, vault 144 |
| Files read at line level (every core hit, every matching line) | **671** → 1,321 distinct matched contexts, all reviewed |
| Files read in full or by targeted multi-line section | **58** |
| Databases inspected | **4** — `cobalt_brain`, `cobalt_dev`, `mattermost` (catalog only), `postgres` |
| Tables inspected | **17 of 17** named in the brief; **77 in total** (cobalt_brain 48 = public 17 + system 16 + user 15; cobalt_dev 29, no `public` schema at all) |
| Timeline events | **38 dated (several spanning a range) + 3 undated** |
| Components tracked | **30** |
| Reached USED | **14** (doing memory's job today: **3**) |
| Stopped at SAID or DECIDED | **11** (5 SAID + 6 DECIDED) · at DESIGNED **3** · at BUILT-never-used **1** · at nothing at all **1** |
| Holes | **12** |
| Memory hit rate on sampled reports | **72 %** (29/40) — cto 83 %, close 87 %, analyst tribunal 100 %, routing tribunal **12 %** |

**A note on method that matters.** The shell's `grep` in this environment is a wrapper that passes `--ignore-files`, so it honours `.gitignore` — and `docs/*` is gitignored by carve-out here. The first sweep silently skipped it. Every count above was produced with `/usr/bin/grep`. A sweep run with the wrapper would have reported clean coverage of a tree it never opened.

---

MEMORY HISTORY READY · swept: 24877 files · hits: 1180 · read: 671 · tables: 17/17 · timeline events: 38 · components tracked: 30 · reached USED: 14 · stopped at SAID/DECIDED: 11 · holes: 12 · memory hit rate on sampled reports: 72% · UNVERIFIED: 7
