# mainframe PROMPT 5 — repo-owned chat template, soft switch, log hygiene

Date: 2026-09-09 · Branch: `ops/mainframe-p5` · Worktree: `~/cobalt-wt/ops-mainframe-p5`
Phase A1 by Opus 5 (developer); architect = Fable session.

---

## 0. Headline

Phase A2 ran the probes on the real renderer and caught A1's soft switch **half dead**: LM Studio
normalises a user message's string `content` into a list, so `m.content is string` was false for
every user message and only the system arm fired. Fixed, re-proven on a side instance, 20 tests
green. The `| safe` fix is confirmed in the wild — the upstream cell lost **1 of 10 runs** to it.
`/no_think` cuts a tool-calling turn **21.3 s -> 5.8 s**. Cleanup proven. **ESCALATE: 3 open (4.3, 4.4, 4.5); 4.1 and 4.2 closed.**

---

## 1. Phase A1

### 1.0 Why A1 exists

LM Studio 1.11.0 forwards neither `enable_thinking` nor `reasoning_effort` from the API into the
model's Jinja chat template, so thinking on the mainframe is unconditionally on and no API parameter
can turn it off. A1 took ownership of the template — `ops/mainframe/chat_template.jinja` is the
repo's source of truth and `ops/start_mainframe.sh` installs it into the model directory on every
start and every heartbeat self-heal, with a one-time `.orig` backup and a refuse-on-unrecognised
guard. Two edits vs upstream: the in-band soft switch (`/no_think`, `/think_low`), and dropping the
`| safe` filter that LM Studio's Jinja engine does not have. Three log-hygiene defects went with it.
**Nothing has been deployed.** Phase B is the deploy, and it has not run.

### 1.1 What changed

| File | Status | What |
|---|---|---|
| `ops/mainframe/chat_template.jinja` | new | Upstream + provenance header + soft-switch block + `\| safe` removal |
| `ops/mainframe/install_template.sh` | new | `install_template()`, sourced by both callers; return-based contract |
| `ops/start_mainframe.sh` | modified | install, spinner filter, rotation, no-think probe, honesty fixes |
| `tests/cobalt/test_mainframe_template.py` | new | 17 offline tests (**20 after A2** — §2.0) |

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
    {%- if m.role == 'system' or loop.last %}
        {%- set cobalt_text = render_content(m.content, false) %}
        {%- if '/no_think' in cobalt_text %}{%- set cobalt_sw.no_think = true %}{%- endif %}
        {%- if '/think_low' in cobalt_text %}{%- set cobalt_sw.low = true %}{%- endif %}
    {%- endif %}
{%- endfor %}
{%- if cobalt_sw.no_think %}{%- set enable_thinking = false %}{%- endif %}
{%- if cobalt_sw.low %}{%- set reasoning_effort = 'low' %}{%- endif %}
```

**AMENDED IN A2.** As written in A1 the guard was `(m.role == 'system' or loop.last) and
m.content is string`, which is dead at runtime: LM Studio hands the template a LIST for user
content. The switch now reads through `render_content`. §2.0 has the proof.

Both the header and the block comment are `{#- … -#}` / `{#- … #}` forms, so they contribute zero
bytes to rendered output. `render_content` is the template's own macro (defined above the switch) and
flattens string content, list content and `none` alike — so multimodal messages neither break the
`in` test nor go unread. ~~The `m.content is string` guard is retained~~ — removed in A2, §2.0.

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
the filter was a no-op under jinja2 and fatal under @huggingface/jinja (LM Studio's renderer) — which is exactly why it survived
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

`tests/cobalt/test_mainframe_template.py` — 17 tests as of A1, **20 after A2**, fully offline (no LM Studio, no network, no
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

| case | assertion | added |
|---|---|---|
| A2 | marker in a LIST-shaped last user message → thinking off | A2 |
| A2 | marker in an EARLIER list-shaped message → thinking stays on | A2 |
| A2 | regression: the dead `is string` guard cannot come back | A2 |

```
uv run pytest tests/cobalt/test_mainframe_template.py -q   →  17 passed (A1)
uv run pytest tests/cobalt/test_mainframe_template.py -q   →  20 passed (A2)
```

**A2 re-run (new core, `tests/cobalt`):** **4 failed, 823 passed** — the same 4 pre-existing
`test_herdr_probe.py::TestBeforeTheHandover` failures, +3 from A2. The old tree
(`tests/test_llm.py`, `test_cortex.py`, `test_scribe.py`, `test_finviz_extractor.py`) fails on
environment, not on this change; nothing under `ops/mainframe/` is reachable from it.

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

## 2. Phase A2 — side-instance measurement (COMPLETE)

Run 2026-09-09 11:19–12:05 ET on three side instances built as symlink dirs under
`~/.lmstudio/models/cobalt-test/` (weights symlinked from the real model dirs, only
`chat_template.jinja` a real file). LM Studio assigned the keys `cobalt-test-sw@8bit`,
`cobalt-test-orig`, `cobalt-test-sw@4bit` — **none share the `qwen3.8-27b` prefix**, so
`start_mainframe.sh`'s `MODEL=` prefix match cannot select one. One instance loaded at a time,
`--estimate-only` before every load (38.50 GiB for the 8-bit, 20.97 GiB for the 4-bit; free-ish
43–48 GB throughout).

**Accepted risk, stated:** side instances share LM Studio's `llmster` daemon with production.
"Production untouched" means the model DIR and the `mainframe` identifier, not the process. The
production template sha was `c3cf9e34…` at start AND at end, `com.cobalt.mainframe` was never
touched, and no `launchctl` command was run. Production served 4 read-only completions (the §2.0
(f) control, 3 of which are 400s by design) plus 10 tool-calling runs (cell 1) plus 1 sanity call.

### 2.0 Probes on the real renderer — and the A1 defect they caught

**The A1 soft switch was half dead.** Probe (c) failed on first run: `/no_think` at the end of the
last user message did nothing. Cause, proven below: **LM Studio normalises a user message's string
`content` into a list (`[{"type":"text","text":…}]`) before rendering**, so A1's
`m.content is string` guard — kept deliberately, to stop multimodal content breaking the `in` test —
was FALSE for every user message. Only the system-message arm ever fired. The jinja2 tests passed
because jinja2 was handed the string the API received, not the list LM Studio renders.

Proof, by tokenising the offline render against the live chat API (`/v1/completions`,
`max_tokens 1`, messages `[user "/no_think"]`):

| render path | prompt_tokens | matches live? |
|---|---|---|
| **live LM Studio chat API** | **55** | — |
| offline render, `content` a string | 15 | no |
| offline render + an appended empty assistant message | 64 | no |
| **offline render, `content` a LIST** | **55** | **yes — exact** |

`loop.last` itself is fine: `@huggingface/jinja` 's own `loop.last`, `namespace()`, substring `in`
and `is string` were all exercised directly (`npm i @huggingface/jinja`, offline) and all behave as
jinja2 does. The bug was entirely the `is string` guard meeting list-shaped content.

**Fix (this phase):** the switch reads content through the template's existing `render_content`
macro, which already flattens both shapes — no new helper, one path. Three new tests
(`tests/cobalt/test_mainframe_template.py`, now **20 passed**) cover a marker in a list-shaped last
message, a marker in an earlier list-shaped message, and a regression guard that the dead
`is string` test cannot come back.

Probes after the fix, on `cobalt-test-q8-sw` (`temperature 0`, `max_tokens 64`):

| probe | expectation | before fix | after fix | verdict |
|---|---|---|---|---|
| (a) no marker | think body | `<think>…</think>\n\n4`, 37 ctok | same, 37 ctok | PASS |
| (b) system `/no_think` | no think body | `4`, 2 ctok | `4`, 2 ctok | PASS |
| (c) `/no_think` at END of last user msg | no think body | **`<think>…` 45 ctok — FAIL** | `4`, 2 ctok | **PASS** |
| (d) `/no_think` in an EARLIER msg only | thinking stays ON | `<think>…`, 29 ctok | same, 29 ctok | PASS |
| (e) system `/think_low` | shorter think body | 22 ctok vs 37 in (a) | 22 ctok | PASS |

(e) note: the low-effort instruction shortened the think body by ~40 % (37 → 22 completion tokens)
and the reasoning text visibly drops the "validate assumptions / consider alternatives" preamble.
It is a length effect, not an off switch.

#### (f) — the `| safe` repro, verbatim

Tool-call history `user → assistant tool_call read_file → tool response`, with a `tools` array,
`max_tokens 1`:

| `arguments` in history | `cobalt-test-q8-sw` (repo template) | production `mainframe` (upstream) |
|---|---|---|
| `{"path":"x.py"}` | OK, usage 380 | OK, usage 380 |
| `{"path":"x.py","limit":5}` | **OK, usage 392** | **HTTP 400** |
| `{"path":"x.py","flags":["a"]}` | **OK, usage 394** | **HTTP 400** |

Production's verbatim error, both failing rows:

```
Error rendering prompt with jinja template: "Unknown StringValue filter: safe".
```

`cobalt-test-q4-orig` (4-bit + its upstream template, sha identical to the 8-bit's `c3cf9e34…`)
reproduces production exactly — string OK, int and list 400. `cobalt-test-q4-sw` renders all three.

### 2.1 Tool-calling matrix

10 runs per cell, `/private/tmp/qwen-tooltest` (`alpha.txt`, `beta.txt`, `gamma.txt`),
`qwen --openai-logging -m <id> --approval-mode plan -p "list the files in this directory using
your tool, then reply DONE"`. Scored from the traces, not the prose.

> Harness note: `qwen -m <name>` selects a **provider id**, not an API model name — the first trial
> silently ran against `mainframe`. Cells 2–4 required a project-scoped
> `/private/tmp/qwen-tooltest/.qwen/settings.json` adding one provider per identifier; every trace
> was then asserted to carry the right `request.model`. That settings file (and `QWEN.md`) are part
> of the listed directory in cells 2–4 and are scored as real files. Both were removed at cleanup.

| # | cell | correct listing tool call | malformed schema | hallucinated | DONE | exit 0 | lost to server error | turn-2 `safe` | wall avg (warm) | completion tok avg | API turns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `mainframe` think-on **[production baseline]** | 10/10 | 0/10 | 0/10 | 10/10 | 10/10 | 0/10 | 0/10 | 21.3 s (18.6) | 313.4 | 2.2 |
| 2 | `cobalt-test-q8-sw` + `/no_think` | 10/10 | 0/10 | 0/10 | 10/10 | 10/10 | 0/10 | 0/10 | **5.8 s (5.8)** | **63.3** | 2.0 |
| 3 | `cobalt-test-q4-orig` think-on | 10/10 | 0/10 | 0/10 | **9/10** | **9/10** | **1/10** | **1/10** | 19.5 s (14.6) | 326.8 | 2.7 |
| 4 | `cobalt-test-q4-sw` + `/no_think` | 10/10 | 0/10 | 0/10 | 10/10 | 10/10 | 0/10 | 0/10 | **9.7 s (4.9)** | **71.9** | 2.0 |

"warm" excludes run 1 of each cell — the first request after a load pays 44–63 s of prompt
processing for qwen-code's 27 000-character system prompt.

**`/no_think` assertion (cells 2 and 4):** all 20 requests per cell carried `/no_think` in the
**system** message, injected by qwen-code as `--- Context from: QWEN.md ---\n/no_think`. Verified
from the traces, not assumed. Zero runs emitted a `<think>` body; cells 1 and 3 emitted one in
10/10 and 9/10.

**The `safe` defect, caught in the wild (cell 3, run 3).** Not a synthetic repro — a real seat
death, exit 1, mid-task:

```
[API Error: Error rendering prompt with jinja template: "Unknown StringValue filter: safe".]
```

The trigger was **not** the listing tool. `glob` calls carry `{"pattern":"*"}` — all strings, always
safe. The killer was qwen-code's own bookkeeping call, replayed as history on the next request:

```
update_goal {"status":"complete","reason":"…","evidenceRefs":["w:1","w:2"]}
                                              ^^^^^^^^^^^^ list-valued -> tojson | safe -> 400
```

That is 1 seat death in 10 runs of a trivial read-only task, on the template production is serving
right now. Cells 2 and 4 (repo template) issued the same `update_goal` and rendered it fine.

### 2.2 Thinking probes across the instances

`temperature 0`, `max_tokens 64`, question "What is 2+2? Reply with just the number."

| instance | template | (a) no marker | (b) system `/no_think` | (c) marker in last user msg | (d) marker earlier only | (e) `/think_low` |
|---|---|---|---|---|---|---|
| `cobalt-test-q8-sw` | repo (fixed) | think, 37 ctok | **no think, 2 ctok** | **no think, 2 ctok** | think, 29 ctok (correct) | think, 22 ctok |
| `cobalt-test-q4-sw` | repo (fixed) | think, 36 ctok | **no think, 2 ctok** | **no think, 2 ctok** | think, 26 ctok (correct) | think, 23 ctok |
| `cobalt-test-q4-orig` | upstream | think, 36 ctok | think, 36 ctok — **ignored (expected)** | not run | not run | think, 37 ctok — **ignored (expected)** |
| `mainframe` | upstream | not probed — production budget spent on the (f) control and cell 1 | | | | |

`q4-orig` is the control and behaves exactly like production: the markers are inert text, and the
prompt simply grows by their token cost (65 → 69).

### 2.3 Throughput

"write 500 words about the ocean", `max_tokens 1600`, `temperature 0`, 3 runs each. USEFUL tokens =
tokens after `</think>`; with thinking on the template ends the prompt with `<think>\n`, so
everything emitted is reasoning until that tag appears.

| instance | marker | decode tok/s | completion tokens | **useful tokens** | words | finish | wall |
|---|---|---|---|---|---|---|---|
| `cobalt-test-q8-sw` | thinking on | 22.37 | 1599 | **0** | 0 | `length` | 71.5 s |
| `cobalt-test-q8-sw` | `/no_think` | 22.38 | 785 | **784** | 625 | `stop` | 35.1 s |
| `cobalt-test-q4-sw` | thinking on | 37.61 | 1599 | **0** | 0 | `length` | 42.5 s |
| `cobalt-test-q4-sw` | `/no_think` | 37.64 | 728 | **727** | 604 | `stop` | 19.3 s |

**The 09-08 finding reproduces exactly: 0 useful tokens at 1600 with thinking on**, 3/3 runs on both
quants, deterministic at `temperature 0`. The model spends the entire budget counting words inside
the think block and the essay never begins. Captured tail of a truncated stream:

```
… Count Tides1 rise2 and3 fall4 with5 the6 moon7 influencing8 shorelines9 estuaries10 …
```

Note also: **LM Studio emits no `<think>` tag at all when the block is length-truncated** — it
echoes the opening tag only if `</think>` is reached. Any consumer that strips `<think>…</think>`
and keeps the rest will pass 1 599 tokens of raw reasoning through as if it were the answer. This
is a live hazard for the LiteLLM local route, independent of the template.

Decode rate is unchanged by the marker (22.4 tok/s 8-bit, 37.6 tok/s 4-bit — the 4-bit is **1.68×**
faster). `/no_think` buys latency by not generating the reasoning, not by generating it faster.

### 2.4 `--parallel 1` — speculative decoding

`cobalt-test-q8-sw` reloaded with `--parallel 1 --context-length 32768`, then a prediction with
`draftModel="qwen3.8-27b-mtp"` (LM Studio Python SDK 1.5.0). Verbatim:

```
LMStudioServerError: Completion error:
  Failed to load draft model. SpeculativeDecodingNotSupportedError:
  Speculative decoding is not supported for batched MLX models.
```

`--parallel 1` does **not** unlock it — LM Studio's MLX engine is a batched engine regardless of the
parallel count, and `lms ps --json` exposes no parallel field to confirm otherwise. Baseline on the
same `--parallel 1` instance, no draft head, 400 tokens × 3 runs: **22.45 / 22.80 / 22.80 tok/s** —
identical to the §2.3 figure, so `--parallel 1` costs nothing and buys nothing.

**Verdict: speculative decoding remains unavailable on this stack.** `qwen3.8-27b-mtp` (265 MB) is
dead weight until LM Studio ships a non-batched MLX path.

### 2.5 122B — ON HOLD (inventory)

Deletion is **on hold** (Dejan's ruling, 2026-09-09). Nothing was removed. For the record:

| model | dir | `du -sh` | `lms ls` |
|---|---|---|---|
| `qwen3.5-122b-a10b` | `mlx-community/Qwen3.5-122B-A10B-4bit` | **65G** | 69.62 GB |

65 G is 37 % of the 175 G model tree. Reclaiming it would take the tree to ~110 G. No action taken.

### 2.6 Model inventory

`du -sh ~/.lmstudio/models/*/*`, after cleanup:

| model dir | size | `lms ls` key | loaded |
|---|---|---|---|
| `mlx-community/Qwen3.5-122B-A10B-4bit` | 65G | `qwen3.5-122b-a10b` | |
| `mlx-community/Qwen3.5-35B-A3B-8bit` | 35G | `qwen3.5-35b-a3b` | |
| `mlx-community/Qwen3.8-27B-8bit` | 28G | `qwen3.8-27b` | **✓ `mainframe`** |
| `lmstudio-community/Qwen3.8-27B-MLX-4bit` | 15G | `qwen/qwen3.8-27b` | |
| `mlx-community/Qwen3.5-27B-4bit` | 15G | `qwen3.5-27b` | |
| `mlx-community/Qwen3.5-27B-Claude-4.6-Opus-Distilled-MLX-4bit` | 14G | `qwen3.5-27b-claude-4.6-opus-distilled-mlx` | |
| `mlx-community/Qwen3.5-4B-MLX-4bit` | 2.9G | `qwen3.5-4b-mlx` | |
| `mlx-community/Qwen3.8-27B-MTP-4bit` | 253M | `qwen3.8-27b-mtp` | (unusable — §2.4) |
| **tree total** | **175G** | 9 models / 187.63 GB reported | |

`df -h /`: 926Gi total, 604Gi → **598Gi** available (the data volume holding `~/.lmstudio` reports
296Gi used / 594Gi avail). Nothing was deleted; the delta is unrelated churn.

> `lms ls` reports GB where `du` reports GiB, which is why 175G of disk reads as 187.63 GB. While
> the symlinked side dirs were indexed it reported **249.32 GB / 12 models** — 61.69 GB of it
> phantom, the same weights counted three times. `du` showed those dirs at 12–16 KB.

### 2.7 Cleanup — proven

| check | step 0 | step 8 | |
|---|---|---|---|
| real files under `cobalt-test/` | — | `find -type f` = **3**, all `chat_template.jinja` | asserted **before** `rm -rf` |
| side identifiers loaded | none | none (`lms unload` × 3) | PASS |
| `lms ps` | `mainframe` only | `mainframe` only | PASS |
| `lms ls` | 9 models / 187.63 GB | **9 models / 187.63 GB**, same keys | PASS |
| production template sha | `c3cf9e34…1041` | **`c3cf9e34…1041`** | PASS |
| 8-bit / 4-bit source dirs | 18 / 13 entries | 18 / 13 entries | PASS |
| `memory_pressure` free | 65 % | 64 % | PASS |
| `/private/tmp/qwen-tooltest` | 3 `.txt` | 3 `.txt` (`QWEN.md`, `.qwen/` removed) | PASS |

The `rm -rf` was gated on the `find … -type f` assertion printing exactly the three
`chat_template.jinja` copies; no weight file was ever writable through those dirs, and no `rm` was
run anywhere else under `~/.lmstudio/models/`.

Final production sanity: one read-only completion to `mainframe` returned normally, and the
heartbeat's last cycle (11:35 ET) is green on every row.

> Collateral, disclosed: `/private/tmp/qwen-tooltest/logs/openai/` — 24 stale trace files from the
> 09-08 session — was deleted at setup so it would not pollute the directory listing the models were
> asked to produce. Scratch data in `/private/tmp`, not a repo or vault surface.

---

## 3. Phase B — deploy — RUN 2026-09-09 16:53–16:58 ET, PROVEN on the second start

| attempt | start | template on disk | served template | nothink probe | `/no_think` (b)/(c) | `| safe` repro |
|---|---|---|---|---|---|---|
| 1 | 16:53:48 (merge 3b57442, kickstart) | installed 16:53:54, `.orig` saved | **OLD upstream** | "OK" — FALSE PASS (16-token, tagless open-air reasoning) | thinking still on, 33–45 ctok | still `Unknown StringValue filter: safe` |
| 2 | 16:56:22 (kickstart again) | `template current` | **ours** (`6543c0f4…`) | `nothink probe OK: 4` | `4`, 2 ctok, no tag, both placements | OK, 365 prompt tokens |

**Root cause of attempt 1 (proven, not guessed):** `lms daemon up` indexes every model dir at
startup and `lms load` takes the chat template from that index, not from disk. The script installed
the template 2 s AFTER the daemon came up, so the first load served the index-time (old) template
while `~/.lmstudio/.internal/model-index-cache.json` (rewritten 16:53 by the file watcher) already
carried ours. The second start found the template on disk before the daemon indexed it. Fix in this
commit: `install_template` runs BEFORE `lms daemon up`. No third kickstart is needed — the file is
on disk, and every future start (RunAtLoad, F1 self-heal) indexes it first.

**Second defect, the false PASS:** the probe used `max_tokens 16`; a length-truncated think block
carries no `<think>` tag (A2 finding 4.4), so open-air reasoning read as "no think body". Fixed:
64 tokens, and the verdict requires `finish_reason == stop`, no populated think block, AND the
answer starts with `4`. Attempt 1 would have logged
`WARN: nothink probe — finish_reason=length, content='We need to respond…' — open-air reasoning`.

**Proof after attempt 2:** `lms ps` = `mainframe` only (29.53 GB, 262144); model-dir template
sha `6543c0f4…` = repo template; `.orig` = upstream `c3cf9e34…`; forced heartbeat **GREEN 16:58:06**
(13 jobs / 11 probes); mainframe.log rotated (9.26 MB → `.1`), no spinner lines. Residents
restarted: `com.cobalt.mainframe` only (twice); outage 16:53:48–16:54:04 and 16:56:22–16:56:33.

### 3.1 The original Phase B block (as planned)

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
nothink probe OK: 4                                     <- the acceptance line (A2-proven)
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
# ff-only merge = NO merge commit to revert. Revert the branch commits by range
# (oldest^..tip). Re-verify against `git log --oneline main` before running —
# 8f896c3 stays the oldest; the tip is HEAD of ops/mainframe-p5 at merge time.
# oldest branch commit after the 16:28 rebase = 7887646 ("repo-owned chat template with /no_think soft switch");
# after the ff-only merge main's tip IS the branch tip, so the range is oldest^..main.
cd /Users/cobalt/cobalt && git revert --no-edit 7887646^..main
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

**4.2 — RESOLVED by A2, and it found a real defect.** Raised as: the A1 tests prove the template
under **jinja2**, while LM Studio (a node app) serves it through **@huggingface/jinja**. The gap was
real, but not where it was expected — the engines agree; **LM Studio's own pre-render message
normalisation** (string `content` → list) is what broke the switch. A1's last-message arm never
fired in production. Fixed and re-proven on `cobalt-test-q8-sw`; all six probes green (§2.0). The
standing runtime check is unchanged: the post-load `nothink probe` in `ops/start_mainframe.sh`.
Closed.

**4.3 — `configs/config.yaml` `mainframe.context` (E4) is unverified here.** Untouched by this work;
the existing context WARN still covers it.

---

**4.4 — NEW, for the architect. Thinking-on truncation silently yields raw reasoning.** At
`max_tokens 1600` with thinking on, 3/3 runs on both quants returned **1 599 completion tokens and
0 useful tokens**, `finish_reason: length` — and **LM Studio emitted no `<think>` tag at all**,
because it echoes the opening tag only when `</think>` is reached. A consumer that strips
`<think>…</think>` and keeps the remainder will pass a raw reasoning stream through as the answer.
This is a template-independent hazard on the LiteLLM local route and it survives Phase B. Two
candidate mitigations, architect's call: (a) make `/no_think` the default for programmatic callers,
(b) have the route reject a `finish_reason: length` response that never closed a think block.
Nothing has been changed for this — it is outside A2's scope.

**4.5 — NEW, low. Speculative decoding is dead on this stack, `--parallel 1` included.** Verbatim:
`SpeculativeDecodingNotSupportedError: Speculative decoding is not supported for batched MLX
models.` `mlx-community/Qwen3.8-27B-MTP-4bit` (253 MB) is unusable weight until LM Studio ships a
non-batched MLX path (§2.4). No action taken.

---

## 5. Git state

```
$ git -C ~/cobalt-wt/ops-mainframe-p5 status --porcelain
(clean)

$ git -C ~/cobalt-wt/ops-mainframe-p5 log --oneline main..HEAD
<this report commit>  docs(report): mainframe-p5 phase A2
4ad91bd ops(mainframe): fix the soft switch's dead last-message arm (proven on a side instance)
eb24ff0 docs(report): mainframe-p5 — rollback by commit range (ff-only), renderer = @huggingface/jinja, llmster shared-daemon caveat
41ebd09 ops(mainframe): drop `| safe`, tighten the template recognition gate
caa254a docs(report): mainframe-p5 phase A1
b8f1423 ops(mainframe): install the template, filter the spinner, rotate the log
8f896c3 ops(mainframe): repo-owned chat template with /no_think soft switch
```

(A report cannot name its own sha without changing it, so the tip is left symbolic. The rollback
range in §3 is `8f896c3^..HEAD` at merge time — re-verify against `git log --oneline main..HEAD`.)

`main` is untouched: no commits, no merges, nothing deployed. Nothing was pushed.
