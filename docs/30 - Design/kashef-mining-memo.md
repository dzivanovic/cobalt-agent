# Kashef / ClaudeClaw Blueprint — Mining Memo
2026-08-28 · Doctrine: patterns in, philosophy out. Postgres spine retained. No war room (one-throat law). Source: blueprint kit in `90 - References/kashef-blueprint/` (REBUILD_PROMPT_V2 knowledge base = densest source; Power Packs + visual guide = implementation reference for the design sessions).

## ADOPT — accelerants (mapped to our register)

1. **Agent SDK as the agent chassis** — THE accelerant. Pattern: `@anthropic-ai/claude-agent-sdk` spawns the `claude` CLI as subprocess; per-agent session IDs persisted in DB keyed `(channel, agent_id)`; `resume` continues threads; `maxTurns` caps runaway loops; per-agent `CLAUDE.md` + working dir + MCP allowlist from `agent.yaml`. Direct mapping: our chief-of-staff + specialist departments (OrchestratorEngine / BaseDepartment / Cortex — all KEEP-CONCEPT/REBUILD) largely collapse into SDK sessions + config. Per-agent CLAUDE.md IS our role-pack charter, executable. `agent.yaml` IS anti-rigidity config-driven agents. Session store moves to Postgres. Runs on the existing Max subscription (no API metering for these agents). ToS: kit cites April 2026 Anthropic guidance — personal local tools wrapping Claude Code/SDK are fine on subscription; banned = extracting OAuth tokens. VERIFY at spike, don't vibe.
2. **Hive mind** — shared actions table `(agent_id, action_type, summary, metadata JSON, created_at)`; agents log significant actions, read peers' context, avoid duplicate work. Trivially portable to Postgres. Solves cross-agent awareness without message-bus complexity.
3. **Delegation syntax** — `@research: <task>` from the chief-of-staff channel. Our Mattermost DM inherits this UX: Dejan talks to CoS only; CoS delegates; specialists reachable directly for debugging.
4. **Memory v2 mechanisms → Data-Model session input** (on OUR Postgres+pgvector, not SQLite): LLM-extracted facts w/ importance (store only >0.5) + salience; dedup-by-cosine (>0.85 = merge not insert); 5-layer retrieval (vector ≥0.3 / FTS keyword / recency×importance / hive mind / conversation turns); 30-min consolidation job w/ contradiction detection; importance-weighted decay + pinning; supersession pointers; relevance-feedback loop scoring whether injected memories helped. Note for embedder ADR: kit uses Gemini 768-dim — reinforces that dimension is a swappable choice, not 1536-forever.
5. **Exfiltration guard** — regex scanner (15+ patterns: sk-/AKIA/JWT/hex/base64/url-encoded secrets, .env dumps) on EVERY outbound message before it reaches any channel; match → [REDACTED] + audit-log row. NEW for us, cheap, and after the vault-dump incident exactly in-theme. Adopt as a Cobalt outbound filter in front of Mattermost/dashboard posts. Backlogged: security layer, small.
6. **maxTurns cap** on every agent loop (their default 30) — codifies our 3-tries/runaway-guard instinct as a hard parameter.
7. **Cost footer** — per-response model+tokens+cost display modes. The instrument-what-you-constrain law made visible. Cheap adopt in the usage-ledger work.
8. **Kill phrase** — chat-level emergency stop (SIGTERM all services). Guardian-adjacent, one evening, optional.
9. **Message classifier** (simple msgs → cheaper model, opt-in) — matches our tiering doctrine; fold into routing design.

## VOICE (post-MVP reference, not now)
- Target experience validated: conversational CoS (their Gemini Live mode: audio→Gemini STT+reasoning+TTS streamed back; auto-routing). Alternative legacy chain: Deepgram STT → router → Claude Code → Cartesia TTS.
- **agent-voice-bridge pattern** is the integration seam worth keeping: Python voice pipeline (Pipecat, typed Frames, VAD) spawns a thin Node CLI that calls the SDK and returns JSON on stdout — voice rides on top, agents unchanged underneath. Their fallback chain (ElevenLabs→Gradium→Kokoro→`say`) validates our Kokoro-local plan.
- One-throat law holds: no war room, no multi-agent theater; voice talks to CoS only.

## REJECT / ALREADY-OURS
SQLite (Postgres stays) · Telegram (Mattermost stays) · single-file HTML dashboard (Obsidian mission control ruled) · meeting bot / Pika avatars / WhatsApp bridge (no requirement) · GoT personas · 20-agent sprawl (fleet stays small, role-packed) · PIN/idle-lock/chat-allowlist (superseded by Tailscale + Mattermost auth + vault + HITL — our stack is categorically heavier because it must be).

## THE SPIKE'S QUESTIONS (Agent SDK runtime evaluation — scheduled at orchestrator design, post-slice-2)
1. **HITL integration**: kit runs `bypassPermissions` (safe for a personal assistant; NOT acceptable wholesale for Cobalt). Question: can SDK permission modes / hooks route risky tool calls into OUR tokenized HITL card flow while leaving jailed reads free? This is the make-or-break question.
2. **Local-model backend**: can SDK sessions ride the local Qwen (ANTHROPIC_BASE_URL → LiteLLM proxy → mainframe) per session? If yes: session-per-agent + appropriate-intelligence-per-task (Phase-1 rule) on one chassis — Dejan's harness-rides-local-LLM idea confirmed viable.
3. **ToS verification** with current Anthropic terms (kit's April-2026 citation re-checked).
4. **Failure surface**: what does fail-loud look like when a session dies/times out (their 15-min AGENT_TIMEOUT + PID lock patterns as starting points)?
Phase-1 standing rule applies: appropriate intelligence for appropriate task, local when available; hot-swap purity is Phase 2 and never blocks progress.
