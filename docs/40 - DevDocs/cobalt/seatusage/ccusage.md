# `src/cobalt/seatusage/ccusage.py`

## What it does
Runs one pinned external binary over the harness logs already on this
disk, and turns its JSON into `DayUsage` / `ModelUsage`. No shell
string, fixed argv, no network, nothing written.

## The four gates (L15), where they are checked
| Gate | How |
|---|---|
| Proven | ~59k npm downloads in the week to 2026-09-06; pinned exactly. |
| Conformant | Read-only over harness logs; opens no Cobalt database, writes no note. `subprocess.run` with a list argv. |
| Industry-standard | MIT, zero declared runtime dependencies, one bin entry. |
| Reviewed-clean | Installed into `~/.npm-global`, outside the repo and the system prefix, so it can be inspected and removed whole. |

`cobalt seat-usage gate` prints the answer sheet and re-checks the
installed version against the pin.

## THE SILENT-ZERO GUARD — the thing to understand here
`--offline` is the no-network gate, and on 2026-09-08 the bundled
pricing table it falls back to had **no rate for `claude-fable-5-1` or
`gpt-6-astra`** and priced both at exactly `$0.00`. The online table
priced the same day's fable tokens at **$17.32**.

A model that was used all day showing `$0` is a plausible-empty
artifact, which is the one thing the fail-loud law forbids outright. So:

* a model with tokens, no configured free status, and a cost of `None`
  **or** exactly `0.0` comes back as `cost=None` — **unpriced**, never
  zero — and its name lands in `DayUsage.unpriced`;
* a model named in the config's `zero_cost_models` keeps its honest
  `$0.00` and raises nothing;
* `priced_total` is therefore a **floor** whenever `unpriced` is
  non-empty, and every caller that prints it says so.

The fix for an unpriced model is a deliberate version bump with a diff.
It is never "let the job reach the network".

## Split for testability, not for tidiness
`fetch_raw` runs the binary; `parse` is pure. The tests drive `parse`
from a recorded fixture, so the guard above is proven against the exact
JSON shape the real tool produced, with no subprocess in the test.

## A day with no activity
Not an error and not an empty artifact: `parse` returns a `DayUsage`
with no models, and the renderer writes a table that says so in words.
