# Draft: F5 gate pass 3 (prompt 970) — 2026-10-21

## §0 Headline
`## THIRD PASS (only on the desk's CONTINUE-3)` is in `prompts/2026-10-21/970-f5-gate-run.md` after `## SECOND PASS`: lock, note Write, migrate up, X2, X6, migrate down, release, note path owed.
The MODEL line gained `Bash(sh /Users/cobalt/cobalt/ops/desk/*)`, `Bash(COBALT_ENV=dev uv run cobalt db *)` and `--add-dir /Users/cobalt/dev-vault-cobalt`, all from standing lines; nothing was removed. Two decisions are open (below). Nothing was committed.

## DECISIONS
- ASK DESK: no standing string can restore the dev DB from a throwaway copy (`ops/desk/gate-lists.md:10-14` has no `COPY CREATE` or `COPY DROP`; there is no `dev-copy` verb in `src/cobalt/db_migrations/cli.py`). Pass 3 step 7 therefore stops on a failed rollback, keeps the lock held and names this for the desk to restore. Default: that stop. [14:58]
- ASK DESK: the added strings reach a seat only through a launch with the edited line. The running `f5-gate-run` seat has the old line, so `CONTINUE-3` needs a fresh launch (or its steps read `NOT RUN — not on the launch line`). Also `sh /Users/cobalt/cobalt/ops/desk/*` is the class (a) string of `BUILD-HUB.md:14`, broader than the two lock scripts; no narrower string is on a standing line, so the section limits its use by text. Default: relaunch, class (a) used for the two lock scripts only. [14:58]

## RECORDS
- Read, all of it: `prompts/2026-10-21/970-f5-gate-run.md`; `reports/f5-gate-run-2026-10-21.md` (X2, X6 lines, `## RECORDS`); `F5-FINAL-2026-10-11.md:176-187`; `src/cobalt/db_migrations/__init__.py:171-229` (last `FORWARD` line `:198`, `0029_market_checkpoints.sql`; `ls` shows the `0029` pair); `git show main:src/cobalt/prefill/checkpoint_probe.py`; `checkpoints.py:640-780`; `BUILD-HUB.md:12-45` (the launch line, THE LOCK); `ops/desk/take-devdb-lock.sh`, `release-devdb-lock.sh`; `ops/desk/gate-lists.md:1-57` (FORWARD, ROLLBACK, PROOF ONLY, `## LEVEL 0013`); `configs/cobalt/templates/daily.md.j2`; `src/cobalt/daymode/note.py:250-268`; `src/cobalt/prefill/daily.py:272`; `configs/dev/vault.yaml`, `configs/dev/aset.yaml:23-24`; `ls` of `~/dev-vault-cobalt/1 - Trading/1- Daily Notes` (four September notes, none for 2026-10-21); `ls /Users/cobalt/cobalt-wt` (`f5-probe` is there).
- `checkpoints.py:747-751`, cited by the old X6 reason and the probe, is stale: on `main` the absent-note branch is `:753-757` and the probe's own check is `checkpoint_probe.py` `_x6` (`daily_note_path(...).exists()`). Code was not edited; pass 3 cites `:779` for the model call, which holds on `main` as read.
- The dev vault root comes from `configs/dev/vault.yaml` (`~/dev-vault-cobalt`) unless `COBALT_VAULT_PATH` overrides it; no env value was read or printed. If the seat's env overrides it, the note lands in the wrong place; step 3's `ls` and X6's own check would show it.
- K1: no standing string removes a file (`Bash(rm …)` is the `.env` string only), so the note's path is named for the desk.
- Times from `date`: end 14:58:33 EDT. Nothing run against the DB, Finviz, or the dev vault; no git write, no launch.

DRAFTED · decisions: 2
