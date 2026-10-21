# Card 958 (f5-x3-values) — preflight, 2026-10-20

Read-only. Card `prompts/2026-10-20/958-f5-x3-values-card.md` against `git show 20dd871d:` (BASE) and `main`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | header keys vs `CARD.md` (read whole): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, BAND, RESTARTS, RULINGS | all present; JOB `f5-x3-values`; LADDER `OFF-LADDER — reports/cto-2026-10-20.md R2217`; TIP empty; HOUSE B `as needed`; BAND `LOW`; RULINGS `2026-10-18 R1863`; REPORT inside `/Users/cobalt/cobalt-wt/f5-x3-values/`; CHECK REPORT under main `reports/`. `CLASS`, `INSTALL`, `RESTARTS` are extra keys, same as the 945 card | OK |
| 2 | `git -C /Users/cobalt/cobalt show --stat --oneline 20dd871d` | `20dd871d docs(f5-x3-measure): build report — de976722`, 2 files (report + `.result`): BASE exists | OK |
| 3 | `grep -c "«FILL" <card>` | `0` | OK |
| 4 | `git -C … diff HEAD --stat -- <card>` · `git log --oneline -2 -- <card>` | empty diff · `3a728b47`, `f6c398ef` (committed) | OK |
| 5 | `git grep -n … 20dd871d -- configs/cobalt/modelaccess.yaml` | `:70 checkpoint.narrative:` · `:77` and `:79` `# source: UNMEASURED, provisional…` · `:78 timeout_s: 60` · `:80 max_output_tokens: 512`; no `(warm model)`, no `source: X3`. All match the card | OK |
| 6 | `git diff 20dd871d main --stat -- configs tests src ops` | empty: BASE code = main's (DECISIONS 5) | OK |
| 7 | arithmetic: 2 × 3.53 = 7.06; 8.67 + 4.97 = 13.64; × 1.5 = 20.46; max = 20.46 → up to a multiple of 5 = 25; 2 × 59 = 118 → floor 256 | `timeout_s 25`, `max_output_tokens 256`. X3 report V1 (`:110-111`): p95 3.53, max 4.97, max tokens 59 — agrees | OK |
| 8 | `grep -n -F "Model loaded successfully" ops/logs/mainframe.log` | `12:Model loaded successfully in 8.67s.` · `31:Model loaded successfully in 5.47s.` (the log has no date on these lines, so "both 2026-09-09" is unverified; line 12 loads `qwen3.8-27b`) | OK |
| 9 | `ops/logs/mainframe.log:58006-58014` | 07:14:00 OK → 07:17:00 `heartbeat FAILED: no response` → `Error: A model with identifier mainframe already exists.` → 07:18:30 OK: matches DECISIONS 2 | OK |
| 10 | `grep -n -F -e "lms unload" -e "lms load" ops/start_mainframe.sh` | `:242 lms unload --all`, `:295 lms load … --identifier` (no `--ttl`); the card's claims hold | OK |
| 11 | `F5-FINAL-2026-10-11.md` at BASE | `:88` (`source:` comment, never 15 s) · `:138` (contention, X3 timeout) · `:177` (X3 row) · `:235` (RESTARTS aset): all match | OK |
| 12 | `tests/cobalt/test_checkpoints_offline.py:553-558` | `test_route_is_loaded_and_local` with `load_routes().routes["checkpoint.narrative"]` and the `!= 15` assert: matches; `load_routes` is imported inside the test | OK |
| 13 | `src/cobalt/jobs/config.py:453,463` · `src/cobalt/modelaccess/config.py:31,150` | `def spec` `:453` · `def load_job_registry` `:463` · `CONFIG_PATH` `:31` · `def load_routes` `:150` | OK |
| 14 | `configs/cobalt/jobs.yaml` at BASE | `:86` aset `reads` has `modelaccess.yaml`; `:102-112` `com.cobalt.mainframe`; four checkpoint rows `timeout_s: 300` (`:261,268,275,282`), comment above `-0715` (`:253-256`) names the two 30 s fetches. 300 > 25 + 60 holds | OK |
| 15 | `test_modelaccess_config.py:69-80` · `test_checkpoints_registry.py:17-27` | match; neither pins the narrative route's values or the 300 against the 60 s (the registry test holds `[300] * 4`) | OK |
| 16 | `docs/40 - DevDocs/cobalt/prefill/checkpoints.md:19` | the `UNMEASURED and provisional` sentence is there | OK |
| 17 | every command the builder needs vs `BUILD-HUB.md:14,16` | `Read`, `Edit` in the worktree, `grep -n -F` of `mainframe.log` (`Bash(grep *)`, `/Users/cobalt/cobalt` is an add-dir), `uv run pytest *`, `uv run cobalt jobs restarts *`, `git add/commit/diff/log/show`, `gate.sh`. The card names no `lms`, `launchctl` or `curl` for the builder | OK |
| 18 | DEPLOY PROOF shapes vs `ops/desk/deploy-smoke.sh` (`shape`, `value_is`, `deploy-card.sh:573-574`) | marker rows 1 and 2 (`before `2` · after `0``, `before `0` · after `2``) are mapped and read GREEN. Marker rows 3 and 4 end `after `1` (T2's line only)` / `after `1` (T1's line)`: `aft` becomes `` `1` (T2's line only)``; `value_is` needs a value that starts and ends with a backtick, so it returns 2 → `RED … (after … is not listed or a backticked value)`. The deploy smoke would be RED on both rows | FAIL |
| 19 | marker counts vs the file | `source: UNMEASURED` 2 at BASE → 0 after both comment lines are replaced; `# source: X3 reports/f5-x3-measure-2026-10-20.md` 0 → 2 (T1, T2); `(warm model)` 0 → 1 (T2 only); `cold load 8.67 s from the mainframe log (proxy, not a live cold call)` 0 → 1 (T1). Agree with the rows | OK |
| 20 | smoke reads: `curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/` · `ls /Users/cobalt/cobalt/ops/com.cobalt.checkpoint-0715.plist` | both are mapped shapes; `exit 0, `200`` and `exit 0, listed` are expectations the script reads; the plist is on disk now (`ls` exit 0) | OK |
| 21 | tests assert an invariant only (L69) | int, > 0, multiple of 5, not `local.plan`'s `timeout_s`; registry `timeout_s` > route + 60; block has no `UNMEASURED`, exactly two `# source: X3 …` lines; `max_output_tokens` int, multiple of 64, `>= 256`. RED on BASE for the right reason (the block holds `UNMEASURED`; the count of two is 0). But T1 says the test "never spells 25 or 256" while T2 says `>= 256`, and CHECK ASK X2 says "no 10, no 256 spelled" (the 10 is the old X3 value) | FAIL |
| 22 | `## GATE` and `desk-launch.sh` (`git grep -n "GATE\|RULINGS\|BAND" -- ops/desk/desk-launch.sh`) | the card states the gate (build only after the 945 check's last line is `CHECK DONE · … ready: YES`; BASE moves with the 945 tip). `desk-launch.sh` greps no `## GATE`; it checks `RULINGS` (`:1312-1331`, `R1863` is `<date> R<n>`) and `BAND` (`:1930-1955`, BAND LOW is allowed for a card dated on or after 2026-10-16). The gate is the desk's, not the launcher's | OK |
| 23 | scope fences | no `src/`, no plist, no `jobs.yaml`, no `ops/`; files per row: `modelaccess.yaml`, `test_checkpoints_offline.py`, `prefill/checkpoints.md` | OK |

## ISSUES

- FAIL (check 18): DEPLOY PROOF lines 3 and 4 (`(warm model)`, `cold load 8.67 s …`) carry a trailing parenthetical after `after `1``. `deploy-smoke.sh` reads the whole tail as the `after` value and marks both rows RED. Fix: end each line at `after `1``; move "(T2's line only)" / "(T1's line)" to a line without `· before` or to `## RECORDS`.
- FAIL (check 21): the NEW test's instruction contradicts itself. T1 and X2 say it spells no value (`25`, `256`, and an old `10`); T2 says `max_output_tokens … >= 256`. Fix: say "the rule's floor, read as a named constant in the test" or drop the `>= 256` and keep "int, multiple of 64"; change X2's "no 10" to "no 25".
- NOTE: `mainframe.log:12` and `:31` carry no date; the card's "both 2026-09-09" is not in the log. Line 12 loads `qwen3.8-27b`. The proxy is a load time from a September log, not a live cold call (the card says so in the source comment).
- NOTE: `configs/cobalt/jobs.yaml:253-256` still says "above the route's provisional 60 s" and `test_checkpoints_registry.py:23` says "UNMEASURED". The card fences both; the stale text stays after this job. The 300 s is still above 25 + 60.
- NOTE: the build waits on the 945 check (`f5-x3-measure-check-2026-10-20.md`, last line `CHECK DONE · … ready: YES`) by design; that is not a block of the card. If the check moves the tip, set BASE to it first (stated in `## GATE`).
- BLOCKS THE BUILD: the two FAILs above (a card edit of three lines). Nothing else.

PREFLIGHT DONE · card: f5-x3-values · checks: 23 · fails: 2 · ready: NO
