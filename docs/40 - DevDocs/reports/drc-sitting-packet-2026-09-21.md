# DRC sitting packet — drafter report (2026-09-21 18:33–18:4x EDT)

Seat: `drc-sitting-packet-0921` (Opus 5) · prompt `docs/40 - DevDocs/prompts/2026-09-21/71-draft-drc-sitting-packet.md`

## §0 Headline
- Packet written: `docs/30 - Design/DRC-SITTING-PACKET-2026-09-21.md` (121 lines, ≤140). 15 decisions, 12 blocking S3-P3; no content recommended.
- Main finding: the separate DRC note ALREADY exists and Cobalt fills 3 units at 15:40 (+ the miss line at 21:10), rendered from a REPO copy of his template, not his Templater file. Two template copies exist today.
- Ladder items: 7 have a home, 4 no home yet, 1 NOT ESTABLISHED (cost-of-discipline tally).
- No personal content copied (headings and keys only, L32). No git, DB, docker, pytest or vault writes.
- ESCALATE: 2.

## Exists-today facts

| claim | path or file:line | status |
|---|---|---|
| His Templater DRC = his docx near verbatim; frontmatter key `aliases` only | `/Users/cobalt/Vault/Think/5 - Templates/DRC.md:1-187`; `docs/90 - References/DRC Template-Dejan.docx` | PROVEN |
| Theme embed targets `/6 - Permanent/<date>#Market Context:`; that folder holds only `Memory/` | `5 - Templates/DRC.md:17`; `ls 6 - Permanent/` | PROVEN (target absent); render UNPROVEN |
| SMB sheet adds segment table (Temp, 9:30-11, 11-12, 12-2, 2-4 × Grade/PTD Only/Sizing/In My Favor/Comments), reminder checkboxes, Overview, Easiest $50k, Changes I need to make | `docs/90 - References/SMB-DRC_Template.pdf` p1 | PROVEN |
| Daily template has its own segment scores (Premarket, 9:30-11, 11-1, 1-3, 3-4) | `5 - Templates/Daily.md:56-73` | PROVEN |
| 15:40 Mon–Fri prefill-drc | `ops/com.cobalt.prefill-drc.plist:50-54` | PROVEN |
| Note path `1 - Trading/5 - Review/DRC-%Y-%m-%d.md` | `configs/cobalt/prefill.yaml:8-10` | PROVEN |
| Created whole from repo `drc.md.j2` when absent (not his Templater file) | `src/cobalt/prefill/drc.py:427`, `:270-272`; `src/cobalt/prefill/config.py:30` | PROVEN |
| Repo template adds heading `### Cobalt Rules Check` absent from his Templater file | `configs/cobalt/templates/drc.md.j2:132-138` | PROVEN |
| Three units: drc-risk/risk_parameters, drc-trades/tickers, drc-rules/rules_check | `drc.py:12-16`, `:441-449` | PROVEN |
| Goal/grade/learnings/selectivity/1%/PnL untouched | `drc.py:6-7` | PROVEN |
| Cards written vs trades taken (FILLED only) | `drc.py:25-28`, `:297-313` | PROVEN |
| Counts read sheet cards (`AsetStore`) only | `drc.py:385-388` | PROVEN; whether radar cards land in `aset_sizings` UNPROVEN |
| Taken/passed/discarded checklist for cards with no fill | `drc.py:230-245` | PROVEN |
| Excitement line only on reversion-tagged trades | `drc.py:178`, `:212-215` | PROVEN |
| Miss line unit drc-misses/miss_line after drc-rules, written by replay 21:10, never creates the note | `src/cobalt/replay/line.py:1`, `:30-33`; `ops/com.cobalt.replay.plist:38-42` | PROVEN |
| 09:00 proposal reads only `Grade:` (must be A+/A/B/C) and `Goal:` (must contain a digit) | `src/cobalt/daymode/drc.py:115-116`, `:127-130`; `src/cobalt/aset/models.py:29-33`; `ops/com.cobalt.daymode-propose.plist:51-55` | PROVEN |
| His template has no line starting `Goal:` (heading is `### My GOAL for today:`) → goal never parses | `5 - Templates/DRC.md:22` vs `daymode/drc.py:116` | PROVEN by regex reading; not executed |
| Picks (pick-vs-rank) stored, not rendered | `src/cobalt/cards/picks.py:3-7` | PROVEN |
| Shadow taps stored + report | `src/cobalt/cards/shadow_report.py:1-7` | PROVEN |
| Cost-of-discipline: no store, no code | grep of `src/cobalt`, `configs/cobalt` = 0 files | PROVEN (absence) |
| Recent notes carry the 3 Cobalt sections | `1 - Trading/5 - Review/DRC-2026-09-18.md:51,64,280`; `DRC-2026-09-21.md:51,64,230` | PROVEN |
| Those notes were Cobalt-created, not Templater | inferred from the Cobalt Rules Check heading | UNPROVEN |
| S3 legs / estimated-confirmed / stop-override gap (names only) | ladder `SPRINT-LADDER-v0_1.md:590`; `cto-2026-09-20.md` R38 via ladder `:492` | PROVEN (names) |

READING:
- `LAWS.md` in full; `areas/daily-report-card.md`; `areas/cobalt-product-definition.md` (grep).
- `SPRINT-LADDER-v0_1.md` :454, :457, :492, :530-545, :586-604; `MVP-CHARTER-v0_2.md` :90-180, :371-385.
- Vault: `5 - Templates/DRC.md`, `Daily.md`, `TRADE REPORT CARD.md`; headings/markers only of `DRC-2026-09-18.md`, `DRC-2026-09-21.md`, daily note `2026-09-21.md`; heading counts of three older DRCs.
- `docs/90 - References/SMB-DRC_Template.pdf`, `DRC Template-Dejan.docx`.
- `src/cobalt/prefill/drc.py` (full), `prefill/daily.py` (grep), `prefill/config.py` (grep), `configs/cobalt/templates/drc.md.j2` (grep), `daymode/drc.py:1-150`, `replay/line.py:1-50`, `cards/picks.py:1-20`, `cards/shadow_report.py:1-30`, `aset/models.py:29-37`, three plists.
- `prompts/2026-09-21/70-propose-s3-exits.md` (grep for names only; its output not read).

## ESCALATE
1. **Acceptance vs clock:** F14 acceptance and the S3 smoke say the DRC at 15:41 carries the miss line (`SPRINT-LADDER-v0_1.md:592`, `:596-597`), but the miss line is written by replay at 21:10 (`ops/com.cobalt.replay.plist:38-42`, `replay/line.py:30-33`). The smoke as worded cannot pass at 15:41. Desk item (smoke wording or clock), not his template design. Packet does not ask him.
2. **Morning reader's goal half is dead today:** `daymode/drc.py:116` wants a `Goal:` line with a digit; his template has none, so the 09:00 proposal can only ever quote the grade (and any self-grade outside A+/A/B/C reads as unfilled and steps the proposal down, `:127-130`). Live F6 behaviour, not a defect claim beyond the regex reading (L70: not executed). Covered by packet decisions 10–11.

## CONTINUE
None — run complete.

## DIGEST FOR THE DESK
Blocking S3-P3 (1–12):
1. Which file is THE template: A his Templater file (Cobalt reads it) / B the repo copy.
2. Which SMB-only pieces join his template (segment table, reminders, Overview, Easiest $50k, Changes) or none.
3. DRC stays its own note in Review, one per day: yes / B inside the daily note.
4. His-alone sections list: confirm or change.
5. Pick-vs-rank: A per-ticker line / B own section / C drop.
6. Estimated legs to confirm: A per ticker / B in Rules Check / C own section.
7. Time blocks: A table in DRC (whose segments) / B daily note only / C drop.
8. Cost-of-discipline tally: keep (define one instance) / drop — NOT ESTABLISHED today.
9. PnL: A Cobalt from legs, provisional / B he types.
10. 09:00 quote: A grade only / B grade + 1% If-Then / C grade + goal.
11. Self-grade always A+/A/B/C: yes / no, name others.
12. Daily-note 3-line stub: keep (A under Notes / B end) / drop.
Not blocking:
13. Reconcile ask surface: A note checkboxes / B + Mattermost / C + panel.
14. Excitement audit: A reversion-only / B every trade / C drop.
15. SMB PDF builder in S3: yes / no.
Sitting: ~30 min (15 one-word answers, template + one recent DRC + SMB sheet + card mock open).
Desk only: ESCALATE 1 (miss line 21:10 vs 15:41 acceptance).

DRC SITTING PACKET READY · decisions: 15 · blocking S3-P3: 12 · ladder items with no home yet: 4 · NOT ESTABLISHED: 1 · sitting length: 30 min · ESCALATE: 2
