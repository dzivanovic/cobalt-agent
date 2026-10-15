# `src/cobalt/classify/ledger.py`

## What it does
The spend ledger that enforces his cap in code (plan §5; cap $5,
`cto-2026-09-23.md` R42). One JSON line per metered call in
`scratch/classify-spend.jsonl`: `call_id`, `cost_usd`, `cost_source`,
`at` (UTC). Never a request, a response or a header. Three sources
(JEV fix r1 F4): `returned` (the response's `usage.cost`), `computed`
(tokens × the listed price), `projected` (a call that came back with no
cost — a non-200, a 200 without `usage`, a 401 / 403 — booked at its own
projection so the cap and the call ceiling see it; never 0, never a
guessed bill). Every POST that came back is exactly one ledger line; a
transport exception (nothing came back) writes none.

- `spent()`, `calls()`, `entries()` — reads; they never create the file.
- `check(projected_usd, calls=n)` — BEFORE any call: refuses when
  `spent() + projected > cap` or `calls() + n > call_ceiling`.
- `stop_if(total=None)` — the running check: total ≥ cap stops the run.
- `check_cost(returned=, projected=)` — a returned cost above 10× its
  projection stops the run (the pricing assumption is wrong); a free
  projection that turns out not to be free trips it too.
- `record(call_id, cost_usd, cost_source)` — the ONLY write, and the only
  thing that creates the file. It refuses a negative or non-finite cost
  with a loud `ClassifyError` BEFORE the file is opened (JEV fix r1 F5:
  a negative line would lower the total). The refusal stays as the last
  line of defence. The collector no longer hands it a refused cost for a
  call that came back (JEV fix r2 F7 / F8): a negative token count is no
  usage, a negative or non-finite listed price refuses the call before
  it is made, and a non-finite computed cost is booked at the call's
  projection.
- One instance lock covers every read and the append, so the trial's
  `parallel` mode never reads a half-written line.

## Laws it carries
- **L53 total demand**: the projection is added to EVERYTHING already
  spent across every earlier run; two runs each under the cap cannot
  together exceed it (tested). The call ceiling is counted the same way.
- **L1**: every refusal is a loud `ClassifyError` naming the numbers.
- "The file exists" ⇔ "a metered call was made": the offline build's
  CLOSE step fails if `scratch/classify-spend.jsonl` exists.

## What it never does
Holds a key, touches the network, a database or the vault.

## 2026-10-15 — jev-shadow-1015
`Ledger(..., carried=())`: carried paid lines counted by `spent()` and `calls()` before the file's lines, never written (F2). The file is now the host-wide `spend_ledger` of trial.yaml / route.yaml, not `scratch/`.
