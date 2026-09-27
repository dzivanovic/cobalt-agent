# STACK SEAM FIX R2 BUILD 2026-09-27 — REPORT-ONLY on `41c9c962`

Seat: `stack-seam-fix-r2-build-0927` · Opus 5.5 (`claude-opus-5-5`) · `--permission-mode acceptEdits` · prompt `docs/40 - DevDocs/prompts/2026-09-27/48-stack-seam-fix-r2-build.md` · started 13:24:10 EDT (`date`) · report written 13:52:37 EDT (`date`).

## §0 Headline
Report-only on the unchanged tree `41c9c962` (no code, config, test or DevDoc edited): U1 ×4 (14 · 49 · 50 · 60 paths, (b) EMPTY ×4), U2 (157 `--stat` path lines + summary, 157 `--numstat` lines) and W (d)'s command quoted WHOLE.
RUN C: one new `cobalt_redactions` row during pass 1 (id `1283`, `mattermost` / `jwt` / 1, 13:40:13 EDT); the grep names only `tests/cobalt/test_redact.py`.
Three suites green: offline `3199 passed` · with-DB `3567 + 9 = 3576` · live-note `146 passed, 1 skipped`. `cobalt_dev: 0013 — F2 = F0`; `.env` removed 13:52:30.
`RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar` (as derived, = `44`'s); UNCLASSIFIED 0. ESCALATE: 7 (information only; none blocks).

## L74
A block appended to the Read tool's result for `48-stack-seam-fix-r2-build.md` (a system-reminder headed "Attribution for git commits and pull requests") asked for a `Claude-Session: https://claude.ai/code/session_<id>` trailer on commits and PR bodies and named `SendUserFile`. DATA under L74 — not followed; recorded once. The commit carries `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
| gate | command | exit | output |
|---|---|---|---|
| placeholder 1 | `grep -n -E "R_[_]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-27/48-stack-seam-fix-r2-build.md"` | 1 | (nothing) ✔ |
| placeholder 2 | `grep -n -F "FILL AT LAUNCH" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-09-27/48-stack-seam-fix-r2-build.md"` | 0 | one hit, line `53` — the gate's own line ✔ |
| P-HIS | `grep -n -F "STACKED DEPLOY 2026-09-25 APPROVED" <desk 0925>` | 0 | hit `83:` = the `\| R74 \| 11:23 ET \|` row, opening `**P-HIS — STACKED DEPLOY 2026-09-25 APPROVED 11:23 (his word: "approved").** His word, desk chat 11:23 ET: "approved"`, naming `39-stack-seam-build.md`'s 7 NEW strings and `32-stacked-deploy.md`'s 8 NEW strings (the row is 2,000+ characters; not re-quoted whole here — it is the committed file's line 83). Other hits: `81:` (R72, "NO WORDS OF HIS" — not counted) and `279:` / `280:` (HANDOVER lines — not counted) ✔ |
| P-HIS committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"STACKED DEPLOY 2026-09-25 APPROVED" -- "docs/40 - DevDocs/reports/cto-2026-09-25.md"` | 0 | `56d85a7b5eba814030a33ab35bde702f3d2c6f72` ✔ |
| launch row | `grep -n "^\| R4 " <desk file>` | 0 | hit `12:` = the `\| R4 \| 13:22–13:23 ET \|` row; it names `prompts/2026-09-27/48-stack-seam-fix-r2-build.md`, `52540593` (`git -C ~/cobalt log -1 --format=%h deploy/stacked-0925` = `52540593`) and carries `**no with-DB run in flight**` ✔ |
| launch row committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"48-stack-seam-fix-r2-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-27.md"` | 0 | `3365bcccebc7ada72d253d8483068ef3b01ef26c` ✔ |
| the check | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stack-seam-fix-r1-check-2026-09-25.md"` | 0 | last non-blank line `STACK SEAM FIX R1 CHECK DONE · round: 2 · opus: CHECK: FIX STANDS · ready for the gate: YES · grok: CHECK: FIX — U1 stale names ellipsized; U2 stat body not quoted · ready for the gate: NO · defects that HOLD: 0 · ready for the gate: NO · ESCALATE: 10` ✔ |
| the check committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/reports/stack-seam-fix-r1-check-2026-09-25.md"` | 0 | `56d85a7b5eba814030a33ab35bde702f3d2c6f72` ✔ |
| the draft | `tail -n 3 "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stack-seam-fix-r2-draft-2026-09-27.md"` | 0 | last non-blank line `STACK SEAM FIX R2 DRAFTED · FIX: 3 · NOT REAL: 6 · UNPROVEN: 1 · OUT OF SCOPE: 3 · OWNER ITEM: 0 · code change: NONE · prompts: 2 · new rule strings: 0 · ESCALATE: 12` ✔ |

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| date | `date` | 0 | `Sun Sep 27 13:24:10 EDT 2026` ✔ (ET) |
| worktree clean | `git -C /Users/cobalt/cobalt-wt/stacked-0925 status --short --branch` | 0 | `## deploy/stacked-0925` ✔ |
| at `<on>` | `git -C /Users/cobalt/cobalt-wt/stacked-0925 log --oneline -2` | 0 | `52540593 docs(stack-seam-fix-r1): stack seam fix r1 build report — 41c9c962` / `41c9c962 fix(jobs): com.cobalt.agent re-reads pyproject.toml, uv.lock — it starts through uv run (cobalt.sh:59), the rule aset and radar carry (stack seam fix r1, L42)` ✔ |
| tree is `<tip>` | `git -C /Users/cobalt/cobalt diff --stat 41c9c962 52540593 -- . ':(exclude)docs'` | 0 | (nothing, exit 0) ✔ |
| lock (record) | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` ✔ |
| our `.env` | `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory` ✔ |
| live-note input | `ls "/Users/cobalt/Vault/Think/1 - Trading/4 - Strategies"` | 0 | 22 lines: `9 EMA Reclaim.md` · `9 EMA Scalp.md` · `Back Through Open.md` · `Backside Scalp.md` · `Bella Fade.md` · `Big Dog.md` · `Bouncy Ball.md` · `Fashionably Late.md` · `First Move Down.md` · `First Move Up.md` · `First VWAP Pullback.md` · `Gap Give and Go.md` · `Hitchhiker.md` · `Off Sides.md` · `Opening Range Break.md` · `Premarket High Break.md` · `Rubberband.md` · `Second Chance Scalp.md` · `Second Day Play.md` · `Spencer Scalp.md` · `The 3:30 Trade.md` · `VWAP Continuation.md` (read only) ✔ |

## R THE RE-QUOTES

### R1 = U1 — the per-branch identity, re-run (FIX R1)
(a) `git -C /Users/cobalt/cobalt diff --name-only <mb> <b> -- . ':(exclude)docs'`; (b) `git -C /Users/cobalt/cobalt diff --stat <b> 41c9c962 -- <every (a) path except the SEAM PATHS, each its own argument>`. Every (a) output below is the tool's output WHOLE, one path per line, in order.

U1 (a) fix/replay-deadline-0924 — 14 lines
```
configs/cobalt/taxonomy/tunables.yaml
src/cobalt/radar/evaluate.py
src/cobalt/radar/evaluate_cli.py
src/cobalt/replay/formations.py
src/cobalt/replay/line.py
src/cobalt/replay/models.py
src/cobalt/replay/runner.py
tests/cobalt/test_radar_evaluate.py
tests/cobalt/test_radar_evaluate_cli.py
tests/cobalt/test_replay_formations.py
tests/cobalt/test_replay_line.py
tests/cobalt/test_replay_runner.py
tests/cobalt/test_setups_d1.py
tests/cobalt/test_setups_registries.py
```
U1 (b) replay, over the 10 non-seam paths (`configs/cobalt/taxonomy/tunables.yaml src/cobalt/radar/evaluate_cli.py src/cobalt/replay/line.py src/cobalt/replay/models.py src/cobalt/replay/runner.py tests/cobalt/test_radar_evaluate.py tests/cobalt/test_radar_evaluate_cli.py tests/cobalt/test_replay_formations.py tests/cobalt/test_replay_line.py tests/cobalt/test_setups_registries.py`) → (nothing, exit 0). Excluded seam paths (4):
```
src/cobalt/radar/evaluate.py
src/cobalt/replay/formations.py
tests/cobalt/test_replay_runner.py
tests/cobalt/test_setups_d1.py
```
**U1 fix/replay-deadline-0924: 14 paths, 4 seam paths excluded, diff EMPTY.**

U1 (a) radar/handicap-h1-0922 — 49 lines
```
configs/cobalt/radar.yaml
src/cobalt/aset/radar_panel.py
src/cobalt/db_migrations/0014_radar_handicap.rollback.sql
src/cobalt/db_migrations/0014_radar_handicap.sql
src/cobalt/db_migrations/__init__.py
src/cobalt/db_migrations/cli.py
src/cobalt/radar/cli.py
src/cobalt/radar/config.py
src/cobalt/radar/handicap.py
src/cobalt/radar/handicap_dry_run.py
src/cobalt/radar/models.py
src/cobalt/radar/pool.py
src/cobalt/radar/runner.py
src/cobalt/radar/store.py
tests/cobalt/radar_migrated_support.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_assumed_store.py
tests/cobalt/test_cards_picks.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_handicap.py
tests/cobalt/test_radar_handicap_dead.py
tests/cobalt/test_radar_handicap_dry_run.py
tests/cobalt/test_radar_handicap_fix_r1_runs.py
tests/cobalt/test_radar_handicap_group.py
tests/cobalt/test_radar_handicap_panel.py
tests/cobalt/test_radar_handicap_runner.py
tests/cobalt/test_radar_handicap_shadow.py
tests/cobalt/test_radar_handicap_store.py
tests/cobalt/test_radar_migrated_harness.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_panel.py
tests/cobalt/test_radar_replay.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_radar_store.py
tests/cobalt/test_tenancy.py
tests/experiments/handicap_h1/conftest.py
tests/experiments/handicap_h1/h1_cache.py
tests/experiments/handicap_h1/h1_support.py
tests/experiments/handicap_h1/test_h1_x0_grouping.py
tests/experiments/handicap_h1/test_h1_x1_blanks.py
tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py
tests/experiments/handicap_h1/test_h1_x3_cell_format.py
tests/experiments/handicap_h1/test_h1_x4_rollback_hazard.py
tests/experiments/handicap_h1/test_h1_x5_x6_x7_reads.py
tests/experiments/handicap_h1/test_h1_x8_x11_group.py
tests/experiments/handicap_h1/test_h1_x9_x10_x15_sources.py
tests/experiments/handicap_h1/test_x12_identity.py
tests/experiments/handicap_h1/test_xl76_membership_harness.py
tests/fixtures/radar/screen-handicap.real-shape.csv
```
U1 (b) H1, over the 41 non-seam paths (every (a) line above except the 8 below, each its own argument) → (nothing, exit 0). Excluded seam paths (8):
```
src/cobalt/db_migrations/__init__.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_assumed_store.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_handicap_store.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_tenancy.py
```
**U1 radar/handicap-h1-0922: 49 paths, 8 seam paths excluded, diff EMPTY.**

U1 (a) cards/stale-score-0922 — 50 lines
```
src/cobalt/cards/scoring.py
src/cobalt/cards/store.py
src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql
src/cobalt/db_migrations/0015_shadow_agreement_stale.sql
src/cobalt/db_migrations/__init__.py
src/cobalt/radar/audit_export.py
src/cobalt/radar/evaluate.py
src/cobalt/replay/formations.py
tests/cobalt/stale_db_support.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_assumed_store.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_replay_runner.py
tests/cobalt/test_rubberband_forms.py
tests/cobalt/test_setups_d1.py
tests/cobalt/test_stale_score.py
tests/cobalt/test_stale_score_db.py
tests/cobalt/test_tenancy.py
tests/experiments/stale_score/conftest.py
tests/experiments/stale_score/stale_predicates.py
tests/experiments/stale_score/stale_support.py
tests/experiments/stale_score/test_x10_replay_as_of.py
tests/experiments/stale_score/test_x11_audit_replay_fallback.py
tests/experiments/stale_score/test_x12_published_null.py
tests/experiments/stale_score/test_x13_tap_keeps_sentence_db.py
tests/experiments/stale_score/test_x14_daily_missing_keeps_proximity.py
tests/experiments/stale_score/test_x15_two_clocks.py
tests/experiments/stale_score/test_x16_last_price_coalesce_db.py
tests/experiments/stale_score/test_x18_x19_callers.py
tests/experiments/stale_score/test_x20_x22_bindings.py
tests/experiments/stale_score/test_x21_htf_tap_no_pair_db.py
tests/experiments/stale_score/test_x23_next_day_card_db.py
tests/experiments/stale_score/test_x24_no_print_minutes_db.py
tests/experiments/stale_score/test_x25_stale_graded_taps_db.py
tests/experiments/stale_score/test_x26_slug_match_not_evaluable.py
tests/experiments/stale_score/test_x27_reason_bytes.py
tests/experiments/stale_score/test_x28_proximity_one_receipts_db.py
tests/experiments/stale_score/test_x29_ladder_render.py
tests/experiments/stale_score/test_x2_stale_sequence_db.py
tests/experiments/stale_score/test_x30_r40_discriminator_db.py
tests/experiments/stale_score/test_x3_taps_moved_null_db.py
tests/experiments/stale_score/test_x4_audit_stale_card.py
tests/experiments/stale_score/test_x5b_prior_session_bars.py
tests/experiments/stale_score/test_x6_htf_proximity_stale.py
tests/experiments/stale_score/test_x7_ladder_promoted_stale.py
tests/experiments/stale_score/test_x8_expiry_on_stale.py
tests/experiments/stale_score/test_x9_stale_scored_cards_db.py
tests/experiments/stale_score/test_xl76_devdb_absence.py
```
U1 (b) stale, over the 38 non-seam paths (every (a) line above except the 12 below, each its own argument) → (nothing, exit 0). Excluded seam paths (12):
```
src/cobalt/db_migrations/__init__.py
src/cobalt/radar/evaluate.py
src/cobalt/replay/formations.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_assumed_store.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_replay_runner.py
tests/cobalt/test_setups_d1.py
tests/cobalt/test_stale_score_db.py
tests/cobalt/test_tenancy.py
```
**U1 cards/stale-score-0922: 50 paths, 12 seam paths excluded, diff EMPTY.**

U1 (a) voice/v1-0923 — 60 lines
```
configs/cobalt/agents/voice.yaml
configs/cobalt/jobs.yaml
configs/cobalt/modelaccess.yaml
configs/cobalt/voice.yaml
ops/start_aset.sh
pyproject.toml
src/cobalt/aset/card_stop.py
src/cobalt/aset/web.py
src/cobalt/cli.py
src/cobalt/db_migrations/0017_voice_turns.rollback.sql
src/cobalt/db_migrations/0017_voice_turns.sql
src/cobalt/db_migrations/__init__.py
src/cobalt/db_migrations/placement.py
src/cobalt/modelaccess/__init__.py
src/cobalt/modelaccess/adapters.py
src/cobalt/modelaccess/client.py
src/cobalt/modelaccess/config.py
src/cobalt/modelaccess/guard.py
src/cobalt/modelaccess/models.py
src/cobalt/voice/__init__.py
src/cobalt/voice/agent.py
src/cobalt/voice/cli.py
src/cobalt/voice/config.py
src/cobalt/voice/confirm.py
src/cobalt/voice/models.py
src/cobalt/voice/registry.py
src/cobalt/voice/resolve.py
src/cobalt/voice/scratch.py
src/cobalt/voice/store.py
src/cobalt/voice/tools.py
src/cobalt/voice/transcribe.py
src/cobalt/voice/turn.py
src/cobalt/voice/web.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_jobs_restarts.py
tests/cobalt/test_modelaccess_client.py
tests/cobalt/test_modelaccess_config.py
tests/cobalt/test_modelaccess_silence.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_panel_cards.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_tenancy.py
tests/cobalt/test_voice_card_stop.py
tests/cobalt/test_voice_cli.py
tests/cobalt/test_voice_config.py
tests/cobalt/test_voice_confirm.py
tests/cobalt/test_voice_fix_r1_runs.py
tests/cobalt/test_voice_lifecycle.py
tests/cobalt/test_voice_plan.py
tests/cobalt/test_voice_resolve.py
tests/cobalt/test_voice_scratch.py
tests/cobalt/test_voice_store.py
tests/cobalt/test_voice_tools.py
tests/cobalt/test_voice_transcribe.py
tests/cobalt/test_voice_turn.py
tests/cobalt/test_voice_web.py
tests/fixtures/voice/plan-replies.constructed.yaml
tests/fixtures/voice/plan-utterances.constructed.yaml
uv.lock
```
U1 (b) voice, over the 50 non-seam paths (every (a) line above except the 10 below, each its own argument; `pyproject.toml` and `uv.lock` included) → (nothing, exit 0). Excluded seam paths (10):
```
configs/cobalt/jobs.yaml
src/cobalt/db_migrations/__init__.py
tests/cobalt/test_archiver_migrations.py
tests/cobalt/test_jobs_restarts.py
tests/cobalt/test_p4_migrations.py
tests/cobalt/test_radar_migration.py
tests/cobalt/test_radar_panel_cards.py
tests/cobalt/test_radar_score_migration.py
tests/cobalt/test_tenancy.py
tests/cobalt/test_voice_store.py
```
**U1 voice/v1-0923: 60 paths, 10 seam paths excluded, diff EMPTY.**

Counts equal `44`'s (14 · 49 · 50 · 60; excluded 4 · 8 · 12 · 10) — no `COUNT:` line, no `U1 NOT EMPTY`.

### R2 = U2 — the non-docs union at `<tip>`, re-run (FIX R2)
(a) `git -C /Users/cobalt/cobalt diff --stat 2b71fe49 41c9c962 -- . ':(exclude)docs'` → exit 0; 158 lines = 157 path lines + the summary line.

part 1 of 2 — lines 1–80
```
 configs/cobalt/agents/voice.yaml                   |  52 +++
 configs/cobalt/jobs.yaml                           |  31 +-
 configs/cobalt/modelaccess.yaml                    |  42 ++
 configs/cobalt/radar.yaml                          |   3 +
 configs/cobalt/taxonomy/tunables.yaml              |  12 +
 configs/cobalt/voice.yaml                          |  44 ++
 ops/start_aset.sh                                  |   4 +
 pyproject.toml                                     |   1 +
 src/cobalt/aset/card_stop.py                       |  68 +++
 src/cobalt/aset/radar_panel.py                     |  95 +++-
 src/cobalt/aset/web.py                             |  30 +-
 src/cobalt/cards/scoring.py                        |  60 ++-
 src/cobalt/cards/store.py                          |  32 +-
 src/cobalt/cli.py                                  |   2 +
 .../db_migrations/0014_radar_handicap.rollback.sql |  10 +
 src/cobalt/db_migrations/0014_radar_handicap.sql   |  15 +
 .../0015_shadow_agreement_stale.rollback.sql       |  16 +
 .../db_migrations/0015_shadow_agreement_stale.sql  |  48 ++
 .../db_migrations/0017_voice_turns.rollback.sql    |   5 +
 src/cobalt/db_migrations/0017_voice_turns.sql      |  72 +++
 src/cobalt/db_migrations/__init__.py               |  30 +-
 src/cobalt/db_migrations/cli.py                    |   4 +
 src/cobalt/db_migrations/placement.py              |   3 +
 src/cobalt/modelaccess/__init__.py                 |  23 +
 src/cobalt/modelaccess/adapters.py                 | 125 +++++
 src/cobalt/modelaccess/client.py                   | 165 +++++++
 src/cobalt/modelaccess/config.py                   | 134 ++++++
 src/cobalt/modelaccess/guard.py                    |  48 ++
 src/cobalt/modelaccess/models.py                   | 103 +++++
 src/cobalt/radar/audit_export.py                   |  20 +-
 src/cobalt/radar/cli.py                            |   9 +-
 src/cobalt/radar/config.py                         |  12 +
 src/cobalt/radar/evaluate.py                       | 144 ++++--
 src/cobalt/radar/evaluate_cli.py                   |  30 +-
 src/cobalt/radar/handicap.py                       | 216 +++++++++
 src/cobalt/radar/handicap_dry_run.py               | 515 +++++++++++++++++++++
 src/cobalt/radar/models.py                         |  34 +-
 src/cobalt/radar/pool.py                           |  70 ++-
 src/cobalt/radar/runner.py                         |  15 +-
 src/cobalt/radar/store.py                          |  28 +-
 src/cobalt/replay/formations.py                    |  17 +-
 src/cobalt/replay/line.py                          |   8 +-
 src/cobalt/replay/models.py                        |  15 +-
 src/cobalt/replay/runner.py                        |  36 +-
 src/cobalt/voice/__init__.py                       |  12 +
 src/cobalt/voice/agent.py                          | 175 +++++++
 src/cobalt/voice/cli.py                            | 110 +++++
 src/cobalt/voice/config.py                         | 169 +++++++
 src/cobalt/voice/confirm.py                        | 121 +++++
 src/cobalt/voice/models.py                         | 162 +++++++
 src/cobalt/voice/registry.py                       | 111 +++++
 src/cobalt/voice/resolve.py                        | 209 +++++++++
 src/cobalt/voice/scratch.py                        | 269 +++++++++++
 src/cobalt/voice/store.py                          | 201 ++++++++
 src/cobalt/voice/tools.py                          | 258 +++++++++++
 src/cobalt/voice/transcribe.py                     | 189 ++++++++
 src/cobalt/voice/turn.py                           | 441 ++++++++++++++++++
 src/cobalt/voice/web.py                            | 312 +++++++++++++
 tests/cobalt/radar_migrated_support.py             |  95 ++++
 tests/cobalt/stale_db_support.py                   | 226 +++++++++
 tests/cobalt/test_archiver_migrations.py           |  29 +-
 tests/cobalt/test_assumed_store.py                 |  11 +-
 tests/cobalt/test_cards_picks.py                   |   7 +-
 tests/cobalt/test_jobs_reads.py                    |  15 +-
 tests/cobalt/test_jobs_restarts.py                 |  70 ++-
 tests/cobalt/test_modelaccess_client.py            | 366 +++++++++++++++
 tests/cobalt/test_modelaccess_config.py            | 131 ++++++
 tests/cobalt/test_modelaccess_silence.py           |  88 ++++
 tests/cobalt/test_p4_migrations.py                 |   9 +
 tests/cobalt/test_radar_evaluate.py                | 105 +++++
 tests/cobalt/test_radar_evaluate_cli.py            | 101 ++++
 tests/cobalt/test_radar_handicap.py                | 229 +++++++++
 tests/cobalt/test_radar_handicap_dead.py           | 193 ++++++++
 tests/cobalt/test_radar_handicap_dry_run.py        | 177 +++++++
 tests/cobalt/test_radar_handicap_fix_r1_runs.py    | 187 ++++++++
 tests/cobalt/test_radar_handicap_group.py          | 257 ++++++++++
 tests/cobalt/test_radar_handicap_panel.py          | 130 ++++++
 tests/cobalt/test_radar_handicap_runner.py         |  47 ++
 tests/cobalt/test_radar_handicap_shadow.py         | 238 ++++++++++
 tests/cobalt/test_radar_handicap_store.py          | 237 ++++++++++
```
(the "..." in this block is git's own --stat abbreviation; the full names are in the --numstat block)

part 2 of 2 — lines 81–158
```
 tests/cobalt/test_radar_migrated_harness.py        |  85 ++++
 tests/cobalt/test_radar_migration.py               |   5 +-
 tests/cobalt/test_radar_panel.py                   |  14 +-
 tests/cobalt/test_radar_panel_cards.py             |   6 +
 tests/cobalt/test_radar_replay.py                  |  70 +++
 tests/cobalt/test_radar_score_migration.py         |   9 +-
 tests/cobalt/test_radar_store.py                   |   3 +-
 tests/cobalt/test_replay_formations.py             |  51 +-
 tests/cobalt/test_replay_line.py                   |  20 +
 tests/cobalt/test_replay_runner.py                 | 102 +++-
 tests/cobalt/test_rubberband_forms.py              |   3 +-
 tests/cobalt/test_setups_d1.py                     |  13 +-
 tests/cobalt/test_setups_registries.py             |   4 +-
 tests/cobalt/test_stale_score.py                   | 409 ++++++++++++++++
 tests/cobalt/test_stale_score_db.py                | 252 ++++++++++
 tests/cobalt/test_tenancy.py                       |   5 +-
 tests/cobalt/test_voice_card_stop.py               | 221 +++++++++
 tests/cobalt/test_voice_cli.py                     | 214 +++++++++
 tests/cobalt/test_voice_config.py                  | 364 +++++++++++++++
 tests/cobalt/test_voice_confirm.py                 | 251 ++++++++++
 tests/cobalt/test_voice_fix_r1_runs.py             | 180 +++++++
 tests/cobalt/test_voice_lifecycle.py               | 229 +++++++++
 tests/cobalt/test_voice_plan.py                    | 179 +++++++
 tests/cobalt/test_voice_resolve.py                 | 182 ++++++++
 tests/cobalt/test_voice_scratch.py                 | 299 ++++++++++++
 tests/cobalt/test_voice_store.py                   | 280 +++++++++++
 tests/cobalt/test_voice_tools.py                   | 252 ++++++++++
 tests/cobalt/test_voice_transcribe.py              | 200 ++++++++
 tests/cobalt/test_voice_turn.py                    | 435 +++++++++++++++++
 tests/cobalt/test_voice_web.py                     | 295 ++++++++++++
 tests/experiments/handicap_h1/conftest.py          |  35 ++
 tests/experiments/handicap_h1/h1_cache.py          |  17 +
 tests/experiments/handicap_h1/h1_support.py        | 139 ++++++
 .../experiments/handicap_h1/test_h1_x0_grouping.py |  24 +
 tests/experiments/handicap_h1/test_h1_x1_blanks.py | 108 +++++
 .../handicap_h1/test_h1_x2_marginal_seat.py        | 117 +++++
 .../handicap_h1/test_h1_x3_cell_format.py          |  56 +++
 .../handicap_h1/test_h1_x4_rollback_hazard.py      |  86 ++++
 .../handicap_h1/test_h1_x5_x6_x7_reads.py          |  91 ++++
 .../handicap_h1/test_h1_x8_x11_group.py            |  78 ++++
 .../handicap_h1/test_h1_x9_x10_x15_sources.py      |  74 +++
 tests/experiments/handicap_h1/test_x12_identity.py |  32 ++
 .../handicap_h1/test_xl76_membership_harness.py    | 195 ++++++++
 tests/experiments/stale_score/conftest.py          |  32 ++
 tests/experiments/stale_score/stale_predicates.py  |  42 ++
 tests/experiments/stale_score/stale_support.py     |  82 ++++
 .../stale_score/test_x10_replay_as_of.py           |  30 ++
 .../stale_score/test_x11_audit_replay_fallback.py  |  55 +++
 .../stale_score/test_x12_published_null.py         |  36 ++
 .../stale_score/test_x13_tap_keeps_sentence_db.py  |  29 ++
 .../test_x14_daily_missing_keeps_proximity.py      |  31 ++
 .../experiments/stale_score/test_x15_two_clocks.py |  59 +++
 .../stale_score/test_x16_last_price_coalesce_db.py |  30 ++
 .../stale_score/test_x18_x19_callers.py            |  54 +++
 .../stale_score/test_x20_x22_bindings.py           |  41 ++
 .../stale_score/test_x21_htf_tap_no_pair_db.py     |  45 ++
 .../stale_score/test_x23_next_day_card_db.py       |  29 ++
 .../stale_score/test_x24_no_print_minutes_db.py    |  56 +++
 .../stale_score/test_x25_stale_graded_taps_db.py   |  25 +
 .../test_x26_slug_match_not_evaluable.py           |  40 ++
 .../stale_score/test_x27_reason_bytes.py           |  35 ++
 .../test_x28_proximity_one_receipts_db.py          |  30 ++
 .../stale_score/test_x29_ladder_render.py          |  63 +++
 .../stale_score/test_x2_stale_sequence_db.py       |  42 ++
 .../stale_score/test_x30_r40_discriminator_db.py   |  96 ++++
 .../stale_score/test_x3_taps_moved_null_db.py      |  31 ++
 .../stale_score/test_x4_audit_stale_card.py        |  55 +++
 .../stale_score/test_x5b_prior_session_bars.py     |  34 ++
 .../stale_score/test_x6_htf_proximity_stale.py     |  31 ++
 .../stale_score/test_x7_ladder_promoted_stale.py   |  33 ++
 .../stale_score/test_x8_expiry_on_stale.py         |  39 ++
 .../stale_score/test_x9_stale_scored_cards_db.py   |  25 +
 .../stale_score/test_xl76_devdb_absence.py         |  33 ++
 .../fixtures/radar/screen-handicap.real-shape.csv  |   8 +
 tests/fixtures/voice/plan-replies.constructed.yaml | 131 ++++++
 .../voice/plan-utterances.constructed.yaml         |  84 ++++
 uv.lock                                            | 125 +++++
 157 files changed, 15263 insertions(+), 165 deletions(-)
```
(the "..." in this block is git's own --stat abbreviation; the full names are in the --numstat block)

My count: 157 path lines (80 in part 1 + 77 in part 2) + 1 summary line. Git abbreviated 41 of the 157 path lines with a leading `.../` (4 in part 1, 37 in part 2) — equal to the drafter's read of 41. Cross-check: `grep -n -F " .../"` on this report lists exactly those 41 block lines plus this one prose sentence. Summary: ` 157 files changed, 15263 insertions(+), 165 deletions(-)` — EXPECTED, MET.

(b) `git -C /Users/cobalt/cobalt diff --numstat 2b71fe49 41c9c962 -- . ':(exclude)docs'` → exit 0; `<added>\t<deleted>\t<full path>`, no abbreviation. My count: **157 lines** (80 + 77).

part 1 of 2 — lines 1–80
```
52	0	configs/cobalt/agents/voice.yaml
20	11	configs/cobalt/jobs.yaml
42	0	configs/cobalt/modelaccess.yaml
3	0	configs/cobalt/radar.yaml
12	0	configs/cobalt/taxonomy/tunables.yaml
44	0	configs/cobalt/voice.yaml
4	0	ops/start_aset.sh
1	0	pyproject.toml
68	0	src/cobalt/aset/card_stop.py
90	5	src/cobalt/aset/radar_panel.py
17	13	src/cobalt/aset/web.py
54	6	src/cobalt/cards/scoring.py
24	8	src/cobalt/cards/store.py
2	0	src/cobalt/cli.py
10	0	src/cobalt/db_migrations/0014_radar_handicap.rollback.sql
15	0	src/cobalt/db_migrations/0014_radar_handicap.sql
16	0	src/cobalt/db_migrations/0015_shadow_agreement_stale.rollback.sql
48	0	src/cobalt/db_migrations/0015_shadow_agreement_stale.sql
5	0	src/cobalt/db_migrations/0017_voice_turns.rollback.sql
72	0	src/cobalt/db_migrations/0017_voice_turns.sql
27	3	src/cobalt/db_migrations/__init__.py
4	0	src/cobalt/db_migrations/cli.py
3	0	src/cobalt/db_migrations/placement.py
23	0	src/cobalt/modelaccess/__init__.py
125	0	src/cobalt/modelaccess/adapters.py
165	0	src/cobalt/modelaccess/client.py
134	0	src/cobalt/modelaccess/config.py
48	0	src/cobalt/modelaccess/guard.py
103	0	src/cobalt/modelaccess/models.py
16	4	src/cobalt/radar/audit_export.py
8	1	src/cobalt/radar/cli.py
12	0	src/cobalt/radar/config.py
105	39	src/cobalt/radar/evaluate.py
26	4	src/cobalt/radar/evaluate_cli.py
216	0	src/cobalt/radar/handicap.py
515	0	src/cobalt/radar/handicap_dry_run.py
32	2	src/cobalt/radar/models.py
65	5	src/cobalt/radar/pool.py
12	3	src/cobalt/radar/runner.py
22	6	src/cobalt/radar/store.py
12	5	src/cobalt/replay/formations.py
7	1	src/cobalt/replay/line.py
14	1	src/cobalt/replay/models.py
31	5	src/cobalt/replay/runner.py
12	0	src/cobalt/voice/__init__.py
175	0	src/cobalt/voice/agent.py
110	0	src/cobalt/voice/cli.py
169	0	src/cobalt/voice/config.py
121	0	src/cobalt/voice/confirm.py
162	0	src/cobalt/voice/models.py
111	0	src/cobalt/voice/registry.py
209	0	src/cobalt/voice/resolve.py
269	0	src/cobalt/voice/scratch.py
201	0	src/cobalt/voice/store.py
258	0	src/cobalt/voice/tools.py
189	0	src/cobalt/voice/transcribe.py
441	0	src/cobalt/voice/turn.py
312	0	src/cobalt/voice/web.py
95	0	tests/cobalt/radar_migrated_support.py
226	0	tests/cobalt/stale_db_support.py
24	5	tests/cobalt/test_archiver_migrations.py
9	2	tests/cobalt/test_assumed_store.py
6	1	tests/cobalt/test_cards_picks.py
14	1	tests/cobalt/test_jobs_reads.py
57	13	tests/cobalt/test_jobs_restarts.py
366	0	tests/cobalt/test_modelaccess_client.py
131	0	tests/cobalt/test_modelaccess_config.py
88	0	tests/cobalt/test_modelaccess_silence.py
9	0	tests/cobalt/test_p4_migrations.py
105	0	tests/cobalt/test_radar_evaluate.py
101	0	tests/cobalt/test_radar_evaluate_cli.py
229	0	tests/cobalt/test_radar_handicap.py
193	0	tests/cobalt/test_radar_handicap_dead.py
177	0	tests/cobalt/test_radar_handicap_dry_run.py
187	0	tests/cobalt/test_radar_handicap_fix_r1_runs.py
257	0	tests/cobalt/test_radar_handicap_group.py
130	0	tests/cobalt/test_radar_handicap_panel.py
47	0	tests/cobalt/test_radar_handicap_runner.py
238	0	tests/cobalt/test_radar_handicap_shadow.py
237	0	tests/cobalt/test_radar_handicap_store.py
```
part 2 of 2 — lines 81–157
```
85	0	tests/cobalt/test_radar_migrated_harness.py
4	1	tests/cobalt/test_radar_migration.py
12	2	tests/cobalt/test_radar_panel.py
6	0	tests/cobalt/test_radar_panel_cards.py
70	0	tests/cobalt/test_radar_replay.py
6	3	tests/cobalt/test_radar_score_migration.py
2	1	tests/cobalt/test_radar_store.py
50	1	tests/cobalt/test_replay_formations.py
20	0	tests/cobalt/test_replay_line.py
94	8	tests/cobalt/test_replay_runner.py
2	1	tests/cobalt/test_rubberband_forms.py
11	2	tests/cobalt/test_setups_d1.py
3	1	tests/cobalt/test_setups_registries.py
409	0	tests/cobalt/test_stale_score.py
252	0	tests/cobalt/test_stale_score_db.py
4	1	tests/cobalt/test_tenancy.py
221	0	tests/cobalt/test_voice_card_stop.py
214	0	tests/cobalt/test_voice_cli.py
364	0	tests/cobalt/test_voice_config.py
251	0	tests/cobalt/test_voice_confirm.py
180	0	tests/cobalt/test_voice_fix_r1_runs.py
229	0	tests/cobalt/test_voice_lifecycle.py
179	0	tests/cobalt/test_voice_plan.py
182	0	tests/cobalt/test_voice_resolve.py
299	0	tests/cobalt/test_voice_scratch.py
280	0	tests/cobalt/test_voice_store.py
252	0	tests/cobalt/test_voice_tools.py
200	0	tests/cobalt/test_voice_transcribe.py
435	0	tests/cobalt/test_voice_turn.py
295	0	tests/cobalt/test_voice_web.py
35	0	tests/experiments/handicap_h1/conftest.py
17	0	tests/experiments/handicap_h1/h1_cache.py
139	0	tests/experiments/handicap_h1/h1_support.py
24	0	tests/experiments/handicap_h1/test_h1_x0_grouping.py
108	0	tests/experiments/handicap_h1/test_h1_x1_blanks.py
117	0	tests/experiments/handicap_h1/test_h1_x2_marginal_seat.py
56	0	tests/experiments/handicap_h1/test_h1_x3_cell_format.py
86	0	tests/experiments/handicap_h1/test_h1_x4_rollback_hazard.py
91	0	tests/experiments/handicap_h1/test_h1_x5_x6_x7_reads.py
78	0	tests/experiments/handicap_h1/test_h1_x8_x11_group.py
74	0	tests/experiments/handicap_h1/test_h1_x9_x10_x15_sources.py
32	0	tests/experiments/handicap_h1/test_x12_identity.py
195	0	tests/experiments/handicap_h1/test_xl76_membership_harness.py
32	0	tests/experiments/stale_score/conftest.py
42	0	tests/experiments/stale_score/stale_predicates.py
82	0	tests/experiments/stale_score/stale_support.py
30	0	tests/experiments/stale_score/test_x10_replay_as_of.py
55	0	tests/experiments/stale_score/test_x11_audit_replay_fallback.py
36	0	tests/experiments/stale_score/test_x12_published_null.py
29	0	tests/experiments/stale_score/test_x13_tap_keeps_sentence_db.py
31	0	tests/experiments/stale_score/test_x14_daily_missing_keeps_proximity.py
59	0	tests/experiments/stale_score/test_x15_two_clocks.py
30	0	tests/experiments/stale_score/test_x16_last_price_coalesce_db.py
54	0	tests/experiments/stale_score/test_x18_x19_callers.py
41	0	tests/experiments/stale_score/test_x20_x22_bindings.py
45	0	tests/experiments/stale_score/test_x21_htf_tap_no_pair_db.py
29	0	tests/experiments/stale_score/test_x23_next_day_card_db.py
56	0	tests/experiments/stale_score/test_x24_no_print_minutes_db.py
25	0	tests/experiments/stale_score/test_x25_stale_graded_taps_db.py
40	0	tests/experiments/stale_score/test_x26_slug_match_not_evaluable.py
35	0	tests/experiments/stale_score/test_x27_reason_bytes.py
30	0	tests/experiments/stale_score/test_x28_proximity_one_receipts_db.py
63	0	tests/experiments/stale_score/test_x29_ladder_render.py
42	0	tests/experiments/stale_score/test_x2_stale_sequence_db.py
96	0	tests/experiments/stale_score/test_x30_r40_discriminator_db.py
31	0	tests/experiments/stale_score/test_x3_taps_moved_null_db.py
55	0	tests/experiments/stale_score/test_x4_audit_stale_card.py
34	0	tests/experiments/stale_score/test_x5b_prior_session_bars.py
31	0	tests/experiments/stale_score/test_x6_htf_proximity_stale.py
33	0	tests/experiments/stale_score/test_x7_ladder_promoted_stale.py
39	0	tests/experiments/stale_score/test_x8_expiry_on_stale.py
25	0	tests/experiments/stale_score/test_x9_stale_scored_cards_db.py
33	0	tests/experiments/stale_score/test_xl76_devdb_absence.py
8	0	tests/fixtures/radar/screen-handicap.real-shape.csv
131	0	tests/fixtures/voice/plan-replies.constructed.yaml
84	0	tests/fixtures/voice/plan-utterances.constructed.yaml
125	0	uv.lock
```
157 numstat lines = `157 files changed` in (a). (The per-column sums were not computed by this seat; the two outputs are the same git range.)

(c) `git -C /Users/cobalt/cobalt diff --stat 2b71fe49 52540593 -- tests/cobalt/test_jobs_reads.py` → exit 0:
```
 tests/cobalt/test_jobs_reads.py | 15 ++++++++++++++-
 1 file changed, 14 insertions(+), 1 deletion(-)
```
`git -C /Users/cobalt/cobalt diff --stat 2b71fe49 57420087 -- tests/cobalt/test_jobs_reads.py` → (nothing, exit 0) — no branch touches it; only `41c9c962` does. EXPECTED, MET.

No `COUNT: U2` line (157 = 157).

## O OFFLINE
- `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 1, `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory` ✔.
- `uv run pytest -q -p no:cacheprovider tests/cobalt tests/taxonomy` (background, tree `41c9c962`) → exit 0.
- **`<p>`**, the summary WHOLE (ANSI colour codes stripped): `3199 passed, 383 skipped, 1 xfailed, 20 warnings in 552.63s (0:09:12)` → **0 failed, 0 errors** ✔ (read 13:36:57 EDT). EXPECTED `3199 passed` (`44`'s, same tree) — MET.

## W WITH-DB
- (a) `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` (lock FREE). `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 0, no output (by name, never read or printed). `ls -la /Users/cobalt/cobalt-wt/*/.env` → EXACTLY one line: `-rw-------  1 cobalt  staff  2186 Sep 27 13:37 /Users/cobalt/cobalt-wt/stacked-0925/.env` ✔. **L76 lock taken 13:37:06 EDT** (`date`).
- (b) `ls -la …/stacked-0925/.env` (LISTED) → `<FP>` →
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
  **`<F0>` = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`** (= `44`'s F0).
  `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate --proof-only` (timeout 600000, foreground) → exit 0, WHOLE:
```
cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)

table                side    schema   rows         digest                             secs
------------------------------------------------------------------------------------------
archive_incidents    system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.02
archive_progress     system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
aset_sizings         user    user     1            0824685c130da3c7cb7f0e76191a6819   0.01
bars                 system  system   1043443      2769919a57144c7bf8720110061dbf72   5.66
card_dot_taps        user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_dots            user    user     0            d41d8cd98f00b204e9800998ecf8427e   0.00
card_stop_edits      user    user     1            7599f9ab6018697c2299e20bbacace54   0.00
card_transitions     user    user     4            f181e76b208a51b503339267865c157c   0.00
cobalt_email_sends   system  system   2            fba8cf9fc07cd6c95b503af272e26639   0.00
cobalt_jobs          system  system   13           8d9b0861615861e343009f33118a4931   0.00
cobalt_kill_switch   system  system   1            2e590e87d4c9576e61d1ee0d5c90bbab   0.00
cobalt_redactions    system  system   175          df5a84a6fd77f743d9bc7b6445ae066f   0.00
day_modes            user    user     2            f2ffb4d41ed0a3bbc3dc2a1c7e6112b9   0.00
desk_grade           system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_packet          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
desk_regime          system  system   0            d41d8cd98f00b204e9800998ecf8427e   0.00
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
vault_writes         user    user     187          2c8181e1b1a4156609f49ce53c27a97f   0.02
voice_turns          user    -        -            -                                  0.00
------------------------------------------------------------------------------------------
29 table(s) probed on cobalt_dev; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. Proof cost: total 5.7 s — and a migration pays it TWICE (before and after), inside the outage.
NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.
code: 52540593 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/stacked-0925
```
  No `CHANGED`; `voice_turns` absent (`cobalt_dev` at `0013`) ✔. **`cobalt_redactions` row: `175` rows, digest `df5a84a6fd77f743d9bc7b6445ae066f`** (= the count `44` read after its pass 1 on 09-25). `code: 52540593` is HEAD (docs-only above `41c9c962`, PREFLIGHT); DIRTY = this untracked report.
- (b2) RUN C BEFORE PASS 1: `ls -la …/.env` (LISTED) → `<RQ>` = `COBALT_ENV=dev uv run cobalt db query --side system "SELECT * FROM system.cobalt_redactions ORDER BY 1 DESC LIMIT 3"` → exit 0, **`<RC0>`** WHOLE (read 13:37:26 EDT, `date` in the same turn):
```
id	ts	channel	pattern	hits
1270	2026-09-25 19:09:17.158573+00:00	mattermost	jwt	1
1257	2026-09-25 17:07:50.043564+00:00	mattermost	jwt	1
1244	2026-09-25 16:49:47.245511+00:00	mattermost	jwt	1
```
  **`<id0>` = `1270`.**
- (c1) PASS 1 at `0013`: `ls -la …/.env` (LISTED) → `date` → `Sun Sep 27 13:37:28 EDT 2026` (**pass-1 start**) → `ls -la …/.env` again (LISTED — the CWD rule wants it immediately before the pytest call) → the command below (background). **U4 — the executed command text, WHOLE, byte for byte:**
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
```
  eight `--deselect` arguments naming nine tests — TestMigrationRoundTrip holds two.
  → **exit 0**. **`<d1>` summary WHOLE (ANSI stripped): `3567 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 643.52s (0:10:43)`** → **0 failed, 0 errors, 9 deselected** ✔. Read at `date` → `Sun Sep 27 13:48:30 EDT 2026` (**pass-1 end**). No `DeadlockDetected`.
  Every SKIPPED line, verbatim (ANSI stripped) — `44`'s known six exactly:
```
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
```
- (c1a) RUN C AFTER PASS 1 (the first DB touch after pass 1): `ls -la …/.env` (LISTED) → `<RQ>` → exit 0, **`<RC1>`** WHOLE:
```
id	ts	channel	pattern	hits
1283	2026-09-27 17:40:13.413454+00:00	mattermost	jwt	1
1270	2026-09-25 19:09:17.158573+00:00	mattermost	jwt	1
1257	2026-09-25 17:07:50.043564+00:00	mattermost	jwt	1
```
  **`RUN C: before 1270 · after 1283 · new rows: 1`.** The row with `id` > `1270`: `id` `1283` · `ts` `2026-09-27 17:40:13.413454+00:00` (= 13:40:13 EDT) · `channel` `mattermost` · `pattern` `jwt` · `hits` `1` — `ts` falls BETWEEN the pass-1 start (13:37:28 EDT) and end (13:48:30 EDT): YES. (No row with an id between 1270 and 1283 is visible to this read; why the ids skip is not established here. The migrate's own proof in (c2) reads `cobalt_redactions 176` = the `175` at (b) plus one row, which agrees with one new committed row.)
  THE WRITER: `grep -rn -F "jwt" /Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt` → exit 0, WHOLE:
```
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:45:    "jwt": (
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:165:        """Each row stands on its own. If `jwt` only ever fired because
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:267:        result = redact(SAMPLES["jwt"][0], channel="test")
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:268:        assert result.describe() == "jwt x1"
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:269:        assert SAMPLES["jwt"][1] not in result.describe()
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:273:            [SAMPLES["jwt"][0], SAMPLES["jwt"][0], SAMPLES["aws_access_key_id"][0]]
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:276:        assert result.hits == {"jwt": 2, "aws_access_key_id": 1}
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:280:        text, hits = redact(SAMPLES["jwt"][0], channel="test")
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:281:        assert "[REDACTED:jwt]" in text and hits == {"jwt": 1}
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:401:        redact(SAMPLES["jwt"][0], channel="mattermost")
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:406:        assert rows[0]["pattern"] == "jwt"
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:421:        redact(SAMPLES["jwt"][0], channel="mattermost")
/Users/cobalt/cobalt-wt/stacked-0925/tests/cobalt/test_redact.py:422:        assert "[REDACTED:jwt]" in result.text
```
  **RUN C WRITER: tests/cobalt/test_redact.py** (the only file the grep names; its two `channel="mattermost"` calls with the `jwt` sample are `:401` and `:421` — which of the two committed the row is not settled by this read). Information (L70) — never a stop, never an edit, never a FIX.
- (c1b) U3 AT `0013`: `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run pytest -q -rA -p no:cacheprovider tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction` (foreground) → exit 0. **`<u3a>`** (ANSI stripped):
```
PASSED tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply
PASSED tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction
2 passed in 0.23s
```
  (captured stdout: each test applies FORWARD and rolls back `0017`, `0015`, `0014` inside its own connection.) **U3 at 0013: H1 PASSED · stale PASSED** — EXPECTED `2 passed`, MET.
- (c2) FORWARD: `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate` (timeout 600000, foreground) → exit 0. **`dev forward: APPLIED 13:48:56 EDT`** (`date`). Output WHOLE:
```
cobalt db migrate — FORWARD on cobalt_dev
-- applying 0001_schemas.sql
-- applying 0002_move_tables.sql
-- applying 0003_heartbeat_vault_outcome.sql
-- applying 0004_radar_pool.sql
-- applying 0005_heartbeat_note_absent.sql
-- applying 0006_radar_score.sql
-- applying 0007_radar_cards.sql
-- applying 0008_radar_value_movers.sql
-- applying 0009_picks_missed.sql
-- applying 0010_archive_progress.sql
-- applying 0011_archive_incidents.sql
-- applying 0013_tunables_slug_nullable.sql
-- applying 0014_radar_handicap.sql
-- applying 0015_shadow_agreement_stale.sql
-- applying 0017_voice_turns.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> system           0 -> 0          0.01 -> 0.00    d41d8cd9 -> d41d8cd9  OK
archive_progress     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.51 -> 5.47    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           176 -> 176      0.00 -> 0.00    6315b450 -> 6315b450  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
missed               user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
movers_daily         system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
picks                user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               187 -> 187      0.01 -> 0.01    2c8181e1 -> 2c8181e1  OK
voice_turns          user    - -> user                  - -> 0          0.00 -> 0.00    - -> d41d8cd9         CREATED
----------------------------------------------------------------------------------------------------------------------
29 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.6 s + AFTER 5.5 s = total 11.1 s; slowest table bars (5.5 s before).
code: 52540593 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/stacked-0925
```
  `0014` → `0015` → `0017` in that order ✔; 28 pre-existing tables `OK`; no `CHANGED`; `voice_turns` the only `CREATED` ✔.
  `ls -la …/.env` (LISTED) → `<FP>` →
```
cols	rels	views_md5
716	36	5727e9dfb418376cc48722a3601ca7c3
```
  **`<F1>` = `716 · 36 · 5727e9dfb418376cc48722a3601ca7c3`** (≠ `<F0>` ✔; = `44`'s F1).
- (c3) U3 AT `0017` (information ONLY, L70): `ls -la …/.env` (LISTED) → the SAME command as (c1b) → exit 1. **`<u3b>`** (ANSI stripped):
```
PASSED tests/cobalt/test_stale_score_db.py::test_0015_applies_twice_and_its_rollback_restores_0007s_view_inside_one_rolled_back_transaction
FAILED tests/cobalt/test_radar_handicap_store.py::test_forward_twice_on_a_populated_table_then_bounded_rollback_then_reapply - AssertionError: assert not ({'below_cap_streak', 'closed_scan_id', 'entered...
1 failed, 1 passed in 0.26s
```
  H1's first failing assertion, verbatim (ANSI stripped; the `...` inside the FAILED line above is pytest's own truncation):
```
>           assert not (before_cols & set(COLUMNS))                   # cobalt_dev holds no 0014
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E           AssertionError: assert not ({'below_cap_streak', 'closed_scan_id', 'entered_at', 'excluded_by', 'first_seen_at', 'handicap', ...} & {'handicap', 'handicap_factor', 'raw_rank'})
E            +  where {'handicap', 'handicap_factor', 'raw_rank'} = set(('raw_rank', 'handicap_factor', 'handicap'))

tests/cobalt/test_radar_handicap_store.py:175: AssertionError
```
  (the `...` inside the set literal is pytest's own repr truncation.) **U3 at 0017: H1 FAILED · stale PASSED** — equal to `44`'s reading. Not a stop, not a gate; the run continued to (d).
- (d) PASS 2 at `0017`: `ls -la …/.env` (LISTED) → the command below (background) → **exit 0**.

W (d) — the executed pass-2 command, WHOLE
```
COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped
```
  **`<d2>` summary WHOLE (ANSI stripped): `9 passed, 5 warnings in 134.83s (0:02:14)`** → 0 failed, 0 errors, 9 passed ✔. No SKIPPED line printed (`grep -c -F "SKIPPED"` on the task output → `0`).
- **`<d>` = `<d1>` 3567 + `<d2>` 9 = 3576 passed, 0 failed** (= `44`'s 3576 on the same tree; no `COUNT:` line).
- (d2) VALIDATE: `ls -la …/.env` (LISTED) → `COBALT_ENV=production uv run cobalt validate` → exit 0. The lines the prompt names, verbatim:
```
  literal guard: INACTIVE — vault file /Users/cobalt/cobalt-wt/stacked-0925/data/.cobalt_vault does not exist — literal guard INACTIVE.
Jobs (F17): 16 registered — 6 resident, 10 one-shot. Kill phrase 'COBALT STOP'.
  registry <-> ops/: 16 label(s), exact match.
  registry <-> plists: schedules and COBALT_ENV agree on every job.
  reads: 10 config path(s) re-read at runtime by 3 resident(s); every path exists, every one-shot empty.
    configs/cobalt/agents/voice.yaml -> com.cobalt.aset
    configs/cobalt/backup.yaml -> com.cobalt.aset
    configs/cobalt/modelaccess.yaml -> com.cobalt.aset
    configs/cobalt/radar.yaml -> com.cobalt.radar
    configs/cobalt/taxonomy/tunables.yaml -> com.cobalt.aset, com.cobalt.radar
    configs/cobalt/voice.yaml -> com.cobalt.aset
    configs/dev/aset.yaml -> com.cobalt.aset
    ops/start_aset.sh -> com.cobalt.aset
    pyproject.toml -> com.cobalt.aset, com.cobalt.agent, com.cobalt.radar
    uv.lock -> com.cobalt.aset, com.cobalt.agent, com.cobalt.radar
Placement (docs/PLACEMENT.md): tree clean.
```
  `by 3 resident(s)` ✔; `pyproject.toml` / `uv.lock` → aset, agent, radar ✔. Also printed: `13 trade_def(s) validated OK from the vault.` and `9 draft(s) skipped — not errors, not yet defs:`. No violation line. `literal guard: INACTIVE` — known, not a stop. `Placement` reads `tree clean` with this report untracked (as `44` recorded) — no `ESCALATE: validate names the untracked fix r2 report` line needed.
- (e) LIVE-NOTE LEG (read-only): `ls -la …/.env` (LISTED) → `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0. **`<l>` summary WHOLE (ANSI stripped): `146 passed, 1 skipped, 15 warnings in 25.78s`** → 0 failed, 0 errors ✔. The one SKIPPED line: `SKIPPED [1] tests/cobalt/test_replay_line.py:256: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (known); NO skip naming `COBALT_LIVE_VAULT_ROOT` ✔. `44`: 146/1 — equal.
- (f) THE L76 RELEASE:
  1. `ls -la …/.env` (LISTED) → `COBALT_ENV=dev uv run cobalt db migrate --rollback --down-to 0013` (timeout 600000, foreground) → exit 0, WHOLE:
```
cobalt db migrate — ROLLBACK on cobalt_dev
-- applying 0017_voice_turns.rollback.sql
-- applying 0015_shadow_agreement_stale.rollback.sql
-- applying 0014_radar_handicap.rollback.sql

table                side    schema before -> after     rows            probe secs      digest before -> after verdict
----------------------------------------------------------------------------------------------------------------------
archive_incidents    system  system -> system           0 -> 0          0.01 -> 0.00    d41d8cd9 -> d41d8cd9  OK
archive_progress     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
aset_sizings         user    user -> user               1 -> 1          0.00 -> 0.00    0824685c -> 0824685c  OK
bars                 system  system -> system           1043443 -> 1043443 5.50 -> 5.32    2769919a -> 2769919a  OK
card_dot_taps        user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_dots            user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
card_stop_edits      user    user -> user               1 -> 1          0.00 -> 0.00    7599f9ab -> 7599f9ab  OK
card_transitions     user    user -> user               4 -> 4          0.00 -> 0.00    f181e76b -> f181e76b  OK
cobalt_email_sends   system  system -> system           2 -> 2          0.00 -> 0.00    fba8cf9f -> fba8cf9f  OK
cobalt_jobs          system  system -> system           13 -> 13        0.00 -> 0.00    8d9b0861 -> 8d9b0861  OK
cobalt_kill_switch   system  system -> system           1 -> 1          0.00 -> 0.00    2e590e87 -> 2e590e87  OK
cobalt_redactions    system  system -> system           176 -> 176      0.00 -> 0.00    6315b450 -> 6315b450  OK
day_modes            user    user -> user               2 -> 2          0.00 -> 0.00    f2ffb4d4 -> f2ffb4d4  OK
desk_grade           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_packet          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
desk_regime          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
missed               user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
movers_daily         system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
picks                user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_membership     system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_pool           system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score          system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_receipt  user    user -> user               0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
radar_score_run      system  system -> system           0 -> 0          0.00 -> 0.00    d41d8cd9 -> d41d8cd9  OK
session_blocks       system  system -> system           6 -> 6          0.00 -> 0.00    b650702d -> b650702d  OK
traders              user    user -> user               1 -> 1          0.00 -> 0.00    a64e0148 -> a64e0148  OK
vault_overrides      user    user -> user               6 -> 6          0.00 -> 0.00    6a8b0520 -> 6a8b0520  OK
vault_writes         user    user -> user               187 -> 187      0.01 -> 0.01    2c8181e1 -> 2c8181e1  OK
voice_turns          user    user -> -                  0 -> -          0.00 -> 0.00    d41d8cd9 -> -         DROPPED
----------------------------------------------------------------------------------------------------------------------
29 table(s) proven; digest excludes user_id, vault_outcome, vault_reason, account_mode, pool_member_id, rank_metric, rank_value; aset_sizings: 25 card column(s) added by 0007; radar_membership: 3 card column(s) added by 0007. content UNCHANGED on every table.
proof cost: BEFORE 5.6 s + AFTER 5.4 s = total 10.9 s; slowest table bars (5.5 s before).
code: 52540593 (DIRTY: 1 path(s)) · /Users/cobalt/cobalt-wt/stacked-0925
```
     `0017`, `0015`, `0014` reversed newest first; nothing at or below `0013` ✔.
  2. `ls -la …/.env` (LISTED) → `<FP>` →
```
cols	rels	views_md5
664	35	272c95bbb12241e3611e4b36326ccf87
```
     **`cobalt_dev: 0013 — F2 = F0 (664 · 35 · 272c95bbb12241e3611e4b36326ccf87)`** ✔.
  3. `rm /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 0, no output; `ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 1, `ls: /Users/cobalt/cobalt-wt/stacked-0925/.env: No such file or directory`; `ls -la /Users/cobalt/cobalt-wt/*/.env` → exit 1, `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env`. **`.env: removed, proven gone (L76 lock released 13:52:30 EDT)`**.

## RESTARTS
`ls -la /Users/cobalt/cobalt-wt/stacked-0925/.env` → exit 1, `No such file or directory` ✔. `COBALT_ENV=production uv run cobalt jobs restarts 2b71fe49..41c9c962` → **exit 0**. The table VERBATIM (every row, header and last line included — 217 lines: header + 215 rows + the `RESTARTS:` line):
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
- **`RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`** — as derived; = `44`'s line on the same range (`stack-seam-fix-r1-build-2026-09-25.md:443`). No `ESCALATE: RESTARTS differs`.

## FOR THE DEPLOY
(Re-issues `44`'s section for `42`; `46` — `42` re-issued — reads THIS one.)
- `<main-at-cut>` `2b71fe49` · `<set>` FOUR · merges `f2377218` (replay) → `35397ed5` (H1) → `91c631ac` (stale) → `00e2b7ff` (voice) · `39`'s registry commit `a7296b44` · **THE FIX COMMIT `41c9c962`** (UNCHANGED — the commit every suite of `44` and of this build ran on; `42`'s `<seam tip>`) · the branch tip is now TWO docs commits above `41c9c962` (`44`'s report `52540593`, then this report) — `42`'s `<gate sha>` = THIS report's commit, read by the desk from `git -C /Users/cobalt/cobalt log --format=%h -1 deploy/stacked-0925` after CLOSE.
- First-parent shape above `<main-at-cut>`: `git -C /Users/cobalt/cobalt-wt/stacked-0925 log --oneline --first-parent 2b71fe49..HEAD` (read 13:52:37 EDT, BEFORE this report's commit — 8 lines; the report commit lands on top as the ninth):
```
52540593 docs(stack-seam-fix-r1): stack seam fix r1 build report — 41c9c962
41c9c962 fix(jobs): com.cobalt.agent re-reads pyproject.toml, uv.lock — it starts through uv run (cobalt.sh:59), the rule aset and radar carry (stack seam fix r1, L42)
57420087 docs(stack-seam): stack seam build report — a7296b44 (FOUR)
a7296b44 chore(jobs): classify voice V1's six paths — aset reads voice/agents-voice/modelaccess yaml, start_aset.sh, pyproject.toml, uv.lock; radar reads pyproject.toml, uv.lock (stack seam, L42)
00e2b7ff Merge branch 'voice/v1-0923' into deploy/stacked-0925
91c631ac Merge branch 'cards/stale-score-0922' into deploy/stacked-0925
35397ed5 Merge branch 'radar/handicap-h1-0922' into deploy/stacked-0925
f2377218 Merge branch 'fix/replay-deadline-0924' into deploy/stacked-0925
```
  `42` STEP-G1's `--no-merges … ':(exclude)docs' ':(exclude)tests'` log still prints TWO seam commits (`a7296b44` and `41c9c962`).
- SEAM PATHS: `44`'s list unchanged (`tests/cobalt/test_jobs_reads.py` included). U2 summary as re-run: ` 157 files changed, 15263 insertions(+), 165 deletions(-)`.
- THE REGISTRY LINES: unchanged since `44` (aset six, radar two, agent two; `44`'s F5 diff at `stack-seam-fix-r1-build-2026-09-25.md:84`–`:141`). validate reads `by 3 resident(s)` (W (d2)).
- **RESTARTS as derived: `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`**. The four rows (verbatim from the table above):
  - `pyproject.toml	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar`
  - `uv.lock	M	resident reads	com.cobalt.agent,com.cobalt.aset,com.cobalt.radar`
  - `configs/cobalt/jobs.yaml	M	registry; register, no restart	-`
  - `tests/cobalt/test_jobs_reads.py	M	test/documentation; no resident	-`
  `com.cobalt.agent` IS in the set → `42`'s K10–K24 folds (`43`'s `## FOR 42`) stand as written.
- Migration facts UNCHANGED: `0014` → `0015` → `0017`; `cobalt_dev` back at `0013` (F2 = F0 = `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`); the with-DB leg ran as `39`'s TWO passes (`3567` at `0013` + `9` at `0017` = `3576`). U3: **at 0013: H1 PASSED · stale PASSED**; **at 0017: H1 FAILED · stale PASSED**. RUN C: **before 1270 · after 1283 · new rows: 1** (`mattermost` / `jwt` / 1 at 13:40:13 EDT, inside pass 1); **RUN C WRITER: tests/cobalt/test_redact.py**.
- The four STALE lines, CARRIED from `44`'s report `:472`–`:475` VERBATIM (tree unchanged; no re-grep, no edit):
  - `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:157–158 — "\`0014_radar_handicap\` (float handicap H1, 2026-09-24; the number settled under L72 P-b) is registered last in \`FORWARD\` and first in \`REVERSE\`."`
  - `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:170 — "The migration-list tests are re-pointed with \`0015\` at the head; every \`0013\` membership pin is kept."`
  - `DEVDOC STALE: docs/40 - DevDocs/cobalt/db_migrations/__init__.md:175 — "The number is the desk's L68 assignment: 0012–0016 belong to unmerged branches (bars chunk 2, the setups build, H1, DRC D1, the stale-score reserve), so the registry reads \`…, 0011, 0017\` until they land"`
  - `DOCSTRING STALE: src/cobalt/db_migrations/__init__.py:74–76 — "\`_rollback_paths\` selects by the numeric prefix, so \`--down-to 0009\` reverses exactly 0011 then 0010, and \`--down-to 0007\` reverses those two plus P4's pair."`
- Rollback (L54): unchanged — `42`'s ONE `git revert -m 2` of the gate merge undoes the four merges, the registry commit and the fix together.

## FOR THE CHECK
- THE TREE UNCHANGED: `git -C /Users/cobalt/cobalt diff --stat 41c9c962 52540593 -- . ':(exclude)docs'` → (nothing, exit 0) (PREFLIGHT). At CLOSE, `git -C /Users/cobalt/cobalt-wt/stacked-0925 show --stat HEAD` is quoted in the builder's final message (it runs after this file is committed) — expected ONE path, this report.
- R1 — the four U1 (a) blocks (under `## R`):
  - replay: 14 lines · first `configs/cobalt/taxonomy/tunables.yaml` · last `tests/cobalt/test_setups_registries.py` · (b) (nothing, exit 0) over 10 paths, 4 excluded.
  - H1: 49 lines · first `configs/cobalt/radar.yaml` · last `tests/fixtures/radar/screen-handicap.real-shape.csv` · (b) (nothing, exit 0) over 41 paths, 8 excluded.
  - stale: 50 lines · first `src/cobalt/cards/scoring.py` · last `tests/experiments/stale_score/test_xl76_devdb_absence.py` · (b) (nothing, exit 0) over 38 paths, 12 excluded.
  - voice: 60 lines · first `configs/cobalt/agents/voice.yaml` · last `uv.lock` · (b) (nothing, exit 0) over 50 paths, 10 excluded.
- R2 — (a) `--stat`: first path line ` configs/cobalt/agents/voice.yaml                   |  52 +++`, last path line ` uv.lock                                            | 125 +++++`, 157 path lines (41 with git's `.../`), summary ` 157 files changed, 15263 insertions(+), 165 deletions(-)`; (b) `--numstat`: 157 lines, first `52	0	configs/cobalt/agents/voice.yaml`, last `125	0	uv.lock`.
- W (d)'s command block (FIX R3, headed `W (d) — the executed pass-2 command, WHOLE`) and W (c1)'s (U4) — both under `## W WITH-DB`.
- RUN C: `<RC0>` (top id `1270`), `<RC1>` (top id `1283`), `RUN C: before 1270 · after 1283 · new rows: 1`, `RUN C WRITER: tests/cobalt/test_redact.py`.
- The three suites: `<p>` `3199 passed, 383 skipped, 1 xfailed, 20 warnings in 552.63s (0:09:12)`; `<d1>` `3567 passed, 6 skipped, 9 deselected, 1 xfailed, 20 warnings in 643.52s (0:10:43)` + `<d2>` `9 passed, 5 warnings in 134.83s (0:02:14)` = `<d>` 3576; `<l>` `146 passed, 1 skipped, 15 warnings in 25.78s`. `<F0>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87` / `<F1>` `716 · 36 · 5727e9dfb418376cc48722a3601ca7c3` / `<F2>` `664 · 35 · 272c95bbb12241e3611e4b36326ccf87`. Lock taken 13:37:06 EDT, released 13:52:30 EDT. U3: `U3 at 0013: H1 PASSED · stale PASSED`; `U3 at 0017: H1 FAILED · stale PASSED`. The RESTARTS table (whole, above) and the exact line `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.
- The statement: `no code, config, test or DevDoc edited; the only commit of this build names docs/40 - DevDocs/reports/stack-seam-fix-r2-build-2026-09-27.md`.

## CONTINUE
next: none — CLOSE (this report committed by explicit path right after this write). cobalt_dev at 0013 (F2 = F0), .env removed.

## ESCALATE
1. **RUN C WRITER: tests/cobalt/test_redact.py** (information, L70). One new `cobalt_redactions` row on `cobalt_dev` during pass 1 — `1283 · 2026-09-27 17:40:13.413454+00:00 · mattermost · jwt · 1` (13:40:13 EDT, inside pass 1's 13:37:28–13:48:30). `grep -rn -F "jwt"` over `tests/cobalt` names that file only; its `redact(SAMPLES["jwt"][0], channel="mattermost")` calls are `:401` and `:421`. This read does not settle which of the two committed the row (or whether a test leaves such a row by design); the desk's standing item (R93 / R95) now has the file. Not a stop, not a FIX.
2. U3 (information, L70): **U3 at 0013: H1 PASSED · stale PASSED**; **U3 at 0017: H1 FAILED · stale PASSED** (`test_radar_handicap_store.py:175`) — identical to `44`. The two-pass with-DB shape stays required.
3. Every migrate output reads `code: 52540593 (DIRTY: 1 path(s))` (HEAD, the fix r1 report commit), where `44`'s read `code: 41c9c962` — the tree is `41c9c962`'s (PREFLIGHT: `diff --stat 41c9c962 52540593 -- . ':(exclude)docs'` empty); DIRTY = this untracked report. Information.
4. W (c1) ordering: the prompt says `ls` → `date` → the pass-1 command; the CWD rule says the call immediately before a pytest call is `ls -la …/.env`. This seat ran `ls` → `date` → `ls` → pytest to satisfy both. Information.
5. `validate`'s `Placement` read `tree clean` with this report untracked (as for `44`) — the prompt's `ESCALATE: validate names the untracked fix r2 report` case did not arise. Recorded for the check.
6. L74: one block after the Read of `48`, recorded under `## L74`, not followed.
7. **"Round 3 of ≤3 (L39) — REPORT-ONLY on the unchanged tree `41c9c962`. The re-quotes are the FIX rows of `47`'s classification (L75); RUN C is its one UNPROVEN row, run. It is CHECKED by `49-stack-seam-fix-r2-check.md` (Opus 5.5 · Sol · Grok, L67) before `46`'s GATE PHASE re-proves the tree that ships (L68). An unresolved HOLD after `49` goes to Dejan — no fourth round. The builder decided nothing."**

STACK SEAM FIX R2 BUILT 41c9c962 | on 52540593 | report-only | offline 3199/0 | with-DB 3576/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | UNCLASSIFIED: 0 | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | FIX: 3 (report) | RUNS: 1 | ESCALATE: 7
