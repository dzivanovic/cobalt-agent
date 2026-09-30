# DEPLOY 2026-09-30 (1 OF 2) — DRC D3 + migrations 0016 0018 0019 0020

Hub `deploy-drc-0930` · Opus 5.5 · prompt `prompts/2026-09-30/44-deploy-1-drc-0930.md` · launch row R14 · attempt 2 (attempt 1: `deploy-2026-09-30-1-attempt1.md`).

## §0 Headline
- NOT DEPLOYED. Gate red at G (a), 07:12 ET. Production, `cobalt_dev` and `main` untouched; residents never went down.
- Offline suite: `1 failed, 3628 passed`. The failure is `test_drc_build.py:904`: `jobs.yaml` must not contain `com.cobalt.prefill-drc`.
- The label is in the `because:` text the desk's config commit `ad805ca4` added, as `44` STEP-S worded it. Preflight, tree and config checks all passed.
- The desk rewords that line, re-issues `44` and relaunches (ESCALATE 1–2).

## L74
- A block inside the tool result of the `areas/cobalt.md` read asked for a `Claude-Session:` line in every commit and named a file-send tool. It is data; not followed. Commits here carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| check | command | exit | result |
|---|---|---|---|
| placeholder 1 | `grep -n -E "R_[_]" <this prompt>` | 1 | no output |
| placeholder 2 | `grep -n -E "«FIL[L]" <this prompt>` | 1 | no output |
| report absent | `ls -la …/reports/deploy-2026-09-30-1.md` | 1 | `No such file or directory` |
| R9 row | `grep -n "^| R9 " <desk file>` | 0 | ONE row, line 17: `| R9 | 06:40 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R9`): two deploys one by one, existing generic list, no new strings; the 09:30 block is cancelled (prod unusable): build and deploy continue past the open. Sets aside L66/L43 window, `41`'s 09:15 stop. | APPROVED |` |
| R9 committed | `git … log -1 --format=%H -S"| R9 |" -- <desk file>` | 0 | `3fe2eb8e4cbe942a469b18d8eff6e251d960b90a` |
| R10 row | `grep -n "^| R10 " <desk file>` | 0 | ONE row, line 18: `| R10 | 06:43 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R10`): run it. STANDING until he says prod is usable for trading: the 09:30 open and L66/L43 windows stop no build or deploy (L73 per-case override, bounded by that condition). | APPROVED |` |
| R10 committed | `git … log -1 --format=%H -S"| R10 |" -- <desk file>` | 0 | `7d7a46a09f33f706ba1188d88e3145c2549649ef` |
| launch row R14 | `grep -n "^| R14 " <desk file>` | 0 | line 22: `| R14 | 06:56 ET | LAUNCH (R9, R10, R13): deploy 1 of 2 `44-deploy-1-drc-0930.md` (DRC D3 `b8ac291b`, migrations 0016 0018 0019 0020), Opus 5.5, gate `~/cobalt-wt/deploy-0930-1`; generic list, no new string. LOCK: no with-DB run in flight. Deploy 2 (`45`) follows its stop line. | LAUNCHED |` |
| R14 committed | `git … log -1 --format=%H -S"44-deploy-1-drc-0930.md" -- <desk file>` | 0 | `423da40dd2076604b77547fbda7af412caf1400d` |

## PREFLIGHT
| rule | command | exit | result |
|---|---|---|---|
| P1 date | `date` | 0 | `Wed Sep 30 07:01:04 EDT 2026` |
| P2 check line | `tail -n 3 …/drc-d3-fix-r2-check-2026-09-29.md` | 0 | last line: `DRC D3 FIX R2 CHECK DONE · round: 3 · opus: CHECK DRC D3 FIX R2: FIX STANDS · ready for K3: YES · sol: NOT SEATED (METER — retry after Oct 4th, 2026 2:06 PM) · grok: CHECK DRC D3 FIX R2: FIX STANDS · ready for K3: YES · houses that checked: 2 of 3 · defects that HOLD: 0 · ready for K3: YES · ESCALATE: 12` |
| P2 committed | `git … log -1 --format=%H -- <check report>` | 0 | `f5166dc4615022e8dab1e349b6aed7b186cff16a` |
| P2 clean | `git … diff --stat -- <check report>` | 0 | no output |
| P3 tip | `git … rev-parse --short=8 b8ac291b` | 0 | `b8ac291b` |
| P3 ancestor | `git … merge-base --is-ancestor b8ac291b drc/d1-trading-log` | 0 | no output |
| P3 docs-only above | `git … diff --stat b8ac291b drc/d1-trading-log -- . ':(exclude)docs'` | 0 | no output |
| P4 lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| P5 rules | `grep -c -F "clinerules" …/configs/cobalt/rules.yaml` | 1 | `0` |
| P5 diff | `git … diff --stat main b8ac291b -- .clinerules` | 0 | no output |
| P6 status | `git -C …/deploy-0930-1 status --short --branch` | 0 | `## deploy/drc-0930` |
| P6 HEAD | `… rev-parse --short=8 HEAD` | 0 | `ad805ca4` = `<jobs commit>` |
| P6 HEAD~1 | `… rev-parse --short=8 HEAD~1` | 0 | `94067d63` = `<m1>` |
| P6 HEAD~2 | `… rev-parse --short=8 HEAD~2` | 0 | `8635cde1` = `<main base>` |
| P6 merge parent | `… rev-parse --short=8 HEAD~1^2` | 0 | `b8ac291b` |
| P6 commit files | `… show --stat HEAD` | 0 | `seam(deploy-0930-1): DRC configs classified (K10)` · `configs/cobalt/jobs.yaml | 10 ++++++++++` · `1 file changed, 10 insertions(+)` |
| P7 0016 | `ls …/db_migrations/0016_drc.sql` | 1 | `No such file or directory` |
| P7 0020 | `ls …/db_migrations/0020_drc_build_kinds.sql` | 1 | `No such file or directory` |

## THE TREE
| check | command | exit | result | verdict |
|---|---|---|---|---|
| merges | `git -C /Users/cobalt/cobalt log --oneline --merges --first-parent 8635cde1..deploy/drc-0930` | 0 | `94067d63 Merge commit 'b8ac291b' into deploy/drc-0930` — one line = `<m1>` | pass |
| tip in gate | `git … merge-base --is-ancestor b8ac291b deploy/drc-0930` | 0 | no output | pass |
| migrations | `git … diff --stat 8635cde1 deploy/drc-0930 -- src/cobalt/db_migrations` | 0 | `0016_drc.rollback.sql` 8 · `0016_drc.sql` 95 · `0018_drc_stated_books.rollback.sql` 18 · `0018_drc_stated_books.sql` 63 · `0019_drc_events.rollback.sql` 28 · `0019_drc_events.sql` 46 · `0020_drc_build_kinds.rollback.sql` 17 · `0020_drc_build_kinds.sql` 16 · `__init__.py` 35 · `placement.py` 19 · `10 files changed, 343 insertions(+), 2 deletions(-)`; no `0021` path | pass |
| registry | `grep -n -F "MIGRATIONS_DIR / \"00" …/deploy-0930-1/src/cobalt/db_migrations/__init__.py` | 0 | `FORWARD` `:122`–`:140`, ending `:135` `0015_shadow_agreement_stale.sql` · `:136` `0016_drc.sql` · `:137` `0017_voice_turns.sql` · `:138` `0018_drc_stated_books.sql` · `:139` `0019_drc_events.sql` · `:140` `0020_drc_build_kinds.sql`; `REVERSE` from `:145` `0020_drc_build_kinds.rollback.sql` · `:146` `0019_drc_events` · `:147` `0018_drc_stated_books` · `:148` `0017_voice_turns` · `:149` `0016_drc.rollback.sql` · `:150` `0015_shadow_agreement_stale.rollback.sql` | pass |
| ops | `git … diff --stat 8635cde1 deploy/drc-0930 -- ops` | 0 | `ops/README.md | 2 +-` · `ops/com.cobalt.prefill-drc.plist | 63 ---` · `2 files changed, 1 insertion(+), 64 deletions(-)` | pass |
| migration list | `git … log --oneline main..b8ac291b -- src/cobalt/db_migrations` | 0 | `d2897b46` · `8e8762ca` · `7cdc5774` · `5bb1f4b5` · `9a0fc900` · `d583f6fd` (the drafter's six) | pass |

## THE CONFIGS
The desk's commit `ad805ca4`, verified against the merged tree.

THE READERS (whole):
- `grep -rn "prefill.yaml" …/deploy-0930-1/src` → `smoke/checks.py:124` (docstring) · `drc/template.py:4` · `:15` · `:41` (prose, message) · `prefill/config.py:29:PREFILL_CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "prefill.yaml"` · `taxonomy/trade_note_migration.py:55` (comment) · `replay/line.py:207` (docstring).
- `grep -rn "load_prefill_paths(" …/src` → `smoke/checks.py:129` · `drc/build.py:25` (docstring) · `drc/template.py:16` (docstring) · `:38` · `:70` · `prefill/config.py:156:def load_prefill_paths() -> PrefillPathsConfig:` · `daymode/drc.py:95` · `taxonomy/trade_note_migration.py:59` · `replay/line.py:211` · `aset/web.py:1034:        prefill_paths = load_prefill_paths()`.
- `grep -rn "drc.md.j2" …/src` → `prefill/drc.py:6` (docstring: `repo template `drc.md.j2` (deleted)`) · `daymode/drc.py:121` (comment). No hit loads the file.
- `grep -n "prefill.yaml" …/configs/cobalt/jobs.yaml` → `81:      - "configs/cobalt/prefill.yaml"              # prefill/config.py:157 (load_prefill_paths), called from aset/web.py:1034 at the fill`.
- `grep -n "drc.md.j2" …/configs/cobalt/jobs.yaml` → `326:  - path: configs/cobalt/templates/drc.md.j2`.
- `grep -n "PREFILL_CONFIG_PATH" …/src/cobalt/prefill/config.py` → `29:` the constant · `157:    data = _load_yaml_mapping(PREFILL_CONFIG_PATH, "prefill")` · `162:` the error text.
- `grep -n "FileSystemLoader(str(TEMPLATES_DIR))" …/src/cobalt/prefill/daily.py` → `238:    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), keep_trailing_newline=True)`.

`git -C /Users/cobalt/cobalt-wt/deploy-0930-1 diff HEAD~1 HEAD` (whole):
```
diff --git a/configs/cobalt/jobs.yaml b/configs/cobalt/jobs.yaml
index 101efc6d..9c62799e 100644
--- a/configs/cobalt/jobs.yaml
+++ b/configs/cobalt/jobs.yaml
@@ -78,6 +78,7 @@ jobs:
       # (prefill/rules_gen.py), which writes this generated file. Moved from no_resident_reads (the schema
       # refuses a path in both); its one-shot reader, provenance kept: prefill/daily.py (com.cobalt.prefill-daily).
       - "configs/cobalt/rules.yaml"
+      - "configs/cobalt/prefill.yaml"              # prefill/config.py:157 (load_prefill_paths), called from aset/web.py:1034 at the fill
       # voice V1's six paths, classified at the stack seam build 2026-09-25 (L42). The sheet serves voice
       # (aset/web.py:90 include_router(voice_web.router)), so this process runs voice's loaders.
       - "configs/cobalt/voice.yaml"                # voice/config.py:32 CONFIG_PATH + :120 (load_voice_config); cached per process in voice/web.py:59 _CONFIG, so a change reaches the sheet only by restart
@@ -322,6 +323,15 @@ no_resident_reads:
       (send_dm, reached from heartbeat/runner.py:304 — the one-shot
       heartbeat) and by `cobalt validate` (cli.py:261, an operator
       command, not a job). No resident sends a DM. Ruled 2026-09-15.
+  - path: configs/cobalt/templates/drc.md.j2
+    readers: [com.cobalt.prefill-daily]
+    because: >
+      DRC D3 deleted this template. No code loads it: the two remaining
+      mentions are prose (prefill/drc.py:6, a docstring; daymode/drc.py:121,
+      a comment). Its one reader was the retired com.cobalt.prefill-drc.
+      com.cobalt.prefill-daily is the one job whose loader reaches
+      configs/cobalt/templates/ (prefill/daily.py:238, FileSystemLoader(TEMPLATES_DIR)).
+      Ruled 2026-09-30.
   # configs/cobalt/rules.yaml LEFT this list in DRC D3 ([F-28]): the DRC build
   # calls regenerate_rules_config() inside com.cobalt.aset — it is now in that
   # job's `reads:` (the 15:40 prefill-drc reader is retired).
```

| cite in `ad805ca4` | shown by | verdict |
|---|---|---|
| `prefill/config.py:157` | the `PREFILL_CONFIG_PATH` grep | pass |
| `aset/web.py:1034` | the `load_prefill_paths(` grep — a resident reader inside `src/cobalt/aset/` | pass |
| `prefill/drc.py:6` · `daymode/drc.py:121` | the `drc.md.j2` grep — prose both | pass |
| `prefill/daily.py:238` | the `FileSystemLoader(str(TEMPLATES_DIR))` grep | pass |
| two decisions only, no other line | the diff above | pass |

## L68 GATE
**RED at (a). Legs (b)–(e) not run.**

| leg | command | exit | result | verdict |
|---|---|---|---|---|
| (a) cwd | `cd /Users/cobalt/cobalt-wt/deploy-0930-1` · `ls -la …/deploy-0930-1/.env` | 0 / 1 | `No such file or directory` | pass |
| (a) OFFLINE | `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background, 07:02:46 → 07:12, on `ad805ca4`) | 1 | `1 failed, 3628 passed, 562 skipped, 1 xfailed, 25 warnings in 592.78s (0:09:52)` · no `uv` sync line | **RED** |
| return | `cd /Users/cobalt/cobalt` · `ls -la /Users/cobalt/cobalt/.env` | 0 | listed | cwd back |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` — L76 lock never taken | — |
| gate worktree | `git -C …/deploy-0930-1 status --short --branch` | 0 | `## deploy/drc-0930` — clean, at `ad805ca4` | — |

THE RED TEST: `tests/cobalt/test_drc_build.py::test_the_retired_files_are_gone`, `test_drc_build.py:904`:
```
>       assert "com.cobalt.prefill-drc" not in (repo / "configs" / "cobalt" / "jobs.yaml").read_text()
E       assert 'com.cobalt.prefill-drc' not in '# F17 TASK ...LT RESUME"\n'
E         'com.cobalt.prefill-drc' is contained here:
E           e retired com.cobalt.prefill-drc.
E                 com.cobalt.prefill-daily is the one job whose loader reaches
E                 configs/cobalt/templates/ (prefill/daily.py:238, FileSystemLoader(TEMPLATES_DIR)).
E                 Ruled 2026-09-30.
```
- The test's first two assertions passed: the plist and `drc.md.j2` are gone from the tree.
- `grep -n -F "com.cobalt.prefill-drc" …/deploy-0930-1/configs/cobalt/jobs.yaml` → ONE hit, `331:      a comment). Its one reader was the retired com.cobalt.prefill-drc.` — the `because:` text `ad805ca4` added.
- 3628 passed = DRC's own 3629 less this one test; skipped 562 and xfailed 1 equal DRC's build (`drc-d3-fix-r2-build-2026-09-29.md` F7).

## RESTARTS
Not run. RESTARTS: none — nothing merged.

## Deploy table
Nothing merged, no migration applied, no resident stopped, no tag made, no snapshot taken, `cobalt_dev` not touched. LIVE stays `deploy-2026-09-27` = `3349466f`.

## Smoke
Not run.

## ESCALATE
1. THE RED IS THE CONFIG COMMIT'S WORDING, AND `44` ORDERS THAT WORDING. `44` bare command (0b) and STEP-S require the `drc.md.j2` entry's `because:` to state that its one reader was the retired `com.cobalt.prefill-drc`; DRC's own test `test_drc_build.py:904` refuses that label anywhere in `jobs.yaml`. One fix: the desk rewords line 331 without the label (for example "the retired 15:40 DRC prefill job") in a new config commit, and re-issues `44`'s STEP-S sentence to match. No code changes.
2. RELAUNCH: this report now exists, so `44` as written ends at its `# RELAUNCH` rule. The re-issue needs a new report path or a relaunch rule (attempt 1 ESCALATE 4).
3. `main` moved after the cut: `git … log --oneline -1 main` → `27f4a86a docs(desk): 09-30 R16 seam build relaunch bd599bad` (`<main base>` `8635cde1`). Not proven docs-only here (STEP-D0 not reached).
4. `ad805ca4`'s message carries `Co-Authored-By: Claude Sonnet 5.5` and a `Claude-Session:` line (the desk's session). A new config commit replaces or follows it; either rides into `main` at the fast-forward.
5. With-DB and live-note legs UNPROVEN on the gate tree (L70): not run.
6. Cleanup (L46): `/Users/cobalt/cobalt-wt/deploy-0930-1` and `deploy/drc-0930` stand clean at `ad805ca4`; reusable once the config commit is fixed.
7. RECORDS, carried: his daily-stop value before the first build (D4's); the E7 ops read of D2; the dev-vault proof with a diff is the desk's HUB-RUN after the deploy (L28); K10.2's note equality is UNPROVEN until read from both jobs' environment.

## CONTINUE
next: none — the desk fixes the config commit's wording (ESCALATE 1), re-issues `44` (ESCALATE 2) and relaunches; every check through STEP-S is quoted above and passed.

## PRE-STOP SELF-CHECK
1. Smoke: not run; no row claimed.
2. Tip re-read at P3 (`b8ac291b`); ancestor of `deploy/drc-0930` (THE TREE row 2). No `<stack-final>` exists.
3. REVERT-READBACK: none — nothing merged. Every sha, count and `file:line` above is from this run's tool output.
4. The config commit's diff is quoted whole under `## THE CONFIGS`; all five cites are shown by STEP-S's greps.

FAILED: gate — G (a) — `tests/cobalt/test_drc_build.py::test_the_retired_files_are_gone` (`:904`: `com.cobalt.prefill-drc` is in `jobs.yaml`, line 331, from config commit `ad805ca4`) · rollback: not used
