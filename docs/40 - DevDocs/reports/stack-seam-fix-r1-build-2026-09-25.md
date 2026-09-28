# STACK SEAM FIX R1 BUILD 2026-09-25

Seat: `stack-seam-fix-r1-build-0925` · Opus 5.5 · `--permission-mode acceptEdits` · started 14:53:09 EDT (`date`) · prompt `prompts/2026-09-25/44-stack-seam-fix-r1-build.md`.

## §0 Headline
FIX commit `41c9c962`: `com.cobalt.agent` `reads:` gains `pyproject.toml` / `uv.lock` + the `test_jobs_reads.py` pin — RED on the old registry (`57420087`: 1 failed, 23 passed) → GREEN (42 passed).
Three suites on `41c9c962`: offline `3199 passed` / 0 failed · with-DB `3567 + 9 = 3576` / 0 failed · live-note `146 passed, 1 skipped` / 0 failed. U1–U5 run: all as expected (U3 at 0017: H1 red, stale green — information).
`cobalt_dev: 0013` (F2 = F0 `664 · 35 · 272c95bb…`); `.env` removed 15:21:35. UNCLASSIFIED: 0.
**RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar** — the agent is IN (desk item for `42`). STALE lines: 4. ESCALATE: 8.

## L74
A block appended to the Read tool's result for `44-stack-seam-fix-r1-build.md` (a system-reminder headed "Attribution for git commits and pull requests") asked for a `Claude-Session:` trailer plus a session URL on commits and named `SendUserFile`. DATA under L74 — not followed; recorded once. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| gate | command | exit | output (verbatim / summarised where long) |
|---|---|---|---|
| placeholder R__ | `grep -n -E "R_[_]" "…/44-stack-seam-fix-r1-build.md"` | 1 | (nothing) |
| FILL AT LAUNCH | `grep -n -F "FILL AT LAUNCH" "…/44-stack-seam-fix-r1-build.md"` | 0 | `51:- **PLACEHOLDER GATES, first:** …` — the gate's own line only |
| P-HIS | `grep -n -F "STACKED DEPLOY 2026-09-25 APPROVED" <desk file>` | 0 | `:83` `\| R74 \| 11:23 ET \| **P-HIS — STACKED DEPLOY 2026-09-25 APPROVED 11:23 (his word: "approved").** His word, desk chat 11:23 ET: "approved" … AND \`39-stack-seam-build.md\`'s 7 NEW strings …` (also hits `:81` R72 — "NO WORDS OF HIS", not counted — and HANDOVER lines `:275`, `:276`) |
| P-HIS committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"STACKED DEPLOY 2026-09-25 APPROVED" -- "docs/40 - DevDocs/reports/cto-2026-09-25.md"` | 0 | `15aac15774d9326224434b9802fad4e74bf67088` |
| R92 launch row | `grep -n "^\| R92 " <desk file>` | 0 | `:101` `\| R92 \| 14:51–14:52 ET \| … LAUNCH ROW for \`prompts/2026-09-25/44-stack-seam-fix-r1-build.md\` … \`git -C ~/cobalt log -1 --format=%h deploy/stacked-0925\` = \`57420087\`; \`ls ~/cobalt-wt/*/.env\` no matches; **no with-DB run in flight** …` |
| R92 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"44-stack-seam-fix-r1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-25.md"` | 0 | `c20b7ee7c9971e0a720a42c9b68b7e175592793b` |
| check stop line | `tail -n 3 ".../stack-seam-check-2026-09-25.md"` | 0 | last line `STACK SEAM CHECK DONE · round: 1 · opus: CHECK: FIX — … · defects that HOLD: 1 · ready for the gate: NO · ESCALATE: 13` |
| check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- ".../stack-seam-check-2026-09-25.md"` | 0 | `7b46bb5aa15cec74b20a30179fed9f4af8a20962` |
| drafter stop line | `tail -n 3 ".../stack-seam-fix-r1-draft-2026-09-25.md"` | 0 | `STACK SEAM FIX R1 DRAFTED · FIX: 5 · NOT REAL: 9 · UNPROVEN: 5 · OUT OF SCOPE: 5 · OWNER ITEM: 0 · agent restart: IN · prompts: 2 · folds for 42: 25 · new rule strings: 4 · ESCALATE: 13` |
All gates pass.

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| date | `date` | 0 | `Fri Sep 25 14:53:23 EDT 2026` |
| clean | `git -C …/stacked-0925 status --short --branch` | 0 | `## deploy/stacked-0925` / `?? "docs/40 - DevDocs/reports/stack-seam-fix-r1-build-2026-09-25.md"` (this report only) |
| at `<on>` | `git -C …/stacked-0925 log --oneline -2` | 0 | `57420087 docs(stack-seam): stack seam build report — a7296b44 (FOUR)` / `a7296b44 chore(jobs): classify voice V1's six paths — aset reads voice/agents-voice/modelaccess yaml, start_aset.sh, pyproject.toml, uv.lock; radar reads pyproject.toml, uv.lock (stack seam, L42)` |
| lock | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| own .env | `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory` |
| live notes | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 notes listed (`9 EMA Reclaim.md` … `VWAP Continuation.md`) |
| FIX input | `grep -n -F "nohup uv run" /Users/cobalt/cobalt/cobalt.sh` | 0 | `59:        nohup uv run src/cobalt_agent/main.py > logs/mattermost_session.log 2>&1 &` |
| FIX input | `grep -n -F "cobalt.sh" …/ops/com.cobalt.agent.plist` | 0 | `25:        <string>/Users/cobalt/cobalt/cobalt.sh</string>` |
| FIX input | `grep -n -F "uv syncs the environment from it when the process starts" …/configs/cobalt/jobs.yaml` | 0 | `82:`, `83:` (aset, `# ops/start_aset.sh:73 (exec uv run python -m cobalt.aset): uv syncs …`), `184:`, `185:` (radar, `# ops/com.cobalt.radar.plist:18–22 (uv run cobalt radar run): uv syncs …`) — FOUR lines |
| FIX input | `grep -n -F "reads: []" …/configs/cobalt/jobs.yaml` | 0 | `94:    reads: []` / `109:    reads: []` / `141:    reads: []` / `172:    reads: []` |
| FIX input | `grep -n -F "com.cobalt.agent" …/tests/cobalt/test_jobs_reads.py` | 0 | `82:            "com.cobalt.agent", "com.cobalt.herdr",` |
| FIX input | `grep -n -F "com.cobalt.agent" …/tests/cobalt/test_jobs_restarts.py` | 1 | (nothing) — `test_jobs_restarts.py` NOT touched |
Every read matches the prompt's numbers.

## F THE FIX
**F1** — `tests/cobalt/test_jobs_reads.py` edited on the unchanged registry: the agent left the empty-reads tuple (`"com.cobalt.agent", "com.cobalt.herdr",` → `"com.cobalt.herdr",`); `test_every_resident_that_starts_through_uv_run_re_reads_the_uv_files` added after `test_the_other_residents_declare_it_empty_deliberately`, text exactly as `44` F1 (b). No other line changed.

**F2 RED** — `ls -la …/stacked-0925/.env` → `No such file or directory` (exit 1); `uv run pytest -q -p no:cacheprovider tests/cobalt/test_jobs_reads.py` → exit 1. `<red>`:
```
tests/cobalt/test_jobs_reads.py:99: AssertionError
>       assert agent.reads == ["pyproject.toml", "uv.lock"]
E       AssertionError: assert [] == ['pyproject.toml', 'uv.lock']
E         Right contains 2 more items, first extra item: 'pyproject.toml'
E         Use -v to get more diff
=========================== short test summary info ============================
  FAILED tests/cobalt/test_jobs_reads.py::TestTheDerivedRows::test_every_resident_that_starts_through_uv_run_re_reads_the_uv_files - AssertionError: assert [] == ['pyproject.toml', 'uv.lock']
1 failed, 23 passed in 2.14s
```
Exactly one failed test, the new pin; every other test passed. `<red hash>` = `git -C …/stacked-0925 rev-parse --short=8 HEAD` → `57420087` (the tree = `<on>` + the test edit alone).

**F3 REGISTRY** — `configs/cobalt/jobs.yaml`, the `com.cobalt.agent` block only: comment line (a) re-worded as `44` F3 (a); `reads: []` → the two lines of `44` F3 (b). PROOF:
- `grep -c -F "uv syncs the environment from it when the process starts" configs/cobalt/jobs.yaml` → `6`
- `grep -c -F "reads: []" configs/cobalt/jobs.yaml` → `3`
- `grep -n -F "reads:" configs/cobalt/jobs.yaml` → `67:    reads:` / `94:    reads: []` / `109:    reads: []` / `141:    reads:` / `174:    reads: []` / `183:    reads:` / `319:no_resident_reads:` — six per-job keys plus `no_resident_reads:`.

**F4 GREEN** — `ls -la …/.env` → `No such file or directory`; `uv run pytest -q -p no:cacheprovider tests/cobalt/test_jobs_reads.py tests/cobalt/test_jobs_restarts.py` → exit 0. `<green>`: `42 passed in 11.19s` (0 failed, 0 errors).

**F5 COMMIT** — `git -C …/stacked-0925 commit -m "fix(jobs): com.cobalt.agent re-reads pyproject.toml, uv.lock — it starts through uv run (cobalt.sh:59), the rule aset and radar carry (stack seam fix r1, L42)" -m "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>" -- configs/cobalt/jobs.yaml tests/cobalt/test_jobs_reads.py` → `[deploy/stacked-0925 41c9c962] … 2 files changed, 18 insertions(+), 3 deletions(-)`.
`git -C …/stacked-0925 show --stat HEAD`:
```
commit 41c9c962a95e5ba39bc4bdca7e2fc65520d2f4a9
Author: dzivanovic <dejan.kenkyukai@gmail.com>
Date:   Fri Sep 25 14:54:37 2026 -0400

    fix(jobs): com.cobalt.agent re-reads pyproject.toml, uv.lock — it starts through uv run (cobalt.sh:59), the rule aset and radar carry (stack seam fix r1, L42)
    
    Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>

 configs/cobalt/jobs.yaml        |  6 ++++--
 tests/cobalt/test_jobs_reads.py | 15 ++++++++++++++-
 2 files changed, 18 insertions(+), 3 deletions(-)
```
`git -C …/stacked-0925 diff HEAD~1 HEAD` (WHOLE):
```diff
diff --git a/configs/cobalt/jobs.yaml b/configs/cobalt/jobs.yaml
index b5f18e73..f5a6c19b 100644
--- a/configs/cobalt/jobs.yaml
+++ b/configs/cobalt/jobs.yaml
@@ -131,14 +131,16 @@ jobs:
     # It gets a row because F18 must be able to say it is down; it gets
     # no wrapper because the strangler rule (CLAUDE.md) says the old tree
     # stays untouched and no new-core code is added to it.
-    # EMPTY, and it needs the caveat. The old tree loads `configs/*.yaml`
+    # NOT EMPTY since the stack seam fix r1 (2026-09-25): the two uv files below. The caveat stands: the old tree loads `configs/*.yaml`
     # ONCE into a singleton at first construction
     # (cobalt_agent/config.py:410) and `Config.load()` returns the cached
     # object thereafter — so it does not RE-READ anything, which is what
     # this field records. It still has to be restarted when one of those
     # files changes, because it is running the old values. That is the
     # read-once class; it wants its own field (09-09 ESCALATE).
-    reads: []
+    reads:
+      - "pyproject.toml"                           # cobalt.sh:59 (nohup uv run src/cobalt_agent/main.py), started by ops/com.cobalt.agent.plist:25 (cobalt.sh start): uv syncs the environment from it when the process starts
+      - "uv.lock"                                  # cobalt.sh:59 (nohup uv run src/cobalt_agent/main.py), started by ops/com.cobalt.agent.plist:25 (cobalt.sh start): uv syncs the environment from it when the process starts
     imports: [cobalt_agent.main]
     what: "the OLD-TREE agent (cobalt.sh start -> cobalt_agent/main.py), detached; liveness from its PID file"
 
diff --git a/tests/cobalt/test_jobs_reads.py b/tests/cobalt/test_jobs_reads.py
index 0c7524da..b66f84fd 100644
--- a/tests/cobalt/test_jobs_reads.py
+++ b/tests/cobalt/test_jobs_reads.py
@@ -79,7 +79,7 @@ class TestTheDerivedRows:
         text = (REPO_ROOT / "configs" / "cobalt" / "jobs.yaml").read_text()
         for label in (
             "com.cobalt.mainframe", "com.cobalt.obsidian",
-            "com.cobalt.agent", "com.cobalt.herdr",
+            "com.cobalt.herdr",
         ):
             spec = load_job_registry().spec(label)
             assert spec.reads == []
@@ -88,6 +88,19 @@ class TestTheDerivedRows:
         keys = [line for line in text.splitlines() if line.strip().startswith("reads:")]
         assert len(keys) == 6, "one per resident, none on a one-shot"
 
+    def test_every_resident_that_starts_through_uv_run_re_reads_the_uv_files(self):
+        """`uv run` syncs the environment from pyproject.toml / uv.lock when
+        the process starts, so a change to either reaches a resident only by
+        restart. Three residents start that way: the sheet
+        (ops/start_aset.sh:73), the radar (ops/com.cobalt.radar.plist) and
+        the old-tree agent (cobalt.sh:59, via ops/com.cobalt.agent.plist:25).
+        Stack seam check 2026-09-25, claim 1 — the agent was missing."""
+        agent = load_job_registry().spec("com.cobalt.agent")
+        assert agent.reads == ["pyproject.toml", "uv.lock"]
+        for path in ("pyproject.toml", "uv.lock"):
+            readers = load_job_registry().readers_of(path)
+            assert [r.label for r in readers] == [SHEET, "com.cobalt.agent", "com.cobalt.radar"]
+
 
 class TestTheModelRefusesNonsense:
     def _spec(self, **kw):
```
**`<tip>` = `41c9c962`** (`rev-parse --short=8 HEAD`) — the tree every suite below runs on.

## U THE RUNS
**U1 — per-branch identity** (`<tip>` = `41c9c962`). (a) `git -C /Users/cobalt/cobalt diff --name-only <mb> <b> -- . ':(exclude)docs'`; (b) `git -C /Users/cobalt/cobalt diff --stat <b> 41c9c962 -- <every (a) path except the SEAM PATHS, each its own argument>`.
- replay `fix/replay-deadline-0924` / `a994a5dd` — (a) 14 paths: `configs/cobalt/taxonomy/tunables.yaml`, `src/cobalt/radar/evaluate.py`, `src/cobalt/radar/evaluate_cli.py`, `src/cobalt/replay/formations.py`, `src/cobalt/replay/line.py`, `src/cobalt/replay/models.py`, `src/cobalt/replay/runner.py`, `tests/cobalt/test_radar_evaluate.py`, `tests/cobalt/test_radar_evaluate_cli.py`, `tests/cobalt/test_replay_formations.py`, `tests/cobalt/test_replay_line.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_setups_d1.py`, `tests/cobalt/test_setups_registries.py`. Excluded (4): `evaluate.py`, `formations.py`, `test_replay_runner.py`, `test_setups_d1.py`. (b) over the other 10 → (nothing, exit 0). **U1 replay: 14 paths, 4 seam paths excluded, diff EMPTY.**
- H1 `radar/handicap-h1-0922` / `f6643d41` — (a) 49 paths: `configs/cobalt/radar.yaml`, `src/cobalt/aset/radar_panel.py`, `src/cobalt/db_migrations/0014_radar_handicap.rollback.sql`, `src/cobalt/db_migrations/0014_radar_handicap.sql`, `src/cobalt/db_migrations/__init__.py`, `src/cobalt/db_migrations/cli.py`, `src/cobalt/radar/cli.py`, `src/cobalt/radar/config.py`, `src/cobalt/radar/handicap.py`, `src/cobalt/radar/handicap_dry_run.py`, `src/cobalt/radar/models.py`, `src/cobalt/radar/pool.py`, `src/cobalt/radar/runner.py`, `src/cobalt/radar/store.py`, `tests/cobalt/radar_migrated_support.py`, `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_assumed_store.py`, `tests/cobalt/test_cards_picks.py`, `tests/cobalt/test_p4_migrations.py`, `tests/cobalt/test_radar_handicap.py`, `tests/cobalt/test_radar_handicap_dead.py`, `tests/cobalt/test_radar_handicap_dry_run.py`, `tests/cobalt/test_radar_handicap_fix_r1_runs.py`, `tests/cobalt/test_radar_handicap_group.py`, `tests/cobalt/test_radar_handicap_panel.py`, `tests/cobalt/test_radar_handicap_runner.py`, `tests/cobalt/test_radar_handicap_shadow.py`, `tests/cobalt/test_radar_handicap_store.py`, `tests/cobalt/test_radar_migrated_harness.py`, `tests/cobalt/test_radar_migration.py`, `tests/cobalt/test_radar_panel.py`, `tests/cobalt/test_radar_replay.py`, `tests/cobalt/test_radar_score_migration.py`, `tests/cobalt/test_radar_store.py`, `tests/cobalt/test_tenancy.py`, `tests/experiments/handicap_h1/` × 13 (`conftest.py`, `h1_cache.py`, `h1_support.py`, `test_h1_x0_grouping.py`, `test_h1_x1_blanks.py`, `test_h1_x2_marginal_seat.py`, `test_h1_x3_cell_format.py`, `test_h1_x4_rollback_hazard.py`, `test_h1_x5_x6_x7_reads.py`, `test_h1_x8_x11_group.py`, `test_h1_x9_x10_x15_sources.py`, `test_x12_identity.py`, `test_xl76_membership_harness.py`), `tests/fixtures/radar/screen-handicap.real-shape.csv`. Excluded (8): `__init__.py`, `test_archiver_migrations.py`, `test_assumed_store.py`, `test_p4_migrations.py`, `test_radar_handicap_store.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py`. (b) over the other 41 → (nothing, exit 0). **U1 H1: 49 paths, 8 seam paths excluded, diff EMPTY.**
- stale `cards/stale-score-0922` / `de48c19b` — (a) 50 paths: `src/cobalt/cards/scoring.py`, `src/cobalt/cards/store.py`, `src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql`, `src/cobalt/db_migrations/0015_shadow_agreement_stale.sql`, `src/cobalt/db_migrations/__init__.py`, `src/cobalt/radar/audit_export.py`, `src/cobalt/radar/evaluate.py`, `src/cobalt/replay/formations.py`, `tests/cobalt/stale_db_support.py`, `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_assumed_store.py`, `tests/cobalt/test_p4_migrations.py`, `tests/cobalt/test_radar_migration.py`, `tests/cobalt/test_radar_score_migration.py`, `tests/cobalt/test_replay_runner.py`, `tests/cobalt/test_rubberband_forms.py`, `tests/cobalt/test_setups_d1.py`, `tests/cobalt/test_stale_score.py`, `tests/cobalt/test_stale_score_db.py`, `tests/cobalt/test_tenancy.py`, `tests/experiments/stale_score/` × 30 (`conftest.py`, `stale_predicates.py`, `stale_support.py`, `test_x10…`, `test_x11…`, `test_x12…`, `test_x13…`, `test_x14…`, `test_x15…`, `test_x16…`, `test_x18_x19…`, `test_x20_x22…`, `test_x21…`, `test_x23…`, `test_x24…`, `test_x25…`, `test_x26…`, `test_x27…`, `test_x28…`, `test_x29…`, `test_x2…`, `test_x30…`, `test_x3…`, `test_x4…`, `test_x5b…`, `test_x6…`, `test_x7…`, `test_x8…`, `test_x9…`, `test_xl76_devdb_absence.py`). Excluded (12): `__init__.py`, `evaluate.py`, `formations.py`, `test_archiver_migrations.py`, `test_assumed_store.py`, `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_replay_runner.py`, `test_setups_d1.py`, `test_stale_score_db.py`, `test_tenancy.py`. (b) over the other 38 → (nothing, exit 0). **U1 stale: 50 paths, 12 seam paths excluded, diff EMPTY.**
- voice `voice/v1-0923` / `04b05cd4` — (a) 60 paths: `configs/cobalt/agents/voice.yaml`, `configs/cobalt/jobs.yaml`, `configs/cobalt/modelaccess.yaml`, `configs/cobalt/voice.yaml`, `ops/start_aset.sh`, `pyproject.toml`, `src/cobalt/aset/card_stop.py`, `src/cobalt/aset/web.py`, `src/cobalt/cli.py`, `src/cobalt/db_migrations/0017_voice_turns.rollback.sql`, `src/cobalt/db_migrations/0017_voice_turns.sql`, `src/cobalt/db_migrations/__init__.py`, `src/cobalt/db_migrations/placement.py`, `src/cobalt/modelaccess/` × 6 (`__init__.py`, `adapters.py`, `client.py`, `config.py`, `guard.py`, `models.py`), `src/cobalt/voice/` × 14 (`__init__.py`, `agent.py`, `cli.py`, `config.py`, `confirm.py`, `models.py`, `registry.py`, `resolve.py`, `scratch.py`, `store.py`, `tools.py`, `transcribe.py`, `turn.py`, `web.py`), `tests/cobalt/test_archiver_migrations.py`, `tests/cobalt/test_jobs_restarts.py`, `tests/cobalt/test_modelaccess_client.py`, `tests/cobalt/test_modelaccess_config.py`, `tests/cobalt/test_modelaccess_silence.py`, `tests/cobalt/test_p4_migrations.py`, `tests/cobalt/test_radar_migration.py`, `tests/cobalt/test_radar_panel_cards.py`, `tests/cobalt/test_radar_score_migration.py`, `tests/cobalt/test_tenancy.py`, `tests/cobalt/test_voice_card_stop.py`, `test_voice_cli.py`, `test_voice_config.py`, `test_voice_confirm.py`, `test_voice_fix_r1_runs.py`, `test_voice_lifecycle.py`, `test_voice_plan.py`, `test_voice_resolve.py`, `test_voice_scratch.py`, `test_voice_store.py`, `test_voice_tools.py`, `test_voice_transcribe.py`, `test_voice_turn.py`, `test_voice_web.py`, `tests/fixtures/voice/plan-replies.constructed.yaml`, `tests/fixtures/voice/plan-utterances.constructed.yaml`, `uv.lock`. Excluded (10): `jobs.yaml`, `__init__.py`, `test_archiver_migrations.py`, `test_jobs_restarts.py`, `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_panel_cards.py`, `test_radar_score_migration.py`, `test_tenancy.py`, `test_voice_store.py`. (b) over the other 50 (incl. `pyproject.toml`, `uv.lock`) → (nothing, exit 0). **U1 voice: 60 paths, 10 seam paths excluded, diff EMPTY.**
(Path counts are this seat's own count of the (a) lines as printed; the (b) calls carried every non-seam path as its own argument.)

**U2 — non-docs union at the fix tip.** `git -C /Users/cobalt/cobalt diff --stat 2b71fe49 41c9c962 -- . ':(exclude)docs'` → exit 0; 157 path lines (full list identical in shape to `39`'s union plus `tests/cobalt/test_jobs_reads.py | 15 +-`); the lines this fix moves: `configs/cobalt/jobs.yaml | 31 +-`, `tests/cobalt/test_jobs_reads.py | 15 +-`, `pyproject.toml | 1 +`, `uv.lock | 125 +++++`. Summary WHOLE:
```
 157 files changed, 15263 insertions(+), 165 deletions(-)
```
= `39`'s `156 files changed, 15245 insertions(+), 162 deletions(-)` + this fix (`2 files changed, 18 insertions(+), 3 deletions(-)`; `jobs.yaml` already in the 156). `git -C /Users/cobalt/cobalt diff --stat 2b71fe49 57420087 -- tests/cobalt/test_jobs_reads.py` → (nothing, exit 0): no branch touches it. EXPECTED `157 files changed` — MET.

**U3** — run inside W: (c1b) at `0013`, (c3) at `0017` (below).

**U4** — W (c1)'s command text is copied WHOLE under `## W WITH-DB` (c1).

**U5 — `<on>` is docs-only above `<seam tip>`.** `git -C /Users/cobalt/cobalt diff --stat a7296b44 57420087 -- . ':(exclude)docs'` → (nothing, exit 0).

## S THE STALE LINES
Report-only; no file edited (`39` rule (e) `:137`, rule (a) `:100`–`:115`). Each grep at `<tip>`, from the worktree:
- `grep -n -F "is registered last in" "docs/40 - DevDocs/cobalt/db_migrations/__init__.md"` → `158:under L72 P-b) is registered last in \`FORWARD\` and first in \`REVERSE\`. It` →
  **`DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:157–158 — "\`0014_radar_handicap\` (float handicap H1, 2026-09-24; the number settled under L72 P-b) is registered last in \`FORWARD\` and first in \`REVERSE\`."`** (on the stack `0017` is last in `FORWARD` and first in `REVERSE`: `src/cobalt/db_migrations/__init__.py:109`, `:114`).
- `grep -n -F "re-pointed with" "docs/40 - DevDocs/cobalt/db_migrations/__init__.md"` → `170:- **Numbering:** … The migration-list tests are re-pointed with \`0015\` at the head; every \`0013\` membership pin is kept.` →
  **`DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:170 — "The migration-list tests are re-pointed with \`0015\` at the head; every \`0013\` membership pin is kept."`** (on the stack `0017` is at the head).
- `grep -n -F "0012–0016 belong to" "docs/40 - DevDocs/cobalt/db_migrations/__init__.md"` → `175:(first). The number is the desk's L68 assignment: 0012–0016 belong to` → CARRIED from `39` (its report `:300`):
  **`DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175 — "The number is the desk's L68 assignment: 0012–0016 belong to unmerged branches (bars chunk 2, the setups build, H1, DRC D1, the stale-score reserve), so the registry reads \`…, 0011, 0017\` until they land"`**.
- `grep -n -F "reverses exactly 0011 then" src/cobalt/db_migrations/__init__.py` → `75:by the numeric prefix, so \`--down-to 0009\` reverses exactly 0011 then` →
  **`DOCSTRING STALE: src/cobalt/db_migrations/__init__.py:74–76 — "\`_rollback_paths\` selects by the numeric prefix, so \`--down-to 0009\` reverses exactly 0011 then 0010, and \`--down-to 0007\` reverses those two plus P4's pair."`** (on the stack `--down-to 0009` also reverses 0017, 0015, 0014 and 0013; kept byte for byte by rule (a), `39:113`).
Every grep hit the prompt's line; no STALE LINE NOT FOUND.

## O OFFLINE
- `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → `ls: …/.env: No such file or directory` ✔.
- `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` (background, on `41c9c962`) → exit 0.
- **`<p>`**, the summary WHOLE: `3199 passed, 383 skipped, 1 xfailed, 20 warnings in 550.83s (0:09:10)` → **0 failed, 0 errors** ✔ (read 15:06:13 EDT). EXPECTED `3199 passed` (`39`'s 3198 + F1 (b)) — MET.

## W WITH-DB
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (lock FREE). `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 0, no output (by name, never read). `ls -la /Users/cobalt/cobalt-wt/*/.env` → EXACTLY one line: `-rw-------  1 cobalt  staff  2186 Sep 25 15:06 /Users/cobalt/cobalt-wt/stacked-0925/.env` ✔. **L76 lock taken 15:06:20 EDT** (`date`).
- (b) `ls -la …/.env` (LISTED) → `<FP>` → `cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87` = **`<F0>`** (= `39`'s F0). `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → exit 0: `cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)`; 29 tables probed; no `CHANGED` line; `voice_turns          user    -        -            -` (absent, as at `0013`); `cobalt_redactions    system  system   174          cbca1e7a4517fb5b6a987f70ac1468fd`; `29 table(s) probed on cobalt_dev; … aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. Proof cost: total 5.6 s …`; `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`; `code: 41c9c962 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/stacked-0925` (the untracked report). `cobalt_dev` at `0013` ✔.
- (c1) PASS 1 at `0013`, launched 15:06:40 EDT (background). **U4 — the executed command text, WHOLE, byte for byte:**
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
```
  (eight `--deselect` arguments naming nine tests — `TestMigrationRoundTrip` carries two, `39:165`.)
  → **exit 0**. **`<d1>` summary WHOLE: `3567 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 640.18s (0:10:40)`** → **0 failed, 0 errors, 9 deselected** ✔ (read 15:17:31 EDT). No `DeadlockDetected`. COUNT: `39`'s 3566 + F1 (b)'s new test (an offline test that pass 1's whole-suite run also collects) = 3567.
  - SKIPPED lines (all 6, verbatim — `39`'s known set exactly): `tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev` · `tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged` · `tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof` · `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` · `tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft` · `tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof`.
- (c1b) U3 AT `0013`: `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction` (foreground) → exit 0. `<u3a>`:
```
PASSED tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply
PASSED tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction
2 passed in 0.22s
```
  (captured stdout: each test applies FORWARD through 0014 / 0017 and rolls back `0017`, `0015`, `0014` inside its own connection.) **U3 at 0013: H1 PASSED · stale PASSED** — EXPECTED `2 passed`, MET.
- (c2) FORWARD: `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate` (timeout 600000, foreground) → exit 0. **`dev forward: APPLIED 15:17:53 EDT`**. Output: `cobalt db migrate — FORWARD on cobalt_dev`; `-- applying 0001_schemas.sql` … `-- applying 0011_archive_incidents.sql`, `-- applying 0013_tunables_slug_nullable.sql`, `-- applying 0014_radar_handicap.sql`, `-- applying 0015_shadow_agreement_stale.sql`, `-- applying 0017_voice_turns.sql` (0014 → 0015 → 0017 in that order ✔); 28 pre-existing tables `OK` (digest before = after); `voice_turns          user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED` — the only created table ✔; no `CHANGED`; `29 table(s) proven; … content UNCHANGED on every table.`; `proof cost: BEFORE 5.7 s + AFTER 5.7 s = total 11.4 s; slowest table bars (5.6 s before).`; `code: 41c9c962 (DIRTY: 1 path(s))`.
  - Observation (not a stop, as `39` ESC): `cobalt_redactions` read `174` / `cbca1e7a` at (b) (15:06) and `175 -> 175` / `df5a84a6 -> df5a84a6` here — one row added between the two reads (during pass 1), not by the migrate. Writer not visible to this run's reads (L35/L70). `<FP>` counts schema only.
  - `ls -la …/.env` (LISTED) → `<FP>` → **`<F1>` = cols `716` · rels `36` · views_md5 `5727e9dfb418376cc48722a3601ca7c3`** (≠ `<F0>` ✔; = `39`'s F1).
- (c3) U3 AT `0017` (information only): `ls -la …/.env` (LISTED) → the SAME command as (c1b) → exit 1. `<u3b>`:
```
PASSED tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction
  FAILED tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply - AssertionError: assert not ({'below_cap_streak', 'closed_scan_id', 'entered...
1 failed, 1 passed in 0.26s
```
  H1's first failing assertion, verbatim:
```
>           assert not (before_cols & set(COLUMNS))                   # cobalt_dev holds no 0014
E           AssertionError: assert not ({'below_cap_streak', 'closed_scan_id', 'entered_at', 'excluded_by', 'first_seen_at', 'handicap', ...} & {'handicap', 'handicap_factor', 'raw_rank'})
E            +  where {'handicap', 'handicap_factor', 'raw_rank'} = set(('raw_rank', 'handicap_factor', 'handicap'))
tests/cobalt/test_radar_handicap_store.py:175: AssertionError
```
  **U3 at 0017: H1 FAILED · stale PASSED** — `40`'s reading confirmed by run (row 11 HOLDS; row 7 DOES NOT HOLD). Not a stop, not a gate (L70); the run continues to (d).
- (d) PASS 2 at `0017`: `ls -la …/.env` (LISTED) → `39:167`'s command byte for byte (the nine ids; background) → **exit 0**. **`<d2>` summary WHOLE: `9 passed, 5 warnings in 135.70s (0:02:15)`** → 0 failed, 0 errors, 9 passed ✔; no SKIPPED line (`grep -c -F "SKIPPED"` on the output → `0`).
- **`<d>` = `<d1>` 3567 + `<d2>` 9 = 3576 passed, 0 failed.** COUNT: with-DB 3576 vs `39`'s 3575 — +1 = F1 (b)'s new offline test, collected by pass 1's whole-suite run (the prompt's "no with-DB test added" holds; the whole-suite pass counts every test).
- (d2) VALIDATE: `ls -la …/.env` (LISTED) → `COBALT_ENV=production uv run cobalt validate` → exit 0. Verbatim: `Jobs (F17): 16 registered — 6 resident, 10 one-shot. Kill phrase 'COBALT STOP'.` · `registry <-> ops/: 16 label(s), exact match.` · `registry <-> plists: schedules and COBALT_ENV agree on every job.` · `reads: 10 config path(s) re-read at runtime by 3 resident(s); every path exists, every one-shot empty.` with every `-> ` line: `configs/cobalt/agents/voice.yaml -> com.cobalt.aset` · `configs/cobalt/backup.yaml -> com.cobalt.aset` · `configs/cobalt/modelaccess.yaml -> com.cobalt.aset` · `configs/cobalt/radar.yaml -> com.cobalt.radar` · `configs/cobalt/taxonomy/tunables.yaml -> com.cobalt.aset, com.cobalt.radar` · `configs/cobalt/voice.yaml -> com.cobalt.aset` · `configs/dev/aset.yaml -> com.cobalt.aset` · `ops/start_aset.sh -> com.cobalt.aset` · **`pyproject.toml -> com.cobalt.aset, com.cobalt.agent, com.cobalt.radar`** · **`uv.lock -> com.cobalt.aset, com.cobalt.agent, com.cobalt.radar`** (EXPECTED — MET; `39`'s `by 2 resident(s)` → now 3) · `Placement (docs/PLACEMENT.md): tree clean.` · known, not a stop: `literal guard: INACTIVE — vault file /Users/cobalt/cobalt-wt/stacked-0925/data/.cobalt_vault does not exist — literal guard INACTIVE.` No violation line. Also `13 trade_def(s) validated OK from the vault.`, `9 draft(s) skipped`.
- (e) LIVE-NOTE LEG (read-only): `ls -la …/.env` (LISTED) → `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0. **`<l>` summary WHOLE: `146 passed, 1 skipped, 15 warnings in 26.17s`** → 0 failed, 0 errors ✔. The one SKIPPED line: `tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (known); NO skip naming `COBALT_LIVE_VAULT_ROOT` ✔. `39`: 146/1 — equal.
- (f) THE L76 RELEASE:
  1. `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (timeout 600000, foreground) → exit 0: `cobalt db migrate — ROLLBACK on cobalt_dev` / `-- applying 0017_voice_turns.rollback.sql` / `-- applying 0015_shadow_agreement_stale.rollback.sql` / `-- applying 0014_radar_handicap.rollback.sql` — newest first, nothing at or below `0013` ✔; 28 tables `OK`; `voice_turns          user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED`; `29 table(s) proven; … content UNCHANGED on every table.`; `code: 41c9c962 (DIRTY: 1 path(s))`.
  2. `ls -la …/.env` (LISTED) → `<FP>` → `<F2>` = cols `664` · rels `35` · views_md5 `272c95bbb12241e3611e4b36326ccf87`. **`cobalt_dev: 0013 — F2 = F0 (664 · 35 · 272c95bbb12241e3611e4b36326ccf87)`** ✔.
  3. `rm /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 0; `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. **`.env: removed, proven gone (L76 lock released 15:21:35 EDT)`**.

## RESTARTS
`ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → `No such file or directory` ✔. `COBALT_ENV=production uv run cobalt jobs restarts 2b71fe49..41c9c962` → exit 0. The table VERBATIM (every row):
```
path	change	rule	restart
configs/cobalt/agents/voice.yaml	A	resident reads	com.cobalt.aset
configs/cobalt/jobs.yaml	M	registry; register, no restart	-
configs/cobalt/modelaccess.yaml	A	resident reads	com.cobalt.aset
configs/cobalt/radar.yaml	M	resident reads	com.cobalt.radar
configs/cobalt/taxonomy/tunables.yaml	M	resident reads	com.cobalt.aset,com.cobalt.radar
configs/cobalt/voice.yaml	A	resident reads	com.cobalt.aset
docs/10 - Decisions/ADR-0009-radar-cards-seam-and-precondition-ast.md	M	DOCS	-
docs/10 - Decisions/ADR-0010-missed-corpus-counterfactual-r-picks.md	M	DOCS	-
docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/card_stop.md	A	DOCS	-
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/scoring.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cards/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/__init__.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/db_migrations/placement.md	M	DOCS	-
docs/40 - DevDocs/cobalt/modelaccess/__init__.md	A	DOCS	-
docs/40 - DevDocs/cobalt/modelaccess/adapters.md	A	DOCS	-
docs/40 - DevDocs/cobalt/modelaccess/client.md	A	DOCS	-
docs/40 - DevDocs/cobalt/modelaccess/config.md	A	DOCS	-
docs/40 - DevDocs/cobalt/modelaccess/guard.md	A	DOCS	-
docs/40 - DevDocs/cobalt/modelaccess/models.md	A	DOCS	-
docs/40 - DevDocs/cobalt/radar/audit_export.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/config.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/evaluate_cli.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/handicap.md	A	DOCS	-
docs/40 - DevDocs/cobalt/radar/handicap_dry_run.md	A	DOCS	-
docs/40 - DevDocs/cobalt/radar/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/pool.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/radar/store.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/formations.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/line.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/models.md	M	DOCS	-
docs/40 - DevDocs/cobalt/replay/runner.md	M	DOCS	-
docs/40 - DevDocs/cobalt/voice/__init__.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/agent.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/cli.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/config.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/confirm.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/models.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/registry.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/resolve.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/scratch.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/store.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/tools.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/transcribe.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/turn.md	A	DOCS	-
docs/40 - DevDocs/cobalt/voice/web.md	A	DOCS	-
docs/40 - DevDocs/reports/handicap-h1-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/reports/handicap-h1-fix-r1-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/reports/handicap-h1-fix-r2-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/reports/replay-deadline-fix-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/reports/stack-seam-build-2026-09-25.md	A	DOCS	-
docs/40 - DevDocs/reports/stale-score-build-2026-09-23.md	A	DOCS	-
docs/40 - DevDocs/reports/stale-score-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md	A	DOCS	-
docs/40 - DevDocs/reports/voice-v1-fix-r1-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/reports/voice-v1-fix-r2-build-2026-09-24.md	A	DOCS	-
docs/40 - DevDocs/tests/fixtures/voice/_voice_fixtures.md	A	DOCS	-
ops/start_aset.sh	M	resident reads	com.cobalt.aset
pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/card_stop.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cards/scoring.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cards/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/0014_radar_handicap.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0014_radar_handicap.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0015_shadow_agreement_stale.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0017_voice_turns.rollback.sql	A	non-Python src asset	-
src/cobalt/db_migrations/0017_voice_turns.sql	A	non-Python src asset	-
src/cobalt/db_migrations/__init__.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/db_migrations/placement.py	M	static import reach	com.cobalt.radar
src/cobalt/modelaccess/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/modelaccess/adapters.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/modelaccess/client.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/modelaccess/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/modelaccess/guard.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/modelaccess/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/audit_export.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/config.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/evaluate_cli.py	M	static import reach	com.cobalt.radar
src/cobalt/radar/handicap.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/handicap_dry_run.py	A	static import reach	com.cobalt.radar
src/cobalt/radar/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/pool.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/runner.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/radar/store.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/formations.py	M	static import reach	com.cobalt.radar
src/cobalt/replay/line.py	M	static import reach	com.cobalt.radar
src/cobalt/replay/models.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/replay/runner.py	M	static import reach	com.cobalt.radar
src/cobalt/voice/__init__.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/agent.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/cli.py	A	static import reach	com.cobalt.radar
src/cobalt/voice/config.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/confirm.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/models.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/registry.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/resolve.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/scratch.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/store.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/tools.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/transcribe.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/turn.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/voice/web.py	A	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/radar_migrated_support.py	A	test/documentation; no resident	-
tests/cobalt/stale_db_support.py	A	test/documentation; no resident	-
tests/cobalt/test_archiver_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_assumed_store.py	M	test/documentation; no resident	-
tests/cobalt/test_cards_picks.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/cobalt/test_modelaccess_client.py	A	test/documentation; no resident	-
tests/cobalt/test_modelaccess_config.py	A	test/documentation; no resident	-
tests/cobalt/test_modelaccess_silence.py	A	test/documentation; no resident	-
tests/cobalt/test_p4_migrations.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_evaluate.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_evaluate_cli.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_handicap.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_dead.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_dry_run.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_fix_r1_runs.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_group.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_panel.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_runner.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_shadow.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_handicap_store.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_migrated_harness.py	A	test/documentation; no resident	-
tests/cobalt/test_radar_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_replay.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_score_migration.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_store.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_formations.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_line.py	M	test/documentation; no resident	-
tests/cobalt/test_replay_runner.py	M	test/documentation; no resident	-
tests/cobalt/test_rubberband_forms.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_d1.py	M	test/documentation; no resident	-
tests/cobalt/test_setups_registries.py	M	test/documentation; no resident	-
tests/cobalt/test_stale_score.py	A	test/documentation; no resident	-
tests/cobalt/test_stale_score_db.py	A	test/documentation; no resident	-
tests/cobalt/test_tenancy.py	M	test/documentation; no resident	-
tests/cobalt/test_voice_card_stop.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_cli.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_config.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_confirm.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_fix_r1_runs.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_lifecycle.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_plan.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_resolve.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_scratch.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_store.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_tools.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_transcribe.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_turn.py	A	test/documentation; no resident	-
tests/cobalt/test_voice_web.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/conftest.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/h1_cache.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/h1_support.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x0_grouping.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x1_blanks.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x3_cell_format.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x4_rollback_hazard.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x5_x6_x7_reads.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x8_x11_group.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_h1_x9_x10_x15_sources.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_x12_identity.py	A	test/documentation; no resident	-
tests/experiments/handicap_h1/test_xl76_membership_harness.py	A	test/documentation; no resident	-
tests/experiments/stale_score/conftest.py	A	test/documentation; no resident	-
tests/experiments/stale_score/stale_predicates.py	A	test/documentation; no resident	-
tests/experiments/stale_score/stale_support.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x10_replay_as_of.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x11_audit_replay_fallback.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x12_published_null.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x13_tap_keeps_sentence_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x14_daily_missing_keeps_proximity.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x15_two_clocks.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x16_last_price_coalesce_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x18_x19_callers.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x20_x22_bindings.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x21_htf_tap_no_pair_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x23_next_day_card_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x24_no_print_minutes_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x25_stale_graded_taps_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x26_slug_match_not_evaluable.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x27_reason_bytes.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x28_proximity_one_receipts_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x29_ladder_render.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x2_stale_sequence_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x30_r40_discriminator_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x3_taps_moved_null_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x4_audit_stale_card.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x5b_prior_session_bars.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x6_htf_proximity_stale.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x7_ladder_promoted_stale.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x8_expiry_on_stale.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_x9_stale_scored_cards_db.py	A	test/documentation; no resident	-
tests/experiments/stale_score/test_xl76_devdb_absence.py	A	test/documentation; no resident	-
tests/fixtures/radar/screen-handicap.real-shape.csv	A	test/documentation; no resident	-
tests/fixtures/voice/plan-replies.constructed.yaml	A	test/documentation; no resident	-
tests/fixtures/voice/plan-utterances.constructed.yaml	A	test/documentation; no resident	-
uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar
```
- No `UNCLASSIFIED` / `UNCLASSIFIED CONFIG` row → **UNCLASSIFIED: 0**.
- **`RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`** — as derived; = the drafter's reading (`43`). `com.cobalt.agent` enters through the `pyproject.toml` and `uv.lock` rows only (rule `resident reads`); no `src/` row reaches it (the old tree is untouched).

## FOR THE DEPLOY
(Re-issues `39`'s section for `42`; `42`'s re-issue reads THIS one.)
- `<main-at-cut>` `2b71fe49` · `<set>` FOUR · merges `f2377218` (replay) → `35397ed5` (H1) → `91c631ac` (stale) → `00e2b7ff` (voice) · `39`'s registry commit `a7296b44` · **THE FIX COMMIT `41c9c962`** (the commit every suite of this build ran on — `42`'s `<seam tip>`) · the branch tip is ONE docs commit above `41c9c962` (this report) — `42`'s `<gate sha>`, read by the desk from `git -C /Users/cobalt/cobalt log --format=%h -1 deploy/stacked-0925` after CLOSE.
- First-parent shape above `<main-at-cut>`, `git -C /Users/cobalt/cobalt-wt/stacked-0925 log --oneline --first-parent 2b71fe49..HEAD` (read 15:21:58 EDT, before this report's commit — the report commit lands on top of the first line):
```
41c9c962 fix(jobs): com.cobalt.agent re-reads pyproject.toml, uv.lock — it starts through uv run (cobalt.sh:59), the rule aset and radar carry (stack seam fix r1, L42)
57420087 docs(stack-seam): stack seam build report — a7296b44 (FOUR)
a7296b44 chore(jobs): classify voice V1's six paths — aset reads voice/agents-voice/modelaccess yaml, start_aset.sh, pyproject.toml, uv.lock; radar reads pyproject.toml, uv.lock (stack seam, L42)
00e2b7ff Merge branch 'voice/v1-0923' into deploy/stacked-0925
91c631ac Merge branch 'cards/stale-score-0922' into deploy/stacked-0925
35397ed5 Merge branch 'radar/handicap-h1-0922' into deploy/stacked-0925
f2377218 Merge branch 'fix/replay-deadline-0924' into deploy/stacked-0925
```
  `42` STEP-G1's `--no-merges … ':(exclude)docs' ':(exclude)tests'` log now prints TWO seam commits (`a7296b44` and `41c9c962`), not one.
- SEAM PATHS: `39`'s list (its `## FOR THE DEPLOY`) PLUS `tests/cobalt/test_jobs_reads.py` (this fix; no branch touches it — U2) · `configs/cobalt/jobs.yaml` changed again (the agent block). U2 summary: ` 157 files changed, 15263 insertions(+), 165 deletions(-)` (EXPECTED 157 — MET).
- THE REGISTRY LINES: `39`'s (aset six, radar two) + this fix's agent two — `configs/cobalt/jobs.yaml` `com.cobalt.agent` `reads:` = `"pyproject.toml"`, `"uv.lock"`, each `# cobalt.sh:59 (nohup uv run src/cobalt_agent/main.py), started by ops/com.cobalt.agent.plist:25 (cobalt.sh start): uv syncs the environment from it when the process starts`; the diff WHOLE under `## F THE FIX` F5. validate now reads `by 3 resident(s)`.
- **RESTARTS as derived: `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`**. The four rows:
  - `pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar`
  - `uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar`
  - `configs/cobalt/jobs.yaml	M	registry; register, no restart	-`
  - `tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-`
  `com.cobalt.agent` IS in the set: `42`'s G03 / G4 / STEP-4 / STEP-5 / (f) literals grow by the agent, and the agent's restart is a NEW string set on his list (`43`'s `## FOR 42` K10–K24 / `## FOR DEJAN`: `cobalt.sh status`, `cobalt.sh stop`, `launchctl kickstart gui/501/com.cobalt.agent`, `ps -p *`).
- Migration facts UNCHANGED: `0014` → `0015` → `0017`; `cobalt_dev` back at `0013` (F2 = F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`); the with-DB leg ran as `39`'s TWO passes (`3567` at `0013` + `9` at `0017` = `3576`). U3: **at 0013: H1 PASSED · stale PASSED**; **at 0017: H1 FAILED · stale PASSED** (H1 `test_radar_handicap_store.py:175` `assert not (before_cols & set(COLUMNS))  # cobalt_dev holds no 0014` — the two-pass shape is required for the H1 half; the stale half does not need it).
- The four STALE lines:
  - `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:157–158 — "\`0014_radar_handicap\` (float handicap H1, 2026-09-24; the number settled under L72 P-b) is registered last in \`FORWARD\` and first in \`REVERSE\`."`
  - `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:170 — "The migration-list tests are re-pointed with \`0015\` at the head; every \`0013\` membership pin is kept."`
  - `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175 — "The number is the desk's L68 assignment: 0012–0016 belong to unmerged branches (bars chunk 2, the setups build, H1, DRC D1, the stale-score reserve), so the registry reads \`…, 0011, 0017\` until they land"`
  - `DOCSTRING STALE: src/cobalt/db_migrations/__init__.py:74–76 — "\`_rollback_paths\` selects by the numeric prefix, so \`--down-to 0009\` reverses exactly 0011 then 0010, and \`--down-to 0007\` reverses those two plus P4's pair."`
- Rollback (L54): unchanged — `42`'s ONE `git revert -m 2` of the gate merge undoes the four merges, the registry commit and this fix together.

## FOR THE CHECK
- The fix range `57420087..41c9c962`: `git -C /Users/cobalt/cobalt-wt/stacked-0925 show --stat 41c9c962` quoted under `## F THE FIX` F5 (`configs/cobalt/jobs.yaml | 6 ++++--`, `tests/cobalt/test_jobs_reads.py | 15 ++++++++++++++-`, `2 files changed, 18 insertions(+), 3 deletions(-)`); the F5 diff WHOLE there.
- F2 `<red>` WHOLE (`1 failed, 23 passed`; the one failure the new pin, `assert [] == ['pyproject.toml', 'uv.lock']`), `<red hash>` `57420087`; F4 `<green>` `42 passed in 11.19s`.
- The PREFLIGHT input greps (FIX 1's inputs, `## PREFLIGHT`) and F3's three proof greps (`6`, `3`, six keys + `no_resident_reads:`).
- U1–U5 under `## U THE RUNS` (U1 four × EMPTY; U2 `157 files changed`; U3 `H1 PASSED · stale PASSED` at 0013, `H1 FAILED · stale PASSED` at 0017; U4 the pass-1 text WHOLE under `## W WITH-DB` (c1); U5 EMPTY).
- The RESTARTS table WHOLE (above) and the exact line `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.
- The four STALE lines (`## S THE STALE LINES`) and: `no DevDoc edited (rule (e)); no docstring edited (rule (a)); git -C /Users/cobalt/cobalt-wt/stacked-0925 show --stat 41c9c962 names only configs/cobalt/jobs.yaml and tests/cobalt/test_jobs_reads.py`.

## CONTINUE
next: none — CLOSE done (this report committed). cobalt_dev at 0013, .env removed.

## ESCALATE
1. **The agent is in the derived set (desk item for `42`):** `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`. `42` must be re-issued with `43`'s `## FOR 42` K10–K24 and the four NEW strings of `43`'s `## FOR DEJAN` on his approval list; without them `42`'s G4 stops FAILED by design (L42: never trimmed).
2. **COUNT: with-DB 3576** (`<d1>` 3567 + `<d2>` 9) vs `44`'s EXPECTED 3575 — the +1 is F1 (b)'s new offline test, which pass 1's whole-suite run collects. Not a stop. `42` K9's `passed ≥` literal should read this build's `3576`.
3. U3 (information, L70): **U3 at 0013: H1 PASSED · stale PASSED**; **U3 at 0017: H1 FAILED · stale PASSED** — `40` row 11 (H1 red at 0017) now PROVEN by run; row 7 (stale red at 0017) proven NOT to hold. The two-pass with-DB shape stays required.
4. U4 wording: the prompt says "all nine `--deselect` ids"; the executed command carries EIGHT `--deselect` arguments naming NINE tests (`TestMigrationRoundTrip` holds two) — byte for byte `39:165`; `9 deselected` confirms.
5. Observation (not a stop; same as `39`'s ESC): `cobalt_redactions` gained one row on `cobalt_dev` during pass 1 (`174` at 15:06 → `175` at 15:17); not by the migrate (before = after inside it). Writer not visible to this run's reads (L35 / L70).
6. `validate`'s `Placement` read `tree clean` with this report untracked — no `ESCALATE: validate names the untracked fix report` line needed; recorded for the check.
7. L74: one block after the Read of `44`, recorded under `## L74`, not followed.
8. **"The fix is built by the classification (L75) and proven by the three suites on `41c9c962`. It is CHECKED by `45-stack-seam-fix-r1-check.md` (Opus 5.5 + Grok, L67) before `42`'s GATE PHASE re-proves it on the tree that ships (L68). The builder decided nothing: every change is a FIX row with its source."**

STACK SEAM FIX R1 BUILT 41c9c962 | on 57420087 | red 57420087 | offline 3199/0 | with-DB 3576/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | UNCLASSIFIED: 0 | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | FIX: 1 | RUNS: 5 | STALE: 4 | ESCALATE: 8
