# `src/cobalt/heartbeat/` — F18 heartbeat host

## What it does
Every `heartbeat.interval_min` minutes (15): probe every service, sweep
every job row, write one red/green block into today's daily note as an
L28 unit, and alert when something enters RED or recovers — plus
standing-state summaries at 07:00 and 16:30 ET (ruled 2026-09-14).

Charter §3 F18 (M10). Job: `com.cobalt.heartbeat`,
`COBALT_ENV=production`, `StartInterval 900`, `RunAtLoad` (a reboot is
precisely when something is most likely to be down — 09-04's 15.7.9
reboot left Obsidian dead and a day's writes unsynced).

## The probes
| probe | red when |
|---|---|
| `database` | `cobalt_brain` will not answer `SELECT 1` |
| `sheet HTTP` | `:5010/` is not **200** |
| `obsidian` | no Obsidian process (RULING 6 — no Obsidian, no Sync) |
| `mainframe` | `:1234` refuses a connection |
| `archiver` | MISSED against its own Mon-Fri cadence (`cobalt.jobs.watchdog.is_missed`), failed, or **ran and wrote zero rows** |
| `vault blocks` | never red — reports refusals **and** ungated repair runs, separately |
| `redactions` | never red — reports F19 hits since the last beat |

Two of those deserve their reasons:
- **the sheet probe asks for 200, not for a PID.** Reshaping
  `aset.yaml` in S1-P2 took the running sheet to HTTP 500 while the
  process stayed alive and launchd stayed happy. The thing he trades
  beside is the *page*.
- **archiver freshness reads rows written.** An archiver that exits 0
  having written nothing looks green in every state column while quietly
  not collecting the corpus every later feature depends on.

## Every probe keeps one rule
"The probe broke" and "the thing is down" are different facts. A probe
that cannot run returns **UNKNOWN**, and UNKNOWN is red — a heartbeat
that says green when it did not look is worse than no heartbeat.

## The three outputs
1. **The daily note.** One Cobalt-owned unit (`section heartbeat` /
   `unit status`) through `VaultWriter` — stable id, updated in place,
   one unified diff per beat. Not 96 blocks a day.
2. **A Mattermost DM** on a RED transition (entered or recovered —
   unchanged is silent), plus a standing-state summary at each
   `heartbeat.summary_at` slot, sent even when nothing is red. The prior
   state and "have we sent this slot today?" are both answered from the
   job row's own `last_result` — the heartbeat is its only writer, and a
   second table would be a table to migrate later for nothing.
   Known-idle states never rate RED: radar outside a scanning session,
   and a `launchd_unmanaged` job (AMBER, see `jobs/watchdog.md`).
3. **The out-of-band channel — RETIRED 2026-09-14.** See below.

## Output 3: built, then retired
Charter §3 F18 specifies *"email via Layer-B Google OAuth"*. S1-P3
(2026-09-04) found no send path and stopped at Mattermost; S1-P4
(2026-09-08) built it. Google's Publish step for the `gmail.send` scope
is gated on restricted-scope verification, so the OAuth client never
left Testing and its refresh token expired every seven days. Dejan ruled
the channel retired on 09-14; it was removed 09-15 (git history keeps the code:
`git show 0ed37f5:src/cobalt/notify/email.py`). **The consequence is
the hole Charter §3 F18's "alert path ≠ monitored path" exists to
close:** the DM goes over Mattermost, which is one of the monitored
services, so a Mattermost outage takes the alert about it along.

## A red beat exits 0
A red heartbeat is the heartbeat *working*. A job row that flipped to
`failed` every time something else was down would make the heartbeat's
own history useless. It exits non-zero only when the beat itself could
not run — and it records its own run like any other job, so a stalled
heartbeat surfaces as its own MISSED row.

## The files
`probes.py` (one function per question) · `render.py` (one renderer, two
destinations — a heartbeat whose channels could disagree is one you have
to check twice) · `runner.py` (the beat) · `cli.py`
(`cobalt heartbeat beat/show`).
