# `src/cobalt/seatusage/runner.py`

## What it does
One seat-usage run, and the F17 wrapper around it.

## The order, and why it is this order
1. **Gate the tool** (`assert_pinned`) and run it. A mis-pinned or
   missing binary crashes here, before anything is written — "ccusage is
   not installed" and "nobody used a seat today" must never render the
   same way.
2. **Read the previous snapshot** from this job's own row, so the Δ
   column compares like with like and only within one day.
3. **`create_if_absent`**, then **`upsert_unit`** for today's table —
   same unit id, so the same hour's table is replaced rather than
   appended.
4. **Seed the human cells**, only if the file does not already have
   them.

Step 4 is last because the region locator needs the day's section to
exist, and step 3 is what creates it.

## Why a repo file goes through the vault writer
The report lives at `docs/40 - DevDocs/reports/seat-usage.md`, which is
repo content by R3 — versioned, reviewed in a diff, no human note in the
folder. It goes through `VaultWriter` anyway, and not for the vault
guards, which do not apply to a file in git. It goes through it for the
**merge**: the writer is the only code here that can rewrite the
generated half hourly while leaving a filled human cell exactly as its
author left it, record the override, and hand back the diff. Writing it
with `open(..., "w")` would mean regenerating over Dejan's own numbers
once an hour.

`cobalt.vault.REPO_OWNED_ROOTS` is the declared carve-out that lets the
writer accept the path. It is a fixed tuple in code, not an argument, so
a caller cannot widen it.

## `--dry-run` never goes through the wrapper
A rehearsal writes nothing, and a job row saying a run completed when it
deliberately did nothing would make the F18 freshness probe green on the
strength of a rehearsal. `cli.cmd_run` calls `run(dry_run=True)`
directly and `run_as_job()` only for a real run.

## Failure behaviour
Everything raises. The wrapper marks the row `failed` with the exit code
and the redacted reason, F18 turns red on it, and the report keeps the
last good table rather than gaining a half-written one.

## The ET day
`today_et()` — the report is written for an **ET calendar day**, because
every other cadence in this system is ET and a UTC boundary would roll
the row at 20:00 local.
