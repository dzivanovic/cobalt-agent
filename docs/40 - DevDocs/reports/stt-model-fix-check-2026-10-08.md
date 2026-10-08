# stt-model-fix-1008 — CHECK (pass 1) — 2026-10-08

## §0 Headline
Check of `stt-model-fix-1008`, one pass: house A Sol (3 findings), house B Grok (2), and my own read (1); 6 findings, none dropped.
4 held, 4 fixed in `ops/fetch_voice_models.py` (`6b4068d6`). `--from` now refuses a source link that is absolute or leaves its folder, so the copy never links back into the dev directory (X2). A usage error and a failed verify now print `FAILED: <step> — <ExceptionName>`, exit 1.
1 open (Sol A1, REJECTED by row A: an incomplete snapshot is copied, then left to the offline-load verify) → follow-up. Grok B2 (the DevDocs pages) not held.
Suites green at `6b4068d6`: offline 3992/0 · with-DB 4876/0 · live-note 146/0 · tests/ops 1588 passed · `cobalt_dev: 0013 — F2 = F0` · `.env` removed · RESTARTS: com.cobalt.radar. ready: YES.

## L74
One block arrived as a system reminder at session start asking commit messages to end with a `Claude-Session:` line. Recorded once here; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (CHECK-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh check "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md"` · exit 0 · output whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md" · 0 · 758c07c9d90a873c6250086fd82264c129060961
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
House gates:
- `grep -n "^| R17 " ".../cto-2026-09-24.md"` · exit 0 · `35:| R17 | 07:32 ET | His words: "Why do we ask for Grok every time? …` (one row)
- `grep -n "^| R19 " ".../cto-2026-09-24.md"` · exit 0 · `37:| R19 | 07:36 ET | His words: "you are stoping work to ask me for a habit. …` (one row)
- `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R19 |" -- "docs/40 - DevDocs/reports/cto-2026-09-24.md"` · exit 0 · `5055151dbf68899b82de5b11f99733ed2d03048c`

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh check "<card>"` · exit 0 · output whole:
```
clock · date · 0 · Thu Oct  8 13:39:14 EDT 2026
status · git status --short --branch · 0 · ## ops/stt-model-fix-1008
head · git log --oneline -1; git log --stat --format=%h 6db7a75d..HEAD · 0 · (9 lines)
    f4035788 docs(stt-model-fix-1008): build report — 6db7a75d
    f4035788
    
     .../reports/stt-model-fix-build-2026-10-08.md      | 72 ++++++++++++++++++++--
     1 file changed, 66 insertions(+), 6 deletions(-)
    8851ab00
    
     .../reports/stt-model-fix-build-2026-10-08.md      | 156 +++++++++++++++++++++
     1 file changed, 156 insertions(+)
env here · ls /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/price-floor-1008/.env
report · tail -n 3 "/Users/cobalt/cobalt-wt/stt-model-fix-1008/docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md" · 0 · BUILT · job: stt-model-fix-1008 · tip: 6db7a75d | on 4f764e79 | migration: none | offline 3992/0 | with-DB 4876/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 200409
range · git log --oneline 4f764e79..6db7a75d · 0 · (2 lines)
    6db7a75d fix(stt-model-fix-1008): the one voice model-fetch command, local copy first; both scripts derive no restart (A, B; L1, L3, L42)
    ec7b3460 wip(stt-model-fix-1008): red
PREFLIGHT OK
```
- THE RANGE · `git log --stat --format=%h 4f764e79..6db7a75d` · exit 0:
```
6db7a75d
 docs/40 - DevDocs/cobalt/jobs/restarts.md   |   4 +
 docs/40 - DevDocs/ops/fetch_voice_models.md |   5 +
 ops/fetch-voice-models.sh                   |   2 +
 ops/fetch_voice_models.py                   | 144 ++++++++++++++++++++++++++++
 src/cobalt/jobs/restarts.py                 |   2 +-
 tests/ops/test_fetch_voice_models.py        |  10 +-
 6 files changed, 164 insertions(+), 3 deletions(-)
ec7b3460
 tests/cobalt/test_jobs_restarts.py   |  12 +++
 tests/ops/test_fetch_voice_models.py | 166 +++++++++++++++++++++++++++++++++++
 2 files changed, 178 insertions(+)
```
  Path union: `docs/40 - DevDocs/cobalt/jobs/restarts.md`, `docs/40 - DevDocs/ops/fetch_voice_models.md`, `ops/fetch-voice-models.sh`, `ops/fetch_voice_models.py`, `src/cobalt/jobs/restarts.py`, `tests/ops/test_fetch_voice_models.py`, `tests/cobalt/test_jobs_restarts.py`. The card carries no `DB: none` key: the DB-none diff rule does not apply.
- `ls <S>` · exit 1 · `ls: /Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stt-model-fix-1008-check: No such file or directory` → fresh.
- THE HOUSE PROBES · `sh /Users/cobalt/cobalt/ops/desk/house-probe.sh` · exit 0:
```
sol: UP
grok: UP
gemini: UP
```
- Seats: **house A: Sol (gpt-5.6-sol) · house B: Grok (grok-4.7)**. Card `HOUSE B: as needed`.
- PROVEN BY FIRST REAL USE: the write strings (`git add`/`git commit`) at `## 4`; `COBALT_ENV=dev …` inside `gate.sh` at `## 6`.

## Files copied
`sh /Users/cobalt/cobalt/ops/desk/stage-set.sh "<card>" "<S>"` · exit 0 · output whole (`<S>` = `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/stt-model-fix-1008-check`):
```
17484 <S>/diff.md
13471 <S>/files/126-stt-model-fix-card.md
29976 <S>/files/stt-model-fix-build-2026-10-08.md
4845 <S>/files/wt/docs/40 - DevDocs/cobalt/jobs/restarts.md
1315 <S>/files/wt/docs/40 - DevDocs/ops/fetch_voice_models.md
102 <S>/files/wt/ops/fetch-voice-models.sh
6273 <S>/files/wt/ops/fetch_voice_models.py
12098 <S>/files/wt/src/cobalt/jobs/restarts.py
29256 <S>/files/wt/tests/cobalt/test_jobs_restarts.py
6585 <S>/files/wt/tests/ops/test_fetch_voice_models.py
384 <S>/rulings.md
STAGED 11 files · 121789 bytes · commits 2
```
(`commits 2` = PREFLIGHT's range count.) The `## READ` files, each `sh /Users/cobalt/cobalt/ops/desk/stage-copy.sh <source> <S>/files/wt/<path>`:
```
COPIED 6851 <S>/files/wt/src/cobalt/voice/transcribe.py
COPIED 15021 <S>/files/wt/src/cobalt/voice/web.py
COPIED 7718 <S>/files/wt/src/cobalt/voice/config.py
COPIED 3825 <S>/files/wt/src/cobalt/env.py
COPIED 11824 <S>/files/wt/src/cobalt/vault.py
COPIED 6736 <S>/files/wt/src/cobalt/backup/config.py
COPIED 3063 <S>/files/wt/configs/cobalt/voice.yaml
COPIED 3223 <S>/files/wt/ops/start_aset.sh
COPIED 7197 <S>/files/wt/tests/cobalt/test_voice_transcribe.py
COPIED 63651 <S>/files/wt/docs/30 - Design/VOICE-TTS-DRAFT-FINAL-2026-09-25.md
```
`<S>/HOUSE-INSTRUCTIONS.md` written (15366 bytes): HOUSE TEXT verbatim, the card's `## ROWS`, `## NOT IN THIS JOB`, `## CHECK ASKS`, `## RECORDS` whole, the Files paragraph.
Houses started 13:41 EDT (`date` → `Thu Oct  8 13:41:18 EDT 2026`), gates R17 / R19 re-read (one row each), `cd <AGY>`, house A Sol (task b4hn27r8r) and house B Grok (task b7jbnjywp) started back to back, `cd <WT>`, `git status --short --branch` → `## ops/stt-model-fix-1008`.

## OWN FINDINGS
Written before either house's list was opened. Read: the card; the diff `4f764e79..6db7a75d` (saved `git log -p`); `ops/fetch_voice_models.py` and the tests as they sit in the diff; `src/cobalt/voice/config.py` whole; `transcribe.py:60`–`:109`; `web.py:40`–`:154`; `configs/cobalt/voice.yaml` whole; the build report's `## RESTARTS`, `## W THE THREE SUITES`, `## PRE-STOP SELF-CHECK`, `## FOR THE CHECK`, `## RECORDS` and last line.

FINDING O1
ROW: X2 (row A, the copy)
CLAIM: `_copy` copies the source repo folder with `shutil.copytree(repo, dest, symlinks=True)` (`ops/fetch_voice_models.py:104`) and never checks where each link points, so a source whose snapshot link is absolute (or relative but leaving the repo folder) is copied as a link back into the source directory; `model_present` and the offline load then pass and the script prints READY while production's model lives in the dev directory.
RUN: TEST — `tests/ops/test_fetch_voice_models.py`
```python
def test_a_source_link_out_of_its_folder_never_lands_in_the_target(env, fake_load, tmp_path, capsys):
    # X2: a snapshot link that leaves the repo folder (here, absolute into the
    # source's blobs) must never be copied as a link back into the source.
    mod, target, calls = env
    src = _fake_source(tmp_path / "src")
    link = src / REPO_DIR / "snapshots" / REV / "model.bin"
    blob = link.resolve()
    link.unlink()
    os.symlink(str(blob), link)
    rc = mod.main(["--from", str(src)])
    copied = target / REPO_DIR / "snapshots" / REV / "model.bin"
    if rc == 0:
        assert copied.resolve().is_relative_to(target.resolve()), f"{copied} resolves to {copied.resolve()}"
    else:
        assert capsys.readouterr().out.strip().splitlines()[-1].startswith("FAILED: ")
        assert not (target / REPO_DIR).exists()
    assert calls == []
```
EXPECT: on the tip `rc == 0` and the assertion fails: `AssertionError: …/target/models--Systran--faster-whisper-tiny.en/snapshots/<rev>/model.bin resolves to …/src/models--Systran--faster-whisper-tiny.en/blobs/blob…`.

Read with no runnable finding (recorded, not counted): X1 — every `--from` path reaches only `local_files_only=True` lookups (`_snapshot`, `model_present`, `_load_model`); `_download` sits on the no-`--from` branch only. X3 — `_config` / `_check_target` match `config.py:141`–`:148`, `:85`–`:93`, `:100`–`:102` word for word, the resolved-vault refusal left out as the card says. X4 — pinned by test (6). The no-`--from` download into a target already holding a partial folder is not refused (the card's step (3) asks no refusal); no offline run can show what the hub library does there, so no finding is written.

## Findings
House A Sol finished 13:48 (`date` → `Thu Oct  8 13:48:01 EDT 2026`); its final message, after the transcript's `tokens used`, written by me to `<S>/house-a.md` (ends `FINDINGS: 3`). House B Grok finished 13:56 (`date` → `Thu Oct  8 13:56:49 EDT 2026`); it wrote `<S>/house-b.md` itself (ends `FINDINGS: 2`) and replied with that path. Every block carries a `RUN:` line followed by a `def test_` or one allowed command: nothing dropped.

| id | house | row | claim (≤30 words) | run |
|---|---|---|---|---|
| O1 | Opus (own) | X2 | `copytree(symlinks=True)` (`ops/fetch_voice_models.py:104` at tip) keeps an absolute source link, so the copied `model.bin` resolves into the source and the script prints READY | TEST |
| A1 | Sol | A | `_copy` checks only `model.bin` (`:97`), so an incomplete pinned snapshot is copied into `model_dir` instead of failing before any write | TEST |
| A2 | Sol | X2 | a relative source link that leaves the repo folder is copied unchecked (`:104`); the copied link resolves into `--from` and READY prints | TEST |
| A3 | Sol | A | `parse_args` (`:111`) sits outside the failure handler: a usage error exits 2 with argparse usage, not a `FAILED: <step> — <ExceptionName>` line and exit 1 | TEST |
| B1 | Grok | A | a copy leaving the model absent raises `Refused` (`:127`) printed as `FAILED: {e}` (`:131`), so the last line is not `FAILED: verify — Refused` | TEST |
| B2 | Grok | SCOPE | the tip adds DevDocs pages the rows do not list (`docs/40 - DevDocs/ops/fetch_voice_models.md`, `docs/40 - DevDocs/cobalt/jobs/restarts.md`) | COMMAND |

## Dropped
none

## RUNS
Each test pasted into `tests/ops/test_fetch_voice_models.py` with the Edit tool, unchanged, run alone with `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_fetch_voice_models.py::<test>` at tip `6db7a75d`.

| id | source | run | output | verdict |
|---|---|---|---|---|
| O1 | Opus | `::test_a_source_link_out_of_its_folder_never_lands_in_the_target` | `1 failed` · `AssertionError: …/target/models--Systran--faster-whisper-tiny.en/snapshots/<rev>/model.bin resolves to …/src/models--Systran--faster-whisper-tiny.en/blobs/blob0000…` · stdout `voice model READY: tiny.en <rev> at …/target/…` | HELD |
| A1 | Sol | `::test_an_incomplete_source_snapshot_fails_and_writes_nothing` | `1 failed` · `AssertionError: assert 0 == 1` · stdout `voice model READY …` | REJECTED — row A: step (2) "finds the pinned snapshot there: `faster_whisper.utils.download_model(…, local_files_only=True, …)`" and copies it; the only no-write refusal is "When `--from` lacks the pinned snapshot"; step (4) "an offline load must succeed: `transcribe._load_model(cfg)`" is where an incomplete snapshot fails. The test patches out `_snapshot`, `model_present` and the offline load (`fake_load`), the three steps the row uses. Test removed again; stays OPEN |
| A2 | Sol | `::test_a_source_link_that_would_point_back_to_the_source_is_refused` | `1 failed` · `AssertionError: assert 0 == 1` · stdout `voice model READY …` | HELD |
| A3 | Sol | `::test_malformed_arguments_fail_with_the_command_contract` | `1 failed` · `argparse.ArgumentError: argument --from: expected one argument` → `SystemExit: 2`; stderr `pytest: error: argument --from: expected one argument` | HELD (row A: "Any failure prints `FAILED: <step> — <ExceptionName>` and exits 1") |
| B1 | Grok | `::test_a_copy_that_leaves_the_model_absent_names_the_exception` | `1 failed` · `AssertionError: assert 'FAILED: veri...he_mo0/target' == 'FAILED: verify — Refused'`; actual `FAILED: verify — the pinned tiny.en <rev> is not present under …/target` | HELD (row A, the same line; the verify failure has no row-given text of its own) |
| B2 | Grok | `git diff --name-only 4f764e79..6db7a75d -- docs` | `docs/40 - DevDocs/cobalt/jobs/restarts.md` · `docs/40 - DevDocs/ops/fetch_voice_models.md` | NOT HELD — the output is as stated, but the claim's reason ("outside the rows") fails: `BUILD-HUB.md` `## E3` requires "ONE dated line in its page under `docs/40 - DevDocs/cobalt/`" for each changed module, and `CHECK-HUB.md` `## 7` (ii) scopes only non-docs paths |

Held tests committed before any fix: `git commit … -- tests/ops/test_fetch_voice_models.py` → `[ops/stt-model-fix-1008 8e8428af] wip(stt-model-fix-1008): check red — O1, A2, A3, B1` · `1 file changed, 77 insertions(+)`.

## FIXES
| ids | file | change | run |
|---|---|---|---|
| O1, A2 | `ops/fetch_voice_models.py` | new `_check_links(repo)`, called in `_copy` before the dest check and before any write: every link in the source repo folder must be relative and resolve inside the folder, else `Refused("<link> links outside <folder> — nothing copied")` | below |
| A3 | `ops/fetch_voice_models.py` | `_Parser(argparse.ArgumentParser)` whose `error()` raises `ArgumentError`; `main` catches it → `FAILED: arguments — ArgumentError`, exit 1, nothing on stderr | below |
| B1 | `ops/fetch_voice_models.py` | verify prints `verify: the pinned <model> <rev> is not present under <dir>` as a detail line, then the last line `FAILED: verify — Refused` | below |

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_fetch_voice_models.py` → `11 passed, 15 warnings in 1.31s` (no skip: test (5), the real dev snapshot, copied and loaded with the link check in place). DevDocs line: `docs/40 - DevDocs/ops/fetch_voice_models.md` `## 2026-10-08 — stt-model-fix-1008 check` (the module's page as the build placed it). Commit: `[ops/stt-model-fix-1008 6b4068d6] fix(stt-model-fix-1008): --from refuses links that leave the folder; usage and verify failures name their exception (check O1, A2, A3, B1)` · `2 files changed, 33 insertions(+), 3 deletions(-)`.

## Suites
RESTARTS first, at `6b4068d6`: `uv run cobalt jobs restarts 4f764e79..HEAD` → exit 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/jobs/restarts.md	M	DOCS	-
docs/40 - DevDocs/ops/fetch_voice_models.md	A	DOCS	-
docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md	A	DOCS	-
ops/fetch-voice-models.sh	A	operator script; no Cobalt reader	-
ops/fetch_voice_models.py	A	operator script; no Cobalt reader	-
src/cobalt/jobs/restarts.py	M	static import reach	com.cobalt.radar
tests/cobalt/test_jobs_restarts.py	M	test/documentation; no resident	-
tests/ops/test_fetch_voice_models.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.radar
```
No `UNCLASSIFIED` row.
W, at tip `6b4068d6`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh stt-model-fix-1008 all --deploy` (background) → exit 0, output whole:
```
offline 3992/0
lock: waited 12 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4876/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/stt-model-fix-1008-all-20261008-135857.log
```
- `grep -n -F "OUTSIDE" <log>` → nothing (no skip outside the allowed set). `grep -n -F "pass 1: whole (deploy)" <log>` → `933:pass 1: whole (deploy)`.
- `cobalt_dev: 0013 — F2 = F0` · `.env: removed`; `ls /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env` → `ls: …/.env: No such file or directory`.
- No migration and no with-DB test in this build or this check: no `--deselect`, no `--migration`, no `--tickers`.
- `tests/ops` (the fetch tests live there; the gate does not run it): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `1588 passed, 1 xfailed, 15 warnings in 453.52s (0:07:33)` (the build's 1584 plus the four held tests).

## Scope
PREFLIGHT's path union plus my commits: `ops/fetch_voice_models.py` (row A), `tests/ops/test_fetch_voice_models.py` (row A test file), `docs/40 - DevDocs/ops/fetch_voice_models.md` (DevDocs line). Nothing else.

## Checked against the branch
(i) `git log --oneline 6db7a75d..HEAD -- . ":(exclude)docs"` →
```
6b4068d6 fix(stt-model-fix-1008): --from refuses links that leave the folder; usage and verify failures name their exception (check O1, A2, A3, B1)
8e8428af wip(stt-model-fix-1008): check red — O1, A2, A3, B1
```
`<tip now>` = `6b4068d6`.
(ii) `git log --stat --format=%h 6db7a75d..HEAD` → `6b4068d6`: `docs/40 - DevDocs/ops/fetch_voice_models.md`, `ops/fetch_voice_models.py`; `8e8428af`: `tests/ops/test_fetch_voice_models.py`; `f4035788`, `8851ab00`: the build report. Every non-docs path is in row A's `files`.
(iii) Fence: `git log --oneline 4f764e79..HEAD -- src/cobalt/voice ops/start_aset.sh configs/cobalt/voice.yaml` → empty (covers `transcribe.py`, `web.py`, `config.py`, `voice.yaml`, `start_aset.sh`).
(iv) Held tests, each `grep -n -F "def <name>" tests/ops/test_fetch_voice_models.py` → one line: O1 `175:`, A2 `194:`, A3 `231:`, B1 `243:`; `8e8428af` (check red) sits below `6b4068d6` (fix) in (i).
(v) `ls <WT>/.env` → No such file; `git status --short --branch` → see `## RECORDS` (taken at close).
(vi) `git log --stat --format=%h 4f764e79..HEAD -- src/cobalt/db_migrations tests/cobalt` → `ec7b3460` `tests/cobalt/test_jobs_restarts.py` only: no migration, no with-DB test needing a level above `0013`; gate lists not concerned.
(vii) Card `## RECORDS`, re-run now:
- `ls -la /Users/cobalt/.cobalt` → `.`, `..`, `voice-scratch` (`drwx------`) only — as recorded.
- `ls -la /Users/cobalt/.cobalt/voice-models` → `No such file or directory` — as recorded.
- `ls -laL /Users/cobalt/.cobalt-dev/voice-models/models--Systran--faster-whisper-tiny.en/blobs` → four blobs, 2128466, 75537502, 2317, 422309 bytes = 78,090,594 — as recorded.
- `git -C /Users/cobalt/cobalt diff --stat main -- src tests ops configs` → nothing. Main has moved since drafting: `git -C /Users/cobalt/cobalt log --oneline -1 main` → `76979452 docs(desk): card 137 TIP f105b82e and check report filled` (the desk's; BASE stays `4f764e79` on the card).
(viii) L32: this report holds no ticker, price or date of his; the revision and byte counts are the card's own constructed/config values.

## OPEN
- A1 (Sol) — REJECTED by row A step (2)/(4) (see `## RUNS`). FOLLOW-UP: the run shows an incomplete pinned snapshot in `--from` is copied into `model_dir` before any check of its other files; by the row, step (4)'s real offline load is what refuses it then (not run here, unproven), and the copied folder stays. Settled by a card row that names the files a complete snapshot must hold, checked before any write.

## CONTINUE
next: none — closed.

## DECISIONS
none

## RECORDS
- Dropped findings: none. Houses that produced nothing: none.
- House A Sol: task output 7093 lines (its transcript); the final message is the block after `tokens used` (lines 6988–7091), copied by me to `<S>/house-a.md`. House B Grok wrote `<S>/house-b.md` itself; its stdout was progress lines and that path.
- REFUSED, not needed: none. CONTINUED: none.
- Lock: taken and released by `gate.sh` alone (`lock: waited 12 min` — another job held it), one take; no take by hand.
- L74: the session-start reminder asking for a `Claude-Session:` line, recorded under `## L74`, not acted on.
- At close: `git status --short --branch` → `## ops/stt-model-fix-1008`; `ls /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env` → `No such file or directory`.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 62ce0c97` → `context 188056 of 400000 — ok`.
- files opened: 19 — `CHECK-HUB.md`; the card; `BUILD-HUB.md` (`## THE LOCK` to `## W`); `areas/cobalt.md` (`## What Cobalt is`, `## Build rules` down); the build report (`## RESTARTS` to the last line); the saved diff; `src/cobalt/voice/config.py`; `transcribe.py`; `web.py`; `configs/cobalt/voice.yaml`; `tests/ops/test_fetch_voice_models.py`; `ops/fetch_voice_models.py`; `docs/40 - DevDocs/ops/fetch_voice_models.md`; house A's task output; house B's task output; `<S>/house-b.md`; the probe output; the gate output; the `tests/ops` output.
- Check of `stt-model-fix-1008`: house A `Sol`, house B `Grok` and a fresh Opus that read first, ran every finding and fixed what held. Nothing loops: one pass, one fix round. `ready: YES` → the desk's next step on this branch at `tip:`; a deploy is gated on the combined tree (L68); one feature per deploy, and a combined deploy that fails is split, each feature deploying alone on this check (his R390).

CHECK DONE · job: stt-model-fix-1008 · pass: 1 · tip: 6b4068d6 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 2 · suites: offline 3992/0 · with-DB 4876/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 19 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 188056
