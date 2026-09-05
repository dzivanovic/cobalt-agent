# `src/cobalt/jobs/` — F17 task integrity, minimal

## What it does
Every scheduled job is a persisted row with a state, a timeout and a
heartbeat; a failure is loud; a kill phrase stops all of them.
Charter §3 F17, L18.

## The registry (10 jobs, one per plist)
`configs/cobalt/jobs.yaml`. `cobalt validate` cross-checks it against
`ops/*.plist` **both ways** — a registry that has drifted from launchd
reports green for a job that is gone, and a plist with no row is a job
nobody watches.

| label | kind | supervisor | timeout | cadence |
|---|---|---|---|---|
| `com.cobalt.aset` | resident | launchd | 300 s | — |
| `com.cobalt.mainframe` | resident | launchd | 600 s | — |
| `com.cobalt.obsidian` | resident | launchd | 300 s | — |
| `com.cobalt.agent` | resident | **pidfile** | 600 s | — |
| `com.cobalt.prefill-daily` | one-shot | self | 600 s | Mon–Fri 05:15 ET |
| `com.cobalt.prefill-drc` | one-shot | self | 600 s | Mon–Fri 15:40 ET |
| `com.cobalt.archiver` | one-shot | self | 5400 s | Mon–Fri 20:30 ET |
| `com.cobalt.cards-expire` | one-shot | self | 300 s | Mon–Fri 16:05 ET |
| `com.cobalt.daymode-propose` | one-shot | self | 300 s | Mon–Fri 09:00 ET |
| `com.cobalt.heartbeat` | one-shot | self | 300 s | every 15 min |

## What `com.cobalt.agent` is
The **old tree's** agent. Its plist runs `cobalt.sh start`, which
pre-flight-checks LM Studio, Postgres and Mattermost, then
`nohup uv run src/cobalt_agent/main.py &` — the Mattermost websocket
listener, the scheduler, the Scribe, the memory layer.

It is `supervisor: pidfile` because of a real shape: `cobalt.sh` spawns
the agent **detached** and exits 0, so launchd holds no PID and
`launchctl list` prints `- 0` for this label whether the agent is alive
or dead. `logs/cobalt.pid` is the only truthful signal. It gets a row so
F18 can say it is down; it gets **no wrapper**, because the strangler
rule keeps the old tree closed.

## Who stamps the heartbeat, and why the column exists
`self` (our code, through the wrapper), `launchd` (a live PID), or
`pidfile`. A probe saying *"the process exists"* and a wrapper saying
*"I am running and past my gates"* are different claims, so
`heartbeat_source` records which one spoke.

## The two conclusions the watchdog draws
- **ZOMBIE** — `running` past `timeout_s` **and** a stale heartbeat.
  Both halves: the archiver legitimately runs 23 minutes, so "started
  and did not finish" is useless as a test.
- **MISSED** — a one-shot past its cadence with no run. **Not a state**:
  there is no row to move, it is a fact about an absent run.

## The files
| file | what it owns |
|---|---|
| `models.py` | `JobKind`, `JobState`, `Supervisor`, `RED_STATES` |
| `config.py` | the registry + `Schedule` arithmetic |
| `store.py` | `cobalt_jobs`, `cobalt_kill_switch` |
| `wrapper.py` | `job_run()` and the beater thread |
| `entrypoint.py` | `as_job()` — the one line each entry point adds |
| `watchdog.py` | the launchd probes, ZOMBIE and MISSED |
| `killswitch.py` | `cobalt stop` / `cobalt resume` |
| `cli.py` | `cobalt jobs list/register/check/run` |

## Tests
`tests/cobalt/test_jobs.py` — 45 cases, including the registry↔plist
agreement (times, weekdays, `COBALT_ENV`), both zombie halves, both
schedule shapes of MISSED, and the loaded-plist probe.
