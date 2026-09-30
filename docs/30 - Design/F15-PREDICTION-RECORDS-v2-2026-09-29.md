# F15 PREDICTION RECORDS + `replay(card_id)` — v2 (2026-09-29)

**Status: DRAFT FINAL — ASTRA PENDING (round 2 not before: no return time recorded. Astra's round-1 stop was a TIMEOUT, not METER: the probe answered `OK` at 12:06 ET, then no item was printed in 59 min and the run was stopped at 13:19 ET. See `reports/f15-tribunal-2026-09-29.md` ESCALATE 4.)** Astra rules round 2 on this DRAFT FINAL (`prompts/2026-09-29/12-f15-tribunal.md` §5). Nothing is built from this file until a FINAL is derived.

- Derived by seat `f15-derive-0929` (Opus 5.5, `claude-opus-5-5`), 2026-09-29 13:28 ET. This seat is the same seat that ruled round 1 blind, so it holds a side (L37). No wording of its own is preferred over a house's.
- Input: the proposal `docs/30 - Design/F15-PREDICTION-RECORDS-PROPOSAL-2026-09-29.md` (commit `42eb7fbb`) and its author's report `reports/f15-design-2026-09-29.md`.
- Rulings binding and not re-opened:
  - `cto-2026-09-29.md` R57 ("proceed with whatever builds are necessary"), R58, R59 (the desk's readings: G5 → ruled as Open 3, OWED as a lane; `shadow_report.py:13-15` → OWED L32 fix lane);
  - `cto-2026-09-23.md` R95, R96, R97;
  - `cto-2026-09-22.md` R109.
  - Launch rows: R64 (round 1), R74 (this derive).
- Round-1 rulings (3 of 4 houses ruled):
  - Grok: `scratch/tribunal-bars-0920/f15/r1/grok-ruling.md` (agy-trial worktree), `TRIBUNAL R1: BUILD AFTER taps-moved output, at-order, and seq lock are specified`.
  - Gemini (optional fourth, R97): `…/f15/r1/gemini-ruling.md`, `TRIBUNAL R1: BUILD`.
  - The Anthropic seat (R109, launch row R64: `derive seat: claude-opus-5-5`): `reports/f15-tribunal-anthropic-r1-2026-09-29.md`, `TRIBUNAL R1: BUILD AFTER records are written inside the card-row transaction, and §8 names the shared files it missed`.
  - Astra: TIMEOUT, no ruling, no round spent (L67).
  - Hub collate and file-check: `reports/f15-tribunal-2026-09-29.md`.
- Fold table: `docs/40 - DevDocs/reports/f15-derive-2026-09-29.md` `## Fold table`. Every amended paragraph below carries its `[F-nn]` tag. A paragraph with no tag is the proposal's text, unchanged.
- **Tags that read `NEEDS ROUND 2 (R2-n)`** mark text this draft carries from one seat while another seat disputes whether the mechanism is correct. The disputing seat's wording is printed beside it, verbatim. Round 2 picks one; the derive does not.
- Committable: his thresholds and settings appear as KEYS only (L32). Redactions: 0.

LADDER `S3-P3 · F15` (`docs/00 - Project/SPRINT-LADDER-v0_1.md:648`; charter `docs/00 - Project/MVP-CHARTER-v0_2.md:173`).

Acceptance, verbatim (ladder `:648`): "Any card's grade replays from stored inputs." — "Every score + WHY stored with its inputs and joined to the card outcome (legs, realized R, MISSED counterfactual); a `replay(card_id)` command recomputes the grade from stored inputs and diffs." S3 smoke clause: "replay of the card's grade matches." (`:653`).

**The design in one paragraph.** Most of F15 already exists. Every radar scan writes an immutable receipt holding the values it scored from, and `replay_receipt` already recomputes every card number in that receipt, refusing a receipt from another evaluator version. Three things are missing. (1) A tap re-grades the card and stores neither its result nor the settings it used. (2) The card row is overwritten, so nothing names which inputs produced the grade a card showed at a given moment. (3) No command replays one card or joins its grade to its outcome. F15 adds one append-only table, `"user".prediction_records`, which ADR-0008 already declares. It holds one row per grade write on a radar card. A scan row references the scan's receipt and stores only the card's slice. A tap row stores its own inputs whole. F15 also adds `cobalt cards replay <card_id>` and one read that joins records to legs, realized R and `missed`. That is one migration and two chunks.

---

## 1. Fact base

### 1a. Every scored object today

| # | Object | Where computed | What it decides | Reaches the card |
|---|---|---|---|---|
| S1 | Dot engine grade (per computed factor, SHADOW) | `cards/scoring.py:165-219` (`compute_dots`), curve `:139-156` | the hollow dot shown; never in conviction (`scoring.py:12-19`) | yes (hollow) |
| S2 | Conviction | `scoring.py:259-265` (mean of TAPPED grades ÷ 10) | the card grade's human half | yes |
| S3 | Proximity | `scoring.py:277-284`; `last` rule `score_last` `:354-364` (STALE-SCORE v2 §2 C) | the card grade's price half; NULL while bars stale | yes |
| S4 | `card_score` + suppression | `scoring.py:287-290`, `:268-274`; `score_card` `:367-393` | WATCH order — "the ONE ranking authority that reaches a radar card" (`scoring.py:1-2`; ladder `cards/radar.py:179-183`) | yes |
| S5 | Proposed key | `scoring.py:296-309` (bands `card.proposed_key` → `snap_down`) | the highlighted key | yes |
| S6 | Radar evaluation label (`formed` … `input_stale`) | `radar/evaluate.py:966` (`evaluate_member`); stored `system.radar_score` (`0006_radar_score.sql:92-109`) | whether a card is created (`evaluate.py:1939-1993`) | yes (creates it) |
| S7 | Health pills (FILLED) | `evaluate.py:1347-1365`, `cards/health.py` | in-trade pills; stored `aset_sizings.health` (overwritten, `cards/store.py:1042-1044`) | yes |
| S8 | Pool rank (`rank_value`, `last_rank`) | `radar/pool.py`; written `radar/store.py:99-105` (overwritten per scan) | admission; ladder tiebreak (`cards/radar.py:176-183`) | yes (tiebreak, `pool_position`) |
| S9 | Float-handicap would-be rank | `radar/handicap.py:1-6`; stored `0014_radar_handicap.sql:13-15` | nothing — shadow, "never used to sort" (`handicap.py:4-5`) | no |
| S10 | Pick-time card-score rank / focus top-N | `cards/picks.py:196-240`; stored `"user".picks` (`0009_picks_missed.sql:14-42`) | nothing live — the pick-vs-rank report | no |
| S11 | Desk grades (`catalyst`, `market_alignment`, `sector_alignment`) | tables `system.desk_*` created empty (`0006:132-184`); dots N/A (`scoring.py:20-24`, `:75-76`) | nothing yet | shown as N/A |

Not scores, named so they are not missed: the radar expiry decision (`cards/expire.py`, a state move); ASET sizing (`sized_grade` via `snap_down`, `shares`, `cards/store.py:1154-1189`, derived from HIS tapped key); the outcomes realized R (`cards/legs.py:677-705` on `s3/exits-c4`) and `missed.cf_r` (`replay/cards.py:1-57`). The stale score is not a separate object: it is S3's NULL rule (`docs/30 - Design/STALE-SCORE-v2-2026-09-22.md` §2 C).

**Scored objects: 11.**

### 1b. What is stored today

| Object | Inputs stored | Scorer version | Settings in force | WHY (writer) |
|---|---|---|---|---|
| S1–S5 at a SCAN | `"user".radar_score_receipt`, one per run, immutable (`0007_radar_cards.sql:157-202`): closed i1 rows as a per-day delta chain, daily rows, RVOL, tunables, settings (`card` rows + `enabled_grades_today`), definitions, and per card: entry, stop, taps, `assumed_keys`, `published` numbers (`evaluate.py:1416-1506`, `:2053-2058`, `:2003-2007`) | `observations.evaluator_version` (`evaluate.py:1496`); run row `evaluator_version`, `formula_sha256` (`0006:76-79`) | values in the receipt; `settings_sha256` on the run (`evaluate.py:1828`) and on the card at creation (`evaluate.py:1972`) | `engine_why` per dot (code, `scoring.py:159-162`, `:179-218`); `score_suppressed` sentence (code, `scoring.py:268-274`, `:342-351`); `proposed_key_reason` computed (`scoring.py:296-309`) but NOT stored on the row or in the receipt |
| S2/S4/S5 at a TAP | `card_dot_taps` stores `grade`, `engine_grade_at_tap`, `at`, `session` only, append-only (`0007:141-150`, `:192-200`); the card row is UPDATEd (`store.py:1242-1246`) | none | NOT stored: `bands` and `enabled` are passed in (`aset/web.py:1363-1367`) and not written (`store.py:1224-1246`) | the row's `score_suppressed` only |
| Card row (current values) | `aset_sizings.conviction/proximity/card_score/score_suppressed/proposed_key/last_price` — overwritten by refresh (`store.py:1039-1056`) and tap (`:1242-1246`); `radar_score_id` = the latest refresh's seam row only (`store.py:1042`) | `formula_sha256`, `tunables_sha256`, `settings_sha256` at creation only (`0007:52-54`) | — | `why` = the formation sentence (`evaluate.py:1194`), at creation |
| S6 | receipt (as S1–S5) + seam row `inputs_sha256` (`0006:107`) | as above | as above | `detail` JSONB (`0006:101`) |
| S7 | `health.entry_snapshot` + pills (`evaluate.py:1349-1365`), overwritten | none | thresholds not stored | pill text (code) |
| S8 | the receipt's `ordered_cohort` has per-scan `pool_position` (`evaluate.py:1801-1806`); the screener rows the rank came from: not verified by this read | none | — | — |
| S10 | `picks.score_inputs` (cohort + tie policy, `0009:9-13`, `:39`) | — | — | — |

`[F-01]` The Anthropic seat (S1 `ADOPT WITH`), verbatim: "§1b adds a row. `system.radar_score.proximity/conviction/card_score/suppressed_reason` (`0006_radar_score.sql:103-106`) is a SECOND store of S2–S4. `copy_card_values` writes it (`radar/store.py:439-441`) from the stage's pre-lock `update` (`evaluate.py:1934-1936`, `:2001-2002`, `:2009`). G3 applies to it too. It is observation only: F15 neither reads nor feeds it. §1a S2/S4/S5: a dot tap is refused only in a TERMINAL state (`store.py:1211`), so taps in ARMED / TRIGGERED / FILLED re-grade the card and rewrite `proposed_key` (`:1241-1245`) after the tapped key froze (`models.py:126`). §1e: the declaration is at `placement.py:115`. 'Immutable' receipts and taps refuse UPDATE only (`0007:188-199`); no DELETE trigger exists."

`[F-14]` Grok (WRONG FACTS 3), verbatim: "`10-PROPOSAL.md:37` calls `"user".radar_score_receipt` immutable and cites `0007:157-202`. The only triggers on that table and on `card_dot_taps` are `BEFORE UPDATE` (`0007:188-190` and `:199`; part1 `refuse_row_update` grep, those two sites only). A DELETE is not refused. F15's own DELETE trigger is a new requirement, not the current shape." (`10-PROPOSAL.md:37` is this section's first row.)

Migration directories found (`ls`): `src/cobalt/db_migrations/` (database-wide: 0001–0011, 0013–0015, 0017 on main), `src/cobalt/cards/migrations/` (0001–0002), `src/cobalt/aset/migrations/` (0001–0009).

Existing replay machinery (reused, not rebuilt):
- `evaluate.replay_receipt` recomputes every card number of a receipt from receipt values only (`evaluate.py:1611-1662`). It refuses a receipt written by another `EVALUATOR_VERSION` (`:1616-1622`).
- `cobalt radar audit-export --run` re-derives the run's hashes and replays them. It refuses when the recompute differs from what was published (`radar/audit_export.py:206-271`).
- `receipts_chain` walks the per-day delta chain (`cards/store.py:1122-1135`).
- No pruning of `radar_score_receipt` was visible to a grep of `archiver/`, `backup/` and `jobs/`. That grep is a scoped read; it does not prove the rows are kept (L35). → experiment X1.

### 1c. The L57 violations found (current code)

| # | Violation | Evidence |
|---|---|---|
| G1 | A tap's RESULT (conviction, `card_score`, `score_suppressed`, proposed key after the tap) is never stored: the row is overwritten and the tap row holds only the grade | `store.py:1224-1246`; `0007:141-150` |
| G2 | A tap's SETTINGS inputs (`card.proposed_key` bands, today's enabled keys) are not stored anywhere | `aset/web.py:1363-1367`; `store.py:1191-1246` |
| G3 | The taps-moved refresh writes a `card_score` computed from the LOCKED conviction and this scan's proximity. The receipt's `published` holds the stage's pre-lock numbers instead, so the card shows a number that no stored record carries | `store.py:1035-1046`; `evaluate.py:1934-1937`, `:2053-2058` |
| G4 | `last_price`'s bar time is not stored, and `COALESCE` keeps a price after the scan that observed it. Legs prefilled from it store `price_asof = NULL` (C3's ESCALATE 3, cited by `cto-2026-09-28.md:191` R182) | `store.py:1040`, `:1049`; `radar/evaluate.py:622` (`last_bar_ts` exists on the evaluation); `s3/exits-c4:docs/40 - DevDocs/reports/s3-exits-c3-build-2026-09-28.md:61`, `:156` |
| G5 | A scan commits each card's numbers BEFORE the run's receipt (separate transactions). A failure between them leaves published card numbers whose inputs were never stored; the run is marked `failed` | `evaluate.py:1926`, `:1984` vs `:2017`; `:1841-1849` |

**L57 gaps: 5.** Consequence for cards graded before F15 lands: their SCAN grades replay today through `audit-export --run` for as long as `EVALUATOR_VERSION` is unchanged. Their TAP grades cannot replay (G1, G2).

### 1d. The outcome side

- `"user".legs`: append-only; a correction is a new row; `legs_current_v` gives the current row per sequence. Branch `s3/exits-c4`, `src/cobalt/db_migrations/0021_legs.sql` (`git show s3/exits-c4:…`).
- Realized R: pure function `realized_r` (`realized_r.1`); `provisional` while any current leg is `estimated`; never stored (`s3/exits-c4:src/cobalt/cards/legs.py:677-705`, `:107-112`).
- CLOSED only by the zero-running leg (C2 fix r1, commit `5e77800f`).
- MISSED counterfactual: `"user".missed`, versioned and never overwritten (`is_current`, `superseded_by`); `cf_r`, `mfe_r`, `excluded_by`; kind `card` carries `card_id` (`0009_picks_missed.sql:47-121`). Written by the nightly replay (`replay/cards.py:1-57`). `[F-13]` Grok's WRONG FACT 2 against this line is NOT folded: the hub's file-check GC2 DOES NOT HOLD (`replay/cards.py:728` is the `INSERT INTO missed`, `:699` the retire). The proposal's file-level claim stands.
- "R had Cobalt's stop held" for a FILLED card: not computed in S3; it is a 21:10 replay-time figure (`docs/30 - Design/S3-EXITS-v3-2026-09-22.md:228`, seam 7).
- Seams S3 left for F15 (`S3-EXITS-v3:228`, `[F-39]`): (4) realized R + provisional + the estimated-legs list; (5) the stop path (`card_stop_edits.kind`, `stop_in_force` per leg); (6) the pick-vs-rank row; (7) the Cobalt-stop counterfactual. The DRC design's only F15 mention is the placement declaration (`docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md:40`).
- BUILT, not on main: S3 C1–C4, branch `s3/exits-c4`. `d05ae72d` is C4. Its report `a0ac51c4` reads "FAILED at W: stray cobalt_dev rows" (`git log main..s3/exits-c4`). DRC D1–D3 is on branch `drc/d1-trading-log`, tip `7dd031fb`. The radar stop-record fix, `4c1f4911` (branch `radar/stop-record-0928`, tip `1a555ebb`), touches `radar/evaluate.py`, `radar/seam.py` and tests; it adds no migration and does not bump `EVALUATOR_VERSION` (`git diff main...4c1f4911`).

### 1e. ADR-0008

A prediction record is USER data: `docs/10 - Decisions/ADR-0008-two-layer-data-model.md:131` ("legs/fills, missed, DRC rows, prediction records | user"). The table name is already declared as `prediction_records → Side.USER` (`src/cobalt/db_migrations/placement.py:108-112`). It references `system.radar_score_run` by id; 0006 already grants REFERENCES on that table to `cobalt_user` (`0006:198-199`).

`[F-02]` Grok (WRONG FACTS 1), verbatim: "`10-PROPOSAL.md:77` says `prediction_records` is declared at `placement.py:108-112`. The staged file and part2's placement grep put `"prediction_records": Side.USER` at `placement.py:115`. The side is right; the lines are not. (`22-migrations.excerpt.sql` header says the same.)" (Hub GC1 HOLDS.)

---

## 2. SCOPE

- **MVP F15 records the radar card grade: S1–S5.** One record captures all five: dots (engine and tapped), conviction, proximity, `card_score` with suppression, and proposed key. That is what the ladder's "any card's grade" means and what the S3 smoke replays.
- `[F-03]` The Anthropic seat (S2 `ADOPT WITH`), verbatim, replacing the proposal's "S6 is replayed as a side effect" sentence: "S6 is replayed by `cobalt radar audit-export --run <run>`, which re-evaluates the run and compares each label with `system.radar_score.evaluation` (`audit_export.py:257-271`). `replay_receipt` alone returns the evaluations and compares nothing (`evaluate.py:1633-1640`). `cobalt cards replay` recomputes and diffs the card grade (S1–S5) only and prints the audit-export line for S6." (Hub FC8 HOLDS.)
- A manual card has no derived grade: its key is his. Replay prints that and exits 2 (§5).
- **Later chunks:**
  - S7 health: a scan record could carry the pills. The thresholds need storing first.
  - S8 pool rank: the rank's screener inputs first need to be confirmed as stored (experiment X2).
  - S9 handicap: shadow only.
  - S10: already stored with its inputs.
  - S11: when the desk ships.
  - ASET sizing replay.
  - "R had Cobalt's stop held".
- **Price of MVP scope vs the charter's "all":** the charter's "all scored objects" (`MVP-CHARTER-v0_2.md:173`) is met for the card and deferred for S7–S11. Doing S7 and S8 now would add about one M chunk each, with a migration each.

## 3. THE RECORD

**One append-only table, one writer (L3).** Columns on existing rows are rejected: the card row is a current-value cache that refresh and tap overwrite (G1). Widening `card_dot_taps` plus reusing receipts would give the corpus two sources and leave G3 open (Open point 1).

`"user".prediction_records` — migration `0022_prediction_records.sql` + `.rollback.sql`, the 0007 tenancy shape:

| Column | Content |
|---|---|
| `id`, `user_id` | identity; `user_id NOT NULL` + FK + tenant GUC default (`0007:119-120` shape) |
| `card_id` | FK `"user".aset_sizings(id)`, **no cascade** (the `legs` shape, `0021`); a corpus row outlives nothing it describes |
| `seq` | per card, 1..n; `UNIQUE (card_id, seq)` |
| `kind` | `create` · `refresh` · `tap` (CHECK); extensible by later scorers |
| `at` | the write's instant |
| `scorer_id` | `card_grade` (CHECK list; a swing / options scorer adds its id) |
| `scorer_version` | `EVALUATOR_VERSION` (`evaluate.py:163`) |
| `formula_sha256` | `formula_sha256()` (`evaluate.py:196-201`) |
| `settings_sha256` | `CardSettings.sha256()` of the settings the write used |
| `run_id` | FK `system.radar_score_run(id)`; NOT NULL for `create`/`refresh`, NULL for `tap` (CHECK) |
| `inputs` | JSONB, validated by a Pydantic `RecordInputs` before INSERT (L10) — below |
| `output` | JSONB: `published_numbers(...)` (`evaluate.py:1597-1608`) + `proposed_key_reason` |
| `why` | TEXT, written by ONE pure code function `grade_why(score, dots)` in `scoring.py` — never an LLM |

Immutability: BEFORE UPDATE and BEFORE DELETE triggers call the existing `"user".refuse_row_update()` (`0007:105-113`). A re-score is the next record, and a correction is a new record. Nothing is ever edited. `[F-06 · NEEDS ROUND 2 (R2-2)]` The trigger set is disputed. Grok's F-05 block keeps UPDATE + DELETE. The Anthropic seat's alternative block (below) refuses UPDATE only. Experiment X8 gates it.

`inputs` by kind (values, not hashes; heavy inputs by reference to the immutable receipt):
- `create` / `refresh`: `{receipt: "by run_id", card: {entry, stop, definition_md5, assumed_keys, taps:[{id,factor,grade}]}, taps_moved: bool, locked: {conviction, score_suppressed} | null}`. This is the card's slice of the receipt (`evaluate.py:2053-2058`) plus the lock-time values G3 needs.
- `tap`: `{tap_id, dots:[{factor, source, tier, na_reason, engine_grade, trader_grade}] as locked, proximity, score_suppressed_before, bands:{<card.proposed_key keys>}, enabled:[keys]}`. The row is self-contained and needs no receipt, which closes G1 and G2.
- `[F-05]` Amended by the F-05 block below: in the create / refresh line, `locked` reads `{conviction, score_suppressed, proposed_key}`; in the tap line, `bands` is `settings.proposed_key`. Under the alternative block, the create / refresh `inputs` drop the `card` slice and read it from the receipt instead (R2-1).

**Where it is written.** `[F-05 · NEEDS ROUND 2 (R2-1)]` This block replaces the proposal's `inputs` / writer / `tap_dot` sentences. The draft carries Grok's wording (S3 `ADOPT WITH`), verbatim:

> `at` is the card-write instant (`instant` for create/refresh, the tap's `ts` for tap), never the receipt-insert time. Replay, the decision grade, and the ROW comparison order by `(at, id)`. `seq` is only `UNIQUE (card_id, seq)`.
> The one writer, `cards/predictions.py::insert_record`, locks `aset_sizings` `FOR UPDATE` on that `card_id` and sets `seq = COALESCE(MAX(seq),0)+1` in the same transaction as the INSERT. `tap_dot` already holds that lock. `write_receipt` takes it per card before inserting that card's create/refresh record.
> `refresh` `inputs.locked` is `{conviction, score_suppressed, proposed_key}` read from the locked row. The refresh SELECT (`store.py:1028-1029`) adds `proposed_key`. `proposed_key_reason` is not a column; a taps-moved refresh does not recompute it.
> `tap_dot(card_id, factor, grade, *, settings, enabled, now=None)`. `bands = settings.proposed_key` and `settings_sha256 = settings.sha256()`. There is no separate `bands` argument. A missing `settings` or `enabled` raises. Production callers: `aset/web.py:1366`, `radar/evaluate_cli.py:412`. Test callers that hit the real method or mock this signature: `tests/cobalt/test_radar_cards_db.py:236`, `:273`, `:334`; `tests/cobalt/test_rubberband_forms.py:585`, `:612`, `:634`; `tests/cobalt/stale_db_support.py:170`; `tests/cobalt/test_radar_card_routes.py:49`; `tests/cobalt/test_radar_evaluate_cli.py:139`.
> Tap `inputs.dots` are the locked dots after the trader-grade update. Scan `inputs` stay a slice plus `run_id`; they are not self-contained. Bars stay in the receipt.
> `output` for a taps-moved refresh is the grade the UPDATE wrote, specified in S5, not `published_numbers` of the stage update.
> Immutability is `BEFORE UPDATE OR DELETE` calling `"user".refuse_row_update()`, not a copy of `0007`'s UPDATE-only triggers (`0007:188-190`, `:199`).
> `card_id` FK to `"user".aset_sizings(id)` with no cascade (default RESTRICT). `0021`'s legs shape was not staged; RESTRICT stands on its own so a corpus row cannot be dropped by a card delete and cannot dangle.
> `last_price_at` is in `0022` (O4). It is not an input to replay.

Under this block the proposal's placement stands: `tap` inside `tap_dot`'s transaction (`store.py:1204-1250`); `create` / `refresh` inside `write_receipt`'s transaction (`store.py:1082-1102`), the stage collecting each card's written numbers, `refresh_radar_card` returning what it actually wrote. A run that fails before its receipt writes no records. The card row then holds numbers that no record carries, and replay says so (§5 ROW line). G5 in the card row is named here, not fixed (Open point 3; OWED as its own lane, R59).

The alternative round 2 weighs, the Anthropic seat (S3 `ADOPT WITH`), verbatim:

> "WHERE IT IS WRITTEN. Each record is written by `cards/predictions.py::write_record(conn, …)` on the caller's open transaction, inside the transaction that writes the card-row numbers it describes:
> - `create`: in `create_radar_card`'s `work`, after the INSERT returns an id (`store.py:1001-1012`). No record when `ON CONFLICT` returns None. `run_id` = `spec.evidence['run_id']` (`evaluate.py:1976`).
> - `refresh`: in `refresh_radar_card`'s `work`, after the UPDATE and the dot upsert (`store.py:1039-1059`). The stage passes `run_id=` as a new keyword (in scope at `evaluate.py:1924`). `output` = the values the UPDATE wrote, with the dots re-read by `_dots_for` (as `tap_dot` does at `:1233`).
> - `tap`: in `tap_dot`'s `work` after its UPDATE (`:1242-1246`).
>
> `seq` = 1 + the card's max `seq`, taken while the `aset_sizings` row lock is held. Every record writer holds that lock (`store.py:1030`, `:1206`; `create` holds the new row). `write_receipt` is UNCHANGED.
>
> A new column `card_state TEXT NOT NULL`: the state read under that lock (`store.py:1028`, `:1206`; `WATCH` for create).
>
> `inputs` for `create` / `refresh` = `{taps_moved, locked: {conviction, score_suppressed} | null}`. The card's slice (entry, stop, definition_md5, assumed_keys, taps) is read from its run's receipt `tap_versions.cards` by `card_id` (`evaluate.py:1644`, `:2053-2058`), never copied.
>
> Order is `seq`, never `at`. `at` = the `ts` the store wrote under: the scan instant for create / refresh (`evaluate.py:1926`, `:1984`), the wall clock for a tap.
>
> Immutability: a BEFORE UPDATE trigger calling `refuse_row_update()` — the 0007 / 0021 shape (`0007:188-199`; 0021's `legs_append_only`). There is no DELETE trigger."

Price of the two, from the seats' own words, not measured:
- Grok's changes `write_receipt(row, records)` and adds the stage's collection. It takes the card lock per card inside the receipt transaction.
- The Anthropic seat's changes neither. It leaves `write_receipt`'s three test sites alone and adds one column (`card_state`) and one kwarg (`refresh_radar_card(run_id=)`).
- The hub's file-check marks the ordering and collision outcomes UNVERIFIABLE FROM READS (GC14, FC23). Experiments X5 and X6 decide them.

**G4 (priced, recommended in the same migration):** `aset_sizings.last_price_at TIMESTAMPTZ`, written with `last_price` from `ev.last_bar_ts` (`evaluate.py:622`) inside the same `COALESCE` pair (`store.py:1040`, `:1049`). Cost: one column, two SQL edits, one test. Replay does not need it, because the receipt holds the bars. It closes C3's ESCALATE 3 at the source. Wiring legs' `price_asof` to the new column is S3 code and stays S3's follow-up. `[F-19]` The column sentence is replaced by §Open point 4's `[F-19]` block (NEEDS ROUND 2, R2-3).

Volume: one `refresh` record per open card per scan, a few kB each (the per-card `output.dots` dominates). Bars stay in the receipt. The "few kB" is UNVERIFIED (grok, the Anthropic seat); experiment X9 measures it.

## 4. THE L57 GAPS — cost and what replay prints

| Gap | Closed by | Cost | A card graded before F15 lands |
|---|---|---|---|
| G1 tap result | `tap` record `output` | in P1 | tap events: `NOT REPLAYABLE — graded before F15: a tap's result and settings were not stored (L57)` |
| G2 tap settings | `tap` record `inputs.bands/enabled` + `settings_sha256` | in P1 | same line |
| G3 taps-moved | `refresh` record `inputs.locked` + the written numbers | in P1 | scan events replay via the receipt; a taps-moved scan shows `DIFF card_score` against the receipt's `published` — the truth, not a defect of replay |
| G4 `last_price` bar time | `last_price_at` column | +1 column in P1 (Open point 4) | `last_price_at: not stored (before F15)` |
| G5 card before receipt | records written with the receipt | in P1 for records; the row-level window stays | `ROW: holds numbers no record stores` |

For a card graded before F15 lands, replay prints `NO PREDICTION RECORDS — graded before F15 lands` and the `cobalt radar audit-export --run <run>` line for the run of its `radar_score_id`, then exits 2. Its scan grades remain auditable that way. No backfill (Owner item 1 — settled by the houses, see §Owner items). `[F-07 · NEEDS ROUND 2 (R2-1)]` The proposal's paragraph is kept. Round 2 weighs two wordings:
- Grok's S4 wording splits the no-records case. The derive does not fold it: its command reads `cobalt radar audit-export --run <radar_score_id>`, but `aset_sizings.radar_score_id` references `system.radar_score(id)` (`0007_radar_cards.sql:50`), a seam row, while `--run` takes a `system.radar_score_run` id (`0006_radar_score.sql`, `radar_score.run_id`). This was read by the derive; no hub checked it.
- The Anthropic seat's S4 wording makes G5 a per-record NOT REPLAYABLE line, which depends on R2-1's write site.

## 5. `replay(card_id)`

**Command:** `cobalt cards replay <card_id> [--json]`, in the existing `cobalt cards` family (`cards/cli.py:190-245`). It reads only: stored records, receipts and taps. It fetches no market data, reads no current settings and writes nothing.

**Replay runs against the RECORDED scorer.** Replay is proven through `replay_receipt`, which refuses a receipt of another `EVALUATOR_VERSION` (`evaluate.py:1616-1622`). Today's code therefore recomputes a record only when its version equals the recorded `scorer_version`. A replay has to show that stored inputs reproduce the stored grade. Re-grading with today's formula answers a different question, a what-if for the curve tribunal (Open point 2).
- `formula_sha256` differs but the version is equal: replay runs and prints `NOTE formula source changed since record #k; replayed with current code`. This is the audit-export rule (`audit_export.py:296-298`).
- Version differs: `#k NOT REPLAYABLE — recorded scorer s…, this code s…; replay from the deploy that wrote it`.

**Per record, decision grade, exit codes.** `[F-08 · NEEDS ROUND 2 (R2-1)]` This replaces the proposal's per-record, decision-grade and exit-code sentences. The draft carries Grok's wording (S5 `ADOPT WITH`), verbatim:

> Order by `(at, id)`.
> `create` / `refresh` with `taps_moved` false: `replay_receipt` on `receipt_for_run` → `receipts_chain`. Diff `output` against that card's `recomputed`, plus `proposed_key_reason` from `proposed_key(conviction, bands, enabled)` using the receipt's settings. `replay_receipt` raises `ReplayError` on a version mismatch: catch it and print NOT REPLAYABLE. Do not let it abort the command.
> `refresh` with `taps_moved` true. Rebuild output as the store wrote it (`store.py:1037-1038`), then diff:
> proximity and dots = the receipt recompute (engine snapshot);
> conviction = `inputs.locked.conviction`;
> proposed_key = `inputs.locked.proposed_key` (not recomputed);
> score_suppressed = the receipt's published `score_suppressed` if proximity is None, else `inputs.locked.score_suppressed`;
> card_score = `card_score(locked conviction, proximity, that sentence)`.
> `tap`: locked dots → `conviction` → the NULL-proximity branch at `store.py:1235-1239` (kept sentence, else `PROXIMITY_UNKNOWN`) or else `suppression(dots)` → `card_score` → `proposed_key(conv, settings.bands, enabled)`. Diff `output`.
> `why` is recomputed with `grade_why` from those same fields and diffed. `grade_why` reads no other source.
> Decision grade: the last record with `at` strictly before the first `card_transitions` row that leaves WATCH. None, if the card is still WATCH. Derived, never stored.
> ROW compares the card's current conviction, proximity, card_score, score_suppressed, proposed_key to that latest record's `output`.
> Exit 0 only when every record is MATCH and ROW matches. Exit 1 when any record DIFFs or ROW does not match, including `ROW: holds numbers no record stores`. Exit 2 when nothing differs and something is NOT REPLAYABLE (pre-F15 with a receipt, manual card, other `EVALUATOR_VERSION`). Manual copy: `manual card: the key is the trader's; there is no derived grade`. A usage error is argparse. The S3 smoke passes on 0 and on nothing else.
> Version equal and `formula_sha256` different: replay with this code and print the NOTE. Version different: NOT REPLAYABLE, name both versions, do not re-grade.

(`ReplayError` exists at `evaluate.py:1516` and is raised on a version mismatch at `:1619`. The derive read this; no hub checked it. The `store.py:1037` rule for NULL proximity: hub GC8 HOLDS.)

The alternative round 2 weighs, the Anthropic seat (S5 `ADOPT WITH`), verbatim:

> "Per record:
> - A taps-moved `refresh` reproduces the store's rule: `suppressed = inputs.locked.score_suppressed` when the recomputed proximity is not NULL, else the recomputed `score_suppressed` (`store.py:1037`). `card_score = card_score(locked.conviction, recomputed.proximity, suppressed)`. The record's `conviction` and `proposed_key` are the row values the refresh left untouched: diffed against the preceding record's, not recomputed.
> - The DECISION GRADE is the last record whose `card_state = 'WATCH'`. It is never derived from timestamps.
> - Numeric fields are compared as `Decimal` values, never as strings.
> - A pre-F15 card's audit-export line names `system.radar_score.run_id` of its `radar_score_id` (a seam-row id, not a run id).
> - Exit 0 only when every record MATCHes and ROW matches. The S3 smoke passes on 0 and on nothing else."

What round 2 must answer:
- Is the decision grade derived from `at` against `card_transitions`, or from a `card_state` column written under the row lock?
- Is the order `(at, id)` or `seq`?
- Both seats agree on the taps-moved suppression rule (GC8) and on "the S3 smoke passes on 0 and on nothing else".
- Experiments X6 (interleavings), X7 (Decimal read-back) and X10 (JSONB round-trip) gate the compare.

**Output (text):**
```
card 11890 XMPL long · radar · CLOSED · scorer card_grade s2p2.3 · 14 records
#1  create   09:41:03  MATCH
#7  tap      09:52:40  MATCH            ← decision grade (last record before ARMED)
#9  refresh  09:55:00  DIFF card_score recorded 57 → replayed 58
#12 refresh  10:03:00  NOT REPLAYABLE — run 4411 has no receipt (L57)
ROW: matches record #14
OUTCOME: CLOSED · realized R +1.20 provisional (1 estimated leg) · missed: none · Cobalt-stop R: not computed (S3 §7 seam 7)
card 11890: 14 records · 12 match · 1 differ · 1 not replayable
```
(The illustrative numbers are constructed, not his.) `[F-15]` The Anthropic seat (WRONG FACTS 2), verbatim: "Proposal §3 (`:126`) says "A run that fails before its receipt writes no records". Its own §5 sample (`:162`) prints `#12 refresh … NOT REPLAYABLE — run 4411 has no receipt`, a record that §3 says cannot exist." (Hub FC19 HOLDS.) Under the F-05 block the `#12` line cannot occur. Under the alternative it can. R2-1 decides which, and the sample follows.

`[F-25]` Grok (D `ADOPT WITH`), verbatim, replacing "`--json` emits the same rows for a checker house (L52 d)": "`cobalt cards replay --json` emits, per record, `at`, `kind`, `scorer_version`, `formula_sha256`, the stored `inputs`, the stored `output`, the recomputed output, and MATCH / DIFF / NOT REPLAYABLE. A house diffs those objects without taking the label as the evidence. `cobalt radar audit-export --run <id>` is unchanged and remains the run-level check."

## 6. THE JOIN TO OUTCOME

**When an outcome is final.** `[F-09]` Grok (S6 `ADOPT WITH`), verbatim, replacing the proposal's three bullets and its "written none" sentence:

> `corpus` calls `legs.realized_r` and uses that return's provisional flag. It does not restate the estimated-leg rule and it does not recompute `cf_r`. It reads the current `"user".missed` row (`is_current`, `kind = 'card'`, `card_id`) for `cf_r`, `mfe_r`, `excluded_by`.
> CLOSED: final or provisional solely from `realized_r`. FILLED and not terminal: `open`. EXPIRED / PASSED / MISSED / not-filled: `final` only when that current missed row exists; otherwise `awaiting nightly replay`. Absence of a row is never `missed: none` / final. The nightly job's "ran and wrote none" artifact is not in this packet; do not invent one.
> `cobalt cards replay`'s outcome line calls `corpus` for that one card. `n` per `outcome_status` is printed before any row. No EV and no aggregate grade.

(Experiment X11 tests whether a card that never triggers ever receives a `missed` row; the Anthropic seat's claim is FC16, UNVERIFIABLE. If it never does, such a card reads `awaiting nightly replay` for good, and the Anthropic seat's alternative status becomes the round-2 question. See the fold table, F-09.)

**ONE read:** `cards/predictions.py::corpus(since) -> list[CorpusRow]`, one row per card:
- decision record, final record, record count;
- state, `realized_r(...)`, and whether it is provisional (the S3 function, never re-implemented: L3);
- the `missed` current row (`cf_r`, `mfe_r`, `excluded_by`);
- the `picks` row;
- `outcome_status` ∈ {open, provisional, final, awaiting nightly replay}.

A SQL view would have to copy the realized-R arithmetic, so the read is Python (L3).
- Surface: `cobalt cards corpus [--since YYYY-MM-DD] [--json]` prints n per status first (L8) and every row. It computes no EV and no aggregate grade; an aggregate stays under L8's rule. The corpus is observation only; nothing in it promotes a scorer (L7).
- `cobalt cards replay` prints the same outcome line for one card (§5).

## 7. WHAT HE SEES

The smallest surface is two CLI reads, `cobalt cards replay <id>` and `cobalt cards corpus`, which the desk runs and reads to him. No card chip and no DRC cell are added in MVP. The panel is S3 C3's (`aset/radar_panel.py`) and the DRC note is his sitting (L67). A "replayable" chip on the card is priced in Open point 5. Nothing is hidden: every NOT REPLAYABLE line names its reason, the corpus prints its n, and a pre-F15 card says it is one.

## 8. INTERACTION WITH IN-FLIGHT WORK

| Branch | Shared files with F15 | Migration | Conflict |
|---|---|---|---|
| S3 C1–C4 `s3/exits-c4` | `cards/store.py` in other functions (`fill`, `set_card_stop`, `_insert_stop_edit`; F15 touches `create_radar_card`, `refresh_radar_card`, `tap_dot`, `write_receipt`); `db_migrations/__init__.py`, `placement.py` | 0021 | textual in the registries only; F15's corpus read CALLS `legs.realized_r` / `legs_current_v` → P2 builds on a tree carrying `s3/exits-c4` |
| DRC D1–D3 `drc/d1-trading-log` `7dd031fb` | `db_migrations/__init__.py`, `placement.py` | 0016, 0018, 0019, 0020 | registries only |
| Radar stop record `4c1f4911` | `radar/evaluate.py` (seam detail + a log line; F15 edits the stage's receipt write) | none | different hunks; neither bumps `EVALUATOR_VERSION` |

`[F-11]` Gemini (S8 & 9 `ADOPT WITH`), verbatim: "The shared files table adds `aset/web.py` to S3 C1–C4 and `radar/seam.py` to the 4c1f4911 row." (Hub GC15, GC16 HOLD.)

`[F-12]` The Anthropic seat (WRONG FACTS 3), verbatim: "Proposal §8 (`:198-199`) lists S3's shared files as `cards/store.py`, `__init__.py`, `placement.py`, and DRC's as "registries only". `git log --name-only main..s3/exits-c4` shows `cards/cli.py`, `aset/web.py` and `db_migrations/cli.py`; `main..drc/d1-trading-log` shows `aset/web.py`." (Hub FC10a, FC10b, FC10c, FC11 HOLD.) The full, cited list is `## SEAM` below.

- **Numbering:** `cobalt_dev` is at `0013` (`cto-2026-09-28.md:191`, R182). The branches take 0016, 0018–0020 (DRC) and 0021 (S3). **F15 takes 0022.** (Hub GC13 / FC21 HOLD: neither branch has a 0022.)
- **Landing order:** DRC and S3 land first, and F15 lands on or after them in the same stacked deploy (L68 integrated gate on the combined tree; L43, one window).
- **No `EVALUATOR_VERSION` bump:** F15 changes no number and does not change the receipt shape. The bytes of `evaluate.py` change, so `formula_sha256` changes, which the NOTE line covers. (Experiment X3 checks that no number changes.)
- **Swing / options:** records key on `scorer_id` + `scorer_version`. A scan record references its run's receipt, whatever bars that receipt holds, and a tap record is self-contained. No i1 or intraday assumption is baked into the table.
- **Shared seam (L72):** P2 reads the record shape P1 writes. The FINAL's §3 table and the Pydantic `PredictionRecord` model are the settled seam both prompts cite, so P1 and P2 build in parallel. (Not settled in this DRAFT: R2-1 and R2-5.)
- **RESTARTS (L42):** changes to `cards/*`, `radar/evaluate.py` and `aset/web.py` restart `com.cobalt.radar` (in the 20:00–21:00 pause, L43) and `com.cobalt.aset`. `cobalt jobs restarts <range>` gives the table.

## 9. CHUNKS

The chunk table the build drafter cites is `## CHUNKS` below. The proposal's §9 is kept there, amended only where a fold row says so.

**Evenings from "tribunal ruled" to "the S3 smoke's replay line can pass": 2** (the proposal's GUESS; both grok and the Anthropic seat mark it UNVERIFIED).
- Evening 1: P1 and P2 build in parallel worktrees.
- Next day: three-house checks.
- Evening 2: one deploy carrying S3, DRC and F15 under the stacked gate (L43, L68, L66).
- The next trading morning: the smoke.

Against S3's stop on 10-07: if the tribunal rules by 10-01, the smoke can run 10-05 or 10-06. The binding risk is the single `cobalt_dev` lock (L76), which S3's and DRC's with-DB reruns also hold. "Tribunal ruled" now means a FINAL after round 2.

---

## L52 (a)–(d)

F15 changes no ranking. It adds no number, factor or order. `card_score` stays the one authority. L52 still binds because F15 touches what reaches the card: it hooks the card's score writers and adds a replay of the scorer.
- **(a)** `[F-22 · rides R2-1]` Grok (A `ADOPT WITH`), verbatim: "`ADOPT WITH` S3's `inputs.locked` and S5's rebuild. Then every recorded grade number traces to stored inputs or the receipt those inputs name." The proposal's sentence stands beside it: a scan record points to its receipt, and a tap record holds its dots, proximity, bands and enabled keys. A number whose inputs are missing is printed NOT REPLAYABLE with the reason, never defaulted (L1).
- **(b)** There is exactly one ranking authority, `card_score` (`scoring.py:1-2`). Records observe it and never feed it (L7).
- **(c)** `[F-24]` Grok (C `ADOPT WITH`), verbatim: "`ADOPT WITH` S3, S4, S5, and S6's pasted sentences as the seam a build prompt cites. The proposal names the artifacts and still leaves these unspecified: the taps-moved `output` rebuild, `(at, id)` order, the `seq` lock, the `tap_dot` signature (settings, not a second bands), the no-records exit split, the decision grade when the card is still WATCH, ROW's exit code, and corpus refusing to treat a missing `missed` row as final." The seam artifacts: the `0022` DDL, the `PredictionRecord` / `RecordInputs` Pydantic models, the writer's signature in `cards/predictions.py`, the write-site signature (R2-1), and the replay output and exit codes of §5. Still unwritten as text is R2-5: the DDL text, `grade_why`'s sentence rule and the `--json` field types.
- **(d)** Another house can audit it without Cobalt's word: `cobalt cards replay --json` (F-25's fields) and the unchanged `audit-export --run` recompute from DB rows alone.

## What this does NOT do

- It does not record S7–S11, sizing, or "R had Cobalt's stop held".
- It does not backfill cards graded before F15 lands.
- It does not re-run old scorer versions (no worktree checkout of old code).
- It does not re-grade with today's formula.
- It adds no card chip, DRC cell, EV or aggregate grade.
- It does not fix G5's row-level window (the card row committed before the receipt; OWED as its own lane, R59). It does not wire legs' `price_asof` to `last_price_at`.
- It does not edit `cards/shadow_report.py:13-15` (OWED, the L32 fix lane, R59; all three seats: a plain edit, no design ruling).
- It does not change `EVALUATOR_VERSION`, the receipt shape, any curve, or any of his settings.

## Open to the tribunal — as ruled in round 1

1. **One new table vs widening `card_dot_taps` and reusing receipts.** ADOPTED 3-0 (grok, gemini, the Anthropic seat). Rejected alternative: a tap row gains output and settings columns, scan grades are read from receipts by searching `tap_versions.cards` for the card id, and no new table is added. It is smaller by one table. It was rejected for three reasons: the corpus would join two sources, G3's locked numbers would have no home, and the JSON search needs a GIN index over a growing table. `[F-16]` Gemini's O1 reason ("a GIN index on `card_dot_taps`") is not folded: hub GC19 DOES NOT HOLD as worded.
2. **Replay against the recorded scorer only.** ADOPTED 3-0. Rejected alternative: recompute with CURRENT code across versions and diff. That measures formula drift, not replay. It belongs to the curve tribunal as a separate `--as-current` flag, if wanted.
3. **Leave G5's row window open.** ADOPTED 3 of 3 (grok, gemini: ADOPT; the Anthropic seat: ADOPT WITH per-record exposure, which rides R2-1). Named gap; the ROW line exposes it; OWED as its own lane (R59). Rejected alternative: write the receipt before the card rows. The receipt lists card ids that are created in the same pass, so the ordering is circular. Breaking the cycle means restructuring the stage beyond F15's size. Replay's ROW line exposes the window instead.
4. **`last_price_at` inside F15's migration.** ADOPTED 3 of 3 that it is in 0022. `[F-19 · NEEDS ROUND 2 (R2-3)]` The draft carries Grok's column sentence (O4 `ADOPT WITH`), verbatim: "`0022` adds `"user".aset_sizings.last_price_at TIMESTAMPTZ`. Both refresh UPDATEs (`store.py:1040`, `:1049`) set `last_price = COALESCE(%s, last_price)` and `last_price_at = COALESCE(%s, last_price_at)`. The stage passes `last_bar_ts` only when `last_price` is not None; when `last_price` is None it passes NULL for both, so a stale scan keeps the previous pair. Replay does not read the column. Wiring `legs.price_asof` is S3's follow-up and is not in F15. C3's ESCALATE 3 is not a basis: that report is not staged." The alternative round 2 weighs, the Anthropic seat (O4 `ADOPT WITH`), verbatim: "Column `aset_sizings.last_price_bar_ts TIMESTAMPTZ`, written with `last_price` inside the same `COALESCE` pair from `ev.last_bar_ts` (a new `CardUpdate.last_price_bar_ts`, set in `refresh_card` beside `last_price=ev.last_price`, `evaluate.py:1371`). It holds the i1 bar's START, as the evaluation does: the price's close time is +1 minute, as `stale_reason` derives it (`scoring.py:350`). The column is added to `db_migrations/cli.py`'s `TABLE_DIGEST_EXCLUDED_COLUMNS['aset_sizings']`." (Hub FC18 HOLDS: `last_bar_ts` is the bar START. FC10c HOLDS: the tuple exists at `db_migrations/cli.py:104-113`.)
5. **No "replayable" chip on the card.** ADOPTED 3-0. Rejected alternative: a chip on the panel. It is one more render in `radar_panel.py`, which C3 is still changing, and the CLI already answers the smoke.
6. **A `refresh` record every scan.** ADOPTED 3-0. Rejected alternative: record only when the output changes. Proximity moves with nearly every price, so deduplication saves little and adds a compare-with-previous query to the write path. Experiment X9 (volume) reopens this only if it measures large.

## Owner items

Neither of the proposal's two items passes the owner test (L67 as amended 2026-09-24), as grok and the Anthropic seat ruled. The houses' mechanism is folded (fold rows F-28, F-29). Gemini ruled that both pass. That split is carried in the derive report's `## OWNER ITEMS`, and Astra rules it in round 2.
1. **Cards graded before F15 lands stay partly unreplayable.** Folded as fact: their tap grades have no stored result or settings. Replay prints NOT REPLAYABLE. No backfill: a backfill would invent them (L1, L57).
2. **The corpus retention.** Folded as: keep indefinitely, USER side only, never pruned, never shipped (L57, L32). Grok, verbatim: "A later request to delete or to ship would be his."

---

## First-gate experiments (L70)

Each runs in dev or in a scratch worktree. With-DB runs go under L76's lock, with a migration applied only inside the suite's rollback. Each is listed before the chunk it gates. The ones gating R2-1/R2-2 run before round 2 closes where the meters allow; otherwise round 2 rules on reads, and the experiment gates the FINAL's P1.

| X | Named by | What runs | Gates | Result that changes the design |
|---|---|---|---|---|
| X1 | proposal (UNPROVEN) · gemini X2 · grok X3 · anthropic X5 | receipt retention: `grep -rn radar_score_receipt` over the whole repo (`ops/`, `dev_utils/`, scripts) + a `pg_catalog` read on `cobalt_dev` for rules, triggers, cron on the table; row counts vs complete runs | P1 | any delete path → scan records need a retention floor for their receipts, or an embed of the card slice + bars |
| X2 | proposal (UNPROVEN) · gemini X1 · grok X2 | whether one scan's pool-rank screener inputs are stored (the receipt's `ordered_cohort`, `radar/store.py` write) | the later S8 chunk; not P1 / P2 | not stored → S8 stays out; stored → S8 still a later chunk |
| X3 | grok X5 | a fixture receipt (`tests/cobalt/test_radar_cards_db.py:97-132` shape) replayed after the F15 diff | P1 | any DIFF → shrink the diff until it matches, no `EVALUATOR_VERSION` bump |
| X4 | grok X7 · hub FC12 (UNVERIFIABLE) | `git diff --name-only main...radar/stop-record-0928` and the `radar/evaluate.py` hunks vs F15's stage hunk | P1 landing order; `## SEAM` | overlap, or a file beyond `evaluate.py` / `seam.py` → landing order and SEAM change |
| X5 | anthropic X1 · hub GC14 / FC23 (UNVERIFIABLE) | two sessions on one synthetic card: `tap_dot` vs the receipt-transaction record insert, under each R2-1 write site | P1 write site (R2-1) | a unique-key failure that rolls back a receipt → the receipt-transaction site is wrong |
| X6 | anthropic X2 | real-shape `world` fixture (`test_radar_cards_db.py:44-93`): (a) a tap between the stage read and `refresh_radar_card`; (b) a tap between the refresh commit and `write_receipt`; assert ROW = the latest record and the decision grade under each R2-1 rule | P1 / P2 (R2-1) | a red ROW or a misplaced decision grade under one rule → that rule is out |
| X7 | anthropic X3 · hub FC9 | psycopg read of NUMERIC(8,6) `conviction` after writing `scoring.conviction()`'s normalized Decimal | P2 | reprs differ → a Decimal compare is required in replay |
| X8 | anthropic X4 · proposal | apply 0022 in the suite's rollback: UPDATE refused; DELETE (refused / allowed); delete a card with records → FK error; `0022.rollback.sql` drops cleanly; `0007.rollback.sql` with 0022 applied → blocked | P1 (R2-2) | decides UPDATE-only vs UPDATE+DELETE and the rollback order |
| X9 | anthropic X6 · proposal "a few kB" · grok UNVERIFIED | `pg_column_size(inputs) + pg_column_size(output)` of one real-shape refresh record × open cards × scans per session (the scan-interval tunable read in dev, never assumed) | P1 (O6) | large → reopens "a record every scan" |
| X10 | anthropic X7 | insert then select a record's `output`; compare with `published_numbers(...)` after the JSONB round trip | P2 | a difference → replay's MATCH needs a canonical compare |
| X11 | hub FC16 (UNVERIFIABLE) | a real-shape card that EXPIRES without triggering, then the nightly replay on `cobalt_dev`: is a `missed` row written? | P2 (F-09 status label) | no row ever → `awaiting nightly replay` never resolves for such cards; the status label goes to round 2 |

Not carried:
- grok X1 (migration numbering): settled by the hub's `git show` listings (GC13 / FC21 HOLD).
- grok X4 (the REFERENCES grant): `0006_radar_score.sql` at `HEAD` carries `GRANT SELECT, REFERENCES ON system.radar_score_run TO cobalt_user;`. The derive read this, and P1's with-DB test proves the FK insert.
- grok X6: grok marked it not a design experiment.

## SEAM

The document P1 and P2 cite (L72). Refs read:
- `main` = `66fdfb76`;
- `s3/exits-c4` tip `a0ac51c4` (a docs-only report commit above C4 `d05ae72d`; hub ESCALATE 1);
- `drc/d1-trading-log` tip `7dd031fb`;
- `radar/stop-record-0928` carrying `4c1f4911` / `67e78a2e`.

| With | File F15 shares | Evidence (file:line at ref) | Status |
|---|---|---|---|
| S3 exits | `src/cobalt/cards/store.py` (F15: `create_radar_card` `:965`, `refresh_radar_card` `:1016`, `tap_dot` `:1191`, `write_receipt` `:1082` on main; S3: `fill`, `set_card_stop`, `_insert_stop_edit`) | proposal §8 | proposal read, not hub-checked (UNSETTLED until the P1 drafter's `git log --name-only main..s3/exits-c4 -- src/cobalt/cards/store.py`) |
| S3 exits | `src/cobalt/cards/cli.py` (F15 adds `replay`, `corpus`, P2) | S3 commits `eb642f05`, `77cf18fd`, `5e77800f`, `d05ae72d` | HOLDS (FC10a) |
| S3 exits | `src/cobalt/aset/web.py` (F15: the `tap_dot` call, `:1366` on main) | 6 S3 commits (`d05ae72d`, `6114304e`, `78549817`, `5e77800f`, `3ceb3b11`, `eb642f05`) | HOLDS (GC15, FC10b) |
| S3 exits | `src/cobalt/db_migrations/cli.py` `TABLE_DIGEST_EXCLUDED_COLUMNS['aset_sizings']` (`:104-113` main) | S3 `eb642f05` | HOLDS (FC10c); whether F15's column joins the tuple is R2-3 |
| S3 exits | `src/cobalt/db_migrations/__init__.py`, `placement.py` (`prediction_records` `:115` main: DECLARED → CREATED) | proposal §8; GC1 | placement line HOLDS; the S3 edit to both registries: proposal read |
| S3 exits | `legs.realized_r`, `legs_current_v` (P2 calls them) | `s3/exits-c4:src/cobalt/cards/legs.py:677-705`; `0021_legs.sql` | absent on main (grok part2 grep; anthropic `git log -S`); P2 builds on a tree carrying `s3/exits-c4` |
| S3 exits | migration `0021` (legs); `card_id` FK shape without cascade | `s3/exits-c4:0021_legs.sql` (`card_id … REFERENCES "user".aset_sizings(id)`, no `ON DELETE`) | HOLDS (GC18) |
| DRC | migrations `0016`, `0018`–`0020` | `git show drc/d1-trading-log:src/cobalt/db_migrations/` | HOLDS (GC13, FC21) |
| DRC | `src/cobalt/aset/web.py` | `d5b72392`, `807c13ec`, `0075db31` | HOLDS (FC11) |
| DRC | `db_migrations/__init__.py`, `placement.py` | proposal §8 | proposal read, not hub-checked |
| Radar stop record | `src/cobalt/radar/evaluate.py` (F15: the stage's receipt write) | `67e78a2e` | HOLDS (GC16); hunk overlap UNSETTLED → X4 |
| Radar stop record | `src/cobalt/radar/seam.py` | `67e78a2e` | HOLDS (GC16, F-11); "only these two files" UNVERIFIABLE (FC12) → X4 |

- **Migration number:** `0022`, after every branch's (0016, 0018–0020 DRC; 0021 S3; none has 0022).
- **Landing order:** DRC and S3 first, F15 on or after them in the same stacked deploy (L43, L68; residents down before the merge, L66).
- **P2** builds on a tree carrying `s3/exits-c4`.
- **P1's base tree** is not settled. The proposal names P2 only. Grok's wording "P1 and P2 worktrees are cut from a tree that already contains `s3/exits-c4`" is not folded: it cites `FORMULA_FILES` at `evaluate.py:20-28`, and hub GC6 DOES NOT HOLD (the tuple is at `:178-187`). This is R2-4.
- **RESTARTS (L42):** `com.cobalt.radar` (inside the 20:00–21:00 pause, L43) and `com.cobalt.aset`, from the `cards/*`, `radar/evaluate.py` and `aset/web.py` changes. `cobalt jobs restarts <range>` gives the table.

## CHUNKS

| Chunk | Content | Files | Size | Builder seat (L29) | Migration | `cobalt_dev` (L76) | Tests it must carry | Gated by |
|---|---|---|---|---|---|---|---|---|
| **P1 — the record** | `0022` + rollback; `cards/predictions.py` (Pydantic `RecordInputs` / `PredictionRecord`, the ONE writer); `scoring.grade_why`; hooks in `tap_dot` (+`settings`, `enabled`), the create / refresh write site per R2-1; `last_price_at` (name per R2-3); `placement.py` DECLARED → CREATED; callers `aset/web.py:1366`, `radar/evaluate_cli.py:412` and the test callers F-05 lists | `db_migrations/0022_prediction_records.sql` + `.rollback.sql`, `db_migrations/__init__.py`, `placement.py`, `cards/predictions.py` (new), `cards/scoring.py`, `cards/store.py`, `radar/evaluate.py`, `aset/web.py`, `radar/evaluate_cli.py`, tests; `db_migrations/cli.py` if R2-3 takes the digest clause | M | write path + migration → Opus 5 floor (Anthropic) or Sol (OpenAI), never auto mode on the write path | yes | with-DB suite under the lock, migration applied only inside the suite's rollback | one record per create, refresh and tap; UPDATE refused, DELETE per R2-2; taps-moved stores the locked numbers; a failed receipt: no record (F-05) or each record NOT REPLAYABLE (alternative), per R2-1; a tap without `settings` is refused; tenancy placement test; rollback leaves no table | X1, X3, X4, X5, X8, X9 |
| **P2 — replay + corpus** | `cobalt cards replay`, `cobalt cards corpus`, `predictions.corpus()`; pure reads; tree carries `s3/exits-c4` | `cards/cli.py`, `cards/predictions.py`, tests | S–M | reads only → any house at the implementation floor | no | with-DB read tests under the lock | MATCH on a create → tap → refresh → fill → exit → CLOSED card; a tampered `output` → DIFF, exit 1; a record at another version → NOT REPLAYABLE, exit 2; a pre-F15 card → exit 2 with the audit-export line; a manual card → exit 2; the ROW line; corpus n per status; `awaiting nightly replay` until `missed` exists | X6, X7, X10, X11 |

- Every test uses real-shape receipt fixtures (`tests/cobalt/test_radar_cards_db.py:97-132`, L45). Settings are constructed values; a test reads `trader_settings` only for an invariant (L69).
- Gate: each chunk runs offline, with-DB and live-note (L68 GATE EARLY). Checks seat Fable (Opus 5.5) · Astra · Grok for the first check of a new build; later checks seat Opus · Sol · Grok (L67).
- No chunk's BUILD depends on an owner item.
- Evenings: 2 (the proposal's GUESS), after the FINAL.

## Dissents, verbatim

None. No seat wrote `REJECT` or `DO NOT BUILD` (hub `## Rulings table`: 0 REJECT, 0 DO NOT BUILD). No wording re-opens R57. No wording pulls G5 or the `shadow_report.py` L32 fix into F15's chunks.

## The bar

- **L1** — a record whose inputs are missing, or whose version differs, prints NOT REPLAYABLE with its reason, never a default. Absence of a `missed` row is never `final` (F-09). A missing `settings` or `enabled` on a tap raises (F-05).
- **L3** — one table, one writer (`insert_record`, or `write_record` under the alternative; the name falls with R2-1), one replay (`replay_receipt` + the `scoring.py` functions the store calls), one outcome read (`corpus`), one realized R (`legs.realized_r`, S3's). `system.radar_score` is a pre-existing second store of S2–S4, observation only, neither read nor fed by F15 (F-01).
- **L7** — records and `corpus` observe `card_score` and feed nothing that ranks. No scorer is promoted from the corpus.
- **L8** — `corpus` prints n per `outcome_status` before any row. No EV, no aggregate grade.
- **L10** — `inputs` validated by the Pydantic `RecordInputs` before INSERT.
- **L28** — F15 writes nothing to the vault.
- **L32** — `prediction_records` is USER-side (`placement.py:115`). Bands and enabled keys are copied into USER rows only, never shipped. This file carries keys only.
- **L45** — real-shape receipt fixtures; no invented fixture where the real one exists.
- **L52 (a)–(d)** — as stated in §L52 above; (c) is not met until R2-1 and R2-5 close.
- **L57** — every grade write on a radar card gets a record with its inputs. Pre-F15 taps are named NOT REPLAYABLE. The G5 row window is named, exposed and OWED.

## OWNER ITEMS

None pass the owner test in this draft (grok, the Anthropic seat: fail; gemini: pass; Astra: pending, round 2). `## FOR DEJAN` in the derive report carries no owner A/B. It carries only the later single approval of the FINAL.
