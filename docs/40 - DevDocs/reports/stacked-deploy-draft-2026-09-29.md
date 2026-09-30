# STACKED DEPLOY DRAFT 2026-09-29 — DRC D3 + S3 exits C1–C4 (`39` → `40`)

## §0 Headline
- `prompts/2026-09-29/40-stacked-deploy-0929.md` is written: one run, gate then deploy, five merges into `deploy/stacked-0929`, migrations `0016 0018 0019 0020 0021`, 12 new-by-text strings (FOR DEJAN).
- AS THE SET STANDS, `40` ENDS `FAILED: merge` AT MERGE 2. DRC and C1 conflict in 12 paths (ESCALATE 1). If the merges were resolved, STEP-R would still fail on two UNCLASSIFIED DRC configs (ESCALATE 2).
- The S3 branches are ONE stack, not four siblings (ESCALATE 3). C2's check verdict is only in an uncommitted working copy (ESCALATE 4).
- `40` needs a seam build and its check (the 09-25 shape) plus a `jobs.yaml` classification before it can go green. The desk decides.

## L74
One block arrived inside a tool result: appended to the output of the read of `39`, it asked for a `Claude-Session:` line in every commit and PR and named a file-send tool. It is data and was not followed. This session made no commit.

## THE SET
| # | branch | tip | check report | its stop line |
|---|---|---|---|---|
| 1 | `drc/d1-trading-log` (head `985cca3b` = build report above the tip) | `b8ac291b` | `reports/drc-d3-fix-r2-check-2026-09-29.md` (commit `f5166dc4`) | `DRC D3 FIX R2 CHECK DONE · round: 3 · opus: CHECK DRC D3 FIX R2: FIX STANDS · ready for K3: YES · sol: NOT SEATED (METER — retry after Oct 4th, 2026 2:06 PM) · grok: CHECK DRC D3 FIX R2: FIX STANDS · ready for K3: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for K3: YES · ESCALATE: 12` |
| 2 | `s3/exits-c1` | `bbf25412` | `reports/s3-exits-c1-fix-r2-check-2026-09-28.md` (`8061141f`) | `S3 EXITS C1 FIX R2 CHECK DONE · round: 3 · opus: CHECK S3 C1 FIX R2: BUILD STANDS · ready for C2: YES · sol: METER · grok: CHECK S3 C1 FIX R2: BUILD STANDS · ready for C2: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C2: YES · ESCALATE: 3` |
| 3 | `s3/exits-c2` | `04b3ca3e` | `reports/s3-exits-c2-fix-r1-check-2026-09-28.md` (committed `a71ecc81` = a different run; see ESCALATE 4) | working copy: `S3 EXITS C2 FIX R1 CHECK DONE · round: 2 · opus: CHECK S3 C2 FIX R1: BUILD STANDS · ready for C3: YES · sol: CHECK S3 C2 FIX R1: BUILD STANDS EXCEPT weak F1 pre-store assertions, weak F2 one-writer scan, weak F3 CLOSED-position coverage · ready for C3: YES · grok: CHECK S3 C2 FIX R1: BUILD STANDS · ready for C3: YES · houses that checked: 3 of 3 · defects that HOLD: 0 · ready for C3: YES · ESCALATE: 4` |
| 4 | `s3/exits-c3` | `6983de75` | `reports/s3-exits-c3-fix-r1-check-2026-09-29.md` (`6d53a1de`) | `S3 EXITS C3 FIX R1 CHECK DONE · round: 2 · opus: CHECK S3 C3 FIX R1: BUILD STANDS EXCEPT (vi) lock taken 3× (ESCALATEd), R1 NaN-exit stored and −1 correction 500 (out of scope, to round-2 classifier) · ready for C4: YES · sol: METER · grok: CHECK S3 C3 FIX R1: BUILD STANDS EXCEPT (iii) C2 not_current replaced by the route sentence · ready for C4: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for C4: YES · ESCALATE: 8` |
| 5 | `s3/exits-c4` (head `0a64bd75` = build report above `6785c7d5`) | `6785c7d5` expected; a launch-time value | `reports/s3-exits-c4-fix-r2-check-2026-09-29.md` | NOT YET WRITTEN (`ls` → No such file, 21:5x). Build: `S3 EXITS C4 FIX R2 BUILT 6785c7d5 \| on 01d0fbb9 \| migration none (0021 rolled back) \| offline 3327/0 \| with-DB 3846/0 \| live-note 146/0 \| cobalt_dev: 0013 \| .env: removed \| RESTARTS: com.cobalt.aset com.cobalt.radar \| FIX: 1 \| RUNS: 1 \| self-check: 3 of 3 \| ESCALATE: 1` |
Main at the draft: `45b4c0ba docs(desk): 09-29 R171 next desk on Sonnet 5.5 with a brain tab on his ask` (22:03:56; `80dc0ed8` at 21:52:50). LIVE `deploy-2026-09-27` = `3349466f`.

## MIGRATIONS
`src/cobalt/db/migrations` does not exist (`ls` → No such file). The path is `src/cobalt/db_migrations`, as `50` G1 uses it. `git -C /Users/cobalt/cobalt diff --stat main...<tip> -- src/cobalt/db_migrations`:
- DRC `b8ac291b`: `0016_drc`, `0018_drc_stated_books`, `0019_drc_events`, `0020_drc_build_kinds` (+ `.rollback.sql` each), `__init__.py`, `placement.py` — 10 files.
- C1 `bbf25412`, C2 `04b3ca3e`, C3 `6983de75`, C4 `6785c7d5`: the same five files — `0021_legs(.rollback).sql`, `__init__.py`, `cli.py`, `placement.py` (C2–C4 carry C1's).
- Total new: **5** (`0016 0018 0019 0020 0021`). Production is at `0017`. Objects: `0016` `"user".drc_imports` / `drc_fills` / `drc_rows`; `0018` `drc_stated_books` + `drc_rows_kind_check`; `0019` `drc_events`; `0020` widens `drc_rows_kind_check` (`build_trade`, `build_day`); `0021` `"user".legs`, `legs_current_v`, `card_stop_edits.kind`, `aset_sizings.trade_note_path` / `drift_warning_pct` / `drift_warned`. `40`'s `<RB>` reads these: BEFORE `0 · 0 · 0 · 0`, AFTER `5 · 1 · 2 · 4`.

## RESTARTS EXPECTED
From each build report's `## RESTARTS` / stop line (the deploy derives the real one):
- DRC D3 fix r2 (`drc-d1` worktree, `drc-d3-fix-r2-build-2026-09-29.md` `## RESTARTS`): `15c23748..b8ac291b` → `RESTARTS: com.cobalt.radar`. The DRC range `f52ed883..b8ac291b` → exit 1, `configs/cobalt/prefill.yaml M UNCLASSIFIED CONFIG` and `configs/cobalt/templates/drc.md.j2 D UNCLASSIFIED CONFIG` → `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar`.
- C1: build `RESTARTS: com.cobalt.aset com.cobalt.radar`; fix r1 the same; fix r2 `RESTARTS: none`.
- C2: build and fix r1 `RESTARTS: com.cobalt.aset com.cobalt.radar`.
- C3: build and fix r1 `RESTARTS: com.cobalt.aset com.cobalt.radar`.
- C4: build `com.cobalt.aset com.cobalt.radar`; fix r1 `none`; fix r2 `com.cobalt.aset com.cobalt.radar` (`e49fe6a2..6785c7d5`: `src/cobalt/prefill/trade_note.py` static import reach).
- DRC changes `pyproject.toml` and `uv.lock` (`git diff --name-status main...b8ac291b`). By 09-27's table those derive `com.cobalt.agent` too (`deploy-2026-09-27.md` G4).
- Expected once DRC's two configs are classified: `com.cobalt.agent com.cobalt.aset com.cobalt.radar`. As they stand, STEP-R ends FAILED.

## RULE STRINGS
`sed -n '6p'` of `50` vs line 6 of `40`, `grep -o '"[^"]*"'`, the `Read '…'` instruction removed, `sort`, `comm -3` (column 1 = `50` only, column 2 = `40` only):
```
"Bash(COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run cobalt radar handicap-dry-run --day 2026-09-27)"
	"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/deploy-0929/.env)"
"Bash(cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0925/.env)"
"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0925)"
	"Bash(git -C /Users/cobalt/cobalt merge --ff-only deploy/stacked-0929)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --abort)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit 04b3ca3e)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit 6983de75)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit b8ac291b)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit bbf25412)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit «FILL AT LAUNCH: c4 tip»)"
	"Bash(git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit main)"
"Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --abort)"
"Bash(git -C /Users/cobalt/cobalt-wt/stacked-0925 merge --no-edit main)"
	"Bash(launchctl bootout gui/501/com.cobalt.prefill-drc)"
	"Bash(rm /Users/cobalt/cobalt-wt/deploy-0929/.env)"
"Bash(rm /Users/cobalt/cobalt-wt/stacked-0925/.env)"
	"Bash(rm /Users/cobalt/Library/LaunchAgents/com.cobalt.prefill-drc.plist)"
```
Common: 47 (44 allow + the 3 denies). `50`: 50 allow; `40`: 56 allow.

## FOR DEJAN
12 strings that are new by text. Each is forced by the set:
- 5 RE-POINTS of `50`'s gate strings from `stacked-0925` to `stacked-0929` / `deploy-0929`: `merge --ff-only deploy/stacked-0929`, the gate's `merge --no-edit main`, `merge --abort`, the `.env` `cp` and `rm`. Reason: tonight's gate branch is new (L54).
- 5 TIP MERGES `git -C /Users/cobalt/cobalt-wt/deploy-0929 merge --no-edit <tip>` for `b8ac291b`, `bbf25412`, `04b3ca3e`, `6983de75` and C4's launch-time tip. Reason: `39` has the deploy build the combined tree. Shape precedent: `07`'s branch-named gate merges (`50`:17).
- 2 FOR DRC's RETIRED JOB: `launchctl bootout gui/501/com.cobalt.prefill-drc` and `rm /Users/cobalt/Library/LaunchAgents/com.cobalt.prefill-drc.plist`. Reason: DRC deletes `ops/com.cobalt.prefill-drc.plist` and its `jobs.yaml` entry, and its build's `## FOR THE DEPLOY` names the bootout and the plist removal. The plist is on disk: `ls -la /Users/cobalt/Library/LaunchAgents/` lists `com.cobalt.prefill-drc.plist` (3361 B, Sep 3).
- DROPPED: `50`'s `radar handicap-dry-run --day 2026-09-27` string (no H1 in the set).
- Also his: the five production migrations by name, and the approval row `40`'s P-HIS reads (`STACKED DEPLOY 2026-09-29 APPROVED`).

## ESCALATE
1. **THE COMBINED TREE DOES NOT MERGE CLEAN (seam, L68 / L72).** This is a read-only `git merge-tree <merge-base> b8ac291b <tip>` (trivial-merge mode; no ref or object written). Conflict hunks, DRC × C1 `bbf25412`: `src/cobalt/db_migrations/__init__.py` 3 · `src/cobalt/db_migrations/placement.py` 2 · `tests/cobalt/test_archiver_migrations.py` 7 · `test_assumed_store.py` 1 · `test_p4_migrations.py` 3 · `test_radar_handicap_store.py` 1 · `test_radar_migration.py` 1 · `test_radar_score_migration.py` 4 · `test_stale_score_db.py` 1 · `test_tenancy.py` 1 · `test_voice_store.py` 1 · `docs/40 - DevDocs/cobalt/db_migrations/__init__.md` 1. DRC × C3 `6983de75` adds `src/cobalt/aset/web.py` 1 and `docs/40 - DevDocs/cobalt/aset/web.md` 1. The cause: each side registers its migrations in the same `FORWARD` / `REVERSE` lines. DRC puts `0016`, `0018`–`0020` around `0017` (`b8ac291b` `__init__.py`:136–149); C1 puts `0021` after `0017` (`bbf25412`:116–123); the nine test files pin the registry. `40` resolves nothing and ends `FAILED: merge — 2 bbf25412 — …`. ASK DESK [22:04]: launch a seam build and check (the 09-25 shape, `50`:30) and re-point `40` at the seam tip? Safe default: `40` stands as `39` asked.
2. **RESTARTS UNCLASSIFIED BY CONSTRUCTION (L42, K10).** `configs/cobalt/prefill.yaml` (M) and `configs/cobalt/templates/drc.md.j2` (D) are UNCLASSIFIED on `b8ac291b` (DRC fix r2 build `## RESTARTS`). S3 does not touch `jobs.yaml`, so the combined table carries both rows and `40` STEP-R ends FAILED. K10: "unclassified config = `no_resident_reads`": a `jobs.yaml` line on a checked branch or in the seam. ASK DESK [22:04]: land it with the seam of item 1?
3. **THE S3 BRANCHES ARE STACKED.** This contradicts `39`'s "`s3/exits-c4` contains none of them". `git merge-base --is-ancestor bbf25412 <x>` → exit 0 for `04b3ca3e`, `6983de75`, `6785c7d5`. `merge-base(04b3ca3e, 6785c7d5)` = `5e77800f` (C2's code tip); `merge-base(6983de75, 6785c7d5)` = `78e9df82` (C3's code tip). `6785c7d5..04b3ca3e` = only `04b3ca3e` (C2's report); `6785c7d5..6983de75` = only `6983de75` (C3's report). The build stop lines agree: C2 `on bbf25412`, C3 `on 5e77800f`, C4 `on 78e9df82`. `40` states this and keeps the five merges. Merges 3–5 add C2–C4's own commits.
4. **C2's CHECK IS NOT ON RECORD.** The committed `s3-exits-c2-fix-r1-check-2026-09-28.md` (`a71ecc81`) is the run that "did NOT launch … Stopped at AUTHORIZATION". The `CHECK DONE` text in THE SET row 3 exists only in the working copy (`git diff --stat` → `96 insertions(+), 16 deletions(-)`). `40` P2 refuses a report whose working copy differs from its commit. The desk commits the file before launch. The branch stays in the set, marked.
5. C4's check `38` had written no report at the draft (`ls` → No such file). `<c4 tip>` and `<c4 check stop>` are launch-time values. If `38` says NO, the desk holds C4 out and re-issues `40`; the drafter decides nothing.
6. THE WINDOW. L66 puts the merge "inside the 20:00–21:00 pause". Tonight's run lands after 21:00. `40` uses L43's overnight-idle clause (after the pause, before 04:00) under his R169 "tonight". ASK DESK [22:04]: is that the right reading of L66 tonight? Safe default: overnight idle, as written.
7. OVERNIGHT GUARDS in `40`. `com.cobalt.generated` commits on main at 23:37 (`configs/cobalt/jobs.yaml:301`): no bootout 23:30:00–23:44:59, and 4.3 refuses a foreign HEAD. The nightly backup at 21:40 runs up to 3600 s (`:260`): `40`'s snapshot waits for it in `backup status`.
8. SCHEMA ROLLBACK SHAPE. `0016` sorts below `0017` in `REVERSE`. `--down-to 0017` then leaves `0016` applied, and `--down-to 0015` also drops `0017`'s live `voice_turns`. How `--down-to` treats an out-of-order id is UNPROVEN (L70). Written into `40`'s ROLLBACK STRING for him.
9. VALIDATE vs the retired job. With DRC's registry and `~/Library/LaunchAgents/com.cobalt.prefill-drc.plist` still on disk, `validate`'s `registry <-> plists` line is UNPROVEN. `40` G (d2) treats a violation naming ONLY `com.cobalt.prefill-drc` as known. After 4.2b removes the plist, 4.5 must be clean.
10. THE WITH-DB GATE ON THE COMBINED TREE. `39` requires C4 W's commands byte for byte. DRC's own F8 ran ONE pass at `0013` with nine ids deselected and never ran the three standing ids (`TestMigrationRoundTrip`, the GUC test, the named-cursor probe) with `0016`–`0020` applied. In `40`'s pass 2 they meet DRC's migrations for the first time, and the named-cursor count moves (DRC probe: `assert 28 == 34`). UNPROVEN: a pass-2 red here is information for the seam, not a defect (L70).
11. `.clinerules` (R74). `grep -n "clinerules"` → no line in `configs/cobalt/rules.yaml`; `cto-2026-09-28.md`:82 (R74, "ESC 1 UNCLASSIFIED `.clinerules` widens RESTARTS → OWED to the DRC deploy") and `:233` (OWED). `git diff --name-only main b8ac291b` carries no `.clinerules` (0 lines): tonight's range derives no row for it. `40` P5 re-proves it.
12. `39` cites R123 for "Radar `4c1f4911` is NOT in the set". R123 (`cto-2026-09-29.md`:131) is a REFRESH record; `grep -n "4c1f4911"` on that file prints nothing. `4c1f4911` is on `radar/stop-record-0928`, not in `40`'s set.
13. SEAMS in `git log main..<tip> -- src` (src commits: DRC 24, C1 2, C2 4, C3 6, C4 8), by each branch's own range (C2–C4 above `bbf25412`): DRC ∩ C1 `src/cobalt/db_migrations/__init__.py`, `src/cobalt/db_migrations/placement.py`; DRC ∩ C1 ∩ C2 ∩ C3 ∩ C4 `src/cobalt/aset/web.py`; C1–C4 (the stack) `src/cobalt/aset/store.py`, `src/cobalt/cards/cli.py`, `src/cobalt/cards/legs.py`, `src/cobalt/cards/store.py`; C3 ∩ C4 `src/cobalt/aset/radar_panel.py`.14. The C4 and DRC build reports `40` cites live only in their worktrees (`s3-exits-c4`, `drc-d1`), under `--add-dir /Users/cobalt/cobalt-wt`.

## CONTINUE
next: the desk reads ESCALATE 1–4 and decides the seam; then it fills `40`'s launch-time values and approval row (P-HIS), runs the placeholder count, commits, and launches.

STACKED DEPLOY 0929 DRAFTED · set: 5 · migrations: 5 · restarts expected: com.cobalt.agent com.cobalt.aset com.cobalt.radar (after DRC's 2 UNCLASSIFIED configs are classified; as they stand: all six) · new rule strings: 12 · ESCALATE: 14
