# drc-design-2026-09-22 — DRC automation proposal (seat `drc-design-0922`, Opus 5.5)

## §0 Headline
- WROTE `docs/30 - Design/DRC-AUTOMATION-PROPOSAL-2026-09-22.md` (298 lines, keys only; §13 DIFF MODEL added 15:55 ET on R68, verified at `cto-2026-09-22.md:35`: 39 section rows + 35 per-ticker rows, 13 PROPOSED additions, nothing of the coach spec dropped) + `docs/_inflight/drc-automation-values-2026-09-22.md` (`no values needed`; gitignored — `.gitignore:43-45` `!docs/_inflight/` · `docs/_inflight/*` · `!docs/_inflight/README.md`). Nothing built, nothing committed, no DB / vault / git write.
- Design: ONE import page `/drc` on the existing ASET app (FastAPI, `aset/web.py:83`); DAS CSV + one TradeZella screenshot per trade → typed event → the build creates the DRC from HIS template; the 15:40 job retires; R67 folded (DAS reconciles legs; open positions carry).
- 5 chunks (32 h seats, ≈45 h with fix rounds), 1 migration, no new dependency, reaches scoring: no. 11 tribunal items, 19 owner items (O19 = rule the diff), ESCALATE 6.
- Written 15:48–15:52 ET. R67 folded on the desk's message (verified at `cto-2026-09-22.md:35`).

## UNPROVEN rows (each = a first-gate experiment, L70)
| Claim | Where | Experiment |
|---|---|---|
| The DAS export's columns, side codes, time zone, account column | no sample on host (F31) | E1 |
| The export carries the order log (stop moves) in the same file | SPEC §1.1 row 1 (F32) | E1 |
| A DAS day-file starts flat (needed for the R67 open-position carry) | — | E1 |
| Which TradeZella stats-panel fields are legible | no sample on host | E2 |
| The three existing placements land correctly on HIS template's text | `prefill/drc.py:321-347` vs `5 - Templates/DRC.md` | E3 |
| Trading-PC vs Mac clock skew / zone (rule 1 needs seconds) | — | E4 |
| Multipart `UploadFile` works with the transitive `python-multipart` | `uv.lock:2879` | E5 |
| Every `render_line` input is persisted after the replay run | `replay/runner.py:443-455` | E6 |
| Which aset config production loads (`bind: lan`?) and LAN upload from the trading PC | `configs/dev/aset.local.yaml:28` | E7 |
| His text inside a removed trade block survives a rebuild | L28 merge, `vaultwrite/writer.py:644-661` | E8 |
| What the daily note's `Sleep:` value measures (hours vs score) | `1- Daily Notes/2026-09-21.md:11` | O11 (his) |
| The trader_settings table takes new keys without a migration | `settings/models.py:107` | read at D4 |
| `0014`/`0015` numbers claimed by H1 / stale-score / S3 M1 | text only | the desk at L68 |

READING:
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` (full, L1–L74)
- `docs/40 - DevDocs/prompts/2026-09-22/38-propose-drc-automation.md`; `docs/40 - DevDocs/reports/cto-2026-09-22.md` §4 R58–R67, :193-198
- `docs/_inflight/DRC-automation-spec-2026-09-22.md` (whole)
- `Vault/Think/1 - Trading/5 - Review/DRC-2026-09-21.md` (whole); `5 - Review/Rules.md`; `5 - Templates/DRC.md` (whole); `5 - Templates/Daily.md` (headings); `1 - Trading/1- Daily Notes/2026-09-21.md` (keys + headings only)
- `docs/30 - Design/DRC-SITTING-PACKET-2026-09-21.md` §1–§6
- `docs/90 - References/trade-reporter/`: `app.py`, `README.md`, `templates/index.html` (drop zones), `static/js/app.js` (drop/paste/POST lines), `utils/drc_builder.py` (signatures + dict keys)
- main code: `prefill/drc.py`, `prefill/config.py:30,110-112`, `prefill/rules_gen.py`, `configs/cobalt/templates/drc.md.j2`, `daily.md.j2:7-50`, `daymode/drc.py:85-144`, `replay/line.py:1-45,64,155-177`, `replay/runner.py:430-474`, `vaultwrite/writer.py:380-679`, `vault.py:92-116`, `aset/web.py` (routes, :1-24, :83, :947), `aset/__main__.py`, `aset/store.py` (defs), `cards/picks.py` (defs), `settings/models.py` (defs), `db_migrations/placement.py:100-154`, `ops/com.cobalt.prefill-drc.plist`, `ops/com.cobalt.replay.plist`, `ops/com.cobalt.daymode-propose.plist`, `ops/start_aset.sh`, `configs/dev/aset.yaml`, `configs/cobalt/smoke/s2.yaml` (drc rows), `configs/cobalt/jobs.yaml` (drc rows), `pyproject.toml`, `uv.lock` (grep)
- `git log --all` on `src/cobalt/db_migrations/00*.sql`
- `docs/30 - Design/S3-EXITS-v3-2026-09-22.md` (grep: F-rows, §3, :164-168, :228, :237, :253-256)
- `docs/00 - Project/MVP-CHARTER-v0_2.md:155-185`; `SPRINT-LADDER-v0_1.md` S3 rows :606-623

## ESCALATE
1. **A committed file carries one of his values.** `configs/cobalt/templates/daily.md.j2:18` hard-codes a daily-stop dollar line (L32 user data in the repo; L53 a cap settled in a file). It is also one of FOUR sources of the same number (with Rules.md rules 2/12, the ASET sheet-mode config, SPEC §7 `account.*`/`grades.*`) — L3. Proposal O5 (value, his) + T9 (mechanism, tribunal). Not fixed here (read-only seat).
2. **SPEC §9 vs R66.** The coach's spec says a day with no trades still produces a DRC (streak); R66 says no inputs, no DRC. Proposal O3 asks what "both placed" means on a no-trade day; default until he rules = no DRC.
3. **Charter F14 and the S3 smoke require "DRC note exists at 15:41"** (`MVP-CHARTER-v0_2.md:171`; ladder `:612`, `:615-617`) — contradicted by R66 (b). Wording changes by his ruling only (O18); S2 smoke rows `s2.yaml:383-398`, `:436-438` change with D3.
4. **Lane load.** 32 h seats (≈45 h) for the DRC on top of v3 C1–C4 (30–42 h) inside S3's window (09-24 → 10-07). R60 puts the DRC in this week's lane; D5 cannot land before v3 C2. The desk's to sequence.
5. **D1 is blocked on a real DAS export (L45).** No DAS export or TradeZella screenshot exists on the host (F31). He must hand one (any recent day) before D1; its redacted real-shape fixture in git needs his consent (O15).
6. **Record correction.** `DRC-2026-09-21.md` was rendered from the repo copy `drc.md.j2`, not his Obsidian template (proposal F4) — the "Cobalt currently uses Obsidian DRC template" fact recorded at `cto-2026-09-22.md:197` does not hold for that note. For the desk's record; R65 (d) already moves the build to his template.

## CONTINUE
- FIRST (R68): he rules the §13 diff model — per row KEEP / MERGE / DROP + WRITER, and which (C) additions stay (O19). The desk records his rulings; the proposal is re-cut from them before the tribunal.
- Then the desk launches the L67 tribunal (Astra, Grok, Gemini, Fable seat) on the proposal as ruled; T1–T11 are its agenda.
- In parallel (L72): ask him for E1's DAS export and E2's screenshot (one each, any recent day) — they gate D1/D2, not the tribunal.
- Owner items O1–O18 to him one per message after the tribunal derives (O3, O5, O18 first — they touch law/acceptance text).
- No rule strings were needed; no ASK DESK raised.

## DIGEST FOR THE DESK
What he gets: a DRC that builds itself from his two files, in his own template, in the same place as today (`1 - Trading/5 - Review/DRC-<date>.md`). No PDF.
Where he drops them: ONE page, `/drc`, on the ASET app he already uses (same server, no new app). From the trading PC over the LAN, or from the Mac/laptop.
- The DAS export CSV (one per day).
- The TradeZella screenshots — the page lists the trades it read from the CSV, one drop zone per trade (drop, click or paste).
- Optional: a few typed figures only TradeZella has (MAE, MFE, target, best exit) — blank stays blank.
The page shows back: each file parsed or FAILED with the reason; trades found; screenshots still missing; then "DRC built" with the note path.
When the DRC appears: the moment the second input is complete (CSV parsed + a screenshot for every trade). One input only → no note at all, the page says what is missing. Re-dropping a file rebuilds the Cobalt parts; his typed text is kept.
What Cobalt writes in the note (marked units): a summary line under the date (rules result first, P&L from DAS, wins/losses, trades, cards); risk parameters (as today); one block per trade (derived figures, the matched card, legs, the screenshot embedded, then his blank answer lines as today); DAS-vs-Cobalt legs reconcile (R67: shown, then Cobalt's legs corrected to DAS, sources named); open positions carried to the next day (R67); rules check (his checkboxes as today) + the engine's pass/fail BESIDE them as shadow; the miss line (replay).
What stays his, never touched: goal + grade, managed risk, technology, collaboration, both learned sections, selectivity, tomorrow's 1%.
What exists already and is reused: the vault writer (create-if-absent, units, human wins), the three DRC units and their placements, the ASET card store, the Rules.md parser, the miss-line renderer, the 09:00 reader (unchanged).
What dies: the 15:40 job (`com.cobalt.prefill-drc`) — nothing left for it once the note is input-driven; the repo copy of the template (`drc.md.j2`) — his template becomes THE template. The 21:10 miss line stops failing on nights with no DRC (records "pending", written when the DRC is built).
Chunks: D1 DAS parser + trade pairing + open-position carry + tables (7 h, 1 migration) · D2 import page + trigger (7 h) · D3 build + note + retire 15:40 job (9 h) · D4 his DRC config keys, schema, dry-run (4 h) · D5 legs reconcile writes (5 h, after v3 C2). 32 h seats, ≈45 h with fix rounds. D1 waits for one real DAS export from him.
Later slices (8): TradeZella OCR · DAS stop-move history · voice capture · ledgers + weekly pack · premarket keys/sleep trigger/opening window/dated rules · sector map · daily-note stub + wider 09:00 quote · setup-sheet reads.
New dependency: none this slice (OCR would be one — his choice, O1).
Reaches scoring: no.
His (19 owner items), first: O19 the diff model (R68); then O3 no-trade day vs "no inputs, no DRC"; O5 one source for the daily stop and grade dollars (four today, one of them a committed file); O18 the "15:41" acceptance wording. Also: typed cells vs OCR, where the files live, which DAS accounts count, his template's example blocks, the packet questions still open (Q2, Q4–Q8, Q10–Q14).
Diff model (§13, R68 — his to rule BEFORE the tribunal): every heading and prompt of today's DRC plus every coach-spec item in one list (39 rows), each with KEEP / MERGE / DROP and who writes it: AUTO (Cobalt fills it, source named), PRE (Cobalt drafts, he edits), HIS (judgment only he has, e.g. the entry self-tag, self-grade, lessons, the self-observation). No DROP proposed. New sections from the coach: premarket block, session scores (copied from his daily note), playbookable trade, corrections, next-day review grade, discretion audit, open items carried. Per-ticker (35 rows): all 14 of today's bullets kept or merged; 21 coach fields added as bullets or lines (entry tag, exit structure, stop-move structure, lesson, exit time/hold, P&L, legs, card-first, risk overrun, planned/realized R, MAE/MFE, window, seat state, losses in a row, rule results, flags, review grade…). Additions (13, PROPOSED): pick vs rank, confirmed realized R, "R had Cobalt's stop held", stop gap, plan-vs-fill drift, the day's radar cards, his human-only dot, logging accuracy vs DAS, P&L by window, expectancy per setup, all-rules streak, TradeZella-vs-DAS P&L check, tomorrow's If/Then offered into the next daily note. Every rate carries its n; n<30 = insufficient data.
For the tribunal (11): the import place + file home; build in-request vs job; miss line on an absent note; table names (`fills` vs v3's strike, `public.trades` collision); engine as L7 shadow; his answers inside Cobalt's unit; R67 reconcile through v3's one correction writer (seams on C1's source column and C2's writer); template reader rules; one-source mechanism for his dollar values; smoke re-keying; open-position carry.

DRC AUTOMATION PROPOSED · chunks this week: 5 · later slices: 8 · write-path chunks: 5 · migrations: 1 · import place: /drc page on the ASET app (aset/web.py) · new dependency: none · reaches scoring: no · build estimate: 32 h · open to the tribunal: 11 · owner items: 19 · diff rows: 74 · additions: 13 · ESCALATE: 6
