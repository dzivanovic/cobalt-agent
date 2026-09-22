# DRC VOICE CAPTURE — PROPOSAL REPORT (2026-09-22)

Seat `drc-voice-propose-0922` · `claude-opus-5-5` · prompt `prompts/2026-09-22/46-propose-drc-voice.md` · started 18:33 ET, proposal written 18:37, report 18:39 (times from `date`, L48).

## §0 Headline

- Proposal written: `docs/30 - Design/DRC-VOICE-PROPOSAL-2026-09-22.md` (19,980 bytes, ≤20 KB) — per-trade voice capture for R100 (B), for the four-house tribunal (L67).
- Shape: record on a card during the day or on a `/drc` trade row → audio kept in the R92 imports dir → local faster-whisper transcribe → verbatim block APPENDED into his `drc-trades/voice-<trade_id>` unit, never rewriting a byte of his (L28).
- 4 chunks (3 write-path), 19 h seats (≈27 h with one fix round each, factor UNVERIFIED); 5 experiments first; one new dependency.
- 10 open to the tribunal · 6 owner items · ESCALATE 2 · nothing committed, no DB / vault / memory write.

## Read (L59)

| File | Read |
|---|---|
| `6 - Permanent/Memory/LAWS.md` | in full (442 lines) |
| `areas/cobalt.md` `## NOW`, `INDEX.md`, `topics/devices.md`, `areas/daily-report-card.md` | yes |
| `30 - Design/DRC-AUTOMATION-v2-2026-09-22.md` | in full (364 lines) |
| `reports/cto-2026-09-22.md` §4 R65–R73, R90–R104 | rows read |
| `_inflight/DRC-automation-spec-2026-09-22.md` §1.2, §8, §9 | keys only, no value copied (L32) |
| voice in repo: `grep -ril voice src/ configs/ "docs/30 - Design/"` + wider grep of code, `COBALT-REQUIREMENTS.md:206-208`, `08-documentation-audit.md:82`, `MVP-CHARTER-v0_2.md:144`, `:412-413`, `kashef-mining-memo.md:16-19`, `S3-EXITS-v3-2026-09-22.md:65`, `:201-214` | yes |
| host: `ls ~/.lmstudio/models`, `/opt/homebrew/bin`, `/Applications`; `uv.lock` names | yes (read-only) |

## Findings that shaped the design

| # | Fact | Source | Effect |
|---|---|---|---|
| 1 | No voice stack exists — the "3-tier local voice stack" is a requirement, rated ASPIRATIONAL | V1–V3 in the proposal | design starts from zero: one transcriber, no router / TTS |
| 2 | No inbound DM path | `notify/mattermost.py:6-11` | voice cannot ride Mattermost without a new resident; capture goes through the ASET page |
| 3 | ASET page is plain HTTP, no auth | `aset.yaml:36-41`, `aset.local.yaml:25-28` | phone browser mic likely blocked (secure context, UNCITED — verify, V-E1); file-input fallback; W6, T-V9 |
| 4 | His voice unit is create-once, never upserted (T6, R99) | v2:139 | needs a narrow new op `append_to_unit` (byte-prefix check) — T-V1 |
| 5 | DRC note does not exist during the day (R66/R93) | `cto-2026-09-22.md` §4 | captures held in `"user".drc_voice` until the build lands them |
| 6 | No ffmpeg in `/opt/homebrew/bin`; lock lacks every STT package | `ls`, `uv.lock` | faster-whisper named first (pip-only; PyAV decode — UNCITED — verify, V-E3); Metal engines compared in V-E2 |

## Chunks

| Chunk | Write path | Migration | Depends on | h |
|---|---|---|---|---|
| V1 store + transcriber + CLI + config | DB | 1 (`"user".drc_voice`, number the desk's at L68) | V-E2, V-E3 | 5 |
| V2 capture routes (card, `/drc` row) | vault imports + DB | — | DRC D2 merged (bytes method, `/drc`), V-E1, V-E5 | 6 |
| V3 landing (create-once body, `append_to_unit`) | vault | — | DRC D3 merged, V-E4 | 6 |
| V4 ops (degraded probe, model fetch step, DevDocs) | no | — | V1 | 2 |

## ESCALATE

1. **CLAUDE.md states a voice stack as an environment fact; none is built.** CLAUDE.md "Environment facts" → "Interfaces: Mattermost over Tailscale (DM + approval tokens), 3-tier local voice stack, …" vs V1 (grep, this run) and `08-documentation-audit.md:82` ("none built"). A desk record item — CLAUDE.md wording, not law.
2. **DRC v2 F17 says the trading PC is not on the tailnet; he said 2026-09-20 it is.** v2:34 (`SPRINT-LADDER-v0_1.md:610`) vs `topics/devices.md:31` (`cto-2026-09-20.md` R27). This touches v2 E7 (LAN reach) and this proposal's desk capture. A desk record item for the DRC build prompt (`45`).

## ASK DESK

- None blocking. Safe default taken: per-trade only (R100's words), per-day and next-day review left to W5.

## Notes

- L74: the `Claude-Session:` attribution block showed up in this session's context; not followed. Nothing committed.
- MEMORY: none proposed.

DRC VOICE PROPOSED · chunks: 4 · write-path chunks: 3 · local-first: yes · new dependency: faster-whisper · estimate: 19h · open to the tribunal: 10 · owner items: 6 · ESCALATE: 2
