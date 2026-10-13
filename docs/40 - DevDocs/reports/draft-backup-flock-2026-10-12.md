# draft backup-flock · card 441

## §0 Headline
Card written: `prompts/2026-10-12/441-backup-flock-card.md`, CLASS K5, build kind, BASE the desk's placeholder, TIP empty.
Rows: F1 flock on `STAGING/.backup.lock` + own-file cleanup (T1-T3, the brain's three reds), F2 the 30 min as `backup.yaml` `lock_wait_min` (T4-T5), R3 RUN restarts.
RESTARTS expected `com.cobalt.aset com.cobalt.radar` (backup.yaml in aset's reads; restic.py reached by radar through `cobalt.cli`), not none.
`DB` key left out: the rows touch `src/`, `configs/`, `tests/cobalt/`, which `BUILD-HUB.md:80` refuses under `DB: none`.
No new command. 5 decisions, defaults taken.

## DECISIONS
1. ASK DESK: the prompt set `DB: none`; `BUILD-HUB.md:80` (W (a0)) fails a `DB: none` card whose diff holds a path outside `ops/`, `tests/ops/`, `docs/`, and this card writes `src/cobalt/backup/`, `configs/cobalt/backup.yaml`, `tests/cobalt/test_backup.py`. Default taken: key left out (the build takes the `cobalt_dev` lock and runs all three suites). [21:55 EDT]
2. ASK DESK: the wait's home. Two settings homes exist: `configs/cobalt/backup.yaml` (`BackupConfig`, `extra="forbid"`, already loaded by `snapshot()`, `restic.py:164`) and `configs/cobalt/taxonomy/tunables.yaml` (the house note `notify/mattermost.py:39-44`: a threshold with consumers is a tunables row). Default taken: `backup.yaml` `lock_wait_min: 30` (no new loader caller, the pinned reader test `test_jobs_restarts.py:440` stands; no tunables `status`/`source` for a brain-set value). The other choice moves F2's files to `tunables.yaml` + a reader in `restic.py`. [21:55 EDT]
3. ASK DESK: a hub `backup run` (DEPLOY-HUB D2.4, `DEPLOY-HUB.md:39`, `:131`; PRODWRITE-HUB, `PRODWRITE-HUB.md:34`) runs FOREGROUND with `timeout` 600000 (10 min); meeting the 21:40 nightly, it waits on the lock past its own tool timeout and is killed, not failed loud. Default taken: no hub change in this job (fenced); the desk keeps a D2.4 or prodwrite launch off the nightly's window. A hub amendment is the desk's own card. [21:55 EDT]
4. ASK DESK: the nightly's `timeout_s: 3600` (`jobs.yaml:263`) covers a 30 min wait plus the dump and snapshot (attempt 2's dump 7133.7 MB, `deploy-recut-archive-1012.md:301`); its margin is not measured. Default taken: unchanged, fenced. [21:55 EDT]
5. ASK DESK: R1289 calls this a "devfix card"; `CARD.md`'s devfix kind is one `cobalt_dev` table rebuild with no rows. Default taken: a build card (rows, check, deploy), as card 434. Its deploy restarts aset and radar (§0), so it needs an outage window like card 45's (`2026-10-06/45-deploy-card-39-card.md:25`). [21:55 EDT]

## RECORDS
- `main` HEAD `c70f7cc7` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`, 21:52 EDT). Reads 21:47-21:56 EDT.
- `prompts/CARD.md` whole; `prompts/2026-10-12/434-recut-archive-card.md` whole (precedent: `CLASS`, `INSTALL`, `RESTARTS`, `DB` header keys, `## RECORDS` shape).
- `reports/cto-2026-10-12.md` R1288, R1289, R1293 and OWED lines `:164`, `:167` (`grep -n`).
- `reports/deploy-recut-archive-1012.md` `:5`, `:156-158`, `:164`, `:194`, `:203`, `:206`, `:229`, `:300-302` (Grep, `sed -n 157p`). One `grep -n -E` over it was blocked by the `bare-guard.py` hook ("route: production is the deploy hub's"); re-read with the Grep tool.
- `src/cobalt/backup/restic.py` whole (`cat -n`, 295 lines): dump write `:184` → `:159`; `finally` `:193-197`, glob `:196`; `STAGING` `:48`.
- `src/cobalt/backup/pgdump.py` whole (117): `out.open("wb")` `:99`, size `:105`. `src/cobalt/backup/config.py` whole (184): `BackupConfig` `:136-158`, refusal `:164-165`. `src/cobalt/backup/cli.py` whole (81): `_run` `:45-55`, imports `:18-19`.
- Writers into STAGING: Grep `STAGING|cobalt-backups|staging|backup\.lock|flock|fcntl` over the repo, docs excluded → only `restic.py:180`, `:184`, `:196`; flock precedent `src/cobalt/voice/scratch.py:200-213`.
- Callers of `backup run`: `ops/run_backup.sh:39` (whole, 39 lines), `DEPLOY-HUB.md:131`, `PRODWRITE-HUB.md:34` (`grep -n -F "backup run"`).
- `configs/cobalt/backup.yaml` whole (83); `configs/cobalt/jobs.yaml` `:60-80`, `:190-206`, `:250-275`, `:75` (`grep -n -F`); `configs/cobalt/taxonomy/tunables.yaml` `:970-1000`.
- `src/cobalt/jobs/restarts.py` whole (281); `src/cobalt/cli.py:67` (`grep -n -F backup`); `tests/cobalt/test_jobs_restarts.py` `:440-500`, `:473`.
- `tests/cobalt/test_backup.py` whole (226): `_cfg` `:29-41`, `TestSnapshotRefusals` `:133-148`, `TestMountGuard` `:151-201`, `TestStagingPath` `:204-226`.
- `BUILD-HUB.md` `:12` (build seat line: `uv run pytest *`, `uv run cobalt jobs restarts *`), `:17-24`, `:73-80`.
- `wc -l` of the six backup files: 295, 184, 117, 81, 226, 83.
- Card placeholder check: `grep -n -F "«"` on the card → line 7 (BASE) only.
DRAFTED · decisions: 5
