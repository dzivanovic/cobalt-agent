# DRC tribunal — derive report (v2 from round 1) — 2026-09-22

Seat: `drc-tribunal-derive-0922` · model `claude-fable-5-1` (R73: `derive seat: claude-fable-5-1`) · the same SEAT that ruled round 1 blind (`41`), fresh session (round-1 context not carried; the round-1 reports read from disk) · started 17:07 ET, v2 written 17:2x ET, this report 17:24 ET · HOLDS A SIDE: recommends nothing to him (L37); its own round-1 wordings passed the same filter as every house's.

## §0 Headline
- WROTE `docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md` (81,677 B): the proposal whole, 35 fold rows (25 verbatim seat wordings, 24 of them grok's or gemini's), §13 carried AS RULED (R69–R72; no ACTION/WRITER cell changed), header `ASTRA PENDING (R13)`.
- Round 2 is owed for ONE item: R2-1 — a C2 refusal at the reconcile (a CLOSED card the export shows still open): grok = build FAILS naming the card (the proposal), Fable seat = build with an unresolved-mismatch row, gemini = correction written and the position carries (refused under v3+R67's N unless O20). Every other item closes.
- Owner items 21 live (O1–O18, O20, O21, O22 new from grok; O19 spent); none a precondition to build; O15 is a precondition to PRODUCTION (the fixture's git commit), not to E1/D1.
- The hub's `## Wording offered, verbatim` attributed Fable-seat text to gemini on 9 items; v2 derives from the raw `gemini-ruling.md` (ESCALATE 1). Its two "splits" (e), (f) re-read from the raw files: (f) stands as round 2; (e) dissolves (gemini's own sentence is consistent with grok's).
- Astra `METER — proceed on three` (R13): recorded, not a refusal; Astra reads this v2 on Sat 2026-09-26. ESCALATE: 10 · redactions: 0.

## Authorization (verified 17:07 ET)

| gate | result |
|---|---|
| `DERIVE ROW: R__` unfilled | 0 (filled: R73) |
| `| R73 ` row in cto-2026-09-22.md | 1 row (line 45) carrying `DRC-AUTOMATION-PROPOSAL-2026-09-22.md` · `Fable seat: yes` · `derive seat: claude-fable-5-1` |
| R73 committed | 938f1f5ecbafaac8220564189435d4a47fa6cd78 |
| seat match | row names `claude-fable-5-1`; this session runs `claude-fable-5-1` |
| hub stop line | `DRC TRIBUNAL R1 DONE · grok: TRIBUNAL R1: BUILD AFTER folds on writers, seams, and E1 · gemini: TRIBUNAL R1: BUILD AFTER HIS REAL-SHAPE EXPORT (E1) IS SECURED · astra: METER — proceed on three · houses that ruled: 2 of 3 · claims that HOLD: 21 · blockers to build: 0 · owner items: 20 · ESCALATE: 8` |
| hub stop line committed | c08719aaf3061d45e736066589d108cf96483f4a |
| Fable r1 stop line | `DRC TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER E1's real export is in hand and vendor names leave every identifier · adopt: 2 · adopt with wording: 19 · reject: 0 · experiments named: 12 · ESCALATE: 4` |
| Fable r1 committed | f3084c02bfcc52b9e53ca980b1296f3b05b0bec7 |
| a house ruled | grok and gemini both carry `TRIBUNAL R1:` lines; houses that ruled 2 of 3 |
| launch line adds no rule | all 7 allow + 3 deny strings count ≥1 in `2026-09-21/22-draft-setups-tribunal.md` |
| Astra | `METER — proceed on three` (R13) — recorded; v2 header `ASTRA PENDING (R13)` |
| recovery (L60) | both output paths absent at 17:07 → fresh derive |

## DIGEST FOR THE DESK
What v2 changed from the proposal, one line each (tag = fold row):
- F-01/F-26 citations corrected (R67 by row; §8's placement range split into the four real definitions) · F-02/F-03 F23's `public.trades` collision and F25's "R2-2 OPEN" struck (grok WRONG FACTS, hub HOLDS) · F-04 four callers added as F35–F38 (gemini) · F-05 F39–F41 the `prefill drc` console script, README rows and the `rules.yaml` reader row (Fable, read by the derive).
- T1 F-06: `_imports/` bytes written only by a NEW `VaultWriter` method, gated by `_session_gate` (grok) — the writer's existing commit path is text-only (FC5), so D2 adds a bytes path inside it; Fable's import-store alternative not taken.
- T2 F-08: in-request build; event row = state; `done` only after the note write returns; E11 kill test (grok).
- T3 F-24: the 21:10 run stores `render_line`'s exact arguments; the build re-renders from that blob only; E6 = that proof (grok). Gemini's re-run-by-run-id names no stored inputs; Fable's stored-body not taken.
- T4 F-35: `drc_imports` + `drc_fills` + declared `drc_rows`; never `fills`/`order_fills` (grok; gemini raw = `drc_fills` too); event state stays with `drc_imports`.
- T5 F-15 + F-16: engine writes only `drc-rules/rule_engine` (grok); DRC keys in `OPTIONAL_SETTING_KEYS` + a text hash on each rule binding (Fable, single-seat, FC7/FC8 HOLD, X12 gates).
- T6 F-21: voice units `drc-trades/voice-<trade_id>` created once via `upsert_unit(skip_if=…)`, never re-upserted; a vanished trade leaves its unit with `orphaned` (grok); gemini's "the merge appends orphaned text" has no code (grep 0); E8 proves.
- T7 F-11: S-C1 in C1's set (`das` value + nullable `source_id`), S-C2/S-C2b on C2's one writer, `adjustment pending (legs writer not built)` before C2 (grok); gemini's `0014_legs.sql` not carried.
- (f) F-12: NEEDS ROUND 2 (R2-1) — the proposal's FAIL sentence kept, tagged, three positions verbatim in v2's OPEN block; X11 runs under the adopted one.
- T11 F-10: seed from the prior `drc_rows`; a contradicting file FAILs (grok); Fable's contiguity check → E1's result column (a flat-start export leaves the seed with no cross-check).
- T8 F-20: date token only, no early return, `drc.md.j2` deleted in D3 (grok). T10 F-25: `s2.yaml:436-438` removed in the same deploy; K10 keyed on the event (grok); the "three smoke kinds" claim does not hold as exhaustive (eight kinds).
- T9 F-18: gemini's one-source wording; grade dollars already live in `aset.sheet_modes` (read by the derive) so grok's `grades.*` family not taken (L3); `daily.md.j2:18` leaves git by reading the key — INSIDE the design (gemini) vs OUTSIDE D1–D5 (grok) is a scope split for the desk (ESCALATE 6).
- (b) F-22 + F-23: plist, `jobs.yaml` rows and the CLI entry killed in the same deploy (grok); a PRE draft never writes a `Grade:`/`Goal:` line (Fable, single-seat, hub HOLDS). (c) F-07, (d) F-09, (e) F-13, (g) F-14, (h) F-17, (i) F-19, (j) F-27 grok verbatim; F-28 the `rules.yaml` `no_resident_reads` row moves to `com.cobalt.aset`'s `reads:` (Fable, read by the derive; L42).
- F-29 L31 names: `das.py` / `das_import_id` / `das` / `das_export_shape` carried as written with `[L31 — NAME PENDING]` — the desk's call (ESCALATE 2). F-30 experiments: E6/E8 changed, E9–E11 added (grok), X10–X13 (Fable), E1's result widened. F-31 O20–O22. F-32 L52 re-answered. F-33/F-34 gemini claims not taken.
Seats that ruled round 1: grok IN FULL (21 items, tagged) · gemini IN FULL (T1–T10 tagged; (a)–(j) untagged prose read as adopt-with) · Fable seat IN FULL (blind) · Astra METER (R13).
Fable claims: 14 hub-checked (FC1–FC14: 12 HOLD, 2 UNVERIFIABLE); 6 more read by the derive (FC10 borne out at `prefill/drc.py:190-217`; FC12: both config paths at `aset/config.py:41-42`, which loads is E7; `jobs.yaml:309-316`, `prefill/cli.py`, `pyproject.toml:64`, `ops/README.md` borne out; the `s2.yaml` kinds list NOT borne out as exhaustive); every other Fable claim UNCHECKED and not folded.
Round 2: ONE item (R2-1, above) — because two seats disagree on whether the proposal's FAIL-the-build mechanism is correct; a run after 2026-09-23 23:59 ET needs his word for `grok`/`agy` (R30).
Owner items, one line each: O1 typed vs OCR · O2 file home · O3 no-trade day (default no DRC) · O4 accounts · O5 dollar VALUES · O6 config home · O7 rule→checker map (+hash) · O8 example blocks · O9 voice unit inside/beside · O10 voice · O11 premarket keys · O12 packet Qs · O13 N + agreement · O14 market_reset drops (default refuse) · O15 fixture commit consent (production precondition) · O16 PnL placeholder · O17 jsonl · O18 "15:41" wording · O20 CLOSED→open edge (new, R2-1's root) · O21 gross vs net (new) · O22 import-size key (new, grok).
Chunks/seats/RESTARTS under v2: D1 (Opus 5, no restart) → D4 ∥ D2 (`com.cobalt.aset`) → D3 (`prefill-drc` retired, `replay`, `aset`; per `cobalt jobs restarts`) → D5 after S3 C2 (`aset`); D4's restarts per L42 — if radar is among them, inside the pause; D2+D3 one deploy; one migration in D1, number the desk's (L68); D4 migration-free unless E10 fails.
Waits: D1 on E1 (his real export — an INPUT, L45); D2 on E2/E5; D5 on S3 C2 merged + R2-1 + X11; nothing on an owner value (L69).
Hours (GUESS): DRC 32 h seats (≈45 with fix rounds, factor UNVERIFIED) + S3 C1–C4 30–42 h = 62–87 h inside 09-24 → 10-07 (10 trading days) — sequencing is the desk's (L68, L72).

## Fold table
`F-nn · item · seats that ruled it · whose wording · adopted verbatim? · why`. All 21 items were ruled by 3 of 4 seats (grok, gemini, Fable; Astra METER) unless stated.

| F | item | seats (of 4) | whose wording | verbatim? | why (≤25 words) |
|---|---|---|---|---|---|
| F-01 | WRONG FACTS (R67 line drift) | 1 (Fable) | proposal kept, cited by row | n/a (citation) | FC3 HOLDS: rows inserted above R67; v2 cites the row, never a line |
| F-02 | (a)/WRONG FACTS F23, F14 | 3 | grok | yes | hub Checked: no `public.trades` in `placement.py`; six `request.form()` sites HOLD |
| F-03 | (a)/WRONG FACTS F25 | 3 | grok | yes | hub Checked HOLDS: R67 ruled R2-2; v3+R67 = FINAL |
| F-04 | (a) callers F35–F38 | 3 | gemini | yes | hub Checked: `daymode/cli.py:151`, `prefill/cli.py:49`, `replay/cli.py:98`, `smoke/checks.py:151,566` all HOLD |
| F-05 | (a) F39–F41 | 1 (Fable) | Fable (facts restated, not its sentence) | no | UNCHECKED by a hub — read by the derive at `pyproject.toml:64`, `prefill/cli.py:1-79`, `ops/README.md:30,145,157`, `jobs.yaml:309-316` |
| F-06 | T1 | 3 | grok | yes | packet excerpt HOLDS; `_session_gate` at `writer.py:387` read by derive; Fable's import-store alternative not taken (own seat; house's equally correct, L40) |
| F-07 | (c) | 3 | grok | yes | hub Checked: six form sites; `uv.lock` pins from packet; E7 not a precondition (3 of 3); Fable's binding sentence → X13 |
| F-08 | T2 | 3 | grok | yes | proposal's own mechanism + L18 state; gemini/Fable ADOPT; E11 (grok) is the proof |
| F-09 | (d) | 3 | grok | yes | F8 PROVEN; refuse-not-queue 3 of 3; Fable's CLI refusal covered by grok's "a CLI run otherwise exits failed" |
| F-10 | T11 | 3 | grok | yes | grok ADOPT + contradiction rule; gemini ADOPT; Fable's contiguity check not taken (own seat) → E1's result column |
| F-11 | T7 | 3 | grok | yes | v3 :125/:132 CHECK sets have no source slot (read by derive); gemini `0014_legs.sql` DOES NOT HOLD (hub); `das` value → F-29 |
| F-12 | (f) | 3 | proposal kept, tagged | not taken | NEEDS ROUND 2: grok (FAIL) vs Fable (unresolved row) disagree on correctness; gemini's walk needs O20 (v3 :149 N refuses) |
| F-13 | (e) | 3 | grok | yes | hub HOLDS the proposal quote; gemini's raw sentence consistent (missing/renamed FAIL), silent on added; hub ESCALATE 3 rested on Fable text mis-attributed to gemini |
| F-14 | (g) | 3 | grok | yes | F15 PROVEN; grok's header check covers Fable's magic-bytes; E9 named by grok and Fable |
| F-15 | T5 | 3 | grok | yes | R69 A21; `replay/line.py:59` MIN_N from packet; gemini ADOPT |
| F-16 | T5 addendum | 1 (Fable) | Fable | yes | single-seat: FC7 HOLDS (order numbering), FC8 HOLDS (tuple split); X12 gates D4; desk may strip (ESCALATE 5) |
| F-17 | (h) | 3 | grok | yes | F20 PROVEN; O7 map his; gemini prose agrees; Fable's boundary list = proposal §12 already |
| F-18 | T9 | 3 | gemini | yes | grok's `grades.*` keys would copy `aset.sheet_modes` — read by derive at `aset/config.py:222-237,:267`, `settings/models.py:30` (L3); Fable's not taken (own seat) |
| F-19 | (i) | 3 | grok | yes | FC13 HOLDS (`mark_filled` UPDATEs); columns = F18; C-row timing flagged (ESCALATE 3) |
| F-20 | T8 | 3 | grok | yes | F2 PROVEN (early return); `:272` sole caller per packet grep + Fable self-attack; gemini/Fable ADOPT |
| F-21 | T6 | 3 | grok | yes | API is `upsert_unit(skip_if=…)` `writer.py:652,:680-682` (read by derive); gemini's orphan claim: `grep -ri orphan vaultwrite/` = 0; Fable's per-trade units not taken |
| F-22 | (b) | 3 | grok | yes | `prefill/cli.py:46-49,:67-69` read by derive; gemini prose same conclusion |
| F-23 | (b) addendum | 1 (Fable) | Fable | yes | single-seat: hub Checked `daymode/drc.py:116-132` HOLDS; constrains HOW PRE rows write, no ACTION/WRITER change (ESCALATE 5) |
| F-24 | T3 | 3 | grok | yes | 8-arg list from the packet's runner excerpt; gemini's re-run names no stored inputs (L57); Fable's stored body not taken (own seat) |
| F-25 | T10 | 3 | grok | yes | F27/F28 PROVEN; gemini ADOPT; Fable's precondition design not taken; FC14 "three kinds" DOES NOT HOLD as exhaustive (8 kinds read by derive) |
| F-26 | WRONG FACTS §8 range | 1 (Fable) | proposal corrected | n/a (citation) | FC2 HOLDS: `:230`, `:248`, `:285`, `daily.py:165` |
| F-27 | (j) | 3 | grok | yes | F24 PROVEN; arithmetic HOLDS (hub); 0.4× UNVERIFIED; RESTARTS by `cobalt jobs restarts` (L42) |
| F-28 | (j) addendum | 1 (Fable) | Fable (fact restated) | no | UNCHECKED by a hub — read by derive at `jobs.yaml:309-316`: "no resident imports either path" false at T2; L42 (ESCALATE 5, 8) |
| F-29 | L31 identifiers | 1 (Fable) | none — tag `[L31 — NAME PENDING]` | not taken | FC1 HOLDS but neither house saw L31 (hub ESCALATE 1); a single-seat rename of house verbatim text is the desk's call (ESCALATE 2) |
| F-30 | experiments | 3 | grok (E6, E8, E9–E11), Fable (X10–X12), derive (X13 from Fable (c)) | yes (E/X texts) | L70: every "not checkable from reads" pushed to a gate; E1 result column widened from grok + Fable |
| F-31 | owner items O20–O22 | 3 | grok (O22 verbatim), Fable (O20, O21) | O22 yes; O20/O21 n/a | none a precondition to build; O15 sharpened (grok) = production precondition |
| F-32 | §12 L52 + bar | — | derive (required by the prompt) | no | L1, L2, L3, L7, L8, L9, L28, L32, L40, L45, L53, L57 each stated for v2 with its fold rows |
| F-33 | T6 gemini claim | 3 | gemini | not taken | "orphaned text … appended at the bottom of the unit" — no code (`grep orphan` 0; `writer.py:684-806`); E8 is the proof either way |
| F-34 | (f) gemini migration file | 3 | gemini | not taken | hub DOES NOT HOLD: `0014_legs.sql` contradicts gemini's own (j); number is the desk's |
| F-35 | T4 | 3 | grok | yes | hub Checked `placement.py` HOLDS; gemini raw = `drc_fills` (2 houses); Fable's `drc_executions` + day-row event not taken (own seat) |

Totals: folds 35 · verbatim yes 25 · not taken 4 (F-12, F-29, F-33, F-34) · citation/derive rows 6.

## NEEDS ROUND 2
**R2-1 — a C2 refusal at the reconcile (proposal §3 step 4; T7/(f)).** Two seats disagree on whether the proposal's mechanism is CORRECT:
- grok (f), verbatim: "A CLOSED card whose DAS position is still open: the build FAILs naming the card. This writer does not reopen the card." (= the proposal's "A refusal from C2's writer (e.g. a CLOSED card moved off 0) = build FAILED naming the card — never forced.")
- Fable seat T7 (i), verbatim: "A refusal from C2's writer is never forced and never fails the build: it is recorded as an UNRESOLVED LEG MISMATCH (a `drc_rows` row: card id, leg ids, the export rows, the refusal text), rendered in the reconcile unit as `unresolved: card <id> — <refusal>`, and carried forward on every later DRC (A31) until resolved; how a CLOSED card the export shows still open is reopened is his (O20)."
- gemini (f), verbatim: "CLOSED card DAS says open: Reconcile writes the correction, and the trade carries to the next day as OPEN (R67)." — a third path; under v3 + R67 (N, v3 :149) that shares correction is REFUSED, so it needs O20 first.
Question round 2 must answer: under the S3 exits FINAL (v3 + R67), when C2's writer refuses the reconcile's correction, is the correct behaviour A (the build FAILS naming the card — that day has no DRC until O20), B (the DRC builds with an unresolved-mismatch row carried on A31), or C (the correction is written and the position carries — only with a CLOSED→open edge, O20)? Evidence to run first: X11 on `cobalt_dev` after S3 C2. Round-2 packet: the raw round-1 files (the hub's attribution error must not be re-staged), L31 uncut (hub ESCALATE 1), v2's OPEN block. NEEDS ROUND 2 count: 1.

## OWNER ITEMS (after the tribunal)
Deduplicated; who raised it; none a precondition to build.
- O1 typed cells vs OCR — proposal; all seats.
- O2 file home `_imports/` vs non-synced dir — proposal; Fable sharpened (every screenshot then syncs to every device).
- O3 no-trade day vs R66 — proposal (author's ESCALATE 2); all seats: default no DRC.
- O4 which accounts count — proposal; grok: a multi-account file FAILs until loaded.
- O5 the daily-stop / grade dollar VALUES — proposal (author's ESCALATE 1); mechanism = F-18.
- O6 config home — proposal; grok: default `trader_settings` until he rules.
- O7 rule→checker map — proposal; grok: the map is the copy he edits; Fable: + text hash (F-16).
- O8 template example blocks — proposal; grok: they copy until he tells the desk (L65).
- O9 voice inside/beside the trade section — proposal; grok: id `drc-trades/voice-<trade_id>` either way.
- O10 voice channel/timing — proposal. O11 premarket keys — proposal. O12 packet Q2, Q4–Q8, Q10–Q14 — proposal. O13 N + agreement — proposal. O14 `market_reset` drops — proposal; all seats: default refuse.
- O15 consent to commit the redacted fixture — proposal; grok: L45 makes the commit a PRODUCTION precondition; E1/D1 on `cobalt_dev` do not wait.
- O16 PnL placeholder — proposal. O17 jsonl files — proposal. O18 "15:41" wording — proposal (author's ESCALATE 3); grok: D3's smoke rows do not wait.
- O19 SPENT (R69–R72) — all seats.
- O20 CLOSED→open edge — Fable (new); the root of R2-1; a trading-logic change (L7 + HITL).
- O21 gross vs net on the summary line — Fable (new).
- O22 import-size limit key (SPEC §7 `limits` has none) — grok (new, MISSING).
Values proposed by a seat for one of his keys: none (grok's `account.daily_stop_full` / `account.daily_stop_half` are SPEC §7 KEY NAMES, no value).

## FOR DEJAN
One A/B per item, in his terms; A = what v2 builds by default, B = the alternative a seat named; seats holding each in brackets; no recommendation (this seat ruled round 1).
- **O1** — On the `/drc` page, A: you type MAE/MFE/target/best exit into four small cells per trade, or leave them blank [proposal, grok, gemini, Fable]. B: Cobalt reads them off the screenshot (a new OCR dependency, shown beside your typed cells first) [named by the proposal as a later slice].
- **O2** — A: the CSV and screenshots are saved inside your vault under `_imports/drc/<date>/` and sync to every device [proposal, grok, gemini]. B: they live in a folder outside the vault that does not sync [Fable named the sync cost].
- **O3** — On a day with no trades, A: you drop nothing and no DRC exists (the page says what is missing) [all seats, R66]. B: a no-trade form on the page counts as "both placed" and a DRC is created for the streak [the coach spec §9].
- **O4** — If the export carries two accounts, A: the import FAILS naming them until you say which count [grok]. B: you name the accounts now and the parser keeps only those [proposal].
- **O5** — Your daily stop and the dollars per grade: A: read from ONE place, your settings rows, loaded by your own `cobalt settings load`; the committed daily template stops carrying the number [gemini, Fable]. B: same one place, but the daily template line is removed by hand later, outside this build [grok].
- **O6** — A: that one place is the settings table [grok default, gemini, Fable]. B: a keyed unit in your note [proposal alternative].
- **O7** — A: you keep a small map "rule number → checker" in settings; a rule with no entry shows `untested`; if you re-word a bound rule the engine shows `untested: text changed` instead of judging the new text [grok + Fable]. B: the same map without the text check — re-wording a rule keeps the old checker on it until you edit the map [grok alone].
- **O8** — A: the two example trade blocks and the example If/Then in your template copy into every DRC until you tell the desk to strip them [grok]. B: the desk removes them from your template on your word now (L65) [proposal].
- **O9** — A: your answer lines for each trade sit in their own small unit next to that trade's Cobalt block; a re-drop never rewrites them [grok]. B: the same unit inside the trade's section [grok's other placement].
- **O10** — A: no voice this slice; you type or dictate in the DRC chat as today [proposal, all]. B: a voice capture per trade later [later slice].
- **O11** — A: only `Sleep:`, `Readiness:`, `RHR:`, `1% goal:` are read from the daily note; meditated / tone / hotkey show `not given` [proposal]. B: you add keyed lines for those to the daily template [his edit].
- **O12** — the packet questions Q2, Q4–Q8, Q10–Q14 stay yours; nothing in v2 waits on them.
- **O13** — A: the engine's pass/fail shows beside your checkboxes as "shadow" with its n until you say N and what "agreement" means [all]. B: none named.
- **O14** — Dropping files between 20:00 and 21:00, A: the page refuses with the reason and you drop again after 21:00 [grok, gemini, Fable]. B: the page accepts and builds after 21:00 (needs something to wake at 21:00 — no seat built it) [proposal's O14 question].
- **O15** — A: you hand over one real export for E1 now; the stripped copy goes into git only when you say so; production waits on that commit, D1 on `cobalt_dev` does not [grok]. B: the commit consent given with the export [proposal's framing].
- **O16** — A: the `### PnL on the day:` placeholder is yours; DAS net P&L sits in its own line [grok]. B: Cobalt fills the placeholder [proposal alternative].
- **O17** — A: no `trades.jsonl` / `days.jsonl`; Postgres only [proposal]. B: a file export beside it [coach spec §5.2].
- **O18** — A: the Charter/S3 line "DRC exists at 15:41" is re-worded by you to "within the build timeout of the second input" [proposal]; the smoke rows change with D3 either way [grok].
- **O20** — When you flattened a card by hand and the export shows shares still open — this is round 2's question (R2-1), brought to you only if round 2 does not settle it: A: no DRC that day until the card can be reopened [grok]; B: the DRC is built with one `unresolved: card <id>` line carried until settled [Fable]; C: the card reopens (a state-machine change with HITL) [gemini].
- **O21** — The summary line's P&L: A: net [proposal]. B: gross, or both [coach spec §2 carries both; Fable].
- **O22** — Upload size: A: no ceiling this slice (E5 does not test size) [grok]. B: you name a `limits.import_max_mb`-style key [grok named the gap; the key name is yours].

## Redactions
0. Every seat text copied into v2 was scanned as copied: no value, rule sentence, ticker, price or P&L of his; the hub's three-literal scan (the same `grep -c -E` the hub ran on every staged file) on v2 = 0 and on this report = 0. Key NAMES (`account.daily_stop_full`, `account.daily_stop_half`, SPEC §7 families) appear as names only, per the hub's shape-only rule. `daily.md.j2:18` is cited by line; its value is not recorded anywhere in either file.

## READING
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` full (:1-407).
- Hub `reports/drc-tribunal-2026-09-22.md` full · `scratch/tribunal-bars-0920/drc-tribunal/r1/grok-ruling.md` full · `…/r1/gemini-ruling.md` full · `reports/drc-tribunal-fable-r1-2026-09-22.md` full (incl. `## Self-attack` WITHDRAWN lines — none folded) · proposal `30 - Design/DRC-AUTOMATION-PROPOSAL-2026-09-22.md` full · `reports/drc-design-2026-09-22.md` full · `reports/cto-2026-09-22.md` rows R60, R65–R73 (grep) · `30 - Design/S3-EXITS-v3-2026-09-22.md` :17-34, :110-170.
- Code, where a fold turned on it (read to check, never to copy): `vaultwrite/writer.py` def list, :640-895 (`upsert_unit`, `skip_if`, `_merge_base`); `vaultwrite/merge.py` def list; `grep -ri orphan src/cobalt/vaultwrite/` (0); `prefill/drc.py:190-221`; `aset/config.py:36-49`, :212-270; `settings/models.py` (grep grades/sheet_modes); `prefill/daily.py` (grep); `configs/cobalt/jobs.yaml:298-316`; `prefill/cli.py` (grep drc); `pyproject.toml:64`; `ops/README.md` (grep); `smoke/checks.py` (grep drc); `configs/cobalt/smoke/s2.yaml` (grep kind:). Prompts: `2026-09-22/42-drc-tribunal-derive.md` (this seat's); `2026-09-21/22-draft-setups-tribunal.md` (string counts only).
- Not read: the coach spec's body, his DRC note or template body, any daily note, `Rules.md`, any production row; no DB, docker, pytest, git write, agent launch, vault write or memory-folder write.

## ESCALATE
1. **The hub's `## Wording offered, verbatim` mis-attributes Fable-seat text to gemini** on T3, T4, T6, T7, T9, T10, (e), (g), (h) (compare hub :114-134 with `gemini-ruling.md` :9-43, :75-99 and the Fable report :54, :61, :77, :84, :107, :114, :150, :163, :169). Its Rulings-table "gemini/Fable-aligned" rows, its ESCALATE 2–3 framing and part of "claims that HOLD: 21" rest on that. v2 uses the raw file only. The desk should not re-stage the hub's tables in a round-2 packet.
2. **L31 names — single-seat law item, tagged not folded.** `das.py`, `das_import_id`, source value `das`, flag `das_export_shape` carry `[L31 — NAME PENDING]` in v2 (F-29). FC1 HOLDS; neither house saw L31 (packet cut). The rename (`trading_log.py` / `import_id` / `trading_log` / `trading_log_shape`) changes no mechanism. `ASK DESK: settle the names on the Fable seat's ruling, or add L31 to the round-2 packet for R2-1 and let the houses rule the names there? [17:24 ET]` — safe default taken: names as written, tagged.
3. **Touches R72 (not a re-open):** grok's (i) (F-19) times C1, C3, C6, C11 as `not given` until their inputs are stored and C13 outside D3. C1–C13 stay ACCEPTED; only WHEN each renders changes. The desk confirms this reads as HOW/WHEN, or brings it to him. No wording re-opens R65–R73's ACTION/WRITER cells, creates a DRC from one input, adds a PDF, reaches his platform, or sets aside R67.
4. **S3 FINAL changes asked for (desk's S3 build prompts):** grok (f) and gemini (f) both say S-C1 / S-C2 CHANGE the S3 FINAL's C1 DDL (a new CHECK value on `source` and `price_source`, a nullable source-id column) and C2's writer semantics (DAS-sourced correction + new exit leg under the same lock and refusals; held-count statement superseded never deleted; running > 0 across days; CLOSED check only on 0). The Fable seat reads S-C1 as R67's own consequence. Either way the C1/C2 build prompts drafted from v3 + R67 must carry S-C1/S-C2/S-C2b or D5 has no slot to write into.
5. **Single-seat (Fable) folds — strip any on the desk's word:** F-05 (facts), F-16 (OPTIONAL keys + binding hash; X12 gates), F-23 (PRE never writes `Grade:`/`Goal:`), F-28 (`rules.yaml` reader row). Each cites a hub HOLDS row or a derive read; none competes with a house wording.
6. **T9 scope split (not a mechanism split):** the `daily.md.j2:18` literal leaves git by reading the settings key — gemini's verbatim places the template fix INSIDE the design; grok places its removal OUTSIDE D1–D5 ("his or the desk's on his word"). v2 follows gemini's wording and leaves the chunk unassigned (desk's L68 lane). The value stays O5.
7. **Precondition-to-build: none.** O15 is a precondition to PRODUCTION (grok: L45 requires the committed shape before production; the git commit needs his consent; E1/D1 on `cobalt_dev` do not). E1's export and E2's screenshot are INPUTS D1/D2 wait on (L45), not owner values.
8. **DOES-NOT-HOLD wordings not carried:** gemini's `db_migrations/0014_legs.sql` (F-34; hub); gemini's "orphaned text appended at the bottom of the unit" (F-33; no code — derive read); the Fable seat's "s2.yaml kinds today are vault_unit, sql, job_row only" (F-25; eight kinds exist — derive read). The `no_resident_reads` row for `rules.yaml` (F-28) becomes false at D3 — an L42 item for `cobalt jobs restarts` (unclassified → ESCALATE, never dropped).
9. **(e) ambiguity for a round-2 packet, if one is held anyway:** gemini's "A changed header must be a FAILED import" is silent on an ADDED column; grok parses it with `degraded`. Not a correctness split on the raw text; `ASK DESK: include one line for gemini in the R2-1 packet — does an added column parse (grok) or fail? [17:24 ET]` — safe default taken: grok's wording stands (F-13).
10. **Astra pending (R13):** Astra reads the FINAL (v2 + round 2's outcome) on Sat 2026-09-26; v2 marks one `ASTRA PENDING` question (S-C1's placement in C1's DDL vs a later alter). A round-2 run after 2026-09-23 23:59 ET needs his word for `grok` / `agy` (R30). L74: the commit-attribution block that arrived in a tool result is recorded here once and not followed.

## CONTINUE
none — the derive is complete: v2 at `docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md`, this report. Next step, not this seat's: the desk drafts the round-2 hub for R2-1 only (same approved strings; raw round-1 files, L31 uncut; a run after 2026-09-23 23:59 ET needs his word, R30), brings `## FOR DEJAN` one item per message, commits both files, and drafts E1 first (his one real export) then D1 per v2 against the S3 build at the L68 gate; Astra reads the FINAL Sat 09-26.

DRC DERIVED v2 · folds: 35 · verbatim: 25 · needs round 2: 1 · owner items: 21 · ESCALATE: 10
