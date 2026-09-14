---
name: Day-open sweep routine
description: Morning read-only heartbeat/market-reset diagnostic checklist; report goes to docs/40 - DevDocs/reports/day-open-<date>.md
type: project
---

Cobalt runs a "day-open" sweep each morning (~07:00 ET, local Qwen seat): a fixed checklist of VERBATIM commands — heartbeat row in `system.cobalt_jobs`, `system.session_blocks` refusal count (baseline 8 as of 2026-09-11, all from the 09-08/09-09 incidents), heartbeat.log/.err greps around the 20:00–21:00 ET market-reset window, `launchctl print`, archiver log, tree-state git checks — then a report to `docs/40 - DevDocs/reports/day-open-<date>.md` (the only file written that day).

**Why:** market_reset is a hard no-vault-write block 20:00–21:00 ET; on 09-08/09 the heartbeat died every in-window beat (SessionBlocked refusals, ~75-min holes). Fix 16847eb (09-10) makes beats ask the session and log `deferred_market_reset` instead. The sweep verifies it holds; anomalies become ESCALATE lines, not fixes — the sweep is strictly read-only (no commits, deploys, restarts, vault writes).

**How to apply:** when the user opens a day-open session, run each command verbatim; adapt only with disclosure (e.g. `\d <table>`, `ls logs/`); never write a figure not seen in output; `system.cobalt_jobs` holds one row per label (latest beat only) — never read overnight behaviour off it; `archiver.log` is empty by design, real archiver output is in `archiver.err`.
