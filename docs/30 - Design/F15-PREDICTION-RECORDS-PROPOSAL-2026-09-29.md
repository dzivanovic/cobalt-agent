# F15 PREDICTION RECORDS + `replay(card_id)` — PROPOSAL (2026-09-29)

LADDER `S3-P3 · F15` (`docs/00 - Project/SPRINT-LADDER-v0_1.md:648`; charter `docs/00 - Project/MVP-CHARTER-v0_2.md:173`). L67 step: the PROPOSAL of one house (seat `f15-design-0929`, Opus 5.5). The tribunal rules on it and derives the final; nothing is built from this file. Committable: his thresholds and settings appear as KEYS only (L32).

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

Migration directories found (`ls`): `src/cobalt/db_migrations/` (database-wide: 0001–0011, 0013–0015, 0017 on main), `src/cobalt/cards/migrations/` (0001–0002), `src/cobalt/aset/migrations/` (0001–0009).

Existing replay machinery (reused, not rebuilt):
- `evaluate.replay_receipt` recomputes every card number of a receipt from receipt values only (`evaluate.py:1611-1662`). It refuses a receipt written by another `EVALUATOR_VERSION` (`:1616-1622`).
- `cobalt radar audit-export --run` re-derives the run's hashes and replays them. It refuses when the recompute differs from what was published (`radar/audit_export.py:206-271`).
- `receipts_chain` walks the per-day delta chain (`cards/store.py:1122-1135`).
- No pruning of `radar_score_receipt` was visible to a grep of `archiver/`, `backup/` and `jobs/`. That grep is a scoped read; it does not prove the rows are kept (L35).

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
- MISSED counterfactual: `"user".missed`, versioned and never overwritten (`is_current`, `superseded_by`); `cf_r`, `mfe_r`, `excluded_by`; kind `card` carries `card_id` (`0009_picks_missed.sql:47-121`). Written by the nightly replay (`replay/cards.py:1-57`).
- "R had Cobalt's stop held" for a FILLED card: not computed in S3; it is a 21:10 replay-time figure (`docs/30 - Design/S3-EXITS-v3-2026-09-22.md:228`, seam 7).
- Seams S3 left for F15 (`S3-EXITS-v3:228`, `[F-39]`): (4) realized R + provisional + the estimated-legs list; (5) the stop path (`card_stop_edits.kind`, `stop_in_force` per leg); (6) the pick-vs-rank row; (7) the Cobalt-stop counterfactual. The DRC design's only F15 mention is the placement declaration (`docs/30 - Design/DRC-AUTOMATION-v2-2026-09-22.md:40`).
- BUILT, not on main: S3 C1–C4, branch `s3/exits-c4`. `d05ae72d` is C4. Its report `a0ac51c4` reads "FAILED at W: stray cobalt_dev rows" (`git log main..s3/exits-c4`). DRC D1–D3 is on branch `drc/d1-trading-log`, tip `7dd031fb`. The radar stop-record fix, `4c1f4911` (branch `radar/stop-record-0928`, tip `1a555ebb`), touches `radar/evaluate.py`, `radar/seam.py` and tests; it adds no migration and does not bump `EVALUATOR_VERSION` (`git diff main...4c1f4911`).

### 1e. ADR-0008

A prediction record is USER data: `docs/10 - Decisions/ADR-0008-two-layer-data-model.md:131` ("legs/fills, missed, DRC rows, prediction records | user"). The table name is already declared as `prediction_records → Side.USER` (`src/cobalt/db_migrations/placement.py:108-112`). It references `system.radar_score_run` by id; 0006 already grants REFERENCES on that table to `cobalt_user` (`0006:198-199`).

---

## 2. SCOPE

- **MVP F15 records the radar card grade: S1–S5.** One record captures all five: dots (engine and tapped), conviction, proximity, `card_score` with suppression, and proposed key. That is what the ladder's "any card's grade" means and what the S3 smoke replays.
- S6 is replayed as a side effect. A scan record references the receipt, and `replay_receipt` re-evaluates S6 (`evaluate.py:1633-1640`). It needs no row of its own.
- A manual card has no derived grade: its key is his. Replay prints that and exits 2 (§5).
- **Later chunks:**
  - S7 health: a scan record could carry the pills. The thresholds need storing first.
  - S8 pool rank: the rank's screener inputs first need to be confirmed as stored.
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

Immutability: BEFORE UPDATE and BEFORE DELETE triggers call the existing `"user".refuse_row_update()` (`0007:105-113`). A re-score is the next record, and a correction is a new record. Nothing is ever edited.

`inputs` by kind (values, not hashes; heavy inputs by reference to the immutable receipt):
- `create` / `refresh`: `{receipt: "by run_id", card: {entry, stop, definition_md5, assumed_keys, taps:[{id,factor,grade}]}, taps_moved: bool, locked: {conviction, score_suppressed} | null}`. This is the card's slice of the receipt (`evaluate.py:2053-2058`) plus the lock-time values G3 needs.
- `tap`: `{tap_id, dots:[{factor, source, tier, na_reason, engine_grade, trader_grade}] as locked, proximity, score_suppressed_before, bands:{<card.proposed_key keys>}, enabled:[keys]}`. The row is self-contained and needs no receipt, which closes G1 and G2.

**Where it is written (atomic with its inputs, closing G5 for records):**
- `tap`: inside `tap_dot`'s transaction (`store.py:1204-1250`). `tap_dot` gains a `settings` argument, from which it takes `sha256()` and the bands. Callers: `aset/web.py:1366`, `radar/evaluate_cli.py:412`.
- `create` / `refresh`: inside `write_receipt`'s transaction (`store.py:1082-1102`). The stage collects each card's written numbers and passes them with the receipt row. `refresh_radar_card` returns what it actually wrote, the locked or the fresh numbers (closing G3). `create_radar_card` already returns the id. A run that fails before its receipt writes no records. The card row then holds numbers that no record carries, and replay says so (§5 ROW line). G5 in the card row is named here, not fixed (Open point 3).

**G4 (priced, recommended in the same migration):** `aset_sizings.last_price_at TIMESTAMPTZ`, written with `last_price` from `ev.last_bar_ts` (`evaluate.py:622`) inside the same `COALESCE` pair (`store.py:1040`, `:1049`). Cost: one column, two SQL edits, one test. Replay does not need it, because the receipt holds the bars. It closes C3's ESCALATE 3 at the source. Wiring legs' `price_asof` to the new column is S3 code and stays S3's follow-up.

Volume: one `refresh` record per open card per scan, a few kB each (the per-card `output.dots` dominates). Bars stay in the receipt.

## 4. THE L57 GAPS — cost and what replay prints

| Gap | Closed by | Cost | A card graded before F15 lands |
|---|---|---|---|
| G1 tap result | `tap` record `output` | in P1 | tap events: `NOT REPLAYABLE — graded before F15: a tap's result and settings were not stored (L57)` |
| G2 tap settings | `tap` record `inputs.bands/enabled` + `settings_sha256` | in P1 | same line |
| G3 taps-moved | `refresh` record `inputs.locked` + the written numbers | in P1 | scan events replay via the receipt; a taps-moved scan shows `DIFF card_score` against the receipt's `published` — the truth, not a defect of replay |
| G4 `last_price` bar time | `last_price_at` column | +1 column in P1 (Open point 4) | `last_price_at: not stored (before F15)` |
| G5 card before receipt | records written with the receipt | in P1 for records; the row-level window stays | `ROW: holds numbers no record stores` |

For a card graded before F15 lands, replay prints `NO PREDICTION RECORDS — graded before F15 lands` and the `cobalt radar audit-export --run <run>` line for the run of its `radar_score_id`, then exits 2. Its scan grades remain auditable that way. No backfill (Owner item 1).

## 5. `replay(card_id)`

**Command:** `cobalt cards replay <card_id> [--json]`, in the existing `cobalt cards` family (`cards/cli.py:190-245`). It reads only: stored records, receipts and taps. It fetches no market data, reads no current settings and writes nothing.

**Replay runs against the RECORDED scorer.** Replay is proven through `replay_receipt`, which refuses a receipt of another `EVALUATOR_VERSION` (`evaluate.py:1616-1622`). Today's code therefore recomputes a record only when its version equals the recorded `scorer_version`. A replay has to show that stored inputs reproduce the stored grade. Re-grading with today's formula answers a different question, a what-if for the curve tribunal (Open point 2).
- `formula_sha256` differs but the version is equal: replay runs and prints `NOTE formula source changed since record #k; replayed with current code`. This is the audit-export rule (`audit_export.py:296-298`).
- Version differs: `#k NOT REPLAYABLE — recorded scorer s…, this code s…; replay from the deploy that wrote it`.

**Per record:**
- `create` / `refresh`: load the chain (`receipt_for_run` → `receipts_chain`, `store.py:1114-1135`), verify it, `replay_receipt`, and take the card's `recomputed`. When `taps_moved` is true, apply `card_score(inputs.locked.conviction, recomputed.proximity, …)` exactly as the store did (`store.py:1037-1038`). Diff against `output`.
- `tap`: `overlay` the locked dots → `conviction` → `suppression` (or the kept sentence while proximity is NULL, `store.py:1235-1239`) → `card_score` → `proposed_key(conv, bands, enabled)`. Pure functions from `scoring.py`. Diff against `output`.

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
(The illustrative numbers are constructed, not his.) `--json` emits the same rows for a checker house (L52 d).

- **Decision grade:** the last record before the card's first transition out of WATCH. From ARMED on the key is frozen (`cards/models.py:122-126`), which makes this record the prediction. For a card that never left WATCH, it is the last record before its terminal transition. It is derived from `card_transitions` and never stored.
- **Exit codes:** `0` every record MATCH and ROW matches · `1` any DIFF · `2` nothing differs but something is NOT REPLAYABLE (this includes a card with no records, and a manual card) · a usage error exits via argparse. The S3 smoke passes on `0`.

## 6. THE JOIN TO OUTCOME

**When an outcome is final:**
- CLOSED with every current leg `confirmed`: final. CLOSED with any leg `estimated`: provisional, the same rule as `realized_r` (`legs.py:689`).
- EXPIRED / PASSED / MISSED / not-filled: final once the nightly replay has written the card's `missed` row (`is_current`, kind `card`) or has run for that date and written none. Before that it is `awaiting nightly replay`.
- FILLED and non-terminal: `open`.

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

- **Numbering:** `cobalt_dev` is at `0013` (`cto-2026-09-28.md:191`, R182). The branches take 0016, 0018–0020 (DRC) and 0021 (S3). **F15 takes 0022.**
- **Landing order:** DRC and S3 land first, and F15 lands on or after them in the same stacked deploy (L68 integrated gate on the combined tree; L43, one window).
- **No `EVALUATOR_VERSION` bump:** F15 changes no number and does not change the receipt shape. The bytes of `evaluate.py` change, so `formula_sha256` changes, which the NOTE line covers.
- **Swing / options:** records key on `scorer_id` + `scorer_version`. A scan record references its run's receipt, whatever bars that receipt holds, and a tap record is self-contained. No i1 or intraday assumption is baked into the table.
- **Shared seam (L72):** P2 reads the record shape P1 writes. The FINAL's §3 table and the Pydantic `PredictionRecord` model are the settled seam both prompts cite, so P1 and P2 build in parallel.
- **RESTARTS (L42):** changes to `cards/*`, `radar/evaluate.py` and `aset/web.py` restart `com.cobalt.radar` (in the 20:00–21:00 pause, L43) and `com.cobalt.aset`. `cobalt jobs restarts <range>` gives the table.

## 9. CHUNKS

| Chunk | Content | Size | Builder (L29) | Migration | `cobalt_dev` (L76) |
|---|---|---|---|---|---|
| **P1 — the record** | `0022` + rollback; `cards/predictions.py` (Pydantic `RecordInputs`/`PredictionRecord`, the ONE writer); `scoring.grade_why`; hooks in `tap_dot` (+`settings`), `refresh_radar_card` (returns what it wrote), `write_receipt` (+records, one transaction), the stage's collection in `_evaluate`; `last_price_at` (if Open point 4 holds); `placement.py` DECLARED → CREATED; callers `aset/web.py:1366`, `evaluate_cli.py:412` | M | write path + migration → Opus 5 floor (Anthropic) or Sol (OpenAI), never auto mode on the write path | yes | with-DB suite under the lock, migration applied only inside the suite's rollback |
| **P2 — replay + corpus** | `cobalt cards replay`, `cobalt cards corpus`, `predictions.corpus()`; pure reads; tree carries `s3/exits-c4` | S–M | reads only → any house at the implementation floor | no | with-DB read tests under the lock |

**Tests (both chunks):**
- Real-shape receipt fixtures, the ones `tests/cobalt/test_radar_cards_db.py:97-132` already builds (L45). Settings are constructed values, and a test reads `trader_settings` only for an invariant (L69).
- **P1:**
  - one record per create, refresh and tap;
  - UPDATE and DELETE refused;
  - taps-moved stores the locked numbers;
  - a failed receipt writes no record;
  - a tap without `settings` is refused;
  - tenancy placement test;
  - rollback leaves no table.
- **P2:**
  - MATCH on a create → tap → refresh → fill → exit → CLOSED card;
  - a tampered `output` → DIFF, exit 1;
  - a record at another version → NOT REPLAYABLE, exit 2;
  - a pre-F15 card → exit 2 with the audit-export line;
  - a manual card → exit 2;
  - the ROW line;
  - corpus n per status;
  - `awaiting nightly replay` until `missed` exists.
- **Gate:** each chunk runs offline, with-DB and live-note (L68 GATE EARLY). Checks seat Fable (Opus 5.5) · Astra · Grok for the first check of a new build; later checks seat Opus · Sol · Grok (L67).

**Evenings from "tribunal ruled" to "the S3 smoke's replay line can pass": 2.**
- Evening 1: P1 and P2 build in parallel worktrees.
- Next day: three-house checks.
- Evening 2: one deploy carrying S3, DRC and F15 under the stacked gate (L43, L68, L66).
- The next trading morning: the smoke.

Against S3's stop on 10-07: if the tribunal rules by 10-01, the smoke can run 10-05 or 10-06. The binding risk is the single `cobalt_dev` lock (L76), which S3's and DRC's with-DB reruns also hold.

---

## L52 (a)–(d)

F15 changes no ranking. It adds no number, factor or order. `card_score` stays the one authority. L52 still binds because F15 touches what reaches the card: it hooks the card's score writers and adds a replay of the scorer.
- **(a)** Every recorded number traces to stored inputs: a scan record points to its receipt, and a tap record holds its dots, proximity, bands and enabled keys. A number whose inputs are missing is printed NOT REPLAYABLE with the reason, never defaulted (L1).
- **(b)** There is exactly one ranking authority, `card_score` (`scoring.py:1-2`). Records observe it and never feed it (L7).
- **(c)** The seam is specified as real artifacts: the `0022` DDL, the `PredictionRecord` / `RecordInputs` Pydantic models, the writer's signature in `cards/predictions.py`, the `write_receipt(row, records)` signature and the replay output and exit codes of §5.
- **(d)** Another house can audit it without Cobalt's word: `cobalt cards replay --json` and the unchanged `audit-export --run` recompute from DB rows alone.

## What this does NOT do

- It does not record S7–S11, sizing, or "R had Cobalt's stop held".
- It does not backfill cards graded before F15 lands.
- It does not re-run old scorer versions (no worktree checkout of old code).
- It does not re-grade with today's formula.
- It adds no card chip, DRC cell, EV or aggregate grade.
- It does not fix G5's row-level window (the card row committed before the receipt). It does not wire legs' `price_asof` to `last_price_at`.
- It does not change `EVALUATOR_VERSION`, the receipt shape, any curve, or any of his settings.

## Open to the tribunal

1. **One new table vs widening `card_dot_taps` and reusing receipts.** Rejected alternative: a tap row gains output and settings columns, scan grades are read from receipts by searching `tap_versions.cards` for the card id, and no new table is added. It is smaller by one table. It was rejected for three reasons: the corpus would join two sources, G3's locked numbers would have no home, and the JSON search needs a GIN index over a growing table.
2. **Replay against the recorded scorer only.** Rejected alternative: recompute with CURRENT code across versions and diff. That measures formula drift, not replay. It belongs to the curve tribunal as a separate `--as-current` flag, if wanted.
3. **Leave G5's row window open.** Rejected alternative: write the receipt before the card rows. The receipt lists card ids that are created in the same pass, so the ordering is circular. Breaking the cycle means restructuring the stage beyond F15's size. Replay's ROW line exposes the window instead.
4. **`last_price_at` inside F15's migration.** Rejected alternative: leave it to an S3 follow-up. Replay does not need it, but it is the same migration and the same writer lines, and C3's ESCALATE 3 stays open until someone adds it.
5. **No "replayable" chip on the card.** Rejected alternative: a chip on the panel. It is one more render in `radar_panel.py`, which C3 is still changing, and the CLI already answers the smoke.
6. **A `refresh` record every scan.** Rejected alternative: record only when the output changes. Proximity moves with nearly every price, so deduplication saves little and adds a compare-with-previous query to the write path.

## Owner items

1. **Cards graded before F15 lands stay partly unreplayable (his law L57).** Their tap grades have no stored result or settings. ASSUMED default: accept, with replay printing NOT REPLAYABLE and no backfill.
2. **The corpus is his data (L32): retention.** Every tap record copies the values of his `card.proposed_key` bands and today's enabled keys into a USER-side row. ASSUMED default: keep indefinitely, USER side only, never pruned, never shipped.
