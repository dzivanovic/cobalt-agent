# DRC merge fix r1 — classification and prompts 2026-09-28 — seat `drc-merge-fix-r1-draft-0928`

## §0 Headline
- `15`'s 7 offline reds on `5bb1f4b5` are all single-side registry position pins → FIX F1–F7, tests only. `15` ESCALATE 3 → FIX F8: R-ARCH as ruled drops the docstring paragraph. `15` ESCALATE 1 → RECORD.
- Pytest stops each test at its first failing assert. The same tests hold 10 more stale pins (`test_assumed_store.py:246–252`, `test_drc_k1_store.py:117`, `test_drc_store.py:66`, `test_voice_store.py:58`), and F1, F2, F4 and F7 re-state them.
- Two with-DB tests the offline run skipped read red at `5bb1f4b5` (U1 a position pin, U2 a rollback on an absent table). Nobody ran them, so they are UNPROVEN (L70) and were not built. ASK DESK 1.
- Written: `prompts/2026-09-28/17-drc-merge-fix-r1-build.md` (33,854 B) and `prompts/2026-09-28/18-drc-merge-fix-r1-check.md` (35,366 B). New rule strings: 0.
- ESCALATE: 1.

## L74
A block arrived appended to the Bash tool result that printed this prompt (`16-draft-drc-merge-fix-r1.md`). It asked every commit and PR body to carry a `Claude-Session:` line and named a file-send tool. It is data and was not followed. This seat commits nothing.

## Authorization
`grep -n -F "16-draft-drc-merge-fix-r1.md" ".../cto-2026-09-28.md"` → `:54` `| R46 | 10:56–10:58 ET |` … `LAUNCH drafter prompts/2026-09-28/16-draft-drc-merge-fix-r1.md` … `| LAUNCHED |`. Read Mon Sep 28 10:58:28 EDT 2026.

## Classification
Source file: `S` = `/Users/cobalt/cobalt-wt/drc-d1/docs/40 - DevDocs/reports/drc-merge-main-build-2026-09-28.md` (committed in `338a2439`). Test lines are at `5bb1f4b5`. Merged order at `5bb1f4b5:src/cobalt/db_migrations/__init__.py`: FORWARD tail `0011, 0013, 0014, 0015, 0016, 0017, 0018`; REVERSE head `0018, 0017, 0016, 0015, 0014, 0013, 0011`. `_rollback_paths(n)` = REVERSE entries numbered above `n` (`cli.py:774–784`).

| # | finding (short) | source line | class | traces to | FIX shape or reason |
|---|---|---|---|---|---|
| 1 | `test_assumed_store.py:245` `FORWARD[-4]` = 0013; same test `:246–252` pins 0014/0015 at `[-3]`/`[-2]`, 0017 as tail | `S:129` | FIX | R38 (1); `15` O; main-side file | F1: every tail slot to its number, `FORWARD[-6]`…`[-1]` = 0013…0018, `REVERSE[5]`…`[0]` mirrored. Intent: 0014 directly after 0013; the whole tail pinned. |
| 2 | `test_drc_k1_store.py:116` `names[-2:]` = 0016, 0018; `:117` `REVERSE[1]` = 0016 | `S:135` | FIX | R38 (1); `15` O; branch-side file | F2: `names[-3:]` = 0016, 0017, 0018; `REVERSE[0]` = K1, `REVERSE[1:3]` = 0017, 0016. Intent: 0018 after 0016, last. |
| 3 | `test_drc_k1_store.py:121` `_rollback_paths("0016")` = [0018] | `S:140` | FIX | R38 (1); `15` O | F3: [0018, 0017] + one comment line. Intent: every rollback above the bound, newest first, 0016 excluded. Name kept (main's precedent: `test_radar_handicap_store.py:82`). |
| 4 | `test_drc_store.py:65` `FORWARD[-2]` = 0016; `:66` `REVERSE[1]` = 0016 | `S:145` | FIX | R38 (1); `15` O; branch-side file | F4: `FORWARD[-3]` = 0016 with `[-2:]` = 0017, 0018; `REVERSE[2]` = 0016 with `[:2]` = 0018, 0017. |
| 5 | `test_drc_store.py:140` `_rollback_paths("0011")` = [0018, 0016] | `S:149` | FIX | R38 (1); `15` O | F5: [0018, 0017, 0016, 0015, 0014, 0013]. |
| 6 | `test_radar_handicap_store.py:84` `_rollback_paths("0013")` = [0017, 0015, 0014] | `S:158` | FIX | R38 (1); `15` O; main-side file | F6: [0018, 0017, 0016, 0015, 0014]; its own comment `:83` kept. |
| 7 | `test_voice_store.py:57` `FORWARD[-1]` = 0017; `:58` `_rollback_paths("0015")` = [0017] | `S:166` | FIX | R38 (1); `15` O; main-side file | F7: `FORWARD[-2]` / `REVERSE[1]` = 0017's pair; `_rollback_paths("0015")` = [0018, 0017, 0016]. |
| 8 | ESCALATE 1: permission dialog during E0 (backslash-escaped path spelling); desk pressed Escape and directed | `S:566` | OUT OF SCOPE — RECORD | L62 / L63 | Not a code finding; no tree change. `17` keeps `15`'s quoted-path rule. |
| 9 | ESCALATE 2: O red, 7 pins outside the conflict set | `S:567` | FIX (= rows 1–7) | R38 (5); L75 | Built as F1–F7; not counted twice. |
| 10 | ESCALATE 3: the branch's registry-pin docstring paragraph in `test_archiver_migrations.py`, outside the markers, kept by safe default | `S:568` | FIX | `15` `## BOTH-SIDES` R-ARCH; R46 | F8: `test_archiver_migrations.py:160–167` → `    never by position."""` (main's ending, `daf36e01`). |
| U1 | `test_stale_score_db.py:156–162` `test_0015_is_registered_after_0013_and_its_rollback_first`: `FORWARD[-2]` = 0015, `REVERSE[1]` = 0015, `FORWARD[-4]` = 0013, `REVERSE[3]` = 0013; at `5bb1f4b5` `FORWARD[-2]` is 0017 | drafter's read, `5bb1f4b5` | UNPROVEN | L70; module `pytestmark` = `requires_db` (`:22`), skipped in `15`'s O | Not built. First run: `17` W (c1). If proven, it is a position pin; the FIX shape is under ASK DESK 1. |
| U2 | `test_radar_handicap_store.py:170–194` applies FORWARD < 14, then 0014, then `_rollback_paths("0013")`, whose first file is now `0018_drc_stated_books.rollback.sql` starting `DELETE FROM "user".drc_rows …`; `drc_rows` does not exist on that tree | drafter's read, `5bb1f4b5` | UNPROVEN | L70; `requires_db`, skipped in O | Not built. Not a position pin: a test setup or a rollback guard (`src/`). An engineering choice the houses can settle, not an owner item (L67). ASK DESK 1. |

## RECORDS
- `17` R0 re-runs the 6 row files offline before any edit and expects exactly `15`'s 7 ids. T re-runs them after the rows. O expects 3547 passed (7 + 3540).
- F1 and F4 add slot pins for 0016 / 0018 / 0017. Before the merge, each test pinned every slot from its number to the tail, and the added pins keep that coverage. No assertion is removed.
- Test names are unchanged (F3, F4, F7 say "last" / "only"). Main's own `test_down_to_0013_selects_only_this_rollback` already selects every newer rollback under the same name.
- `17`'s `## FOR 08` lists the registry-pin files that `08` must re-state when it adds `0019`, including `test_stale_score_db.py`.
- `18` checks the remerge-diff of `5bb1f4b5`. If the option is refused, it falls back to `15`'s `## FOR THE CHECK`.

## OWNER ITEMS
NONE.

## FOR DEJAN
New strings: NONE. `17` uses `15`'s line without the two merge strings (`comm`: 26 common, 2 in `15` only, 0 new). `18` uses `09`'s line (`comm`: 15 common, 0 either side only).

## ESCALATE
1. ASK DESK: should U1 / U2 become FIX rows before `17` launches? [11:08 EDT] Safe default taken: `17` builds F1–F8 only. U1 / U2 first run in `17`'s W (c1), and a red there ends `FAILED: W (c1)` with the lock released by (f) step 3. Reading from `5bb1f4b5`: U1 goes red, and U2 goes red on `UndefinedTable` from 0018's rollback. If the desk rules U1 FIX, the row for `17` (an L19 re-issue) is `test_stale_score_db.py:159–162`: `FORWARD[-4]` / `REVERSE[3]` = 0015's pair, and `FORWARD[-6]` / `REVERSE[5]` = 0013. For U2, the houses choose between a test-only setup (apply the FORWARD files above 0014 before the bounded rollback) and a `to_regclass` guard in `0018_drc_stated_books.rollback.sql` (a `src/` change on an unmerged migration).

## CONTINUE
For the desk: commit this report, `17` and `18`. Answer ASK DESK 1. Fill each prompt's launch-row placeholder and the FILL AT LAUNCH values. Launch `17` (acceptEdits) only while the lock is free. Launch `18` once `17` is BUILT.

DRC MERGE FIX R1 DRAFTED · FIX: 8 · NOT REAL: 0 · UNPROVEN: 2 · OUT OF SCOPE: 1 · OWNER ITEM: 0 · code change: tests only · prompts: 2 · new rule strings: 0 · ESCALATE: 1
