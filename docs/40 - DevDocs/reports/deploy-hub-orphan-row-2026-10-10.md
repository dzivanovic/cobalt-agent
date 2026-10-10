## §0 Headline
- `DEPLOY-HUB.md` has the orphan-clean row in 2 places: 4.2 (`DEPLOY-HUB.md:137`) and STEP-5 (3) (`DEPLOY-HUB.md:162`).
- The hub runs only the dry run `sh /Users/cobalt/cobalt/ops/desk/orphan-clean.sh aset`. `none found` or `verified 0` means clean. `verified ≥ 1` or exit 1 sends 4.2 to STEP-5 with nothing merged. At STEP-5 (3) the same results keep aset DOWN with `DECISION 0 … FOR DEJAN`.
- The ~30 s wait is not a bare allowed command. The default is in place: at 4.2 the hub runs `date` and the dry run again, twice.
- Radar has no call because the script's label table holds `aset` only.

## DECISIONS
- ASK DESK: should the hub run `--kill`? [15:00] Default: dry run only. Card 229 `## RECORDS` says no seat runs `--kill` until `STANDING-LIST.md` names where it may run. That line is still missing, and this job does not touch that file. As a result, a verified orphan ends the deploy FOR DEJAN and the hub does not clean it.
- ASK DESK: the ~30 s wait at 4.2. [15:00] No allowed command waits by itself: `sleep` is not on the line. `wait-stop-line.sh <report> <regex> 30` would time out after 30 s, but that misuses a watch script, and its desk-size guard can exit 3. Default taken: when the dry run reports `verified ≥ 1`, the hub runs `date` and the dry run again, twice, before STEP-5. Those repeats take seconds, not 30 s.
- ASK DESK: radar. [15:00] Default: no call. `orphan-clean.sh radar` is `REFUSED` (exit 1), so a radar call would send every radar deploy to STEP-5. Card 229 `## NOT IN THIS JOB` says a new label needs a new card.
- READER (L67) should check:
  - At 4.2 the dry run comes after aset's print shows `Could not find service` and before 4.3's merge.
  - At (3), aset is never bootstrapped while an orphan is verified.
  - (5)'s stop line then reads `aset: DOWN`.
  - `verified 0` with `spared ≥ 1` can only occur while the job is loaded, and the row treats it as clean.
  - No `--kill`, `sleep` or radar call appears anywhere in the hub.

## RECORDS
- `grep -n -F "launchctl bootout"` on the hub before editing: lines 11 (the allow line, untouched), 137 (4.2) and 158 (STEP-5 (1)).
- `grep -c -F "orphan-clean.sh"` on the hub: 2, one per changed place (`:137` 4.2, `:162` STEP-5 (3)).
- `git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` printed `1 file changed, 2 insertions(+), 2 deletions(-)` for that file only.
- `wc -c` on the hub: 57118 before, 57996 after (+878). The growth is the two rows.
- The script's usage, last lines and exit codes come from `ops/desk/orphan-clean.sh:1-46`. The class (a) allow string `Bash(sh /Users/cobalt/cobalt/ops/desk/*)` is on the hub's allow line at `DEPLOY-HUB.md:11`.
- `STANDING-LIST.md` and the allow line were not touched.

HUB ROW DRAFTED · places: 2 · decisions: 3
