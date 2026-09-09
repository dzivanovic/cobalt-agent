# mainframe PROMPT 5 — repo-owned chat template, soft switch, log hygiene

Date: 2026-09-09 · Branch: `ops/mainframe-p5` · Worktree: `~/cobalt-wt/ops-mainframe-p5`
Phase A1 by Opus 5 (developer); architect = Fable session.

---

## 0. Headline

LM Studio 1.11.0 forwards neither `enable_thinking` nor `reasoning_effort` from the API into the
model's Jinja chat template, so thinking on the mainframe is unconditionally on and no API parameter
can turn it off. Phase A1 takes ownership of the template: `ops/mainframe/chat_template.jinja` is now
the repo's source of truth and `ops/start_mainframe.sh` installs it into the model directory on
every start and every heartbeat self-heal, with a one-time `.orig` backup and a refuse-on-unrecognised
guard that fires on every call.

Two edits vs upstream. The first is the in-band soft switch (`/no_think`, `/think_low`). The second
turned out to matter more: upstream renders tool-call arguments through a `| safe` filter that **LM
Studio's Jinja engine does not have**, so any tool call carrying a non-string argument value fails at
prompt-render time with `Unknown StringValue filter: safe`. That is the defect that killed the Qwen
seat on turn 2 of a read-file task this morning (§1.2).

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
| `ops/mainframe/chat_template.jinja` | new | Upstream + provenance header + soft-switch block + `\| safe` removal |
| `ops/mainframe/install_template.sh` | new | `install_template()`, sourced by both callers; return-based contract |
| `ops/start_mainframe.sh` | modified | install, spinner filter, rotation, no-think probe, honesty fixes |
| `tests/cobalt/test_mainframe_template.py` | new | 17 offline tests |

### 1.2 The template diff vs upstream

Upstream is `mlx-community/Qwen3.8-27B-8bit/chat_template.jinja`, sha256
`c3cf9e34abf4f9e36c2d72165aa9c132d3e2a725b6c2586aaa3a8af9d7a81041` (verified on the copy before
editing). `diff` shows **exactly three hunks — two insertions and one one-token removal**:

```
0a1,26         the provenance header
45a72,85       edit 1: the Cobalt soft-switch block
138c178,185    edit 2: `| safe` dropped (plus its explanatory comment)
```

#### Edit 1 — the soft-switch block, immediately before the untouched `enable_thinking` guard

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

#### Edit 2 — `| safe` dropped: the defect that killed the Qwen seat

Upstream line 138 rendered tool-call arguments as:

```jinja
{%- set args_value = args_value | string if args_value is string else args_value | tojson | safe %}
```

**LM Studio's Jinja engine has no `safe` filter.** The `is string` branch is the only reason anything
ever worked: a tool call whose argument values are all strings never reaches `tojson | safe`. The
moment any argument is an int, list, dict or bool, the render dies.

Reproduced against production with curl (architect, 2026-09-09 09:22):

| tool-call `arguments` in history | result |
|---|---|
| `{"path":"x.py"}` | renders OK |
| `{"path":"x.py","limit":5}` | `Error rendering prompt with jinja template: "Unknown StringValue filter: safe"` |
| `{"path":"x.py","flags":["a"]}` | same error |

**This is why the Qwen seat died on turn 2 of a read-file task this morning.** Turn 1 issues the tool
call and succeeds; turn 2 sends the same call back as *history*, hits line 138, and the whole request
fails at prompt-render time — before the model is reached, so it presents as an API error rather than
a bad completion.

Fix: drop `| safe`. `tojson` already returns a string and nothing autoescapes in this rendering, so
the filter was a no-op under jinja2 and fatal under minijinja — which is exactly why it survived
upstream testing. One token removed; the `is string` branch is untouched.

Five tests cover it (case g, §1.6): a history with int, list, dict and bool arguments plus the tool
response renders without raising and emits the arguments' JSON; a regression test strips Jinja
comments and asserts no `safe` filter has crept back into live template code.

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

**Recognition gate, tightened 09:27 on the architect's ESCALATE 4.1 ruling.** The check that the
template in the model dir is either the pinned upstream or ours now runs on **every call**. It
previously sat inside the `.orig`-missing branch, which meant that once a backup existed a genuine
upstream change was overwritten without a word — the one case the guard was written for.

**Contract:** `install_template` only ever `return`s non-zero; it never calls `exit`. The two callers
need opposite things and now each decide for themselves:

- **main path** → `exit 1`, fail-loud before anything is loaded;
- **heartbeat `reload()`** → logs FATAL and **skips the reload**, so a refusal can never take the
  heartbeat down. The loop keeps running and re-logs every 60 s until a human reviews
  `ops/mainframe/`. Serving a template nobody has reviewed is worse than staying down.

All seven branches exercised in a sandbox (a fake model root; **the real model dir was never written
to**):

| # | scenario | result |
|---|---|---|
| 1 | pristine upstream, no `.orig` | backs up to `.orig`, installs ours — rc 0 — PASS |
| 2 | ours already installed | `template current: <sha>`, no rewrite — rc 0 — PASS |
| 3 | ours installed, `.orig` lost | WARN, continues — rc 0 — PASS |
| 4 | unknown template, no `.orig` | FATAL, rc 1 — PASS |
| 5 | repo template source missing | FATAL, rc 1 — PASS |
| 6 | **model update ships new upstream, `.orig` present** | **FATAL, rc 1, and the new upstream file is left byte-for-byte intact** — PASS (was the hole; now closed) |
| 7 | no template in model dir at all | FATAL, rc 1 — PASS |

Scenario 6's log line:

```
FATAL: model dir template is neither upstream nor ours — a model update shipped
       a new template; review ops/mainframe/ before serving
FATAL:   <target> sha 626a16f4…
FATAL:   expected upstream c3cf9e34…41 or ours f28860a4…
```

One case the ruling did not cover, decided the safe way and flagged: if `install_template.sh` itself
is **missing** at heartbeat time, the fallback stub returns 0 so reloads still happen. The main path
already exits 1 when that file is absent, so reaching this state means it was deleted *after* a good
start — wedging the heartbeat over a repo problem would leave the mainframe down permanently, which
is the wrong side of NN#16. The template simply stops being managed, loudly, every cycle.

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

`tests/cobalt/test_mainframe_template.py` — 17 tests, fully offline (no LM Studio, no network, no
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
| g | tool_call with int/list/dict/bool arguments renders without raising | PASS |
| g | those values appear as JSON; the string branch stays unquoted | PASS |
| g | the tool response renders | PASS |
| g | no `safe` filter in live template code (comments stripped) | PASS |
| g | `/no_think` still works alongside tool calls | PASS |

```
uv run pytest tests/cobalt/test_mainframe_template.py -q   →  17 passed
```

**Full suite, apples-to-apples:**

| | result |
|---|---|
| `main` baseline | **4 failed, 983 passed** |
| `ops/mainframe-p5` | **4 failed, 1000 passed** |

+17 passed = exactly the new tests. The same 4 failures on both sides, all pre-existing and
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

**4.1 — RESOLVED 09:27, ruling: tighten.** Raised as: the unknown-template guard was bypassed once
`.orig` existed, so a model update shipping a new upstream template was silently overwritten. The
architect ruled to tighten — a model update is a deliberate human action and refusing loudly there is
NN#16-correct. Implemented, with `install_template` converted to a return-based contract so the main
path can exit while the heartbeat merely skips the reload. Sandbox scenario 6 now refuses and leaves
the new upstream file intact (§1.4). Closed.

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
