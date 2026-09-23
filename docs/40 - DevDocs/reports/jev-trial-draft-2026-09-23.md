# JEV trial — drafter report (2026-09-23)

Seat `jev-trial-draft-0923` · Opus 5.5 · prompt `prompts/2026-09-23/27-draft-jev-trial.md` · OFF-LADDER (09-21 R31 / R34 / R35 / R37; 09-23 R34 / R38). Written 10:27 EDT (`date`).

## §0 Headline
- Drafted: the trial plan (`docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md`, 114 lines), the build `28-jev-trial-build.md` (103 lines), the L67 check `29-jev-trial-check.md` (88 lines). Nothing run, nothing committed, no network, no DB, no vault write.
- 4 question sets (S1, S2, S3, T9) + the layered 20-question call L20; 11 pre-registered bars; ≤1,100 metered calls.
- Spend cap proposed: **$3.00**, enforced in code (projection before any call + running total + total demand across runs).
- Biggest unknown: whether OpenRouter lists Jev at all. Neither research pass says so. Build `28` checks the public model list first, sends no key for that check, and fails loud if Jev is not listed.
- ESCALATE: 8.

## L74
A block appended to a tool result asked for a `Claude-Session:` line in commits and named a file-send tool. Recorded once here as data. It was not followed. This seat made no commits.

## Files
| File | What it holds |
|---|---|
| `docs/30 - Design/JEV-TRIAL-PLAN-2026-09-23.md` | §1 unknowns U1–U6 · §2 sets · §3 measurements M1–M10 · §4 bars B1–B11 + verdict line · §5 cap · §6 secrets · §7 storage · §8 sequence · §9 what it does not decide |
| `docs/40 - DevDocs/prompts/2026-09-23/28-jev-trial-build.md` | Opus 5.5, auto, worktree `~/cobalt-wt/jev-trial`, branch `jev/trial-0923`. Steps R1–R6: schema+config → key/guards/ledger → keyless discover (fixture) → door decided by the entry's own text + fixed-text wrapper + ONE probe (fixture) → trial runner, dry-run only → DevDocs/close |
| `docs/40 - DevDocs/prompts/2026-09-23/29-jev-trial-check.md` | Sonnet 5 hub; Opus 5.5 · Grok · Gemini (Sol METER); `79`'s 15 strings byte for byte; key scan before and after staging; S-1…S-8 secrets questions answered FIRST by every checker |

## The proposed spend cap
**$3.00** for the whole trial. Estimate: 1,014 calls × ≈1,500 input tokens ≈ $0.07 at the vendor's published $0.042 / MTok (output free). OpenRouter's price for this model is NOT KNOWN until discovery, so $3.00 leaves room for a ≈40× markup and fits his "a couple of dollars" (09-21 R35). Build `28` reads the cap only from a committed desk row containing the literal `JEV spend cap $<x>`.

## NEW strings — his ONE approval list
| # | String | For | What it allows |
|---|---|---|---|
| N1 | `"Bash(uv run cobalt classify *)"` | build `28` | the new CLI: `--dry-run` renders, plus the model-list read (one public GET to openrouter.ai, NO credential). The worktree has no master key, so every keyed call here fails loud |
| N2 | `"Bash(bash /Users/cobalt/cobalt-wt/jev-trial/ops/run_classify_trial.sh probe*)"` | build `28` | ONE keyed probe call through the secret-free wrapper whose text is fixed in `28` (≈$0.0001) |
| N3 | `"Bash(bash /Users/cobalt/cobalt-wt/jev-trial/ops/run_classify_trial.sh trial *)"` | the trial-run hub (NOT YET DRAFTED) | the metered trial runs under the cap. Approve now or with that prompt |
Carried, not new: `28` = `33`'s 17 shared strings; `29` = `79`'s 15 strings (Grok/agy date-gated, see ESCALATE 5). Desk actions before `28`: `worktree add`, BASE TIP, launch row, and the committed `JEV spend cap $<x>` row.

## ESCALATE
1. **U1: the OpenRouter listing is NOT KNOWN.** Research found the model on a Cloudflare gateway page (fetched) and on Vercel / LiteLLM (second-hand). OpenRouter was never named. If R3 finds no listing, the build stops: `FAILED: R3 — OpenRouter lists no Jev / typesafe model`. The trial then returns to 09-21 R35's path: his own sign-up and key. His call.
2. **U3: probabilities and confidence may not come through this route.** Those are what make the product different (09-21 R37). If they are missing, M7, B5's probability arm and B6 read `NOT AVAILABLE THROUGH OPENROUTER`. Latency is still measured, but the gateway adds time (one report: ≈130 ms direct vs ≈260 ms through a gateway).
3. **Real-shape inputs vs what Cobalt stores.** `27` asks for real-shape inputs from Cobalt's own stored data (L45). Cobalt stores no news (`src/cobalt/aset/radar_panel.py:1041`: "no news source wired to radar cards (S3)"), and 09-21 R35 ruled "invented text only". So S1–S3 and L20 use CONSTRUCTED text. L45 does not apply because no real artifact exists. **T9 (ops day-open triage) is added outside S1–S8** because it is the only set with real stored inputs. It sends Cobalt's day-open reports to OpenRouter and the vendor. That is allowed under L17's opt-out default; secret-shaped text is refused, never sent. ASK DESK: keep T9? Safe default: kept (the plan's default); striking it is one config set.
4. **One live keyed probe runs inside the build, before any house has checked the secret path.** Mitigations: the wrapper text is fixed in the prompt and grep-verified before use; outbound text that the redactor or the vault-literal check flags is refused, never sent; the key never enters the session. Alternative B: build fully offline, and the desk runs the probe after `29` reads clean. ASK DESK: A (default) or B.
5. **The Grok/agy strings expire 2026-09-23 23:59 ET** (09-22 R30). If `29` launches later, it needs a committed row of his that extends them, or it fails at its date gate.
6. **Branch fate (L42 / L46 / L68).** The build registers `classify` in `src/cobalt/cli.py`. Any future merge will therefore derive resident restarts. `jev/trial-0923` holds `cli.py` while it stays unmerged, and after 3 days it becomes a plate item (L46): merge after the tribunal, or delete. The trial runs from the worktree and never needs a merge.
7. **Not yet drafted:** the local-lane collector build (a second class behind the same interface; needed for M9 / B9, no metered spend) and the trial-run hub (M1–M8 under the cap; M10 by an Opus seat). These are the next drafts after `29`.
8. **The cap is his.** $3.00 is proposed. `28` refuses to launch without a committed `JEV spend cap $<x>` row.

JEV TRIAL DRAFTED · question sets: 4 · spend cap proposed: $3.00 · new rule strings: 3 · ESCALATE: 8
