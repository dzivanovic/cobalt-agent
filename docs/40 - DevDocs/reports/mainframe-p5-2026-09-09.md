# mainframe PROMPT 5 — repo-owned chat template, soft switch, log hygiene

Date: 2026-09-09 · Branch: `ops/mainframe-p5` · Worktree: `~/cobalt-wt/ops-mainframe-p5`
Phase A1 by Opus 5 (developer); architect = Fable session.

---

## 0. Headline

LM Studio 1.11.0 forwards neither `enable_thinking` nor `reasoning_effort` from the API into the
model's Jinja chat template, so thinking on the mainframe is unconditionally on and no API parameter
can turn it off. Phase A1 takes ownership of the template: `ops/mainframe/chat_template.jinja` is now
the repo's source of truth (upstream, byte-for-byte, plus one in-band soft-switch block giving
`/no_think` and `/think_low`), and `ops/start_mainframe.sh` installs it into the model directory on
every start and every heartbeat self-heal, with a one-time `.orig` backup and a refuse-on-unrecognised
guard.

Three log-hygiene defects went with it: `lms load`'s TTY spinner (815 lines, ~8.8 MB of a 9.2 MB log)
is now filtered, the log rotates at 5 MB (it never rotated), and two misleading log lines were made
honest.

**Nothing has been deployed.** Production is untouched — no `lms load`, no `launchctl`, no writes
under `~/.lmstudio`, no commits to `main`. Phase B is the deploy, and it has not run.

**Status: Phase A1 complete and green. Phase A2 not started.**

---

## 1. Phase A1

### 1.1 What changed

| File | Status | What |
|---|---|---|
| `ops/mainframe/chat_template.jinja` | new | Upstream template + provenance header + soft-switch block |
| `ops/mainframe/install_template.sh` | new | `install_template()`, sourced by both callers |
| `ops/start_mainframe.sh` | modified | +224 / -5 — install, spinner filter, rotation, probe, honesty fixes |
| `tests/cobalt/test_mainframe_template.py` | new | 12 offline tests |

### 1.2 The template diff vs upstream

Upstream is `mlx-community/Qwen3.8-27B-8bit/chat_template.jinja`, sha256
`c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041` (verified on the copy before
editing). `diff` shows **exactly two hunks, both pure insertions — nothing deleted, nothing altered**:

```
0a1,14      the provenance header
45a60,73    the Cobalt soft-switch block
```

The inserted block, immediately before the untouched upstream `enable_thinking` guard:

```jinja
{%- set cobalt_sw = namespace(no_think=false, low=false) %}
{%- for m in messages %}
    {%- if (m.role == 'system' or loop.last) and m.content is string %}
        {%- if '/no_think' in m.content %}{%- set cobalt_sw.no_think = true %}{%- endif %}
        {%- if '/think_low' in m.content %}{%- set cobalt_sw.low = true %}{%- endif %}
    {%- endif %}
{%- endfor %}
{%- if cobalt_sw.no_think %}{%- set enable_thinking = false %}{%- endif %}
{%- if cobalt_sw.low %}{%- set reasoning_effort = 'low' %}{%- endif %}
```

Both the header and the block comment are `{#- … -#}` / `{#- … #}` forms, so they contribute zero
bytes to rendered output. The `m.content is string` guard is retained: it is what stops a multimodal
(list-shaped) message content from breaking the `in` test, and there is a test for it.

Semantics: the marker is honoured in the **system message or the LAST message only**. A stale
`/no_think` in an old turn does not silently disable thinking for the rest of a conversation — case
(d) below.

**Known cosmetic effect, accepted:** the marker stays visible in the rendered prompt text (the
template renders message content unmodified). This is the standard Qwen in-band convention.

### 1.3 Spinner filter — before/after on real captured output

`lms load` prints a progress spinner with no TTY and offers no quiet flag (its only flags are
`--gpu`, `-c/--context-length`, `--parallel`, `--ttl`, `--identifier`, `--estimate-only`, `-y/--yes`).

The spec'd filter (`tr -d '\r'`) was measured and rejected: each spinner burst arrives as **one
physical line** of CR-separated braille frames, so *deleting* the CR concatenates ~9 000 characters of
frames into a single unreadable line — only a 19 % saving. Approved and shipped instead:
CR→LF, strip ANSI, drop the trailing spinner glyph, `uniq`.

Sample: 20 escape-carrying lines from `ops/logs/mainframe.log` (read-only).

| | lines | bytes |
|---|---|---|
| before | 20 | **226 012** |
| after `tr -d '\r'` (spec'd, rejected) | 20 | 182 048 (−19 %) |
| after shipped filter | 40 | **1 260 (−99.4 %)** |

The shipped filter does not merely shrink the log — it **surfaces signal the raw log buried
mid-line**. First four lines out:

```
Loading qwen3.5-122b-a10b
Model loaded successfully in 26.50s.
Loading qwen3.5-122b-a10b
Model loaded successfully in 25.64s.
```

`Model loaded successfully in 26.50s.` was always in the log; it was unreadable inside a 9 000-char
spinner line. Projected across all 815 escape lines: ~8.8 MB → ~51 KB.

`LC_ALL=C` is deliberate. launchd starts this job with no `LANG`, and the spinner glyphs are
multibyte UTF-8; in C locale sed matches bytes and `[^[:print:][:space:]]` catches them without a
multibyte character range whose behaviour would depend on the inherited locale. Verified under
`env -i` (no `LANG`): byte-identical output.

**Equality proof — the two copies of `strip_tty`.** The filter exists twice by necessity (the main
path, and the heartbeat's separate `bash -c`). Both were extracted and run against the same sample
under `env -i`; output is byte-identical (`cmp` clean, 40 lines / 1 260 bytes each). The heartbeat
copy was extracted from the actual injected subshell body, not retyped.

### 1.4 `install_template()` — sourced, not duplicated

Per the architect's Q2 ruling it lives in `ops/mainframe/install_template.sh` and is `source`d by both
the main path and the heartbeat subshell: one implementation, one place to edit.

All six branches were exercised in a sandbox (a fake model root; **the real model dir was never
written to**):

| # | scenario | result |
|---|---|---|
| 1 | pristine upstream, no `.orig` | backs up to `.orig`, installs ours — PASS |
| 2 | ours already installed | `template current: <sha>`, no rewrite — PASS |
| 3 | ours installed, `.orig` lost | WARN, continues — PASS |
| 4 | unknown template, no `.orig` | `FATAL: unknown template in model dir, refusing`, exit 1 — PASS |
| 5 | repo template source missing | FATAL, exit 1 — PASS |
| 6 | model update replaces upstream, `.orig` present | installs over it — **see ESCALATE 4.1** |

In the **heartbeat**, `install_template` is called inside a subshell so its fail-loud `exit 1` cannot
kill the heartbeat: there, a bad template is logged and the reload proceeds anyway. A loaded model
with a stale template still answers; a dead heartbeat never recovers anything (NN#16).

### 1.5 Other script changes

- **Rotation** — none existed. At start, `> 5 MB` → `mv` to `.1`, rotation notice is the first line of
  the new file. One generation only; `.1` is overwritten each time and nothing older is kept.
- **`stop_previous_heartbeat`** — a pid that no longer exists now says
  `previous heartbeat pid N is gone (nothing to stop)` instead of the misleading
  `not one of ours — left alone` (§12.8 of mainframe-swap-2026-09-07.md). This is the *common* case:
  `kickstart -k` kills the old heartbeat before this script runs.
- **`/no_think` post-load probe** — WARN, never fatal. Correctly treats an **empty** `<think></think>`
  pair as a PASS (that is exactly what the no-think path emits); only a *populated* think body counts
  as "thinking still on". Handles a missing/erroring/malformed response as WARN.
- **Main-path `lms load`** now writes to `mainframe.log` instead of launchd's stdout, so
  `mainframe-boot.log` stops collecting spinner. Its exit status is captured via `PIPESTATUS[0]` and
  logged; the arch/quant verification remains the real gate.

### 1.6 Tests

`tests/cobalt/test_mainframe_template.py` — 12 tests, fully offline (no LM Studio, no network, no
model dir). jinja2 `Environment(trim_blocks=True, lstrip_blocks=True)`, default `Undefined` (strict
would break the template's bare `tools` truthiness test), `raise_exception` stub registered.

| case | assertion | result |
|---|---|---|
| a | no marker → ends `<\|im_start\|>assistant\n<think>\n` | PASS |
| b | `/no_think` in system msg → ends `…<think>\n\n</think>\n\n` | PASS |
| c | `/no_think` in last user msg, no system msg → same as b | PASS |
| d | `/no_think` in an EARLIER msg only → thinking stays ON | PASS |
| e | `/think_low` → exact low string present, xhigh absent, thinking on | PASS |
| — | default effort is xhigh | PASS |
| — | multimodal list content does not break the switch | PASS |
| f | anchor line present exactly once | PASS |
| f | marker block once, immediately before the anchor | PASS |
| f | `start_mainframe.sh` sources the installer, ≥2 install sites | PASS |
| f | installer pins the template path + upstream sha | PASS |

```
uv run pytest tests/cobalt/test_mainframe_template.py -q   →  12 passed
```

**Full suite, apples-to-apples:**

| | result |
|---|---|
| `main` baseline | **4 failed, 983 passed** |
| `ops/mainframe-p5` | **4 failed, 995 passed** |

+12 passed = exactly the new tests. The same 4 failures on both sides, all pre-existing and
unrelated — `tests/cobalt/test_herdr_probe.py::TestBeforeTheHandover`, which still asserts the herdr
plist ships disabled after the 2026-09-08 handover enabled it:

```
E   AssertionError: the plist must not be loaded until the keyboard handover —
    a session that bootstraps it takes down the server hosting itself
E   assert True is False
```

Not fixed here, per instruction.

> **Worktree gotcha, worth recording.** A first run in the worktree gave *32 failed, 59 errors*. Cause:
> `.env` is gitignored, so a fresh worktree has no Postgres credentials and every DB-touching test
> fails `DbConfigError: Missing Postgres settings`. Nothing to do with these changes. The numbers
> above were produced with the credentials supplied through the environment (no secret copied into
> the worktree). `tests/cobalt/conftest.py` hard-pins every new-core test to `cobalt_dev` and raises
> on any other database (RULING 7.1d), so the suite cannot reach prod.

### 1.7 Static checks

- `bash -n ops/start_mainframe.sh` — **OK**
- `bash -n ops/mainframe/install_template.sh` — **OK**
- Heartbeat subshell body extracted from the injected `bash -c '…'` string and `bash -n`'d
  separately — **OK** (4 777 bytes), then its `strip_tty` run for real under `env -i`.
- **shellcheck: not installed on this box** (`command -v shellcheck` → nothing). Not installed (L15,
  no third-party code). `bash -n` only.

---

## 2. Phase A2 — NOT STARTED (placeholders)

To be run on a side instance, not on the production `mainframe` identifier.

### 2.1 Tool-calling matrix

| cell | correct tool call | malformed | hallucinated | DONE | exit 0 | wall clock avg | completion tokens avg |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 2.2 Thinking probes

| instance | marker | completion_tokens | think body? |
|---|---|---|---|
| | | | |

### 2.3 Throughput

| instance | marker | decode tok/s | useful tokens post-strip |
|---|---|---|---|
| | | | |

### 2.4 `--parallel 1` result

_TBD._

### 2.5 122B deletion proof

_TBD._

### 2.6 Model inventory

_TBD._

---

## 3. Phase B — deploy (NOT RUN)

Outside market hours only.

```bash
# 1. merge (fast-forward only)
cd /Users/cobalt/cobalt
git merge --ff-only ops/mainframe-p5

# 2. restart the mainframe job
launchctl kickstart -k gui/$(id -u)/com.cobalt.mainframe

# 3. watch
tail -f "/Users/cobalt/cobalt/ops/logs/mainframe.log"
```

**Log lines to expect, in order:**

```
rotated: previous log was 9246952 bytes (> 5242880) -> …/mainframe.log.1
=== start_mainframe.sh starting (pid N) ===
purging lingering LM Studio processes for warm-boot safety
previous heartbeat pid N is gone (nothing to stop)      <- new wording
starting LM Studio daemon and server
waiting for LM Studio API on port 1234 (60s timeout)
template: backed up upstream template to …/chat_template.jinja.orig
template installed: <sha of ops/mainframe/chat_template.jinja>
API online — loading model into VRAM
Loading qwen3.8-27b                                     <- filtered, a few lines not thousands
Model loaded successfully in NN.NNs.
verified: 'mainframe' = qwen3_5/8bit at context 262144
nothink probe OK: 4                                     <- the acceptance line
model loaded — spawning heartbeat (60s ping, logged, self-healing)
heartbeat running as pid N (pidfile …)
```

The rotation fires on the **first** run (the live log is 9.2 MB). `nothink probe OK` is the acceptance
signal; `WARN: nothink probe — thinking still on (template not in effect?)` means the template did not
take and Phase B should be rolled back.

**Rollback (one command block):**

```bash
cp "/Users/cobalt/.lmstudio/models/mlx-community/Qwen3.8-27B-8bit/chat_template.jinja.orig" \
   "/Users/cobalt/.lmstudio/models/mlx-community/Qwen3.8-27B-8bit/chat_template.jinja"
cd /Users/cobalt/cobalt && git revert --no-edit <merge-sha>
launchctl kickstart -k gui/$(id -u)/com.cobalt.mainframe
```

**Residents:**

- **RESTARTED:** `com.cobalt.mainframe` only.
- **NOT restarted but affected for ~40 s** (the model reload window): `com.cobalt.agent`, the Qwen1
  seat, and the F18 mainframe probe. Any LLM call in flight during the window fails; all three
  recover on their own.

---

## 4. ESCALATE

**4.1 — the unknown-template guard is bypassed once `.orig` exists.** Sandbox scenario 6: with a
`.orig` already present, a *model update that ships a new upstream template* is silently overwritten
by ours, because the refuse-on-unrecognised check only runs inside the `[ ! -f "$target.orig" ]`
branch. That is as specified, and I implemented it as specified rather than changing it unilaterally —
but it is a real hole, and it is the exact drift this work exists to end. Tightening it (compare the
target against upstream **and** ours on every run) trades that silence for a mainframe that refuses to
start after a model update, which is an NN#16 call for the architect, not for me.

**4.2 — the minijinja gap is not closed by Phase A1.** These tests prove the template under
**jinja2**; LM Studio serves it through **minijinja**. `namespace()`, `is string`, and `in`-on-string
are compatible but are not the same implementation. **Phase A2 loads the repo template on a side
instance (`q8-sw`) and runs the thinking probes there before Phase B**, and the post-load `nothink
probe` is the standing runtime check thereafter. Until A2 runs, the soft switch is unproven on the
real renderer.

**4.3 — `configs/config.yaml` `mainframe.context` (E4) is unverified here.** Untouched by this work;
the existing context WARN still covers it.

---

## 5. Git state

```
$ git -C ~/cobalt-wt/ops-mainframe-p5 status --porcelain
(clean)

$ git -C ~/cobalt-wt/ops-mainframe-p5 log --oneline main..HEAD
98f385b docs(report): mainframe-p5 phase A1
68f5c1f ops(mainframe): install the template, filter the spinner, rotate the log
369bb6c ops(mainframe): repo-owned chat template with /no_think soft switch
```

(The report commit's own sha is the one this line was written under; it changes when this
paragraph is amended in.)

`main` is untouched: no commits, no merges, nothing deployed.
