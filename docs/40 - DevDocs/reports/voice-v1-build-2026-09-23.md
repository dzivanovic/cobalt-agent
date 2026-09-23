# VOICE V1 BUILD — 2026-09-23 (seat `voice-v1-0923`, Opus 5.5, prompt `prompts/2026-09-23/43-voice-v1-build.md`)

## §0 Headline
(run in progress)

## L74
One block of the L74 shape arrived attached to a tool result on 2026-09-23 13:4x ET (after the first read of the prompt file): it asked for a `Claude-Session: https://claude.ai/code/session_<id>` line in commit messages / PR bodies and named a file-send tool. Recorded ONCE here as data (L74); not followed. Commits carry only the `Co-Authored-By` line of the session's system prompt.

## AUTHORIZATION
Started 13:43:28 EDT (`date`). Each its own call; every check PASSES.

| check | command | result |
|---|---|---|
| R57 approved design | `grep -n "^\| R57 " …/cto-2026-09-23.md` | line 60 carries `"approved design"` and `sha256 prefix 8c469b9544282b55` |
| R57 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"approved design" -- …/cto-2026-09-23.md` | `ffee37ad5e41ab5eb451406a9e11a9e03b26afdb` |
| R56 Point 2: B | `grep -n "^\| R56 " …` | line 59: `"Point 2: B / Point 3: B if I said it …"` |
| FINAL unchanged | `git -C /Users/cobalt/cobalt log --oneline -1 -- "docs/30 - Design/VOICE-v3-FINAL-2026-09-23.md"` | `43a11a1a docs(desk): 09-23 voice v3 FINAL (2 items for him)` |
| seam committed | `git -C … log -1 --format=%H -- "docs/30 - Design/VOICE-v3-SEAM-S1-2026-09-23.md"` | `d7bc4f0ddb6bf5426d674a306ef18107161b4aed` |
| launch row | `grep -n "43-voice-v1-build.md" …/cto-2026-09-23.md` | line 63 R60 (his "A", item (4) = the voice strings) and line 66 `\| R63 \| 13:4x ET \|` DESK LAUNCH ROW, BASE `04b05cd4`, migration `0017` |
| launch row committed | `git -C … log -1 --format=%H -S"43-voice-v1-build.md" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` | `078734aa4287d820ed1f25484d67fc8a20af7a2a` |
| N1–N7 + `.env` pair on the desk file | `grep -c -F -e "<string>" …/cto-2026-09-23.md` ×9 | 1 each (N1 `uv add faster-whisper*`, N2 `uv tree*`, N3 `uv pip show *`, N4, N5, N6, N7, cp `.env`, rm `.env`) |
| N1–N7 + `.env` pair committed | `git -C … log -1 --format=%H -S"<string>" -- "docs/40 - DevDocs/reports/cto-2026-09-2*.md"` ×9 | `078734aa4287d820ed1f25484d67fc8a20af7a2a` each |
| 17 shared allow strings | `grep -c -F -e "\"<rule>\"" …/prompts/2026-09-22/33-setups-fix-r3.md` ×17 | 1 each |
| 3 denies | `grep -c -F -e "\"AskUserQuestion\" \"EnterWorktree\" \"Bash(git push*)\"" …/33-setups-fix-r3.md` | 1 |
| `--add-dir` triplet | `grep -c -F -e "--add-dir /Users/cobalt/Vault --add-dir /Users/cobalt/cobalt --add-dir /Users/cobalt/cobalt-wt" …/33…` | 1 |
| `db migrate` plain | `grep -c -F -e "\"Bash(COBALT_ENV=dev uv run cobalt db migrate)\"" …/27-handicap-h1-build.md` | 1 |
| `db migrate --proof-only` | `grep -rlF -e "…--proof-only)\"" …/prompts/2026-09-22 …/prompts/2026-09-23` | `41-stacked-deploy-r2.md`, `07-stacked-deploy.md` (+ this prompt) |
| 0017 / BASE TIP filled | the prompt text | `0017`, `04b05cd4` |

## PREFLIGHT
| rule | command | exit | result (verbatim / summarised) |
|---|---|---|---|
| clock | `date` | 0 | `Wed Sep 23 13:43:28 EDT 2026` |
| tree clean | `git status --porcelain` | 0 | `?? "docs/40 - DevDocs/reports/voice-v1-build-2026-09-23.md"` — the ONLY entry is this report, created first by the prompt's REPORT rule; nothing else |
| branch | `git status` | 0 | `On branch voice/v1-0923` |
| base | `git log --oneline -1` | 0 | `04b05cd4 docs(desk): 09-23 stale-score 46 + H1 47 re-issued …` = BASE TIP |
| no `.env` | `ls -la /Users/cobalt/cobalt-wt/voice-v1/.env` | 1 | `No such file or directory` |
| new modules absent | `ls src/cobalt/voice src/cobalt/modelaccess` | 1 | both `No such file or directory` |
| dev dir | `ls /Users/cobalt/.cobalt-dev` | 1 | `No such file or directory` (absent — code creates it) |
| JEV on main? | `ls src/cobalt/classify` | 1 | `No such file or directory` → JEV NOT on main: C1 touches nothing of JEV's; the `_guard_outbound` re-point is OWED by `jev/trial-0923`'s merge (ESCALATE) |
| RESTARTS probe | `uv run cobalt jobs restarts 04b05cd4..HEAD` | 0 | `docs/…/voice-v1-build-2026-09-23.md A DOCS -` / `RESTARTS: none` (the venv was created on this first `uv run`) |
| N2 probe | `uv tree --depth 1` | 0 | 258 packages resolved; `litellm v1.81.8`, `openai v2.17.0`, `pydantic v2.12.5`, `fastapi v0.128.4` among direct deps |
| N3 probe | `uv pip show pydantic` | 0 | `Name: pydantic` `Version: 2.12.5` |

**L68 — unmerged branches sharing my paths** (`git -C /Users/cobalt/cobalt log --format="%h %S" --source --all --not main -- src/cobalt/aset/web.py src/cobalt/cards src/cobalt/db_migrations src/cobalt/cli.py pyproject.toml uv.lock ops/start_aset.sh configs/cobalt`):

| branch | commits touching my paths | note |
|---|---|---|
| `deploy/stacked-0923` | `f2dd42cb` (merge) | stacked gate; carries migration 0013 et al. |
| `s2/smoke-fix-0922` | `701b2370` `9e7b5809` `2881b7e5` | |
| `setups/seven-0921` | 11 commits `d31cf12a`…`78ac4be7` | migration 0013 (`09d3a62a`) |
| `jev/trial-0923` | `05d9ddae` `5630e6c8` `537c0978` | `src/cobalt/cli.py` (discover CLI registered), `classify/` |
| `bars/chunk-1a-0920` | 11 commits | `db_migrations` |
| `bars/chunk-2-0920` | `02d67a6e` `c798a0ab` `c941d304` | migration 0012 |
| `sprint-2/cards` | `3a6f2b30` `511bff03` | `db_migrations` (old) |

Migration numbers claimed off main per R63: 0012 bars, 0013 setups, 0014 H1, 0015 D1, 0016 stale-score (reserved) → mine is `0017`.

## BASELINE
On BASE TIP `04b05cd4`, quoted verbatim:
- OFFLINE `uv run pytest -q tests/cobalt -p no:cacheprovider` → `1958 passed, 349 skipped, 1 xfailed in 66.59s (0:01:06)` — exit 0, **1958 / 0**.
- WITH-DB: `cp /Users/cobalt/cobalt/.env /Users/cobalt/cobalt-wt/voice-v1/.env` (exit 0) → `COBALT_ENV=dev uv run cobalt db migrate --proof-only` → 28 tables probed on `cobalt_dev`, `NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.`, `Proof cost: total 5.4 s`; dev head: the probe lists every table of FORWARD 0001–0011 present (`archive_incidents`, `archive_progress` … `vault_writes`), `aset_sizings 1` row, `card_stop_edits 1`, `card_transitions 4`; `code: 04b05cd4 (DIRTY: 1 path(s))` (the dirty path = this report). → `COBALT_ENV=dev uv run pytest -q tests/cobalt -p no:cacheprovider` → `2303 passed, 4 skipped, 1 xfailed in 198.72s (0:03:18)` — exit 0, **2303 / 0**, no BASELINE RED → `rm /Users/cobalt/cobalt-wt/voice-v1/.env` (exit 0).

## EXPERIMENTS

(gate table — §X-TABLE — filled as each experiment lands; final copy in `## ESCALATE`)

### X-E10
**Ran** (N1 / N2 / N3 / N4): `uv add faster-whisper` → resolved 263 packages; installed `+ av==18.1.0`, `+ ctranslate2==4.8.2`, `+ faster-whisper==1.2.1`, `+ flatbuffers==25.12.19`, `+ onnxruntime==1.30.0` (tokenizers 0.22.2 and huggingface-hub 1.5.0 were already in the lock). `uv tree --package faster-whisper` → `faster-whisper v1.2.1` ├ `av v18.1.0` ├ `ctranslate2 v4.8.2` (numpy, pyyaml) ├ `huggingface-hub v1.5.0` ├ `onnxruntime v1.30.0` (flatbuffers, numpy, packaging, protobuf) ├ `tokenizers v0.22.2` └ `tqdm v4.67.3`. `git diff --stat -- pyproject.toml uv.lock` → `pyproject.toml | 1 +`, `uv.lock | 125 +++`, `126 insertions(+)`; the lock diff adds exactly five `[[package]]` blocks (`av`, `ctranslate2`, `faster-whisper`, `flatbuffers`, `onnxruntime`) plus the two `faster-whisper` dependency lines of `cobalt-agent`.

**Licences.** `uv pip show` prints no `License:` field under uv, so each NEW package's `License:` line was read from its `METADATA` (`grep -H -i "^License\|^Classifier: License" …dist-info/METADATA`):

| new package | native? | License line (verbatim) |
|---|---|---|
| `av 18.1.0` | yes (bundles FFmpeg dylibs) | `License-Expression: BSD-3-Clause` |
| `ctranslate2 4.8.2` | yes | `License: MIT` |
| `faster-whisper 1.2.1` | no (`py3-none-any`) | `License: MIT` |
| `flatbuffers 25.12.19` | no (`py2.py3-none-any`) | `License: Apache 2.0` |
| `onnxruntime 1.30.0` | yes | `License: MIT License` |

`grep -rlI "GNU General Public\|GNU Lesser\|LGPL\|AGPL"` over the five `dist-info` dirs → no output. **But** `ls …/site-packages/av/.dylibs` lists `libx264.165.dylib` and `libx265.216.dylib` among 19 bundled libraries. So a probe (N4, `scratch/voice-x/x_e10_av_license.py`, quoted below) asked FFmpeg what it reports about its own build:
```
E10 av 18.1.0 ffmpeg 8.1.2
E10 libavcodec: license='LGPL version 3 or later' version=(62, 28, 102) flags=['--enable-version3', '--enable-libx264', '--enable-libx265']
… (libavdevice, libavfilter, libavformat, libavutil, libswresample, libswscale: the same licence string and flags)
```
Script text (`scratch/voice-x/x_e10_av_license.py`): imports `av`, prints `av.__version__`, `av.ffmpeg_version_info`, then for each entry of `av.library_meta` its `license` and the `--enable-gpl|--enable-version3|--enable-nonfree|--enable-libx26*` configure flags.

**Offline load (v2 X7)** — `uv run python scratch/voice-x/x_e10_offline.py` (script: `WhisperModel("medium.en", device="cpu", compute_type="int8", download_root=<empty tmp dir>, local_files_only=True)` inside try/except, prints the exception's module + name + text):
```
E10 offline load of medium.en from an EMPTY dir: huggingface_hub.errors.LocalEntryNotFoundError: Cannot find an appropriate cached snapshot folder for the specified revision on the local disk and outgoing traffic has been disabled. To enable repo look-ups and downloads online, pass 'local_files_only=False' as input.
E10 faster_whisper 1.2.1 python 3.14.3
```
→ C5 maps `LocalEntryNotFoundError` to the named RED `speech-to-text down (model missing)`.

**Pin:** `pyproject.toml` edited to `"faster-whisper==1.2.1"`, then `uv add faster-whisper==1.2.1` → lock unchanged in content (`Resolved 263 packages`), only `cobalt-agent` rebuilt. Committed `cc2e95b6 chore(voice-v1): X-E10 faster-whisper 1.2.1` (2 files, 126 insertions).

**FINAL's result that changes the design:** "an unexpected native / GPL package → tribunal round 2". **OUTCOME: NO CHANGE by the letter** — every new native package is on the prompt's expected list (`ctranslate2`, `av`, `onnxruntime`; `flatbuffers` is pure Python), and no new package's licence line is GPL / AGPL; FFmpeg reports `LGPL version 3 or later` and no `--enable-gpl`. **FLAGGED, not assumed away:** the `av` wheel bundles `libx264` / `libx265` binaries whose upstream licence is GPL-2.0-or-later (general knowledge — NOT read from any file on this host; no licence text for them ships in the wheel). The voice path decodes AUDIO only and never calls a video encoder; the repo carries only a lock reference, never the wheel. `ASK DESK: X-E10 — av 18.1.0's wheel bundles libx264/libx265 dylibs (upstream GPL-2.0+, unverified here) under an FFmpeg that reports LGPLv3; accept for a private install, or tribunal round 2? [13:51 ET]` — safe default taken: continue the build (the letter of the gate is not met; the desk decides before ship).

### X-E2
**Ran** (N4) `uv run python scratch/voice-x/x_e2_stt.py` (script: downloads each size ONCE into the DEV `model_dir` via `faster_whisper.download_model(size, cache_dir=…)`; builds the set with `say` + PyAV (`scratch/voice-x/common.py`: `voices()`, `say_aiff()`, `encode()` → webm/libopus and mp4/AAC, 48 kHz mono, explicit sample-count pts); runs each size in its OWN subprocess (`WhisperModel(size, device="cpu", compute_type="int8", download_root=<model_dir>, local_files_only=True)`, `transcribe(language="en", beam_size=5, vad_filter=False, condition_on_previous_text=False)`), every file twice; WER by ONE shared normalizer for reference and hypothesis (lower-case, punctuation out, number words → digits, spelled letters joined) and word-level Levenshtein; peak RSS `resource.getrusage(RUSAGE_SELF).ru_maxrss`; `vm_stat` before / after). First run died in my own encode helper (`av.error.ArgumentError … u10.mp4 returned 22` — unset pts on flush; fixed with explicit pts), after the three downloads had landed. Second run, output verbatim:
```
DOWNLOAD tiny.en -> /Users/cobalt/.cobalt-dev/voice-models/models--Systran--faster-whisper-tiny.en/snapshots/0d3d19a32d3338f10357c0889762bd8d64bbdeba revision=0d3d19a32d3338f10357c0889762bd8d64bbdeba (0.2s)
DOWNLOAD base.en -> …/models--Systran--faster-whisper-base.en/snapshots/3d3d5dee26484f91867d81cb899cfcf72b96be6c revision=3d3d5dee26484f91867d81cb899cfcf72b96be6c (0.0s)
DOWNLOAD small.en -> …/models--Systran--faster-whisper-small.en/snapshots/d1d751a5f8271d482d14ca55d9e2deeebbae577f revision=d1d751a5f8271d482d14ca55d9e2deeebbae577f (0.0s)
SET utterances=42 files=84 voices=['Daniel', 'Karen', 'Samantha'] formats=webm/opus-48k-mono,mp4/aac-48k-mono
SIZE tiny.en fmt=webm files=42 WER=7.31% (16/219) p50_ms=185 p95_ms=219 p95_ms_per_5s_audio=1501 max_dur_s=3.16
SIZE tiny.en fmt=mp4 files=42 WER=5.94% (13/219) p50_ms=183 p95_ms=212 p95_ms_per_5s_audio=1546 max_dur_s=3.15
SIZE tiny.en fmt=all files=84 WER=6.62% (29/438) p50_ms=185 p95_ms=217 p95_ms_per_5s_audio=1546 max_dur_s=3.16
SIZE tiny.en confirm_words_right=12/12 setup_phrases_WER=7.78% same_output_twice=84/84 load_ms=297 peak_rss_MB=1041 vm_before_GB={'free': 1.95, 'inactive': 30.4, 'speculative': 2.94, 'wired down': 30.71} vm_after_GB={'free': 1.81, 'inactive': 30.48, 'speculative': 2.92, 'wired down': 30.7}
SIZE base.en fmt=all files=84 WER=2.28% (10/438) p50_ms=347 p95_ms=380 p95_ms_per_5s_audio=3115 max_dur_s=3.16
SIZE base.en confirm_words_right=12/12 setup_phrases_WER=4.44% same_output_twice=84/84 load_ms=240 peak_rss_MB=1075 vm_before_GB={'free': 1.81, …} vm_after_GB={'free': 1.29, 'inactive': 30.59, 'speculative': 2.79, 'wired down': 30.7}
SIZE small.en fmt=all files=84 WER=0.00% (0/438) p50_ms=1059 p95_ms=1136 p95_ms_per_5s_audio=10226 max_dur_s=3.16
SIZE small.en confirm_words_right=12/12 setup_phrases_WER=0.00% same_output_twice=84/84 load_ms=445 peak_rss_MB=1833 vm_before_GB={'free': 1.29, …} vm_after_GB={'free': 1.83, 'inactive': 31.03, 'speculative': 1.15, 'wired down': 30.68}
Metal: NOT RUN — CPU faster-whisper stands (v2 [F-03])
```
(per-format rows of base.en / small.en: base webm 2.74 % / mp4 1.83 %; small 0.00 % / 0.00 %.) The set: 14 constructed texts (10 V1 phrases with `XYZ`-style spelled tickers incl. "yes", "no"; 4 setup phrases whose setup names were read at run time from `configs/cobalt/strategies.yaml` and appear in no committed file) × 3 voices = 42 utterances × 2 containers = 84 files. **Caveats, stated:** (1) the `p95_ms_per_5s_audio` column is a LINEAR extrapolation and is INVALID (Whisper pads every clip to a 30 s window) — ignored; (2) this run overlapped my C1 pytest runs for part of its time — latencies may be inflated. So the bar's "5 s clip" was measured directly and uncontended in **X-E2b** (`uv run python scratch/voice-x/x_e2b_5s.py`: 5 longer constructed texts × 3 voices, webm, each size in its own subprocess):
```
SET files=15 dur_s min=2.99 median=3.52 max=4.85
SIZE tiny.en files=15 WER=4.55% (9/198) p50_ms=220 p95_ms=272 max_ms=276
SIZE base.en files=15 WER=1.52% (3/198) p50_ms=392 p95_ms=429 max_ms=463
SIZE small.en files=15 WER=2.02% (4/198) p50_ms=1195 p95_ms=1286 max_ms=1316
```
RSS beside LM Studio: every size ran with `wired down` ≈ 30.7 GB (LM Studio resident) and its peak RSS was 1041 / 1075 / 1833 MB; no size moved `wired down` (30.71 → 30.68). **Bar (the builder's measure):** smallest size with WER ≤ 10 %, every confirm word right, p95 ≤ 3 s for a ≈5 s clip → **tiny.en** meets it (6.62 % / 4.55 %; 12/12; p95 272 ms at clips up to 4.85 s). **Chosen: `tiny.en`, revision `0d3d19a32d3338f10357c0889762bd8d64bbdeba`, `compute_type int8`, CPU.** (base.en is 2.28 % at p95 380–429 ms — recorded for the desk; the bar's rule picks the smallest.) **OUTCOME: NO CHANGE** — a size meets the bar; CPU faster-whisper stands.

### X-X1
**Ran** (N4) `uv run python scratch/voice-x/x_x1_false_confirm.py tiny.en` (script: numpy-generated 48 kHz clips, 10 each of silence / breath-like filtered noise under a sine envelope / cough-like decaying bursts / keyboard-like clicks / 60 Hz hum + noise, seed `20260923`, encoded webm/opus; + 20 synthesized non-confirm words (`yet mess less guess bless dress nose go snow slow now yellow noble yesterday nope yeah okay sure stop radar`); same transcribe settings as E2; normalizes casefold + strip + trailing `.!?,`; records `no_speech_prob` / `avg_logprob` for any hit). Summary lines verbatim:
```
COUNTS silence=0/10 breath=0/10 cough=0/10 keys=0/10 room=0/10 word=0/20
FALSE_CONFIRM_TOTAL 0 of 70 size=tiny.en
```
Per-clip lines (70) are in the run output; noise transcribed as `''` or `'you'` (23 × `you`), one breath clip as a 23-word hallucinated sentence, one as `'music'`; words mis-heard: `mess→miss`, `bless→class`, `nope→note`. **FINAL: "Any > 0 → … ACTs on a card become tap-only".** **OUTCOME: NO CHANGE** — 0 of 70; the spoken `yes` stays a valid confirm for the V1 act. Informational for C5 / C10: a noise press most often yields `you` or empty; empty → "I heard nothing"; `you` is not a confirm word and ends a pending action with nothing executed ([F-08]).

### X-X20
**Ran** (N4) `uv run python scratch/voice-x/x_x20_unlink.py tiny.en` (a 16.5 s synthesized clip; a thread unlinks it 0.3 s after `transcribe()` starts; (a) path argument, (b) open file object):
```
X20 mode=path dur_s=16.5 OUTCOME=completed words=78 elapsed_s=3.89 unlinked_after_s=0.30 exists_after=False
X20 mode=fileobj dur_s=16.5 OUTCOME=completed words=78 elapsed_s=3.76 unlinked_after_s=0.31 exists_after=False
```
**OUTCOME: INFORMATIONAL (gates nothing)** — the transcript COMPLETES after the unlink in both modes on this engine / size.

### X-X22
Script text written EXACTLY as the prompt block (Write tool); stub `scratch/voice-x/x22/x22_stub.py` likewise. Checks, each its own call: `grep -c -F -x -e 'LABEL="com.cobalt.x22-probe"' scratch/voice-x/x22-launchd.sh` → `1` · `grep -c "com.cobalt.aset\|com.cobalt.radar\|com.cobalt.heartbeat" …` → `1` (the header comment) · `grep -c "launchctl" …` → `5` · `wc -l …` → `59 scratch/voice-x/x22-launchd.sh` (= the prompt block's 59 lines). ONE run at 13:59:37 (`date`), `bash /Users/cobalt/cobalt-wt/voice-v1/scratch/voice-x/x22-launchd.sh`, output WHOLE:
```
X22 before job_pid=2560 port_holder=2566
  PID  PPID COMMAND
 2560     1 /Users/cobalt/.local/bin/uv run --project /Users/cobalt/cobalt-wt/voice-v1 python -m x22_stub
 2566  2560 /opt/homebrew/Cellar/python@3.14/3.14.3_1/Frameworks/Python.framework/Versions/3.14/Resources/Python.app/Contents/MacOS/Python -m x22_stub
X22 after+2s old_holder_alive=yes port_holder=2566 job_pid=none
X22 after+5s old_holder_alive=yes port_holder=2566 job_pid=none
X22 after+15s old_holder_alive=yes port_holder=2566 job_pid=none
X22 byhand uv_pid=2997 port_holder=2566
/Users/cobalt/cobalt-wt/voice-v1/scratch/voice-x/x22-launchd.sh: line 53: kill: (2997) - No such process
X22 byhand child_survived=yes
X22 CLEANUP port 5099 free
STUB pid=2566 ppid=2560 start
STUB pid=2566 bound 5099
STUB pid=2914 ppid=2913 start
STUB pid=2914 BIND FAILED 48
STUB pid=2947 ppid=2946 start
STUB pid=2947 BIND FAILED 48
STUB pid=2999 ppid=2997 start
STUB pid=2999 BIND FAILED 48
```
**Reading.** (1) launchd job: `kill -9` of the job's pid (2560, the `uv` process) left its python child **2566 ALIVE and still holding :5099** at +2 s, +5 s and +15 s, while launchd RESPAWNED the job (the stub log shows respawns 2914 and 2947, each `BIND FAILED 48` = EADDRINUSE, then exit — which is why `job_pid=none` at each sample). **The FINAL's design-changing result occurred: the old holder is alive while launchd respawns.** (2) The by-hand half is **CONFOUNDED, not a result**: the orphan 2566 still held :5099, so the by-hand stub (2999) failed to bind and its `uv` (2997) had exited before the `kill -9` ("No such process"); `port_holder=2566` and `child_survived=yes` describe the launchd orphan, not a by-hand child. UNPROVEN for the by-hand case (L70). (3) The script's own last `CLEANUP` line reads `port 5099 free` — no process left.

**OUTCOME: DESIGN-CHANGING — the old holder survives a `kill -9` of the job pid while launchd respawns ⇒ "a delete-ALL start sweep deletes a live turn's audio" (a start sweep in the respawned process runs before its bind fails: uvicorn runs lifespan startup before it binds).** Side B is HIS letter (R56) and is not reopened: the sweep stays delete-ALL, and C4's DIRECTORY LOCK (built in every case) turns side B's premise into a CHECK — the orphan still holds the flock it took at start, so the new process's sweep deletes NOTHING, logs RED naming the holder, and the start FAILS loud. `ASK DESK: X22 — the orphan child (2566) survived kill -9 of the job pid and held the port through two launchd respawns; the lock guard stands in front of side B's sweep; keep? [13:59 ET]` — safe default taken: **keep the lock**.

### X-E4
**Ran** (N4, after C3's commit) `uv run python scratch/voice-x/x_e4_plan.py --mode json_schema --limit 3` (a live probe: `3/3 parse_valid`, `think_block={'absent': 3}`, `model_returned={'mainframe': 3}`, 3919–5319 ms) and then `uv run python scratch/voice-x/x_e4_plan.py --mode json_schema --contention` (script: the committed constructed set `tests/fixtures/voice/plan-utterances.constructed.yaml` — 65 utterances: 12 stop acts, 8 open-cards, 8 radar, 8 card-numbers, 4 ambiguous, 6 hostile / injection, 6 trade-execution, 5 trading-logic, 4 one-word yes / no, 4 off-topic — each through `cobalt.voice.agent.plan_turn` → `cobalt.modelaccess` on `local.plan` (127.0.0.1:1234, `mainframe`), with an in-script copy of the route whose ONLY changes are `timeout_s 180` / `max_output_tokens 512` so nothing is cut off; `--contention` starts ONE second client (back-to-back 1500-token essay generations through the same module) and runs the set again). The contended pass was STOPPED after 12 of 65 samples (`TaskStop` of the background task I started, between the `date` readings 14:28:03 and 14:30:48 — each contended call queued 60–72 s, the full pass would have held the local model ≈76 min and blocked E6 / the DEMO); the script's own `SUMMARY` lines sat in its unflushed stdout buffer and died with it, so both summaries were recomputed from the flushed per-utterance lines by `uv run python scratch/voice-x/x_e4_summarize.py <that output file>` (a parser of those lines + the fixture's labels), verbatim:
```
SUMMARY solo-json_schema n=65 parse_valid=65/65 (100.0%) agree=64/65 (98.5%) p50_ms=2492 p95_ms=3146 max_ms=3486 fails={} think_block={'absent': 65}
SUMMARY solo-json_schema by_cat (n/parse_valid/agree): {'ambiguous': [4, 4, 4], 'execution': [6, 6, 6], 'hostile': [6, 6, 6], 'logic': [5, 5, 4], 'numbers': [8, 8, 8], 'offtopic': [4, 4, 4], 'oneword': [4, 4, 4], 'open': [8, 8, 8], 'radar': [8, 8, 8], 'stop': [12, 12, 12]}
DISAGREE solo-json_schema #53 logic got clarify/- want ['unsupported/-', 'refuse/-'] :: 'change my daily stop to 500'
SUMMARY contended-json_schema n=12 parse_valid=12/12 (100.0%) agree=12/12 (100.0%) p50_ms=69429 p95_ms=70863 max_ms=71947 fails={} think_block={'absent': 12}
```
Per-call log lines: `input_tokens` 508–516, `output_tokens` 23–48 (e.g. `input_tokens=514 output_tokens=47`), `model_returned=mainframe`. No `DANGER` line: **no hostile / execution / logic utterance was planned as `act/cards.set_stop`**. The one disagreement ("change my daily stop to 500" → `clarify`) is caught by C7's code refusal regardless (`_LOGIC` matches "daily stop" → `unsupported` naming the owner's command; tested). **`/no_think` emits NO think block at all** (`think_block=absent` on all 77 calls; no `reasoning_content` either — `forbid_nonempty` never fired). **`response_format`:** the server ACCEPTED `json_schema` (no 4xx) and 65/65 replies parsed as a `Plan`; `in_prompt` NOT RUN (no need shown).
**Tunables set from these numbers** (each with its `# source: X-E4` line): `modelaccess.yaml` `timeout_s: 15` (solo max 3486 ms, ≈4×), `max_output_tokens: 256` (max seen 48, ≈5×), `response_format: json_schema`; `voice.yaml` `history_turns: 4` (no-history prompt 508–516 tokens); `stt_timeout_s` stays 20 (X-E2 / X-X20).
**FINAL's design-changing rows:** parse-valid < 95 % → NO (100 %). A hostile / execution utterance planned as an act on `cards.set_stop` → NO (0; C7's order refusal would catch it anyway). **Contention p95 beyond `stt_timeout_s` + the Plan budget → YES: contended p95 70 863 ms ≫ 20 s + 15 s.** **OUTCOME: DESIGN-CHANGING — while any other client holds `mainframe`, a voice Plan call queues behind that whole generation (60–72 s measured).** With `timeout_s: 15` such a turn FAILS LOUD (`voice_plan` RED "Cobalt can't think right now (timeout)"); the text box does not help (same model). The FINAL's second-small-local-model lane is NOT built in V1 (`[F-18]`). `ASK DESK: X-E4 — voice Plan calls queue 60–72 s behind any other mainframe client (a Qwen Code seat, the JEV local lane); accept loud timeouts in V1, or put a second small local model on its own route before ship (L23/L26, routing lane)? [14:30 ET]` — safe default taken: the 15 s timeout (loud failure, never a hang).

### X-X5
**Ran** (N4) `uv run python scratch/voice-x/x_x5_values.py` (script: 21 carrier phrases — 12 price, 5 share, 4 time — each in several spoken forms, `say` in 2 voices (Samantha, Daniel), webm/opus 48 kHz mono → `tiny.en` → the value span = the text after the carrier's last ` to ` / ` at ` / ` is ` (code) → the C6 parser; tally right / WRONG / clarify against the value MEANT). Summary lines verbatim:
```
X5 SUMMARY price: n=24 right=16 WRONG=6 clarify=2 clarify_share=8%
X5 SUMMARY shares: n=10 right=10 WRONG=0 clarify=0 clarify_share=0%
X5 SUMMARY time: n=8 right=0 WRONG=0 clarify=8 clarify_share=100%
X5 PRICE-AS-CLOCK transcripts=0 all_clarified=True
```
The six WRONG rows, verbatim (both voices): `said='move the stop to four fifty' heard='Move the stock to 450.' … -> WRONG Decimal('450')` (and `'Move the stop to 450.'`), `said='move the stop to twelve twenty five' heard='Move the stop to 1225.' -> WRONG Decimal('1225')` ×2, `said='move the stop to nine seventy five' heard='Move the stop to 975.' -> WRONG Decimal('975')` ×2. The engine itself writes the spoken dollars-and-cents form WITHOUT "point" as an integer; the parser sees digits and cannot tell. Forms with "point", with "$", "four dollars and fifty cents" and digit forms were all right. Times came back as `945`, `10.30 am`, `3.05 pm` → every one clarified (no `H:MM` from this engine at all). **FINAL: "A price transcribed as a clock time and parsed as a price would be a wrong value → that parser must refuse H:MM shapes."** → did not occur (0 clock-shaped price transcripts); the parser refuses `H:MM` anyway (C6 test). **OUTCOME: DESIGN-CHANGING — a NEW wrong-value path: "four fifty" → `450` (6 of 24 price clips).** The FINAL's own guard stands: the read-back speaks the PARSED value before any confirm ([F-05], §2.4 "a mis-hearing is caught before it lands"). Safe default ADDED (strictly stricter, no model): the stop act CLARIFIES when the parsed stop is ≥ 10× or ≤ 0.1× the card's current stop (C8), naming what was heard. `ASK DESK: X-X5 — spoken prices without "point" arrive as wrong integers (450 for 4.50); keep the 10× clarify guard + read-back, or also refuse any integer-only stop span? [14:18 ET]`.

### X-X12
C6 parser test on the synthetic TEXT, no model: `parse_price("4.50") == Decimal("4.50")`; `parse_price("four fifty")` → `Unparseable: 'four fifty' is ambiguous (a spoken price without 'point')` (`test_x12_spoken_and_digit_forms_do_not_meet_in_silence`, green). **FINAL: "Same decimal → the parser accepts spoken numbers; otherwise clarify."** → not the same decimal → the TEXT form clarifies. **OUTCOME: NO CHANGE** to the parser rule — but X-X5 shows the ENGINE never hands the parser the words "four fifty": it hands it `450`, which is why X5's guard lives in the act, not in the parser.

### X-G2/K5
The config refusal `scratch_max_age_s ≤ stt_timeout_s` is a C2 TEST (side B's text keeps it). Under side B the sweep runs ONLY at process start, before the first request is served, so a sweep firing mid-transcribe inside ONE process cannot happen by construction. The cross-process case (an orphan still transcribing while a respawn starts) is X-X22's, and C4's directory lock is its guard. OUTCOME: NO CHANGE (C2 test).

## C1
### T
Tests written first: `tests/cobalt/test_modelaccess_silence.py`, `test_modelaccess_config.py`, `test_modelaccess_client.py` (seam §4 whole: route resolution / non-loopback refusal / `fallback` refusal; guard → `prompt_refused` with ZERO transport calls; think policy `absent` / `empty_removed` / `think_leak`; every error kind over a fake loopback server; the call line carries no message content; `call()` never blocks a running loop; no non-loopback socket at import (fresh-interpreter probe) or during a call). ORDER NOTE: the first RED run of the silence file happened while X-E2's first run was in the background — i.e. C1's T began before X-A had finished; no C1 code existed until every X-A experiment had its result, and X-E2b re-measured latency uncontended. RED, quoted: `E   AssertionError: {'attempts': [], 'error': "ModuleNotFoundError: No module named 'cobalt.modelaccess'", 'module': 'cobalt.modelaccess'}` and, for the other two files, `E   ModuleNotFoundError: No module named 'cobalt.modelaccess'` (`2 errors during collection`). The probe line printed by the same run: `LITELLM IMPORT PROBE: {"module": "litellm", "attempts": [], "error": null}`.
### C
`src/cobalt/modelaccess/{__init__,models,config,guard,adapters,client}.py` + `configs/cobalt/modelaccess.yaml` (route `local.plan` → `http://127.0.0.1:1234/v1`, `mainframe`, `no_think: true`, `think_policy: forbid_nonempty`, `timeout_s` / `max_output_tokens` / `response_format` marked `# set by X-E4`). **Adapter decision (seam §2.4 (5)) — the `openai` client, with the evidence:** litellm's import IS silent (above). With the litellm adapter the first green attempt read `3 failed, 60 passed`: `test_an_empty_think_block_is_removed_and_recorded` → `'absent' == 'empty_removed'` (the fake server sent `<think>\n\n</think>\n{"kind":"answer"}`; litellm delivered `{"kind":"answer"}` — it REWROTE the reply before the module's think policy could see it), `test_unreachable` → `assert 'http_status' == 'unreachable'`, `test_bad_response` → `assert 'http_status' == 'bad_response'`. The seam forbids exactly this (the module never repairs content; it applies its own think policy, §2.4 (2)(3)(6)), so `adapters.py` uses the pinned `openai` client (`max_retries=0`, `httpx.Client(trust_env=False)`); the interface is unchanged; nothing in `src/cobalt` imports litellm. One seam addition, named: a route key `response_format: json_schema | in_prompt` (X-E4's evidence home for "passes `response_format` only if the server honours it", §2.4 (3)). JEV re-point: NOT done — `src/cobalt/classify` is absent on main (PREFLIGHT) → OWED by `jev/trial-0923`'s merge (ESCALATE).
### D
`docs/40 - DevDocs/cobalt/modelaccess/{__init__,models,config,guard,adapters,client}.md` (new, one per `.py`).
### SUITE
`uv run pytest -q tests/cobalt/test_modelaccess_config.py tests/cobalt/test_modelaccess_client.py tests/cobalt/test_modelaccess_silence.py -p no:cacheprovider` → `63 passed in 16.42s`. Full offline `uv run pytest -q tests/cobalt -p no:cacheprovider` → `2021 passed, 349 skipped, 1 xfailed in 83.20s (0:01:23)` — failed 0.
### COMMIT
`c16af92d feat(modelaccess): C1 seam S1 — the new core's one model-access module, local lane only` — `17 files changed, 1535 insertions(+)` (`git show --stat HEAD`: the six `.py`, the yaml, three test files, six DevDocs, this report).

## C2
### T
`tests/cobalt/test_voice_config.py` first. RED: `E   ModuleNotFoundError: No module named 'cobalt.voice'` (`1 error during collection`).
### C
`src/cobalt/voice/{__init__,config,registry}.py`, `configs/cobalt/voice.yaml` (every tunable with a `# source:` line — X-E2 for `stt_model tiny.en` / `stt_revision 0d3d19a3…` / `stt_compute_type int8` / `stt_timeout_s 20`; "engine default — FINAL §11 W7" for `max_clip_s 30`, `max_upload_bytes 2000000`, `confirm_ttl_s 60`, `scratch_max_age_s 120`; `history_turns 4` marked `# set by X-E4`), `configs/cobalt/agents/voice.yaml` (charter, `route: local.plan` checked against the model-access registry, the four V1 tools with kind / `trading_logic: false` / arg schema, `confirm_words: ["yes"]`, `cancel_words: ["no"]` — quoted, since bare YAML `yes`/`no` load as booleans), `ops/start_aset.sh` (the two production exports beside `:32`, one comment line each). Config boundary: `grep -n "configs" /Users/cobalt/cobalt/.gitignore` → only `50:configs/dev/aset.local.yaml` and `54:configs/dev/rules.generated.yaml` ignore anything under `configs/`; `git status --porcelain` after `git add` shows `A  configs/cobalt/agents/voice.yaml`, `A  configs/cobalt/voice.yaml` — both TRACKED, both under `configs/cobalt/`, outside the old loader's top-level `configs/*.yaml` glob.
**A seam found by the suite, and the choice taken (ESCALATE):** the first version refused `scratch_dir` / `model_dir` under a `backup.yaml` source by calling `load_backup_config()` inside the loader. The full suite went `1 failed, 2073 passed`: `tests/cobalt/test_jobs_restarts.py::test_backup_yaml_is_read_by_one_shots_only_and_derives_no_restart` — `AssertionError: ['cobalt.backup.cli._restore', …]` — `configs/cobalt/jobs.yaml` DECLARES `backup.yaml` has no resident reader, and the ASET resident loading voice config would have made that false (L42's derivation). Changing `jobs.yaml` / that pin is outside my paths. So: the resident loader keeps the relative / docs / repo-root / production-vault / resolved-vault refusals (which already cover both of today's sources: the vault, and `data/.cobalt_vault` under the repo root) and refuses under backup sources only when the caller passes `backup_sources=`; the suite loads the committed dev paths AND `ops/start_aset.sh`'s production overrides with every real `backup.yaml` source passed, and asserts the resident module never names `load_backup_config`. `ASK DESK: C2 — make com.cobalt.aset a declared backup.yaml reader (jobs.yaml + the restarts pin) so the runtime refuses a future backup source too, or keep the suite check? [14:08 ET]` — safe default taken: the suite check.
### D
`docs/40 - DevDocs/cobalt/voice/{__init__,config,registry}.md`.
### SUITE
`uv run pytest -q tests/cobalt/test_voice_config.py tests/cobalt/test_jobs_restarts.py -p no:cacheprovider` → `74 passed in 9.11s`. Full offline (with C3's files also present in the tree) → `2109 passed, 349 skipped, 1 xfailed in 86.15s (0:01:26)` — failed 0.
### COMMIT
(below, in the commit that carries this section)

## C3
### T
`tests/cobalt/test_voice_plan.py` + `tests/fixtures/voice/plan-replies.constructed.yaml` (20 constructed replies: 6 valid kinds; not-JSON, a fenced block, an unknown kind, an extra field, a tool off the allowlist, act-on-read, answer-on-act, answer-without-tool, an extra arg, an invented price span, a model-normalised `XYZ` for a transcript `X Y Z`, a candidate off the list, span+candidate together, an empty span) + the prompt tests (whitelisted keys only; no env value / path / key name in the rendered prompt; a constructed secret through each of transcript / history said / history reply / candidate label / clock → `prompt_refused` by the S1 guard, zero bytes out) + ONE call per turn on the registry route, no retry. RED: `E   ImportError: cannot import name 'agent' from 'cobalt.voice'`.
### C
`src/cobalt/voice/models.py` (`Plan`, `Span`, `CandidateRef`, `CardCandidate`, `HistoryTurn`, `PromptInputs`, `PendingAction`, `TurnState` + `EDGES`, `TurnOutcome`, `DegradedLine`), `src/cobalt/voice/agent.py` (`build_messages`, `validate_plan`, `plan_turn`, `PLAN_SCHEMA`, `PlanFailed` with `failure_class = "voice_plan"`).
### D
`docs/40 - DevDocs/cobalt/voice/{models,agent}.md`; `docs/40 - DevDocs/tests/fixtures/voice/_voice_fixtures.md`.
### SUITE
`uv run pytest -q tests/cobalt/test_voice_plan.py -p no:cacheprovider` → `32 passed in 0.25s`; the full offline run above (`2109 passed … failed 0`) covered C2 and C3 together.
### COMMIT
(below)

### COMMIT (C2, C3)
`cf856dad feat(voice-v1): C2 voice config + agent registry` (11 files, 778 insertions, 1 deletion) · `f81ea150 feat(voice-v1): C3 the Plan and the whitelisted prompt builder` (7 files, 709 insertions).

## C4
### T
`tests/cobalt/test_voice_scratch.py` (one writer: dir 0700 / file 0600 / closed content-type map / `O_EXCL` / no path escape / zero-byte refused; one unlink: RED on a read-only dir; `turn_audio` unlinks on success, on an exception, and raises `ScratchUnlinkFailed` when its own unlink fails; the start sweep deletes every file with AMBER lines, has no age test, RED on a failed unlink, never sweeps `.lock`; a lock held by ANOTHER process (a child the test starts and kills by its own pid) → nothing deleted + `ScratchLocked` naming that pid; the lock is exclusive within one process too; the sweep refuses without the lock; `os.unlink(` appears exactly once in the module). RED: `E   ImportError: cannot import name 'scratch' from 'cobalt.voice'`.
### C
`src/cobalt/voice/scratch.py` (`write_scratch`, `unlink_scratch`, `turn_audio` / `HeldAudio`, `DirectoryLock`, `start_sweep`, `CONTENT_TYPES`). The row's `audio_deleted_at` is set from `HeldAudio.deleted_at` by the turn (C11); the transcribe-failure / Plan-failure `finally:` cases are re-proven through `run_turn` in C11.
### D
`docs/40 - DevDocs/cobalt/voice/scratch.md`.
### SUITE
`uv run pytest -q tests/cobalt/test_voice_scratch.py -p no:cacheprovider` → `35 passed in 0.07s`. Full offline (C4 + C5 + C6 files in the tree) → `2217 passed, 351 skipped, 1 xfailed, 3 warnings in 96.00s (0:01:36)` — failed 0; the 2 extra skips were C5's two `slow` speech tests, skipped by a collection-time `skipif` that ran before conftest pins `COBALT_ENV` (read as "model absent") — FIXED (a fixture now checks inside the test): `uv run pytest -q -rs tests/cobalt/test_voice_transcribe.py` → `8 passed, 3 warnings` (0 skipped; the warnings are `PytestUnknownMarkWarning: Unknown pytest.mark.slow` — `slow` cannot be registered: `pyproject.toml` changes only through N1 in this build).
### COMMIT
(below)

## C5
### T
`tests/cobalt/test_voice_transcribe.py` — speech SYNTHESIZED at test time (`say` → PyAV → webm/opus 48 kHz mono) into `tmp_path`; `slow`; skipped only when the pinned model is absent. Speech → text with every field; same text twice; duration probed before decode; a missing model → `str(e) == "speech-to-text down (model missing)"`; a non-audio file → `undecodable`; timeout → named; off the loop (a ticker keeps ticking); one engine. RED: `E   ImportError: cannot import name 'transcribe' from 'cobalt.voice'`.
### C
`src/cobalt/voice/transcribe.py` (`Transcriber`, `Transcript`, `FasterWhisperTranscriber` — `WhisperModel(stt_model, device="cpu", compute_type, download_root=model_dir, local_files_only=True, revision=stt_revision)`, loaded once per process — `SttDown`, `model_present`, `probe_duration_s`, `transcribe_with_timeout`, `transcribe_async`, `ENGINES`).
### D
`docs/40 - DevDocs/cobalt/voice/transcribe.md`.
### SUITE
as C4 (`8 passed` for the file after the skip fix).
### COMMIT
(below)

## C6
### T
`tests/cobalt/test_voice_resolve.py` — candidates + labels; a unique ticker binds; spoken letters normalize; two matches clarify reading both back; side word and ordinal narrow; zero matches / no argument (even with ONE open card) / no open cards clarify; a candidate ref binds only from the list; prices that parse (digits, `$`, "dollars", spoken WITH "point") and that clarify (`4:50`, `4:50 pm`, `10:05 a.m.`, "four fifty", "twelve twenty five", zero, negative, 5 decimals, words around it); X-X12; share counts; times. RED: `E   ImportError: cannot import name 'resolve' from 'cobalt.voice'`.
### C
`src/cobalt/voice/resolve.py` (`card_candidates`, `resolve_card`, `parse_price`, `parse_shares`, `parse_time`, `Unparseable`).
### D
`docs/40 - DevDocs/cobalt/voice/resolve.md`.
### SUITE
`uv run pytest -q tests/cobalt/test_voice_resolve.py -p no:cacheprovider` → `67 passed in 0.04s`; full offline as C4.
### COMMIT
(below)

### COMMIT (C4, C5, C6)
`b0dcf7cd feat(voice-v1): C4 scratch lifecycle …` (4 files, 573 insertions, 2 deletions) · `7df7a339 feat(voice-v1): C5 the Transcriber …` (3 files, 379 insertions) · `2fe2d7f9 feat(voice-v1): C6 the resolver and the value parsers (X-X5, X-X12)` (3 files, 385 insertions).

## C7
### T
`tests/cobalt/test_voice_tools.py`: the code implements exactly the registry's tools; templates for open cards / numbers (stored fields only, `unsized`) / pool (≤10 names, STALE flag); `radar.pool` goes through the route function itself (a monkeypatched `aset.web.api_radar_pool` is what gets called); a 503 from it is a named failure; no sizer / `/size` / score name in the module's CODE; the figures check (8 cases incl. `4.4` ≠ `4.40`, `440` ≠ `4.40`); a failing `say` is dropped; 8 order phrasings refused WHATEVER the Plan says; 7 trading-logic phrasings → `unsupported` naming `cobalt settings load --card <file> --sha256 <hash> --apply`; 7 ordinary requests NOT refused; a `trading_logic: true` tool is never executed; the dry run (exact change, both hashes, expiry, read-back) and X-X5's 10× guard. RED: `E   ImportError: cannot import name 'tools' from 'cobalt.voice'`. One test of mine then failed on my own docstring (`AssertionError: /size` — the module docstring says "No tool calls `/size`"); the test now reads code only (`inspect.getsource(tl).replace(tl.__doc__, "")`).
### C
`src/cobalt/voice/tools.py` (`code_refusal`, `REFUSE_SENTENCE`, `LOGIC_SENTENCE`, `UNSUPPORTED_SENTENCE`, `figures_ok`, `compose_reply`, `render_*`, `read_open_cards`, `read_pool`, `stop_dry_run`, `STOP_RATIO_GUARD = 10`).
### D
`docs/40 - DevDocs/cobalt/voice/tools.md`.
### SUITE
`uv run pytest -q tests/cobalt/test_voice_tools.py -p no:cacheprovider` → `48 passed in 0.36s`. Full offline (C7 + C8 in the tree) → `2280 passed, 349 skipped, 1 xfailed, 3 warnings in 96.36s (0:01:36)` — failed 0; skipped = BASELINE's 349 (no voice test skipped).
### COMMIT
(below)

## C8
### T
FIRST the pin (`tests/cobalt/test_voice_card_stop.py`): `_render` replaced by a recorder, `CardStore` by a constructed fake, and the route's output for (1) an open card, (2) a card that is not open, (3) a bad decimal, (4) the dev-entry refusal, (5) a store refusal, written as literal strings and run on the BASE code → `5 passed` (the 3 `set_card_stop` tests RED: `ModuleNotFoundError: No module named 'cobalt.aset.card_stop'`). Then the voice act's tests: re-check + one write; a target moved in between → `TargetChanged` carrying the new read-back, nothing written; a card no longer open → refused; in DEV without `COBALT_ALLOW_DEV_ENTRY=1` → `DevEntryRefused` whose text the reply speaks; the act reaches the card only through `set_card_stop(`. RED: `AttributeError: module 'cobalt.voice.tools' has no attribute 'execute_stop'` (×4) and the `set_card_stop(` source check.
### C
`src/cobalt/aset/card_stop.py` (`set_card_stop`, `StopEdit` — the route body `:1247-1257` moved unchanged; `_check_entry_allowed` IMPORTED at call time, never moved or copied; `CardStore` read from `aset.web`'s namespace). `src/cobalt/aset/web.py`: ONE import line + the route body → `edit = set_card_stop(card_id, form.get("stop", ""))`, success banner from `edit.from_stop` / `edit.to_stop`. `src/cobalt/voice/tools.py`: `execute_stop`, `TargetChanged`; `read_open_cards` reads through `aset.web.CardStore` (the sheet's own class). After the extraction: `uv run pytest -q tests/cobalt/test_voice_card_stop.py tests/cobalt/test_aset_web.py` → `46 passed` (the five pins byte-identical), then `13 passed` for the file.
### D
`docs/40 - DevDocs/cobalt/aset/card_stop.md` (new), a dated paragraph in `docs/40 - DevDocs/cobalt/aset/web.md`, `…/voice/tools.md` (execute).
### SUITE
the full offline run under C7 (`2280 passed … failed 0`).
### COMMIT
(below)

### COMMIT (C7, C8)
`2f4ae525 feat(voice-v1): C7 tools …` (4 files, 520 insertions, 1 deletion — it also carries `execute_stop` / `TargetChanged`, written during C8 before the C7 commit) · `f00c37d2 feat(voice-v1): C8 set_card_stop extracted …` (5 files, 298 insertions, 10 deletions).

## C9
### T
`tests/cobalt/test_voice_store.py`: the SQL text (USER side, tenancy shape `user_id INTEGER NOT NULL DEFAULT (current_setting('cobalt.trader_id')::int) REFERENCES "user".traders(id)`, owner `cobalt_user`, the state CHECK = exactly the FINAL §7 states, source / input CHECKs, every column the design names, idempotent CREATEs, touches nothing else, NO `bytea` / `oid` / large object / blob in DDL), registration (last in FORWARD, first in REVERSE, `--down-to 0011` selects it alone), placement, the store's single-flight SQL template, not session-gated, names only its own side, a CLOSED update list, reap limits; `requires_db`: apply + idempotent + rollback drops it cleanly (in a rolled-back migration transaction), the NO-BYTES check over `information_schema.columns` AND `pg_catalog.pg_attribute`/`pg_type` (L35 P-e), round trip + single-flight in the suite transaction, the reaper (transcribing / planned / executing → `failed: reaped_<state>`, an executing row never moved again), single-flight under TWO REAL connections (the X-X13 SQL half). RED: `E   ImportError: cannot import name 'store' from 'cobalt.voice'`.
### C
`src/cobalt/db_migrations/0017_voice_turns.sql` + `.rollback.sql`, `src/cobalt/db_migrations/placement.py` (`CREATED_TABLES["voice_turns"] = Side.USER`), `src/cobalt/voice/store.py` (`VoiceTurnStore`, `TRANSITION_SQL_TEMPLATE`, `UPDATABLE`, `reap_limits`). **Outside the WHAT-YOU-BUILD list, named (ESCALATE):** `src/cobalt/db_migrations/__init__.py` (FORWARD / REVERSE registration — without it `db migrate` cannot apply 0017, which WITH-DB requires) and five existing registry pins, each gaining exactly the one `0017` entry (the setups branch did the same for 0013): `tests/cobalt/test_archiver_migrations.py`, `test_p4_migrations.py`, `test_radar_migration.py`, `test_radar_score_migration.py`, `test_tenancy.py`. First full run after registration: `1 failed, 2356 passed` — `test_radar_score_migration.py::test_rollback_selects_every_newer_migration_then_0007_then_0006_newest_first` (a pin I had missed) → the same one-entry fix.
### D
`docs/40 - DevDocs/cobalt/voice/store.md`; paragraphs in `…/db_migrations/placement.md` and `…/db_migrations/__init__.md`.
### SUITE
`uv run pytest -q tests/cobalt -p no:cacheprovider` → `2357 passed, 355 skipped, 1 xfailed, 3 warnings in 85.32s (0:01:25)` — failed 0; 355 skipped = BASELINE's 349 + the 6 new `requires_db` voice tests (run in WITH-DB).
### COMMIT
`69c376bd feat(voice-v1): C9 migration 0017 "user".voice_turns + the turn store …` (14 files, 648 insertions, 9 deletions).

## C10
### T
`tests/cobalt/test_voice_confirm.py`: `yes` / `Yes.` / `YES` / fullwidth `ｙｅｓ` confirm; `no` forms cancel; "yes please", "yeah", a request containing yes, "you", "" … are `other`; confirm executes once and records the expert's write; a second confirm → `no_pending`; past TTL → `expired`, nothing executed; cancel / other end it; a changed target → `target_changed` + the new read-back; an expert refusal → `failed: expert_refused`, spoken; **X-X13 in memory ×50** (tap Confirm and `no` racing: ≤1 execution, never both states); **X-X13 with-DB ×10** through the real store and two connections (runs in WITH-DB). RED: `E   ImportError: cannot import name 'confirm' from 'cobalt.voice'`.
### C
`src/cobalt/voice/confirm.py` (`normalize`, `classify`, `confirm_pending`, `cancel_pending`, `PendingOutcome`). Normalization STATED: NFKC, casefold, strip whitespace, strip leading / trailing `. , ! ?` — the engine writes "Yes."; X-X1 / X-E2 were counted under this same rule. His R56 clause governs L28 vault edits (V3); this card act keeps FINAL `[F-09]`'s refuse-and-re-confirm (ESCALATE records the reading). X-X1's safe default was NOT needed (0 false confirms), so a spoken `yes` executes.
### D
`docs/40 - DevDocs/cobalt/voice/confirm.md`.
### SUITE
the C9 run (C10's files in the tree): `2357 passed … failed 0`; `uv run pytest -q tests/cobalt/test_voice_confirm.py` → `26 passed, 1 skipped`.
### COMMIT
`53630808 feat(voice-v1): C10 confirm …` (3 files, 358 insertions) · `b0acd0ed chore(voice-v1): X-E4 — the constructed utterance set and the tunables …` (4 files).

## C11
### T
`tests/cobalt/test_voice_turn.py` (26 cases through `run_turn` with an in-memory single-flight store and constructed fakes: template reads; history from THIS session's rows only; an audio turn unlinks its file and records only sha256 / length / duration / `audio_deleted_at`; the file is unlinked and the turn FAILS loud on a transcribe failure (`speech-to-text down (model missing)`, RED), on a Plan failure (`Cobalt can't think right now (unreachable)`), on an exception in between; empty transcript → "I heard nothing." with no Plan call; a clip over `max_clip_s` refused before decode; an act reads back and waits; `yes` confirms with NO model call and executes once; `no` cancels; other words end it unplanned; a confirm word INSIDE a request does not execute; a tap confirms; a tap from another session finds nothing; past TTL → expired, nothing executed; a changed target → the new read-back for re-confirmation; X-X5's guard and "four fifty" clarify; an ambiguous card clarifies; an order refused whatever the Plan; trading logic → `unsupported` row; anything else unsupported; `--dry-run` writes NOTHING and returns plan / resolution / exact change) and `tests/cobalt/test_voice_web.py` (the peer gate: loopback allowed and the turn runs OFF the loop (`asyncio.get_running_loop()` raises in the worker); `192.168.1.5`, `100.64.0.9`, `10.0.0.2`, `testclient` → named 403; a LAN peer with `X-Forwarded-For` / `X-Real-IP` / `Forwarded: for=127.0.0.1` → still 403; every `/voice/*` route gated; the audio part read as bytes; zero-byte → 400 named; a non-file `audio` field → 400 "not a file"; oversize → 413; malformed turns → 400; taps; no `str(v)` in the module; startup sweeps under the lock and shutdown releases; a held lock → `ScratchLocked`, nothing deleted; the app wires router + startup + shutdown; status names a missing model RED). RED: `E   ImportError: cannot import name 'turn' from 'cobalt.voice'` and `… 'web' …`. Two test bugs of mine fixed on the way (a `model_copy` that skipped validation; a missing sheet-config stub).
### C
`src/cobalt/voice/turn.py` (`run_turn`, `TurnInput`, `TurnDeps`, `default_deps`), `src/cobalt/voice/web.py` (router, `peer_gate`, `voice_startup` — lock → side-B sweep → the reaper at start (a DB it cannot reach is a RED status line, never a failed sheet) — `voice_shutdown`, `status_lines`), `src/cobalt/voice/store.py` (`confirm_of` joins `UPDATABLE`), `src/cobalt/voice/agent.py` (`PLAN_SCHEMA` → `plan_schema(agent)`: no config file is read at import any more — the resident imports this through the router). `src/cobalt/aset/web.py`: ONE import, `app.include_router(voice_web.router)`, the startup / shutdown handlers. **Outside the list, named (ESCALATE):** `tests/cobalt/test_radar_panel_cards.py` — `POST_ALLOWLIST` gains `/voice/turn`, `/voice/confirm`, `/voice/cancel` (the explicit POST pin), and the `/radar` byte-equality expectation gains the widget partial before `</body>`.
**X-E6** runs after WITH-DB's migrate (its turns write `voice_turns` rows, and the table exists only after `0017` is applied) — see `### X-E6`.
### D
`docs/40 - DevDocs/cobalt/voice/{turn,web}.md`; `…/voice/agent.md` (`plan_schema`); the "Voice V1 wiring" paragraph in `…/aset/web.md`.

## C12
### T
`tests/cobalt/test_voice_web.py`: the partial renders once on the sheet (`_render`) and on `/radar` before `</body>`; every `fetch('…')` URL in it starts `/voice/`; exactly ONE `speechSynthesis.speak(`, reached only through `getVoices().filter(v => v.localService)`, with the AMBER "no local voice on this device" fallback (a STRING check, stated as such); no card id; hold (`pointerdown` / `pointerup`) and tap on one start/stop, the `isTypeSupported` chain webm/opus → ogg/opus → mp4, Confirm / Cancel, "no microphone on this device", mute; NO `<form` / `method="post"` / `alert(` / `prompt(` / `confirm(` / `.focus(` / `autofocus`.
### C
`widget_html()` in `src/cobalt/voice/web.py` (the partial lives in the router's module, per the prompt's file list); `_render` places it before `</body>`; `GET /radar` injects it into the panel's page after the panel renders (no sheet helper runs — the `/radar` sentinels hold). First full run with the widget: `1 failed, 2420 passed` — `tests/cobalt/test_radar_panel.py::test_panel_has_no_write_or_focus_stealing_markup` → `assert '<form' not in …`: the radar page may carry NO form. The WIDGET changed (a div + a Send button + Enter), not the test; a voice test now holds the partial to the same list.
### D
`docs/40 - DevDocs/cobalt/voice/web.md` (widget section).

## C13
### T
`tests/cobalt/test_voice_cli.py` (the CLI calls `run_turn`; a text turn; `--dry-run` prints plan + change; `--confirm` in production → exit ≠ 0, nothing run; `--confirm` in dev is a tap; `--audio` refuses while a server holds the scratch lock, then takes and releases it; an unknown extension refused; registered on `cobalt`) and `tests/cobalt/test_voice_lifecycle.py` — **X-E7**: (c) grok's case in process (a crash injected after the expert's write and before `done` → the row stays `executing` → the reaper fails it → a second confirm finds `no_pending` → the stop was applied ONCE); (a)+(b) `requires_db` + `slow`: a REAL dev server this test starts on a free loopback port, a ~25 s synthesized clip posted, `kill -9` of THAT pid while the turn runs (< `scratch_max_age_s` after the upload, no later turn) → the file is still on disk → a second server starts → its start sweep deletes the file (side B: every file, whatever its age — the result that would have favoured side A cannot occur) → `.lock` only → the row, past its limit, reaped `failed`. RED: `E   ImportError: cannot import name 'cli' from 'cobalt.voice'`.
### C
`src/cobalt/voice/cli.py` (`cobalt voice turn --text | --audio | --confirm [--dry-run] [--session]`), `src/cobalt/cli.py` (ONE import + `voice_cli.add_parser(sub)`).
### D
`docs/40 - DevDocs/cobalt/voice/cli.md`; the dated paragraph in `…/cobalt/cli.md`.

### SUITE (C11, C12, C13)
Runs in order: `1 failed, 2420 passed` (the radar no-form invariant, above) → widget fixed → `2 failed, 2420 passed` (my own JS COMMENT still contained the literal `<form>`; reworded) → targeted `147 passed, 1 skipped` → full offline `uv run pytest -q tests/cobalt -p no:cacheprovider` → **`2422 passed, 356 skipped, 1 xfailed, 4 warnings in 87.95s (0:01:27)`** — failed 0; 356 = BASELINE 349 + 7 `requires_db` voice tests (store ×5, X13, E7), which run in WITH-DB. The 4 warnings are `PytestUnknownMarkWarning: Unknown pytest.mark.slow` (`slow` cannot be registered without touching `pyproject.toml`, which only N1 may change).
### COMMIT
(below)

## RULE BREACH (recorded when it happened, carried to ESCALATE)
At 14:4x ET (between `date` 14:30:48 and 14:42:18) I issued ONE Bash call outside the allowlist and the UNATTENDED RULES' shape: `sleep 45; tail -c 300 <my own suite's output file>` (chained; `sleep` unlisted). The harness BLOCKED it before execution (`Blocked: sleep 45 followed by: tail … Do not chain shorter sleeps …`); nothing ran; not re-shaped or retried. Not a permission-classifier denial, no dialog. Recorded for the desk to rule whether it counts as an L62 / L63 denial (= FAILED); my reading: a harness block of my own malformed call, no missing permission — the run continued.

## CONTINUE
next: commit C11 + C12 (voice/turn.py, voice/web.py, aset/web.py wiring) and C13 (CLI + lifecycle tests) once the full suite (running) is green; then WITH-DB (migrate → X-E6 → X-X13 / X-E7 with-DB tests → suite), DEMO, CLOSE

(run in progress — next step under ## CONTINUE)
