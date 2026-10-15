JOB: gate-tests-ops-fr1
LADDER: OFF-LADDER — brain L79 2026-10-13 15:00 ET
BRANCH: deploy/gate-tests-ops-fr1
WORKTREE: deploy-gate-tests-ops-1015
BASE: main
TIP: b6370b5f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gate-tests-ops-fr1.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-15-gate-tests-ops
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gate-tests-ops-fr1` | `ec3fabc1` | `b6370b5f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gate-tests-ops-check-fr1-2026-10-15.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "## OFFLINE OPS" /Users/cobalt/cobalt/ops/desk/gate-lists.md` · before `0` · after `1` (T1 adds the one section)
- `grep -c -F "tests/ops: run" /Users/cobalt/cobalt/ops/desk/gate.sh` · before `0` · after the number of `say` lines T2 writes that print `tests/ops: run (` (at least `1`; the builder writes the count from `git show TIP:ops/desk/gate.sh`)
- `grep -c -F -e "--deploy-gate" /Users/cobalt/cobalt/ops/desk/gate.sh` · before `0` · after the number of lines T2's edit puts it on: the usage comment `:2`, the usage `refuse` `:72`, `deploy_gate=""`, the option case, the refusal line and the `do_offline` test (at least `5`; the builder writes the count from the tip)
- `grep -c -F -e "--deploy-gate" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1` or more: `:101` (the call and its clause may share the one line, so the count is the number of lines holding it; the builder writes it from the tip, and the check X2 asserts `BUILD-HUB.md` holds none)

## SMOKE READS
MARKERS (each proved before against `git show HEAD:<file>` at `e303afba`, none holds the string; the after counts are the rule that produces them, filled by the builder at BUILT from the tip's tree and by the deploy at its merge):
SMOKE READS (deploy):
- the deploy gate's own output line, `tests/ops: run (deploy-gate)`: `grep -n -F "tests/ops: run" <the gate log>` after the merge → one line whose reason names the deploy gate (the exact reason the builder's `do_offline` prints for `--deploy-gate`, as BUILT records it), the `OFFLINE OPS` command in the log's command echo, and `offline <p>/0` with `<p>` above `0`
EXTRA READ (521 self-proof): after the merge, sh /Users/cobalt/cobalt/ops/desk/gate.sh <GATE worktree> offline --deploy-gate, once; its verdict prints a tests/ops line run (deploy gate) and is green; a red is a 521 fix round, the merge already done is not rolled back for it unless suites on main go red.
BEFORE THE MERGE (brain 0e848919 10-15): `uv run pytest -q tests/ops` once on the merged tree, by hand, as at 573.

## RECORDS
- gate-tests-ops-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gate-tests-ops-check-fr1-2026-10-15.md` last line: CHECK DONE · job: gate-tests-ops-fr1 · pass: 1 · tip: ec3fabc1 · house A: Grok FINDINGS: 0 · findings: 0 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4328/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 8 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 212760
- gate-tests-ops-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gate-tests-ops-fr1` → `b6370b5f`; code tip `ec3fabc1`
- written by deploy-card.sh at 2026-10-15 08:13 ET (`date`); trial merge of the heads onto main in order: clean
