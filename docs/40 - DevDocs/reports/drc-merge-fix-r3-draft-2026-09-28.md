# DRC merge fix r3 — classification and prompts 2026-09-28 — seat `drc-merge-fix-r3-draft-0928`

## §0 Headline
- `33`'s items (1)–(3) → FIX, ONE report-text row R3-1: `## FOR 08` re-issued whole with the complete pin list (a sweep of 10 idioms; 11 files' slot, number, list and table-set pins, each with its value after `0019`) and the rollback contract per file. Item (4) → NOT REAL (the test claims `0015`'s view; the whole-schema no-op is `32`'s `F3 = F2 = F0`). (5)–(6) → round 2's question (i). ESCALATE 8 → RECORD, OWED to the DRC deploy.
- Code change: none. With-DB: no (no lock, no W); `38` runs O, live-note and the pin greps.
- Written: `prompts/2026-09-28/38-drc-merge-fix-r3-build.md` (29,937 B) and `prompts/2026-09-28/39-drc-merge-fix-r3-check.md` (35,355 B; round 2 of ≤3). New rule strings: 0.
- ESCALATE: 3.

## L74
A block arrived appended to the Bash tool result that printed `37-draft-drc-merge-fix-r3.md`. It asked every commit and PR body to carry a `Claude-Session:` line and named a file-send tool. It is data and was not followed. This seat commits nothing.

## Authorization
`grep -n -F "37-draft-drc-merge-fix-r3.md" ".../cto-2026-09-28.md"` → `:88` `| R80 | 14:18 ET | — DESK LAUNCH ROW: \`37-draft-drc-merge-fix-r3.md\` …` `| LAUNCHED |`. Read Mon Sep 28 14:19:15 EDT 2026.

## Classification
Sources: `C` = `reports/drc-merge-fix-r2-check-2026-09-28.md` (real lines); `R2` = `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-fix-r2-build-2026-09-28.md`; `O` = the check packet's `opus-check.md`; `P32` = `prompts/2026-09-28/32-drc-merge-fix-r2-build.md`. Code lines are at `7cdc5774` (`git log --oneline 7cdc5774..drc/d1-trading-log -- src tests configs` empty; branch head `509f19f5` = `32`'s report commit).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | `32`'s `## FOR 08` pin list was built from the `0018_drc_stated_books` name grep and leaves out slot / number pins `0019` breaks: `test_assumed_store.py:245–254`, `test_drc_k1_store.py:117–118`, `test_voice_store.py:57`, `test_archiver_migrations.py:170–172` | `C:176`; walked `C:141` (HOLDS); `O:74–78` | FIX — REPORT TEXT, row R3-1 | P32:145 (the clause asked for "every `FORWARD[-n]` / `REVERSE[n]` / `names[-n:]` / `_rollback_paths` list" — R2:591 delivered a name grep only); L35 | `38` re-issues `## FOR 08` WHOLE with the complete pin list of `## PIN SWEEP` (K16: the list is in `38` verbatim); the build proves each cited line by a grep at its tip. The sweep found more than both checkers: `test_drc_k1_store.py:123`, `test_radar_score_migration.py:116`/`:121`/`:126`, and the with-DB table-set pin `test_archiver_migrations.py:54` + `:495–519`. |
| 2 | `test_drc_store.py:65` / `:67` half-covered: the list names their continuation lines `:66` / `:68` | `C:177`; walked `C:142` (HOLDS) | FIX — REPORT TEXT, in row R3-1 | P32:145; L35 | Same row: each pin cited by its assertion's first line and its continuation range (`:65–66`, `:67–68`). |
| 3 | the rollback contract's parenthetical ("`IF EXISTS`, or `0013`'s / G2's guard") does not describe `0015` (`CREATE OR REPLACE VIEW`, `0015_shadow_agreement_stale.rollback.sql:4`); "every rollback on this tree" but only `0013`–`0018` walked | `C:178`; walked `C:144` (HOLDS), `C:145` (HOLDS of the packet); `O:82` | FIX — REPORT TEXT, in row R3-1 | R2:580 lives inside `## FOR 08` (R2:532–604); P32:141 | Folded into R3-1: the contract re-worded to the files `--down-to 0013` selects, each with its own shape and line, `0015` named idempotent re-create (not an absent-object guard); rollbacks at or below `0011` stated as outside the contract (`C:145` lists their unguarded `ALTER TABLE`s). |
| 4 | `test_stale_score_db.py:180–181` claims "a repeated reverse is a no-op" but `:181` compares only the view | `C:179`; walked `C:147` (HOLDS: `:181` asserts `_viewdef` only) | NOT REAL | L45; L35 | The claim is narrower than read. The test is `test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction` (`:165`): its subject is `0015`'s view; the module docstring `:9–10` binds it to "Migration `0015`". At `:180` the other four files of the selection act on absent objects (`0016`–`0018` tables dropped at `:178`; `0014`'s columns gone): the only statement that can change state is `0015`'s `CREATE OR REPLACE VIEW` (`0015_shadow_agreement_stale.rollback.sql:4`), which `:181` asserts; a raise fails the test (it did — `17`'s red, cleared by G2). The whole-schema no-op is proven on `cobalt_dev` by R2:366–420, `F3 = F2 = F0` (cols · rels · views_md5). Opus itself: "R2 `:420` F3 = F2 covers the claim … No assertion changed by a fix row is weak" (`O:98`). The test is main's, untouched by either fix (`C:147` note). No with-DB run follows from it. |
| 5 | INPUT NOT WALKED — Grok, (i), `docs/40 - DevDocs/cobalt/cli.md`: no `path:line` | `C:180`; `C:154` | RECORD — a question for round 2 (K14) | `33` §3 (an INPUT NOT WALKED row is a question, never a defect); `33` §4 ready rule | Not a fix row. `39` question (i) asks every seat for a `path:line` per docs cell and stages the three docs at the tip; Opus's round-1 cells (`cli.md:88`, `:96`) are not evidence for Grok's. |
| 6 | INPUT NOT WALKED — Grok, (i), `db_migrations/__init__.md` and `db_migrations/placement.md`: no `path:line` | `C:181`; `C:154` | RECORD — a question for round 2 (K14) | as row 5 | as row 5. |
| E8 | UNCLASSIFIED `.clinerules` widens `RESTARTS:` to every resident; main 33 ahead (docs-only since `daf36e01`); branch head `509f19f5` | `C:191`; R2:624 | RECORD — OWED to the DRC deploy | R74 (L42) | Carried: `38` re-derives `RESTARTS` on its range and re-reads ahead / behind at launch. |

The reading of the desk holds by the rows: every HOLD is hand-off text or a weak-assertion claim; none touches the merge, F1–F8, G1 or the guard (`C:5`). Not re-decided here.
`C` row 8 (`test_radar_handicap_store.py:190` "no assertion after the repeat") DOES NOT HOLD (`C:148`: `:192` asserts after the re-apply) and is not a classifier item.

## PIN SWEEP
At the drc-d1 worktree (tests = `7cdc5774`), `grep -r -n -F "<idiom>" tests`, one call each, 14:21–14:23 EDT:

| idiom | hits | pins `0019` breaks |
|---|---|---|
| `FORWARD[` | 12 | 11: `test_stale_score_db.py:159,161`; `test_assumed_store.py:245,246,249,251,253,255`; `test_drc_store.py:65`; `test_voice_store.py:57`; `test_archiver_migrations.py:84` (list). Not a pin: `test_migrate_proof.py:1510` (`FORWARD[0]`). |
| `REVERSE[` | 12 | `test_stale_score_db.py:160,162`; `test_assumed_store.py:247,248,250,252,254,256`; `test_drc_store.py:67`; `test_drc_k1_store.py:117`; `test_voice_store.py:57`; `test_archiver_migrations.py:101` (list). |
| `_rollback_paths(` | 26 | exact / prefix lists: `test_p4_migrations.py:101,116,127`; `test_radar_handicap_store.py:84`; `test_radar_score_migration.py:121,126`; `test_radar_migration.py:34`; `test_tenancy.py:515`; `test_drc_store.py:142`; `test_drc_k1_store.py:123`; `test_voice_store.py:58`; `test_archiver_migrations.py:129,139`. Not pins: `_apply` calls and suffix asserts (`test_radar_score_migration.py:122,127,132,494`; `test_tenancy.py:527–534`; `test_migrate_proof.py:1528`, value-free `[0]`). |
| `names[` | 12 | `test_drc_k1_store.py:116` (`names[-3:]`); `test_radar_score_migration.py:116` (`reverse_names[:10]`). Not pins: by-name slices (`test_tenancy.py:473`, `:532`; `test_radar_score_migration.py:92`) and non-registry hits (`test_drc_detect.py`, `test_archiver_runner.py`, `tests/taxonomy/test_catalyst.py`). |
| `numbers` (archiver file) | 10 | `test_archiver_migrations.py:170` (full list), `:171` (`[-8:-6]`), `:172` (`[-1] == 18`). |
| `len(FORWARD` / `len(REVERSE` | 0 / 0 | none |
| `range(1, 12)` | 1 | `test_archiver_migrations.py:170` (same pin) |
| `0018_drc_stated_books` | 24 | the name hits `32` listed, plus non-pins `test_drc_k1_store.py:3,45,46`, `test_drc_k1_experiments.py:362,363`. |
| `"0018"` | 0 | none |
| `CREATED_TABLES` | 30 | one set pin: `test_archiver_migrations.py:495–505` survivors (with `DRC_D1_TABLES` `:54`, `voice_turns` `:503`), asserted `:516–519` and `:528–531` (`@requires_db` `:469`). Every other hit is a membership / side check by name. |

With-DB-only pins (never shown by the offline suite): `test_stale_score_db.py` (module `pytestmark` `:22` = `requires_db`) and the archiver set pin. `08`'s re-point line: `prompts/2026-09-28/08-drc-d2-fix-r1-build.md:106` (`THE REGISTRY PINS …`: F0's `grep -rln -F "0018_drc_stated_books" tests` and pre-merge slots such as `test_drc_store.py:65`–`:66` `FORWARD[-3] == SQL`). `08` contains no `FOR 08` string.

## RECORDS
- `38` = `32`'s shape with the lock, R0-with-DB, the rows' Edit steps, T, the fix commit and W removed: this round edits no tracked file. R0 is ten greps against R2 (nine cites absent, `:580` present). R3-1's `## FOR 08` block sits in `38` verbatim (K16); `## PIN PROOF` P1–P11 re-prove every cited line and count at the tip; a moved line is corrected to the printed line and named `LINE MOVED`.
- `38`'s tip after CLOSE is its report commit; the code stays `7cdc5774`. Its stop line reads `report-only (code 7cdc5774; tip = this report's commit)` in the `<fix tip>` place, `files: 1 (src 0, tests 0, report 1)`, `with-DB not run`, `cobalt_dev: 0013 (untouched)`, `.env: absent`, `FIX: 1`.
- `38`'s RESTARTS range is `10163d51..<preflight head>`: its own report commit is not known while the report is written; that commit adds one `docs/` path, no restart by L42.
- `38`'s live-note leg runs with no `.env`: a count below `32`'s 146 whose extra skips name the database is named, not a stop.
- `39` = `33`'s shape, seats, strings and rules; round 2; the packet narrowed to `38`'s `## FOR 08` (+ `32`'s as SUPERSEDED), `38`'s proof sections, the hub's own sweep, the pin slices and six rollbacks, the three docs whole + their remerge hunks, `## BOTH-SIDES`, round 1's findings and this classification. Questions (i) docs with `path:line` · (ii) pin list complete · (iii) contract per file · (iv) the rest of the hand-off · (v) item (4)'s NOT REAL · (vi) scope and moved lines.
- `comm`: `38` line 5 vs `32` line 5 → 26 common, 0 / 0; the launch line identical after substituting path and name. `39` line 1 vs `33` line 1 → 15 common, 0 / 0; the `claude --bg …` span identical after substitution.
- Placeholders (the launch-row token, `grep -c -F`): `38` → 1 line (`:22`, the AUTHORIZATION row and its grep); `39` → 1 line (`:15`). `FILL AT LAUNCH`: `38` `:3` (head, main, time) + the gate `:21`; `39` `:1` (definition), `:12` (the gate), `:43` (`38`'s stop line, read time, `<r3 tip>`), `:64` (ceiling).

## OWNER ITEMS
NONE.

## FOR DEJAN
New strings: NONE. `38` carries `32`'s 25 allow + 3 deny strings unchanged; `39` carries `33`'s 14 allow + 3 deny unchanged.

## FOR THE DESK
- Fill: `38` `:3` and the launch-row token at `:22`; `39` `:43` (after `38` is BUILT: its stop line and `<r3 tip>` = `git -C /Users/cobalt/cobalt log -1 --format=%h drc/d1-trading-log`), `:64` (ceiling) and the launch-row token at `:15`.
- W: NOT run by `38` (no test or `src/` row). `38` needs no lock; its PREFLIGHT still requires no `.env` under any worktree (the drafter prompt's rule; ESCALATE 1).
- The `08` re-point: its registry-pin line is `prompts/2026-09-28/08-drc-d2-fix-r1-build.md:106` (F0's name grep and pre-merge slots). `08` has no `FOR 08` string; its base `6777c463` (stop line `:183`) is pre-merge too.
- Sol METER until 3:32 PM (`33` PREFLIGHT): `39` launched after then seats three houses.
- Order: commit this report, `38`, `39`; launch `38`; after `38` BUILT, fill `39` and launch it.

## ESCALATE
1. ASK DESK: `38`'s PREFLIGHT stops on ANY `.env` under `/Users/cobalt/cobalt-wt/*` (the drafter prompt's rule), though `38` takes no lock and its offline run needs only drc-d1's `.env` absent; a with-DB build elsewhere (e.g. `35`, R78) then blocks it. Narrow the gate to drc-d1 by an L19 re-issue? [14:31 EDT] Safe default taken: the gate stays as the desk wrote it.
2. RECORD: `38`'s stop line departs from the drafter prompt's template in four fields (`<fix tip>` text, `files:` with `report 1`, `cobalt_dev: 0013 (untouched)`, `.env: absent`), because no fix commit, lock or `.env` exists in a report-only round. The prefix `DRC MERGE FIX R3 BUILT ` is kept for the watcher.
3. RECORD: the sweep found pins neither checker named: `test_radar_score_migration.py:116`, `:121`, `:126` (read `newest_four`) and the with-DB table-set pin `test_archiver_migrations.py:54` + `:495–519` (a table `0019` adds to `CREATED_TABLES` must join the survivors' exclusions). Both are in R3-1's list.

## CONTINUE
next: none — the desk commits this report, `38` and `39`.

DRC MERGE FIX R3 DRAFTED · FIX: 3 · NOT REAL: 1 · UNPROVEN: 0 · OUT OF SCOPE: 0 · OWNER ITEM: 0 · code change: none · with-DB: no · prompts: 2 · new rule strings: 0 · ESCALATE: 3
