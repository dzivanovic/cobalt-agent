# DRC BUILD — PROMPTS DRAFTED (S3-P3 · F14) — 2026-09-22

Drafter `drc-build-draft-0922` (Opus 5.5, `claude-opus-5-5`), prompt `prompts/2026-09-22/45-draft-drc-build.md`. Started 18:33 ET, prompts written by 18:47 ET, report 18:4x ET (times from `date`). Built nothing, ran no DB / pytest / git write, launched nothing, committed nothing.

## §0 Digest
- **10 prompts written:** 5 build (`48`–`52`) + 5 check (`53`–`57`), one pair per v2 chunk D1–D5. His R90–R103 are folded in (map below). The L31 renames are applied everywhere.
- **Build order is ONE linear stack: D4 → D1 → D2 → D3 (one deploy for the set) → D5 (after S3 C2 is on main).** This differs from v2's "D1 → D4 ∥ D2 → D3". Reason: ESCALATE 1.
- **4 builds wait on E1** (D1, D2, D3, D5). Each fails PREFLIGHT until `1 - Trading/5 - Review/_imports/drc/<date>/` holds both of his files (R92). D4 does not wait: it can launch when S3 opens on 09-24. On 18:47 ET the `_imports` folder did not exist yet.
- **12 NEW rule strings:** the desk brings them to him as ONE approval list (below). All 5 check prompts reuse `16`'s line byte for byte, with no new string. The checks do also need his date extension for `grok`/`agy` (ESCALATE 9).
- **Hours (seat, UNVERIFIED like v2's):** D4 5 · D1 9 · D2 7 · D3 10 · D5 6 = **37 h** of building. That is v2's 32 h plus R91's second parser, R102's change line, R93's no-trade path and R90's RESOLVE, minus R101's engine. Add ≈1 h per check hub. A fix round would add ≈0.4× (v2's factor, UNVERIFIED).

| # | file | chunk | worktree / branch | base | waits on |
|---|---|---|---|---|---|
| 48 | `48-drc-d1-build.md` | D1 trading-log + stats-log parsers, pairing, carry, store, 1 migration | `~/cobalt-wt/drc-d1` · `drc/d1-trading-log` | D4 tip | E1 + D4 built |
| 49 | `49-drc-d2-build.md` | D2 `/drc` import page, bytes writer, both-placed, no-trade action, event | `~/cobalt-wt/drc-d2` · `drc/d2-import` | D1 tip | E1 + D1 built |
| 50 | `50-drc-d3-build.md` | D3 build + note from his template, no-trade DRC, PnL unit, miss line, 15:40 retired, smoke | `~/cobalt-wt/drc-d3` · `drc/d3-build` | D2 tip | E1 + D2 built |
| 51 | `51-drc-d4-build.md` | D4 DRC settings family, one reader, daily note reads the key, ASET change line | `~/cobalt-wt/drc-d4` · `drc/d4-settings` | main | nothing (S3 open) |
| 52 | `52-drc-d5-build.md` | D5 reconcile writes legs, `unresolved` line, RESOLVE action | `~/cobalt-wt/drc-d5` · `drc/d5-reconcile` | main | E1 + D1–D3 merged + S3 C2 merged |
| 53–57 | `5<n>-drc-d<k>-check.md` | check round 1 per chunk: Sonnet 5 hub; Opus 5.5 + Grok + Gemini (Sol METER until Sat 09-26 06:47 ET, probed then skipped; D5's check may seat Sol) | `~/cobalt-wt/agy-trial` | — | the chunk's `BUILT` line + his grok/agy extension |

All 5 builds run Opus 5.5 in `--permission-mode auto`, as the dev lane under `33`: `cobalt_dev` only inside the suite's rollback, notes in `tmp_path`. The mode is stated on the line (L62 as amended R80). All 5 checks run Sonnet 5 in `auto` and are read-only.

**NEW RULE STRINGS — verbatim, for his ONE approval list:**
1. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env)`
2. `Bash(rm /Users/cobalt/cobalt-wt/drc-d1/.env)`
3. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d2/.env)`
4. `Bash(rm /Users/cobalt/cobalt-wt/drc-d2/.env)`
5. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d3/.env)`
6. `Bash(rm /Users/cobalt/cobalt-wt/drc-d3/.env)`
7. `Bash(git rm configs/cobalt/templates/drc.md.j2)`
8. `Bash(git rm ops/com.cobalt.prefill-drc.plist)`
9. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d4/.env)`
10. `Bash(rm /Users/cobalt/cobalt-wt/drc-d4/.env)`
11. `Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d5/.env)`
12. `Bash(rm /Users/cobalt/cobalt-wt/drc-d5/.env)`

Strings 1–6 and 9–12 are the R64 / R30 `.env` pair pointed at each new worktree (L41 interim: copied by name, never printed, removed at every stop). Strings 7–8 are the exact-path deletions that v2 §8 requires (the repo template dies, the plist leaves `ops/`). Every other string matches `grep -c -F` ≥1 against `33` (builds) or `16` (checks); I checked all ten files at 18:4x ET.

**Where each ruling went**
| ruling | lands in |
|---|---|
| R90: leave the position open, `unresolved: card <id>`, RESOLVE on `/drc`. Settles R2-1 | `52` D5-2 / D5-3 / D5-4 · `57` |
| R91: parse both logs (the TradeZella log replaces typed cells and OCR). E1 = both files | `48` D1-4 · `49` both-placed · `50` B25 / B26 |
| R92: `1 - Trading/5 - Review/_imports/drc/<date>/` | `49` D2-2 · the E1 gate of `48` / `49` / `50` / `52` |
| R93: a DRC every market trading day, plus a "why no trades" section | `49` no-trade action · `50` `drc-day/no_trade` + `drc-day/voice-no-trades` |
| R94: account-agnostic, one bucket | `48` D1-2 (v2's two-account FAIL struck) |
| R95 / R96 / R102(1): one place = the central settings, his ASET change line, shown in the daily note | `51` D4-2 / D4-3 / D4-4 |
| R98: example blocks stay in his template | `50` (nothing strips them) |
| R99: voice unit next to each trade, never rewritten | `50` `drc-trades/voice-<trade_id>` |
| R100: no voice this slice | every build's NOT-IN list |
| R101: no rule→checker map, no engine | `51` (F-16 binding struck) · `50` (`rule_engine` unit, rules line, B33, C11 not rendered) |
| R102(2) O11 four keys · (3) O14 refuse in reset · (4) O16 Cobalt fills the PnL line | `50` premarket · `49` / `51` / `52` refusals · `50` `drc-risk/pnl` |
| R103: fixture consent, Postgres only, 15:41 wording, gross AND net, no size cap | `48` D1-0 · `50` summary / PnL / smoke · desk wording (ESCALATE 11) |
| L31 (in force): `trading_log.py` / `import_id` / `trading_log` / `trading_log_shape` | all prompts, plus `stats_log` for the TradeZella file (ESCALATE 7) |

## ESCALATE
1. **The stack order is the desk's call.** v2 orders the chunks D1 → D4 ∥ D2 → D3. These prompts stack them linearly: D4 → D1 → D2 → D3. There are two reasons. First, D4 is the only chunk that does not wait on E1, so it can use the idle time now (L73). Second, R102's change line puts D4 into `aset/web.py`, which is D2's file. Sibling branches would share a seam, and a shared seam must be settled before either launches (L72 P-b). Stacking settles it. The routes are still kept apart in the file: D4's block goes after `/attest` and D2's goes at the end of the file. The cost is that a fix round on a lower chunk means the desk re-points each later chunk's BASE TIP.
2. `ASK HIM (via desk)`: R91 makes both-placed = trading log + stats log. **Screenshots are optional per-trade embeds, not a gate.** v2 required one screenshot per trade, and R91 is silent on screenshots. The default built is "optional".
3. `ASK HIM`: under R93, **the no-trade DRC is created only by his "No trades today" action on `/drc`, or by a trading log with zero executions.** Nothing creates it without him. The default built is his action.
4. `ASK HIM`: **the RESOLVE choices under R90.** The default built is two choices, each with his text required: (1) "export is right — keep the position open"; (2) "closed outside the export — stop carrying". The card's state machine is never changed: no CLOSED→FILLED edge (L7 + HITL would be needed). So a card he flattened stays CLOSED on the radar while the DRC carries the position.
5. **No v2 addendum for R90 exists.** R90's row says "folded into the design as a desk addendum to v2", but `grep -il addendum "docs/30 - Design/"` finds only TAXONOMY and S3-EXITS. `52` / `57` carry R90's text directly. The desk decides whether to write the addendum before `52` launches.
6. **The change line is a design detail v2 never had** (R96 / R102). It shows a diff and a hash; Apply goes through the CLI's own `put` function, reads back, and is refused in the reset. It also edits `aset.sheet_modes`, the row that drives SIZING. L28's 09-15 exemption names a "trader-run `cobalt settings load --apply`". `ASK DESK: does his web change line carry the same "trader already in the loop" exemption, or does it need its own ruling?` `51` builds it under the CLI's exemption reading. The L67 check (`56`) reads it.
7. **L31 names for the TradeZella file are my choice:** `stats_log.py`, kind `stats_log`, flag `stats_log_shape`. L31 bars the vendor name, and the prompt named only the `das*` renames. They change no mechanism.
8. **S-C1 / S-C2 / S-C2b must be in the S3 C1 / C2 build prompts** (v2 derive ESCALATE 4). `52` D5-0 FAILS if C1's DDL lacks `trading_log` in `source` / `price_source` plus `source_id`, or if C2's writer lacks the trading-log-sourced correction / new exit leg semantics. The value is now `trading_log`, not v2's `das`.
9. **The grok/agy date gate.** R30 covers `Bash(grok *)` / `Bash(agy *)` only through 2026-09-23 23:59 ET. Every DRC check runs 09-24 or later. Each check prompt refuses to launch without a committed row of his that extends them to the run date. The desk brings this with the approval list.
10. **The migration number is fixed at the L68 gate.** D1 takes the next free number over main plus every unmerged branch and records the list; the desk renumbers.
11. **The Charter / ladder "15:41" re-wording is the desk's own document edit** (R103 O18: "within the build time after the second file", "every market trading day"; `MVP-CHARTER-v0_2.md:171`, ladder `:612`, `:616`). No build edits these; `50` re-keys only the smoke.
12. **The deploy prompt is still owed** for D4 + D1 + D2 + D3 as one stacked set. It must include: residents down before the merge inside the pause (L66); `launchctl bootout` of `com.cobalt.prefill-drc` and the plist removed from `~/Library/LaunchAgents`; the RESTARTS lines; the E7 LAN read after the deploy; and **his daily-stop value loaded before the first build.** Without that value the daily note and the DRC show `not given` (a production-visible change).
13. **R101's effect on §13 as ruled (R69–R72) is a HOW / WHEN change only.** No ACTION or WRITER cell changes. The engine halves of A9, A21, A24, B33 and C11 render nothing this slice. `50`'s `## NOT RENDERED` lists them. The desk confirms that reading or brings it to him.
14. **L74:** a commit-attribution block (a `Claude-Session:` line, plus a file-send tool) arrived in a system reminder after the tool result of reading `45`. It is recorded here once and was not followed. I committed nothing.

DRC BUILD PROMPTS DRAFTED · build prompts: 5 · check prompts: 5 · waiting on E1: 4 · new rule strings: 12 · ESCALATE: 14
