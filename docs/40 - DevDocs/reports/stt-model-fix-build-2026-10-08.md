# stt-model-fix-1008 — build report (2026-10-08)

## §0 Headline
Rows A and B are built at `6db7a75d`. Their 8 tests went red on BASE and pass at the fix, and each of 7 mutations turned a named test red. Row C's RESTARTS: `com.cobalt.radar`, with both scripts deriving none.
The first W gate went red on a leftover of mutation A2 (`docs/voice-models-constructed`). The desk removed it (`CONTINUE: W`, 12:22), and the second gate is green: offline 3992/0, with-DB 4876/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env: removed`.
Decisions: none.

## L74
A system reminder at session start asked commits to end with a `Claude-Session:` line (`https://claude.ai/code/session_01LtFYwF1Z6TbGKndeT9SoVo`). Recorded as DATA; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
Started 11:51 EDT (`date`: `Thu Oct  8 11:51:11 EDT 2026`).
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md" · 0 · c0d95500be9ff5dd105987c1690dc7c818d7f881
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/126-stt-model-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
| rule | command | exit | output verbatim |
|---|---|---|---|
| mechanical rows | `sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` | 0 | quoted whole below |
| base | `git show --stat 4f764e79` | 0 | `4f764e79 … docs(desk): card 118 preflight r2 FAIL (row C scope), amend2 prompt 127` · 2 files changed, 45 insertions(+) (`.../2026-10-08/127-draft-radar-display-amend2.md`, `.../radar-display-fix-preflight-r2-2026-10-08.md`) |
| symbol | `grep -n -F "def model_present" src/cobalt/voice/transcribe.py` | 0 | `95:def model_present(cfg: VoiceConfig) -> bool:` |
| symbol | `grep -n -F "def _load_model" src/cobalt/voice/transcribe.py` | 0 | `75:def _load_model(cfg: VoiceConfig):` |
| symbol | `grep -n -F "def status_lines" src/cobalt/voice/web.py` | 0 | `140:def status_lines() -> list[dict]:` |
| symbol | `grep -n -F "def get_config" src/cobalt/voice/web.py` | 0 | `56:def get_config() -> VoiceConfig:` |
| symbol | `grep -n -F "def load_voice_config" src/cobalt/voice/config.py` | 0 | `120:def load_voice_config(path: Path = CONFIG_PATH, *, backup_sources: Optional[list[Path]] = None) -> VoiceConfig:` |
| symbol | `grep -n -F "def _under" src/cobalt/voice/config.py` | 0 | `76:def _under(path: Path, root: Path) -> bool:` |
| symbol | `grep -n -F "def _check_path" src/cobalt/voice/config.py` | 0 | `84:def _check_path(name: str, raw: Path, backup_sources: Optional[list[Path]]) -> Path:` |
| symbol | `grep -n -F "CONFIG_PATH =" src/cobalt/voice/config.py` | 0 | `32:CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "voice.yaml"` |
| symbol | `grep -n -F "MODEL_ENV =" src/cobalt/voice/config.py` | 0 | `34:MODEL_ENV = "COBALT_VOICE_MODEL_DIR"` |
| symbol | `grep -n -F "PROD_VAULT_PATH_REFERENCE" src/cobalt/vault.py` | 0 | `94:PROD_VAULT_PATH_REFERENCE = "/Users/cobalt/Vault/Think"` (+ 7 doc/use lines: 11, 25, 68, 161, 170, 195, 204) |
| symbol | `grep -n -F "def resolve_vault_path" src/cobalt/vault.py` | 0 | `155:def resolve_vault_path() -> Path:` (`:164` `mode = env.resolve_env()  # raises EnvConfigError when unset/unknown`, Read tool) |
| symbol | `grep -n -F "def load_backup_config" src/cobalt/backup/config.py` | 0 | `161:def load_backup_config(path: Path = CONFIG_PATH) -> BackupConfig:` |
| symbol | `grep -n -F "env" src/cobalt/backup/config.py` | 1 | nothing (the backup loader reads no mode) |
| symbol | `grep -n -F "OPS_TOOLS" src/cobalt/jobs/restarts.py` | 0 | `36:OPS_TOOLS = frozenset({"ops/cto-desk.sh"})` · `230:        if not rule and (path in OPS_TOOLS or path.startswith(OPS_DESK_PREFIX)):` |
| symbol | `grep -n -F "def test_an_operator_script_with_no_cobalt_reader_derives_no_restart" tests/cobalt/test_jobs_restarts.py` | 0 | `97:def test_an_operator_script_with_no_cobalt_reader_derives_no_restart(monkeypatch):` |
| symbol | `grep -n -F "needs_model" tests/cobalt/test_voice_transcribe.py` | 0 | `39:def needs_model():` (+ uses at 79, 90, 130) |
| symbol | `grep -n -F "COBALT_VOICE_MODEL_DIR" ops/start_aset.sh` | 0 | `37:export COBALT_VOICE_MODEL_DIR="/Users/cobalt/.cobalt/voice-models"` |
| symbol | `grep -n -F "fetch-voice-models" "docs/30 - Design/VOICE-TTS-DRAFT-FINAL-2026-09-25.md"` | 0 | `159:` [F-30] "The fetch command's path is `ops/fetch-voice-models.sh`. … It is the only network path. …" · `317:` "The ONE model-fetch deploy command, `ops/fetch-voice-models.sh` …" · `332:` L3 one model-fetch command |
| symbol | `grep -n -F "COBALT_ENV" tests/cobalt/conftest.py` | 0 | `11:2. Pin `COBALT_ENV=dev` and give the DB-touching tests a transaction` · `197:` |
| callers | `grep -rn -F "model_present(" src` | 0 | `src/cobalt/voice/web.py:145:        if not model_present(get_config()):` · `transcribe.py:95` (def) |
| callers | `grep -rn -F "_load_model(" src` | 0 | `transcribe.py:75` (def) · `src/cobalt/voice/transcribe.py:136:        model = _load_model(self.cfg)` |
| callers | `grep -rn -F "status_lines(" src` | 0 | `web.py:140` (def) · `src/cobalt/voice/web.py:154:    return {"lines": status_lines()}` |
| callers | `grep -rn -F "load_voice_config(" src` | 0 | `src/cobalt/voice/turn.py:111` · `src/cobalt/voice/web.py:59` · `src/cobalt/voice/cli.py:56` · `config.py:120` (def) |
| tests/ops has no COBALT_ENV pin | Read `tests/ops/conftest.py` | — | its one autouse fixture puts guard stand-ins on PATH; no `COBALT_ENV` |
| dev source | `ls -la /Users/cobalt/.cobalt-dev/voice-models/models--Systran--faster-whisper-tiny.en/snapshots/0d3d19a32d3338f10357c0889762bd8d64bbdeba` | 0 | `config.json -> ../../blobs/4065bb3b…`, `model.bin -> ../../blobs/1a5afae0…`, `tokenizer.json -> ../../blobs/15d7bdf9…`, `vocabulary.txt -> ../../blobs/ee695b8d…` |
| backup sources | `grep -n -F "sources" -A 8 configs/cobalt/backup.yaml` | 0 | `/Users/cobalt/Vault/Think`, `/Users/cobalt/cobalt/data/.cobalt_vault` |
| wc | `wc -l src/cobalt/jobs/restarts.py tests/cobalt/test_jobs_restarts.py` | 0 | 281 · 624 (the three row-A files are new) |
| reports in `## READ` | — | — | none named; no `tail` owed |
| restarts | `uv run cobalt jobs restarts 4f764e79..HEAD` | 0 | `docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md	A	DOCS	-` · `RESTARTS: none` (the only path is this untracked report) |

preflight.sh output, whole:
```
clock · date · 0 · Thu Oct  8 11:51:27 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/stt-model-fix-1008
    ?? "docs/40 - DevDocs/reports/stt-model-fix-build-2026-10-08.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 4f764e79 docs(desk): card 118 preflight r2 FAIL (row C scope), amend2 prompt 127
diff · git diff --stat 4f764e79 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/stt-model-fix-1008 · 0 · 4f764e79 docs(desk): card 118 preflight r2 FAIL (row C scope), amend2 prompt 127
env here · ls /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

Card `## RECORDS` copied: PRODUCTION TODAY (`/Users/cobalt/.cobalt` holds only `voice-scratch`; `voice-models` absent — not re-read: writing or reading there is the desk's, `## NOT IN THIS JOB`) · DEV SOURCE (4 relative links into `blobs/`, 78,090,594 bytes — links re-read above) · POST-DEPLOY (the desk's command) · RESTARTS expected none from the scripts · DB: every test offline; no lock (no with-DB red; W runs the gate, which takes it) · BASE `4f764e79` (re-read: `git log --oneline -1` → `4f764e79`).
No lock probe (L76 as amended).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → exit 0: `3991 passed, 787 skipped, 1 xfailed, 36 warnings in 653.37s (0:10:53)` — 0 failed, 0 errors (`.env` absent, so the with-DB tests skip).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 30.29s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` — it does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests written, no `src/` edit: `tests/ops/test_fetch_voice_models.py` (new, 7 tests) and `test_the_voice_model_fetch_scripts_derive_no_restart` in `tests/cobalt/test_jobs_restarts.py`. No with-DB red, so no lock take.
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_fetch_voice_models.py tests/cobalt/test_jobs_restarts.py` → exit 1: `1 failed, 21 passed, 15 warnings, 7 errors in 14.52s`.
- Row A, all 7 tests: `ERROR at setup` — `E   FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/stt-model-fix-1008/ops/fetch_voice_models.py'` (the script is absent; the row's named reason). (4) is the banner test.
- Row B: `test_the_voice_model_fetch_scripts_derive_no_restart` FAILED — `E           AssertionError: assert ('com.cobalt....cobalt.radar') == ()` / `Left contains 6 more items, first extra item: 'com.cobalt.agent'` (the path escalates to every resident; the row's named reason). The 20 neighbouring tests pass.
Commit `ec7b3460 wip(stt-model-fix-1008): red`.

## E3 THE ROWS
- **Row A** — `ops/fetch_voice_models.py` (new) and `ops/fetch-voice-models.sh` (the two-line wrapper, as the card gives it). `_config()` reads `CONFIG_PATH` with `yaml.safe_load`, takes the four keys (a missing one → `FAILED: config — KeyError`), applies the `COBALT_VOICE_MODEL_DIR` override (set but empty → `FAILED: config — VoiceConfigError: …`), and builds `VoiceConfig.model_construct(...)`. `_check_target()` runs `_check_path`'s refusals that need no mode, in its words, through `config._under`; the backup sources come from `load_backup_config()`. Then: (1) `model_present` → skip; (2) `--from`: `_snapshot()` (local-only `download_model`), dest folder exists → `FAILED: <dest> exists but does not hold the pinned snapshot — move it aside`, else `mkdir(mode=0o700)` + `copytree(..., symlinks=True)`; a missing snapshot → `FAILED: the pinned <model> <revision> snapshot is not under <dir>`; (3) no `--from` → `_download()`, the one network call; (4) `model_present` + `transcribe._load_model` → `voice model READY: …`. No `COBALT_ENV`, no `load_voice_config()`, no delete.
  Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_fetch_voice_models.py` → `7 passed, 15 warnings in 1.47s` (no skip: (5) ran on the real dev snapshot with the real offline load).
- **Row B** — `OPS_TOOLS = frozenset({"ops/cto-desk.sh", "ops/fetch-voice-models.sh", "ops/fetch_voice_models.py"})` (`src/cobalt/jobs/restarts.py:36`). Green: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py` → `46 passed in 16.68s`.
- Together with the neighbours: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_fetch_voice_models.py tests/cobalt/test_jobs_restarts.py tests/cobalt/test_jobs_reads.py tests/cobalt/test_voice_transcribe.py` → `63 passed, 19 warnings in 21.62s`.
- **Test rewritten (said so):** test (7) was strengthened after mutation A2's first run. Under A2 it went red (`assert 0 == 1`; the script printed `voice model READY: … at /Users/cobalt/cobalt-wt/stt-model-fix-1008/docs/voice-models-constructed/…`). But the mutated script had really copied into the worktree's `docs/`. The test now swaps `_copy` for a recorder (so a broken refusal writes nothing), uses a per-test folder name, and asserts the `FAILED: path — VoiceConfigError: model_dir … sits under docs/` line and `copies == []`. The leftover is under `## RECORDS`.

THE MUTATIONS (Edit tool, each undone with the Edit tool; `--tb=line`):
| mutation | change | result (summary · first failing line) |
|---|---|---|
| A1 (the fix undone) | `_copy(cfg, args.source)` → `pass` | `6 failed, 1 passed` · (1) `AssertionError: assert 1 == 0` (stdout `FAILED: verify — the pinned tiny.en 0d3d19a3… is not present under …/target`); (2), (3), (4) the banner test, (5), (6) red too. (7) stayed green: it pins the refusal, so A2 covers it |
| A2 (refusals) | `docs/` and repo-root `if`s → `if False and …` | `1 failed, 6 passed` · (7) `AssertionError: assert False … startswith('FAILED: path — VoiceConfigError: model_dir ')` (got `FAILED: verify — …`) — rerun with the rewritten test, nothing written |
| A3 (partial target, X4) | `if dest.exists() …` → `if False and (…)` | `1 failed, 6 passed` · (6) `AssertionError: assert 'models--Systran--faster-whisper-tiny.en' in 'FAILED: copy — FileExistsError'` |
| A4 (links, X2) | `symlinks=True` → `symlinks=False` | `1 failed, 6 passed` · (1) `AssertionError: assert False … is_symlink()` |
| A5 (network fallback, X1) | a missing `--from` snapshot → `return _download(cfg)` | `1 failed, 6 passed` · (2) `AssertionError: assert False … startswith('FAILED: the pinned tiny.en …')` (got `FAILED: copy — AssertionError`, the raising download) |
| A6 (present skip) | `if transcribe.model_present(cfg):` → `if False and …` | `1 failed, 6 passed` · (3) `AssertionError: assert 1 == 0` (stdout `FAILED: …/target/models--Systran--faster-whisper-tiny.en exists but does not hold the pinned snapshot — move it aside`) |
| B1 (the fix undone) | `OPS_TOOLS` back to `{"ops/cto-desk.sh"}` | `1 failed, 21 passed` · `test_the_voice_model_fetch_scripts_derive_no_restart` `AssertionError: assert ('com.cobalt....cobalt.radar') == ()` |
After the last undo: `git diff --stat` → `src/cobalt/jobs/restarts.py | 2 +-`, `tests/ops/test_fetch_voice_models.py | 10 ++++++++--` (the fix plus the test (7) rewrite, uncommitted at that point; no mutation left).
DevDocs: `docs/40 - DevDocs/cobalt/jobs/restarts.md` `## 2026-10-08 — stt-model-fix-1008`; new page `docs/40 - DevDocs/ops/fetch_voice_models.md` with the same dated heading.
Commit `6db7a75d fix(stt-model-fix-1008): the one voice model-fetch command, local copy first; both scripts derive no restart (A, B; L1, L3, L42)`.
- **Row C (RUN, asserts nothing)** — `uv run cobalt jobs restarts 4f764e79..HEAD` → quoted whole under `## RESTARTS`.

## RESTARTS
`uv run cobalt jobs restarts 4f764e79..HEAD` (at `6db7a75d`, with this report untracked) → exit 0:
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
No `UNCLASSIFIED` row. Both scripts derive no restart (row B). `src/cobalt/jobs/restarts.py` derives `com.cobalt.radar` through its static import reach (the card's RECORDS: "classified by its import reach").

## W THE THREE SUITES
`<tip>` = `6db7a75d`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh stt-model-fix-1008 all --deploy` (background) → exit 1, its output whole:
```
RED (exit 1): 1 failed, 3991 passed, 787 skipped, 1 xfailed, 36 warnings in 660.96s (0:11:00)
FAILED: docs/PLACEMENT.md violations:
log: /Users/cobalt/cobalt-wt/.gate-logs/stt-model-fix-1008-all-20261008-121010.log
```
The red is (a) OFFLINE. `grep -n -F "_____ test" <log>` → `73: test_no_db_skips_the_db_checks_and_exits_clean`. `grep -n -F "PLACEMENT" -A 12 <log>` → `483:  docs/voice-models-constructed: not a directory named in docs/PLACEMENT.md — file into one of the sanctioned tiers, never at repo root or in a new ad-hoc folder`. That folder is the leftover of mutation A2's first run (`## E3`, `## RECORDS`). It is git-ignored and not in the commit, but it sits in this worktree's tree, which `check_tree()` walks. The gate stopped at (a): no lock was taken, and `ls -la /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env` → `No such file or directory`. (b)–(f) and (e) were not run.
Beside the gate: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0, `1584 passed, 1 xfailed, 15 warnings in 472.75s (0:07:52)`.

**Second gate, after `CONTINUE: W` (12:22).** The same call (HEAD `8851ab00`, a report-only wip on top of `6db7a75d`; `git diff --stat 6db7a75d HEAD` → the report alone) → exit 0, its output whole:
```
offline 3992/0
lock: waited 0 min
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
log: /Users/cobalt/cobalt-wt/.gate-logs/stt-model-fix-1008-all-20261008-122245.log
```
- (a) offline: `grep -n -F "passed" <log>` → `863: 3992 passed, 787 skipped, 1 xfailed, 36 warnings in 617.95s (0:10:17)` → `<p>` = 3992. This build adds the 7 tests of `tests/ops/test_fetch_voice_models.py`, which `tests/ops` runs (above), and `tests/cobalt/test_jobs_restarts.py::test_the_voice_model_fetch_scripts_derive_no_restart`, which runs here.
- (b) lock: `868: $ sh /Users/cobalt/cobalt/ops/desk/take-devdb-lock.sh stt-model-fix-1008 90` · `869: lock taken: stt-model-fix-1008` · `872: lock: waited 0 min`. `<F0>` (`880:`) = `664 35 272c95bbb12241e3611e4b36326ccf87`. Proof-only → `LEVEL 0013`.
- (c) pass 1, executed command (log `:935`), copied whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py` → `1088: 4687 passed, 7 skipped, 83 deselected, 3 xfailed, 43 warnings in 803.20s (0:13:23)` → `<d1>` = 4687. The 7 SKIPPED lines are quoted above. `grep -n -F "OUTSIDE" <log>` → nothing, so no skip is outside the allowed set.
- (c2) `1090: dev forward: APPLIED 12:46:52`; `<F1>` (`1165:`) = `893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2 → `1800: 189 passed, 1 deselected, 5 warnings in 234.89s (0:03:54)` → `<d2>` = 189. This build deselects no test of its own, and none of its tests is with-DB. `<d>` = 4687 + 189 = 4876 = the gate's `with-DB 4876/0`.
- (c3r) `stray rows: not read (no --tickers given)`. This build writes no ticker.
- (f) `<F2>` (`1865:`) = `664 35 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`** (`1916:`). `1917: $ sh /Users/cobalt/cobalt/ops/desk/release-devdb-lock.sh stt-model-fix-1008` · `1918: lock released`. `ls /Users/cobalt/cobalt-wt/stt-model-fix-1008/.env` → `No such file or directory`. `.env: removed, proven gone (W)`.
- (e) live-note → `1987: 146 passed, 1 skipped, 15 warnings in 28.23s` → `<l>` = 146. The one skip (`test_replay_line.py:266`, `COBALT_TEST_LIVE_DRC`) does not name `COBALT_LIVE_VAULT_ROOT`.
- No migration in this build, so (c4) does not apply.

## PRE-STOP SELF-CHECK
(1) "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." Each test went red on BASE (E2: 7 × `FileNotFoundError … ops/fetch_voice_models.py`; row B `assert ('com.cobalt....cobalt.radar') == ()`). Each test also went red under a mutation (E3 table): (1) A1, A4 · (2) A1, A5 · (3) A1, A6 · (4) the banner test, A1 · (5) A1 · (6) A1, A3 · (7) A2 · row B B1. Test (7) was rewritten after A2's first run, as said in E3, and went red under A2 again. — holds.
(2) "Every entry path of each rule pinned by a test." Callers from PREFLIGHT:
- `model_present(` ← `web.py:145`: pinned by (4) through `web.status_lines()`.
- `status_lines(` ← `web.py:154`: the route wraps `status_lines()` with no other logic, and (4) calls it directly.
- `_load_model(` ← `transcribe.py:136`: unchanged by this build. The script's new call is pinned by (5), with the real offline load, and by the sentinel in (1)–(4) and (6).
- `load_voice_config(` ← `turn.py:111`, `web.py:59`, `cli.py:56`: unchanged; the script never calls it.
- The script's inputs: `--from` with the snapshot (1, 3, 4, 5), `--from` without it (2), a partial target (6), a refused target with `COBALT_ENV` unset (7). No `--from` (the download path) is pinned only as the call the tests forbid: every test asserts `calls == []`. The card's NOT IN THIS JOB fences any download in the build.
- `OPS_TOOLS` at `restarts.py:230`: both paths are pinned by row B's test, and the real range by row C's table.
— holds.
(3) "Every `file:line`, count and quote in the report re-read from tool output at the tip." Re-run at tip `6db7a75d` (HEAD `8851ab00` + report): `grep -n -F "OPS_TOOLS = " src/cobalt/jobs/restarts.py` → `36:OPS_TOOLS = frozenset({"ops/cto-desk.sh", "ops/fetch-voice-models.sh", "ops/fetch_voice_models.py"})` · `grep -n -F "def test_" tests/ops/test_fetch_voice_models.py` → 7 hits (80, 94, 105, 118, 129, 142, 157) · `git log --oneline 4f764e79..HEAD` · `git diff --stat 6db7a75d HEAD` → the report only · the gate log lines quoted under W were each grepped from the log. — holds.

## FOR THE CHECK
- Range `4f764e79..6db7a75d`:
  - `ec7b3460 wip(stt-model-fix-1008): red`
  - `6db7a75d fix(stt-model-fix-1008): the one voice model-fetch command, local copy first; both scripts derive no restart (A, B; L1, L3, L42)`
  - Report commits come after the tip: `8851ab00 wip(stt-model-fix-1008): W — offline red, docs/voice-models-constructed leftover needs removal`, then this report's close commit.
- Per row, the reds, mutations and greens are under `## E2 RED` and `## E3 THE ROWS`; the caller greps are under `## PREFLIGHT`.
- Row C's output, whole, is under `## RESTARTS`. Re-run at the tip now, the range also holds this committed report (DOCS); the derived set is unchanged.
- Suites: offline 3992/0 · with-DB 4876/0 (pass 1 4687, executed command quoted under W (c); pass 2 189) · live-note 146/0 · `tests/ops` 1584 passed.
- `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 35 272c95bbb12241e3611e4b36326ccf87`. Lock: `lock taken` (waited 0 min) inside the 12:22 gate, forward applied 12:46:52, `lock released` at the gate's end; one take only.
- CHECK ASKS, with where each is pinned (claims for the check to run, not proven by me beyond the tests named):
  - X1: `--from` paths reach `_snapshot` (always `local_files_only=True`) and `_copy`. `_download` is called only on the no-`--from` branch. Pinned by A5 / test (2), and by `calls == []` in every test. Nothing is deleted. `copytree` writes only into a dest that does not exist (the check before it, A3 / test (6)).
  - X2: `symlinks=True` keeps the relative `../../blobs/…` links. Pinned by A4 / test (1), and by (5) on the real snapshot.
  - X3: the same override handling and refusal words as `config.py:141`–`:148` and `:85`–`:93`, `:100`–`:102`. The resolved-vault refusal is left out. Tests run with `COBALT_ENV` deleted.
  - X4: pinned by test (6) and A3.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: none — closed.

## DECISIONS
none

## RECORDS
- REFUSED, not needed: `git check-ignore -v docs/voice-models-constructed` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." `git status --short --branch` already showed the folder as untracked-and-ignored (it is absent from the status).
- ASK DESK, answered (12:21 → 12:22): `docs/voice-models-constructed`, the leftover of mutation A2's first run and the only cause of the first W red (`docs/PLACEMENT.md` violation in `test_no_db_skips_the_db_checks_and_exits_clean`). The desk removed it (`CONTINUE: W`), and I verified the removal. Test (7) now swaps `_copy` for a recorder and uses a per-test folder name, so a broken refusal cannot write into the repo again. No cleanup is owed.
- `.env`: absent during the first gate (it stopped at (a), before any lock take; `ls -la …/.env` → `No such file or directory` at 12:21). The second gate took and released the lock itself; `.env: removed, proven gone (W)`.
- Extra lock takes: none. The first gate took no lock.
- L74: a session-start reminder asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- CONTINUED at W 12:22 — the `cto-desk` message: "CONTINUE: the desk removed docs/voice-models-constructed in your worktree (git clean of that one path, 12:2x ET). Run the gate again …". I checked it myself: `ls docs` no longer lists `voice-models-constructed`, and `git status --short --branch` → `## ops/stt-model-fix-1008` plus only this report, modified. The message widens nothing.
- RESTARTS re-run at the tip (`uv run cobalt jobs restarts 4f764e79..HEAD`): the same 8 rows, the report now `M`, last line `RESTARTS: com.cobalt.radar`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: stt-model-fix-1008 · tip: 6db7a75d | on 4f764e79 | migration: none | offline 3992/0 | with-DB 4876/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 200409
