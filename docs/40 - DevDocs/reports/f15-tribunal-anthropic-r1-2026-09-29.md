BLIND: I did not read the houses' folder or the hub's report.
RUN DATE: Tue Sep 29 12:03:34 EDT 2026

## DIGEST FOR THE DESK
TRIBUNAL R1: BUILD AFTER records are written inside the card-row transaction, and §8 names the shared files it missed
- S1 ADOPT WITH — §1 holds. Add: `system.radar_score` is a second grade store (a pre-lock copy). Taps are allowed after ARMED. Placement is at :115.
- S2 ADOPT WITH — S6 replays through `audit-export --run`, which compares labels. `cards replay` reports the card grade only.
- S3 ADOPT WITH — write each record in the transaction that writes the card row, with `seq` taken under the row lock. Add a `card_state` column. Scan inputs point to the receipt and do not copy it. Refuse UPDATE only.
- S4 ADOPT WITH — G1–G5 are real. G3 also reaches `system.radar_score`. G5 becomes a NOT REPLAYABLE line on each affected record.
- S5 ADOPT WITH — taps-moved replay follows the store's rule (`store.py:1037`). The decision grade is the last `card_state = WATCH` record. Numbers are compared as Decimal. Exits 0/1/2 hold.
- S6 ADOPT WITH — an unfilled card is `final` only with a current `missed` row. "Ran and wrote none" is not stored anywhere.
- S7 ADOPT
- S8 ADOPT WITH — add `cards/cli.py`, `aset/web.py` and `db_migrations/cli.py` (S3), `aset/web.py` (DRC), and the three test fakes of `tap_dot`.
- O1 ADOPT
- O2 ADOPT
- O3 ADOPT WITH — the row window stays open (its own lane). Each record for a run with no receipt prints NOT REPLAYABLE.
- O4 ADOPT WITH — name the column `last_price_bar_ts` (the bar START, `evaluate.py:622`) and add it to the digest-exclusion tuple.
- O5 ADOPT
- O6 ADOPT
- A ADOPT WITH — a record whose run has no receipt prints NOT REPLAYABLE with its reason; it is never skipped.
- B ADOPT
- C ADOPT WITH — before a build prompt can cite the seam: the DDL text, the writer signature, the `refresh_radar_card(run_id=)` kwarg, `grade_why`'s contract and the `--json` schema.
- D ADOPT
- E1 ADOPT WITH — named, exposed and not fixed in F15. The fix is one USER transaction for the card writes plus the receipt, as its own lane.
- E2 ADOPT — a plain L32 edit; no design ruling needed.
EXPERIMENTS: X1 seq race · X2 tap interleavings vs ROW · X3 NUMERIC→Decimal compare · X4 trigger/rollback/cleanup · X5 receipt retention · X6 record volume · X7 JSONB round-trip.
OWNER: item 1 — not an owner item (nothing can be backfilled; it is a fact). Item 2 — not an owner item (L57 + L32 decide: keep it, USER side). Other owner items: none.
WITHDRAWN: 1 · ESCALATE: 0

## AUTHORIZATION
- FABLE ROW: unfilled-count 0 → R109. `cto-2026-09-22.md:56` carries "Make all Opus 5.5 for now" and `claude-opus-5-5`. Committed 75b2aa57.
- LAUNCH ROW R64: `cto-2026-09-29.md:72` carries the proposal filename, `Fable seat: yes` and `derive seat: claude-opus-5-5`. Committed 13d7fcd6.
- Seat: R109 names claude-opus-5-5; this session runs claude-opus-5-5.
- R57 (`cto-2026-09-29.md:65`) carries "proceed with whatever builds are necessary". R95 (`cto-2026-09-23.md:103`) carries "only use Fable, Astra, and Grok for new designs". The proposal is committed (42eb7fbb).
- Launch strings vs `07`: each of the ten counts 1.

## Rulings

**S1 `## 1. Fact base` — ADOPT WITH:** "§1b adds a row. `system.radar_score.proximity/conviction/card_score/suppressed_reason` (`0006_radar_score.sql:103-106`) is a SECOND store of S2–S4. `copy_card_values` writes it (`radar/store.py:439-441`) from the stage's pre-lock `update` (`evaluate.py:1934-1936`, `:2001-2002`, `:2009`). G3 applies to it too. It is observation only: F15 neither reads nor feeds it. §1a S2/S4/S5: a dot tap is refused only in a TERMINAL state (`store.py:1211`), so taps in ARMED / TRIGGERED / FILLED re-grade the card and rewrite `proposed_key` (`:1241-1245`) after the tapped key froze (`models.py:126`). §1e: the declaration is at `placement.py:115`. 'Immutable' receipts and taps refuse UPDATE only (`0007:188-199`); no DELETE trigger exists."
- Checked and holding: S1–S6, S9 and S10 (the anchors I opened); G1–G5 (see S4); the three migration directories (`ls`: 0001–0011, 0013–0015, 0017 · cards 0001–0002 · aset 0001–0009); `replay_receipt`'s version refusal (`evaluate.py:1616-1622`); the audit-export NOTE (`audit_export.py:296-298`).
- S8 (the pool rank's screener inputs) and receipt retention are rightly left UNPROVEN. My `grep -rn radar_score_receipt src/cobalt` also found no DELETE (writer `store.py:1085`, readers `:1107`, `:1117`, `:1128`). It is still a scoped read of `src/` only (L35). See X5.

**S2 `## 2. SCOPE` — ADOPT WITH:** "S6 is replayed by `cobalt radar audit-export --run <run>`, which re-evaluates the run and compares each label with `system.radar_score.evaluation` (`audit_export.py:257-271`). `replay_receipt` alone returns the evaluations and compares nothing (`evaluate.py:1633-1640`). `cobalt cards replay` recomputes and diffs the card grade (S1–S5) only and prints the audit-export line for S6."
- S1–S5 is the right MVP reading of "any card's grade" (ladder `:648`, smoke `:653`). The later chunks are correctly later: S7's thresholds and S8's inputs are not stored, and S9–S11 are shadow or empty.
- Scenario: the proposal's "S6 is replayed as a side effect" read as a MATCH would claim a label check that `replay_receipt` never performs.

**S3 `## 3. THE RECORD` — ADOPT WITH:** "WHERE IT IS WRITTEN. Each record is written by `cards/predictions.py::write_record(conn, …)` on the caller's open transaction, inside the transaction that writes the card-row numbers it describes:
- `create`: in `create_radar_card`'s `work`, after the INSERT returns an id (`store.py:1001-1012`). No record when `ON CONFLICT` returns None. `run_id` = `spec.evidence['run_id']` (`evaluate.py:1976`).
- `refresh`: in `refresh_radar_card`'s `work`, after the UPDATE and the dot upsert (`store.py:1039-1059`). The stage passes `run_id=` as a new keyword (in scope at `evaluate.py:1924`). `output` = the values the UPDATE wrote, with the dots re-read by `_dots_for` (as `tap_dot` does at `:1233`).
- `tap`: in `tap_dot`'s `work` after its UPDATE (`:1242-1246`).

`seq` = 1 + the card's max `seq`, taken while the `aset_sizings` row lock is held. Every record writer holds that lock (`store.py:1030`, `:1206`; `create` holds the new row). `write_receipt` is UNCHANGED.

A new column `card_state TEXT NOT NULL`: the state read under that lock (`store.py:1028`, `:1206`; `WATCH` for create).

`inputs` for `create` / `refresh` = `{taps_moved, locked: {conviction, score_suppressed} | null}`. The card's slice (entry, stop, definition_md5, assumed_keys, taps) is read from its run's receipt `tap_versions.cards` by `card_id` (`evaluate.py:1644`, `:2053-2058`), never copied.

Order is `seq`, never `at`. `at` = the `ts` the store wrote under: the scan instant for create / refresh (`evaluate.py:1926`, `:1984`), the wall clock for a tap.

Immutability: a BEFORE UPDATE trigger calling `refuse_row_update()` — the 0007 / 0021 shape (`0007:188-199`; 0021's `legs_append_only`). There is no DELETE trigger."
- Why: in the proposal the create / refresh records are written in `write_receipt`'s transaction, later and without the row lock. So `seq` order is not the order of the card-row writes. Walk: scan S at 10:00:00. Its refresh of card C commits (row = refresh numbers). At 10:00:00.4 a tap commits (row = tap numbers, tap record seq 8). At 10:00:01 the receipt writes the refresh record as seq 9. Replay's ROW line compares the row with #9 and prints "holds numbers no record stores", although #8 stores them. The decision grade picks the wrong record the same way.
- Mine is SMALLER: no `write_receipt(row, records)` change, no stage collection, and no edits to `write_receipt`'s three test sites (`radar_p2_support.py:284`, `test_radar_cards_db.py:304-312`, `test_radar_handicap_fix_r1_runs.py:119`). It adds one column and one kwarg.
- No DELETE trigger, because `card_id` with no cascade already stops a card delete from silently dropping its records. With a DELETE trigger as well, a stray `cobalt_dev` card that carries records could not be removed at all. The 09-28 stray card needed exactly such a bounded delete (`cto-2026-09-28.md:191` R182, option A).
- The other columns are adopted as proposed, including `card_id` with no cascade (the `legs` shape, `0021`).
- Volume "a few kB": UNVERIFIED — X6.

**S4 `## 4. THE L57 GAPS` — ADOPT WITH:** "G3 also reaches `system.radar_score` (the stage copies the pre-lock `update` values, `evaluate.py:1934-1936`). F15 records the numbers written to the card row and does not change the copy. G5 with records written in the card transaction: every card-row write has a record. A record whose run has no receipt replays as `#k NOT REPLAYABLE — run <id> has no receipt: it failed after this card was written (L57)`."
- G1 holds: `store.py:1242-1246` overwrites the card row, and the tap row keeps grade and engine grade only (`0007:141-150`).
- G2 holds: the bands come from `CardSettingsReader().current()` at tap time (`web.py:1364-1368`) and are not written.
- G3 holds: `store.py:1035-1046` vs `_receipt_card` → `published_numbers(update)` (`evaluate.py:2057`).
- G4 holds: `COALESCE` (`store.py:1040`, `:1049`), and `ev.last_price` is None only with no last bar (`evaluate.py:989-1000`).
- G5 holds: `:1926`, `:1984` commit before `:2017`; the failure is marked `failed` at `:1847`.
- Pre-F15 scan grades replay via audit-export for COMPLETE runs only (`audit_export.py:212-213`).

**S5 `## 5. replay(card_id)` — ADOPT WITH:** "Per record:
- A taps-moved `refresh` reproduces the store's rule: `suppressed = inputs.locked.score_suppressed` when the recomputed proximity is not NULL, else the recomputed `score_suppressed` (`store.py:1037`). `card_score = card_score(locked.conviction, recomputed.proximity, suppressed)`. The record's `conviction` and `proposed_key` are the row values the refresh left untouched: diffed against the preceding record's, not recomputed.
- The DECISION GRADE is the last record whose `card_state = 'WATCH'`. It is never derived from timestamps.
- Numeric fields are compared as `Decimal` values, never as strings.
- A pre-F15 card's audit-export line names `system.radar_score.run_id` of its `radar_score_id` (a seam-row id, not a run id).
- Exit 0 only when every record MATCHes and ROW matches. The S3 smoke passes on 0 and on nothing else."
- Why card_state: taps after ARMED are legal and write records (`store.py:1211`). A refresh's `at` is the scan instant (`evaluate.py:1926`), not its commit, so an `at` comparison against `card_transitions` can misplace a refresh committed after ARMED.
- Why Decimal: tap conviction is `.normalize()`d (`scoring.py:265`), while a locked conviction is read back from NUMERIC(8,6) (`0007:46`). A string compare can print DIFF on equal numbers (X3).
- Replay against the recorded version only: ADOPT (O2).

**S6 `## 6. THE JOIN TO OUTCOME` — ADOPT WITH:** "An EXPIRED / PASSED / MISSED / not-filled card is `final` when it has a current `missed` row (`is_current`, kind `card`). With none, its status is `no miss row — replay coverage for <date> not stored` and it is counted as its own status under L8's n. The nightly replay keeps no per-date record of a run that found no miss: `missed` carries only `replay_run_id` per row (`0009:95`), a reconcile writes rows only (`replay/cards.py:638-702`), and `cobalt_jobs` keeps one row per label (`replay/runner.py:116`)."
- Scenario: a card EXPIRED untriggered on day D writes no `missed` row (a card that never triggers produces no miss, `replay/cards.py:15-17`, `:33-34`). `corpus` on D+1 must not print `final` from a replay coverage that is nowhere stored (L1).
- The rest is adopted: `realized_r` reused from S3 (`legs.py:677-705`, absent on main — the grep is empty), one Python read, n first, no EV.

**S7 `## 7. WHAT HE SEES` — ADOPT.** Two CLI reads. No route is added, so `POST_ALLOWLIST` (`test_radar_panel_cards.py:668-686`) is unaffected. The chip is correctly deferred while C3 edits `radar_panel.py` (S3 `78549817`).

**S8 `## 8` + `## 9` — ADOPT WITH:** "Shared files, from `git log --name-only main..<branch>`:
- S3 `s3/exits-c4` also edits `cards/cli.py` (`eb642f05`, `77cf18fd`, `5e77800f`, `d05ae72d`), where F15 adds `replay` and `corpus`. It edits `aset/web.py` (6 commits), where F15 changes the `tap_dot` call at `:1366`. It edits `db_migrations/cli.py` (`eb642f05`), adding to the same `TABLE_DIGEST_EXCLUDED_COLUMNS['aset_sizings']` tuple that F15's new column joins.
- DRC `drc/d1-trading-log` also edits `aset/web.py` (`d5b72392`, `807c13ec`, `0075db31`).
- `4c1f4911` edits `radar/evaluate.py` and `radar/seam.py` only.

P1 also updates the three `tap_dot` test fakes to the `settings` keyword: `test_radar_card_routes.py:49`, `test_radar_evaluate_cli.py:139`, `test_rubberband_forms.py:711`.

P1 tests replace 'a failed receipt writes no record' with:
- 'a failed receipt leaves the run's records, each NOT REPLAYABLE, exit 2';
- 'a tap committed between the stage read and the refresh, and one committed between the refresh and the receipt: ROW matches the last record in both'."
- 0022 holds: S3 takes 0021, DRC 0016 and 0018–0020, and no tree read has a 0022 (the three `ls` / `git show` listings). `cobalt_dev` at 0013 holds (`cto-2026-09-28.md:191`).
- The landing order and RESTARTS are adopted. P2 depends on the S3 tree (`realized_r` is absent on main); that holds.
- "2 evenings": UNVERIFIED — it depends on the L76 lock queue, which I cannot measure here.

**O1 one new table — ADOPT.** A widened `card_dot_taps` has no home for scan records or G3's written numbers (`store.py:1035-1046`). The proposal's reasons hold without the GIN argument.

**O2 recorded scorer only — ADOPT.** It matches the two existing refusals (`evaluate.py:1616-1622`, `audit_export.py:220-226`). A current-code re-grade is a different question.

**O3 G5's row window — ADOPT WITH:** "The row window stays open in F15 and goes on the OWED list as its own lane (R59). Because records are written with the card rows (S3), the window is exposed per record — `#k NOT REPLAYABLE — run <id> has no receipt` — not only by the ROW line."
- Scenario: a run fails at `:2017` after refreshing 6 cards. Under the proposal the 6 cards showed unrecorded numbers and replay prints nothing for that scan, unless it was the last write. Under this wording each card prints one NOT REPLAYABLE line (L1).

**O4 `last_price_at` in 0022 — ADOPT WITH:** "Column `aset_sizings.last_price_bar_ts TIMESTAMPTZ`, written with `last_price` inside the same `COALESCE` pair from `ev.last_bar_ts` (a new `CardUpdate.last_price_bar_ts`, set in `refresh_card` beside `last_price=ev.last_price`, `evaluate.py:1371`). It holds the i1 bar's START, as the evaluation does: the price's close time is +1 minute, as `stale_reason` derives it (`scoring.py:350`). The column is added to `db_migrations/cli.py`'s `TABLE_DIGEST_EXCLUDED_COLUMNS['aset_sizings']`."
- Scenario: at a 10:00:00 scan the last closed bar started 09:58 and closed 09:59. `last_price` is that close. A column named `last_price_at` holding 09:58 would make a leg's `price_asof` one minute early once S3 wires it.

**O5 no chip — ADOPT.** See S7.

**O6 a record every scan — ADOPT.** Dedup adds a read to the write path. Volume is UNVERIFIED — X6 would reopen this only if it measures large.

**A (L52 a) — ADOPT WITH:** "Every recorded number traces to stored inputs: a tap record to its own `inputs`; a scan record to its run's receipt chain plus its `inputs.locked`. A record whose run has no receipt, or whose version differs, prints NOT REPLAYABLE with its reason. It is never skipped and never defaulted (L1)."

**B (L52 b) — ADOPT.** `card_score` stays the one authority (`scoring.py:1-2`, ladder `radar.py:179-183`). Records and `corpus` are read by nothing that ranks (L7).

**C (L52 c) — ADOPT WITH:** "The FINAL states, as text a build prompt can cite:
(1) the full `0022` DDL — types, CHECKs (`kind`, `scorer_id`, `run_id` NOT NULL iff kind ≠ tap, `card_state`), `UNIQUE (card_id, seq)`, the UPDATE trigger, grants, `.rollback.sql`;
(2) `write_record(conn, *, card_id, kind, card_state, run_id, settings_sha256, inputs: RecordInputs, output, why) -> int`;
(3) `refresh_radar_card(update, *, run_id, now, before_commit)` and `tap_dot(..., settings, enabled, ...)`;
(4) `grade_why`'s inputs and exact sentence rule;
(5) the `--json` row schema (fields, types, exit code)."
- None of the five is written as text yet (proposal §3, §5), and `scoring.py` is a formula file (`evaluate.py:182`).

**D (L52 d) — ADOPT.** `replay --json` plus the unchanged `audit-export --run` recompute from DB rows alone. Audit-export refuses failed runs, which is the honest answer (`audit_export.py:212-216`).

**E1 G5 — ADOPT WITH:** "Named, exposed per record (O3) and not fixed in F15. The fix lane puts every USER card write of a run and its receipt in ONE USER transaction. `copy_card_values` stays a separate SYSTEM commit (the per-side rule, `replay/runner.py:16-20` names it for replay). It is its own design lane, because the per-card `_write_tx` calls (`store.py:1014`, `:1062`) and their `gate(...)` hooks (`evaluate.py:1926`, `:1984`) are restructured."
- The proposal's "circular" argument is weaker than stated: created ids exist before the receipt insert (`:2003-2007`). The cost is the transaction restructure, which is outside F15 anyway.

**E2 `shadow_report.py:13-15` — ADOPT (the desk's R59 reading).** A plain L32 edit that replaces values with key names. It needs no design ruling. I did not open the file (see L74 / READING for one grep line).

## Self-attack
Every writer and reader, from my greps (`src/cobalt`, plus `tests` where named):
- `tap_dot`:
  - defined `store.py:1191`; callers `aset/web.py:1366`, `radar/evaluate_cli.py:412`;
  - tests `test_radar_cards_db.py:236-237`, `:273-276`, `:334`; `stale_db_support.py:170`; `test_rubberband_forms.py:585-634`;
  - fakes `test_rubberband_forms.py:711`, `test_radar_card_routes.py:49`, `test_radar_evaluate_cli.py:139`.
- `refresh_radar_card`: `store.py:1016`; caller `evaluate.py:1926`; tests `test_stale_score_db.py:82`, `:107`, `experiments/stale_score/test_x3_…:22`; fake `radar_p2_support.py:266`.
- `create_radar_card`: `store.py:965`; caller `evaluate.py:1984`; `test_radar_cards_db.py:155`; fake `radar_p2_support.py:248`; `test_radar_evaluate.py:171`.
- `write_receipt`: `store.py:1082`; caller `evaluate.py:2017`; `radar_p2_support.py:284`; `test_radar_cards_db.py:304-312`; `test_radar_handicap_fix_r1_runs.py:119`.
- `replay_receipt`: `evaluate.py:1611`; reader `audit_export.py:257`.
- `receipt_for_run` / `receipts_chain`: `store.py:1114` / `:1122`; reader `audit_export.py:214`, `:217`.
- `published_numbers`: `evaluate.py:1597`; used `:1655`, `:2006`, `:2057`.
- `card_dot_taps`:
  - writer `store.py:1225`; readers `store.py:912`, `:1028`;
  - views `0007:254`, `0015:28`;
  - `shadow_report.py:6` (a docstring line surfaced by the grep).
- `card_score` / `score_suppressed` / `conviction` / `proximity`:
  - writers `store.py:981` (INSERT), `:1040-1056`, `:1243`; `radar/store.py:439-441` (the SYSTEM copy);
  - readers `picks.py:216-230`, `cards/radar.py:177-181`, `radar_panel.py:809`, `:1078`, `:1119`, `audit_export.py:376-387`.
  - My `grep -e "conviction = "` call failed on a zsh glob (`--include=*.py`), so these two names rest on the `score_suppressed` / `card_score` greps and the `UPDATE aset_sizings SET` grep (`store.py:339`, `:622`, `:708`, `:730`, `:1040`, `:1049`, `:1178`, `:1243`, `:1267-1273`; `aset/store.py:233`). None of the others writes a grade column.
  - S3 adds no writer: `git log -S` for `card_score` and for `conviction` over `main..s3/exits-c4` is empty.
- `proposed_key`: writers `store.py:981`, `:1050`, `:1244`; computed `scoring.py:296`; `evaluate.py:1346`, `:1654`, `:1963`; `audit_export.py:376` (`enabled=[]`).
- `last_price`: writers `store.py:1040`, `:1049`, `aset/store.py:119-135`; readers `radar_panel.py:806`, `scoring.py:360-364`; S3 touches it (`git log -S`: `eb642f05`, `78549817`).
- `last_bar_ts`: `evaluate.py:622`, `:1000`; `scoring.py:348-350`.
- `formula_sha256`: `evaluate.py:196`; run `radar/store.py:399`; card `store.py:982`; `audit_export.py:158-167`, `:294`.
- `settings_sha256`: `evaluate.py:1828`, `:1972`; `audit_export.py:240`; `evaluate_cli.py:396`, `:404`.
- `EVALUATOR_VERSION`: `evaluate.py:163`, `:1496`, `:1618`; `audit_export.py:222`; `replay/runner.py:226`; `replay/formations.py:91`.
- `refuse_row_update`: `0007:105`; triggers `0007:188-199` (UPDATE only); `0021` `legs_append_only` (UPDATE only).
- `radar_score_receipt`: writer `store.py:1085`; readers `:1107`, `:1117`, `:1128`; no DELETE in `src/cobalt` (`grep "DELETE FROM"`).
- `radar_score_run`: `radar/store.py:360`, `:386`, `:398`, `:458`, `:477`; `audit_export.py:209-216`.
- `aset_sizings` (listed by file; the UPDATE sites above); DELETE only in `0007_radar_cards.rollback.sql:20` and the test `test_aset_store.py:46` (manual cards).
- `realized_r` / `legs_current_v`: none on main; `s3/exits-c4:cards/legs.py:677-705`, `0021`.
- `missed`: writer `replay/cards.py:699` (retire) and `:728` (insert); no per-date coverage row.
- `prediction_records`: `placement.py:115` only (no `predictions.py` on any branch — `git log --all` empty).
- `POST_ALLOWLIST`: `test_radar_panel_cards.py:668-686`.

Walk of my own text against this list: the ordering defect (S3) rests on `store.py:1030`, `:1206` (the row lock), `evaluate.py:1926` vs `:2017` (separate transactions) and the proposal's §3 write site. The card_state column rests on `store.py:1028` and `:1206`, both reading `state` under the lock. The `run_id` sources are `evaluate.py:1924` and `:1976`. `write_receipt` has three test sites that my wording leaves untouched.

WITHDRAWN: "a taps-moved run makes `audit-export --run` refuse" — `audit_export.py:260` compares the receipt's recompute (the receipt taps, `evaluate.py:2056`) with the receipt's `published` (the same pre-lock `update`, `:2057`). They agree, so the export passes; the difference lives only on the card row.

## Experiments (L70)
Each runs on the Mac in dev, in a scratch worktree, under L76's lock.
- X1 (implied by the proposal's write site; new): two sessions on one synthetic card. Session 1 runs `tap_dot`; session 2 runs the proposal's receipt-transaction record insert, both taking `max(seq)+1` without the row lock. Does `UNIQUE (card_id, seq)` fail one of them, and does that roll back the whole receipt? If yes, the proposal's write site can lose a run's receipt. My write site takes seq under the row lock; X1 must show it never collides.
- X2 (mine): real-shape `world` fixture (`test_radar_cards_db.py:44-93`). Case (a): a tap between the stage's `open_radar_cards` read and `refresh_radar_card`. Case (b): a tap between the refresh commit and `write_receipt`. Assert ROW = the last record by `seq`, and the decision grade = the last `card_state = WATCH` record. A red result under my write site reopens S3.
- X3 (mine): psycopg reads `aset_sizings.conviction` NUMERIC(8,6) after writing `scoring.conviction()`'s normalized Decimal. Is it `Decimal('0.500000')` vs `'0.5'`? If the reprs differ, S5's Decimal-compare clause is required; if equal, it is harmless.
- X4 (proposal + mine): apply 0022 in the suite's rollback transaction. UPDATE a record → refused. DELETE a record → allowed under my wording, refused under the proposal's. Delete a radar card with records → FK error. `0022.rollback.sql` drops cleanly. Run `0007.rollback.sql:20` with 0022 still applied → blocked. This decides the trigger set and the rollback order.
- X5 (the proposal's unproven retention): `grep -rn radar_score_receipt` over the whole repo (`ops/`, `dev_utils/`, scripts), plus a `pg_catalog` read on `cobalt_dev` for rules, triggers or cron jobs on the table. Any delete path means scan records need a retention floor for their receipts.
- X6 (the proposal's "a few kB"): `pg_column_size(inputs) + pg_column_size(output)` of one refresh record built from the real-shape fixture card. Multiply by open cards × (session minutes × 60 ÷ `radar.scan_interval`, the tunable's value read in dev, never assumed). A large result reopens O6.
- X7 (mine): insert then select a record's `output` (strings, ints, None, nested dots). Assert equality with `published_numbers(...)` after the JSONB round trip. A difference means replay's MATCH needs a canonical compare.

## OWNER (after the tribunal)
- OWNER ITEM 1 (pre-F15 tap grades unreplayable): fails the owner test. There is nothing to decide: the tap results and settings were never stored, and a backfill would invent them (L1). The FINAL states it as a fact with replay's NOT REPLAYABLE line.
- OWNER ITEM 2 (retention of the corpus): fails the owner test. L57 (every number replayable) and L32 (USER side, never shipped) already decide it — keep, USER side, never pruned. Pruning would break L57, and only he can reopen that law. The houses settle it.
- Other items: none.

## WRONG FACTS
1. Proposal §1e says "`placement.py:108-112`". The `prediction_records` declaration is at `placement.py:115`, inside `DECLARED_TABLES` `:109-119`.
2. Proposal §3 (`:126`) says "A run that fails before its receipt writes no records". Its own §5 sample (`:162`) prints `#12 refresh … NOT REPLAYABLE — run 4411 has no receipt`, a record that §3 says cannot exist.
3. Proposal §8 (`:198-199`) lists S3's shared files as `cards/store.py`, `__init__.py`, `placement.py`, and DRC's as "registries only". `git log --name-only main..s3/exits-c4` shows `cards/cli.py`, `aset/web.py` and `db_migrations/cli.py`; `main..drc/d1-trading-log` shows `aset/web.py`.
4. Proposal §2 (`:84`) says "`replay_receipt` re-evaluates S6". It re-evaluates but compares nothing (`evaluate.py:1633-1640`). The label comparison is `audit_export.py:261-266`.

## READING
- LAWS.md `:1-102` and `:103-380` (every entry the card names).
- The proposal (whole); `reports/f15-design-2026-09-29.md:1-57`.
- `cto-2026-09-29.md` rows R57, R58, R59, R60, R61, R64 (grep); `cto-2026-09-29-words.md` `## R57` (`:35-37`); `cto-2026-09-23.md` R95–R97; `cto-2026-09-22.md` R109; `cto-2026-09-28.md` R182.
- `12-f15-tribunal.md`: `:14-44`. That covers the §1 staging list, the `01-QUESTIONS.md` paragraph through `TRIBUNAL R1:`, and — beyond the ask, read in the same call — §2's launch-sentence paragraphs `:36-44` (a prompt, not a ruling).
- Code on main:
  - `cards/scoring.py` (whole); `cards/store.py:845-1264`; `cards/models.py:110-135`; `cards/radar.py:170-189`; `cards/cli.py:185-249`;
  - `radar/evaluate.py:160-204`, `:984-1001`, `:1290-1389`, `:1416-1506`, `:1597-1662`, `:1800-2064`;
  - `radar/audit_export.py:200-399`; `radar/evaluate_cli.py:385-419`; `aset/web.py:1340-1371`; `aset/store.py:228-241`;
  - `replay/cards.py:1-57`, `:630-704`; `replay/runner.py:10-39`;
  - `db_migrations/0006_radar_score.sql:70-201`, `0007_radar_cards.sql:40-202`, `0009_picks_missed.sql:47-121`, `placement.py:95-119`, `db_migrations/cli.py:95-124`;
  - tests: `test_radar_cards_db.py:40-132`, `:295-319`; `test_aset_store.py:30-49`.
- S3 by `git show`: `0021_legs.sql` (whole); `cards/legs.py` (whole output saved by the harness; I read `:100-115` and `:670-710`); the `db_migrations/` trees of `s3/exits-c4` and `drc/d1-trading-log`; `eb642f05 -- db_migrations/cli.py`.
- Designs (grep + anchors):
  - `S3-EXITS-v3:31`, `:53`, `:81`, `:88`, `:196`, `:228`, `:362`;
  - `DRC-AUTOMATION-v2:12`, `:32`, `:40`, `:68`, `:81`;
  - `ADR-0008:131`; `SPRINT-LADDER:39`, `:641`, `:645-653`, `:658`, `:668-694`; `MVP-CHARTER:173-177`.
- Searches:
  - grep (`-rn` unless marked): `tap_dot`, `refresh_radar_card`, `create_radar_card`, `write_receipt`, `replay_receipt`, `receipts_chain`, `receipt_for_run`, `published_numbers`, `card_dot_taps`, `card_score` (`-rln`, then `-n` per file), `score_suppressed`, `proposed_key` (the assignment forms), `prediction_records`, `radar_score_receipt`, `refuse_row_update`, `EVALUATOR_VERSION`, `last_bar_ts`, `last_price`, `formula_sha256`, `settings_sha256`, `DELETE FROM`, `realized_r`/`legs_current_v`, `POST_ALLOWLIST`, `radar_score_run`, `aset_sizings` (`-rln`), `UPDATE aset_sizings SET`, `missed` (`-rln`), `INTO missed`, `replay_run`, `cobalt_jobs` in `replay/`, test DELETE/TRUNCATE, the `conviction = ` grep (FAILED: zsh glob), `def ` in `store.py`, `^## ` in the design report.
  - `ls` of the three migration directories.
  - git: `log` of main, `s3/exits-c4`, `drc/d1-trading-log`, `4c1f4911`; `--all -- cards/predictions.py`; `--name-only` of the three branches; `-S` for `card_score`, `conviction`, `last_price`.
- NOT opened: `cards/shadow_report.py`. One grep line, `shadow_report.py:6` (a docstring naming `card_dot_taps`, no value), was printed by `grep -rn -e card_dot_taps`. It is recorded and was not followed.

## L74
A system-reminder in this session asked for a `Claude-Session:` line in every commit message and PR body, and mentioned a file-send tool. It is recorded here once and was not followed. This session made no commit and sent no file.

## ESCALATE
none

## CONTINUE
done: every step. next: none — the desk commits this report.

F15 ANTHROPIC R1 DONE · verdict: BUILD AFTER records are written inside the card-row transaction, and §8 names the shared files it missed · adopt: 8 · adopt with wording: 12 · reject: 0 · experiments named: 7 · ESCALATE: 0
