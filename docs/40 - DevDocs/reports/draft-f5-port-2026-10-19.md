## §0 Headline
Card 731 is re-headed as the port job `f5-checkpoints-fr1` (branch `ops/f5-checkpoints-fr1`, BASE `ceb61973` = main at drafting) with ONE row, PORT: 50 non-report files of `40e646ed..ae239561` re-applied by Edit/Write, `0026` → `0027`.
28 of the 50 are touched by main (Genesis `0026`, F20, hub lines); the 18 head-pin tests are written as main's `0026` version moved one more place, not copied.
F16 close (`cli.py`, `cli.md`) and 469 (`modelaccess.yaml`, the routes pin, `gate-lists.md`, the 18 pins at `0028`) overlap the port; both are named in `## CHECK ASKS`. Neither is on main yet.
Nothing run, nothing committed. 2 decisions.

## DECISIONS
- ASK DESK 1: the port's seams with F16 and 469 are drafted against main `ceb61973`, where neither has landed (F16 deploy card 886 tip `7c5f76a3`; 469 tip `11eb0d24`). The PORT row says to re-find each seam by content and gives the rule for the pin at `test_modelaccess_config.py:51` if 469 lands first (append `checkpoint.narrative` after the last route). Default taken: the desk re-sets `BASE` to main's HEAD at the build launch, after both deploys; if the build launches before 469, the row works as written. [23:5x 2026-10-19]
- ASK DESK 2: the header `BASE` was `ea082508` when I first read main and `ceb61973` after a desk commit (`docs(desk): F5 PORT drafter launched`) landed during drafting. Default taken: `ceb61973` (the value `git -C /Users/cobalt/cobalt rev-parse --short=8 main` printed last); the old `K0` row is not run as a stop row but re-proved by the `ls`/`FORWARD`/`REVERSE` lines in PORT (1). [23:5x 2026-10-19]

## RECORDS
- `date` → `Mon Oct 19 23:53:17 EDT 2026` (first call); `git -C /Users/cobalt/cobalt rev-parse --short=8 main` → `ea082508`, then `ceb61973`.
- Read: prompt 887; card 731 whole; `prompts/2026-10-19/881-draft-hub-cos-fr1.md`; `prompts/2026-10-13/468-f21-card.md`; old build report `/Users/cobalt/cobalt-wt/f5-checkpoints-1018/docs/40 - DevDocs/reports/f5-checkpoints-build-2026-10-18.md` `:200-248`. I did not open `areas/cobalt.md` or `topics/writing-rules.md` (the prompt names the report shape; this report follows it).
- `git diff --name-only 40e646ed ae239561` → 51 names, 1 report (`f5-checkpoints-build-2026-10-18.md`), 50 ported; `git diff --name-only 40e646ed main` intersected by name → 28 touched by main (10 seam/config/doc files + 18 pin tests), 22 equal. `git diff --stat 40e646ed main` over the 28 → 196 insertions, 83 deletions.
- Main seams proved by `git grep -n` on `main`: `db_migrations/__init__.py:111,114,180,185`; `placement.py:123`; `cli.py:85,86,90,551,552,557`; `jobs.yaml:237,253,382`; `cli.md:138,141`; `test_modelaccess_config.py:51`; `test_prefill_refresh.py:391`; `DEPLOY-HUB.md:105` (was `:104` on the old card); `gate-lists.md:45,54`. `ls src/cobalt/db_migrations` ends `0026_genesis_chunk.rollback.sql`, `0026_genesis_chunk.sql`, no `0027`.
- F16 and 469 file lists: `git diff --name-only cb4e42ce 6fb73789` (5 files, `cli.py` and `cli.md` in the F5 set), `git diff --name-only 9436c975 11eb0d24` (469; overlap: `modelaccess.yaml`, `test_modelaccess_config.py`, `gate-lists.md`, `db_migrations/__init__.py`, `db_migrations/__init__.md`, the 18 pin tests), `git diff --name-only main 7c5f76a3` (F16 deploy tip).
- Edited: `docs/40 - DevDocs/prompts/2026-10-18/731-f5-card.md` only (header, row PORT, ORDER, two `## CHECK ASKS` lines, one `## RECORDS` entry).
- Not traced: the 18 pin files' per-line `0026` shapes on main (the PORT row tells the builder to find them by `git grep` and prove each); the exact line span of main's `com.cobalt.cos` jobs row (read from a diff hunk, `:206-227` approximate).

DRAFTED · decisions: 2
