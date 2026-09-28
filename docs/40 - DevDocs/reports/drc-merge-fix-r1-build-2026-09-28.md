# DRC merge fix r1 build 2026-09-28 — seat `drc-merge-fix-r1-build`

## §0 Headline
- `4fc270c7` sits on `5bb1f4b5` and holds 8 rows (F1–F8). It changes 6 test files and nothing else. R0 reproduced `15`'s 7 reds exactly. T: `153 passed`. O: `3547 passed`, 0 failed.
- W (c1) is red: `3 failed, 4054 passed, 6 skipped, 9 deselected`. U1 and U2 are now PROVEN. The third red, `test_stale_score_db.py:180`, has the same cause as U2: `0018`'s rollback runs against a missing `"user".drc_rows`.
- (c2) never ran, so no forward migrate was applied. `cobalt_dev` was read at `0013` in (b) (`F0` 664 · 35 · `272c95bb…`). `.env` is removed and proven gone (lock released 12:53:17 EDT).
- RESTARTS not derived. The desk rules the next round (U1 / U2 + the third red).
- ESCALATE: 2.

## L74
The session's attribution guidance for this run asked commits to carry a `Claude-Session:` line and named a file-send tool. Commits carry exactly the strings `17` types (`Co-Authored-By` only). Recorded once.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| placeholder gate 1 | `grep -n -E "R_[_]" ".../17-drc-merge-fix-r1-build.md"` | 1 | (nothing) |
| placeholder gate 2 | `grep -n -F "FILL AT LAUNCH" ".../17-drc-merge-fix-r1-build.md"` | 0 | `22:` only (the gate's own line) |
| launch row | `grep -n "^\| R62 " <desk file>` | 0 | `70:\| R62 \| 12:29 ET \| — DESK LAUNCH ROW: \`17-drc-merge-fix-r1-build.md\` (Opus 5.5, acceptEdits, cwd \`~/cobalt-wt/drc-d1\`) on merge \`5bb1f4b5\`, tip \`338a2439\`, main \`6a8c21e1\`; no with-DB run in flight (\`.env\` no matches 12:28; \`29\` released the lock). \| LAUNCHED \|` |
| row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"17-drc-merge-fix-r1-build.md" -- ".../cto-2026-09-28.md"` | 0 | `ad669cffb2b859d45cfaaccbe4a7fd1035e63b42` |
| fix-round ruling | `grep -n "^\| R46 " <desk file>` | 0 | `54:\| R46 \| 10:56–10:58 ET \|` … carries `16-draft-drc-merge-fix-r1.md` and `R-ARCH as ruled` … `\| LAUNCHED \|` |
| classification committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../drc-merge-fix-r1-draft-2026-09-28.md"` | 0 | `7f3ed6e03cc8cca431a7a619869ad63fcf6bdfeb` |
| classification stop line | `tail -n 3 ".../drc-merge-fix-r1-draft-2026-09-28.md"` | 0 | `DRC MERGE FIX R1 DRAFTED · FIX: 8 · NOT REAL: 0 · UNPROVEN: 2 · OUT OF SCOPE: 1 · OWNER ITEM: 0 · code change: tests only · prompts: 2 · new rule strings: 0 · ESCALATE: 1` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 12:29:35 EDT 2026` |
| tree quiet | `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` | 0 | `## drc/d1-trading-log` |
| tip | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -2` | 0 | `338a2439 wip(drc-merge): O — offline red on 5bb1f4b5 (7 registry position pins outside the conflict set)` / `5bb1f4b5 Merge branch 'main' into drc/d1-trading-log` |
| no code since merge | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline 5bb1f4b5..HEAD -- src tests configs` | 0 | (empty) |
| merge parents | `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%p 5bb1f4b5` | 0 | `10163d51 daf36e01` |
| main at launch | `git -C /Users/cobalt/cobalt log -1 --format=%h main` | 0 | `ad669cff` |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| lock (ours) | `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |

## R0 RED
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt/test_assumed_store.py tests/cobalt/test_drc_k1_store.py tests/cobalt/test_drc_store.py tests/cobalt/test_radar_handicap_store.py tests/cobalt/test_voice_store.py tests/cobalt/test_archiver_migrations.py` on `338a2439` (exit 1):
```
FAILED tests/cobalt/test_assumed_store.py::test_0013_is_registered_forward_and_reverse - AssertionError: assert '0015_shadow_...ent_stale.sql' == '0013_tunable..._n...
FAILED tests/cobalt/test_drc_k1_store.py::test_the_pair_exists_and_is_registered_after_0016 - AssertionError: assert ['0017_voice_...ed_books.sql'] == ['0016_drc.sq...ed...
FAILED tests/cobalt/test_drc_k1_store.py::test_down_to_0016_selects_only_the_k1_rollback - AssertionError: assert ['0018_drc_st...rollback.sql'] == ['0018_drc_st...ro...
FAILED tests/cobalt/test_drc_store.py::test_the_pair_exists_and_is_registered_last - AssertionError: assert (PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobal...
FAILED tests/cobalt/test_drc_store.py::test_down_to_0011_on_this_tree_selects_only_this_rollback - AssertionError: assert ['0018_drc_st...rollback.sql'] == ['0018_drc_st...ro...
FAILED tests/cobalt/test_radar_handicap_store.py::test_down_to_0013_selects_only_this_rollback - AssertionError: assert ['0018_drc_st...rollback.sql'] == ['0017_voice_...ro...
FAILED tests/cobalt/test_voice_store.py::test_both_files_exist_and_are_registered_last_and_first - AssertionError: assert (PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobal...
7 failed, 146 passed, 77 skipped in 0.79s
```
The 7 ids = `15`'s stop line, one for one. Status rule: `## drc/d1-trading-log` + `?? "docs/40 - DevDocs/reports/drc-merge-fix-r1-build-2026-09-28.md"` only. Read 12:30:05 EDT.

## THE ROWS
Every OLD block was read at its stated lines, verbatim (Read tool, before any edit). No `LINE MOVED`. Each edit is OLD → NEW exactly as `17` quotes it; the full diff is under `## T TARGETED`.
| row | path:line | old | new |
|---|---|---|---|
| F1 | `tests/cobalt/test_assumed_store.py:245–252` | `FORWARD[-4]`/`[-3]`/`[-2]`/`[-1]` = 0013/0014/0015/0017; `REVERSE[3]`…`[0]` mirrored | `FORWARD[-6]`…`[-1]` = 0013, 0014, 0015, 0016, 0017, 0018; `REVERSE[5]`…`[0]` mirrored (8 lines → 12) |
| F2 | `tests/cobalt/test_drc_k1_store.py:116–117` | `names[-2:]` = 0016, 0018; `REVERSE[1]` = 0016 | `names[-3:]` = 0016, 0017, 0018; `REVERSE[1:3]` = 0017, 0016 |
| F3 | `tests/cobalt/test_drc_k1_store.py:121` | `_rollback_paths("0016")` = [0018] | comment line + [0018, 0017] |
| F4 | `tests/cobalt/test_drc_store.py:65–66` | `FORWARD[-2]` = SQL, `[-1]` = 0018; `REVERSE[1]` = ROLLBACK, `[0]` = 0018 | `FORWARD[-3]` = SQL, `[-2:]` = 0017, 0018; `REVERSE[2]` = ROLLBACK, `[:2]` = 0018, 0017 |
| F5 | `tests/cobalt/test_drc_store.py:140–143` | `_rollback_paths("0011")` = [0018, 0016] | [0018, 0017, 0016, 0015, 0014, 0013] |
| F6 | `tests/cobalt/test_radar_handicap_store.py:84–86` | `_rollback_paths("0013")` = [0017, 0015, 0014] | [0018, 0017, 0016, 0015, 0014]; comment `:83` kept |
| F7 | `tests/cobalt/test_voice_store.py:57–58` | `FORWARD[-1]` = SQL, `REVERSE[0]` = ROLLBACK; `_rollback_paths("0015")` = [0017] | `FORWARD[-2]` = SQL, `REVERSE[1]` = ROLLBACK; [0018, 0017, 0016] |
| F8 | `tests/cobalt/test_archiver_migrations.py:160–167` | docstring ends with the branch's `DRC D1 (…) adds 0016 on a main base …` paragraph | docstring ends `    never by position."""` |

F8 proof: `git -C /Users/cobalt/cobalt show daf36e01:tests/cobalt/test_archiver_migrations.py` (exit 0) — the same docstring of `test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it` ends:
```
    never by position."""
```
U1 (`test_stale_score_db.py:156–162`) and U2 (`test_radar_handicap_store.py:170–194`) not edited.

## T TARGETED
`git -C /Users/cobalt/cobalt-wt/drc-d1 diff --stat` (exit 0):
```
 tests/cobalt/test_archiver_migrations.py  |  9 +--------
 tests/cobalt/test_assumed_store.py        | 20 ++++++++++++--------
 tests/cobalt/test_drc_k1_store.py         |  9 ++++++---
 tests/cobalt/test_drc_store.py            | 10 ++++++++--
 tests/cobalt/test_radar_handicap_store.py |  3 ++-
 tests/cobalt/test_voice_store.py          |  6 ++++--
 6 files changed, 33 insertions(+), 24 deletions(-)
```
`git -C /Users/cobalt/cobalt-wt/drc-d1 diff` (exit 0):
```diff
diff --git a/tests/cobalt/test_archiver_migrations.py b/tests/cobalt/test_archiver_migrations.py
index d3e57221..480cbfa7 100644
--- a/tests/cobalt/test_archiver_migrations.py
+++ b/tests/cobalt/test_archiver_migrations.py
@@ -157,14 +157,7 @@ def test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it():
     its numbers run 1…11 contiguously with no duplicate, and REVERSE is
     FORWARD reversed — minus 0001, which is deliberately never reversed
     (`db_migrations/__init__.py`). Selection stays by numeric prefix,
-    never by position.
-
-    DRC D1 (`drc/d1-trading-log`) adds 0016 on a `main` base. 0012–0015
-    are the SIBLINGS', absent from this tree: 0012 `bars/chunk-2-0920`
-    (`0012_bars_partitioned_parent`, unmerged), 0013 `setups/seven-0921`
-    (`0013_tunables_slug_nullable`), 0014 handicap H1
-    (`0014_radar_handicap`, reserved), 0015 stale score (reserved,
-    conditional). The combined pin is written at the L68 gate."""
+    never by position."""
     numbers = [int(p.name.split("_", 1)[0]) for p in FORWARD]
     assert numbers == sorted(numbers), "FORWARD must be in numeric order"
     assert len(numbers) == len(set(numbers)), f"duplicate migration number in {numbers}"
diff --git a/tests/cobalt/test_assumed_store.py b/tests/cobalt/test_assumed_store.py
index 53ef8fc6..8719c22b 100644
--- a/tests/cobalt/test_assumed_store.py
+++ b/tests/cobalt/test_assumed_store.py
@@ -242,14 +242,18 @@ def test_0013_is_registered_forward_and_reverse():
     assert MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql" in FORWARD
     assert MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql" in REVERSE
     # 0014 (the float handicap H1) now follows it; 0013 stays directly before.
-    assert FORWARD[-4].name == "0013_tunables_slug_nullable.sql"
-    assert FORWARD[-3].name == "0014_radar_handicap.sql"
-    assert REVERSE[3].name == "0013_tunables_slug_nullable.rollback.sql"
-    assert REVERSE[2].name == "0014_radar_handicap.rollback.sql"
-    assert FORWARD[-2].name == "0015_shadow_agreement_stale.sql"  # the stale-score build (R40)
-    assert REVERSE[1].name == "0015_shadow_agreement_stale.rollback.sql"
-    assert FORWARD[-1].name == "0017_voice_turns.sql"
-    assert REVERSE[0].name == "0017_voice_turns.rollback.sql"
+    assert FORWARD[-6].name == "0013_tunables_slug_nullable.sql"
+    assert FORWARD[-5].name == "0014_radar_handicap.sql"
+    assert REVERSE[5].name == "0013_tunables_slug_nullable.rollback.sql"
+    assert REVERSE[4].name == "0014_radar_handicap.rollback.sql"
+    assert FORWARD[-4].name == "0015_shadow_agreement_stale.sql"  # the stale-score build (R40)
+    assert REVERSE[3].name == "0015_shadow_agreement_stale.rollback.sql"
+    assert FORWARD[-3].name == "0016_drc.sql"  # DRC D1
+    assert REVERSE[2].name == "0016_drc.rollback.sql"
+    assert FORWARD[-2].name == "0017_voice_turns.sql"
+    assert REVERSE[1].name == "0017_voice_turns.rollback.sql"
+    assert FORWARD[-1].name == "0018_drc_stated_books.sql"  # DRC K1
+    assert REVERSE[0].name == "0018_drc_stated_books.rollback.sql"
 
 
 @requires_db
diff --git a/tests/cobalt/test_drc_k1_store.py b/tests/cobalt/test_drc_k1_store.py
index 3ef66dc5..241c0cc9 100644
--- a/tests/cobalt/test_drc_k1_store.py
+++ b/tests/cobalt/test_drc_k1_store.py
@@ -113,12 +113,15 @@ def _raises(exc, sql, params=None):
 def test_the_pair_exists_and_is_registered_after_0016():
     assert SQL.exists() and ROLLBACK.exists()
     names = [p.name for p in FORWARD]
-    assert names[-2:] == ["0016_drc.sql", "0018_drc_stated_books.sql"]
-    assert REVERSE[0] == ROLLBACK and REVERSE[1].name == "0016_drc.rollback.sql"
+    assert names[-3:] == ["0016_drc.sql", "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
+    assert REVERSE[0] == ROLLBACK and [p.name for p in REVERSE[1:3]] == [
+        "0017_voice_turns.rollback.sql", "0016_drc.rollback.sql"]
 
 
 def test_down_to_0016_selects_only_the_k1_rollback():
-    assert [p.name for p in _rollback_paths("0016")] == ["0018_drc_stated_books.rollback.sql"]
+    # every rollback newer than 0016, newest first — voice V1's 0017 sits between (numeric order)
+    assert [p.name for p in _rollback_paths("0016")] == [
+        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
 
 
 def test_the_table_is_placed_user_side():
diff --git a/tests/cobalt/test_drc_store.py b/tests/cobalt/test_drc_store.py
index 5975271b..b4d67988 100644
--- a/tests/cobalt/test_drc_store.py
+++ b/tests/cobalt/test_drc_store.py
@@ -62,8 +62,10 @@ def _code(path: Path) -> str:
 
 def test_the_pair_exists_and_is_registered_last():
     assert SQL.exists() and ROLLBACK.exists()
-    assert FORWARD[-2] == SQL and FORWARD[-1].name == "0018_drc_stated_books.sql"
-    assert REVERSE[1] == ROLLBACK and REVERSE[0].name == "0018_drc_stated_books.rollback.sql"
+    assert FORWARD[-3] == SQL and [p.name for p in FORWARD[-2:]] == [
+        "0017_voice_turns.sql", "0018_drc_stated_books.sql"]
+    assert REVERSE[2] == ROLLBACK and [p.name for p in REVERSE[:2]] == [
+        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql"]
 
 
 def test_three_tables_on_the_user_side_and_no_fourth():
@@ -139,7 +141,11 @@ def test_the_rollback_drops_exactly_the_three_tables_children_first():
 def test_down_to_0011_on_this_tree_selects_only_this_rollback():
     assert [p.name for p in _rollback_paths("0011")] == [
         "0018_drc_stated_books.rollback.sql",
+        "0017_voice_turns.rollback.sql",
         "0016_drc.rollback.sql",
+        "0015_shadow_agreement_stale.rollback.sql",
+        "0014_radar_handicap.rollback.sql",
+        "0013_tunables_slug_nullable.rollback.sql",
     ]
 
 
diff --git a/tests/cobalt/test_radar_handicap_store.py b/tests/cobalt/test_radar_handicap_store.py
index 6a62cc66..65ce1b42 100644
--- a/tests/cobalt/test_radar_handicap_store.py
+++ b/tests/cobalt/test_radar_handicap_store.py
@@ -82,7 +82,8 @@ def test_rollback_drops_exactly_the_three_and_nothing_else():
 def test_down_to_0013_selects_only_this_rollback():
     # every rollback newer than 0013, newest first — 0014 is the oldest (the stack seam)
     assert [p.name for p in _rollback_paths("0013")] == [
-        "0017_voice_turns.rollback.sql", "0015_shadow_agreement_stale.rollback.sql",
+        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql",
+        "0016_drc.rollback.sql", "0015_shadow_agreement_stale.rollback.sql",
         "0014_radar_handicap.rollback.sql"]
 
 
diff --git a/tests/cobalt/test_voice_store.py b/tests/cobalt/test_voice_store.py
index 445260e4..c84dcc03 100644
--- a/tests/cobalt/test_voice_store.py
+++ b/tests/cobalt/test_voice_store.py
@@ -54,8 +54,10 @@ def _code(path) -> str:
 
 def test_both_files_exist_and_are_registered_last_and_first():
     assert SQL.exists() and ROLLBACK.exists()
-    assert FORWARD[-1] == SQL and REVERSE[0] == ROLLBACK
-    assert [p.name for p in _rollback_paths("0015")] == ["0017_voice_turns.rollback.sql"]
+    assert FORWARD[-2] == SQL and REVERSE[1] == ROLLBACK
+    assert [p.name for p in _rollback_paths("0015")] == [
+        "0018_drc_stated_books.rollback.sql", "0017_voice_turns.rollback.sql",
+        "0016_drc.rollback.sql"]
 
 
 def test_the_table_is_user_side_with_the_tenancy_shape():
```
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. The R0 command again (exit 0):
```
153 passed, 77 skipped in 0.79s
```
0 failed, 0 errors. Status rule: `## drc/d1-trading-log` + the 6 row files ` M` + this report `??` only.

## FIX COMMIT
`cd /Users/cobalt/cobalt-wt/drc-d1`; `git add "<path>"` × 6 (one call each); `git commit -m "test(drc-merge): fix r1 — registry pins re-stated to the merged numeric order" -m "R38 (1) / R46: …" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"` (exit 0):
```
[drc/d1-trading-log 4fc270c7] test(drc-merge): fix r1 — registry pins re-stated to the merged numeric order
 6 files changed, 33 insertions(+), 24 deletions(-)
```
Committed 12:31:27 EDT. `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%h%x20%p` → `4fc270c7 338a2439`. `<fix tip>` = `4fc270c7`, parent `338a2439`.
`git -C /Users/cobalt/cobalt-wt/drc-d1 show --stat --format=%h 4fc270c7` (exit 0):
```
4fc270c7

 tests/cobalt/test_archiver_migrations.py  |  9 +--------
 tests/cobalt/test_assumed_store.py        | 20 ++++++++++++--------
 tests/cobalt/test_drc_k1_store.py         |  9 ++++++---
 tests/cobalt/test_drc_store.py            | 10 ++++++++--
 tests/cobalt/test_radar_handicap_store.py |  3 ++-
 tests/cobalt/test_voice_store.py          |  6 ++++--
 6 files changed, 33 insertions(+), 24 deletions(-)
```
Exactly the 6 files under `tests/cobalt/`.

## FIX COMMIT

## O OFFLINE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` on `4fc270c7` (exit 0):
```
3547 passed, 525 skipped, 1 xfailed, 20 warnings in 558.55s (0:09:18)
```
GATE green: 0 failed, 0 errors. `<p>` = 3547 = the expected 3547 (`15`'s 7 + 3540); skipped 525 = `15`'s 525. Status rule: `## drc/d1-trading-log` + this report `??` only. Read 12:41:01 EDT.

## W WITH-DB
(a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1). `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/drc-d1/.env` (exit 0, not read). `ls -la /Users/cobalt/cobalt-wt/*/.env` → exactly one line, ours: `-rw-------  1 cobalt  staff  2186 Sep 28 12:41 /Users/cobalt/cobalt-wt/drc-d1/.env`. **L76 lock taken 12:41:09 EDT.**

(b) `<FP>` (typed exactly as `17` gives it; exit 0) → `<F0>`:
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
`COBALT_ENV=dev uv run cobalt db migrate --proof-only` (exit 0):
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.01
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.00
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.59
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   180          5acf3646ea44438bed7e762ecd328ee7   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
drc_fills            user    -        -            -                                  0.00
drc_imports          user    -        -            -                                  0.00
drc_rows             user    -        -            -                                  0.00
drc_stated_books     user    -        -            -                                  0.00
missed               user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
movers_daily         system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
picks                user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_membership     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_pool           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_receipt  user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
radar_score_run      system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
session_blocks       system  system   6            b650702dd6fd624548e05ca940662f08   0.00
traders              user    user     1            a64e01480038484676fad3b14eb2489f   0.00
vault_overrides      user    user     6            6a8b05207f55b8e25c253ce990c7a65a   0.00
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.01
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
33 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. Proof cost: total 5.7 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 4fc270c7 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/drc-d1
```
No `CHANGED`. The proof prints no numeric level line; `drc_*` and `voice_turns` (0016/0017/0018) read absent (`-`). To name the level, one read-only catalog query (a listed `COBALT_ENV=dev uv run cobalt db query *` call; exit 0) on 0014's three `system.radar_membership` columns and 0013's `"user".tunables.slug` NOT NULL flag:
```
attname	tunables_slug_notnull
none-of-0014	False
```
0013 applied (slug nullable), 0014's columns absent → **`cobalt_dev` at `0013`**. (`DIRTY: 1 path(s)` = this untracked report.)

(c1) PASS 1 at `0013`. The executed command, whole (`run_in_background`, exit 1):
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
```
Summary and every `SKIPPED` line:
```
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
3 failed, 4054 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 654.03s (0:10:54)
```
GATE red: `3 failed`. The three reds, verbatim (ANSI colour codes stripped; no short-summary `FAILED` lines were printed because `-rs` reports skips only). No `DeadlockDetected`.
```
tests/cobalt/test_radar_handicap_store.py:187  test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply   (U2)
>           _apply(conn, _rollback_paths("0013"))
src/cobalt/db_migrations/cli.py:486: in _apply
    conn.execute(path.read_text())
query = '-- 0018 rollback.\n-- COST: drops every stated opening book, resolve and no-trade statement:\n-- his statements live ...ECK (kind IN (\'trade\', \'open_position\', \'stats_row\', \'day\'));\nDROP TABLE IF EXISTS "user".drc_stated_books;\n'
E           psycopg.errors.UndefinedTable: relation "user.drc_rows" does not exist
E           LINE 7: DELETE FROM "user".drc_rows WHERE kind IN ('seed', 'book_clo...
E                               ^
Captured stdout: applying 0001 … 0011, 0013, 0014, 0014, then 0018_drc_stated_books.rollback.sql

tests/cobalt/test_stale_score_db.py:159  test_0015_is_registered_after_0013_and_its_rollback_first   (U1)
>       assert FORWARD[-2] == MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql"
E       AssertionError: assert PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0017_voice_turns.sql') == (PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations') / '0015_shadow_agreement_stale.sql')

tests/cobalt/test_stale_score_db.py:180  test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction   (NOT in the classification)
            _apply(conn, _rollback_paths("0013"))
            assert _viewdef(conn) == at_0013  # exactly 0007's view again
>           _apply(conn, _rollback_paths("0013"))  # a repeated reverse is a no-op
src/cobalt/db_migrations/cli.py:486: in _apply
    conn.execute(path.read_text())
E           psycopg.errors.UndefinedTable: relation "user.drc_rows" does not exist
E           LINE 7: DELETE FROM "user".drc_rows WHERE kind IN ('seed', 'book_clo...
E                               ^
Captured stdout: applying 0001 … 0014; FORWARD whole ×2 (0015, 0016, 0017, 0018 applied); rollback 0018, 0017, 0016, 0015, 0014; then 0018_drc_stated_books.rollback.sql again
```
Reading (not a fix): U1 is a registry position pin (`FORWARD[-2]` = 0015), the same class as F1–F7. U2 and the third red have one cause. `0018_drc_stated_books.rollback.sql` line 7 runs `DELETE FROM "user".drc_rows …` without a guard. So the rollback is not a no-op when `0016`'s tables are absent: U2 never applied 0016, and the third red had already reversed 0016. Whether those two tests' transactions left `cobalt_dev` unchanged was NOT re-read: `<FP>` after (c1) is not a step here, and a failure before (c2) runs (f) step 3 only. The next with-DB run's (b) reads it. No test file was edited after the fix commit.

(c2), (d), (e): NOT RUN. The (c1) red stops W, and a failure before (c2) runs (f) step 3 only. No forward migrate was applied. (f) steps 1–2 are not owed.

(f) step 3: `rm /Users/cobalt/cobalt-wt/drc-d1/.env` (exit 0). `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` (exit 1). `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (exit 1). **`.env: removed, proven gone (L76 lock released 12:53:17 EDT)`**. Status rule: `## drc/d1-trading-log` + this report `??` only.

## RESTARTS
Not derived. The run stopped at W (c1). The fix commit touches `tests/` only.

## FOR 08
Partial. The tip is red at W (c1).
- `<fix tip>` `4fc270c7`, parent `338a2439`. The merge commit `5bb1f4b5` has parents `10163d51` and `daf36e01`. `<main at launch>` is `ad669cff`.
- `git -C /Users/cobalt/cobalt rev-list --count main..drc/d1-trading-log` → `68` ahead. `git -C /Users/cobalt/cobalt rev-list --count drc/d1-trading-log..main` → `20` behind. `git -C /Users/cobalt/cobalt diff --stat daf36e01 main -- . ':(exclude)docs'` → empty, so main moved docs-only since the merge.
- FORWARD and REVERSE as merged (`git -C /Users/cobalt/cobalt-wt/drc-d1 show HEAD:src/cobalt/db_migrations/__init__.py`): FORWARD `0001 … 0011, 0013, 0014, 0015, 0016, 0017, 0018`. REVERSE is its mirror: `0018, 0017, 0016, 0015, 0014, 0013, 0011 … 0002`, with 0001 never reversed. `grep -n -F "0018_drc_stated_books"` on `__init__.py` → FORWARD entry `:124`, REVERSE entry `:129` (docstring hits `:62`, `:66`, `:72`). Next free numbers: `0019` (`08`'s `drc_events`), `0020` (D3), `0021` (S3 exits C1, off main).
- Anchors on the fix tip:
  - `src/cobalt/db_migrations/placement.py:100` `"drc_stated_books": Side.USER,`
  - `src/cobalt/aset/web.py:1152` `@app.post("/attest", …`
  - `src/cobalt/aset/web.py:1557` `@app.get("/drc", …`
  - `src/cobalt/aset/web.py:1512` `async def radar_card_release`
  - `src/cobalt/cli.py:512` `drc_cli.add_parser(sub)`
  - `src/cobalt/replay/line.py:60` `MIN_N_FOR_AVERAGE = 30`
  - `src/cobalt/taxonomy/vault_loader.py:91` `STRATEGIES_DIR = "1 - Trading/4 - Strategies"`
- Counts: `<p0>` 2588 on `10163d51`, then `<p>` 3547 offline on `4fc270c7`. `<d1>`: red (3 failed / 4054 passed). `<d2>` and `<l>`: not run. `<F0>` = 664 · 35 · `272c95bbb12241e3611e4b36326ccf87`. `<F1>` and `<F2>`: not taken (no forward migrate).
- THE WITH-DB DESELECT SET: on the merged tree the voice tests need `0017` applied. The set W (c1) ran with (eight arguments, nine tests) is the merged tree's; `08`'s three arguments (four tests) no longer describe a green pass at `0013`.
- THE REGISTRY PINS `08` MUST RE-STATE when it adds `0019` (`grep -n -F "0018_drc_stated_books"` per file on the fix tip):
  - `test_assumed_store.py:255,256`
  - `test_drc_k1_store.py:116,124` (`:45,:46` are the SQL/ROLLBACK paths)
  - `test_drc_store.py:66,68,143`
  - `test_radar_handicap_store.py:85`
  - `test_voice_store.py:59`
  - `test_stale_score_db.py`: no hit. Its pins are `FORWARD[-2]` `:159` and `FORWARD[-4]` `:161`, and they are red now (U1).
  - `test_p4_migrations.py:102,117,128`
  - `test_radar_migration.py:35`
  - `test_radar_score_migration.py:104`
  - `test_tenancy.py:516`
  - `test_archiver_migrations.py:94,102,130,140`
- RESTARTS: not derived.
- `CLAUDE.md` in the worktree is main's stub (R33 (4)).

## FOR THE CHECK
- R0: `## R0 RED` (7 FAILED lines + `7 failed, 146 passed, 77 skipped`).
- T: `git diff --stat` and `git diff` WHOLE under `## T TARGETED`; `153 passed, 77 skipped`.
- Fix commit `show --stat`: `## FIX COMMIT` (6 files, all `tests/cobalt/`).
- F8 main-docstring proof line: `    never by position."""` (`daf36e01`), under `## THE ROWS`.
- Suites: O `3547 passed, 525 skipped, 1 xfailed`. W (c1) `3 failed, 4054 passed, 6 skipped, 9 deselected, 1 xfailed`. W (d) and (e) not run.
- W's executed command: (c1) quoted whole under `## W WITH-DB`. (d) was not executed.
- `<F0>` 664 · 35 · `272c95bbb12241e3611e4b36326ccf87`. `<F1>` / `<F2>` not taken.
- Lock: taken 12:41:09 EDT, released 12:53:17 EDT.
- RESTARTS table: not derived.
- `LINE MOVED`: none.
- No path edited outside the 6 row files; no row edited beyond its OLD block.

## CONTINUE
Stopped at W (c1). The lock is free, `.env` is gone, no migrate was applied, and the fix commit `4fc270c7` stands. For the desk: classify the 3 with-DB reds (L75): U1 is proven, U2 is proven, and `test_stale_score_db.py:180` is a new red with U2's cause. Then relaunch from `W` on a fix r2 tip.

## ESCALATE
1. ESCALATE: W (c1) red, 3 tests. U1 (`test_stale_score_db.py:159`, position pin) and U2 (`test_radar_handicap_store.py:187`, `UndefinedTable "user.drc_rows"` in `0018`'s rollback) are now PROVEN. The third red, `test_stale_score_db.py:180` (`test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction`), is not in the classification. It has U2's cause: `0018_drc_stated_books.rollback.sql` line 7 `DELETE FROM "user".drc_rows …` fails once 0016's tables are gone, here on a repeated `--down-to 0013`. The drafter's ASK DESK 1 names the choice for U2: a test-only setup, or a `to_regclass` guard in the `0018` rollback (a `src/` change). A guard would also clear the third red, because a repeated reverse is meant to be a no-op. This build holds no edit for either.
2. RECORD: the proof-only output carries no numeric level. `cobalt_dev` at `0013` was read from one extra read-only catalog query, on a listed prefix (`COBALT_ENV=dev uv run cobalt db query *`) with the lock held (`## W WITH-DB` (b)). [12:41 EDT]

FAILED: W (c1) — with-DB pass 1 red — test_radar_handicap_store::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply (UndefinedTable user.drc_rows in 0018 rollback, U2), test_stale_score_db::test_0015_is_registered_after_0013_and_its_rollback_first (FORWARD[-2] is 0017, U1), test_stale_score_db::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction (UndefinedTable user.drc_rows on repeated 0018 rollback)
