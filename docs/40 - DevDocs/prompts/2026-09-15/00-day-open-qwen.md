MODEL: Qwen3.8-27B local (`mainframe`) via Qwen Code · SEAT: day-open, read-and-judge (L49) · SESSION: one-shot headless · approval: --yolo (ruled 09-14, until the Qwen startup script exists) · METER: local, free · COST: ~10 fixed commands, one report file, ≤3K output tokens

LAUNCH (Dejan, one line, from any Mac terminal; safe to run at once — creates the note if absent, then runs the day-open):
cd ~/cobalt && R="/Users/cobalt/Vault/Think/1 - Trading/5 - Review/Rules.md" && cp "$R" "$R.pre-0915" && sed -i '' 's/\.#process$/. #process/' "$R" && COBALT_ENV=production COBALT_VAULT_PATH=/Users/cobalt/Vault/Think uv run prefill daily && qwen --yolo "$(cat 'docs/40 - DevDocs/prompts/2026-09-15/00-day-open-qwen.md')"

# DAY-OPEN 2026-09-15 — seat qwen-27b, read-only checks, one report

INDEX CARD (all you need; read nothing else): working directory is /Users/cobalt/cobalt (production checkout; you change nothing in it except the one report file below). Laws that bind you: L49 (local seat reads and judges, never composes long prose), L1 (a missing number is FAIL, never a guess), L48 (evidence lands in the report file). Report path: docs/40 - DevDocs/reports/day-open-2026-09-15.md — write it with your file-write tool, then print the VERDICT table as your last output. Known today, not a failure of this check: the heartbeat radar probe flaps RED/OK on a stale IMCC bar-poll record (ticketed, fixed tonight) — rate it KNOWN, not FAIL. Do not run any command not listed here.

Run each command exactly as written, paste its output verbatim under its heading in the report, then judge PASS / FAIL / KNOWN / ERROR (ERROR = the command itself failed).

## S1 radar resident
launchctl print gui/$(id -u)/com.cobalt.radar | grep -E "state =|pid =|last exit"
EXPECT: state = running. 

## S2 radar pool row
COBALT_ENV=production uv run cobalt db query --side system --prod --format table "SELECT state, session, members, cap, last_scan_at, failed_stage, failed_detail FROM radar_pool WHERE pool_key = 'primary'"
EXPECT: state scanning, members ≥ 1, last_scan_at within 6 minutes of `date -u` (run `date -u` and quote it). failed_stage = bars with 'poll failures: 1' = KNOWN.

## S3 first membership rows today
COBALT_ENV=production uv run cobalt db query --side system --prod --format table --limit 5 "SELECT ticker, session, entered_at AT TIME ZONE 'America/New_York' AS entered_et, source, rank_at_entry FROM radar_membership WHERE trade_date = DATE '2026-09-15' ORDER BY entered_at"
EXPECT: at least one premarket row with entered_et after 04:00 today.

## S4 heartbeat, last beat
grep -E "^HEARTBEAT" logs/heartbeat.log | tail -1
grep -E "^(RED|AMB|OK)  +(database|sheet HTTP|radar|archiver|com.cobalt.prefill-daily|com.cobalt.prefill-drc) " logs/heartbeat.log | tail -6
EXPECT: last beat within 20 minutes; database OK; sheet HTTP OK. prefill-daily RED = FAIL unless the note now exists (S6); prefill-drc RED = KNOWN (clears at its 15:40 run); radar RED with 'poll IMCC stale' = KNOWN.

## S5 radar cycle gaps today
grep "2026-09-15" logs/radar.err | grep "radar cycle" | tail -40
EXPECT: consecutive lines ≤ 20 minutes apart (normal ≈ 3 min). Name the largest gap you see.

## S6 daily note
ls -la "/Users/cobalt/Vault/Think/1 - Trading/1- Daily Notes/2026-09-15.md"
COBALT_ENV=production uv run cobalt db query --side system --prod --format table "SELECT label, state, exit_code, finished_at FROM cobalt_jobs WHERE label IN ('com.cobalt.prefill-daily','com.cobalt.prefill-drc')"
EXPECT: the note exists; prefill-daily state done, exit_code 0 (a run from the launch line counts).

## S7 archiver
grep -E "^(RED|AMB|OK)  +archiver " logs/heartbeat.log | tail -1
EXPECT: OK, last run within 30 h.

## VERDICT
Table: check | verdict | one-line evidence. Then OVERALL: RED if any ERROR, else AMBER if any FAIL, else GREEN (KNOWN never lowers it). Then one line: "NEXT: the desk reads this report and states the plate." Write the whole report, print the table, stop.
/no_think
