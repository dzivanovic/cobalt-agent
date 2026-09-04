# `src/cobalt/obsidian.py`

## What it does
Answers one question: **is Obsidian running on this Mac?** RULING 6.3c/3d.

The vault reaches Dejan's other devices only through Obsidian Sync,
which means only through a running Obsidian process here. On 2026-09-04
`prefill-daily` created `2026-09-04.md` correctly at 05:15 — 118 lines,
`vault_writes` rows 525-528, exit 0, green run report — but no Obsidian
had run on the Mac since the previous evening's reboot. Nothing synced.
At 06:30 the trading PC's daily-notes plugin created its own bare
template for the same date and Sync carried that back over the top.
Every byte Cobalt wrote was correct, audited, and invisible.

A vault write nobody is watching is not a success.

## Key functions/classes
- `ObsidianProbeError(RuntimeError)` — the probe itself could not run.
- `PROCESS_NAME = "Obsidian"`.
- `NOT_SYNCING_ERROR` — the exact wording RULING 6.3d specifies:
  `"written; Obsidian not running — will not sync"`.
- `obsidian_pids() -> list[int]` — `pgrep -x Obsidian`.
- `is_running() -> bool`.
- `sync_status() -> tuple[bool, str]` — the one call the writer and the
  future heartbeat both make, so they cannot disagree about wording.

## Data flow in/out
**In:** `pgrep -x Obsidian` (`-x` matches the main app process only,
never the `Obsidian Helper (Renderer)` children, so the count is the
count of running instances).
**Out:** PIDs, a boolean, or raises.

## Config it reads
None.

## Safety properties
- **"The probe is broken" and "Obsidian is down" are different facts.**
  A missing `pgrep`, or any exit code other than 0 or 1, raises rather
  than returning `[]`. Collapsing the two is how a red condition
  becomes invisible — the exact failure class this module exists for.
  Exit 1 is pgrep's documented "no match" and is the one non-zero code
  treated as an answer.

## Who calls it
- `cobalt/vaultwrite/writer.py` — `VaultWriter._annotate_sync()`
  attaches `NOT_SYNCING_ERROR` to any `WriteResult` whose action
  produced bytes (`created`/`updated`/`restored`) while no Obsidian was
  running. Printed as `ERROR:`, never `NOTE:`, and logged at ERROR.
  Hung on the four public entry points via the `@_reports_sync_status`
  decorator rather than the ten `return WriteResult(...)` sites.
- **The heartbeat — NOT YET.** RULING 6.3c asks for an
  "Obsidian process running" probe on the heartbeat. The probe is built
  and tested; there is no heartbeat on this machine to add it to. It is
  an unchecked BACKLOG item ("Heartbeat probe: every ops/ plist expected
  loaded is loaded", STANDING FOLLOW-UPS), sequenced after slice 2 in
  PROJECT-LEDGER. When it lands it calls `sync_status()`.

## Tests
`tests/cobalt/test_obsidian.py` — 16 cases. Probe: running/absent, the
exact ruling wording, exit 1 = not running, exit 3 = raise, missing
pgrep = raise, plus one unmocked call so an interface change cannot pass
silently. Writer: the ERROR line appears for every byte-producing
action, does NOT appear for `unchanged`/`skipped`/`skipped_exists` (a
red line there would train the wrong reflex), a broken probe reports
UNKNOWN rather than "will not sync", and all four public methods still
carry the decorator.

## Proven in the field (2026-09-04)
With `com.cobalt.obsidian` booted out and Obsidian killed, a dev-vault
`prefill daily --dry-run` emitted both the loguru ERROR line and the
run-report `ERROR: written; Obsidian not running — will not sync`. The
same command with Obsidian running emitted neither.

## Gotchas
- The service (`ops/com.cobalt.obsidian.plist`) is `KeepAlive`, so
  Obsidian relaunches within ~1 s of being killed. To reproduce the
  "not running" condition you must `launchctl bootout` the job first,
  then kill the process.
