# desk-ops-fixes — draft report 2026-10-08

## §0 Headline
- Card `prompts/2026-10-08/106-desk-ops-fixes-card.md` written: six rows, G1-G6. G1, G2, G3 and G5 are ready to build. G4 and G6 are HELD because each needs a new command (R411/R412): D1, D2.
- G3 is not `install-fixed.sh`. The ops install is `desk-launch.sh install-ops` (`:616-639`), and its plain-file KEPT is the 10-07 fault: D3.
- The only Mattermost sender is `src/cobalt/notify/mattermost.py:130` `send_dm`. It has no CLI and needs the vault key.
- Not committed. BASE is the only fill token.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/106-desk-ops-fixes-card.md` (13954 bytes).
- Measured against 6 rows. Lines and tokens are the drafter's estimates; the build reports the real ones.

| row | files touched | est. lines changed | est. build tokens | state |
|---|---|---|---|---|
| G1 | 2 | ~25 | ~15k | ready |
| G2 | 2 | ~30 | ~15k | ready |
| G3 | 2 | ~35 | ~20k | ready |
| G4 | 2 | ~30 | ~20k | HELD D1 |
| G5 | 2 | ~40 (wake-up +1 line, ~520 bytes) | ~15k | ready |
| G6 | 2 | ~20 | ~10k | HELD D2 |

## DECISIONS
- D1 ASK DESK: G4 has no existing sender command. Choose A or B. A: `close-timer.sh` sources `~/.cobalt_key` in a subshell (the `ops/run_backup.sh:26-32` form) and runs `uv run --project <repo> python -c '…send_dm(sys.argv[1])'`, a new command in an ops script that brings the vault key into the timer. B: a `cobalt notify` CLI in `src/`, its own card. Recommend A. DEFAULT: G4 leaves this card and waits for its own card [07:45 ET].
- D2 ASK DESK: G6 has no path without a new command or `src/`. Choose A or B. A: `DAY-OPEN-QWEN.md` S0 runs `sh /Users/cobalt/.claude/ops/desk-list.sh`. That needs his Qwen allow line, and only a grep pin can test it. B: a day-open check C7 in `src/cobalt/dayopen/checks.py`, its own card, which gives the stubbed-list red R658 names. Recommend B. DEFAULT: G6 leaves this card for a B card [07:45 ET].
- D3 ASK DESK: G3 lands in `ops/desk/desk-launch.sh` (the install-ops block and its header only), not `install-fixed.sh`, so the card's files list names `desk-launch.sh`. DEFAULT: as written [07:45 ET].

## RECORDS
All reads were at main HEAD `c6b4a04d` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`, 07:0x EDT).
- `reports/cto-2026-10-08-words.md:3-4` R657 "approved"; `reports/cto-2026-10-08.md:10` R657 and `:11` R658, both `HIS RULING · APPROVED`.
- `grep -rn "\.claude/ops" ops/desk/`: the link folder is written only at `desk-launch.sh:621` (install-ops). `close-timer.sh:38` reads `desk-list.sh` there. `install-fixed.sh` has no hit (it is the «INSTALL token installer, `:1-14`).
- `desk-launch.sh:74-80` (header), `:616-639` (install-ops; KEPT at `:628-630`), `:333-341` (close hour gate, 21:00 ET).
- `ops/desk/stop-guard.py` (340 lines): `first_user_text` `:100-118`, `report_last_line` `:135-144`, `Unguarded` `:147-148`, `is_desk` `:151-164`, `listed` `:219-229`, `watched` `:232-240`, `desk` `:269-299`, fail-open `:312-318`. `ops/desk/idle-wake.py:42` calls `report_last_line`.
- `tests/ops/test_stop_guard.py` (646 lines): `stage` `:29-38`, `Desk.first` `:290-299` (first user entry `:294`, no `sessionKind`), `test_g1_the_desk_with_no_owed_block_is_blocked` `:334-338`, `test_g3_a_live_session_id_lets_the_turn_end` `:449`, `unguarded` `:557-559`, `test_g5_a_failing_desk_list_fails_open` `:589-593`.
- `ops/desk/close-timer.sh` (107 lines): `refuse` `:42-45`, refuse calls `:64 :68 :72 :75 :76 :101`. `tests/ops/test_close_timer.py` (256 lines): `box` `:65-115`, refused tests `:162-175`.
- `tests/ops/test_install_ops.py` (153 lines): `:27-45` tmp roots, `:63-78`, `:81-95`, `:97-104`.
- `tail -n 20 /Users/cobalt/cobalt-wt/.timer-logs/close-timer.out`: the last 7 lines are `REFUSED: the session list is unreadable: /Users/cobalt/.claude/ops/desk-list.sh`.
- `grep -rn -i "mattermost" ops/` finds role provisioning only (`ops/mattermost_role_provision.py`, `ops/pg_role.py`, `ops/cobalt_app_role_provision.py`, `ops/README.md:26,401`) and no sender. Repo-wide, the one sender is `src/cobalt/notify/mattermost.py:130` `send_dm`; it needs the key at `:70-77`, and `MASTER_KEY_ENV = "COBALT_MASTER_KEY"` is at `src/cobalt/redact/secrets.py:64`. `ops/README.md:400` says there is no `cobalt notify` command. `ops/desk/com.cobalt.close-timer.plist:11-16` sets only `PATH`.
- `sessionKind`: this drafter's own transcript (`914e0a53…jsonl`) carries `"sessionKind":"bg"` on line 8, its first user entry. A Grep for any other value across `~/.claude/projects/-Users-cobalt-cobalt/*.jsonl` found none. `grep -L -r` lists transcripts with no key (e.g. `cb1427d3…`, `e536403a…`).
- `prompts/CTO-DESK-WAKEUP.md` (51 lines, 11608 bytes): WAIT `:16`, EVERY TURN `:40`, OWED `:42`. `ops/desk/wait-stop-line.sh` (95 lines): guard `:64`, loop `:74-93`, timeout exit 2 `:94-95`.
- Day-open: `src/cobalt/cli.py:24,67,515`; `src/cobalt/dayopen/checks.py` C1-C6 `:87-391`. `grep -rn -i day-open ops/` finds no hit. `prompts/DAY-OPEN-QWEN.md` (3576 bytes) S0 `:7-10`, VERDICT `:27-28`. `~/.qwen/settings.json:58-69` allows no `sh`.
- `LAWS.md`: `### L58 Memory write path` `:304`, `### L79` `:386`. No `ROW B` anywhere under `Memory/` (Grep).
- Card shape: `prompts/CARD.md` whole; precedent `prompts/2026-10-07/83-worktree-salvage-card.md`; `BUILD-HUB.md:93-97` PRE-STOP SELF-CHECK.

DESK OPS FIXES CARD DRAFTED · decisions: 3
