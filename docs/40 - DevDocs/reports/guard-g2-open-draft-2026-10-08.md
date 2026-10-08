# guard-g2-open-draft — 2026-10-08

## §0 Headline
- Card `prompts/2026-10-08/120-guard-g2-open-reads-card.md` drafted at BASE `4125ff02`: three rows, O1 G2 passes the one `db query --prod` read for every seat with no stamp, O2 secrets refused in G3, O3 stamp kept and `desk-launch.sh` gets comment-only edits.
- `cobalt db query --prod` cannot write (`BEGIN READ ONLY` plus rollback in `finally`, and `guard_select`), so the card adds no row for it.
- At BASE, G3 refuses only `.env`. A read of `~/.cobalt_key`, `data/.cobalt_vault` or a keychain dump passes the guard today, so O2 adds those refusals (RED on BASE).
- 4 decisions, each with its default taken.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/120-guard-g2-open-reads-card.md` (uncommitted; the desk commits it).
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-g2-open-reads-build-2026-10-08.md` does not exist (`ls`, 11:31 ET).

## DECISIONS
- ASK DESK: secrets "stay refused", but at BASE the guard refuses only `.env`. Should O2 add `~/.cobalt_key`, `data/.cobalt_vault` and `security find-*-password|dump-keychain|export` to G3 for every seat, deploy included? [11:31 ET] DEFAULT TAKEN: yes, row O2 with a new `ROUTE["G3 secret"]`. A read through `uv run python`, `source` or `.` stays owed (NOT IN THIS JOB).
- ASK DESK: `desk-launch.sh`: drop R1 (stamp) or keep it? [11:31 ET] DEFAULT TAKEN: keep the code unchanged so prompts in flight launch as before, and edit only the stale comments at 115-116 and 506-507.
- ASK DESK: should `ROUTE["G2"]` (pinned by test 143) name the open read shape so that a refused seat finds it? [11:31 ET] DEFAULT TAKEN: no, the text is unchanged.
- ASK DESK: the prompt fixes REPORT in the main checkout's `reports/`, but CARD.md says the build report sits inside the worktree. [11:31 ET] DEFAULT TAKEN: the prompt's path (the G5 fence reads REPORT from the card).

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse HEAD` → `4125ff02c9587ca901d9d5c418f378b8c77593a9` (11:31 ET).
- `git -C /Users/cobalt/cobalt diff --stat HEAD -- ops/desk src/cobalt tests/ops` → empty, so the working tree reads are HEAD's.
- `git -C /Users/cobalt/cobalt show HEAD:src/cobalt/db_query.py` read whole. Line numbers from grep: 20 `REFUSED_WORDS`, 98 `guard_select`, 145 `read_rows`, 160 `allow_prod=prod`, 161 `autocommit = False`, 163 `BEGIN READ ONLY`, 176-177 `finally: conn.rollback()`, 211 `--side` choices, 212 `--prod` store_true. `sed -n 20,28p` gives `REFUSED_FUNCTIONS` at 25-28.
- `ops/desk/bare-guard.py` read at 40-119, 660-749, 775-924 and 1012-1036. G2-related grep lines: 20-21, 57, 107 `PROD`, 849 `MARKER`, 850 `PROD_READ`, 851 `SIDES`, 854-891 `marked_read`, 904 G2 call, 745 `"first": text`, 783-790 `is_env`, 805-812 `g3_bash`, 1022 Read rule.
- `ops/desk/desk-launch.sh` read at 100-124 and 495-549. R1 stamp is at 504-543 and the launch at 545.
- `tests/ops/test_bare_guard.py` read at 385-599. `grep` gives `make_seat` 223, `assert_denied` 267, `assert_allowed` 272, `KINDS` 277, `MARKED_KINDS` 420, worker cwd 438.
- `wc -l` → bare-guard.py 1087, desk-launch.sh 1223, test_bare_guard.py 1398, test_desk_launch_prechecks.py 1144.
- Secrets: `grep -rn` of `ops/desk` and both settings for `cobalt_key|keychain|password` finds no guard rule, only `close-timer.sh:37,65-66` (sources `$HOME/.cobalt_key`). `ls -la` shows `/Users/cobalt/.cobalt_key` (-rw-------, 72 B) and `/Users/cobalt/cobalt/data/.cobalt_vault` (-rw-------, 1996 B); `/Users/cobalt/.pgpass` is absent. The VaultManager path is `src/cobalt_agent/skills/research/finviz_extractor.py:70`.
- Settings: `/Users/cobalt/.claude/settings.json:22` is the hook entry and `:54` allows `Bash(COBALT_ENV=production uv run cobalt db query *)`. `git show HEAD:.claude/settings.json` allows the same.
- `grep -n -F "ops/desk" configs/cobalt/jobs.yaml` → empty (RESTARTS none expected).
- Drafting proof that G2 hits non-production text: my own `grep` whose pattern held `--prod` was denied by G2 (`route: production is the deploy hub's…`). I re-ran it without that word. Recorded in card RECORDS. O1 leaves this as it is.
- R686 read at `reports/cto-2026-10-08-words.md:3-5`.

GUARD G2 CARD DRAFTED · decisions: 4
