# F4 card 304 amend, 2026-10-10

## §0 Headline
Card `304-f4-refresh-card.md` is amended for preflight FAIL 20 and NOTE 1-7; header and every other row untouched.
`drc.py` does reach residents (`com.cobalt.aset`, `com.cobalt.radar`), so `prefill/daily.py` and `market.py` derive both restarts; `prefill/cli.py` reaches none.
Every changed anchor is read at HEAD, `src configs ops tests` equal HEAD.

## DECISIONS
- D1 FAIL 20: RESTARTS now names a class for `jobs.yaml`, `daily.md.j2`, `smoke/s2.yaml`, `daily.py`, `cli.py`, `market.py`. The `drc.py:78` edge is real: `aset/web.py:2114` → `drc/imports.py:640,:808` → `drc/build.py:72,:178` → `prefill/drc.py:78` → `daily.py`; radar via `cobalt/cli.py:68` → `drc/cli.py:146,:194,:261-262`. `import_graph` counts function-local imports (`restarts.py:120`, `:133`). R1's table stays the truth.
- D2 NOTE 7: the baseline reaches `body_fn` through its closure, which calls `writer._baseline(path, section, unit_id)` (`writer.py:836-839`) on every call; the signature stays `body_fn(snapshot)`.
- D3 NOTE 6: E1's hand-typed-table leg is `xfail(strict=True)` with a reason text; D4 and FINAL X16 unchanged.
- D4 NOTE 1: the LADDER grep, re-run, hits `cobalt-sprints.md:17`, `:20`, `:42` (the card said `:17`, `:42`); none is an S5 lane A line, so the fallback still holds.
- NOTE 2-5 folded as ruled: `basis` on `DemandConsumer`; `read_plan()` / `DemandPlan` named with the import edge left to R1; X12 leg re-worded to the commit-window race, with the retry leg kept as X4's; function-local test imports stated in WHY.

## RECORDS
- `git -C /Users/cobalt/cobalt show HEAD:src/cobalt/jobs/restarts.py`, `show HEAD:configs/cobalt/jobs.yaml` · 2026-10-10 19:05 EDT (`date` 19:05:28).
- `git -C /Users/cobalt/cobalt diff HEAD --stat -- src configs ops tests` · empty · 19:06:59 EDT; also empty at 19:05. Reads of the other files below equal HEAD.
- Read/Grep, `restarts.py:196-258` (`:211-214`, `:215-222`, `:223-224`, `:251-256`), `import_graph` `:120`, `:133` · 19:05-19:07 EDT.
- Grep `src/**/*.py` for importers of `cobalt.drc`, `prefill.cli`, `prefill.daily`, `from . import`: no module imports `prefill.cli`; `pyproject.toml:68` is its entry · 19:05 EDT.
- Grep `jobs.yaml`: `:203` radar `imports: [cobalt.cli]`, `:330-335` `daily.md.j2` no_resident_reads · 19:05 EDT.
- Read `radar/notes.py:201-216` (`basis` `:215`), `strike/detector.py:78-89`, `:313-319`, `writer.py:545-586`, `:673-919` · 19:06 EDT (`date` 19:06:00, 19:06:13).
- Grep `F4-FINAL-2026-10-10.md` for X12/X16, `test_finviz_consumers.py:69-73` · 19:06 EDT.
- Grep + `grep -n -o` over `areas/cobalt-sprints.md`; Glob of the two precedent cards · 19:07 EDT (`date` 19:07:10).
- Card edits: RESTARTS, WHY (test imports), W1, G1, E1, RECORDS; no other row.

F4 CARD AMENDED · decisions: 4
