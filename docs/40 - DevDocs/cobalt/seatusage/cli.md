# `src/cobalt/seatusage/cli.py`

## Commands
```
cobalt seat-usage run [--dry-run]   one run (this is what the plist runs)
cobalt seat-usage show              print today's table, write nothing
cobalt seat-usage gate              the L15 four-gate answer sheet
```

## `run`
What `com.cobalt.seat-usage` executes every `seat_usage.interval_min`
minutes inside `seat_usage.window`. Goes through the F17 wrapper, so a
failure is a red job row with the reason on it.

`--dry-run` deliberately **skips the wrapper**: a rehearsal must never
leave a row saying the report was refreshed. It computes and diffs
everything and writes nothing.

## `show`
Renders today's table to stdout with no previous snapshot, so the Δ
column is all em dashes. Touches no file and records no row — the
command for "what would be in the report right now".

## `gate`
Prints the pin, the licence, the binary, the network posture, the report
path and the exact argv — then checks the installed version against the
pin and exits 1 if they disagree. This is the command to run after any
`npm` activity on this machine, and the one to paste into a review when
the pin changes.
