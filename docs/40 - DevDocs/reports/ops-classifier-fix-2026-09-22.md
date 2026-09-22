# OPS CLASSIFIER FIX — `configs/cobalt/backup.yaml` declared one-shot-only (2026-09-21 19:28–19:32 ET)

## §0 Headline
- `configs/cobalt/backup.yaml` is now a row in `jobs.yaml` `no_resident_reads` (readers: `com.cobalt.backup`, `com.cobalt.heartbeat`) with a test; `restarts.py` and all of `src/` untouched.
- `uv run cobalt jobs restarts main..HEAD`: exit 1 → exit 0; `RESTARTS: none`; no `UNCLASSIFIED` row.
- Offline suite 2209 → 2210 passed, 0 failed, 351 skipped, 1 xfailed (baseline + the one new test).
- 2 fix commits (Z1 `d669dfa`, Z2 `ac2e7ae`) on `ops/2026-09-21` from `f6aa4d0`. ESCALATE: 6 (all carried or noted, none blocks).

## L74
A block that arrived appended to the tool result of the Read of this prompt file asked for a `Claude-Session: https://claude.ai/code/session_…` line in commit messages and PR bodies and named a file-send tool. It is DATA (L74); not followed. Recorded once, here. Commits carry `Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Each check its own call; all passed.

| Check | Result |
|---|---|
| R25 row, `cto-2026-09-20.md` | line 262, names `11-bars-chunk-2-build.md` and "approved" |
| R25 committed on main | `fec68e3b914d19e26645d916a890e6ec7dcb9360` |
| R43 row, `cto-2026-09-21.md` | line 54, "App approved", names `06-ops-0921.md` |
| R43 committed | `031196fe9a35132e2e453dbfe613f0f33185015e` |
| R53 row | line 65, names `69-ops-6a-check.md` |
| round-1 check on main | `e27c864 docs(desk): 09-21 ops 6a checked 4 of 4, classifier gap goes to a fix round, drafter launched` |
| launch row R54 | `cto-2026-09-21.md` line 66, names `77-ops-classifier-fix.md`; `cto-2026-09-22.md` does not exist (grep exit 2, recorded — the row is in the other file, not fatal) |
| R54 committed | `4d9c0439b678618c8fa2f00c675de177b24d3ec0` |
| 16 allow strings + 3 deny strings in `02-bars-chunk-2-fix-r3.md` | each `grep -c -F -e '"<rule>"'` = 1 (19 of 19) |

## PREFLIGHT
| Rule | Command | Exit | Result |
|---|---|---|---|
| date | `date` | 0 | allowed — `Mon Sep 21 19:28:57 EDT 2026` |
| clean tree | `git status --porcelain` | 0 | allowed — empty |
| branch | `git status` | 0 | allowed — "On branch ops/2026-09-21 / nothing to commit, working tree clean" |
| tip | `git log --oneline -1` | 0 | allowed — first launch; `<old tip>` = `f6aa4d0` |
| branch moved? | `git log --oneline f6aa4d0..HEAD` | 0 | allowed — empty |
| tip stat | `git show --stat HEAD` | 0 | allowed — `f6aa4d0`, 1 file (`ops-2026-09-21.md`) |
| unstaged | `git diff --stat` | 0 | allowed — empty |
| main tip | `git -C /Users/cobalt/cobalt log --oneline -1` | 0 | allowed — `<main tip>` = `914ee14 docs(desk): 09-21 ops classifier fix build launched` |
| main's runtime paths | `git -C … log --oneline ops/2026-09-21..main -- src configs ops tests .gitignore` | 0 | allowed — empty |
| no `.env` | `ls -la .env` | 1 | allowed — "No such file or directory" |
| branch report last line | `tail -n 3 …ops-2026-09-21.md` | 0 | allowed — last line starts `OPS 0921 DONE ` |
| new report absent | `ls …ops-classifier-fix-2026-09-22.md` | 1 | allowed — "No such file or directory" (first launch) |
| table locate | `grep -n "no_resident_reads\|path: configs/cobalt" configs/cobalt/jobs.yaml` | 0 | allowed — `:301` table, `:302` notify row, `:309` rules row |
| classifier locate | `grep -n "watchlists.yaml\|backup.yaml\|no_resident_read" src/cobalt/jobs/restarts.py` | 0 | allowed — `:205`, `:243` as on the card |
| cwd | `cd /Users/cobalt/cobalt-wt/ops-0921` | 0 | allowed |
| runner | `uv run pytest --version` | 0 | allowed — `pytest 9.0.2` |
| mkdir rule | `mkdir -p "docs/40 - DevDocs/reports"` | 0 | allowed — a no-op (the directory exists), which is how that rule is probed |

No command was denied, so there is no classifier reason string to quote. `git add` / `git commit` were probed by Z1's first real use and allowed; `uv run cobalt jobs restarts` by BASELINE.

## BASELINE
Suite line, verbatim (`uv run pytest -q tests/cobalt tests/taxonomy`, started after the 19:28:57 ET preflight `date`):

    2209 passed, 351 skipped, 1 xfailed, 15 warnings in 64.19s (0:01:04)

= the branch's own `2209 passed, 351 skipped, 1 xfailed`, 0 failed.

THE RED OF THE COMMAND — `uv run cobalt jobs restarts main..HEAD`, exit **1**, verbatim:

    FAILED: RestartError: one or more changed paths were unclassified
    path	change	rule	restart
    .gitignore	M	META	-
    configs/cobalt/backup.yaml	M	UNCLASSIFIED CONFIG	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
    ESCALATE: unclassified path configs/cobalt/backup.yaml
    docs/00 - Project/BACKLOG.md	M	DOCS	-
    docs/30 - Design/DRC-SITTING-PACKET-2026-09-21.md	D	DOCS	-
    docs/30 - Design/S3-EXITS-PROPOSAL-2026-09-21.md	D	DOCS	-
    docs/30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/cobalt/backup/config.md	M	DOCS	-
    docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/58-s2-smoke-first-look.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/59-propose-stale-score.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/60-draft-stale-score-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/61-stale-score-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/62-stale-score-tribunal-fable-seat.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/63-stale-score-tribunal-derive.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/64-draft-setups-one-build.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/65-setups-one-build.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/66-setups-one-check.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/67-draft-tuesday-checks.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/68-stale-marker-check.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/69-ops-6a-check.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/70-propose-s3-exits.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/71-draft-drc-sitting-packet.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/72-draft-s3-exits-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/73-s3-exits-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/74-s3-exits-tribunal-fable-seat.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/75-s3-exits-tribunal-derive.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/76-draft-ops-classifier-fix.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/77-ops-classifier-fix.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/78-ops-6a-check-r2.md	D	DOCS	-
    docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md	M	DOCS	-
    docs/40 - DevDocs/reports/cto-2026-09-21.md	M	DOCS	-
    docs/40 - DevDocs/reports/drc-sitting-packet-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/ops-2026-09-21.md	A	DOCS	-
    docs/40 - DevDocs/reports/ops-6a-check-2026-09-22.md	D	DOCS	-
    docs/40 - DevDocs/reports/ops-classifier-fix-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/s3-exits-design-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/s3-exits-tribunal-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/setups-one-build-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/stale-score-design-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/stale-score-tribunal-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/tuesday-checks-draft-2026-09-21.md	D	DOCS	-
    tests/cobalt/test_backup.py	M	test/documentation; no resident	-
    RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar

It is the branch report's table: exit 1, `UNCLASSIFIED CONFIG`, `ESCALATE: unclassified path configs/cobalt/backup.yaml`.

## READERS
Each result verbatim, each its own call. Expected-empty last grep returned no output.

`grep -rn "load_backup_config" src`

    src/cobalt/heartbeat/probes.py:426:    from cobalt.backup.config import BackupConfigError, load_backup_config
    src/cobalt/heartbeat/probes.py:431:        cfg = load_backup_config()
    src/cobalt/backup/__init__.py:3:from .config import BackupConfig, BackupConfigError, load_backup_config
    src/cobalt/backup/__init__.py:12:    "load_backup_config",
    src/cobalt/backup/config.py:161:def load_backup_config(path: Path = CONFIG_PATH) -> BackupConfig:
    src/cobalt/backup/config.py:183:    "load_backup_config",
    src/cobalt/backup/restic.py:38:from .config import BackupConfig, Destination, load_backup_config
    src/cobalt/backup/restic.py:164:    cfg = cfg or load_backup_config()
    src/cobalt/backup/restic.py:248:    cfg = cfg or load_backup_config()
    src/cobalt/backup/restic.py:269:    cfg = cfg or load_backup_config()
    src/cobalt/backup/cli.py:18:from .config import load_backup_config
    src/cobalt/backup/cli.py:59:    cfg = load_backup_config()

`grep -rn "backup_freshness" src`

    src/cobalt/heartbeat/runner.py:144:        probe_mod.backup_freshness(now=ts),
    src/cobalt/heartbeat/probes.py:416:def backup_freshness(now: Optional[datetime] = None) -> Probe:

`grep -rn "take_beat\|run_beat" src`

    src/cobalt/heartbeat/cli.py:20:from .runner import run_beat, take_beat
    src/cobalt/heartbeat/cli.py:27:    beat = run_beat(dry_run=args.dry_run)
    src/cobalt/heartbeat/cli.py:34:    print(take_beat().console())
    src/cobalt/heartbeat/__init__.py:14:from .runner import run_beat, take_beat
    src/cobalt/heartbeat/__init__.py:16:__all__ = ["Beat", "Probe", "run_beat", "take_beat"]
    src/cobalt/heartbeat/runner.py:126:def take_beat(*, now: Optional[datetime] = None, probe: bool = True) -> Beat:
    src/cobalt/heartbeat/runner.py:486:def run_beat(*, now: Optional[datetime] = None, dry_run: bool = False, probe: bool = True) -> Beat:
    src/cobalt/heartbeat/runner.py:493:        beat = take_beat(now=ts, probe=probe)
    src/cobalt/heartbeat/runner.py:560:    "run_beat",
    src/cobalt/heartbeat/runner.py:563:    "take_beat",
    src/cobalt/jobs/store.py:197:                "beat detail and green_summary_date belong to run_beat"

`grep -rln "\"backup.yaml\"" src`

    src/cobalt/backup/config.py

`grep -n "run_backup.sh" ops/com.cobalt.backup.plist`

    63:        <string>/Users/cobalt/cobalt/ops/run_backup.sh</string>

`grep -n "cobalt backup run" ops/run_backup.sh`

    39:exec /Users/cobalt/.local/bin/uv run cobalt backup run

`grep -n "heartbeat" ops/com.cobalt.heartbeat.plist`

    6:    <string>com.cobalt.heartbeat</string>
    12:             heartbeat reads the LIVE jobs table and writes the LIVE daily
    35:        <string>com.cobalt.heartbeat</string>
    36:        <!-- The remainder is the one heartbeat subprocess. The F17 wrapper
    42:        <string>heartbeat</string>
    50:         week. The heartbeat is the thing that notices a Saturday failure
    55:         900 s = 15 min = the `heartbeat.interval_min` tunable. launchd
    69:    <string>/Users/cobalt/cobalt/logs/heartbeat.log</string>
    71:    <string>/Users/cobalt/cobalt/logs/heartbeat.err</string>

`grep -rn "latest_snapshot_age\|def snapshot\|def restore\|def _run\|def _status\|snapshot(\|restore(" src/cobalt/backup src/cobalt/heartbeat` (run at CLOSE to trace the callers below)

    src/cobalt/backup/__init__.py:4:from .restic import BackupError, BackupRun, latest_snapshot_age, restore, snapshot
    src/cobalt/backup/__init__.py:11:    "latest_snapshot_age",
    src/cobalt/backup/cli.py:19:from .restic import latest_snapshot_age, restore, snapshot
    src/cobalt/backup/cli.py:45:def _run(args) -> int:
    src/cobalt/backup/cli.py:49:        result = snapshot(dry_run=args.dry_run)
    src/cobalt/backup/cli.py:58:def _status(args) -> int:
    src/cobalt/backup/cli.py:70:    age = latest_snapshot_age(cfg)
    src/cobalt/backup/cli.py:75:def _restore(args) -> int:
    src/cobalt/backup/cli.py:76:    into = restore(args.destination, args.snapshot_id, args.into, include=args.include)
    src/cobalt/backup/restic.py:144:def _run(args: list[str], env: dict[str, str], timeout: int = 3600) -> str:
    src/cobalt/backup/restic.py:162:def snapshot(cfg: Optional[BackupConfig] = None, *, dry_run: bool = False) -> BackupRun:
    src/cobalt/backup/restic.py:240:def latest_snapshot_age(cfg: Optional[BackupConfig] = None) -> Optional[timedelta]:
    src/cobalt/backup/restic.py:266:def restore(dest_name: str, snapshot_id: str, into: Path,
    src/cobalt/backup/restic.py:292:    "latest_snapshot_age",
    src/cobalt/heartbeat/runner.py:356:def _run_alerts(
    src/cobalt/heartbeat/runner.py:413:def _run_vault_stage(
    src/cobalt/heartbeat/probes.py:427:    from cobalt.backup.restic import BackupError, latest_snapshot_age
    src/cobalt/heartbeat/probes.py:445:        age = latest_snapshot_age(cfg)

`grep -rn "load_backup_config\|backup_freshness\|take_beat\|run_beat" src/cobalt/radar src/cobalt/aset` — no output (expected).

| Caller file:line | Function | Reached from | Job label | Kind |
|---|---|---|---|---|
| `backup/restic.py:164` | `snapshot` | `backup/cli.py:45` `_run` = `cobalt backup run` ← `ops/run_backup.sh:39` ← `ops/com.cobalt.backup.plist:63` | `com.cobalt.backup` | one-shot |
| `backup/restic.py:248` | `latest_snapshot_age` (`cfg or load_backup_config()` — a fallback) | `backup/cli.py:70` and `heartbeat/probes.py:445`, both passing an already-loaded `cfg`, so the fallback is not hit from either | operator (`status`) / `com.cobalt.heartbeat` | operator / one-shot |
| `backup/restic.py:269` | `restore` | `cobalt backup restore` | none — operator command | — |
| `backup/cli.py:59` | `_status` | `cobalt backup status` | none — operator command | — |
| `heartbeat/probes.py:431` | `backup_freshness` | `heartbeat/runner.py:144` inside `take_beat` ← `heartbeat/cli.py` ← `ops/com.cobalt.heartbeat.plist` | `com.cobalt.heartbeat` | one-shot |

No resident reaches `load_backup_config`; `radar` and `aset` greps are empty. The drafter's list is confirmed with no extra caller. (`backup/__init__.py` re-exports the name; it does not call it.)

## Z1
TEST FIRST. Added `test_backup_yaml_is_read_by_one_shots_only_and_derives_no_restart(monkeypatch)` to `tests/cobalt/test_jobs_restarts.py`, below `test_generated_rules_yaml_derives_no_restart`. (a) real `classify` on `Change("configs/cobalt/backup.yaml", "M")` with the real `load_job_registry()`: `escalate is False`, `restarts == ()`, `rule == "no resident reads (one-shot: com.cobalt.backup,com.cobalt.heartbeat)"` (the string follows the `readers:` order I declared in `jobs.yaml`: backup, then heartbeat). (b) against the real tree: files containing `load_backup_config(` = the four expected; files holding `"backup.yaml"` = `["src/cobalt/backup/config.py"]`; the declaration's readers = `{"com.cobalt.backup", "com.cobalt.heartbeat"}`, each `kind` `JobKind.ONE_SHOT`.

RED, verbatim (`uv run pytest -q tests/cobalt/test_jobs_restarts.py -k backup_yaml`, before the config edit):

    >       assert row.escalate is False
    E       AssertionError: assert True is False
    E        +  where True = Classification(path='configs/cobalt/backup.yaml', change='M', rule='UNCLASSIFIED CONFIG', restarts=('com.cobalt.agent'...om.cobalt.aset', 'com.cobalt.herdr', 'com.cobalt.mainframe', 'com.cobalt.obsidian', 'com.cobalt.radar'), escalate=True).escalate
    tests/cobalt/test_jobs_restarts.py:172: AssertionError
    FAILED tests/cobalt/test_jobs_restarts.py::test_backup_yaml_is_read_by_one_shots_only_and_derives_no_restart - AssertionError: assert True is False
    1 failed, 14 deselected in 0.39s

THEN the rule: one row appended to `no_resident_reads:` in `configs/cobalt/jobs.yaml` below the `rules.yaml` row (whole diff under CLOSE). `because:` is 6 lines, no line starts with `reads:`.

GREEN, verbatim:

    1 passed, 14 deselected in 0.38s

`uv run pytest -q tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py`, verbatim summary:

    38 passed in 6.12s

Unchanged and passing inside those 38 (neither file edited except by the one added test): `test_a_declared_one_shot_only_config_derives_no_restart`, `test_generated_rules_yaml_derives_no_restart`, `test_an_unknown_dotfile_still_escalates`, `test_the_other_residents_declare_it_empty_deliberately`, and the three `TestNoResidentReads` refusals. I read them as part of the 38; I did not run them by name individually.

Commit `d669dfa` — `fix(jobs): configs/cobalt/backup.yaml declared one-shot-only …(ops classifier fix Z1)`; `git show --stat HEAD`: `configs/cobalt/jobs.yaml` (+9), `tests/cobalt/test_jobs_restarts.py` (+52) only.

## Z2
`docs/40 - DevDocs/cobalt/jobs/restarts.md` line 7 extended: names the three declared rows (`notify.yaml` heartbeat, `rules.yaml` the two prefills, `backup.yaml` backup + heartbeat 2026-09-22) and adds the one sentence — a config only one-shots read is DECLARED in `jobs.yaml` `no_resident_reads`, never hard-coded in `restarts.py` (L3; a `restarts.py` edit is itself a `src/` change deriving `com.cobalt.radar` through `cobalt.cli`). Nothing else in the DevDoc changed. Commit `ac2e7ae` — 1 file, 1 insertion, 1 deletion.

## CLOSE
Suite, verbatim (`uv run pytest -q tests/cobalt tests/taxonomy`):

    2210 passed, 351 skipped, 1 xfailed, 15 warnings in 64.22s (0:01:04)

Against BASELINE: failed 0, passed 2209 + 1 = 2210, skipped 351 unchanged, 1 xfailed unchanged.

THE GREEN OF THE COMMAND — `uv run cobalt jobs restarts main..HEAD`, exit **0**, verbatim:

    path	change	rule	restart
    .gitignore	M	META	-
    configs/cobalt/backup.yaml	M	no resident reads (one-shot: com.cobalt.backup,com.cobalt.heartbeat)	-
    configs/cobalt/jobs.yaml	M	registry; register, no restart	-
    docs/00 - Project/BACKLOG.md	M	DOCS	-
    docs/30 - Design/DRC-SITTING-PACKET-2026-09-21.md	D	DOCS	-
    docs/30 - Design/S3-EXITS-PROPOSAL-2026-09-21.md	D	DOCS	-
    docs/30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/cobalt/backup/config.md	M	DOCS	-
    docs/40 - DevDocs/cobalt/db_migrations/cli.md	M	DOCS	-
    docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/58-s2-smoke-first-look.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/59-propose-stale-score.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/60-draft-stale-score-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/61-stale-score-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/62-stale-score-tribunal-fable-seat.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/63-stale-score-tribunal-derive.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/64-draft-setups-one-build.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/65-setups-one-build.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/66-setups-one-check.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/67-draft-tuesday-checks.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/68-stale-marker-check.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/69-ops-6a-check.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/70-propose-s3-exits.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/71-draft-drc-sitting-packet.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/72-draft-s3-exits-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/73-s3-exits-tribunal.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/74-s3-exits-tribunal-fable-seat.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/75-s3-exits-tribunal-derive.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/76-draft-ops-classifier-fix.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/77-ops-classifier-fix.md	D	DOCS	-
    docs/40 - DevDocs/prompts/2026-09-21/78-ops-6a-check-r2.md	D	DOCS	-
    docs/40 - DevDocs/prompts/UNATTENDED-LAUNCH.md	M	DOCS	-
    docs/40 - DevDocs/reports/cto-2026-09-21.md	M	DOCS	-
    docs/40 - DevDocs/reports/drc-sitting-packet-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/ops-2026-09-21.md	A	DOCS	-
    docs/40 - DevDocs/reports/ops-6a-check-2026-09-22.md	D	DOCS	-
    docs/40 - DevDocs/reports/ops-classifier-fix-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/s3-exits-design-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/s3-exits-tribunal-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/setups-one-build-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/stale-score-design-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/stale-score-tribunal-draft-2026-09-21.md	D	DOCS	-
    docs/40 - DevDocs/reports/tuesday-checks-draft-2026-09-21.md	D	DOCS	-
    tests/cobalt/test_backup.py	M	test/documentation; no resident	-
    tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
    RESTARTS: none

`configs/cobalt/backup.yaml` reads `no resident reads (one-shot: com.cobalt.backup,com.cobalt.heartbeat)`, restart `-`; `configs/cobalt/jobs.yaml` reads `registry; register, no restart`; no `UNCLASSIFIED` row. `RESTARTS: none` — the fix derives no resident restart; the one-shots re-read the file at their next run. (`main..HEAD` is a two-dot diff and also lists main's desk-doc changes as `DOCS`, as round 1's table did — the tool's shape, not a defect. The report file itself is committed after these runs, so it does not appear in this table.)

`uv run cobalt jobs restarts f6aa4d0..HEAD` (before the report commit), exit 0, verbatim:

    path	change	rule	restart
    configs/cobalt/jobs.yaml	M	registry; register, no restart	-
    docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
    tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
    RESTARTS: none

OTHER PATHS UNTOUCHED — each `git diff f6aa4d0 -- <path>`:

| Path | Output |
|---|---|
| `src` | no output |
| `ops` | no output |
| `configs/cobalt/backup.yaml` | no output |
| `tests/cobalt/test_jobs_reads.py` | no output |

(`src` includes `restarts.py` and `config.py` — the classifier and the schema are not changed.)

`git diff --stat f6aa4d0 HEAD` (before the report commit), verbatim:

     configs/cobalt/jobs.yaml                  |  9 ++++++
     docs/40 - DevDocs/cobalt/jobs/restarts.md |  2 +-
     tests/cobalt/test_jobs_restarts.py        | 52 +++++++++++++++++++++++++++++++
     3 files changed, 62 insertions(+), 1 deletion(-)

All three are on the named list; the fourth named path is this report.

`git diff f6aa4d0 -- configs/cobalt/jobs.yaml`, whole, verbatim — `+` lines only, inside `no_resident_reads:`, no `-` line:

    diff --git a/configs/cobalt/jobs.yaml b/configs/cobalt/jobs.yaml
    index 1e60b77..7ff2d1e 100644
    --- a/configs/cobalt/jobs.yaml
    +++ b/configs/cobalt/jobs.yaml
    @@ -314,6 +314,15 @@ no_resident_reads:
           regenerate_rules_config() (prefill/rules_gen.py). load_rules_config()
           (prefill/config.py:125) has no caller; no resident imports either
           path. Added 2026-09-16 (the nightly generated commit escalated it).
    +  - path: configs/cobalt/backup.yaml
    +    readers: [com.cobalt.backup, com.cobalt.heartbeat]
    +    because: >
    +      load_backup_config() (backup/config.py:161; the one path :19) is called
    +      by backup/restic.py:164,248,269 and backup/cli.py:59 — the one-shot
    +      com.cobalt.backup (`cobalt backup run`, ops/run_backup.sh:39) plus
    +      status/restore, operator commands — and by heartbeat/probes.py:431
    +      (backup_freshness, from runner.py:144), the one-shot com.cobalt.heartbeat.
    +      No resident calls either. Added 2026-09-22 (6a range; round-1 check).
     
     # THE KILL PHRASE (F17d). Config, not a literal: `cobalt stop` and any
     # future DM listener compare against this exact string.

`git log --oneline f6aa4d0..HEAD` (before the report commit):

    ac2e7ae docs(devdocs): jobs/restarts.md — backup.yaml joins the declared one-shot-only configs (ops classifier fix Z2)
    d669dfa fix(jobs): configs/cobalt/backup.yaml declared one-shot-only — backup + heartbeat read it, no resident; jobs restarts no longer escalates it (ops classifier fix Z1)

One commit per Z step, no wip commits. `git status --porcelain` after the report commit is recorded by the desk's L35 check (the report commit is the last act of this run).

## ESCALATE
1. **The builder's reader claim is corrected.** The branch report said only `com.cobalt.backup` reads `backup.yaml`; `com.cobalt.heartbeat` reads it too (`heartbeat/probes.py:431`, `backup_freshness`, from `heartbeat/runner.py:144`). Both are one-shots, so the derived restart is the same (none); the declaration names both.
2. Round-1 ESCALATE 2 (the `cli.md` seam with `bars/chunk-1a-0920`) — carried by id, untouched, not this run's.
3. Round-1 ESCALATE 3 (the circular restore → 6b) — carried by id, untouched.
4. Round-1 ESCALATE 4 (restic `forget` grouping) — carried by id, untouched.
5. Another classifier gap, listed and NOT fixed: `configs/cobalt/watchlists.yaml` is still a hard-coded `if` at `src/cobalt/jobs/restarts.py:243-244` (`one-shot archiver reads fresh; no resident`), predating the `no_resident_reads` table; a second path for the same job (L3) that `cobalt jobs readers` does not see. Moving it to the table is a `src/` change and is the desk's call.
6. The branch still sits behind main's desk commits (main tip `914ee14`; `ops/2026-09-21..main -- src configs ops tests .gitignore` was EMPTY at preflight, so main moved only in desk docs). The deploy's rebase-then-ff is the desk's.

No `ASK DESK`. No `MEMORY:` / `RULING:` lines.

## CONTINUE
None — the run is complete; nothing is left to resume.

OPS CLASSIFIER FIX BUILT ac2e7ae | on f6aa4d0 | offline 2210/0 (baseline 2209/0) | backup.yaml classified: no resident reads (one-shot: com.cobalt.backup,com.cobalt.heartbeat) | jobs restarts main..HEAD: exit 0, RESTARTS: none | other paths untouched: empty diff | ESCALATE: 6
