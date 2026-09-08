---
title: Research notes — memory structures, capture pipeline, insight design
date: 2026-09-05
status: research (no rulings beyond the appendix)
destination: docs/30 - Design/
---

# 1. Memory layer (owned, vendor-agnostic)

**Mechanism every runtime shares:** a tiny always-loaded block + a one-line index + files read on demand + search over an archive. claude.ai memory works this way (profile + preferences + index; background write pass). Claude Code works this way (CLAUDE.md loaded in full; auto-memory MEMORY.md first 200 lines / 25 KB; skills on trigger; fixed part cached). Hermes works this way (MEMORY.md ≈2,200 chars + USER.md ≈1,375 chars pinned; SQLite FTS+vector archive; agent-initiated recall; nudge_interval reflection; flush before compaction; write fails at cap). OpenClaw fails by appending raw logs with ~6× the budget and loading them (213 KB per 20 events; 19.6 s recall vs 113 ms).

**Design (Ruling 4):**
```
6 - Permanent/Memory/
  INDEX.md            ← only default load; [[name]] — description — updated
  profile.md
  preferences.md
  people/  topics/  areas/    ← one subject per file, <5 KB ideal, 25 KB cap
  _imports/anthropic-2026-09-05/   ← frozen
```
Budget: INDEX + profile + preferences ≤ ~4K chars, write fails when exceeded. Provenance on every line. Superseded marked, not deleted.

**Consolidation ("dreams"):** capture is deterministic (cards, DRC, rulings as L28 units). Nudge = pre-compact / session-end flush in Code. Dream = nightly beside the archiver + on demand before a compact; conservative (few high-confidence add/replace/remove ops, zero writes is fine); volume-driven cadence. Never every-15-minutes on the trading Mac during RTH.

**Postgres side (F21/S5, not before):** one generic observation store (text, about-whom, source, time, confidence, supersedes, embedding) — concepts as rows, not tables; consolidation job rewrites Cobalt-owned sections through L28 and refreshes INDEX. Retrieval algorithmic (FTS + pgvector); LLM only at synthesis.

**Exposure:** local CLIs read the folder directly (herdr panes); chat models via a remote MCP server — note claude.ai connects from Anthropic's cloud, so the endpoint must be reachable on the public internet behind OAuth (Tailscale alone insufficient). ChatGPT supports remote MCP; Grok unknown.

**Honcho patterns extracted (L15 reference only):** provenance per memory; domain as tag, not partition (IT-security conversation retrievable from a trading question); peers (people/agents/projects) first-class; scheduled consolidation; levels of recall (cheap lookup vs reasoning on "why").

# 2. Chat vs Code as architect's office
Historical reasons for chat: fleet memory + past-chat search (now exported); read-only safety after vault damage. Remaining chat advantages: very long sessions without compaction; phone dictation ergonomics. Code-architect gains: direct vault + Postgres read, role packs as CLAUDE.md, no ferrying (L13), dogfoods F20. Decision: spike (read-only role pack, plan mode, L29, Fable 5.1) on the two-layer ADR. Compact guidance: /compact is one full-context call, but not compacting costs more per turn; cheap path = write state out + /clear between tasks.

# 3. Capture / transcription pipeline (five stages; judge tools per stage)
1. Capture → clean markdown: Obsidian Web Clipper (Defuddle → Turndown; templates with metadata, conditionals, loops; YouTube transcript via Reader mode when the panel is open). Defuddle is open and runs headless. Weak on JS-heavy SPAs; SMB member site and Discord need testing.
2. Interpret at capture: Interpreter on Ollama/local (OLLAMA_ORIGINS for the extension; raise num_ctx or long pages silently fail). Cloud providers metered.
3. Audio/video → transcript: engines whisper.cpp / faster-whisper (MIT), WhisperX (word timestamps + diarization), Parakeet; front-ends Meetily (MIT), Anarlog, OpenWhispr, Vibe, Scriberr, Whishper. Kashef kit = reference instance.
4. Link + structure: frontmatter properties + wikilinks at clip time; Cobalt linker pass afterward (the vault-linking gap).
5. Insight: model over the linked corpus; "every mention of X" = search-plus-crawl agent feeding stage 1.
Use as-is: Web Clipper, whisper engines, one meeting front-end. Build: linker, gather agent, vault ingest via L28. Browser-agent-driven clipper (same steps as the hand, logged in as Dejan, still-frame screenshots, no downloads) is the design class.

# 4. Insight structure (playbook from many pools)
Three layers kept apart:
- **Sources** — clips, transcripts, cheat sheets, posts (user data, provenance).
- **Claims** — atomic statements extracted from sources, one note each in 6 - Permanent with properties (setup, variable, source, confidence), wikilinked to a per-concept hub note ("Big Dog Consolidation"); backlinks aggregate every mention; Obsidian Bases renders property tables for review.
- **Instances** — FILLED cards with feature snapshot at entry (taxonomy variables: regime internals, level significance, RVOL, extension, window) + outcome (R, MFE, exit efficiency). Prerequisite: item 46 trade-note writer.
Insight = claims tested against instances. Other people's playbooks are priors; own data updates them (Bayesian). Every insight carries n; hypothesis until n≥30. This generalizes the 09-01 calibration loop.

# 5. User data vs system data — inputs for the ADR session
System: taxonomy anatomy (regime, range, gap, extension, leg, session clock), card engine, radar, alerts, rules engine schema. User: named trades and trade_defs content (cheat-sheet-derived), strategies/settings, SMB-derived material, DRCs/playbooks/trades/research in 1 - Trading, Oura/psychology, Memory folder. To rule: repo location of trade_defs batches → user layer; two-layer Data-Model ADR; naming pass over taxonomy; how the card engine loads a user's trade_defs at runtime (config path, not code).

# 6. Timeline impact (S1 09-08→09-18)
Memory folder: ~1 h, neutral. herdr: after acceptance. Code-architect spike: neutral if it replaces a chat design session. Two-layer ADR: 1–2 mornings now vs ~a week after S2. Cobalt-side memory: S5 only. Research sessions: attention cost only.

# 7. Next chat — opener (single block)
```
Cobalt design session — memory upgrade + user/system data ADR. Fable 5.1, chat.
Dejan the CTO. CODE FREEZE in force until S1 live acceptance (09-08) passes —
this session produces documents and hand tasks only; any Code prompt it drafts
is parked behind the freeze.
Date: <fill>. Attach: MVP-CHARTER-v0_2.md, PROJECT-LEDGER.md (with the 09-05
research appendix), SPRINT-LADDER-v0_1.md, RESEARCH-2026-09-05-memory-and-
capture.md, TAXONOMY-DRAFT-v0_7.md, trade-defs batches 1+2, kashef-mining-memo.md.
Memory export zips already placed in Think/6 - Permanent/Memory/_imports/.

AGENDA, in order, rulings one at a time:
1. Memory folder: confirm INDEX.md draft, seed living files from the export
   (Claude drafts them as markdown; Dejan places them — no Cobalt code),
   provenance format, ~4K-char budget check.
2. Split: what stays hand work vs Cobalt-side F21/S5 (consolidation job,
   budget enforcement, MCP exposure) — S5 items go to the Ladder, not now.
3. Two-layer Data-Model ADR (user data vs system data): draft the ADR text;
   list the code moves it implies (trade_defs to user layer, loader path,
   naming pass) as a post-freeze Code prompt, model Opus 5, SESSION: fresh,
   auto mode on — parked until acceptance.
4. Code-architect spike plan (read-only role pack, plan mode, L29) and herdr
   two-session /rc test — both scheduled after acceptance.
Short answers. Build-session firewall applies.
```
