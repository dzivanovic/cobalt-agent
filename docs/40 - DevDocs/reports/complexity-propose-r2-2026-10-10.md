# Complexity routing proposal r2 (Grok shadow trial) · drafter report · 2026-10-10

## §0 Headline
- Proposal written to `reports/complexity-routing-proposal-r2-2026-10-10.md`, for the model tribunal: Astra, Gemini and the blind Anthropic seat, with Grok's self-tier ruling recorded apart.
- Shadow cards are `strike-fallback-env` (LOW 2), `radar-display-fix` (MID 5) and `s4-p1` (HIGH 13). Each is rebuilt by Grok 4.7 on a `shadow/` branch that is never merged and checked by CHECK-HUB unchanged. The primary figure is the Opus check's own held findings: 1 / 2 / 2 on the originals.
- Gate seat: a fresh Opus 5.5 running BUILD-HUB's allow list plus the standing `Bash(grok *)`, in `dontAsk` mode. It writes no code.
- R411 STOP: the gate seat needs a new fixed file (`SHADOW-HUB.md`) and a new launcher kind (`desk-launch.sh shadow`). The trial cannot launch until a card builds them.
- n=3 is insufficient data (L8). Grok token cost is UNKNOWN (its session summaries have no token field). Dollars: $0.

## DECISIONS
1. ASK DESK: the gate seat must be a write-path launch in `dontAsk` mode. `desk-launch.sh prompt` allows only `auto` and `plan` (`desk-launch.sh:454-457`), and no fixed file exists for this seat. A new `SHADOW-HUB.md` plus a `desk-launch.sh shadow <card>` kind is a new command (R411, `cto-2026-10-05.md:107`). Default taken: the proposal names the need in §3 and stops there. A drafter card for SHADOW-HUB plus the launcher kind goes to the desk, and the tribunal can rule on the design meanwhile (S11). [15:03 EDT]

## RECORDS
- `reports/complexity-routing-proposal-2026-10-10.md`: whole. §1 data, §2 score, §5 trial and §8 Q1–Q8 are carried (proposal r2 S10).
- `reports/complexity-propose-2026-10-10.md`: whole. Its method and its five decisions stand.
- `reports/brain-direction-2026-10-02.md:186-198`: `## RULED 2026-10-10`, read in full.
- `reports/cto-2026-10-10.md:10-12`: R921, R920, R919 HIS RULING · APPROVED.
- `LAWS.md:203-207` (L29), `:269-271` (L47), `:337-351` (L67, including `:347` R919, `:348` R920, `:349` R921, `:346` R908), `:360-361` (L70), `:321` (standing house strings), `:355` (L68 GATE EARLY).
- `prompts/BUILD-HUB.md:9-14`: LAUNCH (0), the line, 26 allow and 4 deny.
- `prompts/CHECK-HUB.md:22-23`: house B and seat order. `:91`: the Grok seat line.
- `ops/grok-sandbox.toml`: the `cobalt-job` profile.
- `~/.claude/ops/desk-launch.sh:308` (kinds), `:410-544` (the prompt kind's mode and write-string gates), `:732-757` (card fields).
- `reports/cto-2026-10-05.md:107`: R411. `reports/ops-hand-draft-2026-10-10.md:17`: precedent for a fixed file plus a launcher kind.
- `strike-fallback-env-check-2026-10-10.md`: `:16` card committed, `:41` build tokens, `:124-139` findings and runs, `:223` stop line.
- `radar-display-fix-check-2026-10-08.md`: `:16`, `:42`, `:158-163`, `:246`.
- `s4-p1-check-2026-10-09.md`: `:18`, `:45`, `:129-167`, `:279`.
- `stop-guard-g7-check-2026-10-09.md`: `:140-168`, `:223` (Grok's held record as a checker).
- Cards `2026-10-09/215-strike-fallback-env-card.md:1-9`, `2026-10-08/118-radar-display-fix-card.md:1-14` and `2026-10-06/72-s4-p1-card.md:1-14`: BASE, HOUSE B, rows and seam.
- `~/.grok/sessions/%2FUsers%2Fcobalt%2Fcobalt-wt%2Fagy-trial/01a126f9-a5cc-7863-a83d-16fabc0d0ca0/summary.json`: no token field, `reasoning_effort: medium`, `sandbox_profile: cobalt-job`.
- UNKNOWN (L70): `radar-display-fix`'s check red commit (not read; the gate seat reads it at launch); Grok tokens per call; gate-seat tokens (modelled at 300–450k for three).
- No commit, launch, DB or production command was run. Two files were written: the proposal, then this report.
COMPLEXITY R2 PROPOSAL DRAFTED · decisions: 1
