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

### X-G2/K5
The config refusal `scratch_max_age_s ≤ stt_timeout_s` is a C2 TEST (side B's text keeps it). Under side B the sweep runs ONLY at process start, before the first request is served, so a sweep firing mid-transcribe inside ONE process cannot happen by construction. The cross-process case (an orphan still transcribing while a respawn starts) is X-X22's, and C4's directory lock is its guard. OUTCOME: NO CHANGE (C2 test).

## CONTINUE
next: C1 (tests already written RED — see ## C1 ### T)

(run in progress — next step under ## CONTINUE)
