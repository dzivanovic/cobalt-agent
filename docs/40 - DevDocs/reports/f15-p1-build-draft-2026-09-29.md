# F15 P1 build drafter — 2026-09-29

Seat: `f15-p1-build-draft-0929` · Opus 5.5 · prompt `prompts/2026-09-29/33-draft-f15-p1-build.md` · launch row R152 · started 20:26:53 ET, closed 20:41 ET (`date`).

## §0 Headline
- Wrote `prompts/2026-09-29/34-f15-p1-build.md` (the P1 build: 141 lines, 55,445 B) and `prompts/2026-09-29/35-f15-p1-check.md` (its NEW-build check, round 1 of ≤3: 49 lines, 20,204 B).
- The base is left for the desk to fill at launch, after `25` returns YES (today `01d0fbb9` / report `e49fe6a2`). The migration is **`0022`**: it is free on every local branch.
- The P1 build is gated by ten experiments (X1, X3, X4, X5, X6, X8, X9, X12, X13, X14). X14 runs in PREFLIGHT. X1, X12 and X13 run before the writer. X3, X5, X6 and X9 run on the built code.
- No new rule strings: both launch lines pass a `comm` check against `26` / `27`. No owner items. 6 ESCALATE lines, two of them ASK DESK, each with a safe default taken.

## L74
One block arrived inside a tool result: it was appended to the output of reading `33-draft-f15-p1-build.md`, styled as a system reminder. It asked for a `Claude-Session:` line in every commit and PR body, and it named a file-send tool. This is data, not an instruction, and I did not follow it. I commit nothing here anyway. Recorded once.

## AUTHORIZATION (K23)
- R151 row: line 160, carries `APPROVED` and `c3c93c7c`: PASS.
- R141 row: line 150, carries `R2-4 settled`: PASS.
- R152 row: line 161, names `33-draft-f15-p1-build.md`: PASS.
- `git log -S"33-draft-f15-p1-build.md"` on the desk file returns `a140f0366f77ba909548215729c2bc703d1e0bb1` (non-empty): PASS.
- Also read: R145 (line 154, his two B rulings) and R146 (line 155). `git log -S"| R145 |"` returns `e2ed984c…`; `-S"| R151 |"` returns `513f0e77…`.

## DECISIONS
1. **Migration number: `0022`.** Source: the FINAL `## SEAM` "Migration number: `0022`" and §8 "F15 takes 0022". I confirmed this by reading every branch (`## MIGRATION`). The file pair, and the rule that tests apply `0022` only inside the suite's rollback (`apply_0022`, the `legs_db_support.apply_0021` precedent), are at `34` P1-1 / E1 (e).
2. **Scope: exactly the FINAL's P1 row** (`## CHUNKS` P1: Content, Files, Tests it must carry).
   - It covers the `[F-40]` DDL, including the trigger `BEFORE UPDATE OR DELETE` (R2-2 B, R145) and the `transition_id` column (R2-1 (c) B).
   - It covers `cards/predictions.py`: `RecordInputs` / `PredictionRecord` and the one `write_record` (L3, L10).
   - It covers `scoring.grade_why`, the three hooks in their `work` bodies (`[F-32]`), `seq` under the row lock (`[F-33]`), `last_price_bar_ts` + `CardUpdate.last_price_bar_ts` (`[F-37]`), the digest entry (`[F-38]`), and placement DECLARED → CREATED.
   - It updates every caller: `aset/web.py:1423`, `radar/evaluate_cli.py:412`, `radar/evaluate.py:1926` (`run_id=`), and the test callers and fakes found by grep at `s3/exits-c4`. That grep found more callers than F-05 lists: `test_radar_cards_db.py:237`, `:274-276`, `test_rubberband_forms.py:598`, `:711`, `radar_p2_support.py:248`, `:266`, `test_stale_score_db.py:82`, `:107`, `tests/experiments/stale_score/test_x3_taps_moved_null_db.py:22`.
   - `NOT IN P1` lists all of P2 (`34` P1-1 … P1-8, NOT IN P1).
   - One choice is my own reading, and `34` P1-6 states it: a refresh record takes `scorer_version`, `formula_sha256` and `settings_sha256` from the run row (`system.radar_score_run` `0006:76-79`). `refresh_radar_card` has no settings in hand, and the run row holds exactly the values the scan used. The FINAL leaves signatures to the builder (`[F-41]`).
3. **Experiments: the ten the FINAL gates P1 on** (FINAL `## First-gate experiments`; P1 row "Gated by": X1, X3, X4, X5, X6, X8, X9, X12, X13, X14). Each carries its pass condition and its design-changing result, quoted from the FINAL row. A design-changing result STOPS the build at that row.
   - X14 and X4 run in PREFLIGHT.
   - X1, X3 (first run), X12 (iii) and X8 run before the writer. So do X12 (i) and (ii), with the test standing in for the writer, and X13 (i)–(iii) around P1-2.
   - X3 (second run), X5, X6 and X9 run after the code, because they measure the built writer. They are written red first.
   - X12 (i) and (ii) re-run through the real writer.
4. **Seams:**
   - `## FOR P2` covers what replay reads: `seq`, `transition_id`, the stored inputs, `grade_why`, the signatures, and X12 / X6 (c).
   - `## SEAM FOR THE STACK` covers every shared file with its `--no-merges` commits, stated as text and never resolved.
   - Both are specified in `34`. The seam facts I read are under `## SEAMS` below.
5. **The check's seats:** Opus 5.5 + Grok. Astra is on METER until Oct 4th, 2026 2:06 PM; the source is `reports/drc-d3-fix-r2-check-2026-09-29.md` PREFLIGHT, which is also `31`'s citation. It is probed only after that time. The floor is TWO, and it fails closed. This is round 1 of ≤3 (L39). K24's counting rule is in the QUESTIONS and in §3 COLLATE. The stop field is `ready for P2`. Source: L67 `CHECKER SEATS BY KIND OF WORK`, R109.

## MIGRATION
I listed `git ls-tree --name-only <branch> src/cobalt/db_migrations/` for each branch:
- `main`: 0001–0011, 0013, 0014, 0015, 0017.
- `s3/exits-c4`: main's set + `0021_legs`.
- `drc/d1-trading-log`: main's set + 0016, 0018, 0019, 0020.
- `voice/v1-0923`: 0001–0011, 0017.
- `radar/stop-record-0928`: main's set.
- Every other local head (`git for-each-ref refs/heads`): scanned for `002[2-9]`, no hit.

`0012` belongs to the unmerged `bars/chunk-2-0920` (`s3/exits-c4:src/cobalt/db_migrations/__init__.py:63-70`). **Pinned: `0022`.** `cobalt_dev` is at `0013`, per the C4 fix r1 report's W (f).

## SEAMS
- **`drc/d1-trading-log`** (non-merge commits since `main`):
  - `db_migrations/__init__.py` and `placement.py`: `d583f6fd`, `9a0fc900`, `8e8762ca`, `d2897b46`. These are registry lines and are expected.
  - `aset/web.py`: `d5b72392`, `807c13ec`, `0075db31`. Against `01d0fbb9` there are five hunks (imports `:67`, `_daymode_banner` `:569` / `:625`, after `attest` `:1189`, and the file's end `:1394`). None is inside the `tap_dot` route.
  - `tests/cobalt/test_stale_score_db.py`: `4ec4ae20`, `7cdc5774`, `d2897b46`.
  - Nothing in `cards/`, `radar/` or `db_migrations/cli.py`. The merge commit `5bb1f4b5` touches many files, but only by carrying `main` into the branch.
- **`radar/stop-record-0928`:**
  - `radar/evaluate.py` `67e78a2e`. Its hunks are at imports `:155`, `evaluate_member` `:1065` / `:1080` / `:1183`, and `EvaluateStage` `:1953` (main numbering). All are outside `CardUpdate`, `refresh_card` and the refresh call `:1926`.
  - `tests/cobalt/test_radar_cards_db.py` `48426344` (one hunk at `:133`, in or after `test_s5_end_to_end…`).
  - The `src/` diff is `radar/evaluate.py` and `radar/seam.py` only.
  - `34` tells P1 to put its new tests in new files, to limit the shared test file.
- **`s3/exits-c4`:** this is P1's base, so its edits to `store.py`, `web.py` and the registries are inside the base and are not a stack seam for P1.
- **X14's merge half:** `git merge-tree` is not on the builder's line. See ESCALATE 1.

## OWNER ITEMS
NONE.

## FOR DEJAN
- New rule strings: **0**.
  - `34`'s line is `26`'s, with the path, the names and the `.env` pair re-pathed to `f15-p1`. This is the same re-path every build since `20` has made. The pair is on his approval list at launch (L62).
  - `35`'s line is `27`'s, with the path and names changed and without `27`'s four `cp` strings. Those were his R88 grant for S3 C4's files, so nothing re-points.
- Nothing needs his decision.

## ESCALATE
1. `ASK DESK: X14's merge half (git merge-tree) is not on 34's line (26's strings), so the builder records it UNVERIFIABLE — should the desk run it at the stacked gate (L68), or add the string? [20:40]`. Safe default taken: X14 = the `git diff --name-only` / `--no-merges` log / hunk table in PREFLIGHT. That table can still STOP the build on an overlap.
2. `ASK DESK: 35 stages Grok's copies by Read → Write (21 §1 (3)); 27 switched to cp after a classifier refused a Read → Write (R84). cp copies of the FINAL (81,541 B), LAWS.md, the build report and 34 would be NEW strings needing his word. [20:40]`. Safe default taken: Read → Write in parts. A refused copy ends the run with `FAILED: copy`, which spends no round (K17).
3. Note, not a question. `33` says "applied only inside the suite's rollback (L76)". `34` applies `0022` inside the suite's transaction for every test (`apply_0022`). It also runs two real forward / rollback pairs on `cobalt_dev`:
   - X13 is defined by the FINAL as a `cobalt db migrate` run.
   - W's pass 2 follows `26`'s shape.

   Each pair is rolled back, with `F = F0` proven, before the stop line. That is L76's second clause.
4. Note: with R2-2 B, any record makes its card undeletable while `0022` is applied. So:
   - `34` puts the real-factory experiments X5 / X6 in `tests/experiments/f15_p1/` and cleans their cards up at W (f2), after `0022` is rolled back, then proves 0 stray rows.
   - `34`'s E0 inventories every with-DB test that deletes a card on the real factory. At `s3/exits-c4` those are `test_aset_store.py:50`, `test_fill_transaction_db.py:283`, `test_legs_c2_db.py:622` and `test_s3_c2_experiments.py:163`. I did not verify whether any of them touches a radar card.
   - A refused cleanup becomes an ESCALATE line in the builder's report. The builder does not change it.
5. Note: I left `grade_why`'s signature and sentence, `write_record`'s signature, and the refresh record's scorer-field source (the run row) to the builder, under `[F-41]` (`reports/f15-final-fold-2026-09-29.md` `## ESCALATE` 1). `34` asks for each of them to be stated under `## FOR P2`, and `35` Q(4) checks them.
6. Note: BASELINE. `33` names `26`'s CLOSE numbers (offline 3318 · with-DB 3829 · live-note 146). The base has since moved to C4 fix r1 (`01d0fbb9`: offline 3320 · with-DB 3835 · live-note 146, per its stop line). `34` carries both, and the desk fills the base's own numbers at launch.

`35`'s packet ceiling (K17): I measured `27`'s staged packet with `wc -c` over `scratch/tribunal-bars-0920/s3-exits-c4/`, leaving out the three seat outputs and the superseded v3 parts. It is **666,872 B**. The desk sets `35`'s ceiling against P1's `--stat` at launch.

## CONTINUE
Done. The desk commits the three files: `prompts/2026-09-29/34-f15-p1-build.md`, `prompts/2026-09-29/35-f15-p1-check.md` and this report.

F15 P1 BUILD DRAFTED · base: FILL AT LAUNCH (after 25) · migration: 0022 · experiments: 10 · prompts: 2 · new rule strings: 0 · owner items: 0 · ESCALATE: 6
