# draft-f5-probe — 2026-10-21

## §0 Headline
- Card `prompts/2026-10-21/973-f5-probe-card.md` drafted: job `f5-probe`, K2, BAND HIGH, BASE `d988d543`, RESTARTS `com.cobalt.radar`, `RULINGS: 2026-10-18 R1863`. It holds no `«FILL`.
- Adds `cobalt checkpoint probe X4|X5|X6|X7|X10|X13`, dev only. Each prints one `PROBE <X> OK|FAIL|NOT RUN …` line and exits 0, 1 or 3. It writes no note, row or DM and loads no plist. X6 runs four real-shape prompts, one per slot pair. X13 is `OK (offline …)`. X5, X7 and X10 are `NOT RUN — needs his hand`.
- Row (b), the X2 real Groups fixture: this card builds the `--keep-groups` capture seam (row G1). The fixture and its parser test follow as a LOW card after the first X6 run (DECISION 3).
- Live cost per probe run: X6 = 1 gate check + 2 GETs + 4 local calls; X4 = 1 gate check + 2 GETs + 20 local calls; the rest = none.

## DECISIONS
1. ASK DESK: exit code 3 for `NOT RUN` (argparse owns 2; the cos probe has OK 0 / FAIL 1 only). [07:38 EDT] Default: 3; the gate seat reads the line, not the code.
2. ASK DESK: X6's four "real-shape prompts, each against its base". No dev rows exist (dry runs write none, the plists are unloaded) and four live fetches cost 8 GETs against 2 rpm (L53). [07:38 EDT] Default: one real fetch is 08:45's figures. The three earlier slots' figures are derived from it by rule D (index price minus k × 0.50, change minus k × 0.10, sector Change rotated k places; the X3 rotation rule). The real names and figure formats reach the guard through `narrate()`'s real path. Alternative: read today's dev `market_checkpoints` rows when present, which needs `cobalt_dev` and its lock.
3. ASK DESK: row (b), the X2 fixture "committed in this card". The builder has no network (`BUILD-HUB.md:14`), and the dry run keeps no body (`checkpoints.py:235`, `:830-832`). [07:38 EDT] Default: this card builds G1, `fetch_groups(keep=)` plus `--keep-groups PATH` on X6, which keeps the header and 11 rows, redact-checked. The first X6 run after deploy writes `/Users/cobalt/cobalt-wt/.f5-probe/groups_sector_v140_real.csv`. A LOW card then commits the fixture and `test_x2_real_groups_body_parses_as_the_eleven`. It never gates load (R2282). Alternative: the card waits on a `«FILL»` until the desk captures a body by hand. The draft-f5-x2 precedent found no desk command that fetches Finviz.
4. ASK DESK: X4's "number-word" list is undefined in `F5-FINAL:178`. [07:38 EDT] Default: zero to twenty, the tens to ninety, hundred, thousand, million, billion, half, quarter, dozen, percent. A word counts as a whole word or as a `_`-separated part. No `PHRASES` key holds one (`checkpoints.py:115-121`).
5. ASK DESK: X4 below 15 of 20 is a FINAL design consequence ("the narrative stays degraded-by-default and the card says so"), not a load stop. [07:38 EDT] Default: the probe prints `FAIL`; the line does not count until the brain rules.
6. ASK DESK: X7's offline leg already runs as the gate run's pytest (970 step 2). [07:38 EDT] Default: the probe's X7 prints `NOT RUN — needs his hand` and runs nothing, as X5 and X10 do.
7. BAND HIGH: a new module, a production seam in `fetch_groups` / `fetch_figures`, six items, live probes (complexity ≥ 7). CLASS K2 and INSTALL none, as in 877 and 965.

## RECORDS
- `date` → 07:32 EDT (start), 07:36 (card start), 07:38 EDT (card and report written). Reads only. No network, no database, no production command, no git write, nothing committed, no launch.
- `git -C /Users/cobalt/cobalt rev-parse main` → `d988d5431608…` (BASE `d988d543`). Every `file:line` in the card was read by `git show main:<path>` or `git grep … main`.
- Read whole by `git show main:`: `prompts/CARD.md`, `prompts/2026-10-19/877-cos-probe-card.md`, `src/cobalt/cos/probe.py`, `prompts/2026-10-21/970-f5-gate-run.md`, `reports/draft-f5-gate-run-2026-10-21.md`, `reports/cto-2026-10-21.md` (R2282, R2279, R2276), `src/cobalt/prefill/checkpoints.py`, `src/cobalt/modelaccess/client.py`, `guard.py`, `src/cobalt/env.py`, `tests/cobalt/test_checkpoints_offline.py`, `tests/cobalt/fixtures/checkpoints/groups_sector_v140.csv` (13 lines, line 1 the synthetic marker), `ops/desk/deploy-smoke.sh`, `prompts/2026-10-20/965-f5-x3-values-port-card.md`, `reports/draft-f5-x2-2026-10-20.md`.
- Read in part: `docs/30 - Design/F5-FINAL-2026-10-11.md:160-199` (rows X1–X15 at `:175-189`); `reports/cos-probe-fr1-build-2026-10-20.md` and `-check-` (headings and stop lines: BUILT `78b93da3`, CHECK DONE `da47500a` ready YES, RESTARTS `com.cobalt.radar`); `configs/cobalt/jobs.yaml` labels, `imports:` and `reads:` lines; `src/cobalt/jobs/restarts.py` rule names; `areas/cobalt.md` `## What Cobalt is` and `## Build rules` down; `topics/writing-rules.md` whole.
- On disk (gitignored): `data/deploy/bootstrap-owed.json:5-8`, the four checkpoint labels and their gate lists.
- `git grep` over `main -- src`: `cobalt.prefill.checkpoints` is imported only by `src/cobalt/cli.py:91`; no resident but `com.cobalt.radar` (`jobs.yaml:203`) imports `cobalt.cli`.
- `git grep` over `main`: no committed real Groups body. The X1 raw CSVs and draft-f5-x2's desk capture were never committed.
- The prompt's path `src/cobalt/checkpoints.py` is `src/cobalt/prefill/checkpoints.py`. Its `:747-751` and `test_checkpoints_offline.py:10-12` hold there.
- `wc -c` of the card → 20725 (a new file).

DRAFTED · decisions: 7
