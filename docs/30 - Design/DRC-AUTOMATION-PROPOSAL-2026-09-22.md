# DRC AUTOMATION — proposal (2026-09-22)

Proposer `drc-design-0922` (Opus 5.5), written 15:48–16:1x ET. LADDER `S3-P3 · F14` (+ the F15 seams it needs). L67 step: THIS IS THE PROPOSAL — the four houses rule and derive; nothing here is built. Rulings it stands on, and nothing wider: `cto-2026-09-22.md` §4 R65, R66, R60, R58. Content/process source: his coach's spec `docs/_inflight/DRC-automation-spec-2026-09-22.md` (gitignored, L32) — cited below as `SPEC §n` by section and key only; no value, rule sentence, ticker or price of his appears in this file. Automation pattern: `docs/90 - References/trade-reporter/` (pattern only, not its field set). NO PDF (R65 c).

## 1. FACT BASE

| # | Claim | file:line | Status |
|---|---|---|---|
| F1 | The 15:40 job runs `uv run prefill drc` Mon–Fri | `ops/com.cobalt.prefill-drc.plist:24-29`, `:50-54` | PROVEN |
| F2 | It creates the note whole only when absent, from the REPO copy `drc.md.j2`, then returns | `prefill/drc.py:270-272`, `:427-432`; `prefill/config.py:30` | PROVEN |
| F3 | On an existing note it upserts three units: `drc-risk/risk_parameters`, `drc-trades/tickers`, `drc-rules/rules_check` | `prefill/drc.py:12-16`, `:441-449` | PROVEN |
| F4 | `DRC-2026-09-21.md` was rendered from the repo copy, not his Obsidian template (date line, no example blocks, `### Cobalt Rules Check` heading that only `drc.md.j2:132` carries) | `DRC-2026-09-21.md:5-17`, `:228`; `drc.md.j2:5-17`, `:132`; `5 - Templates/DRC.md:7`, `:60-124` | PROVEN (shape) — contradicts the "Cobalt uses the Obsidian template" fact recorded at `cto-2026-09-22.md:197`; that note only |
| F5 | His template uses core-Templates tokens `{{date:YYYY-MM-DD}}` (two places), carries its own risk-parameters line, two filled example trade blocks and a filled example If/Then | `5 - Templates/DRC.md:7`, `:17`, `:51`, `:60-124`, `:177-187` | PROVEN |
| F6 | Placements for the three units already handle a note Cobalt did not create (below his risk line, under the trades heading, end of note) | `prefill/drc.py:321-347`, `:441-449` | PROVEN (code) · on HIS template's text: UNPROVEN → E3 |
| F7 | `create_if_absent` never rewrites; `upsert_unit` refuses an absent note | `vaultwrite/writer.py:559-619`, `:669-673` | PROVEN |
| F8 | Every vault write is refused inside `market_reset` (repo targets exempt) | `vaultwrite/writer.py:387-416` | PROVEN |
| F9 | Atomic write + mtime guard, versioned rows, human-wins merge | `vaultwrite/writer.py:457-528`, `:644-661` | PROVEN |
| F10 | Replay (21:10) writes `drc-misses/miss_line` into an EXISTING note only; absent → `DrcNoteAbsent` | `replay/line.py:28-34`, `:155-172`; `ops/com.cobalt.replay.plist:38-42` | PROVEN |
| F11 | The line step's failure is recorded and re-raised → the replay run FAILS on an absent note | `replay/runner.py:443-466` | PROVEN |
| F12 | The 09:00 reader reads only the prior note's `Grade:`/`Goal:` lines; absent note = loud `no prior DRC` | `daymode/drc.py:85-139`; `ops/com.cobalt.daymode-propose.plist:51-55` | PROVEN |
| F13 | The one web surface is the ASET app — **FastAPI**, not Flask ("modeled on the trade-reporter Flask pattern") | `aset/web.py:1-4`, `:83` | PROVEN |
| F14 | Its forms parse with `request.form()` (multipart-capable parser) | `aset/web.py:947`, `:1048` | PROVEN |
| F15 | `python-multipart` is locked only as a transitive dependency (via `mcp`); `pillow` via `matplotlib`; no OCR library in the lock | `uv.lock:2879`, `:2789`; `pyproject.toml:32-33` | PROVEN |
| F16 | Bind is config: dev = loopback, a local override = `lan` | `configs/dev/aset.yaml:39-41`; `configs/dev/aset.local.yaml:28`; `aset/__main__.py:28-50` | PROVEN · which file production loads: UNPROVEN → E7 |
| F17 | The trading PC is not on the tailnet | `SPRINT-LADDER-v0_1.md:610` | PROVEN (text) |
| F18 | Cards live in `aset_sizings` (ticker, direction, grade, entry, stop, shares, risk, state, actual_fill, recomputed shares, created_at) | `aset/store.py:292-322`, `:268` | PROVEN |
| F19 | The daily note carries the cards as ```aset / ```aset-fill fences — a rendered copy of the DB rows | `1- Daily Notes/2026-09-21.md:385-546`; `prefill/drc.py:70` | PROVEN |
| F20 | Rules parser: numbered lines, exactly one trailing tag, fail-loud; no dated/expiring-rule syntax | `prefill/rules_gen.py:37-107`, `:128`; `Rules.md:4-15` | PROVEN |
| F21 | Daily note premarket keys that exist: `Sleep:`, `Readiness:`, `RHR:`, `1% goal:`; meditated / tone / hotkey are not keyed lines (free text in a segment-score line) | `daily.md.j2:11-16`; `1- Daily Notes/2026-09-21.md:11-17`, `:330` | PROVEN · what `Sleep:` measures (hours vs score): UNPROVEN → O11 |
| F22 | The committed daily template hard-codes a daily-stop dollar line | `configs/cobalt/templates/daily.md.j2:18` | PROVEN (see ESCALATE, report) |
| F23 | `"user".legs`, `fills`, `drc_rows`, `prediction_records` are DECLARED, not built; the old tree's `public.trades` / `order_fills` names are taken | `db_migrations/placement.py:106-112`, `:143-147` | PROVEN |
| F24 | Migrations on main end at `0011`; unmerged branches add `0012` (bars, `02d67a6`) and `0013` (setups, `61a283f`); `0014`/`0015` claimed by H1 / stale-score / S3 M1 | `git log --all` on `db_migrations/`; `S3-EXITS-v3-2026-09-22.md:139` | PROVEN (0012/0013) · 0014+ claims: text only |
| F25 | v3: one `legs` table, estimated vs confirmed flag, `realized_r.1` pure function, `fills` kept declared (strike = v3 O16), "Nothing reads DAS" | `S3-EXITS-v3-2026-09-22.md:110-139`, `:164`, `:168`, `:237` | PROVEN (text) · v3 R2-2 OPEN FOR DEJAN |
| F26 | v3 names seven F14 seams (trade_note_path, trade_def, fill data from legs, realized R + provisional, stop path, pick row, cf-R at 21:10) | `S3-EXITS-v3-2026-09-22.md:228` | PROVEN (text) |
| F27 | S2 smoke checks the `drc-misses` unit and the prefill-drc job's last run | `configs/cobalt/smoke/s2.yaml:383-398`, `:436-438`; `configs/cobalt/jobs.yaml:181-186` | PROVEN |
| F28 | Charter F14 and the S3 smoke require "DRC note exists at 15:41" | `MVP-CHARTER-v0_2.md:160-171`; `SPRINT-LADDER-v0_1.md:612`, `:615-617` | PROVEN — contradicted by R66 (b) |
| F29 | Trade-reporter pattern: drop / click / paste per zone → client reads to data URL → one JSON POST → `build_drc_pdf(data: dict)` → artifact under `tmp/<uuid>` → view/download | `app.js:109`, `:121`, `:152-164`, `:263`; `app.py:10`, `:21-31`, `:47-68`; `drc_builder.py:60`; `index.html:62-63`, `:72-73` | PROVEN |
| F30 | `_imports/` is a Cobalt-owned vault location by the 09-06 R3 ruling; it does not exist in the vault today | `vault.py:99-101`; `find` of `Vault/Think` (none) | PROVEN |
| F31 | No real DAS export or TradeZella screenshot exists anywhere readable on this host | `find` over Vault, docs, Downloads, Desktop | PROVEN (absence) → E1, E2 |
| F32 | The DAS export carries an order log (stop placed/modified/cancelled/filled) in the same file | SPEC §1.1 row 1 | UNPROVEN → E1 |
| F33 | R67 (15:48 ET, S3-exits R2-2): the DAS import is the RECONCILE truth — Cobalt's legs are corrected to DAS as append-only correction rows naming the DAS source (L57), his taps / held-count statements kept as history; a mismatch is shown on the DRC, then adjusted; a position open at the DRC carries to the next day as an OPEN POSITION with its held shares until closed | `cto-2026-09-22.md:35` (R67) | PROVEN (ruling text; desk reading "B + his additions") |
| F34 | v3's `legs` correction row carries `price_source`; its values today are `last_poll` / `typed` / `dm` — no DAS value, no source-id column | `S3-EXITS-v3-2026-09-22.md:86`, `:133`, `:164` | PROVEN (text) → seam S-C1 below |

## 2. THE IMPORT PLACE

**Where.** ONE page, `/drc`, on the existing ASET app (`aset/web.py:83`) — the one web surface (Charter §5, L3). A second app is not needed: the ASET app already serves forms, already writes the vault through `VaultWriter`, already runs as `com.cobalt.aset`. Reached from the trading PC over the LAN bind (F16, F17 — the tailnet does not reach that PC) and from the Mac/laptop over Tailscale.

**What it accepts.**
- The DAS export: exactly one CSV per day, filename shape per SPEC §1.1 row 1 (date in the name).
- TradeZella screenshots: PNG/JPEG, one per trade. The page lists the trades parsed from the CSV; each trade row has its own drop zone (trade-reporter's per-ticker zones, F29) — drop, click or paste. That binds a screenshot to a trade deterministically, no image reading needed.
- Optional per-trade typed cells for the few figures only TradeZella carries (SPEC §2 keys `MAE`, `MFE`, planned target, best exit) — blank stays blank (`not given`), never guessed. Choice vs OCR = **O1**.
- Upload is multipart (not trade-reporter's base64 JSON — screenshots are heavy; F29 uses a 50 MB cap). `python-multipart` becomes a DIRECT dependency at its already-locked version (F15) — no new package.

**How a day is bound to its files.** A date field, default today (ET). Refused, loudly, naming the file: CSV filename date ≠ form date; any execution dated off the form date; a screenshot dropped with no trade row. Files land byte-for-byte under the vault's `_imports/drc/<YYYY-MM-DD>/` (Cobalt-owned by R3, F30; home = **O2**), sha256 recorded in `"user".drc_imports` (one row per file: date, kind, name, sha256, trade key for a screenshot, parse status, supersedes).

**What it shows back.** Per file: parsed ✓ / FAILED with the reason and the line. Counts: executions, trades paired, screenshots bound / trades, trades without a screenshot, cards with no DAS trade. Status line: `waiting for: DAS export` · `waiting for: screenshots (k of n)` · `READY → DRC built: <note path>` · `DRC build FAILED: <step> — <reason>`.

## 3. THE TRIGGER

- **Both placed** = a parsed CSV for the date AND a screenshot bound to every trade it contains (or **O3**'s no-trade form). The import handler computes that state after every upload — deterministic code, no LLM (L2) — and writes one typed event row `DrcInputsPlaced{date, das_import_id, screenshot_import_ids[], sha256s}` into `"user".drc_imports`' event table with state `pending → running → done | failed` (L18).
- **The build** runs on that event: in the same request, bounded by a timeout, result shown on the page; the CLI `cobalt drc build --date D [--dry-run]` runs the SAME function on the stored event (retry and L10 dry-run — not a second path). Synchronous vs a one-shot job = **T2**.
- **Only one placed** → nothing is created, no note, no unit. The page says what is missing. No nag timer, no failure: R66 makes "no DRC" his lawful choice. The heartbeat may show `DRC inputs: none / partial for D` as information (not red).
- **Placed inside `market_reset`** (20:00–21:00): the files are vault bytes and the note write is gated (F8) → default = the upload is refused with the reason, drop again after 21:00 (**O14**).
- **Reconcile step (R67, F33) — inside the build, after parsing, before the note write.** (1) Match each DAS trade to its card (§4) and to that card's current legs (`legs_current_v`, v3 C1). (2) Compute the diff per leg seq: shares, price, time; DAS exits with no Cobalt leg; Cobalt legs with no DAS execution; held count after each leg. (3) Render the diff (the "before") into the note's reconcile unit (§6). (4) Write the adjustment through v3's ONE correction writer (C2 — never a second leg writer, L3): a correction row per mismatched leg, a new exit leg per DAS exit Cobalt never recorded, each with source `das` + the `drc_imports` row id (L57); his taps and held-count statements stay as history rows (append-only). (5) Running shares after reconcile = the DAS position. (6) Re-render the unit with "adjusted to DAS: k rows (ids)". A card with no legs yet (filled before C1) gets its entry leg from DAS through the same writer. A refusal from C2's writer (e.g. a CLOSED card moved off 0) = build FAILED naming the card — never forced.
- **Open position carry (R67, F33).** A symbol whose DAS position is not 0 at file end is NOT a parse failure: the trade is `OPEN` with its held shares, its card stays FILLED (v3 expiry never touches FILLED, v3 F15), and it is stored in `drc_rows` as the day's open position. The NEXT day's pairing SEEDS each symbol with the carried position before reading that day's executions (a DAS day-file starts flat — UNPROVEN → E1); the next DRC shows it as a continuing open position until an execution brings it to 0. The trade keeps one `trade_id` across days; P&L realized per day, carried shares unrealized (no mark price invented — `unrealized: not computed`).
- **Re-import / correction.** Dropping a new file of a kind supersedes the old row (`supersedes` FK; old bytes kept, never deleted). A superseding upload re-fires the event; the build re-runs: the note exists → `create_if_absent` skips (F7), units upsert in place by id, his text inside a unit is preserved, a Cobalt line he changed → human wins + override row (F9). A trade that disappears from the new CSV loses its Cobalt block; any text of his that was inside it is kept by the merge and listed as orphaned (experiment E8).

## 4. PARSERS — each behind an interface (L9), each fail-loud (L1), each against the real shape (L45)

| Input | Interface → model | Reads | Fail-loud rule |
|---|---|---|---|
| DAS export | `ExecutionSource` → `Execution` (Pydantic: time, symbol, side ∈ SPEC §1.1 side codes, price, qty, route, account) | columns by header NAME; FIFO pairing per symbol/direction, trade closes at position 0 (SPEC §2 row 1) → `Trade` + exit `Leg`s | unknown/missing column, unknown side code, unparseable time/number, a position going through 0 to the other side in one execution (unless E1 shows DAS books that), a carried position the file contradicts, or a mixed-date file = the whole import FAILED naming file + line; a position left open at file end = an `OPEN` trade carried to the next day (R67, §3), never a failure; a header change = `degraded: das_export_shape` flag (L9). Order-log rows → `stop_moves` only if E1 proves they are in the file (F32 UNPROVEN) |
| TradeZella screenshot | `TradeStatsSource` → `TradeStats` | MVP: nothing read from the image — it is bound to a trade, embedded in the note, and its typed cells (if he types them) are the figures. OCR (Apple Vision via `pyobjc-framework-Vision`, or tesseract) = a NEW dependency, a later slice, in shadow beside his typed cells (CLAUDE.md: extracted figures need their verbatim source) — **O1** | not an image / unreadable / zero bytes = that file FAILED; a trade without a screenshot keeps the day `waiting` |
| ASET cards | existing `AsetStore.for_date` (F18) — the DB, not the note fences (F19; L3) | nearest prior card, same ticker+direction, within `limits.card_match_window_minutes` (SPEC §2 key) | DB unreachable = build FAILED; a trade with no card = `card: none` shown (a rule-1 fact, not an error) |
| Daily-note premarket block | new `PremarketSource` reading keyed lines only (F21) | `Sleep:`, `Readiness:`, `RHR:`, `1% goal:` | a missing key renders `not given`; never inferred (SPEC §9); keys that do not exist (meditated, tone, hotkey, sleep hours) → **O11** |
| Rules | existing `regenerate_rules_config()` (F20) | numbered rules + tags | as today (loud, line-numbered). Dated temporary rules need new syntax → later slice |
| v3 legs (after S3 C1/C2) | `legs_current_v` per v3 (F25) | Cobalt's estimated/confirmed legs + his held-count statements | absent (not built yet) = reconcile section says `legs: not built`, no write |
| Carried positions | `drc_rows` of the prior DRC day | open trades with held shares (R67) | a carried position with no prior row = FAILED naming the symbol (never assumed flat) |

**Seam with v3 C1/C2 (R67).** S-C1: C1's `legs` DDL carries a source value `das` and a nullable source-id column (the `drc_imports` row) so a DAS correction names its source (L57) — C1's migration set, not a DRC migration. S-C2: C2's correction writer accepts a DAS-sourced correction and a DAS-sourced NEW exit leg under the same row lock and refusals; a held-count statement is a history row the DAS correction supersedes, never deletes. S-C2b: running shares may stay > 0 across days (open position); C2's CLOSED check runs only on 0. D5 (§9) is gated on C2 merged.

**Clock seam.** Rule 1 compares a card's `created_at` (Mac clock) with the first DAS fill time (trading-PC clock, timezone per export). Seconds matter (`card_lead_seconds`, SPEC §2). Skew and timezone are UNPROVEN → E4.

## 5. DERIVED FIELDS AND THE RULE ENGINE

**SPEC §2, mapped.**

| SPEC §2 key(s) | Exists today | This slice | Later |
|---|---|---|---|
| trade_id, ticker, side, entry/exit time, hold, avg entry/exit, shares, gross/net P&L, commissions, legs | — | NEW from DAS (confirmed data, his export) | — |
| card_id, grade_at_card, planned stop/entry, risk budget, planned shares | `aset_sizings` (F18) | card match | — |
| card_first, card_lead_seconds, card_regenerations | card timestamps exist | NEW (after E4) | — |
| planned/actual risk, risk_overrun_pct | fill recompute on the card (`aset/store.py:185-257`) | NEW over DAS fills | — |
| planned_R, realized_R | v3 `realized_r.1` over legs (F25) | realized R = the SAME pure function fed DAS legs (one formula, L3); planned R needs a target → typed cell or `untested` | — |
| MAE, MFE, exit_efficiency, best_exit_gap_R | — | typed cells only (O1) | OCR |
| window | — | NEW from `windows.*` (SPEC §7 keys) | — |
| seat_state_at_entry, thesis_key, attempt_number, consecutive_losses_before | — | NEW (pure, from the day's DAS trades) | correlated flag needs the sector map |
| stop_moves, discretion_delta_R | v3 `card_stop_edits` (Cobalt-side only) | — | DAS order log (if E1) |
| known_family, written_exit_exists | — | — | setup-sheet reads |

Every derived value is stored with its inputs and the function id that computed it (L57) in `"user".drc_rows` (declared, F23): one row per trade, one per day, JSON `inputs` + `derived` + `fn_version`. No number is re-derived in the note that is not in the row.

**Rule engine.** Rules are data: rule text and numbers from `Rules.md` (F20); thresholds from his config (SPEC §7 keys `account.*`, `grades.*`, `windows.*`, `limits.*`, `goal.*`, `sleep_trigger.*`) — his config, home `"user".trader_settings` (`settings/models.py:107`) loaded by his own `cobalt settings load --apply` (L28 as amended 09-15), Pydantic schema + dry-run (L10); never a committed value (L32, L53). Checkers are code keyed by a stable checker id; the binding `rule number → checker id` is his config (renumbering a rule is his edit, not ours) — **O7**. Result per trade/day: `pass | fail | untested | needs_voice` (SPEC §3).

This slice's checkers (all inputs present from DAS + cards + config): rules 1, 2, 4, 5, 8, 9, 12, and rule 3's R:R half when a target is given. `untested` this slice: 6, 10 (correlation), 11, opening window, temporary rules, sleep trigger. `needs_voice`: 3's structure half, 7's content, 11's structure.

**L7.** Today adherence is his checkboxes (human-fed). The engine's pass/fail renders in its OWN unit BESIDE his checkboxes, labelled shadow, for N sessions; agreement per rule shown with its n (L8); his checkboxes retire only on his HITL approval (L61 interim). N and "agreement" = **O13**.

## 6. THE NOTE

**Template.** His `5 - Templates/DRC.md` is THE template (R65 d). Cobalt reads it at build time, substitutes ONLY `{{date:YYYY-MM-DD}}` tokens (F5); any other `{{` token = loud failure naming the line (L1); no Templater execution. `configs/cobalt/templates/drc.md.j2` dies (L3). His example trade blocks and example If/Then (F5) would copy into every DRC → **O8** (keep, or the desk removes them on his word, L65).

**Sections mapped onto `DRC-2026-09-21.md`'s headings.**

| Heading (his) | Writer | Unit |
|---|---|---|
| title, date, `### Tickers:` dataview, `### Theme:` embed | HIS (template) | — |
| NEW: directly under the date line | COBALT | `drc-summary/summary` — rules line FIRST (engine result, shadow-labelled, SPEC §5.1 item 1), net P&L from DAS, W/L, trades, cards written / taken, screenshots bound |
| `### My GOAL for today:` + `Grade:` | HIS — never touched | — |
| `### How I managed risk:` · `### PnL on the day:` | HIS text; the heading's placeholder is his (**O16**) | `drc-risk/risk_parameters` (existing, kept) |
| `### Catalyst + Set Up + Trades` | COBALT scaffold + HIS answers inside it (today's shape, F3) | `drc-trades/tickers` REBUILT: one block per DAS trade — derived table, matched card, legs, flags (SPEC §5.1 item 3 keys), screenshot embed `![[_imports/drc/<date>/<file>]]`, then his blank voice lines (SPEC §1.2 per-trade keys) — inside-unit vs his own block = **T6 / O9** |
| same | COBALT | `drc-trades/reconcile` — per trade: DAS legs vs Cobalt legs (v3) — the mismatches as found (before), then "adjusted to DAS: k rows (ids)" (R67, §3); his taps / held-count statements listed as history |
| same | COBALT | `drc-trades/open_positions` — every position open at the DRC (R67): symbol, side, held shares, trade_id, day opened; on the next day's DRC the same trade appears as `continuing open position` until closed |
| `### Technology:` · `### Collaboration:` · both `### What I learned` · `### Selectivity notes:` · `### Tomorrow's one percent better:` | HIS — never touched | — |
| `### Cobalt Rules Check` (heading exists only in the repo copy — his template lacks it, F4) | COBALT | `drc-rules/rules_check` (existing: his checkboxes + card reconcile, now "cards with no DAS trade") · NEW `drc-rules/rule_engine` (shadow, §5) |
| after `drc-rules` | COBALT (replay) | `drc-misses/miss_line` (existing, §8) |

**Voice / narrative (SPEC §1.2).** Today he gives it in the DRC chat. MVP proposal: no voice pipeline — he types into the blank lines in the note (as today) or dictates in the DRC chat. Later slice: the local voice stack captures per-trade and per-day blocks, stored verbatim beside parsed fields (SPEC §9), corrections to any auto value logged as overrides with reason. Channel and timing = **O10**.

## 7. LEDGERS (SPEC §4)

| Ledger | This slice | Later |
|---|---|---|
| Streak | the day row in `drc_rows` (DRC built or not, by date) | render |
| Rule breaks per day/rule | engine rows (shadow), core vs new split needs rule age → later | ✓ |
| Sniper tally, grade-accuracy, discretion audit, exit efficiency, rule-10 ledger, prevented column, playbook instances, goal progress | — | each a slice; every rate with its n, n<30 = `insufficient data` (L8) |
| `trades.jsonl` / `days.jsonl` (SPEC §5.2) | NOT built — Postgres is the store; a file export is **O17** | — |
| Weekly pack (SPEC §5.3) | — | ✓ |

## 8. WHAT DIES, WHAT IS REUSED

- **15:40 job** (`com.cobalt.prefill-drc`, F1): its CREATE step dies (R66 b). With no note it has nothing to upsert (F7), so the whole plist retires: `launchctl bootout`, plist removed from `ops/`, row removed from `jobs.yaml:181-186` and `:310` readers, S2 smoke rows `s2.yaml:436-438` replaced by a `drc build` check. RESTARTS: that job (removed) + `com.cobalt.aset` (L42).
- **Its three units** are REUSED by the build: `format_risk_parameters`, `format_rules_checkbox_block`, `format_card_reconcile_block`, the three placements (`prefill/drc.py:248-347`). `format_tickers_block` is replaced (cards → DAS trades). `parse_fill_updates` (`:70`) and `find_trade_note_for_card` (`:101`) leave the DRC path (DB fill columns; v3 `trade_note_path` seam). `run_drc_prefill` becomes `run_drc_build(event)`; `uv run prefill drc` is retired for `cobalt drc build` (one CLI).
- **21:10 miss line** (F10, F11): unchanged when the note exists. When it does not, today's run FAILS every such night — wrong under R66. Proposal: `line_step` on an absent note records `line: pending (no DRC)` and ends green; the DRC build, when it runs later, calls the SAME `render_line` + `write_miss_line` for that date from the replay's persisted rows (`missed.current`, run result) — whether every `render_line` input is persisted is UNPROVEN → E6; **T3**.
- **09:00 reader** (F12): unchanged. A day he did not import reads `no prior DRC` (loud, steps down) — consistent with R66. What it quotes stays packet Q10/Q11 (his).
- **Repo template** `drc.md.j2`: dies (§6). **S2 smoke** `s2.yaml:383-398` (miss unit present): keyed to a built DRC, else `pending`.
- **Charter F14 / S3 smoke "exists at 15:41"** (F28): re-worded to "exists within the build timeout of the second input placed" — his ruling (**O18**).

## 9. CHUNKS

This week (R60) — the MVP only. Seats: Opus 5 floor on every write-path chunk, never auto mode on a write path (L29). Hours are seat hours; a fix round ≈ 0.4× on each (v3's own pattern).

| Chunk | Files | Write path | Migration | RESTARTS | h |
|---|---|---|---|---|---|
| D1 DAS parser + pairing (incl. carried open positions, R67) + models + stores | new `src/cobalt/drc/{das.py,models.py,store.py}`; real-shape fixture from E1 (redacted, L45/L32); one `db_migrations` file + `.rollback.sql`: `"user".drc_imports` (+ event state), `"user".drc_fills` (DAS executions; name vs declared `fills` = **T4**), `"user".drc_rows`; `placement.py` entries | DB — yes | YES — one set; number the desk's at L68 (≥ the stacked branches') | none (library) | 7 |
| D2 Import page + trigger | `aset/web.py` (`GET /drc`, `POST /drc/import`), `src/cobalt/drc/imports.py`, `pyproject.toml` (direct `python-multipart`) | vault `_imports/` + DB — yes | — | `com.cobalt.aset` | 7 |
| D3 Build + note | `src/cobalt/drc/build.py` (his-template reader, create-if-absent, units §6, derived + engine rows §5), `prefill/drc.py` (reused helpers; create step removed), `replay/runner.py` line-step pending + build hook, `cli.py` (`cobalt drc build`), `drc.md.j2` deleted, `ops/com.cobalt.prefill-drc.plist` retired, `jobs.yaml`, `smoke/s2.yaml` | vault + DB — yes | — | `com.cobalt.prefill-drc` (retired), `com.cobalt.replay`, `com.cobalt.aset` | 9 |
| D4 DRC config family | `settings/models.py` keys + Pydantic schema for SPEC §7 key families, checker binding, dry-run (`cobalt drc build --dry-run`) | DB (settings loader) — yes | none if the settings table is key-value (UNPROVEN → read at build) | readers of trader_settings per `jobs restarts` (L42) | 4 |
| D5 Reconcile writes to legs (R67) | `src/cobalt/drc/reconcile.py` calling C2's correction writer; reconcile + open-position units | DB (`legs`) + vault — yes | none of its own (S-C1 rides C1's set) | `com.cobalt.aset` | 5 |

This slice: 5 chunks, 32 h seats (≈ 45 h with one fix round each). Order: E1–E4 → D1 → D4 ∥ D2 → D3; D5 after v3 C2 is merged (S3 window, 09-24 →). D1 cannot start before E1 (L45: the real shape exists; no invented fixture). Until D5 lands, the reconcile unit shows the diff only and says `adjustment pending (legs writer not built)`.

Later slices (named, not proposed as this week's build): **L1** TradeZella OCR (new dependency, shadow vs typed) · **L2** DAS order log → stop_moves + discretion audit (if E1) · **L3** voice capture per trade / per day · **L4** ledgers + weekly pack (SPEC §4, §5.3) · **L5** premarket keys + sleep trigger + opening window + dated temporary rules (Rules.md syntax) · **L6** sector/correlation map (rule 10 correlated half) · **L7** daily-note 3-line stub + wider 09:00 quote (packet Q10, Q12) · **L8** setup-sheet reads (rule 11 written exit, known family).

## 10. FIRST-GATE EXPERIMENTS (L70) — every "not checkable from reads"

| # | Before | What | Pass / what changes |
|---|---|---|---|
| E1 | D1 | one real DAS export from him (any recent day): header, side codes, time format + zone, account column(s), whether order-log rows share the file, whether a day-file starts flat or lists overnight positions (R67 carry) | columns named → fixture cut (values stripped, L45 companion); order log absent → L2 needs a second export or dies |
| E2 | D2 | one real TradeZella screenshot: which SPEC §1.1 row 2 fields are legible on the stats panel | decides O1's typed-cell list; OCR accuracy only if O1 = OCR |
| E3 | D3 | on the dev vault: render his template with only the date token substituted, run the three existing placements + the new ones | every unit lands under its heading, no other `{{` token, his lines byte-identical |
| E4 | D1 | one card created in ASET vs the same trade's first DAS fill time | skew + zone known → `card_lead_seconds` trustworthy, or rule 1 gets a tolerance key |
| E5 | D2 | multipart `UploadFile` in the dev ASET app with the transitive `python-multipart` | works → pin direct; fails → the dependency is added knowingly |
| E6 | D3 | replay line re-rendered for a date from persisted rows only, after the run | same bytes as the 21:10 render → T3's hook holds; else the build reruns replay's line step |
| E7 | D2 | which aset config production loads (`aset.local.yaml` bind `lan`?), and a >1 MB PNG POSTed from the trading PC over the LAN | reachable; else the page is used from the Mac and the CSV travels by his own means |
| E8 | D3 | build twice with a trade removed between, his text typed inside the removed block | his text kept + listed; no silent loss |

## 11. OWNER ITEMS (his, one per message)

O1 TradeZella figures: typed cells (MVP) vs OCR (new dependency) · O2 file home: vault `_imports/drc/<date>/` vs a non-synced data directory · O3 a no-trade day: what counts as "both placed" (SPEC §9 streak vs R66 "no inputs, no DRC") · O4 which DAS accounts count · O5 ONE source for the daily stop and grade dollars (today: `daily.md.j2:18`, Rules.md rules 2/12, the ASET sheet-mode config, SPEC §7 `account.*`/`grades.*`) · O6 config home: `trader_settings` vs a keyed unit in his note · O7 rule number → checker binding · O8 his template's example blocks · O9 his per-trade answers inside Cobalt's unit vs his own block · O10 voice channel and timing · O11 premarket keys (meditated, tone, hotkey, sleep hours vs the `Sleep:` value) · O12 the packet questions still his: Q2 (confirm "none" from R65 b), Q4, Q5, Q6, Q7 (SPEC's session-score segments?), Q8 (SPEC §4 rule-10 / prevented as the definition?), Q10, Q11, Q12, Q13, Q14 · O13 rule-engine shadow length N + agreement definition · O14 inputs dropped inside `market_reset` · O15 consent to a redacted real-shape DAS fixture in git · O16 the PnL heading placeholder: his, or Cobalt fills it · O17 `trades.jsonl` / `days.jsonl` files wanted beside Postgres · O18 Charter F14 / S3-smoke "15:41" wording · O19 the diff model (§13): KEEP / MERGE / DROP and WRITER per row, and which additions (C) stay — ruled BEFORE the tribunal (R68).

Packet §4 against the spec + rulings: answered — Q1 (R65 a/d), Q3 (R65 d), Q9 (SPEC §2: P&L from fills → DAS, confirmed), Q15 (R65 c). Partly — Q2 (R65 b reading), Q7 (SPEC §1.2 per-day session scores), Q8 (SPEC §4). His — the rest (O12).

## 12. L52

Nothing this slice builds feeds a score, a rank, an admission, a grade or a size: no chunk touches `cards/scoring.py`, `cards/radar.py`, `radar/evaluate.py`, `aset/engine.py` or `daymode/propose.py`. The DRC reads cards and writes a review note, review rows and (D5, R67) leg corrections through v3's own writer — records the card DISPLAYS (realized R, running shares), never an input to its score. **Reaches scoring: no.** Named boundary for later: SPEC §3's sleep trigger (key `sleep_trigger.effect`) and any use of rule results or grade-accuracy in the 09:00 proposal WOULD gate sizing — each is a trading-logic change (L7 shadow + HITL) and, reaching the card, an L52 tribunal first.

## TRIBUNAL — open items (T)

T1 import place = `/drc` on the ASET app + files in vault `_imports/` · T2 build synchronous in the request vs a one-shot job · T3 replay line on an absent note → `pending`, rendered later by the build · T4 table names (`drc_fills` vs declared `fills`, v3 O16) and the `public.trades` collision · T5 engine as L7 shadow beside his checkboxes · T6 his answers inside a Cobalt unit across rebuilds · T7 DAS-vs-legs reconcile per R67: shown, then written as correction / new-leg rows through C2's one writer, source named; seams S-C1 / S-C2 / S-C2b (R66 sets aside v3 `:237` for this reconcile only) · T11 open-position carry: pairing seeded from the prior `drc_rows`, one trade_id across days, no unrealized P&L invented · T8 template reader: date token only, repo copy dies · T9 one source for the daily stop / grade dollars (L3; O5 is his value, the mechanism is the tribunal's) · T10 S2/S3 smoke re-keyed to the input-driven build.

## 13. DIFF MODEL — current DRC vs coach spec (R68; he rules this BEFORE the tribunal)

Keys and line refs only (L32). `DRC:n` = `DRC-2026-09-21.md` line n; `SPEC §n` = the coach spec. ACTION = KEEP · MERGE → (target) · DROP. WRITER = **AUTO** (Cobalt populates; source named) · **PRE** (Cobalt drafts, he edits) · **HIS** (judgment only he can give). His default applied: AUTO wherever data exists; HIS only where no data can say it. No row is DROPped: every coach item survives as its own row or inside a named MERGE target.

### (A) SECTIONS

| # | Item | Today | ACTION | WRITER · source |
|---|---|---|---|---|
| A1 | title line | DRC:5 | KEEP | AUTO · his template |
| A2 | date line | DRC:7 | KEEP | AUTO · template date token |
| A3 | `### Tickers:` dataview | DRC:9-14 | KEEP | AUTO · Obsidian dataview over trade notes |
| A4 | `### Theme:` embed (target folder empty, packet §2) | DRC:15-17 | MERGE ← SPEC §5.1-2 market tone | AUTO · embed re-pointed to the day's daily note `### Market Context:` (`daily.md.j2:51`) |
| A5 | `### My GOAL for today:` + one-goal prompt | DRC:22-24 | MERGE ← SPEC §1.1 row 4 goal, §5.1-2 goal | PRE · daily note `1% goal:` key |
| A6 | goal-format prompts (sentences / specific) | DRC:27-29 | MERGE → A5 | template prompt text, unchanged |
| A7 | progress-toward-goal summary + paragraph | DRC:32-35 | MERGE ← SPEC §4 goal progress | PRE · metric line from config `goal.metric` over the day's tags (count AUTO, tags HIS, n shown); paragraph HIS |
| A8 | `Grade:` + why prompt | DRC:38-40 | MERGE ← SPEC §1.2 per-day overall score | HIS (self-grade; the 09:00 reader's source, F12) |
| A9 | `### How I managed risk:` prompt | DRC:45-47 | KEEP | PRE · facts above his paragraph: planned vs actual risk, overrun flags, distance to daily stop, rules 2/10/12 results (DAS + cards + engine) |
| A10 | `### PnL on the day:` | DRC:49 | KEEP | AUTO · DAS net P&L (placement O16) |
| A11 | risk-parameters unit + allocation prompt | DRC:51-57 | KEEP | AUTO · sheet-mode config + cards (existing unit) |
| A12 | `### Catalyst + Set Up + Trades` | DRC:62 | KEEP | per trade → table (B) |
| A13 | cards written · trades taken | DRC:66 | KEEP | AUTO · `aset_sizings` + DAS trades |
| A14 | `### Technology:` (2 prompts) | DRC:167-169 | KEEP | HIS |
| A15 | `### Collaboration:` (3 prompts) | DRC:173-179 | KEEP | HIS |
| A16 | `### What I learned (from the trading day)` (3 prompts) | DRC:183-189 | MERGE ← SPEC §1.2 per-trade mistakes/lesson | PRE · his per-trade lesson lines gathered; paragraph HIS |
| A17 | `### What I learned (from myself)` (3 prompts) | DRC:193-199 | KEEP | HIS (SPEC §9: nothing inferred about state) |
| A18 | `### Selectivity notes:` passed-on ticker + why | DRC:203-205 | MERGE ← SPEC §1.2 passes, §4 prevented column | PRE · list AUTO: cards with no DAS trade, radar cards passed/expired (`card_transitions`), engine-detected stand-downs/cooldowns; reasons HIS |
| A19 | passed-on: mistake not repeated | DRC:206 | KEEP | HIS |
| A20 | `### Tomorrow's one percent better:` If / Then / Because | DRC:211-223 | MERGE ← SPEC §1.2 tomorrow's goal / IF-THEN | HIS |
| A21 | `### Cobalt Rules Check` checkboxes | DRC:228-244 | KEEP | AUTO · Rules.md (existing) + engine shadow unit (§5) |
| A22 | card reconcile (taken / passed / discarded) | DRC:246-249 | KEEP | PRE · "taken" AUTO from DAS match; passed vs discarded HIS |
| A23 | miss line | unit `drc-misses` | KEEP | AUTO · replay 21:10 (§8) |
| A24 | header: rules line first, W/L, sniper x/y | SPEC §5.1-1 | MERGE → summary unit (§6) | AUTO (rules, W/L from engine + DAS); sniper x/y count AUTO over HIS tags |
| A25 | premarket block: sleep, meditated, tone, goal, sheet mode / hotkey file, score | SPEC §5.1-2, §1.1 row 4 | NEW section under A5 | PRE · daily note keys (F21), sheet + hotkey from the day-mode attestation row; meditated / tone per O11; score HIS |
| A26 | session scores (premarket + four blocks + overall) | SPEC §1.2 per day, §5.1-4 | NEW section | PRE · copied from the daily note's `Score -` lines (`daily.md.j2:84-99`); the grades are HIS (packet Q7) |
| A27 | playbookable trade | SPEC §1.2, §5.1-8 | NEW section | PRE · candidates AUTO (trades with every auto rule `pass`); choice HIS |
| A28 | disputes / correction lines | SPEC §1.2, §8 step 8 | NEW unit | HIS input; AUTO override log with reason (SPEC §9) |
| A29 | next-day review grade per trade → grade log | SPEC §1.2, §5.1-7, §4 | NEW section on the prior DRC | HIS grade; AUTO slot + miss direction vs grade at card |
| A30 | discretion audit entries | SPEC §5.1-6, §4 | NEW section | PRE · stop moves AUTO (DAS order log if E1; v3 stop edits); structure HIS |
| A31 | open items carried forward | SPEC §5.1-10 | NEW section | AUTO · open positions (R67), unanswered reconcile, `needs_voice` rules, unresolved leg mismatches, prior DRC's empty HIS rows |
| A32 | streak | SPEC §4 | MERGE → summary | AUTO · `drc_rows` day rows |
| A33 | rule-break ledger (core vs new) | SPEC §4 | weekly | AUTO · engine rows (shadow) |
| A34 | sniper tally vs target | SPEC §4 | weekly | AUTO count over HIS tags, n shown (L8) |
| A35 | exit-efficiency distribution | SPEC §4 | weekly | AUTO when MFE present (O1), n |
| A36 | rule-10 ledger (cost vs prevented) | SPEC §4 | weekly | PRE · counts AUTO, cost instances HIS (voice) |
| A37 | playbook instances per setup | SPEC §4 | weekly | AUTO · setup key per trade, n |
| A38 | structured trade / day records | SPEC §5.2 | KEEP as DB | AUTO · `drc_rows` (file export O17) |
| A39 | weekly review pack | SPEC §5.3 | separate weekly note (later slice) | AUTO |

### (B) PER-TICKER — `### Catalyst + Set Up + Trades` block vs SPEC per-trade fields

| # | DRC bullet (DRC:68-162 shape) | SPEC field | ACTION | WRITER · source |
|---|---|---|---|---|
| B1 | `Ticker:` | §2 ticker, trade_id | KEEP | AUTO · DAS |
| B2 | `Entry #n — time` | §2 entry_time, attempt_number, thesis_key | MERGE (n = attempt per thesis) | AUTO · DAS + card time |
| B3 | re-entry #2 what's-new line | §1.2 re-entry what's new, §6 what_new | KEEP | HIS (presence AUTO-checked, rule 7) |
| B4 | Grade · Direction · Sheet mode | §2 grade_at_card, side; §6 card.sheet_mode | KEEP | AUTO · card |
| B5 | Entry · Stop · Shares · Risk budget | §2 planned_entry, planned_stop, planned_shares, risk_budget | KEEP | AUTO · card |
| B6 | Fill update | §2 avg_entry, shares (actual) | MERGE → plan-vs-DAS line | AUTO · DAS + `aset_sizings` fill columns |
| B7 | `Catalyst:` | §1.2 catalyst | KEEP | PRE · daily-note Trade Ideas `Catalyst` column (`daily.md.j2:65`) / radar card WHY |
| B8 | `Set Up:` | §1.2 setup name, §6 setup_family / setup_name | KEEP | PRE · card `trade_def` (v3 seam 2) / trade note / TZ tag |
| B9 | `Trade Notes:` | §1.2 read at entry + flip condition | MERGE → "read / flip" | HIS |
| B10 | `Keys to success here:` | — (no SPEC field) | KEEP | HIS |
| B11 | setup + self observation | §6 narrative (verbatim) | KEEP | HIS (SPEC §9) |
| B12 | ideal vs actual dots on chart | §1.2 entry self-tag (closest) | KEEP + NEW tag line (B15) | HIS |
| B13 | `Insert Chart with Executions:` | §6 attachments | KEEP | AUTO · embed of the dropped screenshot |
| B14 | excitement question (reversion-tagged only, `prefill/drc.py` scaffold) | — (no SPEC field) | KEEP | HIS (packet Q14) |
| B15 | — | §1.2 entry self-tag | NEW bullet | HIS (config enum) |
| B16 | — | §1.2 exit reasoning, §6 exit_structure | NEW bullet | HIS (config list offered) |
| B17 | — | §1.2 stop-move structure | NEW line per stop move | PRE · time/price AUTO (order log, E1); structure HIS |
| B18 | — | §1.2 mistakes / lesson | NEW bullet | HIS (feeds A16) |
| B19 | — | §2 exit_time, hold_minutes | NEW line | AUTO · DAS |
| B20 | — | §2 avg_exit, gross/net P&L, commissions | NEW line | AUTO · DAS |
| B21 | — | §2 legs / scale events, R at exit | NEW table | AUTO · DAS (+ reconcile R67) |
| B22 | — | §2 card_first, card_lead_seconds | NEW line | AUTO · card + DAS (E4) |
| B23 | — | §2 card_regenerations | NEW line | AUTO · `aset_sizings` |
| B24 | — | §2 planned/actual risk, risk_overrun_pct | NEW line | AUTO |
| B25 | — | §2 planned_R, realized_R | NEW line | AUTO · `realized_r.1`; planned R needs a target (typed / TZ) |
| B26 | — | §2 MAE, MFE, exit_efficiency, best_exit_gap_R | NEW line | AUTO when typed/OCR (O1) |
| B27 | — | §2 window | NEW line | AUTO · config windows |
| B28 | — | §2 seat_state_at_entry | NEW line | AUTO · DAS day |
| B29 | — | §2 consecutive_losses_before, minutes since last loss | NEW line | AUTO |
| B30 | — | §2 stop_moves, positive_pnl_stop | NEW table | AUTO · order log (E1) |
| B31 | — | §2 discretion_delta_R | NEW line | AUTO |
| B32 | — | §2 known_family, written_exit_exists | NEW line | AUTO · setup sheets (later slice) |
| B33 | — | §6 rule_results per trade | NEW line | AUTO · engine (shadow) |
| B34 | — | §5.1-3 flags (card after fill, regenerations, overrun, winner→loser, late tag at size) | NEW line | AUTO (late-tag flag needs HIS tag) |
| B35 | — | §1.2 next-day review grade, §6 grade_review | NEW line (next day) | HIS |

### (C) ADDITIONS — neither has them; all PROPOSED

| # | Addition | Source | n rule (L8) |
|---|---|---|---|
| C1 | pick vs Cobalt's rank per filled card | `picks` rows (`cards/picks.py`) | per-day list; agreement rate only at n≥30 |
| C2 | realized R confirmed after the DAS reconcile (no longer provisional) | v3 `realized_r.1` over reconciled legs | per trade; averages n≥30 |
| C3 | "R had Cobalt's stop held" | v3 seam 7, 21:10 replay | per trade; Σ with n |
| C4 | stop gap: his stop vs Cobalt's structural stop | v3 `stop_in_force` − `structural_stop` | per trade |
| C5 | plan-vs-fill drift | `aset_sizings.distance_change_pct` vs DAS avg entry | per trade |
| C6 | the day's radar cards (armed / triggered / expired / missed) linked to trades | `card_transitions`, `missed` | counts with n |
| C7 | human-only dot per card, shown as his (L11) | card dots | — |
| C8 | logging accuracy: his taps / held-counts vs DAS mismatches | R67 reconcile rows | weekly rate, n≥30 |
| C9 | P&L and R by window (config windows) | `drc_rows` | weekly, n per window; <30 = insufficient data |
| C10 | expectancy per setup | `drc_rows` × setup key | n≥30 else insufficient data |
| C11 | all-rules-pass streak (shadow) | engine rows | count days |
| C12 | TradeZella vs DAS P&L cross-check flag | typed TZ figure vs DAS | per trade |
| C13 | tomorrow's If/Then offered into the next daily note's blank `1% goal:` (L28 clause 2a, blank → value only) | A20 | — |

None of (C) feeds a score or rank; all are displays / review rows (§12 unchanged).
