# `src/cobalt/heartbeat/cli.py`

```
cobalt heartbeat beat [--dry-run]     one beat (launchd runs this)
cobalt heartbeat show                 probe and print; write/send nothing
```

`beat` is what `com.cobalt.heartbeat` runs every
`heartbeat.interval_min` minutes. It installs F19's log guard first —
the heartbeat's output includes probe details and error text, and
`logs/heartbeat.log` is read over Tailscale.

It **exits 0 on a red**; see `runner.md`.

`show` is the read-only form for a human at a terminal: every probe, no
write, no DM.
