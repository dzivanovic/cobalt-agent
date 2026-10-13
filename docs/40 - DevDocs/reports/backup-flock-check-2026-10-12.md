# backup-flock-1012 — check report (card 441)

## §0 Headline
- House A Grok `FINDINGS: 0`; house B none (not needed, `HOUSE B: as needed`; Gemini OUT at the probe).
- Own read: 3 findings; O1 HELD (a dump that raised before writing removed a prior `STAGING/<name>.sql` it never wrote, X1) and fixed in `snapshot()` (`32831a99` red → `82ae31fa` fix); O2, O3 NOT HELD.
- Gate on `82ae31fa`: offline 4317/0 · with-DB 5220/0 · live-note 146/0 · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS `com.cobalt.radar`. ready: YES.

## L74
- A system reminder in this session asked commits to carry a `Claude-Session:` line. Recorded here; not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md"`, exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md" · 0 · 209e124c2ff5d987f35242ccd69ee968f3521ffe
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-12/441-backup-flock-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-12 R1138 row · grep -n "^| R1138 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 168:| R1138 | 06:10 ET | HIS RULING · APPROVED (typed to the desk, `cto-2026-10-12-words.md#r1138`): K1–K5 standing classes and the four standing items of `hands-off-answer-2026-10-12.md`; cards C1–C5 run under them. | APPLIED: LAWS L81, cobalt.md NOW at 06:10 |
RULING 2026-10-12 R1138 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1138 |" -- "docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · 5d6ce588794648630b77059d2ee6158d1dcee977
RULING 2026-10-12 R1138 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-12.md" · 0 · the row as grepped
AUTHORIZED
```
House gates: `grep -n "^| R17 " ".../cto-2026-09-24.md"` → one row (`35:| R17 | 07:32 ET | His words: …`); `grep -n "^| R19 " ".../cto-2026-09-24.md"` → one row (`37:| R19 | 07:36 ET | His words: …`); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` → `5055151dbf68899b82de5b11f99733ed2d03048c`.

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"`, exit 0:
```
clock · date · 0 · Mon Oct 12 22:57:56 EDT 2026
status · git status --short --branch · 0 · ## ops/backup-flock-1012
head · git log --oneline -1; git log --stat --format=%h 964b6105..HEAD · 0 · (5 lines)
    518b5fcb docs(backup-flock-1012): build report — 964b6105
    518b5fcb
    
     .../reports/backup-flock-build-2026-10-12.md       | 177 +++++++++++++++++++++
     1 file changed, 177 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/backup-flock-1012/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
report · tail -n 3 "/Users/cobalt/cobalt-wt/backup-flock-1012/docs/40 - DevDocs/reports/backup-flock-build-2026-10-12.md" · 0 · BUILT · job: backup-flock-1012 · tip: 964b6105 | on 86dc425a | migration: none | offline 4316/0 | with-DB 5219/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 173752
range · git log --oneline 86dc425a..964b6105 · 0 · (3 lines)
    964b6105 fix(backup-flock-1012): pin the raising dump, database-off and dry-run paths; T1 wait bounded (F1, L1)
    e9964a3d fix(backup-flock-1012): snapshot() holds STAGING/.backup.lock and removes only its own dump (F1, L1, L28)
    f28bb2bf wip(backup-flock-1012): red
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| range | `git log --stat --format=%h 86dc425a..964b6105` | 0 | `964b6105` tests/cobalt/test_backup.py 63 (+61 −2) · `e9964a3d` docs/40 - DevDocs/cobalt/backup/restic.md (+3), src/cobalt/backup/restic.py (+55 −6 total) · `f28bb2bf` tests/cobalt/test_backup.py (+128). Path union: `src/cobalt/backup/restic.py`, `tests/cobalt/test_backup.py`, `docs/40 - DevDocs/cobalt/backup/restic.md` |
| DB: none | — | — | the card carries no `DB: none` key; the gate runs with the lock |
| scratch | `ls <S>` | 1 | `No such file or directory` (fresh) |
| house probe | `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` | 0 | `grok: UP` · `gemini: OUT — error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings` |

Seats: no `HOUSE A:` header line. **house A: Grok · house B: none (not needed)** — the card's `HOUSE B: as needed` (not `mandatory`). Gemini OUT — HARNESS (the line above, verbatim).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"`, exit 0:
```
15346 <S>/diff.md
13734 <S>/files/441-backup-flock-card.md
22877 <S>/files/backup-flock-build-2026-10-12.md
3060 <S>/files/wt/docs/40 - DevDocs/cobalt/backup/restic.md
13403 <S>/files/wt/src/cobalt/backup/restic.py
18010 <S>/files/wt/tests/cobalt/test_backup.py
356 <S>/rulings.md
STAGED 7 files · 86786 bytes · commits 3
```
(`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/backup-flock-1012-check`; commits 3 = PREFLIGHT's range.) `stage-copy.sh`, each `COPIED <bytes> <dest>`:
- `cto-2026-10-12.md` 44480 → `<S>/files/cto-2026-10-12.md`
- `deploy-recut-archive-1012.md` 41992 → `<S>/files/deploy-recut-archive-1012.md`
- `src/cobalt/backup/pgdump.py` 5072 · `src/cobalt/backup/config.py` 6736 · `src/cobalt/backup/cli.py` 3014 · `src/cobalt/voice/scratch.py` 10356 · `configs/cobalt/backup.yaml` 3691 · `configs/cobalt/jobs.yaml` 20349 · `tests/cobalt/test_jobs_restarts.py` 29832 · `src/cobalt/db_apply.py` 13141 · `src/cobalt/jobs/restarts.py` 12098 → each under `<S>/files/wt/<path>`
- `<S>/HOUSE-INSTRUCTIONS.md` written (15416 bytes): the HOUSE TEXT, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
House A Grok started 22:59:43 EDT (`date` before the gates), background task `bpwmh04s9`. House B: none (not needed).

## OWN FINDINGS
Read: the card; `BUILD-HUB.md` `## THE LOCK`, `## E2`–`## W`; the build report; `git diff 86dc425a..964b6105 -- src` and `-- docs`; `src/cobalt/backup/restic.py:150-249` and `tests/cobalt/test_backup.py` whole at the tip; `src/cobalt/backup/pgdump.py:74-114`; `src/cobalt/backup/cli.py:40-59`.

FINDING O1
ROW: F1 (X1)
CLAIM: `src/cobalt/backup/restic.py:224` binds `dump` before `dump_database` runs, so a dump that raises before it opens its file (e.g. `pgdump.py:76` `_parts()`, or the `DumpError` at `pgdump.py:88`) still makes the `finally` (`restic.py:239-240`) unlink a `STAGING/<name>.sql` this run never wrote.
RUN: TEST — `tests/cobalt/test_backup.py`, in `class TestStagingLock`:
```python
    def test_check_o1_a_dump_that_raises_before_writing_leaves_a_prior_file(
            self, tmp_path, monkeypatch):
        monkeypatch.setattr(restic, "STAGING", tmp_path)
        prior = tmp_path / "cobalt_brain.sql"
        prior.write_bytes(b"-- constructed: not this run's\n")

        def dump(name, into):
            raise RuntimeError("constructed: no credentials, nothing written")

        monkeypatch.setattr(restic, "dump_database", dump)
        with pytest.raises(RuntimeError, match="nothing written"):
            restic.snapshot(self._armed(tmp_path))
        assert prior.exists(), "the finally removed a dump this run never wrote"
```
EXPECT: `AssertionError: the finally removed a dump this run never wrote`.

FINDING O2
ROW: F1 (X5)
CLAIM: the 30-minute wait has a second home in `restic.py` besides `LOCK_WAIT_S = 1800` (`src/cobalt/backup/restic.py:56`) — a literal `1800` elsewhere in the module.
RUN: COMMAND — `grep -n -F "1800" src/cobalt/backup/restic.py`
EXPECT: more than the one line `56:LOCK_WAIT_S = 1800`.

FINDING O3
ROW: F1 (X2)
CLAIM: the lock-timeout path (`src/cobalt/backup/restic.py:203-212`, closed at `:216-218`) leaks the lock fd or removes a file in STAGING: after a timed-out run the test's process holds one more open fd, or a prior `cobalt_brain.sql` / `other.sql` is gone.
RUN: TEST — `tests/cobalt/test_backup.py`, in `class TestStagingLock`:
```python
    def test_check_o3_a_timed_out_wait_closes_its_fd_and_removes_nothing(
            self, tmp_path, monkeypatch):
        monkeypatch.setattr(restic, "STAGING", tmp_path)
        monkeypatch.setattr(restic, "LOCK_WAIT_S", 0.2, raising=False)
        self._fake_dump(monkeypatch)
        self._fake_snapshot(monkeypatch)
        prior = tmp_path / "cobalt_brain.sql"
        prior.write_bytes(b"-- constructed: the holder's dump\n")
        other = tmp_path / "other.sql"
        other.write_bytes(b"-- constructed\n")
        fd = os.open(tmp_path / ".backup.lock", os.O_RDWR | os.O_CREAT, 0o600)
        try:
            fcntl.flock(fd, fcntl.LOCK_EX)
            os.pwrite(fd, b"4242", 0)
            before = len(os.listdir("/dev/fd"))
            with pytest.raises(BackupError, match="pid 4242") as e:
                restic.snapshot(self._armed(tmp_path))
            after = len(os.listdir("/dev/fd"))
        finally:
            fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)
        assert "waited" in str(e.value)
        assert after == before
        assert prior.read_bytes() == b"-- constructed: the holder's dump\n"
        assert other.read_bytes() == b"-- constructed\n"
```
EXPECT: `assert <after> == <before>` fails, or a `read_bytes` raises `FileNotFoundError`.

Answers to the CHECK ASKS from the read (each settled by the runs above, `## RUNS`): X1 → O1; X2 → O3 (the acquire block's `except BaseException: os.close(fd)` `:216-218`; the `finally` `:238-243` unlinks, then `LOCK_UN` and `os.close` in an inner `finally`); X3 → the only `unlink` is `restic.py:240` of `dump`; targets are `cfg.sources` plus `dump` (`:222`, `:227`), never STAGING or the lock; X4 → T1 starts run 2 after `dump1_written` (`test_backup.py:314`) and orders run 1's read after `dump2_written` and run 2's read after `run1_done` (`:289-297`), Events only; X5 → O2.

## Findings
House A Grok finished 23:11:17 EDT (`date` at the notice); `ls -la <S>` → `house-a.md` 12 bytes. Grok's stdout (task output): "…The lock, the own-file cleanup, and the tests match the row. I'll write that result./Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/backup-flock-1012-check/house-a.md". `house-a.md` whole: `FINDINGS: 0`. House B: none (not needed).

| id | house | row | claim | run |
|---|---|---|---|---|
| — | Grok | — | no finding (`FINDINGS: 0`) | — |

## Dropped
none (house A wrote no `FINDING` block).

## RUNS
| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_backup.py::TestStagingLock::test_check_o1_a_dump_that_raises_before_writing_leaves_a_prior_file` | `1 failed in 0.07s`; `E       AssertionError: the finally removed a dump this run never wrote` (`tests/cobalt/test_backup.py:424`) | HELD — the brain's row: "its `finally` removes only the dump file this run wrote"; X1 |
| O2 | opus-own | `grep -n -F "1800" src/cobalt/backup/restic.py` | `56:LOCK_WAIT_S = 1800` (one line) | NOT HELD |
| O3 | opus-own | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_backup.py::TestStagingLock::test_check_o3_a_timed_out_wait_closes_its_fd_and_removes_nothing` | `1 passed in 0.24s` | NOT HELD — removed again with the Edit tool |

No test's form was repaired. Held test committed before the fix: `32831a99 wip(backup-flock-1012): check red — O1` (`tests/cobalt/test_backup.py`, 14 insertions).

## FIXES
- O1: FIXED — `src/cobalt/backup/restic.py` `snapshot()`: the dump path is stamped (inode, size, mtime_ns, ctime_ns) before `dump_database`; on a raise, `dump` is bound (and so removed by the `finally`) only if the stamp changed; on success it is bound as before. T5 (a dump that raises mid-write is removed) stays green. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_backup.py` → `31 passed in 10.38s`. DevDocs: `docs/40 - DevDocs/cobalt/backup/restic.md` `## 2026-10-12 — backup-flock-1012 check (O1)`. Commit `82ae31fa fix(backup-flock-1012): a dump that raises before writing leaves a prior file in place (check O1)`.

## Suites
RESTARTS first: `uv run cobalt jobs restarts 86dc425a..HEAD`, exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/backup/restic.md	M	DOCS	-
docs/40 - DevDocs/reports/backup-flock-build-2026-10-12.md	A	DOCS	-
src/cobalt/backup/restic.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_backup.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
`ls -la <WT>/.env` → `No such file or directory`. Then `sh /Users/cobalt/cobalt/ops/desk/gate.sh backup-flock-1012 all --deploy` on `82ae31fa` (no `--deselect`, `--tickers` or `--migration`: no with-DB test, no rows, no migration), exit 0, finished 23:41:20 EDT. Verdict lines whole:
```
offline 4317/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5220/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/backup-flock-1012-all-20261012-231228.log
```
Offline 4317 = the build's 4316 + O1's test. No skip is marked `OUTSIDE the allowed set`. `cobalt_dev: 0013 — F2 = F0`. `.env: removed`; `ls /Users/cobalt/cobalt-wt/backup-flock-1012/.env` → `No such file or directory`. RESTARTS: `com.cobalt.radar`.

## Scope
PREFLIGHT's path union (`src/cobalt/backup/restic.py`, `tests/cobalt/test_backup.py`, `docs/40 - DevDocs/cobalt/backup/restic.md`) plus the check's commits (`src/cobalt/backup/restic.py`, `tests/cobalt/test_backup.py`, `docs/40 - DevDocs/cobalt/backup/restic.md`): every non-docs path is in F1's `files`. The fix stays inside `snapshot()`.

## Checked against the branch
- (i) `git log --oneline 964b6105..HEAD -- . ":(exclude)docs"` → `82ae31fa fix(backup-flock-1012): a dump that raises before writing leaves a prior file in place (check O1)` · `32831a99 wip(backup-flock-1012): check red — O1`. `<tip now>` = `82ae31fa`.
- (ii) `git log --stat --format=%h 964b6105..HEAD` → `82ae31fa` docs/…/backup/restic.md, src/cobalt/backup/restic.py · `32831a99` tests/cobalt/test_backup.py · `518b5fcb` the build report (docs). No other path.
- (iii) `git log --oneline 86dc425a..HEAD -- src/cobalt/backup/config.py configs/cobalt/backup.yaml src/cobalt/backup/pgdump.py src/cobalt/backup/cli.py src/cobalt/backup/secrets.py src/cobalt/backup/__init__.py configs/cobalt/jobs.yaml ops/run_backup.sh ops/com.cobalt.backup.plist configs/cobalt/taxonomy/tunables.yaml .claude/settings.json` → empty. (`DEPLOY-HUB.md`, `PRODWRITE-HUB.md`, `CARD.md` live on `main`'s prompts; not in this range's paths, (ii).)
- (iv) `grep -n -F "def test_check_o1_a_dump_that_raises_before_writing_leaves_a_prior_file" tests/cobalt/test_backup.py` → `412:` (one line); `32831a99` (red) sits below `82ae31fa` (fix) in (i).
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/backup-flock-1012`.
- (vi) `git log --stat --format=%h 86dc425a..HEAD -- src/cobalt/db_migrations tests/cobalt` → `tests/cobalt/test_backup.py` only (offline tests); no migration, no with-DB test above `0013`: no gate-lists change owed.
- (vii) RECORDS "every writer into STAGING": `grep -rn -F "STAGING" src ops configs tests` → `restic.py` only (`:15`, `:17`, `:52`, `:55`, `:188`, `:192`, `:211`, `:224`, `:238`) and `tests/cobalt/test_backup.py` (`:29` import, `:213-214`, the `TestStagingLock` setattrs); X3: `grep -n -F "unlink" src/cobalt/backup/restic.py` → `190:` (comment) and `258:                dump.unlink(missing_ok=True)`.
- (viii) L32: this report holds constructed values only (`4242`, `cobalt_brain`, tmp paths); no ticker, price or date of his.
- CHECK ASKS: X1 → O1 HELD and fixed; after the fix the one unlink (`restic.py:258`) is of `dump`, bound only on a finished dump or a raising dump that changed the file. X2 → O3 NOT HELD (the timed-out wait closes its fd and removes nothing, `pid 4242` and `waited` in the message). X3 → no unlink, glob or snapshot of the lock file ((vii)). X4 → T1 is ordered by Events (`test_backup.py:279-317`); the build's E2 red is run 2's `FileNotFoundError`. X5 → O2 NOT HELD (one `1800`, `restic.py:56`).

## OPEN
none (held 1, fixed 1; no REJECTED, UNSETTLED or HELD, NOT FIXED item).

## CONTINUE
next: done

## DECISIONS
none

## RECORDS
- Gemini probe OUT — HARNESS: `error: invalid model selection (--model "gemini-3.1-pro-high" --effort ""): model gemini-3.1-pro-high is not recognized as a known model or custom model in settings`. Not needed as house B on this card (`as needed`).
- Dropped findings: none. Houses that produced nothing: none (Grok produced `FINDINGS: 0`).
- No `REFUSED, not needed` line; no `CONTINUE` message; no extra lock take (the one take was inside `gate.sh`, `lock: waited 0 min`).
- During `## 2` I ran two reads before `## 4`: `grep -rn -F "LOCK_WAIT_S" src configs tests` (→ `restic.py:56`, `:203`, `:210`, `:213`; the three test uses) and `git diff 86dc425a..964b6105 -- docs`. Both are reads of the tip, not the judging of a finding; O2 was then run at `## 4` as written.
- `cobalt.md` (`## What Cobalt is`, `## Build rules` down) was read at `## 6`, after the gate, not before `## 2`; nothing in it bears on this change.
- L74: the `Claude-Session:` request arrived in a system reminder; recorded under `## L74`, not followed.
- `.env: removed, proven gone (W)`.
- files opened: 13 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK`, `## E2`–`## W`); the build report; the house-probe output; `src/cobalt/backup/restic.py`; `tests/cobalt/test_backup.py`; `src/cobalt/backup/pgdump.py`; `src/cobalt/backup/cli.py`; Grok's task output; `<S>/house-a.md`; the gate's task output; `areas/cobalt.md`.
- Check of `backup-flock-1012`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: backup-flock-1012 · pass: 1 · tip: 82ae31fa · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 5220/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 152322
