# stt-model-fix-1008 — build report (2026-10-08)

## §0 Headline
Rows A and B are built at `6db7a75d`. Their 8 tests went red on BASE and pass at the fix, and each of 7 mutations turned a named test red. Row C's RESTARTS: `com.cobalt.radar`, with both scripts deriving none.
The W gate is red offline on a `docs/PLACEMENT.md` violation: `docs/voice-models-constructed`, a leftover in this worktree from mutation A2. No listed command removes it. Stopped at W and staying for the desk's `CONTINUE: W`.

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

## PRE-STOP SELF-CHECK

## FOR THE CHECK

## CONTINUE
next: W — once `/Users/cobalt/cobalt-wt/stt-model-fix-1008/docs/voice-models-constructed` is removed, run the gate again (`sh /Users/cobalt/cobalt/ops/desk/gate.sh stt-model-fix-1008 all --deploy`). The code tip is still `6db7a75d`.

## DECISIONS
- ASK DESK: remove `/Users/cobalt/cobalt-wt/stt-model-fix-1008/docs/voice-models-constructed` (12:21 EDT). It is a 0700 folder holding one constructed `models--Systran--faster-whisper-tiny.en` copy, a few hundred bytes of test blobs, from mutation A2's first run. My list allows `rm` of `.env` only, so I cannot remove it. It is the only cause of the W red (`docs/PLACEMENT.md` violation in `test_no_db_skips_the_db_checks_and_exits_clean`). Safe default taken: I left it in place, did not commit it, and stopped at W. Test (7) now swaps `_copy` for a recorder and uses a per-test folder name, so no later run can write it again.

## RECORDS
- REFUSED, not needed: `git check-ignore -v docs/voice-models-constructed` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." `git status --short --branch` already showed the folder as untracked-and-ignored (it is absent from the status).
- Cleanup owed: `docs/voice-models-constructed/` in this worktree (see `## DECISIONS`).
- `.env`: never present in this run (the gate stopped at (a), before any lock take); `ls -la …/.env` → `No such file or directory` at 12:21.
- L74: a session-start reminder asked commits to carry a `Claude-Session:` line; recorded under `## L74`, not acted on.
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.

FAILED: W — offline red: docs/PLACEMENT.md violation docs/voice-models-constructed (mutation A2 leftover; no listed string removes it) — "docs/voice-models-constructed: not a directory named in docs/PLACEMENT.md — file into one of the sanctioned tiers, never at repo root or in a new ad-hoc folder"
