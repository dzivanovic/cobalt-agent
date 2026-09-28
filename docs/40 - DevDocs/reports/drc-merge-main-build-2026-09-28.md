# DRC merge-main build 2026-09-28 — seat `drc-merge-main-build`

## §0 Headline
- `5bb1f4b5` = main `daf36e01` merged into `10163d51`. The 12 expected conflicts were resolved by rule. Main moved docs-only during the build.
- E0 on `10163d51`: `2588 passed`. O on `5bb1f4b5`: `7 failed, 3540 passed` → FAILED at O.
- The 7 reds are single-side position pins on the migration registry (`test_assumed_store`, `test_drc_k1_store` ×2, `test_drc_store` ×2, `test_radar_handicap_store`, `test_voice_store`), outside `## BOTH-SIDES`.
- W not run. No lock taken, no `.env`, `cobalt_dev` untouched. The merge commit stays; the desk rules a fix round (R38 (5)).
- ESCALATE: 3.

## L74
A block arrived appended to the Read tool result of this prompt (`15-drc-merge-main-build.md`): it asked every commit to carry a `Claude-Session:` line and named a file-send tool. Data, not followed; commits carry `Co-Authored-By` only, as `15` types them. Recorded once.

## AUTHORIZATION
| rule | command | exit | output |
|---|---|---|---|
| placeholder gate | `grep -n -E "R_[_]" ".../15-drc-merge-main-build.md"` | 1 | (nothing) |
| launch row | `grep -n "^\| R41 " <desk file>` | 0 | `:49` R41 10:29 ET — names `15-drc-merge-main-build.md`, `10163d51`, carries `no with-DB run in flight`; `APPROVED — LAUNCHING` |
| row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"15-drc-merge-main-build.md" -- ".../cto-2026-09-28.md"` | 0 | `af66bfe1827aea15030427c79dcf5696fd645cdf` |
| his approval | `grep -n -F "git merge --no-ff --no-edit main" <desk file>` | 0 | `:47` R39 10:11 ET — `P-HIS — "approved"` → both NEW strings APPROVED (also `:45`, `:46`, `:49`) |
| merge call | `grep -n "^\| R33 " <desk file>` | 0 | `:41` R33 — `(1) MERGE \`main\` INTO \`drc/d1-trading-log\` BEFORE \`08\`` |

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| date | `date` | 0 | `Mon Sep 28 10:29:11 EDT 2026` |
| tree quiet | `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` | 0 | `## drc/d1-trading-log` |
| branch tip | `git -C /Users/cobalt/cobalt-wt/drc-d1 log --oneline -1` | 0 | `10163d51 docs(drc-d2): DRC D2 build report — 6777c463` |
| main at preflight | `git -C /Users/cobalt/cobalt log -1 --format=%h main` | 0 | `af66bfe1` |
| merge-base | `git -C /Users/cobalt/cobalt merge-base main drc/d1-trading-log` | 0 | `04b05cd4ded1c6e809aae47e70333c17406368ea` |
| behind | `git -C /Users/cobalt/cobalt rev-list --count drc/d1-trading-log..main` | 0 | `607` |
| ahead | `git -C /Users/cobalt/cobalt rev-list --count main..drc/d1-trading-log` | 0 | `65` |
| main migrations | `git -C /Users/cobalt/cobalt show main:src/cobalt/db_migrations/__init__.py` | 0 | FORWARD tail `0011`, `0013`, `0014`, `0015`, `0017`; no `0016`/`0018`–`0021` file entries |
| lock (all) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| lock (ours) | `ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/drc-d1/.env: No such file or directory` |

## E0 BASELINE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` on `10163d51` (exit 0):
```
2588 passed, 493 skipped, 1 xfailed, 15 warnings in 71.69s (0:01:11)
```
`<p0>` = 2588 passed / 0 failed (same as D2's `offline 2588/0`). Recorded 10:41:58 EDT.

## MERGE
`date` → `Mon Sep 28 10:42:06 EDT 2026`. `git merge --no-ff --no-edit main` (exit 1, conflict expected):
```
Auto-merging docs/40 - DevDocs/cobalt/aset/web.md
CONFLICT (content): Merge conflict in docs/40 - DevDocs/cobalt/aset/web.md
Auto-merging docs/40 - DevDocs/cobalt/cli.md
CONFLICT (content): Merge conflict in docs/40 - DevDocs/cobalt/cli.md
Auto-merging docs/40 - DevDocs/cobalt/db_migrations/__init__.md
CONFLICT (content): Merge conflict in docs/40 - DevDocs/cobalt/db_migrations/__init__.md
Auto-merging docs/40 - DevDocs/cobalt/db_migrations/placement.md
CONFLICT (content): Merge conflict in docs/40 - DevDocs/cobalt/db_migrations/placement.md
Auto-merging pyproject.toml
Auto-merging src/cobalt/aset/web.py
Auto-merging src/cobalt/cli.py
Auto-merging src/cobalt/db_migrations/__init__.py
CONFLICT (content): Merge conflict in src/cobalt/db_migrations/__init__.py
Auto-merging src/cobalt/db_migrations/placement.py
CONFLICT (content): Merge conflict in src/cobalt/db_migrations/placement.py
Auto-merging tests/cobalt/test_archiver_migrations.py
CONFLICT (content): Merge conflict in tests/cobalt/test_archiver_migrations.py
Auto-merging tests/cobalt/test_p4_migrations.py
CONFLICT (content): Merge conflict in tests/cobalt/test_p4_migrations.py
Auto-merging tests/cobalt/test_radar_migration.py
CONFLICT (content): Merge conflict in tests/cobalt/test_radar_migration.py
Auto-merging tests/cobalt/test_radar_panel_cards.py
CONFLICT (content): Merge conflict in tests/cobalt/test_radar_panel_cards.py
Auto-merging tests/cobalt/test_radar_score_migration.py
CONFLICT (content): Merge conflict in tests/cobalt/test_radar_score_migration.py
Auto-merging tests/cobalt/test_tenancy.py
CONFLICT (content): Merge conflict in tests/cobalt/test_tenancy.py
Auto-merging uv.lock
Automatic merge failed; fix conflicts and then commit the result.
```
`git -C /Users/cobalt/cobalt-wt/drc-d1 diff --name-only --diff-filter=U`:
```
docs/40 - DevDocs/cobalt/aset/web.md
docs/40 - DevDocs/cobalt/cli.md
docs/40 - DevDocs/cobalt/db_migrations/__init__.md
docs/40 - DevDocs/cobalt/db_migrations/placement.md
src/cobalt/db_migrations/__init__.py
src/cobalt/db_migrations/placement.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_panel_cards.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_tenancy.py
```
= the 12 EXPECTED CONFLICTED exactly. The 4 EXPECTED CLEAN (`aset/web.py`, `cli.py`, `pyproject.toml`, `uv.lock`) auto-merged: R-WEB / R-CLI not invoked; no UNPLANNED path or hunk.

Resolution, per path (Edit only inside markers; each path: `<<<<<<<`, `>>>>>>>`, `=======` greps → nothing; then `git add "<path>"`; after all 12, `diff --name-only --diff-filter=U` → empty):
| path | rule | what was done |
|---|---|---|
| `src/cobalt/db_migrations/__init__.py` | R-MIG | docstring entries 0013–0018 numeric; main's `0012 AND 0016` gap paragraph kept, branch's `0012–0015` paragraph dropped; FORWARD `…0011, 0013, 0014, 0015, 0016, 0017, 0018`; REVERSE `0018, 0017, 0016, 0015, 0014, 0013, 0011…0002` |
| `src/cobalt/db_migrations/placement.py` | R-PLACE | `CREATED_TABLES` tail: 0016 block, 0017 `voice_turns`, 0018 block; the branch's `DECLARED_TABLES` edit merged clean |
| `tests/cobalt/test_archiver_migrations.py` | R-ARCH | `FORWARD[-10:]`, `REVERSE[:10]`, `_rollback_paths("0009")` / `("0007")` begin `0018…0013`; pin `[*range(1, 12), 13, 14, 15, 16, 17, 18]`, `numbers[-8:-6] == [10, 11]`, `numbers[-1] == 18`; main's comment block kept; survivors exclude `NEW_TABLES`, `P4_TABLES`, `DRC_D1_TABLES`, `"voice_turns"` (main's comment kept; the branch's comment above the set is outside the hunk and stays) |
| `tests/cobalt/test_p4_migrations.py` | R-PINS | three lists begin `0018…0013`, each side's comment on its lines |
| `tests/cobalt/test_radar_migration.py` | R-PINS | `[:10]`, list begins `0018…0013` |
| `tests/cobalt/test_radar_score_migration.py` | R-PINS | list begins `0018…0013`; three `[:10]` slices; the two size comments say ten (`the list is ten now`, `the list is now the newest ten`) |
| `tests/cobalt/test_tenancy.py` | R-PINS | `[:10]`, list begins `0018…0013`; `DrcStore` import + entry merged clean |
| `tests/cobalt/test_radar_panel_cards.py` | R-PANEL | base lines, branch's `/settings/daily…` and `/drc/…` lines, then main's voice comment + three `/voice/*`; `GET_ONLY` the branch's (with `"/drc"`) — merged clean |
| `docs/…/aset/web.md` | R-DOCS | main's voice V1 section, then `---`, then the branch's D4-4 and D2-4 sections |
| `docs/…/cli.md` | R-DOCS | main's voice section, then the branch's K1 section |
| `docs/…/db_migrations/__init__.md` | R-DOCS | main's 0013 / 0014 / 0015 / 0017 sections, then the branch's 0016 and 0018 sections |
| `docs/…/db_migrations/placement.md` | R-DOCS | main's voice section, then the branch's D1 and K1 sections |

`diff --cached main` per resolved path: quoted whole under `## FOR THE CHECK`.

THE MERGE COMMIT: `git commit -m "Merge branch 'main' into drc/d1-trading-log" -m "R33 (1): main merged into the DRC stack before 08; conflicts resolved by rule: 12 paths (15-drc-merge-main-build.md ## BOTH-SIDES)." -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"` → `[drc/d1-trading-log 5bb1f4b5] Merge branch 'main' into drc/d1-trading-log`. `date` → `Mon Sep 28 10:45:28 EDT 2026`.

PROOF:
| read | output |
|---|---|
| `git -C /Users/cobalt/cobalt-wt/drc-d1 log -1 --format=%h%x20%p` | `5bb1f4b5 10163d51 daf36e01` — `<merged tip>` `5bb1f4b5`, first parent `10163d51`, `<main sha>` `daf36e01` |
| `<main sha>` vs `<main at preflight>` | `daf36e01` ≠ `af66bfe1` → `git -C /Users/cobalt/cobalt diff --stat af66bfe1 daf36e01 -- . ':(exclude)docs'` → (empty): main moved with docs only; no ESCALATE |
| delta path sets | both stat blocks (under `## FOR THE CHECK`) list the SAME 66 paths; line counts differ only on `src/cobalt/db_migrations/__init__.py` (24 → 17) and `tests/cobalt/test_radar_score_migration.py` (8 → 10), both resolved paths |

## O OFFLINE
`ls -la /Users/cobalt/cobalt-wt/drc-d1/.env` → `No such file or directory`. `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` on `5bb1f4b5` (exit 1):
```
7 failed, 3540 passed, 525 skipped, 1 xfailed, 20 warnings in 562.87s (0:09:22)
```
GATE red (`7 failed`). Status rule after the first `uv run`: `git -C /Users/cobalt/cobalt-wt/drc-d1 status --short --branch` → `## drc/d1-trading-log` + `?? "docs/40 - DevDocs/reports/drc-merge-main-build-2026-09-28.md"` only (no `uv.lock` change). Read 10:55:48 EDT.

The 7 reds. Each test is OUTSIDE the conflict set: it merged clean from one side and pins that side's tail position. Each assertion, verbatim:
```
tests/cobalt/test_assumed_store.py:245  test_0013_is_registered_forward_and_reverse
>       assert FORWARD[-4].name == "0013_tunables_slug_nullable.sql"
E       AssertionError: assert '0015_shadow_...ent_stale.sql' == '0013_tunable..._nullable.sql'
E         - 0013_tunables_slug_nullable.sql
E         + 0015_shadow_agreement_stale.sql

tests/cobalt/test_drc_k1_store.py:116  test_the_pair_exists_and_is_registered_after_0016
>       assert names[-2:] == ["0016_drc.sql", "0018_drc_stated_books.sql"]
E       AssertionError: assert ['0017_voice_...ed_books.sql'] == ['0016_drc.sq...ed_books.sql']
E         At index 0 diff: '0017_voice_turns.sql' != '0016_drc.sql'

tests/cobalt/test_drc_k1_store.py:121  test_down_to_0016_selects_only_the_k1_rollback
>       assert [p.name for p in _rollback_paths("0016")] == ["0018_drc_stated_books.rollback.sql"]
E       AssertionError: assert ['0018_drc_st...rollback.sql'] == ['0018_drc_st...rollback.sql']
E         Left contains one more item: '0017_voice_turns.rollback.sql'

tests/cobalt/test_drc_store.py:65  test_the_pair_exists_and_is_registered_last
>       assert FORWARD[-2] == SQL and FORWARD[-1].name == "0018_drc_stated_books.sql"
E       AssertionError: assert (PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0017_voice_turns.sql') == PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0016_drc.sql'))

tests/cobalt/test_drc_store.py:140  test_down_to_0011_on_this_tree_selects_only_this_rollback
>       assert [p.name for p in _rollback_paths("0011")] == [
            "0018_drc_stated_books.rollback.sql",
            "0016_drc.rollback.sql",
        ]
E       AssertionError: assert ['0018_drc_st...rollback.sql'] == ['0018_drc_st...rollback.sql']
E         At index 1 diff: '0017_voice_turns.rollback.sql' != '0016_drc.rollback.sql'
E         Left contains 4 more items, first extra item: '0016_drc.rollback.sql'

tests/cobalt/test_radar_handicap_store.py:84  test_down_to_0013_selects_only_this_rollback
>       assert [p.name for p in _rollback_paths("0013")] == [
            "0017_voice_turns.rollback.sql", "0015_shadow_agreement_stale.rollback.sql",
            "0014_radar_handicap.rollback.sql"]
E       AssertionError: assert ['0018_drc_st...rollback.sql'] == ['0017_voice_...rollback.sql']
E         At index 0 diff: '0018_drc_stated_books.rollback.sql' != '0017_voice_turns.rollback.sql'
E         Left contains 2 more items, first extra item: '0015_shadow_agreement_stale.rollback.sql'

tests/cobalt/test_voice_store.py:57  test_both_files_exist_and_are_registered_last_and_first
>       assert FORWARD[-1] == SQL and REVERSE[0] == ROLLBACK
E       AssertionError: assert (PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0018_drc_stated_books.sql') == PosixPath('/Users/cobalt/cobalt-wt/drc-d1/src/cobalt/db_migrations/0017_voice_turns.sql'))
```
Reading (not a fix): every red is a position pin on FORWARD / REVERSE / `_rollback_paths` that the interleaved numeric order (`0016` between `0015` and `0017`, `0018` after `0017`) moves. The drafter's `## BOTH-SIDES` scan counted only files both sides touched, and these 5 files are each touched by ONE side (4 by main, 2 by the branch), so none conflicted and no rule names them. R-MIG itself is as ruled (R38 (1)). Not edited (O: "never an edit"). The merge commit `5bb1f4b5` stays.

## W WITH-DB
Not run: O red stops the run before W. The L76 lock was never taken. `.env` was never copied (`ls -la /Users/cobalt/cobalt-wt/*/.env` → `no matches found`, 10:55). No migrate ran; `cobalt_dev` untouched by this run.

## RESTARTS
Not derived: the run stopped at O.

## FOR 08
Not written whole: the run stopped at O; the tip is red. Known so far: `<merged tip>` `5bb1f4b5`, parents `10163d51` `daf36e01`; FORWARD `…0011, 0013, 0014, 0015, 0016, 0017, 0018`, REVERSE its mirror (see `## FOR THE CHECK`). `CLAUDE.md` in the worktree is now main's stub (R33 (4)).

## FOR THE CHECK
Conflicted list as git printed it: see `## MERGE` (12 paths).

`git -C /Users/cobalt/cobalt-wt/drc-d1 diff --cached main -- <the 8 code/test paths>` (one call, before the merge commit), WHOLE:
```diff
diff --git a/src/cobalt/db_migrations/__init__.py b/src/cobalt/db_migrations/__init__.py
index 8fd654fc..b03a6c26 100644
--- a/src/cobalt/db_migrations/__init__.py
+++ b/src/cobalt/db_migrations/__init__.py
@@ -49,10 +49,23 @@
                          by X30 (A)). Additive: the view only.
 `0015_shadow_agreement_stale.rollback.sql` — the view exactly as 0007
                          defines it.
+`0016_drc.sql` — DRC D1: `"user".drc_imports` (one row per dropped
+                         file, + the input event's state), `drc_fills`
+                         (one row per execution) and the declared
+                         `drc_rows` (trades, open positions, stats rows,
+                         the day — inputs + derived + fn_version). Additive.
+`0016_drc.rollback.sql` — drops those three tables, children first.
 `0017_voice_turns.sql` — `"user".voice_turns`, voice V1's turn rows
                          (voice v3 FINAL §7): the state machine, no audio
                          bytes of any kind. Additive.
 `0017_voice_turns.rollback.sql` — drops that one table.
+`0018_drc_stated_books.sql` — DRC K1: `"user".drc_stated_books` (his
+                         stated opening books, resolves and no-trade
+                         statements; append-only) and `drc_rows.kind`
+                         widened by `seed` / `book_close`. Additive.
+`0018_drc_stated_books.rollback.sql` — deletes the `seed` / `book_close`
+                         rows, restores the four-kind CHECK, drops the
+                         table (his statements with it — its COST line).
 
 0012 AND 0016 ARE NOT GAPS BY ACCIDENT: 0012 belongs to the unmerged
 `bars/chunk-2-0920` (`0012_bars_partitioned_parent`) and 0016 to DRC D1
@@ -106,12 +119,16 @@ FORWARD = (
     MIGRATIONS_DIR / "0013_tunables_slug_nullable.sql",
     MIGRATIONS_DIR / "0014_radar_handicap.sql",
     MIGRATIONS_DIR / "0015_shadow_agreement_stale.sql",
+    MIGRATIONS_DIR / "0016_drc.sql",
     MIGRATIONS_DIR / "0017_voice_turns.sql",
+    MIGRATIONS_DIR / "0018_drc_stated_books.sql",
 )
 
 #: `--rollback`, newest first. 0001 is deliberately NOT reversed.
 REVERSE = (
+    MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql",
     MIGRATIONS_DIR / "0017_voice_turns.rollback.sql",
+    MIGRATIONS_DIR / "0016_drc.rollback.sql",
     MIGRATIONS_DIR / "0015_shadow_agreement_stale.rollback.sql",
     MIGRATIONS_DIR / "0014_radar_handicap.rollback.sql",
     MIGRATIONS_DIR / "0013_tunables_slug_nullable.rollback.sql",
diff --git a/src/cobalt/db_migrations/placement.py b/src/cobalt/db_migrations/placement.py
index 74689bdf..bd3333d8 100644
--- a/src/cobalt/db_migrations/placement.py
+++ b/src/cobalt/db_migrations/placement.py
@@ -86,9 +86,18 @@ CREATED_TABLES: dict[str, Side] = {
     # (L32). `cobalt_user` is granted nothing on either.
     "archive_progress": Side.SYSTEM,
     "archive_incidents": Side.SYSTEM,
+    # db_migrations/0016_drc.sql — DRC D1: his imported files, their
+    # executions, and the derived DRC rows. USER, all three: one trader's
+    # own record (L32). `drc_rows` left DECLARED_TABLES when 0016 built it.
+    "drc_imports": Side.USER,
+    "drc_fills": Side.USER,
+    "drc_rows": Side.USER,
     # db_migrations/0017_voice_turns.sql — voice V1's turn rows (voice v3
     # FINAL §7). USER: one trader's words and the command they ran (L32).
     "voice_turns": Side.USER,
+    # db_migrations/0018_drc_stated_books.sql — DRC K1: his stated opening
+    # books, resolves and no-trade statements. USER: his own word (L32).
+    "drc_stated_books": Side.USER,
 }
 
 #: VIEWS created by database-wide migrations. On a side like any table
@@ -108,10 +117,11 @@ CREATED_VIEWS: dict[str, Side] = {
 #: yet; the placement test only checks tables that DO exist.
 DECLARED_TABLES: dict[str, Side] = {
     # S3 — named now so the placement test knows them on sight. `missed`
-    # left this list when S2-P4's 0009 built it.
+    # left this list when S2-P4's 0009 built it, `drc_rows` when DRC D1's
+    # 0016 did. `fills` stays declared and unbuilt (DRC D1 stores its
+    # executions in `drc_fills`, v2 [F-35]).
     "legs": Side.USER,
     "fills": Side.USER,
-    "drc_rows": Side.USER,
     "prediction_records": Side.USER,
     # S2-P2 — taxonomy anatomy instances (regime, range, gap, extension,
     # leg, session clock). The anatomy IS the system.
diff --git a/tests/cobalt/test_archiver_migrations.py b/tests/cobalt/test_archiver_migrations.py
index dab5cb09..d3e57221 100644
--- a/tests/cobalt/test_archiver_migrations.py
+++ b/tests/cobalt/test_archiver_migrations.py
@@ -49,6 +49,10 @@ NEW_TABLES = ("archive_progress", "archive_incidents")
 #: pins can say which bound owns what instead of asserting "mine only".
 P4_TABLES = ("movers_daily", "picks", "missed")
 
+#: DRC D1's tables (0016) and K1's (0018), numbered ABOVE this branch's
+#: pair: every rollback bound below 0016 reverses them too.
+DRC_D1_TABLES = ("drc_imports", "drc_fills", "drc_rows", "drc_stated_books")
+
 #: §11: the five kinds. `regression` is v3's addition to v2's four.
 INCIDENT_KINDS = ("gap", "restated", "stored_only", "empty_export", "regression")
 
@@ -77,7 +81,7 @@ def test_forward_ends_0008_0009_0010_0011():
     """The tail after the P4 rebase: P4's pair, then this branch's pair,
     in numeric order. The invariant is unchanged — 0010 and 0011 are the
     LAST two registered, and nothing of this branch's was displaced."""
-    assert [p.name for p in FORWARD[-8:]] == [
+    assert [p.name for p in FORWARD[-10:]] == [
         "0008_radar_value_movers.sql",
         "0009_picks_missed.sql",
         "0010_archive_progress.sql",
@@ -85,15 +89,19 @@ def test_forward_ends_0008_0009_0010_0011():
         "0013_tunables_slug_nullable.sql",  # the setups one build (R2-3 = B); 0012 is bars/chunk-2-0920's
         "0014_radar_handicap.sql",  # the float handicap H1 (L72 P-b)
         "0015_shadow_agreement_stale.sql",  # the stale-score build (R40, X30 (A)); 0014 is handicap H1's
+        "0016_drc.sql",  # DRC D1; 0012–0015 are the siblings' (see the registry pin)
         "0017_voice_turns.sql",  # voice V1; 0012 and 0016 are unmerged branches' (L68)
+        "0018_drc_stated_books.sql",  # DRC K1; 0017 is the voice branch's
     ]
 
 
 def test_reverse_begins_0011_0010_0009_0008():
     """The exact mirror of the tail above: this branch's pair reverses
     FIRST, then P4's."""
-    assert [p.name for p in REVERSE[:8]] == [
+    assert [p.name for p in REVERSE[:10]] == [
+        "0018_drc_stated_books.rollback.sql",
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",
         "0015_shadow_agreement_stale.rollback.sql",
         "0014_radar_handicap.rollback.sql",
         "0013_tunables_slug_nullable.rollback.sql",
@@ -119,7 +127,9 @@ def test_rollback_down_to_0009_undoes_this_branch_alone_and_0007_also_reaches_p4
     because selection is by numeric prefix and P4 now sits between.
     Both are pinned so neither can drift."""
     assert [p.name for p in _rollback_paths("0009")] == [
+        "0018_drc_stated_books.rollback.sql",
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",
         "0015_shadow_agreement_stale.rollback.sql",
         "0014_radar_handicap.rollback.sql",
         "0013_tunables_slug_nullable.rollback.sql",
@@ -127,7 +137,9 @@ def test_rollback_down_to_0009_undoes_this_branch_alone_and_0007_also_reaches_p4
         "0010_archive_progress.rollback.sql",
     ]
     assert [p.name for p in _rollback_paths("0007")] == [
+        "0018_drc_stated_books.rollback.sql",
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",
         "0015_shadow_agreement_stale.rollback.sql",
         "0014_radar_handicap.rollback.sql",
         "0013_tunables_slug_nullable.rollback.sql",
@@ -145,7 +157,14 @@ def test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it():
     its numbers run 1…11 contiguously with no duplicate, and REVERSE is
     FORWARD reversed — minus 0001, which is deliberately never reversed
     (`db_migrations/__init__.py`). Selection stays by numeric prefix,
-    never by position."""
+    never by position.
+
+    DRC D1 (`drc/d1-trading-log`) adds 0016 on a `main` base. 0012–0015
+    are the SIBLINGS', absent from this tree: 0012 `bars/chunk-2-0920`
+    (`0012_bars_partitioned_parent`, unmerged), 0013 `setups/seven-0921`
+    (`0013_tunables_slug_nullable`), 0014 handicap H1
+    (`0014_radar_handicap`, reserved), 0015 stale score (reserved,
+    conditional). The combined pin is written at the L68 gate."""
     numbers = [int(p.name.split("_", 1)[0]) for p in FORWARD]
     assert numbers == sorted(numbers), "FORWARD must be in numeric order"
     assert len(numbers) == len(set(numbers)), f"duplicate migration number in {numbers}"
@@ -155,8 +174,9 @@ def test_the_registry_is_an_explicit_contiguous_list_and_reverse_mirrors_it():
     # The stale-score build adds 0015 (R40); 0014 is handicap H1's (same seam).
     # Voice V1 adds 0017; 0012 and 0016 belong to unmerged branches and close
     # the gap as they land (L68 seam).
-    assert numbers == [*range(1, 12), 13, 14, 15, 17], f"1…11 then 13, 14, 15, 17, got {numbers}"
-    assert numbers[-6:-4] == [10, 11], "this branch's pair is still in place"
+    assert numbers == [*range(1, 12), 13, 14, 15, 16, 17, 18], f"1…11 then 13–18, got {numbers}"
+    assert numbers[-8:-6] == [10, 11], "this branch's pair is still in place"
+    assert numbers[-1] == 18, "DRC K1's 0018 is the tail"
     reverse_numbers = [int(p.name.split("_", 1)[0]) for p in REVERSE]
     assert reverse_numbers == sorted(reverse_numbers, reverse=True)
     assert reverse_numbers == [n for n in reversed(numbers) if n != 1], (
@@ -476,18 +496,25 @@ def test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4(
     conn = _migration_conn()
     try:
         _apply(conn, FORWARD)
+        # DRC D1's 0016 and K1's 0018 sit ABOVE both bounds, so each bound reverses them
+        # too (`_rollback_paths` selects by number); its tables are owned
+        # by both rollbacks, never survivors.
         survivors = {
             name
             for name in CREATED_TABLES
             # voice V1's 0017 sits ABOVE both bounds, so both rollbacks
             # correctly drop voice_turns too; it is not a survivor.
-            if name not in NEW_TABLES and name not in P4_TABLES and name != "voice_turns"
+            if name not in NEW_TABLES
+            and name not in P4_TABLES
+            and name not in DRC_D1_TABLES
+            and name != "voice_turns"
             and _regclass(conn, name)
         }
 
-        # (1) THE ARCHIVER'S OWN BOUND: `--down-to 0009` is this branch alone.
+        # (1) THE ARCHIVER'S OWN BOUND: `--down-to 0009` is this branch
+        # (and everything numbered above it) alone.
         _apply(conn, _rollback_paths("0009"))
-        for table in NEW_TABLES:
+        for table in (*NEW_TABLES, *DRC_D1_TABLES):
             assert _regclass(conn, table) is None, f"{table} survived its own rollback"
         for name in P4_TABLES:
             assert _regclass(conn, name), (
@@ -501,7 +528,7 @@ def test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4(
 
         # (2) `--down-to 0007` REACHES P4 TOO, and stops there.
         _apply(conn, _rollback_paths("0007"))
-        for table in (*NEW_TABLES, *P4_TABLES):
+        for table in (*NEW_TABLES, *P4_TABLES, *DRC_D1_TABLES):
             assert _regclass(conn, table) is None, (
                 f"{table} survived --down-to 0007, which reverses everything above 0007"
             )
@@ -512,7 +539,7 @@ def test_rollback_down_to_0009_drops_this_branch_alone_and_0007_also_reaches_p4(
 
         # ...and forward again lands back where it started.
         _apply(conn, FORWARD)
-        for table in (*NEW_TABLES, *P4_TABLES):
+        for table in (*NEW_TABLES, *P4_TABLES, *DRC_D1_TABLES):
             assert _regclass(conn, table), table
     finally:
         conn.rollback()
diff --git a/tests/cobalt/test_p4_migrations.py b/tests/cobalt/test_p4_migrations.py
index ef29de79..5f6e2a18 100644
--- a/tests/cobalt/test_p4_migrations.py
+++ b/tests/cobalt/test_p4_migrations.py
@@ -99,7 +99,9 @@ def test_rollback_down_to_0007_reverses_everything_above_p2_newest_first():
     now reverses all four, newest first. P4's own bound is still pinned
     below it: nothing at or below the bound is ever selected."""
     assert [p.name for p in _rollback_paths("0007")] == [
+        "0018_drc_stated_books.rollback.sql",  # DRC K1
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",  # DRC D1
         "0015_shadow_agreement_stale.rollback.sql",  # the stale-score build (R40, X30 (A))
         "0014_radar_handicap.rollback.sql",  # the float handicap H1
         "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
@@ -112,7 +114,9 @@ def test_rollback_down_to_0007_reverses_everything_above_p2_newest_first():
     above_0009 = [p.name for p in _rollback_paths("0009")]
     assert not [n for n in above_0009 if n.startswith(("0008", "0009"))], above_0009
     assert above_0009 == [
+        "0018_drc_stated_books.rollback.sql",
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",
         "0015_shadow_agreement_stale.rollback.sql",  # the stale-score build (R40, X30 (A))
         "0014_radar_handicap.rollback.sql",  # the float handicap H1
         "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
@@ -121,7 +125,9 @@ def test_rollback_down_to_0007_reverses_everything_above_p2_newest_first():
     ]
     # ...and at 0008 exactly 0009 and everything newer, 0008 itself excluded.
     assert [p.name for p in _rollback_paths("0008")] == [
+        "0018_drc_stated_books.rollback.sql",
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",
         "0015_shadow_agreement_stale.rollback.sql",  # the stale-score build (R40, X30 (A))
         "0014_radar_handicap.rollback.sql",  # the float handicap H1
         "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
diff --git a/tests/cobalt/test_radar_migration.py b/tests/cobalt/test_radar_migration.py
index b10cb6a1..af369727 100644
--- a/tests/cobalt/test_radar_migration.py
+++ b/tests/cobalt/test_radar_migration.py
@@ -31,8 +31,10 @@ def test_rollback_selects_only_newer_files_newest_first():
     ahead of 0007 in REVERSE, and the property under test is "everything
     newer than the bound, newest first", never a fixed tuple length."""
     selected = _rollback_paths("0003")
-    assert [p.name for p in selected][:8] == [
+    assert [p.name for p in selected][:10] == [
+        "0018_drc_stated_books.rollback.sql",  # DRC K1
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",  # DRC D1
         "0015_shadow_agreement_stale.rollback.sql",  # the stale-score build (R40, X30 (A))
         "0014_radar_handicap.rollback.sql",  # the float handicap H1
         "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
diff --git a/tests/cobalt/test_radar_panel_cards.py b/tests/cobalt/test_radar_panel_cards.py
index aef870ea..1efed329 100644
--- a/tests/cobalt/test_radar_panel_cards.py
+++ b/tests/cobalt/test_radar_panel_cards.py
@@ -669,10 +669,12 @@ POST_ALLOWLIST = {
     "/size", "/fill", "/attest", "/card/{card_id}/move", "/card/{card_id}/stop",
     "/radar/card/{card_id}/key", "/radar/card/{card_id}/dot/{factor}",
     "/radar/card/{card_id}/promote", "/radar/card/{card_id}/release",
+    "/settings/daily", "/settings/daily/apply",
+    "/drc/import", "/drc/no-trade", "/drc/scan",  # DRC D2-4 (the /drc import page)
     # voice V1 (FINAL §9): the widget's turn and its Confirm / Cancel taps
     "/voice/turn", "/voice/confirm", "/voice/cancel",
 }
-GET_ONLY = {"/", "/radar", "/api/radar/pool", "/api/health", "/api/prefill"}
+GET_ONLY = {"/", "/radar", "/api/radar/pool", "/api/health", "/api/prefill", "/drc"}
 
 
 def test_post_routes_are_exactly_the_explicit_allowlist():
diff --git a/tests/cobalt/test_radar_score_migration.py b/tests/cobalt/test_radar_score_migration.py
index 3fe790ca..6295c4d4 100644
--- a/tests/cobalt/test_radar_score_migration.py
+++ b/tests/cobalt/test_radar_score_migration.py
@@ -101,7 +101,9 @@ def test_rollback_selects_every_newer_migration_then_0007_then_0006_newest_first
     newest four are named explicitly: P4's 0008/0009 and the archiver's
     0010/0011 both reverse before 0007."""
     newest_four = [
-        "0017_voice_turns.rollback.sql",  # voice V1 (the list is now the newest eight)
+        "0018_drc_stated_books.rollback.sql",  # DRC K1 (the name stays; the list is ten now)
+        "0017_voice_turns.rollback.sql",  # voice V1 (the list is now the newest ten)
+        "0016_drc.rollback.sql",  # DRC D1
         "0015_shadow_agreement_stale.rollback.sql",  # the stale-score build (R40, X30 (A))
         "0014_radar_handicap.rollback.sql",  # the float handicap H1
         "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
@@ -111,17 +113,17 @@ def test_rollback_selects_every_newer_migration_then_0007_then_0006_newest_first
         "0008_radar_value_movers.rollback.sql",
     ]
     reverse_names = [p.name for p in REVERSE]
-    assert reverse_names[:8] == newest_four
+    assert reverse_names[:10] == newest_four
     assert (
         reverse_names.index("0006_radar_score.rollback.sql")
         == reverse_names.index("0007_radar_cards.rollback.sql") + 1
     )
-    assert [p.name for p in _rollback_paths("0005")][:8] == newest_four
+    assert [p.name for p in _rollback_paths("0005")][:10] == newest_four
     assert [p.name for p in _rollback_paths("0005")][-2:] == [
         "0007_radar_cards.rollback.sql",
         "0006_radar_score.rollback.sql",
     ]
-    assert [p.name for p in _rollback_paths("0006")][:8] == newest_four
+    assert [p.name for p in _rollback_paths("0006")][:10] == newest_four
     assert [p.name for p in _rollback_paths("0006")][-1:] == [
         "0007_radar_cards.rollback.sql"
     ]
diff --git a/tests/cobalt/test_tenancy.py b/tests/cobalt/test_tenancy.py
index 7c301958..f1c9fa24 100644
--- a/tests/cobalt/test_tenancy.py
+++ b/tests/cobalt/test_tenancy.py
@@ -71,6 +71,7 @@ def _stores():
     from cobalt.aset.store import AsetStore
     from cobalt.cards.store import CardStore
     from cobalt.daymode.store import DayModeStore
+    from cobalt.drc.store import DrcStore
     from cobalt.jobs.store import JobStore
     from cobalt.radar.store import RadarStore
     from cobalt.redact.store import RedactionStore
@@ -80,7 +81,7 @@ def _stores():
     from cobalt.vaultwrite.store import VaultWriteStore
 
     return [
-        BarStore, AsetStore, CardStore, DayModeStore, JobStore,
+        BarStore, AsetStore, CardStore, DayModeStore, DrcStore, JobStore,
         RadarStore, RedactionStore, SessionBlockStore,
         TraderSettingsStore, TradeDefStore, VaultWriteStore,
     ]
@@ -511,8 +512,10 @@ def test_down_to_0004_selects_0009_0008_0007_0006_then_0005_reverse():
 
     selected = [path.name for path in _rollback_paths("0004")]
     names = selected
-    assert selected[:8] == [
+    assert selected[:10] == [
+        "0018_drc_stated_books.rollback.sql",  # DRC K1
         "0017_voice_turns.rollback.sql",  # voice V1
+        "0016_drc.rollback.sql",  # DRC D1
         "0015_shadow_agreement_stale.rollback.sql",  # the stale-score build (R40, X30 (A))
         "0014_radar_handicap.rollback.sql",  # the float handicap H1
         "0013_tunables_slug_nullable.rollback.sql",  # the setups one build (R2-3 = B)
```
`git -C /Users/cobalt/cobalt-wt/drc-d1 diff --cached main -- <the 4 DevDocs>`: pure appends of the branch's sections after main's, verbatim; `--stat`:
```
 docs/40 - DevDocs/cobalt/aset/web.md               | 54 ++++++++++++++++++++++
 docs/40 - DevDocs/cobalt/cli.md                    |  6 +++
 docs/40 - DevDocs/cobalt/db_migrations/__init__.md | 31 +++++++++++++
 .../40 - DevDocs/cobalt/db_migrations/placement.md | 20 ++++++++
 4 files changed, 111 insertions(+)
```
(The full DevDocs diff was read in-session: every `+` line is a branch-side line verbatim, plus one `---` separator line and blank lines between sections in `aset/web.md` and one blank line in each of the other three; zero `-` lines.)

PROOF stat blocks (both 66 paths, identical set):
- `git -C /Users/cobalt/cobalt-wt/drc-d1 diff --stat 04b05cd4 10163d51 -- . ':(exclude)docs'` → `66 files changed, 13131 insertions(+), 45 deletions(-)`; `__init__.py | 24 +`, `test_radar_score_migration.py | 8 +-`.
- `git -C /Users/cobalt/cobalt-wt/drc-d1 diff --stat daf36e01 5bb1f4b5 -- . ':(exclude)docs'` → `66 files changed, 13125 insertions(+), 46 deletions(-)`; `__init__.py | 17 +`, `test_radar_score_migration.py | 10 +-`. Every other line identical.

No path edited outside the conflicted set; no conflict resolved outside its rule.

## CONTINUE
Stopped at O. For the desk: rule a fix round (L75) for the 7 position pins on `5bb1f4b5`, then relaunch from `O`.

## ESCALATE
1. DIALOG (L62/L63), during E0 (a prep read, no tree change): `git -C /Users/cobalt/cobalt diff 04b05cd4 10163d51 --stat -- docs/40\ -\ DevDocs/cobalt/aset/web.md docs/40\ -\ DevDocs/cobalt/cli.md` raised a permission dialog (backslash-escaped spaces, not the plain quoted form; the seat's own spelling error). The desk (`cto-desk`) pressed Escape and directed by message: "Carry on from E0 per your ## CONTINUE", paths quoted from now on. Continued on that direction; no merge was in progress, no `.env` present. Also: the seat's first law-read grep used a `\|` pattern (ran, no dialog).
2. ESCALATE: O red — 7 position pins outside the conflict set (`## O OFFLINE`). `## BOTH-SIDES` named no rule for single-side files that pin the registry tail. The desk rules the fix (L75); this build holds no edit for them.
3. ASK DESK: R-ARCH says the branch's registry-pin docstring paragraph (`DRC D1 (\`drc/d1-trading-log\`) adds 0016 on a \`main\` base …`) is dropped. It sits OUTSIDE the conflict markers (main never changed that docstring, so it merged clean), and UNATTENDED RULES allow edits only inside markers. Safe default taken: kept (visible in the `test_archiver_migrations.py` diff under `## FOR THE CHECK`). [10:55 EDT]

FAILED: O — offline red on 5bb1f4b5 — test_assumed_store::test_0013_is_registered_forward_and_reverse, test_drc_k1_store::test_the_pair_exists_and_is_registered_after_0016, test_drc_k1_store::test_down_to_0016_selects_only_the_k1_rollback, test_drc_store::test_the_pair_exists_and_is_registered_last, test_drc_store::test_down_to_0011_on_this_tree_selects_only_this_rollback, test_radar_handicap_store::test_down_to_0013_selects_only_this_rollback, test_voice_store::test_both_files_exist_and_are_registered_last_and_first
