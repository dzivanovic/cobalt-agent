# `src/cobalt/jobs/cli.py`

Registers `cobalt jobs restarts <git-range>` and delegates derivation to `jobs.restarts`.

```
cobalt jobs list                     the table, as F18 reads it
cobalt jobs register                 upsert every row from jobs.yaml
cobalt jobs check                    run the watchdog, print findings
cobalt jobs run LABEL -- CMD ARGS    wrap any command as that job
cobalt stop [--phrase ...] [--by ...]
cobalt resume [--by ...]
```

`jobs check` exits 1 on any red, so it composes into a shell script.

`jobs run` is the plist-facing half of the wrapper: a launchd job whose
program is not our Python gets its row, its heartbeat and its exit code
by being launched through it.

`stop` / `resume` are **top-level**, not under `jobs`, deliberately: the
kill phrase is what you reach for when something is wrong, and
`cobalt jobs killswitch engage` is not what anyone types at that moment.
