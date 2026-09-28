# `tests/fixtures/replay/_cut_p4_fixtures.py`

Deterministic, re-runnable cutter for the S2-P4 replay/picks fixtures (L45). It reads only raw production-read output staged under `scratch/` and two named harness tool-result paths; it never opens the database, never calls Finviz, and never invents a row. Dates in the anchor month are shifted to a synthetic anchor and 12-hex source suffixes are zeroed by `_anonymize`, so no fixture carries a real anchor-month date string.

Four modes, chosen by the first CLI argument.

## No argument — the full cut

`main()` writes all six fixtures: the day's cards, bars and membership, the radar pool-metrics export, and both movers exports. Some of its raw inputs no longer exist, so this mode is kept working rather than exercised; re-cutting one fixture is what the `movers` mode is for.

## `evidence` — read-only (AT-0)

Cuts nothing. It reads every cached Finviz export it can find plus the two staged movers exports and writes one scratch report comparing the `Asset Type` column against `Industry = Exchange Traded Fund`. It exists because Finviz fills `Asset Type` only for funds and leaves it blank for an ordinary stock, so the radar config's `not_equity.values: [Exchange Traded Fund]` matches nothing; the report is the evidence for rebuilding that rule, and it is a decision aid, never a rule. A file whose header lacks either column is counted and named, never skipped — that absence is itself evidence — but a file with no header at all is not a screener export and raises `EvidenceError` naming it (L1). Tickers live in the scratch report only (L32); stdout carries counts.

## `movers` — re-cut the two movers fixtures (AT-1 2.5)

The first movers cut came from a 21-column default view, not the shape the collector receives, which is the L45 defect this mode fixes. It re-cuts only `movers-{gainers,losers}.real-shape.csv` from the re-fetched raw exports (151 columns, the radar's own `v` and `c`), and touches nothing else.

Rules it enforces rather than assumes:

- The header row is the raw file's own, never rebuilt and never trimmed, and `_anonymize` must leave it byte for byte — asserted, because a header the cutter edited is not the shape the collector receives. Line-ending normalisation (`read_text`) is the one transformation, and it is the same one every other fixture here gets, which is why the movers header matches the radar export fixture's exactly.
- Cutting by line is verified, not assumed: if the CSV parses to a different number of records than there are lines, a field spans lines and the cut would split a row, so it fails loud.
- At least one real row with a non-blank `Asset Type` is guaranteed to be in the cut. Finviz fills that column only for funds, so a 60-row cut with none would leave every "reads `Asset Type` when present" claim asserted against blanks alone. If the top rows hold none, the first such row further down the file is appended out of rank order and stdout says so; if the raw file holds none at all, the cut is what exists and stdout says that instead. A row is never invented.

The fixture is never hand-edited. A divergence is fixed here and the mode re-run; the output is byte-identical across runs, which is how the re-cut is verified.

## `movers-blank <raw-export-path>` — the blank-`Change` tail (S2 smoke fix F1-FX)

The 2026-09-22 replay failed on `movers: Change '' is not a percentage`: the gainers export listed 14 never-traded listings at its very end with an EMPTY `Change` cell. The committed movers fixtures are the export's top 60 rows, so that tail was cut away and no test could see the shape that failed. This mode reads ONE raw export named on the command line (read only; run once on the retained `data/radar-cache/2026-09-22/movers-gainers-211004.csv`) and writes one new fixture, `movers-gainers-blank-change.real-shape.csv`: the raw header byte for byte (the same `_anonymize` assertion as `movers`), the first `BLANK_TOP_ROWS = 25` data rows, and every data row whose `Change` cell is empty after strip — exactly the cell `parse_movers` leaves unranked — in export order, each through `_anonymize`. The same one-record-per-line guard as `movers` runs before any line is kept. A raw file with no blank-`Change` row fails the mode loud (`NO row with a blank Change exists in the raw export`) instead of writing a fixture that proves nothing. Stdout names counts and export positions only, never a ticker (L32). The existing modes and fixtures are untouched.
