MODEL: Qwen3.8-27B local (`mainframe`) via Qwen Code · SEAT: day-open, read-and-judge (L49) · HOW (Qwen under watch, ruled 09-15; `--yolo` retired 09-16 — the `~/.qwen/settings.json` allowlist covers every command below): in the Qwen1 pane, start plain `qwen`, then type ONE line: `Read docs/40 - DevDocs/prompts/DAY-OPEN-QWEN.md and follow it exactly. /no_think` · METER: local, free · COST: ≤10 fixed commands, one report file. This file is dateless and stable; the date comes from `date +%F`.

# DAY-OPEN — seat qwen-27b, read-only checks, one report, every trading morning

INDEX CARD (read nothing else): working directory `/Users/cobalt/cobalt` (production; you change nothing except the report). Laws: L49 (read and judge, never compose long prose), L1 (a missing number is FAIL, never a guess), L48 (evidence in the report file). First run `date +%F` and use that date everywhere below as DATE. Report path: `docs/40 - DevDocs/reports/day-open-DATE.md` — write it with your file-write tool, print the VERDICT table last, stop.

## S0 — is the day-open command available? (after 2026-09-15 it is)
`COBALT_ENV=production uv run cobalt day-open --help`
If exit 0: run `COBALT_ENV=production uv run cobalt day-open` (it writes the report itself), read the OVERALL line, then run `COBALT_ENV=production uv run cobalt day-open verdict "SEAT VERDICT: <GREEN|AMBER|RED> — <one line, the single most important fact>"`, print the table, STOP — skip S1–S7.
If it fails: continue with S1–S7 below.

## S1 radar resident
`launchctl print gui/$(id -u)/com.cobalt.radar | grep -E "state =|pid =|last exit"` — EXPECT state = running.
## S2 radar pool row
`COBALT_ENV=production uv run cobalt db query --side system --prod --format table "SELECT state, session, members, cap, last_scan_at, failed_stage, failed_detail FROM radar_pool WHERE pool_key = 'primary'"` and `date -u` — EXPECT scanning, members ≥ 1, last_scan_at within 6 min of `date -u`.
## S3 first membership rows today
`COBALT_ENV=production uv run cobalt db query --side system --prod --format table --limit 5 "SELECT ticker, session, entered_at AT TIME ZONE 'America/New_York' AS entered_et, source, rank_at_entry FROM radar_membership WHERE trade_date = current_date ORDER BY entered_at"` — EXPECT ≥1 premarket row after 04:00.
## S4 heartbeat, last beat
`grep -E "^HEARTBEAT" logs/heartbeat.log | tail -1` and `grep -E "^(RED|AMB|OK)  +(database|sheet HTTP|radar|archiver|com.cobalt.prefill-daily|com.cobalt.prefill-drc) " logs/heartbeat.log | tail -6` — EXPECT last beat ≤ 20 min; database OK; sheet HTTP OK; any RED = FAIL unless the note in NOW lists it as KNOWN.
## S5 radar cycle gaps today
`grep "$(date +%F)" logs/radar.err | grep "radar cycle" | tail -40` — EXPECT gaps ≤ 20 min; name the largest.
## S6 daily note
`ls -la "/Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/$(date +%F).md"` and `COBALT_ENV=production uv run cobalt db query --side system --prod --format table "SELECT label, state, exit_code, finished_at FROM cobalt_jobs WHERE label IN ('com.cobalt.prefill-daily','com.cobalt.prefill-drc')"` — EXPECT the note exists; prefill-daily done, exit 0.
## S7 archiver
`grep -E "^(RED|AMB|OK)  +archiver " logs/heartbeat.log | tail -1` — EXPECT OK, last run within 30 h.

## VERDICT
Table: check | verdict PASS/FAIL/KNOWN/ERROR | one-line evidence. OVERALL: RED if any ERROR, else AMBER if any FAIL, else GREEN (KNOWN never lowers). Last line: `NEXT: the desk reads this report and states the plate.` Write the report, print the table, stop.
/no_think
