# card 137 price floor — amend 2 · 2026-10-08

## §0 Headline
Card `137` amended in place for preflight r1's three FAILs and notes 1–3.
Registry and ~16 order-pin files joined row M; five `members_for_day` fakes joined F5; `test_radar_daily.py` joined F1.
The walk found five more pin files and one more fake than the preflight named; all are in.
Header, other rows and the radar.yaml design are unchanged.

## CHANGES
- LADDER: `OFF-LADDER — reports/cto-2026-10-08-words.md 2026-10-08 R692` (NOTE 1).
- Row M (FAIL 12): added `src/cobalt/db_migrations/__init__.py` (`0023` last in `FORWARD` after `:156`, first in `REVERSE` before `:161`, two docstring entries after `:95`, seam paragraph `:101`–`:105`) and the order-pin files with their offsets: `test_archiver_migrations`, `test_radar_score_migration`, `test_drc_k1_store`, `test_f15_p1_records_offline`, `test_assumed_store`, `test_seam_drc_s3_registry`, `test_legs_migration`, `test_stale_score_db`, `test_drc_d2_fix_r1_db`, `test_drc_d3_experiments`, `test_drc_store`, `test_voice_store`, `test_p4_migrations`, `test_radar_handicap_store`, `test_tenancy`, `test_radar_migration`. The slice comment `test_radar_score_migration.py:104` ("newest twelve" becomes "thirteen") and slices `:118`, `:123`, `:128` are named; the two cited lines are fixed (`:104`, `test_drc_k1_store.py:126`). The old row cited `:106` and `:127`.
- Row F5 (FAIL 14): added the fakes `test_replay_runner.py:407`, `:844`, `test_radar_evaluate_cli.py:31`, `:134`, and `test_replay_formations.py:78` (new), each `*, price_floor_rows=False`. Stated that `test_radar_panel.py:61` and the three real-store SQL tests stay green.
- Row F1 (FAIL 15): added `test_radar_daily.py:161` (its CSV gets `Price`).
- `## NOT IN THIS JOB` (NOTES 2, 3): the `screen_inactive` reason case (`pool.py:297`–`:302`); `dayopen/checks.py:125`–`:132` is a diagnostic, unchanged.
- `## RECORDS`: RESTARTS adds `db_migrations/__init__.py` as static import reach; new AMEND 2 record.

## DECISIONS
- The builder proves the pin set with two greps named in row M and edits only what breaks. A fixed list could miss a pin; the greps are the check. Default taken.
- `test_radar_evaluate.py`, `test_radar_replay.py` and `test_radar_runner.py` fakes bypass the collector's header check, so they are not forced to carry `Price`; row F1 keeps `Price` on the runner fake only.
- Not edited: `radar_panel.py` fake, `dev_rebuild.py:58` (a comment).

## RECORDS
- Read `docs/40 - DevDocs/prompts/2026-10-08/137-price-floor-card.md` (whole), the preflight r1 report (whole), `writing-rules.md`.
- `src/cobalt/db_migrations/__init__.py:1`–`:184`: docstring `:90`–`:95`, `:97`–`:105`; `FORWARD` `:135`–`:157` (`0022` `:156`); `REVERSE` `:160`–`:181` (`0022` `:161`).
- `grep -rn "FORWARD\[\|REVERSE\[\|forward\[\|reverse\[" tests` and `grep 0022 tests` read: every file named in row M carries a pin, with the lines in the row. `test_archiver_migrations.py:84`–`:97` (list opens at `0010`, 12 names), `:103`–`:116`, `:133`–`:148`, `:185`–`:187`. `test_radar_score_migration.py:104`, `:118`, `:123`, `:128`. `test_drc_k1_store.py:117`–`:128`. `test_legs_migration.py:30`. `test_stale_score_db.py:154`–`:157`. `test_seam_drc_s3_registry.py:20`–`:21`. `test_assumed_store.py:245`–`:264`.
- `grep -rn "members_for_day" --include=*.py`: src callers `radar_panel.py:616`, `audit_export.py:339`, `replay/runner.py:403`, `handicap_dry_run.py:511`, `evaluate_cli.py:183`, `:382`, `store.py:492`. Fakes `test_replay_runner.py:407`, `:844`; `test_radar_evaluate_cli.py:31`, `:134`; `test_replay_formations.py:78` (reaches `evaluate_cli.py:155` `replay_formations`); `test_radar_panel.py:61` (panel, unchanged). `store.py:55`–`:73` SQL params `(pool_key, trade_date)`; `test_radar_panel.py:157`–`:202` pins them.
- `test_radar_daily.py:155`–`:168`; `grep "Relative Volume" tests/cobalt/{test_radar_replay,test_radar_evaluate,test_finviz_consumers,test_radar_throttle,test_radar_propose,test_radar_collector,test_radar_runner}.py` read; only `test_radar_daily` serves a CSV through `load_config()`.
- `pool.py:295`–`:303`, `dayopen/checks.py:122`–`:133`, `dev_rebuild.py:50`–`:63`.
- `git -C /Users/cobalt/cobalt diff --stat 059da441 HEAD -- src configs tests ops` printed nothing: BASE's lines are HEAD's. HEAD `63a2ae45`.
- Not run: `uv run`, any test (no allowlist, L36).

PRICE FLOOR CARD AMENDED2 · decisions: 3
