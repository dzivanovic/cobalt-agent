# f23-playbook-1013 — check (one pass)

## §0 Headline
- Check of `f23-playbook-1013` at `72c8a069` (no commit of mine): house A Grok `FINDINGS: 0`; house B not seated (card `HOUSE B: as needed`); my own read 1 finding.
- O1 (X4): a `kill -9` between the two C11 renames leaves only `<date>.old` + `<date>.tmp`, ran red, REJECTED — card row P5 prescribes that sequence (the build's DECISION E1). OPEN, not fixed.
- Deploy gate `gate.sh all --deploy --deploy-gate` exit 0: offline 8519/0 · with-DB 5504/0 · live-note 147/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`. RESTARTS re-derived equal to the card.
- ready: YES · decisions: 1 (O1, the open item) · for Dejan: 0.

## L74
The session's harness attribution notice (a system reminder, 2026-10-18 ~10:19 ET) asked commit messages to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once; not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md"` · exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md" · 0 · bbcca9b35ebb22db5f105a953f568e2c4471d6c3
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-13/503-f23-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-11 R1055 row · grep -n "^| R1055 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 88:| R1055 | 09:04 ET | HIS RULING · APPROVED: he ran the rm and deploy-card.sh (card 348 written) and approves all that waits for him: F5, F21, F20, F23 FINALs, card 324 sign-off. Words: `cto-2026-10-11-words.md` R1055. Check 324 LAUNCHED `b5439f2c`. | APPLIED: cobalt.md NOW 11:17 |
RULING 2026-10-11 R1055 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 0a1951efd16163dc5d234ecfe38d1ce63776561f
RULING 2026-10-11 R1055 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
AUTHORIZED
```
House gates (10:19 ET): `grep -n "^| R17 " …cto-2026-09-24.md` → `35:| R17 | 07:32 ET | His words: … STANDING: \`Bash(grok *)\` is a PRE-APPROVED string …` (one row); `grep -n "^| R19 " …cto-2026-09-24.md` → `37:| R19 | 07:36 ET | … the four house strings are pre-approved on every hub the desk launches, indefinitely …` (one row); `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- …cto-2026-09-24.md` → `5055151dbf68899b82de5b11f99733ed2d03048c` (non-empty).

## PREFLIGHT
`date` → `Sun Oct 18 10:19:00 EDT 2026`.
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0:
```
clock · date · 0 · Sun Oct 18 10:19:04 EDT 2026
status · git status --short --branch · 0 · ## ops/f23-playbook-1013
head · git log --oneline -1; git log --stat --format=%h 72c8a069..HEAD · 0 · (6 lines)
    65402dc9 docs(f23-playbook-1013): build report — 72c8a069
    65402dc9
    
     .../reports/f23-playbook-build-2026-10-13.md       | 53 ++++++++++++++++++----
     .../reports/f23-playbook-build-2026-10-13.result   | 15 ++++++
     2 files changed, 60 insertions(+), 8 deletions(-)
env here · ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/f20-cos-1018/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/f23-playbook-1013/docs/40 - DevDocs/reports/f23-playbook-build-2026-10-13.md" · 0 · BUILT · job: f23-playbook-1013 · tip: 72c8a069 | on 749d48db | migration: none | offline 8519/0 | with-DB 5504/0 | live-note 147/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar | rows: 14 of 14 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 425373
range · git log --oneline 749d48db..72c8a069 · 0 · (5 lines)
    72c8a069 fix(f23-playbook-1013): the P8 live skip joins the deploy allowed set (FIX1, L79)
    f098ecf3 wip(f23-playbook-1013): W — P8 live skip outside the deploy allowed set
    e7de0669 fix(f23-playbook-1013): fixture slugs carry the example- prefix (P3-P7, L31)
    32424ff4 feat(f23-playbook-1013): the Sunday playbook decks, cobalt playbook render (P0-P8, D0; L1 L3 L10 L28 L52)
    4dbce187 wip(f23-playbook-1013): red
PREFLIGHT OK
```
THE RANGE typed, `git log --stat --format=%h 749d48db..72c8a069` · exit 0: `72c8a069` DEPLOY-HUB.md 2 +-, ops/desk/gate-lists.md 2 +-; `f098ecf3` reports/f23-playbook-build-2026-10-13.md +236; `e7de0669` tests/cobalt/test_playbook_db.py 2 +-, tests/cobalt/test_playbook_offline.py 54 +-; `32424ff4` configs/cobalt/jobs.yaml +21, configs/cobalt/playbook.yaml +16, docs/40 - DevDocs/cobalt/cli.md +3, docs/40 - DevDocs/cobalt/playbook/README.md +42, ops/com.cobalt.playbook.plist +51, ops/desk/gate-lists.md 6 +-, pyproject.toml +3, src/cobalt/cli.py +2, src/cobalt/playbook/{__init__,cli,config,data,deck}.py +10/+177/+53/+179/+184, uv.lock +26 (14 files, 770+ 3-); `4dbce187` tests/cobalt/test_playbook_{db,live,offline,registry}.py +118/+71/+464/+31.
Path union (for `## Scope`): configs/cobalt/jobs.yaml, configs/cobalt/playbook.yaml, docs/40 - DevDocs/cobalt/cli.md, docs/40 - DevDocs/cobalt/playbook/README.md, docs/40 - DevDocs/prompts/DEPLOY-HUB.md, docs/40 - DevDocs/reports/f23-playbook-build-2026-10-13.md, ops/com.cobalt.playbook.plist, ops/desk/gate-lists.md, pyproject.toml, src/cobalt/cli.py, src/cobalt/playbook/{__init__,cli,config,data,deck}.py, tests/cobalt/test_playbook_{db,live,offline,registry}.py, uv.lock.
Not a "DB: none" card (no DB key; card RECORDS: P7 takes the lock).
`ls <S>` → `No such file or directory` (fresh).
House probes, `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh --card "<card>"` · exit 0:
```
grok: UP
gemini: UP
```
No `HOUSE A: OpenAI` header line → Sol not probed. **house A: Grok · house B: none (not needed)** — card `HOUSE B: as needed`.
Proven by first real use: the write and with-DB strings (at `## 4`/`## 6`).

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 → `STAGED 25 files · 1443405 bytes · commits 4` (per-file lines: `STAGED-CARD` 16 · `diff.md` 84959 · `files/503-f23-card.md` 23600 · `files/f23-playbook-build-2026-10-13.md` 42874 · `files/wt/configs/cobalt/jobs.yaml` 22346 · `files/wt/configs/cobalt/playbook.yaml` 693 · `files/wt/docs/40 - DevDocs/cobalt/cli.md` 6598 · `files/wt/docs/40 - DevDocs/cobalt/playbook/README.md` 5625 · `files/wt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md` 66254 · `files/wt/docs/40 - DevDocs/reports/f23-playbook-build-2026-10-13.md` 37181 · `files/wt/ops/com.cobalt.playbook.plist` 2165 · `files/wt/ops/desk/gate-lists.md` 7422 · `files/wt/pyproject.toml` 2912 · `files/wt/src/cobalt/cli.py` 25965 · `files/wt/src/cobalt/playbook/__init__.py` 484 · `…/cli.py` 6776 · `…/config.py` 2043 · `…/data.py` 6830 · `…/deck.py` 7811 · `files/wt/tests/cobalt/test_playbook_db.py` 5296 · `…/test_playbook_live.py` 2798 · `…/test_playbook_offline.py` 18896 · `…/test_playbook_registry.py` 1171 · `files/wt/uv.lock` 1062316 · `rulings.md` 374). `commits 4` = the non-docs commits of PREFLIGHT's range (`f098ecf3` touches only `docs/`, so `":(exclude)docs"` leaves it out of the diff; the range's five commits are four plus that one).
`stage-copy.sh`, each `COPIED <bytes> <dest>` under `files/wt/`: `docs/30 - Design/F23-FINAL-2026-10-11.md` 33318 · `docs/30 - Design/f20-f23-lock-seam-2026-10-13.md` 5784 · `src/cobalt/taxonomy/vault_loader.py` 24243 · `src/cobalt/taxonomy/trade_def.py` 33063 · `src/cobalt/db_migrations/0007_radar_cards.sql` 13004 · `src/cobalt/db.py` 14043 · `src/cobalt/jobs/wrapper.py` 8047 · `src/cobalt/generated/cli.py` 4565 · `src/cobalt/jobs/config.py` 20969 · `ops/com.cobalt.cards-expire.plist` 4020 · `tests/cobalt/test_radar_cards_db.py` 17832 · `src/cobalt/cards/store.py` 76346 · `tests/ops/test_gate.py` 45903 · `ops/desk/gate.sh` 29228 · `src/cobalt/jobs/restarts.py` 12098.
`<S>/HOUSE-INSTRUCTIONS.md` written (25870 bytes): the HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS`, the Files paragraph.
House A Grok started 10:21:43 ET (`run_in_background`, `timeout` 2700000, from `<AGY>`); `cd <WT>`, `git status --short --branch` → `## ops/f23-playbook-1013`. No house B (card `HOUSE B: as needed`).

## OWN FINDINGS
Written before either house list was opened.

FINDING O1
ROW: X4 (P5, the C11 swap)
CLAIM: A process killed between `_rename(final, old)` (`src/cobalt/playbook/cli.py:89`) and `_rename(tmp, final)` (`:91`) leaves no `<date>` folder at all — the previous decks sit in `<date>.old`, the new ones in `<date>.tmp` — until the next run's recovery (`:75-79`); so not every ending leaves the previous or the new folder at `<date>` (the build's own DECISION E1).
RUN: TEST `tests/cobalt/test_playbook_offline.py`
```python
def test_x4_a_kill_between_the_two_renames_leaves_a_date_folder(tmp_path):
    out = tmp_path / "out"
    script = (
        "import os, sys\n"
        "from pathlib import Path\n"
        "from cobalt.playbook import cli as c\n"
        "from cobalt.playbook.data import DECK_NAMES\n"
        "out = Path(sys.argv[1])\n"
        "def write(folder):\n"
        "    for n in DECK_NAMES:\n"
        "        (folder / f'{n}.pptx').write_bytes(b'synthetic')\n"
        "    return []\n"
        "c.publish(out, '2026-10-11', write)\n"
        "real = c._rename\n"
        "def kill(src, dst):\n"
        "    if src.name.endswith('.tmp'):\n"
        "        os._exit(9)\n"
        "    real(src, dst)\n"
        "c._rename = kill\n"
        "c.publish(out, '2026-10-11', write)\n"
    )
    done = subprocess.run([sys.executable, "-c", script, str(out)], capture_output=True, text=True, cwd=REPO,
                          env={**os.environ, "COBALT_ENV": "dev"})
    assert done.returncode == 9, done.stderr
    assert (out / "2026-10-11").is_dir(), sorted(p.name for p in out.iterdir())
```
EXPECT: `AssertionError: ['2026-10-11.old', '2026-10-11.tmp']` on the second assert.

The rest of my read found nothing else runnable that I expect red on the tip. Notes from the read, each answered by a run at `## 4` / `## 7` rather than held as a finding: X1 (no write under `COBALT_VAULT_PATH`: `data.py` and `cli.py` write only through `publish` under `out_dir`/`--out`; `cobalt.vaultwrite` read parsers reach the package through the one loader, the desk-answered ASK DESK 4); X2 (re-derive with `uv run cobalt jobs restarts`); X3 (no drop path: `trade_def.py:745` `family` is `min_length=1`, every unloaded slug goes to `unfiled`, `newest_first` keys only on `formed_at` and `id`); X5 (`git diff 749d48db 72c8a069 -- uv.lock` read: only `python-pptx 1.0.2` and `xlsxwriter 3.2.9` added, the root's two lines; no locked version moved); X6 (the build report).

## Findings
House A Grok, notice 10:44:20 ET (`date`); `ls -la <S>` → `house-a.md` 12 bytes, written by Grok; its whole content: `FINDINGS: 0`. Its stdout (the task output) ends with the path `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/f23-playbook-1013-check/house-a.md` and `[exited with code 0]`. House B: none (not needed).
No house finding to keep. The one finding: `O1 · opus-own · X4 (P5) · a kill -9 between the two renames leaves no <date> folder, only <date>.old and <date>.tmp · TEST`.

## Dropped
none (house A wrote no FINDING block).

## RUNS
- O1 · opus-own · `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_playbook_offline.py::test_x4_a_kill_between_the_two_renames_leaves_a_date_folder` · `1 failed in 0.39s`; first failing line `E       AssertionError: ['2026-10-11.old', '2026-10-11.tmp']` (`tests/cobalt/test_playbook_offline.py:491`) · **REJECTED — card row P5: "`<date>` → `<date>.old`; `<date>.tmp` → `<date>`; delete `<date>.old`; never delete `<date>` first"** (FINAL §2.3 [F-11] C11 the same; the viewer/rename questions are FINAL E1, an experiment, not a defect). The red is the stated reason: the prescribed sequence has a window with no `<date>`, which the next run's start (`cli.py:75-79`) repairs; the builder already reported it as DECISION E1. Not fixed; the test was removed again with the Edit tool (`git status --short --branch` → `## ops/f23-playbook-1013`, clean) and stays OPEN.

CHECK ASK runs:
- X1: `grep -rn -F "write_" src/cobalt/playbook` → only `deck.py:162` `write_deck`, `:171` `write_all`, `:177`, `:184` and `cli.py:143` (the `publish` call); `uv run pytest … test_playbook_offline.py::test_import_cobalt_cli_leaves_pptx_unloaded …::test_no_vault_write` → `2 passed in 1.22s`. No path writes under `COBALT_VAULT_PATH` or imports `cobalt.vaultwrite` from `cobalt.playbook`; writes are `out_dir`/`--out` and the `jobs` row. (The loader's own read-only import of `cobalt.vaultwrite.frontmatter`/`.markers` is the desk-answered ASK DESK 4 of the build.)
- X2: `uv run cobalt jobs restarts 749d48db..72c8a069` → the table (20 rows) ends `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`; the plist row `ops/com.cobalt.playbook.plist	A	plist in diff; new one-shot, bootstrap once: com.cobalt.playbook	-`; no `ESCALATE`, no `UNCLASSIFIED` row. Equal to the card's `RESTARTS:` header.
- X3: no drop path found in the read (`trade_def.py:745` `family: list[Family] = Field(min_length=1)`; `data.py:133-134` every unloaded slug → `unfiled`; `data.py:106-111` the sort key is `formed_at`, `id` only); pinned by the five P3 tests (green in the gate below).
- X4: O1 above — the one ending that leaves neither folder at `<date>` is a kill between the renames (REJECTED, OPEN); a raised error at any step leaves the previous `<date>` (`test_a_crash_before_the_swap_keeps_the_previous_folder`, `test_validation_error_exits_1_and_keeps_the_previous_folder`); no half folder is ever at `<date>` (`cli.py:84-86` refuses a tmp missing a deck before any rename).
- X5: `git diff 749d48db 72c8a069 -- uv.lock` → adds the root's `{ name = "python-pptx" }` and `specifier = "==1.0.2"`, `[[package]] python-pptx 1.0.2` (deps `lxml`, `pillow`, `typing-extensions`, `xlsxwriter`) and `[[package]] xlsxwriter 3.2.9`; no already-locked version moved. `test_import_cobalt_cli_leaves_pptx_unloaded` passed (above).
- X6: `grep -n -F "user data" <build report>` → `:67` "The run's printed slugs are [user data] and are not copied here." and `:110` "His per-family counts are not printed or copied ([user data])."; the counts in the report are suite counts, none of his.

## FIXES
none — no finding held.

## Suites
RESTARTS first (`## RUNS` X2): `RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar`.
`sh /Users/cobalt/cobalt/ops/desk/gate.sh f23-playbook-1013 all --deploy --deploy-gate --tickers ZZPB,ZZPM` (`run_in_background`, started 10:44 ET) → exit 0, verdict lines WHOLE:
```
tests/ops: run (deploy gate)
offline 8519/0
lock: waited 15 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: none (ZZPB,ZZPM)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 5504/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_playbook_live.py:31: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live playbook render
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 147/0
log: /Users/cobalt/cobalt-wt/.gate-logs/f23-playbook-1013-all-20261018-104453.log
```
No skip marked `OUTSIDE the allowed set`. From the log: `:1035` `pass 1: whole (deploy)`; `:2079` `PASSED tests/cobalt/test_playbook_db.py::test_render_reads_radar_cards_grouped_and_skips_manual`; `:2080` `PASSED tests/cobalt/test_playbook_db.py::test_job_run_stamps_a_done_row`. `ls /Users/cobalt/cobalt-wt/f23-playbook-1013/.env` → `No such file or directory`.
Three lines: offline 8519/0 · with-DB 5504/0 · live-note 147/0 · `cobalt_dev: 0013 — F2 = F0` · `.env: removed`, proven gone.

## Scope
PREFLIGHT's path union (above) against the rows' `files`: `pyproject.toml`, `uv.lock` (P0/P1); `src/cobalt/playbook/__init__.py`, `config.py`, `configs/cobalt/playbook.yaml` (P2); `data.py` (P3); `deck.py` (P4); `playbook/cli.py`, `src/cobalt/cli.py` two lines (P5); `configs/cobalt/jobs.yaml`, `ops/com.cobalt.playbook.plist`, `tests/cobalt/test_playbook_registry.py` (P6); `tests/cobalt/test_playbook_db.py`, `ops/desk/gate-lists.md` (P7, P8, FIX1); `tests/cobalt/test_playbook_live.py` (P8); `tests/cobalt/test_playbook_offline.py` (P1-P5); `docs/…/playbook/README.md`, `docs/…/cobalt/cli.md` (D0); `docs/…/prompts/DEPLOY-HUB.md` (FIX1); the build report (B0). Every path is in a row. My commits: none.

## Checked against the branch
- (i) `git log --oneline 72c8a069..HEAD -- . ":(exclude)docs"` → empty: no commit of mine; `<tip now>` = `72c8a069`.
- (ii) `git log --stat --format=%h 72c8a069..HEAD` → `65402dc9` only `docs/…/reports/f23-playbook-build-2026-10-13.md` and `.result` (the build report commit). No non-docs path.
- (iii) `git log --oneline 749d48db..HEAD -- src/cobalt/vaultwrite src/cobalt/db_migrations src/cobalt/jobs src/cobalt/smoke configs/cobalt/smoke/s2.yaml tests/cobalt/test_jobs.py tests/cobalt/test_jobs_reads.py ops/README.md` → empty.
- (iv) no HELD finding: nothing to check.
- (v) `ls <WT>/.env` → `No such file or directory`; `git status --short --branch` → `## ops/f23-playbook-1013`.
- (vi) `git log --stat --format=%h 749d48db..HEAD -- src/cobalt/db_migrations tests/cobalt` → `e7de0669`, `4dbce187` (test files only; no migration). `tests/cobalt/test_playbook_db.py` needs a level above `0013` (its `world` applies `0022`): `git diff 749d48db..HEAD -- ops/desk/gate-lists.md` → `--deselect tests/cobalt/test_playbook_db.py` at the end of PASS 1 and `tests/cobalt/test_playbook_db.py` at the end of PASS 2; row P7 names `ops/desk/gate-lists.md` in its `files`. Carried; the gate's pass 1/2 ran those lines (log `:1035`, `:2079-2080`).
- (vii) records: R1055 → authorize.sh row `88:| R1055 | 09:04 ET | HIS RULING · APPROVED …` and `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1055 |" -- …cto-2026-10-11.md` → `0a1951efd16163dc5d234ecfe38d1ce63776561f` (my own `grep -n -F "^| R1055 "` returned nothing: `-F` reads `^` literally, my typo; the authorize.sh row stands). `ls ".../prompts/2026-10-13"` → no F20 card among the listed files (`445-…` to `530-…`; `502-draft-f23.md`, `503-f23-card.md`, no `f20` name). `grep -n -F "test_playbook_live" ops/desk/gate-lists.md` → `:45` (LIVE-NOTE, last file, once) and `:54` (ALLOWED SKIPS item). The `git -C … rev-parse` and `git diff --stat main …` records are not on my list: not re-run.
- (viii) L32: this report holds no value of his: constructed tickers `ZZPB`, `ZZPM` and the test's date `2026-10-11` only.

## OPEN
- O1 (X4) · REJECTED — card row P5 (the C11 sequence). A kill between `<date>` → `<date>.old` and `<date>.tmp` → `<date>` leaves no `<date>` until the next run's start renames `.old` back (`cli.py:75-79`). What would settle it: a ruling that the window is accepted as designed (FINAL C11 / E1 already frame it as an experiment), or a card row that changes the swap. The test text is under `## OWN FINDINGS`.

## CONTINUE
next: none — CHECK DONE.

## DECISIONS
- O1 (open item, ships to the follow-up list): REJECTED, red for its stated reason (`AssertionError: ['2026-10-11.old', '2026-10-11.tmp']`), but row P5 prescribes the sequence. Safe default taken: not fixed, test removed, the build's DECISION E1 stands as the record. Not his notes, money or sizing.

## RECORDS
- L74: `## L74` (the session's attribution notice asked for a `Claude-Session:` line; not acted on).
- House A Grok produced `FINDINGS: 0` (its own file, closing line present). Gemini probed UP and was not seated: the card's `HOUSE B: as needed` needs no house B; the stop line's field reads `none available` as the only house-B "none" form the stop line allows.
- No dropped finding; no house that produced nothing; no `REFUSED, not needed`; no `CONTINUED`; no extra lock take (the one take was the gate's, after `lock: waited 15 min`).
- `files opened: 21` — CHECK-HUB.md; the card; BUILD-HUB.md (`## THE LOCK`, `## E2`, `## RESTARTS`, `## W`); `src/cobalt/playbook/cli.py`, `data.py`, `deck.py`, `config.py`; `src/cobalt/taxonomy/vault_loader.py`; `tests/cobalt/test_playbook_offline.py`, `test_playbook_db.py`, `test_playbook_live.py`; `src/cobalt/jobs/config.py`, `wrapper.py`; `src/cobalt/cli.py`; the build report; `docs/30 - Design/F23-FINAL-2026-10-11.md`; `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); `<S>/house-a.md`; the house-probe, Grok and gate task outputs.
- Check of `f23-playbook-1013`: house A `Grok`, house B `none` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: f23-playbook-1013 · pass: 1 · tip: 72c8a069 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8519/0 · with-DB 5504/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 220271
