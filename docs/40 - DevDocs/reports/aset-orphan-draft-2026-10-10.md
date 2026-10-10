# aset-orphan · drafter report · 2026-10-10

## §0 Headline
- Card written: `prompts/2026-10-10/222-aset-orphan-card.md`, `BASE` left `«FILL»` for the desk.
- Row A takes (ii): `start_aset.sh` runs `uv sync --inexact`, then execs `.venv/bin/python`. The plist is untouched.
- (i) is not taken: DEPLOY-HUB.md:88 refuses a modified `ops/com.cobalt.*.plist`, so (i) cannot ship through the hub.
- Row B audit: aset is the only KeepAlive resident with the defect. No other plist or script changes.
- Row C, orphan-clean and ops-hand are fenced under `## NOT IN THIS JOB`.

## CHANGES
- NEW `docs/40 - DevDocs/prompts/2026-10-10/222-aset-orphan-card.md`: header per the prompt (`DB:` omitted); `## ROWS` A, B; `## NOT IN THIS JOB`; `## READ`; `## CHECK ASKS` (FOR THE CHECK verbatim, X1–X3); `## RECORDS` (code base, RESTARTS, DEPLOY PROOF, approval, no new command).
- NEW this report.

## DECISIONS
1. Row A takes (ii), not (i). Reasons:
   - DEPLOY-HUB.md:88 refuses any plist ADDED or MODIFIED under `ops/` with a jobs.yaml label ("the desk runs it as its own job"). Under (i) the fix needs a separate desk job, which means new strings (R411, R412).
   - The plist comment beside the key (`com.cobalt.aset.plist:31–40`) explains RunAtLoad and KeepAlive. It does not explain `AbandonProcessGroup`. Its only link is "matches archiver/prefill's detached, supervised posture" (`:37–38`). The archiver's "detached" note (`archiver.plist:41–46`) is about launchd versus an interactive session, which this key does not govern. So the key has no aset-specific reason, but removing it is still blocked by the hub.
2. (ii) keeps the start-time sync in the script (`uv sync --inexact`, the default `uv run` sync). The card does not rely on the deploy's own `uv run`, for two reasons:
   - The aset rows `jobs.yaml:88–89` (`pyproject.toml`, `uv.lock`: "uv syncs the environment … when the process starts") stay true.
   - The venv also stays current on any KeepAlive restart, not only after a deploy's 4.5.
   - The builder confirms the flag with `uv sync --help` (X2).
3. `configs/cobalt/jobs.yaml` is left untouched. The deploy hub runs no `jobs register` (DEPLOY-HUB.md:3), and a registry edit would put a `registry; register` row into RESTARTS (`restarts.py:223–224`). The cost: the comments at `:88–89` keep citing `start_aset.sh:73 (exec uv run …)`, which goes stale. The next card that touches jobs.yaml re-points them.
4. DEPLOY PROOF gap: `<old aset pid>` from `launchctl print` is the `uv` pid under the OLD script. Its python child is the one that orphans. So `ps -p <old aset pid>` → header only does not by itself prove the child gone. The card adds a second read on an existing string: after 4.6, `launchctl print` aset twice with the same pid. A lock collision would show as a KeepAlive restart loop. This deploy's own 4.2 can still orphan the old python, and row C (his) is what closes that. Default: the deploy goes on existing strings, with the gap named.
5. Row B scope: KeepAlive residents get the fix. They are radar, aset, herdr and obsidian (`KeepAlive` at `radar:28`, `aset:42`, `herdr:79`, `obsidian:35`). Registry residents without KeepAlive are listed, not fixed:
   - mainframe: clean, no `AbandonProcessGroup`.
   - agent: `AbandonProcessGroup` is load-bearing (`cobalt.sh:59` nohup detach; `jobs.yaml:139–145`).
6. One-shots are listed and none is fixed. No deploy boots one out (DEPLOY-HUB.md:137), and none holds a port. The only lock is the archiver's session advisory lock (`archiver/store.py:64`), which is released when its run ends.

## RECORDS
- `git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD` → `c3a484e4`; `git -C /Users/cobalt/cobalt diff --stat d0a5fbb8 HEAD -- . ":(exclude)docs"` → nothing.
- Read at `d0a5fbb8` (`git -C /Users/cobalt/cobalt show d0a5fbb8:<path>`):
  - `ops/com.cobalt.aset.plist` (`AbandonProcessGroup` at `:29–30`, comment `:31–40`, KeepAlive `:42`).
  - `ops/start_aset.sh` (`:35` scratch dir, `:67` cd, `:68–72` comment, `:73` exec).
  - `ops/com.cobalt.radar.plist`, `ops/com.cobalt.mainframe.plist`, `ops/com.cobalt.agent.plist`, `ops/com.cobalt.archiver.plist`, `ops/com.cobalt.herdr.plist`, `ops/com.cobalt.obsidian.plist`.
  - `ops/start_mainframe.sh`, `ops/README.md`, `configs/cobalt/jobs.yaml`, `src/cobalt/jobs/restarts.py`, `tests/ops/conftest.py`, `tests/ops/test_install_ops.py`, `tests/cobalt/test_jobs_reads.py`.
  - `git … show d0a5fbb8:ops/` and `git … show d0a5fbb8:tests/ops/` listings.
- Greps at `d0a5fbb8`:
  - `AbandonProcessGroup|KeepAlive|exec |uv run|ProgramArguments` over `ops/` → `AbandonProcessGroup` in agent:32, archiver:31, aset:29, backup:67, cards-expire:41, daymode-propose:35, generated:46, heartbeat:47, prefill-daily:33, replay:28, seat-usage:42. `KeepAlive` key in aset:42, herdr:79, obsidian:35, radar:28. `run_backup.sh:39` `exec …/uv run cobalt backup run`.
  - `subprocess|Popen|os.fork|start_new_session|setsid|multiprocessing` over `src/cobalt/aset`, `src/cobalt/voice` → nothing.
  - Locks over the one-shot and radar packages → `src/cobalt/archiver/store.py:64` only.
  - Locks in `voice/scratch.py` → `DirectoryLock` `:193–209`, `flock` `:202`.
  - `cobalt.sh` → `:59` nohup, `:71` kill -15.
- Line counts on main (same code): `start_aset.sh` 73, `com.cobalt.aset.plist` 49, `scratch.py` 269. Program lines: herdr:62, obsidian:30, mainframe:35.
- `DEPLOY-HUB.md` (main `c3a484e4`): `:3` no `jobs register`; `:88` plist refusal; `:137` 4.2; `:141` 4.6 bootstrap from `ops/com.cobalt.aset.plist`; `:158` STEP-5 (1); allow list `:11` holds `ps -p *` and `launchctl print gui/501/*`.
- launchd.plist(5) `AbandonProcessGroup`: when a job dies, launchd kills the remaining processes of its process group unless this key is true. This is from the drafter's knowledge and was not run here; the live proof is the deploy.
ASET ORPHAN CARD DRAFTED · decisions: 6
