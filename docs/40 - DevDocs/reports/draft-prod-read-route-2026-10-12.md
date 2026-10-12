# draft-prod-read-route — 2026-10-12

## §0 Headline
- Card `prompts/2026-10-12/408-prod-read-route-card.md` drafted, CLASS K5, BASE `«FILL»` (cut after 392's deploy), TIP empty.
- R1: `desk-launch.sh prompt` drops the exact word `"Bash(COBALT_ENV=production uv run cobalt db query *)"` from its allow scan; 406's line launches, a production `migrate` stays refused. Red: `write string 'uv run'`.
- R2: the wake-up `- LAUNCH` span (`CTO-DESK-WAKEUP.md:13`) is the desk line's one pin (`desk-launch.sh desk` and `cto-desk.sh` only read it, and there is no `desk)` arm). It gains the string, plus one row in STANDING-LIST §4. Red: a new test in `test_hub_lines.py`; 392's W7 dict entry for the wake-up becomes that string.
- R3: RESTARTS RUN row (392 W8 precedent), expected none. INSTALL: none (both ops scripts are links to the repo).
- Seam: 392 W6 sits right before the loop R1 edits, and 392 W7 pins the desk line to no production string. 392 deploys first.

## DECISIONS
- ASK DESK: `.claude/settings.json:9` at HEAD already allows the exact string for any session in `/Users/cobalt/cobalt`, so the desk's lack of a DB read is not proven to be a permission block. Keep R2 anyway? [11:04 ET] Default: keep R2 as directed (R1200). The line then carries the string explicitly, and a test pins it.
- ASK DESK: STANDING-LIST §4 gains one row for the desk line's new string, citing 2026-10-08 R686 (L62: a string not in that file is NEW). [11:04 ET] Default: yes, in R2.
- ASK DESK: today, prompt 406 with one added line `RULINGS: 2026-10-08 R686` would pass the F5 exception (`desk-launch.sh:577-592`; the R686 row is HIS RULING · APPROVED and stands in HEAD). That is a route before the deploy, without this card. [11:04 ET] Default: not used; 406 launches unchanged after the deploy (R1200).

## RECORDS
- 11:04 ET, `main` HEAD `b16e5dd4` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`).
- `ops/desk/desk-launch.sh`: kind `prompt` `:527-664`; F5 scan `:577`, `outside` `:578`, loop `:584-592` (`uv run` before `COBALT_ENV=`); `IT REFUSES` prompt comment `:113-125`; kind `desk` `:506-525` reads the wake-up span; `run_launch` eval `:241`; `tool_list` `:297-317`; per-kind case `:886-891` (no `desk)` arm); deploy prod strings `:1535` (sed -n, grep -n).
- `ops/desk/bare-guard.py`: `PROD_READ` `:967`, `prod_read` `:971-1006`, G2 `:1074` (sed -n).
- `.claude/settings.json:9` carries `"Bash(COBALT_ENV=production uv run cobalt db query *)"` exactly. The working-tree diff (`git diff HEAD`) leaves line 9 unchanged and adds other lines that are not this card's (Grep).
- The tests carry no `Bash(…)` form of the string (Grep over `tests/`: no match). `tests/ops/test_bare_guard.py:420` `PROD_QUERY` and `:447-451` `PROD_READS` are command shapes. `:481` `test_g2_every_seat_runs_a_production_db_query_without_the_stamp` covers the desk seat.
- The desk line's `--allowedTools`: 12 words, each one `"…"`-quoted word, blank-separated, ending at `--disallowedTools`; the whole line is a backticked span on `CTO-DESK-WAKEUP.md:13`, eval'd (grep -n).
- Desk-line pins: `grep -rn -F "git -C * merge-base*"` over ops, tests, prompts and Memory finds the live line only at `CTO-DESK-WAKEUP.md:13` and `STANDING-LIST.md:165` (§4). The rest are dated prompts (history), `DEPLOY-HUB.md:11` and `STANDING-LIST.md:129` (both the deploy line). `--name cto-desk` appears in `desk-launch.sh` and in fixtures in `test_desk_launch_prechecks.py:87-89` and `test_desk_size_guard.py:229-231`. `test_hub_lines.py:101-105` pins the flag only. `DESK-LINE.md` does not exist (ls).
- `CTO-DESK-WAKEUP.md` is 12794 bytes (wc -c).
- Prompt 406 (cat): no `RULINGS:` line; allow `"Read" "Write" "Grep" "Bash(date*)" "Bash(COBALT_ENV=production uv run cobalt db query *)"`.
- `cto-2026-10-08.md:39` R686 is HIS RULING · APPROVED. Its working-tree diff deletes one OWED line, not R686 (git diff -U0).
- Card 392 branch `ops/prodwrite-seat-1012b` tip `62ea5957`: W6 `pw_allow`/`pw_bad` before the loop, plus F6/F7/O2 tests; W7 `PROD_ALLOW_TODAY["CTO-DESK-WAKEUP.md"] = []` (`git diff 7744ece9 62ea5957`).
- `/Users/cobalt/.claude/ops/desk-launch.sh` and `bare-guard.py` are links to `/Users/cobalt/cobalt/ops/desk/` (ls -l).
- `src/cobalt/jobs/restarts.py:38`, `:225-228`, `:232`, `:246` (grep -n).
- A Bash `grep` holding `COBALT_ENV=production` was refused by G2 for this seat; the Grep tool read it.

DRAFTED · decisions: 3
