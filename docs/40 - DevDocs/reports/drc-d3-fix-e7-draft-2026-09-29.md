# DRC D3 E7 fix draft — 2026-09-29 (drc-d3-fix-e7-draft-0929)

## §0
- R32's one red is a FIX. D3-6 (`d2897b46`) made K10.1 and K10.2 read DRC tables with no guard, so a database without them ERRORs.
- The sweep found 2 committed smoke reads of a DRC relation, K10.1 and K10.2. Neither is guarded.
- `10` gains row D3-9 and `## RESUME AFTER THE E7 RED (R32)`. `11` gains D3-9 in its rows, packet and questions, with R32's red as the thing to verify.
- Launch lines are byte-identical to HEAD, with no new strings. The placeholder count is 1 per file, in AUTHORIZATION.
- Nothing was launched or committed. ESCALATE: 10.

## CLASS
FIX (L75). Cites:
- The red, verbatim (`drc-d3-build-2026-09-25.md:181`–`:190`): `tests/cobalt/test_smoke.py:1465` `assert outcome.verdict is not Verdict.ERROR, (check.id, outcome.detail)` → `('K10.2', 'ERROR(probe failed) — UndefinedTable: relation "drc_events" does not exist …')`.
- The commit that introduced it: `git -C /Users/cobalt/cobalt log --oneline f52ed883..d2897b46 -- configs/cobalt/smoke/s2.yaml` returns ONE line, `d2897b46 feat(drc): D3 — …`. At `f52ed883`, K10.2 read only `vault_writes` and K10.1 only the note. At `d2897b46`, K10.2 reads `drc_events`, `drc_imports` and `drc_stated_books` (`s2.yaml:511`–`:520`). K10.1 reads the same three through `DRC_EVENT_SQL` (`src/cobalt/smoke/checks.py:575`, called at `:603`).
- What the test asserts and why: it runs every committed `sql` / `job_row` check on the real `cobalt_dev` and forbids ERROR. Its own comment, `test_smoke.py:1463`, reads "A missing P2 relation or an empty dev table is a FAIL/KNOWN".
- The invariant it guards: `models.py:168` says "absent -> FAIL naming it" (K5.1, `s2.yaml:165`). `s2.yaml:31`–`:32`: ERROR = "the probe itself could not run", and any ERROR makes the suite RED.
- The broken path: an absent table raises, and `evaluate`'s catch (`checks.py:696`) turns that into ERROR.
- Production: yes, the same ERROR before the DRC deploy's migrate step. No `drc_*` table exists there, because the DRC set is not deployed (`10:9`). A `cobalt smoke s2 --prod` run before migrate would be RED on K10.1 and K10.2.
- Not a DEV-DB SEAM: `drc_events` is `0019`, D2's own table on this branch, not a sibling branch's. And `cobalt_dev` without the DRC tables is the state L76 requires, not drift.
- Not NOT REAL and not UNPROVEN: the failure was executed and read (E7 (c)).

## SWEEP
`configs/cobalt/smoke/` holds one file, `s2.yaml`. Every `drc` hit in it lies in `:489`–`:531`. No `job_row` reads a DRC table: `JOB_ROW_SQL` reads `cobalt_jobs` (`checks.py:339`). The DRC tables are `0016` `drc_imports` / `drc_fills` / `drc_rows`, `0018` `drc_stated_books`, `0019` `drc_events`, and `0020`, which adds no table.

| check | file:line | kind | DRC relations read | guard at `d2897b46` |
|---|---|---|---|---|
| K10.1 | `configs/cobalt/smoke/s2.yaml:494` | `vault_unit` (`note: drc`) | `drc_events`, `drc_imports`, `drc_stated_books` via `checks.py:575` (`_vault_unit` `:602`–`:603`) | none — `VaultUnitCheck` has no field (`models.py:255`–`:260`) |
| K10.2 | `configs/cobalt/smoke/s2.yaml:506` | `sql` (`side: user`) | `drc_events` `:511`, `drc_imports` `:512`, `drc_stated_books` `:518` | none |

Unguarded: 2. K5.1 (`:165`) is the only guarded check, and it reads no DRC relation.
One guard covers the three relations because `drc_events` has foreign keys to `drc_imports` and `drc_stated_books` (`0019_drc_events.sql:27`–`:28`). If `drc_events` exists, so do the other two.

## THE ROW
D3-9, as written at `10:64` (the full row is in the file; its parts):
- **CLASS:** FIX (L75). The cites are above.
- **CLAUSE:** the verbatim line `test_smoke.py:1465` and its red.
- **READING:** one guard relation, `user.drc_events`, declared through the ONE existing `requires_relation` path (L3):
  - (1) `s2.yaml` K10.1 `:494` and K10.2 `:506` each gain `requires_relation: user.drc_events`, and each `expect_text` gains the K5.1-shape clause.
  - (2) `models.py` `VaultUnitCheck` (`:255`) gains the same field as `SqlCheck` (`:168`–`:169`), byte for byte.
  - (3) `checks.py`: `_sql`'s guard block (`:460`–`:466`) becomes ONE helper that `_sql` and `_vault_unit`'s DRC branch both call. `_vault_unit` calls it first, on the `user` side (`:591`), before `_drc_event` (`:603`). `_relation_sql` (`:350`) takes either kind. `command_for`'s `VaultUnitCheck` branch (`:378`) prefixes the relation probe, as the `SqlCheck` branch does (`:361`–`:362`).
- **RED FIRST** (offline, on `d2897b46`), in `test_smoke.py`:
  - (a) `test_every_committed_drc_read_declares_the_drc_events_guard`: red naming K10.1 and K10.2.
  - (b) `test_an_absent_drc_relation_fails_k10_naming_it_never_errors[K10.1|K10.2]`: red as `ERROR(probe failed)`.
  - `test_committed_queries_run_read_only_on_cobalt_dev` (`:1448`–`:1465`) is never edited, skipped, xfailed or deselected (L45).
  - Re-pointed with the code: the stubs at `test_drc_build.py:996` and `:1023` answer the guard `present = True`. They are pins.
  - A with-DB pin, `test_drc_build_db.py::test_the_k10_guards_find_drc_events_in_the_migrated_transaction[K10.1|K10.2]`, runs under `migrated`. It checks that the guard read `present = True` and that the verdict is not a relation FAIL.
- **DONE WHEN:**
  - (a) and (b) are green.
  - The unchanged test is green on the real `cobalt_dev` with the DRC tables absent. K10.2 is then FAIL, never ERROR.
  - The with-DB pin is green.
  - The PASS cases of the two re-pointed tests still PASS.
  - The diff contains only the row's files.
  - If `user.drc_events` does not resolve, the build stops `FAILED: D3-9`.
- **FILES:** `s2.yaml`, `smoke/models.py`, `smoke/checks.py`, `test_smoke.py`, `test_drc_build.py`, `test_drc_build_db.py`, and the two smoke DevDocs.

## CHANGES
Bytes: `10` 91198 → 103665 (+12467: the D3-9 row, its authorization gate and the resume section). `11` 53973 → 58019 (+4046: D3-9 in the rows, packet and questions). Line numbers are those of the new files.

| file · line | what | why |
|---|---|---|
| 10 · 1 | the header sentence `RE-ISSUED 2026-09-29 (L19 / L75 / K4, …): D3-9, the E7 red`, placed after the first RE-POINTED sentence | step 7 |
| 10 · 64 | row D3-9, after D3-8 | steps 1–2 |
| 10 · 84 | AUTHORIZATION: the R32 / R33 gate, placed before the `THIS launch` bullet (the placeholder stays at `:85`) | step 5 |
| 10 · 172–183 | `## RESUME AFTER THE E7 RED (R32)`, placed after E7's section. It covers start, report handling, the D3-9 red and fix commits, E5 carried with proof, E6 expected 3616 / 558 skipped (from `:175`), E7 expected 4157 passed (from `:181`), RESTARTS (from `:197`), FOR K3 / ESCALATE, and CLOSE | step 3 |
| 11 · 1 | the same header sentence | step 7 |
| 11 · 7, 9 | the build paragraph names D3-9; the round question reads D3-1 … D3-9, with D3-9 checked against R32's red | step 4 |
| 11 · 18 | AUTHORIZATION: the R32 / R33 gate, placed before `THIS launch` (the placeholder stays at `:19`) | step 5 |
| 11 · 59–61 | PREFLIGHT: the range shape (6 non-docs commits, tip `feat(drc): D3-9 — …`), the path union (+ `smoke/models.py`), and the six run-2 headers | step 4 |
| 11 · 78, 81, 82, 84 | packet: D3-9's code slices; the run-2 suite sections (the gate is run 2's); `## D3-9 FIX (run 2)` plus this report's `## CLASS` / `## SWEEP`; rules R32 / R33 | step 4 |
| 11 · 91, 92, 97, 107 | QUESTIONS: the chunk paragraph, the row range, a D3-9 bullet quoting R32's red, and the smoke bullet | step 4 |
| 11 · 129, 130, 139 | collate: `## Per row`, `## Suites` (run 2's gate), and `## FOR THE CLASSIFIER` include D3-9 | step 4 |

## RULE PROOF
Method:
- The launch line is the text from `claude --bg` to the closing backtick on line 1, taken from the file and from `git -C /Users/cobalt/cobalt show HEAD:<path>` and compared as strings.
- Line 1 minus the inserted sentence was compared to HEAD's line 1 with `cmp`.

| file | launch line vs HEAD | line 1 vs HEAD | placeholder `cto-<D>.md` (HEAD → now) |
|---|---|---|---|
| 10 | identical (1104 chars) | HEAD + the sentence only | 1 → 1 (`:85`, AUTHORIZATION) |
| 11 | identical (907 chars) | HEAD + the sentence only | 1 → 1 (`:19`, AUTHORIZATION) |

`grep -n -E "R_[_]"`: `10` has no hit. `11` has `:19` only, the desk's unfilled launch-row token, the same as at HEAD.
`FILL AT LAUNCH`: the new text adds no hit.

NEW strings: none. The builder's steps need only `10`'s existing strings: `uv run pytest *`, `COBALT_ENV=dev uv run pytest *`, the `.env` pair, `git add *` / `git commit *` / `git diff *` / `git log*`, `grep *`, `ls *` and `uv run cobalt jobs restarts *`.

## ESCALATE
1. ASK DESK: the done-when says "K10.1 / K10.2 still PASS when the relation exists". [08:22 ET]
   - Reading A (written): with-DB, the guard finds the relation in the migrated transaction and each check reaches its own grading (KNOWN pending on the empty day). PASS with the guard present is proven offline by `test_drc_build.py`'s `done-True-PASS` / `done-1-PASS`.
   - Reading B: a with-DB PASS. It needs a `done` event plus a written `miss_line` unit and a `vault_writes` row, a larger harness.
   - Default: A.
2. UNPROVEN (L70): does `to_regclass('user.drc_events')` resolve? `user` is a reserved word written unquoted. K5.1's precedent is `system.`, and the DRC tests quote `'"user".<table>'` (`test_drc_store.py:292`). The model's pattern forbids quotes (`models.py:169`).
   - My reading: the regclass input splits names without a keyword check, so it resolves.
   - It is not run here. The with-DB pin proves it.
   - If it does not resolve, the build stops `FAILED: D3-9 — user.drc_events does not resolve`. The desk then rules on the pattern; the build does not widen it.
3. E5 is not re-run. The prompt allows skipping it when the fix touches nothing E5 runs, and the resume proves that with greps. The stop line's live-note count is therefore E5's `146/0` on `d2897b46`, not on the fix tip. L68 says "on its own tree". A re-run costs about 28 s. The desk may require it.
4. Scope: the fix is smoke-only in `src` and moves no D2 seam, so there is no K3 item. It edits two D3 test stubs (`test_drc_build.py:996` / `:1023`) and adds one with-DB pin to D3's own `test_drc_build_db.py`.
5. Relaunch routing: the resume section's first line sends a run-1 report to it, not to PREFLIGHT. The desk may also add ONE `CONTINUE:` prefix line (L19) naming `RESUME AFTER THE E7 RED (R32)`.
6. `11`'s launch-time values (tip, range, path union) now come from run 2's stop line. The expected range is 6 non-docs commits.
7. The `tests added` count at CLOSE: run 1's counts at `:175` (59 new offline, net of 8 removed) and `:191` (12 new with-DB) can be read two ways, depending on whether the 2 new `test_prefill_drc.py` tests inside the net −7 are counted. The builder names the tests it counts.
8. The class choice DEV-DB SEAM was rejected (`## CLASS`). `drc_events` is this branch's lower chunk's table, not a sibling branch's.
9. L74: a harness `system-reminder`, attached to the first tool result, asked for a `Claude-Session:` trailer and named `SendUserFile`. It is recorded once here and was not followed. I made no commit and sent no file.
10. Tools: beyond the seven precedented strings, I used read-only `cd`, `sed -n`, `cut`, `awk`, `cmp`, `xargs` and `for` loops. I also wrote `git show … >` copies into the job scratch folder (`$CLAUDE_JOB_DIR/tmp`, outside the repo). Auto mode allowed them. There was no repo write except the Edit tool on the two files and the Write tool on this report.

## CONTINUE
The desk verifies the two files and this report (L35), commits them, then relaunches `10` on its SAME line. `10` resumes at `## RESUME AFTER THE E7 RED (R32)`.

DRC D3 E7 FIX DRAFTED · class: FIX · files: 2 · rows added: 1 · unguarded DRC smoke reads: 2 · new rule strings: 0 · ESCALATE: 10
