# VOICE v3 — DRAFT REPORT (2026-09-23)

Seat `voice-v3-draft-0923` · `claude-opus-5-5` · prompt `prompts/2026-09-23/12-draft-voice-v3.md` · started 07:24 ET, proposal written 07:3x, prompts 07:3x, report 07:39 (times from `date`, L48).

## §0 Headline

- Proposal: `docs/30 - Design/VOICE-v3-proposal-2026-09-23.md` (31,958 B). One press-to-talk widget; local STT; ONE local-model call per turn returning a typed plan; code resolves note, trade/card, field and value; confirm by code-matched "yes" or tap; the owning expert writes; audio deleted at transcription.
- Tribunal prompts: `13` hub (Grok + Gemini), `14` Anthropic seat (Opus 5.5, R109), `15` derive (Opus 5.5, R109). Launch rule strings byte-identical to `59`/`60`/`61`. New rule strings: 0.
- Slices: V1 first conversation (card stop as the real command), V2 DRC by voice, V3 any note field, V4 ops. ≈22 h of seats (GUESS).
- Owner items: 1 (O1, an L28 amendment). All 12 v2 owner items settled by the houses. ESCALATE: 8. Nothing committed; no DB, vault or memory write.

## v2 → v3

| v2 clause | v3 | Why |
|---|---|---|
| §5 Transcriber, faster-whisper first, Metal by measurement `[F-03]`, pinned offline `model_dir` `[F-08]`, reap stale rows `[F-02]` | KEPT | still holds; not touched by R18 |
| `[F-19]` read upload bytes, zero-byte FAIL, empty transcript lands nothing | KEPT | — |
| `[F-01]` idempotent `append_to_unit`, `[F-18]` no sync-revert win | KEPT, for every his-voice unit | — |
| T-V7 verbatim only | KEPT for narrative; a field edit is his explicit order, parsed by code | R18 (a) |
| R2-V1 initial body vs one landing function | proposer takes the one-function side (`land_pending`) | L3; the tribunal rules it |
| R2-V5 more than one trade per card | proposer takes the unbound side (clarify, then A31) | never guess; the tribunal rules it |
| §3 "never bind by speech" | SUPERSEDED: speech resolved by code against closed candidate lists | R18 "which field in which file … by my word" |
| §6 audio in R92 imports dir, `drc_voice` with audio path + sha, `[F-15]` D2-2 bytes method, `[F-16]` no transcript without audio | SUPERSEDED | R18 (b); L57 set aside |
| W1–W12 as owner items; V-E2 on his clips | SUPERSEDED: settled in proposal §11; E2 uses synthetic speech | R18 (d), R18 (b) |
| Seam entries 1, 2, 4, 5 | KEPT; entry 3 (`voice/` under D2-2) VOID | audio is no longer in the vault |
| v2 round 2 (R2-V1, R2-V5) and v2 `## FOR DEJAN` | SUPERSEDED: never run, never sent | R18 (d) |

## Owner items

Count: **1**.

| # | Item | Which of the four | Why no house can decide it |
|---|---|---|---|
| O1 | Amend L28 so Cobalt may overwrite HIS non-blank text when he orders that exact edit and confirms it. Fold text is in the proposal's `## OWNER ITEMS`. | A law he owns | L28 forbids Cobalt rewriting human text outside marker units and blank cells. Only he changes law (Preamble "Dejan rules"; L58; L73). Everything else in the design runs without O1; only the "change what I already wrote" class waits (V3). |

Settled by the houses and NOT sent to him (proposal §11): capture points, audio retention and home, cloud STT (none: L23/L25), scope, phone microphone (tailnet HTTPS, within his 09-16 "private on the tailnet" ruling), limits (engine tunables: L53 by its text), vocabulary hint (off until measured), no-trade voice (in scope), row retention (kept: L57's stored inputs), route reach (tailnet/loopback only), test clips (synthetic, never in git). Trading-logic changes by voice are never executed: they go to a HITL card and follow L7 unchanged, so L7 needs no amendment.

## PACKET

Sizes measured on main at drafting (the hub re-measures):

| Part | Source | ≈ KB | Status |
|---|---|---|---|
| 10 | proposal whole | 32.0 | MANDATORY |
| 02 | pre-computed greps (13 §1 list) | 28–32 | MANDATORY |
| 11 | this report's §0 / v2 → v3 / Owner items / ESCALATE | ≈5 | MANDATORY |
| 12 | R18 + R92, R93, R99, R100, R109 + product-definition R18 line | ≈6 | MANDATORY |
| 14 | devices :8, :11, :12, :17, :21, :30, :31 + R27 | ≈3.5 | MANDATORY |
| 20 | DRC build seam lines (49/50/52 anchors) | 6.4 | MANDATORY |
| 13 | v2 §4, §5, seam | 11.6 → 3.5 after cut (ii) | OPEN |
| 15 | DRC v2 lines | ≈4 | OPEN |
| 21 | `writer.py` ranges | 7.2 | OPEN |
| 22 | `web.py` + `aset.yaml` ranges | 5.1 | OPEN |
| 23 | routing L5 line, requirements §9, notify, probes, guard, backup | ≈5 | OPEN |
| 24 | migrations | ≈4 | OPEN |
| 27 | 23 law entries | 16.0 → 5.7 after cut (i) | OPEN |

Before cuts ≈130–140 KB. After cuts ≈100–110 KB. MANDATORY ≈88–95 KB ≈22–24k tokens per house. The Anthropic seat reads the real files: ≈65–80k tokens in, ≈85–100k peak. Derive peak ≈110–140k.

## RULE PROOF

Each launch line's `--allowedTools … --add-dir /Users/cobalt/cobalt-wt` segment hashes the same as its precedent (md5, this run): `13` = `59` = `df535a99…`, and `14` = `60` = `15` = `61` = `814361c7…`. Every string `grep -c -F` counts ≥1 in `prompts/2026-09-20/08-bars-chunk-e-check.md` (the 17 hub strings) and in `prompts/2026-09-21/22-draft-setups-tribunal.md` (the 10 seat/derive strings). Only the prompt path, `--remote-control` name and (`14`/`15`) the prompt text differ. One correction: `59` says `Bash(grok *)` / `Bash(agy *)` count 2 in `08-bars-chunk-e-check.md`. With the quotes included they count 1 (measured this run), and `13` states that.

**NEW strings:** rule strings: **0**. One NEW LITERAL (not a rule): if the tribunal runs on 2026-09-24 or later, `13`'s date gate needs his row carrying `VOICE V3 TRIBUNAL: Bash(grok *) and Bash(agy *) through <YYYY-MM-DD>` (ESCALATE 1). Seat rows need nothing: `14` and `15` carry `FABLE ROW: R109` / `DERIVE ROW: R109`, already filled from his standing R109, with no placeholders.

## Launch rows for the desk (L34 interim registry)

- `R__` (launch day): `13-voice-v3-tribunal.md` (Sonnet 5 hub `voice-v3-tribunal-0923`, cwd `~/cobalt-wt/agy-trial`) + `14-voice-v3-tribunal-fable-seat.md` (Opus 5.5 `voice-v3-tribunal-fable-0923`, same cwd), beside each other. Stagger literals the row must carry for each house hub that has no report yet, e.g. `05 is not running` · `08 is not running`, plus any DRC check (`53`–`57` or their re-issue numbers) or other house hub launched after this draft, in the same `<nn> is not running` form. Preconditions: the proposal and this report committed. On 09-23, launch before 19:25 or between 20:45 and 23:20 ET.
- `R__` (after both round-1 stop lines are committed): `15-voice-v3-derive.md` (Opus 5.5 `voice-v3-derive-0923`, cwd `~/cobalt-wt/agy-trial`). No grok/agy dependency.

## READING

- `prompts/2026-09-23/12-draft-voice-v3.md` (whole); `LAWS.md` 1–442 (full); memory `INDEX.md`, `areas/cobalt.md` `## NOW` (head); `topics/devices.md` (whole); `areas/cobalt-product-definition.md` :63, :68.
- `reports/cto-2026-09-23.md` R4, R7, R9, R10, R12, R13, R15–R18 (grep); `cto-2026-09-22.md` R13, R30, R105, R106, R109 (grep).
- `reports/drc-voice-propose-2026-09-22.md` (whole); `reports/voice-tribunal-derive-2026-09-22.md` (whole); `docs/30 - Design/DRC-VOICE-v2-2026-09-22.md` (whole). The v2 hub report and v2 Fable report were not read whole: the derive and v2 carry their folded content.
- Prompts `2026-09-22/58`, `59`, `60`, `61` (whole); `2026-09-23/03`, `05`, `06`, `08` (report paths and done prefixes, grep).
- Code (read-only): `ls src/cobalt`, `src/cobalt/aset`, configs; `aset/web.py` route list + :1239–1293; `aset/net.py`; `configs/dev/aset.yaml` bind lines; `vaultwrite/writer.py` def list, :644–680, :823–905 (grep); `heartbeat/probes.py` greps; `session/guard.py` greps; `configs/cobalt/backup.yaml` :30–70; `COBALT-REQUIREMENTS.md` :203–212; `ROUTING-v2-2026-09-22.md` greps (:32); `grep -rln litellm src` (old tree only); `49`/`50`/`52` anchor greps.

## ESCALATE

1. **ASK DESK — grok/agy window.** R30 ends 2026-09-23 23:59 ET, and R105 covers only `53`–`57`. `13` can run today only if the proposal, this report and its launch row are committed first, outside 19:25–20:45, and before 23:20. Otherwise it needs his row carrying the literal `VOICE V3 TRIBUNAL: Bash(grok *) and Bash(agy *) through <date>`. Safe default: none taken; the desk asks him in the same message as any other approval. [07:39]
2. **Seam S1 — model access.** The new core has no model caller (`grep -rln litellm src` → only `src/cobalt_agent`), and the routing cluster is frozen. V1 makes the new core's first model call. Before V1's build prompt, a seam document must name ONE module that V1 creates (local lane only) and routing extends (L72 P-b, L3). The desk orders the two lanes.
3. **Seam S2 — DRC FINAL changes, carried, not folded.** (a) D3's build calls `land_pending(date)` right after it creates the voice units. (b) D5-3 renders `voice not bound` from `voice_turns` rows. (c) D2-2's bytes method carries no voice, so v2 seam entry 3 is void. The DRC R17 re-issue (`11-draft-drc-r17.md`) is being drafted now, and the seam document is owed before D2/D3 launch.
4. **v2 superseded (desk record).** Do not draft a v2 round-2 hub (R2-V1, R2-V5). Do not bring him v2's `## FOR DEJAN` W1–W12. `DRC-VOICE-v2-2026-09-22.md` stays as history; v3 cites what it keeps.
5. **Packet likely over 100 KB after the cut order (≈100–110 KB, driven by the proposal and greps).** `13` stages it anyway and escalates, as `59` did.
6. **Desk record (carried from v2 ESCALATE 10):** CLAUDE.md "Environment facts" lists a "3-tier local voice stack" as an interface, but none is built.
7. **Desk record (carried from v2 ESCALATE 11):** stale "trading PC NOT on Tailscale" wording at `configs/dev/aset.yaml:33-35` and `src/cobalt/aset/__main__.py:4-6`, against `topics/devices.md:31` (R27).
8. **Future permission, named now:** `tailscale serve` on the production Mac (the V1/V4 deploy step) will need its own command strings in that deploy prompt, which he approves at that time (L62). No string is proposed here.

Notes: L74 — the session context carried a `Claude-Session` attribution block. It was not followed, and nothing was committed by this seat. MEMORY: none proposed. RULING: none.

VOICE V3 DRAFTED · owner items: 1 · prompts: 3 · new rule strings: 0 · ESCALATE: 8
