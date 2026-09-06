# `src/cobalt/heartbeat/` — F18 heartbeat host

## What it does
Every `heartbeat.interval_min` minutes (15): probe every service, sweep
every job row, write one red/green block into today's daily note as an
L28 unit, and DM on any red — plus one green summary a day.

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
2. **A Mattermost DM** on any red, plus one green summary at
   `heartbeat.green_summary_at` (17:30 ET). "Have we sent today's?" is
   answered from the job row's own `last_result` — the heartbeat is its
   only writer, and a second table to remember one boolean a day is a
   table to migrate later for nothing.
3. **The out-of-band channel — WHICH DOES NOT EXIST.** See below.

## Output 3: what exists, and what does not
Charter §3 F18 specifies *"email via Layer-B Google OAuth"*. **There is
no email send path in this repo.** Searched at S1-P3 (2026-09-04): no
`smtplib`, no `sendmail`, no Gmail/OAuth client, no credentials file, no
`send_email` anywhere in `src/`, `ops/`, `dev_utils/` or `configs/`.
`google-api-python-client` is in pyproject's dependencies and
`googleapiclient` appears in the old tree only as a Gemini/LLM import,
never as a mail sender; the vault's cloud entries are GEMINI / OPENAI /
OPENROUTER **API keys**, which are not an OAuth credential and cannot
send mail.

S1-P3's instruction was explicit: do not build OAuth, report what exists,
stop at Mattermost. So `out_of_band()` says so on every red, naming what
was searched for. **The consequence is the hole Charter §3 F18's "alert
path ≠ monitored path" exists to close:** the DM goes over Mattermost,
which is one of the monitored services, so a Mattermost outage takes the
alert about it along. Carried to P4.

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
